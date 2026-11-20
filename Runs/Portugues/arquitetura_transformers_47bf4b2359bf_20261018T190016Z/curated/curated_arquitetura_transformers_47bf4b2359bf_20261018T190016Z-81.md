[referencia=74cf7186aa6d419e score=0.998]
## **Abstract** 

Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges. Sparse attention offers a promising direction for improving efficiency while maintaining model capabilities. We present NSA, a <u>Natively trainable Sparse Attention mechanism that integrates</u> algorithmic innovations with hardware-aligned optimizations to achieve efficient long-context modeling. NSA employs a dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection to preserve both global context awareness and local precision. Our approach advances sparse attention design with two key innovations: (1) We achieve substantial speedups through arithmetic intensity-balanced algorithm design, with implementation optimizations for modern hardware. (2) We enable end-to-end training, reducing pretraining computation without sacrificing model performance. As shown in Figure 1, experiments show the model pretrained with NSA maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning. Meanwhile, NSA achieves substantial speedups over Full Attention on 64k-length sequences across decoding, forward propagation, and backward propagation, validating its efficiency throughout the model lifecycle.

---

[referencia=74cf7186aa6d419e score=0.991]
#### **4.3. Performance Comparison** 

**General Evaluation.** We evaluated the pretrained NSA and Full Attention baseline, on a comprehensive suite of benchmarks spanning knowledge, reasoning, and coding capabilities, including MMLU (Hendrycks et al., 2020), MMLU-PRO (Wang et al., 2024), CMMLU (Li et al., 2023), BBH (Suzgun et al., 2022), GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2020), DROP (Dua et al., 2019), MBPP (Austin et al., 2021), and HumanEval (Chen et al., 2021). The results are shown in Table 1. Despite its sparsity, NSA achieves superior overall performance, outperforming all baselines including Full Attention on 7 out of 9 metrics. This indicates that although NSA may not fully leverage its efficiency advantages on shorter sequences, it shows strong performance. Notably, NSA demonstrates significant gains in reasoning-related benchmarks (DROP: +0.042, GSM8K: +0.034), suggesting that our pretraining helps models to develop specialized attention mechanisms. This sparse attention pretraining mechanism forces model to focus on the most important information, potentially enhancing performance by filtering out noise from irrelevant attention pathways. The consistent performance across diverse evaluations also validates NSA’s robustness as a general-purpose architecture. 

**Long-Context Evaluation.** As shown in Figure 5, NSA achieves perfect retrieval accuracy across all positions in 64k-context needle-in-a-haystack (Kamradt, 2023) test. This performance stems from our hierarchical sparse attention design, which combines compression tokens for efficient global context scanning, and selection tokens for precise local information retrieval. The coarse-grained compression identifies relevant context blocks at low computational cost, while the token-level attention on selected tokens ensures the preservation of critical fine-grained information. This design enables NSA to maintain both global awareness and local precision. 

We also evaluate NSA on LongBench (Bai et al., 2023) against state-of-the-art sparse attention 

11 





Figure 5 | Needle-in-a-Haystack retrieval accuracy across context positions with 64k context length. NSA achieves perfect accuracy through its hierarchical sparse attention design.

---

[referencia=74cf7186aa6d419e score=0.987]
The proposed architecture achieves an effective trade-off between computation cost and model performance. For NSA, we set compression block size _𝑙_ = 32, sliding stride _𝑑_ = 16, selected block size _𝑙_<sup>′</sup> = 64, selected block count _𝑛_ = 16 (including fixed activating the 1 initial block and 2 local blocks), and sliding window size _𝑤_ = 512. Both Full Attention and sparse attention models are pretrained on 270B tokens of 8k-length texts, followed by continued training and supervised fine-tuning on 32k-length texts with YaRN (Peng et al., 2024) to achieve long-context adaptation. Both models are trained to full convergence to ensure fair comparison. As shown in Figure 4, the pretraining loss curve of our NSA and Full Attention baseline demonstrates stable and smooth decline, with NSA consistently outperforming the Full Attention model.

---

[referencia=74cf7186aa6d419e score=0.971]
11 





Figure 5 | Needle-in-a-Haystack retrieval accuracy across context positions with 64k context length. NSA achieves perfect accuracy through its hierarchical sparse attention design. 

methods and Full Attention baseline. To ensure consistent sparsity, we set the token activated by each query in all sparse attention baselines to 2560 tokens, which corresponds to the average number of tokens activated in NSA when handling 32k sequence lengths. Following StreamLLM (Xiao et al., 2023), this token budget includes the leading 128 tokens and 512 local tokens. We exclude certain subsets from LongBench due to their low scores across all models, which may not provide meaningful comparisons. As shown in Table 2, NSA achieves the highest average score 0.469, outperforming all baselines (+0.032 over Full Attention and +0.046 over Exact-Top). This improvement arises from two key innovations: (1) our native sparse attention design, which enables end-to-end optimization of sparse patterns during pretraining, facilitates synchronized adaptation between the sparse attention module and other model components; and (2) the hierarchical sparse attention mechanism achieves a balance between local and global information processing. 

Notably, NSA demonstrates exceptional performance on tasks requiring complex reasoning over long contexts, achieving +0.087 and +0.051 improvements over Full Attention on multi-hop QA tasks (HPQ and 2Wiki), exceeding the performance of baselines on code understanding (LCC: +0.069), and outperforming other methods on passage retrieval (PassR-en: +0.075). These results validate NSA’s capability to handle diverse long-context challenges, with its natively pretrained sparse attention providing additional benefits in learning task-optimal patterns.

---

[referencia=74cf7186aa6d419e score=0.968]
### **1. Introduction** 

The research community increasingly recognizes long-context modeling as a crucial capability for next-generation large language models, driven by diverse real-world applications ranging from in-depth reasoning (DeepSeek-AI, 2025; Zelikman et al., 2022), repository-level code generation (Zhang et al., 2023a; Zhang et al.) and multi-turn autonomous agent systems (Park et al., 2023). Recent breakthroughs, including OpenAI’s o-series models, DeepSeek-R1 (DeepSeek-AI, 2025), and Gemini 1.5 Pro (Google et al., 2024), enabling models to process entire codebases, lengthy documents, maintain coherent multi-turn conversations over thousands of tokens, and perform complex reasoning across long-range dependencies. However, the high complexity (Zaheer et al., 2020) of vanilla Attention (Vaswani et al., 2017) mechanisms emerges as a critical 

*Contribution during internship at DeepSeek-AI. 



<!-- Start of picture text -->
Performance on Benchmarks Speed on Stages<br>13.0<br>Full Attention 11.6×<br>0.5 NSA 11.0<br>9.0×<br>9.0<br>0.4<br>7.0<br>0.3 6.0×<br>5.0<br>0.2<br>3.0<br>0.1<br>1.0<br>0.0<br>General LongBench Reasoning Decode Forward Backward<br>Score<br>Speedup Ratio<br><!-- End of picture text -->

Figure 1 | Comparison of performance and efficiency between Full Attention model and our NSA. Left: Despite being sparse, NSA surpasses Full Attention baseline on average across general benchmarks, long-context tasks, and reasoning evaluation. Right: For 64k-length sequence processing, NSA achieves substantial computational speedup compared to Full Attention in all stages: decoding, forward propagation, and backward propagation. 

latency bottleneck as sequence length increases. Theoretical estimates indicate that attention computation with softmax architectures accounts for 70–80% of total latency when decoding 64k-length contexts, underscoring the urgent need for more efficient attention mechanisms.

---

[referencia=74cf7186aa6d419e score=0.960]
2 



<!-- Start of picture text -->
Native Sparse Attention Mechanism<br>Split to Continuous Blocks<br>Compressed Attention Mask<br>Compress Selection<br>Compression<br>Sliding Selected Attention Mask<br>Compressed Attention Selected Attention Sliding Attention<br>Sliding Attention Mask<br>Output Output Output<br>Gated Output Attention Score Query Token Activated Token Evicted Token Ignored Token<br>...<br>Concat<br>Top-n Selection<br><!-- End of picture text -->

Figure 2 | Overview of NSA’s architecture. Left: The framework processes input sequences through three parallel attention branches: For a given query, preceding keys and values are processed into compressed attention for coarse-grained patterns, selected attention for important token blocks, and sliding attention for local context. Right: Visualization of different attention patterns produced by each branch. Green areas indicate regions where attention scores need to be computed, while white areas represent regions that can be skipped. 

we implement specialized kernels to maximize its practical efficiency. NSA introduces two core innovations corresponding to the key requirements above: (1) Hardware-aligned system: Optimize blockwise sparse attention for Tensor Core utilization and memory access, ensuring balanced arithmetic intensity. (2) Training-aware design: Enable stable end-to-end training through efficient algorithms and backward operators. This optimization enables NSA to support both efficient deployment and end-to-end training. 

We evaluate NSA through comprehensive experiments on real-world language corpora. Pretraining on a 27B-parameter transformer backbone with 260B tokens, we assess NSA’s performance across general language evaluations, long-context evaluations, and chain-of-thought reasoning evaluation. We further compare the kernel speed on A100 GPUs with optimized Triton (Tillet et al., 2019) implementations. Experimental results demonstrate that NSA achieves comparable or superior performance to full attention baseline, while outperforming existing sparse attention approaches. Additionally, NSA delivers substantial speedups across decoding, forward, and backward stages compared to Full Attention, with the speedup ratio increasing for longer sequences. These results validate that our hierarchical sparse attention design effectively balances model capability and computational efficiency.

---

[referencia=74cf7186aa6d419e score=0.957]
### **5. Efficiency Analysis** 

We evaluate the computational efficiency of NSA against Full Attention on an 8-GPU A100 system. In efficiency analysis, we also configure the model with GQA group _𝑔_ = 4, heads per group _ℎ_ = 16, query/key dimension _𝑑𝑘_ = 192, and value dimension _𝑑𝑣_ = 128. Following the same settings in Section 4, we set NSA compression block size _𝑙_ = 32, sliding stride _𝑑_ = 16, selected block size _𝑙_<sup>′</sup> = 64, selected block count _𝑛_ = 16, and sliding window size _𝑤_ = 512. 

#### **5.1. Training Speed** 

We compare the Triton-based implementations of our NSA attention and Full Attention with Triton-based FlashAttention-2 to ensure fair speed comparison across the same backend. As shown in Figure 6, our NSA achieves progressively greater speedups as context length increases, up to 9.0× forward and 6.0× backward speedup at 64k context-length. Notably, the speed advantage becomes more pronounced with longer sequences. This speedup stems from our 

13 

|Context Length|8192|16384|32768|65536|
|---|---|---|---|---|
|Full Attention|8192|16384|32768|65536|
|NSA|2048|2560|3584|5632|
|Expected Speedup|**4**×|**6.4**×|**9.1**×|**11.6**×|



Table 4 | Memory access volume (in equivalent number of tokens) per attention operation during decoding. Due to the low arithmetic intensity and memory-bound nature of decoding, the expected speedup is approximately linear with the volume of memory access. 

hardware-aligned algorithm design to maximize the efficiency of sparse attention architecture: (1) The Blockwise memory access pattern maximizes Tensor Core utilization through coalesced loads, (2) The delicate loop scheduling in the kernel eliminates redundant KV transfers.

---

[referencia=74cf7186aa6d419e score=0.957]
#### **7.3. Query-Aware Selection** 

Other works focus on query-dependent token selection methods to reduce attention computation while preserving attention quality. Quest (Tang et al., 2024) employs a blockwise selection strategy where each chunk’s importance is estimated by product between query and coordinatewise min-max of the key chunks. InfLLM (Xiao et al., 2024a) combines fixed patterns with retrieval by maintaining attention sinks, local context, and retrievable chunks. This method selects representative keys from each chunk to estimate chunk importance. HashAttention (Desai et al., 2024) formulates pivotal token identification as a recommendation problem by mapping queries and keys to Hamming space using learned functions. ClusterKV (Liu et al., 2024) achieves sparsity by firstly clustering keys and then selecting the most relevant clusters for attention computation based on query-cluster similarity. MInference (Jiang et al., 2024) and TokenSelect (Wu et al., 2024) select KV pairs for computation based on token-level importance scoring. SeerAttention (Gao et al., 2024) separates queries and keys into spatial blocks and performs blockwise selection for efficient computation. Compared to these methods, our NSA 

16 

achieves hardware-aligned sparse attention computation throughout the full model lifecycle, including training, prefilling, and decoding. 

### **8. Conclusion** 

We present NSA, a hardware-aligned sparse attention architecture for efficient long-context modeling. By integrating hierarchical token compression with blockwise token selection within a trainable architecture, our architecture achieves accelerated training and inference while maintaining Full Attention performance. NSA advances the state-of-the-art by demonstrating general benchmark performance matches full-attention baselines, exceeding modeling capability in long-context evaluations, and enhanced reasoning ability, all accompanied by measurable reductions in computational latency and achieving significant speedup.

---

[referencia=74cf7186aa6d419e score=0.937]
### **4. Experiments** 

We evaluate NSA through three lenses: (1) general benchmarks performance, (2) long-context benchmarks performance, and (3) chain-of-thought reasoning performance, comparing against Full Attention baseline and state-of-the-art sparse attention methods. We defer the efficiency analysis of our sparse computation paradigm to Section 5, where we provide detailed discussions on training and inference speed.

---

[referencia=74cf7186aa6d419e score=0.923]
**Chain-of-Thought Reasoning Evaluation.** To evaluate NSA’s compatibility with advanced downstream training paradigms, we investigate its capacity to acquire chain-of-thought mathematical reasoning abilities via post-training. Given the limited effectiveness of reinforcement learning on smaller-scale models, we employ knowledge distillation from DeepSeek-R1, conducting supervised fine-tuning (SFT) with 10B tokens of 32k-length mathematical reasoning traces. This produces two comparable models: Full Attention-R (Full Attention baseline) and NSA-R (our sparse variant). We assess both models on the challenging American Invitational Mathematics Examination (AIME 24) benchmark. We use a sampling temperature of 0.7 and a top- _𝑝_ value of 0.95 to generate 16 responses for each question and obtain the average score. To validate the impact of reasoning depth, we conduct experiments with two generation context limits: 8k and 16k tokens, measuring whether extended reasoning chains improve accuracy. Example comparisons of model predictions are provided in Appendix A. 

12 

|Generation Token Limit|8192|16384|
|---|---|---|
|Full Attention-R|0.046|0.092|
|NSA-R|**0.121**|**0.146**|



Table 3 | AIME Instruction-based Evaluating after supervised fine-tuning. Our NSA-R demonstrates better performance than Full Attention-R at both 8k and 16k sequence lengths 



<!-- Start of picture text -->
Forward Time Comparison Backward Time Comparison<br>1000 FlashAttention-2 2500<br>Sparse Attention Kernel<br>Compression and<br>800 Window Attention 2000<br>9.0 × Speedup Ratio<br>600 1500 6.0×<br>9.0×<br>400 1000<br>200 500<br>6.3× 3.4×<br>2.1× 3 .8× 1.1× 2.0×<br>0 0<br>8k 16k 32k 64k 8k 16k 32k 64k<br>Time (ms)<br><!-- End of picture text -->

Figure 6 | Comparison of Triton-based NSA kernel with Triton-based FlashAttention-2 kernel. Our implementation significantly reduces latency across all context lengths, with the improvement becoming more pronounced as input length increases.

---

[referencia=74cf7186aa6d419e score=0.909]
#### **4.1. Pretraining Setup** 

Following the common practice in state-of-the-art LLMs, our experiments adopt a backbone combining Grouped-Query Attention (GQA) and Mixture-of-Experts (MoE), featuring 27B total parameters with 3B active parameters. The model consists of 30 layers with a hidden dimension of 2560. For GQA, we set the number of groups to 4, with a total of 64 attention heads. For each head, the hidden dimensions of the query, key, and value are configured as _𝑑𝑞_ = _𝑑𝑘_ = 192 and _𝑑𝑣_ = 128, respectively. For MoE, we utilize the DeepSeekMoE (Dai et al., 2024; DeepSeek-AI, 2024) structure, with 72 routed experts and 2 shared experts, and set the top-k experts to 6. To ensure training stability, the MoE in the first layer is replaced by an MLP in the form of SwiGLU. 

9 



<!-- Start of picture text -->
Taining Loss Curve<br>4.0<br>Full Attention<br>NSA<br>3.5<br>3.0<br>2.5<br>2.0<br>1.5<br>0 10000 20000 30000 40000 50000 60000<br>step<br>loss<br><!-- End of picture text -->

Figure 4 | Pretraining loss comparison between Full Attention and our NSA on 27B-parameter model. Both models exhibit stable convergence, with NSA achieving lower loss values.

---

[referencia=74cf7186aa6d419e score=0.896]
Table 2 | Performance comparison between our NSA and baselines on LongBench, including subsets in single document QA, multi-document QA, synthetic and code task categories. NSA outperformed most of the baselines including Full Attention. 

methods span diverse sparse attention paradigms, including KV-cache eviction, query-aware _𝑛_ selection, and exact top- sparse selection. 

For general evaluation, where most samples have lengths within the local context window of sparse attention baselines, these methods are effectively equivalent to Full Attention. Therefore, we present only the comparison results between NSA and Full Attention baseline in this setting. In the long-context evaluation, we conduct comparisons across all baseline methods, with the sparsity of all sparse attention methods set to the same to ensure a fair comparison. For chainof-thought reasoning evaluation, which requires long-text supervised fine-tuning, we limit our comparison to Full Attention, as sparse attention baselines do not support training.

---

[referencia=74cf7186aa6d419e score=0.867]
#### **6.1. Challenges with Alternative Token Selection Strategies** 

Before designing NSA, we explored adapting existing sparse attention methods to the training stage. However, these attempts encountered various challenges, prompting us to design a different sparse attention architecture: 

**Key-Clustering Based Strategies.** We examined clustering-based strategies like ClusterKV (Liu et al., 2024). These methods store Keys and Values from the same cluster in contiguous memory regions. While theoretically feasible for training and inference, they face three significant challenges: (1) Non-trivial computational overhead introduced by dynamic clustering mechanisms; (2) Operator optimization difficulties exacerbated by inter-cluster imbalances, especially in Mixture-of-Experts (MoE) systems, where skewed Expert Parallelism (EP) group execution times lead to persistent load imbalances; (3) Implementation constraints arising from the need for mandatory periodic reclustering and chunk-sequential training protocols. These combined factors create substantial bottlenecks, significantly limiting their effectiveness for real-world deployment. 

14 



<!-- Start of picture text -->
Training Loss Curve Visualization for Attention Score Block Pattern<br>3.2<br>Full Attention<br>Auxiliary Loss-based Learnable Selection<br>3.0 Heuristic Parameter-free Selection<br>NSA<br>2.8<br>2.6<br>2.4<br>position<br>2.2<br>0 5000 10000 15000 20000 25000 30000<br>step Figure 8 | Visualization of Attention Map | Visualization of Attention Map Visualization of Attention Map<br>position<br>loss<br><!-- End of picture text -->

Figure 8 | Visualization of Attention Map | Visualization of Attention Map Visualization of Attention Map on a Full Attention transformer. Lightcolored regions indicate higher attention values. As shown in the figure, attention scores exhibit blockwise clustering distribution. 

Figure 7 | Compare training loss on a 3Bparameter model with Full Attention and different token selection strategies and. Our NSA achieves better performance.

---

[referencia=74cf7186aa6d419e score=0.863]
#### **_3.3.3. Sliding Window_** 

In attention mechanisms, local patterns typically adapt faster and can dominate the learning process, potentially preventing the model from effectively learning from compression and selection tokens. To address this issue, we introduce a dedicated sliding window branch that explicitly handles local context, allowing other branches (compression and selection) to focus on learning their respective features without being shortcutted by local patterns. Specifically, we maintain recent tokens _𝐾_<sup>˜</sup> _𝑡_<sup>win</sup> = **k** _𝑡_ − _𝑤_ : _𝑡_ , _𝑉_<sup>˜</sup> _𝑡_<sup>win</sup> = **v** _𝑡_ − _𝑤_ : _𝑡_ in a window _𝑤_ , and isolate attention computations of different information sources (compression tokens, and selected tokens, sliding window) into separate branches. These branch outputs are then aggregated through a learned gating mechanism. To further prevent shortcut learning across attention branches with marginal computational overhead, we provide independent keys and values for three branches. This architectural design enables stable learning by preventing gradient interference between local and long-range pattern recognition, while introducing minimal overhead. 

After obtaining all three categories of keys and values ( _𝐾_<sup>˜</sup> _𝑡_<sup>cmp</sup> , _𝑉_<sup>˜</sup> _𝑡_<sup>cmp</sup> ; _𝐾_<sup>˜</sup> _𝑡_<sup>slc,</sup><sup>_𝑉_˜</sup> _𝑡_<sup>slc; and</sup><sup>_𝐾_˜</sup> _𝑡_<sup>win</sup> , _𝑉_<sup>˜</sup> _𝑡_<sup>win</sup> ), we compute the final attention output following Equation (5). Together with the compression, selection, and sliding window mechanisms described above, this forms the complete algorithmic framework of NSA.

---

[referencia=74cf7186aa6d419e score=0.856]
latency bottleneck as sequence length increases. Theoretical estimates indicate that attention computation with softmax architectures accounts for 70–80% of total latency when decoding 64k-length contexts, underscoring the urgent need for more efficient attention mechanisms. 

A natural approach to efficient long-context modeling is to take advantage of the inherent sparsity of softmax attention (Ge et al., 2023; Jiang et al., 2023), where selectively computing critical query-key pairs can significantly reduce computational overhead while preserving performance. Recent advances demonstrate this potential through diverse strategies: KV-cache eviction methods (Li et al., 2024; Zhang et al., 2023b; Zhou et al., 2024), blockwise KV-cache selection methods (Gao et al., 2024; Tang et al., 2024; Xiao et al., 2024a), and sampling, clustering or hashing-based selection methods (Chen et al., 2024b; Desai et al., 2024; Liu et al., 2024). Despite these promising strategies, existing sparse attention methods often fall short in practical deployments. Many approaches fail to achieve speedups comparable to their theoretical gains; moreover, most methods lack effective training-time support to fully exploit the sparsity patterns of attention. 

To address these limitations, the deployment of effective sparse attention must tackle two key challenges: (1) **_Hardware-aligned inference speedup_** : Converting theoretical computation reductions into actual speed improvements requires hardware-friendly algorithm design during both prefilling and decoding stages to mitigate memory access and hardware scheduling bottlenecks; (2) **_Training-aware algorithm design_** : Enabling end-to-end computation with trainable operators to reduce training costs while maintaining model performance. These requirements are crucial for real-world applications to achieve fast long-context inference or training. When considering both aspects, existing methods still exhibit a noticeable gap. 

To achieve more effective and efficient sparse attention, we present NSA, a Natively trainable Sparse Attention architecture that integrates hierarchical token modeling. As shown in Figure 2, NSA reduces per-query computation by organizing keys and values into temporal blocks and processing them through three attention paths: compressed coarse-grained tokens, selectively retained fine-grained tokens, and sliding windows for local contextual information. Then 

2 



<!-- Start of picture text -->

---

[referencia=74cf7186aa6d419e score=0.833]
Figure 4 | Pretraining loss comparison between Full Attention and our NSA on 27B-parameter model. Both models exhibit stable convergence, with NSA achieving lower loss values. 

|Model|MMLU<br>Acc. 5-shot|MMLU-PRO <br>Acc. 5-shot|CMMLU<br>Acc. 5-shot|BBH<br>Acc. 3-shot|GSM8K<br>Acc. 8-shot|MATH<br>Acc. 4-shot|DROP<br>F1 1-shot|MBPP<br>Pass@1 3-shot|HumanEval <br>Pass@1 0-shot|Avg.|
|---|---|---|---|---|---|---|---|---|---|---|
|Full Attn|**0.567**|0.279|0.576|0.497|0.486|0.263|0.503|**0.482**|0.335|0.443|
|NSA|0.565|**0.286**|**0.587**|**0.521**|**0.520**|**0.264**|**0.545**|0.466|**0.348**|**0.456**|



Table 1 | Pretraining performance comparison between the full attention baseline and NSA on general benchmarks, across knowledge (MMLU, MMLU-PRO, CMMLU), reasoning (BBH, GSM8K, MATH, DROP), and coding (MBPP, HumanEval) tasks. NSA achieves superior average performance on most benchmarks despite high sparsity.

---

[referencia=74cf7186aa6d419e score=0.772]
#### **4.2. Baselines Methods** 

In addition to comparing with Full Attention, we evaluate several state-of-the-art inferencestage sparse attention methods: H2O (Zhang et al., 2023b), infLLM (Xiao et al., 2024a), Quest _𝑛_ (Tang et al., 2024), and Exact-Top, which first computes full attention score and select the topscores keys corresponding to each query and then calculates attention on these positions. These 

10 

|Model||SQA|||M|QA||Synt|hetic|Code|Avg.|
|---|---|---|---|---|---|---|---|---|---|---|---|
||MFQA-en|MFQA-zh|Qasper|HPQ|2Wiki|GovRpt|Dur|PassR-en|PassR-zh|LCC||
|H2O|0.428|0.429|0.308|0.112|0.101|0.231|0.208|0.704|0.421|0.092|0.303|
|InfLLM|0.474|0.517|0.356|0.306|0.250|0.277|0.257|0.766|0.486|0.143|0.383|
|Quest|0.495|0.561|0.365|0.295|0.245|0.293|0.257|0.792|0.478|0.135|0.392|
|Exact-Top|0.502|0.605|0.397|0.321|0.288|0.316|0.291|0.810|0.548|0.156|0.423|
|Full Attn|**0.512**|0.623|0.409|0.350|0.305|**0.324**|0.294|0.830|**0.560**|0.163|0.437|
|NSA|0.503|**0.624**|**0.432**|**0.437**|**0.356**|0.307|**0.341**|**0.905**|0.550|**0.232 **|**0.469**|

---

[referencia=74cf7186aa6d419e score=0.745]
Figure 7 | Compare training loss on a 3Bparameter model with Full Attention and different token selection strategies and. Our NSA achieves better performance. 

**Other Blockwise Selection Strategies.** We also considered blockwise key, value selection strategies different from NSA, such as Quest (Tang et al., 2024) and InfLLM (Xiao et al., 2024a). _𝑛_ These methods rely on computing an importance score for each KV block and selecting the topblocks based on their similarity with _𝑞𝑡_ . However, existing methods face two critical issues: (1) Since the selection operation is non-differentiable, importance score computation based on neural networks relies on auxiliary loss, which increases operator overhead and often degrades model performance; (2) Heuristic parameter-free importance score computation strategy suffer from low recall rates, leading to suboptimal performance. We evaluate both approaches on a 3B-parameter model with similar architecture and compare their loss curve with NSA and Full Attention. For the auxiliary loss-based selection method, we introduce additional queries for each token and representative keys for each block to estimate the block importance scores. We compute block-level supervision signals by mean-pooling attention scores within each key block, and use KL divergence to supervise block importance prediction. We maintain individual query granularity instead of block-averaged queries to accommodate efficient decoding. This auxiliary loss-based importance estimation shares conceptual similarity with SeerAttention (Gao et al., 2024). For the heuristic parameter-free selection method, following the strategy of Quest, we implement direct selection using the product between queries and coordinate-wise min-max of the key chunks, without introducing additional parameters. We also explore a cold-start training approach where Full Attention is applied for the initial 1000 steps before transitioning to the heuristic blockwise selection. As shown in Figure 7, both methods exhibited inferior loss.

---

[referencia=74cf7186aa6d419e score=0.731]
#### **3.2. Overall Framework** 

To leverage the potential of attention with natural sparse pattern, we propose replacing the original key-value pairs **k** : _𝑡_ , **v** : _𝑡_ in Equation (1) with a more compact and information-dense set of representation key-value pairs _𝐾_<sup>˜</sup> _𝑡_ , _𝑉_<sup>˜</sup> _𝑡_ given each query **q** _𝑡_ . Specifically, we formally define the optimized attention output as follows: 





where _𝐾_<sup>˜</sup> _𝑡_ , _𝑉_<sup>˜</sup> _𝑡_ are dynamically constructed based on the current query **q** _𝑡_ and the contextual memory **k** : _𝑡_ , **v** : _𝑡_ . We can design various mapping strategies to get different categories of _𝐾_<sup>˜</sup> _𝑡_<sup>_𝑐_,</sup><sup>_𝑉_˜</sup> _𝑡_<sup>_𝑐_,</sup> and combine them as follows: 



As illustrated in Figure 2, NSA have three mapping strategies C = {cmp, slc, win}, representing compression, selection, and sliding window for keys and values. _𝑔𝑡_<sup>_𝑐_∈[0, 1]is the gate score for</sup> corresponding strategy _𝑐_ , derived from input features via an MLP and sigmoid activation. Let _𝑁𝑡_ denote the total number of remapped keys/values: 



We maintain a high sparsity ratio by ensuring _𝑁𝑡_ ≪ _𝑡_ . 

#### **3.3. Algorithm Design** 

In this subsection, we introduce the design of our remapping strategies _𝑓𝐾_ and _𝑓𝑉_ : token compression, token selection, and sliding window.

---

[referencia=74cf7186aa6d419e score=0.728]
Figure 6 | Comparison of Triton-based NSA kernel with Triton-based FlashAttention-2 kernel. Our implementation significantly reduces latency across all context lengths, with the improvement becoming more pronounced as input length increases. 

As shown in Table 3, NSA-R achieves significantly higher accuracy than Full Attention-R under the 8k context setting (+0.075), with this advantage persisting at 16k contexts (+0.054). These results validate two key benefits of native sparse attention: (1) The pretrained sparse attention patterns enable efficient capture of long-range logical dependencies critical for complex mathematical derivations; (2) Our architecture’s hardware-aligned design maintains sufficient context density to support growing reasoning depth without catastrophic forgetting. The consistent outperformance across context lengths confirms sparse attention’s viability for advanced reasoning tasks when natively integrated into the training pipeline.