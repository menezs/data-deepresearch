[referencia=2d76bc16fcc7825d score=0.996]
# **Emergent Abilities of Large Language Models** 

**Jason Wei**<sup>1</sup> **Yi Tay**<sup>1</sup> **Rishi Bommasani**<sup>2</sup> **Colin Raffel**<sup>3</sup> **Barret Zoph**<sup>1</sup> **Sebastian Borgeaud**<sup>4</sup> **Dani Yogatama**<sup>4</sup> **Maarten Bosma**<sup>1</sup> **Denny Zhou**<sup>1</sup> **Donald Metzler**<sup>1</sup> **Ed H. Chi**<sup>1</sup> **Tatsunori Hashimoto**<sup>2</sup> **Oriol Vinyals**<sup>4</sup> **Percy Liang**<sup>2</sup> **Jeff Dean**<sup>1</sup> **William Fedus**<sup>1</sup> 

_jasonwei@google.com yitay@google.com nlprishi@stanford.edu craffel@gmail.com barretzoph@google.com sborgeaud@deepmind.com dyogatama@deepmind.com bosma@google.com dennyzhou@google.com metzler@google.com edchi@google.com thashim@stanford.edu vinyals@deepmind.com pliang@stanford.edu jeff@google.com liamfedus@google.com_ 

> 1 _Google Research_ 2 _Stanford University_ 3 _UNC Chapel Hill_ 4 _DeepMind_ 

**Reviewed on OpenReview:** _https://openreview.net/forum?id=yzkSU5zdwD_ 

## **Abstract** 

Scaling up language models has been shown to predictably improve performance and sample efficiency on a wide range of downstream tasks. This paper instead discusses an unpredictable phenomenon that we refer to as _emergent abilities_ of large language models. We consider an ability to be emergent if it is not present in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted simply by extrapolating the performance of smaller models. The existence of such emergence raises the question of whether additional scaling could potentially further expand the range of capabilities of language models.

---

[referencia=2d76bc16fcc7825d score=0.995]
|Here we will explore emergence with respect to model scale, as measured by training compute and number of<br>model parameters. Specifcally, we defne _emergent abilities of large language models_ as abilities that are<br>not present in smaller-scale models but are present in large-scale models; thus they cannot be predicted by<br>simply extrapolating the performance improvements on smaller-scale models (§2).<sup>1 </sup>We survey emergent<br>abilities as observed in a range of prior work, categorizing them in settings such as few-shot prompting (§3)<br>and augmented prompting strategies (§4). Emergence motivates future research on why such abilities are<br>acquired and whether more scaling will lead to further emergent abilities, which we highlight as important<br>questions for the feld (§5).|
|---|
|**2**<br>**Emergent Abilities Defnition**|
|As a broad concept, emergence is often used informally and can be reasonably interpreted in many diferent<br>ways. In this paper, we will consider a focused defnition of emergent abilities of large language models:|
|_An ability is emergent if it is not present in smaller models but is present in larger models._|

---

[referencia=2d76bc16fcc7825d score=0.989]
## **5 Discussion** 

We have seen that a range of abilities—in the few-shot prompting setup or otherwise—have thus far only been observed when evaluated on a sufficiently large language model. Hence, their emergence cannot be predicted by simply extrapolating performance on smaller-scale models. Emergent few-shot prompted tasks are also unpredictable in the sense that these tasks are not explicitly included in pre-training, and we likely do not know the full scope of few-shot prompted tasks that language models can perform. This raises the question of whether further scaling could potentially endow even-larger language models with new emergent abilities. Tasks that language models cannot currently do are prime candidates for future emergence; for instance, there are dozens of tasks in BIG-Bench for which even the largest GPT-3 and PaLM models do not achieve above-random performance (see Appendix E.4). 

The ability for scale to unpredictably enable new techniques is not just theoretical. Consider the Word in Context (WiC) benchmark (Pilehvar & Camacho-Collados, 2019) shown in Figure 2H, as a historical example. Here, scaling GPT-3 to around 3 _·_ 10<sup>23</sup> training FLOPs (175B parameters) failed to unlock above-random one-shot prompting performance.<sup>3</sup> Regarding this negative result, Brown et al. (2020) cited the model architecture of GPT-3 or the use of an autoregressive language modeling objective (rather than using a denoising training objective) as potential reasons, and suggested training a model of comparable size with bidirectional architecture as a remedy. However, later work found that further scaling a decoder-only language model was actually enough to enable above-random performance on this task. As is shown in Figure 2H, scaling PaLM (Chowdhery et al., 2022) from 3 _·_ 10<sup>23</sup> training FLOPs (62B parameters) to 3 _·_ 10<sup>24</sup> training 

> 3GPT-3 does achieve slightly above-random performance on the dev set with few-shot instead of one-shot prompting ( _∼_ 55%), but this above-random performance did not appear to be a result of scale and did not hold on the test set server. 

6 

Published in Transactions on Machine Learning Research <u>(08/2022)</u>

---

[referencia=2d76bc16fcc7825d score=0.984]
### **5.2 Beyond scaling** 

Although we may observe an emergent ability to occur at a certain scale, it is possible that the ability could be later achieved at a smaller scale—in other words, model scale is not the singular factor for unlocking an emergent ability. As the science of training large language models progresses, certain abilities may be unlocked for smaller models with new architectures, higher-quality data, or improved training procedures. For example, there are 14 BIG-Bench tasks<sup>5</sup> for which LaMDA 137B and GPT-3 175B models perform at near-random, but PaLM 62B in fact achieves above-random performance, despite having fewer model parameters and training FLOPs. While there is not an empirical study ablating every difference between PaLM 62B and prior models (the computational cost would be too high), potential reasons for the better performance of PaLM could include high-quality training data (e.g., more multilingual and code data than LaMDA) and architectural differences (e.g., split digit-encodings; see Section 2 in Chowdhery et al. (2022)). Another potentially way of unlocking emergence is through a different pre-training objective—it was shown in Tay et al. (2022c) that a computationally-efficient continued pre-training stage on a mixture-of-denoisers objective (Tay et al., 2022a) enabled emergent performance on several BIG-Bench tasks. 

Moreover, once an ability is discovered, further research may make the ability available for smaller scale models. Consider the nascent direction of enabling language models to follow natural language instructions describing a task (Wei et al., 2022a; Sanh et al., 2022; Ouyang et al., 2022, _inter alia_ ). Although Wei et al. (2022a) initially found that instruction-based finetuning only worked for 68B parameter or larger decoder-only 

> 4Though note that encoding world knowledge in parameters is just one approach; there are others (e.g., Guu et al., 2020; Borgeaud et al., 2021). 

> 5These tasks are enumerated in Appendix F. 

7 

Published in Transactions on Machine Learning Research <u>(08/2022)</u>

---

[referencia=2d76bc16fcc7825d score=0.983]
|_An ability is emergent if it is not present in smaller models but is present in larger models._|
|Emergent abilities would not have been directly predicted by extrapolating a scaling law (i.e. consistent<br>performance improvements) from small-scale models. When visualized via a scaling curve (_x_-axis: model<br>scale, _y_-axis: performance), emergent abilities show a clear pattern—performance is near-random until a<br>certain critical threshold of scale is reached, after which performance increases to substantially above random.<br>This qualitative change is also known as a_phase transition_—a dramatic change in overall behavior that would<br>not have been foreseen by examining smaller-scale systems (Huberman & Hogg, 1987).<br>Today’s language models have been scaled primarily along three factors: amount of computation, number<br>of model parameters, and training dataset size (Kaplan et al., 2020; Hofmann et al., 2022). In this paper,<br>we will analyze scaling curves by plotting the performance of diferent models where training compute for<br>each model is measured in FLOPs on the _x_-axis (Hofmann et al., 2022). Because language models trained<br>with more compute tend to also have more parameters, we additionally show plots with number of model<br>parameters as the _x_-axis in Appendix D (see Figure 11 and Figure 12, as well as Figure 4 and Figure 10).<br>Using training FLOPs or model parameters as the _x_-axis produces curves with similar shapes due to the fact<br>that most dense Transformer language model families have scaled training compute roughly proportionally<br>with model parameters (Kaplan et al., 2020).<br>Training dataset size is also an important factor, but we do not plot capabilities against it because many|



language model families use a fixed number of training examples for all model sizes (Brown et al., 2020; Rae et al., 2021; Chowdhery et al., 2022). Although we focus on training computation and model size here, there is not a single proxy that adequately captures all aspects of scale. For example, Chinchilla (Hoffmann et al.,

---

[referencia=2d76bc16fcc7825d score=0.973]
## **6 Conclusions** 

We have discussed emergent abilities of language models, for which meaningful performance has only been thus far observed at a certain computational scale. Emergent abilities can span a variety of language models, task types, and experimental scenarios. Such abilities are a recently discovered outcome of scaling up language models, and the questions of how they emerge and whether more scaling will enable further emergent abilities seem to be important future research directions for the field of NLP. 

### **Broader Impact Statement** 

In this paper, we surveyed results in the existing literature, without proposing new methods or models. As discussed in (§5), emergent abilities are unpredictable in several ways, and include emergent risks (§5.4). We believe these phenomena warrant careful study and raise important questions for the field. 

### **Acknowledgments** 

We thank Charles Sutton, Slav Petrov, Douglas Eck, Jason Freidenfelds, Jascha Sohl-Dickstein, Ethan Dyer, Dale Schuurmans, and Xavier Garcia for useful discussions and feedback on the manuscript. 

11 

Published in Transactions on Machine Learning Research <u>(08/2022)</u>

---

[referencia=2d76bc16fcc7825d score=0.969]
## **1 Introduction** 

Language models have revolutionized natural language processing (NLP) in recent years. It is now well-known that increasing the scale of language models (e.g., training compute, model parameters, etc.) can lead to better performance and sample efficiency on a range of downstream NLP tasks (Devlin et al., 2019; Brown et al., 2020, _inter alia_ ). In many cases, the effect of scale on performance can often be methodologically predicted via scaling laws—for example, scaling curves for cross-entropy loss have been shown to empirically span more than seven orders of magnitude (Kaplan et al., 2020; Hoffmann et al., 2022). On the other hand, performance for certain downstream tasks counterintuitively does not appear to continuously improve as a function of scale, and such tasks cannot be predicted ahead of time (Ganguli et al., 2022). 

In this paper, we will discuss the unpredictable phenomena of _emergent abilities_ of large language models. Emergence as an idea has been long discussed in domains such as physics, biology, and computer science (Anderson, 1972; Hwang et al., 2012; Forrest, 1990; Corradini & O’Connor, 2010; Harper & Lewis, 2012, _inter_ 

1 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

_alia_ ). We will consider the following general definition of emergence, adapted from Steinhardt (2022) and rooted in a 1972 essay called “More Is Different” by Nobel prize-winning physicist Philip Anderson (Anderson, 1972): 

_Emergence is when quantitative changes in a system result in qualitative changes in behavior._

---

[referencia=2d76bc16fcc7825d score=0.966]
### **5.1 Potential explanations of emergence** 

Although there are dozens of examples of emergent abilities, there are currently few compelling explanations for why such abilities emerge in the way they do. For certain tasks, there may be natural intuitions for why emergence requires a model larger than a particular threshold scale. For instance, if a multi-step reasoning task requires _l_ steps of sequential computation, this might require a model with a depth of at least _O_ ( _l_ ) layers. It is also reasonable to assume that more parameters and more training enable better memorization that could be helpful for tasks requiring world knowledge.<sup>4</sup> As an example, good performance on closed-book question-answering may require a model with enough parameters to capture the compressed knowledge base itself (though language model-based compressors can have higher compression ratios than conventional compressors (Bellard, 2021)). 

It is also important to consider the evaluation metrics used to measure emergent abilities (BIG-Bench, 2022). For instance, using exact string match as the evaluation metric for long-sequence targets may disguise compounding incremental improvements as emergence. Similar logic may apply for multi-step or arithmetic reasoning problems, where models are only scored on whether they get the final answer to a multi-step problem correct, without any credit given to partially correct solutions. However, the jump in final answer accuracy does not explain why the quality of intermediate steps suddenly emerges to above random, and using evaluation metrics that do not give partial credit are at best an incomplete explanation, because emergent abilities are still observed on many classification tasks (e.g., the tasks in Figure 2D–H). 

As an alternative evaluation, we measure cross-entropy loss, which is used in scaling laws for pre-training, for the six emergent BIG-Bench tasks, as detailed in Appendix A. This analysis follows the same experimental setup from BIG-Bench (2022) and affirms their conclusions for the six emergent tasks we consider. Namely, cross-entropy loss improves even for small model scales where the downstream metrics (exact match, BLEU, and accuracy) are close to random and do not improve, which shows that improvements in the log-likelihood of the target sequence can be masked by such downstream metrics. However, this analysis does not explain why downstream metrics are emergent or enable us to predict the scale at which emergence occurs. Overall, more work is needed to tease apart what enables scale to unlock emergent abilities.

---

[referencia=2d76bc16fcc7825d score=0.964]
2022) has one-fourth as many parameters as Gopher (Rae et al., 2021) but uses similar training compute; and sparse mixture-of-expert models have more parameters per training/inference compute than dense models (Fedus et al., 2021; Du et al., 2021). Overall, it may be wise to view emergence as a function of many correlated variables. For example, later in Figure 4 we will also plot emergence as a function of WikiText103 perplexity (Merity et al., 2016), which happens to closely correlate with training computation for Gopher/ Chinchilla (though this correlation may not hold in the long-run). Note that the scale at which an ability is first observed to emerge depends on a number of factors and is not an immutable property of the ability. For instance, emergence may occur with less training compute 

> 1This survey focuses on pre-trained Transformer language models. Emergent abilities in NLP more broadly, however, could go back to Miller et al. (2004), Liang (2005), or earlier. 

2 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

or fewer model parameters for models trained on higher-quality data. Conversely, emergent abilities also crucially depend on other factors such as not being limited by the amount of data, its quality, or the number of parameters in the model. Today’s language models are likely not trained optimally (Hoffmann et al., 2022), and our understanding of how to best train models will evolve over time. Our goal in this paper is not to characterize or claim that a specific scale is required to observe emergent abilities, but rather, we aim to discuss examples of emergent behavior in prior work.

---

[referencia=2d76bc16fcc7825d score=0.935]
**Frontier tasks.** Although language models can perform a wide range of tasks, there are still many tasks that even the largest language models to date cannot perform with above-random accuracy. Dozens of such tasks from BIG-Bench are enumerated in Appendix E.4; these tasks often involve abstract reasoning (e.g., playing Chess, challenging math, etc). Future research could potentially investigate why these abilities have not yet emerged, and how to enable models to perform these tasks. Looking forward, another growing direction could be multilingual emergence; results on multilingual BIG-Bench tasks indicate that both model scale and training data play a role in emergence (e.g., Figure 2D shows that both using PaLM’s training dataset and scaling to 62B parameters is required for question-answering in Persian). Other frontier tasks could include prompting in multiple modalities (Alayrac et al., 2022; Ramesh et al., 2022). 

**Understanding emergence.** Beyond research on unlocking further emergence, an open question for future research is how and why emergent abilities occur in large language models. This paper conducted initial analyses regarding scaling of the cross-entropy loss on BIG-Bench (Appendix A.1), different metrics for generative tasks (Appendix A.2), and which types of tasks emergence occurs (Appendix A.3 and Appendix B). These analyses did not provide complete answers to why emergence occurs or how to predict it. Future research could potentially analyze emergence in new ways (e.g., analyze the relationship between emergent tasks and similar data in training; create a synthetic task that requires multiple compositional sub-tasks and evaluate how each of those sub-tasks improve with scale and unlock emergence when combined). Overall, understanding emergence is an important direction because it could potentially allow us predict what abilities future models may have, as well as provide new insights into how to train more-capable language models.

---

[referencia=2d76bc16fcc7825d score=0.908]
**Program execution.** Consider computational tasks involving multiple steps, such as adding large numbers or executing computer programs. Nye et al. (2021) show that finetuning language models to predict intermediate outputs (“scratchpad”) enables them to successfully execute such multi-step computations. As shown in Figure 3C, on 8-digit addition, using a scratchpad only helps for models of _∼_ 9 _·_ 10<sup>19</sup> training FLOPs (40M parameters) or larger. 

**Model calibration.** Finally, an important direction for deployment of language models studies is _calibration_ , which measures whether models can predict which questions they will be able to answer correctly. Kadavath et al. (2022) compared two ways of measuring calibration: a True/False technique, where models first propose answers and then evaluate the probability “P(True)” that their answers are correct, and more-standard methods of calibration, which use the probability of the correct answer compared with other answer options. As shown in Figure 3D, the superiority of the True/False technique only emerges when scaled to the largest model scale of _∼_ 3 _·_ 10<sup>23</sup> training FLOPs (52B parameters). 

5 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

Table 1: List of emergent abilities of large language models and the scale (both training FLOPs and number of model parameters) at which the abilities emerge.

---

[referencia=2d76bc16fcc7825d score=0.906]
**BIG-Bench.** Figure 2A–D depicts four emergent few-shot prompted tasks from BIG-Bench, a crowd-sourced suite of over 200 benchmarks for language model evaluation (BIG-Bench, 2022). Figure 2A shows an arithmetic benchmark that tests 3-digit addition and subtraction, as well as 2-digit multiplication. GPT-3 and LaMDA (Thoppilan et al., 2022) have close-to-zero performance for several orders of magnitude of training compute, before performance jumps to sharply above random at 2 _·_ 10<sup>22</sup> training FLOPs (13B parameters) for GPT-3, and 10<sup>23</sup> training FLOPs (68B parameters) for LaMDA. Similar emergent behavior also occurs at around the same model scale for other tasks, such as transliterating from the International Phonetic Alphabet (Figure 2B), recovering a word from its scrambled letters (Figure 2C), and Persian question-answering (Figure 2D). Even more emergent abilities from BIG-Bench are given in Appendix E. 

**TruthfulQA.** Figure 2E shows few-shot prompted performance on the TruthfulQA benchmark, which measures the ability to answer questions truthfully (Lin et al., 2021). This benchmark is adversarially curated against GPT-3 models, which do not perform above random, even when scaled to the largest model size. Small Gopher models also do not perform above random until scaled up to the largest model of 5 _·_ 10<sup>23</sup> training FLOPs (280B parameters), for which performance jumps to more than 20% above random (Rae et al., 2021). 

**Grounded conceptual mappings.** Figure 2F shows the task of grounded conceptual mappings, where language models must learn to map a conceptual domain, such as a cardinal direction, represented in a textual grid world (Patel & Pavlick, 2022). Again, performance only jumps to above random using the largest GPT-3 model.

---

[referencia=2d76bc16fcc7825d score=0.900]
## **4 Augmented Prompting Strategies** 

Although few-shot prompting is perhaps currently the most common way of interacting with large language models, recent work has proposed several other prompting and finetuning strategies to further augment the abilities of language models. If a technique shows no improvement or is harmful when compared to the baseline of not using the technique until applied to a model of a large-enough scale, we also consider the technique an emergent ability. 

4 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 



<!-- Start of picture text -->
(A) Math word (B) Instruction<br>problems following (C) 8-digit addition (D) Calibration<br>25<br>70 100<br>Instruction Scratchpad 10 0 T/F<br>20 tuning<br>Chain of 80<br>thought 60<br>15 60<br>50 No Letter<br>10 instruction 40 choices<br>tuning<br>40<br>5 20<br>No chain No 10 1<br>of thought scratchpad<br>0 30 0<br>10 21 10 22 10 23 10 24 10 21 10 22 10 23 10 24 10 19 10 20 10 21 10 22 10 23 10 24<br>Model scale (training FLOPs)<br>(%)<br>average (%) decreasing)<br>Accuracy task<br>NLU Accuracy (log-scale,<br>10<br>GSM8K<br>ECE<br>%<br><!-- End of picture text -->

Figure 3: Specialized prompting or finetuning methods can be emergent in that they do not have a positive effect until a certain model scale. A: Wei et al. (2022b). B: Wei et al. (2022a). C: Nye et al. (2021). D: Kadavath et al. (2022). An analogous figure with number of parameters on the _x_ -axis instead of training FLOPs is given in Figure 12. The model shown in A-C is LaMDA (Thoppilan et al., 2022), and the model shown in D is from Anthropic.

---

[referencia=2d76bc16fcc7825d score=0.889]
> 5These tasks are enumerated in Appendix F. 

7 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

models, Sanh et al. (2022) induced similar behavior in a 11B model with an encoder-decoder architecture, which typically has higher performance after finetuning than decoder-only architectures (Wang et al., 2022a). As another example, Ouyang et al. (2022) proposed a finetuning and reinforcement learning from human feedback approach for the InstructGPT models, which enabled a 1.3B model to outperform much larger models in human-rater evaluations on a broad set of use cases. 

There has also been work on improving the general few-shot prompting abilities of language models (Gao et al., 2021; Schick & Schütze, 2021, _inter alia_ ). Theoretical and interpretability research (Wei et al., 2021a; Saunshi et al., 2021) on why a language modeling objective facilitates certain downstream behavior could in turn have implications on how to enable emergence beyond simply scaling. For instance, certain features of pre-training data (e.g., long-range coherence, having many rare classes) have also been shown to correlate with emergent few-shot prompting and could potentially enable it in smaller models (Xie et al., 2022; Chan et al., 2022), and few-shot learning can require certain model architectures in some scenarios (Chan et al., 2022). Computational linguistics work has further shown how threshold frequencies of training data can activate emergent syntactic rule-learning when model parameters and training FLOPs are held constant (Wei et al., 2021b), which has even been shown to have striking “aha” moments similar to those in the psycholinguistics literature (Abend et al., 2017; Zhang et al., 2021). As we continue to train language models, lowering the scale threshold for emergent abilities will become more important for making research on such abilities to available to the community more broadly (Bommasani et al., 2021; Ganguli et al., 2022; Liang et al., 2022).

---

[referencia=2d76bc16fcc7825d score=0.861]
> 7https://copilot.github.com/ 

> 8https://beta.openai.com/docs/introduction 

10 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

underestimated the amount of training data needed to train a compute-optimal model, underscoring the importance of training data. Collecting large datasets so that models can be trained for longer could allow a greater range of emergent abilities under a fixed model size constraint. 

**Better techniques for and understanding of prompting.** Although few-shot prompting (Brown et al., 2020) is simple and effective, general improvements to prompting may further expand the abilities of language models. For instance, simple modifications such as calibrating output probabilities (Zhao et al., 2021; Holtzman et al., 2021) or using a noisy channel (Min et al., 2022a) have improved performance on a range of tasks. Augmenting few-shot exemplars with intermediate steps (Reynolds & McDonell, 2021; Nye et al., 2021; Wei et al., 2022b) has also enabled models to perform multi-step reasoning tasks not possible in the standard prompting formulation from Brown et al. (2020). Moreover, better exploration of what makes prompting successful (Wei et al., 2021a; Xie et al., 2022; Min et al., 2022b; Olsson et al., 2022) could lead to insights on how to elicit emergent abilities at a smaller model scale. Sufficient understanding of why models work generally lags the development and popularization of techniques such as few-shot prompting, and it is also likely that the best practices for prompting will change as more-powerful models are developed over time.

---

[referencia=2d76bc16fcc7825d score=0.833]
### **5.6 Directions for future work** 

Future work on emergent abilities could involve train more-capable language models, as well as methods for better enabling language models to perform tasks. Some potential directions include but are not limited to the following. 

**Further model scaling.** Further scaling up models has so far appeared to increase the capabilities of language models, and is a straightforward direction for future work. However, simply scaling up language models is computationally expensive and requires solving substantial hardware challenges, and so other approaches will likely play a key role in the future of the emergent abilities of large language models. 

**Improved model architectures and training.** Improving model architecture and training procedures may facilitate high-quality models with emergent abilities while mitigating computational cost. One direction is using sparse mixture-of-experts architectures (Lepikhin et al., 2021; Fedus et al., 2021; Artetxe et al., 2021; Zoph et al., 2022), which scale up the number of parameters in a model while maintaining constant computational costs for an input. Other directions for better computational efficiency could involve variable amounts of compute for different inputs (Graves, 2016; Dehghani et al., 2018), using more localized learning strategies than backpropagation through all weights in a neural network (Jaderberg et al., 2017), and augmenting models with external memory (Guu et al., 2020; Borgeaud et al., 2021; Wu et al., 2022b, _inter alia_ ). These nascent directions have already shown promise in many settings but have not yet seen widespread adoption, which will likely require further work. 

**Data scaling.** Training long enough on a large-enough dataset has been shown to be key for the ability of language models to acquire syntactic, semantic, and other world knowledge (Zhang et al., 2021; Wei et al., 2021b; Razeghi et al., 2022). Recently, Hoffmann et al. (2022) argued that prior work (Kaplan et al., 2020) 

> 7https://copilot.github.com/ 

> 8https://beta.openai.com/docs/introduction 

10 

Published in Transactions on Machine Learning Research <u>(08/2022)</u>

---

[referencia=2d76bc16fcc7825d score=0.830]
### **5.5 Sociological changes** 

Finally, the emergent abilities discussed here focus on model behavior and are just one of several types of emergence in NLP (Manning et al., 2020; Teehan et al., 2022). Another notable type of qualitative change is sociological, in which increasing scale has shifted how the community views and uses language models. For instance, NLP has historically focused on task-specific models (Jurafsky & Martin, 2009). Recently, scaling has led to an explosion in research on and development of models that are “general purpose” in that they are single models that aim to perform a range of tasks not explicitly encoded in the training data (e.g., GPT-3, Chinchilla, and PaLM) (Manning, 2022). 

One key set of results in the emergent sociological shift towards general-purpose models is when scaling enables a few-shot prompted general-purpose model to outperform prior state of the art held by finetuned task-specific models. As a few examples, GPT-3 175B achieved new state of the art on the TriviaQA and PiQA question-answering benchmarks (Brown et al., 2020); PaLM 540B achieved new state of the art on three arithmetic reasoning benchmarks (Chowdhery et al., 2022); and the multimodal Flamingo 80B model achieved new state of the art on six visual question answering benchmarks (Alayrac et al., 2022). In all of these cases, state-of-the-art performance was achieved by few-shot prompting a language model of unprecendented scale (scaling curves for these examples are shown in Appendix Figure 13). These abilities are not necessarily emergent since they have smooth, predictable scaling curves—however, they do underscore an emergent sociological shift towards general-purpose models in the NLP community.

---

[referencia=2d76bc16fcc7825d score=0.799]
emergent until using PaLM models. The non-emergent tasks in this plot include either “smoothly increasing” 

tasks (performance predictably increased with model size) or “flat” tasks (all models achieved approximately random performance). The remaining 40 BIG-Bench tasks not included in this chart did not fit into any of the above categories (e.g., too noisy due to very few eval examples, performance not correlated with model scale, etc.). Since the number of tasks per keyword varied substantially among keywords, and most keywords had less than twenty tasks, the “most emergent” keywords differed depending on whether we compare number of emergent tasks or percentage of emergent tasks per keyword. Tracking the absolute number of emergent tasks per keyword is problematic since it effectively just captures the most common keywords used across BigBench. We therefore tracked which keywords had the highest percent of emergent tasks, which were analogical reasoning, word sense disambiguation, truthfulness, social reasoning, and emotional understanding. While one might expect a priori that reasoning-related tasks would more likely to be emergent, only two of 

the top five tasks were reasoning and other keyword tags like logical reasoning and causal reasoning did not 

22 

Published in Transactions on Machine Learning Research <u>(08/2022)</u> 

have a particularly high fraction of emergent tasks. Moreover, arithmetic and mathematics had relatively low percentage of emergent tasks, which was unexpected since some of the earliest examples of emergence were on arithmetic (Brown et al., 2020). Overall, there are no clear trends for which types of tasks are most emergent. 

Finally, examining which keywords have the most tasks with flat scaling curves can also align with prior intuitions. For instance, visual reasoning has the largest fraction of tasks with flat scaling curves (8/13), since language models are not designed for visual reasoning. Other categories with a large fraction of flat scaling curve tasks are non-language, repeated interaction, context length, computer code, and multi-step—all targeting weaknesses of large language models. These flat categories could be directions for future work in emergence in large language models. 



<!-- Start of picture text -->

---

[referencia=2d76bc16fcc7825d score=0.754]
We find that all six BIG-Bench tasks fall under Outcome 2, and detail this analysis below. Overall, the conclusion from this analysis is that small models do improve in some ways that downstream metrics that EM/BLEU/Acc do not capture. However, these tasks are still considered emergent, and this analysis does not provide any straightforward indicators of how to predict such emergent behaviors. 

### **A.1.1 Generative tasks** 

Figure 5 shows the cross-entropy loss on the three generative BIG-Bench tasks (modified arithmetic, IPA transliterate, and word unscramble) alongside the downstream evaluation metrics used in Figure 2. For all three tasks, notice that while the error rate is nearly 100% for small models ( _≤_ 10<sup>22</sup> FLOPs / _≤_ 27B params), the cross-entropy loss does actually improve for these model sizes. At the point of emergence as measured by error rate, we also see an “elbow” in performance improvement for cross-entropy loss.

---

[referencia=2d76bc16fcc7825d score=0.711]
<!-- Start of picture text -->
50<br>45<br>40<br>35<br>30<br>Emergent with LaMDA/GPT<br>25 Emergent with PaLM<br>Smoothly increasing<br>20<br>Flat (no model better than random)<br>15<br>10<br>5<br>0<br>Keyword Tag<br>logical-reasoningreading-comprehensioncommon-sensecontext-free-question-answeringanalogical-reasoningmathematicshuman-like-behaviorcontextual-question-answeringsocial-reasoningnumerical-responsearithmeticnon-languagenon-Englishvisual-reasoningout-of-distributionimplicit-reasoningcreativitycausal-reasoningemotional-understandingparaphrasecomputer-codeword-sense-disambiguationmultilinguallow-resource-languagemulti-stepcontext-lengthnarrative-understandingtranslationtheory-of-mindsummarizationdomain-specificrepeated-interactiontruthfulness<br>tasks<br>of<br>Number<br><!-- End of picture text -->

Figure 8: Proportion of emergent tasks for keywords in BIG-Bench (each task can be associated with multiple keywords). We only included keywords with at least five tasks. Smoothly increasing: performance improved predictably as model scale increased. Emergent with LaMDA/GPT: performance was near-random until used with LaMDA 137B or GPT-3 175B. Emergent with PaLM: performance was near-random for all previous models, until using a PaLM model (8B, 62B, or 540B). Flat: no model performs better than random. 

23 

Published in Transactions on Machine Learning Research <u>(08/2022)</u>