[referencia=34c4c8ee90c46400 score=0.620]
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

[referencia=34c4c8ee90c46400 score=0.564]
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

As of 2026,<sup>[update]</sup> the paper has been cited more than 250,000 times, placing it among the top ten most-cited papers of the 21st century.<sup>[6]</sup> After the paper was published by Google, each of the eight authors left the company to join other companies or to found startups.

---

[referencia=34c4c8ee90c46400 score=0.262]
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

[referencia=34c4c8ee90c46400 score=0.209]
In 2016, Google Translate was revamped to Google Neural Machine Translation, which replaced the previous model based on statistical machine translation. The new model was a seq2seq model where the encoder and the decoder were both 8 layers of bidirectional LSTM.<sup>[27]</sup> It took nine months to develop, and it outperformed the statistical approach, which took ten years to develop.<sup>[28]</sup>

### Parallelizing attention

[edit]
Seq2seq models with attention (including self-attention) still suffered from the same issue with recurrent networks, which is that they are hard to parallelize, which prevented them from being accelerated on GPUs. In 2016, *decomposable attention* applied a self-attention mechanism to feedforward networks, which are easy to parallelize, and achieved state-of-the-art (SOTA) results in textual entailment with an order of magnitude fewer parameters than LSTMs.<sup>[29]</sup> One of its authors, Jakob Uszkoreit, suspected that attention *without* recurrence would be sufficient for language translation, thus the title "attention is *All* you need".<sup>[30]</sup> That hypothesis was against conventional wisdom at the time, and even his father Hans Uszkoreit, a well-known computational linguist, was skeptical.<sup>[30]</sup> In the same year, self-attention (called *intra-attention or* *intra-sentence attention*) was proposed for LSTMs.<sup>[31]</sup>

On 2017-06-12, the original (100M-parameter) encoder–decoder transformer model was published in the "Attention is All you need" paper. At the time, the focus of the research was on improving seq2seq for machine translation, by removing its recurrence to process all tokens in parallel, but preserving its dot-product attention mechanism to keep its text processing performance.<sup>[1]</sup> This led to the introduction of a multi-head attention model that was easier to parallelize due to the use of independent heads and the lack of recurrence. Its parallelizability was an important factor to its widespread use in large neural networks.<sup>[32]</sup>

---

[referencia=34c4c8ee90c46400 score=0.196]
## Historical context

[edit]
### Predecessors

[edit]
Before transformers, recurrent neural networks (RNNs) were widely used for sequence modelling and generation. A well-cited early example was the Elman network (1990). In theory, the information from one token can propagate arbitrarily far down the sequence, but in practice the vanishing-gradient problem leaves the model's state at the end of a long sentence without precise, extractable information about preceding tokens.

A key breakthrough was LSTM (originally described in a 1995 technical report and formally published in 1997),<sup>[11]</sup><sup>[note 1]</sup> an RNN that introduced gating mechanisms to mitigate the vanishing gradient problem, allowing efficient learning of long-sequence modelling. One key architectural element was the use of *multiplicative gating units*, in which the outputs of some neurons modulate the outputs of others. These multiplicative units are conceptually distinct from the additive attention mechanism later introduced for sequence-to-sequence models.
<sup>[12]</sup> Neural networks using multiplicative units were later called *sigma-pi networks*<sup>[13]</sup> or *higher-order networks*.<sup>[14]</sup> LSTM became the standard architecture for long sequence modelling until the 2017 publication of transformers. However, LSTM still used sequential processing, like most other RNNs.<sup>[note 2]</sup> Specifically, RNNs operate one token at a time from first to last; they cannot operate in parallel over all tokens in a sequence.

Transformers allow parallel processing of tokens during training, but standard self-attention has computational and memory costs that grow quadratically with sequence length. The fast weight controller, proposed in 1992, used one network to generate input-dependent weights for another network. This method built on earlier work on "fast weights" and "dynamic links".<sup>[15]</sup><sup>[16]</sup><sup>[17]</sup> A slow neural network learns by gradient descent to generate keys and values for computing the weight changes of the fast neural network which computes answers to queries.<sup>[18]</sup> This was later shown to be equivalent to the unnormalized linear transformer.<sup>[19]</sup><sup>[20]</sup>

---

[referencia=34c4c8ee90c46400 score=0.134]
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

[referencia=34c4c8ee90c46400 score=0.101]
## Background

[edit]
The authors of the paper are Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, and Illia Polosukhin. All eight authors were "equal contributors" to the paper; the listed order was randomized (according to the paper itself). After the paper, each of the authors left Google to join other companies or to found startups.<sup>[7]</sup><sup>[8]</sup>

The paper's title is a reference to the song "All You Need Is Love" by the Beatles.<sup>[9]</sup> The name "Transformer" was picked because Jakob Uszkoreit, one of the paper's authors, liked the sound of that word.<sup>[5]</sup> An early design document was titled "Transformers: Iterative Self-Attention and Processing for Various Tasks", and included an illustration of six characters from the *Transformers* franchise. The team was named Team Transformer.<sup>[9]</sup>

---

[referencia=34c4c8ee90c46400 score=0.070]
## External links

[edit]
- "Attention Is All You Need" on Google Research
- "Attention Is All You Need" on arXiv
- Uszkoreit, Jakob (31 August 2017). "Transformer: A Novel Neural Network Architecture for Language Understanding". *research.google* . Retrieved 9 August 2024. A concurrent blog post on the Google Research blog.

---

[referencia=34c4c8ee90c46400 score=0.058]
### AI boom era

[edit]

In spring 2017, before the "Attention is All you need" preprint was published, one of the co-authors applied the "decoder-only" variation of the architecture to generate fictitious Wikipedia articles.<sup>[33]</sup> Transformer architecture is now used alongside many generative models that contribute to the ongoing AI boom.

The "reference implementation" of the original Transformer was written in a TensorFlow library.<sup>[34]</sup><sup>[35]</sup> In language modelling, ELMo (2018) was a bi-directional LSTM that produces contextualized word embeddings, improving upon the line of research from bag of words and word2vec. It was followed by BERT (2018), an encoder-only transformer model.<sup>[36]</sup> In October 2019, Google started using BERT to process search queries.<sup>[37]</sup> In 2020, Google Translate replaced the previous RNN-encoder–RNN-decoder model by a transformer-encoder–RNN-decoder model.<sup>[38]</sup><sup>[*non-primary source needed*]</sup>

Starting in 2018, the OpenAI GPT series of decoder-only transformers became state of the art in natural language generation. At the end of 2022, ChatGPT, a chatbot based on a fine-tuned variant of GPT-3.5, became unexpectedly<sup>[39]</sup><sup>[40]</sup> popular, triggering a boom around large language models.<sup>[41]</sup>

Transformers have been applied in modalities beyond text. Four days after the publication of "Attention is All You Need", a multimodal transformer architecture, MultiModel, was published by most authors of that paper.<sup>[42]</sup> Other examples include the vision transformer, which has led to developments in convolutional neural networks.<sup>[43]</sup> Image and video generators like DALL-E (2021), Stable Diffusion 3 (2024), and Sora (2024), use transformers to analyse input data (like text prompts) by breaking it down into "tokens" and then calculating the relevance between each token using self-attention, which helps the model simulate the context and relationships within the data.<sup>[*citation needed*]</sup>

---

[referencia=34c4c8ee90c46400 score=0.018]
19. ↑ Katharopoulos, Angelos; Vyas, Apoorv; Pappas, Nikolaos; Fleuret, François (2020). "Transformers are RNNs: Fast autoregressive Transformers with linear attention". *ICML 2020* . PMLR. pp. 5156–5165.
20. ↑ Schlag, Imanol; Irie, Kazuki; Schmidhuber, Jürgen (2021). "Linear Transformers Are Secretly Fast Weight Programmers". *ICML 2021* . Springer. pp. 9355–9366. Archived from the original on 20 May 2026. Retrieved 20 May 2026.
21. 1 2 Cho, Kyunghyun; van Merriënboer, Bart; Gulcehre, Caglar; Bahdanau, Dzmitry; Bougares, Fethi; Schwenk, Holger; Bengio, Yoshua (October 2014). "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation". In Moschitti, Alessandro; Pang, Bo; Daelemans, Walter (eds.). *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)* . Doha, Qatar: Association for Computational Linguistics. pp. 1724–1734. arXiv:1406.1078. doi:10.3115/v1/D14-1179. Archived from the original on 6 September 2024. Retrieved 9 August 2024.
22. 1 2 Sutskever, Ilya; Vinyals, Oriol; Le, Quoc Viet (14 December 2014). "Sequence to sequence learning with neural networks". arXiv:1409.3215 [cs.CL]. [first version posted to arXiv on 10 Sep 2014]
23. ↑ Chung, Junyoung; Gulcehre, Caglar; Cho, KyungHyun; Bengio, Yoshua (2014). "Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling". arXiv:1412.3555 [cs.NE].

---

[referencia=34c4c8ee90c46400 score=0.012]
1. 1 2 3 4 5 6 Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N; Kaiser, Łukasz; Polosukhin, Illia (December 2017). "Attention is All you Need" (PDF). In I. Guyon and U. Von Luxburg and S. Bengio and H. Wallach and R. Fergus and S. Vishwanathan and R. Garnett (ed.). *31st Conference on Neural Information Processing Systems (NIPS)* . Advances in Neural Information Processing Systems. Vol. 30. Curran Associates, Inc. arXiv:1706.03762.
2. 1 2 Bahdanau, Dzmitry; Cho, Kyunghyun; Bengio, Yoshua (19 May 2016). "Neural Machine Translation by Jointly Learning to Align and Translate". arXiv:1409.0473 [cs.CL].
3. ↑ Shinde, Gitanjali; Wasatkar, Namrata; Mahalle, Parikshit (6 June 2024). *Data-Centric Artificial Intelligence for Multidisciplinary Applications* . CRC Press. p. 75. ISBN 9781040031131. Archived from the original on 19 August 2024. Retrieved 19 August 2024.
4. ↑ Murgia, Madhumita (23 July 2023). "Transformers: the Google scientists who pioneered an AI revolution". *Financial Times* . Archived from the original on 23 July 2023. Retrieved 22 March 2024.
5. 1 2 Marche, Stephen (23 August 2024). "Was Linguistic A.I. Created by Accident?". *The New Yorker* . Condé Nast. ISSN 0028-792X. OCLC 320541675. Archived from the original on 23 August 2024. Retrieved 24 August 2024.

---

[referencia=34c4c8ee90c46400 score=0.003]
### Attention with seq2seq

[edit]
The idea of encoder–decoder sequence transduction had been developed in the early 2010s; commonly cited as the originators that produced seq2seq are two concurrently published papers from 2014.<sup>[21]</sup><sup>[22]</sup><sup>[*original research?*]</sup>

A 380M-parameter model for machine translation uses two long short-term memories (LSTM).<sup>[22]</sup> Its architecture consists of two parts. The *encoder* is an LSTM that takes in a sequence of tokens and turns it into a vector. The *decoder* is another LSTM that converts the vector into a sequence of tokens. Similarly, another 130M-parameter model used gated recurrent units (GRU) instead of LSTM.<sup>[21]</sup> Later research showed that GRUs are neither better nor worse than LSTMs for seq2seq.<sup>[23]</sup><sup>[24]</sup>

These early seq2seq models had no attention mechanism, and the state vector is accessible only after the *last* word of the source text was processed. Although in theory such a vector retains the information about the whole original sentence, in practice the information is poorly preserved. This is because the input is processed sequentially by one recurrent network into a *fixed*-size output vector, which is then processed by another recurrent network into an output. If the input is long, then the output vector would not be able to contain all relevant information, degrading the output. As evidence, reversing the input sentence improved seq2seq translation.<sup>[25]</sup>

The *RNN search* model introduced an attention mechanism to seq2seq for machine translation to solve the bottleneck problem (of the *fixed-size* output vector), allowing the model to process long-distance dependencies more easily. The name is because it "emulates searching through a source sentence during decoding a translation".<sup>[2]</sup>

The relative performances were compared between global (that of *RNN search*) and local (sliding window) attention model architectures for machine translation, finding that mixed attention had higher quality than global attention, while local attention reduced translation time.<sup>[26]</sup>

---

[referencia=34c4c8ee90c46400 score=0.002]
6. ↑ Pearson, Helen; Ledford, Heidi; Hutson, Matthew; Van Noorden, Richard (15 April 2025). "Exclusive: the most-cited papers of the twenty-first century". *Nature* .**640** (8059): 588–592. Bibcode:2025Natur.640..588P. doi:10.1038/d41586-025-01125-9. PMID 40234577. Archived from the original on 18 April 2025. Retrieved 18 April 2025.
7. ↑ Murgia, Madhumita (23 July 2023). "Transformers: the Google scientists who pioneered an AI revolution". *Financial Times* . Archived from the original on 23 February 2024. Retrieved 22 March 2025.
8. ↑ "Meet the $4 Billion AI Superstars That Google Lost". *Bloomberg* . 13 July 2023. Archived from the original on 20 August 2023. Retrieved 26 January 2024 – via www.bloomberg.com.
9. 1 2 Levy, Steven. "8 Google Employees Invented Modern AI. Here's the Inside Story". *Wired* . ISSN 1059-1028. Archived from the original on 20 March 2024. Retrieved 20 March 2024.
10. ↑ Ciaramella, Alberto; Ciaramella, Marco (2024). *Introduction to Artificial Intelligence : from data analysis to generative AI* . Intellisemantic Editions. pp. 153–156, 196. ISBN 978-88-947876-0-3.
11. ↑ Hochreiter, Sepp; Schmidhuber, Jürgen (November 1997). "Long Short-Term Memory". *Neural Computation* .**9** (8): 1735–1780. doi:10.1162/neco.1997.9.8.1735. PMID 9377276.
12. ↑ Feldman, J; Ballard, D (September 1982). "Connectionist models and their properties". *Cognitive Science* .**6** (3): 205–254. doi:10.1016/S0364-0213(82)80001-3.

---

[referencia=34c4c8ee90c46400 score=0.001]
24. ↑ Gruber, Nicole; Jockisch, Alfred (30 June 2020). "Are GRU Cells More Specific and LSTM Cells More Sensitive in Motive Classification of Text?". *Frontiers in Artificial Intelligence* .**3** 40. doi:10.3389/frai.2020.00040. PMC 7861254. PMID 33733157.
25. ↑ Sutskever, Ilya; Vinyals, Oriol; Le, Quoc V (2014). "Sequence to Sequence Learning with Neural Networks". *Advances in Neural Information Processing Systems* .**27** . Curran Associates, Inc. arXiv:1409.3215. Archived from the original on 27 January 2025. Retrieved 23 July 2024.
26. ↑ Luong, Minh-Thang; Pham, Hieu; Manning, Christopher D. (2015). "Effective Approaches to Attention-based Neural Machine Translation". arXiv:1508.04025 [cs.CL].
27. ↑ Wu, Yonghui; et al. (1 September 2016). "Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation". arXiv:1609.08144 [cs.CL].
28. ↑ Lewis-Kraus, Gideon (14 December 2016). "The Great A.I. Awakening". *The New York Times* . Archived from the original on 24 May 2023. Retrieved 22 June 2023.
29. ↑ Parikh, Ankur P.; Täckström, Oscar; Das, Dipanjan; Uszkoreit, Jakob (25 September 2016). "A Decomposable Attention Model for Natural Language Inference". arXiv:1606.01933 [cs.CL].
30. 1 2 Levy, Steven. "8 Google Employees Invented Modern AI. Here's the Inside Story". *Wired* . Archived from the original on 20 March 2024. Retrieved 6 August 2024.

---

[referencia=34c4c8ee90c46400 score=0.001]
30. 1 2 Levy, Steven. "8 Google Employees Invented Modern AI. Here's the Inside Story". *Wired* . Archived from the original on 20 March 2024. Retrieved 6 August 2024.
31. ↑ Cheng, Jianpeng; Dong, Li; Lapata, Mirella (November 2016). "Long Short-Term Memory-Networks for Machine Reading". In Su, Jian; Duh, Kevin; Carreras, Xavier (eds.). *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing* . Austin, Texas: Association for Computational Linguistics. pp. 551–561. doi:10.18653/v1/D16-1053. Archived from the original on 27 August 2024. Retrieved 27 August 2024.
32. ↑ Peng, Bo; Alcaide, Eric; Anthony, Quentin; Albalak, Alon; Arcadinho, Samuel; Biderman, Stella; Cao, Huanqi; Cheng, Xin; Chung, Michael (10 December 2023). "RWKV: Reinventing RNNs for the transformer Era". arXiv:2305.13048 [cs.CL].
33. ↑ Marche, Stephen (23 August 2024). "Was Linguistic A.I. Created by Accident?". *The New Yorker* . Retrieved 27 August 2024.
34. ↑ Vaswani, Ashish; Bengio, Samy; Brevdo, Eugene; Chollet, Francois; Gomez, Aidan; Gouws, Stephan; Jones, Llion; Kaiser, Łukasz; Kalchbrenner, Nal; Parmar, Niki; Sepassi, Ryan; Shazeer, Noam; Uszkoreit, Jakob (March 2018). Cherry, Colin; Neubig, Graham (eds.). "Tensor2Tensor for Neural Machine Translation". *Proceedings of the 13th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)* . Boston, MA: Association for Machine Translation in the Americas: 193–199. Archived from the original on 29 April 2026. Retrieved 31 March 2026.

---

[referencia=34c4c8ee90c46400 score=0.001]
35. ↑ Kaiser, Łukasz (19 June 2017). "Accelerating Deep Learning Research with the Tensor2Tensor Library". *Google Research Blog* . Archived from the original on 15 April 2026. Retrieved 31 March 2026.
36. ↑ Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (11 October 2018). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding". arXiv:1810.04805v2 [cs.CL].
37. ↑ "Google: BERT now used on almost every English query". *Search Engine Land* . 15 October 2020. Archived from the original on 6 May 2022. Retrieved 24 November 2020.
38. ↑ Caswell, Isaac; Liang, Bowen (8 June 2020). "Recent Advances in Google Translate". *Google Research* . Archived from the original on 4 July 2024. Retrieved 7 August 2024.
39. ↑ "The inside story of how ChatGPT was built from the people who made it". *MIT Technology Review* . Archived from the original on 3 March 2023. Retrieved 6 August 2024.
40. ↑ "Introducing ChatGPT". *OpenAI* . 30 November 2022. Archived from the original on 5 April 2026. Retrieved 16 May 2026.
41. ↑ Deign, Jason (6 December 2024). "How ChatGPT changed… well, almost everything". *Cisco Newsroom* . Retrieved 22 October 2026.`{{cite web}}` :  CS1 maint: url-status (link)
42. ↑ Kaiser, Lukasz; Gomez, Aidan N.; Shazeer, Noam; Vaswani, Ashish; Parmar, Niki; Jones, Llion; Uszkoreit, Jakob (16 June 2017). "One Model To Learn Them All". arXiv:1706.05137v1 [cs.LG].
43. ↑ Liu, Zhuang; Mao, Hanzi; Wu, Chao-Yuan; Feichtenhofer, Christoph; Darrell, Trevor; Xie, Saining (2022). *A ConvNet for the 2020s* . Conference on Computer Vision and Pattern Recognition (CVPR). pp. 11976–11986.

---

[referencia=34c4c8ee90c46400 score=0.001]
13. ↑ Rumelhart, David E.; McClelland, James L.; Hinton, Geoffrey E. (1986). *Parallel Distributed Processing, Volume 1: Explorations in the Microstructure of Cognition: Foundations, Chapter 2* (PDF). Cambridge, Massachusetts: Bradford Books. ISBN 978-0-262-68053-0. OCLC 12837549. OL 21219798M. Archived (PDF) from the original on 16 April 2026.
14. ↑ Giles, C. Lee; Maxwell, Tom (December 1987). "Learning, invariance, and generalization in high-order neural networks". *Applied Optics* .**26** (23): 4972–4978. doi:10.1364/AO.26.004972. PMID 20523475.
15. ↑ Christoph von der Malsburg: The correlation theory of brain function. Internal Report 81-2, MPI Biophysical Chemistry, 1981. http://cogprints.org/1380/1/vdM_correlation.pdf Archived 2022-01-26 at the Wayback Machine See Reprint in Models of Neural Networks II, chapter 2, pages 95–119. Springer, Berlin, 1994.
16. ↑ Feldman, Jerome A. (December 1982). "Dynamic connections in neural networks". *Biological Cybernetics* .**46** (1): 27–39. doi:10.1007/BF00335349. PMID 6307398.
17. ↑ Hinton, Geoffrey E.; Plaut, David C. (1987). "Using Fast Weights to Deblur Old Memories". *Proceedings of the Annual Meeting of the Cognitive Science Society* .**9** . Archived from the original on 23 July 2024. Retrieved 23 July 2024.
18. ↑ Schmidhuber, Jürgen (January 1992). "Learning to Control Fast-Weight Memories: An Alternative to Dynamic Recurrent Networks". *Neural Computation* .**4** (1): 131–139. doi:10.1162/neco.1992.4.1.131.

---

[referencia=34c4c8ee90c46400 score=0.000]
## References

[edit]