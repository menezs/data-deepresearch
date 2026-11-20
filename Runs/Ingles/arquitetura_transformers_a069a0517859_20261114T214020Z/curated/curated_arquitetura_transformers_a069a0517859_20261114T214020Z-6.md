[referencia=c23bf2a3bc33cb7a score=0.984]
# NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE 

### **Dzmitry Bahdanau** 

Jacobs University Bremen, Germany 

**KyungHyun Cho Yoshua Bengio**<sup>_∗_</sup> Universit´e de Montr´eal 

## ABSTRACT 

Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

---

[referencia=c23bf2a3bc33cb7a score=0.931]
## 1 INTRODUCTION 

_Neural machine translation_ is a newly emerging approach to machine translation, recently proposed by Kalchbrenner and Blunsom (2013), Sutskever _et al._ (2014) and Cho _et al._ (2014b). Unlike the traditional phrase-based translation system (see, e.g., Koehn _et al._ , 2003) which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation. 

Most of the proposed neural machine translation models belong to a family of _encoder– decoders_ (Sutskever _et al._ , 2014; Cho _et al._ , 2014a), with an encoder and a decoder for each language, or involve a language-specific encoder applied to each sentence whose outputs are then compared (Hermann and Blunsom, 2014). An encoder neural network reads and encodes a source sentence into a fixed-length vector. A decoder then outputs a translation from the encoded vector. The whole encoder–decoder system, which consists of the encoder and the decoder for a language pair, is jointly trained to maximize the probability of a correct translation given a source sentence. 

A potential issue with this encoder–decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus. Cho _et al._ (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases. 

In order to address this issue, we introduce an extension to the encoder–decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words. 

> _∗_ CIFAR Senior Fellow 

1 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.808]
## 7 CONCLUSION 

The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from which a translation will be decoded. We conjectured that the use of a fixed-length context vector is problematic for translating long sentences, based on a recent empirical study reported by Cho _et al._ (2014b) and Pouget-Abadie _et al._ (2014). 

In this paper, we proposed a novel architecture that addresses this issue. We extended the basic encoder–decoder by letting a model (soft-)search for a set of input words, or their annotations computed by an encoder, when generating each target word. This frees the model from having to encode a whole source sentence into a fixed-length vector, and also lets the model focus only on information relevant to the generation of the next target word. This has a major positive impact on the ability of the neural machine translation system to yield good results on longer sentences. Unlike with the traditional machine translation systems, all of the pieces of the translation system, including the alignment mechanism, are jointly trained towards a better log-probability of producing correct translations. 

We tested the proposed model, called RNNsearch, on the task of English-to-French translation. The experiment revealed that the proposed RNNsearch outperforms the conventional encoder–decoder model (RNNencdec) significantly, regardless of the sentence length and that it is much more robust to the length of a source sentence. From the qualitative analysis where we investigated the (soft-)alignment generated by the RNNsearch, we were able to conclude that the model can correctly align each target word with the relevant words, or their annotations, in the source sentence as it generated a correct translation. 

Perhaps more importantly, the proposed approach achieved a translation performance comparable to the existing phrase-based statistical machine translation. It is a striking result, considering that the proposed architecture, or the whole family of neural machine translation, has only been proposed as recently as this year. We believe the architecture proposed here is a promising step toward better machine translation and a better understanding of natural languages in general. 

One of challenges left for the future is to better handle unknown, or rare words. This will be required for the model to be more widely used and to match the performance of current state-of-the-art machine translation systems in all contexts. 

9 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.635]
One of the motivations behind the proposed approach was the use of a fixed-length context vector in the basic encoder–decoder approach. We conjectured that this limitation may make the basic encoder–decoder approach to underperform with long sentences. In Fig. 2, we see that the performance of RNNencdec dramatically drops as the length of the sentences increases. On the other hand, both RNNsearch-30 and RNNsearch-50 are more robust to the length of the sentences. RNNsearch50, especially, shows no performance deterioration even with sentences of length 50 or more. This superiority of the proposed model over the basic encoder–decoder is further confirmed by the fact that the RNNsearch-30 even outperforms RNNencdec-50 (see Table 1). 

6 

Published as a conference paper at ICLR 2015 

|Model|All|No UNK<sup>_◦_</sup>|
|---|---|---|
|RNNencdec-30|13.93|24.19|
|RNNsearch-30|21.50|31.44|
|RNNencdec-50|17.82|26.71|
|RNNsearch-50|26.75|34.16|
|RNNsearch-50<sup>_⋆_</sup>|28.45|36.15|
|Moses|33.30|35.63|



Table 1: BLEU scores of the trained models computed on the test set. The second and third columns show respectively the scores on all the sentences and, on the sentences without any unknown word in themselves and in the reference translations. Note that RNNsearch-50<sup>_⋆_</sup> was trained much longer until the performance on the development set stopped improving. ( _◦_ ) We disallowed the models to generate [UNK] tokens when only the sentences having no unknown words were evaluated (last column). 

### 5.2 QUALITATIVE ANALYSIS

---

[referencia=c23bf2a3bc33cb7a score=0.411]
### 2.1 RNN ENCODER–DECODER 

Here, we describe briefly the underlying framework, called _RNN Encoder–Decoder_ , proposed by Cho _et al._ (2014a) and Sutskever _et al._ (2014) upon which we build a novel architecture that learns to align and translate simultaneously. 

In the Encoder–Decoder framework, an encoder reads the input sentence, a sequence of vectors **x** = ( _x_ 1 _, · · · , xTx_ ), into a vector _c_ .<sup>2</sup> The most common approach is to use an RNN such that 



and 



where _ht ∈_ R<sup>_n_</sup> is a hidden state at time _t_ , and _c_ is a vector generated from the sequence of the hidden states. _f_ and _q_ are some nonlinear functions. Sutskever _et al._ (2014) used an LSTM as _f_ and _q_ ( _{h_ 1 _, · · · , hT }_ ) = _hT_ , for instance. 

> 1 We mean by the state-of-the-art performance, the performance of the conventional phrase-based system without using any neural network-based component. 

> 2 Although most of the previous works (see, e.g., Cho _et al._ , 2014a; Sutskever _et al._ , 2014; Kalchbrenner and Blunsom, 2013) used to encode a variable-length input sentence into a _fixed-length_ vector, it is not necessary, and even it may be beneficial to have a _variable-length_ vector, as we will show later. 

2 

Published as a conference paper at ICLR 2015 

The decoder is often trained to predict the next word _yt′_ given the context vector _c_ and all the previously predicted words _{y_ 1 _, · · · , yt′−_ 1 _}_ . In other words, the decoder defines a probability over the translation **y** by decomposing the joint probability into the ordered conditionals:

---

[referencia=c23bf2a3bc33cb7a score=0.197]
- Pouget-Abadie, J., Bahdanau, D., van Merri¨enboer, B., Cho, K., and Bengio, Y. (2014). Overcoming the curse of sentence length for neural machine translation using automatic segmentation. In _Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation_ . to appear. 

- Schuster, M. and Paliwal, K. K. (1997). Bidirectional recurrent neural networks. _Signal Processing, IEEE Transactions on_ , **45** (11), 2673–2681. 

- Schwenk, H. (2012). Continuous space translation models for phrase-based statistical machine translation. In M. Kay and C. Boitet, editors, _Proceedings of the 24th International Conference on Computational Linguistics (COLIN)_ , pages 1071–1080. Indian Institute of Technology Bombay. 

- Schwenk, H., Dchelotte, D., and Gauvain, J.-L. (2006). Continuous space language models for statistical machine translation. In _Proceedings of the COLING/ACL on Main conference poster sessions_ , pages 723–730. Association for Computational Linguistics. 

- Sutskever, I., Vinyals, O., and Le, Q. (2014). Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems (NIPS 2014)_ . 

Zeiler, M. D. (2012). ADADELTA: An adaptive learning rate method. _arXiv:_ 1212.5701 [cs.LG]. 

11 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.160]
> _∗_ CIFAR Senior Fellow 

1 

Published as a conference paper at ICLR 2015 

The most important distinguishing feature of this approach from the basic encoder–decoder is that it does not attempt to encode a whole input sentence into a single fixed-length vector. Instead, it encodes the input sentence into a sequence of vectors and chooses a subset of these vectors adaptively while decoding the translation. This frees a neural translation model from having to squash all the information of a source sentence, regardless of its length, into a fixed-length vector. We show this allows a model to cope better with long sentences. 

In this paper, we show that the proposed approach of jointly learning to align and translate achieves significantly improved translation performance over the basic encoder–decoder approach. The improvement is more apparent with longer sentences, but can be observed with sentences of any length. On the task of English-to-French translation, the proposed approach achieves, with a single model, a translation performance comparable, or close, to the conventional phrase-based system. Furthermore, qualitative analysis reveals that the proposed model finds a linguistically plausible (soft-)alignment between a source sentence and the corresponding target sentence.

---

[referencia=c23bf2a3bc33cb7a score=0.120]
### A.2 DETAILED DESCRIPTION OF THE MODEL 

### A.2.1 ENCODER 

In this section, we describe in detail the architecture of the proposed model (RNNsearch) used in the experiments (see Sec. 4–5). From here on, we omit all bias terms in order to increase readability. 

The model takes a source sentence of 1-of-K coded word vectors as input 



and outputs a translated sentence of 1-of-K coded word vectors 



where _Kx_ and _Ky_ are the vocabulary sizes of source and target languages, respectively. _Tx_ and _Ty_ respectively denote the lengths of source and target sentences. 

First, the forward states of the bidirectional recurrent neural network (BiRNN) are computed: 



where 



_E ∈_ R<sup>_m×Kx_</sup> is the word embedding matrix.<sup>_−→_</sup> _W,_<sup>_−→_</sup> _W z,_<sup>_−→_</sup> _W r ∈_ R<sup>_n×m_</sup> ,<sup>_−→_</sup> _U ,_<sup>_−→_</sup> _U z,_<sup>_−→_</sup> _U r ∈_ R<sup>_n×n_</sup> are weight matrices. _m_ and _n_ are the word embedding dimensionality and the number of hidden units, respectively. _σ_ ( _·_ ) is as usual a logistic sigmoid function. 

The backward states (<sup>_←−_</sup> _h_ 1 _, · · · ,_<sup>_←−_</sup> _h Tx_ ) are computed similarly. We share the word embedding matrix _E_ between the forward and backward RNNs, unlike the weight matrices. 

We concatenate the forward and backward states to to obtain the annotations ( _h_ 1 _, h_ 2 _, · · · , hTx_ ), where

---

[referencia=c23bf2a3bc33cb7a score=0.116]
Again, the RNNsearch-50 was able to translate this long sentence correctly: 

_Ce genre d’exp´erience fait partie des efforts de Disney pour ”prolonger la dur´ee de vie de ses s´eries et cr´eer de nouvelles relations avec des publics_ _<u>via des plateformes numeriques´ de plus en plus importantes”, a-t-il ajoute.´</u>_ 

In conjunction with the quantitative results presented already, these qualitative observations confirm our hypotheses that the RNNsearch architecture enables far more reliable translation of long sentences than the standard RNNencdec model. 

In Appendix C, we provide a few more sample translations of long source sentences generated by the RNNencdec-50, RNNsearch-50 and Google Translate along with the reference translations.

---

[referencia=c23bf2a3bc33cb7a score=0.112]
### The RNNencdec-50 translated this sentence into: 

_Un privil`ege d’admission est le droit d’un m´edecin de reconnaˆıtre un patient `a l’hˆopital ou un centre m´edical_ _<u>d’un diagnostic ou de prendre un diagnostic en fonction de son etat´ de sante.´</u>_ 

7 

Published as a conference paper at ICLR 2015 

The RNNencdec-50 correctly translated the source sentence until [a medical center]. However, from there on (underlined), it deviated from the original meaning of the source sentence. For instance, it replaced [based on his status as a health care worker at a hospital] in the source sentence with [en fonction de son ´etat de sant´e] (“based on his state of health”). 

On the other hand, the RNNsearch-50 generated the following correct translation, preserving the whole meaning of the input sentence without omitting any details: 

_Un privil`ege d’admission est le droit d’un m´edecin d’admettre un patient `a un hˆopital ou un centre m´edical_ _<u>pour effectuer un diagnostic ou une procedure,´ selon son statut de travailleur des soins de sante´ a` l’hopital.ˆ</u>_ 

Let us consider another sentence from the test set: 

_This kind of experience is part of Disney’s efforts to ”extend the lifetime of its series and build new relationships with audiences_ _<u>via digital platforms that are becoming ever more important,” he added.</u>_ 

The translation by the RNNencdec-50 is 

_Ce type d’exp´erience fait partie des initiatives du Disney pour ”prolonger la dur´ee de vie de ses nouvelles et de d´evelopper des liens avec les_ _<u>lecteurs numeriques´ qui deviennent plus complexes.</u>_ 

As with the previous example, the RNNencdec began deviating from the actual meaning of the source sentence after generating approximately 30 words (see the underlined phrase). After that point, the quality of the translation deteriorates, with basic mistakes such as the lack of a closing quotation mark. 

Again, the RNNsearch-50 was able to translate this long sentence correctly:

---

[referencia=c23bf2a3bc33cb7a score=0.107]
### 3.1 DECODER: GENERAL DESCRIPTION 

In a new model architecture, we define each conditional probability in Eq. (2) as: 



where _si_ is an RNN hidden state for time _i_ , computed by 



It should be noted that unlike the existing encoder–decoder approach (see Eq. (2)), here the probability is conditioned on a distinct context vector _ci_ for each target word _yi_ . 

The context vector _ci_ depends on a sequence of _annotations_ ( _h_ 1 _, · · · , hTx_ ) to which an encoder maps the input sentence. Each annotation _hi_ contains information about the whole input sequence with a strong focus on the parts surrounding the _i_ -th word of the input sequence. We explain in detail how the annotations are computed in the next section. 

The context vector _ci_ is, then, computed as a weighted sum of these annotations _hi_ : 





<!-- Start of picture text -->
yt-1 yt<br>s t-1 s t<br>+<br>αt,1 αt,T<br>αt,2 αt,3<br>h1 h2 h3 hT<br>h1 h2 h3 hT<br>x1 x2 x3 xT<br><!-- End of picture text -->

Figure 1: The graphical illustration of the proposed model trying to generate the _t_ -th target word _yt_ given a source sentence ( _x_ 1 _, x_ 2 _, . . . , xT_ ). 

The weight _αij_ of each annotation _hj_ is computed by 



where 



is an _alignment model_ which scores how well the inputs around position _j_ and the output at position _i_ match. The score is based on the RNN hidden state _si−_ 1 (just before emitting _yi_ , Eq. (4)) and the _j_ -th annotation _hj_ of the input sentence. 

We parametrize the alignment model _a_ as a feedforward neural network which is jointly trained with all the other components of the proposed system. Note that unlike in traditional machine translation, 

3 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.090]
- Cho, K., van Merri¨enboer, B., Bahdanau, D., and Bengio, Y. (2014b). On the properties of neural machine translation: Encoder–Decoder approaches. In _Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation_ . to appear. 

- Devlin, J., Zbib, R., Huang, Z., Lamar, T., Schwartz, R., and Makhoul, J. (2014). Fast and robust neural network joint models for statistical machine translation. In _Association for Computational Linguistics_ . 

- Forcada, M. L. and Neco,<sup>˜</sup> R. P. (1997). Recursive hetero-associative memories for translation. In J. Mira, R. Moreno-D´ıaz, and J. Cabestany, editors, _Biological and Artificial Computation: From Neuroscience to Technology_ , volume 1240 of _Lecture Notes in Computer Science_ , pages 453–462. Springer Berlin Heidelberg. 

- Goodfellow, I., Warde-Farley, D., Mirza, M., Courville, A., and Bengio, Y. (2013). Maxout networks. In _Proceedings of The 30th International Conference on Machine Learning_ , pages 1319– 1327. 

- Graves, A. (2012). Sequence transduction with recurrent neural networks. In _Proceedings of the 29th International Conference on Machine Learning (ICML 2012)_ . 

- Graves, A. (2013). Generating sequences with recurrent neural networks. _arXiv:_ 1308.0850 [cs.NE]. 

- Graves, A., Jaitly, N., and Mohamed, A.-R. (2013). Hybrid speech recognition with deep bidirectional LSTM. In _Automatic Speech Recognition and Understanding (ASRU), 2013 IEEE Workshop on_ , pages 273–278. 

10 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.089]
### A.1.1 RECURRENT NEURAL NETWORK 

For the activation function _f_ of an RNN, we use the gated hidden unit recently proposed by Cho _et al._ (2014a). The gated hidden unit is an alternative to the conventional _simple_ units such as an element-wise tanh. This gated unit is similar to a long short-term memory (LSTM) unit proposed earlier by Hochreiter and Schmidhuber (1997), sharing with it the ability to better model and learn long-term dependencies. This is made possible by having computation paths in the unfolded RNN for which the product of derivatives is close to 1. These paths allow gradients to flow backward easily without suffering too much from the vanishing effect (Hochreiter, 1991; Bengio _et al._ , 1994; Pascanu _et al._ , 2013a). It is therefore possible to use LSTM units instead of the gated hidden unit described here, as was done in a similar context by Sutskever _et al._ (2014). 

The new state _si_ of the RNN employing _n_ gated hidden units<sup>8</sup> is computed by 



where _◦_ is an element-wise multiplication, and _zi_ is the output of the update gates (see below). The proposed updated state ˜ _si_ is computed by 



where _e_ ( _yi−_ 1) _∈_ R<sup>_m_</sup> is an _m_ -dimensional embedding of a word _yi−_ 1, and _ri_ is the output of the reset gates (see below). When _yi_ is represented as a 1-of- _K_ vector, _e_ ( _yi_ ) is simply a column of an embedding matrix _E ∈_ R<sup>_m×K_</sup> . Whenever possible, we omit bias terms to make the equations less cluttered. 

The update gates _zi_ allow each hidden unit to maintain its previous activation, and the reset gates _ri_ control how much and what information from the previous state should be reset. We compute them by 



where _σ_ ( _·_ ) is a logistic sigmoid function.

---

[referencia=c23bf2a3bc33cb7a score=0.076]
- Hermann, K. and Blunsom, P. (2014). Multilingual distributed representations without word alignment. In _Proceedings of the Second International Conference on Learning Representations (ICLR 2014)_ . 

- Hochreiter, S. (1991). Untersuchungen zu dynamischen neuronalen Netzen. Diploma thesis, Institut f¨ur Informatik, Lehrstuhl Prof. Brauer, Technische Universit¨at M¨unchen. 

- Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. _Neural Computation_ , **9** (8), 1735–1780. 

- Kalchbrenner, N. and Blunsom, P. (2013). Recurrent continuous translation models. In _Proceedings of the ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1700–1709. Association for Computational Linguistics. 

- Koehn, P. (2010). _Statistical Machine Translation_ . Cambridge University Press, New York, NY, USA. 

- Koehn, P., Och, F. J., and Marcu, D. (2003). Statistical phrase-based translation. In _Proceedings of the 2003 Conference of the North American Chapter of the Association for Computational Linguistics on Human Language Technology - Volume 1_ , NAACL ’03, pages 48–54, Stroudsburg, PA, USA. Association for Computational Linguistics. 

- Pascanu, R., Mikolov, T., and Bengio, Y. (2013a). On the difficulty of training recurrent neural networks. In _ICML’2013_ . 

- Pascanu, R., Mikolov, T., and Bengio, Y. (2013b). On the difficulty of training recurrent neural networks. In _Proceedings of the 30th International Conference on Machine Learning (ICML 2013)_ . 

- Pascanu, R., Gulcehre, C., Cho, K., and Bengio, Y. (2014). How to construct deep recurrent neural networks. In _Proceedings of the Second International Conference on Learning Representations (ICLR 2014)_ .

---

[referencia=c23bf2a3bc33cb7a score=0.064]
### 5.2.2 LONG SENTENCES 

As clearly visible from Fig. 2 the proposed model (RNNsearch) is much better than the conventional model (RNNencdec) at translating long sentences. This is likely due to the fact that the RNNsearch does not require encoding a long sentence into a fixed-length vector perfectly, but only accurately encoding the parts of the input sentence that surround a particular word. 

As an example, consider this source sentence from the test set: 

_An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre_ _<u>to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.</u>_

---

[referencia=c23bf2a3bc33cb7a score=0.056]
- Axelrod, A., He, X., and Gao, J. (2011). Domain adaptation via pseudo in-domain data selection. In _Proceedings of the ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 355–362. Association for Computational Linguistics. 

- Bastien, F., Lamblin, P., Pascanu, R., Bergstra, J., Goodfellow, I. J., Bergeron, A., Bouchard, N., and Bengio, Y. (2012). Theano: new features and speed improvements. Deep Learning and Unsupervised Feature Learning NIPS 2012 Workshop. 

- Bengio, Y., Simard, P., and Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. _IEEE Transactions on Neural Networks_ , **5** (2), 157–166. 

- Bengio, Y., Ducharme, R., Vincent, P., and Janvin, C. (2003). A neural probabilistic language model. _J. Mach. Learn. Res._ , **3** , 1137–1155. 

- Bergstra, J., Breuleux, O., Bastien, F., Lamblin, P., Pascanu, R., Desjardins, G., Turian, J., WardeFarley, D., and Bengio, Y. (2010). Theano: a CPU and GPU math expression compiler. In _Proceedings of the Python for Scientific Computing Conference (SciPy)_ . Oral Presentation. 

- Boulanger-Lewandowski, N., Bengio, Y., and Vincent, P. (2013). Audio chord recognition with recurrent neural networks. In _ISMIR_ . 

- Cho, K., van Merrienboer, B., Gulcehre, C., Bougares, F., Schwenk, H., and Bengio, Y. (2014a). Learning phrase representations using RNN encoder-decoder for statistical machine translation. In _Proceedings of the Empiricial Methods in Natural Language Processing (EMNLP 2014)_ . to appear.

---

[referencia=c23bf2a3bc33cb7a score=0.055]
#### 10 ~~RNNsearch-50~~ 

RNNsearch-30 5 ~~RNNenc-50~~ RNNenc-30 0 0 10 20 30 40 Sentence length 

2012 and news-test-2013 to make a development (validation) set, and evaluate the models on the test set (news-test-2014) from WMT ’14, which consists of 3003 sentences not present in the training data. After a usual tokenization<sup>6</sup> , we use a shortlist of 30,000 most frequent words in each language to train our models. Any word not included in the shortlist is mapped to a special token ([UNK]). We do not apply any other special preprocessing, such as lowercasing or stemming, to the data. 

4.2 MODELS 

We train two types of models. The first one is an RNN Encoder–Decoder (RNNencdec, Cho _et al._ , 2014a), and the other is the proposed model, to which we refer as RNNsearch. We train each model twice: first with the sentences of length up to 30 words (RNNencdec-30, RNNsearch-30) and then with the sentences of length up to 50 word (RNNencdec-50, RNNsearch-50). 

The encoder and decoder of the RNNencdec have 1000 hidden units each.<sup>7</sup> The encoder of the RNNsearch consists of forward and backward recurrent neural networks (RNN) each having 1000 hidden units. Its decoder has 1000 hidden units. In both cases, we use a multilayer network with a single maxout (Goodfellow _et al._ , 2013) hidden layer to compute the conditional probability of each target word (Pascanu _et al._ , 2014). We use a minibatch stochastic gradient descent (SGD) algorithm together with Adadelta (Zeiler, 2012) to train each model. Each SGD update direction is computed using a minibatch of 80 sentences. We trained each model for approximately 5 days.

---

[referencia=c23bf2a3bc33cb7a score=0.045]
## B TRAINING PROCEDURE 

### B.1 PARAMETER INITIALIZATION 

We initialized the recurrent weight matrices _U, Uz, Ur,_<sup>_←−_</sup> _U ,_<sup>_←−_</sup> _U z,_<sup>_←−_</sup> _U r,_<sup>_−→_</sup> _U ,_<sup>_−→_</sup> _U z_ and<sup>_−→_</sup> _U r_ as random orthogonal matrices. For _Wa_ and _Ua_ , we initialized them by sampling each element from the Gaussian distribution of mean 0 and variance 0 _._ 001<sup>2</sup> . All the elements of _Va_ and all the bias vectors were initialized to zero. Any other weight matrix was initialized by sampling from the Gaussian distribution of mean 0 and variance 0 _._ 01<sup>2</sup> . 

### B.2 TRAINING 

We used the stochastic gradient descent (SGD) algorithm. Adadelta (Zeiler, 2012) was used to automatically adapt the learning rate of each parameter ( _ϵ_ = 10<sup>_−_6</sup> and _ρ_ = 0 _._ 95). We explicitly 

14 

Published as a conference paper at ICLR 2015 

normalized the _L_ 2-norm of the gradient of the cost function each time to be at most a predefined threshold of 1, when the norm was larger than the threshold (Pascanu _et al._ , 2013b). Each SGD update direction was computed with a minibatch of 80 sentences. 

At each update our implementation requires time proportional to the length of the longest sentence in a minibatch. Hence, to minimize the waste of computation, before every 20-th update, we retrieved 1600 sentence pairs, sorted them according to the lengths and split them into 20 minibatches. The training data was shuffled once before training and was traversed sequentially in this manner. 

In Tables 2 we present the statistics related to training all the models used in the experiments.

---

[referencia=c23bf2a3bc33cb7a score=0.042]
## 2 BACKGROUND: NEURAL MACHINE TRANSLATION 

From a probabilistic perspective, translation is equivalent to finding a target sentence **y** that maximizes the conditional probability of **y** given a source sentence **x** , i.e., arg max **y** _p_ ( **y** _|_ **x** ). In neural machine translation, we fit a parameterized model to maximize the conditional probability of sentence pairs using a parallel training corpus. Once the conditional distribution is learned by a translation model, given a source sentence a corresponding translation can be generated by searching for the sentence that maximizes the conditional probability. 

Recently, a number of papers have proposed the use of neural networks to directly learn this conditional distribution (see, e.g., Kalchbrenner and Blunsom, 2013; Cho _et al._ , 2014a; Sutskever _et al._ , 2014; Cho _et al._ , 2014b; Forcada and Neco, 1997).<sup>˜</sup> This neural machine translation approach typically consists of two components, the first of which encodes a source sentence **x** and the second decodes to a target sentence **y** . For instance, two recurrent neural networks (RNN) were used by (Cho _et al._ , 2014a) and (Sutskever _et al._ , 2014) to encode a variable-length source sentence into a fixed-length vector and to decode the vector into a variable-length target sentence. 

Despite being a quite new approach, neural machine translation has already shown promising results. Sutskever _et al._ (2014) reported that the neural machine translation based on RNNs with long shortterm memory (LSTM) units achieves close to the state-of-the-art performance of the conventional phrase-based machine translation system on an English-to-French translation task.<sup>1</sup> Adding neural components to existing translation systems, for instance, to score the phrase pairs in the phrase table (Cho _et al._ , 2014a) or to re-rank candidate translations (Sutskever _et al._ , 2014), has allowed to surpass the previous state-of-the-art performance level.

---

[referencia=c23bf2a3bc33cb7a score=0.035]
### 6.2 NEURAL NETWORKS FOR MACHINE TRANSLATION 

Since Bengio _et al._ (2003) introduced a neural probabilistic language model which uses a neural network to model the conditional probability of a word given a fixed number of the preceding words, neural networks have widely been used in machine translation. However, the role of neural networks has been largely limited to simply providing a single feature to an existing statistical machine translation system or to re-rank a list of candidate translations provided by an existing system. 

For instance, Schwenk (2012) proposed using a feedforward neural network to compute the score of a pair of source and target phrases and to use the score as an additional feature in the phrase-based statistical machine translation system. More recently, Kalchbrenner and Blunsom (2013) and Devlin _et al._ (2014) reported the successful use of the neural networks as a sub-component of the existing translation system. Traditionally, a neural network trained as a target-side language model has been used to rescore or rerank a list of candidate translations (see, e.g., Schwenk _et al._ , 2006). 

Although the above approaches were shown to improve the translation performance over the stateof-the-art machine translation systems, we are more interested in a more ambitious objective of designing a completely new translation system based on neural networks. The neural machine translation approach we consider in this paper is therefore a radical departure from these earlier works. Rather than using a neural network as a part of the existing system, our model works on its own and generates a translation from a source sentence directly.