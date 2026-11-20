[referencia=fed4ebad736ddcea score=0.957]
|_._<br>|0<br>20<br>40<br>60<br>80<br>100<br>Training Epochs|



Figure 4: The best (solid line) and worst (dashed line) trials of each method from 10 trials of SimCLR for each method on ImageNet1k with 40 epochs of learning rate warmup. We show classification performance alongside relevant metrics from the first attention layer (top to bottom): attention entropy, the spectral norm of the attention weights, and the _ℓ∞_ –gradient norm of the attention weights. We see that the _Frozen Patcher_ method functions as intended, regulating its gradient norm, and protecting it from the large gradient norms inducing instability in _Baseline_ . We also observe a second form of instability during training: the growing spectral norm leads to a poorly behaved attention mechanism, entropy collapse, and a drop in performance as described in Section 3. This affects _Baseline_ , as well as _Frozen Patcher_ , as neither method gives specific protection against this second type of instability (solid and dashed red, and dashed green lines). Finally, we see that _σ_ Reparam with and without pre-LN regulate both the gradient norms, as well as the spectral norms, giving defense against both types of instability. 

We observe two types of instability. The first, as observed in Chen et al. (2021), is induced by large gradient norms in early layers. The second, described in Section 3, relates to entropy collapse. We find that _Frozen Patcher_ protects 

8 

A PREPRINT - JULY 26, 2023 

- 60 <u>Baseline</u> 40 20 0 

- 60 <u>Frozen Patcher</u> 



<!-- Start of picture text -->
Frozen Patcher<br><!-- End of picture text -->

40 20 0 60 

60 _<u>σ</u>_ <u>Reparam + Pre-LN</u> 40 20 0 60 _<u>σ</u>_ <u>Reparam</u> 

40 20 0 0 20 40 60 80 100 Training Epochs

---

[referencia=fed4ebad736ddcea score=0.951]
Figure 8: Training stability of a Vision Transformer under sharp reductions of its temperature by 10 _×_ , varying at what epoch in training the intervention occurs. We plot (left, top to bottom) training performance, the spectral norm of the first attention projection matrix, the attention entropy of the first attention block, the learning rate and the temperature, (right, top to bottom) the largest to fifth largest singular values of the Hessian by magnitude. We see that interventions in the warmup period – at epochs 10 and 20 – induce a sharp drop in the entropy _α_<sup>(1)</sup> of the attention mechanism in the first Transformer block. This is accompanied by an increase in the sharpness _|λ_ 1 _|_ beyond the stability threshold Cohen et al. (2021, 2022) (black dashed), resulting in training instability. Interventions afterwards, at epochs 20, 30, 50 and 80 all induce a drop in attention entropy, but no entropy collapse. These models also recover as the sharpness does not exceed the stability threshold. We also show the performance of an unintervened Transformer (None). 

19 

A PREPRINT - JULY 26, 2023 

60 10<sup>10</sup> 10<sup>7</sup> 40 10<sup>4</sup> 20 50 25 0 0 0 5 10 15 20 25 30 10<sup>10</sup> 10<sup>7</sup> 20 10<sup>4</sup> 10 50 25 0 0 5 10 15 20 25 5 10<sup>10</sup> 4 10<sup>7</sup> 3 10<sup>4</sup> 2 50 1 25 0 0

---

[referencia=fed4ebad736ddcea score=0.948]
Wang et al. (2022); Liu et al. (2020a) are recent works that proposed to rescale residual connections. To stabilize training and resolve vanishing gradients problem in deep post-LN models to preserve post-LN generalization properties. We focus in this paper on Wang et al. (2022), DeepNorm, solution (it uses post-LN and rescale residual connections depending on the initial model depth) as they reported ability to train up to 1000-depth Transformer models. We are able to reproduce DeepNorm results for 6L-6L, 18L-18L and 50L-50L depths observing stable training (no any models diverged and training went nicely). However we see no performance gain of a 50L-50L depth model over a 18L-18L model. Furthermore, we observe instability in training of the 100L-100L model resulting in only 1 successful run among 3 (only seed is varied) while 2 others are diverging after some time (training loss is growing). By close inspection of the training behaviour we do not see any drastic issue of vanishing gradients, however we see the attention entropy collapse happening, see Figure 18. First of all, attention entropy is not bounded for DeepNorm even in 18L-18L and 50L-50L similarly to what we observed in post-LN models. Also a tiny attention entropy collapse happens in 50L-50L (see top plot in Figure 18) though it does not lead to any divergence. Second, attention entropy collapse is clearly pronounced for 100L-100L models (second, third, and forth rows of Figure 18) leading to 2/3 seeds divergence and one with worse performance than 50L-50L models<sup>13</sup> . Finally, it is interesting to note that attention entropy collapse in 100L-100L can happen for different layers, first and / or last, and with different regimes for the encoder/decoder self-attention and the encoder-decoder cross-attention. 

All models performance on validation and test sets across depths as well as the number of successful runs are reported in Table 11. 

> 13From our empirical observations in other domains it could be that deeper models are worse as any attention entropy collapse degrades optimization process resulting in worse generalization. 

31 

A PREPRINT - JULY 26, 2023

---

[referencia=fed4ebad736ddcea score=0.946]
To further demonstrate this connection, we modify the Transformer to have a global temperature by dividing the pre-softmax (logits) matrix of each attention mechanism by a scalar quantity whose default value is 1. Modifying the temperature gives direct control over the attention entropy, enabling the investigation of a causal connection between entropy collapse and training instability (see Figure 2 and Figures 8 and 9 in Appendix B). Here we train a ViT-B/16 on ImageNet1k. At an _intervention epoch_ we modify the temperature from its default value to 0.1. We see that when performing this intervention during warmup, attention entropy drops to near zero and training becomes unstable. A late intervention also causes a drop in entropy and accuracy curves, however, the model is able to recover to a higher attention entropy regime, although yielding a lower accuracy than non-intervened training. 

3 

A PREPRINT - JULY 26, 2023 



<!-- Start of picture text -->
To further understand these phenomena, we computed the  sharpness  – the largest singular value of the Hessian (the<br>second order derivative of the loss with respect to the model parameters), as its magnitude has implications for training<br>stability Ghorbani et al. (2019); Yao et al. (2020); Cohen et al. (2021, 2022); Gilmer et al. (2021). When sharpness<br>exceeds an algorithm-dependent stability threshold, training iterations diverge Cohen et al. (2021, 2022). We see that<br>interventions inducing the largest drop in attention entropy result in the sharpness exceeding the stability threshold,<br>whereas the later interventions do not cause the threshold to be crossed, explaining how they can recover. For details on<br>the empirical setup and additional results see Appendix B.<br><!-- End of picture text -->



<!-- Start of picture text -->

---

[referencia=fed4ebad736ddcea score=0.937]
Figure 16: Attention entropy behaviour for MT models trained on WMT’17 with pre-LN for 18L-18L (top) and 100L-100L (bottom): encoder self-attention (left), encoder-decoder cross-attention (middle) and decoder self-attention (right). We plot training (dashed, green) and validation (dot-dashed, blue) losses and attention entropy across all Transformer layers (solid): a lighter color corresponds to a deeper layer. Both deep and shallow pre-LN models have nicely bounded attention entropy and no instability issues are observed across runs with different seeds. 

For post-LN models, we reproduced stable results for 6L-6L depth and observe nicely bounded attention entropy behaviour. However for 18L-18L configurations, divergence is observed when varying the random seed. By close inspection we observe no vanishing gradients problem while attention entropy collapse clearly occurs during training (compare top and middle in Figure 17) in the encoder attention and the encoder-decoder cross-attention. Deeper models, namely 50L-50L and 100L-100L, are unable to train and we observe the same vanishing gradients problem as reported by Wang et al. (2022); Liu et al. (2020a) as well as attention entropy collapse for some of the deep layers across the board, see bottom plot in Figure 17. 

12Note, we did not do any hyperparameters search to investigate how models behave with, e.g., wider range of learning rates as we did for ASR models. 

30 

A PREPRINT - JULY 26, 2023 



<!-- Start of picture text -->

---

[referencia=fed4ebad736ddcea score=0.936]
### **5 Conclusion** 

Transformer training stability is a well acknowledged, but still unsolved problem. This problem comes with many facets, and there are multiple necessary conditions that need to be met in order to guarantee stable and robust training. Our work identifies attention entropy collapse as a unique failure pattern that seems to be commonly observed in a wide range of settings and tasks. We also show that _σ_ Reparam as a simple reparameterization of the weights can effectively address the entropy collapse problem, which often leads to improved training stability and robustness. 

There are also limitations of our work. First of all, it is unclear if there is a causal relationship between entropy collapse and training instability of Transformers. We believe that establishing such a connection will enable a deeper understanding of the challenges of Transformer training from the optimization perspective. Second, _σ_ Reparam, while effective, is not a panacea. In the practical sense, one might still benefit from combining _σ_ Reparam with many other 

11 

A PREPRINT - JULY 26, 2023 

useful techniques, including initialization, feature normalization, advanced optimizers, etc. We hope that our work opens new perspectives towards inventing new design and training principles in the future. 

**6 Acknowledgement** 

We would like to thank Navdeep Jaitly, Vimal Thilak, Russ Webb for their helpful feedback and critical discussions on 

the experimental part of the work; Samy Bengio, Andy Keller, Russ Webb, Luca Zappella for their help throughout the process of writing this paper; Hassan Babaie, Mubarak Seyed Ibrahim, Li Li, Evan Samanas, Cindy Liu, Guillaume Seguin, Okan Akalin, and the wider Apple infrastructure team for assistance with developing scalable, fault tolerant code; and Shuming Ma for providing details on the DeepNorm reproduction steps. Names are listed in alphabetical order.

---

[referencia=fed4ebad736ddcea score=0.936]
<br>Training step Training step Training step<br>4 encoder-1 encoder-100 15 . 0 4 cross-1 cross-100 15 . 0 4 decoder-1 decoder-100 15 . 0<br>12 . 5 12 . 5 12 . 5<br>3 3 3<br>10 . 0 10 . 0 10 . 0<br>2 2 2<br>7 . 5 7 . 5 7 . 5<br>1 1 1<br>5 . 0 5 . 0 5 . 0<br>0 0 0<br>0 5000 10000 15000 20000 0 5000 10000 15000 20000 0 5000 10000 15000 20000<br>Training step Training step Training step<br>Training Loss<br>Attention Entropy<br>Training Loss<br>Attention Entropy<br>Training Loss<br>Attention Entropy<br>Training Loss<br>Attention Entropy<br><!-- End of picture text -->

Figure 18: Attention entropy behaviour for MT models trained on WMT’17 with DeepNorm (Wang et al., 2022) (residual rescaling and post-LN) for 50L-50L (row 1) and 100L-100L with three seeds (2-4 rows): encoder self-attention (left), encoder-decoder cross-attention (middle) and decoder self-attention (right). We plot training (dashed, green) and validation (dot-dashed, blue) losses and attention entropy across all Transformer layers (solid): a lighter color corresponds to a deeper layer. While DeepNorm solves vanishing gradient problem for deep models we observe attention entropy collapse phenomenon in both 50L-50L and 100L-100L models. While the 50L-50L model can recover from attention entropy collapse (happens in encoder layers) and nicely converge, 100L-100L suffers from it and can diverge. While Wang et al. (2022) reported stable training for 100L-100L we are unable to reproduce their results and observe 2/3 runs with different seeds (the rest of hyperparameters are the same as reported in the paper) diverge with attention entropy collapse.

---

[referencia=fed4ebad736ddcea score=0.923]
Figure 9: Training stability of a Vision Transformer under modifications of its temperature at epoch 10 in training. We plot (left, top to bottom) training performance, the spectral norm of the first attention projection matrix, the attention entropy of the first attention block, the learning rate and the temperature, (right, top to bottom) the largest to fifth largest singular values of the Hessian by magnitude. We see that reducing the temperature to below 0.15 causes a sharp drop in the entropy _α_<sup>(1)</sup> of the attention mechanism in the first Transformer block and an increase in the sharpness _|λ_ 1 _|_ beyond the stability threshold Cohen et al. (2021, 2022) (black dashed), resulting in training instability. Temperatures larger than 0.16 but lower than 1 do not induce training as they do not cross the stability threshold, although these interventions cause a moderate drop in attention entropy before recovery. We also investigated increasing the temperature, to ensure we were not just “shocking” the system, and in fact it is a drop in temperature that is particularly problematic. Setting the temperature to 100 increases the entropy as expected, but also induces a drop in performance. These models also recover as the sharpness does not exceed the stability threshold. 

20 

A PREPRINT - JULY 26, 2023

---

[referencia=fed4ebad736ddcea score=0.911]
- epochs (69.6 %) and 300 epochs (74.5 %) epochs, as well as very stable training over many trials, both at long and short learning rate warmup. 

9 

A PREPRINT - JULY 26, 2023 



<!-- Start of picture text -->
70<br>60<br>Baseline<br>50 Frozen Patcher<br>σ Reparam + Pre-LN<br>40 σ Reparam<br>1 2 3 4 5 6 7 8 9 10<br>Run rank<br>Test Top 1 (%)<br><!-- End of picture text -->

Figure 6: Linear probe performance on ImageNet1k at the end of training over 10 trials for each method. Trials are ordered by decreasing performance, with run rank 1 (10) corresponding to the best (worst) trial. _Frozen Patcher_ and _σReparam + pre-LN_ produce the best individual runs, with _σReparam_ marginally lower. _σReparam + pre-LN_ and _σReparam_ are the methods most reliably giving good performance, with _Baseline_ and _Frozen Patcher_ each susceptible to at least one instability type. 



<!-- Start of picture text -->
3<br>2<br>1<br>0<br>3<br>2<br>1<br>0<br>15 DeepNorm<br>+  σ Reparam(0.1)<br>10<br>5<br>2000 4000 6000 8000<br>Training Steps<br>)(95 Entropy<br>α<br>Self-<br>)(95 Entropy<br>α<br>Cross-<br>Training Loss<br><!-- End of picture text -->

Figure 7: MT training on WMT’17 for 100L-100L DeepNorm and DeepNorm with injected _σ_ Reparam across 3 runs with different seeds: training loss (bottom), encoder self-attention entropy (top) and encoder-decoder cross-attention entropy (middle) for 95th layers. Attention entropy collapse with further model divergence is observed for DeepNorm, while _σ_ Reparam is bounding entropy and provides stable training.

---

[referencia=fed4ebad736ddcea score=0.911]
### **1 Introduction** 

Transformers (Vaswani et al., 2017) are state-of-the-art models in many application domains. Despite their empirical success and wide adoption, great care often needs to be taken in order to achieve good training stability and convergence. In the original paper (Vaswani et al., 2017), residual connections and Layer Normalizations (LNs) (Ba et al., 2016) are extensively used for each attention and MLP block (specifically, in the post-LN fashion). There has since been various works attempting to promote better training stability and robustness. For example, the pre-LN (Radford et al., 2019) scheme has gained wide popularity, where one moves the placement of LNs to the beginning of each residual block. Others have argued that it is important to properly condition the residual connections. Bachlechner et al. (2021) proposes to initialize the residual connections to zero to promote better signal propagation. Zhang et al. (2019); Huang et al. (2020) remove LNs with carefully designed initializations. 

In this work, we study the training instability of Transformers through the lens of training dynamics. We start by monitoring the entropy of the attention maps averaged over all query positions, heads and examples. We have found that the attention entropy is tightly correlated with the model’s stability and convergence. In particular, small attention entropy is often accompanied with slow convergence, fluctuations in training loss and, in the worst case, divergence. As a motivator, we plot the attention entropy curves of a highly optimized Vision Transformer (ViT) (Dosovitskiy et al., 2021; Touvron et al., 2021) in Figure 1. We observe an initial loss oscillation happening at the same time with sharp dips of the attention entropy curves. When doubling the default learning rate, all attention entropy collapses to near zero and training diverges. In addition, we show in Figures 4 and 7 two sets of experiments of baseline Transformers models with training instability occurring at the same time of entropy collapse. And more generally, similar observations can be made in a wide range of model/task settings if hyperparameters such as learning rate, warmup, initialization are not carefully tuned.

---

[referencia=fed4ebad736ddcea score=0.897]
#### **B.1 Experimental Outline** 

Here we will investigate the interplay between entropy collapse and training stability by asking: _would a model with stable training but not exhibiting entropy collapse have been stable if entropy collapse was induced, all other factors held constant?_ In do-calculus (Pearl, 2009), this roughly corresponds to checking 



**Inducing entropy collapse** Note that logits **_u_** _∈_ R<sup>_d_</sup> and temperature _τ_ give rise to the temperature normalized softmax 



and corresponding entropy 



Holding **_u_** constant, the entropy is low when _τ →_ 0, and is high when _τ →∞_ . As entropy collapse is observed in experiments when _Hp_ ( **_u_** _, τ_ ) _→_ 0, we will attempt to induce entropy collapse by sending _τ → τ_ target, where _τ_ target _≪_ 1. 

Concretely, for a Transformer model, we normalize the logits of the attention matrix by temperature. We use the same temperature normalization for every layer, i.e. the Transformer has a _global temperature_ . We start the temperature _τ_ = 1 which corresponds to the default Transformer model without temperature normalization. At a prescribed epoch during training, we perform a _temperature intervention_ , where we change the temperature from _τ_ = 1 to a target temperature _τ_ target. The transition is sharp, and happens at the start of the prescribed epoch, which we refer to as the _intervention epoch_ . 

We use the MAE ViT-B/16 recipe (see Appendix H) for these experiments, and train for a total of 100 epochs on ImageNet1k. To simplify the analysis, we only use ImageNet1k training augmentations, and use no learning rate decay schedule (i.e. the learning rate is flat after warmup). 

**Eigenvalues of the Hessian** As properties of the Hessian have been successfully used to gain an understanding of stability of the learning process Ghorbani et al. (2019); Yao et al. (2020); Cohen et al. (2021, 2022); Gilmer et al. (2021), we will also use them in our analysis. Specifically, we will analyze the magnitude _|λi|_ of the largest magnitude eigenvalues _λi_ of the Hessian _H_

---

[referencia=fed4ebad736ddcea score=0.890]
#### **4.3 Machine Translation** 

In machine translation (MT) stable training of deep encoder-decoder post-LN Transformers is an active research area (Wang et al., 2022; Liu et al., 2020a). Vanishing gradients problem has been reported by many works, leading to different solutions including rescaling residual connections: e.g., Wang et al. (2022) trained a 1000-layer Transformer by properly rescaling residual connections and initialization depending on model depth, dubbed DeepNorm. We examined attention entropy collapse for the deep Transformers in MT and found that they suffer not only from vanishing gradients but also from entropy collapse, both for vanilla post-LN and DeepNorm. By injecting _σ_ Reparam alongside post-LN/DeepNorm, we empirically show that it is able to bound attention entropy and stabilize training without any divergent training loss growth issues. Details on experiments and all findings are in Appendix F. 

10 

A PREPRINT - JULY 26, 2023 

Table 4: Results for MT on WMT’17 English-German data for post-LN, with or without additional _σ_ Reparam, with or without residual rescaling (‘DeepNorm’ from Wang et al. (2022)). We report average BLEU score and its std across 3 runs with different seeds for a variety of encoder-decoder architectures: 6L-6L, 18L-18L, 50L-50L, and 100L-100L. ‘DV’ states for how many times a model diverges / is not training across runs. With red block we mark unstable baseline training while with blue block – training stabilized by _σ_ Reparam.

---

[referencia=fed4ebad736ddcea score=0.886]
<!-- Start of picture text -->
The empirical correlation of entropy collapse and training instability leads to the following questions: 1) How do we<br>prevent entropy collapse? 2) Can we improve training stability by doing so? We answer these by showing that entropy<br>collapse can be effectively prevented by controlling the spectral norms of the query and key projections. In particular,<br>we prove a tight lower bound on the attention entropy, which decreases exponentially fast with the growth of the spectral<br>norm of the attention matrix logits. This bound suggests that entropy collapse can occur swiftly when letting the spectral<br><!-- End of picture text -->

norm of the weights increase uncontrollably. We then provide a simple fix, _σ_ Reparam, which reparameterizes all weight matrices by sequentially applying Spectral Normalization (Miyato et al., 2018) and a learned multiplicative scalar. Intuitively, _σ_ Reparam decouples the update of the spectral norms of weights from their dimensionality, which allows them to update smoothly and in a controlled way. Also note that _σ_ Reparam does not change the model space, which allows one to learn an equally expressive model. 

We evaluate five tasks: image classification, self-supervised learning (SSL), machine translation, automatic speech 

recognition (Appendix E), and language modeling (Appendix G). We highlight the empirical results as follows: 

1. We show that entropy collapse is commonly observed in the baseline models of various benchmarks. 2. Image classification: _σ_ Reparam enables a drastically simplified ViT training recipe by removing pre-LN, learning rate warmup, weight decay and not requiring adaptive optimizers. This recipe leads to equivalent (or slightly better) model performance against baseline training strategies, all the while reducing training duration by 16% . 3. Self-supervised learning: _σ_ Reparam helps to drastically improve the stability and robustness of the SimCLR training, improving upon existing baselines.

---

[referencia=fed4ebad736ddcea score=0.886]
Figure 2: _Training can become unstable due to rapid change in attention logit magnitude._ We train a Vision Transformer, sharply reducing its temperature in the attention logits by 10 _×_ at different intervention epochs. (Blue) Intervention during warmup – at epoch 10 – induces a sharp drop in the attention entropy of the first Transformer block. This is accompanied by an increase in the sharpness, the largest singular value of the Hessian, and exceeds the stability threshold Cohen et al. (2021) (black dashed), resulting in training instability. (Orange) Reduction after warmup – at epoch 50 – induces a less severe drop in attention entropy. The model recovers from this intervention as the sharpness does not exceed the stability threshold, although the resulting performance is lower performance than the model that did not experience any intervention (black solid).

---

[referencia=fed4ebad736ddcea score=0.876]
#### 4. Machine translation: _σ_ Reparam allows us to stabilize very deep post-LN architectures up to 100L-100L encoder- 

decoder layers. 

5. Speech recognition: _σ_ Reparam allows us to improve training stability and simplify the training recipe for post-LN Transformer by removing learning rate warmup and adaptive optimization. 

6. Language modeling: _σ_ Reparam is compatible with causal Transformer architectures, and achieves results competitive with state-of-the-art without using post-LN. 

**2 Related Works** 

Transformers have relied heavily on LNs to achieve training stability. Besides the popular post-LN and pre-LN 

configurations, other variants have been proposed (Wang et al., 2022; Shleifer et al., 2021; Liu et al., 2020a). On the one hand, we show empirically that entropy collapse (and its accompanied training instability) happens even equipped with extensive use of normalization layers. On the other hand, _σ_ Reparam does not rely on specific normalization layers and can even work in the absence of it, while effectively smoothing the attention entropy curves. 

There have also been numerous attempts to design better Transformer initialization schemes, including Zhang et al. (2019); Huang et al. (2020); Yang et al. (2022); Bachlechner et al. (2021). While proper initializations are indeed crucial 

to stable and fast training, we argue that the training dynamics (affected by the optimizer and training hyperparameters) is equally important. _σ_ Reparam in this sense is an orthogonal approach that specifically targets the entropy collapse problem, which makes it compatible with standard initialization methods and provides robust performance.

---

[referencia=fed4ebad736ddcea score=0.858]
> 5The token set consists of the 26 English alphabet letters augmented with the apostrophe and a word boundary token. 

24 

A PREPRINT - JULY 26, 2023 



<!-- Start of picture text -->
LR 1, warmup 32k LR 1, warmup 64k LR 0.5, warmup 64k<br>600 600 600<br>5 5 5<br>500 500 500<br>4 4 4<br>400 400 400<br>3 3 3<br>300 300 300<br>2 2 2<br>200 200 200<br>1 1 1<br>100 100 100<br>0 0 0<br>10000 20000 30000 40000 50000 60000 10000 20000 30000 40000 50000 60000 10000 20000 30000 40000 50000 60000<br>Training Steps Training Steps Training Steps<br>Training Loss<br>Attention Entropy<br><!-- End of picture text -->

Figure 12: Attention entropy collapse is observed for pre-LN ASR models trained on 100h of LibriSpeech when hyperparameters, learning rate and warmup, are varied. For every hyperparameters configuration we plot training loss (dashed, green) and attention entropy for every of 36 layers (solid): a lighter color corresponds to a deeper layer. The right plot (LR 0.5, warmup 64k) gives stable training and the best performance while left (LR 1, warmup 64k) and middle (LR 1 and warmup 32k) have attention entropy collapse phenomenon. 



<!-- Start of picture text -->

---

[referencia=fed4ebad736ddcea score=0.838]
### **ABSTRACT** 

Training stability is of great importance to Transformers. In this work, we investigate the training dynamics of Transformers by examining the evolution of the attention layers. In particular, we track the attention entropy for each attention head during the course of training, which is a proxy for model sharpness. We identify a common pattern across different architectures and tasks, where low attention entropy is accompanied by high training instability, which can take the form of oscillating loss or divergence. We denote the pathologically low attention entropy, corresponding to highly concentrated attention scores, as _entropy collapse_ . As a remedy, we propose _σ_ Reparam, a simple and efficient solution where we reparametrize all linear layers with spectral normalization and an additional learned scalar. We demonstrate that _σ_ Reparam successfully prevents entropy collapse in the attention layers, promoting more stable training. Additionally, we prove a tight lower bound of the attention entropy, which decreases exponentially fast with the spectral norm of the attention logits, providing additional motivation for our approach. We conduct experiments with _σ_ Reparam on image classification, image self-supervised learning, machine translation, speech recognition, and language modeling tasks. We show that _σ_ Reparam provides stability and robustness with respect to the choice of hyperparameters, going so far as enabling training (a) a Vision Transformer to competitive performance without warmup, weight decay, layer normalization or adaptive optimizers; (b) deep architectures in machine translation and (c) speech recognition to competitive performance without warmup and adaptive optimizers. Code is available at `https://github.com/apple/ml-sigma-reparam` . 

**_K_ eywords** Transformers, self-attention, optimization, stability, spectral normalization, self-supervised learning, vision, speech, language, contrastive learning

---

[referencia=fed4ebad736ddcea score=0.829]
### **J Discussion** 

We believe that our experiments have covered representative domains, architectures and training losses for typical Transformer applications. The key factors that affect training stability are the initial token embedding layer (where for vision and speech tasks they are based on convolution projections, and for MT and language modeling are with word embeddings), topology of architecture (encoder mode for vision and speech, encoder-decoder for MT and decoder for language modeling), and the training loss (cross-entropy loss, contrastive and CTC loss). While each of these design choices may bring their own challenges for training, we show that entropy collapse is a common symptom accompanying instability and _σ_ Reparam is a general fix compatible with all settings.

---

[referencia=fed4ebad736ddcea score=0.822]
**Attention entropy collapse occurs in deep models.** While we reproduced stable results for 6L-6L post-LN and observed nicely bounded attention entropy behaviour, for 18L-18L configurations, divergence is observed when varying the random seed. By close inspection we observe no vanishing gradients problem, but attention entropy collapse clearly occurs during training. Deeper models, namely 50L-50L and 100L-100L, are unable to train due to vanishing gradients as well as attention entropy collapse for some of the deep layers (Figure 17). For DeepNorm while we are able to reproduce results for 6L-6L, 18L-18L and 50L-50L depths observing stable training (no any models diverged and training behaved well), yet we observe instability in training of the 100L-100L model, resulting in only 1 over 3 (different seeds) successful run. By closer inspection of the training behaviour we do not see any drastic issue of vanishing gradients, however we see attention entropy collapse, see Figures 7 and 18. 

_σ_ **Reparam resolves entropy collapse in deep models.** To alleviate attention entropy collapse and confirm _σ_ Reparam effectiveness for deep models we inject _σ_ Reparam into post-LN and DeepNorm models. As a result, _σ_ Reparam nicely bounds attention entropy for 18L-18L and 50L-50L post-LN models (Figure 19), resolving any divergence issues as well as vanishing gradients in the 50L-50L model. _σ_ Reparam also nicely bounds attention entropy for 18L-18L, 50L-50L, 100L-100L DeepNorm models (Figure 20), resolving any divergence issues for 100L-100L, see Figure 7 (vanishing gradients are not observed as DeepNorm targets it). In terms of performance (Table 4), _σ_ Reparam with post-LN or DeepNorm matches their baselines for 6L-6L and in the same ballpark for 18L-18L. However, _σ_ Reparam is inferior to DeepNorm for 50L-50L and 100L-100L.

---

[referencia=fed4ebad736ddcea score=0.784]
#### **E.2 Training Stability, Robustness and Generalization** 

We start with exploring training stability of the baseline model described above using both pre-LayerNorm (pre-LN) and post-LayerNorm (post-LN) configurations trained on small-scale data, namely 100h of LibriSpeech ( _train-clean-100_ ). By varying different hyperparameters, such as learning rate, warmup, and gradient clipping, post-LN models fail to train. By inspecting the gradient norms per layer and per each parameters’ matrix we find a similar vanishing gradients problem as reported, e.g., by Liu et al. (2020b,a); Wang et al. (2022) for deep Transformers ( _>_ 12 layers) in machine translation domain. At the same time, pre-LN is stable as reported by, e.g., Nguyen & Salazar (2019); Wang et al. (2022); Liu et al. (2020a): we are able to reduce warmup from 64k to 16k, increase learning rate from 0.03 to 0.5, and obtain better results than the training setting from the post-LN baseline. However, stable training of pre-LN leads to a degradation in performance compared to post-LN in ASR, similarly as reported in the aforementioned works: validation WER is worse while training loss is lower, see top of Table 7. By varying, e.g., learning rate and warmup hyperparameters and deeper inspecting training stability of pre-LN models we observe that attention entropy is not bounded and can collapse leading to the model divergence with training loss growing, see Figure 12.