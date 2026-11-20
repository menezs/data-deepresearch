[referencia=319a638394e5883b score=0.997]
# **On the difficulty of training Recurrent Neural Networks** 

### **Razvan Pascanu** 

pascanur@iro.umontreal.ca 

Universite de Montreal 

### **Tomas Mikolov** 

t.mikolov@gmail.com 

Brno University 

### **Yoshua Bengio** 

yoshua.bengio@umontreal.ca 

Universite de Montreal 

## **Abstract** 

There are two widely known issues with properly training Recurrent Neural Networks, the _vanishing_ and the _exploding_ gradient problems detailed in Bengio _et al._ (1994). In this paper we attempt to improve the understanding of the underlying issues by exploring these problems from an analytical, a geometric and a dynamical systems perspective. Our analysis is used to justify a simple yet effective solution. We propose a gradient norm clipping strategy to deal with exploding gradients and a soft constraint for the vanishing gradients problem. We validate empirically our hypothesis and proposed solutions in the experimental section.

---

[referencia=319a638394e5883b score=0.979]
## **1. Introduction** 

A recurrent neural network (RNN), e.g. Fig. 1, is a neural network model proposed in the 80’s (Rumelhart _et al._ , 1986; Elman, 1990; Werbos, 1988) for modeling time series. The structure of the network is similar to that of a standard multilayer perceptron, with the distinction that we allow connections among hidden units associated with a time delay. Through these connections the model can retain information about the past inputs, enabling it to discover temporal correlations between events that are possibly far away from each other in the data (a crucial property for proper learning of time series). 

While in principle the recurrent network is a simple and powerful model, in practice, it is unfortunately hard to train properly. Among the main reasons why this model is so unwieldy are the _vanishing gradient_ 



_Figure 1._ Schematic of a recurrent neural network. The recurrent connections in the hidden layer allow information to persist from one input to another. 

and _exploding gradient_ problems described in Bengio _et al._ (1994).

---

[referencia=319a638394e5883b score=0.974]
## **2. Exploding and Vanishing Gradients** 

As introduced in Bengio _et al._ (1994), the _exploding gradients_ problem refers to the large increase in the norm of the gradient during training. Such events are caused by the explosion of the long term components, which can grow exponentially more then short term ones. The _vanishing gradients_ problem refers to the opposite behaviour, when long term components go exponentially fast to norm 0, making it impossible for the model to learn correlation between temporally distant events.

---

[referencia=319a638394e5883b score=0.949]
## **3. Dealing with the exploding and vanishing gradient**

---

[referencia=319a638394e5883b score=0.943]
### 4.1.1. The Temporal Order problem 

We consider the temporal order problem as the prototypical pathological problem, extending our results to the other proposed tasks afterwards. The input is a long stream of discrete symbols. At two points in time (in the beginning and middle of the sequence) a symbol within _{A, B}_ is emitted. The task consists in classifying the order (either _AA, AB, BA, BB_ ) at the end of the sequence. 

Fig. 7 shows the success rate of standard SGD, SGD-C (SGD enhanced with out clipping strategy) and SGDCR (SGD with the clipping strategy and the regularization term). Note that for sequences longer than 20, the vanishing gradients problem ensures that neither SGD nor SGD-C algorithms can solve the task. The _x_ -axis is on log scale. 

This task provides empirical evidence that exploding gradients are linked with tasks that require long memory traces. We know that initially the model operates in the one-attractor regime (i.e. _λ_ 1 _<_ 1), in which the amount of memory is controlled by _λ_ 1. More memory means larger spectral radius, and, when this value crosses a certain threshold the model enters rich regimes where gradients are likely to explode. We see in Fig. 7 that as long as the vanishing gradient prob- 

**On the difficulty of training Recurrent Neural Networks** 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>SGD-C<br>SGD<br>0.0<br>SGD-CR<br>2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5<br>Log of sequence length<br>Rate of success<br><!-- End of picture text -->

_Figure 7._ Rate of success for solving the temporal order problem versus log of sequence length. See text. 

lem does not become an issue, addressing the exploding gradients problem ensures a better success rate.

---

[referencia=319a638394e5883b score=0.919]
In Hochreiter and Schmidhuber (1997); Graves _et al._ (2009) a solution is proposed for the vanishing gradients problem, where the structure of the model is changed. Specifically it introduces a special set of units called LSTM units which are linear and have a recurrent connection to itself which is fixed to 1. The flow of information into the unit and from the unit is guarded by an input and output gates (their behaviour is learned). There are several variations of this basic structure. This solution does not address explicitly the exploding gradients problem. 

Sutskever _et al._ (2011) use the Hessian-Free optimizer in conjunction with _structural damping_ , a specific damping strategy of the Hessian. This approach seems to deal very well with the vanishing gradient, though more detailed analysis is still missing. Presumably this method works because in high dimensional spaces there is a high probability for long term components to be orthogonal to short term ones. This would allow the Hessian to rescale these components independently. In practice, one can not guarantee that this property holds. As discussed in section 2.3, this method is able to deal with the exploding gradient as well. Structural damping is an enhancement that forces the change in the state to be small, when the parameter changes by some small value ∆ _θ_ . This asks for the Jacobian matrices<sup>_<u>∂</u>_</sup> _∂θ_<sup>**<u>x</u>**</sup><sup>_<u>t</u>_tohavesmallnorm,hence</sup> further helping with the exploding gradients problem. The fact that it helps when training recurrent neural models on long sequences suggests that while the curvature might explode at the same time with the gradient, it might not grow at the same rate and hence not be sufficient to deal with the exploding gradient.

---

[referencia=319a638394e5883b score=0.906]
The x-axis covers the parameter _b_ and the y-axis the asymptotic state **x** _∞_ . The bold line follows the movement of the final point attractor, **x** _∞_ , as _b_ changes. At _b_ 1 we have a bifurcation boundary where a new attractor emerges (when _b_ decreases from _∞_ ), while at _b_ 2 we have another that results in the disappearance of one of the two attractors. In the interval ( _b_ 1 _, b_ 2) we are in a rich regime, where there are two attractors and the change in position of boundary between them, as we change _b_ , is traced out by a dashed line. The vector field (gray dashed arrows) describe the evolution of the state **x** if the network is initialized in that region. 



_Figure 3._ Bifurcation diagram of a single hidden unit RNN (with fixed recurrent weight of 5.0 and adjustable bias _b_ ; example introduced in Doya (1993)). See text. 

We show that there are two types of events that could lead to a large change in **x** _t_ , with _t →∞_ . One is crossing a boundary between basins of attraction (depicted with a unfilled circles), while the other is crossing a bifurcation boundary (filled circles). For large _t_ , the ∆ _xt_ resulting from a change in _b_ will be large even for very small changes in _b_ (as the system is attracted towards different attractors) which leads to a large gradient. 

It is however _neither necessary nor sufficient_ to cross a bifurcation for the gradients to explode, as bifurcations are global events that could have no effect locally. Learning traces out a path in the parameterstate space. If we are at a bifurcation boundary, but the state of the model is such that it is in the basin of attraction of one attractor (from many possible attractors) that does not change shape or disappear when the bifurcation is crossed, then this bifurcation will not affect learning. 

**On the difficulty of training Recurrent Neural Networks**

---

[referencia=319a638394e5883b score=0.904]
We first **prove** that it is _sufficient_ for _λ_ 1 _< γ_<sup><u>1</u>,where</sup> _λ_ 1 is the absolute value of the largest eigenvalue of the recurrent weight matrix **W** _rec_ , for the _vanishing gradient_ problem to occur. Note that we assume the parametrization given by equation (11). The Jacobian matrix _∂∂_ **xx** _k_ <u>+</u> _k_ 1 is given by **W** _rec_<sup>_Tdiag_(</sup><sup>_σ′_(</sup><sup>**x**</sup><sup>_k_)).The2-</sup> norm of this Jacobian is bounded by the product of 

**On the difficulty of training Recurrent Neural Networks** 

the norms of the two matrices (see equation (6)). Due to our assumption, this implies that it is smaller than 1. 



Let _η ∈_ R be such that _∀k,_ ��� _∂∂_ **xx** _k_ <u>+</u> _k_ 1 ��� _≤ η <_ 1. The existence of _η_ is given by equation (6). By induction over _i_ , we can show that 



As _η <_ 1, it follows that, according to equation (7), long term contributions (for which _t − k_ is large) go to 0 exponentially fast with _t − k_ . □ 

By inverting this proof we get the _necessary_ condition for _exploding gradients_ , namely that the largest eigenvalue _λ_ 1 is larger than _γ_<sup><u>1</u>(otherwise the long term com-</sup> ponents would vanish instead of exploding). For tanh we have _γ_ = 1 while for sigmoid we have _γ_ =<sup>1</sup> _/_ 4.

---

[referencia=319a638394e5883b score=0.888]
### **4.2. Natural problems** 

We address the task of polyphonic music prediction, using the datasets Piano-midi.de, Nottingham and MuseData described in Boulanger-Lewandowski _et al._ (2012) and language modelling at the character level on the Penn Treebank dataset (Mikolov _et al._ , 2012). We also explore a modified version of the task, where we ask the model to predict the 5th character in the future (instead of the next). Our assumption is that to solve this modified task long term correlations are more important than short term ones, and hence our regularization term should be more helpful. 

The training and test scores reported in Table 1 are average negative log likelihood per time step. We fixed hyper-parameters across the three runs, except for the regularization factor and clipping cutoff threshold. **SGD-CR provides a statistically significant improvement on the state-of-the-art for RNNs on all the polyphonic music prediction tasks** _except_ for MuseData on which we get exactly the same performance as the state-of-the-art (Bengio _et al._ , 2012), which uses a different architecture. Table 2 contains the results on language modelling (in bits per letter). 

These results suggest that clipping the gradients solves an optimization issue and does not act as a regularizer, as both the training and test error improve in general. Results on Penn Treebank reach the state of the art achieved by Mikolov _et al._ (2012), who used a different clipping algorithm similar to ours, thus providing evidence that both behave similarly. The regularized model performs as well as the Hessian-Free trained model. 

By employing the proposed regularization term we are able to improve test error even on tasks that are not 

**On the difficulty of training Recurrent Neural Networks** 

dominated by long term contributions.

---

[referencia=319a638394e5883b score=0.877]
a deep multi-layer one (with an unbounded number of layers) and backpropagation is applied on the unrolled model (see Fig. 2). 



<!-- Start of picture text -->
Et− 1 Et Et +1<br>∂Et− 1 ∂Et ∂Et +1<br>∂ x t− 1 ∂ x t ∂ x t +1<br>x t− 1 x t x t +1<br>∂ x t− 1 ∂ x t ∂ x t +1 ∂ x t +2<br>∂ x t− 2 ∂ x t− 1 ∂ x t ∂ x t +1<br>ut− 1 ut ut +1<br><!-- End of picture text -->

_Figure 2._ Unrolling recurrent neural networks in time by creating a copy of the model for each time step. We denote by **x** _t_ the hidden state of the network at time _t_ , by **u** _t_ the input of the network at time _t_ and by _Et_ the error obtained from the output at time _t_ . 

We will diverge from the classical BPTT equations at this point and re-write the gradients (see equations (3), (4) and (5)) in order to better highlight the exploding gradients problem. These equations were obtained by writing the gradients in a sum-of-products form.

---

[referencia=319a638394e5883b score=0.876]
**On the difficulty of training Recurrent Neural Networks** 



_Figure 6._ We plot the error surface of a single hidden unit recurrent network, highlighting the existence of high curvature walls. The solid lines depicts standard trajectories that gradient descent might follow. Using dashed arrow the diagram shows what would happen if the gradients is 

_explode so does the curvature along_ **v** _, leading to a wall in the error surface_ , like the one seen in Fig. 6. 

If this holds, then it gives us a simple solution to the exploding gradients problem depicted in Fig. 6. 

If both the gradient and the leading eigenvector of the curvature are aligned with the exploding direction **v** , it follows that the error surface has a steep wall perpendicular to **v** (and consequently to the gradient). This means that when stochastic gradient descent (SGD) reaches the wall and does a gradient descent step, it will be forced to jump across the valley moving perpendicular to the steep walls, possibly leaving the valley and disrupting the learning process. 

The dashed arrows in Fig. 6 correspond to _ignoring the norm of this large step_ , ensuring that the model stays close to the wall. The key insight is that all the steps taken when the gradient explodes are aligned with **v** and ignore other descent direction (i.e. the model moves perpendicular to the wall). At the wall, a small-norm step in the direction of the gradient therefore merely pushes us back inside the smoother lowcurvature region besides the wall, whereas a regular gradient step would bring us very far, thus slowing or preventing further training. Instead, with a bounded step, we get back in that smooth region near the wall where SGD is free to explore other descent directions. 

The important addition in this scenario to the classical high curvature valley, is that we assume that the valley is wide, as we have a large region around the wall where if we land we can rely on first order methods to move towards the local minima. This is why just clipping the gradient might be sufficient, not requiring the use a second order method. Note that this algo- 

rithm should work even when the rate of growth of the gradient is not the same as the one of the curvature (a case for which a second order method would fail as the ratio between the gradient and curvature could still explode).

---

[referencia=319a638394e5883b score=0.839]
## **Analytical analysis of the exploding and vanishing gradients problem** 



Let us consider the term **g** _k_<sup>_T_=</sup> _∂∂_ **x** _<u>Ett</u> ∂∂_ **xx** _kt_ _<u>∂</u>_<sup>+</sup> _∂θ_ **<u>x</u>** _<u>k</u>_ for the linear version of the parametrization in equation (11) (i.e. set _σ_ to the identity function) and assume _t_ goes to infinity and _l_ = _t − k_ . We have that: 



By employing a generic _power iteration method_ based proof we can show that, given certain conditions, _∂∂_ **x** _<u>Ett</u>_ � **W** _rec_<sup>_T_</sup> � _l_ grows exponentially. 

**Proof** Let **W** _rec_ have the eigenvalues _λ_ 1 _, .., λn_ with _|λ_ 1 _| > |λ_ 2 _| > .. > |λn|_ and the corresponding eigenvectors **q** 1 _,_ **q** 2 _, ..,_ **q** _n_ which form a vector basis. We can now write the row vector<sup>_<u>∂Et</u>_thisbasis:</sup> _∂_ **x** _t_<sup>into</sup> 



If _j_ is such that _cj_ = 0 and any _j_<sup>_′_</sup> _< j, cj′_ = 0, using the fact that **q**<sup>_T_</sup> _i_ � **W** _rec_<sup>_T_</sup> � _l_ = _λli_<sup>**q**</sup><sup>_T_</sup> _i_<sup>wehavethat</sup>

---

[referencia=a37966686d387941 score=0.836]
# Learning long-term dependencies with gradient descent is difficult

Authors:

- P. SimardPSP. Simard
- P. FrasconiPFP. Frasconi

- 1 March 1994
- journal article
- Published by Institute of Electrical and Electronics Engineers (IEEE) in IEEE Transactions on Neural Networks
- Vol. 5 (2) , 157-166

##### Abstract

Recurrent neural networks can be used to map input sequences to output sequences, such as for recognition, production or prediction problems. However, practical difficulties have been reported in training recurrent neural networks to perform tasks in which the temporal contingencies present in the input/output sequences span long intervals. We show why gradient based learning algorithms face an increasingly difficult problem as the duration of the dependencies to be captured increases. These results expose a trade-off between efficient learning by gradient descent and latching on information for long periods. Based on an understanding of this problem, alternatives to standard gradient descent are considered.<>
##### Keywords

This publication has 9 references indexed in Scilit:

- Global optimization of a neural network-hidden Markov model hybridIEEE Transactions on Neural Networks, 1992
- Using random weights to train multilayer networks of hard-limiting unitsIEEE Transactions on Neural Networks, 1992
- Local Feedback Multilayered NetworksNeural Computation, 1992
- Nonlinear dynamics and stability of analog neural networksPhysica D: Nonlinear Phenomena, 1991
- A Learning Algorithm for Continually Running Fully Recurrent Neural NetworksNeural Computation, 1989
- BPS: a learning algorithm for capturing the dynamic nature of speech1989
- Minimizing multimodal functions of continuous variables with the “simulated annealing” algorithm—Corrigenda for this article is available hereACM Transactions on Mathematical Software, 1987
- Learning Process in an Asymmetric Threshold Network1986
- Optimization by Simulated AnnealingScience, 1983

---

[referencia=319a638394e5883b score=0.832]
### **2.2. Drawing similarities with Dynamical Systems** 

We can improve our understanding of the exploding gradients and vanishing gradients problems by employing a dynamical systems perspective, as it was done before in Doya (1993); Bengio _et al._ (1993). 

We recommend reading Strogatz (1994) for a formal and detailed treatment of dynamical systems theory. For any parameter assignment _θ_ , depending on the initial state **x** 0, the state **x** _t_ of an autonomous dynamical system converges, under the repeated application of the map _F_ , to one of several possible different attractor states (e.g. point attractors, though other type of attractors exist). The model could also find itself in a chaotic regime, case in which some of the following observations may not hold, but that is not treated in depth here. Attractors describe the asymptotic behaviour of the model. The state space is divided into basins of attraction, one for each attractor. If the model is started in one basin of attraction, the model will converge to the corresponding attractor as _t_ grows. 

Dynamical systems theory tells us that as _θ_ changes slowly, the asymptotic behaviour changes smoothly almost everywhere except for certain crucial points where drastic changes occur (the new asymptotic behaviour ceases to be topologically equivalent to the old one). These points are called bifurcation boundaries and are caused by attractors that appear, disappear or change shape. 

(Doya, 1993) hypothesizes that such bifurcation crossings could cause the gradients to explode. We would like to extend this observation into a sufficient condition for gradients to explode, and for that reason we will re-use the one-hidden unit model (and plot) from (Doya, 1993) (see Fig. 3).

---

[referencia=319a638394e5883b score=0.822]
### **3.3. Vanishing gradient regularization** 

We opt to address the vanishing gradients problem using a regularization term that represents a preference for parameter values such that back-propagated gradients neither increase or decrease too much in magnitude. Our intuition is that increasing the norm of _<u>∂</u>_ **<u>x</u>** _<u>t</u>_<sup>theerrorattime</sup><sup>_t_ismoresensitivetoall</sup> _∂_ **x** _k_<sup>means</sup> inputs **u** _t, ..,_ **u** _k_ ( _∂_<sup>_<u>∂</u>_</sup> **x**<sup>**<u>x</u>**</sup> _k_<sup>_<u>t</u>_isafactorin</sup> _∂∂_ **u** _<u>Ekt</u>_<sup>).Inpractice</sup> some of these inputs will be irrelevant for the prediction at time _t_ and will behave like noise that the network needs to learn to ignore. The network can not learn to ignore these irrelevant inputs unless there is an error signal. These two issues can not be solved in parallel, and it seems natural to expect that we need to force the network to increase the norm of<sup>_<u>∂</u>_</sup><sup>**<u>x</u>**</sup><sup>_<u>t</u>_</sup> _∂_ **x** _k_<sup>at the</sup> expense of larger errors (caused by the irrelevant input entries) and _then_ wait for it to learn to ignore these irrelevant input entries. This suggest that moving towards increasing the norm of _∂∂_ **xx** _kt_<sup>cannotbealways</sup> done while following a descent direction of the error _E_ (which is, for e.g., what a second order method would try to do), and therefore we need to enforce it via a regularization term. 

The regularizer we propose below prefers solutions for which the error signal preserves norm as it travels back in time:

---

[referencia=319a638394e5883b score=0.810]
The regularizer we propose below prefers solutions for which the error signal preserves norm as it travels back in time: 



In order to be computationally efficient, we only use the “immediate” partial derivative of Ωwith respect to _<u>∂E</u>_ **W** _rec_ (we consider that **x** _k_ and _∂_ **x** _k_ +1<sup>as being constant</sup> with respect to **W** _rec_ when computing the derivative of Ω _k_ ), as depicted in equation (10). Note we use the parametrization of equation (11). This can be done efficiently because we get the values of _∂∂_ **x** _<u>Ek</u>_<sup>from BPTT.</sup> We use Theano to compute these gradients (Bergstra _et al._ , 2010; Bastien _et al._ , 2012). 



Note that our regularization term only forces the Jacobian matrices<sup>_∂_</sup> _∂_<sup>**x**</sup> **x**<sup>_k_</sup><sup><u>+</u></sup> _k_<sup>1</sup> to preserve norm in the relevant 

direction of the error _<u>∂E</u>_<sup>notforanydirection(i.e.</sup> _∂_ **x** _k_ +1<sup>,</sup> we do not enforce that all eigenvalues are close to 1). The second observation is that we are using a soft constraint, therefore we are not ensured the norm of the error signal is preserved. If it happens that these Jacobian matrices are such that the norm explodes (as _t−k_ increases), then this could lead to the exploding gradients problem and we need to deal with it for example as described in section 3.2. This can be seen from the dynamical systems perspective as well: preventing vanishing gradients implies that we are pushing the model such that it is further away from the attractor (such that it does not converge to it, case in which the gradients vanish) and closer to boundaries between basins of attractions, making it more probable for the gradients to explode.

---

[referencia=319a638394e5883b score=0.770]
### **3.1. Previous solutions** 

Using an L1 or L2 penalty on the recurrent weights can help with exploding gradients. Given that the parameters initialized with small values, the spectral radius of **W** _rec_ is probably smaller than 1, from which it follows that the gradient can not explode (see necessary condition found in section 2.1). The regularization term can ensure that during training the spectral radius never exceeds 1. This approach limits the model to a simple regime (with a single point attractor at the origin), where any information inserted in the model has to die out exponentially fast in time. In such a regime we can not train a generator network, nor can we exhibit long term memory traces. 

Doya (1993) proposes to pre-program the model (to initialize the model in the right regime) or to use _teacher forcing_ . The first proposal assumes that if the model exhibits from the beginning the same kind of asymptotic behaviour as the one required by the target, then there is no need to cross a bifurcation boundary. The downside is that one can not always know the required asymptotic behaviour, and, even if such information is known, it is not trivial to initialize a model in this specific regime. We should also note that such initialization does not prevent crossing the boundary between basins of attraction, which, as shown, could happen even though no bifurcation boundary is crossed. 

Teacher forcing is a more interesting, yet a not very well understood solution. It can be seen as a way of initializing the model in the right regime and the right 

**On the difficulty of training Recurrent Neural Networks** 

region of space. It has been shown that in practice it can reduce the chance that gradients explode, and even allow training generator models or models that work with unbounded amounts of memory(Pascanu and Jaeger, 2011; Doya and Yoshizawa, 1991). One important downside is that it requires a target to be defined at every time step.

---

[referencia=319a638394e5883b score=0.760]
## **5. Summary and Conclusions** 

We provided different perspectives through which one can gain more insight into the _exploding and vanishing gradients_ issue. To deal with the exploding gradients problem, we propose a solution that involves clipping the norm of the exploded gradients when it is too large. The algorithm is motivated by the assumption that when gradients explode, the curvature and higher order derivatives explode as well, and we are faced with a specific pattern in the error surface, namely a valley with a single steep wall. In order to deal with the vanishing gradient problem we use a regularization term that forces the error signal not to vanish as it travels back in time. This regularization term forces the Jacobian matrices _<u>∂</u>_ **<u>x</u>** _<u>i</u>_<sup>preservenormonlyin</sup> _∂_ **x** _i−_ 1<sup>to</sup> relevant directions. In practice we show that these solutions improve performance on both the pathological synthetic datasets considered as well as on polyphonic music prediction and language modelling. 

### **Acknowledgements** 

We would like to thank the Theano development team as well (particularly to Frederic Bastien, Pascal Lamblin and James Bergstra) for their help. 

We acknowledge NSERC, FQRNT, CIFAR, RQCHP and Compute Canada for the resources they provided.

---

[referencia=319a638394e5883b score=0.751]
### **1.1. Training recurrent networks** 

A generic recurrent neural network, with input **u** _t_ and state **x** _t_ for time step _t_ , is given by equation (1). In the theoretical section of this paper we will sometimes make use of the specific parametrization given by equation (11)<sup>1</sup> in order to provide more precise conditions and intuitions about the everyday use-case. 



The parameters of the model are given by the recurrent weight matrix **W** _rec_ , the biases **b** and input weight matrix **W** _in_ , collected in _θ_ for the general case. **x** 0 is provided by the user, set to zero or learned, and _σ_ is an element-wise function (usually the _tanh_ or _sigmoid_ ). A cost _E_ measures the performance of the network on some given task and it can be broken apart into individual costs for each step _E_ =<sup>�</sup> 1 _≤t≤T_<sup>_Et_,where</sup> _Et_ = _L_ ( **x** _t_ ). 

One approach that can be used to compute the necessary gradients is Backpropagation Through Time (BPTT), where the recurrent model is represented as 

> 1 This formulation is equivalent to the more widely known equation **x** _t_ = _σ_ ( **W** _rec_ **x** _t−_ 1 + **W** _in_ **u** _t_ + **b** ), and it was chosen for convenience. 

**On the difficulty of training Recurrent Neural Networks** 

a deep multi-layer one (with an unbounded number of layers) and backpropagation is applied on the unrolled model (see Fig. 2). 



<!-- Start of picture text -->

---

[referencia=319a638394e5883b score=0.724]
### **2.3. The geometrical interpretation** 

Let us consider a simple one hidden unit model (equation (8)) where we provide an initial state _x_ 0 and train the model to have a specific target value after 50 steps. Note that for simplicity we assume no input. 



Fig. 6 shows the error surface _E_ 50 = ( _σ_ ( _x_ 50) _−_ 0 _._ 7)<sup>2</sup> , where _x_ 0 = _._ 5 and _σ_ to be the sigmoid function. 

We can more easily analyze the behavior of this model by further simplifying it to be linear ( _σ_ then being the identity function), with _b_ = 0. _xt_ = _x_ 0 _w_<sup>_t_</sup> from which it follows that<sup>_<u>∂x</u>_</sup> _∂w_<sup>_<u>t</u>_=</sup><sup>_tx_0</sup><sup>_wt−_1and</sup><sup>_<u>∂</u>_</sup> _∂w_<sup>2</sup><sup>_<u>x</u>_2</sup><sup>_<u>t</u>_=</sup><sup>_t_(</sup><sup>_t−_1)</sup><sup>_x_0</sup><sup>_wt−_2,</sup> implying that when the first derivative explodes, so does the second derivative. 

In the general case, when the gradients explode they do so along some directions **v** . This says that there exists, in such situations, a vector **v** such that<sup>_<u>∂</u>_</sup> _∂θ_<sup>_<u>Et</u>_</sup><sup>**v**</sup><sup>_≥Cαt_,</sup> where _C, α ∈_ R and _α >_ 1. For the linear case ( _σ_ is the identity function), **v** is the eigenvector corresponding to the largest eigenvalue of **W** _rec_ . If this bound is tight, we hypothesize that in general _when gradients_ 

**On the difficulty of training Recurrent Neural Networks**