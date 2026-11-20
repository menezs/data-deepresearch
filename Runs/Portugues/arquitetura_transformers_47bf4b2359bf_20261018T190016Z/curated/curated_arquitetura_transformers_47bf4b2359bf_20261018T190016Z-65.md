[referencia=a7468c6851652691 score=0.031]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=5727fed78bddc701 score=0.029]
# **C Proofs** 

_Proof of Theorem 1._ We first count the number of FLOPs and extra memory required. 

The dominating FLOPs are from matrix multiplication. In the inner loop, (Algorithm 1 line 9), we compute **Q** _𝑖_ **K**<sup>⊤</sup> _𝑗_<sup>∈R</sup><sup>_𝐵𝑟_×</sup><sup>_𝐵𝑐_for</sup><sup>**Q**</sup><sup>_𝑖_∈R</sup><sup>_𝐵𝑟_×</sup><sup>_𝑑_and</sup><sup>**K**</sup><sup>_𝑗_∈R</sup><sup>_𝐵𝑐_×</sup><sup>_𝑑_,whichtakes</sup><sup>_𝑂_(</sup><sup>_𝐵𝑟𝐵𝑐𝑑_)FLOPs.Wealsocompute</sup> (Algorithm 1 line 12) **P**<sup>˜</sup> _𝑖𝑗_ **V** _𝑗_ ∈ R<sup>_𝐵𝑟_×</sup><sup>_𝑑_</sup> for **P**<sup>˜</sup> _𝑖𝑗_ ∈ R<sup>_𝐵𝑟_×</sup><sup>_𝐵𝑐_</sup> and **V** _𝑗_ ∈ R<sup>_𝐵𝑐_×</sup><sup>_𝑑_</sup> , which takes _𝑂_ ( _𝐵𝑟 𝐵𝑐 𝑑_ ) FLOPs. We execute the inner loops _𝑇𝑐𝑇𝑟_ = � _𝐵𝑁𝑐_ �� _𝐵𝑁𝑟_ � times. Therefore the total number of FLOPs is 



In terms of extra memory required, we see that we need _𝑂_ ( _𝑁_ ) memory to store the statistics ( _ℓ, 𝑚_ ).

---

[referencia=a7468c6851652691 score=0.029]
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

[referencia=5727fed78bddc701 score=0.017]
</sup> to HBM. 22: On chip, compute **dK**<sup>˜</sup> _𝑗_ ← **dK**<sup>˜</sup> _𝑗_ + _𝜏_ **dS**<sup>⊤</sup> _𝑖𝑗_<sup>**Q**</sup><sup>_𝑖_∈R</sup><sup>_𝐵𝑐_×</sup><sup>_𝑑_.</sup> 23: **end for** ˜ ˜ 24: Write **dK** _𝑗_ ← **dK** _𝑗 ,_ **dV** _𝑗_ ← **dV** _𝑗_ to HBM. 25: **end for** 

- 26: Return **dQ** _,_ **dK** _,_ **dV** . 

We see that similar to the forward pass, the backward pass performs _𝑂_ ( _𝑁_<sup>2</sup> ) FLOPs and only requires _𝑂_ ( _𝑁_ ) extra memory beyond inputs, output, output gradient, and input gradients. 

We analyze the IO-complexity of the backward pass, similar to the forward pass (Theorem 2). 

**Theorem 5.** _Let 𝑁 be the sequence length, 𝑑 be the head dimension, and 𝑀 be size of SRAM with 𝑑_ ≤ _𝑀_ ≤ _𝑁𝑑. Standard attention (Algorithm 0) backward pass requires_ Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) _HBM accesses, while_ FlashAttention _backward pass (Algorithm 4) requires_ Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) _HBM accesses._ 

The proof is in Appendix C. 

21

---

[referencia=a7468c6851652691 score=0.012]
## **7 Conclusion** 

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. 

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. 

The code we used to train and evaluate our models is available at `https://github.com/ tensorflow/tensor2tensor` . 

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

---

[referencia=5727fed78bddc701 score=0.009]
## **2.2 Standard Attention Implementation** 

Given input sequences **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> where _𝑁_ is the sequence length and _𝑑_ is the head dimension, we want to compute the attention output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> : 



where softmax is applied row-wise. 

Standard attention implementations materialize the matrices **S** and **P** to HBM, which takes _𝑂_ ( _𝑁_<sup>2</sup> ) memory. Often _𝑁_ ≫ _𝑑_ (e.g., for GPT2, _𝑁_ = 1024 and _𝑑_ = 64). We describe the standard attention implementation in Algorithm 0. As some or most of the operations are memory-bound (e.g., softmax), the large number of memory accesses translates to slow wall-clock time. 

This problem is exacerbated by other elementwise operations applied to the attention matrix, such as masking applied to **S** or dropout applied to **P** . As a result, there have been many attempts to fuse several elementwise operations, such as fusing masking with softmax [77]. 

In Section 3.2, we will show that the standard attention implementation performs HBM accesses quadratic in the sequence length _𝑁_ . We also compare the number of FLOPs and number of HBM accesses of standard attention and of our method (FlashAttention). 

**Algorithm 0** Standard Attention Implementation 

**Require:** Matrices **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM.

---

[referencia=5727fed78bddc701 score=0.006]
**Require:** Matrices **Q** _,_ **K** _,_ **V** _,_ **O** _,_ **dO** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> in HBM, vectors _ℓ, 𝑚_ ∈ R<sup>_𝑁_</sup> in HBM, on-chip SRAM of size _𝑀_ , softmax scaling constant _𝜏_ ∈ R, masking function mask, dropout probability _𝑝_ drop, pseudo-random number generator state R from the forward pass. 1: Set the pseudo-random number generator state to R. 2: Set block sizes _𝐵𝑐_ = <u>�</u> 4 _<u>𝑀𝑑</u>_ � _, 𝐵𝑟_ = min<sup>��</sup> 4<sup>_<u>𝑀</u>_</sup> _𝑑_ � _, 𝑑_<sup>�</sup> . 3: Divide **Q** into _𝑇𝑟_ = � _𝐵𝑁𝑟_ � blocks **Q** 1 _, . . . ,_ **Q** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, and divide **K** _,_ **V** in to _𝑇𝑐_ = � _𝐵𝑁𝑐_ � blocks **K** 1 _, . . . ,_ **K** _𝑇𝑐_ and **V** 1 _, . . . ,_ **V** _𝑇𝑐_ , of size _𝐵𝑐_ × _𝑑_ each. 4: Divide **O** into _𝑇𝑟_ blocks **O** _𝑖, . . . ,_ **O** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, divide **dO** into _𝑇𝑟_ blocks **dO** _𝑖, . . . ,_ **dO** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_

---

[referencia=a7468c6851652691 score=0.005]
### **5.4 Regularization** 

We employ three types of regularization during training: 

7 

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost. 

||BL|EU|Training C|ost (FLOPs)|
|---|---|---|---|---|
|Model|||||
||EN-DE|EN-FR|EN-DE|EN-FR|
|ByteNet [18]|23.75||||
|Deep-Att + PosUnk [39]||39.2||1_._0_·_10<sup>20</sup>|
|<br>GNMT + RL [38]|24.6|39.92|2_._3_·_10<sup>19</sup>|1_._4_·_10<sup>20</sup>|
|ConvS2S [9]|25.16|40.46|9_._6_·_10<sup>18</sup>|1_._5_·_10<sup>20</sup>|
|MoE[32]|26.03|40.56|2_._0_·_10<sup>19</sup>|1_._2_·_10<sup>20</sup>|
|Deep-Att + PosUnk Ensemble [39]||40.4||8_._0_·_10<sup>20</sup>|
|GNMT + RL Ensemble [38]|26.30|41.16|1_._8_·_10<sup>20</sup>|1_._1_·_10<sup>21</sup>|
|ConvS2S Ensemble[9]|26.36|**41.29**|7_._7_·_10<sup>19</sup>|1_._2_·_10<sup>21</sup>|
|Transformer (base model)|27.3|38.1|**3****_._3****_·_**|**10**<sup>**18**</sup>|
|Transformer (big)|**28.4**|**41.8**|2_._3_·_|10<sup>19</sup>|

---

[referencia=5727fed78bddc701 score=0.005]
### _arithmetic intensity_ [85], which is the number of arithmetic operations per byte of memory access. 

1. Compute-bound: the time taken by the operation is determined by how many arithmetic operations there 

are, while time accessing HBM is much smaller. Typical examples are matrix multiply with large inner dimension, and convolution with large number of channels. 

2. Memory-bound: the time taken by the operation is determined by the number of memory accesses, while time spent in computation is much smaller. Examples include most other operations: elementwise (e.g., activation, dropout), and reduction (e.g., sum, softmax, batch norm, layer norm). 

**Kernel fusion.** The most common approach to accelerate memory-bound operations is kernel fusion: if there are multiple operations applied to the same input, the input can be loaded once from HBM, instead of multiple times for each operation. Compilers can automatically fuse many elementwise operations [53, 65, 75]. 

> 1FlashAttention code is available at `https://github.com/HazyResearch/flash-attention` 

3 

However, in the context of model training, the intermediate values still need to be written to HBM to save for the backward pass, reducing the effectiveness of naive kernel fusion.

---

[referencia=a7468c6851652691 score=0.005]
### **3.5 Positional Encoding** 

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension _d_ model as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [9]. 

In this work, we use sine and cosine functions of different frequencies: 



where _pos_ is the position and _i_ is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 _π_ to 10000 _·_ 2 _π_ . We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset _k_ , _PEpos_ + _k_ can be represented as a linear function of _PEpos_ . 

We also experimented with using learned positional embeddings [9] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

---

[referencia=5727fed78bddc701 score=0.004]
For typical values of _𝑑_ (64-128) and _𝑀_ (around 100KB), _𝑑_<sup>2</sup> is many times smaller than _𝑀_ , and thus FlashAttention requires many times fewer HBM accesses than standard implementation. This leads to both faster execution and lower memory footprint, which we validate in Section 4.3. 

The main idea of the proof is that given the SRAM size of _𝑀_ , we can load blocks of **K** _,_ **V** of size Θ( _𝑀_ ) each (Algorithm 1 line 6). For each block of **K** and **V** , we iterate over all blocks of **Q** (Algorithm 1 line 8) to compute the intermediate values, resulting in Θ( _𝑁𝑑𝑀_<sup>−1</sup> ) passes over **Q** . Each pass loads Θ( _𝑁𝑑_ ) elements, which amounts to Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses. We similarly prove that the backward pass of standard attention requires Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses while the backward pass of FlashAttention requires Θ( _𝑁_<sup>2</sup> _𝑑_<sup>2</sup> _𝑀_<sup>−1</sup> ) HBM accesses (Appendix B). 

We prove a lower-bound: one cannot asymptotically improve on the number of HBM accesses for all values of _𝑀_ (the SRAM size) when computing exact attention.

---

[referencia=a7468c6851652691 score=0.004]
||_N_|_d_model|_d_ff|_h_|_dk_|_dv_|_Pdrop_|_ϵls_|train<br>steps|PPL<br>(dev)|BLEU<br>(dev)|params<br>_×_10<sup>6</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|base|6|512|2048|8|64|64|0.1|0.1|100K|4.92|25.8|65|
|||||1|512|512||||5.29|24.9||
|A||||4|128|128||||5.00|25.5||
|()||||16|32|32||||4.91|25.8||
|||||32|16|16||||5.01|25.4||
||||||16|||||5.16|25.1|58|
|(B)|||||32|||||5.01|25.4|60|
||2|||||||||6.11|23.7|36|
||4|||||||||5.19|25.3|50|
||8|||||||||4.88|25.5|80|
|(C)||256|||32|32||||5.75|24.5|28|
|||1024|||128|128||||4.66|26.0|168|
||||1024|||||||5.12|25.4|53|
||||4096|||||||4.75|26.2|90|
||||||||0.0|||5.77|24.6||
|D|||||||0.2|||4.95|25.5||
|()||||||||0.0||4.67|25.3||
|||||||||0.2||5.47|25.7||
|(E)||posi|tional e|mbedd|ingins|tead of|sinusoi|ds||4.92|25.7||
|big|6|1024|4096|16|||0.3||300K|**4.33**|**26.4**|213|



development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3.

---

[referencia=5727fed78bddc701 score=0.003]
We then see that the claim is also true for _𝑗_ + 1. By induction, the claim is true for all _𝑗_ = 0 _, . . . ,𝑇𝑐_ . When _𝑗_ = _𝑇𝑐_ , we conclude that the final value of **O** in HBM is softmax( **S** ) **V** = softmax( **QK**<sup>⊤</sup> ) **V** . 

_Proof of Theorem 2._ We first analyze the IO complexity of standard attention implementation. The inputs **Q** _,_ **K** _,_ **V** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> reside in HBM, and the at the end of the algorithm the output **O** ∈ R<sup>_𝑁_×</sup><sup>_𝑑_</sup> is written to HBM. In the first step of computing the matrix multiply **S** = **QK**<sup>⊤</sup> , the inputs **Q** _,_ **K** are read from HBM and the output **S** ∈ R<sup>_𝑁_×</sup><sup>_𝑁_</sup> is written to HBM (Algorithm 0 line 1). This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses. 

In the second step of computing **P** = softmax( **S** ), the input **S** is read from HBM and the output **P** is written to HBM (Algorithm 0 line 2). This incurs Θ( _𝑁_<sup>2</sup> ) HBM accesses. 

In the last step of computing **O** = **PV** , the inputs **P** _,_ **V** are read from global memory and the output **O** is written to HBM (Algorithm 0 line 3). This incurs Θ( _𝑁𝑑_ + _𝑁_<sup>2</sup> ) HBM accesses.

---

[referencia=5727fed78bddc701 score=0.003]
> 3: Divide **Q** into _𝑇𝑟_ = � _𝐵𝑁𝑟_ � blocks **Q** 1 _, . . . ,_ **Q** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, and divide **K** _,_ **V** in to _𝑇𝑐_ = � _𝐵𝑁𝑐_ � blocks **K** 1 _, . . . ,_ **K** _𝑇𝑐_ and **V** 1 _, . . . ,_ **V** _𝑇𝑐_ , of size _𝐵𝑐_ × _𝑑_ each. 

> 4: Divide **O** into _𝑇𝑟_ blocks **O** _𝑖, . . . ,_ **O** _𝑇𝑟_ of size _𝐵𝑟_ × _𝑑_ each, divide _ℓ_ into _𝑇𝑟_ blocks _ℓ𝑖, . . . , ℓ𝑇𝑟_ of size _𝐵𝑟_ each, 

divide _𝑚_ into _𝑇𝑟_ blocks _𝑚_ 1 _, . . . , 𝑚𝑇𝑟_ of size _𝐵𝑟_ each. 5: **for** 1 ≤ _𝑗_ ≤ _𝑇𝑐_ **do** 6: Load **K** _𝑗 ,_ **V** _𝑗_ from HBM to on-chip SRAM. 7: **for** 1 ≤ _𝑖_ ≤ _𝑇𝑟_ **do**

---

[referencia=5727fed78bddc701 score=0.002]
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

[referencia=5727fed78bddc701 score=0.002]
In terms of extra memory required, we see that we need _𝑂_ ( _𝑁_ ) memory to store the statistics ( _ℓ, 𝑚_ ). 

We now prove the algorithm’s correctness by induction on _𝑗_ for 0 ≤ _𝑗_ ≤ _𝑇𝑐_ . Let **K** : _𝑗_ ∈ R<sup>_𝑗𝐵𝑐_×</sup><sup>_𝑑_</sup> be the first _𝑗𝐵𝑐_ rows of **K** , and similarly **V** : _𝑗_ ∈ R<sup>_𝑗𝐵𝑐_×</sup><sup>_𝑑_</sup> the the first _𝑗𝐵𝑐_ rows of **V** . Let **S** : _,_ : _𝑗_ = **QK**<sup>⊤</sup> : _𝑗_<sup>∈R</sup><sup>_𝑁_×</sup><sup>_𝑗𝐵𝑐_,and</sup> **P** : _,_ : _𝑗_ = softmax( **S** : _,_ : _𝑗_ ) ∈ R<sup>_𝑁_×</sup><sup>_𝑗𝐵𝑐_</sup> (softmax applied row-wise). Let _𝑚_<sup>_𝑗_</sup> _, ℓ_<sup>(</sup><sup>_𝑗_)</sup> _,_ **O**<sup>(</sup><sup>_𝑗_)</sup> be the values of _𝑚, ℓ,_ **O** in HBM after the _𝑗_ -th iteration of the outer loop (Algorithm 1 line 5). (Note that these values of _𝑚, ℓ,_ **O** are updated after each iteration of the outer loop.) We want to show that after the _𝑗_ -th iteration of the outer loop, we have computed in HBM:

---

[referencia=5727fed78bddc701 score=0.002]
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

[referencia=5727fed78bddc701 score=0.002]
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

[referencia=5727fed78bddc701 score=0.002]
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

[referencia=5727fed78bddc701 score=0.002]
- [1] Alok Aggarwal and S Vitter, Jeffrey. The input/output complexity of sorting and related problems. _Communications of the ACM_ , 31(9):1116–1127, 1988. 

- [2] Irwan Bello. LambdaNetworks: Modeling long-range interactions without attention. _arXiv preprint arXiv:2102.08602_ , 2021. 

- [3] Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. _arXiv preprint arXiv:2004.05150_ , 2020. 

- [4] L Susan Blackford, Antoine Petitet, Roldan Pozo, Karin Remington, R Clint Whaley, James Demmel, Jack Dongarra, Iain Duff, Sven Hammarling, Greg Henry, et al. An updated set of basic linear algebra subprograms (blas). _ACM Transactions on Mathematical Software_ , 28(2):135–151, 2002. 

- [5] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33:1877–1901, 2020. 

- [6] Ilias Chalkidis, Ion Androutsopoulos, and Nikolaos Aletras. Neural legal judgment prediction in English. In _Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics_ , pages 4317–4323, Florence, Italy, 2019. Association for Computational Linguistics. doi: 10.18653/v1/P19-1424. URL `https://www.aclweb.org/anthology/P19-1424` .