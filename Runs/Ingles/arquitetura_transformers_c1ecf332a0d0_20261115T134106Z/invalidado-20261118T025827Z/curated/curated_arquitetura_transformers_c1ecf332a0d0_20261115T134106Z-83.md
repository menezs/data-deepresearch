[referencia=ca517c4b4b64d6cc score=0.529]
### 5.1 GD<sup>++</sup> and least squares solver

GD<sup>++</sup>, introduced in von Oswald et al. (2023a), represents a linear transformer that is trained on a fixed noise variance problem (6). It is a variant of a diagonal linear transformer, with all the heads satisfying . Dynamics are influenced only by  and , leading to simpler updates:

|  |  |  |  | (11) | 

The update on acts as preconditioning and the update on performs gradient descent on the data.

While existing analysis by Ahn et al. (2023) has not yielded fast convergence rates for GD<sup>++</sup>, we show here that it is actually a second-order optimization algorithm for the least squares problem (4):

###### Theorem 5.1.

Given  where  has eigenvalues in the range  with a condition number . Let  be the optimal solution to least squares problem (4), then there exists hyperparameters for GD<sup>++</sup> algorithm that outputs  with accuracy  in  steps. In particular that implies there exists an -layer linear transformer that can solve this task.

The convergence rate of is typically achieved only by second-order algorithms such as Newton’s method.

---

[referencia=ca517c4b4b64d6cc score=0.404]
#### Baseline estimates.

We evaluated the linear transformer against a closed-form solution to the ridge regression problem (5). We estimated the noise variance using the following methods:

- • 
*Constant Ridge Regression (ConstRR).* The noise variance is estimated using a single scalar value for all the sequences, tuned separately for each mixed variance problem.
- • 
*Adaptive Ridge Regression (AdaRR).* Estimate the noise variance via unbiased estimator (Cherkassky & Ma, 2003) , where  represents the solution to the ordinary least squares (4), found in a closed-form.
- • 
*Tuned Adaptive Ridge Regression (TunedRR).* Same as above, but after the noise is estimated, we tuned two additional parameters to minimize the evaluation loss: (1) a max. threshold value for the estimated variance, (2) a multiplicative adjustment to the noise estimator. These values are tuned separately for each problem.

Notice that all the baselines above are based on ridge regression, which is a closed-form, non-iterative solution. Thus, they have an algorithmic advantage over linear transformers that do not have access to matrix inversion. These baselines help us gauge the best possible performance, establishing an upper bound rather than a strictly equivalent comparison.

A more faithful comparison to our method would be an iterative version of the AdaRR that does not use matrix inversion. Instead, we can use gradient descent to estimate the noise and the solution to the ridge regression. However, in practice, this gradient descent estimator converges to AdaRR only after iterations. In contrast, linear transformers typically converge in fewer than layers.

|  |  | 
|  |  | 

*Top:*loss for models with various number of layers and per-variance profile for models with 7 layers.

*Bottom:*Per-variance profile of the model across different numbers of layers. In-distribution noise is shaded gray.

We consider two choices for the distribution of :

- • 
*Uniform.* drawn from a uniform distribution bounded by . We tried multiple scenarios with  ranging from 0 to 7.
- • 
*Categorical.* chosen from a discrete set . We tested  and .

Our approach generalizes the problem studied by Bai et al. (2023), who considered only categorical variance selection and show experiments only with two values.

---

[referencia=ca517c4b4b64d6cc score=0.278]
## 1 Introduction

The transformer architecture (Vaswani et al., 2017) has revolutionized the field of machine learning, driving breakthroughs across various domains and serving as a foundation for powerful models (Anil et al., 2023; Achiam et al., 2023; Team et al., 2023; Jiang et al., 2023). However, despite their widespread success, the mechanisms that drive their performance remain an active area of research. A key component of their success is attributed to in-context learning (ICL, Brown et al., 2020) – an emergent ability of transformers to make predictions based on information provided within the input sequence itself, without explicit parameter updates.

Recently, several papers (Garg et al., 2022; Akyürek et al., 2022; von Oswald et al., 2023a) have suggested that ICL might be partially explained by an implicit meta-optimization of the transformers that happens on input context (aka mesa-optimization Hubinger et al., 2019). They have shown that transformers with linear self-attention layers (aka linear transformers) trained on linear regression tasks can internally implement gradient-based optimization.

Specifically, von Oswald et al. (2023a) demonstrated that linear transformers can execute iterations of an algorithm similar to the gradient descent algorithm (which they call GD<sup>++</sup>), with each attention layer representing one step of the algorithm. Later, Ahn et al. (2023); Zhang et al. (2023) further characterized this behavior, showing that the learned solution is a form of preconditioned GD, and this solution is optimal for one-layer linear transformers.

In this paper, we continue to study linear transformers trained on linear regression problems. We prove that each layer of every linear transformer maintains a weight vector for an underlying linear regression problem. Under some restrictions, the algorithm it runs can be interpreted as a complex variant of preconditioned gradient descent with momentum-like behaviors.

While maintaining a linear regression model (regardless of the data) might seem restrictive, we show that linear transformers can discover powerful optimization algorithms. As a first example, we prove that in case of GD<sup>++</sup>, the preconditioner results in a second order optimization algorithm.

---

[referencia=ca517c4b4b64d6cc score=0.104]
###### Proof.

By Lemma A.3 we know in iterations, by assigning in the way of Lemma A.3 one can reduce the condition number of to (we chose here to give some slack for later analysis).

Let be the covariance matrix after these iterations, and be the upper and lowerbound for its eigenvalues. The data ’s are transformed to a new data for some matrix . Let , then since we know is a matrix with singular values between and . The optimal solution has norm at most . Therefore by Lemma A.2 we know the one-step gradient step with satisfy . The test data is also transformed to , and the algorithm outputs , so the error is at most . By the choice of we can check that RHS is at most . ∎

### A.5 Proof of the Theorem 5.2

###### Proof.

The key observation here is that when , under the assumptions we have . Therefore the ridge regression solutions converge to and the desired output is .

By the calculations before, we know after the first-layer, the implicit is . As long as is a constant, when we know (as the part of that depend on is negligible compared to noise), therefore the output of the second layer satisfies

Therefore, as long as we choose and to satisfy when or (notice that these are two linear equations on and , so they always have a solution), then we have for the two noise levels. ∎

---

[referencia=ca517c4b4b64d6cc score=0.097]
### A.4 Proof for Theorem 5.1

In this section we prove Theorem 5.1 by finding hyperparameters for GD<sup>++</sup> algorithm that solves least squares problems with very high accuracy. The first steps in the construction iteratively makes the data ’s better conditioned, and the last step is a single step of gradient descent. The proof is based on several lemma, first we observe that if the data is very well-conditioned, then one-step gradient descent solves the problem accurately:

###### Lemma A.2.

Given where has eigenvalues between and . Let be the optimal least squares solution, then satisfies .

###### Proof.

We can write . By the fact that is the optimal solution we know ’s satisfy . Therefore . This implies

∎

Next we show that by applying just the preconditioning step of GD<sup>++</sup>, one can get a well-conditioned  matrix very quickly. Note that the  matrix is updated as , so an eigenvalue of  in the original  matrix would become . The following lemma shows that this transformation is effective in shrinking the condition number

###### Lemma A.3.

Suppose , then there exists an universal constant such that choosing implies

On the other hand, if where , then choosing implies

The first claim shows that one can reduce the condition number by a constant factor in every step until it’s a small constant. The second claim shows that once the condition number is small (), each iteration can bring it much closer to 1 (to the order of ).

Now we prove the lemma.

###### Proof.

First, notice that the function is monotonically nondecreasing for if (indeed, it’s derivative is always nonnegative). Therefore, the max is always achieved at and the min is always achieved at . The new ratio is therefore

When the ratio is always below which is a constant bounded away from 1.

When , we can write down the RHS in terms of

Note that by the careful choice of , the RHS has the following Taylor expansion:

One can then check the RHS is always upperbounded by when .

∎

With the two lemmas we are now ready to prove the main theorem:

---

[referencia=ca517c4b4b64d6cc score=0.094]
#### Categorical noise variance.

Fig. 3 shows a notable difference between Diag and Full models for categorical noise variance . This could stem from a bad local minima, or suggest a fundamental difference between the models for this problem. Interestingly, from per-variance profiling we see that Diag extrapolates better for variances not used for training, while Full, despite its lower in-distribution error, performs worse on unseen variances. Fig. 4 shows learned weights of the 4 layer linear transformer with Full parametrization. The weights are very diagonal heavy, potentially with some low-rank component.

For , examining the per-variance profile at the bottom of Fig. 3 reveals differences in their behaviors. Full exhibits a more complex per-variance profile with more fluctuations than the diagonal model, suggesting greater representational capacity. Surprisingly, it did not translate to better loss results compared to Diag.

For easy comparison, we compile the results of all methods and baselines in Table 1 in the Appendix.

## 7 Conclusions

Our research reveals the surprising ability of linear transformers to tackle challenging in-context learning problems. We show that each layer maintains an implicit linear regression model, akin to a complex variant of preconditioned gradient descent with momentum-like behavior.

Remarkably, when trained on noisy linear regression problems with unknown noise variance, linear transformers not only outperform standard baselines but also uncover a sophisticated optimization algorithm that incorporates noise-aware step-size adjustments and rescaling. This discovery highlights the potential of linear transformers to automatically discover novel optimization algorithms when presented with the right problems, opening exciting avenues for future research, including automated algorithm discovery using transformers and generalization to other problem domains.

While our findings demonstrate the impressive capabilities of linear transformers in learning optimization algorithms, we acknowledge limitations in our work. These include the focus on simplified linear models, analysis of primarily diagonal attention matrices, and the need for further exploration into the optimality of discovered algorithms, generalization to complex function classes, scalability with larger datasets, and applicability to more complex transformer architectures. We believe these limitations present valuable directions for future research and emphasize the need for a deeper understanding of the implicit learning mechanisms within transformer architectures.

---

[referencia=ca517c4b4b64d6cc score=0.087]
## 3 Related work

#### In-context Learning as Gradient Descent

Our work builds on research that frames in-context learning as (variants of) gradient descent (Akyürek et al., 2022; von Oswald et al., 2023a). For 1-layer linear transformer, several works Zhang et al. (2023); Mahankali et al. (2023); Ahn et al. (2023) characterized the optimal parameters and training dynamics. More recent works extended the ideas to auto-regressive models (Li et al., 2023; von Oswald et al., 2023b) and nonlinear models (Cheng et al., 2023). Fu et al. (2023) noticed that transformers perform similarly to second-order Newton methods on linear data, for which we give a plausible explanation in Theorem 5.1.

#### In-context Learning in LLMs

There are also many works that study how in-context learning works in pre-trained LLMs (Kossen et al., 2023; Wei et al., 2023; Hendel et al., 2023; Shen et al., 2023). Due to the complexity of such models, the exact mechanism for in-context learning is still a major open problem. Several works (Olsson et al., 2022; Chan et al., 2022; Akyürek et al., 2024) identified induction heads as a crucial mechanism for simple in-context learning tasks, such as copying, token translation and pattern matching.

#### Other theories for training transformers

Other than the setting of linear models, several other works (Garg et al., 2022; Tarzanagh et al., 2023; Li et al., 2023; Huang et al., 2023; Tian et al., 2023a; Tian et al., 2023b) considered optimization of transformers under different data and model assumptions. Wen et al. (2023) showed that it can be difficult to interpret the “algorithm” performed by transformers without very strong restrictions.

---

[referencia=ca517c4b4b64d6cc score=0.066]
### 5.3 Understanding : adapting step-sizes

The final term in the diagonal model, , has a more complicated effect. Since it changes only the -coordinates, it does not have an immediate effect on . To understand how it influences the we consider a simplified two-step process, where the first step only has and the second step only has (so the second step is just doing one step of gradient descent). In this case, the first layer will update the ’s as:

There are two effects of the term, one is a multiplicative effect on , and the other is an additive term that makes -output related to the residual . The multiplicative step in has an unknown preconditioning effect. For simplicity we assume the multiplicative term is small, that is:

The first layer does not change , so and . For this set of , we can write down the output on in the second layer as

Here we used the properties of residual (in particular , and ). Note that is basically what a gradient descent step on the original input should do. Therefore effectively, the two-layer network is doing gradient descent, but the step size is the product of and . The factor depends on the level of noise, and when , the effective step size is smaller when there is more noise. This is especially helpful in the model selection problem, because intuitively one would like to perform early-stopping (small step sizes) when the noise is high.

---

[referencia=ca517c4b4b64d6cc score=0.066]
### 2.2 Noisy regression model

As a model problem, we consider data generated from a noisy linear regression model. For each input sequence , we sample a ground-truth weight vector , and generate data points as and , with noise .

Note that each sequence can have different ground-truth weight vectors , but every data point in the sequence shares the same and . The query is generated as and (since the noise is independent, whether we include noise in will only be an additive constant to the final objective).

We further define an ordinary least square (OLS) loss as

|  |  |  | (4) | 

The OLS solution is with residuals .

In the presence of noise ,  in general is not equal to the ground truth . For a *known* noise level , the best estimator for  is provided by ridge regression:

|  |  |  | (5) | 

with solution . Of course, in reality the variance of the noise is not known and has to be estimated from the data.

### 2.3 Fixed vs. mixed noise variance problems

We consider two different problems within the noisy linear regression framework.

#### Fixed noise variance.

In this scenario, the variance remains constant for all the training data. Here, the in-context loss is:

|  |  |  | (6) | 

where  and . This problem was initially explored by Garg et al. (2022). Later, von Oswald et al. (2023a) have demonstrated that a linear transformer (6) converges to a form of a gradient descent solution, which they called GD<sup>++</sup>. We define this in details later.

#### Mixed noise variance.

In this case, the noise variance is drawn from some fixed distribution for each sequence. The in-context learning loss becomes:

|  |  |  | (7) | 

In other words, each training sequence  has a fixed noise level , but different training sequences have different noise levels sampled from a specified distribution . This scenario adds complexity because the model must predict  for changing noise distribution, and the optimal solution likely would involve some sort of noise estimation. We have found that empirically, GD<sup>++</sup> fails to model this noise variance and instead converges to a solution which can be interpreted as a single noise variance estimate across all input data.

---

[referencia=ca517c4b4b64d6cc score=0.061]
- Mahankali et al. (2023)
Arvind Mahankali, Tatsunori B Hashimoto, and Tengyu Ma.
One step of gradient descent is provably the optimal in-context
learner with one layer of linear self-attention.
*arXiv preprint arXiv:2307.03576* , 2023.
- Mirchandani et al. (2023)
Suvir Mirchandani, Fei Xia, Pete Florence, Brian Ichter, Danny Driess,
Montserrat Gonzalez Arenas, Kanishka Rao, Dorsa Sadigh, and Andy Zeng.
Large language models as general pattern machines.
*arXiv preprint arXiv:2307.04721* , 2023.
- Olsson et al. (2022)
Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma,
Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, et al.
In-context learning and induction heads.
*arXiv preprint arXiv:2209.11895* , 2022.
- Pathak et al. (2023)
Reese Pathak, Rajat Sen, Weihao Kong, and Abhimanyu Das.
Transformers can optimally learn regression mixture models.
*arXiv preprint arXiv:2311.08362* , 2023.
- Schlag et al. (2021)
Imanol Schlag, Kazuki Irie, and Jürgen Schmidhuber.
Linear transformers are secretly fast weight programmers.
In *International Conference on Machine Learning* , pp. 9355–9366. PMLR, 2021.
- Shen et al. (2023)
Lingfeng Shen, Aayush Mishra, and Daniel Khashabi.
Do pretrained transformers really learn in-context by gradient
descent?
*arXiv preprint arXiv:2310.08540* , 2023.
- Tarzanagh et al. (2023)
Davoud Ataee Tarzanagh, Yingcong Li, Xuechen Zhang, and Samet Oymak.
Max-margin token selection in attention mechanism.
In *Thirty-seventh Conference on Neural Information Processing
Systems* , 2023.

---

[referencia=ca517c4b4b64d6cc score=0.059]
| Method | Uniform ) |  |  |  |  |  |  |  | Categorical |  | 
|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | {1,3} | {1,3,5} | 
| 1 layer |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 1.768 | 1.639 | 1.396 | 1.175 | 1.015 | 0.907 | 0.841 | 0.806 | 1.007 | 0.819 | 
| Diag | 1.767 | 1.639 | 1.396 | 1.175 | 1.015 | 0.906 | 0.841 | 0.806 | 1.007 | 0.819 | 
| Full | 1.768 | 1.640 | 1.397 | 1.176 | 1.016 | 0.907 | 0.842 | 0.806 | 1.008 | 0.820 | 
| 2 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 0.341 | 0.295 | 0.243 | 0.265 | 0.347 | 0.366 | 0.440 | 0.530 | 0.305 | 0.427 | 
| Diag | 0.265 | 0.214 | 0.173 | 0.188 | 0.219 | 0.242 | 0.254 | 0.259 | 0.201 | 0.246 | 
| Full | 0.264 | 0.215 | 0.173 | 0.188 | 0.220 | 0.245 | 0.259 | 0.263 | 0.202 | 0.276 | 
| 3 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup>

---

[referencia=ca517c4b4b64d6cc score=0.058]
 
| Diag | 1.81e-07 | 0.004 | 0.016 | 0.029 | 0.041 | 0.051 | 0.058 | 0.062 | 0.026 | 0.051 | 
| Full | 1.79e-07 | 0.002 | 0.015 | 0.026 | 0.038 | 0.048 | 0.059 | 0.065 | 0.016 | 0.048 | 
| 6 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 2.37e-10 | 0.009 | 0.066 | 0.161 | 0.265 | 0.344 | 0.454 | 0.530 | 0.222 | 0.422 | 
| Diag | 2.57e-10 | 0.003 | 0.014 | 0.028 | 0.040 | 0.048 | 0.054 | 0.059 | 0.020 | 0.047 | 
| Full | 2.71e-10 | 0.002 | 0.014 | 0.025 | 0.036 | 0.044 | 0.052 | 0.059 | 0.011 | 0.043 | 
| 7 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 2.65e-12 | 0.009 | 0.066 | 0.161 | 0.265 | 0.344 | 0.454 | 0.530 | 0.222 | 0.422 | 
| Diag | 2.50e-12 | 0.002 | 0.014 | 0.027 | 0.040 | 0.047 | 0.052 | 0.059 | 0.018 | 0.046 |

---

[referencia=ca517c4b4b64d6cc score=0.049]
## 4 Linear transformers maintain linear regression model at every layer

While large, nonlinear transformers can model complex relationship, we show that linear transformers are restricted to maintaining a linear regression model based on the input, in the sense that the -th layer output is always a linear function of the input with latent (and possibly nonlinear) coefficients.

###### Theorem 4.1.

Suppose the output of a linear transformer at -th layer is , then there exists matrices , vectors and scalars such that

Note that , and are not linear in the input, but this still poses restrictions on what the linear transformers can do. For example we show that it cannot represent a quadratic function:

###### Theorem 4.2.

Suppose the input to a linear transformer is where and , let the -th layer output be and let and (here is just the first coordinate of ), then when with high probability the cosine similarity of and is at most 0.1.

Theorem 4.1 implies that the output of linear transformer can always be explained as linear combinations of input with latent weights and . The matrices , vectors and numbers are not linear and can in fact be quite complex, which we characterize below:

###### Lemma 4.3.

In the setup of Theorem 4.1, if we let

then one can recursively compute matrices , vectors and numbers for every layer using

with the init. condition .

The updates to the parameters are complicated and nonlinear, allowing linear transformers to implement powerful algorithms, as we will later see in Section 5. In fact, even with diagonal and , they remain flexible. The updates in this case can be further simplified to a more familiar form:

###### Lemma 4.4.

Note that is (proportional to) the gradient of a linear model . This makes the updates similar to a gradient descent with momentum:

Of course, the formula in Lemma 4.4 is still much more complicated with matrices in places of and , and also including a gradient term for the update of .

---

[referencia=ca517c4b4b64d6cc score=0.047]
#### Uniform noise variance.

For the uniform noise variance, Fig. 1 shows that Full and Diag achieve comparable performance across different numbers of layers and different . On the other hand, GD<sup>++</sup> converges to a higher value, closely approaching the performance of the ConstRR baseline.

As grows, linear transformers show a clear advantage over the baselines. With 4 layers, they outperform the closed-form solution AdaRR for and larger. Models with or more layers match or exceed the performance of TunedRR.

The top of Fig. 2 offers a detailed perspective on performance of 7-layer models and the baselines. Here, we computed per-variance profiles across noise variance range from 0 to . We can see that poor performance of GD<sup>++</sup> comes from its inability to estimate well across the full noise variance range. Its performance closely mirrors to ConstRR, suggesting that GD<sup>++</sup> under the hood might also be estimating a single constant variance for all the data.

AdaRR perfectly estimates problems with no noise, but struggles more as noise variance increases. TunedRR slightly improves estimation by incorporating into its tunable parameters, yet its prediction suffers in the mid-range. Full and Diag demonstrate comparable performance across all noise variances. While more research is needed to definitively confirm or deny their equivalence, we believe that these models are actually not identical despite their similar performance.

At the bottom of Fig. 2 we set the noise variance to  and display a per-variance profile for models with varying layers. Two-layer models for Full and Diag behave akin to GD<sup>++</sup>, modeling only a single noise variance in the middle. However, the results quickly improve across the entire noise spectrum for 3 or more layers. In contrast, GD<sup>++</sup> quickly converges to a suboptimal solution.

---

[referencia=ca517c4b4b64d6cc score=0.041]
 
| 3 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 0.019 | 0.021 | 0.071 | 0.161 | 0.259 | 0.344 | 0.454 | 0.530 | 0.222 | 0.422 | 
| Diag | 0.013 | 0.015 | 0.048 | 0.087 | 0.109 | 0.118 | 0.121 | 0.123 | 0.098 | 0.119 | 
| Full | 0.012 | 0.015 | 0.049 | 0.075 | 0.101 | 0.117 | 0.124 | 0.127 | 0.076 | 0.113 | 
| 4 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 9.91e-05 | 0.014 | 0.066 | 0.160 | 0.258 | 0.344 | 0.454 | 0.530 | 0.222 | 0.422 | 
| Diag | 1.19e-04 | 0.006 | 0.024 | 0.041 | 0.050 | 0.059 | 0.065 | 0.073 | 0.043 | 0.062 | 
| Full | 1.63e-04 | 0.005 | 0.021 | 0.038 | 0.052 | 0.065 | 0.068 | 0.076 | 0.032 | 0.061 | 
| 5 layers |  |  |  |  |  |  |  |  |  |  | 
| GD <sup>++</sup> | 1.14e-07 | 0.014 | 0.066 | 0.161 | 0.265 | 0.344 | 0.454 | 0.530 | 0.222 | 0.422 |

---

[referencia=ca517c4b4b64d6cc score=0.033]
# Linear Transformers are Versatile In-Context Learners

###### Abstract

Recent research has demonstrated that transformers, particularly linear attention models, implicitly execute gradient-descent-like algorithms on data provided in-context during their forward inference step. However, their capability in handling more complex problems remains unexplored. In this paper, we prove that each layer of a linear transformer maintains a weight vector for an implicit linear regression problem and can be interpreted as performing a variant of preconditioned gradient descent. We also investigate the use of linear transformers in a challenging scenario where the training data is corrupted with different levels of noise. Remarkably, we demonstrate that for this problem linear transformers discover an intricate and highly effective optimization algorithm, surpassing or matching in performance many reasonable baselines. We analyze this algorithm and show that it is a novel approach incorporating momentum and adaptive rescaling based on noise levels. Our findings show that even linear transformers possess the surprising ability to discover sophisticated optimization strategies.

---

[referencia=ca517c4b4b64d6cc score=0.033]
Furthermore, we demonstrate that linear transformers can be trained to uncover even more powerful and intricate algorithms. We modified the problem formulation to consider mixed linear regression with varying noise levels<sup>1</sup><sup>1</sup>
            1
            
            
            
          We consider a model where each sequence contains data with the same noise level, while different sequences have different noise levels. (inspired by Bai et al., 2023). This is a harder and non-trivial problem with no obvious closed-form solution, since it needs to account for various levels of noise in the input.

Our experiments with two different noise variance distributions (uniform and categorical) demonstrate the remarkable flexibility of linear transformers. Training a linear transformer in these settings leads to an algorithm that outperforms GD<sup>++</sup> as well as various baselines derived from the exact closed-form solution of the ridge regression. We discover that this result holds even when training a linear transformer with diagonal weight matrices.

Through a detailed analysis, we reveal key distinctions from GD<sup>++</sup>, including momentum-like term and adaptive rescaling based on the noise levels.

Our findings contribute to the growing body of research where novel, high-performing algorithms have been directly discovered through the reverse-engineering of transformer weights. This work expands our understanding of the implicit learning capabilities of attention-based models and highlights the remarkable versatility of even simple linear transformers as in-context learners. We demonstrate that transformers have the potential to discover effective algorithms that may advance the state-of-the-art in optimization and machine learning in general.

---

[referencia=ca517c4b4b64d6cc score=0.021]
- Brown et al. (2020)
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell,
et al.
Language models are few-shot learners.
*Advances in neural information processing systems* ,
33:1877–1901, 2020.
- Chan et al. (2022)
Stephanie Chan, Adam Santoro, Andrew Lampinen, Jane Wang, Aaditya Singh, Pierre
Richemond, James McClelland, and Felix Hill.
Data distributional properties drive emergent in-context learning in
transformers.
*Advances in Neural Information Processing Systems* ,
35:18878–18891, 2022.
- Cheng et al. (2023)
Xiang Cheng, Yuxin Chen, and Suvrit Sra.
Transformers implement functional gradient descent to learn
non-linear functions in context.
*arXiv preprint arXiv:2312.06528* , 2023.
- Cherkassky & Ma (2003)
Vladimir Cherkassky and Yunqian Ma.
Comparison of model selection for regression.
*Neural computation* , 15(7):1691–1714,
2003.

---

[referencia=ca517c4b4b64d6cc score=0.020]
- Team et al. (2023)
Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac,
Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al.
Gemini: a family of highly capable multimodal models.
*arXiv preprint arXiv:2312.11805* , 2023.
- Tian et al. (2023a)
Yuandong Tian, Yiping Wang, Beidi Chen, and Simon Du.
Scan and snap: Understanding training dynamics and token composition
in 1-layer transformer.
*arXiv preprint arXiv:2305.16380* , 2023a.
- Tian et al. (2023b)
Yuandong Tian, Yiping Wang, Zhenyu Zhang, Beidi Chen, and Simon Du.
Joma: Demystifying multilayer transformers via joint dynamics of mlp
and attention.
In *NeurIPS 2023 Workshop on Mathematics of Modern Machine
Learning* , 2023b.
- Vaswani et al. (2017)
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin.
Attention is all you need.
*Advances in neural information processing systems* , 30, 2017.
- von Oswald et al. (2023a)
Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento,
Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov.
Transformers learn in-context by gradient descent.
In *International Conference on Machine Learning* , pp. 35151–35174. PMLR, 2023a.

---

[referencia=ca517c4b4b64d6cc score=0.017]
## 6 Experiments

In this section, we investigate the training dynamics of linear transformers when trained with a mixed noise variance problem (7). We evaluate three types of single-head linear transformer models:

- • 
Full. Trains full parameter matrices.
- • 
Diag. Trains diagonal parameter matrices (10).
- • 
GD <sup>++</sup> . An even more restricted diagonal variant defined in (11).

For each experiment, we train each linear transformer modifications with a varying number of layers ( to ) using using Adam optimizer for iterations with a learning rate of and a batch size of . In some cases, especially for a large number of layers, we had to adjust the learning rate to prevent stability issues. We report the best result out of runs with different training seeds. We used in-context examples in dimensions. We evaluated the algorithm using novel sequences. All the experiments were done on a single H100 GPU with 80GB of VRAM. It took on average 4–12 hours to train a single algorithm, however experimenting with different weight decay parameters, better optimizer and learning rate schedule will likely reduce this number dramatically.

We use *adjusted evaluation loss* as our main performance metric. It is calculated by subtracting the oracle loss from the predictor’s loss. The oracle loss is the closed-form solution of the ridge regression loss (5), assuming the noise variance  is known. The adjusted evaluation loss allows for direct model performance comparison across different noise variances. This is important because higher noise significantly degrades the model prediction. Our adjustment does not affect the model’s optimization process, since it only modifies the loss by an additive constant.