[referencia=a7468c6851652691 score=0.986]
### **3.2 Attention** 

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum 

3

---

[referencia=a7468c6851652691 score=0.880]
### Scaled Dot-Product Attention 



Multi-Head Attention 



Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. 

of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. **3.2.1 Scaled Dot-Product Attention** 

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension _dk_ , and values of dimension _dv_ . We compute the dot products of the 

query with all keys, divide each by<sup>_√_</sup> _dk_ , and apply a softmax function to obtain the weights on the values. 

In practice, we compute the attention function on a set of queries simultaneously, packed together 

into a matrix _Q_ . The keys and values are also packed together into matrices _K_ and _V_ . We compute the matrix of outputs as: 

Attention( _Q, K, V_ ) = softmax(<sup>_<u>QK</u>T_</sup> ) _V_ (1) _~~√~~ dk_ The two most commonly used attention functions are additive attention [2], and dot-product (multi-2], and dot-product (multi-], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dkk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. While for small values of _dk_ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of _dk_ [3]. We suspect that for large values of _dk_ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup> . To counteract this effect, we scale the dot products by _~~√~~_ <u>1</u> _dk_<sup>.</sup> **3.2.2 Multi-Head Attention**

---

[referencia=a7468c6851652691 score=0.639]
The two most commonly used attention functions are additive attention [2], and dot-product (multi-2], and dot-product (multi-], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dkk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

Instead of performing a single attention function with _d_ model-dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values _h_ times with different, learned linear projections to _dk_ , _dk_ and _dv_ dimensions, respectively. On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding _dv_ -dimensional 4To illustrate why the dot products get large, assume that the components of _q_ and _k_ are independent random variables with mean 0 and variance 1. Then their dot product, _q · k_ =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_kqiki_, has mean 0 and variance</sup><sup>_dk_.</sup> 

4 

output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2. 

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this. 

MultiHead( _Q, K, V_ ) = Concat(head1 _, ...,_ headh) _W_<sup>_O_</sup>

---

[referencia=a7468c6851652691 score=0.493]
development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3. 

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. 

In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

---

[referencia=34c4c8ee90c46400 score=0.437]
## Methods discussed and introduced

[edit]
The paper is best known for introducing the Transformer architecture, which underlies most modern large language models (LLMs).<sup>[10]</sup> A key reason why the architecture is preferred by most modern LLMs is the parallelizability of the architecture over its predecessors. This ensures that the operations necessary for training can be accelerated on a GPU, allowing both faster training times and models of bigger sizes to be trained.

The paper introduced the following mechanisms as part of the development of the transformer architecture.

### Scaled dot-product attention and self-attention

[edit]
The use of the scaled dot-product attention and self-attention mechanism instead of a recurrent neural network (RNN) or long short-term memory (which rely on recurrence) allows for better performance as described in the following paragraph. The paper described the scaled dot-product attention as follows:

where , , are respectively the query, key, value matrices, and is the dimension of the queries and keys, corresponding to the number of columns in their matrices.

Here, the softmax function is applied row-wise: let and , then the element at row and column in the matrix is calculated as

,

where is the number of columns and rows in the and matrices, respectively, corresponding to the length of the context window.

Since the model relies on Query, Key, and Value matrices that come from the same source (i.e., the input sequence or context window), this eliminates the need for RNNs, completely ensuring parallelizability for the architecture. This differs from the original form of the Attention mechanism introduced in 2014. Additionally, the paper discusses the use of an additional scaling factor that was found to be most effective with respect to the dimension of the key vectors (represented as and initially set to 64 within the paper) in the manner shown above.

---

[referencia=34c4c8ee90c46400 score=0.409]
## Background

[edit]
The authors of the paper are Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, and Illia Polosukhin. All eight authors were "equal contributors" to the paper; the listed order was randomized (according to the paper itself). After the paper, each of the authors left Google to join other companies or to found startups.<sup>[7]</sup><sup>[8]</sup>

The paper's title is a reference to the song "All You Need Is Love" by the Beatles.<sup>[9]</sup> The name "Transformer" was picked because Jakob Uszkoreit, one of the paper's authors, liked the sound of that word.<sup>[5]</sup> An early design document was titled "Transformers: Iterative Self-Attention and Processing for Various Tasks", and included an illustration of six characters from the *Transformers* franchise. The team was named Team Transformer.<sup>[9]</sup>

---

[referencia=34c4c8ee90c46400 score=0.286]
### Cross-attention

[edit]
In the specific context of translation, which the paper focused on, the Query matrix is usually represented in embeddings corresponding to the target language, while the Key and Value matrices correspond to the source language. In the paper, this form of attention is called *encoder-decoder attention*; another common name is *cross-attention*. More specifically, the authors state that “in ‘encoder-decoder attention’ layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder”. In analogy with the *seq2seq* approach (see below), the encoder hereby consumes the source language sequence, while the decoder autoregressively consumes and produces the target language sequence.

### Multi-head attention

[edit]
In the self-attention mechanism, queries (Q), keys (K), and values (V) are dynamically generated for each input sequence (typically limited by the size of the context window), allowing the model to focus on different parts of the input sequence at different steps. Multi-head attention enhances this process by introducing multiple parallel attention heads. Each attention head learns different linear projections of the Q, K, and V matrices. This allows the model to capture different aspects of the relationships between words in the sequence simultaneously, rather than focusing on a single aspect.

By doing this, multi-head attention ensures that the input embeddings are updated from a more varied and diverse set of perspectives. After the attention outputs from all heads are calculated, they are concatenated and passed through a final linear transformation to generate the output.

### Positional encoding

[edit]
Since the Transformer does not rely on recurrence or convolution of the text in order to perform encoding and decoding, the paper relied on the use of sine and cosine wave functions to encode the position of the token into the embedding. The methods introduced in the paper are discussed below:

wherein , , correspond to the position of the word, the current dimension index, and the dimension of the model, respectively. The sine function is used for even indices of the embedding while the cosine function is used for odd indices. The resultant embedding is then added to the word at that corresponding position with respect to the current context window. The paper specifically comments on why this method was chosen describing:

We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.<sup>[1]</sup>

---

[referencia=34c4c8ee90c46400 score=0.131]
## Training

[edit]
While the primary focus of the paper at the time was to improve machine translation, the paper also discussed the use of the architecture on English Constituency Parsing, both with limited and large-sized datasets, achieving a high-score without specific tuning for the task indicating the promising nature of the model for use in a wide-variety of general purpose of seq2seq tasks.

- Dataset - The English-to-German translation model was trained on the 2014 WMT (Workshop on Statistical Machine Translation) English-German dataset, consisting of nearly 4.5 million sentences derived from TED Talks and high-quality news articles. A separate translation model was trained on the much larger 2014 WMT English-French dataset, consisting of 36 million sentences. Both datasets were encoded with byte-pair encoding.

- Hardware - The models were trained using 8 NVIDIA P100 GPUs. The base models were trained for 100,000 steps, and the big models were trained for 300,000 steps - each step taking about 0.4 seconds to complete for the base models and 1.0 seconds for the big models. The base model was trained for a total of 12 hours, and the big model was trained for a total of 3.5 days. Both the base and big models outperform the 2017 state-of-the-art in both English-German and English-French, while achieving the comparatively lowest training cost.<sup>[1]</sup>

- Hyperparameters and regularization - For their 100M-parameter Transformer model, the authors increased the learning rate linearly for the first 4000 (warmup) steps and decreased it proportionally to the inverse square root of the current step number. Dropout layers were applied to the output of each sub-layer before normalization, the sums of the embeddings, and the positional encodings. The dropout rate was set to 0.1. Label smoothing was applied with a value of 0.1, which "improves accuracy and BLEU score".<sup>[1]</sup>

## See also

[edit]
## Notes

[edit]
1. ↑ Gated recurrent units (2014) further reduced its complexity.
2. ↑ Some architectures, such as RWKV (Receptance Weighted Key Value) or state space models, avoid the issue.

---

[referencia=a7468c6851652691 score=0.131]
## **Abstract** 

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 Englishto-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. 

> _∗_ Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention and started the effort to evaluate this idea. Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. 

> _†_ Work performed while at Google Brain. 

> _‡_ Work performed while at Google Research. 

31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.

---

[referencia=a7468c6851652691 score=0.117]
MultiHead( _Q, K, V_ ) = Concat(head1 _, ...,_ headh) _W_<sup>_O_</sup> 



Where the projections are parameter matrices _Wi_<sup>_Q_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_K_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_V_</sup> _∈_ R<sup>_d_model</sup><sup>_×dv_</sup> and _W_<sup>_O_</sup> _∈_ R<sup>_hdv×d_model</sup> . 

In this work we employ _h_ = 8 parallel attention layers, or heads. For each of these we use _dk_ = _dv_ = _d_ model _/h_ = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality. 

### **3.2.3 Applications of Attention in our Model** 

The Transformer uses multi-head attention in three different ways: 

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. 

- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2.

---

[referencia=a7468c6851652691 score=0.081]
### **6.3 English Constituency Parsing** 

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. 

We trained a 4-layer transformer with _dmodel_ = 1024 on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting. 

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we 

9 

Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)

---

[referencia=34c4c8ee90c46400 score=0.063]
In 2016, Google Translate was revamped to Google Neural Machine Translation, which replaced the previous model based on statistical machine translation. The GNMT system was a sequence-to-sequence model with eight LSTM layers in its encoder and eight in its decoder. The first encoder layer was bidirectional, the remaining seven encoder layers were unidirectional, and all eight decoder layers were unidirectional.<sup>[21]</sup> It took nine months to develop, and it outperformed the statistical approach, which took ten years to develop.<sup>[22]</sup>

### Parallelizing attention

[edit]
Seq2seq models with attention (including self-attention) still suffered from the same issue with recurrent networks, which is that they are hard to parallelize, which prevented them from being accelerated on GPUs. In 2016, *decomposable attention* applied a self-attention mechanism to feedforward networks, which are easy to parallelize, and achieved state-of-the-art (SOTA) results in textual entailment with an order of magnitude fewer parameters than LSTMs.<sup>[23]</sup> One of its authors, Jakob Uszkoreit, suspected that attention *without* recurrence would be sufficient for language translation, thus the title "attention is *All* you need".<sup>[24]</sup> That hypothesis was against conventional wisdom at the time, and even his father Hans Uszkoreit, a well-known computational linguist, was skeptical.<sup>[24]</sup> In the same year, self-attention (called *intra-attention or* *intra-sentence attention*) was proposed for LSTMs.<sup>[25]</sup>

The original encoder–decoder Transformer was introduced in the paper "Attention Is All You Need," submitted to arXiv on 2017-06-12. At the time, the focus of the research was on improving seq2seq for machine translation, by removing its recurrence to process all tokens in parallel, but preserving its dot-product attention mechanism to keep its text processing performance.<sup>[1]</sup> This led to the introduction of a multi-head attention model that was easier to parallelize due to the use of independent heads and the lack of recurrence. Its parallelizability was an important factor to its widespread use in large neural networks.<sup>[26]</sup>

---

[referencia=34c4c8ee90c46400 score=0.062]
# Attention Is All You Need


| "Attention Is All You Need" |  | 
|---|---|
| Project type | Artificial intelligence research | 
| Sponsors |  | 
| Objective | Provide a novel approach to train AI | 
| Duration | June 12, 2017 – | 
| Website | proceedings | 

"**Attention Is All You Need**"<sup>[1]</sup> is a 2017 research paper on machine learning authored by eight scientists and engineers working at Google. The paper introduced a new deep learning architecture known as the transformer, based on the attention mechanism proposed in 2014 by Bahdanau *et al.*<sup>[2]</sup> The transformer approach it describes has become the main architecture of a wide variety of artificial intelligence systems, including large language models.<sup>[3]</sup><sup>[4]</sup> At the time, the focus of the research was on improving Seq2seq techniques for machine translation, but the authors went further in the paper, foreseeing the technique's potential for other tasks like question answering and what is now known as multimodal generative AI.<sup>[1]</sup>

Some early examples on which the team tried their Transformer architecture included English-to-German translation, generating Wikipedia articles on "The Transformer", and parsing. These convinced the team that the Transformer is a general-purpose language model, and not just good for translation.<sup>[5]</sup>

As of 2026,<sup>[update]</sup> the paper has been cited more than 150,000 times, placing it among the top ten most-cited papers of the 21st century.<sup>[6]</sup> After the paper was published by Google, each of the eight authors left the company to join other companies or to found startups.

---

[referencia=a7468c6851652691 score=0.060]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=a7468c6851652691 score=0.048]
### A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output 

positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

[referencia=34c4c8ee90c46400 score=0.039]
24. 1 2 Levy, Steven. "8 Google Employees Invented Modern AI. Here's the Inside Story". *Wired* . Archived from the original on 20 March 2024. Retrieved 6 August 2024.
25. ↑ Cheng, Jianpeng; Dong, Li; Lapata, Mirella (November 2016). "Long Short-Term Memory-Networks for Machine Reading". In Su, Jian; Duh, Kevin; Carreras, Xavier (eds.). *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing* . Austin, Texas: Association for Computational Linguistics. pp. 551–561. doi:10.18653/v1/D16-1053. Archived from the original on 27 August 2024. Retrieved 27 August 2024.
26. ↑ Peng, Bo; Alcaide, Eric; Anthony, Quentin; Albalak, Alon; Arcadinho, Samuel; Biderman, Stella; Cao, Huanqi; Cheng, Xin; Chung, Michael (10 December 2023). "RWKV: Reinventing RNNs for the transformer Era". arXiv:2305.13048 [cs.CL].
27. ↑ Marche, Stephen (23 August 2024). "Was Linguistic A.I. Created by Accident?". *The New Yorker* . Retrieved 27 August 2024.
28. ↑ Vaswani, Ashish; Bengio, Samy; Brevdo, Eugene; Chollet, Francois; Gomez, Aidan; Gouws, Stephan; Jones, Llion; Kaiser, Łukasz; Kalchbrenner, Nal; Parmar, Niki; Sepassi, Ryan; Shazeer, Noam; Uszkoreit, Jakob (March 2018). Cherry, Colin; Neubig, Graham (eds.). "Tensor2Tensor for Neural Machine Translation". *Proceedings of the 13th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)* . Boston, MA: Association for Machine Translation in the Americas: 193–199. Archived from the original on 29 April 2026. Retrieved 31 March 2026.

---

[referencia=34c4c8ee90c46400 score=0.038]
### Attention with seq2seq

[edit]
The idea of encoder–decoder sequence transduction had been developed in the early 2010s; commonly cited as the originators that produced seq2seq are two concurrently published papers from 2014.<sup>[15]</sup><sup>[16]</sup><sup>[*original research?*]</sup>

A 380M-parameter model for machine translation uses two long short-term memories (LSTM).<sup>[16]</sup> Its architecture consists of two parts. The *encoder* is an LSTM that takes in a sequence of tokens and turns it into a vector. The *decoder* is another LSTM that converts the vector into a sequence of tokens. Similarly, another 130M-parameter model used gated recurrent units (GRU) instead of LSTM.<sup>[15]</sup> Later research showed that GRUs are neither better nor worse than LSTMs for seq2seq.<sup>[17]</sup><sup>[18]</sup>

These early seq2seq models had no attention mechanism, and the state vector is accessible only after the *last* word of the source text was processed. Although in theory such a vector retains the information about the whole original sentence, in practice the information is poorly preserved. This is because the input is processed sequentially by one recurrent network into a *fixed*-size output vector, which is then processed by another recurrent network into an output. If the input is long, then the output vector would not be able to contain all relevant information, degrading the output. As evidence, reversing the input sentence improved seq2seq translation.<sup>[19]</sup>

The *RNN search* model introduced an attention mechanism to seq2seq for machine translation to solve the bottleneck problem (of the *fixed-size* output vector), allowing the model to process long-distance dependencies more easily. The name is because it "emulates searching through a source sentence during decoding a translation".<sup>[2]</sup>

The relative performances were compared between global (that of *RNN search*) and local (sliding window) attention model architectures for machine translation, finding that mixed attention had higher quality than global attention, while local attention reduced translation time.<sup>[20]</sup>

---

[referencia=a7468c6851652691 score=0.032]
# **Attention Is All You Need** 

**Ashish Vaswani**<sup>_∗_</sup> **Noam Shazeer**<sup>_∗_</sup> **Niki Parmar**<sup>_∗_</sup> **Jakob Uszkoreit**<sup>_∗_</sup> Google Brain Google Brain Google Research Google Research `avaswani@google.com noam@google.com nikip@google.com usz@google.com` 

**Llion Jones**<sup>_∗_</sup> Google Research `llion@google.com` 

**Aidan N. Gomez**<sup>_∗†_</sup> **Łukasz Kaiser**<sup>_∗_</sup> University of Toronto Google Brain `aidan@cs.toronto.edu lukaszkaiser@google.com` 

**Illia Polosukhin**<sup>_∗‡_</sup> 

```
illia.polosukhin@gmail.com
```

---

[referencia=34c4c8ee90c46400 score=0.030]
1. 1 2 3 4 5 6 Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N; Kaiser, Łukasz; Polosukhin, Illia (December 2017). "Attention is All you Need" (PDF). In I. Guyon and U. Von Luxburg and S. Bengio and H. Wallach and R. Fergus and S. Vishwanathan and R. Garnett (ed.). *31st Conference on Neural Information Processing Systems (NIPS)* . Advances in Neural Information Processing Systems. Vol. 30. Curran Associates, Inc. arXiv:1706.03762.
2. 1 2 Bahdanau, Dzmitry; Cho, Kyunghyun; Bengio, Yoshua (19 May 2016). "Neural Machine Translation by Jointly Learning to Align and Translate". arXiv:1409.0473 [cs.CL].
3. ↑ Shinde, Gitanjali; Wasatkar, Namrata; Mahalle, Parikshit (6 June 2024). *Data-Centric Artificial Intelligence for Multidisciplinary Applications* . CRC Press. p. 75. ISBN 9781040031131. Archived from the original on 19 August 2024. Retrieved 19 August 2024.
4. ↑ Murgia, Madhumita (23 July 2023). "Transformers: the Google scientists who pioneered an AI revolution". *Financial Times* . Archived from the original on 23 July 2023. Retrieved 22 March 2024.
5. 1 2 Marche, Stephen (23 August 2024). "Was Linguistic A.I. Created by Accident?". *The New Yorker* . Condé Nast. ISSN 0028-792X. OCLC 320541675. Archived from the original on 23 August 2024. Retrieved 24 August 2024.

---

[referencia=a7468c6851652691 score=0.028]
||_N_|_d_model|_d_ff|_h_|_dk_|_dv_|_Pdrop_|_ϵls_|train<br>steps|PPL<br>(dev)|BLEU<br>(dev)|params<br>_×_10<sup>6</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|base|6|512|2048|8|64|64|0.1|0.1|100K|4.92|25.8|65|
|||||1|512|512||||5.29|24.9||
|A||||4|128|128||||5.00|25.5||
|()||||16|32|32||||4.91|25.8||
|||||32|16|16||||5.01|25.4||
||||||16|||||5.16|25.1|58|
|(B)|||||32|||||5.01|25.4|60|
||2|||||||||6.11|23.7|36|
||4|||||||||5.19|25.3|50|
||8|||||||||4.88|25.5|80|
|(C)||256|||32|32||||5.75|24.5|28|
|||1024|||128|128||||4.66|26.0|168|
||||1024|||||||5.12|25.4|53|
||||4096|||||||4.75|26.2|90|
||||||||0.0|||5.77|24.6||
|D|||||||0.2|||4.95|25.5||
|()||||||||0.0||4.67|25.3||
|||||||||0.2||5.47|25.7||
|(E)||posi|tional e|mbedd|ingins|tead of|sinusoi|ds||4.92|25.7||
|big|6|1024|4096|16|||0.3||300K|**4.33**|**26.4**|213|



development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3.