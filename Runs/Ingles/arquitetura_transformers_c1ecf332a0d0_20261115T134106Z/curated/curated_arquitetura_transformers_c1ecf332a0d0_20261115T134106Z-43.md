[referencia=7d62adb6f51940dc score=0.992]
# **Are Sixteen Heads Really Better than One?** 

**Paul Michel** 

Language Technologies Institute Carnegie Mellon University Pittsburgh, PA pmichel1@cs.cmu.edu 

**Omer Levy** 

Facebook Artificial Intelligence Research Seattle, WA omerlevy@fb.com 

### **Graham Neubig** 

Language Technologies Institute Carnegie Mellon University Pittsburgh, PA gneubig@cs.cmu.edu 

## **Abstract** 

Attention is a powerful and ubiquitous mechanism for allowing neural models to focus on particular salient pieces of information by taking their weighted average when making predictions. In particular, _multi-headed attention_ is a driving force behind many recent state-of-the-art natural language processing (NLP) models such as Transformer-based MT models and BERT. These models apply multiple attention mechanisms in parallel, with each attention “head” potentially focusing on different parts of the input, which makes it possible to express sophisticated functions beyond the simple weighted average. In this paper we make the surprising observation that even if models have been trained using multiple heads, in practice, a large percentage of attention heads can be removed at test time without significantly impacting performance. In fact, some layers can even be reduced to a single head. We further examine greedy algorithms for pruning down models, and the potential speed, memory efficiency, and accuracy improvements obtainable therefrom. Finally, we analyze the results with respect to which parts of the model are more reliant on having multiple heads, and provide precursory evidence that training dynamics play a role in the gains provided by multi-head attention<sup>1</sup> .

---

[referencia=7d62adb6f51940dc score=0.966]
## **1 Introduction** 

Transformers (Vaswani et al., 2017) have shown state of the art performance across a variety of NLP tasks, including, but not limited to, machine translation (Vaswani et al., 2017; Ott et al., 2018), question answering (Devlin et al., 2018), text classification (Radford et al., 2018), and semantic role labeling (Strubell et al., 2018). Central to its architectural improvements, the Transformer extends the standard attention mechanism (Bahdanau et al., 2015; Cho et al., 2014) via multi-headed attention (MHA), where attention is computed independently by _Nh_ parallel attention mechanisms (heads). It has been shown that beyond improving performance, MHA can help with subject-verb agreement (Tang et al., 2018) and that some heads are predictive of dependency structures (Raganato and Tiedemann, 2018). Since then, several extensions to the general methodology have been proposed (Ahmed et al., 2017; Shen et al., 2018). 

> 1Code to replicate our experiments is provided at https://github.com/pmichel31415/ are-16-heads-really-better-than-1 

33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 

However, it is still not entirely clear: what do the multiple heads in these models buy us? In this paper, we make the surprising observation that – in both Transformer-based models for machine translation and BERT-based (Devlin et al., 2018) natural language inference – most attention heads can be individually removed after training without any significant downside in terms of test performance (§3.2). Remarkably, many attention layers can even be individually reduced to a single attention head without impacting test performance (§3.3).

---

[referencia=7d62adb6f51940dc score=0.909]
Concurrently to our own work, Voita et al. (2019) have made to a similar observation on multi-head attention. Their approach involves using LRP (Binder et al., 2016) for determining important heads and looking at specific properties such as attending to adjacent positions, rare words or syntactically related words. They propose an alternate pruning mechanism based on doing gradient descent on the mask variables _ξh_ . While their approach and results are complementary to this paper, our study provides additional evidence of this phenomenon beyond NMT, as well as an analysis of the training dynamics of pruning attention heads. 

## **8 Conclusion** 

We have observed that MHA does not always leverage its theoretically superior expressiveness over vanilla attention to the fullest extent. Specifically, we demonstrated that in a variety of settings, several heads can be removed from trained transformer models without statistically significant degradation in test performance, and that some layers can be reduced to only one head. Additionally, we have shown that in machine translation models, the encoder-decoder attention layers are much more reliant on multi-headedness than the self-attention layers, and provided evidence that the relative importance of each head is determined in the early stages of training. We hope that these observations will advance our understanding of MHA and inspire models that invest their parameters and attention more efficiently. 

## **Acknowledgments** 

The authors would like to extend their thanks to the anonymous reviewers for their insightful feedback. We are also particularly grateful to Thomas Wolf from Hugging Face, whose independent reproduction efforts allowed us to find and correct a bug in our speed comparison experiments. This research was supported in part by a gift from Facebook.

---

[referencia=7d62adb6f51940dc score=0.888]
Based on this observation, we further propose a simple algorithm that greedily and iteratively prunes away attention heads that seem to be contributing less to the model. By jointly removing attention heads from the entire network, without restricting pruning to a single layer, we find that large parts of the network can be removed with little to no consequences, but that the majority of heads must remain to avoid catastrophic drops in performance (§4). We further find that this has significant benefits for inference-time efficiency, resulting in up to a 17.5% increase in inference speed for a BERT-based model. 

We then delve into further analysis. A closer look at the case of machine translation reveals that the encoder-decoder attention layers are particularly sensitive to pruning, much more than the selfattention layers, suggesting that multi-headedness plays a critical role in this component (§5). Finally, we provide evidence that the distinction between important and unimporant heads increases as training progresses, suggesting an interaction between multi-headedness and training dynamics (§6).

---

[referencia=7d62adb6f51940dc score=0.864]
### **3.3 Ablating All Heads but One** 

This observation begets the question: is more than one head even needed? Therefore, we compute the difference in performance when all heads except one are removed, within a single layer. In Table 2 and Table 3 we report the best score for each layer in the model, i.e. the score when reducing the entire layer to the single most important head. 

We find that, for most layers, one head is indeed sufficient at test time, even though the network was trained with 12 or 16 attention heads. This is remarkable because these layers can be reduced to single-headed attention with only 1 _/_ 16th (resp. 1 _/_ 12th) of the number of parameters of a vanilla attention layer. However, some layers _do_ require multiple attention heads; for example, substituting the last layer in the encoder-decoder attention of WMT with a single head degrades performance by at least 13.5 BLEU points. We further analyze when different modeling components depend on more heads in §5. 

Additionally, we verify that this result holds even when we don’t have access to the evaluation set when selecting the head that is “best on its own”. For this purpose, we select the best head for each layer on a validation set (newstest2013 for WMT and a 5,000-sized randomly selected subset of the training set of MNLI for BERT) and evaluate the model’s performance on a test set 

4 



<!-- Start of picture text -->

---

[referencia=7d62adb6f51940dc score=0.702]
## **3 Are All Attention Heads Important?** 

We perform a series of experiments in which we remove one or more attention heads from a given architecture at test time, and measure the performance difference. We first remove a single attention head at each time (§3.2) and then remove every head in an entire layer except for one (§3.3). 

### **3.1 Experimental Setup** 

In all following experiments, we consider two trained models: 

**WMT** This is the original “large” transformer architecture from Vaswani et al. 2017 with 6 layers and 16 heads per layer, trained on the WMT2014 English to French corpus. We use the pretrained model of Ott et al. 2018.<sup>3</sup> and report BLEU scores on the newstest2013 test set. In accordance with Ott et al. 2018, we compute BLEU scores on the tokenized output of the model using Moses (Koehn et al., 2007). Statistical significance is tested with paired bootstrap resampling (Koehn, 2004) using compare-mt<sup>4</sup> (Neubig et al., 2019) with 1000 resamples. A particularity of this model is that it features 3 distinct attention mechanism: encoder self-attention (Enc-Enc), encoder-decoder attention (Enc-Dec) and decoder self-attention (Dec-Dec), all of which use MHA. 

**BERT** BERT (Devlin et al., 2018) is a single transformer pre-trained on an unsupervised clozestyle “masked language modeling task” and then fine-tuned on specific tasks. At the time of its inception, it achieved state-of-the-art performance on a variety of NLP tasks. We use the pre-trained base-uncased model of Devlin et al. 2018 with 12 layers and 12 attention heads which we fine-tune and evaluate on MultiNLI (Williams et al., 2018). We report accuracies on the “matched” validation set. We test for statistical significance using the t-test. In contrast with the WMT model, BERT only features one attention mechanism (self-attention in each layer).

---

[referencia=7d62adb6f51940dc score=0.649]
## **6 Dynamics of Head Importance during Training** 

Previous sections tell us that some heads are more important than others in _trained_ models. To get more insight into the dynamics of head importance _during training_ , we perform the same incremental pruning experiment of §4.2 at every epoch. We perform this experiment on a smaller version of WMT model (6 layers and 8 heads per layer), trained for German to English translation on the smaller IWSLT 2014 dataset Cettolo et al. (2015). We refer to this model as **IWSLT** . 

Figure 5 reports, for each level of pruning (by increments of 10% — 0% corresponding to the original model), the evolution of the model’s score (on newstest2013) for each epoch. For better readability we display epochs on a logarithmic scale, and only report scores every 5 epochs after the 10th). To make scores comparable across epochs, the Y axis reports the relative degradation of BLEU score with respect to the un-pruned model at each epoch. Notably, we find that there are two distinct regimes: in very early epochs (especially 1 and 2), performance decreases linearly with the pruning percentage, _i.e._ the relative decrease in performance is independent from _Ih_ , indicating that most heads are more or less equally important. From epoch 10 onwards, there is a concentration of unimportant heads that can be pruned while staying within 85 _−_ 90% of the original BLEU score (up to 40% of total heads). 

This suggests that the important heads are determined early (but not immediately) during the training process. The two phases of training are reminiscent of the analysis by Shwartz-Ziv and Tishby (2017), according to which the training of neural networks decomposes into an “empirical risk minimization” phase, where the model maximizes the mutual information of its intermediate representations with the labels, and a “compression” phase where the mutual information with the input is minimized. A more principled investigation of this phenomenon is left to future work.

---

[referencia=7d62adb6f51940dc score=0.602]
### **2.2 Multi-headed Attention** 

In _multi-headed_ attention (MHA), _Nh_ independently parameterized attention layers are applied in parallel to obtain the final result: 



where _Wk_<sup>_h, W_</sup> _q_<sup>_h, W_</sup> _v_<sup>_h∈_R</sup><sup>_dh×d_and</sup><sup>_W h_</sup> _o_<sup>_∈_R</sup><sup>_d×dh_.When</sup><sup>_dh_=</sup><sup>_d_, MHA is strictly more expressive</sup> than vanilla attention. However, to keep the number of parameters constant, _dh_ is typically set to _<u>d</u>_<sup>In the</sup> _Nh_<sup>, in which case MHA can be seen as an ensemble of low-rank vanilla attention layers2.</sup> following, we use Att _h_ ( _x_ ) as a shorthand for the output of head _h_ on input _x_ . 

To allow the different attention heads to interact with each other, transformers apply a non-linear feed-forward network over the MHA’s output, at each transformer layer (Vaswani et al., 2017). 

2This notation, equivalent to the “concatenation” formulation from Vaswani et al. (2017), is used to ease exposition in the following sections. 

2 



<!-- Start of picture text -->
80 Baseline Baseline<br>BLEU accuracy<br>70<br>40<br>60<br>50 30<br>40<br>20<br>30<br>20<br>10<br>10<br>35.5 35.6 35.7 35.8 35.9 36.0 36.1 36.2 36.3 0.824 0.826 0.828 0.830 0.832 0.834 0.836 0.838<br>BLEU Accuracy<br>(a) WMT (b) BERT<br>#heads #heads<br><!-- End of picture text -->

Figure 1: Distribution of heads by model score after masking.

---

[referencia=7d62adb6f51940dc score=0.495]
## **4 Iterative Pruning of Attention Heads** 

In our ablation experiments (§3.2 and §3.3), we observed the effect of removing one or more heads within a single layer, without considering what would happen if we altered two or more different layers at the same time. To test the compounding effect of pruning multiple heads from across the entire model, we sort all the attention heads in the model according to a proxy importance score (described below), and then remove the heads one by one. We use this iterative, heuristic approach to avoid combinatorial search, which is impractical given the number of heads and the time it takes to evaluate each model. 

5 



<!-- Start of picture text -->
35<br>0.8<br>30<br>25 0.6<br>20<br>15 0.4<br>10<br>0.2<br>5<br>0<br>0.0<br>0% 20% 40% 60% 80% 100% 0% 20% 40% 60% 80% 100%<br>Percentage pruned Percentage pruned<br>(a) Evolution of BLEU score on newstest2013 (b) Evolution of accuracy on the MultiNLI-matched<br>when heads are pruned from WMT. validation set when heads are pruned from BERT.<br>BLEU<br>Accuracy<br><!-- End of picture text -->

Figure 3: Evolution of accuracy by number of heads pruned according to _Ih_ (solid blue) and individual oracle performance difference (dashed green).

---

[referencia=7d62adb6f51940dc score=0.428]
## **5 When Are More Heads Important? The Case of Machine Translation** 

As shown in Table 2, not all MHA layers can be reduced to a single attention head without significantly impacting performance. To get a better idea of how much each part of the transformer-based translation model relies on multi-headedness, we repeat the heuristic pruning experiment from §4 for each type of attention separately (Enc-Enc, Enc-Dec, and Dec-Dec). 

Figure 4 shows that performance drops much more rapidly when heads are pruned from the Enc-Dec attention layers. In particular, pruning more than 60% of the Enc-Dec attention heads will result in catastrophic performance degradation, while the encoder and decoder self-attention layers can still produce reasonable translations (with BLEU scores around 30) with only 20% of the original attention heads. In other words, encoder-decoder attention is much more dependent on multi-headedness than self-attention. 



<!-- Start of picture text -->
35<br>30<br>25<br>20<br>15<br>10<br>Enc-Enc<br>5 Enc-Dec<br>Dec-Dec<br>0<br>0% 20% 40% 60% 80% 100%<br>Percentage pruned<br>BLEU<br><!-- End of picture text -->

Figure 4: BLEU when incrementally pruning heads from each attention type in the WMT model. 

> 6Slightly more in WMT because of the Enc-Dec attention. 

7 



<!-- Start of picture text -->

---

[referencia=7d62adb6f51940dc score=0.401]
Table 1: Difference in BLEU score for each head of the encoder’s self attention mechanism. Underlined numbers indicate that the change is statistically significant with _p <_ 0 _._ 01. The base BLEU score is 36 _._ 05. 

|Layer|Enc-Enc|Enc-Dec|Dec-Dec|Layer||Layer||
|---|---|---|---|---|---|---|---|
|1|**-1.31**|**0.24**|-0.03|1|-0.01%|7|0.05%|
|2|-0.16|0.06|0.12|2|0.10%|8|-0.72%|
|3|0.12|0.05|0.18|3|-0.14%|9|-0.96%|
|4|-0.15|-0.24|0.17|4|-0.53%|10|0.07%|
|5|0.02|**-1.55**|-0.04|5|-0.29%|11|-0.19%|
|6|**-0.36**|**-13.56**|0.24|6|-0.52%|12|-0.12%|



Table 2: Best delta BLEU by layer when only one head is kept in the WMT model. Underlined numbers indicate that the change is statistically significant with _p <_ 0 _._ 01. 

Table 3: Best delta accuracy by layer when only one head is kept in the BERT model. None of these results are statistically significant with _p <_ 0 _._ 01. 

worse than the full model’s, _h_ is obviously important; if the performance is comparable, _h_ is redundant given the rest of the model. 

Figures 1a and 1b shows the distribution of heads in term of the model’s score after masking it, for WMT and BERT respectively. We observe that the majority of attention heads can be removed without deviating too much from the original score. Surprisingly, in some cases removing an attention head results in an increase in BLEU/accuracy.

---

[referencia=7d62adb6f51940dc score=0.309]
To get a finer-grained view on these results we zoom in on the encoder self-attention layers of the WMT model in Table 1. Notably, we see that only 8 (out of 96) heads cause a statistically significant change in performance when they are removed from the model, half of which actually result in a higher BLEU score. This leads us to our first observation: **at test time, most heads are redundant given the rest of the model** .

---

[referencia=7d62adb6f51940dc score=0.299]
### **3.4 Are Important Heads the Same Across Datasets?** 

There is a caveat to our two previous experiments: these results are only valid on specific (and rather small) test sets, casting doubt on their generalizability to other datasets. As a first step to understand whether some heads are universally important, we perform the same ablation study on a second, out-of-domain test set. Specifically, we consider the MNLI “mismatched” validation set for BERT and the MTNT English to French test set (Michel and Neubig, 2018) for the WMT model, both of which have been assembled for the very purpose of providing contrastive, out-of-domain test suites for their respective tasks. 

We perform the same ablation study as §3.2 on each of these datasets and report results in Figures 2a and 2b. We notice that there is a positive, _>_ 0 _._ 5 correlation ( _p <_ 001) between the effect of removing a head on both datasets. Moreover, heads that have the highest effect on performance on one domain tend to have the same effect on the other, which suggests that the most important heads from §3.2 are indeed “universally” important.

---

[referencia=7d62adb6f51940dc score=0.288]
Figure 4: BLEU when incrementally pruning heads from each attention type in the WMT model. 

> 6Slightly more in WMT because of the Enc-Dec attention. 

7 



<!-- Start of picture text -->
100% P ercentage of<br>heads pruned<br>0% Epoch 1<br>80% 10% 100% Epoch 2<br>20% 75% Epoch 35<br>60% 30% Epoch 40<br>40% 50%<br>40% 50%<br>60% 25%<br>70%<br>20% 0%<br>80%<br>0% 25% 50% 75% 100%<br>90% Percentage pruned<br>0%<br>1 2 3 5 10 20 30 40<br>[3.0] [6.2] [18.1] [26.9] [30.6] [34.5] [34.7][34.9]<br>Epoch<br>[un-pruned BLEU score]<br>model BLEU score<br>Percentage of un-pruned<br>Percentage of original BLEU<br><!-- End of picture text -->

Figure 5: **Left side** : relationship between percentage of heads pruned and relative score decrease during training of the IWSLT model. We report epochs on a logarithmic scale. The BLEU score of the original, un-pruned model is indicated in brackets. **Right side** : focus on the difference in behaviour at the beginning (epochs 1 and 2) and end (epochs 35 and 40) of training.

---

[referencia=7d62adb6f51940dc score=0.156]
## **2 Background: Attention, Multi-headed Attention, and Masking** 

In this section we lay out the notational groundwork regarding attention, and also describe our method for masking out attention heads. 

### **2.1 Single-headed Attention** 

We briefly recall how vanilla attention operates. We focus on scaled bilinear attention (Luong et al., 2015), the variant most commonly used in MHA layers. Given a sequence of _n d_ -dimensional vectors **x** = _x_ 1 _, . . . , xn ∈_ R<sup>_d_</sup> , and a query vector _q ∈_ R<sup>_d_</sup> , the attention layer parametrized by _Wk, Wq, Wv, Wo ∈_ R<sup>_d×d_</sup> computes the weighted sum: 



In self-attention, every _xi_ is used as the query _q_ to compute a new sequence of representations, whereas in sequence-to-sequence models _q_ is typically a decoder state while **x** corresponds to the encoder output.

---

[referencia=7d62adb6f51940dc score=0.151]
## **A Ablating All Heads but One: Additional Experiment.** 

Tables 5 and 6 report the difference in performance when only one head is kept for any given layer. The head is chosen to be the best head on its own on a _separate_ dataset. 

11 

|Layer|Enc-Enc|Enc-Dec|Dec-Dec|Layer|||Layer|
|---|---|---|---|---|---|---|---|
|1|**-1.96**|0.02|0.03|1|-0.01%|7|0.05%|
|2|**-0.57**|0.09|-0.13|2|-0.02%|8|-0.72%|
|3|**-0.45**|**-0.42**|0.00|3|-0.26%|9|-0.96%|
|4|-0.30|**-0.60**|-0.31|4|-0.53%|10|0.07%|
|5|-0.32|**-2.75**|**-0.66**|5|-0.29%|11|-0.19%|
|6|**-0.67**|**-18.89**|-0.03|6|-0.52%|12|-0.15%|



Table 5: Best delta BLEU by layer on newstest2014 when only the best head (as evaluated on newstest2013) is kept in the WMT model. Underlined numbers indicate that the change is statistically significant with _p <_ 0 _._ 01. 

Table 6: Best delta accuracy by layer on the validation set of MNLI-matched when only the best head (as evaluated on 5,000 training examples) is kept in the BERT model. None of these results are statistically significant with _p <_ 0 _._ 01.

---

[referencia=7d62adb6f51940dc score=0.150]
- Ravid Shwartz-Ziv and Naftali Tishby. Opening the black box of deep neural networks via information. _arXiv preprint arXiv:1703.00810_ , 2017. 

- Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D. Manning, Andrew Ng, and Christopher Potts. Recursive deep models for semantic compositionality over a sentiment treebank. In _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1631–1642, 2013. 

- Emma Strubell, Patrick Verga, Daniel Andor, David Weiss, and Andrew McCallum. Linguisticallyinformed self-attention for semantic role labeling. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 5027–5038, 2018. 

- Gongbo Tang, Mathias Müller, Annette Rios, and Rico Sennrich. Why self-attention? a targeted evaluation of neural machine translation architectures. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 4263–4272, 2018. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In _Proceedings of the 30th Annual Conference on Neural Information Processing Systems (NIPS)_ , pages 5998–6008, 2017. 

- Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Titov Ivan. Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. In _Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL)_ , page to appear, 2019. 

- Alex Warstadt, Amanpreet Singh, and Samuel R. Bowman. Neural network acceptability judgments. _arXiv preprint arXiv:1805.12471_ , 2018.

---

[referencia=7d62adb6f51940dc score=0.113]
## **7 Related work** 

The use of an attention mechanism in NLP and in particular neural machine translation (NMT) can be traced back to Bahdanau et al. (2015) and Cho et al. (2014), and most contemporaneous implementations are based on the formulation from Luong et al. (2015). Attention was shortly adapted (successfully) to other NLP tasks, often achieving then state-of-the-art performance in reading comprehension (Cheng et al., 2016), natural language inference (Parikh et al., 2016) or abstractive summarization (Paulus et al., 2017) to cite a few. Multi-headed attention was first introduced by Vaswani et al. (2017) for NMT and English constituency parsing, and later adopted for transfer learning (Radford et al., 2018; Devlin et al., 2018), language modeling (Dai et al., 2019; Radford et al., 2019), or semantic role labeling (Strubell et al., 2018), among others. 

There is a rich literature on pruning trained neural networks, going back to LeCun et al. (1990) and Hassibi and Stork (1993) in the early 90s and reinvigorated after the advent of deep learning, with two 

8 

orthogonal approaches: fine-grained “weight-by-weight” pruning (Han et al., 2015) and structured pruning (Anwar et al., 2017; Li et al., 2016; Molchanov et al., 2017), wherein entire parts of the model are pruned. In NLP , structured pruning for auto-sizing feed-forward language models was first investigated by Murray and Chiang (2015). More recently, fine-grained pruning approaches have been popularized by See et al. (2016) and Kim and Rush (2016) (mostly on NMT).

---

[referencia=7d62adb6f51940dc score=0.095]
### **4.3 Effect of Pruning on Efficiency** 

Beyond the downstream task performance, there are intrinsic advantages to pruning heads. First, each head represents a non-negligible proportion of the total parameters in each attention layer (6 _._ 25% for WMT, _≈_ 8 _._ 34% for BERT), and thus of the total model (roughly speaking, in both our models, approximately one third of the total number of parameters is devoted to MHA across all layers).<sup>6</sup> This is appealing in the context of deploying models in memory-constrained settings. 

|Batch size|1|4|16|64|
|---|---|---|---|---|
|Original|17_._0_±_0_._3|67_._3_±_1_._3|114_._0_±_3_._6|124_._7_±_2_._9|
|Pruned (50%)|17_._3_±_0_._6|69_._1_±_1_._3|134_._0_±_3_._6|146_._6_±_3_._4|
||(+1.9%)|(+2.7%)|(+17.5%)|(+17.5%)|



Table 4: Average inference speed of BERT on the MNLI-matched validation set in examples per second ( _±_ standard deviation). The speedup relative to the original model is indicated in parentheses. 

Moreover, we find that actually pruning the heads (and not just masking) results in an appreciable increase in inference speed. Table 4 reports the number of examples per second processed by BERT, before and after pruning 50% of all attention heads. Experiments were conducted on two different machines, both equipped with GeForce GTX 1080Ti GPUs. Each experiment is repeated 3 times on each machine (for a total of 6 datapoints for each setting). We find that pruning half of the model’s heads speeds up inference by up to _≈_ 17 _._ 5% for higher batch sizes (this difference vanishes for smaller batch sizes).

---

[referencia=7d62adb6f51940dc score=0.080]
### **4.2 Effect of Pruning on BLEU/Accuracy** 

Figures 3a (for WMT) and 3b (for BERT) describe the effect of attention-head pruning on model performance while incrementally removing 10% of the total number of heads in order of increasing _Ih_ at each step. We also report results when the pruning order is determined by the score difference from §3.2 (in dashed lines), but find that using _Ih_ is faster and yields better results. 

We observe that this approach allows us to prune up to 20% and 40% of heads from WMT and BERT (respectively), without incurring any noticeable negative impact. Performance drops sharply when pruning further, meaning that neither model can be reduced to a purely single-head attention model without retraining or incurring substantial losses to performance. We refer to Appendix B for experiments on four additional datasets. 

> 5For the WMT model we use all newstest20[09-12] sets to estimate _I_ . 

6