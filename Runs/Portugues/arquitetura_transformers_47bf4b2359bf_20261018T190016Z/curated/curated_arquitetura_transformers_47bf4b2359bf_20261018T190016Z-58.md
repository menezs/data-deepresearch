[referencia=887da5f02141c29f score=0.015]
In general, we find that multi-task training underperforms pre-training followed by fine-tuning on most tasks. The “equal” mixing strategy in particular results in dramatically degraded performance, which may be because the low-resource tasks have overfit, the highresource tasks have not seen enough data, or the model has not seen enough unlabeled data to learn general-purpose language capabilities. For examples-proportional mixing, we find that for most tasks there is a “sweet spot” for _K_ where the model obtains the best performance, and larger or smaller values of _K_ tend to result in worse performance. The exception (for the range of _K_ values we considered) was WMT English to French translation, which is such a high-resource task that it always benefits from a higher mixing proportion. Finally, we note that temperature-scaled mixing also provides a means of obtaining reasonable performance from most tasks, with _T_ = 2 performing the best in most cases. The finding that a multi-task model is outperformed by separate models trained on each individual task has previously been observed e.g. by Arivazhagan et al. (2019) and McCann et al. (2018), though it has been shown that the multi-task setup can confer benefits across very similar tasks Liu et al. (2019b); Ratner et al. (2018). In the following section, we explore ways to close the gap between multi-task training and the pre-train-then-fine-tune approach.

---

[referencia=887da5f02141c29f score=0.013]
in our empirical study. For a broader literature review, we recommend a recent survey by Ruder et al. (2019). 

We systematically study these contributions by taking a reasonable baseline (described 

in Section 3.1) and altering one aspect of the setup at a time. For example, in Section 3.3 we measure the performance of different unsupervised objectives while keeping the rest of our experimental pipeline fixed. This “coordinate ascent” approach might miss second-order 

effects (for example, some particular unsupervised objective may work best on a model larger than our baseline setting), but performing a combinatorial exploration of all of the factors in our study would be prohibitively expensive. In future work, we expect it could be fruitful to more thoroughly consider combinations of the approaches we study. 

Our goal is to compare a variety of different approaches on a diverse set of tasks while keeping as many factors fixed as possible. In order to satisfy this aim, in some cases we do not exactly replicate existing approaches. For example, “encoder-only” models like BERT (Devlin et al., 2018) are designed to produce a single prediction per input token or a single prediction for an entire input sequence. This makes them applicable for classification or span prediction tasks but not for generative tasks like translation or abstractive summarization. 

As such, none of the model architectures we consider are identical to BERT or consist of an encoder-only structure. Instead, we test approaches that are similar in spirit—for example, we consider an analogous objective to BERT’s “masked language modeling” objective in 

10 

Exploring the Limits of Transfer Learning 

Section 3.3 and we consider a model architecture that behaves similarly to BERT on text classification tasks in Section 3.2. 

After outlining our baseline experimental setup in the following subsection, we undertake an empirical comparison of model architectures (Section 3.2), unsupervised objectives (Section 3.3), pre-training data sets (Section 3.4), transfer approaches (Section 3.5), and scaling (Section 3.6). At the culmination of this section, we combine insights from our study with scale to obtain state-of-the-art results in many tasks we consider (Section 3.7).

---

[referencia=887da5f02141c29f score=0.009]
33 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 

|Training strategy|GLUE|CNNDM|SQuAD|SGLUE|EnDe|EnFr|EnRo|
|---|---|---|---|---|---|---|---|
|⋆Unsupervised pre-training + fne-tuning|**83**_._**28**|**19**_._**24**|**80**_._**88**|**71**_._**36**|**26**_._**98**|39_._82|27_._65|
|Multi-task training|81_._42|**19**_._**24**|79_._78|67_._30|25_._21|36_._30|27_._76|
|Multi-task pre-training + fne-tuning|**83**_._**11**|**19**_._**12**|**80**_._**26**|**71**_._**03**|**27**_._**08**|39_._80|**28**_._**07**|
|Leave-one-out multi-task training|81_._98|19_._05|79_._97|**71**_._**68**|**26**_._**93**|39_._79|**27**_._**87**|
|Supervised multi-task pre-training|79_._93|18_._96|77_._38|65_._36|26_._81|**40**_._**13**|**28**_._**04**|



Table 12: Comparison of unsupervised pre-training, multi-task learning, and various forms of multi-task pre-training. 

could suggest that the translation tasks benefit less from (English) pre-training, whereas unsupervised pre-training is an important factor in the other tasks.

---

[referencia=887da5f02141c29f score=0.005]
|2<br>⋆Enc/dec, denoising<br>2<br>Enc/dec, shared, denoising|83_._28<br>82_._81|53_._84<br>92_._68<br>55_._24<br>91_._86|92_._07<br>88_._92<br>88_._02<br>87_._94<br>88_._67<br>91_._56<br>84_._24<br>84_._57<br>90_._48<br>76_._28<br>41_._33<br>19_._24<br>38_._77<br>80_._88<br>88_._81<br>71_._36<br>76_._62<br>91_._22<br>91_._96<br>66_._20<br>66_._13<br>25_._78<br>69_._05<br>68_._16<br>75_._34<br>68_._04<br>78_._56<br>26_._98<br>91_._58<br>88_._24<br>87_._43<br>87_._58<br>88_._69<br>91_._60<br>83_._88<br>84_._01<br>90_._23<br>73_._65<br>41_._11<br>18_._78<br>38_._48<br>80_._63<br>88_._49<br>70_._73<br>77_._13<br>95_._04<br>96_._43<br>65_._00<br>66_._16<br>22_._98<br>68_._95<br>68_._09<br>70_._76<br>68_._18<br>75_._96<br>26_._72|39_._82<br>27_._65<br>39_._03<br>27_._46|

---

[referencia=887da5f02141c29f score=0.004]
8 

Exploring the Limits of Transfer Learning 

examples is shown in Figure 1. We provide full examples of preprocessed inputs for every task we studied in Appendix D. 

Our text-to-text framework follows previous work that casts multiple NLP tasks into a common format: McCann et al. (2018) propose the “Natural Language Decathlon”, a benchmark that uses a consistent question-answering format for a suite of ten NLP tasks. The Natural Language Decathlon also stipulates that all models must be multi-task, i.e. are able to simultaneously tackle all of the tasks at once. We instead allow for separately fine-tuning the model on each individual task and use short task prefixes instead of an explicit question-answer format. Radford et al. (2019) evaluate the zero-shot learning capabilities of language models by feeding some input to the model as a prefix and then autoregressively sampling an output. For example, automatic summarization is done by feeding in a document followed by the text “TL;DR:” (short for “too long, didn’t read”, a common abbreviation) and then the summary is predicted via autoregressive decoding. We mainly consider models that explicitly process an input with an encoder before generating an output with a separate decoder and we focus on transfer learning rather than zero-shot learning. Finally, Keskar et al. (2019b) unify many NLP tasks as “span extraction”, where text corresponding to possible output choices are appended to the input and the model is trained to extract the input span corresponding to the correct choice. In contrast, our framework also allows for generative tasks like machine translation and abstractive summarization where it is not possible to enumerate all possible output choices.

---

[referencia=887da5f02141c29f score=0.004]
This synergy has resulted in a great deal of recent work developing transfer learning methodology for NLP, which has produced a wide landscape of pre-training objectives (Howard and Ruder, 2018; Devlin et al., 2018; Yang et al., 2019; Dong et al., 2019), unlabeled data sets (Yang et al., 2019; Liu et al., 2019c; Zellers et al., 2019), benchmarks (Wang et al., 2019b, 2018; Conneau and Kiela, 2018), fine-tuning methods (Howard and Ruder, 2018; Houlsby et al., 2019; Peters et al., 2019), and more. The rapid rate of progress and diversity of techniques in this burgeoning field can make it difficult to compare different algorithms, tease apart the effects of new contributions, and understand the space of existing methods for transfer learning. Motivated by a need for more rigorous understanding, we leverage a unified approach to transfer learning that allows us to systematically study different approaches and push the current limits of the field. 

The basic idea underlying our work is to treat every text processing problem as a “text-to-text” problem, i.e. taking text as input and producing new text as output. This approach is inspired by previous unifying frameworks for NLP tasks, including casting all text problems as question answering (McCann et al., 2018), language modeling (Radford et al., 2019), or span extraction Keskar et al. (2019b) tasks. Crucially, the text-to-text framework allows us to directly apply the same model, objective, training procedure, and decoding process to every task we consider. We leverage this flexibility by evaluating performance on a wide variety of English-based NLP problems, including question answering, document 

> 2. `http://commoncrawl.org` 

2 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->

---

[referencia=887da5f02141c29f score=0.004]
|2<br>Language model, denoising<br>2<br>Prefx LM, denoising|74_._70<br>81_._82|24_._50<br>90_._60<br>49_._99<br>92_._43|86_._08<br>78_._92<br>85_._22<br>85_._42<br>85_._40<br>88_._99<br>76_._72<br>77_._05<br>86_._02<br>64_._62<br>39_._49<br>17_._93<br>36_._91<br>61_._14<br>71_._37<br>55_._02<br>65_._47<br>60_._08<br>71_._43<br>58_._00<br>43_._03<br>2_._94<br>53_._35<br>52_._31<br>53_._07<br>58_._62<br>63_._46<br>25_._09<br>91_._43<br>88_._24<br>87_._20<br>86_._98<br>88_._41<br>91_._39<br>82_._32<br>82_._93<br>88_._71<br>74_._01<br>40_._46<br>18_._61<br>37_._90<br>78_._94<br>87_._31<br>68_._11<br>75_._50<br>93_._37<br>91_._07<br>60_._00<br>63_._43<br>21_._20<br>65_._03<br>64_._11<br>71_._48<br>65_._67<br>73_._08<br>26_._43|35_._28<br>25_._86<br>37_._98<br>27_._39|

---

[referencia=887da5f02141c29f score=0.004]
# **Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer** 

**Colin Raffel**<sup>_∗_</sup> **Noam Shazeer**<sup>_∗_</sup> **Adam Roberts**<sup>_∗_</sup> **Katherine Lee**<sup>_∗_</sup> **Sharan Narang Michael Matena Yanqi Zhou Wei Li Peter J. Liu** 

craffel@gmail.com noam@google.com adarob@google.com katherinelee@google.com sharannarang@google.com mmatena@google.com yanqiz@google.com mweili@google.com peterjliu@google.com 

_Google, Mountain View, CA 94043, USA_ 

**Editor:** Ivan Titov 

## **Abstract** 

Transfer learning, where a model is first pre-trained on a data-rich task before being finetuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts all text-based language problems into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled data sets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new “Colossal Clean Crawled Corpus”, we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our data set, pre-trained models, and code.<sup>1</sup> 

**Keywords:** transfer learning, natural language processing, multi-task learning, attentionbased models, deep learning

---

[referencia=887da5f02141c29f score=0.004]
We compare the results of these approaches in Table 12. For comparison, we also include results for our baseline (pre-train then fine-tune) and for standard multi-task learning (without fine-tuning) on an examples-proportional mixture with _K_ = 2<sup>19</sup> . We find that fine-tuning after multi-task pre-training results in comparable performance to our baseline. This suggests that using fine-tuning after multi-task learning can help mitigate some of the trade-offs between different mixing rates described in Section 3.5.2. Interestingly, the performance of “leave-one-out” training was only slightly worse, suggesting that a model that was trained on a variety of tasks can still adapt to new tasks (i.e. multi-task pretraining might not result in a dramatic task interference). Finally, supervised multi-task pre-training performed significantly worse in every case except for the translation tasks. This 

33 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.003]
|-sye (evn e a., )<br><br>|_._<br>|_._<br>_._<br><br>|_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br>_._<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>|_._<br>_._<br><br>|
|4<br>Deshufing|73_._17|22_._82<br>87_._16|86_._88<br>81_._13<br>84_._03<br>83_._82<br>86_._38<br>89_._90<br>76_._30<br>76_._34<br>84_._18<br>58_._84<br>40_._75<br>18_._59<br>38_._10<br>67_._61<br>76_._76<br>58_._47<br>69_._17<br>63_._70<br>78_._57<br>56_._00<br>59_._85<br>12_._70<br>45_._52<br>44_._36<br>57_._04<br>64_._89<br>68_._27<br>26_._11|39_._30<br>25_._62|

---

[referencia=887da5f02141c29f score=0.003]
### **2.3 Downstream Tasks** 

Our goal in this paper is to measure general language learning abilities. As such, we study downstream performance on a diverse set of benchmarks, including machine translation, question answering, abstractive summarization, and text classification. Specifically, we measure performance on the GLUE and SuperGLUE text classification meta-benchmarks; CNN/Daily Mail abstractive summarization; SQuAD question answering; and WMT English to German, French, and Romanian translation. All data was sourced from TensorFlow Datasets.<sup>9</sup> 

GLUE (Wang et al., 2018) and SuperGLUE (Wang et al., 2019b) each comprise a collection of text classification tasks meant to test general language understanding abilities: 

- Sentence acceptability judgment (CoLA (Warstadt et al., 2018)) 

- Sentiment analysis (SST-2 (Socher et al., 2013)) 

- Paraphrasing/sentence similarity (MRPC (Dolan and Brockett, 2005), STS-B (Cer et al., 2017), QQP (Iyer et al., 2017)) 

- Natural language inference (MNLI (Williams et al., 2017), QNLI (Rajpurkar et al., 2016), RTE (Dagan et al., 2005), CB (De Marneff et al., 2019)) 

- Coreference resolution (WNLI and WSC (Levesque et al., 2012)) 

- Sentence completion (COPA (Roemmele et al., 2011)) 

- Word sense disambiguation (WIC (Pilehvar and Camacho-Collados, 2018)) 

- Question answering (MultiRC (Khashabi et al., 2018), ReCoRD (Zhang et al., 2018), BoolQ (Clark et al., 2019)) 

> 8. `https://www.tensorflow.org/datasets/catalog/c4` 

> 9. `https://www.tensorflow.org/datasets` 

7 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.003]
We emphasize that our goal is not to propose new methods but instead to provide a comprehensive perspective on where the field stands. As such, our work primarily comprises a survey, exploration, and empirical comparison of existing techniques. We also explore the limits of current approaches by scaling up the insights from our systematic study (training models up to 11 billion parameters) to obtain state-of-the-art results in many of the tasks we consider. In order to perform experiments at this scale, we introduce the “Colossal Clean Crawled Corpus” (C4), a data set consisting of hundreds of gigabytes of clean English text scraped from the web. Recognizing that the main utility of transfer learning is the possibility of leveraging pre-trained models in data-scarce settings, we release our code, data sets, and pre-trained models.<sup>1</sup> 

The remainder of the paper is structured as follows: In the following section, we discuss our base model and its implementation, our procedure for formulating every text processing problem as a text-to-text task, and the suite of tasks we consider. In Section 3, we present a large set of experiments that explore the field of transfer learning for NLP. At the end of the section (Section 3.7), we combine insights from our systematic study to obtain state-of-the-art results on a wide variety of benchmarks. Finally, we provide a summary of our results and wrap up with a look towards the future in Section 4. 

3 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.002]
### 3.3.1 Disparate High-Level Approaches 

To begin with, we compare three techniques that are inspired by commonly-used objectives but differ significantly in their approach. First, we include a basic “prefix language modeling” objective as was used in Section 3.2.3. This technique splits a span of text into two components, one to use as inputs to the encoder and the other to use as a target sequence to be predicted by the decoder. Second, we consider an objective inspired by the “masked language modeling” (MLM) objective used in BERT (Devlin et al., 2018). MLM takes a span of text and corrupts 15% of the tokens. 90% of the corrupted tokens are replaced with a special mask token and 10% are replaced with a random token. Since BERT is an encoder-only model, its goal during pre-training is to reconstruct masked tokens at the output of the encoder. In the encoder-decoder case, we simply use the entire uncorrupted sequence as the target. Note that this differs from our baseline objective, which uses only the corrupted tokens as targets; we compare these two approaches in Section 3.3.2. Finally, we also consider a basic deshuffling objective as used e.g. in (Liu et al., 2019a) where it was applied to a denoising sequential autoencoder. This approach takes a sequence of tokens, shuffles it, and then uses the original deshuffled sequence as a target. We provide examples of the inputs and targets for these three methods in the first three rows of Table 3. 

The performance of these three objectives is shown in Table 4. Overall, we find that the BERT-style objective performs best, though the prefix language modeling objective attains similar performance on the translation tasks. Indeed, the motivation for the BERT objective was to outperform language model-based pre-training. The deshuffling objective performs considerably worse than both prefix language modeling and the BERT-style objective. 

21 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.002]
> 2. `http://commoncrawl.org` 

2 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
"translate English to German: That is good."<br>"cola sentence: The  "Das ist gut."<br>course is jumping well."<br>"not acceptable"<br>"stsb sentence1: The rhino grazed<br>on the grass. sentence2: A rhino  T5<br>is grazing in a field." "3.8"<br>"summarize: state authorities  "six people hospitalized after<br>dispatched emergency crews tuesday to  a storm in attala county."<br>survey the damage after an onslaught<br>of severe weather in mississippi…"<br><!-- End of picture text -->

- Figure 1: A diagram of our text-to-text framework. Every task we consider—including translation, question answering, and classification—is cast as feeding our model text as input and training it to generate some target text. This allows us to use the same model, loss function, hyperparameters, etc. across our diverse set of tasks. It also provides a standard testbed for the methods included in our empirical survey. “T5” refers to our model, which we dub the “ **T** ext- **t** o- **T** ext **T** ransfer **T** ransformer”. 

summarization, and sentiment classification, to name a few. With this unified approach, we can compare the effectiveness of different transfer learning objectives, unlabeled data sets, and other factors, while exploring the limits of transfer learning for NLP by scaling up models and data sets beyond what has previously been considered.

---

[referencia=887da5f02141c29f score=0.001]
|12<br>Multi-task pre-training + fne-tuning<br>12<br>Leave-one-out multi-task training|83_._11<br>81_._98|51_._42<br>92_._66<br>48_._00<br>93_._23|91_._73<br>88_._73<br>88_._06<br>87_._70<br>88_._61<br>91_._61<br>84_._09<br>84_._31<br>91_._85<br>76_._53<br>41_._15<br>19_._12<br>38_._59<br>80_._26<br>88_._50<br>71_._03<br>79_._54<br>81_._69<br>87_._50<br>65_._00<br>70_._72<br>31_._48<br>65_._94<br>65_._03<br>81_._23<br>68_._18<br>73_._08<br>27_._08<br>91_._72<br>88_._24<br>87_._76<br>87_._32<br>88_._61<br>91_._44<br>84_._00<br>84_._11<br>90_._79<br>72_._20<br>41_._34<br>19_._05<br>38_._77<br>79_._97<br>88_._10<br>71_._68<br>78_._35<br>86_._76<br>89_._29<br>66_._00<br>68_._09<br>29_._49<br>66_._23<br>65_._27<br>79_._06<br>68_._65<br>78_._85<br>26_._93|39_._80<br>28_._07<br>39_._79<br>27_._87|

---

[referencia=887da5f02141c29f score=0.001]
The decoder in an encoder-decoder Transformer is used to autoregressively produce an output sequence. That is, at each output timestep, a token is sampled from the model’s predicted distribution and the sample is fed back into the model to produce a prediction for the next output timestep, and so on. As such, a Transformer decoder (without an encoder) can be used as a language model (LM), i.e. a model trained solely for next-step prediction (Liu et al., 2018; Radford et al., 2018; Al-Rfou et al., 2019). This constitutes the second model structure we consider. A schematic of this architecture is shown in Figure 4, middle. In fact, early work on transfer learning for NLP used this architecture with a language modeling objective as a pre-training method (Radford et al., 2018). 

Language models are typically used for compression or sequence generation (Graves, 2013). However, they can also be used in the text-to-text framework simply by concatenating the inputs and targets. As an example, consider the case of English to German translation: If we have a training datapoint with input sentence “That is good.” and target “Das ist gut.”, we would simply train the model on next-step prediction over the concatenated input sequence “translate English to German: That is good. target: Das ist gut.” If we wanted to 

16 

Exploring the Limits of Transfer Learning 



<!-- Start of picture text -->
y1 y2 .<br>Language model Prefix LM<br>x2 x3 y1 y2 . x2 x3 y1 y2 .<br>x x x x x1 x2 x3 y1 y2 x1 x2 x3 y1 y2<br>1 2 3 4<br>Decoder<br>Encoder<br><!-- End of picture text -->

---

[referencia=887da5f02141c29f score=0.001]
useful in downstream tasks. Preliminary work that applied the transfer learning paradigm of pre-training and fine-tuning all of the model’s parameters to NLP problems used a causal language modeling objective for pre-training (Dai and Le, 2015; Peters et al., 2018; Radford et al., 2018; Howard and Ruder, 2018). However, it has recently been shown that “denoising” objectives (Devlin et al., 2018; Taylor, 1953) (also called “masked language modeling”) produce better performance and as a result they have quickly become standard. In a denoising objective, the model is trained to predict missing or otherwise corrupted tokens in the input. Inspired by BERT’s “masked language modeling” objective and the “word dropout” regularization technique (Bowman et al., 2015), we design an objective that randomly samples and then drops out 15% of tokens in the input sequence. All consecutive spans of dropped-out tokens are replaced by a single sentinel token. Each sentinel token is assigned a token ID that is unique to the sequence. The sentinel IDs are special tokens which are added to our vocabulary and do not correspond to any wordpiece. The target then corresponds to all of the dropped-out spans of tokens, delimited by the same sentinel tokens used in the input sequence plus a final sentinel token to mark the end of the target sequence. Our choices to mask consecutive spans of tokens and only predict dropped-out tokens were made to reduce the computational cost of pre-training. We perform thorough investigation into pre-training objectives in Section 3.3. An example of the transformation resulting from applying this objective is shown in Figure 2. We empirically compare this objective to many other variants in Section 3.3.

---

[referencia=887da5f02141c29f score=0.001]
> 7. `https://pypi.org/project/langdetect/` 

6 

Exploring the Limits of Transfer Learning 

Crawl as a source of data for NLP: For example, Grave et al. (2018) also filter text using an automatic language detector and discard short lines and Smith et al. (2013); Grave et al. (2018) both perform line-level deduplication. However, we opted to create a new data set because prior data sets use a more limited set of filtering heuristics, are not publicly available, and/or are different in scope (e.g. are limited to News data (Zellers et al., 2019; Liu et al., 2019c), comprise only Creative Commons content (Habernal et al., 2016), or are focused on parallel training data for machine translation (Smith et al., 2013)). 

To assemble our base data set, we downloaded the web extracted text from April 2019 and applied the aforementioned filtering. This produces a collection of text that is not only orders of magnitude larger than most data sets used for pre-training (about 750 GB) but also comprises reasonably clean and natural English text. We dub this data set the “ **C** olossal **C** lean **C** rawled **C** orpus” (or C4 for short) and release it as part of TensorFlow Datasets.<sup>8</sup> We consider the impact of using various alternative versions of this data set in Section 3.4.

---

[referencia=887da5f02141c29f score=0.001]
- Figure 4: Schematics of the Transformer architecture variants we consider. In this diagram, blocks represent elements of a sequence and lines represent attention visibility. Different colored groups of blocks indicate different Transformer layer stacks. Dark grey lines correspond to fully-visible masking and light grey lines correspond to causal masking. We use “.” to denote a special end-of-sequence token that represents the end of a prediction. The input and output sequences are represented as _x_ and _y_ respectively. Left: A standard encoder-decoder architecture uses fullyvisible masking in the encoder and the encoder-decoder attention, with causal masking in the decoder. Middle: A language model consists of a single Transformer layer stack and is fed the concatenation of the input and target, using a causal mask throughout. Right: Adding a prefix to a language model corresponds to allowing fully-visible masking over the input. 

obtain the model’s prediction for this example, the model would be fed the prefix “translate English to German: That is good. target:” and would be asked to generate the remainder of the sequence autoregressively. In this way, the model can predict an output sequence given an input, which satisfies the needs of text-to-text tasks. This approach was recently used to show that language models can learn to perform some text-to-text tasks without supervision (Radford et al., 2019). 

A fundamental and frequently cited drawback of using a language model in the textto-text setting is that causal masking forces the model’s representation of the _i_ th entry of the input sequence to only depend on the entries up until _i_ . To see why this is potentially disadvantageous, consider the text-to-text framework where the model is provided with a prefix/context before being asked to make predictions (e.g., the prefix is an English sentence and the model is asked to predict the German translation). With fully causal masking, the model’s representation of a prefix state can only depend on prior entries of the prefix. So, when predicting an entry of the output, the model will attend to a representation of the prefix that is unnecessarily limited. Similar arguments have been made against using a unidirectional recurrent neural network encoder in sequence-to-sequence models (Bahdanau et al., 2015). 

17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.001]
### **3.3 Unsupervised Objectives** 

The choice of unsupervised objective is of central importance as it provides the mechanism through which the model gains general-purpose knowledge to apply to downstream tasks. This has led to the development of a wide variety of pre-training objectives (Dai and Le, 2015; Ramachandran et al., 2016; Radford et al., 2018; Devlin et al., 2018; Yang et al., 2019; Liu et al., 2019b; Wang et al., 2019a; Song et al., 2019; Dong et al., 2019; Joshi et al., 2019). In this section, we perform a procedural exploration of the space of unsupervised objectives. In many cases, we will not replicate an existing objective exactly—some will be modified to fit our text-to-text encoder-decoder framework and, in other cases, we will use objectives that combine concepts from multiple common approaches. 

Overall, all of our objectives ingest a sequence of token IDs corresponding to a tokenized span of text from our unlabeled text data set. The token sequence is processed to produce a (corrupted) input sequence and a corresponding target. Then, the model is trained as usual 

20 

Exploring the Limits of Transfer Learning 

|Objective|Inputs|Targets|
|---|---|---|
|Prefx language modeling|Thank you for inviting|me to your party last week .|
|BERT-style Devlin et al. (2018)|Thank you `<M> <M>` me to your party apple week .|_(original text)_|
|Deshufing|party me for your to . last fun you inviting week Thank|_(original text)_|
|MASS-style Song et al. (2019)|Thank you `<M> <M>` me to your party `<M>` week .|_(original text)_|
|I.i.d. noise, replace spans|Thank you `<X>` me to your party `<Y>` week .|`<X>` for inviting `<Y>` last `<Z>`|
|I.i.d. noise, drop tokens|Thank you me to your party week .|for inviting last|
|Random spans|Thank you `<X>` to `<Y>` week .|`<X>` for inviting me `<Y>` your party last `<Z>`|