[referencia=c684a6d64091ddbb score=0.804]
### 1.2 Related Work

##### In-Context Learning.

Brown et al. [8] demonstrated that GPT-3 can perform in-context learning, which has led to much subsequent work on understanding how such in-context learning ability arises. Xie et al. [36] presents a Bayesian perspective on in-context learning by looking at the log-likelihood of out-of-distribution prompt sequences. Olsson et al. [27] posits that in-context learning relies on the emergence of induction heads.

Garg et al. [17] formalizes the setting of learning a function class in-context, and shows that transformers can be trained to in-context learn various simple function classes such as (sparse) linear models or shallow neural networks. This bears similarity to transformer neural processes [26], which recasts uncertainty-aware meta learning as an in-context learning task. Many recent works have sought to understand which in-context learning algorithms can be efficiently expressed by a transformer. Akyürek et al. [2], Bai et al. [4], Von Oswald et al. [35] show that transformers can implement gradient descent to solve in-context linear regression, while Fu et al. [16] constructs transformers which implement higher-order learning algorithms such as Newton’s method. Giannou et al. [18] constructs a transformer that can express general-purpose computational operations. However, these works are solely concerned with the representational capabilities of transformers, and do not answer the question of whether gradient descent indeed learns such constructions.

---

[referencia=c684a6d64091ddbb score=0.491]
##### Training dynamics of transformers.

Prior works have primarily studied the optimization dynamics of a single attention layer. Lu et al. [24], Li et al. [23] show that a single attention layer trained via gradient descent learns to encode topic structure. Snell et al. [29] studies the dynamics of a simplified attention layer on sequence-to-sequence translation tasks. Tarzanagh et al. [31], Tarzanagh et al. [30] show an equivalence between the optimization dynamics of a single attention layer and a certain SVM problem. Ahn et al. [1] shows that the global optimum of a single linear attention layer trained on in-context linear regression implements a single step of preconditioned gradient descent. Mahankali et al. [25], Zhang et al. [37] study the optimization dynamics of a single linear attention layer for performing in-context linear regression. Huang et al. [19] shows that gradient descent on a single softmax attention layer learns to solve linear regression in-context when the input data are orthogonal. Jelassi et al. [20] analyzes the gradient descent dynamics of the position-position block of a single layer vision transformer, and shows that it converges to a solution encoding spacial structure. Tian et al. [32] studies the optimization dynamics of a single attention layer for a specific toy dataset, while Tian et al. [33] shows that jointly training a self-attention and MLP layer corresponds to the optimization dynamics of a certain modified MLP module. Boix-Adsera et al. [6] shows that transformers with diagonal attention matrices display incremental learning behavior.

Bietti et al. [5] studies a synthetic ICL task, and shows that an induction head is formed during training. They demonstrate heuristically that a few gradient steps on a modifed transformer architecture approximately learns the induction head. Our synthetic task handles more general causal structure, and requires attending to all prior instances of the final token rather than the most recent one. Furthermore, Bietti et al. [5] requires the alphabet size to be significantly larger than the context length ; we, however, assume that , and our main theorem (Theorem 1) is an end-to-end guarantee on learning the causal structure and obtaining vanishing population loss.

---

[referencia=c684a6d64091ddbb score=0.490]
As another example, consider the setting of learning a function class in-context, introduced by Garg et al. [17]. Each prompt sequence is formed by sampling a new function from some function class , and generating the prompt for i.i.d inputs . The model must learn to estimate from the pairs given in-context. This setting has proved a useful testbed to understand which in-context learning algorithms can be implemented by transformers; see Section 1.2 for additional discussion. Such prompts also possess special causal structure. Conditioned on , the -th token in the prompt only depends on the -th token, and is independent of the rest of the sequence. The model must thus learn to associate each , at position , with its corresponding , at position . We view this instance as a problem with both a global causal structure, which comes from pairing with , and an in-context transition which comes from the specific sampled for the sequence.

Transformers are clearly able to model causal structure, yet despite the necessity of doing so for performing in-context learning tasks, we still do not understand how such structures are learned by gradient descent when training from scratch. We thus ask the following question:

How do transformers learn causal structure with gradient descent?

---

[referencia=c684a6d64091ddbb score=0.430]
# How Transformers Learn Causal Structure with Gradient Descent

###### Abstract

The incredible success of transformers on sequence modeling tasks can be largely attributed to the *self-attention* mechanism, which allows information to be transferred between different parts of a sequence. Self-attention allows transformers to encode causal structure which makes them particularly suitable for sequence modeling. However, the process by which transformers learn such causal structure via gradient-based training algorithms remains poorly understood. To better understand this process, we introduce an in-context learning task that requires learning latent causal structure. We prove that gradient descent on a simplified two-layer transformer learns to solve this task by encoding the latent causal graph in the first attention layer. The key insight of our proof is that the gradient of the attention matrix encodes the mutual information between tokens. As a consequence of the data processing inequality, the largest entries of this gradient correspond to edges in the latent causal graph. As a special case, when the sequences are generated from in-context Markov chains, we prove that transformers learn an *induction head* [27]. We confirm our theoretical findings by showing that transformers trained on our in-context learning task are able to recover a wide variety of causal structures.

---

[referencia=c684a6d64091ddbb score=0.322]
- [18]
Angeliki Giannou, Shashank Rajput, Jy-yong Sohn, Kangwook Lee, Jason D Lee, and
Dimitris Papailiopoulos.
Looped transformers as programmable computers.
*arXiv preprint arXiv:2301.13196* , 2023.
- [19]
Yu Huang, Yuan Cheng, and Yingbin Liang.
In-context convergence of transformers.
*arXiv preprint arXiv:2310.05249* , 2023.
- [20]
Samy Jelassi, Michael Sander, and Yuanzhi Li.
Vision transformers provably learn spatial structure.
*Advances in Neural Information Processing Systems* ,
35:37822–37836, 2022.
- [21]
John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov,
Olaf Ronneberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin
Žídek, Anna Potapenko, et al.
Highly accurate protein structure prediction with alphafold.
*Nature* , 596(7873):583–589, 2021.
- [22] Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization, 2017.
- [23]
Yuchen Li, Yuanzhi Li, and Andrej Risteski.
How do transformers learn topic structure: Towards a mechanistic
understanding.
In *International Conference on Machine Learning* , pages
19689–19729. PMLR, 2023.
- [24]
Haoye Lu, Yongyi Mao, and Amiya Nayak.
On the dynamics of training attention models.
In *International Conference on Learning Representations* , 2021.
URL https://openreview.net/forum?id=1OCTOShAmqB.
- [25]
Arvind Mahankali, Tatsunori B Hashimoto, and Tengyu Ma.
One step of gradient descent is provably the optimal in-context
learner with one layer of linear self-attention.
*arXiv preprint arXiv:2307.03576* , 2023.

---

[referencia=c684a6d64091ddbb score=0.280]
##### Concurrent Work.

A number of concurrent works also study the ability of transformers to solve synthetic in-context learning tasks. Reddy [28] shows empirically that an induction head suddenly emerges during the training of a two-attention layer transformer on a specific in-context learning task. Akyürek et al. [3] demonstrates that transformers can learn regular languages in-context, where each prompt consists of strings generated from a prompt-dependent formal language. This is due to the ability of transformers to compute in-context -gram counts, via a generalization of the induction head mechanism using multiple attention layers. In Section 6, we show that a two-layer transformer with heads can also compute such -gram counts.

Edelman et al. [13] study the formation of induction heads on the task of learning Markov chains in context, which is equivalent to our Task 1 when the latent causal graph is the chain graph. Their theoretical analysis focuses on two steps of gradient descent on a simplified linear transformer model, for Markov chains over two states. An interesting empirical observation of theirs is that transformers trained to learn -grams in-context undergo a sequential learning procedure, by first predicting using the unigram counts, then the bigram counts, and so on.

---

[referencia=c684a6d64091ddbb score=0.176]
### 1.1 Our Contributions

In this work, we analyze the gradient descent dynamics of an autoregressive two-layer attention-only transformer, and prove that it recovers latent causal structure. Our specific contributions are as follows:

- • 
We introduce a novel family of in-context learning problems, which we call *random sequences with causal structure* (Task 1). The task fixes a latent causal structure, unknown to the transformer, and samples each sequence from a different distribution which respects the causal structure.
- • 
When the latent causal graph is a tree, we prove that gradient descent on a simplified two-layer transformer solves this task by encoding the causal graph in the first attention layer in order to perform in-context estimation of the transition distribution (Theorem 1). As a special case of Theorem 1, we show that when the sequences are generated from in-context Markov chains, the transformer learns an induction head.
- • 
The proof of Theorem 1 relies on showing that the gradient of the first attention layer automatically computes the -mutual information between pairs of tokens. As a result of the data processing inequality, the largest entries of this gradient correspond to edges in the latent causal graph, and hence the first attention layer converges to the adjacency matrix of this graph.
- • 
When the causal graph is not a tree, we explicitly construct a multi-head transformer which solves this task by distributing the latent causal graph across many heads. We show empirically that transformers trained by gradient descent on this task learn our construction.

---

[referencia=c684a6d64091ddbb score=0.147]
## 6 Causal Graphs with Multiple Parents

We next consider a generalization of Task 1. Let be a directed acyclic graph over the vertex set . For each node , we assume that the set of parent nodes satisfy the property that either or . If , we write , where . As before, let be the root nodes. We additionally assume that .

We now consider -parent transition tensors : For any , is a probability distribution over . Let be a prior over such . Each sequence is now generated as follows:

###### Task 2 (Graphs with Multiple Parents).

1. 1. 
Draw .
2. 2. 
For , if , sample . Otherwise, sample
3. 3. 
Return the input and the target .

##### Example.

One example of Task 2 is learning in-context -grams. In an -gram model, each token only depends on the prior tokens in the sequence. This -gram model can be obtained by setting , letting the root nodes be , and choosing the parent sets for . The conditional density is then just the transition ; the goal is to estimate this transition in-context, by first learning that all sequences share the same -gram causal structure.

Given a sequence , a good estimate for the transition is the empirical transition , defined as

|  |  |  | (34) | 

We explicitly construct a two-layer transformer with heads in the first layer that approximately expresses this empirical transition.

###### Construction 2.

There exists a two attention layer transformer with heads such that

|  |  |  | (35) | 

Construction 2 is deferred to Appendix B. At a high level, the th head in the first layer copies to the residual stream of , and copies to the residual stream of ; the second attention head compares these tuples of parents, and thus attends to tokens where for all .

In Figures 5 and 7, we show empirically that transformers trained on Task 2 for varying latent graphs indeed converge to such a construction. The challenge, however, in analyzing the gradient descent dynamics is that there are multiple attention heads each of which attends to a different parent. The dynamics must thus break the symmetry between the multiple heads. Analyzing the optimization dynamics of a multi-head transformer for solving Task 2 is thus a very interesting direction for future work.

---

[referencia=c684a6d64091ddbb score=0.126]
### D.5 Gradient of (Stage 1)

We show that during the first stage of training, converges to the adjacency matrix of the graph .

The first step is to show that a quantity called the “idealized gradient” approximately aligns with the adjacency matrix of . For a transition matrix , define

and let .

The following lemma shows that this idealized gradient is maximized at . The proof relies on the data processing inequality argument, and is deferred to Section G.1.

###### Lemma 5 (Idealized gradient is aligned with ).

If , then

for all . Otherwise .

Next, we show that the true gradient with respect to can indeed be approximated by this idealized gradient, and hence the adjacency matrix of .

###### Lemma 6 (True gradient of is aligned with (Stage 1)).

Let . There exist constants such that, if ,

- • 
If , for with .
- • 
If , then for any ,

###### Proof.

First, see that

Thus

Let , and define the quantities by

We remark that

|  |  |  | (37) | 

Since , by Lemma 23 we have

It thus suffices to analyze . Note that . Therefore

and

The th entry of , , is thus equal to

By Lemma 24, this is approximately equal to the idealized gradient :

We are now ready to prove the theorem. First, consider the case where . By Lemma 5, , and thus

Since , the claim follows.

Otherwise if , Lemma 5 tells us that, for all ,

Next, see that

Therefore for any , we can bound

as desired. ∎

We can now analyze the gradient descent dynamics over multiple timesteps. First, we show that for most root nodes , moves very little.

###### Lemma 7.

Let . Then

for all .

###### Proof.

Let . We have that (where is the vector from Lemma 6),

and thus

Fix . Assume there exists some such that , and let be the first such time . We can always bound

and thus for , . Therefore

Bounding and , we get that

Additionally, when , we have the bound

Therefore

as desired. ∎

Next, we bound the time it takes until .

###### Lemma 8.

Let , where There exists such that, for any

for all with .

---

[referencia=c684a6d64091ddbb score=0.103]
- [33]
Yuandong Tian, Yiping Wang, Zhenyu Zhang, Beidi Chen, and Simon Du.
Joma: Demystifying multilayer transformers via joint dynamics of mlp
and attention.
*arXiv preprint arXiv:2310.00535* , 2023b.
- [34]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin.
Attention is all you need.
*Advances in neural information processing systems* , 30, 2017.
- [35]
Johannes Von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento,
Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov.
Transformers learn in-context by gradient descent.
In *International Conference on Machine Learning* , pages
35151–35174. PMLR, 2023.
- [36]
Sang Michael Xie, Aditi Raghunathan, Percy Liang, and Tengyu Ma.
An explanation of in-context learning as implicit bayesian inference.
*arXiv preprint arXiv:2111.02080* , 2021.
- [37]
Ruiqi Zhang, Spencer Frei, and Peter L Bartlett.
Trained transformers learn linear models in-context.
*arXiv preprint arXiv:2306.09927* , 2023.

---

[referencia=c684a6d64091ddbb score=0.096]
## 3 What does the Transformer Learn?

### 3.1 Experiments

We train a series of two-layer disentangled transformers with one head per layer on Task 1, for varying latent graphs . The prior is chosen so that each row of is sampled i.i.d from the Dirichlet distribution with parameter , i.e , for varying values of . We train using gradient descent on the cross entropy loss with initial learning rate and cosine decay over steps.

We observe that the weights of the trained disentangled transformers exhibit consistent structure. First, all of the entries of remain small except the position-position block (red box under in Figure 2), which converges to the adjacency matrix of the graph . Next, all of the entries of are small, except the token/token block comparing the component of the residual stream of token to the component of the residual stream of token for (red box under in Figure 2). Finally, all of the entries of the output matrix are small except the token/token block which returns the value of the first component of the output of the second attention (red box under in Figure 2). In Figure 6, we observe that this weight pattern persists for different latent graphs .

In the following section, we explicitly define this construction and describe the corresponding dynamics of the forward pass in Figure 3.

---

[referencia=c684a6d64091ddbb score=0.089]
## 4 Main Results

### 4.1 Training Algorithm

Our training algorithm is stage-wise gradient descent on the population loss (18) using the reduced model (17). The model is initialized at for small initialization scale . The first stage is gradient descent on with learning rate for timesteps. The second stage is gradient descent on with learning rate for timesteps. Pseudocode is given in Algorithm 1.

We require the following assumptions on the prior :

###### Assumption 1 (Assumptions on prior .).

There exists such that almost surely over the draw of :

- • 
(Transition lower bounded): .
- • 
(Non-degeneracy of chain): The chain does not immediately mix to the stationary measure in one step:
- • 
(Symmetry): For any permutation on , .
- • 
(Constant mean): .

The final two assumptions imply that the marginal distributions of are equal for any , and likewise for , and that these distributions have mean . We remark that Assumption 1 is satisfied with probability for some when each row of is sampled i.i.d from a Dirichlet distribution with parameter .

Additionally, we assume that a non-vanishing fraction of nodes have a parent.

###### Assumption 2.

Let . Then .

Throughout the proof, we let  denote an absolute constant that depends *polynomially* on  and . If , then we write  or . For convenience, we also drop the dependence on , and write  or .

---

[referencia=c684a6d64091ddbb score=0.059]
#### 5.1.2 The Gradient Descent Dynamics

We next compute the gradient with respect to . Let denote the th row of (restricted to the first entries, since is lower triangular). Define by ; is the Jacobian of the softmax function , in that

The following lemma computes the gradient with respect to ; a heuristic derivation is deferred to Section D.3.

###### Lemma 3.

|  |  |  | (25) | 

where the th entry of , , is

|  |  |  | (26) | 

For non-root nodes , has joint distribution , and thus is

|  |  |  | (27) | 

It turns out that this expression is exactly equal to the -mutual information, , between and conditioned on . The -divergence is the -divergence obtained by setting . Therefore

|  |  |  | (28) | 

By Cauchy-Schwarz, we can also upper bound by the sum of two -mutual informations:

|  |  |  | (29) | 

Applying the data processing inequality<sup>1</sup><sup>1</sup>
                1
                
                
                
                
                
                
                
              By the assumptions on the prior  (Assumption 1), the data processing inequality is indeed strict., we obtain that for 

|  |  |  | (30) | 

Therefore is maximized at , and the gradient is aligned with the adjacency matrix of the causal graph . In fact, the gradient descent dynamics mimic Algorithm 2!

Maintaining the inductive hypothesis that , we see by the gradient formula in Lemma 3 that . Thus continues to grow faster than the other entries throughout stage 1. This growth continues until

For root nodes , is independent of . Since both and have the marginal , one has

|  |  |  | (31) | 

and thus . Therefore at the end of stage 1, for all .

Altogether, at the end of stage , satisfies

|  |  |  | (32) | 

The precise quantitative bound is given in Corollary 1, and requires controlling the various error terms throughout multiple steps of gradient descent.

### 5.2 Stage 2: Decreasing the Loss

We next show that during the second stage, grows large in the direction . By a symmetry argument, one can show that is proportional to . Writing , it suffices to show that .

---

[referencia=c684a6d64091ddbb score=0.043]
- [1]
Kwangjun Ahn, Xiang Cheng, Hadi Daneshmand, and Suvrit Sra.
Transformers learn to implement preconditioned gradient descent for
in-context learning.
*arXiv preprint arXiv:2306.00297* , 2023.
- [2]
Ekin Akyürek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou.
What learning algorithm is in-context learning? investigations with
linear models.
In *The Eleventh International Conference on Learning
Representations* , 2023.
URL https://openreview.net/forum?id=0g0X4H8yN4I.
- [3]
Ekin Akyürek, Bailin Wang, Yoon Kim, and Jacob Andreas.
In-context language learning: Arhitectures and algorithms.
*arXiv preprint arXiv:2401.12973* , 2024.
- [4]
Yu Bai, Fan Chen, Huan Wang, Caiming Xiong, and Song Mei.
Transformers as statisticians: Provable in-context learning with
in-context algorithm selection.
*arXiv preprint arXiv:2306.04637* , 2023.
- [5]
Alberto Bietti, Vivien Cabannes, Diane Bouchacourt, Herve Jegou, and Leon
Bottou.
Birth of a transformer: A memory viewpoint.
*arXiv preprint arXiv:2306.00802* , 2023.
- [6]
Enric Boix-Adsera, Etai Littwin, Emmanuel Abbe, Samy Bengio, and Joshua
Susskind.
Transformers learn through gradual rank increase.
*arXiv preprint arXiv:2306.07042* , 2023.
- [7] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and Qiao Zhang. JAX: composable transformations of Python+NumPy programs, 2018. URL http://github.com/google/jax.

---

[referencia=c684a6d64091ddbb score=0.041]
##### Output Layer.

reads from the third block in this stream, which we denoted by in (15) above. It then returns the token embedding of which is equal to:

|  |  |  | (16) | 

as desired. ∎

See Figure 3 for a breakdown of this forward pass through the transformer for a specific sequence.

### 3.3 The Reduced Model

Motivated by the sparsity pattern in Figure 2 and Section 3.2, we consider training a simplified two-layer transformer architecture where the sparsity in Section 3.2 is fixed, and only and are trained. The transformer can be rewritten as the following reduced model:

###### Lemma 1.

Let , and let be defined in Section 3.2. Let be a two-layer disentangled transformer parameterized by . Then if where ,

|  |  |  | (17) | 

Due to the masking operation, we can restrict to be lower diagonal.

Our goal is to analyze the gradient descent dynamics of under the cross entropy loss. However, if the token does not appear in , then is and the cross entropy loss is infinite. As such, we perturb the predictions by some small . The perturbed population loss is thus:

|  |  |  | (18) |

---

[referencia=c684a6d64091ddbb score=0.040]
### I.2 Stage 2

One challenge in directly using the population analysis for stage 2 is that the finite-sample update no longer preserves symmetry, and hence we do not have that throughout the entirety of stage 2. Instead, we will consider taking only a single large gradient step with learning rate , on an independent dataset of prompts.

During the first step of stage 2, the population gradient is

where, by Lemma 10,

The following lemma concentrates the population gradient to the empirical gradient at :

###### Lemma 34.

###### Proof.

The finite sample gradient can be written as

Let . By (46), we have

Additionally, . We next see that we can bound

Therefore on , each entry of can be bounded in absolute value by , and on each entry can be bounded by some . Therefore by an identical concentration argument as in Lemma 33, with high probability we get that

∎

After one gradient step with learning rate , is equal to

where the error matrix satisfies .

Next, define the parameter vector as , where is the result of the population update. We can bound the error between the finite-sample predictor and population predictor as

Now if we choose so that , then by Lemma 32, we get that satisfies

Therefore

as long as . Therefore the output of running gradient descent on the finite sample loss, , achieves small population loss.

Altogether, both Stage 1 and Stage 2 succeed on the finite-sample loss as long as .

---

[referencia=c684a6d64091ddbb score=0.025]
## Appendix I Finite Sample Analysis

Our theory focuses on the case of gradient descent on the population loss (18). It is relatively straightforward to extend our analysis to the finite sample setting. In this case, we are given a dataset of prompts of length :

Each sequence is generated via the procedure in Task 1, with transition matrix . Let be the embedding of .

We now consider running gradient descent on the finite sample loss :

|  |  |  | (47) | 

Below, we present a sketch of the extension of the analysis of our main theorem to this finite sample setting.

### I.1 Stage 1

The crux of Stage 1 is Lemma 6, where in (37) we show that

where the vector is defined by

In particular, we show that satisfies the property that

for and for . As a step towards proving this, we let , define the quantity by

and show that

The empirical gradient can be written as

where

As in the population setting, we define to be

By Lemma 23, we get that It thus suffices to show that is small, which is given by the following lemma:

###### Lemma 33.

For any

with probability .

###### Proof.

First, see that can be written as

Define the event as

By a union bound, . We can naively bound , and on the complement of (denoted by ) we can bound . Therefore we can concentrate as:

with probability by Hoeffding’s inequality on the . Next, we see that the are Bernoulli random variables with mean and standard deviation at most . Therefore with probability , one has

since . Union bounding over yields the desired result ∎

Combining everything together, we get that for , the quantities satisfy

with high probability, and thus Stage 1 succeeds on the empirical loss with high probability.

---

[referencia=c684a6d64091ddbb score=0.011]
### D.6 Gradient of (Stage 2)

First, we observe that the population dynamics of possess a certain symmetry:

###### Lemma 9.

For all time, for some scalar .

###### Proof.

If (all diagonals are equal and all off-diagonals are equal), then by symmetry the gradient is also of this form. Additionally, see that

since . Therefore for some scalar . Since we initialize , throughout training is of the form . ∎

Throughout the rest of the proof, we let be the scalar such that

The goal of this section is to show that when approximates the adjacency matrix of , will grow large. Since the gradient descent update for is

the update for is

As such, we define the quantity by

Finally, for notational convenience, let be the matrix such that

encodes the adjacency matrix of on nodes where .

###### Lemma 10 (Stage 2).

Let , where is the output of stage 1, and for . If satisfies

then

---

[referencia=c684a6d64091ddbb score=0.006]
## 1 Introduction

The transformer architecture [34] has revolutionized the field of deep learning, and has led to state-of-the art performance on tasks spanning language modeling [8], computer vision [12], reinforcement learning [9], and the sciences [21]. The basic primitive of a transformer is a *self-attention* head, a sequence-to-sequence mapping in which each token in the output is a weighted linear combination of, i.e “attends to,” the other tokens in the sequence. Prior work [14] has sought to understand which specific computational operations, or “circuits,” are implemented by self-attention layers in trained transformers. However, the process by which such circuits arise when transformers are trained from scratch via gradient-based algorithms is still unknown.

One hallmark capability of transformers is *in-context learning* [8], which is the ability to learn from information present in the input context without needing to update the model parameters. For example, given a prompt of input-output pairs, in-context learning is the ability to predict the output corresponding to a new input. Prior work has shown that this in-context learning ability relies on the existence of specific circuits called *induction heads* [27]. Given a prompt of the form , an induction head copies the token which follows the previous occurrence of , in this case being . This can be implemented using two attention layers: the first performs the operation of “copying” the previous token, while the second compares this previous token to the last token of the context. By copying the previous token, the first attention layer thus implicitly encodes the causal structure of a Markov chain.

---

[referencia=c684a6d64091ddbb score=0.005]
- [26]
Tung Nguyen and Aditya Grover.
Transformer neural processes: Uncertainty-aware meta learning via
sequence modeling.
In *International Conference on Machine Learning* , pages
16569–16594. PMLR, 2022.
- [27]
Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma,
Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly,
Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott
Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario
Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah.
In-context learning and induction heads.
*Transformer Circuits Thread* , 2022.
https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html.
- [28]
Gautam Reddy.
The mechanistic basis of data dependence and abrupt learning in an
in-context classification task.
*arXiv preprint arXiv:2312.03002* , 2023.
- [29]
Charlie Snell, Ruiqi Zhong, Dan Klein, and Jacob Steinhardt.
Approximating how single head attention learns.
*arXiv preprint arXiv:2103.07601* , 2021.
- [30]
Davoud Ataee Tarzanagh, Yingcong Li, Christos Thrampoulidis, and Samet Oymak.
Transformers as support vector machines.
*arXiv preprint arXiv:2308.16898* , 2023a.
- [31]
Davoud Ataee Tarzanagh, Yingcong Li, Xuechen Zhang, and Samet Oymak.
Max-margin token selection in attention mechanism.
In *Thirty-seventh Conference on Neural Information Processing
Systems* , 2023b.
- [32]
Yuandong Tian, Yiping Wang, Beidi Chen, and Simon Du.
Scan and snap: Understanding training dynamics and token composition
in 1-layer transformer.
*arXiv preprint arXiv:2305.16380* , 2023a.