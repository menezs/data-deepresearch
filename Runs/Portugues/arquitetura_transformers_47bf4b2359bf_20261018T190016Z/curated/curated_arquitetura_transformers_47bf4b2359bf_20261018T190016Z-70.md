[referencia=db62100d4f40075e score=0.445]
## 3 REVERSIBLE TRANSFORMER 

As the above section shows, the complexity of attention can be reduced from square in length to linear, provided an approximation is acceptable. But it is clear from Table 1 that each field starts with a _b · nh · l_ term: the _b · nh · l · dk_ , or alternatively _b · l · dmodel_ cost cannot be avoided. Indeed, the activations before each layer are already of the size _b · l · dmodel_ , so the memory use of the whole model with _nl_ layers is at least _b · l · dmodel · nl_ . Even worse: inside the feed-forward layers of Transformer this goes up to _b · l · dff · nl_ . In a big Transformer it is usual to set _dff_ = 4 _K_ and _nl_ = 16 so with _l_ = 64 _K_ this again would use an impractical 16 _GB_ of memory 

In this section, we show how to reduce this cost by first dealing with the _nl_ part of the term using reversible layers and then showing how chunking can allow us to handle the _dff_ problem. The effects of each of these approaches on memory and time complexity are summarized in Table 3. 

**RevNets.** Reversible residual networks were introduced by Gomez et al. (2017) where it was shown that they can replace ResNets for image classification. The main idea is to allow the activations at any given layer to be recovered from the activations at the following layer, using only the model parameters. Rather than having to checkpoint intermediate values for use in the backward pass, layers can be reversed one-by-one as back-propagation proceeds from the output of the network to its input. Whereas a normal residual layer performs a function _x �→ y_ that operates on a single input and produces a single output and has the form _y_ = _x_ + _F_ ( _x_ ), a reversible layer works on pairs of inputs/outputs: ( _x_ 1 _, x_ 2) _�→_ ( _y_ 1 _, y_ 2), and follows the equations: 



A layer can be reversed by subtracting (rather than adding) the residuals:

---

[referencia=db62100d4f40075e score=0.400]
The above estimate includes only per-layer memory and input activations cost and does not take into account the following major sources of memory use in the Transformer. 

- Memory in a model with _N_ layers is _N_ -times larger than in a single-layer model due to the fact that activations need to be stored for back-propagation. 

- Since the depth _dff_ of intermediate feed-forward layers is often much larger than the depth _dmodel_ of attention activations, it accounts for a large fraction of memory use. 

- Attention on sequences of length _L_ is O( _L_<sup>2</sup> ) in both computational and memory complexity, so even for a single sequence of 64K tokens can exhaust accelerator memory. 

> _∗_ Equal Contribution 

> 1https://hackingsemantics.xyz/2019/leaderboards/ 

1 

Published as a conference paper at ICLR 2020 

We introduce the Reformer model which solves these problems using the following techniques: 

- Reversible layers, first introduced in Gomez et al. (2017), enable storing only a single copy of activations in the whole model, so the _N_ factor disappears. 

- Splitting activations inside feed-forward layers and processing them in chunks removes the _dff_ factor and saves memory inside feed-forward layers. 

- Approximate attention computation based on locality-sensitive hashing replaces the O( _L_<sup>2</sup> ) factor in attention layers with O( _L_ log _L_ ) and so allows operating on long sequences. 

We study these techniques and show that they have negligible impact on the training process compared to the standard Transformer. Splitting activations in fact only affects the implementation; it is numerically identical to the layers used in the Transformer. Applying reversible residuals instead of the standard ones does change the model but has a negligible effect on training in all configurations we experimented with. Finally, locality-sensitive hashing in attention is a more major change that can influence the training dynamics, depending on the number of concurrent hashes used. We study this parameter and find a value which is both efficient to use and yields results very close to full attention.

---

[referencia=db62100d4f40075e score=0.214]
- Antoine Bordes, Nicolas Usunier, Sumit Chopra, and Jason Weston. Large-scale simple question answering with memory networks. _CoRR_ , abs/1506.02075, 2015. URL http://arxiv.org/ abs/1506.02075. 

- Sarath Chandar, Sungjin Ahn, Hugo Larochelle, Pascal Vincent, Gerald Tesauro, and Yoshua Bengio. Hierarchical memory networks. _arXiv preprint arXiv:1605.07427_ , 2016. 

- Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. _URL https://openai.com/blog/sparse-transformers_ , 2019. 

- Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: pre-training of deep bidirectional transformers for language understanding. _CoRR_ , abs/1810.04805, 2018. URL http://arxiv.org/abs/1810.04805. 

- Aidan N Gomez, Mengye Ren, Raquel Urtasun, and Roger B Grosse. The reversible residual network: Backpropagation without storing activations. In _Advances in neural information processing systems_ , pp. 2214–2224, 2017. 

- Felix Hill, Antoine Bordes, Sumit Chopra, and Jason Weston. The goldilocks principle: Reading children’s books with explicit memory representations. _CoRR_ , abs/1511.02301, 2015. URL http://arxiv.org/abs/1511.02301. 

- Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Noam Shazeer, Curtis Hawthorne, Andrew M Dai, Matthew D Hoffman, and Douglas Eck. Music transformer: Generating music with long-term structure. _arXiv preprint arXiv:1809.04281_ , 2018. 

- Guillaume Lample, Alexandre Sablayrolles, Marc’Aurelio Ranzato, Ludovic Denoyer, and Herv´e J´egou. Large memory layers with product keys. _CoRR_ , abs/1907.05242, 2019. URL http: //arxiv.org/abs/1907.05242.

---

[referencia=db62100d4f40075e score=0.125]
# REFORMER: THE EFFICIENT TRANSFORMER 

### **Nikita Kitaev**<sup>_∗_</sup> 

U.C. Berkeley & Google Research kitaev@cs.berkeley.edu 

**Łukasz Kaiser**<sup>_∗_</sup> **Anselm Levskaya** Google Research Google Research _{_ lukaszkaiser,levskaya _}_ @google.com 

## ABSTRACT 

Large Transformer models routinely achieve state-of-the-art results on a number of tasks but training these models can be prohibitively costly, especially on long sequences. We introduce two techniques to improve the efficiency of Transformers. For one, we replace dot-product attention by one that uses locality-sensitive hashing, changing its complexity from O( _L_<sup>2</sup> ) to O( _L_ log _L_ ), where _L_ is the length of the sequence. Furthermore, we use reversible residual layers instead of the standard residuals, which allows storing activations only once in the training process instead of _N_ times, where _N_ is the number of layers. The resulting model, the Reformer, performs on par with Transformer models while being much more memory-efficient and much faster on long sequences.

---

[referencia=db62100d4f40075e score=0.042]
A layer can be reversed by subtracting (rather than adding) the residuals: 



**Reversible Transformer.** We apply the RevNet idea to the Transformer by combining the attention and feed-forward layers inside the revnet block. In the notation above, F becomes an attention layer while G becomes the feed-forward layer. Note that Layer Normalization (Ba et al., 2016) is moved inside the residual blocks. 



The reversible Transformer does not need to store activations in each layer and so gets rid of the _nl_ term. In Section 5 we show that it performs the same as the normal Transformer when using the same number of parameters; we achieve this by having both _x_ 1 and _x_ 2 have size _dmodel_ . 

**Chunking.** While reversibility covers the _nl_ term, the thicker layers can still use a lot of memory. The feed-forward layer in particular can use intermediate vectors of dimensionality _dff_ = 4 _K_ or higher. However, computations in feed-forward layers are completely independent across positions in a sequence, so the computation can be split into _c_ chunks: 



This layer is typically batched by performing operations for all positions in parallel, but operating on one chunk at a time can reduce memory. The reverse computation in (8) and the backward pass are also chunked. In addition to the feed-forward layers, for models with large vocabulary (more than _dmodel_ word types) we also chunk the log-probabilities at the output and calculate the loss for sections of the sequence at a time. 

**Chunking, large batches and parameter reuse.** With chunking and reversible layers the memory we use for activations in the whole network is independent of the number of layers. The same is not true for parameters though as their number grows with the number of layers. This problem is remedied though because we can swap layer parameters to and from CPU memory when this layer is not computing. In a standard Transformer this would be inefficient because memory transfer to CPU is slow. The batch size multiplied by length in Reformer is much larger though and therefore the amount of compute done with the parameters amortizes the cost of their transfer. 

6 

Published as a conference paper at ICLR 2020

---

[referencia=db62100d4f40075e score=0.004]
**Reversible layers in machine translation.** We also evaluate reversible layers in the context of an encoder-decoder Transformer model for machine translation from English to German. We start by making both the encoder and the decoder fully reversible in the Transformer-base architecture, and 

> 2https://github.com/google/trax/tree/master/trax/models/reformer 

> 3 BLEU+case.lc+lang.en-de+numrefs.1+smooth.exp+test.wmt14/full+tok.intl+version.1.4.3 

> 4 BLEU+case.mixed+lang.en-de+numrefs.1+smooth.exp+test.wmt14/full+tok.intl+version.1.4.3 

8 

Published as a conference paper at ICLR 2020 



Figure 4: LSH attention performance as a function of hashing rounds on imagenet64. 



Figure 5: Left: LSH attention performance as a function of number of layers on enwik8. Right: Speed of attention evaluation as a function of input length for full- and LSH- attention. 

see that the resulting model performs comparably to Vaswani et al. (2017) when trained for 100K steps. We also evaluate training for a greater number of steps and with a larger model. Reformer models are very memory-efficient, so for the latter two experiments we do not need to save memory by sharing embedding and output projection weight matrices throughout the model. Results are shown in Table 4. We do not apply LSH attention in this setting because examples are single sentences, and sentences tend to be relatively short. Our typical LSH attention configuration uses chunks of 128 tokens after hashing and sorting, whereas the examples in the WMT14 test set are all shorter than 128 tokens.

---

[referencia=db62100d4f40075e score=0.003]
## 5 EXPERIMENTS 

In this section we present experimental results demonstrating the techniques described above. We analyze the techniques one-by-one to make clear which combinations have impact on performance. We start by showing that reversible layers and shared query-key spaces do not impact performance, then proceed to analyze hashing attention and finally the full Reformer model. 

We ran our experiments on the imagenet64 and enwik8-64K tasks, where the latter is a variant of enwik8 that is chunked into subsequences of 2<sup>16</sup> = 64 _K_ tokens. We use 3-layer models for our ablations so as to make it tractable to compare with the regular Transformer, which has high memory usage and performs full _O_ ( _l_<sup>2</sup> ) attention. All experiments have _dmodel_ = 1024, _dff_ = 4096, _nheads_ = 8, and a total batch size of 8 sequences. We used the Adafactor optimizer (Shazeer & Stern, 2018) for training these models. We also evaluate on the WMT 2014 English-to-German translation task, following the hyperparameters of Vaswani et al. (2017). Training for all experiments 

7 

Published as a conference paper at ICLR 2020 



Figure 3: Effect of shared query-key space (left) and reversibility (right) on performance on enwik8 and imagenet64 training. The curves show bits per dim on held-out data. 

Table 4: BLEU scores on newstest2014 for WMT English-German (EnDe). We additionally report detokenized BLEU scores as computed by sacreBLEU (Post, 2018).

---

[referencia=db62100d4f40075e score=0.002]
Table 4: BLEU scores on newstest2014 for WMT English-German (EnDe). We additionally report detokenized BLEU scores as computed by sacreBLEU (Post, 2018). 

|Model|BLEU|_sacreB_<br>_Uncased_<sup>3</sup>|_LEU_<br>_Cased_<sup>4</sup>|
|---|---|---|---|
|Vaswani et al. (2017), base model|27.3|||
|Vaswani et al. (2017), big|28.4|||
|Ott et al.(2018),big|29.3|||
|Reversible Transformer (base, 100K steps)|27.6|_27.4_|_26.9_|
|Reversible Transformer (base, 500K steps, no weight sharing)|28.0|_27.9_|_27.4_|
|Reversible Transformer (big, 300K steps, no weight sharing)|29.1|_28.9_|_28.4_|



was parallelized across 8 devices (8 GPUs or 8 TPU v3 cores). Code for training our models is made publicly available.<sup>2</sup> 

**Effect of sharing QK.** We first consider the effect of shared-QK attention on a regular Transformer model. Shared-QK attention sets _kj_ = _∥qqjj ∥_<sup>andpreventstokensfromattendingtothemselves</sup> (except when no other context is available). In the left part of Figure 3, we plot perplexity curves for both regular and shared-QK attention. A shared query-key space does not perform worse than regular attention; in fact, for enwik8 it appears to train slightly faster. In other words, we are not sacrificing accuracy by switching to shared-QK attention. 

**Effect of reversible layers.** In the two plots on the right in Figure 3, we compare a regular Transformer per Vaswani et al. (2017) with the reversible one describe in Section 3. The two models have identical parameter counts, and the learning curves likewise appear to be nearly the same. These results show that the memory savings in the reversible Transformer do not come at the expense of accuracy.

---

[referencia=db62100d4f40075e score=0.001]
6 

Published as a conference paper at ICLR 2020 

Table 3: Memory and time complexity of Transformer variants. We write _dmodel_ and _dff_ for model depth and assume _dff ≥ dmodel_ ; _b_ stands for batch size, _l_ for length, _nl_ for the number of layers. We assume _nc_ = _l/_ 32 so 4 _l/nc_ = 128 and we write _c_ = 128<sup>2</sup> . 

|Model Type|MemoryComplexity<br>|Time Complexity<br>|
|---|---|---|
|Transformer|max(_bldff, bnhl_<sup>2</sup>)_nl_<br>|(_bldff_ +_bnhl_<sup>2</sup>)_nl_<br>|
|Reversible Transformer|max(_bldff, bnhl_<sup>2</sup>)<br>|(_bnhldff_ +_bnhl_<sup>2</sup>)_nl_<br>|
|Chunked Reversible Transformer|max(_bldmodel, bnhl_<sup>2</sup>)|(_bnhldff_ +_bnhl_<sup>2</sup>)_nl_|
|LSH Transformer|max(_bldff, bnhlnrc_)_nl_|(_bldff_ +_bnhnrlc_)_nl_|
|Reformer|max(_bldmodel, bnhlnrc_)|(_bldff_ +_bnhnrlc_)_nl_|

---

[referencia=db62100d4f40075e score=0.000]
Table 2: Accuracies on the duplication task of a 1-layer Transformer model with full attention and with locality-sensitive hashing attention using different number of parallel hashes. 

|Train<br>Eval|Full Attention|LSH-8|LSH-4|LSH-2|LSH-1|
|---|---|---|---|---|---|
|Full Attention|100%|94.8%|92.5%|76.9%|52.5%|
|LSH-4|0.8%|100%|99.9%|99.4%|91.9%|
|LSH-2|0.8%|100%|99.9%|98.1%|86.8%|
|LSH-1|0.8%|99.9%|99.6%|94.8%|77.9%|



While attention to the future is not allowed, typical implementations of the Transformer _do_ allow a position to attend to _itself_ . Such behavior is undesirable in a shared-QK formulation because the dot-product of a query vector with itself will almost always be greater than the dot product of a query vector with a vector at another position. We therefore modify the masking to forbid a token from attending to itself, except in situations where a token has no other valid attention targets (e.g. the first token in a sequence).

---

[referencia=db62100d4f40075e score=0.000]
**Memory-efficient attention.** To calculate the memory use of the attention mechanism, let us focus on the attention computation from Equation 1. Let us assume that Q, K and V all have the shape [ _batch_ _~~s~~ ize, length, dmodel_ ]. The main issue is the term _QK_<sup>_T_</sup> , which has the shape [ _batch_ _~~s~~ ize, length, length_ ]. In the experimental section we train a model on sequences of length 64 _K_ – in this case, even at batch-size of 1, this is a 64 _K ×_ 64 _K_ matrix, which in 32-bit floats would take 16GB of memory. This is impractical and has hindered the use of the Transformer for long sequences. But it is important to note that the _QK_<sup>_T_</sup> matrix does not need to be fully materialized in memory. The attention can indeed be computed for each query _qi_ separately, only calculating softmax(<sup>_<u>q</u>_</sup> _~~√~~_<sup>_<u>iK</u>_</sup> _dk_<sup>_T_)</sup><sup>_V_once in memory, and then re-computing it on the backward pass when needed for</sup> gradients. This way of computing attention may be less efficient but it only uses memory proportional to _length_ . We use this memory-efficient implementation of attention to run the full-attention baselines presented in the experimental section. 

**Where do Q, K, V come from?** The multi-head attention described above operates on keys, queries and values, but usually we are only given a single tensor of activations A of the shape [ _batch_ _~~s~~ ize, length, dmodel_ ] – e.g., coming from embedding the tokens in a sentence into vectors. 

2 

Published as a conference paper at ICLR 2020 



Figure 1: An angular locality sensitive hash uses random rotations of spherically projected points to establish buckets by an argmax over signed axes projections. In this highly simplified 2D depiction, two points _x_ and _y_ are unlikely to share the same hash buckets (above) for the three different angular hashes unless their spherical projections are close to one another (below).

---

[referencia=db62100d4f40075e score=0.000]
## REFERENCES 

Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, and Llion Jones. Character-level language modeling with deeper self-attention. _CoRR_ , abs/1808.04444, 2018. URL http: //arxiv.org/abs/1808.04444. 

- Alexandr Andoni, Piotr Indyk, Thijs Laarhoven, Ilya P. Razenshteyn, and Ludwig Schmidt. Practical and optimal LSH for angular distance. _CoRR_ , abs/1509.02897, 2015. URL http://arxiv. org/abs/1509.02897. 

Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. URL http://arxiv.org/abs/1607.06450.

---

[referencia=db62100d4f40075e score=0.000]
The multi-round case essentially involves performing LSH attention _nrounds_ times in parallel; the details of the procedure are described in in Appendix A. 

**Causal masking for shared-QK attention.** In a Transformer decoder, masking (denoted by _m_ ( _j, Pi_ ) in Equation 3) is used to prevent positions from attending into the future. To implement masking in LSH attention, we associate every query/key vector with a position index, re-order the position indices using the same permutations used to sort the query/key vectors, and then use a comparison operation to compute the mask. 

4 

Published as a conference paper at ICLR 2020 

Table 1: Memory and time complexity of attention variants. We write _l_ for length, _b_ for batch size, _nh_ for the number of heads, _nc_ for the number of LSH chunks, _nr_ for the number of hash repetitions. 

|Attention Type|MemoryComplexity<br>|Time Complexity<br>|
|---|---|---|
|Scaled Dot-Product|max(_bnhldk, bnhl_<sup>2</sup>)<br>|max(_bnhldk, bnhl_<sup>2</sup>)<br>|
|Memory-Effcient|max(_bnhldk, bnhl_<sup>2</sup>)<br>|max(_bnhldk, bnhl_<sup>2</sup>)<br>|
|LSH Attention|max(_bnhldk, bnhlnr_(4_l/nc_)<sup>2</sup>)|max(_bnhldk, bnhnrl_(4_l/nc_)<sup>2</sup>)|



Table 2: Accuracies on the duplication task of a 1-layer Transformer model with full attention and with locality-sensitive hashing attention using different number of parallel hashes.

---

[referencia=db62100d4f40075e score=0.000]
We achieve this by employing random projections as follows (see Figure 1). To get _b_ hashes, we first fix a random matrix _R_ of size [ _dk, b/_ 2]. We then define _h_ ( _x_ ) = arg max([ _xR_ ; _−xR_ ]) where [ _u_ ; _v_ ] denotes the concatenation of two vectors. This method is a known LSH scheme (Andoni et al., 2015) and is easy to implement and apply to batches of vectors. 

**LSH attention.** Knowing our LSH scheme and the general idea of hashing attention, we will now formalize the LSH attention we use in this paper. We first rewrite the equation for normal attention, (1), for a single query position _i_ at a time: 



We introduce the notation _Pi_ to represent the set that the query at position _i_ attends to, and _z_ to denote the partition function (i.e. the normalizing term in the softmax). For clarity, we also omit scaling by<sup>_√_</sup> _dk_ . 

For batching purposes we typically perform attention over a larger set _P_<sup>�</sup> _i_ = _{_ 0 _,_ 1 _, . . . , l} ⊇Pi_ while masking out elements not in _Pi_ : 



3 

Published as a conference paper at ICLR 2020 



Figure 2: Simplified depiction of LSH Attention showing the hash-bucketing, sorting, and chunking steps and the resulting causal attentions. (a-d) Attention matrices for these varieties of attention. 

Now we turn to LSH attention, which we can think of in terms of restricting the set _Pi_ of target items a query position _i_ can attend to, by only allowing attention within a single hash bucket. 



Figure 2(a-b) shows a schematic comparison of full-attention with a hashed variant. Part (a) depicts that the attention matrix for full attention is typically sparse, but the computation does not take advantage of this sparsity. In (b), the queries and keys have been sorted according to their hash bucket. Since similar items fall in the same bucket with high probability, the full attention pattern can be approximated by only allowing attention within each bucket.

---

[referencia=db62100d4f40075e score=0.000]
**LSH attention in Transformer.** LSH attention is an approximation for full attention that, as evidenced in Figure 4, becomes more accurate as the number of hashes increases. At _nrounds_ = 8, it already almost matches full attention. The computational cost of a model grows with the number of hashes, so this hyperparameter can be adjusted depending on the available compute budget. Additionally, as in Table 2, the number of hashes can be increased at evaluation time to produce more accurate results. On the right half of Figure 5, we plot the speed of different attention types vs. the sequence length, while holding the total number of tokens fixed. We see that while regular attention becomes slower at longer sequence length, LSH attention speed remains flat. 

**Large Reformer models.** To verify that the Reformer can indeed fit large models on a single core and train fast on long sequences, we train up to 20-layer big Reformers on enwik8 and imagenet64. As can be seen in Figure 5, these models fit into memory and train. We were not able to train Transformer baselines in this case as they are too slow and memory-hungry, but we see clear improvement with the number of layers. A 12-layer model on enwik8 trained for 20K steps with a dropout rate of 0.1 achieves 1.19 bits/dim on the test set. We also trained a 12-layer Reformer model for longer with further tuning and improvements and we reached 1.05 bits/dim on the enwiki8 test set. 

9 

Published as a conference paper at ICLR 2020 

## 6 CONCLUSION 

Reformer combines the modeling capacity of a Transformer with an architecture that can be executed efficiently on long sequences and with small memory use even for models with a large number of layers. We believe that this will help large, richly-parameterized Transformer models become more widespread and accessible. Also, the ability to handle long sequences opens the way for the use of the Reformer on many generative tasks. In addition to generating very long coherent text, the Reformer can bring the power of Transformer models to other domains like time-series forecasting, music, image and video generation.

---

[referencia=db62100d4f40075e score=0.000]
## 4 RELATED WORK 

The Transformer model introduced in (Vaswani et al., 2017) has been used widely in natural language tasks and further extended to model diverse data such as music scores (Huang et al., 2018), and images (Parmar et al., 2018; Ramachandran et al., 2019). Most notably, this model class has been applied successfully in the self-supervised training of extremely large language models (Devlin et al., 2018; Radford et al., 2019). 

Given the enormous computational requirements of state of the art sequence models, there has been increasing interest in finding methods to reduce the memory footprint and computational requirements of Transformer models. In addition to standard methods such as precision reduction and gradient checkpointing (Sohoni et al., 2019), more efficient versions of the Transformer model’s self-attention mechanism (Sukhbaatar et al., 2019a;b) have also recently been explored. 

In particular, leveraging sparsity in the attention layers has proved fruitful. OpenAI introduced the sparse Transformer (Child et al., 2019) which exploits a factorized sparse representation of attention. Using product-key attention to increase the key space has also been used to reduce memory requirements in the feed-forward layers with no loss in performance (Lample et al., 2019).

---

[referencia=db62100d4f40075e score=0.000]
## A MULTI-ROUND LSH ATTENTION 

In this section we describe in more detail the multi-hash version of our LSH attention mechanism. We first repeat Equation (3) from the main text, which describes a general formulation of attention with sparsity: 



In the multi-round case, a query position _i_ can attend to key positions _Pi_ as defined in (6), which we also repeat here: 



For batching purposes, attention is performed on chunks of sorted queries/keys: 



Combining (3) and (6) gives: 



Each round of LSH attention produces a vector _o_<sup>(</sup> _i_<sup>_r_)</sup> that can be computed independently from other rounds, except for the inclusion of a term _Ni,j_ to avoid double-counting elements when constructing the union of _Pi_<sup>(</sup><sup>_r_)</sup> sets. In our implementation we fold the _Ni,j_ factor into the masking term _m_<sup>(</sup> _i,j_<sup>_r_).</sup> 

We also modify _m_<sup>(</sup> _i,j_<sup>_r_)tointroduceaspecialcasefor</sup><sup>_i_=</sup><sup>_j_.Thiscaseisaddedbecausecausal</sup> masking in a standard Transformer allows position _i_ to attend to itself, which is not desirable in a shared-QK formulation. We set the mask to a large but finite value to disallow attention-in-place, except in the situation where a token has no other valid attention targets. For example, the first token in a sequence attends only to itself, because no prior context is available. 

12

---

[referencia=db62100d4f40075e score=0.000]
- Noam Shazeer, Youlong Cheng, Niki Parmar, Dustin Tran, Ashish Vaswani, Penporn Koanantakool, Peter Hawkins, HyoukJoong Lee, Mingsheng Hong, Cliff Young, Ryan Sepassi, and Blake Hechtman. Mesh-tensorflow: Deep learning for supercomputers. _CoRR_ , abs/1811.02084, 2018. URL http://arxiv.org/abs/1811.02084. 

- Nimit Sharad Sohoni, Christopher Richard Aberger, Megan Leszczynski, Jian Zhang, and Christopher R´e. Low-memory neural network training: A technical report. _CoRR_ , abs/1904.10631, 2019. URL http://arxiv.org/abs/1904.10631. 

- Sainbayar Sukhbaatar, Edouard Grave, Piotr Bojanowski, and Armand Joulin. Adaptive attention span in transformers. _CoRR_ , abs/1905.07799, 2019a. URL http://arxiv.org/abs/ 1905.07799. 

- Sainbayar Sukhbaatar, Edouard Grave, Guillaume Lample, Herv´e J´egou, and Armand Joulin. Augmenting self-attention with persistent memory. _CoRR_ , abs/1907.01470, 2019b. URL http: //arxiv.org/abs/1907.01470. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. _CoRR_ , 2017. URL http: //arxiv.org/abs/1706.03762. 

- Jason Weston, Sumit Chopra, and Antoine Bordes. Memory networks. _CoRR_ , abs/1410.3916, 2014. URL http://arxiv.org/abs/1410.3916. 

11 

Published as a conference paper at ICLR 2020

---

[referencia=db62100d4f40075e score=0.000]
Locality-sensitive hashing (LSH) has, to our knowledge, not been directly applied to Transformer attention layers before. But previous work using external memory with neural networks has dealt with memories of large sizes. The original implementation of memory networks (Weston et al., 2014) and later work on scaling it (Bordes et al., 2015; Chandar et al., 2016) used memory with size in the millions. The cost of doing so is that the memory must be fixed prior to training. Moreover, since during the beginning of training the model is unlikely to query the memory correctly, strong supervision is used to encourage the model to query memory locations that are useful. These hints are either given as additional supervising information by the task or determined heuristically as in Hill et al. (2015). The requirement that the memory be fixed before has been removed in Santoro et al. (2016) at the cost of memory size and later alleviated by Rae et al. (2016). The last paper considered memory lookups with approximate nearest neighbors including both LSH and random kd-trees, but only for lookups in external memory.

---

[referencia=db62100d4f40075e score=0.000]
- Niki Parmar, Ashish Vaswani, Jakob Uszkoreit, Lukasz Kaiser, Noam Shazeer, and Alexander Ku. Image transformer. _CoRR_ , abs/1802.05751, 2018. URL http://arxiv.org/abs/1802. 05751. 

- Matt Post. A call for clarity in reporting BLEU scores. In _Proceedings of the Third Conference on Machine Translation: Research Papers_ , pp. 186–191, Belgium, Brussels, October 2018. Association for Computational Linguistics. URL https://www.aclweb.org/anthology/ W18-6319. 

- Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are unsupervised multitask learners. 2019. 

- Jack W Rae, Jonathan J Hunt, Tim Harley, Ivo Danihelka, Andrew Senior, Greg Wayne, Alex Graves, and Timothy P Lillicrap. Scaling memory-augmented neural networks with sparse reads and writes. In _Advances in Neural Information Processing Systems, (NIPS)_ , 2016. 

- Prajit Ramachandran, Niki Parmar, Ashish Vaswani, Irwan Bello, Anselm Levskaya, and Jonathon Shlens. Stand-alone self-attention in vision models. _CoRR_ , abs/1906.05909, 2019. URL http: //arxiv.org/abs/1906.05909. 

- Adam Santoro, Sergey Bartunov, Matthew Botvinick, Daan Wierstra, and Timothy P. Lillicrap. Oneshot learning with memory-augmented neural networks. _CoRR_ , abs/1605.06065, 2016. URL http://arxiv.org/abs/1605.06065. 

- Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. _CoRR_ , abs/1804.04235, 2018. URL http://arxiv.org/abs/1804.04235.