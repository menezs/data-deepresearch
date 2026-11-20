[referencia=5727fed78bddc701 score=0.580]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.445]
Table 6: We report the first Transformer model that can achieve non-random performance on Path-X and Path-256. Table 5: Long Document performance (micro _𝐹_ 1) at different sequence lengths using **Model** Path-X Path-256 FlashAttention. Transformer Linformer [84] 512 1024 2048 4096 8192 16384 Linear Attention [50] MIMIC-IIIECtHR[47][6] 52.872.2 50.774.3 51.777.1 54.678.6 **80.7** 56.4 **57.1** 79.2 LocalPerformerReformerAttention[51][12][80] SMYRF <u>[19]</u> FlashAttention **61.4** Block-sparse FlashAttention 56.0 **63.1** 

**Path-X and Path-256.** The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128×128 (or 256×256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance [80]. There has been a search for alternative architectures that can model such long context [37]. We present here the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). We pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings. FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy<sup>4</sup> on Path-256. **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and 

a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details.

---

[referencia=5727fed78bddc701 score=0.443]
_𝑖𝑗_−</sup><sup>_𝑚_</sup> _𝑖_<sup>new</sup> _ℓ_ ˜ _𝑖𝑗_ ∈ R<sup>_𝐵_</sup> _𝑟_ . 12: Write **O** _𝑖_ ← diag( _ℓ𝑖_<sup>new</sup> )<sup>−1</sup> (diag( _ℓ𝑖_ ) _𝑒_<sup>_𝑚𝑖_−</sup><sup>_𝑚_</sup> _𝑖_<sup>new</sup> **O** _𝑖_ + _𝑒_<sup>_𝑚_˜</sup><sup>_𝑖𝑗_−</sup><sup>_𝑚_</sup> _𝑖_<sup>new</sup> **P** _𝑖𝑗_ **V** _𝑗_ ) to HBM. 13: Write _ℓ𝑖_ ← _ℓ𝑖_<sup>new</sup> , _𝑚𝑖_ ← _𝑚𝑖_<sup>new</sup> to HBM. 14: **end for** 

15: **end for** 

16: Return **O** . 

We show FlashAttention’s correctness, runtime, and memory requirement (proof in Appendix C). **Theorem 1.** _Algorithm 1 returns_ **O** = softmax( **QK**<sup>⊤</sup> ) **V** _with 𝑂_ ( _𝑁_<sup>2</sup> _𝑑_ ) _FLOPs and requires 𝑂_ ( _𝑁_ ) _additional memory beyond inputs and output._ 

- **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared 

to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->

---

[referencia=5727fed78bddc701 score=0.413]
while performing on par with standard attention (Section 4). 

**4 Experiments** 

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks. 

• **Training Speed.** FlashAttention outperforms the MLPerf 1.1 [58] speed record for BERT by 15%, and speeds up GPT-2 up to 3× over HuggingFace [87] and 1 _._ 8× over Megatron [77] over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4×. 

• **Quality.** FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two long- 

document classification tasks. Finally, FlashAttention yields the **first Transformer** that can achieve 

better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the **first sequence model** that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K). 

• **Benchmarking Attention.** We measure the runtime and memory performance of FlashAttention 

and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3× faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines. 

Additional experiment details are in Appendix E. 

**4.1 Faster Models with FlashAttention**

---

[referencia=5727fed78bddc701 score=0.404]
Table 3: The performance of standard attention, FlashAttention, block-sparse FlashAttention, and approximate attention baselines on the Long-Range-Arena benchmarks. 

|Models|ListOps|Text|Retrieval|Image|Pathfnder|Avg|Speedup|
|---|---|---|---|---|---|---|---|
|Transformer|36.0|63.6|81.6|42.3|72.7|59.3|-|
|FlashAttention|37.6|63.9|81.4|43.5|72.7|59.8|2.4×|
|Block-sparse FlashAttention|37.0|63.0|81.3|43.6|73.3|59.6|**2.8**×|
|Linformer [84]|35.6|55.9|77.7|37.8|67.6|54.9|2.5×|
|Linear Attention [50]|38.8|63.2|80.7|42.6|72.5|59.6|2.3×|
|Performer [12]|36.8|63.6|82.2|42.1|69.9|58.9|1.8×|
|Local Attention [80]|36.1|60.2|76.7|40.6|66.6|56.0|1.7×|
|Reformer [51]|36.5|63.8|78.5|39.6|69.4|57.6|1.3×|
|Smyrf [19]|36.1|64.1|79.0|39.6|70.5|57.9|1.7×|

---

[referencia=5727fed78bddc701 score=0.341]
a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=5727fed78bddc701 score=0.325]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and 

block-sparse FlashAttention compared to prior attention implementations. 

• **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves 

their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 

6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

• **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512,

---

[referencia=5727fed78bddc701 score=0.299]
<!-- Start of picture text -->
FlashAttention: Fast and Memory-Efficient Exact Attention<br>with IO-Awareness<br>Tri Dao † , Daniel Y. Fu † , Stefano Ermon † , Atri Rudra ‡ , and Christopher Ré †<br>†Department of Computer Science, Stanford University<br>‡Department of Computer Science and Engineering, University at Buffalo, SUNY<br>{trid,danfu}@cs.stanford.edu , ermon@stanford.edu , atri@buffalo.edu ,<br>chrismre@cs.stanford.edu<br><!-- End of picture text -->

June 24, 2022 

**Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity 

of self-attention are quadratic in sequence length. Approximate attention methods have attempted 

to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity 

of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models 

(0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new

---

[referencia=5727fed78bddc701 score=0.228]
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

[referencia=5727fed78bddc701 score=0.179]
## **B.5 Comparison with Rabe and Staats [66]** 

We describe here some similarities and differences between our FlashAttention algorithm and the algorithm of Rabe and Staats [66]. 

Conceptually, both FlashAttention and Rabe and Staats [66] operate on blocks of the attention matrix using the well-established technique of tiling (or softmax scaling) [51, 60]. To reduce the memory footprint, both methods avoid storing the large attention matrix in the forward pass and recompute it in the backward pass. 

The first major difference is that Rabe and Staats [66] focuses on the reducing the total memory footprint (maximum amount of GPU memory required) while FlashAttention focuses on reducing memory accesses (the number of memory reads/writes). As mentioned in Section 2, the amount of memory access is the primary determining factor of runtime. Reducing memory accesses also necessarily reduces the total amount of memory required (e.g., if an operation incurs _𝐴_ memory accesses, then its total memory requirement is at most _𝐴_ ). As a result, FlashAttention is faster than standard attention (2-4×) while Rabe and Staats [66] is around the same speed or slightly slower than standard attention. In terms of total memory required, both methods offer substantial memory saving. 

The second difference between the two methods is the way information is summarized from each block to pass to the next block. Rabe and Staats [66] summarizes each block with its temporary output along with the softmax normalization statistics. At the end of the forward pass, the temporary outputs of all the blocks are combined using the statistics to produce the final output. FlashAttention instead incrementally updates the output (Algorithm 1 line 12) after processing each block, so only one copy of the output is needed (instead of _𝐾_ copies for _𝐾_ blocks). This means that FlashAttention has smaller total memory requirement compared to Rabe and Staats [66]. 

The final major difference is the way the backward pass is computed. Rabe and Staats [66] uses gradient checkpointing to recompute the attention matrix and the temporary output of each block. FlashAttention instead simplifies the backward pass analytically (Appendices B.2 and B.4). It only recomputes the attention matrix and does not recompute the temporary output of each block. This reduces the memory requirement for the backward pass and yields speedup.

---

[referencia=5727fed78bddc701 score=0.177]
# **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=5727fed78bddc701 score=0.172]
• **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, 

FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of. 

**2 Background** 

We provide some background on the performance characteristics of common deep learning operations on 

modern hardware (GPUs). We also describe the standard implementation of attention.

---

[referencia=5727fed78bddc701 score=0.159]
**B.3 FlashAttention: Forward Pass** 

- We describe the full details of FlashAttention forward pass. Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 

   - **S** = _𝜏_ **QK**<sup>⊤</sup> ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> _,_ **S**<sup>masked</sup> = mask( _𝑆_ ) ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> _,_ **P** = softmax( **S**<sup>masked</sup> ) ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> _,_ **P**<sup>dropped</sup> = dropout( **P** _, 𝑝_ drop) _,_ **O** = **P**<sup>dropped</sup> **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> _,_ 

- <u>1</u> 

- where _𝜏_ ∈ R is some softmax scaling (typically ~~√~~ _𝑑_<sup>),maskissomemaskingfunctionthatsetssomeentriesof</sup> the input to −∞ and keep other entries the same (e.g., key padding mask when sequences in the batch don’t 

- have the same lengths and are padded), and dropout( _𝑥, 𝑝_ ) applies dropout to _𝑥_ elementwise (i.e., output with probability 1 − _𝑝_ and output 0 with probability _𝑝_ for each element _𝑥_ ). 

_<u>𝑥</u>_ 1− _𝑝_ 

   - The full algorithm is in Algorithm 2. We save the output **O** , the softmax statistics _ℓ_ and _𝑚_ , and the 

- pseudo-random number generator state R for the backward pass. 

19

---

[referencia=5727fed78bddc701 score=0.157]
We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention. 

**Proposition 3.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. There does not exist an algorithm to compute exact attention with 𝑜_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses for all 𝑀 in the range_ [ _𝑑, 𝑁𝑑_ ] _._ 

The proof relies on the fact that for _𝑀_ = Θ( _𝑁𝑑_ ) any algorithm must perform Ω( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) = Ω( _𝑁𝑑_ ) HBM accesses. This type of lower bound over a subrange of _𝑀_ is common in the streaming algorithms literature [88]. We leave proving parameterized complexity [27] lower bounds in terms of _𝑀_ as exciting future work. 

We validate that the number of HBM accesses is the main determining factor of attention run-time. In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size _𝐵𝑐_ of FlashAttention, which results in different amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number of HBM accesses decreases (as we make fewer passes over the input), and runtime decreases. For large enough block size (beyond 256), the runtime is then bottlenecked by other factors (e.g., arithmetic operations). Moreover, larger block size will not fit into the small SRAM size.

---

[referencia=5727fed78bddc701 score=0.140]
## **3.3 Extension: Block-Sparse FlashAttention** 

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity. Given inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and a mask matrix **M**<sup>˜</sup> ∈{0 _,_ 1}<sup>_𝑁_×</sup><sup>_𝑁_</sup> , we want to compute: 



where ( **S** ⊙ 𝟙 **M** ˜ ) _𝑘𝑙_ = **S** _𝑘𝑙_ if **M**<sup>˜</sup> _𝑘𝑙_ = 1 and −∞ if **M** _𝑘𝑙_ = 0. We require **M**<sup>˜</sup> to have block form: for some block sizes _𝐵𝑟 , 𝐵𝑐_ , for all _𝑘, 𝑙_ , **M**<sup>˜</sup> _𝑘,𝑙_ = **M** _𝑖𝑗_ with _𝑖_ = ⌊ _𝑘_ / _𝐵𝑟_ ⌋ _, 𝑗_ = ⌊ _𝑙_ / _𝐵𝑐_ ⌋ for some **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> . 

6

---

[referencia=5727fed78bddc701 score=0.130]
to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._

---

[referencia=5727fed78bddc701 score=0.115]
6 

|Given a predefned block sparsity mask **M** ∈{0_,_1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup>we can easily adapt Algorithm 1 to only<br>compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we<br>skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.<br>We also analyze the IO complexity of block-sparse FlashAttention.|
|---|
|**Proposition 4.** _Let 𝑁be the sequence length, 𝑑be the head dimension, and 𝑀be size of SRAM with_<br>_𝑑_≤_𝑀_≤_𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ(_𝑁𝑑_+_𝑁_<sup>2</sup>_𝑑_<sup>2</sup>_𝑀_<sup>−1</sup>_𝑠_) _HBM accesses_<br>_where 𝑠is the fraction of nonzero blocks in the block-sparsity mask._|
|We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the<br>IO complexity. For large sequence lengths _𝑁_, _𝑠_is often set to _𝑁_<sup>−1/2 </sup>[11] or _𝑁_<sup>−1 </sup>log_𝑁_[3, 17, 92], resulting<br>in Θ(_𝑁_<br>√<br>_𝑁_) or Θ(_𝑁_log_𝑁_) IO complexity. For downstream experiments, we use the fxed butterfy sparsity<br>pattern [17], which has been shown to be able to approximate arbitrary sparsity [16].<br>In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention<br>improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup,|



while performing on par with standard attention (Section 4). 

**4 Experiments**

---

[referencia=5727fed78bddc701 score=0.106]
# **3 FlashAttention: Algorithm, Analysis, and Extensions** 

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention. 

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

---

[referencia=5727fed78bddc701 score=0.095]
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

[referencia=5727fed78bddc701 score=0.088]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>