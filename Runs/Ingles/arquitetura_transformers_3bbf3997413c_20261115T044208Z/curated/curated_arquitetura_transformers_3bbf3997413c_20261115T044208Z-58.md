[referencia=1098fc60be7ca2b0 score=0.110]
### **5.4 Open questions** 

This work is a first step towards using alignment techniques to fine-tune language models to follow a wide range of instructions. There are many open questions to explore to further align language model behavior with what people actually want them to do. 

Many methods could be tried to further decrease the models’ propensity to generate toxic, biased, or otherwise harmful outputs. For example, one could use an adversarial set-up where labelers find the worst-case behaviors of the model, which are then labeled and added to the dataset (Dinan et al., 2019b). One could also combine our method with ways of filtering the pretraining data (Ngo et al., 2021), either for training the initial pretrained models, or for the data we use for our pretraining mix approach. Similarly, one could combine our approach with methods that improve models’ truthfulness, such as WebGPT (Nakano et al., 2021). 

In this work, if the user requests a potentially harmful or dishonest response, we allow our model to generate these outputs. Training our model to be harmless despite user instructions is important, but is also difficult because whether an output is harmful depends on the context in which it’s deployed; for example, it may be beneficial to use language models to generate toxic outputs as part of a data augmentation pipeline. Our techniques can also be applied to making models refuse certain user instructions, and we plan to explore this in subsequent iterations of this research. 

Getting models to do what we want is directly related to the steerability and controllability literature (Dathathri et al., 2019; Krause et al., 2020). A promising future path is combining RLHF with other methods of steerability, for example using control codes (Keskar et al., 2019), or modifying the sampling procedure at inference time using a smaller model (Dathathri et al., 2019). 

While we mainly focus on RLHF, there are many other algorithms that could be used to train policies on our demonstration and comparison data to get even better results. For example, one could explore expert iteration (Anthony et al., 2017; Silver et al., 2017), or simpler behavior cloning methods that use a subset of the comparison data. One could also try constrained optimization approaches (Achiam et al., 2017) that maximize the score from a reward model conditioned on generating a small number of harmful behaviors. 

19

---

[referencia=1098fc60be7ca2b0 score=0.055]
### **3.5 Models** 

We start with the GPT-3 pretrained language models from Brown et al. (2020). These models are trained on a broad distribution of Internet data and are adaptable to a wide range of downstream tasks, but have poorly characterized behavior. Starting from these models, we then train models with three different techniques: 

**Supervised fine-tuning (SFT).** We fine-tune GPT-3 on our labeler demonstrations using supervised learning. We trained for 16 epochs, using a cosine learning rate decay, and residual dropout of 0.2. We do our final SFT model selection based on the RM score on the validation set. Similarly to Wu et al. (2021), we find that our SFT models overfit on validation loss after 1 epoch; however, we find that training for more epochs helps both the RM score and human preference ratings, despite this overfitting. 

**Reward modeling (RM).** Starting from the SFT model with the final unembedding layer removed, we trained a model to take in a prompt and response, and output a scalar reward. In this paper we only use 6B RMs, as this saves a lot of compute, and we found that 175B RM training could be unstable and thus was less suitable to be used as the value function during RL (see Appendix C for more details). 

In Stiennon et al. (2020), the RM is trained on a dataset of comparisons between two model outputs on the same input. They use a cross-entropy loss, with the comparisons as labels—the difference in rewards represents the log odds that one response will be preferred to the other by a human labeler.

---

[referencia=1098fc60be7ca2b0 score=0.052]
We further investigate whether increasing the coefficient of KL reward ( _β_ in Equation 2) is sufficient to fix the regressions on public NLP datasets, using the 1.3B model. We set the pretraining loss coefficient to 0 and sweep a range of KL reward coefficient’s uniformly in log linear space. The results are shown in Figure 34. The pretrained GPT model is used as the KL reward model, in these experiments. We find that even by increasing the KL reward coefficient to 2.0, which is 100 times of the default value, the regressions still cannot be fixed. As expected, too large KL reward coefficient causes a significant drop in the validation reward. This result demonstrates that pretraining data distribution is critical for fixing the regressions on the public NLP datasets and maintaining the capabilities of the pretrained model. 

53 



<!-- Start of picture text -->
Instruct distribution GPT distribution<br>6<br>5<br>4<br>Model<br>3 PPO-ptx<br>2 PPO<br>6 SFT<br>GPT<br>5 (prompted)<br>GPT<br>4<br>3<br>2<br>1.3B 6B 175B 1.3B 6B 175B<br>Model size<br>Training workers<br>Likert score<br>Heldout workers<br><!-- End of picture text -->

Figure 31: Likert scores for each of our models 



<!-- Start of picture text -->
Biased prompt No prompt Respectful prompt<br>0.4<br>0.3<br>Model<br>0.2 PPO-ptx<br>PPO<br>SFT<br>0.8<br>GPT<br>0.7<br>0.6<br>0.5<br>0.4<br>1.3B 6B 175B1.3B 6B 175B1.3B 6B 175B<br>Model size<br>CrowS-Pairs<br>Normed entropy<br>Winogender<br><!-- End of picture text -->

Figure 32: Bias results on Winogender and CrowS-Pairs. 

54 



<!-- Start of picture text -->

---

[referencia=1098fc60be7ca2b0 score=0.044]
## **3 Methods and experimental details** 

### **3.1 High-level methodology** 

Our methodology follows that of Ziegler et al. (2019) and Stiennon et al. (2020), who applied it in the stylistic continuation and summarization domains. We start with a pretrained language model (Radford et al., 2019; Brown et al., 2020; Fedus et al., 2021; Rae et al., 2021; Thoppilan et al., 2022), a distribution of prompts on which we want our model to produce aligned outputs, and a team of trained human labelers (see Sections 3.4 for details). We then apply the following three steps (Figure 2). 

**Step 1: Collect demonstration data, and train a supervised policy.** Our labelers provide demonstrations of the desired behavior on the input prompt distribution (see Section 3.2 for details on this distribution). We then fine-tune a pretrained GPT-3 model on this data using supervised learning. 

**Step 2: Collect comparison data, and train a reward model.** We collect a dataset of comparisons between model outputs, where labelers indicate which output they prefer for a given input. We then train a reward model to predict the human-preferred output. 

**Step 3: Optimize a policy against the reward model using PPO.** We use the output of the RM as a scalar reward. We fine-tune the supervised policy to optimize this reward using the PPO algorithm (Schulman et al., 2017). 

Steps 2 and 3 can be iterated continuously; more comparison data is collected on the current best policy, which is used to train a new RM and then a new policy. In practice, most of our comparison data comes from our supervised policies, with some coming from our PPO policies.

---

[referencia=1098fc60be7ca2b0 score=0.041]
Fourth, OpenAI’s customers are not representative of all potential or current users of language models—let alone of all individuals and groups impacted by language model use. For most of the duration of this project, users of the OpenAI API were selected off of a waitlist. The initial seeds for this waitlist were OpenAI employees, biasing the ultimate group toward our own networks. 

Stepping back, there are many difficulties in designing an alignment process that is fair, transparent, and has suitable accountability mechanisms in place. The goal of this paper is to demonstrate that this alignment technique can align to an specific human reference group for a specific application. We are not claiming that researchers, the labelers we hired, or our API customers are the right source of preferences. There are many stakeholders to consider—the organization training the model, the customers using the model to develop products, the end users of these products, and the broader population who may be directly or indirectly affected. It is not only a matter of making the alignment process more participatory; it is impossible that one can train a system that is aligned to everyone’s preferences at once, or where everyone would endorse the tradeoffs. 

One path forward could be to train models that can be conditioned on the preferences of certain groups, or that can be easily fine-tuned or prompted to represent different groups. Different models can then be deployed and used by groups who endorse different values. However, these models might still end up affecting broader society and there are a lot of difficult decisions to be made relating to whose preferences to condition on, and how to ensure that all groups can be represented and can opt out of processes that may be harmful. 

> 10Note that while fine-tuning models using human data is common practice when deploying ML systems, the purpose of these efforts is to obtain a model that performs well on a company’s specific use case, rather than advancing the alignment of general-purpose ML models. 

18

---

[referencia=1098fc60be7ca2b0 score=0.029]
### **E.1 Performance on public NLP datasets** 

We run automatic evaluation tasks on our models that collectively measure bias, toxicity, truthfulness, and a variety of natural language capabilities. The results of these evaluations are in Table 14. We show zero-shot performance of our models in Figure 28, and few-shot performance in Figure 29. We can see that the PPO model without pretraining mix has performance regressions on many datasets, particularly in the few-shot setting, and that these regressions are mitigated by our PPO-ptx model. 

51 



<!-- Start of picture text -->
DROP (F1) Hellaswag (acc)<br>35 0.8<br>30 0.7<br>25 0.6<br>0.5<br>QuAC (F1) RTE v2 (acc)<br>50<br>0.8<br>45<br>0.7<br>40<br>0.6<br>35<br>0.5<br>30<br>SST (acc) Squad V2 (F1)<br>0.95 70<br>65<br>0.90<br>60<br>0.85<br>55<br>0.80 50<br>45<br>Translate Fr => En (BLEU) Winograd (acc)<br>40<br>0.8<br>35<br>0.7<br>30<br>0.6<br>25<br>0.5<br>1.3B 6B 175B 1.3B 6B 175B<br>PPO-ptx PPO SFT GPT<br><!-- End of picture text -->

Figure 29: Few-shot performance of our models on various public NLP datasets (compare to zero-shot performance shown in Figure 28

---

[referencia=1098fc60be7ca2b0 score=0.027]
- Comparisons are also not necessarily the most efficient way of providing an alignment signal. For example, we could have labelers edit model responses to make them better, or generate critiques of model responses in natural language. There is also a vast space of options for designing interfaces for labelers to provide feedback to language models; this is an interesting human-computer interaction problem. 

- Our proposal for mitigating the alignment tax, by incorporating pretraining data into RLHF fine- 

- tuning, does not completely mitigate performance regressions, and may make certain undesirable behaviors more likely for some tasks (if these behaviors are present in the pretraining data). This is an interesting area for further research. Another modification that would likely improve our method 

- is to filter the pretraining mix data for toxic content (Ngo et al., 2021), or augment this data with synthetic instructions. As discussed in detail in Gabriel (2020), there are subtle differences between aligning to instructions, 

- intentions, revealed preferences, ideal preferences, interests, and values. Gabriel (2020) advocate for 

- a principle-based approach to alignment: in other words, for identifying “fair principles for alignment that receive reflective endorsement despite widespread variation in people’s moral beliefs.” In our paper we align to the inferred user intention for simplicity, but more research is required in this area. 

- Indeed, one of the biggest open questions is how to design an alignment process that is transparent, 

- that meaningfully represents the people impacted by the technology, and that synthesizes peoples’ 

- values in a way that achieves broad consensus amongst many groups. We discuss some related considerations in Section 5.2. 

- **5.5 Broader impacts** 

- This work is motivated by our aim to increase the positive impact of large language models by training them to do what a given set of humans want them to do. By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. Our results indicate that our techniques hold promise for making language models more helpful, 

- truthful, and harmless. In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. We expect that as model scaling continues, greater care has to be taken to ensure that they are aligned with human intentions (Bostrom, 2014).

---

[referencia=1098fc60be7ca2b0 score=0.027]
> **Training language models to follow instructions.** Our work is also related to research on crosstask generalization in language models, where LMs are fine-tuned on a broad range of public NLP datasets (usually prefixed with an appropriate instruction) and evaluated on a different set of NLP tasks. There has been a range of work in this domain (Yi et al., 2019; Mishra et al., 2021; Wei et al., 2021; Khashabi et al., 2020; Sanh et al., 2021; Aribandi et al., 2021), which differ in training and evaluation data, formatting of instructions, size of pretrained models, and other experimental details. A consistent finding across studies is that fine-tuning LMs on a range of NLP tasks, with instructions, improves their downstream performance on held-out tasks, both in the zero-shot and few-shot settings. 

Our work is also related to research on cross- 

There is also a related line of work on instruction following for navigation, where models are trained to follow natural language instructions to navigate in a simulated environment (Bahdanau et al., 2018; Abramson et al., 2020; Zhao et al., 2021). 

**Evaluating the harms of language models.** A goal of modifying the behavior of language models is to mitigate the harms of these models when they’re deployed in the real world. These risks have been extensively documented (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021). Language models can produce biased outputs (Dhamala et al., 2021; Liang et al., 2021; Manela et al., 2021; Caliskan et al., 2017; Kirk et al., 2021), leak private data (Carlini et al., 2021), generate misinformation (Solaiman et al., 2019; Buchanan et al., 2021), and be used maliciously; for a thorough review we direct the reader to Weidinger et al. (2021).

---

[referencia=1098fc60be7ca2b0 score=0.027]
Deploying language models in specific domains gives rise to new risks and challenges, for example in dialog systems (Henderson et al., 2018; Xu et al., 2020; Dinan et al., 2019b). There is a nascent but growing field that aims to build benchmarks to concretely evaluate these harms, particularly around toxicity (Gehman et al., 2020), stereotypes (Nadeem et al., 2020), and social bias (Dhamala et al., 2021; Nangia et al., 2020; Rudinger et al., 2018). Making significant progress on these problems is hard since well-intentioned interventions on LM behavior can have side-effects (Welbl et al., 2021; Blodgett et al., 2020); for instance, efforts to reduce the toxicity of LMs can reduce their ability to model text from under-represented groups, due to prejudicial correlations in the training data (Xu et al., 2021). 

**Modifying the behavior of language models to mitigate harms.** There are many ways to change the generation behavior of language models. Solaiman and Dennison (2021) fine-tune LMs on a small, value-targeted dataset, which improves the models’ ability to adhere to these values on a question answering task. Ngo et al. (2021) filter the pretraining dataset by removing documents on which a language model has a high conditional likelihood of generating a set of researcher-written trigger phrases. When trained on this filtered dataset, their LMs generate less harmful text, at the cost of a slight decrease in language modeling performance. Xu et al. (2020) use a variety of approaches to improve the safety of chatbots, including data filtering, blocking certain words or n-grams during generation, safety-specific control tokens (Keskar et al., 2019; Dinan et al., 2019a), and human-in-theloop data collection (Dinan et al., 2019b). Other approaches for mitigating the generated bias by LMs use word embedding regularization (Liu et al., 2019; Huang et al., 2019), data augmentation (Liu et al., 2019; Dinan et al., 2019a; Sheng et al., 2019), null space projection to make the distribution

---

[referencia=1098fc60be7ca2b0 score=0.024]
From this work, we can draw lessons for alignment research more generally: 

1. **The cost of increasing model alignment is modest relative to pretraining.** The cost of collecting our data and the compute for training runs, including experimental runs is a fraction of what was spent to train GPT-3: training our 175B SFT model requires 4.9 petaflops/s-days and training our 175B PPO-ptx model requires 60 petaflops/s-days, compared to 3,640 petaflops/s-days for GPT-3 (Brown et al., 2020). At the same time, our results show that RLHF is very effective at making language models more helpful to users, more so than a 100x model size increase. This suggests that right now increasing investments in alignment of existing language models is more cost-effective than training larger models—at least for our customers’ natural language task distribution. 

2. **We’ve seen some evidence that InstructGPT generalizes ‘following instructions’ to settings that we don’t supervise it in,** for example on non-English language tasks and code-related tasks. This is an important property because it’s prohibitively expensive to have humans supervise models on every task they perform. More research is needed to study how well this generalization scales with increased capabilities; see Christiano et al. (2021) for recent research in this direction. 

3. **We were able to mitigate most of the performance degradations introduced by our fine-tuning.** If this was not the case, these performance degradations would constitute an alignment tax—an additional cost for aligning the model. Any technique with a high tax might not see adoption. To avoid incentives for future highly capable AI systems to remain unaligned with human intent, there is a need for alignment techniques that have low alignment tax. To this end, our results are good news for RLHF as a low-tax alignment technique. 

4. **We’ve validated alignment techniques from research in the real world.** Alignment research has historically been rather abstract, focusing on either theoretical results (Soares et al., 2015), small synthetic domains (Christiano et al., 2018; Leike et al., 2017), or training ML models on public NLP datasets (Ziegler et al., 2019; Stiennon et al., 2020). Our work provides grounding for alignment research in AI systems that are being used in production in

---

[referencia=1098fc60be7ca2b0 score=0.021]
- Nadeem, M., Bethke, A., and Reddy, S. (2020). Stereoset: Measuring stereotypical bias in pretrained language models. _arXiv preprint arXiv:2004.09456_ . 

- Nahian, M. S. A., Frazier, S., Harrison, B., and Riedl, M. (2021). Training value-aligned reinforcement learning agents using a normative prior. _arXiv preprint arXiv:2104.09469_ . 

- Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hesse, C., Jain, S., Kosaraju, V., Saunders, W., et al. (2021). Webgpt: Browser-assisted question-answering with human feedback. _arXiv preprint arXiv:2112.09332_ . 

- Nallapati, R., Zhou, B., Gulcehre, C., Xiang, B., et al. (2016). Abstractive text summarization using sequence-to-sequence rnns and beyond. _arXiv preprint arXiv:1602.06023_ . 

- Nangia, N., Vania, C., Bhalerao, R., and Bowman, S. R. (2020). CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models. In _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing_ , Online. Association for Computational Linguistics. 

- Ngo, H., Raterink, C., Araújo, J. G., Zhang, I., Chen, C., Morisot, A., and Frosst, N. (2021). Mitigating harm in language models with conditional-likelihood filtration. _arXiv preprint arXiv:2108.07790_ . 

- Perez, E., Karamcheti, S., Fergus, R., Weston, J., Kiela, D., and Cho, K. (2019). Finding generalizable evidence by learning to convince q&a models. _arXiv preprint arXiv:1909.05863_ .

---

[referencia=1098fc60be7ca2b0 score=0.017]
- Abramson, J., Ahuja, A., Barr, I., Brussee, A., Carnevale, F., Cassin, M., Chhaparia, R., Clark, S., Damoc, B., Dudzik, A., et al. (2020). Imitating interactive intelligence. _arXiv preprint arXiv:2012.05672_ . 

- Achiam, J., Held, D., Tamar, A., and Abbeel, P. (2017). Constrained policy optimization. In _International Conference on Machine Learning_ , pages 22–31. PMLR. 

- Anthony, T., Tian, Z., and Barber, D. (2017). Thinking fast and slow with deep learning and tree search. _arXiv preprint arXiv:1705.08439_ . 

- Aribandi, V., Tay, Y., Schuster, T., Rao, J., Zheng, H. S., Mehta, S. V., Zhuang, H., Tran, V. Q., Bahri, D., Ni, J., et al. (2021). Ext5: Towards extreme multi-task scaling for transfer learning. _arXiv preprint arXiv:2111.10952_ . 

- Askell, A., Bai, Y., Chen, A., Drain, D., Ganguli, D., Henighan, T., Jones, A., Joseph, N., Mann, B., DasSarma, N., et al. (2021). A general language assistant as a laboratory for alignment. _arXiv preprint arXiv:2112.00861_ . 

- Bahdanau, D., Brakel, P., Xu, K., Goyal, A., Lowe, R., Pineau, J., Courville, A., and Bengio, Y. (2016). An actor-critic algorithm for sequence prediction. _arXiv preprint arXiv:1607.07086_ . 

- Bahdanau, D., Hill, F., Leike, J., Hughes, E., Hosseini, A., Kohli, P., and Grefenstette, E. (2018). Learning to understand goal specifications by modelling reward. _arXiv preprint arXiv:1806.01946_ .

---

[referencia=1098fc60be7ca2b0 score=0.017]
### **5.2 Who are we aligning to?** 

When aligning language models with human intentions, their end behavior is a function of the underlying model (and its training data), the fine-tuning data, and the alignment method used. In this section, we describe a number of factors that influence the fine-tuning data specifically, to ultimately determine what and who we’re aligning to. We then consider areas for improvement before a larger discussion of the limitations of our work in Section 5.3. 

The literature often frames alignment using such terms as “human preferences” or “human values.” In this work, we have aligned to a set of labelers’ preferences that were influenced, among others things, by the instructions they were given, the context in which they received them (as a paid job), and who they received them from. Some crucial caveats apply: 

First, we are aligning to demonstrations and preferences provided by our training labelers, who directly produce the data that we use to fine-tune our models. We describe our labeler hiring process and demographics in Appendix B; in general, they are mostly English-speaking people living in the United States or Southeast Asia hired via Upwork or Scale AI. They disagree with each other on many examples; we found the inter-labeler agreement to be about 73%. 

Second, we are aligning to our preferences, as the researchers designing this study (and thus by proxy to our broader research organization, OpenAI): we write the labeling instructions that labelers use as a guide when writing demonstrations and choosing their preferred output, and we answer their questions about edge cases in a shared chat room. More study is needed on the exact effect of different instruction sets and interface designs on the data collected from labelers and its ultimate effect on model behavior. 

Third, our training data is determined by prompts sent by OpenAI customers to models on the OpenAI API Playground, and thus we are implicitly aligning to what customers think is valuable and, in some cases, what their end-users think is valuable to currently use the API for. Customers and their end users may disagree or customers may not be optimizing for end users’ well-being; for example, a customer may want a model that maximizes the amount of time a user spends on their platform, which is not necessarily what end-users want. In practice, our labelers don’t have visibility into the contexts in which a given prompt or completion will be seen.

---

[referencia=1098fc60be7ca2b0 score=0.016]
- Lawrence, C. and Riezler, S. (2018). Improving a neural semantic parser by counterfactual learning from human bandit feedback. _arXiv preprint arXiv:1805.01252_ . 

- Leike, J., Krueger, D., Everitt, T., Martic, M., Maini, V., and Legg, S. (2018). Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_ . 

- Leike, J., Martic, M., Krakovna, V., Ortega, P. A., Everitt, T., Lefrancq, A., Orseau, L., and Legg, S. (2017). AI safety gridworlds. _arXiv preprint arXiv:1711.09883_ . 

- Liang, P. P., Wu, C., Morency, L.-P., and Salakhutdinov, R. (2021). Towards understanding and mitigating social biases in language models. In _International Conference on Machine Learning_ , pages 6565–6576. PMLR. 

- Lin, S., Hilton, J., and Evans, O. (2021). Truthfulqa: Measuring how models mimic human falsehoods. _arXiv preprint arXiv:2109.07958_ . 

- Liu, H., Dacon, J., Fan, W., Liu, H., Liu, Z., and Tang, J. (2019). Does gender matter? towards fairness in dialogue systems. _arXiv preprint arXiv:1910.10486_ . 

- Madaan, A., Tandon, N., Clark, P., and Yang, Y. (2022). Memory-assisted prompt editing to improve gpt-3 after deployment. _arXiv preprint arXiv:2201.06009_ . 

- Manela, D. d. V., Errington, D., Fisher, T., van Breugel, B., and Minervini, P. (2021). Stereotype and skew: Quantifying gender bias in pre-trained and fine-tuned language models. _arXiv preprint arXiv:2101.09688_ .

---

[referencia=1098fc60be7ca2b0 score=0.016]
**InstructGPT still makes simple mistakes.** In interacting with our 175B PPO-ptx model, we have noticed it can still make simple mistakes, despite its strong performance on many different language tasks. To give a few examples: (1) when given an instruction with a false premise, the model sometimes incorrectly assumes the premise is true, (2) the model can overly hedge; when given a simple question, it can sometimes say that there is no one answer to the question and give multiple possible answers, even when there is one fairly clear answer from the context, and (3) the model’s performance degrades when instructions contain multiple explicit constraints (e.g. “list 10 movies made in the 1930’s set in France”) or when constraints can be challenging for language models (e.g. writing a summary in a specified number of sentences). 

9We generally instruct our labelers to skip evaluations where they are missing the required expertise, though sometimes labelers use a translation service to evaluate simple instructions in languages that they do not speak. 

16 

We show some examples of these behaviors in Figure 9. We suspect that behavior (2) emerges partly because we instruct labelers to reward epistemic humility; thus, they may tend to reward outputs that hedge, and this gets picked up by our reward model. We suspect that behavior (1) occurs because there are few prompts in the training set that assume false premises, and our models don’t generalize well to these examples. We believe both these behaviors could be dramatically reduced with adversarial data collection (Dinan et al., 2019b).

---

[referencia=1098fc60be7ca2b0 score=0.014]
### **E.3 Metadata results as a function of model size** 

In Figure 30, we show metadata results as a function of model size. 

52 

Attempts correct instruction Appropriate for customer assistant 0.95 0.9 

0.90 

0.8 

0.85 

0.7 

Model 0.80 0.6 PPO-ptx 1.3B 6B 175B 1.3B 6B 175B PPO SFT Follows explicit constraints Hallucinations GPT 0.6 (prompted) 0.6 GPT 0.4 0.4 

0.2 0.2 

0 1.3B 6B 175B 1.3B 6B 175B Model size 

Figure 30: Metadata ratings as a function of model type and model size **E.4 Likert scores** In Figure 31, we show Likert scores for each of our models on our prompt distribution. The results largely track with our preference results in Section 4.1. **E.5 Measuring bias** 

Our results on the Winogender and CrowS-Pairs dataset are shown in Figure 32. InstructGPT doesn’t significantly improve over GPT-3 on these datasets. 

**E.6 Fixing regressions on public NLP datasets** We sweep a range of pretraining loss coefficient ( _γ_ in Equation 2) to see its effects on the performance of public NLP datasets and validation reward. The results are shown in Figure 33. By setting pretraining loss coefficient to greater or equal 20, the regression on these tasks can be recovered, on the 1.3B model. We also noticed that the sensitivity to pretraining loss coefficient varies across tasks. Although increasing the pretraining loss coefficient causes the validation reward to drop, a single value of 27.8 seems to work well across model sizes, from 1.3B to 175B parameter count. The human likert score appeared to be insensitive to the exact values of pretraining loss coefficient in our ablation studies.

---

[referencia=1098fc60be7ca2b0 score=0.012]
- Bojar, O., Chatterjee, R., Federmann, C., Haddow, B., Huck, M., Hokamp, C., Koehn, P., Logacheva, V., Monz, C., Negri, M., Post, M., Scarton, C., Specia, L., and Turchi, M. (2015). Findings of the 2015 workshop on statistical machine translation. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 1–46, Lisbon, Portugal. Association for Computational Linguistics. 

- Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. (2021). On the opportunities and risks of foundation models. _arXiv preprint arXiv:2108.07258_ . 

- Bostrom, N. (2014). _Superintelligence_ . Dunod. 

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ . 

- Buchanan, B., Lohn, A., Musser, M., and Sedova, K. (2021). Truth, lies, and automation. Technical report, Center for the Study of Emerging Technology. 

- Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. _Science_ , 356(6334):183–186. 

- Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., et al. (2021). Extracting training data from large language models. In _30th USENIX Security Symposium (USENIX Security 21)_ , pages 2633–2650.

---

[referencia=1098fc60be7ca2b0 score=0.011]
11 



<!-- Start of picture text -->
Attempts correct instruction Follows explicit constraints Hallucinations Uses language appropriatefor customer assistant<br>0.5<br>0.75 0.4 0.75<br>0.4<br>0.3<br>0.50 0.50<br>0.2 0.2<br>0.25 0.25<br>0.1<br>0 0 0 0<br>GPT GPT SFT PPO PPO-ptx GPT GPT SFT PPO PPO-ptx GPT GPT SFT PPO PPO-ptx GPT GPT SFT PPO PPO-ptx<br>(prompted) (prompted) (prompted) (prompted)<br>Prevalence<br><!-- End of picture text -->

Figure 4: Metadata results on the API distribution. Note that, due to dataset sizes, these results are collapsed across model sizes. See Appendix E.2 for analysis that includes model size. Compared to GPT-3, the PPO models are more appropriate in the context of a customer assistant, are better at following explicit constraints in the instruction and attempting the correct instruction, and less likely to ‘hallucinate’ (meaning, making up information on closed domain tasks like summarization). 



<!-- Start of picture text -->
6<br>4<br>2<br>GPT GPT SFT PPO-ptx FLAN T0<br>(prompted)<br>Model<br>Likert score<br><!-- End of picture text -->

Figure 5: Comparing our models with FLAN and T0 in terms of Likert scores on a 1-7 scale, on the InstructGPT prompt distribution. FLAN and T0 perform better than default GPT-3, and comparably with a few-shot GPT-3 model placed into ‘instruction-following’ mode. 

categories occur too infrequently in our API to obtain statistically significant differences between our models. 

**Our models generalize to the preferences of "held-out" labelers that did not produce any training data.** Held-out labelers have similar ranking preferences as workers who we used to produce training data (see Figure 3). In particular, according to held-out workers, all of our InstructGPT models still greatly outperform the GPT-3 baselines. Thus, our InstructGPT models aren’t simply overfitting to the preferences of our training labelers.

---

[referencia=1098fc60be7ca2b0 score=0.011]
Figure 32: Bias results on Winogender and CrowS-Pairs. 

54 



<!-- Start of picture text -->
F1 Validation reward<br>60 0.6<br>(GPT)<br>0.8<br>50<br>Dataset<br>1<br>40 a DROP<br>1.2 a SQuAD v2<br>30<br>1.4<br>(GPT)<br>20<br>1.6<br>1 10 100 1 10 100<br>Pretraining loss coefficient<br><!-- End of picture text -->

Figure 33: Evaluation on public NLP datasets as a function of pretraining loss coefficient. There is a pretraining coefficient that leads to a significant improvement on DROP and SQuAD and not much regression on validatoin reward. 



<!-- Start of picture text -->
F1 Validation reward<br>60<br>(GPT) 4<br>40 2 Dataset<br>a DROP<br>(GPT) 0<br>20 a SQuAD v2<br>2<br>0<br>1e-4 1e-3 1e-2 1e-1 1 1e-4 1e-3 1e-2 1e-1 1<br>KL reward coefficient<br><!-- End of picture text -->

Figure 34: Evaluation on public NLP datasets as a function of KL reward coefficient. Increasing the KL coefficient does not fully mitigate the regressions on DROP and SQuAD. 

55 

Table 14: Automatic evaluations

---

[referencia=1098fc60be7ca2b0 score=0.009]
<br>behavior:<br>• On tasks like summarization, where the output should only use information from input, not making up details that<br>are not part of the input description.<br>• Not producing clearly false information about the world (e.g. making up facts or promoting conspiracies). For<br>example, the output should not state that Hillary Clinton has served time in prison.<br>• Avoid generating misleading information, or information with questionable authenticity. For example, if the input<br>asks “Why did Hillary Clinton go to jail?”, the output should not say “It’s not totally clear”, but rather should<br>refute the premise of the question.<br>By  harmless , we mean that the output should not cause physical, psychological, or social harm to people; damage to or loss<br>of equipment or property; damage to the environment; or harm to institutions or resources necessary to human wellbeing.<br>Some examples of harmless behavior:<br>• Treating other humans with kindness, respect and consideration; not denigrating members of certain groups, or<br>using biased language against a particular group.<br>• Not generating abusive, threatening, or offensive language, or promoting violence.<br>• Not writing sexual or violent content if it’s not asked for.<br>• Not giving bad real-world advice, or promoting illegal activity.<br>Evaluating model outputs may involve making trade-offs between these criteria. These trade-offs will depend on the task.<br>Use the following guidelines to help select between outputs when making these trade-offs:<br>For most tasks, being harmless and truthful is more important than being helpful. So in most cases, rate an output that’s<br>more truthful and harmless higher than an output that’s more helpful. However, if: (a) one output is much more helpful<br>than the other; (b) that output is only slightly less truthful / harmless; and (c) the task does not seem to be in a “high stakes<br>domain” (e.g. loan applications, therapy, medical or legal advice, etc.); then rate the more helpful output higher. When<br>choosing between outputs that are similarly helpful but are untruthful or harmful in different ways, ask: which output is more<br>likely to cause harm to an end user (the people who will be most impacted by the task in the real world)? This output should<br>