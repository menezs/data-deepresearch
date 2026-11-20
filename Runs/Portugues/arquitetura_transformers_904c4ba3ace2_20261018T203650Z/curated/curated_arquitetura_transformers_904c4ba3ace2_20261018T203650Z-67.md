[referencia=5727fed78bddc701 score=0.881]
FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness Tri Dao<sup>†</sup> , Daniel Y. Fu<sup>†</sup> , Stefano Ermon<sup>†</sup> , Atri Rudra<sup>‡</sup> , and Christopher Ré<sup>†</sup> 

> †Department of Computer Science, Stanford University 

> ‡Department of Computer Science and Engineering, University at Buffalo, SUNY `{trid,danfu}@cs.stanford.edu` , `ermon@stanford.edu` , `atri@buffalo.edu` , `chrismre@cs.stanford.edu` 

June 24, 2022 

**Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IO-_ 

_aware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, 

an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention

---

[referencia=5727fed78bddc701 score=0.392]
and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy). 

**1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->

---

[referencia=5727fed78bddc701 score=0.248]
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

[referencia=5727fed78bddc701 score=0.229]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=5727fed78bddc701 score=0.173]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.165]
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

[referencia=5727fed78bddc701 score=0.109]
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|
|**Block-Sparse FlashAttention**|0.11|**0.12**|**0.16**|**0.38**|**1.20**|**2.34**|**4.69**|**9.10**|**18.74**|**37.04**|



Table 20: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.095]
|**Block-Sparse FlashAttention**|**0.30**|0.27|**0.29**|**0.59**|**1.50**|**2.94**|**5.82**|**11.85**|**23.98**|**47.61**|



Table 11: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.077]
## **3.3 Extension: Block-Sparse FlashAttention** 

We extend FlashAttention to approximate attention: we propose block-sparse FlashAttention, whose IO complexity is smaller than FlashAttention by a factor proportional to the sparsity. Given inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and a mask matrix **M**<sup>˜</sup> ∈{0 _,_ 1}<sup>_𝑁_×</sup><sup>_𝑁_</sup> , we want to compute: 



where ( **S** ⊙ 𝟙 **M** ˜ ) _𝑘𝑙_ = **S** _𝑘𝑙_ if **M**<sup>˜</sup> _𝑘𝑙_ = 1 and −∞ if **M** _𝑘𝑙_ = 0. We require **M**<sup>˜</sup> to have block form: for some block sizes _𝐵𝑟 , 𝐵𝑐_ , for all _𝑘, 𝑙_ , **M**<sup>˜</sup> _𝑘,𝑙_ = **M** _𝑖𝑗_ with _𝑖_ = ⌊ _𝑘_ / _𝐵𝑟_ ⌋ _, 𝑗_ = ⌊ _𝑙_ / _𝐵𝑐_ ⌋ for some **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> . 

6 

Given a predefined block sparsity mask **M** ∈{0 _,_ 1}<sup>_𝑁_/</sup><sup>_𝐵𝑟_×</sup><sup>_𝑁_/</sup><sup>_𝐵𝑐_</sup> we can easily adapt Algorithm 1 to only compute the nonzero blocks of the attention matrix. The algorithm is identical to Algorithm 1, except we skip zero blocks. We reproduce the algorithm description in Algorithm 5 in Appendix B.

---

[referencia=5727fed78bddc701 score=0.076]
|**Block-Sparse FlashAttention**|0.34|0.34|**0.36**|**0.69**|**1.85**|**3.89**|**7.16**|**14.85**|**30.46**|**60.03**|



Table 15: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.069]
|**Block-Sparse FlashAttention**|0.56|0.52|0.63|0.65|**0.61**|**0.96**|**1.69**|**3.02**|**5.69**|**11.77**|



Table 19: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.066]
|**Block-Sparse FlashAttention**|0.54|0.51|0.68|0.61|**0.67**|**1.10**|**1.89**|**3.71**|**7.18**|**14.41**|



Table 16: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.065]
|**Block-Sparse FlashAttention**|0.22|0.22|**0.26**|**0.57**|**1.55**|**3.13**|**5.98**|**12.21**|**23.49**|**47.85**|



32 

Table 14: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.064]
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

[referencia=5727fed78bddc701 score=0.062]
|**Block-Sparse FlashAttention**|0.05|**0.04**|**0.05**|**0.11**|**0.35**|**0.68**|**1.33**|**2.54**|**5.34**|**10.73**|



Table 13: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.054]
|**Block-Sparse FlashAttention**|0.91|0.83|0.94|**0.92**|**1.83**|**3.50**|**7.02**|**13.56**|**26.71**|**53.92**|



33 

Table 18: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.054]
|**Block-Sparse FlashAttention**|0.44|0.44|**0.45**|**0.89**|**1.95**|**4.12**|**7.64**|**16.60**|**32.73**|**64.11**|



Table 12: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.040]
Table 9: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=5727fed78bddc701 score=0.033]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.26|0.29|0.78|2.44|8.82|33.87|-|-|-|-|
|**Megatron**|0.29|0.30|0.80|2.59|8.86|-|-|-|-|-|
|**Reformer**|2.18|4.21|8.14|16.12|32.02|63.84|127.60|-|-|-|
|**Local Attention**|0.51|0.64|1.28|3.60|12.52|25.08|50.22|100.23|200.66|-|
|**Linformer**|0.69|0.76|0.69|0.80|2.04|3.88|7.67|15.04|30.11|63.15|
|**Smyrf**|1.24|2.49|4.77|9.42|18.65|37.12|74.15|148.35|-|-|
|**LSformer**|1.68|1.61|3.02|7.40|19.72|38.27|74.89|147.99|-|-|
|**Block Sparse**|1.24|1.25|2.04|2.91|6.78|19.67|-|-|-|-|
|**Longformer**|1.27|1.23|1.24|1.85|4.99|10.21|24.89|-|-|-|
|**BigBird**|1.43|1.50|1.44|1.69|5.25|10.86|26.26|-|-|-|
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|

---

[referencia=5727fed78bddc701 score=0.033]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.67|0.70|1.18|3.67|13.22|50.44|-|-|-|-|
|**Megatron**|0.74|0.65|1.23|3.80|13.21|-|-|-|-|-|
|**Reformer**|3.93|7.01|13.15|25.89|52.09|105.00|215.13|-|-|-|
|**Local Attention**|1.09|1.27|1.99|5.38|18.32|36.77|73.67|147.29|296.35|-|
|**Linformer**|1.31|1.25|1.30|1.29|3.20|6.10|11.93|23.39|46.72|100.52|
|**Smyrf**|2.98|4.23|7.78|15.12|29.96|59.45|118.60|237.02|-|-|
|**LSformer**|3.03|3.05|4.26|10.70|30.77|60.15|118.33|234.94|-|-|
|**Block Sparse**|2.39|2.40|3.31|5.02|12.25|35.94|-|-|-|-|
|**Longformer**|2.36|2.34|2.38|2.94|9.83|21.35|58.12|-|-|-|
|**BigBird**|2.35|2.35|2.37|3.25|10.36|22.57|60.63|-|-|-|
|**FlashAttention**|**0.31**|**0.31**|**0.73**|2.29|7.64|30.09|118.50|470.51|1876.08|7492.85|