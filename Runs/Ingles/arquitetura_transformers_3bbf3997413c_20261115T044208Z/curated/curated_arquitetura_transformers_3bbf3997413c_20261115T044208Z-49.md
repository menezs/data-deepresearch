[referencia=32f3c7d144f036a0 score=0.977]
In this paper, we improve the fine-tuning based approaches by proposing BERT: **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked 

word based only on its context. Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer. In addition to the masked language model, we also use a “next sentence prediction” task that jointly pretrains text-pair representations. The contributions of our paper are as follows: 

- We demonstrate the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional language models for pre-training, BERT uses masked language models to enable pretrained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. 

- We show that pre-trained representations reduce the need for many heavily-engineered taskspecific architectures. BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level _and_ token-level tasks, outperforming many task-specific architectures. 

- BERT advances the state of the art for eleven NLP tasks. The code and pre-trained models are available at https://github.com/ google-research/bert.

---

[referencia=32f3c7d144f036a0 score=0.976]
### **3.1 Pre-training BERT** 

Unlike Peters et al. (2018a) and Radford et al. (2018), we do not use traditional left-to-right or right-to-left language models to pre-train BERT. Instead, we pre-train BERT using two unsupervised tasks, described in this section. This step is presented in the left part of Figure 1. 

**Task #1: Masked LM** Intuitively, it is reasonable to believe that a deep bidirectional model is strictly more powerful than either a left-to-right model or the shallow concatenation of a left-toright and a right-to-left model. Unfortunately, standard conditional language models can only be trained left-to-right _or_ right-to-left, since bidirectional conditioning would allow each word to indirectly “see itself”, and the model could trivially predict the target word in a multi-layered context. 

former is often referred to as a “Transformer encoder” while the left-context-only version is referred to as a “Transformer decoder” since it can be used for text generation. 

In order to train a deep bidirectional representation, we simply mask some percentage of the input tokens at random, and then predict those masked tokens. We refer to this procedure as a “masked LM” (MLM), although it is often referred to as a _Cloze_ task in the literature (Taylor, 1953). In this case, the final hidden vectors corresponding to the mask tokens are fed into an output softmax over the vocabulary, as in a standard LM. In all of our experiments, we mask 15% of all WordPiece tokens in each sequence at random. In contrast to denoising auto-encoders (Vincent et al., 2008), we only predict the masked words rather than reconstructing the entire input.

---

[referencia=32f3c7d144f036a0 score=0.966]
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

[referencia=32f3c7d144f036a0 score=0.951]
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

[referencia=32f3c7d144f036a0 score=0.922]
# **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** 

**Jacob Devlin Ming-Wei Chang Kenton Lee Kristina Toutanova** Google AI Language 

_{_ jacobdevlin,mingweichang,kentonl,kristout _}_ @google.com 

## **Abstract** 

We introduce a new language representation model called **BERT** , which stands for **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. Unlike recent language representation models (Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial taskspecific architecture modifications. 

BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

---

[referencia=32f3c7d144f036a0 score=0.834]
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

[referencia=32f3c7d144f036a0 score=0.778]
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

[referencia=32f3c7d144f036a0 score=0.771]
Figure 3: Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-toleft LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach. 

to converge. In Section C.1 we demonstrate that MLM does converge marginally slower than a leftto-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost. 

**Next Sentence Prediction** The next sentence prediction task can be illustrated in the following examples. 

Input = [CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP] Label = IsNext 

Input = [CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP] Label = NotNext

---

[referencia=32f3c7d144f036a0 score=0.730]
### **A.2 Pre-training Procedure** 

To generate each training input sequence, we sample two spans of text from the corpus, which we refer to as “sentences” even though they are typically much longer than single sentences (but can be shorter also). The first sentence receives the A embedding and the second receives the B embedding. 50% of the time B is the actual next sentence that follows A and 50% of the time it is a random sentence, which is done for the “next sentence prediction” task. They are sampled such that the combined length is _≤_ 512 tokens. The LM masking is applied after WordPiece tokenization with a uniform masking rate of 15%, and no special consideration given to partial word pieces. 

We train with batch size of 256 sequences (256 sequences * 512 tokens = 128,000 tokens/batch) for 1,000,000 steps, which is approximately 40 

epochs over the 3.3 billion word corpus. We use Adam with learning rate of 1e-4, _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 999, L2 weight decay of 0 _._ 01, learning rate warmup over the first 10,000 steps, and linear decay of the learning rate. We use a dropout probability of 0.1 on all layers. We use a gelu activation (Hendrycks and Gimpel, 2016) rather than the standard relu, following OpenAI GPT. The training loss is the sum of the mean masked LM likelihood and the mean next sentence prediction likelihood. 

Training of BERTBASE was performed on 4 Cloud TPUs in Pod configuration (16 TPU chips total).<sup>13</sup> Training of BERTLARGE was performed on 16 Cloud TPUs (64 TPU chips total). Each pretraining took 4 days to complete. 

Longer sequences are disproportionately expensive because attention is quadratic to the sequence length. To speed up pretraing in our experiments, we pre-train the model with sequence length of 128 for 90% of the steps. Then, we train the rest 10% of the steps of sequence of 512 to learn the positional embeddings.

---

[referencia=32f3c7d144f036a0 score=0.713]
### 2018; Radford et al., 2018; Dai and Le, 2015). 

**Model Architecture** BERT’s model architec- 

**2.3 Transfer Learning from Supervised Data** There has also been work showing effective transfer from supervised tasks with large datasets, such 

as natural language inference (Conneau et al., 2017) and machine translation (McCann et al., 2017). Computer vision research has also demonstrated the importance of transfer learning from 

large pre-trained models, where an effective recipe is to fine-tune models pre-trained with Ima- 

geNet (Deng et al., 2009; Yosinski et al., 2014). 

**3 BERT** We introduce BERT and its detailed implementation in this section. There are two steps in our framework: _pre-training_ and _fine-tuning_ . Dur- 

ture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017) and released in the tensor2tensor library.<sup>1</sup> Because the use 

of Transformers has become common and our implementation is almost identical to the original, we will omit an exhaustive background descrip- 

tion of the model architecture and refer readers to Vaswani et al. (2017) as well as excellent guides such as “The Annotated Transformer.”<sup>2</sup> 

In this work, we denote the number of layers (i.e., Transformer blocks) as _L_ , the hidden size as _H_ , and the number of self-attention heads as _A_ .<sup>3</sup> We primarily report results on two model sizes: **BERTBASE** (L=12, H=768, A=12, Total Parameters=110M) and **BERTLARGE** (L=24, H=1024, 

ing pre-training, the model is trained on unlabeled A=16, Total Parameters=340M). data over different pre-training tasks. For fineBERTBASE was chosen to have the same model tuning, the BERT model is first initialized with size as OpenAI GPT for comparison purposes. the pre-trained parameters, and all of the paramCritically, however, the BERT Transformer uses 

eters are fine-tuned using labeled data from the downstream tasks. Each downstream task has sep-

---

[referencia=32f3c7d144f036a0 score=0.672]
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

[referencia=32f3c7d144f036a0 score=0.565]
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

[referencia=32f3c7d144f036a0 score=0.549]
### **A.4 Comparison of BERT, ELMo ,and OpenAI GPT** 

Here we studies the differences in recent popular representation learning models including ELMo, OpenAI GPT and BERT. The comparisons between the model architectures are shown visually in Figure 3. Note that in addition to the architecture differences, BERT and OpenAI GPT are finetuning approaches, while ELMo is a feature-based approach. 

The most comparable existing pre-training method to BERT is OpenAI GPT, which trains a left-to-right Transformer LM on a large text corpus. In fact, many of the design decisions in BERT were intentionally made to make it as close to GPT as possible so that the two methods could be minimally compared. The core argument of this work is that the bi-directionality and the two pretraining tasks presented in Section 3.1 account for the majority of the empirical improvements, but we do note that there are several other differences between how BERT and GPT were trained: 

- GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCorpus (800M words) and Wikipedia (2,500M words). 

- GPT uses a sentence separator ([SEP]) and classifier token ([CLS]) which are only introduced at fine-tuning time; BERT learns [SEP], [CLS] and sentence A/B embeddings during pre-training. 

- GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words. 

- GPT used the same learning rate of 5e-5 for all fine-tuning experiments; BERT chooses a task-specific fine-tuning learning rate which performs the best on the development set. 

To isolate the effect of these differences, we perform ablation experiments in Section 5.1 which demonstrate that the majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality they enable.

---

[referencia=32f3c7d144f036a0 score=0.514]
We use a batch size of 32 and fine-tune for 3 epochs over the data for all GLUE tasks. For each task, we selected the best fine-tuning learning rate (among 5e-5, 4e-5, 3e-5, and 2e-5) on the Dev set. Additionally, for BERTLARGE we found that finetuning was sometimes unstable on small datasets, so we ran several random restarts and selected the best model on the Dev set. With random restarts, we use the same pre-trained checkpoint but perform different fine-tuning data shuffling and classifier layer initialization.<sup>9</sup> 

Results are presented in Table 1. Both BERTBASE and BERTLARGE outperform all systems on all tasks by a substantial margin, obtaining 4.5% and 7.0% respective average accuracy improvement over the prior state of the art. Note that BERTBASE and OpenAI GPT are nearly identical in terms of model architecture apart from the attention masking. For the largest and most widely reported GLUE task, MNLI, BERT obtains a 4.6% absolute accuracy improvement. On the official GLUE leaderboard<sup>10</sup> , BERTLARGE obtains a score of 80.5, compared to OpenAI GPT, which obtains 72.8 as of the date of writing. 

We find that BERTLARGE significantly outperforms BERTBASE across all tasks, especially those with very little training data. The effect of model size is explored more thoroughly in Section 5.2.

---

[referencia=32f3c7d144f036a0 score=0.477]
The numbers in the left part of the table represent the probabilities of the specific strategies used during MLM pre-training (BERT uses 80%, 10%, 10%). The right part of the paper represents the Dev set results. For the feature-based approach, we concatenate the last 4 layers of BERT as the features, which was shown to be the best approach in Section 5.3. 

From the table it can be seen that fine-tuning is surprisingly robust to different masking strategies. However, as expected, using only the MASK strategy was problematic when applying the featurebased approach to NER. Interestingly, using only the RND strategy performs much worse than our strategy as well. 

Figure 5: Ablation over number of training steps. This shows the MNLI accuracy after fine-tuning, starting from model parameters that have been pre-trained for _k_ steps. The x-axis is the value of _k_ .

---

[referencia=32f3c7d144f036a0 score=0.466]
## **1 Introduction** 

Language model pre-training has been shown to be effective for improving many natural language processing tasks (Dai and Le, 2015; Peters et al., 2018a; Radford et al., 2018; Howard and Ruder, 2018). These include sentence-level tasks such as natural language inference (Bowman et al., 2015; Williams et al., 2018) and paraphrasing (Dolan and Brockett, 2005), which aim to predict the relationships between sentences by analyzing them holistically, as well as token-level tasks such as named entity recognition and question answering, where models are required to produce fine-grained output at the token level (Tjong Kim Sang and De Meulder, 2003; Rajpurkar et al., 2016). 

There are two existing strategies for applying pre-trained language representations to downstream tasks: _feature-based_ and _fine-tuning_ . The feature-based approach, such as ELMo (Peters et al., 2018a), uses task-specific architectures that include the pre-trained representations as additional features. The fine-tuning approach, such as the Generative Pre-trained Transformer (OpenAI GPT) (Radford et al., 2018), introduces minimal task-specific parameters, and is trained on the downstream tasks by simply fine-tuning _all_ pretrained parameters. The two approaches share the same objective function during pre-training, where they use unidirectional language models to learn general language representations. 

We argue that current techniques restrict the power of the pre-trained representations, especially for the fine-tuning approaches. The major limitation is that standard language models are unidirectional, and this limits the choice of architectures that can be used during pre-training. For example, in OpenAI GPT, the authors use a left-toright architecture, where every token can only attend to previous tokens in the self-attention layers of the Transformer (Vaswani et al., 2017). Such restrictions are sub-optimal for sentence-level tasks, and could be very harmful when applying finetuning based approaches to token-level tasks such as question answering, where it is crucial to incorporate context from both directions.

---

[referencia=32f3c7d144f036a0 score=0.443]
## **5 Ablation Studies** 

In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative importance. Additional 

||||Dev Set|||
|---|---|---|---|---|---|
|Tasks|MNLI-m <br>(Acc)|QNLI <br>(Acc)|MRPC <br>(Acc)|SST-2 <br>(Acc)|SQuAD<br>(F1)|
|BERTBASE|84.4|88.4|86.7|92.7|88.5|
|No NSP|83.9|84.9|86.5|92.6|87.9|
|LTR & No NSP|82.1|84.3|77.5|92.1|77.8|
|+ BiLSTM|82.1|84.1|75.7|91.6|84.9|



Table 5: Ablation over the pre-training tasks using the BERTBASE architecture. “No NSP” is trained without the next sentence prediction task. “LTR & No NSP” is trained as a left-to-right LM without the next sentence prediction, like OpenAI GPT. “+ BiLSTM” adds a randomly initialized BiLSTM on top of the “LTR + No NSP” model during fine-tuning. 

### ablation studies can be found in Appendix C.

---

[referencia=32f3c7d144f036a0 score=0.433]
### **5.2 Effect of Model Size** 

In this section, we explore the effect of model size on fine-tuning task accuracy. We trained a number of BERT models with a differing number of layers, hidden units, and attention heads, while otherwise using the same hyperparameters and training procedure as described previously. 

Results on selected GLUE tasks are shown in Table 6. In this table, we report the average Dev Set accuracy from 5 random restarts of fine-tuning. We can see that larger models lead to a strict accuracy improvement across all four datasets, even for MRPC which only has 3,600 labeled training examples, and is substantially different from the pre-training tasks. It is also perhaps surprising that we are able to achieve such significant improvements on top of models which are already quite large relative to the existing literature. For example, the largest Transformer explored in Vaswani et al. (2017) is (L=6, H=1024, A=16) with 100M parameters for the encoder, and the largest Transformer we have found in the literature is (L=64, H=512, A=2) with 235M parameters (Al-Rfou et al., 2018). By contrast, BERTBASE contains 110M parameters and BERTLARGE contains 340M parameters. 

It has long been known that increasing the model size will lead to continual improvements on large-scale tasks such as machine translation and language modeling, which is demonstrated by the LM perplexity of held-out training data shown in Table 6. However, we believe that this is the first work to demonstrate convincingly that scaling to extreme model sizes also leads to large improvements on very small scale tasks, provided that the model has been sufficiently pre-trained. Peters et al. (2018b) presented 

mixed results on the downstream task impact of increasing the pre-trained bi-LM size from two to four layers and Melamud et al. (2016) mentioned in passing that increasing hidden dimension size from 200 to 600 helped, but increasing further to 1,000 did not bring further improvements. Both of these prior works used a featurebased approach — we hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the taskspecific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small.

---

[referencia=32f3c7d144f036a0 score=0.391]
eters are fine-tuned using labeled data from the downstream tasks. Each downstream task has sep- 

arate fine-tuned models, even though they are initialized with the same pre-trained parameters. The question-answering example in Figure 1 will serve as a running example for this section. 

A distinctive feature of BERT is its unified architecture across different tasks. There is mini- 

bidirectional self-attention, while the GPT Trans- 

former uses constrained self-attention where every token can only attend to context to its left.<sup>4</sup> 1https://github.com/tensorflow/tensor2tensor 2http://nlp.seas.harvard.edu/2018/04/03/attention.html 

> 3In all cases we set the feed-forward/filter size to be 4 _H_ , 

i.e., 3072 for the _H_ = 768 and 4096 for the _H_ = 1024. 4We note that in the literature the bidirectional Trans- 

**Input/Output Representations** To make BERT handle a variety of down-stream tasks, our input representation is able to unambiguously represent both a single sentence and a pair of sentences (e.g., _⟨_ Question, Answer _⟩_ ) in one token sequence. Throughout this work, a “sentence” can be an arbitrary span of contiguous text, rather than an actual linguistic sentence. A “sequence” refers to the input token sequence to BERT, which may be a single sentence or two sentences packed together. 

We use WordPiece embeddings (Wu et al., 2016) with a 30,000 token vocabulary. The first token of every sequence is always a special classification token ([CLS]). The final hidden state corresponding to this token is used as the aggregate sequence representation for classification tasks. Sentence pairs are packed together into a single sequence. We differentiate the sentences in two ways. First, we separate them with a special token ([SEP]). Second, we add a learned embedding to every token indicating whether it belongs to sentence A or sentence B. As shown in Figure 1, we denote input embedding as _E_ , the final hidden vector of the special [CLS] token as _C ∈_ R<sup>_H_</sup> , and the final hidden vector for the _i_<sup>th</sup> input token as _Ti ∈_ R<sup>_H_</sup> .

---

[referencia=32f3c7d144f036a0 score=0.387]
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