[referencia=a7468c6851652691 score=0.011]
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

[referencia=a7468c6851652691 score=0.001]
A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

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
development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3. 

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. 

In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

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
## **5 Training** 

This section describes the training regime for our models. 

### **5.1 Training Data and Batching** 

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared sourcetarget vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens. 

### **5.2 Hardware and Schedule** 

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models,(described on the bottom line of table 3), step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days). 

### **5.3 Optimizer** 

We used the Adam optimizer [20] with _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 98 and _ϵ_ = 10<sup>_−_9</sup> . We varied the learning rate over the course of training, according to the formula: 



This corresponds to increasing the learning rate linearly for the first _warmup_  steps_ training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used _warmup_  steps_ = 4000.

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
- [40] Muhua Zhu, Yue Zhang, Wenliang Chen, Min Zhang, and Jingbo Zhu. Fast and accurate shift-reduce constituent parsing. In _Proceedings of the 51st Annual Meeting of the ACL (Volume 1: Long Papers)_ , pages 434–443. ACL, August 2013. 

12

---

[referencia=a7468c6851652691 score=0.000]
- [5] Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. Learning phrase representations using rnn encoder-decoder for statistical machine translation. _CoRR_ , abs/1406.1078, 2014. 

- [6] Francois Chollet. Xception: Deep learning with depthwise separable convolutions. _arXiv preprint arXiv:1610.02357_ , 2016. 

- [7] Junyoung Chung, Çaglar Gülçehre, Kyunghyun Cho, and Yoshua Bengio. Empirical evaluation of gated recurrent neural networks on sequence modeling. _CoRR_ , abs/1412.3555, 2014. 

- [8] Chris Dyer, Adhiguna Kuncoro, Miguel Ballesteros, and Noah A. Smith. Recurrent neural network grammars. In _Proc. of NAACL_ , 2016. 

- [9] Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N. Dauphin. Convolutional sequence to sequence learning. _arXiv preprint arXiv:1705.03122v2_ , 2017. 

- [10] Alex Graves. Generating sequences with recurrent neural networks. _arXiv preprint arXiv:1308.0850_ , 2013. 

- [11] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , pages 770–778, 2016. 

- [12] Sepp Hochreiter, Yoshua Bengio, Paolo Frasconi, and Jürgen Schmidhuber. Gradient flow in recurrent nets: the difficulty of learning long-term dependencies, 2001. 

- [13] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. _Neural computation_ , 9(8):1735–1780, 1997.

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
14 



<!-- Start of picture text -->
The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br><!-- End of picture text -->

Figure 5: Many of the attention heads exhibit behaviour that seems related to the structure of the sentence. We give two such examples above, from two different heads from the encoder self-attention at layer 5 of 6. The heads clearly learned to perform different tasks. 

15

---

[referencia=a7468c6851652691 score=0.000]
- [13] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. _Neural computation_ , 9(8):1735–1780, 1997. 

- [14] Zhongqiang Huang and Mary Harper. Self-training PCFG grammars with latent annotations across languages. In _Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing_ , pages 832–841. ACL, August 2009. 

- [15] Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. Exploring the limits of language modeling. _arXiv preprint arXiv:1602.02410_ , 2016. 

- [16] Łukasz Kaiser and Samy Bengio. Can active memory replace attention? In _Advances in Neural Information Processing Systems, (NIPS)_ , 2016. 

- [17] Łukasz Kaiser and Ilya Sutskever. Neural GPUs learn algorithms. In _International Conference on Learning Representations (ICLR)_ , 2016. 

- [18] Nal Kalchbrenner, Lasse Espeholt, Karen Simonyan, Aaron van den Oord, Alex Graves, and Koray Kavukcuoglu. Neural machine translation in linear time. _arXiv preprint arXiv:1610.10099v2_ , 2017. 

- [19] Yoon Kim, Carl Denton, Luong Hoang, and Alexander M. Rush. Structured attention networks. In _International Conference on Learning Representations_ , 2017. 

- [20] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _ICLR_ , 2015. 

- [21] Oleksii Kuchaiev and Boris Ginsburg. Factorization tricks for LSTM networks. _arXiv preprint arXiv:1703.10722_ , 2017. 

- [22] Zhouhan Lin, Minwei Feng, Cicero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou, and Yoshua Bengio. A structured self-attentive sentence embedding. _arXiv preprint arXiv:1703.03130_ , 2017.

---

[referencia=a7468c6851652691 score=0.000]
### **3.5 Positional Encoding** 

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension _d_ model as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [9]. 

In this work, we use sine and cosine functions of different frequencies: 



where _pos_ is the position and _i_ is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 _π_ to 10000 _·_ 2 _π_ . We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset _k_ , _PEpos_ + _k_ can be represented as a linear function of _PEpos_ . 

We also experimented with using learned positional embeddings [9] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

---

[referencia=a7468c6851652691 score=0.000]
### **6.3 English Constituency Parsing** 

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. 

We trained a 4-layer transformer with _dmodel_ = 1024 on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting. 

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we 

9 

Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)

---

[referencia=a7468c6851652691 score=0.000]
### **6.2 Model Variations** 

To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the 

> 5We used values of 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively. 

8 

Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development set, newstest2013. Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities.

---

[referencia=a7468c6851652691 score=0.000]
Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.

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
# **Attention Is All You Need** 

**Ashish Vaswani**<sup>_∗_</sup> **Noam Shazeer**<sup>_∗_</sup> **Niki Parmar**<sup>_∗_</sup> **Jakob Uszkoreit**<sup>_∗_</sup> Google Brain Google Brain Google Research Google Research `avaswani@google.com noam@google.com nikip@google.com usz@google.com` 

**Llion Jones**<sup>_∗_</sup> Google Research `llion@google.com` 

**Aidan N. Gomez**<sup>_∗†_</sup> **Łukasz Kaiser**<sup>_∗_</sup> University of Toronto Google Brain `aidan@cs.toronto.edu lukaszkaiser@google.com` 

**Illia Polosukhin**<sup>_∗‡_</sup> 

```
illia.polosukhin@gmail.com
```