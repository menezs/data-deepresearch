[referencia=32f3c7d144f036a0 score=0.906]
### **A.5 Illustrations of Fine-tuning on Different Tasks** 

The illustration of fine-tuning BERT on different tasks can be seen in Figure 4. Our task-specific models are formed by incorporating BERT with one additional output layer, so a minimal number of parameters need to be learned from scratch. Among the tasks, (a) and (b) are sequence-level tasks while (c) and (d) are token-level tasks. In the figure, _E_ represents the input embedding, _Ti_ represents the contextual representation of token _i_ , [CLS] is the special symbol for classification output, and [SEP] is the special symbol to separate non-consecutive token sequences.

---

[referencia=32f3c7d144f036a0 score=0.818]
### **A.4 Comparison of BERT, ELMo ,and OpenAI GPT** 

Here we studies the differences in recent popular representation learning models including ELMo, OpenAI GPT and BERT. The comparisons between the model architectures are shown visually in Figure 3. Note that in addition to the architecture differences, BERT and OpenAI GPT are finetuning approaches, while ELMo is a feature-based approach. 

The most comparable existing pre-training method to BERT is OpenAI GPT, which trains a left-to-right Transformer LM on a large text corpus. In fact, many of the design decisions in BERT were intentionally made to make it as close to GPT as possible so that the two methods could be minimally compared. The core argument of this work is that the bi-directionality and the two pretraining tasks presented in Section 3.1 account for the majority of the empirical improvements, but we do note that there are several other differences between how BERT and GPT were trained: 

- GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCorpus (800M words) and Wikipedia (2,500M words). 

- GPT uses a sentence separator ([SEP]) and classifier token ([CLS]) which are only introduced at fine-tuning time; BERT learns [SEP], [CLS] and sentence A/B embeddings during pre-training. 

- GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words. 

- GPT used the same learning rate of 5e-5 for all fine-tuning experiments; BERT chooses a task-specific fine-tuning learning rate which performs the best on the development set. 

To isolate the effect of these differences, we perform ablation experiments in Section 5.1 which demonstrate that the majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality they enable.

---

[referencia=32f3c7d144f036a0 score=0.813]
## **5 Ablation Studies** 

In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative importance. Additional 

results are still far worse than those of the pre- 



<!-- Start of picture text -->
Dev Set results are still far worse than those of the pre-<br>Tasks MNLI-m QNLI MRPC SST-2 SQuAD trained bidirectional models. The BiLSTM hurts<br>(Acc) (Acc) (Acc) (Acc) (F1)<br>performance on the GLUE tasks.<br>BERTNo NSPBASE 84.483.9 88.484.9 86.786.5 92.792.6 88.587.9 We recognize that it would also be possible to<br>LTR & No NSP 82.1 84.3 77.5 92.1 77.8 train separate LTR and RTL models and represent<br>+ BiLSTM 82.1 84.1 75.7 91.6 84.9 each token as the concatenation of the two mod-<br>els, as ELMo does. However: (a) this is twice as<br>Table 5: Ablation over the pre-training tasks using the<br>BERTBASE architecture. “No NSP” is trained without expensive as a single bidirectional model; (b) this<br>the next sentence prediction task. “LTR & No NSP” is is non-intuitive for tasks like QA, since the RTL<br>trained as a left-to-right LM without the next sentence model would not be able to condition the answer<br>prediction, like OpenAI GPT. “+ BiLSTM” adds a ran- on the question; (c) this it is strictly less powerful<br>domly initialized BiLSTM on top of the “LTR + No than a deep bidirectional model, since it can use<br>NSP” model during fine-tuning. both left and right context at every layer.<br><!-- End of picture text -->

**5.2 Effect of Model Size** In this section, we explore the effect of model size 

ablation studies can be found in Appendix C. 

**5.1 Effect of Pre-training Tasks** 

on fine-tuning task accuracy. We trained a number 

of BERT models with a differing number of layers,

---

[referencia=32f3c7d144f036a0 score=0.804]
### We demonstrate the importance of the deep bidi- 

hidden units, and attention heads, while otherwise 

rectionality of BERT by evaluating two pretraining objectives using exactly the same pretraining data, fine-tuning scheme, and hyperparameters as BERTBASE: **No NSP** : A bidirectional model which is trained using the “masked LM” (MLM) but without the “next sentence prediction” (NSP) task. **LTR & No NSP** : A left-context-only model which is trained using a standard Left-to-Right (LTR) LM, rather than an MLM. The left-only constraint 

using the same hyperparameters and training procedure as described previously. Results on selected GLUE tasks are shown in Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks. It is also perhaps surpris- 

was also applied at fine-tuning, because removing 

ing that we are able to achieve such significant improvements on top of models which are already quite large relative to the existing literature. 

it introduced a pre-train/fine-tune mismatch that degraded downstream performance. Additionally, 

this model was pre-trained without the NSP task. 

For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, A=2) with 235M parameters 

This is directly comparable to OpenAI GPT, but using our larger training dataset, our input representation, and our fine-tuning scheme. We first examine the impact brought by the NSP 

(Al-Rfou et al., 2018). By contrast, BERTBASE contains 110M parameters and BERTLARGE contains 340M parameters. 

task. In Table 5, we show that removing NSP hurts performance significantly on QNLI, MNLI, and SQuAD 1.1. Next, we evaluate the impact of training bidirectional representations by comparing “No NSP” to “LTR & No NSP”. The LTR

---

[referencia=32f3c7d144f036a0 score=0.798]
In this paper, we improve the fine-tuning based approaches by proposing BERT: **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked 

word based only on its context. Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer. In addition to the masked language model, we also use a “next sentence prediction” task that jointly pretrains text-pair representations. The contributions of our paper are as follows: 

- We demonstrate the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional language models for pre-training, BERT uses masked language models to enable pretrained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. 

- We show that pre-trained representations reduce the need for many heavily-engineered taskspecific architectures. BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level _and_ token-level tasks, outperforming many task-specific architectures. 

- BERT advances the state of the art for eleven NLP tasks. The code and pre-trained models are available at https://github.com/ google-research/bert.

---

[referencia=32f3c7d144f036a0 score=0.759]
# **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** 

**Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova** Google AI Language 

_{_ jacobdevlin,mingweichang,kentonl,kristout _}_ @google.com 

## **Abstract** 

We introduce a new language representation model called **BERT** , which stands for **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. 

BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

---

[referencia=32f3c7d144f036a0 score=0.587]
## **3 BERT** 

We introduce BERT and its detailed implementation in this section. There are two steps in our framework: _pre-training_ and _fine-tuning_ . During pre-training, the model is trained on unlabeled data over different pre-training tasks. For finetuning, the BERT model is first initialized with the pre-trained parameters, and all of the parameters are fine-tuned using labeled data from the downstream tasks. Each downstream task has separate fine-tuned models, even though they are initialized with the same pre-trained parameters. The question-answering example in Figure 1 will serve as a running example for this section. 

A distinctive feature of BERT is its unified architecture across different tasks. There is mini- 

mal difference between the pre-trained architec- 

**Model Architecture** BERT’s model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017) and released in the tensor2tensor library.<sup>1</sup> Because the use of Transformers has become common and our implementation is almost identical to the original, we will omit an exhaustive background description of the model architecture and refer readers to Vaswani et al. (2017) as well as excellent guides such as “The Annotated Transformer.”<sup>2</sup> 

In this work, we denote the number of layers (i.e., Transformer blocks) as _L_ , the hidden size as _H_ , and the number of self-attention heads as _A_ .<sup>3</sup> We primarily report results on two model sizes: **BERTBASE** (L=12, H=768, A=12, Total Parameters=110M) and **BERTLARGE** (L=24, H=1024, A=16, Total Parameters=340M). 

BERTBASE was chosen to have the same model size as OpenAI GPT for comparison purposes. Critically, however, the BERT Transformer uses bidirectional self-attention, while the GPT Transformer uses constrained self-attention where every token can only attend to context to its left.<sup>4</sup> 

> 1https://github.com/tensorflow/tensor2tensor 

> 2http://nlp.seas.harvard.edu/2018/04/03/attention.html 

> 3In all cases we set the feed-forward/filter size to be 4 _H_ ,

---

[referencia=32f3c7d144f036a0 score=0.582]
### **2.2 Unsupervised Fine-tuning Approaches** 

As with the feature-based approaches, the first works in this direction only pre-trained word embedding parameters from unlabeled text (Collobert and Weston, 2008). 

More recently, sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task (Dai and Le, 2015; Howard and Ruder, 2018; Radford et al., 2018). The advantage of these approaches is that few parameters need to be learned from scratch. At least partly due to this advantage, OpenAI GPT (Radford et al., 2018) achieved previously state-of-the-art results on many sentencelevel tasks from the GLUE benchmark (Wang et al., 2018a). Left-to-right language model- 



<!-- Start of picture text -->
NSP Mask LM Mask LM MNLI NER SQuAD Start/End Span<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1 ... TN T[SEP] T1’ ... TM’<br>BERT BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1 ... EN  E[SEP] E1’ ... EM’<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM<br>Masked Sentence A Masked Sentence B Question Paragraph<br>Unlabeled Sentence A and B Pair  Question Answer Pair<br>Pre-training Fine-Tuning<br><!-- End of picture text -->

Figure 1: Overall pre-training and fine-tuning procedures for BERT. Apart from output layers, the same architectures are used in both pre-training and fine-tuning. The same pre-trained model parameters are used to initialize models for different down-stream tasks. During fine-tuning, all parameters are fine-tuned. [CLS] is a special symbol added in front of every input example, and [SEP] is a special separator token (e.g. separating questions/answers). 

ing and auto-encoder objectives have been used for pre-training such models (Howard and Ruder, 2018; Radford et al., 2018; Dai and Le, 2015).

---

[referencia=32f3c7d144f036a0 score=0.491]
<!-- Start of picture text -->
Class  Class<br>Label Label<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1  T2 ...  TN<br>BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1  E2 ...  EN<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS][CLS] Tok 1 Tok 2 ... Tok N<br>Sentence 1 Sentence 2 Single Sentence<br>Start/End Span O B-PER ... O<br>C T1 ... TN T[SEP] T1’ ... TM’ C T1  T2 ...  TN<br>BERT BERT<br>E[CLS] E1 ... EN  E[SEP] E1’ ... EM’ E[CLS] E1  E2 ...  EN<br>[CLS] Tok 1 ... Tok N  [SEP] Tok 1 ... TokM [CLS] Tok 1 Tok 2 ... Tok N<br>Question Paragraph Single Sentence<br><!-- End of picture text -->

Figure 4: Illustrations of Fine-tuning BERT on Different Tasks. 

**SST-2** The Stanford Sentiment Treebank is a binary single-sentence classification task consisting of sentences extracted from movie reviews with human annotations of their sentiment (Socher et al., 2013). 

**CoLA** The Corpus of Linguistic Acceptability is a binary single-sentence classification task, where the goal is to predict whether an English sentence is linguistically “acceptable” or not (Warstadt et al., 2018). 

**STS-B** The Semantic Textual Similarity Benchmark is a collection of sentence pairs drawn from news headlines and other sources (Cer et al., 2017). They were annotated with a score from 1 to 5 denoting how similar the two sentences are in terms of semantic meaning. 

**MRPC** Microsoft Research Paraphrase Corpus consists of sentence pairs automatically extracted from online news sources, with human annotations 

for whether the sentences in the pair are semantically equivalent (Dolan and Brockett, 2005). 

**RTE** Recognizing Textual Entailment is a binary entailment task similar to MNLI, but with much less training data (Bentivogli et al., 2009).<sup>14</sup>

---

[referencia=32f3c7d144f036a0 score=0.489]
### **3.2 Fine-tuning BERT** 

Fine-tuning is straightforward since the selfattention mechanism in the Transformer allows BERT to model many downstream tasks— whether they involve single text or text pairs—by swapping out the appropriate inputs and outputs. For applications involving text pairs, a common pattern is to independently encode text pairs before applying bidirectional cross attention, such as Parikh et al. (2016); Seo et al. (2017). BERT instead uses the self-attention mechanism to unify these two stages, as encoding a concatenated text pair with self-attention effectively includes _bidirectional_ cross attention between two sentences. 

For each task, we simply plug in the taskspecific inputs and outputs into BERT and finetune all the parameters end-to-end. At the input, sentence A and sentence B from pre-training are analogous to (1) sentence pairs in paraphrasing, (2) hypothesis-premise pairs in entailment, (3) question-passage pairs in question answering, and 

(4) a degenerate text-∅ pair in text classification or sequence tagging. At the output, the token representations are fed into an output layer for tokenlevel tasks, such as sequence tagging or question answering, and the [CLS] representation is fed into an output layer for classification, such as entailment or sentiment analysis. 

Compared to pre-training, fine-tuning is relatively inexpensive. All of the results in the paper can be replicated in at most 1 hour on a single Cloud TPU, or a few hours on a GPU, starting from the exact same pre-trained model.<sup>7</sup> We describe the task-specific details in the corresponding subsections of Section 4. More details can be found in Appendix A.5.

---

[referencia=32f3c7d144f036a0 score=0.477]
> 2http://nlp.seas.harvard.edu/2018/04/03/attention.html 

> 3In all cases we set the feed-forward/filter size to be 4 _H_ , 

> i.e., 3072 for the _H_ = 768 and 4096 for the _H_ = 1024. 

> 4We note that in the literature the bidirectional Trans- 

**Input/Output Representations** To make BERT handle a variety of down-stream tasks, our input representation is able to unambiguously represent both a single sentence and a pair of sentences (e.g., _⟨_ Question, Answer _⟩_ ) in one token sequence. Throughout this work, a “sentence” can be an arbitrary span of contiguous text, rather than an actual linguistic sentence. A “sequence” refers to the input token sequence to BERT, which may be a single sentence or two sentences packed together. 

We use WordPiece embeddings (Wu et al., 2016) with a 30,000 token vocabulary. The first token of every sequence is always a special classification token ([CLS]). The final hidden state corresponding to this token is used as the aggregate sequence representation for classification tasks. Sentence pairs are packed together into a single sequence. We differentiate the sentences in two ways. First, we separate them with a special token ([SEP]). Second, we add a learned embedding to every token indicating whether it belongs to sentence A or sentence B. As shown in Figure 1, we denote input embedding as _E_ , the final hidden vector of the special [CLS] token as _C ∈_ R<sup>_H_</sup> , and the final hidden vector for the _i_<sup>th</sup> input token as _Ti ∈_ R<sup>_H_</sup> . 

For a given token, its input representation is constructed by summing the corresponding token, segment, and position embeddings. A visualization of this construction can be seen in Figure 2.

---

[referencia=32f3c7d144f036a0 score=0.417]
We organize the appendix into three sections: 

Compared to standard langauge model training, 

the masked LM only make predictions on 15% of 

• Additional implementation details for BERT are presented in Appendix A; 

tokens in each batch, which suggests that more pre-training steps may be required for the model 



<!-- Start of picture text -->
BERT (Ours) OpenAI GPT ELMo<br> T1 T2 ... TN  T1 T2 ...  TN  T1 T2 ...  TN<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br> E1 E2 ...  EN  E1 E2 ...  EN  E1 E2 ...  EN<br><!-- End of picture text -->

Figure 3: Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-toleft LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach. 

to converge. In Section C.1 we demonstrate that MLM does converge marginally slower than a leftto-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost. 

**Next Sentence Prediction** The next sentence prediction task can be illustrated in the following examples. 

Input = [CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP] Label = IsNext 

Input = [CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP] Label = NotNext

---

[referencia=32f3c7d144f036a0 score=0.375]
## **4 Experiments** 

In this section, we present BERT fine-tuning results on 11 NLP tasks.

---

[referencia=32f3c7d144f036a0 score=0.338]
### **5.3 Feature-based Approach with BERT** 

All of the BERT results presented so far have used the fine-tuning approach, where a simple classification layer is added to the pre-trained model, and all parameters are jointly fine-tuned on a downstream task. However, the feature-based approach, where fixed features are extracted from the pretrained model, has certain advantages. First, not all tasks can be easily represented by a Transformer encoder architecture, and therefore require a task-specific model architecture to be added. Second, there are major computational benefits to pre-compute an expensive representation of the training data once and then run many experiments with cheaper models on top of this representation. 

In this section, we compare the two approaches by applying BERT to the CoNLL-2003 Named Entity Recognition (NER) task (Tjong Kim Sang and De Meulder, 2003). In the input to BERT, we use a case-preserving WordPiece model, and we include the maximal document context provided by the data. Following standard practice, we formulate this as a tagging task but do not use a CRF 

|System|Dev F1|Test F1|
|---|---|---|
|ELMo (Peters et al.,2018a)|95.7|92.2|
|CVT (Clark et al.,2018)|-|92.6|
|CSE (Akbik et al.,2018)|-|**93.1**|
|Fine-tuning approach|||
|BERTLARGE|96.6|92.8|
|BERTBASE|96.4|92.4|
|Feature-based approach (BERTBASE)|||
|Embeddings|91.0|-|
|Second-to-Last Hidden|95.6|-|
|Last Hidden|94.9|-|
|Weighted Sum Last Four Hidden|95.9|-|
|Concat Last Four Hidden|96.1|-|
|Weighted Sum All 12 Layers|95.5|-|



Table 7: CoNLL-2003 Named Entity Recognition results. Hyperparameters were selected using the Dev set. The reported Dev and Test scores are averaged over 5 random restarts using those hyperparameters. 

layer in the output. We use the representation of the first sub-token as the input to the token-level

---

[referencia=32f3c7d144f036a0 score=0.310]
### **4.1 GLUE** 

The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018a) is a collection of diverse natural language understanding tasks. Detailed descriptions of GLUE datasets are included in Appendix B.1. 

To fine-tune on GLUE, we represent the input sequence (for single sentence or sentence pairs) as described in Section 3, and use the final hidden vector _C ∈_ R<sup>_H_</sup> corresponding to the first input token ([CLS]) as the aggregate representation. The only new parameters introduced during fine-tuning are classification layer weights _W ∈_ R<sup>_K×H_</sup> , where _K_ is the number of labels. We compute a standard classification loss with _C_ and _W_ , i.e., log(softmax( _CW_<sup>_T_</sup> )). 

> 7For example, the BERT SQuAD model can be trained in around 30 minutes on a single Cloud TPU to achieve a Dev F1 score of 91.0%. 

> 8 See (10) in https://gluebenchmark.com/faq.

---

[referencia=32f3c7d144f036a0 score=0.306]
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

[referencia=32f3c7d144f036a0 score=0.222]
### **3.1 Pre-training BERT** 

Unlike Peters et al. (2018a) and Radford et al. (2018), we do not use traditional left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train BERT using two unsupervised tasks, described in this section. This step is presented in the left part of Figure 1. 

**Task #1: Masked LM** Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-toright and a right-to-left model. Unfortunately, standard conditional language models can only be trained left-to-right _or_ right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself”, and the model could trivially predict the target word in a multi-layered context. 

former is often referred to as a “Transformer encoder” while the left-context-only version is referred to as a “Transformer decoder” since it can be used for text generation. 

In order to train a deep bidirectional representation, we simply mask some percentage of the input tokens at random, and then predict those masked tokens. We refer to this procedure as a “masked LM” (MLM), although it is often referred to as a _Cloze_ task in the literature (Taylor, 1953). In this case, the final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM. In all of our experiments, we mask 15% of all WordPiece tokens in each sequence at random. In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input.

---

[referencia=32f3c7d144f036a0 score=0.220]
Jason Yosinski, Jeff Clune, Yoshua Bengio, and Hod Lipson. 2014. How transferable are features in deep 

neural networks? In _Advances in neural information_ my dog is [MASK] _processing systems_ , pages 3320–3328. • 10% of the time: Replace the word with a Adams Wei Yu, David Dohan, Minh-Thang Luong, Rui random word, e.g., my dog is hairy _→_ my Zhao, Kai Chen, Mohammad Norouzi, and Quoc V dog is apple Le. 2018. QANet: Combining local convolution withsion. globalIn _ICLR_ self-attention. for reading comprehen• 10% of the time: Keep the word unchanged, e.g., my dog is hairy _→_ my dog Rowan Zellers, Yonatan Bisk, Roy Schwartz, and Yejin is hairy. The purpose of this is to bias the Choi. 2018. Swag: A large-scale adversarial dataset representation towards the actual observed for grounded commonsense inference. In _Proceed-_ word. 

_ings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ . 

The advantage of this procedure is that the 

Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan SalakhutTransformer encoder does not know which words dinov, Raquel Urtasun, Antonio Torralba, and Sanja it will be asked to predict or which have been reFidler. 2015. Aligning books and movies: Towards placed by random words, so it is forced to keep story-like visual explanations by watching movies and reading books. In _Proceedings of the IEEE_ a distributional contextual representation of _evinternational conference on computer vision_ , pages _ery_ input token. Additionally, because random 19–27. replacement only occurs for 1.5% of all tokens (i.e., 10% of 15%), this does not seem to harm **Appendix for “BERT: Pre-training of** the model’s language understanding capability. In **Deep Bidirectional Transformers for** Section C.2, we evaluate the impact this proce- **Language Understanding”** dure. 

We organize the appendix into three sections: 

Compared to standard langauge model training, 

the masked LM only make predictions on 15% of

---

[referencia=32f3c7d144f036a0 score=0.206]
### In Section 3.1, we mention that BERT uses a 

10%). The right part of the paper represents the mixed strategy for masking the target tokens when pre-training with the masked language model Dev set results. For the feature-based approach, (MLM) objective. The following is an ablation we concatenate the last 4 layers of BERT as the study to evaluate the effect of different masking features, which was shown to be the best approach in Section 5.3. strategies. From the table it can be seen that fine-tuning is surprisingly robust to different masking strategies. 84 However, as expected, using only the MASK strategy was problematic when applying the feature82 based approach to NER. Interestingly, using only 80 the RND strategy performs much worse than our strategy as well. 78 BERTBASE (Masked LM) 76 BERTBASE (Left-to-Right) 200 400 600 800 1 _,_ 000 Pre-training Steps (Thousands) 

Figure 5: Ablation over number of training steps. This shows the MNLI accuracy after fine-tuning, starting from model parameters that have been pre-trained for _k_ steps. The x-axis is the value of _k_ .

---

[referencia=32f3c7d144f036a0 score=0.195]
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