[referencia=5727fed78bddc701 score=0.948]
FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness Tri Dao<sup>†</sup> , Daniel Y. Fu<sup>†</sup> , Stefano Ermon<sup>†</sup> , Atri Rudra<sup>‡</sup> , and Christopher Ré<sup>†</sup> 

> †Department of Computer Science, Stanford University 

> ‡Department of Computer Science and Engineering, University at Buffalo, SUNY `{trid,danfu}@cs.stanford.edu` , `ermon@stanford.edu` , `atri@buffalo.edu` , `chrismre@cs.stanford.edu` 

June 24, 2022 

**Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IO-_ 

_aware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, 

an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention

---

[referencia=5727fed78bddc701 score=0.737]
and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy). 

**1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->

---

[referencia=5727fed78bddc701 score=0.673]
We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations. 

- **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

- **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

---

[referencia=5727fed78bddc701 score=0.524]
# **4 Experiments** 

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks. 

- **Training Speed.** FlashAttention outperforms the MLPerf 1.1 [58] speed record for BERT by 15%, and speeds up GPT-2 up to 3× over HuggingFace [87] and 1 _._ 8× over Megatron [77] over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4×. 

- **Quality.** FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two longdocument classification tasks. Finally, FlashAttention yields the **first Transformer** that can achieve better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the **first sequence model** that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K). 

- **Benchmarking Attention.** We measure the runtime and memory performance of FlashAttention and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3× faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines. 

- Additional experiment details are in Appendix E.

---

[referencia=5727fed78bddc701 score=0.422]
# **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=5727fed78bddc701 score=0.312]
## **4.2 Better Models with Longer Sequences** 

**Language Modeling with Long Context.** The runtime and memory-efficiency of FlashAttention allow us to increase the context length of GPT-2 by 4× while still running faster than the optimized implementation from Megatron-LM. Table 4 shows that that GPT-2 with FlashAttention and context length 4K is still 30% faster than GPT-2 from Megatron with context length 1K, while achieving 0.7 better perplexity. 

Table 4: GPT-2 small with FlashAttention, with 4× larger context length compared to Megatron-LM, is still 30% faster while achieving 0.7 better perplexity. Training time on 8×A100 GPUs is reported. 

|Model implementations|Context length|OpenWebText (ppl)|Training time (speedup)|
|---|---|---|---|
|GPT-2 small - Megatron-LM|1k|18.2|4.7 days (1.0×)|
|GPT-2 small - FlashAttention|1k|18.2|**2.7 days (1.7**×**)**|
|GPT-2 small - FlashAttention|2k|17.6|3.0 days (1.6×)|
|GPT-2 small - FlashAttention|4k|**17.5**|3.6 days (1.3×)|



**Long Document Classification.** Training Transformers with longer sequences with FlashAttention improves performance on the MIMIC-III [47] and ECtHR [6, 7] datasets. MIMIC-III contains intensive care unit patient discharge summaries, each annotated with multiple labels. ECtHR contains legal cases from the 

> 3LRA accuracy results are known to be highly dependent on the tuning procedure [90]. Our reproduced baselines perform better than as reported in the original comparison [80]. 

8 



<!-- Start of picture text -->

---

[referencia=5727fed78bddc701 score=0.239]
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

[referencia=5727fed78bddc701 score=0.229]
> 3LRA accuracy results are known to be highly dependent on the tuning procedure [90]. Our reproduced baselines perform better than as reported in the original comparison [80]. 

8 



<!-- Start of picture text -->
Attention Runtime (Fwd Pass + Bwd Pass) Attention Memory Usage<br>10 2<br>Crossover Points 20 2x<br>10 1<br>10<br>20x<br>10 0<br>128 256 512 1024 2048 4096 8192 256 8K 16K 32K 64K<br>Sequence Length Sequence Length<br>FlashAttention PyTorch Attention Linformer Attention<br>Block-Sparse FlashAttention Megatron Attention OpenAI Sparse Attention<br>Runtime (ms)<br>Memory Footprint (GB)<br><!-- End of picture text -->

Figure 3: **Left:** runtime of forward pass + backward pass. **Right:** attention memory usage. 

European Court of Human Rights, each of which is mapped to articles of the Convention of Human Rights that were allegedly violaged. Both of these datasets contain very long text documents; the average number of tokens in MIMIC is 2,395 tokens, and the longest document contains 14,562 tokens, while the average and longest numbers in ECtHR are 2,197 and 49,392, respectively. We evaluate lift from increasing the sequence length of a pretrained RoBERTa model [56] (we repeat the positional embeddings, as in Beltagy et al. [3]). Table 5 shows that sequence length 16K outperforms length 512 by 4.3 points on MIMIC, and that length 8K outperforms length 512 by 8.5 points on ECtHR. The discrepancies may be due to subtle distribution shifts: MIMIC-III contains specialized medical text and thus may be more susceptible to a distribution shift in the document length, whereas ECtHR contains general language. 

Table 6: We report the first Transformer model that can achieve non-random performance on Path-X and Path-256. 

Table 5: Long Document performance (micro _𝐹_ 1) at different sequence lengths using FlashAttention.

---

[referencia=5727fed78bddc701 score=0.217]
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

[referencia=5727fed78bddc701 score=0.215]
**Sparse Training.** Our block-sparse FlashAttention can be seen as a step towards making sparse model training more efficient. Sparse models have seen success in compressing models for inference (pruning) by sparsifying the weight matrices [23, 38, 39, 55, 76]. For model training, the lottery tickets hypothesis [28, 29, 30] suggests that there are a set of small sub-networks derived from a larger dense network that performs as well as the original dense network. Out block-sparse FlashAttention can also be seen as a fixed lottery ticket in the context of attention: we fix the sparsity pattern to be the butterfly pattern through training, and observe that it performs almost as well as the (dense) FlashAttention on the Long-range Arena tasks. 

**Efficient Transformer.** Transformer-based models have become the most widely-used architecture in natural language processing [22] and computer vision [24, 91]. However, one of their computational bottlenecks is that their time and memory scales quadratic in the sequence length. There are numerous approaches to overcome this bottleneck, including approximation with hashing (i.e., sparse) such as Reformer [51] and Smyrf [19] and with low-rank approximation such as Performer [12, 54]. One can even combine sparse and low-rank approximation for better accuracy (e.g., Longformer [3], BigBird [92], Scatterbrain [9], Long-short transformer [94], Combiner [73]). Other approaches include compressing along the sequence dimension to attend to multiple tokens at once [52, 57, 79, 89]. One can also attend over the states from previous sequences to help lengthen the context (e.g., Transformer-XL [14] and Compressive Transformer [69]). We recommend the survey [81] for more details. 

There are several lines of work on developing other modules instead of attention to model longer context. HiPPO [35] and its extensions, most notably S4 [31, 36, 37] projects the history on a polynomial basis, allowing accurate reconstruction of the history through state-space models. They combine the strengths of CNNs (efficient training), RNNs (efficient inference), and continuous models (robust to change in sampling rates). LambdaNetworks [2], AFT [93] and FLASH [42] are other attempts at replacing attention in the context of image classification and language modeling.

---

[referencia=5727fed78bddc701 score=0.214]
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

[referencia=5727fed78bddc701 score=0.153]
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

[referencia=5727fed78bddc701 score=0.150]
|where softmax is applied row-wise.<br>Standard attention implementations materialize the matrices**S**and**P**to HBM, which takes_𝑂_(_𝑁_<sup>2</sup>) memory.<br>Often _𝑁_≫_𝑑_(e.g., for GPT2, _𝑁_=1024 and _𝑑_=64). We describe the standard attention implementation<br>in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of<br>memory accesses translates to slow wall-clock time.<br>This problem is exacerbated by other elementwise operations applied to the attention matrix, such as<br>masking applied to **S** or dropout applied to **P**. As a result, there have been many attempts to fuse several<br>elementwise operations, such as fusing masking with softmax [77].<br>In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic<br>in the sequence length _𝑁_. We also compare the number of FLOPs and number of HBM accesses of standard<br>attention and of our method (FlashAttention).|
|**Algorithm 0** Standard Attention Implementation|
|**Require:** Matrices **Q**_,_**K**_,_**V** ∈R<sup>_𝑁_×</sup><sup>_𝑑_</sup>in HBM.<br>1: Load **Q**_,_**K** by blocks from HBM, compute **S**=**QK**<sup>⊤</sup>, write **S** to HBM.<br>2: Read **S** from HBM, compute **P**=softmax(**S**), write **P** to HBM.<br>3: Load **P** and **V** by blocks from HBM, compute **O**=**PV**, write **O** to HBM.<br>4: Return **O**.|

---

[referencia=5727fed78bddc701 score=0.131]
Table 6: We report the first Transformer model that can achieve non-random performance on Path-X and Path-256. 

Table 5: Long Document performance (micro _𝐹_ 1) at different sequence lengths using FlashAttention. 

|ro 1) a <br>|ere<br>|se<br>|uenc|e en|s|sng|**Model**|Path-X|Path-256|
|---|---|---|---|---|---|---|---|---|---|
|FlashAtte|ntion.||||||Transformer<br>|||
||||||||Linformer [84]|||
||512|1024|2048|4096|8192|16384|Linear Attention [50]<br>Performer[12]|<br>|<br>|
|MIMIC-III [47]|52.8|50.7|51.7|54.6|56.4|**57.1**|<br>LocalAttention[80]|<br>|<br>|
|ECtHR [6]|72.2|74.3|77.1|78.6|**80.7**|79.2|<br>Reformer [51]|<br>|<br>|
||||||||SMYRF [19]|||
||||||||FlashAttention|**61.4**||
||||||||Block-sparse FlashAttention|56.0|**63.1**|

---

[referencia=5727fed78bddc701 score=0.096]
## **4.3 Benchmarking Attention** 

We vary sequence length and measure runtime and memory usage of FlashAttention and block-sparse FlashAttention against various attention baselines on one A100 GPU with 40 GB HBM, with dropout and a padding mask. We compare against reference implementations for exact attention, approximate attention, and sparse attention. We report a subset of baselines in the main body; Appendix E contains more baselines and full details. 

> 4Path-256 requires longer sequences but has relatively shorter paths than Path-X, so it is easier to obtain a higher accuracy. 

9 

**Runtime.** Figure 3 (left) reports the runtime in milliseconds of the forward + backward pass of FlashAttention and block-sparse FlashAttention compared to the baselines in exact, approximate, and sparse attention (exact numbers in Appendix E). Runtime grows quadratically with sequence length, but FlashAttention runs significantly faster than **exact attention** baselines, up to 3× faster than the PyTorch implementation. The runtimes of many approximate/sparse attention mechanisms grow linearly with sequence length, but FlashAttention still runs faster than approximate and sparse attention for short sequences due to fewer memory accesses. The **approximate attention** runtimes begin to cross over with FlashAttention at sequences between 512 and 1024. On the other hand, block-sparse FlashAttention is faster than all implementations of exact, sparse, and approximate attention that we know of, across all sequence lengths. 

**Memory Footprint.** Figure 3 (right) shows the memory footprint of FlashAttention and block-sparse FlashAttention compared to various exact, approximate, and sparse attention baselines. FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than **exact attention** baselines, and is more memory-efficient than the **approximate attention** baselines. All other algorithms except for Linformer run out of memory on an A100 GPU before 64K, and FlashAttention is still 2× more efficient than Linformer.

---

[referencia=5727fed78bddc701 score=0.084]
**Path-X and Path-256.** The Path-X and Path-256 benchmarks are challenging tasks from the long-range arena benchmark designed to test long context. The task is to classify whether two points in a black and white 128×128 (or 256×256) image have a path connecting them, and the images are fed to the transformer one pixel at a time. In prior work, all transformer models have either run out of memory, or only achieved random performance [80]. There has been a search for alternative architectures that can model such long context [37]. We present here the first result of Transformer models being able to solve Path-X and Path-256 (Table 6). We pretrain a transformer on Path-64, and then transfer to Path-X by spatially interpolating the positional embeddings. FlashAttention achieves 61.4 accuracy on Path-X. Additionally, block-sparse FlashAttention enables the Transformers to scale to sequence length 64K, achieving 63.1 accuracy<sup>4</sup> on Path-256.

---

[referencia=5727fed78bddc701 score=0.064]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.26|0.24|0.57|1.80|6.56|25.34|-|-|-|-|
|**Megatron**|0.27|0.27|0.56|1.88|6.56|-|-|-|-|-|
|**Reformer**|1.83|2.96|5.31|10.33|21.19|43.42|91.96|201.34|-|-|
|**Local Attention**|0.51|0.60|0.78|2.01|6.23|12.52|25.07|50.50|102.18|-|
|**Linformer**|0.47|0.37|0.49|**0.52**|1.37|2.65|5.12|10.13|20.25|44.16|
|**Smyrf**|2.12|2.01|3.15|5.97|11.83|23.36|46.48|92.72|-|-|
|**LSformer**|1.28|1.33|1.51|3.39|11.40|22.54|44.96|89.85|179.73|-|
|**Block Sparse**|1.03|1.00|1.72|2.39|5.96|17.88|-|-|-|-|
|**Longformer**|1.02|1.03|1.03|1.73|5.10|11.63|34.22|-|-|-|
|**BigBird**|0.99|1.03|1.01|1.58|5.36|12.27|35.56|-|-|-|
|**FlashAttention**|**0.10**|**0.10**|**0.22**|0.83|2.81|10.38|41.63|167.01|668.74|2678.11|

---

[referencia=5727fed78bddc701 score=0.062]
asymptotically improve on HBM accesses over all SRAM sizes. Proofs are in Appendix C. 

**Theorem 2.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _(Algorithm 1) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3.

---

[referencia=5727fed78bddc701 score=0.061]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.30|0.30|0.63|1.93|7.08|27.45|112.90|-|-|-|
|**Megatron**|0.45|0.41|0.43|1.52|5.80|-|-|-|-|-|
|**Reformer**|1.87|3.00|5.37|10.43|21.40|43.83|92.80|203.24|-|-|
|**Local Attention**|0.70|0.81|1.02|2.09|6.64|13.34|26.77|54.02|110.11|-|
|**Linformer**|0.63|0.50|0.67|0.65|1.36|2.60|5.04|9.92|19.69|43.47|
|**Smyrf**|2.38|2.32|3.76|7.16|14.14|28.09|55.98|111.73|-|-|
|**LSformer**|1.22|1.29|1.44|3.28|10.99|21.72|43.29|86.32|172.76|-|
|**Block Sparse**|0.96|1.04|1.66|2.16|5.41|16.15|-|-|-|-|
|**Longformer**|0.99|0.98|0.99|1.56|4.79|11.07|32.98|-|-|-|
|**BigBird**|0.96|1.02|1.02|1.48|5.05|11.59|34.16|-|-|-|
|**FlashAttention**|**0.03**|**0.04**|0.17|0.68|2.28|8.40|33.55|134.14|537.50|2150.88|

---

[referencia=5727fed78bddc701 score=0.059]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.21|0.22|0.43|1.27|4.32|16.47|67.77|-|-|-|
|**Megatron**|0.24|0.26|0.42|1.33|4.28|-|-|-|-|-|
|**Reformer**|1.77|2.82|5.01|9.74|20.03|41.11|87.39|192.40|-|-|
|**Local Attention**|0.48|0.57|0.80|1.90|5.76|11.56|23.13|46.65|94.74|-|
|**Linformer**|0.46|0.36|0.45|**0.50**|1.09|2.09|4.01|7.90|15.70|35.40|
|**Smyrf**|1.94|1.96|3.01|5.69|11.26|22.23|44.21|88.22|-|-|
|**LSformer**|1.21|1.34|1.34|3.31|11.01|21.71|43.27|86.32|172.85|-|
|**Block Sparse**|0.96|1.04|1.66|2.16|5.41|16.15|-|-|-|-|
|**Longformer**|0.99|0.98|0.99|1.56|4.79|11.07|32.98|-|-|-|
|**BigBird**|0.96|1.02|1.02|1.48|5.05|11.59|34.16|-|-|-|
|**FlashAttention**|**0.08**|**0.09**|**0.18**|0.68|2.40|8.42|33.54|134.03|535.95|2147.05|