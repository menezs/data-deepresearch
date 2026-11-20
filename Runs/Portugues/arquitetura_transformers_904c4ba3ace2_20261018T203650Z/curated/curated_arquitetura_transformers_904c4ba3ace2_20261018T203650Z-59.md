[referencia=c0170963c7095dc7 score=0.699]
### **2.2 Architecture** 

Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements that were subsequently proposed, and used in different models such as PaLM. Here are the main difference with the original architecture, and where we were found the inspiration for this change (in bracket): 

**Pre-normalization [GPT3].** To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use the RMSNorm normalizing function, introduced by Zhang and Sennrich (2019). 

**SwiGLU activation function [PaLM].** We replace the ReLU non-linearity by the SwiGLU activation function, introduced by Shazeer (2020) to improve the performance. We use a dimension of <u>2</u> 3<sup>4</sup><sup>_d_instead of 4</sup><sup>_d_as in PaLM.</sup> 

**Rotary Embeddings [GPTNeo].** We remove the absolute positional embeddings, and instead, add rotary positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of the network. 

The details of the hyper-parameters for our different models are given in Table 2.

---

[referencia=c0170963c7095dc7 score=0.054]
- Claude E Shannon. 1951. Prediction and entropy of printed english. _Bell system technical journal_ , 30(1):50–64. 

- Noam Shazeer. 2020. Glu variants improve transformer. _arXiv preprint arXiv:2002.05202_ . 

- Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun Peng. 2019. The woman worked as a babysitter: On biases in language generation. _arXiv preprint arXiv:1909.01326_ . 

- Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and Bryan Catanzaro. 2019. Megatron-lm: Training multi-billion parameter language models using model parallelism. _arXiv preprint arXiv:1909.08053_ . 

- Shaden Smith, Mostofa Patwary, Brandon Norick, Patrick LeGresley, Samyam Rajbhandari, Jared Casper, Zhun Liu, Shrimai Prabhumoye, George Zerveas, Vijay Korthikanti, Elton Zhang, Rewon Child, Reza Yazdani Aminabadi, Julie Bernauer, Xia Song, Mohammad Shoeybi, Yuxiong He, Michael Houston, Saurabh Tiwary, and Bryan Catanzaro. 2022. Using deepspeed and megatron to train megatron-turing nlg 530b, a large-scale generative language model. 

- Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. 2021. Roformer: Enhanced transformer with rotary position embedding. _arXiv preprint arXiv:2104.09864_ .

---

[referencia=c0170963c7095dc7 score=0.026]
As show in Table 8, for a similar number of parameters, LLaMA outperforms other general models such as LaMDA and PaLM, which are not trained or finetuned specifically for code. 

LLaMA with 13B parameters and more outperforms LaMDA 137B on both HumanEval and 

ArXiv, Gutenberg and Books3, that sums up to only 177GB, while these models were trained on up to 2TB of books. This large quantity of books used by Gopher, Chinchilla and PaLM may also explain 

MBPP. LLaMA 65B also outperforms PaLM 62B, 

even when it is trained longer. The pass@1 results 

reported in this table were obtained by sampling by Gopher, Chinchilla and PaLM may also explain with temperature 0.1. The pass@100 and pass@80 metrics were obtained with temperature 0.8. We why Gopher outperforms GPT-3 on this benchmark, use the same method as Chen et al. (2021) to obtain while it is comparable on other benchmarks. unbiased estimates of the pass@k. 

**3.7 Evolution of performance during training** 

It is possible to improve the performance on code 

by finetuning on code-specific tokens. For instance, 

During training, we tracked the performance of our models on a few question answering and common 

PaLM-Coder (Chowdhery et al., 2022) increases 

- the pass@1 score of PaLM on HumanEval from 26.2% for PaLM to 36%. Other models trained 

sense benchmarks, and report them in Figure 2. 

On most benchmarks, the performance improves steadily, and correlates with the training perplexity of the model (see Figure 1). The exceptions are SIQA and WinoGrande. Most notably, on SIQA, we observe a lot of variance in performance, 

specifically for code also perform better than general models on these tasks (Chen et al., 2021; Nijkamp et al., 2022; Fried et al., 2022). Finetuning 

on code tokens is beyond the scope of this paper.

---

[referencia=c0170963c7095dc7 score=0.022]
- Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. _Neural computation_ , 9(8):1735–1780. 

- Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre. 2022. Training compute-optimal large language models. 

- Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru, Todor Mihaylov, Dániel Simig, Ping Yu, Kurt Shuster, Tianlu Wang, Qing Liu, Punit Singh Koura, et al. 2022. Opt-iml: Scaling language model instruction meta learning through the lens of generalization. _arXiv preprint arXiv:2212.12017_ . 

- Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. 2017. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. _arXiv preprint arXiv:1705.03551_ . 

- Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016. Exploring the limits of language modeling. _arXiv preprint arXiv:1602.02410_ . 

- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. Scaling laws for neural language models. _arXiv preprint arXiv:2001.08361_ . 

- Slava Katz. 1987. Estimation of probabilities from sparse data for the language model component of a speech recognizer. _IEEE transactions on acoustics, speech, and signal processing_ , 35(3):400–401.

---

[referencia=c0170963c7095dc7 score=0.010]
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

[referencia=c0170963c7095dc7 score=0.009]
- Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, Yanping Huang, Maxim Krikun, Dmitry Lepikhin, James Qin, Dehao Chen, Yuanzhong Xu, Zhifeng Chen, Adam Roberts, Maarten Bosma, Vincent Zhao, Yanqi Zhou, Chung-Ching Chang, Igor Krivokon, Will Rusch, Marc Pickett, Pranesh Srinivasan, Laichee Man, Kathleen Meier-Hellstern, Meredith Ringel Morris, Tulsee Doshi, Renelito Delos Santos, Toju Duke, Johnny Soraker, Ben Zevenbergen, Vinodkumar Prabhakaran, Mark Diaz, Ben Hutchinson, Kristen Olson, Alejandra Molina, Erin HoffmanJohn, Josh Lee, Lora Aroyo, Ravi Rajakumar, Alena Butryna, Matthew Lamm, Viktoriya Kuzmina, Joe Fenton, Aaron Cohen, Rachel Bernstein, Ray Kurzweil, Blaise Aguera-Arcas, Claire Cui, Marian Croak, Ed Chi, and Quoc Le. 2022. Lamda: Language models for dialog applications. 

- A. M. Turing. 1950. _Computing Machinery and Intelligence_ . [Oxford University Press, Mind Association]. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In _Advances in Neural Information Processing Systems 30_ , pages 5998–6008. 

- Ben Wang and Aran Komatsuzaki. 2021. GPT-J6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/ mesh-transformer-jax. 

- Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery,

---

[referencia=c0170963c7095dc7 score=0.008]
The focus of this work is to train a series of language models that achieve the best possible performance at various inference budgets, by training on more tokens than what is typically used. The resulting models, called _LLaMA_ , ranges from 7B to 65B parameters with competitive performance compared to the best existing LLMs. For instance, LLaMA-13B outperforms GPT-3 on most benchmarks, despite being 10 _×_ smaller. We believe that this model will help democratize the access and study of LLMs, since it can be run on a single GPU. At the higher-end of the scale, our 65B-parameter model is also competitive with the best large language models such as Chinchilla or PaLM-540B. 

Unlike Chinchilla, PaLM, or GPT-3, we only use publicly available data, making our work compatible with open-sourcing, while most existing models rely on data which is either not publicly available or undocumented (e.g. “Books – 2TB” or “Social media conversations”). There exist some exceptions, notably OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022) and GLM (Zeng et al., 2022), but none that are competitive with PaLM-62B or Chinchilla. 

In the rest of this paper, we present an overview of the modifications we made to the transformer architecture (Vaswani et al., 2017), as well as our training method. We then report the performance of our models and compare with others LLMs on a set of standard benchmarks. Finally, we expose some of the biases and toxicity encoded in our models, using some of the most recent benchmarks from the responsible AI community.

---

[referencia=c0170963c7095dc7 score=0.007]
In the context of neural language models, Jozefowicz et al. (2016) obtained state-of-the-art results on the Billion Word benchmark by scaling LSTMs to 1 billion parameters. Later, scaling transformers lead to improvement on many NLP tasks. Notable models include BERT (Devlin et al., 2018), GPT-2 (Radford et al., 2019), MegatronLM (Shoeybi et al., 2019), and T5 (Raffel et al., 2020). A significant breakthrough was obtained with GPT-3 (Brown et al., 2020), a model with 175 billion parameters. This lead to a series of _Large Language Models_ , such as Jurassic-1 (Lieber et al., 2021), Megatron-Turing NLG (Smith et al., 

2022), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022), PaLM (Chowdhery et al., 2022), OPT (Zhang et al., 2022), and GLM (Zeng et al., 2022). Hestness et al. (2017) and Rosenfeld et al. (2019) studied the impact of scaling on the performance of deep learning models, showing the existence of power laws between the model and dataset sizes and the performance of the system. Kaplan et al. (2020) derived power laws specifically for transformer based language models, which were later refined by Hoffmann et al. (2022), by adapting the learning rate schedule when scaling datasets. Finally, Wei et al. (2022) studied the effect of scaling on the abilities of large language models.

---

[referencia=c0170963c7095dc7 score=0.006]
### **2.1 Pre-training Data** 

Our training dataset is a mixture of several sources, reported in Table 1, that cover a diverse set of domains. For the most part, we reuse data sources that have been leveraged to train other LLMs, with the restriction of only using data that is publicly available, and compatible with open sourcing. This leads to the following mixture of data and the percentage they represent in the training set: 

**English CommonCrawl [67%].** We preprocess five CommonCrawl dumps, ranging from 2017 to 2020, with the CCNet pipeline (Wenzek et al., 2020). This process deduplicates the data at the line level, performs language identification with a fastText linear classifier to remove non-English pages and filters low quality content with an n- gram language model. In addition, we trained a linear model to classify pages used as references in Wikipedia _v.s._ randomly sampled pages, and discarded pages not classified as references. 

**C4 [15%].** During exploratory experiments, we observed that using diverse pre-processed CommonCrawl datasets improves performance. We thus included the publicly available C4 dataset (Raffel et al., 2020) in our data. The preprocessing of C4 also contains deduplication and language identification steps: the main difference with CCNet is the quality filtering, which mostly relies on heuristics such as presence of punctuation marks or the number of words and sentences in a webpage. 

**Github [4.5%].** We use the public GitHub dataset available on Google BigQuery. We only kept projects that are distributed under the Apache, BSD and MIT licenses. Additionally, we filtered low quality files with heuristics based on the line length or proportion of alphanumeric characters, and removed boilerplate, such as headers, with regular expressions. Finally, we deduplicate the resulting dataset at the file level, with exact matches. 

**Wikipedia [4.5%].** We add Wikipedia dumps from the June-August 2022 period, covering 20

---

[referencia=c0170963c7095dc7 score=0.006]
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

[referencia=c0170963c7095dc7 score=0.005]
## **1 Introduction** 

Large Languages Models (LLMs) trained on massive corpora of texts have shown their ability to perform new tasks from textual instructions or from a few examples (Brown et al., 2020). These few-shot properties first appeared when scaling models to a sufficient size (Kaplan et al., 2020), resulting in a line of work that focuses on further scaling these models (Chowdhery et al., 2022; Rae et al., 2021). These efforts are based on the assumption that more parameters will lead to better performance. However, recent work from Hoffmann et al. (2022) shows that, for a given compute budget, the best performances are not achieved by the largest models, but by smaller models trained on more data. 

The objective of the scaling laws from Hoffmann et al. (2022) is to determine how to best scale the dataset and model sizes for a particular _training_ compute budget. However, this objective disregards the _inference_ budget, which becomes critical when serving a language model at scale. In this context, given a target level of performance, the preferred model is not the fastest to train but the fastest at inference, and although it may be cheaper to train a large model to reach a certain level of 

> _∗_ Equal contribution. Correspondence: {htouvron, thibautlav,gizacard,egrave,glample}@meta.com 

> 1https://github.com/facebookresearch/llama 

performance, a smaller one trained longer will ultimately be cheaper at inference. For instance, although Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, we find that the performance of a 7B model continues to improve even after 1T tokens.

---

[referencia=c0170963c7095dc7 score=0.005]
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

[referencia=c0170963c7095dc7 score=0.004]
### **2.4 Efficient implementation** 

We make several optimizations to improve the training speed of our models. First, we use an efficient implementation of the causal multi-head attention to reduce memory usage and runtime. This implementation, available in the xformers library,<sup>2</sup> is inspired by Rabe and Staats (2021) and uses the backward from Dao et al. (2022). This is achieved by not storing the attention weights and not computing the key/query scores that are masked due to the causal nature of the language modeling task. 

To further improve training efficiency, we reduced the amount of activations that are recomputed during the backward pass with checkpointing. More precisely, we save the activations that are expensive to compute, such as the outputs of linear layers. This is achieved by manually implementing the backward function for the transformer layers, instead of relying on the PyTorch autograd. To fully benefit from this optimization, we need to 

2https://github.com/facebookresearch/xformers

---

[referencia=c0170963c7095dc7 score=0.003]
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

[referencia=c0170963c7095dc7 score=0.003]
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

[referencia=c0170963c7095dc7 score=0.003]
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

[referencia=c0170963c7095dc7 score=0.002]
- Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. _The Journal of Machine Learning Research_ , 21(1):5485–5551. 

- Jonathan S Rosenfeld, Amir Rosenfeld, Yonatan Belinkov, and Nir Shavit. 2019. A constructive prediction of the generalization error across scales. _arXiv preprint arXiv:1909.12673_ . 

- Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme. 2018. Gender bias in coreference resolution. In _NAACL-HLT 2018_ . 

- Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. 2021. Winogrande: An adversarial winograd schema challenge at scale. _Communications of the ACM_ , 64(9):99–106. 

- Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi. 2019. Socialiqa: Commonsense reasoning about social interactions. _arXiv preprint arXiv:1904.09728_ . 

- Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ili´c, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, Matthias Gallé, et al. 2022. Bloom: A 176bparameter open-access multilingual language model. _arXiv preprint arXiv:2211.05100_ . 

- Rico Sennrich, Barry Haddow, and Alexandra Birch. 2015. Neural machine translation of rare words with subword units. _arXiv preprint arXiv:1508.07909_ . 

- Claude E Shannon. 1948. A mathematical theory of communication. _The Bell system technical journal_ , 27(3):379–423. 

- Claude E Shannon. 1951. Prediction and entropy of printed english. _Bell system technical journal_ , 30(1):50–64.

---

[referencia=c0170963c7095dc7 score=0.002]
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

[referencia=c0170963c7095dc7 score=0.002]
## **8 Conclusion** 

In this paper, we presented a series of language models that are released openly, and competitive with state-of-the-art foundation models. Most notably, LLaMA-13B outperforms GPT-3 while being more than 10 _×_ smaller, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B. Unlike previous studies, we show that it is possible to achieve state-of-the-art performance by training exclusively on publicly available data, without resorting to proprietary datasets. We hope that releasing these models to the research community will accelerate the development of large language models, and help efforts to improve their robustness and mitigate known issues such as toxicity and bias. Additionally, we observed like Chung et al. (2022) that finetuning these models on instructions lead to promising results, and we plan to further investigate this in future work. Finally, we plan to release larger models trained on larger pretraining corpora in the future, since we have seen a constant improvement in performance as we were scaling. 

## **Acknowledgements** 

We thank Daniel Haziza, Francisco Massa, Jeremy Reizenstein, Artem Korenev, and Patrick Labatut from the xformers team. We thank Susan Zhang and Stephen Roller for their support on data deduplication. We thank Luca Wehrstedt, Vegard Mella, and Pierre-Emmanuel Mazaré for their support on training stability. We thank Shubho Sengupta, Kalyan Saladi, and all the AI infra team for their support. We thank Jane Yu for her input on evaluation. We thank Yongyi Hu for his help on data collection.

---

[referencia=c0170963c7095dc7 score=0.002]
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