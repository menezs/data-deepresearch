[referencia=267984873f6938ac score=0.982]
## **1 Introduction** 

The attention mechanism [BCB15] was initially developed to better learn long-range sequential knowledge, and found effective use in transformer networks [VSP<sup>+</sup> 17]. Since then, attention-based architectures have permeated across data domains machine learning applications, such as in natural language processing [DCLT18, POT16], speech recognition [LZL<sup>+</sup> 20], and computer vision [RPV<sup>+</sup> 19, BZV<sup>+</sup> 19]. As such, it is vital to develop tools to understand the inner workings of transformers and attention in general, both to shed light on existing models, and to design more effective future models. 

This work provides new insights about the operation and inductive bias of networks built by stacking multiple self-attention layers. Surprisingly, we find that _pure_ self-attention networks (SANs), i.e., transformers with skip connections and multi-layer perceptrons (MLPs) disabled, lose expressive power _doubly exponentially_ with respect to network depth. More specifically, we prove that the output converges with a cubic rate to a rank one matrix that has identical rows. While we derive the convergence bounds in part by using properties of stochastic matrices, our results go beyond what one would expect based on standard results. In particular, by leveraging the cascading effects of specifically stacking self-attention modules, we show exponentially faster convergence than what standard theory prescribes. Furthermore, while previous studies have considered the rank of individial self-attention matrices [WLK<sup>+</sup> 20, KVPF20, CLJ20a], our results are the first to address conditions under which the _entire_ network converges to rank _one_ . 

This raises the question, why do transformers work? Our analysis indicates that skip connections play a key role in mitigating rank collapse, and MLPs can slow down the convergence by increasing their Lipschitz constant. We characterize these counteracting forces by proving upper and lower bounds of this convergence behavior under SAN architectural variants that resemble transformers. Our results reveal a previously unknown vital utility of skip connections, beyond facilitating optimization and gradient flow [HZRS16a, BFL<sup>+</sup> 18]. 

> 1Our code is publicly available at `https://github.com/twistedcubic/attention-rank-collapse` 

1 



<!-- Start of picture text -->

---

[referencia=267984873f6938ac score=0.972]
## **2 Attention doubly exponentially loses rank** 

We start by studying self-attention networks (SANs) built exclusively out of multi-head self-attention layers. We prove that SANs converge exponentially (with depth) to a rank-1 matrix that makes all tokens identical. 

Our analysis in §2.1 relies on an unconventional way to express the output of a multi-head SAN as a sum of single-head networks. We refer to the latter as _paths_ , where each path is denoted by a sequence of attention heads (see Figure 1). A proof sketch of why rank collapse occurs is given in §2.2, whereas the main rank collapse result is presented in §2.3. 

2

---

[referencia=267984873f6938ac score=0.965]
# Attention is not _all_ need: you attention loses rank with pure doubly exponentially depth 

Yihe Dong Jean-Baptiste Cordonnier Andreas Loukas Google EPFL EPFL yihed@google.com jean-baptiste.cordonnier@epfl.ch andreas.loukas@epfl.ch 

#### **Abstract** 

Attention-based architectures have become ubiquitous in machine learning. Yet our understanding of the reasons for their effectiveness remains limited. This work proposes a new way to understand self-attention networks: we show that their output can be decomposed into a sum of smaller terms, each involving the operation of a sequence of attention heads across layers. Using this decomposition, we prove that self-attention possesses a strong inductive bias towards “token uniformity”. Specifically, without skip connections or multi-layer perceptrons (MLPs), the output converges doubly exponentially to a rank-1 matrix. On the other hand, skip connections and MLPs stop the output from degeneration. Our experiments verify the identified convergence phenomena on different variants of standard transformer architectures<sup>1</sup> .

---

[referencia=267984873f6938ac score=0.951]
### **3.2 Multi-layer perceptrons (MLP) help** 

We now study how using an MLP affects the residual. In particular, we focus on SANs with layers written as 



Note that, to keep the notation compact, we use _fl_ to denote both the MLP as well as the output bias. 

In our subsequent analysis, we use _λl,_ 1 _,∞_ to denote the Lipschitz constant of _fl_ with respect to _ℓ_ 1 _,∞_ norm. Note that, though finding the exact constant can be NP-hard even for shallow MLPs [SV18], since _fl_ comprises of linear transformations with Lipschitz nonlinearities, _fl_ is generally Lipschitz. 

**Corollary 3.2** (Simplified) **.** _Consider a depth-L and width-H SAN with MLP. Suppose that ∥_ **_W_** _QK,h_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup> _h_<sup>_l∥_1</sup><sup>_,∞≤_</sup> _β for all h ∈_ [ _H_ ] _and l ∈_ [ _L_ ] _, let γ be a term that depends on the attention entries, and fix λl,_ 1 _,∞ ≤ λ. We have that_ 



_which amounts to a doubly exponential rate of convergence._ 

As seen, though the effect of MLP is less drastic than that of skip connections, the convergence rate in Cor 3.2 can be controlled by the Lipschitz constants _λf,_ 1 _,∞_ of the MLPs: the more powerful the MLPs are the slower the convergence becomes. This reveals a tug-of-war between the self-attention layers and the the MLPs, which due to their nonlinearity can increase the rank. §4 shows that indeed MLPs counteract convergence in experiments. 

We should emphasize that using MLPs to counteract the rank-collapse is not without drawbacks: While increasing the Lipschitz constants slows down residual convergence, it also renders the model less robust and more sensitive to input perturbations [CKSN18]. Larger Lipschitz constants may also pose greater challenges to optimization, as they lead to larger gradient variance.

---

[referencia=267984873f6938ac score=0.933]
## **3 Mechanisms that counteract rank collapse** 

Our findings raise a pertinent question— _why do attention-based networks work in practice if attention degenerates to a rank-1 matrix doubly exponentially with depth?_ Aiming to obtain a deeper understanding, we focus on the transformer architecture [VSP<sup>+</sup> 17] and expand our analysis by incorporating the three important components of transformers that SANs lack: _skip connections_ , _multi-layer perceptrons_ , and _layer normalization_ . 

We adopt a methodical approach where the modifications to the SAN architecture are introduced one at a time. For each case, we re-derive the convergence bounds and discuss the observed effect.

---

[referencia=267984873f6938ac score=0.926]
- Specifically, we train a single-layer transformer to sequentially predict two circular arcs in R<sup>2</sup> of radius 0 _._ 3, starting at ( _−_ 0 _._ 3 _,_ 0) and (0 _._ 3 _,_ 0), respectively, each directed counter-clockwise and consisting of 1000 points 

- (illustrated as gray trajectories). An input sample consists of a sequence of two opposing points on the circle, one from the top arc and the other from the bottom arc. We apply teacher-forcing at each step, meaning we give the network the ground truth coordinates of the two current points, and train it to predict the next 

two points. The model attempts to minimize the MSE loss between the predicted points and the ground 

- truth points on the trajectories. At inference time, we don’t apply teacher-forcing, and simply feed the model output as input for the next step. 

9 

Since this recurrent application of a single-layer transformer can be reparametrized to be equivalent to a multi-layer transformer without skip connections, _we hypothesize that at inference time the predicted trajectories of the two arcs will converge to the same point (indicating a rank collapse)_ , rather than following the training trajectories. Note that the setting has also been intentionally constructed to enable training even without skip connections (by using teacher forcing) and thus to disentangle the two distinct benefits of skip connections: their ability to improve optimization and their mitigation of rank collapse. 

We trained the network until it could perfectly memorize the next step on the circular trajectories with near-zero loss. Figure 3 demonstrates the trajectories predicted at inference time (i.e., without teacher forcing). As seen on the top row, without MLP or skip connections the network exhibits rank collapse. Theorem 2.2 predicts that the convergence is slower when _β ≥∥_ **_W_** _QK_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _V_<sup>_∥_1</sup><sup>_,∞_increases.Indeed,asthe</sup> hidden dimension increases from 32 to 128 (leading to larger _β_ at initialization), the convergence slows down, becoming hardly observable for dimension 128.

---

[referencia=267984873f6938ac score=0.924]
> 1Our code is publicly available at `https://github.com/twistedcubic/attention-rank-collapse` 

1 



<!-- Start of picture text -->
Layer 1 Layer 2 Layer  L<br>Skip connection Skip connection Skip connection<br>concat and project concat and project concat and project<br><!-- End of picture text -->

**Figure 1:** Two paths in a deep Self-Attention Network (SAN) with _H_ heads and _L_ layers. At each layer, a path can go through one of the heads or bypass the layer. Adding an MLP block after each attention layer forms the transformer architecture. 

In the process, we develop a new _path decomposition_ to study self-attention networks. Namely, we decompose a SAN into a linear combination of weakly-interdependent _paths_ , where each ‘path’ corresponds to a deep single-head SAN. Intuitively, one can view the self-attention heads in each layer of the original network as different gateways, and a path follows a sequence of gateway choices, one gateway per layer (Figure 1). Coupled with the rank collapse analysis, our results suggest that deep SANs with skip connections behave like an ensemble of weakly-dependent shallow networks. 

Our main contributions are as follows: (1) We present a systematic study of building blocks of the transformer, revealing opposing impacts between self-attention and the counteracting forces: skip connections and MLP, in contributing and preventing a _rank collapse_ in transformers. As a corollary, this reveals a previously unknown vital effect of skip connections beyond facilitating optimization. (2) We propose a new method for analyzing SANs via a _path decomposition_ , revealing SANs as an ensemble of shallow networks. (3) We verify our theory with experiments on common transformer architectures.

---

[referencia=267984873f6938ac score=0.912]
- dimension 32 

- 0.5 0.0 

- -0.5 0.5 0.0 

- -0.5 0.5 0.0 

- -0.5 -0.5 0.0 0.5 -0.5 

- dimension 86 dimension 128 





   - 0.0 0.5 -0.5 0.0 0.5 

- **Figure 3:** Applying a trained single-layer transformer module recurrently, to models of increasing hidden dimension (horizontal direction) and across architectural variants (vertical direction). The two light background paths illustrate the two training trajectories, for which the starting points are ( _−_ 0 _._ 3 _,_ 0) and (0 _._ 3 _,_ 0). Each figure contains the same number of steps. Consistent with the theory in §3, convergence slows down or stops as the dimension increases (since _β ≥∥_ **_W_** _QK_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup> _V_<sup>_l∥_1</sup><sup>_,∞_isgenerallylarger),aswellaswheneitherMLPorskipconnectionsareadded.</sup> 

- To compute these ratios we ran the network on 32 samples of 128 tokens excerpts of biographies from Wikipedia [LGA16] and display the mean and standard deviation. 

- The experiments confirm that, as soon as the skip connections are removed, all networks exhibit a rapid rank collapse. Though MLPs do not seem to help in the mitigation of convergence, we caution that the observation is not an accurate portrayal of how trained transformers behave: removing the skip connections introduces a drastic distribution shift in the MLP input. We expect that the convergence will slow down if the network is retrained. 

- **4.2 Visualizing the bias of different architectures** 

- To empirically investigate the inductive bias of the different components of the transformer architecture, we study the behavior of a single-layer transformer when applied _recurrently_ (akin to the universal transformer [DGV<sup>+</sup> 19]) to predict a simple 2D circular sequence.

---

[referencia=267984873f6938ac score=0.871]
<br>∥ )( SAN X l 1 ∞, ∥ )( SAN X l 1 ∞, ∥ )( SAN X l 1 ∞,<br> ∥  ∥  ∥<br>/ / /<br>∥ 1 ∞, ∥ 1 ∞, ∥ 1 ∞,<br>)) )) ))<br>(( SAN X resl (( SAN X resl (( SAN X resl<br>∥ ∥ ∥<br><!-- End of picture text -->

**Figure 2:** Relative norm of the residual along the depth for three models before and after training. Pure attention (SAN) converges rapidly to a rank-1 matrix. Adding MLP blocks and skip connection gives a transformer. Skip connections play a critical role in mitigating rank collapse (i.e., a zero residual). 

By setting **_W_**<sup>˜</sup> _h_ = **_W_** _h_ **_D_** _LN_<sup>_−_1and</sup><sup>**_b_**˜</sup><sup>_O_=</sup><sup>**_b_**</sup><sup>_O −_</sup><sup>**_b_**</sup><sup>_LN_,theaboveisre-writtenas</sup> 



which is identical to the equation before layer normalization was applied, though now **_W_** ˜ _h_ and **_b_**<sup>˜</sup> _O_ are input dependent. Since right multiplication cannot increase the rank of a matrix, we conclude that layer normalization does not mitigate the rank collapse.

---

[referencia=267984873f6938ac score=0.851]
We conclude that, in accordance to our analysis, adding MLP or skip connections either stops or drastically slows down rank collapse. As observed, skip connections tend to slow down points from moving. The latter phenomenon is because in this setting skip connections introduce a bias towards remaining in the same position. On the other hand, adding MLPs does not exhibit the same bias.

---

[referencia=267984873f6938ac score=0.769]
### **3.1 Skip connections are crucial** 

A simple modification to the path decomposition argument for SAN suffices to take into account skip connections. Specifically, we indicate the event that a path has skipped a layer by setting _h_ = 0 on the corresponding notation: 



where we have fixed **_P_** 0 = **_I_** and **_W_** 0 = **_I_** . 

As observed, skip connections dramatically diversify the path distribution. Denote by _Pl_ the set of paths of length _l_ . With skip connections enabled, we have 



paths of length _l_ (whereas before we had only length _L_ paths). We hypothesize that it is the presence of short paths that stops SAN from degenerating to rank-1. 

While we can derive an upper bound for the residual similar to above (which we do in the Appendix for completeness) such an upper bound is vacuously large. Indeed, it is more informative to have a _lower_ bound on the residual, to align with practice, where SANs with skip connections do not suffer rank collapse. We present the following simple lower bound: 

**Claim 3.1.** _Consider a depth-L and width-H self-attention network with skip connections. There exist infinitely many parameterizations for which ∥res_ ( **_X_**<sup>_L_</sup> ) _∥≥∥res_ ( **_X_** ) _∥. The preceeding holds even for L →∞ and β arbitrarily small._

---

[referencia=267984873f6938ac score=0.767]
## **5 Related works** 

Skip connections were first introduced in ResNets [HZRS16a], ever since, it has been used to facilitate optimization in deep networks [HZRS16b, VWB16b, BFL<sup>+</sup> 18]. In particular, skip connections tackle the vanishing gradient problem, by allowing the gradient to flow bypass the skipped layers during backpropagation. The original motivation of using skip connections in transformers follow the same reasoning on facilitating optimization [VSP<sup>+</sup> 17]. With the paths decomposition for transformers, we discover an additional surprising importance of skip connections: they prevent the transformer output from degenerating to rank one exponentially quickly with respect to network depth. 

Veit et al. ([VWB16b]) introduced an analogous interpretation for residual networks as a collection of paths of varying lengths, and found that the length of the effective paths in deep residual networks are much shorter than the total network depth, due to the gradients used for parameter updates coming overwhelmingly from these short paths. Our finding suggests that SANs rely on short paths to avoid rank collapse. On the other hand, Daneshmand et al. [DKB<sup>+</sup> 20] studied rank collapse in randomly initialized linear and ReLU networks and showed that batch normalization is an effective mitigation strategy. 

Some recent works have approximated the attention matrix with low-rank factorizations [WLK<sup>+</sup> 20, TBM<sup>+</sup> 20] or kernel methods [KVPF20, CLD<sup>+</sup> 20], to reduce the quadratic self-attention complexity. Our work is orthogonal to these works, by studying the rank of the network’s output (rather than of the attention matrix). 

There have been other recent advances in understanding the theory behind transformers: [PMB19, DGV<sup>+</sup> 19] proved Turing universality, [CLJ20b] provided necessary and sufficient conditions for attention to simulate convolution. A linearized form of self-attention was also found to exhibit a depth phase transition [LWS<sup>+</sup> 20]; and the Lipschitz constant of self-attention was analyzed by [KPM20].

---

[referencia=267984873f6938ac score=0.766]
### **2.3 Exponential convergence for attention networks** 

We now move on to analyse the convergence of SANs with _multiple_ heads per layer. 

Our main result is as follows: 

**Theorem 2.3** (Simplified) **.** _Consider a depth-L and width-H self-attention network without skip connections. Suppose that ∥_ **_W_** _QK,h_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _h_<sup>_∥_1</sup><sup>_,∞≤βforallheadsh∈_[</sup><sup>_H_]</sup><sup>_andlayersl∈_[</sup><sup>_L_]</sup><sup>_,andletγbeatermthat_</sup> _depends on the attention entries. We have_ 



_which amounts to a doubly exponential rate of convergence._ 

The bound guarantees convergence of SAN( **_X_** ) to rank one when 4 _γβH <_ � _dqk_ . Our experiments show that this is a rather pessimistic estimate, as, in practice, we observe widespread convergence of output to rank-1. 

**Remark 1. Implications for Xformers.** There has been a surge of architectural variants – that we collectively refer to as Xformers – aimed to improve the vanilla transformer [VSP<sup>+</sup> 17] by reducing the quadratic self-attention complexity. The rank collapse result of Theorem 2.3 carries interesting implications for these architectures. One such variant relies on low-rank or kernel-based approximations to the full attention matrix [KVPF20, WLK<sup>+</sup> 20, CLD<sup>+</sup> 20], in which case the paths likely converge even faster to rank one due to the imposed low-rankedness. Another variant only computes a subset of the attention matrix entries using particular patterns [ZGD<sup>+</sup> 20, CGRS19], such as random patterns, in which case one expects the paths to converge more slowly, as randomization tends to increase the rank of the output. 

5

---

[referencia=267984873f6938ac score=0.718]
## **A Deferred Proofs** 

We build our argument step by step, by first considering a single-head self-attention layer in §A.1 and then moving to deeper networks with single and multiple heads in §A.3 and §A.4. The results are extended to take into account skip connections and MLPs in §A.5 and §A.6

---

[referencia=267984873f6938ac score=0.667]
### **2.2 Convergence of single-head SAN** 

Before tackling the full SAN, it is instructive to consider the behavior of each path separately. We examine, in particular, how the residual 

res( **_X_** ) = **_X_** _−_ **1** **_x_**<sup>_⊤_</sup> _,_ where **_x_** = argmin **_x_** _∥_ **_X_** _−_ **1** **_x_**<sup>_⊤_</sup> _∥_ 

changes during the forward pass. 

As the following result shows, the residual norm converges to zero surprisingly quickly (doubly exponentially with a cubic rate): 

**Theorem 2.2** (Simplified) **.** _For any single-head SAN consisting of L layers with ∥_ **_W_** _QK_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _V_<sup>_∥_1</sup><sup>_,∞≤β_</sup> _and for a term γ that depends on the attention entries, we have that_ 



_which amounts to a doubly exponential convergence to a rank-1 matrix._ 

For the full theorem, we refer the reader to the Appendix. 

Note that the bound in Eq 2 guarantees _∥_ res(SAN( **_X_** )) _∥_ 1 _,∞_ convergence for all inputs of small residual whenever 4 _γβ <_ � _dqk_ . In practice, our experiments imply that the region for convergence can be much greater. 

The identified cubic rate of convergence is significantly faster than what would be expected when analyzing products of stochastic matrices (linear rate). As a rule of thumb, to achieve a decline of three orders of magnitude, say from 1000 to 1, one could expect a linear rate of convergence to require roughly a dozen iterations, whereas a cubic rate can do so in just two or three iterations. The reason why we get a cubic rate is that the rank of attention matrices depends also on the rank of the input. As we show, the self-attention 

4

---

[referencia=267984873f6938ac score=0.663]
### **A.3 Single-head and multiple-layers** 

We next consider how the residual changes after _L_ layers of the form: **_X_**<sup>_l_</sup> = SA<sup>_l_</sup> 1<sup>(</sup><sup>**_X_**</sup><sup>_l−_1)</sup><sup>_._</sup> 

**Corollary 2.2.** _In the setting of Lemma A.1, for any single-head SAN consisting of L layers with ∥_ **_W_** _QK,_<sup>_l_</sup> 1<sup>_∥_1</sup><sup>_≤_</sup> _β for every l ∈_ [ _L_ ] _, the residual is bounded by_ 



_which amounts to a doubly exponential convergence to a rank-1 matrix._ 

_Proof._ Unfolding the recursion backwards from the last layer to the first and applying Lemma A.1 we obtain: 





matching the theorem statement. 

18 

### **A.4 Multiple-head and multiple-layers** 

**Corollary 2.3** (mutli-head multi-layer) **.** _In the setting of Lemma A.1, consider a depth-L SAN with H heads per layer. Fix ∥_ **_W_** _QK,h_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _h_<sup>_∥_1</sup><sup>_,∞≤βforallh ∈_[</sup><sup>_H_]</sup><sup>_andl ∈_[</sup><sup>_L_]</sup><sup>_.Theoutputresidualisboundedby_</sup> 



_which indicates that the output convergences to a rank-1 matrix doubly exponentialy._ 

_Proof._ The proof procceeds recursively as for Theorem 2.2 in the single head case but using the bound on single-layer multi-heads residuals from Lemma A.2.

---

[referencia=267984873f6938ac score=0.657]
Perhaps the convergence to rank one of a path should come as no surprise: each path component contains row-stochastic matrices as a result of the softmax attention, and [AT77] showed the exponential convergence of products of stochastic matrices to rank one. While the intuition behind stochastic matrices driving convergence still applies, in deep attention networks these matrices interact in more complex ways than what classical analyses consider. As we show, because of these interactions the rank collapses much faster than what would be expected based on classical analyses (cubic vs linear rate). 

## **6 Conclusion** 

This work exposes competing forces over rank collapse in self-attention networks, namely self-attention vs skip connections and MLPs. In the process, we develop a path decomposition for SANs, which modularizes the study of self-attention and is of independent interest to additional applications. These results open the door for many exciting future directions. For instance, how can one leverage the token-uniformity inductive bias revealed to design more effective networks, perhaps better at utilizing long paths? What are some practical implications for width-depth trade-off? How do we prove meaningful lower bounds of residue convergence for transformers? Answering these questions has broad implications in advancing the state of the art in deep learning. 

**Acknowledgements.** Andreas Loukas would like to thank the Swiss National Science Foundation for supporting him in the context of the project “Deep Learning for Graph-Structured Data” (grant number PZ00P2 179981). Jean-Baptiste Cordonnier is supported by the Swiss Data Science Center (SDSC). 

12

---

[referencia=267984873f6938ac score=0.509]
### **A.5 SAN with skip connections** 

As noted in the main text, a lower bound on the residual better aligns with practice, where SANs with skip connections do not suffer rank collapse. For consistency with the other analyses and as one way to illustrate residual growth, we provide a (vacuously large) upper bound on the residual for SANs with skip connections. 

**Corollary 3.1** (SAN with skip connections) **.** _In the setting of Lemma A.1, consider a depth-L SAN with H heads per layer and skip connections. Fix ∥_ **_W_** _QK,h_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _h_<sup>_∥_1</sup><sup>_,∞≤βforallheadsh ∈_[</sup><sup>_H_]</sup><sup>_andlayersl ∈_[</sup><sup>_L_]</sup><sup>_._</sup> _The output residual is bounded by_ 



_which does not indicate convergence._ 

_Proof._ For a SAN with skip connections, the residual bound for a single-head single-layer SAN from lemma A.1 now becomes: 



To obtain a multi-layer bound, we unfold the recursion backwards. 

Let us consider a single head model first and fix _∥_ **_W_** _QK,h_<sup>_l∥_1</sup><sup>_∥_</sup><sup>**_W_**</sup><sup>_l_</sup> _h_<sup>_∥_1</sup><sup>_,∞≤β_forall</sup><sup>_l ∈_[</sup><sup>_L_].Wehavethat:</sup>

---

[referencia=267984873f6938ac score=0.492]
Excluding biases **1** **_b_**<sup>_⊤_</sup> _O,h_<sup>,theSANoutputisgivenby</sup> 



which, after unrolling the recursion backwards, yields: 

The above equations have a clear interpretation if we think of the SAN as a directed acyclic graph, with nodes corresponding to self-attention heads and directed edge connecting heads of consecutive layers. 

We formalize this intuition in the following: 

**Theorem 2.1** (Path decomposition of SAN) **.** _The output of a depth L self-attention network with H heads per layer (including biases and skip connections) is given by_ 



_where_ **_P_** _path_ = **_P_** _h_<sup>_L_</sup> _L_<sup>_· · ·_</sup><sup>**_P_**1</sup> _h_ 1<sup>_isaninput-dependentstochasticmatrix,whereas_</sup><sup>**_W_**</sup><sup>_path_=</sup><sup>**_W_**1</sup> _h_ 1<sup>_· · ·_</sup><sup>**_W_**</sup><sup>_L_</sup> _hL_<sup>_and_</sup><sup>**_b_**</sup><sup>_do_</sup> _not depend on the input._ 

3 

_Proof._ The proof follows from the fact that the set of row-stochastic matrices is closed under multiplication (i.e., **_P_** _h_<sup>_L_</sup> _L_<sup>_· · ·_</sup><sup>**_P_**</sup><sup>_i_</sup> _hi_<sup>isrow-stochastic)and,moreover,foranyrow-stochasticmatrix</sup><sup>**_P_**,wehave</sup><sup>**_P_1**=</sup><sup>**1**.</sup> 

Each term in (1) describes a path of length _L_ across heads of different layers 



and there are a total of _H_<sup>_L_</sup> such paths without skip connections.

---

[referencia=267984873f6938ac score=0.488]
Each term in (1) describes a path of length _L_ across heads of different layers 



and there are a total of _H_<sup>_L_</sup> such paths without skip connections. 

The path decomposition thus describes the action of a multi-head SAN as the combination of simpler single-head networks. To gain intuition on path interdependence, it helps to split the operations performed into two types: those that act across tokens (multiplication from left) and those that apply independently on each token (multiplication from right). As seen, though paths can interact through token mixing (since _Ppath_ matrices jointly depend on _X_ ), token-wise operations are independent. We can also notice that biases are not particularly meaningful: their total contribution amounts to the single term **1** **_b_**<sup>_⊤_</sup> independently of the number of layers or heads used. 

In the following we show that each path converges rapidly (as a function of length) to a rank-1 matrix with identical rows. Interestingly, this convergence is so dominant that adding more layers to the SAN does not help: though the number of paths is increased exponentially, each path degenerates doubly exponentially, leading also to a rank-1 output.