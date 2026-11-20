[referencia=a7468c6851652691 score=0.004]
# **Attention Is All You Need** 

**Ashish Vaswani**<sup>_∗_</sup> **Noam Shazeer**<sup>_∗_</sup> **Niki Parmar**<sup>_∗_</sup> **Jakob Uszkoreit**<sup>_∗_</sup> Google Brain Google Brain Google Research Google Research `avaswani@google.com noam@google.com nikip@google.com usz@google.com` 

**Llion Jones**<sup>_∗_</sup> Google Research `llion@google.com` 

**Aidan N. Gomez**<sup>_∗†_</sup> **Łukasz Kaiser**<sup>_∗_</sup> University of Toronto Google Brain `aidan@cs.toronto.edu lukaszkaiser@google.com` 

**Illia Polosukhin**<sup>_∗‡_</sup> 

```
illia.polosukhin@gmail.com
```

---

[referencia=a7468c6851652691 score=0.002]
Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.

---

[referencia=a7468c6851652691 score=0.001]
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

[referencia=a7468c6851652691 score=0.001]
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

[referencia=a7468c6851652691 score=0.000]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

### **3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ .

---

[referencia=a7468c6851652691 score=0.000]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=a7468c6851652691 score=0.000]
9 

Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ) 

|**Parser**|**Training**|**WSJ 23 F1**|
|---|---|---|
|Vinyals & Kaiser el al. (2014) [37]|WSJ only, discriminative|88.3|
|Petrov et al. (2006) [29]|WSJ only, discriminative|90.4|
|Zhu et al. (2013) [40]|WSJ only, discriminative|90.4|
|Dyer et al. (2016) [8]|WSJ only,discriminative|91.7|
|Transformer(4 layers)|WSJ only,discriminative|91.3|
|Zhu et al. (2013) [40]|semi-supervised|91.3|
|Huang & Harper (2009) [14]|semi-supervised|91.3|
|McClosky et al. (2006) [26]|semi-supervised|92.1|
|Vinyals & Kaiser el al. (2014) [37]|semi-supervised|92.1|
|Transformer(4 layers)|semi-supervised|92.7|
|Luong et al. (2015) [23]|multi-task|93.0|
|Dyer et al. (2016) [8]|generative|93.3|



increased the maximum output length to input length + 300. We used a beam size of 21 and _α_ = 0 _._ 3 for both WSJ only and the semi-supervised setting. 

Our results in Table 4 show that despite the lack of task-specific tuning our model performs surprisingly well, yielding better results than all previously reported models with the exception of the Recurrent Neural Network Grammar [8]. 

In contrast to RNN sequence-to-sequence models [37], the Transformer outperforms the BerkeleyParser [29] even when training only on the WSJ training set of 40K sentences.

---

[referencia=a7468c6851652691 score=0.000]
## **References** 

- [1] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. 

- [2] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. _CoRR_ , abs/1409.0473, 2014. 

- [3] Denny Britz, Anna Goldie, Minh-Thang Luong, and Quoc V. Le. Massive exploration of neural machine translation architectures. _CoRR_ , abs/1703.03906, 2017. 

- [4] Jianpeng Cheng, Li Dong, and Mirella Lapata. Long short-term memory-networks for machine reading. _arXiv preprint arXiv:1601.06733_ , 2016. 

10

---

[referencia=a7468c6851652691 score=0.000]
## **Attention Visualizations** 



<!-- Start of picture text -->
It is in this spirit that a majority of American governments have passed new laws since 2009 making the registration or voting process more difficult . <EOS> <pad> <pad> <pad> <pad> <pad> <pad><br>It is in this spirit that a majority of American governments have passed new laws since 2009 making the registration or voting process more difficult . <EOS> <pad> <pad> <pad> <pad> <pad> <pad><br><!-- End of picture text -->

Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads attend to a distant dependency of the verb ‘making’, completing the phrase ‘making...more difficult’. Attentions here shown only for the word ‘making’. Different colors represent different heads. Best viewed in color. 

13 



<!-- Start of picture text -->
The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br><!-- End of picture text -->

Figure 4: Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions from just the word ‘its’ for attention heads 5 and 6. Note that the attentions are very sharp for this word. 

14 



<!-- Start of picture text -->

---

[referencia=a7468c6851652691 score=0.000]
### **3.2 Attention** 

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum 

3 

Scaled Dot-Product Attention 





Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. 

of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. 

### **3.2.1 Scaled Dot-Product Attention** 

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension _dk_ , and values of dimension _dv_ . We compute the dot products of the query with all keys, divide each by<sup>_√_</sup> _dk_ , and apply a softmax function to obtain the weights on the values. 

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix _Q_ . The keys and values are also packed together into matrices _K_ and _V_ . We compute the matrix of outputs as: 



The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

While for small values of _dk_ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of _dk_ [3]. We suspect that for large values of _dk_ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup> . To counteract this effect, we scale the dot products by _~~√~~_ <u>1</u> _dk_<sup>.</sup>

---

[referencia=a7468c6851652691 score=0.000]
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

[referencia=a7468c6851652691 score=0.000]
- [33] Nitish Srivastava, Geoffrey E Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. _Journal of Machine Learning Research_ , 15(1):1929–1958, 2014. 

- [34] Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, and Rob Fergus. End-to-end memory networks. In C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama, and R. Garnett, editors, _Advances in Neural Information Processing Systems 28_ , pages 2440–2448. Curran Associates, Inc., 2015. 

- [35] Ilya Sutskever, Oriol Vinyals, and Quoc VV Le. Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems_ , pages 3104–3112, 2014. 

- [36] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. _CoRR_ , abs/1512.00567, 2015. 

- [37] Vinyals & Kaiser, Koo, Petrov, Sutskever, and Hinton. Grammar as a foreign language. In _Advances in Neural Information Processing Systems_ , 2015. 

- [38] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google’s neural machine translation system: Bridging the gap between human and machine translation. _arXiv preprint arXiv:1609.08144_ , 2016. 

- [39] Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu. Deep recurrent models with fast-forward connections for neural machine translation. _CoRR_ , abs/1606.04199, 2016.

---

[referencia=a7468c6851652691 score=0.000]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=a7468c6851652691 score=0.000]
14 



<!-- Start of picture text -->
The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br><!-- End of picture text -->

Figure 5: Many of the attention heads exhibit behaviour that seems related to the structure of the sentence. We give two such examples above, from two different heads from the encoder self-attention at layer 5 of 6. The heads clearly learned to perform different tasks. 

15

---

[referencia=a7468c6851652691 score=0.000]
### **6.2 Model Variations** 

To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the 

> 5We used values of 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively. 

8 

Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development set, newstest2013. Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities.

---

[referencia=a7468c6851652691 score=0.000]
A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

[referencia=a7468c6851652691 score=0.000]
## **7 Conclusion** 

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. 

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. 

The code we used to train and evaluate our models is available at `https://github.com/ tensorflow/tensor2tensor` . 

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

---

[referencia=a7468c6851652691 score=0.000]
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

[referencia=a7468c6851652691 score=0.000]
- [25] Mitchell P Marcus, Mary Ann Marcinkiewicz, and Beatrice Santorini. Building a large annotated corpus of english: The penn treebank. _Computational linguistics_ , 19(2):313–330, 1993. 

- [26] David McClosky, Eugene Charniak, and Mark Johnson. Effective self-training for parsing. In _Proceedings of the Human Language Technology Conference of the NAACL, Main Conference_ , pages 152–159. ACL, June 2006. 

- [27] Ankur Parikh, Oscar Täckström, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model. In _Empirical Methods in Natural Language Processing_ , 2016. 

- [28] Romain Paulus, Caiming Xiong, and Richard Socher. A deep reinforced model for abstractive summarization. _arXiv preprint arXiv:1705.04304_ , 2017. 

- [29] Slav Petrov, Leon Barrett, Romain Thibaux, and Dan Klein. Learning accurate, compact, and interpretable tree annotation. In _Proceedings of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the ACL_ , pages 433–440. ACL, July 2006. 

- [30] Ofir Press and Lior Wolf. Using the output embedding to improve language models. _arXiv preprint arXiv:1608.05859_ , 2016. 

- [31] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. _arXiv preprint arXiv:1508.07909_ , 2015. 

- [32] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. _arXiv preprint arXiv:1701.06538_ , 2017.

---

[referencia=a7468c6851652691 score=0.000]
- [40] Muhua Zhu, Yue Zhang, Wenliang Chen, Min Zhang, and Jingbo Zhu. Fast and accurate shift-reduce constituent parsing. In _Proceedings of the 51st Annual Meeting of the ACL (Volume 1: Long Papers)_ , pages 434–443. ACL, August 2013. 

12