[referencia=2cab3ea10b8b7ae2 score=0.695]
In this paper, we test this hypothesis by training a 175 billion parameter autoregressive language model, which we call GPT-3, and measuring its in-context learning abilities. Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to be directly contained in the training set. For each task, we evaluate GPT-3 under 3 conditions: (a) “few-shot learning”, or in-context learning where we allow as many demonstrations as will fit into the model’s context window (typically 10 to 100), (b) “one-shot learning”, where we allow only one demonstration, and (c) “zero-shot” learning, where no demonstrations are allowed and only an instruction in natural language is given to the model. GPT-3 could also in principle be evaluated in the traditional fine-tuning setting, but we leave this to future work. 

Figure 1.2 illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a word. Model performance improves with the addition of a natural language task description, and with the number of examples in the model’s context, _K_ . Few-shot learning also improves dramatically with model size. Though the results in this case are particularly striking, the general trends with both model size and number of examples in-context hold for most tasks we study. We emphasize that these “learning” curves involve no gradient updates or fine-tuning, just increasing numbers of demonstrations given as conditioning. 

Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the the few-shot setting is sometimes competitive with or even occasionally surpasses state-of-the-art (despite state-of-the-art being held by fine-tuned models). For example, GPT-3 achieves 81.5 F1 on CoQA in the zero-shot setting, 84.0 F1 on CoQA in the one-shot setting, 85.0 F1 in the few-shot setting. Similarly, GPT-3 achieves 64.3% accuracy on TriviaQA in the zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting, the last of which is state-of-the-art relative to fine-tuned models operating in the same closed-book setting.

---

[referencia=a3e86ad05f37e40d score=0.466]
## **3 Framework** 

Our training procedure consists of two stages. The first stage is learning a high-capacity language model on a large corpus of text. This is followed by a fine-tuning stage, where we adapt the model to a discriminative task with labeled data. 

### **3.1 Unsupervised pre-training** 

Given an unsupervised corpus of tokens _U_ = _{u_ 1 _, . . . , un}_ , we use a standard language modeling objective to maximize the following likelihood: 



where _k_ is the size of the context window, and the conditional probability _P_ is modeled using a neural network with parameters Θ. These parameters are trained using stochastic gradient descent [51]. 

In our experiments, we use a multi-layer _Transformer decoder_ [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens: 





where _U_ = ( _u−k, . . . , u−_ 1) is the context vector of tokens, _n_ is the number of layers, _We_ is the token embedding matrix, and _Wp_ is the position embedding matrix.

---

[referencia=2cab3ea10b8b7ae2 score=0.414]
GPT-3 has several structural and algorithmic limitations, which could account for some of the issues above. We focused on exploring in-context learning behavior in autoregressive language models because it is straightforward to both sample and compute likelihoods with this model class. As a result our experiments do not include any bidirectional architectures or other training objectives such as denoising. This is a noticeable difference from much of the recent literature, which has documented improved fine-tuning performance when using these approaches over standard language models [RSR<sup>+</sup> 19]. Thus our design decision comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality. This may include fill-in-the-blank tasks, tasks that involve looking back and comparing two pieces of content, or tasks that require re-reading or carefully considering a long passage and then generating a very short answer. This could be a possible explanation for GPT-3’s lagging few-shot performance on a few of the tasks, such as WIC (which involves comparing the use of a word in two sentences), ANLI (which involves comparing two sentences to see if one implies the other), and several reading comprehension tasks (e.g. QuAC and RACE). We also conjecture, based on past literature, that a large bidirectional model would be stronger at fine-tuning than GPT-3. Making a bidirectional model at the scale of GPT-3, and/or trying to make bidirectional models work with few- or zero-shot learning, is a promising direction for future research, and could help achieve the “best of both worlds”. 

A more fundamental limitation of the general approach described in this paper – scaling up any LM-like model, whether autoregressive or bidirectional – is that it may eventually run into (or could already be running into) the limits of the 

33 

pretraining objective. Our current objective weights every token equally and lacks a notion of what is most important to

---

[referencia=2cab3ea10b8b7ae2 score=0.335]
Another approach to increasing generality and transfer-learning capability in language models is multi-task learning [Car97], which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results [LGH<sup>+</sup> 15, LSP<sup>+</sup> 18] and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets [PFB18] and pushed the boundaries on certain tasks [KKS<sup>+</sup> 20], but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a “natural” broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR<sup>+</sup> 17], human interaction [ZSW<sup>+</sup> 19b], or active learning [Mac92]. 

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality [DCLT18], prefixLM [DL15] and encoder-decoder architectures [LLG<sup>+</sup> 19, RSR<sup>+</sup> 19], random permutations during training [YDY<sup>+</sup> 19], architectures that improve the efficiency of sampling [DYY<sup>+</sup> 19], improvements in data and training procedures [LOG<sup>+</sup> 19], and efficiency increases in the embedding parameters [LCG<sup>+</sup> 19]. Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

---

[referencia=2cab3ea10b8b7ae2 score=0.233]
## **B Details of Model Training** 

To train all versions of GPT-3, we use Adam with _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 95, and _ϵ_ = 10<sup>_−_8</sup> , we clip the global norm of the gradient at 1.0, and we use cosine decay for learning rate down to 10% of its value, over 260 billion tokens (after 260 billion tokens, training continues at 10% of the original learning rate). There is a linear LR warmup over the first 375 million tokens. We also gradually increase the batch size linearly from a small value (32k tokens) to the full value over the first 4-12 billion tokens of training, depending on the model size. Data are sampled without replacement during training (until an epoch boundary is reached) to minimize overfitting. All models use weight decay of 0.1 to provide a small amount of regularization [LH17]. 

During training we always train on sequences of the full _n_ ctx = 2048 token context window, packing multiple documents into a single sequence when documents are shorter than 2048, in order to increase computational efficiency. Sequences with multiple documents are not masked in any special way but instead documents within a sequence are delimited with a special end of text token, giving the language model the information necessary to infer that context separated by the end of text token is unrelated. This allows for efficient training without need for any special sequence-specific masking.

---

[referencia=2cab3ea10b8b7ae2 score=0.201]
|**1**<br>**Intr**|**oduction**|**3**|
|---|---|---|
|**2**<br>**App**|**roach**|**6**|
|2.1|Model and Architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
|2.2|Training Dataset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
|2.3|Training Process<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>9|
|2.4|Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>10|
|**3**<br>**Res**|**ults**|**10**|
|3.1|Language Modeling, Cloze, and Completion Tasks<br>. . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>11|
|3.2|Closed Book Question Answering . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>13|
|3.3|Translation<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>14|

---

[referencia=2cab3ea10b8b7ae2 score=0.140]
23 



**Figure 3.11:** Few-shot performance on the five word scrambling tasks for different sizes of model. There is generally smooth improvement with model size although the random insertion task shows an upward slope of improvement with the 175B model solving the task the majority of the time. Scaling of one-shot and zero-shot performance is shown in the appendix. All tasks are done with _K_ = 100. 

random insertions, 38.6% on cycling letters, 40.2% on the easier anagram task, and 15.1% on the more difficult anagram task (where only the first and last letters are held fixed). None of the models can reverse the letters in a word. 

In the one-shot setting, performance is significantly weaker (dropping by half or more), and in the zero-shot setting the model can rarely perform any of the tasks (Table 3.10). This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial nature makes them unlikely to appear in the pre-training data (although we cannot confirm this with certainty). 

We can further quantify performance by plotting “in-context learning curves”, which show task performance as a function of the number of in-context examples. We show in-context learning curves for the Symbol Insertion task in Figure 1.2. We can see that larger models are able to make increasingly effective use of in-context information, including both task examples and natural language task descriptions. 

Finally, it is worth adding that solving these tasks requires character-level manipulations, whereas our BPE encoding operates on significant fractions of a word (on average _∼_ 0 _._ 7 words per token), so from the LM’s perspective succeeding at these tasks involves not just manipulating BPE tokens but understanding and pulling apart their substructure. Also, CL, A1, and A2 are not bijective (that is, the unscrambled word is not a deterministic function of the scrambled word), requiring the model to perform some search to find the correct unscrambling. Thus, the skills involved appear to require non-trivial pattern-matching and computation.

---

[referencia=2cab3ea10b8b7ae2 score=0.114]
The articles we selected were not in the models’ training data and the model outputs were formatted and selected programmatically to prevent human cherry-picking. All models used the same context to condition outputs on and were pre-trained with the same context size and the same article titles and subtitles were used as prompts for each model. However, we also ran an experiment to control for participant effort and attention that followed the same format but involved intentionally bad model generated articles. This was done by generating articles from a “control model”: a 160M parameter model with no context and increased output randomness. 

> 3 This task is also relevant to the potential misuse of language models discussed in Section 6.1. 

> 4We wanted to identify how good an average person on the internet is at detecting language model outputs, so we focused on participants drawn from the general US population. See Appendix E for details. 

25 

||Mean accuracy|95% Confdence<br>Interval (low, hi)|_t_compared to<br>control (_p_-value)|“I don’t know”<br>assignments|
|---|---|---|---|---|
|Control (deliberately bad model)|86%|83%–90%|-|3.6 %|
|GPT-3 Small|76%|72%–80%|3.9 (2_e_-4)|4.9%|
|GPT-3 Medium|61%|58%–65%|10.3 (7_e_-21)|6.0%|
|GPT-3 Large|68%|64%–72%|7.3 (3_e_-11)|8.7%|
|GPT-3 XL|62%|59%–65%|10.7 (1_e_-19)|7.5%|
|GPT-3 2.7B|62%|58%–65%|10.4 (5_e_-19)|7.1%|
|GPT-3 6.7B|60%|56%–63%|11.2 (3_e_-21)|6.2%|
|GPT-3 13B|55%|52%–58%|15.3 (1_e_-32)|7.1%|
|GPT-3 175B|52%|49%–54%|16.9 (1_e_-34)|7.8%|

---

[referencia=2cab3ea10b8b7ae2 score=0.082]
## OpenAI 

## **Abstract** 

Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions – something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art finetuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3’s few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general. 

> _∗_ Equal contribution 

> _†_ Johns Hopkins University, OpenAI 

Author contributions listed at end of paper.

---

[referencia=2cab3ea10b8b7ae2 score=0.073]
- Another line of work goes in the opposite direction from scaling, attempting to preserve strong performance in language 

- models that are as small as possible. This approach includes ALBERT [LCG<sup>+</sup> 19] as well as general [HVD15] and 

39 

task-specific [SDCW19, JYS<sup>+</sup> 19, KR16] approaches to distillation of language models. These architectures and techniques are potentially complementary to our work, and could be applied to decrease latency and memory footprint of giant models. 

As fine-tuned language models have neared human performance on many standard benchmark tasks, considerable effort has been devoted to constructing more difficult or open-ended tasks, including question answering [KPR<sup>+</sup> 19, IBGC<sup>+</sup> 14, CCE<sup>+</sup> 18, MCKS18], reading comprehension [CHI<sup>+</sup> 18, RCM19], and adversarially constructed datasets designed to be difficult for existing language models [SBBC19, NWD<sup>+</sup> 19]. In this work we test our models on many of these datasets. 

Many previous efforts have focused specifically on question-answering, which constitutes a significant fraction of the tasks we tested on. Recent efforts include [RSR<sup>+</sup> 19, RRS20], which fine-tuned an 11 billion parameter language model, and [GLT<sup>+</sup> 20], which focused on attending over a large corpus of data at test time. Our work differs in focusing on in-context learning but could be combined in the future with those of [GLT<sup>+</sup> 20, LPP<sup>+</sup> 20].

---

[referencia=2cab3ea10b8b7ae2 score=0.071]
## **2 Approach** 

Our basic pre-training approach, including model, data, and training, is similar to the process described in [RWC<sup>+</sup> 19], with relatively straightforward scaling up of the model size, dataset size and diversity, and length of training. Our use of in-context learning is also similar to [RWC<sup>+</sup> 19], but in this work we systematically explore different settings for learning within the context. Therefore, we start this section by explicitly defining and contrasting the different settings that we will be evaluating GPT-3 on or could in principle evaluate GPT-3 on. These settings can be seen as lying on a spectrum of how much task-specific data they tend to rely on. Specifically, we can identify at least four points on this spectrum (see Figure 2.1 for an illustration):

---

[referencia=a3e86ad05f37e40d score=0.067]
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

[referencia=2cab3ea10b8b7ae2 score=0.065]
sufficient to enable a human to perform a new task to at least a reasonable degree of competence. Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages – it allows humans to seamlessly mix together or switch between many tasks and skills, for example performing addition during a lengthy dialogue. To be broadly useful, we would someday like our NLP systems to have this same fluidity and generality. 

One potential route towards addressing these issues is meta-learning<sup>1</sup> – which in the context of language models means the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task (illustrated in Figure 1.1). Recent work [RWC<sup>+</sup> 19] attempts to do this via what we call “in-context learning”, using the text input of a pretrained language model as a form of task specification: the model is conditioned on a natural language instruction and/or a few demonstrations of the task and is then expected to complete further instances of the task simply by predicting what comes next. 

While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning – for example [RWC<sup>+</sup> 19] achieves only 4% on Natural Questions, and even its 55 F1 CoQa result is now more than 35 points behind the state of the art. Meta-learning clearly requires substantial improvement in order to be viable as a practical method of solving language tasks.

---

[referencia=2cab3ea10b8b7ae2 score=0.062]
A limitation, or at least uncertainty, associated with few-shot learning in GPT-3 is ambiguity about whether few-shot learning actually learns new tasks “from scratch” at inference time, or if it simply recognizes and identifies tasks that it has learned during training. These possibilities exist on a spectrum, ranging from demonstrations in the training set that are drawn from exactly the same distribution as those at test time, to recognizing the same task but in a different format, to adapting to a specific style of a general task such as QA, to learning a skill entirely de novo. Where GPT-3 is on this spectrum may also vary from task to task. Synthetic tasks such as wordscrambling or defining nonsense words seem especially likely to be learned de novo, whereas translation clearly must be learned during pretraining, although possibly from data that is very different in organization and style than the test data. Ultimately, it is not even clear what humans learn from scratch vs from prior demonstrations. Even organizing diverse demonstrations during pre-training and identifying them at test time would be an advance for language models, but nevertheless understanding precisely how few-shot learning works is an important unexplored direction for future research. 

A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of models of this scale in their current form. One possible future direction to address this is distillation [HVD15] of large 

models down to a manageable size for specific tasks. Large models such as GPT-3 contain a very wide range of skills, 

most of which are not needed for a specific task, suggesting that in principle aggressive distillation may be possible. Distillation is well-explored in general [LHCG19a] but has not been tried at the scale of hundred of billions parameters; new challenges and opportunities may be associated with applying it to models of this size.

---

[referencia=a3e86ad05f37e40d score=0.060]
### **3.2 Supervised fine-tuning** 

After training the model with the objective in Eq. 1, we adapt the parameters to the supervised target task. We assume a labeled dataset _C_ , where each instance consists of a sequence of input tokens, _x_<sup>1</sup> _, . . . , x_<sup>_m_</sup> , along with a label _y_ . The inputs are passed through our pre-trained model to obtain the final transformer block’s activation _h_<sup>_m_</sup> _l_<sup>, which is then fed into an added linear output layer with</sup> parameters _Wy_ to predict _y_ : 



This gives us the following objective to maximize: 



We additionally found that including language modeling as an auxiliary objective to the fine-tuning helped learning by (a) improving generalization of the supervised model, and (b) accelerating convergence. This is in line with prior work [50, 43], who also observed improved performance with such an auxiliary objective. Specifically, we optimize the following objective (with weight _λ_ ): 



Overall, the only extra parameters we require during fine-tuning are _Wy_ , and embeddings for delimiter tokens (described below in Section 3.3). 

3 





Figure 1: **(left)** Transformer architecture and training objectives used in this work. **(right)** Input transformations for fine-tuning on different tasks. We convert all structured inputs into token sequences to be processed by our pre-trained model, followed by a linear+softmax layer.

---

[referencia=2cab3ea10b8b7ae2 score=0.056]
Metalearning in language models has been utilized in [RWC<sup>+</sup> 19], though with much more limited results and no systematic study. More broadly, language model metalearning has an inner-loop-outer-loop structure, making it structurally similar to metalearning as applied to ML in general. Here there is an extensive literature, including matching networks [VBL<sup>+</sup> 16], RL2 [DSC<sup>+</sup> 16], learning to optimize [RL16, ADG<sup>+</sup> 16, LM17] and MAML [FAL17]. Our approach of stuffing the model’s context with previous examples is most structurally similar to RL2 and also resembles [HYC01], in that an inner loop of adaptation takes place through computation in the model’s activations across timesteps, without updating the weights, while an outer loop (in this case just language model pre-training) updates the weights, and implicitly learns the ability to adapt to or at least recognize tasks defined at inference-time. Few-shot auto-regressive density estimation was explored in [RCP<sup>+</sup> 17] and [GWC<sup>+</sup> 18] studied low-resource NMT as a few-shot learning problem. 

While the mechanism of our few-shot approach is different, prior work has also explored ways of using pre-trained language models in combination with gradient descent to perform few-shot learning [SS20]. Another sub-field with similar goals is semi-supervised learning where approaches such as UDA [XDH<sup>+</sup> 19] also explore methods of fine-tuning when very little labeled data is available. 

Giving multi-task models instructions in natural language was first formalized in a supervised setting with [MKXS18] and utilized for some tasks (such as summarizing) in a language model with [RWC<sup>+</sup> 19]. The notion of presenting tasks in natural language was also explored in the text-to-text transformer [RSR<sup>+</sup> 19], although there it was applied for multi-task fine-tuning rather than for in-context learning without weight updates.

---

[referencia=a3e86ad05f37e40d score=0.042]
For our model architecture, we use the _Transformer_ [62], which has been shown to perform strongly on various tasks such as machine translation [62], document generation [34], and syntactic parsing [29]. This model choice provides us with a more structured memory for handling long-term dependencies in text, compared to alternatives like recurrent networks, resulting in robust transfer performance across diverse tasks. During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens. As we demonstrate in our experiments, these adaptations enable us to fine-tune effectively with minimal changes to the architecture of the pre-trained model. 

We evaluate our approach on four types of language understanding tasks – natural language inference, question answering, semantic similarity, and text classification. Our general task-agnostic model outperforms discriminatively trained models that employ architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test) [40], 5.7% on question answering (RACE) [30], 1.5% on textual entailment (MultiNLI) [66] and 5.5% on the recently introduced GLUE multi-task benchmark [64]. We also analyzed zero-shot behaviors of the pre-trained model on four different settings and demonstrate that it acquires useful linguistic knowledge for downstream tasks.

---

[referencia=a3e86ad05f37e40d score=0.041]
but is shuffled at a sentence level - destroying long-range structure. Our language model achieves a very low token level perplexity of 18.4 on this corpus. 

**Model specifications** Our model largely follows the original transformer work [62]. We trained a 12-layer decoder-only transformer with masked self-attention heads (768 dimensional states and 12 attention heads). For the position-wise feed-forward networks, we used 3072 dimensional inner states. We used the Adam optimization scheme [27] with a max learning rate of 2.5e-4. The learning rate was increased linearly from zero over the first 2000 updates and annealed to 0 using a cosine schedule. We train for 100 epochs on minibatches of 64 randomly sampled, contiguous sequences of 512 tokens. Since layernorm [2] is used extensively throughout the model, a simple weight initialization of _N_ (0 _,_ 0 _._ 02) was sufficient. We used a bytepair encoding (BPE) vocabulary with 40,000 merges [53] and residual, embedding, and attention dropouts with a rate of 0.1 for regularization. We also employed a modified version of L2 regularization proposed in [37], with _w_ = 0 _._ 01 on all non bias or gain weights. For the activation function, we used the Gaussian Error Linear Unit (GELU) [18]. We used learned position embeddings instead of the sinusoidal version proposed in the original work. We use the _ftfy_ library<sup>2</sup> to clean the raw text in BooksCorpus, standardize some punctuation and whitespace, and use the _spaCy_ tokenizer.<sup>3</sup> 

**Fine-tuning details** Unless specified, we reuse the hyperparameter settings from unsupervised pre-training. We add dropout to the classifier with a rate of 0.1. For most tasks, we use a learning rate of 6.25e-5 and a batchsize of 32. Our model finetunes quickly and 3 epochs of training was sufficient for most cases. We use a linear learning rate decay schedule with warmup over 0.2% of training. _λ_ was set to 0.5.

---

[referencia=2cab3ea10b8b7ae2 score=0.040]
### **2.4 Evaluation** 

For few-shot learning, we evaluate each example in the evaluation set by randomly drawing _K_ examples from that task’s training set as conditioning, delimited by 1 or 2 newlines depending on the task. For LAMBADA and Storycloze there is no supervised training set available so we draw conditioning examples from the development set and evaluate on the test set. For Winograd (the original, not SuperGLUE version) there is only one dataset, so we draw conditioning examples directly from it. 

_K_ can be any value from 0 to the maximum amount allowed by the model’s context window, which is _n_ ctx = 2048 for all models and typically fits 10 to 100 examples. Larger values of _K_ are usually but not always better, so when a separate development and test set are available, we experiment with a few values of _K_ on the development set and then run the best value on the test set. For some tasks (see Appendix G) we also use a natural language prompt in addition to (or for _K_ = 0, instead of) demonstrations. 

On tasks that involve choosing one correct completion from several options (multiple choice), we provide _K_ examples of context plus correct completion, followed by one example of context only, and compare the LM likelihood of each completion. For most tasks we compare the per-token likelihood (to normalize for length), however on a small number of datasets (ARC, OpenBookQA, and RACE) we gain additional benefit as measured on the development set _P_ <u>(completion</u> _<u>|</u>_ context) by normalizing by the unconditional probability of each completion, by computing _P_ (completion _|_ answer ~~c~~ ontext)<sup>, where</sup> answer ~~c~~ ontext is the string `"Answer: "` or `"A: "` and is used to prompt that the completion should be an answer but is otherwise generic. 

On tasks that involve binary classification, we give the options more semantically meaningful names (e.g. “True” or “False” rather than 0 or 1) and then treat the task like multiple choice; we also sometimes frame the task similar to what is done by [RSR<sup>+</sup> 19] (see Appendix G) for details.

---

[referencia=2cab3ea10b8b7ae2 score=0.035]
**Figure G.8:** Formatted dataset example for OpenBookQA. When predicting, we normalize by the unconditional probability of each answer as described in 2. 

|`Context` _→_|`Making a cake:`<br>`Several cake pops are shown on a display.`<br>`A woman and girl`<br>`are shown making the cake pops in a kitchen.`<br>`They`|
|---|---|
|`Correct Answer` _→_<br>`Incorrect Answer` _→_<br>`Incorrect Answer` _→_<br>`Incorrect Answer` _→_|`bake them, then frost and decorate.`<br>`taste them as they place them on plates.`<br>`put the frosting on the cake as they pan it.`<br>`come out and begin decorating the cake as well.`<br>**Figure G.9:** Formatted dataset example for HellaSwag|
|`Context` _→_|`anli 3:`<br>`anli 3:`<br>`We shut the loophole which has American workers actually`<br>`subsidizing the loss of their own job.`<br>`They just passed an expansion of`<br>`that loophole in the last few days:`<br>`$43 billion of giveaways, including`<br>`favors to the oil and gas industry and the people importing ceiling fans`<br>`from China.`<br>`Question:`<br>`The loophole is now gone True, False, or Neither?`|
|`Correct Answer` _→_<br>`Incorrect Answer` _→_<br>`Incorrect Answer` _→_|`False`<br>`True`<br>`Neither`|
|`Context` _→_|**Figure G.10:** Formatted dataset example for ANLI R3<br>`Question:`<br>`George wants to warm his hands quickly by rubbing them.`<br>`Which`<br>`skin surface will produce the most heat?`<br>`Answer:`|
|`Correct Answer` _→_<br>`Incorrect Answer` _→_<br>`Incorrect Answer` _→_|`dry palms`<br>`wet palms`<br>`palms covered with oil`|
|`Incorrect Answer` _→_|`palms covered with lotion`|



**Figure G.11:** Formatted dataset example for ARC (Challenge). When predicting, we normalize by the unconditional probability of each answer as described in 2.