[referencia=a7468c6851652691 score=0.719]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=99bf4c74cf248c24 score=0.603]
# **1. Introduction** 

Sequence to sequence learning has been successful in many tasks such as machine translation, speech recognition (Sutskever et al., 2014; Chorowski et al., 2015) and text summarization (Rush et al., 2015; Nallapati et al., 2016; Shen et al., 2016) amongst others. The dominant approach to date encodes the input sequence with a series of bi-directional recurrent neural networks (RNN) and generates a variable length output with another set of decoder RNNs, both of which interface via a soft-attention mechanism (Bahdanau et al., 2014; Luong et al., 2015). In machine translation, this architecture has been demonstrated to outperform traditional phrase-based models by large margins (Sennrich et al., 2016b; Zhou et al., 2016; Wu et al., 2016; _§_ 2). 

> 1The source code and models are available at https:// github.com/facebookresearch/fairseq. 

Convolutional neural networks are less common for sequence modeling, despite several advantages (Waibel et al., 1989; LeCun & Bengio, 1995). Compared to recurrent layers, convolutions create representations for fixed size contexts, however, the effective context size of the network can easily be made larger by stacking several layers on top of each other. This allows to precisely control the maximum length of dependencies to be modeled. Convolutional networks do not depend on the computations of the previous time step and therefore allow parallelization over every element in a sequence. This contrasts with RNNs which maintain a hidden state of the entire past that prevents parallel computation within a sequence.

---

[referencia=9cee40b637f69874 score=0.460]
al. [5] by translating pieces of the source sentence in way that produces smooth translations, which 

is similar to a phrase-based approach. We suspect that they could achieve similar improvements by simply training their networks on reversed source sentences. 

End-to-end training is also the focus of Hermann et al. [12], whose model represents the inputs and outputs by feedforward networks, and map them to similar points in space. However, their approach cannot generate translations directly: to get a translation, they need to do a look up for closest vector in the pre-computed database of sentences, or to rescore a sentence. 

**5 Conclusion** 

In this work, we showed that a large deep LSTM, that has a limited vocabulary and that makes almost no assumption about problem structure can outperform a standard SMT-based system whose vocabulary is unlimited on a large-scale MT task. The success of our simple LSTM-based approach on MT suggests that it should do well on many other sequence learning problems, provided they have enough training data. 

We were surprised by the extent of the improvement obtained by reversing the words in the source sentences. We conclude that it is important to find a problem encoding that has the greatest number of short term dependencies, as they make the learning problem much simpler. In particular, while we were unable to train a standard RNN on the non-reversed translation problem (shown in fig. 1), we believe that a standard RNN should be easily trainable when the source sentences are reversed (although we did not verify it experimentally). 

We were also surprised by the ability of the LSTM to correctly translate very long sentences. We were initially convinced that the LSTM would fail on long sentences due to its limited memory, and other researchers reported poor performance on long sentences with a model similar to ours [5, 2, 26]. And yet, LSTMs trained on the reversed dataset had little difficulty translating long sentences. 

Most importantly, we demonstrated that a simple, straightforward and a relatively unoptimized approach can outperform an SMT system, so further work will likely lead to even greater translation accuracies. These results suggest that our approach will likely do well on other challenging sequence to sequence problems. **6 Acknowledgments**

---

[referencia=a7468c6851652691 score=0.296]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=a7468c6851652691 score=0.293]
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

[referencia=9cee40b637f69874 score=0.262]
## **1 Introduction** 

Deep Neural Networks (DNNs) are extremely powerful machine learning models that achieve excellent performance on difficult problems such as speech recognition [13, 7] and visual object recognition [19, 6, 21, 20]. DNNs are powerful because they can perform arbitrary parallel computation for a modest number of steps. A surprising example of the power of DNNs is their ability to sort N N -bit numbers using only 2 hidden layers of quadratic size [27]. So, while neural networks are related to conventional statistical models, they learn an intricate computation. Furthermore, large DNNs can be trained with supervised backpropagation whenever the labeled training set has enough information to specify the network’s parameters. Thus, if there exists a parameter setting of a large DNN that achieves good results (for example, because humans can solve the task very rapidly), supervised backpropagation will find these parameters and solve the problem. 

can be sensibly encoded with vectors of fixed dimensionality. It is a significant limitation, since many important problems are best expressed with sequences whose lengths are not known a-priori. For example, speech recognition and machine translation are sequential problems. Likewise, question answering can also be seen as mapping a sequence of words representing the question to a 

1 

sequence of words representing the answer. It is therefore clear that a domain-independent method that learns to map sequences to sequences would be useful. 

Sequences pose a challenge for DNNs because they require that the dimensionality of the inputs and outputs is known and fixed. In this paper, we show that a straightforward application of the Long Short-Term Memory (LSTM) architecture [16] can solve general sequence to sequence problems. The idea is to use one LSTM to read the input sequence, one timestep at a time, to obtain large fixeddimensional vector representation, and then to use another LSTM to extract the output sequence from that vector (fig. 1). The second LSTM is essentially a recurrent neural network language model [28, 23, 30] except that it is conditioned on the input sequence. The LSTM’s ability to successfully learn on data with long range temporal dependencies makes it a natural choice for this application due to the considerable time lag between the inputs and their corresponding outputs (fig. 1).

---

[referencia=99bf4c74cf248c24 score=0.230]
This can be seen as attention with multiple ’hops’ (Sukhbaatar et al., 2015) compared to single step attention (Bahdanau et al., 2014; Luong et al., 2015; Zhou et al., 2016; Wu et al., 2016). In particular, the attention of the first layer determines a useful source context which is then fed to the second layer that takes this information into account when computing attention etc. The decoder also has immediate access to the attention history of the _k −_ 1 previous time steps because the conditional inputs _c_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , c_</sup> _i_<sup>_l−_1</sup> are part of _h_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , hl_</sup> _i_<sup>_−_1</sup> which are input to _h_<sup>_l_</sup> _i_<sup>.Thismakesiteasierforthemodeltotakeintoac-</sup> count which previous inputs have been attended to already compared to recurrent nets where this information is in the recurrent state and needs to survive several non-linearities. Overall, our attention mechanism considers which words we previously attended to (Yang et al., 2016) _and_ performs multiple attention ’hops’ per time step. In Appendix _§_ C, we plot attention scores for a deep decoder and show that at different layers, different portions of the source are attended to. 

Our convolutional architecture also allows to batch the attention computation across all elements of a sequence compared to RNNs (Figure 1, middle). We batch the computations of each decoder layer individually.

---

[referencia=a7468c6851652691 score=0.189]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=99bf4c74cf248c24 score=0.187]
**Convolutional Sequence to Sequence Learning** 

**Jonas Gehring Michael Auli David Grangier Denis Yarats Yann N. Dauphin** 

Facebook AI Research 

# **Abstract** 

The prevalent approach to sequence to sequence learning maps an input sequence to a variable length output sequence via recurrent neural networks. We introduce an architecture based entirely on convolutional neural networks.<sup>1</sup> Compared to recurrent models, computations over all elements can be fully parallelized during training to better exploit the GPU hardware and optimization is easier since the number of non-linearities is fixed and independent of the input length. Our use of gated linear units eases gradient propagation and we equip each decoder layer with a separate attention module. We outperform the accuracy of the deep LSTM setup of Wu et al. (2016) on both WMT’14 English-German and WMT’14 English-French translation at an order of magnitude faster speed, both on GPU and CPU.

---

[referencia=a7468c6851652691 score=0.140]
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

[referencia=99bf4c74cf248c24 score=0.135]
# **6. Conclusion and Future Work** 

We introduce the first fully convolutional model for sequence to sequence learning that outperforms strong recurrent models on very large benchmark datasets at an order of magnitude faster speed. Compared to recurrent networks, our convolutional approach allows to discover compositional structure in the sequences more easily since representations are built hierarchically. Our model relies on gating and performs multiple attention steps. 

We achieve a new state of the art on several public translation benchmark data sets. On the WMT’16 EnglishRomanian task we outperform the previous best result by 1.9 BLEU, on WMT’14 English-French translation we improve over the LSTM model of Wu et al. (2016) by 1.6 BLEU in a comparable setting, and on WMT’14 EnglishGerman translation we ouperform the same model by 0.5 BLEU. In future work, we would like to apply convolutional architectures to other sequence to sequence learning problems which may benefit from learning hierarchical representations as well. 

# **Acknowledgements** 

We thank Benjamin Graham for providing a fast 1-D convolution, and Ronan Collobert as well as Yann LeCun for helpful discussions related to this work.

---

[referencia=9cee40b637f69874 score=0.104]
## **2 The model** 

The Recurrent Neural Network (RNN) [31, 28] is a natural generalization of feedforward neural networks to sequences. Given a sequence of inputs (x1, . . . , xT ), a standard RNN computes a sequence of outputs (y1, . . . , yT ) by iterating the following equation: 



The RNN can easily map sequences to sequences whenever the alignment between the inputs the outputs is known ahead of time. However, it is not clear how to apply an RNN to problems whose input and the output sequences have different lengths with complicated and non-monotonic relationships. 

The simplest strategy for general sequence learning is to map the input sequence to a vector using one RNN, and then to map the vector to the target sequence with another RNN (this approach has also been taken by Cho et al. [5]). While it could work in principle since the RNN is provided with all the relevant information, it would be difficult to train the RNNs due to the resulting long term dependencies (figure 1) [14, 4, 16, 15]. However, the Long Short-Term Memory (LSTM) [16] is known to learn problems with long range temporal dependencies, so an LSTM may succeed in this setting. 

The goal of the LSTM is to estimate the conditional probability p(y1, . . . , yT ′|x1, . . . , xT ) where (x1, . . . , xT ) is an input sequence and y1, . . . , yT ′ is its corresponding output sequence whose length T<sup>′</sup> may differ from T . The LSTM computes this conditional probability by first obtaining the fixeddimensional representation v of the input sequence (x1, . . . , xT ) given by the last hidden state of the LSTM, and then computing the probability of y1, . . . , yT ′ with a standard LSTM-LM formulation whose initial hidden state is set to the representation v of x1, . . . , xT :

---

[referencia=99bf4c74cf248c24 score=0.100]
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

[referencia=99bf4c74cf248c24 score=0.097]
# **3. A Convolutional Architecture** 

Next we introduce a fully convolutional architecture for sequence to sequence modeling. Instead of relying on RNNs to compute intermediate encoder states **z** and decoder states **h** we use convolutional neural networks (CNN). 

## **3.1. Position Embeddings** 

First, we embed input elements **x** = ( _x_ 1 _, . . . , xm_ ) in distributional space as **w** = ( _w_ 1 _, . . . , wm_ ), where _wj ∈_ R<sup>_f_</sup> is a column in an embedding matrix _D ∈_ R<sup>_V ×f_</sup> . We also equip our model with a sense of order by embedding the absolute position of input elements **p** = ( _p_ 1 _, . . . , pm_ ) where _pj ∈_ R<sup>_f_</sup> . Both are combined to obtain input element representations **e** = ( _w_ 1 + _p_ 1 _, . . . , wm_ + _pm_ ). We proceed similarly for output elements that were already generated by the decoder network to yield output element representations that are being fed back into the decoder network **g** = ( _g_ 1 _, . . . , gn_ ). Position embeddings are useful in our architecture since they give our model a sense of which portion of the sequence in the input or output it is currently dealing with ( _§_ 5.4).

---

[referencia=99bf4c74cf248c24 score=0.089]
# **2. Recurrent Sequence to Sequence Learning** 

Sequence to sequence modeling has been synonymous with recurrent neural network based encoder-decoder architectures (Sutskever et al., 2014; Bahdanau et al., 2014). The encoder RNN processes an input sequence **x** = ( _x_ 1 _, . . . , xm_ ) of _m_ elements and returns state representations **z** = ( _z_ 1 _. . . . , zm_ ). The decoder RNN takes **z** and generates the output sequence **y** = ( _y_ 1 _, . . . , yn_ ) left to right, one element at a time. To generate output _yi_ +1, the decoder computes a new hidden state _hi_ +1 based on the previous state _hi_ , an embedding _gi_ of the previous target language word _yi_ , as well as a conditional input _ci_ derived from the encoder output **z** . Based on this generic formulation, various encoder-decoder architectures have been proposed, which differ mainly in the conditional input and the type of RNN. 

Models without attention consider only the encoder state _zm_ by setting _ci_ = _zm_ for all _i_ (Cho et al., 2014), or simply initialize the first decoder state with _zm_ (Sutskever et al., 2014), in which case _ci_ is not used. Architectures with attention (Bahdanau et al., 2014; Luong et al., 2015) compute _ci_ as a weighted sum of ( _z_ 1 _. . . . , zm_ ) at each time step. The weights of the sum are referred to as attention scores and allow the network to focus on different parts of the input sequence as it generates the output sequences. Attention scores are computed by essentially comparing each encoder state _zj_ to a combination of the previous decoder 

state _hi_ and the last prediction _yi_ ; the result is normalized to be a distribution over input elements.

---

[referencia=99bf4c74cf248c24 score=0.085]
state _hi_ and the last prediction _yi_ ; the result is normalized to be a distribution over input elements. 

Popular choices for recurrent networks in encoder-decoder models are long short term memory networks (LSTM; Hochreiter & Schmidhuber, 1997) and gated recurrent units (GRU; Cho et al., 2014). Both extend Elman RNNs (Elman, 1990) with a gating mechanism that allows the memorization of information from previous time steps in order to model long-term dependencies. Most recent approaches also rely on bi-directional encoders to build representations of both past and future contexts (Bahdanau et al., 2014; Zhou et al., 2016; Wu et al., 2016). Models with many layers often rely on shortcut or residual connections (He et al., 2015a; Zhou et al., 2016; Wu et al., 2016).

---

[referencia=99bf4c74cf248c24 score=0.068]
## **5.1. Recurrent vs. Convolutional Models** 

tion tasks. On WMT’16 English-Romanian translation we compare to Sennrich et al. (2016b) which is the winning entry on this language pair at WMT’16 (Bojar et al., 2016). Their model implements the attention-based sequence to sequence architecture of Bahdanau et al. (2014) and uses GRU cells both in the encoder and decoder. We test both word-based and BPE vocabularies ( _§_ 4). 

Table 1 shows that our fully convolutional sequence to sequence model (ConvS2S) outperforms the WMT’16 winning entry for English-Romanian by 1.9 BLEU with a BPE encoding and by 1.3 BLEU with a word factored vocabulary. This instance of our architecture has 20 layes in the encoder and 20 layers in the decoder, both using kernels of width 3 and hidden size 512 throughout. Training took between 6 and 7.5 days on a single GPU. 

On WMT’14 English to German translation we compare to the following prior work: Luong et al. (2015) is based on a four layer LSTM attention model, ByteNet (Kalchbrenner et al., 2016) propose a convolutional model based on characters without attention, with 30 layers in the encoder and 30 layers in the decoder, GNMT (Wu et al., 2016) represents the state of the art on this dataset and they use eight encoder LSTMs as well as eight decoder LSTMs, we quote their result for a word-based model, such as ours, as well as a word-piece model (Schuster & Nakajima, 2012).<sup>5</sup>

---

[referencia=9cee40b637f69874 score=0.067]
- [1] M. Auli, M. Galley, C. Quirk, and G. Zweig. Joint language and translation modeling with recurrent neural networks. In _EMNLP_ , 2013. 

- [2] D. Bahdanau, K. Cho, and Y. Bengio. Neural machine translation by jointly learning to align and translate. _arXiv preprint arXiv:1409.0473_ , 2014. 

- [3] Y. Bengio, R. Ducharme, P. Vincent, and C. Jauvin. A neural probabilistic language model. In _Journal of Machine Learning Research_ , pages 1137–1155, 2003. 

- [4] Y. Bengio, P. Simard, and P. Frasconi. _IEEE Transactions on Neural Networks_ , 5(2):157–166, 1994. 

- [5] K. Cho, B. Merrienboer, C. Gulcehre, F. Bougares, H. Schwenk, and Y. Bengio. Learning phrase representations using RNN encoder-decoder for statistical machine translation. In _Arxiv preprint arXiv:1406.1078_ , 2014. 

- [6] D. Ciresan, U. Meier, and J. Schmidhuber. In _CVPR_ , 2012. 

- [7] G. E. Dahl, D. Yu, L. Deng, and A. Acero. Context-dependent pre-trained deep neural networks for large vocabulary speech recognition. _IEEE Transactions on Audio, Speech, and Language Processing - Special Issue on Deep Learning for Speech and Language Processing_ , 2012. 

- [8] J. Devlin, R. Zbib, Z. Huang, T. Lamar, R. Schwartz, and J. Makhoul. Fast and robust neural network joint models for statistical machine translation. In _ACL_ , 2014. 

- [9] Edinburgh’s phrase-based machine translation systems for wmt-14. In _WMT_ , 2014. 

- [10] A. Graves. Generating sequences with recurrent neural networks. In _Arxiv preprint arXiv:1308.0850_ , 2013.

---

[referencia=a7468c6851652691 score=0.056]
- [33] Nitish Srivastava, Geoffrey E Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov. Dropout: a simple way to prevent neural networks from overfitting. _Journal of Machine Learning Research_ , 15(1):1929–1958, 2014. 

- [34] Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, and Rob Fergus. End-to-end memory networks. In C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama, and R. Garnett, editors, _Advances in Neural Information Processing Systems 28_ , pages 2440–2448. Curran Associates, Inc., 2015. 

- [35] Ilya Sutskever, Oriol Vinyals, and Quoc VV Le. Sequence to sequence learning with neural networks. In _Advances in Neural Information Processing Systems_ , pages 3104–3112, 2014. 

- [36] Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna. Rethinking the inception architecture for computer vision. _CoRR_ , abs/1512.00567, 2015. 

- [37] Vinyals & Kaiser, Koo, Petrov, Sutskever, and Hinton. Grammar as a foreign language. In _Advances in Neural Information Processing Systems_ , 2015. 

- [38] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google’s neural machine translation system: Bridging the gap between human and machine translation. _arXiv preprint arXiv:1609.08144_ , 2016. 

- [39] Jie Zhou, Ying Cao, Xuguang Wang, Peng Li, and Wei Xu. Deep recurrent models with fast-forward connections for neural machine translation. _CoRR_ , abs/1606.04199, 2016.

---

[referencia=99bf4c74cf248c24 score=0.055]
## machine translation. In _Proc. of EMNLP_ , 2015. 

Meng, Fandong, Lu, Zhengdong, Wang, Mingxuan, Li, Hang, Jiang, Wenbin, and Liu, Qun. Encoding Source Language with Convolutional Neural Network for Machine Translation. In _Proc. of ACL_ , 2015. 

Mi, Haitao, Wang, Zhiguo, and Ittycheriah, Abe. Vocabulary Manipulation for Neural Machine Translation. In _Proc. of ACL_ , 2016. 

Miller, Alexander H., Fisch, Adam, Dodge, Jesse, Karimi, Amir-Hossein, Bordes, Antoine, and Weston, Jason. Key-value memory networks for directly reading documents. In _Proc. of EMNLP_ , 2016. 

Nallapati, Ramesh, Zhou, Bowen, Gulcehre, Caglar, Xiang, Bing, et al. Abstractive text summarization using sequence-to-sequence rnns and beyond. In _Proc. of EMNLP_ , 2016. 

**Convolutional Sequence to Sequence Learning** 

Oord, Aaron van den, Kalchbrenner, Nal, and Kavukcuoglu, Koray. Pixel recurrent neural networks. _arXiv preprint arXiv:1601.06759_ , 2016a.