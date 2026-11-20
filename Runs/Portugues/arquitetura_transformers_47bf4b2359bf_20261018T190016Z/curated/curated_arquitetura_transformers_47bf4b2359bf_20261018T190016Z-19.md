[referencia=99bf4c74cf248c24 score=0.405]
**Convolutional Sequence to Sequence Learning** 

**Jonas Gehring Michael Auli David Grangier Denis Yarats Yann N. Dauphin** 

Facebook AI Research 

# **Abstract** 

The prevalent approach to sequence to sequence learning maps an input sequence to a variable length output sequence via recurrent neural networks. We introduce an architecture based entirely on convolutional neural networks.<sup>1</sup> Compared to recurrent models, computations over all elements can be fully parallelized during training to better exploit the GPU hardware and optimization is easier since the number of non-linearities is fixed and independent of the input length. Our use of gated linear units eases gradient propagation and we equip each decoder layer with a separate attention module. We outperform the accuracy of the deep LSTM setup of Wu et al. (2016) on both WMT’14 English-German and WMT’14 English-French translation at an order of magnitude faster speed, both on GPU and CPU.

---

[referencia=99bf4c74cf248c24 score=0.201]
### **Convolutional Sequence to Sequence Learning** 

|**WMT’14 English-German**|**BLEU**||**BLEU**|Time (s)|
|---|---|---|---|---|
|Wu et al.(2016) GNMT|26.20|GNMT GPU (K80)|31.20|3,028|
|Wu et al.(2016) GNMT + RL|26.30|GNMT CPU 88 cores|31.20|1,322|
|ConvS2S|26.43|GNMT TPU|31.21|384|
|||ConvS2S GPU (K40)_b_= 1|33.45|327|
|||ConvS2S GPU (M40)_b_= 1|33.45|221|
|**WMT’14 English-French**|**BLEU**|ConvS2S GPU (GTX-1080ti)_b_= 1|33.45|142|
|Zhou et al.(2016)|40.4|ConvS2S CPU 48 cores_b_= 1|33.45|142|
|Wu et al.(2016) GNMT|40.35|ConvS2S GPU (K40)_b_= 5|34.10|587|
|Wu et al.(2016) GNMT + RL|41.16|ConvS2S CPU 48 cores_b_= 5|34.10|482|
|ConvS2S|41.44|ConvS2S GPU (M40)_b_= 5|34.10|406|
|ConvS2S (10 models)|41.62|ConvS2S GPU (GTX-1080ti)_b_= 5|34.10|256|



_Table 2._ Accuracy of ensembles with eight models. We show both likelihood and Reinforce (RL) results for GNMT; Zhou et al. (2016) and ConvS2S use simple likelihood training. 

The translations produced by our models often match the length of the references, particularly for the large WMT’14 English-French task, or are very close for small to medium data sets such as WMT’14 English-German or WMT’16 English-Romanian.

---

[referencia=99bf4c74cf248c24 score=0.131]
The results (Table 1) show that our convolutional model outpeforms GNMT by 0.5 BLEU. Our encoder has 15 layers and the decoder has 15 layers, both with 512 hidden units in the first ten layers and 768 units in the subsequent three layers, all using kernel width 3. The final two layers have 2048 units which are just linear mappings with a single input. We trained this model on a single GPU over a period of 18.5 days with a batch size of 48. LSTM sparse mixtures have shown strong accuracy at 26.03 BLEU for a single run (Shazeer et al., 2016) which compares to 25.39 BLEU for our best run. This mixture sums the output of four experts, not unlike an ensemble which sums the output of multiple networks. ConvS2S also benefits from ensembling ( _§_ 5.2), therefore mixtures are a promising direction. 

Finally, we train on the much larger WMT’14 EnglishFrench task where we compare to the state of the art result of GNMT (Wu et al., 2016). Our model is trained with a simple token-level likelihood objective and we improve over GNMT in the same setting by 1.6 BLEU on average. We also outperform their reinforcement (RL) models by 0.5 

5We did not use the exact same vocabulary size because word pieces and BPE estimate the vocabulary differently.

---

[referencia=99bf4c74cf248c24 score=0.123]
## **5.6. Kernel size and Depth** 

Figure 2 shows accuracy when we change the number of layers in the encoder or decoder. The kernel width for layers in the encoder is 3 and for the decoder it is 5. Deeper architectures are particularly beneficial for the encoder but less so for the decoder. Decoder setups with two layers already perform well whereas for the encoder accuracy keeps increasing steadily with more layers until up to 9 layers when accuracy starts to plateau. 

The computational overhead for attention is very small compared to the rest of the network. Training with attention in all five decoder layers processes 3624 target words per second on average on a single GPU, compared to 3772 words per second for attention in a single layer. This is only 

**Convolutional Sequence to Sequence Learning** 

|||**DUC-2004**|||**Gigaword**||
|---|---|---|---|---|---|---|
||**RG-1 (R)**|**RG-2 (R)**|**RG-L (R)**|**RG-1 (F)**|**RG-2 (F)**|**RG-L (F)**|
|RNN MLE (Shen et al.,2016)|24.92|8.60|22.25|32.67|15.23|30.56|
|RNN MRT (Shen et al.,2016)|30.41|10.87|26.79|36.54|16.59|33.44|
|WFE (Suzuki & Nagata,2017)|32.28|10.54|27.80|36.30|17.31|33.88|
|ConvS2S|30.44|10.84|26.90|35.88|17.48|33.29|



_Table 6._ Accuracy on two summarization tasks in terms of Rouge-1 (RG-1), Rouge-2 (RG-2), and Rouge-L (RG-L). 

|**Kernel width**|**Enc**|**oder lay**|**ers**|
|---|---|---|---|
||5|9|13|
|3|20.61|21.17|21.63|
|5|20.80|21.02|21.42|
|7|20.81|21.30|21.09|

---

[referencia=99bf4c74cf248c24 score=0.112]
## **5.1. Recurrent vs. Convolutional Models** 

tion tasks. On WMT’16 English-Romanian translation we compare to Sennrich et al. (2016b) which is the winning entry on this language pair at WMT’16 (Bojar et al., 2016). Their model implements the attention-based sequence to sequence architecture of Bahdanau et al. (2014) and uses GRU cells both in the encoder and decoder. We test both word-based and BPE vocabularies ( _§_ 4). 

Table 1 shows that our fully convolutional sequence to sequence model (ConvS2S) outperforms the WMT’16 winning entry for English-Romanian by 1.9 BLEU with a BPE encoding and by 1.3 BLEU with a word factored vocabulary. This instance of our architecture has 20 layes in the encoder and 20 layers in the decoder, both using kernels of width 3 and hidden size 512 throughout. Training took between 6 and 7.5 days on a single GPU. 

On WMT’14 English to German translation we compare to the following prior work: Luong et al. (2015) is based on a four layer LSTM attention model, ByteNet (Kalchbrenner et al., 2016) propose a convolutional model based on characters without attention, with 30 layers in the encoder and 30 layers in the decoder, GNMT (Wu et al., 2016) represents the state of the art on this dataset and they use eight encoder LSTMs as well as eight decoder LSTMs, we quote their result for a word-based model, such as ours, as well as a word-piece model (Schuster & Nakajima, 2012).<sup>5</sup>

---

[referencia=99bf4c74cf248c24 score=0.067]
BLEU. Reinforcement learning is equally applicable to our architecture and we believe that it would further improve our results. 

The ConvS2S model for this experiment uses 15 layers in the encoder and 15 layers in the decoder, both with 512 hidden units in the first five layers, 768 units in the subsequent four layers, 1024 units in the next 3 layers, all using kernel width 3; the final two layers have 2048 units and 4096 units each but the they are linear mappings with kernel width 1. This model has an effective context size of only 25 words, beyond which it cannot access any information on the target size. Our results are based on training with 8 GPUs for about 37 days and batch size 32 on each worker.<sup>6</sup> The same configuration as for WMT’14 EnglishGerman achieves 39.41 BLEU in two weeks on this dataset in an eight GPU setup. 

Zhou et al. (2016) report a non-averaged result of 39.2 BLEU. More recently, Ha et al. (2016) showed that one can generate weights with one LSTM for another LSTM. This approach achieves 40.03 BLEU but the result is not averaged. Shazeer et al. (2016) compares at 40.56 BLEU to our best single run of 40.70 BLEU. 

6This is half of the GPU time consumed by a basic model of Wu et al. (2016) who use 96 GPUs for 6 days. We expect the time to train our model to decrease substantially in a multi-machine setup.

---

[referencia=99bf4c74cf248c24 score=0.041]
## **3.2. Convolutional Block Structure** 

Both encoder and decoder networks share a simple block structure that computes intermediate states based on a fixed number of input elements. We denote the output of the _l_ - th block as **h**<sup>_l_</sup> = ( _h_<sup>_l_</sup> 1<sup>_, . . . , hl_</sup> _n_<sup>)forthedecodernetwork,</sup> and **z**<sup>_l_</sup> = ( _z_ 1<sup>_l, . . . , z_</sup> _m_<sup>_l_)fortheencodernetwork;werefer</sup> to blocks and layers interchangeably. Each block contains a one dimensional convolution followed by a non-linearity. For a decoder network with a single block and kernel width _k_ , each resulting state _h_<sup>1</sup> _i_<sup>contains information over</sup><sup>_k_input</sup> elements. Stacking several blocks on top of each other increases the number of input elements represented in a state. For instance, stacking 6 blocks with _k_ = 5 results in an input field of 25 elements, i.e. each output depends on 25 

**Convolutional Sequence to Sequence Learning** 

inputs. Non-linearities allow the networks to exploit the full input field, or to focus on fewer elements if needed. 

Each convolution kernel is parameterized as _W ∈_ R<sup>2</sup><sup>_d×kd_</sup> , _bw ∈_ R<sup>2</sup><sup>_d_</sup> and takes as input _X ∈_ R<sup>_k×d_</sup> which is a concatenation of _k_ input elements embedded in _d_ dimensions and maps them to a single output element _Y ∈_ R<sup>2</sup><sup>_d_</sup> that has twice the dimensionality of the input elements; subsequent layers operate over the _k_ output elements of the previous layer. We choose gated linear units (GLU; Dauphin et al., 2016) as non-linearity which implement a simple gating mechanism over the output of the convolution _Y_ = [ _A B_ ] _∈_ R<sup>2</sup><sup>_d_</sup> :

---

[referencia=99bf4c74cf248c24 score=0.032]
# **1. Introduction** 

Sequence to sequence learning has been successful in many tasks such as machine translation, speech recognition (Sutskever et al., 2014; Chorowski et al., 2015) and text summarization (Rush et al., 2015; Nallapati et al., 2016; Shen et al., 2016) amongst others. The dominant approach to date encodes the input sequence with a series of bi-directional recurrent neural networks (RNN) and generates a variable length output with another set of decoder RNNs, both of which interface via a soft-attention mechanism (Bahdanau et al., 2014; Luong et al., 2015). In machine translation, this architecture has been demonstrated to outperform traditional phrase-based models by large margins (Sennrich et al., 2016b; Zhou et al., 2016; Wu et al., 2016; _§_ 2). 

> 1The source code and models are available at https:// github.com/facebookresearch/fairseq. 

Convolutional neural networks are less common for sequence modeling, despite several advantages (Waibel et al., 1989; LeCun & Bengio, 1995). Compared to recurrent layers, convolutions create representations for fixed size contexts, however, the effective context size of the network can easily be made larger by stacking several layers on top of each other. This allows to precisely control the maximum length of dependencies to be modeled. Convolutional networks do not depend on the computations of the previous time step and therefore allow parallelization over every element in a sequence. This contrasts with RNNs which maintain a hidden state of the entire past that prevents parallel computation within a sequence.

---

[referencia=99bf4c74cf248c24 score=0.027]
This can be seen as attention with multiple ’hops’ (Sukhbaatar et al., 2015) compared to single step attention (Bahdanau et al., 2014; Luong et al., 2015; Zhou et al., 2016; Wu et al., 2016). In particular, the attention of the first layer determines a useful source context which is then fed to the second layer that takes this information into account when computing attention etc. The decoder also has immediate access to the attention history of the _k −_ 1 previous time steps because the conditional inputs _c_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , c_</sup> _i_<sup>_l−_1</sup> are part of _h_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , hl_</sup> _i_<sup>_−_1</sup> which are input to _h_<sup>_l_</sup> _i_<sup>.Thismakesiteasierforthemodeltotakeintoac-</sup> count which previous inputs have been attended to already compared to recurrent nets where this information is in the recurrent state and needs to survive several non-linearities. Overall, our attention mechanism considers which words we previously attended to (Yang et al., 2016) _and_ performs multiple attention ’hops’ per time step. In Appendix _§_ C, we plot attention scores for a deep decoder and show that at different layers, different portions of the source are attended to. 

Our convolutional architecture also allows to batch the attention computation across all elements of a sequence compared to RNNs (Figure 1, middle). We batch the computations of each decoder layer individually.

---

[referencia=99bf4c74cf248c24 score=0.026]
## **5.4. Position Embeddings** 

In the following sections, we analyze the design choices in our architecture. The remaining results in this paper are based on the WMT’14 English-German task with 13 encoder layers at kernel size 3 and 5 decoder layers at kernel size 5. We use a target vocabulary of 160K words as well as vocabulary selection (Mi et al., 2016; L’Hostis et al., 2016) to decrease the size of the output layer which speeds up training and testing. The average vocabulary size for each training batch is about 20K target words. All figures are averaged over three runs ( _§_ 4) and BLEU is reported on newstest2014 before unknown word replacement. 

We start with an experiment that removes the position em- 

**Convolutional Sequence to Sequence Learning** 

|**PPL**|**BLEU**|**Attn Layers**|**PPL**|**BLEU**|
|---|---|---|---|---|
|ConvS2S<br>6.64|21.7|1,2,3,4,5|6.65|21.63|
|-source position<br>6.69|21.3|1,2,3,4|6.70|21.54|
|-target position<br>6.63|21.5|1,2,3|6.95|21.36|
|-source & target position<br>6.68|21.2|1,2|6.92|21.47|
|||1,3,5|6.97|21.10|
|Effect of removing position embeddin<br>of validation erlexit (valid PPL) an|gs from our model<br>d BLEU|1|7.15|21.26|
|ppy|.|2|7.09|21.30|
|||3|7.11|21.19|
|||4|7.19|21.31|
|s from the encoder and decoder (_§_|3.1). These em-|5|7.66|20.24|



_Table 4._ Effect of removing position embeddings from our model in terms of validation perplexity (valid PPL) and BLEU.

---

[referencia=99bf4c74cf248c24 score=0.020]
Bradbury, James, Merity, Stephen, Xiong, Caiming, and Socher, Richard. Quasi-Recurrent Neural Networks. 

- _arXiv preprint arXiv:1611.01576_ , 2016. 

- Cho, Kyunghyun, Van Merri¨enboer, Bart, Gulcehre, Caglar, Bahdanau, Dzmitry, Bougares, Fethi, Schwenk, Holger, and Bengio, Yoshua. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation. In _Proc. of EMNLP_ , 2014. 

- Chorowski, Jan K, Bahdanau, Dzmitry, Serdyuk, Dmitriy, Cho, Kyunghyun, and Bengio, Yoshua. Attention-based models for speech recognition. In _Advances in Neural_ 

- _Information Processing Systems_ , pp. 577–585, 2015. 

- Collobert, Ronan, Kavukcuoglu, Koray, and Farabet, Clement. Torch7: A Matlab-like Environment for Machine Learning. In _BigLearn, NIPS Workshop_ , 2011. URL http://torch.ch. 

- Dauphin, Yann N., Fan, Angela, Auli, Michael, and Grangier, David. Language modeling with gated linear units. 

- _arXiv preprint arXiv:1612.08083_ , 2016. 

- Dyer, Chris, Chahuneau, Victor, and Smith, Noah A. A Simple, Fast, and Effective Reparameterization of IBM Model 2. In _Proc. of ACL_ , 2013. 

## Elman, Jeffrey L. Finding Structure in Time. _Cognitive Science_ , 14:179–211, 1990. 

Gehring, Jonas, Auli, Michael, Grangier, David, and Dauphin, Yann N. A Convolutional Encoder Model for Neural Machine Translation. _arXiv preprint_

---

[referencia=99bf4c74cf248c24 score=0.020]
## **4.1. Datasets** 

We consider three major WMT translation tasks as well as a text summarization task. 

**WMT’16 English-Romanian.** We use the same data and pre-processing as Sennrich et al. (2016b) but remove sentences with more than 175 words. This results in 2.8M sentence pairs for training and we evaluate on newstest2016.<sup>2</sup> 

> 2We followed the pre-processing of https://github. com/rsennrich/wmt16-scripts/blob/80e21e5/ sample/preprocess.sh and added the back-translated data from http://data.statmt.org/rsennrich/wmt16_ 

**Convolutional Sequence to Sequence Learning** 

We experiment with word-based models using a source vocabulary of 200K types and a target vocabulary of 80K types. We also consider a joint source and target byte-pair encoding (BPE) with 40K types (Sennrich et al., 2016a;b). **WMT’14 English-German.** We use the same setup as Luong et al. (2015) which comprises 4.5M sentence pairs for training and we test on newstest2014.<sup>3</sup> As vocabulary we use 40K sub-word types based on BPE. **WMT’14 English-French.** We use the full training set of 

still in GPU memory. If the threshold is exceeded, we simply split the batch until the threshold is met and process the parts separatedly. Gradients are normalized by the number of non-padding tokens per mini-batch. We also use weight normalization for all layers except for lookup tables (Salimans & Kingma, 2016). 

Besides dropout on the embeddings and the decoder output, we also apply dropout to the input of the convolutional blocks (Srivastava et al., 2014). All models are im- 

plemented in Torch (Collobert et al., 2011) and trained on a single Nvidia M40 GPU except for WMT’14 EnglishFrench for which we use a multi-GPU setup on a single 

36M sentence pairs, and remove sentences longer than 175 words as well as pairs with a source/target length ratio exceeding 1.5. This results in 35.5M sentence-pairs for train-

---

[referencia=99bf4c74cf248c24 score=0.019]
5We did not use the exact same vocabulary size because word pieces and BPE estimate the vocabulary differently. 

|**WMT’16 English-Romanian**|**BLEU**|
|---|---|
|Sennrich et al.(2016b) GRU (BPE 90K)|28.1|
|ConvS2S (Word 80K)|29.45|
|ConvS2S (BPE 40K)|30.02|
|**WMT’14 English-German**|**BLEU**|
|Luong et al.(2015) LSTM (Word 50K)|20.9|
|Kalchbrenner et al.(2016) ByteNet (Char)|23.75|
|Wu et al.(2016) GNMT (Word 80K)|23.12|
|Wu et al.(2016) GNMT (Word pieces)|24.61|
|ConvS2S (BPE 40K)|25.16|
|**WMT’14 English-French**|**BLEU**|
|Wu et al.(2016) GNMT (Word 80K)|37.90|
|Wu et al.(2016) GNMT (Word pieces)|38.95|
|Wu et al.(2016) GNMT (Word pieces) + RL|39.92|
|ConvS2S (BPE 40K)|40.51|



_Table 1._ Accuracy on WMT tasks comapred to previous work. ConvS2S and GNMT results are averaged over several runs. 

BLEU. Reinforcement learning is equally applicable to our architecture and we believe that it would further improve our results.

---

[referencia=99bf4c74cf248c24 score=0.015]
## **5.3. Generation Speed** 

Next, we evaluate the inference speed of our architecture on the development set of the WMT’14 English-French task which is the concatenation of newstest2012 and newstest2013; it comprises 6003 sentences. We measure generation speed both on GPU and CPU hardware. Specifically, we measure GPU speed on three generations of Nvidia cards: a GTX-1080ti, an M40 as well as an older K40 card. CPU timings are measured on one host with 48 hyperthreaded cores (Intel Xeon E5-2680 @ 2.50GHz) with 40 workers. In all settings, we batch up to 128 sentences, composing batches with sentences of equal length. Note that the majority of batches is smaller because of the small size of the development set. We experiment with beams of size 5 as well as greedy search, i.e beam of size 1. To make generation fast, we do not recompute convolution states that have not changed compared to the previous time step but rather copy (shift) these activations. 

We compare to results reported in Wu et al. (2016) who 

_Table 3._ CPU and GPU generation speed in seconds on the development set of WMT’14 English-French. We show results for different beam sizes _b_ . GNMT figures are taken from Wu et al. (2016). CPU speeds are not directly comparable because Wu et al. (2016) use a 88 core machine versus our 48 core setup. 

use Nvidia K80 GPUs which are essentially two K40s. We did not have such a GPU available and therefore run experiments on an older K40 card which is inferior to a K80, in addition to the newer M40 and GTX-1080ti cards. The results (Table 3) show that our model can generate translations on a K40 GPU at 9.3 times the speed and 2.25 higher BLEU; on an M40 the speed-up is up to 13.7 times and on a GTX-1080ti card the speed is 21.3 times faster. A larger beam of size 5 decreases speed but gives better BLEU.

---

[referencia=99bf4c74cf248c24 score=0.014]
_Table 4._ Effect of removing position embeddings from our model in terms of validation perplexity (valid PPL) and BLEU. 

beddings from the encoder and decoder ( _§_ 3.1). These embeddings allow our model to identify which portion of the source and target sequence it is dealing with but also impose a restriction on the maximum sentence length. Table 4 shows that position embeddings are helpful but that our model still performs well without them. Removing the source position embeddings results in a larger accuracy decrease than target position embeddings. However, removing both source and target positions decreases accuracy only by 0 _._ 5 BLEU. We had assumed that the model would not be able to calibrate the length of the output sequences very well without explicit position information, however, the output lengths of models without position embeddings closely matches models with position information. This indicates that the models can learn relative position information within the contexts visible to the encoder and decoder networks which can observe up to 27 and 25 words respectively. 

_Table 5._ Multi-step attention in all five decoder layers or fewer layers in terms of validation perplexity (PPL) and test BLEU. 



<!-- Start of picture text -->
 22<br> 21.5<br> 21<br> 20.5<br> 20<br> 19.5<br>Encoder<br>Decoder<br> 19<br> 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25<br>Layers<br>BLEU<br><!-- End of picture text -->

Recurrent models typically do not use explicit position embeddings since they can learn where they are in the sequence through the recurrent hidden state computation. In our setting, the use of position embeddings requires only a simple addition to the input word embeddings which is a negligible overhead. 

_Figure 2._ Encoder and decoder with different number of layers.

---

[referencia=99bf4c74cf248c24 score=0.013]
# **6. Conclusion and Future Work** 

We introduce the first fully convolutional model for sequence to sequence learning that outperforms strong recurrent models on very large benchmark datasets at an order of magnitude faster speed. Compared to recurrent networks, our convolutional approach allows to discover compositional structure in the sequences more easily since representations are built hierarchically. Our model relies on gating and performs multiple attention steps. 

We achieve a new state of the art on several public translation benchmark data sets. On the WMT’16 EnglishRomanian task we outperform the previous best result by 1.9 BLEU, on WMT’14 English-French translation we improve over the LSTM model of Wu et al. (2016) by 1.6 BLEU in a comparable setting, and on WMT’14 EnglishGerman translation we ouperform the same model by 0.5 BLEU. In future work, we would like to apply convolutional architectures to other sequence to sequence learning problems which may benefit from learning hierarchical representations as well. 

# **Acknowledgements** 

We thank Benjamin Graham for providing a fast 1-D convolution, and Ronan Collobert as well as Yann LeCun for helpful discussions related to this work.

---

[referencia=99bf4c74cf248c24 score=0.013]
# **B. Upper Bound on Squared Sigmoid** 



and a similar condition, i.e. (1 _/_ 4)ˆ _nlV ar_ [ _wl_<sup>_a_]=1.Inthe</sup> networks we consider, successions of convolutional layers usually operate on the same number of inputs so that most ˆ cases _nl_ = _nl_ . Note that _Wl_<sup>_b_isdiscardedintheapprox-</sup> imation; however, for the sake of consistency we use the same initialization for _Wl_<sup>_a_and</sup><sup>_W b_</sup> _l_<sup>.</sup> 

For arbitrarily large variances of network inputs and activations, our approximations are invalid; in that case, the initial values for _Wl_<sup>_a_and</sup><sup>_W b_</sup> _l_<sup>would have to be balanced for</sup> the input distribution to be retained. Alternatively, methods that explicitly control the variance in the network, e.g. batch normalization (Ioffe & Szegedy, 2015) or layer normalization (Ba et al., 2016) could be employed.

---

[referencia=99bf4c74cf248c24 score=0.013]
## **A.2. Backward Pass** 

The gradient of a convolutional layer is computed via backpropagation as ∆ **x** _l_ = _W_<sup>ˆ</sup> _l_ **y** _l_ . Considering separate gradients ∆ **y** _l_<sup>_a_and ∆</sup><sup>**y**</sup> _l_<sup>_b_for GLU, the gradient of</sup><sup>**x**is given by</sup> 



ˆ _W_ corresponds to _W_ with re-arranged weights to enable back-propagation. Analogously to the forward pass, ∆ _xl_ , _w_ ˆ _l_ and ∆ _yl_ represent the random variables for the values in ∆ **xl** , _W_<sup>ˆ</sup> _l_ and ∆ **yl** , respectively. Note that _W_ and _W_<sup>ˆ</sup> ˆ contain the same values, i.e. _w_ = _w_ . Similar to (3), the variance of ∆ _xl_ is 





**Convolutional Sequence to Sequence Learning** 

The approximation for the forward pass can be used for _V ar_ [∆ _yl_<sup>_a_], and for estimating</sup><sup>_V ar_[∆</sup><sup>_y_</sup> _l_<sup>_b_] we assume an up-</sup> per bound on _E_ [ _σ_<sup>_′_</sup> ( _yl_<sup>_b_)2]of1</sup><sup>_/_16since</sup><sup>_σ′_(</sup><sup>_y_</sup> _l_<sup>_b_)</sup><sup>_∈_[0</sup><sup>_,_</sup> 4<sup><u>1</u>].</sup> Hence, 





We observe relatively small gradients in our network, typically around 0.001 at the start of training. Therefore, we approximate by discarding the quadratic terms above, i.e. 







As for the forward pass, the above result can be generalized to backpropagation through many successive layers, resulting in 

of _r_ and _E_ [ _x_ ] = 0, the variance after dropout is

---

[referencia=99bf4c74cf248c24 score=0.011]
# **References** 

- Ba, Jimmy Lei, Kiros, Jamie Ryan, and Hinton, Geoffrey E. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. 

- Bahdanau, Dzmitry, Cho, Kyunghyun, and Bengio, Yoshua. Neural machine translation by jointly learning to align and translate. _arXiv preprint arXiv:1409.0473_ , 2014. 

- Bojar, Ondej, Chatterjee, Rajen, Federmann, Christian, Graham, Yvette, Haddow, Barry, Huck, Matthias, 

**Convolutional Sequence to Sequence Learning** 

Jimeno-Yepes, Antonio, Koehn, Philipp, Logacheva, Varvara, Monz, Christof, Negri, Matteo, N´ev´eol, Aur´elie, Neves, Mariana L., Popel, Martin, Post, Matt, Rubino, Rapha¨el, Scarton, Carolina, Specia, Lucia, Turchi, Marco, Verspoor, Karin M., and Zampieri, Marcos. Findings of the 2016 conference on machine translation. In _Proc. of WMT_ , 2016. 

Bradbury, James, Merity, Stephen, Xiong, Caiming, and Socher, Richard. Quasi-Recurrent Neural Networks.

---

[referencia=99bf4c74cf248c24 score=0.009]
# **3. A Convolutional Architecture** 

Next we introduce a fully convolutional architecture for sequence to sequence modeling. Instead of relying on RNNs to compute intermediate encoder states **z** and decoder states **h** we use convolutional neural networks (CNN). 

## **3.1. Position Embeddings** 

First, we embed input elements **x** = ( _x_ 1 _, . . . , xm_ ) in distributional space as **w** = ( _w_ 1 _, . . . , wm_ ), where _wj ∈_ R<sup>_f_</sup> is a column in an embedding matrix _D ∈_ R<sup>_V ×f_</sup> . We also equip our model with a sense of order by embedding the absolute position of input elements **p** = ( _p_ 1 _, . . . , pm_ ) where _pj ∈_ R<sup>_f_</sup> . Both are combined to obtain input element representations **e** = ( _w_ 1 + _p_ 1 _, . . . , wm_ + _pm_ ). We proceed similarly for output elements that were already generated by the decoder network to yield output element representations that are being fed back into the decoder network **g** = ( _g_ 1 _, . . . , gn_ ). Position embeddings are useful in our architecture since they give our model a sense of which portion of the sequence in the input or output it is currently dealing with ( _§_ 5.4).