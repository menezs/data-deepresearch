[referencia=6c590c4bea08449d score=0.956]
**Corollary 3.2.** _Non-uniform_ TC<sup>0</sup> _⊆_ T _/_ poly _._ 

Since non-uniform TC<sup>0</sup> even contains some undecidable languages (Arora and Barak, 2009, Claim 6.8), T _/_ poly is clearly a very powerful class and a strict superset of T, the class of decision problems recognized by transformers (which are all decidable). Thus, a problem in T _/_ poly cannot always be solved by a transformer on its own. However, if given a description of _how_ to do so (“advice”) in the form of a TC<sup>0</sup> circuit, our result shows that a transformer _could_ solve that problem. 

# **8 Conclusion** 

Answering two open questions from Merrill et al. (2022), we prove log-precision transformers with any (including soft) attention can be simulated by _uniform_ constant-depth threshold circuits. This establishes _thresholded addition_ as a fundamental operation for understanding the computational model of transformers: any log-precision transformer can be re-expressed as a polynomial number of threshold gates stacked to a constant depth. This result also establishes potential limits on the computational power of log-precision transformers; e.g., if L _⊂_ P, transformers cannot compute all poly-time functions. They are certainly very far from being universal. The intuition at the heart of this result is that forcing a model to be highly parallelizable likely sacrifices its expressiveness. Since parallelism seems essential to pretraining any massive model at scale, any large language model—transformer or otherwise—may suffer from a similar tradeoff.

---

[referencia=6c590c4bea08449d score=0.952]
**The Parallelism Tradeoff: Limitations of Log-Precision Transformers** 

# **William Merrill** 

Center for Data Science New York University, New York, NY willm@nyu.edu 

# **Abstract** 

Despite their omnipresence in modern NLP, characterizing the computational power of transformer neural nets remains an interesting open question. We prove that transformers whose arithmetic precision is logarithmic in the number of input tokens (and whose feedforward nets are computable using space linear in their input) can be simulated by constant-depth logspace-uniform threshold circuits. This provides insight on the power of transformers using known results in complexity theory. For example, if L = P (i.e., not all poly-time problems can be solved using logarithmic space), then transformers cannot even accurately solve linear equalities or check membership in an arbitrary context-free grammar with empty productions. Our result intuitively emerges from the transformer architecture’s high parallelizability. We thus speculatively introduce the idea of a fundamental **parallelism tradeoff** : any model architecture as parallelizable as the transformer will obey limitations similar to it. Since parallelism is key to training models at massive scale, this suggests a potential inherent weakness of the scaling paradigm. 

# **1 Introduction** 

This work aims to characterize the computational model implicit in transformer neural networks (Vaswani et al., 2017), which form the basis of recent breakthroughs in large language models such as BERT (Devlin et al., 2019), T5 (Raffel et al., 2020), and GPT-3 (Brown et al., 2020). What computational primitives can the transformer’s components implement, and what problems can the full system solve in aggregate? These questions are important for interpreting transformers in a principled way, understanding potential limitations of their reasoning capabilities, and building trust in deployed transformer-based systems.

---

[referencia=6c590c4bea08449d score=0.942]
**2 Implications of Our Findings** 



<!-- Start of picture text -->
• Propositional satisfiability  (SAT) 3<br><!-- End of picture text -->



<!-- Start of picture text -->
Before diving into technical details, we discuss the •<br>Horn-clause satisfiability  (HORN-SAT) 1<br>general implications of our findings on the abili- • AI planning  (Bylander, 1991)<br>ties and limitations of transformers. We will focus • Permanent computation 4<br>here on our main result (Thm. 2), which shows that<br>This highlights the limits of practical transformers<br>log-precision transformers are in the complexity with limited-precision arithmetic, indicating that<br>class logspace-uniform TC 0 . they are far from being universal or all-powerful<br>as suggested by some prior studies.<br>The Parallelism Tradeoff. One interpretation<br>One important caveat about these negative re-<br>of complexity classes such as NC 0 , AC 0 , and TC 0<br>sults is that they are asymptotic in nature—they<br>is sets of poly-time solvable problems that are<br>apply for “large enough” input size  n . It’s possible<br>parallelizable to a very high degree—they can be<br>for log-precision transformers to solve such prob-<br>solved in parallel in constant time with enough<br>lems easily when  n  is small. Further, these nega-<br>parallel processors. This gives some intuitive ex-<br>tive results are about exact solutions, but they of-<br>planation of our result: log-precision transformers<br>ten also extend beyond this when formal hardness-<br>end up in TC 0 because they were designed to be<br>of-approximation results are known.<br>highly parallelizable. Since parallelism is an im-<br>portant property of today’s dominant paradigm of Limitations of Our Formal Model. Prior for-<br>training models at massive scale, this points to the mal characterizations of transformers either make<br>conclusion that any massively scaled up model— unrealistically strong assumptions (Pérez et al.,<br>transformer or otherwise—will likely obey restric- 2019; et al., 2019) or unrealistic<br><!-- End of picture text -->

---

[referencia=6c590c4bea08449d score=0.849]
# **3 Circuit Computation** 

Let _{_ 0 _,_ 1 _}_<sup>_∗_</sup> be the set of finite binary strings. For _x ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , let _|x|_ be its length. We refer to a function from _{_ 0 _,_ 1 _}_<sup>_∗_</sup> to _{_ 0 _,_ 1 _}_<sup>_∗_</sup> as a boolean function. Boolean functions can implement arithmetic operations if we define a semantics for binary strings as numbers. We will treat the intermediate values in a transformer as binary strings, and the internal operations as boolean functions. 

_Circuits_ are a model of computation for computing boolean functions of fixed-length binary strings.<sup>6</sup> Formally, a circuit is a directed acyclic computation graph. The leaf nodes represent binary variables and their negations. The internal nodes represent functions in some set _G_ , and the 

> 5Their sense of “circuit” is not exactly the formal sense we use in this paper, though the goal of capturing transformers’ implicit computational mechanism is the same. 

> 6For a mini-tutorial on circuit complexity theory and its relevance to transformers, see Merrill et al. (2022). 

directed edges represent the flow of function outputs into inputs of other functions. One or more nodes in the circuit are marked such that their value is the output of the circuit. 

**Definition 1.** For a set of functions _G_ , a _G_ -circuit is a directed acyclic computation graph where the internal nodes have labels from _G_ . 

**Complexity Measures.** The _size_ of a circuit is the total number of gates in it, including negation. The _depth_ of a circuit is the length of the longest path from any input node to any output node. 

**Circuit Families.** A _circuit family_ generalizes a circuit to take variable-length binary strings as input. Formally, a circuit family is a sequence of circuits _Cn_ : _{_ 0 _,_ 1 _}_<sup>_n_</sup> _→{_ 0 _,_ 1 _}_ for _n ∈_ N. A circuit family implicitly recognizes a formal language defined as follows:

---

[referencia=6c590c4bea08449d score=0.840]
We show that one can achieve both of these goals by making the modest assumption that all values in the transformer have O(log _n_ ) precision (where _n_ is the number of input tokens), 

and, similarly, that transformer’s subnetworks are computable in O(log _n_ ) space. Log precision is enough to represent the positional encodings at the input layer of the transformer, and to encode pointers to all other positions in the sequence at later transformer layers. Assuming log precision across all layers captures the idea that the hidden representations contain a constant number of hidden states whose precision (16 or 32 bits) is small relative to the length of the input (2048 in GPT-3). On long sequences, the precision will not be enough to losslessly encode the full input sequence into a single vector. Instead, the processing of the sequence must somehow be distributed in each layer and performed in parallel. 

**Upper Bound on Transformers.** Our main contribution is proving that log-precision transformers can be simulated by _uniform_ constant-depth threshold circuits. Thus, **such transformers can only solve problems in uniform** TC<sup>0</sup> . This characterization is strikingly weak compared to the Turing-completeness of infinite-precision transformers. Since we believe log precision is more realistic for practical transformers than infinite precision, these results point to the conclusion that transformers are not Turing-complete in practice. 

In contrast to past results, our upper bound on transformers is a _uniform_ circuit class, enabling direct comparison of log-precision transformers to many natural complexity classes. These connections reveal specific problems that define the upper limits of log-precision transformers’ capabilities, as discussed further in §2. 

Intuitively, our upper bound says that logprecision transformers are computationally shallow, and that this shallowness can be understood to emerge from their parallelizability. Transformers’ inherent parallelism is useful for training them efficiently at massive scale, but may limit the complexity of the computations they can express. We introduce the term **parallelism tradeoff** to capture this idea, which represents a potential fundamental weakness of the current paradigm of scaling language models. Formally characterizing reasoning capabilities relevant to language models and understanding whether they likely fall outside upper bounds implied by the tradeoff would clarify the practical implications of this limitation of scaling. 

It could also be that the limitations of parallelism are not a curse but a blessing, if they constrain the hypothesis space in a way useful for

---

[referencia=6c590c4bea08449d score=0.808]
It could also be that the limitations of parallelism are not a curse but a blessing, if they constrain the hypothesis space in a way useful for 

learning. We have no evidence that this is true, but mention it as an alternate interpretation of the 

**Instruction Following and Advice Transformers.** We also consider an instruction following setting (Brown et al., 2020) where the transformer is provided the description of a task along with an input on which to execute the instruction. We construct a practically parameterizable transformer that can execute instructions perfectly if they are provided in the form of TC<sup>0</sup> circuits. This complements recent work that studies transformers’ ability to follow other forms of instructions such as regular expressions (Finlayson et al., 2022). 

Based on the fundamental property that transformers can correctly _evaluate_ any given TC<sup>0</sup> circuit on a given input, we introduce the notion of _advice transformers_ akin to advice taking Turing machines. We show that transformers can recognize any (non-uniform) TC<sup>0</sup> language if provided appropriate poly-size advice. 

In summary, our findings provide new insights on both the abilities and the limitations of transformers, and bring out bounded precision, threshold computations, and parallelism as key notions for understanding the implicit computational model of transformers in practice. 

**Roadmap.** Before diving into technical details, we discuss in §2 the implications of our results on both fundamental as well as practical abilities of transformers. §3 provides a brief primer on circuits as a model of computation. It then discusses a way of serializing a circuit into a string; we later show how to generate such serializations using a resource-bounded algorithm, which is the key to proving containment of transformers in _uniform_ circuit classes. §4 defines our formal model of bounded-precision transformers. §5 derives our first formal bound on log-precision transformers. This bound involves _non-uniform_ circuit families, similar in spirit to prior results in this area. §6 proves our more technical main result: the first _uniform_ circuit complexity upper bound for transformers (specifically, uniform TC<sup>0</sup> ). Finally, §7 provides a _lower bound_ on transformers, introduces the notion of an Advice Transformer, and connects these to the machine learning problems of Instruction Learning and Following. 

• **Universal context-free recognition**<sup>1</sup><sup>_,_2</sup>

---

[referencia=6c590c4bea08449d score=0.787]
# **Ashish Sabharwal** 

Allen Institute for AI Seattle, WA ashishs@allenai.org 

Early theoretical work on transformers established their Turing completeness, albeit with assumptions like infinite precision and arbitrarily powerful feedforward subnets (Pérez et al., 2019; Dehghani et al., 2019). On the other hand, a strand of more recent work uses techniques from circuit complexity theory to derive strong limitations on the types of problems transformers can solve given restrictions on the form of attention allowed in the transformer. Specifically, Hahn (2020) and Hao et al. (2022) showed transformers restricted to hard attention are very limited: they can only solve problems in a weak complexity class (non-uniform AC<sup>0</sup> ) that doesn’t even contain basic problems like majority of _n_ bits. Merrill et al. (2022) extended this to a more general class of “saturated attention” transformers with a floating point datatype, and showed a larger class of problems (non-uniform TC<sup>0</sup> ) as an upper bound. This motivates analyzing a setting that strikes a middle ground: _Can we characterize transformers whose precision and feedforward nets’ computational power are realistically bounded, but where attention is also realistically expressive?_ 

An important practical limitation of these prior results is the “non-uniform” nature of the considered circuit classes, which makes these classes non-realizable and the findings difficult to interpret. This is because non-uniform AC<sup>0</sup> and TC<sup>0</sup> , while highly limited in computation, also contain some problems that are not even decidable, i.e., for which there doesn’t exist any exact algorithm. Thus, non-uniform classes cannot be directly compared with standard algorithmic complexity classes such as P, NP, etc. This motivates our second key question: _Can we derive uniform upper bounds on transformers?_ 

We show that one can achieve both of these goals by making the modest assumption that all values in the transformer have O(log _n_ ) precision (where _n_ is the number of input tokens),

---

[referencia=6c590c4bea08449d score=0.745]
**Definition 2.** A circuit family _Cn_ recognizes _L ⊆ {_ 0 _,_ 1 _}_<sup>_∗_</sup> if, for all _x ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , _C|x|_ ( _x_ ) = 1 if and only if _x ∈ L_ . 

We now define classes of languages by constraining the complexity of the circuit families needed to recognize them: 

**Definition 3.** Let non-uniform AC<sup>0</sup> be the set of _L ⊆{_ 0 _,_ 1 _}_<sup>_∗_</sup> such that _L_ is recognizable by a polysize, constant-depth _{¬, ∧, ∨}_ -circuit family. 

For _k ∈_ N, a _threshold gate θ≤k_ takes _m_ input bits and returns whether<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_xi≤k_.We define</sup> _θ≥k_ analogously. For example, _θ≤_ 3(110011) = 0. 

**Definition 4.** Let TC<sup>0</sup> be the set of _L ⊆ {_ 0 _,_ 1 _}_<sup>_∗_</sup> such that _L_ is recognizable by a poly-size, constant-depth _{θ≤k, θ≥k}k∈_ N-circuit. 

The gates _¬_ , _∧_ , and _∨_ are all just special cases of thresholds, so we can imagine TC<sup>0</sup> circuits to have access to these as well. Thus, TC<sup>0</sup> circuits can implement AC<sup>0</sup> circuits. 

**Circuit Serialization.** We identify a circuit with its serialization in a formal language that identifies each node’s label and adjacency list. We will adopt a specific grammar for concreteness, but our construction can be adapted to other string representations of circuits.

---

[referencia=6c590c4bea08449d score=0.724]
# **6 Log-Precision Transformers as** **_Uniform_ Threshold Circuits** 

We will now extend the argument from the last section to show that O(log _n_ )-precision transformers can be simulated by uniform constant-depth threshold circuits by capitalizing on the assumption that _φ, s,_ and _f_ are log-precision, and thus can be computed in O(log _n_ ) space. The overall proof idea is similar, but due to the uniformity condition, the proof becomes substantially more technical. We must not just show the existence of a threshold circuit family computing a transformer, but also show that this circuit family can be generated by a log-space Turing machine. 

We first extend Lem. 1 to respect uniformity: 

**Lemma 2.** _Let f_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>_m_</sup> _be a linearspace computable function. There exists a Turing machine that, for all n ∈_ N _and c ∈_ R<sup>+</sup> _, uses at most c_ log _n_ + log _m space to map input_ 1<sup>_n_</sup> _to a circuit of size at most n_<sup>_c_</sup> + _c_ log _n_ + _m and depth_ 3 _that computes f on inputs of size at most c_ log _n._ 

_Proof._ We give the proof in the form of an algorithm to construct a circuit as a function of _n_ and then justify its correctness and space complexity. 

Algorithm. We first print 2 _c_ log _n_ nodes representing unnegated and negated input nodes.<sup>15</sup>

---

[referencia=6c590c4bea08449d score=0.721]
- Neil Immerman. 2012. _Descriptive complexity_ . Springer Science & Business Media. 

- Neil D. Jones and William T. Laaser. 1976. Complete problems for deterministic polynomial time. _Theoretical Computer Science_ , 3(1):105– 117. 

- Richard E Ladner. 1975. The circuit value problem is log space complete for P. _ACM SIGACT News_ , 7(1):18–20. 

- Harry R. Lewis and Christos H. Papadimitriou. 1982. Symmetric space-bounded computation. _Theoretical Computer Science_ , 19:161–187. 

- William Merrill, Vivek Ramanujan, Yoav Goldberg, Roy Schwartz, and Noah A. Smith. 2021. Effects of parameter norm growth during transformer training: Inductive bias from gradient descent. In _Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing_ . 

- William Cooper Merrill. 2020. On the linguistic capacity of real-time counter automata. _ArXiv_ , abs/2004.06866. 

- William Cooper Merrill, Ashish Sabharwal, and Noah A. Smith. 2022. Saturated transformers are constant-depth threshold circuits. _Transactions of the Association for Computational Linguistics_ , 10. 

- Jorge Pérez, Javier Marinkovi´c, and Pablo Barceló. 2019. On the Turing completeness of modern neural network architectures. In _International Conference on Learning Representations_ . 

- Colin Raffel, Noam M. Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. _Journal of Machine Learning Research_ , 21(140). 

- Omer Reingold. 2008. Undirected connectivity in log-space. _Journal of the ACM_ , 55:17:1–17:24. 

- Leslie G. Valiant. 1979. The complexity of computing the permanent. _Theoretical Computer Science_ , 8:189–201.

---

[referencia=6c590c4bea08449d score=0.709]
# **7 Lower Bounds for Instruction Following and Advice Transformers** 

So far, we have shown that uniform TC<sup>0</sup> is an upper bound for log-precision transformers. Is this upper bound tight, i.e., also a lower bound? While we do not answer this question here, we address a related question as a first step: we construct a transformer that can evaluate TC<sup>0</sup> circuits on binary inputs, showing that transformers can compute any TC<sup>0</sup> function when their input is augmented with the right “instructions”. 

More formally, we consider the **Circuit Value Problem (CVP)** (Ladner, 1975), also referred to as the Circuit Evaluation Problem, where the input is a boolean circuit _C_ and a string _x ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> , and the task is to return the value of _C_ ( _x_ ) _∈{_ 0 _,_ 1 _}_ . This problem is known to be complete for the class P under AC<sup>0</sup> reductions (Ladner, 1975). We will assume _C_ is serialized as described in §3 and prove that log-precision transformers can evaluate any TC<sup>0</sup> circuit. Note that this is an extension of the typical CVP since the circuit has threshold gates, not just standard AND/OR gates. 

It is known that LSTMs cannot evaluate boolean formulae (Merrill, 2020), a special case of the CVP. In contrast, we show that transformers can. 

To demonstrate the practicality of our lower bound construction, we will not just prove the existence of transformers that can evaluate TC<sup>0</sup> circuits but also specify concrete choices for the positional embedding scheme and the class of attention

---

[referencia=6c590c4bea08449d score=0.687]
_Proof._ We will provide a proof by induction over transformer layers _ℓ_ that there is a Turing machine _M_ operating in O(log _n_ ) space that, on input 1<sup>_n_</sup> , outputs a circuit that simulates the transformer’s computation on inputs of size _n_ . This circuit is identical to the one in the proof of Thm. 1, and thus has the same circuit depth. 

In the base case, we use log space to track a counter maintaining the current token _i_ (between 1 and _n_ ) throughout the circuit construction. We construct gates encoding the constant _i_ in binary. We can then apply Lem. 2 to construct a Turing machine that maps 1<sup>_n_</sup> to a constant-depth threshold circuit computing **h**<sup>0</sup> _i_<sup>=</sup><sup>_φ_(</sup><sup>_wi, i_).</sup> 

In the inductive case, we assume we can output in O(log _n_ ) space a circuit computing every value **h**<sup>_ℓ_</sup> _i_<sup>inthepreviouslayer</sup><sup>_ℓ_.Wewillshowthatwe</sup> can, in O(log _n_ ) space, now output a circuit computing every value in layer _ℓ_ + 1. 

As in Thm. 1, we first fix a head **a**<sup>_ℓ_</sup> _ih_<sup>+1</sup> to simulate. Recall (Def. 8) that

---

[referencia=6c590c4bea08449d score=0.572]
We now use Lem. 1 to prove the following non-uniform result. We note that the proof goes through even if the notion of _p_ -precision (Def. 6) is relaxed to not require computability in space _p_ . This requirement will, however, become important for our subsequent result in §6. 

**Theorem 1** (Non-uniform) **.** _Any c_ log _n-precision depth-d transformer operating on inputs in_ Σ<sup>_n_</sup> _can_ 

> 12Saturated attention is uniform attention over a subset of the prior layer nodes. 

_be simulated by a threshold circuit family of depth_ 3 + (9 + 2 _d⊕_ ) _d._ 

_Proof._ Let _w ∈_ Σ<sup>_n_</sup> be the input of a _c_ log _n_ - precision transformer. We show by induction that we can construct a composition of constant-depth, poly-size threshold circuits to compute each layer of this transformer. Thus, any constant-depth transformer will be computable by a constantdepth threshold circuit. 

In the base case of layer 0 and token _i_ , we construct gates representing the constant _i_ encoded in binary. We can then compute **h**<sup>0</sup> _i_<sup>=</sup><sup>_φ_(</sup><sup>_wi, i_) using</sup> Lem. 1, yielding a poly-size depth-3 circuit. 

In the inductive case of computing layer **h**<sup>_ℓ_</sup> _i_<sup>+1</sup> for 1 _≤ ℓ_ + 1 _≤ d_ , we note that each vector output of layer **h**<sup>_ℓ_</sup> _i_<sup>has size (at most)</sup><sup>_c_log</sup><sup>_n_bits because</sup> of the log-precision assumption.

---

[referencia=6c590c4bea08449d score=0.438]
## X X <= 00 &1 >= 10 & &11 

We say a threshold circuit serialization is in _prefix form_ if all inputs (X) come before all threshold gates (<= or >=), as is the case in this example. 

> 7Spaces here (and in the grammar) are added for readability. We will ignore these spaces when passing circuit serializations as inputs to a transformer in §7. 

> 8We can apply De Morgan’s laws to force any AC0 circuit to have this property. 

**Uniformity.** The circuit families we have defined above are _non-uniform_ , meaning that we do not enforce that the circuits processing different input sizes must be related in any way. In degenerate cases, non-uniform circuit families can solve undecidable problems<sup>9</sup> because they have infinite description length, making them a physically unrealizable model of computation. Complexity theorists have thus introduced _uniform_ circuit families. Uniform circuit families are a realizable model of computation with relations to classes in computational complexity and formal language theory. 

Intuitively, in a uniform circuit family, the circuits for different input sizes must be “somewhat similar” to each other. We formalize this (cf. Arora and Barak, 2009) by saying that there exists a resource-constrained Turing machine that maps the input 1<sup>_n_</sup> to a serialization of circuit _Cn_ . 

**Definition 5.** A language _L_ is ( _S_ ( _n_ ) _, I_ ( _n_ ))-space uniformly computable by a circuit model _M_ iff there exists a Turing machine that, for all _n ≥_ 0, uses _S_ ( _n_ ) space to map 1<sup>_n_</sup> to an _M_ -circuit recognizing _L_ on inputs of size _I_ ( _n_ ). 

This notion of uniformity is more general than the standard notion in that the input size _I_ ( _n_ ) is a function of the problem complexity _n_ . The reason for this is that we will apply uniformity to subcomputations with different input sizes _I_ ( _n_ ) within a larger computation of input size _n_ . The standard notion of uniformity corresponds to _I_ ( _n_ ) = _n_ .

---

[referencia=6c590c4bea08449d score=0.412]
We now simulate a layer **h**<sup>_ℓ_</sup> _i_<sup>+1</sup> (Def. 10) in terms of its constituent heads. Since all arguments of _g_ have size _c_ log _n_ , we apply Lem. 1 to compute _g_ with a poly-size depth-3 circuit, yielding **h**<sup>_ℓ_</sup> _i_<sup>+1</sup> . We repeat this in parallel for all _i_ . This completes the inductive step new to compute all values in the _ℓ_ + 1-st layer with a circuit depth of 9 + 2 _d⊕_ . 

Aggregating the circuit over all _d_ layers, the overall circuit depth is 3 + (9 + 2 _d⊕_ ) _d_ . 

**Corollary 1.1** (Non-uniform) **.** _Any log-precision transformer can be simulated by a non-uniform_ TC<sup>0</sup> _circuit family._<sup>14</sup> 

> 13This may seem counterintuitive since multiplication of two _n_ -precision numbers is outside AC<sup>0</sup> . However, here we leverage the fact that the precision is _c_ log _n_ . 

> 14Here, a TC0 circuit family is a constant-depth, poly-size circuit family computing some function _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>_∗_</sup> . While we define TC<sup>0</sup> for decision problems in Def. 4, it is standard and well-defined to extend the same term to refer to circuit families computing functions as well (Hesse, 2001).

---

[referencia=6c590c4bea08449d score=0.400]
We define a circuit serialization as a traversal of a circuit ordered by some topological sort. In this serialization, leaf nodes (variables) are represented by the string X. An internal node (gate) is represented in Polish notation by the function it 

computes (AND, OR, or NOT) followed by a list of pointers to its arguments. Each argument &1<sup>_j_</sup> of gate _i_ encodes (in a unary) a zero-indexed pointer to the _j_ -th gate in the circuit, where _j < i_ . The final node is interpreted as the circuit output. 

To serialize _{∧, ∨}_ -circuits, we use the following grammar, where the _i_ parameter is passed through Gate[ _i_ ] nonterminals to track the index of the gate in left-to-right order: 



In the Arg[ _i_ ] rule, we enforce that _j < i_ so that arguments must be pointers to already defined gates. As an example of this serialization language, the circuit for _x_ 1 _∨¬x_ 2 _∨ x_ 3 is represented as<sup>7</sup> 

## X X X NOT &1 OR & &111 &11 

By convention (cf. §3), negations in AC<sup>0</sup> circuits are usually taken to occur at the beginning of the circuit, rather than after _∧_ or _∨_ nodes.<sup>8</sup> Our serialization grammar does not enforce this property, but of course any circuit with this property can be serialized by our grammar. 

It is a bit more complicated to serialize threshold circuits. Formally, a threshold circuit serialization is generated by the following grammar: 



In the rewrite rule for Gate[ _i_ ], _m ∈_ N is the arity of the gate, and _k ≤ m_ is its threshold. The span 1<sup>_k_</sup> after Dir can be interpreted semantically as a unary encoding of the parameter _k_ for a threshold gate, padded by 0’s to the number of total arguments of gate _i_ . For simplicity, we imagine _¬_ gates are represented as unary _θ≤_ 0 gates. Thus, the circuit _θ≥_ 1( _x_ 1 _, ¬x_ 2) would be represented as

---

[referencia=6c590c4bea08449d score=0.373]
- Tim Dettmers, Mike Lewis, and Luke Zettlemoyer. 2022. GPT3.int8(): 8-bit matrix multiplication for transformers at scale. In _Advances in Neural Information Processing Systems_ . 

- Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers for language understanding. In _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ . 

- Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah. 2021. A mathematical framework for transformer circuits. _Transformer Circuits Thread_ . 

- Matthew Finlayson, Kyle Richardson, Ashish Sabharwal, and Peter Clark. 2022. What makes instruction learning hard? An investigation and a new challenge in a synthetic environment. In _Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing_ . 

- Raymond Greenlaw, James M. Hoover, and Walter L. Ruzzo. 1991. A compendium of problems complete for P. Technical Report TR9111, University of Alberta. 

- Michael Hahn. 2020. Theoretical limitations of self-attention in neural sequence models. _Transactions of the Association for Computational Linguistics_ , 8:156–171. 

- Yiding Hao, Dana Angluin, and Robert Frank. 2022. Formal language recognition by hard attention transformers: Perspectives from circuit complexity. _Transactions of the Association for Computational Linguistics_ , 10:800–810. 

- William Hesse. 2001. Division is in uniform _TC_<sup>0</sup> . In _International Colloquium on Automata, Languages, and Programming_ , pages 104–114. 

- Neil Immerman. 2012. _Descriptive complexity_ . Springer Science & Business Media.

---

[referencia=6c590c4bea08449d score=0.332]
# **5 Log-Precision Transformers as Non-Uniform Threshold Circuits** 

We first show that log-precision transformers can be simulated by _non-uniform_ threshold circuits, before presenting the more technical _uniform_ version of the results in §6. The initial non-uniform result extends the findings of Merrill et al. (2022), who showed that _saturated_ attention transformers<sup>12</sup> can be simulated in TC<sup>0</sup> . Here, we remove the simplifying saturated attention assumption and other restrictions on the underlying datatype. Instead, we show that our log-precision assumption is enough to prove that a transformer can be simulated in TC<sup>0</sup> with any attention function. 

Hao et al. observed that any boolean function of O(log _n_ ) bits can be computed by a poly( _n_ ) size circuit. We extend this to _m_ -bit outputs, which is both more convenient and more efficient than constructing _m_ separate boolean circuits: 

**Lemma 1** (Extended from Hao et al., 2022) **.** _Let f_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>_m_</sup> _be a function. For all c ∈_ R<sup>+</sup> _and n ∈_ N _, there exists an AND/OR circuit of size at most n_<sup>_c_</sup> + _c_ log _n_ + _m and depth_ 3 _that computes f on inputs of size c_ log _n._ 

_Proof._ Like Hao et al. (2022), we construct a circuit using a DNF representation of _f_ on inputs of size _c_ log _n_ , except we use a combined DNF representation for all output bits of _f_ . The DNF formula has at most 2<sup>_c_log</sup><sup>_n_</sup> = _n_<sup>_c_</sup> terms. The circuit has a NOT gate for each input bit, an AND gate for each DNF term, and, for each of the _m_ output bits, an OR gate combining the outputs of those AND gates (i.e., DNF terms) for which that bit is 1.

---

[referencia=6c590c4bea08449d score=0.297]
<u>Correctness.</u> We show that this Turing machine maps input _n_ to a serialized circuit computing _f_ 

> 15We ignore the initial unnegated input nodes when considering the size of the circuit. 

on inputs of size _n_ . The first layer simply produces unnegated and negated input values. The second layer then produce all possible DNF terms. Finally, node _k_ of the third layer computes the disjunction over all terms _x_ such that _fk_ ( _x_ ) = 1. Thus, node _k_ of the third layer computes _fk_ . 

Log Space. To complete the proof, we justify that _M_ uses O(log _n_ +log _m_ ) space. Looping over _x ∈{_ 0 _,_ 1 _}_<sup>_c_log</sup><sup>_n_</sup> is accomplished by treating _x_ as a binary number initialized to 0 and incrementing it at each step. Thus, the loop pointer for building the DNF terms takes _c_ log _n_ space to store. For building the _m_ output nodes, we maintain a similar loop pointer as well as an index _k ≤ m_ , taking _c_ log _n_ + log _m_ space. Thus, the overall algorithm uses _c_ log _n_ + log _m_ space. 

Thus, _M_ uses _c_ log _n_ + log _m_ space to map 1<sup>_n_</sup> to a circuit of size at most _n_<sup>_c_</sup> + _c_ log _n_ + _m_ and depth 3 that computes _f_ on size _c_ log _n_ inputs. 

We can leverage this lemma to derive the _uniform_ analog of Thm. 1, as follows. 

**Theorem 2** (Uniform, main result) **.** _Any c_ log _nprecision depth-d transformer operating on inputs in_ Σ<sup>_n_</sup> _can be simulated by a logspace-uniform threshold circuit family of depth_ 3 + (9 + 2 _d⊕_ ) _d._

---

[referencia=6c590c4bea08449d score=0.284]
We will use _n_ to denote the length of _w_ , and take the transformer’s depth _d_ to be fixed w.r.t. _n_ . 

The **input** to the transformer can thus be represented with _N_ = _n_ log _|_ Σ _|_ bits using a binary encoding for the vocabulary. The circuits we construct in subsequent sections to simulate transformers will also have input size _N_ . We will assume transformers have **log-precision** relative to the size of the input, specifically O(log _N_ )- precision. Since _|_ Σ _|_ is fixed (typically 30000 in practice), we will think in terms of O(log _n_ )- precision. Thus, by Def. 6, all of the intermediate functions of such transformers are computable in O(log _n_ ) space and output (at most) these many bits. Note that this is enough precision to represent positional encodings and for each position to point to a constant number of other values, but not enough precision for non-lossy pooling of the entire input into a single value. 

**Relationship to Practical Transformers.** Our log-precision transformers do not enforce that _s_ (Def. 7) and _f_ (Def. 9) follow the transformer structure. However, a feedforward net whose primitive operations (e.g., scalar multiplication) are defined over O(log _n_ )-size numbers can be 

> 11 To apply the normal notion of _p_ -precision to inputs outside _{_ 0 _,_ 1 _}_<sup>_∗_</sup> , we imagine elements of Σ are encoded as integers _≤|_ Σ _|_ in binary, and natural numbers are represented as integers _≤ n_ . Thus, we assume log _|_ Σ _|_ + log _n ≤ p_ . 

computed in O(log _n_ ) space. Thus, boundedprecision practical transformers are a special case of our log-precision transformers. This makes our setup appropriate for proving upper bounds on transformers, which is our main contribution.