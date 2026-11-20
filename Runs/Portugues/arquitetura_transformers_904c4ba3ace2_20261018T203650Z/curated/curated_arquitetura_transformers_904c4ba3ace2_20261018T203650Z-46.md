[referencia=85f66a6419d173a7 score=0.981]
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

[referencia=85f66a6419d173a7 score=0.837]
According to Figure 1, we expect that when we are bottlenecked by the dataset size (ie by overfitting), the loss should scale as _L_ ( _D_ ) _∝ D_<sup>_−_0</sup><sup>_._095</sup> . This implies that the loss would scale with compute as _L_ ( _D_ ( _C_ min)) _∝ C_ min<sup>_−_0</sup><sup>_._03</sup> once we are data-limited. Once again, we have a contradiction, as this will eventually intersect with our prediction for _L_ ( _C_ min) from Figure 13, where we found a scaling _L_ ( _C_ min) _∝ C_ min<sup>_−_0</sup><sup>_._050</sup> . 

The intersection point of _L_ ( _D_ ( _C_ min)) and _L_ ( _C_ min) occurs at 

_C_<sup>_∗_</sup> _∼_ 10<sup>4</sup> PF-Days _N_<sup>_∗_</sup> _∼_ 10<sup>12</sup> parameters _, D_<sup>_∗_</sup> _∼_ 10<sup>12</sup> tokens _, L_<sup>_∗_</sup> _∼_ 1 _._ 7 nats/token (6.8) 

though the numerical values are highly uncertain, varying by an order or magnitude in either direction depending on the precise values of the exponents from the power-law fits. The most obvious interpretation is that our scaling laws break down at or before we reach this point, which is still many orders of magnitude away in both compute and model size. 

17

---

[referencia=85f66a6419d173a7 score=0.772]
#### **6.3 Contradictions and a Conjecture** 

We observe no signs of deviation from straight power-law trends at large values of compute, data, or model size. Our trends must eventually level off, though, since natural language has non-zero entropy. 

Indeed, the trends for compute-efficient training described in this section already contain an apparent contradiction. At scales several orders of magnitude above those documented here, the performance predicted by the _L_ ( _C_ min) scaling law decreases below what should be possible given the slow growth in training data with compute. This implies that our scaling laws must break down before this point, but we conjecture that the intersection point has a deeper meaning: it provides an estimate of the point at which Transformer language models reach maximal performance. 

Since the amount of data used by compute-efficient training grows slowly with the compute budget, the performance predicted by _L_ ( _C_ min) eventually hits a lower bound set by the _L_ ( _D_ ) power law (see Figure 15). Let us work this out in more detail. 

To keep overfitting under control, the results of Section 4 imply that we should scale the dataset size as 



where we have used the compute-efficient _N_ ( _C_ min) from Figure 14. 

Let us compare this to the data requirements of compute-efficient training. If we train at the critical batch size (i.e. _C_ = 2 _C_ min) and never re-use data during training, we find that data usage grows with compute as 



This is the maximum rate at which the dataset size can productively grow with compute, since it means that we are only training for a single epoch. But it grows the dataset much more slowly than in Equation (6.6). It appears to imply that compute-efficient training will eventually run into a problem with overfitting, even if the training process never re-uses any data!

---

[referencia=85f66a6419d173a7 score=0.698]
- **1.2 Summary of Scaling Laws** 

- The test loss of a Transformer trained to autoregressively model language can be predicted using a power-law when performance is limited by only either the number of non-embedding parameters _N_ , the dataset size _D_ , or the optimally allocated compute budget _C_ min (see Figure 1): 

   1. For models with a limited number of parameters, trained to convergence on sufficiently large datasets: _L_ ( _N_ ) = ( _N_ c _/N_ )<sup>_αN_</sup> ; _αN ∼_ 0 _._ 076 _, N_ c _∼_ 8 _._ 8 _×_ 10<sup>13</sup> (non-embedding parameters) (1.1) 

   2. For large models trained with a limited dataset with early stopping: 

_L_ ( _D_ ) = ( _D_ c _/D_ )<sup>_αD_</sup> ; _αD ∼_ 0 _._ 095 _, D_ c _∼_ 5 _._ 4 _×_ 10<sup>13</sup> (tokens) (1.2) 3. When training with a limited amount of compute, a sufficiently large dataset, an optimally-sized model, and a sufficiently small batch size (making optimal<sup>3</sup> use of compute): _L_ ( _C_ min) = <u>�</u> _C_ c<sup>min</sup> _/C_ min� _α_<sup>min</sup> _C_ ; _αC_<sup>min</sup> _∼_ 0 _._ 050 _, C_ c<sup>min</sup> _∼_ 3 _._ 1 _×_ 10<sup>8</sup> (PF-days) (1.3) 

> 3We also observe an empirical power-law trend with the training compute _C_ (Figure 1) while training at fixed batch size, but it is the trend with _C_ min that should be used to make predictions. They are related by equation (5.5). 

4 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.687]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=85f66a6419d173a7 score=0.675]
### **1 Introduction** 

Language provides a natural domain for the study of artificial intelligence, as the vast majority of reasoning tasks can be efficiently expressed and evaluated in language, and the world’s text provides a wealth of data for unsupervised learning via generative modeling. Deep learning has recently seen rapid progress in language modeling, with state of the art models [RNSS18, DCLT18, YDY<sup>+</sup> 19, LOG<sup>+</sup> 19, RSR<sup>+</sup> 19] approaching human-level performance on many specific tasks [WPN<sup>+</sup> 19], including the composition of coherent multiparagraph prompted text samples [RWC<sup>+</sup> 19]. 

One might expect language modeling performance to depend on model architecture, the size of neural models, the computing power used to train them, and the data available for this training process. In this work we will empirically investigate the dependence of language modeling loss on all of these factors, focusing on the Transformer architecture [VSP<sup>+</sup> 17, LSP<sup>+</sup> 18]. The high ceiling and low floor for performance on language tasks allows us to study trends over more than seven orders of magnitude in scale. 

Throughout we will observe precise power-law scalings for performance as a function of training time, context length, dataset size, model size, and compute budget.

---

[referencia=85f66a6419d173a7 score=0.618]
4 



<!-- Start of picture text -->
Loss vs Model and Dataset Size Loss vs Model Size and Training Steps<br>4.4<br>4.5<br>4.0<br>4.0 Params 10 8<br>708M 3.6<br>3.5 302M<br>85M3M 3.2 10 7<br>3.0 25M<br>393.2K 2.8<br>10 6<br>2.5<br>2.4<br>10 7 10 8 10 9 10 10 10 4 10 5<br>Tokens in Dataset Estimated Smin<br>Loss Loss<br>Parameters (non-embed)<br><!-- End of picture text -->

**Figure 4 Left** : The early-stopped test loss _L_ ( _N, D_ ) varies predictably with the dataset size _D_ and model size _N_ according to Equation (1.5). **Right** : After an initial transient period, learning curves for all model sizes _N_ can be fit with Equation (1.6), which is parameterized in terms of _S_ min, the number of steps when training at large batch size (details in Section 5.1). 

These relations hold across eight orders of magnitude in _C_ min, six orders of magnitude in _N_ , and over two orders of magnitude in _D_ . They depend very weakly on model shape and other Transformer hyperparameters (depth, width, number of self-attention heads), with specific numerical values associated with the Webtext2 training set [RWC<sup>+</sup> 19]. The power laws _α_ N _, α_ D _, αC_<sup>min</sup> specify the degree of performance improvement expected as we scale up _N_ , _D_ , or _C_ min; for example, doubling the number of parameters yields a loss that is smaller by a factor 2<sup>_−αN_</sup> = 0 _._ 95. The precise numerical values of _N_ c _, C_ c<sup>min</sup> _,_ and _D_ c depend on the vocabulary size and tokenization and hence do not have a fundamental meaning.

---

[referencia=85f66a6419d173a7 score=0.617]
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

[referencia=85f66a6419d173a7 score=0.604]
11 



<!-- Start of picture text -->
Critical Batch Size vs. Performance<br>10 6<br>10 5<br>Empirical Bcrit, N = 3M<br>10 4<br>Empirical Bcrit, N = 85M<br>Bcrit = 2.1 × 10 8 tokens L 4.8<br>Noise Scale Measurement<br>10 3<br>10 1 6 × 10 0 4 × 10 0 3 × 10 0<br>WebText2 Train Loss<br>Critical Batch Size (Tokens)<br><!-- End of picture text -->

**Figure 10** The critical batch size _B_ crit follows a power law in the loss as performance increase, and does not depend directly on the model size. We find that the critical batch size approximately doubles for every 13% decrease in loss. _B_ crit is measured empirically from the data shown in Figure 18, but it is also roughly predicted by the gradient noise scale, as in [MKAT18]. 

defining 



and studying it as a function of _N, D_ . In fact, we see empirically that _δL_ depends only a specific combination of _N_ and _D_ , as shown in Figure 16. This follows from the scaling law of Equation (1.5), which implies 



Note that at large _D_ this formula also has a series expansion in powers of 1 _/D_ . 

We estimate that the variation in the loss with different random seeds is roughly 0 _._ 02, which means that to avoid overfitting when training to within that threshold of convergence we require 



With this relation, models smaller than 10<sup>9</sup> parameters can be trained with minimal overfitting on the 22B token WebText2 dataset, but our largest models will encounter some mild overfitting. More generally, this relation shows that dataset size may grow sub-linearly in model size while avoiding overfitting. Note however that this does not typically represent maximally compute-efficient training. We should also emphasize that we have not optimized regularization (eg the dropout probability) while varying dataset and model size.

---

[referencia=85f66a6419d173a7 score=0.554]
### **5 Scaling Laws with Model Size and Training Time** 

In this section we will demonstrate that a simple scaling law provides a good description for the loss as a function of model size _N_ and training time. First we will explain how to use the results of [MKAT18] to define a universal training step _S_ min, which accounts for the fact that most of our models have not been trained at an optimal batch size. Then we will demonstrate that we can fit the model size and training time dependence of the loss using Equation (1.6). Later we will use these results to predict the optimal allocation of training compute between model size and training time, and then confirm that prediction.

---

[referencia=85f66a6419d173a7 score=0.532]
### **C Caveats** 

In this section we list some potential caveats to our analysis. 

> _•_ At present we do not have a solid theoretical understanding for any of our proposed scaling laws. The scaling relations with model size and compute are especially mysterious. It may be possible to understand scaling at very large _D_ holding model size fixed [AS17], and also the shape of learning curves late in training, by modeling the loss with a noisy quadratic. But the scaling with _D_ at very large model size still remains mysterious. Without a theory or a systematic understanding of the corrections to our scaling laws, it’s difficult to determine in what circumstances they can be trusted. 

22 



<!-- Start of picture text -->
6<br>Test Loss 10 10<br>Early Stopping Step 5 Train Loss<br>10 5 Data Size21M 4 10 9<br>43M<br>86M<br>10 4 172M344M 3<br>688M 10 8<br>1.4B<br>2<br>10 3<br>10 3 10 4 10 5 10 3 10 4 10 5<br>Sc × [L(N, D) L(N, )] 1/ S Step<br>Loss<br>stop<br>S<br>Dataset Size (Tokens)<br><!-- End of picture text -->

**Figure 16 Left:** We characterize the step on which early stopping occurs, as a function of the extent of overfitting. The red line indicates a lower bound for early stopping that is derived in Section 5.3. **Right:** We display train and test loss for a series of 300M parameter models trained on different sized dataset subsamples. The test loss typically follows that of a run done with unrestricted data until diverging. Note that the degree of overfitting (as compared to the infinite data limit) is significantly overestimated by _L_ test _− L_ train (denoted by a black bar for each run).

---

[referencia=85f66a6419d173a7 score=0.522]
#### **3.3 Performance with Dataset Size and Compute** 

We display empirical trends for the test loss as a function of dataset size _D_ (in tokens) and training compute _C_ in Figure 1. 

For the trend with _D_ we trained a model with ( _n_ layer _, n_ embd) = (36 _,_ 1280) on fixed subsets of the WebText2 dataset. We stopped training once the test loss ceased to decrease. We see that the resulting test losses can be fit with simple power-law 



in the dataset size. The data and fit appear in Figure 1. 

The total amount of non-embedding compute used during training can be estimated as _C_ = 6 _NBS_ , where _B_ is the batch size, _S_ is the number of parameter updates, and the factor of 6 accounts for the forward and backward passes. Thus for a given value of _C_ we can scan over all models with various _N_ to find the model 

9 



<!-- Start of picture text -->
7 5.0<br>WebText2 (Test) Books during training<br>6 Internet Books 4.5 Wikipedia during training<br>Books Books at convergence<br>5 Wikipedia 4.0 Wikipedia at convergence<br>Common Crawl<br>3.5<br>4<br>3.0<br>3<br>2.5<br>10 4 10 5 10 6 10 7 10 8 10 9 5.0 4.5 4.0 3.5 3.0 2.5<br>Parameters (non-embedding) Test Loss on Training Distribution<br>Test Loss<br>Loss on Other Distribution<br><!-- End of picture text -->

**Figure 8 Left:** Generalization performance to other data distributions improves smoothly with model size, with only a small and very slowly growing offset from the WebText2 training distribution. **Right:** Generalization performance depends only on training distribution performance, and not on the phase of training. We compare generalization of converged models (points) to that of a single large model (dashed curves) as it trains.

---

[referencia=85f66a6419d173a7 score=0.473]
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

[referencia=85f66a6419d173a7 score=0.465]
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

[referencia=85f66a6419d173a7 score=0.445]
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

[referencia=85f66a6419d173a7 score=0.436]
|13|Comparison between empirical and adjusted compute trends . . . . . . . . . . . . . . . . .|15|
|14|Optimal model size and serial number of steps versus compute budget . . . . . . . . . . . .|16|
|15|Contradiction between compute and data trends . . . . . . . . . . . . . . . . . . . . . . . .|17|
|16|Early stopping lower bound and training curves for overft models<br>. . . . . . . . . . . . . .|23|
|17|Universal transformers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|18|Batch size scans . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|19|Another look at sample effciency<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|20|Power-law dependence of performance on position in context . . . . . . . . . . . . . . . . .|25|
|21|Performance at different context positions versus model size<br>. . . . . . . . . . . . . . . . .|25|
|22|Learning rate schedule scan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|23|Comparison of Power-Law and Logarithmic Fits<br>. . . . . . . . . . . . . . . . . . . . . . .|26|
|24|Generalization versus depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|



27

---

[referencia=85f66a6419d173a7 score=0.434]
### **7 Related Work** 

Power laws can arise from a wide variety of sources [THK18]. Power-law scalings with model and dataset size in density estimation [Was06] and in random forest models [Bia12] may be connected with our results. These models suggest that power-law exponents may have a very rough interpretation as the inverse of the number of relevant features in the data. 

Some early [BB01, Goo01] work found power-law scalings between performance and dataset size. More recent work [HNA<sup>+</sup> 17, HAD19] also investigated scaling between model size and data size; their work is perhaps the closest to ours in the literature<sup>8</sup> . Note, however, that [HNA<sup>+</sup> 17] found super-linear scaling of dataset size with model size, whereas we find a sub-linear scaling. There are some parallels between our findings on optimal allocation of compute and [Kom19], including power-law learning curves. EfficientNets [TL19] also appear to obey an approximate power-law relation between accuracy and model size. Very recent work [RRBS19b] studies scaling with both dataset size and model size for a variety of datasets, and fits an ansatz similar to ours. 

EfficientNet [TL19] advocates scaling depth and width exponentially (with different coefficients) for optimal performance of image models, resulting in a power-law scaling of width as a function of depth. We find that for language models this power should be roughly one when scaling up (as width/depth should remain fixed). But more importantly, we find that the precise architectural hyperparameters are unimportant compared to the overall scale of the language model. In [VWB16] it was argued that deep models can function as ensembles of shallower models, which could potentially explain this finding. Earlier work [ZK16] has compared width and depth, and found that wide ResNets can outperform deep ResNets on image classification. Some studies fix computation per data example, which tends to scale in proportion to the number of model parameters, whereas we investigate scaling with both model size and the quantity of training computation.

---

[referencia=85f66a6419d173a7 score=0.434]
### **8 Discussion** 

We have observed consistent scalings of language model log-likelihood loss with non-embedding parameter count _N_ , dataset size _D_ , and optimized training computation _C_ min, as encapsulated in Equations (1.5) and (1.6). Conversely, we find very weak dependence on many architectural and optimization hyperparameters. Since scalings with _N, D, C_ min are power-laws, there are diminishing returns with increasing scale. 

> 7Defining words using the `wc` utility, the WebText2 dataset has 1 _._ 4 tokens per word and 4 _._ 3 characters per token. 

> 8After this work was completed, [RRBS19a] also appeared, which makes similar predictions for the dependence of loss on both model and dataset size. 

18 

We were able to precisely model the dependence of the loss on _N_ and _D_ , and alternatively on _N_ and _S_ , when these parameters are varied simultaneously. We used these relations to derive the compute scaling, magnitude of overfitting, early stopping step, and data requirements when training large language models. So our scaling relations go beyond mere observation to provide a predictive framework. One might interpret these relations as analogues of the ideal gas law, which relates the macroscopic properties of a gas in a universal way, independent of most of the details of its microscopic consituents. 

It is natural to conjecture that the scaling relations will apply to other generative modeling tasks with a maximum likelihood loss, and perhaps in other settings as well. To this purpose, it will be interesting to test these relations on other domains, such as images, audio, and video models, and perhaps also for random network distillation. At this point we do not know which of our results depend on the structure of natural language data, and which are universal. It would also be exciting to find a theoretical framework from which the scaling relations can be derived: a ‘statistical mechanics’ underlying the ‘thermodynamics’ we have observed. Such a theory might make it possible to derive other more precise predictions, and provide a systematic understanding of the limitations of the scaling laws.

---

[referencia=85f66a6419d173a7 score=0.374]
#### **B.4 Suboptimal Model Sizes** 

We can solve A.1 to find an expression for the amount of compute needed to reach a given value of the loss _L_ with a model of size _N_ : 



Using A.6 and A.9, we can eliminate _L_ in favor of _N_ eff ( _L_ ), the model size which reaches _L_ most efficiently. From there, we find an expression for the excess compute needed as a consequence of using a suboptimal model size: 



The result is shown in Figure X. Models between 0.6x and 2.2x the optimal size can be used with only a 20% increase in compute budget. Using a smaller model is useful when accounting for the cost inference. A larger model can be trained the the same level of performance in fewer steps, allowing for more parallelism and faster training if sufficient harware is available (see Figure Y): 



A 2.2x larger model requires 45% fewer steps at a cost of 20% more training compute. Note that this equation should not be trusted for very large models, as it is only valid in the power-law region of the learning curve after initial transient effects.

---

[referencia=85f66a6419d173a7 score=0.335]
24 



<!-- Start of picture text -->
Per-token Loss (774M Params)<br>10 3<br>8 4.0 + 3.23.4 + 4.0 TT 0.470.56 10<br>7 2.9 + 4.5 T 0.56<br>2.7 + 4.9 T 0.60 10 8 8 10 2<br>6 2.4 + 5.1 T 0.61<br>2.3 + 5.4 T 0.62<br>5 6<br>10 7<br>10 1<br>4<br>4<br>3 10 6<br>2 10 0<br>10 0 10 1 10 2 10 3 10 1 10 3 10 5<br>Token Index Step<br>20 This figure provides information about the performance per token as a function of model<br>and training time. Left: Loss per token as a function of its position  T in the 1024-token context. Loss scales<br>predictably as a power-law in  T . Right: Test loss per token as a function of training step.<br>7.5 Token 1/1024<br>Token 2/1024<br>6.0 Token 4/1024<br>Token 8/1024<br>Token 16/1024<br>4.5 Token 64/1024<br>Token 256/1024<br>Token 1024/1024<br>Token 1/8<br>Token 2/8<br>3.0 Token 4/8<br>Token 8/8<br>10 4 10 5 10 6 10 7 10 8 10 9<br>Parameters (excl. embedding)<br>Test Loss<br>Token Index<br>Per-Token Test Loss Model Parameters<br>Test Loss<br><!-- End of picture text -->

**Figure 20** This figure provides information about the performance per token as a function of model size and training time. **Left:** Loss per token as a function of its position _T_ in the 1024-token context. Loss scales predictably as a power-law in _T_ . **Right:** Test loss per token as a function of training step.