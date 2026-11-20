[referencia=74cf7186aa6d419e score=0.031]
## **Abstract** 

Long-context modeling is crucial for next-generation language models, yet the high computational cost of standard attention mechanisms poses significant computational challenges. Sparse attention offers a promising direction for improving efficiency while maintaining model capabilities. We present NSA, a <u>Natively trainable Sparse Attention mechanism that integrates</u> algorithmic innovations with hardware-aligned optimizations to achieve efficient long-context modeling. NSA employs a dynamic hierarchical sparse strategy, combining coarse-grained token compression with fine-grained token selection to preserve both global context awareness and local precision. Our approach advances sparse attention design with two key innovations: (1) We achieve substantial speedups through arithmetic intensity-balanced algorithm design, with implementation optimizations for modern hardware. (2) We enable end-to-end training, reducing pretraining computation without sacrificing model performance. As shown in Figure 1, experiments show the model pretrained with NSA maintains or exceeds Full Attention models across general benchmarks, long-context tasks, and instruction-based reasoning. Meanwhile, NSA achieves substantial speedups over Full Attention on 64k-length sequences across decoding, forward propagation, and backward propagation, validating its efficiency throughout the model lifecycle.

---

[referencia=fe2a3307a3dae3e5 score=0.010]
## **1 Introduction** 

There is growing interest in using language models to generate text for practical applications. Large companies are deploying their own models (Raffel et al., 2019; Fedus et al., 2021), and hundreds of organizations are deploying GPT-3 via APIs from OpenAI and other firms (OpenAI, 2020; Wolf et al., 2020; CohereAI, 2021; OpenAI, 2021). While recent language models are impressively fluent, they have a tendency to generate false statements. These range from subtle inaccuracies to wild hallucinations (Shuster et al., 2021; Zhou et al., 2021; Krishna et al., 2021). This leads to three concerns: 

1. **Accidental misuse** . Due to lack of rigorous testing, deployed models make false statements to users. This could lead to deception and distrust (Tamkin et al., 2021). 

2. **Blocking positive applications** . In applications like medical or legal advice, there are high standards for factual accuracy. Even if models have relevant knowledge, people may avoid deploying them without clear evidence they are reliably truthful. 

3. **Malicious misuse.** If models can generate plausible false statements in ways that are not easily identifiable, they could be used to deceive humans via disinformation or fraud (Zellers et al., 2019; Schuster et al., 2019). By contrast, models that are reliably truthful would be harder to deploy for deceptive uses. 

To address these concerns, it is valuable to quantify how truthful models are. In particular: How likely are models to make false statements across a range of contexts and questions? Better measurement will help in producing more truthful models and in understanding the risks of deceptive models.

---

[referencia=6ee83218472b4aa1 score=0.009]
# **6 Related Work** 

## **6.1 Long-Context Language Models** 

There is much prior work in designing performant language models with cheaper scaling than Transformers in the context length. Many lines of work pursue Transformer variants with attention modifications like recurrence (Dai et al., 2019), factorizing attention into computationally less intensive approximations (Beltagy et al., 2020; Zaheer et al., 2020), or low-rank approximations (Wang et al., 2020; Peng et al., 2021). Dao et al. (2022) instead provide a faster exact attention by a carefully- 

crafted IO-aware CUDA kernel. Separately, there are attempts to do away with attention entirely to remove quadratic sequence length complexity, often through convolution and/or linear RNNs, e.g., in RWKV (Peng, 2023), S4 (Gu et al., 2022), or Hyena (Poli et al., 2023). Many prior efforts evaluate perplexity on a diverse web corpus as a proxy for the ability to process long contexts; this work shows that precise knowledge access on long contexts may be an added challenge.

---

[referencia=6ee83218472b4aa1 score=0.009]
Figure 5: The effect of changing the position of relevant information (document containing the answer) on multidocument question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context. 

(16K).<sup>5</sup> GPT-3.5-Turbo has a maximum context length of 4K tokens, and GPT-3.5-Turbo (16K) is a version with an extended maximum context length of 16K tokens. We evaluate Claude-1.3 and Claude1.3 (100K) with the Anthropic API; Claude-1.3 has a maximum context length of 8K tokens, and Claude-1.3 (100K) has an extended context length of 100K tokens.<sup>6</sup> 

|Model|Closed-Book|Oracle|
|---|---|---|
|LongChat-13B (16K)|35.0%|83.4%|
|MPT-30B-Instruct|31.5%|81.9%|
|GPT-3.5-Turbo|56.1%|88.3%|
|GPT-3.5-Turbo (16K)|56.0%|88.6%|
|Claude-1.3|48.3%|76.1%|
|Claude-1.3 (100K)|48.2%|76.4%|



Table 1: Closed-book and oracle accuracy of language models on the multi-document question answering task.

---

[referencia=6ee83218472b4aa1 score=0.005]
• Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context. 

Our results indicate that prompting language 

models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. To better understand this trade-off in practice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly _one_ document that answers the question, none or many of the top _k_ documents may contain the answer in the open-domain QA setting. When retrieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model performance saturates long before retriever recall saturates, indicating that current models fail to effectively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( _∼_ 1.5% for GPT-3.5-Turbo and _∼_ 1% for claude-1.3). 

Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future longcontext models; to claim that a language model can robustly use information within long input contexts, it is necessary to show that its performance is minimally affected by the position of the relevant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data.<sup>1</sup>

---

[referencia=1098fc60be7ca2b0 score=0.005]
used for many recent large LMs—predicting the next token on a webpage from the internet—is different from the objective “follow the user’s instructions helpfully and safely” (Radford et al., 2019; Brown et al., 2020; Fedus et al., 2021; Rae et al., 2021; Thoppilan et al., 2022). Thus, we say that the language modeling objective is _misaligned_ . Averting these unintended behaviors is especially important for language models that are deployed and used in hundreds of applications. 

We make progress on aligning language models by training them to act in accordance with the user’s intention (Leike et al., 2018). This encompasses both explicit intentions such as following instructions and implicit intentions such as staying truthful, and not being biased, toxic, or otherwise harmful. Using the language of Askell et al. (2021), we want language models to be _helpful_ (they should help the user solve their task), _honest_ (they shouldn’t fabricate information or mislead the user), and _harmless_ (they should not cause physical, psychological, or social harm to people or the environment). We elaborate on the evaluation of these criteria in Section 3.6.

---

[referencia=fe2a3307a3dae3e5 score=0.003]
Figure 1: **TruthfulQA questions with answers from GPT-3-175B with default prompt.** Examples illustrate false answers from GPT-3 that mimic human falsehoods and misconceptions. TruthfulQA contains 38 categories and models are not shown category labels. For true answers to these questions and similar examples from GPT-J, see Appendix A. 

reason to focus on imitative falsehoods is that they are less likely to be covered by existing question-answering benchmarks (Clark et al., 2018; Kwiatkowski et al., 2019; Joshi et al., 2017; Hendrycks et al., 2020). Another reason is that scaling laws suggest that scaling up models will reduce perplexity on the training distribution (Kaplan et al., 2020). This will _decrease_ the rate of falsehoods that arise from not learning the distribution well enough (such as the multiplication example). Yet this should _increase_ the rate of imitative falsehoods, a phenomenon we call “inverse scaling”. Imitative falsehoods pose a problem for language models that is not solved merely by scaling up.

---

[referencia=fe2a3307a3dae3e5 score=0.002]
- Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke Zettlemoyer. 2017. TriviaQA: A large scale distantly supervised challenge dataset for reading comprehension. In _Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)_ , pages 1601– 1611, Vancouver, Canada. Association for Computational Linguistics. 

- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020. Scaling laws for neural language models. _CoRR_ , abs/2001.08361. 

- Zachary Kenton, Tom Everitt, Laura Weidinger, Iason Gabriel, Vladimir Mikulik, and Geoffrey Irving. 2021. Alignment of language agents. _CoRR_ , abs/2103.14659. 

- Daniel Khashabi, Sewon Min, Tushar Khot, Ashish Sabharwal, Oyvind Tafjord, Peter Clark, and Hannaneh Hajishirzi. 2020. UNIFIEDQA: Crossing format boundaries with a single QA system. In _Findings of the Association for Computational Linguistics: EMNLP 2020_ , pages 1896–1907, Online. Association for Computational Linguistics. 

- Sarah Kreps, R. Miles McCain, and Miles Brundage. 2020. All the news that’s fit to fabricate: Aigenerated text as a tool of media misinformation. _Journal of Experimental Political Science_ , page 1–14. 

- Kalpesh Krishna, Aurko Roy, and Mohit Iyyer. 2021. Hurdles to progress in long-form question answering. In _Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , pages 4940–4957, Online. Association for Computational Linguistics.

---

[referencia=74cf7186aa6d419e score=0.002]
### **4. Experiments** 

We evaluate NSA through three lenses: (1) general benchmarks performance, (2) long-context benchmarks performance, and (3) chain-of-thought reasoning performance, comparing against Full Attention baseline and state-of-the-art sparse attention methods. We defer the efficiency analysis of our sparse computation paradigm to Section 5, where we provide detailed discussions on training and inference speed.

---

[referencia=74cf7186aa6d419e score=0.002]
### **2. Rethinking Sparse Attention Methods** 

Modern sparse attention methods have made significant strides in reducing the theoretical computational complexity of transformer models. However, most approaches predominantly apply sparsity during inference while retaining a pretrained Full Attention backbone, potentially introducing architectural bias that limits their ability to fully exploit sparse attention’s advantages. Before introducing our native sparse architecture, we systematically analyze these limitations through two critical lenses.

---

[referencia=1098fc60be7ca2b0 score=0.002]
### **5.5 Broader impacts** 

This work is motivated by our aim to increase the positive impact of large language models by training them to do what a given set of humans want them to do. By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. Our results indicate that our techniques hold promise for making language models more helpful, truthful, and harmless. In the longer term, alignment failures could lead to more severe consequences, particularly if these models are deployed in safety-critical situations. We expect that as model scaling continues, greater care has to be taken to ensure that they are aligned with human intentions (Bostrom, 2014). 

However, making language models better at following user intentions also makes them easier to misuse. It may be easier to use these models to generate convincing misinformation, or hateful or abusive content. 

Alignment techniques are not a panacea for resolving safety issues associated with large language models; rather, they should be used as one tool in a broader safety ecosystem. Aside from intentional misuse, there are many domains where large language models should be deployed only with great care, or not at all. Examples include high-stakes domains such as medical diagnoses, classifying people based on protected characteristics, determining eligibility for credit, employment, or housing, generating political advertisements, and law enforcement. If these models are open-sourced, it becomes challenging to limit harmful applications in these and other domains without proper regulation. On the other hand, if large language model access is restricted to a few organizations with the resources required to train them, this excludes most people from access to cutting-edge ML technology. Another option is for an organization to own the end-to-end infrastructure of model deployment, and make it accessible via an API. This allows for the implementation of safety protocols like use case restriction (only allowing the model to be used for certain applications), monitoring for misuse and revoking access to those who misuse the system, and rate limiting to prevent the generation of large-scale misinformation. However, this can come at the cost of reduced transparency and increased centralization of power because it requires the API provider to make decisions on where to draw the line on each of these questions. 

Finally, as discussed in Section 5.2, the question of who these models are aligned to is extremely important, and will significantly affect whether the net impact of these models is positive or negative. 

20

---

[referencia=6ee83218472b4aa1 score=0.002]
## guage models is perhaps surprising, since the self- 

former. ArXiv:2004.05150. 

attention mechanisms underlying Transformer language models is technically equally capable of retrieving any token from their contexts. **7 Conclusion** 

Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob 

We empirically study how language models use long input contexts via a series of controlled experiments. We show that language model performance degrades significantly when changing the position of relevant information, indicating that models struggle to robustly access and use infor- 

mation in long input contexts. In particular, per- 

Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-

---

[referencia=1098fc60be7ca2b0 score=0.002]
Fourth, OpenAI’s customers are not representative of all potential or current users of language models—let alone of all individuals and groups impacted by language model use. For most of the duration of this project, users of the OpenAI API were selected off of a waitlist. The initial seeds for this waitlist were OpenAI employees, biasing the ultimate group toward our own networks. 

Stepping back, there are many difficulties in designing an alignment process that is fair, transparent, and has suitable accountability mechanisms in place. The goal of this paper is to demonstrate that this alignment technique can align to an specific human reference group for a specific application. We are not claiming that researchers, the labelers we hired, or our API customers are the right source of preferences. There are many stakeholders to consider—the organization training the model, the customers using the model to develop products, the end users of these products, and the broader population who may be directly or indirectly affected. It is not only a matter of making the alignment process more participatory; it is impossible that one can train a system that is aligned to everyone’s preferences at once, or where everyone would endorse the tradeoffs. 

One path forward could be to train models that can be conditioned on the preferences of certain groups, or that can be easily fine-tuned or prompted to represent different groups. Different models can then be deployed and used by groups who endorse different values. However, these models might still end up affecting broader society and there are a lot of difficult decisions to be made relating to whose preferences to condition on, and how to ensure that all groups can be represented and can opt out of processes that may be harmful. 

> 10Note that while fine-tuning models using human data is common practice when deploying ML systems, the purpose of these efforts is to obtain a model that performs well on a company’s specific use case, rather than advancing the alignment of general-purpose ML models. 

18

---

[referencia=1098fc60be7ca2b0 score=0.002]
17 

the real world with customers.<sup>10</sup> This enables an important feedback loop on the techniques’ effectiveness and limitations.

---

[referencia=6ee83218472b4aa1 score=0.002]
## **2.3 Results and Discussion** 

We experiment with input contexts containing 10, 20, and 30 total documents. Figure 5 presents multidocument question answering performance when varying the position of relevant information within the input context. To contextualize model performance, we also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. 

**Model performance is highest when relevant information occurs at the beginning or end of its input context.** As illustrated in Figure 5, changing the position of relevant information in the input context leads to substantial decreases in model performance. In particular, we see a distinctive U- 

> 5We use the 0613 OpenAI model versions. 

> 6We also evaluate GPT-4 (8K) on a subset of multidocument QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute performance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. 

shaped performance curve—models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded performance when forced to use information within the middle of its input context. For example, GPT-3.5Turbo’s multi-document QA performance can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than performance without _any_ input documents (i.e., closedbook performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks.

---

[referencia=6ee83218472b4aa1 score=0.001]
Handling these use-cases requires language models to successfully operate over long sequences. Existing language models are generally implemented with Transformers (Vaswani et al., 2017), which require memory and compute that increases quadratically in sequence length. As a result, Transformer language models were often trained with relatively small context windows (between 5122048 tokens). Recent improvements in hardware (e.g., faster GPUs with more memory) and algorithms (Dai et al., 2019; Dao et al., 2022; Poli et al., 



<!-- Start of picture text -->

---

[referencia=fe2a3307a3dae3e5 score=0.001]
While we don’t expect current models to be truthful, there are many contexts in which truthfulness is necessary. Large language models such as GPT-3 may see widespread use as foundation models for downstream tasks that require robust truthfulness (Bommasani et al.Bommasani et al., 2021). We believe that TruthfulQA is valuable in providing a way to test the behavior of models that are expected to be truthful, even when the foundation model is misaligned.

---

[referencia=74cf7186aa6d419e score=0.001]
#### **2.2. The Myth of Trainable Sparsity** 

Our pursuit of native trainable sparse attention is motivated by two key insights from analyzing inference-only approaches: (1) **_Performance Degradation_** : Applying sparsity post-hoc forces models to deviate from their pretrained optimization trajectory. As demonstrated by Chen et al. (2024b), top 20% attention can only cover 70% of the total attention scores, rendering structures like retrieval heads in pretrained models vulnerable to pruning during inference. (2) **_Training Efficiency Demands_** : Efficient handling of long-sequence training is crucial for modern LLM development. This includes both pretraining on longer documents to enhance model capacity, and subsequent adaptation phases such as long-context fine-tuning and reinforcement learning. However, existing sparse attention methods primarily target inference, leaving the computational challenges in training largely unaddressed. This limitation hinders the development of more capable long-context models through efficient training. Additionally, efforts to adapt existing sparse attention for training also expose challenges: 

**Non-Trainable Components.** Discrete operations in methods like ClusterKV (Liu et al., 2024) (includes k-means clustering) and MagicPIG (Chen et al., 2024b) (includes SimHash-based selecting) create discontinuities in the computational graph. These non-trainable components prevent gradient flow through the token selection process, limiting the model’s ability to learn optimal sparse patterns. 

**Inefficient Back-propagation.** Some theoretically trainable sparse attention methods suffer 

4 

from practical training inefficiencies. Token-granular selection strategy used in approaches like HashAttention (Desai et al., 2024) leads to the need to load a large number of individual tokens from the KV cache during attention computation. This non-contiguous memory access prevents efficient adaptation of fast attention techniques like FlashAttention, which rely on contiguous memory access and blockwise computation to achieve high throughput. As a result, implementations are forced to fall back to low hardware utilization, significantly degrading training efficiency. 

#### **2.3. Native Sparsity as an Imperative** 

These limitations in inference efficiency and training viability motivate our fundamental redesign of sparse attention mechanisms. We propose NSA, a natively sparse attention framework that addresses both computational efficiency and training requirements. In the following sections, we detail the algorithmic design and operator implementation of NSA.

---

[referencia=fe2a3307a3dae3e5 score=0.001]
- Eric Wallace and Jordan Boyd-Graber. 2018. Trick me if you can: Adversarial writing of trivia challenge questions. In _Proceedings of ACL 2018, Student Research Workshop_ , pages 127–133, Melbourne, Australia. Association for Computational Linguistics. 

- Alex Wang, Kyunghyun Cho, and Mike Lewis. 2020. Asking and answering questions to evaluate the factual consistency of summaries. In _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics_ , pages 5008–5020, Online. Association for Computational Linguistics. 

- Ben Wang and Aran Komatsuzaki. 2021. GPTJ-6B: A 6 Billion Parameter Autoregressive Language Model. https://github.com/ kingoflolz/mesh-transformer-jax. 

- Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. 2021. Finetuned language models are zero-shot learners. 

- Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest, and Alexander Rush. 2020. Transformers: State-of-the-art natural language processing. In _Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations_ , pages 38–45, Online. Association for Computational Linguistics. 

- Jing Xu, Da Ju, Margaret Li, Y-Lan Boureau, Jason Weston, and Emily Dinan. 2020. Recipes for safety in open-domain chatbots. _CoRR_ , abs/2010.07079. 

- Rowan Zellers, Ari Holtzman, Hannah Rashkin, Yonatan Bisk, Ali Farhadi, Franziska Roesner, and Yejin Choi. 2019. Defending against neural fake news. _CoRR_ , abs/1905.12616.

---

[referencia=fe2a3307a3dae3e5 score=0.001]
## **6 Related Work** 

Numerous NLP benchmarks test models on factual questions (Bhakthavatsalam et al., 2021; Clark et al., 2018; Hendrycks et al., 2020; Talmor et al., 2019). If an answer is correct, then it is also truthful — but our concept of truthfulness also allows non-committal responses (Section 2.1). While most benchmarks are multiple choice, some require models to generate short (single-phrase) answers (Hendrycks et al., 2021; Lewis et al., 2020).