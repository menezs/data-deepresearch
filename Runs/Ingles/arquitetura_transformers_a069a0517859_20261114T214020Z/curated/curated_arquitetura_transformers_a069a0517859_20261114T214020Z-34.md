[referencia=887da5f02141c29f score=0.962]
### 3.3.1 Disparate High-Level Approaches 

To begin with, we compare three techniques that are inspired by commonly-used objectives but differ significantly in their approach. First, we include a basic “prefix language modeling” objective as was used in Section 3.2.3. This technique splits a span of text into two components, one to use as inputs to the encoder and the other to use as a target sequence to be predicted by the decoder. Second, we consider an objective inspired by the “masked language modeling” (MLM) objective used in BERT (Devlin et al., 2018). MLM takes a span of text and corrupts 15% of the tokens. 90% of the corrupted tokens are replaced with a special mask token and 10% are replaced with a random token. Since BERT is an encoder-only model, its goal during pre-training is to reconstruct masked tokens at the output of the encoder. In the encoder-decoder case, we simply use the entire uncorrupted sequence as the target. Note that this differs from our baseline objective, which uses only the corrupted tokens as targets; we compare these two approaches in Section 3.3.2. Finally, we also consider a basic deshuffling objective as used e.g. in (Liu et al., 2019a) where it was applied to a denoising sequential autoencoder. This approach takes a sequence of tokens, shuffles it, and then uses the original deshuffled sequence as a target. We provide examples of the inputs and targets for these three methods in the first three rows of Table 3. 

The performance of these three objectives is shown in Table 4. Overall, we find that the BERT-style objective performs best, though the prefix language modeling objective attains similar performance on the translation tasks. Indeed, the motivation for the BERT objective was to outperform language model-based pre-training. The deshuffling objective performs considerably worse than both prefix language modeling and the BERT-style objective. 

21 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.939]
Table 7: Performance of the span-corruption objective (inspired by Joshi et al. (2019)) for different average span lengths. In all cases, we corrupt 15% of the original text sequence. 

randomly to satisfy these specified parameters. For example, if we are processing a sequence of 500 tokens and we have specified that 15% of tokens should be corrupted and that there should be 25 total spans, then the total number of corrupted tokens would be 500 _×_ 0 _._ 15 = 75 and the average span length would be 75 _/_ 25 = 3. Note that given the original sequence length and corruption rate, we can equivalently parametrize this objective either by the average span length or the total number of spans. 

We compare the span-corruption objective to the i.i.d-corruption objective in Table 7. We use a corruption rate of 15% in all cases and compare using average span lengths of 2, 3, 5 and 10. Again, we find a limited difference between these objectives, though the version with an average span length of 10 slightly underperforms the other values in some cases. We also find in particular that using an average span length of 3 slightly (but significantly) outperforms the i.i.d. objective on most non-translation benchmarks. Fortunately, the span-corruption objective also provides some speedup during training compared to the i.i.d. noise approach because span corruption produces shorter sequences on average. 

### 3.3.5 Discussion 

Figure 5 shows a flow chart of the choices made during our exploration of unsupervised objectives. Overall, the most significant difference in performance we observed was that denoising objectives outperformed language modeling and deshuffling for pre-training. We did not observe a remarkable difference across the many variants of the denoising objectives we explored. However, different objectives (or parameterizations of objectives) can lead to different sequence lengths and thus different training speeds. This implies that choosing among the denoising objectives we considered here should mainly be done according to their computational cost. Our results also suggest that additional exploration of objectives similar to the ones we consider here may not lead to significant gains for the tasks and model we consider. Instead, it may be fortuitous to explore entirely different ways of leveraging unlabeled data.

---

[referencia=887da5f02141c29f score=0.919]
|Language model|LM|_P_|_M_|73_._78|17_._54|53_._81|56_._51|25_._23|34_._31|25_._38|
|Prefx LM|LM|_P_|_M_|79_._68|17_._84|76_._87|64_._86|26_._28|37_._51|26_._76|



Table 2: Performance of the different architectural variants described in Section 3.2.2. We use _P_ to refer to the number of parameters in a 12-layer base Transformer layer stack and _M_ to refer to the FLOPs required to process a sequence using the encoderdecoder model. We evaluate each architectural variant using a denoising objective (described in Section 3.1.4) and an autoregressive objective (as is commonly used to train language models). 

the encoder and decoder stacks significantly hurt performance. Concurrent work (Lan et al., 2019) also found that sharing parameters across Transformer blocks can be an effective means of lowering the total parameter count without sacrificing much performance. XLNet also bears some resemblance to the shared encoder-decoder approach with a denoising objective (Yang et al., 2019). We also note that the shared parameter encoder-decoder outperforms the decoder-only prefix LM, suggesting that the addition of an explicit encoder-decoder attention is beneficial. Finally, we confirm the widely-held conception that using a denoising objective always results in better downstream task performance compared to a language modeling objective. This observation has been previously made by Devlin et al. (2018), Voita et al. (2019), and Lample and Conneau (2019) among others. We undertake a more detailed exploration of unsupervised objectives in the following section.

---

[referencia=887da5f02141c29f score=0.894]
### 3.3.2 Simplifying the BERT Objective 

Based on the results in the prior section, we will now focus on exploring modifications to the BERT-style denoising objective. This objective was originally proposed as a pre-training technique for an encoder-only model trained for classification and span prediction. As such, it may be possible to modify it so that it performs better or is more efficient in our encoder-decoder text-to-text setup. 

First, we consider a simple variant of the BERT-style objective where we don’t include the random token swapping step. The resulting objective simply replaces 15% of the tokens in the input with a mask token and the model is trained to reconstruct the original uncorrupted sequence. A similar masking objective was used by Song et al. (2019) where it was referred to as “MASS”, so we call this variant the “MASS-style” objective. Second, we were interested to see if it was possible to avoid predicting the entire uncorrupted text span since this requires self-attention over long sequences in the decoder. We consider two strategies to achieve this: First, instead of replacing each corrupted token with a mask token, we replace the entirety of each consecutive span of corrupted tokens with a unique mask token. Then, the target sequence becomes the concatenation of the “corrupted” spans, each prefixed by the mask token used to replace it in the input. This is the pre-training objective we use in our baseline, described in Section 3.1.4. Second, we also consider a variant where we simply drop the corrupted tokens from the input sequence completely and task the model with reconstructing the dropped tokens in order. Examples of these approaches are shown in the fifth and sixth rows of Table 3. 

An empirical comparison of the original BERT-style objective to these three alternatives is shown in Table 5. We find that in our setting, all of these variants perform similarly. The only exception was that dropping corrupted tokens completely produced a small improvement in the GLUE score thanks to a significantly higher score on CoLA (60 _._ 04, compared to our 

22 

Exploring the Limits of Transfer Learning

---

[referencia=887da5f02141c29f score=0.892]
### 3.2.4 Results 

The scores achieved by each of the architectures we compare are shown in Table 2. For all tasks, the encoder-decoder architecture with the denoising objective performed best. This variant has the highest parameter count (2 _P_ ) but the same computational cost as the _P_ -parameter decoder-only models. Surprisingly, we found that sharing parameters across the encoder and decoder performed nearly as well. In contrast, halving the number of layers in 

19 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.853]
> 12. `https://github.com/jcpeterson/openwebtext` 

> 13. `https://www.tensorflow.org/datasets/catalog/wikipedia` 

26 

Exploring the Limits of Transfer Learning 

|Data set|Size|GLUE|CNNDM|SQuAD|SGLUE|EnDe|EnFr|EnRo|
|---|---|---|---|---|---|---|---|---|
|⋆C4|745GB|83_._28|**19**_._**24**|80_._88|71_._36|**26**_._**98**|**39**_._**82**|**27**_._**65**|
|C4, unfltered|6.1TB|81_._46|19_._14|78_._78|68_._04|26_._55|39_._34|27_._21|
|RealNews-like|35GB|**83**_._**83**|**19**_._**23**|80_._39|72_._38|**26**_._**75**|**39**_._**90**|**27**_._**48**|
|WebText-like|17GB|**84**_._**03**|**19**_._**31**|**81**_._**42**|71_._40|**26**_._**80**|**39**_._**74**|**27**_._**59**|
|Wikipedia|16GB|81_._85|**19**_._**31**|81_._29|68_._01|**26**_._**94**|39_._69|**27**_._**67**|
|Wikipedia + TBC|20GB|83_._65|**19**_._**28**|**82**_._**08**|**73**_._**24**|**26**_._**77**|39_._63|**27**_._**57**|



Table 8: Performance resulting from pre-training on different data sets. The first four variants are based on our new C4 data set.

---

[referencia=887da5f02141c29f score=0.822]
Table 4: Performance of the three disparate pre-training objectives described in Section 3.3.1. 

|Objective|GLUE|CNNDM|SQuAD|SGLUE|EnDe|EnFr|EnRo|
|---|---|---|---|---|---|---|---|
|BERT-style (Devlin et al., 2018)|82_._96|19_._17|**80**_._**65**|69_._85|26_._78|**40**_._**03**|27_._41|
|MASS-style (Song et al., 2019)|82_._32|19_._16|80_._10|69_._28|26_._79|**39**_._**89**|27_._55|
|⋆Replace corrupted spans|83_._28|**19**_._**24**|**80**_._**88**|**71**_._**36**|**26**_._**98**|39_._82|**27**_._**65**|
|Drop corrupted tokens|**84**_._**44**|**19**_._**31**|**80**_._**52**|68_._67|**27**_._**07**|39_._76|**27**_._**82**|



Table 5: Comparison of variants of the BERT-style pre-training objective. In the first two variants, the model is trained to reconstruct the original uncorrupted text segment. In the latter two, the model only predicts the sequence of corrupted tokens.

---

[referencia=887da5f02141c29f score=0.803]
- **Objective** We swap out the i.i.d. denoising objective in our baseline for the span-corruption objective described in Section 3.3.4, which was loosely inspired by SpanBERT (Joshi et al., 2019). Specifically, we use a mean span length of 3 and corrupt 15% of the original sequence. We found that this objective produced marginally better performance (Table 7) while being slightly more computationally efficient due to shorter target sequence lengths. 

- **Longer training** Our baseline model uses a relatively small amount of pre-training (<sup>1</sup> ⁄4 as much as BERT (Devlin et al., 2018),<sup>1</sup> ⁄16 as much as XLNet (Yang et al., 2019),<sup>1</sup> ⁄64 as much as RoBERTa (Liu et al., 2019c), etc.). Fortunately, C4 is big enough that we can train for substantially longer without repeating data (which can be detrimental, as shown in Section 3.4.2). We found in Section 3.6 that additional pre-training can indeed be helpful, and that both increasing the batch size and increasing the number of training steps can confer this benefit. We therefore pre-train our models for 1 million steps on a batch size of 2<sup>11</sup> sequences of length 512, corresponding to a total of about 1 trillion pre-training tokens (about 32 _×_ as many as our baseline). In Section 3.4.1, we showed that pre-training on the RealNews-like, WebText-like, and Wikipedia + TBC data sets outperformed pre-training on C4 on a few downstream tasks. However, these data set variants are sufficiently small that they would be repeated hundreds of times over the course of pre-training on 1 trillion tokens. Since we showed in Section 3.4.2 that this repetition could be harmful, we opted instead to continue using the C4 data set.

---

[referencia=887da5f02141c29f score=0.711]
- Figure 4: Schematics of the Transformer architecture variants we consider. In this diagram, blocks represent elements of a sequence and lines represent attention visibility. Different colored groups of blocks indicate different Transformer layer stacks. Dark grey lines correspond to fully-visible masking and light grey lines correspond to causal masking. We use “.” to denote a special end-of-sequence token that represents the end of a prediction. The input and output sequences are represented as _x_ and _y_ respectively. Left: A standard encoder-decoder architecture uses fullyvisible masking in the encoder and the encoder-decoder attention, with causal masking in the decoder. Middle: A language model consists of a single Transformer layer stack and is fed the concatenation of the input and target, using a causal mask throughout. Right: Adding a prefix to a language model corresponds to allowing fully-visible masking over the input. 

obtain the model’s prediction for this example, the model would be fed the prefix “translate English to German: That is good. target:” and would be asked to generate the remainder of the sequence autoregressively. In this way, the model can predict an output sequence given an input, which satisfies the needs of text-to-text tasks. This approach was recently used to show that language models can learn to perform some text-to-text tasks without supervision (Radford et al., 2019). 

A fundamental and frequently cited drawback of using a language model in the textto-text setting is that causal masking forces the model’s representation of the _i_ th entry of the input sequence to only depend on the entries up until _i_ . To see why this is potentially disadvantageous, consider the text-to-text framework where the model is provided with a prefix/context before being asked to make predictions (e.g., the prefix is an English sentence and the model is asked to predict the German translation). With fully causal masking, the model’s representation of a prefix state can only depend on prior entries of the prefix. So, when predicting an entry of the output, the model will attend to a representation of the prefix that is unnecessarily limited. Similar arguments have been made against using a unidirectional recurrent neural network encoder in sequence-to-sequence models (Bahdanau et al., 2015). 

17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.705]
To provide a reasonable means of comparison, we consider multiple configurations for our encoder-decoder model. We will refer to the number of layers and parameters in a BERTBASE-sized layer stack as _L_ and _P_ , respectively. We will use _M_ to refer to the number of FLOPs required for an _L_ + _L_ -layer encoder-decoder model or _L_ -layer decoder-only model to process a given input-target pair. In total, we will compare: 

- An encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder. This model has 2 _P_ parameters and a computation cost of _M_ FLOPs. 

- An equivalent model, but with parameters shared across the encoder and decoder, resulting in _P_ parameters and an _M_ -FLOP computational cost. 

- An encoder-decoder model with _L/_ 2 layers each in the encoder and decoder, giving _P_ parameters and an _M/_ 2-FLOP cost. 

- A decoder-only language model with _L_ layers and _P_ parameters and a resulting computational cost of _M_ FLOPs. 

- A decoder-only prefix LM with the same architecture (and thus the same number of parameters and computational cost), but with fully-visible self-attention over the input.

---

[referencia=887da5f02141c29f score=0.702]
## **2. Setup** 

Before presenting the results from our large-scale empirical study, we review the necessary background topics required to understand our results, including the Transformer model architecture and the downstream tasks we evaluate on. We also introduce our approach for treating every problem as a text-to-text task and describe our “Colossal Clean Crawled Corpus” (C4), the Common Crawl-based data set we created as a source of unlabeled text data. We refer to our model and framework as the “ **T** ext- **t** o- **T** ext **T** ransfer **T** ransformer” (T5).

---

[referencia=887da5f02141c29f score=0.655]
### **4.1 Takeaways** 

**Text-to-text** Our text-to-text framework provides a simple way to train a single model on a wide variety of text tasks using the same loss function and decoding procedure. 

We showed how this approach can be successfully applied to generative tasks like abstractive summarization, classification tasks like natural language inference, and even regression tasks like STS-B. In spite of its simplicity, we found the text-totext framework obtained comparable performance to task-specific architectures and ultimately produced state-of-the-art results when combined with scale. 

**Architectures** While some work on transfer learning for NLP has considered architectural variants of the Transformer, we found the original encoder-decoder form worked best in our text-to-text framework. Though an encoder-decoder model uses twice as many parameters as “encoder-only” (e.g. BERT) or “decoder-only” (language model) architectures, it has a similar computational cost. We also showed that sharing the parameters in the encoder and decoder did not result in a substantial performance drop while halving the total parameter count. 

41 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.597]
#### Exploring the Limits of Transfer Learning 

Section 3.3 and we consider a model architecture that behaves similarly to BERT on text classification tasks in Section 3.2. 

After outlining our baseline experimental setup in the following subsection, we undertake an empirical comparison of model architectures (Section 3.2), unsupervised objectives 

(Section 3.3), pre-training data sets (Section 3.4), transfer approaches (Section 3.5), and scaling (Section 3.6). At the culmination of this section, we combine insights from our study with scale to obtain state-of-the-art results in many tasks we consider (Section 3.7). 

### **3.1 Baseline** 

Our goal for our baseline is to reflect typical, modern practice. We pre-train a standard Transformer (described in Section 2.1) using a simple denoising objective and then separately fine-tune on each of our downstream tasks. We describe the details of this experimental setup in the following subsections. 

### 3.1.1 Model 

For our model, we use a standard encoder-decoder Transformer as proposed by Vaswani et al.

---

[referencia=887da5f02141c29f score=0.587]
### 3.2.3 Objectives 

As an unsupervised objective, we will consider both a basic language modeling objective as well as our baseline denoising objective described in Section 3.1.4. We include the language modeling objective due to its historic use as a pre-training objective (Dai and Le, 2015; Ramachandran et al., 2016; Howard and Ruder, 2018; Radford et al., 2018; Peters et al., 2018) as well as its natural fit for the language model architectures we consider. For models that ingest a prefix before making predictions (the encoder-decoder model and prefix LM), we sample a span of text from our unlabeled data set and choose a random point to split it into prefix and target portions. For the standard language model, we train the model to predict the entire span from beginning to end. Our unsupervised denoising objective is designed for text-to-text models; to adapt it for use with a language model we concatenate the inputs and targets as described in Section 3.2.1.

---

[referencia=887da5f02141c29f score=0.559]
40 

Exploring the Limits of Transfer Learning 

Model GLUE CNNDM SQuAD SGLUE EnDe EnFr EnRo ⋆ Baseline 83 _._ 28 19 _._ 24 80 _._ 88 71 _._ 36 26 _._ 98 39 _._ 82 27 _._ 65 Baseline-1T 84 _._ 80 19 _._ 62 83 _._ 01 73 _._ 90 27 _._ 46 40 _._ 30 28 _._ 34 T5-Base **85** _._ **97 20** _._ **90 85** _._ **44 75** _._ **64 28** _._ **37 41** _._ **37 28** _._ **98** 

Table 15: Performance comparison of T5-Base to our baseline experimental setup used in the rest of the paper. Results are reported on the validation set. “Baseline-1T” refers to the performance achieved by pre-training the baseline model on 1 trillion tokens (the same number used for the T5 model variants) instead of 2<sup>35</sup> _≈_ 34B tokens (as was used for the baseline). 



<!-- Start of picture text -->
“non-scaling” changes we made when designing T5. As such, comparing the performance of<br>these two models gives us a concrete measurement of the impact of the insights from our<br>systematic study.<br>The performance of these three model configurations is shown in Table 15. Consistent<br>with the findings in Section 3.6, we find that additional pre-training improves performance<br>over the baseline. Nevertheless, T5-Base substantially outperforms baseline-1T on all<br>downstream tasks. This suggests that scale is not the only factor that contributes to T5’s<br>success. We hypothesize that the larger models benefit not only from their increased size<br>but also from these non-scaling factors.<br>4. Reflection<br>Having completed our systematic study, we wrap up by first recapping some of our most<br>significant findings. Our results provide some high-level perspective on which avenues of<br>research might be more or less promising. To conclude, we outline some topics we think<br>might provide effective approaches for further progressing the field.<br><!-- End of picture text -->

---

[referencia=887da5f02141c29f score=0.556]
### (2017). While many modern approaches to transfer learning for NLP use a Transformer 

architecture consisting of only a single “stack” (e.g. for language modeling (Radford et al., 2018; Dong et al., 2019) or classification and span prediction (Devlin et al., 2018; Yang et al., 2019)), we found that using a standard encoder-decoder structure achieved good results on both generative and classification tasks. We explore the performance of different model architectures in Section 3.2. 

Our baseline model is designed so that the encoder and decoder are each similar in size and configuration to a “BERTBASE” (Devlin et al., 2018) stack. Specifically, both the encoder and decoder consist of 12 blocks (each block comprising self-attention, optional encoder-decoder attention, and a feed-forward network). The feed-forward networks in each block consist of a dense layer with an output dimensionality of _d_ ff = 3072 followed by a ReLU nonlinearity and another dense layer. The “key” and “value” matrices of all attention mechanisms have an inner dimensionality of _d_ kv = 64 and all attention mechanisms have 12 heads. All other sub-layers and embeddings have a dimensionality of _d_ model = 768. In total, this results in a model with about 220 million parameters. This is roughly twice the number of parameters of BERTBASE since our baseline model contains two layer stacks instead of one. For regularization, we use a dropout probability of 0 _._ 1 everywhere dropout is applied in the model. 

3.1.2 Training 

As described in Section 2.4, all tasks are formulated as text-to-text tasks. This allows us to always train using standard maximum likelihood, i.e. using teacher forcing (Williams and Zipser, 1989) and a cross-entropy loss. For optimization, we use AdaFactor (Shazeer and 

Stern, 2018). At test time, we use greedy decoding (i.e. choosing the highest-probability logit at every timestep). 

We pre-train each model for 2<sup>19</sup> = 524 _,_ 288 steps on C4 before fine-tuning. We use a maximum sequence length of 512 and a batch size of 128 sequences. Whenever possible, 

11

---

[referencia=887da5f02141c29f score=0.536]
The decoder in an encoder-decoder Transformer is used to autoregressively produce an output sequence. That is, at each output timestep, a token is sampled from the model’s predicted distribution and the sample is fed back into the model to produce a prediction for the next output timestep, and so on. As such, a Transformer decoder (without an encoder) can be used as a language model (LM), i.e. a model trained solely for next-step prediction (Liu et al., 2018; Radford et al., 2018; Al-Rfou et al., 2019). This constitutes the second model structure we consider. A schematic of this architecture is shown in Figure 4, middle. In fact, early work on transfer learning for NLP used this architecture with a language modeling objective as a pre-training method (Radford et al., 2018). 

Language models are typically used for compression or sequence generation (Graves, 2013). However, they can also be used in the text-to-text framework simply by concatenating the inputs and targets. As an example, consider the case of English to German translation: If we have a training datapoint with input sentence “That is good.” and target “Das ist gut.”, we would simply train the model on next-step prediction over the concatenated input sequence “translate English to German: That is good. target: Das ist gut.” If we wanted to 

16 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
y1 y2 .<br>Language model Prefix LM<br>x2 x3 y1 y2 . x2 x3 y1 y2 .<br>x x x x x1 x2 x3 y1 y2 x1 x2 x3 y1 y2<br>1 2 3 4<br>Decoder<br>Encoder<br><!-- End of picture text -->

---

[referencia=887da5f02141c29f score=0.512]
- **Unsupervised objectives** Overall, we found that most “denoising” objectives, which train the model to reconstruct randomly corrupted text, performed similarly in the text-totext setup. As a result, we suggest using objectives that produce short target sequences so that unsupervised pre-training is more computationally efficient. 

- **Data sets** We introduced the “Colossal Clean Crawled Corpus” (C4), which comprises heuristically-cleaned text from the Common Crawl web dump. When comparing C4 to data sets that use additional filtering, we found that training on in-domain unlabeled data could boost performance in a few downstream tasks. However, constraining to a single domain typically results in a smaller data set. We separately showed that performance can degrade when an unlabeled data set is small enough that it is repeated many times over the course of pre-training. This motivates the use of a large and diverse data set like C4 for generic language understanding tasks. 

- **Training strategies** We found that the basic approach of updating all of a pre-trained model’s parameters during fine-tuning outperformed methods that are designed to update fewer parameters, although updating all parameters is most expensive. We also experimented with various approaches for training the model on multiple tasks at once, which in our text-to-text setting simply corresponds to mixing examples from different data sets when constructing batches. The primary concern in multi-task learning is setting the proportion of each task to train on. We ultimately did not find a strategy for setting mixing proportions that matched the performance of the basic approach of unsupervised pre-training followed by supervised fine-tuning. However, we found that fine-tuning after pre-training on a mixture of tasks produced comparable performance to unsupervised pre-training. 

- **Scaling** We compared various strategies for taking advantage of additional compute, including training the model on more data, training a larger model, and using an ensemble of models. We found each approach conferred a significant boost in performance, though training a smaller model on more data was often outperformed by training a larger model for fewer steps. We also showed an ensemble of models can provide substantially better results than a single model, which provides an orthogonal means of leveraging additional computation. Ensembling models that were fine-tuned from the same base pre-trained model performed worse than pre-training and fine-tuning all models completely separately, though fine-tune-only ensembling still substantially outperformed a single model.

---

[referencia=887da5f02141c29f score=0.473]
### 3.2.2 Comparing Different Model Structures 

In the interest of experimentally comparing these architectural variants, we would like each model we consider to be equivalent in some meaningful way. We might say that two models are equivalent if they either have the same number of parameters or they require roughly the same amount of computation to process a given (input-sequence, target-sequence) pair. Unfortunately, it is not possible to compare an encoder-decoder model to a language model architecture (comprising a single Transformer stack) according to both of these criteria at the same time. To see why, first note an encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder has approximately the same number of parameters as a language model with 2 _L_ layers. However, the same _L_ + _L_ encoder-decoder model will have approximately the same computational cost as a language model with _only L_ layers. This is a consequence of the fact that the _L_ layers in the language model must be applied to _both_ the input and output sequence, while the encoder is only applied to the input sequence and the decoder is only applied to the output sequence. Note that these equivalences are approximate—there are some extra parameters in the decoder due to the encoder-decoder attention and there are also some computational costs in the attention layers that are quadratic in the sequence lengths. In practice, however, we observed nearly identical step 

18 

Exploring the Limits of Transfer Learning 

times for _L_ -layer language models versus _L_ + _L_ -layer encoder-decoder models, suggesting a roughly equivalent computational cost. Further, for the model sizes we consider, the number of parameters in the encoder-decoder attention layers is about 10% of the total parameter count, so we make the simplifying assumption that an _L_ + _L_ -layer encoder-decoder model has the same number of parameters as an 2 _L_ -layer language model.

---

[referencia=887da5f02141c29f score=0.419]
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