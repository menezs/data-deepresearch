[referencia=c7a67a93fef201c0 score=0.995]
# **Effective Approaches to Attention-based Neural Machine Translation** 

**Minh-Thang Luong Hieu Pham Christopher D. Manning** Computer Science Department, Stanford University, Stanford, CA 94305 { `lmthang,hyhieu,manning` } `@stanford.edu` 

## **Abstract** 

An attentional mechanism has lately been used to improve neural machine translation (NMT) by selectively focusing on parts of the source sentence during translation. However, there has been little work exploring useful architectures for attention-based NMT. This paper examines two simple and effective classes of attentional mechanism: a _global_ approach which always attends to all source words and a _local_ one that only looks at a subset of source words at a time. We demonstrate the effectiveness of both approaches on the WMT translation tasks between English and German in both directions. With local attention, we achieve a significant gain of 5.0 BLEU points over non-attentional systems that already incorporate known techniques such as dropout. Our ensemble model using different attention architectures yields a new state-of-the-art result in the WMT’15 English to German translation task with 25.9 BLEU points, an improvement of 1.0 BLEU points over the existing best system backed by NMT and an n-gram reranker.<sup>1</sup>

---

[referencia=c7a67a93fef201c0 score=0.981]
### **4.2 English-German Results** 

We compare our NMT systems in the EnglishGerman task with various other systems. These include the winning system in WMT’14 (Buck et al., 2014), a phrase-based system whose language models were trained on a huge monolingual text, the Common Crawl corpus. For end-to-end NMT systems, to the best of our knowledge, (Jean et al., 2015) is the only work experimenting with this language pair and currently the SOTA system. We only present results for some of our attention models and will later analyze the rest in Section 5. 

As shown in Table 1, we achieve pro- 

gressive improvements when (a) reversing the source sentence, +1.3 BLEU, as proposed in (Sutskever et al., 2014) and (b) using dropout, +1.4 BLEU. On top of that, (c) the global attention approach gives a significant boost of +2.8 BLEU, making our model slightly better than the base attentional system of Bahdanau et al. (2015) (row _RNNSearch_ ). When (d) using the _inputfeeding_ approach, we seize another notable gain of +1.3 BLEU and outperform their system. The local attention model with predictive alignments (row _local-p_ ) proves to be even better, giving us a further improvement of +0.9 BLEU on top of the global attention model. It is interesting to observe the trend previously reported in (Luong et al., 2015) that perplexity strongly correlates with translation quality. In total, we achieve a significant gain of 5.0 BLEU points over the non-attentional baseline, which already includes known techniques such as source reversing and dropout. 

The unknown replacement technique proposed in (Luong et al., 2015; Jean et al., 2015) yields another nice gain of +1.9 BLEU, demonstrating that our attentional models do learn useful alignments for unknown works. Finally, by ensembling 8 different models of various settings, e.g., using different attention approaches, with and without dropout etc., we were able to achieve a _new SOTA_ result of 23.0 BLEU, outperforming the existing 

best system (Jean et al., 2015) by +1.4 BLEU.

---

[referencia=c7a67a93fef201c0 score=0.929]
In this work, we design, with simplicity and ef- 

fectiveness in mind, two novel types of attentionbased models: a _global_ approach in which all source words are attended and a _local_ one whereby only a subset of source words are considered at a time. The former approach resembles the model of (Bahdanau et al., 2015) but is simpler architecturally. The latter can be viewed as an interesting blend between the _hard_ and _soft_ attention models proposed in (Xu et al., 2015): it is computationally less expensive than the global model or the soft attention; at the same time, unlike the hard attention, the local attention is differentiable almost everywhere, making it easier to implement and train.<sup>2</sup> Besides, we also examine various alignment functions for our attention-based models. 

Experimentally, we demonstrate that both of our approaches are effective in the WMT translation tasks between English and German in both directions. Our attentional models yield a boost of up to 5.0 BLEU over non-attentional systems which already incorporate known techniques such as dropout. For English to German translation, we achieve new state-of-the-art (SOTA) results for both WMT’14 and WMT’15, outperforming previous SOTA systems, backed by NMT models and n-gram LM rerankers, by more than 1.0 BLEU. We conduct extensive analysis to evaluate our models in terms of learning, the ability to handle long sentences, choices of attentional architectures, alignment quality, and translation outputs.

---

[referencia=c7a67a93fef201c0 score=0.923]
best system (Jean et al., 2015) by +1.4 BLEU. 



|**System**|**BLEU**|
|---|---|
|Top –_NMT + 5-gram rerank_(Montreal)|24.9|
|Our ensemble 8 models + unk replace|**25.9**|





Table 2: **WMT’15 English-German results** – _NIST_ BLEU scores of the winning entry in WMT’15 and our best one on newstest2015. 

_Latest results in WMT’15_ – despite the fact that our models were trained on WMT’14 with slightly less data, we test them on newstest2015 to demonstrate that they can generalize well to different test sets. As shown in Table 2, our best system establishes a _new SOTA_ performance of 25.9 BLEU, outperforming the existing best system backed by NMT and a 5-gram LM reranker by +1.0 BLEU. 

### **4.3 German-English Results** 

We carry out a similar set of experiments for the WMT’15 translation task from German to English. While our systems have not yet matched the performance of the SOTA system, we nevertheless show the effectiveness of our approaches with large and progressive gains in terms of BLEU as illustrated in Table 3. The _attentional_ mechanism gives us +2.2 BLEU gain and on top of that, we obtain another boost of up to +1.0 BLEU from the _input-feeding_ approach. Using a better alignment function, the content-based _dot_ product one, together with _dropout_ yields another gain of +2.7 BLEU. Lastly, when applying the unknown word replacement technique, we seize an additional +2.1 BLEU, demonstrating the usefulness of attention in aligning rare words.

---

[referencia=c7a67a93fef201c0 score=0.878]
## **6 Conclusion** 

In this paper, we propose two simple and effective attentional mechanisms for neural machine translation: the _global_ approach which always looks at all source positions and the _local_ one that only attends to a subset of source positions at a time. We test the effectiveness of our models in the WMT translation tasks between English and German in both directions. Our local attention yields large gains of up to 5.0 BLEU over non-attentional 

models which already incorporate known techniques such as dropout. For the English to German translation direction, our ensemble model has established new state-of-the-art results for both WMT’14 and WMT’15, outperforming existing best systems, backed by NMT models and n-gram LM rerankers, by more than 1.0 BLEU. 

We have compared various alignment functions and shed light on which functions are best for which attentional models. Our analysis shows that attention-based NMT models are superior to nonattentional ones in many cases, for example in translating names and handling long sentences.

---

[referencia=c7a67a93fef201c0 score=0.697]
### **5.1 Learning curves** 

We compare models built on top of one another as listed in Table 1. It is pleasant to observe in Figure 5 a clear separation between non-attentional and attentional models. The input-feeding approach and the local attention model also demonstrate their abilities in driving the test costs lower. The non-attentional model with dropout (the blue 





|**System**|**Ppl.**|**BLEU**|
|---|---|---|
|_WMT’15 systems_|||
|SOTA –_phrase-based_ (Edinburgh)||**29.2**|
|NMT + 5-gram rerank (MILA)||27.6|
|_Our NMT systems_|||
|Base (reverse)|14.3|16.9|
|+ global (_location_)|12.7|19.1 (_+2.2_)|
|+ global (_location_) + feed|10.9|20.1 (_+1.0_)|
|+ global (_dot_) + drop + feed|97|22.8 (_+2.7_)|
|+ global (_dot_) + drop + feed + unk|.|24.9 (_+2.1_)|













Table 3: **WMT’15 German-English results** – performances of various systems (similar to Table 1). The _base_ system already includes source reversing on which we add _global_ attention, _drop_ out, input _feed_ ing, and _unk_ replacement. 



<!-- Start of picture text -->
6 basic<br>basic+reverse<br>5 basic+reverse+dropout<br>basic+reverse+dropout+globalAttn<br>basic+reverse+dropout+globalAttn+feedInput<br>4 basic+reverse+dropout+pLocalAttn+feedInput<br>3<br>2<br>0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8<br>Mini−batches 5<br>x 10<br>Test cost<br><!-- End of picture text -->

Figure 5: **Learning curves** – test cost (ln perplexity) on newstest2014 for English-German NMTs as training progresses.

---

[referencia=c7a67a93fef201c0 score=0.692]
## **4 Experiments** 

We evaluate the effectiveness of our models on the WMT translation tasks between English and German in both directions. newstest2013 (3000 sentences) is used as a development set to select our hyperparameters. Translation performances are reported in case-sensitive BLEU (Papineni et al., 2002) on newstest2014 (2737 sentences) and newstest2015 (2169 sentences). Following (Luong et al., 2015), we report translation quality using two types of BLEU: (a) _tokenized_<sup>12</sup> BLEU to be comparable with existing NMT work and (b) _NIST_<sup>13</sup> BLEU to be comparable with WMT results.

---

[referencia=c7a67a93fef201c0 score=0.630]
### **4.1 Training Details** 

All our models are trained on the WMT’14 training data consisting of 4.5M sentences pairs (116M English words, 110M German words). Similar to (Jean et al., 2015), we limit our vocabularies to be the top 50K most frequent words for both languages. Words not in these shortlisted vocabularies are converted into a universal token < `unk` >. 

When training our NMT systems, following (Bahdanau et al., 2015; Jean et al., 2015), we filter out sentence pairs whose lengths exceed 50 words and shuffle mini-batches as we proceed. Our stacking LSTM models have 4 layers, each with 1000 cells, and 1000-dimensional embeddings. We follow (Sutskever et al., 2014; Luong et al., 2015) in training NMT with similar settings: (a) our parameters are uniformly initialized in [−0.1, 0.1], (b) we train for 10 epochs us- 



> 12All texts are tokenized with `tokenizer.perl` and BLEU scores are computed with `multi-bleu.perl` . 

> 13With the `mteval-v13a` script as per WMT guideline.

---

[referencia=c7a67a93fef201c0 score=0.562]
> 13With the `mteval-v13a` script as per WMT guideline. 





|**System**|**Ppl**|**BLEU**|
|---|---|---|
|Winning WMT’14 system –_phrase-based + large LM_(Buck et al., 2014)||20.7|
|_Existing NMT systems_|||
|RNNsearch (Jean et al., 2015)||16.5|
|RNNsearch + unk replace (Jean et al., 2015)||19.0|
|RNNsearch + unk replace + large vocab +_ensemble_8 models (Jean et al., 2015)||**21.6**|
|_Our NMT systems_|||
|Base|10.6|11.3|
|Base + reverse|9.9|12.6 (_+1.3_)|
|Base + reverse + dropout<br>Base + reverse + dropout + global attention (_location_)|8.1<br>7.3|14.0 (_+1.4_)<br>16.8 (_+2.8_)|
|Base + reverse + dropout + global attention (_location_) + feed input|6.4|18.1 (_+1.3_)|
|Base + reverse + dropout + local-p attention (_general_) + feed input|59|19.0 (_+0.9_)|
|Base + reverse + dropout + local-p attention (_general_) + feed input + unk replace<br>_Ensemble_8 models + unk replace|.|20.9 (_+1.9_)<br>**23.0 (**_+2.1_**)**|

















Table 1: **WMT’14 English-German results** – shown are the perplexities (ppl) and the _tokenized_ BLEU scores of various systems on newstest2014. We highlight the **best** system in bold and give _progressive_ improvements in italic between consecutive systems. _local-p_ referes to the local attention with predictive alignments. We indicate for each attention model the alignment score function used in pararentheses.

---

[referencia=c7a67a93fef201c0 score=0.354]
## **1 Introduction** 

Neural Machine Translation (NMT) achieved state-of-the-art performances in large-scale translation tasks such as from English to French (Luong et al., 2015) and English to German (Jean et al., 2015). NMT is appealing since it requires minimal domain knowledge and is conceptually simple. The model by Luong et al. (2015) reads through all the source words until the end-ofsentence symbol < `eos` > is reached. It then starts 



> 1All our code and models are publicly available at `http://nlp.stanford.edu/projects/nmt` . 



<!-- Start of picture text -->
X Y Z <eos><br>A B C D <eos> X Y Z<br><!-- End of picture text -->

Figure 1: **Neural machine translation** – a stacking recurrent architecture for translating a source sequence `A B C D` into a target sequence `X Y Z` . Here, < `eos` > marks the end of a sentence. 

emitting one target word at a time, as illustrated in Figure 1. NMT is often a large neural network that is trained in an end-to-end fashion and has the ability to generalize well to very long word sequences. This means the model does not have to explicitly store gigantic phrase tables and language models as in the case of standard MT; hence, NMT has a small memory footprint. Lastly, implementing NMT decoders is easy unlike the highly intricate decoders in standard MT (Koehn et al., 2003). 

In parallel, the concept of “attention” has gained popularity recently in training neural networks, allowing models to learn alignments between different modalities, e.g., between image objects and agent actions in the dynamic control problem (Mnih et al., 2014), between speech frames and text in the speech recognition task ( **?** ), or between visual features of a picture and its text description in the image caption generation task (Xu et al., 2015). In the context of NMT, Bahdanau et al. (2015) has successfully applied such attentional mechanism to jointly translate and align words. To the best of our knowledge, there has not been any other work exploring the use of attention-based architectures for NMT. 

In this work, we design, with simplicity and ef-

---

[referencia=c7a67a93fef201c0 score=0.205]
Figure 5: **Learning curves** – test cost (ln perplexity) on newstest2014 for English-German NMTs as training progresses. 

+ curve) learns slower than other non-dropout models, but as time goes by, it becomes more robust in terms of minimizing test errors. 

### **5.2 Effects of Translating Long Sentences** 

We follow (Bahdanau et al., 2015) to group sentences of similar lengths together and compute a BLEU score per group. Figure 6 shows that our attentional models are more effective than the non-attentional one in handling long sentences: the quality does not degrade as sentences become longer. Our best model (the blue + curve) outperforms all other systems in all length buckets.

---

[referencia=c7a67a93fef201c0 score=0.133]
### **5.4 Alignment Quality** 

A by-product of attentional models are word alignments. While (Bahdanau et al., 2015) visualized 



> 14There is a subtle difference in how we retrieve alignments for the different alignment functions. At time step t in which we receive yt−1 as input and then compute ht, at, ct, and h<sup>˜</sup> t before predicting yt, the alignment vector at is used as alignment weights for (a) the predicted word yt in the _location-based_ alignment functions and (b) the input word yt−1 in the _content-based_ functions. 

> 15With _concat_ , the perplexities achieved by different models are 6.7 (global), 7.1 (local-m), and 7.1 (local-p). Such high perplexities could be due to the fact that we simplify the matrix Wa to set the part that corresponds to h<sup>¯</sup> s to identity. 

|**Method**|**AER**|
|---|---|
|global (location)|0.39|
|local-m (general)|0.34|
|local-p (general)|0.36|
|ensemble|0.34|
|Berkeley Aligner|0.32|







Table 6: **AER scores** – results of various models on the RWTH English-German alignment data. 

alignments for some sample sentences and observed gains in translation quality as an indication of a working attention model, no work has assessed the alignments learned as a whole. In contrast, we set out to evaluate the alignment quality using the alignment error rate (AER) metric. 

Given the gold alignment data provided by RWTH for 508 English-German Europarl sentences, we “force” decode our attentional models to produce translations that match the references. We extract only one-to-one alignments by selecting the source word with the highest alignment weight per target word. Nevertheless, as shown in Table 6, we were able to achieve AER scores comparable to the one-to-many alignments obtained by the Berkeley aligner (Liang et al., 2006).<sup>16</sup>

---

[referencia=c7a67a93fef201c0 score=0.131]
|_best_|In an interview , however , Bloom said that he and_Kerr_still love .|
|base|However , in an interview , Bloom said that he and**Tina**were still<unk>.|
|src|Wegen der von Berlin und der Europ¨aischen Zentralbank verh¨angten strengen Sparpolitik in<br>Verbindung mit der Zwangsjacke , in die die jeweilige nationale Wirtschaft durch das Festhal-<br>ten an der gemeinsamen W¨ahrung gen¨otigt wird , sind viele Menschen der Ansicht , das Projekt<br>Europa sei zu weit gegangen|
|ref|The _austerity imposed by Berlin and the European Central Bank , coupled with the straitjacket_<br>imposed on national economies through adherence to the common currency , has led many people<br>to think Project Europe has gone too far .|
|_best_|Because of the strict _austerity measures imposed by Berlin and the European Central Bank in_<br>_connection with the straitjacket_ in which the respective national economy is forced to adhere to<br>the common currency , many people believe that the European project has gone too far .|
|base|Because of the pressure**imposed by the European Central Bank and the Federal Central Bank**<br>**with the strict austerity** imposed on the national economy in the face of the single currency ,<br>many people believe that the European project has gone too far .|





















Table 5: **Sample translations** – for each example, we show the source ( _src_ ), the human translation ( _ref_ ), the translation from our best model ( _best_ ), and the translation of a non-attentional model ( _base_ ). We italicize some _correct_ translation segments and highlight a few **wrong** ones in bold. 

bar”, meaning “not compatible”.<sup>17</sup> The attentional model also demonstrates its superiority in translating long sentences as in the last example.

---

[referencia=c7a67a93fef201c0 score=0.126]
In more detail, one can parameterize the probability of decoding each word yj as: 



with g being the transformation function that outputs a vocabulary-sized vector.<sup>5</sup> Here, hj is the RNN hidden unit, abstractly computed as: 



where f computes the current hidden state given the previous hidden state and can be either a vanilla RNN unit, a GRU, or an LSTM unit. In (Kalchbrenner and Blunsom, 2013; Sutskever et al., 2014; Cho et al., 2014; Luong et al., 2015), the source representation s is only used once to initialize the decoder hidden state. On the other hand, in (Bahdanau et al., 2015; Jean et al., 2015) and this work, s, in fact, implies a set of source hidden states which are consulted throughout the entire course of the translation process. Such an approach is referred to as an attention mechanism, which we will discuss next. 

In this work, following (Sutskever et al., 2014; Luong et al., 2015), we use the stacking LSTM architecture for our NMT systems, as illustrated 



> 4They all used a single RNN layer except for the latter two works which utilized a bidirectional RNN for the encoder. 

> 5 One can provide g with other inputs such as the currently predicted word yj as in (Bahdanau et al., 2015). 

in Figure 1. We use the LSTM unit in (Zaremba et al., 2015). Our training objective is formulated as follows: 



with D being our parallel training corpus.

---

[referencia=c7a67a93fef201c0 score=0.102]
### **5.3 Choices of Attentional Architectures** 

We examine different attention models ( _global, local-m, local-p_ ) and different alignment functions ( _location, dot, general, concat_ ) as described in Section 3. Due to limited resources, we cannot run all the possible combinations. However, results in Table 4 do give us some idea about different choices. The _location-based_ function does 



<!-- Start of picture text -->
25<br>20<br>ours, no attn (BLEU 13.9)<br>o urs, local−p attn (BLEU 20.9)<br>o urs, best system (BLEU 23.0)<br>1 5 WMT’14 best (BLEU 20.7)<br>Jeans et al., 2015 (BLEU 21.6)<br>10<br>10 20 30 40 50 60 70<br>Sent Lengths<br>BLEU�����<br><!-- End of picture text -->

Figure 6: **Length Analysis** – translation qualities of different systems as sentences become longer. 





|**System**|**Ppl**|**B**<br>|**LEU**<br>|
|---|---|---|---|
|||Before|After unk|
|global (location)|6.4|18.1|19.3 (+1.2)|
|global (dot)|6.1|18.6|20.5 (+1.9)|
|global (general)|6.1|17.3|19.1 (+1.8)|
|local-m (dot)|>7.0|x|x|
|local-m (general)|6.2|18.6|20.4 (+1.8)|
|local-p (dot)|6.6|18.0|19.6 (+1.9)|
|local-p (general)|**5.9**|**19**|**20.9 (+1.9)**|





Table 4: **Attentional Architectures** – performances of different attentional models. We trained two local-m (dot) models; both have ppl > 7.0.

---

[referencia=c7a67a93fef201c0 score=0.062]
### **3.1 Global Attention** 

The idea of a global attentional model is to consider all the hidden states of the encoder when deriving the context vector ct. In this model type, a variable-length alignment vector at, whose size equals the number of time steps on the source side, is derived by comparing the current target hidden state ht with each source hidden state h<sup>¯</sup> s: 





<!-- Start of picture text -->
yt<br>h˜ t<br>Attention Layer<br>Context vector<br>ct<br>Global align weights<br>at<br>h¯ s<br>ht<br><!-- End of picture text -->

Figure 2: **Global attentional model** – at each time step t, the model infers a _variable-length_ alignment weight vector at based on the current target state ht and all source states h<sup>¯</sup> s. A global context vector ct is then computed as the weighted average, according to at, over all the source states. 

Here, score is referred as a _content-based_ function for which we consider three different alternatives: 



Besides, in our early attempts to build attentionbased models, we use a _location-based_ function in which the alignment scores are computed from solely the target hidden state ht as follows: 



Given the alignment vector as weights, the context vector ct is computed as the weighted average over all the source hidden states.<sup>6</sup> 

_Comparison to (Bahdanau et al., 2015)_ – While our global attention approach is similar in spirit to the model proposed by Bahdanau et al. (2015), there are several key differences which reflect how we have both simplified and generalized from the original model. First, we simply use hidden states at the top LSTM layers in both the encoder and decoder as illustrated in Figure 2. Bahdanau et al. (2015), on the other hand, use the concatenation of the forward and backward source hidden states in the bi-directional encoder 



6 Eq. (8) implies that all alignment vectors at are of the same length. For short sentences, we only use the top part of at and for long sentences, we ignore words near the end. 



<!-- Start of picture text -->
yt<br>h˜ t<br>Attention Layer<br>Context vector<br>ct<br>Aligned position<br>pt<br>h¯ s at Local weights<br>ht<br><!-- End of picture text -->

---

[referencia=c7a67a93fef201c0 score=0.056]
### **3.3 Input-feeding Approach** 

In our proposed global and local approaches, the attentional decisions are made independently, which is suboptimal. Whereas, in standard MT, a _coverage_ set is often maintained during the translation process to keep track of which source words have been translated. Likewise, in attentional NMTs, alignment decisions should be made jointly taking into account past alignment information. To address that, we propose an _inputfeeding_ approach in which attentional vectors h<sup>˜</sup> t are concatenated with inputs at the next time steps as illustrated in Figure 4.<sup>11</sup> The effects of having such connections are two-fold: (a) we hope to make the model fully aware of previous alignment choices and (b) we create a very deep network spanning both horizontally and vertically. 

_Comparison to other work_ – Bahdanau et al. (2015) use context vectors, similar to our ct, in building subsequent hidden states, which can also achieve the “coverage” effect. However, there has not been any analysis of whether such connections are useful as done 



> 11If n is the number of LSTM cells, the input size of the first LSTM layer is 2n; those of subsequent layers are n. 

in this work. Also, our approach is more general; as illustrated in Figure 4, it can be applied to general stacking recurrent architectures, including non-attentional models. 

Xu et al. (2015) propose a _doubly attentional_ approach with an additional constraint added to the training objective to make sure the model pays equal attention to all parts of the image during the caption generation process. Such a constraint can also be useful to capture the coverage set effect in NMT that we mentioned earlier. However, we chose to use the input-feeding approach since it provides flexibility for the model to decide on any attentional constraints it deems suitable.

---

[referencia=c7a67a93fef201c0 score=0.052]
## **2 Neural Machine Translation** 

A neural machine translation system is a neural network that directly models the conditional probability p(y|x) of translating a source sentence, x1, . . . , xn, to a target sentence, y1, . . . , ym.<sup>3</sup> A basic form of NMT consists of two components: (a) an _encoder_ which computes a representation s for each source sentence and (b) a _decoder_ which generates one target word at a time and hence decomposes the conditional probability as: 



A natural choice to model such a decomposition in the decoder is to use a 



> 2There is a recent work by Gregor et al. (2015), which is very similar to our local attention and applied to the image generation task. However, as we detail later, our model is much simpler and can achieve good performance for NMT. 

> 3All sentences are assumed to terminate with a special “end-of-sentence” token < `eos` >. 

recurrent neural network (RNN) architecture, which most of the recent NMT work such as (Kalchbrenner and Blunsom, 2013; Sutskever et al., 2014; Cho et al., 2014; Bahdanau et al., 2015; Luong et al., 2015; Jean et al., 2015) have in common. They, however, differ in terms of which RNN architectures are used for the decoder and how the encoder computes the source sentence representation s. 

Kalchbrenner and Blunsom (2013) used an RNN with the standard hidden unit for the decoder and a convolutional neural network for encoding the source sentence representation. On the other hand, both Sutskever et al. (2014) and Luong et al. (2015) stacked multiple layers of an RNN with a Long Short-Term Memory (LSTM) hidden unit for both the encoder and the decoder. Cho et al. (2014), Bahdanau et al. (2015), and Jean et al. (2015) all adopted a different version of the RNN with an LSTM-inspired hidden unit, the gated recurrent unit (GRU), for both components.<sup>4</sup> 

In more detail, one can parameterize the probability of decoding each word yj as:

---

[referencia=c7a67a93fef201c0 score=0.043]
<!-- Start of picture text -->
yt<br>h˜ t<br>Attention Layer<br>Context vector<br>ct<br>Aligned position<br>pt<br>h¯ s at Local weights<br>ht<br><!-- End of picture text -->

Figure 3: **Local attention model** predicts a single aligned position pt for the current target word. A window centered around the source position pt is then used to compute a context vector ct, a weighted average of the source hidden states in the window. The weights at are inferred from the current target state ht and those source states h<sup>¯</sup> s in the window. 

and target hidden states in their non-stacking unidirectional decoder. Second, our computation path is simpler; we go from ht → at → ct → h<sup>˜</sup> t then make a prediction as detailed in Eq. (5), Eq. (6), and Figure 2. On the other hand, at any time t, Bahdanau et al. (2015) build from the previous hidden state ht−1 → at → ct → ht, which, in turn, goes through a deep-output and a maxout layer before making predictions.<sup>7</sup> Lastly, Bahdanau et al. (2015) only experimented with one alignment function, the _concat_ product; whereas we show later that the other alternatives are better.

---

[referencia=c7a67a93fef201c0 score=0.043]
|[Jean et al.2015] S´ebastien<br>Jean,<br>Kyunghyun<br>Cho,<br>Roland Memisevic, and Yoshua Bengio. 2015. On<br>using very large target vocabulary for neural ma-<br>chine translation. In_ACL_.|English to German is harder than translating into<br>French as done in (Bahdanau et al., 2015), which<br>is an interesting point to examine in future work.|



- [Kalchbrenner and Blunsom2013] N. Kalchbrenner and P. Blunsom. 2013. Recurrent continuous translation models. In _EMNLP_ . 

- [Koehn et al.2003] Philipp Koehn, Franz Josef Och, and Daniel Marcu. 2003. Statistical phrase-based translation. In _NAACL_ . 

- [Liang et al.2006] P. Liang, B. Taskar, and D. Klein. 2006. Alignment by agreement. In _NAACL_ . 

- [Luong et al.2015] M.-T. Luong, I. Sutskever, Q. V. Le, O. Vinyals, and W. Zaremba. 2015. Addressing the rare word problem in neural machine translation. In _ACL_ . 

- [Mnih et al.2014] Volodymyr Mnih, Nicolas Heess, 

   - Alex Graves, and Koray Kavukcuoglu. 2014. Re- 

   - current models of visual attention. In _NIPS_ . 



<!-- Start of picture text -->
Sie<br>verstehen<br>nicht<br>warum,<br>Europa<br>theoretisch<br>zwar<br>existiert<br>aber,<br>nicht<br>in<br>Wirklichkeit<br>.<br>Theydo notunderstandwhyEuropeexistsin theorybutnotin reality.<br><!-- End of picture text -->



<!-- Start of picture text -->