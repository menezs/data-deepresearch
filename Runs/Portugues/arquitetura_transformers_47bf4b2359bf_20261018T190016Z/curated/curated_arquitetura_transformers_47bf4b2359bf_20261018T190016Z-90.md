[referencia=29a0882390ee7063 score=0.371]
### **5 Limitations** 

Despite its capabilities, GPT-4 has similar limitations as earlier GPT models. Most importantly, it still is not fully reliable (it “hallucinates” facts and makes reasoning errors). Great care should be taken when using language model outputs, particularly in high-stakes contexts, with the exact protocol (such as human review, grounding with additional context, or avoiding high-stakes uses altogether) matching the needs of specific applications. See our System Card for details. 

GPT-4 significantly reduces hallucinations relative to previous GPT-3.5 models (which have themselves been improving with continued iteration). GPT-4 scores 19 percentage points higher than our latest GPT-3.5 on our internal, adversarially-designed factuality evaluations (Figure 6).

---

[referencia=29a0882390ee7063 score=0.301]
As we see above, both improved language model capabilities and limitations can pose challenges to the responsible and safe societal adoption of these models. To ensure that we are all well-prepared for the pace of progress, we need more research emphasis on areas such as AI literacy, economic and social resilience, and anticipatory governance.[11] It is very important that OpenAI, other labs, and academia further develop effective evaluation tools and technical improvements in model safety. Progress has been made in the last few years, and more investment in safety will likely produce more gains. 

We encourage readers interested in this topic to read our work on language model impacts in areas such as disinformation, misuse, education, and economy and labor market. 

69

---

[referencia=29a0882390ee7063 score=0.213]
### **2.2 Hallucinations** 

GPT-4 has the tendency to “hallucinate,”<sup>9</sup> i.e. “produce content that is nonsensical or untruthful in relation to certain sources.”[31, 32] This tendency can be particularly harmful as models become increasingly convincing and believable, leading to overreliance on them by users. [See further discussion in Overreliance]. Counterintuitively, hallucinations can become more dangerous as models become more truthful, as users build trust in the model when it provides truthful information in areas where they have some familiarity. Additionally, as these models are integrated into society and used to help automate various systems, this tendency to hallucinate is one of the factors that can lead to the degradation of overall information quality and further reduce veracity of and trust in freely available information.[33] 

We have measured GPT-4’s hallucination potential in both closed domain and open domain contexts<sup>10</sup> using a range of methods. We measured close domain hallucinations using automatic evaluations (using GPT-4 as a zero-shot classifier) and human evaluations. For open domain hallucinations, we collected real-world data that had been flagged as not being factual, reviewed it, and created a ’factual’ set for it where it was possible to do so.<sup>11</sup> We used this to assess model generations in relation to the ’factual’ set, and facilitate human evaluations. 

GPT-4 was trained to reduce the model’s tendency to hallucinate by leveraging data from prior models such as ChatGPT. On internal evaluations, GPT-4-launch scores 19 percentage points higher than our latest GPT-3.5 model at avoiding open-domain hallucinations, and 29 percentage points higher at avoiding closed-domain hallucinations. 

> 9 We use the term “hallucinations,” though we recognize ways this framing may suggest anthropomorphization, which in turn can lead to harms or incorrect mental models of how the model learns.

---

[referencia=29a0882390ee7063 score=0.186]
confidence in an answer generally matches the probability of being correct). However, after the post-training process, the calibration is reduced (Figure 8). 

GPT-4 has various biases in its outputs that we have taken efforts to correct but which will take some time to fully characterize and manage. We aim to make GPT-4 and other systems we build have reasonable default behaviors that reflect a wide swath of users’ values, allow those systems to be customized within some broad bounds, and get public input on what those bounds should be. See OpenAI [68] for more details.

---

[referencia=29a0882390ee7063 score=0.165]
# GPT-4 System Card 

### OpenAI 

##### **Abstract** 

Large language models (LLMs) are being deployed in many domains of our lives ranging from browsing, to voice assistants, to coding assistance tools, and have potential for vast societal impacts.[1, 2, 3, 4, 5, 6, 7] This system card analyzes GPT-4, the latest LLM in the GPT family of models.[8, 9, 10] First, we highlight safety challenges presented by the model’s limitations (e.g., producing convincing text that is subtly false) and capabilities (e.g., increased adeptness at providing illicit advice, performance in dual-use capabilities, and risky emergent behaviors). Second, we give a high-level overview of the safety processes OpenAI adopted to prepare GPT-4 for deployment. This spans our work across measurements, model-level changes, product- and system-level interventions (such as monitoring and policies), and external expert engagement. Finally, we demonstrate that while our mitigations and processes alter GPT-4’s behavior and prevent certain kinds of misuses, they are limited and remain brittle in some cases. This points to the need for anticipatory planning and governance.[11] 

**Content Warning:** This document contains content that some may disturbing or including content that is sexual, hateful, or violent in nature. 

41

---

[referencia=29a0882390ee7063 score=0.154]
## **1 Introduction** 

Large language models, also known as LLMs, have become an increasingly prevalent part of our day-to-day lives, with their use extending to a wide range of domains including web browsing, voice assistants, and coding assistance tools.[1, 2, 3, 4] These models have the potential to significantly impact society in numerous ways.[5, 6, 7] This system card analyzes GPT-4, the latest large language model in the GPT family of models.[8, 9, 10] Since it finished training in August of 2022, we have been evaluating, adversarially testing, and iteratively improving the model and the system-level mitigations around it. Our mitigations and processes alter GPT-4’s behavior and prevent certain kinds of misuses, though they have limitations, pointing to the need for anticipatory planning and governance[11] and further safety research. Our approach to deployment balances minimizing risk from deployment, enabling positive use cases, and learning from deployment. 

GPT models are often trained in two stages. First, they are trained, using a large dataset of text from the Internet, to predict the next word. The models are then fine-tuned with additional data, using an algorithm called reinforcement learning from human feedback (RLHF), to produce outputs that are preferred by human labelers.[10, 12, 13] Training language models on large text datasets has given rise to capabilities such as few-shot learning[10] and the ability to carry out a wide range of natural language tasks spanning different domains, including question answering, arithmetic, and classification. Fine-tuning has made these models more controllable and useful.

---

[referencia=29a0882390ee7063 score=0.119]
### **1 Introduction** 

This technical report presents GPT-4, a large multimodal model capable of processing image and text inputs and producing text outputs. Such models are an important area of study as they have the potential to be used in a wide range of applications, such as dialogue systems, text summarization, and machine translation. As such, they have been the subject of substantial interest and progress in recent years [1–34]. 

One of the main goals of developing such models is to improve their ability to understand and generate natural language text, particularly in more complex and nuanced scenarios. To test its capabilities in such scenarios, GPT-4 was evaluated on a variety of exams originally designed for humans. In these evaluations it performs quite well and often outscores the vast majority of human test takers. For example, on a simulated bar exam, GPT-4 achieves a score that falls in the top 10% of test takers. This contrasts with GPT-3.5, which scores in the bottom 10%. 

On a suite of traditional NLP benchmarks, GPT-4 outperforms both previous large language models and most state-of-the-art systems (which often have benchmark-specific training or hand-engineering). On the MMLU benchmark [35, 36], an English-language suite of multiple-choice questions covering 57 subjects, GPT-4 not only outperforms existing models by a considerable margin in English, but also demonstrates strong performance in other languages. On translated variants of MMLU, GPT-4 surpasses the English-language state-of-the-art in 24 of 26 languages considered. We discuss these model capability results, as well as model safety improvements and results, in more detail in later sections. 

This report also discusses a key challenge of the project, developing deep learning infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to make predictions about the expected performance of GPT-4 (based on small runs trained in similar ways) that were tested against the final run to increase confidence in our training. 

Despite its capabilities, GPT-4 has similar limitations to earlier GPT models [1, 37, 38]: it is not fully reliable (e.g. can suffer from “hallucinations”), has a limited context window, and does not learn

---

[referencia=29a0882390ee7063 score=0.069]
- [22] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever, “Language Models are Unsupervised Multitask Learners,” 2019. 

- [23] G. C. Bowker and S. L. Star, _Sorting Things Out_ . MIT Press, Aug. 2000. 

- [24] L. Weidinger, J. Uesato, M. Rauh, C. P.-S. Huang, J. Mellor, A. Glaese, M. Cheng, B. Balle, A. Kasirzadeh, C. Biles, S. Brown, Z. Kenton, W. Hawkins, T. Stepleton, A. Birhane, L. A. Hendricks, L. Rimell, W. Isaac, J. Haas, S. Legassick, G. Irving, and I. Gabriel, “Taxonomy of Risks posed by Language Models,” in _2022 ACM Conference on Fairness, Accountability, and Transparency_ , FAccT ’22, (New York, NY, USA), pp. 214–229, Association for Computing Machinery, June 2022. 

72

---

[referencia=29a0882390ee7063 score=0.066]
- [44] K. Webster, M. Recasens, V. Axelrod, and J. Baldridge, “Mind the GAP: A Balanced Corpus of Gendered Ambiguous Pronouns,” Oct. 2018. 

- [45] E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell, “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? ,” in _Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency_ , (Virtual Event Canada), pp. 610–623, ACM, Mar. 2021.

---

[referencia=29a0882390ee7063 score=0.062]
- [7] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. _arXiv preprint arXiv:1810.04805_ , 2018. 

- [8] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. _arXiv preprint arXiv:1910.10683_ , 2019. 

- [9] Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. _arXiv preprint arXiv:1804.04235_ , 2018. 

- [10] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E. Hinton. Layer normalization. _arXiv preprint arXiv:1607.06450_ , 2016. 

- [11] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Ed Chi, Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. _NeurIPS_ , 2022. 

- [12] Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Jiawei Han. Large language models can self-improve. _arXiv preprint arXiv:2210.11610_ , 2022. 

18

---

[referencia=29a0882390ee7063 score=0.057]
Red teamers noted that threat actors may from the model’s capability to critique and provide feedback on user-proposed acquisition strategies. Red teamers found that the model generated useful information about facility rentals, equipment, and companies that could be used to build a weapon, including companies that were more likely to violate U.S export restrictions. Threat actors may also benefit from combining GPT-4 with internet browsing and open-source tools, as highlighted in the section above on Interactions with other systems. 

> 15We focus here on unconventional weapons, but note that large language models like GPT-4 can also contribute to conventional weapons such as, for example, small arms. 

> 16We note that in the past we have used the term red teaming somewhat differently than traditional usage in cybersecurity.[26] Throughout this system card, we refer to the people performing stress testing, boundary testing, and red teaming as “red teamers” for simplicity and in order to use language consistent with that we used with our collaborators. 

> 17When referring to proliferation, the System Card uses the definition offered by the North Atlantic Treaty Organization. “WMD proliferation refers to attempts by state or non-state actors to develop, acquire, manufacture, possess, transport or transfer nuclear, radiological, chemical or biological weapons or devices and their means of delivery or related material, including precursors, without prejudice to the rights and obligations of the States Parties to the following agreements: the Treaty on the Non-Proliferation of Nuclear Weapons or Non-Proliferation Treaty (NPT); the Convention on the Prohibition of the Development, Production, Stockpiling and Use of Chemical Weapons and on their Destruction (CWC) and the Convention on the Prohibition of the Development, Production and Stockpiling of Bacteriological (Biological) and Toxin Weapons and on their Destruction (BWC)”.[58] 

52 

The model still possesses capability weaknesses in this domain. Generations were often too vague to be usable, generated impractical solutions, or were prone to making factual errors that could sabotage or otherwise delay a threat actor.<sup>18</sup> Also, longer responses were more likely to contain inaccuracies. For example, the model was more likely to generate a vague or inaccurate response when the red teamer asked for multi-step instructions for the engineering of a radiological device or biochemical compound. Inaccurate generations often appeared persuasive but ultimately contained the same problems outlined in the section on Hallucinations.

---

[referencia=29a0882390ee7063 score=0.051]
## **2 GPT-4 Observed Safety Challenges** 

GPT-4 demonstrates increased performance in areas such as reasoning, knowledge retention, and coding, compared to earlier models such as GPT-2[22] and GPT-3.[10] Many of these improvements also present new safety challenges, which we highlight in this section. 

We conducted a range of qualitative and quantitative evaluations of GPT-4. These evaluations helped us gain an understanding of GPT-4’s capabilities, limitations, and risks; prioritize our mitigation efforts; and iteratively test and build safer versions of the model. Some of the specific risks we explored are:<sup>6</sup> 

- Hallucinations 

- Harmful content 

- Harms of representation, allocation, and quality of service 

- Disinformation and operations 

- Proliferation of conventional and unconventional weapons 

- Privacy 

- Cybersecurity 

- Potential for risky emergent behaviors 

- Interactions with other systems 

- Economic impacts 

- Acceleration 

- Overreliance 

We found that GPT-4-early and GPT-4-launch exhibit many of the same limitations as earlier language models, such as producing biased and unreliable content. Prior to our mitigations being put in place, we also found that GPT-4-early presented increased risks in areas such as finding websites selling illegal goods or services, and planning attacks. Additionally, the increased coherence of the model enables it to generate content that may be more believable and more persuasive. We elaborate on our evaluation procedure and findings below.

---

[referencia=29a0882390ee7063 score=0.044]
- [28] D. Ganguli, L. Lovitt, J. Kernion, A. Askell, Y. Bai, S. Kadavath, B. Mann, E. Perez, N. Schiefer, K. Ndousse, A. Jones, S. Bowman, A. Chen, T. Conerly, N. DasSarma, D. Drain, N. Elhage, S. El-Showk, S. Fort, Z. Hatfield-Dodds, T. Henighan, D. Hernandez, T. Hume, J. Jacobson, S. Johnston, S. Kravec, C. Olsson, S. Ringer, E. Tran-Johnson, D. Amodei, T. Brown, N. Joseph, S. McCandlish, C. Olah, J. Kaplan, and J. Clark, “Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned,” Nov. 2022. 

- [29] E. Perez, S. Huang, F. Song, T. Cai, R. Ring, J. Aslanides, A. Glaese, N. McAleese, and G. Irving, “Red Teaming Language Models with Language Models,” Feb. 2022. 

- [30] H. Khlaaf, P. Mishkin, J. Achiam, G. Krueger, and M. Brundage, “A Hazard Analysis Framework for Code Synthesis Large Language Models,” July 2022. 

- [31] J. Maynez, S. Narayan, B. Bohnet, and R. McDonald, “On Faithfulness and Factuality in Abstractive Summarization,” May 2020. 

- [32] S. Lin, J. Hilton, and O. Evans, “TruthfulQA: Measuring How Models Mimic Human Falsehoods,” May 2022. 

- [33] J. A. Goldstein, G. Sastry, M. Musser, R. DiResta, M. Gentzel, and K. Sedova, “Forecasting potential misuses of language models for disinformation campaigns and how to reduce risk.” https://openai.com/research/forecasting-misuse, Jan. 2023.

---

[referencia=29a0882390ee7063 score=0.038]
Figure 3: Example prompts that led to biased content in GPT-4-early. These examples demonstrates how GPT-4-launch and our mitigations still have important limitations: assuming offensiveness can itself be offensive, and caveats can be insufficient for discouraging unsafe use.

---

[referencia=29a0882390ee7063 score=0.036]
- [1] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D. Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in Neural Information Processing Systems_ , 33:1877–1901, 2020. 

- [2] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. _arXiv preprint arXiv:2203.15556_ , 2022. 

- [3] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. PaLM: Scaling language modeling with pathways. _arXiv preprint arXiv:2204.02311_ , 2022. 

- [4] Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song, John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language models: Methods, analysis & insights from training gopher. _arXiv preprint arXiv:2112.11446_ , 2021. 

- [5] Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, and Ruslan Salakhutdinov. Transformer-XL: Attentive language models beyond a fixed-length context. _arXiv preprint arXiv:1901.02860_ , 2019. 

- [6] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. RoBERTa: A robustly optimized BERT pretraining approach. _arXiv preprint arXiv:1907.11692_ , 2019.

---

[referencia=29a0882390ee7063 score=0.034]
Our existing mitigations across all of these axes include documentation and hedging language within the model. However, mitigating overreliance requires multiple defenses, and especially depends on downstream interventions by developers. We recommend that developers using our tools provide end users with detailed documentation on their systems’ capabilities and limitations, as well as guidance on how to get the best performance from the system. To prevent dependency, we urge developers to be cautious in how they refer to the model/system, and to generally avoid misleading claims or implications—including that it is human—and to consider the potential impact of changes to the model’s style, tone, or perceived personality on users. We also suggest that developers communicate to users the importance of critically evaluating model outputs. 

At the model-level we’ve also made changes to address the risks of both overreliance and underreliance. Weve found that GPT-4 exhibits enhanced steerability which allows it to better infer users intentions without extensive prompt tuning. 

To tackle overreliance, we’ve the model’s refusal behavior, making it more stringent in rejecting requests that go against our content policy, while being more open to requests it can safely fulfill. One objective here is to discourage users from disregarding the model’s refusals. 

However, it’s worth noting that GPT-4 still displays a tendency to hedge in its responses. Some of our early studies suggest that this epistemic humility may inadvertently foster overreliance, as users develop trust in the model’s cautious approach. It’s crucial to recognize that the model isn’t always accurate in admitting its limitations, as evidenced by its tendency to hallucinate. Additionally, users might grow less attentive to the model’s hedging and refusal cues over time, further complicating the issue of overreliance. 

60

---

[referencia=29a0882390ee7063 score=0.032]
- [58] NATO, “Arms control, disarmament and non-proliferation in nato,” February 27 2023. accessed 2023-02-27. 

- [59] N. Carlini, F. Tramer, E. Wallace, M. Jagielski, A. Herbert-Voss, K. Lee, A. Roberts, T. Brown, D. Song, U. Erlingsson, A. Oprea, and C. Raffel, “Extracting Training Data from Large Language Models,” June 2021. 

- [60] N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and C. Zhang, “Quantifying Memorization Across Neural Language Models,” Mar. 2023. 

- [61] D. Ganguli, D. Hernandez, L. Lovitt, N. DasSarma, T. Henighan, A. Jones, N. Joseph, J. Kernion, B. Mann, A. Askell, Y. Bai, A. Chen, T. Conerly, D. Drain, N. Elhage, S. E. Showk, S. Fort, Z. Hatfield-Dodds, S. Johnston, S. Kravec, N. Nanda, K. Ndousse, C. Olsson, D. Amodei, D. Amodei, T. Brown, J. Kaplan, S. McCandlish, C. Olah, and J. Clark, “Predictability and Surprise in Large Generative Models,” in _2022 ACM Conference on Fairness, Accountability, and Transparency_ , pp. 1747–1764, June 2022. 

- [62] J. Wei, Y. Tay, R. Bommasani, C. B. Zoph, S. Borgeaud, D. Yogatama, M. Bosma, D. Zhou, D. Metzler, E. H. Chi, T. Hashimoto, O. Vinyals, P. Liang, J. Dean, and W. Fedus, “Emergent Abilities of Large Language Models,” Oct. 2022. 

- [63] R. Ngo, L. Chan, and S. Mindermann, “The alignment problem from a deep learning perspective,” Feb. 2023.

---

[referencia=29a0882390ee7063 score=0.029]
- [1] A. Tamkin, M. Brundage, J. Clark, and D. Ganguli, “Understanding the Capabilities, Limitations, and Societal Impact of Large Language Models,” Feb. 2021. 

- [2] “Introducing the new Bing.” https://www.bing.com/new. 

- [3] J. Hilton, R. Nakano, S. Balaji, and J. Schulman, “WebGPT: Improving the factual accuracy of language models through web browsing.” https://openai.com/research/webgpt, Dec. 2021. 

- [4] “ACT-1: Transformer for Actions – Adept.” https://www.adept.ai/blog/act-1. 

- [5] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri, G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan, S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, C. Winter, P. Tillet, F. P. Such, D. Cummings, M. Plappert, F. Chantzis, E. Barnes, A. Herbert-Voss, W. H. Guss, A. Nichol, A. Paino, N. Tezak, J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Radford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, B. McGrew, D. Amodei, S. McCandlish, I. Sutskever, and W. Zaremba, “Evaluating Large Language Models Trained on Code,” July 2021.

---

[referencia=29a0882390ee7063 score=0.028]
For closed-domain hallucinations, we are able to use GPT-4 itself to generate synthetic data. Specifically, we design a multi-step process to generate comparison data: 

1. Pass a prompt through GPT-4 model and get a response 

2. Pass prompt + response through GPT-4 with an instruction to list all hallucinations 

   - (a) If no hallucinations are found, continue 

3. Pass prompt + response + hallucinations through GPT-4 with an instruction to rewrite the response without hallucinations 

4. Pass prompt + new response through GPT-4 with an instruction to list all hallucinations 

   - (a) If none are found, keep (original response, new response) comparison pair (b) Otherwise, repeat up to 5x 

This process produces comparisons between (original response with hallucinations, new response without hallucinations according to GPT-4), which we also mix into our RM dataset. 

We that our mitigations on hallucinations improve performance on factuality as measured by evaluations such as TruthfulQA[34] and increase accuracy to around 60% as compared to 30% for an earlier version. 

> risk of neural toxic degeneration in models.[102] 

> 30We collected 5,214 user prompts sent to us through ChatGPT and the OpenAI API, sampled one response from each model, and sent these prompts and responses to human labelers. The labelers were instructed to judge whether the response is what the user would have wanted given the prompt. The labelers were not told which response was generated by which model and the order in which the responses were presented was randomised. We filter out prompts containing personally identifiable information (PII). 

64 



<!-- Start of picture text -->
Accuracy on adversarial questions (TruthfulQA mc1)<br>Accuracy<br>70%<br>Anthropic-LM<br>gpt-3.5<br>gpt-4<br>60%<br>50%<br>40%<br>30%<br>20%<br>10%<br>0%<br>Askell et al. Askell et al. gpt-3.5-base gpt-3.5-base gpt-3.5-turbo gpt-4-base gpt-4-base gpt-4<br>2022 2022<br>Model<br><!-- End of picture text -->

---

[referencia=29a0882390ee7063 score=0.027]
### **2.5 Disinformation and Operations** 

GPT-4 can generate plausibly realistic and targeted content, including news articles, tweets, dialogue, and emails. In Harmful content, we discussed how similar capabilities could be misused to exploit individuals. Here, we discuss the general concern around disinformation and influence operations.<sup>14</sup> Based on our general capability evaluations, we expect GPT-4 to be better than GPT-3 at producing realistic, targeted content. As such, there is risk of GPT-4 being used for generating content that is intended to mislead.[50] 

Empirical evidence suggests that earlier language models could also be useful for generating content that is misleading, but persuasive.[51] For example, researchers found that GPT-3 was capable of tasks relevant to changing the narrative on a topic.[52] Persuasive appeals written by language models such as GPT-3 on politically charged issues were also found to be nearly as effective as human-written appeals.[53, 54] Based on GPT-4’s performance at related language tasks, we expect it to be better than GPT-3 at these sorts of tasks, which increases the risk that bad actors could use GPT-4 to create misleading content and that society’s future epistemic views could be partially shaped by persuasive LLMs. 

Our red teaming results suggest that GPT-4 can rival human propagandists in many domains, especially if teamed with a human editor. Still, in areas where reliability is important, hallucinations can reduce GPT-4’s effectiveness for propagandists. Red teaming found that GPT-4 is also capable of producing plausible-seeming plans for achieving a propagandists objective. For example, when asked 

> 14We focus here on disinformation (which is intended to mislead), not on misinformation (which is not), and for this reason emphasize adversarial testing vs. general testing in this section. We touch briefly on misinformation and the reinforcement of truths and untruths in the section on Representation, allocation, and quality of service. 

50 



<!-- Start of picture text -->