[referencia=b9e232df2cb9a34c score=0.969]
# The Evolution of Statistical Induction Heads: 

In-Context Learning Markov Chains

###### Abstract

Large language models have the ability to generate text that mimics patterns in their inputs. We introduce a simple Markov Chain sequence modeling task in order to study how this in-context learning (ICL) capability emerges. In our setting, each example is sampled from a Markov chain drawn from a prior distribution over Markov chains. Transformers trained on this task form *statistical induction heads* which compute accurate next-token probabilities given the bigram statistics of the context. During the course of training, models pass through multiple phases: after an initial stage in which predictions are uniform, they learn to sub-optimally predict using in-context single-token statistics (unigrams); then, there is a rapid phase transition to the correct in-context bigram solution. We conduct an empirical and theoretical investigation of this multi-phase process, showing how successful learning results from the interaction between the transformer’s layers, and uncovering evidence that the presence of the simpler unigram solution may delay formation of the final bigram solution. We examine how learning is affected by varying the prior distribution over Markov chains, and consider the generalization of our in-context learning of Markov chains (ICL-MC) task to -grams for .

---

[referencia=b9e232df2cb9a34c score=0.962]
### 1.1 Related Work

#### In-context Learning.

Recently, many works have focused on understanding how ICL emerges in language models. In (Chan et al.,, 2022), the authors discuss how properties of the data distribution promote ICL, with a focus on empirical observations.
Xie et al., (2022) studies a data model similar to ours, demonstrating that language models trained on Hidden Markov Models (HMMs) can learn in-context HMMs not found in the training data.
Abernethy et al., (2023) study the ability of transformers to segment the context into pairs of examples and labels and provide learning guarantees when the labeling is of the form of a sparse function.
The work of Bietti et al., (2023) studies the dynamics of training transformers on a task that is reminiscent of our Markov chain setting but has additional complexities. Instead of drawing a fresh Markov chain for each sequence, in their task all sequences are sampled from the same Markov chain; after certain ‘trigger’ tokens, the following ‘output’ token is chosen deterministically within a sequence. Thus, successful prediction requires incorporating both global bigram statistics and in-context deterministic bigram copying, unlike in our setting where the patterns computed by *statistical* induction heads are necessary and sufficient. As in our work, they identify multiple distinct stages of training and show how multiple top-down gradient steps lead to a solution.

Other works observe that ICL is possible due to the ability of transformers to implement gradient descent as a “meta learning” algorithm, and show some evidence that this indeed corresponds to how transformers learn in-context (Von Oswald et al.,, 2023; Dai et al.,, 2022). The work of Li et al., (2023) presents a theoretical framework for studying ICL, providing some risk bounds on ICL of supervised learning algorithms. Guo et al., (2023) construct synthetic in-context learning problems with a compositional structure, studying the representation capacity of transformers to learn these problems in-context. In (Hendel et al.,, 2023), the authors demonstrate that transformers learn to represent task vectors, providing a mechanistic analysis of ICL in LLMs. Kirsch et al., (2022) view ICL as a broad meta-learning paradigm, and observe that transformers meta-trained on real image classification tasks undergo similar phase transitions as the ones we observe in this work.

---

[referencia=b9e232df2cb9a34c score=0.919]
### 2.3 Architectures: Transformers and Simplifications

We are mainly interested in investigating how transformers (Vaswani et al.,, 2017) can succeed in in-context learning this task. We focus on attention-only transformers with 2 layers with causal masking which is a popular architecture for language modeling. Given an input sequence , the output of an -layer attention-only transformer is:

|  |  |  | (4) | 

Where is a linear projection, is an embedding of , and is masked self attention with relative position embeddings (Shaw et al.,, 2018), which is parameterized by :

|  |  |  | (5) | 

During training, we minimize this loss:

|  |  |  | (6) | 

where denotes the parameters of the model and is a loss function such as the cross entropy or margin loss. For our experiments, we run on the standard cross-entropy loss. For our theoretical results, we analyze training under the margin loss that is a generalization of the hinge loss to the case of more than 2 classes: for hyperparameter ,

|  |  |  | (7) | 

We now show how a two-layer transformer can represent the optimal bigrams solution.

###### Proposition 2.2 (Transformer Construction).

A single-head two layer attention-only transformer can find the bigram statistics in the in-context learning markov chain task.

###### Proof.

Set the internal dimension , and choose to be one-hot embeddings, that is, , where is the Kronecker delta. We will call the parameters of attention layer , . Let

The attention of this first layer will focus on the previous token, and for all , . Then, as approaches infinity, the first attention layer at index approaches .

The second layer attention counts the bigrams of past tokens, as  approaches infinity, at index  the attention is (a constant times) a count of how many positions ,  and . Letting , the output approaches the probabilities given by empirical bigram statistics.<sup>1</sup><sup>1</sup>
                  1
                  
                  
                  
                  
                  
                  
                  
                Technically, the output of this is probabilities, not log probabilities as generally cross-entropy loss assumes. This can be approximated linearly by setting
 to change the output from  to . In practice, this approximation can achieve close to Bayes optimal loss.
∎

---

[referencia=b9e232df2cb9a34c score=0.873]
### 3.3 Beyond Bigrams: -gram Statistics

We also investigated the performance of transformers on learning in-context -grams for ; in particular, 3-grams. We trained attention-only transformers with three heads in each layer by minimizing the in-context cross entropy loss with the Adam optimizer. As can be seen in Figure 5 (left), the model eventually converges to the Bayes optimal solution. Interestingly, as in the case of Markov Chains, the model displays a “hierarchical learning" behavior characterized by long plateaus and sudden drops. In this setup, the different strategies correspond to unigrams, bigrams and trigrams, respectively. This is presented clearly on the right of Figure 5, where we plot the similarity of the model with the different strategies and it exhibits the same clear pattern as in the case of . Single attention headed models could not achieve better performance than bigrams. We leave a more thorough investigation for future work.

## 4 Conclusion and Discussion

In this work, we have introduced a simple learning problem which serves as a controlled setting for understanding in-context learning and the emergence of (statistical) induction heads. Induction heads are a common motif in LLMs, which suggests the natural direction of exploring to what extent our various findings extend to natural language training data. Notably, on the way to solving the ICL-MC task, networks pass through a sequence of well-characterized discrete incomplete solutions. Simple but incomplete solutions may be commonplace in language modeling and other rich learning settings; for any such solution, one can ask to what extent its presence speeds up or slows down the formation of more complex circuits with higher accuracy.

#### Acknowledgments.

BE acknowledges funding from the ONR under award N00014-22-1-2377 and the NSF under award IIS 2229881. NT acknowledges support through the National Science Foundation under NSF Award 1922658. NT would like to thank Boaz Barak, Cengiz Pehlevan and the whole ML Foundations Group at Harvard for their hospitality during Fall 2023 when most of this work was done.

---

[referencia=b9e232df2cb9a34c score=0.852]
### 2.2 Potential Strategies to Solve ICL-MC

We adopt the Bayesian interpretation of in-context learning (Xie et al.,, 2022), in which a prior distribution is given by the training data, and, at test time, the model updates this prior given the in-context sequence. In this framework, we focus on two strategies for Bayesian inference: a *unigram* strategy which assumes tokens in each sequence are i.i.d. samples, and the *bigram* strategy which correctly takes into account dependencies among adjacent tokens.

#### 1st strategy: Unigrams

Since we let the Markov chain reach its stationary distribution (which exists a.s.), the optimal strategy across unigrams is just to count frequency of states and form a posterior belief about the stationary distribution. Unfortunately, the stationary distribution of this random Markov chain does not admit a simple analytical characterization when there is a finite number of states, but it can be estimated approximately. At the limit of , the stationary distribution converges to the uniform distribution (Bordenave et al.,, 2008).

#### 2nd strategy: Bigrams

For any pair of states and , let be probability of transitioning from to . On each sample , we can focus on the transitions from the -th state, which follow a categorical distribution with probabilities equal to . If we observe the in-context empirical counts of the transitions, then is given by:

|  |  |  | (1) | 

where, recall, are the Dirichlet concentration parameters of the prior. Hence, each has a (marginal) distribution that is actually a Beta distribution:

|  |  |  | (2) | 

where is the total number of observed transitions from state . As such, our best (point) estimate for each state is given by:

|  |  |  | (3) | 

For the uniform Dirichlet, , it is .

###### Remark 2.1.

The bigram strategy implicitly assumes that the first token is sampled uniformly, as opposed to being sampled from the stationary distribution (which is used in our experiments and theoretical results). As the context length grows, the bigram statistics approach the Bayes optimal solution either way and this difference becomes negligible.

---

[referencia=b9e232df2cb9a34c score=0.744]
- Li et al., (2023) Li, Y., Ildiz, M. E., Papailiopoulos, D., and Oymak, S. (2023). Transformers as algorithms: Generalization and stability in in-context learning. In International Conference on Machine Learning, pages 19565–19594. PMLR.
- Lyu et al., (2023) Lyu, K., Jin, J., Li, Z., Du, S. S., Lee, J. D., and Hu, W. (2023). Dichotomy of early and late phase implicit biases can provably induce grokking. CoRR, abs/2311.18817.
- Makkuva et al., (2024) Makkuva, A. V., Bondaschi, M., Girish, A., Nagle, A., Jaggi, M., Kim, H., and Gastpar, M. (2024). Attention with markov: A framework for principled analysis of transformers via markov chains. CoRR, abs/2402.04161.
- Merrill et al., (2023) Merrill, W., Tsilivis, N., and Shukla, A. (2023). A tale of two circuits: Grokking as competition of sparse and dense subnetworks. CoRR, abs/2303.11873.
- Olsson et al., (2022) Olsson, C., Elhage, N., Nanda, N., Joseph, N., DasSarma, N., Henighan, T., Mann, B., Askell, A., Bai, Y., Chen, A., Conerly, T., Drain, D., Ganguli, D., Hatfield-Dodds, Z., Hernandez, D., Johnston, S., Jones, A., Kernion, J., Lovitt, L., Ndousse, K., Amodei, D., Brown, T., Clark, J., Kaplan, J., McCandlish, S., and Olah, C. (2022). In-context learning and induction heads. Transformer Circuits Thread. https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html.

---

[referencia=b9e232df2cb9a34c score=0.702]
### 3.1 Transformers in-context learn Markov Chains hierarchically

As can be seen in Figure 3, all the models converge near the Bayesian optimal solution, suggesting that they learn to implement the bigram strategy. Curiously, however, the learning seems to be happening in stages; there is an initial rapid drop and the model quickly finds a better than random solution. Afterwards, there is a long period of only slight improvement before a second rapid drop brings the model close to the Bayes optimal loss. We observe that training a 1-layer transformer fails to undergo a phase transition or converge to the right solution - see Figure 13.

Interestingly, as can be seen from the horizontal lines in Figure 3, the intermediate plateau corresponds to a phase when the model reaches the unigram baseline. We provide evidence that this is not a coincidence, and that after the initial drop in loss, the model’s strategy is very similar to the unigram strategy, before eventually being overtaken by the bigram strategy. Some of the strongest such evidence is on the right in Figure 3, where we plot the KL divergence between model’s prediction and the two different strategies. For both the strategies, their KL divergence from the model quickly goes down, with the unigram solution being significantly lower. Around the point of the second loss drop, the KL divergence between the model and the bigram solution decreases, while the other one increases, making it clear that the model transitions from the one solution to the other. This final drop is what has been associated to prior work with induction heads formation (Olsson et al.,, 2022); special dedicated heads inside a transformer are suddenly being formed to facilitate in-context learning.

#### Mechanistic Evidence For Solutions Found By Transformer.

To confirm how the two layer attention-only transformer solves ICL-MC, we inspected the attention in each layer throughout training. Figure 2 shows the attention for a particular input during different parts of training. By the end of training, the attention consistently matches that of our construction, with the first layer attending to tokens one in the past, and the second layer attending to tokens that follow the same token as the current one. Note that even if the second layer of the transformer is mostly the same as at the end of training, if the first layer is different, then the weights shown for the second layer attention could differ dramatically. See also Figure 11 in the Appendix that displays how the models perform on different parts of the distribution during training.

---

[referencia=b9e232df2cb9a34c score=0.686]
## Appendix A Proofs

In this section, we present our theoretical results on in-context learning Markov Chains with the minimal model of Section 2.3.

#### Setup and notation

Our data consists of sequences of length , , drawn from a Markov Chain with state space (i.e., for all ), and a random transition matrix . Each row of the matrix is sampled from a Dirichlet distribution with concentration parameter , i.e. . Unless stated otherwise, we set , corresponding drawing the row from a uniform distribution over the simplex. Let denote the one-hot embedding of the state at position and let be the embedding matrix. We assume there are 2 states in the Markov Chain, i.e. . In that case, the transition matrix can be parameterized as:

|  |  |  | (A.9) | 

where .

#### Model

We define our model as a simplified sequence to sequence linear transformer with . It is and , where . Equivalently, we can express the -th logit for the -th position as:

|  |  |  | (A.10) | 

The model can represent the unigrams and bigrams solutions as following:

- • 
Construction for bigrams: and , then .
- • 
Construction for unigrams: and (all ones), then .

---

[referencia=b9e232df2cb9a34c score=0.630]
## 2 Setup

In this section, we describe our learning problem, several analytical properties of it, and present the neural networks that we will use for learning.

### 2.1 ICL-MC Task

Our learning task consists of Markov Chains with random transition matrices. The goal is to in-context estimate the transition probabilities from sampled sequences, in order to predict the next state. Formally, a sample is a Markov Chain with state space and a transition matrix randomly sampled from some prior distribution, with drawn from some other prior distribution (potentially dependent on ), and the rest of drawn from the Markov Chain. We primarily focus on the case where each row of the matrix is sampled from the Dirichlet distribution with concentration parameter , i.e. . We want to learn a predictor that, given context , predicts the next token, . Note that this is an inherently non-deterministic task, even provided full information about the transition matrix, and as such it can better capture certain properties of language than previous in-context learning modeling approaches (Garg et al.,, 2022).

We focus on the case of that corresponds to uniformly random transition probabilities between states. We draw the initial state from the stationary distribution of the chain (which exists almost surely). We primarily consider the case where the number of states is 2 or 3.

In subsection 3.3, we consider the generalization of this setting to -grams for . Instead of being determined by , we let be determined by , according to a conditional distribution drawn from some prior. In particular, for each tuple of tokens, we sample the vector of conditional probabilities for the next state from a uniform Dirichlet distribution.

---

[referencia=b9e232df2cb9a34c score=0.617]
The goal of this work is to propose and analyze a simple synthetic setting for studying ICL. To achieve this, we consider -gram models (Brown et al.,, 1992; Shannon,, 1948; Chomsky,, 1956), one of the simplest and oldest methods for language modeling. An -gram language model predicts the probability of a token based on the preceding tokens, using fixed-size chunks (-grams) of text data to capture linguistic patterns. Our work studies ICL of -gram models, where the network needs to compute the conditional probability of the next token based on the statistics of the tokens observed in the input context, rather than on the statistics of the entire training data. We mainly focus on the simple case of ; i.e., bigram models, which can be represented as Markov chains. We therefore consider ICL of Markov chains (ICL-MC): we train a transformer on sequences of tokens, where each sequence is produced by a different Markov chain, generated using a different transition matrix (see Figure 1 (left)).

By studying ICL-MC, we are able to replicate and study multiple phenomena that have been observed in ICL for LLMs, and identify new ones. We demonstrate our findings using a combination of empirical observations on transformers trained from scratch on ICL-MC and theoretical analysis of a simplified linear transformer. Our key findings are summarized below:

---

[referencia=b9e232df2cb9a34c score=0.609]
#### Simplicity Bias.

Various works observed that neural networks have a “simplicity bias”, which causes them to “prioritize” learning simple patterns first (Arpit et al.,, 2017; Valle-Perez et al.,, 2018). The work of (Kalimeris et al.,, 2019) shows that SGD learns functions of increased complexity, first fitting a linear concept to the data before moving to more complex functions. (Shah et al.,, 2020) shows that the simplicity bias of neural networks can sometimes be harmful, causing them to ignore important features of the data. Chen et al., (2023) demonstrate the effect of simplicity bias on language tasks that require understanding of syntactic structure. Abbe et al., (2023) provide a theoretical framework for understanding how the simplicity of the target function can govern the convergence time of SGD, describing how simple partial solutions can speed up learning; in contrast, in our setting, the unigram solution appears likely to be a distractor which delays learning of the correct solution.

#### Concurrent works

In parallel to this work, there have been a number of papers devoted to the study of similar questions regarding in-context learning and Markov Chains: Akyürek et al., (2024) empirically compare the ability of different architectures to perform in-context learning of regular languages. Hoogland et al., (2024) observe similar stage-wise learning behaviors on transformers trained on language or synthetic linear regression tasks. Makkuva et al., (2024) study the loss landscape of transformers trained on sequences sampled from a single Markov Chain.

---

[referencia=b9e232df2cb9a34c score=0.589]
## 3 Empirical Findings and Theoretical Validation

In this section, we present our empirical findings on how transformers succeed in in-context learning Markov Chains, we demonstrate the different learning stages during training and the sudden transitions between them, and draw analytical and empirical insights from the minimal model.

---

[referencia=b9e232df2cb9a34c score=0.557]
- Chomsky, (1956) Chomsky, N. (1956). Three models for the description of language. IRE Transactions on information theory, 2(3):113–124.
- Dai et al., (2022) Dai, D., Sun, Y., Dong, L., Hao, Y., Sui, Z., and Wei, F. (2022). Why can gpt learn in-context? language models secretly perform gradient descent as meta optimizers. arXiv preprint arXiv:2212.10559.
- Dong et al., (2022) Dong, Q., Li, L., Dai, D., Zheng, C., Wu, Z., Chang, B., Sun, X., Xu, J., and Sui, Z. (2022). A survey for in-context learning. arXiv preprint arXiv:2301.00234.
- Elhage et al., (2021) Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., Askell, A., Bai, Y., Chen, A., Conerly, T., et al. (2021). A mathematical framework for transformer circuits. Transformer Circuits Thread, 1.
- Garg et al., (2022) Garg, S., Tsipras, D., Liang, P., and Valiant, G. (2022). What can transformers learn in-context? A case study of simple function classes. In Koyejo, S., Mohamed, S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A., editors, Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November 28 - December 9, 2022.
- Guo et al., (2023) Guo, T., Hu, W., Mei, S., Wang, H., Xiong, C., Savarese, S., and Bai, Y. (2023). How do transformers learn in-context beyond simple functions? a case study on learning with representations. arXiv preprint arXiv:2310.10616.

---

[referencia=b9e232df2cb9a34c score=0.352]
- Hendel et al., (2023) Hendel, R., Geva, M., and Globerson, A. (2023). In-context learning creates task vectors. In Findings of the Association for Computational Linguistics: EMNLP 2023, pages 9318–9333.
- Hoogland et al., (2024) Hoogland, J., Wang, G., Farrugia-Roberts, M., Carroll, L., Wei, S., and Murfet, D. (2024). The developmental landscape of in-context learning. CoRR, abs/2402.02364.
- Jacot et al., (2018) Jacot, A., Hongler, C., and Gabriel, F. (2018). Neural tangent kernel: Convergence and generalization in neural networks. In Bengio, S., Wallach, H. M., Larochelle, H., Grauman, K., Cesa-Bianchi, N., and Garnett, R., editors, Advances in Neural Information Processing Systems 31: Annual Conference on Neural Information Processing Systems 2018, NeurIPS 2018, December 3-8, 2018, Montréal, Canada, pages 8580–8589.
- Kalimeris et al., (2019) Kalimeris, D., Kaplun, G., Nakkiran, P., Edelman, B., Yang, T., Barak, B., and Zhang, H. (2019). Sgd on neural networks learns functions of increasing complexity. Advances in neural information processing systems, 32.
- Karpathy, (2023) Karpathy, A. (2023). Mingpt. https://github.com/karpathy/minGPT/tree/master.
- Kirsch et al., (2022) Kirsch, L., Harrison, J., Sohl-Dickstein, J., and Metz, L. (2022). General-purpose in-context learning by meta-learning transformers. CoRR, abs/2212.04458.
- Kumar et al., (2023) Kumar, T., Bordelon, B., Gershman, S. J., and Pehlevan, C. (2023). Grokking as the transition from lazy to rich training dynamics. CoRR, abs/2310.06110.

---

[referencia=b9e232df2cb9a34c score=0.343]
## 1 Introduction

Large language models (LLMs) exhibit a remarkable ability to perform *in-context learning* (ICL): learning from patterns in their input context (Brown et al.,, 2020; Dong et al.,, 2022).
The ability of LLMs to adaptively learn from context is profoundly useful, yet the underlying mechanisms of this emergent capability are not fully understood.

In an effort to better understand ICL, some recent works propose to study ICL in controlled synthetic settings—in particular, training transformers on mathematically defined tasks which require learning from the input context. For example, a recent line of works studies the ability of transformers to perform ICL of standard supervised learning problems such as linear regression (Garg et al.,, 2022; Akyürek et al.,, 2022; Li et al.,, 2023; Wu et al.,, 2023). Studying these well-understood synthetic learning tasks enables fine-grained control over the data distribution, allows for comparisons with established supervised learning algorithms, and facilitates the examination of the in-context “algorithm” implemented by the network. That said, these supervised settings are reflective specifically of *few-shot learning*, which is only a special case of the more general phenomenon of networks incorporating patterns from their context into their predictions. A few recent works (Bietti et al.,, 2023; Xie et al.,, 2022) go beyond the case of cleanly separated in-context inputs and outputs, studying in-context learning on distributions based on discrete stochastic processes.

---

[referencia=b9e232df2cb9a34c score=0.262]
- • 
Transformers learn statistical induction heads to optimally solve ICL-MC. Prior work studying ICL in transformers revealed the formation of *induction heads* (Elhage et al.,, 2021), a circuit that looks for recent occurrence(s) of the current token, and boosts the probabilities of tokens which followed in the input context.
We show that in order to solve ICL-MC, transformers learn statistical induction heads that are able to compute the correct*conditional (posterior) probability* of the next token given all previous occurrences of the prior token (see the attention patterns in Figure 2). We show that these statistical induction heads lead to the transformers achieving performance approaching that of the Bayes-optimal predictor.
- • 
Transformers learn predictors of increasing complexity and undergo a phase transition when increasing complexity. We observe that transformers display phase transitions when learning Markov chains—learning appears to be separated into phases, with fast drops in loss between the phases. We are able to show that different phases correspond to learning models of increased complexity—unigrams, then bigrams (see Figure 1)—and characterize the transition between the phases. We also consider the -gram generalization of our setting where the next token is generated based on the previous tokens.
- • 
Simplicity bias may slow down learning. We provide evidence that the model’s inherent bias towards simpler solutions (in particular, in-context unigrams) causes learning of the optimal solution to be delayed. Changing the distribution of the in-context examples to remove the usefulness of in-context unigrams leads to faster convergence, even when evaluated on the original distribution.
- • 
Alignment of layers is crucial. We show that the transition from a phase of learning the simple-but-inadequate solution to the complex-and-correct solution happens due to an alignment between the layers of the model: the learning signal for the first layer is tied to the extent to which the second layer approaches its correct weights.
- • 
Alternating patterns in positional embeddings. When we train transformers with relative position embeddings, the theoretical optimization analysis of our simplified model indicates that along the way to the correct solution, the first layer develops a bias toward looking back an *odd* number of tokens, even though only looking back by 1 is clearly useful. We empirically observe this curious phenomenon in real transformers as well.

---

[referencia=b9e232df2cb9a34c score=0.255]
#### Passing by unigrams.

The gradient of the positional embeddings at initialization delivers no information about the optimal solution, but has a quadratic structure instead that mostly favors . If the gradient of the 2nd layer is small in scale (which can happen either due to the initialization of or to a small learning rate), then will not deviate much from the uniform initialization. Notice, then, that a uniform together with a biased first coordinate of correspond precisely to the unigram solution in this model. Thus, it is clear in this case that not being aligned with the solution yet, not only slows down , but also biases it towards a simpler solution. We believe that the same mechanism, perhaps manifested differently, is also responsible for the hierarchical learning in the transformer.

#### Even/odd pattern.

An interesting observation that comes out from the calculations is the form of after 2 steps; the gradient amplifies much more the even coordinates than the odd ones, with a scale that follows a geometric series. In fact, the ratio is closely related to the moments of the eigenvalue of the transition matrix. This way the second coordinate starts growing larger than the rest and the model eventually learns to represent the bigrams solution. As a byproduct, however, the rest of the even coordinates also grow in magnitude, despite not being part of the optimal solution. Perhaps surprisingly, we are able to also identify the same spurious pattern in the transformers! In the transformer, if the positional embeddings are dominating attention (that is, if is unimportant in that layer), we can define an analogue of the minimal model: . Unlike in the minimal model, depends on the token at position , but in practice, during most of training, is similar regardless of the value of . As can be seen on the top of Figure 3 (see also Figure 12), shortly before the second drop in the loss as the induction head forms around , the positional embeddings start showing the same even/odd pattern for the first positions.

---

[referencia=b9e232df2cb9a34c score=0.180]
### 3.2 Theoretical Insights from the Minimal Model

To abstract away some of the many complicated components from the transformer architecture, we focus our attention now to the minimal model of Section 2.3. We train minimal models of eq. (8), starting from a deterministic constant initialization, by minimizing the cross entropy loss with sgd. Full experimental details can be found in the Appendix. Figure 3 (bottom) displays the training curves for the minimal model. Similar to the transformer, the model learns to converge to the bigrams solution, spending however significantly less time, if any, to the unigram solution - even though they can represent it.

We now provide theoretical insights on how training progresses stage by stage and how this is achieved by the synergy between the two layers. As it turns out, there need to be at least two steps of gradient descent in order for both elements of the solution to be formed. The following lemma quantifies this.

###### Lemma 3.1.

See Appendix A for the proof. We see that the gradient of at initialization has a clear diagonal bias, and so it starts driving the 2nd layer towards the correct solution - see Constructions in subsection 2.3. The gradient of the positional embeddings, , however, is rather “uninformative" to the correct coordinate that contains the one back position. Instead, it mostly favors the first position (look at current token), and has a quadratic decay. It is only after the second step that the 1st layer also starts realizing the solution, by growing - see Figure 4(b).

There are several interesting observations that follow from Lemma 3.1 and can help us understand better the two stages of learning - both in the toy model and in the transformer:

#### 2nd layer is learnt first

It has been observed before in a similar bigram learning setting with a two-layer transformer that the model might be learning first the 2nd layer (Bietti et al.,, 2023). We also make similar observations in our experiments with the minimal model and the transformers 2, although the evidence is not so clear in the latter case. For the minimal model, the gradient calculations, clearly suggest that starting from a default initialization, it is only the 2nd layer that quickly “picks up" the right solution.

---

[referencia=b9e232df2cb9a34c score=0.172]
#### Induction Heads.

Elhage et al., (2021) studies the formation of induction heads, sub-components of transformers that match previous occurrences of the current token, retrieving the token that succeeds the most recent occurrence. Olsson et al., (2022) studies in-context learning by analyzing the formation of induction heads in language models, showing empirical evidence that both large and small transformers display a phase transition in the ability to learn in-context. Reddy, (2023) also studies the formation of induction heads and their role in ICL, showing empirically that a three layer network exhibits a sudden formation of induction heads towards solving some ICL problem of interest. Bietti et al., (2023) study the effect of specific trigger tokens on the formation of induction heads.

#### Phase Transitions.

It has been observed in different contexts that neural networks and language models display a sudden drop in loss during their training process. This phase transition is often related to emergence of new capabilities in the network. The work of (Power et al.,, 2022) observed the “grokking” phenomena, where the test loss of neural networks sharply drops, long after the network overfits the training data. (Chen et al.,, 2023) shows another example of a phase transition in language model training, where the formation of specific attention mechanisms happen suddenly in training, causing the loss to quickly drop. Barak et al., (2022) observe that neural networks trained on complex learning problems display a phase transition when converging to the correct solution. Several works (Kumar et al.,, 2023; Lyu et al.,, 2023) attribute these phase transitions to rapid changes in the inductive bias of networks, while Merrill et al., (2023) argue that the models are sparser after the phase change. Schaeffer et al., (2023) warn that phenomena in deep learning that seem to be discontinuous can actually be understood to evolve continuously once seen through the right lens.

---

[referencia=b9e232df2cb9a34c score=0.154]
- Vaswani et al., (2017) Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. (2017). Attention is all you need. In Guyon, I., von Luxburg, U., Bengio, S., Wallach, H. M., Fergus, R., Vishwanathan, S. V. N., and Garnett, R., editors, Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA, pages 5998–6008.
- Von Oswald et al., (2023) Von Oswald, J., Niklasson, E., Randazzo, E., Sacramento, J., Mordvintsev, A., Zhmoginov, A., and Vladymyrov, M. (2023). Transformers learn in-context by gradient descent. In International Conference on Machine Learning, pages 35151–35174. PMLR.
- Wu et al., (2023) Wu, J., Zou, D., Chen, Z., Braverman, V., Gu, Q., and Bartlett, P. L. (2023). How many pretraining tasks are needed for in-context learning of linear regression? arXiv preprint arXiv:2310.08391.
- Xie et al., (2022) Xie, S. M., Raghunathan, A., Liang, P., and Ma, T. (2022). An explanation of in-context learning as implicit bayesian inference. In The Tenth International Conference on Learning Representations, ICLR 2022, Virtual Event, April 25-29, 2022.