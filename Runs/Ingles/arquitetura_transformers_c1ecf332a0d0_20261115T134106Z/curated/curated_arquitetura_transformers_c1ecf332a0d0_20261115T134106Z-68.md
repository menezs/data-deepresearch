[referencia=85f66a6419d173a7 score=0.982]
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

[referencia=85f66a6419d173a7 score=0.960]
#### **D.4 Sample Efficiency vs Model Size** 

It is easy to see from figure 2 that larger models train faster, and are therefore more sample efficient. We provide another way of looking at this phenomenon in figure 19, which shows when different models reach 



<!-- Start of picture text -->
5.5 5.5<br>10 11<br>10 5 5.0 5.0<br>4.5 10 10 4.5<br>10 4 4.0 4.0<br>3.5 10 9 3.5<br>3.0 3.0<br>10 3 10 8<br>2.5 2.5<br>10 6 10 7 10 8 10 6 10 7 10 8<br>Parameters (non-embedding) Parameters (non-embedding)<br>)<br>) min<br>min E<br>S<br>Loss Loss<br>Minimum Steps (<br>Minimum Examples (<br><!-- End of picture text -->

**Figure 19** The number of minimum serial steps needed to reach any fixed value of the test loss decreases precipitously with model size. Sample efficiency (show here for training far below the critical batch size) improves greatly as well, improving by a factor of almost 100 when comparing the smallest possible model to a very large one. 

24 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.957]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=85f66a6419d173a7 score=0.939]
**Transfer improves with test performance:** When we evaluate models on text with a different distribution 

than they were trained on, the results are strongly correlated to those on the training validation set with a roughly constant offset in the loss – in other words, transfer to a different distribution incurs a constant penalty but otherwise improves roughly in line with performance on the training set. (Section 3.2.2) **Sample efficiency:** Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4). **Convergence is inefficient:** When working within a fixed compute budget _C_ but without any other restrictions on the model size _N_ or available data _D_ , we attain optimal performance by training _very large models_ and stopping _significantly short of convergence_ (see Figure 3). Maximally compute-efficient training would therefore be far more sample efficient than one might expect based on training small models to convergence, with data requirements growing very slowly as _D ∼ C_<sup>0</sup><sup>_._27</sup> with training compute. (Section 6) 

**Optimal batch size:** The ideal batch size for training these models is roughly a power of the loss only, and continues to be determinable by measuring the gradient noise scale [MKAT18]; it is roughly 1-2 million tokens at convergence for the largest models we can train. (Section 5.1) 

Taken together, these results show that language modeling performance improves smoothly and predictably as we appropriately scale up model size, data, and compute. We expect that larger language models will perform better and be more sample efficient than current models. 

3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.876]
**Figure 23** The trend for performance as a function of parameter count, _L_ ( _N_ ), is fit better by a power law than by other functions such as a logarithm at a qualitative level. 

schedules appear to be statistical noise, and provide a rough gauge for the scale of variation between different training runs. Experiments on larger models suggest that the variation in the final test loss between different random seeds is roughly constant in magnitude for different model sizes. 

We found that larger models require a smaller learning rate to prevent divergence, while smaller models can tolerate a larger learning rate. To implement this, the following rule of thumb was used for most runs: 

LR( _N_ ) _≈_ 0 _._ 003239 + _−_ 0 _._ 0001395 log( _N_ ) (D.1) 

We expect that this formula could be improved. There may be a dependence on network width, likely set by the initialization scale. The formula also breaks down for _N >_ 10<sup>10</sup> parameters. Nevertheless, we found that it works sufficiently well for the models we considered. 

#### **D.7 Fit Details and Power Law Quality** 

We experimented with a number of functional forms for the fits to _L_ ( _N_ ) _, L_ ( _C_ ), and _L_ ( _D_ ); the power-law fits were qualitatively much more accurate than other functions such as logarithms (see Figure 23). 

For _L_ ( _C_ ), we do not include small models with only 1 layer in the fit, as the transition from 1 to 2 layers causes a noticable lump in the data. For _L_ ( _N_ ) we also do not include very small models with only 1 layer in the fit, and we exclude the largest models that have not trained fully to convergence. Fit parameters change marginally if we do include them, and the trend extrapolates well in both directions regardless.

---

[referencia=85f66a6419d173a7 score=0.874]
When training within a fixed compute budget _C_ , but with no other constraints, Equation (1.6) leads to the prediction that the optimal model size _N_ , optimal batch size _B_ , optimal number of steps _S_ , and dataset size _D_ should grow as 



with 



which closely matches the empirically optimal results _N ∝ C_ min<sup>0</sup><sup>_._73,</sup><sup>_B∝C_</sup> min<sup>0</sup><sup>_._24,and</sup><sup>_S∝C_</sup> min<sup>0</sup><sup>_._03.Asthe</sup> computational budget _C_ increases, it should be spent primarily on larger models, without dramatic increases in training time or dataset size (see Figure 3). This also implies that as models grow larger, they become increasingly sample efficient. In practice, researchers typically train smaller models for longer than would 

5 

be maximally compute-efficient because of hardware constraints. Optimal performance depends on total compute as a power law (see Equation (1.3)). 

We provide some basic theoretical motivation for Equation (1.5), an analysis of learning curve fits and their implications for training time, and a breakdown of our results per token. We also make some brief comparisons to LSTMs and recurrent Transformers [DGV<sup>+</sup> 18].

---

[referencia=85f66a6419d173a7 score=0.788]
**Figure 9** The early-stopped test loss _L_ ( _N, D_ ) depends predictably on the dataset size _D_ and model size _N_ according to Equation (1.5). **Left** : For large _D_ , performance is a straight power law in _N_ . For a smaller fixed _D_ , performance stops improving as _N_ increases and the model begins to overfit. (The reverse is also true, _αN_ see Figure 4.) **Right** : The extent of overfitting depends predominantly on the ratio _N αD /D_ , as predicted in equation (4.3). The line is our fit to that equation. 

Since we stop training early when the test loss ceases to improve and optimize all models in the same way, we expect that larger models should always perform better than smaller models. But with fixed finite _D_ , we also do not expect any model to be capable of approaching the best possible loss (ie the entropy of text). Similarly, a model with fixed size will be capacity-limited. These considerations motivate our second principle. Note that knowledge of _L_ ( _N_ ) at infinite _D_ and _L_ ( _D_ ) at infinite _N_ fully determines all the parameters in _L_ ( _N, D_ ). 

The third principle is more speculative. There is a simple and general reason one might expect overfitting to scale _∝_ 1 _/D_ at very large _D_ . Overfitting should be related to the variance or the signal-to-noise ratio of the dataset [AS17], and this scales as 1 _/D_ . This expectation should hold for any smooth loss function, since we expect to be able to expand the loss about the _D →∞_ limit. However, this argument assumes that 1 _/D_ corrections dominate over other sources of variance, such as the finite batch size and other limits on the efficacy of optimization. Without empirical confirmation, we would not be very confident of its applicability. 

Our third principle explains the asymmetry between the roles of _N_ and _D_ in Equation (1.5). Very similar symmetric expressions<sup>4</sup> are possible, but they would not have a 1 _/D_ expansion with integer powers, and would require the introduction of an additional parameter.

---

[referencia=85f66a6419d173a7 score=0.781]
### **8 Discussion** 

We have observed consistent scalings of language model log-likelihood loss with non-embedding parameter count _N_ , dataset size _D_ , and optimized training computation _C_ min, as encapsulated in Equations (1.5) and (1.6). Conversely, we find very weak dependence on many architectural and optimization hyperparameters. Since scalings with _N, D, C_ min are power-laws, there are diminishing returns with increasing scale. 

> 7Defining words using the `wc` utility, the WebText2 dataset has 1 _._ 4 tokens per word and 4 _._ 3 characters per token. 

> 8After this work was completed, [RRBS19a] also appeared, which makes similar predictions for the dependence of loss on both model and dataset size. 

18 

We were able to precisely model the dependence of the loss on _N_ and _D_ , and alternatively on _N_ and _S_ , when these parameters are varied simultaneously. We used these relations to derive the compute scaling, magnitude of overfitting, early stopping step, and data requirements when training large language models. So our scaling relations go beyond mere observation to provide a predictive framework. One might interpret these relations as analogues of the ideal gas law, which relates the macroscopic properties of a gas in a universal way, independent of most of the details of its microscopic consituents. 

It is natural to conjecture that the scaling relations will apply to other generative modeling tasks with a maximum likelihood loss, and perhaps in other settings as well. To this purpose, it will be interesting to test these relations on other domains, such as images, audio, and video models, and perhaps also for random network distillation. At this point we do not know which of our results depend on the structure of natural language data, and which are universal. It would also be exciting to find a theoretical framework from which the scaling relations can be derived: a ‘statistical mechanics’ underlying the ‘thermodynamics’ we have observed. Such a theory might make it possible to derive other more precise predictions, and provide a systematic understanding of the limitations of the scaling laws.

---

[referencia=85f66a6419d173a7 score=0.772]
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

[referencia=85f66a6419d173a7 score=0.745]
3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->
Li ne  color indicates<br>Test Loss 10 10 nu m ber of parameters<br>10 3 10 6 10 9<br>8 8<br>10 3  Params<br>6 6<br>Co m pute-efficient<br>10 9  Params trai n ing stops far<br>sh o rt of convergence<br>4 4<br>10 7 10 9 10 11 1 0 -9 1 0 -6 1 0 -3 10 0<br>Tokens Processed Compute (PF-days)<br><!-- End of picture text -->

**Figure 2** We show a series of language model training runs, with models ranging in size from 10<sup>3</sup> to 10<sup>9</sup> parameters (excluding embeddings). 



<!-- Start of picture text -->
Minimum serial steps  Data requirements<br>increases negligibly grow relatively slowly<br>Optimal model size<br>increases very quickly<br>>1,000,000x Model Size<br>100x Batch Size<br><10x Serial Steps<br><!-- End of picture text -->

**Figure 3** As more compute becomes available, we can choose how much to allocate towards training larger models, using larger batches, and training for more steps. We illustrate this for a billion-fold increase in compute. For optimally compute-efficient training, most of the increase should go towards increased model size. A relatively small increase in data is needed to avoid reuse. Of the increase in data, most can be used to increase parallelism through larger batch sizes, with only a very small increase in serial training time required.

---

[referencia=85f66a6419d173a7 score=0.712]
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

[referencia=85f66a6419d173a7 score=0.699]
According to Figure 1, we expect that when we are bottlenecked by the dataset size (ie by overfitting), the loss should scale as _L_ ( _D_ ) _∝ D_<sup>_−_0</sup><sup>_._095</sup> . This implies that the loss would scale with compute as _L_ ( _D_ ( _C_ min)) _∝ C_ min<sup>_−_0</sup><sup>_._03</sup> once we are data-limited. Once again, we have a contradiction, as this will eventually intersect with our prediction for _L_ ( _C_ min) from Figure 13, where we found a scaling _L_ ( _C_ min) _∝ C_ min<sup>_−_0</sup><sup>_._050</sup> . 

The intersection point of _L_ ( _D_ ( _C_ min)) and _L_ ( _C_ min) occurs at 

_C_<sup>_∗_</sup> _∼_ 10<sup>4</sup> PF-Days _N_<sup>_∗_</sup> _∼_ 10<sup>12</sup> parameters _, D_<sup>_∗_</sup> _∼_ 10<sup>12</sup> tokens _, L_<sup>_∗_</sup> _∼_ 1 _._ 7 nats/token (6.8) 

though the numerical values are highly uncertain, varying by an order or magnitude in either direction depending on the precise values of the exponents from the power-law fits. The most obvious interpretation is that our scaling laws break down at or before we reach this point, which is still many orders of magnitude away in both compute and model size. 

17

---

[referencia=85f66a6419d173a7 score=0.697]
with the best performance on step _S_ = 6 _BSC_<sup>.Notethatintheseresults</sup><sup>_thebatchsizeBremainsfixedfor_</sup> _all models_ , which means that these empirical results are not truly optimal. We will account for this in later sections using an adjusted _C_ min to produce cleaner trends. 

The result appears as the heavy black line on the left-hand plot in Figure 1. It can be fit with 



The figure also includes images of individual learning curves to clarify when individual models are optimal. We will study the optimal allocation of compute more closely later on. The data strongly suggests that sample efficiency improves with model size, and we also illustrate this directly in Figure 19 in the appendix.

---

[referencia=85f66a6419d173a7 score=0.649]
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

[referencia=85f66a6419d173a7 score=0.626]
With these parameters, we obtain the learning curve fits in Figure 4. Though the fits are imperfect, we believe they are quite compelling given the simplicity of Equation (5.6). 

The data and fits can be visualized in a different and more interesting way, as shown in Figure 11. There we study the test loss as a function of model size while fixing either the total non-embedding compute _C_ used in training, or the number of steps _S_ . For the fits we use Equation (5.5) and (5.4) along with the parameters above and Equation (5.6). 

The power-law dependence of the loss on _S_ min reflects the interplay of optimizer dynamics and the loss landscape. Since the fits are best late in training, when the loss may be approximately quadratic, the powerlaw should provide information about the spectrum of the Hessian of the loss. Its universality suggests that the Hessian eigenvalue density is roughly independent of model size. 

#### **5.3 Lower Bound on Early Stopping Step** 

The results for _L_ ( _N, S_ min) can be used to derive a lower-bound (and rough estimate) of the step at which early stopping should occur when training is data limited. It is motivated by the idea that finite and infinite _D_ learning curves for a given model will be very similar until we reach _S_ min _≈ S_ stop. Thus overfitting should be proportional to the correction from simply ending training at _S_ stop. This will underestimate _S_ stop, because in reality the test loss will decrease more slowly when we have a finite _D_ , and therefore we will require more training steps to reach the optimal test loss at finite _D_ . This line of reasoning leads to the inequality 



where _L_ ( _N, ∞_ ) is the converged loss, evaluated with infinite available data. This inequality and its comparison to the empirical data is displayed in Figure 16 in the appendix. In that figure, the values of _S_ stop and _L_ ( _N, D_ ) are empirical (though _S_ stop is adjusted to mimic training at _B ≫ B_ crit), while _L_ ( _N, ∞_ ) is computed from the fit to _L_ ( _N, D_ ) evaluated at _D_ = _∞_ .

---

[referencia=85f66a6419d173a7 score=0.611]
#### **1.3 Notation** 

We use the following notation: 

- _L_ – the cross entropy loss in nats. Typically it will be averaged over the tokens in a context, but in some cases we report the loss for specific tokens within the context. 

- _N_ – the number of model parameters, _excluding all vocabulary and positional embeddings_ 

- _C ≈_ 6 _NBS_ – an estimate of the total non-embedding training compute, where _B_ is the batch size, and _S_ is the number of training steps (ie parameter updates). We quote numerical values in PF-days, where one PF-day = 10<sup>15</sup> _×_ 24 _×_ 3600 = 8 _._ 64 _×_ 10<sup>19</sup> floating point operations. 

- _D_ – the dataset size in tokens 

- _B_ crit – the critical batch size [MKAT18], defined and discussed in Section 5.1. Training at the critical batch size provides a roughly optimal compromise between time and compute efficiency. 

- _C_ min – an estimate of the minimum amount of non-embedding compute to reach a given value of the loss. This is the training compute that would be used if the model were trained at a batch size much less than the critical batch size. 

- _S_ min – an estimate of the minimal number of training steps needed to reach a given value of the loss. This is also the number of training steps that would be used if the model were trained at a batch size much greater than the critical batch size. 

- _αX_ – power-law exponents for the scaling of the loss as _L_ ( _X_ ) _∝_ 1 _/X_<sup>_αX_</sup> where _X_ can be any of _N, D, C, S, B, C_<sup>min</sup> .

---

[referencia=85f66a6419d173a7 score=0.568]
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

[referencia=85f66a6419d173a7 score=0.565]
#### **B.4 Suboptimal Model Sizes** 

We can solve A.1 to find an expression for the amount of compute needed to reach a given value of the loss _L_ with a model of size _N_ : 



Using A.6 and A.9, we can eliminate _L_ in favor of _N_ eff ( _L_ ), the model size which reaches _L_ most efficiently. From there, we find an expression for the excess compute needed as a consequence of using a suboptimal model size: 



The result is shown in Figure X. Models between 0.6x and 2.2x the optimal size can be used with only a 20% increase in compute budget. Using a smaller model is useful when accounting for the cost inference. A larger model can be trained the the same level of performance in fewer steps, allowing for more parallelism and faster training if sufficient harware is available (see Figure Y): 



A 2.2x larger model requires 45% fewer steps at a cost of 20% more training compute. Note that this equation should not be trusted for very large models, as it is only valid in the power-law region of the learning curve after initial transient effects.

---

[referencia=85f66a6419d173a7 score=0.561]
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

[referencia=85f66a6419d173a7 score=0.526]
### **C Caveats** 

In this section we list some potential caveats to our analysis. 

> _•_ At present we do not have a solid theoretical understanding for any of our proposed scaling laws. The scaling relations with model size and compute are especially mysterious. It may be possible to understand scaling at very large _D_ holding model size fixed [AS17], and also the shape of learning curves late in training, by modeling the loss with a noisy quadratic. But the scaling with _D_ at very large model size still remains mysterious. Without a theory or a systematic understanding of the corrections to our scaling laws, it’s difficult to determine in what circumstances they can be trusted. 

22 



<!-- Start of picture text -->
6<br>Test Loss 10 10<br>Early Stopping Step 5 Train Loss<br>10 5 Data Size21M 4 10 9<br>43M<br>86M<br>10 4 172M344M 3<br>688M 10 8<br>1.4B<br>2<br>10 3<br>10 3 10 4 10 5 10 3 10 4 10 5<br>Sc × [L(N, D) L(N, )] 1/ S Step<br>Loss<br>stop<br>S<br>Dataset Size (Tokens)<br><!-- End of picture text -->

**Figure 16 Left:** We characterize the step on which early stopping occurs, as a function of the extent of overfitting. The red line indicates a lower bound for early stopping that is derived in Section 5.3. **Right:** We display train and test loss for a series of 300M parameter models trained on different sized dataset subsamples. The test loss typically follows that of a run done with unrestricted data until diverging. Note that the degree of overfitting (as compared to the infinite data limit) is significantly overestimated by _L_ test _− L_ train (denoted by a black bar for each run).