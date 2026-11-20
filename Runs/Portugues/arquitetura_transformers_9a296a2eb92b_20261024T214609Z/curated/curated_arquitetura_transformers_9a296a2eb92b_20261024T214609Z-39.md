[referencia=b8b957c4b0d92246 score=0.001]
## Context without a chain

An encoder builds representations of the input, and a decoder uses them to produce a translation. In the paper's model, each of six encoder layers combines multi-head self-attention with a position-wise feed-forward layer. The six decoder layers add attention to the encoder output.

In attention, a token compares its query with keys for available tokens. It turns those comparisons into weights and uses the weights to combine the corresponding values. Multiple learned heads perform this operation in parallel. This lets the model draw on different representation subspaces instead of averaging everything through one head. Attention alone does not encode word order, so position information is added to token embeddings. The decoder masks later positions, so a prediction cannot use future target words.

These choices have a cost and a condition. A self-attention layer uses a constant number of sequential operations across sequence positions, while a recurrent layer needs a number that grows with sequence length. Self-attention arithmetic scales quadratically with sequence length. The authors say it is faster than recurrent arithmetic when sequence length is smaller than representation width.

Conceptual animation from Jakob Uszkoreit's author post. It starts with initial word embeddings and adds sentence-wide context through self-attention, repeating this step for all words in parallel. The decoder generates output words left-to-right while attending to encoder representations.

---

[referencia=b8b957c4b0d92246 score=0.001]
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

[referencia=b8b957c4b0d92246 score=0.001]
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

[referencia=b8b957c4b0d92246 score=0.000]
# Attention Is All You Need

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## AI Overview

Translation requires a model to use context from across a sentence. Recurrent models process input positions in sequence, which limits parallel work within a training example, especially as sequences get longer. The Transformer lets tokens exchange context directly instead. The encoder can then process positions in parallel, and the decoder can be trained on positions in parallel with a causal mask. Output generation remains sequential: the decoder is autoregressive and produces output tokens one at a time at inference.

---

[referencia=b8b957c4b0d92246 score=0.000]
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

[referencia=b8b957c4b0d92246 score=0.000]
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

[referencia=b8b957c4b0d92246 score=0.000]
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

[referencia=b8b957c4b0d92246 score=0.000]
## Discussion

30

---

[referencia=b8b957c4b0d92246 score=0.000]
## Does quality hold up?

BLEU is a reference-based translation score, and higher is better. On WMT 2014 English-to-German newstest2014, Transformer big scores 28.4. The best listed prior ensemble, ConvS2S Ensemble, scores 26.36. Table 2 reports estimated training costs of 2.3 × 10¹⁹ FLOPs for Transformer big and 7.7 × 10¹⁹ FLOPs for ConvS2S Ensemble. These are estimates, not a controlled elapsed-time comparison. Transformer big took 3.5 days on eight P100 GPUs. The comparison does not establish lower compute than every prior model.

The head-count ablation is the mechanism-specific comparison. Table 3 evaluates variants on the English-to-German development set, newstest2013, without checkpoint averaging. Row (A) varies head count and per-head key/value widths at roughly constant computation:

- The eight-head base model scores 25.8 BLEU.
- A one-head, 512-dimensional setting scores 24.9.
- With 32 heads, the score is 25.4.

The authors say quality falls with one head and with too many heads. Per-head dimensions change along with head count, so this supports the multi-head design without showing that head count alone caused the difference.

## What the result establishes

The Transformer changes where a model gathers context: through direct links between sentence positions instead of a chain of state updates. This makes context-building parallel during training, while generation stays one token at a time. A single model beats a prior ensemble on English-to-German with lower estimated compute. However, no matched recurrent or convolutional control isolates self-attention as the sole cause of that improvement.

## Audio

## Transcript

## Similar papers

---

[referencia=b8b957c4b0d92246 score=0.000]
Submitted 02 Aug 2023