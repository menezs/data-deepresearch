[referencia=5727fed78bddc701 score=0.204]
# **C Proofs** 

_Proof of Theorem 1._ We first count the number of FLOPs and extra memory required. 

The dominating FLOPs are from matrix multiplication. In the inner loop, (Algorithm 1 line 9), we compute **Q** _𝑖_ **K**<sup>⊤</sup> _𝑗_<sup>∈R</sup><sup>_𝐵𝑟_×</sup><sup>_𝐵𝑐_for</sup><sup>**Q**</sup><sup>_𝑖_∈R</sup><sup>_𝐵𝑟_×</sup><sup>_𝑑_and</sup><sup>**K**</sup><sup>_𝑗_∈R</sup><sup>_𝐵𝑐_×</sup><sup>_𝑑_,whichtakes</sup><sup>_𝑂_(</sup><sup>_𝐵𝑟𝐵𝑐𝑑_)FLOPs.Wealsocompute</sup> (Algorithm 1 line 12) **P**<sup>˜</sup> _𝑖𝑗_ **V** _𝑗_ ∈ R<sup>_𝐵𝑟_×</sup><sup>_𝑑_</sup> for **P**<sup>˜</sup> _𝑖𝑗_ ∈ R<sup>_𝐵𝑟_×</sup><sup>_𝐵𝑐_</sup> and **V** _𝑗_ ∈ R<sup>_𝐵𝑐_×</sup><sup>_𝑑_</sup> , which takes _𝑂_ ( _𝐵𝑟 𝐵𝑐 𝑑_ ) FLOPs. We execute the inner loops _𝑇𝑐𝑇𝑟_ = � _𝐵𝑁𝑐_ �� _𝐵𝑁𝑟_ � times. Therefore the total number of FLOPs is 



In terms of extra memory required, we see that we need _𝑂_ ( _𝑁_ ) memory to store the statistics ( _ℓ, 𝑚_ ).

---

[referencia=5727fed78bddc701 score=0.130]
For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3. 

The main idea of the proof is that given the SRAM size of _𝑀_ , we can load blocks of **K** _,_ **V** of size Θ( _𝑀_ ) each (Algorithm 1 line 6). For each block of **K** and **V** , we iterate over all blocks of **Q** (Algorithm 1 line 8) to compute the intermediate values, resulting in Θ( _𝑁𝑑𝑀_<sup>−1</sup> ) passes over **Q** . Each pass loads Θ( _𝑁𝑑_ ) elements, which amounts to Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses. We similarly prove that the backward pass of standard attention requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). 

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention.

---

[referencia=5727fed78bddc701 score=0.109]
We then see that the claim is also true for _𝑗_ + 1. By induction, the claim is true for all _𝑗_ = 0 _, . . . ,𝑇𝑐_ . When _𝑗_ = _𝑇𝑐_ , we conclude that the final value of **O** in HBM is softmax( **S** ) **V** = softmax( **QK**<sup>⊤</sup> ) **V** . 

_Proof of Theorem 2._ We first analyze the IO complexity of standard attention implementation. The inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> is written to HBM. In the first step of computing the matrix multiply **S** = **QK**<sup>⊤</sup> , the inputs **Q** _,_ **K** are read from HBM and the output **S** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> is written to HBM (Algorithm 0 line 1). This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

In the second step of computing **P** = softmax( **S** ), the input **S** is read from HBM and the output **P** is written to HBM (Algorithm 0 line 2). This incurs Θ( _𝑁_<sup>2</sup> ) HBM accesses. 

In the last step of computing **O** = **PV** , the inputs **P** _,_ **V** are read from global memory and the output **O** is written to HBM (Algorithm 0 line 3). This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses.

---

[referencia=5727fed78bddc701 score=0.105]
|However, by storing the output **O** and the softmax normalization statistics (_𝑚, ℓ_), we can recompute the<br>attention matrix **S** and **P** easily in the backward pass from blocks of **Q**_,_**K**_,_**V** in SRAM. This can be seen as a<br>form of selective gradient checkpointing [10, 34]. While gradient checkpointing has been suggested to reduce<br>the maximum amount of memory required [66], all implementations (that we know of) have to trade speed|



for memory. In contrast, even with more FLOPs, our recomputation speeds up the backward pass due to reduced HBM accesses (Fig. 2). The full backward pass description is in Appendix B. 

**Implementation details: Kernel fusion.** Tiling enables us to implement our algorithm in one CUDA kernel, loading input from HBM, performing all the computation steps (matrix multiply, softmax, 

optionally masking and dropout, matrix multiply), then write the result back to HBM (masking and dropout in Appendix B). This avoids repeatedly reading and writing of inputs and outputs from and to HBM. **Algorithm 1** FlashAttention **Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, on-chip SRAM of size _𝑀_ . 1: Set block sizes _𝐵𝑐_ = � 4 _<u>𝑀𝑑</u>_ � _, 𝐵𝑟_ = min<sup>��</sup> 4<sup>_<u>𝑀</u>_</sup> _𝑑_ � _, 𝑑_<sup>�</sup> . 

2: Initialize **O** = (0) _𝑁_ × _𝑑_ ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> _, ℓ_ = (0) _𝑁_ ∈ R<sup>_𝑁_</sup> _, 𝑚_ = (−∞) _𝑁_ ∈ R<sup>_𝑁_</sup> in HBM.

---

[referencia=5727fed78bddc701 score=0.093]
## **D.2 Potential Extensions** 

We discuss here a few potential extensions of the IO-aware approach to speed up deep learning training. **Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other 

25 

GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. 

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. We believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. We are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime. 

**Kernel machine learning.** Our approach in FlashAttention relies on the fact that the _𝑁_ × _𝑁_ attention matrix is a function of a low-rank matrix **QK**<sup>⊤</sup> (of rank _𝑑_ ≪ _𝑁_ ). As a result, we can repeatedly load the inputs **Q** _,_ **K** and recompute the block of the attention matrix that we need, significantly reducing HBM access. As similar scenario happens in kernel machine learning: each element _𝐾𝑖𝑗_ of the _𝑁_ × _𝑁_ kernel matrix **K** is a function of two vectors of size _𝑑_ ≪ _𝑁_ , as it measures the similarity between two datapoints _𝑥𝑖_ and _𝑥 𝑗_ . The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. We hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs.

---

[referencia=5727fed78bddc701 score=0.089]
## **2.2 Standard Attention Implementation** 

Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> where _𝑁_ is the sequence length and _𝑑_ is the head dimension, we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



where softmax is applied row-wise. 

Standard attention implementations materialize the matrices **S** and **P** to HBM, which takes _𝑂_ ( _𝑁_<sup>2</sup> ) memory. Often _𝑁_ ≫ _𝑑_ (e.g., for GPT2, _𝑁_ = 1024 and _𝑑_ = 64). We describe the standard attention implementation in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time. 

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to **S** or dropout applied to **P** . As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax [77]. 

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length _𝑁_ . We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention). 

**Algorithm 0** Standard Attention Implementation 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM.

---

[referencia=5727fed78bddc701 score=0.083]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.082]
## **B.1 Memory-efficient forward pass** 

The main challenge in making attention memory-efficient is the softmax that couples the columns of **K** (and columns of **V** ). Our approach is to compute the softmax normalization constant separately to decouple the columns. This technique [60] has been used in the literature [51, 66] to show that attention computation does not need quadratic _extra_ memory (though the number of HBM accesses is still quadratic, resulting in slow run-time). 

For simplicity, we omit here the max-shifting step during softmax. The full algorithm in Appendix B.3 contains all the steps. 

Recall that given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



We have that _𝑆𝑖𝑗_ = _𝑞_<sup>_𝑇_</sup> _𝑖_<sup>_𝑘𝑗_where</sup><sup>_𝑞𝑖_and</sup><sup>_𝑘𝑗_arethe</sup><sup>_𝑖_-thand</sup><sup>_𝑗_-thcolumnsof</sup><sup>**Q**and</sup><sup>**K**respectively.Define</sup> the normalization constants of softmax: 



Let _𝑣 𝑗_ be the _𝑗_ -th column of **V** , then the _𝑖_ -th columns of the output is 



We see that once _𝐿𝑖_ is computed, we can compute _𝑜𝑖_ without extra memory by repeatedly summing _<u>𝑒</u>_<sup>_𝑞𝑇_</sup> _𝑖_<sup>_𝑘𝑗_</sup> _𝐿𝑖 𝑣 𝑗_ . Therefore the forward pass can be computed with _𝑂_ ( _𝑛_ ) extra memory:

---

[referencia=5727fed78bddc701 score=0.060]
# **3 FlashAttention: Algorithm, Analysis, and Extensions** 

We show how to compute exact attention with fewer HBM reads/writes and without storing large intermediate matrices for the backward pass. This yields an attention algorithm that is both memory efficient and faster in wall-clock time. We analyze its IO complexity, showing that our method requires much fewer HBM accesses compared to standard attention. We further show that FlashAttention can serve as a useful primitive by extending it to handle block-sparse attention. 

We focus here on the forward pass for ease of exposition; Appendix B contains details for the backward.

---

[referencia=5727fed78bddc701 score=0.053]
### _arithmetic intensity_ [85], which is the number of arithmetic operations per byte of memory access. 

1. Compute-bound: the time taken by the operation is determined by how many arithmetic operations there 

are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels. 

2. Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm). 

**Kernel fusion.** The most common approach to accelerate memory-bound operations is kernel fusion: if there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations [53, 65, 75]. 

> 1FlashAttention code is available at `https://github.com/HazyResearch/flash-attention` 

3 

However, in the context of model training, the intermediate values still need to be written to HBM to save for the backward pass, reducing the effectiveness of naive kernel fusion.

---

[referencia=5727fed78bddc701 score=0.047]
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

[referencia=a7468c6851652691 score=0.033]
### **3.2 Attention** 

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum 

3 

Scaled Dot-Product Attention 





Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. 

of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. 

### **3.2.1 Scaled Dot-Product Attention** 

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension _dk_ , and values of dimension _dv_ . We compute the dot products of the query with all keys, divide each by<sup>_√_</sup> _dk_ , and apply a softmax function to obtain the weights on the values. 

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix _Q_ . The keys and values are also packed together into matrices _K_ and _V_ . We compute the matrix of outputs as: 



The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

While for small values of _dk_ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of _dk_ [3]. We suspect that for large values of _dk_ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup> . To counteract this effect, we scale the dot products by _~~√~~_ <u>1</u> _dk_<sup>.</sup>

---

[referencia=5727fed78bddc701 score=0.028]
|**Block-Sparse FlashAttention**|0.74|0.77|0.82|**0.88**|**1.71**|**3.21**|**6.56**|**12.60**|**24.93**|**50.39**|



Table 21: Memory usage (MB) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.024]
6 

|Given a predefned block sparsity mask **M** ∈{0_,_1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup>we can easily adapt Algorithm 1 to only<br>compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we<br>skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.<br>We also analyze the IO complexity of block-sparse FlashAttention.|
|---|
|**Proposition 4.** _Let 𝑁be the sequence length, 𝑑be the head dimension, and 𝑀be size of SRAM with_<br>_𝑑_≤_𝑀_≤_𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ(_𝑁𝑑_+_𝑁_<sup>2</sup>_𝑑_<sup>2</sup>_𝑀_<sup>−1</sup>_𝑠_) _HBM accesses_<br>_where 𝑠is the fraction of nonzero blocks in the block-sparsity mask._|
|We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the<br>IO complexity. For large sequence lengths _𝑁_, _𝑠_is often set to _𝑁_<sup>−1/2 </sup>[11] or _𝑁_<sup>−1 </sup>log_𝑁_[3, 17, 92], resulting<br>in Θ(_𝑁_<br>√<br>_𝑁_) or Θ(_𝑁_log_𝑁_) IO complexity. For downstream experiments, we use the fxed butterfy sparsity<br>pattern [17], which has been shown to be able to approximate arbitrary sparsity [16].<br>In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention<br>improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup,|



while performing on par with standard attention (Section 4). 

**4 Experiments**

---

[referencia=5727fed78bddc701 score=0.024]
**Sparse Training.** Our block-sparse FlashAttention can be seen as a step towards making sparse model training more efficient. Sparse models have seen success in compressing models for inference (pruning) by sparsifying the weight matrices [23, 38, 39, 55, 76]. For model training, the lottery tickets hypothesis [28, 29, 30] suggests that there are a set of small sub-networks derived from a larger dense network that performs as well as the original dense network. Out block-sparse FlashAttention can also be seen as a fixed lottery ticket in the context of attention: we fix the sparsity pattern to be the butterfly pattern through training, and observe that it performs almost as well as the (dense) FlashAttention on the Long-range Arena tasks. 

**Efficient Transformer.** Transformer-based models have become the most widely-used architecture in natural language processing [22] and computer vision [24, 91]. However, one of their computational bottlenecks is that their time and memory scales quadratic in the sequence length. There are numerous approaches to overcome this bottleneck, including approximation with hashing (i.e., sparse) such as Reformer [51] and Smyrf [19] and with low-rank approximation such as Performer [12, 54]. One can even combine sparse and low-rank approximation for better accuracy (e.g., Longformer [3], BigBird [92], Scatterbrain [9], Long-short transformer [94], Combiner [73]). Other approaches include compressing along the sequence dimension to attend to multiple tokens at once [52, 57, 79, 89]. One can also attend over the states from previous sequences to help lengthen the context (e.g., Transformer-XL [14] and Compressive Transformer [69]). We recommend the survey [81] for more details. 

There are several lines of work on developing other modules instead of attention to model longer context. HiPPO [35] and its extensions, most notably S4 [31, 36, 37] projects the history on a polynomial basis, allowing accurate reconstruction of the history through state-space models. They combine the strengths of CNNs (efficient training), RNNs (efficient inference), and continuous models (robust to change in sampling rates). LambdaNetworks [2], AFT [93] and FLASH [42] are other attempts at replacing attention in the context of image classification and language modeling.

---

[referencia=a7468c6851652691 score=0.023]
### **3.2.2 Multi-Head Attention** 

Instead of performing a single attention function with _d_ model-dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values _h_ times with different, learned linear projections to _dk_ , _dk_ and _dv_ dimensions, respectively. On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding _dv_ -dimensional 

> 4To illustrate why the dot products get large, assume that the components of _q_ and _k_ are independent random variables with mean 0 and variance 1. Then their dot product, _q · k_ =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_kqiki_, has mean 0 and variance</sup><sup>_dk_.</sup> 

4 

output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2. 

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this. 

MultiHead( _Q, K, V_ ) = Concat(head1 _, ...,_ headh) _W_<sup>_O_</sup> 



Where the projections are parameter matrices _Wi_<sup>_Q_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_K_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_V_</sup> _∈_ R<sup>_d_model</sup><sup>_×dv_</sup> and _W_<sup>_O_</sup> _∈_ R<sup>_hdv×d_model</sup> . 

In this work we employ _h_ = 8 parallel attention layers, or heads. For each of these we use _dk_ = _dv_ = _d_ model _/h_ = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.

---

[referencia=5727fed78bddc701 score=0.020]
## **3.3 Extension: Block-Sparse FlashAttention** 

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity. Given inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and a mask matrix **M**<sup>˜</sup> ∈{0 _,_ 1}<sup>_𝑁_×</sup><sup>_𝑁_</sup> , we want to compute: 



where ( **S** ⊙ 𝟙 **M** ˜ ) _𝑘𝑙_ = **S** _𝑘𝑙_ if **M**<sup>˜</sup> _𝑘𝑙_ = 1 and −∞ if **M** _𝑘𝑙_ = 0. We require **M**<sup>˜</sup> to have block form: for some block sizes _𝐵𝑟 , 𝐵𝑐_ , for all _𝑘, 𝑙_ , **M**<sup>˜</sup> _𝑘,𝑙_ = **M** _𝑖𝑗_ with _𝑖_ = ⌊ _𝑘_ / _𝐵𝑟_ ⌋ _, 𝑗_ = ⌊ _𝑙_ / _𝐵𝑐_ ⌋ for some **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> . 

6

---

[referencia=5727fed78bddc701 score=0.020]
We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention. 

**Proposition 3.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. There does not exist an algorithm to compute exact attention with 𝑜_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses for all 𝑀 in the range_ [ _𝑑, 𝑁𝑑_ ] _._ 

The proof relies on the fact that for _𝑀_ = Θ( _𝑁𝑑_ ) any algorithm must perform Ω( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) = Ω( _𝑁𝑑_ ) HBM accesses. This type of lower bound over a subrange of _𝑀_ is common in the streaming algorithms literature [88]. We leave proving parameterized complexity [27] lower bounds in terms of _𝑀_ as exciting future work. 

We validate that the number of HBM accesses is the main determining factor of attention run-time. In Fig. 2 (left), we see that even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime. In Fig. 2 (middle), we vary the block size _𝐵𝑐_ of FlashAttention, which results in different amounts of HBM accesses, and measure the runtime of the forward pass. As block size increases, the number of HBM accesses decreases (as we make fewer passes over the input), and runtime decreases. For large enough block size (beyond 256), the runtime is then bottlenecked by other factors (e.g., arithmetic operations). Moreover, larger block size will not fit into the small SRAM size.

---

[referencia=5727fed78bddc701 score=0.018]
## **B.2 Memory-efficient backward pass** 

We derive the backward pass of attention and show that it can also be computed with linear memory. Rabe and Staats [66] suggests that the backward pass can be done without quadratic extra memory by applying gradient checkpointing to the memory-efficient forward pass. We instead derive the backward pass explicitly and show how it can be computed in a memory-efficient manner. 

Suppose that there is a scalar loss function _𝜙_ , and let the output gradient be **dO** ∈ R<sup>_𝑛_×</sup><sup>_𝑑_</sup> (where **dO** denotes _𝜕𝜙_<sup>Wewanttocomputetheinputgradients</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**∈R</sup><sup>_𝑛_×</sup><sup>_𝑑_(where</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**denote</sup><sup>_𝜕𝜙𝜕𝜙𝜕𝜙_</sup> _𝜕_ **O**<sup>).</sup> _𝜕_ **Q**<sup>_,_</sup> _𝜕_ **K**<sup>_,_</sup> _𝜕_ **V** respectively). 

The gradient **dV** is easy to see. Applying reverse-mode autodiff by hand (aka the chain rule), we obtain (in matrix notation) **dV** = **P**<sup>_𝑇_</sup> **dO** . Thus: 



Since we already computed _𝐿𝑖_ , _𝑑𝑣 𝑗_ can be computed without extra memory by repeated summing. 

The gradients **dQ** and **dK** are a little more complicated. We go through the gradients **dP** and **dS** first. From Eq. (2), we have that **dP** = **dOV**<sup>_𝑇_</sup> , and so:

---

[referencia=5727fed78bddc701 score=0.018]
# **5 Limitations and Future Directions** 

We discuss limitations of our approach and future directions. Related work is given in Appendix A. 

**Compiling to CUDA.** Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA—similar to efforts such as Halide in image processing [70]. 

**IO-Aware Deep Learning.** We believe that the IO-aware approach can extend beyond attention. Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. We hope our work inspires IO-aware implementations of additional modules. We discuss these potential extensions in Appendix D. 

**Multi-GPU IO-Aware Methods.** Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs [72]. Using multiple GPUs adds an additional layer to IO analysis—accounting for data transfer between GPUs. We hope our work inspires future work in this direction.