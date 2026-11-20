[referencia=143feaeaaeb2d7cd score=0.966]
# **Transformer Feed-Forward Layers Are Key-Value Memories** 

**Mor Geva**<sup>1</sup><sup>_,_2</sup> **Roei Schuster**<sup>1</sup><sup>_,_3</sup> **Jonathan Berant**<sup>1</sup><sup>_,_2</sup> **Omer Levy**<sup>1</sup> 

1Blavatnik School of Computer Science, Tel-Aviv University 2Allen Institute for Artificial Intelligence 3Cornell Tech 

{morgeva@mail,joberant@cs,levyomer@cs}.tau.ac.il, rs864@cornell.edu 

## **Abstract** 

Feed-forward layers constitute two-thirds of a transformer model’s parameters, yet their role in the network remains under-explored. We show that feed-forward layers in transformerbased language models operate as key-value memories, where each key correlates with textual patterns in the training examples, and each value induces a distribution over the output vocabulary. Our experiments show that the learned patterns are human-interpretable, and that lower layers tend to capture shallow patterns, while upper layers learn more semantic ones. The values complement the keys’ input patterns by inducing output distributions that concentrate probability mass on tokens likely to appear immediately after each pattern, particularly in the upper layers. Finally, we demonstrate that the output of a feed-forward layer is a composition of its memories, which is subsequently refined throughout the model’s layers via residual connections to produce the final output distribution.

---

[referencia=143feaeaaeb2d7cd score=0.954]
## **7 Discussion and Conclusion** 

Understanding how and why transformers work is crucial to many aspects of modern NLP, including model interpretability, data security, and development of better models. Feed-forward layers account for most of a transformer’s parameters, yet little is known about their function in the network. 

In this work, we propose that feed-forward layers emulate key-value memories, and provide a set of experiments showing that: (a) keys are correlated with human-interpretable input patterns; (b) values, mostly in the model’s upper layers, induce distributions over the output vocabulary that correlate with the next-token distribution of patterns in the corresponding key; and (c) the model’s output is formed via an aggregation of these distributions, whereby they are first composed to form individual layer outputs, which are then refined throughout the model’s layers using residual connections. 

Our findings open important research directions: 

- **Layer embedding space.** We observe a correlation between value distributions over the output 

vocabulary and key patterns, that increases from lower to upper layers (Section 4). Is this because the layer’s output space transforms across layers? If so, how? We note that this possible transformation cannot be explained solely by the function of feed-forward layers: if the model only did a series of key-value look-ups and value-distribution aggregation via weighted addition, then a single, unifying embedding space would appear more natural. Thus, the transformation might have to do with the interplay between feed-forward layers and self-attention layers. 

- **Beyond language modeling.** Our formulation of feed-forward networks as key-value memories generalizes to any transformer model, e.g. BERT encoders and neural translation models. We thus expect our qualitative empirical observations to hold across diverse settings, and leave verification of this for future work. 

- **Practical implications.** A better understanding of feed-forward layers has many implications in NLP. For example, future studies may offer interpretability methods by automating the patternidentification process; memory cells might affect training-data privacy as they could facilitate white-box membership inference (Nasr et al., 2019); and studying cases where a correct pattern is identified but then suppressed during aggregation may guide architectural novelties. 

Thus, by illuminating the role of feed-forward layers, we move towards a better understanding of the inner workings of transformers, and open new research threads on modern NLP models.

---

[referencia=143feaeaaeb2d7cd score=0.942]
**Discussion.** When viewed as distributions over the output vocabulary, values in the upper layers tend to assign higher probability to the next- 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>top prediction probability<br>8.9e-51.3e-41.8e-42.2e-42.7e-43.1e-43.6e-44.e-4<br>agreement rate<br><!-- End of picture text -->

Figure 6: Agreement rate (between the top-ranked token based on the value vector **v** _i_<sup>_ℓ_andthenexttoken</sup> of the top-ranked trigger example associated with the key vector **k**<sup>_ℓ_</sup> _i_<sup>) as a function of the maximal probability</sup> assigned by the value vector. 

token of examples triggering the corresponding keys. This suggests that memory cells often store information on how to directly predict the output (the distribution of the next word) from the input (patterns in the prefix). Conversely, the lower layers do not exhibit such clear correlation between the keys’ patterns and the corresponding values’ distributions. A possible explanation is that the lower layers do not operate in the same embedding space, and therefore, projecting values onto the vocabulary using the output embeddings does not produce distributions that follow the trigger examples. However, our results imply that some intermediate layers _do_ operate in the same or similar space to upper layers (exhibiting some agreement), which in itself is non-trivial. We leave further exploration of this phenomenon to future work.

---

[referencia=143feaeaaeb2d7cd score=0.934]
parameter matrix in the layer corresponds to _keys_ , and the second parameter matrix to _values_ . Figure 1 shows how the keys (first parameter matrix) interact with the input to produce coefficients, which are then used to compute a weighted sum of the values (second parameter matrix) as the output. While the theoretical similarity between feed-forward layers and key-value memories has previously been suggested by Sukhbaatar et al. (2019), we take this observation one step further, and analyze the “memories” that the feed-forward layers store. 

We find that each key correlates with a specific set of human-interpretable input patterns, such as _n_ -grams or semantic topics. For example, _k_ 2 in Figure 1 is triggered by inputs that describe a pe- 

riod of time and end with _“a”_ . Simultaneously, we observe that each _value_ can induce a distribution over the output vocabulary, and that this distribution correlates with the next-token distribution of the corresponding keys in the upper layers of the model. In the above example, the corresponding value _v_ 2 represents a distribution that puts most of its probability mass on the word _“while”_ . 

Lastly, we analyze how the language model, as a whole, composes its final prediction from individual memories. We observe that each layer combines hundreds of active memories, creating a distribution that is qualitatively different from each of its component memories’ values. Meanwhile, the residual connection between layers acts as a refinement mechanism, gently tuning the prediction at each layer while retaining most of the residual’s information. 

In conclusion, our work sheds light on the function of feed-forward layers in transformer-based language models. We show that feed-forward layers act as pattern detectors over the input across all layers, and that the final output distribution is gradually constructed in a bottom-up fashion.<sup>1</sup>

---

[referencia=143feaeaaeb2d7cd score=0.929]
### **Feed-forward layers emulate neural memory** 

Comparing equations 1 and 2 shows that feedforward layers are almost identical to key-value neural memories; the only difference is that neural memory uses softmax as the non-linearity _f_ ( _·_ ), while the canonical transformer does not use a normalizing function in the feed-forward layer. The _hidden dimension dm_ is essentially the number of memories in the layer, and the activation **m** = _f_ ( **x** _· K_<sup>_⊤_</sup> ), commonly referred to as the _hidden layer_ , is a vector containing an unnormalized non-negative coefficient for each memory. We refer to each **m** _i_ as the _memory coefficient_ of the _i_ th memory cell. 

Sukhbaatar et al. (2019) make an analogous observation, and incorporate the parameters of the feed-forward layers as persistent memory cells in the self-attention layers. While this reparameterization works in practice, the experiment does not tell us much about the role of feed-forward layers in the canonical transformer. If transformer feed-forward layers are indeed key-value memories, then what memories do they store? 

We conjecture that each key vector **k** _i_ captures a particular pattern (or set of patterns) in the input sequence (Section 3), and that its corresponding value vector **v** _i_ represents the distribution of tokens that follows said pattern (Section 4).

---

[referencia=143feaeaaeb2d7cd score=0.842]
**h** , and compute the number of examples where the following condition holds: 



Figure 8 shows that, for any layer in the network, the layer’s final prediction is different than _every one_ of the memories’ predictions in at least _∼_ 68% of the examples. Even in the upper layers, where the memories’ values are more correlated with the output space (Section 4), the layer-level prediction is typically not the result of a single dominant memory cell, but a composition of multiple memories. 

We further analyze cases where at least one memory cell agrees with the layer’s prediction, and find that (a) in 60% of the examples the target token is a common stop word in the vocabulary (e.g. _“the”_ or _“of”_ ), and (b) in 43% of the cases the input prefix has less than 5 tokens. This suggests that very common patterns in the training data might 



<!-- Start of picture text -->
100<br>80<br>60<br>40<br>20<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>% examples with zero agreement<br><!-- End of picture text -->

Figure 8: The fraction of examples in a random sample of 4,000 examples where the layer’s prediction is different from the prediction of all of its memories. 

be “cached” in individual memory cells, and do not require compositionality.

---

[referencia=143feaeaaeb2d7cd score=0.818]
## **1 Introduction** 

Transformer-based language models (Vaswani et al., 2017) are at the core of state-of-the-art natural language processing (Devlin et al., 2019; Brown et al., 2020), largely due to the success of selfattention. While much literature has been devoted to analyzing the function of self-attention layers (Voita et al., 2019; Clark et al., 2019; Vig and Belinkov, 2019), they account for only a third of a typical transformer’s parameters (4 _d_<sup>2</sup> per layer, where _d_ is the model’s hidden dimension). Most of the parameter budget is spent on position-wise feedforward layers (8 _d_<sup>2</sup> per layer), yet their role remains under-explored. What, if so, is the function of feed-forward layers in a transformer language model? 

We show that feed-forward layers emulate neural memories (Sukhbaatar et al., 2015), where the first 



<!-- Start of picture text -->
Transformer layers<br>x’ x’ x’ x’ x’<br>1 2 3 4 5<br>FF<br>layer<br>while<br>.2 v 1 1.5 v 2 ... it will take a 0 v dm<br>... every once in a<br>... , and for a<br>k 1 k 2 k dm<br>x x x x x<br>1 2 3 4 5<br>self-attention layer<br>Transformer layers<br>Stay with you for a<br><!-- End of picture text -->

Figure 1: An illustration of how a feed-forward layer emulates a key-value memory. Input vectors (here, **x** 5) are multiplied by _keys_ to produce _memory coefficients_ (e.g., the memory coefficient for **v** 1 is 0 _._ 2), which then weigh distributions over the output vocabulary, stored in the _values_ . The feed-forward layer’s output is thus the weighted sum of its values.

---

[referencia=143feaeaaeb2d7cd score=0.627]
## **2 Feed-Forward Layers as Unnormalized Key-Value Memories** 

**Feed-forward layers** A transformer language model (Vaswani et al., 2017) is made of intertwined self-attention and feed-forward layers. Each feedforward layer is a position-wise function, processing each input vector independently. Let **x** _∈_ R<sup>_d_</sup> be a vector corresponding to some input text prefix. We can express the feed-forward layer FF( _·_ ) as follows (bias terms are omitted): 



Here, _K, V ∈_ R<sup>_dm×d_</sup> are parameter matrices, and _f_ is a non-linearity such as ReLU. 

**Neural memory** A neural memory (Sukhbaatar et al., 2015) consists of _dm_ key-value pairs, which we call _memories_ .<sup>2</sup> Each key is represented by a _d_ -dimensional vector **k** _i ∈_ R<sup>_d_</sup> , and together form the parameter matrix _K ∈_ R<sup>_dm×d_</sup> ; likewise, we define the value parameters as _V ∈_ R<sup>_dm×d_</sup> . Given an input vector **x** _∈_ R<sup>_d_</sup> , we compute a distribution 

> 1The code for reproducing our experiments is available at https://github.com/mega002/ff-layers/. 

> 2We use the terms “memory cells” and “memories” interchangeably. 

over the keys, and use it to compute the expected value: 



With matrix notation, we arrive at a more compact formulation:

---

[referencia=143feaeaaeb2d7cd score=0.599]
### **5.2 Inter-Layer Prediction Refinement** 

While a single feed-forward layer composes its memories in parallel, a multi-layer model uses the residual connection **r** to _sequentially_ compose predictions to produce the model’s final output:<sup>5</sup> 



We hypothesize that the model uses the sequential composition apparatus as a means to _refine_ its prediction from layer to layer, often deciding what the prediction will be at one of the lower layers. 

To test our hypothesis, we first measure how often the probability distribution induced by the residual vector **r**<sup>_ℓ_</sup> matches the model’s final output **o**<sup>_L_</sup> ( _L_ being the total number of layers): 



Figure 9 shows that roughly a third of the model’s predictions are determined in the bottom few layers. This number grows rapidly from layer 10 onwards, implying that the majority of “hard” decisions occur before the final layer. 

We also measure the probability mass _p_ that each layer’s residual vector **r**<sup>_ℓ_</sup> assigns to the model’s 

> 5The residual propagates information from previous layers, including the transformer’s self-attention layers. 



<!-- Start of picture text -->
100<br>80<br>60<br>40<br>20<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br> predicts the final output<br>% examples s.t. the residual<br><!-- End of picture text -->

Figure 9: Fraction of examples in each layer, where the residual’s top prediction matches the model’s output. 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>probability<br><!-- End of picture text -->

Figure 10: Probability of the token output by the model according to the residual of each layer. 

final prediction: 



Figure 10 shows a similar trend, but emphasizes that it is not only the top prediction’s identity that is refined as we progress through the layers, it is

---

[referencia=143feaeaaeb2d7cd score=0.598]
agreement rate is close to zero in the lower layers (1-10), but starting from layer 11, the agreement rate quickly rises until 3.5%, showing higher agreement between keys and values on the identity of the top-ranked token. Importantly, this value is orders of magnitude higher than a random token prediction from the vocabulary, which would produce a far lower agreement rate (0 _._ 0004%), showing that upper-layer memories manifest non-trivial predictive power. 

Next, we take the next token of **k**<sup>_ℓ_</sup> _i_<sup>’s top-1 trig-</sup> ger example ( _wi_<sup>_ℓ_),andfindwhereitranksinthe</sup> value vector’s distribution **p**<sup>_ℓ_</sup> _i_<sup>.Figure 5 shows that</sup> the rank of the next token of a trigger example increases through the layers, meaning that _wi_<sup>_ℓ_tends</sup> to get higher probability in the upper layers. 

**Detecting predictive values.** To examine if we can automatically detect values with high agreement rate, we analyze the probability of the values’ top prediction, i.e., (max( **p**<sup>_ℓ_</sup> _i_<sup>)).Figure6shows</sup> that although these distributions are not calibrated, distributions with higher maximum probabilities are more likely to agree with their key’s top trigger example. We then take the 100 values with highest probability across all layers and dimensions (97 out of the 100 are in the upper layers, 11-16), and for each value **v** _i_<sup>_ℓ_,analyze the top-50 trigger ex-</sup> amples of **k**<sup>_ℓ_</sup> _i_<sup>.Wefindthatinalmosthalfofthe</sup> values (46 out of 100), there is at least one trigger example that agrees with the value’s top prediction. Examples are provided in Table 2. 

**Discussion.** When viewed as distributions over the output vocabulary, values in the upper layers tend to assign higher probability to the next- 



<!-- Start of picture text -->

---

[referencia=143feaeaaeb2d7cd score=0.583]
final prediction: 



Figure 10 shows a similar trend, but emphasizes that it is not only the top prediction’s identity that is refined as we progress through the layers, it is 

To better understand how the refinement process works at each layer, we measure how often the residual’s top prediction changes following its interaction with the feed-forward layer (top( **r**<sup>_ℓ_</sup> ) = top( **o**<sup>_ℓ_</sup> )), and whether this change results from the feed-forward layer overriding the residual (top( **o**<sup>_ℓ_</sup> ) = top( **y**<sup>_ℓ_</sup> )) or from a true composition (top( **r**<sup>_ℓ_</sup> ) = top( **o**<sup>_ℓ_</sup> ) = top( **y**<sup>_ℓ_</sup> )). 

Figure 11 shows the breakdown of different cases per layer. In the vast majority of examples, the residual’s top prediction ends up being the 



<!-- Start of picture text -->
100<br>80<br>60<br>40<br>residual<br>agreement<br>20 composition<br>ffn<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>% examples<br><!-- End of picture text -->

Figure 11: Breakdown of examples by prediction cases: the layer’s output prediction matches the residual’s prediction ( _residual_ ), matches the feed-forward layer’s prediction ( _ffn_ ), matches both of the predictions ( _agreement_ ), or none of the predictions ( _composition_ ). By construction, there are no cases where the residual’s prediction matches the feed-forward layer’s prediction and does not match the output’s prediction.

---

[referencia=143feaeaaeb2d7cd score=0.498]
## **4 Values Represent Distributions** 

After establishing that keys capture patterns in training examples, we turn to analyze the information 



<!-- Start of picture text -->
3.5<br>3.0<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0.0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>agreement rate (%)<br><!-- End of picture text -->

Figure 4: Agreement rate between the top-ranked token based on the value vector **v** _i_<sup>_ℓ_, and the next token of</sup> the top-ranked trigger example associated with the key vector **k**<sup>_ℓ_</sup> _i_<sup>.</sup> 

stored in their corresponding values. We show that each value **v** _i_<sup>_ℓ_can be viewed as a distribution over</sup> the output vocabulary, and demonstrate that this distribution complements the patterns in the corresponding key **k**<sup>_ℓ_</sup> _i_<sup>in the model’s upper layers (see</sup> Figure 1). 

**Casting values as distributions over the vocabulary.** We begin by converting each value vector **v** _i_<sup>_ℓ_intoaprobabilitydistributionoverthevocab-</sup> ulary by multiplying it by the output embedding matrix _E_ and applying a softmax:<sup>4</sup> 



The probability distribution **p**<sup>_ℓ_</sup> _i_<sup>isuncalibrated,</sup> since the value vector **v** _i_<sup>_ℓ_istypicallymultiplied</sup> by the input-dependent memory coefficient **m**<sup>_ℓ_</sup> _i_<sup>,</sup> changing the skewness of the output distribution. That said, the _ranking_ induced by **p**<sup>_ℓ_</sup> _i_<sup>is invariant to</sup> the coefficient, and can still be examined. This conversion assumes (naïvely) that all model’s layers operate in the same embedding space.

---

[referencia=143feaeaaeb2d7cd score=0.372]
model’s prediction ( _residual+agreement_ ). In most of these cases, the feed forward layer predicts something different ( _residual_ ). Perhaps surprisingly, when the residual’s prediction does change ( _composition+ffn_ ), it rarely changes to the feed-forward layer’s prediction ( _ffn_ ). Instead, we observe that composing the residual’s distribution with that of the feed-forward layer produces a “compromise” prediction, which is equal to neither ( _composition_ ). This behavior is similar to the intra-layer composition we observe in Section 5.1. A possible conjecture is that the feed-forward layer acts as an elimination mechanism to “veto” the top prediction in the residual, and thus shifts probability mass towards one of the other candidate predictions in the head of the residual’s distribution. 

Finally, we manually analyze 100 random cases of last-layer composition, where the feed-forward layer modifies the residual output in the _final_ layer. We find that in most cases (66 examples), the output changes to a semantically distant word (e.g., _“people” → “same”_ ) and in the rest of the cases (34 examples), the feed-forward layer’s output shifts the residual prediction to a related word (e.g. _“later” → “earlier”_ and _“gastric” → “stomach”_ ). This suggests that feed-forward layers tune the residual predictions at varying granularity, even in the last layer of the model.

---

[referencia=143feaeaaeb2d7cd score=0.295]
## **5 Aggregating Memories** 

So far, our discussion has been about the function of a single memory cell in feed-forward layers. How does the information from _multiple_ cells in multiple _layers_ aggregate to form a model-wide prediction? We show that every feed-forward layer combines multiple memories to produce a distribution that is qualitatively different from each of its component memories’ value distributions (Section 5.1). These layer-wise distributions are then combined via residual connections in a refinement process, where each feed-forward layer updates the residual’s distribution to finally form the model’s output (Section 5.2). 

|Value|Prediction|Precision@50|Trigger example|
|---|---|---|---|
|**v**<sup>15</sup><br>222|_each_|68%|_But when bees and wasps resemble each_|
|**v**<sup>16</sup><br>752|_played_|16%|_Her frst role was in Vijay Lalwani’s psychological thriller Karthik Calling_<br>_Karthik, where Padukone was cast as the supportive girlfriend of a depressed_<br>_man (played_|
|**v**<sup>13</sup><br>2601|_extratropical_|4%|_Most of the winter precipitation is the result of synoptic scale, low pressure_<br>_weather systems (large scale storms such as extratropical_|
|**v**<sup>15</sup><br>881|_part_|92%|_Comet served only briefy with the feet, owing in large part_|
|**v**<sup>16</sup><br>2070|_line_|84%|_Sailing from Lorient in October 1805 with one ship of the line_|
|**v**<sup>12</sup><br>3186|_jail_|4%|_On May 11, 2011, four days after scoring 6 touchdowns for the Slaughter, Grady_<br>_was sentenced to twenty days in jail_|



Table 2: Example values, their top prediction, the fraction of their key’s top-50 trigger examples that agree with their prediction, and a matching trigger example (with the target token marked in blue).

---

[referencia=143feaeaaeb2d7cd score=0.244]
To further test this hypothesis, we sample 1600 random keys (100 keys per layer) and apply local modifications to the top-50 trigger examples of every key. Specifically, we remove either the _first_ , _last_ , or a _random_ token from the input, and measure how this mutation affects the memory coefficient. Figure 3 shows that the model considers the end of an example as more salient than the beginning for predicting the next token. In upper layers, removing the last token has less impact, supporting our conclusion that upper-layer keys are less correlated with shallow patterns.

---

[referencia=143feaeaaeb2d7cd score=0.217]
### **5.1 Intra-Layer Memory Composition** 

The feed-forward layer’s output can be defined as the sum of value vectors weighted by their memory coefficients, plus a bias term: 



If each value vector **v** _i_<sup>_ℓ_contains information about</sup> the target token’s distribution, how is this information aggregated into a single output distribution? To find out, we analyze the behavior of 4,000 randomly-sampled prefixes from the validation set. Here, the validation set is used (rather than the training set used to find trigger examples) since we are trying to characterize the model’s behavior at inference time, not find the examples it “memorizes” during training. 

We first measure the fraction of “active” memories (cells with a non-zero coefficient). Figure 7 shows that a typical example triggers hundreds of memories per layer (10%-50% of 4096 dimensions), but the majority of cells remain inactive. Interestingly, the number of active memories drops towards layer 10, which is the same layer in which semantic patterns become more prevalent than shallow patterns, according to expert annotations (see Section 3, Figure 2). 

While there are cases where a single memory cell dominates the output of a layer, the majority of outputs are clearly compositional. We count the number of instances where the feed-forward layer’s top prediction is _different_ from all of the memories’ top predictions. Formally, we denote: 



as a generic shorthand for the top prediction from the vocabulary distribution induced by the vector 



<!-- Start of picture text -->
100<br>80<br>60<br>40<br>20<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>% of active memories<br><!-- End of picture text -->

Figure 7: The fraction of active memories (i.e., with positive memory coefficient) out of 4096 memories in every layer, for a random sample of 4,000 examples. 

**h** , and compute the number of examples where the following condition holds:

---

[referencia=143feaeaaeb2d7cd score=0.154]
## **6 Related Work** 

Considerable attention has been given to demystifying the operation of neural NLP models. An 

extensive line of work targeted neuron functionality in general, extracting the properties that neurons and subsets of neurons capture (Durrani et al., 2020; Dalvi et al., 2019; Rethmeier et al., 2020; Mu and Andreas, 2020; Vig et al., 2020), regardless of the model architecture or neurons’ position in it. Jacovi et al. (2018) analyzed CNN architectures in text classification and showed that they extract key n-grams from the inputs. 

The study of the transformer architecture has focused on the role and function of self-attention layers (Voita et al., 2019; Clark et al., 2019; Vig and Belinkov, 2019) and on inter-layer differences (i.e. lower vs. upper layers) (Tenney et al., 2019; Jawahar et al., 2019). Previous work also highlighted the importance of feed-forward layers in transformers (Press et al., 2020; Pulugundla et al., 2021; Xu et al., 2020). Still, to date, the role of feed-forward layers remains under-explored. 

Also related are interpretability methods that explain predictions (Han et al., 2020; Wiegreffe and Pinter, 2019), however, our focus is entirely different: we do not interpret individual predictions, but aim to understand the mechanism of transformers. 

Characterizing the functionality of memory cells based on examples that trigger maximal activations has been used previously in NLP (Rethmeier et al., 2020) and vision (Erhan et al., 2009).

---

[referencia=143feaeaaeb2d7cd score=0.154]
### **Value predictions follow key patterns in upper** 

**layers.** For every layer _ℓ_ and memory dimension _i_ , we compare the top-ranked token according to **v** _i_<sup>_ℓ_, (argmax(</sup><sup>**p**</sup><sup>_ℓ_</sup> _i_<sup>)) to the next token</sup><sup>_w_</sup> _i_<sup>_ℓ_in the top-</sup> 1 trigger example according to **k**<sup>_ℓ_</sup> _i_<sup>(theexample</sup> whose memory coefficient for **k**<sup>_ℓ_</sup> _i_<sup>isthehighest).</sup> Figure 4 shows the _agreement rate_ , i.e. the fraction of memory cells (dimensions) where the value’s top prediction matches the key’s top trigger example (argmax( **p**<sup>_ℓ_</sup> _i_<sup>)=</sup><sup>_w_</sup> _i_<sup>_ℓ_).Itcanbeseenthatthe</sup> 

4This is a simplification; in practice, we use the adaptive softmax (Baevski and Auli, 2019) to compute probabilities. 



<!-- Start of picture text -->
30000<br>25000<br>20000<br>15000<br>10000<br>5000<br>0<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>layer<br>rank distribution<br><!-- End of picture text -->

Figure 5: Distribution of the rank of the next-token in the top-1 trigger example of **k**<sup>_ℓ_</sup> _i_<sup>(</sup><sup>_w_</sup> _i_<sup>_ℓ_),accordingtothe</sup> ranking induced by the value vector **v** _i_<sup>_ℓ_.We cut the tail</sup> of the distribution, which stretches up to the vocabulary _∼_ size ( 270K tokens).

---

[referencia=143feaeaaeb2d7cd score=0.045]
### **3.1 Experiment** 

We conduct our experiment over the language model of Baevski and Auli (2019), a 16-layer transformer language model trained on WikiText103 (Merity et al., 2017). This model defines _d_ = 1024 and _dm_ = 4096, and has a total of _dm ·_ 16 = 65 _,_ 536 potential keys to analyze. We randomly sample 10 keys per layer (160 in total). 

Figure 2: Breakdown of the labels experts assigned to trigger examples in each layer. Some examples were not associated with any pattern (“not-covered”). 

**Retrieving trigger examples** We assume that patterns stored in memory cells originate from examples the model was trained on. Therefore, given a key **k**<sup>_ℓ_</sup> _i_<sup>that corresponds to the</sup><sup>_i_-th hidden dimen-</sup> sion of the _ℓ_ -th feed-forward layer, we compute the memory coefficient ReLU( **x**<sup>_ℓ_</sup> _j_<sup>_·_</sup><sup>**k**</sup><sup>_ℓ_</sup> _i_<sup>) for every prefix</sup> _x_ 1 _, . . . , xj_ of every sentence from the WikiText103’s training set.<sup>3</sup> For example, for the hypothetical sentence _“I love dogs”_ , we will compute three coefficients, for the prefixes _“I”_ , _“I love”_ , and _“I love dogs”_ . Then, we retrieve the _top-t trigger examples_ , that is, the _t_ prefixes whose representation at layer _ℓ_ yielded the highest inner product with **k**<sup>_ℓ_</sup> _i_<sup>.</sup>

---

[referencia=143feaeaaeb2d7cd score=0.017]
- Ofir Press, Noah A. Smith, and Omer Levy. 2020. Improving transformer models by reordering their sublayers. In _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics_ , pages 2996–3005, Online. Association for Computational Linguistics.