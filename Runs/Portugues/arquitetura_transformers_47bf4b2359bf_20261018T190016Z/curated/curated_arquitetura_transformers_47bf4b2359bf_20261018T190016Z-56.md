[referencia=887da5f02141c29f score=0.668]
## **2. Setup** 

Before presenting the results from our large-scale empirical study, we review the necessary background topics required to understand our results, including the Transformer model architecture and the downstream tasks we evaluate on. We also introduce our approach for treating every problem as a text-to-text task and describe our “Colossal Clean Crawled Corpus” (C4), the Common Crawl-based data set we created as a source of unlabeled text data. We refer to our model and framework as the “ **T** ext- **t** o- **T** ext **T** ransfer **T** ransformer” (T5).

---

[referencia=887da5f02141c29f score=0.422]
> 2. `http://commoncrawl.org` 

2 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
"translate English to German: That is good."<br>"cola sentence: The  "Das ist gut."<br>course is jumping well."<br>"not acceptable"<br>"stsb sentence1: The rhino grazed<br>on the grass. sentence2: A rhino  T5<br>is grazing in a field." "3.8"<br>"summarize: state authorities  "six people hospitalized after<br>dispatched emergency crews tuesday to  a storm in attala county."<br>survey the damage after an onslaught<br>of severe weather in mississippi…"<br><!-- End of picture text -->

- Figure 1: A diagram of our text-to-text framework. Every task we consider—including translation, question answering, and classification—is cast as feeding our model text as input and training it to generate some target text. This allows us to use the same model, loss function, hyperparameters, etc. across our diverse set of tasks. It also provides a standard testbed for the methods included in our empirical survey. “T5” refers to our model, which we dub the “ **T** ext- **t** o- **T** ext **T** ransfer **T** ransformer”. 

summarization, and sentiment classification, to name a few. With this unified approach, we can compare the effectiveness of different transfer learning objectives, unlabeled data sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up models and data sets beyond what has previously been considered.

---

[referencia=887da5f02141c29f score=0.395]
||SQuAD|SQuAD<br>SuperGLUE<br>BoolQ<br>CB|CB|COPA|
|Model|EM|F1<br>Average<br>Accuracy<br>F1|Accuracy|Accuracy|
|Previous best|90_._1<sup>_a_</sup>|95_._5<sup>_a_</sup><br>84_._6<sup>_d_</sup><br>87_._1<sup>_d_</sup><br>90_._5<sup>_d_</sup>|95_._2<sup>_d_</sup>|90_._6<sup>_d_</sup>|
|T5-Small|79_._10|87_._24<br>63_._3<br>76_._4<br>56_._9|81_._6|46_._0|
|T5-Base|85_._44|92_._08<br>76_._2<br>81_._4<br>86_._2|94_._0|71_._2|
|T5-Large|86_._66|93_._79<br>82_._3<br>85_._4<br>91_._6|94_._8|83_._4|
|T5-3B|88_._53|94_._95<br>86_._4<br>89_._9<br>90_._3|94_._4|92_._0|
|T5-11B|**91**_._**26**|**96**_._**22**<br>**88**_._**9**<br>**91**_._**2**<br>**93**_._**9**|**96**_._**8**|**94**_._**8**|
||MultiRC|MultiRC<br>ReCoRD<br>ReCoRD<br>RTE|WiC|WSC|
|Model|F1a|EM<br>F1<br>Accuracy<br>Accuracy|Accuracy|Accuracy|

---

[referencia=887da5f02141c29f score=0.276]
37 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 

- **Beam search** All of our previous results were reported using greedy decoding. For tasks with long output sequences, we found improved performance from using beam search (Sutskever et al., 2014). Specifically, we use a beam width of 4 and a length penalty of _α_ = 0 _._ 6 (Wu et al., 2016) for the WMT translation and CNN/DM summarization tasks. 

- **Test set** Since this is our final set of experiments, we report results on the test set rather than the validation set. For CNN/Daily Mail, we use the standard test set distributed with the data set. For the WMT tasks, this corresponds to using `newstest2014` for English-German, `newstest2015` for English-French, and `newstest2016` for EnglishRomanian. For GLUE and SuperGLUE, we used the benchmark evaluation servers to compute official test set scores.<sup>15,16</sup> For SQuAD, evaluating on the test set requires running inference on a benchmark server. Unfortunately, the computational resources on this server are insufficient for obtaining predictions from our largest models. As a result, we instead continue to report performance on the SQuAD validation set. Fortunately, the model with the highest performance on the SQuAD test set also reported results on the validation set, so we can still compare to what is ostensibly the state-of-the-art. 

Apart from those changes mentioned above, we use the same training procedure and hyperparameters as our baseline (AdaFactor optimizer, inverse square root learning rate schedule for pre-training, constant learning rate for fine-tuning, dropout regularization, vocabulary, etc.). For reference, these details are described in Section 2. 

The results of this final set of experiments are shown in Table 14. Overall, we achieved state-of-the-art performance on 18 out of the 24 tasks we consider. As expected, our largest (11 billion parameter) model performed best among our model size variants across all tasks. Our T5-3B model variant did beat the previous state of the art in a few tasks, but scaling the model size to 11 billion parameters was the most important ingredient for achieving our best performance. We now analyze the results for each individual benchmark.

---

[referencia=887da5f02141c29f score=0.232]
17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 

This issue can be avoided in a Transformer-based language model simply by changing the masking pattern. Instead of using a causal mask, we use fully-visible masking during the prefix portion of the sequence. This masking pattern and a schematic of the resulting “prefix LM” (the third model structure we consider) are illustrated in the rightmost panels of Figures 3 and 4, respectively. In the English to German translation example mentioned above, fully-visible masking would be applied to the prefix “translate English to German: That is good. target:” and causal masking would be used during training for predicting the target “Das ist gut.” Using a prefix LM in the text-to-text framework was originally proposed by Liu et al. (2018). More recently, Dong et al. (2019) showed that this architecture is effective on a wide variety of text-to-text tasks. This architecture is similar to an encoder-decoder model with parameters shared across the encoder and decoder and with the encoder-decoder attention replaced with full attention across the input and target sequence. 

We note that when following our text-to-text framework, the prefix LM architecture closely resembles BERT (Devlin et al., 2018) for classification tasks. To see why, consider an example from the MNLI benchmark where the premise is “I hate pigeons.”, the hypothesis is “My feelings towards pigeons are filled with animosity.” and the correct label is “entailment”. To feed this example into a language model, we would transform it into the sequence “mnli premise: I hate pigeons. hypothesis: My feelings towards pigeons are filled with animosity. target: entailment”. In this case, the fully-visible prefix would correspond to the entire input sequence up to the word “target:”, which can be seen as being analogous to the “classification” token used in BERT. So, our model would have full visibility over the entire input, and then would be tasked with making a classification by outputting the word “entailment”. It is easy for the model to learn to output one of the valid class labels given the task prefix (“mnli” in this case). As such, the main difference between a prefix LM and the BERT architecture is that the classifier is simply integrated into the output layer of the Transformer decoder in the prefix LM.

---

[referencia=887da5f02141c29f score=0.213]
- Figure 4: Schematics of the Transformer architecture variants we consider. In this diagram, blocks represent elements of a sequence and lines represent attention visibility. Different colored groups of blocks indicate different Transformer layer stacks. Dark grey lines correspond to fully-visible masking and light grey lines correspond to causal masking. We use “.” to denote a special end-of-sequence token that represents the end of a prediction. The input and output sequences are represented as _x_ and _y_ respectively. Left: A standard encoder-decoder architecture uses fullyvisible masking in the encoder and the encoder-decoder attention, with causal masking in the decoder. Middle: A language model consists of a single Transformer layer stack and is fed the concatenation of the input and target, using a causal mask throughout. Right: Adding a prefix to a language model corresponds to allowing fully-visible masking over the input. 

obtain the model’s prediction for this example, the model would be fed the prefix “translate English to German: That is good. target:” and would be asked to generate the remainder of the sequence autoregressively. In this way, the model can predict an output sequence given an input, which satisfies the needs of text-to-text tasks. This approach was recently used to show that language models can learn to perform some text-to-text tasks without supervision (Radford et al., 2019). 

A fundamental and frequently cited drawback of using a language model in the textto-text setting is that causal masking forces the model’s representation of the _i_ th entry of the input sequence to only depend on the entries up until _i_ . To see why this is potentially disadvantageous, consider the text-to-text framework where the model is provided with a prefix/context before being asked to make predictions (e.g., the prefix is an English sentence and the model is asked to predict the German translation). With fully causal masking, the model’s representation of a prefix state can only depend on prior entries of the prefix. So, when predicting an entry of the output, the model will attend to a representation of the prefix that is unnecessarily limited. Similar arguments have been made against using a unidirectional recurrent neural network encoder in sequence-to-sequence models (Bahdanau et al., 2015). 

17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.202]
|Language model|LM|_P_|_M_|73_._78|17_._54|53_._81|56_._51|25_._23|34_._31|25_._38|
|Prefx LM|LM|_P_|_M_|79_._68|17_._84|76_._87|64_._86|26_._28|37_._51|26_._76|



Table 2: Performance of the different architectural variants described in Section 3.2.2. We use _P_ to refer to the number of parameters in a 12-layer base Transformer layer stack and _M_ to refer to the FLOPs required to process a sequence using the encoderdecoder model. We evaluate each architectural variant using a denoising objective (described in Section 3.1.4) and an autoregressive objective (as is commonly used to train language models). 

the encoder and decoder stacks significantly hurt performance. Concurrent work (Lan et al., 2019) also found that sharing parameters across Transformer blocks can be an effective means of lowering the total parameter count without sacrificing much performance. XLNet also bears some resemblance to the shared encoder-decoder approach with a denoising objective (Yang et al., 2019). We also note that the shared parameter encoder-decoder outperforms the decoder-only prefix LM, suggesting that the addition of an explicit encoder-decoder attention is beneficial. Finally, we confirm the widely-held conception that using a denoising objective always results in better downstream task performance compared to a language modeling objective. This observation has been previously made by Devlin et al. (2018), Voita et al. (2019), and Lample and Conneau (2019) among others. We undertake a more detailed exploration of unsupervised objectives in the following section.

---

[referencia=887da5f02141c29f score=0.189]
### **2.1 Model** 

Early results on transfer learning for NLP leveraged recurrent neural networks (Peters et al., 2018; Howard and Ruder, 2018), but it has recently become more common to use models based on the “Transformer” architecture (Vaswani et al., 2017). The Transformer was initially shown to be effective for machine translation, but it has subsequently been used in a wide variety of NLP settings (Radford et al., 2018; Devlin et al., 2018; McCann et al., 2018; Yu et al., 2018). Due to its increasing ubiquity, all of the models we study are based on the Transformer architecture. Apart from the details mentioned below and the variants we explore in Section 3.2, we do not deviate significantly from this architecture as originally proposed. Instead of providing a comprehensive definition of this model, we refer the interested reader to the original paper (Vaswani et al., 2017) or follow-up tutorials<sup>3,4</sup> for a more detailed introduction. 

The primary building block of the Transformer is self-attention (Cheng et al., 2016). Self-attention is a variant of attention (Graves, 2013; Bahdanau et al., 2015) that processes a sequence by replacing each element by a weighted average of the rest of the sequence. The original Transformer consisted of an encoder-decoder architecture and was intended for sequence-to-sequence (Sutskever et al., 2014; Kalchbrenner et al., 2014) tasks. It has recently also become common to use models consisting of a single Transformer layer stack, with varying forms of self-attention used to produce architectures appropriate for language modeling (Radford et al., 2018; Al-Rfou et al., 2019) or classification and span prediction tasks (Devlin et al., 2018; Yang et al., 2019). We empirically explore these architectural variants in Section 3.2.

---

[referencia=887da5f02141c29f score=0.177]
The decoder in an encoder-decoder Transformer is used to autoregressively produce an output sequence. That is, at each output timestep, a token is sampled from the model’s predicted distribution and the sample is fed back into the model to produce a prediction for the next output timestep, and so on. As such, a Transformer decoder (without an encoder) can be used as a language model (LM), i.e. a model trained solely for next-step prediction (Liu et al., 2018; Radford et al., 2018; Al-Rfou et al., 2019). This constitutes the second model structure we consider. A schematic of this architecture is shown in Figure 4, middle. In fact, early work on transfer learning for NLP used this architecture with a language modeling objective as a pre-training method (Radford et al., 2018). 

Language models are typically used for compression or sequence generation (Graves, 2013). However, they can also be used in the text-to-text framework simply by concatenating the inputs and targets. As an example, consider the case of English to German translation: If we have a training datapoint with input sentence “That is good.” and target “Das ist gut.”, we would simply train the model on next-step prediction over the concatenated input sequence “translate English to German: That is good. target: Das ist gut.” If we wanted to 

16 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
y1 y2 .<br>Language model Prefix LM<br>x2 x3 y1 y2 . x2 x3 y1 y2 .<br>x x x x x1 x2 x3 y1 y2 x1 x2 x3 y1 y2<br>1 2 3 4<br>Decoder<br>Encoder<br><!-- End of picture text -->

---

[referencia=887da5f02141c29f score=0.173]
### **4.1 Takeaways** 

- **Text-to-text** Our text-to-text framework provides a simple way to train a single model on a wide variety of text tasks using the same loss function and decoding procedure. We showed how this approach can be successfully applied to generative tasks like abstractive summarization, classification tasks like natural language inference, and even regression tasks like STS-B. In spite of its simplicity, we found the text-totext framework obtained comparable performance to task-specific architectures and ultimately produced state-of-the-art results when combined with scale. 

- **Architectures** While some work on transfer learning for NLP has considered architectural variants of the Transformer, we found the original encoder-decoder form worked best in our text-to-text framework. Though an encoder-decoder model uses twice as many parameters as “encoder-only” (e.g. BERT) or “decoder-only” (language model) architectures, it has a similar computational cost. We also showed that sharing the parameters in the encoder and decoder did not result in a substantial performance drop while halving the total parameter count. 

41 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.166]
- **Pushing the limits** We combined our above insights and trained substantially larger models (up to 11 billion parameters) to achieve state-of-the-art results across many of the benchmarks we considered. For unsupervised training, we extracted text from our C4 data set and applied a denoising objective that corrupts contiguous spans of tokens. We pre-trained on a multi-task mixture before fine-tuning on individual tasks. Overall, our models were trained on over 1 trillion tokens. In the interest of facilitating the replication, extension, and application of our results, we release our code, the C4 data set, and pre-trained model weights for each T5 variant.<sup>1</sup> 

42 

Exploring the Limits of Transfer Learning

---

[referencia=887da5f02141c29f score=0.163]
40 

Exploring the Limits of Transfer Learning 

|Model|GLUE|CNNDM|SQuAD|SGLUE|EnDe|EnFr|EnRo|
|---|---|---|---|---|---|---|---|
|⋆Baseline|83_._28|19_._24|80_._88|71_._36|26_._98|39_._82|27_._65|
|Baseline-1T|84_._80|19_._62|83_._01|73_._90|27_._46|40_._30|28_._34|
|T5-Base|**85**_._**97**|**20**_._**90**|**85**_._**44**|**75**_._**64**|**28**_._**37**|**41**_._**37**|**28**_._**98**|



Table 15: Performance comparison of T5-Base to our baseline experimental setup used in the rest of the paper. Results are reported on the validation set. “Baseline-1T” refers to the performance achieved by pre-training the baseline model on 1 trillion tokens (the same number used for the T5 model variants) instead of 2<sup>35</sup> _≈_ 34B tokens (as was used for the baseline). 

“non-scaling” changes we made when designing T5. As such, comparing the performance of these two models gives us a concrete measurement of the impact of the insights from our systematic study. 

The performance of these three model configurations is shown in Table 15. Consistent with the findings in Section 3.6, we find that additional pre-training improves performance over the baseline. Nevertheless, T5-Base substantially outperforms baseline-1T on all downstream tasks. This suggests that scale is not the only factor that contributes to T5’s success. We hypothesize that the larger models benefit not only from their increased size but also from these non-scaling factors.

---

[referencia=887da5f02141c29f score=0.142]
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

[referencia=887da5f02141c29f score=0.112]
### **3.1 Baseline** 

Our goal for our baseline is to reflect typical, modern practice. We pre-train a standard Transformer (described in Section 2.1) using a simple denoising objective and then separately fine-tune on each of our downstream tasks. We describe the details of this experimental setup in the following subsections. 

### 3.1.1 Model 

For our model, we use a standard encoder-decoder Transformer as proposed by Vaswani et al. (2017). While many modern approaches to transfer learning for NLP use a Transformer architecture consisting of only a single “stack” (e.g. for language modeling (Radford et al., 2018; Dong et al., 2019) or classification and span prediction (Devlin et al., 2018; Yang et al., 2019)), we found that using a standard encoder-decoder structure achieved good results on both generative and classification tasks. We explore the performance of different model architectures in Section 3.2. 

Our baseline model is designed so that the encoder and decoder are each similar in size and configuration to a “BERTBASE” (Devlin et al., 2018) stack. Specifically, both the encoder and decoder consist of 12 blocks (each block comprising self-attention, optional encoder-decoder attention, and a feed-forward network). The feed-forward networks in each block consist of a dense layer with an output dimensionality of _d_ ff = 3072 followed by a ReLU nonlinearity and another dense layer. The “key” and “value” matrices of all attention mechanisms have an inner dimensionality of _d_ kv = 64 and all attention mechanisms have 12 heads. All other sub-layers and embeddings have a dimensionality of _d_ model = 768. In total, this results in a model with about 220 million parameters. This is roughly twice the number of parameters of BERTBASE since our baseline model contains two layer stacks instead of one. For regularization, we use a dropout probability of 0 _._ 1 everywhere dropout is applied in the model.

---

[referencia=887da5f02141c29f score=0.107]
We emphasize that our goal is not to propose new methods but instead to provide a comprehensive perspective on where the field stands. As such, our work primarily comprises a survey, exploration, and empirical comparison of existing techniques. We also explore the limits of current approaches by scaling up the insights from our systematic study (training models up to 11 billion parameters) to obtain state-of-the-art results in many of the tasks we consider. In order to perform experiments at this scale, we introduce the “Colossal Clean Crawled Corpus” (C4), a data set consisting of hundreds of gigabytes of clean English text scraped from the web. Recognizing that the main utility of transfer learning is the possibility of leveraging pre-trained models in data-scarce settings, we release our code, data sets, and pre-trained models.<sup>1</sup> 

The remainder of the paper is structured as follows: In the following section, we discuss our base model and its implementation, our procedure for formulating every text processing problem as a text-to-text task, and the suite of tasks we consider. In Section 3, we present a large set of experiments that explore the field of transfer learning for NLP. At the end of the section (Section 3.7), we combine insights from our systematic study to obtain state-of-the-art results on a wide variety of benchmarks. Finally, we provide a summary of our results and wrap up with a look towards the future in Section 4. 

3 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.091]
Overall, our encoder-decoder Transformer implementation closely follows its originallyproposed form (Vaswani et al., 2017). First, an input sequence of tokens is mapped to a sequence of embeddings, which is then passed into the encoder. The encoder consists of a stack of “blocks”, each of which comprises two subcomponents: a self-attention layer followed by a small feed-forward network. Layer normalization (Ba et al., 2016) is applied to the input of each subcomponent. We use a simplified version of layer normalization where the activations are only rescaled and no additive bias is applied. After layer normalization, a residual skip connection (He et al., 2016) adds each subcomponent’s input to its output. Dropout (Srivastava et al., 2014) is applied within the feed-forward network, on the skip connection, on the attention weights, and at the input and output of the entire stack. The decoder is similar in structure to the encoder except that it includes a standard attention 

> 3. `http://nlp.seas.harvard.edu/2018/04/03/attention.html` 

> 4. `http://jalammar.github.io/illustrated-transformer/` 

4 

Exploring the Limits of Transfer Learning 

mechanism after each self-attention layer that attends to the output of the encoder. The self-attention mechanism in the decoder also uses a form of autoregressive or causal selfattention, which only allows the model to attend to past outputs. The output of the final decoder block is fed into a dense layer with a softmax output, whose weights are shared with the input embedding matrix. All attention mechanisms in the Transformer are split up into independent “heads” whose outputs are concatenated before being further processed.

---

[referencia=887da5f02141c29f score=0.078]
Finally, on CNN/Daily Mail we attain state-of-the-art performance, though only by a significant amount on the ROUGE-2-F score. It has been shown that improvements to the ROUGE score do not necessarily correspond to more coherent summaries (Paulus et al., 2017). Furthermore, while CNN/Daily Mail is posed as an abstractive summarization benchmark, purely extractive approaches have been shown to work well (Liu, 2019). It has also been argued that generative models trained with maximum likelihood are prone to producing repetitive summaries (See et al., 2017). Despite these potential issues, we find that our models do generate coherent and largely correct summaries. We provide some non-cherry-picked validation set examples in Appendix C. 

To achieve its strong results, T5 combines insights from our experimental study with unprecedented scale. Note that in Section 3.6 we found that scaling up the pre-training amount or size of our baseline model produced substantial gains. Given this, we were interested to measure how much the “non-scaling” changes we introduced into T5 contributed to its strong performance. We therefore carried out a final experiment where we compared the following three configurations: First, the standard baseline model, which was pre-trained on 2<sup>35</sup> _≈_ 34B tokens; second, the baseline trained instead for about 1 trillion tokens (i.e. the same amount of pre-training used for T5), which we refer to as “baseline-1T”; and third, T5-Base. Note that the differences between baseline-1T and T5-Base comprise the 

40 

Exploring the Limits of Transfer Learning

---

[referencia=887da5f02141c29f score=0.077]
Table 14: Performance of our T5 variants on every task we study. Small, Base, Large, 3B, and 11B refer to model configurations with 60 million, 220 million, 770 million, 3 billion, and 11 billion parameters, respectively. In the first row of each table, we report the state-of-the-art for the task (as of October 24th, 2019), with the superscript denoting its source with references listed at the end of this caption. All results are reported on the test set except for SQuAD where we use the validation set. _a_ (Lan et al., 2019) _b_ (Wang et al., 2019c) _c_ (Zhu et al., 2019) _d_ (Liu et al., 2019c)<sup>_e_</sup> (Edunov et al., 2018)<sup>_f_</sup> (Lample and Conneau, 2019)<sup>_g_</sup> (Dong et al., 2019) 

39 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 

was created over three years ago, and most recent improvements have only increased the state-of-the-art by a fraction of a percentage point. We note that when results are reported on the test set, they are typically based on an ensemble of models and/or leverage external data sets (e.g. TriviaQA (Joshi et al., 2017) or NewsQA (Trischler et al., 2016)) to augment the small SQuAD training set. Human performance on SQuAD is estimated at 82 _._ 30 and 91 _._ 22 for the Exact Match and F1 metric respectively (Rajpurkar et al., 2016), so it is not clear if further improvements on this benchmark are meaningful.

---

[referencia=887da5f02141c29f score=0.045]
### 3.2.1 Model Structures 

A major distinguishing factor for different architectures is the “mask” used by different attention mechanisms in the model. Recall that the self-attention operation in a Transformer takes a sequence as input and outputs a new sequence of the same length. Each entry of the output sequence is produced by computing a weighted average of entries of the input sequence. Specifically, let _yi_ refer to the _i_ th element of the output sequence and _xj_ refer to the _j_ th entry of the input sequence. _yi_ is computed as<sup>�</sup> _j_<sup>_wi,jxj_,where</sup><sup>_wi,j_isthescalar</sup> weight produced by the self-attention mechanism as a function of _xi_ and _xj_ . The attention mask is then used to zero out certain weights in order to constrain which entries of the input can be attended to at a given output timestep. Diagrams of the masks we will consider are shown in Figure 3. For example, the causal mask (Figure 3, middle) sets any _wi,j_ to zero if _j > i_ . 

The first model structure we consider is an an encoder-decoder Transformer, which consists of two layer stacks: The encoder, which is fed an input sequence, and the decoder, which produces a new output sequence. A schematic of this architectural variant is shown in the left panel of Figure 4. 

The encoder uses a “fully-visible” attention mask. Fully-visible masking allows a selfattention mechanism to attend to any entry of the input when producing each entry of its output. We visualize this masking pattern in Figure 3, left. This form of masking is appropriate when attending over a “prefix”, i.e. some context provided to the model that is later used when making predictions. BERT (Devlin et al., 2018) also uses a fully-visible masking pattern and appends a special “classification” token to the input. BERT’s output 

15 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 



<!-- Start of picture text -->

---

[referencia=887da5f02141c29f score=0.045]
### 3.5.1 Fine-tuning Methods 

It has been argued that fine-tuning all of the model’s parameters can lead to suboptimal results, particularly on low-resource tasks (Peters et al., 2019). Early results on transfer learning for text classification tasks advocated fine-tuning only the parameters of a small classifier that was fed sentence embeddings produced by a fixed pre-trained model (Subramanian et al., 2018; Kiros et al., 2015; Logeswaran and Lee, 2018; Hill et al., 2016; Conneau et al., 2017). This approach is less applicable to our encoder-decoder model because the entire decoder must be trained to output the target sequences for a given task. Instead, we focus on two alternative fine-tuning approaches that update only a subset of the parameters of our encoder-decoder model. 

The first, “adapter layers” (Houlsby et al., 2019; Bapna et al., 2019), is motivated by the goal of keeping most of the original model fixed while fine-tuning. Adapter layers are additional dense-ReLU-dense blocks that are added after each of the preexisting feed-forward networks in each block of the Transformer. These new feed-forward networks are designed so that their output dimensionality matches their input. This allows them to be inserted into the network with no additional changes to the structure or parameters. When finetuning, only the adapter layer and layer normalization parameters are updated. The main hyperparameter of this approach is the inner dimensionality _d_ of the feed-forward network, which changes the number of new parameters added to the model. We experiment with various values for _d_ . 

The second alternative fine-tuning method we consider is “gradual unfreezing” (Howard and Ruder, 2018). In gradual unfreezing, more and more of the model’s parameters are finetuned over time. Gradual unfreezing was originally applied to a language model architecture consisting of a single stack of layers. In this setting, at the start of fine-tuning only the 

29 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu