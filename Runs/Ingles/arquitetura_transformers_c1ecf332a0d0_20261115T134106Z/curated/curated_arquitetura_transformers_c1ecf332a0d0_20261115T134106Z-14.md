[referencia=94d3d49016ad4075 score=0.846]
3.3 Input-feeding Approach tokenized 12 BLEU to be comparable with existing<br>In our proposed global and local approaches, NMT work and (b)  NIST 13 BLEU to be compara-<br>ble with WMT results.<br>the attentional decisions are made independently,<br>which is suboptimal. Whereas, in standard MT,<br>4.1 Training Details<br>a coverage set is often maintained during the<br>translation process to keep track of which source All our models are trained on the WMT’14 train-<br>words have been translated. Likewise, in atten- ing data consisting of 4.5M sentences pairs (116M<br>tional NMTs, alignment decisions should be made English words, 110M German words). Similar<br>jointly taking into account past alignment infor- to (Jean et al., 2015), we limit our vocabularies to<br>mation. To address that, we propose an input- be the top 50K most frequent words for both lan-<br>feeding approach in which attentional vectors h ˜ t guages. Words not in these shortlisted vocabular-<br>are concatenated with inputs at the next time steps ies are converted into a universal token < unk >.<br>as illustrated in Figure 4. 11 The effects of hav- When training our NMT systems, following<br>ing such connections are two-fold: (a) we hope (Bahdanau et al., 2015; Jean et al., 2015), we fil-<br>to make the model fully aware of previous align- ter out sentence pairs whose lengths exceed<br>ment choices and (b) we create a very deep net- 50 words and shuffle mini-batches as we pro-<br><!-- End of picture text -->

ceed. Our stacking LSTM models have 4 lay- 

work spanning both horizontally and vertically.

---

[referencia=94d3d49016ad4075 score=0.798]
**1 Introduction** Neural Machine Translation (NMT) achieved 

state-of-the-art performances in large-scale trans- 

performances large-scale transframes and text in the speech recognition task lation tasks such as from English to French ( **?** ), or between visual features of a picture and (Luong et al., 2015) and English to German its text description in the image caption gener(Jean et al., 2015). NMT is appealing since it reation task (Xu et al., 2015). In the context of quires minimal domain knowledge and is concepNMT, Bahdanau et al. (2015) has successfully ap- 

tually simple. The model by Luong et al. (2015) reads through all the source words until the end-ofsentence symbol < `eos` > is reached. It then starts 1All our code and models are publicly available at `http://nlp.stanford.edu/projects/nmt` . 

plied such attentional mechanism to jointly translate and align words. To the best of our knowledge, there has not been any other work exploring the use of attention-based architectures for NMT. In this work, we design, with simplicity and ef- 



fectiveness in mind, two novel types of attentionbased models: a _global_ approach in which all source words are attended and a _local_ one whereby only a subset of source words are considered at a time. The former approach resembles the model of (Bahdanau et al., 2015) but is simpler architecturally. The latter can be viewed as an interesting blend between the _hard_ and _soft_ attention models proposed in (Xu et al., 2015): it is computationally less expensive than the global model or the soft attention; at the same time, unlike the hard attention, the local attention is differentiable almost everywhere, making it easier to implement and train.<sup>2</sup> Besides, we also examine various alignment functions for our attention-based models.

---

[referencia=94d3d49016ad4075 score=0.771]
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

[referencia=94d3d49016ad4075 score=0.764]
## **Abstract** 



An attentional mechanism has lately been 

used to improve neural machine transla- 

tion (NMT) by selectively focusing on parts of the source sentence during translation. However, there has been little work exploring useful architectures for attention-based NMT. This paper examines two simple and effective classes of attentional mechanism: a _global_ approach which always attends to all source words and a _local_ one that only looks at a subset of source words at a time. We demonstrate the effectiveness of both approaches on the WMT translation tasks between English and German in both directions. With local attention, we achieve a significant gain of 

A B C D <eos> X Y Z 

Figure 1: **Neural machine translation** – a stacking recurrent architecture for translating a source sequence `A B C D` into a target sequence `X Y Z` . Here, < `eos` > marks the end of a sentence. emitting one target word at a time, as illustrated in Figure 1. NMT is often a large neural network that 

is trained in an end-to-end fashion and has the abil- 

5.0 BLEU points over non-attentional sys- 

ity to generalize well to very long word sequences. This means the model does not have to explicitly 

tems that already incorporate known tech- 

niques such as dropout. Our ensemble 

store gigantic phrase tables and language models as in the case of standard MT; hence, NMT has a small memory footprint. Lastly, implementing NMT decoders is easy unlike the highly intricate decoders in standard MT (Koehn et al., 2003). 

model using different attention architectures yields a new state-of-the-art result in the WMT’15 English to German translation task with 25.9 BLEU points, an im- 

provement of 1.0 BLEU points over the existing best system backed by NMT and an n-gram reranker.<sup>1</sup> 

In parallel, the concept of “attention” has gained popularity recently in training neural networks, allowing models to learn alignments between different modalities, e.g., between image objects and agent actions in the dynamic control problem (Mnih et al., 2014), between speech 

**1 Introduction** Neural Machine Translation (NMT) achieved 

state-of-the-art performances in large-scale trans-

---

[referencia=94d3d49016ad4075 score=0.731]
˜ in this work. Also, our approach is more general;<br>h˜t as illustrated in Figure 4, it can be applied to<br>general stacking recurrent architectures, including<br>non-attentional models.<br>Xu et al. (2015) propose a doubly attentional<br>Attention Layer<br>approach with an additional constraint added to<br>the training objective to make sure the model pays<br>equal attention to all parts of the image during the<br>caption generation process. Such a constraint can<br>also be useful to capture the coverage set effect<br>in NMT that we mentioned earlier. However, we<br>chose to use the input-feeding approach since it<br>A B C D <eos> X Y Z provides flexibility for the model to decide on any<br>Figure 4: Input-feeding approach – Attentional attentional constraints it deems suitable.<br>vectors h ˜ t are fed as inputs to the next time steps to<br>4 Experiments<br>inform the model about past alignment decisions.<br>We evaluate the effectiveness of our models<br>on the WMT translation tasks between En-<br>Comparison to (Gregor et al., 2015)  – have pro-<br>posed a  selective attention mechanism, very simi- glish and German in both directions. new-<br>stest2013 (3000 sentences) is used as a develop-<br>lar to our local attention, for the image generation<br>task. Their approach allows the model to select an ment set to select our hyperparameters. Transla-<br>image patch of varying location and zoom. We, tion performances are reported in case-sensitive<br>instead, use the same “zoom” for all target posi- BLEU (Papineni et al., 2002) on newstest2014<br>tions, which greatly simplifies the formulation and (2737 sentences) and newstest2015 (2169 sen-<br>tences). Following (Luong et al., 2015), we report<br>still achieves good performance.<br>translation quality using two types of BLEU: (a)<br>3.3 Input-feeding Approach tokenized 12 BLEU to be comparable with existing<br>In our proposed global and local approaches, NMT work and (b)  NIST 13 BLEU to be compara-<br>

---

[referencia=94d3d49016ad4075 score=0.697]
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

[referencia=94d3d49016ad4075 score=0.680]
### **3.2 Local Attention** 

The global attention has a drawback that it has to attend to all words on the source side for each target word, which is expensive and can potentially render it impractical to translate longer sequences, e.g., paragraphs or documents. To address this deficiency, we propose a _local_ attentional mechanism that chooses to focus only on a small subset of the source positions per target word. 

This model takes inspiration from the tradeoff between the _soft_ and _hard_ attentional models proposed by Xu et al. (2015) to tackle the image caption generation task. In their work, soft attention 



7We will refer to this difference again in Section 3.3. 

refers to the global attention approach in which weights are placed “softly” over all patches in the source image. The hard attention, on the other hand, selects one patch of the image to attend to at a time. While less expensive at inference time, the hard attention model is non-differentiable and requires more complicated techniques such as variance reduction or reinforcement learning to train. 

Our local attention mechanism selectively focuses on a small window of context and is differentiable. This approach has an advantage of avoiding the expensive computation incurred in the soft attention and at the same time, is easier to train than the hard attention approach. In concrete details, the model first generates an aligned position pt for each target word at time t. The context vector ct is then derived as a weighted average over the set of source hidden states within the window [pt−D, pt+D]; D is empirically selected.<sup>8</sup> Unlike the global approach, the local alignment vector at is now fixed-dimensional, i.e., ∈ R<sup>2D+1</sup> . We consider two variants of the model as below. 

_Monotonic_ alignment ( **local-m** ) – we simply set pt = t assuming that source and target sequences are roughly monotonically aligned. The alignment vector at is defined according to Eq. (7).<sup>9</sup> 

_Predictive_ alignment ( **local-p** ) – instead of assuming monotonic alignments, our model predicts an aligned position as follows:

---

[referencia=94d3d49016ad4075 score=0.658]
### **4.2 English-German Results** 

We compare our NMT systems in the EnglishGerman task with various other systems. These include the winning system in WMT’14 (Buck et al., 2014), a phrase-based system whose language models were trained on a huge monolingual text, the Common Crawl corpus. For end-to-end NMT systems, to the best of our knowledge, (Jean et al., 2015) is the only work experimenting with this language pair and currently the SOTA system. We only present results for some of our attention models and will later analyze the rest in Section 5. 

As shown in Table 1, we achieve pro- 

gressive improvements when (a) reversing the source sentence, +1.3 BLEU, as proposed in (Sutskever et al., 2014) and (b) using dropout, +1.4 BLEU. On top of that, (c) the global attention approach gives a significant boost of +2.8 BLEU, making our model slightly better than the base attentional system of Bahdanau et al. (2015) (row _RNNSearch_ ). When (d) using the _inputfeeding_ approach, we seize another notable gain of +1.3 BLEU and outperform their system. The local attention model with predictive alignments (row _local-p_ ) proves to be even better, giving us a further improvement of +0.9 BLEU on top of the global attention model. It is interesting to observe the trend previously reported in (Luong et al., 2015) that perplexity strongly correlates with translation quality. In total, we achieve a significant gain of 5.0 BLEU points over the non-attentional baseline, which already includes known techniques such as source reversing and dropout. 

The unknown replacement technique proposed in (Luong et al., 2015; Jean et al., 2015) yields another nice gain of +1.9 BLEU, demonstrating that our attentional models do learn useful alignments for unknown works. Finally, by ensembling 8 different models of various settings, e.g., using different attention approaches, with and without dropout etc., we were able to achieve a _new SOTA_ result of 23.0 BLEU, outperforming the existing 

best system (Jean et al., 2015) by +1.4 BLEU.

---

[referencia=94d3d49016ad4075 score=0.457]
Table 4: **Attentional Architectures** – performances of different attentional models. We trained two local-m (dot) models; both have ppl > 7.0. 

not learn good alignments: the _global (location)_ model can only obtain a small gain when performing unknown word replacement compared to using other alignment functions.<sup>14</sup> For _contentbased_ functions, our implementation _concat_ does not yield good performances and more analysis should be done to understand the reason.<sup>15</sup> It is interesting to observe that _dot_ works well for the global attention and _general_ is better for the local attention. Among the different models, the local attention model with predictive alignments ( _localp_ ) is best, both in terms of perplexities and BLEU.

---

[referencia=94d3d49016ad4075 score=0.340]
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

[referencia=94d3d49016ad4075 score=0.332]
## **A Alignment Visualization** 

We visualize the alignment weights produced by our different attention models in Figure 7. The visualization of the local attention model is much sharper than that of the global one. This contrast matches our expectation that local attention is designed to only focus on a subset of words each time. Also, since we translate from English to German and reverse the source English sentence, the white strides at the words _“reality”_ and _“.”_ in the global attention model reveals an interesting access pattern: it tends to refer back to the beginning of the source sequence. 

Compared to the alignment visualizations in (Bahdanau et al., 2015), our alignment patterns are not as sharp as theirs. Such difference could possibly be due to the fact that translating from English to German is harder than translating into French as done in (Bahdanau et al., 2015), which is an interesting point to examine in future work. 

- [Kalchbrenner and Blunsom2013] N. Kalchbrenner and P. Blunsom. 2013. Recurrent continuous translation models. In _EMNLP_ . 

- [Koehn et al.2003] Philipp Koehn, Franz Josef Och, and Daniel Marcu. 2003. Statistical phrase-based translation. In _NAACL_ . 

- [Liang et al.2006] P. Liang, B. Taskar, and D. Klein. 2006. Alignment by agreement. In _NAACL_ . 

- [Luong et al.2015] M.-T. Luong, I. Sutskever, Q. V. Le, O. Vinyals, and W. Zaremba. 2015. Addressing the rare word problem in neural machine translation. In _ACL_ . 

- [Mnih et al.2014] Volodymyr Mnih, Nicolas Heess, Alex Graves, and Koray Kavukcuoglu. 2014. Recurrent models of visual attention. In _NIPS_ . 





- Sie 

   - Sie 

- verstehen verstehen nicht nicht 

- warum, warum, Europa Europa 

- theoretisch theoretisch zwar zwar 

- existiert existiert 

aber, 

aber, nicht in . 

##### nicht in Wirklichkeit 

Wirklichkeit

---

[referencia=94d3d49016ad4075 score=0.303]
In more detail, one can parameterize the probability of decoding each word yj as: 



with g being the transformation function that outputs a vocabulary-sized vector.<sup>5</sup> Here, hj is the RNN hidden unit, abstractly computed as: 



where f computes the current hidden state given the previous hidden state and can be either a vanilla RNN unit, a GRU, or an LSTM unit. In (Kalchbrenner and Blunsom, 2013; Sutskever et al., 2014; Cho et al., 2014; Luong et al., 2015), the source representation s is only used once to initialize the decoder hidden state. On the other hand, in (Bahdanau et al., 2015; Jean et al., 2015) and this work, s, in fact, implies a set of source hidden states which are consulted throughout the entire course of the translation process. Such an approach is referred to as an attention mechanism, which we will discuss next. 

In this work, following (Sutskever et al., 2014; Luong et al., 2015), we use the stacking LSTM architecture for our NMT systems, as illustrated 



> 4They all used a single RNN layer except for the latter two works which utilized a bidirectional RNN for the encoder. 

> 5 One can provide g with other inputs such as the currently predicted word yj as in (Bahdanau et al., 2015). 

in Figure 1. We use the LSTM unit in (Zaremba et al., 2015). Our training objective is formulated as follows: 



with D being our parallel training corpus.

---

[referencia=94d3d49016ad4075 score=0.265]
## **2 Neural Machine Translation** 

A neural machine translation system is a neural network that directly models the conditional probability p(y|x) of translating a source sentence, x1, . . . , xn, to a target sentence, y1, . . . , ym.<sup>3</sup> A basic form of NMT consists of two components: (a) an _encoder_ which computes a representation s for each source sentence and (b) a _decoder_ which generates one target word at a time and hence decomposes the conditional probability as: 



A natural choice to model such a decomposition in the decoder is to use a 



> 2There is a recent work by Gregor et al. (2015), which is very similar to our local attention and applied to the image generation task. However, as we detail later, our model is much simpler and can achieve good performance for NMT. 

> 3All sentences are assumed to terminate with a special “end-of-sentence” token < `eos` >. 

recurrent neural network (RNN) architecture, which most of the recent NMT work such as (Kalchbrenner and Blunsom, 2013; Sutskever et al., 2014; Cho et al., 2014; Bahdanau et al., 2015; Luong et al., 2015; Jean et al., 2015) have in common. They, however, differ in terms of which RNN architectures are used for the decoder and how the encoder computes the source sentence representation s. 

Kalchbrenner and Blunsom (2013) used an RNN with the standard hidden unit for the decoder and a convolutional neural network for encoding the source sentence representation. On the other hand, both Sutskever et al. (2014) and Luong et al. (2015) stacked multiple layers of an RNN with a Long Short-Term Memory (LSTM) hidden unit for both the encoder and the decoder. Cho et al. (2014), Bahdanau et al. (2015), and Jean et al. (2015) all adopted a different version of the RNN with an LSTM-inspired hidden unit, the gated recurrent unit (GRU), for both components.<sup>4</sup> 

In more detail, one can parameterize the probability of decoding each word yj as:

---

[referencia=94d3d49016ad4075 score=0.237]
## **6 Conclusion** 

best systems, backed by NMT models and n-gram In this paper, we propose two simple and effective LM rerankers, by more than 1.0 BLEU. attentional mechanisms for neural machine transWe have compared various alignment functions 

lation: the _global_ approach which always looks 

and shed light on which functions are best for at all source positions and the _local_ one that only which attentional models. Our analysis shows that attends to a subset of source positions at a time. attention-based NMT models are superior to nonWe test the effectiveness of our models in the attentional ones in many cases, for example in WMT translation tasks between English and Gertranslating names and handling long sentences. man in both directions. Our local attention yields 

large gains of up to 5.0 BLEU over non-attentional **Acknowledgment** 



> 17The reference uses a more fancy translation of “incompatible”, which is “im Widerspruch zu etwas stehen”. Both We gratefully acknowledge support from a gift 

> models, however, failed to translate “passenger experience”. from Bloomberg L.P. and the support of NVIDIA 

Corporation with the donation of Tesla K40 GPUs. We thank Andrew Ng and his group as well as the Stanford Research Computing for letting us use their computing resources. We thank Russell Stewart for helpful discussions on the models. Lastly, we thank Quoc Le, Ilya Sutskever, Oriol Vinyals, Richard Socher, Michael Kayser, Jiwei Li, Panupong Pasupat, Kelvin Guu, members of the Stanford NLP Group and the annonymous reviewers for their valuable comments and feedback.

---

[referencia=94d3d49016ad4075 score=0.224]
## **3 Attention-based Models** 

Our various attention-based models are classifed into two broad categories, _global_ and _local_ . These classes differ in terms of whether the “attention” is placed on all source positions or on only a few source positions. We illustrate these two model types in Figure 2 and 3 respectively. 

Common to these two types of models is the fact that at each time step t in the decoding phase, both approaches first take as input the hidden state ht at the top layer of a stacking LSTM. The goal is then to derive a context vector ct that captures relevant source-side information to help predict the current target word yt. While these models differ in how the context vector ct is derived, they share the same subsequent steps. 

ht and the source-side context vector ct, we employ a simple concatenation layer to combine the information from both vectors to produce an attentional hidden state as follows: 



The attentional vector h<sup>˜</sup> t is then fed through the softmax layer to produce the predictive distribution formulated as: 



We now detail how each model type computes the source-side context vector ct.

---

[referencia=94d3d49016ad4075 score=0.159]
# **Effective Approaches to Attention-based Neural Machine Translation** 

**Minh-Thang Luong Hieu Pham Christopher D. Manning** Computer Science Department, Stanford University, Stanford, CA 94305 { `lmthang,hyhieu,manning` } `@stanford.edu` 

X Y 

Z <eos>

---

[referencia=94d3d49016ad4075 score=0.154]
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

[referencia=94d3d49016ad4075 score=0.132]
##### nicht in Wirklichkeit 

Wirklichkeit 

##### . 

Sie Sie verstehen verstehen nicht nicht 





warum, warum, Europa Europa theoretisch theoretisch zwar zwar existiert existiert aber, aber, nicht nicht in in Wirklichkeit Wirklichkeit 

. . 

- Figure 7: **Alignment visualizations** – shown are images of the attention weights learned by various models: (top left) global, (top right) local-m, and (bottom left) local-p. The _gold_ alignments are displayed at the bottom right corner.

---

[referencia=94d3d49016ad4075 score=0.130]
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

[referencia=94d3d49016ad4075 score=0.106]
## **5 Analysis** 

We conduct extensive analysis to better understand our models in terms of learning, the ability to handle long sentences, choices of attentional architectures, and alignment quality. All results reported here are on English-German newstest2014.