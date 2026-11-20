[referencia=dfc666458a07fb9c score=0.959]
### **3.2 Scaling up to 1B Tokens** 

We verify the feasibility of scaling to 1B tokens with the modern distributed systems. Starting from 8K, we gradually scale the sequence length until the limit of GPU memory. We reduce the batch size accordingly to keep the number of tokens per batch at 1 billion. Each model of different sequence 

7 

- **Github** 

- **Model Length Batch 2K 8K 32K** 

- Transformer [VSP<sup>+</sup> 17] 2K 256 4.24 5.07 11.29 Sparse Transformer [CGRS19] 4.39 3.35 8.79 8K 64 

- **LONGNET (ours)** 4.23 3.24 3.36 Sparse Transformer [CGRS19] 4.85 3.73 19.77 16K 32 

- **LONGNET (ours)** 4.27 3.26 3.31 

|Sparse Transformer [CGRS19]|32K|16|5.15|4.00|3.64|
|---|---|---|---|---|---|
|**LONGNET (ours)**|||4.37|3.33|3.01|



Table 2: Perplexity of language models for LONGNET and the baselines. 

lengths has up to 3 segment lengths, which are 2,048, the number of tokens per device, and the sequence length. We compute the average speed in the forward propagation for 10 different runs. Figure 5 reports the runtime of vanilla attention and our dilated attention. Both of them are implemented with FlashAttention Kernel for saving memory and improving speed. It shows that dilated attention can successfully scale up the sequence length with almost constant latency. By partitioning the sequence dimension, it can leverage the distributed systems to scale the sequence length to 1 billion tokens. In contrast, vanilla attention suffers from the quadratic dependency on the sequence length. Its latency dramatically increases as the length grows. Moreover, there is no distributed algorithm for vanilla attention to break sequence length limitation. This proves the advantage of the linear complexity as well as the distributed algorithm for LONGNET. 

**4 Experiments on Language Modeling** 

**4.1 Setup**

---

[referencia=dfc666458a07fb9c score=0.906]
## **Abstract** 

Scaling sequence length has become a critical demand in the era of large language models. However, existing methods struggle with either computational complexity or model expressivity, rendering the maximum sequence length restricted. To address this issue, we introduce LONGNET, a Transformer variant that can scale sequence length to more than 1 billion tokens, without sacrificing the performance on shorter sequences. Specifically, we propose dilated attention, which expands the attentive field exponentially as the distance grows. LONGNET has significant advantages: 1) it has a linear computation complexity and a logarithm dependency between any two tokens in a sequence; 2) it can be served as a distributed trainer for extremely long sequences; 3) its dilated attention is a drop-in replacement for standard attention, which can be seamlessly integrated with the existing Transformer-based optimization. Experiments results demonstrate that LONGNET yields strong performance on both long-sequence modeling and general language tasks. Our work opens up new possibilities for modeling very long sequences, e.g., treating a whole corpus or even the entire Internet as a sequence. Code is available at `https://aka.ms/LongNet` . 



<!-- Start of picture text -->
1000<br>LongNet (1B)<br>800<br>600<br>400<br>Memorizing<br>Transformers (262K) RMT (1M)<br>200<br>Sparse Transformer  Reformer (64K)<br>(12K)<br>GPT (512)<br>0<br>2017 2018 2019 2020 2021 2022 2023 2024<br>Millions<br>Length<br><!-- End of picture text -->

Figure 1: Trend of Transformer sequence lengths over time. 

> ∗ Equal contribution. † Corresponding author.

---

[referencia=dfc666458a07fb9c score=0.902]
_Oi_ = softmax( _QiKi_<sup>_T_)</sup><sup>_V_</sup> _i_ (6) 

ˆ _Oi_ = { _Oi,j_ ∣ _j_ mod _r_ = 0; 0∣ _j_ mod _r_ ≠ 0} (7) 

_O_ = [ _O_<sup>ˆ</sup> 0 _, O_<sup>ˆ</sup> 1 _, ..., O_<sup>ˆ</sup><sup>_<u>N</u>_</sup> _w_<sup>−1]</sup> (8) 

In the implementation, the dilated attention can be transformed into dense attention between a gathering operation over the input ( _Q, K, V_ ) and a scattering operation over the output _Oi_ , so it can directly reuse any optimization for vanilla attention (e.g., flash attention [DFE<sup>+</sup> 22]). Dilated attention can significantly reduce the computation cost by a factor of<sup>_<u>N</u>_</sup> _w_<sup>_r_2 over the vanilla attention.</sup> 

3 



<!-- Start of picture text -->
Segment Length: 4 Segment Length: 8  Segment Length: 16<br>Dilated Rate: 1 Dilated Rate: 2 Dilated Rate: 4<br><!-- End of picture text -->

Figure 2: Building blocks of dilated attention used in LONGNET. It consists of a series of attention patterns for modeling both short-range and long-range dependency. The number of attention patterns can be extended according to the sequence length. 

In practice, the segment size _w_ trades the globality of attention for efficiency, while the dilation with a size _r_ reduces the computation cost by approximating the attention matrix. To capture both long-range and short-range information efficiently, we implement a mixture of dilated attentions with different segment sizes and dilation rates { _ri, wi_ }<sup>_k_</sup> :

---

[referencia=dfc666458a07fb9c score=0.894]
**4 Experiments on Language Modeling** 

**4.1 Setup** 

We implement LONGNET on language modeling. The backbone architecture is MAGNETO [WMH<sup>+</sup> 22] with XPOS [SDP<sup>+</sup> 22] relative position encoding, except that we replace the standard attention with our dilated attention. We use the base-size configuration of MAGNETO, which has a hidden dimension of 768, 12 attention heads, and 12 decoder layers. We pre-train the model with The Stack dataset [KLA<sup>+</sup> 22], a source code collection in over 300 programming languages. The data is preprocessed with the tiktoken tokenizer<sup>2</sup> with `cl100k_base` encoding. The models are trained with a batch size of 0.5M tokens for 300K steps. More details regarding the hyperparameters can be found in the appendix. All experiments are conducted based on the _torchscale_ [MWH<sup>+</sup> 22] codebase. 

**4.2 Results** 

We compare LONGNET with both vanilla Transformer and sparse Transformers. The differences among the architectures are the attention layers, while the others remain the same. We scale the sequence length of these models from 2K to 32K, while reducing the batch size to keep the number of tokens per batch constant. For LONGNET, we use segment lengths of _w_ = {2048 _,_ 4096 _,_ 8192 _,_ 16384 _,_ 32768}, and the dilated ratios are _r_ = {1 _,_ 2 _,_ 4 _,_ 6 _,_ 12}. We implement the fixed pattern for sparse attention as in [CGRS19] with multiple heads attending to distinct subblocks. The block size is set to 2048. We adjust their sparse ratios to match the computation flops with LONGNET so that the comparison is fair. The attention layers in vanilla Transformers are dense and fully connected, so the computation cost is much higher. Due to the computation constraints, we only scale it up to 32K sequence length. All of our implementations of attention variants are based on FlashAttention<sup>3</sup> for training efficiency. We customize the flash attention kernels for both sparse attention and dilated attention. 

> 2 `https://github.com/openai/tiktoken`

---

[referencia=dfc666458a07fb9c score=0.792]
### **4.5 Long Context Prompting** 

Prompting is an essential method to guide and provide additional information to the language models. We conduct experiments to verify whether LONGNET can benefit from a longer context window for prompting. Specifically, we reserve a piece of prefixes as the prompt and test the perplexity of its suffixes. We gradually scale the length of the prompt from 2K to 32K. For a fair comparison, we keep the suffixes the same, while increasing the length of the prefixes to the maximum lengths of the models. The results on the test set are reported in Figure 7(b). It shows that the test loss of LONGNET gradually decreases as the context window grows. This demonstrates the superiority of LONGNET in fully leveraging the long context to improve the language model. 

## **5 Conclusion and Future Work** 

We present LONGNET, a Transformer variant that can scale the sequence length to 1 billion tokens and beyond, with no loss in shorter sequences. The core of LONGNET is dilated attention, which reduces the computation complexity from quadratic to linear. LONGNET can be served as a distributed trainer that parallelizes the training of a sequence across multiple GPU devices. Experiments show that LONGNET has superior performance over the strong baselines on modeling both long and short sequences. In the future, we will extend LONGNET to support more tasks, e.g., multimodal large language modeling [HDW<sup>+</sup> 23, PWD<sup>+</sup> 23], BEiT pretraining [BDPW22, PDB<sup>+</sup> 22, WBD<sup>+</sup> 23], and genomic data modeling. 

**Acknowledgement** We would like to acknowledge Yuqing Xia and Jilong Xue for the early exploration of the flash attention kernel.

---

[referencia=dfc666458a07fb9c score=0.785]
Table 1: Comparison of computation complexity among different methods. _N_ is the sequence length and _d_ is the hidden dimension. 

**In this work, we successfully scale the sequence length to 1 billion tokens** . Our solution is LONGNET, which replaces the attention of vanilla Transformers with a novel component named dilated attention. The general design principle is - _attention allocation decreases exponentially as the distance between tokens grows_ . We prove that it obtains a linear computation complexity and a logarithm dependency between tokens. This deals with the contradiction between limited attention resources and the accessibility to every token. In the implementation, LONGNET can be transformed into a dense Transformer, which seamlessly supports the off-the-shelf optimization for Transformers (e.g., kernel fusion, quantization, and distributed training). Taking advantage of the linear complexity, LONGNET can parallelize the training across nodes, breaking the constraint of both computation and memory with a distributed algorithm. This allows us to efficiently scale up the sequence length to 1B 

2 

tokens with nearly constant runtime (see Figure 5), while vanilla Transformer suffers from quadratic complexity. 

**2 LONGNET 2.1 Preliminary** 

The core of Transformers [VSP<sup>+</sup> 17] is self-attention, which maps a query and a set of keys and values to output. Given the inputs _Q, K, V_ ∈ R<sup>_N_×</sup><sup>_d_</sup> , it computes the outputs _O_ with 

_O_ = softmax( _QK_<sup>_T_</sup> ) _V_ (1) 

Self-attention struggles with long sequences, due to its quadratic dependency on the sequence length. One query would attend to all keys and values, leading to computational inefficiencies. 

Sparse attention alleviates this issue by restricting the query’s access to a subset of keys and values. The key of sparse attention is the sparse attention pattern _S_ ∈ {0 _,_ 1}<sup>_N_×</sup><sup>_N_</sup> , which determines specific keys and values that the query _Q_ can attend to. 

_O_ = softmax( _QK_<sup>_T_</sup> ⊙ 1 _S_ ) _V_ (2)

---

[referencia=dfc666458a07fb9c score=0.779]
## **3 LONGNET as a Distributed Trainer: Scaling up to 1B Tokens** 

Although the computation complexity of dilated attention has been greatly reduced to _O_ ( _Nd_ ), it is infeasible to scale the sequence length to the million level on a single GPU device due to the computation and memory constraints. There are some distributed training algorithms for large-scale model training, such as model parallelism [SPP<sup>+</sup> 19], sequence parallelism [LXLY21, KCL<sup>+</sup> 22], and pipeline parallelism [HCB<sup>+</sup> 19]. However, they are insufficient for LONGNET especially when the sequence dimension is extremely large.

---

[referencia=dfc666458a07fb9c score=0.770]
### **2.4 Computational Complexity and Token Dependency** 

Given dilated attention with a segment size and dilation rate of ( _r, w_ ), each query-key-value pair is sparsified from ( _Q, K, V_ ) ∈ R<sup>_N_×</sup><sup>_d_</sup> to ( _Q, K, V_ ) ∈ R _<u>wr</u>_<sup>×</sup><sup>_d_</sup> , so the flops of the attention computation are estimated as: 



We further extend it to dilated attention with multiple segment sizes and dilation rates. The flops can be written as: 



With the segment sizes and dilation rates in Equation (11) and Equation (12), the flops are given by 



where _w_ 0 is a predefined constant and _α_ is the common ratio for geometric sequences _w_ and _r_ . Therefore, the computation complexity of dilated attention is approximate to _O_ ( _Nd_ ). 

5 



<!-- Start of picture text -->
GPU 1 GPU 2<br>𝑂1 𝑂2<br>෩𝐾 ෨𝑉<br>All gather<br>𝑄෨1 ෩𝐾1 𝑉෨1 ෩𝐾2 𝑉෨2 ෨𝑄2<br>Sparsify<br>𝑄1 𝐾1 𝑉1 𝐾2 𝑉2 𝑄2<br>Project<br>𝑋1 𝑋2<br>Split<br>𝑋<br><!-- End of picture text -->

Figure 4: Distributed training of LONGNET on two GPU devices. It parallelizes the training by partitioning the sequence dimension. The computation and communication costs are nearly constant as the number of devices grows. 

Moreover, the information of each tokens can be propagated to a maximum distance of _D_ : 



where _l_ is the length of the propagated path. Therefore, the maximum path length of a sequence with _N_ tokens can be estimated as: 



This proves that the token dependency is approximate to _O_ (log _N_ ).

---

[referencia=dfc666458a07fb9c score=0.752]
### **4.4 Scaling up Model Size** 

An important property of large language models is that the loss scales as a power law with compute. To verify whether LONGNET still follows the similar scaling law, we train a series of models with different model sizes, from 125 million to 2.7 billion parameters. The 2.7B model is trained with 

9 



<!-- Start of picture text -->
2.6 125M LongNet 2.2 LongNet<br>2.4 350M 2.1<br>760M<br>2.2<br>2.0<br>2.0<br>1.9<br>1.8<br>1.8<br>1.6<br>1.4 1.7<br>1.2 2.7B 1.6<br>10 16 10 17 10 18 1K 2K 4K 8K 16K 32K<br>FLOPs Context Window<br>(a) (b)<br>Test Loss Test Loss<br><!-- End of picture text -->

Figure 7: **Left:** Test loss of LONGNET with an increasing model size. The scaling curve follows a similar law to the vanilla Transformers. **Right:** Test loss of LONGNET using different context windows. A longer context window yields better language modeling. 

300B tokens, while the rest digest about 40B tokens. Figure 7(a) plots the scaling curve of LONGNET regarding the compute. We compute the perplexity on the same test set. The amount of compute is estimated by calculating the total flops of matrix multiplication during training. It proves that LONGNET can still follow the power law. This implies that the dense Transformer is not a prerequisite for scaling the language models. Additionally, the scalability and the efficiency are both obtained by LONGNET.

---

[referencia=dfc666458a07fb9c score=0.705]
### **3.1 Distributed Algorithm** 

We take advantage of the linear computation complexity of LONGNET for the distributed training of sequence dimension. Without loss of generality, Figure 4 presents our distributed algorithm on two GPUs, which can be further scaled to an arbitrary number of devices. We start by splitting the input sequence along the sequence dimension. Each sequence is put on one device separately: 



Then, they are projected into queries, keys, and values on the two devices: 

6 



<!-- Start of picture text -->
Dilated attention w/ FlashAttention<br>Vanilla attention w/ FlashAttention<br>5000<br>4000<br>3000<br>2000<br>1000<br>8K 16K 32K 64K 128K 512K 2M 8M 32M 128M 1B<br>Sequence Length<br>Runtime (ms)<br><!-- End of picture text -->

Figure 5: Runtime of our dilated attention and vanilla attention. Both are equipped with FlashAttention [DFE<sup>+</sup> 22]. 



For the segment length _wi_ ≤ _l_ (where _l_ is the sequence length on the local device), we compute the attention locally with Equation (3) to Equation (8). For the segment length _wi_ > _l_ , the keys and values are distributed across different devices. Therefore, we collect the key-value pairs before computing the attention. We use Equation (3) to Equation (5) to sparsify the { _Q, K, V_ } into { _Q, K, V_ }. An all-gather operation is implemented to collect the key-value pairs: 



Note that the all-gather operation in the backward becomes a reduce-scatter operation. Different from vanilla attention, both sizes of _Ki_ and _Vi_ are independent of the sequence length _N_ , making the communication cost constant. 

Finally, we compute the cross-attention with the local queries _Qi_ and the global key-value pairs { _K, V_ }. The formulation is written as: 



The concatenation of the outputs across different devices becomes the final attention output: 



The distributed algorithm described above is orthogonal to other parallelisms, including data parallelism which partitions the batch dimension, model parallelism which partitions the hidden dimension, and pipeline parallelism which partitions the layers.

---

[referencia=dfc666458a07fb9c score=0.669]
Another strand of scaling the sequence length is to decrease the complexity of Transformers, i.e., the quadratic complexity of self-attention. Implementing sliding windows or convolution modules over the attention is a straightforward way to make the complexity nearly linear. Nevertheless, this sacrifices the ability to recall the early tokens, forgetting the prompts at the very beginning of the sequence. Sparse attention reduces the computation by sparsifying the attention matrix, preserving the possibility of recalling long-distant information. For example, [CGRS19] obtains _O_ ( _N_ ~~√~~ _Nd_ ) time complexity with a fixed sparse pattern. Besides the heuristic patterns [ZGD<sup>+</sup> 20, BPC20], the learnable patterns prove to be useful for sparse attention [KKL20, ALdJ<sup>+</sup> 23]. There are also some other efficient Transformer-based variants, including low-rank attention [WLK<sup>+</sup> 20, WCL<sup>+</sup> 20], kernel-based methods [KVPF20, CLD<sup>+</sup> 21, QHS<sup>+</sup> 22], downsampling approaches [LLK<sup>+</sup> 19, JGB<sup>+</sup> 21, MKW<sup>+</sup> 21], recurrent models [DYY<sup>+</sup> 19, BKB23], and retrieval-based methods [WRHS22, WDC<sup>+</sup> 23]. Yet, none has been scaled to 1 billion tokens (see Figure 1). 

|**Method**|**Computation Complexity**|
|---|---|
|Recurrent|_O_(_Nd_<sup>2</sup>)<br>|
|Vanilla Attention|_O_(_N_ <sup>2</sup>_d_)<br>|
|Sparse Attention|_O_(_N_<br>√<br>_Nd_)|
|**Dilated Attention (This Work)**|_O_(_Nd_)|



Table 1: Comparison of computation complexity among different methods. _N_ is the sequence length and _d_ is the hidden dimension.

---

[referencia=dfc666458a07fb9c score=0.488]
# **LONGNET: Scaling Transformers to 1,000,000,000 Tokens** 

**Jiayu Ding**<sup>♣∗</sup> **Shuming Ma**<sup>♠∗</sup> **Li Dong**<sup>♠</sup> **Xingxing Zhang**<sup>♠</sup> **Shaohan Huang**<sup>♠</sup> **Wenhui Wang**<sup>♠</sup> **Nanning Zheng**<sup>♣†</sup> **Furu Wei**<sup>♠†</sup> 

♠ Microsoft Research 

♣ Xi’an Jiaotong University https://aka.ms/GeneralAI

---

[referencia=dfc666458a07fb9c score=0.382]
_O_ = softmax( _QK_<sup>_T_</sup> ⊙ 1 _S_ ) _V_ (2) 

For example, the fixed pattern of sparse Transformer [CGRS19] is composed of a local pattern and a strided pattern. The sequence is divided into blocks of length _l_ . The local pattern allows one query to attend to tokens within the same block, while strided pattern allows one query to attend to the last _c_ tokens of each block. Formally, the local pattern _Si_ (1) = { _j_ ∣⌊ _j_ / _l_ ⌋ = ⌊ _i_ / _l_ ⌋}, and the strided pattern _Si_ (2) = { _j_ ∣ _j_ mod _l_ ∈ { _t, t_ + 1 _, ..., l_ }}. **2.2 Dilated Attention** 

Figure 2 illustrates the overview of dilated attention. Dilated attention splits the input ( _Q_ , _K_ , _V_ ) into _<u>N</u>_ segments {( _Qi, Ki, Vi_ )} _w_ equally with a segment length _w_ . Each segment is then sparsified along the sequence dimension by selecting the rows with an interval _r_ . The computation can be written as: 

_Qi_ = [ _Qiw, Qiw_ + _r, Qiw_ +2 _r, ..., Q_ ( _i_ +1) _w_ −1] (3) 

_Ki_ = [ _Kiw, Kiw_ + _r, Kiw_ +2 _r, ..., K_ ( _i_ +1) _w_ −1] (4) 

_Vi_ = [ _Viw, Viw_ + _r, Viw_ +2 _r, ..., V_ ( _i_ +1) _w_ −1] (5) 

_<u>N</u>_ The sparsified segments {( _Qi, Ki, Vi_ )} _w_ are fed into the attention in parallel, after which are scattered and concatenated as the output _O_ : 

_Oi_ = softmax( _QiKi_<sup>_T_)</sup><sup>_V_</sup> _i_ (6)

---

[referencia=dfc666458a07fb9c score=0.344]
where _si_ denotes the denominator of the attention softmax for _O_ ∣ _ri,wi_ . Note that the computations for { _O_ ∣ _ri,wi_ }<sup>_k_</sup> are in parallel because there is no computation dependency among them. Experiments show that dynamic weights calculated by the denominator of the attention softmax are better than learnable fixed weights. For a query attends to keys in different dilated attentions, our method to mix dilated attentions is equivalent to gather keys in different parts and calculate softmax together. 

Intuitively, the local attention should be precisely computed, while the global attention can be approximate. Therefore, we set a larger _wi_ with a bigger _ri_ . Moreover, we gradually increase the _wi_ for each attention until it reaches the maximum length _N_ or the number of attention patterns _k_ : 



4 



<!-- Start of picture text -->
1 st  head 2 nd  head 3 rd  head 4 th  head<br>Segment Length: 8<br>Dilated Rate: 2<br>Heads: 4<br><!-- End of picture text -->

Figure 3: Dilated attention with multiple heads. The attention patterns differ among heads by shifting the position successively. 



In practice, we set _w_ and _r_ to geometric sequences for an exponential attentive field. 

### **2.3 Multi-Head Dilated Attention** 

As shown in Figure 3, we differ in the computation among different heads by sparsifying different parts of the query-key-value pairs. Specifically, for the _j_ -th head, we have an offset _sj_ = _j_ mod _r_ when selecting the ( _Q, K, V_ ): 







Following the vanilla multi-head attention, the outputs of different heads are concatenated into a final output. The rest of the computation remains the same as the single-head counterpart in Section 2.2.

---

[referencia=dfc666458a07fb9c score=0.211]
> 2 `https://github.com/openai/tiktoken` 

> 3 `https://github.com/HazyResearch/flash-attention/tree/main` 

8 



<!-- Start of picture text -->
2K<br>Transformer<br>LongNet<br>10<br>8<br>6<br>4<br>8K<br>8K16K 16K<br>32K<br>4 × 10 16 6 × 10 16 10 17<br>FLOPs<br>Test PPL<br><!-- End of picture text -->

Figure 6: Test perplexity of LONGNET and dense Transformers using different sequence lengths during training. LONGNET outperforms dense Transformers with a lower perplexity and a significantly smaller amount of computation. 

Table 2 summarizes the results of these models on the Stack dataset. We use perplexity as the evaluation metric. The models are tested with different sequence lengths, ranging from 2K to 32K. When the input is longer than the maximum length that the models support, we implement blockwise causal attention (BCA) [SDP<sup>+</sup> 22], a state-of-the-art extrapolation method for language model inference. Besides, we remove the absolute position encoding. Primarily, the results demonstrate that increasing the sequence length during training generally leads to a better language model. Secondly, the extrapolation of sequence length in inference does not apply to the case when the length is much larger than the model supports. Finally, LONGNET consistently outperforms the baseline models, proving its effectiveness in language modeling.

---

[referencia=dfc666458a07fb9c score=0.093]
### **4.3 Scaling Curves of Sequence Length** 

Previous work [KMH<sup>+</sup> 20] has shown that language models follow some scaling laws by increasing parameters or training tokens. We are interested in the performance of language models when the context length is scaled up during training. We test the losses with inputs of a mixture of different lengths, from 1K to 32K. We use blockwise causal attention during inference to improve the generalization of sequence lengths. 

Figure 6 plots the scaling curves of sequence length for both vanilla Transformers and LONGNET. We estimate the amount of compute by calculating the total flops of matrix multiplication. The results show that both vanilla Transformers and LONGNET benefit from a larger context length during training. However, LONGNET can scale up the context length more efficiently, achieving a lower test loss with a smaller amount of computing. This demonstrates the advantage of longer training input over extrapolation. In conclusion, our experiments show that LONGNET is a more efficient way to scale up the context length in language models. This is because LONGNET can learn longer-range dependencies more effectively.

---

[referencia=dfc666458a07fb9c score=0.041]
[CGRS19] Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. _ArXiv_ , abs/1904.10509, 2019. 

[CLD<sup>+</sup> 21] Krzysztof Marcin Choromanski, Valerii Likhosherstov, David Dohan, Xingyou Song, Andreea Gane, Tamás Sarlós, Peter Hawkins, Jared Quincy Davis, Afroz Mohiuddin, Lukasz Kaiser, David Benjamin Belanger, Lucy J. Colwell, and Adrian Weller. Rethinking attention with performers. In _9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021_ . OpenReview.net, 2021. 



<!-- Start of picture text -->
[CND + 22] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Many Others, Jeff Dean, Slav<br>Petrov, and Noah Fiedel. PaLM: Scaling language modeling with Pathways. ArXiv ,<br>abs/2204.02311, 2022.<br>[DDM + 23] Mostafa Dehghani, Josip Djolonga, Basil Mustafa, Piotr Padlewski, Jonathan Heek,<br>Justin Gilmer, Many Others, Xiaohua Zhai, Daniel Keysers, Jeremiah Harmsen, and Neil<br>Houlsby. Scaling vision transformers to 22 billion parameters. CoRR , abs/2302.05442,<br>2023.<br>[DFE + 22] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. Flashattention:<br>Fast and memory-efficient exact attention with io-awareness. In  NeurIPS , 2022.<br><!-- End of picture text -->

[DYY<sup>+</sup> 19] Zihang Dai, Zhilin Yang, Yiming Yang, Jaime G. Carbonell, Quoc Viet Le, and Ruslan Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. In Anna Korhonen, David R. Traum, and Lluís Màrquez, editors, _Proceedings_

---

[referencia=dfc666458a07fb9c score=0.012]
## **References** 

- [ALdJ<sup>+</sup> 23] Joshua Ainslie, Tao Lei, Michiel de Jong, Santiago Ontañón, Siddhartha Brahma, Yury Zemlyanskiy, David C. Uthus, Mandy Guo, James Lee-Thorp, Yi Tay, Yun-Hsuan Sung, and Sumit Sanghai. CoLT5: Faster long-range transformers with conditional computation. _CoRR_ , abs/2303.09752, 2023. 

10 

- [BDPW22] Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. BEiT: BERT pre-training of image transformers. In _International Conference on Learning Representations_ , 2022. 

- [BKB23] Aydar Bulatov, Yuri Kuratov, and Mikhail S. Burtsev. Scaling transformer to 1m tokens and beyond with RMT. _CoRR_ , abs/2304.11062, 2023. 

[BMR<sup>+</sup> 20] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark 

Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners. In _NeurIPS 2020_ , 2020. [BPC20] Iz Beltagy, Matthew E. Peters, and Arman Cohan. Longformer: The long-document transformer. _CoRR_ , abs/2004.05150, 2020. 

[CGRS19] Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. _ArXiv_ , abs/1904.10509, 2019.

---

[referencia=dfc666458a07fb9c score=0.010]
- [QHS<sup>+</sup> 22] Zhen Qin, Xiaodong Han, Weixuan Sun, Dongxu Li, Lingpeng Kong, Nick Barnes, and Yiran Zhong. The devil in linear transformer. In Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang, editors, _Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, EMNLP 2022, Abu Dhabi, United Arab Emirates, December 7-11, 2022_ , pages 7025–7041. Association for Computational Linguistics, 2022. 

- [SDP<sup>+</sup> 22] Yutao Sun, Li Dong, Barun Patra, Shuming Ma, Shaohan Huang, Alon Benhaim, Vishrav Chaudhary, Xia Song, and Furu Wei. A length-extrapolatable transformer. _CoRR_ , abs/2212.10554, 2022. 

- [SPP<sup>+</sup> 19] Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. Megatron-lm: Training multi-billion parameter language models using model parallelism. _CoRR_ , abs/1909.08053, 2019. 

- [SWL23] Jimmy T. H. Smith, Andrew Warrington, and Scott W. Linderman. Simplified state space layers for sequence modeling. In _The Eleventh International Conference on Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023_ . OpenReview.net, 2023. 

- [TDA<sup>+</sup> 21] Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, and Donald Metzler. Long range arena : A benchmark for efficient transformers. In _9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021_ . OpenReview.net, 2021.

---

[referencia=dfc666458a07fb9c score=0.009]
## **A Hyperparameters** 

|**Hyperparameters**|**Value**|
|---|---|
|Layers|12|
|Hidden size|768|
|FFN size|3072|
|Heads|12|
|Learning rate|6e-4|
|LR scheduler|Polynomial decay|
|Warm-up steps|750|
|Tokens per batch|500K|
|Adam_β_|(0.9, 0.98)|
|Training steps|300K|
|Gradient clipping|2.0|
|Dropout|0.0|
|Weight decay|0.01|



Table 3: Hyperparamters used for the models in Table 2. 

|**Parameters**|**Layers**|**Hidden**|**Heads**|**Learning Rate**|**Batch Size**|
|---|---|---|---|---|---|
|125M|12|768|12|6e-4|500K|
|350M|24|1024|16|6e-4|500K|
|760M|24|1536|16|6e-4|500K|
|2.7B|32|2560|32|2e-4|4M|



Table 4: Hyperparamters used for the experiments in Figure 7(a). 

15