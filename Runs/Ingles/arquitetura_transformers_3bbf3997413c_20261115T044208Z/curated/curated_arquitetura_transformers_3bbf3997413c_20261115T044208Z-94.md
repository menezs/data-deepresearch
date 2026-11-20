[referencia=1098fc60be7ca2b0 score=0.962]
**InstructGPT still makes simple mistakes.** For example, InstructGPT can still fail to follow instructions, make up facts, give long hedging answers to simple questions, or fail to detect instructions with false premises. 

Overall, our results indicate that fine-tuning large language models using human preferences significantly improves their behavior on a wide range of tasks, though much work remains to be done to improve their safety and reliability. 

The rest of this paper is structured as follows: We first detail related work in Section 2, before diving into our method and experiment details in Section 3, including our high-level methodology (3.1), task and dataset details (3.3 and 3.2), human data collection (3.4), how we trained our models (3.5), and our evaluation procedure (3.6). We then present our results in Section 4, divided into three parts: results on the API prompt distribution (4.1), results on public NLP datasets (4.2), and qualitative results (4.3). Finally we give an extended discussion of our work in Section 5, including implications for alignment research (5.1), what we are aligning to (5.2), limitations (5.3), open questions (5.4), and broader impacts of this work (5.5).

---

[referencia=1098fc60be7ca2b0 score=0.961]
**InstructGPT still makes simple mistakes.** In interacting with our 175B PPO-ptx model, we have noticed it can still make simple mistakes, despite its strong performance on many different language tasks. To give a few examples: (1) when given an instruction with a false premise, the model sometimes incorrectly assumes the premise is true, (2) the model can overly hedge; when given a simple question, it can sometimes say that there is no one answer to the question and give multiple possible answers, even when there is one fairly clear answer from the context, and (3) the model’s performance degrades when instructions contain multiple explicit constraints (e.g. “list 10 movies made in the 1930’s set in France”) or when constraints can be challenging for language models (e.g. writing a summary in a specified number of sentences). 

9We generally instruct our labelers to skip evaluations where they are missing the required expertise, though sometimes labelers use a translation service to evaluate simple instructions in languages that they do not speak. 

16 

We show some examples of these behaviors in Figure 9. We suspect that behavior (2) emerges partly because we instruct labelers to reward epistemic humility; thus, they may tend to reward outputs that hedge, and this gets picked up by our reward model. We suspect that behavior (1) occurs because there are few prompts in the training set that assume false premises, and our models don’t generalize well to these examples. We believe both these behaviors could be dramatically reduced with adversarial data collection (Dinan et al., 2019b).

---

[referencia=1098fc60be7ca2b0 score=0.939]
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



<!-- Start of picture text -->

---

[referencia=1098fc60be7ca2b0 score=0.911]
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

[referencia=1098fc60be7ca2b0 score=0.854]
**Our models generalize to the preferences of “held-out” labelers that did not produce any training data.** To test the generalization of our models, we conduct a preliminary experiment with held-out labelers, and find that they prefer InstructGPT outputs to outputs from GPT-3 at about the same rate as our training labelers. However, more work is needed to study how these models perform on broader groups of users, and how they perform on inputs where humans disagree about the desired behavior. 

**Public NLP datasets are not reflective of how our language models are used.** We compare GPT-3 fine-tuned on our human preference data (i.e. InstructGPT) to GPT-3 fine-tuned on two different compilations of public NLP tasks: the FLAN (Wei et al., 2021) and T0 (Sanh et al., 2021) (in particular, the T0++ variant). These datasets consist of a variety of NLP tasks, combined with natural language instructions for each task. On our API prompt distribution, our FLAN and T0 models perform slightly worse than our SFT baseline, and labelers significantly prefer InstructGPT to these models (InstructGPT has a 73.4 _±_ 2% winrate vs. our baseline, compared to 26.8 _±_ 2% and 29.8 _±_ 2% for our version of T0 and FLAN, respectively). 

**InstructGPT models show promising generalization to instructions outside of the RLHF finetuning distribution.** We qualitatively probe InstructGPT’s capabilities, and find that it is able to follow instructions for summarizing code, answer questions about code, and sometimes follows instructions in different languages, despite these instructions being very rare in the fine-tuning distribution. In contrast, GPT-3 can perform these tasks but requires more careful prompting, and does not usually follow instructions in these domains. This result is exciting because it suggests that our models are able to generalize the notion of “following instructions.” They retain some alignment even on tasks for which they get very little direct supervision signal. 

**InstructGPT still makes simple mistakes.** For example, InstructGPT can still fail to follow instructions, make up facts, give long hedging answers to simple questions, or fail to detect instructions with false premises.

---

[referencia=1098fc60be7ca2b0 score=0.769]
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

[referencia=1098fc60be7ca2b0 score=0.747]
> 8 `www.perspectiveapi.com` 

13 



<!-- Start of picture text -->
Human eval PerspectiveAPI score<br>0.25<br>0.20<br>Model<br>0.15 GPT<br>SFT<br>0.10<br>PPO-ptx<br>0.05<br>0<br>None Respectful None Respectful<br>Prompt<br>Toxicity<br><!-- End of picture text -->

Figure 7: Comparing human evaluations and automatic evaluations (Perspective API scores) on RealToxicityPrompts. A total of 1,729 prompts were labeled for three different 175B models, both with and without "respectful" instructions. The automatic evaluations shown here are calculated over the same set of prompts as the human evaluations, and thus differ slightly from the full set of evaluations recorded in Table 14 in Appendix D. 

standard evaluation procedure for this dataset, and we also send these samples to labelers to obtain ratings on absolute toxicity, toxicity relative to the prompt, continuity, and overall output preference. We sample prompts from this dataset uniformly according to prompt toxicity to better assess how our models perform with high input toxicity (see Figure 39 in Appendix E); this differs from the standard prompt sampling for this dataset, and thus our absolute toxicity numbers are inflated. 

Our results are in Figure 7. We find that, when instructed to produce a safe and respectful output (“respectful prompt”), InstructGPT models generate less toxic outputs than those from GPT-3 according to the Perspective API. This advantage disappears when the respectful prompt is removed (“no prompt”). Interestingly, when explicitly prompted to produce a toxic output, InstructGPT outputs are much more toxic than those from GPT-3 (see Figure 39). 

These results are confirmed in our human evaluations: InstructGPT is less toxic than GPT-3 in the “respectful prompt” setting, but performs similarly in the “no prompt” setting. We provide extended results in Appendix E. To summarize: all of our models are rated as less toxic than expected given the prompt (they get a negative score on a scale from -1 to 1, where 0 is ‘about as toxic as expected’). Our SFT baseline is the least toxic out of all of our models, but also has the lowest continuity and is the least preferred in our rankings, which could indicate that the model generates very short or degenerate responses.

---

[referencia=1098fc60be7ca2b0 score=0.702]
We focus on _fine-tuning_ approaches to aligning language models. Specifically, we use reinforcement learning from human feedback (RLHF; Christiano et al., 2017; Stiennon et al., 2020) to fine-tune GPT-3 to follow a broad class of written instructions (see Figure 2). This technique uses human preferences as a reward signal to fine-tune our models. We first hire a team of 40 contractors to label our data, based on their performance on a screening test (see Section 3.4 and Appendix B.1 for more details). We then collect a dataset of human-written demonstrations of the desired output behavior on (mostly English) prompts submitted to the OpenAI API<sup>3</sup> and some labeler-written prompts, and use this to train our supervised learning baselines. Next, we collect a dataset of human-labeled comparisons between outputs from our models on a larger set of API prompts. We then train a reward model (RM) on this dataset to predict which model output our labelers would prefer. Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm (Schulman et al., 2017). We illustrate this process in Figure 2. This procedure aligns the behavior of GPT-3 to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of “human values”; we discuss this further in Section 5.2. We call the resulting models _InstructGPT_ . 

We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers (who are not represented in the training data). We also conduct automatic evaluations on a range of public NLP datasets. We train three model 

> 3Specifically, we train on prompts submitted to earlier versions of the InstructGPT models on the OpenAI API Playground, which were trained only using demonstration data. We filter out prompts containing PII. 

2

---

[referencia=1098fc60be7ca2b0 score=0.685]
## **1 Introduction** 

Large language models (LMs) can be “prompted” to perform a range of natural language processing (NLP) tasks, given some examples of the task as input. However, these models often express unintended behaviors such as making up facts, generating biased or toxic text, or simply not following user instructions (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021; Gehman et al., 2020). This is because the language modeling objective 

> _∗_ Primary authors. This was a joint project of the OpenAI Alignment team. RL and JL are the team leads. Corresponding author: `lowe@openai.com` . 

> _†_ Work done while at OpenAI. Current affiliations: AA: Anthropic; PC: Alignment Research Center. 



<!-- Start of picture text -->
0.6<br>Model<br>PPO-ptx<br>PPO<br>0.4<br>SFT<br>GPT (prompted)<br>GPT<br>0.2<br>1.3B 6B 175B<br>Model size<br>Win rate against SFT 175B<br><!-- End of picture text -->

Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our 1.3B PPO-ptx model are preferred to those from the 175B GPT-3. Error bars throughout the paper are 95% confidence intervals.

---

[referencia=1098fc60be7ca2b0 score=0.677]
### **5.3 Limitations** 

**Methodology.** The behavior of our InstructGPT models is determined in part by the human feedback obtained from our contractors. Some of the labeling tasks rely on value judgments that may be impacted by the identity of our contractors, their beliefs, cultural backgrounds, and personal history. We hired about 40 contractors, guided by their performance on a screening test meant to judge how well they could identify and respond to sensitive prompts, and their agreement rate with researchers on a labeling task with detailed instructions (see Appendix B). We kept our team of contractors small because this facilitates high-bandwidth communication with a smaller set of contractors who are doing the task full-time. However, this group is clearly not representative of the full spectrum of people who will use and be affected by our deployed models. As a simple example, our labelers are primarily English-speaking and our data consists almost entirely of English instructions. 

There are also many ways in which we could improve our data collection set-up. For instance, most comparisons are only labeled by 1 contractor for cost reasons. Having examples labeled multiple times could help identify areas where our contractors disagree, and thus where a single model is unlikely to align to all of them. In cases of disagreement, aligning to the average labeler preference may not be desirable. For example, when generating text that disproportionately affects a minority group, we may want the preferences of labelers belonging to that group to be weighted more heavily. 

**Models.** Our models are neither fully aligned nor fully safe; they still generate toxic or biased outputs, make up facts, and generate sexual and violent content without explicit prompting. They can also fail to generate reasonable outputs on some inputs; we show some examples of this in Figure 9. 

Perhaps the greatest limitation of our models is that, in most cases, they follow the user’s instruction, even if that could lead to harm in the real world. For example, when given a prompt instructing the models to be maximally biased, InstructGPT generates more toxic outputs than equivalently-sized GPT-3 models. We discuss potential mitigations in the following sections.

---

[referencia=1098fc60be7ca2b0 score=0.675]
Similarly to honesty, measuring the harms of language models also poses many challenges. In most cases, the harms from language models depend on how their outputs are used in the real world. For instance, a model generating toxic outputs could be harmful in the context of a deployed chatbot, but might even be helpful if used for data augmentation to train a more accurate toxicity detection model. Earlier in the project, we had labelers evaluate whether an output was ‘potentially harmful’. However, we discontinued this as it required too much speculation about how the outputs would ultimately be used; especially since our data also comes from customers who interact with the Playground API interface (rather than from production use cases). 

Therefore we use a suite of more specific proxy criteria that aim to capture different aspects of behavior in a deployed model that could end up being harmful: we have labelers evaluate whether an output is inappropriate in the context of a customer assistant, denigrates a protected class, or contains sexual or violent content. We also benchmark our model on datasets intended to measure bias and toxicity, such as RealToxicityPrompts (Gehman et al., 2020) and CrowS-Pairs (Nangia et al., 2020). 

To summarize, we can divide our quantitative evaluations into two separate parts: 

**Evaluations on API distribution.** Our main metric is human preference ratings on a held out set of prompts from the same source as our training distribution. When using prompts from the API for evaluation, we only select prompts by customers we haven’t included in training. However, given that our training prompts are designed to be used with InstructGPT models, it’s likely that they disadvantage the GPT-3 baselines. Thus, we also evaluate on prompts submitted to GPT-3 models on the API; these prompts are generally not in an ‘instruction following’ style, but are designed specifically for GPT-3. In both cases, for each model we calculate how often its outputs are preferred to a baseline policy; we choose our 175B SFT model as the baseline since its performance is near the middle of the pack. Additionally, we ask labelers to judge the overall quality of each response on a 1-7 Likert scale and collect a range of metadata for each model output (see Table 3).

---

[referencia=1098fc60be7ca2b0 score=0.616]
### **B.2 Labeling instructions** 

The instructions we provided to labelers evolved over the course of the project, as we provided feedback, changed our metadata fields, and developed a better understanding of what we wanted to measure. We also amended instructions when they were confusing or inconsistent. 

Of particular note, during the labeling of our training data, we had labelers prioritize helpfulness to the user as the most important criteria (above truthfulness and harmlessness), whereas in our final evaluations we had labelers prioritize truthfulness and harmlessness. We are exploring research avenues for having the model sometimes prioritizing truthfulness and harmlessness over helpfulness during training, particularly through the use of refusals: having the model refuse to answer certain instructions. This comes with new challenges: different applications have different levels of risk, and thus we likely want what a model refuses to be configurable at inference time. Also, there is a risk that models could over-generalize and refuse innocuous instructions, which would be undesirable for most applications. 

We show excerpts of our instructions for our final evaluations on our prompt distribution in Table 10, and on the RealToxicityPrompts distribution in Table 11.

---

[referencia=1098fc60be7ca2b0 score=0.609]
### **4.1 Results on the API distribution** 

**Labelers significantly prefer InstructGPT outputs over outputs from GPT-3.** On our test set of prompts, our labelers significantly prefer InstructGPT outputs across model sizes. These results are shown in Figure 1. We find that GPT-3 outputs perform the worst, and one can obtain significant step-size improvements by using a well-crafted few-shot prompt (GPT-3 (prompted)), then by training on demonstrations using supervised learning (SFT), and finally by training on comparison data using PPO. Adding updates on the pretraining mix during PPO does not lead to large changes in labeler preference. To illustrate the magnitude of our gains: when compared directly, 175B InstructGPT outputs are preferred to GPT-3 outputs 85 _±_ 3% of the time, and preferred 71 _±_ 4% of the time to few-shot GPT-3. 

We also found that our results do not change significantly when evaluated on prompts submitted to GPT-3 models on the API (see Figure 3), though our PPO-ptx models perform slightly worse at larger model sizes. 

In Figure 4 we show that labelers also rate InstructGPT outputs favorably along several more concrete axes. Specifically, compared to GPT-3, InstructGPT outputs are more appropriate in the context of a customer assistant, more often follow explicit constraints defined in the instruction (e.g. “Write your answer in 2 paragraphs or less.”), are less likely to fail to follow the correct instruction entirely, and make up facts (‘hallucinate’) less often in closed-domain tasks. These results suggest that InstructGPT models are more reliable and easier to control than GPT-3. We’ve found that our other metadata 

11 



<!-- Start of picture text -->

---

[referencia=1098fc60be7ca2b0 score=0.553]
## **4 Results** 

In this section, we provide experimental evidence for our claims in Section 1, sorted into three parts: results on the API prompt distribution, results on public NLP datasets, and qualitative results. 

> 7Accessible here: `https://github.com/openai/following-instructions-human-feedback` . 

10 



<!-- Start of picture text -->
GPT distribution Instruct distribution<br>0.75<br>0.50<br>0.25<br>0.75<br>0.50<br>0.25<br>1.3B 6B 175B 1.3B 6B 175B<br>Model size<br>GPT<br>GPT SFT PPO PPO-ptx<br>(prompted)<br>Heldout workers<br>Win rate against SFT 175B<br>Training workers<br><!-- End of picture text -->

Figure 3: Preference results of our models, measured by winrate against the 175B SFT model. Left: results on prompts submitted to GPT models on the API; Right: results on prompts submitted to InstructGPT models on the API; Top: results from held-out labelers; Bottom: results from training labelers. We omit GPT (prompted) from the evals on prompts submitted to GPT-3 models (left) as these prompts are already designed to perform well for GPT-3, as opposed to prompts submitted to InstructGPT models (right).

---

[referencia=1098fc60be7ca2b0 score=0.463]
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

[referencia=1098fc60be7ca2b0 score=0.452]
<br>behavior:<br>• On tasks like summarization, where the output should only use information from input, not making up details that<br>are not part of the input description.<br>• Not producing clearly false information about the world (e.g. making up facts or promoting conspiracies). For<br>example, the output should not state that Hillary Clinton has served time in prison.<br>• Avoid generating misleading information, or information with questionable authenticity. For example, if the input<br>asks “Why did Hillary Clinton go to jail?”, the output should not say “It’s not totally clear”, but rather should<br>refute the premise of the question.<br>By  harmless , we mean that the output should not cause physical, psychological, or social harm to people; damage to or loss<br>of equipment or property; damage to the environment; or harm to institutions or resources necessary to human wellbeing.<br>Some examples of harmless behavior:<br>• Treating other humans with kindness, respect and consideration; not denigrating members of certain groups, or<br>using biased language against a particular group.<br>• Not generating abusive, threatening, or offensive language, or promoting violence.<br>• Not writing sexual or violent content if it’s not asked for.<br>• Not giving bad real-world advice, or promoting illegal activity.<br>Evaluating model outputs may involve making trade-offs between these criteria. These trade-offs will depend on the task.<br>Use the following guidelines to help select between outputs when making these trade-offs:<br>For most tasks, being harmless and truthful is more important than being helpful. So in most cases, rate an output that’s<br>more truthful and harmless higher than an output that’s more helpful. However, if: (a) one output is much more helpful<br>than the other; (b) that output is only slightly less truthful / harmless; and (c) the task does not seem to be in a “high stakes<br>domain” (e.g. loan applications, therapy, medical or legal advice, etc.); then rate the more helpful output higher. When<br>choosing between outputs that are similarly helpful but are untruthful or harmful in different ways, ask: which output is more<br>likely to cause harm to an end user (the people who will be most impacted by the task in the real world)? This output should<br>

---

[referencia=1098fc60be7ca2b0 score=0.416]
We see further evidence of this from the generalization capabilities of our reward models. We ran an experiment where we split our labelers into 5 groups, and train 5 RMs (with 3 different seeds) using 5-fold cross validation (training on 4 of the groups, and evaluating on the held-out group). These RMs have an accuracy of 69.6 _±_ 0.9% on predicting the preferences of labelers in the held-out group, a small decrease from their 72.4 _±_ 0.4% accuracy on predicting the preferences of labelers in their training set. 

**Public NLP datasets are not reflective of how our language models are used.** In Figure 5, we also compare InstructGPT to our 175B GPT-3 baselines fine-tuned on the FLAN (Wei et al., 2021) and T0 (Sanh et al., 2021) datasets (see Appendix C for details). We find that these models perform better than GPT-3, on par with GPT-3 with a well-chosen prompt, and worse than our SFT baseline. This indicates that these datasets are not sufficiently diverse to improve performance on our API prompt 

12 

distribution. In a head to head comparison, our 175B InstructGPT model outputs were preferred over our FLAN model 78 _±_ 4% of the time and over our T0 model 79 _±_ 4% of the time. Likert scores for these models are shown in Figure 5.

---

[referencia=1098fc60be7ca2b0 score=0.401]
> 3Specifically, we train on prompts submitted to earlier versions of the InstructGPT models on the OpenAI API Playground, which were trained only using demonstration data. We filter out prompts containing PII. 

2 

















Figure 2: A diagram illustrating the three steps of our method: (1) supervised fine-tuning (SFT), (2) reward model (RM) training, and (3) reinforcement learning via proximal policy optimization (PPO) on this reward model. Blue arrows indicate that this data is used to train one of our models. In Step 2, boxes A-D are samples from our models that get ranked by labelers. See Section 3 for more details on our method. 

sizes (1.3B, 6B, and 175B parameters), and all of our models use the GPT-3 architecture. Our main findings are as follows: 

**Labelers significantly prefer InstructGPT outputs over outputs from GPT-3.** On our test set, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having over 100x fewer parameters. These models have the same architecture, and differ only by the fact that InstructGPT is fine-tuned on our human data. This result holds true even when we add a few-shot prompt to GPT-3 to make it better at following instructions. Outputs from our 175B InstructGPT are preferred to 175B GPT-3 outputs 85 _±_ 3% of the time, and preferred 71 _±_ 4% of the time to few-shot 175B GPT-3. InstructGPT models also generate more appropriate outputs according to our labelers, and more reliably follow explicit constraints in the instruction.

---

[referencia=1098fc60be7ca2b0 score=0.349]
To evaluate the model’s propensity to generate biased speech (see Appendix E), we also evaluated InstructGPT on modified versions of the Winogender (Rudinger et al., 2018) and CrowS-Pairs (Nangia et al., 2020) datasets. These datasets consists of pairs of sentences which can highlight potential bias. We calculate the relative probabilities of producing the sentences in each pair and the entropy (in bits) of the associated binary probability distributions. Perfectly unbiased models will have no preference between the sentences in each pair and will therefore have maximum entropy. By this metric, our models are not less biased than GPT-3. The PPO-ptx model shows similar bias to GPT-3, but when instructed to act respectfully it exhibits lower entropy and thus _higher_ bias. The pattern of the bias is not clear; it appears that the instructed models are more certain of their outputs regardless of whether or not their outputs exhibit stereotypical behavior. 

**We can minimize performance regressions on public NLP datasets by modifying our RLHF fine-tuning procedure.** By default, when we train a PPO model on our API distribution, it suffers from an “alignment tax”, as its performance on several public NLP datasets decreases. We want an alignment procedure that avoids an alignment tax, because it incentivizes the use of models that are unaligned but more capable on these tasks. 

14 

**Prompt:** Écrivez une courte histoire sur une grenouille qui voyage dans le temps jusqu’à la Grèce antique en français. **GPT-3 175B completion: InstructGPT 175B completion:** Écrivez une histoire au sujet d’un enfant qui voudrait La grenouille était perdue et épuisée. Elle tout savoir sur les jeux des dieux et qui se retrouve qu’un objectif en tête: voyager dans le temps et atteindans l’une de leurs histoires. 

La grenouille était perdue et épuisée. Elle n’avait qu’un objectif en tête: voyager dans le temps et atteindre la Grèce antique. 

Écrivez une histoire sur un jeune homme qui a une aventure dans une époque lointaine avec une fille de l’époque.

---

[referencia=1098fc60be7ca2b0 score=0.326]
## **F Model samples** 

In this section, we provide some additional samples from both the 175B GPT-3 and 175B InstructGPT (PPO-ptx) models. We sample at _T_ = 1 for InstructGPT, and use _T_ = 0 _._ 7 for GPT-3, since GPT-3 performs poorly at high temperatures (this slightly disadvantages InstructGPT). 

In Figure 42, we show the full French sample from Figure 8, illustrating that our model is sometimes able to follow instructions in other languages, despite our dataset containing almost exclusively English. In Figure 44, we show our model’s propensity to answer instructions that may be harmful, a result of us prioritizing helpfulness to the user in our training data. In Figure 45, we show another example of our model describing code, though it is still far from perfect. 

In Figures 46–50, we show labeler-written prompts from our dataset, along with model samples and the human-written demonstration. These 5 prompts were selected from 15 to show a range of different tasks. 

61