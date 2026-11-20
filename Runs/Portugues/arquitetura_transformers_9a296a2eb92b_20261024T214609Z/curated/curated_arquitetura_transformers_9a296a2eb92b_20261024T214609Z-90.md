[referencia=9cb658eb63c3853b score=0.900]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=9cb658eb63c3853b score=0.865]
**Recomputation.** One of our goals is to not store _𝑂_ ( _𝑁_<sup>2</sup> ) intermediate values for the backward pass. The backward pass typically requires the matrices **S** _,_ **P** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> to compute the gradients with respect to **Q** _,_ **K** _,_ **V** . However, by storing the output **O** and the softmax normalization statistics ( _𝑚, ℓ_ ), we can recompute the attention matrix **S** and **P** easily in the backward pass from blocks of **Q** _,_ **K** _,_ **V** in SRAM. This can be seen as a form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce the maximum amount of memory required [66], all implementations (that we know off) have to trade speed for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B. 

**Implementation details: Kernel fusion.** Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM. 

**Algorithm 1** FlashAttention 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ .

---

[referencia=9cb658eb63c3853b score=0.821]
## **3 FlashAttention: Algorithm, Analysis, and Extensions** 

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention. 

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

---

[referencia=9cb658eb63c3853b score=0.790]
</sup> to HBM. 22: On chip, compute **dK**<sup>˜</sup> _𝑗_ ← **dK**<sup>˜</sup> _𝑗_ + _𝜏_ **dS**<sup>⊤</sup> _𝑖𝑗_<sup>**Q**</sup><sup>_𝑖_∈R</sup><sup>_𝐵𝑐_×</sup><sup>_𝑑_.</sup> 23: **end for** ˜ ˜ 24: Write **dK** _𝑗_ ← **dK** _𝑗 ,_ **dV** _𝑗_ ← **dV** _𝑗_ to HBM. 25: **end for** 

- 26: Return **dQ** _,_ **dK** _,_ **dV** . 

We see that similar to the forward pass, the backward pass performs _𝑂_ ( _𝑁_<sup>2</sup> ) FLOPs and only requires _𝑂_ ( _𝑁_ ) extra memory beyond inputs, output, output gradient, and input gradients. 

We analyze the IO-complexity of the backward pass, similar to the forward pass (Theorem 2). 

**Theorem 5.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) backward pass requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _backward pass (Algorithm 4) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

The proof is in Appendix C. 

21

---

[referencia=9cb658eb63c3853b score=0.760]
## **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=9cb658eb63c3853b score=0.755]
The main idea of the proof is that given the SRAM size of _𝑀_ , we can load blocks of **K** _,_ **V** of size Θ( _𝑀_ ) each (Algorithm 1 line 6). For each block of **K** and **V** , we iterate over all blocks of **Q** (Algorithm 1 line 8) to compute the intermediate values, resulting in Θ( _𝑁𝑑𝑀_<sup>−1</sup> ) passes over **Q** . Each pass loads Θ( _𝑁𝑑_ ) elements, which amounts to Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses. We similarly prove that the backward pass of standard attention requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). 

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention. 

**Proposition 3.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. There does not exist an algorithm to compute exact attention with 𝑜_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses for all 𝑀 in the range_ [ _𝑑, 𝑁𝑑_ ] _._

---

[referencia=9cb658eb63c3853b score=0.722]
### **B.4 FlashAttention: Backward Pass** 

We describe the full details of FlashAttention backward pass. Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , the output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , and the output gradient **dO** , we want to compute the input gradients **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> . We first describe the standard attention backward pass in Algorithm 3 for completeness. 

**Algorithm 3** Standard Attention Backward Pass 

**Require:** Matrices **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , **P** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> in HBM.

---

[referencia=9cb658eb63c3853b score=0.667]
- 6: Return **dQ** _,_ **dK** _,_ **dV** . 

We now make two observations about FlashAttention backward pass: 

1. We do not need to store the dropout mask of size _𝑂_ ( _𝑁_<sup>2</sup> ) from the forward pass. Instead, we can save the pseudo-random number generator states from the forward pass and re-generate the dropout mask in the backward pass. This allows us to only use _𝑂_ ( _𝑁_ ) extra memory. 

2. When computing the softmax gradient, we use Eq. (4) to compute _𝐷𝑖_ = _𝑃𝑖_<sup>⊤</sup> :<sup>_𝑑𝑃𝑖_:withoutreducingover</sup> _𝑃𝑖_ : and _𝑑𝑃𝑖_ : of size _𝑁_ (they might not fit into SRAM). Instead we can rewrite _𝐷𝑖_ = _𝑑𝑜_<sup>⊤</sup> _𝑖_<sup>_𝑜𝑖_andcompute</sup> the dot product between vectors of size _𝑑_ . 

20 

The full FlashAttention backward pass algorithm is in Algorithm 4. Conceptually it is just a block version of the derivation in Appendix B.2. 

**Algorithm 4** FlashAttention Backward Pass

---

[referencia=9cb658eb63c3853b score=0.657]
### **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

---

[referencia=9cb658eb63c3853b score=0.620]
|**FlashAttention**|**0.04**|0.06|0.21|0.82|2.85|10.41|41.74|167.19|670.76|2682.35|
|**Block-Sparse FlashAttention**|0.06|**0.06**|**0.06**|**0.12**|**0.44**|**0.86**|**1.70**|**3.29**|**6.55**|**13.34**|



We report timing results on the forward pass, backward pass, and combined forward + backward pass. We measure each method with and without dropout, masking, or both—except for Block Sparse, Longformer, and BigBird. These methods did not successfully run the backward pass with masking due to a bug in external libraries, so we measured them without masking to be generous. We use FP16 for all measurements, except for Local Attention, whose implementation only supports FP32. 

For each baseline, we increase sequence length until it runs out of memory on the GPU, except for the following exceptions: The Megatron implementation does not support sequence lengths longer than 2048. Block-Sparse (OpenAI) does not support sequence lengths longer than 4096. Longformer and BigBird do not support sequence lengths longer than 8092. 

We measure memory usage on the combined forward + backward pass, without dropout or masking. 

**Results** Table 8 summarizes all the experimental configurations and contains pointers to the results tables. 

31 

Table 10: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.606]
asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

---

[referencia=9cb658eb63c3853b score=0.561]
- 1: Load **P** _,_ **dO** by blocks from HBM, compute **dV** = **P**<sup>⊤</sup> **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , write **dV** to HBM. 

- 2: Load **dO** _,_ **V** by blocks from HBM, compute **dP** = **dOV**<sup>⊤</sup> ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> , write **dP** to HBM. 

- 3: Read **P** _,_ **dP** from HBM, compute **dS** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> where _𝑑𝑆𝑖𝑗_ = _𝑃𝑖𝑗_ ( _𝑑𝑃𝑖𝑗_ −<sup>�</sup> _𝑙_<sup>_𝑃_</sup> _𝑖𝑙_<sup>_𝑑𝑃_</sup> _𝑖𝑙_<sup>),write</sup><sup>**dS**toHBM.</sup> 

- 4: Load **dS** and **K** by blocks from HBM, compute **dQ** = **dSK** , write **dQ** to HBM. 

- 5: Load **dS** and **Q** by blocks from HBM, compute **dK** = **dS**<sup>⊤</sup> **Q** , write **dK** to HBM. 

- 6: Return **dQ** _,_ **dK** _,_ **dV** . 

We now make two observations about FlashAttention backward pass:

---

[referencia=9cb658eb63c3853b score=0.556]
The proof relies on the fact that for _𝑀_ = Θ( _𝑁𝑑_ ) any algorithm must perform Ω( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) = Ω( _𝑁𝑑_ ) HBM accesses. This type of lower bound over a subrange of _𝑀_ is common in the streaming algorithms literature [88]. We leave proving parameterized complexity [27] lower bounds in terms of _𝑀_ as exciting future work. 

We validate that the number of HBM accesses is the main determining factor of attention run-time. In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size _𝐵𝑐_ of FlashAttention, which results in different amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number of HBM accesses decreases (as we make fewer passes over the input), and runtime decreases. For large enough block size (beyond 256), the runtime is then bottlenecked by other factors (e.g., arithmetic operations). Moreover, larger block size will not fit into the small SRAM size.

---

[referencia=9cb658eb63c3853b score=0.545]
In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses: 



However, the input to attention (matrices **Q** _,_ **K** _,_ **V** ) and the output **O** have size _𝑁𝑑_ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least Ω( _𝑁𝑑_ ) HBM accesses. This is a contradiction. □ 

_Proof of Theorem 5._ The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). Here we provide a sketch of the proof. 

We first analyze the IO complexity of standard attention backward pass. The inputs **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the outputs **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> are written to HBM. 

At each step of the standard attention backward pass, one needs to load inputs of size _𝑁𝑑_ or _𝑁_<sup>2</sup> from HBM, and needs to write the outputs of size _𝑁_<sup>2</sup> or _𝑁𝑑_ to HBM. This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

We now analyze the IO complexity of FlashAttention backward pass.

---

[referencia=9cb658eb63c3853b score=0.530]
### **B.2 Memory-efficient backward pass** 

We derive the backward pass of attention and show that it can also be computed with linear memory. Rabe and Staats [66] suggests that the backward pass can be done without quadratic extra memory by applying gradient checkpointing to the memory-efficient forward pass. We instead derive the backward pass explicitly and show how it can be computed in a memory-efficient manner. 

Suppose that there is a scalar loss function _𝜙_ , and let the output gradient be **dO** ∈ R<sup>_𝑛_×</sup><sup>_𝑑_</sup> (where **dO** denotes _𝜕𝜙_<sup>Wewanttocomputetheinputgradients</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**∈R</sup><sup>_𝑛_×</sup><sup>_𝑑_(where</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**denote</sup><sup>_𝜕𝜙𝜕𝜙𝜕𝜙_</sup> _𝜕_ **O**<sup>).</sup> _𝜕_ **Q**<sup>_,_</sup> _𝜕_ **K**<sup>_,_</sup> _𝜕_ **V** respectively). 

The gradient **dV** is easy to see. Applying reverse-mode autodiff by hand (aka the chain rule), we obtain (in matrix notation) **dV** = **P**<sup>_𝑇_</sup> **dO** . Thus: 



Since we already computed _𝐿𝑖_ , _𝑑𝑣 𝑗_ can be computed without extra memory by repeated summing. 

The gradients **dQ** and **dK** are a little more complicated. We go through the gradients **dP** and **dS** first. From Eq. (2), we have that **dP** = **dOV**<sup>_𝑇_</sup> , and so:

---

[referencia=9cb658eb63c3853b score=0.491]
|**Block-Sparse FlashAttention**|0.22|0.22|**0.26**|**0.57**|**1.55**|**3.13**|**5.98**|**12.21**|**23.49**|**47.85**|



32 

Table 14: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.476]
|**Block-Sparse FlashAttention**|**0.30**|0.27|**0.29**|**0.59**|**1.50**|**2.94**|**5.82**|**11.85**|**23.98**|**47.61**|



Table 11: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.466]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.465]
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|
|**Block-Sparse FlashAttention**|0.11|**0.12**|**0.16**|**0.38**|**1.20**|**2.34**|**4.69**|**9.10**|**18.74**|**37.04**|



Table 20: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.457]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->