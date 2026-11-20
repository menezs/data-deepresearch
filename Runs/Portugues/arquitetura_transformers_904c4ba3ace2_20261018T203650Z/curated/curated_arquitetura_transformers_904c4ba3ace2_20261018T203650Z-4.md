[referencia=b6909588ff7b9ebf score=0.023]
# NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE 

### **Dzmitry Bahdanau** 

Jacobs University Bremen, Germany 

**KyungHyun Cho Yoshua Bengio**<sup>_∗_</sup> Universit´e de Montr´eal 

## ABSTRACT 

Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

---

[referencia=b6909588ff7b9ebf score=0.003]
### 5.2 QUALITATIVE ANALYSIS 

### 5.2.1 ALIGNMENT 

The proposed approach provides an intuitive way to inspect the (soft-)alignment between the words in a generated translation and those in a source sentence. This is done by visualizing the annotation weights _αij_ from Eq. (6), as in Fig. 3. Each row of a matrix in each plot indicates the weights associated with the annotations. From this we see which positions in the source sentence were considered more important when generating the target word. 

We can see from the alignments in Fig. 3 that the alignment of words between English and French is largely monotonic. We see strong weights along the diagonal of each matrix. However, we also observe a number of non-trivial, non-monotonic alignments. Adjectives and nouns are typically ordered differently between French and English, and we see an example in Fig. 3 (a). From this figure, we see that the model correctly translates a phrase [European Economic Area] into [zone ´economique europ´een]. The RNNsearch was able to correctly align [zone] with [Area], jumping over the two words ([European] and [Economic]), and then looked one word back at a time to complete the whole phrase [zone ´economique europ´eenne]. 

The strength of the soft-alignment, opposed to a hard-alignment, is evident, for instance, from Fig. 3 (d). Consider the source phrase [the man] which was translated into [l’ homme]. Any hard alignment will map [the] to [l’] and [man] to [homme]. This is not helpful for translation, as one must consider the word following [the] to determine whether it should be translated into [le], [la], [les] or [l’]. Our soft-alignment solves this issue naturally by letting the model look at both [the] and [man], and in this example, we see that the model was able to correctly translate [the] into [l’]. We observe similar behaviors in all the presented cases in Fig. 3. An additional benefit of the soft alignment is that it naturally deals with source and target phrases of different lengths, without requiring a counter-intuitive way of mapping some words to or from nowhere ([NULL]) (see, e.g., Chapters 4 and 5 of Koehn, 2010).

---

[referencia=b6909588ff7b9ebf score=0.000]
### A.2.2 DECODER 

The hidden state _si_ of the decoder given the annotations from the encoder is computed by 



where 



_E_ is the word embedding matrix for the target language. _W, Wz, Wr ∈_ R<sup>_n×m_</sup> , _U, Uz, Ur ∈_ R<sup>_n×n_</sup> , and _C, Cz, Cr ∈_ R<sup>_n×_2</sup><sup>_n_</sup> are weights. Again, _m_ and _n_ are the word embedding dimensionality and the number of hidden units, respectively. The initial hidden state _s_ 0 is computed by _s_ 0 = _←−_ tanh _Ws h_ 1 _,_ where _Ws ∈_ R<sup>_n×n_</sup> . � � 

The context vector _ci_ are recomputed at each step by the alignment model: 



13 

Published as a conference paper at ICLR 2015 

|Model|Updates (_×_10<sup>5</sup>)|Epochs|Hours|GPU|Train NLL|Dev. NLL|
|---|---|---|---|---|---|---|
|RNNenc-30|8.46|6.4|109|TITAN BLACK|28.1|53.0|
|RNNenc-50|6.00|4.5|108|Quadro K-6000|44.0|43.6|
|RNNsearch-30|4.71|3.6|113|TITAN BLACK|26.7|47.2|
|RNNsearch-50|2.88|2.2|111|Quadro K-6000|40.7|38.1|
|RNNsearch-50<sup>_⋆_</sup>|6.67|5.0|252|Quadro K-6000|36.7|35.2|



Table 2: Learning statistics and relevant information. Each update corresponds to updating the parameters once using a single minibatch. One epoch is one pass through the training set. NLL is the average conditional log-probabilities of the sentences in either the training set or the development set. Note that the lengths of the sentences differ. 

where

---

[referencia=b6909588ff7b9ebf score=0.000]
## A MODEL ARCHITECTURE 

### A.1 ARCHITECTURAL CHOICES 

The proposed scheme in Section 3 is a general framework where one can freely define, for instance, the activation functions _f_ of recurrent neural networks (RNN) and the alignment model _a_ . Here, we describe the choices we made for the experiments in this paper.

---

[referencia=b6909588ff7b9ebf score=0.000]
> _∗_ CIFAR Senior Fellow 

1 

Published as a conference paper at ICLR 2015 

The most important distinguishing feature of this approach from the basic encoder–decoder is that it does not attempt to encode a whole input sentence into a single fixed-length vector. Instead, it encodes the input sentence into a sequence of vectors and chooses a subset of these vectors adaptively while decoding the translation. This frees a neural translation model from having to squash all the information of a source sentence, regardless of its length, into a fixed-length vector. We show this allows a model to cope better with long sentences. 

In this paper, we show that the proposed approach of jointly learning to align and translate achieves significantly improved translation performance over the basic encoder–decoder approach. The improvement is more apparent with longer sentences, but can be observed with sentences of any length. On the task of English-to-French translation, the proposed approach achieves, with a single model, a translation performance comparable, or close, to the conventional phrase-based system. Furthermore, qualitative analysis reveals that the proposed model finds a linguistically plausible (soft-)alignment between a source sentence and the corresponding target sentence.

---

[referencia=b6909588ff7b9ebf score=0.000]
3 

Published as a conference paper at ICLR 2015 

the alignment is not considered to be a latent variable. Instead, the alignment model directly computes a soft alignment, which allows the gradient of the cost function to be backpropagated through. This gradient can be used to train the alignment model as well as the whole translation model jointly. We can understand the approach of taking a weighted sum of all the annotations as computing an _expected annotation_ , where the expectation is over possible alignments. Let _αij_ be a probability that the target word _yi_ is aligned to, or translated from, a source word _xj_ . Then, the _i_ -th context vector _ci_ is the expected annotation over all the annotations with probabilities _αij_ . 

The probability _αij_ , or its associated energy _eij_ , reflects the importance of the annotation _hj_ with respect to the previous hidden state _si−_ 1 in deciding the next state _si_ and generating _yi_ . Intuitively, this implements a mechanism of attention in the decoder. The decoder decides parts of the source sentence to pay attention to. By letting the decoder have an attention mechanism, we relieve the encoder from the burden of having to encode all information in the source sentence into a fixedlength vector. With this new approach the information can be spread throughout the sequence of annotations, which can be selectively retrieved by the decoder accordingly.

---

[referencia=b6909588ff7b9ebf score=0.000]
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

[referencia=b6909588ff7b9ebf score=0.000]
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

[referencia=b6909588ff7b9ebf score=0.000]
- Axelrod, A., He, X., and Gao, J. (2011). Domain adaptation via pseudo in-domain data selection. In _Proceedings of the ACL Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 355–362. Association for Computational Linguistics. 

- Bastien, F., Lamblin, P., Pascanu, R., Bergstra, J., Goodfellow, I. J., Bergeron, A., Bouchard, N., and Bengio, Y. (2012). Theano: new features and speed improvements. Deep Learning and Unsupervised Feature Learning NIPS 2012 Workshop. 

- Bengio, Y., Simard, P., and Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. _IEEE Transactions on Neural Networks_ , **5** (2), 157–166. 

- Bengio, Y., Ducharme, R., Vincent, P., and Janvin, C. (2003). A neural probabilistic language model. _J. Mach. Learn. Res._ , **3** , 1137–1155. 

- Bergstra, J., Breuleux, O., Bastien, F., Lamblin, P., Pascanu, R., Desjardins, G., Turian, J., WardeFarley, D., and Bengio, Y. (2010). Theano: a CPU and GPU math expression compiler. In _Proceedings of the Python for Scientific Computing Conference (SciPy)_ . Oral Presentation. 

- Boulanger-Lewandowski, N., Bengio, Y., and Vincent, P. (2013). Audio chord recognition with recurrent neural networks. In _ISMIR_ . 

- Cho, K., van Merrienboer, B., Gulcehre, C., Bougares, F., Schwenk, H., and Bengio, Y. (2014a). Learning phrase representations using RNN encoder-decoder for statistical machine translation. In _Proceedings of the Empiricial Methods in Natural Language Processing (EMNLP 2014)_ . to appear.

---

[referencia=b6909588ff7b9ebf score=0.000]
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

[referencia=b6909588ff7b9ebf score=0.000]
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

[referencia=b6909588ff7b9ebf score=0.000]
and mixture coefficient of each kernel was predicted from an alignment model. More specifically, his alignment was restricted to predict the location such that the location increases monotonically. The main difference from our approach is that, in (Graves, 2013), the modes of the weights of the annotations only move in one direction. In the context of machine translation, this is a severe limitation, as (long-distance) reordering is often needed to generate a grammatically correct translation (for instance, English-to-German). 

Our approach, on the other hand, requires computing the annotation weight of every word in the source sentence for each word in the translation. This drawback is not severe with the task of translation in which most of input and output sentences are only 15–40 words. However, this may limit the applicability of the proposed scheme to other tasks. 

8 

Published as a conference paper at ICLR 2015

---

[referencia=b6909588ff7b9ebf score=0.000]
- Pouget-Abadie, J., Bahdanau, D., van Merri¨enboer, B., Cho, K., and Bengio, Y. (2014). Overcoming the curse of sentence length for neural machine translation using automatic segmentation. In _Eighth Workshop on Syntax, Semantics and Structure in Statistical Translation_ . to appear. 

- Schuster, M. and Paliwal, K. K. (1997). Bidirectional recurrent neural networks. _Signal Processing, IEEE Transactions on_ , **45** (11), 2673–2681. 

- Schwenk, H. (2012). Continuous space translation models for phrase-based statistical machine translation. In M. Kay and C. Boitet, editors, _Proceedings of the 24th International Conference on Computational Linguistics (COLIN)_ , pages 1071–1080. Indian Institute of Technology Bombay. 

- Schwenk, H., Dchelotte, D., and Gauvain, J.-L. (2006). Continuous space language models for statistical machine translation. In _Proceedings of the COLING/ACL on Main conference poster sessions_ , pages 723–730. Association for Computational Linguistics. 

- Sutskever, I., Vinyals, O., and Le, Q. (2014). Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems (NIPS 2014)_ . 

Zeiler, M. D. (2012). ADADELTA: An adaptive learning rate method. _arXiv:_ 1212.5701 [cs.LG]. 

11 

Published as a conference paper at ICLR 2015

---

[referencia=b6909588ff7b9ebf score=0.000]
Figure 3: Four sample alignments found by RNNsearch-50. The x-axis and y-axis of each plot correspond to the words in the source sentence (English) and the generated translation (French), respectively. Each pixel shows the weight _αij_ of the annotation of the _j_ -th source word for the _i_ -th target word (see Eq. (6)), in grayscale (0: black, 1: white). (a) an arbitrary sentence. (b–d) three randomly selected samples among the sentences without any unknown words and of length between 10 and 20 words from the test set. 

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

---

[referencia=b6909588ff7b9ebf score=0.000]
where **y** = � _y_ 1 _, · · · , yTy_ �. With an RNN, each conditional probability is modeled as _p_ ( _yt | {y_ 1 _, · · · , yt−_ 1 _} , c_ ) = _g_ ( _yt−_ 1 _, st, c_ ) _,_ (3) 

where _g_ is a nonlinear, potentially multi-layered, function that outputs the probability of _yt_ , and _st_ is the hidden state of the RNN. It should be noted that other architectures such as a hybrid of an RNN and a de-convolutional neural network can be used (Kalchbrenner and Blunsom, 2013). 

3 LEARNING TO ALIGN AND TRANSLATE 

In this section, we propose a novel architecture for neural machine translation. The new architecture consists of a bidirectional RNN as an encoder (Sec. 3.2) and a decoder that emulates searching through a source sentence during decoding a translation (Sec. 3.1).

---

[referencia=b6909588ff7b9ebf score=0.000]
where 



and _hj_ is the _j_ -th annotation in the source sentence (see Eq. (7)). _va ∈_ R<sup>_n′_</sup> _, Wa ∈_ R<sup>_n′×n_</sup> and _Ua ∈_ R<sup>_n′×_2</sup><sup>_n_</sup> are weight matrices. Note that the model becomes RNN Encoder–Decoder (Cho _et al._ , 2014a), if we fix _ci_ to<sup>_−→_</sup> _h Tx_ . 

With the decoder state _si−_ 1, the context _ci_ and the last generated word _yi−_ 1, we define the probability of a target word _yi_ as 



where 



and _t_<sup>˜</sup> _i,k_ is the _k_ -th element of a vector _t_<sup>˜</sup> _i_ which is computed by 



_Wo ∈_ R<sup>_Ky×l_</sup> , _Uo ∈_ R<sup>2</sup><sup>_l×n_</sup> , _Vo ∈_ R<sup>2</sup><sup>_l×m_</sup> and _Co ∈_ R<sup>2</sup><sup>_l×_2</sup><sup>_n_</sup> are weight matrices. This can be understood as having a deep output (Pascanu _et al._ , 2014) with a single maxout hidden layer (Goodfellow _et al._ , 2013). 

### A.2.3 MODEL SIZE 

For all the models used in this paper, the size of a hidden layer _n_ is 1000, the word embedding dimensionality _m_ is 620 and the size of the maxout hidden layer in the deep output _l_ is 500. The number of hidden units in the alignment model _n_<sup>_′_</sup> is 1000.

---

[referencia=b6909588ff7b9ebf score=0.000]
## 7 CONCLUSION 

The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from which a translation will be decoded. We conjectured that the use of a fixed-length context vector is problematic for translating long sentences, based on a recent empirical study reported by Cho _et al._ (2014b) and Pouget-Abadie _et al._ (2014). 

In this paper, we proposed a novel architecture that addresses this issue. We extended the basic encoder–decoder by letting a model (soft-)search for a set of input words, or their annotations computed by an encoder, when generating each target word. This frees the model from having to encode a whole source sentence into a fixed-length vector, and also lets the model focus only on information relevant to the generation of the next target word. This has a major positive impact on the ability of the neural machine translation system to yield good results on longer sentences. Unlike with the traditional machine translation systems, all of the pieces of the translation system, including the alignment mechanism, are jointly trained towards a better log-probability of producing correct translations. 

We tested the proposed model, called RNNsearch, on the task of English-to-French translation. The experiment revealed that the proposed RNNsearch outperforms the conventional encoder–decoder model (RNNencdec) significantly, regardless of the sentence length and that it is much more robust to the length of a source sentence. From the qualitative analysis where we investigated the (soft-)alignment generated by the RNNsearch, we were able to conclude that the model can correctly align each target word with the relevant words, or their annotations, in the source sentence as it generated a correct translation. 

Perhaps more importantly, the proposed approach achieved a translation performance comparable to the existing phrase-based statistical machine translation. It is a striking result, considering that the proposed architecture, or the whole family of neural machine translation, has only been proposed as recently as this year. We believe the architecture proposed here is a promising step toward better machine translation and a better understanding of natural languages in general. 

One of challenges left for the future is to better handle unknown, or rare words. This will be required for the model to be more widely used and to match the performance of current state-of-the-art machine translation systems in all contexts. 

9 

Published as a conference paper at ICLR 2015

---

[referencia=b6909588ff7b9ebf score=0.000]
Figure 2: The BLEU scores of the generated translations on the test set with respect to the lengths of the sentences. The results are on the full test set which includes sentences having unknown words to the models. 

2012 and news-test-2013 to make a development (validation) set, and evaluate the models on the test set (news-test-2014) from WMT ’14, which consists of 3003 sentences not present in the training data. 

After a usual tokenization<sup>6</sup> , we use a shortlist of 30,000 most frequent words in each language to train our models. Any word not included in the shortlist is mapped to a special token ([UNK]). We do not apply any other special preprocessing, such as lowercasing or stemming, to the data.

---

[referencia=b6909588ff7b9ebf score=0.000]
3.2 ENCODER: BIDIRECTIONAL RNN FOR ANNOTATING SEQUENCES The usual RNN, described in Eq. (1), reads an input sequence **x** in order starting from the first symbol _x_ 1 to the last one _xTx_ . However, in the proposed scheme, we would like the annotation of each word to summarize not only the preceding words, but also the following words. Hence, we propose to use a bidirectional RNN (BiRNN, Schuster and Paliwal, 1997), which has been successfully used recently in speech recognition (see, e.g., Graves _et al._ , 2013). A BiRNN consists of forward and backward RNN’s. The forward RNN<sup>_−→_</sup> _f_ reads the input sequence Theas it is ordered (frombackward RNN _x_<sup>_←−_</sup> _f_ 1 toreads _xTx_ ) and calculates a sequence ofthe sequence in the reverse _forward hidden states_ order (from _xTx_ to _x_ (1),<sup>_−→_</sup> _h_ resulting1 _, · · · ,_<sup>_−→_</sup> _h T_ in _x_ )a. sequence of _backward hidden states_ (<sup>_←−_</sup> _h_ 1 _, · · · ,_<sup>_←−_</sup> _h Tx_ ). We obtain an annotation for each word _xj_ by concatenating the forward hidden state<sup>_−→_</sup> _h j_ and the _−→ ⊤_ backward one<sup>_←−_</sup> _h j_ , i.e., _hj_ = � _h ⊤j_<sup>;</sup><sup>_←−h⊤_</sup> _j_ � . In this way, the annotation _hjj_ contains the summaries 

. In this way, the annotation _hjj_ contains the summaries 

of both the preceding words and the following words. Due to the tendency of RNNs to better represent recent inputs, the annotation _hj_ will be focused on the words around _xj_ . This sequence of annotations is used by the decoder and the alignment model later to compute the context vector (Eqs. (5)–(6)).

---

[referencia=b6909588ff7b9ebf score=0.000]
Table 1: BLEU scores of the trained models computed on the test set. The second and third columns show respectively the scores on all the sentences and, on the sentences without any unknown word in themselves and in the reference translations. Note that RNNsearch-50<sup>_⋆_</sup> was trained much longer until the performance on the development set stopped improving. ( _◦_ ) We disallowed the models to generate [UNK] tokens when only the sentences having no unknown words were evaluated (last column). 

### 5.2 QUALITATIVE ANALYSIS