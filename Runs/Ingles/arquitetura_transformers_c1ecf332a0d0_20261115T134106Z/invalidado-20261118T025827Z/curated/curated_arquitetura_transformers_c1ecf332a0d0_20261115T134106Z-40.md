[referencia=8f0aaf906971379f score=0.946]
## Core Innovation and Architecture

The Transformer's central innovation lies in its exclusive use of attention mechanisms to process sequences. The architecture maintains the successful encoder-decoder framework but reimagines how information flows through the network.

### Multi-Head Self-Attention

The cornerstone of the Transformer is its multi-head self-attention mechanism. Rather than processing sequences sequentially, self-attention allows each position in a sequence to attend to all other positions simultaneously. The mechanism computes attention using three components: queries (Q), keys (K), and values (V).

The scaled dot-product attention function is defined as:

where is the dimension of the keys. The scaling factor prevents the dot products from becoming too large, which would push the softmax function into regions with extremely small gradients.

*Figure 2: Left shows Scaled Dot-Product Attention, right shows Multi-Head Attention which runs multiple attention functions in parallel*

Multi-head attention extends this concept by running multiple attention functions in parallel with different learned projections:

where each and is a learned output projection matrix. This allows the model to jointly attend to information from different representation subspaces, capturing diverse types of relationships within the sequence.

### Encoder-Decoder Structure

The encoder consists of six identical layers, each containing two sub-layers: a multi-head self-attention mechanism and a position-wise feed-forward network. The decoder also has six layers but includes an additional multi-head attention layer that attends to the encoder's output. Crucially, the decoder's self-attention is masked to prevent positions from attending to subsequent positions, preserving the auto-regressive property needed for sequence generation.

### Positional Encoding

Since the model contains no recurrence or convolution, it lacks inherent knowledge of sequence order. To address this, positional encodings are added to the input embeddings using sinusoidal functions:

where is the position and is the dimension. This encoding scheme allows the model to learn relative positions and potentially extrapolate to longer sequences than those seen during training.

---

[referencia=8f0aaf906971379f score=0.632]
## Experimental Results and Performance

The Transformer achieved remarkable results across multiple tasks, fundamentally challenging established approaches in sequence modeling.

### Machine Translation Performance

The model achieved state-of-the-art BLEU scores on two major translation benchmarks:

- **WMT 2014 English-to-German** : 28.4 BLEU (surpassing previous best by over 2.0 BLEU)
- **WMT 2014 English-to-French** : 41.0 BLEU (outperforming all previously published single models)

More importantly, these results were achieved with dramatically reduced training costs. The base model trained in just 12 hours on 8 NVIDIA P100 GPUs, while achieving superior performance to models that required weeks of training.

### Generalization Beyond Translation

To demonstrate broader applicability, the authors applied the Transformer to English constituency parsing. Despite minimal task-specific modifications, the model achieved competitive performance on the Wall Street Journal dataset (91.3 F1) and set a new state-of-the-art F1 score of 92.7 in semi-supervised settings. This was particularly significant because RNN-based models had previously struggled with parsing tasks in small-data regimes.

### Ablation Studies

The paper included comprehensive ablation studies that validated key design choices:

- **Multi-head attention** : Single-head attention performed significantly worse, confirming the benefit of multiple attention heads
- **Attention key dimension** : Reducing the key dimension hurt performance, indicating that compatibility computation requires sufficient dimensionality
- **Model size** : Larger models generally performed better, demonstrating the architecture's scalability
- **Positional encoding** : Learned positional embeddings yielded nearly identical results to sinusoidal encoding

## Attention Visualization and Interpretability

The self-attention mechanism provided an unexpected benefit: improved model interpretability. Visualizations revealed that different attention heads learned to capture distinct linguistic phenomena.

*Figure 3: Attention visualizations showing how different heads focus on different types of relationships, such as syntactic dependencies and long-distance connections*

The attention patterns showed that some heads focused on syntactic relationships, others on semantic dependencies, and some specialized in handling specific linguistic constructions like relative clauses or anaphora resolution. This interpretability offered insights into how the model processes language, something that was difficult to achieve with RNN-based architectures.

---

[referencia=8f0aaf906971379f score=0.282]
## Significance and Impact

The Transformer's impact extends far beyond its immediate technical contributions. By proving that attention mechanisms alone could achieve superior performance while enabling massive parallelization, the paper initiated a paradigm shift in sequence modeling that continues to influence AI research today.

### Computational Efficiency Revolution

The ability to process all positions in a sequence simultaneously, rather than sequentially, addressed the primary computational bottleneck of RNNs. This parallelization reduced training times from weeks or months to hours or days, making it feasible to train much larger models on massive datasets. The efficiency gains accelerated research across the field by enabling rapid experimentation and iteration.

### Foundation for Modern Language Models

Perhaps most significantly, the Transformer became the architectural foundation for the current generation of large language models. Models like BERT (using the encoder component), GPT (using the decoder component), and T5 (using the full encoder-decoder structure) all built directly upon the Transformer architecture. These pre-trained models have revolutionized natural language processing by enabling effective transfer learning across a wide range of tasks.

### Cross-Domain Applications

While demonstrated primarily in NLP, the Transformer's principles have proven broadly applicable. Vision Transformers (ViTs) have successfully adapted the architecture for computer vision tasks, achieving competitive results with convolutional networks. The architecture has also found applications in speech recognition, time series analysis, and even scientific domains like protein structure prediction.

The paper's open-source implementation through TensorFlow's tensor2tensor library further accelerated adoption by lowering barriers to entry for researchers and practitioners worldwide.

## Technical Contributions and Novelty

The Transformer's key contributions can be summarized as:

1. 
**Complete elimination of recurrence** : Demonstrating that sequential processing, long considered essential for sequence modeling, could be entirely replaced by attention mechanisms
2. 
**Scaled dot-product attention** : A computationally efficient attention mechanism that maintains effectiveness while enabling parallelization
3. 
**Multi-head attention** : Allowing the model to attend to different types of information simultaneously through parallel attention heads
4. 
**Architectural simplicity** : Achieving superior results with a cleaner, more interpretable architecture than complex RNN variants

The work fundamentally changed how the field approached sequence modeling problems, shifting focus from sequential architectures to attention-based parallel processing. This shift enabled the scaling that has driven much of the recent progress in AI, making "Attention Is All You Need" one of the most influential papers in modern machine learning.

## Audio

## Similar papers

## Show moreShow less

---

[referencia=8f0aaf906971379f score=0.179]
### Confusion About Variable Length Sequences

This expression describing attention is a little bit confusing to me. It seems to me that the actual structure of a transformer can be applied to sequences of any length. In this case, while both Q and K are NxN matrices where N is sequence length, none of the actual weight matrices depend on N -- why do I see that transformers published on huggingface like https://huggingface.co/meta-llama/Llama-2-7b have a max token length?

This is a good question. The max token length actually has to do with the positional embeddings. You can read more about it here: https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/ .

I think the main reason for the length limit in Llama is that excessively long texts can cause GPU memory to explode during training.

They design in such a way so masked attention(only in decoder) can be applied. Maybe you can design other structures for where the masked attention is no needed.

In brief, there's an O(N<sup>2</sup>) term where N is the sequence length, in the computational complexity of performing a self-attention layer.

I don't believe there's a fundamental reason the sequence length is limited, however there are a few reasons I can think of why a very long sequence can be unwieldy and undesirable.

1.

Computing the K, Q and V representations will each take (embedding-dim) x (weight-dim) x (N) floating point multiply operations.

Computing the attention matrix, i.e. K<sup>T</sup>Q, will take (N) x (weight-dim) x (N) floating point multiply operations. 

Applying the attention matrix to the representation V will also take (N) x (weight-dim) x (N) floating point multiply operations.

In rough terms (we've ignored softmax, additions, and some other aspects), we see the self-attention computation scales with: O(embedding-dim x weight-dim x N) + O(N<sup>2</sup> x weight-dim)

Increases to N, the sequence length, can have a quadratic impact on the computational complexity.

---

[referencia=8f0aaf906971379f score=0.123]
## AI Overview

## Background and Context

The research paper "Attention Is All You Need" was authored by a team of researchers primarily from Google Brain and Google Research, including Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. This work emerged from Google's highly influential AI research divisions, which are renowned for their contributions to deep learning and neural network architectures.

*Figure 1: The Transformer model architecture showing the encoder-decoder structure with multi-head attention mechanisms and feed-forward networks*

Prior to this work, sequence transduction tasks like machine translation were dominated by recurrent neural networks (RNNs), particularly Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) architectures. These models processed sequences token by token, maintaining hidden states that encoded information from previous steps. While effective, RNNs suffered from fundamental limitations: their sequential nature prevented parallelization within training examples, and they struggled with long-range dependencies despite architectural improvements like attention mechanisms that had been added as enhancements.

The Transformer represented a radical departure from this paradigm by proposing an architecture that relied entirely on attention mechanisms, completely eliminating recurrence and convolution as primary computational components.

---

[referencia=8f0aaf906971379f score=0.049]
### # The Dot Product Is Scaffolding

我用自己的话总结了一下：transformer，从NLP领域开启的生成式AI的革命。它的核心就是注意力，最知名的就是论文中的注意力公式。运用注意力机制，建立自然语言的句子/段落的全局视野。获取某token和任意一个token的关联的时间复杂度永远是O（1）。该论文一开始是作为seq2seq，处理自然语言的。它的架构是编码器-解码器架构，然后，采用多头注意力机制，其实就是一个注意力机制做n次，理解的更深更多角度。同时它支持并行。相比于RNN的串行，它的速度并行效率极佳。相比于CNN的视野局限，它直接拥有全局视野，上帝视角。于是，革命开始了。在2017年。

如果只需要一个凭证和自己的IP，通行所有的平台。或者让自己的agent通行所有的平台，那多好呀。

key findings

Why do we scale embedding by sqrt(d_model)?

Here they doing the same

https://www.tensorflow.org/text/tutorials/transformer#the_embedding_and_positional_encoding_layer

Similar discussion here

means

### "Factor"

What does factor mean in this context?

---

[referencia=8f0aaf906971379f score=0.046]
Increases to N, the sequence length, can have a quadratic impact on the computational complexity.

The 7-B model is reported to have required 184K GPU hours to train and the 70-B model 1.7M GPU hours. If we were to increase N by a factor of 4 on the 7-B model, presumably training would take roughly 16 x 184K GPU hours = 2.9M GPU hours. In other words, increasing the sequence length by 4 times makes the smallest model almost twice as computationally expensive as the biggest one!

2. We assumed all matrix multiplies are created equally earlier, or at least they scale linearly with each matrix's dimension. However, if the size of the matrix exceeds your cache sizes or available RAM, the matrix multiply operation will be much, much slower. Very roughly speaking, cache is 100 times faster than RAM which is 1,000 times faster than an SSD (solid state drive). This of course depends on the hardware used for training.

3. As mentioned earlier, positional embeddings schemes may need to be re-designed to accomodate longer sequence lengths (i.e. more possible positions). Though, as long as the sequence length is less than 2<sup>embedding-dim</sup>, I don't think this should be a fundamental issue.

Thanks. I never worried about the size of a model since I only mess with super tiny models(on my 1660)

### How are Keys, Queries, and Values Calculated?

The paper jumps right into key, query, and value matrices which has me a little bit confused. How are these matrices actually produced? The paper mentions that "we compute the dot products of the query with all keys, divide each by sqrt(d<sub>k</sub>), and apply a softmax..." But where did the queries and keys come from?

There are indeed learned weight matrices that are multiplied by each of the input vectors to produce a corresponding key, query, and value. So basically there will be Wq, Wv, and Wk matrices that are each multiplied with the input vector. These matrices are updated via gradient descent.

q=wq @ x

wq is weight tensor ,x is input tensor

simliar to k,v

search this account on twitter ProfTomYeh

then 2024 jul 7, he post the gif.

---

[referencia=8f0aaf906971379f score=0.044]
### Possible to pre combine 2 Ws?

If I don't remember wrong, the formula looks like:

(input@Wq)@(Wk@input)

@ matmul

transpose is ignored.

Can we do input@some [email protected] directly?

Thanks.

Not really sure of what I'm going to say but W_q, W_k are of size d_model x d_k. That is, we have 2xd_k x d_model parameters.

If we want to combine those two in a single matrix, W, it will need to be of size d_model x d_model (because of the sizes of X). So, depending on the sizes of d_model and d_k you are going to have to learn more parameters.

However, once again, this was the reason I came across, I'm sure there are other (better) reasons. I'd be glad if anyone else answered and showed as some research in this direction

Hi.

If I was not too wrong, my guess is that, the seperated form helps training. But I don't have these super big gpus, so I can only wait for any answers.

Haven't have time to make a thorough read, but I believe this might answer our question, maybe you want to give it a look

Someone answered my question. Because the combination requires the model to store a NbyN matrix, and the N is the sequence length.

Not really, right?

Q = X x W<sub>q</sub>, where X is of size N x in_dim and W<sub>q</sub> is of size in_dim x out_dim, where in_dim and out_dim are the dimensions of the input and output embedding. W<sub>q</sub> and W<sub>k</sub> have the same shape.

Then:

QK<sup>T</sup> = X.W<sub>q</sub>.W<sub>K</sub><sup>T</sup>X<sup>T</sup>, then the product W<sub>q</sub>W<sub>k</sub><sup>T</sup> is a matrix

multiplication between matrixes of shape (in_dim x out_dim) x (out_dim x in_dim), getting a final dimension of (in_dim x in_dim)

---

[referencia=8f0aaf906971379f score=0.038]
# Attention Is All You Need

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.0 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## Context readers might want to know

This paper introduced the Transformer, an architecture that became foundational to modern artificial intelligence. Originally developed for machine translation, it provided the architectural basis for BERT and GPT-3, and was subsequently adapted to image recognition through the Vision Transformer. Its influence extended beyond its original task to shape the development of large language models and learning across multiple modalities.

## AI Overview

---

[referencia=8f0aaf906971379f score=0.031]
### Layer norm

Why is *layer norm* effective?

Xu et al find that Layer Norm's effectiveness is attributable to the importance of the mean + variance of a particular layer. In particular, mean + variance re-center and re-scale the backward gradients.

rmsnorm make its training more stable ,becase rmsnorm ensure the gradient not rely on the scale of input any more

This probably shouldn't even be called attention. And the dot product is the worst function I tested. https://medium.com/@mbonsign/the-dot-product-is-scaffolding-b42a0e4c5794.

### Equation 1

Does this mean that attention scales quadratically with respect to sequence length?

yes, training in self-attention scales quadratically with sequence length. This is one of the scaling issues that are mitigated by future works like Linear Transformer, H3, and RetNet (see Table 1 on page 6 of https://alphaxiv.org/abs/2307.08621 )

Although some successor have been tried, in the end, none really ended up in production. The biggest limitation was the quadratic cost in memory, which was fixed by flash attention (https://alphaxiv.org/abs/2205.14135). The quadratic cost in runtime in practice is solved by faster machines. And also, LLMs don't really scale to big sequence length. Some papers claim they achieve 1M tokens, but in practice information in the middle is never taken into account. So with this architecture, that is not the main limitation.

There are some up and coming successors, although whether they will ever rival the performance of a transformer is up for debate. I'd take a look at RWKV, whose author also has some notes on alphaXiv: RWKV .

---

[referencia=8f0aaf906971379f score=0.000]
Submitted 01 Jul 2017

Newer version published 02 Aug 2023, read v7

---

[referencia=8f0aaf906971379f score=0.000]
## Discussion

30