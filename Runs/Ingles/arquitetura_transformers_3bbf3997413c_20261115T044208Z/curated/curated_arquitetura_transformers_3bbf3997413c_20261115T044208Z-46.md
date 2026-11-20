[referencia=a7468c6851652691 score=0.493]
In this work we employ _h_ = 8 parallel attention layers, or heads. For each of these we use _dk_ = _dv_ = _d_ model _/h_ = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality. 

**3.2.3 Applications of Attention in our Model** The Transformer uses multi-head attention in three different ways: 

• In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. 

• The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to 

all positions in the decoder up to and including that position. We need to prevent leftward 

information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2. 

**3.3 Position-wise Feed-Forward Networks** 

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between. 

FFN( _x_ ) = max(0 _, xW_ 1 + _b_ 1) _W_ 2 + _b_ 2 (2) 

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is _d_ model = 512, and the inner-layer has dimensionality _dff_ = 2048. 

**3.4 Embeddings and Softmax**

---

[referencia=a7468c6851652691 score=0.304]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

**3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two 

sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention 

sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ . 

**3.2 Attention**

---

[referencia=a7468c6851652691 score=0.172]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=a7468c6851652691 score=0.155]
**3.2 Attention** 

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum 

3 

Scaled Dot-Product Attention 





Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel. 

of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. 

### **3.2.1 Scaled Dot-Product Attention** 

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension _dk_ , and values of dimension _dv_ . We compute the dot products of the query with all keys, divide each by<sup>_√_</sup> _dk_ , and apply a softmax function to obtain the weights on the values. 

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix _Q_ . The keys and values are also packed together into matrices _K_ and _V_ . We compute the matrix of outputs as: 



The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

While for small values of _dk_ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of _dk_ [3]. We suspect that for large values of _dk_ , the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients<sup>4</sup> . To counteract this effect, we scale the dot products by _~~√~~_ <u>1</u> _dk_<sup>.</sup>

---

[referencia=a7468c6851652691 score=0.152]
A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

[referencia=a2690ed31e8cc7e9 score=0.120]
### **4.1 Subword statistics** 

Apart from translation quality, which we will verify empirically, our main objective is to represent an open vocabulary through a compact fixed-size subword vocabulary, and allow for efficient training and decoding.<sup>8</sup> 

Statistics for different segmentations of the Ger- 



> 6Clipped unigram precision is essentially 1-gram BLEU without brevity penalty. 

> 7 `github.com/sebastien-j/LV_groundhog` 

> 8The time complexity of encoder-decoder architectures is at least linear to sequence length, and oversplitting harms efficiency. 

man side of the parallel data are shown in Table 1. A simple baseline is the segmentation of words into character n-grams.<sup>9</sup> Character n-grams allow for different trade-offs between sequence length (# tokens) and vocabulary size (# types), depending on the choice of n. The increase in sequence length is substantial; one way to reduce sequence length is to leave a shortlist of the k most frequent word types unsegmented. Only the unigram representation is truly open-vocabulary. However, the unigram representation performed poorly in preliminary experiments, and we report translation results with a bigram representation, which is empirically better, but unable to produce some tokens in the test set with the training set vocabulary. 

We report statistics for several word segmentation techniques that have proven useful in previous SMT research, including frequency-based compound splitting (Koehn and Knight, 2003), rulebased hyphenation (Liang, 1983), and Morfessor (Creutz and Lagus, 2002). We find that they only moderately reduce vocabulary size, and do not solve the unknown word problem, and we thus find them unsuitable for our goal of open-vocabulary translation without back-off dictionary. 

BPE meets our goal of being open-vocabulary, and the learned merge operations can be applied to the test set to obtain a segmentation with no unknown symbols.<sup>10</sup> Its main difference from the character-level model is that the more compact representation of BPE allows for shorter sequences, and that the attention model operates on variable-length units.<sup>11</sup> Table 1 shows BPE with 59 500 merge operations, and joint BPE with 89 500 operations.

---

[referencia=a7468c6851652691 score=0.117]
**3.4 Embeddings and Softmax** 

Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension _d_ model. We also use the usual learned linear transfor- 

mation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to [30]. In the embedding layers, we multiply those weights by<sup>_√_</sup> _d_ model. 

5 

Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. _n_ is the sequence length, _d_ is the representation dimension, _k_ is the kernel size of convolutions and _r_ the size of the neighborhood in restricted self-attention. 

|Layer Type|Complexity per Layer|Sequential<br>Operations|Maximum Path Length|
|---|---|---|---|
|Self-Attention|_O_(_n_<sup>2</sup> _· d_)|_O_(1)|_O_(1)|
|Recurrent|_O_(_n · d_<sup>2</sup>)|_O_(_n_)|_O_(_n_)|
|Convolutional|_O_(_k · n · d_<sup>2</sup>)|_O_(1)|_O_(_logk_(_n_))|
|Self-Attention (restricted)|_O_(_r · n · d_)|_O_(1)|_O_(_n/r_)|

---

[referencia=a7468c6851652691 score=0.113]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=a2690ed31e8cc7e9 score=0.094]
### **3.1 Related Work** 

For Statistical Machine Translation (SMT), the translation of unknown words has been the subject of intensive research. 

A large proportion of unknown words are names, which can just be copied into the target text if both languages share an alphabet. If alphabets differ, transliteration is required (Durrani et al., 2014). Character-based translation has also been investigated with phrase-based models, which proved especially successful for closely related languages (Vilar et al., 2007; Tiedemann, 2009; Neubig et al., 2012). 

The segmentation of morphologically complex words such as compounds is widely used for SMT, and various algorithms for morpheme segmentation have been investigated (Nießen and Ney, 2000; Koehn and Knight, 2003; Virpioja et al., 2007; Stallard et al., 2012). Segmentation algorithms commonly used for phrase-based SMT tend to be conservative in their splitting decisions, whereas we aim for an aggressive segmentation that allows for open-vocabulary translation with a compact network vocabulary, and without having to resort to back-off dictionaries. 

The best choice of subword units may be taskspecific. For speech recognition, phone-level language models have been used (Bazzi and Glass, 2000). Mikolov et al. (2012) investigate subword language models, and propose to use syllables. For multilingual segmentation tasks, multilingual algorithms have been proposed (Snyder and Barzilay, 2008). We find these intriguing, but inapplicable at test time. 

Various techniques have been proposed to produce fixed-length continuous word vectors based on characters or morphemes (Luong et al., 2013; Botha and Blunsom, 2014; Ling et al., 2015a; Kim et al., 2015). An effort to apply such techniques to NMT, parallel to ours, has found no significant improvement over word-based approaches (Ling et al., 2015b). One technical difference from our work is that the attention mechanism still operates on the level of words in the model by Ling et al. (2015b), and that the representation of each word is fixed-length. We expect that the attention mechanism benefits from our variable-length representation: the network can learn to place atten-

---

[referencia=a7468c6851652691 score=0.086]
- [13] Sepp Hochreiter and Jürgen Schmidhuber. Long short-term memory. _Neural computation_ , 9(8):1735–1780, 1997. 

- [14] Zhongqiang Huang and Mary Harper. Self-training PCFG grammars with latent annotations across languages. In _Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing_ , pages 832–841. ACL, August 2009. 

- [15] Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. Exploring the limits of language modeling. _arXiv preprint arXiv:1602.02410_ , 2016. 

- [16] Łukasz Kaiser and Samy Bengio. Can active memory replace attention? In _Advances in Neural Information Processing Systems, (NIPS)_ , 2016. 

- [17] Łukasz Kaiser and Ilya Sutskever. Neural GPUs learn algorithms. In _International Conference on Learning Representations (ICLR)_ , 2016. 

- [18] Nal Kalchbrenner, Lasse Espeholt, Karen Simonyan, Aaron van den Oord, Alex Graves, and Koray Kavukcuoglu. Neural machine translation in linear time. _arXiv preprint arXiv:1610.10099v2_ , 2017. 

- [19] Yoon Kim, Carl Denton, Luong Hoang, and Alexander M. Rush. Structured attention networks. In _International Conference on Learning Representations_ , 2017. 

- [20] Diederik Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _ICLR_ , 2015. 

- [21] Oleksii Kuchaiev and Boris Ginsburg. Factorization tricks for LSTM networks. _arXiv preprint arXiv:1703.10722_ , 2017. 

- [22] Zhouhan Lin, Minwei Feng, Cicero Nogueira dos Santos, Mo Yu, Bing Xiang, Bowen Zhou, and Yoshua Bengio. A structured self-attentive sentence embedding. _arXiv preprint arXiv:1703.03130_ , 2017.

---

[referencia=a7468c6851652691 score=0.081]
- [25] Mitchell P Marcus, Mary Ann Marcinkiewicz, and Beatrice Santorini. Building a large annotated corpus of english: The penn treebank. _Computational linguistics_ , 19(2):313–330, 1993. 

- [26] David McClosky, Eugene Charniak, and Mark Johnson. Effective self-training for parsing. In _Proceedings of the Human Language Technology Conference of the NAACL, Main Conference_ , pages 152–159. ACL, June 2006. 

- [27] Ankur Parikh, Oscar Täckström, Dipanjan Das, and Jakob Uszkoreit. A decomposable attention model. In _Empirical Methods in Natural Language Processing_ , 2016. 

- [28] Romain Paulus, Caiming Xiong, and Richard Socher. A deep reinforced model for abstractive summarization. _arXiv preprint arXiv:1705.04304_ , 2017. 

- [29] Slav Petrov, Leon Barrett, Romain Thibaux, and Dan Klein. Learning accurate, compact, and interpretable tree annotation. In _Proceedings of the 21st International Conference on Computational Linguistics and 44th Annual Meeting of the ACL_ , pages 433–440. ACL, July 2006. 

- [30] Ofir Press and Lior Wolf. Using the output embedding to improve language models. _arXiv preprint arXiv:1608.05859_ , 2016. 

- [31] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword units. _arXiv preprint arXiv:1508.07909_ , 2015. 

- [32] Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, and Jeff Dean. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. _arXiv preprint arXiv:1701.06538_ , 2017.

---

[referencia=a7468c6851652691 score=0.051]
development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3. 

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. 

In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

---

[referencia=a2690ed31e8cc7e9 score=0.044]
We report results with BLEU ( _mteval-v13a.pl_ ), and CHRF3 (Popovi´c, 2015), a character n-gram F3 score which was found to correlate well with 



4In practice, we simply concatenate the source and target side of the training set to learn joint BPE. 

> 5Since the Russian training text also contains words that use the Latin alphabet, we also apply the Latin BPE operations. 

human judgments, especially for translations out of English (Stanojevi´c et al., 2015). Since our main claim is concerned with the translation of rare and unseen words, we report separate statistics for these. We measure these through unigram F1, which we calculate as the harmonic mean of clipped unigram precision and recall.<sup>6</sup> 

We perform all experiments with Groundhog<sup>7</sup> (Bahdanau et al., 2015). We generally follow settings by previous work (Bahdanau et al., 2015; Jean et al., 2015). All networks have a hidden layer size of 1000, and an embedding layer size of 620. Following Jean et al. (2015), we only keep a shortlist of τ = 30000 words in memory. 

During training, we use Adadelta (Zeiler, 2012), a minibatch size of 80, and reshuffle the training set between epochs. We train a network for approximately 7 days, then take the last 4 saved models (models being saved every 12 hours), and continue training each with a fixed embedding layer (as suggested by (Jean et al., 2015)) for 12 hours. We perform two independent training runs for each models, once with cut-off for gradient clipping (Pascanu et al., 2013) of 5.0, once with a cut-off of 1.0 – the latter produced better single models for most settings. We report results of the system that performed best on our development set (newstest2013), and of an ensemble of all 8 models.

---

[referencia=a7468c6851652691 score=0.033]
## **4 Why Self-Attention** 

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to another sequence of equal length ( _z_ 1 _, ..., zn_ ), with _xi, zi ∈_ R<sup>_d_</sup> , such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata. 

One is the total computational complexity per layer. Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required. 

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types. 

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires _O_ ( _n_ ) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence 

6 

length _n_ is smaller than the representation dimensionality _d_ , which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size _r_ in the input sequence centered around the respective output position. This would increase the maximum path length to _O_ ( _n/r_ ). We plan to investigate this approach further in future work.

---

[referencia=a2690ed31e8cc7e9 score=0.019]
## **6 Conclusion** 

The main contribution of this paper is that we show that neural machine translation systems are capable of open-vocabulary translation by representing rare and unseen words as a sequence of subword units.<sup>14</sup> This is both simpler and more effective than using a back-off translation model. We introduce a variant of byte pair encoding for word segmentation, which is capable of encoding open vocabularies with a compact symbol vocabulary of variable-length subword units. We show performance gains over the baseline with both BPE segmentation, and a simple character bigram segmentation. 

Our analysis shows that not only out-ofvocabulary words, but also rare in-vocabulary words are translated poorly by our baseline NMT 



> 14The source code of the segmentation algorithms is available at `https://github.com/rsennrich/ subword-nmt` . 

system, and that reducing the vocabulary size of subword models can actually improve performance. In this work, our choice of vocabulary size is somewhat arbitrary, and mainly motivated by comparison to prior work. One avenue of future research is to learn the optimal vocabulary size for a translation task, which we expect to depend on the language pair and amount of training data, automatically. We also believe there is further potential in bilingually informed segmentation algorithms to create more alignable subword units, although the segmentation algorithm cannot rely on the target text at runtime. 

While the relative effectiveness will depend on language-specific factors such as vocabulary size, we believe that subword segmentations are suitable for most language pairs, eliminating the need for large NMT vocabularies or back-off models. 

## **Acknowledgments** 

We thank Maja Popovi´c for her implementation of CHRF, with which we verified our reimplementation. The research presented in this publication was conducted in cooperation with Samsung Electronics Polska sp. z o.o. - Samsung R&D Institute Poland. This project received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement 645452 (QT21).

---

[referencia=a2690ed31e8cc7e9 score=0.018]
## **4 Evaluation** 

Figure 1: BPE merge operations learned from dictionary {‘low’, ‘lowest’, ‘newer’, ‘wider’}. 

gorithm 1. In practice, we increase by indexing all pairs, and updating data structures incrementally. 

The main difference to other compression algorithms, such as Huffman encoding, which have been proposed to produce a variable-length encoding of words for NMT (Chitnis and DeNero, 2015), is that our symbol sequences are still interpretable as subword units, and that the network can generalize to translate and produce new words (unseen at training time) on the basis of these subword units. 

Figure 1 shows a toy example of learned BPE operations. At test time, we first split words into sequences of characters, then apply the learned operations to merge the characters into larger, known symbols. This is applicable to any word, and allows for open-vocabulary networks with fixed symbol vocabularies.<sup>3</sup> In our example, the OOV ‘lower’ would be segmented into ‘low er·’. 



> 3The only symbols that will be unknown at test time are unknown characters, or symbols of which all occurrences in the training text have been merged into larger symbols, like ‘safeguar’, which has all occurrences in our training text merged into ‘safeguard’. We observed no such symbols at test time, but the issue could be easily solved by recursively reversing specific merges until all symbols are known. 

We aim to answer the following empirical questions: 

- Can we improve the translation of rare and unseen words in neural machine translation by representing them via subword units? 

- Which segmentation into subword units performs best in terms of vocabulary size, text size, and translation quality? 

We perform experiments on data from the shared translation task of WMT 2015. For English→German, our training set consists of 4.2 million sentence pairs, or approximately 100 million tokens. For English→Russian, the training set consists of 2.6 million sentence pairs, or approximately 50 million tokens. We tokenize and truecase the data with the scripts provided in Moses (Koehn et al., 2007). We use newstest2013 as development set, and report results on newstest2014 and newstest2015.

---

[referencia=a2690ed31e8cc7e9 score=0.016]
In practice, we did not include infrequent subword units in the NMT network vocabulary, since there is noise in the subword symbol sets, e.g. because of characters from foreign alphabets. Hence, our network vocabularies in Table 2 are typically slightly smaller than the number of types in Table 1. 



> 9Our character n-grams do not cross word boundaries. We mark whether a subword is word-final or not with a special character, which allows us to restore the original tokenization. 

> 10Joint BPE can produce segments that are unknown because they only occur in the English training text, but these are rare (0.05% of test tokens). 

> 11We highlighted the limitations of word-level attention in section 3.1. At the other end of the spectrum, the character level is suboptimal for alignment (Tiedemann, 2009).

---

[referencia=a2690ed31e8cc7e9 score=0.015]
This paper has two main contributions: 

• We show that open-vocabulary neural ma- 

chine translation is possible by encoding (rare) words via subword units. We find our architecture simpler and more effective than using large vocabularies and back-off dictionaries (Jean et al., 2015; Luong et al., 2015b). 

- We adapt _byte pair encoding_ (BPE) (Gage, 1994), a compression algorithm, to the task of word segmentation. BPE allows for the representation of an open vocabulary through a fixed-size vocabulary of variable-length character sequences, making it a very suitable word segmentation strategy for neural network models. 

## **2 Neural Machine Translation** 

We follow the neural machine translation architecture by Bahdanau et al. (2015), which we will briefly summarize here. However, we note that our approach is not specific to this architecture. 

The neural machine translation system is implemented as an encoder-decoder network with recurrent neural networks. 

The encoder is a bidirectional neural network with gated recurrent units (Cho et al., 2014) that reads an input sequence x = (x1, ..., xm) and calculates a forward sequence of hidden states (<sup>−→</sup> h 1, ...,<sup>−→</sup> h m), and a backward sequence (<sup>←−</sup> h 1, ...,<sup>←−</sup> h m). The hidden states<sup>−→</sup> h j and<sup>←−</sup> h j are concatenated to obtain the annotation vector h . j 

The decoder is a recurrent neural network that predicts a target sequence y = (y1, ..., yn). Each word yi is predicted based on a recurrent hidden state si, the previously predicted word yi−1, and a context vector ci. ci is computed as a weighted sum of the annotations hj. The weight of each annotation hj is computed through an _alignment model_ αij, which models the probability that yi is aligned to xj. The alignment model is a singlelayer feedforward neural network that is learned jointly with the rest of the network through backpropagation. 

A detailed description can be found in (Bahdanau et al., 2015). Training is performed on a parallel corpus with stochastic gradient descent. For translation, a beam search with small beam size is employed.

---

[referencia=a7468c6851652691 score=0.014]
### **6.3 English Constituency Parsing** 

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input. Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37]. 

We trained a 4-layer transformer with _dmodel_ = 1024 on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting. 

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we 

9 

Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)

---

[referencia=a7468c6851652691 score=0.014]
### **5.4 Regularization** 

We employ three types of regularization during training: 

7 

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost. 

||BL|EU|Training C|ost (FLOPs)|
|---|---|---|---|---|
|Model|||||
||EN-DE|EN-FR|EN-DE|EN-FR|
|ByteNet [18]|23.75||||
|Deep-Att + PosUnk [39]||39.2||1_._0_·_10<sup>20</sup>|
|<br>GNMT + RL [38]|24.6|39.92|2_._3_·_10<sup>19</sup>|1_._4_·_10<sup>20</sup>|
|ConvS2S [9]|25.16|40.46|9_._6_·_10<sup>18</sup>|1_._5_·_10<sup>20</sup>|
|MoE[32]|26.03|40.56|2_._0_·_10<sup>19</sup>|1_._2_·_10<sup>20</sup>|
|Deep-Att + PosUnk Ensemble [39]||40.4||8_._0_·_10<sup>20</sup>|
|GNMT + RL Ensemble [38]|26.30|41.16|1_._8_·_10<sup>20</sup>|1_._1_·_10<sup>21</sup>|
|ConvS2S Ensemble[9]|26.36|**41.29**|7_._7_·_10<sup>19</sup>|1_._2_·_10<sup>21</sup>|
|Transformer (base model)|27.3|38.1|**3****_._3****_·_**|**10**<sup>**18**</sup>|
|Transformer (big)|**28.4**|**41.8**|2_._3_·_|10<sup>19</sup>|