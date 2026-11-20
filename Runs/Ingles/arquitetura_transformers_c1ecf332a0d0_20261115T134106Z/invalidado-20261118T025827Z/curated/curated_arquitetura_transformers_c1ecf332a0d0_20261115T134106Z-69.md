[referencia=d7eccd072c35cb31 score=0.618]
### 3.2 Pretraining

We next briefly present the key model and training parameters (detailed in Table 5 in the Appendix A.1) and the pretraining software and configuration.

Architecture Poro 34B is a decoder-only model with a parameter count of 34 billion, sharing its architecture with FinGPT (Luukkonen et al., 2023) and BLOOM (Le Scao et al., 2022). It incorporates layer normalization immediately following the input embedding layer for better training stability and uses ALiBi (Press et al., 2021) as its positional encoding method. The model consists of 54 layers with a hidden dimension of 7168 and a total of 56 attention heads.

Training We train to 1T tokens, intentionally exceeding the Chinchilla compute-opimality estimate (Hoffmann et al., 2022a) of approximately 700B tokens for a model of this size, thus gaining inference-time efficiency for the cost of additional compute investment in pretraining (Sardana and Frankle, 2023). We train with a sequence length of 2048 tokens<sup>5</sup><sup>5</sup>
              5
              
              
              
            We acknowledge that this can be considered limiting by today’s standards, but this limitation can be relieved by methods for extending the context length, for example via linear extrapolation (Press et al., 2021) or interpolation (Al-Khateeb et al., 2023).
using a cosine learning rate scheduler with a maximum learning rate of 1.5e-4, decaying to a minimum of 2e-5 over 990B tokens, and a linear warmup of 10B tokens. Our global batch size is 2048 samples totaling to 4194304 tokens per optimization step.

Software Poro 34B was trained on the LUMI supercomputer GPU partition, which is powered by AMD MI250X GPUs. The majority of open source frameworks for large language model pretraining are made to be primarily NVIDIA-compatible, and we required scalable AMD-compatible training software. Thus, we adopted the Megatron-DeepSpeed fork<sup>6</sup><sup>6</sup>
              6
              
              
              
            https://github.com/TurkuNLP/Megatron-DeepSpeed introduced by Luukkonen et al. (2023),

---

[referencia=d7eccd072c35cb31 score=0.303]
## 1 Introduction

Neural language models based on the transformer architecture Vaswani et al. (2017) have led to substantial advances in natural language processing. Encoder-only transformer models such as BERT Devlin et al. (2019) have advanced the state of the art in a broad range of classification tasks, while decoder-only models such as GPT Radford et al. (2018) have redefined what can be achieved by generative models, opening new areas of study in prompting and in-context learning. The success of these models is related in substantial part to their scaling properties: training larger models on more data leads to better results and even entirely new capabilities (Brown et al., 2020). Studies refining our understanding of the optimal balance of model size and training steps have increased the demands on data (Hoffmann et al., 2022b), and many recent models optimize further for inference-time efficiency by training smaller models on more data (Sardana and Frankle, 2023).

These developments have introduced increasing demands for textual data, with many recent models pretrained on a trillion tokens or more (Touvron et al., 2023; Almazrouei et al., 2023; MosaicML, 2023; Li et al., 2023; Lozhkov et al., 2024; Groeneveld et al., 2024, e.g.). While such resources can still be assembled from internet crawls for a few of the languages best represented online, for the vast majority of human languages we have already run out of data for training the largest of language models (Joshi et al., 2020; Villalobos et al., 2022). While it is standard to repeat training data, repetition can lead to reduced sample efficiency and degradation of performance (Hernandez et al., 2022): Muennighoff et al. (2024) estimate that the value of repetition starts to diminish rapidly after four epochs and that repetition ceases to add information around 40 epochs. The availability of data is thus currently a limit for monolingual training for all but a few of the highest-resourced languages.

---

[referencia=d7eccd072c35cb31 score=0.201]
Multilingual training offers one obvious solution for increasing the amount of training data available, and a large number of multilingual transformer models have been introduced (Conneau et al., 2020; Lin et al., 2022b; Le Scao et al., 2022; Wei et al., 2023, e.g.). However, despite the intuitive appeal of augmenting training data with texts in other natural languages, multilinguality is frequently seen as a negative – commonly referred to as the *curse of multilinguality* (Conneau et al., 2020). While there have been studies of the tradeoffs between monolingual and multilingual training (Fujinuma et al., 2022; Chang et al., 2023) as well as efforts to enhance models specifically for multilinguality (Pfeiffer et al., 2022) and to introduce additional language capabilities to existing models (Gogoulou et al., 2023; Kew et al., 2023; Zhao et al., 2024; Ibrahim et al., 2024), state-of-the-art generative models are still frequently trained near-exclusively on large languages such as English, with only limited efforts specifically focusing on optimizing performance for smaller languages.
In this study, we explore how to lift data limitations to create state-of-the-art large generative models from scratch for smaller languages, drawing on the understanding emerging in recent studies on how to make the most of limited data and assure that multilinguality is a blessing rather than a curse. Some key lessons from previous work include
1) limited multilinguality instead of a large number of languages (Conneau et al., 2020; Chang et al., 2023)
2) matching scripts (e.g., Latin) (Fujinuma et al., 2022) and
3) matching language families (Pyysalo et al., 2021),
4) incorporating a cross-lingual signal using translation pairs (Anil et al., 2023; Wei et al., 2023),
5) oversampling target language data up to four epochs (Muennighoff et al., 2024) and 6) augmenting natural language with programming language data (Madaan et al., 2022; Aryabumi et al., 2024).

---

[referencia=d7eccd072c35cb31 score=0.178]
## 2 Pretraining data

For pretraining Poro 34B, we rely on datasets that have been previously preprocessed to remove low-quality texts and boilerplate, filter toxic context, and deduplicate repeated texts. We illustrate the pretraining data distribution in Figure 1 and describe the data briefly in the following. Data sources are detailed in Table 4 in the Appendix.

#### Finnish

For Finnish pretraining data, we draw on the resources recently introduced by Luukkonen et al. for creating the FinGPT model family. We exclude the *ePub* and *Lehdet* resources provided by the National Library of Finland for that work as they could not be shared due to copyright limitations, but use the remaining sources of data, totalling to a 32B token monolingual corpus. The majority of the Finnish data originates from web crawls (approx. 84%) complemented with news sources (approx. 2%), Project Lönnrot, the Finnish equivalent of Project Gutenberg copyright-free book corpus (approx. 0.5%), Wikipedia (approx. 0.5%) and Finnish online discussion forum contents from Reddit and Suomi24 (approx. 13%). Following the rule of thumb proposed by Muennighoff et al. (2024), we upsample the 32B tokens of Finnish so that four epochs over the data are made during training. Consequently, approximately 13% of the total tokens seen in pretraining are Finnish.

#### English

For English pretraining data, we primarily use SlimPajama (Soboleva et al., 2023), a cleaned and deduplicated subset of the RedPajama corpus<sup>1</sup><sup>1</sup>
              1
              
              
              
            https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T (Together Computer, 2023), from which we excluded data from the books category due to their copyright status. We supplemented this dataset with the Project Gutenberg public domain books data from the Dolma corpus<sup>2</sup><sup>2</sup>
              2
              
              
              
            https://huggingface.co/datasets/allenai/dolma (Soldaini et al., 2024). We train for one epoch over the 542B tokens of the English data, which thus represents slightly over half of the 1T total training tokens.

---

[referencia=d7eccd072c35cb31 score=0.142]
## 5 Discussion and conclusions

In this study, we have considered the challenges that the availability of data poses for pretraining large generative models for smaller languages and explored a limited multilingual approach to create Poro 34B, a 34B-parameter model trained on 1T tokens of Finnish, English, and code, including 8B tokens of Finnish-English translation pairs. We thoroughly evaluated the model and found it to substantially advance over the performance of existing models for Finnish while also performing competitively in its class of open models for English and code generation, as well as achieving remarkably good results in translation tasks. Two human judges and GPT-4 Turbo found the texts generated by Poro 34B to be superior to the competing models.

Our model architecture and the Finnish datasets included follow those of the FinGPT family of monolingual Finnish models, which were constrained by the available Finnish training data. The superior performance of our model in Finnish evaluations demonstrates that multilingual training can lift such limitations, allowing further scaling of models focused on smaller languages. In future work, we hope to explore this effect more systematically to answer some of the many questions that remain open regarding the training of large generative models for smaller languages, including the impacts of covering multiple smaller languages and the effect of the size of data available in the target languages.

A number of the choices made in training Poro 34B were made with incomplete information regarding their specific impacts on the final model. For example, we opted to include a comparatively large amount of programming language data as well as instruction-formatted translation examples in the pretraining data, the latter on the assumption that this would provide a cross-lingual signal that would strengthen the ability of the model to benefit from data in a more distantly related language (English). While this approach is intuitively appealing and the performance of our model suggests that it has at a minimum not notably detracted from the capabilities of the model, we did not as part of this work have the resources to conduct ablation studies nor to explore alternative ways to incorporate cross-lingual information in pretraining. We aim to study these questions further in future work.

---

[referencia=d7eccd072c35cb31 score=0.108]
## 3 Methods

In this section, we describe the method used to create the Poro 34B tokenizer, the pretraining setup, and provide an estimate of the compute cost of pretraining the model.

### 3.1 Tokenization

The choice of tokenizer has a broad range of impacts, not only on the efficiency of training and inference but also the capabilities of trained models (Rust et al., 2021; Petrov et al., 2023; Ali et al., 2023). As we were not aware of any existing tokenizer that would be a good fit for our combination of languages and code, we created a new tokenizer for our model. Specifically, we trained a custom byte-level BPE tokenizer using the same pre-normalization as the FinGPT tokenizer. We selected a vocabulary size of 128K tokens, aiming to achieve low fertility on the targeted languages while keeping the vocabulary reasonably small. The tokenizer was trained on a uniform distribution of samples of the Finnish, English and code datasets.

We assess the fertility of the tokenizer on the English and Finnish sentences from the devtest portion of the widely used Flores-101 benchmark for machine translation Goyal et al. (2022), which allows for a degree of cross-lingual comparability. For code, we use an approximately 1M character sample of lines from the Starcoder held-out test data.<sup>4</sup><sup>4</sup>
              4
              
              
              
            We only sample lines with at least 10 alphabetic characters to avoid very short lines.
Figure 2
provides a comparison of the fertility of the tokenizer compared to selected reference tokenizers (see Section 4). We find that on this data the new Poro 34B tokenizer has at least broadly comparable fertility to the lowest-scoring tokenizer on each of Finnish, English, and code, as well as the lowest average fertility of the compared tokenizers.

---

[referencia=d7eccd072c35cb31 score=0.108]
## 4 Evaluation

We thoroughly analyze the capabilities of the model for Finnish, English and code, first briefly reporting perplexity results and then focusing on community-standard benchmarks for evaluating generative models. We then assess the quality of Finnish text generated by the model and finally evaluate the model’s translation capability from English to Finnish (and vice versa). For comparison, we include results for the state-of-the-art Finnish language models, FinGPT 8B and FinGPT 13B (Luukkonen et al., 2023), and a selection of similarly-sized general-purpose open source base language models trained on broadly comparable numbers of tokens for English<sup>9</sup><sup>9</sup>
            9
            
            
            
          We chose English models of similar size and training token budget rather than state-of-the-art models to more directly assess the effects of our multilingual training setup on performance in English.: Llama 33B (Touvron et al., 2023),
MPT 30B (MosaicML, 2023), and Falcon 40B (Almazrouei et al., 2023). We also provide results for
StarCoder base (Li et al., 2023) as a reference for performance on code tasks.

---

[referencia=d7eccd072c35cb31 score=0.092]
- Sardana and Frankle (2023)
Nikhil Sardana and Jonathan Frankle. 2023.
Beyond chinchilla-optimal: Accounting for inference in language model scaling laws.
*arXiv preprint arXiv:2401.00448* .
- Soboleva et al. (2023) Daria Soboleva, Faisal Al-Khateeb, Robert Myers, Jacob R Steeves, Joel Hestness, and Nolan Dey. 2023. SlimPajama: A 627B token cleaned and deduplicated version of RedPajama.
- Soldaini et al. (2024)
Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, David Atkinson, Russell Authur, Ben Bogin, Khyathi Chandu, Jennifer Dumas, Yanai Elazar, Valentin Hofmann, Ananya Harsh Jha, Sachin Kumar, Li Lucy, Xinxi Lyu, Nathan Lambert, Ian Magnusson, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew E. Peters, Abhilasha Ravichander, Kyle Richardson, Zejiang Shen, Emma Strubell, Nishant Subramani, Oyvind Tafjord, Pete Walsh, Luke Zettlemoyer, Noah A. Smith, Hannaneh Hajishirzi, Iz Beltagy, Dirk Groeneveld, Jesse Dodge, and Kyle Lo. 2024.
Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research.
*arXiv preprint* .
- Srivastava et al. (2022)
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. 2022.
Beyond the imitation game: Quantifying and extrapolating the capabilities of language models.
*arXiv preprint arXiv:2206.04615* .

---

[referencia=d7eccd072c35cb31 score=0.065]
### 4.3 Benchmark results

The overall results of the benchmark evaluations are summarized in Table 2 and detailed in Appendix A.2. We find that Poro 34B is the best-performing model for Finnish in this comparison, substantially outperforming the best previously introduced monolingual Finnish model. We further analyzed the progression of the Finnish capabilities by evaluating Poro 34B checkpoints at 10% intervals on FIN-bench. These results are summarized in Figure 3. Interestingly, the model outperforms the best FinGPT model already after 100B tokens of training (10%) despite the relatively small proportion of Finnish in the Poro 34B data and the fact that the FinGPT models were trained on 300B tokens in total. These results indicate that our limited multilingual approach is effective for creating stronger models for Finnish than possible through monolingual training and demonstrate that the model is benefiting substantially from its training data in other languages even when tested on Finnish tasks.

For English, we find that the model achieves broadly comparable results to the MPT 30B and Falcon 40B models, both of which were trained for 1T tokens of predominantly English data. This indicates that the limited multilingual training approach has not notably detracted from the English capabilities of the model. The best-performing open model in this comparison is Llama 33B, which was trained for longer (1.4T tokens), also predominantly on English data. We find that Poro 34B is nevertheless a capable model in its class also for English, despite not optimizing specifically for English performance. The programming language benchmarks indicate that Poro 34B is more capable on code than the other natural language-focused models, while the code-focused StarCoder model clearly outperforms all of the other models. We attribute the relatively high performance of Poro 34B on code to the comparatively large proportion of the training data dedicated to code. As with English, we consider the performance of the model on code a positive addition even though code generation was not a primary goal in creating the model.

---

[referencia=d7eccd072c35cb31 score=0.047]
# Poro 34B and the Blessing of Multilinguality

###### Abstract

The pretraining of state-of-the-art large language models now requires trillions of words of text, which is orders of magnitude more than available for the vast majority of languages. While including text in more than one language is an obvious way to acquire more pretraining data, multilinguality is often seen as a curse, and most model training efforts continue to focus near-exclusively on individual large languages. We believe that multilinguality can be a blessing: when the lack of training data is a constraint for effectively training larger models for a target language, augmenting the dataset with other languages can offer a way to improve over the capabilities of monolingual models for that language. In this study, we introduce Poro 34B, a 34 billion parameter model trained for 1 trillion tokens of Finnish, English, and programming languages, and demonstrate that a multilingual training approach can produce a model that substantially advances over the capabilities of existing models for Finnish and excels in translation, while also achieving competitive performance in its class for English and programming languages. We release the model parameters, scripts, and data under open licenses at https://huggingface.co/LumiOpen/Poro-34B.

---

[referencia=d7eccd072c35cb31 score=0.038]
We chose to specifically target the Finnish language, which is an interesting case for study as it is a Uralic language with no large close neighbours in its language family, necessitating more distant transfer than, for example, between English and another Germanic language. While the language is natively spoken by under six million people, its resources are still sufficient to consider a monolingual training approach for larger generative models. In a recent study, Luukkonen et al. (2023) combined several web crawls and curated sources of Finnish to create a dataset of approximately 40B tokens and introduced the monolingual FinGPT models trained from scratch for 300B tokens. With approximately 8 epochs, the repetition of data is expected to show diminishing returns (Muennighoff et al., 2024), and the largest of these models show signs of data limitations, with the 8B parameter model outperforming the 13B in benchmarks. We believe it should be possible to overcome these limitations by applying the lessons listed above. While we cannot match language families, we train for four epochs over the Finnish data and augment it with both English and programming language data as well as an explicit cross-lingual signal from translation pairs. We pursue this approach to create Poro 34B, training a 34B parameter model for a total of 1T tokens – 25 times more than the available Finnish data – and evaluate the model in detail on Finnish, English, and programming language tasks. We find that the model not only achieves the goal of substantially advancing over the performance of existing Finnish models, but is also competitive in its class of open models on English and code as well as remarkably strong in translation tasks.

---

[referencia=d7eccd072c35cb31 score=0.026]
### Ethical considerations

We are committed to open science, transparency and accessibility in our work. While we acknowledge the concerns and the potential for negative impacts associated with making powerful generative models and the technology to create them more widely available, we believe that in the case of Poro 34B the positives clearly outweigh the negatives. We discuss some specific concerns and their mitigations in the following.

Poro 34B is a base model trained in substantial part on texts sourced from web crawls, which are known to include biases, toxicity and factual errors. While we have selected curated text sources that have been extensively filtered to remove problematic material, no such filtering is perfect. Like all language models, Poro 34B is a product of its inputs, and its output may reflect issues in its training material. Furthermore, as Poro 34B is a base model that has not been finetuned for any specific purpose, extra care should be taken when interpreting its output, and the model should not be used as is in any application with potential for significant impact on people’s rights or well-being. We emphasize these limitations in the model card published with the model.

Pretraining large language models is computationally intensive, and the creation of large models can have substantial environmental impacts. Poro 34B was trained on the LUMI supercomputer, which is powered entirely by renewable energy resources. According to the official specifications, the carbon intensity factor of LUMI’s operation is considered to be zero. This approach effectively minimizes the carbon footprint associated with the computational aspects of training our model.

Though concerns about the capabilities of frontier models to cause catastrophic harm have been discussed in the literature, a model of Poro 34B’s size and training duration does not represent new frontier capability and releasing the model does not introduce any new classes of risk.

### Acknowledgements

The authors wish to acknowledge CSC – IT Center for Science, Finland, for generous computational resources on the LUMI supercomputer. This project has received funding from the European Union’s Horizon Europe research and innovation programme under Grant agreement No 101070350. The contents of this publication are the sole responsibility of its authors and do not necessarily reflect the opinion of the European Union.

---

[referencia=d7eccd072c35cb31 score=0.024]
### A.1 Training details

It has been our aim throughout this work to release Poro 34B fully openly, including model weights, pretraining configuration, the pretraining and evaluation data, and all associated scripts and tools. We provide here additional details of these to facilitate accurate reproduction of our work. The pretraining data sources are detailed in Table 4, and the model and pretraining hyperparameters in Table 5.

| Dataset | Language | Reference | 
|---|---|---|
| SlimPajama | English | https://huggingface.co/datasets/cerebras/SlimPajama-627B | 
| Starcoder | Code | https://huggingface.co/datasets/bigcode/starcoderdata | 
| Tatoeba challenge | Eng-Fin | https://huggingface.co/datasets/tatoeba | 
| Project Gutenberg | English | https://huggingface.co/datasets/allenai/dolma | 
| Parsebank | Finnish | https://turkunlp.org/finnish_nlp.html | 
| mC4 |  | https://huggingface.co/datasets/mc4 | 
| CC-Fi |  | https://github.com/TurkuNLP/CC-Fi | 
| Fiwiki |  | https://fi.wikipedia.org/wiki | 
| Lönnrot |  | http://www.lonnrot.net | 
| Suomi24 |  | http://urn.fi/urn:nbn:fi:lb-2021101527 | 
| Reddit-Fi |  | https://www.reddit.com/r/Suomi | 
| STT |  | http://urn.fi/urn:nbn:fi:lb-2019041501 | 
| Yle |  | http://urn.fi/urn:nbn:fi:lb-2017070501 | 
| Yle |  | http://urn.fi/urn:nbn:fi:lb-2021050401 | 
| Yle |  | http://urn.fi/urn:nbn:fi:lb-2019050901 | 
| Yle |  | http://urn.fi/urn:nbn:fi:lb-2021050701 |

---

[referencia=d7eccd072c35cb31 score=0.021]
- Hernandez et al. (2022)
Danny Hernandez, Tom Brown, Tom Conerly, Nova DasSarma, Dawn Drain, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Tom Henighan, Tristan Hume, et al. 2022.
Scaling laws and interpretability of learning from repeated data.
*arXiv preprint arXiv:2205.10487* .
- Hoffmann et al. (2022a)
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. 2022a.
Training compute-optimal large language models.
*arXiv preprint arXiv:2203.15556* .
- Hoffmann et al. (2022b)
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Thomas Hennigan, Eric Noland, Katherine Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karén Simonyan, Erich Elsen, Oriol Vinyals, Jack Rae, and Laurent Sifre. 2022b.
An empirical analysis of compute-optimal large language model training.
In *Advances in Neural Information Processing Systems* , volume 35, pages 30016–30030. Curran Associates, Inc.
- Ibrahim et al. (2024) Adam Ibrahim, Benjamin Thérien, Kshitij Gupta, Mats L. Richter, Quentin Anthony, Timothée Lesort, Eugene Belilovsky, and Irina Rish. 2024. Simple and scalable strategies to continually pre-train large language models.
- Joshi et al. (2020)
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika Bali, and Monojit Choudhury. 2020.
The state and fate of linguistic diversity and inclusion in the NLP world.
In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* , pages 6282–6293.

---

[referencia=d7eccd072c35cb31 score=0.016]
We hope that our approach can serve as a template for the creation of larger models for other smaller languages and that the model introduced in this work can serve as both as a focus of research in its own right as well as a starting point for further pretraining, finetuning and alignment to create useful models, tools and methods not only for Finnish but also other languages. We release the model weights as well as all relevant documentation and software fully openly at https://huggingface.co/LumiOpen/Poro-34B.

### Limitations

Our study applies a pretraining recipe that combines insights on effective multilingual and data-constrained model training from a variety of previous studies. While the findings of these studies are supported by a broad range of relevant experimental results, we did not have the resources to perform separate ablation experiments specifically assessing the impact that various parts of our combined pretraining recipe (e.g., four repetitions of target language data and the inclusion of a translation signal) have on the resulting model. Thus, while we believe that our results demonstrate the pretraining recipe to be effective for creating state-of-the-art models for data-constrained languages, our work is limited in leaving many questions open regarding specific choices that form part of that recipe.

Poro 34B is a base model and as such has not been aligned to follow instructions and engage in conversations. It has not been evaluated on safety and toxicity benchmarks. As we have noted in our language generation evaluation, Poro 34B does not adequately follow instructions and has the tendency to generate texts with hallucinations. Further research is needed to improve the model in terms of factuality, safety, and alignment in English and Finnish. We encourage developers using Poro 34B to be aware of the potential risks associated with LLMs such as non-factual outputs, harmful language, and perpetuation of biases and stereotypes. We recommend that developers finetune Poro 34B to meet their specific needs and codes of conduct.

---

[referencia=d7eccd072c35cb31 score=0.016]
| Architecture hyperparameters |  | Pretraining hyperparameters |  | 
|---|---|---|---|
| Parameters | 34B | Global Batch Size | 2048 | 
| Precision | bfloat16 | Learning rate | 1.5e-4 | 
| Layers | 54 | Total tokens | 1000B | 
| Hidden dim | 7168 | Warmup tokens | 10B | 
| Attention heads | 56 | Decay tokens | 1000B | 
| Vocab size | 131072 | Decay style | cosine | 
| Sequence length | 2048 | Min. learning rate | 2e-5 | 
| Activation | GELU | Adam (, ) | (0.9, 0.95) | 
| Position embedding | ALiBi | Weight decay | 2e-5 | 
| Tied embeddings | True | Gradient clipping | 1.0 |

---

[referencia=d7eccd072c35cb31 score=0.013]
### 4.1 Data and experimental setup

We assess the perplexity of the model on the same data used to evaluate tokenizer fertility (Section 3.1), namely Flores-101 devtest English and Finnish and a sample of the StarCoder test data. As token-level perplexity is dependent on tokenization, it cannot be used to directly compare models with different tokenizers. We therefore report character-level perplexity following Ekgren et al. (2022), normalizing by character rather than token count when calculating perplexity.

We benchmark the capabilities of the model in Finnish using the FIN-bench<sup>10</sup><sup>10</sup>
              10
              
              
              
            https://github.com/TurkuNLP/FIN-bench dataset  (Luukkonen et al., 2023), which covers a variety of tasks to assess various aspects of model capabilities in Finnish, combining selected tasks translated and manually corrected from English BIG-bench (Srivastava et al., 2022) with additional Finnish tasks. We evaluate all FIN-bench results in a 3-shot setting using the standard metrics defined for the benchmark. For English evaluations, we use LM Eval Harness (Gao et al., 2023) to evaluate with the following datasets:
ARC Challenge (Clark et al., 2018),
GSM8K (Cobbe et al., 2021),
HellaSwag (Zellers et al., 2019),
MMLU (Hendrycks et al., 2021),
TruthfulQA (Lin et al., 2022a), and
Winogrande (Sakaguchi et al., 2019). We selected these evaluations based on their use as English language benchmarks by Beeching et al. (2023) and use an identical testing configuration here.
Programming language proficiency is assessed via the Bigcode Evaluation Harness (Ben Allal et al., 2022) with the
HumanEval (Chen et al., 2021), and
MBPP (Austin et al., 2021) benchmarks, employing the pass@10 metric for evaluation.

---

[referencia=d7eccd072c35cb31 score=0.012]
              
              
              
            https://github.com/TurkuNLP/Megatron-DeepSpeed introduced by Luukkonen et al. (2023),
which has optimized kernels converted from CUDA to be compatible with AMD ROCm, and has been demonstrated to be a viable solution for large model pretraining on LUMI. The hardware used to train the model is described in detail in Appendix A.3.

Configuration Considering the hardware available and the selected hyperparameters such as batch size, a configuration of 128 nodes was chosen for the training of the model, resulting in a world size of 1024. The training was done using activation checkpointing, a micro batch size of 1, gradient accumulation of 16, and a 3D parallelism strategy of tensor parallel degree 2, pipeline parallel degree 4, resulting in a data parallel degree of 128. This allowed total training cycle throughput of 49618 TFLOPs and 174378 tokens/second.

---

[referencia=d7eccd072c35cb31 score=0.011]
#### Programming Languages

To introduce data representing various programming languages (referred to hereinafter as “code" for short) into our pretraining, we make use of the Starcoder corpus (Li et al., 2023), a processed subset of The Stack corpus<sup>3</sup><sup>3</sup>
              3
              
              
              
            https://huggingface.co/datasets/bigcode/the-stack (Kocetkov et al., 2023). The original corpus consists of 208B tokens, which we oversample 1.5x so that approximately a third of the tokens seen during pretraining represent code.

#### Cross-lingual data

We introduce a cross-lingual signal into pretraining by including translation examples from OPUS (Tiedemann, 2009). Specifically, we use the English-Finnish examples from the Tatoeba dataset (Tiedemann, 2020) to generate instruction-formatted translation examples. The Tatoeba training data was reformatted into a minimalistic instruction-following format by recasting each English-Finnish translation pair into a document with the following format:

```
<|user|>Translate into Finnish: {{en}}
<|assistant|>{{fi}}
```
Where {{en}} and {{fi}} are the English and Finnish texts (resp.) of the translation pair. We additionally reverse the translation order (i.e., Finnish to English instead of English to Finnish) for a total of two documents for each sentence pair. No weighting is applied to the approximately 8B tokens of cross-lingual data, which thus represents slightly under 1% of the pretraining tokens.

---

[referencia=d7eccd072c35cb31 score=0.010]
- Ahuja et al. (2023)
Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Segal, Mohamed Ahmed, et al. 2023.
Mega: Multilingual evaluation of generative ai.
In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* , pages 4232–4267.
- Al-Khateeb et al. (2023)
Faisal Al-Khateeb, Nolan Dey, Daria Soboleva, and Joel Hestness. 2023.
Position Interpolation Improves ALiBi Extrapolation.
*arXiv preprint arXiv:2310.13017* .
- Ali et al. (2023)
Mehdi Ali, Michael Fromm, Klaudia Thellmann, Richard Rutmann, Max Lübbering, Johannes Leveling, Katrin Klug, Jan Ebert, Niclas Doll, Jasper Schulze Buschhoff, et al. 2023.
Tokenizer Choice For LLM Training: Negligible or Crucial?
*arXiv preprint arXiv:2310.08754* .
- Almazrouei et al. (2023)
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra Cojocaru, Mérouane Debbah, Étienne Goffinet, Daniel Hesslow, Julien Launay, Quentin Malartic, et al. 2023.
The Falcon series of open language models.
*arXiv preprint arXiv:2311.16867* .
- Alves et al. (2024) Duarte M. Alves, José Pombal, Nuno M. Guerreiro, Pedro H. Martins, João Alves, Amin Farajian, Ben Peters, Ricardo Rei, Patrick Fernandes, Sweta Agrawal, Pierre Colombo, José G. C. de Souza, and André F. T. Martins. 2024. Tower: An open multilingual large language model for translation-related tasks.