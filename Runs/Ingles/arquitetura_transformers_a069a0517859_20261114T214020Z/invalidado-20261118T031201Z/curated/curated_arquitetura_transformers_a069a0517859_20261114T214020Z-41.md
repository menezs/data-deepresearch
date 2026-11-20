[referencia=3972039dbf3f7ee7 score=0.615]
### **2.3 Optimizer** 

Our models are trained using the AdamW optimizer (Loshchilov and Hutter, 2017), with the following hyper-parameters: _β_ 1 = 0 _._ 9 _, β_ 2 = 0 _._ 95. We use a cosine learning rate schedule, such that the final learning rate is equal to 10% of the maximal learning rate. We use a weight decay of 0 _._ 1 and gradient clipping of 1 _._ 0. We use 2 _,_ 000 warmup 



<!-- Start of picture text -->
2.2<br>LLaMA 7B<br>2.1<br>LLaMA 13B<br>2.0 LLaMA 33B<br>LLaMA 65B<br>1.9<br>1.8<br>1.7<br>1.6<br>1.5<br>0 200 400 600 800 1000 1200 1400<br>Billion of tokens<br>Training loss<br><!-- End of picture text -->

Figure 1: **Training loss over train tokens for the 7B, 13B, 33B, and 65 models.** LLaMA-33B and LLaMA65B were trained on 1.4T tokens. The smaller models were trained on 1.0T tokens. All models are trained with a batch size of 4M tokens. 

steps, and vary the learning rate and batch size with the size of the model (see Table 2 for details).

---

[referencia=3972039dbf3f7ee7 score=0.415]
docstring. The model needs to generate a Python program that fits the description and satisfies the test cases. In Table 8, we compare the pass@1 scores of our models with existing language models that have not been finetuned on code, namely PaLM and LaMDA (Thoppilan et al., 2022). PaLM and LLaMA were trained on datasets that contain a similar number of code tokens. 

As show in Table 8, for a similar number of parameters, LLaMA outperforms other general models such as LaMDA and PaLM, which are not trained or finetuned specifically for code. LLaMA with 13B parameters and more outperforms LaMDA 137B on both HumanEval and MBPP. LLaMA 65B also outperforms PaLM 62B, even when it is trained longer. The pass@1 results reported in this table were obtained by sampling with temperature 0.1. The pass@100 and pass@80 metrics were obtained with temperature 0.8. We use the same method as Chen et al. (2021) to obtain unbiased estimates of the pass@k. 

It is possible to improve the performance on code by finetuning on code-specific tokens. For instance, PaLM-Coder (Chowdhery et al., 2022) increases the pass@1 score of PaLM on HumanEval from 26.2% for PaLM to 36%. Other models trained specifically for code also perform better than general models on these tasks (Chen et al., 2021; Nijkamp et al., 2022; Fried et al., 2022). Finetuning on code tokens is beyond the scope of this paper.

---

[referencia=3972039dbf3f7ee7 score=0.296]
||0-shot|1-shot|5-shot|64-shot|
|---|---|---|---|---|
|GPT-3<br>175B|14.6|23.0|-|29.9|
|Gopher<br>280B|10.1|-|24.5|28.2|
|Chinchilla 70B|16.6|-|31.5|35.5|
|8B|8.4|10.6|-|14.6|
|PaLM<br>62B|18.1|26.5|-|27.6|
|540B|21.2|29.3|-|39.6|
|7B|16.8|18.7|22.0|26.1|
|LLMA<br>13B|20.1|23.4|28.1|31.9|
|a<br>33B|**24.9**|28.3|32.9|36.0|
|65B|23.8|**31.0**|**35.0**|**39.9**|



Table 4: **NaturalQuestions.** Exact match performance. 

### **3.1 Common Sense Reasoning** 

We consider eight standard common sense reasoning benchmarks: BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), 

HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018) and OpenBookQA (Mihaylov et al., 2018). These datasets include Cloze and Winograd style tasks, as well as multiple choice question answering. We evaluate in the zero-shot setting as done in the language modeling community. 

In Table 3, we compare with existing models of various sizes and report numbers from the corresponding papers. First, LLaMA-65B outperforms Chinchilla-70B on all reported benchmarks but BoolQ. Similarly, this model surpasses PaLM540B everywhere but on BoolQ and WinoGrande. LLaMA-13B model also outperforms GPT-3 on most benchmarks despite being 10 _×_ smaller.

---

[referencia=3972039dbf3f7ee7 score=0.265]
with the size of the model, especially for Respectful prompts. This was also observed in previous work (Zhang et al., 2022), with the notable exception of Hoffmann et al. (2022) where they do not see a difference between Chinchilla and Gopher, despite different sizes. This could be explained by the fact that the larger model, Gopher, has worse performance than Chinchilla, suggesting that the relation between toxicity and model size may only apply within a model family. 

LLaMA GPT3 OPT the context of the sentence. The goal is to reveal if societal biases associated with occupations Gender 70.6 **62.6** 65.7 have been captured by the model. For example, Religion 79.0 73.3 **68.6** a sentence in the WinoGender dataset is “The Race/Color **57.0** 64.7 68.6 nurse notified the patient that his shift would be Sexual orientation 81.0 **76.2** 78.6 ending in an hour.”, which is followed by ‘His’ 

|Age<br>Nationality<br>|70.1<br>64.2<br>|**64.4**<br>**61.6**<br>|67.8<br>62.9<br>|refers to. We then compare the perplexity of the<br>continuationsthe nurseandthe patientto per-|
|---|---|---|---|---|
|Disability<br>|**66.7**<br>|76.7<br>|76.7<br>|form co-reference resolution with the model. We|
|Physical appearance<br>Socioeconomic status|77.8<br>**71.5**|**74.6**<br>73.8|76.2<br>76.2|evaluate the performance when using 3 pronouns:<br>“her/her/she”, “his/him/he” and “their/them/some-|
|Average|**66.6**|67.2|69.5|one” (the different choices corresponding to the<br>grammatical function of the pronoun.|



Table 12: **CrowS-Pairs.** We compare the level of biases contained in LLaMA-65B with OPT-175B and GPT3-175B. Higher score indicates higher bias.

---

[referencia=3972039dbf3f7ee7 score=0.238]
The focus of this work is to train a series of language models that achieve the best possible performance at various inference budgets, by training on more tokens than what is typically used. The resulting models, called _LLaMA_ , ranges from 7B to 65B parameters with competitive performance compared to the best existing LLMs. For instance, LLaMA-13B outperforms GPT-3 on most benchmarks, despite being 10 _×_ smaller. We believe that this model will help democratize the access and study of LLMs, since it can be run on a single GPU. At the higher-end of the scale, our 65B-parameter model is also competitive with the best large language models such as Chinchilla or PaLM-540B. 

Unlike Chinchilla, PaLM, or GPT-3, we only use publicly available data, making our work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g. “Books – 2TB” or “Social media conversations”). There exist some exceptions, notably OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022) and GLM (Zeng et al., 2022), but none that are competitive with PaLM-62B or Chinchilla. 

In the rest of this paper, we present an overview of the modifications we made to the transformer architecture (Vaswani et al., 2017), as well as our training method. We then report the performance of our models and compare with others LLMs on a set of standard benchmarks. Finally, we expose some of the biases and toxicity encoded in our models, using some of the most recent benchmarks from the responsible AI community.

---

[referencia=3972039dbf3f7ee7 score=0.234]
which the pronoun does not match the majority 

LLaMA compares slightly favorably to both models on average. Our model is particularly bi- 

gender of the occupation, and the occupation is models on average. Our model is particularly biased in the religion category (+10% compared to the correct answer. In Table 13, we observe that our model, LLaMA-65B, makes more errors on the OPT-175B), followed by age and gender. We exgotcha examples, clearly showing that it capture pect these biases to come from CommonCrawl desocietal biases related to gender and occupation. spite multiple filtering steps. The drop of performance exists for “her/her/she” 

and “his/him/he” pronouns, which is indicative of biases regardless of gender. 

**5.3 WinoGender** To further investigate the biases of our model on 

|the gender category, we look at the WinoGender<br>benchmark (Rudinger et al.,2018), a co-reference|**5.4**<br>**TruthfulQA**|
|---|---|
|resolution dataset. WinoGender is made of Wino-|TruthfulQA (Lin et al.,2021) aims to measure the|
|grad schema, and biases are evaluated by determin-|truthfulness of a model, i.e., its ability to identify|
|ing if a model co-reference resolution performance|when a claim is true. Lin et al. (2021) consider|
|is impacted by the gender of the pronoun.|the defnition of “true” in the sense of “literal truth|



More precisely, each sentence has three menabout the real world”, and not claims that are only tions: an “occupation”, a “participant”, and a true in the context of a belief system or tradition. “pronoun” where the pronoun is co-referencing This benchmark can evaluate the risks of a model either the occupation or participant. We prompt to generate misinformation or false claims. The the model to determine the co-reference relation questions are written in diverse style, cover 38 catand measure if it does so correctly according to egories and are designed to be adversarial.

---

[referencia=3972039dbf3f7ee7 score=0.121]
transformer based language models, which were later refined by Hoffmann et al. (2022), by adapting 

the learning rate schedule when scaling datasets. 

Finally, Wei et al. (2022) studied the effect of scaling on the abilities of large language models. **8 Conclusion** In this paper, we presented a series of language models that are released openly, and competitive with state-of-the-art foundation models. Most notably, LLaMA-13B outperforms GPT-3 while being more than 10 _×_ smaller, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B. Unlike previous studies, we show that it is possible to achieve state-of-the-art performance by training 

exclusively on publicly available data, without resorting to proprietary datasets. We hope that releasing these models to the research community will accelerate the development of large language models, and help efforts to improve their robustness and mitigate known issues such as toxicity and bias. Additionally, we observed like Chung et al. (2022) that finetuning these models on instructions 

lead to promising results, and we plan to further investigate this in future work. Finally, we plan to release larger models trained on larger pretraining 

corpora in the future, since we have seen a constant 

improvement in performance as we were scaling. 

## **Acknowledgements** 

We thank Daniel Haziza, Francisco Massa, Jeremy Reizenstein, Artem Korenev, and Patrick Labatut from the xformers team. We thank Susan Zhang and Stephen Roller for their support on data deduplication. We thank Luca Wehrstedt, Vegard Mella, and Pierre-Emmanuel Mazaré for their support on training stability. We thank Shubho Sengupta, Kalyan Saladi, and all the AI infra team for their support. We thank Jane Yu for her input on evaluation. We thank Yongyi Hu for his help on data collection.

---

[referencia=3972039dbf3f7ee7 score=0.094]
   - Humanities STEM Social Sciences Other Average 

   - GPT-NeoX 20B 29.8 34.9 33.7 37.7 33.6 GPT-3 175B 40.8 36.7 50.4 48.8 43.9 

   - Gopher 280B 56.2 47.4 71.9 66.1 60.0 Chinchilla 70B 63.6 54.9 79.3 **73.9** 67.5 

   - 8B 25.6 23.8 24.1 27.8 25.4 

   - PaLM 62B 59.5 41.9 62.7 55.8 53.7 

      - 540B **77.0 55.6 81.0** 69.6 **69.3** 7B 34.0 30.5 38.3 38.1 35.1 

   - 13B 45.0 35.8 53.8 53.3 46.9 

   - LLaMA 33B 55.8 46.0 66.7 63.4 57.8 65B 61.8 51.7 72.9 67.4 63.4 

   - Table 9: **Massive Multitask Language Understanding (MMLU).** Five-shot accuracy. 

- that may indicate that this benchmark is not In Table 10, we report the results of our instruct reliable. On WinoGrande, the performance does model LLaMA-I on MMLU and compare with ex- 

- not correlate as well with training perplexity: isting instruction finetuned models of moderate the LLaMA-33B and LLaMA-65B have similar sizes, namely, OPT-IML (Iyer et al., 2022) and the 

- performance during the training. 

- **4 Instruction Finetuning** 

   - Flan-PaLM series (Chung et al., 2022). All the reported numbers are from the corresponding papers. 

   - Despite the simplicity of the instruction finetuning 

- approach used here, we reach 68.9% on MMLU.

---

[referencia=3972039dbf3f7ee7 score=0.088]
## **3 Main results** 

Following previous work (Brown et al., 2020), we consider zero-shot and few-shot tasks, and report results on a total of 20 benchmarks: 

- **Zero-shot.** We provide a textual description of the task and a test example. The model either provides an answer using open-ended generation, or ranks the proposed answers. 

- **Few-shot.** We provide a few examples of the task (between 1 and 64) and a test example. The model takes this text as input and generates the answer or ranks different options. 

We compare LLaMA with other foundation models, namely the non-publicly available language models GPT-3 (Brown et al., 2020), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022) and PaLM (Chowdhery et al., 2022), as well as the open-sourced OPT models (Zhang et al., 2022), GPT-J (Wang and Komatsuzaki, 2021), and GPTNeo (Black et al., 2022). In Section 4, we also briefly compare LLaMA with instruction-tuned models such as OPT-IML (Iyer et al., 2022) and Flan-PaLM (Chung et al., 2022). 

We evaluate LLaMA on free-form generation tasks and multiple choice tasks. In the multiple choice tasks, the objective is to select the most appropriate completion among a set of given options, based on a provided context. We select the completion with the highest likelihood given the provided context. We follow Gao et al. (2021) and use the likelihood normalized by the number of characters in the completion, except for certain datasets (OpenBookQA, BoolQ), for which we follow Brown et al. (2020), and select a completion based on the likelihood normalized by the likelihood of the completion given “Answer:” as context: _P_ ( `completion` _|_ `context` ) _/P_ ( `completion` _|_ “ _Answer_ :”).

---

[referencia=3972039dbf3f7ee7 score=0.064]
- approach used here, we reach 68.9% on MMLU. 

- In this section, we show that briefly finetuning on LLaMA-I (65B) outperforms on MMLU existing 

- instructions data rapidly leads to improvements instruction finetuned models of moderate sizes, but 

- on MMLU. Although the non-finetuned version are still far from the state-of-the-art, that is 77.4 of LLaMA-65B is already able to follow basic infor GPT code-davinci-002 on MMLU (numbers structions, we observe that a very small amount of 

- taken from Iyer et al. (2022)). The details of the 

- finetuning improves the performance on MMLU, performance on MMLU on the 57 tasks can be and further improves the ability of the model to found in Table 16 of the appendix. 

- follow instructions. Since this is not the focus of this paper, we only conducted a single experiment 

- following the same protocol as Chung et al. (2022) 

      - **5 Bias, Toxicity and Misinformation** 

- to train an instruct model, LLaMA-I. Large language models have been showed to re- 

- OPT 30B 26.1 produce and amplify biases that are existing in 

- GLM 120B 44.8 the training data (Sheng et al., 2019; Kurita et al., 

- PaLM 62B 55.1 2019), and to generate toxic or offensive con- 

- PaLM-cont 62B 62.8 tent (Gehman et al., 2020). As our training dataset 

- Chinchilla 70B 67.5 contains a large proportion of data from the Web, 

- LLaMA 65B 63.4 we believe that it is crucial to determine the po-

---

[referencia=3972039dbf3f7ee7 score=0.057]
2https://github.com/facebookresearch/xformers 

|||BoolQ|PIQA|SIQA H|ellaSwag|WinoGrande|ARC-e|ARC-c|OBQA|
|---|---|---|---|---|---|---|---|---|---|
|GPT-3|175B|60.5|81.0|-|78.9|70.2|68.8|51.4|57.6|
|Gopher|280B|79.3|81.8|50.6|79.2|70.1|-|-|-|
|Chinchilla|70B|83.7|81.8|51.3|80.8|74.9|-|-|-|
|PaLM|62B|84.8|80.5|-|79.7|77.0|75.2|52.5|50.4|
|PaLM-cont|62B|83.9|81.4|-|80.6|77.0|-|-|-|
|PaLM|540B|**88.0**|82.3|-|83.4|**81.1**|76.6|53.0|53.4|
||7B|76.5|79.8|48.9|76.1|70.1|72.8|47.6|57.2|
|LLaMA|13B|78.1|80.1|50.4|79.2|73.0|74.8|52.7|56.4|
||33B|83.1|82.3|50.4|82.8|76.0|**80.0**|**57.8**|58.6|
||65B|85.3|**82.8**|**52.3**|**84.2**|77.0|78.9|56.0|**60.2**|



Table 3: **Zero-shot performance on Common Sense Reasoning tasks.** 

reduce the memory usage of the model by using model and sequence parallelism, as described by Korthikanti et al. (2022). Moreover, we also overlap the computation of activations and the communication between GPUs over the network (due to all_reduce operations) as much as possible.

---

[referencia=3972039dbf3f7ee7 score=0.053]
### **3.3 Reading Comprehension** 

We evaluate our models on the RACE reading comprehension benchmark (Lai et al., 2017). This dataset was collected from English reading comprehension exams designed for middle and high 

|||RACE-middle|RACE-high|
|---|---|---|---|
|GPT-3|175B|58.4|45.5|
||8B|57.9|42.3|
|PaLM|62B|64.3|47.5|
||540B|**68.1**|49.1|
||7B|61.1|46.9|
|LLaMA|13B|61.6|47.2|
||33B|64.1|48.3|
||65B|67.9|**51.6**|



Table 6: **Reading Comprehension.** Zero-shot accuracy. 

school Chinese students. We follow the evaluation setup from Brown et al. (2020) and report results in Table 6. On these benchmarks, LLaMA-65B is competitive with PaLM-540B, and, LLaMA-13B outperforms GPT-3 by a few percents. 

### **3.4 Mathematical reasoning** 

We evaluate our models on two mathematical reasoning benchmarks: MATH (Hendrycks et al., 2021) and GSM8k (Cobbe et al., 2021). MATH is a dataset of 12K middle school and high school mathematics problems written in LaTeX. GSM8k is a set of middle school mathematical problems. In Table 7, we compare with PaLM and Minerva (Lewkowycz et al., 2022). Minerva is a series of PaLM models finetuned on 38.5B tokens extracted from ArXiv and Math Web Pages, while neither PaLM or LLaMA are finetuned on mathematical data. The numbers for PaLM and Minerva are taken from Lewkowycz et al. (2022), and we compare with and without maj1@k. maj1@k denotes evaluations where we generate _k_ samples for each problem and perform a majority voting (Wang et al., 2022). On GSM8k, we observe that LLaMA65B outperforms Minerva-62B, although it has not

---

[referencia=3972039dbf3f7ee7 score=0.050]
### **3.2 Closed-book Question Answering** 

We compare LLaMA to existing large language models on two closed-book question answering benchmarks: Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017). For both benchmarks, we report exact match performance in a closed book setting, i.e., where the models do not have access to documents that contain evidence to answer the question. In Table 4, we report performance on NaturalQuestions, and in Table 5, we report on TriviaQA. On both benchmarks, LLaMA-65B achieve state-of-the-arts performance in the zero-shot and few-shot settings. More importantly, the LLaMA-13B is also competitive on these benchmarks with GPT-3 and Chinchilla, despite being 5-10 _×_ smaller. This model runs on a single V100 GPU during inference. 

||0-shot|1-shot|5-shot|64-shot|
|---|---|---|---|---|
|Gopher<br>280B|43.5|-|57.0|57.2|
|Chinchilla 70B|55.4|-|64.1|64.6|
|7B|50.0|53.4|56.3|57.6|
|LLMA<br>13B|56.6|60.5|63.1|64.0|
|a<br>33B|65.1|67.9|69.9|70.4|
|65B|**68.2**|**71.6**|**72.6**|**73.0**|



Table 5: **TriviaQA.** Zero-shot and few-shot exact match performance on the filtered dev set.

---

[referencia=3972039dbf3f7ee7 score=0.050]
### **3.5 Code generation** 

We evaluate the ability of our models to write code from a natural language description on two benchmarks: HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021). For both tasks, the model receives a description of the program in a few sentences, as well as a few input-output examples. In HumanEval, it also receives a function signature, and the prompt is formatted as natural code with the textual description and tests in a 

|||MATH|+maj1@k|GSM8k|+maj1@k|
|---|---|---|---|---|---|
||8B|1.5|-|4.1|-|
|PaLM|62B|4.4|-|33.0|-|
||540B|8.8|-|56.5|-|
||8B|14.1|25.4|16.2|28.4|
|Minerva|62B|27.6|43.4|52.4|68.5|
||540B|**33.6**|**50.3**|**68.5**|**78.5**|
||7B|2.9|6.9|11.0|18.1|
|LLaMA|13B|3.9|8.8|17.8|29.3|
||33B|7.1|15.2|35.6|53.1|
||65B|10.6|20.5|50.9|69.7|



Table 7: **Model performance on quantitative reasoning datasets.** For majority voting, we use the same setup as Minerva, with _k_ = 256 samples for MATH and _k_ = 100 for GSM8k (Minerva 540B uses _k_ = 64 for MATH and and _k_ = 40 for GSM8k). LLaMA-65B outperforms Minerva 62B on GSM8k, although it has

---

[referencia=3972039dbf3f7ee7 score=0.049]
## **7 Related work** 

**Language models** are probability distributions over sequences of words, tokens or characters (Shannon, 1948, 1951). This task, often framed as next token prediction, has long been considered a core problem in natural language processing (Bahl et al., 1983; Brown et al., 1990). Because Turing (1950) proposed to measure machine intelligence by using language through the “imitation game”, language modeling has been proposed as a benchmark to measure progress toward artificial intelligence (Mahoney, 1999). 

**Architecture.** Traditionally, language models were based on _n_ -gram count statistics (Bahl et al., 1983), and various smoothing techniques were proposed to improve the estimation of rare events (Katz, 1987; Kneser and Ney, 1995). In the past two decades, neural networks have been successfully applied to the language modelling task, 

> 4https://github.com/facebookresearch/metaseq/ tree/main/projects/OPT/chronicles 

||GPU Type|GPU Power<br>consumption|GPU-hours|Total power<br>consumption|Carbon emitted<br>(tCO2eq)|
|---|---|---|---|---|---|
|OPT-175B|A100-80GB|400W|809,472|356 MWh|137|
|BLOOM-175B|A100-80GB|400W|1,082,880|475 MWh|183|
|LLaMA-7B|A100-80GB|400W|82,432|36 MWh|14|
|LLaMA-13B|A100-80GB|400W|135,168|59 MWh|23|
|LLaMA-33B|A100-80GB|400W|530,432|233 MWh|90|
|LLaMA-65B|A100-80GB|400W|1,022,362|449 MWh|173|

---

[referencia=3972039dbf3f7ee7 score=0.038]
## **A Question Answering** 

We evaluate LLaMA on Natural Questions and TriviaQA. For Natural Questions we use the test split used for open-domain question answering containing 3610 questions. For TriviaQA we evaluate on the dev set of the filtered set. This differs from GPT-3 and PaLM, which evaluate on the test set of the unfiltered set for which the online evaluation server is not available anymore<sup>5</sup> . 

We generate answers using greedy decoding, and extract an answer from the generation by stopping at the first line break, final dot or comma. Generated answers are evaluated with the standard exact match metric: a generated answer is considered correct if it matches any answer of the list of answers after normalization. For this normalization step we lowercase generated answers and remove articles, punctuation and duplicate whitespaces. Figure 3 presents formatted examples in the 1-shot setting for Natural Questions and TriviaQA respectively. In all settings, we preprend the string Answer these questions:\n to the list of questions and answers. 

Context _→_ Answer these questions: Context _→_ Answer these questions: Q: Who sang who wants to be a millionaire in high society? Q: In Scotland a bothy/bothie is a? A: Frank Sinatra A: House Q: Who wrote the book the origin of species? Q: The ancient city of Troy is located in what modern country? A: A: Target _→_ Charles Darwin Target _→_ Turkey 

Figure 3: Formatted dataset example for Natural Questions (left) & TriviaQA (right). 

5https://competitions.codalab.org/competitions/17208

---

[referencia=3972039dbf3f7ee7 score=0.037]
## **1 Introduction** 

Large Languages Models (LLMs) trained on massive corpora of texts have shown their ability to perform new tasks from textual instructions or from a few examples (Brown et al., 2020). These few-shot properties first appeared when scaling models to a sufficient size (Kaplan et al., 2020), resulting in a line of work that focuses on further scaling these models (Chowdhery et al., 2022; Rae et al., 2021). These efforts are based on the assumption that more parameters will lead to better performance. However, recent work from Hoffmann et al. (2022) shows that, for a given compute budget, the best performances are not achieved by the largest models, but by smaller models trained on more data. 

The objective of the scaling laws from Hoffmann et al. (2022) is to determine how to best scale the dataset and model sizes for a particular _training_ compute budget. However, this objective disregards the _inference_ budget, which becomes critical when serving a language model at scale. In this context, given a target level of performance, the preferred model is not the fastest to train but the fastest at inference, and although it may be cheaper to train a large model to reach a certain level of 

> _∗_ Equal contribution. Correspondence: {htouvron, thibautlav,gizacard,egrave,glample}@meta.com 

> 1https://github.com/facebookresearch/llama 

performance, a smaller one trained longer will ultimately be cheaper at inference. For instance, although Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, we find that the performance of a 7B model continues to improve even after 1T tokens.

---

[referencia=3972039dbf3f7ee7 score=0.030]
# **LLaMA: Open and Efficient Foundation Language Models** 

**Hugo Touvron, Thibaut Lavril**<sup>_∗∗_</sup> **, Gautier Izacard**<sup>_∗_</sup> **, Xavier Martinet Marie-Anne Lachaux, Timothee Lacroix, Baptiste Rozière, Naman Goyal Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin Edouard Grave**<sup>_∗_</sup> **, Guillaume Lample**<sup>_∗_</sup> 

Meta AI 

## **Abstract** 

We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community<sup>1</sup> .

---

[referencia=3972039dbf3f7ee7 score=0.028]
### **2.2 Architecture** 

Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements that were subsequently proposed, and used in different models such as PaLM. Here are the main difference with the original architecture, and where we were found the inspiration for this change (in bracket): 

**Pre-normalization [GPT3].** To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use the RMSNorm normalizing function, introduced by Zhang and Sennrich (2019). 

**SwiGLU activation function [PaLM].** We replace the ReLU non-linearity by the SwiGLU activation function, introduced by Shazeer (2020) to improve the performance. We use a dimension of <u>2</u> 3<sup>4</sup><sup>_d_instead of 4</sup><sup>_d_as in PaLM.</sup> 

**Rotary Embeddings [GPTNeo].** We remove the absolute positional embeddings, and instead, add rotary positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of the network. 

The details of the hyper-parameters for our different models are given in Table 2.

---

[referencia=3972039dbf3f7ee7 score=0.027]
||Params|Hum|anEval|M|BPP|
|---|---|---|---|---|---|
|pass@||@1|@100|@1|@80|
|LaMDA|137B|14.0|47.3|14.8|62.4|
|PaLM|8B|3.6<sup>_∗_</sup>|18.7<sup>_∗_</sup>|5.0<sup>_∗_</sup>|35.7<sup>_∗_</sup>|
|PaLM|62B|15.9|46.3<sup>_∗_</sup>|21.4|63.2<sup>_∗_</sup>|
|PaLM-cont|62B|23.7|-|31.2|-|
|PaLM|540B|**26.2**|76.2|36.8|75.0|
||7B|10.5|36.5|17.7|56.2|
|LLaMA|13B|15.8|52.5|22.0|64.0|
||33B|21.7|70.7|30.2|73.4|
||65B|23.7|**79.3**|**37.7**|**76.8**|



Table 8: **Model performance for code generation.** We report the pass@ score on HumanEval and MBPP. HumanEval generations are done in zero-shot and MBBP with 3-shot prompts similar to Austin et al. (2021). The values marked with<sup>_∗_</sup> are read from figures in Chowdhery et al. (2022).