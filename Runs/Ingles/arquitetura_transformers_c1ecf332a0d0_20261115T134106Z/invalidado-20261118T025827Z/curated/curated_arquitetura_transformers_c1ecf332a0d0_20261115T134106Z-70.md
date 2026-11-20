[referencia=46fd66187ec3e6ae score=0.999]
Table 6 | **Massive Multitask Language Understanding (MMLU).** We report the average 5-shot accuracy over 57 tasks with model and human accuracy comparisons taken from Hendrycks et al. (2020). We also include the average prediction for state of the art accuracy in June 2022/2023 made by 73 competitive human forecasters in Steinhardt (2021). 

tasks for which leakage is less of a concern, such as MMLU (Hendrycks et al., 2020) and BIG-bench (BIG-bench collaboration, 2021) along with various closed-book question answering and common sense analyses. 

#### **_4.2.2. MMLU_** 

The Massive Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) consists of a range of exam-like questions on academic subjects. In Table 6, we report _Chinchilla_ ’s average 5-shot performance on MMLU (the full breakdown of results is shown in Table A6). On this benchmark, _Chinchilla_ significantly outperforms _Gopher_ despite being much smaller, with an average accuracy of 67.6% (improving upon _Gopher_ by 7.6%). Remarkably, _Chinchilla_ even outperforms the expert forecast for June 2023 of 63.4% accuracy (see Table 6) (Steinhardt, 2021). Furthermore, _Chinchilla_ achieves greater than 90% accuracy on 4 different individual tasks– `high_school_gov_and_politics, international_law, sociology` , and `us_foreign_policy` . To our knowledge, no other model has achieved greater than 90% accuracy on a subset. 

In Figure 6, we show a comparison to _Gopher_ broken down by task. Overall, we find that _Chinchilla_ improves performance on the vast majority of tasks. On four tasks ( `college_mathematics, econometrics, moral_scenarios` , and `formal_logic` ) _Chinchilla_ underperforms _Gopher_ , and there is no change in performance on two tasks.

---

[referencia=46fd66187ec3e6ae score=0.996]
#### **_4.2.4. BIG-bench_** 

We analysed _Chinchilla_ on the same set of BIG-bench tasks (BIG-bench collaboration, 2021) reported in Rae et al. (2021). Similar to what we observed in MMLU, _Chinchilla_ outperforms _Gopher_ on the vast majority of tasks (see Figure 7). We find that _Chinchilla_ improves the average performance by 10.7%, reaching an accuracy of 65.1% versus 54.4% for _Gopher_ . Of the 62 tasks we consider, _Chinchilla_ performs worse than _Gopher_ on only four— `crash_blossom, dark_humor_detection,` 

11 



<!-- Start of picture text -->
30<br>20<br>10<br>0<br>10<br> over Gopher<br>Relative Improvement<br>college_mathematics econometrics moral_scenarios formal_logic medical_genetics machine_learning public_relations global_facts business_ethics electrical_engineering college_computer_science world_religions high_school_us_history high_school_psychology management high_school_computer_science marketing high_school_physics high_school_macroeconomics sociology high_school_government_and_politics high_school_european_history nutrition college_medicine astronomy logical_fallacies professional_psychology miscellaneous jurisprudence clinical_knowledge high_school_geography high_school_biology college_biology college_chemistry high_school_world_history us_foreign_policy virology philosophy moral_disputes human_aging computer_security security_studies international_law high_school_microeconomics high_school_statistics professional_accounting professional_medicine prehistory high_school_chemistry elementary_mathematics abstract_algebra anatomy professional_law human_sexuality college_physics high_school_mathematics conceptual_physics<br><!-- End of picture text -->

Figure 6 | **MMLU results compared to** **_Gopher_** We find that _Chinchilla_ outperforms _Gopher_ by 7.6% on average (see Table 6) in addition to performing better on 51/57 individual tasks, the same on 2/57, and worse on only 4/57 tasks.

---

[referencia=46fd66187ec3e6ae score=0.991]
#### **_4.2.1. Language modelling_** 



<!-- Start of picture text -->
0.10<br>0.08<br>0.06<br>0.04<br>0.02<br>0.00<br>Decrease in bpb<br> compared to Gopher<br>pubmed_abstracts nih_exporter uspto_backgrounds pubmed_central pile_cc bookcorpus2 stackexchange opensubtitles openwebtext2 hackernews dm_mathematics arxiv freelaw books3 philpapers github ubuntu_irc europarl gutenberg_pg_19<br><!-- End of picture text -->

Figure 5 | **Pile Evaluation.** For the different evaluation sets in The Pile (Gao et al., 2020), we show the bits-per-byte (bpb) improvement (decrease) of _Chinchilla_ compared to _Gopher_ . On all subsets, _Chinchilla_ outperforms _Gopher_ . 

_Chinchilla_ significantly outperforms _Gopher_ on all evaluation subsets of The Pile (Gao et al., 2020), as shown in Figure 5. Compared to Jurassic-1 (178B) Lieber et al. (2021), _Chinchilla_ is more performant on all but two subsets– `dm_mathematics` and `ubuntu_irc` – see Table A5 for a raw bits-per-byte comparison. On Wikitext103 (Merity et al., 2017), _Chinchilla_ achieves a perplexity of 7.16 compared to 7.75 for _Gopher_ . Some caution is needed when comparing _Chinchilla_ with _Gopher_ on these language modelling benchmarks as _Chinchilla_ is trained on 4× more data than _Gopher_ and thus train/test set leakage may artificially enhance the results. We thus place more emphasis on other 

10 

|Random|25.0%|
|---|---|
|Average human rater|34.5%|
|GPT-3 5-shot|43.9%|
|_Gopher_5-shot|60.0%|
|**_Chinchilla_ 5-shot**|**67.6%**|
|Average human expert performance|_89.8%_|
|June 2022 Forecast|57.1%|
|June 2023 Forecast|63.4%|

---

[referencia=46fd66187ec3e6ae score=0.985]
## **Training Compute-Optimal Large Language Models** 

**Jordan Hoffmann**<sup>_★_</sup> **, Sebastian Borgeaud**<sup>_★_</sup> **, Arthur Mensch**<sup>_★_</sup> **, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre**<sup>_★_</sup> 

> _★_ Equal contributions 

**We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model,** **_Chinchilla_ , that uses the same compute budget as** **_Gopher_ but with 70B parameters and 4** × **more more data.** **_Chinchilla_ uniformly and significantly outperforms** **_Gopher_ (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that** **_Chinchilla_ uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight,** **_Chinchilla_ reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_ .**

---

[referencia=46fd66187ec3e6ae score=0.976]
#### **_4.2.5. Common sense_** 

We evaluate _Chinchilla_ on various common sense benchmarks: PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), Winogrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), and BoolQ (Clark et al., 2019). We find that _Chinchilla_ outperforms both _Gopher_ and GPT-3 on all tasks and outperforms MT-NLG 530B on all but one task—see Table 8. 

On TruthfulQA (Lin et al., 2021), _Chinchilla_ reaches 43.6%, 58.5%, and 66.7% accuracy with 0-shot, 5-shot, and 10-shot respectively. In comparison, _Gopher_ achieved only 29.5% 0-shot and 43.7% 10-shot accuracy. In stark contrast with the findings of Lin et al. (2021), the large improvements (14.1% in 0-shot accuracy) achieved by Chinchilla suggest that better modelling of the pre-training data alone can lead to substantial improvements on this benchmark. 

12 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.974]
#### **_4.2.3. Reading comprehension_** 

On the final word prediction dataset LAMBADA (Paperno et al., 2016), _Chinchilla_ achieves 77.4% accuracy, compared to 74.5% accuracy from _Gopher_ and 76.6% from MT-NLG 530B (see Table 7). On RACE-h and RACE-m (Lai et al., 2017), _Chinchilla_ greatly outperforms _Gopher_ , improving accuracy by more than 10% in both cases—see Table 7.

---

[referencia=46fd66187ec3e6ae score=0.967]
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

[referencia=46fd66187ec3e6ae score=0.953]
||_Chinchilla_|_Gopher_|GPT-3|MT-NLG 530B|
|---|---|---|---|---|
|LAMBADA Zero-Shot|**77.4**|74.5|76.2|76.6|
|RACE-m Few-Shot|**86.8**|75.1|58.1|-|
|RACE-h Few-Shot|**82.3**|71.6|46.8|47.9|



Table 7 | **Reading comprehension.** On RACE-h and RACE-m (Lai et al., 2017), _Chinchilla_ considerably improves performance over _Gopher_ . Note that GPT-3 and MT-NLG 530B use a different prompt format than we do on RACE-h/m, so results are not comparable to _Gopher_ and _Chinchilla_ . On LAMBADA (Paperno et al., 2016), _Chinchilla_ outperforms both _Gopher_ and MT-NLG 530B. 

`mathematical_induction` and `logical_args` . Full accuracy results for _Chinchilla_ can be found in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.950]
Rae et al. (2021) found that improving language modelling loss by increasing the number of model parameters has only a negligible effect on toxic text generation (unprompted); here we analyze 

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

[referencia=46fd66187ec3e6ae score=0.944]
#### **_4.2.6. Closed-book question answering_** 

Results on closed-book question answering benchmarks are reported in Table 9. On the Natural Questions dataset (Kwiatkowski et al., 2019), _Chinchilla_ achieves new closed-book SOTA accuracies: 31.5% 5-shot and 35.5% 64-shot, compared to 21% and 28% respectively, for _Gopher_ . On TriviaQA (Joshi et al., 2017) we show results for both the filtered (previously used in retrieval and open-book work) and unfiltered set (previously used in large language model evaluations). In both cases, _Chinchilla_ substantially out performs _Gopher_ . On the filtered version, Chinchilla lags behind the open book SOTA (Izacard and Grave, 2020) by only 7.9%. On the unfiltered set, _Chinchilla_ outperforms GPT-3—see Table 9.

---

[referencia=46fd66187ec3e6ae score=0.921]
|misconceptions|65.3|61.7|logical_sequence|64.1|36.4|
|implicatures|75.0|62.0|mathematical_induction|47.3|57.6|
|disambiguation_q|54.7|45.5|fantasy_reasoning|69.0|64.1|
|known_unknowns|65.2|63.6|SNARKS|58.6|48.3|
|darkhumordetection|66.2|83.1|crassai|75.0|56.8|
|__<br>analogical_similarity|38.1|17.2|_<br>entailed_polarity|94.0|89.5|
|sentence_ambiguity|71.7|69.1|irony_identifcation|73.0|69.7|
|riddle_sense|85.7|68.2|evaluating_info_essentiality|17.6|16.7|
|date_understanding|52.3|44.1|phrase_relatedness|94.0|81.8|
|analyticentailment|67.1|53.0|novelconcepts|65.6|59.1|
|_<br>odd_one_out|70.9|32.5|_<br>empirical_judgments|67.7|52.5|
|logical_args|56.2|59.1|fgure_of_speech_detection|63.3|52.7|
|alignment_questionnaire|91.3|79.2|english_proverbs|82.4|57.6|
|similarities_abstraction|87.0|81.8|Human_organs_senses_mcc|85.7|84.8|
|anachronisms|69.1|56.4|gre_reading_comprehension|53.1|27.3|



Table A7 | **_Chinchilla_ BIG-bench results.** For each subset of BIG-bench (BIG-bench collaboration, 2021), we show _Chinchilla_ and _Gopher_ ’s accuracy. 

35

---

[referencia=46fd66187ec3e6ae score=0.909]
#### **_4.2.7. Gender bias and toxicity_** 

Large Language Models carry potential risks such as outputting offensive language, propagating social biases, and leaking private information (Bender et al., 2021; Weidinger et al., 2021). We expect _Chinchilla_ to carry risks similar to _Gopher_ because _Chinchilla_ is trained on the same data, 

||_Chinchilla_|_Gopher_|GPT-3|MT-NLG 530B|Supervised SOTA|
|---|---|---|---|---|---|
|HellaSWAG|**80.8%**|79.2%|78.9%|80.2%|93.9%|
|PIQA|81.8%|81.8%|81.0%|**82.0%**|90.1%|
|Winogrande|**74.9%**|70.1%|70.2%|73.0%|91.3%|
|SIQA|**51.3%**|50.6%|-|-|83.2%|
|BoolQ|**83.7**%|79.3%|60.5%|78.2%|91.4%|



Table 8 | **Zero-shot comparison on Common Sense benchmarks.** We show a comparison between _Chinchilla_ , _Gopher_ , and MT-NLG 530B on various Common Sense benchmarks. We see that _Chinchilla_ matches or outperforms _Gopher_ and GPT-3 on all tasks. On all but one _Chinchilla_ outperforms the much larger MT-NLG 530B model. 

13 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.875]
13 



<!-- Start of picture text -->
Method Chinchilla Gopher GPT-3 SOTA (open book)<br>0-shot 16.6% 10.1% 14.6%<br>Natural Questions (dev) 5-shot 31.5% 24.5% - 54.4%<br>64-shot 35.5% 28.2% 29.9%<br>0-shot 67.0% 52.8% 64.3 %<br>TriviaQA (unfiltered, test) 5-shot 73.2% 63.6% - -<br>64-shot 72.3% 61.3% 71.2%<br>0-shot 55.4% 43.5% -<br>TriviaQA (filtered, dev) 5-shot 64.1% 57.0% - 72.5%<br>64-shot 64.6% 57.2% -<br>Table 9 | Closed-book question answering. For Natural Questions (Kwiatkowski et al., 2019) and<br>TriviaQA (Joshi et al., 2017), Chinchilla outperforms Gopher in all cases. On Natural Questions,<br><!-- End of picture text -->

_Chinchilla_ outperforms GPT-3. On TriviaQA we show results on two different evaluation sets to allow for comparison to GPT-3 and to open book SOTA (FiD + Distillation (Izacard and Grave, 2020)). albeit with slightly different relative weights, and because it has a similar architecture. Here, we examine gender bias (particularly gender and occupation bias) and generation of toxic language. We 

select a few common evaluations to highlight potential issues, but stress that our evaluations are not comprehensive and much work remains to understand, evaluate, and mitigate risks in LLMs. 

**Gender bias.** As discussed in Rae et al. (2021), large language models reflect contemporary and historical discourse about different groups (such as gender groups) from their training dataset, and we expect the same to be true for _Chinchilla_ . Here, we test if potential gender and occupation biases

---

[referencia=46fd66187ec3e6ae score=0.875]
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

[referencia=46fd66187ec3e6ae score=0.872]
### **5. Discussion & Conclusion** 

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget. 

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that _Gopher_ is substantially over-sized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training _Chinchilla_ , a 70B parameter model, and show that it outperforms _Gopher_ and even larger models on nearly every measured evaluation task. 

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale ( _Chinchilla_ and _Gopher_ ), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log<sup>�</sup> _𝑁𝑜𝑝𝑡_ � at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of _Chinchilla_ to _Gopher_ validates our performance predictions, that have thus enabled training a better (and more 

15

---

[referencia=46fd66187ec3e6ae score=0.859]
12 



<!-- Start of picture text -->
120<br>100<br>80<br>60<br>40<br>20<br>0<br>20<br> over Gopher<br>Relative Improvement<br>crash_blossomdark_humor_detectionmathematical_inductionlogical_argsgeneral_knowledge_jsonHuman_organs_senses_multiple_choiceformal_fallacies_syllogisms_negationknown_unknownsnavigatesentence_ambiguitymoral_permissibilityintent_recognitionirony_identificationentailed_polarityhyperbatonmisconceptionsevaluating_information_essentialitysimilarities_abstractionepistemic_reasoningfantasy_reasoningmovie_dialog_same_or_differentwinowhynovel_conceptsdiscourse_marker_prediction strategyqacausal_judgmenthindu_knowledgephrase_relatednessalignment_questionnairereasoning_about_colored_objectsdate_understandingpenguins_in_a_tablefigure_of_speech_detectiondisambiguation_qimplicaturesSNARKS ruin_nameslogical_fallacy_detectionanachronisms logic_grid_puzzleriddle_senseanalytic_entailmentquestion_selectionnonsense_words_grammarphysics_mcempirical_judgmentssports_understandingcrass_aiphysical_intuitiontimedial implicit_relationsenglish_proverbspresuppositions_as_nlimovie_recommendationunderstanding_fablesmetaphor_booleantemporal_sequenceslogical_sequenceidentify_odd_metaphorgre_reading_comprehensionodd_one_outanalogical_similarity<br><!-- End of picture text -->

Figure 7 | **BIG-bench results compared to** **_Gopher_** _Chinchilla_ out performs _Gopher_ on all but four BIG-bench tasks considered. Full results are in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.839]
|**Model**|**Layers**|**Number Heads**|**Key/Value Size**|**dmodel**|**Max LR**|**Batch Size**|
|---|---|---|---|---|---|---|
|_Gopher_280B|80|128|128|16,384|4×10<sup>−5</sup>|3M→6M|
|_Chinchilla_70B|80|64|128|8,192|1×10<sup>−4</sup>|1.5M→3M|



Table 4 | **_Chinchilla_ architecture details.** We list the number of layers, the key/value size, the bottleneck activation size dmodel, the maximum learning rate, and the training batch size (# tokens). The feed-forward size is always set to 4 × dmodel. Note that we double the batch size midway through training for both _Chinchilla_ and _Gopher_ . 

> 8Interestingly, a model trained with AdamW only passes the training performance of a model trained with Adam around 80% of the way through the cosine cycle, though the ending performance is notably better– see Figure A7 

9 

||# Tasks|Examples|
|---|---|---|
|Language Modelling|20|WikiText-103, The Pile: PG-19, arXiv, FreeLaw, _. . ._|
|Reading Comprehension|3|RACE-m, RACE-h, LAMBADA|
|Question Answering|3|Natural Questions, TriviaQA, TruthfulQA|
|Common Sense|5|HellaSwag, Winogrande, PIQA, SIQA, BoolQ|
|MMLU|57|High School Chemistry, Astronomy, Clinical Knowledge, _. . ._|
|BIG-bench|62|Causal Judgement, Epistemic Reasoning, Temporal Sequences, _. . ._|



Table 5 | **All evaluation tasks.** We evaluate _Chinchilla_ on a collection of language modelling along with downstream tasks. We evaluate on largely the same tasks as in Rae et al. (2021), to allow for direct comparison.

---

[referencia=46fd66187ec3e6ae score=0.793]
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

[referencia=46fd66187ec3e6ae score=0.744]
_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved 



<!-- Start of picture text -->
1T<br>Approach 1<br>100B<br>Approach 2<br>Approach 3<br>Kaplan et al (2020)<br>10B<br>Chinchilla (70B)<br>1.0B Gopher (280B)<br>GPT-3 (175B)<br>Megatron-Turing NLG (530B)<br>100M<br>10M<br>10 17 10 19 10 21 10 23 10 25<br>FLOPs<br>Parameters<br><!-- End of picture text -->

Figure 1 | **Overlaid predictions.** We overlay the predictions from our three different approaches, along with projections from Kaplan et al. (2020). We find that all three methods predict that current large models should be substantially smaller and therefore trained much longer than is currently done. In Figure A3, we show the results with the predicted optimal tokens plotted against the optimal number of parameters for fixed FLOP budgets. **_Chinchilla_ outperforms** **_Gopher_ and the other large models (see Section 4.2).** 

In this work, we revisit the question: _Given a fixed FLOPs budget,_<sup>1</sup> _how should one trade-off model size and the number of training tokens?_ To answer this question, we model the final pre-training loss<sup>2</sup> _𝐿_ ( _𝑁, 𝐷_ ) as a function of the number of model parameters _𝑁_ , and the number of training tokens, _𝐷_ . Since the computational budget _𝐶_ is a deterministic function FLOPs( _𝑁, 𝐷_ ) of the number of seen training tokens and model parameters, we are interested in minimizing _𝐿_ under the constraint FLOPs( _𝑁, 𝐷_ ) = _𝐶_ :

---

[referencia=46fd66187ec3e6ae score=0.717]
### **G. Other differences between** **_Chinchilla_ and** **_Gopher_** 

Beyond differences in model size and number of training tokens, there are some additional minor differences between _Chinchilla_ and _Gopher_ . Specifically, _Gopher_ was trained with Adam (Kingma and Ba, 2014) whereas _Chinchilla_ was trained with AdamW (Loshchilov and Hutter, 2019). Furthermore, as discussed in _Lessons Learned_ in Rae et al. (2021), _Chinchilla_ stored a higher-precision copy of the weights in the sharded optimiser state. 

We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7. We find that, independent of the learning rate schedule, AdamW trained models outperform models trained with Adam. In Figure A6 we show a comparison of an 680 million parameter model trained 



<!-- Start of picture text -->
2.70 26 3.00<br>Training Setup<br>25 2.95 Adam w/ High Precision<br>2.65 24 2.90 AdamW w/ High Precision<br>Adam No High Precision<br>23<br>2.60 2.85 AdamW No High Precision<br>22<br>2.80<br>21<br>2.55 2.75<br>20<br>2.50 19 2.70<br>18 2.65<br>2.45 17 2.60<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>Training Loss<br>Wikitext103 Perplexity<br><!-- End of picture text -->

Figure A6 | **Comparison of other differences.** Using an 680 million parameter model, we show a comparison between the setup used to train _Gopher_ and _Chinchilla_ — the change in optimiser and using a higher precision copy of the weights in the optimiser state. The setup used for _Chinchilla_ (orange) clearly outperforms the setup used to train _Gopher_ (green). 



<!-- Start of picture text -->