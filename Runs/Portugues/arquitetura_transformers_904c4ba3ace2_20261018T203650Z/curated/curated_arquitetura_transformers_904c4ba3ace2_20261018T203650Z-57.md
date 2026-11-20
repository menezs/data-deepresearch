[referencia=c0170963c7095dc7 score=0.743]
### **2.2 Architecture** 

Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements that were subsequently proposed, and used in different models such as PaLM. Here are the main difference with the original architecture, and where we were found the inspiration for this change (in bracket): 

**Pre-normalization [GPT3].** To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use the RMSNorm normalizing function, introduced by Zhang and Sennrich (2019). 

**SwiGLU activation function [PaLM].** We replace the ReLU non-linearity by the SwiGLU activation function, introduced by Shazeer (2020) to improve the performance. We use a dimension of <u>2</u> 3<sup>4</sup><sup>_d_instead of 4</sup><sup>_d_as in PaLM.</sup> 

**Rotary Embeddings [GPTNeo].** We remove the absolute positional embeddings, and instead, add rotary positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of the network. 

The details of the hyper-parameters for our different models are given in Table 2.

---

[referencia=c0170963c7095dc7 score=0.002]
- Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al. 2022. Emergent abilities of large language models. _arXiv preprint arXiv:2206.07682_ . 

- Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand Joulin, and Edouard Grave. 2020. CCNet: Extracting high quality monolingual datasets from web crawl data. In _Language Resources and Evaluation Conference_ . 

- Carole-Jean Wu, Ramya Raghavendra, Udit Gupta, Bilge Acun, Newsha Ardalani, Kiwan Maeng, Gloria Chang, Fiona Aga, Jinshi Huang, Charles Bai, et al. 2022. Sustainable ai: Environmental implications, challenges and opportunities. _Proceedings of Machine Learning and Systems_ , 4:795–813. 

- Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. 2019. Hellaswag: Can a machine really finish your sentence? _arXiv preprint arXiv:1905.07830_ . 

- Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma, Yufei Xue, Jidong Zhai, Wenguang Chen, Peng Zhang, Yuxiao Dong, and Jie Tang. 2022. Glm130b: An open bilingual pre-trained model. 

- Biao Zhang and Rico Sennrich. 2019. Root mean square layer normalization. _Advances in Neural Information Processing Systems_ , 32. 

- Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. 2022. Opt: Open pre-trained transformer language models. _arXiv preprint arXiv:2205.01068_ .

---

[referencia=c0170963c7095dc7 score=0.001]
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

[referencia=c0170963c7095dc7 score=0.001]
## **A Question Answering** 

We evaluate LLaMA on Natural Questions and TriviaQA. For Natural Questions we use the test split used for open-domain question answering containing 3610 questions. For TriviaQA we evaluate on the dev set of the filtered set. This differs from GPT-3 and PaLM, which evaluate on the test set of the unfiltered set for which the online evaluation server is not available anymore<sup>5</sup> . 

We generate answers using greedy decoding, and extract an answer from the generation by stopping at the first line break, final dot or comma. Generated answers are evaluated with the standard exact match metric: a generated answer is considered correct if it matches any answer of the list of answers after normalization. For this normalization step we lowercase generated answers and remove articles, punctuation and duplicate whitespaces. Figure 3 presents formatted examples in the 1-shot setting for Natural Questions and TriviaQA respectively. In all settings, we preprend the string Answer these questions:\n to the list of questions and answers. 

Context _→_ Answer these questions: Context _→_ Answer these questions: Q: Who sang who wants to be a millionaire in high society? Q: In Scotland a bothy/bothie is a? A: Frank Sinatra A: House Q: Who wrote the book the origin of species? Q: The ancient city of Troy is located in what modern country? A: A: Target _→_ Charles Darwin Target _→_ Turkey 

Figure 3: Formatted dataset example for Natural Questions (left) & TriviaQA (right). 

5https://competitions.codalab.org/competitions/17208

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
|Miscellaneous|Other|60.0|75.7|84.5|42.4|65.4|78.5|82.1|84.3|
|Moral Disputes|Humanities|44.5|66.8|77.5|40.2|50.9|66.2|72.3|76.9|
|Moral Scenarios|Humanities|26.0|40.2|36.5|24.3|30.1|38.2|48.9|55.9|
|Nutrition|Other|47.0|69.9|77.1|37.6|51.6|62.8|67.3|74.5|
|Philosophy|Humanities|51.0|68.8|79.4|39.9|54.0|66.2|74.0|79.1|
|Prehistory|Humanities|53.0|67.6|81.2|36.1|51.5|67.0|75.3|79.0|
|Professional Accounting|Other|33.0|44.3|52.1|25.9|35.8|43.6|46.5|56.0|
|Professional Law|Humanities|34.5|44.5|56.5|30.2|38.0|45.9|49.1|54.4|
|<br>Professional Medicine|Other|36.0|64.0|75.4|<br>44.5|<br> 50.4|<br> 54.0|<br> 61.4|70.6|
|Professional Psychology<br>|Social Science<br>|44.5<br>|68.1<br>|75.7<br>|35.1 <br>|47.7 <br>|62.9 <br>|65.7<br>|71.4<br>|
|Public Relations|Social Science|48.0|71.8|73.6|40.9|60.9|67.3|73.6|74.6|
|Security Studies|Social Science|520|649|759|318|539|653|718|776|

---

[referencia=c0170963c7095dc7 score=0.000]
|High School Us History|Humanities|53.0|78.9|83.3|39.7|58.3|77.9|83.8|90.7|
|High School World History<br>|Humanities<br>|56.0<br>|75.1<br>|85.2<br>|40.9 <br>|66.2 <br>|79.3 <br>|83.1<br>|89.0<br>|
|Human Aging|Other|50.0|66.4|77.6|40.8|54.7|67.7|69.5|72.2|
|<br>Human Sexualit|Social Science|540|672|863|366|588|641|779|870|
|y<br>International Law|<br>Humanities|.<br>55.5|.<br>77.7|.<br>90.9|. <br>51.2|. <br> 62.8|. <br> 72.7|.<br> 79.3|.<br>87.6|
|Jurisprudence|Humanities|55.0|71.3|79.6|38.9|51.9|70.4|73.2|85.2|
|Logical Fallacies|Humanities|48.0|72.4|80.4|39.3|52.8|68.1|77.3|80.4|
|<br>Machine Learning|STEM|31.0|41.1|41.1|23.2|31.3|39.3|49.1|52.7|
|Management|Other|56.0|77.7|82.5|35.0|66.0|77.7|82.5|83.5|
|Marketing|Other|60.0|83.3|89.7|46.6|71.8|83.3|85.9|92.7|
|Medical Genetics|Other|40.0|69.0|69.0|43.0|52.0|67.0|67.0|68.0|
|Miscellaneous|Other|60.0|75.7|84.5|42.4|65.4|78.5|82.1|84.3|

---

[referencia=c0170963c7095dc7 score=0.000]
- Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long short-term memory. _Neural computation_ , 9(8):1735–1780. 

- Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, and Laurent Sifre. 2022. Training compute-optimal large language models. 

- Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru, Todor Mihaylov, Dániel Simig, Ping Yu, Kurt Shuster, Tianlu Wang, Qing Liu, Punit Singh Koura, et al. 2022. Opt-iml: Scaling language model instruction meta learning through the lens of generalization. _arXiv preprint arXiv:2212.12017_ . 

- Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. 2017. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. _arXiv preprint arXiv:1705.03551_ . 

- Rafal Jozefowicz, Oriol Vinyals, Mike Schuster, Noam Shazeer, and Yonghui Wu. 2016. Exploring the limits of language modeling. _arXiv preprint arXiv:1602.02410_ . 

- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. Scaling laws for neural language models. _arXiv preprint arXiv:2001.08361_ . 

- Slava Katz. 1987. Estimation of probabilities from sparse data for the language model component of a speech recognizer. _IEEE transactions on acoustics, speech, and signal processing_ , 35(3):400–401.

---

[referencia=c0170963c7095dc7 score=0.000]
- Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, Yanping Huang, Maxim Krikun, Dmitry Lepikhin, James Qin, Dehao Chen, Yuanzhong Xu, Zhifeng Chen, Adam Roberts, Maarten Bosma, Vincent Zhao, Yanqi Zhou, Chung-Ching Chang, Igor Krivokon, Will Rusch, Marc Pickett, Pranesh Srinivasan, Laichee Man, Kathleen Meier-Hellstern, Meredith Ringel Morris, Tulsee Doshi, Renelito Delos Santos, Toju Duke, Johnny Soraker, Ben Zevenbergen, Vinodkumar Prabhakaran, Mark Diaz, Ben Hutchinson, Kristen Olson, Alejandra Molina, Erin HoffmanJohn, Josh Lee, Lora Aroyo, Ravi Rajakumar, Alena Butryna, Matthew Lamm, Viktoriya Kuzmina, Joe Fenton, Aaron Cohen, Rachel Bernstein, Ray Kurzweil, Blaise Aguera-Arcas, Claire Cui, Marian Croak, Ed Chi, and Quoc Le. 2022. Lamda: Language models for dialog applications. 

- A. M. Turing. 1950. _Computing Machinery and Intelligence_ . [Oxford University Press, Mind Association]. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In _Advances in Neural Information Processing Systems 30_ , pages 5998–6008. 

- Ben Wang and Aran Komatsuzaki. 2021. GPT-J6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/kingoflolz/ mesh-transformer-jax. 

- Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery,

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
- Aitor Lewkowycz, Anders Johan Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Venkatesh Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. 2022. Solving quantitative reasoning problems with language models. In _Advances in Neural Information Processing Systems_ . 

- Opher Lieber, Or Sharir, Barak Lenz, and Yoav Shoham. 2021. Jurassic-1: Technical details and evaluation. _White Paper. AI21 Labs_ , 1. 

- Stephanie Lin, Jacob Hilton, and Owain Evans. 2021. Truthfulqa: Measuring how models mimic human falsehoods. _arXiv preprint arXiv:2109.07958_ . 

- Ilya Loshchilov and Frank Hutter. 2017. Decoupled weight decay regularization. _arXiv preprint arXiv:1711.05101_ . 

- Matthew V Mahoney. 1999. Text compression as a test for artificial intelligence. _AAAI/IAAI_ , 970. 

- Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish Sabharwal. 2018. Can a suit of armor conduct electricity? a new dataset for open book question answering. _arXiv preprint arXiv:1809.02789_ . 

- Tomas Mikolov, Martin Karafiát, Lukas Burget, Jan Cernock`y, and Sanjeev Khudanpur. 2010. Recurrent neural network based language model. In _Interspeech_ , pages 1045–1048. Makuhari. 

- Nikita Nangia, Clara Vania, Rasika Bhalerao, and Samuel R. Bowman. 2020. CrowS-pairs: A challenge dataset for measuring social biases in masked language models. In _EMNLP 2020_ .

---

[referencia=c0170963c7095dc7 score=0.000]
### **2.3 Optimizer** 

Our models are trained using the AdamW optimizer (Loshchilov and Hutter, 2017), with the following hyper-parameters: _β_ 1 = 0 _._ 9 _, β_ 2 = 0 _._ 95. We use a cosine learning rate schedule, such that the final learning rate is equal to 10% of the maximal learning rate. We use a weight decay of 0 _._ 1 and gradient clipping of 1 _._ 0. We use 2 _,_ 000 warmup 



<!-- Start of picture text -->
2.2<br>LLaMA 7B<br>2.1<br>LLaMA 13B<br>2.0 LLaMA 33B<br>LLaMA 65B<br>1.9<br>1.8<br>1.7<br>1.6<br>1.5<br>0 200 400 600 800 1000 1200 1400<br>Billion of tokens<br>Training loss<br><!-- End of picture text -->

Figure 1: **Training loss over train tokens for the 7B, 13B, 33B, and 65 models.** LLaMA-33B and LLaMA65B were trained on 1.4T tokens. The smaller models were trained on 1.0T tokens. All models are trained with a batch size of 4M tokens. 

steps, and vary the learning rate and batch size with the size of the model (see Table 2 for details).

---

[referencia=c0170963c7095dc7 score=0.000]
|Security Studies|Social Science|520|649|759|318|539|653|718|776|
|<br>Sociology|<br>Social Science|.<br>53.0|.<br>84.1|.<br>91.0|. <br>46.8|. <br> 61.2|. <br> 78.6|.<br> 78.6|.<br>88.1|
|Us Forein Polic|Social Science|690|810|920|460|800|830|860|870|
|g y<br>Virology|<br>Other|.<br>46.0|.<br>47.0|.<br>53.6|. <br>30.1|. <br> 43.4|. <br> 50.0|.<br> 53.0|.<br>57.8|
|World Religions|Humanities|55.0|84.2|87.7|50.9|67.8|81.3|81.3|84.2|
|Humanities||40.6|56.2|63.6|34.0|45.0|55.8|61.8|67.4|
|STEM||36.7|47.4|54.9|30.5|35.8|46.0|51.7|56.6|
|Social Science||50.5|71.9|79.3|38.3|53.8|66.7|72.9|79.2|
|Others||49.0|66.1|73.9|38.1|53.3|63.4|67.4|72.6|
|All||43.9|60.0|67.6|35.1|46.9|57.8|63.4|68.9|



Table 16: **MMLU.** Detailed 5-shot results per domain on the test sets.

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