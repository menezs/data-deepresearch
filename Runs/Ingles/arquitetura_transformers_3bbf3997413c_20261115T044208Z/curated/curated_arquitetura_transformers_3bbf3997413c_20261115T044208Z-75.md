[referencia=5727fed78bddc701 score=0.995]
FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness 

Tri Dao<sup>†</sup> , Daniel Y. Fu<sup>†</sup> , Stefano Ermon<sup>†</sup> , Atri Rudra<sup>‡</sup> , and Christopher Ré<sup>†</sup> 

      - †Department of Computer Science, Stanford University 

- ‡Department of Computer Science and Engineering, University at Buffalo, SUNY 

   - `{trid,danfu}@cs.stanford.edu` , `ermon@stanford.edu` , `atri@buffalo.edu` , `chrismre@cs.stanford.edu` 

June 24, 2022 

**Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding

---

[referencia=5727fed78bddc701 score=0.976]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.961]
# **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention 

and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=5727fed78bddc701 score=0.932]
Overall, standard attention implementation requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) global memory accesses. We now analyze the IO complexity of streaming attention. 

Following Algorithm 1, we see that each element of **K** and **V** is loaded from HBM once (Algorithm 1 line 6). We make _𝑇𝑐_ passes over **Q** and **O** , each pass loading all of **Q** and all of **O** to HBM (Algorithm 1 line 8). Therefore the number of HBM accesses is Θ ( _𝑁𝑑_ + _𝑁𝑑𝑇𝑐_ ) = Θ( _𝑁𝑑𝑇𝑐_ ). 

We derive the conditions on the block sizes _𝐵𝑐_ and _𝐵𝑟_ . We need the blocks **K** _𝑗_ and **V** _𝑗_ of size _𝐵𝑐_ × _𝑑_ to fit into on-chip memory, which translates to: 



Similarly, we need the blocks **Q** _𝑖,_ **O** _𝑖_ of size _𝐵𝑟_ × _𝑑_ to fit into on-chip memory, which translates to: 



Finally, we need the block **S** _𝑖𝑗_ of size _𝐵𝑟_ × _𝐵𝑐_ to fit into on-chip memory, which translates to: 



23 

We therefore set: 

We then have: 



As a result, the number of HBM accesses is: 



□ 

_Proof of Proposition 3._ For contradiction, suppose that there exists an algorithm that computes exact attention where the number for HBM access for all _𝑀_ ∈[ _𝑑, 𝑁𝑑_ ] is 



In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses:

---

[referencia=5727fed78bddc701 score=0.896]
## **3.1 An Efficient Attention Algorithm With Tiling and Recomputation** 

Given the inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, we aim to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in _𝑁_ ). 

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs **Q** _,_ **K** _,_ **V** into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end. 

**Tiling.** We compute attention by blocks. Softmax couples columns of **K** , so we decompose the large softmax with scaling [51, 60, 66]. For numerical stability, the softmax of vector _𝑥_ ∈ R<sup>_𝐵_</sup> is computed as: 



4 



Therefore if we keep track of some extra statistics ( _𝑚_ ( _𝑥_ ) _, ℓ_ ( _𝑥_ )), we can compute softmax one block at a time.<sup>2</sup> We thus split the inputs **Q** _,_ **K** _,_ **V** into blocks (Algorithm 1 line 3), compute the softmax values along with extra statistics (Algorithm 1 line 10), and combine the results (Algorithm 1 line 12).

---

[referencia=5727fed78bddc701 score=0.879]
# **5 Limitations and Future Directions** 

We discuss limitations of our approach and future directions. Related work is given in Appendix A. 

**Compiling to CUDA.** Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA—similar to efforts such as Halide in image processing [70]. 

**IO-Aware Deep Learning.** We believe that the IO-aware approach can extend beyond attention. Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. We hope our work inspires IO-aware implementations of additional modules. We discuss these potential extensions in Appendix D. 

**Multi-GPU IO-Aware Methods.** Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs [72]. Using multiple GPUs adds an additional layer to IO analysis—accounting for data transfer between GPUs. We hope our work inspires future work in this direction.

---

[referencia=5727fed78bddc701 score=0.873]
requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention. 

**Proposition 3.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. There does not exist an algorithm to compute exact attention with 𝑜_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses for all 𝑀 in the range_ [ _𝑑, 𝑁𝑑_ ] _._ 

The proof relies on the fact that for _𝑀_ = Θ( _𝑁𝑑_ ) any algorithm must perform Ω( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) = Ω( _𝑁𝑑_ ) HBM accesses. This type of lower bound over a subrange of _𝑀_ is common in the streaming algorithms literature [88]. We leave proving parameterized complexity [27] lower bounds in terms of _𝑀_ as exciting future work. We validate that the number of HBM accesses is the main determining factor of attention run-time. 

In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size _𝐵𝑐_ of FlashAttention, which results in different 

amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number

---

[referencia=5727fed78bddc701 score=0.784]
## **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=5727fed78bddc701 score=0.771]
# **3 FlashAttention: Algorithm, Analysis, and Extensions** 

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention. 

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

---

[referencia=5727fed78bddc701 score=0.752]
Figure 1: **Left:** FlashAttention uses tiling to prevent materialization of the large _𝑁_ × _𝑁_ attention matrix (dotted box) on (relatively) slow GPU HBM. In the outer loop (red arrows), FlashAttention loops through blocks of the **K** and **V** matrices and loads them to fast on-chip SRAM. In each block, FlashAttention loops over blocks of **Q** matrix (blue arrows), loading them to SRAM, and writing the output of the attention computation back to HBM. **Right:** Speedup over the PyTorch implementation of attention on GPT-2. FlashAttention does not read and write the large _𝑁_ × _𝑁_ attention matrix to HBM, resulting in an 7.6× speedup on the attention computation. 

GPUs, compute speed has out-paced memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43]. IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime—such as database joins [71], image processing [70], numerical linear algebra [4], and more [40, 85]. However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

---

[referencia=5727fed78bddc701 score=0.646]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=5727fed78bddc701 score=0.642]
In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses: 



However, the input to attention (matrices **Q** _,_ **K** _,_ **V** ) and the output **O** have size _𝑁𝑑_ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least Ω( _𝑁𝑑_ ) HBM accesses. This is a contradiction. □ 

_Proof of Theorem 5._ The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). Here we provide a sketch of the proof. 

We first analyze the IO complexity of standard attention backward pass. The inputs **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the outputs **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> are written to HBM. 

At each step of the standard attention backward pass, one needs to load inputs of size _𝑁𝑑_ or _𝑁_<sup>2</sup> from HBM, and needs to write the outputs of size _𝑁_<sup>2</sup> or _𝑁𝑑_ to HBM. This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

We now analyze the IO complexity of FlashAttention backward pass.

---

[referencia=5727fed78bddc701 score=0.606]
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

[referencia=5727fed78bddc701 score=0.501]
**Recomputation.** One of our goals is to not store _𝑂_ ( _𝑁_<sup>2</sup> ) intermediate values for the backward pass. The backward pass typically requires the matrices **S** _,_ **P** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> to compute the gradients with respect to **Q** _,_ **K** _,_ **V** . However, by storing the output **O** and the softmax normalization statistics ( _𝑚, ℓ_ ), we can recompute the attention matrix **S** and **P** easily in the backward pass from blocks of **Q** _,_ **K** _,_ **V** in SRAM. This can be seen as a form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce the maximum amount of memory required [66], all implementations (that we know off) have to trade speed for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B. 

**Implementation details: Kernel fusion.** Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM. 

**Algorithm 1** FlashAttention 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ .

---

[referencia=5727fed78bddc701 score=0.491]
## **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 

|Attention<br>Standard<br>FlashAttention<br>GFLOPs<br>66.6<br>75.2<br>HBM R/W (GB)<br>40.3<br>4.4<br>Runtime (ms)<br>41.7<br>7.3<br>**Sparsity Speedup**<br>50<br>100<br>150<br>Fwd + Bwd (ms)<br>**Efect of Block Size**<br>Fwd Runtime (m<br>6<br>2<br>BM Accesses (GB)<br>**Dense**<br>**FlashAttention**<br>**Block-Sparse**<br>**FlashAttention**<br>2<br>4<br>6<br>**Runtime**<br>**HBM**<br>**Accesses**|
|---|
|% Non-Zero Blocks<br>20<br>60<br>Block Size<br>64 128<br>256<br>512<br>s)<br>H|
|Figure 2:<br>**Left**: Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium<br>(seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor afecting<br>runtime. **Middle**: Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on<br>A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right**: The runtime (for seq. length 4K) of<br>block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity.|
|asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.|

---

[referencia=5727fed78bddc701 score=0.469]
## **B.5 Comparison with Rabe and Staats [66]** 

We describe here some similarities and differences between our FlashAttention algorithm and the algorithm of Rabe and Staats [66]. 

Conceptually, both FlashAttention and Rabe and Staats [66] operate on blocks of the attention matrix using the well-established technique of tiling (or softmax scaling) [51, 60]. To reduce the memory footprint, both methods avoid storing the large attention matrix in the forward pass and recompute it in the backward pass. 

The first major difference is that Rabe and Staats [66] focuses on the reducing the total memory footprint (maximum amount of GPU memory required) while FlashAttention focuses on reducing memory accesses (the number of memory reads/writes). As mentioned in Section 2, the amount of memory access is the primary determining factor of runtime. Reducing memory accesses also necessarily reduces the total amount of memory required (e.g., if an operation incurs _𝐴_ memory accesses, then its total memory requirement is at most _𝐴_ ). As a result, FlashAttention is faster than standard attention (2-4×) while Rabe and Staats [66] is around the same speed or slightly slower than standard attention. In terms of total memory required, both methods offer substantial memory saving. 

The second difference between the two methods is the way information is summarized from each block to pass to the next block. Rabe and Staats [66] summarizes each block with its temporary output along with the softmax normalization statistics. At the end of the forward pass, the temporary outputs of all the blocks are combined using the statistics to produce the final output. FlashAttention instead incrementally updates the output (Algorithm 1 line 12) after processing each block, so only one copy of the output is needed (instead of _𝐾_ copies for _𝐾_ blocks). This means that FlashAttention has smaller total memory requirement compared to Rabe and Staats [66]. 

The final major difference is the way the backward pass is computed. Rabe and Staats [66] uses gradient checkpointing to recompute the attention matrix and the temporary output of each block. FlashAttention instead simplifies the backward pass analytically (Appendices B.2 and B.4). It only recomputes the attention matrix and does not recompute the temporary output of each block. This reduces the memory requirement for the backward pass and yields speedup.

---

[referencia=5727fed78bddc701 score=0.404]
## **D.2 Potential Extensions** 

We discuss here a few potential extensions of the IO-aware approach to speed up deep learning training. **Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other 

25 

GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. 

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. We believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. We are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime. 

**Kernel machine learning.** Our approach in FlashAttention relies on the fact that the _𝑁_ × _𝑁_ attention matrix is a function of a low-rank matrix **QK**<sup>⊤</sup> (of rank _𝑑_ ≪ _𝑁_ ). As a result, we can repeatedly load the inputs **Q** _,_ **K** and recompute the block of the attention matrix that we need, significantly reducing HBM access. As similar scenario happens in kernel machine learning: each element _𝐾𝑖𝑗_ of the _𝑁_ × _𝑁_ kernel matrix **K** is a function of two vectors of size _𝑑_ ≪ _𝑁_ , as it measures the similarity between two datapoints _𝑥𝑖_ and _𝑥 𝑗_ . The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. We hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs.

---

[referencia=5727fed78bddc701 score=0.368]
## **B.1 Memory-efficient forward pass** 

The main challenge in making attention memory-efficient is the softmax that couples the columns of **K** (and columns of **V** ). Our approach is to compute the softmax normalization constant separately to decouple the columns. This technique [60] has been used in the literature [51, 66] to show that attention computation does not need quadratic _extra_ memory (though the number of HBM accesses is still quadratic, resulting in slow run-time). 

For simplicity, we omit here the max-shifting step during softmax. The full algorithm in Appendix B.3 contains all the steps. 

Recall that given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



We have that _𝑆𝑖𝑗_ = _𝑞_<sup>_𝑇_</sup> _𝑖_<sup>_𝑘𝑗_where</sup><sup>_𝑞𝑖_and</sup><sup>_𝑘𝑗_arethe</sup><sup>_𝑖_-thand</sup><sup>_𝑗_-thcolumnsof</sup><sup>**Q**and</sup><sup>**K**respectively.Define</sup> the normalization constants of softmax: 



Let _𝑣 𝑗_ be the _𝑗_ -th column of **V** , then the _𝑖_ -th columns of the output is 



We see that once _𝐿𝑖_ is computed, we can compute _𝑜𝑖_ without extra memory by repeatedly summing _<u>𝑒</u>_<sup>_𝑞𝑇_</sup> _𝑖_<sup>_𝑘𝑗_</sup> _𝐿𝑖 𝑣 𝑗_ . Therefore the forward pass can be computed with _𝑂_ ( _𝑛_ ) extra memory:

---

[referencia=5727fed78bddc701 score=0.305]
## **2.1 Hardware Performance** 

We focus here on GPUs. Performance on other hardware accelerators are similar [46, 48]. 

**GPU Memory Hierarchy.** The GPU memory hierarchy (Fig. 1 left) comprises multiple forms of memory of different sizes and speeds, with smaller memory being faster. As an example, the A100 GPU has 40-80GB of high bandwidth memory (HBM) with bandwidth 1.5-2.0TB/s and 192KB of on-chip SRAM per each of 108 streaming multiprocessors with bandwidth estimated around 19TB/s [44, 45]. The on-chip SRAM is an order of magnitude faster than HBM but many orders of magnitude smaller in size. As compute has gotten faster relative to memory speed [61, 62, 63], operations are increasingly bottlenecked by memory (HBM) accesses. Thus exploiting fast SRAM becomes more important. 

**Execution Model.** GPUs have a massive number of threads to execute an operation (called a kernel). Each kernel loads inputs from HBM to registers and SRAM, computes, then writes outputs to HBM. 

**Performance characteristics.** Depending on the balance of computation and memory accesses, operations can be classified as either compute-bound or memory-bound. This is commonly measured by the _arithmetic intensity_ [85], which is the number of arithmetic operations per byte of memory access. 

1. Compute-bound: the time taken by the operation is determined by how many arithmetic operations there are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels. 

2. Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm). **Kernel fusion.** The most common approach to accelerate memory-bound operations is kernel fusion: if 

there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations [53, 65, 75]. 

> 1FlashAttention code is available at `https://github.com/HazyResearch/flash-attention` 

3

---

[referencia=5727fed78bddc701 score=0.266]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>