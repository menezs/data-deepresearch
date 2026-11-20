[referencia=25676193afe5f7ab score=0.992]
### ofirp@cs.washington.edu 

ABSTRACT Since the introduction of the transformer model by Vaswani et al. (2017), a fundamental question has yet to be answered: how does a model achieve extrapolation 

at inference time for sequences that are longer than it saw during training? We first show that extrapolation can be enabled by simply changing the position representation method, though we find that current methods do not allow for _efficient_ ex- 

trapolation. We therefore introduce a simpler and more efficient position method, Attention with Linear Biases (ALiBi). ALiBi does not add positional embeddings to word embeddings; instead, it biases query-key attention scores with a penalty that is proportional to their distance. We show that this method trains a 1.3 bil- 

lion parameter model on input sequences of length 1024 that extrapolates to input 

sequences of length 2048, achieving the same perplexity as a sinusoidal position embedding model trained on inputs of length 2048 but training 11% faster and using 11% less memory. ALiBi’s inductive bias towards recency also leads it to outperform multiple strong position methods on the WikiText-103 benchmark.<sup>1</sup> 

1 INTRODUCTION 

When constructing a transformer-based language model, a major design decision is the length of training sequences, denoted _L_ herein, which has to date been equivalent to the length of inference sequences. More context, achieved by larger _L_ , improves predictions at inference time. But longer sequences are more expensive to train on.<sup>2</sup> 

Before transformers, RNN language models were trained on shorter- _L_ sequences and assumed to generalize to longer contexts at inference time (Mikolov et al., 2010; Mikolov & Zweig, 2012; Zaremba et al., 2014). Vaswani et al. (2017), introducing the transformer, speculated that it “may [...] extrapolate to sequence lengths longer than the ones encountered during training.” We define _extrapolation_ as a model’s ability to continue performing well as the number of input tokens during validation increases beyond the number of tokens on which the the model was trained. We find that transformer language models (LMs) that use sinusoidal position embeddings have very weak extrapolation abilities; see Figure 1.

---

[referencia=25676193afe5f7ab score=0.960]
Additionally, Table 5 (in the appendix) also shows that, for _L_ s of 1024 and 3072, our method performs better than the rotary and T5 bias models even when _Lvalid_ = _L_ (i.e., no extrapolation is occurring). Figure 1 (and the corresponding Appendix Tables 2 and 3) more broadly explore our method vs. the other position methods. They show that the T5 bias (the best of the baselines) improves perplexity until _Lvalid_ is around 2 _L_ , but on the WikiText-103 dataset our method continually improves perplexity until at least around 3 _L_ , with the _L_ = 512 model improving perplexity even when _Lvalid_ exceeds 12k tokens. Even when unable to improve perplexity given longer sequences, ALiBi always maintains strong performance as more tokens are added. 

Appendix Table 6 shows that our results on the validation set also transfer to the test set of WikiText103. Currently, almost all models that present results on WikiText-103 use sliding window evaluation (defined in §B) to compute perplexities. We apply that method to our (and to the sinusoidal, rotary and T5 bias) models in Appendix Table 7. We find that our L = 3072 model surpasses the performance of Transformer-XL (Dai et al., 2019), the Sandwich (Press et al., 2020), and Shortformer (Press et al., 2021) models. Our results are similar to the ones obtained with staged training (Press et al., 2021) but fall short of results obtained by Routing Transformer (Roy et al., 2020) and kNN-LM (Khandelwal et al., 2020). The methods used in those models are orthogonal to ours, and we hypothesize that combining them with ours might lead to even larger performance increases. 

After developing our method on WikiText-103, in Appendix Section A.3, we run one set of experiments on a different domain (books) using a similar model architecture and without modifying any of the ALiBi hyperparameters (the slopes) and show that our results fully transfer to this new domain. Our models are able to both surpass the sinusoidal baseline when not extrapolating while also outperforming it when extrapolating to longer sequences.

---

[referencia=25676193afe5f7ab score=0.949]
scores while running faster and using less memory (since it is trained on shorter inputs). 



use the learned position embedding method from Vaswani et al., and GPT-J uses the rotary method. Our results on the 1.3B parameter model show our method’s ability to generalize to larger models, dataset sizes and training durations without retuning the hyperparameter. 



Figure 4: ALiBi models trained and evaluated on varying sequence lengths on the WikiText-103 

validation set and the sinusoidal baseline (not evaluated on longer sequences). All of our models outperform the sinusoidal ones even when trained on fewer tokens. Appendix Table 5 has exact perplexities, more ALiBi models (trained on fewer tokens), and results for rotary and T5 bias models. 

We first develop our method on the WikiText-103 corpus (Merity et al., 2016), replacing the sinusoidal position embeddings in the language model of Baevski & Auli (2018) with ALiBi. 

Figure 4 (and the corresponding Appendix Table 5) show our results for models trained with varying numbers of input subsequence tokens ( _L_ ), extrapolating to longer subsequence lengths on the validation dataset. Our first observation is that, without extrapolation, for every _L_ , our models outperform those using the sinusoidal method, sometimes by a significant amount. For example, the Baevski & Auli model achieves 18.67 _±_ 0.24 (std. dev.) perplexity when trained with _L_ = 3072 input tokens, but our _L_ = 3072 model achieves 17.60 perplexity (when both models evaluate with _Lvalid_ = 3072). 

6 

Published as a conference paper at ICLR 2022

---

[referencia=25676193afe5f7ab score=0.924]
In Figure 5 (right), results become even more impressive, showing that our model trained on _L_ = 1024 outperforms by 0.09 perplexity the sinusoidal model trained on _L_ = 2048 (when evaluating with _Lvalid_ = 2048) even though our model uses 3.1 GB less memory. Our model maintains a lead in perplexity over the sinusoidal model during the entire training process. By sampling five evenly distributed points across the training process, we compute that our _L_ = 1024 model reaches a given perplexity value, on average, 11% faster than the sinusoidal model does. 

Since our models in these comparisons use much less memory, they allow for stacking more layers, which would further improve performance (with negligible, if any, runtime cost). To keep our experiments as straightforward as possible, however, we do not add layers to our models. 

Appendix Table 12 presents additional results comparing our models to the sinusoidal baseline when both are trained on the same _L_ , showing that ALiBi performs similarly to the sinusoidal baseline when not extrapolating. This contrasts with the results presented on the smaller datasets, where ALiBi consistently outperforms other position methods even when not extrapolating, suggesting that ALiBi’s inductive bias provides additional benefits for lower-resource language modeling. 



<!-- Start of picture text -->
Extrapolation, L = 512 Extrapolation, L = 1024<br>on CC100+RoBERTa on CC100+RoBERTa<br>10.2 10.2<br>Sinusoidal<br>9.8 9.8 ALiBi<br>9.4 9.4<br>9.0 Sinusoidal 9.0<br>ALiBi<br>8.6 8.6<br>512 2500 5000 7500 10000 1024 2500 5000 7500 10000<br>Validation Input Length (Lvalid) Validation Input Length (Lvalid)<br>) )<br>Perplexity ( Perplexity (<br><!-- End of picture text -->

---

[referencia=25676193afe5f7ab score=0.920]
### B.2 EXTRAPOLATION REDUCES THE EARLY TOKEN CURSE 

We presented results showing that our ALiBi method (and, to a lesser extent, the T5 bias) allows LMs to extrapolate during inference. Two reasons could explain why these methods enable LMs to achieve better perplexity given longer input subsequences: 

1. Performance improves because the models can use longer contexts to make more accurate predictions. For example, the average article length in the WikiText-103 corpus is about 3600 tokens; therefore, if a model trained on _L_ = 512 tokens extrapolates to _Lvalid_ = 3072 tokens during inference and achieves better results, that might be because it can spot patterns occurring across more than 512 tokens. 

2. Performance improves because longer input sequences mean the early token curse is reduced. For example, during nonoverlapping evaluation on sequences of length _Lvalid_ = 1000, 10% of predictions have 100 tokens of context or less. If we rerun nonoverlapping evaluation on that model with _Lvalid_ = 2000 tokens, now only 5% of predictions have 100 

> 12Nonoverlapping inference can be viewed as sliding window inference with stride _L_ . 

23 

Published as a conference paper at ICLR 2022 

tokens of context or less. So, by simply being able to handle longer sequences, a model can substantially reduce the early token curse and improve performance.<sup>13</sup> 

To better understand what might be occurring, we re-evaluate the development set of WikiText-103 with our models and the sinusoidal baseline with _L_ = 512 _,_ 1024 _,_ 3072. However, this time we use sliding window evaluation with a stride of _S_ = 1, meaning that we move the sliding window just one token after every inference pass, giving each prediction the maximum number of context tokens that the model can use. 



<!-- Start of picture text -->

---

[referencia=25676193afe5f7ab score=0.906]
> 11In our experiments, trainable slopes also slowed down the training speed by 3%. 

5 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
Implementation. ALiBi is easy to implement, with all changes accomplished in a few lines of<br>code. We implement it by modifying the mask matrix by adding the linear biases to it (in practice,<br>when training a transformer LM, query  q i  attends only to keys 1 to  i ; this is implemented by adding<br>a mask matrix to the query-key dot product before the softmax operation is applied). This means<br>that there is no runtime penalty when using our method since we add no operations to the network.<br>Compared to the sinusoidal model trained on the same input lengths, AliBi incurs a memory increase<br>(up to 100MB in some of our experiments): in the unmodified transformer, the mask is of size  L×L ;<br>when using ALiBi, the mask is a slightly larger  n×L×L  (where  n  is the number of heads) since the<br>linear biases added for each head uses a different slope. But, as we show, ALiBi enables training on<br>much smaller sequences while still achieving (and occasionally surpassing) results obtained using<br>sinusoidal embeddings on longer sequences, which saves multiple gigabytes of memory.<br>4 RESULTS<br>We first show that on WikiText103 ALiBi is efficient and enables training models with short input<br>subsequences that outperform strong baselines even when the ALiBi models extrapolate to more than<br>six times the number of tokens that they were trained on. We then take the same hyperparameters for<br>our method (the set of slopes) that worked on WikiText-103 and show that – with no modification<br>– they provide strong results on a dataset in a very different domain: books. Finally, we show that<br>a 1.3B parameter model trained with AliBi on a much larger (461 GB) dataset with much more<br>compute provides a superior alternative to the sinusoidal method since it achieves similar perplexity<br><!-- End of picture text -->

scores while running faster and using less memory (since it is trained on shorter inputs).

---

[referencia=25676193afe5f7ab score=0.904]
We demonstrate that this failure to extrapolate is caused by the position embedding method. As shown in Figure 1, recent alternatives to the original sinusoidal position method (Su et al., 2021; Raffel et al., 2020) have improved extrapolation. However, the better of these, the T5 bias, is considerably slower than the sinusoidal approach and uses extra memory and parameters (Figure 2). 

We therefore introduce Attention with Linear Biases (ALiBi) to facilitate efficient extrapolation. ALiBi negatively biases attention scores with a linearly decreasing penalty proportional to the distance between the relevant key and query. Our simple approach eliminates position embeddings. 

> 1Code & models: https://github.com/ofirpress/attention_with_linear_biases 

> 2Figure 7 in the appendix plots training speed, in words per second, against _L_ . 

1 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
Extrapolation for Extrapolation for<br>Models Trained on 512 Tokens Models Trained on 1024 Tokens<br>55 55<br>Sinusoidal<br>Rotary<br>45 45<br>Sinusoidal T5 Bias<br>Rotary ALiBi<br>35 35<br>T5 Bias<br>ALiBi<br>25 25<br>15 15<br>512 4000 8000 12000 16000 1024 4000 8000 12000 16000<br>Inference Input Tokens Inference Input Tokens<br>) )<br>Perplexity ( Perplexity (<br><!-- End of picture text -->

Figure 1: Extrapolation: as the (validation-set’s) input sequence gets longer ( _x_ -axis), current position methods (sinusoidal, rotary, and T5) show degraded perplexity ( _y_ -axis, lower is better), but our method (§3) does not. Models were trained on WikiText-103 with sequences of _L_ = 512 (left) or _L_ = 1,024 (right) tokens. T5 ran out of memory on our 32GB GPU. For more detail on exact perplexities and runtimes, see Tables 2 and 3 in the appendix.

---

[referencia=25676193afe5f7ab score=0.893]
## 5 RELATED WORK 

In parallel with our work, Wennberg & Henter (2021) introduce a relative position method that, like our method, adds a bias to attention scores that is a function of the distance between the key and query elements. Unlike our ALiBi method, which uses a non-learned linear function, their method uses a radial-basis function, with multiple trainable parameters (in our experiments, this led to a slight decrease in runtime). In addition, they present experiments on text classification, not on language modeling. They do not explore extrapolation. The Distance Aware Transformer (Wu et al., 2021) multiplies attention scores by a bias that is a function of the distance between the key and query. This function uses a different, learned parameter in every head. They show results only on text classification. In our experiments (not presented), multiplying attention scores by the bias (instead of adding, as in ALiBi) degraded performance. 

Transformer-XL (Dai et al., 2019) presented a language model that uses a cache and can attend to more tokens during inference than it was trained on (by increasing the length of the cache). However, this work presents results only where output length is limited to the _L_ (the training length), and their relative position method is very slow (Press et al., 2021). The Longformer (Beltagy et al., 2020) adapts models trained on shorter sequences to document-level tasks. However, to achieve this they had to partially train their models on longer sequences. Our ALiBi method enables extrapolation without any additional training on longer sequences.

---

[referencia=25676193afe5f7ab score=0.867]
Table 5: Perplexity when ALiBi extrapolates on the WikiText-103 development set.<sup>_∗_</sup> For results we present for the sinusoidal, rotary and T5 bias models, _L_ = _Lvalid_ (so we do not test the extrapolation abilities of those baselines here). 

|ALiBi|||E|valuation|Length||||
|---|---|---|---|---|---|---|---|---|
|Train Length|64|128|256|512|1024|1536|2048|3072|
|64|28.46|24.70|22.88|22.09|21.73|21.63|21.59|21.53|
|128|-|23.98|21.70|20.67|20.36|20.29|20.31|20.28|
|256|-|-|**21.29**|19.89|19.29|19.13|19.10|19.03|
|512|-|-|-|19.73|18.81|18.50|18.48|18.40|
|1024|-|-|-|-|**18.66**|18.20|18.05|17.96|
|1536|-|-|-|-|-|**18.12**|17.90|17.72|
|2048|-|-|-|-|-|-|**17.91**|17.64|
|3072|-|-|-|-|-|-|-|**17.60**|
|Sinusoidal<sup>_∗_</sup>|**28.03**|**23.81**|21.45|20.05|19.34|19.05|18.87|18.67|
|Rotary<sup>_∗_</sup>|-|-|-|20.07|19.33|-|-|18.57|
|T5 Bias<sup>_∗_</sup>|-|-|-|**19.65**|18.80|-|-|18.01|



Table 6 compares ALiBi to the sinusoidal, rotary and T5 bias baselines on the test set of WikiText103, and Table 7 compares ALiBi to the current state of the art models on that test set. 

19

---

[referencia=25676193afe5f7ab score=0.862]
|ValidationInput Length (Lvalid|)|
|---|---|
|Figure 9: ALiBi-enabled models evaluated on differe<br>Our models extrapolate to longer sequence lengths <br>when trained on much shorter sequences.|nt input lengths on the Toronto BookCorpus.<br> and outperform the sinusoidal baseline even|
|addition, our model is able to extrapolate to longer se<br>our set of slopes was_not_ tuned on this dataset. This<br>the particular set of slopes we found and suggests th<br>without further hyperparameter tuning.|quences at inference. This occurs even though<br>result establishes the generality of ALiBi and<br>at they may be used on different text domains|
|Tables 9 and 10 present the perplexities for our ALiB<br>of the art on the Toronto BookCorpus validation and t<br>WikiText-103: we improve over the sinusoidal baselin|i models, the baselines, and the current state<br>est sets. Our results here mirror our results on<br>e even when AliBi is trained on fewer tokens.|
|Table 8: ALiBi models extrapolating on the Toronto<br>of the sinusoidal models, _L_ = _Lvalid_ (so we do not te<br>here).|BookCorpus development set. <sup>_∗_</sup>For the results<br>st the extrapolation abilities of those models|
|Evalu|ation Length|
|Train Length<br>512|1024<br>3072|
|512<br>14.29|13.64<br>13.55|
|1024<br>-|13.86<br>13.52|
|3072<br>-|-<br>13.15|
|Sinusoidal<sup>_∗_</sup><br>14.80|14.73<br>14.46|



Table 9: Validation and test perplexities on the Toronto Book Corpus dataset.

---

[referencia=25676193afe5f7ab score=0.822]
## 3 ATTENTION WITH LINEAR BIASES (ALIBI) 

In the transformer model of Vaswani et al. (2017), position embeddings are added to the word embeddings at the bottom of the network. For an input subsequence of length _L_ , the attention sublayer computes the attention scores for the _i_ th query **q** _i ∈_ R<sup>1</sup><sup>_×d_</sup> , (1 _≤ i ≤ L_ ) in each head, given the first _i_ keys **K** _∈_ R<sup>_i×d_</sup> , where _d_ is the head dimension: 

softmax( **q** _i_ **K**<sup>_⊤_</sup> ) 

These attention scores are then multiplied by the values to return the output of the attention sublayer.<sup>9</sup> 

When using ALiBi, we do not add position embeddings at any point in the network. The only modification we apply is after the query-key dot product, where we add a static, non-learned bias:<sup>10</sup> 

softmax( **q** _i_ **K**<sup>_⊤_</sup> + _m ·_ [ _−_ ( _i −_ 1) _, ..., −_ 2 _, −_ 1 _,_ 0]) _,_ 

where scalar _m_ is a head-specific slope fixed before training. Figure 3 offers a visualization.

---

[referencia=25676193afe5f7ab score=0.820]
where scalar _m_ is a head-specific slope fixed before training. Figure 3 offers a visualization. 

For our models with 8 heads, the slopes that we used are the geometric sequence: 21<sup>1</sup><sup>_,_</sup> 2<sup><u>12</u></sup><sup>_, ...,_</sup> 2<sup><u>18</u>.</sup> For models that require 16 heads, we interpolate those 8 slopes by geometrically averaging every consecutive pair, resulting in the geometric sequence that starts at _~~√~~_ <u>12</u><sup>andhastheratioof</sup> _~~√~~_ <u>12</u><sup>:</sup> 2<sup>0</sup> <u>1</u><sup>_._5</sup><sup>_,_</sup> 2<sup><u>11</u></sup><sup>_,_</sup> 2<sup>1</sup> <u>1</u><sup>_._5</sup><sup>_, ...,_</sup> 2<sup><u>18</u>.In general, for</sup><sup>_n_heads, our set of slopes is the geometric sequence that starts</sup> _−_ <u>8</u> at 2 _n_ and uses that same value as its ratio. 

In §4, we observe that this set of slopes works on a wide variety of text domains and model sizes. Therefore, we do not believe that it is necessary to tune these slope values every time a new model is trained on a new dataset. This makes our method similar to the sinusoidal approach, where the hyperparameters (the start and end of the geometric progression of wavelengths) were set once by Vaswani et al. (2017) and then reused in different models of different sizes on different datasets. 

ALiBi has an inductive bias towards recency; it penalizes attention scores between distant query-key pairs, with the penalty increasing as the distance between a key and a query grows. The different heads increase their penalties at different rates, depending on the slope magnitude.

---

[referencia=25676193afe5f7ab score=0.789]
Figure 6: The ALiBi and sinusoidal models (with both _L_ = 512 and 1024) trained for 50k updates (1 epoch) on the CC100+RoBERTa corpus, extrapolating on the validation set. ALiBi achieves the best results at around 2 _L_ but maintains strong performance even up to 10000 tokens in these experiments. 

Figure 6 shows that our models trained on _L_ = 512 and _L_ = 1024 achieve the best results when extrapolating to about double the tokens that they were trained on. Specifically, the _L_ = 512 model (that obtains 9.79 perplexity when _Lvalid_ = 512) achieves its best score (9.3) when extrapolating to 

8 

Published as a conference paper at ICLR 2022 

1012 tokens, and the _L_ = 1024 model (that obtains 9.16 perplexity when _Lvalid_ = 1024) achieves its best score (8.9) when extrapolating to 2024 tokens. 

One possible explanation is that the subsequences the model observes during training are up to _L_ tokens long. When performing inference on subsequences of length 2 _L_ , half of the subsequences the model consumes are as long as the examples seen during training. When inference is performed on subsequences of length 2 _L_ + 1 or longer, less than half of the predictions the model makes are on subsequences of lengths seen during training, and that might degrade performance. 

The sinusoidal model cannot extrapolate at all in this setting, with its performance degrading for both the _L_ = 512 and 1024 models as soon as one token more than _L_ is added during evaluation. 

In Appendix B, we find that ALiBi’s edge over sinusoidal embeddings is largely explained by its improved avoidance of the early token curse. We posit that future work building on ALiBi might achieve further gains by more efficiently exploiting longer histories.

---

[referencia=25676193afe5f7ab score=0.767]
We initially experimented with making the slopes trainable, but this did not yield strong extrapolation results.<sup>11</sup> A brief manual exploration of around ten slope sets led us to discover the set of slopes that we finally picked. Our main insight from this exploration is that the slope sets that work best are those with slopes in the (0 _,_ 1) range, with the slopes’ density increasing as we get closer to 0. We also found our method to be robust to slope choice. Even randomly sampling from the exponential distribution worked well in some cases (although that method had high variance). 

Since ALiBi is a relative position method, we add position information at every layer to the keys and queries but not to the values, as is done in the T5 bias and rotary methods. We hypothesize that these properties might be beneficial for extrapolation. 

> 9For simplicity we omit the key, query, value and final output projections, dropout, and the scaling factor. 

> 10The ALiBi bias is not multiplied by the<sup>_~~√~~_</sup> _dk_ scaling factor from Equation 1 of Vaswani et al. (2017). 

> 11In our experiments, trainable slopes also slowed down the training speed by 3%. 

5 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->

---

[referencia=25676193afe5f7ab score=0.756]
### A.2 ALIBI RESULTS ON WIKITEXT-103 



<!-- Start of picture text -->
Training Speed vs. Valid Perple(it)<br>19.0 with Lvalid = 3072<br>Sinus idal<br>L = 3072 ALiBi<br>18.5<br>L = 512<br>18.0 L = 102←<br>L = 3072 L = 1536<br>L = 20←8<br>17.5<br>15000 20000 25000 30000<br>Training W rds Per Sec nd (→→<br>Perple(it) (←→<br><!-- End of picture text -->

Figure 8: The training speed and validation perplexity (with _Lvalid_ = 3072) for ALiBi models and the sinusoidal model trained with _L_ = 3072. All our models trained on 512 or more tokens achieve better perplexity than the sinusoidal model even though all of them (except the _L_ = 3072) require less time and memory to train. 

Figure 8 depicts a cross section of Figure 4, showing our models with different train lengths and the sinusoidal baseline, all evaluated on _Lvalid_ = 3072 tokens. We observe that all our models with 512 _≤ L <_ 3072 are faster to train than the sinusoidal model with _L_ = 3072, but they all achieve greater perplexity scores on the validation set. Our model with _L_ = 3072 trains just as fast as the sinusoidal one but bests its score by more than one perplexity point; (the standard deviation for the the sinusoidal model with _L_ = 3072 is 0.24). 

Table 5 shows the perplexity values obtained when 8 different ALiBi models, trained on _L_ values between 64 and 3072, extrapolating to _Lvalid_ values longer than the ones they were trained on. In addition, we present results for the sinusoidal, rotary and T5 bias models, with _Lvalid_ = _L_ .

---

[referencia=25676193afe5f7ab score=0.706]
Published as a conference paper at ICLR 2022 

- TRAIN SHORT, TEST LONG: ATTENTION WITH LINEAR BIASES ENABLES INPUT LENGTH EXTRAPOLATION 

- <sup>1</sup><sup>_,_2</sup> **Noah A. Smith**<sup>1</sup><sup>_,_3</sup> **Mike Lewis**<sup>2</sup> 

- 1Paul G. Allen School of Computer Science & Engineering, University of Washington 2Facebook AI Research 

- 3Allen Institute for AI

---

[referencia=25676193afe5f7ab score=0.688]
- Tables 2, 3, and 4 show the perplexity and runtime of models using the sinusoidal, rotary T5 bias, and ALiBi position methods when extrapolating to sequences longer than the ones they were trained on. The models used in these tables were trained on _L_ = 512 _,_ 1024 and 3072 tokens. 

15 

Published as a conference paper at ICLR 2022 

Table 2: The sinusoidal, rotary, T5 bias and ALiBi models trained on _L_ = **512** on WikiText-103 and evaluated with different values of _Lvalid_ on the validation set. **Bold** shows the best score for each model. Inference speeds (in words per second) are from inference on a GPU with batch size of one.

---

[referencia=25676193afe5f7ab score=0.684]
Our ALiBi results mirror what occurs in the model using the T5 bias: when using sliding window evaluation, perplexity remains relatively flat when evaluating longer sequences (see Table 14). 

Our analysis reveals that when _Lvalid > L_ , ALiBi might not be using contexts longer than the ones it was trained on. This highlights a research direction that could be pursued in future work. 

These findings do not lessen the value of ALiBi. When _Lvalid_ = _L_ , ALiBi achieves either superior or similar results to the sinusoidal method and other alternatives even though it is simpler and requires no learned parameters. When evaluating _Lvalid > L_ tokens, even if ALiBi does not attend to more than _L_ tokens, it yields better results than the other alternatives that can be used in this case, i.e., standard nonoverlapping inference (which is cheap, but does not perform as well) and the more accurate sliding window approach (which is very slow). 

> 13100 tokens is an arbitrary small number used here to represent a short history context, i.e., one in which making predictions for the next output token would be harder. 

24 

Published as a conference paper at ICLR 2022 

Table 13: Perplexities of the **sinusoidal** models evaluated with sliding window evaluation with stride _S_ = 1 on the WikiText-103 validation dataset. 

|||Evaluati|on Length|(_S_ = 1)||
|---|---|---|---|---|---|
|Train Length|512|1024|1536|2048|3072|
|512|18.35|204.42|264.74|306.19|360.12|
|1024|-|18.05|206.55|302.6|393.71|
|3072|-|-|-|-|18.03|



Table 14: Perplexities of the **T5 bias** models evaluated with sliding window evaluation with stride _S_ = 1 on the WikiText-103 validation dataset.

---

[referencia=25676193afe5f7ab score=0.679]
<!-- Start of picture text -->
ALiBi and Sinu(oidal<br>Evalua)ion (w/ Sliding Window)<br>on WikiTex)-103<br>19.5<br>Sinusoidal, L = 512<br>19.0 Sinusoidal, L = 1024<br>Sinusoidal, L = 3072<br>18.5<br>ALiBi, L = 512<br>18.0 ALiBi, L = 1024<br>ALiBi, L = 3072<br>17.5<br>17.0<br>16.5<br>512 1024 1536 2048 3072<br>Validation Input Lengt  (Lvalid)<br>Perplexi). (←)<br><!-- End of picture text -->

Figure 11: ALiBi models evaluated on different input lengths on WikiText-103 with sliding window evaluation (with stride _S_ = 1). Unlike results shown in Figure 4, where performance improves in each of our models as we increase the validation sequence length, here performance stays relatively flat as we increase _Lvalid_ . This might mean that ALiBi increases performance when _Lvalid > L_ not because it uses longer contexts, but because fewer tokens suffer from the early token curse. Note that as in §2, the perplexity of the sinusoidal model explodes when _Lvalid > L_ even when using sliding window evaluation. 

The results are shown in Figure 11 and in the corresponding Tables 13 (sinusoidal) and 15 (ALiBi). 

Unsurprisingly, for the sinusoidal model, as in §2, increasing _Lvalid_ causes an explosion in perplexity even when using sliding window evaluation. Our ALiBi models cannot improve perplexity when looking at longer sequences in this setting, but they keep perplexity flat when _Lvalid_ increases. 

This leads us to believe that our perplexity improvement when increasing _Lvalid_ and using nonoverlapping evaluation is caused by explanation 2, not explanation 1. Because sliding window evaluation provides long context windows for _every_ prediction made, it curtails the early token curse. In this setting, ALiBi’s performance remains flat when _Lvalid_ increases, leading us to hypothesize that the gains seen while increasing _Lvalid_ in §4 were the result of larger _Lvalid_ values mitigating the early token curse.

---

[referencia=25676193afe5f7ab score=0.678]
30k <u>Training Speed</u> 100k <u>Inference Speed</u> 30 <u>Training Memory</u> Sinusoidal 20k 75k 20 Rotary 50k 10k 25k 10 T5 Bias ALiBi 0 512 1024 3072 0k 512 1024 3072 0 512 1024 3072 Input Length Input Length Input Length Figure 2: A comparison of batched training, inference speed and memory use of the sinusoidal, rotary, T5 bias, and our ALiBi position methods. The speed differences between our method and the sinusoidal are within 1% during training and 3% for inference, which is insignificant on our hardware. ALiBi uses 100MB of extra memory when training on input lengths 1024 and 3072 in this setting. Memory usage is lower in all approaches when training on 3072 tokens (compared to 1024) since we break batches into multiple updates. See Table 1 in the appendix for exact numbers. **Nonoverlapping Inference** To train on or evaluate a sequence longer than _L_ tokens, it is typical to segment the sequence into _L_ -length subsequences and train on or evaluate them independently. Unless otherwise stated, we use nonoverlapping inference to report perplexity scores. **Extrapolation During Inference** Formally, the functions that define a transformer layer are agnostic to input length;<sup>3</sup> they map from some arbitrary, unfixed number of input vectors to the same number of output vectors. When transformers are applied to data that is inherently sequential, like text, positional information is injected into the inputs in various ways. Vaswani et al. (2017) discussed two options for embedding positions into vectors to be added to word embeddings: learning embeddings for specific positions and unlearned sinusoidal embeddings. They observed similar performance between these two but preferred the sinusoidal approach, which they argued might extrapolate to longer input sequences during inference. We find that this model cannot extrapolate to more than a few dozen tokens beyond _L_ .<sup>4</sup> **Experiment Setup**