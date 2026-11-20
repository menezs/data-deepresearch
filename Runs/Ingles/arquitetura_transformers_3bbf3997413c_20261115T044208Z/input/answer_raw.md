# Transformer Architecture: Attention Mechanism and the Foundation of LLMs

## Scope and historical significance

The Transformer is the neural-network architecture that made modern large language models technically practical by replacing recurrent sequence processing with layers built primarily around attention, feed-forward transformations, residual connections, and normalization.[1] citeturn292328search0 Introduced by Vaswani and colleagues in *Attention Is All You Need* in 2017, the original Transformer was developed for neural machine translation and used an encoder-decoder design in which both sides were composed of stacked self-attention and feed-forward blocks.[1] citeturn292328search0 Its key departure from recurrent neural networks was that relationships among tokens could be computed in parallel rather than requiring a hidden state to propagate sequentially from one position to the next.[1] citeturn292328search0 This parallelism made the architecture particularly compatible with matrix-multiplication hardware and substantially accelerated training relative to recurrent approaches of the period.[1] citeturn292328search0

The original Transformer was not itself a “large language model” in the contemporary sense, but its components became the substrate from which the dominant families of pretrained language models developed.[1] citeturn292328search0 GPT demonstrated that a Transformer decoder could first be generatively pretrained on unlabeled text and then adapted to downstream tasks, establishing an influential pretraining-and-transfer paradigm.[2] citeturn136624search4 BERT subsequently showed the complementary strength of a bidirectional Transformer encoder trained with masked-language-model objectives, while T5 explored encoder-decoder pretraining under a unified text-to-text framework.[3][4] citeturn292328search2turn136624search0 GPT-3 then demonstrated that scaling an autoregressive Transformer to 175 billion parameters substantially strengthened zero-shot and few-shot behavior without task-specific gradient updates at inference time.[5] citeturn292328academia4

The modern importance of the Transformer therefore comes from more than the attention mechanism alone.[1] citeturn292328search0 Its broader contribution is a modular computational pattern in which token representations are repeatedly contextualized through attention, independently transformed by position-wise multilayer networks, and propagated through many residual layers.[1] citeturn292328search0 Large-scale language modeling then adds subword tokenization, massive unsupervised or self-supervised corpora, next-token or denoising objectives, optimized distributed training, and post-training methods such as supervised instruction tuning and preference optimization.[2][4][6] citeturn136624search4turn136624search0turn410184academia9

## Scaled dot-product attention and multi-head attention

Attention can be understood as content-addressable retrieval inside the network.[1] citeturn292328search0 Each token representation is projected into three vectors: a **query** \(q\), describing what that token is seeking; a **key** \(k\), describing what another token offers for matching; and a **value** \(v\), containing information that can be retrieved if the key is relevant.[1] citeturn292328search1 For a collection of tokens, the corresponding vectors are stacked into matrices \(Q\), \(K\), and \(V\).[1] citeturn292328search1

The Transformer's scaled dot-product attention is

\[
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^\top}{\sqrt{d_k}}
\right)V ,
\]

where \(d_k\) is the dimensionality of each key and query vector.[1] citeturn292328search1 The matrix \(QK^\top\) contains pairwise similarity scores between queries and keys, so each row represents how strongly one token attends to every eligible token.[1] citeturn292328search1 Softmax converts these scores into nonnegative weights that sum to one across the attended positions, and multiplication by \(V\) produces a weighted mixture of their value vectors.[1] citeturn292328search1

The factor \(1/\sqrt{d_k}\) is crucial rather than cosmetic.[1] citeturn292328search1 As key dimensionality grows, unscaled dot products tend to increase in magnitude, which can push softmax into strongly saturated regions with small gradients; scaling counteracts this effect.[1] citeturn292328search1 Dot-product attention is also computationally attractive because its central operations can be expressed as dense matrix multiplications, which are highly optimized on accelerators.[1] citeturn292328search1

A single attention computation, however, compresses all relationships into one similarity geometry, so the Transformer uses **multi-head attention**.[1] citeturn292328search0 For head \(i\),

\[
\text{head}_i
=
\operatorname{Attention}
\left(
QW_i^Q,\,
KW_i^K,\,
VW_i^V
\right),
\]

and the heads are combined as

\[
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}
(\text{head}_1,\ldots,\text{head}_h)W^O .
\]

These learned projections allow different heads to construct different query-key matching spaces and value representations.[1] citeturn292328search0 Intuitively, one head might become useful for nearby syntactic dependencies while another encodes longer-range or semantic associations, although individual heads should not automatically be interpreted as clean symbolic rules because attention patterns are learned distributed representations rather than guaranteed human-readable modules.[1] citeturn292328search0

In self-attention, \(Q\), \(K\), and \(V\) originate from the same sequence representation, which allows every position to contextualize itself using other positions.[1] citeturn292328search0 In encoder-decoder cross-attention, the decoder supplies queries while encoder states supply keys and values, allowing the decoder to retrieve information from the source sequence.[1] citeturn292328search0 Because unrestricted self-attention compares every token with every other token, conventional attention has time and memory requirements that grow quadratically with sequence length, making long contexts expensive.[7] citeturn290239academia3

Each Transformer block also contains a position-wise feed-forward network that independently transforms every token after attention has mixed information across positions.[1] citeturn292328search0 Residual connections and normalization surround these transformations, helping information and gradients propagate through deep stacks.[1] citeturn292328search0 Thus attention provides token-to-token communication, whereas the feed-forward component supplies substantial nonlinear feature transformation at each position.[1] citeturn292328search0

## Positional information, masking, tokenization, and embeddings

Pure self-attention is not inherently sensitive to sequence order, because rearranging tokens and applying the same rearrangement to queries, keys, and values produces correspondingly rearranged outputs unless positional information is introduced.[1] citeturn292328search0 The original Transformer therefore added positional encodings to token embeddings before the first layer.[1] citeturn292328search0 Vaswani and colleagues used fixed sinusoidal functions,

\[
PE_{(pos,2i)}
=
\sin
\left(
pos/10000^{2i/d_{\text{model}}}
\right)
\]

and

\[
PE_{(pos,2i+1)}
=
\cos
\left(
pos/10000^{2i/d_{\text{model}}}
\right),
\]

so different dimensions oscillate at different wavelengths and encode the token's position.[1] citeturn292328search0 They also experimented with learned positional embeddings and reported similar results in their translation setting.[1] citeturn292328search0

Later architectures developed alternatives that inject relative position information more directly into attention.[8] citeturn381790search0 Rotary Position Embedding, or RoPE, represents token position by applying position-dependent rotations to query and key vectors, making their dot products naturally depend on relative displacement between positions.[8] citeturn381790search0 RoPE became particularly influential in decoder-only LLMs; the original LLaMA models, for example, used rotary positional embeddings together with other architectural refinements.[9] citeturn136624search1

Masking determines which positions attention is allowed to inspect.[1] citeturn292328search0 The original encoder uses unrestricted self-attention over its input sequence, whereas the decoder applies a causal, or look-ahead, mask that prevents position \(t\) from seeing positions later than \(t\).[1] citeturn292328search0 Conceptually, masked attention can be written

\[
\operatorname{softmax}
\left(
\frac{QK^\top+M}{\sqrt{d_k}}
\right)V ,
\]

where prohibited elements of \(M\) are assigned \(-\infty\) before softmax, giving future positions zero attention probability.[1] citeturn292328search0 This causal constraint is what makes a decoder-only Transformer a valid autoregressive model: the probability of a token is conditioned only on tokens already available.[2] citeturn136624search4

Before any of this computation occurs, raw text must be converted into discrete token identifiers.[10] citeturn381790academia4 Modern language models commonly use subword tokenization rather than maintaining one vocabulary entry for every possible word.[10] citeturn381790academia4 Sennrich, Haddow, and Birch adapted byte-pair encoding to neural NLP, showing that words could be represented as sequences drawn from a fixed vocabulary of variable-length character fragments and thereby reducing the out-of-vocabulary problem.[10] citeturn381790academia4 SentencePiece later provided language-independent BPE and unigram tokenization that can train directly on raw text without requiring prior whitespace tokenization, an important property for multilingual systems and languages in which word boundaries are not conventionally marked by spaces.[11] citeturn381790search1

A learned embedding matrix maps each token identifier to a continuous vector of dimension \(d_{\text{model}}\), after which positional information is incorporated and the resulting vectors enter the Transformer stack.[1] citeturn292328search0 At the output of an autoregressive language model, the final hidden state is mapped to logits over the vocabulary and normalized into a next-token probability distribution.[2] citeturn136624search4 Tokenization therefore defines the basic discrete units over which language modeling operates, while embeddings provide the continuous representational space in which attention and feed-forward layers perform computation.[1][10] citeturn292328search0turn381790academia4

## Encoder, decoder, and pretraining objectives

The Transformer supports three major architectural configurations that correspond to different ways of exposing context during pretraining.[1][3][4] citeturn292328search0turn292328search2turn136624search0 Encoder-only systems such as BERT process the whole visible input bidirectionally, which makes them particularly natural as representation models for classification, extraction, and sequence understanding.[3] citeturn292328search2 BERT was pretrained primarily by masking some input tokens and training the model to recover them using both left and right context.[3] citeturn292328search2 This differs fundamentally from causal language modeling because a masked token can incorporate evidence from words on both sides.[3] citeturn292328search2

Decoder-only models instead optimize an autoregressive factorization,

\[
P(x_1,\ldots,x_T)
=
\prod_{t=1}^{T}
P(x_t\mid x_{<t}),
\]

so training consists of predicting each next token given its preceding context.[2] citeturn136624search4 GPT used this strategy for generative pretraining, and the same broad paradigm became the dominant foundation for general-purpose generative LLMs.[2][5] citeturn136624search4turn292328academia4 GPT-3 showed that sufficiently large autoregressive models could condition directly on instructions and examples placed in their context, producing substantial zero-shot, one-shot, and few-shot task performance without updating model parameters during evaluation.[5] citeturn292328academia4

Encoder-decoder architectures retain both halves of the original Transformer.[1] citeturn292328search0 T5 treated essentially every NLP task as text-to-text transformation and systematically compared architectures, objectives, datasets, and transfer methods within one framework.[4] citeturn136624search0 Its pretraining framework used corruption-and-reconstruction objectives in which portions of text are replaced and the decoder learns to generate the missing material, combining bidirectional source understanding with autoregressive output generation.[4] citeturn136624search3

Pretraining is powerful because the prediction target can be generated from raw text rather than requiring human labels for every example.[2][3][4] citeturn136624search4turn292328search2turn136624search0 Nonetheless, a pretrained model is not automatically optimized to behave as an interactive assistant.[6] citeturn410184academia9 InstructGPT demonstrated a widely influential post-training pipeline in which a pretrained language model first receives supervised fine-tuning on human-written demonstrations and is subsequently optimized using human preference rankings through reinforcement learning from human feedback.[6] citeturn410184academia9 The study found that human evaluators preferred outputs from its 1.3-billion-parameter InstructGPT model to those from the much larger 175-billion-parameter base GPT-3 on the evaluation distribution, illustrating that behavioral alignment and raw pretraining scale are distinct dimensions.[6] citeturn410184academia9

## Scaling, inference, and efficiency

The emergence of LLMs cannot be explained by Transformer architecture alone; large-scale optimization and data are equally central.[12] citeturn381790search2 Kaplan and colleagues found empirical power-law relationships between language-model cross-entropy loss and model size, dataset size, and training compute over broad experimental ranges.[12] citeturn381790search2 Their results helped formalize the observation that predictable improvements can often be obtained by allocating more parameters, data, and computation.[12] citeturn381790search2

The precise allocation of compute between parameter count and training tokens later proved important.[13] citeturn292328academia6 The Chinchilla study trained more than 400 language models ranging from 70 million to more than 16 billion parameters and concluded that, under its experimental assumptions, compute-optimal scaling called for increasing model size and the number of training tokens together rather than concentrating additional compute mainly on parameters.[13] citeturn292328academia6 Its 70-billion-parameter Chinchilla model used the same stated training compute as the 280-billion-parameter Gopher model but substantially more data, and it outperformed several larger models across the authors' evaluation suite.[13] citeturn292328academia6 The result helped shift the field's emphasis from parameter count alone toward the joint scaling of parameters and training data.[13] citeturn292328academia6

Inference in an autoregressive Transformer has a different performance profile from training.[14] citeturn290239academia4 During training, all positions of a known sequence can be evaluated largely in parallel under a causal mask, whereas generation must normally proceed token by token because the next step depends on the token selected at the previous step.[14] citeturn290239academia4 Implementations therefore cache the previously computed key and value tensors rather than recomputing them from scratch for every generated token, but repeatedly accessing this KV cache can make decoding heavily constrained by memory bandwidth.[14] citeturn290239academia4

Multi-query attention addresses this bottleneck by retaining multiple query heads while sharing a single key and value head, sharply reducing KV-cache size and bandwidth requirements.[14] citeturn290239academia4 Grouped-query attention generalizes that design by dividing query heads into groups that share key-value heads, providing an intermediate point between conventional multi-head attention and multi-query attention.[15] citeturn290239academia5 Ainslie and colleagues reported that GQA could approach multi-head-attention quality while obtaining inference characteristics close to MQA in their experiments.[15] citeturn290239academia5

FlashAttention attacks a different inefficiency.[7] citeturn290239academia3 Rather than approximating attention mathematically, it computes exact attention with a tiled, IO-aware algorithm designed to minimize transfers between slower high-bandwidth GPU memory and faster on-chip memory.[7] citeturn290239academia3 Its authors demonstrated substantial training speedups and showed that hardware-memory traffic can matter as much as nominal arithmetic operation counts when designing efficient Transformer kernels.[7] citeturn290239academia3 FlashAttention does not eliminate the underlying quadratic arithmetic structure of dense attention, but it greatly reduces practical memory overhead and intermediate materialization.[7] citeturn290239academia3

Speculative decoding improves autoregressive generation by using a faster approximation model to propose several tokens, after which the larger target model verifies them in parallel according to a correction procedure that preserves the target sampling distribution.[16] citeturn136624search2 The original study reported two- to three-fold acceleration on T5-XXL compared with its baseline implementation while maintaining identical output distributions.[16] citeturn136624search2 This approach addresses the serial nature of decoding without changing the underlying trained target model.[16] citeturn136624search2

Another path to efficiency is conditional computation.[17] citeturn290239search0 Mixture-of-experts architectures route different tokens to different subsets of feed-forward parameters, allowing total parameter count to grow much faster than the number of parameters activated for any individual token.[17] citeturn290239search0 Switch Transformer simplified expert routing to make sparse models easier to train and demonstrated models reaching trillion-parameter scale while keeping per-token computation far below that of an equivalently sized dense network.[17] citeturn290239search0 The tradeoff is that expert routing introduces communication, load-balancing, memory, and training-stability challenges.[17] citeturn290239search0

## Architectural evolution and persistent limitations

The architecture used in contemporary LLMs is therefore better understood as an evolving family than as a frozen replication of the 2017 Transformer.[1][9] citeturn292328search0turn136624search1 Encoder-only BERT, encoder-decoder T5, and decoder-only GPT represent three major branches built from the same core idea but optimized for different information-flow patterns and objectives.[2][3][4] citeturn136624search4turn292328search2turn136624search0 Modern decoder models have further incorporated alternatives to the original positional scheme, normalization choices, feed-forward activations, and attention organizations; LLaMA, for example, combined RoPE with RMSNorm and SwiGLU-style feed-forward networks as part of a design focused on strong performance from publicly available training data.[9] citeturn136624search1

One persistent limitation is computational scaling with context length.[7] citeturn290239academia3 Dense self-attention forms token-pair interactions whose number grows quadratically with sequence length, so increasing context windows can substantially raise computation and memory requirements even when implementation techniques such as FlashAttention reduce the constant factors.[7] citeturn290239academia3 KV caching reduces redundant computation during autoregressive decoding but creates its own memory footprint, which is one reason MQA and GQA have become important inference optimizations.[14][15] citeturn290239academia4turn290239academia5

A second limitation is that the language-modeling objective is fundamentally predictive rather than truth-verifying.[18] citeturn410184search0 TruthfulQA demonstrated that models can reproduce popular misconceptions present in human-generated text, and its authors argued that increasing scale alone does not guarantee improved truthfulness.[18] citeturn410184search0 More generally, pretrained models learn statistical regularities from their data rather than accessing an intrinsic database of validated propositions, so fluent generation and factual reliability must be treated as separate properties.[18] citeturn410184search0 Post-training methods can improve helpfulness and reduce some classes of undesirable behavior, but InstructGPT still exhibited mistakes despite measurable improvements in human preference and truthfulness-oriented evaluations.[6] citeturn410184academia9

Training data create additional limitations.[19] citeturn410184search3 Bender and colleagues emphasized that web-scale corpora can carry social biases, harmful associations, documentation deficiencies, and representation imbalances, while the financial and environmental costs of ever-larger models create broader questions about how scaling decisions are made.[19] citeturn410184search3 GPT-3's authors likewise documented limitations associated with training on large web-derived corpora and discussed societal impacts alongside capability improvements.[5] citeturn292328academia4 These issues arise from the interaction of architecture, objective, dataset composition, scale, and deployment rather than from attention alone.[5][19] citeturn292328academia4turn410184search3

The Transformer's lasting significance is consequently not that attention solved language understanding in a single algorithmic step, but that it supplied an unusually scalable substrate for representation learning.[1][12] citeturn292328search0turn381790search2 Scaled dot-product attention provides flexible token-to-token information routing; multi-head attention supplies multiple learned interaction spaces; positional representations recover sequence structure; causal masking turns the architecture into an autoregressive generator; subword tokenization makes large open vocabularies tractable; and large-scale self-supervised pretraining converts abundant text into a learning signal.[1][10][12] citeturn292328search0turn381790academia4turn381790search2 Scaling laws, compute-optimal training, sparse experts, efficient attention kernels, KV-cache optimizations, and speculative decoding then transformed that basic architecture into systems that can be trained and served at vastly larger scales.[7][13][15][16][17] citeturn290239academia3turn292328academia6turn290239academia5turn136624search2turn290239search0

The central conceptual insight remains remarkably simple: each token repeatedly asks which other available tokens are useful, retrieves a learned mixture of their information, transforms that representation, and passes it to the next layer.[1] citeturn292328search0 What turned this mechanism into the foundation of LLMs was the discovery that the process remains effective when repeated across many layers, trained over enormous token corpora, scaled to billions of parameters, and combined with objectives and post-training methods that turn generic sequence prediction into broadly useful language behavior.[5][6][12][13] citeturn292328academia4turn410184academia9turn381790search2turn292328academia6

## References

1. Ashish Vaswani et al., **“Attention Is All You Need.”** https://arxiv.org/abs/1706.03762

2. Alec Radford et al., **“Improving Language Understanding by Generative Pre-Training.”** https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

3. Jacob Devlin et al., **“BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.”** https://arxiv.org/abs/1810.04805

4. Colin Raffel et al., **“Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.”** https://www.jmlr.org/papers/v21/20-074.html

5. Tom B. Brown et al., **“Language Models are Few-Shot Learners.”** https://arxiv.org/abs/2005.14165

6. Long Ouyang et al., **“Training Language Models to Follow Instructions with Human Feedback.”** https://arxiv.org/abs/2203.02155

7. Tri Dao et al., **“FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.”** https://arxiv.org/abs/2205.14135

8. Jianlin Su et al., **“RoFormer: Enhanced Transformer with Rotary Position Embedding.”** https://arxiv.org/abs/2104.09864

9. Hugo Touvron et al., **“LLaMA: Open and Efficient Foundation Language Models.”** https://arxiv.org/abs/2302.13971

10. Rico Sennrich, Barry Haddow, and Alexandra Birch, **“Neural Machine Translation of Rare Words with Subword Units.”** https://arxiv.org/abs/1508.07909

11. Taku Kudo and John Richardson, **“SentencePiece: A Simple and Language Independent Subword Tokenizer and Detokenizer for Neural Text Processing.”** https://aclanthology.org/D18-2012/

12. Jared Kaplan et al., **“Scaling Laws for Neural Language Models.”** https://arxiv.org/abs/2001.08361

13. Jordan Hoffmann et al., **“Training Compute-Optimal Large Language Models.”** https://arxiv.org/abs/2203.15556

14. Noam Shazeer, **“Fast Transformer Decoding: One Write-Head is All You Need.”** https://arxiv.org/abs/1911.02150

15. Joshua Ainslie et al., **“GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.”** https://arxiv.org/abs/2305.13245

16. Yaniv Leviathan, Matan Kalman, and Yossi Matias, **“Fast Inference from Transformers via Speculative Decoding.”** https://proceedings.mlr.press/v202/leviathan23a.html

17. William Fedus, Barret Zoph, and Noam Shazeer, **“Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity.”** https://www.jmlr.org/papers/v23/21-0998.html

18. Stephanie Lin, Jacob Hilton, and Owain Evans, **“TruthfulQA: Measuring How Models Mimic Human Falsehoods.”** https://aclanthology.org/2022.acl-long.229/

19. Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell, **“On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?”** https://doi.org/10.1145/3442188.3445922