[referencia=e3019f635a854c51 score=0.627]
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

[referencia=e3019f635a854c51 score=0.500]
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

[referencia=e3019f635a854c51 score=0.315]
95
]. Concurrently, Kimi-K2.5 focuses on token-efficient optimization, significantly reducing redundancy in CoT reasoning (e.g., roughly 25%–30%) while maintaining accuracy [

188
].

**Agentic training.**
 Given the growing importance of agentic capabilities, mainstream LLMs often incorporate a dedicated stage or design for agentic training. As discussed in the agentic instruction synthesis section (Section 4.1.1), constructing appropriate training environments is a foundational step. For instance, enhancing search and coding abilities requires establishing corresponding web and programming environments, along with the associated instruction data. Such data can be used to bootstrap agentic abilities as a cold start. Following this, agentic RL can be introduced. In this setup, for each input task, the model serves as a policy that generates trajectories by interleaving intermediate reasoning, tool calls, and environment observations. Optimization is then guided by trajectory-level feedback, which may be derived from rule-based, task-specific reward functions (e.g., success checks, unit tests, constraint violations, pre-specified rubrics) or from learned evaluators such as LLM-as-a-judge reward models. Compared to standard RL training, agentic RL is significantly more resource-intensive and demands specialized infrastructure and algorithmic efficiency. In practice, agentic training has become a necessary component in the development of advanced LLMs. For example, DeepSeek-V3.2 [

78
] adopts a cold-start phase that unifies reasoning and tool use within single trajectories, combined with large-scale agentic task synthesis involving thousands of environments and tens of thousands of complex prompts to support RL-driven post-training. Similarly, Kimi-K2.5 [

188
] builds a unified multimodal agentic RL framework and employs outcome- and trajectory-based evaluators to deliver scalable feedback for multimodal tool-using behaviors. It also introduces the 

*agent swarm*
 approach, using parallel-agent RL to decompose complex tasks among multiple sub-agents, optimizing their orchestration toward a global, verifiable objective.

In summary, industrial post-training has evolved into a systematic, multi-stage process that supports both normal response and deep thinking modes to accommodate diverse usage scenarios. It moves beyond general alignment via SFT and RL to incorporate specialized training for reasoning and agentic capabilities. By integrating tailored data and reward strategies, modern pipelines enable LLMs to address user queries with greater effectiveness and reliability.

---

[referencia=e3019f635a854c51 score=0.295]
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

[referencia=e3019f635a854c51 score=0.230]
#### **4.3.2 Industrial practice of post-training**

In this part, we describe the general post-training pipeline of industrial-level LLMs and the reasoning-enhanced post-training approach.

**General pipeline.**
 Industrial-level LLMs undergo rigorous post-training to enhance their comprehensive task-solving capabilities. Overall, this process involves multi-stage alignment procedures involving SFT on carefully curated instruction datasets followed by offline or online RL. For instance, Qwen2.5 [

26
] is first fine-tuned on a large, high-quality dataset of over one million human-curated and model-augmented instructions (including long-form text, code, and mathematical reasoning data selected by reward models) and then aligned through a two-phase RL process, i.e., an offline DPO stage followed by online policy optimization with GRPO, to align the model with human preferences. In production settings, post-training is typically iterative, with repeated cycles of alignment and comprehensive capability/safety evaluations that act as deployment gates and guide subsequent data and reward updates [

229
]. Recently, there is growing emphasis on improving the reasoning capabilities of LLMs during post-training [

40
,

136
], leading to the widespread use of mathematical and coding problems. Agentic capability is also frequently treated as a dedicated objective due to its diverse real-world applications. To facilitate the training of verifiable reasoning and agentic tasks, rule-based rewards are primarily employed, complementing model-based rewards in RL training. Thus, reward design often splits into preference-based objectives for open-ended helpfulness (e.g., DPO-style signals) and verifiable rewards for reasoning-heavy domains (e.g., math/agent), enabling RL with automatically checkable criteria (i.e., RLVR). For example, DeepSeek-V3 [

40
] and Tulu 3 [

193
] incorporate both model- and rule-based rewards for RL training.

**Reasoning-oriented training.**
 Following the above general post-training pipeline described above, this procedure can be adapted for developing long-CoT reasoning models like DeepSeek-R1. A typical approach proceeds by first eliciting the long-CoT reasoning capabilities of the base models and then integrating SFT and RL by augmenting the training data with long-CoT-oriented data at each stage. In DeepSeek-R1 [

---

[referencia=e3019f635a854c51 score=0.204]
#### **3.2.3 Mixture-of-Experts (MoE)**

Benefiting from efficient parameter scaling, the MoE architecture has been widely adopted as a replacement for standard feed-forward network (FFN) modules in LLMs. Typically, each MoE layer consists of a gating function, commonly referred to as a *router*, and a set of expert sub-networks. During each forward pass, the router dynamically selects a sparse subset of experts for activation and computation. In the following, we discuss how this architecture can be adapted and optimized for LLM development.

**Gating function.**
 Given an input token representation, the gating function maps it to a gating value for each expert and selects the experts with the highest values for activation. Notably, early large MoE models, like Mixtral [

111
], typically chose top-

 experts and employed the softmax function to compute the final gating values. To reduce communication when distributing experts across different devices using expert parallelism, device-limited routing has been introduced [

67
], which first selects a small number of devices and then applies top-

 selection only to the experts on those devices. Additionally, some research employs the top-

 sampling, also called 

*nucleus sampling*
, to dynamically allocate the number of activated experts per token [

112
]. Beyond the selection strategy, new activation functions of the router (e.g., sigmoid) have been proposed to avoid expert competition and achieve improved performance [

113
].

**Expert.**
 MoE models typically activate a relatively small number of routed experts (e.g., 8 experts in Mixtral [

111
]) per layer, with each expert being an FFN. To reduce redundancy among experts, some recent MoE models (e.g., DeepSeek-V3 [

40
]) introduce shared experts and replace large experts with multiple smaller fine-grained experts. Additionally, since shallow layers are more general than deep layers, allocating more experts to the deep layers can effectively enhance the model’s performance [

114
]. In addition to using FFNs as experts, some research explores constant vectors or memory layers, which help reduce computation and improve performance [

115
].

**Load balancing.**
 During MoE training, it is important to balance the training across experts to ensure they are sufficiently trained. For this purpose, an auxiliary loss is commonly introduced to achieve load balancing among experts, typically minimizing the product of activation frequency and average gating scores across all experts [

---

[referencia=e3019f635a854c51 score=0.160]
#### **3.3.2 Scalable training**

As model and data scales increase, efficiently training LLMs poses significant challenges. In particular, two key issues must be addressed: fitting large models into GPU clusters and improving training throughput. We summarize the training details of several representative LLMs in Table 2. In the following, we review several key techniques that tackle these challenges.

**Parallel training.**
 To scale the training of LLMs across hardware clusters, various forms of parallelism have been developed, each targeting different computational or memory bottlenecks [

149
,

150
]. These include data parallelism, which replicates models across devices and distributes input batches; tensor parallelism, which splits parameter matrices across devices; pipeline parallelism, which assigns consecutive layers to different devices; model parallelism, which refers to the combination of pipeline parallelism and tensor parallelism; context parallelism, which partitions long input sequences for distributed attention computation [

151
,

152
]; and expert parallelism, which distributes MoE experts across devices for parallel execution. These parallelism strategies are typically supported by libraries such as DeepSpeed and Megatron. Additionally, specialized strategies can be developed according to GPU properties. For example, DeepSeek-V3 [

40
] introduces DualPipe, a technique that reduces pipeline bubbles by overlapping forward and backward computation with communication phases. Additionally, the collaborative hardware and software design is also necessary to further break the bottleneck for training and inference acceleration [

153
].

**ZeRO.**
 The zero redundancy optimizer (ZeRO) [

154
] addresses the problem of memory redundancy in data parallelism. It retains only a fraction of model and optimizer parameters on each GPU, while the rest can be retrieved from other GPUs when required. Specifically, ZeRO introduces three optimization levels based on which components are partitioned: optimizer state partitioning (ZeRO-1), gradient partitioning (ZeRO-2), and parameter partitioning (ZeRO-3), which provides increasing levels of memory savings. ZeRO-1 and ZeRO-2 introduce minimal additional communication overhead, while ZeRO-3 incurs about 50% more communication cost but yields greater memory efficiency. In scenarios with limited GPU memory, additional strategies such as offloading [

155
] and ZeRO-Infinity [

---

[referencia=e3019f635a854c51 score=0.147]
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

[referencia=e3019f635a854c51 score=0.113]
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

[referencia=e3019f635a854c51 score=0.080]
210
], which assess model outputs against predefined criteria, and preference rankings [

25
], which compare multiple responses to capture relative quality. These supervision signals are used to train neural reward models that either regress to human-provided scores or learn contrastive preference boundaries between candidate outputs. Recent extensions [

211
] further integrate reasoning-aware reward modeling into RLVR-style training. In particular, reasoning reward models formulate reward estimation as an explicit reasoning process, generating structured evaluation traces or rubric-like judgments before producing final rewards, which significantly improves interpretability and evaluation accuracy across reward benchmarks.

**Extensions.**
 Since rule-based and model-based reward modeling excel at different tasks, hybrid approaches have been proposed to combine both paradigms in mainstream commercial LLMs like DeepSeek-R1 [

29
] and Qwen3 [

57
]. A major challenge for both reward types lies in obtaining reliable rewards in general domains, as reward criteria are more diverse and complex, and explicit references or ground truth are often unavailable. Generalist reward modeling [

212
] is therefore critical for LLM capability generalization, requiring flexibility across input types and accurate reward generation in diverse domains. To overcome the high variance issue of sparse feedback in outcome-based reward modeling, process reward modeling is proposed by evaluating individual output components (e.g., sentences or reasoning steps), providing fine-grained training signals [

213
]. Despite these advances, defining, learning, and scaling effective reward signals for the general alignment of LLMs remains a significant challenge.

---

[referencia=e3019f635a854c51 score=0.080]
#### **6.3 Potential issues**

While existing benchmarks have driven significant progress in assessing LLMs, they now face three fundamental challenges: ensuring fair evaluation free from biases and data contamination, closing the gap between practical utility and narrow benchmark success, and developing meaningful frameworks to evaluate emerging superintelligent capabilities as standard benchmarks saturate.

**Evaluation fairness.**
 Achieving truly fair and unbiased evaluation of LLMs remains a significant challenge. A key issue is 

*data contamination*
, where benchmark exposure during training inflates scores through memorization rather than true generalization [

341
]. Potential solutions include rigorous decontamination and continuously updated benchmarks [

342
]. Additional biases further complicate assessment due to inherent limitations in LLMs: length bias (favoring unnecessarily long outputs), position bias (order effects in candidates), and style bias (favoring certain linguistic styles over content) [

337
–

338
,

343
], potentially distorting results regardless of model capability.

**Practical utility.**
 Another major challenge in evaluation lies in the frequent discrepancy between a model’s benchmark performance and its real-world usability: models that achieve high scores on standardized tests often fail to generalize to the variability and unpredictability of real user interactions, resulting in strong academic performance that does not reliably translate into practical utility in deployed systems [

344
]. For example, recent analyses demonstrate that while benchmark scores can remain stable under fixed test conditions, absolute effectiveness might often decline significantly when inputs are varied or rendered more flexible [

345
]. To better assess how models perform in real scenarios, it is essential to develop more realistic and applied evaluation tasks. These could include simulations of customer service dialogues, live coding sessions with debuggers, multi-step web navigation with actual APIs, or interactive task completion in sandbox environments. Such benchmarks would provide a more reliable measure of practical capability, helping to align research progress with real-world utility.

**Superintelligence assessment.**
 Existing benchmarks for assessing LLMs are showing clear signs of saturation. As illustrated in Fig. 6, key LLM capabilities such as general reasoning, mathematical problem-solving, and code synthesis have advanced rapidly in recent years. For example, on the widely used MMLU benchmark [

325
], state-of-the-art models now exceed human-level performance after large scale training, with DeepSeek-R1 achieving over 90% accuracy [

29
]. As a result, further gains on these established benchmarks are becoming increasingly meaningless. Although more challenging benchmarks continue to emerge [

329
,

331
,

---

[referencia=e3019f635a854c51 score=0.050]
168
]. Furthermore, DeepGEMM [

169
] improves matrix multiplication utilization by taking advantage of architectural advancements in Hopper. Other popular training kernels [

170
–

173
] also markedly speed up specific algorithms like MLA and Linear Attention.

**Mixed precision training.**
 In earlier language models such as BERT [

11
], 32-bit floating-point (FP32) precision was standard during pre-training. To reduce optimization costs, subsequent studies [

174
] explored using 16-bit floating-point (FP16) precision, which decreases both memory consumption and computational overhead. However, research has demonstrated that FP16 can compromise computational accuracy [

108
]. To mitigate this, the 

*Brain Floating Point (BF16)*
 format was adopted, which allocates more bits to the exponent and fewer to the significant parts, thereby improving numerical representation accuracy. Most recently, DeepSeek-V3 [

40
] has implemented FP8 training, utilizing FP8 for computation-intensive GEMM while maintaining BF16 or FP32 for critical operations to preserve numerical stability. To enable lower numerical precision, fine-grained scaling factors are introduced to normalize values within each module before quantization, preserving dynamic range under reduced bit-width. For example, MXFP4, as used in GPT-OSS [

100
], adopts a microscaling-based representation [

175
]. Recent hardware architectures, such as NVIDIA’s Hopper and Blackwell, also provide native support for such low-precision numerical formats.

#### **3.4 Mid training**

Although pre-training establishes a broad foundation for LLMs, it often falls short of preparing models for advanced, domain-specific tasks such as mathematics, coding, or agentic reasoning. To address this gap, *mid-training* (also referred to in earlier literature as *continual pre-training*) has emerged as a widely-adopted practice for boosting downstream performance. By integrating large-scale, domain-curated data into the training pipeline, mid-training enables models to refine and strengthen their proficiency in targeted capabilities.

---

[referencia=e3019f635a854c51 score=0.044]
#### **4.1.1 Data collection**

An instruction-formatted instance (

*a.k.a.,* *instruction data*
) typically consists of a task description, an optional input, and a corresponding output. For constructing instruction data, early research primarily adapts traditional NLP datasets through human annotation (as exemplified by FLAN [

181
]), while subsequent work adopts real human instructions, following InstructGPT [

25
]. Since both approaches require considerable effort, recent studies have increasingly focused on synthesizing instruction data using LLMs, as discussed below.

**General instruction synthesis.**
 Recent advancements have automated the generation of instruction data using LLM-based synthesis and refinement of datasets. This process typically starts with human-written seed examples that guide LLMs to generate new instructional data through iterative prompting and filtering (e.g., Self-Instruct [

182
]). Given the critical impact of data quality on instruction tuning performance, researchers are increasingly focused on enhancing instruction datasets. Current approaches use carefully crafted prompts to direct advanced LLMs in refining instructions, focusing on three key aspects: improving complexity and diversity by adding constraints or broadening topics [

183
], integrating external knowledge sources such as topic taxonomies [

184
], and better aligning with human intents through principle guidance [

185
].

**Long-CoT instruction synthesis.**
 OpenAI’s o1 [

28
] and DeepSeek-R1 [

29
] have gained attention from the research community for their ability to perform deep reasoning through substantially extended CoT processes. Following this direction, researchers have proposed several methods for synthesizing instructions that elicit long-CoT reasoning. Long-CoT instances can be generated using in-context learning with the corresponding demonstrations based on powerful LLMs. Additionally, prompting strategies can be used to encourage the model to produce detailed reasoning processes with self-reflection and self-verification [

29
]. Multi-agent approaches can also be employed by assigning different roles to LLMs, typically involving a policy model generating the solution steps and a critique model evaluating the process and deciding whether to proceed or backtrack [

186
]. With the open-sourcing of large reasoning models, long-CoT instruction data can be directly distilled to fine-tune existing LLMs. Notably, DeepSeek-R1’s approach successfully adapted Qwen2.5 and LLaMA-3 through this method for long-CoT reasoning [

29
].

---

[referencia=e3019f635a854c51 score=0.043]
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

[referencia=e3019f635a854c51 score=0.035]
 and 

) to distinguish between the corresponding datasets. Similarly, Hunyuan-TurboS [

194
] employs short CoT data for queries solvable by an instruct model and long CoT data for those requiring a reasoning-focused approach.

**Instruction amount.**
 In terms of the data amount, existing open-source LLMs typically use approximately one million instruction-tuning instances to effectively elicit capabilities across various tasks. For instance, DeepSeek-V3, Qwen2.5, and Tulu-v3 utilize 1.5M, 1M, and 939K instances, respectively. However, when focusing specifically on a single task or narrow set of tasks, far fewer instruction instances may suffice. Prior studies have demonstrated that even a limited number of instances (e.g., a few thousand) can enable LLMs to perform well on specific tasks such as open-ended dialogue [

195
]. Additionally, the required number of training instances depends on the base model’s capabilities. For strong base models, learning efficiency can be remarkably high when using high-quality instruction data for some specific tasks. For instance, Qwen2.5-32B can readily master complex deep reasoning behaviors through fine-tuning with just several thousand long-CoT instruction instances [

29
].

---

[referencia=e3019f635a854c51 score=0.030]
#### **4.2.2 Optimization criteria and reward models**

In essence, RL provides the mechanism for translating high-level objectives into concrete optimization targets through carefully defined reward signals. Prior alignment research has commonly framed desirable LLM behavior in terms of the principles of *helpfulness*, *honesty*, and *harmlessness* (3H criteria). More recently, RL has been extensively employed as an effective method to extend model capabilities (e.g., complex reasoning). While objectives may vary, RL training fundamentally adjusts model behavior in response to defined reward signals. These signals originate from diverse sources, including human preference feedback, rule-based verification, and learned evaluators. Accordingly, existing approaches can be broadly categorized by their reward construction into two paradigms: *rule-based rewards*, which depend on heuristic constraints or formal verification procedures, and *model-based rewards*, which rely on trained reward models to automatically assess outputs. The remainder of this part reviews these two paradigms and their extensions.

**Rule-based reward.**
 Rule-based reward modeling derives supervision signals from explicit and verifiable rules, enabling precise and low-noise evaluation. Early successes of rule-grounded RL appear in fully specified environments such as AlphaGo [

206
], where game rules provide exact outcome-based rewards. In LLM post-training, rule-based rewards typically arise from two sources: natural-language rule adherence, which evaluates compliance with predefined behavioral or constitutional principles (e.g., DeepMind’s Sparrow [

207
]), and verifier-based correctness signals, which assess outputs through answer matching, symbolic checking, or executable validation. The latter has recently evolved into RLVR, where correctness can be formally verifiable for domains such as mathematics and code generation, as demonstrated by DeepSeek-R1 [

29
]. Rule-derived rewards are increasingly adopted in agentic RL [

208
], where feedback may depend on environment interaction success, tool execution validity, or multi-step task completion. Recent work [

209
] further introduces 

*rubric-based rewards*
, which decompose response quality into structured, multi-criteria checklists that can be automatically aggregated into scalar supervision, thereby extending RLVR to domains lacking verifiable answers and enabling more general reasoning alignment.

**Model-based reward.**
 Model-based reward modeling learns an explicit reward estimator from high-quality human feedback, enabling scalable and flexible evaluation beyond manually specified rules. Such feedback is typically collected in two complementary forms: scoring annotations [

210
], which assess model outputs against predefined criteria, and preference rankings [

---

[referencia=e3019f635a854c51 score=0.026]
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

[referencia=e3019f635a854c51 score=0.021]
#### **4.2.3 Reinforcement learning algorithms**

RL algorithms for LLM post-training can be categorized along the axis of 

*online*
 versus 

*offline*
 policy optimization, depending on whether new training data are generated through interaction with the current or recently updated policy [

214
]. Online policy optimization continuously collects rollouts as training proceeds and updates the model using newly obtained reward signals, typically following an on-policy RL paradigm. In contrast, offline policy optimization learns directly from a fixed dataset of human preferences or logged trajectories without further environment interaction, often reformulating the alignment objective into supervised or preference-based optimization. This distinction is conceptually different from the classical on-policy/off-policy taxonomy in RL, which is defined by whether the data-generating policy matches the policy being optimized. In the following, we review RL algorithms from the perspective of online/offline policy optimization.

**Online policy optimization.**
 Online RL for LLM post-training is commonly built upon the PPO algorithm [

200
], which stabilizes policy updates through a clipped objective and advantage estimation via a learned value function. While effective, PPO’s actor-critic design requires a separate value network, which increases both training and inference complexity and overhead. Recently, GRPO [

30
] has simplified this paradigm by removing the value model entirely. Instead, it estimates advantage by comparing rewards across multiple responses generated for the same prompt. This design offers greater algorithmic simplicity by eliminating value function training, though it introduces new considerations such as group sampling strategies and relative reward normalization. Subsequent research has aimed to enhance GRPO’s stability and effectiveness through decoupled clipping strategies, sequence-level importance weighting, and refined sampling techniques to improve training dynamics and reduce bias [

203
–

205
]. With the popularity of reasoning models such as DeepSeek-R1 [

196
], GRPO has now become a standard practice for alignment and capability refinement in settings where verifiable reward signals are available. More recently, on-policy distillation (OPD) [

57
] has also been adopted, where the student model learns from the teacher model’s logits in an online manner, thereby gaining access to more dense supervision signals.

**Offline policy optimization.**
 In contrast to PPO-style online reinforcement learning, offline preference optimization directly learns policies from fixed human preference data without iterative environment interaction or explicit reward-model training. A representative method is direct preference optimization (DPO) [

---

[referencia=e3019f635a854c51 score=0.013]
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

---

[referencia=e3019f635a854c51 score=0.013]
#### **5.2.2 Retrieval-augmented generation**

As an inherent limitation, LLMs often struggle with real-time or domain-specific queries due to their constrained knowledge scope. To address this, retrieval-augmented generation (RAG) integrates external knowledge sources to enhance response quality and relevance. In what follows, we outline the typical RAG workflow and highlight recent methodological advances.

**Basic workflow.**
 RAG generally proceeds in three stages [

260
]: (i) 

*context retrieval*
, where relevant documents are retrieved using lexical-based methods (based on sparse representations) or semantic-based methods (based on dense embeddings); (ii) 

*prompt construction*
, where the retrieved information is incorporated into the model’s prompt along with task instructions. Due to context length limitations, techniques like reranking, summarization, or information extraction are often applied to retain the most useful content and reduce issues such as attention bias (e.g., the 

*lost in the middle*
 issue [

261
]); and (iii) 

*response generation*
, where the LLM generates an output using the enriched prompt. If the retrieved content is noisy or contradictory, the model may assess its confidence or re-evaluate its output to determine whether further retrieval is necessary [

262
].

**Improvement strategies.**
 RAG’s performance can be enhanced through several techniques. First, 

*retrieval quality enhancement*
 optimizes context retrieval by adjusting document granularity or reranking candidate documents [

263
]. Existing work [

264
] has adopted LLMs to rewrite or expand the input query for enhancing the informativeness, and filter or extract the information from retrieved documents to improve the relevance. Second, 

*iterative retrieval enhancement*
 enables multi-turn refinement when single-round retrieval is insufficient. LLMs can dynamically revise queries based on intermediate outputs, gradually enhancing retrieved content [

262
]. In complex scenarios, this process can be integrated with CoT reasoning by converting each reasoning step into new queries that inform subsequent thought processes [

265
].

#### **5.3 Agentic systems**

Recent advances [

266
–

268
] use LLMs as the core reasoning component within autonomous agents—systems that perceive environments, make decisions, and execute tasks through reasoning and interaction. This section outlines the fundamental workflow of LLM-based agents, describes advanced architectures and techniques, and highlights representative applications.