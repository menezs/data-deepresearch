[referencia=65fa01dbc0699c35 score=0.427]
As usual, here I test the `FeedForward()` class by passing through a tensor of size `BATCH_SIZE`×`SEQ_LENGTH`×`D_MODEL` as shown in Codeblock 17.

We can see in the output above that the dimensionality of each token, which is initially 512, becomes 2048 thanks to the `self.linear_0` layer (`#(1)`). This tensor size remains unchanged until the dropout layer before eventually squeezed back to 512 by the `self.linear_1` layer (`#(2)`).

---

[referencia=65fa01dbc0699c35 score=0.048]
## Feed Forward Blocks

Our previous discussion about attention mechanism was quite intense, especially for those who have never heard about this before - well, at least for me when I first tried to understand this idea. - To give our brain a little bit of rest, let's shift our focus to the simplest component of Transformer: the Feed Forward block.

In the Transformer architecture, you will find two identical Feed Forward blocks - one in the Encoder and another one in the Decoder. Take a look at Figure 13 below to see where they are located. By implementing Feed Forward blocks like this, the depth of the network will increase, and so does the number of learnable parameters. This allows the network to capture more complex patterns in the data so that it does not rely solely on the information extracted by the attention blocks.

Each of the two Feed Forward blocks above consists of a stack of two linear layers with a ReLU activation function and a dropout layer in between. The implementation of this structure is very easy, as you can just stack these layers one after another like what I do in Codeblock 16 below.

There are several things I want to emphasize in the above codeblock. First the `self.linear_0` layer is configured to accept a tensor of size `D_MODEL` (512) and expands it to `HIDDEN_DIM` (2048) as shown at line `#(1)`. As I've mentioned earlier, we do this so that the model can extract more information from the dataset. This tensor dimension will eventually be shrunk back down to 512 by the `self.linear_1` layer (`#(3)`), which helps keep the input and output dimensions consistent throughout the network. Next, here we set the rate of our dropout layer to `DROP_PROB` (0.1) (`#(2)`) according to the configuration table provided in Figure 2. As for the `forward()` method, I won't go into the details as it simply connects the layers we initialized in the `__init__()` method.

As usual, here I test the `FeedForward()` class by passing through a tensor of size `BATCH_SIZE`×`SEQ_LENGTH`×`D_MODEL` as shown in Codeblock 17.

---

[referencia=65fa01dbc0699c35 score=0.042]
Still with Codeblock 2, here I set the `BATCH_SIZE` to 1 (`#(4)`). You can actually use any number for the batch size since it does not affect the model architecture at all. The `D_MODEL` and `NUM_HEADS` parameters on the other hand, are something that you cannot choose arbitrarily, in a sense that `D_MODEL` (`#(5)`) needs to be divisible by `NUM_HEADS` (`#(6)`). The `D_MODEL` itself corresponds to the model dimension, which is actually also equivalent to the ***embedding dimension***. This notion implies that every single token is going to be represented as a vector of size 512. Meanwhile, `NUM_HEADS=8` means that there will be 8 heads inside a Multihead Attention layer. Later on, the 512 features of each token will be spread evenly into these 8 attention heads, so every single head will be responsible for handling 64 features (`HEAD_DIM`) as marked at line `#(7)`. The `HIDDEN_DIM` parameter, which the value is set to 2048 (`#(8)`), denotes the number of neurons in the hidden layer inside the Feed Forward blocks. Next, if you go back to Figure 1, you will notice that there is a symbol *N×* next to the Encoder and the Decoder which essentially means that we can stack them *N* times. In this case, we set it to 6 as marked at line `#(9)`. Lastly, we can also control the rate of the dropout layers through the `DROP_PROB` parameter (`#(10)`).

In fact, all the parameter values I set above are taken from the *base* configuration of the Transformer model shown in the figure below.

---

[referencia=65fa01dbc0699c35 score=0.002]
Let's test the code by running the codeblock below. - By the way, here I re-run all previous codeblocks with the `print()` function commented out since I only want to focus on the flow of the `SelfAttention()` class we just created.

Based on the output above, we can see that our tensor successfully flows through all the layers. The input tensor, which initially has the size of 200×512 (`#(1)`), becomes 200×1536 thanks to the expansion done by the first linear layer (`#(2)`). The last dimension of the tensor is then distributed evenly into 8 attention heads, resulting in each head processing 192-dimensional token vectors (`#(3)`). The permutation done to swap the 8-attention head axis with the 200-sequence length axis is essentially just a method that allows PyTorch to do the computation for each head in parallel (`#(4)`). Next, at line `#(5)` to `#(7)` you can see that each of the `q`, `k`, and `v` tensors has the dimension of 200×64 for each head, which matches our discussion for Codeblock 9. After being processed with `Attention()` layer, we got the `attn_output` tensor which is then permuted (`#(9)`) and reshaped (`#(10)`) to the original input tensor dimension. - It is important to note that the permutation and reshaping operations need to be performed in this exact order because we initially changed its dimension by reshaping followed by a permutation. Technically, you could revert to the original dimension without permuting, but that would mess up your tensor elements. So, you really need to keep this in mind. - Finally, the last step to be done is to pass the tensor through the second linear layer in the `SelfAttention()` block, which does not change the tensor dimension at all (`#(11)`).

---

[referencia=65fa01dbc0699c35 score=0.002]
Now let's test our `CrossAttention()` class by passing dummy `x_enc` and `x_dec` tensors. See Codeblock 15 and the output below for the details.

Initially, both `x_enc` and `x_dec` tensors have the exact same dimensions, as shown at line `#(1)` and `#(2)` in the above output. After being passed through the `self.kv_linear` layer, the embedding dimension of `x_enc` expands from 512 to 1024 (`#(3)`). This means that each token is now represented by a 1024-dimensional vector. This tensor is then reshaped, permuted, and chunked, so that it becomes `k` and `v`. At this point the embedding dimensions of these two tensors are already split into 8 attention heads, ready to be used as the input for the Scaled Dot-Product Attention layer (`#(4)` and `#(5)`). We do also apply the reshaping and permuting steps to `x_dec`, yet we omit the chunking process since this entire tensor will act as the `q` (`#(6)`). As the process is done, now that the `q`, `k`, and `v` tensors are having the exact same dimensions, which is the same as what we have earlier in the `SelfAttention()` block. Processing with the `self.attention` layer results in `attn_output` tensor (`#(7)`) which will later be permuted and reshaped back to the initial tensor dimension (`#(8)`). Finally, after being processed with `self.linear` layer (`#(9)`), our tensor is now containing the translated language which already has the contextual information from the original language.

---

[referencia=65fa01dbc0699c35 score=0.001]
## Layer Normalization

The last Transformer component I want to talk about is the one that you can see throughout the entire Encoder and Decoder, namely the Add & Norm block (colored in yellow in Figure 14).

As the name suggests, this block essentially comprises an element-wise addition and a layer normalization operation. However, for the sake of simplicity, in this section I will only focus on the normalization process. The element-wise addition will later be discussed when we assemble the entire Transformer architecture.

The purpose of implementing layer normalization in this case is to normalize the tensor right after being processed by the preceding block. Keep in mind that what we use here is *layer* normalization, not *batch* normalization. In case you're not yet familiar with Layer Norm, it essentially performs normalization where the statistics (i.e., mean and variance) are computed across the features (embedding dimensions) for each individual token. This is essentially the reason that in Figure 15 the color that I use for all embedding dimensions is the same for each token. On the other hand, in Batch Norm, the cells that have the same color spans across its batch and sequence dimension, indicating that the mean and variance are computed based on these axes.

You can see the implementation of a layer normalization mechanism in Codeblock 18. There are several variables that I need to initialize within the `__init__()` method of the `LayerNorm()` class. First, there is a small number called *epsilon* (`#(1)`), which we need to define to prevent a division-by-zero error that potentially occur at line `#(8)`. Next, we also need to initialize *gamma* (`#(2)`) and *beta* (`#(3)`). These two variables can be thought of as weight and bias in linear regression, where the *gamma* is responsible to scale the normalized output, whereas *beta* is for shifting it. By understanding this property, if we set *gamma* to be fixed to 1 and the *beta* to 0, then the normalized output values won't change. However, although we indeed use these two numbers for the initial *gamma* and *beta*, yet I set the `requires_grad` parameter to `True` so that they will get updated as the training goes.

---

[referencia=65fa01dbc0699c35 score=0.001]
The way our `forward()` method works is a little bit unusual. Remember that the entire Transformer accepts two inputs: a sequence from the original language, and the *shifted-right* sequence from the translated language. Hence, in Codeblock 25 below, you will see that this method accepts two sequences: `x_enc_raw` and `x_dec_raw` (`#(1)`). The `_raw` suffix I use indicates that it is a raw token sequence, i.e., a sequence of integers, not the tokens that have been converted into 512-dimensional vectors. This conversion will then be done at line `#(2)` and `#(5)`. Afterwards, we will inject positional encoding to the resulting tensors by element-wise addition, which is done at line `#(3)` for the sequence to be fed into the Encoder, and `#(6)` for the one to be passed through the Decoder. Next, we use a loop to feed the output of an Encoder block into the subsequent one sequentially (`#(4)`). We also do the similar thing to the Decoder blocks, except that each of these accepts both `x_enc` and `x_dec` (`#(7)`). What you need to notice at this point is that the `x_enc` to be fed into the Decoder block is only the one coming out from the last Encoder block. Meanwhile, the `x_dec` tensor to be fed into the next Decoder is always the one produced by the previous Decoder block. - You can verify this by taking a closer look at line `#(7)`, where `x_dec` is updated at each iteration while `x_enc` is not. - Lastly, once the Decoder loop is completed, we will pass the resulting tensor to the linear layer (`#(8)`). If you take a look at Figure 18, you will notice that there is a softmax layer placed after this linear layer. However, we won't implement it here because in PyTorch it is already included in the loss function.

As the `Transformer()` class is completed, now that we can test it with the following codeblock. You can see in the resulting output that our `x_enc_raw` and `x_dec_raw` successfully passed through the entire Transformer architecture, which essentially means that our network is finally ready to be trained for *seq2seq* tasks.

---

[referencia=65fa01dbc0699c35 score=0.001]
Now let's move on to the `forward()` method of the `SelfAttention()` class. Below is what it looks like.

Here we can see that the input tensor `x` is directly processed with the `self.qkv_linear` layer (`#(1)`). The resulting tensor is then reshaped to `BATCH_SIZE` × `SEQ_LENGTH` × `NUM_HEADS` × `3*HEAD_DIM` as demonstrated at line `#(2)`. Next, the `permute()` method is used to swap the `SEQ_LENGTH` and `NUM_HEADS` axes (`#(3)`). Such a reshaping and permutation process is actually a trick to distribute the 1536-dimensional token vectors into 8 attention heads, allowing them to be processed in parallel without needing to be separated into different tensors. Next, we use the `chunk()` method to divide the tensor into 3 parts, which will correspond to `q`, `k` and `v` (`#(4)`). One thing to keep in mind is that the division will operate on the last (token embedding) dimension, leaving the sequence length axis unchanged.

With the *query,* *key,* and *value* ready, we can now pass them all together through the Scaled Dot-Product Attention block (`#(5)`). Although the attention mechanism returns two tensors, in this case we will only bring `attn_output` to the next process since it is the one that actually contains the context-aware token sequence (recall that `attn_output_weights` is just a matrix containing the relationships between tokens). The next step to be done is to swap back the `HEAD_DIM` and the `SEQ_LENGTH` axes (`#(6)`) before eventually reshaping it back to the original dimension (`#(7)`). If you take a closer look at this line, you will see that `NUM_HEADS` is directly multiplied with `HEAD_DIM`. This operation effectively flattens the embeddings from the 8 attention heads back into a single dimension, which is conceptually similar to concatenating the output of each head together, as illustrated in Figure 7. Lastly, to actually combine the information from these 8 heads, we need to pass the tensor through another linear layer we discussed earlier (`#(8)`). We can think of the operation done in this linear layer as an approach to let the attention heads interacting with each other, which results in a better context understanding.

---

[referencia=65fa01dbc0699c35 score=0.001]
To the `forward()` method, it initially works by accepting tensor `x` (`#(4)`). Afterwards, we calculate the mean (`#(5)`) and variance (`#(6)`) from it. Remember that because we want to compute these statistics from each row, hence we need to use `dim=[-1]` (since the embedding dimension is the last axis of the tensor). Next, we calculate the standard deviation (`#(7)`) so that the normalized tensor can be obtained (`#(8)`). Lastly, this normalized tensor will be rescaled using `self.gamma` and `self.beta` as shown at line `#(9)`.

As the `LayerNorm()` class has successfully been constructed, now that we will run the following codeblock to check if our implementation is correct.

We can see in the output above that all processes done inside the `LayerNorm()` class do not alter the tensor dimension at all. The `mean`, `var`, and `stddev` are just the statistics that we compute for each row (token), hence the embedding dimension collapses to 1 for these tensors. By the way, in case you're wondering why we use `keepdim=True`, it is because setting it to `False` would result in `mean`, `var`, and `stddev` having the dimension of 1×200 rather than 1×200×1, which causes these tensors to be incompatible for the subsequent operations.

---

[referencia=65fa01dbc0699c35 score=0.001]
The `x_enc` and `x_dec` tensors are processed separately using similar steps to those in the Self-Attention layer, i.e., processing with linear layer, reshaping, and permuting. Notice that the processes done for these two input tensors are essentially the same. For example, line `#(2)` is equivalent to line `#(6)`, line `#(3)` corresponds to line `#(7)`, and line `#(4)` matches line `#(8)`. We apply the `chunk()` method to split the `x_enc` tensor into *key* and *value* (`#(5)`), whereas in the case of `x_dec`, we don't need to do so as it will directly serve as the *query* tensor. Next, we feed `q`, `k`, and `v` into the Scaled Dot-Product Attention layer (`#(9)`). This is actually the step where the information from the Encoder is queried by the Decoder. Additionally, keep in mind that here we should not pass the *look-ahead* mask parameter since we want to leave the attention weights unmasked. Next, I don't think I need to explain the remaining steps because these are all exactly the same as the one in the Multihead Self-Attention mechanism, which we already discussed in the previous section.

Now let's test our `CrossAttention()` class by passing dummy `x_enc` and `x_dec` tensors. See Codeblock 15 and the output below for the details.

---

[referencia=65fa01dbc0699c35 score=0.001]
## Introduction

As the title suggests, in this article I am going to implement the Transformer architecture from scratch with PyTorch - yes, literally from scratch. Before we get into it, let me provide a brief overview of the architecture. Transformer was first introduced in a paper titled "*Attention Is All You Need*" written by Vaswani et al. back in 2017 [1]. This neural network model is designed to perform *seq2seq* (Sequence-to-Sequence) tasks, where it accepts a sequence as the input and is expected to return another sequence for the output such as machine translation and question answering.

Before Transformer was introduced, we usually used RNN-based models like LSTM or GRU to accomplish *seq2seq* tasks. These models are indeed capable of capturing context, yet they do so in a sequential manner. This approach makes it challenging to capture long-range dependencies, especially when the important context is very far behind the current timestep. In contrast, Transformer can freely attend any parts of the sequence that it considers important without being constrained by sequential processing.

---

[referencia=65fa01dbc0699c35 score=0.001]
Talking more specifically about the flow, you can see here that the tensor dimensions throughout the entire Encoder and Decoder blocks are consistent. This kind of property allows us to scale the model easily. So, for example, if we want to increase the model complexity to improve its ability in understanding larger dataset, we can simply stack more Encoders and Decoders. Or, if you want the model to be more efficient, you can just decrease the number of these blocks. - In fact, not only the number of Encoders and Decoders, but you can basically change the value of all parameters defined in Codeblock 2 according to your needs.

The following code is an optional step, but in case you're wondering what the overall structure of the Transformer architecture looks like, you can just run it.

## Ending

And that's all for today's tutorial about Transformer and its PyTorch implementation. I would like to congratulate those who followed through all the discussions above, as you've spent more than 40 minutes to read this article! By the way, feel free to comment if you spot any mistake in my explanation or the code.

I hope you find this article useful. Thanks for reading, and see ya in the next one!

_P.S. Here's the link to the GitHub repository._

## References

[1] Ashish Vaswani et al. Attention Is All You Need. Arxiv. https://arxiv.org/pdf/1706.03762 [Accessed September 29, 2024].

[2] Image created originally by author.

[3] Sheng Shen et al. PowerNorm: Rethinking Batch Normalization in Transformers. Arxiv. https://arxiv.org/abs/2003.07845 [Accessed October 3, 2024].

---

[referencia=65fa01dbc0699c35 score=0.000]
As always, to check whether our Scaled Dot-Product Attention mechanism and the masking process are working properly, we can run the following codeblock.

In the Codeblock 9 output above, we can see that the multiplication between `q` (200×64) and transposed `k` (64×200) results in a tensor of size 200×200 (`#(1)`). The scaling operation, mask application, and the processing with softmax function do not alter this dimension. The tensor eventually changes back to the original `q`, `k`, and `v` size (200×64) after we perform matrix multiplication between `attn_output_weights` (200×200) and `v` (200×64), with the result now stored in `attn_output` variable (`#(2)`).

---

[referencia=65fa01dbc0699c35 score=0.000]
All processes done in the forward pass encapsulates the equation shown in Figure 5. The `pos` variable I create at line `#(1)` corresponds to the same thing in the equation, in which it is essentially just a sequence of numbers from 0 to `SEQ_LENGTH` (200). I want these numbers to span along the `SEQ_LENGTH` axis in the embedding tensor, so I add a new axis using the `reshape()` method. Next, at line `#(2)` I initialize the `i` array with values ranging from 0 to `D_MODEL` (512) with the step of 2. Hence, there will only be 256 numbers generated. The reason that I do this is because in the subsequent step I want to use the `i` array twice: one for the even embedding dimension and another one for the odd embedding dimension. However, the `i` array itself is not going to be used for the two directly, rather, we will employ it to compute the entire denominator in the equation (`#(3)`) before eventually being used for creating the sine (`#(4)`) and cosine waves (`#(5)`). At this point we have already had two positional embedding tensors: `even_pos_embed` and `odd_pos_embed`. What we are going to do next is to combine them such that the resulting tensor will have alternating sine and cosine pattern as shown back in Figure 6. This can be achieved using a little trick that I do at line `#(6)` and `#(7)`.

Next, we will run the following code to test if our `PositionalEncoding()` class works properly.

Here I print out every single step in the `forward()` function so that you can see what is actually going on under the hood. The main idea of this process is that, once you get the `even_pos_embed` (`#(1)`) and `odd_pos_embed` (`#(2)`) tensors, what you need to do afterwards is to merge them such that the resulting dimension becomes 200×512 as shown at line `#(3)` in the Codeblock 7 output. This dimension exactly matches with the size of the embedding tensor we discussed in the previous section (`SEQ_LENGTH`×`D_MODEL`), allowing element-wise addition to be performed.

---

[referencia=65fa01dbc0699c35 score=0.000]
# Paper Walkthrough: Attention Is All You Need

The complete guide to implementing a Transformer from scratch

---

[referencia=65fa01dbc0699c35 score=0.000]
## The Entire Transformer Architecture

At this point we have successfully created all components for the Transformer architecture, so they are now ready to be assembled. We will start by assembling the Encoder, followed by the Decoder, and finally, I will connect the two as well as the other remaining components.

---

[referencia=65fa01dbc0699c35 score=0.000]
### Transformer Components

The main Transformer architecture can be seen in the Figure 1 below. It might look a bit intimidating at first, but don't worry - I am going to explain the entire implementation as complete as possible.

You can see in the figure that Transformer comprises of many components. The large block on the left is called ***Encoder***, while the one on the right is called ***Decoder***. In the case of machine translation, for example, the Encoder is responsible for capturing the pattern of the original sentence, whereas the Decoder is employed to generate the corresponding translation.

The ability of the Transformer to freely attend to specific words is due to the presence of the ***Multihead Attention*** block, in which it works by comparing each word with every other word within the sequence. It is important to note that the three Multihead Attention blocks (highlighted in orange) are not exactly the same despite their similar purpose. Nevertheless, while the attention mechanism captures the relationships between words, it does not account for the sequence of the words itself, which is actually very crucial in NLP. Thus, to retain sequence information, we employ the so-called ***Positional Encoding***.

I think the remaining components of the network are pretty straighforward: ***Add & Norm*** block (colored in yellow) is basically an addition followed by normalization operation, ***Feed Forward*** (blue) is just a linear layer, ***Input & Output Embedding*** (red) are used to convert input words into vectors, ***Linear*** block after the Decoder (purple) is another standard linear layer, and ***Softmax*** (green) is the layer responsible for generating a probability distribution over the vocabulary to predict the next word.

---

[referencia=65fa01dbc0699c35 score=0.000]
You can see in the output that the sequence which initially has the length of 200 now becomes 200×512. This indicates that our `InputEmbedding()` class successfully converted a sequence of 200 tokens into a sequence of 200 vectors with 512 dimensions each.

We can also test our `OutputEmbedding()` class in the exact same way as shown in Codeblock 5.

In addition to the Output Embedding layer, you can see back in Figure 1 that it accepts the ***shifted right outputs*** as its input. This basically means that the current token in the original sentence corresponds to the next token in the translated sentence (i.e., the token at the subsequent timestep). This shifting is necessary to be done because the first position in the translated sentence is reserved for the so-called *start token*, which signals to the network that it is the beginning of the sentence to generate. However - as I have mentioned earlier, we are not going to get deeper into such a preprocessing step. Here we assume that the `x_dst` tensor passed through the `output_embedding` layer in the Codeblock 5 above already includes the *start token*. See the Figure 3 below to better understand this idea. In this example, the sequence on the left is a sentence in English, and the sequence on the right is the corresponding shifted-right output in Indonesian.

---

[referencia=65fa01dbc0699c35 score=0.000]
## Imports and Configurations

Now let's actually start coding by importing the required modules: the base `torch` module for basic functionalities, the `nn` submodule for initializing neural network layers, and the `summary()` function from `torchinfo` which I will use to display the details of the entire deep learning model.

Afterwards, I am going to initialize the parameters for the Transformer model. The first parameter is `SEQ_LENGTH` which the value is set to 200 (marked with `#(1)` in Codeblock 2 below). This is essentially done because we want the model to capture a sequence of exactly 200 tokens. If the sequence is longer, it will be truncated. Meanwhile, if it has fewer than 200 tokens, padding will be applied. By the way the term *token* itself does not necessarily correspond to a single word, as each word can actually be broken down into several tokens. However, we will not talk about these kinds of preprocessing details here, as the main goal of this article is to implement the architectural design. In this particular case we assume that the sequence has already been preprocessed and is ready to be fed into the network. The subsequent parameters are `VOCAB_SIZE_SRC` (`#(2)`) and `VOCAB_SIZE_DST` (`#(3)`), in which the former denotes the number of unique tokens possible to appear in the original sequence, while the latter is the same thing but for the translated sequence. It is worth noting that the numbers for these parameters are chosen arbitrarily. In practice, sequence lengths can range from a few hundred to several thousand tokens, while the vocabulary size typically range from tens of thousands to a few hundred thousand tokens.

---

[referencia=65fa01dbc0699c35 score=0.000]
### Combining Encoder and Decoder

As we have successfully created the `Encoder()` and `Decoder()` class, we can now get into the very last part of this writing: connecting the Encoder to the Decoder along with the other components that interact with them. Here I provide you a figure showing the entire Transformer architecture for reference, so you don't need to scroll all the way to Figure 1 just to verify our implementation in Codeblock 24 and 25.

In the codeblock below, I implement the architecture inside the `Transformer()` class. In the `__init__()` method, we initialize the input and output embedding layers (`#(1)` and `#(2)`). These two layers are responsible for converting tokens into their corresponding 512-dimensional vector representations. Next, we initialize a single `positional_encoding` layer which will be used twice: one for the embedded input tokens, and another one for the embedded output tokens. Meanwhile, the initialization of the Encoder (`#(4)`) and the Decoder (`#(5)`) blocks is a little bit different, where in this case we utilize `nn.ModuleList()`. We can think of this like a list of modules which we will connect sequentially later in the forward pass, and in this case each is repeated `N` (6) times. In fact, this is essentially why I name them `self.encoders` and `self.decoders` (with *s*). The last thing we need to do in the `__init__()` method is to initialize the `self.linear` layer (`#(6)`), in which it will be responsible to map the 512-dimensional token embeddings to all possible tokens in the destination language. We can perceive this like a classification task, where the model will choose one token at a time as the prediction result based on their probability scores.