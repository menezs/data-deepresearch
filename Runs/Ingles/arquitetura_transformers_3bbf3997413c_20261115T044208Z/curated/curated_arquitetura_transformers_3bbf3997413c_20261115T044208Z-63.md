[referencia=85f66a6419d173a7 score=0.640]
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

[referencia=85f66a6419d173a7 score=0.631]
that in fact we could train more efficiently<sup>6</sup> by training at the batch size _B_ crit discussed in Section 5.1. Large and small values of the loss could have been achieved with fewer samples or fewer steps, respectively, and correcting for this inefficiency by standardizing to the critical batch size results in cleaner and more predictable trends. 

In this section we will adjust for this oversight. More importantly, we will use the results of Section 5 to determine the optimal _allocation_ of compute between model size _N_ and the quantity of data processed during training, namely 2 _B_ crit _S_ min. We will determine this allocation both empirically and theoretically, by using the equation for _L_ ( _N, S_ min), and we will demonstrate that these methods agree.

---

[referencia=85f66a6419d173a7 score=0.436]
#### can be fit very well with a power-law 

_N_ ( _C_ min) _∝_ ( _C_ min)<sup>0</sup><sup>_._73</sup> _._ (6.1) In Figure 12, we show the effect of training models of sub-optimal sizes (see Appendix B.4). By definition _C_ min _≡_ 6 _NB_ crit _S_ , and so we can use _N_ ( _C_ min) to extract further results. In particular, since prior fits show _B ∝ L_<sup>_−_4</sup><sup>_._8</sup> and _L ∝ C_ min<sup>_−_0</sup><sup>_._05</sup> , we can conclude that _B_ crit _∝ C_ min<sup>0</sup><sup>_._24.This leads us to conclude</sup> that the optimal number of steps will only grow very slowly with compute, as _S_ min _∝_ ( _C_ min)<sup>0</sup><sup>_._03</sup> _,_ (6.2) matching the empirical results in Figure 14. In fact the measured exponent is sufficiently small that our results may even be consistent with an exponent of zero. Thus we conclude that as we scale up language modeling with an optimal allocation of computation, we should predominantly increase the model size _N_ , while simultaneously scaling up the batch size via _B ∝ B_ crit with negligible increase in the number of serial steps. Since compute-efficient training uses relatively few optimization steps, additional work on speeding up early training dynamics may be warranted. 

**6.2 Predictions from** _L_ ( _N, S_ min) 

The results for _L_ ( _C_ min) and the allocations can be predicted from the _L_ ( _N, S_ min) equation obtained in Section 5. Given our equation for _L_ ( _N, S_ min), we can substitute _S_ min =<sup>_<u>C</u>_</sup> 6 _NB_<sup><u>min</u>and then find the minimum</sup> of the loss as a function of _N_ , while fixing the training compute. We carry out this procedure in detail in Appendix B, where we also provide some additional predictions.

---

[referencia=85f66a6419d173a7 score=0.414]
### **8 Discussion** 

We have observed consistent scalings of language model log-likelihood loss with non-embedding parameter count _N_ , dataset size _D_ , and optimized training computation _C_ min, as encapsulated in Equations (1.5) and (1.6). Conversely, we find very weak dependence on many architectural and optimization hyperparameters. Since scalings with _N, D, C_ min are power-laws, there are diminishing returns with increasing scale. 

> 7Defining words using the `wc` utility, the WebText2 dataset has 1 _._ 4 tokens per word and 4 _._ 3 characters per token. 

> 8After this work was completed, [RRBS19a] also appeared, which makes similar predictions for the dependence of loss on both model and dataset size. 

18 

We were able to precisely model the dependence of the loss on _N_ and _D_ , and alternatively on _N_ and _S_ , when these parameters are varied simultaneously. We used these relations to derive the compute scaling, magnitude of overfitting, early stopping step, and data requirements when training large language models. So our scaling relations go beyond mere observation to provide a predictive framework. One might interpret these relations as analogues of the ideal gas law, which relates the macroscopic properties of a gas in a universal way, independent of most of the details of its microscopic consituents. 

It is natural to conjecture that the scaling relations will apply to other generative modeling tasks with a maximum likelihood loss, and perhaps in other settings as well. To this purpose, it will be interesting to test these relations on other domains, such as images, audio, and video models, and perhaps also for random network distillation. At this point we do not know which of our results depend on the structure of natural language data, and which are universal. It would also be exciting to find a theoretical framework from which the scaling relations can be derived: a ‘statistical mechanics’ underlying the ‘thermodynamics’ we have observed. Such a theory might make it possible to derive other more precise predictions, and provide a systematic understanding of the limitations of the scaling laws.

---

[referencia=85f66a6419d173a7 score=0.394]
3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->
Li ne  color indicates<br>Test Loss 10 10 nu m ber of parameters<br>10 3 10 6 10 9<br>8 8<br>10 3  Params<br>6 6<br>Co m pute-efficient<br>10 9  Params trai n ing stops far<br>sh o rt of convergence<br>4 4<br>10 7 10 9 10 11 1 0 -9 1 0 -6 1 0 -3 10 0<br>Tokens Processed Compute (PF-days)<br><!-- End of picture text -->

**Figure 2** We show a series of language model training runs, with models ranging in size from 10<sup>3</sup> to 10<sup>9</sup> parameters (excluding embeddings). 



<!-- Start of picture text -->
Minimum serial steps  Data requirements<br>increases negligibly grow relatively slowly<br>Optimal model size<br>increases very quickly<br>>1,000,000x Model Size<br>100x Batch Size<br><10x Serial Steps<br><!-- End of picture text -->

**Figure 3** As more compute becomes available, we can choose how much to allocate towards training larger models, using larger batches, and training for more steps. We illustrate this for a billion-fold increase in compute. For optimally compute-efficient training, most of the increase should go towards increased model size. A relatively small increase in data is needed to avoid reuse. Of the increase in data, most can be used to increase parallelism through larger batch sizes, with only a very small increase in serial training time required.

---

[referencia=85f66a6419d173a7 score=0.377]
**Transfer improves with test performance:** When we evaluate models on text with a different distribution than they were trained on, the results are strongly correlated to those on the training validation set with a roughly constant offset in the loss – in other words, transfer to a different distribution incurs a constant penalty but otherwise improves roughly in line with performance on the training set. (Section 3.2.2) 

**Sample efficiency:** Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4). 

**Convergence is inefficient:** When working within a fixed compute budget _C_ but without any other restrictions on the model size _N_ or available data _D_ , we attain optimal performance by training _very large models_ and stopping _significantly short of convergence_ (see Figure 3). Maximally compute-efficient training would therefore be far more sample efficient than one might expect based on training small models to convergence, with data requirements growing very slowly as _D ∼ C_<sup>0</sup><sup>_._27</sup> with training compute. (Section 6) 

**Optimal batch size:** The ideal batch size for training these models is roughly a power of the loss only, and continues to be determinable by measuring the gradient noise scale [MKAT18]; it is roughly 1-2 million tokens at convergence for the largest models we can train. (Section 5.1) 

Taken together, these results show that language modeling performance improves smoothly and predictably as we appropriately scale up model size, data, and compute. We expect that larger language models will perform better and be more sample efficient than current models. 

3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.297]
### **7 Related Work** 

Power laws can arise from a wide variety of sources [THK18]. Power-law scalings with model and dataset size in density estimation [Was06] and in random forest models [Bia12] may be connected with our results. These models suggest that power-law exponents may have a very rough interpretation as the inverse of the number of relevant features in the data. 

Some early [BB01, Goo01] work found power-law scalings between performance and dataset size. More recent work [HNA<sup>+</sup> 17, HAD19] also investigated scaling between model size and data size; their work is perhaps the closest to ours in the literature<sup>8</sup> . Note, however, that [HNA<sup>+</sup> 17] found super-linear scaling of dataset size with model size, whereas we find a sub-linear scaling. There are some parallels between our findings on optimal allocation of compute and [Kom19], including power-law learning curves. EfficientNets [TL19] also appear to obey an approximate power-law relation between accuracy and model size. Very recent work [RRBS19b] studies scaling with both dataset size and model size for a variety of datasets, and fits an ansatz similar to ours. 

EfficientNet [TL19] advocates scaling depth and width exponentially (with different coefficients) for optimal performance of image models, resulting in a power-law scaling of width as a function of depth. We find that for language models this power should be roughly one when scaling up (as width/depth should remain fixed). But more importantly, we find that the precise architectural hyperparameters are unimportant compared to the overall scale of the language model. In [VWB16] it was argued that deep models can function as ensembles of shallower models, which could potentially explain this finding. Earlier work [ZK16] has compared width and depth, and found that wide ResNets can outperform deep ResNets on image classification. Some studies fix computation per data example, which tends to scale in proportion to the number of model parameters, whereas we investigate scaling with both model size and the quantity of training computation.

---

[referencia=85f66a6419d173a7 score=0.249]
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

[referencia=85f66a6419d173a7 score=0.216]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=85f66a6419d173a7 score=0.182]
### **6 Optimal Allocation of the Compute Budget** 

We displayed the _empirical_ trend of performance as a function of the computation used during training in the top-right of Figure 1. However, this result involved training at a fixed batch size _B_ , whereas we know 

14 



<!-- Start of picture text -->
Smaller models require<br>more steps to train, while<br>larger models require fewer<br>Models between 0.6x and 2.2x the<br>optimal size can be trained with a<br>20% larger compute budget<br>Our framework does not<br>capture early training dynamics<br><!-- End of picture text -->

**Figure 12 Left:** Given a fixed compute budget, a particular model size is optimal, though somewhat larger or smaller models can be trained with minimal additional compute. **Right:** Models larger than the computeefficient size require fewer steps to train, allowing for potentially faster training if sufficient additional parallelism is possible. Note that this equation should not be trusted for very large models, as it is only valid in the power-law region of the learning curve, after initial transient effects. 



<!-- Start of picture text -->
7 L = (Cmin/2.3 10 8 ) 0.050<br>6 L = (C/2.0 10 7 ) 0.057<br>5<br>4<br>3<br>2<br>10 8 10 6 10 4 10 2 10 0<br>Compute (PF-days), non-embedding<br>Test Loss<br><!-- End of picture text -->

**Figure 13** When adjusting performance to simulate training far below the critical batch size, we find a somewhat altered power law for _L_ ( _C_ min) when compared with the fully empirical results. The conspicuous lump at 10<sup>_−_5</sup> PF-days marks the transition from 1-layer to 2-layer networks; we exclude 1-layer networks in the power-law fits. It is the _L_ ( _C_ min) trend that we expect to provide a reliable extrapolation for larger compute.

---

[referencia=85f66a6419d173a7 score=0.167]
7 5.0<br>WebText2 (Test) Books during training<br>6 Internet Books 4.5 Wikipedia during training<br>Books Books at convergence<br>5 Wikipedia 4.0 Wikipedia at convergence<br>Common Crawl<br>3.5<br>4<br>3.0<br>3<br>2.5<br>10 4 10 5 10 6 10 7 10 8 10 9 5.0 4.5 4.0 3.5 3.0 2.5<br>Parameters (non-embedding) Test Loss on Training Distribution<br>Figure 8 Left: Generalization performance to other data distributions improves smoothly with model size,<br>with only a small and very slowly growing offset from the WebText2 training distribution. Right: Gener-<br>alization performance depends only on training distribution performance, and not on the phase of training.<br>We compare generalization of converged models (points) to that of a single large model (dashed curves) as it<br>trains.<br>with the best performance on step S = 6 BSC . Note that in these results the batch size B remains fixed for<br>all models , which means that these empirical results are not truly optimal. We will account for this in later<br>sections using an adjusted  C min to produce cleaner trends.<br>The result appears as the heavy black line on the left-hand plot in Figure 1. It can be fit with<br>L ( C )  ≈ Cc αC (3.3)<br>� C �<br>The figure also includes images of individual learning curves to clarify when individual models are optimal.<br>We will study the optimal allocation of compute more closely later on. The data strongly suggests that sample<br>efficiency improves with model size, and we also illustrate this directly in Figure 19 in the appendix.<br>4 Charting the Infinite Data Limit and Overfitting<br>In Section 3 we found a number of basic scaling laws for language modeling performance. Here we will<br>study the performance of a model of size N trained on a dataset with D tokens while varying N and D<br>simultaneously. We will empirically demonstrate that the optimally trained test loss accords with the scaling<br>law of Equation (1.5). This provides guidance on how much data we would need to train models of increasing<br>

---

[referencia=85f66a6419d173a7 score=0.126]
#### **B.2 Efficient Training** 

Now we assemble the implications of (B.3) and (B.4). First, note that inserting (B.4) into (B.3) yields 



which implies that for compute-efficient training, we should train to a **fixed percentage**<sup>_<u>α</u>_</sup> _α_<sup>_<u>N</u>_</sup> _S_<sup>_≈_10%above</sup> the converged loss. Next, let’s determine how the optimal loss depends on the compute budget. Eliminating _N_ yields a power-law dependence of performance on compute: 





Similarly, we can eliminate _L_ to find _N_ ( _C_ ): 

and 



> 9There is a slight ambiguity here: we can imagine training either at a constant batch size _B_ ( _L_ target), or we could instead train at a variable batch size _B_<sup>˜</sup> ( _L_ ), where _B_<sup>˜</sup> is the instantaneous critical batch size (as opposed to _B_ , which is the averaged version). These two prescriptions result in the same number of steps, so we can ignore this subtlety (see [MKAT18]). 

21 

#### **B.3 Comparison to Inefficient** 

Typically, researchers train models until they appear to be close to convergence. In this section, we compare the efficient training procedure described above to this more typical setup. We define a the convergence factor _f_ as the percent deviation from the converged loss: 



For compute-efficient training we have _f_ = _αN /αS ≈_ 10% from the previous section, but researchers typically use a much smaller value. Here, we choose _f_<sup>_′_</sup> = 2% as an estimate. For a fixed value of the loss, we predict: 



So that compute-efficient training uses 7.7x fewer parameter updates, 2.7x more parameters, and 65% less compute to reach the same loss.

---

[referencia=85f66a6419d173a7 score=0.120]
# **Appendices** 

|**A**<br>**Summary of**|**Power**|**Laws**|||
|---|---|---|---|---|
|For easier reference, w|e provid|e a summary|below of the k|ey trends described throughout the paper.|
|**Parameters**|**Data**|**Compute**|**Batch Size**|**Equation**|
|_N_|_∞_|_∞_|Fixed|_L_(_N_) = (_N_c_/N_)<sup>_αN_</sup>|
|_∞_|_D_|Early Stop|Fixed|_L_(_D_) = (_D_c_/D_)<sup>_αD_</sup>|
|Optimal|_∞_|_C_|Fixed|_L_(_C_) = (_C_c_/C_)<sup>_αC_ </sup>(naive)|
|_N_opt|_D_opt|_C_min|_B ≪B_crit|_L_(_C_min) =<br>�<br>_C_<sup>min</sup><br>c<br>_/C_min<br>�_α_<sup>min</sup><br>_C_<br><br>|
|_N_|_D_|Early Stop|Fixed|_L_(_N, D_) =<br>��_N_c<br>_N_<br>�<sup>_αN_</sup><br>_αD_ + _Dc_<br>_D_<br>�_~~α~~D_|
|_N_|_∞_|_S_ steps|_B_<br>**Table 4**|_L_(_N, S_) =<br>�_N_c<br>_N_<br>�_αN_ +<br>�<br>_S_c<br>_S_min(_S,B_)<br>�_~~α~~S_|



The empirical fitted values for these trends are: 

**Power Law Scale (tokenization-dependent)** _αN_ = 0 _._ 076 _N_ c = 8 _._ 8 _×_ 10<sup>13</sup> params (non-embed)

---

[referencia=85f66a6419d173a7 score=0.107]
This is the maximum rate at which the dataset size can productively grow with compute, since it means that we are only training for a single epoch. But it grows the dataset much more slowly than in Equation (6.6). It appears to imply that compute-efficient training will eventually run into a problem with overfitting, even if the training process never re-uses any data! 

According to Figure 1, we expect that when we are bottlenecked by the dataset size (ie by overfitting), the loss should scale as _L_ ( _D_ ) _∝ D_<sup>_−_0</sup><sup>_._095</sup> . This implies that the loss would scale with compute as _L_ ( _D_ ( _C_ min)) _∝ C_ min<sup>_−_0</sup><sup>_._03</sup> once we are data-limited. Once again, we have a contradiction, as this will eventually intersect with our prediction for _L_ ( _C_ min) from Figure 13, where we found a scaling _L_ ( _C_ min) _∝ C_ min<sup>_−_0</sup><sup>_._050</sup> . The intersection point of _L_ ( _D_ ( _C_ min)) and _L_ ( _C_ min) occurs at 

_C_<sup>_∗_</sup> _∼_ 10<sup>4</sup> PF-Days _N_<sup>_∗_</sup> _∼_ 10<sup>12</sup> parameters _, D_<sup>_∗_</sup> _∼_ 10<sup>12</sup> tokens _, L_<sup>_∗_</sup> _∼_ 1 _._ 7 nats/token (6.8) though the numerical values are highly uncertain, varying by an order or magnitude in either direction depending on the precise values of the exponents from the power-law fits. The most obvious interpretation is that our scaling laws break down at or before we reach this point, which is still many orders of magnitude away in both compute and model size. 

17

---

[referencia=85f66a6419d173a7 score=0.103]
Various works [AS17, BHMM18] have investigated generalization in highly overparameterized models, finding a “jamming transition” [GJS<sup>+</sup> 19] when the model size reaches the dataset size (this may require training many orders of magnitude beyond typical practice, and in particular does not use early stopping). We do not observe such a transition, and find that the necessary training data scales sublinearly in the model size. Expansions in the model size, particularly at large width [JGH18, LXS<sup>+</sup> 19], may provide a useful framework for thinking about some of our scaling relations. Our results on optimization, such as the shape of learning curves, can likely be explained using a noisy quadratic model, which can provide quite accurate predictions [ZLN<sup>+</sup> 19] in realistic settings. Making this connection quantitative will require a characterization of the Hessian spectrum [Pap18, GKX19, GARD18].

---

[referencia=85f66a6419d173a7 score=0.098]
<br>as a function of model size is shown in Figure 8; in all cases the models were trained only on the WebText2<br>dataset. We see that the loss on these other data distributions improves smoothly with model size, in direct<br>parallel with the improvement on WebText2. We find that generalization depends almost exclusively on the<br>in-distribution validation loss, and does not depend on the duration of training or proximity to convergence.<br>We also observe no dependence on model depth (see Appendix D.8).<br><!-- End of picture text -->



<!-- Start of picture text -->
3.3 Performance with Dataset Size and Compute<br>We display empirical trends for the test loss as a function of dataset size  D  (in tokens) and training compute<br>C in Figure 1.<br>For the trend with  D  we trained a model with ( n layer , n embd) = (36 ,  1280) on fixed subsets of the WebText2<br>dataset. We stopped training once the test loss ceased to decrease. We see that the resulting test losses can be<br>fit with simple power-law<br>L ( D )  ≈ Dc αD (3.2)<br>� D �<br>in the dataset size. The data and fit appear in Figure 1.<br><!-- End of picture text -->

The total amount of non-embedding compute used during training can be estimated as _C_ = 6 _NBS_ , where _B_ is the batch size, _S_ is the number of parameter updates, and the factor of 6 accounts for the forward and backward passes. Thus for a given value of _C_ we can scan over all models with various _N_ to find the model 

9 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.082]
|1|Summary of simple power laws. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
|---|---|---|
|2|Illustration of sample effciency and compute effciency. . . . . . . . . . . . . . . . . . . . .|4|
|3|How to scale up model size, batch size, and serial steps . . . . . . . . . . . . . . . . . . . .|4|
|4|Performance when varying model and data size, or model and training steps, simultaneously|5|
|5|Weak dependence of performance on hyperparameter tuning . . . . . . . . . . . . . . . . .|8|
|6|Comparison of performance trend when including or excluding embeddings . . . . . . . . .|8|
|7|LSTM and Transformer performance comparison . . . . . . . . . . . . . . . . . . . . . . .|9|
|8|Generalization to other test datasets<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
|9|Universality of overftting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
|10|Critical batch size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
|11|Performance versus compute budget or number of parameter updates . . . . . . . . . . . . .|14|
|12|Training on suboptimal models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|15|
|13|Comparison between empirical and adjusted compute trends . . . . . . . . . . . . . . . . .|15|

---

[referencia=85f66a6419d173a7 score=0.082]
**Figure 23** The trend for performance as a function of parameter count, _L_ ( _N_ ), is fit better by a power law than by other functions such as a logarithm at a qualitative level. 

schedules appear to be statistical noise, and provide a rough gauge for the scale of variation between different training runs. Experiments on larger models suggest that the variation in the final test loss between different random seeds is roughly constant in magnitude for different model sizes. 

We found that larger models require a smaller learning rate to prevent divergence, while smaller models can tolerate a larger learning rate. To implement this, the following rule of thumb was used for most runs: 

LR( _N_ ) _≈_ 0 _._ 003239 + _−_ 0 _._ 0001395 log( _N_ ) (D.1) 

We expect that this formula could be improved. There may be a dependence on network width, likely set by the initialization scale. The formula also breaks down for _N >_ 10<sup>10</sup> parameters. Nevertheless, we found that it works sufficiently well for the models we considered. 

#### **D.7 Fit Details and Power Law Quality** 

We experimented with a number of functional forms for the fits to _L_ ( _N_ ) _, L_ ( _C_ ), and _L_ ( _D_ ); the power-law fits were qualitatively much more accurate than other functions such as logarithms (see Figure 23). 

For _L_ ( _C_ ), we do not include small models with only 1 layer in the fit, as the transition from 1 to 2 layers causes a noticable lump in the data. For _L_ ( _N_ ) we also do not include very small models with only 1 layer in the fit, and we exclude the largest models that have not trained fully to convergence. Fit parameters change marginally if we do include them, and the trend extrapolates well in both directions regardless.

---

[referencia=85f66a6419d173a7 score=0.081]
For the loss as a function of training compute, we predict that _L_ ( _C_ min) = _Cc_ min _α_<sup>min</sup> _C_ (6.3) � _C_ min � where 

1 _αC_<sup>min</sup> _≡_ 1 _/αS_ + 1 _/αB_ + 1 _/αN ≈_ 0 _._ 054 (6.4) 

in excellent agreement with the exponent of Figure 13. We also predict that 

_N_ ( _C_ min) _∝_ ( _C_ min)<sup>_α_</sup> _C_<sup>min</sup> _/αN ≈_ ( _C_ min)0 _._ 71 (6.5) 

which also matches the scaling of Figure 14 to within a few percent. Our scaling laws provide a predictive framework for the performance of language modeling. 

16 



|The intersection point is sensitive to|
|---|
|the precise power-law parameters|



**Figure 15** Far beyond the model sizes we study empirically, we find a contradiction between our equations for _L_ ( _C_ min) and _L_ ( _D_ ) due to the slow growth of data needed for compute-efficient training. The intersection marks the point before which we expect our predictions to break down. The location of this point is highly sensitive to the precise exponents from our power-law fits.

---

[referencia=85f66a6419d173a7 score=0.067]
#### **6.3 Contradictions and a Conjecture** 

We observe no signs of deviation from straight power-law trends at large values of compute, data, or model size. Our trends must eventually level off, though, since natural language has non-zero entropy. Indeed, the trends for compute-efficient training described in this section already contain an apparent contradiction. At scales several orders of magnitude above those documented here, the performance predicted by the _L_ ( _C_ min) scaling law decreases below what should be possible given the slow growth in training data with compute. This implies that our scaling laws must break down before this point, but we conjecture that the intersection point has a deeper meaning: it provides an estimate of the point at which Transformer language models reach maximal performance. 

Since the amount of data used by compute-efficient training grows slowly with the compute budget, the performance predicted by _L_ ( _C_ min) eventually hits a lower bound set by the _L_ ( _D_ ) power law (see Figure 15). Let us work this out in more detail. 

To keep overfitting under control, the results of Section 4 imply that we should scale the dataset size as 

_D ∝ N_<sup>0</sup><sup>_._74</sup> _∝ C_ min<sup>0</sup><sup>_._54</sup> (6.6) 

where we have used the compute-efficient _N_ ( _C_ min) from Figure 14. Let us compare this to the data requirements of compute-efficient training. If we train at the critical batch size (i.e. _C_ = 2 _C_ min) and never re-use data during training, we find that data usage grows with compute as 

2 _C_ min _D_ ( _C_ min) = �4 _×_ 10<sup>10</sup> tokens� ( _C_ min _/_ PF-Day)<sup>0</sup><sup>_._26</sup> (6.7) 6 _N_ ( _C_ min)<sup>_≈_</sup>