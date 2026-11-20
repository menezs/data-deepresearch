[referencia=e3019f635a854c51 score=0.714]
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

[referencia=e3019f635a854c51 score=0.575]
**Scaling enhancement.**
 Scaling serves as the foundational paradigm in LLM development. It is governed by the principle of converting growing computational resources into enhanced model capability—a core tenet of “

*The Bitter Lesson*
” [

348
]. Initially, scaling efforts focused on training-time expansion through increases in model and dataset size [

14
,

18
]. More recently, test-time scaling, exemplified by long chain-of-thought models such as DeepSeek-R1 [

196
], has emerged as a powerful complementary dimension. Moving forward, scaling will remain essential for advancing machine intelligence, but it must evolve into a more systematic and multifaceted discipline. On one hand, the cost of current scaling approaches should be substantially reduced—by investigating learning mechanisms, improving architectures, and optimizing training algorithms. On the other hand, we must architect new, inherently scalable training environments designed to systematically unlock advanced capabilities in LLMs [

78
,

188
]. Ultimately, this dual approach will transform scaling from a blunt-force expansion into an efficient, directed, and capability-aware engineering practice.

**Data barrier.**
 The continued advancement of LLMs is fundamentally limited by the growing scarcity of high-quality training data, as state-of-the-art models have largely exhausted existing public and curated textual sources [

34
]. This creates a critical scaling bottleneck for future progress. To overcome this limitation, research can pursue two complementary directions. The first is to enhance 

*data efficiency*
: this entails maximizing the utility extracted from existing datasets and enhancing the functional capacity learned per token (i.e., token efficiency). This will require advances in data curation, training curricula, and model architectures [

46
,

49
,

132
]. The second direction moves beyond static corpora to develop verifiable, programmatic data-generation environments [

60
,

78
]. These environments, such as code execution sandboxes, simulation platforms, or reasoning domains with ground-truth solutions, can systematically produce vast, diverse, and intrinsically validated training data. Progress in both areas, improving how data is utilized and how it is generated, will be essential to transcend current data limitations and sustain the next generation of LLMs.

**Training efficacy.**
 The development of foundational capabilities in LLMs remains heavily dependent on large-scale pre-training via text completion on unlabeled corpora [

13
,

347
]. Although this method has proven effective and generalizable, its learning efficiency is fundamentally limited: it demands vast datasets spanning trillions of tokens for cutting-edge models [

57
,

---

[referencia=e3019f635a854c51 score=0.437]
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

[referencia=e3019f635a854c51 score=0.316]
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

[referencia=e3019f635a854c51 score=0.241]
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

[referencia=e3019f635a854c51 score=0.228]
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

[referencia=e3019f635a854c51 score=0.161]
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

[referencia=e3019f635a854c51 score=0.158]
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

[referencia=e3019f635a854c51 score=0.144]
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

[referencia=e3019f635a854c51 score=0.129]
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

[referencia=e3019f635a854c51 score=0.123]
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

[referencia=e3019f635a854c51 score=0.121]
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

[referencia=e3019f635a854c51 score=0.120]
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

[referencia=e3019f635a854c51 score=0.114]
10
] pioneered this learning paradigm using bidirectional LSTMs, while BERT [

11
] significantly advanced the approach by employing the highly parallelizable Transformer architecture [

12
]. This evolution established the influential “

*pre-train + fine-tune*
” paradigm, in which models first learn a broad understanding of language and are subsequently adapted to specific downstream tasks via task-specific fine-tuning.

● Large language models (LLMs) [

13
] achieve substantially enhanced capabilities by scaling up model size, training data, and computational resources in accordance with established scaling laws [

14
]. Pioneering examples include GPT-3 (175B parameters) [

13
] and PaLM (540B parameters) [

15
], which delivered significant performance gains over their predecessors, such as BERT [

11
] and GPT-1 [

16
]. Notably, GPT-3 excels at few-shot tasks through 

*in-context learning*
, a capability absent in GPT-2. This leap in capability led the research community to formalize the term “

*large language models*
” [

17
,

18
], distinguishing them from conventional pre-trained language models. The transformative potential of LLMs became widely recognized with the launch of ChatGPT, an advanced dialogue-oriented model that sparked global interest in generative AI.

Today, LLMs have transformed both AI research and industry, driving a paradigm shift from task-specific models toward general-purpose foundation models. Beyond merely improving upon traditional benchmarks, LLMs now act as accelerators for scientific discovery—synthesizing literature, generating code to lower barriers, and aiding hypothesis formation—thus becoming indispensable tools for research work. In industry, LLMs leverage their extensive world knowledge and advanced capabilities, such as planning, reasoning, and tool use, to serve as versatile intelligent assistants. This technological leap has catalyzed a rapidly growing application ecosystem. LLMs now form the core of advanced enterprise search platforms, AI-driven data analysis tools, automated customer support systems, and sophisticated content creation suites, demonstrating their deep integration into professional and operational workflows. Given their expanding role, LLM development has accelerated markedly, with numerous models now emerging and being integrated into daily life, as shown in the evolution timeline (Fig. 1).

---

[referencia=e3019f635a854c51 score=0.110]
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

[referencia=e3019f635a854c51 score=0.108]
21
], underscoring the critical role of data engineering in the pre-training process. In this framework, task-solving is framed as a 

*text completion*
 problem, where a response is generated based on the given input. When scaled sufficiently, this approach allows language models to address a wide range of downstream tasks by learning to accurately reconstruct and produce natural language. Following pre-training, an optional 

*mid-training*
 phase can be applied to further strengthen the model’s foundational capabilities, improving subsequent adaptation. To bridge the gap between foundational training and practical deployment, a standard 

*post-training*
 stage is then conducted. This stage serves two main purposes: eliciting the model’s underlying capabilities and aligning its outputs with human expectations and values [

25
]. The combination of pre-training (optionally enhanced by mid-training) and post-training has established the prevailing methodology for developing capable and aligned LLMs [

26
,

27
].

**Scaling law.**
 Scaling has been a pivotal factor in the success of modern language models. Early research formalized these scaling effects through 

*train-time scaling laws*
, modeling performance as a function of three key variables: model size (

), dataset size (

), and training compute (

), for neural language models [

14
,

18
]. Given a fixed compute budget, these studies empirically fit a power-law relationship: 

, where 

 denotes the cross entropy loss in nats and 

. Initial scaling laws [

14
] favored allocating more resources toward increasing model size over data size. Subsequent work [

18
] refined this view by advocating for a more balanced scaling of model and dataset sizes. In practice, expanding dataset size has often proven highly effective—even relatively small models show substantial improvements when trained on large, high-quality corpora [

26
]. Nevertheless, continued scaling faces significant challenges due to escalating computational costs and the scarcity of high-quality data. This has shifted research focus toward 

*test-time scaling*
 approaches (e.g., OpenAI’s o1 [

28
] and DeepSeek-R1 [

29
]), where enhanced model performance is achieved through strategic allocation of additional inference-time computation—essentially trading efficiency for enhanced capability.

**Representative abilities.**
 Unlike previous-generation models (e.g., BERT, BART), modern language models exhibit a broader and more robust set of capabilities. These include general competencies such as in-context learning (ICL) [

13
], chain-of-thought (CoT) [

17
] reasoning, and instruction following [

---

[referencia=e3019f635a854c51 score=0.103]
224
]. Another challenge is that RL algorithms typically involve numerous hyperparameters and configurations that significantly impact training stability and performance [

203
,

225
]. Stabilizing RL training requires careful hyperparameter selection, continuous monitoring of training dynamics, and the use of well-curated training data. In practice, monitoring entropy provides a valuable indicator of exploration in LLMs, while specialized strategies that regulate and maintain entropy levels have been widely adopted in RL training [

203
,

226
]. Efficiency also remains a critical concern in RL for LLMs, especially in agentic RL where models must plan over long horizons and execute precise tool calls, requiring the generation and evaluation of complex, multi-turn trajectories. To address the associated computational bottlenecks, key strategies include asynchronous training systems that decouple trajectory generation from policy updates, partial rollout training that truncates long action sequences into manageable segments, and parallel distributed computation across dynamically scaled inference and training nodes [

227
]. These approaches enhance learning efficiency, making large-scale RL training practically feasible.

#### **4.3 Discussion**

In this section, we will discuss the comparison of the above two post-training techniques (i.e., SFT and RL) and then present industrial practice of post-training.

---

[referencia=e3019f635a854c51 score=0.096]
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

[referencia=e3019f635a854c51 score=0.066]
Overall, the development and deployment of modern language models (Fig. 2) involves substantially greater complexity than earlier generations. This complexity is driven by the increasing scale and capabilities of these models, and is manifested in a multi-stage pipeline. The foundational pre-training stage requires the meticulous orchestration of data, architecture, and large-scale optimization, balancing performance goals with practical constraints. An optional mid-training phase then further refine advanced capabilities. Subsequently, rigorous post-training has become indispensable, enhancing instruction following, complex reasoning, and task performance while aligning models with human values and addressing critical safety concerns. To leverage these models effectively in practice, they are typically used with prompt engineering techniques and are often deployed within agentic frameworks designed to enhance both usability and performance. Finally, establishing reliable and challenging evaluation benchmarks is essential for steering the future development of LLMs.

The remarkable advancement of LLMs has brought both transformative capabilities and significant new challenges. As these systems demonstrate increasingly sophisticated capacities, the research community requires authoritative frameworks to navigate this rapidly evolving and complex technical pipeline. This survey addresses this necessity by providing a structured overview and analysis of four critical, interconnected stages of the LLM lifecycle: 

*pre-training*
 (developing capable base models), 

*post-training*
 (optimizing models for alignment and task-oriented adaptation), 

*utilization*
 (effective strategies for deployment and downstream use), and 

*evaluation*
 (robust assessment of capabilities and risks). Our contribution is twofold: we offer a systematic introduction to the fundamental techniques driving LLM development, while synthesizing current research to highlight advanced topics and technical challenges. Through a rigorous review of the literature, we consolidate key findings, methodologies, and technical approaches across the field. To support ongoing research, we also maintain a curated GitHub repository of essential LLM resources and supplementary materials, accessible at the website of github.com/RUCAIBox/LLMSurvey. This survey is a concise, self-contained review. It is an updated and refined version of our earlier arXiv article [

19
] (now expanded into a comprehensive book [

20
]). The content and presentation have been substantially revised to better suit the format of a journal review paper and to reflect the current state of the field.

---

[referencia=e3019f635a854c51 score=0.065]
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