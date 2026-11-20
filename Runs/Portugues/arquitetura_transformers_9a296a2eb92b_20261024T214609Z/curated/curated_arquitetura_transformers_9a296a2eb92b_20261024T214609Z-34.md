[referencia=44e9a350d3df66d1 score=0.923]
### **3.2.3 Applications of Attention in our Model** 

The Transformer uses multi-head attention in three different ways: 

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [31, 2, 8]. 

- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2. 

### **3.3 Position-wise Feed-Forward Networks** 

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between. 

FFN( _x_ ) = max(0 _, xW_ 1 + _b_ 1) _W_ 2 + _b_ 2 (2) 

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is _d_ model = 512, and the inner-layer has dimensionality _dff_ = 2048.

---

[referencia=44e9a350d3df66d1 score=0.609]
### **3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position- 

2 



Figure 1: The Transformer - model architecture. 

wise fully connected feed-forward network. We employ a residual connection [10] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer 

itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ . 

**3.2 Attention** 

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

---

[referencia=44e9a350d3df66d1 score=0.051]
6 

the input sequence centered around the respective output position. This would increase the maximum path length to _O_ ( _n/r_ ). We plan to investigate this approach further in future work. 

A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [15], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

[referencia=44e9a350d3df66d1 score=0.028]
In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs. 

## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [20], ByteNet [15] and ConvS2S [8], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [11]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 22, 23, 19]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [28]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [14, 15] and [8].

---

[referencia=44e9a350d3df66d1 score=0.024]
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



In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility

---

[referencia=44e9a350d3df66d1 score=0.021]
### **3.2.1 Scaled Dot-Product Attention** 

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension _dk_ , and values of dimension _dv_ . We compute the dot products of the 

3 

Scaled Dot-Product Attention 





Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. 

query with all keys, divide each by<sup>_√_</sup> _dk_ , and apply a softmax function to obtain the weights on the values. 

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix _Q_ . The keys and values are also packed together into matrices _K_ and _V_ . We compute the matrix of outputs as: 



The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

While for small values of _dk_ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of _dk_ [3]. We suspect that for large values of _dk_ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup> . To counteract this effect, we scale the dot products by _~~√~~_ <u>1</u> _dk_<sup>.</sup>

---

[referencia=44e9a350d3df66d1 score=0.019]
- [29] Ilya Sutskever, Oriol Vinyals, and Quoc VV Le. Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems_ , pages 3104–3112, 2014. 

- [30] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. _CoRR_ , abs/1512.00567, 2015. 

- [31] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google’s neural machine translation system: Bridging the gap between human and machine translation. _arXiv preprint arXiv:1609.08144_ , 2016. 

- [32] Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu. Deep recurrent models with fast-forward connections for neural machine translation. _CoRR_ , abs/1606.04199, 2016. 

11

---

[referencia=44e9a350d3df66d1 score=0.015]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [12] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [29, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [31, 21, 13]. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

- Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [18] and conditional computation [26], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 16]. In all but a few cases [22], however, such attention mechanisms are used in conjunction with a recurrent network.

---

[referencia=44e9a350d3df66d1 score=0.013]
We also experimented with using learned positional embeddings [8] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

---

[referencia=44e9a350d3df66d1 score=0.011]
## **References** 

- [1] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. 

|[2] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly|
|---|
|learning to align and translate. _CoRR_, abs/1409.0473, 2014.|



|[3] Denny Britz, Anna Goldie, Minh-Thang Luong, and Quoc V. Le. Massive exploration of neural<br>machine translation architectures. _CoRR_, abs/1703.03906, 2017.|
|---|
|[4] Jianpeng Cheng, Li Dong, and Mirella Lapata. Long short-term memory-networks for machine<br>reading. _arXiv preprint arXiv:1601.06733_, 2016.|
|[5] Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Fethi Bougares, Holger Schwenk,<br>and Yoshua Bengio. Learning phrase representations using rnn encoder-decoder for statistical<br>machine translation. _CoRR_, abs/1406.1078, 2014.|



[6] Francois Chollet. Xception: Deep learning with depthwise separable convolutions. _arXiv preprint arXiv:1610.02357_ , 2016. 

[7] Junyoung Chung, Çaglar Gülçehre, Kyunghyun Cho, and Yoshua Bengio. Empirical evaluation of gated recurrent neural networks on sequence modeling. _CoRR_ , abs/1412.3555, 2014. 

[8] Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N. Dauphin. Convolutional sequence to sequence learning. _arXiv preprint arXiv:1705.03122v2_ , 2017. 

[9] Alex Graves. Generating sequences with recurrent neural networks. _arXiv preprint_

---

[referencia=44e9a350d3df66d1 score=0.008]
### **3.5 Positional Encoding** 

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the 

5 

Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. _n_ is the sequence length, _d_ is the representation dimension, _k_ is the kernel size of convolutions and _r_ the size of the neighborhood in restricted self-attention. 

|Layer Type|Complexity per Layer|Sequential<br>Operations|Maximum Path Length|
|---|---|---|---|
|Self-Attention|_O_(_n_<sup>2</sup> _· d_)|_O_(1)|_O_(1)|
|Recurrent|_O_(_n · d_<sup>2</sup>)|_O_(_n_)|_O_(_n_)|
|Convolutional|_O_(_k · n · d_<sup>2</sup>)|_O_(1)|_O_(_logk_(_n_))|
|Self-Attention (restricted)|_O_(_r · n · d_)|_O_(1)|_O_(_n/r_)|



bottoms of the encoder and decoder stacks. The positional encodings have the same dimension _d_ model as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [8]. 

In this work, we use sine and cosine functions of different frequencies: 



where _pos_ is the position and _i_ is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 _π_ to 10000 _·_ 2 _π_ . We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset _k_ , _PEpos_ + _k_ can be represented as a linear function of _PEpos_ .

---

[referencia=44e9a350d3df66d1 score=0.008]
7 

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost. 

|Model|BL|EU|Training C|ost (FLOPs)|
|---|---|---|---|---|
||EN-DE|EN-FR|EN-DE|EN-FR|
|ByteNet [15]|23.75||||
|Deep-Att + PosUnk [32]||39.2||1_._0_·_10<sup>20</sup><br>|
|GNMT + RL [31]|24.6|39.92|2_._3_·_10<sup>19</sup>|1_._4_·_10<sup>20</sup>|
|ConvS2S [8]|25.16|40.46|9_._6_·_10<sup>18</sup><br>|1_._5_·_10<sup>20</sup><br>|
|MoE[26]|26.03|40.56|2_._0_·_10<sup>19</sup>|1_._2_·_10<sup>20</sup>|
|Deep-Att + PosUnk Ensemble [32]||40.4||8_._0_·_10<sup>20</sup><br>|
|GNMT + RL Ensemble [31]|26.30|41.16|1_._8_·_10<sup>20</sup><br>|1_._1_·_10<sup>21</sup><br>|
|ConvS2S Ensemble[8]|26.36|**41.29**|7_._7_·_10<sup>19</sup>|1_._2_·_10<sup>21</sup>|
|Transformer (base model)|27.3|38.1|**3****_._3****_·_**|**10**<sup>**18**</sup>|
|Transformer (big)|**28.4**|**41.0**|2_._3_·_|10<sup>19</sup>|

---

[referencia=44e9a350d3df66d1 score=0.006]
- [21] Minh-Thang Luong, Hieu Pham, and Christopher D Manning. Effective approaches to attentionbased neural machine translation. _arXiv preprint arXiv:1508.04025_ , 2015. 

- [22] Ankur Parikh, Oscar Täckström, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model. In _Empirical Methods in Natural Language Processing_ , 2016. 

- [23] Romain Paulus, Caiming Xiong, and Richard Socher. A deep reinforced model for abstractive summarization. _arXiv preprint arXiv:1705.04304_ , 2017. 

- [24] Ofir Press and Lior Wolf. Using the output embedding to improve language models. _arXiv preprint arXiv:1608.05859_ , 2016. 

- [25] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. _arXiv preprint arXiv:1508.07909_ , 2015. 

- [26] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. _arXiv preprint arXiv:1701.06538_ , 2017. 

- [27] Nitish Srivastava, Geoffrey E Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. _Journal of Machine Learning Research_ , 15(1):1929–1958, 2014. 

- [28] Sainbayar Sukhbaatar, arthur szlam, Jason Weston, and Rob Fergus. End-to-end memory networks. In C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama, and R. Garnett, editors, _Advances in Neural Information Processing Systems 28_ , pages 2440–2448. Curran Associates, Inc., 2015.

---

[referencia=44e9a350d3df66d1 score=0.005]
### **5.4 Regularization** 

We employ three types of regularization during training: 

**Residual Dropout** We apply dropout [27] to the output of each sub-layer, before it is added to the sub-layer input and normalized. In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of _Pdrop_ = 0 _._ 1. 

7 

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost.

---

[referencia=44e9a350d3df66d1 score=0.004]
### _arXiv:1308.0850_ , 2013. 

[10] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for im- 

age recognition. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 770–778, 2016. 

> [11] Sepp Hochreiter, Yoshua Bengio, Paolo Frasconi, and Jürgen Schmidhuber. Gradient flow in 

recurrent nets: the difficulty of learning long-term dependencies, 2001. [12] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. _Neural computation_ , 9(8):1735–1780, 1997. 

[13] Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. Exploring the limits of language modeling. _arXiv preprint arXiv:1602.02410_ , 2016. 

[14] Łukasz Kaiser and Ilya Sutskever. Neural GPUs learn algorithms. In _International Conference_ 

_on Learning Representations (ICLR)_ , 2016. 

[15] Nal Kalchbrenner, Lasse Espeholt, Karen Simonyan, Aaron van den Oord, Alex Graves, and Ko- 

ray Kavukcuoglu. Neural machine translation in linear time. _arXiv preprint arXiv:1610.10099v2_ , 2017. 

[16] Yoon Kim, Carl Denton, Luong Hoang, and Alexander M. Rush. Structured attention networks. 

In _International Conference on Learning Representations_ , 2017.

---

[referencia=44e9a350d3df66d1 score=0.004]
## **4 Why Self-Attention** 

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to another sequence of equal length ( _z_ 1 _, ..., zn_ ), with _xi, zi ∈_ R<sup>_d_</sup> , such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata. 

One is the total computational complexity per layer. Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required. 

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [11]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types. 

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires _O_ ( _n_ ) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length _n_ is smaller than the representation dimensionality _d_ , which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [31] and byte-pair [25] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size _r_ in 

6 

the input sequence centered around the respective output position. This would increase the maximum path length to _O_ ( _n/r_ ). We plan to investigate this approach further in future work.

---

[referencia=44e9a350d3df66d1 score=0.003]
[16] Yoon Kim, Carl Denton, Luong Hoang, and Alexander M. Rush. Structured attention networks. 

In _International Conference on Learning Representations_ , 2017. 

- [17] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _ICLR_ , 2015. 

- [18] Oleksii Kuchaiev and Boris Ginsburg. Factorization tricks for LSTM networks. _arXiv preprint arXiv:1703.10722_ , 2017. 

- [19] Zhouhan Lin, Minwei Feng, Cicero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou, and Yoshua Bengio. A structured self-attentive sentence embedding. _arXiv preprint arXiv:1703.03130_ , 2017. 

- [20] Samy Bengio Łukasz Kaiser. Can active memory replace attention? In _Advances in Neural Information Processing Systems, (NIPS)_ , 2016. 

10

---

[referencia=44e9a350d3df66d1 score=0.002]
# **Attention Is All You Need** 

**Ashish Vaswani**<sup>_∗_</sup> **Noam Shazeer**<sup>_∗_</sup> **Niki Parmar**<sup>_∗_</sup> **Jakob Uszkoreit**<sup>_∗_</sup> Google Brain Google Brain Google Research Google Research `avaswani@google.com noam@google.com nikip@google.com usz@google.com` 

**Llion Jones**<sup>_∗_</sup> Google Research `llion@google.com` 

**Aidan N. Gomez**<sup>_∗†_</sup> **Łukasz Kaiser**<sup>_∗_</sup> University of Toronto Google Brain `aidan@cs.toronto.edu lukaszkaiser@google.com` 

### **Illia Polosukhin**<sup>_∗‡_</sup> 

```
illia.polosukhin@gmail.com
```

## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature.

---

[referencia=44e9a350d3df66d1 score=0.002]
In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility 

function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [8], and observe nearly identical results to the base model. 

**7 Conclusion** In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with 

multi-headed self-attention. 

For translation tasks, the Transformer can be trained significantly faster than architectures based 

on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 

We are excited about the future of attention-based models and plan to apply them to other tasks. We 

plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. The code we used to train and evaluate our models is available at `https://github.com/ tensorflow/tensor2tensor` . 

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration. 

9

---

[referencia=44e9a350d3df66d1 score=0.001]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 29]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [9], consuming the previously generated symbols as additional input when generating the next. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.