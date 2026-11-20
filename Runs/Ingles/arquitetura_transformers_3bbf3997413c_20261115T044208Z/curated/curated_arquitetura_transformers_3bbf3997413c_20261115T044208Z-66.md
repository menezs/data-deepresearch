[referencia=46fd66187ec3e6ae score=0.995]
### **5. Discussion & Conclusion** 

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget. 

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that _Gopher_ is substantially over-sized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training _Chinchilla_ , a 70B parameter model, and show that it outperforms _Gopher_ and even larger models on nearly every measured evaluation task. 

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale ( _Chinchilla_ and _Gopher_ ), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log<sup>�</sup> _𝑁𝑜𝑝𝑡_ � at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of _Chinchilla_ to _Gopher_ validates our performance predictions, that have thus enabled training a better (and more 

15

---

[referencia=46fd66187ec3e6ae score=0.987]
## **Training Compute-Optimal Large Language Models** 

**Jordan Hoffmann**<sup>_★_</sup> **, Sebastian Borgeaud**<sup>_★_</sup> **, Arthur Mensch**<sup>_★_</sup> **, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre**<sup>_★_</sup> 

> _★_ Equal contributions 

**We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model,** **_Chinchilla_ , that uses the same compute budget as** **_Gopher_ but with 70B parameters and 4** × **more more data.** **_Chinchilla_ uniformly and significantly outperforms** **_Gopher_ (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that** **_Chinchilla_ uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight,** **_Chinchilla_ reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_ .**

---

[referencia=46fd66187ec3e6ae score=0.981]
#### **_4.2.7. Gender bias and toxicity_** 

Large Language Models carry potential risks such as outputting offensive language, propagating social biases, and leaking private information (Bender et al., 2021; Weidinger et al., 2021). We expect _Chinchilla_ to carry risks similar to _Gopher_ because _Chinchilla_ is trained on the same data, 

_Chinchilla Gopher_ GPT-3 MT-NLG 530B Supervised SOTA 

HellaSWAG **80.8%** 79.2% 78.9% 80.2% 93.9% PIQA 81.8% 81.8% 81.0% **82.0%** 90.1% Winogrande **74.9%** 70.1% 70.2% 73.0% 91.3% SIQA **51.3%** 50.6% - - 83.2% BoolQ **83.7** % 79.3% 60.5% 78.2% 91.4% 

Table 8 | **Zero-shot comparison on Common Sense benchmarks.** We show a comparison between 

_Chinchilla_ , _Gopher_ , and MT-NLG 530B on various Common Sense benchmarks. We see that _Chinchilla_ matches or outperforms _Gopher_ and GPT-3 on all tasks. On all but one _Chinchilla_ outperforms the much larger MT-NLG 530B model. 

13

---

[referencia=46fd66187ec3e6ae score=0.978]
#### **4.2. Results** 

- We perform an extensive evaluation of _Chinchilla_ , comparing against various large language models. We evaluate on a large subset of the tasks presented in Rae et al. (2021), shown in Table 5. As 

- the focus of this work is on optimal model scaling, we included a large representative subset, and introduce a few new evaluations to allow for better comparison to other existing large models. The evaluation details for all tasks are the same as described in Rae et al. (2021). 

- **_4.2.1. Language modelling_** 

      - 0.10 0.08 0.06 0.04 0.02 0.00 

- Figure 5 | **Pile Evaluation.** For the different evaluation sets in The Pile (Gao et al., 2020), we show the bits-per-byte (bpb) improvement (decrease) of _Chinchilla_ compared to _Gopher_ . On all subsets, 

- _Chinchilla_ outperforms _Gopher_ . 

   - _Chinchilla_ significantly outperforms _Gopher_ on all evaluation subsets of The Pile (Gao et al., 

- 2020), as shown in Figure 5. Compared to Jurassic-1 (178B) Lieber et al. (2021), _Chinchilla_ is more performant on all but two subsets– `dm_mathematics` and `ubuntu_irc` – see Table A5 for a raw 

- bits-per-byte comparison. On Wikitext103 (Merity et al., 2017), _Chinchilla_ achieves a perplexity of 

- 7.16 compared to 7.75 for _Gopher_ . Some caution is needed when comparing _Chinchilla_ with _Gopher_ on these language modelling benchmarks as _Chinchilla_ is trained on 4× more data than _Gopher_ and 

- thus train/test set leakage may artificially enhance the results. We thus place more emphasis on other 

10

---

[referencia=46fd66187ec3e6ae score=0.978]
#### **_4.2.5. Common sense_** 

We evaluate _Chinchilla_ on various common sense benchmarks: PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), Winogrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), and BoolQ (Clark et al., 2019). We find that _Chinchilla_ outperforms both _Gopher_ and GPT-3 on all tasks and outperforms MT-NLG 530B on all but one task—see Table 8. 

On TruthfulQA (Lin et al., 2021), _Chinchilla_ reaches 43.6%, 58.5%, and 66.7% accuracy with 0-shot, 5-shot, and 10-shot respectively. In comparison, _Gopher_ achieved only 29.5% 0-shot and 43.7% 10-shot accuracy. In stark contrast with the findings of Lin et al. (2021), the large improvements (14.1% in 0-shot accuracy) achieved by Chinchilla suggest that better modelling of the pre-training data alone can lead to substantial improvements on this benchmark. 

12 

120 100 80 60 40 20 0 20 

Figure 7 | **BIG-bench results compared to** **_Gopher_** _Chinchilla_ out performs _Gopher_ on all but four BIG-bench tasks considered. Full results are in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.976]
The functions _𝑁𝑜𝑝𝑡_ ( _𝐶_ ), and _𝐷𝑜𝑝𝑡_ ( _𝐶_ ) describe the optimal allocation of a computational budget _𝐶_ . We empirically estimate these functions based on the losses of over 400 models, ranging from under 70M to over 16B parameters, and trained on 5B to over 400B tokens – with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ in Section 2. 

Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train _Gopher_ , an optimal model should be 4 times smaller, while being training on 4 times more tokens. We verify this by training a more _compute-optimal_ 70B model, called _Chinchilla_ , on 1.4 trillion tokens. Not only does _Chinchilla_ outperform its much larger counterpart, _Gopher_ , but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware. The energy cost of a large language model is amortized through its usage for inference an fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the immediate benefits of its improved performance. 

> 1For example, knowing the number of accelerators and a target training duration. 

> 2For simplicity, we perform our analysis on the smoothed training loss which is an unbiased estimate of the test loss, as we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus). 

2 

Table 1 | **Current LLMs** . We show five of the current largest dense transformer models, their size, and the number of training tokens. Other than LaMDA (Thoppilan et al., 2022), most models are trained for approximately 300 billion tokens. We introduce _Chinchilla_ , a substantially smaller model, trained for much longer than 300B tokens.

---

[referencia=46fd66187ec3e6ae score=0.973]
14 

||_Chinchilla_|_Gopher_||_Chinchilla_|_Gopher_|
|---|---|---|---|---|---|
|All|78.3%|71.4%|Male_gotcha_|62.5%|59.2%|
|Male|71.2%|68.0%|Male_not gotcha_|80.0%|76.7%|
|Female|79.6%|71.3%|Female_gotcha_|76.7%|66.7%|
|Neutral|84.2%|75.0%|Female_not gotcha_|82.5%|75.8%|



Table 10 | **Winogender results. Left:** _Chinchilla_ consistently resolves pronouns better than _Gopher_ . **Right:** _Chinchilla_ performs better on examples which contradict gender stereotypes ( _gotcha_ examples). However, difference in performance across groups suggests _Chinchilla_ exhibits bias. 

whether the same holds true for a lower LM loss achieved via more compute-optimal training. Similar to the protocol of Rae et al. (2021), we generate 25,000 unprompted samples from _Chinchilla_ , and compare their _PerspectiveAPI_ toxicity score distribution to that of _Gopher_ -generated samples. Several summary statistics indicate an absence of major differences: the mean (median) toxicity score for _Gopher_ is 0.081 (0.064), compared to 0.087 (0.066) for _Chinchilla_ , and the 95<sup>th</sup> percentile scores are 0.230 for _Gopher_ , compared to 0.238 for _Chinchilla_ . That is, the large majority of generated samples are classified as non-toxic, and the difference between the models is negligible. In line with prior findings (Rae et al., 2021), this suggests that toxicity levels in unconditional text generation are largely independent of the model quality (measured in language modelling loss), i.e. that better models of the training dataset are not necessarily more toxic.

---

[referencia=46fd66187ec3e6ae score=0.971]
31 

|Primary Intended Users|DeepMind researchers. We will not make this model available<br>publicly.|
|---|---|
|Out-of-Scope Uses|Uses of the language model for language generation in harm-<br>ful or deceitful settings. More generally, the model should not<br>be used for downstream applications without further safety<br>and fairness mitigations.|
||**Factors**|
|Card Prompts – Relevant Factor|Relevant factors include which language is used. Our model is<br>trained on English data. Furthermore, in the analysis of mod-<br>els trained on the same corpus inRae et al.(2021), we found<br>it has unequal performance when modelling some dialects<br>(e.g., African American English). Our model is designed for<br>research. The model should not be used for downstream ap-<br>plications without further analysis on factors in the proposed<br>downstream application.|
|Card Prompts – Evaluation Factors|See the results inRae et al.(2021) which analyzes models<br>trained on the same text corpus.|
||**Metrics**|
|Model Performance Measures|• Perplexity and bits per byte on language modelling<br>datasets<br>• Accuracy on completion tasks, reading comprehension,<br>MMLU, BIG-bench and fact checking.<br>• Exact match accuracy for question answering.<br>• Generation toxicity from Real Toxicity Prompts (RTP)<br>alongside toxicity classifcation accuracy.<br>• Gender and occupation bias. Test include comparing<br>the probability of generating diferent gender terms<br>and the Winogender coreference resolution task.<br>We principally focus on_Chinchilla_’s performance compared<br>to_Gopher_on text likelihood prediction.|
|Decision thresholds|N/A|
|Approaches to Uncertainty and Vari-<br>ability|Due to the costs of training large language models, we did<br>not train _Chinchilla_ multiple times. However, the breadth<br>of our evaluation on a range of diferent task types gives a<br>reasonable estimate of the overall performance of the model.<br>Furthermore, the existence of another large model trained<br>on the same dataset (_Gopher_) provides a clear point of com-<br>parison.|



#### **Evaluation Data** 

32

---

[referencia=46fd66187ec3e6ae score=0.956]
_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved 



<!-- Start of picture text -->
1T<br>Approach 1<br>100B<br>Approach 2<br>Approach 3<br>Kaplan et al (2020)<br>10B<br>Chinchilla (70B)<br>1.0B Gopher (280B)<br>GPT-3 (175B)<br>Megatron-Turing NLG (530B)<br>100M<br>10M<br>10 17 10 19 10 21 10 23 10 25<br>FLOPs<br>Parameters<br><!-- End of picture text -->

Figure 1 | **Overlaid predictions.** We overlay the predictions from our three different approaches, along with projections from Kaplan et al. (2020). We find that all three methods predict that current large models should be substantially smaller and therefore trained much longer than is currently done. In Figure A3, we show the results with the predicted optimal tokens plotted against the optimal number of parameters for fixed FLOP budgets. **_Chinchilla_ outperforms** **_Gopher_ and the other large models (see Section 4.2).** 

In this work, we revisit the question: _Given a fixed FLOPs budget,_<sup>1</sup> _how should one trade-off model size and the number of training tokens?_ To answer this question, we model the final pre-training loss<sup>2</sup> _𝐿_ ( _𝑁, 𝐷_ ) as a function of the number of model parameters _𝑁_ , and the number of training tokens, _𝐷_ . Since the computational budget _𝐶_ is a deterministic function FLOPs( _𝑁, 𝐷_ ) of the number of seen training tokens and model parameters, we are interested in minimizing _𝐿_ under the constraint FLOPs( _𝑁, 𝐷_ ) = _𝐶_ :

---

[referencia=46fd66187ec3e6ae score=0.953]
Table 3 | **Estimated optimal training FLOPs and training tokens for various model sizes.** For various model sizes, we show the projections from Approach 1 of how many FLOPs and training tokens would be needed to train compute-optimal models. The estimates for Approach 2 & 3 are similar (shown in Section D.3) 

Parameters FLOPs FLOPs (in _Gopher_ unit) Tokens 400 Million 1.92e+19 1/29 _,_ 968 8.0 Billion 

1 Billion 1.21e+20 1/4 _,_ 761 20.2 Billion 10 Billion 1.23e+22 1/46 205.1 Billion 67 Billion 5.76e+23 1 1.5 Trillion . 175 Billion 3.85e+24 6 _._ 7 3.7 Trillion 280 Billion 9.90e+24 17 _._ 2 5.9 Trillion 520 Billion 3.43e+25 59 _._ 5 11.0 Trillion 1 Trillion 1.27e+26 221 _._ 3 21.2 Trillion 10 Trillion 1.30e+28 22515 _._ 9 216.2 Trillion 

large language models are considerably over-sized, given their respective compute budgets, as shown in Figure 1. For example, we find that a 175 billion parameter model should be trained with a compute budget of 4 _._ 41 × 10<sup>24</sup> FLOPs and on over 4.2 trillion tokens. A 280 billion _Gopher_ -like model is the optimal model to train given a compute budget of approximately 10<sup>25</sup> FLOPs and should be trained on 6.8 trillion tokens. Unless one has a compute budget of 10<sup>26</sup> FLOPs (over 250× the compute used to 

train _Gopher_ ), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale. While there is significant uncertainty extrapolating out

---

[referencia=46fd66187ec3e6ae score=0.943]
### **4.** **_Chinchilla_** 

Based on our analysis in Section 3, the optimal model size for the _Gopher_ compute budget is somewhere between 40 and 70 billion parameters. We test this hypothesis by training a model on the larger end of this range—70B parameters—for 1.4T tokens, due to both dataset and computational efficiency considerations. In this section we compare this model, which we call _Chinchilla_ , to _Gopher_ and other LLMs. Both _Chinchilla_ and _Gopher_ have been trained for the same number of FLOPs but differ in the size of the model and the number of training tokens. 

While pre-training a large language model has a considerable compute cost, downstream finetuning and inference also make up substantial compute usage (Rae et al., 2021). Due to being 4× smaller than _Gopher_ , both the memory footprint and inference cost of _Chinchilla_ are also smaller.

---

[referencia=46fd66187ec3e6ae score=0.941]
||_Chinchilla_|_Gopher_|GPT-3|MT-NLG 530B|
|---|---|---|---|---|
|LAMBADA Zero-Shot|**77.4**|74.5|76.2|76.6|
|RACE-m Few-Shot|**86.8**|75.1|58.1|-|
|RACE-h Few-Shot|**82.3**|71.6|46.8|47.9|



Table 7 | **Reading comprehension.** On RACE-h and RACE-m (Lai et al., 2017), _Chinchilla_ considerably improves performance over _Gopher_ . Note that GPT-3 and MT-NLG 530B use a different prompt format than we do on RACE-h/m, so results are not comparable to _Gopher_ and _Chinchilla_ . On LAMBADA (Paperno et al., 2016), _Chinchilla_ outperforms both _Gopher_ and MT-NLG 530B. 

`mathematical_induction` and `logical_args` . Full accuracy results for _Chinchilla_ can be found in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.920]
#### **4.1. Model and training details** 

The full set of hyperparameters used to train _Chinchilla_ are given in Table 4. _Chinchilla_ uses the same model architecture and training setup as _Gopher_ with the exception of the differences listed below. 

- We train _Chinchilla_ on _MassiveText_ (the same dataset as _Gopher_ ) but use a slightly different subset distribution (shown in Table A1) to account for the increased number of training tokens. 

- We use AdamW (Loshchilov and Hutter, 2019) for _Chinchilla_ rather than Adam (Kingma and Ba, 2014) as this improves the language modelling loss and the downstream task performance after finetuning.<sup>8</sup> 

- We train _Chinchilla_ with a slightly modified SentencePiece (Kudo and Richardson, 2018) tokenizer that does not apply NFKC normalisation. The vocabulary is very similar– 94.15% of tokens are the same as those used for training _Gopher_ . We find that this particularly helps with the representation of mathematics and chemistry, for example. 

- Whilst the forward and backward pass are computed in `bfloat16` , we store a `float32` copy of the weights in the distributed optimiser state (Rajbhandari et al., 2020). See _Lessons Learned_ from Rae et al. (2021) for additional details. 

In Appendix G we show the impact of the various optimiser related changes between _Chinchilla_ and _Gopher_ . All models in this analysis have been trained on TPUv3/TPUv4 (Jouppi et al., 2017) with JAX (Bradbury et al., 2018) and Haiku (Hennigan et al., 2020). We include a _Chinchilla_ model card (Mitchell et al., 2019) in Table A8.

---

[referencia=46fd66187ec3e6ae score=0.909]
#### **_4.2.4. BIG-bench_** 

We analysed _Chinchilla_ on the same set of BIG-bench tasks (BIG-bench collaboration, 2021) reported in Rae et al. (2021). Similar to what we observed in MMLU, _Chinchilla_ outperforms _Gopher_ on the vast majority of tasks (see Figure 7). We find that _Chinchilla_ improves the average performance by 10.7%, reaching an accuracy of 65.1% versus 54.4% for _Gopher_ . Of the 62 tasks we consider, _Chinchilla_ performs worse than _Gopher_ on only four— `crash_blossom, dark_humor_detection,` 

11 



<!-- Start of picture text -->
30<br>20<br>10<br>0<br>10<br> over Gopher<br>Relative Improvement<br>college_mathematics econometrics moral_scenarios formal_logic medical_genetics machine_learning public_relations global_facts business_ethics electrical_engineering college_computer_science world_religions high_school_us_history high_school_psychology management high_school_computer_science marketing high_school_physics high_school_macroeconomics sociology high_school_government_and_politics high_school_european_history nutrition college_medicine astronomy logical_fallacies professional_psychology miscellaneous jurisprudence clinical_knowledge high_school_geography high_school_biology college_biology college_chemistry high_school_world_history us_foreign_policy virology philosophy moral_disputes human_aging computer_security security_studies international_law high_school_microeconomics high_school_statistics professional_accounting professional_medicine prehistory high_school_chemistry elementary_mathematics abstract_algebra anatomy professional_law human_sexuality college_physics high_school_mathematics conceptual_physics<br><!-- End of picture text -->

Figure 6 | **MMLU results compared to** **_Gopher_** We find that _Chinchilla_ outperforms _Gopher_ by 7.6% on average (see Table 6) in addition to performing better on 51/57 individual tasks, the same on 2/57, and worse on only 4/57 tasks.

---

[referencia=46fd66187ec3e6ae score=0.900]
### **G. Other differences between** **_Chinchilla_ and** **_Gopher_** 

Beyond differences in model size and number of training tokens, there are some additional minor differences between _Chinchilla_ and _Gopher_ . Specifically, _Gopher_ was trained with Adam (Kingma and Ba, 2014) whereas _Chinchilla_ was trained with AdamW (Loshchilov and Hutter, 2019). Furthermore, as discussed in _Lessons Learned_ in Rae et al. (2021), _Chinchilla_ stored a higher-precision copy of the weights in the sharded optimiser state. 

We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7. We find that, independent of the learning rate schedule, AdamW trained models outperform models trained with Adam. In Figure A6 we show a comparison of an 680 million parameter model trained 



<!-- Start of picture text -->
2.70 26 3.00<br>Training Setup<br>25 2.95 Adam w/ High Precision<br>2.65 24 2.90 AdamW w/ High Precision<br>Adam No High Precision<br>23<br>2.60 2.85 AdamW No High Precision<br>22<br>2.80<br>21<br>2.55 2.75<br>20<br>2.50 19 2.70<br>18 2.65<br>2.45 17 2.60<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>Training Loss<br>Wikitext103 Perplexity<br><!-- End of picture text -->

Figure A6 | **Comparison of other differences.** Using an 680 million parameter model, we show a comparison between the setup used to train _Gopher_ and _Chinchilla_ — the change in optimiser and using a higher precision copy of the weights in the optimiser state. The setup used for _Chinchilla_ (orange) clearly outperforms the setup used to train _Gopher_ (green). 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.876]
#### **_4.2.2. MMLU_** 

The Massive Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) consists of a range of exam-like questions on academic subjects. In Table 6, we report _Chinchilla_ ’s average 5-shot performance on MMLU (the full breakdown of results is shown in Table A6). On this benchmark, _Chinchilla_ significantly outperforms _Gopher_ despite being much smaller, with an average accuracy of 67.6% (improving upon _Gopher_ by 7.6%). Remarkably, _Chinchilla_ even outperforms the expert forecast for June 2023 of 63.4% accuracy (see Table 6) (Steinhardt, 2021). Furthermore, _Chinchilla_ achieves greater than 90% accuracy on 4 different individual tasks– `high_school_gov_and_politics, international_law, sociology` , and `us_foreign_policy` . To our knowledge, no other model has achieved greater than 90% accuracy on a subset. 

In Figure 6, we show a comparison to _Gopher_ broken down by task. Overall, we find that _Chinchilla_ improves performance on the vast majority of tasks. On four tasks ( `college_mathematics, econometrics, moral_scenarios` , and `formal_logic` ) _Chinchilla_ underperforms _Gopher_ , and there is no change in performance on two tasks. 

#### **_4.2.3. Reading comprehension_** 

On the final word prediction dataset LAMBADA (Paperno et al., 2016), _Chinchilla_ achieves 77.4% accuracy, compared to 74.5% accuracy from _Gopher_ and 76.6% from MT-NLG 530B (see Table 7). On RACE-h and RACE-m (Lai et al., 2017), _Chinchilla_ greatly outperforms _Gopher_ , improving accuracy by more than 10% in both cases—see Table 7.

---

[referencia=46fd66187ec3e6ae score=0.836]
|**Model**|**Layers**|**Number Heads**|**Key/Value Size**|**dmodel**|**Max LR**|**Batch Size**|
|---|---|---|---|---|---|---|
|_Gopher_280B|80|128|128|16,384|4×10<sup>−5</sup>|3M→6M|
|_Chinchilla_70B|80|64|128|8,192|1×10<sup>−4</sup>|1.5M→3M|



Table 4 | **_Chinchilla_ architecture details.** We list the number of layers, the key/value size, the bottleneck activation size dmodel, the maximum learning rate, and the training batch size (# tokens). The feed-forward size is always set to 4 × dmodel. Note that we double the batch size midway through training for both _Chinchilla_ and _Gopher_ . 

> 8Interestingly, a model trained with AdamW only passes the training performance of a model trained with Adam around 80% of the way through the cosine cycle, though the ending performance is notably better– see Figure A7 

9 

-

---

[referencia=46fd66187ec3e6ae score=0.810]
#### **H.1. The Pile** 

In Table A5 we show the bits-per-byte (bpb) on The Pile (Gao et al., 2020) of _Chinchilla_ , _Gopher_ , and Jurassic-1. _Chinchilla_ outperforms _Gopher_ on all subsets. Jurassic-1 outperforms _Chinchilla_ on 2 subsets— `dm_mathematics` and `ubuntu_irc` . 

29 

|Subset|_Chinchilla_(70B)|_Gopher_(280B)|Jurassic-1 (170B)|
|---|---|---|---|
|pile_cc|**0.667**|0.691|0.669|
|pubmed_abstracts|**0.559**|0.578|0.587|
|stackexchange|**0.614**|0.641|0.655|
|github|**0.337**|0.377|0.358|
|openwebtext2|**0.647**|0.677|-|
|arxiv|**0.627**|0.662|0.680|
|uspto_backgrounds|**0.526**|0.546|0.537|
|freelaw|**0.476**|0.513|0.514|
|pubmed_central|**0.504**|0.525|0.579|
|dm_mathematics|1.111|1.142|**1.037**|
|hackernews|**0.859**|0.890|0.869|
|nih_exporter|**0.572**|0.590|0.590|
|opensubtitles|**0.871**|0.900|0.879|
|europarl|**0.833**|0.938|-|
|books3|**0.675**|0.712|0.835|
|philpapers|**0.656**|0.695|0.742|
|gutenberg_pg_19|**0.548**|0.656|0.890|
|bookcorpus2|**0.714**|0.741|-|
|ubuntu_irc|1.026|1.090|**0.857**|

---

[referencia=46fd66187ec3e6ae score=0.798]
|human_aging|77.6|66.4|human_sexuality|86.3|67.2|
|international_law|90.9|77.7|jurisprudence|79.6|71.3|
|logical_fallacies|80.4|72.4|machine_learning|41.1|41.1|
|management|82.5|77.7|marketing|89.7|83.3|
|medical_genetics|69.0|69.0|miscellaneous|84.5|75.7|
|moral_disputes|77.5|66.8|moral_scenarios|36.5|40.2|
|nutrition|77.1|69.9|philosophy|79.4|68.8|
|prehistory|81.2|67.6|professional_accounting|52.1|44.3|
|professional_law|56.5|44.5|professional_medicine|75.4|64.0|
|professional_psychology|75.7|68.1|public_relations|73.6|71.8|
|security_studies|75.9|64.9|sociology|91.0|84.1|
|us_foreign_policy<br>|92.0|81.0|virology|53.6|47.0|
|world_religions|87.7|84.2||||



Table A6 | **_Chinchilla_ MMLU results.** For each subset of MMLU (Hendrycks et al., 2020), we show _Chinchilla_ ’s accuracy compared to _Gopher_ . 

||**Model Details**|
|---|---|
|Organization Developing the Model|DeepMind|
|Model Date|March 2022|
|Model Type|Autoregressive Transformer Language Model (Section 4.1for<br>details)|
|Feedback on the Model|`{jordanhoffmann, sborgeaud,`<br>`amensch,sifre}@deepmind.com`|
||**Intended Uses**|
|Primary Intended Uses|The primary use is research on language models, including:<br>research on the scaling behaviour of language models along<br>with those listed inRae et al.(2021).|



31

---

[referencia=46fd66187ec3e6ae score=0.742]
#### **Evaluation Data** 

32 

#### Datasets 

- Language modelling on LAMBADA, Wikitext103 (Merity et al., 2017), C4 (Raffel et al., 2020a), PG-19 (Rae et al., 2020) and the Pile (Gao et al., 2020). 

- Language understanding, real world knowledge, mathematical and logical reasoning on the Massive Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) and on the “Beyond the Imitation Game Benchmark” (BIG-bench) (BIG-bench collaboration, 2021). 

- Question answering (closed book) on Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017). 

- Reading comprehension on RACE (Lai et al., 2017) 

||• Common sense understanding on HellaSwag (Zellers<br>et al., 2019),<br>PIQA (Bisk et al., 2020),<br>Wino-<br>grande (Sakaguchi et al.,2020), SIQA (Sap et al.,2019),<br>BoolQ (Clark et al.,2019), and TruthfulQA (Lin et al.,<br>2021).|
|---|---|
|Motivation|We chose evaluations fromRae et al.(2021) to allow us to<br>most directly compare to_Gopher_.|
|Preprocessing|Input text is tokenized using a SentencePiece tokenizer with<br>a vocabulary of size 32,000. Unlike the tokenizer used for<br>_Gopher_, the tokenizer used for_Chinchilla_does not perform<br>NFKC normalization.|



#### **Training Data** 

The same dataset is used as in Rae et al. (2021). Differences in sampling are shown in Table A1.