[referencia=e3019f635a854c51 score=0.923]
#### **5.4.2 Efficient inference methods**

To reduce the inference latency, efforts can be categorized into three areas: system-level optimization, algorithm-level optimization, and KV cache optimization.

**System-level optimization.**
 To mitigate the high inference costs associated with long-chain reasoning, several system-level optimization strategies have been developed. A primary focus has been on accelerating kernel execution by minimizing memory movement during attention computation, with FlashAttention being a prominent example [

166
]. Parallel efforts target memory efficiency, such as PagedAttention’s approach to KV cache management, which reduces fragmentation and overhead [

289
]. Furthermore, dynamic workload challenges are addressed through optimized data scheduling and batching techniques, improving hardware utilization [

290
]. In a recent advance, DeepSeek-V3 introduced an expert-parallelism load balancer (EPLB) that alleviates serving-time imbalance by dynamically duplicating and heuristically reassigning overloaded experts across GPUs [

40
]. Collectively, these system-level improvements significantly reduce inference latency and increase serving throughput.

**Algorithm-level optimization.**
 This approach accelerates de-coding by reducing computation across tokens or within the model. A representative example is 

*speculative decoding*
 [

291
–

292
], which uses a small draft model to generate multiple token candidates that are later verified by the target LLM. Subsequent studies further reduce overhead by employing smaller draft models [

293
] or by using output consistency to decide whether generation should continue with the weaker model or the stronger model [

294
]. As another line of work, early exit techniques [

295
] reduce computation within the model by skipping layers or selectively activating them based on prediction confidence.

**KV cache optimization.**
 The KV cache has become a major bottleneck for efficient inference, especially for long-context generation, due to its memory growth with sequence length. Recent work tackles this problem through optimizations at three levels. At the token level, token dropping [

296
] removes low-attention tokens, while softer alternatives [

297
] compress the KV cache using quantization or low-rank decomposition instead of removing them. At the model level, KV cache reduction can be achieved through architectural modifications, such as layer-wise KV sharing [

298
] and multi-head latent attention (MLA) [

67
,

299
]. At the system level, techniques like paged memory management [

300
] and KV access scheduling [

301
] reduce overhead during batched inference.

---

[referencia=e3019f635a854c51 score=0.883]
#### **5.4 Efficient deployment and inference**

In this section, we first introduce the major deployment issues and then discuss the optimization techniques for addressing these challenges.

#### **5.4.1 Deployment issues**

In real-world deployment, LLMs confront two primary challenges: significant memory demands and high inference latency. The first challenge arises from the massive scale of LLMs, which consist of billions or even trillions of parameters [

287
]. Storing these parameters requires substantial memory, leading to increased deployment costs, particularly in production environments [

26
,

40
]. The second challenge, high inference latency, stems from the autoregressive nature of LLM text generation. During inference, the model generates tokens sequentially, sampling each new token using strategies such as greedy search, beam search, or random sampling [

13
,

39
]. This process involves two main stages: The 

*prefill*
 stage processes the input prompt, computes initial states, and caches key-value tensors (

*a.k.a.,*
 KV cache) for efficient reuse. The subsequent 

*decoding*
 stage generates tokens autoregressively, updating the KV cache at each step while producing the next token until completion. Crucially, the decoding stage is 

*memory-bound*
—performance is limited by the GPU’s memory bandwidth rather than compute throughput. This bottleneck, known as the “

*memory wall*
” [

288
], results in inefficient hardware utilization and significantly increases latency, especially for long sequences. Therefore, optimizing LLM inference requires addressing both memory consumption and the inefficiencies of autoregressive decoding.

---

[referencia=e3019f635a854c51 score=0.352]
#### **5.4.3 Compression methods**

In addition to reducing inference latency, minimizing memory usage has also been a key challenge in LLM deployment.

**Quantization methods.**
 Quantization [

302
] is a fundamental technique in neural network compression that reduces the precision of numerical representations to lower memory and computational costs. In LLMs, quantization is primarily applied to two types of data: model weights and activations. The process typically proceeds by scaling and rounding original values to discrete integer levels, followed by dequantization to approximate the original computation during inference. In practice, 

*post-training quantization*
 (PTQ) has become a widely adopted approach, as it avoids full retraining and scales effectively to large models. Overall, empirical studies show that LLM weights are relatively robust to low-bit quantization, with even 4-bit precision maintaining strong performance in key capabilities such as ICL [

303
–

304
], whereas activation quantization, particularly for the KV cache, remains comparatively more challenging due to the presence of outliers in activation distributions [

303
]. For weights, a representative approach is to achieve efficient low-bit quantization through layerwise reconstruction [

304
]. To further reduce the quantization error, recent studies propose to protect important weights that are more sensitive to quantization, known as 

*salient weights*
 [

305
–

306
]. For activation quantization, one straightforward approach bypasses the impact of activation outliers by explicitly preserving them, as in the mixed-precision decomposition [

307
]. More recent methods instead mitigate the outliers through transformations before quantization, including Hadamard transformations [

308
] and learned rotations [

309
], making low-bit end-to-end quantization increasingly practical.

**Other compression methods.**
 In addition to quantization, distillation and pruning have also been explored to reduce the overall footprint of LLMs. Distillation compresses a large model by transferring its capabilities to a smaller one, either by aligning internal features [

310
] or learning from the model’s outputs [

311
]. In contrast, pruning reduces parameter count by removing less important components, either at the weight level [

312
] for high sparsity or at the structural level for hardware efficiency, such as removing Transformer layers [

312
] or MoE expert modules [

---

[referencia=e3019f635a854c51 score=0.325]
#### **3.2.1 Attention**

The core of the attention mechanism lies in its ability to explicitly model relationships between any two tokens in a sequence, enabling it to capture sequence semantics more effectively. Its expressive power is further enhanced through multi-head projections, which map hidden states into queries, keys, and values across multiple subspaces. However, the original implementation suffers from quadratic complexity with respect to sequence length, and storing the full key-value (KV) cache for all attention heads imposes significant memory overhead. We now turn to discuss important improvements to the original Transformer architecture.

**Sparse attention.**
 Attention modules in LLMs exhibit inherent sparsity, with most attention concentrated on a limited set of tokens. To leverage this property, sparse attention mechanisms have been developed, allowing each query to attend to only a selected subset of keys and values instead of the entire sequence. In particular, location-based sparse attention restricts each token’s attention to specific positions, such as initial tokens and those within a recent sliding window, achieving 

 inference and memory overhead [

68
,

77
]. To address the limitation of location-based methods in capturing long-range dependencies, another approach partitions sequences into blocks and selects those most relevant to the current token for attention computation, as seen in methods such as MoBA [

69
], NSA [

70
], DSA [

78
], and HySparse [

79
]. Sparse attention is now widely integrated into LLMs to enhance computational efficiency, including models like MiniCPM4 [

80
], Kimi [

69
], and DeepSeek V3.2 [

78
].

**Attention grouping and compression.**
 Another line of research focuses on grouping or compressing attention heads to reduce computational and memory demands. Intra-layer attention grouping methods (e.g., GQA [

65
], MQA [

66
]) typically partition the attention heads within a layer into several groups, with heads in the same group sharing their key and value projection matrices and the associated KV cache. Additionally, cross-layer attention grouping approaches reuse the KV cache or even the attention scores from earlier layers in subsequent layers, further reducing memory and computational costs [

81
,

82
]. Attention decomposition techniques, such as MLA [

67
], TPA [

83
], and MFA [

---

[referencia=e3019f635a854c51 score=0.225]
#### **3.2.4 Alternative architecture design**

Beyond standard architectural enhancements, the recent literature has introduced a number of emerging designs aimed at improving Transformer performance.

● Residual connection. Typically, existing LLMs use residual connections to create direct pathways for gradients and representations during training, thereby improving optimization [

119
,

120
]. However, recent work finds that the design of the vanilla residual connection may cause unstable training in deep networks [

99
,

121
]. Thus, they add a scaling factor to the residual stream or adjust the placement of normalization within the residual [

12
,

122
,

123
]. In addition, a recent line of work (e.g., Hyper-Connections [

124
] and mHC [

125
]) has identified the phenomenon of representation collapse in existing residual designs and expanded the width of the residual stream. These approaches maintain multiple independent streams, dynamically combine them as input, and update them based on layer outputs, which significantly enhances model performance.

● Memory augmentation. To scale model capacity under limited computational budgets, memory-augmented architectures offer an alternative to standard MoE. These methods maintain large parameterized KV pairs and activate subsets dynamically according to the current hidden state [

126
–

128
]. Other approaches integrate embedding modules in each layer and trigger them based on the current token and local 

-grams [

129
,

130
]. Such embeddings can reside on CPU memory and be transferred to the GPU only upon activation, keeping device memory usage low.

● Looped Transformer. As an important extension, recurrent mechanisms have been incorporated into Transformer architectures [

131
–

133
] by reusing weights across layers. This approach has been shown to improve the performance of smaller models on certain reasoning tasks such as ARC-AGI. However, existing looped Transformer methods generally remain less competitive on standard benchmarks. Extending looped designs to larger-scale models represents a promising direction for further advancing the reasoning capabilities of LLMs.

● Diffusion language models. In addition to the autoregressive (AR) paradigm, the training objective of masked language models has been successfully adapted to natural language modeling, giving rise to diffusion language models (DLMs) [

134
]. DLMs inherently support high computational parallelism in predicting multiple tokens at one time, but they are often compute-bound during decoding, requiring more FLOPs per token and thus limiting their practical efficiency. To address this issue, block based diffusion [

---

[referencia=e3019f635a854c51 score=0.135]
#### **5.3.2 Advanced agentic architectures and techniques**

This part highlights three important techniques that augment agent capabilities: long-context management, agentic self-evolution, and multi-agent collaboration.

**Long-context management.**
 Handling long-range dependencies and extended interaction histories is critical for agents that must maintain coherent behavior over prolonged time horizons. Existing strategies for long-context management in agentic systems can be broadly grouped into two paradigms. The first paradigm focuses on 

*in-context compression and reconstruction*
, where past trajectories are summarized, folded, or iteratively synthesized into bounded representations that prevent uncontrolled context growth. This includes hierarchical context folding techniques [

272
] and iterative synthesis frameworks such as IterResearch [

273
], which periodically condense interaction history into an evolving report and reconstruct the reasoning workspace. The second paradigm introduces 

*external memory*
 that store past information in structured or unstructured forms and enable selective retrieval of context relevant to the current decision. Typical examples include targeted attention over persistent memory [

274
], reversible memory architectures [

275
], and sparse context invocation strategies [

276
]. By retrieving only the information relevant to the current decision, these approaches avoid processing the entire interaction history, thereby reducing computational cost while still maintaining awareness of long-term context. Together, these two paradigms provide complementary mechanisms for maintaining continuity over extended horizons, enabling sustained reasoning and progressive planning in long-running agentic tasks.

**Agentic self-evolution.**
 Recent research has shifted toward enabling agents to autonomously self-improve when provided with suitable interactive environments. These self-evolutionary approaches investigate mechanisms for agents to continuously refine their planning, decision making, and reasoning policies using feedback from interaction outcomes, internal evaluations, or accumulated experience [

277
–

278
]. Among them, experience-driven learning has received particular attention, exploring how diverse forms of generated experience—such as online interactions, historical trajectories, curated replay, and task-specific evaluation loops—can guide subsequent behavior and policy updates [

279
–

281
]. This process is often facilitated by external memory systems that store and structure past interactions. Together, these advances are transforming agents from static, inference-based systems into progressively adaptive, self-improving entities capable of greater robustness and sustained performance growth in dynamic environments.

---

[referencia=e3019f635a854c51 score=0.118]
### **2 Key concepts and background**

In contemporary literature [

13
,

15
], large language models (LLMs) primarily refer to Transformer-based neural networks with parameter counts in the billions or more. Typically, these models are pre-trained on vast amounts of unlabeled natural language text and then post-trained to adapt to real-world applications and ensure safe deployment. While there is no universally accepted criterion for parameter threshold for LLMs, this survey focuses on models with at least several billion parameters, thereby distinguishing modern LLMs from earlier, smaller-scale language models such as BERT and BART. This section introduces key concepts and background necessary for understanding and building LLMs.

**Transformer architecture.**
 Transformer [

12
], a neural network architecture built entirely on attention mechanisms, has become the cornerstone of LLMs. In contrast to traditional recurrent and convolutional neural networks, Transformers explicitly model pairwise relationships between all elements in a sequence, leading to significantly enhanced expressive power. This design yields two critical benefits: (1) 

*inherent parallelizability*
 that leverages modern parallel computing infrastructure, and (2) 

*exceptional scalability*
 to billions of parameters—both indispensable for cutting-edge language model development. While the original Transformer employs an encoder-decoder structure, used by early models like T5 [

21
] and BART [

22
], most contemporary LLMs (e.g., the GPT family) adopt a causal decoder-only architecture [

13
,

16
]. An intermediate alternative, known as the 

*prefix decoder*
 (or 

*non-causal decoder*
) [

23
,

24
], modifies the causal decoder to enable bidirectional attention on prefix tokens while maintaining unidirectional masking for autoregressive generation. Despite extensive earlier exploration of alternative designs, the causal decoder architecture has now become the de facto standard for LLM development.

**Training paradigm.**
 The predominant training approach for modern language models is autoregressive language modeling, which sequentially predicts each token in a text via 

*next-token prediction*
 [

16
]. Despite its conceptual simplicity, this formulation offers a powerful and generalizable method for learning from large-scale unlabeled text. Resembling multitask learning, accurately predicting each token encourages the development of diverse abilities and knowledge. When trained on vast and varied datasets, this approach enables LLMs to acquire versatile, transferable skills applicable to a broad spectrum of real-world scenarios [

---

[referencia=e3019f635a854c51 score=0.073]
#### **3.2.2 Positional encoding (PE)**

To capture positional information, vanilla Transformer uses absolute PEs, which are added to the input token embeddings. However, absolute PEs struggle to represent relative positions and generalize to longer sequences. This limitation has prompted research into improved methods for PEs, as discussed below.

**Rotary PE (RoPE).**
 RoPE [

74
] is a fundamental component widely adopted in modern language models, employing specific rotary matrices based on the absolute position of each key or query. It allows scores between keys and queries to be computed using relative position information. Furthermore, the context windows of RoPE-based models can be extended by preventing out-of-distribution rotary angles. Some methods, such as PI [

103
] and SelfExtend [

104
], reorganize positional indices to ensure they remain within context lengths. Meanwhile, another line of research, including ABF [

105
], YaRN [

101
], and LongRoPE [

106
], modifies the basis of rotary matrices to achieve different interpolation ratios across dimensions, enabling longer context windows. For example, Qwen2.5-7B adopts RoPE and further employs ABF to support a context window of 128K tokens.

**Length extrapolation PE.**
 Relative PEs [

21
] typically incorporate position-based biases into attention values, enabling models to process text beyond their original context length, a capability known as 

*length extrapolation*
. To further enhance this ability, various PE methods introduce a linear penalty factor proportional to the relative distance to adjust the attention scores, encouraging greater reliance on local information (e.g., ALiBi [

75
] and KERPLE [

107
]). For example, ALiBi has been adopted by BLOOM [

108
] for achieving strong extrapolation capabilities. However, research has demonstrated that these methods approximate sliding-window attention, which still struggles to utilize long-range information from previous contexts [

109
]. Thus, designing better PE—both theoretically and empirically—to achieve effective length extrapolation and efficient utilization of global information under an infinite context window remains a key challenge for future research.

**Contextualized PE.**
 To achieve more powerful representational capacities, recent research has proposed contextualized PE that incorporate semantic information. One class of methods builds upon relative PE by integrating positional and semantic information to compute bias values and vectors [

76
]. Alternatively, another approach treats PEs as hidden states, which are dynamically updated through interactions with semantic representations [

110
].

---

[referencia=e3019f635a854c51 score=0.040]
78
,

137
]. A key format for such data is long CoT trajectories, which help build foundational capacities during mid-training that are essential for effective post-training of reasoning models. This fosters a tighter feedback loop between mid-training and post-training: mid-training injects and expands foundational reasoning capacities, enabling models to internalize new reasoning strategies as they evolve, while post-training incentivizes effective behavior patterns. Finally, mid-training can be typically organized as a staged curriculum, allocating dedicated token budgets across different reasoning and planning skills so that competence grows progressively while minimizing destabilizing distribution shifts.

**Long-context adaptation.**
 Another key objective of mid-training is to extend the model’s context length to support downstream tasks, as expanding context during early pre-training is prohibitively resource-intensive. This practice has become standard for most mainstream LLMs and requires specific adaptation strategies. For example, some methods apply techniques like ABF to adjust the rotary base, better aligning positional encoding with longer training contexts [

137
,

138
]. Architectural modifications can further improve efficiency: DeepSeek-V3.2 [

78
], for instance, switches from the full attention used in pre-training to a sparse attention mechanism during mid-training. This strategy preserves the model’s core capabilities while significantly reducing the computational cost of long-context adaptation. Beyond architectural adjustments, effective long-context adaptation also requires sufficient exposure to long sequences. In practice, most open-source models perform mid-training on data with context lengths ranging from 32K to 200K tokens. A length-based curriculum is commonly adopted, wherein the context window is progressively extended during training. Moreover, achieving the model’s maximum context length typically requires a substantial amount of dedicated training (e.g., 50B tokens) [

138
]. For further details on the composition of mid-training data, we refer readers to the discussion in Section 3.4.1 and Section 3.1.3.

---

[referencia=e3019f635a854c51 score=0.039]
● General pre-training curriculum. A common strategy involves dividing the pre-training process into multiple phases (e.g., 27 phases of 40B tokens for YuLan-Mini [

41
]) while systematically varying the proportions of different data sources across these phases. Generally, data should be sequenced according to its inherent complexity, with reasoning-focused data predominantly utilized in later phases. These phase-specific data distributions can be refined through empirical evaluations on development datasets or optimized using specialized models. Crucially, the data distribution should change only gradually between training phases to ensure stability. In addition to curricula that rely on manually designed proxy metrics (such as data complexity), recent work has explored approaches driven by training signals. For instance, In-Run Data Shapley approximates the loss difference before and after training via a Taylor expansion, enabling real-time estimation of each data point’s contribution with little additional training overhead [

50
]. Motivated by this idea, OPUS introduces a step-wise, optimizer-aware data curriculum and leverages soft sampling to maintain diversity while mitigating redundancy [

51
]. To further enhance base model performance, researchers have introduced an annealing strategy that incorporates specially curated data (e.g., instruction data) during the final stages of pre-training while employing a decaying learning rate [

52
]. Empirical evidence demonstrates that this annealing approach can substantially improve model evaluation performance [

39
,

41
,

52
]. Similar curriculum-based strategies can be effectively applied to continual pre-training scenarios (e.g., adapting a code model for specialized math domains through increased exposure to mathematical data [

30
]).

● Long-context pre-training curriculum. The deployment of LLMs requires handling very long input contexts, whether in multi-turn dialogues, lengthy documents, or even book-length inputs. Regarding efficient long-context training, it typically adopts a curriculum learning strategy by progressively increasing context length. For example, Qwen2.5-1M [

26
] follows a four-stage schedule (i.e., 32K → 65K → 131K → 262K) while maintaining a mix of 40% full-length and 60% short sequences in each batch to prevent catastrophic forgetting. At each stage, specific text data of the expected length should be prepared accordingly. Typically, existing work upsamples natural long texts or concatenates short text data from the same distribution as the pre-training dataset to form long texts [

53
,

---

[referencia=e3019f635a854c51 score=0.036]
81
,

82
]. Attention decomposition techniques, such as MLA [

67
], TPA [

83
], and MFA [

84
], apply low-rank or tensor decompositions to queries, keys, and values, achieving a balance between efficiency and performance. For example, GQA has been adopted by LLaMA-3.1 and Qwen2, while MLA has been employed in DeepSeek-V3.

**Linear attention.**
 As the required context length continues to grow, linear attention (LA) [

71
] has re-emerged as an attractive attention alternative with sub-quadratic complexity. Throughout both training and inference, linear attention maintains only a fixed-size matrix-valued recurrent state, which is updated recurrently to learn the mapping from keys to values. From an online-learning perspective, these models can be broadly categorized into three progressive generations. The first generation, including RetNet [

85
], Lightning Attention [

86
,

87
], and RWKV-4 [

88
], updates the state using a data-independent forget gate. This is equivalent to adding a Frobenius-norm penalty on the state to the online-learning objective. Building on this, the second-generation models such as Mamba [

72
] and Mamba-2 [

89
] employ a data-dependent forget gate, which helps mitigate the forgetting dilemma. Most recently, the third generation [

90
–

93
] adopts the 

*delta rule*
 as the state-update equation: old memory is first removed from the state, and then new memory is added [

73
]. This corresponds to changing the online-learning objective from an inner-product loss to a squared loss, thereby preventing the state from diverging to infinity. Despite successive generations of development, linear attention still faces a fundamental trade-off between memory capacity and expressiveness. As a result, most models, such as MiniMax-M1 [

94
], Qwen3-Next [

95
], and Kimi Linear [

92
], mix linear attention with full attention at a fixed ratio, typically 3:1. Recently, an alternative line of research has sought to enhance expressiveness through nonlinear RNN-based models [

96
–

98
], which remain less widely adopted in practice due to the additional effort required to attain computational efficiency.

**Other enhancement techniques.**
 Beyond efficiency-focused variants, another technical direction seeks to address inherent limitations within the attention mechanism itself, aiming to enhance its expressive capability. Existing research has identified issues such as

---

[referencia=e3019f635a854c51 score=0.030]
### **7 Research challenges and open issues**

This section provides an overview of several critical research challenges and open issues in LLMs.

**Theoretical foundations.**
 The rise of LLMs represents a profound methodological shift in AI—from focused optimization on narrow, task-specific data to a universalist paradigm rooted in the self-supervised prediction of natural language text [

13
,

347
]. Despite transformative empirical results, fundamental theoretical questions remain unresolved: How does next-token prediction on unlabeled data at scale give rise to general-purpose capabilities? How do Transformer architectures form and dynamically compose internal representations for semantic modeling? And how does prompting functionally steer model behavior to perform target tasks? Current analyses, including mechanistic interpretability, yield only fragmented, post-hoc insights rather than a predictive, first-principles theory of capability formation. Developing a rigorous theoretical foundation is therefore essential to transition from heuristic scaling to principled design, ultimately enabling reliable generalization, process-aware verification, and intentional steering of future models.

**Architecture innovations.**
 The standard Transformer architecture is constrained by the quadratic computational complexity of its self-attention mechanism [

12
]. While efficiency-focused modifications like sparse or linear attention alleviate this issue [

78
,

92
,

95
], they often struggle to maintain a favorable trade-off between performance and efficiency over extremely long contexts, or require substantial engineering effort to adapt for long-context deployment. The Transformer architecture also shows weaknesses in areas such as factual recall and compositional reasoning [

130
,

132
]. Guiding next-generation designs therefore demands a holistic reassessment of these core capabilities, backed by thorough evaluation and systematic diagnosis. Moreover, progress in this direction faces a major practical barrier: the prohibitively high cost of testing new architectures at scale, a challenge even for industrial labs. To manage this, a 

*scaling ladder*
 approach has become standard practice: experiments are designed to grow gradually, with each phase of scaling contingent on clear success from the preceding one. Another promising path is the co-design of algorithms and hardware for natively optimized systems [

40
], especially as isolated algorithmic improvements become saturated or harder to achieve. Ultimately, moving beyond these limits is necessary to build the more powerful, efficient, and capable systems that next-generation AI requires.

**Scaling enhancement.**
 Scaling serves as the foundational paradigm in LLM development. It is governed by the principle of converting growing computational resources into enhanced model capability—a core tenet of “

*The Bitter Lesson*
” [

---

[referencia=e3019f635a854c51 score=0.030]
#### **3.4.1 Mid-training data**

Mid-training aims to bridge the gap between general pre-training and downstream performance by exposing models to data that systematically covers a wider spectrum of target capabilities, particularly those that are challenging to distill from general web corpora alone, such as mathematical reasoning, competitive coding, long-context understanding, and agentic tasks [

137
,

138
].

Early methods for mid-training data curation prioritized high-value sources by up-sampling domain-specific corpora and curated reasoning data, particularly those with CoT trajectories, to strengthen relevant analytical and reasoning capabilities in specific domains [

30
,

176
]. As research expanded toward more interactive and multi-step tasks, recent studies have incorporated agentic tasks, often by generating corresponding trajectories, to better train models on such scenarios [

137
–

138
]. To more efficiently determine optimal data mixtures, recent methods such as MergeMix first train domain-specific models, then employ model merging to learn the weights that define the final data blend [

49
].

To achieve sufficient scale while preserving quality, modern mid-training mixtures increasingly rely on large-scale synthetic data, where constraints such as atomic skill definitions or curriculum structures guide the synthesis process. For example, GLM-4.5 organizes its mid-training into structured data blocks that combine extensive code corpora, synthetic reasoning tokens, and long-context/agentic trajectories, progressively broadening competence across tasks [

138
]. Techniques like best-fit packing are also employed at this stage to maximize the utility of the training data [

138
,

177
]. A similar curriculum-based scaling is seen in Step-3.5-Flash [

137
], which trains on nearly one trillion tokens through a staged sequence from general texts to code, tool-use, long-context, and finally agent-specialized data. This progressive design stabilizes distribution shifts while building agentic and long-context reasoning abilities.

Together, these methods reflect a continued shift toward systematic, scalable, and quality-aware data curation in mid-training.

---

[referencia=e3019f635a854c51 score=0.026]
53
,

54
]. To enhance the quality of long data, some metrics (e.g., attention scores, perplexity and information gain) have been proposed to further select texts with long-range dependencies [

55
,

56
]. Additionally, achieving long-context modeling at scale requires architectural adaptations, where position encodings (discussed in Section 3.2.2) should be adjusted to support the corresponding context length.

---

[referencia=e3019f635a854c51 score=0.022]
29
] is a recently emerging paradigm that generates an extended, in-context reasoning trace before producing the final response. This method emulates a 

*slow thinking*
 cognitive mode, engaging more deeply with complex problems compared to the fast thinking used in standard CoT. Long-CoT offers two principal advantages over traditional CoT: (1) it enables iterative self-correction during reasoning rather than one-shot generation, and (2) it allows for structured, multi-step exploration akin to advanced search algorithms such as ToT [

254
]. To enable this extended reasoning behavior, recent post-training pipelines increasingly rely on large-scale RL training to optimize intermediate reasoning trajectories and process-level objectives, aligning with the RL-based long-CoT training paradigm discussed in Section 4.2.3. This RL-driven optimization not only improves reasoning depth and stability but also shapes the model’s preference for deliberate, stepwise problem solving at inference time. Despite its effectiveness, long-CoT reasoning still faces challenges such as problematic reasoning patterns (e.g., overthinking and hallucination [

259
]) and high inference costs. These issues have attracted considerable attention in ongoing research aimed at their mitigation.

---

[referencia=e3019f635a854c51 score=0.017]
#### **5.3.3 Representative agentic applications**

Recent advances increasingly target *long-horizon* agent capabilities that solve complex information seeking tasks, where agents must sustain reasoning, planning, and interaction across extended multi-step trajectories in complex interaction environments. Such tasks expose fundamental limitations of conventional LLM agents, including unbounded context growth, accumulated execution errors, fragile intermediate reasoning, and the inability to persist, revise, or consolidate knowledge over time. Addressing these challenges requires not only improved memory and planning mechanisms, but also new interaction paradigms that support iterative exploration, feedback integration, and adaptive decision-making throughout prolonged task execution.

Representative long-horizon agents have therefore begun to specialize into several typical application-driven paradigms. 

*Deep search*
 focus on multi-step web navigation and information retrieval, combining structured reasoning, tool interaction, and reinforcement learning to solve complex multi-hop search problems and progressively scale tool usage during inference [

187
,

284
]. These systems emphasize efficient exploration of large external information spaces and the coordination of reasoning with environment feedback under limited interaction budgets. 

*Deep research*
 extend this paradigm toward comprehensive knowledge synthesis, iteratively collecting evidence, refining hypotheses, and producing citation-grounded reports comparable to professional analytical workflows [

285
]. Compared with deep search, they place greater emphasis on long-range consistency, evidence integration, and structured report generation over extended reasoning horizons. Meanwhile, 

*code agents*
 address long-horizon software engineering or code analysis tasks, where agents must reason over large codebases, perform iterative execution and debugging, and integrate environment feedback to complete complex programming objectives [

286
]. Such settings require persistent state tracking, error recovery, and incremental solution refinement, making them a particularly stringent testbed for long-horizon autonomy.

These efforts have substantially advanced long-horizon agents in complex task scenarios, significantly extending both reasoning depth and interaction fidelity within real-world environments. Building on this progress, wide reasoning has emerged as a growing focus, wherein multiple candidate paths—or subtasks, more broadly—are explored in parallel to enable a broader yet still effective reasoning paradigm [

188
]. By integrating both depth and width, this approach supports more robust reasoning in complex settings.

#### **5.4 Efficient deployment and inference**

In this section, we first introduce the major deployment issues and then discuss the optimization techniques for addressing these challenges.

---

[referencia=e3019f635a854c51 score=0.014]
155
] and ZeRO-Infinity [

156
] can be employed. These approaches offload computation-light optimizer states to CPU memory and high-speed storage, respectively, to further reduce GPU memory usage. Note that, unlike Adam, optimizers based on gradient spectral norms (e.g., Muon) require full matrix representations, which necessitates additional parameter sharding strategies in their corresponding ZeRO implementations [

148
].

**Communication optimization.**
 As the scale of GPU clusters increases, inter-GPU communication in distributed training becomes a dominant contributor to end-to-end training time. Most communications are handled by highly optimized collective communication libraries (such as NCCL [

157
]) and can be further optimized through operator selection and computation overlapping. For example, changing the MoE communication operator from all-gather to all-to-all can avoid redundant data distribution, thereby reducing communication volume [

150
,

158
]. Furthermore, training efficiency can be improved by overlapping computation and communication in specific scenarios, such as general matrix multiplication (GEMM) and all-to-all sequence in expert parallelism [

159
], or GEMM followed by AllReduce and ReduceScatter in tensor parallelism [

149
]. However, collective communication is typically initiated by the CPU and operates at a coarse granularity, leading to suboptimal efficiency. Leveraging NVIDIA InfiniBand GPUDirect Async (IBGDA [

160
]), DeepEP implements a GPU-initiated, token-level communication method for expert parallelism. This approach enables fine-grained communication without the need to wait for the completion of the entire token packing process [

161
].

**Kernel optimization.**
 To mitigate the performance bottlenecks in dynamic graph execution, many deep learning systems leverage low-level GPU programming libraries and languages (e.g., CUDA [

162
], Triton [

163
], TileLang [

164
], and CUTLASS [

165
]) to implement their most performance-sensitive kernels. These kernel optimizations combine the strengths of such tools to better exploit GPU memory bandwidth and computational resources. For example, FlashAttention [

166
–

167
] uses CUDA kernels that fuse block-wise matrix multiplication with an online softmax computation, to reduce the quadratic time and memory complexity in the sequence length of vanilla self-attention. To further enhance computational utilization, the kernel pipeline is subsequently redesigned to overlap non-GEMM operations within the softmax layer with the asynchronous WGMMA instructions for GEMM [

168
]. Furthermore, DeepGEMM [

---

[referencia=e3019f635a854c51 score=0.007]
**Other enhancement techniques.**
 Beyond efficiency-focused variants, another technical direction seeks to address inherent limitations within the attention mechanism itself, aiming to enhance its expressive capability. Existing research has identified issues such as 

*attention sinks*
 — a tendency for attention to disproportionately focus on a small set of initial tokens [

77
]. To mitigate this, approaches like learnable sink tokens, query-key normalization, and element-wise sigmoid gating have been proposed [

99
,

100
]. Another important challenge is 

*attention dilution*
, where attention weights become diffused across irrelevant tokens as context length grows. To counteract this, recent work introduces techniques such as length-dependent scaling and modified attention-scoring functions [

101
,

102
], focusing on critical information and promoting the emergence of sparse attention patterns.

---

[referencia=e3019f635a854c51 score=0.007]
#### **5.2.1 Reasoning enhancement**

Traditional CoT prompting methods still face challenges with complex tasks. An important line of work for enhancing LLM reasoning is to deliberately allocate additional computation during inference. This paradigm is commonly referred to as *test-time scaling*. In this part, we review several reasoning enhancement methods.

**Sampling based methods.**
 A straightforward yet effective form of test-time scaling involves generating multiple reasoning trajectories and aggregating their results to produce a final answer, mitigating the brittleness of single-path CoT reasoning. Early methods employed majority voting [

29
] or self-consistency [

251
], where the most frequent answer across multiple CoT rollouts is selected. This strategy generalizes to the 

*Best-of- (BoN)*
 inference paradigm, in which a model samples 

 candidate solutions and selects the optimal one based on a predefined criterion. To improve selection quality, subsequent work has moved beyond simple aggregation to promote diversity among samples [

252
] or to incorporate learned verifiers and reward models for candidate ranking [

253
]. In current practice, BoN has become a standard baseline for test-time scaling, consistently yielding performance gains as 

 increases.

**Search-based methods.**
 To overcome the limitations of linear CoT and unstructured sampling, recent work reframes inference-time reasoning as an explicit search problem over intermediate states. Early approaches extend CoT into tree- or graph-structured representations, such as tree-of-thoughts (ToT) [

254
] and graph-of-thoughts (GoT) [

255
], enabling LLMs to branch, evaluate, and backtrack across multiple reasoning paths. More recent methods further integrate classical search algorithms, particularly Monte Carlo Tree Search (MCTS), into LLM inference, unifying reasoning, acting, and planning within a search-based framework [

256
] and incorporating language-model-based value estimation and process-level reward modeling to guide exploration [

257
–

258
]. These search-based methods explicitly trade inference-time computation for reasoning quality, allowing the model to explore and evaluate intermediate steps more thoroughly.

**Long-CoT reasoning.**
 Popularized by models such as OpenAI’s o1 and DeepSeek-R1, long-CoT reasoning [

29
] is a recently emerging paradigm that generates an extended, in-context reasoning trace before producing the final response. This method emulates a

---

[referencia=e3019f635a854c51 score=0.007]
#### **3.3.1 Training configuration**

Compared with small models, pre-training LLMs are more challenging, as abnormal optimization issues may frequently occur during the process. To address this, we must carefully configure the optimization settings and adopt stabilization techniques for training.

**Optimization configurations.**
 Based on extensive studies, empirical guidance has accumulated for setting hyperparameter configurations, including batch size, learning rate, and optimizer choice. For batch training, existing studies [

140
] typically implement a dynamic schedule that gradually increases the batch size, eventually reaching a scale of millions of tokens. For learning rate, LLMs commonly adopt a combination of warm-up and decay strategies. In earlier work, researchers often selected the batch size and learning rate based on empirical observations (e.g., a batch size of 3.2M and a learning rate of 

 [

13
]). More recently, researchers have explored scaling laws for batch size and learning rate, deriving formal relationship functions to determine these parameters based on model size and dataset size [

141
]: a recent study has found that the optimal learning rate follows a power law with respect to model and dataset size, while the optimal batch size primarily depends on dataset size. Another commonly used optimization strategy is the 

P parameterization (Maximal Parameterization Update), which allows hyperparameters (e.g., learning rate) tuned on small-sized models to be directly transferred to larger models [

142
,

143
].

**Optimizers.**
 Regarding the optimizer, Adam and AdamW are commonly used in LLM training, typically with the following hyperparameters [

27
]: 

, 

, and 

. Additionally, efforts have been made to improve the efficiency and reduce the memory consumption of Adam, leading to improved optimizers such as Adafactor [

144
] and Adam-mini [

145
]. Recently, a new class of spectral-norm based optimizers has been increasingly adopted in large-scale training (e.g., Shampoo [

146
], SOAP [

147
], and Muon [

117
,

148
]). Shampoo and Muon share similar designs in their update rules, and Muon introduces Newton–Schulz iterations to avoid the expensive SVD computation. Prior work typically treats optimization hyperparameters and optimizer configurations as independent design choices. A promising co-design direction is to adjust model parameters during optimization updates to satisfy the 

P condition [

142
]. Building on this idea, the SSO optimizer retracts each Muon update onto the spectral sphere of the parameter weights [