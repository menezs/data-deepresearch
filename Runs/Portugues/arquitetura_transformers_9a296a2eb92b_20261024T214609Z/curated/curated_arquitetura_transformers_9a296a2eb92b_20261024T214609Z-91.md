[referencia=9cb658eb63c3853b score=0.816]
asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

---

[referencia=9cb658eb63c3853b score=0.767]
The main idea of the proof is that given the SRAM size of _𝑀_ , we can load blocks of **K** _,_ **V** of size Θ( _𝑀_ ) each (Algorithm 1 line 6). For each block of **K** and **V** , we iterate over all blocks of **Q** (Algorithm 1 line 8) to compute the intermediate values, resulting in Θ( _𝑁𝑑𝑀_<sup>−1</sup> ) passes over **Q** . Each pass loads Θ( _𝑁𝑑_ ) elements, which amounts to Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses. We similarly prove that the backward pass of standard attention requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). 

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention. 

**Proposition 3.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. There does not exist an algorithm to compute exact attention with 𝑜_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses for all 𝑀 in the range_ [ _𝑑, 𝑁𝑑_ ] _._

---

[referencia=9cb658eb63c3853b score=0.686]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=9cb658eb63c3853b score=0.637]
</sup> to HBM. 22: On chip, compute **dK**<sup>˜</sup> _𝑗_ ← **dK**<sup>˜</sup> _𝑗_ + _𝜏_ **dS**<sup>⊤</sup> _𝑖𝑗_<sup>**Q**</sup><sup>_𝑖_∈R</sup><sup>_𝐵𝑐_×</sup><sup>_𝑑_.</sup> 23: **end for** ˜ ˜ 24: Write **dK** _𝑗_ ← **dK** _𝑗 ,_ **dV** _𝑗_ ← **dV** _𝑗_ to HBM. 25: **end for** 

- 26: Return **dQ** _,_ **dK** _,_ **dV** . 

We see that similar to the forward pass, the backward pass performs _𝑂_ ( _𝑁_<sup>2</sup> ) FLOPs and only requires _𝑂_ ( _𝑁_ ) extra memory beyond inputs, output, output gradient, and input gradients. 

We analyze the IO-complexity of the backward pass, similar to the forward pass (Theorem 2). 

**Theorem 5.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) backward pass requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _backward pass (Algorithm 4) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

The proof is in Appendix C. 

21

---

[referencia=9cb658eb63c3853b score=0.462]
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

[referencia=9cb658eb63c3853b score=0.459]
### **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

---

[referencia=9cb658eb63c3853b score=0.394]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=9cb658eb63c3853b score=0.313]
The proof relies on the fact that for _𝑀_ = Θ( _𝑁𝑑_ ) any algorithm must perform Ω( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) = Ω( _𝑁𝑑_ ) HBM accesses. This type of lower bound over a subrange of _𝑀_ is common in the streaming algorithms literature [88]. We leave proving parameterized complexity [27] lower bounds in terms of _𝑀_ as exciting future work. 

We validate that the number of HBM accesses is the main determining factor of attention run-time. In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size _𝐵𝑐_ of FlashAttention, which results in different amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number of HBM accesses decreases (as we make fewer passes over the input), and runtime decreases. For large enough block size (beyond 256), the runtime is then bottlenecked by other factors (e.g., arithmetic operations). Moreover, larger block size will not fit into the small SRAM size.

---

[referencia=9cb658eb63c3853b score=0.285]
- **Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ , softmax scaling constant _𝜏_ ∈ R, masking function mask, dropout probability _𝑝_ drop. 

- 1: Initialize the pseudo-random number generator state R and save to HBM. 2: Set block sizes _𝐵𝑐_ = � 4 _<u>𝑀𝑑</u>_ � _, 𝐵𝑟_ = min<sup>��</sup> 4<sup>_<u>𝑀</u>_</sup> _𝑑_ � _, 𝑑_<sup>�</sup> . 3: Initialize **O** = (0) _𝑁_ × _𝑑_ ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> _, ℓ_ = (0) _𝑁_ ∈ R<sup>_𝑁_</sup> _, 𝑚_ = (−∞) _𝑁_ ∈ R<sup>_𝑁_</sup> in HBM. 4: Divide **Q** into _𝑇𝑟_ = � _𝐵𝑁𝑟_ � blocks **Q** 1 _, . . . ,_ **Q** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, and divide **K** _,_ **V** in to _𝑇𝑐_ = � _𝐵𝑁𝑐_ � blocks **K** 1 _, . . . ,_ **K** _𝑇𝑐_ and **V** 1 _, . . . ,_ **V** _𝑇𝑐_ , of size _𝐵𝑐_ × _𝑑_ each.

---

[referencia=9cb658eb63c3853b score=0.263]
## **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=9cb658eb63c3853b score=0.229]
### **2.2 Standard Attention Implementation** 

Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> where _𝑁_ is the sequence length and _𝑑_ is the head dimension, we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



where softmax is applied row-wise. 

Standard attention implementations materialize the matrices **S** and **P** to HBM, which takes _𝑂_ ( _𝑁_<sup>2</sup> ) memory. Often _𝑁_ ≫ _𝑑_ (e.g., for GPT2, _𝑁_ = 1024 and _𝑑_ = 64). We describe the standard attention implementation in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time. 

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to **S** or dropout applied to **P** . As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax [77]. 

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length _𝑁_ . We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention). 

**Algorithm 0** Standard Attention Implementation 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM.

---

[referencia=9cb658eb63c3853b score=0.197]
### **2.1 Hardware Performance** 

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

[referencia=9cb658eb63c3853b score=0.192]
##### **Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

---

[referencia=9cb658eb63c3853b score=0.174]
**Require:** Matrices **Q** _,_ **K** _,_ **V** _,_ **O** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, vectors _ℓ, 𝑚_ ∈ R<sup>_𝑁_</sup> in HBM, on-chip SRAM of size _𝑀_ , softmax scaling constant _𝜏_ ∈ R, masking function mask, dropout probability _𝑝_ drop, pseudo-random number generator state R from the forward pass. 1: Set the pseudo-random number generator state to R. 2: Set block sizes _𝐵𝑐_ = <u>�</u> 4 _<u>𝑀𝑑</u>_ � _, 𝐵𝑟_ = min<sup>��</sup> 4<sup>_<u>𝑀</u>_</sup> _𝑑_ � _, 𝑑_<sup>�</sup> . 3: Divide **Q** into _𝑇𝑟_ = � _𝐵𝑁𝑟_ � blocks **Q** 1 _, . . . ,_ **Q** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, and divide **K** _,_ **V** in to _𝑇𝑐_ = � _𝐵𝑁𝑐_ � blocks **K** 1 _, . . . ,_ **K** _𝑇𝑐_ and **V** 1 _, . . . ,_ **V** _𝑇𝑐_ , of size _𝐵𝑐_ × _𝑑_ each. 4: Divide **O** into _𝑇𝑟_ blocks **O** _𝑖, . . . ,_ **O** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, divide **dO** into _𝑇𝑟_ blocks **dO** _𝑖, . . . ,_ **dO** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_

---

[referencia=9cb658eb63c3853b score=0.136]
blocks **dO** _𝑖, . . . ,_ **dO** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, divide _ℓ_ into _𝑇𝑟_ blocks _ℓ𝑖, . . . , ℓ𝑇𝑟_ of size _𝐵𝑟_ each, divide _𝑚_ into _𝑇𝑟_ blocks _𝑚_ 1 _, . . . , 𝑚𝑇𝑟_ of size _𝐵𝑟_ each. 5: Initialize **dQ** = (0) _𝑁_ × _𝑑_ in HBM and divide it into _𝑇𝑟_ blocks **dQ** 1 _, . . . ,_ **dQ** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each. Initialize **dK** = (0) _𝑁_ × _𝑑,_ **dV** = (0) _𝑁_ × _𝑑_ in HBM and divide **dK** _,_ **dV** in to _𝑇𝑐_ blocks **dK** 1 _, . . . ,_ **dK** _𝑇𝑐_ and **dV** 1 _, . . . ,_ **dV** _𝑇𝑐_ , of size _𝐵𝑐_ × _𝑑_ each. 6: **for** 1 ≤ _𝑗_ ≤ _𝑇𝑐_ **do** 7: Load **K** _𝑗 ,_ **V** _𝑗_ from HBM to on-chip SRAM. 8: Initialize **dK**<sup>˜</sup> _𝑗_ = (0) _𝐵𝑐_ × _𝑑,_ **dV**<sup>˜</sup> _𝑗_ = (0) _𝐵𝑐_ × _𝑑_ on SRAM. 9: **for** 1 ≤ _𝑖_ ≤ _𝑇𝑟_ **do**

---

[referencia=9cb658eb63c3853b score=0.133]
**Recomputation.** One of our goals is to not store _𝑂_ ( _𝑁_<sup>2</sup> ) intermediate values for the backward pass. The backward pass typically requires the matrices **S** _,_ **P** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> to compute the gradients with respect to **Q** _,_ **K** _,_ **V** . However, by storing the output **O** and the softmax normalization statistics ( _𝑚, ℓ_ ), we can recompute the attention matrix **S** and **P** easily in the backward pass from blocks of **Q** _,_ **K** _,_ **V** in SRAM. This can be seen as a form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce the maximum amount of memory required [66], all implementations (that we know off) have to trade speed for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B. 

**Implementation details: Kernel fusion.** Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM. 

**Algorithm 1** FlashAttention 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ .

---

[referencia=9cb658eb63c3853b score=0.116]
### **3.1 An Efficient Attention Algorithm With Tiling and Recomputation** 

Given the inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, we aim to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in _𝑁_ ). 

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs **Q** _,_ **K** _,_ **V** into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end. 

**Tiling.** We compute attention by blocks. Softmax couples columns of **K** , so we decompose the large softmax with scaling [51, 60, 66]. For numerical stability, the softmax of vector _𝑥_ ∈ R<sup>_𝐵_</sup> is computed as: 



4 



Therefore if we keep track of some extra statistics ( _𝑚_ ( _𝑥_ ) _, ℓ_ ( _𝑥_ )), we can compute softmax one block at a time.<sup>2</sup> We thus split the inputs **Q** _,_ **K** _,_ **V** into blocks (Algorithm 1 line 3), compute the softmax values along with extra statistics (Algorithm 1 line 10), and combine the results (Algorithm 1 line 12).

---

[referencia=9cb658eb63c3853b score=0.115]
We also analyze the IO complexity of block-sparse FlashAttention. 

**Proposition 4.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> _𝑠_ ) _HBM accesses where 𝑠 is the fraction of nonzero blocks in the block-sparsity mask._ 

We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths _𝑁_ , _𝑠_ is often set to _𝑁_<sup>−1/2</sup> [11] or _𝑁_<sup>−1</sup> log _𝑁_ [3, 17, 92], resulting in Θ( _𝑁_ √ _𝑁_ ) or Θ( _𝑁_ log _𝑁_ ) IO complexity. For downstream experiments, we use the fixed butterfly sparsity pattern [17], which has been shown to be able to approximate arbitrary sparsity [16]. 

In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup, while performing on par with standard attention (Section 4).

---

[referencia=9cb658eb63c3853b score=0.098]
Figure 1: **Left:** FlashAttention uses tiling to prevent materialization of the large _𝑁_ × _𝑁_ attention matrix (dotted box) on (relatively) slow GPU HBM. In the outer loop (red arrows), FlashAttention loops through blocks of the **K** and **V** matrices and loads them to fast on-chip SRAM. In each block, FlashAttention loops over blocks of **Q** matrix (blue arrows), loading them to SRAM, and writing the output of the attention computation back to HBM. **Right:** Speedup over the PyTorch implementation of attention on GPT-2. FlashAttention does not read and write the large _𝑁_ × _𝑁_ attention matrix to HBM, resulting in an 7.6× speedup on the attention computation. 

GPUs, compute speed has out-paced memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43]. IO-aware algorithms have been critical for similar memory-bound operations, when reading and writing data can account for a large portion of the runtime—such as database joins [71], image processing [70], numerical linear algebra [4], and more [40, 85]. However, common Python interfaces to deep learning such as PyTorch and Tensorflow do not allow fine-grained control of memory access.

---

[referencia=9cb658eb63c3853b score=0.088]
## **D Extension Details** 

### **D.1 Block-sparse FlashAttention** 

We describe the full block-sparse FlashAttention algorithm in Algorithm 5. The algorithm is identical to Algorithm 2, except that we skip zero blocks. 

We prove the IO-complexity of block-sparse FlashAttention. 

_Proof of Proposition 4._ The proof is very similar to the proof of Theorem 2. For the block-sparse case, notice that we only need to load blocks corresponding to nonzero blocks. As a result, the number of HBM accesses are scaled by _𝑠_ , the fraction of nonzero blocks in the block-sparsity mask. However, for small values of _𝑠_ , we would still need to write the result **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> . Therefore the number of HBM accesses is