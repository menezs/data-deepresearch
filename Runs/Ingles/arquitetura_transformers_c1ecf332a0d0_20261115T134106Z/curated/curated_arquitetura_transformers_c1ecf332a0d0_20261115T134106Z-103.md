[referencia=0927a2806ac8318f score=0.999]
# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning 

Tri Dao<sup>1,2</sup> 

> 1Department of Computer Science, Princeton University 

> 2Department of Computer Science, Stanford University `trid@cs.stanford.edu` 

July 18, 2023 

##### **Abstract** 

Scaling Transformers to longer sequence lengths has been a major problem in the last several years, promising to improve performance in language modeling and high-resolution image understanding, as well as to unlock new applications in code, audio, and video generation. The attention layer is the main bottleneck in scaling to longer sequences, as its runtime and memory increase quadratically in the sequence length. FlashAttention [5] exploits the asymmetric GPU memory hierarchy to bring significant memory saving (linear instead of quadratic) and runtime speedup (2-4× compared to optimized baselines), with no approximation. However, FlashAttention is still not nearly as fast as optimized matrix-multiply (GEMM) operations, reaching only 25-40% of the theoretical maximum FLOPs/s. We observe that the inefficiency is due to suboptimal work partitioning between different thread blocks and warps on the GPU, causing either low-occupancy or unnecessary shared memory reads/writes. We propose FlashAttention-2, with better work partitioning to address these issues. In particular, we (1) tweak the algorithm to reduce the number of non-matmul FLOPs (2) parallelize the attention computation, even for a single head, across different thread blocks to increase occupancy, and (3) within each thread block, distribute the work between warps to reduce communication through shared memory. These yield around 2× speedup compared to FlashAttention, reaching 50-73% of the theoretical maximum FLOPs/s on A100 and getting close to the efficiency of GEMM operations. We empirically validate that when used end-to-end to train GPT-style models, FlashAttention-2 reaches training speed of up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization).<sup>1</sup>

---

[referencia=0927a2806ac8318f score=0.998]
## **4 Empirical Validation** 

We evaluate the impact of using FlashAttention-2 to train Transformer models. 

- **Benchmarking attention.** We measure the runtime of FlashAttention-2 across different sequence lengths and compare it to a standard implementation in PyTorch, FlashAttention, and FlashAttention in Triton. We confirm that FlashAttention-2 is 1.7-3.0× faster than FlashAttention, 1.3-2.5× faster than FlashAttention in Triton, and 3-10× faster than a standard attention implementation. 

9 

FlashAttention-2 reaches up to 230 TFLOPs/s, 73% of the theoretical maximum TFLOPs/s on A100 GPUs. 

- **End-to-end training speed** When used end-to-end to train GPT-style models of size 1.3B and 2.7B on sequence lengths either 2k or 8k, FlashAttention-2 yields up to 1.3× speedup compared to FlashAttention and 2.8× speedup compared to a baseline without FlashAttention. FlashAttention-2 reaches up to 225 TFLOPs/s (72% model FLOPs utilization) per A100 GPU.

---

[referencia=0927a2806ac8318f score=0.997]
Figure 6: Attention backward speed on A100 GPU 

Table 1: Training speed (TFLOPs/s/GPU) of GPT-style models on 8×A100 GPUs. FlashAttention-2 reaches up to 225 TFLOPs/s (72% model FLOPs utilization). We compare against a baseline running without FlashAttention. 

|Model|Without FlashAttention|FlashAttention|FlashAttention-2|
|---|---|---|---|
|GPT3-1.3B 2k context|142 TFLOPs/s|189 TFLOPs/s|196 TFLOPs/s|
|GPT3-1.3B 8k context|72 TFLOPS/s|170 TFLOPs/s|220 TFLOPs/s|
|GPT3-2.7B 2k context|149 TFLOPs/s|189 TFLOPs/s|205 TFLOPs/s|
|GPT3-2.7B 8k context|80 TFLOPs/s|175 TFLOPs/s|225 TFLOPs/s|



be used to understand long books and reports, high resolution images, audio and video. FlashAttention-2 will also speed up training, finetuning, and inference of existing models. 

In the near future, we plan to collaborate with researchers and engineers to make FlashAttention widely applicable in different kinds of devices (e.g., H100 GPUs, AMD GPUs), as well as new data types such as FP8. As an immediate next step, we plan to optimize FlashAttention-2 for H100 GPUs to use new hardware features (TMA, 4th-gen Tensor Cores, fp8). Combining the low-level optimizations in FlashAttention-2 with high-level algorithmic changes (e.g., local, dilated, block-sparse attention) could allow us to train AI models with much longer context. We are also excited to work with compiler researchers to make these optimization techniques easily programmable. 

12 



<!-- Start of picture text -->

---

[referencia=0927a2806ac8318f score=0.995]
than a standard attention implementation, the forward pass only reaches 30-50% of the theoretical maximum FLOPs/s of the device (Fig. 5), while the backward pass is even more challenging, reaching only 25-35% 

- of maximum throughput on A100 GPU (Fig. 6). In contrast, optimized GEMM can reach up to 80-90% of the theoretical maximum device throughput. Through careful profiling, we observe that FlashAttention still has suboptimal work partitioning between different thread blocks and warps on the GPU, causing either low-occupancy or unnecessary shared memory reads/writes. 

- Building on FlashAttention, we propose FlashAttention-2 with better parallelism and work 

- partitioning to address these challenges. 

   1. In Section 3.1, we tweak the algorithms to reduce the number of non-matmul FLOPs while not changing 

      - the output. While the non-matmul FLOPs only account for a small fraction of the total FLOPs, they take longer to perform as GPUs have specialized units for matrix multiply, and as a result the matmul throughput can be up to 16× higher than non-matmul throughput. It is thus important to reduce 

      - non-matmul FLOPs and spend as much time as possible doing matmul FLOPs. 

   2. We propose to parallelize both the forward pass and backward pass along the sequence length dimension, in addition to the batch and number of heads dimension. This increases occupancy (utilization of GPU resources) in the case where the sequences are long (and hence batch size is often small). 

   3. Even within one block of attention computation, we partition the work between different warps of a thread block to reduce communication and shared memory reads/writes. 

- In Section 4, we empirically validate that FlashAttention-2 yields significant speedup compared to 

- even FlashAttention. Benchmarks on different settings (with or without causal mask, different head dimensions) show that FlashAttention-2 achieves around 2× speedup over FlashAttention, reaching 

up to 73% of the theoretical max throughput in the forward pass, and up to 63% of the theoretical max 

- throughput in the backward pass. When used end-to-end to train GPT-style models, we reach training speed of up to 225 TFLOPs/s per A100 GPU.

---

[referencia=0927a2806ac8318f score=0.987]
OOM OOM 512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k Sequence length Sequence length (a) Without causal mask, head dimension 64 (b) Without causal mask, head dimension 128 Attention forward speed (A100 80GB SXM4) Attention forward speed (A100 80GB SXM4) Pytorch Pytorch 200 FlashAttentionxformers 177 181 183 200 FlashAttentionxformers 187 198 200 197 FlashAttention Triton 167 FlashAttention Triton168 150 FlashAttention-2146 131 137 143 150 FlashAttention-2132 126 133 141 148 115 112 108 107 112 115 117 100 99 89 8992 9194 9495 100 89 95 78 82 81 79 5671 70 59 65 68 70 71 49 50 50 10 10 10 10 10 15 18 19 19 19 OOM OOM 512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k 

Sequence length Sequence length (c) With causal mask, head dimension 64 (d) With causal mask, head dimension 128 Figure 5: Attention forward speed on A100 GPU 

Just running the same implementation on H100 GPUs (using no special instructions to make use of new features such as TMA and 4th-gen Tensor Cores), we obtain up to 335 TFLOPs/s (Fig. 7). We expect that by using new instructions, we can obtain another 1.5x-2x speedup on H100 GPUs. We leave that to future work. 

**4.2 End-to-end Performance** We measure the training throughput of GPT-style models with either 1.3B or 2.7B parameters, on 8×A100 80GB SXM. As shown in Table 1, FlashAttention-2 yields 2.8× speedup compared to a baseline without FlashAttention and 1.3× speedup compared to FlashAttention-2, reaching up to 225 TFLOPs/s per A100 GPU.

---

[referencia=0927a2806ac8318f score=0.969]
## **3 FlashAttention-2: Algorithm, Parallelism, and Work Partitioning** 

We describe the FlashAttention-2 algorithm, which includes several tweaks to FlashAttention to reduce the number of non-matmul FLOPs. We then describe how to parallelize the computation on different thread blocks to make full use the GPU resources. Finally we describe we partition the work between different warps within one thread block to reduce the amount of shared memory access. These improvements lead to 2-3× speedup as validated in Section 4.

---

[referencia=0927a2806ac8318f score=0.936]
7 

an A100 GPU for example. This scheduling is efficient when this number is large (say ≥ 80), since we can effectively use almost all of the compute resources on the GPU. 

|In the case of long sequences (which usually means small batch sizes or small number of heads), to make<br>better use of the multiprocessors on the GPU, we now additionally parallelize over the sequence length<br>dimension. This results in signifcant speedup for this regime.|
|---|
|**Forward pass.**<br>We see that the outer loop (over sequence length) is embarrassingly parallel, and we<br>schedule them on diferent thread blocks that do not need to communicate with each other. We also parallelize<br>over the batch dimension and number of heads dimension, as done in FlashAttention. The increased<br>parallelism over sequence length helps improve occupancy (fraction of GPU resources being used) when the<br>batch size and number of heads are small, leading to speedup in this case.<br>These ideas of swapping the order of the loop (outer loop over row blocks and inner loop over column<br>blocks, instead of the other way round in the original FlashAttention paper), as well as parallelizing<br>over the sequence length dimension were frst suggested and implemented by Phil Tillet in the Triton [17]<br>implementation.<sup>3</sup>|
|**Backward pass.**<br>Notice that the only shared computation between diferent column blocks is in update **dQ**<br>in Algorithm 2, where we need to load **dQ**_𝑖_from HBM to SRAM, then on chip, update **dQ**_𝑖_←**dQ**_𝑖_+**dS**<sup>(</sup><sup>_𝑗_)</sup><br>_𝑖_<br>**K**_𝑗_,<br>and write back to HBM. We thus parallelize over the sequence length dimension as well, and schedule 1<br>thread block for each column block of the backward pass. We use atomic adds to communicate between<br>diferent thread blocks to update **dQ**.<br>We describe the parallelization scheme in Fig. 2.|

---

[referencia=0927a2806ac8318f score=0.914]
<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br><!-- End of picture text -->

Figure 4: Attention forward + backward speed on A100 GPU 

10 

Attention forward speed (A100 80GB SXM4) Attention forward speed (A100 80GB SXM4) Pytorch Pytorch209 224 227 222 224 FlashAttention FlashAttention 200 191 193 192 192 192 200 xformers178 xformers FlashAttention Triton FlashAttention Triton 

|50<br>100<br>150<br>200<br>29<br>34<br>35<br>37<br>37<br>OOM<br>91<br>96<br>99<br>104<br>104<br>104<br>89<br>94<br>97<br>99<br>98<br>98<br>128<br>141<br>149<br>152<br>152<br>155<br>178<br>191<br>193<br>192<br>192<br>192<br>Pytorch<br>FlashAttention<br>xformers<br>FlashAttention Triton<br>FlashAttention-2|50<br>100<br>150<br>200<br>Speed (TFLOPs/s)|42<br>56<br>60<br>63<br>67<br>OOM<br>69<br>66<br>71<br>71<br>72<br>73<br>107<br>115<br>120<br>122<br>122<br>122<br>127<br>140<br>152<br>157<br>160<br>163<br>209<br>224<br>227<br>222<br>224<br>223<br>Pytorch<br>FlashAttention<br>xformers<br>FlashAttention Triton<br>FlashAttention-2|
|---|---|---|

---

[referencia=0927a2806ac8318f score=0.899]
### **3.3 Work Partitioning Between Warps** 

As Section 3.2 describe how we schedule thread blocks, even within each thread block, we also have to decide how to partition the work between different warps. We typically use 4 or 8 warps per thread block, and the partitioning is described in Fig. 3. 

**Forward pass.** For each block, FlashAttention splits **K** and **V** across 4 warps while keeping **Q** accessible by all warps. Each warp multiplies to get a slice of **QK**<sup>⊤</sup> , then they need to multiply with a slice of **V** and communicate to add up the result. This is referred to as the “split-K” scheme. However, this is inefficient since all warps need to write their intermediate results out to shared memory, synchronize, then add up the intermediate results. These shared memory reads/writes slow down the forward pass in FlashAttention. In FlashAttention-2, we instead split **Q** across 4 warps while keeping **K** and **V** accessible by all warps. After each warp performs matrix multiply to get a slice of **QK**<sup>⊤</sup> , they just need to multiply with their shared slice of **V** to get their corresponding slice of the output. There is no need for communication between warps. The reduction in shared memory reads/writes yields speedup (Section 4). 





Figure 3: Work partitioning between different warps in the forward pass 

**Backward pass.** Similarly for the backward pass, we choose to partition the warps to avoid the “split-K” scheme. However, it still requires some synchronization due to the more complicated dependency between all the different inputs and gradients **Q** _,_ **K** _,_ **V** _,_ **O** _,_ **dO** _,_ **dQ** _,_ **dK** _,_ **dV** . Nevertheless, avoiding “split-K” reduces shared memory reads/writes and again yields speedup (Section 4).

---

[referencia=0927a2806ac8318f score=0.897]
12 



<!-- Start of picture text -->
Attention forward + backward speed (H100 80GB SXM5) Attention forward + backward speed (H100 80GB SXM5)<br>Pytorch Pytorch<br>FlashAttention FlashAttention 320 326 335 338<br>300 FlashAttention-2 274 288 294 296 300 FlashAttention-2294<br>254 248<br>215<br>200 200<br>157 159 161 161 166 168 160 167<br>127 120127 145128 131 137 139<br>100 62 72 81 86 87 100 93<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(a) Without causal mask, head dimension 64 (b) Without causal mask, head dimension 128<br>Attention forward + backward speed (H100 80GB SXM5) Attention forward + backward speed (H100 80GB SXM5)<br>Pytorch Pytorch<br>FlashAttention FlashAttention 328<br>FlashAttention-2 FlashAttention-2 308<br>300 284 300 294<br>257 273 265<br>232 221<br>200 192 200<br>141 123 136 138 149 156 163 126 135 137<br>104 98 109 108<br>100 100<br>26 29 31 32 32 40 50 57 61 63<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(c) With causal mask, head dimension 64 (d) With causal mask, head dimension 128<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br><!-- End of picture text -->

Figure 7: Attention forward + backward speed on H100 GPU

---

[referencia=0927a2806ac8318f score=0.868]
### **3.1 Algorithm** 

We tweak the algorithm from FlashAttention to reduce the number of non-matmul FLOPs. This is because modern GPUs have specialized compute units (e.g., Tensor Cores on Nvidia GPUs) that makes matmul much faster. As an example, the A100 GPU has a max theoretical throughput of 312 TFLOPs/s of FP16/BF16 matmul, but only 19.5 TFLOPs/s of non-matmul FP32. Another way to think about this is that each non-matmul FLOP is 16× more expensive than a matmul FLOP. To maintain high throughput (e.g., more than 50% of the maximum theoretical TFLOPs/s), we want to spend as much time on matmul FLOPs as possible.

---

[referencia=0927a2806ac8318f score=0.865]
Attention forward + backward speed (A100 80GB SXM4) Attention forward + backward speed (A100 80GB SXM4)<br>Pytorch Pytorch<br>200 FlashAttentionxformers 200 FlashAttentionxformers 187 196 201 203<br>FlashAttention Triton 162 171 175 176 FlashAttention Triton173<br>FlashAttention-2153 FlashAttention-2151<br>150 150<br>132<br>100 916890 9273102 1047698 1087798 11075100 11075100 100 768378 67729185 76769590 79809693 86829795 839895<br>53<br>50 36 40 43 45 46 50<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(a) Without causal mask, head dimension 64 (b) Without causal mask, head dimension 128<br>Attention forward + backward speed (A100 80GB SXM4) Attention forward + backward speed (A100 80GB SXM4)<br>Pytorch Pytorch<br>FlashAttention FlashAttention<br>200 xformers 200 xformers 182 189<br>FlashAttention Triton 165 171 FlashAttention Triton 173<br>FlashAttention-2 156 FlashAttention-2 155<br>150 140 150<br>133<br>119<br>100 58515988 706075 776679 876876 926979 976780 100 55585099 627261 698268 768774 809178 839280<br>50 50<br>15 16 17 18 18 23 28 32 32 34<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(c) With causal mask, head dimension 64 (d) With causal mask, head dimension 128<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br>

---

[referencia=0927a2806ac8318f score=0.829]
## **1 Introduction** 

Scaling up the context length of Transformers [18] is a challenge, since the attention layer at their heart has runtime and memory requirements quadratic in the input sequence length. Ideally, we would like to go beyond the standard 2k sequence length limit to train models to understand books, high resolution images, and long-form videos. Just within the last year, there have been several language models with much longer context than before: GPT-4 [12] with context length 32k, MosaicML’s MPT with context length 65k, and Anthropic’s Claude with context length 100k. Emerging use cases such as long document querying and story writing have demonstrated a need for models with such long context. 

To reduce the computational requirement of attention on such long context, there have been numerous methods proposed to approximate attention [2, 3, 4, 8, 9, 14, 19, 20]. Though these methods have seen some use cases, as far as we know, most large-scale training runs still use standard attention. Motivated by this, Dao et al. [5] proposed to reorder the attention computation and leverages classical techniques (tiling, recomputation) to significantly speed it up and reduce memory usage from quadratic to linear in sequence length. This yields 2-4× wall-clock time speedup over optimized baselines, up to 10-20× memory saving, 

> 1FlashAttention-2 is available at `https://github.com/Dao-AILab/flash-attention` 

1 

- with no approximation, and as a result FlashAttention has seen wide adoption in large-scale training and inference of Transformers. 

However, context length increases even more, FlashAttention is still not nearly as efficient as other primitives such as matrix-multiply (GEMM). In particular, while FlashAttention is already 2-4× faster 

than a standard attention implementation, the forward pass only reaches 30-50% of the theoretical maximum FLOPs/s of the device (Fig. 5), while the backward pass is even more challenging, reaching only 25-35%

---

[referencia=0927a2806ac8318f score=0.822]
11 



<!-- Start of picture text -->
Attention backward speed (A100 80GB SXM4) Attention backward speed (A100 80GB SXM4)<br>Pytorch Pytorch<br>200 FlashAttentionxformers 200 FlashAttentionxformers 187 193 196<br>FlashAttention Triton 163 169 170 FlashAttention Triton159 175<br>FlashAttention-2 152 FlashAttention-2<br>150 141 150 136<br>120<br>106 109 112 113<br>100 916281 906792 7087 7086 6987 6888 100 59787668 73758474 86798877 88848980 97869082 889181<br>50 39 43 48 49 51 50<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(a) Without causal mask, head dimension 64 (b) Without causal mask, head dimension 128<br>Attention backward speed (A100 80GB SXM4) Attention backward speed (A100 80GB SXM4)<br>Pytorch Pytorch<br>FlashAttention FlashAttention<br>200 xformers 200 xformers 186<br>176<br>FlashAttention Triton 160 166 FlashAttention Triton 165<br>150 FlashAttention-2 149 150 FlashAttention-2 145<br>131<br>122<br>111<br>10050 58465381 705468 766071 856265 936267 986068 10050 59534390 37636552 43717558 45808063 49868466 898467<br>19 21 24 25 26 30<br>OOM OOM<br>512 1k 2k 4k 8k 16k 512 1k 2k 4k 8k 16k<br>Sequence length Sequence length<br>(c) With causal mask, head dimension 64 (d) With causal mask, head dimension 128<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br>Speed (TFLOPs/s) Speed (TFLOPs/s)<br><!-- End of picture text -->

---

[referencia=0927a2806ac8318f score=0.775]
### **3.2 Parallelism** 

The first version of FlashAttention parallelizes over batch size and number of heads. We use 1 thread block to process one attention head, and there are overall batch size · number of heads thread blocks. Each thread block is scheduled to run on a streaming multiprocessor (SM), and there are 108 of these SMs on 

7 

an A100 GPU for example. This scheduling is efficient when this number is large (say ≥ 80), since we can effectively use almost all of the compute resources on the GPU.

---

[referencia=0927a2806ac8318f score=0.704]
### **4.1 Benchmarking Attention** 

We measure the runtime of different attention methods on an A100 80GB SXM4 GPU for different settings (without / with causal mask, head dimension 64 or 128). We report the results in Fig. 4, Fig. 5 and Fig. 6, showing that FlashAttention-2 is around 2× faster than FlashAttention and FlashAttention in `xformers` (the “cutlass” implementation). FlashAttention-2 is around 1.3-1.5× faster than FlashAttention in Triton in the forward pass and around 2× faster in the backward pass. Compared to a standard attention implementation in PyTorch, FlashAttention-2 can be up to 10× faster. 

Benchmark setting: we vary the sequence length from 512, 1k, ..., 16k, and set batch size so that the total number of tokens is 16k. We set hidden dimension to 2048, and head dimension to be either 64 or 128 (i.e., 32 heads or 16 heads). To calculate the FLOPs of the forward pass, we use: 



With causal mask, we divide this number by 2 to account for the fact that approximately only half of the entries are calculated. To get the FLOPs of the backward pass, we multiply the forward pass FLOPs by 2.5 (since there are 2 matmuls in the forward pass and 5 matmuls in the backward pass, due to recomputation). 



<!-- Start of picture text -->

---

[referencia=0927a2806ac8318f score=0.607]
#### **3.1.1 Forward pass** 

We revisit the online softmax trick as shown in Section 2.3 and make two minor tweaks to reduce non-matmul FLOPs: 

1. We do not have to rescale both terms of the output update by diag( _ℓ_<sup>(2)</sup> )<sup>−1</sup> : 



We can instead maintain an “un-scaled” version of **O**<sup>(2)</sup> and keep around the statistics _ℓ_<sup>(2)</sup> : 



Only at the every end of the loop do we scale the final **O**<sup>˜(last)</sup> by diag( _ℓ_<sup>(last)</sup> )<sup>−1</sup> to get the right output. 

2. We do not have to save both the max _𝑚_<sup>(</sup><sup>_𝑗_)</sup> and the sum of exponentials _ℓ_<sup>(</sup><sup>_𝑗_)</sup> for the backward pass. We only need to store the logsumexp _𝐿_<sup>(</sup><sup>_𝑗_)</sup> = _𝑚_<sup>(</sup><sup>_𝑗_)</sup> + log( _ℓ_<sup>(</sup><sup>_𝑗_)</sup> ). 

5 

In the simple case of 2 blocks in Section 2.3, the online softmax trick now becomes: 



We describe the full FlashAttention-2 forward pass in Algorithm 1. 

**Algorithm 1** FlashAttention-2 forward pass 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, block sizes _𝐵𝑐_ , _𝐵𝑟_ .

---

[referencia=0927a2806ac8318f score=0.499]
## **2 Background** 

We provide some background on the performance characteristics and execution model of GPUs. We also describe the standard implementation of attention, as well as FlashAttention. 

### **2.1 Hardware characteristics** 

**GPU performance characteristics.** The GPU consists of compute elements (e.g., floating point arithmetic units) and a memory hierarchy. Most modern GPUs contain specialized units to accelerate matrix multiply in 

- low-precision (e.g., Tensor Cores on Nvidia GPUs for FP16/BF16 matrix multiply). The memory hierarchy comprise of high bandwidth memory (HBM), and on-chip SRAM (aka shared memory). As an example, the A100 GPU has 40-80GB of high bandwidth memory (HBM) with bandwidth 1.5-2.0TB/s and 192KB of 

- on-chip SRAM per each of 108 streaming multiprocessors with bandwidth estimated around 19TB/s [6, 7]. As the L2 cache is not directly controllable by the programmer, we focus on the HBM and SRAM for the purpose of this discussion. 

- **Execution Model.** GPUs have a massive number of threads to execute an operation (called a kernel). 

- Threads are organized into thread blocks, which are scheduled to run on streaming multiprocessors (SMs). Within each thread blocks, threads are grouped into warps (a group of 32 threads). Threads within a warp 

can communicate by fast shuffle instructions or cooperate to perform matrix multiply. Warps within a thread block can communicate by reading from / writing to shared memory. Each kernel loads inputs from HBM to registers and SRAM, computes, then writes outputs to HBM. 

2

---

[referencia=0927a2806ac8318f score=0.434]
#### **Acknowledgments** 

We thank Phil Tillet and Daniel Haziza, who have implemented versions of FlashAttention in Triton [17] and the `xformers` library [10]. FlashAttention-2 was motivated by exchange of ideas between different ways that attention could be implemented. We are grateful to the Nvidia CUTLASS team (especially Vijay Thakkar, Cris Cecka, Haicheng Wu, and Andrew Kerr) for their CUTLASS library, in particular the CUTLASS 3.x release, which provides clean abstractions and powerful building blocks for the implementation of FlashAttention-2. We thank Driss Guessous for integrating FlashAttention to PyTorch. FlashAttention-2 has benefited from helpful discussions with Phil Wang, Markus Rabe, James Bradbury, Young-Jun Ko, Julien Launay, Daniel Hesslow, Michaël Benesty, Horace He, Ashish Vaswani, and Erich Elsen. Thanks for Stanford CRFM and Stanford NLP for the compute support. We thank Dan Fu and Christopher Ré for their collaboration, constructive feedback, and constant encouragement on this line of work of designing hardware-efficient algorithms. We thank Albert Gu and Beidi Chen for their helpful suggestions on early drafts of this technical report.

---

[referencia=0927a2806ac8318f score=0.424]
#### **2.3.1 Forward pass** 

FlashAttention applies the classical technique of tiling to reduce memory IOs, by (1) loading blocks of inputs from HBM to SRAM, (2) computing attention with respect to that block, and then (3) updating the output without writing the large intermediate matrices **S** and **P** to HBM. As the softmax couples entire rows or blocks of row, online softmax [11, 13] can split the attention computation into blocks, and rescale the output of each block to finally get the right result (with no approximation). By significantly reducing the amount of memory reads/writes, FlashAttention yields 2-4× wall-clock speedup over optimized baseline attention implementations. 

We describe the online softmax technique [11] and how it is used in attention [13]. For simplicity, consider just one row block of the attention matrix **S** , of the form � **S**<sup>(1)</sup> **S**<sup>(2)�</sup> for some matrices **S**<sup>(1)</sup> _,_ **S**<sup>(2)</sup> ∈ R<sup>_𝐵𝑟_×</sup><sup>_𝐵𝑐_</sup> , where _𝐵𝑟_ and _𝐵𝑐_ are the row and column block sizes. We want to compute softmax of this row block and **V** (1) multiply with the value, of the form for some matrices **V**<sup>(1)</sup> _,_ **V**<sup>(2)</sup> ∈ R<sup>_𝐵𝑐_×</sup><sup>_𝑑_</sup> . Standard softmax would **V**<sup>(2)</sup> <u>� �</u> 

> 2For clarity of exposition, we omit the scaling of **QK** ⊤ (typically by 1/d), and optionally elementwise masking on **S** and/or dropout applied to **P** 

3 

compute: 



Online softmax instead computes “local” softmax with respect to each block and rescale to get the right output at the end: 



We show how FlashAttention uses online softmax to enable tiling (Fig. 1) to reduce memory reads/writes.