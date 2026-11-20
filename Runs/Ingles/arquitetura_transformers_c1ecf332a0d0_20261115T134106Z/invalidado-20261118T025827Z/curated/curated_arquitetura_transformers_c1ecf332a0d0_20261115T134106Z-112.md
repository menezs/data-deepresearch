[referencia=0c47ea4675bf3dd1 score=0.976]
# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality 

Tri Dao<sup>∗1</sup> and Albert Gu<sup>∗2</sup> 

1 Department of Computer Science, Princeton University 

2 Machine Learning Department, Carnegie Mellon University tri@tridao.me, agu@cs.cmu.edu 

##### **Abstract** 

While Transformers have been the main architecture behind deep learning’s success in language modeling, state-space models (SSMs) such as Mamba have recently been shown to match or outperform Transformers at small to medium scale. We show that these families of models are actually quite closely related, and develop a rich framework of theoretical connections between SSMs and variants of attention, connected through various decompositions of a well-studied class of structured _semiseparable matrices_ . Our state space duality (SSD) framework allows us to design a new architecture ( **Mamba-2** ) whose core layer is an a refinement of Mamba’s selective SSM that is 2-8× faster, while continuing to be competitive with Transformers on language modeling.

---

[referencia=0c47ea4675bf3dd1 score=0.975]
<!-- Start of picture text -->
SSD, Scan, Convolution vs Attention time (A100 80GB PCIe) SSD vs Scan time (A100 80GB PCIe)<br>FlashAttention-2 FlashAttention-2<br>1000 Convolution 7 Scan (Mamba)<br>Scan (PyTorch), state dim 64 SSD (ours)<br>Scan (Mamba), state dim 64 6<br>100 SSD (ours), state dim 64 5<br>10 4<br>3<br>1<br>2<br>0.1 1<br>0<br>512 1k 2k 4k 8k 16k 32k 64k 128k 256k 512k 4 8 16 32 64 128 256<br>Sequence length State dim<br>Time (ms) Time (ms)<br><!-- End of picture text -->

Figure 10: ( **Efficiency Benchmarks** .) ( _Left_ ) Our SSD is 2 − 8× faster than a Mamba fused scan for large state expansion ( _𝑁_ = 64) and faster than FlashAttention-2 for sequence length 2k and above. ( _Right_ ) Sequence length 4K: Increasing state expansion slows down the Mamba optimized scan implementation linearly. SSD can handle much larger state expansion factors without much slowdown. 

29 

We compare on a challenging version of the MQAR setup from (Arora, Eyuboglu, Zhang, et al. 2024), using a harder task, longer sequences, and smaller models. Our baselines include standard multi-head softmax attention as well as the Based architecture which combines convolutions, local attention, and a linear attention variant. 

Results are shown in Figure 8. While Mamba-1 struggles on this task, Mamba-2 performs well across all settings. Surprisingly, it is significantly better than Mamba-1 even when the state sizes are controlled (N = 16). (We are not sure which aspect of the architecture is the predominant factor, which remains a question to explore in future work.) Additionally, this task validates the importance of state size: increasing from N = 16 to N = 64 and N = 256 consistently improves performance on MQAR, as the larger state allows more information (key-value pairs) to be memorized.

---

[referencia=0c47ea4675bf3dd1 score=0.973]
|<br>and attention through the bridge of structured matrices.<br>• We connect SSMs and SMA, showing that they have a large<br>intersection that are duals of each other, possessing both<br>SSM-like linear and attention-like quadratic forms (Sec-<br>tion 5). We also prove that any kernel attention method<br>possessing a fast recurrent form must be an SSM.|
|---|
|Beyond its intrinsic theoretical value, our framework opens up a broad set of directions for understanding and improving<br>sequence models.|
|**Efcient Algorithms.**<br>First and most importantly, our framework exposes new efcient and easily-implementable algo-<br>rithms for computing SSMs (Section6). We introduce a new**SSD algorithm**, based on block decompositions of semisepa-<br>rable matrices, that takes advantage of both the linear SSM recurrence and quadratic dual form, obtaining optimal tradeofs<br>on all main efciency axes (e.g. training and inference compute, memory usage, and ability to leverage matrix multipli-<br>cation units on modern hardware). A dedicated implementation of SSD is 2−8×faster than the optimized selective scan<br>implementation of Mamba, while simultaneously allowing for much larger recurrent state sizes (8×the size of Mamba or<br>even higher, with minimal slowdown). SSD is highly competitive with optimized implementations of softmax attention<br>(FlashAttention-2 (Dao2024)), crossing over at sequence length 2K and 6×faster at sequence length 16K.|
|**Architecture Design.**<br>One major obstacle to adopting new architectures such as SSMs is the ecosystem tailored to<br>Transformers, such as hardware-efcient optimization and parallelism techniques for large-scale training. Our framework<br>allows using established conventions and techniques for attention to build a vocabulary of architecture design choices for<br>SSMs, and further improve them (Section7). For example, we introduce the analog of heads from multi-head attention<br>(MHA) to SSMs. We show that the Mamba architecture is a**multi-input SSM (MIS)**that turns out to be analogous to<br>**multi-value attention (MVA)**, and compare other variants of Mamba with diferent head structures.|

---

[referencia=0c47ea4675bf3dd1 score=0.966]
### **9.3 Speed Benchmarks** 

We benchmark the speed of the SSD algorithm against Mamba’s scan implementation and FlashAttention-2 (Figure 10). SSD, thanks to its reformulation to use matrix multiplication as a subroutine, can exploit specialized matrix multiplication (matmul) units on GPUs, also known as tensor cores. As a result, it is 2-8× faster than Mamba’s fused associative scan, which does not leverage matmul units. Due to its linear scaling in sequence length, SSD is faster than FlashAttention-2 starting at sequence length 2 _𝐾_ . 

However, we note that the Mamba-2 model as a whole might not be as efficient to train as Transformer at short sequence length (e.g. at 2 _𝐾_ ), since a Transformer with _𝐿_ layers would have<sup>_<u>𝐿</u>_</sup> 2<sup>MLP layers and</sup><sup>_<u>𝐿</u>_</sup> 2<sup>attention layers, while a Mamba-2</sup> model would have _𝐿_ SSD layers for the same number of parameters. Generally the MLP layers are very hardware efficient since they consist of simple matrix multiplication and pointwise linearity. As shown in Section 9.2.3, one can also combine _<u>𝐿</u>_ 2<sup>SSD layers and</sup><sup>_<u>𝐿</u>_</sup> 2<sup>MLP layers to speed up training at short sequence length.</sup> 

> 6In small-scale experiments, we find that as long as the attention layers are spaced out, not at the very beginning or at the very end, the model quality does not depend very much on the exact location of the attention layers. 

31 

Table 4: ( **Ablations: Mamba-2 block** .) We ablate the major differences between the Mamba-2 and Mamba-1 neural network blocks (Figure 6, Section 7.1). Note that these components are independent of the inner sequence mixing layer; in these ablations, we use SSD for the inner SSM layer (differing from the S6 layer of Mamba-1).

---

[referencia=0c47ea4675bf3dd1 score=0.951]
> ∗Alphabetical by last name. 

> 1Technically speaking, these connections only relate to certain flavors of attention; the title of this paper is an homage to Katharopoulos et al. (2020) which first showed that “Transformers are RNNs”. 

1 

**State Space Duality.** Our framework connecting structured SSMs and variants of attention, which we call **structured state space duality** (SSD), is made through the abstractions of **structured matrices** : matrices with subquadratic parameters and multiplication complexity. We develop two broad frameworks for representing sequence models, one as matrix transformations and one as tensor contractions, which each reveal different perspectives of the duality. Our technical contributions include: 



<!-- Start of picture text -->
Efficient<br><!-- End of picture text -->

**Algorithms tured state space duality** (SSD), is made through the abstractions of **structured matrices** : matrices with subquadratic parameters and multiplication complexity. We deSec. 6 velop two broad frameworks for representing sequence models, one as matrix transformations and one as tensor contrac- **Structured** tions, which each reveal different perspectives of the duality. **Matrices** Our technical contributions include: **Semiseparable Structured Masked** • We show an equivalence between state space models and a **Matrices** Sec. 3 Sec. 4 **Attention (SMA)** well-studied family of structured matrices called **semiseparable matrices** (Section 3). This connection is at the heart our framework, revealing new properties and algoSec. 5 **State Space** rithms for SSMs. A central message of this paper is that **Models (SSM) Attention** _different methods of computing state space models can be re-_ **State Space** _framed as various matrix multiplication algorithms on structured matrices_ . **Duality (SSD)** • We significantly improve the theory of linear attenSec. 7 

- We significantly improve the theory of linear attention (Katharopoulos et al. 2020). We first provide an incisive proof of its recurrent form through the language of tensor contractions, and then generalize it to a new family of **structured masked attention (SMA)** (Section 4). 



<!-- Start of picture text -->
Mamba-2<br><!-- End of picture text -->

---

[referencia=0c47ea4675bf3dd1 score=0.947]
### **10.3 (Linear) Attention** 

Compared to standard (causal) attention, SSD has only two main differences. 

First, SSD does not use the softmax activation of standard attention (Bahdanau, Cho, and Bengio 2015; Vaswani et al. 2017), which is what gives attention its quadratic complexity. When the softmax is dropped, the sequence can be computed with linear scaling through the linear attention framework (Katharopoulos et al. 2020). 

Second, SSD multiplies the logits matrix by an input-dependent 1-semiseparable mask. Thus this mask can be viewed as replacing the softmax in standard attention. 

This semiseparable mask can also be viewed as providing positional information. The elements _𝑎𝑡_ act as “gates” in the RNN sense, or a “selection” mechanism (see discussion in Mamba paper), and their cumulative products _𝑎 𝑗_ : _𝑖_ control how much interaction is allowed between positions _𝑖_ and _𝑗_ . Positional embeddings (e.g. sinusoidal (Vaswani et al. 2017), AliBi (Press, N. Smith, and Lewis 2022), and RoPE (Su et al. 2021)) are an important component of Transformers that are often viewed as heuristics, and the 1-SS mask of SSD can be seen as a more principled form of relative positional embeddings. We note that this view was also posited concurrently by GateLoop (Katsch 2023). 

The second viewpoint of state space duality is a special case of our more general structured masked attention (SMA) framework, where the duality is revealed as different contraction orderings on a simple 4-way tensor contraction. SMA is a strong generalization of linear attention that is much more general than SSD as well; other forms of structured masks may lead to more variants of efficient attention with different properties than SSD. 

Beside leading to new models, these connections to attention can lead to other directions for understanding SSMs. For example, we are curious whether the phenomenon of attention sinks (Darcet et al. 2024; Xiao et al. 2024) exist for Mamba models, and more broadly whether interpretability techniques can be transferred to SSMs (Ali, Zimerman, and Wolf 2024).

---

[referencia=0c47ea4675bf3dd1 score=0.935]
17 



<!-- Start of picture text -->
Structured State Space Model (SSM) Structured<br>Structured State Space Model Structured Masked Attention State Space<br>𝐶 (contraction matrix) 𝑄 (queries) S4 Diagonal State Space Model Duality (SSD)<br>𝑋𝐵 (expansion matrix)(input sequence) 𝑉𝐾 (values)(keys) DSS Scalar-Identity SSM<br>𝐴𝑗 : 𝑖 (state matrix) 𝐿𝑗𝑖 (mask) S4D RetNet GateLoop<br>N (state expansion dim.) N (kernel feature dim.) S5 TransNormer<br>S6 Linear Attention<br>𝐻 (hidden states (8b))<br>=  𝐿 ·  𝑋𝐵 (linear mode) SMA linear dual (15) 1-Semiseparable SMA<br>Efficient Autoregressive Attention<br>𝐺 (Gram matrix (13a)) Semiseparable SMA<br>SSM quadratic dual (16) =  𝑄 ·  𝐾 ⊤ (quadratic mode)<br>Structured Masked Attention (SMA)<br><!-- End of picture text -->

Figure 4: ( **Structured State Space Duality** .) State space duality describes the close relationship between state space models and masked attention. ( _Left_ ) General SSMs and SMA both possess linear and quadratic forms, with direct analogs in notation. ( _Right_ ) SSMs and SMA intersect at a large class of _state space dual models_ (SSD) which capture many sequence models as special cases. 

Note that all of these bounds are tight, because a state space model with state expansion N operating on a head size of N has total state size N<sup>2</sup> (yielding the lower bounds for training and inference FLOPs of _𝑂_ (TN<sup>2</sup> ) and _𝑂_ (N<sup>2</sup> ) respectively). Furthermore the input _𝑋_ itself has TN elements, yielding the memory lower bound.

---

[referencia=0c47ea4675bf3dd1 score=0.897]
### **5.3 Structured State-Space Duality (SSD)** 

To summarize our results: 

- Structured state-space models (Section 3) are a model usually defined through a linear-time recurrence. However, by expanding the matrix formulation characterizing its linear sequence-to-sequence transformation, one can derive a quadratic form. 

- Attention variants (Section 4) are a model defined through quadratic-time pairwise interactions. However, by viewing it as a four-way tensor contraction and reducing in a different order, one can derive a linear form. 

- A natural special case of each one – more precisely, state space models with scalar-identity structure on the _𝐴_ matrices, and structured masked attention with 1-semiseparable structure on its _𝐿_ mask – are duals of each other with the exact same linear and quadratic forms. 

Figure 4 summarizes the duality between these two representations. 

An extended related work and discussion (Section 10) describes the relationship between SSD and general SSMs / attention in more detail.

---

[referencia=0c47ea4675bf3dd1 score=0.863]
## **1 Introduction** 

Transformers, in particular decoder-only models (e.g. GPT (Brown et al. 2020), Llama (Touvron, Lavril, et al. 2023)) which process input sequences in a causal fashion, are one of the main drivers of modern deep learning’s success. Numerous approaches attempt to approximate the core attention layer to address its efficiency issues (Tay et al. 2022), such as scaling quadratically in sequence length during training and requiring a cache of size linear in sequence length during autoregressive generation. In parallel, a class of alternative sequence models, structured state-space models (SSMs), have emerged with linear scaling in sequence length during training and constant state size during generation. They show strong performance on long-range tasks (e.g. S4 (Gu, Goel, and Ré 2022)) and recently matched or beat Transformers on language modeling (e.g. Mamba (Gu and Dao 2023)) at small to moderate scale. However, the development of SSMs have appeared disjoint from the community’s collective effort to improve Transformers, such as understanding them theoretically as well as optimizing them on modern hardware. As a result, it is more difficult to understand and experiment with SSMs compared to Transformers, and it remains challenging to train SSMs as efficiently as Transformers from both an algorithmic and systems perspective. 

Our main goal is to develop a rich body of theoretical connections between structured SSMs and variants of attention. This will allow us to transfer algorithmic and systems optimizations originally developed for Transformers to SSMs, towards the goal of building foundation models that perform better than Transformers while scaling more efficiently in sequence length. A milestone contribution in this direction was the **Linear Attention (LA)** framework (Katharopoulos et al. 2020), which derived a connection between autoregressive attention and linear RNNs by showing the equivalence between “dual forms” of quadratic kernelized attention and a particular linear recurrence. This duality allows new capabilities such as the ability to have both efficient parallelizable training and efficient autoregressive inference. In the same spirit, this paper provides multiple viewpoints connecting linear-complexity SSMs with quadratic-complexity forms to combine the strengths of SSMs and attention.<sup>1</sup> 

> ∗Alphabetical by last name.

---

[referencia=0c47ea4675bf3dd1 score=0.854]
#### **9.2.3 Hybrid Models: Combining SSD Layer with MLP and Attention** 

Recent and concurrent work (Dao, D. Y. Fu, et al. 2023; De et al. 2024; Glorioso et al. 2024; Lieber et al. 2024) suggests that a hybrid architecture with both SSM layers and attention layers could improve the model quality over that of a Transformer, or a pure SSM (e.g., Mamba) model, especially for in-context learning. We explore the different ways that SSD layers can be combined with attention and MLP to understand the benefits of each. Empirically we find that having around 10% of the total number of layers being attention performs best. Combining SSD layers, attention layers, and MLP also works better than either pure Transformer++ or Mamba-2. 

**SSD and Attention** We find that SSD and attention layers are complementary: by themselves (e.g. in the Mamba-2 architecture vs. Transformer++) their performance (measured by perplexity) is nearly the same, but a mixture of SSD and attention layers outperforms the pure Mamba-2 or Transformer++ architecture. We show some results (Table 2) for the 350M model (48 layers) trained to 7B tokens on the Pile with the GPT-2 tokenizer (same number of parameters, same hyperparameters, same training and validation set). Adding in just a few attention layers already yields notable improvement and strikes the best balance between quality and efficiency. We hypothesize that the SSM layers function well as a general sequence-to-sequence mapping, and attention layers act as a retrieval mechanism to quickly refer to previous tokens in the sequence instead of forcing the model to compress all the context to its memory (SSM states). 

30 

Table 2: ( **Combining SSD and Attention Blocks** .) Perplexity of a 350M model with 48 layers, with different number of attention layers. Having around a 10% ratio of attention layers performs best.

---

[referencia=0c47ea4675bf3dd1 score=0.846]
Table 2: ( **Combining SSD and Attention Blocks** .) Perplexity of a 350M model with 48 layers, with different number of attention layers. Having around a 10% ratio of attention layers performs best. 

|Num. Attn Blocks|0 (Mamba-2)|1|2|3|4|5|6|7|9|11|15|24|Transformer++|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Perplexity↓|8.60|8.38|8.32|8.29|8.29|8.28|**8.26**|8.27|8.28|8.30|8.34|8.50|8.68|



**Hybrid Models with SSD, MLP, and Attention** We compare different ways that SSD can be combined with the (gated) MLP and attention layers, and evaluate at the 2.7B scale (64 layers), trained to 300B tokens on the Pile (same number of parameters, same hyperparameters, same training and validation set, same data order): 

1. Transformer++: 32 attention layers and 32 gated MLP, interleaving. 

2. Mamba-2: 64 SSD layers. 

3. Mamba-2-MLP: 32 SSD and 32 gated MLP layers, interleaving. 

4. Mamba-2-Attention: 58 SSD layers and 6 attention layers (at indices 9, 18, 27, 36, 45, 56)<sup>6</sup> . 

5. Mamba-2-MLP-Attention: 28 SSD layers and 4 attention layers, interleaving with 32 gated MLP layers. 

We report the validation perplexity on the Pile, as well as zero-shot evaluation, in Table 3. In general, the quality of Transformer++ and Mamba-2 models are around the same. We see that adding just 6 attention layers noticeably improves over the pure Mamba-2 model (and over Transformer++). Adding MLP layers reduces model quality, but can (i) speed up training and inference due to the simplicity and hardware-efficiency of the MLP layer (ii) be easier to up-cycle to MoE models by replacing MLP layers with mixture-of-experts.

---

[referencia=0c47ea4675bf3dd1 score=0.843]
- **Dual (Quadratic) Form.** The dual form of SSD is a quadratic computation closely related to attention, defined as ( _𝐿_ ◦ _𝑄𝐾_<sup>⊤</sup> ) · _𝑉 𝐿𝑖𝑗_ = _𝑎𝑖_ × · · · × _𝑎 𝑗_ +1 _𝑖_ ≥ _𝑗_ �0 _𝑖 < 𝑗_ 

- where _𝑎𝑖_ are input-dependent scalars bounded in [0 _,_ 1]. 

- Compared to standard softmax attention, there are two main differences 

   - The softmax is dropped. 

   - The attention matrix is multiplied elementwise-wise by an additional mask matrix _𝐿_ . 

- Both of these changes can be viewed as addressing problems in vanilla attention. For example, the softmax has been recently observed to cause problems in attention scores, such as the “attention sink” phenomenon (Darcet et al. 2024; Xiao et al. 2024). More importantly, the mask matrix _𝐿_ can be viewed as replacing the heuristic positional embeddings of Transformers with a different _data-dependent positional mask_ that controls how much information is transfered across time. 

- More broadly, this form is an instance of our **structured masked attention** generalization of linear attention, defined in Section 4. 

- **Matrix Form and SSD Algorithm.** The various forms of SSD are connected through a unified matrix representation, by showing that SSMs have a matrix transformation form _𝑌_ = _𝑀𝑋_ for a matrix _𝑀𝜃_ ∈ R<sup>(T</sup><sup>_,_T)</sup> that depends on _𝜃_ = ( _𝐴, 𝐵,𝐶_ ). In particular, the dual form of SSD is equivalent to naive (quadratic-time) multiplication by the matrix _𝑀_ , and the recurrent form is a particular efficient (linear-time) algorithm that leverages the structure in _𝑀_ .

---

[referencia=0c47ea4675bf3dd1 score=0.822]
### **10.2 Structured Matrices** 

The first viewpoint of the state space duality adopts the viewpoint of these models as **matrix sequence transformations** or “matrix mixers”: sequence transformations (Definition 2.1) that can be represented as matrix multiplication (by a T × T matrix) along the sequence dimension T. 

Several such matrix mixers have been proposed before, where the primary axis of variation is the representation of the matrix. These include MLP-Mixer (Tolstikhin et al. 2021) (unstructured matrix), FNet (Lee-Thorp et al. 2021) (Fourier Transform matrix), M2 (Dao, B. Chen, et al. 2022; Dao, Gu, et al. 2019; Dao, Sohoni, et al. 2020; D. Fu et al. 2024) (butterfly/monarch matrix), Toeplitz matrices (Poli et al. 2023; Qin, Han, Weixuan Sun, B. He, et al. 2023), and even more exotic structures (De Sa et al. 2018; Thomas et al. 2018). 

An important characterization is that efficient (sub-quadratic) matrix sequence transformations are exactly those which have _structured matrix mixers_ . A core result of the SSD framework is viewing SSMs as matrix mixers with a particular structure – semiseparable matrices (Section 3). The linear vs. quadratic duality then takes the form of structured matrix multiplication vs. naive matrix multiplication. 

34 

The structure matrix representation led to our efficient SSD algorithm through block decompositions of particular semiseparable matrices (Section 6). We note that semiseparable matrices are well-studied in the scientific computing literature, and incorporating those ideas may be a promising avenue for more improvements to state space models. We also suggest that focusing on the matrix mixer viewpoint can lead to more fruitful directions for sequence models, such as designing principled non-causal variants of Mamba, or finding ways to characterize and bridge the gap between softmax attention and sub-quadratic models through analyzing their matrix transformation structure.

---

[referencia=0c47ea4675bf3dd1 score=0.818]
### **2.4 Overview: Structured State Space Duality** 

While this paper develops a much richer framework of connections between SSMs, attention, and structured matrices, we provide a brief summary of the main method, which is actually quite self-contained and simple algorithmically. 

**Recurrent (Linear) Form.** The state space dual (SSD) layer can be defined as a special case of the selective SSM (2). The standard computation of an SSM as a recurrence (or parallel scan) can be applied, which has linear complexity in sequence length. Compared to the version used in Mamba, SSD has two minor differences: 

- The structure on _𝐴_ is further simplified from diagonal to _scalar times identity_ structure. Each _𝐴𝑡_ can also be identified with just a scalar in this case. 

- We use a larger head dimension P, compared to P = 1 used in Mamba. Typically P = {64 _,_ 128} is chosen which is similar to conventions for modern Transformers. 

Compared to the original selective SSM, these changes can be viewed as slightly decreasing the expressive power in return for significant training efficiency improvements. In particular, our new algorithms will allow the use of matrix multiplication units on modern accelerators. 

5

---

[referencia=0c47ea4675bf3dd1 score=0.798]
**Multi-contract SSM (MCS) / Multi-query Attention (MQA) Pattern.** Multi-query attention (Shazeer 2019) is a clever optimization for attention that can dramatically improve the speed of autoregressive inference, which relies on caching the _𝐾_ and _𝑉_ tensors. This technique simply avoids giving _𝐾_ and _𝑉_ the extra head dimension, or in other words broadcasts a single head of ( _𝐾,𝑉_ ) across all the heads of _𝑄_ . 

Using the state space duality, we can define an equivalent SSM version of MQA as equation (18). Here, _𝑋_ and _𝐵_ (the SSM analogs of attention’s _𝑉_ and _𝐾_ ) are shared across the H heads. We also call this the _multi-contract SSM (MCS)_ head pattern, because the _𝐶_ parameter which controls the SSM state contraction has independent copies per head. 

We can similarly define a multi-key attention (MKA) or _multi-expand SSM (MES)_ head pattern, where _𝐵_ (which controls the SSM expansion) is independent per head while _𝐶_ and _𝑋_ are shared across heads. 

**Multi-input SSM (MIS) / Multi-value Attention (MVA) Pattern.** While MQA makes sense for attention because of its KV cache, it is not the natural choice for SSMs. In Mamba, instead, _𝑋_ is viewed as the main input to the SSM, and therefore _𝐵_ and _𝐶_ are parameters that are shared across the input channels. We define a new multi-value attention (MVA) of _multi-input SSM (MIS)_ pattern in equation (20), which can again be applied to any sequence transformation such as SSD. 

Armed with this vocabulary, we can characterize the original Mamba architecture more precisely. 

**Proposition 7.2.** _The selective SSM (S6) layer of the Mamba architecture (Gu and Dao 2023) can be viewed as having_ 

24

---

[referencia=0c47ea4675bf3dd1 score=0.790]
|We also use these ideas to make slight modifcations to the Mamba block, which allows tensor parallelism to be imple-<br>mented (e.g. in the style of Megatron (Shoeybi et al.2019)). The main ideas include introducing grouped-value attention<br>(GVA) head structure, and moving all data-dependent projections to occur in parallel at the beginning of the block.|
|The combination of the modifed parallel Mamba block, together with using SSD as the inner SSM layer, results in the<br>**Mamba-2**architecture. We investigate Chinchilla scaling laws for Mamba-2 in the same setting as Mamba, fnding that<br>it Pareto dominates Mamba and Transformer++ in both perplexity and wall-clock time. We additionally train a family of|



2 

Mamba-2 models at varying sizes on the Pile, showing that it matches or outperforms Mamba and open source Transformers on standard downstream evaluations. For example, Mamba-2 with 2.7B parameters trained on 300B tokens on the Pile outperforms Mamba-2.8B, Pythia-2.8B and even Pythia-6.9B trained on the same dataset. 

**Systems Optimizations.** The SSD framework connects SSMs and Transformers, allowing us to leverage a rich body of work on systems optimizations developed for Transformers (Section 8). 

- For example, Tensor Parallelism (TP) is an important model parallelism technique to train large Transformer models by splitting each layer across GPUs on the same node. We design Mamba-2 to be TP-friendly, reducing the number of synchronization point per block by half. 

- For very long sequences whose activations do not fit on one device, sequence parallelism has been developed for the attention blocks. We describe how to train SSMs in general and Mamba-2 in particular with sequence parallelism, by passing the recurrent states between devices. 

- For finetuning with examples of different lengths, for best efficiency, Transformer requires sophisticated techniques to remove padding tokens and perform attention on variable length sequences. We show how Mamba-2 can be trained with variable sequence lengths efficiently, requiring no padding tokens.

---

[referencia=0c47ea4675bf3dd1 score=0.778]
|Kernel activation_𝜑_|Perplexity|Kernel activation_𝜑_|Perplexity|
|---|---|---|---|
|none|11_._58|Swish|11_._67|
|Swish|11_._66|Swish + Taylor (Based)|12_._19|
|Exp|11_._62|LayerNorm|11_._50|
|ReLU|11_._73|LayerNorm + Square (ReBased)|11_._84|
|ReLU + normalization|11_._64|Swish|8_._58|
|cosFormer|11_._97|Swish + Taylor (Based)|8_._71|
|Random Feature Attention|11_._57|LayerNorm|8_._61|
|Positive Random Features (Performer)|12_._21|LayerNorm + Square (ReBased)|8_._63|



We note that this technique has been independently proposed as the “QK-Norm” for softmax attention (Team 2024) and an “internal normalization” for Mamba (Lieber et al. 2024). 

Overall, Table 6 and Table 7 found that the kernel approximation methods we tried did not seem to improve over simple pointwise non-linear activation functions for _𝜓_ . Thus our default settings for Mamba-2 used _𝜓_ ( _𝑥_ ) = Swish( _𝑥_ ) to follow Mamba-1, but we suggest that removing this activation entirely may be a simpler choice that we did not extensively test. 

We emphasize however that SSD and vanilla linear attention differ in the inclusion of the 1-semiseparable mask _𝐿_ , while the various linear attention methods in the literature were derived to approximate softmax attention without this term; thus, our negative results may be not unexpected.

---

[referencia=0c47ea4675bf3dd1 score=0.772]
### **7.3 Other SSD Extensions from Linear Attention** 

We describe here an example of architectural modifications to SSD motivated by linear attention. We ablate these in Section 9.4.3 as a form of negative result, finding that they do not significantly improve performance enough to adopt them as default settings. Nonetheless, these illustrate how the vast literature on attention can be incorporated to define variants of SSD. We treat the choice of kernel feature map as a hyperparameter in the Mamba-2 architecture, and expect other simple modifications inspired by attention to be possible as well. 

**Kernel Attention Approximations to Softmax Attention.** Many variants of linear attention or kernel attention are motivated by viewing the attention scores softmax( _𝑄𝐾_<sup>⊤</sup> ) as composed of 

1. An exponential kernel _𝑍_ = exp( _𝑄𝐾_<sup>⊤</sup> ), which can be approximated by _𝑍_ = _𝜓_ ( _𝑄_ ) _𝜓_ ( _𝐾_ )<sup>⊤</sup> for some kernel feature map. 

2. Normalizing the kernel so that rows sum to 1 via _𝑀_ = _𝐺_ / _𝐺_ 11<sup>⊤</sup> , where the division happens elementwise and 1 is the all 1’s vector. 

**Exponential Kernel Feature Maps.** In Mamba-2, we incorporate a flexible kernel feature map, and apply it to the _𝐵_ and _𝐶_ branches (corresponding to the _𝐾_ and _𝑉_ branches in attention). The feature map can also be optionally applied to the _𝑋_ ( _𝑉_ ) branch, for simplicity and symmetry. This is represented in Figure 6 by an arbitrary nonlinearity. By default, we simply choose _𝜓_ to be an elementwise Swish / SiLU function (Hendrycks and Gimpel 2016; Ramachandran, Zoph, and Le 2017). We explore other options in the ablations in Section 9.4.3, including feature maps used by Linear Attention, Performer, Random Feature Attention, and cosFormer (Section 4.1.3).

---

[referencia=0c47ea4675bf3dd1 score=0.770]
### **10.1 State Space Models** 

Structured state space models can be characterized along the axes 

33 

- (i) whether it is time-invariant or time-varying. 

- (ii) the dimensionality of the system. 

- (iii) the structure on the recurrent transitions _𝐴_ . 

SSD can be described as a selective SSM with SISO dimensions and scalar-identity structure. 

**Time Variance (Selectivity).** The original structured SSMs (S4) were linear time-invariant (LTI) systems (Gu 2023; Gu, Goel, and Ré 2022) motivated by continuous-time online memorization (Gu, Dao, et al. 2020; Gu, Johnson, Goel, et al. 2021; Gu, Johnson, Timalsina, et al. 2023). Many variants of structured SSMs have been proposed (Dao, D. Y. Fu, et al. 2023; Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Ma et al. 2023; J. T. Smith, Warrington, and Linderman 2023), including several that drop the recurrence and focus on the convolutional representation of LTI SSMs (D. Y. Fu et al. 2023; Y. Li et al. 2023; Poli et al. 2023; Qin, Han, Weixuan Sun, B. He, et al. 2023).

---

[referencia=0c47ea4675bf3dd1 score=0.764]
## **5 State Space Duality** 

In Sections 3 and 4, we defined structured state space models and structured attention, discussed their properties, and showed that they both have a quadratic algorithm and a linear algorithm. This section connects them together. Our main result is showing that a particular case of structured state space models coincides with a particular case of structured attention, and that the linear-time SSM algorithm and quadratic-time kernel attention algorithm are dual forms of each other. 

- Section 5.1 specializes state space models to scalar structure, where the naive quadratic computation can be seen as an instance of kernel attention. 

- Section 5.2 specializes structured masked attention to semiseparable SMA, which characterizes masked attention with efficient autoregression. 

- Section 5.3 summarizes the connection between structured masked attention and structured state space models, termed structured state space duality.