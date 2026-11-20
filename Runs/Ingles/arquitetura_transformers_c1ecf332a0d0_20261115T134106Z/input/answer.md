# The Transformer Architecture: Attention Mechanisms and the Architectural Foundation of Large Language Models

Introduced in 2017 by Vaswani and colleagues, the Transformer architecture redesigned neural sequence modeling by replacing recurrence and convolution entirely with self-attention mechanisms[1]. Rather than stepping hidden states sequentially across a sequence, self-attention connects every token position directly to every other position in a constant number of sequential operations, unlocking large-scale GPU parallelization while shortening long-range dependency paths[2]. Over the following decade, this architecture—particularly in its causal decoder-only configuration—became the computational foundation of large language models (LLMs), enabling zero-shot generalization, few-shot in-context adaptation, multilinguality, coding, reasoning, and tool usage[8].

Understanding how the Transformer supports frontier LLMs requires examining the interaction of every sub-component alongside the scaling bottlenecks that emerge at large context lengths and parameter counts. Pure self-attention stacked without skip connections and multilayer perceptrons loses representation rank doubly exponentially with depth, while position-wise feed-forward networks (FFNs) act as key-value memories that compose distributed information across layers[12]. As models scaled, self-attention's quadratic complexity per layer and growing key-value (KV) cache footprint shifted inference constraints toward memory bandwidth, spurring grouped-query and latent cache compression, IO-aware exact kernels, and sparse Mixture-of-Experts (MoE) routing[6]. At the same time, theoretical complexity bounds show that fixed-depth, log-precision Transformers remain limited to constant-depth threshold circuits[19], while competitive selective state-space models and Transformer-Mamba hybrids continue testing the necessity of pure quadratic attention[20].

## From Sequential Bottlenecks to Parallel Self-Attention

Prior to the Transformer, competitive sequence transduction systems relied largely on recurrent neural networks (RNNs), particularly Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks arranged in encoder-decoder pipelines[2]. Early sequence-to-sequence models demonstrated that deep LSTMs could map variable-length input strings to target sequences, though optimization proved sensitive enough that reversing source-sentence word order markedly improved translation by shortening dependencies between corresponding source and target words[23]. Secondary technical analyses of Cho and colleagues' 2014 RNN encoder-decoder note that flattening all sequential structure from a variable-length input into a single fixed-width context vector created an acute representational bottleneck[24]. Even large recurrent translation systems—such as an eight-layer 380-million-parameter LSTM setup documented in encyclopedic retrospectives, where only the first encoder layer was bidirectional and the remaining seven encoder and eight decoder layers were unidirectional—required nine months to develop[5].

Attention mechanisms first emerged to relieve this fixed-vector bottleneck within recurrent encoders and decoders rather than replace recurrence altogether[25]. Bahdanau, Cho, and Bengio introduced an alignment module enabling a neural translation decoder to compute a dynamic context vector at each output step as a weighted average over all encoder source hidden states[25]. Neural machine translation surveys note that Bahdanau's additive alignment function applied a hyperbolic tangent (tanh) transformation across decoder and encoder states[27]. Luong, Pham, and Manning subsequently simplified and generalized this mechanism into global and local attention variants, altering the recurrent state-update flow while still filtering training sentence pairs exceeding 50 words[25].

Researchers soon applied attention within a single sequence rather than solely across encoder-decoder boundaries[28]. Cheng, Dong, and Lapata integrated intra-attention into LSTM-Networks (LSTMN) for machine reading, language modeling, sentiment analysis, and natural language inference[28]. However, academic seminar reviews observe that embedding self-attention inside an LSTM still preserved sequential recurrent execution[29]. Parallel work by Gehring and colleagues replaced recurrence with stacked convolutions in ConvS2S, outperforming deep LSTM baselines on WMT 2014 English-German and English-French translation at an order-of-magnitude speedup on both GPUs and CPUs[30]. Nevertheless, convolutional layers still required stacked hierarchies to connect distant sequence positions, motivating an architecture built solely on attention[1].

## Core Mechanics of the Original Transformer

The 2017 Transformer resolved the tension between hardware parallelization and global dependency modeling by discarding both recurrence and convolution[1]. Vaswani and colleagues evaluated layer designs for sequence length  and representation dimension  along three metrics: computational complexity per layer, minimum sequential operations, and maximum path length between any two positions[6]. Recurrent layers require  operations per layer,  sequential operations, and an  maximum path length[6]. Secondary analyses of the paper's table note that convolutional layers with kernel width  achieve  sequential operations at  complexity, yet require  path length even under dilated convolutions[7]. Self-attention incurs  complexity per layer while maintaining  sequential operations and an  maximum path length across all token pairs[6]. When  is smaller than , as in sentence-level translation, self-attention is faster per layer than recurrence[7], though quadratic scaling with  later becomes a central bottleneck for long-context LLMs[17].

At the mathematical center of the Transformer is Scaled Dot-Product Attention, which maps a query matrix  and key matrix  of dimension , alongside a value matrix  of dimension , to a weighted sum of values[2]:

The scaling factor  counters a specific optimization pathology[2]. Although additive attention and unscaled dot-product attention perform similarly at small , additive attention outperforms unscaled dot-product attention for larger [2]. Vaswani and colleagues illustrated why by modeling query and key components as independent random variables with mean zero and variance one: their dot product  has mean zero and variance , meaning dot-product magnitudes grow like [2]. Unscaled logits push the softmax function into regions with extremely small gradients, whereas dividing by  stabilizes pre-softmax logit scale regardless of head dimensionality[2].

Rather than computing a single attention map at full embedding width , the Transformer uses Multi-Head Attention[2]. The model applies  learned linear projections  to map queries, keys, and values into lower-dimensional subspaces, evaluates attention in parallel, concatenates the resulting head outputs, and mixes them through an output projection [2]:

Structured paper extractions and seminar notes confirm that the 2017 base model used  heads with  (corresponding to [32]), keeping total computation comparable to a single full-dimensional head while preventing weighted averaging from collapsing information across distinct representation subspaces[2]. Those extraction notes also record that the original ablations found a single head degraded translation quality by roughly 0.9 BLEU, while subdividing into too many tiny heads likewise hurt performance[4].

The original Transformer arranged these operations into encoder and decoder stacks of  identical layers[2]. Each encoder layer paired multi-head self-attention with a position-wise fully connected FFN, applying residual connections and layer normalization after each sub-layer (Post-LN)². Each decoder layer added a multi-head cross-attention sub-layer over the encoder output and masked its own self-attention to block positions from attending to subsequent tokens, preserving autoregression[3]. Because pure attention contains no recurrence or convolution, Vaswani and colleagues added deterministic sinusoidal positional encodings to the input embeddings[3]:

This encoding allows the model to learn relative positions and potentially extrapolate to longer sequences than seen in training[3]. Empirically, the Transformer reached 28.4 BLEU on WMT 2014 English-to-German (beating prior bests by over 2.0 BLEU) and 41.0 BLEU on WMT 2014 English-to-French while training its base model in 12 hours on 8 NVIDIA P100 GPUs and generalizing effectively to English constituency parsing[1]. By 2026, encyclopedic records count over 150,000 citations to the paper, placing it among the ten most-cited works of the twenty-first century[5].

## Inside the Transformer Block: Head Specialization, Memory, and Optimization Stability

Later empirical and theoretical work challenged the view that self-attention alone drives Transformer capability. In 2019, Michel, Levy, and Neubig examined whether sixteen heads are genuinely better than one, analyzing which model components rely most on multiple heads and presenting preliminary evidence that training dynamics contribute to multi-head attention's gains[33]. Concurrently, Voita and colleagues demonstrated that specialized heads perform the critical work while redundant heads can be pruned without major accuracy loss; on WMT English-Russian translation, removing 38 of 48 encoder heads lowered BLEU by only 0.15 points[34].

Surrounding residual and FFN components proved mathematically essential for preserving representation geometry. Dong, Cordonnier, and Loukas (2021) demonstrated theoretically and verified experimentally that pure attention stacked without skip connections or MLPs loses rank doubly exponentially with depth, degenerating token representations across layers[13]. Residual skip connections and FFNs arrest this rank collapse[13]. Moreover, Geva and colleagues (2021) established that Transformer FFN layers operate as key-value memories whose outputs compose distributed memories refined progressively along the residual stream[12]. Secondary architectural guides explain that columns of the first FFN projection matrix () detect input patterns like keys while rows of the second matrix () contribute associated values, helping explain why substantial factual knowledge resides in FFNs rather than attention[32].

Scaling Transformers deeper also prompted critical revisions to normalization and gating. Xiong and colleagues (2020) analyzed layer normalization placement, and secondary breakdowns summarize how shifting normalization from after residual addition (Post-LN) to before each sub-layer (Pre-LN) stabilizes training and reduces reliance on delicate learning-rate warm-up schedules[32]. Zhang and Sennrich (2019) proposed Root Mean Square Layer Normalization (RMSNorm), achieving performance comparable to standard LayerNorm while cutting runtime by 7% to 64% across diverse architectures[36]. In the FFN sub-layer, Shazeer (2020) showed that replacing standard activations with Gated Linear Unit (GLU) variants—component-wise products of linear projections—consistently improves Transformer quality[37].

Even with  scaling and Pre-LN, training multi-billion-parameter Transformers exposed fragile attention-softmax dynamics. Zhai and colleagues (2023) identified attention entropy collapse as a primary driver of training instability[38]. Hoffmann and colleagues (2024) analyzed this failure mode in detail, noting that both overly sharp low-entropy distributions—which drive every entry of the softmax Jacobian near zero—and overly uniform attention cause vanishing gradients for  and [39]. Because attention entropy collapse grows severe above 8 billion parameters, large models adopted measures such as applying layer normalization to  before softmax or using NormSoftmax to regulate logit variance and attention temperature[39]. Low-precision arithmetic creates further late-training hazards: Chen and colleagues (2026) showed that broken symmetry in BF16 FlashAttention kernels can make gradients blow up late in training, cutting median query and key gradient errors from 219% and 13% down to 0.34% and 0.37% (matching FP32 loss trajectories) for 4.7% extra step time, whereas FlashAttention-3 and key smoothing both destabilized in matched from-scratch runs[40].

## Architectural Divergence, Tokenization, Scaling Laws, and Emergence

Following the original encoder-decoder blueprint, Transformer NLP bifurcated into three primary configurations[8]. Encoder-only models led by BERT (Devlin and colleagues, 2018)—which used 12 heads and  in BERT-base according to secondary guides[32]—pretrained deep bidirectional representations via masked language modeling (MLM), advancing SQuAD v1.1 Test F1 to 93.2 and SQuAD v2.0 Test F1 to 83.1[8]. Encoder-decoder models such as T5 (Raffel and colleagues, 2019) preserved bidirectional encoding alongside causal decoding within a unified text-to-text setup[8]. Causal decoder-only models, however, ultimately anchored general-purpose LLMs after GPT-3 (Brown and colleagues, 2020) demonstrated strong few-shot task execution from prompts alone and generated news articles difficult for human evaluators to distinguish from human writing[11]. Systematic architecture ablations by Wang and colleagues (2022) confirmed that causal decoder-only models trained with autoregressive causal language modeling (CLM) exhibit the strongest zero-shot generalization after unsupervised pretraining[8], establishing the paradigm extended across Llama 3, Llama 3.1, and Qwen2[10].

Downstream LLM efficiency and equity also depend heavily on subword tokenization at the input boundary. Subword segmentation techniques introduced by Sennrich, Haddow, and Birch for rare words[44] and language-independent SentencePiece by Kudo and Richardson[45] enabled open-vocabulary generation with bounded embedding tables. Yet Petrov and colleagues (2023) demonstrated that language model tokenizers introduce systematic unfairness across languages[46]. Technical notes summarizing their findings report token-count disparities up to 15x between languages for equivalent content—raising API costs and shrinking effective context windows—while noting that subword chunking blinds models to raw character composition[47]. To counter cross-lingual disparities, multilingual efforts such as Poro 34B trained custom 128K-token byte-level Byte Pair Encoding (BPE) vocabularies balanced across Finnish, English, and code[48].

Over the same period, empirical scaling laws governed how pretraining compute translated into loss reductions. Kaplan and colleagues (2020) observed smooth power-law relationships for cross-entropy loss and argued that sample efficiency favored training very large models on modest data and stopping well before convergence[49]. Hoffmann and colleagues (2022) revised this prescription in the Chinchilla study, increasing the emphasis on training token volume relative to model size[48]; Chinchilla outperformed Gopher by over 7% to reach 67.5% average accuracy on MMLU[50]. Sardana and colleagues (2024) subsequently incorporated inference costs into scaling theory, showing that lifetime cost optimality favors training smaller models on significantly larger datasets past Chinchilla ratios[48]—aligning with frontier runs such as DeepSeek-V3's 14.8 trillion pretraining tokens[52].

Whether smooth loss curves conceal discontinuous capability leaps remains contested. Wei and colleagues (2022) documented "emergent abilities" absent in smaller models that appear at larger scales and cannot be predicted by extrapolating small-model performance[53]. Schaeffer, Miranda, and Koyejo (2023) countered that such apparent discontinuities often evaporate under continuous metrics or improved statistics, describing them as artifacts of discontinuous evaluation metrics rather than fundamental scaling properties[39]. Providing middle-ground mechanistic evidence, Hoffmann and colleagues (2024) observed sudden "Eureka-moments" even under continuous metrics in multi-step tasks when softmax attention overcomes gradient bottlenecks[39], and Edelman and colleagues (2024) documented phase transitions as layers align from unigram to bigram models on in-context Markov chains[55].

## In-Context Algorithms and Theoretical Expressivity Limits

A defining property of Transformer LLMs is their ability to adapt to novel tasks using only examples inside the prompt[56]. Mechanistic interpretability attributes a major share of this behavior to induction heads—circuits spanning at least two attention layers that implement the pattern-completion rule [A][B] ... [A] -> [B][32]. Olsson and colleagues (2022) presented strong causal evidence in small attention-only models and correlational evidence in larger MLP-equipped models linking induction-head formation to in-context learning[58]. Extending this account, Edelman and colleagues (2024) showed that Transformers learn statistical induction heads that compute posterior conditional probabilities approaching the Bayes-optimal predictor on in-context Markov chains[55].

A complementary line of theory frames attention layers as implicit optimization algorithms executing in a single forward pass. Akyürek and colleagues (2023) showed constructively that Transformers can implement gradient descent and closed-form ridge regression over linear models encoded in prompts[57]. Independently, von Oswald and colleagues (2023) demonstrated that a linear self-attention layer can directly transform prompt data equivalently to one gradient-descent step on a linear regression loss without explicitly materializing weights, while multi-layer models perform curvature correction (GD++)[56]—later analyzed as a second-order solver converging in under 10 layers where standard gradient descent needs roughly 100 iterations[60]. Dai and colleagues likewise interpreted relaxed linear attention's dual relationship with gradient descent as implicit meta-optimization[59]. Still, recent studies caution that constructive expressivity does not automatically demonstrate what gradient-descent training learns in practice[61], and Bhattamishra and colleagues (2023) showed empirically that while Transformers select sample-efficient algorithms given informative teaching sequences, they perform no better than random guessing on Boolean parity functions[62].

Formal complexity theory clarifies these structural boundaries. Hahn (2020) established theoretical limitations of pure self-attention across formal sequence tasks[63]. Building on circuit complexity, Merrill and Sabharwal (2023) proved a fundamental parallelism tradeoff: the same  parallel depth that allows log-precision Transformers to train efficiently confines any fixed-depth forward pass to the expressive power of constant-depth threshold circuits, suggesting an inherent ceiling on serial computation within a single forward pass[19].

## Scaling Attention to Frontier LLMs: Memory Walls, Sparsity, and Sub-Quadratic Hybrids

Extending the Transformer from 2017 sentence lengths to long-context frontier LLMs required overcoming positional extrapolation limits, KV-cache memory bottlenecks, and quadratic prefill compute. Fixed sinusoidal encodings gave way to Rotary Position Embedding (RoPE) in RoFormer (Su and colleagues, 2021)[64] and Attention with Linear Biases (ALiBi) (Press, Smith, and Lewis, 2022), whose recency bias enables length extrapolation and outperforms multiple strong positional methods on WikiText-103[65]. For pretrained RoPE checkpoints, Positional Interpolation (Chen and colleagues, 2023) extended windows while preserving existing infrastructure[66], and YaRN (Peng and colleagues, 2023) enabled efficient extension and extrapolation past fine-tuning sequence lengths[67]. Even with wider windows, Liu and colleagues (2023) showed in "Lost in the Middle" that models exhibit uneven utilization of information across long contexts[68], while Xiao and colleagues (2024) demonstrated with StreamingLLM that accounting for attention sinks accelerates streaming generation by up to 22.2x over sliding-window recomputation[69].

During autoregressive decoding, caching past Key and Value vectors prevents recomputing history at every token, but turns KV cache size and memory bandwidth into the primary constraint on long-context serving[17]. Shazeer (2019) introduced Multi-Query Attention (MQA) to share a single K/V head across all query heads, speeding up decoding with minor quality loss[18]. Ainslie and colleagues (2023) balanced quality and speed with Grouped-Query Attention (GQA), grouping query heads to share K/V projections and showing uptrained GQA matches MHA quality at MQA-like speed[15], leading to adoption in Llama 3.1 and Qwen2[43]. DeepSeek-V2 and DeepSeek-V3 pushed cache compression further with Multi-Head Latent Attention (MLA)[14]. As an independent engineering analysis details, MLA caches a 512-element compressed joint KV latent alongside a 64-element shared decoupled RoPE key—576 elements per token per layer compared with 32,768 in a counterfactual 128-head, 128-dimension MHA layer (1.76% of MHA's entries)—and absorbs up-projections into query and output matrices during memory-bound decode[18]. While DeepSeek-V2 reported a 93.3% KV cache reduction and 5.76x maximum generation throughput alongside ablations outperforming MHA, that same independent analysis notes face-value arithmetic spans roughly 82% to 98.2% depending on whether GQA-8 or counterfactual MHA serves as the baseline[18].

Simultaneously, kernel engineering and conditional sparsity addressed quadratic prefill compute and dense FFN cost. Dao and colleagues (2022) introduced IO-aware exact FlashAttention, speeding up BERT-large (512 tokens) by 15%, GPT-2 (1K) by 3x, and Long-Range Arena (1K–4K) by 2.4x while enabling 16K to 64K sequence benchmarks[16]. FlashAttention-2 improved GPU parallelism and work partitioning to reach up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization)[72], and FlashAttention-3 harnessed hardware asynchrony and low precision so FP8 FlashAttention-3 cut numerical error by 2.6x relative to baseline FP8 attention[73]. Recent 2026 research pairs dense layers with oracle-guided sparse prefill—reporting preliminary single-card time-to-first-token speedups of 1.71x to 1.93x over FlashAttention-2 across 4K to 100K RULER sweeps within 0.48 points[74]—and integrates sparse attention designs like NSA and MoBA into models including MiniCPM4, Kimi, and DeepSeek-V3.2[17]. On the FFN side, Switch Transformers (Fedus, Zoph, and Shazeer, 2022) scaled sparse MoE routing to trillion-parameter pretraining at a 4x speedup over T5-XXL[75]. DeepSeek-V3 extended MoE to 671B main parameters (685B including 14B Multi-Token Prediction weights) with 37B active per token—an 18:1 parameter-to-compute ratio—training stably on 14.8 trillion tokens with auxiliary-loss-free load balancing and zero irrecoverable loss spikes[14]. Yet 2026 systems profiling shows MoE introduces distinct overheads: unoptimized multi-node all-to-all dispatch can occupy up to 60% of training time, small expert matrix multiplications drop below 50% of execution time (versus roughly 70% in dense Llama-3 405B), and routing adds roughly 9% layer overhead[76].

Finally, attention's quadratic scaling revived sub-quadratic alternatives and hybrid models. Katharopoulos and colleagues (2020) showed that replacing softmax with kernel feature maps casts causal linear attention as an RNN, accelerating autoregressive prediction on long sequences by up to 4000x[29]. Gu and Dao introduced selective state spaces in Mamba (2023), whose linear-time 3B model outperformed equal-sized Transformers and matched twice-as-large Transformers[20], before Dao and Gu (2024) unified structured SSMs and masked linear attention via Structured State Space Duality (SSD) in Mamba-2 at 2x to 8x higher speed[21]. Because empirical benchmarks still show sub-quadratic inference models lagging Transformers on certain tasks[62], hybrid architectures such as Jamba (Lieber and colleagues, 2024) combine Transformer and Mamba layers[22], underscoring that self-attention remains indispensable for high-precision relational computation even as surrounding architectures optimize its memory and compute footprint.

## Referências

[1] [1706.03762] Attention Is All You Need - arXiv, https://arxiv.org/abs/1706.03762
[2] Attention is All you Need - NIPS, https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf?utm_source=nationaltribune&utm_medium=nationaltribune&utm_campaign=news
[3] Attention Is All You Need | alphaXiv, https://www.alphaxiv.org/abs/1706.03762v4
[4] Process arXiv:1706.03762 — Attention Is All You Need, https://huggingface.co/datasets/attention-wiki/knowledge-base/commit/597b4e5675fb2ddd291e75a886eedc568c6fedc2
[5] Attention Is All You Need - Wikipedia, https://en.wikipedia.org/wiki/Attention_Is_All_You_Need
[6] arXiv:1706.03762v7 [cs.CL] 2 Aug 2023, https://arxiv.org/pdf/1706.03762
[7] (PDF) Tensor2Tensor for Neural Machine Translation - ResearchGate, https://www.researchgate.net/publication/323904682_Tensor2Tensor_for_Neural_Machine_Translation
[8] Enhancing Instruction-Following Capabilities in Seq2Seq Models, https://arxiv.org/html/2512.03803v1
[9] What Language Model Architecture and Pretraining Objective Work, https://arxiv.org/abs/2204.05832
[10] [2407.21783] The Llama 3 Herd of Models - arXiv, https://arxiv.org/abs/2407.21783
[11] [2005.14165] Language Models are Few-Shot Learners - arXiv, https://arxiv.org/abs/2005.14165
[12] Transformer Feed-Forward Layers Are Key-Value Memories - arXiv, https://arxiv.org/abs/2012.14913
[13] Pure Attention Loses Rank Doubly Exponentially with Depth - arXiv, https://arxiv.org/abs/2103.03404
[14] [2412.19437] DeepSeek-V3 Technical Report - arXiv, https://arxiv.org/abs/2412.19437
[15] GQA: Training Generalized Multi-Query Transformer Models ... - arXiv, https://arxiv.org/abs/2305.13245
[16] FlashAttention: Fast and Memory-Efficient Exact Attention with IO, https://arxiv.org/abs/2205.14135
[17] A Survey of Large Language Models - Hep Journals, https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60308-3
[18] From 390 KB to 890 Bytes — DeepSeek's KV Cache Optimization, https://local-ai-zone.github.io/blog/deepseek-kv-cache-optimization-research-paper.html
[19] The Parallelism Tradeoff: Limitations of Log-Precision Transformers, https://arxiv.org/abs/2207.00729
[20] Mamba: Linear-Time Sequence Modeling with Selective State Spaces, https://arxiv.org/abs/2312.00752
[21] Transformers are SSMs: Generalized Models and Efficient ... - arXiv, https://arxiv.org/abs/2405.21060
[22] Jamba: A Hybrid Transformer-Mamba Language Model - arXiv, https://arxiv.org/abs/2403.19887
[23] [1409.3215] Sequence to Sequence Learning with Neural Networks, https://arxiv.org/abs/1409.3215
[24] A History of Large Language Models - Gregory Gundersen, https://gregorygundersen.com/blog/2025/10/01/large-language-models/
[25] arXiv:1508.04025v5 [cs.CL] 20 Sep 2015, https://arxiv.org/pdf/1508.04025
[26] Neural Machine Translation by Jointly Learning to Align and ... - arXiv, https://arxiv.org/abs/1409.0473
[27] (PDF) A Survey of Deep Learning Techniques for Neural Machine, https://www.researchgate.net/publication/339350384_A_Survey_of_Deep_Learning_Techniques_for_Neural_Machine_Translation
[28] Long Short-Term Memory-Networks for Machine Reading - arXiv, https://arxiv.org/abs/1601.06733
[29] Chapter 8 Attention and Self-Attention for NLP, https://slds-lmu.github.io/seminar_nlp_ss20/attention-and-self-attention-for-nlp.html
[30] [1705.03122] Convolutional Sequence to Sequence Learning - arXiv, https://arxiv.org/abs/1705.03122
[31] Attention Is All You Need: Transformer Architecture - ScaleDojo, https://scaledojo.dev/papers/attention-is-all-you-need
[32] Opening the Black Box of LLM Inference: Foundations of Generative AI, https://medium.com/@aridiosilva/opening-the-black-box-of-llm-inference-foundations-of-generative-ai-65f6d3563bd2
[33] [1905.10650] Are Sixteen Heads Really Better than One? - arXiv, https://arxiv.org/abs/1905.10650
[34] Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned, https://arxiv.org/abs/1905.09418
[35] On Layer Normalization in the Transformer Architecture - arXiv, https://arxiv.org/abs/2002.04745
[36] [1910.07467] Root Mean Square Layer Normalization - arXiv, https://arxiv.org/abs/1910.07467
[37] [2002.05202] GLU Variants Improve Transformer - arXiv, https://arxiv.org/abs/2002.05202
[38] Stabilizing Transformer Training by Preventing Attention Entropy, https://arxiv.org/abs/2303.06296
[39] Eureka-Moments in Transformers:Multi-Step Tasks Reveal Softmax, https://arxiv.org/html/2310.12956v2
[40] Broken Symmetry in BF16 Attention: Why FlashAttention Gradients, https://arxiv.org/abs/2609.34272
[41] BERT: Pre-training of Deep Bidirectional Transformers for Language, https://arxiv.org/abs/1810.04805
[42] Exploring the Limits of Transfer Learning with a Unified Text-to-Text, https://arxiv.org/abs/1910.10683
[43] (PDF) A Survey of Large Language Models - ResearchGate, https://www.researchgate.net/publication/404686943_A_Survey_of_Large_Language_Models
[44] Neural Machine Translation of Rare Words with Subword Units - arXiv, https://arxiv.org/abs/1508.07909
[45] SentencePiece: A simple and language independent subword, https://arxiv.org/abs/1808.06226
[46] Language Model Tokenizers Introduce Unfairness Between ... - arXiv, https://arxiv.org/abs/2305.15425
[47] LLM Engineering - Pattern is Everything, https://patterniseverything.com/llm/
[48] Poro 34B and the Blessing of Multilinguality - arXiv, https://arxiv.org/html/2404.01856v3
[49] [2001.08361] Scaling Laws for Neural Language Models - arXiv, https://arxiv.org/abs/2001.08361
[50] Training Compute-Optimal Large Language Models - arXiv, https://arxiv.org/abs/2203.15556
[51] Accounting for Inference in Language Model Scaling Laws - arXiv, https://arxiv.org/abs/2401.00448
[52] Trace - lecture_01 - Stanford CS336, https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json
[53] [2206.07682] Emergent Abilities of Large Language Models - arXiv, https://arxiv.org/abs/2206.07682
[54] Are Emergent Abilities of Large Language Models a Mirage? - arXiv, https://arxiv.org/abs/2304.15004
[55] The Evolution of Statistical Induction Heads: In-Context Learning, https://arxiv.org/html/2402.11004v1
[56] Transformers Learn In-Context by Gradient Descent - arXiv, https://arxiv.org/pdf/2212.07677
[57] What learning algorithm is in-context learning? Investigations with, https://arxiv.org/abs/2211.15661
[58] [2209.11895] In-context Learning and Induction Heads - arXiv, https://arxiv.org/abs/2209.11895
[59] arXiv:2311.00237v3 [cs.CL] 3 Oct 2024, https://arxiv.org/pdf/2311.00237
[60] Linear Transformers are Versatile In-Context Learners - arXiv, https://arxiv.org/html/2402.14180v2
[61] How Transformers Learn Causal Structure with Gradient Descent, https://arxiv.org/html/2402.14735v2
[62] Understanding In-Context Learning in Transformers and LLMs by, https://arxiv.org/html/2310.03016v1
[63] Theoretical Limitations of Self-Attention in Neural Sequence Models, https://arxiv.org/abs/1906.06755
[64] RoFormer: Enhanced Transformer with Rotary Position Embedding, https://arxiv.org/abs/2104.09864
[65] Train Short, Test Long: Attention with Linear Biases Enables Input, https://arxiv.org/abs/2108.12409
[66] Extending Context Window of Large Language Models via ... - arXiv, https://arxiv.org/abs/2306.15595
[67] YaRN: Efficient Context Window Extension of Large Language Models, https://arxiv.org/abs/2309.00071
[68] Lost in the Middle: How Language Models Use Long Contexts - arXiv, https://arxiv.org/abs/2307.03172
[69] Efficient Streaming Language Models with Attention Sinks - arXiv, https://arxiv.org/abs/2309.17453
[70] Fast Transformer Decoding: One Write-Head is All You Need - arXiv, https://arxiv.org/abs/1911.02150
[71] DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of ... - arXiv, https://arxiv.org/abs/2405.04434
[72] FlashAttention-2: Faster Attention with Better Parallelism and Work, https://arxiv.org/abs/2307.08691
[73] FlashAttention-3: Fast and Accurate Attention with Asynchrony and, https://arxiv.org/abs/2407.08608
[74] How Much Dense Attention is Necessary? Oracle-Guided Sparse, https://arxiv.org/abs/2606.07703
[75] Scaling to Trillion Parameter Models with Simple and Efficient Sparsity, https://arxiv.org/abs/2101.03961
[76] Scalable Training of Mixture-of-Experts Models with Megatron Core, https://arxiv.org/html/2603.07685v2
[77] Fast Autoregressive Transformers with Linear Attention - arXiv, https://arxiv.org/abs/2006.16236

⁂

Attention Is All You Need (arXiv:1706.03762) — https://arxiv.org/abs/1706.03762
Attention Is All You Need (NeurIPS 2017 Proceedings) — https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf?utm_source=nationaltribune&utm_medium=nationaltribune&utm_campaign=news
Attention Is All You Need (alphaXiv) — https://www.alphaxiv.org/abs/1706.03762v4
Process arXiv:1706.03762 — Attention Is All You Need (Attention Wiki Knowledge Base) — https://huggingface.co/datasets/attention-wiki/knowledge-base/commit/597b4e5675fb2ddd291e75a886eedc568c6fedc2
Attention Is All You Need (arXiv PDF) — https://arxiv.org/pdf/1706.03762
Tensor2Tensor for Neural Machine Translation — https://www.researchgate.net/publication/323904682_Tensor2Tensor_for_Neural_Machine_Translation
Attention Is All You Need — Wikipedia — https://en.wikipedia.org/wiki/Attention_Is_All_You_Need
Contrastive Decoding in Autoregressive and Seq2Seq Language Models — https://arxiv.org/html/2512.03803v1
What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot Generalization? — https://arxiv.org/abs/2204.05832
The Llama 3 Herd of Models — https://arxiv.org/abs/2407.21783
Language Models are Few-Shot Learners — https://arxiv.org/abs/2005.14165
Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth — https://arxiv.org/abs/2103.03404
Transformer Feed-Forward Layers Are Key-Value Memories — https://arxiv.org/abs/2012.14913
Efficient Attention and KV Cache Mechanisms in LLMs (Frontiers of Computer Science) — https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60308-3
DeepSeek KV Cache Optimization Analysis — https://local-ai-zone.github.io/blog/deepseek-kv-cache-optimization-research-paper.html
DeepSeek-V3 Technical Report — https://arxiv.org/abs/2412.19437
GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints — https://arxiv.org/abs/2305.13245
FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness — https://arxiv.org/abs/2205.14135
The Parallelism Tradeoff: Limitations of Log-Precision Transformers — https://arxiv.org/abs/2207.00729
Mamba: Linear-Time Sequence Modeling with Selective State Spaces — https://arxiv.org/abs/2312.00752
Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality — https://arxiv.org/abs/2405.21060
Jamba: A Hybrid Transformer-Mamba Language Model — https://arxiv.org/abs/2403.19887
Sequence to Sequence Learning with Neural Networks — https://arxiv.org/abs/1409.3215
Large Language Models — Gregory Gundersen — https://gregorygundersen.com/blog/2025/10/01/large-language-models/
Neural Machine Translation by Jointly Learning to Align and Translate — https://arxiv.org/abs/1409.0473
Effective Approaches to Attention-based Neural Machine Translation — https://arxiv.org/pdf/1508.04025
A Survey of Deep Learning Techniques for Neural Machine Translation — https://www.researchgate.net/publication/339350384_A_Survey_of_Deep_Learning_Techniques_for_Neural_Machine_Translation
Long Short-Term Memory-Networks for Machine Reading — https://arxiv.org/abs/1601.06733
Attention and Self-Attention for NLP (LMU Munich Seminar) — https://slds-lmu.github.io/seminar_nlp_ss20/attention-and-self-attention-for-nlp.html
Convolutional Sequence to Sequence Learning — https://arxiv.org/abs/1705.03122
Why Drop Recurrence at All — Attention Is All You Need (ScaleDojo) — https://scaledojo.dev/papers/attention-is-all-you-need
Opening the Black Box of LLM Inference: Foundations of Generative AI — https://medium.com/@aridiosilva/opening-the-black-box-of-llm-inference-foundations-of-generative-ai-65f6d3563bd2
Are Sixteen Heads Really Better than One? — https://arxiv.org/abs/1905.10650
Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned — https://arxiv.org/abs/1905.09418
On Layer Normalization in the Transformer Architecture — https://arxiv.org/abs/2002.04745
Root Mean Square Layer Normalization — https://arxiv.org/abs/1910.07467
GLU Variants Improve Transformer — https://arxiv.org/abs/2002.05202
Stabilizing Transformer Training by Preventing Attention Entropy Collapse — https://arxiv.org/abs/2303.06296
Multi-Step Tasks, Softmax Attention, and Phase Transitions in Transformers — https://arxiv.org/html/2310.12956v2
Broken Symmetry in BF16 Attention: Why FlashAttention Gradients Blow Up Late in Training — https://arxiv.org/abs/2609.34272
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding — https://arxiv.org/abs/1810.04805
Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer — https://arxiv.org/abs/1910.10683
A Survey of Large Language Models — https://www.researchgate.net/publication/404686943_A_Survey_of_Large_Language_Models
Neural Machine Translation of Rare Words with Subword Units — https://arxiv.org/abs/1508.07909
SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing — https://arxiv.org/abs/1808.06226
Language Model Tokenizers Introduce Unfairness Between Languages — https://arxiv.org/abs/2305.15425
LLM Tokenization Notes — Pattern Is Everything — https://patterniseverything.com/llm/
Poro 34B Multilingual Language Model and Tokenizer Evaluation — https://arxiv.org/html/2404.01856v3
Scaling Laws for Neural Language Models — https://arxiv.org/abs/2001.08361
Training Compute-Optimal Large Language Models — https://arxiv.org/abs/2203.15556
Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws — https://arxiv.org/abs/2401.00448
Stanford CS336 Spring 2025 Lecture 1 — https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json
Emergent Abilities of Large Language Models — https://arxiv.org/abs/2206.07682
Are Emergent Abilities of Large Language Models a Mirage? — https://arxiv.org/abs/2304.15004
Statistical Induction Heads and Phase Transitions in In-Context Markov Chains — https://arxiv.org/html/2402.11004v1
In-context Learning and Induction Heads — https://arxiv.org/abs/2209.11895
In-Context Learning Survey: Mechanisms and Meta-Optimization — https://arxiv.org/pdf/2311.00237
What learning algorithm is in-context learning? Investigations with linear models — https://arxiv.org/abs/2211.15661
Transformers Learn In-Context by Gradient Descent — https://arxiv.org/pdf/2212.07677
Second-Order Optimization and GD++ in Linear Transformers — https://arxiv.org/html/2402.14180v2
Transformers Recover In-Context Causal Structures — https://arxiv.org/html/2402.14735v2
Understanding In-Context Learning on Boolean Functions and Teaching Sequences — https://arxiv.org/html/2310.03016v1
Theoretical Limitations of Self-Attention in Neural Sequence Models — https://arxiv.org/abs/1906.06755
RoFormer: Enhanced Transformer with Rotary Position Embedding — https://arxiv.org/abs/2104.09864
Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation — https://arxiv.org/abs/2108.12409
Extending Context Window of Large Language Models via Positional Interpolation — https://arxiv.org/abs/2306.15595
YaRN: Efficient Context Window Extension of Large Language Models — https://arxiv.org/abs/2309.00071
Lost in the Middle: How Language Models Use Long Contexts — https://arxiv.org/abs/2307.03172
Efficient Streaming Language Models with Attention Sinks — https://arxiv.org/abs/2309.17453
Fast Transformer Decoding: One Write-Head is All You Need — https://arxiv.org/abs/1911.02150
DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model — https://arxiv.org/abs/2405.04434
FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning — https://arxiv.org/abs/2307.08691
FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision — https://arxiv.org/abs/2407.08608
How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models — https://arxiv.org/abs/2606.07703
Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity — https://arxiv.org/abs/2101.03961
Mixture-of-Experts Parallelism and Performance Optimization — https://arxiv.org/html/2603.07685v2
Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention — https://arxiv.org/abs/2006.16236
