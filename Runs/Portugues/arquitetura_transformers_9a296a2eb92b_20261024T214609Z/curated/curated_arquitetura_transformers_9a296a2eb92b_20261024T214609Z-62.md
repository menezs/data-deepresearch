[referencia=0e79d837309e23ac score=0.966]
## **BERT** 

▶ The BERT architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. [2017]. 

▶ In this work, denote the number of layers (i.e., Transformer blocks) as _L_ , the hidden size as _H_ , and the number of self-attention heads as _A_ . ▶ **BASE** model: _L_ = 12, _H_ = 768, _A_ = 12, Total Parameters = 110M. 

▶ **LARGE** model: _L_ = 24, _H_ = 1024, _A_ = 16, Total Parameters = 340M. 

[Vaswani et al., 2017] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, �L. Kaiser, and I. Polosukhin. Attention is all you need. In Advances in Neural Information Processing Systems (NeurIPS), volume 30, pages 5998–6008, Long Beach, California, USA, 2017. 

**18/33** 

## **Input Representations** 

|Input|[CLS]|my|dog|is|cute|[SEP]|he|likes|play|##ing|[SEP]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Token<br>Embeddings|E[CLS]|Emy|Edog|Eis|Ecute|E[SEP]|Ehe|Elikes|Eplay|E##ing|E[SEP]|
|Segment<br>Embeddings|EA|EA|EA|EA|EA|EA|EB|EB|EB|EB|EB|
|Position<br>Embeddings|E0|E1|E2|E3|E4|E5|E6|E7|E8|E9|E10|



- Both a single sentence and a pair of sentences, e.g., _⟨_ Question, Answer _⟩_ are represented in one token sequence. 

- The WordPiece embeddings with a 30,000 token vocabulary are used. 

- Some special tokens, e.g., `[SEP]` and `[CLS]` , exist. 

**19/33**

---

[referencia=0e79d837309e23ac score=0.056]
# **A Machine Learning Model** 

**13/33** 

## **Main Ideas** 

▶ **Bidirectional representation** : A left-to-right architecture, at which every token can only attend to previous tokens, is limited, because some tasks require incorporating context from both directions. 

- **Pre-training, then fine-tuning** : It reduces the need for many heavily-engineered task-specific architectures. 

**14/33** 

## **Bidirectional Recurrent Neural Networks** 



Figure 1: Illustration of bidirectional recurrent neural networks. 

- It has a recurrent connection, similar to the vanilla recurrent neural network. 

- Compared to the vanilla recurrent neural network, a sequence of input instances is processed by considering forward and backward directions. 

Figure 1 is taken from [Schuster and Paliwal, 1997]. 

- [Schuster and Paliwal, 1997] M. Schuster and K. K. Paliwal. Bidirectional recurrent neural networks. IEEE Transactions on Signal Processing, 45(11): 2673–2681, 1997. 

**15/33** 

## **Transformer** 



Figure 2: Transformer. 

Figure 2 is taken from [Vaswani et al., 2017]. 

**16/33** 

## **BERT** 



<!-- Start of picture text -->
NSP Mask LM Mask LM MNLI NER SQuAD Start/End Span<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1 ... TN T[SEP] T1’ ... TM’<br>BERT BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Masked Sentence A Masked Sentence B Question Paragraph<br>Unlabeled Sentence A and B Pair  Question Answer Pair<br>Pre-training Fine-Tuning<br><!-- End of picture text -->

**17/33**

---

[referencia=0e79d837309e23ac score=0.038]
## **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding [CSED490X] Recent Trends in ML: A Large-Scale Perspective** 

Jungtaek Kim `jtkim@postech.ac.kr` 

POSTECH Pohang 37673, Republic of Korea `https://jungtaek.github.io` March 30, 2022 

**1/33** 

## **Table of Contents** 

Introduction 

Tasks & Datasets 

A Machine Learning Model 

A Learning Scheme Experimental Results 

**2/33** 

# **Introduction** 

**3/33** 

## **Bidirectional Encoder Representations from Transformers (BERT)** 

- BERT has been introduced in the work by Devlin et al. [2018]. 

- Unlike recent language representation models, it is designed to pre-train deep bidirectional representations. 

- It is trained by unlabeled text by jointly conditioning on both left and right 

   - contexts. 

- As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to solve down-stream tasks. 

- [Devlin et al., 2018] J. Devlin, M. Chang, K. Lee, and K. Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018. 

**4/33** 

## **Today’s Lecture** 

- We will cover the tasks and datasets solved in this paper first. 

- Before introducing the BERT model, we will visit a bidirectional RNN model. 

- Eventually, we will study the BERT model and the details of learning schemes, used in this paper. 

- Finally, we will investigate the experimental results. 

**5/33**

---

[referencia=0e79d837309e23ac score=0.026]
## **Pre-Training BERT** 

- Training of BERTBASE was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total). 

- Training of BERTLARGE was performed on 16 Cloud TPUs (64 TPU chips total). 

- Each pre-training took 4 days to complete. 

- To speed up pre-training, the model is pre-trained with sequence length of 128 for 90% of the steps. Then, it is trained with sequence of 512 for the rest 10% of the steps to learn the positional embeddings. 

**24/33** 

## **Fine-Tuning BERT** 

- Fine-tuning is straightforward since the self-attention mechanism allows BERT to model many downstream tasks. 

- BERT uses the self-attention mechanism by encoding a concatenated text pair to effectively include bidirectional cross attention between two sentences. 

- For each task, we simply plug in the task-specific inputs and outputs into BERT and fine-tune all the parameters end-to-end. 

- All of the results in the paper can be replicated in at most 1 hour on a single Cloud TPU, or a few hours on a GPU, starting from the exact same pre-trained model. 

**25/33**

---

[referencia=0e79d837309e23ac score=0.012]
# **Any Questions?** 

**32/33** 

## **References I** 

- J. Devlin, M. Chang, K. Lee, and K. Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. _arXiv preprint arXiv:1810.04805_ , 2018. 

- P. Rajpurkar, J. Zhang, K. Lopyrev, and P. Liang. SQuAD: 100,000+ questions for machine comprehension of text. In _Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , 2016. 

- P. Rajpurkar, R. Jia, and P. Liang. Know what you don’t know: Unanswerable questions for SQuAD. In _Proceedings of the Annual Meeting of the Association for Computational Linguistics_ , pages 784–789, 2018. Short Paper. 

- M. Schuster and K. K. Paliwal. Bidirectional recurrent neural networks. _IEEE Transactions on Signal Processing_ , 45(11):2673–2681, 1997. 

- A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, �L. Kaiser, and I. Polosukhin. Attention is all you need. In _Advances in Neural Information Processing Systems (NeurIPS)_ , volume 30, pages 5998–6008, Long Beach, California, USA, 2017. 

- A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, and S. R. Bowman. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2019. 

- R. Zellers, Y. Bisk, R. Schwartz, and Y. Choi. SWAG: A large-scale adversarial dataset for grounded commonsense inference. In _Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , 2018. 

**33/33**

---

[referencia=0e79d837309e23ac score=0.010]
# **Tasks & Datasets** 

**6/33** 

## **Tasks & Datasets** 

- BERT is tested on four experimental circumstances: 

1. General Language Understanding Evaluation (GLUE) benchmark; 

2. Stanford Question Answering Dataset v1.1 (SQuAD v1.1); 

3. Stanford Question Answering Dataset v2.0 (SQuAD v2.0); 

4. Situations With Adversarial Generations (SWAG) dataset. 

**7/33** 

## **General Language Understanding Evaluation (GLUE)** 

- The GLUE benchmark [Wang et al., 2019] is a collection of diverse natural language understanding tasks. 

### ▶ **MNLI** 

- The Multi-Genre Natural Language Inference Corpus is a crowdsourced collection of sentence pairs with textual entailment annotations. 

- Given a premise sentence and a hypothesis sentence, the task is to predict whether the premise entails the hypothesis (entailment), contradicts the hypothesis (contradiction), or neither (neutral). 

### ▶ **QQP** 

- The Quora Question Pairs dataset is a collection of question pairs from the community question-answering website Quora. 

- The task is to determine whether a pair of questions are semantically equivalent. 

**8/33** 

## **General Language Understanding Evaluation (GLUE)** 

- The GLUE benchmark [Wang et al., 2019] is a collection of diverse natural language understanding tasks. 

### ▶ **QNLI** 

- The Stanford Question Answering Dataset is a question-answering dataset consisting of question-paragraph pairs, where one of the sentences in the paragraph (drawn from Wikipedia) contains the answer to the corresponding question (written by an annotator). 

- The authors convert the task into sentence pair classification by forming a pair between each question and each sentence in the corresponding context, and filtering out pairs with low lexical overlap between the question and the context sentence. 

- The task is to determine whether the context sentence contains the answer to the question. 

**9/33**

---

[referencia=0e79d837309e23ac score=0.005]
## **Fine-Tuning BERT** 



<!-- Start of picture text -->
C T1 ... TN T[SEP] T1’ ... TM’<br>BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br><!-- End of picture text -->



<!-- Start of picture text -->
[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Sentence 1 Sentence 2<br>Start/End Span<br><!-- End of picture text -->



<!-- Start of picture text -->
C T1 ... TN T[SEP] T1’ ... TM’<br>BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br><!-- End of picture text -->



<!-- Start of picture text -->
[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Question Paragraph<br><!-- End of picture text -->



<!-- Start of picture text -->
C T1  T2 ...  TN<br>BERT<br>E[CLS] E1  E2 ...  EN<br>[CLS][CLS] Tok 1 Tok 2 ... Tok N<br><!-- End of picture text -->



<!-- Start of picture text -->
Single Sentence<br>O B-PER ... O<br><!-- End of picture text -->



<!-- Start of picture text -->
C T1  T2 ...  TN<br>BERT<br>E[CLS] E1  E2 ...  EN<br><!-- End of picture text -->



<!-- Start of picture text -->
[CLS] Tok 1 Tok 2 ... Tok N<br>Single Sentence<br><!-- End of picture text -->

**26/33** 

# **Experimental Results** 

**27/33** 

## **Experimental Results** 



**28/33** 

## **Experimental Results** 





**29/33** 

## **Experimental Results** 



**30/33** 

## **Experimental Results** 



**31/33**

---

[referencia=0e79d837309e23ac score=0.002]
# **A Learning Scheme** 

**20/33** 

## **Pre-Training BERT** 

- BERT is pre-trained using two unsupervised tasks. 

- **Task #1 Masked Language Model** : Simply mask some percentage of the input tokens at random, and then predict those masked tokens. 

- **Task #2 Next Sentence Prediction** : Given A and B sentences contiguously, discriminate whether B is the next sentence of A, or not. 

**21/33** 

## **Masked Language Model** 

- 15% of all WordPiece tokens are masked in each sequence at random. 

- If some token is chosen, the selected token is replaced with the `[MASK]` token or a random word, or unchanged. 

- For example, 

   - 80% of the time: Replace the word with the `[MASK]` token 

`my dog is hairy` _→_ `my dog is [MASK]` , 

10% of the time: Replace the word with a random word 

`my dog is hairy` _→_ `my dog is apple` , 

10% of the time: Keep the word unchanged 

`my dog is hairy` _→_ `my dog is hairy` . 

**22/33** 

## **Next Sentence Prediction** 

▶ Many important down-stream tasks such as question answering and natural language inference are based on understanding the relationship between two sentences. 

- For example, 

Input: `[CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP]` 

Label: `IsNext` 

or 

Input: `[CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP]` 

Label: `NotNext` 

**23/33**

---

[referencia=0e79d837309e23ac score=0.000]
## **General Language Understanding Evaluation (GLUE)** 

- The GLUE benchmark [Wang et al., 2019] is a collection of diverse natural language understanding tasks. 

### ▶ **SST-2** 

- The Stanford Sentiment Treebank consists of sentences from movie reviews and human annotations of their sentiment. 

- The task is to predict the sentiment of a given sentence. 

**10/33** 

## **Stanford Question Answering Dataset (SQuAD) v1.1 & v2.0** 

- SQuAD v1.1 [Rajpurkar et al., 2016] is a collection of 100k crowdsourced question and answer pairs. 

- Given a question and a passage from Wikipedia containing the answer, the SQuAD v1.1 task is to predict the answer text span in the passage. 

▶ The SQuAD v2.0 [Rajpurkar et al., 2018] task extends the SQuAD v1.1 problem definition by allowing for the possibility that no short answer exists in the provided paragraph, making the problem more realistic. 



**11/33** 

## **Situations With Adversarial Generations (SWAG)** 

▶ SWAG [Zellers et al., 2018] contains 113k sentence-pair completion examples that evaluate grounded common-sense inference. 

- Given a sentence, the task is to choose the most plausible continuation among four choices. 



**12/33**