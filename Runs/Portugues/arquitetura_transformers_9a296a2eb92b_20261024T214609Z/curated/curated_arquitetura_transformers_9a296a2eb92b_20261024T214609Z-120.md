[referencia=9cb658eb63c3853b score=0.095]
##### **Abstract** 

Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. Approximate attention methods have attempted to address this problem by trading off model quality to reduce the compute complexity, but often do not achieve wall-clock speedup. We argue that a missing principle is making attention algorithms _IOaware_ —accounting for reads and writes between levels of GPU memory. We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory (HBM) and GPU on-chip SRAM. We analyze the IO complexity of FlashAttention, showing that it requires fewer HBM accesses than standard attention, and is optimal for a range of SRAM sizes. We also extend FlashAttention to block-sparse attention, yielding an approximate attention algorithm that is faster than any existing approximate attention method. FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) compared to the MLPerf 1.1 training speed record, 3× speedup on GPT-2 (seq. length 1K), and 2.4× speedup on long-range arena (seq. length 1K-4K). FlashAttention and block-sparse FlashAttention enable longer context in Transformers, yielding higher quality models (0.7 better perplexity on GPT-2 and 6.4 points of lift on long-document classification) and entirely new capabilities: the first Transformers to achieve better-than-chance performance on the Path-X challenge (seq. length 16K, 61.4% accuracy) and Path-256 (seq. length 64K, 63.1% accuracy).

---

[referencia=9cb658eb63c3853b score=0.048]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.042]
## **1 Introduction** 

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length. An important question is whether making attention faster and more memory-efficient can help Transformer models address their runtime and memory challenges for long sequences. 

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These methods range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many of them do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO). 

In this paper, we argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left). On modern 

1 



<!-- Start of picture text -->
Outer Loop<br>K T :  d x N<br>Attention on GPT-2<br>Copy Block to  SRAM<br>Q:  N x d Outer Loop V:  N X d 15 Matmul<br>GPU SRAM: 19 TB/s (20 MB)<br>SRAM Dropout<br>GPU HBM: 1.5 TB/s (40 GB) Copy 10<br>HBM Compute  Block Softmax<br>on  SRAM<br>Main Memory(CPU DRAM) DRAM                (>1 TB): 12.8 GB/s Copy 5 Mask KernelFused<br>Matmul<br>Memory Hierarchy with Output to HBM 0<br>Bandwidth & Memory Size sm (QK T )V:  N x d PyTorch FlashAttention<br>Inner Loop<br>FlashAttention<br>TQK N x N :  Time (ms)<br>Inner Loop Outer Loop<br>Inner Loop<br><!-- End of picture text -->

---

[referencia=9cb658eb63c3853b score=0.041]
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|
|**Block-Sparse FlashAttention**|0.11|**0.12**|**0.16**|**0.38**|**1.20**|**2.34**|**4.69**|**9.10**|**18.74**|**37.04**|



Table 20: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.026]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> 

We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations.

---

[referencia=9cb658eb63c3853b score=0.021]
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

[referencia=9cb658eb63c3853b score=0.019]
|**Block-Sparse FlashAttention**|0.34|0.34|**0.36**|**0.69**|**1.85**|**3.89**|**7.16**|**14.85**|**30.46**|**60.03**|



Table 15: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.019]
|**Block-Sparse FlashAttention**|0.54|0.51|0.68|0.61|**0.67**|**1.10**|**1.89**|**3.71**|**7.18**|**14.41**|



Table 16: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.018]
|**Block-Sparse FlashAttention**|**0.30**|0.27|**0.29**|**0.59**|**1.50**|**2.94**|**5.82**|**11.85**|**23.98**|**47.61**|



Table 11: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.018]
|**Block-Sparse FlashAttention**|0.22|0.22|**0.26**|**0.57**|**1.55**|**3.13**|**5.98**|**12.21**|**23.49**|**47.85**|



32 

Table 14: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.017]
|**Block-Sparse FlashAttention**|0.05|**0.04**|**0.05**|**0.11**|**0.35**|**0.68**|**1.33**|**2.54**|**5.34**|**10.73**|



Table 13: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.017]
|**Block-Sparse FlashAttention**|0.44|0.44|**0.45**|**0.89**|**1.95**|**4.12**|**7.64**|**16.60**|**32.73**|**64.11**|



Table 12: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.017]
|**Block-Sparse FlashAttention**|0.91|0.83|0.94|**0.92**|**1.83**|**3.50**|**7.02**|**13.56**|**26.71**|**53.92**|



33 

Table 18: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.016]
We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and block-sparse FlashAttention compared to prior attention implementations. 

- **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

- **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that we know of.

---

[referencia=9cb658eb63c3853b score=0.015]
- [79] Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, and Armand Joulin. Adaptive attention span in transformers. In _Proceedings of the Annual Meeting of the Association for Computational Linguistics_ , 2019. 

- [80] Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena: A benchmark for efficient transformers. In _International Conference on Learning Representations_ , 2020. 

- [81] Yi Tay, Mostafa Dehghani, Dara Bahri, and Donald Metzler. Efficient transformers: A survey. _arXiv preprint arXiv:2009.06732_ , 2020. 

- [82] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. _Advances in neural information processing systems_ , 30, 2017. 

- [83] Hongyu Wang, Shuming Ma, Li Dong, Shaohan Huang, Dongdong Zhang, and Furu Wei. Deepnet: Scaling transformers to 1,000 layers. _arXiv preprint arXiv:2203.00555_ , 2022. 

- [84] Sinong Wang, Belinda Z Li, Madian Khabsa, Han Fang, and Hao Ma. Linformer: Self-attention with linear complexity. _arXiv preprint arXiv:2006.04768_ , 2020. 

- [85] Samuel Williams, Andrew Waterman, and David Patterson. Roofline: an insightful visual performance model for multicore architectures. _Communications of the ACM_ , 52(4):65–76, 2009. 

- [86] Michael E Wolf and Monica S Lam. A data locality optimizing algorithm. In _Proceedings of the ACM SIGPLAN 1991 conference on Programming language design and implementation_ , pages 30–44, 1991. 

15

---

[referencia=9cb658eb63c3853b score=0.012]
Table 9: Forward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout and masking** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.011]
|**Block-Sparse FlashAttention**|0.56|0.52|0.63|0.65|**0.61**|**0.96**|**1.69**|**3.02**|**5.69**|**11.77**|



Table 19: Backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=9cb658eb63c3853b score=0.009]
In the regime of _𝑀_ = Θ( _𝑁𝑑_ ), this results in the number of HBM accesses: 



However, the input to attention (matrices **Q** _,_ **K** _,_ **V** ) and the output **O** have size _𝑁𝑑_ and they start out being in HBM, so if the algorithm computes exact attention it must incur at least Ω( _𝑁𝑑_ ) HBM accesses. This is a contradiction. □ 

_Proof of Theorem 5._ The IO complexity of the attention backward is very similar to the IO complexity of the attention forward (Theorem 2). Here we provide a sketch of the proof. 

We first analyze the IO complexity of standard attention backward pass. The inputs **Q** _,_ **K** _,_ **V** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the outputs **dQ** _,_ **dK** _,_ **dV** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> are written to HBM. 

At each step of the standard attention backward pass, one needs to load inputs of size _𝑁𝑑_ or _𝑁_<sup>2</sup> from HBM, and needs to write the outputs of size _𝑁_<sup>2</sup> or _𝑁𝑑_ to HBM. This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

We now analyze the IO complexity of FlashAttention backward pass.

---

[referencia=9cb658eb63c3853b score=0.008]
## **B Algorithm Details** 

We first derive the forward and backward passes of attention and show that they can be computed in a memory-efficient manner (requiring extra memory linear instead of quadratic in the sequence length). Though they reduce the amount of extra memory required, naively they still incur quadratic HBM accesses, resulting in slower execution speed. We describe the FlashAttention algorithm to implement both the forward 

17 

and the backward passes on GPUs that reduces HBM accesses, leading to both faster runtime and smaller memory footprint.

---

[referencia=9cb658eb63c3853b score=0.008]
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