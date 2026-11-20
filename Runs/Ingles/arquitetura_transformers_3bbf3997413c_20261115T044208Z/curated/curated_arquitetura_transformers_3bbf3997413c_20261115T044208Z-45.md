[referencia=a3e86ad05f37e40d score=0.468]
## **3 Framework** 

Our training procedure consists of two stages. The first stage is learning a high-capacity language model on a large corpus of text. This is followed by a fine-tuning stage, where we adapt the model to a discriminative task with labeled data. 

### **3.1 Unsupervised pre-training** 

Given an unsupervised corpus of tokens _U_ = _{u_ 1 _, . . . , un}_ , we use a standard language modeling objective to maximize the following likelihood: 



where _k_ is the size of the context window, and the conditional probability _P_ is modeled using a neural network with parameters Θ. These parameters are trained using stochastic gradient descent [51]. 

In our experiments, we use a multi-layer _Transformer decoder_ [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens: 





where _U_ = ( _u−k, . . . , u−_ 1) is the context vector of tokens, _n_ is the number of layers, _We_ is the token embedding matrix, and _Wp_ is the position embedding matrix.

---

[referencia=a3e86ad05f37e40d score=0.181]
but is shuffled at a sentence level - destroying long-range structure. Our language model achieves a very low token level perplexity of 18.4 on this corpus. 

**Model specifications** Our model largely follows the original transformer work [62]. We trained a 12-layer decoder-only transformer with masked self-attention heads (768 dimensional states and 12 attention heads). For the position-wise feed-forward networks, we used 3072 dimensional inner states. We used the Adam optimization scheme [27] with a max learning rate of 2.5e-4. The learning rate was increased linearly from zero over the first 2000 updates and annealed to 0 using a cosine schedule. We train for 100 epochs on minibatches of 64 randomly sampled, contiguous sequences of 512 tokens. Since layernorm [2] is used extensively throughout the model, a simple weight initialization of _N_ (0 _,_ 0 _._ 02) was sufficient. We used a bytepair encoding (BPE) vocabulary with 40,000 merges [53] and residual, embedding, and attention dropouts with a rate of 0.1 for regularization. We also employed a modified version of L2 regularization proposed in [37], with _w_ = 0 _._ 01 on all non bias or gain weights. For the activation function, we used the Gaussian Error Linear Unit (GELU) [18]. We used learned position embeddings instead of the sinusoidal version proposed in the original work. We use the _ftfy_ library<sup>2</sup> to clean the raw text in BooksCorpus, standardize some punctuation and whitespace, and use the _spaCy_ tokenizer.<sup>3</sup> 

**Fine-tuning details** Unless specified, we reuse the hyperparameter settings from unsupervised pre-training. We add dropout to the classifier with a rate of 0.1. For most tasks, we use a learning rate of 6.25e-5 and a batchsize of 32. Our model finetunes quickly and 3 epochs of training was sufficient for most cases. We use a linear learning rate decay schedule with warmup over 0.2% of training. _λ_ was set to 0.5.

---

[referencia=a3e86ad05f37e40d score=0.115]
### **3.2 Supervised fine-tuning** 

After training the model with the objective in Eq. 1, we adapt the parameters to the supervised target task. We assume a labeled dataset _C_ , where each instance consists of a sequence of input tokens, _x_<sup>1</sup> _, . . . , x_<sup>_m_</sup> , along with a label _y_ . The inputs are passed through our pre-trained model to obtain the final transformer block’s activation _h_<sup>_m_</sup> _l_<sup>, which is then fed into an added linear output layer with</sup> parameters _Wy_ to predict _y_ : 



This gives us the following objective to maximize: 



We additionally found that including language modeling as an auxiliary objective to the fine-tuning helped learning by (a) improving generalization of the supervised model, and (b) accelerating convergence. This is in line with prior work [50, 43], who also observed improved performance with such an auxiliary objective. Specifically, we optimize the following objective (with weight _λ_ ): 



Overall, the only extra parameters we require during fine-tuning are _Wy_ , and embeddings for delimiter tokens (described below in Section 3.3). 

3 





Figure 1: **(left)** Transformer architecture and training objectives used in this work. **(right)** Input transformations for fine-tuning on different tasks. We convert all structured inputs into token sequences to be processed by our pre-trained model, followed by a linear+softmax layer.

---

[referencia=a3e86ad05f37e40d score=0.100]
### **3.3 Task-specific input transformations** 

For some tasks, like text classification, we can directly fine-tune our model as described above. Certain other tasks, like question answering or textual entailment, have structured inputs such as ordered sentence pairs, or triplets of document, question, and answers. Since our pre-trained model was trained on contiguous sequences of text, we require some modifications to apply it to these tasks. Previous work proposed learning task specific architectures on top of transferred representations [44]. Such an approach re-introduces a significant amount of task-specific customization and does not use transfer learning for these additional architectural components. Instead, we use a traversal-style approach [52], where we convert structured inputs into an ordered sequence that our pre-trained model can process. These input transformations allow us to avoid making extensive changes to the architecture across tasks. We provide a brief description of these input transformations below and Figure 1 provides a visual illustration. All transformations include adding randomly initialized start and end tokens ( _⟨s⟩_ , _⟨e⟩_ ). 

> **Textual entailment** For entailment tasks, we concatenate the premise _p_ and hypothesis _h_ token sequences, with a delimiter token ($) in between. 

**Similarity** For similarity tasks, there is no inherent ordering of the two sentences being compared. To reflect this, we modify the input sequence to contain both possible sentence orderings (with a delimiter in between) and process each independently to produce two sequence representations _h_<sup>_m_</sup> _l_ which are added element-wise before being fed into the linear output layer. 

**Question Answering and Commonsense Reasoning** For these tasks, we are given a context document _z_ , a question _q_ , and a set of possible answers _{ak}_ . We concatenate the document context and question with each possible answer, adding a delimiter token in between to get [ _z_ ; _q_ ; $; _ak_ ]. Each of these sequences are processed independently with our model and then normalized via a softmax layer to produce an output distribution over possible answers.

---

[referencia=a3e86ad05f37e40d score=0.077]
For CoLA (linguistic acceptability), examples are scored as the average token log-probability the generative model assigns and predictions are made by thresholding. For SST-2 (sentiment analysis), we append the token _very_ to each example and restrict the language model’s output distribution to only the words _positive_ and _negative_ and guess the token it assigns higher probability to as the prediction. For RACE (question answering), we pick the answer the generative model assigns the highest average token log-probability when conditioned on the document and question. For DPRD [46] (winograd schemas), we replace the definite pronoun with the two possible referrents and predict the resolution that the generative model assigns higher average token log-probability to the rest of the sequence after the substitution. 

**Ablation studies** We perform three different ablation studies (Table 5). First, we examine the performance of our method without the auxiliary LM objective during fine-tuning. We observe that the auxiliary objective helps on the NLI tasks and QQP. Overall, the trend suggests that larger datasets benefit from the auxiliary objective but smaller datasets do not. Second, we analyze the effect of the Transformer by comparing it with a single layer 2048 unit LSTM using the same framework. We observe a 5.6 average score drop when using the LSTM instead of the Transformer. The LSTM only outperforms the Transformer on one dataset – MRPC. Finally, we also compare with our transformer architecture directly trained on supervised target tasks, without pre-training. We observe that the lack of pre-training hurts performance across all the tasks, resulting in a 14.8% decrease compared to our full model.

---

[referencia=a3e86ad05f37e40d score=0.058]
## **5 Analysis** 

**Impact of number of layers transferred** We observed the impact of transferring a variable number of layers from unsupervised pre-training to the supervised target task. Figure 2(left) illustrates the performance of our approach on MultiNLI and RACE as a function of the number of layers transferred. We observe the standard result that transferring embeddings improves performance and that each transformer layer provides further benefits up to 9% for full transfer on MultiNLI. This indicates that each layer in the pre-trained model contains useful functionality for solving target tasks. 





Figure 2: ( **left** ) Effect of transferring increasing number of layers from the pre-trained language model on RACE and MultiNLI. ( **right** ) Plot showing the evolution of zero-shot performance on different tasks as a function of LM pre-training updates. Performance per task is normalized between a random guess baseline and the current state-of-the-art with a single model. 

**Zero-shot Behaviors** We’d like to better understand why language model pre-training of transformers is effective. A hypothesis is that the underlying generative model learns to perform many of the tasks we evaluate on in order to improve its language modeling capability and that the more structured 

7 

Table 5: Analysis of various model ablations on different tasks. Avg. score is a unweighted average of all the results. ( _mc_ = Mathews correlation, _acc_ =Accuracy, _pc_ =Pearson correlation)

---

[referencia=a3e86ad05f37e40d score=0.049]
### **4.1 Setup** 

**Unsupervised pre-training** We use the BooksCorpus dataset [71] for training the language model. It contains over 7,000 unique unpublished books from a variety of genres including Adventure, Fantasy, and Romance. Crucially, it contains long stretches of contiguous text, which allows the generative model to learn to condition on long-range information. An alternative dataset, the 1B Word Benchmark, which is used by a similar approach, ELMo [44], is approximately the same size 

4 

Table 1: A list of the different tasks and datasets used in our experiments. 

|**Task**|**Datasets**|
|---|---|
|Natural language inference|SNLI [5], MultiNLI [66], Question NLI [64], RTE [4], SciTail [25]|
|Question Answering|RACE [30], Story Cloze [40]|
|Sentence similarity|MSR Paraphrase Corpus [14], Quora Question Pairs [9], STS Benchmark [6]|
|Classifcation|Stanford Sentiment Treebank-2 [54], CoLA [65]|



but is shuffled at a sentence level - destroying long-range structure. Our language model achieves a very low token level perplexity of 18.4 on this corpus.

---

[referencia=a3e86ad05f37e40d score=0.043]
**Classification** Finally, we also evaluate on two different text classification tasks. The Corpus of Linguistic Acceptability (CoLA) [65] contains expert judgements on whether a sentence is grammatical or not, and tests the innate linguistic bias of trained models. The Stanford Sentiment Treebank (SST-2) [54], on the other hand, is a standard binary classification task. Our model obtains an score of 45.4 on CoLA, which is an especially big jump over the previous best result of 35.0, showcasing the innate linguistic bias learned by our model. The model also achieves 91.3% accuracy on SST-2, which is competitive with the state-of-the-art results. We also achieve an overall score of 72.8 on the GLUE benchmark, which is significantly better than the previous best of 68.9. 

6 

Table 4: Semantic similarity and classification results, comparing our model with current state-of-theart methods. All task evaluations in this table were done using the GLUE benchmark. ( _mc_ = Mathews correlation, _acc_ =Accuracy, _pc_ =Pearson correlation) 

|**Method**|**Classif**|**cation**|**Seman**|**tic Simil**|**arity**|**GLUE**|
|---|---|---|---|---|---|---|
||CoLA<br>(mc)|SST2<br>(acc)|MRPC<br>(F1)|STSB<br>(pc)|QQP<br>(F1)||
|Sparse byte mLSTM [16]|-|**93.2**|-|-|-|-|
|TF-KLD [23]|-|-|**86.0**|-|-|-|
|ECNU (mixed ensemble) [60]|-|-|-|81.0|-|-|
|Single-task BiLSTM + ELMo + Attn [64]|35.0|90.2|80.2|55.5|66.1|64.8|
|Multi-task BiLSTM + ELMo + Attn [64]|18.9|91.6|83.5|72.8|63.3|68.9|
|Finetuned Transformer LM (ours)|**45.4**|91.3|82.3|**82.0**|**70.3**|**72.8**|

---

[referencia=a3e86ad05f37e40d score=0.038]
5 

Table 2: Experimental results on natural language inference tasks, comparing our model with current state-of-the-art methods. 5x indicates an ensemble of 5 models. All datasets use accuracy as the evaluation metric. 

|Method|MNLI-m|MNLI-mm|SNLI|SciTail|QNLI|RTE|
|---|---|---|---|---|---|---|
|ESIM + ELMo [44] (5x)|-|-|89.3|-|-|-|
|CAFE [58] (5x)|80.2|79.0|89.3|-|-|-|
|Stochastic Answer Network [35] (3x)|80.6|80.1|-|-|-|-|
|CAFE [58]|78.7|77.9|88.5|83.3|||
|GenSen [64]|71.4|71.3|-|-|82.3|59.2|
|Multi-task BiLSTM + Attn [64]|72.2|72.1|-|-|82.1|**61.7**|
|Finetuned Transformer LM (ours)|**82.1**|**81.4**|**89.9**|**88.3**|**88.1**|56.0|



Table 3: Results on question answering and commonsense reasoning, comparing our model with current state-of-the-art methods.. 9x means an ensemble of 9 models. 

|Method|Story Cloze|RACE-m|RACE-h|RACE|
|---|---|---|---|---|
|val-LS-skip [55]|76.5|-|-|-|
|Hidden Coherence Model [7]|77.6|-|-|-|
|Dynamic Fusion Net [67] (9x)|-|55.6|49.4|51.2|
|BiAttention MRU [59] (9x)|-|60.2|50.3|53.3|
|Finetuned Transformer LM (ours)|**86.5**|**62.9**|**57.4**|**59.0**|

---

[referencia=a3e86ad05f37e40d score=0.029]
For our model architecture, we use the _Transformer_ [62], which has been shown to perform strongly on various tasks such as machine translation [62], document generation [34], and syntactic parsing [29]. This model choice provides us with a more structured memory for handling long-term dependencies in text, compared to alternatives like recurrent networks, resulting in robust transfer performance across diverse tasks. During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens. As we demonstrate in our experiments, these adaptations enable us to fine-tune effectively with minimal changes to the architecture of the pre-trained model. 

We evaluate our approach on four types of language understanding tasks – natural language inference, question answering, semantic similarity, and text classification. Our general task-agnostic model outperforms discriminatively trained models that employ architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test) [40], 5.7% on question answering (RACE) [30], 1.5% on textual entailment (MultiNLI) [66] and 5.5% on the recently introduced GLUE multi-task benchmark [64]. We also analyzed zero-shot behaviors of the pre-trained model on four different settings and demonstrate that it acquires useful linguistic knowledge for downstream tasks.

---

[referencia=a3e86ad05f37e40d score=0.027]
## **1 Introduction** 

The ability to learn effectively from raw text is crucial to alleviating the dependence on supervised learning in natural language processing (NLP). Most deep learning methods require substantial amounts of manually labeled data, which restricts their applicability in many domains that suffer from a dearth of annotated resources [61]. In these situations, models that can leverage linguistic information from unlabeled data provide a valuable alternative to gathering more annotation, which can be time-consuming and expensive. Further, even in cases where considerable supervision is available, learning good representations in an unsupervised fashion can provide a significant performance boost. The most compelling evidence for this so far has been the extensive use of pretrained word embeddings [10, 39, 42] to improve performance on a range of NLP tasks [8, 11, 26, 45]. 

Leveraging more than word-level information from unlabeled text, however, is challenging for two main reasons. First, it is unclear what type of optimization objectives are most effective at learning text representations that are useful for transfer. Recent research has looked at various objectives such as language modeling [44], machine translation [38], and discourse coherence [22], with each method outperforming the others on different tasks.<sup>1</sup> Second, there is no consensus on the most effective way to transfer these learned representations to the target task. Existing techniques involve a combination of making task-specific changes to the model architecture [43, 44], using intricate learning schemes [21] and adding auxiliary learning objectives [50]. These uncertainties have made it difficult to develop effective semi-supervised learning approaches for language processing. 

> 1https://gluebenchmark.com/leaderboard 

Preprint. Work in progress. 

In this paper, we explore a semi-supervised approach for language understanding tasks using a combination of unsupervised pre-training and supervised fine-tuning. Our goal is to learn a universal representation that transfers with little adaptation to a wide range of tasks. We assume access to a large corpus of unlabeled text and several datasets with manually annotated training examples (target tasks). Our setup does not require these target tasks to be in the same domain as the unlabeled corpus. We employ a two-stage training procedure. First, we use a language modeling objective on the unlabeled data to learn the initial parameters of a neural network model. Subsequently, we adapt these parameters to a target task using the corresponding supervised objective.

---

[referencia=a3e86ad05f37e40d score=0.024]
## **References** 

[1] S. Arora, Y. Liang, and T. Ma. A simple but tough-to-beat baseline for sentence embeddings. 2016. 

8 

[2] J. L. Ba, J. R. Kiros, and G. E. Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. 

|[3] Y. Bengio, P. Lamblin, D. Popovici, and H. Larochelle. Greedy layer-wise training of deep networks. In<br>_Advances in neural information processing systems_, pages 153–160, 2007.|
|---|
|[4] L. Bentivogli, P. Clark, I. Dagan, and D. Giampiccolo. The ffth pascal recognizing textual entailment<br>challenge. In_TAC_, 2009.|
|[5] S. R. Bowman, G. Angeli, C. Potts, and C. D. Manning. A large annotated corpus for learning natural<br>language inference. _EMNLP_, 2015.|
|[6] D. Cer, M. Diab, E. Agirre, I. Lopez-Gazpio, and L. Specia. Semeval-2017 task 1: Semantic textual<br>similarity-multilingual and cross-lingual focused evaluation. _arXiv preprint arXiv:1708.00055_, 2017.|
|[7] S. Chaturvedi, H. Peng, and D. Roth. Story comprehension for predicting what happens next. In_Proceedings_<br>_of the 2017 Conference on Empirical Methods in Natural Language Processing_, pages 1603–1614, 2017.|



[8] D. Chen and C. Manning. A fast and accurate dependency parser using neural networks. In _Proceedings_ 

_of the 2014 conference on empirical methods in natural language processing (EMNLP)_ , pages 740–750, 2014. 

[9] Z. Chen, H. Zhang, X. Zhang, and L. Zhao. Quora question pairs. https://data.quora.com/First-Quora- 

Dataset-Release-Question-Pairs, 2018.

---

[referencia=a3e86ad05f37e40d score=0.017]
biguation. In _Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)_ , volume 2, pages 30–34, 2013. 

[18] D. Hendrycks and K. Gimpel. Bridging nonlinearities and stochastic regularizers with gaussian error linear units. _arXiv preprint arXiv:1606.08415_ , 2016. 

[19] K. M. Hermann, T. Kocisky, E. Grefenstette, L. Espeholt, W. Kay, M. Suleyman, and P. Blunsom. Teaching 

machines to read and comprehend. In _Advances in Neural Information Processing Systems_ , pages 1693– 1701, 2015. 

- [20] G. E. Hinton, S. Osindero, and Y.-W. Teh. A fast learning algorithm for deep belief nets. _Neural computation_ , 18(7):1527–1554, 2006. 

- [21] J. Howard and S. Ruder. Universal language model fine-tuning for text classification. _Association for Computational Linguistics (ACL)_ , 2018. 

- [22] Y. Jernite, S. R. Bowman, and D. Sontag. Discourse-based objectives for fast unsupervised sentence representation learning. _arXiv preprint arXiv:1705.00557_ , 2017. 

- [23] Y. Ji and J. Eisenstein. Discriminative improvements to distributional sentence similarity. In _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing_ , pages 891–896, 2013. 

9

---

[referencia=a3e86ad05f37e40d score=0.016]
### **4.2 Supervised fine-tuning** 

We perform experiments on a variety of supervised tasks including natural language inference, question answering, semantic similarity, and text classification. Some of these tasks are available as part of the recently released GLUE multi-task benchmark [64], which we make use of. Figure 1 provides an overview of all the tasks and datasets. 

**Natural Language Inference** The task of natural language inference (NLI), also known as recognizing textual entailment, involves reading a pair of sentences and judging the relationship between them from one of `entailment` , `contradiction` or `neutral` . Although there has been a lot of recent interest [58, 35, 44], the task remains challenging due to the presence of a wide variety of phenomena like lexical entailment, coreference, and lexical and syntactic ambiguity. We evaluate on five datasets with diverse sources, including image captions (SNLI), transcribed speech, popular fiction, and government reports (MNLI), Wikipedia articles (QNLI), science exams (SciTail) or news articles (RTE). 

Table 2 details various results on the different NLI tasks for our model and previous state-of-the-art approaches. Our method significantly outperforms the baselines on four of the five datasets, achieving absolute improvements of upto 1.5% on MNLI, 5% on SciTail, 5.8% on QNLI and 0.6% on SNLI over the previous best results. This demonstrates our model’s ability to better reason over multiple sentences, and handle aspects of linguistic ambiguity. On RTE, one of the smaller datasets we evaluate on (2490 examples), we achieve an accuracy of 56%, which is below the 61.7% reported by a multi-task biLSTM model. Given the strong performance of our approach on larger NLI datasets, it is likely our model will benefit from multi-task training as well but we have not explored this currently. 

> 2 `https://ftfy.readthedocs.io/en/latest/` 

> 3 `https://spacy.io/` 

5 

Table 2: Experimental results on natural language inference tasks, comparing our model with current state-of-the-art methods. 5x indicates an ensemble of 5 models. All datasets use accuracy as the evaluation metric.

---

[referencia=a3e86ad05f37e40d score=0.011]
- [54] R. Socher, A. Perelygin, J. Wu, J. Chuang, C. D. Manning, A. Ng, and C. Potts. Recursive deep models for semantic compositionality over a sentiment treebank. In _Proceedings of the 2013 conference on empirical methods in natural language processing_ , pages 1631–1642, 2013. 

- [55] S. Srinivasan, R. Arora, and M. Riedl. A simple and effective approach to the story cloze test. _arXiv preprint arXiv:1803.05547_ , 2018. 

- [56] S. Subramanian, A. Trischler, Y. Bengio, and C. J. Pal. Learning general purpose distributed sentence representations via large scale multi-task learning. _arXiv preprint arXiv:1804.00079_ , 2018. 

- [57] J. Suzuki and H. Isozaki. Semi-supervised sequential labeling and segmentation using giga-word scale unlabeled data. _Proceedings of ACL-08: HLT_ , pages 665–673, 2008. 

- [58] Y. Tay, L. A. Tuan, and S. C. Hui. A compare-propagate architecture with alignment factorization for natural language inference. _arXiv preprint arXiv:1801.00102_ , 2017. 

- [59] Y. Tay, L. A. Tuan, and S. C. Hui. Multi-range reasoning for machine comprehension. _arXiv preprint arXiv:1803.09074_ , 2018. 

- [60] J. Tian, Z. Zhou, M. Lan, and Y. Wu. Ecnu at semeval-2017 task 1: Leverage kernel-based traditional nlp features and neural networks to build a universal model for multilingual and cross-lingual semantic textual similarity. In _Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017)_ , pages 191–197, 2017. 

- [61] Y. Tsvetkov. Opportunities and challenges in working with low-resource languages. _CMU_ , 2017.

---

[referencia=a3e86ad05f37e40d score=0.011]
- [33] P. Liang. _Semi-supervised learning for natural language_ . PhD thesis, Massachusetts Institute of Technology, 2005. 

- [34] P. J. Liu, M. Saleh, E. Pot, B. Goodrich, R. Sepassi, L. Kaiser, and N. Shazeer. Generating wikipedia by summarizing long sequences. _ICLR_ , 2018. 

- [35] X. Liu, K. Duh, and J. Gao. Stochastic answer networks for natural language inference. _arXiv preprint arXiv:1804.07888_ , 2018. 

- [36] L. Logeswaran and H. Lee. An efficient framework for learning sentence representations. _ICLR_ , 2018. 

- [37] I. Loshchilov and F. Hutter. Fixing weight decay regularization in adam. _arXiv preprint arXiv:1711.05101_ , 2017. 

- [38] B. McCann, J. Bradbury, C. Xiong, and R. Socher. Learned in translation: Contextualized word vectors. In _Advances in Neural Information Processing Systems_ , pages 6297–6308, 2017. 

- [39] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. Distributed representations of words and phrases and their compositionality. In _Advances in neural information processing systems_ , pages 3111–3119, 2013. 

- [40] N. Mostafazadeh, M. Roth, A. Louis, N. Chambers, and J. Allen. Lsdsem 2017 shared task: The story cloze test. In _Proceedings of the 2nd Workshop on Linking Models of Lexical, Sentential and Discourse-level Semantics_ , pages 46–51, 2017. 

- [41] K. Nigam, A. McCallum, and T. Mitchell. Semi-supervised text classification using em. _Semi-Supervised Learning_ , pages 33–56, 2006.

---

[referencia=a3e86ad05f37e40d score=0.009]
# **Improving Language Understanding by Generative Pre-Training** 

**Alec Radford** OpenAI `alec@openai.com` 

**Karthik Narasimhan Tim Salimans Ilya Sutskever** OpenAI OpenAI OpenAI `karthikn@openai.com tim@openai.com ilyasu@openai.com` 

## **Abstract** 

Natural language understanding comprises a wide range of diverse tasks such as textual entailment, question answering, semantic similarity assessment, and document classification. Although large unlabeled text corpora are abundant, labeled data for learning these specific tasks is scarce, making it challenging for discriminatively trained models to perform adequately. We demonstrate that large gains on these tasks can be realized by _generative pre-training_ of a language model on a diverse corpus of unlabeled text, followed by _discriminative fine-tuning_ on each specific task. In contrast to previous approaches, we make use of task-aware input transformations during fine-tuning to achieve effective transfer while requiring minimal changes to the model architecture. We demonstrate the effectiveness of our approach on a wide range of benchmarks for natural language understanding. Our general task-agnostic model outperforms discriminatively trained models that use architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test), 5.7% on question answering (RACE), and 1.5% on textual entailment (MultiNLI).

---

[referencia=a3e86ad05f37e40d score=0.008]
## **6 Conclusion** 

We introduced a framework for achieving strong natural language understanding with a single task-agnostic model through generative pre-training and discriminative fine-tuning. By pre-training on a diverse corpus with long stretches of contiguous text our model acquires significant world knowledge and ability to process long-range dependencies which are then successfully transferred to solving discriminative tasks such as question answering, semantic similarity assessment, entailment determination, and text classification, improving the state of the art on 9 of the 12 datasets we study. Using unsupervised (pre-)training to boost performance on discriminative tasks has long been an important goal of Machine Learning research. Our work suggests that achieving significant performance gains is indeed possible, and offers hints as to what models (Transformers) and data sets (text with long range dependencies) work best with this approach. We hope that this will help enable new research into unsupervised learning, for both natural language understanding and other domains, further improving our understanding of how and when unsupervised learning works.

---

[referencia=a3e86ad05f37e40d score=0.007]
## **4 Experiments**

---

[referencia=a3e86ad05f37e40d score=0.006]
Overall, our approach achieves new state-of-the-art results in 9 out of the 12 datasets we evaluate on, outperforming ensembles in many cases. Our results also indicate that our approach works well across datasets of different sizes, from smaller datasets such as STS-B ( _≈_ 5.7k training examples) – to the largest one – SNLI ( _≈_ 550k training examples).