[referencia=5727fed78bddc701 score=0.444]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=5727fed78bddc701 score=0.434]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.340]
|**FlashAttention**|**0.04**|0.06|0.21|0.82|2.85|10.41|41.74|167.19|670.76|2682.35|
|**Block-Sparse FlashAttention**|0.06|**0.06**|**0.06**|**0.12**|**0.44**|**0.86**|**1.70**|**3.29**|**6.55**|**13.34**|



We report timing results on the forward pass, backward pass, and combined forward + backward pass. We measure each method with and without dropout, masking, or both—except for Block Sparse, Longformer, and BigBird. These methods did not successfully run the backward pass with masking due to a bug in external libraries, so we measured them without masking to be generous. We use FP16 for all measurements, except for Local Attention, whose implementation only supports FP32. 

For each baseline, we increase sequence length until it runs out of memory on the GPU, except for the following exceptions: The Megatron implementation does not support sequence lengths longer than 2048. Block-Sparse (OpenAI) does not support sequence lengths longer than 4096. Longformer and BigBird do not support sequence lengths longer than 8092. 

We measure memory usage on the combined forward + backward pass, without dropout or masking. 

**Results** Table 8 summarizes all the experimental configurations and contains pointers to the results tables. 

31 

Table 10: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.305]
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

[referencia=a114e852aac1b2cb score=0.242]
## **4 Related Work** 

This work is focused on achieving a better tradeoff between decoder quality and inference time through reducing the memory bandwidth overhead (Williams et al., 2009) from loading keys and values. Shazeer (2019) first proposed reducing this overhead through multi-query attention. Follow-up work showed that multi-query attention 

is especially helpful for long inputs (Pope et al., 2022; de Jong et al., 2022). Rabe (2023) independently developed GQA with public implementation. Other works have explored grouping attention heads for computational efficiency (Park et al., 2020; Luo et al., 2022; Ni et al., 2023) without focusing specifically on key-value heads, which determine memory bandwidth overhead. 

A number of other methods have been proposed to reduce memory bandwidth overhead from keys and values, as well as parameters. Flash attention (Dao et al., 2022) structures the attention computation to avoid materializing the quadratic attention scores, reducing memory and speeding up training. Quantization (Dettmers et al., 2022; Frantar et al., 2022) reduces the size of weights and activations, including keys and values, by lowering precision. Model distillation (Hinton et al., 2015; Gou et al., 2021) instead reduces model size at a given precision, using data generated from the larger model to finetune the smaller model. Layersparse cross-attention (de Jong et al., 2022) eliminates most cross-attention layers which make up the primary expense for longer inputs. Speculative sampling (Chen et al., 2023; Leviathan et al., 2022) ameliorates the memory bandwidth bottleneck by proposing multiple tokens with a smaller model which are then scored in parallel by a larger model. 

Finally, the uptraining procedure we propose is inspired by Komatsuzaki et al. (2022), which uptrains standard T5 checkpoints into sparsely activated Mixture-of-Experts models.

---

[referencia=5727fed78bddc701 score=0.237]
## **5 Limitations and Future Directions** 

We discuss limitations of our approach and future directions. Related work is given in Appendix A. 

**Compiling to CUDA.** Our current approach to building IO-aware implementations of attention requires writing a new CUDA kernel for each new attention implementation. This requires writing the attention algorithm in a considerably lower-level language than PyTorch, and requires significant engineering effort. Implementations may also not be transferrable across GPU architectures. These limitations suggest the need for a method that supports writing attention algorithms in a high-level language (e.g., PyTorch), and compiling to IO-aware implementations in CUDA—similar to efforts such as Halide in image processing [70]. 

**IO-Aware Deep Learning.** We believe that the IO-aware approach can extend beyond attention. Attention is the most memory-intensive computation in Transformers, but every layer in a deep network touches GPU HBM. We hope our work inspires IO-aware implementations of additional modules. We discuss these potential extensions in Appendix D. 

**Multi-GPU IO-Aware Methods.** Our IO-aware implementation of attention is optimal within constants for computing attention on a single GPU. However, the attention computation may be parallelizable across multiple GPUs [72]. Using multiple GPUs adds an additional layer to IO analysis—accounting for data transfer between GPUs. We hope our work inspires future work in this direction.

---

[referencia=5727fed78bddc701 score=0.151]
Θ _𝑁𝑑_ +<sup>_𝑁_2</sup><sup>_𝑑_2</sup> _𝑠 ._ � _𝑀_ � □ **D.2 Potential Extensions** 

We discuss here a few potential extensions of the IO-aware approach to speed up deep learning training. **Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces 

another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other 

25 

GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. 

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. We believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. We are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime.

---

[referencia=5727fed78bddc701 score=0.149]
We also analyze the IO complexity of block-sparse FlashAttention. 

**Proposition 4.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> _𝑠_ ) _HBM accesses where 𝑠 is the fraction of nonzero blocks in the block-sparsity mask._ 

We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths _𝑁_ , _𝑠_ is often set to _𝑁_<sup>−1/2</sup> [11] or _𝑁_<sup>−1</sup> log _𝑁_ [3, 17, 92], resulting in Θ( _𝑁_ √ _𝑁_ ) or Θ( _𝑁_ log _𝑁_ ) IO complexity. For downstream experiments, we use the fixed butterfly sparsity pattern [17], which has been shown to be able to approximate arbitrary sparsity [16]. 

In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup, while performing on par with standard attention (Section 4).

---

[referencia=647d0f26df7e19e1 score=0.112]
Mistral 7B takes a significant step in balancing the goals of getting high performance while keeping large language models efficient. Through our work, our aim is to help the community create more affordable, efficient, and high-performing language models that can be used in a wide range of real-world applications. 

**2 Architectural details** 



**Figure 1: Sliding Window Attention.** The number of operations in vanilla attention is quadratic in the sequence length, and the memory increases linearly with the number of tokens. At inference time, this incurs higher latency and smaller throughput due to reduced cache availability. To alleviate this issue, we use sliding window attention: each token can attend to at most _W_ tokens from the previous layer (here, _W_ = 3). Note that tokens outside the sliding window still influence next word prediction. At each attention layer, information can move forward by _W_ tokens. Hence, after _k_ attention layers, information can move forward by up to _k × W_ tokens. 

Mistral 7B is based on a transformer architecture [27]. The main parameters of the architecture are summarized in Table 1. Compared to Llama, it introduces a few changes that we summarize below. 

**Sliding Window Attention.** SWA exploits the stacked layers of a transformer to attend information beyond the window size _W_ . The hidden state in position _i_ of the layer _k_ , _hi_ , attends to all hidden states from the previous layer with positions between _i − W_ and _i_ . Recursively, _hi_ can access tokens from the input layer at a distance of up to _W × k_ tokens, as illustrated in Figure 1. At the last layer, using a window size of _W_ = 4096, we have a theoretical attention span of approximately 131 _K_ tokens. In practice, for a sequence length of 16K and _W_ = 4096, changes made to FlashAttention [11] and xFormers [18] yield a 2x speed improvement over a vanilla attention baseline. 

**Parameter Value** `dim` 4096 `n_layers` 32 `head_dim` 128 `hidden_dim` 14336 `n_heads` 32 `n_kv_heads` 8 `window_size` 4096 `context_len` 8192 `vocab_size` 32000 

**Table 1: Model architecture.**

---

[referencia=5727fed78bddc701 score=0.096]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=5727fed78bddc701 score=0.086]
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

[referencia=5727fed78bddc701 score=0.067]
### **3.3 Extension: Block-Sparse FlashAttention** 

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity. Given inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and a mask matrix **M**<sup>˜</sup> ∈{0 _,_ 1}<sup>_𝑁_×</sup><sup>_𝑁_</sup> , we want to compute: 



where ( **S** ⊙ 𝟙 **M** ˜ ) _𝑘𝑙_ = **S** _𝑘𝑙_ if **M**<sup>˜</sup> _𝑘𝑙_ = 1 and −∞ if **M** _𝑘𝑙_ = 0. We require **M**<sup>˜</sup> to have block form: for some block sizes _𝐵𝑟 , 𝐵𝑐_ , for all _𝑘, 𝑙_ , **M**<sup>˜</sup> _𝑘,𝑙_ = **M** _𝑖𝑗_ with _𝑖_ = ⌊ _𝑘_ / _𝐵𝑟_ ⌋ _, 𝑗_ = ⌊ _𝑙_ / _𝐵𝑐_ ⌋ for some **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> . 

6 

Given a predefined block sparsity mask **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> we can easily adapt Algorithm 1 to only compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.

---

[referencia=5727fed78bddc701 score=0.048]
### **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

---

[referencia=a114e852aac1b2cb score=0.038]
## **5 Conclusion** 

Language models are expensive for inference primarily due to the memory bandwidth overhead from loading keys and values. Multi-query attention reduces this overhead at the cost of decreased model capacity and quality. We propose to convert multi-head attention models to multi-query models with a small fraction of original pre-training compute. Moreover, we introduce grouped-query attention, an interpolation of multi-query and multi-head attention that achieves quality close to multi-head at comparable speed to multi-query attention. 

## **Limitations** 

This paper focuses on ameliorating the memory bandwidth overhead from loading keys and values. This overhead is most important when generating longer sequences, for which quality is inherently difficult to evaluate. For summarization we employ Rouge score, which we know is a flawed evaluation that does not tell the whole story; for that reason, it is difficult to be certain our trade-offs are correct. Due to limited computation, we also do not compare our XXL GQA model to a comparitive model trained from scratch, so we do not know the relative performance of uptraining vs training from scratch. Finally, we evaluate the impact of uptraining and GQA only on encoder-decoder models. Recently, decoder-only models are extremely popular, and since these models do not have separate self-attention and cross-attention, we expect GQA to have a stronger advantage over MQA.

---

[referencia=5727fed78bddc701 score=0.035]
### **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=5727fed78bddc701 score=0.028]
**Kernel machine learning.** Our approach in FlashAttention relies on the fact that the _𝑁_ × _𝑁_ attention matrix is a function of a low-rank matrix **QK**<sup>⊤</sup> (of rank _𝑑_ ≪ _𝑁_ ). As a result, we can repeatedly load the inputs **Q** _,_ **K** and recompute the block of the attention matrix that we need, significantly reducing HBM access. As similar scenario happens in kernel machine learning: each element _𝐾𝑖𝑗_ of the _𝑁_ × _𝑁_ kernel matrix **K** is a function of two vectors of size _𝑑_ ≪ _𝑁_ , as it measures the similarity between two datapoints _𝑥𝑖_ and _𝑥 𝑗_ . The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. We hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs.

---

[referencia=5727fed78bddc701 score=0.026]
##### **Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

---

[referencia=a114e852aac1b2cb score=0.025]
## **2 Method** 

### **2.1 Uptraining** 

Generating a multi-query model from a multi-head model takes place in two steps: first, converting the checkpoint, and second, additional pre-training to allow the model to adapt to its new structure. Figure 1 shows the process for converting a multi-head checkpoint into a multi-query checkpoint. The projection matrices for key and value heads are mean pooled into single projection matrices, which we find works better than selecting a single key and value head or randomly initializing new key and value heads from scratch. 



Figure 1: Overview of conversion from multi-head to multi-query attention. Key and value projection matrices from all heads are mean pooled into a single head. 

The converted checkpoint is then pre-trained for 

> _†_ University of Southern California. Work done at Google Research. 



Figure 2: Overview of grouped-query method. Multi-head attention has H query, key, and value heads. Multi-query attention shares single key and value heads across all query heads. Grouped-query attention instead shares single key and value heads for each _group_ of query heads, interpolating between multi-head and multi-query attention. 

a small proportion _α_ of its original training steps on the same pre-training recipe.

---

[referencia=5727fed78bddc701 score=0.023]
In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses: 



However, the input to attention (matrices **Q** _,_ **K** _,_ **V** ) and the output **O** have size _𝑁𝑑_ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least Ω( _𝑁𝑑_ ) HBM accesses. This is a contradiction. □ 

_Proof of Theorem 5._ The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). Here we provide a sketch of the proof. 

We first analyze the IO complexity of standard attention backward pass. The inputs **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the outputs **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> are written to HBM. 

At each step of the standard attention backward pass, one needs to load inputs of size _𝑁𝑑_ or _𝑁_<sup>2</sup> from HBM, and needs to write the outputs of size _𝑁_<sup>2</sup> or _𝑁𝑑_ to HBM. This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

We now analyze the IO complexity of FlashAttention backward pass.

---

[referencia=5727fed78bddc701 score=0.021]
- **Sparse Training.** Our block-sparse FlashAttention can be seen as a step towards making sparse model 

- training more efficient. Sparse models have seen success in compressing models for inference (pruning) by sparsifying the weight matrices [23, 38, 39, 55, 76]. For model training, the lottery tickets hypothesis [28, 29, 30] suggests that there are a set of small sub-networks derived from a larger dense network that performs as well as the original dense network. Out block-sparse FlashAttention can also be seen as a fixed lottery ticket in the context of attention: we fix the sparsity pattern to be the butterfly pattern through training, and observe that it performs almost as well as the (dense) FlashAttention on the Long-range Arena tasks. **Efficient Transformer.** Transformer-based models have become the most widely-used architecture in 

- natural language processing [22] and computer vision [24, 91]. However, one of their computational bottlenecks is that their time and memory scales quadratic in the sequence length. There are numerous approaches to overcome this bottleneck, including approximation with hashing (i.e., sparse) such as Reformer [51] and Smyrf [19] and with low-rank approximation such as Performer [12, 54]. One can even combine sparse and low-rank approximation for better accuracy (e.g., Longformer [3], BigBird [92], Scatterbrain [9], Long-short transformer [94], Combiner [73]). Other approaches include compressing along the sequence dimension to attend to multiple tokens at once [52, 57, 79, 89]. One can also attend over the states from previous sequences to help lengthen the context (e.g., Transformer-XL [14] and Compressive Transformer [69]). We recommend the survey [81] for more details. 

- There are several lines of work on developing other modules instead of attention to model longer context. 

- HiPPO [35] and its extensions, most notably S4 [31, 36, 37] projects the history on a polynomial basis, allowing accurate reconstruction of the history through state-space models. They combine the strengths of CNNs (efficient training), RNNs (efficient inference), and continuous models (robust to change in sampling rates). LambdaNetworks [2], AFT [93] and FLASH [42] are other attempts at replacing attention in the context of image classification and language modeling.