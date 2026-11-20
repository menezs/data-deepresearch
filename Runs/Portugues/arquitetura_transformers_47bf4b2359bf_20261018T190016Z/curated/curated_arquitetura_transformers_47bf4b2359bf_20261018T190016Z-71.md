[referencia=abee5142f9553110 score=0.981]
# RETHINKING ATTENTION WITH PERFORMERS 

**Krzysztof Choromanski**<sup>_∗_1</sup> **, Valerii Likhosherstov**<sup>_∗_2</sup> **, David Dohan**<sup>_∗_1</sup> **, Xingyou Song**<sup>_∗_1</sup> **Andreea Gane**<sup>_∗_1</sup> **, Tamas Sarlos**<sup>_∗_1</sup> **, Peter Hawkins**<sup>_∗_1</sup> **, Jared Davis**<sup>_∗_3</sup> **, Afroz Mohiuddin**<sup>1</sup> **Lukasz Kaiser**<sup>1</sup> **, David Belanger**<sup>1</sup> **, Lucy Colwell**<sup>1</sup><sup>_,_2</sup> **, Adrian Weller**<sup>2</sup><sup>_,_4</sup> 1Google 2University of Cambridge 3DeepMind 4Alan Turing Institute 

## ABSTRACT 

We introduce _Performers_ , Transformer architectures which can estimate regular (softmax) full-rank-attention Transformers with provable accuracy, but using only linear (as opposed to quadratic) space and time complexity, without relying on any priors such as sparsity or low-rankness. To approximate softmax attentionkernels, Performers use a novel _Fast Attention Via positive Orthogonal Random features_ approach (FAVOR+), which may be of independent interest for scalable kernel methods. FAVOR+ can also be used to efficiently model kernelizable attention mechanisms beyond softmax. This representational power is crucial to accurately compare softmax with other kernels for the first time on large-scale tasks, beyond the reach of regular Transformers, and investigate optimal attention-kernels. Performers are linear architectures fully compatible with regular Transformers and with strong theoretical guarantees: unbiased or nearly-unbiased estimation of the attention matrix, uniform convergence and low estimation variance. We tested Performers on a rich set of tasks stretching from pixel-prediction through text models to protein sequence modeling. We demonstrate competitive results with other examined efficient sparse and dense attention methods, showcasing effectiveness of the novel attention-learning paradigm leveraged by Performers.

---

[referencia=abee5142f9553110 score=0.977]
|FAVOR+ can be also applied to effciently model other kernelizable attention mechanisms beyond<br>softmax. This representational power is crucial to accurately compare softmax with other kernels<br>for the frst time on large-scale tasks, that are beyond the reach of regular Transformers, and fnd for<br>them optimal attention-kernels. FAVOR+ can also be applied beyond the Transformer scope as a<br>more scalable replacement for regular attention, which itself has a wide variety of uses in computer<br>vision (Fu et al., 2019), reinforcement learning (Zambaldi et al., 2019), training with softmax cross<br>entropy loss, and even combinatorial optimization (Vinyals et al., 2015).|
|We test Performers on a rich set of tasks ranging from pixel-prediction through text models to protein<br>sequence modeling. We demonstrate competitive results with other examined effcient sparse and|
|dense attention methods, showcasing the effectiveness of the novel attention-learning paradigm<br>leveraged by Performers. We emphasize that in principle, FAVOR+ can also be combined with other<br>techniques, such as reversible layers (Kitaev et al., 2020) or cluster-based attention (Roy et al., 2020).|
|2<br>FAVOR+ MECHANISM& POSITIVEORTHOGONALRANDOMFEATURES|
|Below we describe in detail the FAVOR+ mechanism - the backbone of thePerformer<sup>_′_</sup>sarchitecture.<br>We introduce a new method for estimating softmax (and Gaussian) kernels with**positive**orthogonal|
|<br>random features which FAVOR+ leverages for the robust and unbiased estimation of regular (softmax)<br>attention and show how FAVOR+ can be applied for other attention-kernels.|
|2.1<br>PRELIMINARIES- REGULAR ATTENTION MECHANISM|

---

[referencia=abee5142f9553110 score=0.969]
|layers (Child et al., 2019). Unfortunately, there is a lack of rigorous guarantees for the representation<br>power produced by such methods, and sometimes the validity of sparsity patterns can only be verifed<br>empirically through trial and error by constructing special GPU operations (e.g. either writing C++<br>CUDA kernels (Child et al., 2019) or using TVMs (Beltagy et al., 2020)). Other techniques which<br>aim to reduce Transformers’ space complexity include reversible residual layers allowing one-time<br>activation storage in training (Kitaev et al., 2020) and shared attention weights (Xiao et al., 2019).<br>These constraints may impede application to long-sequence problems, where approximations of<br>the attention mechanism are not suffcient. Approximations based on truncated back-propagation<br>(Dai et al., 2019) are also unable to capture long-distance correlations since the gradients are only<br>propagated inside a localized window. Other methods propose biased estimation of regular attention<br>but only in the non-causal setting and with large mean squared error (Wang et al., 2020).|
|---|
|In response, we introduce the frst Transformer architectures, _Performers_, capable of **provably**<br>accurate and practical estimation of regular (softmax) full-rank attention, but of only linear space|
|<br>and time complexity and**not relying on any priors**such as sparsity or low-rankness. Performers<br>use the_Fast Attention Via positive Orthogonal Random features_(FAVOR+) mechanism, leveraging<br>new methods for approximating softmax and Gaussian kernels, which we propose. We believe<br>these methods are of independent interest, contributing to the theory of scalable kernel methods.<br>Consequently, Performers are the frst linear architectures **fully compatible** (via small amounts<br>of fne-tuning) with regular Transformers, providing strong theoretical guarantees: unbiased or<br>nearly-unbiased estimation of the attention matrix, uniform convergence and lower variance of the<br>approximation.|

---

[referencia=abee5142f9553110 score=0.968]
## 5 CONCLUSION 

We presented Performer, a new type of Transformer, relying on our Fast Attention Via positive Orthogonal Random features (FAVOR+) mechanism to significantly improve space and time complexity of regular Transformers. Our mechanism provides to our knowledge the first effective unbiased estimation of the original softmax-based Transformer with linear space and time complexity and opens new avenues in the research on Transformers and the role of non-sparsifying attention mechanisms. 

8 

Published as a conference paper at ICLR 2021

---

[referencia=abee5142f9553110 score=0.927]
Transformers rely on a trainable _attention_ mechanism that identifies complex dependencies between the elements of each input sequence. Unfortunately, the regular Transformer scales quadratically with the number of tokens _L_ in the input sequence, which is prohibitively expensive for large _L_ and precludes its usage in settings with limited computational resources even for moderate values of _L_ . Several solutions have been proposed to address this issue (Beltagy et al., 2020; Gulati et al., 2020; Chan et al., 2020; Child et al., 2019; Bello et al., 2019). Most approaches restrict the attention mechanism to attend to local neighborhoods (Parmar et al., 2018) or incorporate structural priors on attention such as sparsity (Child et al., 2019), pooling-based compression (Rae et al., 2020) clustering/binning/convolution techniques (e.g. (Roy et al., 2020) which applies _k_ -means clustering to learn dynamic sparse attention regions, or (Kitaev et al., 2020), where locality sensitive hashing is used to group together tokens of similar embeddings), sliding windows (Beltagy et al., 2020), or truncated targeting (Chelba et al., 2020). There is also a long line of research on using dense attention matrices, but defined by low-rank kernels substituting softmax (Katharopoulos et al., 2020; Shen et al., 2018). Those methods critically rely on kernels admitting explicit representations as dot-products of finite positive-feature vectors. 

The approaches above do not aim to approximate regular attention, but rather propose simpler and more tractable attention mechanisms, often by incorporating additional constraints (e.g. identical query and key sets as in (Kitaev et al., 2020)), or by trading regular with sparse attention using more 

> _∗_ Equal contribution. Correspondence to {kchoro,lcolwell}@google.com. 

> Code for Transformer models on protein data can be found in github.com/google-research/ google-research/tree/master/protein_lm and Performer code can be found in github.com/ google-research/google-research/tree/master/performer. Google AI Blog: https:// ai.googleblog.com/2020/10/rethinking-attention-with-performers.html 

1 

Published as a conference paper at ICLR 2021

---

[referencia=abee5142f9553110 score=0.921]
### 4.3 SOFTMAX APPROXIMATION ON TRANSFORMERS 

Even if the approximation of the attention mechanism is tight, small errors can easily propagate throughout multiple Transformer layers (e.g. MLPs, multiple heads), as we show in Fig. 14 (Appendix). In other words, the model’s _Lipschitz constant_ can easily scale up small attention approximation error, which means that very tight approximations may sometimes be needed. Thus, when applying FAVOR(+)’s softmax approximations on a Transformer model (i.e. "Performer-XSOFTMAX"), we demonstrate that: 

**1.** Backwards compatibility with pretrained models is available as a benefit from softmax approximation, via small finetuning (required due to error propagation) even for trigonometric features (Fig. 5, left) on the LM1B dataset (Chelba et al., 2014). However, when on larger dataset PG-19, **2.** Positive (POS) softmax features (with redrawing) become crucial for achieving performance matching regular Transformers (Fig. 5, right). 



Figure 5: We transferred the original pretrained Transformer’s weights into the Performer, which produces an initial non-zero 0.07 accuracy (dotted orange line), but quickly recovers accuracy in a small fraction of the original number of gradient steps. However on PG-19, Trigonometric (TRIG) softmax approximation becomes highly unstable (full curve in Appendix D.2), while positive features (POS) (without redrawing) and Linformer (which also approximates softmax) _even with redrawn projections_ , plateau at the same perplexity. Positive softmax with feature redrawing is necessary to match the Transformer, with SMREG (regularization from Sec. 3) allowing faster convergence. Additional ablation studies over many attention kernels, showing also that trigonometric random features lead even to NaN values in training are given in Appendix D.3. 

7 

Published as a conference paper at ICLR 2021

---

[referencia=abee5142f9553110 score=0.920]
6 

Published as a conference paper at ICLR 2021 

We observed (Fig. 3) that in terms of _L_ , the Performer reaches nearly linear time and sub-quadratic memory consumption (since the explicit _O_ ( _L_<sup>2</sup> ) attention matrix is not stored). In fact, the Performer achieves nearly optimal speedup and memory efficiency possible, depicted by the "X"-line when attention is replaced with the "identity function" simply returning the **V** -matrix. The combination of both memory and backward pass efficiencies for large _L_ allows respectively, large batch training and lower wall clock time per gradient step. Extensive additional results are demonstrated in Appendix E by varying layers, raw attention, and architecture sizes. 

### 4.2 SOFTMAX ATTENTION APPROXIMATION ERROR 

We further examined the approximation error via FAVOR+ in Fig. 4. We demonstrate that **1.** Orthogonal features produce lower error than unstructured (IID) features, **2.** Positive features produce lower error than trigonometric sin/cos features. These two empirically validate the PORF mechanism. 





Figure 4: MSE of the approximation output when comparing Orthogonal vs IID features and trigonometric sin/cos vs positive features. We took _L_ = 4096 _, d_ = 16, and varied the number of random samples _m_ . Standard deviations shown across 15 samples of appropriately normalized random matrix input data. 

To further improve overall approximation of attention blocks across multiple iterations which further improves training, random samples should be periodically redrawn (Fig. 5, right). This is a cheap procedure, but can be further optimized (Appendix B.2).

---

[referencia=abee5142f9553110 score=0.898]
### 2.4 ORTHOGONAL RANDOM FEATURES (ORFS) 

The above constitutes the R+ part of the FAVOR+ method. It remains to explain the O-part. To further reduce the variance of the estimator (so that we can use an even smaller number of random features _r_ ), we entangle different random samples _ω_ 1 _, ..., ωm_ to be **exactly** orthogonal. This can be done while maintaining unbiasedness whenever isotropic distributions _D_ are used (i.e. in particular in all kernels we considered so far) by the standard Gram-Schmidt orthogonalization procedure (see (Choromanski et al., 2017) for details). ORFs is a well-known method, yet it turns out that it works particularly well with our introduced PRFs for softmax. This leads to the **first theoretical results** showing that ORFs can be applied to reduce the variance of softmax/Gaussian kernel estimators **for any** dimensionality _d_ rather than just asymptotically for large enough _d_ (as is the case for previous methods, see: next section) and leads to the **first exponentially small bounds** on large deviations probabilities that are strictly smaller than for non-orthogonal methods. Positivity of random features plays a key role in these bounds. The ORF mechanism requires _m ≤ d_ , but this will be the case in all our experiments. The pseudocode of the entire FAVOR+ algorithm is given in Appendix B. 

Our theoretical results are tightly aligned with experiments. We show in Section 4 that PRFs+ORFs drastically improve accuracy of the approximation of the attention matrix and enable us to reduce _r_ which results in an accurate as well as space and time efficient mechanism which we call FAVOR+.

---

[referencia=abee5142f9553110 score=0.872]
> Here Att<sup>�</sup> _↔_ stands for the approximate attention and brackets indicate the order of computations. It is easy to see that such a mechanism is characterized by space complexity _O_ ( _Lr_ + _Ld_ + _rd_ ) and time complexity _O_ ( _Lrd_ ) as opposed to _O_ ( _L_<sup>2</sup> + _Ld_ ) and _O_ ( _L_<sup>2</sup> _d_ ) of the regular attention (see also Fig. 1). 



Figure 1: Approximation of the regular attention mechanism **AV** (before **D**<sup>_−_1</sup> -renormalization) via (random) feature maps. Dashed-blocks indicate order of computation with corresponding time complexities attached. 

The above scheme constitutes the FA-part of the FAVOR+ mechanism. The remaining OR+ part answers the following questions: **(1)** How expressive is the attention model defined in Equation 3, and in particular, can we use it in principle to approximate regular softmax attention ? **(2)** How do we implement it robustly in practice, and in particular, can we choose _r ≪ L_ for _L ≫ d_ to obtain desired space and time complexity gains? We answer these questions in the next sections. 

2.3 HOW TO AND HOW NOT TO APPROXIMATE SOFTMAX-KERNELS FOR ATTENTION 

It turns out that by taking _φ_ of the following form for functions _f_ 1 _, ..., fl_ : R _→_ R, function iid _g_ : R<sup>_d_</sup> _→_ R and deterministic vectors _ωi_ or _ω_ 1 _, ..., ωm ∼D_ for some distribution _D ∈P_ (R<sup>_d_</sup> ):

---

[referencia=abee5142f9553110 score=0.855]
Figure 13: Amino acid similarity matrix estimated from attention matrices aggregated across a small subset of sequences, as described in Vig et al. (Vig et al., 2020). The sub-figures correspond respectively to: **(1)** the normalized BLOSUM matrix, **(2)** the amino acid similarity estimated via a trained Performer model. Note that the Performer recognizes highly similar amino acid pairs such as (D, E) and (F, Y). 

22 

Published as a conference paper at ICLR 2021 

D EXTENDED APPROXIMATION AND COMPARISON RESULTS 

D.1 BACKWARDS COMPATIBILITY - ERROR PROPAGATION Although mentioned previously (Sec. 4.2) that the Performer with additional finetuning is backwards compatible with the Transformer, we demonstrate below in Fig. 14 that error propagation due to nonattention components of the Transformer is one of the primary reasons that pretrained Transformer weights cannot be immediately used for inference on the corresponding Performer. 



Figure 14: Output approximation errors between a vanilla Transformer and a Performer (with orthogonal features) for varying numbers of layers. 

D.2 APPROXIMATE SOFTMAX - EXTENDED PROPERTIES We show the following properties of our softmax approximation, in Fig. 15: **Redrawing:** While the benefits of redrawing features was shown in Subsec. 4.3 of the main body of the paper, we also demonstrate its benefits when there are multiple layers with large scale (16x16 TPU-v2) training. **Unidirectional:** While we have shown on TrEMBL that Performer with generalized ReLU attention outperforms softmax, we also show that approximate softmax attention can still be a solid choice, for example on ImageNet64 (U). After 100K steps of training, the Performer-ReLU, Performer-Softmax, and Performer-Softmax (SMREG) variants achieve respectively, 3.67, 3.69, 3.67 BPD. **Instability of Trigonometric Features:** We see the full view of the unstable training curve when using Trigonometric softmax.

---

[referencia=abee5142f9553110 score=0.821]
There is however a caveat there. The attention module from (1) constructs for each token, a convex combination of value-vectors with coefficients given as corresponding renormalized kernel scores. That is why kernels producing non-negative scores are used. Applying random feature maps with potentially negative dimension-values (sin _/_ cos) leads to unstable behaviours, especially when kernel scores close to 0 (which is the case for many entries of **A** corresponding to low relevance tokens) are approximated by estimators with large variance in such regions. This results in abnormal behaviours, e.g. negative-diagonal-values renormalizers **D**<sup>_−_1</sup> , and consequently either completely prevents training or leads to sub-optimal models. We demonstrate empirically that this is what happens for SM�trig _m_ and provide detailed theoretical explanations showing that the variance of SM<sup>�</sup> trig _m_ is large as approximated values tend to 0 (see: Section 3). This is one of the main reasons why the robust random feature map mechanism for approximating regular softmax attention was never proposed. 

We propose a robust mechanism in this paper. Furthermore, the variance of our new unbiased positive random feature map estimator tends to 0 as approximated values tend to 0 (see: Section 3). **Lemma 1** (Positive Random Features (PRFs) for Softmax) **.** _For_ **x** _,_ **y** _∈_ R<sup>_d_</sup> _,_ **z** = **x** + **y** _we have:_

---

[referencia=abee5142f9553110 score=0.814]
### A.2 TRAINING HYPERPARAMETERS 

Unless specifically stated, all Performer + Transformer runs by default used 0 _._ 5 grad clip, 0 _._ 1 weight decay, 0 _._ 1 dropout, 10<sup>_−_3</sup> fixed learning rate with Adam hyperparameters ( _β_ 1 = 0 _._ 9 _, β_ 2 = 0 _._ 98 _, ϵ_ = 10<sup>_−_9</sup> ), with batch size maximized (until TPU memory overload) for a specific model. 

All 36-layer protein experiments used the same amount of compute (i.e. 16x16 TPU-v2, 8GB per chip). For concatenated experiments, 16x16 TPU-v2’s were also used for the Performer, while 8x8’s were used for the 1-3 layer ( _d_ = 256) Transformer models (using 16x16 did not make a difference in accuracy). 

**Note that Performers are using the same training hyperparameters as Transformers, yet achieving competitive results** - this shows that FAVOR can act as a simple drop-in without needing much tuning. 

### A.3 APPROXIMATE SOFTMAX ATTENTION DEFAULT VALUES 

The optimal values, set to default parameters<sup>1</sup> , are: renormalize_attention = True, numerical stabilizer = 10<sup>_−_6</sup> , number of features = 256, ortho_features = True, ortho_scaling = 0.0. 

> 1https://github.com/google-research/google-research/blob/master/ performer/fast_attention 

15 

Published as a conference paper at ICLR 2021 

### A.4 GENERALIZED ATTENTION DEFAULT VALUES 

The optimal values, set to default parameters<sup>2</sup> , are: renormalize_attention = True, numerical stabilizer = 0.0, number of features = 256, kernel = ReLU, kernel_epsilon = 10<sup>_−_3</sup> .

---

[referencia=abee5142f9553110 score=0.793]
In Fig. 2 we visualize the advantages of positive versus standard trigonometric random features. In critical regions, where kernel values are small and need careful approximation, our method outperforms its counterpart. In Section 4 we further confirm our method’s advantages empirically, using positive features to efficiently train softmax-based linear Transformers. If we replace in (7) _ω_ with _√d ∥_<sup>_<u>ω</u>_</sup> _ω∥_<sup>, we obtain the so-called</sup><sup>**regularized softmax-kernel**SMREG which we can approximate in</sup> a similar manner, simply changing _D_ = _N_ (0 _,_ **I** _d_ ) to _D_ = Unif( _√dS_<sup>_d−_1</sup> ), a distribution correspond� + ing to Haar measure on the sphere of radius _√d_ in R<sup>_d_</sup> , obtaining estimator SMREG _m_<sup>.As we show</sup> in Section 3, such random features can also be used to accurately approximate regular softmax-kernel. 

4 

Published as a conference paper at ICLR 2021

---

[referencia=abee5142f9553110 score=0.779]
### A.5 REFORMER DEFAULT VALUES 

For the Reformer, we used the same hyperparameters as mentioned for protein experiments, without gradient clipping, while using the defaults<sup>3</sup> (which instead use learning rate decay) for ImageNet-64. In both cases, the Reformer used the same default LSH attention parameters. 

### A.6 LINFORMER DEFAULT VALUES 

Using our standard pipeline as mentioned above, we replaced the attention function with the Linformer variant via Jax, with _δ_ = 10<sup>_−_6</sup> _, k_ = 600 (same notation used in the paper (Wang et al., 2020)), where _δ_ is the exponent in a renormalization procedure using _e_<sup>_−δ_</sup> as a multiplier in order to approximate softmax, while _k_ is the dimension of the projections of the **Q** and **K** matrices. As a sanity check, we found that our Linformer implementation in Jax correctly approximated exact softmax’s output within 0 _._ 02 error for all entries. 

Note that for rigorous comparisons, our Linformer hyperparameters are even stronger than the defaults found in (Wang et al., 2020), as: 

- We use _k_ = 600, which is more than twice than the default _k_ = 256 from the paper, and also twice than our default _m_ = 256 number of features. 

- We also use redrawing, which avoids "unlucky" projections on **Q** and **K** . 

> 2https://github.com/google-research/google-research/blob/master/ performer/fast_attention 

> 3https://github.com/google/trax/blob/master/trax/supervised/configs/ reformer_imagenet64.gin 

16 

Published as a conference paper at ICLR 2021

---

[referencia=abee5142f9553110 score=0.736]
We see that ORFs provide exponentially small and sharper bounds for critical regions where the softmax-kernel is small. Below we show that even for the SM<sup>trig</sup> mechanism with ORFs, it suffices to take _m_ = Θ( _d_ log( _d_ )) random projections to accurately approximate the attention matrix (thus if not attention renormalization, PRFs would not be needed). In general, _m_ depends on the dimensionality _d_ of the embeddings, radius _R_ of the ball where all queries/keys live and precision parameter _ϵ_ (see: Appendix F.6 for additional discussion), but does not depend on input sequence length _L_ . **Theorem 4** (uniform convergence for attention approximation) **.** _Assume that L_ 2 _-norms of queries/keys are upper-bounded by R >_ 0 _. Define l_ = _Rd_<sup>_−_</sup><sup><u>1</u></sup> 4 _and take h_<sup>_∗_</sup> = exp(<sup>_<u>l</u>_</sup> 2<sup>2)</sup><sup>_.Then_</sup> <u>3</u> _for any ϵ >_ 0 _, δ_ = ( _h_<sup>_∗_</sup> _<u>ϵ</u>_ )<sup>2</sup><sup>_andthenumberofrandomprojectionsm_=Θ(</sup> _δ_<sup>_<u>d</u>_2log(</sup><sup><u>4</u></sup><sup>_<u>d</u>_</sup> _δ_ 4 _<u>R</u>_ )) _the following holds for the attention approximation mechanism leveraging estimators_ SM<sup>�</sup> trig _with ORFs: ∥_ **A**<sup>�</sup> _−_ **A** _∥∞ ≤ ϵ with any constant probability, where_ **A**<sup>�</sup> _approximates the attention matrix_ **A** _._ 

4 EXPERIMENTS

---

[referencia=abee5142f9553110 score=0.654]
SM( **x** _,_ **y** ) = E _ω∼N_ (0 _,_ **I** _d_ )�exp� _ω_<sup>_⊤_</sup> **x** _−_<sup>_<u>∥</u>_</sup><sup>**x**</sup> 2<sup>_<u>∥</u>_2</sup> �exp� _ω_<sup>_⊤_</sup> **y** _−_<sup>_<u>∥</u>_</sup><sup>**<u>y</u>**</sup> 2<sup>_<u>∥</u>_2</sup> �� = ΛE _ω∼N_ (0 _,_ **I** _d_ ) cosh( _ω_<sup>_⊤_</sup> **z** ) _,_ (7) _where_ Λ = exp( _−_<sup>_<u>∥</u>_</sup><sup>**x**</sup><sup>_<u>∥</u>_2+</sup> 2<sup>_<u>∥</u>_</sup><sup>**<u>y</u>**</sup><sup>_<u>∥</u>_2</sup> ) _and_ cosh _is hyperbolic cosine. Consequently, softmax-kernel admits a positive random feature map unbiased approximation with h_ ( **x** ) = exp( _−_<sup>_<u>∥</u>_</sup><sup>**x**</sup> 2<sup>_<u>∥</u>_2)</sup><sup>_, l_=1</sup><sup>_, f_1=exp</sup> _and D_ = _N_ (0 _,_ **I** _d_ ) _or: h_ ( **x** ) = _~~√~~_ <u>12</u><sup>exp(</sup><sup>_−_</sup><sup>_<u>∥</u>_</sup><sup>**x**</sup> 2<sup>_<u>∥</u>_2)</sup><sup>_, l_= 2</sup><sup>

---

[referencia=abee5142f9553110 score=0.632]
## 6 BROADER IMPACT 

We believe that the presented algorithm can be impactful in various ways: 

**Biology and Medicine:** Our method has the potential to directly impact research on biological sequence analysis by enabling the Transformer to be applied to much longer sequences without constraints on the structure of the attention matrix. The initial application that we consider is the prediction of interactions between proteins on the proteome scale. Recently published approaches require large evolutionary sequence alignments, a bottleneck for applications to mammalian genomes (Cong et al., 2019). The potentially broad translational impact of applying these approaches to biological sequences was one of the main motivations of this work. We believe that modern bioinformatics can immensely benefit from new machine learning techniques with Transformers being among the most promising. Scaling up these methods to train faster more accurate language models opens the door to the ability to design sets of molecules with pre-specified interaction properties. These approaches could be used to augment existing physics-based design strategies that are of critical importance for example in the development of new nanoparticle vaccines (Marcandalli et al., 2019). 

**Environment:** As we have shown, Performers with FAVOR+ are characterized by much lower compute costs and substantially lower space complexity which can be directly translated to CO2 emission reduction (Strubell et al., 2019) and lower energy consumption (You et al., 2020), as regular Transformers require very large computational resources. 

**Research on Transformers:** We believe that our results can shape research on efficient Transformers architectures, guiding the field towards methods with strong mathematical foundations. Our research may also hopefully extend Transformers also beyond their standard scope (e.g. by considering the Generalized Attention mechanism and connections with kernels). Exploring scalable Transformer architectures that can handle _L_ of the order of magnitude few thousands and more, preserving accuracy of the baseline at the same time, is a gateway to new breakthroughs in bio-informatics, e.g. language modeling for proteins, as we explained in the paper. Our presented method can be potentially a first step. 

**Backward Compatibility:** Our Performer can be used on the top of a regular pre-trained Transformer as opposed to other Transformer variants. Even if up-training is not required, FAVOR+ can still be used for fast inference with no loss of accuracy. We think about this backward compatibility as a very important additional feature of the presented techniques that might be particularly attractive for practitioners.

---

[referencia=abee5142f9553110 score=0.623]
## A HYPERPARAMETERS FOR EXPERIMENTS 

This optimal setting (including comparisons to approximate softmax) we use for the Performer is specified in the Generalized Attention (Subsec. A.4), and **unless specifically mentioned (e.g. using name "Performer-SOFTMAX"), "Performer" refers to using this generalized attention setting.** 

### A.1 METRICS 

We report the following evaluation metrics: 

1. **Accuracy** : For unidirectional models, we measure the accuracy on next-token prediction, averaged across all sequence positions in the dataset. For bidirectional models, we mask each token with 15% probability (same as (Devlin et al., 2018)) and measure accuracy across the masked positions. 

2. **Perplexity** : For unidirectional models, we measure perplexity across all sequence positions in the dataset. For bidirectional models, similar to the accuracy case, we measure perplexity across the masked positions. 

3. **Bits Per Dimension/Character (BPD/BPC)** : This calculated by loss divided by ln(2). 

We used the full evaluation dataset for TrEMBL in the plots in the main section, while for other datasets such as ImageNet64 and PG-19 which have very large evaluation dataset sizes, we used random batches (>2048 samples) for plotting curves.

---

[referencia=abee5142f9553110 score=0.592]
## 3 THEORETICAL RESULTS 

We present here the theory of positive orthogonal random features for softmax-kernel estimation. All these results can be applied also to the Gaussian kernel, since as explained in the previous section, one can be obtained from the other by renormalization (see: Section 2.3). All proofs and additional more general theoretical results with a discussion are given in the Appendix. 

**Lemma 2** (positive (hyperbolic) versus trigonometric random features) **.** _The following is true:_ 



_for independent random samples ωi, and where_ MSE _stands for the mean squared error._ 

trig + Thus, for SM( **x** _,_ **y** ) _→_ 0 we have: MSE(SM<sup>�</sup> _m_<sup>(</sup><sup>**x**</sup><sup>_,_</sup><sup>**y**))</sup><sup>_→∞_and MSE(</sup> SM<sup>�</sup> _m_<sup>(</sup><sup>**x**</sup><sup>_,_</sup><sup>**y**))</sup><sup>_→_0.Further-</sup> more, the hyperbolic estimator provides additional accuracy improvements that are strictly better than those from SM<sup>�</sup> +2 _m_<sup>(</sup><sup>**x**</sup><sup>_,_</sup><sup>**y**) with twice as many random features.The next result shows that the</sup> regularized softmax-kernel is in practice an accurate proxy of the softmax-kernel in attention. 

**Theorem 1** (regularized versus softmax-kernel) **.** _Assume that the L∞-norm of the attention matrix for the softmax-kernel satisfies: ∥_ **A** _∥∞ ≤ C for some constant C ≥_ 1 _. Denote by_ **A**<sup>reg</sup> _the corresponding attention matrix for the regularized softmax-kernel. The following holds:_ 



_Furthermore, the latter holds for d ≥_ 2 _even if the L∞-norm condition is not satisfied, i.e. the regularized softmax-kernel is a universal lower bound for the softmax-kernel._

---

[referencia=abee5142f9553110 score=0.589]
### F.5 PROOF OF THEOREM 4 

We showed in the main body of the paper that in contrast to other methods approximating the attention matrix **A** , our algorithm provides strong concentration guarantees. This is the case also for trigonometric random features, yet, as discussed in the main body of the paper, due to attention renormalization and higher variance of the estimation of small entries of the attention matrix, trigonometric mechanism is sub-optimal. We show here that _m_ opt, the optimal number of random projections for the trigonometric orthogonal mechanism for accurate estimation of the attention matrix does not depend on _L_ but only on _d_ . In fact, we prove that if we take _m_ opt = Θ( _d_ log( _d_ )), then with _O_ ( _Ld_<sup>2</sup> log( _d_ ))-time, we can approximate **A** up to any precision, regardless of the number of tokens _L_ . In order to provide those guarantees, we leverage recent research on the theory of negative dependence for ORFs (Lin et al., 2020). 

We prove the more general version of Theorem 4 from the main body of the paper: 

**Theorem 7** (Uniform convergence for the trigonometric mechanism) **.** _Define entries of the attention matrix_ **A** _as follows:_ **A** _i,j_ = _g_ ( **q**<sup>_⊤_</sup> _i_<sup>)K(</sup> _d_<sup><u>1</u></sup> <u>14</u><sup>**q**</sup> _i_<sup>_⊤,_</sup> _d_ <u>114</u><sup>**k**</sup> _j_<sup>_⊤_)</sup><sup>_h_(</sup><sup>**k**</sup><sup>_⊤_</sup> _j_<sup>)</sup><sup>_for some g, h_: R</sup><sup>_d→_R</sup><sup>_and where_K</sup> 

37 

Published as a conference paper at ICLR 2021