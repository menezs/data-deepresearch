[referencia=4791e267352f48bb score=0.999]
# Fast and Accurate Attention with Asynchrony and Low-precision 

Jay Shah<sup>∗1</sup> , Ganesh Bikshandi<sup>∗1</sup> , Ying Zhang2, Vijay Thakkar3 _,_ 4, Pradeep Ramani3, and Tri Dao5 _,_ 6 

> 1Colfax Research 2Meta 3NVIDIA 4Georgia Tech 5Princeton University 6Together AI `{jayhshah,ganesh}@colfax-intl.com` , `yingz@meta.com` , `{vithakkar,prraman}@nvidia.com` , `tri@tridao.me` 

July 16, 2024 

##### **Abstract** 

Attention, as a core layer of the ubiquitous Transformer architecture, is the bottleneck for large language models and long-context applications. FlashAttention elaborated an approach to speed up attention on GPUs through minimizing memory reads/writes. However, it has yet to take advantage of new capabilities present in recent hardware, with FlashAttention-2 achieving only 35% utilization on the H100 GPU. We develop three main techniques to speed up attention on Hopper GPUs: exploiting asynchrony of the Tensor Cores and TMA to (1) overlap overall computation and data movement via warp-specialization and (2) interleave block-wise matmul and softmax operations, and (3) block quantization and incoherent processing that leverages hardware support for FP8 low-precision. We demonstrate that our method, FlashAttention-3, achieves speedup on H100 GPUs by 1.5-2.0× with FP16 reaching up to 740 TFLOPs/s (75% utilization), and with FP8 reaching close to 1.2 PFLOPs/s. We validate that FP8 FlashAttention-3 achieves 2.6× lower numerical error than a baseline FP8 attention.

---

[referencia=4791e267352f48bb score=0.996]
## **5 Dicussion, Limitations, Conclusion** 

With FlashAttention-3, we have demonstrated that new programming techniques and hardware features such as asynchrony and low-precision can have a dramatic impact on the efficiency and accuracy of attention. We are able to speed up attention by 1.5-2.0× times compared to FlashAttention-2, and reduce FP8 numerical error by 2.6× compared to standard per-tensor quantization. Some limitations of our work that we hope to address in the future include: optimizing for LLM inference, integrating a persistent kernel design into the FP8 kernel,<sup>10</sup> and understanding the effects of low-precision attention in large-scale training. Though we have focused on Hopper GPUs in this work, we expect that the techniques developed here will apply to other hardware accelerators. We hope that a faster and more accurate primitive such as attention will unlock new applications in long-context tasks. 

#### **Acknowledgments** 

We are grateful to the NVIDIA CUTLASS team (especially Haicheng Wu, Aniket Shivam, and Cris Cecka) for helping us understand Hopper’s programming model and for their library, which provides clean and powerful building blocks for the implementation of FlashAttention-3. We thank the cuDNN team for the idea of in-kernel transpose for FP8. The idea of overlapping GEMMs and softmax was inspired by insightful conversations with Christopher Ré, Benjamin Spector, Aniket Shivam, and Markus Hoehnerbach. The pingpong scheduling is adapted from the warp-specialized pingpong GEMM implementation in CUTLASS. We appreciate Driss Guessous for integrating FlashAttention to PyTorch. FlashAttention-3 has benefited from helpful discussions with Horace He on different attention variants, with Hao Liu and Phil Wang on distributed attention, and with Daniel Haziza and Chris De Sa on quantization. We thank Meta, Together AI, and Princeton Language and Intelligence (PLI) for compute support.

---

[referencia=4791e267352f48bb score=0.995]
## **4 Empirical Validation** 

We use the primitives from CUTLASS [57] such as WGMMA and TMA abstractions to implement FlashAttention3 and evaluate its efficiency and accuracy. 

- **Benchmarking attention.** We measure the runtime of FlashAttention-3 across different sequence lengths and compare it to a standard implementation in PyTorch, FlashAttention-2, FlashAttention-2 in Triton (which uses H100-specific instructions), as well as a vendor’s implementation of FlashAttention-2 optimized for H100 GPUs from cuDNN. We confirm that FlashAttention-3 is up to 2.0× faster than FlashAttention-2 and 1.5× faster than FlashAttention-2 in Triton. FlashAttention-3 reaches up to 740 TFLOPs/s, 75% of the theoretical maximum TFLOPs/s on H100 GPUs. 

- **Ablation study.** We confirm that our algorithmic improvements with warp-specialization and GEMM-softmax pipelining contribute to the speedup of FlashAttention-3. 

- **Accuracy of FP8 attention.** We validate that block quantization and incoherent processing reduces the numerical error of FP8 FlashAttention-3 by 2.6×.

---

[referencia=4791e267352f48bb score=0.993]
#### N (0 _,_ 1) + N (0 _,_ 100) · Bernoulli(0 _._ 001) _._ 

That is, each entry is normally distributed with zero mean and standard deviation 1, but for 0.1% of entries we add an independent term that’s normally distributed with standard deviation 10. We then measure the root mean squared error (RMSE) in Table 3. In FP16, both FlashAttention-2 and FlashAttention-3 achieves 1.7× lower RMSE compared to the standard implementation since intermediate results (softmax) are kept in FP32. The baseline attention in FP8 uses per-tensor scaling, with matmul accumulator in FP32 and intermediate softmax results kept in FP16. Thanks to block quantization and incoherent processing, FlashAttention-3 in FP8 is 2.6× more accurate than this baseline. 

11 

Table 3: Numerical error comparisons in FP16 and FP8 (e4m3). 

||Method|Baseline FP16|FlashAttention-2 FP16<br>Flash|Attention-3 FP16|
|---|---|---|---|---|
||RMSE|3.2e-4|**1.9e-4**|**1.9e-4**|
|Method|Basel|ine FP8<br>Flash|Attention-3 FP8<br>No block quant|No incoherent processing|
|RMSE|2.|4e-2|**9.1e-3**<br>9.3e-3|2.4e-2|

---

[referencia=4791e267352f48bb score=0.986]
To validate our method empirically, we benchmark FlashAttention-3 on the H100 SXM5 GPU over a range of parameters and show that (1) FP16 achieves 1.5-2.0× speedup over FlashAttention-2 in the forward pass (reaching up to 740 TFLOPs/s) and 1.5-1.75× in the backward pass, (2) FP8 achieves close to 1.2 PFLOPs/s, and (3) for large sequence length, FP16 outperforms and FP8 is competitive<sup>2</sup> with a state-of-the-art implementation of attention from NVIDIA’s cuDNN library. We also validate that FP16 FlashAttention-3 yields the same numerical error as FlashAttention-2 and is better than the standard attention implementation as intermediate results (e.g., softmax rescaling) are kept in FP32. Moreover, FP8 FlashAttention-3 with block quantization and incoherent processing is 2.6× more accurate than standard attention with per-tensor quantization in cases with outlier features. 

We open-source FlashAttention-3 with a permissive license<sup>3</sup> and plan to integrate it with PyTorch and Hugging Face libraries to benefit the largest number of researchers and developers.

---

[referencia=4791e267352f48bb score=0.973]
To this end, we propose FlashAttention-3, which contributes and synthesizes three new ideas to further improve performance on newer GPU architectures:<sup>1</sup> 

1. **Producer-Consumer asynchrony:** We define a warp-specialized software pipelining scheme that exploits the asynchronous execution of data movement and Tensor Cores by splitting producers and consumers of data into separate warps, thereby extending the algorithm’s ability to hide memory and instruction issue latencies. 

2. **Hiding softmax under asynchronous block-wise GEMMs:** We overlap the comparatively low-throughput non-GEMM operations involved in softmax, such as floating point multiply-add and exponential, with the asynchronous WGMMA instructions for GEMM. As part of this, we rework the FlashAttention-2 algorithm to circumvent certain sequential dependencies between softmax and the GEMMs. For example, in the 2-stage version of our algorithm, while softmax executes on one block of the scores matrix, WGMMA executes in the asynchronous proxy to compute the next block. 

3. **Hardware-accelerated low-precision GEMM:** We adapt the forward pass algorithm to allow for targeting the FP8 Tensor Cores for GEMM, nearly doubling the measured TFLOPs/s. This requires bridging the different layout conformance requirements of WGMMA in terms of how blocks of FP32 accumulator and FP8 operand matrices are assumed to be laid out in memory. We use the techniques of block quantization and incoherent processing to mitigate the loss of accuracy that results from moving to FP8 precision.

---

[referencia=4791e267352f48bb score=0.956]
> ∗Equal contribution 

1 

More fundamentally, FlashAttention-2’s algorithm adheres to a simplified synchronous model and makes no explicit use of asynchrony and low-precision in its design. Asynchrony is a result of hardware specialization to accelerate the most important operations in a ML workload: specific hardware units performing matrix multiplication (Tensor Cores) or memory loading (Tensor Memory Accelerator – TMA), separate from the rest of the CUDA cores performing logic, integer, and floating point computation. Low precision such as FP8 in Hopper and FP4 in Blackwell, continuing the trend of FP16 (Pascal in 2017) and BF16 (Ampere in 2020), is a proven technique to get double or quadruple throughput for the same power and chip area. We review the capabilities afforded by Hopper in these directions in §2.2. The technical challenge is to redesign FlashAttention-2 to make use of these hardware features: asynchrony requires overlapping computation between matmul and softmax even though one depends on the output of the other, and low-precision requires care to minimize quantization error, especially in the case of outlier features in LLMs [20, 54]. 

To this end, we propose FlashAttention-3, which contributes and synthesizes three new ideas to further improve performance on newer GPU architectures:<sup>1</sup>

---

[referencia=4791e267352f48bb score=0.949]
### **2.1 Multi-Head Attention** 

Let **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> be the query, key and value input sequences associated to a single head, where _𝑁_ is the sequence length and _𝑑_ is the head dimension. Then the attention output **O** is computed as: 

**S** = _𝛼_ **QK**<sup>⊤</sup> ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> _,_ **P** = softmax( **S** ) ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> _,_ **O** = **PV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> _,_ 

> 1We describe our results in the context of NVIDIA’s Hopper architecture. However, our algorithm is operative for any GPU architecture with sufficiently robust asynchronous execution and low-precision capabilities. 

> 2More precisely, for head dimension 64 FlashAttention-3 FP8 is ahead, while for head dimensions 128 and 256 it is at par for those cases without causal masking and behind with causal masking. 

> 3FlashAttention-3 is available at `https://github.com/Dao-AILab/flash-attention` 

2 

where softmax is applied row-wise and one typically sets _𝛼_ = 1/√ _𝑑_ as the scaling factor. In practice, we subtract rowmax( **S** ) from **S** to prevent numerical instability with the exponential function. For multi-head attention (MHA), each head has its own set of query, key and value projections, and this computation parallelizes across multiple heads and batches to produce the full output tensor. 

Now let _𝜙_ be a scalar loss function and let **d** (−) = _𝜕𝜙_ / _𝜕_ (−) be notation for the gradient. Given the output gradient **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we compute **dQ** , **dK** , and **dV** according to the chain rule as follows:

---

[referencia=4791e267352f48bb score=0.929]
#### { `d0 d1 d4 d5 d2 d3 d6 d7` } _,_ 

and this register permutation is then replicated over every 8 bytes. In terms of the logical shape of the **P** tile, this manuever permutes its columns (e.g., columns 0189 now become the first four columns). For WGMMA to then compute the correct output tile, we can correspondingly arrange for the in-kernel transpose to write out a matching row permutation of the **V** tile.<sup>9</sup> 

**Accuracy: block quantization and incoherent processing.** With FP8 (e4m3) format, one only uses 3 bits to store the mantissa and 4 bits for the exponent. This results in higher numerical error than FP16/BF16. Moreover, large models typically have outlier values [20, 54] that are much larger in magnitude than most other values, making quantization difficult. One typically use per-tensor scaling [37] by keeping one scalar per tensor (e.g., one for **Q** , for **K** , and for **V** ). To reduce the numerical error of attention in FP8, we employ two techniques: 

1. **Block quantization** : we keep one scalar per block, so that for each of **Q** , **K** , **V** we split the tensor into blocks of size _𝐵𝑟_ × _𝑑_ or _𝐵𝑐_ × _𝑑_ and quantize them separately. This quantization can be fused with an operation right before attention (e.g., rotary embedding) with no additional slow down (since rotary embedding is memory-bandwidth bound). As the FlashAttention-3 algorithm naturally operates on blocks, we can scale each block of **S** to account for this block quantization at no computation cost. 

> 7An optimized transpose kernel will achieve speed near the bandwidth of the device [46].

---

[referencia=4791e267352f48bb score=0.831]
> 7An optimized transpose kernel will achieve speed near the bandwidth of the device [46]. 

> 8In the PTX documentation, LDSM/STSM are described as copying 8 × 8 matrices with 16-bit entries [40, §9.7.13.4.15-16], but we can pack 8-bit entries two at a time to use LDSM/STSM in the context of FP8 precision. However, the transpose versions of LDSM/STSM cannot split packed 8-bit entries, which necessitates certain register movements in between LDSM and STSM to actually perform a tile-wise transpose; we omit the details. 

> 9This additional freedom afforded by doing the in-kernel transpose eliminates having to use shuffle instructions to change register ownership across threads, which we previously described in [7]. 

8 

2. **Incoherent processing** : to even out outliers, we multiply **Q** and **K** with a random orthogonal matrix **M** before quantizing to FP8. Since **M** is orthogonal, **MM**<sup>⊤</sup> = _𝐼_ and so ( **QM** )( **KM** )<sup>⊤</sup> = **QK**<sup>⊤</sup> , i.e., multiplying both **Q** and **K** with **M** does not change the attention output. This serves to “spread out” the outliers since each entry of **QM** or **KM** is a random sum of entries of **Q** or **K** , thus reducing quantization error. In practice, we follow Chee et al. [9] and Tseng et al. [58] and choose **M** to be the product of random diagonal matrices of ±1 and a Hadamard matrix, which can be multiplied in _𝑂_ ( _𝑑_ log _𝑑_ ) instead of _𝑂_ ( _𝑑_<sup>2</sup> ), and can also be fused with the rotary embedding at no extra computation cost. 

We validate that these two techniques reduces numerical error by up to 2.6× in §4.3.

---

[referencia=4791e267352f48bb score=0.777]
### **4.1 Benchmarking Attention** 

We measure the runtime of different attention methods on an H100 80GB SXM5 GPU for different settings (without / with causal mask, head dimension 64 or 128) for FP16 inputs. We report the results in Fig. 5 and Fig. 6, showing that FlashAttention-3 is around 1.5-2.0× faster than FlashAttention-2 in the forward pass and 1.5-1.75× faster in the backward pass. Compared to a standard attention implementation, FlashAttention-3 can be up to 3-16× faster. For medium and long sequences (1k and above), FlashAttention-3 even surpasses the speed of a vendor’s library (cuDNN – closed source) that has been optimized for H100 GPUs. 

**Benchmark settings:** We vary the sequence length as 512, 1k, ..., 16k, and set batch size so that the total number of tokens is 16k. We set the hidden dimension to 2048, and head dimension to be either 64, 128, or 256 (i.e., 32 heads, 16 heads, or 8 heads). To calculate the FLOPs of the forward pass, we use: 



With causal masking, we divide this number by 2 to account for the fact that approximately only half of the entries are calculated. To get the FLOPs of the backward pass, we multiply the forward pass FLOPs by 2.5 (since there are 2 matmuls in the forward pass and 5 matmuls in the backward pass, due to recomputation). 

We also measure the runtime for FP8 for the forward pass under similar settings. We report the results for headdim 256 in Fig. 7 and give the full results in Appendix C.2.

---

[referencia=4791e267352f48bb score=0.770]
### **3.3 Low-precision with FP8** 

**Efficiency: layout transformations.** Computing the forward pass of FlashAttention-3 in FP8 precision poses additional challenges not encountered for FP16 in terms of layout conformance. 

7 

T0 {d0, d1} T1 {d0, d1} T2 {d0, d1} T3 {d0, d1} T0 {d4, d5} T1 {d4, d5} T2 {d4, d5} T3 {d4, d5} T0 {d2, d3} T1 {d2, d3} T2 {d2, d3} T3 {d2, d3} T0 {d6, d7} T1 {d6, d7} T2 {d6, d7} T3 {d6, d7} 

Figure 3: FP32 accumulator register WGMMA layout – rows 0 and 8, threads 0-3, entries 0-7. 

T0 {a0, a1} T0 {a2, a3} T1 {a0, a1} T1 {a2, a3} T2 {a0, a1} T2 {a2, a3} T3 {a0, a1} T3 {a2, a3} T0 {a4, a5} T0 {a6, a7} T1 {a4, a5} T1 {a6, a7} T2 {a4, a5} T2 {a6, a7} T3 {a4, a5} T3 {a6, a7} 

Figure 4: FP8 operand A register WGMMA layout – rows 0 and 8, threads 0-3, entries 0-7.

---

[referencia=4791e267352f48bb score=0.755]
### **4.3 Numerical Error Validation** 

As there has been interest in the numerical error [21] of FlashAttention, we compare FlashAttention-2, FlashAttention-3, and a standard implementation of attention against a reference implementation in FP64. To simulate outlier features and activations in LLMs [20, 54], we generate the entries of **Q** _,_ **K** _,_ **V** with the following 

10 



<!-- Start of picture text -->
Attention backward speed, head dim 64 (H100 80GB SXM5) Attention backward speed, head dim 128 (H100 80GB SXM5)<br>Standard attention Standard attention<br>600 FlashAttention-2cuDNN 600 FlashAttention-2cuDNN 542 559 561<br>FlashAttention-3 453 472 474 FlashAttention-3 465501 499 518 516<br>400 348363 395422 417 432 433 400 408424<br>266272 264 279 287 291 305316 260 291 310 318 322<br>238<br>198 214<br>200 200 159 174 181<br>131<br>68 76 88 92 95 104<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br><!-- End of picture text -->

- (a) Backward, without causal mask, head dim 64 

- (b) Backward, without causal mask, head dim 128 

Figure 6: Attention backward speed (FP16/BF16) on H100 GPU 



<!-- Start of picture text -->

---

[referencia=4791e267352f48bb score=0.698]
**Asynchrony and warp-specialization:** GPUs are throughput processors that rely on concurrency and asynchrony to hide memory and execution latencies. For async memory copy between GMEM and SMEM, Hopper has the Tensor Memory Accelerator (TMA) as a dedicated hardware unit [38, §7.29]. Furthermore, unlike prior architectures such as Ampere, the Tensor Core of Hopper, exposed via the warpgroup-wide WGMMA instruction [40, §9.7.14], is also asynchronous and can source its inputs directly from shared memory. 

> 4Luo et al. [34] reports shared memory bandwidth of 128 bytes per clock cycle per SM, and we multiply that by 132 SMs and the boost clock of 1830 MHz. 

3 

Hardware support for asynchrony allows for warp-specialized kernels, where the warps of a CTA are divided into producer or consumer roles that only ever issue either data movement or computation. Generically, this improves the compiler’s ability to generate optimal instruction schedules [4]. In addition, Hopper supports the dynamic reallocation of registers between warpgroups via `setmaxnreg` [40, §9.7.17.1], so those warps doing MMAs can obtain a larger share of RMEM than those just issuing TMA (for which only a single thread is needed). 

**Low-precision number formats:** Modern GPUs have specialized hardware units for accelerating low-precision computation. For example, the WGMMA instruction can target the FP8 Tensor Cores on Hopper to deliver 2x the throughput per SM when compared to FP16 or BF16.

---

[referencia=4791e267352f48bb score=0.645]
## **3 FlashAttention-3: Algorithm** 

In this section, we describe the FlashAttention-3 algorithm. For simplicity, we focus on the forward pass, with the backward pass algorithm described in Appendix B.1. We first indicate how to integrate warp-specialization with a circular SMEM buffer into the base algorithm of FlashAttention-2. We then explain how to exploit asynchrony of WGMMA to define an overlapped GEMM-softmax 2-stage pipeline. Finally, we describe the modifications needed for FP8, both in terms of layout conformance and accuracy via block quantization and incoherent processing.

---

[referencia=4791e267352f48bb score=0.554]
However, correctly invoking FP8 WGMMA entails understanding the layout constraints on its operands. Given a GEMM call to multiply _𝐴_ × _𝐵_<sup>⊤</sup> for an _𝑀_ × _𝐾_ -matrix _𝐴_ and an _𝑁_ × _𝐾_ -matrix _𝐵_ , we say that the _𝐴_ or _𝐵_ operand is _mn-major_ if it is contiguous in the outer _𝑀_ or _𝑁_ dimension, and _k-major_ if is instead contiguous in the inner _𝐾_ -dimension. Then for FP16 WGMMA, both mn-major and k-major input operands are accepted for operands in SMEM, but for FP8 WGMMA, only the k-major format is supported. Moreover, in situations such as attention where one wants to fuse back-to-back GEMMs in a single kernel, clashing FP32 accumulator and FP8 operand layouts pose an obstacle to invoking dependent FP8 WGMMAs. 

In the context of attention, these layout restrictions entail certain modifications to the design of an FP8 algorithm, which we describe in §3.3. 

### **2.3 Standard Attention and Flash Attention** 

Following Dao et al. [17], we let **standard attention** denote an implementation of attention on the GPU that materializes the intermediate matrices **S** and **P** to HBM. The main idea of FlashAttention was to leverage a local version of the softmax reduction to avoid these expensive intermediate reads/writes and fuse attention into a single kernel. Local softmax corresponds to lines 18-19 of the consumer mainloop in Algorithm 1 together with the rescalings of blocks of **O** . The simple derivation that this procedure indeed computes **O** can be found in [15, §2.3.1].

---

[referencia=4791e267352f48bb score=0.514]
## **References** 

- [1] Ahmad Abdelfattah, Azzam Haidar, Stanimire Tomov, and Jack Dongarra. Performance, design, and autotuning of batched gemm for gpus. pages 21–38, 06 2016. ISBN 978-3-319-41320-4. doi: 10.1007/978-3-319-41321-1_2. 

- [2] AI21. Introducing jamba: Ai21’s groundbreaking ssm-transformer model. _AI21 blog_ , 2024. 

- [3] Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón, and Sumit Sanghai. Gqa: Training generalized multi-query transformer models from multi-head checkpoints. _arXiv preprint arXiv:2305.13245_ , 2023. 

- [4] Michael Bauer, Henry Cook, and Brucek Khailany. CudaDMA: Optimizing GPU Memory Bandwidth via Warp Specialization. In _Proceedings of 2011 International Conference for High Performance Computing, Networking, Storage and Analysis_ , SC ’11, New York, NY, USA, 2011. Association for Computing Machinery. ISBN 9781450307710. doi: 10.1145/2063384.2063400. URL `https://doi.org/10.1145/2063384.2063400` . 

- [5] Maximilian Beck, Korbinian Pöppel, Markus Spanring, Andreas Auer, Oleksandra Prudnikova, Michael Kopp, Günter Klambauer, Johannes Brandstetter, and Sepp Hochreiter. xlstm: Extended long short-term memory. _arXiv preprint arXiv:2405.04517_ , 2024. 

> 10For our benchmarks, FP16 FlashAttention-3 has a persistent kernel and load balancing strategy, while FP8 FlashAttention-3 does not. This partly explains why FP8 FlashAttention-3 does not perform as well for small sequence length and causal masking compared to the FP8 cuDNN kernels. 

12

---

[referencia=4791e267352f48bb score=0.509]
### **C.2 FP8 Attention Full Results** 

We use following sequence lengths: 512, 1024, 2048, 4224, 8448, 16896. When sequence length ≥ 4k, we make it also divisible by 132 (number of SMs in H100 SXM5) to avoid wave quantization. 

21 



<!-- Start of picture text -->
Attention forward speed, head dim 64 (H100 80GB SXM5)<br>1200 Triton<br>cuDNN<br>FlashAttention-3<br>800<br>568 596 613<br>400 392344 444398396 473447462 499413 506431 511438<br>240<br>512 1k 2k 4k 8k 16k<br>Sequence length<br>Speed (TFLOPs/s)<br><!-- End of picture text -->

- (a) Forward, without causal mask, head dim 64 



<!-- Start of picture text -->
Attention forward speed, head dim 128 (H100 80GB SXM5)<br><!-- End of picture text -->



<!-- Start of picture text -->
1200 Triton<br>cuDNN<br>FlashAttention-3 971974 10031008<br>918<br>886 864<br>800 751 733<br>617 596 605 630 635<br>563<br>502<br>408<br>400 348<br>512 1k 2k 4k 8k 16k<br>Sequence length<br>(c) Forward, without causal mask, head dim 128<br>Attention forward speed, head dim 256 (H100 80GB SXM5)<br>1200 TritoncuDNN 1087 11221151 11391171<br>FlashAttention-3 1001<br>966<br>878 931 854 897 903<br>800 744 766<br>686 664<br>529 510<br>400<br>512 1k 2k 4k 8k 16k<br>Sequence length<br>Speed (TFLOPs/s)<br>Speed (TFLOPs/s)<br><!-- End of picture text -->

(e) Forward, without causal mask, head dim 256 



<!-- Start of picture text -->

---

[referencia=4791e267352f48bb score=0.494]
**Alternative architectures** Motivated by the limitations of attention, a variety of alternative architectures have been proposed. They build on the connection between linear attention [27] and recurrent neural networks (RNNs). RWKV [42], H3 [18], MEGA [35], Retnet [55] enhance the expressivity of the simple cumulative sum in linear attention with more sophisticated recurrences. Mamba [22] and xLSTM [5] use learnable weighting for the recurrence and can match the quality of Transformers in language modeling at small or medium scale. These approaches can be connected to generalizations of linear attention through the lens of the structure of the token-mixing matrix [16]. These models have started to see some traction, seeing usage in some medium to large-scale models such as Jamba [2], Zamba [64], Megalodon [36], and Mamba2-hybrid [60]. For the highest quality, these SSM- and RNN-based models still employ many layers of attention. We expect that techniques to speed up attention presented in this work will be useful to speedup these alternative architectures. 

**Low-precision attention** Quantization is a promising approach to speed up attention, but they have mostly focused on reducing the space for KV cache for inference efficiency. QuIP [9] and QuIP#[58] use incoherent processing to reduce the quantization, and we adapted this technique for FP8 FlashAttention-3. Recent work suggests that for inference the KV cache is highly compressible down to 4-, 3-, or even 2-bits [26, 33]. However, quantization during training is still challenging as higher precision is typically required for stable training.

---

[referencia=4791e267352f48bb score=0.494]
**O** _𝑖_ = **O** _𝑖_ + **P**<sup>˜</sup> last **V** _𝑇𝑐_ −1 using WGMMA. Commit and wait. 

> 20: Epilogue: Rescale **O** _𝑖_ based on _𝑚𝑖_ . Compute _𝐿𝑖_ based on _𝑚𝑖_ and _ℓ𝑖_ . Write **O** _𝑖_ and _𝐿𝑖_ to HBM as the _𝑖_ -th block of **O** and _𝐿_ . 

Algorithm 2 functions as a replacement for the consumer path of Algorithm 1 to comprise the complete FlashAttention-3 algorithm for FP16 precision. At a high-level, we use WGMMA as a metonym for asynchronous 



<!-- Start of picture text -->