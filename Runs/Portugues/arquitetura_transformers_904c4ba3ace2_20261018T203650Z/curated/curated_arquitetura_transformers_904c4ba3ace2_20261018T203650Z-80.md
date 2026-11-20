[referencia=d001ef8922253622 score=0.964]
# Mamba: Linear-Time Sequence Modeling with Selective State Spaces 

Albert Gu<sup>∗1</sup> and Tri Dao<sup>∗2</sup> 

1 Machine Learning Department, Carnegie Mellon University 

2 Department of Computer Science, Princeton University agu@cs.cmu.edu, tri@tridao.me 

##### **Abstract** 

Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to _selectively_ propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks ( **Mamba** ). Mamba enjoys fast inference (5× higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

---

[referencia=d001ef8922253622 score=0.043]
Additionally, we elaborate on effects of each selective parameter. 

**Interpretation of** Δ **.** In general, Δ controls the balance between how much to focus or ignore the current input _𝑥𝑡_ . It generalizes RNN gates (e.g. _𝑔𝑡_ in Theorem 1): mechanically, a large Δ resets the state _ℎ_ and focuses on the current input _𝑥_ , while a small Δ persists the state and ignores the current input. SSMs (1)-(2) can be interpreted as a continuous system discretized by a timestep Δ, and in this context the intuition is that large Δ →∞ represents the system focusing on the current input for longer (thus “selecting” it and forgetting its current state) while a small Δ → 0 represents a transient input that is ignored. 

**Interpretation of** _𝑨_ **.** We remark that while the _𝑨_ parameter could also be selective, it ultimately affects the model only through its interaction with Δ via _𝑨_ = exp(Δ _𝑨_ ) (the discretization (4)). Thus selectivity in Δ is enough to ensure selectivity in ( _𝑨, 𝑩_ ), and is the main source of improvement. We hypothesize that making _𝑨_ selective in addition to (or instead of) Δ would have similar performance, and leave it out for simplicity. 

**Interpretation of** _𝑩_ **and** _𝑪_ **.** As discussed in Section 3.1, the most important property of selectivity is filtering out irrelevant information so that a sequence model’s context can be compressed into an efficient state. In an SSM, modifying _𝑩_ and _𝑪_ to be selective allows finer-grained control over whether to let an input _𝑥𝑡_ into the state _ℎ𝑡_ , or the state into the output _𝑦𝑡_ . These can be interpreted as allowing the model to modulate the recurrent dynamics based on content (input) and context (hidden states) respectively.

---

[referencia=d001ef8922253622 score=0.015]
### **3.1 Motivation: Selection as a Means of Compression** 

We argue that a fundamental problem of sequence modeling is _compressing context into a smaller state_ . In fact, we can view the tradeoffs of popular sequence models from this point of view. For example, attention is both effective and inefficient because it explicitly does not compress context at all. This can be seen from the fact that autoregressive inference requires explicitly storing the entire context (i.e. the KV cache), which directly causes the slow linear-time inference and quadratic-time training of Transformers. On the other hand, recurrent models are efficient because they have a finite state, implying constant-time inference and linear-time training. However, their effectiveness is limited by how well this state has compressed the context. 

To understand this principle, we focus on two running examples of synthetic tasks (Figure 2). 

- The **Selective Copying** task modifies the popular Copying task (Arjovsky, Shah, and Bengio 2016) by varying the position of the tokens to memorize. It requires _content-aware_ reasoning to be able to memorize the relevant tokens ( _colored_ ) and filter out the irrelevant ones ( _white_ ). 

- The **Induction Heads** task is a well-known mechanism hypothesized to explain the majority of in-context learning abilities of LLMs (Olsson et al. 2022). It requires _context-aware_ reasoning to know when to produce the correct output in the appropriate context ( _black_ ). 

These tasks reveal the failure mode of LTI models. From the recurrent view, their constant dynamics (e.g. the ( _𝑨, 𝑩_ ) transitions in (2)) cannot let them select the correct information from their context, or affect the hidden state passed along the sequence in an input-dependent way. From the convolutional view, it is known that global convolutions can solve the vanilla Copying task (Romero et al. 2021) because it only requires time-awareness, but that they have difficulty with the Selective Copying task because of lack of content-awareness (Figure 2). More concretely, the spacing between inputs-to-outputs is varying and cannot be modeled by static convolution kernels.

---

[referencia=d001ef8922253622 score=0.015]
In summary, the efficiency vs. effectiveness tradeoff of sequence models is characterized by how well they compress their state: efficient models must have a small state, while effective models must have a state that contains all necessary information from the context. In turn, we propose that a fundamental principle for building sequence models is **selectivity** : or the context-aware ability to focus on or filter out inputs into a sequential state. In particular, a selection mechanism controls how information propagates or interacts along the sequence dimension (see Section 3.5 for more discussion).

---

[referencia=d001ef8922253622 score=0.013]
#### **4.1.2 Induction Heads** 

Induction heads (Olsson et al. 2022) is a simple task from the mechanistic interpretability lens (Elhage et al. 2021) that is surprisingly predictive of the in-context learning ability of LLMs. It requires models to perform associative recall and copy: for example, if the model has seen a bigram such as “Harry Potter” in the sequence, then the next time “Harry” appears in the same sequence, the model should be able to predict “Potter” by copying from history. 

**Dataset.** We train a 2-layer model on the induction heads task at sequence length 256, with a vocab size of 16, which is comparable to prior work on this task (Dao, Fu, Saab, et al. 2023) but with longer sequences. We additionally investigate generalization and extrapolation abilities by evaluating on a range of sequence lengths from 2<sup>6</sup> = 64 up to 2<sup>20</sup> = 1048576 at test time. 

**Models.** Following established work on induction heads, we use 2 layer models, which allows attention to mechanistically solve the induction heads task (Olsson et al. 2022). We test both multi-head attention (8 heads, with various positional encodings) and SSM variants. We use a model dimension _𝐷_ of 64 for Mamba and 128 for the other models. 

**Results.** Table 2 shows that Mamba—or more precisely, its selective SSM layer—has the ability to solve the task perfectly because of its ability to selectively remember the relevant token while ignoring everything else in between. **It generalizes perfectly to million-length sequences, or** 4000× **longer than it saw during training** , while no other method goes beyond 2×. 

10

---

[referencia=d001ef8922253622 score=0.006]
#### **3.5.2 Interpretation of Selection Mechanisms** 

We elaborate on three particular mechanistic effects of selection. 

**Variable Spacing.** Selectivity allows filtering out irrelevant noise tokens that may occur between inputs of interest. This is exemplified by the Selective Copying task, but occurs ubiquitously in common data modalities, particularly for discrete data – for example the presence of language fillers such as “um”. This property arises because the model can mechanistically filter out any particular input _𝑥𝑡_ , for example in the gated RNN case (Theorem 1) when _𝑔𝑡_ → 0. 

**Filtering Context.** It has been empirically observed that many sequence models do not improve with longer context (F. Shi et al. 2023), despite the principle that more context should lead to strictly better performance. An explanation is that many sequence models cannot effectively ignore irrelevant context when necessary; an intuitive example are global convolutions (and general LTI models). On the other hand, selective models can simply reset their state at any time to remove extraneous history, and thus their performance in principle improves monotonicly with context length (e.g. Section 4.3.2). 

8 

**Boundary Resetting.** In settings where multiple independent sequences are stitched together, Transformers can keep them separate by instantiating a particular attention mask, while LTI models will bleed information between the sequences. Selective SSMs can also reset their state at boundaries (e.g. Δ _𝑡_ →∞, or Theorem 1 when _𝑔𝑡_ → 1). These settings may occur artificially (e.g. packing documents together to improve hardware utilization) or naturally (e.g. episode boundaries in reinforcement learning (Lu et al. 2023)). 

Additionally, we elaborate on effects of each selective parameter.

---

[referencia=d001ef8922253622 score=0.005]
|Mamba|74K|✓|✓|100.0|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|✓|



> <u>∗</u> Most of the parameters are in learnable positional encodings. 

optimized Transformer implementation with FlashAttention. In particular, each attention layer (FlashAttention) stores around 12 bytes of activations per token, an each MLP layer stores around 20 bytes of activations per token, for a total of 32 bytes ((assuming mixed-precision training in FP16 or BF16)). Each selective SSM stores around 16 bytes of activations per token. Hence two layers of selective SSMs have around the same activation memory as an attention layer and an MLP layer.

---

[referencia=d001ef8922253622 score=0.004]
> ∗Alphabetical by first name. 

1 

Arena (Tay, Dehghani, Abnar, et al. 2021). Many flavors of SSMs (Gu, Goel, and Ré 2022; Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Y. Li et al. 2023; Ma et al. 2023; Orvieto et al. 2023; Smith, Warrington, and Linderman 2023) have been successful in domains involving continuous signal data such as audio and vision (Goel et al. 2022; Nguyen, Goel, et al. 2022; Saon, Gupta, and Cui 2023). However, they have been less effective at modeling discrete and information-dense data such as text. 

We propose a new class of **selective state space models** , that improves on prior work on several axes to achieve the modeling power of Transformers while scaling linearly in sequence length. 

**Selection Mechanism.** First, we identify a key limitation of prior models: the ability to efficiently _select_ data in an input-dependent manner (i.e. focus on or ignore particular inputs). Building on intuition based on important synthetic tasks such as selective copy and induction heads, we design a simple selection mechanism by parameterizing the SSM parameters based on the input. This allows the model to filter out irrelevant information and remember relevant information indefinitely. 

**Hardware-aware Algorithm.** This simple change poses a technical challenge for the computation of the model; in fact, all prior SSMs models must be time- and input-invariant in order to be computationally efficient. We overcome this with a hardware-aware algorithm that computes the model recurrently with a scan instead of convolution, but does not materialize the expanded state in order to avoid IO access between different levels of the GPU memory hierarchy. The resulting implementation is faster than previous methods both in theory (scaling linearly in sequence length, compared to pseudo-linear for all convolution-based SSMs) and on modern hardware (up to 3× faster on A100 GPUs).

---

[referencia=d001ef8922253622 score=0.004]
### **4.1 Synthetic Tasks** 

Full experiment details for these tasks including task details and training protocol are in Appendix E.1. 

#### **4.1.1 Selective Copying** 

The Copying task is one of the most well-studied synthetic tasks for sequence modeling, originally designed to test the memorization abilities of recurrent models. As discussed in Section 3.1, LTI SSMs (linear recurrences and global convolutions) can easily solve this task by only keeping track of time instead of reasoning about the data; for example, by constructing a convolution kernel of exactly the right length (Figure 2). This was explicitly validated in earlier work on global convolutions (Romero et al. 2021). The Selective Copying task prevents this shortcut by randomizing the spacing between tokens. Note that this task has been introduced before as the Denoising task (Jing et al. 2019). 

Note that many previous works argue that adding architecture gating (multiplicative interactions) can endow models with “data-dependence” and solve related tasks (Dao, Fu, Saab, et al. 2023; Poli et al. 2023). However, we find this explanation insufficient intuitively because such gating does not interact along the sequence axis, and cannot affect the spacing between tokens. In particular architecture gating is not an instance of a selection mechanism (Appendix A). 

Table 1 confirms that gated architectures such as H3 and Mamba only partially improve performance, while the selection mechanism (modifying S4 to S6) easily solves this task, particularly when combined with these more powerful architectures.

---

[referencia=d001ef8922253622 score=0.003]
Instead, we view it as most closely related to the gating mechanism of traditional RNNs, which is a special case (Theorem 1) and also has a deeper history of connections to SSMs through variable (input-dependent) discretization of Δ (Funahashi and Nakamura 1993; Gu, Dao, et al. 2020; Tallec and Ollivier 2018). We also eschew the term “gating” in favor of _selection_ to clarify the overloaded use of former. More narrowly, we use selection to refer to the _mechanistic_ action of a model to select or ignore inputs and facilitate data interaction along the sequence length (Section 3.1). Beyond selective SSMs and gated RNNs, other examples may include input-dependent convolutions (Kosma, Nikolentzos, and Vazirgiannis 2023; Lioutas and Guo 2020; Lutati, Zimerman, and Wolf 2023; Yang et al. 2019) and even attention.

---

[referencia=d001ef8922253622 score=0.002]
|Model|Token.|Pile<br>ppl↓|LAMBADA<br>ppl↓|LAMBADA<br>acc↑|HellaSwag<br>acc↑|PIQA<br>acc↑|Arc-E<br>acc↑|Arc-C<br>acc↑|WinoGrande<br>acc↑|Average<br>acc↑|
|---|---|---|---|---|---|---|---|---|---|---|
|Hybrid H3-130M|GPT2|—|89.48|25.77|31.7|64.2|44.4|24.2|50.6|40.1|
|Pythia-160M|NeoX|29.64|38.10|33.0|30.2|61.4|43.2|24.1|**51.9**|40.6|
|**Mamba-130M**|NeoX|**10.56**|**16.07**|**44.3**|**35.3**|**64.5**|**48.0**|**24.3**|**51.9**|**44.7**|
|Hybrid H3-360M|GPT2|—|12.58|48.0|41.5|68.1|51.4|24.7|54.1|48.0|
|Pythia-410M|NeoX|9.95|10.84|51.4|40.6|66.9|52.1|24.6|53.8|48.2|
|**Mamba-370M**|NeoX|**8.28**|**8.14**|**55.6**|**46.5**|**69.5**|**55.1**|**28.0**|**55.3**|**50.0**|
|Pythia-1B|NeoX|7.82|7.92|56.1|47.2|70.7|57.0|27.1|53.5|51.9|

---

[referencia=d001ef8922253622 score=0.002]
Finally, we must also avoid saving the intermediate states, which are necessary for backpropagation. We carefully apply the classic technique of recomputation to reduce the memory requirements: the intermediate states are not stored but recomputed in the backward pass when the inputs are loaded from HBM to SRAM. As a result, the fused selective scan layer has the same memory requirements as an optimized transformer implementation with FlashAttention. 

Details of the fused kernel and recomputation are in Appendix D. The full Selective SSM layer and algorithm is illustrated in Figure 1.

---

[referencia=d001ef8922253622 score=0.002]
## **A Discussion: Selection Mechanism** 

Our selection mechanism is inspired by and related to concepts such as gating, hypernetworks, and data-dependence. It can also be viewed as related to “fast weights” (J. Ba et al. 2016; Schmidhuber 1992), which connects classical RNNs with the mechanism of linear attention (Schlag, Irie, and Schmidhuber 2021). However, we believe that it is a distinct concept that is worth clarifying. 

**Gating.** Gating originally referred to the gating mechanisms of RNNs such as the LSTM (Hochreiter and Schmidhuber 1997) and GRU (J. Chung et al. 2014), or the gated equation (5) in Theorem 1. This was interpreted as a particular mechanism for controlling whether to let an input into the hidden state of an RNN. In particular, this affects the propagation of signal through time and causes inputs to interact along the sequence length dimension. 

However, the concept of gating has since been relaxed in popular usage to simply mean any multiplicative interaction (often with an activation function). For example, _elementwise_ multiplicative components of neural network architectures (that do not interact along sequence length) are now commonly referred to as gated architectures (Hua et al. 2022; Mehta et al. 2023), despite a very different meaning than the original RNN sense. Thus we believe the original concept of _RNN gating_ versus the popular usage of _multiplicative gating_ actually have a very different semantic meaning. 

**Hypernetworks.** Hypernetworks refer to neural networks whose parameters are themselves generated by smaller neural networks. The original idea (Ha, Dai, and Quoc V. Le 2017) used it in a narrow sense to define a large RNN whose recurrent parameters are generated by a smaller RNN, and other variants have been around for a long time (Schmidhuber 1992). 

**Data-dependence.** Similar to hypernetworks, data-dependence can refer to any notion where some parameters of the model depend on the data (Poli et al. 2023).

---

[referencia=d001ef8922253622 score=0.001]
### **3.2 Improving SSMs with Selection** 

One method of incorporating a selection mechanism into models is by letting their parameters that affect interactions along the sequence (e.g. the recurrent dynamics of an RNN or the convolution kernel of a CNN) be input-dependent. 

Algorithms 1 and 2 illustrates the main selection mechanism that we use. The main difference is simply making several parameters Δ _, 𝑩, 𝑪_ functions of the input, along with the associated changes to tensor shapes throughout. In particular, we highlight that these parameters now have a length dimension _𝐿_ , meaning that the model has changed from time-invariant to time-varying. (Note that shape annotations were described in Section 2.) This loses the equivalence to convolutions (3) with implications for its efficiency, discussed next. 

We specifically choose _𝑠𝐵_ ( _𝑥_ ) = Linear _𝑁_ ( _𝑥_ ), _𝑠𝐶_ ( _𝑥_ ) = Linear _𝑁_ ( _𝑥_ ), _𝑠_ Δ ( _𝑥_ ) = Broadcast _𝐷_ (Linear1( _𝑥_ )), and _𝜏_ Δ = softplus, where Linear _𝑑_ is a parameterized projection to dimension _𝑑_ . The choice of _𝑠_ Δ and _𝜏_ Δ is due to a connection to RNN gating mechanisms explained in Section 3.5. 

5 



<!-- Start of picture text -->
Copying Selective Copying<br>Output Output<br>Input Input<br>Solution Induction Heads<br>Perfectly solved by LTI (e.g. convolutional) models that do not need to look at the actual inputs ?<br><!-- End of picture text -->

Figure 2: ( _Left_ ) The standard version of the Copying task involves constant spacing between input and output elements and is easily solved by time-invariant models such as linear recurrences and global convolutions. ( _Right Top_ ) The Selective Copying task has random spacing in between inputs and requires time-varying models that can _selectively_ remember or ignore inputs depending on their content. ( _Right Bottom_ ) The Induction Heads task is an example of associative recall that requires retrieving an answer based on context, a key ability for LLMs.

---

[referencia=d001ef8922253622 score=0.001]
|**Algorithm 1**SSM (S4)|**Algorithm 2**SSM + Selection (S6)|
|---|---|
|**Input:** _𝑥_: (B_,_L_,_D)|**Input:** _𝑥_: (B_,_L_,_D)|
|**Output:** _𝑦_: (B_,_L_,_D)|**Output:** _𝑦_: (B_,_L_,_D)|
|1: _𝑨_: (D_,_N) ←Parameter|1: _𝑨_: (D_,_N) ←Parameter|
|_⊲_Represents structured|_𝑁_×_𝑁_matrix<br>_⊲_Represents structured_𝑁_×_𝑁_matrix|
|2: _𝑩_: (D_,_N) ←Parameter|2: _𝑩_: (B_,_L_,_N) ←_𝑠𝐵_(_𝑥_)|
|3: _𝑪_: (D_,_N) ←Parameter|3: _𝑪_: (B_,_L_,_N) ←_𝑠𝐶_(_𝑥_)|
|4: Δ: (D) ←_𝜏_Δ(Parameter)|4: Δ: (B_,_L_,_D) ←_𝜏_Δ(Parameter+_𝑠_Δ(_𝑥_))|
|5:<br>_𝑨,_<br>_𝑩_: (D_,_N) ←discretize(Δ_, 𝑨, 𝑩_)|5:<br>_𝑨,_<br>_𝑩_: (B_,_L_,_D_,_N) ←discretize(Δ_, 𝑨, 𝑩_)|
|6: _𝑦_←SSM(<br>_𝑨,_<br>_𝑩, 𝑪_)(_𝑥_)|6: _𝑦_←SSM(<br>_𝑨,_<br>_𝑩, 𝑪_)(_𝑥_)|
|_⊲_Time-invariant: recurrence o|r convolution<br>_⊲_Time-varying: recurrence (_scan_) only|

---

[referencia=d001ef8922253622 score=0.001]
## **D Hardware-aware Algorithm For Selective SSMs** 

Without input-dependent selectivity, SSMs can be efficiently implemented as a convolution (Dao, Fu, Saab, et al. 2023; Gu, Goel, and Ré 2022), which leverages the fast Fourier transform (FFT) as primitive. With selectivity, SSMs are no-longer equivalent to convolution, but we leverage the parallel associative scan. While SSM scans are theoretically efficient ( _𝑂_ ( _𝐵𝐿𝐷𝑁_ ) FLOPs, scaling linear in _𝐿_ ), training foundation models with selective SSMs requires them to be efficient on modern hardware (GPUs) as well. We describe how we use _kernel fusion_ and _recomputation_ to make SSM scan fast and memory-efficient. We evaluate the speed of our scan implementation compared to convolution and attention in Section 4.5, showing that it is up to 7× times faster than attention at sequence length 32K, and is as memory-efficient as the best attention implementation (FlashAttention). 

**Speed.** On modern hardware accelerators (GPUs) most operations (except matrix multiply) are bounded by memorybandwidth (Dao, Fu, Ermon, et al. 2022; Ivanov et al. 2021; Williams, Waterman, and Patterson 2009). This the case with our scan operation, and we use kernel fusion to reduce the amount of memory IOs, leading to significant speedup compared to a standard implementation.

---

[referencia=d001ef8922253622 score=0.001]
|SelectiveΔ|Selective_𝑩_|Selective_𝑪_|Perplexity||||
|---|---|---|---|---|---|---|
|✗|✗|✗|10.93|_𝑨𝑛_Initialization|Field|Perplexity|
|✗|✓|✗|10.15|_𝑨𝑛_=−<sup>1</sup><br>2 <sup>+</sup><sup>_𝑛𝑖_</sup>|Complex|9.16|
|✗|✗|✓|9.98|_𝑨𝑛_=−1/2|Real|8.85|
|✓|✗|✗|9.81|_𝑨𝑛_=−(_𝑛_+1)|Real|8.71|
|✓|✓|✓|8.71|_𝑨𝑛_∼exp(N (0_,_1))|Real|8.71|



- The Mamba architecture performs similarly to the H3 architecture (and seems slightly better when using a selective layer). 

We also investigate interleaving the Mamba block with other blocks such as MLP (a traditional architecture) MHA (a hybrid attention architecture) in Appendix E.2.2.

---

[referencia=d001ef8922253622 score=0.001]
### **4.6 Model Ablations** 

We perform a series of detailed ablations on components of our model, focusing on the setting of language modeling with size ≈ 350M models at Chinchilla token counts (same setting as Figure 4).

---

[referencia=d001ef8922253622 score=0.001]
- [23] DeepSound. _SampleRNN_ . https://github.com/deepsound-project/samplernn-pytorch. 2017. [24] Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, and Furu Wei. “LongNet: Scaling Transformers to 1,000,000,000 Tokens”. In: _arXiv preprint arXiv:2307.02486_ (2023). 

18

---

[referencia=d001ef8922253622 score=0.001]
**Data-dependence.** Similar to hypernetworks, data-dependence can refer to any notion where some parameters of the model depend on the data (Poli et al. 2023). 

**Example: GLU Activation.** To illustrate the issues with these concepts, consider a simple diagonal linear layer _𝑦_ = _𝑫𝑥_ , where _𝑫_ is a diagonal weight parameter. Now suppose that _𝑫_ is itself generated from a linear transformation of _𝑥_ , with an optional nonlinearity: _𝑫_ = _𝜎_ ( _𝑾𝑥_ ). Since it is diagonal, the multiplication becomes an elementwise product: _𝑦_ = _𝜎_ ( _𝑾𝑥_ ) ◦ _𝑥_ . 

This is a rather trivial transformation, yet it technically satisfies the common meanings of gating (since it has a multiplicative “branch”), hypernetworks (since the parameter _𝑫_ is generated by another layer), and data-dependent (since _𝑫_ depends on the data _𝑥_ ). However, this in fact simply defines a GLU function, which is so simple that it is often considered just an activation function (Dauphin et al. 2017; Shazeer 2020) instead of a meaningful layer. 

**Selection.** Thus, while selection mechanisms could be considered a special case of ideas such as architectural gating, hypernetworks, or data-dependence, so can an enormous range of other constructions—essentially anything with a multiplication, including standard attention mechanisms (Bahdanau, Cho, and Bengio 2015; Vaswani et al. 2017) as well—and we find it uninformative to think of them as such.