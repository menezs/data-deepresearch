[referencia=bf9cd21d7a7afdff score=0.935]
Table 9: Switch model design and pre-training performance. We compare the hyperparameters and pre-training performance of the T5 models to our Switch Transformer variants. The last two columns record the pre-training model quality on the C4 data set after 250k and 500k steps, respectively. We observe that the SwitchC Transformer variant is 4x faster to a fixed perplexity (with the same compute budget) than the T5-XXL model, with the gap increasing as training progresses. 

depth, number of heads, and so on, are all much smaller than the T5-XXL model. In contrast, the Switch-XXL is FLOP-matched to the T5-XXL model, which allows for larger dimensions of the hyper-parameters, but at the expense of additional communication costs induced by model-parallelism (see Section 5.5 for more details). 

**Sample efficiency versus T5-XXL.** In the final two columns of Table 9 we record the negative log perplexity on the C4 corpus after 250k and 500k steps, respectively. After 250k steps, we find both Switch Transformer variants to improve over the T5-XXL version’s negative log perplexity by over 0.061.<sup>10</sup> To contextualize the significance of a gap of 0.061, we note that the T5-XXL model had to train for an _additional_ 250k steps to increase 0.052. The gap continues to increase with additional training, with the Switch-XXL model out-performing the T5-XXL by 0.087 by 500k steps. 

**Training instability.** However, as described in the introduction, large sparse models can be unstable, and as we increase the scale, we encounter some sporadic issues. We find that the larger Switch-C model, with 1.6T parameters and 2048 experts, exhibits no training instability at all. Instead, the Switch XXL version, with nearly 10x larger FLOPs per sequence, is sometimes unstable. As a result, though this is our better model on a step-basis, we do not pre-train for a full 1M steps, in-line with the final reported results of T5 (Raffel et al., 2019).

---

[referencia=bf9cd21d7a7afdff score=0.906]
- The Switch Transformer architecture, which simplifies and improves over Mixture of Experts. 

- Scaling properties and a benchmark against the strongly tuned T5 model (Raffel et al., 2019) where we measure 7x+ pre-training speedups while still using the same FLOPS per token. We further show the improvements hold even with limited computational resources, using as few as two experts. 

- Successful distillation of sparse pre-trained and specialized fine-tuned models into small dense models. We reduce the model size by up to 99% while preserving 30% of the quality gains of the large sparse teacher. 

- Improved pre-training and fine-tuning techniques: **(1)** selective precision training that enables training with lower bfloat16 precision **(2)** an initialization scheme that allows for scaling to a larger number of experts and **(3)** increased expert regularization that improves sparse model fine-tuning and multi-task training. 

- A measurement of the pre-training benefits on multilingual data where we find a universal improvement across all 101 languages and with 91% of languages benefiting from 4x+ speedups over the mT5 baseline (Xue et al., 2020). 

- An increase in the scale of neural language models achieved by efficiently combining data, model, and expert-parallelism to create models with up to a trillion parameters. These models improve the pre-training speed of a strongly tuned T5-XXL baseline by 4x.

---

[referencia=bf9cd21d7a7afdff score=0.899]
8 

Switch Transformers 

|Model|Capacity<br>Factor|Quality after<br>100k steps (_↑_)<br>(Neg. Log Perp.)|Time to Quality<br>Threshold (_↓_)<br>(hours)|Speed (_↑_)<br>(examples/sec)|
|---|---|---|---|---|
|T5-Base|—|-1.731|Not achieved<sup>_†_</sup>|1600|
|T5-Large|—|-1.550|131.1|470|
|MoE-Base|2.0|-1.547|68.7|840|
|Switch-Base|2.0|-1.554|72.8|860|
|MoE-Base|1.25|-1.559|80.7|790|
|Switch-Base|1.25|-1.553|65.0|910|
|MoE-Base|1.0|-1.572|80.1|860|
|Switch-Base|1.0|-1.561|**62.8**|1000|
|Switch-Base+|1.0|**-1.534**|67.6|780|



- Table 1: Benchmarking Switch versus MoE. Head-to-head comparison measuring per step and per time benefits of the Switch Transformer over the MoE Transformer and T5 dense baselines. We measure quality by the negative log perplexity and the time to reach an arbitrary chosen quality threshold of Neg. Log Perp.=-1.50. All MoE and Switch Transformer models use 128 experts, with experts at every other feed-forward layer. For Switch-Base+, we increase the model size until it matches the speed of the MoE model by increasing the model hidden-size from 768 to 896 and the number of heads from 14 to 16. All models are trained with the same amount of computation (32 cores) and on the same hardware (TPUv3). Further note that all our models required pre-training beyond 100k steps to achieve our level threshold of -1.50. _†_ T5-Base did not achieve this negative log perplexity in the 100k steps the models were trained. 

in the softmax computation for our router. We describe training difficulties here and the methods we use to overcome them to achieve stable and scalable training.

---

[referencia=bf9cd21d7a7afdff score=0.891]
9. The speedup on a step basis is computed as the ratio of the number of steps for the baseline divided by the number of steps required by our model to reach that same quality. 

18 

Switch Transformers 



<!-- Start of picture text -->
0.4<br>0.6<br>0.8<br>1.0<br>1.2<br>1.4<br>1.6<br>1.8 Switch<br>Dense<br>Language<br>Neg. Log Perplexity<br>ja nyxh mr su zh eo bg-latn ms zu so et ta la hi-latn ha sn ht myjvaf mi fi fil sw no eu lo sv yode en th co tr ml fy es ar sl mn kysi iw hu is ko ja-latn ro uz zh-latn te am km kk ku nl st it da mglt sr sqmt glhi cs hmn ighaw lv fr sm ru gask ur tgyipt az psbgru-latn ca plmk id kn ne fa be ka el-latn uk gubn cyhylb pael ceb vi sd gd<br><!-- End of picture text -->

- Figure 7: Multilingual pre-training on 101 languages. Improvements of Switch T5 Base model over dense baseline when multi-task training on 101 languages. We observe Switch Transformers to do quite well in the multi-task training setup and yield improvements on all 101 languages. 



<!-- Start of picture text -->
50<br>40<br>30<br>20<br>10<br>0<br>4 6 8 10 12 14 16<br>Switch Speedup over Dense Baseline<br>Number of Languages<br><!-- End of picture text -->

Figure 8: Multilingual pre-training on 101 languages. We histogram for each language, the step speedup of Switch Transformers over the FLOP matched T5 dense baseline to reach the same quality. Over all 101 languages, we achieve a mean step speedup over mT5-Base of 5x and, for 91% of languages, we record a 4x, or greater, speedup to reach the final perplexity of mT5-Base. 

and computation performed and is ultimately limited by the memory per accelerator. Once it exceeds the size of the accelerator’s memory, single program multiple data (SPMD) modelparallelism can be employed. This section studies the trade-offs of combining data, model, and expert-parallelism.

---

[referencia=bf9cd21d7a7afdff score=0.882]
### **3.3 Scaling Versus a Larger Dense Model** 

The above analysis shows that a computationally-matched dense model is outpaced by its Switch counterpart. Figure 6 considers a different scenario: what if we instead had allocated our resources to a larger dense model? We do so now, measuring Switch-Base against the 

next strong baseline, _T5-Large_ . But despite T5-Large applying 3.5x more FLOPs per token, 

13 

Fedus, Zoph and Shazeer 

Switch-Base is still more sample efficient and yields a 2.5x speedup. Furthermore, more gains can be had simply by designing a new, larger sparse version, Switch-Large, which is FLOP-matched to T5-Large. We do this and demonstrate superior scaling and fine-tuning in the following section. 



<!-- Start of picture text -->
1.2 1.2<br>1.3 1.3<br>1.4 1.4 2.5x Speedup<br>1.5 1.5 7.0x Speedup<br>1.6 1.6<br>1.7 1.7<br>1.8 1.8<br>Switch-Base: 64e Switch-Base: 64e<br>1.9 T5-Large 1.9 T5-Large<br>T5-Base T5-Base<br>2.0 2.0<br>0 1 2 3 4 50 100 150 200 250 300 350<br>Training Step 1e5 Training Time<br>Neg Log Perplexity Neg Log Perplexity<br><!-- End of picture text -->

Figure 6: Scaling Transformer models with Switch layers or with standard dense model scaling. Left Plot: Switch-Base is more sample efficient than both the T5-Base, and T5-Large variant, which applies 3.5x more FLOPS per token. Right Plot: As before, on a wall-clock basis, we find that Switch-Base is still faster, and yields a 2.5x speedup over T5-Large.

---

[referencia=bf9cd21d7a7afdff score=0.872]
|10<sup>9</sup><br>10<sup>10</sup><br>Sparse Model Parameters<br>4.8<br>0<br>1<br>2<br>3<br>4<br>Training Step<br>1e5<br>2.0|



Figure 4: Scaling properties of the Switch Transformer. Left Plot: We measure the quality improvement, as measured by perplexity, as the parameters increase by scaling the number of experts. The top-left point corresponds to the T5-Base model with 223M parameters. Moving from top-left to bottom-right, we double the number of experts from 2, 4, 8 and so on until the bottom-right point of a 256 expert model 

with 14.7B parameters. Despite all models using an equal computational budget, we observe consistent improvements scaling the number of experts. Right Plot: Negative log perplexity per step sweeping over the number of experts. The dense baseline is shown with the purple line and we note improved sample efficiency of our Switch-Base models. 

12 

Switch Transformers 

### **3.2 Scaling Results on a Time-Basis** 

### Figure 4 demonstrates that on a step basis, as we increase the number of experts, the 

performance consistently improves. While our models have roughly the same amount of FLOPS per token as the baseline, our Switch Transformers incurs additional communication costs across devices as well as the extra computation of the routing mechanism. Therefore, the increased sample efficiency observed on a step-basis doesn’t necessarily translate to a better model quality as measured by wall-clock. This raises the question: _For a fixed training duration and computational budget, should one train a dense or a sparse model?_ 

#### 1.2 

1.3 1.4 1.5 ~~7x Speedup~~ 1.6 1.7 

1.8 Switch-Base: 128e Switch-Base: 64e 1.9 Switch-Base: 32e T5-Base 2.0 50 100 150 200 250 300 350 Training Time 

Figure 5: Speed advantage of Switch Transformer. All models trained on 32 TPUv3 cores with equal FLOPs per example. For a fixed amount of computation and training time, Switch Transformers significantly outperform the dense Transformer baseline. Our 64 expert Switch-Base model achieves the same quality in _one-seventh_

---

[referencia=bf9cd21d7a7afdff score=0.858]
<br>using top-2 routing, has two experts which each apply a separate FFN to each token and<br>thus its FLOPS are larger. All models were trained for the same number of steps on identical<br>hardware. Note that the MoE model going from capacity factor 2.0 to 1.25 actually slows<br>down (840 to 790) in the above experiment setup, which is unexpected. 5<br>We highlight three key findings from Table 1: (1) Switch Transformers outperform<br>both carefully tuned dense models and MoE Transformers on a speed-quality basis. For<br>a fixed amount of computation and wall-clock time, Switch Transformers achieve the best<br>result. (2) The Switch Transformer has a smaller computational footprint than the MoE<br>counterpart. If we increase its size to match the training speed of the MoE Transformer,<br>we find this outperforms all MoE and Dense models on a per step basis as well. (3) Switch<br>Transformers perform better at lower capacity factors (1.0, 1.25). Smaller expert capacities<br>are indicative of the scenario in the large model regime where model memory is very scarce<br>and the capacity factor will want to be made as small as possible.<br><!-- End of picture text -->

**2.4 Improved Training and Fine-Tuning Techniques** Sparse expert models may introduce training difficulties over a vanilla Transformer. Instability can result because of the hard-switching (routing) decisions at each of these layers. Further, low precision formats like bfloat16 (Wang and Kanwar, 2019) can exacerbate issues 

4. We use log base- _e_ for this metric so the units are nats. 

5. Note that speed measurements are both a function of the algorithm and the implementation details. Switch Transformer reduces the necessary computation relative to MoE (algorithm), but the final speed differences are impacted by low-level optimizations (implementation). 

8 

Switch Transformers

---

[referencia=bf9cd21d7a7afdff score=0.842]
## **D. Switch Transformers in Lower Compute Regimes** 

Switch Transformer is also an effective architecture at small scales as well as in regimes with thousands of cores and trillions of parameters. Many of our prior experiments were 

29 

Fedus, Zoph and Shazeer 



<!-- Start of picture text -->
Expert 1 Expert 2 Expert 3<br>Stage-2<br>Route token to<br>second highest<br>probability if not<br>routed<br>Stage-1<br>Route token to<br>highest probability<br>0.1 0.7 0.5 0.8 0.3 0.7<br>0.7 0.2 0.3 0.1 0.1 0.1<br>0.2 0.1 0.2 0.1 0.6 0.2<br>Router<br>Tokens<br>Probabilities<br><!-- End of picture text -->

Figure 11: Diagram of the _No-Token-Left-Behind Routing_ . Stage 1 is equivalent to Switch routing where tokens are routed to the expert with the highest probability from the router. In Stage 2 we look at all tokens that have overflowed and route them to the expert with which has the second highest probability. Tokens can still be overflowed if their second highest expert has too many tokens, but this allows most of the tokens to be routed. This process can be iterated to guarantee virtually no tokens are dropped at all. 

|Model|Quality (Neg. Log Perp.) (_↑_)|
|---|---|
|Argmax|-1.471|
|Sample softmax|-1.570|
|Input dropout|-1.480|
|Input jitter|**-1.468**|



Table 11: Router Exploration Strategies. Quality of the Switch Transformer, measured by the negative log perplexity, under different randomness-strategies for selecting the expert (lower is better). There is no material speed performance difference between the variants. 

at the scale of 10B+ parameter models, but we show in Figure 12 as few as 2 experts produce compelling gains over a FLOP-matched counterpart. Even if a super computer is not readily available, training Switch Transformers with 2, 4, or 8 experts (as we typically recommend one expert per core) results in solid improvements over T5 dense baselines. 

30 

Switch Transformers 



<!-- Start of picture text -->

---

[referencia=bf9cd21d7a7afdff score=0.840]
the P -vector is differentiable, but the f -vector is not. The final loss is multiplied by expert<br>count N to keep the loss constant as the number of experts varies since under uniform<br>routing � N i =1 ( fi · Pi ) = � N i =1 ( N 1 · N 1 ) = N 1 . Finally, a hyper-parameter α is a multiplicative<br>coefficient for these auxiliary losses; throughout this work we use an α = 10 − 2 which was<br>sufficiently large to ensure load balancing while small enough to not to overwhelm the<br>primary cross-entropy objective. We swept hyper-parameter ranges of α from 10 − 1 to 10 − 5<br>in powers of 10 and found 10 − 2 balanced load quickly without interfering with training loss.<br>2.3 Putting It All Together: The Switch Transformer<br>Our first test of the Switch Transformer starts with pre-training on the “Colossal Clean<br>Crawled Corpus” (C4), introduced in (Raffel et al., 2019). For our pre-training objective,<br>we use a masked language modeling task (Taylor, 1953; Fedus et al., 2018; Devlin et al.,<br>2018) where the model is trained to predict missing tokens. In our pre-training setting, as<br>determined in Raffel et al. (2019) to be optimal, we drop out 15% of tokens and then replace<br>the masked sequence with a single sentinel token. To compare our models, we record the<br>negative log perplexity. 4 Throughout all tables in the paper,  ↑ indicates that a higher value<br>for that metric is better and vice-versa for ↓ . A comparison of all the models studied in<br>this work are in Table 9.<br>A head-to-head comparison of the Switch Transformer and the MoE Transformer is<br>presented in Table 1. Our Switch Transformer model is FLOP-matched to ‘T5-Base’ (Raffel<br>et al., 2019) (same amount of computation per token is applied). The MoE Transformer,<br>using top-2 routing, has two experts which each apply a separate FFN to each token and<br>thus its FLOPS are larger. All models were trained for the same number of steps on identical<br>

---

[referencia=bf9cd21d7a7afdff score=0.835]
### the time of the T5-Base and continues to improve. 

Figures 5 and 6 address this question. Figure 5 measures the pre-training model quality as a function of time. For a fixed training duration and computational budget, Switch Transformers yield a substantial speed-up. In this setting, our Switch-Base 64 expert model trains in _one-seventh_ the time that it would take the T5-Base to get similar perplexity.

---

[referencia=bf9cd21d7a7afdff score=0.829]
26 

Switch Transformers 

layer replaces the weight matrices which produce Q, K, V. However, due to training instabilities with the bfloat16 format, we instead leave this as an area for future work. 

6. Examining Switch Transformer in new and across different modalities. We have thus far only considered language, but we believe that model sparsity can similarly provide advantages in new modalities, as well as multi-modal networks. 

This list could easily be extended, but we hope this gives a flavor for the types of challenges that we are thinking about and what we suspect are promising future directions. 

## **9. Conclusion** 

Switch Transformers are scalable and effective natural language learners. We simplify Mixture of Experts to produce an architecture that is easy to understand, stable to train and vastly more sample efficient than equivalently-sized dense models. We find that these models excel across a diverse set of natural language tasks and in different training regimes, including pre-training, fine-tuning and multi-task training. These advances make it possible to train models with hundreds of billion to trillion parameters and which achieve substantial speedups relative to dense T5 baselines. We hope our work motivates sparse models as an effective architecture and that this encourages researchers and practitioners to consider these flexible models in natural language tasks, and beyond. 

## **Acknowledgments** 

The authors would like to thank Margaret Li who provided months of key insights into algorithmic improvements and suggestions for empirical studies. Hugo Larochelle for sage advising and clarifying comments on the draft, Irwan Bello for detailed comments and careful revisions, Colin Raffel and Adam Roberts for timely advice on neural language models and the T5 code-base, Yoshua Bengio for advising and encouragement on research in adaptive computation, Jascha Sohl-dickstein for interesting new directions for stabilizing new large scale models and paper revisions, and the Google Brain Team for useful discussions on the paper. Blake Hechtman who provided invaluable help in profiling and improving the training performance of our models.

---

[referencia=31ff4e3be2e00940 score=0.819]
## **1 Introduction** 

In this paper, we present Mixtral 8x7B, a sparse mixture of experts model (SMoE) with open weights, licensed under Apache 2.0. Mixtral outperforms Llama 2 70B and GPT-3.5 on most benchmarks. As it only uses a subset of its parameters for every token, Mixtral allows faster inference speed at low batch-sizes, and higher throughput at large batch-sizes. 

Mixtral is a sparse mixture-of-experts network. It is a decoder-only model where the feedforward block picks from a set of 8 distinct groups of parameters. At every layer, for every token, a router network chooses two of these groups (the “experts”) to process the token and combine their output additively. This technique increases the number of parameters of a model while controlling cost and latency, as the model only uses a fraction of the total set of parameters per token. 

Mixtral is pretrained with multilingual data using a context size of 32k tokens. It either matches or exceeds the performance of Llama 2 70B and GPT-3.5, over several benchmarks. In particular, 



**Figure 1: Mixture of Experts Layer.** Each input vector is assigned to 2 of the 8 experts by a router. The layer’s output is the weighted sum of the outputs of the two selected experts. In Mixtral, an expert is a standard feedforward block as in a vanilla transformer architecture. 

Mixtral demonstrates superior capabilities in mathematics, code generation, and tasks that require multilingual understanding, significantly outperforming Llama 2 70B in these domains. Experiments show that Mixtral is able to successfully retrieve information from its context window of 32k tokens, regardless of the sequence length and the location of the information in the sequence. 

We also present Mixtral 8x7B – Instruct, a chat model fine-tuned to follow instructions using supervised fine-tuning and Direct Preference Optimization [25]. Its performance notably surpasses that of GPT-3.5 Turbo, Claude-2.1, Gemini Pro, and Llama 2 70B – chat model on human evaluation benchmarks. Mixtral – Instruct also demonstrates reduced biases, and a more balanced sentiment profile in benchmarks such as BBQ, and BOLD.

---

[referencia=bf9cd21d7a7afdff score=0.808]
|Model|Parameters|FLOPS|SuperGLUE (_↑_)|
|---|---|---|---|
|T5-Base|223M|124B|74.6|
|Switch-Base|7410M|124B|81.3|
|Distilled T5-Base|223M|124B|(30%) 76.6|



Table 8: Distilling a fine-tuned SuperGLUE model. We distill a Switch-Base model finetuned on the SuperGLUE tasks into a T5-Base model. We observe that on smaller data sets our large sparse model can be an effective teacher for distillation. We find that we again achieve 30% of the teacher’s performance on a 97% compressed model. 

pre-training both versions for 1M steps, we find that on _all_ 101 languages considered, Switch Transformer increases the final negative log perplexity over the baseline. In Figure 8, we present a different view and now histogram the per step _speed-up_ of using Switch Transformer over the mT5-Base.<sup>9</sup> We find a mean speed-up over mT5-Base of 5x and that 91% of languages achieve at least a 4x speedup. This presents evidence that Switch Transformers are effective multi-task and multi-lingual learners. 

**5. Designing Models with Data, Model, and Expert-Parallelism** 

Arbitrarily increasing the number of experts is subject to diminishing returns (Figure 4). Here we describe _complementary_ scaling strategies. The common way to scale a Transformer is to increase dimensions in tandem, like _dmodel_ or _dff_ . This increases both the parameters 

9. The speedup on a step basis is computed as the ratio of the number of steps for the baseline divided by the number of steps required by our model to reach that same quality. 

18 

Switch Transformers 



<!-- Start of picture text -->

---

[referencia=bf9cd21d7a7afdff score=0.803]
## **Abstract** 

In deep learning, models typically reuse the same parameters for all inputs. Mixture of Experts (MoE) models defy this and instead select _different_ parameters for each incoming example. The result is a sparsely-activated model—with an outrageous number of parameters—but a constant computational cost. However, despite several notable successes of MoE, widespread adoption has been hindered by complexity, communication costs, and training instability. We address these with the introduction of the Switch Transformer. We simplify the MoE routing algorithm and design intuitive improved models with reduced communication and computational costs. Our proposed training techniques mitigate the instabilities, and we show large sparse models may be trained, for the first time, with lower precision (bfloat16) formats. We design models based off T5-Base and T5-Large (Raffel et al., 2019) to obtain up to 7x increases in pre-training speed with the same computational resources. These improvements extend into multilingual settings where we measure gains over the mT5-Base version across all 101 languages. Finally, we advance the current scale of language models by pre-training up to trillion parameter models on the “Colossal Clean Crawled Corpus”, and achieve a 4x speedup over the T5-XXL model.<sup>12</sup> 

**Keywords:** mixture-of-experts, natural language processing, sparsity, large-scale machine learning, distributed computing 

> ∗. Equal contribution. 

> 1. JAX code for Switch Transformer and all model checkpoints are available at `https://github.com/ google-research/t5x` 

> 2. Tensorflow code for Switch Transformer is available at `https://github.com/tensorflow/mesh/blob/ master/mesh_tensorflow/transformer/moe.py` 

> ©2022 William Fedus, Barret Zoph and Noam Shazeer. 

License: CC-BY 4.0, see `https://creativecommons.org/licenses/by/4.0/` . Attribution requirements are provided at `http://jmlr.org/papers/v23/21-0998.html` . 

Fedus, Zoph and Shazeer

---

[referencia=bf9cd21d7a7afdff score=0.800]
> 10. This reported quality difference is a lower bound, and may actually be larger. The T5-XXL was pretrained on an easier C4 data set which included duplicated, and thus easily copied, snippets within examples. 

23 

Fedus, Zoph and Shazeer 

**Reasoning fine-tuning performance.** As a preliminary assessment of the model quality, we use a Switch-XXL model partially pre-trained on 503B tokens, or approximately half the text used by the T5-XXL model. Using this checkpoint, we conduct multi-task training for efficiency, where all tasks are learned jointly, rather than individually fine-tuned. We find that SQuAD accuracy on the validation set increases to 89.7 versus state-of-the-art of 91.3. Next, the average SuperGLUE test score is recorded at 87.5 versus the T5 version obtaining a score of 89.3 compared to the state-of-the-art of 90.0 (Wang et al., 2019). On ANLI (Nie et al., 2019), Switch XXL improves over the prior state-of-the-art to get a 65.7 accuracy versus the prior best of 49.4 (Yang et al., 2020). We note that while the Switch- 

XXL has state-of-the-art Neg. Log Perp. on the upstream pre-training task, its gains have not yet fully translated to SOTA downstream performance. We study this issue more in Appendix E. 

**Knowledge-based fine-tuning performance.** Finally, we also conduct an early examination of the model’s knowledge with three closed-book knowledge-based tasks: Natural Questions, WebQuestions and TriviaQA, without additional pre-training using Salient Span Masking (Guu et al., 2020). In all three cases, we observe improvements over the prior stateof-the-art T5-XXL model (without SSM). Natural Questions exact match increases to 34.4 versus the prior best of 32.8, Web Questions increases to 41.0 over 37.2, and TriviaQA increases to 47.5 versus 42.9. 

Summing up, despite training on less than half the data of other models, we already find comparable, and sometimes state-of-the-art, model quality. Currently, the Switch Transformer translates substantial upstream gains better to knowledge-based tasks, than

---

[referencia=bf9cd21d7a7afdff score=0.777]
## **1. Introduction** 

Large scale training has been an effective path towards flexible and powerful neural language models (Radford et al., 2018; Kaplan et al., 2020; Brown et al., 2020). Simple architectures— backed by a generous computational budget, data set size and parameter count—surpass more complicated algorithms (Sutton, 2019). An approach followed in Radford et al. (2018); Raffel et al. (2019); Brown et al. (2020) expands the model size of a densely-activated Transformer (Vaswani et al., 2017). While effective, it is also extremely computationally intensive (Strubell et al., 2019). Inspired by the success of model scale, but seeking greater computational efficiency, we instead propose a _sparsely-activated_ expert model: the Switch Transformer. In our case the sparsity comes from activating a _subset_ of the neural network weights for each incoming example. 



<!-- Start of picture text -->
1e 1.2<br>6.0 Switch-Base: 128e<br>2e 1.3 Switch-Base: 64eSwitch-Base: 32e<br>5.8 Switch-Base: 16e<br>4e 1.4 T5-Base<br>5.6 8e 1.5<br>5.4 1.6<br>16e<br>1.7<br>5.2 32e<br>64e 1.8<br>5.0 128e 1.9<br>256e<br>4.8 2.0<br>10 9 10 10 0 1 2 3 4<br>Sparse Model Parameters Training Step 1e5<br>Test Loss<br>Neg Log Perplexity<br><!-- End of picture text -->

Figure 1: Scaling and sample efficiency of Switch Transformers. Left Plot: Scaling properties for increasingly sparse (more experts) Switch Transformers. Right Plot: Negative log perplexity comparing Switch Transformers to T5 (Raffel et al., 2019) models using the same compute budget.

---

[referencia=bf9cd21d7a7afdff score=0.775]
are broadcast through all-to-all communication operations, but we still benefit from the increased stability of float32. 

**Smaller parameter initialization for stability** . Appropriate initialization is critical to successful training in deep learning and we especially observe this to be true for Switch Transformer. We initialize our weight matrices by drawing elements from a truncated normal distribution with mean _µ_ = 0 and standard deviation _σ_ = ~~�~~ _s/n_ where _s_ is a scale hyper-parameter and _n_ is the number of input units in the weight tensor (e.g. fan-in).<sup>6</sup> 

As an additional remedy to the instability, we recommend reducing the default Transformer initialization scale _s_ = 1 _._ 0 by a factor of 10. This both improves quality and reduces the likelihood of destabilized training in our experiments. Table 3 measures the improvement of the model quality and reduction of the variance early in training. We find that 

|Model (Initialization scale)|Average Quality|Std. Dev. of Quality|
|---|---|---|
||(Neg. Log Perp.)|(Neg. Log Perp.)|
|Switch-Base (0.1x-init)|**-2.72**|**0.01**|
|Switch-Base (1.0x-init)|-3.60|0.68|



Table 3: Reduced initialization scale improves stability. Reducing the initialization scale results in better model quality and more stable training of Switch Transformer. Here we record the average and standard deviation of model quality, measured by the negative log perplexity, of a 32 expert model after 3.5k steps (3 random seeds each). 

the average model quality, as measured by the Neg. Log Perp., is dramatically improved and there is a far reduced variance across runs. Further, this same initialization scheme is broadly effective for models spanning several orders of magnitude. We use the same approach to stably train models as small as our 223M parameter baseline to enormous models in excess of one trillion parameters. 

> 6. Values greater than two standard deviations from the mean are resampled. 

10 

Switch Transformers

---

[referencia=bf9cd21d7a7afdff score=0.734]
## **2. Switch Transformer** 

The guiding design principle for Switch Transformers is to maximize the parameter count of a Transformer model (Vaswani et al., 2017) in a simple and computationally efficient way. The benefit of scale was exhaustively studied in Kaplan et al. (2020) which uncovered powerlaw scaling with model size, data set size and computational budget. Importantly, this work advocates training large models on relatively small amounts of data as the computationally optimal approach. 

Heeding these results, we investigate a fourth axis: increase the _parameter count_ while keeping the floating point operations (FLOPs) per example constant. Our hypothesis is that the parameter count, independent of total computation performed, is a separately important axis on which to scale. We achieve this by designing a sparsely activated model that efficiently uses hardware designed for dense matrix multiplications such as GPUs and TPUs. Our work here focuses on TPU architectures, but these class of models may be similarly trained on GPU clusters. In our distributed training setup, our sparsely activated layers split _unique_ weights on different devices. Therefore, the weights of the model increase with the number of devices, all while maintaining a manageable memory and computational footprint on each device. 

4 

Switch Transformers 



<!-- Start of picture text -->
y1 y2<br>Add + Normalize<br>y<br>FFN 1 FFN 2 FFN 3 FFN 4 FFN 1 FFN 2 FFN 3 FFN 4<br>Add + Normalize<br>p = 0.8<br>Switching FFN Layer p = 0.65<br>Add + Normalize Router Router<br>Self-Attention<br>Add + Normalize<br>x Self-Attention<br>Positional Positional<br>embedding embedding<br>x1 x2<br>More Parameters<br><!-- End of picture text -->

Figure 2: Illustration of a Switch Transformer encoder block. We replace the dense feed forward network (FFN) layer present in the Transformer with a sparse Switch FFN layer (light blue). The layer operates independently on the tokens in the sequence. We diagram two tokens ( _x_ 1 = “More” and _x_ 2 = “Parameters” below) being routed (solid lines) across four FFN experts, where the router independently 

routes each token. The switch FFN layer returns the output of the selected FFN multiplied by the router gate value (dotted-line).

---

[referencia=31ff4e3be2e00940 score=0.698]
|**Mixtral 8x7B**|13B|**70.6%**|84.4%|77.2%|**83.6%**|**83.1%**|**59.7%**|**30.6%**|71.5%|**40.2%**|**60.7%**|**28.4%**|**74.4%**|



**Table 2: Comparison of Mixtral with Llama.** Mixtral outperforms or matches Llama 2 70B performance on almost all popular benchmarks while using 5x fewer active parameters during inference. 



**Figure 3: Results on MMLU, commonsense reasoning, world knowledge and reading comprehension, math and code for Mistral (7B/8x7B) vs Llama 2 (7B/13B/70B)** . Mixtral largely outperforms Llama 2 70B on all benchmarks, except on reading comprehension benchmarks while using 5x lower active parameters. It is also vastly superior to Llama 2 70B on code and math. 

Detailed results for Mixtral, Mistral 7B and Llama 2 7B/13B/70B and Llama 1 34B<sup>2</sup> are reported in Table 2. Figure 2 compares the performance of Mixtral with the Llama models in different categories. Mixtral surpasses Llama 2 70B across most metrics. In particular, Mixtral displays a superior performance in code and mathematics benchmarks. 

**Size and Efficiency.** We compare our performance to the Llama 2 family, aiming to understand Mixtral models’ efficiency in the cost-performance spectrum (see Figure 3). As a sparse Mixtureof-Experts model, Mixtral only uses 13B active parameters for each token. With 5x lower active parameters, Mixtral is able to outperform Llama 2 70B across most categories.

---

[referencia=bf9cd21d7a7afdff score=0.690]
|tokens passed between the layers. In this section, we consider the scaling properties on a<br>step-basis and a time-basis with a fxed computational budget.|
|---|
|**3.1 Scaling Results on a Step-Basis**|
|Figure 4 demonstrates consistent scaling benefts with the number of experts when training<br>all models for a fxed number of steps. We observe a clear trend: when keeping the FLOPS<br>per token fxed, having more parameters (experts) speeds up training.<br>The left Figure<br>demonstrates consistent scaling properties (with fxed FLOPS per token) between sparse<br>model parameters and test loss. This reveals the advantage of scaling along this additional<br>axis of sparse model parameters. Our right Figure measures sample efciency of a dense<br>model variant and four FLOP-matched sparse variants. We fnd that increasing the number<br>of experts leads to more sample efcient models. Our Switch-Base 64 expert model achieves<br>the same performance of the T5-Base model at step 60k at step 450k, which is a<br>7.5x<br>speedup in terms of step time. In addition, consistent with the fndings of Kaplan et al.<br>(2020), we fnd that larger models are also more _sample efcient_—learning more quickly<br>for a fxed number of observed tokens.|
|5.0<br>5.2<br>5.4<br>5.6<br>5.8<br>6.0<br>Test Loss<br>1e<br>2e<br>4e<br>8e<br>16e<br>~~32e~~<br>64e<br>~~128e~~<br>256e<br>1.9<br>1.8<br>1.7<br>1.6<br>1.5<br>1.4<br>1.3<br>1.2<br>Neg Log Perplexity<br>Switch-Base: 128e<br>Switch-Base: 64e<br>Switch-Base: 32e<br>Switch-Base: 16e<br>~~T5-Base~~|