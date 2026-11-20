[referencia=85f66a6419d173a7 score=0.922]
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

[referencia=85f66a6419d173a7 score=0.020]
#### **D.8 Generalization and Architecture** 

In figure 24 we show that generalization to other data distributions does not depend on network depth when we hold the total parameter count fixed. It seems to depend only on the performance on the training distribution. 

26 



<!-- Start of picture text -->
2.8<br>2.7<br>Wikipedia<br>Books<br>2.6 Internet Books<br>Common Crawl<br>2.5 WebText2 (Train)<br>WebText2 (Test)<br>2.4<br>2.3<br>10 1 10 2<br>Depth<br>Test Loss<br><!-- End of picture text -->

**Figure 24** We show evaluations on a series of datasets for models with approximately 1.5 Billion parameters. We observe no effect of depth on generalization; generalization performance depends primarily on training distribution performance. The 12-layer model overfit the Internet Books dataset and we show the early-stopped performance; we have not seen this surprising result in other experiments.

---

[referencia=85f66a6419d173a7 score=0.012]
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

[referencia=85f66a6419d173a7 score=0.004]
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

[referencia=85f66a6419d173a7 score=0.004]
- [SLA<sup>+</sup> 18] Christopher J. Shallue, Jaehoon Lee, Joe Antognini, Jascha Sohl-Dickstein, Roy Frostig, and George E. Dahl. Measuring the effects of data parallelism on neural network training, 2018, arXiv:1811.03600. 12 

- [SS18] Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. _CoRR_ , abs/1804.04235, 2018, 1804.04235. URL `http://arxiv.org/abs/1804.04235` . 7 

- [THK18] Stefan Thurner, Rudolf Hanel, and Peter Klimek. _Introduction to the theory of complex systems_ . Oxford University Press, 2018. 18 

- [TL19] Mingxing Tan and Quoc V. Le. Efficientnet: Rethinking model scaling for convolutional neural networks. _CoRR_ , abs/1905.11946, 2019, 1905.11946. URL `http://arxiv.org/abs/1905. 11946` . 18 

- [VSP<sup>+</sup> 17] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems 30_ , pages 5998–6008. Curran Associates, Inc., 2017. URL `http://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf` . 2, 6 

- [VWB16] Andreas Veit, Michael Wilber, and Serge Belongie. Residual networks behave like ensembles of relatively shallow networks, 2016, arXiv:1605.06431. 8, 18

---

[referencia=85f66a6419d173a7 score=0.003]
**Figure 23** The trend for performance as a function of parameter count, _L_ ( _N_ ), is fit better by a power law than by other functions such as a logarithm at a qualitative level. 

schedules appear to be statistical noise, and provide a rough gauge for the scale of variation between different training runs. Experiments on larger models suggest that the variation in the final test loss between different random seeds is roughly constant in magnitude for different model sizes. 

We found that larger models require a smaller learning rate to prevent divergence, while smaller models can tolerate a larger learning rate. To implement this, the following rule of thumb was used for most runs: 

LR( _N_ ) _≈_ 0 _._ 003239 + _−_ 0 _._ 0001395 log( _N_ ) (D.1) 

We expect that this formula could be improved. There may be a dependence on network width, likely set by the initialization scale. The formula also breaks down for _N >_ 10<sup>10</sup> parameters. Nevertheless, we found that it works sufficiently well for the models we considered. 

#### **D.7 Fit Details and Power Law Quality** 

We experimented with a number of functional forms for the fits to _L_ ( _N_ ) _, L_ ( _C_ ), and _L_ ( _D_ ); the power-law fits were qualitatively much more accurate than other functions such as logarithms (see Figure 23). 

For _L_ ( _C_ ), we do not include small models with only 1 layer in the fit, as the transition from 1 to 2 layers causes a noticable lump in the data. For _L_ ( _N_ ) we also do not include very small models with only 1 layer in the fit, and we exclude the largest models that have not trained fully to convergence. Fit parameters change marginally if we do include them, and the trend extrapolates well in both directions regardless.

---

[referencia=85f66a6419d173a7 score=0.002]
- [LOG<sup>+</sup> 19] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized BERT pretraining approach. _CoRR_ , abs/1907.11692, 2019, 1907.11692. URL `http://arxiv.org/abs/ 1907.11692` . 2 

- [LSP<sup>+</sup> 18] Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. Generating wikipedia by summarizing long sequences. _arXiv:1801.10198 [cs]_ , 2018, 1801.10198. URL `http://arxiv.org/abs/1801.10198` . 2, 6 

- [LT16] Henry W Lin and Max Tegmark. Criticality in formal languages and statistical physics. _arXiv preprint arXiv:1606.06737_ , 2016. 25 

- [LXS<sup>+</sup> 19] Jaehoon Lee, Lechao Xiao, Samuel S. Schoenholz, Yasaman Bahri, Roman Novak, Jascha SohlDickstein, and Jeffrey Pennington. Wide neural networks of any depth evolve as linear models under gradient descent, 2019, arXiv:1902.06720. 18 

- [MKAT18] Sam McCandlish, Jared Kaplan, Dario Amodei, and OpenAI Dota Team. An empirical model of large-batch training, 2018, arXiv:1812.06162. 3, 5, 6, 12, 13, 21 

- [Pap18] Vardan Papyan. The full spectrum of deep net hessians at scale: Dynamics with sample size. _CoRR_ , abs/1811.07062, 2018, 1811.07062. URL `http://arxiv.org/abs/1811.07062` . 18

---

[referencia=85f66a6419d173a7 score=0.002]
### **7 Related Work** 

Power laws can arise from a wide variety of sources [THK18]. Power-law scalings with model and dataset size in density estimation [Was06] and in random forest models [Bia12] may be connected with our results. These models suggest that power-law exponents may have a very rough interpretation as the inverse of the number of relevant features in the data. 

Some early [BB01, Goo01] work found power-law scalings between performance and dataset size. More recent work [HNA<sup>+</sup> 17, HAD19] also investigated scaling between model size and data size; their work is perhaps the closest to ours in the literature<sup>8</sup> . Note, however, that [HNA<sup>+</sup> 17] found super-linear scaling of dataset size with model size, whereas we find a sub-linear scaling. There are some parallels between our findings on optimal allocation of compute and [Kom19], including power-law learning curves. EfficientNets [TL19] also appear to obey an approximate power-law relation between accuracy and model size. Very recent work [RRBS19b] studies scaling with both dataset size and model size for a variety of datasets, and fits an ansatz similar to ours. 

EfficientNet [TL19] advocates scaling depth and width exponentially (with different coefficients) for optimal performance of image models, resulting in a power-law scaling of width as a function of depth. We find that for language models this power should be roughly one when scaling up (as width/depth should remain fixed). But more importantly, we find that the precise architectural hyperparameters are unimportant compared to the overall scale of the language model. In [VWB16] it was argued that deep models can function as ensembles of shallower models, which could potentially explain this finding. Earlier work [ZK16] has compared width and depth, and found that wide ResNets can outperform deep ResNets on image classification. Some studies fix computation per data example, which tends to scale in proportion to the number of model parameters, whereas we investigate scaling with both model size and the quantity of training computation.

---

[referencia=85f66a6419d173a7 score=0.002]
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

[referencia=85f66a6419d173a7 score=0.002]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=85f66a6419d173a7 score=0.001]
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

[referencia=85f66a6419d173a7 score=0.001]
### **A Summary of Power Laws** 

For easier reference, we provide a summary below of the key trends described throughout the paper. 

|**Parameters**|**Data**|**Compute**|**Batch Size**|**Equation**|
|---|---|---|---|---|
|_N_|_∞_|_∞_|Fixed|_L_(_N_) = (_N_c_/N_)<sup>_αN_</sup>|
|_∞_|_D_|Early Stop|Fixed|_L_(_D_) = (_D_c_/D_)<sup>_αD_</sup>|
|Optimal|_∞_|_C_|Fixed|_L_(_C_) = (_C_c_/C_)<sup>_αC_ </sup>(naive)|
|_N_opt|_D_opt|_C_min|_B ≪B_crit|_L_(_C_min) =<br>�<br>_C_<sup>min</sup><br>c<br>_/C_min<br>�_α_<sup>min</sup><br>_C_|
|_N_|_D_|Early Stop|Fixed|_L_(_N, D_) =<br>��_N_c<br>_N_<br>�<sup>_αN_</sup><br>_αD_ + _Dc_<br>_D_<br>�_~~α~~D_|
|_N_|_∞_|_S_ steps|_B_|_L_(_N, S_) =<br>�_N_c<br>_N_<br>�_αN_ +<br>�<br>_S_c<br>_S_min(_S,B_)<br>�_~~α~~S_|



**Table 4** 

The empirical fitted values for these trends are:

---

[referencia=85f66a6419d173a7 score=0.001]
- [DGV<sup>+</sup> 18] Mostafa Dehghani, Stephan Gouws, Oriol Vinyals, Jakob Uszkoreit, and Lukasz Kaiser. Universal transformers. _CoRR_ , abs/1807.03819, 2018, 1807.03819. URL `http://arxiv.org/ abs/1807.03819` . 6, 9, 23, 24 

- [EP94] Werner Ebeling and Thorsten Pöschel. Entropy and long-range correlations in literary english. _EPL (Europhysics Letters)_ , 26(4):241, 1994. 25 

- [Fou] The Common Crawl Foundation. Common crawl. URL `http://commoncrawl.org` . 7 

- [GARD18] Guy Gur-Ari, Daniel A. Roberts, and Ethan Dyer. Gradient descent happens in a tiny subspace. 2018, arXiv:1812.04754. 18 

- [GJS<sup>+</sup> 19] Mario Geiger, Arthur Jacot, Stefano Spigler, Franck Gabriel, Levent Sagun, Stéphane d’Ascoli, Giulio Biroli, Clément Hongler, and Matthieu Wyart. Scaling description of generalization with number of parameters in deep learning. _arXiv_ , 2019, 1901.01608. 18 

- [GKX19] Behrooz Ghorbani, Shankar Krishnan, and Ying Xiao. An investigation into neural net optimization via hessian eigenvalue density. _CoRR_ , abs/1901.10159, 2019, 1901.10159. URL `http://arxiv.org/abs/1901.10159` . 18 

- [Goo01] Joshua Goodman. A bit of progress in language modeling. _CoRR_ , cs.CL/0108005, 2001. URL `http://arxiv.org/abs/cs.CL/0108005` . 18 

- [GRK17] Scott Gray, Alec Radford, and Diederik P Kingma. Gpu kernels for block-sparse weights. _openai.com_ , 2017. 19

---

[referencia=85f66a6419d173a7 score=0.001]
Various works [AS17, BHMM18] have investigated generalization in highly overparameterized models, finding a “jamming transition” [GJS<sup>+</sup> 19] when the model size reaches the dataset size (this may require training many orders of magnitude beyond typical practice, and in particular does not use early stopping). We do not observe such a transition, and find that the necessary training data scales sublinearly in the model size. Expansions in the model size, particularly at large width [JGH18, LXS<sup>+</sup> 19], may provide a useful framework for thinking about some of our scaling relations. Our results on optimization, such as the shape of learning curves, can likely be explained using a noisy quadratic model, which can provide quite accurate predictions [ZLN<sup>+</sup> 19] in realistic settings. Making this connection quantitative will require a characterization of the Hessian spectrum [Pap18, GKX19, GARD18].

---

[referencia=85f66a6419d173a7 score=0.001]
#### **4.2 Results** 

We regularize all our models with 10% dropout, and by tracking test loss and stopping once it is no longer decreasing. The results are displayed in Figure 9, including a fit to the four parameters _αN , αD, Nc, Dc_ in Equation (1.5): 

|Parameter|_αN_|_αD_|_Nc_|_Dc_|
|---|---|---|---|---|
|Value|0_._076|0_._103|6_._4_×_10<sup>13</sup>|1_._8_×_10<sup>13</sup>|
||**Table**|**2**<br>Fits|to_L_(_N, D_)||



We obtain an excellent fit, with the exception of the runs where the dataset has been reduced by a factor of 1024, to about 2 _×_ 10<sup>7</sup> tokens. With such a small dataset, an epoch consists of only 40 parameter updates. Perhaps such a tiny dataset represents a different regime for language modeling, as overfitting happens very early in training (see Figure 16). Also note that the parameters differ very slightly from those obtained in Section 3, as here we are fitting the full _L_ ( _N, D_ ) rather than just _L_ ( _N, ∞_ ) or _L_ ( _∞, D_ ). 

To chart the borderlands of the infinite data limit, we can directly study the extent of overfitting. For all but the largest models, we see no sign of overfitting when training with the full 22B token WebText2 dataset, so we can take it as representative of _D_ = _∞_ . Thus we can compare finite _D_ to the infinite data limit by 



11 



<!-- Start of picture text -->

---

[referencia=85f66a6419d173a7 score=0.001]
- [ACDE12] Eduardo G Altmann, Giampaolo Cristadoro, and Mirko Degli Esposti. On the origin of longrange correlations in texts. _Proceedings of the National Academy of Sciences_ , 109(29):11582– 11587, 2012. 25 

- [AS17] Madhu S. Advani and Andrew M. Saxe. High-dimensional dynamics of generalization error in neural networks. _arXiv_ , 2017, 1710.03667. 11, 18, 22 

- [BB01] Michele Banko and Eric Brill. Scaling to very very large corpora for natural language disambiguation. In _Proceedings of the 39th annual meeting on association for computational linguistics_ , pages 26–33. Association for Computational Linguistics, 2001. 18 

- [BHMM18] Mikhail Belkin, Daniel Hsu, Siyuan Ma, and Soumik Mandal. Reconciling modern machine learning and the bias-variance trade-off. _arXiv_ , 2018, 1812.11118. 18 

- [Bia12] GÃŠrard Biau. Analysis of a random forests model. _Journal of Machine Learning Research_ , 13(Apr):1063–1095, 2012. 18 

- [CGRS19] Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. _CoRR_ , abs/1904.10509, 2019, 1904.10509. URL `http://arxiv.org/ abs/1904.10509` . 19 

- [DCLT18] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding, 2018, arXiv:1810.04805. 2

---

[referencia=85f66a6419d173a7 score=0.000]
#### **3.2.1 Comparing to LSTMs and Universal Transformers** 

In Figure 7 we compare LSTM and Transformer performance as a function of non-embedding parameter count _N_ . The LSTMs were trained with the same dataset and context length. We see from these figures that the LSTMs perform as well as Transformers for tokens appearing early in the context, but cannot match the Transformer performance for later tokens. We present power-law relationships between performance and context position Appendix D.5, where increasingly large powers for larger models suggest improved ability to quickly recognize patterns. 

We also compare the performance of standard Transformers to recurrent Transformers [DGV<sup>+</sup> 18] in Figure 17 in the appendix. These models re-use parameters, and so perform slightly better as a function of _N_ , at the cost of additional compute per-parameter. 

#### **3.2.2 Generalization Among Data Distributions** 

We have also tested our models on a set of additional text data distributions. The test loss on these datasets as a function of model size is shown in Figure 8; in all cases the models were trained only on the WebText2 dataset. We see that the loss on these other data distributions improves smoothly with model size, in direct parallel with the improvement on WebText2. We find that generalization depends almost exclusively on the in-distribution validation loss, and does not depend on the duration of training or proximity to convergence. We also observe no dependence on model depth (see Appendix D.8).

---

[referencia=85f66a6419d173a7 score=0.000]
- [HCC<sup>+</sup> 18] Yanping Huang, Yonglong Cheng, Dehao Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V. Le, and Zhifeng Chen. Gpipe: Efficient training of giant neural networks using pipeline parallelism. _CoRR_ , abs/1811.06965, 2018, 1811.06965. URL `http://arxiv.org/abs/1811.06965` . 19 

- [HNA<sup>+</sup> 17] Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos, Heewoo Jun, Hassan Kianinejad, Md. Mostofa Ali Patwary, Yang Yang, and Yanqi Zhou. Deep learning scaling is predictable, empirically, 2017, 1712.00409. 18 

- [JGH18] Arthur Jacot, Franck Gabriel, and Clément Hongler. Neural tangent kernel: Convergence and generalization in neural networks. In _Advances in neural information processing systems_ , pages 8571–8580, 2018. 18 

- [KB14] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization, 2014, 1412.6980. 7 

- [Kom19] Aran Komatsuzaki. One epoch is all you need, 2019, arXiv:1906.06669. 18 

- [KSH12] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton. Imagenet classification with deep convolutional neural networks. In _Proceedings of the 25th International Conference on Neural Information Processing Systems - Volume 1_ , NIPS’12, pages 1097–1105, USA, 2012. Curran Associates Inc. URL `http://dl.acm.org/citation.cfm?id=2999134.2999257` . 19 

- [LCG<sup>+</sup> 19] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. Albert: A lite bert for self-supervised learning of language representations, 2019, 1909.11942. 9

---

[referencia=85f66a6419d173a7 score=0.000]
with the best performance on step _S_ = 6 _BSC_<sup>.Notethatintheseresults</sup><sup>_thebatchsizeBremainsfixedfor_</sup> _all models_ , which means that these empirical results are not truly optimal. We will account for this in later sections using an adjusted _C_ min to produce cleaner trends. 

The result appears as the heavy black line on the left-hand plot in Figure 1. It can be fit with 



The figure also includes images of individual learning curves to clarify when individual models are optimal. We will study the optimal allocation of compute more closely later on. The data strongly suggests that sample efficiency improves with model size, and we also illustrate this directly in Figure 19 in the appendix.

---

[referencia=85f66a6419d173a7 score=0.000]
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