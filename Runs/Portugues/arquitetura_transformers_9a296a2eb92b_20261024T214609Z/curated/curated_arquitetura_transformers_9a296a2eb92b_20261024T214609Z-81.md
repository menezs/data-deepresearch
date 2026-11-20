[referencia=9cb658eb63c3853b score=0.602]
##### **Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

---

[referencia=9cb658eb63c3853b score=0.391]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=9cb658eb63c3853b score=0.343]
asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

---

[referencia=9cb658eb63c3853b score=0.120]
## **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=9cb658eb63c3853b score=0.092]
|**FlashAttention**|**0.04**|0.06|0.21|0.82|2.85|10.41|41.74|167.19|670.76|2682.35|
|**Block-Sparse FlashAttention**|0.06|**0.06**|**0.06**|**0.12**|**0.44**|**0.86**|**1.70**|**3.29**|**6.55**|**13.34**|



We report timing results on the forward pass, backward pass, and combined forward + backward pass. We measure each method with and without dropout, masking, or both—except for Block Sparse, Longformer, and BigBird. These methods did not successfully run the backward pass with masking due to a bug in external libraries, so we measured them without masking to be generous. We use FP16 for all measurements, except for Local Attention, whose implementation only supports FP32. 

For each baseline, we increase sequence length until it runs out of memory on the GPU, except for the following exceptions: The Megatron implementation does not support sequence lengths longer than 2048. Block-Sparse (OpenAI) does not support sequence lengths longer than 4096. Longformer and BigBird do not support sequence lengths longer than 8092. 

We measure memory usage on the combined forward + backward pass, without dropout or masking. 

**Results** Table 8 summarizes all the experimental configurations and contains pointers to the results tables. 

31 

Table 10: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.082]
Table 21: Memory usage (MB) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u> 

|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|36|104|336|1184|4416|17024|-|-|-|-|
|**Megatron**|36|104|336|1184|4416|-|-|-|-|-|
|**Reformer**|377|754|1508|3016|6033|12067|24134|-|-|-|
|**Local Attention**|53|110|232|592|1696|3392|6784|13568|27136|-|
|**Linformer**|25|52|114|287|832|1652|3292|6572|13132|26252|
|**Smyrf**|217|434|868|1737|3474|6947|13894|27788|-|-|
|**LSformer**|72|152|333|796|2540|5068|10125|20240|-|-|
|**Block Sparse**|33|82|228|408|910|2401|-|-|-|-|
|**Longformer**|30|61|124|277|681|1370|2748|-|-|-|
|**BigBird**|33|66|131|294|708|1431|2872|-|-|-|
|**FlashAttention**|**22**|**44**|**104**|**209**|**418**|**836**|**1672**|**3344**|**6688**|**13376**|
|**Block-Sparse FlashAttention**|22|44|104|209|418|836|1672|3344|6690|13384|



34

---

[referencia=9cb658eb63c3853b score=0.073]
### **E.6 Full Benchmarking Results** 

We report the full benchmarking results and experimental details on A100. 

**Baselines** We compare against reference implementations for exact attention from PyTorch/HuggingFace and Megatron, approximate attention, and sparse attention. For approximate attention, we compare against reference implementations of Reformer [51], Local Attention [68], Linformer Attention [84], Smyrf [19], and LongShortFormer (LSFormer) [94]. For sparse attention, we compare against reference implementations of Block-Sparse Attention form OpenAI [11], Longformer[3], and BigBird Attention [92]. For the approximate and sparse attention, we use a compression ratio of 1/8, or a compressed sequence length of 256, whichever is smaller. 

**Setup** We measure runtime and memory usage of the attention computation with 8 heads of dimension 64, and batch size 16 on a machine with one A100 GPU with 40 GB of GPU HBM. We vary sequence length in our experiments. We compute attention on random vectors for **Q** , **K** , and **V** (we do not measure the projection from the hidden layer). For dropout, we use dropout 0.1; for masking, we use a padding mask with uniformly-random mask lengths between the total sequence length and the total sequence length minus 20. To measure runtime, we take the average of 100 measurements of the attention call. We only measure memory footprint once, since it does not vary between runs. 

30 

Table 8: Pointers to results tables. 

|**Dropout**|**Masking**|**Pass**|**Table**|
|---|---|---|---|
|Yes|Yes|Forward|Table 9|
|Yes|Yes|Backward|Table 10|
|Yes|Yes|Combined|Table 11|
|No|Yes|Forward|Table 12|
|No|Yes|Backward|Table 13|
|No|Yes|Combined|Table 14|
|Yes|No|Forward|Table 15|
|Yes|No|Backward|Table 16|
|Yes|No|Combined|Table 17|
|No|No|Forward|Table 18|
|No|No|Backward|Table 19|
|No|No|Combined<br>|Table 20|
|No|No|Memory Usage (Combined)|Table 21|

---

[referencia=9cb658eb63c3853b score=0.070]
|**Block-Sparse FlashAttention**|0.74|0.77|0.82|**0.88**|**1.71**|**3.21**|**6.56**|**12.60**|**24.93**|**50.39**|



Table 21: Memory usage (MB) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.066]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=9cb658eb63c3853b score=0.063]
We also analyze the IO complexity of block-sparse FlashAttention. 

**Proposition 4.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> _𝑠_ ) _HBM accesses where 𝑠 is the fraction of nonzero blocks in the block-sparsity mask._ 

We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths _𝑁_ , _𝑠_ is often set to _𝑁_<sup>−1/2</sup> [11] or _𝑁_<sup>−1</sup> log _𝑁_ [3, 17, 92], resulting in Θ( _𝑁_ √ _𝑁_ ) or Θ( _𝑁_ log _𝑁_ ) IO complexity. For downstream experiments, we use the fixed butterfly sparsity pattern [17], which has been shown to be able to approximate arbitrary sparsity [16]. 

In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup, while performing on par with standard attention (Section 4).

---

[referencia=9cb658eb63c3853b score=0.059]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=9cb658eb63c3853b score=0.056]
We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations. 

- **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

- **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

---

[referencia=9cb658eb63c3853b score=0.055]
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|
|**Block-Sparse FlashAttention**|0.11|**0.12**|**0.16**|**0.38**|**1.20**|**2.34**|**4.69**|**9.10**|**18.74**|**37.04**|



Table 20: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.054]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.050]
|Model implementations|OpenWebText (ppl)|Training time (speedup)|
|---|---|---|
|GPT-2 small - Huggingface [87]|18.2|9.5 days (1.0×)|
|GPT-2 small - Megatron-LM [77]|18.2|4.7 days (2.0×)|
|GPT-2 small - FlashAttention|18.2|**2.7 days (3.5**×**)**|
|GPT-2 medium - Huggingface [87]|14.2|21.0 days (1.0×)|
|GPT-2 medium - Megatron-LM [77]|14.3|11.5 days (1.8×)|
|GPT-2 medium - FlashAttention|14.3|**6.9 days (3.0**×**)**|



**Long-range Arena.** We compare vanilla Transformer (with either standard implementation or FlashAttention) on the long-range arena (LRA [80]) benchmark. We measure accuracy, throughput, and training time of all models. Each task has a different sequence length varying between 1024 and 4096. We follow the implementation and experimental setting in Tay et al. [80]and Xiong et al. [90].<sup>3</sup> Table 3 shows that FlashAttention achieves up 2.4× speed-up compared to standard attention. Block-sparse FlashAttention is faster than all of the approximate attention methods that we have tested. 

Table 3: The performance of standard attention, FlashAttention, block-sparse FlashAttention, and approximate attention baselines on the Long-Range-Arena benchmarks.

---

[referencia=9cb658eb63c3853b score=0.049]
### **2.2 Standard Attention Implementation** 

Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> where _𝑁_ is the sequence length and _𝑑_ is the head dimension, we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



where softmax is applied row-wise. 

Standard attention implementations materialize the matrices **S** and **P** to HBM, which takes _𝑂_ ( _𝑁_<sup>2</sup> ) memory. Often _𝑁_ ≫ _𝑑_ (e.g., for GPT2, _𝑁_ = 1024 and _𝑑_ = 64). We describe the standard attention implementation in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time. 

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to **S** or dropout applied to **P** . As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax [77]. 

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length _𝑁_ . We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention). 

**Algorithm 0** Standard Attention Implementation 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM.

---

[referencia=9cb658eb63c3853b score=0.046]
In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses: 



However, the input to attention (matrices **Q** _,_ **K** _,_ **V** ) and the output **O** have size _𝑁𝑑_ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least Ω( _𝑁𝑑_ ) HBM accesses. This is a contradiction. □ 

_Proof of Theorem 5._ The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). Here we provide a sketch of the proof. 

We first analyze the IO complexity of standard attention backward pass. The inputs **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the outputs **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> are written to HBM. 

At each step of the standard attention backward pass, one needs to load inputs of size _𝑁𝑑_ or _𝑁_<sup>2</sup> from HBM, and needs to write the outputs of size _𝑁_<sup>2</sup> or _𝑁𝑑_ to HBM. This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

We now analyze the IO complexity of FlashAttention backward pass.

---

[referencia=9cb658eb63c3853b score=0.034]
### **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=9cb658eb63c3853b score=0.033]
|**Block-Sparse FlashAttention**|0.05|**0.04**|**0.05**|**0.11**|**0.35**|**0.68**|**1.33**|**2.54**|**5.34**|**10.73**|



Table 13: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.032]
### **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.