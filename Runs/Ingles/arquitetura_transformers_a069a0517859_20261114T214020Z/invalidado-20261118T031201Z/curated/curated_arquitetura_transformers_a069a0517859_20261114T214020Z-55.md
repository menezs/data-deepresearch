[referencia=a426845dabe2c7d6 score=0.997]
# **Attention is not Explanation** 

## **Sarthak Jain** 

Northeastern University 

jain.sar@husky.neu.edu 

**Byron C. Wallace** Northeastern University 

b.wallace@northeastern.edu 

## **Abstract** 

Attention mechanisms have seen wide adoption in neural NLP models. In addition to improving predictive performance, these are often touted as affording transparency: models equipped with attention provide a distribution over attended-to input units, and this is often presented (at least implicitly) as communicating the relative importance of inputs. However, it is unclear what relationship exists between attention weights and model outputs. In this work we perform extensive experiments across a variety of NLP tasks that aim to assess the degree to which attention weights provide meaningful “explanations" for predictions. We find that they largely do not. For example, learned attention weights are frequently uncorrelated with gradient-based measures of feature importance, and one can identify very different attention distributions that nonetheless yield equivalent predictions. Our findings show that standard attention modules do not provide meaningful explanations and should not be treated as though they do. Code to reproduce all experiments is available at https://github.com/successar/ AttentionExplanation.

---

[referencia=a426845dabe2c7d6 score=0.995]
Assuming attention provides a faithful explanation for model predictions, we might expect the following properties to hold. (i) Attention weights should correlate with feature importance measures (e.g., gradient-based measures); (ii) Alternative (or _counterfactual_ ) attention weight configurations ought to yield corresponding changes in prediction (and if they do not then are equally plausible as explanations). We report that neither property is consistently observed by a BiLSTM with a standard attention mechanism in the context of text classification, question answering (QA), and Natural Language Inference (NLI) tasks. 

> 1We do not intend to single out any particular work; indeed one of the authors has himself presented (supervised) attention as providing interpretability (Zhang et al., 2016). 

Consider Figure 1. The left panel shows the original attention distribution _α_ over the words of a particular movie review using a standard attentive BiLSTM architecture for sentiment analysis. It is tempting to conclude from this that the token _waste_ is largely responsible for the model coming ˆ to its disposition of ‘negative’ ( _y_ = 0 _._ 01). But one can construct an alternative attention distribution _α_ ˜ (right panel) that attends to entirely different tokens yet yields an essentially identical prediction (holding all other parameters of _f_ , _θ_ , constant). 

Such counterfactual distributions imply that explaining the original prediction by highlighting attended-to tokens is misleading. One may, e.g., now conclude from the right panel that model output was due primarily to _was_ ; but both _waste_ and _was_ cannot simultaneously be responsible. Further, the attention weights in this case correlate only weakly with gradient-based measures of feature importance ( _τg_ = 0 _._ 29). And arbitrarily permuting the entries in _α_ yields a median output difference of 0.006 with the original prediction. 

These and similar findings call into question the view that attention provides meaningful insight into model predictions, at least for RNN-based models. We thus caution against using attention weights to highlight input tokens “responsible for” model outputs and constructing just-so stories on this basis.

---

[referencia=a426845dabe2c7d6 score=0.992]
**Research questions and contributions** . We examine the extent to which the (often implicit) narrative that attention provides model _transparency_ (Lipton, 2016). We are specifically interested in whether attention weights indicate _why_ a model made the prediction that it did. This is sometimes called _faithful_ explanation (Ross et al., 2017). We investigate whether this holds across tasks by exploring the following empirical questions. 

1. To what extent do induced attention weights correlate with measures of feature importance – specifically, those resulting from gradients and _leave-one-out_ (LOO) methods? 

2. Would alternative attention weights (and hence distinct heatmaps/“explanations”) necessarily yield different predictions? 

Our findings for attention weights in recurrent (BiLSTM) encoders with respect to these questions are summarized as follows: (1) Only weakly and inconsistently, and, (2) No; it is very often 

possible to construct _adversarial_ attention distributions that yield effectively equivalent predictions as when using the originally induced attention weights, despite attending to entirely different input features. Even more strikingly, randomly permuting attention weights often induces only minimal changes in output. By contrast, attention weights in simple, feedforward (weighted average) encoders enjoy better behaviors with respect to these criteria.

---

[referencia=a426845dabe2c7d6 score=0.979]
## **4 Experiments** 

We run a battery of experiments that aim to examine empirical properties of learned attention weights and to interrogate their interpretability and transparency. The key questions are: _Do learned attention weights agree with alternative, natural measures of feature importance_ ? And, _Had we attended to different features, would the prediction have been different?_ 

More specifically, in Section 4.1, we empirically analyze the correlation between gradientbased feature importance and learned attention weights, and between emphleave-one-out (LOO; or ‘feature erasure’) measures and the same. In Section 4.2 we then consider counterfactual (to those observed) attention distributions. Under the assumption that attention weights are explanatory, such counterfactual distributions may be viewed as alternative potential explanations; if these do not correspondingly change model output, then it is hard to argue that the original attention weights provide meaningful explanation in the first place. 

To generate counterfactual attention distributions, we first consider randomly permuting observed attention weights and recording associated changes in model outputs (4.2.1). We then propose explicitly searching for “adversarial” attention weights that maximally differ from the observed attention weights (which one might show in a heatmap and use to explain a model prediction), and yet yield an effectively equivalent prediction (4.2.2). The latter strategy also provides a useful potential metric for the reliability of attention weights as explanations: we can report a measure quantifying how different attention weights can be for a given instance without changing the model output by more than some threshold _ϵ_ . 

All results presented below are generated on test sets. We present results for _Additive_ attention below. The results for _Scaled Dot Product_ in its place are generally comparable. We provide a web interface to interactively browse the (very large set of) plots for all datasets, model variants, and experiment types: https://successar.github. io/AttentionExplanation/docs/. 

In the following sections, we use Total Variation Distance (TVD) as the measure of change

---

[referencia=a426845dabe2c7d6 score=0.976]
## **6 Discussion and Conclusions** 

We have provided evidence that correlation between intuitive feature importance measures (including gradient and feature erasure approaches) and learned attention weights is weak for recurrent encoders (Section 4.1). We also established that counterfactual attention distributions — which would tell a different story about why a model made the prediction that it did — often have modest effects on model output (Section 4.2). 

These results suggest that while attention modules consistently yield improved performance on NLP tasks, their ability to provide transparency or meaningful explanations for model predictions is, at best, questionable – especially when a complex 

encoder is used, which may entangle inputs in the hidden space. In our view, this should not be terribly surprising, given that the encoder induces rep- 

spective tasks included in our analysis. We have been particularly focused on RNNs (here, BiL- 

resentations that may encode arbitrary interactions STMs) and attention, which is very commonly between individual inputs; presenting heatmaps of used. As we have shown, results for the simple attention weights placed over these inputs can then feed-forward encoder demonstrate greater fidelity be misleading. And indeed, how one is meant to to alternative feature importance measures. Other interpret such heatmaps is unclear. They would feedforward models (including convolutional arseem to suggest a story about how a model arrived chitectures) may enjoy similar properties, when 

at a particular disposition, but the results here indesigned with care. Alternative attention specifidicate that the relationship between this and attencations may yield different conclusions; and intion is not always obvious. deed we hope this work motivates further devel- 



<!-- Start of picture text -->

---

[referencia=a426845dabe2c7d6 score=0.963]
A potential issues with using Kendall _τ_ as our metric here is that (potentially many) irrelevant features may add noise to the correlation measures. We acknowledge that this as a shortcoming 

of the metric. One observation that may mitigate this concern is that we might expect such noise to depress the LOO and gradient correlations to the same extent as they do the correlation between attention and feature importance scores; but as per Figure 4, they do not. We also note that the correlations between the attention weights on top of feedforward (projection) encoder and LOO scores are much stronger, on average, than those between BiLSTM attention weights and LOO. This is shown in Figure 5. Were low correlations due simply to noise, we would not expect this.<sup>5</sup> 

The results here suggest that, in general, attention weights do not strongly or consistently agree with standard feature importance scores. The exception to this is when one uses a very simple (averaging) encoder model, as one might expect. These findings should be disconcerting to one hoping to view attention weights as explanatory, given the face validity of input gradient/erasure based explanations (Ross et al., 2017; Li et al., 2016).

---

[referencia=a426845dabe2c7d6 score=0.957]
### **4.1 Correlation Between Attention and Feature Importance Measures** 

We empirically characterize the relationship between attention weights and corresponding feature importance scores. Specifically we measure correlations between attention and: (1) gradient based measures of feature importance ( _τg_ ), and, (2) differences in model output induced by leaving features out ( _τloo_ ). While these measures are themselves insufficient for interpretation of neural model behavior (Feng et al., 2018), they do provide measures of individual feature importance with known semantics (Ross et al., 2017). It is thus instructive to ask whether these measures correlate with attention weights. 

The process we follow to quantify this is described by Algorithm 1. We denote the input resulting from removing the word at position _t_ in **x** by **x** _−t_ . Note that we disconnect the computation graph at the attention module so that the gradient does not flow through this layer: This means the gradients tell us how the prediction changes as a function of inputs, _keeping the attention distribution fixed_ .<sup>4</sup> 



Table 2 reports summary statistics of Kendall _τ_ correlations for each dataset. Full distributions are shown in Figure 2, which plots histograms of _τg_ for every data point in the respective corpora. (Corresponding plots for _τloo_ are similar and the full set can be browsed via the aforementioned online supplement.) We plot these separately for each class: orange (■) represents instances predicted as positive, and purple (■) those predicted 

> 4For further discussion concerning our motivation here, see the Appendix. We also note that LOO results are comparable, and do not have this complication.

---

[referencia=a426845dabe2c7d6 score=0.948]
### **4.2 Counterfactual Attention Weights** 

We next consider _what-if_ scenarios corresponding to alternative (counterfactual) attention weights. The idea is to investigate whether the prediction would have been different, had the model emphasized (attended to) different input features. More ˆ precisely, suppose _α_ = _{_ ˆ _αt}_<sup>_T_</sup> _t_ =1<sup>aretheatten-</sup> tion weights induced for an instance, giving rise to model output _y_ ˆ. We then consider counterfactual distributions over _y_ , under alternative _α_ . To be clear, these experiments tell us the degree to which a particular (attention) heat map uniquely induces an output. 

We experiment with two means of constructing such distributions. First, we simply scramble the original attention weights _α_ ˆ, re-assigning each value to an arbitrary, randomly sampled index (input feature). Second, we generate an _adversarial attention distribution_ : this is a set of attention weights that is maximally distinct from _α_ ˆ but that nonetheless yields an equivalent prediction (i.e., prediction within some _ϵ_ of _y_ ˆ). 

### **4.2.1 Attention Permutation** 

To characterize model behavior when attention weights are shuffled, we follow Algorithm 2. 

> 5The same contrast can be seen for the gradients, as one would expect given the direct gradient paths in the projection network back to individual tokens.

---

[referencia=a426845dabe2c7d6 score=0.941]
Equation 1 attempts to identify a set of new attention distributions over the input that is as far as possible from the observed _α_ (as measured by JSD) and from each other (and thus diverse), while keeping the output of the model within _ϵ_ of the original prediction. We denote the output obtained under the _i_<sup>_th_</sup> adversarial attention by ˆ _y_<sup>(</sup><sup>_i_)</sup> . Note that the JS Divergence between any two categorical distributions (irrespective of length) is bounded from above by 0.69. 

One can view an attentive decoder as a function that maps from the space of latent input representations and attention weights over input words ∆<sup>_T−_1</sup> to a distribution over the output space _Y_ . Thus, for any output _y_ ˆ, we can define how likely each attention distribution _α_ will generate the output as inversely proportional to TVD( _y_ ( _α_ ) _,_ ˆ _y_ ). 

> 6We make the threshold slightly higher for QA because the output space is larger and thus small dimension-wise perturbations can produce comparatively large TVD. 

> 7We set _λ_ = 500. 



Figure 7 depicts the distributions of max JSDs realized over instances with adversarial attention weights for a subset of the datasets considered (plots for the remaining corpora are available online). Colors again indicate predicted class. Mass toward the upper-bound of 0.69 indicates that we are frequently able to identify maximally different attention weights that hardly budge model output. We observe that one can identify adversarial attention weights associated with high JSD for a significant number of examples. This means that it is often the case that quite different attention distributions over inputs would yield essentially the same (within _ϵ_ ) output. 

In the case of the _Diabetes_ task, we again observe a pattern of low JSD for positive examples (where evidence is present) and high JSD for negative examples. In other words, for this task, if one perturbs the attention weights when it is inferred that the patient is diabetic, this does change the output, which is intuitively agreeable. However, this behavior again is an exception to the rule.

---

[referencia=a426845dabe2c7d6 score=0.927]
<!-- Start of picture text -->
There are important limitations to this work opment of principled attention mechanisms.<br>and the conclusions we can draw from it. We have It is also important to note that the counterfac-<br>tual attention experiments demonstrate the exis-<br>reported the (generally weak) correlation between<br>learned attention weights and various alternative tence of alternative heatmaps that yield equiva-<br>measures of feature importance, e.g., gradients. lent predictions; thus one cannot conclude that the<br>We do not intend to imply that such alternative model made a particular prediction because it at-<br>measures are necessarily ideal or that they should tended over inputs in a specific way. However,<br>be considered ‘ground truth’. While such mea- the adversarial weights themselves may be scored<br>sures do enjoy a clear intrinsic (to the model) se- as unlikely under the attention module parame-<br>mantics, their interpretation in the context of non- ters. Furthermore, it may be that multiple plausi-<br><!-- End of picture text -->

ble explanations for a particular disposition exist, and this may complicate interpretation: We would maintain that in such cases the model should highlight all plausible explanations, but one may instead view a model that provides ‘sufficient’ ex- 

linear neural networks can nonetheless be difficult for humans (Feng et al., 2018). Still, that attention consistently correlates poorly with _multiple_ such measures ought to give pause to practitioners. That said, exactly how strong such correla- 



<!-- Start of picture text -->

---

[referencia=a426845dabe2c7d6 score=0.895]
### **Algorithm 2** Permuting attention weights 

**h** _←_ Enc( **x** ), _α_ ˆ _←_ softmax( _φ_ ( **h** _,_ **Q** )) _y_ ˆ _←_ Dec( **h** _,_ ˆ _α_ ) **for** _p ←_ 1 to 100 **do** _α_<sup>_p_</sup> _←_ Permute(ˆ _α_ ) _y_ ˆ<sup>_p_</sup> _←_ Dec( **h** _, α_<sup>_p_</sup> ) _▷_ Note : **h** is not changed ∆ˆ _y_<sup>_p_</sup> _←_ TVD[ˆ _y_<sup>_p_</sup> _,_ ˆ _y_ ] **end for** ∆ˆ _y_<sup>_med_</sup> _←_ Median _p_ (∆ˆ _y_<sup>_p_</sup> ) 

Figure 6 depicts the relationship between the maximum attention value in the original _α_ ˆ and the median induced change in model output (∆ˆ _y_<sup>_med_</sup> ) across instances in the respective datasets. Colors again indicate class predictions, as above. 

We observe that there exist many points with small ∆ˆ _y_<sup>_med_</sup> despite large magnitude attention weights. These are cases in which the attention weights might suggest explaining an output by a small set of features (this is how one might reasonably read a heatmap depicting the attention weights), but where scrambling the attention makes little difference to the prediction. 

In some cases, such as predicting ICD codes from notes using the MIMIC dataset, one can see different behavior for the respective classes. For the _Diabetes_ task, e.g., attention behaves intuitively for at least the positive class; perturbing attention in this case causes large changes to the prediction. This is consistent with our preceding observations regarding Figure 4. We again conjecture that this is due to a few tokens serving as high precision indicators for the positive class; in their absence (or when they are not attended to sufficiently), the prediction drops considerably. However, this is the exception rather than the rule.

---

[referencia=a426845dabe2c7d6 score=0.889]
### **4.2.2 Adversarial Attention** 

We next propose a more focused approach to counterfactual attention weights, which we will refer to as _adversarial attention_ . The intuition is to explicitly seek out attention weights that differ as much as possible from the observed attention distribution and yet leave the prediction effectively unchanged. Such adversarial weights violate an intuitive property of explanations: shifting model attention to very different input features should yield corresponding changes in the output. Alternative attention distributions identified adversarially may then be viewed as equally plausible explanations for the same output. (A complication 



<!-- Start of picture text -->

---

[referencia=a426845dabe2c7d6 score=0.867]
to be negative. For SNLI, ■, ■, ■, code for neutral, contradiction and entailment, respectively. 

In general, observed correlations are modest (recall that a value of 0 indicates no correspondence, while 1 implies perfect concordance) for the BiLSTM model. The centrality of observed densities hovers around or below 0.5 in most of the corpora considered. On some datasets — notably the MIMIC tasks, and to a lesser extent the QA corpora — correlations are consistently significant, but they remain relatively weak. The more consistently significant correlations observed on these datasets is likely attributable to the increased length of the documents that they comprise, which in turn provide sufficiently large sample sizes to establish significant (if weak) correlation between attention weights and feature importance scores. 

Gradients for inputs in the “average” (linear projection) embedding based models show much higher correspondence with attention weights, as we would expect for these simple encoders. We hypothesize that the trouble is in the BiRNN inducing attention on the basis of hidden states, which are influenced (potentially) by all words, and then presenting the scores in reference to the original input. 

A question one might have here is how well correlated LOO and gradients are with _one another_ . We report such results in their entirety on the paper website, and we summarize their correlations relative to those realized by attention in a BiLSTM model with LOO measures in Figure 3. This reports the mean differences between (i) gradient and LOO correlations, and (ii) attention and LOO correlations. As expected, we find that these exhibit, in general, considerably higher correlation with one another (on average) than LOO does with attention scores. (The lone exception is on SNLI.) Figure 4 shows the same for gradients and attention scores; the differences are comparable. In the _ADR_ and _Diabetes_ corpora, a few high precision tokens indicate (the positive) class, and in these cases we see better agreement between LOO/gradient measures with attention; this is consistent with Figure 7 which shows that it is difficult for the BiLSTM variant to find adversarial attention distributions for _Diabetes_ . 

A potential issues with using Kendall _τ_ as our metric here is that (potentially many) irrelevant features may add noise to the correlation measures. We acknowledge that this as a shortcoming

---

[referencia=a426845dabe2c7d6 score=0.858]
## **1 Introduction and Motivation** 

_Attention mechanisms_ (Bahdanau et al., 2014) induce conditional distributions over input units to compose a weighted context vector for downstream modules. These are now a near-ubiquitous component of neural NLP architectures. Attention weights are often claimed (implicitly or explicitly) to afford insights into the “inner-workings” of models: for a given output one can inspect the inputs to which the model assigned large attention weights. Li _et al._ (2016) summarized this commonly held view in NLP: “Attention provides an important way to explain the workings of neural models". Indeed, claims that attention provides 

_after 15 minutes watching the after 15 minutes watching the movie i was asking myself what to movie i was asking myself what to do leave the theater sleep or try do leave the theater sleep or try to keep watching the movie to to keep watching the movie to see if there was anything worth i see if there was anything worth i finally watched the movie what a finally watched the movie what a waste of time maybe i am not a 5 waste of time maybe i am not a 5 years old kid anymore years old kid anymore_ original _↵_ adversarial _↵_ ˜ ˜ _f_ ( _x|↵, ✓_ ) = 0 _._ 01 _f_ ( _x|↵, ✓_ ) = 0 _._ 01 

Figure 1: Heatmap of attention weights induced over a negative movie review. We show observed model attention (left) and an adversarially constructed set of attention weights (right). Despite being quite dissimilar, these both yield effectively the same prediction (0.01). 

interpretability are common in the literature, e.g., (Xu et al., 2015; Choi et al., 2016; Lei et al., 2017; Martins and Astudillo, 2016; Xie et al., 2017; Mullenbach et al., 2018).<sup>1</sup> 

Implicit in this is the assumption that the inputs (e.g., words) accorded high attention weights are responsible for model outputs. But as far as we are aware, this assumption has not been formally evaluated. Here we empirically investigate the relationship between attention weights, inputs, and outputs.

---

[referencia=a426845dabe2c7d6 score=0.858]
We also consider the relationship between max attention weights (indicating strong emphasis on a particular feature) and the dissimilarity of identified adversarial attention weights, as measured via JSD, for adversaries that yield a prediction within _ϵ_ of the original model output. Intuitively, one might hope that if attention weights are peaky, then counterfactual attention weights that are very different but which yield equivalent predictions would be more difficult to identify. 

Figure 8 illustrates that while there is a negative trend to this effect, it is realized only weakly. Thus there exist many cases (in all datasets) in which despite a high attention weight, an alternative and quite different attention configuration over inputs yields effectively the same output. In light of this, presenting a heatmap in such a scenario that im- 



<!-- Start of picture text -->

---

[referencia=a426845dabe2c7d6 score=0.837]
## **5 Related Work** 

We have focused on attention mechanisms and the question of whether they afford transparency, but a number of interesting strategies unrelated to attention mechanisms have been recently proposed to provide insights into neural NLP models. These include approaches that measure feature importance based on gradient information (Ross et al., 2017; Sundararajan et al., 2017) (aligned with the gradient-based measures that we have used here), and methods based on _representation erasure_ (Li et al., 2016), in which dimensions are removed and then the resultant change in output is recorded (similar to our experiments with removing tokens from inputs, albeit we do this at the input layer). 

Comparing such importance measures to attention scores may provide additional insights into the working of attention based models (Ghaeini et al., 2018). Another novel line of work in this direction involves explicitly identifying explanations of black-box predictions via a causal framework (Alvarez-Melis and Jaakkola, 2017). We also note that there has been complementary work demonstrating correlation between human attention and induced attention weights, which was relatively strong when humans agreed on an explanation (Pappas and Popescu-Belis, 2016). It would be interesting to explore if such cases present explicit ‘high precision’ signals in the text (for example, the positive label in diabetes dataset). 

More specific to attention mechanisms, re- 

cent promising work has proposed more principled attention variants designed explicitly for interpretability; these may provide greater transparency by imposing _hard_ , _sparse_ attention. Such instantiations explicitly select (modest) subsets of inputs to be considered when making a prediction, which are then by construction responsible for model output (Lei et al., 2016; Peters et al., 2018). _Structured attention_ models (Kim et al., 2017) provide a generalized framework for describing and fitting attention variants with explicit probabilistic semantics. Tying attention weights to human-provided rationales is another potentially promising avenue (Bao et al., 2018). 

We hope our work motivates further development of these methods, resulting in attention variants that both improve predictive performance and provide insights into model predictions.

---

[referencia=a426845dabe2c7d6 score=0.795]
<!-- Start of picture text -->
planation as reasonable.<br>tions ‘should’ be in order to establish reliability as<br>Finally, we have limited our evaluation to tasks<br>explanation is an admittedly subjective question.<br>with unstructured output spaces, i.e., we have not<br>We also acknowledge that irrelevant features<br>considered seq2seq tasks, which we leave for fu-<br>may be contributing noise to the Kendall τ<br>ture work. However we believe interpretability is<br>measure, thus depressing this metric artificially.<br>more often a consideration in, e.g., classification<br>However, we would highlight again that atten-<br>than in translation.<br>tion weights over non-recurrent encoders exhibit<br>stronger correlations, on average, with leave-one- 7 Acknowledgements<br>out (LOO) feature importance scores than do at-<br>tention weights induced over BiLSTM outputs We thank Zachary Lipton for insightful feedback<br><!-- End of picture text -->

on a preliminary version of this manuscript. We also thank Yuval Pinter and Sarah Wiegreffe for helpful comments on previous versions of this 

(Figure 5). Furthermore, LOO and gradient-based measures correlate with one another much more strongly than do (recurrent) attention weights and 

either feature importance score. It is not clear why paper. We additionally had productive discussions either of these comparative relationships should regarding this work with Sofia Serrano and Rayhold if the poor correlation between attention and mond Mooney. feature importance scores owes solely to noise. This work was supported by the Army Research However, it remains a possibility that agreement Office (ARO), award W911NF1810328. is strong between attention weights and feature 

importance scores for the top- _k_ features only (the **References** trouble would be defining this _k_ and then measuring correlation between non-identical sets). David causal An additional limitation is that we have only black-box 

David Alvarez-Melis and Tommi Jaakkola. 2017. A causal framework for explaining the predictions of black-box sequence-to-sequence models. In _Pro-_ 

considered a handful of attention variants, selected 

_ceedings of the 2017 Conference on Empirical Meth-_ 

_ods in Natural Language Processing_ , pages 412– 421.

---

[referencia=a426845dabe2c7d6 score=0.760]
Figure 3: Mean difference in correlation of (i) LOO vs. Gradients and (ii) Attention vs. LOO scores using BiLSTM Encoder + Tanh Attention. On average the former is more correlated than the latter by _>_ 0.2 _τloo_ . 



<!-- Start of picture text -->
SST<br>IMDB<br>ADR<br>AG News<br>20 News Sports<br>Diabetes<br>Anemia<br>CNN<br>bAbI 1<br>bAbI 2<br>bAbI 3<br>SNLI<br>0.0 0.1 0.2 0.3 0.4<br>Mean Difference between Correlations<br>Dataset<br><!-- End of picture text -->

Figure 4: Mean difference in correlation of (i) LOO vs. Gradients and (ii) Attention vs. Gradients using BiLSTM Encoder + Tanh Attention. On average the former is more correlated than the latter by _∼_ 0.25 _τg_ . 



<!-- Start of picture text -->
SST<br>IMDB<br>ADR<br>AG News<br>20 News Sports<br>Diabetes<br>Anemia<br>CNN<br>bAbI 1<br>bAbI 2<br>bAbI 3<br>SNLI<br>0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7<br>Mean Difference between Correlations<br>Dataset<br><!-- End of picture text -->

Figure 5: Difference in mean correlation of attention weights vs. LOO importance measures for (i) Average (feed-forward projection) and (ii) BiLSTM Encoders with Tanh attention. Average correlation (vertical bar) is on average _∼_ 0.375 points higher for the simple feedforward encoder, indicating greater correspondence with the LOO measure. 

to be negative. For SNLI, ■, ■, ■, code for neutral, contradiction and entailment, respectively.

---

[referencia=a426845dabe2c7d6 score=0.561]
<!-- Start of picture text -->
0.5<br>0.8<br>0.20 0.4<br>0.15<br>0.6<br>0.15 0.3<br>0.10 0.4<br>0.10 0.2<br>0.05 0.1 0.2<br>0. 0 5<br>0.0 0.0<br>0.00 0. 0 0 .0 1.0 0.5 0.0 0.5 1.0 . 0 1. 0 0.5 0.0 0.5 1.0<br>1 0 1 1 0 1<br>(a) SST (BiLSTM) (b) SST (Average) (c) Diabetes (BiLSTM) (d) Diabetes (Average)<br>0 . 25<br>0.15 0.15 0.125<br>0 . 20<br>0.100<br>0.10 0 . 10 0 . 15<br>0.075<br>0 . 10<br>0.050<br>0.05 0.05<br>0 . 05 0 . 025<br>0.00 0 . 00 0 . 00 0 . 000<br>1 0 1 1 0 1 1 0 1 1 0 1<br>(e) SNLI (BiLSTM) (f) SNLI (Average) (g) CNN-QA (BiLSTM) (h) BAbI 1 (BiLSTM)<br><!-- End of picture text -->

Figure 2: Histogram of **Kendall** _τ_ between attention and gradients. Encoder variants are denoted parenthetically; colors indicate predicted classes. Exhaustive results are available for perusal online. 



<!-- Start of picture text -->
SST<br>IMDB<br>ADR<br>AG News<br>20 News Sports<br>Diabetes<br>Anemia<br>CNN<br>bAbI 1<br>bAbI 2<br>bAbI 3<br>SNLI<br>0.1 0.0 0.1 0.2 0.3 0.4<br>Mean Difference between Correlations<br>Dataset<br><!-- End of picture text -->

---

[referencia=a426845dabe2c7d6 score=0.448]
|bAbI 2|Overall|0_._17_±_0_._12|0_._57|0_._84_±_0_._09|1_._00|0_._11_±_0_._13|0_._40|
|bAbI 3|Overall|0_._30_±_0_._11|0_._93|0_._76_±_0_._12|1_._00|0_._31_±_0_._11|0_._94|
|SNLI|0|0_._36_±_0_._22|0_._46|0_._54_±_0_._20|0_._76|0_._44_±_0_._18|0_._60|
||1|0_._42_±_0_._19|0_._57|0_._59_±_0_._18|0_._84|0_._43_±_0_._17|0_._59|
||2|0_._40_±_0_._20|0_._52|0_._53_±_0_._19|0_._75|0_._44_±_0_._17|0_._61|



Table 2: Mean and std. dev. of correlations between gradient/leave-one-out importance measures and attention weights. _Sig. Frac._ columns report the fraction of instances for which this correlation is statistically significant; note that this largely depends on input length, as correlation does tend to exist, just weakly. Encoders are denoted parenthetically. These are representative results; exhaustive results for all encoders are available to browse online. 



<!-- Start of picture text -->