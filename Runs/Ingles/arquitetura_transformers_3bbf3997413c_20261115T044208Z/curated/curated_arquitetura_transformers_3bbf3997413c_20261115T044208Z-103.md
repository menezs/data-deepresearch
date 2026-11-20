[referencia=46fd66187ec3e6ae score=0.536]
### **1. Introduction** 

Recently a series of _Large Language Models_ (LLMs) have been introduced (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022), with the largest dense language models now having over 500 billion parameters. These large autoregressive transformers (Vaswani et al., 2017) have demonstrated impressive performance on many tasks using a variety of evaluation protocols such as zero-shot, few-shot, and fine-tuning. 

The compute and energy cost for training large language models is substantial (Rae et al., 2021; Thoppilan et al., 2022) and rises with increasing model size. In practice, the allocated training compute budget is often known in advance: how many accelerators are available and for how long we want to use them. Since it is typically only feasible to train these large models once, accurately estimating the best model hyperparameters for a given compute budget is critical (Tay et al., 2021). 

Kaplan et al. (2020) showed that there is a power law relationship between the number of parameters in an autoregressive language model (LM) and its performance. As a result, the field has been training larger and larger models, expecting performance improvements. One notable conclusion in Kaplan et al. (2020) is that large models should not be trained to their lowest possible loss to be compute optimal. Whilst we reach the same conclusion, we estimate that large models should be trained for many more training tokens than recommended by the authors. Specifically, given a 10× increase computational budget, they suggests that the size of the model should increase 5 _._ 5× while the number of training tokens should only increase 1.8×. Instead, we find that model size and the number of training tokens should be scaled in equal proportions. 

Following Kaplan et al. (2020) and the training setup of GPT-3 (Brown et al., 2020), many of the recently trained large models have been trained for approximately 300 billion tokens (Table 1), in line with the approach of predominantly increasing model size when increasing compute. 

_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved

---

[referencia=46fd66187ec3e6ae score=0.344]
### **5. Discussion & Conclusion** 

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget. 

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that _Gopher_ is substantially over-sized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training _Chinchilla_ , a 70B parameter model, and show that it outperforms _Gopher_ and even larger models on nearly every measured evaluation task. 

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale ( _Chinchilla_ and _Gopher_ ), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log<sup>�</sup> _𝑁𝑜𝑝𝑡_ � at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of _Chinchilla_ to _Gopher_ validates our performance predictions, that have thus enabled training a better (and more 

15

---

[referencia=2cab3ea10b8b7ae2 score=0.285]
## **7 Related Work** 

Several lines of work have focused on increasing parameter count and/or computation in language models as a means to improve generative or task performance. An early work scaled LSTM based language models to over a billion parameters [JVS<sup>+</sup> 16]. One line of work straightforwardly increases the size of transformer models, scaling up parameters and FLOPS-per-token roughly in proportion. Work in this vein has successively increased model size: 213 million parameters [VSP<sup>+</sup> 17] in the original paper, 300 million parameters [DCLT18], 1.5 billion parameters [RWC<sup>+</sup> 19], 8 billion parameters [SPP<sup>+</sup> 19], 11 billion parameters [RSR<sup>+</sup> 19], and most recently 17 billion parameters [Tur20]. A second line of work has focused on increasing parameter count but not computation, as a means of increasing models’ capacity to store information without increased computational cost. These approaches rely on the conditional computation framework [BLC13] and specifically, the mixture-of-experts method [SMM<sup>+</sup> 17] has been used to produce 100 billion parameter models and more recently 50 billion parameter translation models [AJF19], though only a small fraction of the parameters are actually used on each forward pass. A third approach increases computation without increasing parameters; examples of this approach include adaptive computation time [Gra16] and the universal transformer [DGV<sup>+</sup> 18]. Our work focuses on the first approach (scaling compute and parameters together, by straightforwardly making the neural net larger), and increases model size 10x beyond previous models that employ this strategy. 

Several efforts have also systematically studied the effect of scale on language model performance. [KMH<sup>+</sup> 20, RRBS19, LWS<sup>+</sup> 20, HNA<sup>+</sup> 17], find a smooth power-law trend in loss as autoregressive language models are scaled up. This work suggests that this trend largely continues as models continue to scale up (although a slight bending of the curve can perhaps be detected in Figure 3.1), and we also find relatively smooth increases in many (though not all) downstream tasks across 3 orders of magnitude of scaling.

---

[referencia=2cab3ea10b8b7ae2 score=0.254]
## **8 Conclusion** 

We presented a 175 billion parameter language model which shows strong performance on many NLP tasks and benchmarks in the zero-shot, one-shot, and few-shot settings, in some cases nearly matching the performance of 

40 

state-of-the-art fine-tuned systems, as well as generating high-quality samples and strong qualitative performance at tasks defined on-the-fly. We documented roughly predictable trends of scaling in performance without using fine-tuning. We also discussed the social impacts of this class of model. Despite many limitations and weaknesses, these results suggest that very large language models may be an important ingredient in the development of adaptable, general language systems. 

## **Acknowledgements** 

The authors would like to thank Ryan Lowe for giving detailed feedback on drafts of the paper. Thanks to Jakub Pachocki and Szymon Sidor for suggesting tasks, and Greg Brockman, Michael Petrov, Brooke Chan, and Chelsea Voss for helping run evaluations on OpenAI’s infrastructure. Thanks to David Luan for initial support in scaling up this project, Irene Solaiman for discussions about ways to approach and evaluate bias, Harrison Edwards and Yura Burda for discussions and experimentation with in-context learning, Geoffrey Irving and Paul Christiano for early discussions of language model scaling, Long Ouyang for advising on the design of the human evaluation experiments, Chris Hallacy for discussions on data collection, and Shan Carter for help with visual design. Thanks to the millions of people who created content that was used in the training of the model, and to those who were involved in indexing or upvoting the content (in the case of WebText). Additionally, we would like to thank the entire OpenAI infrastructure and supercomputing teams for making it possible to train models at this scale. 

41

---

[referencia=2cab3ea10b8b7ae2 score=0.249]
Another approach to increasing generality and transfer-learning capability in language models is multi-task learning [Car97], which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results [LGH<sup>+</sup> 15, LSP<sup>+</sup> 18] and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets [PFB18] and pushed the boundaries on certain tasks [KKS<sup>+</sup> 20], but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a “natural” broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR<sup>+</sup> 17], human interaction [ZSW<sup>+</sup> 19b], or active learning [Mac92]. 

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality [DCLT18], prefixLM [DL15] and encoder-decoder architectures [LLG<sup>+</sup> 19, RSR<sup>+</sup> 19], random permutations during training [YDY<sup>+</sup> 19], architectures that improve the efficiency of sampling [DYY<sup>+</sup> 19], improvements in data and training procedures [LOG<sup>+</sup> 19], and efficiency increases in the embedding parameters [LCG<sup>+</sup> 19]. Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

---

[referencia=85f66a6419d173a7 score=0.227]
### **3 Empirical Results and Basic Power Laws** 

To characterize language model scaling we train a wide variety of models, varying a number of factors including: 

- Model size (ranging in size from 768 to 1.5 billion non-embedding parameters) 

- Dataset size (ranging from 22 million to 23 billion tokens) 

- Shape (including depth, width, attention heads, and feed-forward dimension) 

- Context length (1024 for most runs, though we also experiment with shorter contexts) 

- Batch size (2<sup>19</sup> for most runs, but we also vary it to measure the critical batch size) 

7 



<!-- Start of picture text -->
10%<br>8%<br>6% A wide range of architectures<br>achieve similar performance<br>4% 22% additional compute<br>compensates for 1% loss increase<br>2%<br>0%<br>Feed-Forward Ratio (dff / dmodel)  Attention Head Dimension  (dmodel / nhead)<br>50M Parameters Aspect Ratio (dmodel / nlayer) 25M Parameters<br>Loss Increase<br><!-- End of picture text -->

**Figure 5** Performance depends very mildly on model shape when the total number of non-embedding parameters _N_ is held fixed. The loss varies only a few percent over a wide range of shapes. Small differences in parameter counts are compensated for by using the fit to _L_ ( _N_ ) as a baseline. Aspect ratio in particular can vary by a factor of 40 while only slightly impacting performance; an ( _n_ layer _, d_ model) = (6 _,_ 4288) reaches a loss within 3% of the (48 _,_ 1600) model used in [RWC<sup>+</sup> 19]. 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.225]
**Modelling the scaling behavior.** Understanding the scaling behaviour of language models and their transfer properties has been important in the development of recent large models (Hernandez et al., 2021; Kaplan et al., 2020). Kaplan et al. (2020) first showed a predictable relationship between model size and loss over many orders of magnitude. The authors investigate the question of choosing the optimal model size to train for a given compute budget. Similar to us, they address this question by training various models. Our work differs from Kaplan et al. (2020) in several important ways. First, the authors use a fixed number of training tokens and learning rate schedule for all models; this prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find that setting the learning rate schedule to approximately match the number of training tokens results in the best final loss regardless of model size—see Figure A1. For a fixed learning rate cosine schedule to 130B tokens, the intermediate loss estimates (for _𝐷_<sup>′</sup> _<<_ 130B) are therefore overestimates of the loss of a model trained with a schedule length matching _𝐷_<sup>′</sup> . Using these intermediate losses results in underestimating the effectiveness of training models on less data than 130B tokens, and eventually contributes to the conclusion that model size should increase faster than training data size as compute budget increases. In contrast, our analysis predicts that both quantities should scale at roughly the same rate. Secondly, we include models with up to 16B parameters, as we observe that there is slight curvature in the FLOP-loss frontier (see Appendix E)—in fact, the majority of the models used in our analysis have more than 500 million parameters, in contrast the majority of runs in Kaplan et al. (2020) are significantly smaller—many being less than 100M parameters. 

Recently, Clark et al. (2022) specifically looked in to the scaling properties of Mixture of Expert 

3 

language models, showing that the scaling with number of experts diminishes as the model size increases—their approach models the loss as a function of two variables: the model size and the number of experts. However, the analysis is done with a fixed number of training tokens, as in Kaplan et al. (2020), potentially underestimating the improvements of branching.

---

[referencia=2cab3ea10b8b7ae2 score=0.221]
A more fundamental limitation of the general approach described in this paper – scaling up any LM-like model, whether autoregressive or bidirectional – is that it may eventually run into (or could already be running into) the limits of the 

33 

pretraining objective. Our current objective weights every token equally and lacks a notion of what is most important to predict and what is less important. [RRS20] demonstrate benefits of customizing prediction to entities of interest. Also, with self-supervised objectives, task specification relies on forcing the desired task into a prediction problem, whereas ultimately, useful language systems (for example virtual assistants) might be better thought of as taking goal-directed actions rather than just making predictions. Finally, large pretrained language models are not grounded in other domains of experience, such as video or real-world physical interaction, and thus lack a large amount of context about the world [BHT<sup>+</sup> 20]. For all these reasons, scaling pure self-supervised prediction is likely to hit limits, and augmentation with a different approach is likely to be necessary. Promising future directions in this vein might include learning the objective function from humans [ZSW<sup>+</sup> 19a], fine-tuning with reinforcement learning, or adding additional modalities such as images to provide grounding and a better model of the world [CLY<sup>+</sup> 19]. 

Another limitation broadly shared by language models is poor sample efficiency during pre-training. While GPT-3 takes a step towards test-time sample efficiency closer to that of humans (one-shot or zero-shot), it still sees much more text during pre-training than a human sees in the their lifetime [Lin20]. Improving pre-training sample efficiency is an important direction for future work, and might come from grounding in the physical world to provide additional information, or from algorithmic improvements.

---

[referencia=2cab3ea10b8b7ae2 score=0.145]
sufficient to enable a human to perform a new task to at least a reasonable degree of competence. Aside from pointing to a conceptual limitation in our current NLP techniques, this adaptability has practical advantages – it allows humans to seamlessly mix together or switch between many tasks and skills, for example performing addition during a lengthy dialogue. To be broadly useful, we would someday like our NLP systems to have this same fluidity and generality. 

One potential route towards addressing these issues is meta-learning<sup>1</sup> – which in the context of language models means the model develops a broad set of skills and pattern recognition abilities at training time, and then uses those abilities at inference time to rapidly adapt to or recognize the desired task (illustrated in Figure 1.1). Recent work [RWC<sup>+</sup> 19] attempts to do this via what we call “in-context learning”, using the text input of a pretrained language model as a form of task specification: the model is conditioned on a natural language instruction and/or a few demonstrations of the task and is then expected to complete further instances of the task simply by predicting what comes next. 

While it has shown some initial promise, this approach still achieves results far inferior to fine-tuning – for example [RWC<sup>+</sup> 19] achieves only 4% on Natural Questions, and even its 55 F1 CoQa result is now more than 35 points behind the state of the art. Meta-learning clearly requires substantial improvement in order to be viable as a practical method of solving language tasks.

---

[referencia=1098fc60be7ca2b0 score=0.138]
used for many recent large LMs—predicting the next token on a webpage from the internet—is different from the objective “follow the user’s instructions helpfully and safely” (Radford et al., 2019; Brown et al., 2020; Fedus et al., 2021; Rae et al., 2021; Thoppilan et al., 2022). Thus, we say that the language modeling objective is _misaligned_ . Averting these unintended behaviors is especially important for language models that are deployed and used in hundreds of applications. 

We make progress on aligning language models by training them to act in accordance with the user’s intention (Leike et al., 2018). This encompasses both explicit intentions such as following instructions and implicit intentions such as staying truthful, and not being biased, toxic, or otherwise harmful. Using the language of Askell et al. (2021), we want language models to be _helpful_ (they should help the user solve their task), _honest_ (they shouldn’t fabricate information or mislead the user), and _harmless_ (they should not cause physical, psychological, or social harm to people or the environment). We elaborate on the evaluation of these criteria in Section 3.6.

---

[referencia=46fd66187ec3e6ae score=0.122]
### **2. Related Work** 

**Large language models.** A variety of large language models have been introduced in the last few years. These include both dense transformer models (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022) and mixture-of-expert (MoE) models (Du et al., 2021; Fedus et al., 2021; Zoph et al., 2022). The largest dense transformers have passed 500 billion parameters (Smith et al., 2022). The drive to train larger and larger models is clear—so far increasing the size of language models has been responsible for improving the state-of-the-art in many language modelling tasks. Nonetheless, large language models face several challenges, including their overwhelming computational requirements (the cost of training and inference increase with model size) (Rae et al., 2021; Thoppilan et al., 2022) and the need for acquiring more high-quality training data. In fact, in this work we find that larger, high quality datasets will play a key role in any further scaling of language models.

---

[referencia=1098fc60be7ca2b0 score=0.106]
- Bojar, O., Chatterjee, R., Federmann, C., Haddow, B., Huck, M., Hokamp, C., Koehn, P., Logacheva, V., Monz, C., Negri, M., Post, M., Scarton, C., Specia, L., and Turchi, M. (2015). Findings of the 2015 workshop on statistical machine translation. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 1–46, Lisbon, Portugal. Association for Computational Linguistics. 

- Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. (2021). On the opportunities and risks of foundation models. _arXiv preprint arXiv:2108.07258_ . 

- Bostrom, N. (2014). _Superintelligence_ . Dunod. 

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ . 

- Buchanan, B., Lohn, A., Musser, M., and Sedova, K. (2021). Truth, lies, and automation. Technical report, Center for the Study of Emerging Technology. 

- Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. _Science_ , 356(6334):183–186. 

- Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., et al. (2021). Extracting training data from large language models. In _30th USENIX Security Symposium (USENIX Security 21)_ , pages 2633–2650.

---

[referencia=46fd66187ec3e6ae score=0.096]
many orders of magnitude, our analysis clearly suggests that given the training compute budget for 

many current LLMs, smaller models should have been trained on more tokens to achieve the most performant model. 

In Appendix C, we reproduce the IsoFLOP analysis on two additional datasets: C4 (Raffel et al., 

2020a) and GitHub code (Rae et al., 2021). In both cases we reach the similar conclusion that model size and number of training tokens should be scaled in equal proportions. 

8

---

[referencia=2cab3ea10b8b7ae2 score=0.094]
Another line of work goes in the opposite direction from scaling, attempting to preserve strong performance in language models that are as small as possible. This approach includes ALBERT [LCG<sup>+</sup> 19] as well as general [HVD15] and 

39 

task-specific [SDCW19, JYS<sup>+</sup> 19, KR16] approaches to distillation of language models. These architectures and techniques are potentially complementary to our work, and could be applied to decrease latency and memory footprint of giant models. 

As fine-tuned language models have neared human performance on many standard benchmark tasks, considerable effort has been devoted to constructing more difficult or open-ended tasks, including question answering [KPR<sup>+</sup> 19, IBGC<sup>+</sup> 14, CCE<sup>+</sup> 18, MCKS18], reading comprehension [CHI<sup>+</sup> 18, RCM19], and adversarially constructed datasets designed to be difficult for existing language models [SBBC19, NWD<sup>+</sup> 19]. In this work we test our models on many of these datasets. 

Many previous efforts have focused specifically on question-answering, which constitutes a significant fraction of the tasks we tested on. Recent efforts include [RSR<sup>+</sup> 19, RRS20], which fine-tuned an 11 billion parameter language model, and [GLT<sup>+</sup> 20], which focused on attending over a large corpus of data at test time. Our work differs in focusing on in-context learning but could be combined in the future with those of [GLT<sup>+</sup> 20, LPP<sup>+</sup> 20].

---

[referencia=2cab3ea10b8b7ae2 score=0.088]
Second, the potential to exploit spurious correlations in training data fundamentally grows with the expressiveness of the model and the narrowness of the training distribution. This can create problems for the pre-training plus fine-tuning paradigm, where models are designed to be large to absorb information during pre-training, but are then fine-tuned on very narrow task distributions. For instance [HLW<sup>+</sup> 20] observe that larger models do not necessarily generalize better out-of-distribution. There is evidence that suggests that the generalization achieved under this paradigm can be poor because the model is overly specific to the training distribution and does not generalize well outside it [YdC<sup>+</sup> 19, MPL19]. Thus, the performance of fine-tuned models on specific benchmarks, even when it is nominally at human-level, may exaggerate actual performance on the underlying task [GSL<sup>+</sup> 18, NK19]. 

Third, humans do not require large supervised datasets to learn most language tasks – a brief directive in natural language (e.g. “please tell me if this sentence describes something happy or something sad”) or at most a tiny number of demonstrations (e.g. “here are two examples of people acting brave; please give a third example of bravery”) is often 



**Figure 1.1: Language model meta-learning.** During unsupervised pre-training, a language model develops a broad set of skills and pattern recognition abilities. It then uses these abilities at inference time to rapidly adapt to or recognize the desired task. We use the term “in-context learning” to describe the inner loop of this process, which occurs within the forward-pass upon each sequence. The sequences in this diagram are not intended to be representative of the data a model would see during pre-training, but are intended to show that there are sometimes repeated sub-tasks embedded within a single sequence. 

3 



**Figure 1.2: Larger models make increasingly efficient use of in-context information.** We show in-context learning performance on a simple task requiring the model to remove random symbols from a word, both with and without a natural language task description (see Sec. 3.9.2). The steeper “in-context learning curves” for large models demonstrate improved ability to learn a task from contextual information. We see qualitatively similar behavior across a wide range of tasks.

---

[referencia=85f66a6419d173a7 score=0.079]
**Figure 21** In addition to the averaged loss, individual tokens within the 1024-token context also improve smoothly as model size increases. Training runs with shorter context _n_ ctx = 8 (dashed lines) perform better on early tokens, since they can allocate all of their capacity to them. 

#### **D.5 Context Dependence** 

The trends for loss as a function of model size are displayed for different tokens in the context in Figure 21. We see that models trained on _n_ ctx = 1024 show steady improvement with model size on all but the first token. 

Fixing model size, it appears that the loss scales as a power-law as a function of position _T_ in the context, see Figure 20. This may be a consequence of underlying power-law correlations in language [EP94, ACDE12, LT16], or a more general feature of the model architecture and optimization. It provides some suggestion for the potential benefits (or lack thereof) from training on larger contexts. Not only do larger models converge to better performance at _T_ = 1024, but they also improve more quickly at early tokens, suggesting that larger models are more efficient at detecting patterns with less contextual information. In the right-hand plot we show how per-token performance varies for a fixed model as a function of the training step. The model begins by learning short-range information, and only learns longer-range correlations later in training. 

We have also included models trained with a tiny context _n_ ctx = 8 in order to compare with our longer context models. Even modestly sized models trained on _n_ ctx = 8 can dominate our largest _n_ ctx = 1024 models on very early tokens. This also suggests that further improvements should be possible with much larger models trained on large contexts.

---

[referencia=46fd66187ec3e6ae score=0.070]
31 

|Primary Intended Users|DeepMind researchers. We will not make this model available<br>publicly.|
|---|---|
|Out-of-Scope Uses|Uses of the language model for language generation in harm-<br>ful or deceitful settings. More generally, the model should not<br>be used for downstream applications without further safety<br>and fairness mitigations.|
||**Factors**|
|Card Prompts – Relevant Factor|Relevant factors include which language is used. Our model is<br>trained on English data. Furthermore, in the analysis of mod-<br>els trained on the same corpus inRae et al.(2021), we found<br>it has unequal performance when modelling some dialects<br>(e.g., African American English). Our model is designed for<br>research. The model should not be used for downstream ap-<br>plications without further analysis on factors in the proposed<br>downstream application.|
|Card Prompts – Evaluation Factors|See the results inRae et al.(2021) which analyzes models<br>trained on the same text corpus.|
||**Metrics**|
|Model Performance Measures|• Perplexity and bits per byte on language modelling<br>datasets<br>• Accuracy on completion tasks, reading comprehension,<br>MMLU, BIG-bench and fact checking.<br>• Exact match accuracy for question answering.<br>• Generation toxicity from Real Toxicity Prompts (RTP)<br>alongside toxicity classifcation accuracy.<br>• Gender and occupation bias. Test include comparing<br>the probability of generating diferent gender terms<br>and the Winogender coreference resolution task.<br>We principally focus on_Chinchilla_’s performance compared<br>to_Gopher_on text likelihood prediction.|
|Decision thresholds|N/A|
|Approaches to Uncertainty and Vari-<br>ability|Due to the costs of training large language models, we did<br>not train _Chinchilla_ multiple times. However, the breadth<br>of our evaluation on a range of diferent task types gives a<br>reasonable estimate of the overall performance of the model.<br>Furthermore, the existence of another large model trained<br>on the same dataset (_Gopher_) provides a clear point of com-<br>parison.|



#### **Evaluation Data** 

32

---

[referencia=2cab3ea10b8b7ae2 score=0.068]
## **1 Introduction** 

Recent years have featured a trend towards pre-trained language representations in NLP systems, applied in increasingly flexible and task-agnostic ways for downstream transfer. First, single-layer representations were learned using word vectors [MCCD13, PSM14] and fed to task-specific architectures, then RNNs with multiple layers of representations and contextual state were used to form stronger representations [DL15, MBXS17, PNZtY18] (though still applied to task-specific architectures), and more recently pre-trained recurrent or transformer language models [VSP<sup>+</sup> 17] have been directly fine-tuned, entirely removing the need for task-specific architectures [RNSS18, DCLT18, HR18]. 

This last paradigm has led to substantial progress on many challenging NLP tasks such as reading comprehension, question answering, textual entailment, and many others, and has continued to advance based on new architectures and algorithms [RSR<sup>+</sup> 19, LOG<sup>+</sup> 19, YDY<sup>+</sup> 19, LCG<sup>+</sup> 19]. However, a major limitation to this approach is that while the architecture is task-agnostic, there is still a need for task-specific datasets and task-specific fine-tuning: to achieve strong performance on a desired task typically requires fine-tuning on a dataset of thousands to hundreds of thousands of examples specific to that task. Removing this limitation would be desirable, for several reasons. 

First, from a practical perspective, the need for a large dataset of labeled examples for every new task limits the applicability of language models. There exists a very wide range of possible useful language tasks, encompassing anything from correcting grammar, to generating examples of an abstract concept, to critiquing a short story. For many of these tasks it is difficult to collect a large supervised training dataset, especially when the process must be repeated for every new task.

---

[referencia=1098fc60be7ca2b0 score=0.067]
> **Training language models to follow instructions.** Our work is also related to research on crosstask generalization in language models, where LMs are fine-tuned on a broad range of public NLP datasets (usually prefixed with an appropriate instruction) and evaluated on a different set of NLP tasks. There has been a range of work in this domain (Yi et al., 2019; Mishra et al., 2021; Wei et al., 2021; Khashabi et al., 2020; Sanh et al., 2021; Aribandi et al., 2021), which differ in training and evaluation data, formatting of instructions, size of pretrained models, and other experimental details. A consistent finding across studies is that fine-tuning LMs on a range of NLP tasks, with instructions, improves their downstream performance on held-out tasks, both in the zero-shot and few-shot settings. 

Our work is also related to research on cross- 

There is also a related line of work on instruction following for navigation, where models are trained to follow natural language instructions to navigate in a simulated environment (Bahdanau et al., 2018; Abramson et al., 2020; Zhao et al., 2021). 

**Evaluating the harms of language models.** A goal of modifying the behavior of language models is to mitigate the harms of these models when they’re deployed in the real world. These risks have been extensively documented (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021). Language models can produce biased outputs (Dhamala et al., 2021; Liang et al., 2021; Manela et al., 2021; Caliskan et al., 2017; Kirk et al., 2021), leak private data (Carlini et al., 2021), generate misinformation (Solaiman et al., 2019; Buchanan et al., 2021), and be used maliciously; for a thorough review we direct the reader to Weidinger et al. (2021).

---

[referencia=46fd66187ec3e6ae score=0.062]
#### lightweight) model at the same compute budget. 

Though there has been significant recent work allowing larger and larger models to be trained, our analysis suggests an increased focus on dataset scaling is needed. Speculatively, we expect that scaling to larger and larger datasets is only beneficial when the data is high-quality. This calls for responsibly collecting larger datasets with a high focus on dataset quality. Larger datasets will require extra care to ensure train-test set overlap is properly accounted for, both in the language modelling loss but also with downstream tasks. Finally, training for trillions of tokens introduces many ethical and privacy concerns. Large datasets scraped from the web will contain toxic language, biases, and private information. With even larger datasets being used, the quantity (if not the frequency) of such information increases, which makes dataset introspection all the more important. _Chinchilla_ does suffer from bias and toxicity but interestingly it seems less affected than _Gopher_ . Better understanding how performance of large language models and toxicity interact is an important future research question. 

While we have applied our methodology towards the training of auto-regressive language models, we expect that there is a similar trade-off between model size and the amount of data in other modalities. As training large models is very expensive, choosing the optimal model size and training steps beforehand is essential. The methods we propose are easy to reproduce in new settings. 

### **6. Acknowledgements** 

We’d like to thank Jean-baptiste Alayrac, Kareem Ayoub, Chris Dyer, Nando de Freitas, Demis Hassabis, Geoffrey Irving, Koray Kavukcuoglu, Nate Kushman and Angeliki Lazaridou for useful comments on the manuscript. We’d like to thank Andy Brock, Irina Higgins, Michela Paganini, Francis Song, and other colleagues at DeepMind for helpful discussions. We are also very grateful to the JAX and XLA team for their support and assistance.