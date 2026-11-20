[referencia=2cab3ea10b8b7ae2 score=0.067]
In this paper, we test this hypothesis by training a 175 billion parameter autoregressive language model, which we call GPT-3, and measuring its in-context learning abilities. Specifically, we evaluate GPT-3 on over two dozen NLP datasets, as well as several novel tasks designed to test rapid adaptation to tasks unlikely to be directly contained in the training set. For each task, we evaluate GPT-3 under 3 conditions: (a) “few-shot learning”, or in-context learning where we allow as many demonstrations as will fit into the model’s context window (typically 10 to 100), (b) “one-shot learning”, where we allow only one demonstration, and (c) “zero-shot” learning, where no demonstrations are allowed and only an instruction in natural language is given to the model. GPT-3 could also in principle be evaluated in the traditional fine-tuning setting, but we leave this to future work. 

Figure 1.2 illustrates the conditions we study, and shows few-shot learning of a simple task requiring the model to remove extraneous symbols from a word. Model performance improves with the addition of a natural language task description, and with the number of examples in the model’s context, _K_ . Few-shot learning also improves dramatically with model size. Though the results in this case are particularly striking, the general trends with both model size and number of examples in-context hold for most tasks we study. We emphasize that these “learning” curves involve no gradient updates or fine-tuning, just increasing numbers of demonstrations given as conditioning. 

Broadly, on NLP tasks GPT-3 achieves promising results in the zero-shot and one-shot settings, and in the the few-shot setting is sometimes competitive with or even occasionally surpasses state-of-the-art (despite state-of-the-art being held by fine-tuned models). For example, GPT-3 achieves 81.5 F1 on CoQA in the zero-shot setting, 84.0 F1 on CoQA in the one-shot setting, 85.0 F1 in the few-shot setting. Similarly, GPT-3 achieves 64.3% accuracy on TriviaQA in the zero-shot setting, 68.0% in the one-shot setting, and 71.2% in the few-shot setting, the last of which is state-of-the-art relative to fine-tuned models operating in the same closed-book setting.

---

[referencia=2cab3ea10b8b7ae2 score=0.032]
Another recent trend in language modeling may offer a way forward. In recent years the capacity of transformer language models has increased substantially, from 100 million parameters [RNSS18], to 300 million parameters [DCLT18], to 1.5 billion parameters [RWC<sup>+</sup> 19], to 8 billion parameters [SPP<sup>+</sup> 19], 11 billion parameters [RSR<sup>+</sup> 19], and finally 17 billion parameters [Tur20]. Each increase has brought improvements in text synthesis and/or downstream NLP tasks, and there is evidence suggesting that log loss, which correlates well with many downstream tasks, follows a smooth trend of improvement with scale [KMH<sup>+</sup> 20]. Since in-context learning involves absorbing many skills and tasks within the parameters of the model, it is plausible that in-context learning abilities might show similarly strong gains with scale. 

> 1In the context of language models this has sometimes been called “zero-shot transfer”, but this term is potentially ambiguous: the method is “zero-shot” in the sense that no gradient updates are performed, but it often involves providing inference-time demonstrations to the model, so is not truly learning from zero examples. To avoid this confusion, we use the term “meta-learning” to capture the inner-loop / outer-loop structure of the general method, and the term “in context-learning” to refer to the inner loop of meta-learning. We further specialize the description to “zero-shot”, “one-shot”, or “few-shot” depending on how many demonstrations are provided at inference time. These terms are intended to remain agnostic on the question of whether the model learns new tasks from scratch at inference time or simply recognizes patterns seen during training – this is an important issue which we discuss later in the paper, but “meta-learning” is intended to encompass both possibilities, and simply describes the inner-outer loop structure. 

4 



**Figure 1.3: Aggregate performance for all 42 accuracy-denominated benchmarks** While zero-shot performance improves steadily with model size, few-shot performance increases more rapidly, demonstrating that larger models are more proficient at in-context learning. See Figure 3.8 for a more detailed analysis on SuperGLUE, a standard NLP benchmark suite.

---

[referencia=2cab3ea10b8b7ae2 score=0.025]
## **3 Results** 

In Figure 3.1 we display training curves for the 8 models described in Section 2. For this graph we also include 6 additional extra-small models with as few as 100,000 parameters. As observed in [KMH<sup>+</sup> 20], language modeling performance follows a power-law when making efficient use of training compute. After extending this trend by two more orders of magnitude, we observe only a slight (if any) departure from the power-law. One might worry that these improvements in cross-entropy loss come only from modeling spurious details of our training corpus. However, we will see in the following sections that improvements in cross-entropy loss lead to consistent performance gains across a broad spectrum of natural language tasks. 

Below, we evaluate the 8 models described in Section 2 (the 175 billion parameter parameter GPT-3 and 7 smaller models) on a wide range of datasets. We group the datasets into 9 categories representing roughly similar tasks. 

In Section 3.1 we evaluate on traditional language modeling tasks and tasks that are similar to language modeling, such as Cloze tasks and sentence/paragraph completion tasks. In Section 3.2 we evaluate on “closed book” question answering tasks: tasks which require using the information stored in the model’s parameters to answer general knowledge questions. In Section 3.3 we evaluate the model’s ability to translate between languages (especially one-shot and few-shot). In Section 3.4 we evaluate the model’s performance on Winograd Schema-like tasks. In Section 3.5 we evaluate on datasets that involve commonsense reasoning or question answering. In Section 3.6 we evaluate on reading comprehension tasks, in Section 3.7 we evaluate on the SuperGLUE benchmark suite, and in 3.8 we briefly explore NLI. Finally, in Section 3.9, we invent some additional tasks designed especially to probe in-context learning abilities – these tasks focus on on-the-fly reasoning, adaptation skills, or open-ended text synthesis. We evaluate all tasks in the few-shot, one-shot, and zero-shot settings. 

10

---

[referencia=2cab3ea10b8b7ae2 score=0.012]
### **3.6 Reading Comprehension** 

Next we evaluate GPT-3 on the task of reading comprehension. We use a suite of 5 datasets including abstractive, multiple choice, and span based answer formats in both dialog and single question settings. We observe a wide spread in GPT-3’s performance across these datasets suggestive of varying capability with different answer formats. In general we observe GPT-3 is on par with initial baselines and early results trained using contextual representations on each respective dataset. 

GPT-3 performs best (within 3 points of the human baseline) on CoQA [RCM19] a free-form conversational dataset and performs worst (13 F1 below an ELMo baseline) on QuAC [CHI<sup>+</sup> 18] a dataset which requires modeling structured dialog acts and answer span selections of teacher-student interactions. On DROP [DWD<sup>+</sup> 19], a dataset testing discrete reasoning and numeracy in the context of reading comprehension, GPT-3 in a few-shot setting outperforms the fine-tuned BERT baseline from the original paper but is still well below both human performance and state-of-the-art approaches which augment neural networks with symbolic systems [RLL<sup>+</sup> 19]. On SQuAD 2.0 [RJL18], GPT-3 demonstrates its few-shot learning capabilities, improving by almost 10 F1 (to 69.8) compared to a zero-shot setting. This allows it to slightly outperform the best fine-tuned result in the original paper. On RACE [LXL<sup>+</sup> 17], a multiple choice dataset of middle school and high school english examinations, GPT-3 performs relatively weakly and is only competitive with the earliest work utilizing contextual representations and is still 45% behind SOTA.

---

[referencia=2cab3ea10b8b7ae2 score=0.011]
Second, the potential to exploit spurious correlations in training data fundamentally grows with the expressiveness of the model and the narrowness of the training distribution. This can create problems for the pre-training plus fine-tuning paradigm, where models are designed to be large to absorb information during pre-training, but are then fine-tuned on very narrow task distributions. For instance [HLW<sup>+</sup> 20] observe that larger models do not necessarily generalize better out-of-distribution. There is evidence that suggests that the generalization achieved under this paradigm can be poor because the model is overly specific to the training distribution and does not generalize well outside it [YdC<sup>+</sup> 19, MPL19]. Thus, the performance of fine-tuned models on specific benchmarks, even when it is nominally at human-level, may exaggerate actual performance on the underlying task [GSL<sup>+</sup> 18, NK19]. 

Third, humans do not require large supervised datasets to learn most language tasks – a brief directive in natural language (e.g. “please tell me if this sentence describes something happy or something sad”) or at most a tiny number of demonstrations (e.g. “here are two examples of people acting brave; please give a third example of bravery”) is often 



**Figure 1.1: Language model meta-learning.** During unsupervised pre-training, a language model develops a broad set of skills and pattern recognition abilities. It then uses these abilities at inference time to rapidly adapt to or recognize the desired task. We use the term “in-context learning” to describe the inner loop of this process, which occurs within the forward-pass upon each sequence. The sequences in this diagram are not intended to be representative of the data a model would see during pre-training, but are intended to show that there are sometimes repeated sub-tasks embedded within a single sequence. 

3 



**Figure 1.2: Larger models make increasingly efficient use of in-context information.** We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural language task description (see Sec. 3.9.2). The steeper “in-context learning curves” for large models demonstrate improved ability to learn a task from contextual information. We see qualitatively similar behavior across a wide range of tasks.

---

[referencia=2cab3ea10b8b7ae2 score=0.010]
|`Context` _→_|

---

[referencia=2cab3ea10b8b7ae2 score=0.008]
Another approach to increasing generality and transfer-learning capability in language models is multi-task learning [Car97], which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results [LGH<sup>+</sup> 15, LSP<sup>+</sup> 18] and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets [PFB18] and pushed the boundaries on certain tasks [KKS<sup>+</sup> 20], but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a “natural” broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR<sup>+</sup> 17], human interaction [ZSW<sup>+</sup> 19b], or active learning [Mac92]. 

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality [DCLT18], prefixLM [DL15] and encoder-decoder architectures [LLG<sup>+</sup> 19, RSR<sup>+</sup> 19], random permutations during training [YDY<sup>+</sup> 19], architectures that improve the efficiency of sampling [DYY<sup>+</sup> 19], improvements in data and training procedures [LOG<sup>+</sup> 19], and efficiency increases in the embedding parameters [LCG<sup>+</sup> 19]. Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

---

[referencia=2cab3ea10b8b7ae2 score=0.007]
sufficient to enable a human to perform a new task to at least a reasonable degree of competence. Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages – it allows humans to seamlessly mix together or switch between many tasks and skills, for example performing addition during a lengthy dialogue. To be broadly useful, we would someday like our NLP systems to have this same fluidity and generality. 

One potential route towards addressing these issues is meta-learning<sup>1</sup> – which in the context of language models means the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task (illustrated in Figure 1.1). Recent work [RWC<sup>+</sup> 19] attempts to do this via what we call “in-context learning”, using the text input of a pretrained language model as a form of task specification: the model is conditioned on a natural language instruction and/or a few demonstrations of the task and is then expected to complete further instances of the task simply by predicting what comes next. 

While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning – for example [RWC<sup>+</sup> 19] achieves only 4% on Natural Questions, and even its 55 F1 CoQa result is now more than 35 points behind the state of the art. Meta-learning clearly requires substantial improvement in order to be viable as a practical method of solving language tasks.

---

[referencia=2cab3ea10b8b7ae2 score=0.006]
## **2 Approach** 

Our basic pre-training approach, including model, data, and training, is similar to the process described in [RWC<sup>+</sup> 19], with relatively straightforward scaling up of the model size, dataset size and diversity, and length of training. Our use of in-context learning is also similar to [RWC<sup>+</sup> 19], but in this work we systematically explore different settings for learning within the context. Therefore, we start this section by explicitly defining and contrasting the different settings that we will be evaluating GPT-3 on or could in principle evaluate GPT-3 on. These settings can be seen as lying on a spectrum of how much task-specific data they tend to rely on. Specifically, we can identify at least four points on this spectrum (see Figure 2.1 for an illustration):

---

[referencia=2cab3ea10b8b7ae2 score=0.006]
- **Figure 3.11:** Few-shot performance on the five word scrambling tasks for different sizes of model. There is generally smooth improvement with model size although the random insertion task shows an upward slope of improvement with the 175B model solving the task the majority of the time. Scaling of one-shot and zero-shot performance is shown in the appendix. All tasks are done with _K_ = 100. 

- random insertions, 38.6% on cycling letters, 40.2% on the easier anagram task, and 15.1% on the more difficult anagram task (where only the first and last letters are held fixed). None of the models can reverse the letters in a word. In the one-shot setting, performance is significantly weaker (dropping by half or more), and in the zero-shot setting the model can rarely perform any of the tasks (Table 3.10). This suggests that the model really does appear to learn these tasks at test time, as the model cannot perform them zero-shot and their artificial nature makes them unlikely to appear in the pre-training data (although we cannot confirm this with certainty). 

- We can further quantify performance by plotting “in-context learning curves”, which show task performance as a function of the number of in-context examples. We show in-context learning curves for the Symbol Insertion task in Figure 1.2. We can see that larger models are able to make increasingly effective use of in-context information, including both task examples and natural language task descriptions. 

- Finally, it is worth adding that solving these tasks requires character-level manipulations, whereas our BPE encoding operates on significant fractions of a word (on average _∼_ 0 _._ 7 words per token), so from the LM’s perspective succeeding 

- at these tasks involves not just manipulating BPE tokens but understanding and pulling apart their substructure. Also, CL, A1, and A2 are not bijective (that is, the unscrambled word is not a deterministic function of the scrambled word), requiring the model to perform some search to find the correct unscrambling. Thus, the skills involved appear to require non-trivial pattern-matching and computation. 

- **3.9.3 SAT Analogies**

---

[referencia=2cab3ea10b8b7ae2 score=0.004]
## **Contributions** 

**Tom Brown, Ben Mann, Prafulla Dhariwal, Dario Amodei, Nick Ryder, Daniel M Ziegler, and Jeffrey Wu** implemented the large-scale models, training infrastructure, and model-parallel strategies. 

**Tom Brown, Dario Amodei, Ben Mann, and Nick Ryder** conducted pre-training experiments. 

**Ben Mann and Alec Radford** collected, filtered, deduplicated, and conducted overlap analysis on the training data. 

**Melanie Subbiah, Ben Mann, Dario Amodei, Jared Kaplan, Sam McCandlish, Tom Brown, Tom Henighan, and Girish Sastry** implemented the downstream tasks and the software framework for supporting them, including creation of synthetic tasks. 

**Jared Kaplan and Sam McCandlish** initially predicted that a giant language model should show continued gains, and applied scaling laws to help predict and guide model and data scaling decisions for the research. 

**Ben Mann** implemented sampling without replacement during training. 

**Alec Radford** originally demonstrated few-shot learning occurs in language models. 

**Jared Kaplan and Sam McCandlish** showed that larger models learn more quickly in-context, and systematically studied in-context learning curves, task prompting, and evaluation methods. 

**Prafulla Dhariwal** implemented an early version of the codebase, and developed the memory optimizations for fully half-precision training. 

**Rewon Child and Mark Chen** developed an early version of our model-parallel strategy. 

**Rewon Child and Scott Gray** contributed the sparse transformer. 

**Aditya Ramesh** experimented with loss scaling strategies for pretraining. 

**Melanie Subbiah and Arvind Neelakantan** implemented, experimented with, and tested beam search. 

**Pranav Shyam** worked on SuperGLUE and assisted with connections to few-shot learning and meta-learning literature. **Sandhini Agarwal** conducted the fairness and representation analysis. 

**Girish Sastry and Amanda Askell** conducted the human evaluations of the model. 

**Ariel Herbert-Voss** conducted the threat analysis of malicious use. 

**Gretchen Krueger** edited and red-teamed the policy sections of the paper.

---

[referencia=2cab3ea10b8b7ae2 score=0.004]
Another line of work goes in the opposite direction from scaling, attempting to preserve strong performance in language models that are as small as possible. This approach includes ALBERT [LCG<sup>+</sup> 19] as well as general [HVD15] and 

39 

task-specific [SDCW19, JYS<sup>+</sup> 19, KR16] approaches to distillation of language models. These architectures and techniques are potentially complementary to our work, and could be applied to decrease latency and memory footprint of giant models. 

As fine-tuned language models have neared human performance on many standard benchmark tasks, considerable effort has been devoted to constructing more difficult or open-ended tasks, including question answering [KPR<sup>+</sup> 19, IBGC<sup>+</sup> 14, CCE<sup>+</sup> 18, MCKS18], reading comprehension [CHI<sup>+</sup> 18, RCM19], and adversarially constructed datasets designed to be difficult for existing language models [SBBC19, NWD<sup>+</sup> 19]. In this work we test our models on many of these datasets. 

Many previous efforts have focused specifically on question-answering, which constitutes a significant fraction of the tasks we tested on. Recent efforts include [RSR<sup>+</sup> 19, RRS20], which fine-tuned an 11 billion parameter language model, and [GLT<sup>+</sup> 20], which focused on attending over a large corpus of data at test time. Our work differs in focusing on in-context learning but could be combined in the future with those of [GLT<sup>+</sup> 20, LPP<sup>+</sup> 20].

---

[referencia=2cab3ea10b8b7ae2 score=0.004]
|3.4|Winograd-Style Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>16|
|3.5|Common Sense Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>17|
|3.6|Reading Comprehension . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>18|
|3.7|SuperGLUE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>18|
|3.8|NLI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>20|
|3.9|Synthetic and Qualitative Tasks . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>21|
|**4**<br>**Mea**|**suring and Preventing Memorization Of Benchmarks**|**29**|
|**5**<br>**Lim**|**itations**|**33**|
|**6**<br>**Bro**|**ader Impacts**|**34**|
|6.1|Misuse of Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>35|

---

[referencia=2cab3ea10b8b7ae2 score=0.004]
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

[referencia=2cab3ea10b8b7ae2 score=0.002]
GPT-3 has several structural and algorithmic limitations, which could account for some of the issues above. We focused on exploring in-context learning behavior in autoregressive language models because it is straightforward to both sample and compute likelihoods with this model class. As a result our experiments do not include any bidirectional architectures or other training objectives such as denoising. This is a noticeable difference from much of the recent literature, which has documented improved fine-tuning performance when using these approaches over standard language models [RSR<sup>+</sup> 19]. Thus our design decision comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality. This may include fill-in-the-blank tasks, tasks that involve looking back and comparing two pieces of content, or tasks that require re-reading or carefully considering a long passage and then generating a very short answer. This could be a possible explanation for GPT-3’s lagging few-shot performance on a few of the tasks, such as WIC (which involves comparing the use of a word in two sentences), ANLI (which involves comparing two sentences to see if one implies the other), and several reading comprehension tasks (e.g. QuAC and RACE). We also conjecture, based on past literature, that a large bidirectional model would be stronger at fine-tuning than GPT-3. Making a bidirectional model at the scale of GPT-3, and/or trying to make bidirectional models work with few- or zero-shot learning, is a promising direction for future research, and could help achieve the “best of both worlds”. 

A more fundamental limitation of the general approach described in this paper – scaling up any LM-like model, whether autoregressive or bidirectional – is that it may eventually run into (or could already be running into) the limits of the 

33

---

[referencia=2cab3ea10b8b7ae2 score=0.002]
- [BHT<sup>+</sup> 20] Yonatan Bisk, Ari Holtzman, Jesse Thomason, Jacob Andreas, Yoshua Bengio, Joyce Chai, Mirella Lapata, Angeliki Lazaridou, Jonathan May, Aleksandr Nisnevich, et al. Experience grounds language. _arXiv preprint arXiv:2004.10151_ , 2020. 

- [BLC13] Yoshua Bengio, Nicholas Leonard, and Aaron C. Courville.´ Estimating or propagating gradients through stochastic neurons for conditional computation. _Arxiv_ , 2013. 

- [BZB<sup>+</sup> 19] Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, and Yejin Choi. Piqa: Reasoning about physical commonsense in natural language. _arXiv preprint arXiv:1911.11641_ , 2019. 

- [Car97] Rich Caruana. Multitask learning. _Machine learning_ , 28(1), 1997. 

- [CB78] Susan Carey and Elsa Bartlett. Acquiring a single new word. _Proceedings of the Stanford Child Language Conference_ , 1978. 

- [CCE<sup>+</sup> 18] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge. _ArXiv_ , abs/1803.05457, 2018. 

- [CGRS19] Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers, 2019. 

- [CHI<sup>+</sup> 18] Eunsol Choi, He He, Mohit Iyyer, Mark Yatskar, Wen-tau Yih, Yejin Choi, Percy Liang, and Luke Zettlemoyer. Quac : Question answering in context. _Arxiv_ , 2018.

---

[referencia=2cab3ea10b8b7ae2 score=0.001]
## **8 Conclusion** 

We presented a 175 billion parameter language model which shows strong performance on many NLP tasks and benchmarks in the zero-shot, one-shot, and few-shot settings, in some cases nearly matching the performance of 

40 

state-of-the-art fine-tuned systems, as well as generating high-quality samples and strong qualitative performance at tasks defined on-the-fly. We documented roughly predictable trends of scaling in performance without using fine-tuning. We also discussed the social impacts of this class of model. Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language systems. 

## **Acknowledgements** 

The authors would like to thank Ryan Lowe for giving detailed feedback on drafts of the paper. Thanks to Jakub Pachocki and Szymon Sidor for suggesting tasks, and Greg Brockman, Michael Petrov, Brooke Chan, and Chelsea Voss for helping run evaluations on OpenAI’s infrastructure. Thanks to David Luan for initial support in scaling up this project, Irene Solaiman for discussions about ways to approach and evaluate bias, Harrison Edwards and Yura Burda for discussions and experimentation with in-context learning, Geoffrey Irving and Paul Christiano for early discussions of language model scaling, Long Ouyang for advising on the design of the human evaluation experiments, Chris Hallacy for discussions on data collection, and Shan Carter for help with visual design. Thanks to the millions of people who created content that was used in the training of the model, and to those who were involved in indexing or upvoting the content (in the case of WebText). Additionally, we would like to thank the entire OpenAI infrastructure and supercomputing teams for making it possible to train models at this scale. 

41

---

[referencia=2cab3ea10b8b7ae2 score=0.001]
`Target Completion` _→_ `mr. moncrieff` 

**Figure G.33:** Formatted dataset example for WSC 

`Context` _→_ `Q: ‘Nude Descending A Staircase’ is perhaps the most famous painting by which 20th century artist?` 

```
A:
```

`Target Completion` _→_ `MARCEL DUCHAMP Target Completion` _→_ `r mutt Target Completion` _→_ `duchamp Target Completion` _→_ `marcel duchamp Target Completion` _→_ `R.Mutt Target Completion` _→_ `Marcel duChamp Target Completion` _→_ `Henri-Robert-Marcel Duchamp Target Completion` _→_ `Marcel du Champ Target Completion` _→_ `henri robert marcel duchamp Target Completion` _→_ `Duchampian Target Completion` _→_ `Duchamp Target Completion` _→_ `duchampian Target Completion` _→_ `marcel du champ Target Completion` _→_ `Marcel Duchamp Target Completion` _→_ `MARCEL DUCHAMP` 

**Figure G.34:** Formatted dataset example for TriviaQA. TriviaQA allows for multiple valid completions. 

59 

|`Context` _→_|`Q: `|`What school did burne hogarth establish?`|
|---|---|---|
||`A:`||
|`Target Completion` _→_|`Sch`|`ool of Visual Arts`|



**Figure G.35:** Formatted dataset example for WebQA 

|`Context` _→_|`Keinesfalls d¨urfen `|`diese f¨ur den kommerziellen Gebrauch verwendet werden.`|
|---|---|---|
|`Target Completion` _→_|`=`<br>`In no case may they`|`be used for commercial purposes.`|



**Figure G.36:** Formatted dataset example for De _→_ En. This is the format for one- and few-shot learning, for this and other langauge tasks, the format for zero-shot learning is “Q: What is the _{_ language _}_ translation of _{_ sentence _}_ A: _{_ translation _}_ .”

---

[referencia=2cab3ea10b8b7ae2 score=0.001]
### **3.1.2 LAMBADA** 

The LAMBADA dataset [PKL<sup>+</sup> 16] tests the modeling of long-range dependencies in text – the model is asked to predict the last word of sentences which require reading a paragraph of context. It has recently been suggested that the continued scaling of language models is yielding diminishing returns on this difficult benchmark. [BHT<sup>+</sup> 20] reflect on the small 1.5% improvement achieved by a doubling of model size between two recent state of the art results ([SPP<sup>+</sup> 19] 

11 

|Setting|LAMBADA<br>(acc)|LAMBADA<br>(ppl)|StoryCloze<br>(acc)|HellaSwag<br>(acc)|
|---|---|---|---|---|
|SOTA|68.0<sup>_a_</sup>|8.63<sup>_b_</sup>|**91.8**<sup>_c_</sup>|**85.6**<sup>_d_</sup>|
|GPT-3 Zero-Shot|**76.2**|**3.00**|83.2|78.9|
|GPT-3 One-Shot|**72.5**|**3.35**|84.7|78.1|
|GPT-3 Few-Shot|**86.4**|**1.92**|87.7|79.3|



**Table 3.2: Performance on cloze and completion tasks.** GPT-3 significantly improves SOTA on LAMBADA while achieving respectable performance on two difficult completion prediction datasets.<sup>_a_</sup> [Tur20]<sup>_b_</sup> [RWC<sup>+</sup> 19]<sup>_c_</sup> [LDL19] _d_ [LCH+20] 



**Figure 3.2:** On LAMBADA, the few-shot capability of language models results in a strong boost to accuracy. GPT-3 2.7B outperforms the SOTA 17B parameter Turing-NLG [Tur20] in this setting, and GPT-3 175B advances the state of the art by 18%. Note zero-shot uses a different format from one-shot and few-shot as described in the text.

---

[referencia=2cab3ea10b8b7ae2 score=0.001]
- [CLC<sup>+</sup> 19] Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova. BoolQ: Exploring the surprising difficulty of natural yes/no questions. _arXiv preprint arXiv:1905.10044_ , 2019. 

- [CLY<sup>+</sup> 19] Yen-Chun Chen, Linjie Li, Licheng Yu, Ahmed El Kholy, Faisal Ahmed, Zhe Gan, Yu Cheng, and Jingjing Liu. Uniter: Learning universal image-text representations. _arXiv preprint arXiv:1909.11740_ , 2019. 

- [Cra17] Kate Crawford. The trouble with bias. _NIPS 2017 Keynote_ , 2017. 

- [DCLT18] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. _arXiv preprint arXiv:1810.04805_ , 2018. 

68