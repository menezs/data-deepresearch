[referencia=99bf4c74cf248c24 score=0.019]
This can be seen as attention with multiple ’hops’ (Sukhbaatar et al., 2015) compared to single step attention (Bahdanau et al., 2014; Luong et al., 2015; Zhou et al., 2016; Wu et al., 2016). In particular, the attention of the first layer determines a useful source context which is then fed to the second layer that takes this information into account when computing attention etc. The decoder also has immediate access to the attention history of the _k −_ 1 previous time steps because the conditional inputs _c_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , c_</sup> _i_<sup>_l−_1</sup> are part of _h_<sup>_l_</sup> _i_<sup>_−_</sup> _−_<sup>1</sup> _k_<sup>_, . . . , hl_</sup> _i_<sup>_−_1</sup> which are input to _h_<sup>_l_</sup> _i_<sup>.Thismakesiteasierforthemodeltotakeintoac-</sup> count which previous inputs have been attended to already compared to recurrent nets where this information is in the recurrent state and needs to survive several non-linearities. Overall, our attention mechanism considers which words we previously attended to (Yang et al., 2016) _and_ performs multiple attention ’hops’ per time step. In Appendix _§_ C, we plot attention scores for a deep decoder and show that at different layers, different portions of the source are attended to. 

Our convolutional architecture also allows to batch the attention computation across all elements of a sequence compared to RNNs (Figure 1, middle). We batch the computations of each decoder layer individually.

---

[referencia=99bf4c74cf248c24 score=0.011]
_Table 4._ Effect of removing position embeddings from our model in terms of validation perplexity (valid PPL) and BLEU. 

beddings from the encoder and decoder ( _§_ 3.1). These embeddings allow our model to identify which portion of the source and target sequence it is dealing with but also impose a restriction on the maximum sentence length. Table 4 shows that position embeddings are helpful but that our model still performs well without them. Removing the source position embeddings results in a larger accuracy decrease than target position embeddings. However, removing both source and target positions decreases accuracy only by 0 _._ 5 BLEU. We had assumed that the model would not be able to calibrate the length of the output sequences very well without explicit position information, however, the output lengths of models without position embeddings closely matches models with position information. This indicates that the models can learn relative position information within the contexts visible to the encoder and decoder networks which can observe up to 27 and 25 words respectively. 

_Table 5._ Multi-step attention in all five decoder layers or fewer layers in terms of validation perplexity (PPL) and test BLEU. 



<!-- Start of picture text -->
 22<br> 21.5<br> 21<br> 20.5<br> 20<br> 19.5<br>Encoder<br>Decoder<br> 19<br> 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25<br>Layers<br>BLEU<br><!-- End of picture text -->

Recurrent models typically do not use explicit position embeddings since they can learn where they are in the sequence through the recurrent hidden state computation. In our setting, the use of position embeddings requires only a simple addition to the input word embeddings which is a negligible overhead. 

_Figure 2._ Encoder and decoder with different number of layers.

---

[referencia=99bf4c74cf248c24 score=0.011]
## **3.2. Convolutional Block Structure** 

Both encoder and decoder networks share a simple block structure that computes intermediate states based on a fixed number of input elements. We denote the output of the _l_ - th block as **h**<sup>_l_</sup> = ( _h_<sup>_l_</sup> 1<sup>_, . . . , hl_</sup> _n_<sup>)forthedecodernetwork,</sup> and **z**<sup>_l_</sup> = ( _z_ 1<sup>_l, . . . , z_</sup> _m_<sup>_l_)fortheencodernetwork;werefer</sup> to blocks and layers interchangeably. Each block contains a one dimensional convolution followed by a non-linearity. For a decoder network with a single block and kernel width _k_ , each resulting state _h_<sup>1</sup> _i_<sup>contains information over</sup><sup>_k_input</sup> elements. Stacking several blocks on top of each other increases the number of input elements represented in a state. For instance, stacking 6 blocks with _k_ = 5 results in an input field of 25 elements, i.e. each output depends on 25 

**Convolutional Sequence to Sequence Learning** 

inputs. Non-linearities allow the networks to exploit the full input field, or to focus on fewer elements if needed. 

Each convolution kernel is parameterized as _W ∈_ R<sup>2</sup><sup>_d×kd_</sup> , _bw ∈_ R<sup>2</sup><sup>_d_</sup> and takes as input _X ∈_ R<sup>_k×d_</sup> which is a concatenation of _k_ input elements embedded in _d_ dimensions and maps them to a single output element _Y ∈_ R<sup>2</sup><sup>_d_</sup> that has twice the dimensionality of the input elements; subsequent layers operate over the _k_ output elements of the previous layer. We choose gated linear units (GLU; Dauphin et al., 2016) as non-linearity which implement a simple gating mechanism over the output of the convolution _Y_ = [ _A B_ ] _∈_ R<sup>2</sup><sup>_d_</sup> :

---

[referencia=a7468c6851652691 score=0.009]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=a7468c6851652691 score=0.007]
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

[referencia=99bf4c74cf248c24 score=0.007]
_Figure 2._ Encoder and decoder with different number of layers. 

a 4% slow down when adding 4 attention modules. Most neural machine translation systems only use a single module. This demonstrates that attention is not the bottleneck in neural machine translation, even though it is quadratic in the sequence length (cf. Kalchbrenner et al., 2016). Part of the reason for the low impact on speed is that we batch the computation of an attention module over all target words, similar to Kalchbrenner et al. (2016). However, for RNNs batching of the attention may be less effective because of the dependence on the previous time step. 

## **5.5. Multi-step Attention** 

The multiple attention mechanism ( _§_ 3.3) computes a separate source context vector for each decoder layer. The computation also takes into account contexts computed for preceding decoder layers of the current time step as well as previous time steps that are within the receptive field of the decoder. How does multiple attention compare to attention in fewer layers or even only in a single layer as is usual? Table 5 shows that attention in all decoder layers achieves the best validation perplexity (PPL). Furthermore, removing more and more attention layers decreases accuracy, both in terms of BLEU as well as PPL.

---

[referencia=99bf4c74cf248c24 score=0.006]
Multi-layer convolutional neural networks create hierarchical representations over the input sequence in which nearby input elements interact at lower layers while distant elements interact at higher layers. Hierarchical structure provides a shorter path to capture long-range dependencies compared to the chain structure modeled by recurrent networks, e.g. we can obtain a feature representation capturing relationships within a window of _n_ words by applying only _O_ (<sup>_<u>n</u>_</sup> _k_<sup>)convolutionaloperationsforkernelsofwidth</sup> _k_ , compared to a linear number _O_ ( _n_ ) for recurrent neural networks. Inputs to a convolutional network are fed through a constant number of kernels and non-linearities, whereas recurrent networks apply up to _n_ operations and non-linearities to the first word and only a single set of operations to the last word. Fixing the number of nonlinearities applied to the inputs also eases learning. 

Recent work has applied convolutional neural networks to sequence modeling such as Bradbury et al. (2016) who introduce recurrent pooling between a succession of convolutional layers or Kalchbrenner et al. (2016) who tackle neural translation without attention. However, none of these approaches has been demonstrated improvements over state of the art results on large benchmark datasets. Gated convolutions have been previously explored for machine translation by Meng et al. (2015) but their evaluation was restricted to a small dataset and the model was used in tandem with a traditional count-based model. Architec- 

**Convolutional Sequence to Sequence Learning** 

tures which are partially convolutional have shown strong performance on larger tasks but their decoder is still recurrent (Gehring et al., 2016). 

In this paper we propose an architecture for sequence to sequence modeling that is entirely convolutional. Our model is equipped with gated linear units (Dauphin et al., 2016) and residual connections (He et al., 2015a). We also use attention in every decoder layer and demonstrate that each attention layer only adds a negligible amount of overhead. The combination of these choices enables us to tackle large scale problems ( _§_ 3).

---

[referencia=99bf4c74cf248c24 score=0.005]
## **A.1. Forward Pass** 

Assuming that the inputs **x** _l_ of a convolutional layer _l_ and its weights _Wl_ are independent and identically distributed (i.i.d.), the variance of its output, computed as **y** _l_ = _Wl_ **x** _l_ + **b** _l_ , is 



where _nl_ is the number inputs to the layer. For onedimensional convolutional layers with kernel width _k_ and input dimension _c_ , this is _kc_ . We adopt the notation in (He et al., 2015b), i.e. _yl_ , _wl_ and _xl_ represent the random variables in **y** _l_ , _Wl_ and **x** _l_ . With _wl_ and _xl_ independent from each other and normally distributed with zero mean, this amounts to 



**x** _l_ is the result of the GLU activation function **y** _l_<sup>_a_</sup> _−_ 1<sup>_σ_(</sup><sup>**y**</sup> _l_<sup>_b_</sup> _−_ 1<sup>)with</sup><sup>**y**</sup><sup>_l−_1=(</sup><sup>**y**</sup> _l_<sup>_a_</sup> _−_ 1<sup>_,_</sup><sup>**y**</sup> _l_<sup>_b_</sup> _−_ 1<sup>),and</sup><sup>**y**</sup> _l_<sup>_a_</sup> _−_ 1<sup>_,_</sup><sup>**y**</sup> _l_<sup>_b_</sup> _−_ 1 i.i.d. Next, we formulate upper and lower bounds in order to approximate _V ar_ [ _xl_ ]. If **y** _l−_ 1 follows a symmetric distribution with mean 0, then

---

[referencia=99bf4c74cf248c24 score=0.005]
## **A.2. Backward Pass** 

The gradient of a convolutional layer is computed via backpropagation as ∆ **x** _l_ = _W_<sup>ˆ</sup> _l_ **y** _l_ . Considering separate gradients ∆ **y** _l_<sup>_a_and ∆</sup><sup>**y**</sup> _l_<sup>_b_for GLU, the gradient of</sup><sup>**x**is given by</sup> 



ˆ _W_ corresponds to _W_ with re-arranged weights to enable back-propagation. Analogously to the forward pass, ∆ _xl_ , _w_ ˆ _l_ and ∆ _yl_ represent the random variables for the values in ∆ **xl** , _W_<sup>ˆ</sup> _l_ and ∆ **yl** , respectively. Note that _W_ and _W_<sup>ˆ</sup> ˆ contain the same values, i.e. _w_ = _w_ . Similar to (3), the variance of ∆ _xl_ is 





**Convolutional Sequence to Sequence Learning** 

The approximation for the forward pass can be used for _V ar_ [∆ _yl_<sup>_a_], and for estimating</sup><sup>_V ar_[∆</sup><sup>_y_</sup> _l_<sup>_b_] we assume an up-</sup> per bound on _E_ [ _σ_<sup>_′_</sup> ( _yl_<sup>_b_)2]of1</sup><sup>_/_16since</sup><sup>_σ′_(</sup><sup>_y_</sup> _l_<sup>_b_)</sup><sup>_∈_[0</sup><sup>_,_</sup> 4<sup><u>1</u>].</sup> Hence, 





We observe relatively small gradients in our network, typically around 0.001 at the start of training. Therefore, we approximate by discarding the quadratic terms above, i.e. 







As for the forward pass, the above result can be generalized to backpropagation through many successive layers, resulting in 

of _r_ and _E_ [ _x_ ] = 0, the variance after dropout is

---

[referencia=99bf4c74cf248c24 score=0.004]
A lower bound is given by (1 _/_ 4) _V ar_ [ _yl_<sup>_a_</sup> _−_ 1<sup>] when expand-</sup> ing (6) with _E_<sup>2</sup> [ _σ_ ( **y** _l_<sup>_b_</sup> _−_ 1<sup>)] = 1</sup><sup>_/_4:</sup> 



and _V ar_ [ _yl_<sup>_a_</sup> _−_ 1<sup>]</sup><sup>_V ar_[</sup><sup>_σ_(</sup><sup>**y**</sup> _l_<sup>_b_</sup> _−_ 1<sup>)]</sup><sup>_>_0.Weutilizetherelation</sup> _σ_ ( _x_ )<sup>2</sup> _≤_ (1 _/_ 16) _x_<sup>2</sup> _−_ 1 _/_ 4 + _σ_ ( _x_ ) (Appendix B) to provide an upper bound on _E_ [ _σ_ ( _x_ )<sup>2</sup> ]: 



With _x ∼N_ (0 _, std_ ( _x_ )), this yields 



With (7) and _V ar_ [ _yl_<sup>_a_</sup> _−_ 1<sup>]=</sup><sup>_V ar_[</sup><sup>_y_</sup> _l_<sup>_b_</sup> _−_ 1<sup>]=</sup><sup>_V ar_[</sup><sup>_yl−_1],this</sup> results in 



We initialize the embedding matrices in our network with small variances (around 0 _._ 01), which allows us to dismiss the quadratic term and approximate the GLU output variance with 



If _L_ network layers of equal size and with GLU activations are combined, the variance of the final output **y** _L_ is given by 



Following (He et al., 2015b), we aim to satisfy the condition 



so that the activations in a network are neither exponentially magnified nor reduced. This is achieved by initializing _Wl_ from _N_ (0 _,_ ~~�~~ 4 _/nl_ ).

---

[referencia=a7468c6851652691 score=0.004]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=a7468c6851652691 score=0.004]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

### **3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ .

---

[referencia=a7468c6851652691 score=0.004]
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

[referencia=a7468c6851652691 score=0.004]
## **4 Why Self-Attention** 

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to another sequence of equal length ( _z_ 1 _, ..., zn_ ), with _xi, zi ∈_ R<sup>_d_</sup> , such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata. 

One is the total computational complexity per layer. Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required. 

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types. 

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires _O_ ( _n_ ) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence 

6 

length _n_ is smaller than the representation dimensionality _d_ , which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size _r_ in the input sequence centered around the respective output position. This would increase the maximum path length to _O_ ( _n/r_ ). We plan to investigate this approach further in future work.

---

[referencia=99bf4c74cf248c24 score=0.003]
# **B. Upper Bound on Squared Sigmoid** 



and a similar condition, i.e. (1 _/_ 4)ˆ _nlV ar_ [ _wl_<sup>_a_]=1.Inthe</sup> networks we consider, successions of convolutional layers usually operate on the same number of inputs so that most ˆ cases _nl_ = _nl_ . Note that _Wl_<sup>_b_isdiscardedintheapprox-</sup> imation; however, for the sake of consistency we use the same initialization for _Wl_<sup>_a_and</sup><sup>_W b_</sup> _l_<sup>.</sup> 

For arbitrarily large variances of network inputs and activations, our approximations are invalid; in that case, the initial values for _Wl_<sup>_a_and</sup><sup>_W b_</sup> _l_<sup>would have to be balanced for</sup> the input distribution to be retained. Alternatively, methods that explicitly control the variance in the network, e.g. batch normalization (Ioffe & Szegedy, 2015) or layer normalization (Ba et al., 2016) could be employed.

---

[referencia=a7468c6851652691 score=0.002]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=a7468c6851652691 score=0.002]
development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3. 

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. 

In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

---

[referencia=99bf4c74cf248c24 score=0.002]
# **6. Conclusion and Future Work** 

We introduce the first fully convolutional model for sequence to sequence learning that outperforms strong recurrent models on very large benchmark datasets at an order of magnitude faster speed. Compared to recurrent networks, our convolutional approach allows to discover compositional structure in the sequences more easily since representations are built hierarchically. Our model relies on gating and performs multiple attention steps. 

We achieve a new state of the art on several public translation benchmark data sets. On the WMT’16 EnglishRomanian task we outperform the previous best result by 1.9 BLEU, on WMT’14 English-French translation we improve over the LSTM model of Wu et al. (2016) by 1.6 BLEU in a comparable setting, and on WMT’14 EnglishGerman translation we ouperform the same model by 0.5 BLEU. In future work, we would like to apply convolutional architectures to other sequence to sequence learning problems which may benefit from learning hierarchical representations as well. 

# **Acknowledgements** 

We thank Benjamin Graham for providing a fast 1-D convolution, and Ronan Collobert as well as Yann LeCun for helpful discussions related to this work.

---

[referencia=a7468c6851652691 score=0.002]
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

[referencia=a7468c6851652691 score=0.002]
### **3.5 Positional Encoding** 

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension _d_ model as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [9]. 

In this work, we use sine and cosine functions of different frequencies: 



where _pos_ is the position and _i_ is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 _π_ to 10000 _·_ 2 _π_ . We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset _k_ , _PEpos_ + _k_ can be represented as a linear function of _PEpos_ . 

We also experimented with using learned positional embeddings [9] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.