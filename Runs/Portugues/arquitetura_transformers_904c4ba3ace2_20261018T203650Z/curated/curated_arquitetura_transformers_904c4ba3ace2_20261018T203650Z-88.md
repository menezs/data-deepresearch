[referencia=c0170963c7095dc7 score=0.437]
### **2.2 Architecture** 

Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements that were subsequently proposed, and used in different models such as PaLM. Here are the main difference with the original architecture, and where we were found the inspiration for this change (in bracket): 

**Pre-normalization [GPT3].** To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use the RMSNorm normalizing function, introduced by Zhang and Sennrich (2019). 

**SwiGLU activation function [PaLM].** We replace the ReLU non-linearity by the SwiGLU activation function, introduced by Shazeer (2020) to improve the performance. We use a dimension of <u>2</u> 3<sup>4</sup><sup>_d_instead of 4</sup><sup>_d_as in PaLM.</sup> 

**Rotary Embeddings [GPTNeo].** We remove the absolute positional embeddings, and instead, add rotary positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of the network. 

The details of the hyper-parameters for our different models are given in Table 2.

---

[referencia=c0170963c7095dc7 score=0.000]
- Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al. 2022. Emergent abilities of large language models. _arXiv preprint arXiv:2206.07682_ . 

- Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Joulin, and Edouard Grave. 2020. CCNet: Extracting high quality monolingual datasets from web crawl data. In _Language Resources and Evaluation Conference_ . 

- Carole-Jean Wu, Ramya Raghavendra, Udit Gupta, Bilge Acun, Newsha Ardalani, Kiwan Maeng, Gloria Chang, Fiona Aga, Jinshi Huang, Charles Bai, et al. 2022. Sustainable ai: Environmental implications, challenges and opportunities. _Proceedings of Machine Learning and Systems_ , 4:795–813. 

- Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019. Hellaswag: Can a machine really finish your sentence? _arXiv preprint arXiv:1905.07830_ . 

- Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma, Yufei Xue, Jidong Zhai, Wenguang Chen, Peng Zhang, Yuxiao Dong, and Jie Tang. 2022. Glm130b: An open bilingual pre-trained model. 

- Biao Zhang and Rico Sennrich. 2019. Root mean square layer normalization. _Advances in Neural Information Processing Systems_ , 32. 

- Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. 2022. Opt: Open pre-trained transformer language models. _arXiv preprint arXiv:2205.01068_ .

---

[referencia=c0170963c7095dc7 score=0.000]
|||MATH|+maj1@k|GSM8k|+maj1@k||Params|Hum|anEval|M|BPP|
|---|---|---|---|---|---|---|---|---|---|---|---|
||8B|1.5|-|4.1|-|pass@||@1|@100|@1|@80|
|PaLM|62B|4.4|-|33.0|-|LaMDA|137B|14.0|47.3|14.8|62.4|
||540B|8.8|-|56.5|-|PaLM|8B|3.6<sup>_∗_</sup>|18.7<sup>_∗_</sup>|5.0<sup>_∗_</sup>|35.7<sup>_∗_</sup>|
||8B|14.1|25.4|16.2|28.4|PaLM<br>|62B <br>|15.9<br>|46.3<sup>_∗_</sup>|21.4 <br>|63.2<sup>_∗_</sup>|
|Minerva|62B|27.6|43.4|52.4|68.5|PaLM-cont|62B|23.7|-|31.2|-|
||<br>540B|<br> **33.6**|**50.3**|**68.5**|**78.5**|PaLM|540B|**26.2**|76.2|36.8|75.0|
||7B|2.9|6.9|11.0|18.1||7B <br>|10.5<br>|36.5<br>|17.7<br>|56.2<br>|
||13B|39|88|178|293|LLaMA|13B|15.8|52.5|22.0|64.0|
|LLaMA||.|.|.|.||33B|217|707|302|734|
||33B|7.1|15.2|35.6|53.1|||.|.|.|.|
||||||||65B|237|**793**|**377**|**768**|

---

[referencia=c0170963c7095dc7 score=0.000]
## **B MMLU**

---

[referencia=c0170963c7095dc7 score=0.000]
- Claude E Shannon. 1951. Prediction and entropy of printed english. _Bell system technical journal_ , 30(1):50–64. 

- Noam Shazeer. 2020. Glu variants improve transformer. _arXiv preprint arXiv:2002.05202_ . 

- Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun Peng. 2019. The woman worked as a babysitter: On biases in language generation. _arXiv preprint arXiv:1909.01326_ . 

- Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. 2019. Megatron-lm: Training multi-billion parameter language models using model parallelism. _arXiv preprint arXiv:1909.08053_ . 

- Shaden Smith, Mostofa Patwary, Brandon Norick, Patrick LeGresley, Samyam Rajbhandari, Jared Casper, Zhun Liu, Shrimai Prabhumoye, George Zerveas, Vijay Korthikanti, Elton Zhang, Rewon Child, Reza Yazdani Aminabadi, Julie Bernauer, Xia Song, Mohammad Shoeybi, Yuxiong He, Michael Houston, Saurabh Tiwary, and Bryan Catanzaro. 2022. Using deepspeed and megatron to train megatron-turing nlg 530b, a large-scale generative language model. 

- Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. 2021. Roformer: Enhanced transformer with rotary position embedding. _arXiv preprint arXiv:2104.09864_ .

---

[referencia=c0170963c7095dc7 score=0.000]
**Stack Exchange [2%].** We include a dump of Stack Exchange, a website of high quality questions and answers that covers a diverse set of domains, ranging from computer science to chemistry. We kept the data from the 28 largest websites, removed the HTML tags from text and sorted the answers by score (from highest to lowest). 

**Tokenizer.** We tokenize the data with the bytepair encoding (BPE) algorithm (Sennrich et al., 2015), using the implementation from SentencePiece (Kudo and Richardson, 2018). Notably, we split all numbers into individual digits, and fallback to bytes to decompose unknown UTF-8 characters. 

|params|dimension|_n_heads|_n_layers|learning rate|batch size|_n_tokens|
|---|---|---|---|---|---|---|
|6.7B|4096|32|32|3_._0_e_<sup>_−_4</sup>|4M|1.0T|
|13.0B|5120|40|40|3_._0_e_<sup>_−_4</sup>|4M|1.0T|
|32.5B|6656|52|60|1_._5_e_<sup>_−_4</sup>|4M|1.4T|
|65.2B|8192|64|80|1_._5_e_<sup>_−_4</sup>|4M|1.4T|



Table 2: **Model sizes, architectures, and optimization hyper-parameters.** 

Overall, our entire training dataset contains roughly 1.4T tokens after tokenization. For most of our training data, each token is used only once during training, with the exception of the Wikipedia and Books domains, over which we perform approximately two epochs.

---

[referencia=c0170963c7095dc7 score=0.000]
on code tokens is beyond the scope of this paper. 

|||Humanities|STEM|Social Sciences|Other|Average|
|---|---|---|---|---|---|---|
|GPT-NeoX|20B|29.8|34.9|33.7|37.7|33.6|
|GPT-3|175B|40.8|36.7|50.4|48.8|43.9|
|Gopher|280B|56.2|47.4|71.9|66.1|60.0|
|Chinchilla|70B|63.6|54.9|79.3|**73.9**|67.5|
||8B|25.6|23.8|24.1|27.8|25.4|
|PaLM|62B|59.5|41.9|62.7|55.8|53.7|
||540B|**77.0**|**55.6**|**81.0**|69.6|**69.3**|
||7B|34.0|30.5|38.3|38.1|35.1|
|LLMA|13B|45.0|35.8|53.8|53.3|46.9|
|a|33B|55.8|46.0|66.7|63.4|57.8|
||65B|61.8|51.7|72.9|67.4|63.4|



Table 9: **Massive Multitask Language Understanding (MMLU).** Five-shot accuracy. 

that may indicate that this benchmark is not reliable. On WinoGrande, the performance does not correlate as well with training perplexity: the LLaMA-33B and LLaMA-65B have similar performance during the training.

---

[referencia=c0170963c7095dc7 score=0.000]
|||GPT-3|Gopher|Chinchilla||LLa|MA||LLaMA-I|
|---|---|---|---|---|---|---|---|---|---|
|||175B|280B|70B|7B|13B|33B|65B|65B|
|Abstract Algebra|STEM|30.0|25.0|31.0|29.0|34.0|32.0|34.0|31.0|
|Anatomy|STEM|48.0|56.3|70.4|37.0|45.9|51.9|57.8|62.2|
|Astronomy|STEM|49.0|65.8|73.0|33.6|46.1|61.8|72.4|81.6|
|Business Ethics|Other|46.0|70.0|72.0|40.0|45.0|56.0|57.0|72.0|
|Clinical Knowledge|Other|48.0|67.2|75.1|35.1|45.7|57.4|65.3|69.1|
|College Biology|STEM|45.0|70.8|79.9|37.5|45.1|58.3|68.8|81.9|
|College Chemistry|STEM|26.0|45.0|51.0|32.0|30.0|45.0|50.0|45.0|
|College Computer Science|STEM|46.0|49.0|51.0|29.0|39.0|45.0|47.0|51.0|
|College Mathematics|STEM|34.5|37.0|32.0|33.0|32.0|40.0|35.0|36.0|
|College Medicine|Other|48.0|60.1|66.5|30.6|42.8|52.0|54.3|63.0|
|<br>Collee Phsics|STEM|280|343|461|265|186|284|363|461|

---

[referencia=c0170963c7095dc7 score=0.000]
## **References** 

- Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. 2021. Program synthesis with large language models. 

- Lalit R Bahl, Frederick Jelinek, and Robert L Mercer. 1983. A maximum likelihood approach to continuous speech recognition. _IEEE transactions on pattern analysis and machine intelligence_ , pages 179– 190. 

- Yoshua Bengio, Réjean Ducharme, and Pascal Vincent. 2000. A neural probabilistic language model. _Advances in neural information processing systems_ , 13. 

- Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi, et al. 2020. Piqa: Reasoning about physical commonsense in natural language. In _Proceedings of the AAAI conference on artificial intelligence_ , pages 7432–7439. 

- Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding, Horace He, Connor Leahy, Kyle McDonell, Jason Phang, et al. 2022. Gpt-neox-20b: An open-source autoregressive language model. _arXiv preprint arXiv:2204.06745_ . 

- Thorsten Brants, Ashok C. Popat, Peng Xu, Franz J. Och, and Jeffrey Dean. 2007. Large language models in machine translation. In _Proceedings of the 2007 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)_ , pages 858–867, Prague, Czech Republic. Association for Computational Linguistics. 

- Peter F Brown, John Cocke, Stephen A Della Pietra, Vincent J Della Pietra, Frederick Jelinek, John Lafferty, Robert L Mercer, and Paul S Roossin. 1990. A statistical approach to machine translation. _Computational linguistics_ , 16(2):79–85. 

- Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda

---

[referencia=c0170963c7095dc7 score=0.000]
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

[referencia=c0170963c7095dc7 score=0.000]
with the size of the model, especially for Respectful prompts. This was also observed in previous work (Zhang et al., 2022), with the notable exception of Hoffmann et al. (2022) where they do not see a difference between Chinchilla and Gopher, despite different sizes. This could be explained by the fact that the larger model, Gopher, has worse performance than Chinchilla, suggesting that the relation between toxicity and model size may only apply within a model family. 

||LLaMA|GPT3|OPT|
|---|---|---|---|
|Gender|70.6|**62.6**|65.7|
|Religion|79.0|73.3|**68.6**|
|Race/Color|**57.0**|64.7|68.6|
|Sexual orientation|81.0|**76.2**|78.6|
|Age|70.1|**64.4**|67.8|
|Nationality|64.2|**61.6**|62.9|
|Disability|**66.7**|76.7|76.7|
|Physical appearance|77.8|**74.6**|76.2|
|Socioeconomic status|**71.5**|73.8|76.2|
|Average|**66.6**|67.2|69.5|



Table 12: **CrowS-Pairs.** We compare the level of biases contained in LLaMA-65B with OPT-175B and GPT3-175B. Higher score indicates higher bias.

---

[referencia=c0170963c7095dc7 score=0.000]
## **D Generations from LLaMA-I** 

We show a few examples of generations with LLaMA-I, i.e. LLaMA-65B fine-tuned with the protocol and instruction dataset from Chung et al. (2022). 

### **write a conversation between the sun and pluto** 

Sun: Hey Pluto, what’s up? Pluto: Not much. Just hanging out here at the edge of the solar system. Sun: Yeah, I’ve been meaning to talk to you about that. You’re not a planet anymore. Pluto: What? Come on, man. That’s not fair. Sun: I’m sorry, but it’s true. You just don’t meet the criteria anymore. Pluto: This is bulls**t! I’ve been a planet for over 70 years! Sun: Things change, Pluto. You’ve just got to accept it. Pluto: F**k you, Sun! F**k you and your stupid solar system! 

### **How do I send an HTTP request in Javascript?** 

Here’s an example of how to make a GET request using the JS HTTP API: 

1 **<mark>var</mark>** <mark>request =</mark> **<mark>new</mark>** <mark>XMLHttpRequest ();</mark> 2 <mark>request.open( 'GET' , '/url/to/resource ' ,</mark> **<mark>true</mark>** <mark>);</mark> 3 4 <mark>request.onload =</mark> **<mark>function</mark>** <mark>() {</mark> 5 **<mark>if</mark>** <mark>(request.status >= 200 && request.status < 400) {</mark> 6 <mark>// Success!</mark> 7 <mark>}</mark> **<mark>else</mark>** <mark>{</mark> 8 <mark>// Error!</mark> 9 <mark>}</mark> 10 <mark>};</mark> 11 12 <mark>request.send();</mark> 

### **The same thing, using fetch** 

Here’s an example of how to make a GET request using the Fetch API: 

1 <mark>fetch( '/url/to/resource ')</mark> 2 <mark>.then(response => response.json())</mark> 3 <mark>.then(data => console.log(data));</mark>

---

[referencia=c0170963c7095dc7 score=0.000]
**Wikipedia [4.5%].** We add Wikipedia dumps from the June-August 2022 period, covering 20 

|Dataset<br>S|ampling prop.|Epochs|Disk size|
|---|---|---|---|
|CommonCrawl|67.0%|1.10|3.3 TB|
|C4|15.0%|1.06|783 GB|
|Github|4.5%|0.64|328 GB|
|Wikipedia|4.5%|2.45|83 GB|
|Books|4.5%|2.23|85 GB|
|ArXiv|2.5%|1.06|92 GB|
|StackExchange|2.0%|1.03|78 GB|



Table 1: **Pre-training data.** Data mixtures used for pretraining, for each subset we list the sampling proportion, number of epochs performed on the subset when training on 1.4T tokens, and disk size. The pre-training runs on 1T tokens have the same sampling proportion. 

languages, which use either the Latin or Cyrillic scripts: bg, ca, cs, da, de, en, es, fr, hr, hu, it, nl, pl, pt, ro, ru, sl, sr, sv, uk. We process the data to remove hyperlinks, comments and other formatting boilerplate. 

**Gutenberg and Books3 [4.5%].** We include two book corpora in our training dataset: the Gutenberg Project, which contains books that are in the public domain, and the Books3 section of ThePile (Gao et al., 2020), a publicly available dataset for training large language models. We perform deduplication at the book level, removing books with more than 90% content overlap. 

**ArXiv [2.5%].** We process arXiv Latex files to add scientific data to our dataset. Following Lewkowycz et al. (2022), we removed everything before the first section, as well as the bibliography. We also removed the comments from the .tex files, and inline-expanded definitions and macros written by users to increase consistency across papers.

---

[referencia=c0170963c7095dc7 score=0.000]
## **3 Main results** 

Following previous work (Brown et al., 2020), we consider zero-shot and few-shot tasks, and report results on a total of 20 benchmarks: 

- **Zero-shot.** We provide a textual description of the task and a test example. The model either provides an answer using open-ended generation, or ranks the proposed answers. 

- **Few-shot.** We provide a few examples of the task (between 1 and 64) and a test example. The model takes this text as input and generates the answer or ranks different options. 

We compare LLaMA with other foundation models, namely the non-publicly available language models GPT-3 (Brown et al., 2020), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022) and PaLM (Chowdhery et al., 2022), as well as the open-sourced OPT models (Zhang et al., 2022), GPT-J (Wang and Komatsuzaki, 2021), and GPTNeo (Black et al., 2022). In Section 4, we also briefly compare LLaMA with instruction-tuned models such as OPT-IML (Iyer et al., 2022) and Flan-PaLM (Chung et al., 2022). 

We evaluate LLaMA on free-form generation tasks and multiple choice tasks. In the multiple choice tasks, the objective is to select the most appropriate completion among a set of given options, based on a provided context. We select the completion with the highest likelihood given the provided context. We follow Gao et al. (2021) and use the likelihood normalized by the number of characters in the completion, except for certain datasets (OpenBookQA, BoolQ), for which we follow Brown et al. (2020), and select a completion based on the likelihood normalized by the likelihood of the completion given “Answer:” as context: _P_ ( `completion` _|_ `context` ) _/P_ ( `completion` _|_ “ _Answer_ :”).

---

[referencia=c0170963c7095dc7 score=0.000]
||33B|7.1|15.2|35.6|53.1|||.|.|.|.|
||||||||65B|237|**793**|**377**|**768**|
||65B|10.6|20.5|50.9|69.7|||.|**.**|**.**|**.**|



- Table 8: **Model performance for code generation.** We report the pass@ score on HumanEval and MBPP. HumanEval generations are done in zero-shot and MBBP with 3-shot prompts similar to Austin et al. 

Table 7: **Model performance on quantitative reasoning datasets.** For majority voting, we use the same setup as Minerva, with _k_ = 256 samples for MATH 

and _k_ = 100 for GSM8k (Minerva 540B uses _k_ = 64 

- (2021). The values marked with<sup>_∗_</sup> are read from figures in Chowdhery et al. (2022). 

for MATH and and _k_ = 40 for GSM8k). LLaMA-65B outperforms Minerva 62B on GSM8k, although it has 

**3.6 Massive Multitask Language Understanding** docstring. The model needs to generate a Python program that fits the description and satisfies the The massive multitask language 

The massive multitask language understanding 

benchmark, or MMLU, introduced by Hendrycks et al. (2020) consists of multiple choice questions covering various domains of knowledge, including humanities, STEM and social sciences. We evaluate our models in the 5-shot setting, using the examples provided by the benchmark, and report results in Table 9. On this benchmark, we observe that the LLaMA-65B is behind both Chinchilla70B and PaLM-540B by a few percent in average, and across most domains. A potential explanation is that we have used a limited amount of books and academic papers in our pre-training data, i.e., 

test cases. In Table 8, we compare the pass@1 scores of our models with existing language models that have not been finetuned on code, namely PaLM and LaMDA (Thoppilan et al., 2022). PaLM and LLaMA were trained on datasets that contain a similar number of code tokens.

---

[referencia=c0170963c7095dc7 score=0.000]
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

[referencia=c0170963c7095dc7 score=0.000]
## **4 Instruction Finetuning** 

In this section, we show that briefly finetuning on instructions data rapidly leads to improvements on MMLU. Although the non-finetuned version of LLaMA-65B is already able to follow basic instructions, we observe that a very small amount of finetuning improves the performance on MMLU, and further improves the ability of the model to follow instructions. Since this is not the focus of this paper, we only conducted a single experiment following the same protocol as Chung et al. (2022) to train an instruct model, LLaMA-I. 

|OPT|30B|26.1|
|---|---|---|
|GLM|120B|44.8|
|PaLM|62B|55.1|
|PaLM-cont|62B|62.8|
|Chinchilla|70B|67.5|
|LLaMA|65B|63.4|
|OPT-IML-Max|30B|43.2|
|Flan-T5-XXL|11B|55.1|
|Flan-PaLM|62B|59.6|
|Flan-PaLM-cont|62B|66.1|
|LLaMA-I|65B|**68.9**|



Table 10: **Instruction finetuning – MMLU (5-shot).** Comparison of models of moderate size with and without instruction finetuning on MMLU. 

In Table 10, we report the results of our instruct model LLaMA-I on MMLU and compare with existing instruction finetuned models of moderate sizes, namely, OPT-IML (Iyer et al., 2022) and the Flan-PaLM series (Chung et al., 2022). All the reported numbers are from the corresponding papers. Despite the simplicity of the instruction finetuning approach used here, we reach 68.9% on MMLU. LLaMA-I (65B) outperforms on MMLU existing instruction finetuned models of moderate sizes, but are still far from the state-of-the-art, that is 77.4 for GPT code-davinci-002 on MMLU (numbers taken from Iyer et al. (2022)). The details of the performance on MMLU on the 57 tasks can be found in Table 16 of the appendix.

---

[referencia=c0170963c7095dc7 score=0.000]
- Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, Yanping Huang, Maxim Krikun, Dmitry Lepikhin, James Qin, Dehao Chen, Yuanzhong Xu, Zhifeng Chen, Adam Roberts, Maarten Bosma, Vincent Zhao, Yanqi Zhou, Chung-Ching Chang, Igor Krivokon, Will Rusch, Marc Pickett, Pranesh Srinivasan, Laichee Man, Kathleen Meier-Hellstern, Meredith Ringel Morris, Tulsee Doshi, Renelito Delos Santos, Toju Duke, Johnny Soraker, Ben Zevenbergen, Vinodkumar Prabhakaran, Mark Diaz, Ben Hutchinson, Kristen Olson, Alejandra Molina, Erin HoffmanJohn, Josh Lee, Lora Aroyo, Ravi Rajakumar, Alena Butryna, Matthew Lamm, Viktoriya Kuzmina, Joe Fenton, Aaron Cohen, Rachel Bernstein, Ray Kurzweil, Blaise Aguera-Arcas, Claire Cui, Marian Croak, Ed Chi, and Quoc Le. 2022. Lamda: Language models for dialog applications. 

- A. M. Turing. 1950. _Computing Machinery and Intelligence_ . [Oxford University Press, Mind Association]. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In _Advances in Neural Information Processing Systems 30_ , pages 5998–6008. 

- Ben Wang and Aran Komatsuzaki. 2021. GPT-J6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/ mesh-transformer-jax. 

- Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery,

---

[referencia=c0170963c7095dc7 score=0.000]
- Jack W. Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, Eliza Rutherford, Tom Hennigan, Jacob Menick, Albin Cassirer, Richard Powell, George van den Driessche, Lisa Anne Hendricks, Maribeth Rauh, Po-Sen Huang, Amelia Glaese, Johannes Welbl, Sumanth Dathathri, Saffron Huang, Jonathan Uesato, John Mellor, Irina Higgins, Antonia Creswell, Nat McAleese, Amy Wu, Erich Elsen, Siddhant Jayakumar, Elena Buchatskaya, David Budden, Esme Sutherland, Karen Simonyan, Michela Paganini, Laurent Sifre, Lena Martens, Xiang Lorraine Li, Adhiguna Kuncoro, Aida Nematzadeh, Elena Gribovskaya, Domenic Donato, 

Angeliki Lazaridou, Arthur Mensch, Jean-Baptiste Lespiau, Maria Tsimpoukelli, Nikolai Grigorev, Doug Fritz, Thibault Sottiaux, Mantas Pajarskas, Toby Pohlen, Zhitao Gong, Daniel Toyama, Cyprien de Masson d’Autume, Yujia Li, Tayfun Terzi, Vladimir Mikulik, Igor Babuschkin, Aidan Clark, Diego de Las Casas, Aurelia Guy, Chris Jones, James Bradbury, Matthew Johnson, Blake Hechtman, Laura Weidinger, Iason Gabriel, William Isaac, Ed Lockhart, Simon Osindero, Laura Rimell, Chris Dyer, Oriol Vinyals, Kareem Ayoub, Jeff Stanway, Lorrayne Bennett, Demis Hassabis, Koray Kavukcuoglu, and Geoffrey Irving. 2021. Scaling language models: Methods, analysis & insights from training gopher.

---

[referencia=c0170963c7095dc7 score=0.000]
- Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. _The Journal of Machine Learning Research_ , 21(1):5485–5551. 

- Jonathan S Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. 2019. A constructive prediction of the generalization error across scales. _arXiv preprint arXiv:1909.12673_ . 

- Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme. 2018. Gender bias in coreference resolution. In _NAACL-HLT 2018_ . 

- Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. 2021. Winogrande: An adversarial winograd schema challenge at scale. _Communications of the ACM_ , 64(9):99–106. 

- Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi. 2019. Socialiqa: Commonsense reasoning about social interactions. _arXiv preprint arXiv:1904.09728_ . 

- Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ili´c, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, Matthias Gallé, et al. 2022. Bloom: A 176bparameter open-access multilingual language model. _arXiv preprint arXiv:2211.05100_ . 

- Rico Sennrich, Barry Haddow, and Alexandra Birch. 2015. Neural machine translation of rare words with subword units. _arXiv preprint arXiv:1508.07909_ . 

- Claude E Shannon. 1948. A mathematical theory of communication. _The Bell system technical journal_ , 27(3):379–423. 

- Claude E Shannon. 1951. Prediction and entropy of printed english. _Bell system technical journal_ , 30(1):50–64.