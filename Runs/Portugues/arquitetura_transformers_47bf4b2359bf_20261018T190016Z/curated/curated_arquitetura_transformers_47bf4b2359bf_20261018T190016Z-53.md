[referencia=a3e86ad05f37e40d score=0.092]
## **3 Framework** 

Our training procedure consists of two stages. The first stage is learning a high-capacity language model on a large corpus of text. This is followed by a fine-tuning stage, where we adapt the model to a discriminative task with labeled data. 

### **3.1 Unsupervised pre-training** 

Given an unsupervised corpus of tokens _U_ = _{u_ 1 _, . . . , un}_ , we use a standard language modeling objective to maximize the following likelihood: 



where _k_ is the size of the context window, and the conditional probability _P_ is modeled using a neural network with parameters Θ. These parameters are trained using stochastic gradient descent [51]. 

In our experiments, we use a multi-layer _Transformer decoder_ [34] for the language model, which is a variant of the transformer [62]. This model applies a multi-headed self-attention operation over the input context tokens followed by position-wise feedforward layers to produce an output distribution over target tokens: 





where _U_ = ( _u−k, . . . , u−_ 1) is the context vector of tokens, _n_ is the number of layers, _We_ is the token embedding matrix, and _Wp_ is the position embedding matrix.

---

[referencia=2cab3ea10b8b7ae2 score=0.088]
Another approach to increasing generality and transfer-learning capability in language models is multi-task learning [Car97], which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results [LGH<sup>+</sup> 15, LSP<sup>+</sup> 18] and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets [PFB18] and pushed the boundaries on certain tasks [KKS<sup>+</sup> 20], but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a “natural” broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR<sup>+</sup> 17], human interaction [ZSW<sup>+</sup> 19b], or active learning [Mac92]. 

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality [DCLT18], prefixLM [DL15] and encoder-decoder architectures [LLG<sup>+</sup> 19, RSR<sup>+</sup> 19], random permutations during training [YDY<sup>+</sup> 19], architectures that improve the efficiency of sampling [DYY<sup>+</sup> 19], improvements in data and training procedures [LOG<sup>+</sup> 19], and efficiency increases in the embedding parameters [LCG<sup>+</sup> 19]. Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

---

[referencia=2cab3ea10b8b7ae2 score=0.032]
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

[referencia=a3e86ad05f37e40d score=0.030]
### **3.3 Task-specific input transformations** 

For some tasks, like text classification, we can directly fine-tune our model as described above. Certain other tasks, like question answering or textual entailment, have structured inputs such as ordered sentence pairs, or triplets of document, question, and answers. Since our pre-trained model was trained on contiguous sequences of text, we require some modifications to apply it to these tasks. Previous work proposed learning task specific architectures on top of transferred representations [44]. Such an approach re-introduces a significant amount of task-specific customization and does not use transfer learning for these additional architectural components. Instead, we use a traversal-style approach [52], where we convert structured inputs into an ordered sequence that our pre-trained model can process. These input transformations allow us to avoid making extensive changes to the architecture across tasks. We provide a brief description of these input transformations below and Figure 1 provides a visual illustration. All transformations include adding randomly initialized start and end tokens ( _⟨s⟩_ , _⟨e⟩_ ). 

> **Textual entailment** For entailment tasks, we concatenate the premise _p_ and hypothesis _h_ token sequences, with a delimiter token ($) in between. 

**Similarity** For similarity tasks, there is no inherent ordering of the two sentences being compared. To reflect this, we modify the input sequence to contain both possible sentence orderings (with a delimiter in between) and process each independently to produce two sequence representations _h_<sup>_m_</sup> _l_ which are added element-wise before being fed into the linear output layer. 

**Question Answering and Commonsense Reasoning** For these tasks, we are given a context document _z_ , a question _q_ , and a set of possible answers _{ak}_ . We concatenate the document context and question with each possible answer, adding a delimiter token in between to get [ _z_ ; _q_ ; $; _ak_ ]. Each of these sequences are processed independently with our model and then normalized via a softmax layer to produce an output distribution over possible answers.

---

[referencia=2cab3ea10b8b7ae2 score=0.026]
Sections 2.1-2.3 below give details on our models, training data, and training process respectively. Section 2.4 discusses the details of how we do few-shot, one-shot, and zero-shot evaluations. 

7 

|Model Name|_n_params|_n_layers|_d_model|_n_heads|_d_head|Batch Size|Learning Rate|
|---|---|---|---|---|---|---|---|
|GPT-3 Small|125M|12|768|12|64|0.5M|6_._0_×_10<sup>_−_4</sup><br>|
|GPT-3 Medium|350M|24|1024|16|64|0.5M|3_._0_×_10<sup>_−_4</sup>|
|GPT-3 Large|760M|24|1536|16|96|0.5M|2_._5_×_10<sup>_−_4</sup>|
|GPT-3 XL|1.3B|24|2048|24|128|1M|2_._0_×_10<sup>_−_4</sup>|
|GPT-3 2.7B|2.7B|32|2560|32|80|1M|1_._6_×_10<sup>_−_4</sup>|
|GPT-3 6.7B|6.7B|32|4096|32|128|2M|1_._2_×_10<sup>_−_4</sup><br>|
|GPT-3 13B|13.0B|40|5140|40|128|2M|1_._0_×_10<sup>_−_4</sup>|
|GPT-3 175B or “GPT-3”|175.0B|96|12288|96|128|3.2M|0_._6_×_10<sup>_−_4</sup>|



**Table 2.1:** Sizes, architectures, and learning hyper-parameters (batch size in tokens and learning rate) of the models which we trained. All models were trained for a total of 300 billion tokens.

---

[referencia=a3e86ad05f37e40d score=0.022]
For our model architecture, we use the _Transformer_ [62], which has been shown to perform strongly on various tasks such as machine translation [62], document generation [34], and syntactic parsing [29]. This model choice provides us with a more structured memory for handling long-term dependencies in text, compared to alternatives like recurrent networks, resulting in robust transfer performance across diverse tasks. During transfer, we utilize task-specific input adaptations derived from traversal-style approaches [52], which process structured text input as a single contiguous sequence of tokens. As we demonstrate in our experiments, these adaptations enable us to fine-tune effectively with minimal changes to the architecture of the pre-trained model. 

We evaluate our approach on four types of language understanding tasks – natural language inference, question answering, semantic similarity, and text classification. Our general task-agnostic model outperforms discriminatively trained models that employ architectures specifically crafted for each task, significantly improving upon the state of the art in 9 out of the 12 tasks studied. For instance, we achieve absolute improvements of 8.9% on commonsense reasoning (Stories Cloze Test) [40], 5.7% on question answering (RACE) [30], 1.5% on textual entailment (MultiNLI) [66] and 5.5% on the recently introduced GLUE multi-task benchmark [64]. We also analyzed zero-shot behaviors of the pre-trained model on four different settings and demonstrate that it acquires useful linguistic knowledge for downstream tasks.

---

[referencia=2cab3ea10b8b7ae2 score=0.019]
- **7 Related Work** Several lines of work have focused on increasing parameter count and/or computation in language models as a means to improve generative or task performance. An early work scaled LSTM based language models to over a billion parameters [JVS<sup>+</sup> 16]. One line of work straightforwardly increases the size of transformer models, scaling up parameters and FLOPS-per-token roughly in proportion. Work in this vein has successively increased model size: 213 million parameters [VSP<sup>+</sup> 17] in the original paper, 300 million parameters [DCLT18], 1.5 billion parameters [RWC<sup>+</sup> 19], 8 billion parameters [SPP<sup>+</sup> 19], 11 billion parameters [RSR<sup>+</sup> 19], and most recently 17 billion parameters [Tur20]. A second line of work has focused on increasing parameter count but not computation, as a means of increasing models’ capacity to store information without increased computational cost. These approaches rely on the conditional computation framework [BLC13] and specifically, the mixture-of-experts method [SMM<sup>+</sup> 17] has been 

- used to produce 100 billion parameter models and more recently 50 billion parameter translation models [AJF19], though only a small fraction of the parameters are actually used on each forward pass. A third approach increases computation without increasing parameters; examples of this approach include adaptive computation time [Gra16] and the universal transformer [DGV<sup>+</sup> 18]. Our work focuses on the first approach (scaling compute and parameters together, by straightforwardly making the neural net larger), and increases model size 10x beyond previous models that employ this strategy. 

- Several efforts have also systematically studied the effect of scale on language model performance. [KMH<sup>+</sup> 20, RRBS19, LWS<sup>+</sup> 20, HNA<sup>+</sup> 17], find a smooth power-law trend in loss as autoregressive language models are scaled up. 

- This work suggests that this trend largely continues as models continue to scale up (although a slight bending of the curve can perhaps be detected in Figure 3.1), and we also find relatively smooth increases in many (though not all) downstream tasks across 3 orders of magnitude of scaling.

---

[referencia=a3e86ad05f37e40d score=0.018]
### **3.2 Supervised fine-tuning** 

After training the model with the objective in Eq. 1, we adapt the parameters to the supervised target task. We assume a labeled dataset _C_ , where each instance consists of a sequence of input tokens, _x_<sup>1</sup> _, . . . , x_<sup>_m_</sup> , along with a label _y_ . The inputs are passed through our pre-trained model to obtain the final transformer block’s activation _h_<sup>_m_</sup> _l_<sup>, which is then fed into an added linear output layer with</sup> parameters _Wy_ to predict _y_ : 



This gives us the following objective to maximize: 



We additionally found that including language modeling as an auxiliary objective to the fine-tuning helped learning by (a) improving generalization of the supervised model, and (b) accelerating convergence. This is in line with prior work [50, 43], who also observed improved performance with such an auxiliary objective. Specifically, we optimize the following objective (with weight _λ_ ): 



Overall, the only extra parameters we require during fine-tuning are _Wy_ , and embeddings for delimiter tokens (described below in Section 3.3). 

3 





Figure 1: **(left)** Transformer architecture and training objectives used in this work. **(right)** Input transformations for fine-tuning on different tasks. We convert all structured inputs into token sequences to be processed by our pre-trained model, followed by a linear+softmax layer.

---

[referencia=2cab3ea10b8b7ae2 score=0.017]
|4D+|acc|n/a|50|005|005000|000005005015400|000<br>000010|000000010080140|000<br>005005|000015015040255||
|4D-<br>|acc|n/a<br>|50<br>|.<br>0.00<br>|. .<br>0.00 0.00<br>|. . . . .<br>0.00 0.00 0.00 0.10 7.50<br>|.<br>. .<br>0.00<br>0.00 0.00<br><br>|. . . . .<br>0.00 0.05 0.00 0.50 14.0<br>|.<br>. .<br>0.00<br>0.05 0.00<br><br>|. . . . .<br>0.00 0.10 0.05 0.40 26.8<br>||
|5D+|acc|n/a|50|0.00|0.00 0.00|0.00 0.00 0.00 0.00 0.65|0.00<br>0.00 0.00|0.00 0.00 0.00 0.05 3.45|0.00<br>0.00 0.00|0.00 0.00 0.00 0.05 9.30||
|5D-|acc|n/a|50|0.00|0.00 0.00|0.00 0.00 0.00 0.00 0.80|0.00<br>0.00 0.00|0.00 0.00 0.00 0.05 3.75|0.00<br>0.00 0.00|0.00 0.00 0.00 0.00 9.90||

---

[referencia=2cab3ea10b8b7ae2 score=0.016]
23 



**Figure 3.11:** Few-shot performance on the five word scrambling tasks for different sizes of model. There is generally smooth improvement with model size although the random insertion task shows an upward slope of improvement with the 175B model solving the task the majority of the time. Scaling of one-shot and zero-shot performance is shown in the appendix. All tasks are done with _K_ = 100. 

random insertions, 38.6% on cycling letters, 40.2% on the easier anagram task, and 15.1% on the more difficult anagram task (where only the first and last letters are held fixed). None of the models can reverse the letters in a word. 

In the one-shot setting, performance is significantly weaker (dropping by half or more), and in the zero-shot setting the model can rarely perform any of the tasks (Table 3.10). This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial nature makes them unlikely to appear in the pre-training data (although we cannot confirm this with certainty). 

We can further quantify performance by plotting “in-context learning curves”, which show task performance as a function of the number of in-context examples. We show in-context learning curves for the Symbol Insertion task in Figure 1.2. We can see that larger models are able to make increasingly effective use of in-context information, including both task examples and natural language task descriptions. 

Finally, it is worth adding that solving these tasks requires character-level manipulations, whereas our BPE encoding operates on significant fractions of a word (on average _∼_ 0 _._ 7 words per token), so from the LM’s perspective succeeding at these tasks involves not just manipulating BPE tokens but understanding and pulling apart their substructure. Also, CL, A1, and A2 are not bijective (that is, the unscrambled word is not a deterministic function of the scrambled word), requiring the model to perform some search to find the correct unscrambling. Thus, the skills involved appear to require non-trivial pattern-matching and computation.

---

[referencia=2cab3ea10b8b7ae2 score=0.014]
|Model|Total train<br>compute<br>(PF-days)|Total train<br>compute<br>(fops)|Params<br>(M)|Training tokens<br>(billions)|Flops<br>per param<br>per token|Mult for<br>bwd pass|Fwd-pass<br>fops per<br>active param<br>per token|Frac of<br>params active<br>for each<br>token|
|---|---|---|---|---|---|---|---|---|
|T5-Small|2.08E+00|1.80E+20|60|1,000|3|3|1|0.5|
|T5-Base|7.64E+00|6.60E+20|220|1,000|3|3|1|0.5|
|T5-Large|2.67E+01|2.31E+21|770|1,000|3|3|1|0.5|
|T5-3B|1.04E+02|9.00E+21|3,000|1,000|3|3|1|0.5|
|T5-11B|3.82E+02|3.30E+22|11,000|1,000|3|3|1|0.5|
|BERT-Base|1.89E+00|1.64E+20|109|250|6|3|2|1.0|
|BERT-Large|6.16E+00|5.33E+20|355|250|6|3|2|1.0|
|RoBERTa-Base|1.74E+01|1.50E+21|125|2,000|6|3|2|1.0|
|RoBERTa-Large|4.93E+01|4.26E+21|355|2,000|6|3|2|1.0|
|GPT-3 Small|2.60E+00|2.25E+20|125|300|6|3|2|1.0|
|GPT-3 Medium|7.42E+00|6.41E+20|356|300|6|3|2|1.0|

---

[referencia=2cab3ea10b8b7ae2 score=0.012]
A limitation, or at least uncertainty, associated with few-shot learning in GPT-3 is ambiguity about whether few-shot learning actually learns new tasks “from scratch” at inference time, or if it simply recognizes and identifies tasks that it has learned during training. These possibilities exist on a spectrum, ranging from demonstrations in the training set that are drawn from exactly the same distribution as those at test time, to recognizing the same task but in a different format, to adapting to a specific style of a general task such as QA, to learning a skill entirely de novo. Where GPT-3 is on this spectrum may also vary from task to task. Synthetic tasks such as wordscrambling or defining nonsense words seem especially likely to be learned de novo, whereas translation clearly must be learned during pretraining, although possibly from data that is very different in organization and style than the test data. Ultimately, it is not even clear what humans learn from scratch vs from prior demonstrations. Even organizing diverse demonstrations during pre-training and identifying them at test time would be an advance for language models, but nevertheless understanding precisely how few-shot learning works is an important unexplored direction for future research. 

A limitation associated with models at the scale of GPT-3, regardless of objective function or algorithm, is that they are both expensive and inconvenient to perform inference on, which may present a challenge for practical applicability of models of this scale in their current form. One possible future direction to address this is distillation [HVD15] of large 

models down to a manageable size for specific tasks. Large models such as GPT-3 contain a very wide range of skills, 

most of which are not needed for a specific task, suggesting that in principle aggressive distillation may be possible. Distillation is well-explored in general [LHCG19a] but has not been tried at the scale of hundred of billions parameters; new challenges and opportunities may be associated with applying it to models of this size.

---

[referencia=a3e86ad05f37e40d score=0.011]
Table 5: Analysis of various model ablations on different tasks. Avg. score is a unweighted average of all the results. ( _mc_ = Mathews correlation, _acc_ =Accuracy, _pc_ =Pearson correlation) 

|Method|Avg. Score|CoLA|SST2|MRPC|STSB|QQP|MNLI|QNLI|RTE|
|---|---|---|---|---|---|---|---|---|---|
|||(mc)|(acc)|(F1)|(pc)|(F1)|(acc)|(acc)|(acc)|
|Transformer w/ aux LM (full)|74.7|45.4|91.3|82.3|82.0|**70.3**|**81.8**|**88.1**|**56.0**|
|Transformer w/o pre-training|59.9|18.9|84.0|79.4|30.9|65.5|75.7|71.2|53.8|
|Transformer w/o aux LM|**75.0**|**47.9**|**92.0**|**84.9**|**83.2**|69.8|81.1|86.9|54.4|
|LSTM w/ aux LM|69.1|30.3|90.5|83.2|71.8|68.1|73.7|81.1|54.6|



attentional memory of the transformer assists in transfer compared to LSTMs. We designed a series of heuristic solutions that use the underlying generative model to perform tasks without supervised finetuning. We visualize the effectiveness of these heuristic solutions over the course of generative pre-training in Fig 2(right). We observe the performance of these heuristics is stable and steadily increases over training suggesting that generative pretraining supports the learning of a wide variety of task relevant functionality. We also observe the LSTM exhibits higher variance in its zero-shot performance suggesting that the inductive bias of the Transformer architecture assists in transfer.

---

[referencia=2cab3ea10b8b7ae2 score=0.008]
**Table 3.10:** GPT-3 175B performance on various word unscrambling and word manipulation tasks, in zero-, one-, and few-shot settings. CL is “cycle letters in word”, A1 is anagrams of but the first and last letters, A2 is anagrams of all but the first and last two letters, RI is “Random insertion in word”, RW is “reversed words”. 

outperforms few-shot learning for all smaller models. All three settings for the full GPT-3 are shown in Table 3.9, and model capacity scaling for all three settings is shown in Appendix H. 

To spot-check whether the model is simply memorizing specific arithmetic problems, we took the 3-digit arithmetic problems in our test set and searched for them in our training data in both the forms `"<NUM1> + <NUM2> ="` and `"<NUM1> plus <NUM2>"` . Out of 2,000 addition problems we found only 17 matches (0.8%) and out of 2,000 subtraction problems we found only 2 matches (0.1%), suggesting that only a trivial fraction of the correct answers could have been memorized. In addition, inspection of incorrect answers reveals that the model often makes mistakes such as not carrying a “1”, suggesting it is actually attempting to perform the relevant computation rather than memorizing a table. 

Overall, GPT-3 displays reasonable proficiency at moderately complex arithmetic in few-shot, one-shot, and even zero-shot settings.

---

[referencia=a3e86ad05f37e40d score=0.008]
- [19] K. M. Hermann, T. Kocisky, E. Grefenstette, L. Espeholt, W. Kay, M. Suleyman, and P. Blunsom. Teaching machines to read and comprehend. In _Advances in Neural Information Processing Systems_ , pages 1693– 1701, 2015. 

- [20] G. E. Hinton, S. Osindero, and Y.-W. Teh. A fast learning algorithm for deep belief nets. _Neural computation_ , 18(7):1527–1554, 2006. 

- [21] J. Howard and S. Ruder. Universal language model fine-tuning for text classification. _Association for Computational Linguistics (ACL)_ , 2018. 

- [22] Y. Jernite, S. R. Bowman, and D. Sontag. Discourse-based objectives for fast unsupervised sentence representation learning. _arXiv preprint arXiv:1705.00557_ , 2017. 

- [23] Y. Ji and J. Eisenstein. Discriminative improvements to distributional sentence similarity. In _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing_ , pages 891–896, 2013. 

9

---

[referencia=2cab3ea10b8b7ae2 score=0.007]
|eQs|acc|es|.<br>|.|. .|. . . . .|.<br>. .|. . . . .|.<br>. .|. . . . .||
|Ro_→_En 16|BLEU-|mb test|39.9<br>64|2.08|2.71 3.09|3.15 16.3 8.34 20.2 19.9|0.55<br>15.4 23.0|26.3 30.6 33.2 35.6 38.6|1.25<br>20.7 25.8|29.2 33.1 34.8 37.0 39.5||
|Ro_→_En 16<br>|BLEU-<br>|sb<br>test<br>|64<br><br>|2.39<br>|3.08 3.49<br>|3.56 16.8 8.75 20.8 20.9<br>|0.65<br>15.9 23.6<br><br>|26.8 31.3 34.2 36.7 40.0<br>|1.40<br>21.3 26.6<br><br>|30.1 34.3 36.2 38.4 41.3<br>||

---

[referencia=2cab3ea10b8b7ae2 score=0.007]
|2Dx<br>|acc|n/a<br>|50<br>|2.20<br>|2.25 2.65<br>|2.10 2.55 5.80 6.15 19.8<br>|1.35<br>2.35 3.35<br><br>|2.35 4.75 9.15 11.0 27.4<br>|1.35<br>2.90 2.70<br><br>|2.85 4.25 6.10 7.05 29.2<br>||
|1DC|acc|n/a|50|1.25|2.95 2.75|0.05 0.30 2.35 0.75 9.75|1.90<br>2.80 2.85|3.65 6.45 9.15 8.20 14.3|1.70<br>2.15 3.90|5.75 6.20 7.60 9.95 21.3||
|Cycled Letters<br>|acc<br>|n/a<br>|100<br>|0.62<br>|0.71 2.85<br>|0.00 0.63 1.35 2.58 3.66<br>|1.67<br>4.36 5.68<br><br>|6.46 6.25 9.41 15.1 21.7<br>|4.63<br>9.27 10.7<br><br>|14.5 16.7 21.9 27.7 37.9<br>||
|Anagrams 1<br>|acc|n/a<br>|100<br>|0.10<br>|0.14 0.40<br>|0.00 0.27 0.69 1.16 2.28<br>|0.21<br>0.61 1.12<br><br>|1.27 1.60 2.72 3.72 8.62<br>|0.50<br>1.27 2.13<br><br>|3.05 3.81 5.49 8.38 15.1<br>||

---

[referencia=2cab3ea10b8b7ae2 score=0.006]
|SQuADv2|em|dev|90.7<br>16|22.6|32.8 33.9|43.1 43.6 45.4 49.0 52.6|25.1<br>37.5 37.9|47.9 47.9 51.1 56.0 60.1|27.5<br>40.5 39.2|53.5 50.0 56.6 62.6 64.9||
|SQuADv2<br>CA|f1<br>f1|dev<br>d|93.0<br>16<br>907<br>5|28.3<br>345|40.2 41.4<br>550618|50.3 51.0 52.7 56.3 59.5<br>653711728763815|30.1<br>43.6 44.1<br>306<br>521616|54.0 54.1 57.1 61.8 65.4<br>661718751779840|32.1<br>45.5 44.9<br>311<br>520627|58.7 55.9 62.1 67.7 69.8<br>668732773799850||
|oQ<br>DROP|f1|ev<br>dev|.<br><br>89.1<br>20|.<br>9.40|. .<br>13.6 14.4|. . . . .<br>16.4 19.7 17.0 24.0 23.6|.<br>. .<br>11.7<br>18.1 20.9|. . . . .<br>23.0 26.4 27.3 29.2 34.3|.<br>. .<br>12.9<br>18.7 24.0|. . . . .<br>25.6 29.7 29.7 32.3 36.5||

---

[referencia=2cab3ea10b8b7ae2 score=0.005]
- [LPP<sup>+</sup> 20] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler,¨ Mike Lewis, Wen-tau Yih, Tim Rocktaschel,¨ Sebastian Riedel, and Kiela Douwe. Retrieval-augmented generation for knowledge-intensive nlp tasks. _arXiv preprint arXiv:2005.11401_ , 2020. 

- [LSP<sup>+</sup> 18] Peter J. Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. Generating Wikipedia by summarizing long sequences. _arXiv preprint arXiv:1801.10198_ , 2018. 

- [LWS<sup>+</sup> 20] Zhuohan Li, Eric Wallace, Sheng Shen, Kevin Lin, Kurt Keutzer, Dan Klein, and Joseph E. Gonzalez. Train large, then compress: Rethinking model size for efficient training and inference of transformers, 2020. 

- [LXL<sup>+</sup> 17] Guokun Lai, Qizhe Xie, Hanxiao Liu, Yiming Yang, and Eduard Hovy. Race: Large-scale reading comprehension dataset from examinations. _arXiv preprint arXiv:1704.04683_ , 2017. 

- [LYN<sup>+</sup> 20] Sheng-Chieh Lin, Jheng-Hong Yang, Rodrigo Nogueira, Ming-Feng Tsai, Chuan-Ju Wang, and Jimmy Lin. Tttttackling winogrande schemas. _arXiv preprint arXiv:2003.08380_ , 2020. 

- [Mac92] David. MacKay. Information-based objective functions for active data selection. _Neural Computation_ , 1992. 

71

---

[referencia=2cab3ea10b8b7ae2 score=0.005]
|GPT-3 Medium|7.42E+00|6.41E+20|356|300|6|3|2|1.0|
|GPT-3 Large|1.58E+01|1.37E+21|760|300|6|3|2|1.0|
|GPT-3 XL|2.75E+01|2.38E+21|1,320|300|6|3|2|1.0|
|GPT-3 2.7B|5.52E+01|4.77E+21|2,650|300|6|3|2|1.0|
|GPT-3 6.7B|1.39E+02|1.20E+22|6,660|300|6|3|2|1.0|
|GPT-3 13B|2.68E+02|2.31E+22|12,850|300|6|3|2|1.0|
|GPT-3 175B|3.64E+03|3.14E+23|174,600|300|6|3|2|1.0|



**Table D.1:** Starting from the right hand side and moving left, we begin with the number of training tokens that each model was trained with. Next we note that since T5 uses an encoder-decoder model, only half of the parameters are active for each token during a forward or backwards pass. We then note that each token is involved in a single addition and a single multiply for each active parameter in the forward pass (ignoring attention). Then we add a multiplier of 3x to account for the backwards pass (as computing both<sup>_∂p_</sup> _∂loss_<sup>_arams_</sup> and<sup>_<u>∂acts</u>_</sup> _∂loss_<sup>use a similar amount of compute as the</sup> forwards pass. Combining the previous two numbers, we get the total flops per parameter per token. We multiply this value by the total training tokens and the total parameters to yield the number of total flops used during training. We report both flops and petaflop/s-day (each of which are 8.64e+19 flops).