[referencia=a7468c6851652691 score=0.056]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=5727fed78bddc701 score=0.052]
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

[referencia=5727fed78bddc701 score=0.048]
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|
|**Block-Sparse FlashAttention**|0.17|**0.17**|**0.17**|**0.40**|**1.10**|**2.04**|**4.43**|**9.33**|**18.28**|**37.31**|



Table 17: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length, **with dropout** . Best in **bold** , second best <u>underlined.</u>

---

[referencia=a7468c6851652691 score=0.045]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=5727fed78bddc701 score=0.040]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.44|0.46|1.53|5.33|20.34|79.87|-|-|-|-|
|**Megatron**|0.29|0.31|0.65|1.95|6.49|-|-|-|-|-|
|**Reformer**|2.31|4.47|8.68|17.20|34.14|68.09|136.02|-|-|-|
|**Local Attention**|0.51|0.62|1.30|3.81|13.33|26.72|53.41|106.82|214.15|-|
|**Linformer**|0.76|0.81|0.94|0.87|2.24|4.25|8.35|16.38|32.67|72.11|
|**Smyrf**|1.34|2.77|5.30|10.46|20.73|41.27|82.41|164.86|-|-|
|**LSformer**|1.66|1.61|3.09|7.42|19.68|38.35|74.92|147.86|-|-|
|**Block Sparse**|1.24|1.25|2.04|2.91|6.78|19.67|-|-|-|-|
|**Longformer**|1.27|1.23|1.24|1.85|4.99|10.21|24.89|-|-|-|
|**BigBird**|1.43|1.50|1.44|1.69|5.25|10.86|26.26|-|-|-|
|**FlashAttention**|**0.21**|**0.22**|0.62|1.84|5.77|22.25|86.21|338.91|1343.91|5361.09|

---

[referencia=5727fed78bddc701 score=0.039]
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

[referencia=5727fed78bddc701 score=0.035]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.37|0.49|1.66|5.81|22.32|87.67|-|-|-|-|
|**Megatron**|0.35|0.32|0.77|2.42|8.43|-|-|-|-|-|
|**Reformer**|2.37|4.59|8.91|17.68|35.13|70.05|140.01|-|-|-|
|**Local Attention**|0.55|0.62|1.49|4.03|13.78|27.61|55.20|110.27|221.40|-|
|**Linformer**|0.89|0.80|0.81|0.93|2.48|4.75|9.29|18.27|36.53|-|
|**Smyrf**|1.41|2.83|5.43|10.72|21.25|42.31|84.48|168.95|-|-|
|**LSformer**|1.75|1.76|3.01|7.50|20.07|39.08|76.39|150.82|-|-|
|**Block Sparse**|1.29|1.28|2.18|3.04|7.27|21.16|-|-|-|-|
|**Longformer**|1.27|1.31|1.29|2.04|5.24|10.74|25.95|-|-|-|
|**BigBird**|1.33|1.28|1.32|1.81|5.55|11.44|27.45|-|-|-|
|**FlashAttention**|**0.30**|**0.26**|0.68|2.02|6.84|26.89|105.70|418.96|1666.89|6660.44|

---

[referencia=5727fed78bddc701 score=0.034]
## **B.2 Memory-efficient backward pass** 

We derive the backward pass of attention and show that it can also be computed with linear memory. Rabe and Staats [66] suggests that the backward pass can be done without quadratic extra memory by applying gradient checkpointing to the memory-efficient forward pass. We instead derive the backward pass explicitly and show how it can be computed in a memory-efficient manner. 

Suppose that there is a scalar loss function _𝜙_ , and let the output gradient be **dO** ∈ R<sup>_𝑛_×</sup><sup>_𝑑_</sup> (where **dO** denotes _𝜕𝜙_<sup>Wewanttocomputetheinputgradients</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**∈R</sup><sup>_𝑛_×</sup><sup>_𝑑_(where</sup><sup>**dQ**</sup><sup>_,_</sup><sup>**dK**</sup><sup>_,_</sup><sup>**dV**denote</sup><sup>_𝜕𝜙𝜕𝜙𝜕𝜙_</sup> _𝜕_ **O**<sup>).</sup> _𝜕_ **Q**<sup>_,_</sup> _𝜕_ **K**<sup>_,_</sup> _𝜕_ **V** respectively). 

The gradient **dV** is easy to see. Applying reverse-mode autodiff by hand (aka the chain rule), we obtain (in matrix notation) **dV** = **P**<sup>_𝑇_</sup> **dO** . Thus: 



Since we already computed _𝐿𝑖_ , _𝑑𝑣 𝑗_ can be computed without extra memory by repeated summing. 

The gradients **dQ** and **dK** are a little more complicated. We go through the gradients **dP** and **dS** first. From Eq. (2), we have that **dP** = **dOV**<sup>_𝑇_</sup> , and so:

---

[referencia=5727fed78bddc701 score=0.033]
|**FlashAttention**|**0.11**|0.16|0.52|1.62|5.45|21.57|84.75|336.00|1338.56|5343.19|
|**Block-Sparse FlashAttention**|0.11|**0.12**|**0.16**|**0.38**|**1.20**|**2.34**|**4.69**|**9.10**|**18.74**|**37.04**|



Table 20: Forward pass + backward pass runtime (ms) of various exact/approximate/sparse attention mechanisms by sequence length. Best in **bold** , second best <u>underlined.</u>

---

[referencia=a7468c6851652691 score=0.033]
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

[referencia=5727fed78bddc701 score=0.032]
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

[referencia=5727fed78bddc701 score=0.032]
We also show that FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, we implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4× faster than even FlashAttention, scaling up to sequence length of 64k. We prove that block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. We discuss further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix 

2 

multiply) in Section 5. We open-source FlashAttention to make it easier to build on this primitive.<sup>1</sup> We empirically validate that FlashAttention speeds up model training and improves model quality by modeling longer context. We also benchmark the runtime and memory footprint of FlashAttention and 

block-sparse FlashAttention compared to prior attention implementations. 

• **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. We train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3× faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4× faster than baselines. 

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, which improves 

their quality and enables new capabilities. We observe a 0.7 improvement in perplexity on GPT-2 and 

6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256. 

• **Benchmarking Attention.** FlashAttention is up to 3× faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512,

---

[referencia=5727fed78bddc701 score=0.031]
|**Attention Method**|128|256|512|1024|2048|4096|8192|16384|32768|65536|
|---|---|---|---|---|---|---|---|---|---|---|
|**PyTorch Attention**|0.44|0.35|0.90|2.94|10.77|41.67|-|-|-|-|
|**Megatron**|0.28|0.33|0.92|2.94|10.80|-|-|-|-|-|
|**Reformer**|2.24|4.34|8.39|16.62|33.02|65.77|131.52|-|-|-|
|**Local Attention**|0.51|0.58|1.41|3.71|12.96|25.98|51.94|103.72|207.78|-|
|**Linformer**|0.84|0.74|0.79|0.85|2.28|4.37|8.66|17.02|33.78|-|
|**Smyrf**|1.27|2.56|4.90|9.66|19.16|38.13|76.17|152.39|-|-|
|**LSformer**|1.67|1.77|3.03|7.52|20.10|39.13|76.35|150.83|-|-|
|**Block Sparse**|1.27|1.36|2.15|3.04|7.27|21.18|-|-|-|-|
|**Longformer**|1.28|1.34|1.38|1.98|5.24|10.74|25.95|-|-|-|
|**BigBird**|1.48|1.47|1.50|1.81|5.57|11.38|27.43|-|-|-|
|**FlashAttention**|**0.15**|0.18|0.58|1.86|6.50|26.21|104.27|416.10|1661.92|6643.01|

---

[referencia=a7468c6851652691 score=0.030]
### **3.2.3 Applications of Attention in our Model** 

The Transformer uses multi-head attention in three different ways: 

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. 

- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2. 

### **3.3 Position-wise Feed-Forward Networks** 

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between. 

### FFN( _x_ ) = max(0 _, xW_ 1 + _b_ 1) _W_ 2 + _b_ 2 

(2) 

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is _d_ model = 512, and the inner-layer has dimensionality _dff_ = 2048.

---

[referencia=5727fed78bddc701 score=0.030]
while performing on par with standard attention (Section 4). 

**4 Experiments** 

We evaluate the impact of using FlashAttention to train Transformer models. We validate two claims about training time and model accuracy, and report attention runtime and memory benchmarks. 

• **Training Speed.** FlashAttention outperforms the MLPerf 1.1 [58] speed record for BERT by 15%, and speeds up GPT-2 up to 3× over HuggingFace [87] and 1 _._ 8× over Megatron [77] over standard Transformers. FlashAttention speeds up the long-range arena (LRA) benchmark 2.4×. 

• **Quality.** FlashAttention scales Transformers to longer sequences, yielding higher quality. FlashAttention trains GPT-2 with context length 4K faster than Megatron trains GPT-2 with context length 1K, while achieving 0.7 better perplexity. Modeling longer sequences yields 6.4 points of lift on two long- 

document classification tasks. Finally, FlashAttention yields the **first Transformer** that can achieve 

better-than-random performance on the challenging Path-X task (sequence length 16K), and block-sparse FlashAttention yields the **first sequence model** that we know of that can achieve better-than-random performance on Path-256 (sequence length 64K). 

• **Benchmarking Attention.** We measure the runtime and memory performance of FlashAttention 

and block-sparse FlashAttention based on sequence length. We confirm that the memory footprint of FlashAttention scales linearly with seq. length and is up to 3× faster than standard attention for common seq. lengths (up to 2K). We confirm that runtime of block-sparse FlashAttention scales linearly in seq. length and is faster than all existing approximate attention baselines. 

Additional experiment details are in Appendix E. 

**4.1 Faster Models with FlashAttention**

---

[referencia=a7468c6851652691 score=0.030]
### **3.4 Embeddings and Softmax** 

Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension _d_ model. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to [30]. In the embedding layers, we multiply those weights by<sup>_√_</sup> _d_ model. 

5 

Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. _n_ is the sequence length, _d_ is the representation dimension, _k_ is the kernel size of convolutions and _r_ the size of the neighborhood in restricted self-attention. 

|Layer Type|Complexity per Layer|Sequential<br>Operations|Maximum Path Length|
|---|---|---|---|
|Self-Attention|_O_(_n_<sup>2</sup> _· d_)|_O_(1)|_O_(1)|
|Recurrent|_O_(_n · d_<sup>2</sup>)|_O_(_n_)|_O_(_n_)|
|Convolutional|_O_(_k · n · d_<sup>2</sup>)|_O_(1)|_O_(_logk_(_n_))|
|Self-Attention (restricted)|_O_(_r · n · d_)|_O_(1)|_O_(_n/r_)|

---

[referencia=5727fed78bddc701 score=0.029]
## **3.1 An Efficient Attention Algorithm With Tiling and Recomputation** 

Given the inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, we aim to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> and write it to HBM. Our goal is to reduce the amount of HBM accesses (to sub-quadratic in _𝑁_ ). 

We apply two established techniques (tiling, recomputation) to overcome the technical challenge of computing exact attention in sub-quadratic HBM accesses. We describe this in Algorithm 1. The main idea is that we split the inputs **Q** _,_ **K** _,_ **V** into blocks, load them from slow HBM to fast SRAM, then compute the attention output with respect to those blocks. By scaling the output of each block by the right normalization factor before adding them up, we get the correct result at the end. 

**Tiling.** We compute attention by blocks. Softmax couples columns of **K** , so we decompose the large softmax with scaling [51, 60, 66]. For numerical stability, the softmax of vector _𝑥_ ∈ R<sup>_𝐵_</sup> is computed as: 



4

---

[referencia=5727fed78bddc701 score=0.027]
## **B.1 Memory-efficient forward pass** 

The main challenge in making attention memory-efficient is the softmax that couples the columns of **K** (and columns of **V** ). Our approach is to compute the softmax normalization constant separately to decouple the columns. This technique [60] has been used in the literature [51, 66] to show that attention computation does not need quadratic _extra_ memory (though the number of HBM accesses is still quadratic, resulting in slow run-time). 

For simplicity, we omit here the max-shifting step during softmax. The full algorithm in Appendix B.3 contains all the steps. 

Recall that given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> , we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



We have that _𝑆𝑖𝑗_ = _𝑞_<sup>_𝑇_</sup> _𝑖_<sup>_𝑘𝑗_where</sup><sup>_𝑞𝑖_and</sup><sup>_𝑘𝑗_arethe</sup><sup>_𝑖_-thand</sup><sup>_𝑗_-thcolumnsof</sup><sup>**Q**and</sup><sup>**K**respectively.Define</sup> the normalization constants of softmax: 



Let _𝑣 𝑗_ be the _𝑗_ -th column of **V** , then the _𝑖_ -th columns of the output is 



We see that once _𝐿𝑖_ is computed, we can compute _𝑜𝑖_ without extra memory by repeatedly summing _<u>𝑒</u>_<sup>_𝑞𝑇_</sup> _𝑖_<sup>_𝑘𝑗_</sup> _𝐿𝑖 𝑣 𝑗_ . Therefore the forward pass can be computed with _𝑂_ ( _𝑛_ ) extra memory:

---

[referencia=a7468c6851652691 score=0.026]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=5727fed78bddc701 score=0.026]
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