[referencia=a3e86ad05f37e40d score=0.749]
## **1 Introduction** 

The ability to learn effectively from raw text is crucial to alleviating the dependence on supervised learning in natural language processing (NLP). Most deep learning methods require substantial amounts of manually labeled data, which restricts their applicability in many domains that suffer from a dearth of annotated resources [61]. In these situations, models that can leverage linguistic information from unlabeled data provide a valuable alternative to gathering more annotation, which can be time-consuming and expensive. Further, even in cases where considerable supervision is available, learning good representations in an unsupervised fashion can provide a significant performance boost. The most compelling evidence for this so far has been the extensive use of pretrained word embeddings [10, 39, 42] to improve performance on a range of NLP tasks [8, 11, 26, 45]. 

Leveraging more than word-level information from unlabeled text, however, is challenging for two main reasons. First, it is unclear what type of optimization objectives are most effective at learning text representations that are useful for transfer. Recent research has looked at various objectives such as language modeling [44], machine translation [38], and discourse coherence [22], with each method outperforming the others on different tasks.<sup>1</sup> Second, there is no consensus on the most effective way to transfer these learned representations to the target task. Existing techniques involve a combination of making task-specific changes to the model architecture [43, 44], using intricate learning schemes [21] and adding auxiliary learning objectives [50]. These uncertainties have made it difficult to develop effective semi-supervised learning approaches for language processing. 

> 1https://gluebenchmark.com/leaderboard 

Preprint. Work in progress. 

In this paper, we explore a semi-supervised approach for language understanding tasks using a combination of unsupervised pre-training and supervised fine-tuning. Our goal is to learn a universal representation that transfers with little adaptation to a wide range of tasks. We assume access to a large corpus of unlabeled text and several datasets with manually annotated training examples (target tasks). Our setup does not require these target tasks to be in the same domain as the unlabeled corpus. We employ a two-stage training procedure. First, we use a language modeling objective on the unlabeled data to learn the initial parameters of a neural network model. Subsequently, we adapt these parameters to a target task using the corresponding supervised objective.

---

[referencia=32f3c7d144f036a0 score=0.629]
### **2.2 Unsupervised Fine-tuning Approaches** 

As with the feature-based approaches, the first works in this direction only pre-trained word embedding parameters from unlabeled text (Collobert and Weston, 2008). 

More recently, sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task (Dai and Le, 2015; Howard and Ruder, 2018; Radford et al., 2018). The advantage of these approaches is that few parameters need to be learned from scratch. At least partly due to this advantage, OpenAI GPT (Radford et al., 2018) achieved previously state-of-the-art results on many sentencelevel tasks from the GLUE benchmark (Wang et al., 2018a). Left-to-right language model- 



<!-- Start of picture text -->
NSP Mask LM Mask LM MNLI NER SQuAD Start/End Span<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1 ... TN T[SEP] T1’ ... TM’<br>BERT BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Masked Sentence A Masked Sentence B Question Paragraph<br>Unlabeled Sentence A and B Pair  Question Answer Pair<br>Pre-training Fine-Tuning<br><!-- End of picture text -->

Figure 1: Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architectures are used in both pre-training and fine-tuning. The same pre-trained model parameters are used to initialize 

models for different down-stream tasks. During fine-tuning, all parameters are fine-tuned. [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). 

ing and auto-encoder objectives have been used for pre-training such models (Howard and Ruder, 

mal difference between the pre-trained architec-

---

[referencia=a3e86ad05f37e40d score=0.465]
# **Improving Language Understanding by Generative Pre-Training** 

**Alec Radford** OpenAI `alec@openai.com` 

**Karthik Narasimhan Tim Salimans Ilya Sutskever** OpenAI OpenAI OpenAI `karthikn@openai.com tim@openai.com ilyasu@openai.com` 

## **Abstract** 

Natural language understanding comprises a wide range of diverse tasks such as textual entailment, question answering, semantic similarity assessment, and document classification. Although large unlabeled text corpora are abundant, labeled data for learning these specific tasks is scarce, making it challenging for discriminatively trained models to perform adequately. We demonstrate that large gains on these tasks can be realized by _generative pre-training_ of a language model on a diverse corpus of unlabeled text, followed by _discriminative fine-tuning_ on each specific task. In contrast to previous approaches, we make use of task-aware input transformations during fine-tuning to achieve effective transfer while requiring minimal changes to the model architecture. We demonstrate the effectiveness of our approach on a wide range of benchmarks for natural language understanding. Our general task-agnostic model outperforms discriminatively trained models that use architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test), 5.7% on question answering (RACE), and 1.5% on textual entailment (MultiNLI).

---

[referencia=32f3c7d144f036a0 score=0.423]
### **A.2 Pre-training Procedure** 

To generate each training input sequence, we sample two spans of text from the corpus, which we refer to as “sentences” even though they are typically much longer than single sentences (but can be shorter also). The first sentence receives the A embedding and the second receives the B embedding. 50% of the time B is the actual next sentence that follows A and 50% of the time it is a random sentence, which is done for the “next sentence prediction” task. They are sampled such that the combined length is _≤_ 512 tokens. The LM masking is applied after WordPiece tokenization with a uniform masking rate of 15%, and no special consideration given to partial word pieces. 

We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 

epochs over the 3.3 billion word corpus. We use Adam with learning rate of 1e-4, _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 999, L2 weight decay of 0 _._ 01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate. We use a dropout probability of 0.1 on all layers. We use a gelu activation (Hendrycks and Gimpel, 2016) rather than the standard relu, following OpenAI GPT. The training loss is the sum of the mean masked LM likelihood and the mean next sentence prediction likelihood. 

Training of BERTBASE was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total).<sup>13</sup> Training of BERTLARGE was performed on 16 Cloud TPUs (64 TPU chips total). Each pretraining took 4 days to complete. 

Longer sequences are disproportionately expensive because attention is quadratic to the sequence length. To speed up pretraing in our experiments, we pre-train the model with sequence length of 128 for 90% of the steps. Then, we train the rest 10% of the steps of sequence of 512 to learn the positional embeddings.

---

[referencia=32f3c7d144f036a0 score=0.387]
Although this allows us to obtain a bidirectional pre-trained model, a downside is that we are creating a mismatch between pre-training and fine-tuning, since the [MASK] token does not appear during fine-tuning. To mitigate this, we do not always replace “masked” words with the actual [MASK] token. The training data generator chooses 15% of the token positions at random for prediction. If the _i_ -th token is chosen, we replace the _i_ -th token with (1) the [MASK] token 80% of the time (2) a random token 10% of the time (3) the unchanged _i_ -th token 10% of the time. Then, _Ti_ will be used to predict the original token with cross entropy loss. We compare variations of this procedure in Appendix C.2. 

**Task #2: Next Sentence Prediction (NSP)** Many important downstream tasks such as Question Answering (QA) and Natural Language Inference (NLI) are based on understanding the _relationship_ between two sentences, which is not directly captured by language modeling. In order to train a model that understands sentence relationships, we pre-train for a binarized _next sentence prediction_ task that can be trivially generated from any monolingual corpus. Specifically, when choosing the sentences A and B for each pretraining example, 50% of the time B is the actual next sentence that follows A (labeled as IsNext), and 50% of the time it is a random sentence from the corpus (labeled as NotNext). As we show in Figure 1, _C_ is used for next sentence prediction (NSP).<sup>5</sup> Despite its simplicity, we demonstrate in Section 5.1 that pre-training towards this task is very beneficial to both QA and NLI.<sup>6</sup> 

> 5The final model achieves 97%-98% accuracy on NSP. 

> 6The vector _C_ is not a meaningful sentence representation without fine-tuning, since it was trained with NSP.

---

[referencia=32f3c7d144f036a0 score=0.384]
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

[referencia=32f3c7d144f036a0 score=0.291]
## **1 Introduction** 

Language model pre-training has been shown to be effective for improving many natural language processing tasks (Dai and Le, 2015; Peters et al., 2018a; Radford et al., 2018; Howard and Ruder, 2018). These include sentence-level tasks such as natural language inference (Bowman et al., 2015; Williams et al., 2018) and paraphrasing (Dolan and Brockett, 2005), which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level (Tjong Kim Sang and De Meulder, 2003; Rajpurkar et al., 2016). 

There are two existing strategies for applying pre-trained language representations to downstream tasks: _feature-based_ and _fine-tuning_ . The feature-based approach, such as ELMo (Peters et al., 2018a), uses task-specific architectures that include the pre-trained representations as additional features. The fine-tuning approach, such as the Generative Pre-trained Transformer (OpenAI GPT) (Radford et al., 2018), introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning _all_ pretrained parameters. The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations. 

We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches. The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training. For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani et al., 2017). Such restrictions are sub-optimal for sentence-level tasks, and could be very harmful when applying finetuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions.

---

[referencia=a3e86ad05f37e40d score=0.284]
## **2 Related Work** 

**Semi-supervised learning for NLP** Our work broadly falls under the category of semi-supervised learning for natural language. This paradigm has attracted significant interest, with applications to tasks like sequence labeling [24, 33, 57] or text classification [41, 70]. The earliest approaches used unlabeled data to compute word-level or phrase-level statistics, which were then used as features in a supervised model [33]. Over the last few years, researchers have demonstrated the benefits of using word embeddings [11, 39, 42], which are trained on unlabeled corpora, to improve performance on a variety of tasks [8, 11, 26, 45]. These approaches, however, mainly transfer word-level information, whereas we aim to capture higher-level semantics. 

Recent approaches have investigated learning and utilizing more than word-level semantics from unlabeled data. Phrase-level or sentence-level embeddings, which can be trained using an unlabeled corpus, have been used to encode text into suitable vector representations for various target tasks [28, 32, 1, 36, 22, 12, 56, 31]. 

**Unsupervised pre-training** Unsupervised pre-training is a special case of semi-supervised learning where the goal is to find a good initialization point instead of modifying the supervised learning objective. Early works explored the use of the technique in image classification [20, 49, 63] and regression tasks [3]. Subsequent research [15] demonstrated that pre-training acts as a regularization scheme, enabling better generalization in deep neural networks. In recent work, the method has been used to help train deep neural networks on various tasks like image classification [69], speech recognition [68], entity disambiguation [17] and machine translation [48].

---

[referencia=32f3c7d144f036a0 score=0.278]
# **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** 

**Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova** Google AI Language 

_{_ jacobdevlin,mingweichang,kentonl,kristout _}_ @google.com 

## **Abstract** 

We introduce a new language representation model called **BERT** , which stands for **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. 

BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

---

[referencia=32f3c7d144f036a0 score=0.269]
### **3.1 Pre-training BERT** 

Unlike Peters et al. (2018a) and Radford et al. (2018), we do not use traditional left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train BERT using two unsupervised tasks, described in this section. This step is presented in the left part of Figure 1. 

**Task #1: Masked LM** Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-toright and a right-to-left model. Unfortunately, standard conditional language models can only be trained left-to-right _or_ right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself”, and the model could trivially predict the target word in a multi-layered context. 

former is often referred to as a “Transformer encoder” while the left-context-only version is referred to as a “Transformer decoder” since it can be used for text generation. 

In order to train a deep bidirectional representation, we simply mask some percentage of the input tokens at random, and then predict those masked tokens. We refer to this procedure as a “masked LM” (MLM), although it is often referred to as a _Cloze_ task in the literature (Taylor, 1953). In this case, the final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM. In all of our experiments, we mask 15% of all WordPiece tokens in each sequence at random. In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input.

---

[referencia=32f3c7d144f036a0 score=0.265]
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

[referencia=a3e86ad05f37e40d score=0.240]
## **6 Conclusion** 

We introduced a framework for achieving strong natural language understanding with a single task-agnostic model through generative pre-training and discriminative fine-tuning. By pre-training on a diverse corpus with long stretches of contiguous text our model acquires significant world knowledge and ability to process long-range dependencies which are then successfully transferred to solving discriminative tasks such as question answering, semantic similarity assessment, entailment determination, and text classification, improving the state of the art on 9 of the 12 datasets we study. Using unsupervised (pre-)training to boost performance on discriminative tasks has long been an important goal of Machine Learning research. Our work suggests that achieving significant performance gains is indeed possible, and offers hints as to what models (Transformers) and data sets (text with long range dependencies) work best with this approach. We hope that this will help enable new research into unsupervised learning, for both natural language understanding and other domains, further improving our understanding of how and when unsupervised learning works.

---

[referencia=dd0416935c1f8d1f score=0.234]
## Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

***Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu***; 21(140):1−67, 2020.

### Abstract

Transfer learning, where a model is first pre-trained on a data-rich task before being fine-tuned on a downstream task, has emerged as a powerful technique in natural language processing (NLP). The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework that converts all text-based language problems into a text-to-text format. Our systematic study compares pre-training objectives, architectures, unlabeled data sets, transfer approaches, and other factors on dozens of language understanding tasks. By combining the insights from our exploration with scale and our new “Colossal Clean Crawled Corpus”, we achieve state-of-the-art results on many benchmarks covering summarization, question answering, text classification, and more. To facilitate future work on transfer learning for NLP, we release our data set, pre-trained models, and code.

[abs]

[pdf][bib] [code]
| © JMLR 2020. (edit, beta) |

---

[referencia=32f3c7d144f036a0 score=0.194]
Figure 3: Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-toleft LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach. 

to converge. In Section C.1 we demonstrate that MLM does converge marginally slower than a leftto-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost. 

**Next Sentence Prediction** The next sentence prediction task can be illustrated in the following examples. 

Input = [CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP] Label = IsNext 

Input = [CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP] Label = NotNext

---

[referencia=a3e86ad05f37e40d score=0.192]
For our model architecture, we use the _Transformer_ [62], which has been shown to perform strongly on various tasks such as machine translation [62], document generation [34], and syntactic parsing [29]. This model choice provides us with a more structured memory for handling long-term dependencies in text, compared to alternatives like recurrent networks, resulting in robust transfer performance across diverse tasks. During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens. As we demonstrate in our experiments, these adaptations enable us to fine-tune effectively with minimal changes to the architecture of the pre-trained model. 

We evaluate our approach on four types of language understanding tasks – natural language inference, question answering, semantic similarity, and text classification. Our general task-agnostic model outperforms discriminatively trained models that employ architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test) [40], 5.7% on question answering (RACE) [30], 1.5% on textual entailment (MultiNLI) [66] and 5.5% on the recently introduced GLUE multi-task benchmark [64]. We also analyzed zero-shot behaviors of the pre-trained model on four different settings and demonstrate that it acquires useful linguistic knowledge for downstream tasks.

---

[referencia=a3e86ad05f37e40d score=0.169]
## **3 Framework** 

Our training procedure consists of two stages. The first stage is learning a high-capacity language model on a large corpus of text. This is followed by a fine-tuning stage, where we adapt the model to a discriminative task with labeled data. 

### **3.1 Unsupervised pre-training** 

Given an unsupervised corpus of tokens _U_ = _{u_ 1 _, . . . , un}_ , we use a standard language modeling objective to maximize the following likelihood: 



where _k_ is the size of the context window, and the conditional probability _P_ is modeled using a neural network with parameters Θ. These parameters are trained using stochastic gradient descent [51]. 

In our experiments, we use a multi-layer _Transformer decoder_ [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens: 





where _U_ = ( _u−k, . . . , u−_ 1) is the context vector of tokens, _n_ is the number of layers, _We_ is the token embedding matrix, and _Wp_ is the position embedding matrix.

---

[referencia=32f3c7d144f036a0 score=0.154]
In this paper, we improve the fine-tuning based approaches by proposing BERT: **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked 

word based only on its context. Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer. In addition to the masked language model, we also use a “next sentence prediction” task that jointly pretrains text-pair representations. The contributions of our paper are as follows: 

- We demonstrate the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional language models for pre-training, BERT uses masked language models to enable pretrained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. 

- We show that pre-trained representations reduce the need for many heavily-engineered taskspecific architectures. BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level _and_ token-level tasks, outperforming many task-specific architectures. 

- BERT advances the state of the art for eleven NLP tasks. The code and pre-trained models are available at https://github.com/ google-research/bert.

---

[referencia=a3e86ad05f37e40d score=0.142]
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

[referencia=32f3c7d144f036a0 score=0.128]
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

[referencia=32f3c7d144f036a0 score=0.125]
### **5.2 Effect of Model Size** 

In this section, we explore the effect of model size on fine-tuning task accuracy. We trained a number of BERT models with a differing number of layers, hidden units, and attention heads, while otherwise using the same hyperparameters and training procedure as described previously. 

Results on selected GLUE tasks are shown in Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks. It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative to the existing literature. For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, A=2) with 235M parameters (Al-Rfou et al., 2018). By contrast, BERTBASE contains 110M parameters and BERTLARGE contains 340M parameters. 

It has long been known that increasing the model size will lead to continual improvements on large-scale tasks such as machine translation and language modeling, which is demonstrated by the LM perplexity of held-out training data shown in Table 6. However, we believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. Peters et al. (2018b) presented 

mixed results on the downstream task impact of increasing the pre-trained bi-LM size from two to four layers and Melamud et al. (2016) mentioned in passing that increasing hidden dimension size from 200 to 600 helped, but increasing further to 1,000 did not bring further improvements. Both of these prior works used a featurebased approach — we hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the taskspecific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small.