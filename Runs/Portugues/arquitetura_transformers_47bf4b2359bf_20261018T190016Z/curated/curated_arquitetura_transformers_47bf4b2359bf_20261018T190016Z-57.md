[referencia=887da5f02141c29f score=0.323]
- Figure 4: Schematics of the Transformer architecture variants we consider. In this diagram, blocks represent elements of a sequence and lines represent attention visibility. Different colored groups of blocks indicate different Transformer layer stacks. Dark grey lines correspond to fully-visible masking and light grey lines correspond to causal masking. We use “.” to denote a special end-of-sequence token that represents the end of a prediction. The input and output sequences are represented as _x_ and _y_ respectively. Left: A standard encoder-decoder architecture uses fullyvisible masking in the encoder and the encoder-decoder attention, with causal masking in the decoder. Middle: A language model consists of a single Transformer layer stack and is fed the concatenation of the input and target, using a causal mask throughout. Right: Adding a prefix to a language model corresponds to allowing fully-visible masking over the input. 

obtain the model’s prediction for this example, the model would be fed the prefix “translate English to German: That is good. target:” and would be asked to generate the remainder of the sequence autoregressively. In this way, the model can predict an output sequence given an input, which satisfies the needs of text-to-text tasks. This approach was recently used to show that language models can learn to perform some text-to-text tasks without supervision (Radford et al., 2019). 

A fundamental and frequently cited drawback of using a language model in the textto-text setting is that causal masking forces the model’s representation of the _i_ th entry of the input sequence to only depend on the entries up until _i_ . To see why this is potentially disadvantageous, consider the text-to-text framework where the model is provided with a prefix/context before being asked to make predictions (e.g., the prefix is an English sentence and the model is asked to predict the German translation). With fully causal masking, the model’s representation of a prefix state can only depend on prior entries of the prefix. So, when predicting an entry of the output, the model will attend to a representation of the prefix that is unnecessarily limited. Similar arguments have been made against using a unidirectional recurrent neural network encoder in sequence-to-sequence models (Bahdanau et al., 2015). 

17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.319]
### 3.2.1 Model Structures 

A major distinguishing factor for different architectures is the “mask” used by different attention mechanisms in the model. Recall that the self-attention operation in a Transformer takes a sequence as input and outputs a new sequence of the same length. Each entry of the output sequence is produced by computing a weighted average of entries of the input sequence. Specifically, let _yi_ refer to the _i_ th element of the output sequence and _xj_ refer to the _j_ th entry of the input sequence. _yi_ is computed as<sup>�</sup> _j_<sup>_wi,jxj_,where</sup><sup>_wi,j_isthescalar</sup> weight produced by the self-attention mechanism as a function of _xi_ and _xj_ . The attention mask is then used to zero out certain weights in order to constrain which entries of the input can be attended to at a given output timestep. Diagrams of the masks we will consider are shown in Figure 3. For example, the causal mask (Figure 3, middle) sets any _wi,j_ to zero if _j > i_ . 

The first model structure we consider is an an encoder-decoder Transformer, which consists of two layer stacks: The encoder, which is fed an input sequence, and the decoder, which produces a new output sequence. A schematic of this architectural variant is shown in the left panel of Figure 4. 

The encoder uses a “fully-visible” attention mask. Fully-visible masking allows a selfattention mechanism to attend to any entry of the input when producing each entry of its output. We visualize this masking pattern in Figure 3, left. This form of masking is appropriate when attending over a “prefix”, i.e. some context provided to the model that is later used when making predictions. BERT (Devlin et al., 2018) also uses a fully-visible masking pattern and appends a special “classification” token to the input. BERT’s output 

15 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 



<!-- Start of picture text -->

---

[referencia=887da5f02141c29f score=0.240]
Overall, our encoder-decoder Transformer implementation closely follows its originallyproposed form (Vaswani et al., 2017). First, an input sequence of tokens is mapped to a sequence of embeddings, which is then passed into the encoder. The encoder consists of a stack of “blocks”, each of which comprises two subcomponents: a self-attention layer followed by a small feed-forward network. Layer normalization (Ba et al., 2016) is applied to the input of each subcomponent. We use a simplified version of layer normalization where the activations are only rescaled and no additive bias is applied. After layer normalization, a residual skip connection (He et al., 2016) adds each subcomponent’s input to its output. Dropout (Srivastava et al., 2014) is applied within the feed-forward network, on the skip connection, on the attention weights, and at the input and output of the entire stack. The decoder is similar in structure to the encoder except that it includes a standard attention 

> 3. `http://nlp.seas.harvard.edu/2018/04/03/attention.html` 

> 4. `http://jalammar.github.io/illustrated-transformer/` 

4 

Exploring the Limits of Transfer Learning 

mechanism after each self-attention layer that attends to the output of the encoder. The self-attention mechanism in the decoder also uses a form of autoregressive or causal selfattention, which only allows the model to attend to past outputs. The output of the final decoder block is fed into a dense layer with a softmax output, whose weights are shared with the input embedding matrix. All attention mechanisms in the Transformer are split up into independent “heads” whose outputs are concatenated before being further processed.

---

[referencia=a7468c6851652691 score=0.238]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

### **3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ .

---

[referencia=887da5f02141c29f score=0.209]
### 3.2.4 Results 

The scores achieved by each of the architectures we compare are shown in Table 2. For all tasks, the encoder-decoder architecture with the denoising objective performed best. This variant has the highest parameter count (2 _P_ ) but the same computational cost as the _P_ -parameter decoder-only models. Surprisingly, we found that sharing parameters across the encoder and decoder performed nearly as well. In contrast, halving the number of layers in 

19 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.168]
To provide a reasonable means of comparison, we consider multiple configurations for our encoder-decoder model. We will refer to the number of layers and parameters in a BERTBASE-sized layer stack as _L_ and _P_ , respectively. We will use _M_ to refer to the number of FLOPs required for an _L_ + _L_ -layer encoder-decoder model or _L_ -layer decoder-only model to process a given input-target pair. In total, we will compare: 

- An encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder. This model has 2 _P_ parameters and a computation cost of _M_ FLOPs. 

- An equivalent model, but with parameters shared across the encoder and decoder, resulting in _P_ parameters and an _M_ -FLOP computational cost. 

- An encoder-decoder model with _L/_ 2 layers each in the encoder and decoder, giving _P_ parameters and an _M/_ 2-FLOP cost. 

- A decoder-only language model with _L_ layers and _P_ parameters and a resulting computational cost of _M_ FLOPs. 

- A decoder-only prefix LM with the same architecture (and thus the same number of parameters and computational cost), but with fully-visible self-attention over the input.

---

[referencia=a7468c6851652691 score=0.160]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=887da5f02141c29f score=0.149]
### **3.1 Baseline** 

Our goal for our baseline is to reflect typical, modern practice. We pre-train a standard Transformer (described in Section 2.1) using a simple denoising objective and then separately fine-tune on each of our downstream tasks. We describe the details of this experimental setup in the following subsections. 

### 3.1.1 Model 

For our model, we use a standard encoder-decoder Transformer as proposed by Vaswani et al. (2017). While many modern approaches to transfer learning for NLP use a Transformer architecture consisting of only a single “stack” (e.g. for language modeling (Radford et al., 2018; Dong et al., 2019) or classification and span prediction (Devlin et al., 2018; Yang et al., 2019)), we found that using a standard encoder-decoder structure achieved good results on both generative and classification tasks. We explore the performance of different model architectures in Section 3.2. 

Our baseline model is designed so that the encoder and decoder are each similar in size and configuration to a “BERTBASE” (Devlin et al., 2018) stack. Specifically, both the encoder and decoder consist of 12 blocks (each block comprising self-attention, optional encoder-decoder attention, and a feed-forward network). The feed-forward networks in each block consist of a dense layer with an output dimensionality of _d_ ff = 3072 followed by a ReLU nonlinearity and another dense layer. The “key” and “value” matrices of all attention mechanisms have an inner dimensionality of _d_ kv = 64 and all attention mechanisms have 12 heads. All other sub-layers and embeddings have a dimensionality of _d_ model = 768. In total, this results in a model with about 220 million parameters. This is roughly twice the number of parameters of BERTBASE since our baseline model contains two layer stacks instead of one. For regularization, we use a dropout probability of 0 _._ 1 everywhere dropout is applied in the model.

---

[referencia=887da5f02141c29f score=0.140]
### 3.2.2 Comparing Different Model Structures 

In the interest of experimentally comparing these architectural variants, we would like each model we consider to be equivalent in some meaningful way. We might say that two models are equivalent if they either have the same number of parameters or they require roughly the same amount of computation to process a given (input-sequence, target-sequence) pair. Unfortunately, it is not possible to compare an encoder-decoder model to a language model architecture (comprising a single Transformer stack) according to both of these criteria at the same time. To see why, first note an encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder has approximately the same number of parameters as a language model with 2 _L_ layers. However, the same _L_ + _L_ encoder-decoder model will have approximately the same computational cost as a language model with _only L_ layers. This is a consequence of the fact that the _L_ layers in the language model must be applied to _both_ the input and output sequence, while the encoder is only applied to the input sequence and the decoder is only applied to the output sequence. Note that these equivalences are approximate—there are some extra parameters in the decoder due to the encoder-decoder attention and there are also some computational costs in the attention layers that are quadratic in the sequence lengths. In practice, however, we observed nearly identical step 

18 

Exploring the Limits of Transfer Learning 

times for _L_ -layer language models versus _L_ + _L_ -layer encoder-decoder models, suggesting a roughly equivalent computational cost. Further, for the model sizes we consider, the number of parameters in the encoder-decoder attention layers is about 10% of the total parameter count, so we make the simplifying assumption that an _L_ + _L_ -layer encoder-decoder model has the same number of parameters as an 2 _L_ -layer language model.

---

[referencia=887da5f02141c29f score=0.088]
The decoder in an encoder-decoder Transformer is used to autoregressively produce an output sequence. That is, at each output timestep, a token is sampled from the model’s predicted distribution and the sample is fed back into the model to produce a prediction for the next output timestep, and so on. As such, a Transformer decoder (without an encoder) can be used as a language model (LM), i.e. a model trained solely for next-step prediction (Liu et al., 2018; Radford et al., 2018; Al-Rfou et al., 2019). This constitutes the second model structure we consider. A schematic of this architecture is shown in Figure 4, middle. In fact, early work on transfer learning for NLP used this architecture with a language modeling objective as a pre-training method (Radford et al., 2018). 

Language models are typically used for compression or sequence generation (Graves, 2013). However, they can also be used in the text-to-text framework simply by concatenating the inputs and targets. As an example, consider the case of English to German translation: If we have a training datapoint with input sentence “That is good.” and target “Das ist gut.”, we would simply train the model on next-step prediction over the concatenated input sequence “translate English to German: That is good. target: Das ist gut.” If we wanted to 

16 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
y1 y2 .<br>Language model Prefix LM<br>x2 x3 y1 y2 . x2 x3 y1 y2 .<br>x x x x x1 x2 x3 y1 y2 x1 x2 x3 y1 y2<br>1 2 3 4<br>Decoder<br>Encoder<br><!-- End of picture text -->

---

[referencia=887da5f02141c29f score=0.085]
|Language model|LM|_P_|_M_|73_._78|17_._54|53_._81|56_._51|25_._23|34_._31|25_._38|
|Prefx LM|LM|_P_|_M_|79_._68|17_._84|76_._87|64_._86|26_._28|37_._51|26_._76|



Table 2: Performance of the different architectural variants described in Section 3.2.2. We use _P_ to refer to the number of parameters in a 12-layer base Transformer layer stack and _M_ to refer to the FLOPs required to process a sequence using the encoderdecoder model. We evaluate each architectural variant using a denoising objective (described in Section 3.1.4) and an autoregressive objective (as is commonly used to train language models). 

the encoder and decoder stacks significantly hurt performance. Concurrent work (Lan et al., 2019) also found that sharing parameters across Transformer blocks can be an effective means of lowering the total parameter count without sacrificing much performance. XLNet also bears some resemblance to the shared encoder-decoder approach with a denoising objective (Yang et al., 2019). We also note that the shared parameter encoder-decoder outperforms the decoder-only prefix LM, suggesting that the addition of an explicit encoder-decoder attention is beneficial. Finally, we confirm the widely-held conception that using a denoising objective always results in better downstream task performance compared to a language modeling objective. This observation has been previously made by Devlin et al. (2018), Voita et al. (2019), and Lample and Conneau (2019) among others. We undertake a more detailed exploration of unsupervised objectives in the following section.

---

[referencia=a7468c6851652691 score=0.071]
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

[referencia=a7468c6851652691 score=0.069]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=887da5f02141c29f score=0.065]
### **2.1 Model** 

Early results on transfer learning for NLP leveraged recurrent neural networks (Peters et al., 2018; Howard and Ruder, 2018), but it has recently become more common to use models based on the “Transformer” architecture (Vaswani et al., 2017). The Transformer was initially shown to be effective for machine translation, but it has subsequently been used in a wide variety of NLP settings (Radford et al., 2018; Devlin et al., 2018; McCann et al., 2018; Yu et al., 2018). Due to its increasing ubiquity, all of the models we study are based on the Transformer architecture. Apart from the details mentioned below and the variants we explore in Section 3.2, we do not deviate significantly from this architecture as originally proposed. Instead of providing a comprehensive definition of this model, we refer the interested reader to the original paper (Vaswani et al., 2017) or follow-up tutorials<sup>3,4</sup> for a more detailed introduction. 

The primary building block of the Transformer is self-attention (Cheng et al., 2016). Self-attention is a variant of attention (Graves, 2013; Bahdanau et al., 2015) that processes a sequence by replacing each element by a weighted average of the rest of the sequence. The original Transformer consisted of an encoder-decoder architecture and was intended for sequence-to-sequence (Sutskever et al., 2014; Kalchbrenner et al., 2014) tasks. It has recently also become common to use models consisting of a single Transformer layer stack, with varying forms of self-attention used to produce architectures appropriate for language modeling (Radford et al., 2018; Al-Rfou et al., 2019) or classification and span prediction tasks (Devlin et al., 2018; Yang et al., 2019). We empirically explore these architectural variants in Section 3.2.

---

[referencia=887da5f02141c29f score=0.065]
15 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 



<!-- Start of picture text -->
y5 y5 y5<br>y4 y4 y4<br>y3 y3 y3<br>y2 y2 y2<br>y1 y1 y1<br>x x x x x x x x x x x x x x x<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br><!-- End of picture text -->

Figure 3: Matrices representing different attention mask patterns. The input and output of the self-attention mechanism are denoted _x_ and _y_ respectively. A dark cell at row _i_ and column _j_ indicates that the self-attention mechanism is allowed to attend to input element _j_ at output timestep _i_ . A light cell indicates that the self-attention mechanism is _not_ allowed to attend to the corresponding _i_ and _j_ combination. Left: A fully-visible mask allows the self-attention mechanism to attend to the full input at every output timestep. Middle: A causal mask prevents the _i_ th output element from depending on any input elements from “the future”. Right: Causal masking with a prefix allows the self-attention mechanism to use fully-visible masking on a portion of the input sequence. 

at the timestep corresponding to the classification token is then used to make a prediction for classifying the input sequence. 

The self-attention operations in the Transformer’s decoder use a “causal” masking pattern. When producing the _i_ th entry of the output sequence, causal masking prevents the model from attending to the _j_ th entry of the input sequence for _j > i_ . This is used during training so that the model can’t “see into the future” as it produces its output. An attention matrix for this masking pattern is shown in Figure 3, middle.

---

[referencia=887da5f02141c29f score=0.057]
|Architecture|Objective|Params|Cost|GLUE|CNNDM|SQuAD|SGLUE|EnDe|EnFr|EnRo|
|---|---|---|---|---|---|---|---|---|---|---|
|⋆Encoder-decoder|Denoising|2_P_|_M_|**83**_._**28**|**19**_._**24**|**80**_._**88**|**71**_._**36**|**26**_._**98**|**39**_._**82**|**27**_._**65**|
|Enc-dec, shared|Denoising|_P_|_M_|82_._81|18_._78|**80**_._**63**|**70**_._**73**|26_._72|39_._03|**27**_._**46**|
|Enc-dec, 6 layers|Denoising|_P_|_M/_2|80_._88|18_._97|77_._59|68_._42|26_._38|38_._40|26_._95|
|Language model|Denoising|_P_|_M_|74_._70|17_._93|61_._14|55_._02|25_._09|35_._28|25_._86|
|Prefx LM|Denoising|_P_|_M_|81_._82|18_._61|78_._94|68_._11|26_._43|37_._98|27_._39|
|Encoder-decoder|LM|2_P_|_M_|79_._56|18_._59|76_._02|64_._29|26_._27|39_._17|26_._86|
|Enc-dec, shared|LM|_P_|_M_|79_._60|18_._13|76_._35|63_._50|26_._62|39_._17|27_._05|
|Enc-dec, 6 layers|LM|_P_|_M/_2|78_._67|18_._26|75_._32|64_._06|26_._13|38_._42|26_._89|

---

[referencia=887da5f02141c29f score=0.052]
   - **Large.** Since our baseline uses a BERTBASE-sized encoder and decoder, we also consider a variant where the encoder and decoder are both similar in size and structure to BERTLARGE. Specifically, this variant uses _d_ model = 1 _,_ 024, _d_ ff = 4 _,_ 096, _d_ kv = 64, 16-headed attention, and 24 layers each in the encoder and decoder, resulting in around 770 million parameters. 

   - **3B and 11B.** To further explore what kind of performance is possible when using larger models, we consider two additional variants. In both cases, we use _d_ model = 1024, a 24 layer encoder and decoder, and _d_ kv = 128. For the “3B” variant, we use _d_ ff = 16 _,_ 384 with 32-headed attention, which results in around 2 _._ 8 billion parameters; for “11B” we use _d_ ff = 65 _,_ 536 with 128-headed attention producing a model with about 11 billion parameters. We chose to scale up _d_ ff specifically because modern accelerators (such as the TPUs we train our models on) are most efficient for large dense matrix multiplications like those in the Transformer’s feed-forward networks.

---

[referencia=887da5f02141c29f score=0.045]
### **4.1 Takeaways** 

- **Text-to-text** Our text-to-text framework provides a simple way to train a single model on a wide variety of text tasks using the same loss function and decoding procedure. We showed how this approach can be successfully applied to generative tasks like abstractive summarization, classification tasks like natural language inference, and even regression tasks like STS-B. In spite of its simplicity, we found the text-totext framework obtained comparable performance to task-specific architectures and ultimately produced state-of-the-art results when combined with scale. 

- **Architectures** While some work on transfer learning for NLP has considered architectural variants of the Transformer, we found the original encoder-decoder form worked best in our text-to-text framework. Though an encoder-decoder model uses twice as many parameters as “encoder-only” (e.g. BERT) or “decoder-only” (language model) architectures, it has a similar computational cost. We also showed that sharing the parameters in the encoder and decoder did not result in a substantial performance drop while halving the total parameter count. 

41 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=a7468c6851652691 score=0.027]
## **4 Why Self-Attention** 

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to another sequence of equal length ( _z_ 1 _, ..., zn_ ), with _xi, zi ∈_ R<sup>_d_</sup> , such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata. 

One is the total computational complexity per layer. Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required. 

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types. 

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires _O_ ( _n_ ) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence 

6 

length _n_ is smaller than the representation dimensionality _d_ , which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size _r_ in the input sequence centered around the respective output position. This would increase the maximum path length to _O_ ( _n/r_ ). We plan to investigate this approach further in future work.

---

[referencia=887da5f02141c29f score=0.022]
Table 10: Comparison of different alternative fine-tuning methods that only update a subset of the model’s parameters. For adapter layers, _d_ refers to the inner dimensionality of the adapters. 

parameters of the final layer are updated, then after training for a certain number of updates the parameters of the second-to-last layer are also included, and so on until the entire network’s parameters are being fine-tuned. To adapt this approach to our encoder-decoder model, we gradually unfreeze layers in the encoder and decoder in parallel, starting from the top in both cases. Since the parameters of our input embedding matrix and output classification matrix are shared, we update them throughout fine-tuning. Recall that our baseline model consists of 12 layers each in the encoder and decoder and is fine-tuned for 2<sup>18</sup> steps. As such, we subdivide the fine-tuning process into 12 episodes of<sup>218</sup> _/_ 12 steps each and train from layers 12 _− n_ to 12 in the _n_ th episode. We note that Howard and Ruder (2018) suggested fine-tuning an additional layer after each epoch of training. However, since our supervised data sets vary so much in size and since some of our downstream tasks are actually mixtures of many tasks (GLUE and SuperGLUE), we instead adopt the simpler strategy of fine-tuning an additional layer after every<sup>218</sup> _/_ 12 steps.