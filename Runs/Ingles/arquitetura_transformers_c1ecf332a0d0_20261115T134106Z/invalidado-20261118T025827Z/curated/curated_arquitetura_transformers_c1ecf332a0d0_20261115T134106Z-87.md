[referencia=260c917913f5d8f0 score=0.978]
# **Theoretical Limitations of Self-Attention in Neural Sequence Models** 

## **Michael Hahn** 

Stanford University mhahn2@stanford.edu 

## **Abstract** 

Transformers are emerging as the new workhorse of NLP, showing great success across tasks. Unlike LSTMs, transformers process input sequences entirely through self-attention. Previous work has suggested that the computational capabilities of selfattention to process hierarchical structures are limited. In this work, we mathematically investigate the computational power of selfattention to model formal languages. Across both soft and hard attention, we show strong theoretical limitations of the computational abilities of self-attention, finding that it cannot model periodic finite-state languages, nor hierarchical structure, unless the number of layers or heads increases with input length. These limitations seem surprising given the practical success of self-attention and the prominent role assigned to hierarchical structure in linguistics, suggesting that natural language can be approximated well with models that are too weak for the formal languages typically assumed in theoretical linguistics.

---

[referencia=260c917913f5d8f0 score=0.743]
the first theoretical results on limitations in the by Pérez et al. (2019), who theoretically studied power of self-attention. We will provide results the ability of Seq2Seq transformers to emulate the both for hard and soft attention settings, using difcomputation of Turing machines. While we conferent proof methods. Our results are strongest in sider incremental modeling of sequences, where the hard attention setting, holding without further the number of computation steps is bounded by assumptions on activation functions and paramethe input length _n_ , they study the setting in which ter norms. In the soft attention settings, we still the transformer computes an unbounded number obtain results assuming smoothness of activation of autoregressive decoding steps, not bounded in functions as used in practical implementations. the input length _n_ . Even more recently, and more 

- After discussing related work (Section 2), we closely related to our interest here, Hsieh et al. 

- introduce self-attention (Section 3) and two funda(2019) studied the adversarial robustness of transmental formal languages representing regular and formers. While they focused on experiments on context-free languages (Section 4). We then prove NLP tasks, they also provided a theoretical analythat self-attention cannot model these languages sis, showing that a single self-attention layer with 

- using either hard (Section 5) or soft (Section 6) ata single head will be robust against input perturbatention. Finally, we discuss our results (Section 7). tions, assuming that input embeddings are drawn uniformly from the unit sphere. One of our results, 

- **2 Related Work** Lemma 5, can be seen as considerably widening the scope of their result, both by avoiding distribu- 

- **Prior Work on Self-Attention** Transformers tional assumptions, and by applying to transform- 

- were proposed by Vaswani et al. (2017), previous ers with arbitrary numbers of heads and layers.

---

[referencia=260c917913f5d8f0 score=0.712]
Nonetheless, the success of transformers across NLP tasks suggests that many aspects of natu- 

ral language can be modeled well with methods that are formally too weak for the formal languages typically assumed in theoretical linguistics. Beyond general limitations of asymptotic analysis, a possible reason for this phenomenon is that language uses recursive structure only in restricted ways due to cognitive factors. For instance, it has long been noted that center embeddings, syntactic structures exhibiting iterated bracketing, are very challenging for humans to process (Miller and Chomsky, 1963; Gibson and Thomas, 1999). Intriguingly, self-attention bears some resemblance to psycholinguistic models of memory in human sentence processing that assume that humans, while processing a word, attend to chunks that were stored in memory when processing some previous words (Lewis and Vasishth, 2005; Parker et al., 2017). Such processing models predict difficulty with center embedding because they cannot count brackets (Lewis and Vasishth, 2005), akin to what we have shown theoretically for neural network models based on self-attention. 

## **8 Conclusion** 

We formally investigated the capabilities of selfattention in modeling regular languages and hierarchical structure. We showed that transformers cannot model periodic regular languages or basic recursion, either with hard or soft attention, and even if infinite precision is allowed. This entails that self-attention cannot in general emulate stacks or general finite-state automata. Our results theoretically confirm the idea that self-attention, by avoiding recurrence, has quite limited computational power. 

## **Acknowledgments** 

I thank Dan Jurafsky, Yoav Goldberg, the anonymous reviewers, and the members of the Stanford NLP Group for helpful comments.

---

[referencia=260c917913f5d8f0 score=0.661]
In this work, we examine these questions from a theoretical perspective, asking whether models entirely based on self-attention are theoretically capable of modeling hierarchical structures involving unbounded recursion. Formally, we study their ability to perform two computations that are thought to be essential to hierarchical structure: First, their ability to correctly **close brackets** , a basic problem underlying all nonregular contextfree languages and formalized by the **DYCK** language (Chomsky and Schützenberger, 1963). Second, their ability to **evaluate iterated negation** , a basic component of the task of evaluating logical formulas, amounting to evaluating the **PARITY** of bitstrings. We show that neither of these problems can be solved by transformers and similar models relying entirely on self-attention, unless the number or size of parameters increases with the input length. Besides representing basic building blocks of hierarchical structure, these languages also represent large classes of regular and contextfree languages, meaning that our results carry over 

to classes of other formal languages. Our results therefore also yield more generally limitations on the ability of self-attention to model finite-state languages and context-free languages. 

verb agreement and evaluating logical formulas. 

therefore also yield more generally limitations on Their experimental results suggested that LSTMs the ability of self-attention to model finite-state are better at learning hierarchical structure. Yang languages and context-free languages. et al. (2019) experimentally investigated the power While theoretical work has investigated the of self-attention to extract word order informapower of recurrent neural networks in depth tion, finding differences between recurrent and (e.g., Siegelman and Sontag (1995); Bengio et al. self-attention models; however, these were mod(1994); Weiss et al. (2018); Miller and Hardt ulated by the training objective. Lin et al. (2019) (2019); Merrill (2019)), the theoretical study of and Tenney et al. (2019) show that BERT (Devlin self-attention has begun only recently (Pérez et al., et al., 2019) encodes syntactic information. 2019; Hsieh et al., 2019). Our study provides Theoretical study of transformers was initiated

---

[referencia=260c917913f5d8f0 score=0.653]
We believe that the most imminent implications of our results are theoretical in nature. They showcase mathematical techniques for analyzing the 

capabilities of self-attention, an architecture at the heart of recent advances in NLP. These tools provide theoretical understanding of differences between self-attention and theoretically more wellstudied recurrent architectures: Recurrent networks such as LSTMs can perfectly emulate finitestate automata, and therefore can model any finite state language with optimal cross-entropy, as long as the state transition and symbol emission distributions are Markovian. In particular, PARITY of i.i.d. bitstrings can be predicted with perfect accuracy and cross-entropy, independent of the input length. Furthermore, infinite-precision RNNs and LSTMs can model stacks (Tabor, 2000; Grüning, 2006; Kirov and Frank, 2012) and thus are theoretically capable of modeling 2DYCK and other deterministic context-free languages perfectly. The results presented here thus theoretically confirm the intuition that models entirely built on selfattention may have restricted expressivity when compared to recurrent architectures (Tran et al., 2018; Dehghani et al., 2019; Shen et al., 2018a; Chen et al., 2018; Hao et al., 2019). Complementing the asymptotic methods developed here with empirical studies or non-asymptotic extensions is an interesting avenue for future research. 

While finite languages are sufficient to model language up to any finite bound on sequence length, it has typically been argued that asymptotically more powerful formalisms at the level of context-free grammars or beyond are necessary to properly capture generalizations about the syntax and meaning of natural language (e.g., Chomsky (1957); Shieber (1985)). Our results entail that self-attention is limited in its ability to model context-free languages or evaluate logical formulas. In particular, self-attention cannot in general emulate stacks or arbitrary finite-state automata. Whether this hinders its capacity for syntactic generalization in practice is an interesting question; empirical research suggests that models with strong quantitative performance – both recurrent and transformer models – continue to struggle with syntactic generalization and that quantitative performance metrics such as perplexity can partly be dissociated from syntactic knowledge displayed on more challenging benchmarks (e.g., Kuncoro et al. (2018); Marvin and Linzen (2018); Tran et al. (2018); McCoy et al. (2019)).

---

[referencia=260c917913f5d8f0 score=0.071]
- R Thomas McCoy, Junghyun Min, and Tal Linzen. 2019. Berts of a feather do not generalize together: Large variability in generalization across models with similar test set performance. _arXiv preprint arXiv:1911.02969_ . 

- Robert McNaughton and Seymour A Papert. 1971. _Counter-Free Automata (MIT research monograph no. 65)_ . The MIT Press. 

- William Merrill. 2019. Sequential neural netRNN/CNN-free language understanding. In works as automata. In _Proceedings of the WorkThirty-Second AAAI Conference on Artificial shop on Deep Learning and Formal Languages: Intelligence_ . _Building Bridges_ , pages 1–13, Florence. Association for Computational Linguistics. Tao Shen, Tianyi Zhou, Guodong Long, Jing 

   - Tao Shen, Tianyi Zhou, Guodong Long, Jing Jiang, Sen Wang, and Chengqi Zhang. 2018b. Reinforced self-attention network: a hybrid of hard and soft attention for sequence modeling. In _IJCAI’18 Proceedings of the 27th International Joint Conference on Artificial Intelligence_ , pages 4345–4352. 

- George A Miller and Noam Chomsky. 1963. Finitary models of language users. In R. Duncan Luce, Robert R. Bush, and Eugene Galanter, editors, _Handbook of Mathematical Psychology_ , pages 419–492. John Wiley. 

- John Miller and Moritz Hardt. 2019. Stable recurrent models. In _International Conference on Learning Representations_ . 

   - Stuart M Shieber. 1985. Evidence against the context-freeness of natural language. In _Philosophy, Language, and Artificial Intelligence_ , pages 79–89. Springer. 

- Michael Mitzenmacher and Eli Upfal. 2017. _Probability and Computing_ , 2nd edition. Cambridge University Press, Cambridge. 

   - Hava Siegelman and Eduardo D Sontag. 1995. On the computational power of neural nets. _Journal of Computer and System Sciences_ , 50:132– 150.

---

[referencia=260c917913f5d8f0 score=0.069]
of heads in the first layer. After this step, we can collapse the first layer into a collection of feedforward networks that transform a bounded number _≤ cc_<sup>_′_</sup> of input positions into an activation _yi_<sup>(0)</sup> of the lowest layer. After this step, the first layer has been entirely removed. Iterating this argument, we remove all layers until the prediction output only depends on a bounded number of input positions, bounded independently of input length. 

We now make these ideas formal. After the removal of the first layer of a transformer, the resulting structure is not a transformer any more, as each head in the lowest layer now depends on a _combination_ of input positions. We introduce a technical definition to make this concept precise: 

**Definition 3** ( _c_ -Transformer) **.** _Let c be a positive integer. A c-transformer with L layers is one in which the layer-0 activations y_<sup>(</sup> _j_<sup>0)</sup> _depend on the embeddings not just at one position j, but are a function of the embeddings at ≤ c input positions:_ 



With this technical notion, we show that we can reduce layers, iteratively removing the lowest layer until no self-attention layer is left: 

**Lemma 4** (Depth Reduction Lemma) **.** _Given a c- transformer with L layers, and some restriction_ ρ _such that_ 



_(C ∈_ (0 _,_ 1] _) for all sufficiently large n. Choose any C_<sup>_′_</sup> _< C. Then there is a restriction_ ρ<sup>_′_</sup> _such that_ 



_for all sufficiently large n, and such that the resulting function is computed by a_ ( _c ·_ (2<sup>_c_</sup> _kH_ + 1)) _- transformer with L −_ 1 _layers, for some integer k (depending on C_<sup>_′_</sup> _), where H ≥_ 1 _is the number of attention heads at each layer and position._

---

[referencia=260c917913f5d8f0 score=0.058]
related work using self-attention includes Cheng et al. (2016); Parikh et al. (2016); Paulus et al. **Investigating the Power of Sequence Modeling** (2018); Lin et al. (2017). It has been a recurrent **Architectures** The computational power of resuggestion in the literature that transformers, relycurrent neural networks has been a focus of study. ing entirely on self-attention, are restricted comA particular focus has been on their ability to 

A particular focus has been on their ability to 

putationally, as they cannot process their input sequentially. Dehghani et al. (2019) suggested that 

learn non-regular context-free languages, thought to provide simple models of recursion and hierar- 

transformers cannot compute functions that re- 

chical structure as found in natural language.

---

[referencia=260c917913f5d8f0 score=0.041]
## **7 Discussion** 

We have shown that, even with infinite precision, transformers cannot robustly model noncounter-free regular languages, nor basic hierarchical structure. In the hard attention setting, our results hold independently of activation functions and the magnitude of the parameters, and show that no transformer can accurately classify strings as belonging to such languages. In the soft attention setting, our results are slightly less general, but still show that transformers cannot achieve perfect cross-entropies when modeling distributions over these formal languages. 

Our results are asymptotic, in the sense that they show that any transformer will make mistakes on modeling PARITY and 2DYCK when the input is _sufficiently long_ . A transformer may nonetheless be able to perform well on on short inputs; indeed, given any bound _N_ on the input length, it is possible to construct a transformer that will achieve perfect accuracy or cross-entropy on all examples of length _n ≤ N_ ; our results show that the number of heads and layers, or the parameter norms, will have to increase with _N_ . Practical implementations of transformers might thus be able circumvent such asymptotic limitations by using large numbers of layers and heads, in relation to the sentence lengths typically occurring in natural language. Therefore, pending tighter nonasymptotic bounds, the results reported here need not constitute conclusive evidence for practical limitations of real-world NLP systems. 

We believe that the most imminent implications of our results are theoretical in nature. They showcase mathematical techniques for analyzing the

---

[referencia=260c917913f5d8f0 score=0.038]
## **1 Introduction** 

Transformers are emerging as the new workhorse of NLP, achieving the state-of-the-art in tasks such as language modeling, machine translation, and creating pretrained contextualized word embeddings. Eschewing recurrent computations, transformers are entirely based on self-attention, performing their computations largely in parallel. This enables them to scale to very long sequences (Vaswani et al., 2017; Dai et al., 2019; Child et al., 2019). On the other hand, it has been suggested that this limits their expressiveness, as they cannot process input sequentially (Tran et al., 2018; Dehghani et al., 2019; Shen et al., 2018a; Chen et al., 2018; Hao et al., 2019). One aspect thought to be challenging for sequence models is hierar- 

chical structure and recursion. Hierarchical structure is widely thought to be essential to modeling natural language, in particular its syntax (Everaert et al., 2015). Consequently, many researchers have studied the capability of recurrent neural network models to capture context-free languages (e.g., Kalinke and Lehmann (1998); Gers and Schmidhuber (2001); Grüning (2006); Weiss et al. (2018); Sennhauser and Berwick (2018); Korsky and Berwick (2019)) and linguistic phenomena involving hierarchical structure (e.g., Linzen et al. (2016); Gulordava et al. (2018)). Some experimental evidence suggests that transformers might not be as strong as LSTMs at modeling hierarchical structure (Tran et al., 2018), though analysis studies have shown that transformer-based models encode a good amount of syntactic knowledge (e.g., Clark et al. (2019); Lin et al. (2019); Tenney et al. (2019)).

---

[referencia=260c917913f5d8f0 score=0.027]
### quire sequential processing of input, without pro- 

A range of studies has experimentally examined 

viding further details or proofs. Similarly, Shen 

viding further details or proofs. Similarly, Shen the ability of recurrent networks to model counter et al. (2018a); Chen et al. (2018); Hao et al. (2019) languages such as _a_<sup>_n_</sup> _b_<sup>_n_</sup> (Kalinke and Lehmann, have introduced extensions of transformers with 1998; Gers and Schmidhuber, 2001; Cartling, recurrence, citing similar intuitions about limita2008; Weiss et al., 2018; Suzgun et al., 2019). tions of transformers. Our results provide the first Other work has experimentally studied the perfor- 

explicit formalization of these limitations. 

explicit formalization of these limitations. mance of recurent architectures on learning to recA few studies have experimentally tested the ognize well-bracketed strings, a similar but more abilities of transformers to learn structures. Most challenging problem (Sennhauser and Berwick, related to our work, Tran et al. (2018) compared 2018; Skachkova et al., 2018; Bernardy, 2018). 

the ability of transformers and LSTMs to learn hiBeyond modeling formal languages, another line erarchical structure, specifically English subjectof work has studied the ability of LSTMs to model 

hierarchical structure as occurring in realistic natural language data (Linzen et al., 2016; Gulordava et al., 2018). 

Recently, Merrill (2019) and Korsky and Berwick (2019) theoretically studied several types of recurrent networks. Merrill (2019) showed that – in the finite precision setting – LSTMs recognize a subset of the counter languages, whereas GRUs and simple RNNs recognize regular languages. Korsky and Berwick (2019) showed, among other results, that arbitrary-precision RNNs can emulate pushdown automata, and can therefore recognize all deterministic context-free languages.

---

[referencia=260c917913f5d8f0 score=0.024]
## **3 Self-Attention** 

Here we define self-attention as used in Transformers, following Vaswani et al. (2017), with some changes in the notation to simplify arguments in our proofs. We have an input **x** = _x_ 1 _... xn_ , where all _xi_ come from some finite alphabet _V_ , and _xn_ is an end-of-sequence symbol. This input is then encoded into a sequence of input embeddings _v_ 1 _,..., vn_ using some embedding map _V →_ R<sup>_k_</sup> . We furthermore have a sequence _p_ 1 _, p_ 2 _,..._ of positional embeddings _pi ∈_ R<sup>_k_</sup> . These are independent of the input **x** , and can be computed through some predefined scheme, or could be learned for each position occurring in the training data (Vaswani et al., 2017). Input and positional embeddings are combined (e.g., via addition or concatenation) to vectors _y_<sup>(</sup> _i_<sup>0)</sup> = _f_ ( _vi, pi_ ) ( _i_ = 1 _,..., n_ ), which we will refer to as Layer 0. 

A transformer has a fixed number _L_ of **layers** ; the **activations** _y_<sup>(</sup> _i_<sup>_k_)</sup> at position _i_ of the _k_ -th layer ( _k_ = 1 _,..., L_ ) are defined as follows. Each layer has a set of _H_ **attention heads** ; we first compute attention scores for the _h_ -th head:

---

[referencia=260c917913f5d8f0 score=0.017]
duction method, and indeed _can_ be modeled perfectly with self-attention. 

In general, the depth reduction method applies to languages that are sufficiently _sensitive_ : If, for some _C ∈_ (0 _,_ 1), fixing _Cn_ input symbols cannot force a word to be inside or outside of the language, then hard-attention transformers cannot recognize this language. Sensitivity of functions has been studied in computational complexity (Boppana, 1997; Gopalan et al., 2016) and more recently linked to generalization in feedforward networks (De Palma et al., 2018). We intend to investigate these connections in future work. 

**Proof Idea of the Theorem** Our approach for proving Theorem 1 will be to construct input restrictions in a layerwise manner, starting from layer 1. In order for this construction to go through, the main challenge is to construct a suitable restriction at a given layer: As shown in Figure 2, this restriction should only affect a few input bits (about (1 _−C_<sup>1</sup><sup>_/L_</sup> ) _n_ many input bits), while forcing each attention head in the first layer to ignore all but _c_ input bits. Perhaps surprisingly, this is possible; the idea is to fix input bits that achieve high attention scores for several heads, so that input bits that cannot achieve such high attention scores will be ignored. 







Figure 2: Finding a good input restriction: (a) Every attention head in the first layer could potentially attend to any input bit. (b) Perhaps surprisingly, one can fix a small number of input bits in such a way that each layer-1 attention head can only possibly attend to _c_ (here, _c_ = 1) inputs, and ignores all other inputs. Each activation vector _y_<sup>(</sup> _j_<sup>1)</sup> in the first layer then only depends on the _H · c_ inputs that its _H_ (here, _H_ = 1) attention heads can attend to, plus the input _x j_ that feeds into it via a skip-connection.

---

[referencia=260c917913f5d8f0 score=0.016]
In the soft attention version, these weights _a_ ˆ<sup>(</sup> _i,_<sup>_k_</sup> _j_<sup>_,h_)</sup> ˆ are obtained by the softmax operation: _a_<sup>(</sup> _i,_<sup>_k_</sup> _·_<sup>_,h_)</sup> = softmax( _a_<sup>(</sup> _i,_<sup>_k_</sup> _·_<sup>_,h_)</sup> ). In the hard attention variant (Pérez et al., 2019), one takes the actual maximum ˆ attention values: _a_<sup>(</sup> _i,_<sup>_k_</sup> _j_<sup>_,h_)</sup> = δ _j,_ argmax _j′ a_ ( _i,kj,_<sup>_′_</sup> _h_ )<sup>.1</sup> 

The per-position activations are then computed 

as 



where _f_<sup>_act_</sup> is implemented as a fully-connected feedforward network with a skip-connection (Vaswani et al., 2017) from _y_<sup>(</sup> _i_<sup>_k−_1)</sup> to _y_<sup>(</sup> _i_<sup>_k_).</sup> 

**Hard and Soft Attention** There is a choice between soft attention and hard attention (Shen et al., 2018b; Pérez et al., 2019). The one prior theoretical study of transformers (Pérez et al., 2019) assumes hard attention. In practice, soft attention is easier to train with gradient descent; however, analysis studies suggest that attention often concentrates on one or a few positions in trained transformer models (Voita et al., 2019; Clark et al., 2019) and that the most important heads are those that clearly focus on a few positions (Voita et al., 

> 1When there are multiple positions with maximal attention weight, we will assume that the one occurring first in the sequence is chosen. Our analysis also works under other schemes of resolving ties, such as random selection. 

2019), suggesting that attention often behaves like hard attention in practice. We will examine both hard (Section 5) and soft (Section 6) attention.

---

[referencia=260c917913f5d8f0 score=0.015]
## **6 Results for Soft Attention** 

In the previous section, we showed that transformers using hard attention are not able to recognize a range of core formal languages. In this section, we study soft attention. It turns out that proving limitations as strong as what we found in the hard attention setting would settle a major open problem in computational complexity, and may therefore be extremely hard to attain with currently available mathematical methods.<sup>3</sup> This barrier prevents us from proving bounds on the _accuracy_ that soft attention transformers can achieve; nevertheless, we will be able to prove limitations on the achievable _cross-entropy_ in modeling distributions over the formal languages. We will use the smoothness of the operations used in transformers to show that any transformer, as inputs get longer, will not be able to robustly model such distributions. The idea behind the proof is that the impact of any single input symbol on the output of the transformer is small if the input is long: 

**Lemma 5.** _Let a soft attention transformer be given, and let n be the input length. If we exchange one input symbol xi (i < n), then the change in the resulting activation yn_<sup>(</sup><sup>_L_)</sup> _at the decoder layer is bounded as O_ (<sup><u>1</u></sup> _n_<sup>)</sup><sup>_withconstantsdependingon_</sup> _the parameter matrices._ 

3Showing that soft attention transformers cannot achieve perfect accuracy on evaluating Boolean formulas would separate the complexity classes _LTC_<sup>0</sup> and _NC_<sup>1</sup> , a widely conjectured but long-open problem in computational complexity. 

This contrasts with recurrent networks: Changing a single input can have nonnegligible impact on the final state even for very long input. E.g., an RNN recognizing PARITY through a hidden state that encodes parity of the current prefix will flip its hidden state if a single input bit is flipped. 

Lemma 5 entails that, as inputs become longer, soft attention transformers cannot achieve good cross-entropies on prediction problems that are very sensitive to individual input symbols: A Lipschitz-continuous prediction function, such as a ReLU MLP with a softmax output, will not be able to make very different predictions for inputs that are encoded into similar activations _yn_<sup>(</sup><sup>_L_).</sup>

---

[referencia=260c917913f5d8f0 score=0.013]
For 2DYCK, we show that hard attention transformers cannot even solve the simpler variant 

1DYCK with a single bracket type (‘(’, ‘)’). We first restrict the first 0 _._ 2 _n_ input positions to ‘(’ and the last 0 _._ 2 _n_ positions to ‘)’. After then applying the restriction provided by the theorem with _C_ = 0 _._ 9, the resulting restricted input will still be compatible with both well-bracketed and nonwell-bracketed inputs, but the prediction will depend only on a bounded number of positions. As the prediction depends on only a bounded number of positions, this shows the transformer could not recognize 1DYCK, and thus also not 2DYCK. 

**Discussion** It may be instructive to compare to similar languages that _can_ be modeled by hardattention transformers. First, 1<sup>_∗_</sup> (over the alphabet _{_ 0 _,_ 1 _}_ ) is the regular language of words that have only ones and no zeroes; its minimal automaton has two states, like PARITY. A transformer can recognize this by having an attention head that attends to a position with zero input if it exists, and rejects if the head found such a position. Second, _a_<sup>_n_</sup> _b_<sup>_n_</sup> is a very basic context-free language. It can be recognized using suitable positional embeddings by (1) having one head attend to the largest position _n_ , (2) using this information to attend to any _b_ at position _< n/_ 2 or any _a_ at position _≥ n/_ 2. If such a symbol is found, the model rejects, else it accepts. A crucial difference between these languages and PARITY / 2DYCK is that fixing a few inputs in any part of an input string can easily force nonmembership, e.g. a single 0 for 1<sup>_∗_</sup> , and an _a_ in the second half for _a_<sup>_n_</sup> _b_<sup>_n_</sup> . Therefore, such simple languages are immune to the depth re- 

duction method, and indeed _can_ be modeled perfectly with self-attention.

---

[referencia=260c917913f5d8f0 score=0.011]
For _k_ = 0, _∥y_<sup>(</sup> _i_<sup>0)</sup> _− y_<sup>(</sup> _i_<sup>0)</sup> _′∥≤ D_ , and _∥y_ ( _j_ 0) _− ′ y_<sup>(</sup> _j_<sup>0)</sup> _∥_ = 0 for _j_ = _i_ . For _k >_ 0, we first note that _∥y_<sup>(</sup> _j_<sup>_k_)</sup><sup>_∥_2</sup><sup>_≤_2</sup><sup>_CL_</sup> _f_<sup>_act_(</sup><sup>_∥pj∥_+</sup><sup>_∥vj∥_),where</sup><sup>_Cf act<_</sup> ∞ depends on the norms of the parameter matrices of _f_<sup>_act_</sup> , which is implemented as a ReLU MLP (Vaswani et al., 2017). We’ll write _F_ for this upper bound for _∥y_<sup>(</sup> _j_<sup>_k_)</sup><sup>_∥_2.</sup> Attention logits are bounded by _A_ := _F_<sup>2</sup> _C f att_ in the case of dotproduct attention, and _A_ := 2 _FC f att_ in the case of additive attention. Then any attention weight � _a j,i_ = exp( _ai_ ) _/_ ∑ _j_ exp( _a j_ ) is upper bounded by exp( _A_ <u>)</u> exp( _A_ )+( _n−_ 1) exp( _−A_ )<sup>_≤_ex</sup> _n_<sup><u>p</u></sup> _−_<sup><u>(2</u></sup> 1<sup>_A_</sup><sup><u>)</u>.</sup>

---

[referencia=260c917913f5d8f0 score=0.009]
2019), suggesting that attention often behaves like hard attention in practice. We will examine both hard (Section 5) and soft (Section 6) attention. 

**Formalizing Language Recognition** We consider the problem of language recognition, the task of classifying input strings as belonging to or not belonging to a formal language. Following Weiss et al. (2018), we formalize this as the sequence-to-sequence task of mapping words to labels 1 (‘in the language’) and 0 (‘not in the language’). Following the construction of transformers in sequence-to-sequence tasks (Vaswani et al., 2017), we compute a softmax probability vector for this label from the last activation _yn_<sup>(</sup><sup>_L_), obtained</sup> after reading the end-of-sequence symbol.

---

[referencia=260c917913f5d8f0 score=0.009]
- André Grüning. 2006. Stack-like and queue-like dynamics in recurrent neural networks. _Connection Science_ , 18(1):23–42. 

- Kristina Gulordava, Piotr Bojanowski, Edouard Grave, Tal Linzen, and Marco Baroni. 2018. Colorless green recurrent networks dream hierarchically. In _Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)_ , pages 1195–1205, New Orleans, Louisiana. Association for Computational Linguistics. 

- Jie Hao, Xing Wang, Baosong Yang, Longyue Wang, Jinfeng Zhang, and Zhaopeng Tu. 2019. Modeling recurrence for transformer. In _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)_ , pages 1198–1207, Minneapolis, Minnesota. Association for Computational Linguistics. 

- Johan Hastad, Ingo Wegener, Norbert Wurm, and Sang-Zin Yi. 1994. Optimal depth, very small size circuits for symmetrical functions in AC0. _Information and Computation_ , 108(2):200–211. 

- Yu-Lun Hsieh, Minhao Cheng, Da-Cheng Juan, Wei Wei, Wen-Lian Hsu, and Cho-Jui Hsieh. 2019. On the robustness of self-attentive models. In _Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics_ , pages 1520–1529, Florence, Italy. Association for Computational Linguistics. 

- Yvonne Kalinke and Helko Lehmann. 1998. Computation in recurrent neural networks: From counters to iterated function systems. In _Australian Joint Conference on Artificial Intelligence_ , pages 179–190. Springer. 

- Christo Kirov and Robert Frank. 2012. Processing of nested and cross-serial dependencies: an automaton perspective on SRN behaviour. _Connection Science_ , 24(1):1–24.

---

[referencia=260c917913f5d8f0 score=0.007]
downwards by this value, obtaining a sequence _j_ 1<sup>(</sup><sup>_z_)</sup><sup>_,..., j_</sup> _n_<sup>(</sup><sup>_z_)</sup> for each layer-1 attention head _h_ at a position _i_ and each possible value _z_ of _y_<sup>(</sup> _i_<sup>0)</sup> (In the case of ties, we order by position, by Footnote 1). For each layer-1 attention head and each _z_ , we select a sequence 1 _≤ i_<sup>(</sup> 1<sup>_z_)</sup><sup>_< i_(</sup> 2<sup>_z_)</sup><sup>_< ··· < i_(</sup> _k_<sup>_z_)</sup><sup>_≤n_such</sup> that (1) for each _i_<sup>(</sup> _s_<sup>_z_),thereisatleastoneinput</sup><sup>_x_</sup> _q_ that only feeds into the activation at position _j_<sup>(</sup><sup>_z_)</sup> _i_<sup>(</sup> _s_<sup>_z_)</sup> and no _j_<sup>(</sup><sup>_z_)=</sup><sup>_s′_),and(2)</sup><sup>_i_(</sup> _k_<sup>_z_)</sup> is minimal, i.e. _i_<sup>(</sup> _s_<sup>_z′_)(</sup><sup>_s_</sup> there is no subsequence with smaller _i_<sup>(</sup> _k_<sup>_z_)</sup> that also satisfies (1). This construction is visualized in an example in Figure 3. Such a subsequence exists unless _n ≤ ck_ , in which case the Depth Reduction Lemma is already satisfied for this input length _n_ .