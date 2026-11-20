[referencia=5727fed78bddc701 score=0.641]
# **3 FlashAttention: Algorithm, Analysis, and Extensions** 

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention. 

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

---

[referencia=5727fed78bddc701 score=0.398]
1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

Figure 1: **Left:** FlashAttention uses tiling to prevent materialization of the large _𝑁_ × _𝑁_ attention matrix (dotted box) on (relatively) slow GPU HBM. In the outer loop (red arrows), FlashAttention loops through blocks of the **K** and **V** matrices and loads them to fast on-chip SRAM. In each block, FlashAttention loops over blocks of **Q** matrix (blue arrows), loading them to SRAM, and writing the output of the attention computation back to HBM. **Right:** Speedup over the PyTorch implementation of attention on GPT-2. FlashAttention does not read and write the large _𝑁_ × _𝑁_ attention matrix to HBM, resulting in an 7.6× speedup on the attention computation. 

GPUs, compute speed has out-paced memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43]. IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime—such as database joins [71], image processing [70], numerical linear algebra [4], and more [40, 85]. However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

---

[referencia=5727fed78bddc701 score=0.300]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.071]
For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3. 

The main idea of the proof is that given the SRAM size of _𝑀_ , we can load blocks of **K** _,_ **V** of size Θ( _𝑀_ ) each (Algorithm 1 line 6). For each block of **K** and **V** , we iterate over all blocks of **Q** (Algorithm 1 line 8) to compute the intermediate values, resulting in Θ( _𝑁𝑑𝑀_<sup>−1</sup> ) passes over **Q** . Each pass loads Θ( _𝑁𝑑_ ) elements, which amounts to Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses. We similarly prove that the backward pass of standard attention requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). 

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention.

---

[referencia=5727fed78bddc701 score=0.070]
## **B.5 Comparison with Rabe and Staats [66]** 

We describe here some similarities and differences between our FlashAttention algorithm and the algorithm of Rabe and Staats [66]. 

Conceptually, both FlashAttention and Rabe and Staats [66] operate on blocks of the attention matrix using the well-established technique of tiling (or softmax scaling) [51, 60]. To reduce the memory footprint, both methods avoid storing the large attention matrix in the forward pass and recompute it in the backward pass. 

The first major difference is that Rabe and Staats [66] focuses on the reducing the total memory footprint (maximum amount of GPU memory required) while FlashAttention focuses on reducing memory accesses (the number of memory reads/writes). As mentioned in Section 2, the amount of memory access is the primary determining factor of runtime. Reducing memory accesses also necessarily reduces the total amount of memory required (e.g., if an operation incurs _𝐴_ memory accesses, then its total memory requirement is at most _𝐴_ ). As a result, FlashAttention is faster than standard attention (2-4×) while Rabe and Staats [66] is around the same speed or slightly slower than standard attention. In terms of total memory required, both methods offer substantial memory saving. 

The second difference between the two methods is the way information is summarized from each block to pass to the next block. Rabe and Staats [66] summarizes each block with its temporary output along with the softmax normalization statistics. At the end of the forward pass, the temporary outputs of all the blocks are combined using the statistics to produce the final output. FlashAttention instead incrementally updates the output (Algorithm 1 line 12) after processing each block, so only one copy of the output is needed (instead of _𝐾_ copies for _𝐾_ blocks). This means that FlashAttention has smaller total memory requirement compared to Rabe and Staats [66]. 

The final major difference is the way the backward pass is computed. Rabe and Staats [66] uses gradient checkpointing to recompute the attention matrix and the temporary output of each block. FlashAttention instead simplifies the backward pass analytically (Appendices B.2 and B.4). It only recomputes the attention matrix and does not recompute the temporary output of each block. This reduces the memory requirement for the backward pass and yields speedup.

---

[referencia=5727fed78bddc701 score=0.064]
## **D.2 Potential Extensions** 

We discuss here a few potential extensions of the IO-aware approach to speed up deep learning training. **Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other 

25 

GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. 

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. We believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. We are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime. 

**Kernel machine learning.** Our approach in FlashAttention relies on the fact that the _𝑁_ × _𝑁_ attention matrix is a function of a low-rank matrix **QK**<sup>⊤</sup> (of rank _𝑑_ ≪ _𝑁_ ). As a result, we can repeatedly load the inputs **Q** _,_ **K** and recompute the block of the attention matrix that we need, significantly reducing HBM access. As similar scenario happens in kernel machine learning: each element _𝐾𝑖𝑗_ of the _𝑁_ × _𝑁_ kernel matrix **K** is a function of two vectors of size _𝑑_ ≪ _𝑁_ , as it measures the similarity between two datapoints _𝑥𝑖_ and _𝑥 𝑗_ . The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. We hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs.

---

[referencia=5727fed78bddc701 score=0.060]
## **2.2 Standard Attention Implementation** 

Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> where _𝑁_ is the sequence length and _𝑑_ is the head dimension, we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



where softmax is applied row-wise. 

Standard attention implementations materialize the matrices **S** and **P** to HBM, which takes _𝑂_ ( _𝑁_<sup>2</sup> ) memory. Often _𝑁_ ≫ _𝑑_ (e.g., for GPT2, _𝑁_ = 1024 and _𝑑_ = 64). We describe the standard attention implementation in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time. 

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to **S** or dropout applied to **P** . As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax [77]. 

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length _𝑁_ . We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention). 

**Algorithm 0** Standard Attention Implementation 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM.

---

[referencia=5727fed78bddc701 score=0.053]
|However, by storing the output **O** and the softmax normalization statistics (_𝑚, ℓ_), we can recompute the<br>attention matrix **S** and **P** easily in the backward pass from blocks of **Q**_,_**K**_,_**V** in SRAM. This can be seen as a<br>form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce<br>the maximum amount of memory required [66], all implementations (that we know of) have to trade speed|



for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B. 

**Implementation details: Kernel fusion.** Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, 

optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM. **Algorithm 1** FlashAttention **Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ . 1: Set block sizes _𝐵𝑐_ = � 4 _<u>𝑀𝑑</u>_ � _, 𝐵𝑟_ = min<sup>��</sup> 4<sup>_<u>𝑀</u>_</sup> _𝑑_ � _, 𝑑_<sup>�</sup> . 

2: Initialize **O** = (0) _𝑁_ × _𝑑_ ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> _, ℓ_ = (0) _𝑁_ ∈ R<sup>_𝑁_</sup> _, 𝑚_ = (−∞) _𝑁_ ∈ R<sup>_𝑁_</sup> in HBM.

---

[referencia=5727fed78bddc701 score=0.045]
### _arithmetic intensity_ [85], which is the number of arithmetic operations per byte of memory access. 

1. Compute-bound: the time taken by the operation is determined by how many arithmetic operations there 

are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels. 

2. Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm). 

**Kernel fusion.** The most common approach to accelerate memory-bound operations is kernel fusion: if there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations [53, 65, 75]. 

> 1FlashAttention code is available at `https://github.com/HazyResearch/flash-attention` 

3 

However, in the context of model training, the intermediate values still need to be written to HBM to save for the backward pass, reducing the effectiveness of naive kernel fusion.

---

[referencia=5727fed78bddc701 score=0.042]
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

[referencia=5727fed78bddc701 score=0.033]
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

[referencia=5727fed78bddc701 score=0.032]
## **3.1 An Efficient Attention Algorithm With Tiling and Recomputation** 

Given the inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, we aim to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in _𝑁_ ). 

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs **Q** _,_ **K** _,_ **V** into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end. 

**Tiling.** We compute attention by blocks. Softmax couples columns of **K** , so we decompose the large softmax with scaling [51, 60, 66]. For numerical stability, the softmax of vector _𝑥_ ∈ R<sup>_𝐵_</sup> is computed as: 



4

---

[referencia=5727fed78bddc701 score=0.029]
(0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new 

capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy). 

**1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], 

and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->

---

[referencia=5727fed78bddc701 score=0.028]
6 

|Given a predefned block sparsity mask **M** ∈{0_,_1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup>we can easily adapt Algorithm 1 to only<br>compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we<br>skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.<br>We also analyze the IO complexity of block-sparse FlashAttention.|
|---|
|**Proposition 4.** _Let 𝑁be the sequence length, 𝑑be the head dimension, and 𝑀be size of SRAM with_<br>_𝑑_≤_𝑀_≤_𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ(_𝑁𝑑_+_𝑁_<sup>2</sup>_𝑑_<sup>2</sup>_𝑀_<sup>−1</sup>_𝑠_) _HBM accesses_<br>_where 𝑠is the fraction of nonzero blocks in the block-sparsity mask._|
|We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the<br>IO complexity. For large sequence lengths _𝑁_, _𝑠_is often set to _𝑁_<sup>−1/2 </sup>[11] or _𝑁_<sup>−1 </sup>log_𝑁_[3, 17, 92], resulting<br>in Θ(_𝑁_<br>√<br>_𝑁_) or Θ(_𝑁_log_𝑁_) IO complexity. For downstream experiments, we use the fxed butterfy sparsity<br>pattern [17], which has been shown to be able to approximate arbitrary sparsity [16].<br>In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention<br>improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup,|



while performing on par with standard attention (Section 4). 

**4 Experiments**

---

[referencia=5727fed78bddc701 score=0.028]
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

[referencia=5727fed78bddc701 score=0.027]
## **E.6 Full Benchmarking Results** 

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

[referencia=5727fed78bddc701 score=0.025]
# **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=5727fed78bddc701 score=0.024]
## **B.1 Memory-efficient forward pass** 

The main challenge in making attention memory-efficient is the softmax that couples the columns of **K** (and columns of **V** ). Our approach is to compute the softmax normalization constant separately to decouple the columns. This technique [60] has been used in the literature [51, 66] to show that attention computation does not need quadratic _extra_ memory (though the number of HBM accesses is still quadratic, resulting in slow run-time). 

For simplicity, we omit here the max-shifting step during softmax. The full algorithm in Appendix B.3 contains all the steps. 

Recall that given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



We have that _𝑆𝑖𝑗_ = _𝑞_<sup>_𝑇_</sup> _𝑖_<sup>_𝑘𝑗_where</sup><sup>_𝑞𝑖_and</sup><sup>_𝑘𝑗_arethe</sup><sup>_𝑖_-thand</sup><sup>_𝑗_-thcolumnsof</sup><sup>**Q**and</sup><sup>**K**respectively.Define</sup> the normalization constants of softmax: 



Let _𝑣 𝑗_ be the _𝑗_ -th column of **V** , then the _𝑖_ -th columns of the output is 



We see that once _𝐿𝑖_ is computed, we can compute _𝑜𝑖_ without extra memory by repeatedly summing _<u>𝑒</u>_<sup>_𝑞𝑇_</sup> _𝑖_<sup>_𝑘𝑗_</sup> _𝐿𝑖 𝑣 𝑗_ . Therefore the forward pass can be computed with _𝑂_ ( _𝑛_ ) extra memory:

---

[referencia=5727fed78bddc701 score=0.021]
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

[referencia=5727fed78bddc701 score=0.018]
## **B.2 Memory-efficient backward pass** 

We derive the backward pass of attention and show that it can also be computed with linear memory. Rabe and Staats [66] suggests that the backward pass can be done without quadratic extra memory by applying gradient checkpointing to the memory-efficient forward pass. We instead derive the backward pass explicitly and show how it can be computed in a memory-efficient manner. 

Suppose that there is a scalar loss function _𝜙_ , and let the output gradient be **dO** ∈ R<sup>_𝑛_×</sup><sup>_𝑑_</sup> (where **dO** denotes _𝜕𝜙_<sup>Wewanttocomputetheinputgradients</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**∈R</sup><sup>_𝑛_×</sup><sup>_𝑑_(where</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**denote</sup><sup>_𝜕𝜙𝜕𝜙𝜕𝜙_</sup> _𝜕_ **O**<sup>).</sup> _𝜕_ **Q**<sup>_,_</sup> _𝜕_ **K**<sup>_,_</sup> _𝜕_ **V** respectively). 

The gradient **dV** is easy to see. Applying reverse-mode autodiff by hand (aka the chain rule), we obtain (in matrix notation) **dV** = **P**<sup>_𝑇_</sup> **dO** . Thus: 



Since we already computed _𝐿𝑖_ , _𝑑𝑣 𝑗_ can be computed without extra memory by repeated summing. 

The gradients **dQ** and **dK** are a little more complicated. We go through the gradients **dP** and **dS** first. From Eq. (2), we have that **dP** = **dOV**<sup>_𝑇_</sup> , and so: