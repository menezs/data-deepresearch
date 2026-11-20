[referencia=8a5681d011455a55 score=0.037]
### **6.1 How well can DPO optimize the RLHF objective?** 

The KL-constrained reward maximization objective used in typical RLHF algorithms balances exploitation of reward while restricting the policy from deviating far from the reference policy. Therefore, when comparing algorithms, we must take into account both reward achieved as well as the KL discrepancy; achieving slightly higher reward but with much higher KL is not necessarily desirable. Figure 2 shows the reward-KL frontier for various algorithms in the sentiment setting. We execute multiple training runs for each algorithm, using a different hyperparameter for policy conservativeness in each run (target KL _2 {_ 3 _,_ 6 _,_ 9 _,_ 12 _}_ for PPO, _β 2 {_ 0 _._ 05 _,_ 0 _._ 1 _,_ 1 _,_ 5 _}_ , _↵ 2 {_ 0 _._ 05 _,_ 0 _._ 1 _,_ 0 _._ 5 _,_ 1 _}_ for unlikelihood, random seeds for preferred-FT). This sweep includes 22 runs in total. After each 100 training steps until convergence, we evaluate each policy on a set of test prompts, computing the average reward under the true reward function as well as the average sequence-level KL<sup>3</sup> with the reference policy KL ( _⇡ || ⇡_ ref). We find that DPO produces by far the most efficient frontier, achieving the highest reward while still achieving low KL. This result is particularly notable for multiple reasons. First, DPO and PPO optimize the same objective, but DPO is notably more efficient; 

> 3That is, the sum of the per-timestep KL-divergences. 

8 

DPO’s reward/KL tradeoff strictly dominates PPO. Second, DPO achieves a better frontier than PPO, _even when PPO can access ground truth rewards_ (PPO-GT).

---

[referencia=8a5681d011455a55 score=0.037]
## **6 Experiments** 

In this section, we empirically evaluate DPO’s ability to train policies directly from preferences. First, in a well-controlled text-generation setting, we ask: how efficiently does DPO trade off maximizing reward and minimizing KL-divergence with the reference policy, compared to common preference learning algorithms such as PPO? Next, we evaluate DPO’s performance on larger models and more difficult RLHF tasks, including summarization and dialogue. We find that with almost no tuning of hyperparameters, DPO tends to perform as well or better than strong baselines like RLHF with PPO as well as returning the best of _N_ sampled trajectories under a learned reward function. Before presenting these results, we describe the experimental set-up; additional details are in Appendix C.

---

[referencia=8a5681d011455a55 score=0.036]
where _σ_ is the logistic function. In the context of LMs, the network _rφ_ ( _x, y_ ) is often initialized from the SFT model _⇡_<sup>SFT</sup> ( _y | x_ ) with the addition of a linear layer on top of the final transformer layer that produces a single scalar prediction for the reward value [48]. To ensure a reward function with lower variance, prior works normalize the rewards, such that E _x,y⇠D_ [ _rφ_ ( _x, y_ )] = 0 for all _x_ . 

**RL Fine-Tuning Phase** : During the RL phase, we use the learned reward function to provide feedback to the language model. In particular, we formulate the following optimization problem 



3 

where _β_ is a parameter controlling the deviation from the base reference policy _⇡_ ref, namely the initial SFT model _⇡_<sup>SFT</sup> . In practice, the language model policy _⇡✓_ is also initialized to _⇡_<sup>SFT</sup> . The added constraint is important, as it prevents the model from deviating too far from the distribution on which the reward model is accurate, as well as maintaining the generation diversity and preventing mode-collapse to single high-reward answers. Due to the discrete nature of language generation, this objective is not differentiable and is typically optimized with reinforcement learning. The standard approach [48, 38, 1, 26] has been to construct the reward function _r_ ( _x, y_ ) = _rφ_ ( _x, y_ ) _− β_ (log _⇡✓_ ( _y | x_ ) _−_ log _⇡_ ref( _y | x_ )), and maximize using PPO [37].

---

[referencia=8a5681d011455a55 score=0.033]
**DPO outline.** The general DPO pipeline is as follows: 1) Sample completions _y_ 1 _, y_ 2 _⇠ ⇡_ ref( _· | x_ ) for every prompt _x_ , label with human preferences to construct the offline dataset of preferences _D_ = _{x_<sup>(</sup><sup>_i_)</sup> _, yw_<sup>(</sup><sup>_i_)</sup><sup>_, y_</sup> _l_<sup>)(</sup><sup>_i_)</sup><sup>_}N_</sup> _i_ =1<sup>and 2) optimize the language model</sup><sup>_⇡✓_to minimize</sup><sup>_L_DPOfor the given</sup> _⇡_ ref and _D_ and desired _β_ . In practice, one would like to reuse preference datasets publicly available, rather than generating samples and gathering human preferences. Since the preference datasets are sampled using _⇡_<sup>SFT</sup> , we initialize _⇡_ ref = _⇡_<sup>SFT</sup> whenever available. However, when _⇡_<sup>SFT</sup> is not available, we initialize _⇡_ ref by maximizing likelihood of preferred completions ( _x, yw_ ), that is, _⇡_ ref = arg max _⇡_ E _x,yw⇠D_ [log _⇡_ ( _yw | x_ )]. This procedure helps mitigate the distribution shift between the true reference distribution which is unavailable, and _⇡_ ref used by DPO. Further details related to the implementation and hyperparameters can be found in Appendix B.

---

[referencia=8a5681d011455a55 score=0.007]
### **5.2 Instability of Actor-Critic Algorithms** 

We can also use our framework to diagnose instabilities with standard actor-critic algorithms used for the RLHF, such as PPO. We follow the RLHF pipeline and focus on the RL fine-tuning step outlined in Section 3. We can draw connections to the control as inference framework [20] for the constrained RL problem outlined in 3. We assume a parameterized model _⇡✓_ ( _y | x_ ) and minimize DKL[ _⇡✓_ ( _y|x_ ) _|| ⇡_<sup>_⇤_</sup> ( _y | x_ )] where _⇡_<sup>_⇤_</sup> is the optimal policy from Eq. 7 induced by the reward function _rφ_ ( _y, x_ ). With some algebra this leads to the optimization objective: 



This is the same objective optimized in prior works [48, 38, 1, 26] using the DPO-equivalent reward for the reward class of _rφ_ . In this setting, we can interpret the normalization term in _f_ ( _rφ, ⇡_ ref _, β_ ) as the soft value function of the reference policy _⇡_ ref. While this term does not affect the optimal solution, without it, the policy gradient of the objective could have high variance, making learning unstable. We can accommodate for the normalization term using a learned value function, but that can also be difficult to optimize. Alternatively, prior works have normalized rewards using a human completion baseline, essentially a single sample Monte-Carlo estimate of the normalizing term. In contrast the DPO reparameterization yields a reward function that does not require any baselines. 

6 



Figure 2: **Left.** The frontier of expected reward vs KL to the reference policy. DPO provides the highest expected reward for all KL values, demonstrating the quality of the optimization. **Right.** TL;DR summarization win rates vs. human-written summaries, using GPT-4 as evaluator. DPO exceeds PPO’s best-case performance on summarization, while being more robust to changes in the sampling temperature.

---

[referencia=8a5681d011455a55 score=0.006]
**Methods.** In addition to DPO, we evaluate several existing approaches to training language models to adhere to human preferences. Most simply, we explore zero-shot prompting with **GPT-J** [43] in the summarization task and 2-shot prompting with **Pythia-2.8B** [3] in the dialogue task. In addition, we evaluate the **SFT** model as well as **Preferred-FT** , which is a model fine-tuned with supervised learning on the chosen completion _yw_ from either the SFT model (in controlled sentiment and summarization) or a generic LM (in single-turn dialogue). Another pseudo-supervised method is **Unlikelihood** , which simply optimizes the policy to maximize the probability assigned to _yw_ and _minimize_ the probability assigned to _yl_ ; we use an optional coefficient _↵ 2_ [0 _,_ 1] on the ‘unlikelihood’ term. We also consider **PPO** [37] using a reward function learned from the preference data and **PPO-GT** , which is an oracle that learns from the ground truth reward function available in the controlled sentiment setting. In our sentiment experiments, we use two implementations of PPO-GT, one of-the-shelf version [42] as well as a modified version that normalizes rewards and further tunes hyperparameters to improve performance (we also use these modifications when running ‘normal’ PPO with learned rewards). Finally, we consider the **Best of** _N_ baseline, sampling _N_ responses from the SFT model (or Preferred-FT in dialogue) and returning the highest-scoring response according to a reward function learned from the preference dataset. This high-performing method decouples the quality of the reward model from the PPO optimization, but is computationally impractical even for moderate _N_ as it requires sampling _N_ completions for every query at test time.

---

[referencia=8a5681d011455a55 score=0.005]
# **Direct Preference Optimization: Your Language Model is Secretly a Reward Model** 

**Rafael Rafailov**<sup>_⇤†_</sup> **Archit Sharma**<sup>_⇤†_</sup> **Eric Mitchell**<sup>_⇤†_</sup> **Stefano Ermon**<sup>_†‡_</sup> **Christopher D. Manning**<sup>_†_</sup> **Chelsea Finn**<sup>_†_</sup> 

> _†_ Stanford University _‡_ CZ Biohub `{rafailov,architsh,eric.mitchell}@cs.stanford.edu` 

## **Abstract** 

While large-scale unsupervised language models (LMs) learn broad world knowledge and some reasoning skills, achieving precise control of their behavior is difficult due to the completely unsupervised nature of their training. Existing methods for gaining such steerability collect human labels of the relative quality of model generations and fine-tune the unsupervised LM to align with these preferences, often with reinforcement learning from human feedback (RLHF). However, RLHF is a complex and often unstable procedure, first fitting a reward model that reflects the human preferences, and then fine-tuning the large unsupervised LM using reinforcement learning to maximize this estimated reward without drifting too far from the original model. In this paper, we leverage a mapping between reward functions and optimal policies to show that this constrained reward maximization problem can be _optimized exactly_ with a single stage of policy training, essentially solving a classification problem on the human preference data. The resulting algorithm, which we call _Direct Preference Optimization_ (DPO), is stable, performant, and computationally lightweight, eliminating the need for fitting a reward model, sampling from the LM during fine-tuning, or performing significant hyperparameter tuning. Our experiments show that DPO can fine-tune LMs to align with human preferences as well as or better than existing methods. Notably, fine-tuning with DPO exceeds RLHF’s ability to control sentiment of generations and improves response quality in summarization and single-turn dialogue while being substantially simpler to implement and train.

---

[referencia=8a5681d011455a55 score=0.004]
### **6.2 Can DPO scale to real preference datasets?** 

For summarization, automatic evaluation metrics such as ROUGE can be poorly correlated with human preferences [38], and prior work has found that fine-tuning LMs using PPO on human preferences to provide more effective summaries. We evaluate different methods by sampling completions on the test split of TL;DR summarization dataset, and computing the average win rate against reference completions in the test set. The completions for all methods are sampled at temperatures varying from 0.0 to 1.0, and the win rates are shown in Figure 2 (right). DPO, PPO and Preferred-FT all fine-tune the same GPT-J SFT model<sup>4</sup> . We find that DPO has a win rate of approximately 61% at a temperature of 0.0, exceeding the performance of PPO at 57% at its optimal sampling temperature of 0.0. DPO also achieves a higher maximum win rate compared to the best of _N_ baseline. We note that we did not meaningfully tune DPO’s _β_ hyperparameter, so these results may underestimate DPO’s potential. Moreover, we find DPO to be much more robust to the sampling temperature than PPO, the performance of which can degrade to that of the base GPT-J model at high temperatures. Preferred-FT does not improve significantly over the SFT model. We also compare DPO and PPO head-to-head in human evaluations in Section 6.4, where DPO samples at temperature 0.25 were preferred 58% times over PPO samples at temperature 0.

---

[referencia=8a5681d011455a55 score=0.004]
**Evaluation.** Our experiments use two different approaches to evaluation. In order to analyze the effectiveness of each algorithm in optimizing the constrained reward maximization objective, in the controlled sentiment generation setting we evaluate each algorithm by its frontier of achieved reward and KL-divergence from the reference policy; this frontier is computable because we have acccess to the ground-truth reward function (a sentiment classifier). However, in the real world, the ground truth reward function is not known; therefore, we evaluate algorithms with their _win rate_ against a baseline policy, using GPT-4 as a proxy for human evaluation of summary quality and response helpfulness in the summarization and single-turn dialogue settings, respectively. For summarization, we use reference summaries in the test set as the baseline; for dialogue, we use the preferred response in the 

> 2 `https://huggingface.co/CarperAI/openai_summarize_tldr_sft` 

7 



Figure 3: **Left.** Win rates computed by GPT-4 for Anthropic-HH one-step dialogue; DPO is the only method that improves over chosen summaries in the Anthropic-HH test set. **Right.** Win rates for different sampling temperatures over the course of training. DPO’s improvement over the dataset labels is fairly stable over the course of training for different sampling temperatures. 

test dataset as the baseline. While existing studies suggest LMs can be better automated evaluators than existing metrics [10], we conduct a human study to justify our usage of GPT-4 for evaluation in Sec. 6.4. We find GPT-4 judgments correlate strongly with humans, with human agreement with GPT-4 typically similar or higher than inter-human annotator agreement.

---

[referencia=8a5681d011455a55 score=0.003]
## **4 Direct Preference Optimization** 

Motivated by the challenges of applying reinforcement learning algorithms on large-scale problems such as fine-tuning language models, our goal is to derive a simple approach for policy optimization using preferences directly. Unlike prior RLHF methods, which learn a reward and then optimize it via RL, our approach bypasses the reward modeling step and directly optimizes a language model using preference data. As we will describe next in detail, our key insight is to leverage an analytical mapping from reward functions to optimal policies, which enables us to transform a loss function over reward functions into a loss function over policies. This change-of-variables approach allows us to skip the explicit reward modeling step, while still optimizing under existing models of human preferences, such as the Bradley-Terry model. In essence, the policy network represents both the language model and the reward. 

**Deriving the DPO objective.** We start with the same RL objective as prior work, Eq. 3, under a general reward function _r_ . Following prior work [29, 28, 17, 15], it is straightforward to show that the optimal solution to the KL-constrained reward maximization objective in Eq. 3 takes the form: 



where _Z_ ( _x_ ) =<sup>P</sup> _y_<sup>_⇡_ref(</sup><sup>_y|x_) exp</sup> ⇣ _β_ <u>1</u><sup>_r_(</sup><sup>_x, y_)</sup> ⌘ is the partition function. See Appendix A.1 for a complete derivation. Even if we use the MLE estimate _rφ_ of the ground-truth reward function _r_<sup>_⇤_</sup> , it is still expensive to estimate the partition function _Z_ ( _x_ ) [17, 15], which makes this representation hard to utilize in practice. However, we can rearrange Eq. 4 to express the reward function in terms of its corresponding optimal policy _⇡r_ , the reference policy _⇡_ ref, and the unknown partition function _Z_ ( _·_ ). Specifically, we first take the logarithm of both sides of Eq. 4 and then with some algebra we obtain:

---

[referencia=8a5681d011455a55 score=0.003]
We can apply this reparameterization to the ground-truth reward _r_<sup>_⇤_</sup> and corresponding optimal model _⇡_<sup>_⇤_</sup> . Fortunately, the Bradley-Terry model depends only on the difference of rewards between two completions, i.e., _p_<sup>_⇤_</sup> ( _y_ 1 _≻ y_ 2 _| x_ ) = _σ_ ( _r_<sup>_⇤_</sup> ( _x, y_ 1) _− r_<sup>_⇤_</sup> ( _x, y_ 2)). Substituting the reparameterization in Eq. 5 for _r_<sup>_⇤_</sup> ( _x, y_ ) into the preference model Eq. 1, the partition function cancels, and we can express the human preference probability in terms of only the optimal policy _⇡_<sup>_⇤_</sup> and reference policy _⇡_ ref. Thus, the optimal RLHF policy _⇡_<sup>_⇤_</sup> under the Bradley-Terry model satisfies the preference model: 



The derivation is in Appendix A.2. While Eq. 6 uses the Bradley-Terry model, we can similarly derive expressions under the more general Plackett-Luce models [30, 21], shown in Appendix A.3. 

Now that we have the probability of human preference data in terms of the optimal policy rather than the reward model, we can formulate a maximum likelihood objective for a parametrized policy _⇡✓_ . Analogous to the reward modeling approach (i.e. Eq. 2), our policy objective becomes: 



This way, we simultaneously bypass the explicit reward modeling step while also avoiding the need to perform reinforcement learning optimization. Moreover, since our procedure is equivalent to fitting 

4 

a reparametrized Bradley-Terry model, it enjoys certain theoretical properties, such as consistencies under suitable assumption of the preference data distribution [4]. In Section 5, we further discuss theoretical properties of DPO in relation to other works.

---

[referencia=8a5681d011455a55 score=0.002]
Table 2: Comparing human and GPT-4 win rates and per-judgment agreement on TL;DR summarization samples. **Humans agree with GPT-4 about as much as they agree with each other.** Each experiment compares a summary from the stated method with a summary from PPO with temperature 0. 

## **7 Discussion** 

Learning from preferences is a powerful, scalable framework for training capable, aligned language models. We have introduced DPO, a simple training paradigm for training language models from preferences without reinforcement learning. Rather than coercing the preference learning problem into a standard RL setting in order to use off-the-shelf RL algorithms, DPO identifies a mapping between language model policies and reward functions that enables training a language model to satisfy human preferences _directly_ , with a simple cross-entropy loss, without reinforcement learning or loss of generality. With virtually no tuning of hyperparameters, DPO performs similarly or better than existing RLHF algorithms, including those based on PPO; DPO thus meaningfully reduces the barrier to training more language models from human preferences. 

**Limitations & Future Work.** Our results raise several important questions for future work. How does the DPO policy generalize out of distribution, compared with learning from an explicit reward function? Our initial results suggest that DPO policies can generalize similarly to PPO-based models, but more comprehensive study is needed. For example, can training with self-labeling from the DPO policy similarly make effective use of unlabeled prompts? On another front, how does reward over-optimization manifest in the direct preference optimization setting, and is the slight decrease in performance in Figure 3-right an instance of it? Additionally, while we evaluate models up to 6B parameters, exploration of scaling DPO to state-of-the-art models orders of magnitude larger is an exciting direction for future work. Regarding evaluations, we find that the win rates computed by GPT-4 are impacted by the prompt; future work may study the best way to elicit high-quality judgments from automated systems. Finally, many possible applications of DPO exist beyond training language models from human preferences, including training generative models in other modalities.

---

[referencia=8a5681d011455a55 score=0.001]
- [7] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33:1877–1901, 2020. 

- [8] S. Bubeck, V. Chandrasekaran, R. Eldan, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T. Lee, Y. Li, S. Lundberg, H. Nori, H. Palangi, M. T. Ribeiro, and Y. Zhang. Sparks of artificial general intelligence: Early experiments with GPT-4, 2023. arXiv preprint arXiv:2303.12712. 

- [9] R. Busa-Fekete, B. Szörényi, P. Weng, W. Cheng, and E. Hüllermeier. Preference-based reinforcement learning: evolutionary direct policy search using a preference-based racing algorithm. _Machine Learning_ , 97(3):327–351, July 2014. doi: 10.1007/s10994-014-5458-8. URL `https://doi.org/10.1007/s10994-014-5458-8` . 

- [10] Y. Chen, R. Wang, H. Jiang, S. Shi, and R.-L. Xu. Exploring the use of large language models for reference-free text quality evaluation: A preliminary empirical study. _ArXiv_ , abs/2304.00723, 2023. 

- [11] A. Chowdhery, S. Narang, J. Devlin, M. Bosma, G. Mishra, A. Roberts, P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, et al. Palm: Scaling language modeling with pathways. _arXiv preprint arXiv:2204.02311_ , 2022.

---

[referencia=8a5681d011455a55 score=0.001]
The proofs are straightforward and we defer them to Appendix A.5. The first lemma is a well-known under-specification issue with the Plackett-Luce family of models [30]. Due to this under-specification, 

5 

we usually have to impose additional identifiability constraints to achieve any guarantees on the MLE estimates from Eq. 2 [4]. The second lemma states that all reward functions from the same class yield the same optimal policy, hence for our final objective, we are only interested in recovering an arbitrary reward function from the optimal class. We prove the following Theorem in Appendix A.6: 

**Theorem 1.** _Under mild assumptions, all reward classes consistent with the Plackett-Luce (and Bradley-Terry in particular) models can be represented with the reparameterization r_ ( _x, y_ ) = _β_ log _⇡⇡ref_ <u>((</u> _<u>yy|x|x</u>_ <u>))</u><sup>_for some model ⇡_(</sup><sup>_y| x_)</sup><sup>_and a given reference model ⇡ref_(</sup><sup>_y| x_)</sup><sup>_._</sup> 

_Proof Sketch._ Consider any reward function _r_ ( _x, y_ ), which induces a corresponding optimal model _⇡r_ ( _y | x_ ), specified by Eq. 4. We will show that a reward function from the equivalence class of _r_ can be represented using the reparameterization given above. We define the projection _f_ as

---

[referencia=8a5681d011455a55 score=0.001]
The operator _f_ simply normalizes the reward function with the logarithm of the partition function of _⇡r_ . Since the added normalization term is only a function of the prefix _x_ , _f_ ( _r_ ; _⇡_ ref _, β_ )( _x, y_ ) is a reward function in the equivalence class of _r_ ( _x, y_ ). Finally, replacing _r_ with the RHS of Eq. 5 (which holds for any reward function), we have _f_ ( _r_ ; _⇡_ ref _, β_ )( _x, y_ ) = _β_ log _⇡_<sup>_⇡_</sup> ref<sup>_r_</sup><sup><u>(</u></sup> (<sup>_<u>y</u>_</sup> _y_<sup>_<u>|</u>_</sup> _|_<sup>_x_</sup> _x_<sup><u>)</u></sup> )<sup>.That is, the projection</sup> _f_ produces a member of the equivalence class of _r_ with the desired form, and we do not lose any generality in our reward model from the proposed reparameterization. 

We can alternatively view Theorem 1 as specifying exactly which reward function within each equivalence class the DPO reparameterization selects, that is, the reward function satisfying: 



i.e., _⇡_ ( _y | x_ ) is a valid distribution (probabilities are positive and sum to 1). However, following Eq. 4, we can see that Eq. 9 is the partition function of the optimal policy induced by the reward function _r_ ( _x, y_ ). The key insight of the DPO algorithm is that we can impose certain constraints on the under-constrained Plackett-Luce (and Bradley-Terry in particular) family of preference models, such that we preserve the class of representable reward models, but explicitly make the optimal policy in Eq. 4 analytically tractable for all prompts _x_ .

---

[referencia=8a5681d011455a55 score=0.001]
a reparametrized Bradley-Terry model, it enjoys certain theoretical properties, such as consistencies under suitable assumption of the preference data distribution [4]. In Section 5, we further discuss theoretical properties of DPO in relation to other works. 

**What does the DPO update do?** For a mechanistic understanding of DPO, it is useful to analyze the gradient of the loss function _L_ DPO. The gradient with respect to the parameters _✓_ can be written as: 



where ˆ _r✓_ ( _x, y_ ) = _β_ log _⇡_<sup>_⇡_</sup> ref<sup>_<u>✓</u>_</sup><sup><u>(</u></sup> (<sup>_<u>y</u>_</sup> _y_<sup>_<u>|</u>_</sup> _|_<sup>_x_</sup> _x_<sup><u>)</u></sup> )<sup>is the reward implicitly defined by the language model</sup><sup>_⇡✓_and refer-</sup> ence model _⇡_ ref (more in Section 5). Intuitively, the gradient of the loss function _L_ DPO increases the likelihood of the preferred completions _yw_ and decreases the likelihood of dispreferred completions _yl_ . Importantly, the examples are weighed by how much higher the implicit reward model ˆ _r✓_ rates the dispreferred completions, scaled by _β_ , i.e, how incorrectly the implicit reward model orders the completions, accounting for the strength of the KL constraint. Our experiments suggest the importance of this weighting, as a naïve version of this method without the weighting coefficient can cause the language model to degenerate (Appendix Table 3).

---

[referencia=8a5681d011455a55 score=0.001]
### **5.1 Your Language Model Is Secretly a Reward Model** 

DPO is able to bypass both explicit reward estimation and RL to learn the policy using a single maximum likelihood objective. However, the optimization objective Eq. 5 is equivalent to a BradleyTerry model with a reward function _r_<sup>_⇤_</sup> ( _x, y_ ) = _β_ log _⇡_<sup>_⇡_</sup> ref _<u>✓</u>_<sup>_⇤_</sup><sup><u>(</u></sup> (<sup>_<u>y</u>_</sup> _y_<sup>_<u>|</u>_</sup> _|_<sup>_x_</sup> _x_<sup><u>)</u></sup> )<sup>and we optimize our parametric model</sup> _⇡✓_ , equivalently to the reward model optimization in Eq. 2 under the this change of variables. In this section we will build the theory behind this reparameterization, show that it does not constrain the class of learned reward models, and allows for the exact recovery of the optimal policy. We begin with by defining an equivalence relation between reward functions. 

**Definition 1.** _We say that two reward functions r_ ( _x, y_ ) _and r_<sup>_0_</sup> ( _x, y_ ) _are equivalent iff r_ ( _x, y_ ) _− r_<sup>_0_</sup> ( _x, y_ ) = _f_ ( _x_ ) _for some function f ._ 

It is easy to see that this is indeed an equivalence relation, which partitions the set of reward functions into classes. We can state the following two lemmas: 

**Lemma 1.** _Under the Plackett-Luce, and in particular the Bradley-Terry, preference framework, two reward functions from the same class induce the same preference distribution._ 

**Lemma 2.** _Two reward functions from the same equivalence class induce the same optimal policy under the constrained RL problem._ 

The proofs are straightforward and we defer them to Appendix A.5. The first lemma is a well-known under-specification issue with the Plackett-Luce family of models [30]. Due to this under-specification, 

5

---

[referencia=8a5681d011455a55 score=0.001]
**Tasks.** Our experiments explore three different open-ended text generation tasks. For all experiments, _N_ algorithms learn a policy from a dataset of preferences _D_ = � _x_<sup>(</sup><sup>_i_)</sup> _, yw_<sup>(</sup><sup>_i_)</sup><sup>_, y_</sup> _l_<sup>(</sup><sup>_i_)</sup> _i_ =1<sup>.In</sup><sup>**controlled**</sup> **sentiment generation** , _x_ is a prefix of a movie review from the IMDb dataset [22], and the policy must generate _y_ with positive sentiment. In order to perform a controlled evaluation, for this experiment we _generate_ preference pairs over generations using a pre-trained sentiment classifier, where _p_ (positive _| x, yw_ ) _> p_ (positive _| x, yl_ ). For SFT, we fine-tune GPT-2-large until convergence on reviews from the train split of the IMDB dataset (further details in App C.1). In **summarization** , _x_ is a forum post from Reddit; the policy must generate a summary _y_ of the main points in the post. Following prior work, we use the Reddit TL;DR summarization dataset [41] along with human preferences gathered by Stiennon et al.. We use an SFT model fine-tuned on human-written forum post summaries<sup>2</sup> with the TRLX [42] framework for RLHF. The human preference dataset was gathered by Stiennon et al. on samples from a different, but similarly-trained, SFT model. Finally, in **single-turn dialogue** , _x_ is a human query, which may be anything from a question about astrophysics to a request for relationship advice. A policy must produce an engaging and helpful response _y_ to a user’s query; we use the Anthropic Helpful and Harmless dialogue dataset [1], containing 170k dialogues between a human and an automated assistant. Each transcript ends with a pair of responses generated by a large (although unknown) language model along with a preference label denoting the human-preferred response. In this setting, no pre-trained SFT model is available; we therefore fine-tune an off-the-shelf language model on only the preferred completions to form the SFT model.

---

[referencia=8a5681d011455a55 score=0.001]
- [41] M. Völske, M. Potthast, S. Syed, and B. Stein. TL;DR: Mining Reddit to learn automatic summarization. In _Proceedings of the Workshop on New Frontiers in Summarization_ , pages 59–63, Copenhagen, Denmark, Sept. 2017. Association for Computational Linguistics. doi: 10.18653/v1/W17-4508. URL `https://aclanthology.org/W17-4508` . 

- [42] L. von Werra, J. Tow, reciprocated, S. Matiana, A. Havrilla, cat state, L. Castricato, Alan, D. V. Phung, A. Thakur, A. Bukhtiyarov, aaronrmm, F. Milo, Daniel, D. King, D. Shin, E. Kim, J. Wei, M. Romero, N. Pochinkov, O. Sanseviero, R. Adithyan, S. Siu, T. Simonini, V. Blagojevic, X. Song, Z. Witten, alexandremuzio, and crumb. CarperAI/trlx: v0.6.0: LLaMa (Alpaca), Benchmark Util, T5 ILQL, Tests, Mar. 2023. URL `https://doi.org/10.5281/zenodo. 7790115` . 

- [43] B. Wang and A. Komatsuzaki. GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model. `https://github.com/kingoflolz/mesh-transformer-jax` , May 2021. 

- [44] R. J. Williams. Simple statistical gradient-following algorithms for connectionist reinforcement learning. _Mach. Learn._ , 8(3–4):229–256, may 1992. ISSN 0885-6125. doi: 10.1007/BF00992696. URL `https://doi.org/10.1007/BF00992696` .

---

[referencia=8a5681d011455a55 score=0.001]
- [28] X. B. Peng, A. Kumar, G. Zhang, and S. Levine. Advantage-weighted regression: Simple and scalable off-policy reinforcement learning. _arXiv preprint arXiv:1910.00177_ , 2019. 

- [29] J. Peters and S. Schaal. Reinforcement learning by reward-weighted regression for operational space control. In _Proceedings of the 24th international conference on Machine learning_ , pages 745–750, 2007. 

- [30] R. L. Plackett. The analysis of permutations. _Journal of the Royal Statistical Society. Series C (Applied Statistics)_ , 24(2):193–202, 1975. doi: https://doi.org/10.2307/2346567. 

- [31] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are unsupervised multitask learners, 2019. Ms., OpenAI. 

- [32] R. Ramamurthy, P. Ammanabrolu, K. Brantley, J. Hessel, R. Sifa, C. Bauckhage, H. Hajishirzi, and Y. Choi. Is reinforcement learning (not) for natural language processing: Benchmarks, baselines, and building blocks for natural language policy optimization. In _The Eleventh International Conference on Learning Representations_ , 2023. URL `https://openreview. net/forum?id=8aHzds2uUyB` . 

- [33] M. Ranzato, S. Chopra, M. Auli, and W. Zaremba. Sequence level training with recurrent neural networks. _CoRR_ , abs/1511.06732, 2015. 

- [34] D. Sadigh, A. D. Dragan, S. Sastry, and S. A. Seshia. Active preference-based learning of reward functions. In _Robotics: Science and Systems (RSS)_ , 2017.