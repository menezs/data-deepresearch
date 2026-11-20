[referencia=32f3c7d144f036a0 score=0.770]
In this paper, we improve the fine-tuning based approaches by proposing BERT: **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked 

word based only on its context. Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer. In addition to the masked language model, we also use a “next sentence prediction” task that jointly pretrains text-pair representations. The contributions of our paper are as follows: 

- We demonstrate the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional language models for pre-training, BERT uses masked language models to enable pretrained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. 

- We show that pre-trained representations reduce the need for many heavily-engineered taskspecific architectures. BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level _and_ token-level tasks, outperforming many task-specific architectures. 

- BERT advances the state of the art for eleven NLP tasks. The code and pre-trained models are available at https://github.com/ google-research/bert.

---

[referencia=32f3c7d144f036a0 score=0.237]
### **3.1 Pre-training BERT** 

Unlike Peters et al. (2018a) and Radford et al. (2018), we do not use traditional left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train BERT using two unsupervised tasks, described in this section. This step is presented in the left part of Figure 1. 

**Task #1: Masked LM** Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-toright and a right-to-left model. Unfortunately, standard conditional language models can only be trained left-to-right _or_ right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself”, and the model could trivially predict the target word in a multi-layered context. 

former is often referred to as a “Transformer encoder” while the left-context-only version is referred to as a “Transformer decoder” since it can be used for text generation. 

In order to train a deep bidirectional representation, we simply mask some percentage of the input tokens at random, and then predict those masked tokens. We refer to this procedure as a “masked LM” (MLM), although it is often referred to as a _Cloze_ task in the literature (Taylor, 1953). In this case, the final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM. In all of our experiments, we mask 15% of all WordPiece tokens in each sequence at random. In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input.

---

[referencia=32f3c7d144f036a0 score=0.064]
ELMo and its predecessor (Peters et al., 2017, 2018a) generalize traditional word embedding research along a different dimension. They extract _context-sensitive_ features from a left-to-right and a right-to-left language model. The contextual representation of each token is the concatenation of the left-to-right and right-to-left representations. When integrating contextual word embeddings with existing task-specific architectures, ELMo advances the state of the art for several major NLP benchmarks (Peters et al., 2018a) including question answering (Rajpurkar et al., 2016), sentiment analysis (Socher et al., 2013), and named entity recognition (Tjong Kim Sang and De Meulder, 2003). Melamud et al. (2016) proposed learning contextual representations through a task to predict a single word from both left and right context using LSTMs. Similar to ELMo, their model is feature-based and not deeply bidirectional. Fedus et al. (2018) shows that the cloze task can be used to improve the robustness of text generation models.

---

[referencia=32f3c7d144f036a0 score=0.039]
layer in the output. We use the representation of the first sub-token as the input to the token-level 

To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers _without_ fine-tuning any parameters of BERT. These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer. 

Results are presented in Table 7. BERTLARGE performs competitively with state-of-the-art methods. The best performing method concatenates the token representations from the top four hidden layers of the pre-trained Transformer, which is only 0.3 F1 behind fine-tuning the entire model. This demonstrates that BERT is effective for both finetuning and feature-based approaches. 

## **6 Conclusion** 

|Hy|perpar|ams||Dev Se|t Accura|cy|
|---|---|---|---|---|---|---|
|#L|#H|#A|LM (ppl)|MNLI-m|MRPC|SST-2|
|3|768|12|5.84|77.9|79.8|88.4|
|6|768|3|5.24|80.6|82.2|90.7|
|6|768|12|4.68|81.9|84.8|91.3|
|12|768|12|3.99|84.4|86.7|92.9|
|12|1024|16|3.54|85.7|86.9|93.3|
|24|1024|16|3.23|86.6|87.8|93.7|



Table 6: Ablation over BERT model size. #L = the number of layers; #H = hidden size; #A = number of attention heads. “LM (ppl)” is the masked LM perplexity of held-out training data. 

Recent empirical improvements due to transfer learning with language models have demonstrated that rich, unsupervised pre-training is an integral part of many language understanding systems. In particular, these results enable even low-resource tasks to benefit from deep unidirectional architectures. Our major contribution is further generalizing these findings to deep _bidirectional_ architectures, allowing the same pre-trained model to successfully tackle a broad set of NLP tasks.

---

[referencia=32f3c7d144f036a0 score=0.030]
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

---

[referencia=32f3c7d144f036a0 score=0.028]
### **A.1 Illustration of the Pre-training Tasks** 

We provide examples of the pre-training tasks in the following. 

**Masked LM and the Masking Procedure** Assuming the unlabeled sentence is my dog is hairy, and during the random masking procedure we chose the 4-th token (which corresponding to hairy), our masking procedure can be further illustrated by 

- 80% of the time: Replace the word with the [MASK] token, e.g., my dog is hairy _→_ my dog is [MASK] 

- 10% of the time: Replace the word with a random word, e.g., my dog is hairy _→_ my dog is apple 

- 10% of the time: Keep the word unchanged, e.g., my dog is hairy _→_ my dog is hairy. The purpose of this is to bias the representation towards the actual observed word. 

The advantage of this procedure is that the Transformer encoder does not know which words it will be asked to predict or which have been replaced by random words, so it is forced to keep a distributional contextual representation of _every_ input token. Additionally, because random replacement only occurs for 1.5% of all tokens (i.e., 10% of 15%), this does not seem to harm the model’s language understanding capability. In Section C.2, we evaluate the impact this procedure. 

Compared to standard langauge model training, the masked LM only make predictions on 15% of tokens in each batch, which suggests that more pre-training steps may be required for the model 



<!-- Start of picture text -->
BERT (Ours) OpenAI GPT ELMo<br> T1 T2 ... TN  T1 T2 ...  TN  T1 T2 ...  TN<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br> E1 E2 ...  EN  E1 E2 ...  EN  E1 E2 ...  EN<br><!-- End of picture text -->

---

[referencia=32f3c7d144f036a0 score=0.022]
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

[referencia=32f3c7d144f036a0 score=0.006]
> 5The final model achieves 97%-98% accuracy on NSP. 

> 6The vector _C_ is not a meaningful sentence representation without fine-tuning, since it was trained with NSP. 

|Input|[CLS]|my|dog|is|cute|[SEP]|he|likes|play|##ing|[SEP]|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Token<br>Embeddings|E[CLS]|Emy|Edog|Eis|Ecute|E[SEP]|Ehe|Elikes|Eplay|E##ing|E[SEP]|
|Segment<br>Embeddings|EA|EA|EA|EA|EA|EA|EB|EB|EB|EB|EB|
|Position<br>Embeddings|E0|E1|E2|E3|E4|E5|E6|E7|E8|E9|E10|



Figure 2: BERT input representation. The input embeddings are the sum of the token embeddings, the segmentation embeddings and the position embeddings. 

The NSP task is closely related to representationlearning objectives used in Jernite et al. (2017) and Logeswaran and Lee (2018). However, in prior work, only sentence embeddings are transferred to down-stream tasks, where BERT transfers all parameters to initialize end-task model parameters. 

**Pre-training data** The pre-training procedure largely follows the existing literature on language model pre-training. For the pre-training corpus we use the BooksCorpus (800M words) (Zhu et al., 2015) and English Wikipedia (2,500M words). For Wikipedia we extract only the text passages and ignore lists, tables, and headers. It is critical to use a document-level corpus rather than a shuffled sentence-level corpus such as the Billion Word Benchmark (Chelba et al., 2013) in order to extract long contiguous sequences.

---

[referencia=32f3c7d144f036a0 score=0.005]
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

[referencia=32f3c7d144f036a0 score=0.003]
### **2.2 Unsupervised Fine-tuning Approaches** 

As with the feature-based approaches, the first works in this direction only pre-trained word embedding parameters from unlabeled text (Collobert and Weston, 2008). 

More recently, sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task (Dai and Le, 2015; Howard and Ruder, 2018; Radford et al., 2018). The advantage of these approaches is that few parameters need to be learned from scratch. At least partly due to this advantage, OpenAI GPT (Radford et al., 2018) achieved previously state-of-the-art results on many sentencelevel tasks from the GLUE benchmark (Wang et al., 2018a). Left-to-right language model- 



<!-- Start of picture text -->
NSP Mask LM Mask LM MNLI NER SQuAD Start/End Span<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1 ... TN T[SEP] T1’ ... TM’<br>BERT BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Masked Sentence A Masked Sentence B Question Paragraph<br>Unlabeled Sentence A and B Pair  Question Answer Pair<br>Pre-training Fine-Tuning<br><!-- End of picture text -->

Figure 1: Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architectures are used in both pre-training and fine-tuning. The same pre-trained model parameters are used to initialize models for different down-stream tasks. During fine-tuning, all parameters are fine-tuned. [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). 

ing and auto-encoder objectives have been used for pre-training such models (Howard and Ruder, 2018; Radford et al., 2018; Dai and Le, 2015).

---

[referencia=32f3c7d144f036a0 score=0.002]
- Alan Akbik, Duncan Blythe, and Roland Vollgraf. 2018. Contextual string embeddings for sequence labeling. In _Proceedings of the 27th International Conference on Computational Linguistics_ , pages 1638–1649. 

- Rami Al-Rfou, Dokook Choe, Noah Constant, Mandy Guo, and Llion Jones. 2018. Character-level language modeling with deeper self-attention. _arXiv preprint arXiv:1808.04444_ . 

- Rie Kubota Ando and Tong Zhang. 2005. A framework for learning predictive structures from multiple tasks and unlabeled data. _Journal of Machine Learning Research_ , 6(Nov):1817–1853. 

- Luisa Bentivogli, Bernardo Magnini, Ido Dagan, Hoa Trang Dang, and Danilo Giampiccolo. 2009. The fifth PASCAL recognizing textual entailment challenge. In _TAC_ . NIST. 

- John Blitzer, Ryan McDonald, and Fernando Pereira. 2006. Domain adaptation with structural correspondence learning. In _Proceedings of the 2006 conference on empirical methods in natural language processing_ , pages 120–128. Association for Computational Linguistics. 

- Samuel R. Bowman, Gabor Angeli, Christopher Potts, and Christopher D. Manning. 2015. A large annotated corpus for learning natural language inference. In _EMNLP_ . Association for Computational Linguistics. 

- Peter F Brown, Peter V Desouza, Robert L Mercer, Vincent J Della Pietra, and Jenifer C Lai. 1992. Class-based n-gram models of natural language. _Computational linguistics_ , 18(4):467–479. 

- Daniel Cer, Mona Diab, Eneko Agirre, Inigo LopezGazpio, and Lucia Specia. 2017. Semeval-2017 task 1: Semantic textual similarity multilingual and crosslingual focused evaluation. In _Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)_ , pages 1–14, Vancouver, Canada. Association for Computational Linguistics.

---

[referencia=32f3c7d144f036a0 score=0.002]
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

[referencia=32f3c7d144f036a0 score=0.002]
- Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. 2015. Aligning books and movies: Towards story-like visual explanations by watching movies and reading books. In _Proceedings of the IEEE international conference on computer vision_ , pages 19–27. **Appendix for “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”** 

We organize the appendix into three sections: 

- Additional implementation details for BERT are presented in Appendix A; 

- Additional details for our experiments are presented in Appendix B; and 

- Additional ablation studies are presented in Appendix C. 

We present additional ablation studies for BERT including: 

- Effect of Number of Training Steps; and 

- Ablation for Different Masking Procedures.

---

[referencia=32f3c7d144f036a0 score=0.002]
- William Fedus, Ian Goodfellow, and Andrew M Dai. 2018. Maskgan: Better text generation via filling in the ~~.~~ _arXiv preprint arXiv:1801.07736_ . 

- Dan Hendrycks and Kevin Gimpel. 2016. Bridging nonlinearities and stochastic regularizers with gaussian error linear units. _CoRR_ , abs/1606.08415. 

- Felix Hill, Kyunghyun Cho, and Anna Korhonen. 2016. Learning distributed representations of sentences from unlabelled data. In _Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ . Association for Computational Linguistics. 

- Jeremy Howard and Sebastian Ruder. 2018. Universal language model fine-tuning for text classification. In _ACL_ . Association for Computational Linguistics. 

- Minghao Hu, Yuxing Peng, Zhen Huang, Xipeng Qiu, Furu Wei, and Ming Zhou. 2018. Reinforced mnemonic reader for machine reading comprehension. In _IJCAI_ . 

- Yacine Jernite, Samuel R. Bowman, and David Sontag. 2017. Discourse-based objectives for fast unsupervised sentence representation learning. _CoRR_ , abs/1705.00557. 

- Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. 2017. Triviaqa: A large scale distantly supervised challenge dataset for reading comprehension. In _ACL_ . 

- Ryan Kiros, Yukun Zhu, Ruslan R Salakhutdinov, Richard Zemel, Raquel Urtasun, Antonio Torralba, and Sanja Fidler. 2015. Skip-thought vectors. In _Advances in neural information processing systems_ , pages 3294–3302. 

- Quoc Le and Tomas Mikolov. 2014. Distributed representations of sentences and documents. In _International Conference on Machine Learning_ , pages 1188–1196. 

- Hector J Levesque, Ernest Davis, and Leora Morgenstern. 2011. The winograd schema challenge. In _Aaai spring symposium: Logical formalizations of commonsense reasoning_ , volume 46, page 47.

---

[referencia=32f3c7d144f036a0 score=0.001]
The numbers in the left part of the table represent the probabilities of the specific strategies used during MLM pre-training (BERT uses 80%, 10%, 10%). The right part of the paper represents the Dev set results. For the feature-based approach, we concatenate the last 4 layers of BERT as the features, which was shown to be the best approach in Section 5.3. 

From the table it can be seen that fine-tuning is surprisingly robust to different masking strategies. However, as expected, using only the MASK strategy was problematic when applying the featurebased approach to NER. Interestingly, using only the RND strategy performs much worse than our strategy as well. 

Figure 5: Ablation over number of training steps. This shows the MNLI accuracy after fine-tuning, starting from model parameters that have been pre-trained for _k_ steps. The x-axis is the value of _k_ .

---

[referencia=32f3c7d144f036a0 score=0.001]
### **2.1 Unsupervised Feature-based Approaches** 

Learning widely applicable representations of words has been an active area of research for decades, including non-neural (Brown et al., 1992; Ando and Zhang, 2005; Blitzer et al., 2006) and neural (Mikolov et al., 2013; Pennington et al., 2014) methods. Pre-trained word embeddings are an integral part of modern NLP systems, offering significant improvements over embeddings learned from scratch (Turian et al., 2010). To pretrain word embedding vectors, left-to-right language modeling objectives have been used (Mnih and Hinton, 2009), as well as objectives to discriminate correct from incorrect words in left and right context (Mikolov et al., 2013). 

These approaches have been generalized to coarser granularities, such as sentence embeddings (Kiros et al., 2015; Logeswaran and Lee, 2018) or paragraph embeddings (Le and Mikolov, 2014). To train sentence representations, prior work has used objectives to rank candidate next sentences (Jernite et al., 2017; Logeswaran and Lee, 2018), left-to-right generation of next sentence words given a representation of the previous sentence (Kiros et al., 2015), or denoising autoencoder derived objectives (Hill et al., 2016).

---

[referencia=32f3c7d144f036a0 score=0.001]
# **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** 

**Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova** Google AI Language 

_{_ jacobdevlin,mingweichang,kentonl,kristout _}_ @google.com 

## **Abstract** 

We introduce a new language representation model called **BERT** , which stands for **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. 

BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

---

[referencia=32f3c7d144f036a0 score=0.001]
2017). They were annotated with a score from 1 GLUE submission, we always predicted the ma- 

> to 5 denoting how similar the two sentences are in terms of semantic meaning. 14Note that we only report single-task fine-tuning results in this paper. A multitask fine-tuning approach could poten- **MRPC** Microsoft Research Paraphrase Corpus tially push the performance even further. For example, we did observe substantial improvements on RTE from multiconsists of sentence pairs automatically extracted task training with MNLI. 

from online news sources, with human annotations 

> 15https://gluebenchmark.com/faq 

jority class.

---

[referencia=32f3c7d144f036a0 score=0.001]
We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set. Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on the Dev set. With random restarts, we use the same pre-trained checkpoint but perform different fine-tuning data shuffling and classifier layer initialization.<sup>9</sup> 

Results are presented in Table 1. Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. Note that BERTBASE and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard<sup>10</sup> , BERTLARGE obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8 as of the date of writing. 

We find that BERTLARGE significantly outperforms BERTBASE across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

---

[referencia=32f3c7d144f036a0 score=0.001]
## **1 Introduction** 

Language model pre-training has been shown to be effective for improving many natural language processing tasks (Dai and Le, 2015; Peters et al., 2018a; Radford et al., 2018; Howard and Ruder, 2018). These include sentence-level tasks such as natural language inference (Bowman et al., 2015; Williams et al., 2018) and paraphrasing (Dolan and Brockett, 2005), which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level (Tjong Kim Sang and De Meulder, 2003; Rajpurkar et al., 2016). 

There are two existing strategies for applying pre-trained language representations to downstream tasks: _feature-based_ and _fine-tuning_ . The feature-based approach, such as ELMo (Peters et al., 2018a), uses task-specific architectures that include the pre-trained representations as additional features. The fine-tuning approach, such as the Generative Pre-trained Transformer (OpenAI GPT) (Radford et al., 2018), introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning _all_ pretrained parameters. The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations. 

We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches. The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training. For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani et al., 2017). Such restrictions are sub-optimal for sentence-level tasks, and could be very harmful when applying finetuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions.