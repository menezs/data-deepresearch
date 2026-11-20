[referencia=85f66a6419d173a7 score=0.393]
### **1 Introduction** 

Language provides a natural domain for the study of artificial intelligence, as the vast majority of reasoning tasks can be efficiently expressed and evaluated in language, and the world’s text provides a wealth of data for unsupervised learning via generative modeling. Deep learning has recently seen rapid progress in language modeling, with state of the art models [RNSS18, DCLT18, YDY<sup>+</sup> 19, LOG<sup>+</sup> 19, RSR<sup>+</sup> 19] approaching human-level performance on many specific tasks [WPN<sup>+</sup> 19], including the composition of coherent multiparagraph prompted text samples [RWC<sup>+</sup> 19]. 

One might expect language modeling performance to depend on model architecture, the size of neural models, the computing power used to train them, and the data available for this training process. In this work we will empirically investigate the dependence of language modeling loss on all of these factors, focusing on the Transformer architecture [VSP<sup>+</sup> 17, LSP<sup>+</sup> 18]. The high ceiling and low floor for performance on language tasks allows us to study trends over more than seven orders of magnitude in scale. 

Throughout we will observe precise power-law scalings for performance as a function of training time, context length, dataset size, model size, and compute budget.

---

[referencia=85f66a6419d173a7 score=0.200]
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

[referencia=85f66a6419d173a7 score=0.183]
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

[referencia=85f66a6419d173a7 score=0.142]
#### **2.1 Parameter and Compute Scaling of Transformers** 

We parameterize the Transformer architecture using hyperparameters _n_ layer (number of layers), _d_ model (dimension of the residual stream), _d_ ff (dimension of the intermediate feed-forward layer), _d_ attn (dimension of the attention output), and _n_ heads (number of attention heads per layer). We include _n_ ctx tokens in the input context, with _n_ ctx = 1024 except where otherwise noted. 

We use _N_ to denote the model size, which we define as the number of _non-embedding_ parameters 





where we have excluded biases and other sub-leading terms. Our models also have _n_ vocab _d_ model parameters in an embedding matrix, and use _n_ ctx _d_ model parameters for positional embeddings, but we do not include these when discussing the ‘model size’ _N_ ; we will see that this produces significantly cleaner scaling laws. 

Evaluating a forward pass of the Transformer involves roughly 

_C_ forward _≈_ 2 _N_ + 2 _n_ layer _n_ ctx _d_ model (2.2) 

add-multiply operations, where the factor of two comes from the multiply-accumulate operation used in matrix multiplication. A more detailed per-operation parameter and compute count is included in Table 1. 

6 

|**Operation**|**Parameters**|**FLOPs per Token**|
|---|---|---|
|Embed|(_n_vocab+_n_ctx)_d_model|4_d_model|
|Attention: QKV|_n_layer_d_model3_d_attn|2_n_layer_d_model3_d_attn|
|Attention: Mask|—|2_n_layer_n_ctx_d_attn|
|Attention: Project|_n_layer_d_attn_d_model|2_n_layer_d_attn_d_embd|
|Feedforward|_n_layer2_d_model_d_f|2_n_layer2_d_model_d_f|
|De-embed|—|2_d_model_n_vocab|
|**Total (Non-Embedding)**|_N_ = 2_d_model_n_layer(2_d_attn+_d_f)|_C_forward = 2_N_ + 2_n_layer_n_ctx_d_attn|

---

[referencia=85f66a6419d173a7 score=0.139]
#### **6.3 Contradictions and a Conjecture** 

We observe no signs of deviation from straight power-law trends at large values of compute, data, or model size. Our trends must eventually level off, though, since natural language has non-zero entropy. Indeed, the trends for compute-efficient training described in this section already contain an apparent contradiction. At scales several orders of magnitude above those documented here, the performance predicted by the _L_ ( _C_ min) scaling law decreases below what should be possible given the slow growth in training data with compute. This implies that our scaling laws must break down before this point, but we conjecture that the intersection point has a deeper meaning: it provides an estimate of the point at which Transformer language models reach maximal performance. 

Since the amount of data used by compute-efficient training grows slowly with the compute budget, the performance predicted by _L_ ( _C_ min) eventually hits a lower bound set by the _L_ ( _D_ ) power law (see Figure 15). Let us work this out in more detail. 

To keep overfitting under control, the results of Section 4 imply that we should scale the dataset size as 

_D ∝ N_<sup>0</sup><sup>_._74</sup> _∝ C_ min<sup>0</sup><sup>_._54</sup> (6.6) 

where we have used the compute-efficient _N_ ( _C_ min) from Figure 14. Let us compare this to the data requirements of compute-efficient training. If we train at the critical batch size (i.e. _C_ = 2 _C_ min) and never re-use data during training, we find that data usage grows with compute as 

2 _C_ min _D_ ( _C_ min) = �4 _×_ 10<sup>10</sup> tokens� ( _C_ min _/_ PF-Day)<sup>0</sup><sup>_._26</sup> (6.7) 6 _N_ ( _C_ min)<sup>_≈_</sup>

---

[referencia=85f66a6419d173a7 score=0.088]
**Transfer improves with test performance:** When we evaluate models on text with a different distribution than they were trained on, the results are strongly correlated to those on the training validation set with a roughly constant offset in the loss – in other words, transfer to a different distribution incurs a constant penalty but otherwise improves roughly in line with performance on the training set. (Section 3.2.2) 

**Sample efficiency:** Large models are more sample-efficient than small models, reaching the same level of performance with fewer optimization steps (Figure 2) and using fewer data points (Figure 4). 

**Convergence is inefficient:** When working within a fixed compute budget _C_ but without any other restrictions on the model size _N_ or available data _D_ , we attain optimal performance by training _very large models_ and stopping _significantly short of convergence_ (see Figure 3). Maximally compute-efficient training would therefore be far more sample efficient than one might expect based on training small models to convergence, with data requirements growing very slowly as _D ∼ C_<sup>0</sup><sup>_._27</sup> with training compute. (Section 6) 

**Optimal batch size:** The ideal batch size for training these models is roughly a power of the loss only, and continues to be determinable by measuring the gradient noise scale [MKAT18]; it is roughly 1-2 million tokens at convergence for the largest models we can train. (Section 5.1) 

Taken together, these results show that language modeling performance improves smoothly and predictably as we appropriately scale up model size, data, and compute. We expect that larger language models will perform better and be more sample efficient than current models. 

3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.072]
Various works [AS17, BHMM18] have investigated generalization in highly overparameterized models, finding a “jamming transition” [GJS<sup>+</sup> 19] when the model size reaches the dataset size (this may require training many orders of magnitude beyond typical practice, and in particular does not use early stopping). We do not observe such a transition, and find that the necessary training data scales sublinearly in the model size. Expansions in the model size, particularly at large width [JGH18, LXS<sup>+</sup> 19], may provide a useful framework for thinking about some of our scaling relations. Our results on optimization, such as the shape of learning curves, can likely be explained using a noisy quadratic model, which can provide quite accurate predictions [ZLN<sup>+</sup> 19] in realistic settings. Making this connection quantitative will require a characterization of the Hessian spectrum [Pap18, GKX19, GARD18].

---

[referencia=85f66a6419d173a7 score=0.057]
### **8 Discussion** 

We have observed consistent scalings of language model log-likelihood loss with non-embedding parameter count _N_ , dataset size _D_ , and optimized training computation _C_ min, as encapsulated in Equations (1.5) and (1.6). Conversely, we find very weak dependence on many architectural and optimization hyperparameters. Since scalings with _N, D, C_ min are power-laws, there are diminishing returns with increasing scale. 

> 7Defining words using the `wc` utility, the WebText2 dataset has 1 _._ 4 tokens per word and 4 _._ 3 characters per token. 

> 8After this work was completed, [RRBS19a] also appeared, which makes similar predictions for the dependence of loss on both model and dataset size. 

18 

We were able to precisely model the dependence of the loss on _N_ and _D_ , and alternatively on _N_ and _S_ , when these parameters are varied simultaneously. We used these relations to derive the compute scaling, magnitude of overfitting, early stopping step, and data requirements when training large language models. So our scaling relations go beyond mere observation to provide a predictive framework. One might interpret these relations as analogues of the ideal gas law, which relates the macroscopic properties of a gas in a universal way, independent of most of the details of its microscopic consituents. 

It is natural to conjecture that the scaling relations will apply to other generative modeling tasks with a maximum likelihood loss, and perhaps in other settings as well. To this purpose, it will be interesting to test these relations on other domains, such as images, audio, and video models, and perhaps also for random network distillation. At this point we do not know which of our results depend on the structure of natural language data, and which are universal. It would also be exciting to find a theoretical framework from which the scaling relations can be derived: a ‘statistical mechanics’ underlying the ‘thermodynamics’ we have observed. Such a theory might make it possible to derive other more precise predictions, and provide a systematic understanding of the limitations of the scaling laws.

---

[referencia=85f66a6419d173a7 score=0.054]
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

[referencia=85f66a6419d173a7 score=0.044]
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

[referencia=85f66a6419d173a7 score=0.044]
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

[referencia=85f66a6419d173a7 score=0.039]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=85f66a6419d173a7 score=0.036]
These relations hold across eight orders of magnitude in _C_ min, six orders of magnitude in _N_ , and over two orders of magnitude in _D_ . They depend very weakly on model shape and other Transformer hyperparameters (depth, width, number of self-attention heads), with specific numerical values associated with the Webtext2 training set [RWC<sup>+</sup> 19]. The power laws _α_ N _, α_ D _, αC_<sup>min</sup> specify the degree of performance improvement expected as we scale up _N_ , _D_ , or _C_ min; for example, doubling the number of parameters yields a loss that is smaller by a factor 2<sup>_−αN_</sup> = 0 _._ 95. The precise numerical values of _N_ c _, C_ c<sup>min</sup> _,_ and _D_ c depend on the vocabulary size and tokenization and hence do not have a fundamental meaning. 

The critical batch size, which determines the speed/efficiency tradeoff for data parallelism ([MKAT18]), also roughly obeys a power law in _L_ : 



Equation (1.1) and (1.2) together suggest that as we increase the model size, we should increase the dataset _αN_ size sublinearly according to _D ∝ N αD ∼ N_<sup>0</sup><sup>_._74</sup> . In fact, we find that there is a single equation combining (1.1) and (1.2) that governs the simultaneous dependence on _N_ and _D_ and governs the degree of overfitting: 



with fits pictured on the left in figure 4. We conjecture that this functional form may also parameterize the trained log-likelihood for other generative modeling tasks. 

When training a given model for a finite number of parameter update steps _S_ in the infinite data limit, after an initial transient period, the learning curves can be accurately fit by (see the right of figure 4) 



where _Sc ≈_ 2 _._ 1 _×_ 10<sup>3</sup> and _αS ≈_ 0 _._ 76, and _S_ min( _S_ ) is the minimum possible number of optimization steps (parameter updates) estimated using Equation (5.4).

---

[referencia=85f66a6419d173a7 score=0.036]
#### **5.1 Adjustment for Training at** _B_ crit( _L_ ) 

A simple empirical theory for the batch size dependence of training was developed in [MKAT18] (see also [SLA<sup>+</sup> 18, ZLN<sup>+</sup> 19]). It was argued that there is a critical batch size _B_ crit for training; for _B_ up to _B_ crit the batch size can be increased with very minimal degradation in compute-efficiency, whereas for _B > B_ crit increases in _B_ result in diminishing returns. It was also argued that the gradient noise scale provides a simple 

12 

prediction for _B_ crit, and that neither depends directly on model size except through the value of the loss that has been attained. These results can be used to predict how training time and compute will vary with the batch size. To utilize both training time and compute as effectively as possible, it is best to train with a batch size _B ≈ B_ crit. Training at _B ≫ B_ crit minimizes the number of training steps, while _B ≪ B_ crit minimizes the use of compute. 

More specifically, it was demonstrated that for a wide variety of neural network tasks, the number of training steps _S_ and the number of data examples processed _E_ = _BS_ satisfy the simple relation 



when training to any fixed value of the loss _L_ . Here _S_ min is the minimum number of steps necessary to reach _L_ , while _E_ min is the minimum number of data examples that must be processed. 

We demonstrate the relation (5.1) for Transformers in Figure 18 in the appendix. This relation defines the critical batch size 



which is a function of the target value of the loss. Training at the critical batch size makes a roughly optimal time/compute tradeoff, requiring 2 _S_ min training steps and processing _E_ = 2 _E_ min data examples. 

In Figure 10 we have plotted the critical batch size and gradient noise scale<sup>5</sup> as a function of training loss for two different models. We see that _B_ crit( _L_ ) is independent of model size, and only depends on the loss _L_ . So the predictions of [MKAT18] continue to hold for Transformer language models. The critical batch size can be fit with a power-law in the loss

---

[referencia=85f66a6419d173a7 score=0.035]
When training within a fixed compute budget _C_ , but with no other constraints, Equation (1.6) leads to the prediction that the optimal model size _N_ , optimal batch size _B_ , optimal number of steps _S_ , and dataset size _D_ should grow as 



with 



which closely matches the empirically optimal results _N ∝ C_ min<sup>0</sup><sup>_._73,</sup><sup>_B∝C_</sup> min<sup>0</sup><sup>_._24,and</sup><sup>_S∝C_</sup> min<sup>0</sup><sup>_._03.Asthe</sup> computational budget _C_ increases, it should be spent primarily on larger models, without dramatic increases in training time or dataset size (see Figure 3). This also implies that as models grow larger, they become increasingly sample efficient. In practice, researchers typically train smaller models for longer than would 

5 

be maximally compute-efficient because of hardware constraints. Optimal performance depends on total compute as a power law (see Equation (1.3)). 

We provide some basic theoretical motivation for Equation (1.5), an analysis of learning curve fits and their implications for training time, and a breakdown of our results per token. We also make some brief comparisons to LSTMs and recurrent Transformers [DGV<sup>+</sup> 18].

---

[referencia=85f66a6419d173a7 score=0.032]
Test Loss 5.4 Per-token<br>Test Loss 6<br>4.8<br>4.2 LSTMs 4 Parameters:<br>3.6 400K<br>1 Layer2 Layers 5 400K2M<br>3.0 Transformers 4 Layers 3M<br>3 200M<br>2.4 300M<br>2<br>10 5 10 6 10 7 10 8 10 9 10 1 10 2 10 3<br>Parameters (non-embedding) Token Index in Context<br>Figure 7<br>To observe these trends it is crucial to study performance as a function of N ; if we instead use the total<br>parameter count (including the embedding parameters) the trend is somewhat obscured (see Figure 6). This<br>suggests that the embedding matrix can be made smaller without impacting performance, as has been seen in<br>recent work [LCG + 19].<br>Although these models have been trained on the WebText2 dataset, their test loss on a variety of other datasets<br>is also a power-law in  N with nearly identical power, as shown in Figure 8.<br>3.2.1 Comparing to LSTMs and Universal Transformers<br>In Figure 7 we compare LSTM and Transformer performance as a function of non-embedding parameter<br>count N . The LSTMs were trained with the same dataset and context length. We see from these figures<br>that the LSTMs perform as well as Transformers for tokens appearing early in the context, but cannot match<br>the Transformer performance for later tokens. We present power-law relationships between performance and<br>context position Appendix D.5, where increasingly large powers for larger models suggest improved ability<br>to quickly recognize patterns.<br>We also compare the performance of standard Transformers to recurrent Transformers [DGV + 18] in Figure<br>17 in the appendix. These models re-use parameters, and so perform slightly better as a function of  N , at the<br>cost of additional compute per-parameter.<br>3.2.2 Generalization Among Data Distributions<br>We have also tested our models on a set of additional text data distributions. The test loss on these datasets<br>as a function of model size is shown in Figure 8; in all cases the models were trained only on the WebText2<br>

---

[referencia=85f66a6419d173a7 score=0.022]
<!-- Start of picture text -->
7 7<br>6 6<br>5 5<br>0 Layer<br>4 4<br>1 Layer 1 Layer<br>2 Layers 2 Layers<br>3 3 Layers 3 3 Layers<br>6 Layers 6 Layers<br>> 6 Layers > 6 Layers<br>2 2<br>10 6 10 7 10 8 10 9 10 3 10 4 10 5 10 6 10 7 10 8 10 9<br>Parameters (with embedding) Parameters (non-embedding)<br>Test Loss Test Loss<br><!-- End of picture text -->

**Figure 6 Left:** When we include embedding parameters, performance appears to depend strongly on the number of layers in addition to the number of parameters. **Right:** When we exclude embedding parameters, the performance of models with different depths converge to a single trend. Only models with fewer than 2 layers or with extreme depth-to-width ratios deviate significantly from the trend. 

In this section we will display data along with empirically-motivated fits, deferring theoretical analysis to later sections. 

#### **3.1 Approximate Transformer Shape and Hyperparameter Independence** 

Transformer performance depends very weakly on the shape parameters _n_ layer _, n_ heads, and _d_ ff when we hold the total non-embedding parameter count _N_ fixed. To establish these results we trained models with fixed size while varying a single hyperparameter. This was simplest for the case of _n_ heads. When varying _n_ layer, we simultaneously varied _d_ model while keeping _N ≈_ 12 _n_ layer _d_<sup>2</sup> model<sup>fixed.Similarly,tovary</sup><sup>_d_ffatfixed</sup> model size we also simultaneously varied the _d_ model parameter, as required by the parameter counts in Table 1. Independence of _n_ layers would follow if deeper Transformers effectively behave as ensembles of shallower models, as has been suggested for ResNets [VWB16]. The results are shown in Figure 5.

---

[referencia=85f66a6419d173a7 score=0.020]
3 

Larger models require **fewer samples** The optimal model size grows smoothly to reach the same performance with the loss target and compute budget 



<!-- Start of picture text -->
Li ne  color indicates<br>Test Loss 10 10 nu m ber of parameters<br>10 3 10 6 10 9<br>8 8<br>10 3  Params<br>6 6<br>Co m pute-efficient<br>10 9  Params trai n ing stops far<br>sh o rt of convergence<br>4 4<br>10 7 10 9 10 11 1 0 -9 1 0 -6 1 0 -3 10 0<br>Tokens Processed Compute (PF-days)<br><!-- End of picture text -->

**Figure 2** We show a series of language model training runs, with models ranging in size from 10<sup>3</sup> to 10<sup>9</sup> parameters (excluding embeddings). 



<!-- Start of picture text -->
Minimum serial steps  Data requirements<br>increases negligibly grow relatively slowly<br>Optimal model size<br>increases very quickly<br>>1,000,000x Model Size<br>100x Batch Size<br><10x Serial Steps<br><!-- End of picture text -->

**Figure 3** As more compute becomes available, we can choose how much to allocate towards training larger models, using larger batches, and training for more steps. We illustrate this for a billion-fold increase in compute. For optimally compute-efficient training, most of the increase should go towards increased model size. A relatively small increase in data is needed to avoid reuse. Of the increase in data, most can be used to increase parallelism through larger batch sizes, with only a very small increase in serial training time required.

---

[referencia=85f66a6419d173a7 score=0.016]
7 5.0<br>WebText2 (Test) Books during training<br>6 Internet Books 4.5 Wikipedia during training<br>Books Books at convergence<br>5 Wikipedia 4.0 Wikipedia at convergence<br>Common Crawl<br>3.5<br>4<br>3.0<br>3<br>2.5<br>10 4 10 5 10 6 10 7 10 8 10 9 5.0 4.5 4.0 3.5 3.0 2.5<br>Parameters (non-embedding) Test Loss on Training Distribution<br>Figure 8 Left: Generalization performance to other data distributions improves smoothly with model size,<br>with only a small and very slowly growing offset from the WebText2 training distribution. Right: Gener-<br>alization performance depends only on training distribution performance, and not on the phase of training.<br>We compare generalization of converged models (points) to that of a single large model (dashed curves) as it<br>trains.<br>with the best performance on step S = 6 BSC . Note that in these results the batch size B remains fixed for<br>all models , which means that these empirical results are not truly optimal. We will account for this in later<br>sections using an adjusted  C min to produce cleaner trends.<br>The result appears as the heavy black line on the left-hand plot in Figure 1. It can be fit with<br>L ( C )  ≈ Cc αC (3.3)<br>� C �<br>The figure also includes images of individual learning curves to clarify when individual models are optimal.<br>We will study the optimal allocation of compute more closely later on. The data strongly suggests that sample<br>efficiency improves with model size, and we also illustrate this directly in Figure 19 in the appendix.<br>4 Charting the Infinite Data Limit and Overfitting<br>In Section 3 we found a number of basic scaling laws for language modeling performance. Here we will<br>study the performance of a model of size N trained on a dataset with D tokens while varying N and D<br>simultaneously. We will empirically demonstrate that the optimally trained test loss accords with the scaling<br>law of Equation (1.5). This provides guidance on how much data we would need to train models of increasing<br>

---

[referencia=85f66a6419d173a7 score=0.014]
- [DGV<sup>+</sup> 18] Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. Universal transformers. _CoRR_ , abs/1807.03819, 2018, 1807.03819. URL `http://arxiv.org/ abs/1807.03819` . 6, 9, 23, 24 

- [EP94] Werner Ebeling and Thorsten Pöschel. Entropy and long-range correlations in literary english. _EPL (Europhysics Letters)_ , 26(4):241, 1994. 25 

- [Fou] The Common Crawl Foundation. Common crawl. URL `http://commoncrawl.org` . 7 

- [GARD18] Guy Gur-Ari, Daniel A. Roberts, and Ethan Dyer. Gradient descent happens in a tiny subspace. 2018, arXiv:1812.04754. 18 

- [GJS<sup>+</sup> 19] Mario Geiger, Arthur Jacot, Stefano Spigler, Franck Gabriel, Levent Sagun, Stéphane d’Ascoli, Giulio Biroli, Clément Hongler, and Matthieu Wyart. Scaling description of generalization with number of parameters in deep learning. _arXiv_ , 2019, 1901.01608. 18 

- [GKX19] Behrooz Ghorbani, Shankar Krishnan, and Ying Xiao. An investigation into neural net optimization via hessian eigenvalue density. _CoRR_ , abs/1901.10159, 2019, 1901.10159. URL `http://arxiv.org/abs/1901.10159` . 18 

- [Goo01] Joshua Goodman. A bit of progress in language modeling. _CoRR_ , cs.CL/0108005, 2001. URL `http://arxiv.org/abs/cs.CL/0108005` . 18 

- [GRK17] Scott Gray, Alec Radford, and Diederik P Kingma. Gpu kernels for block-sparse weights. _openai.com_ , 2017. 19