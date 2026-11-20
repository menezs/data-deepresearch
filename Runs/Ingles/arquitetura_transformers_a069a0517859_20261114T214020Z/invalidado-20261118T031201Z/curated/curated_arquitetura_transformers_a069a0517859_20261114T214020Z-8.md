[referencia=c23bf2a3bc33cb7a score=0.972]
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

[referencia=c23bf2a3bc33cb7a score=0.848]
### 4.1 DATASET 

WMT ’14 contains the following English-French parallel corpora: Europarl (61M words), news commentary (5.5M), UN (421M) and two crawled corpora of 90M and 272.5M words respectively, totaling 850M words. Following the procedure described in Cho _et al._ (2014a), we reduce the size of the combined corpus to have 348M words using the data selection method by Axelrod _et al._ (2011).<sup>5</sup> We do not use any monolingual data other than the mentioned parallel corpora, although it may be possible to use a much larger monolingual corpus to pretrain an encoder. We concatenate news-test- 

> 3 http://www.statmt.org/wmt14/translation-task.html 

> 4 Implementations are available at https://github.com/lisa-groundhog/GroundHog. 

> 5 Available online at http://www-lium.univ-lemans.fr/˜schwenk/cslm_joint_paper/. 

4 

Published as a conference paper at ICLR 2015 

30 25 20 15 10 



<!-- Start of picture text -->
Figure 2: The BLEU scores<br>of the generated translations<br>on the test set with respect<br>to the lengths of the sen-<br>RNNsearch-50 tences. The results are on<br>RNNsearch-30 the full test set which in-<br>RNNenc-50 cludes sentences having un-<br>RNNenc-30 known words to the models.<br>0 10 20 30 40 50 60<br><!-- End of picture text -->

---

[referencia=c23bf2a3bc33cb7a score=0.824]
#### 10 ~~RNNsearch-50~~ 

RNNsearch-30 5 ~~RNNenc-50~~ RNNenc-30 0 0 10 20 30 40 Sentence length 

2012 and news-test-2013 to make a development (validation) set, and evaluate the models on the test set (news-test-2014) from WMT ’14, which consists of 3003 sentences not present in the training data. After a usual tokenization<sup>6</sup> , we use a shortlist of 30,000 most frequent words in each language to train our models. Any word not included in the shortlist is mapped to a special token ([UNK]). We do not apply any other special preprocessing, such as lowercasing or stemming, to the data. 

4.2 MODELS 

We train two types of models. The first one is an RNN Encoder–Decoder (RNNencdec, Cho _et al._ , 2014a), and the other is the proposed model, to which we refer as RNNsearch. We train each model twice: first with the sentences of length up to 30 words (RNNencdec-30, RNNsearch-30) and then with the sentences of length up to 50 word (RNNencdec-50, RNNsearch-50). 

The encoder and decoder of the RNNencdec have 1000 hidden units each.<sup>7</sup> The encoder of the RNNsearch consists of forward and backward recurrent neural networks (RNN) each having 1000 hidden units. Its decoder has 1000 hidden units. In both cases, we use a multilayer network with a single maxout (Goodfellow _et al._ , 2013) hidden layer to compute the conditional probability of each target word (Pascanu _et al._ , 2014). We use a minibatch stochastic gradient descent (SGD) algorithm together with Adadelta (Zeiler, 2012) to train each model. Each SGD update direction is computed using a minibatch of 80 sentences. We trained each model for approximately 5 days.

---

[referencia=c23bf2a3bc33cb7a score=0.744]
> 7 In this paper, by a ’hidden unit’, we always mean the gated hidden unit (see Appendix A.1.1). 

5 

Published as a conference paper at ICLR 2015 



<!-- Start of picture text -->
L'<br>accord Il<br>convient<br>sur<br>de<br>la noter<br>zone que<br>économique l'<br>européenne environnement<br>marin<br>a<br>est<br>été le<br>signé moins<br>en connu<br>août de<br>l'<br>1992<br>environnement<br>. .<br><end> <end><br>(a) (b)<br>La<br>destruction "<br>de Cela<br>l' va<br>équipement changer<br>signifie mon<br>que avenir<br>la avec<br>Syrie ma<br>ne famille<br>peut "<br>plus<br>produire ,<br>de a<br>nouvelles dit<br>armes l'<br>chimiques homme<br>. .<br><end> <end><br>(c) (d)<br>The agreement on the European Economic Area was signed in August 1992 . <end><br>It should be noted that the marine environment is the least known of environments . <end><br>Destruction of the equipment means that Syria can no longer produce new chemical weapons . <end><br>" This will change my future with my family , " the man said . <end><br><!-- End of picture text -->





Figure 3: Four sample alignments found by RNNsearch-50. The x-axis and y-axis of each plot correspond to the words in the source sentence (English) and the generated translation (French), respectively. Each pixel shows the weight _αij_ of the annotation of the _j_ -th source word for the _i_ -th target word (see Eq. (6)), in grayscale (0: black, 1: white). (a) an arbitrary sentence. (b–d) three randomly selected samples among the sentences without any unknown words and of length between 10 and 20 words from the test set.

---

[referencia=c23bf2a3bc33cb7a score=0.743]
## 7 CONCLUSION 

The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from which a translation will be decoded. We conjectured that the use of a fixed-length context vector is problematic for translating long sentences, based on a recent empirical study reported by Cho _et al._ (2014b) and Pouget-Abadie _et al._ (2014). 

In this paper, we proposed a novel architecture that addresses this issue. We extended the basic encoder–decoder by letting a model (soft-)search for a set of input words, or their annotations computed by an encoder, when generating each target word. This frees the model from having to encode a whole source sentence into a fixed-length vector, and also lets the model focus only on information relevant to the generation of the next target word. This has a major positive impact on the ability of the neural machine translation system to yield good results on longer sentences. Unlike with the traditional machine translation systems, all of the pieces of the translation system, including the alignment mechanism, are jointly trained towards a better log-probability of producing correct translations. 

We tested the proposed model, called RNNsearch, on the task of English-to-French translation. The experiment revealed that the proposed RNNsearch outperforms the conventional encoder–decoder model (RNNencdec) significantly, regardless of the sentence length and that it is much more robust to the length of a source sentence. From the qualitative analysis where we investigated the (soft-)alignment generated by the RNNsearch, we were able to conclude that the model can correctly align each target word with the relevant words, or their annotations, in the source sentence as it generated a correct translation. 

Perhaps more importantly, the proposed approach achieved a translation performance comparable to the existing phrase-based statistical machine translation. It is a striking result, considering that the proposed architecture, or the whole family of neural machine translation, has only been proposed as recently as this year. We believe the architecture proposed here is a promising step toward better machine translation and a better understanding of natural languages in general. 

One of challenges left for the future is to better handle unknown, or rare words. This will be required for the model to be more widely used and to match the performance of current state-of-the-art machine translation systems in all contexts. 

9 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.720]
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

[referencia=c23bf2a3bc33cb7a score=0.686]
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

[referencia=c23bf2a3bc33cb7a score=0.575]
Again, the RNNsearch-50 was able to translate this long sentence correctly: 

_Ce genre d’exp´erience fait partie des efforts de Disney pour ”prolonger la dur´ee de vie de ses s´eries et cr´eer de nouvelles relations avec des publics_ _<u>via des plateformes numeriques´ de plus en plus importantes”, a-t-il ajoute.´</u>_ 

In conjunction with the quantitative results presented already, these qualitative observations confirm our hypotheses that the RNNsearch architecture enables far more reliable translation of long sentences than the standard RNNencdec model. 

In Appendix C, we provide a few more sample translations of long source sentences generated by the RNNencdec-50, RNNsearch-50 and Google Translate along with the reference translations.

---

[referencia=c23bf2a3bc33cb7a score=0.569]
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

[referencia=c23bf2a3bc33cb7a score=0.528]
### 5.2.2 LONG SENTENCES 

As clearly visible from Fig. 2 the proposed model (RNNsearch) is much better than the conventional model (RNNencdec) at translating long sentences. This is likely due to the fact that the RNNsearch does not require encoding a long sentence into a fixed-length vector perfectly, but only accurately encoding the parts of the input sentence that surround a particular word. 

As an example, consider this source sentence from the test set: 

_An admitting privilege is the right of a doctor to admit a patient to a hospital or a medical centre_ _<u>to carry out a diagnosis or a procedure, based on his status as a health care worker at a hospital.</u>_

---

[referencia=c23bf2a3bc33cb7a score=0.452]
### 5.2 QUALITATIVE ANALYSIS 

### 5.2.1 ALIGNMENT 

The proposed approach provides an intuitive way to inspect the (soft-)alignment between the words in a generated translation and those in a source sentence. This is done by visualizing the annotation weights _αij_ from Eq. (6), as in Fig. 3. Each row of a matrix in each plot indicates the weights associated with the annotations. From this we see which positions in the source sentence were considered more important when generating the target word. 

We can see from the alignments in Fig. 3 that the alignment of words between English and French is largely monotonic. We see strong weights along the diagonal of each matrix. However, we also observe a number of non-trivial, non-monotonic alignments. Adjectives and nouns are typically ordered differently between French and English, and we see an example in Fig. 3 (a). From this figure, we see that the model correctly translates a phrase [European Economic Area] into [zone ´economique europ´een]. The RNNsearch was able to correctly align [zone] with [Area], jumping over the two words ([European] and [Economic]), and then looked one word back at a time to complete the whole phrase [zone ´economique europ´eenne]. 

The strength of the soft-alignment, opposed to a hard-alignment, is evident, for instance, from Fig. 3 (d). Consider the source phrase [the man] which was translated into [l’ homme]. Any hard alignment will map [the] to [l’] and [man] to [homme]. This is not helpful for translation, as one must consider the word following [the] to determine whether it should be translated into [le], [la], [les] or [l’]. Our soft-alignment solves this issue naturally by letting the model look at both [the] and [man], and in this example, we see that the model was able to correctly translate [the] into [l’]. We observe similar behaviors in all the presented cases in Fig. 3. An additional benefit of the soft alignment is that it naturally deals with source and target phrases of different lengths, without requiring a counter-intuitive way of mapping some words to or from nowhere ([NULL]) (see, e.g., Chapters 4 and 5 of Koehn, 2010).

---

[referencia=c23bf2a3bc33cb7a score=0.426]
|RNNenc-50|Lors de la conf´erence de presse de jeudi, M. Blair a dit qu’il n’y avait rien dans cette vid´eo qui<br>pourrait constituer une ”motivation raisonnable” pouvant entraˆıner des accusations criminelles<br>port´ees contre le maire.|
|RNNsearch-50|Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vid´eo qui<br>pourrait constituer un ”motif raisonnable” qui pourrait conduire `a des accusations criminelles<br>contre le maire.|
|Google<br>Translate|Lors d’une conf´erence de presse jeudi, M. Blair a d´eclar´e qu’il n’y avait rien dans cette vido<br>qui pourrait constituer un ”motif raisonnable” qui pourrait mener `a des accusations criminelles<br>portes contre le maire.|



Table 3: The translations generated by RNNenc-50 and RNNsearch-50 from long source sentences (30 words or more) selected from the test set. For each source sentence, we also show the goldstandard translation. The translations by Google Translate were made on 27 August 2014. 

15

---

[referencia=c23bf2a3bc33cb7a score=0.320]
## 4 EXPERIMENT SETTINGS 

We evaluate the proposed approach on the task of English-to-French translation. We use the bilingual, parallel corpora provided by ACL WMT ’14.<sup>3</sup> As a comparison, we also report the performance of an RNN Encoder–Decoder which was proposed recently by Cho _et al._ (2014a). We use the same training procedures and the same dataset for both models.<sup>4</sup>

---

[referencia=c23bf2a3bc33cb7a score=0.258]
# NEURAL MACHINE TRANSLATION BY JOINTLY LEARNING TO ALIGN AND TRANSLATE 

### **Dzmitry Bahdanau** 

Jacobs University Bremen, Germany 

**KyungHyun Cho Yoshua Bengio**<sup>_∗_</sup> Universit´e de Montr´eal 

## ABSTRACT 

Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder–decoders and encode a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture, and propose to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

---

[referencia=c23bf2a3bc33cb7a score=0.194]
## 1 INTRODUCTION 

_Neural machine translation_ is a newly emerging approach to machine translation, recently proposed by Kalchbrenner and Blunsom (2013), Sutskever _et al._ (2014) and Cho _et al._ (2014b). Unlike the traditional phrase-based translation system (see, e.g., Koehn _et al._ , 2003) which consists of many small sub-components that are tuned separately, neural machine translation attempts to build and train a single, large neural network that reads a sentence and outputs a correct translation. 

Most of the proposed neural machine translation models belong to a family of _encoder– decoders_ (Sutskever _et al._ , 2014; Cho _et al._ , 2014a), with an encoder and a decoder for each language, or involve a language-specific encoder applied to each sentence whose outputs are then compared (Hermann and Blunsom, 2014). An encoder neural network reads and encodes a source sentence into a fixed-length vector. A decoder then outputs a translation from the encoded vector. The whole encoder–decoder system, which consists of the encoder and the decoder for a language pair, is jointly trained to maximize the probability of a correct translation given a source sentence. 

A potential issue with this encoder–decoder approach is that a neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector. This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus. Cho _et al._ (2014b) showed that indeed the performance of a basic encoder–decoder deteriorates rapidly as the length of an input sentence increases. 

In order to address this issue, we introduce an extension to the encoder–decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant information is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words. 

> _∗_ CIFAR Senior Fellow 

1 

Published as a conference paper at ICLR 2015

---

[referencia=c23bf2a3bc33cb7a score=0.153]
where 



and _hj_ is the _j_ -th annotation in the source sentence (see Eq. (7)). _va ∈_ R<sup>_n′_</sup> _, Wa ∈_ R<sup>_n′×n_</sup> and _Ua ∈_ R<sup>_n′×_2</sup><sup>_n_</sup> are weight matrices. Note that the model becomes RNN Encoder–Decoder (Cho _et al._ , 2014a), if we fix _ci_ to<sup>_−→_</sup> _h Tx_ . 

With the decoder state _si−_ 1, the context _ci_ and the last generated word _yi−_ 1, we define the probability of a target word _yi_ as 



where 



and _t_<sup>˜</sup> _i,k_ is the _k_ -th element of a vector _t_<sup>˜</sup> _i_ which is computed by 



_Wo ∈_ R<sup>_Ky×l_</sup> , _Uo ∈_ R<sup>2</sup><sup>_l×n_</sup> , _Vo ∈_ R<sup>2</sup><sup>_l×m_</sup> and _Co ∈_ R<sup>2</sup><sup>_l×_2</sup><sup>_n_</sup> are weight matrices. This can be understood as having a deep output (Pascanu _et al._ , 2014) with a single maxout hidden layer (Goodfellow _et al._ , 2013). 

### A.2.3 MODEL SIZE 

For all the models used in this paper, the size of a hidden layer _n_ is 1000, the word embedding dimensionality _m_ is 620 and the size of the maxout hidden layer in the deep output _l_ is 500. The number of hidden units in the alignment model _n_<sup>_′_</sup> is 1000.

---

[referencia=c23bf2a3bc33cb7a score=0.139]
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

[referencia=c23bf2a3bc33cb7a score=0.136]
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

[referencia=c23bf2a3bc33cb7a score=0.125]
Once a model is trained, we use a beam search to find a translation that approximately maximizes the conditional probability (see, e.g., Graves, 2012; Boulanger-Lewandowski _et al._ , 2013). Sutskever _et al._ (2014) used this approach to generate translations from their neural machine translation model. 

For more details on the architectures of the models and training procedure used in the experiments, see Appendices A and B. 

5 RESULTS 5.1 QUANTITATIVE RESULTS In Table 1, we list the translation performances measured in BLEU score. It is clear from the table that in all the cases, the proposed RNNsearch outperforms the conventional RNNencdec. More importantly, the performance of the RNNsearch is as high as that of the conventional phrase-based translation system (Moses), when only the sentences consisting of known words are considered. This is a significant achievement, considering that Moses uses a separate monolingual corpus (418M words) in addition to the parallel corpora we used to train the RNNsearch and RNNencdec. 

> 6 We used the tokenization script from the open-source machine translation package, Moses. 

> 7 In this paper, by a ’hidden unit’, we always mean the gated hidden unit (see Appendix A.1.1). 

5 

Published as a conference paper at ICLR 2015 



<!-- Start of picture text -->

---

[referencia=c23bf2a3bc33cb7a score=0.099]
### 3.2 ENCODER: BIDIRECTIONAL RNN FOR ANNOTATING SEQUENCES 

The usual RNN, described in Eq. (1), reads an input sequence **x** in order starting from the first symbol _x_ 1 to the last one _xTx_ . However, in the proposed scheme, we would like the annotation of each word to summarize not only the preceding words, but also the following words. Hence, we propose to use a bidirectional RNN (BiRNN, Schuster and Paliwal, 1997), which has been successfully used recently in speech recognition (see, e.g., Graves _et al._ , 2013). 

A BiRNN consists of forward and backward RNN’s. The forward RNN<sup>_−→_</sup> _f_ reads the input sequence Theas it is ordered (frombackward RNN _x_<sup>_←−_</sup> _f_ 1 toreads _xTx_ ) and calculates a sequence ofthe sequence in the reverse _forward hidden states_ order (from _xTx_ to _x_ (1),<sup>_−→_</sup> _h_ resulting1 _, · · · ,_<sup>_−→_</sup> _h T_ in _x_ )a. sequence of _backward hidden states_ (<sup>_←−_</sup> _h_ 1 _, · · · ,_<sup>_←−_</sup> _h Tx_ ). 

We obtain an annotation for each word _xj_ by concatenating the forward hidden state<sup>_−→_</sup> _h j_ and the _−→ ⊤_ backward one<sup>_←−_</sup> _h j_ , i.e., _hj_ = � _h ⊤j_<sup>;</sup><sup>_←−h⊤_</sup> _j_ � . In this way, the annotation _hj_ contains the summaries of both the preceding words and the following words. Due to the tendency of RNNs to better represent recent inputs, the annotation _hj_ will be focused on the words around _xj_ . This sequence of annotations is used by the decoder and the alignment model later to compute the context vector (Eqs. (5)–(6)). 

See Fig. 1 for the graphical illustration of the proposed model.