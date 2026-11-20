[referencia=5727fed78bddc701 score=0.997]
We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations. 

- **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

- **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

---

[referencia=5727fed78bddc701 score=0.992]
## **4 Experiments** 

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks. 

- **Training Speed.** FlashAttention outperforms the MLPerf 1.1 [58] speed record for BERT by 15%, and speeds up GPT-2 up to 3× over HuggingFace [87] and 1 _._ 8× over Megatron [77] over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4×. 

- **Quality.** FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two longdocument classification tasks. Finally, FlashAttention yields the **first Transformer** that can achieve better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the **first sequence model** that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K). 

- **Benchmarking Attention.** We measure the runtime and memory performance of FlashAttention and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3× faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines. 

- Additional experiment details are in Appendix E.

---

[referencia=5727fed78bddc701 score=0.983]
##### **Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

---

[referencia=5727fed78bddc701 score=0.974]
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

[referencia=5727fed78bddc701 score=0.902]
### **4.1 Faster Models with FlashAttention** 

**BERT.** FlashAttention yields the fastest single-node BERT training speed that we know of. We train a BERT-large [22] model with FlashAttention on Wikipedia. Table 1 compares our training time to the implementation from Nvidia that set the training speed record for MLPerf 1.1 [58]. Our implementation is 15% faster. 

Table 1: Training time of BERT-large, starting from the same initialization provided by the MLPerf benchmark, to reach the target accuracy of 72.0% on masked language modeling. Averaged over 10 runs on 8×A100 GPUs. 

|BERT Implementation|Training time (minutes)|
|---|---|
|Nvidia MLPerf 1.1 [58]|20.0 ± 1.5|
|FlashAttention (ours)|**17.4** ± 1.4|



**GPT-2.** FlashAttention yields faster training times for GPT-2 [67] on the large OpenWebtext dataset [32] than the widely used HuggingFace [87] and Megatron-LM [77] implementations. Table 2 shows up to 3× endto-end speedup compared to Huggingface and 1.7× speedup compared to Megatron-LM. FlashAttention 

7 

achieves the same perplexity as the other two implementations, as we do not change the model definition. Appendix E includes plots of the validation perplexity throughout training, confirming that FlashAttention is as numerically stable as the baselines and produces the same training / validation curves. Table 2: GPT-2 small and medium using FlashAttention achieve up to 3× speed up compared to Huggingface implementation and up to 1.7× compared to Megatron-LM. Training time reported on 8×A100s GPUs.

---

[referencia=5727fed78bddc701 score=0.867]
### **3.2 Analysis: IO Complexity of FlashAttention** 

We analyze the IO complexity of FlashAttention, showing significant reduction in HBM accesses compared to standard attention. We also provide a lower bound, proving that no exact attention algorithm can 

> 2This style of aggregation is called _algebraic aggregation_ [33]. 

5 



<!-- Start of picture text -->
Effect of Block Size Sparsity Speedup<br>6 Dense<br>Attention Standard FlashAttention 6 150 FlashAttention<br>GFLOPs 66.6 75.2 4 Runtime 100<br>HBM R/W (GB) 40.3 4.4 2<br>Runtime (ms) 41.7 7.3 2 50<br>64 128 256 512 20 60<br>Block Size % Non-Zero Blocks<br>HBM<br>Accesses<br>Block-Sparse<br>FlashAttention<br>Fwd + Bwd (ms)<br>HBM Accesses (GB) Fwd Runtime (ms)<br><!-- End of picture text -->

Figure 2: **Left** : Forward + backward runtime of standard attention and FlashAttention for GPT-2 medium (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. HBM access is the primary factor affecting runtime. **Middle** : Forward runtime of FlashAttention (seq. length 1024, head dim. 64, 16 heads, batch size 64) on A100 GPU. Fewer HBM accesses result in faster runtime, up to a point. **Right** : The runtime (for seq. length 4K) of block-sparse FlashAttention is faster than FlashAttention by a factor proportional to the sparsity. 

asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C.

---

[referencia=5727fed78bddc701 score=0.861]
We propose FlashAttention, a new attention algorithm that computes exact attention with far fewer memory accesses. Our main goal is to avoid reading and writing the attention matrix to and from HBM. This requires (i) computing the softmax reduction without access to the whole input (ii) not storing the large intermediate attention matrix for the backward pass. We apply two well-established techniques to address these challenges. (i) We restructure the attention computation to split the input into blocks and make several passes over input blocks, thus incrementally performing the softmax reduction (also known as **tiling** ). (ii) We store the softmax normalization factor from the forward pass to quickly **recompute** attention on-chip in the backward pass, which is faster than the standard approach of reading the intermediate attention matrix from HBM. We implement FlashAttention in CUDA to achieve fine-grained control over memory access and fuse all the attention operations into one GPU kernel. Even with the increased FLOPs due to recomputation, our algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** —linear in sequence length—than standard attention, thanks to the massively reduced amount of HBM access. 

We analyze the IO complexity [1] of FlashAttention, proving that it requires _𝑂_ ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses where _𝑑_ is the head dimension and _𝑀_ is the size of SRAM, as compared to Ω( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) of standard attention. For typical values of _𝑑_ and _𝑀_ , FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9× fewer, as shown in Fig. 2). Moreover, we provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

---

[referencia=5727fed78bddc701 score=0.791]
### **E.2 GPT-2** 

We use the standard implementations of GPT-2 [67] from Huggingface `transformers` library and from Nvidia’s Megatron-LM repo. We follow the training recipe of the Megatron-LM repo. 

We use an effective batch size of 512, and use gradient accumulation to fit into available GPU memory. We use the AdamW optimizer, with learning rate 6e-4 for GPT-2 small and 1.5e-4 for GPT-2 medium, and weight decay of 0.1. All models are trained with the same hyperparameters for 400K steps. We run all implementations with mixed-precision training (PyTorch AMP). 

We use the Openwebtext dataset, with the GPT-2 BPE tokenizer. We randomly select 0.5% of the dataset as the validation set, with the rest being used as training set. This random selection of validation set is done once, and all models are evaluated on the same validation set. We train the model on 8×A100-40GB GPUs, and we measure the wall-clock training time. Training GPT-2 small takes between 2.7-9.5 days, and training GPT-2 medium takes between 6.9-21.0 days (Table 2). 

In Fig. 4, we plot of the validation perplexity throughout training of GPT-2 small/medium, using either HuggingFace implementation or our FlashAttention implementation. We see that FlashAttention behaves the same as the baseline implementation and the validation perplexity curves of the two implementations almost lie on top of each other. 

**Long Document Classification.** For MIMIC-III and ECtHR, we follow the hyperparameters of Dai et al. [13]. 

26 



<!-- Start of picture text -->
30<br>GPT-2-small HuggingFace<br>GPT-2-small FlashAttention<br>25 GPT-2-medium HuggingFace<br>GPT-2-medium FlashAttention<br>20<br>15<br>10<br>100k 200k 300k<br>Training steps<br>Val perplexity<br><!-- End of picture text -->

Figure 4: Validation perplexity of GPT-2 small/medium using two implementations. We confirm that FlashAttention yields the same validation curves as the baseline implementation from HuggingFace.

---

[referencia=5727fed78bddc701 score=0.770]
### **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=5727fed78bddc701 score=0.757]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=5727fed78bddc701 score=0.720]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=5727fed78bddc701 score=0.702]
> 3LRA accuracy results are known to be highly dependent on the tuning procedure [90]. Our reproduced baselines perform better than as reported in the original comparison [80]. 

8 



<!-- Start of picture text -->
Attention Runtime (Fwd Pass + Bwd Pass) Attention Memory Usage<br>10 2<br>Crossover Points 20 2x<br>10 1<br>10<br>20x<br>10 0<br>128 256 512 1024 2048 4096 8192 256 8K 16K 32K 64K<br>Sequence Length Sequence Length<br>FlashAttention PyTorch Attention Linformer Attention<br>Block-Sparse FlashAttention Megatron Attention OpenAI Sparse Attention<br>Runtime (ms)<br>Memory Footprint (GB)<br><!-- End of picture text -->

Figure 3: **Left:** runtime of forward pass + backward pass. **Right:** attention memory usage. 

European Court of Human Rights, each of which is mapped to articles of the Convention of Human Rights that were allegedly violaged. Both of these datasets contain very long text documents; the average number of tokens in MIMIC is 2,395 tokens, and the longest document contains 14,562 tokens, while the average and longest numbers in ECtHR are 2,197 and 49,392, respectively. We evaluate lift from increasing the sequence length of a pretrained RoBERTa model [56] (we repeat the positional embeddings, as in Beltagy et al. [3]). Table 5 shows that sequence length 16K outperforms length 512 by 4.3 points on MIMIC, and that length 8K outperforms length 512 by 8.5 points on ECtHR. The discrepancies may be due to subtle distribution shifts: MIMIC-III contains specialized medical text and thus may be more susceptible to a distribution shift in the document length, whereas ECtHR contains general language. 

Table 6: We report the first Transformer model that can achieve non-random performance on Path-X and Path-256. 

Table 5: Long Document performance (micro _𝐹_ 1) at different sequence lengths using FlashAttention.

---

[referencia=5727fed78bddc701 score=0.547]
# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness 

Tri Dao<sup>†</sup> , Daniel Y. Fu<sup>†</sup> , Stefano Ermon<sup>†</sup> , Atri Rudra<sup>‡</sup> , and Christopher Ré<sup>†</sup> 

> †Department of Computer Science, Stanford University 

> ‡Department of Computer Science and Engineering, University at Buffalo, SUNY 

`{trid,danfu}@cs.stanford.edu` , `ermon@stanford.edu` , `atri@buffalo.edu` , `chrismre@cs.stanford.edu` 

June 24, 2022

---

[referencia=5727fed78bddc701 score=0.534]
### **D.2 Potential Extensions** 

We discuss here a few potential extensions of the IO-aware approach to speed up deep learning training. **Multi-GPU Attention.** Large language models are trained on hundreds or thousands of GPUs, and one typically splits the attention computation between 4-8 GPUs on the same node [77]. This introduces another level of memory hierarchy: beside GPU SRAM and GPU HBM, we also have the HBM of other 

25 

GPUs. For very long sequences, the different GPUs on the same node can cooperate to compute attention by taking into account the asymmetry of different levels of memory hierarchy. 

**Sparse MLP layers.** Typical dense MLP layers are compute-bound and not memory-bound. To improve their efficiency, MLP layers with sparse weight matrices can be used [17]. However, many sparse MLP layers are instead memory-bound, and their speedup is often not proportional to the sparsity. We believe that an IO-aware implementation can alleviate this issue and realize the benefits of sparsity. We are excited about future work in this direction, to reduce the computational requirement of large models and improve their wall-block runtime. 

**Kernel machine learning.** Our approach in FlashAttention relies on the fact that the _𝑁_ × _𝑁_ attention matrix is a function of a low-rank matrix **QK**<sup>⊤</sup> (of rank _𝑑_ ≪ _𝑁_ ). As a result, we can repeatedly load the inputs **Q** _,_ **K** and recompute the block of the attention matrix that we need, significantly reducing HBM access. As similar scenario happens in kernel machine learning: each element _𝐾𝑖𝑗_ of the _𝑁_ × _𝑁_ kernel matrix **K** is a function of two vectors of size _𝑑_ ≪ _𝑁_ , as it measures the similarity between two datapoints _𝑥𝑖_ and _𝑥 𝑗_ . The KeOps library [8, 26] is a successful example of how reducing memory reads/writes can speed up kernel operations. We hope that this will motivate kernel methods that focus more on reducing IOs instead of just FLOPs.

---

[referencia=5727fed78bddc701 score=0.501]
asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

---

[referencia=5727fed78bddc701 score=0.487]
**Path-X and Path-256.** The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128×128 (or 256×256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance [80]. There has been a search for alternative architectures that can model such long context [37]. We present here the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). We pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings. FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy<sup>4</sup> on Path-256.

---

[referencia=5727fed78bddc701 score=0.482]
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

[referencia=5727fed78bddc701 score=0.464]
We also analyze the IO complexity of block-sparse FlashAttention. 

**Proposition 4.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Block-sparse_ FlashAttention _(Algorithm 5) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> _𝑠_ ) _HBM accesses where 𝑠 is the fraction of nonzero blocks in the block-sparsity mask._ 

We see that applying block-sparsity yields a direct improvement by the sparsity to the larger term in the IO complexity. For large sequence lengths _𝑁_ , _𝑠_ is often set to _𝑁_<sup>−1/2</sup> [11] or _𝑁_<sup>−1</sup> log _𝑁_ [3, 17, 92], resulting in Θ( _𝑁_ √ _𝑁_ ) or Θ( _𝑁_ log _𝑁_ ) IO complexity. For downstream experiments, we use the fixed butterfly sparsity pattern [17], which has been shown to be able to approximate arbitrary sparsity [16]. 

In Fig. 2 (right), we validate that as the sparsity increases, the runtime of block-sparse FlashAttention improves proportionally. On the LRA benchmark, block-sparse FlashAttention achieves 2.8× speedup, while performing on par with standard attention (Section 4).

---

[referencia=5727fed78bddc701 score=0.442]
### **E.5 Speedup On Different Hardware and Configurations** 

Speedup varies between different types of GPU types and generations depending on HBM bandwidth and SRAM size. In this section, we profile FlashAttention speedup on different GPUs and configurations. 



Figure 5: Speedup over standard PyTorch attention at different sequence lengths, on A100. 

**A100** Figure 5 shows speedup on an A100 GPU with batch size 8, head dimension 64, and 12 attention heads, across different sequence lengths. We generally see 2-4× speedup, and we see more speedup when using dropout and masking due to kernel fusion. 

28 



Figure 6: Speedup over standard PyTorch attention at different sequence lengths, on A100, with head dimension 128. 

**A100, Head Dimension 128** Speedup also changes when we increase the head dimension. Each block requires more memory, so we need to use smaller block sizes to fit into SRAM. Figure 6 shows speedup with head dimension 128 on an A100 (batch size 16, 12 heads). We see less speedup overall—but we can still see significant speedup (up to 3×) with a causal mask, where half the blocks are masked out. 



Figure 7: Speedup over standard PyTorch attention at different sequence lengths, on RTX 3090. 

**RTX 3090** Figure 7 shows speedup on an RTX 3090 GPU. Here, we use batch size 12 with 12 attention heads. We observe slightly higher speedups on the RTX 3090 (between 2.5-4.5×), since the memory bandwidth on an RTX 3090 is lower than on an A100 (roughly 900 GB/s vs. 1.5 TB/s). 

**T4** Figure 8 shows speedup on a T4 GPU. T4 SRAM is smaller than A100, so we need to make the block sizes smaller in FlashAttention. As a result, we observe less speedup on T4, which matches the IO complexity analysis in Section 3.2. T4 GPUs are commonly used for inference, so we also report speedup on the forward pass only. 

29

---

[referencia=5727fed78bddc701 score=0.340]
### **E.4 Comparison with Apex FMHA** 

We compare our method/implementation with Apex FMHA ( `https://github.com/NVIDIA/apex/tree/ master/apex/contrib/csrc/fmha` ). 

When we started this project, Apex FMHA was the fastest implementation of attention (that we knew of), tailored for short sequences of length at most 512. In fact, almost all MLPerf submissions for BERT training benchmark running on Nvidia GPUs use FMHA for their model code, as of MLPerf 1.1 [58]. Since 

27 

Table 7: Runtime (ms) of FlashAttention compared to FMHA by sequence length, with masking and dropout, measured on an A100-SXM4-40GB GPU. Batch size 64, 16 heads, head dimension 64 (i.e., BERT-large size). 

|**Attention Method**|128|256|512|
|---|---|---|---|
|**Apex FMHA forward**|0.10|0.29|1.14|
|**FlashAttention forward**|**0.08**|**0.22**|**0.81**|
|**Apex FMHA backward**|**0.17**|**0.52**|**1.81**|
|**FlashAttention backward**|0.20|0.53|2.00|
|**Apex FMHA forward + backward**|**0.27**|0.81|2.95|
|**FlashAttention forward + backward**|0.28|**0.75**|**2.81**|



FMHA targets BERT models, it only supports head dimension 64, and only runs on A100 GPUs. FMHA fuses the attention computation dropout(softmax(mask( **QK**<sup>⊤</sup> ))) **V** into one CUDA kernel. In the forward pass, it stores the attention matrix softmax(mask( **QK**<sup>_𝑇_</sup> )) to HBM to be used in gradient computation. As a result, it does not offer substantial memory saving (though for shorter sequences memory footprint is often not a primary concern).