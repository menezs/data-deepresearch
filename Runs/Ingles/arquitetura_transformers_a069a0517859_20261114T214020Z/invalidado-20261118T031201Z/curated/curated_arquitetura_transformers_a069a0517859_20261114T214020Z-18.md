[referencia=a7468c6851652691 score=0.964]
The two most commonly used attention functions are additive attention [2], and dot-product (multi-2], and dot-product (multi-], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of <u>1</u><sup>Additive attention computes the compatibility function using a feed-forward network with</sup> _~~√~~ dkk_<sup>.</sup> a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. 

Instead of performing a single attention function with _d_ model-dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values _h_ times with different, learned linear projections to _dk_ , _dk_ and _dv_ dimensions, respectively. On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding _dv_ -dimensional 4To illustrate why the dot products get large, assume that the components of _q_ and _k_ are independent random variables with mean 0 and variance 1. Then their dot product, _q · k_ =<sup>�</sup><sup>_d_</sup> _i_ =1<sup>_kqiki_, has mean 0 and variance</sup><sup>_dk_.</sup> 

4 

output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2. 

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this. 

MultiHead( _Q, K, V_ ) = Concat(head1 _, ...,_ headh) _W_<sup>_O_</sup>

---

[referencia=ab38f2e1ef39faa3 score=0.963]
In this work we employ h=8 parallel attention layers, or heads. For each of these we use d_k=d_v=d_{\text{model}}/h=64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.

```
class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        "Take in model size and number of heads."
        super(MultiHeadedAttention, self).__init__()
        assert d_model % h == 0
        # We assume d_v always equals d_k
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.attn = None
        self.dropout = nn.Dropout(p=dropout)
    def forward(self, query, key, value, mask=None):
        "Implements Figure 2"
        if mask is not None:
            # Same mask applied to all h heads.
            mask = mask.unsqueeze(1)
        nbatches = query.size(0)
        # 1) Do all the linear projections in batch from d_model => h x d_k
        query, key, value = [
            lin(x).view(nbatches, -1, self.h, self.d_k).transpose(1, 2)
            for lin, x in zip(self.linears, (query, key, value))
        ]
        # 2) Apply attention on all the projected vectors in batch.
        x, self.attn = attention(
            query, key, value, mask=mask, dropout=self.dropout
        )
        # 3) "Concat" using a view and apply a final linear.
        x = (
            x.transpose(1, 2)
            .contiguous()
            .view(nbatches, -1, self.h * self.d_k)
        )
        del query
        del key
        del value
        return self.linears[-1](x)

---

[referencia=ab38f2e1ef39faa3 score=0.956]
The two most commonly used attention functions are additive attention (cite), and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of \frac{1}{\sqrt{d_k}}. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.

While for small values of d_k the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of d_k (cite). We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients (To illustrate why the dot products get large, assume that the components of q and k are independent random variables with mean 0 and variance 1. Then their dot product, q \cdot k = \sum_{i=1}^{d_k} q_ik_i, has mean 0 and variance d_k.). To counteract this effect, we scale the dot products by \frac{1}{\sqrt{d_k}}.

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.

\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head_1}, ..., \mathrm{head_h})W^O \\ \text{where}~\mathrm{head_i} = \mathrm{Attention}(QW^Q_i, KW^K_i, VW^V_i)

Where the projections are parameter matrices W^Q_i \in \mathbb{R}^{d_{\text{model}} \times d_k}, W^K_i \in \mathbb{R}^{d_{\text{model}} \times d_k}, W^V_i \in \mathbb{R}^{d_{\text{model}} \times d_v} and W^O \in \mathbb{R}^{hd_v \times d_{\text{model}}}.

In this work we employ h=8 parallel attention layers, or heads. For each of these we use d_k=d_v=d_{\text{model}}/h=64.

---

[referencia=a7468c6851652691 score=0.913]
MultiHead( _Q, K, V_ ) = Concat(head1 _, ...,_ headh) _W_<sup>_O_</sup> 



Where the projections are parameter matrices _Wi_<sup>_Q_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_K_</sup> _∈_ R<sup>_d_model</sup><sup>_×dk_</sup> , _Wi_<sup>_V_</sup> _∈_ R<sup>_d_model</sup><sup>_×dv_</sup> and _W_<sup>_O_</sup> _∈_ R<sup>_hdv×d_model</sup> . 

In this work we employ _h_ = 8 parallel attention layers, or heads. For each of these we use _dk_ = _dv_ = _d_ model _/h_ = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality. 

### **3.2.3 Applications of Attention in our Model** 

The Transformer uses multi-head attention in three different ways: 

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. 

- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. 

- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to _−∞_ ) all values in the input of the softmax which correspond to illegal connections. See Figure 2.

---

[referencia=a7468c6851652691 score=0.593]
development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3. 

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads. 

In Table 3 rows (B), we observe that reducing the attention key size _dk_ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

---

[referencia=ab38f2e1ef39faa3 score=0.568]
```
The Transformer uses multi-head attention in three different ways: 1) In “encoder-decoder attention” layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as (cite).

The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.

Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to -\infty) all values in the input of the softmax which correspond to illegal connections.

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between.

\mathrm{FFN}(x)=\max(0, xW_1 + b_1) W_2 + b_2

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is d_{\text{model}}=512, and the inner-layer has dimensionality d_{ff}=2048.

```
class PositionwiseFeedForward(nn.Module):
    "Implements FFN equation."
    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)
    def forward(self, x):
        return self.w_2(self.dropout(self.w_1(x).relu()))

---

[referencia=ab38f2e1ef39faa3 score=0.435]
```
My comments are blockquoted. The main text is all from the paper itself.


The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU, ByteNet and ConvS2S, all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention.

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations. End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks.

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence aligned RNNs or convolution.

Most competitive neural sequence transduction models have an encoder-decoder structure (cite). Here, the encoder maps an input sequence of symbol representations (x_1, ..., x_n) to a sequence of continuous representations \mathbf{z} = (z_1, ..., z_n). Given \mathbf{z}, the decoder then generates an output sequence (y_1,...,y_m) of symbols one element at a time. At each step the model is auto-regressive (cite), consuming the previously generated symbols as additional input when generating the next.

```

---

[referencia=a7468c6851652691 score=0.422]
## **2 Background** 

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2. 

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22]. 

End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34]. 

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequencealigned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

---

[referencia=a7468c6851652691 score=0.401]
## **3 Model Architecture** 

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations ( _x_ 1 _, ..., xn_ ) to a sequence of continuous representations **z** = ( _z_ 1 _, ..., zn_ ). Given **z** , the decoder then generates an output sequence ( _y_ 1 _, ..., ym_ ) of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next. 

2 



Figure 1: The Transformer - model architecture. 

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively. 

### **3.1 Encoder and Decoder Stacks** 

**Encoder:** The encoder is composed of a stack of _N_ = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is LayerNorm( _x_ + Sublayer( _x_ )), where Sublayer( _x_ ) is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension _d_ model = 512. 

**Decoder:** The decoder is also composed of a stack of _N_ = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position _i_ can depend only on the known outputs at positions less than _i_ .

---

[referencia=a7468c6851652691 score=0.360]
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

---

[referencia=a7468c6851652691 score=0.349]
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

[referencia=ab38f2e1ef39faa3 score=0.282]
```
We employ a residual connection (cite) around each of the two sub-layers, followed by layer normalization (cite).

```
class LayerNorm(nn.Module):
    "Construct a layernorm module (See citation for details)."
    def __init__(self, features, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.a_2 = nn.Parameter(torch.ones(features))
        self.b_2 = nn.Parameter(torch.zeros(features))
        self.eps = eps
    def forward(self, x):
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        return self.a_2 * (x - mean) / (std + self.eps) + self.b_2
```
That is, the output of each sub-layer is \mathrm{LayerNorm}(x + \mathrm{Sublayer}(x)), where \mathrm{Sublayer}(x) is the function implemented by the sub-layer itself. We apply dropout (cite) to the output of each sub-layer, before it is added to the sub-layer input and normalized.

To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_{\text{model}}=512.

```
class SublayerConnection(nn.Module):
    """
    A residual connection followed by a layer norm.
    Note for code simplicity the norm is first as opposed to last.
    """
    def __init__(self, size, dropout):
        super(SublayerConnection, self).__init__()
        self.norm = LayerNorm(size)
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, sublayer):
        "Apply residual connection to any sublayer with the same size."
        return x + self.dropout(sublayer(self.norm(x)))
```
Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.

```

---

[referencia=ab38f2e1ef39faa3 score=0.209]
```
Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.

```
class EncoderLayer(nn.Module):
    "Encoder is made up of self-attn and feed forward (defined below)"
    def __init__(self, size, self_attn, feed_forward, dropout):
        super(EncoderLayer, self).__init__()
        self.self_attn = self_attn
        self.feed_forward = feed_forward
        self.sublayer = clones(SublayerConnection(size, dropout), 2)
        self.size = size
    def forward(self, x, mask):
        "Follow Figure 1 (left) for connections."
        x = self.sublayer[0](x, lambda x: self.self_attn(x, x, x, mask))
        return self.sublayer[1](x, self.feed_forward)
```
The decoder is also composed of a stack of N=6 identical layers.

```
class Decoder(nn.Module):
    "Generic N layer decoder with masking."
    def __init__(self, layer, N):
        super(Decoder, self).__init__()
        self.layers = clones(layer, N)
        self.norm = LayerNorm(layer.size)
    def forward(self, x, memory, src_mask, tgt_mask):
        for layer in self.layers:
            x = layer(x, memory, src_mask, tgt_mask)
        return self.norm(x)
```
In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization.

```

---

[referencia=a7468c6851652691 score=0.193]
14 



<!-- Start of picture text -->
Figure 5: Many of the attention heads exhibit behaviour that seems related to the structure of the<br>sentence. We give two such examples above, from two different heads from the encoder self-attention<br>at layer 5 of 6. The heads clearly learned to perform different tasks.<br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br><!-- End of picture text -->

15

---

[referencia=a7468c6851652691 score=0.175]
### A single convolutional layer with kernel width _k < n_ does not connect all pairs of input and output 

positions. Doing so requires a stack of _O_ ( _n/k_ ) convolutional layers in the case of contiguous kernels, or _O_ ( _logk_ ( _n_ )) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of _k_ . Separable convolutions [6], however, decrease the complexity considerably, to _O_ ( _k · n · d_ + _n · d_<sup>2</sup> ). Even with _k_ = _n_ , however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model. 

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

---

[referencia=a7468c6851652691 score=0.112]
## **Attention Visualizations** 



<!-- Start of picture text -->
It is in this spirit that a majority of American governments have passed new laws since 2009 making the registration or voting process more difficult . <EOS> <pad> <pad> <pad> <pad> <pad> <pad><br>It is in this spirit that a majority of American governments have passed new laws since 2009 making the registration or voting process more difficult . <EOS> <pad> <pad> <pad> <pad> <pad> <pad><br><!-- End of picture text -->

Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads attend to a distant dependency of the verb ‘making’, completing the phrase ‘making...more difficult’. Attentions here shown only for the word ‘making’. Different colors represent different heads. Best viewed in color. 

13 



<!-- Start of picture text -->
The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br>The Law will never be perfect , but its application should be just - this is what we are missing , in my opinion . <EOS> <pad><br><!-- End of picture text -->

Figure 4: Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions from just the word ‘its’ for attention heads 5 and 6. Note that the attentions are very sharp for this word. 

14 



<!-- Start of picture text -->

---

[referencia=ab38f2e1ef39faa3 score=0.111]
def make_model(
    src_vocab, tgt_vocab, N=6, d_model=512, d_ff=2048, h=8, dropout=0.1
):
    "Helper: Construct a model from hyperparameters."
    c = copy.deepcopy
    attn = MultiHeadedAttention(h, d_model)
    ff = PositionwiseFeedForward(d_model, d_ff, dropout)
    position = PositionalEncoding(d_model, dropout)
    model = EncoderDecoder(
        Encoder(EncoderLayer(d_model, c(attn), c(ff), dropout), N),
        Decoder(DecoderLayer(d_model, c(attn), c(attn), c(ff), dropout), N),
        nn.Sequential(Embeddings(d_model, src_vocab), c(position)),
        nn.Sequential(Embeddings(d_model, tgt_vocab), c(position)),
        Generator(d_model, tgt_vocab),
    )
    # This was important from their code.
    # Initialize parameters with Glorot / fan_avg.
    for p in model.parameters():
        if p.dim() > 1:
            nn.init.xavier_uniform_(p)
    return model
```
Here we make a forward step to generate a prediction of the model. We try to use our transformer to memorize the input. As you will see the output is randomly generated due to the fact that the model is not trained yet. In the next tutorial we will build the training function and try to train our model to memorize the numbers from 1 to 10.


```

---

[referencia=a7468c6851652691 score=0.093]
## **1 Introduction** 

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15]. 

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states _ht_ , as a function of the previous hidden state _ht−_ 1 and the input for position _t_ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains. 

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network. 

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

---

[referencia=ab38f2e1ef39faa3 score=0.091]
```
Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension d_{\text{model}}. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to (cite). In the embedding layers, we multiply those weights by \sqrt{d_{\text{model}}}.

```
class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        super(Embeddings, self).__init__()
        self.lut = nn.Embedding(vocab, d_model)
        self.d_model = d_model
    def forward(self, x):
        return self.lut(x) * math.sqrt(self.d_model)
```
Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add “positional encodings” to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d_{\text{model}} as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed (cite).

In this work, we use sine and cosine functions of different frequencies:

PE_{(pos,2i)} = \sin(pos / 10000^{2i/d_{\text{model}}})

PE_{(pos,2i+1)} = \cos(pos / 10000^{2i/d_{\text{model}}})

where pos is the position and i is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2\pi to 10000 \cdot 2\pi. We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PE_{pos+k} can be represented as a linear function of PE_{pos}.

In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of P_{drop}=0.1.

```

---

[referencia=a7468c6851652691 score=0.078]
## **7 Conclusion** 

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. 

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles. 

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours. 

The code we used to train and evaluate our models is available at `https://github.com/ tensorflow/tensor2tensor` . 

**Acknowledgements** We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.