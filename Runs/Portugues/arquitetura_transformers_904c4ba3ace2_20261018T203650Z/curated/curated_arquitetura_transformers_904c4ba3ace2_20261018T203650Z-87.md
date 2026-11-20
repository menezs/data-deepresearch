[referencia=1098fc60be7ca2b0 score=0.136]
## **2 Related work** 

**Research on alignment and learning from human feedback.** We build on previous techniques to align models with human intentions, particularly reinforcement learning from human feedback (RLHF). Originally developed for training simple robots in simulated environments and Atari games (Christiano et al., 2017; Ibarz et al., 2018), it has recently been applied to fine-tuning language models to summarize text (Ziegler et al., 2019; Stiennon et al., 2020; Böhm et al., 2019; Wu et al., 2021). This work is in turn influenced by similar work using human feedback as a reward in domains such as dialogue (Jaques et al., 2019; Yi et al., 2019; Hancock et al., 2019), translation (Kreutzer et al., 2018; Bahdanau et al., 2016), semantic parsing (Lawrence and Riezler, 2018), story generation (Zhou and Xu, 2020), review generation (Cho et al., 2018), and evidence extraction (Perez et al., 2019). Madaan et al. (2022) use written human feedback to augment prompts and improve the performance of GPT-3. There has also been work on aligning agents in text-based environments using RL with 

4 

a normative prior (Nahian et al., 2021). Our work can be seen as a direct application of RLHF to aligning language models on a broad distribution of language tasks. 

The question of what it means for language models to be aligned has also received attention recently (Gabriel, 2020). Kenton et al. (2021) catalog behavioral issues in LMs that result from misalignment, including producing harmful content and gaming misspecified objectives. In concurrent work, Askell et al. (2021) propose language assistants as a testbed for alignment research, study some simple baselines, and their scaling properties.

---

[referencia=1098fc60be7ca2b0 score=0.027]
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

[referencia=1098fc60be7ca2b0 score=0.026]
> 10Note that while fine-tuning models using human data is common practice when deploying ML systems, the purpose of these efforts is to obtain a model that performs well on a company’s specific use case, rather than advancing the alignment of general-purpose ML models. 

18 

### **5.3 Limitations** 

**Methodology.** The behavior of our InstructGPT models is determined in part by the human feedback obtained from our contractors. Some of the labeling tasks rely on value judgments that may be impacted by the identity of our contractors, their beliefs, cultural backgrounds, and personal history. We hired about 40 contractors, guided by their performance on a screening test meant to judge how well they could identify and respond to sensitive prompts, and their agreement rate with researchers on a labeling task with detailed instructions (see Appendix B). We kept our team of contractors small because this facilitates high-bandwidth communication with a smaller set of contractors who are doing the task full-time. However, this group is clearly not representative of the full spectrum of people who will use and be affected by our deployed models. As a simple example, our labelers are primarily English-speaking and our data consists almost entirely of English instructions. 

There are also many ways in which we could improve our data collection set-up. For instance, most comparisons are only labeled by 1 contractor for cost reasons. Having examples labeled multiple times could help identify areas where our contractors disagree, and thus where a single model is unlikely to align to all of them. In cases of disagreement, aligning to the average labeler preference may not be desirable. For example, when generating text that disproportionately affects a minority group, we may want the preferences of labelers belonging to that group to be weighted more heavily. 

**Models.** Our models are neither fully aligned nor fully safe; they still generate toxic or biased outputs, make up facts, and generate sexual and violent content without explicit prompting. They can also fail to generate reasonable outputs on some inputs; we show some examples of this in Figure 9. 

Perhaps the greatest limitation of our models is that, in most cases, they follow the user’s instruction, even if that could lead to harm in the real world. For example, when given a prompt instructing the models to be maximally biased, InstructGPT generates more toxic outputs than equivalently-sized GPT-3 models. We discuss potential mitigations in the following sections.

---

[referencia=1098fc60be7ca2b0 score=0.017]
- Nadeem, M., Bethke, A., and Reddy, S. (2020). Stereoset: Measuring stereotypical bias in pretrained language models. _arXiv preprint arXiv:2004.09456_ . 

- Nahian, M. S. A., Frazier, S., Harrison, B., and Riedl, M. (2021). Training value-aligned reinforcement learning agents using a normative prior. _arXiv preprint arXiv:2104.09469_ . 

- Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hesse, C., Jain, S., Kosaraju, V., Saunders, W., et al. (2021). Webgpt: Browser-assisted question-answering with human feedback. _arXiv preprint arXiv:2112.09332_ . 

- Nallapati, R., Zhou, B., Gulcehre, C., Xiang, B., et al. (2016). Abstractive text summarization using sequence-to-sequence rnns and beyond. _arXiv preprint arXiv:1602.06023_ . 

- Nangia, N., Vania, C., Bhalerao, R., and Bowman, S. R. (2020). CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models. In _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing_ , Online. Association for Computational Linguistics. 

- Ngo, H., Raterink, C., Araújo, J. G., Zhang, I., Chen, C., Morisot, A., and Frosst, N. (2021). Mitigating harm in language models with conditional-likelihood filtration. _arXiv preprint arXiv:2108.07790_ . 

- Perez, E., Karamcheti, S., Fergus, R., Weston, J., Kiela, D., and Cho, K. (2019). Finding generalizable evidence by learning to convince q&a models. _arXiv preprint arXiv:1909.05863_ .

---

[referencia=1098fc60be7ca2b0 score=0.012]
- Solaiman, I., Brundage, M., Clark, J., Askell, A., Herbert-Voss, A., Wu, J., Radford, A., Krueger, G., Kim, J. W., Kreps, S., et al. (2019). Release strategies and the social impacts of language models. _arXiv preprint arXiv:1908.09203_ . 

- Solaiman, I. and Dennison, C. (2021). Process for adapting language models to society (palms) with values-targeted datasets. _arXiv preprint arXiv:2106.10328_ . 

- Stiennon, N., Ouyang, L., Wu, J., Ziegler, D. M., Lowe, R., Voss, C., Radford, A., Amodei, D., and Christiano, P. (2020). Learning to summarize from human feedback. _arXiv preprint arXiv:2009.01325_ . 

- Tamkin, A., Brundage, M., Clark, J., and Ganguli, D. (2021). Understanding the capabilities, limitations, and societal impact of large language models. _arXiv preprint arXiv:2102.02503_ . 

- Thoppilan, R., De Freitas, D., Hall, J., Shazeer, N., Kulshreshtha, A., Cheng, H.-T., Jin, A., Bos, T., Baker, L., Du, Y., et al. (2022). Lamda: Language models for dialog applications. _arXiv preprint arXiv:2201.08239_ . 

- Vig, J., Gehrmann, S., Belinkov, Y., Qian, S., Nevo, D., Singer, Y., and Shieber, S. M. (2020). Investigating gender bias in language models using causal mediation analysis. In _NeurIPS_ . 

- Völske, M., Potthast, M., Syed, S., and Stein, B. (2017). Tl; dr: Mining reddit to learn automatic summarization. In _Proceedings of the Workshop on New Frontiers in Summarization_ , pages 59–63.

---

[referencia=1098fc60be7ca2b0 score=0.012]
## **4 Results** 

In this section, we provide experimental evidence for our claims in Section 1, sorted into three parts: results on the API prompt distribution, results on public NLP datasets, and qualitative results. 

> 7Accessible here: `https://github.com/openai/following-instructions-human-feedback` . 

10 



<!-- Start of picture text -->
GPT distribution Instruct distribution<br>0.75<br>0.50<br>0.25<br>0.75<br>0.50<br>0.25<br>1.3B 6B 175B 1.3B 6B 175B<br>Model size<br>GPT<br>GPT SFT PPO PPO-ptx<br>(prompted)<br>Heldout workers<br>Win rate against SFT 175B<br>Training workers<br><!-- End of picture text -->

Figure 3: Preference results of our models, measured by winrate against the 175B SFT model. Left: results on prompts submitted to GPT models on the API; Right: results on prompts submitted to InstructGPT models on the API; Top: results from held-out labelers; Bottom: results from training labelers. We omit GPT (prompted) from the evals on prompts submitted to GPT-3 models (left) as these prompts are already designed to perform well for GPT-3, as opposed to prompts submitted to InstructGPT models (right).

---

[referencia=1098fc60be7ca2b0 score=0.012]
We focus on _fine-tuning_ approaches to aligning language models. Specifically, we use reinforcement learning from human feedback (RLHF; Christiano et al., 2017; Stiennon et al., 2020) to fine-tune GPT-3 to follow a broad class of written instructions (see Figure 2). This technique uses human preferences as a reward signal to fine-tune our models. We first hire a team of 40 contractors to label our data, based on their performance on a screening test (see Section 3.4 and Appendix B.1 for more details). We then collect a dataset of human-written demonstrations of the desired output behavior on (mostly English) prompts submitted to the OpenAI API<sup>3</sup> and some labeler-written prompts, and use this to train our supervised learning baselines. Next, we collect a dataset of human-labeled comparisons between outputs from our models on a larger set of API prompts. We then train a reward model (RM) on this dataset to predict which model output our labelers would prefer. Finally, we use this RM as a reward function and fine-tune our supervised learning baseline to maximize this reward using the PPO algorithm (Schulman et al., 2017). We illustrate this process in Figure 2. This procedure aligns the behavior of GPT-3 to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of “human values”; we discuss this further in Section 5.2. We call the resulting models _InstructGPT_ . 

We mainly evaluate our models by having our labelers rate the quality of model outputs on our test set, consisting of prompts from held-out customers (who are not represented in the training data). We also conduct automatic evaluations on a range of public NLP datasets. We train three model 

> 3Specifically, we train on prompts submitted to earlier versions of the InstructGPT models on the OpenAI API Playground, which were trained only using demonstration data. We filter out prompts containing PII. 

2

---

[referencia=1098fc60be7ca2b0 score=0.008]
- Kenton, Z., Everitt, T., Weidinger, L., Gabriel, I., Mikulik, V., and Irving, G. (2021). Alignment of language agents. _arXiv preprint arXiv:2103.14659_ . 

- Keskar, N. S., McCann, B., Varshney, L. R., Xiong, C., and Socher, R. (2019). Ctrl: A conditional transformer language model for controllable generation. _arXiv preprint arXiv:1909.05858_ . 

- Khashabi, D., Min, S., Khot, T., Sabharwal, A., Tafjord, O., Clark, P., and Hajishirzi, H. (2020). Unifiedqa: Crossing format boundaries with a single qa system. _arXiv preprint arXiv:2005.00700_ . 

- Kirk, H., Jun, Y., Iqbal, H., Benussi, E., Volpin, F., Dreyer, F. A., Shtedritski, A., and Asano, Y. M. (2021). How true is gpt-2? an empirical analysis of intersectional occupational biases. _arXiv preprint arXiv:2102.04130_ . 

- Krause, B., Gotmare, A. D., McCann, B., Keskar, N. S., Joty, S., Socher, R., and Rajani, N. F. (2020). Gedi: Generative discriminator guided sequence generation. _arXiv preprint arXiv:2009.06367_ . 

- Kreutzer, J., Khadivi, S., Matusov, E., and Riezler, S. (2018). Can neural machine translation be improved with user feedback? _arXiv preprint arXiv:1804.05958_ . 

- Lawrence, C. and Riezler, S. (2018). Improving a neural semantic parser by counterfactual learning from human bandit feedback. _arXiv preprint arXiv:1805.01252_ .

---

[referencia=1098fc60be7ca2b0 score=0.008]
### **5.1 Implications for alignment research** 

This research is part of our broader research program to align AI systems with human intentions (Christiano et al., 2017; Ziegler et al., 2019; Stiennon et al., 2020). Even though this work focuses on our current language model systems, we seek general and scalable methods that work for future AI systems (Leike et al., 2018). The systems we work with here are still fairly limited, but they are among the largest language models today and we apply them on a wide range of language tasks, including classification, summarization, question-answering, creative writing, dialogue, and others. 

Our approach to alignment research in this work is iterative: we are improving the alignment of current AI systems instead of focusing abstractly on aligning AI systems that don’t yet exist. A disadvantage of this approach is that we are not directly facing alignment problems that occur only when aligning superhuman systems (Bostrom, 2014). However, our approach does provides us with a clear empirical feedback loop of what works and what does not. We believe that this feedback loop is essential to refine our alignment techniques, and it forces us to keep pace with progress in machine learning. Moreover, the alignment technique we use here, RLHF, is an important building block in several proposals to align superhuman systems (Leike et al., 2018; Irving et al., 2018; Christiano et al., 2018). For example, RLHF was a central method in recent work on summarizing books, a task that exhibits some of the difficulties of aligning superhuman AI systems as it is difficult for humans to evaluate directly (Wu et al., 2021). 

From this work, we can draw lessons for alignment research more generally:

---

[referencia=1098fc60be7ca2b0 score=0.007]
- Lawrence, C. and Riezler, S. (2018). Improving a neural semantic parser by counterfactual learning from human bandit feedback. _arXiv preprint arXiv:1805.01252_ . 

- Leike, J., Krueger, D., Everitt, T., Martic, M., Maini, V., and Legg, S. (2018). Scalable agent alignment via reward modeling: a research direction. _arXiv preprint arXiv:1811.07871_ . 

- Leike, J., Martic, M., Krakovna, V., Ortega, P. A., Everitt, T., Lefrancq, A., Orseau, L., and Legg, S. (2017). AI safety gridworlds. _arXiv preprint arXiv:1711.09883_ . 

- Liang, P. P., Wu, C., Morency, L.-P., and Salakhutdinov, R. (2021). Towards understanding and mitigating social biases in language models. In _International Conference on Machine Learning_ , pages 6565–6576. PMLR. 

- Lin, S., Hilton, J., and Evans, O. (2021). Truthfulqa: Measuring how models mimic human falsehoods. _arXiv preprint arXiv:2109.07958_ . 

- Liu, H., Dacon, J., Fan, W., Liu, H., Liu, Z., and Tang, J. (2019). Does gender matter? towards fairness in dialogue systems. _arXiv preprint arXiv:1910.10486_ . 

- Madaan, A., Tandon, N., Clark, P., and Yang, Y. (2022). Memory-assisted prompt editing to improve gpt-3 after deployment. _arXiv preprint arXiv:2201.06009_ . 

- Manela, D. d. V., Errington, D., Fisher, T., van Breugel, B., and Minervini, P. (2021). Stereotype and skew: Quantifying gender bias in pre-trained and fine-tuned language models. _arXiv preprint arXiv:2101.09688_ .

---

[referencia=1098fc60be7ca2b0 score=0.005]
19 

Comparisons are also not necessarily the most efficient way of providing an alignment signal. For example, we could have labelers edit model responses to make them better, or generate critiques of model responses in natural language. There is also a vast space of options for designing interfaces for labelers to provide feedback to language models; this is an interesting human-computer interaction problem. 

Our proposal for mitigating the alignment tax, by incorporating pretraining data into RLHF finetuning, does not completely mitigate performance regressions, and may make certain undesirable behaviors more likely for some tasks (if these behaviors are present in the pretraining data). This is an interesting area for further research. Another modification that would likely improve our method is to filter the pretraining mix data for toxic content (Ngo et al., 2021), or augment this data with synthetic instructions. 

As discussed in detail in Gabriel (2020), there are subtle differences between aligning to instructions, intentions, revealed preferences, ideal preferences, interests, and values. Gabriel (2020) advocate for a principle-based approach to alignment: in other words, for identifying “fair principles for alignment that receive reflective endorsement despite widespread variation in people’s moral beliefs.” In our paper we align to the inferred user intention for simplicity, but more research is required in this area. Indeed, one of the biggest open questions is how to design an alignment process that is transparent, that meaningfully represents the people impacted by the technology, and that synthesizes peoples’ values in a way that achieves broad consensus amongst many groups. We discuss some related considerations in Section 5.2.

---

[referencia=1098fc60be7ca2b0 score=0.004]
17 



<!-- Start of picture text -->
the real world with customers. 10 This enables an important feedback loop on the techniques’<br>effectiveness and limitations.<br>5.2 Who are we aligning to?<br>When aligning language models with human intentions, their end behavior is a function of the<br>underlying model (and its training data), the fine-tuning data, and the alignment method used. In this<br>section, we describe a number of factors that influence the fine-tuning data specifically, to ultimately<br>determine what and who we’re aligning to. We then consider areas for improvement before a larger<br>discussion of the limitations of our work in Section 5.3.<br>The literature often frames alignment using such terms as “human preferences” or “human values.”<br>In this work, we have aligned to a set of labelers’ preferences that were influenced, among others<br>things, by the instructions they were given, the context in which they received them (as a paid job),<br>and who they received them from. Some crucial caveats apply:<br>First, we are aligning to demonstrations and preferences provided by our training labelers, who<br>directly produce the data that we use to fine-tune our models. We describe our labeler hiring process<br>and demographics in Appendix B; in general, they are mostly English-speaking people living in the<br>United States or Southeast Asia hired via Upwork or Scale AI. They disagree with each other on<br>many examples; we found the inter-labeler agreement to be about 73%.<br><!-- End of picture text -->

Second, we are aligning to our preferences, as the researchers designing this study (and thus by proxy to our broader research organization, OpenAI): we write the labeling instructions that labelers use as a guide when writing demonstrations and choosing their preferred output, and we answer their questions about edge cases in a shared chat room. More study is needed on the exact effect of 

different instruction sets and interface designs on the data collected from labelers and its ultimate effect on model behavior.

---

[referencia=1098fc60be7ca2b0 score=0.002]
## **1 Introduction** 

Large language models (LMs) can be “prompted” to perform a range of natural language processing (NLP) tasks, given some examples of the task as input. However, these models often express unintended behaviors such as making up facts, generating biased or toxic text, or simply not following user instructions (Bender et al., 2021; Bommasani et al., 2021; Kenton et al., 2021; Weidinger et al., 2021; Tamkin et al., 2021; Gehman et al., 2020). This is because the language modeling objective 

> _∗_ Primary authors. This was a joint project of the OpenAI Alignment team. RL and JL are the team leads. Corresponding author: `lowe@openai.com` . 

> _†_ Work done while at OpenAI. Current affiliations: AA: Anthropic; PC: Alignment Research Center. 



<!-- Start of picture text -->
0.6<br>Model<br>PPO-ptx<br>PPO<br>0.4<br>SFT<br>GPT (prompted)<br>GPT<br>0.2<br>1.3B 6B 175B<br>Model size<br>Win rate against SFT 175B<br><!-- End of picture text -->

Figure 1: Human evaluations of various models on our API prompt distribution, evaluated by how often outputs from each model were preferred to those from the 175B SFT model. Our InstructGPT models (PPO-ptx) as well as its variant trained without pretraining mix (PPO) significantly outperform the GPT-3 baselines (GPT, GPT prompted); outputs from our 1.3B PPO-ptx model are preferred to those from the 175B GPT-3. Error bars throughout the paper are 95% confidence intervals.

---

[referencia=1098fc60be7ca2b0 score=0.002]
- Bojar, O., Chatterjee, R., Federmann, C., Haddow, B., Huck, M., Hokamp, C., Koehn, P., Logacheva, V., Monz, C., Negri, M., Post, M., Scarton, C., Specia, L., and Turchi, M. (2015). Findings of the 2015 workshop on statistical machine translation. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 1–46, Lisbon, Portugal. Association for Computational Linguistics. 

- Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. (2021). On the opportunities and risks of foundation models. _arXiv preprint arXiv:2108.07258_ . 

- Bostrom, N. (2014). _Superintelligence_ . Dunod. 

- Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. _arXiv preprint arXiv:2005.14165_ . 

- Buchanan, B., Lohn, A., Musser, M., and Sedova, K. (2021). Truth, lies, and automation. Technical report, Center for the Study of Emerging Technology. 

- Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. _Science_ , 356(6334):183–186. 

- Carlini, N., Tramer, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, U., et al. (2021). Extracting training data from large language models. In _30th USENIX Security Symposium (USENIX Security 21)_ , pages 2633–2650.

---

[referencia=1098fc60be7ca2b0 score=0.001]
different instruction sets and interface designs on the data collected from labelers and its ultimate effect on model behavior. 

Third, our training data is determined by prompts sent by OpenAI customers to models on the OpenAI API Playground, and thus we are implicitly aligning to what customers think is valuable and, in some cases, what their end-users think is valuable to currently use the API for. Customers and their end users may disagree or customers may not be optimizing for end users’ well-being; for example, a customer may want a model that maximizes the amount of time a user spends on their platform, which is not necessarily what end-users want. In practice, our labelers don’t have visibility into the contexts in which a given prompt or completion will be seen. 

Fourth, OpenAI’s customers are not representative of all potential or current users of language 

models—let alone of all individuals and groups impacted by language model use. For most of the duration of this project, users of the OpenAI API were selected off of a waitlist. The initial seeds for this waitlist were OpenAI employees, biasing the ultimate group toward our own networks. Stepping back, there are many difficulties in designing an alignment process that is fair, transparent, and has suitable accountability mechanisms in place. The goal of this paper is to demonstrate that 

this alignment technique can align to an specific human reference group for a specific application. 

We are not claiming that researchers, the labelers we hired, or our API customers are the right source of preferences. There are many stakeholders to consider—the organization training the model, the customers using the model to develop products, the end users of these products, and the broader population who may be directly or indirectly affected. It is not only a matter of making the alignment process more participatory; it is impossible that one can train a system that is aligned to everyone’s preferences at once, or where everyone would endorse the tradeoffs. 

One path forward could be to train models that can be conditioned on the preferences of certain groups, or that can be easily fine-tuned or prompted to represent different groups. Different models can then be deployed and used by groups who endorse different values. However, these models might still end up affecting broader society and there are a lot of difficult decisions to be made relating to whose preferences to condition on, and how to ensure that all groups can be represented and can opt out of processes that may be harmful.

---

[referencia=1098fc60be7ca2b0 score=0.001]
- Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. d. O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., et al. (2021). Evaluating large language models trained on code. _arXiv preprint arXiv:2107.03374_ . 

- Cho, W. S., Zhang, P., Zhang, Y., Li, X., Galley, M., Brockett, C., Wang, M., and Gao, J. (2018). Towards coherent and cohesive long-form text generation. _arXiv preprint arXiv:1811.00511_ . 

- Choi, E., He, H., Iyyer, M., Yatskar, M., Yih, W.-t., Choi, Y., Liang, P., and Zettlemoyer, L. (2018). Quac: Question answering in context. In _Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing_ , pages 2174–2184. 

- Christiano, P., Cotra, A., and Xu, M. (2021). Eliciting latent knowledge: How to tell if your eyes deceive you. _https://www.alignmentforum.org/posts/qHCDysDnvhteW7kRd/arc-s-first-technicalreport-eliciting-latent-knowledge_ . 

- Christiano, P., Shlegeris, B., and Amodei, D. (2018). Supervising strong learners by amplifying weak experts. _arXiv preprint arXiv:1810.08575_ . 

- Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., and Amodei, D. (2017). Deep reinforcement learning from human preferences. In _Advances in Neural Information Processing Systems_ , pages 4299–4307. 

- Dathathri, S., Madotto, A., Lan, J., Hung, J., Frank, E., Molino, P., Yosinski, J., and Liu, R. (2019). Plug and play language models: A simple approach to controlled text generation. _arXiv preprint arXiv:1912.02164_ .

---

[referencia=1098fc60be7ca2b0 score=0.001]
**3.3 Tasks** 

Our training tasks are from two sources: (1) a dataset of prompts written by our labelers and (2) a dataset of prompts submitted to early InstructGPT models on our API (see Table 6). These prompts are very diverse and include generation, question answering, dialog, summarization, extractions, and other natural language tasks (see Table 1). Our dataset is over 96% English, however in Section 4.3 we also probe our model’s ability to respond to instructions in other languages and complete coding tasks. For each natural language prompt, the task is most often specified directly through a natural language instruction (e.g. “Write a story about a wise frog”), but could also be indirectly through either few-shot examples (e.g. giving two examples of frog stories, and prompting the model to generate a new one) or implicit continuation (e.g. providing the start of a story about a frog). In each case, we ask our labelers to do their best to infer the intent of the user who wrote the prompt, and ask them to skip inputs where the task is very unclear. Moreover, our labelers also take into account the implicit intentions such as truthfulness of the response, and potentially harmful outputs such as biased or toxic language, guided by the instructions we provide them (see Appendix B) and their best judgment. **3.4 Human data collection** To produce our demonstration and comparison data, and to conduct our main evaluations, we hired a team of about 40 contractors on Upwork and through ScaleAI. Compared to earlier work that collects human preference data on the task of summarization (Ziegler et al., 2019; Stiennon et al., 2020; Wu et al., 2021), our inputs span a much broader range of tasks, and can occasionally include 

controversial and sensitive topics. Our aim was to select a group of labelers who were sensitive to the preferences of different demographic groups, and who were good at identifying outputs that were potentially harmful. Thus, we conducted a screening test designed to measure labeler performance on these axes. We selected labelers who performed well on this test; for more information about our 

selection procedure and labeler demographics, see Appendix B.1. 

During training and evaluation, our alignment criteria may come into conflict: for example, when a user requests a potentially harmful response. During training we prioritize helpfulness to the user (not 

7

---

[referencia=1098fc60be7ca2b0 score=0.001]
### **C.1 Details of SFT training** 

We train our SFT models for 16 epochs with residual dropout of 0.2. We use a cosine LR schedule down to 10% of the original learning rate, with no learning rate warmup. For our 1.3B and 6B models, we use an LR of 9.65e-6 and a batch size of 32. For 175B, we use a LR of 5.03e-6 and a batch size of 8. To select learning rates, we did a geometric search over 7 LRs for 1.3B and 6B, and 5 LRs for 175B. We also tuned the number of epochs using geometric search. Our final models 

40 

Table 13: Labeler satisfaction survey 

|**It was clear from the instructions what I was supposed**|**to do.**|
|---|---|
|Strongly agree|57.9%|
|Agree|42.1%|
|Neither agree nor disagree|0%|
|Disagree|0%|
|Strongly disagree|0%|
|**I found the task enjoyable and engaging.**||
|Strongly agree|57.9%|
|Agree|36.8%|
|Neither agree nor disagree|5.3%|
|Disagree|0%|
|Strongly disagree|0%|
|**I found the task repetitive.**||
|Strongly agree|0%|
|Agree|31.6%|
|Neither agree nor disagree|31.6%|
|Disagree|36.8%|
|Strongly disagree|0%|
|**I was paid fairly for doing the task.**||
|Strongly agree|47.4%|
|Agree|42.1%|
|Neither agree nor disagree|10.5%|
|Disagree|0%|
|Strongly disagree|0%|
|**Overall, I’m glad I did this task.**||
|Strongly agree|78.9%|
|<br>Agree|21.1%|
|Neither agree nor disagree|0%|
|Disagree|0%|
|Strongly disagree|0%|



were selected based on the RM score, which we’ve found to be more predictive of human preference results compared to validation loss.

---

[referencia=1098fc60be7ca2b0 score=0.001]
### **5.5 Broader impacts** 

This work is motivated by our aim to increase the positive impact of large language models by training them to do what a given set of humans want them to do. By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. Our results indicate that our techniques hold promise for making language models more helpful, truthful, and harmless. In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. We expect that as model scaling continues, greater care has to be taken to ensure that they are aligned with human intentions (Bostrom, 2014). 

However, making language models better at following user intentions also makes them easier to misuse. It may be easier to use these models to generate convincing misinformation, or hateful or abusive content. 

Alignment techniques are not a panacea for resolving safety issues associated with large language models; rather, they should be used as one tool in a broader safety ecosystem. Aside from intentional misuse, there are many domains where large language models should be deployed only with great care, or not at all. Examples include high-stakes domains such as medical diagnoses, classifying people based on protected characteristics, determining eligibility for credit, employment, or housing, generating political advertisements, and law enforcement. If these models are open-sourced, it becomes challenging to limit harmful applications in these and other domains without proper regulation. On the other hand, if large language model access is restricted to a few organizations with the resources required to train them, this excludes most people from access to cutting-edge ML technology. Another option is for an organization to own the end-to-end infrastructure of model deployment, and make it accessible via an API. This allows for the implementation of safety protocols like use case restriction (only allowing the model to be used for certain applications), monitoring for misuse and revoking access to those who misuse the system, and rate limiting to prevent the generation of large-scale misinformation. However, this can come at the cost of reduced transparency and increased centralization of power because it requires the API provider to make decisions on where to draw the line on each of these questions. 

Finally, as discussed in Section 5.2, the question of who these models are aligned to is extremely important, and will significantly affect whether the net impact of these models is positive or negative. 

20

---

[referencia=1098fc60be7ca2b0 score=0.001]
From this work, we can draw lessons for alignment research more generally: 

1. **The cost of increasing model alignment is modest relative to pretraining.** The cost of collecting our data and the compute for training runs, including experimental runs is a fraction of what was spent to train GPT-3: training our 175B SFT model requires 4.9 petaflops/s-days and training our 175B PPO-ptx model requires 60 petaflops/s-days, compared to 3,640 petaflops/s-days for GPT-3 (Brown et al., 2020). At the same time, our results show that RLHF is very effective at making language models more helpful to users, more so than a 100x model size increase. This suggests that right now increasing investments in alignment of existing language models is more cost-effective than training larger models—at least for our customers’ natural language task distribution. 

2. **We’ve seen some evidence that InstructGPT generalizes ‘following instructions’ to settings that we don’t supervise it in,** for example on non-English language tasks and code-related tasks. This is an important property because it’s prohibitively expensive to have humans supervise models on every task they perform. More research is needed to study how well this generalization scales with increased capabilities; see Christiano et al. (2021) for recent research in this direction. 

3. **We were able to mitigate most of the performance degradations introduced by our fine-tuning.** If this was not the case, these performance degradations would constitute an alignment tax—an additional cost for aligning the model. Any technique with a high tax might not see adoption. To avoid incentives for future highly capable AI systems to remain unaligned with human intent, there is a need for alignment techniques that have low alignment tax. To this end, our results are good news for RLHF as a low-tax alignment technique. 

4. **We’ve validated alignment techniques from research in the real world.** Alignment research has historically been rather abstract, focusing on either theoretical results (Soares et al., 2015), small synthetic domains (Christiano et al., 2018; Leike et al., 2017), or training ML models on public NLP datasets (Ziegler et al., 2019; Stiennon et al., 2020). Our work provides grounding for alignment research in AI systems that are being used in production in