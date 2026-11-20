[referencia=a7468c6851652691 score=0.642]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=85f66a6419d173a7 score=0.465]
#### **2.1 Parameter and Compute Scaling of Transformers** 

We parameterize the Transformer architecture using hyperparameters _n_ layer (number of layers), _d_ model (dimension of the residual stream), _d_ ff (dimension of the intermediate feed-forward layer), _d_ attn (dimension of the attention output), and _n_ heads (number of attention heads per layer). We include _n_ ctx tokens in the input context, with _n_ ctx = 1024 except where otherwise noted. 

We use _N_ to denote the model size, which we define as the number of _non-embedding_ parameters 





where we have excluded biases and other sub-leading terms. Our models also have _n_ vocab _d_ model parameters in an embedding matrix, and use _n_ ctx _d_ model parameters for positional embeddings, but we do not include these when discussing the ‘model size’ _N_ ; we will see that this produces significantly cleaner scaling laws. 

Evaluating a forward pass of the Transformer involves roughly 

_C_ forward _≈_ 2 _N_ + 2 _n_ layer _n_ ctx _d_ model (2.2) 

add-multiply operations, where the factor of two comes from the multiply-accumulate operation used in matrix multiplication. A more detailed per-operation parameter and compute count is included in Table 1. 

6 

|**Operation**|**Parameters**|**FLOPs per Token**|
|---|---|---|
|Embed|(_n_vocab+_n_ctx)_d_model|4_d_model|
|Attention: QKV|_n_layer_d_model3_d_attn|2_n_layer_d_model3_d_attn|
|Attention: Mask|—|2_n_layer_n_ctx_d_attn|
|Attention: Project|_n_layer_d_attn_d_model|2_n_layer_d_attn_d_embd|
|Feedforward|_n_layer2_d_model_d_f|2_n_layer2_d_model_d_f|
|De-embed|—|2_d_model_n_vocab|
|**Total (Non-Embedding)**|_N_ = 2_d_model_n_layer(2_d_attn+_d_f)|_C_forward = 2_N_ + 2_n_layer_n_ctx_d_attn|

---

[referencia=a7468c6851652691 score=0.354]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=a7468c6851652691 score=0.220]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=85f66a6419d173a7 score=0.218]
### **1 Introduction** 

Language provides a natural domain for the study of artificial intelligence, as the vast majority of reasoning tasks can be efficiently expressed and evaluated in language, and the world’s text provides a wealth of data for unsupervised learning via generative modeling. Deep learning has recently seen rapid progress in language modeling, with state of the art models [RNSS18, DCLT18, YDY<sup>+</sup> 19, LOG<sup>+</sup> 19, RSR<sup>+</sup> 19] approaching human-level performance on many specific tasks [WPN<sup>+</sup> 19], including the composition of coherent multiparagraph prompted text samples [RWC<sup>+</sup> 19]. 

One might expect language modeling performance to depend on model architecture, the size of neural models, the computing power used to train them, and the data available for this training process. In this work we will empirically investigate the dependence of language modeling loss on all of these factors, focusing on the Transformer architecture [VSP<sup>+</sup> 17, LSP<sup>+</sup> 18]. The high ceiling and low floor for performance on language tasks allows us to study trends over more than seven orders of magnitude in scale. 

Throughout we will observe precise power-law scalings for performance as a function of training time, context length, dataset size, model size, and compute budget.

---

[referencia=85f66a6419d173a7 score=0.212]
#### **1.1 Summary** 

Our key findings for Transformer language models are are as follows: 

> 2Here we display predicted compute when using a sufficiently small batch size. See Figure 13 for comparison to the purely empirical data. 

2 



<!-- Start of picture text -->
C omput e Dataset Size  Parameters<br>PF-days, non-embedding tokens non-embedding<br>Test Loss<br><!-- End of picture text -->

**Figure 1** Language modeling performance improves smoothly as we increase the model size, datasetset size, and amount of compute<sup>2</sup> used for training. For optimal performance all three factors must be scaled up in tandem. Empirical performance has a power-law relationship with each individual factor when not bottlenecked by the other two. **Performance depends strongly on scale, weakly on model shape:** Model performance depends most strongly on scale, which consists of three factors: the number of model parameters _N_ (excluding embeddings), the size of the dataset _D_ , and the amount of compute _C_ used for training. Within reasonable limits, performance depends very weakly on other architectural hyperparameters such as depth vs. width. (Section 3) 

**Smooth power laws:** Performance has a power-law relationship with each of the three scale factors _N, D, C_ when not bottlenecked by the other two, with trends spanning more than six orders of magnitude (see Figure 1). We observe no signs of deviation from these trends on the upper end, though performance must flatten out eventually before reaching zero loss. (Section 3) 

**Universality of overfitting:** Performance improves predictably as long as we scale up _N_ and _D_ in tandem, but enters a regime of diminishing returns if either _N_ or _D_ is held fixed while the other increases. The performance penalty depends predictably on the ratio _N_<sup>0</sup><sup>_._74</sup> _/D_ , meaning that every time we increase the model size 8x, we only need to increase the data by roughly 5x to avoid a penalty. (Section 4) 

**Universality of training:** Training curves follow predictable power-laws whose parameters are roughly independent of the model size. By extrapolating the early part of a training curve, we can roughly predict the loss that would be achieved if we trained for much longer. (Section 5)

---

[referencia=85f66a6419d173a7 score=0.209]
## **Scaling Laws for Neural Language Models** 

**Jared Kaplan**<sup>_∗_</sup> 

Johns Hopkins University, OpenAI 

```
jaredk@jhu.edu
```

**Sam McCandlish**<sup>_∗_</sup> 

OpenAI 

```
sam@openai.com
```

**Tom Henighan** 

**Tom B. Brown** 

**Benjamin Chess** 

#### **Rewon Child** 

OpenAI OpenAI OpenAI OpenAI `henighan@openai.com tom@openai.com bchess@openai.com rewon@openai.com` 

**Scott Gray Alec Radford Jeffrey Wu Dario Amodei** OpenAI OpenAI OpenAI OpenAI `scott@openai.com alec@openai.com jeffwu@openai.com damodei@openai.com` 

### **Abstract** 

We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sampleefficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence. 

> _∗_ Equal contribution. 

> Contributions: Jared Kaplan and Sam McCandlish led the research. Tom Henighan contributed the LSTM experiments. Tom Brown, Rewon Child, and Scott Gray, and Alec Radford developed the optimized Transformer implementation. Jeff Wu, Benjamin Chess, and Alec Radford developed the text datasets. Dario Amodei provided guidance throughout the project.

---

[referencia=a7468c6851652691 score=0.207]
In this work we employ _h_ = 8 parallel attention layers, or heads. For each of these we use _dk_ = _dv_ = _d_ model _/h_ = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality. 

**3.2.3 Applications of Attention in our Model** The Transformer uses multi-head attention in three different ways: 

• In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. 

• The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to 

all positions in the decoder up to and including that position. We need to prevent leftward 

information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2. 

**3.3 Position-wise Feed-Forward Networks** 

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between. 

FFN( _x_ ) = max(0 _, xW_ 1 + _b_ 1) _W_ 2 + _b_ 2 (2) 

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is _d_ model = 512, and the inner-layer has dimensionality _dff_ = 2048. 

**3.4 Embeddings and Softmax**

---

[referencia=a7468c6851652691 score=0.177]
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

[referencia=a7468c6851652691 score=0.160]
### **6.3 English Constituency Parsing** 

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. 

We trained a 4-layer transformer with _dmodel_ = 1024 on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting. 

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we 

9 

Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)

---

[referencia=a7468c6851652691 score=0.146]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

**3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two 

sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention 

sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ . 

**3.2 Attention**

---

[referencia=a7468c6851652691 score=0.143]
## **7 Conclusion** 

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. 

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. 

The code we used to train and evaluate our models is available at `https://github.com/ tensorflow/tensor2tensor` . 

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

---

[referencia=a7468c6851652691 score=0.126]
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

[referencia=85f66a6419d173a7 score=0.110]
#### **1.2 Summary of Scaling Laws** 

The test loss of a Transformer trained to autoregressively model language can be predicted using a power-law when performance is limited by only either the number of non-embedding parameters _N_ , the dataset size _D_ , or the optimally allocated compute budget _C_ min (see Figure 1): 

1. For models with a limited number of parameters, trained to convergence on sufficiently large datasets: 



2. For large models trained with a limited dataset with early stopping: 



3. When training with a limited amount of compute, a sufficiently large dataset, an optimally-sized model, and a sufficiently small batch size (making optimal<sup>3</sup> use of compute): 



> 3We also observe an empirical power-law trend with the training compute _C_ (Figure 1) while training at fixed batch size, but it is the trend with _C_ min that should be used to make predictions. They are related by equation (5.5). 

4 



<!-- Start of picture text -->
Loss vs Model and Dataset Size Loss vs Model Size and Training Steps<br>4.4<br>4.5<br>4.0<br>4.0 Params 10 8<br>708M 3.6<br>3.5 302M<br>85M3M 3.2 10 7<br>3.0 25M<br>393.2K 2.8<br>10 6<br>2.5<br>2.4<br>10 7 10 8 10 9 10 10 10 4 10 5<br>Tokens in Dataset Estimated Smin<br>Loss Loss<br>Parameters (non-embed)<br><!-- End of picture text -->

**Figure 4 Left** : The early-stopped test loss _L_ ( _N, D_ ) varies predictably with the dataset size _D_ and model size _N_ according to Equation (1.5). **Right** : After an initial transient period, learning curves for all model sizes _N_ can be fit with Equation (1.6), which is parameterized in terms of _S_ min, the number of steps when training at large batch size (details in Section 5.1).

---

[referencia=a7468c6851652691 score=0.105]
### **6.2 Model Variations** 

To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the 

> 5We used values of 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively. 

8 

Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development set, newstest2013. Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities.

---

[referencia=85f66a6419d173a7 score=0.080]
Test Loss 5.4 Per-token<br>Test Loss 6<br>4.8<br>4.2 LSTMs 4 Parameters:<br>3.6 400K<br>1 Layer2 Layers 5 400K2M<br>3.0 Transformers 4 Layers 3M<br>3 200M<br>2.4 300M<br>2<br>10 5 10 6 10 7 10 8 10 9 10 1 10 2 10 3<br>Parameters (non-embedding) Token Index in Context<br>Figure 7<br>To observe these trends it is crucial to study performance as a function of N ; if we instead use the total<br>parameter count (including the embedding parameters) the trend is somewhat obscured (see Figure 6). This<br>suggests that the embedding matrix can be made smaller without impacting performance, as has been seen in<br>recent work [LCG + 19].<br>Although these models have been trained on the WebText2 dataset, their test loss on a variety of other datasets<br>is also a power-law in  N with nearly identical power, as shown in Figure 8.<br>3.2.1 Comparing to LSTMs and Universal Transformers<br>In Figure 7 we compare LSTM and Transformer performance as a function of non-embedding parameter<br>count N . The LSTMs were trained with the same dataset and context length. We see from these figures<br>that the LSTMs perform as well as Transformers for tokens appearing early in the context, but cannot match<br>the Transformer performance for later tokens. We present power-law relationships between performance and<br>context position Appendix D.5, where increasingly large powers for larger models suggest improved ability<br>to quickly recognize patterns.<br>We also compare the performance of standard Transformers to recurrent Transformers [DGV + 18] in Figure<br>17 in the appendix. These models re-use parameters, and so perform slightly better as a function of  N , at the<br>cost of additional compute per-parameter.<br>3.2.2 Generalization Among Data Distributions<br>We have also tested our models on a set of additional text data distributions. The test loss on these datasets<br>as a function of model size is shown in Figure 8; in all cases the models were trained only on the WebText2<br>

---

[referencia=85f66a6419d173a7 score=0.076]
### **3 Empirical Results and Basic Power Laws** 

To characterize language model scaling we train a wide variety of models, varying a number of factors including: 

- Model size (ranging in size from 768 to 1.5 billion non-embedding parameters) 

- Dataset size (ranging from 22 million to 23 billion tokens) 

- Shape (including depth, width, attention heads, and feed-forward dimension) 

- Context length (1024 for most runs, though we also experiment with shorter contexts) 

- Batch size (2<sup>19</sup> for most runs, but we also vary it to measure the critical batch size) 

7 



<!-- Start of picture text -->
10%<br>8%<br>6% A wide range of architectures<br>achieve similar performance<br>4% 22% additional compute<br>compensates for 1% loss increase<br>2%<br>0%<br>Feed-Forward Ratio (dff / dmodel)  Attention Head Dimension  (dmodel / nhead)<br>50M Parameters Aspect Ratio (dmodel / nlayer) 25M Parameters<br>Loss Increase<br><!-- End of picture text -->

**Figure 5** Performance depends very mildly on model shape when the total number of non-embedding parameters _N_ is held fixed. The loss varies only a few percent over a wide range of shapes. Small differences in parameter counts are compensated for by using the fit to _L_ ( _N_ ) as a baseline. Aspect ratio in particular can vary by a factor of 40 while only slightly impacting performance; an ( _n_ layer _, d_ model) = (6 _,_ 4288) reaches a loss within 3% of the (48 _,_ 1600) model used in [RWC<sup>+</sup> 19]. 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.074]
- [RNSS18] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language understanding by generative pre-training. _URL https://s3-us-west-2. amazonaws. com/openaiassets/research-covers/languageunsupervised/language understanding paper. pdf_ , 2018. 2, 6 

- [RRBS19a] Jonathan S. Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. A constructive prediction of the generalization error across scales, 2019, 1909.12673. 18 

- [RRBS19b] Jonathan S. Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. A constructive prediction of the generalization error across scales, 2019, arXiv:1909.12673. 18 

- [RSR<sup>+</sup> 19] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer, 2019, arXiv:1910.10683. 2 

- [RWC<sup>+</sup> 19] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. _openai.com_ , 2019. 2, 5, 6, 7, 8 

- [SCP<sup>+</sup> 18] Noam Shazeer, Youlong Cheng, Niki Parmar, Dustin Tran, Ashish Vaswani, Penporn Koanantakool, Peter Hawkins, HyoukJoong Lee, Mingsheng Hong, Cliff Young, Ryan Sepassi, and Blake Hechtman. Mesh-tensorflow: Deep learning for supercomputers, 2018, 1811.02084. 19 

- [SHB15] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. _CoRR_ , 2015, 1508.07909. 6 

29

---

[referencia=85f66a6419d173a7 score=0.070]
<!-- Start of picture text -->
7 7<br>6 6<br>5 5<br>0 Layer<br>4 4<br>1 Layer 1 Layer<br>2 Layers 2 Layers<br>3 3 Layers 3 3 Layers<br>6 Layers 6 Layers<br>> 6 Layers > 6 Layers<br>2 2<br>10 6 10 7 10 8 10 9 10 3 10 4 10 5 10 6 10 7 10 8 10 9<br>Parameters (with embedding) Parameters (non-embedding)<br>Test Loss Test Loss<br><!-- End of picture text -->

**Figure 6 Left:** When we include embedding parameters, performance appears to depend strongly on the number of layers in addition to the number of parameters. **Right:** When we exclude embedding parameters, the performance of models with different depths converge to a single trend. Only models with fewer than 2 layers or with extreme depth-to-width ratios deviate significantly from the trend. 

In this section we will display data along with empirically-motivated fits, deferring theoretical analysis to later sections. 

#### **3.1 Approximate Transformer Shape and Hyperparameter Independence** 

Transformer performance depends very weakly on the shape parameters _n_ layer _, n_ heads, and _d_ ff when we hold the total non-embedding parameter count _N_ fixed. To establish these results we trained models with fixed size while varying a single hyperparameter. This was simplest for the case of _n_ heads. When varying _n_ layer, we simultaneously varied _d_ model while keeping _N ≈_ 12 _n_ layer _d_<sup>2</sup> model<sup>fixed.Similarly,tovary</sup><sup>_d_ffatfixed</sup> model size we also simultaneously varied the _d_ model parameter, as required by the parameter counts in Table 1. Independence of _n_ layers would follow if deeper Transformers effectively behave as ensembles of shallower models, as has been suggested for ResNets [VWB16]. The results are shown in Figure 5.

---

[referencia=85f66a6419d173a7 score=0.055]
#### **5.1 Adjustment for Training at** _B_ crit( _L_ ) 

A simple empirical theory for the batch size dependence of training was developed in [MKAT18] (see also [SLA<sup>+</sup> 18, ZLN<sup>+</sup> 19]). It was argued that there is a critical batch size _B_ crit for training; for _B_ up to _B_ crit the batch size can be increased with very minimal degradation in compute-efficiency, whereas for _B > B_ crit increases in _B_ result in diminishing returns. It was also argued that the gradient noise scale provides a simple 

12 

prediction for _B_ crit, and that neither depends directly on model size except through the value of the loss that has been attained. These results can be used to predict how training time and compute will vary with the batch size. To utilize both training time and compute as effectively as possible, it is best to train with a batch size _B ≈ B_ crit. Training at _B ≫ B_ crit minimizes the number of training steps, while _B ≪ B_ crit minimizes the use of compute. 

More specifically, it was demonstrated that for a wide variety of neural network tasks, the number of training steps _S_ and the number of data examples processed _E_ = _BS_ satisfy the simple relation 



when training to any fixed value of the loss _L_ . Here _S_ min is the minimum number of steps necessary to reach _L_ , while _E_ min is the minimum number of data examples that must be processed. 

We demonstrate the relation (5.1) for Transformers in Figure 18 in the appendix. This relation defines the critical batch size 



which is a function of the target value of the loss. Training at the critical batch size makes a roughly optimal time/compute tradeoff, requiring 2 _S_ min training steps and processing _E_ = 2 _E_ min data examples. 

In Figure 10 we have plotted the critical batch size and gradient noise scale<sup>5</sup> as a function of training loss for two different models. We see that _B_ crit( _L_ ) is independent of model size, and only depends on the loss _L_ . So the predictions of [MKAT18] continue to hold for Transformer language models. The critical batch size can be fit with a power-law in the loss