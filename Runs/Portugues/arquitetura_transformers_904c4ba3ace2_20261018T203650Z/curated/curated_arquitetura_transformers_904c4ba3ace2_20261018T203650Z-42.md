[referencia=32f3c7d144f036a0 score=0.981]
# **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** 

**Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova** Google AI Language 

_{_ jacobdevlin,mingweichang,kentonl,kristout _}_ @google.com 

## **Abstract** 

We introduce a new language representation model called **BERT** , which stands for **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. 

BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

---

[referencia=32f3c7d144f036a0 score=0.360]
> 8 See (10) in https://gluebenchmark.com/faq. 

|System|MNLI-(m/mm)|QQP|QNLI|SST-2|CoLA|STS-B|MRPC|RTE|**Average**|
|---|---|---|---|---|---|---|---|---|---|
||392k|363k|108k|67k|8.5k|5.7k|3.5k|2.5k|-|
|Pre-OpenAI SOTA|80.6/80.1|66.1|82.3|93.2|35.0|81.0|86.0|61.7|74.0|
|BiLSTM+ELMo+Attn|76.4/76.1|64.8|79.8|90.4|36.0|73.3|84.9|56.8|71.0|
|OpenAI GPT|82.1/81.4|70.3|87.4|91.3|45.4|80.0|82.3|56.0|75.1|
|BERTBASE|84.6/83.4|71.2|90.5|93.5|52.1|85.8|88.9|66.4|79.6|
|BERTLARGE|**86.7/85.9**|**72.1**|**92.7**|**94.9**|**60.5**|**86.5**|**89.3**|**70.1**|**82.1**|



Table 1: GLUE Test results, scored by the evaluation server (https://gluebenchmark.com/leaderboard). The number below each task denotes the number of training examples. The “Average” column is slightly different than the official GLUE score, since we exclude the problematic WNLI set.<sup>8</sup> BERT and OpenAI GPT are singlemodel, single task. F1 scores are reported for QQP and MRPC, Spearman correlations are reported for STS-B, and accuracy scores are reported for the other tasks. We exclude entries that use BERT as one of their components.

---

[referencia=32f3c7d144f036a0 score=0.235]
### **4.1 GLUE** 

The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. Detailed descriptions of GLUE datasets are included in Appendix B.1. 

To fine-tune on GLUE, we represent the input sequence (for single sentence or sentence pairs) as described in Section 3, and use the final hidden vector _C ∈_ R<sup>_H_</sup> corresponding to the first input token ([CLS]) as the aggregate representation. The only new parameters introduced during fine-tuning are classification layer weights _W ∈_ R<sup>_K×H_</sup> , where _K_ is the number of labels. We compute a standard classification loss with _C_ and _W_ , i.e., log(softmax( _CW_<sup>_T_</sup> )). 

> 7For example, the BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score of 91.0%. 

> 8 See (10) in https://gluebenchmark.com/faq.

---

[referencia=32f3c7d144f036a0 score=0.206]
## **4 Experiments** 

In this section, we present BERT fine-tuning results on 11 NLP tasks.

---

[referencia=32f3c7d144f036a0 score=0.188]
We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set. Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on the Dev set. With random restarts, we use the same pre-trained checkpoint but perform different fine-tuning data shuffling and classifier layer initialization.<sup>9</sup> 

Results are presented in Table 1. Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. Note that BERTBASE and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard<sup>10</sup> , BERTLARGE obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8 as of the date of writing. 

We find that BERTLARGE significantly outperforms BERTBASE across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

---

[referencia=32f3c7d144f036a0 score=0.119]
- Erik F Tjong Kim Sang and Fien De Meulder. 2003. Introduction to the conll-2003 shared task: Language-independent named entity recognition. In _CoNLL_ . 

- Joseph Turian, Lev Ratinov, and Yoshua Bengio. 2010. Word representations: A simple and general method for semi-supervised learning. In _Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics_ , ACL ’10, pages 384–394. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. In _Advances in Neural Information Processing Systems_ , pages 6000–6010. 

- Pascal Vincent, Hugo Larochelle, Yoshua Bengio, and Pierre-Antoine Manzagol. 2008. Extracting and composing robust features with denoising autoencoders. In _Proceedings of the 25th international conference on Machine learning_ , pages 1096–1103. ACM. 

- Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2018a. Glue: A multi-task benchmark and analysis platform 

for natural language understanding. In _Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP_ , pages 353–355.

---

[referencia=32f3c7d144f036a0 score=0.070]
### **5.2 Effect of Model Size** 

In this section, we explore the effect of model size on fine-tuning task accuracy. We trained a number of BERT models with a differing number of layers, hidden units, and attention heads, while otherwise using the same hyperparameters and training procedure as described previously. 

Results on selected GLUE tasks are shown in Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks. It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative to the existing literature. For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, A=2) with 235M parameters (Al-Rfou et al., 2018). By contrast, BERTBASE contains 110M parameters and BERTLARGE contains 340M parameters. 

It has long been known that increasing the model size will lead to continual improvements on large-scale tasks such as machine translation and language modeling, which is demonstrated by the LM perplexity of held-out training data shown in Table 6. However, we believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. Peters et al. (2018b) presented 

mixed results on the downstream task impact of increasing the pre-trained bi-LM size from two to four layers and Melamud et al. (2016) mentioned in passing that increasing hidden dimension size from 200 to 600 helped, but increasing further to 1,000 did not bring further improvements. Both of these prior works used a featurebased approach — we hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the taskspecific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small.

---

[referencia=32f3c7d144f036a0 score=0.067]
2017). They were annotated with a score from 1 GLUE submission, we always predicted the ma- 

> to 5 denoting how similar the two sentences are in terms of semantic meaning. 14Note that we only report single-task fine-tuning results in this paper. A multitask fine-tuning approach could poten- **MRPC** Microsoft Research Paraphrase Corpus tially push the performance even further. For example, we did observe substantial improvements on RTE from multiconsists of sentence pairs automatically extracted task training with MNLI. 

from online news sources, with human annotations 

> 15https://gluebenchmark.com/faq 

jority class.

---

[referencia=32f3c7d144f036a0 score=0.048]
> E[CLS][CLS] E11 ... ENN E[SEP][SEP] E1’1’’ ... EM’M’’ E[CLS][CLS] E11 E22 ... ENN [CLS] Tok 1 ... Tok N [SEP] Tok 1 ... TokM [CLS] Tok 1 Tok 2 ... Tok N Question Paragraph Single Sentence 



<!-- Start of picture text -->
BERT<br>E[CLS][CLS] E11 ... ENN  E[SEP][SEP] E1’1’’ ... EM’M’’<br><!-- End of picture text -->



<!-- Start of picture text -->
BERT<br>E[CLS][CLS] E11  E22 ...  ENN<br><!-- End of picture text -->

Figure 4: Illustrations of Fine-tuning BERT on Different Tasks. 

**SST-2** The Stanford Sentiment Treebank is a for whether the sentences in the pair are semantibinary single-sentence classification task consistcally equivalent (Dolan and Brockett, 2005). ing of sentences extracted from movie reviews with human annotations of their sentiment (Socher **RTE** Recognizing Textual Entailment is a biet al., 2013). nary entailment task similar to MNLI, but with much less training data (Bentivogli et al., 2009).<sup>14</sup> 

**CoLA** The Corpus of Linguistic Acceptability is a binary single-sentence classification task, where **WNLI** Winograd NLI is a small natural lanthe goal is to predict whether an English sentence guage inference dataset (Levesque et al., 2011). is linguistically “acceptable” or not (Warstadt The GLUE webpage notes that there are issues et al., 2018). with the construction of this dataset,<sup>15</sup> and every trained system that’s been submitted to GLUE has **STS-B** The Semantic Textual Similarity Benchperformed worse than the 65.1 baseline accuracy mark is a collection of sentence pairs drawn from of predicting the majority class. We therefore exnews headlines and other sources (Cer et al., clude this set to be fair to OpenAI GPT. For our 

2017). They were annotated with a score from 1 GLUE submission, we always predicted the ma-

---

[referencia=32f3c7d144f036a0 score=0.041]
### ablation studies can be found in Appendix C. 

### **5.1 Effect of Pre-training Tasks** 

We demonstrate the importance of the deep bidirectionality of BERT by evaluating two pretraining objectives using exactly the same pretraining data, fine-tuning scheme, and hyperparameters as BERTBASE: 

**No NSP** : A bidirectional model which is trained using the “masked LM” (MLM) but without the “next sentence prediction” (NSP) task. 

**LTR & No NSP** : A left-context-only model which is trained using a standard Left-to-Right (LTR) LM, rather than an MLM. The left-only constraint was also applied at fine-tuning, because removing it introduced a pre-train/fine-tune mismatch that degraded downstream performance. Additionally, this model was pre-trained without the NSP task. This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme. 

We first examine the impact brought by the NSP task. In Table 5, we show that removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1. Next, we evaluate the impact of training bidirectional representations by comparing “No NSP” to “LTR & No NSP”. The LTR model performs worse than the MLM model on all tasks, with large drops on MRPC and SQuAD. 

For SQuAD it is intuitively clear that a LTR model will perform poorly at token predictions, since the token-level hidden states have no rightside context. In order to make a good faith attempt at strengthening the LTR system, we added a randomly initialized BiLSTM on top. This does significantly improve results on SQuAD, but the 

results are still far worse than those of the pretrained bidirectional models. The BiLSTM hurts performance on the GLUE tasks. 

We recognize that it would also be possible to train separate LTR and RTL models and represent each token as the concatenation of the two models, as ELMo does. However: (a) this is twice as expensive as a single bidirectional model; (b) this is non-intuitive for tasks like QA, since the RTL model would not be able to condition the answer on the question; (c) this it is strictly less powerful than a deep bidirectional model, since it can use both left and right context at every layer.

---

[referencia=32f3c7d144f036a0 score=0.040]
- Ciprian Chelba, Tomas Mikolov, Mike Schuster, Qi Ge, Thorsten Brants, Phillipp Koehn, and Tony Robinson. 2013. One billion word benchmark for measuring progress in statistical language modeling. _arXiv preprint arXiv:1312.3005_ . 

- Z. Chen, H. Zhang, X. Zhang, and L. Zhao. 2018. Quora question pairs. 

- Christopher Clark and Matt Gardner. 2018. Simple and effective multi-paragraph reading comprehension. In _ACL_ . 

- Kevin Clark, Minh-Thang Luong, Christopher D Manning, and Quoc Le. 2018. Semi-supervised sequence modeling with cross-view training. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing_ , pages 1914– 1925. 

- Ronan Collobert and Jason Weston. 2008. A unified architecture for natural language processing: Deep neural networks with multitask learning. In _Proceedings of the 25th international conference on Machine learning_ , pages 160–167. ACM. 

- Alexis Conneau, Douwe Kiela, Holger Schwenk, Lo¨ıc Barrault, and Antoine Bordes. 2017. Supervised learning of universal sentence representations from natural language inference data. In _Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing_ , pages 670–680, Copenhagen, Denmark. Association for Computational Linguistics. 

- Andrew M Dai and Quoc V Le. 2015. Semi-supervised sequence learning. In _Advances in neural information processing systems_ , pages 3079–3087. 

- J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. FeiFei. 2009. ImageNet: A Large-Scale Hierarchical Image Database. In _CVPR09_ . 

- William B Dolan and Chris Brockett. 2005. Automatically constructing a corpus of sentential paraphrases. In _Proceedings of the Third International Workshop on Paraphrasing (IWP2005)_ . 

- William Fedus, Ian Goodfellow, and Andrew M Dai. 2018. Maskgan: Better text generation via filling in the ~~.~~ _arXiv preprint arXiv:1801.07736_ .

---

[referencia=32f3c7d144f036a0 score=0.039]
### **B.1 Detailed Descriptions for the GLUE Benchmark Experiments.** 

Our GLUE results in Table1 are obtained from https://gluebenchmark.com/ leaderboard and https://blog. openai.com/language-unsupervised. The GLUE benchmark includes the following datasets, the descriptions of which were originally summarized in Wang et al. (2018a): 

**MNLI** Multi-Genre Natural Language Inference is a large-scale, crowdsourced entailment classification task (Williams et al., 2018). Given a pair of sentences, the goal is to predict whether the second sentence is an _entailment_ , _contradiction_ , or _neutral_ with respect to the first one. 

**QQP** Quora Question Pairs is a binary classification task where the goal is to determine if two questions asked on Quora are semantically equivalent (Chen et al., 2018). 

**QNLI** Question Natural Language Inference is a version of the Stanford Question Answering Dataset (Rajpurkar et al., 2016) which has been converted to a binary classification task (Wang et al., 2018a). The positive examples are (question, sentence) pairs which do contain the correct answer, and the negative examples are (question, sentence) from the same paragraph which do not contain the answer. 

Class Label 

Class 

Label 

TN 

C T1 ... TN T[SEP] T1’ ... TM’ C T1 T2 ... BERT BERT 



<!-- Start of picture text -->
BERT<br><!-- End of picture text -->



<!-- Start of picture text -->
BERT<br><!-- End of picture text -->

> E[CLS] E1 ... EN E[SEP] E1’ ... EM’ E[CLS] E1 E2 ... EN [CLS] Tok 1 ... Tok N [SEP] Tok 1 ... TokM [CLS][CLS] **Tok 1** Tok 2 ... Tok N Sentence 1 Sentence 2 Single Sentence Start/End Span O B-PER ... O C T1 ... TN T[SEP] T1’ ... TM’ C T1 T2 ... TN BERT BERT

---

[referencia=32f3c7d144f036a0 score=0.022]
## **1 Introduction** 

Language model pre-training has been shown to be effective for improving many natural language processing tasks (Dai and Le, 2015; Peters et al., 2018a; Radford et al., 2018; Howard and Ruder, 2018). These include sentence-level tasks such as natural language inference (Bowman et al., 2015; Williams et al., 2018) and paraphrasing (Dolan and Brockett, 2005), which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level (Tjong Kim Sang and De Meulder, 2003; Rajpurkar et al., 2016). 

There are two existing strategies for applying pre-trained language representations to downstream tasks: _feature-based_ and _fine-tuning_ . The feature-based approach, such as ELMo (Peters et al., 2018a), uses task-specific architectures that include the pre-trained representations as additional features. The fine-tuning approach, such as the Generative Pre-trained Transformer (OpenAI GPT) (Radford et al., 2018), introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning _all_ pretrained parameters. The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations. 

We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches. The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training. For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani et al., 2017). Such restrictions are sub-optimal for sentence-level tasks, and could be very harmful when applying finetuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions.

---

[referencia=32f3c7d144f036a0 score=0.019]
- Alan Akbik, Duncan Blythe, and Roland Vollgraf. 2018. Contextual string embeddings for sequence labeling. In _Proceedings of the 27th International Conference on Computational Linguistics_ , pages 1638–1649. 

- Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, and Llion Jones. 2018. Character-level language modeling with deeper self-attention. _arXiv preprint arXiv:1808.04444_ . 

- Rie Kubota Ando and Tong Zhang. 2005. A framework for learning predictive structures from multiple tasks and unlabeled data. _Journal of Machine Learning Research_ , 6(Nov):1817–1853. 

- Luisa Bentivogli, Bernardo Magnini, Ido Dagan, Hoa Trang Dang, and Danilo Giampiccolo. 2009. The fifth PASCAL recognizing textual entailment challenge. In _TAC_ . NIST. 

- John Blitzer, Ryan McDonald, and Fernando Pereira. 2006. Domain adaptation with structural correspondence learning. In _Proceedings of the 2006 conference on empirical methods in natural language processing_ , pages 120–128. Association for Computational Linguistics. 

- Samuel R. Bowman, Gabor Angeli, Christopher Potts, and Christopher D. Manning. 2015. A large annotated corpus for learning natural language inference. In _EMNLP_ . Association for Computational Linguistics. 

- Peter F Brown, Peter V Desouza, Robert L Mercer, Vincent J Della Pietra, and Jenifer C Lai. 1992. Class-based n-gram models of natural language. _Computational linguistics_ , 18(4):467–479. 

- Daniel Cer, Mona Diab, Eneko Agirre, Inigo LopezGazpio, and Lucia Specia. 2017. Semeval-2017 task 1: Semantic textual similarity multilingual and crosslingual focused evaluation. In _Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)_ , pages 1–14, Vancouver, Canada. Association for Computational Linguistics.

---

[referencia=32f3c7d144f036a0 score=0.018]
- Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. 2018a. Deep contextualized word representations. In _NAACL_ . 

- Matthew Peters, Mark Neumann, Luke Zettlemoyer, and Wen-tau Yih. 2018b. Dissecting contextual word embeddings: Architecture and representation. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing_ , pages 1499–1509. 

- Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. 2018. Improving language understanding with unsupervised learning. Technical report, OpenAI. 

- Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. Squad: 100,000+ questions for machine comprehension of text. In _Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing_ , pages 2383–2392. 

- Minjoon Seo, Aniruddha Kembhavi, Ali Farhadi, and Hannaneh Hajishirzi. 2017. Bidirectional attention flow for machine comprehension. In _ICLR_ . 

- Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Ng, and Christopher Potts. 2013. Recursive deep models for semantic compositionality over a sentiment treebank. In _Proceedings of the 2013 conference on empirical methods in natural language processing_ , pages 1631–1642. 

- Fu Sun, Linyang Li, Xipeng Qiu, and Yang Liu. 2018. U-net: Machine reading comprehension with unanswerable questions. _arXiv preprint arXiv:1810.06638_ . 

- Wilson L Taylor. 1953. Cloze procedure: A new tool for measuring readability. _Journalism Bulletin_ , 30(4):415–433. 

- Erik F Tjong Kim Sang and Fien De Meulder. 2003. Introduction to the conll-2003 shared task: Language-independent named entity recognition. In _CoNLL_ .

---

[referencia=32f3c7d144f036a0 score=0.010]
### **2.2 Unsupervised Fine-tuning Approaches** 

As with the feature-based approaches, the first works in this direction only pre-trained word embedding parameters from unlabeled text (Collobert and Weston, 2008). 

More recently, sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task (Dai and Le, 2015; Howard and Ruder, 2018; Radford et al., 2018). The advantage of these approaches is that few parameters need to be learned from scratch. At least partly due to this advantage, OpenAI GPT (Radford et al., 2018) achieved previously state-of-the-art results on many sentencelevel tasks from the GLUE benchmark (Wang et al., 2018a). Left-to-right language model- 



<!-- Start of picture text -->
NSP Mask LM Mask LM MNLI NER SQuAD Start/End Span<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1 ... TN T[SEP] T1’ ... TM’<br>BERT BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Masked Sentence A Masked Sentence B Question Paragraph<br>Unlabeled Sentence A and B Pair  Question Answer Pair<br>Pre-training Fine-Tuning<br><!-- End of picture text -->

Figure 1: Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architectures are used in both pre-training and fine-tuning. The same pre-trained model parameters are used to initialize models for different down-stream tasks. During fine-tuning, all parameters are fine-tuned. [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). 

ing and auto-encoder objectives have been used for pre-training such models (Howard and Ruder, 2018; Radford et al., 2018; Dai and Le, 2015).

---

[referencia=32f3c7d144f036a0 score=0.008]
- Lajanugen Logeswaran and Honglak Lee. 2018. An efficient framework for learning sentence representations. In _International Conference on Learning Representations_ . 

- Bryan McCann, James Bradbury, Caiming Xiong, and Richard Socher. 2017. Learned in translation: Contextualized word vectors. In _NIPS_ . 

- Oren Melamud, Jacob Goldberger, and Ido Dagan. 2016. context2vec: Learning generic context embedding with bidirectional LSTM. In _CoNLL_ . 

- Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, and Jeff Dean. 2013. Distributed representations of words and phrases and their compositionality. In _Advances in Neural Information Processing Systems 26_ , pages 3111–3119. Curran Associates, Inc. 

- Andriy Mnih and Geoffrey E Hinton. 2009. A scalable hierarchical distributed language model. In D. Koller, D. Schuurmans, Y. Bengio, and L. Bottou, editors, _Advances in Neural Information Processing Systems 21_ , pages 1081–1088. Curran Associates, Inc. 

- Ankur P Parikh, Oscar T¨ackstr¨om, Dipanjan Das, and Jakob Uszkoreit. 2016. A decomposable attention model for natural language inference. In _EMNLP_ . 

- Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. Glove: Global vectors for word representation. In _Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1532– 1543. 

- Matthew Peters, Waleed Ammar, Chandra Bhagavatula, and Russell Power. 2017. Semi-supervised sequence tagging with bidirectional language models. In _ACL_ . 

- Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer. 2018a. Deep contextualized word representations. In _NAACL_ .

---

[referencia=32f3c7d144f036a0 score=0.008]
- Wei Wang, Ming Yan, and Chen Wu. 2018b. Multigranularity hierarchical attention fusion networks for reading comprehension and question answering. In _Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_ . Association for Computational Linguistics. 

- Alex Warstadt, Amanpreet Singh, and Samuel R Bowman. 2018. Neural network acceptability judgments. _arXiv preprint arXiv:1805.12471_ . 

- Adina Williams, Nikita Nangia, and Samuel R Bowman. 2018. A broad-coverage challenge corpus for sentence understanding through inference. In _NAACL_ . 

- Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. 2016. Google’s neural machine translation system: Bridging the gap between human and machine translation. _arXiv preprint arXiv:1609.08144_ . 

- Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. 2014. How transferable are features in deep neural networks? In _Advances in neural information processing systems_ , pages 3320–3328. 

- Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui Zhao, Kai Chen, Mohammad Norouzi, and Quoc V Le. 2018. QANet: Combining local convolution with global self-attention for reading comprehension. In _ICLR_ . 

- Rowan Zellers, Yonatan Bisk, Roy Schwartz, and Yejin Choi. 2018. Swag: A large-scale adversarial dataset for grounded commonsense inference. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ .

---

[referencia=32f3c7d144f036a0 score=0.007]
### **4.2 SQuAD v1.1** 

The Stanford Question Answering Dataset (SQuAD v1.1) is a collection of 100k crowdsourced question/answer pairs (Rajpurkar et al., 2016). Given a question and a passage from 

> 9The GLUE data set distribution does not include the Test labels, and we only made a single GLUE evaluation server submission for each of BERTBASE and BERTLARGE. 10https://gluebenchmark.com/leaderboard 

Wikipedia containing the answer, the task is to predict the answer text span in the passage. 

As shown in Figure 1, in the question answering task, we represent the input question and passage as a single packed sequence, with the question using the A embedding and the passage using the B embedding. We only introduce a start vector _S ∈_ R<sup>_H_</sup> and an end vector _E ∈_ R<sup>_H_</sup> during fine-tuning. The probability of word _i_ being the start of the answer span is computed as a dot product between _Ti_ and _S_ followed by a softmax over all of the words in the paragraph: _Pi_ = <u>�</u> _<u>ej</u>_<sup>_Se·STi·Tj_.</sup> The analogous formula is used for the end of the answer span. The score of a candidate span from position _i_ to position _j_ is defined as _S·Ti_ + _E·Tj_ , and the maximum scoring span where _j ≥ i_ is used as a prediction. The training objective is the sum of the log-likelihoods of the correct start and end positions. We fine-tune for 3 epochs with a learning rate of 5e-5 and a batch size of 32.

---

[referencia=32f3c7d144f036a0 score=0.005]
### **C.2 Ablation for Different Masking Procedures** 

In Section 3.1, we mention that BERT uses a mixed strategy for masking the target tokens when pre-training with the masked language model (MLM) objective. The following is an ablation study to evaluate the effect of different masking strategies. 



<!-- Start of picture text -->
84<br>82<br>80<br>78<br>BERTBASE (Masked LM)<br>76 BERTBASE (Left-to-Right)<br>200 400 600 800 1 , 000<br>Pre-training Steps (Thousands)<br>MNLI Dev Accuracy<br><!-- End of picture text -->

Note that the purpose of the masking strategies is to reduce the mismatch between pre-training and fine-tuning, as the [MASK] symbol never appears during the fine-tuning stage. We report the Dev results for both MNLI and NER. For NER, we report both fine-tuning and feature-based approaches, as we expect the mismatch will be amplified for the feature-based approach as the model will not have the chance to adjust the representations. 

|Ma|sking Ra|tes||Dev Set Results|
|---|---|---|---|---|
|MASK|SAME|RND|MNLI|NER|
||||Fine-tune|Fine-tune Feature-based|
|80%|10%|10%|84.2|95.4<br>94.9|
|100%|0%|0%|84.3|94.9<br>94.0|
|80%|0%|20%|84.1|95.2<br>94.6|
|80%|20%|0%|84.4|95.2<br>94.7|
|0%|20%|80%|83.7|94.8<br>94.6|
|0%|0%|100%|83.6|94.9<br>94.6|



Table 8: Ablation over different masking strategies. 

The results are presented in Table 8. In the table, MASK means that we replace the target token with the [MASK] symbol for MLM; SAME means that we keep the target token as is; RND means that we replace the target token with another random token.