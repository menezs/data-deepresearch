[referencia=25676193afe5f7ab score=0.990]
# TRAIN SHORT, TEST LONG: ATTENTION WITH LINEAR BIASES ENABLES INPUT LENGTH EXTRAPOLATION 

> <sup>1</sup><sup>_,_2</sup> **Noah A. Smith**<sup>1</sup><sup>_,_3</sup> **Mike Lewis**<sup>2</sup> 

1Paul G. Allen School of Computer Science & Engineering, University of Washington 2Facebook AI Research 

3Allen Institute for AI 

ofirp@cs.washington.edu 

### ABSTRACT 

Since the introduction of the transformer model by Vaswani et al. (2017), a fundamental question has yet to be answered: how does a model achieve extrapolation at inference time for sequences that are longer than it saw during training? We first show that extrapolation can be enabled by simply changing the position representation method, though we find that current methods do not allow for _efficient_ extrapolation. We therefore introduce a simpler and more efficient position method, Attention with Linear Biases (ALiBi). ALiBi does not add positional embeddings to word embeddings; instead, it biases query-key attention scores with a penalty that is proportional to their distance. We show that this method trains a 1.3 billion parameter model on input sequences of length 1024 that extrapolates to input sequences of length 2048, achieving the same perplexity as a sinusoidal position embedding model trained on inputs of length 2048 but training 11% faster and using 11% less memory. ALiBi’s inductive bias towards recency also leads it to outperform multiple strong position methods on the WikiText-103 benchmark.<sup>1</sup>

---

[referencia=25676193afe5f7ab score=0.987]
> 2Figure 7 in the appendix plots training speed, in words per second, against _L_ . 

1 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
Extrapolation for Extrapolation for<br>Models Trained on 512 Tokens Models Trained on 1024 Tokens<br>55 55<br>Sinusoidal<br>Rotary<br>45 45<br>Sinusoidal T5 Bias<br>Rotary ALiBi<br>35 35<br>T5 Bias<br>ALiBi<br>25 25<br>15 15<br>512 4000 8000 12000 16000 1024 4000 8000 12000 16000<br>Inference Input Tokens Inference Input Tokens<br>) )<br>Perplexity ( Perplexity (<br><!-- End of picture text -->

Figure 1: Extrapolation: as the (validation-set’s) input sequence gets longer ( _x_ -axis), current position methods (sinusoidal, rotary, and T5) show degraded perplexity ( _y_ -axis, lower is better), but our method (§3) does not. Models were trained on WikiText-103 with sequences of _L_ = 512 (left) or _L_ = 1,024 (right) tokens. T5 ran out of memory on our 32GB GPU. For more detail on exact perplexities and runtimes, see Tables 2 and 3 in the appendix. 

Compared to a sinusoidal model trained on the same input length, our method requires no additional runtime or parameters and incurs a negligible (0–0.7%) memory increase. ALiBi can be implemented by changing only a few lines of existing transformer code. 

Using ALiBi, a transformer LM can be trained on short- _L_ sequences and therefore at much lower cost, and it can still be reliably applied to long sequences at runtime. For example, a 1.3 billion parameter LM trained on _L_ = 1024 tokens with ALiBi achieves the same perplexity as a sinusoidal model trained on _L_ = 2048 when both are tested on sequences of 2048 tokens, even though _our model is 11% faster and uses 11% less memory._

---

[referencia=25676193afe5f7ab score=0.981]
#### A.4 RESULTS ON THE CC100+ROBERTA CORPUS 

Table 11 compares our 1.3 billion parameter ALiBi models when extrapolating to two times the number of tokens that they were trained on. We use the sinusoidal model as our baseline, and train it for the same amount of time as we train the ALiBi model that we compare it to (and so since our ALiBi models run faster in this setting, the sinusoidal models complete less updates). 

21 

Published as a conference paper at ICLR 2022 

Table 10: Validation and test perplexities on the Toronto Book Corpus dataset with a sliding window (§B). Following (Baevski & Auli, 2018; Khandelwal et al., 2020; Press et al., 2020; 2021), we set the sliding window stride _S_ =512. 

|Model|Param. _↓_|Valid_↓_|Test_↓_|
|---|---|---|---|
|kNN-LM (Khandelwal et al., 2020)|**247M**|14.20|10.89|
|Shortformer (Press et al., 2021)|**247M**|13.40|10.88|
|Sandwich (Press et al., 2020)|**247M**|-|10.83|
|Staged Training (Press et al., 2021)|**247M**|12.80|10.48|
|Sinusoidal, L = 3072|**247M**|14.06|11.40|
|iBi<br>_L_= 512,_Lvalid_= 3072|**247M**|13.76|11.11|
|AL<br>_L_= 3072,_Lvalid_= 3072|**247M**|12.70|10.40|



Table 11: Perplexity, memory, and train time on the CC100+RoBERTa corpus for our ALiBi models and the sinusoidal baseline. We run our _L_ = 512 (1024) model and the sinusoidal model with _L_ = 1024 (2048) for the same amount of time. We show that our models achieve strong results even though they use 6–11% less memory.

---

[referencia=25676193afe5f7ab score=0.980]
In Figure 5 (right), results become even more impressive, showing that our model trained on _L_ = 1024 outperforms by 0.09 perplexity the sinusoidal model trained on _L_ = 2048 (when evaluating with _Lvalid_ = 2048) even though our model uses 3.1 GB less memory. Our model maintains a lead in perplexity over the sinusoidal model during the entire training process. By sampling five evenly distributed points across the training process, we compute that our _L_ = 1024 model reaches a given perplexity value, on average, 11% faster than the sinusoidal model does. 

Since our models in these comparisons use much less memory, they allow for stacking more layers, which would further improve performance (with negligible, if any, runtime cost). To keep our experiments as straightforward as possible, however, we do not add layers to our models. 

Appendix Table 12 presents additional results comparing our models to the sinusoidal baseline when both are trained on the same _L_ , showing that ALiBi performs similarly to the sinusoidal baseline when not extrapolating. This contrasts with the results presented on the smaller datasets, where ALiBi consistently outperforms other position methods even when not extrapolating, suggesting that ALiBi’s inductive bias provides additional benefits for lower-resource language modeling. 



<!-- Start of picture text -->
Extrapolation, L = 512 Extrapolation, L = 1024<br>on CC100+RoBERTa on CC100+RoBERTa<br>10.2 10.2<br>Sinusoidal<br>9.8 9.8 ALiBi<br>9.4 9.4<br>9.0 Sinusoidal 9.0<br>ALiBi<br>8.6 8.6<br>512 2500 5000 7500 10000 1024 2500 5000 7500 10000<br>Validation Input Length (Lvalid) Validation Input Length (Lvalid)<br>) )<br>Perplexity ( Perplexity (<br><!-- End of picture text -->

---

[referencia=25676193afe5f7ab score=0.953]
|||Training||Valid P|PL_↓_|
|---|---|---|---|---|---|
||Memory_↓_|Updates|Hours_↓_|_Lvalid_= 1024|_Lvalid_= 2048|
|Sinusoidal,_Ltrain_= 1024|26.2 GB|46.7k|5.5k|**9.24**|-|
|ALiBi,_Ltrain_= 512|**24.6 GB**|50.0k|5.5k|9.30|-|
|Sinusoidal,_Ltrain_= 2048|29.3 GB|44.2k|5.9k|-|9.01|
|ALiBi,_Ltrain_= 1024|**26.2 GB**|50.0k|5.9k|-|**8.92**|



Table 12 compares our 1.3 billion parameter ALiBi models to the sinusoidal baselines, with and without extrapolation, with all models completing 50,000 updates. 

Table 12: Perplexity, train time and memory use of the sinusoidal and ALiBi models on the CC100+RoBERTa corpus when all models are trained with 50k updates.

---

[referencia=25676193afe5f7ab score=0.953]
### 1 INTRODUCTION 

When constructing a transformer-based language model, a major design decision is the length of training sequences, denoted _L_ herein, which has to date been equivalent to the length of inference sequences. More context, achieved by larger _L_ , improves predictions at inference time. But longer sequences are more expensive to train on.<sup>2</sup> 

Before transformers, RNN language models were trained on shorter- _L_ sequences and assumed to generalize to longer contexts at inference time (Mikolov et al., 2010; Mikolov & Zweig, 2012; Zaremba et al., 2014). Vaswani et al. (2017), introducing the transformer, speculated that it “may [...] extrapolate to sequence lengths longer than the ones encountered during training.” We define _extrapolation_ as a model’s ability to continue performing well as the number of input tokens during validation increases beyond the number of tokens on which the the model was trained. We find that transformer language models (LMs) that use sinusoidal position embeddings have very weak extrapolation abilities; see Figure 1. 

We demonstrate that this failure to extrapolate is caused by the position embedding method. As shown in Figure 1, recent alternatives to the original sinusoidal position method (Su et al., 2021; Raffel et al., 2020) have improved extrapolation. However, the better of these, the T5 bias, is considerably slower than the sinusoidal approach and uses extra memory and parameters (Figure 2). 

We therefore introduce Attention with Linear Biases (ALiBi) to facilitate efficient extrapolation. ALiBi negatively biases attention scores with a linearly decreasing penalty proportional to the distance between the relevant key and query. Our simple approach eliminates position embeddings. 

> 1Code & models: https://github.com/ofirpress/attention_with_linear_biases 

> 2Figure 7 in the appendix plots training speed, in words per second, against _L_ . 

1 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->

---

[referencia=25676193afe5f7ab score=0.947]
#### 4.1 RESULTS ON WIKITEXT-103 AND TORONTO BOOKCORPUS 



<!-- Start of picture text -->
AL B  Ex(rapola( ng on W k Tex(-103<br>21.0<br>AL B , L = 512<br>20.5<br>S nuso dal, L = 512<br>20.0 AL B , L = 1024<br>19.5 S nuso dal, L = 1024<br>19.0 AL B , L = 1536<br>18.5 S nuso dal, L = 1536<br>18.0 AL B , L = 2048<br>S nuso dal, L = 2048<br>17.5<br>AL B , L = 3072<br>17.0<br>512 1024 1536 2048 3072 S nuso dal, L = 3072<br>Validation Input Length (Lvalid)<br> (←←<br>Perplexi(y<br><!-- End of picture text -->

Figure 4: ALiBi models trained and evaluated on varying sequence lengths on the WikiText-103 validation set and the sinusoidal baseline (not evaluated on longer sequences). All of our models outperform the sinusoidal ones even when trained on fewer tokens. Appendix Table 5 has exact perplexities, more ALiBi models (trained on fewer tokens), and results for rotary and T5 bias models. 

We first develop our method on the WikiText-103 corpus (Merity et al., 2016), replacing the sinusoidal position embeddings in the language model of Baevski & Auli (2018) with ALiBi. 

Figure 4 (and the corresponding Appendix Table 5) show our results for models trained with varying numbers of input subsequence tokens ( _L_ ), extrapolating to longer subsequence lengths on the validation dataset. Our first observation is that, without extrapolation, for every _L_ , our models outperform those using the sinusoidal method, sometimes by a significant amount. For example, the Baevski & Auli model achieves 18.67 _±_ 0.24 (std. dev.) perplexity when trained with _L_ = 3072 input tokens, but our _L_ = 3072 model achieves 17.60 perplexity (when both models evaluate with _Lvalid_ = 3072). 

6

---

[referencia=25676193afe5f7ab score=0.942]
### 4 RESULTS 

We first show that on WikiText103 ALiBi is efficient and enables training models with short input subsequences that outperform strong baselines even when the ALiBi models extrapolate to more than six times the number of tokens that they were trained on. We then take the same hyperparameters for our method (the set of slopes) that worked on WikiText-103 and show that – with no modification – they provide strong results on a dataset in a very different domain: books. Finally, we show that a 1.3B parameter model trained with AliBi on a much larger (461 GB) dataset with much more compute provides a superior alternative to the sinusoidal method since it achieves similar perplexity scores while running faster and using less memory (since it is trained on shorter inputs). 

While multiple alternatives to the position methods presented in Vaswani et al. (2017) have been proposed, few have been adopted in large (1B or more parameter) LMs since that setting is much more challenging than the smaller scale experiments. GPT-3 and Jurassic-1 (Lieber et al., 2021) use the learned position embedding method from Vaswani et al., and GPT-J uses the rotary method. Our results on the 1.3B parameter model show our method’s ability to generalize to larger models, dataset sizes and training durations without retuning the hyperparameter.

---

[referencia=25676193afe5f7ab score=0.928]
Figure 6: The ALiBi and sinusoidal models (with both _L_ = 512 and 1024) trained for 50k updates (1 epoch) on the CC100+RoBERTa corpus, extrapolating on the validation set. ALiBi achieves the best results at around 2 _L_ but maintains strong performance even up to 10000 tokens in these experiments. 

Figure 6 shows that our models trained on _L_ = 512 and _L_ = 1024 achieve the best results when extrapolating to about double the tokens that they were trained on. Specifically, the _L_ = 512 model (that obtains 9.79 perplexity when _Lvalid_ = 512) achieves its best score (9.3) when extrapolating to 

8 

Published as a conference paper at ICLR 2022 

1012 tokens, and the _L_ = 1024 model (that obtains 9.16 perplexity when _Lvalid_ = 1024) achieves its best score (8.9) when extrapolating to 2024 tokens. 

One possible explanation is that the subsequences the model observes during training are up to _L_ tokens long. When performing inference on subsequences of length 2 _L_ , half of the subsequences the model consumes are as long as the examples seen during training. When inference is performed on subsequences of length 2 _L_ + 1 or longer, less than half of the predictions the model makes are on subsequences of lengths seen during training, and that might degrade performance. 

The sinusoidal model cannot extrapolate at all in this setting, with its performance degrading for both the _L_ = 512 and 1024 models as soon as one token more than _L_ is added during evaluation. 

In Appendix B, we find that ALiBi’s edge over sinusoidal embeddings is largely explained by its improved avoidance of the early token curse. We posit that future work building on ALiBi might achieve further gains by more efficiently exploiting longer histories.

---

[referencia=25676193afe5f7ab score=0.926]
#### 2.1 BACKGROUND AND EXPERIMENTAL SETUP 

A transformer LM receives a list of tokens and outputs a probability distribution representing its prediction for the next token. We call the input list the _current input subsequence_ since the inputs to language models are typically subsequences from (much longer) training or evaluation sequences. During both training and perplexity evaluation (i.e., scoring a fixed sequence), many predictions can be calculated at once; this is done using a “causal mask” that ensures each position’s prediction is influenced only by tokens to its left. Let _L_ be the length of each input subsequence during training; it includes _L_ predictions, which on average have access to<sup>_<u>L</u>_</sup><sup><u>+1</u></sup> 2 tokens of (left) context. To explore a model’s extrapolation abilities, we are interested in cases where sequences of length _Lvalid > L_ are considered at evaluation time. When _L_ differs between inference and training, we use _L_ to refer to the length of subsequences during training and _Lvalid_ to refer to their length at validation. 

2 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
30k Training Speed 100k Inference Speed 30 Training Memory<br>Sinusoidal<br>20k 75k 20 Rotary<br>50k<br>10k 25k 10 T5 Bias<br>ALiBi<br>0 512 1024 3072 0k 512 1024 3072 0 512 1024 3072<br>Input Length Input Length Input Length<br>) ) )<br>WPS ( WPS ( GB (<br><!-- End of picture text -->

Figure 2: A comparison of batched training, inference speed and memory use of the sinusoidal, rotary, T5 bias, and our ALiBi position methods. The speed differences between our method and the sinusoidal are within 1% during training and 3% for inference, which is insignificant on our hardware. ALiBi uses 100MB of extra memory when training on input lengths 1024 and 3072 in this setting. Memory usage is lower in all approaches when training on 3072 tokens (compared to 1024) since we break batches into multiple updates. See Table 1 in the appendix for exact numbers.

---

[referencia=25676193afe5f7ab score=0.918]
<!-- Start of picture text -->
ALiBi and Sinu(oidal<br>Evalua)ion (w/ Sliding Window)<br>on WikiTex)-103<br>19.5<br>Sinusoidal, L = 512<br>19.0 Sinusoidal, L = 1024<br>Sinusoidal, L = 3072<br>18.5<br>ALiBi, L = 512<br>18.0 ALiBi, L = 1024<br>ALiBi, L = 3072<br>17.5<br>17.0<br>16.5<br>512 1024 1536 2048 3072<br>Validation Input Lengt  (Lvalid)<br>Perplexi). (←)<br><!-- End of picture text -->

Figure 11: ALiBi models evaluated on different input lengths on WikiText-103 with sliding window evaluation (with stride _S_ = 1). Unlike results shown in Figure 4, where performance improves in each of our models as we increase the validation sequence length, here performance stays relatively flat as we increase _Lvalid_ . This might mean that ALiBi increases performance when _Lvalid > L_ not because it uses longer contexts, but because fewer tokens suffer from the early token curse. Note that as in §2, the perplexity of the sinusoidal model explodes when _Lvalid > L_ even when using sliding window evaluation. 

The results are shown in Figure 11 and in the corresponding Tables 13 (sinusoidal) and 15 (ALiBi). 

Unsurprisingly, for the sinusoidal model, as in §2, increasing _Lvalid_ causes an explosion in perplexity even when using sliding window evaluation. Our ALiBi models cannot improve perplexity when looking at longer sequences in this setting, but they keep perplexity flat when _Lvalid_ increases. 

This leads us to believe that our perplexity improvement when increasing _Lvalid_ and using nonoverlapping evaluation is caused by explanation 2, not explanation 1. Because sliding window evaluation provides long context windows for _every_ prediction made, it curtails the early token curse. In this setting, ALiBi’s performance remains flat when _Lvalid_ increases, leading us to hypothesize that the gains seen while increasing _Lvalid_ in §4 were the result of larger _Lvalid_ values mitigating the early token curse.

---

[referencia=25676193afe5f7ab score=0.916]
#### A.2 ALIBI RESULTS ON WIKITEXT-103 



<!-- Start of picture text -->
Training Speed vs. Valid Perple(it)<br>19.0 with Lvalid = 3072<br>Sinus idal<br>L = 3072 ALiBi<br>18.5<br>L = 512<br>18.0 L = 102←<br>L = 3072 L = 1536<br>L = 20←8<br>17.5<br>15000 20000 25000 30000<br>Training W rds Per Sec nd (→→<br>Perple(it) (←→<br><!-- End of picture text -->

Figure 8: The training speed and validation perplexity (with _Lvalid_ = 3072) for ALiBi models and the sinusoidal model trained with _L_ = 3072. All our models trained on 512 or more tokens achieve better perplexity than the sinusoidal model even though all of them (except the _L_ = 3072) require less time and memory to train. 

Figure 8 depicts a cross section of Figure 4, showing our models with different train lengths and the sinusoidal baseline, all evaluated on _Lvalid_ = 3072 tokens. We observe that all our models with 512 _≤ L <_ 3072 are faster to train than the sinusoidal model with _L_ = 3072, but they all achieve greater perplexity scores on the validation set. Our model with _L_ = 3072 trains just as fast as the sinusoidal one but bests its score by more than one perplexity point; (the standard deviation for the the sinusoidal model with _L_ = 3072 is 0.24). 

Table 5 shows the perplexity values obtained when 8 different ALiBi models, trained on _L_ values between 64 and 3072, extrapolating to _Lvalid_ values longer than the ones they were trained on. In addition, we present results for the sinusoidal, rotary and T5 bias models, with _Lvalid_ = _L_ .

---

[referencia=25676193afe5f7ab score=0.913]
#### 4.2 RESULTS ON THE CC100+ROBERTA CORPUS 

Our final set of experiments investigates whether ALiBi transfers to a larger model trained with a larger computational budget on a larger dataset than the ones we previously used. We show that our method achieves strong results in this more challenging setting, obtaining similar performance to the sinusoidal baseline while using significantly less memory, since we train on shorter subsequences. 

The dataset we choose is a combination of the datasets used to train the RoBERTa (Liu et al., 2019) implementation of BERT (Devlin et al., 2019) and the English part of the CC-100 corpus introduced in Conneau et al. (2020), for a total of 461 GB. The RoBERTa training corpus—i.e., the Toronto Book Corpus (Zhu et al., 2015), English Wikipedia, CC-News (Nagel, 2016), OpenWebText (Gokaslan & Cohen, 2019) and Stories (Trinh & Le, 2018))—is 161 gigabytes, and the English part of the CC-100 corpus is 300 gigabytes. The validation set contains 649K tokens. 

Our models for this dataset have 25 transformer layers with 16 heads and a dimension of 2048, with an 8192 hidden dimension of the feedforward sublayers. These models have 1.3B parameters. We train our models for one epoch, which is 50k updates on 128 V100 GPUs. 

In Figure 5 (left), we compare the validation perplexity for _Lvalid_ = 1024 throughout the training process for an ALiBi model trained with _L_ = 512 compared to the sinusoidal model trained with _L_ = 1024. Since our model is trained on shorter sequences, it is 7% faster and uses 1.6 GB less 

7 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->

---

[referencia=25676193afe5f7ab score=0.910]
Figure 9: ALiBi-enabled models evaluated on different input lengths on the Toronto BookCorpus. Our models extrapolate to longer sequence lengths and outperform the sinusoidal baseline even when trained on much shorter sequences. 

addition, our model is able to extrapolate to longer sequences at inference. This occurs even though our set of slopes was _not_ tuned on this dataset. This result establishes the generality of ALiBi and the particular set of slopes we found and suggests that they may be used on different text domains without further hyperparameter tuning. 

Tables 9 and 10 present the perplexities for our ALiBi models, the baselines, and the current state of the art on the Toronto BookCorpus validation and test sets. Our results here mirror our results on WikiText-103: we improve over the sinusoidal baseline even when AliBi is trained on fewer tokens. 

Table 8: ALiBi models extrapolating on the Toronto BookCorpus development set.<sup>_∗_</sup> For the results of the sinusoidal models, _L_ = _Lvalid_ (so we do not test the extrapolation abilities of those models here). 

||Evalu|ation Le|ngth|
|---|---|---|---|
|Train Length|512|1024|3072|
|512|14.29|13.64|13.55|
|1024|-|13.86|13.52|
|3072|-|-|13.15|
|Sinusoidal<sup>_∗_</sup>|14.80|14.73|14.46|



Table 9: Validation and test perplexities on the Toronto Book Corpus dataset. 

|Model|Param. _↓_|Valid_↓_|Test_↓_|
|---|---|---|---|
|Sinusoidal, L = 3072|**247M**|14.46|11.67|
|iBi<br>_Ltrain_= 512,_Lvalid_ = 3072|**247M**|13.55|10.98|
|AL<br>_Ltrain_= 3072,_Lvalid_= 3072|**247M**|**13.15**|**10.73**|

---

[referencia=25676193afe5f7ab score=0.910]
7 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
Validatio  Perple(it) Through Trai i g Validatio  Perple(it) Through Trai i g<br>11.0 with Lvalid = 10←4 11.0 with Lvalid = ←048<br>10.5 10.5<br>10.0 10.0<br>9.5 Si usoidal 9.5 Si usoidal<br>L = 10←4 L = ←048<br>9.0 ALiBi 9.0 ALiBi<br>L = 51← L = 10←4<br>8.5 8.5<br>0 1000 2000 3000 4000 5000 6000 0 1000 2000 3000 4000 5000 6000<br>Training Time (GPU Hours) Training Time (GPU Hours)<br>Perple(it) (←) Perple(it) (←)<br><!-- End of picture text -->

Figure 5: On the left (right), a 1.3B-parameter ALiBi model trained on 512 (1024) and evaluated on 1024 (2048) tokens during training, compared to the sinusoidal baseline trained on 1024 (2048) tokens. The ALiBi models obtain strong results even though they use 6%-11% less memory since they train on shorter sequences. Appendix Table 11 shows memory use and end-of-training perplexities. 

memory. We halt training of the sinusoidal baseline when our model reaches the end of its training (one epoch). At that time, our model is just 0.06 perplexity away from the baseline even though it was trained on sequences that are half the length of those the baseline used and requires less memory.

---

[referencia=25676193afe5f7ab score=0.907]
6 

Published as a conference paper at ICLR 2022 

Our second observation is that all of our models can extrapolate, and they obtain improved perplexity scores when handling more tokens than they observed during training. For example, our model trained on 512 tokens (which achieves 19.73 perplexity when evaluating subsequences of length 512 in the development set) achieves a perplexity score of 18.40 on the development set when extrapolating to subsequences of length 3072. Surprisingly, this surpasses the score that the _L_ = 3072 sinusoidal model obtains on the development set by a statistically significant margin. Note that all our models trained on _L_ = 512 to _L_ = 2048 outperform the sinusoidal baseline trained on _L_ = 3072 when extrapolating to _Lvalid_ = 3072 even though those models all take much less time to train since they train on shorter subsequences (Appendix Figure 8 compares training speed to perplexity for these models)! The _L_ = 512 model is 1.84 times faster to train and yet still outperforms the _L_ = 3072 sinusoidal model when extrapolating to _Lvalid_ = 3072. In addition, training the _L_ = 3072 sinusoidal model requires a GPU with more than 16 GB of memory to fit the large attention matrices, which our _L_ = 512 outperforms even though it can be trained on a GPU with much less memory due to much smaller attention matrices.

---

[referencia=25676193afe5f7ab score=0.885]
|Position Method|Train Length|Spee<br>Train|d (_↑_)<br>Eval.|Memory (_↓_)|
|---|---|---|---|---|
||512|28.5k|82.1k|15.3 GB|
|Sinusoidal|1024|26.0k|77.8k|19.2 GB|
||3072|15.3k|42.4k|15.1 GB|
||512|20.0k|43.4k|17.8 GB|
|Rotary|1024|17.7k|39.4k|22.8 GB|
||3072|11.5k|29.5k|17.8 GB|
||512|14.4k|21.8k|16.9 GB|
|T5 Bias|1024|13.0k|20.2k|20.9 GB|
||3072|4.3k|4.9k|15.9 GB|
||512|28.3k|85.8k|15.3 GB|
|ALiBi|1024|25.8k|76.4k|19.3 GB|
||3072|15.5k|42.2k|15.2 GB|



Tables 2, 3, and 4 show the perplexity and runtime of models using the sinusoidal, rotary T5 bias, and ALiBi position methods when extrapolating to sequences longer than the ones they were trained on. The models used in these tables were trained on _L_ = 512 _,_ 1024 and 3072 tokens. 

15 

Published as a conference paper at ICLR 2022 

Table 2: The sinusoidal, rotary, T5 bias and ALiBi models trained on _L_ = **512** on WikiText-103 and evaluated with different values of _Lvalid_ on the validation set. **Bold** shows the best score for each model. Inference speeds (in words per second) are from inference on a GPU with batch size of one.

---

[referencia=25676193afe5f7ab score=0.880]
### 3 ATTENTION WITH LINEAR BIASES (ALIBI) 

In the transformer model of Vaswani et al. (2017), position embeddings are added to the word embeddings at the bottom of the network. For an input subsequence of length _L_ , the attention sublayer computes the attention scores for the _i_ th query **q** _i ∈_ R<sup>1</sup><sup>_×d_</sup> , (1 _≤ i ≤ L_ ) in each head, given the first _i_ keys **K** _∈_ R<sup>_i×d_</sup> , where _d_ is the head dimension: 

softmax( **q** _i_ **K**<sup>_⊤_</sup> ) 

These attention scores are then multiplied by the values to return the output of the attention sublayer.<sup>9</sup> 

When using ALiBi, we do not add position embeddings at any point in the network. The only modification we apply is after the query-key dot product, where we add a static, non-learned bias:<sup>10</sup> 

softmax( **q** _i_ **K**<sup>_⊤_</sup> + _m ·_ [ _−_ ( _i −_ 1) _, ..., −_ 2 _, −_ 1 _,_ 0]) _,_ 

where scalar _m_ is a head-specific slope fixed before training. Figure 3 offers a visualization.

---

[referencia=25676193afe5f7ab score=0.875]
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

[referencia=25676193afe5f7ab score=0.867]
4 

Published as a conference paper at ICLR 2022 



<!-- Start of picture text -->
q1 k1<br>q2 k1 q2 k2<br>q3 k1 q3 k2 q3 k3<br>q4 k1 q4 k2 q4 k3 q4 k4<br>q5 k1 q5 k2 q5 k3 q5 k4 q5 k5<br><!-- End of picture text -->



<!-- Start of picture text -->
0<br>1 0<br>+ 2 1 0 m<br>3 2 1 0<br>4 3 2 1 0<br><!-- End of picture text -->

Figure 3: When computing attention scores for each head, our linearly biased attention method, ALiBi, adds a constant bias (right) to each attention score ( **q** _i ·_ **k** _j_ , left). As in the unmodified attention sublayer, the softmax function is then applied to these scores, and the rest of the computation is unmodified. **m is a head-specific scalar** that is set and not learned throughout training. We show that our method for setting _m_ values generalizes to multiple text domains, models and training compute budgets. When using ALiBi, we do _not_ add positional embeddings at the bottom of the network.