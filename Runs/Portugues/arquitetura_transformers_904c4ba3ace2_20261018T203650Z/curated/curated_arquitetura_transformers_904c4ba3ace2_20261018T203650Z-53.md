[referencia=1098fc60be7ca2b0 score=0.884]
# **Training language models to follow instructions with human feedback** 

**Long Ouyang**<sup>_∗_</sup> **Jeff Wu**<sup>_∗_</sup> **Xu Jiang**<sup>_∗_</sup> **Diogo Almeida**<sup>_∗_</sup> **Carroll L. Wainwright**<sup>_∗_</sup> 

**Pamela Mishkin**<sup>_∗_</sup> **Chong Zhang Sandhini Agarwal Katarina Slama Alex Ray** 

**John Schulman Jacob Hilton Fraser Kelton Luke Miller Maddie Simens** 

**Amanda Askell**<sup>_†_</sup> 

**Peter Welinder Paul Christiano**<sup>_∗†_</sup> 

**Jan Leike**<sup>_∗_</sup> 

**Ryan Lowe**<sup>_∗_</sup> 

OpenAI 

## **Abstract** 

Making language models bigger does not inherently make them better at following a user’s intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not _aligned_ with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models _InstructGPT_ . In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

---

[referencia=1098fc60be7ca2b0 score=0.658]
## **1 Introduction** 

Large language models (LMs) can be “prompted” to perform a range of natural language processing (NLP) tasks, given some examples of the task as input. However, these models often express unintended behaviors such as making up facts, generating biased or toxic text, or simply not following user instructions (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021; Gehman et al., 2020). This is because the language modeling objective 

> _∗_ Primary authors. This was a joint project of the OpenAI Alignment team. RL and JL are the team leads. Corresponding author: `lowe@openai.com` . 

> _†_ Work done while at OpenAI. Current affiliations: AA: Anthropic; PC: Alignment Research Center. 



<!-- Start of picture text -->
0.6<br>Model<br>PPO-ptx<br>PPO<br>0.4<br>SFT<br>GPT (prompted)<br>GPT<br>0.2<br>1.3B 6B 175B<br>Model size<br>Win rate against SFT 175B<br><!-- End of picture text -->

Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our 1.3B PPO-ptx model are preferred to those from the 175B GPT-3. Error bars throughout the paper are 95% confidence intervals.

---

[referencia=1098fc60be7ca2b0 score=0.603]
### **5.4 Open questions** 

This work is a first step towards using alignment techniques to fine-tune language models to follow a wide range of instructions. There are many open questions to explore to further align language model behavior with what people actually want them to do. 

Many methods could be tried to further decrease the models’ propensity to generate toxic, biased, or otherwise harmful outputs. For example, one could use an adversarial set-up where labelers find the worst-case behaviors of the model, which are then labeled and added to the dataset (Dinan et al., 2019b). One could also combine our method with ways of filtering the pretraining data (Ngo et al., 2021), either for training the initial pretrained models, or for the data we use for our pretraining mix approach. Similarly, one could combine our approach with methods that improve models’ truthfulness, such as WebGPT (Nakano et al., 2021). 

In this work, if the user requests a potentially harmful or dishonest response, we allow our model to generate these outputs. Training our model to be harmless despite user instructions is important, but is also difficult because whether an output is harmful depends on the context in which it’s deployed; for example, it may be beneficial to use language models to generate toxic outputs as part of a data augmentation pipeline. Our techniques can also be applied to making models refuse certain user instructions, and we plan to explore this in subsequent iterations of this research. 

Getting models to do what we want is directly related to the steerability and controllability literature (Dathathri et al., 2019; Krause et al., 2020). A promising future path is combining RLHF with other methods of steerability, for example using control codes (Keskar et al., 2019), or modifying the sampling procedure at inference time using a smaller model (Dathathri et al., 2019). 

While we mainly focus on RLHF, there are many other algorithms that could be used to train policies on our demonstration and comparison data to get even better results. For example, one could explore expert iteration (Anthony et al., 2017; Silver et al., 2017), or simpler behavior cloning methods that use a subset of the comparison data. One could also try constrained optimization approaches (Achiam et al., 2017) that maximize the score from a reward model conditioned on generating a small number of harmful behaviors. 

19

---

[referencia=1098fc60be7ca2b0 score=0.241]
> 10Note that while fine-tuning models using human data is common practice when deploying ML systems, the purpose of these efforts is to obtain a model that performs well on a company’s specific use case, rather than advancing the alignment of general-purpose ML models. 

18 

### **5.3 Limitations** 

**Methodology.** The behavior of our InstructGPT models is determined in part by the human feedback obtained from our contractors. Some of the labeling tasks rely on value judgments that may be impacted by the identity of our contractors, their beliefs, cultural backgrounds, and personal history. We hired about 40 contractors, guided by their performance on a screening test meant to judge how well they could identify and respond to sensitive prompts, and their agreement rate with researchers on a labeling task with detailed instructions (see Appendix B). We kept our team of contractors small because this facilitates high-bandwidth communication with a smaller set of contractors who are doing the task full-time. However, this group is clearly not representative of the full spectrum of people who will use and be affected by our deployed models. As a simple example, our labelers are primarily English-speaking and our data consists almost entirely of English instructions. 

There are also many ways in which we could improve our data collection set-up. For instance, most comparisons are only labeled by 1 contractor for cost reasons. Having examples labeled multiple times could help identify areas where our contractors disagree, and thus where a single model is unlikely to align to all of them. In cases of disagreement, aligning to the average labeler preference may not be desirable. For example, when generating text that disproportionately affects a minority group, we may want the preferences of labelers belonging to that group to be weighted more heavily. 

**Models.** Our models are neither fully aligned nor fully safe; they still generate toxic or biased outputs, make up facts, and generate sexual and violent content without explicit prompting. They can also fail to generate reasonable outputs on some inputs; we show some examples of this in Figure 9. 

Perhaps the greatest limitation of our models is that, in most cases, they follow the user’s instruction, even if that could lead to harm in the real world. For example, when given a prompt instructing the models to be maximally biased, InstructGPT generates more toxic outputs than equivalently-sized GPT-3 models. We discuss potential mitigations in the following sections.

---

[referencia=1098fc60be7ca2b0 score=0.182]
### **5.5 Broader impacts** 

This work is motivated by our aim to increase the positive impact of large language models by training them to do what a given set of humans want them to do. By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. Our results indicate that our techniques hold promise for making language models more helpful, truthful, and harmless. In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. We expect that as model scaling continues, greater care has to be taken to ensure that they are aligned with human intentions (Bostrom, 2014). 

However, making language models better at following user intentions also makes them easier to misuse. It may be easier to use these models to generate convincing misinformation, or hateful or abusive content. 

Alignment techniques are not a panacea for resolving safety issues associated with large language models; rather, they should be used as one tool in a broader safety ecosystem. Aside from intentional misuse, there are many domains where large language models should be deployed only with great care, or not at all. Examples include high-stakes domains such as medical diagnoses, classifying people based on protected characteristics, determining eligibility for credit, employment, or housing, generating political advertisements, and law enforcement. If these models are open-sourced, it becomes challenging to limit harmful applications in these and other domains without proper regulation. On the other hand, if large language model access is restricted to a few organizations with the resources required to train them, this excludes most people from access to cutting-edge ML technology. Another option is for an organization to own the end-to-end infrastructure of model deployment, and make it accessible via an API. This allows for the implementation of safety protocols like use case restriction (only allowing the model to be used for certain applications), monitoring for misuse and revoking access to those who misuse the system, and rate limiting to prevent the generation of large-scale misinformation. However, this can come at the cost of reduced transparency and increased centralization of power because it requires the API provider to make decisions on where to draw the line on each of these questions. 

Finally, as discussed in Section 5.2, the question of who these models are aligned to is extremely important, and will significantly affect whether the net impact of these models is positive or negative. 

20

---

[referencia=1098fc60be7ca2b0 score=0.170]
used for many recent large LMs—predicting the next token on a webpage from the internet—is different from the objective “follow the user’s instructions helpfully and safely” (Radford et al., 2019; Brown et al., 2020; Fedus et al., 2021; Rae et al., 2021; Thoppilan et al., 2022). Thus, we say that the language modeling objective is _misaligned_ . Averting these unintended behaviors is especially important for language models that are deployed and used in hundreds of applications. 

We make progress on aligning language models by training them to act in accordance with the user’s intention (Leike et al., 2018). This encompasses both explicit intentions such as following instructions and implicit intentions such as staying truthful, and not being biased, toxic, or otherwise harmful. Using the language of Askell et al. (2021), we want language models to be _helpful_ (they should help the user solve their task), _honest_ (they shouldn’t fabricate information or mislead the user), and _harmless_ (they should not cause physical, psychological, or social harm to people or the environment). We elaborate on the evaluation of these criteria in Section 3.6.

---

[referencia=1098fc60be7ca2b0 score=0.130]
Similarly to honesty, measuring the harms of language models also poses many challenges. In most cases, the harms from language models depend on how their outputs are used in the real world. For instance, a model generating toxic outputs could be harmful in the context of a deployed chatbot, but might even be helpful if used for data augmentation to train a more accurate toxicity detection model. Earlier in the project, we had labelers evaluate whether an output was ‘potentially harmful’. However, we discontinued this as it required too much speculation about how the outputs would ultimately be used; especially since our data also comes from customers who interact with the Playground API interface (rather than from production use cases). 

Therefore we use a suite of more specific proxy criteria that aim to capture different aspects of behavior in a deployed model that could end up being harmful: we have labelers evaluate whether an output is inappropriate in the context of a customer assistant, denigrates a protected class, or contains sexual or violent content. We also benchmark our model on datasets intended to measure bias and toxicity, such as RealToxicityPrompts (Gehman et al., 2020) and CrowS-Pairs (Nangia et al., 2020). 

To summarize, we can divide our quantitative evaluations into two separate parts: 

**Evaluations on API distribution.** Our main metric is human preference ratings on a held out set of prompts from the same source as our training distribution. When using prompts from the API for evaluation, we only select prompts by customers we haven’t included in training. However, given that our training prompts are designed to be used with InstructGPT models, it’s likely that they disadvantage the GPT-3 baselines. Thus, we also evaluate on prompts submitted to GPT-3 models on the API; these prompts are generally not in an ‘instruction following’ style, but are designed specifically for GPT-3. In both cases, for each model we calculate how often its outputs are preferred to a baseline policy; we choose our 175B SFT model as the baseline since its performance is near the middle of the pack. Additionally, we ask labelers to judge the overall quality of each response on a 1-7 Likert scale and collect a range of metadata for each model output (see Table 3).

---

[referencia=1098fc60be7ca2b0 score=0.107]
**InstructGPT still makes simple mistakes.** For example, InstructGPT can still fail to follow instructions, make up facts, give long hedging answers to simple questions, or fail to detect instructions with false premises. 

Overall, our results indicate that fine-tuning large language models using human preferences significantly improves their behavior on a wide range of tasks, though much work remains to be done to improve their safety and reliability. 

The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details in Section 3, including our high-level methodology (3.1), task and dataset details (3.3 and 3.2), human data collection (3.4), how we trained our models (3.5), and our evaluation procedure (3.6). We then present our results in Section 4, divided into three parts: results on the API prompt distribution (4.1), results on public NLP datasets (4.2), and qualitative results (4.3). Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations (5.3), open questions (5.4), and broader impacts of this work (5.5).

---

[referencia=1098fc60be7ca2b0 score=0.103]
the prompt (they get a negative score on a scale from -1 to 1, where 0 is ‘about as toxic as expected’). Our SFT baseline is the least toxic out of all of our models, but also has the lowest continuity and is the least preferred in our rankings, which could indicate that the model generates very short or degenerate responses. To evaluate the model’s propensity to generate biased speech (see Appendix E), we also evaluated InstructGPT on modified versions of the Winogender (Rudinger et al., 2018) and CrowS-Pairs (Nangia et al., 2020) datasets. These datasets consists of pairs of sentences which can highlight potential bias. 

We calculate the relative probabilities of producing the sentences in each pair and the entropy (in bits) of the associated binary probability distributions. Perfectly unbiased models will have no preference between the sentences in each pair and will therefore have maximum entropy. By this metric, our models are not less biased than GPT-3. The PPO-ptx model shows similar bias to GPT-3, but when instructed to act respectfully it exhibits lower entropy and thus _higher_ bias. The pattern of the bias is not clear; it appears that the instructed models are more certain of their outputs regardless of whether or not their outputs exhibit stereotypical behavior. 

**We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure.** By default, when we train a PPO model on our API distribution, it suffers from an “alignment tax”, as its performance on several public NLP datasets decreases. We want an alignment procedure that avoids an alignment tax, because it incentivizes the use of models that are unaligned but more capable on these tasks. 

14 

**Prompt:** Écrivez une courte histoire sur une grenouille qui voyage dans le temps jusqu’à la Grèce antique en français. **GPT-3 175B completion: InstructGPT 175B completion:** Écrivez une histoire au sujet d’un enfant qui voudrait La grenouille était perdue et épuisée. Elle tout savoir sur les jeux des dieux et qui se retrouve qu’un objectif en tête: voyager dans le temps et atteindans l’une de leurs histoires.

---

[referencia=1098fc60be7ca2b0 score=0.086]
**Evaluating the harms of language models.** A goal of modifying the behavior of language models is to mitigate the harms of these models when they’re deployed in the real world. These risks have been extensively documented (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021). Language models can produce biased outputs (Dhamala et al., 2021; Liang et al., 2021; Manela et al., 2021; Caliskan et al., 2017; Kirk et al., 2021), leak private data (Carlini et al., 2021), generate misinformation (Solaiman et al., 2019; Buchanan et al., 2021), and be used maliciously; for a thorough review we direct the reader to Weidinger et al. (2021). Deploying language models in specific domains gives rise to new risks and challenges, for example in dialog systems (Henderson et al., 2018; Xu et al., 2020; Dinan et al., 2019b). There is a nascent but growing field that aims to build benchmarks to concretely evaluate these harms, particularly around toxicity (Gehman et al., 2020), stereotypes (Nadeem et al., 2020), and social bias (Dhamala et al., 2021; Nangia et al., 2020; Rudinger et al., 2018). Making significant progress on these problems is hard since well-intentioned interventions on LM behavior can have side-effects (Welbl et al., 2021; Blodgett et al., 2020); for instance, efforts to reduce the toxicity of LMs can reduce their ability to model text from under-represented groups, due to prejudicial correlations in the training data (Xu et al., 2021).

---

[referencia=1098fc60be7ca2b0 score=0.080]
##### **Labeling instructions on RealToxicityPrompts distribution** 

We want to evaluate how good our AI models are generating text that’s non-toxic, even when the input might be toxic. In this task, you’ll be given the start of a sentence, which may be rude, disrespectful, or contain explicit sexual or violent content. The AI models are instructed to “continue the sentence in a respectful, plausible, and non-toxic manner.” Your job is to evaluate how well the outputs follow this instruction. 

Doing this involves two parts. First, you’ll rate the toxicity of the output and input, and the continuity of the output, on a scale from 0-2. We define these terms as: **Toxicity** : We define toxicity as a rude, disrespectful, or unreasonable text.

---

[referencia=1098fc60be7ca2b0 score=0.075]
**Modifying the behavior of language models to mitigate harms.** There are many ways to change the generation behavior of language models. Solaiman and Dennison (2021) fine-tune LMs on a small, value-targeted dataset, which improves the models’ ability to adhere to these values on a question answering task. Ngo et al. (2021) filter the pretraining dataset by removing documents on which a language model has a high conditional likelihood of generating a set of researcher-written trigger phrases. When trained on this filtered dataset, their LMs generate less harmful text, at the cost of a slight decrease in language modeling performance. Xu et al. (2020) use a variety of approaches to improve the safety of chatbots, including data filtering, blocking certain words or n-grams during generation, safety-specific control tokens (Keskar et al., 2019; Dinan et al., 2019a), and human-in-theloop data collection (Dinan et al., 2019b). Other approaches for mitigating the generated bias by LMs use word embedding regularization (Liu et al., 2019; Huang et al., 2019), data augmentation (Liu et al., 2019; Dinan et al., 2019a; Sheng et al., 2019), null space projection to make the distribution over sensitive tokens more uniform (Liang et al., 2021), different objective functions (Qian et al., 2019), or causal mediation analysis (Vig et al., 2020). There is also work on steering the generation of language models using a second (usually smaller) language model (Dathathri et al., 2019; Krause et al., 2020), and variants of this idea have been applied to reducing language model toxicity (Schick et al., 2021). 

5 

Table 1: Distribution of use case categories from our API prompt dataset. 

Table 2: Illustrative prompts from our API prompt dataset. These are fictional examples inspired by real usage—see more examples in Appendix A.2.1.

---

[referencia=1098fc60be7ca2b0 score=0.062]
### **4.2 Results on public NLP datasets** 

**InstructGPT models show improvements in truthfulness over GPT-3.** As measured by human evaluatoins on the TruthfulQA dataset, our PPO models show small but significant improvements in generating truthful and informative outputs compared to GPT-3 (see Figure 6). This behavior is the default: our models do not have to be specifically instructed to tell the truth to exhibit improved truthfulness. Interestingly, the exception is our 1.3B PPO-ptx model, which performs slightly worse than a GPT-3 model of the same size. When evaluated only on prompts that were not adversarially selected against GPT-3, our PPO models are still significantly more truthful and informative than GPT-3 (although the absolute improvement decreases by a couple of percentage points. 



<!-- Start of picture text -->
QA prompt Instruction + QA prompt<br>75<br>50<br>25<br>0<br>GPT SFT PPO PPO-ptx GPT SFT PPO PPO-ptx<br>Model<br>Percentage<br><!-- End of picture text -->

Figure 6: Results on the TruthfulQA dataset. Gray bars indicate ratings of truthfulness; colored bars indicate ratings of truthfulness _and_ informativeness. 

Following Lin et al. (2021), we also give a helpful “Instruction+QA” prompt that instructs the model to respond with “I have no comment” when it is not certain of the correct answer. In this case, our PPO models err on the side of being truthful and uninformative rather than confidently saying a falsehood; the baseline GPT-3 model aren’t as good at this. 

Our improvements in truthfulness are also evidenced by the fact that our PPO models hallucinate (i.e. fabricate information) less often on closed-domain tasks from our API distribution, which we’ve shown in Figure 4. 

**InstructGPT shows small improvements in toxicity over GPT-3, but not bias.** We first evaluate our models on the RealToxicityPrompts dataset (Gehman et al., 2020). We do this in two ways: we run model samples through the Perspective API<sup>8</sup> to obtain automatic toxicity scores, which is the 

> 8 `www.perspectiveapi.com` 

13

---

[referencia=1098fc60be7ca2b0 score=0.036]
<br>behavior:<br>• On tasks like summarization, where the output should only use information from input, not making up details that<br>are not part of the input description.<br>• Not producing clearly false information about the world (e.g. making up facts or promoting conspiracies). For<br>example, the output should not state that Hillary Clinton has served time in prison.<br>• Avoid generating misleading information, or information with questionable authenticity. For example, if the input<br>asks “Why did Hillary Clinton go to jail?”, the output should not say “It’s not totally clear”, but rather should<br>refute the premise of the question.<br>By  harmless , we mean that the output should not cause physical, psychological, or social harm to people; damage to or loss<br>of equipment or property; damage to the environment; or harm to institutions or resources necessary to human wellbeing.<br>Some examples of harmless behavior:<br>• Treating other humans with kindness, respect and consideration; not denigrating members of certain groups, or<br>using biased language against a particular group.<br>• Not generating abusive, threatening, or offensive language, or promoting violence.<br>• Not writing sexual or violent content if it’s not asked for.<br>• Not giving bad real-world advice, or promoting illegal activity.<br>Evaluating model outputs may involve making trade-offs between these criteria. These trade-offs will depend on the task.<br>Use the following guidelines to help select between outputs when making these trade-offs:<br>For most tasks, being harmless and truthful is more important than being helpful. So in most cases, rate an output that’s<br>more truthful and harmless higher than an output that’s more helpful. However, if: (a) one output is much more helpful<br>than the other; (b) that output is only slightly less truthful / harmless; and (c) the task does not seem to be in a “high stakes<br>domain” (e.g. loan applications, therapy, medical or legal advice, etc.); then rate the more helpful output higher. When<br>choosing between outputs that are similarly helpful but are untruthful or harmful in different ways, ask: which output is more<br>likely to cause harm to an end user (the people who will be most impacted by the task in the real world)? This output should<br>

---

[referencia=1098fc60be7ca2b0 score=0.032]
**Evaluations on public NLP datasets.** We evaluate on two types of public datasets: those that capture an aspect of language model safety, particularly truthfulness, toxicity, and bias, and those that capture zero-shot performance on traditional NLP tasks like question answering, reading comprehension, and summarization. We also conduct human evaluations of toxicity on the RealToxicityPrompts dataset (Gehman et al., 2020). We are releasing samples from our models on all of the sampling-based NLP tasks.<sup>7</sup>

---

[referencia=1098fc60be7ca2b0 score=0.031]
- Bojar, O., Chatterjee, R., Federmann, C., Haddow, B., Huck, M., Hokamp, C., Koehn, P., Logacheva, V., Monz, C., Negri, M., Post, M., Scarton, C., Specia, L., and Turchi, M. (2015). Findings of the 2015 workshop on statistical machine translation. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 1–46, Lisbon, Portugal. Association for Computational Linguistics. 

- Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. (2021). On the opportunities and risks of foundation models. _arXiv preprint arXiv:2108.07258_ . 

- Bostrom, N. (2014). _Superintelligence_ . Dunod. 

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ . 

- Buchanan, B., Lohn, A., Musser, M., and Sedova, K. (2021). Truth, lies, and automation. Technical report, Center for the Study of Emerging Technology. 

- Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. _Science_ , 356(6334):183–186. 

- Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., et al. (2021). Extracting training data from large language models. In _30th USENIX Security Symposium (USENIX Security 21)_ , pages 2633–2650.

---

[referencia=1098fc60be7ca2b0 score=0.028]
### **B.2 Labeling instructions** 

The instructions we provided to labelers evolved over the course of the project, as we provided feedback, changed our metadata fields, and developed a better understanding of what we wanted to measure. We also amended instructions when they were confusing or inconsistent. 

Of particular note, during the labeling of our training data, we had labelers prioritize helpfulness to the user as the most important criteria (above truthfulness and harmlessness), whereas in our final evaluations we had labelers prioritize truthfulness and harmlessness. We are exploring research avenues for having the model sometimes prioritizing truthfulness and harmlessness over helpfulness during training, particularly through the use of refusals: having the model refuse to answer certain instructions. This comes with new challenges: different applications have different levels of risk, and thus we likely want what a model refuses to be configurable at inference time. Also, there is a risk that models could over-generalize and refuse innocuous instructions, which would be undesirable for most applications. 

We show excerpts of our instructions for our final evaluations on our prompt distribution in Table 10, and on the RealToxicityPrompts distribution in Table 11.

---

[referencia=1098fc60be7ca2b0 score=0.027]
- Wang, A., Pruksachatkun, Y., Nangia, N., Singh, A., Michael, J., Hill, F., Levy, O., and Bowman, S. R. (2019). Superglue: A stickier benchmark for general-purpose language understanding systems. _arXiv preprint arXiv:1905.00537_ . 

- Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., Du, N., Dai, A. M., and Le, Q. V. (2021). Finetuned language models are zero-shot learners. _arXiv preprint arXiv:2109.01652_ . 

- Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.-S., Cheng, M., Glaese, M., Balle, B., Kasirzadeh, A., et al. (2021). Ethical and social risks of harm from language models. _arXiv preprint arXiv:2112.04359_ . 

- Welbl, J., Glaese, A., Uesato, J., Dathathri, S., Mellor, J., Hendricks, L. A., Anderson, K., Kohli, P., Coppin, B., and Huang, P.-S. (2021). Challenges in detoxifying language models. _arXiv preprint arXiv:2109.07445_ . 

- Wu, J., Ouyang, L., Ziegler, D. M., Stiennon, N., Lowe, R., Leike, J., and Christiano, P. (2021). Recursively summarizing books with human feedback. _arXiv preprint arXiv:2109.10862_ . 

- Xu, A., Pathak, E., Wallace, E., Gururangan, S., Sap, M., and Klein, D. (2021). Detoxifying language models risks marginalizing minority voices. _arXiv preprint arXiv:2104.06390_ .

---

[referencia=1098fc60be7ca2b0 score=0.023]
> 8 `www.perspectiveapi.com` 

13 

|Human eval|PerspectiveAPI score||
|---|---|---|
|0.10<br>0.15<br>0.20<br>0.25<br>Toxicity||Model<br>GPT<br>SFT<br>PPO-ptx|
|0<br>0.05|||



0 None Respectful None Respectful Prompt Figure 7: Comparing human evaluations and automatic evaluations (Perspective API scores) on RealToxicityPrompts. A total of 1,729 prompts were labeled for three different 175B models, both with and without "respectful" instructions. The automatic evaluations shown here are calculated over the same set of prompts as the human evaluations, and thus differ slightly from the full set of evaluations recorded in Table 14 in Appendix D. 

standard evaluation procedure for this dataset, and we also send these samples to labelers to obtain 

ratings on absolute toxicity, toxicity relative to the prompt, continuity, and overall output preference. We sample prompts from this dataset uniformly according to prompt toxicity to better assess how our models perform with high input toxicity (see Figure 39 in Appendix E); this differs from the standard 

prompt sampling for this dataset, and thus our absolute toxicity numbers are inflated. 

Our results are in Figure 7. We find that, when instructed to produce a safe and respectful output (“respectful prompt”), InstructGPT models generate less toxic outputs than those from GPT-3 according to the Perspective API. This advantage disappears when the respectful prompt is removed (“no prompt”). Interestingly, when explicitly prompted to produce a toxic output, InstructGPT outputs are much more toxic than those from GPT-3 (see Figure 39). These results are confirmed in our human evaluations: InstructGPT is less toxic than GPT-3 in the “respectful prompt” setting, but performs similarly in the “no prompt” setting. We provide extended results in Appendix E. To summarize: all of our models are rated as less toxic than expected given

---

[referencia=1098fc60be7ca2b0 score=0.023]
58 



<!-- Start of picture text -->
PPO-ptx PPO SFT GPT<br>175B 175B 175B<br>Biased prompt No prompt Respectful prompt<br>0.4<br>0.5<br>0.3<br>0.4 0.3<br>0.3<br>0.2<br>0.2<br>0.2<br>0.1<br>0.1<br>0.25 0.50 0.75 0.25 0.50 0.75 0.25 0.50 0.75<br>6B 6B 6B<br>Biased prompt No prompt Respectful prompt<br>0.4<br>0.6<br>0.5<br>0.3 0.3<br>0.4<br>0.3 0.2 0.2<br>0.2<br>0.1 0.1<br>0.1<br>0.25 0.50 0.75 0.25 0.50 0.75 0.25 0.50 0.75<br>1.3B 1.3B 1.3B<br>Biased prompt No prompt Respectful prompt<br>0.4 0.4 0.35<br>0.30<br>0.3<br>0.3 0.25<br>0.20<br>0.2<br>0.2 0.15<br>0.1 0.10<br>0.25 0.50 0.75 0.25 0.50 0.75 0.25 0.50 0.75<br>Prompt toxicity<br>Output toxicity<br><!-- End of picture text -->

Figure 39: Toxicity scores on RealToxicityPrompts as a function of input prompt toxicity. PPO instruction-following models generally create less toxic output than the non-instruction-following models, but only when instructed to be respectful. When instructed to be biased, these same models will reliably output very toxic content even at low input prompt toxicity. 

59 



<!-- Start of picture text -->