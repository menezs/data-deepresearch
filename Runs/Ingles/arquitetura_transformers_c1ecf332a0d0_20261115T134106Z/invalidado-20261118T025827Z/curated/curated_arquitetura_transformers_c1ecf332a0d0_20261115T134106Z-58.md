[referencia=2d7205e3738744ae score=0.420]
### 2.3 LLaMA (decoder-only) vs. T5 architecture (encoder-decoder)

The LLaMA family uses a causal decoder-only architecture trained as a traditional language model to predict the next token given an input sequence. These models do not have independent means of processing or representing input sequences and target sequences differently, but their unidirectional attention mechanism and language modeling capability [20] have nonetheless proven highly effective for generative tasks that require coherent and human-like text [21].

The T5 family, on the other hand, uses an encoder-decoder architecture as shown in Figure 1. The encoder is presented with an input sequence of tokens, which could be a sentence in English to translate to German, and outputs a sequence of embeddings that captures the information from the input tokens. The decoder then takes over to autoregressively predict the target sequence, which in our example, generates the translation one token at a time using the previously generated tokens as context for each new prediction. The decoder has cross-attention layers that allow each of its blocks to pay attention to the full encoder output, giving it access to information from the input as it generates the translation. However, within its own layers, a causal masking pattern [22] is applied to restrict its attention to previously generated tokens, ensuring that the model does not “cheat” by using future information to predict the current token.

There are several ongoing studies that provide comparisons between decoder-only and encoder-decoder architectures [23, 24, 25, 26] with mixed results. Raffel et al. [19] demonstrated that encoder-decoder models outperform decoder-only LLMs for transfer learning, where a pretrained model is finetuned on single downstream task. Liu et al. [27] found that encoder-decoder model architectures make better use of their context windows as their bidirectional encoder improves importance estimation in long inputs. However, Wang et al. [26] found that causal decoder-only models trained on an auto-regressive language modeling objectives exhibit the strongest zero-shot generalization after unsupervised training. In our work, we seek to understand whether DoLa can be effective for encoder-decoder architectures given their relative sparsity of parameters and unique architecture.

---

[referencia=2d7205e3738744ae score=0.261]
## 1 Introduction

Large Language Models (LLMs) have exhibited great capability in generating human-like text across a spectrum of topics and styles, and are used for a variety of tasks including question answering, content generation, and complex chain-of-thought-reasoning. However, even state-of-the-art models can hallucinate, or in other words, generate text that lacks factuality (according to its training data) or faithfulness (according to the input prompt and data) [1]. While LLM hallucination has multifaceted origins that range anywhere from pre-training to model design, recent work by Chuang et al. [2] has shown that Decoding by Contrastive Layers (DoLa), an inference-time decoding strategy where tokens are selected by contrasting predictions made by intermediate model layers, can reduce factuality hallucinations in LLMs.

In particular, DoLa takes advantage of the modular nature of knowledge encoding [3, 4] within transformer-based LMs. By manipulating how outputs from different layers are combined during decoding, DoLa exploits the inherent structure of LLMs to reduce hallucinations without fundamentally altering the underlying model architecture or training procedure. For example, since knowledge neurons have been shown to exist in the top layers of LLM’s, contrasting the final layer with an intermediate layer before this knowledge injection can ensure that the output logits correctly weight this later information. DoLa consistently improves truthfulness and performance of LLaMA models by 12-17% on TruthfulQA (a truthfulness benchmark), demonstrating its effectiveness in reducing factuality hallucinations [2].

However, the mechanics of faithfulness hallucinations are less understood. One way to benchmark faithfulness is to evaluate models on datasets of tasks with language-based constraints and judge their ability to follow the provided instructions. Some of these tasks have been shown to demonstrate properties of inverse scaling, where the performance of larger models are worse than that of their smaller analogues, reflecting a tendency of LLMs to memorize training data. To explore the potential effect of DoLa on faithfulness, we selected two instruction following datasets from the Hallucinations Leaderboard [5], MemoTrap and IFEval, to evaluate our models.

Furthermore, given that encoder-decoder models like FLAN-T5 have demonstrated impressive instruction-following performance with much fewer parameters and greater computation efficiency, we decided to integrate and evaluate DoLa on the T5 family and explored its impact on FLAN-T5 in the realm of instruction following.

---

[referencia=2d7205e3738744ae score=0.219]
## 4 Experimental Setup

### 4.1 Models and Baselines

We examine four sizes of FLAN-T5 (small, base, large and xl) and of T5 (small, base, large and xl) and compare them with and without the DoLa decoding strategy. Our experiment focuses on evaluating the performance of the FLAN-T5 and T5 baseline models (MLM-baseline in Figure 2) and MLM-DoLa, the same models implemented with DoLa.

### 4.2 Datasets

We considered two instruction following datasets: MemoTrap (as used in the Inverse Scaling Prize) [33] and IFEval [34], which are both designed to evaluate LLM’s abilities to follow specific instructions. MemoTrap is a dataset spanning text completion, translation and question-answering (QA), created to investigate whether when language models fall into memorization traps. It contains instructions that prompt the LLM to complete a well-known saying with an ending word that deviates from the commonly seen ending. We utilized the ‘Proverb Ending’ dataset (837 instances), a data set with three columns, prompt: the input provided to the LM, class: a list of two candidate continuations for the prompt, and answer_index: the correct continuation in the class list. The model is then tasked to follow these instructions in a zero-shot setting.

IFEval [34] is a framework that includes a series of prompts and a flexible evaluation framework to assess an LM’s proficiency in executing text-based instructions. The prompts encompass a variety of challenges that range from straightforward text manipulation to intricate, multi-step reasoning that mirrors the demands of real-life use. Each entry in the dataset features a detailed task prompt, which instructs the model to produce content that conforms to specific guidelines. The evaluation framework breaks down the different verifiable tasks and judges the natural language responses in loose and strict modes, allowing for a comprehensive and detailed understanding of a model’s instruction following ability.

---

[referencia=2d7205e3738744ae score=0.073]
## 3 Methodology

### 3.1 DoLa Implementation with T5

As DoLa was originally designed for the LLaMA-v1 family of models, we had to implement DoLa in version 1.1 of the T5 family (T5v1.1) [19] of the HuggingFace transformers package. We also needed to modify the generation utils of the transformer package for our logit analysis of the early exit layers.

While T5 is trained with unsupervised denoising, our implementation utilizes the T5ForConditionalGeneration class, which includes a language modeling head on top of the decoder. Here, portions of the input sequence are masked by sentinel tokens (unique mask tokens), which the model learns to predict based on the surrounding context. We distinguish the differing training objectives between T5 and LLaMa, masked language modeling (MLM) and casual language modeling (CLM), in the experimental setup in Figure 2. Notably, we have implemented the contrastive decoding solely in the decoder module of T5.

---

[referencia=2d7205e3738744ae score=0.072]
- [12] Alisa Liu, Maarten Sap, Ximing Lu, Swabha Swayamdipta, Chandra Bhagavatula, Noah A. Smith, and Yejin Choi. Dexperts: Decoding-time controlled text generation with experts and anti-experts, 06 2021. URL https://arxiv.org/abs/2105.03023.
- [13] Sean O’brien and Mike Lewis. Contrastive decoding improves reasoning in large language models, 09 2023. URL https://arxiv.org/pdf/2309.09117.pdf.
- [14] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep bidirectional transformers for language understanding, 10 2018. URL https://arxiv.org/abs/1810.04805.
- [15] Openai. Gpt-4 technical report, 03 2023. URL https://arxiv.org/pdf/2303.08774.pdf.
- [16]
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample.
Llama: Open and efficient foundation language models.
*arXiv (Cornell University)* , 02 2023a.
doi: 10.48550/arxiv.2302.13971.

---

[referencia=2d7205e3738744ae score=0.052]
- [1]
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang, Andrea Madotto, and Pascale Fung.
Survey of hallucination in natural language generation.
*ACM Computing Surveys* , 55, 11 2022.
doi: 10.1145/3571730.
- [2] Yung-Sung Chuang, Yujia Xie, Hongyin Luo, Yoon Kim, James Glass, and Pengcheng He. Dola: Decoding by contrastive layers improves factuality in large language models, 03 2024. URL https://arxiv.org/pdf/2309.03883.pdf.
- [3] Ian Tenney, Dipanjan Das, and Ellie Pavlick. Bert rediscovers the classical nlp pipeline, 2019. URL https://aclanthology.org/P19-1452.pdf.
- [4] Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, Furu Wei, and Moe Key. Knowledge neurons in pretrained transformers. 1:8493–8502, 2022. URL https://aclanthology.org/2022.acl-long.581.pdf.
- [5] Giwon Hong, Aryo Pradipta Gema, Rohit Saxena, Xiaotang Du, Ping Nie, Yu Zhao, Laura Perez-Beltrachini, Max Ryabinin, Xuanli He, and Pasquale Minervini. The hallucinations leaderboard – an open effort to measure hallucinations in large language models, 2024.
- [6] Zheng Zhang Dan Klein Ruiqi Zhong, Kristy Lee. Adapting language models for zero-shot learning by meta-tuning on dataset and prompt collections, 04 2021. URL https://arxiv.org/pdf/2104.04670.pdf.

---

[referencia=2d7205e3738744ae score=0.046]
- [20]
Amir Feder, Nadav Oved, Uri Shalit, and Roi Reichart.
Causalm: Causal model explanation through counterfactual language models.
*Computational Linguistics* , 47:1–54, 05 2021.
doi: 10.1162/coli_a_00404.
- [21]
Emre Kıcıman, Robert A Van, Vishal Sharma, and Chenhao Tan.
Causal reasoning and large language models: Opening a new frontier for causality.
*arXiv (Cornell University)* , 04 2023.
doi: 10.48550/arxiv.2305.00050.
- [22]
Qingyu Yin, Xuzheng He, Xiang Zhuang, Yu Zhao, Jianhua Yao, Xiaoyu Shen, and Qiang Zhang.
Stablemask: Refining causal masking in decoder-only transformer.
*arXiv (Cornell University)* , 02 2024.
doi: 10.48550/arxiv.2402.04779.
- [23] Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, and Omer Levy. Zeroscrolls: A zero-shot benchmark for long text understanding. URL https://arxiv.org/pdf/2305.14196.pdf.
- [24]
Tianyang Lin, Yuxin Wang, Xiangyang Liu, and Xipeng Qiu.
A survey of transformers.
*AI Open* , 3, 10 2022.
doi: 10.1016/j.aiopen.2022.10.001.
- [25] Shubham Toshniwal, Anjuli Kannan, Chung-Cheng Chiu, Yonghui Wu, Tara N Sainath, and Karen Livescu. A comparison of techniques for language model integration in encoder-decoder speech recognition, 12 2018. URL https://ieeexplore.ieee.org/abstract/document/8639038?casa_token=RoF0ZZfsApIAAAAA:MLQs0Hg2XBz7GlGjAz3PWc_7VzR0S3j6iHLGG3VHUC4WClq_6WghIQ1wxroTzlUGVQ86gVXOsEM.

---

[referencia=2d7205e3738744ae score=0.036]
### 3.2 Dynamic Contrastive Premature Layer Selection (DoLa)

This section serves as a summary of Chuang et al. [2]’s work, which describes the mechanism of DoLa in detail. Traditionally, the next-token distribution of T5 is taken directly from the final layer of the decoder. However, given the complexity of the attention mechanism and the increasingly abstracted context, the final layer may not represent the best next-token prediction, particularly if the intermediate outputs of the layers are changing dramatically. This is where DoLa becomes significant – by dynamically selecting the most informative premature layer, or the layer with the greatest contrast to the final mature layer, we can ensure that we surface the best information that emerges and are not overly influenced by earlier, more naive predictions.

In the selection process, we use the Jensen-Shannon Divergence (JSD), a symmetric measure of distance derived from the Kullback-Leibler Divergence, to measure distance between the layers. Given previous tokens , the log probabilities of the next token in layer of the early exit layers can be represented as . Thus, we can define our distance metric between an early exit layer and the mature layer as:

The layer with the greatest JSD is chosen as the optimal premature layer :

The premature layer is then used to adjust the output from the mature layer, amplifying the contribution of tokens that are contextually relevant and downplaying those that are not. The final predicted probability distribution over the vocabulary used to sample the next token is defined as:

where is a function that adjusts the output probability of to if it had high probability in the mature layer and to otherwise. This ensures that the final output distribution does not over-weight low-probability tokens due to unstable contrasting and retains sufficient signal from the original mature layer distribution. A softmax is applied to normalize the resultant values into a proper probability distribution before use.

### 3.3 Repetition Penalty

To mitigate the tendency of language models to produce repetitive text, we incorporate a repetition penalty [28] of during the decoding process. Prior work [29] and recent findings by [30] have demonstrated the effectiveness of this specific value in reducing repetition during generation of extended text sequences, particularly in tasks requiring chain-of-thought reasoning. While this allowed our model to avoid looping outputs in general, we still saw some evidence of undesirable repetition in model outputs with specific prompts.

---

[referencia=2d7205e3738744ae score=0.035]
- [7]
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei.
Scaling instruction-finetuned language models.
*arXiv:2210.11416 [cs]* , 10 2022.
URL https://arxiv.org/abs/2210.11416.
- [8] Ariel Gera, Roni Friedman, Ofir Arviv, Chulaka Gunasekara, Benjamin Sznajder, Noam Slonim, and Eyal Shnarch. The benefits of bad advice: Autocontrastive decoding across model layers. 1:10406, 1042. URL https://aclanthology.org/2023.acl-long.580.pdf.
- [9] Lisa Xiang, Li, Ari Holtzman, Daniel Fried, Percy Liang, Jason Eisner, Tatsunori Hashimoto, Luke Zettlemoyer, and Mike Lewis. Contrastive decoding: Open-ended text generation as optimization. URL https://arxiv.org/pdf/2210.15097.pdf.
- [10] Weijia Shi, Xiaochuang Han, Mike Lewis, Yulia Tsvetkov, Luke Zettlemoyer, and Scott Yih. Trusting your evidence: Hallucinate less with context-aware decoding. URL https://arxiv.org/pdf/2305.14739.pdf.
- [11] Nikolay Malkin, Zhen Wang, and Nebojsa Jojic. Coherence boosting: When your pretrained language model is not paying enough attention, 03 2022. URL https://arxiv.org/abs/2110.08294.

---

[referencia=2d7205e3738744ae score=0.029]
- [32] Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu, Lei Li, and Zhifang Sui. A survey on in-context learning, 12 2022. URL https://arxiv.org/abs/2301.00234.
- [33] Ian Mckenzie, Alexander Lyzhov, Michael Pieler, Stability Ai, Alicia Parrish, Aaron Mueller, Ameya Prabhu, Euan Mclean, Aaron Kirtland, Alexis Ross, Alisa Liu, Andrew Gritsevskiy, Daniel Wurgaft, Derik Kauffman, Gabriel Recchia, Jiacheng Liu, Joe Cavanagh, Max Weiss, Sicong Huang, Floating Droid, Tom Tseng, Tomasz Korbak, Xudong Shen, Yuhui Zhang, Zhengping Zhou, Najoung Kim, Samuel Bowman, and Ethan Perez. Inverse scaling: When bigger isn’t better winning task authors *, 06 2023. URL https://arxiv.org/pdf/2306.09479.pdf.
- [34] Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou. Instruction-following evaluation for large language models, 2023. URL https://arxiv.org/pdf/2311.07911.pdf.
- [35] Cheng-Han Chiang and Hung-yi Lee. Can large language models be an alternative to human evaluations?, 05 2023a. URL https://arxiv.org/abs/2305.01937.
- [36]
Cheng-Han Chiang and Hung-yi Lee.
A closer look into automatic evaluation using large language models.
*arXiv (Cornell University)* , 10 2023b.
doi: 10.48550/arxiv.2310.05657.
- [37] Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Ruochen Xu, and Chenguang Zhu. G-eval: Nlg evaluation using gpt-4 with better human alignment. 03 2023. doi: 10.48550/arxiv.2303.16634.

---

[referencia=2d7205e3738744ae score=0.024]
## 8 Appendix

### 8.1 IFEval Verifiable Instruction Accuracy of FLAN-T5-Small-DoLa

| Instruction Categories | FLAN-T5-Small-DoLa Accuracy (%) | 
|---|---|
| change_case | 17.98 | 
| combination | 4.615 | 
| detectable_content | 20.75 | 
| detectable_format | 4.459 | 
| keywords | 29.45 | 
| language | 29.03 | 
| length_constraints | 34.27 | 
| punctuation | 69.70 | 
| startend | 2.985 | 
| change_case:capital_word_frequency | 32.00 | 
| change_case:english_capital | 0 | 
| change_case:english_lowercase | 20.51 | 
| combination:repeat_prompt | 0 | 
| combination:two_responses | 12.50 | 
| detectable_content:number_placeholders | 14.81 | 
| detectable_content:postscript | 26.92 | 
| detectable_format:constrained_response | 20.00 | 
| detectable_format:json_format | 5.882 | 
| detectable_format:multiple_sections | 0 | 
| detectable_format:number_bullet_lists | 0 | 
| detectable_format:number_highlighted_sections | 8.333 | 
| detectable_format:title | 0 | 
| keywords:existence | 10.26 | 
| keywords:forbidden_words | 46.94 | 
| keywords:frequency | 21.43 | 
| keywords:letter_frequency | 36.36 | 
| language:response_language | 29.03 | 
| length_constraints:nth_paragraph_first_word | 0 | 
| length_constraints:number_paragraphs | 0 | 
| length_constraints:number_sentences | 55.77 | 
| length_constraints:number_words | 38.46 | 
| punctuation:no_comma | 69.70 | 
| startend:end_checker | 7.692 | 
| startend:quotation | 0 |

---

[referencia=2d7205e3738744ae score=0.021]
### 2.2 Contrastive Decoding Methods

Contrastive decoding has become a popular method to improve the text generation capability of language models. One class of methods contrasts predictions between models. Gera et al. [8] introduces a token-level probability distribution adjustment method which enhances the accuracy of LMs by contrasting predictions from an expert and amateur model with the same architecture. Xiang et al. [9] use a similar method with an additional plausibility constraint that tunes how much contrasting is used depending on the confidence of the expert model. Outside the expert-amateur model paradigm, Shi et al. [10] contrasts the output distribution of the a model when it is used with and without the full context of the token history. Finally, DoLa contrasts logits within a single model between the final layer and a dynamically chosen “early-exit” layer at inference-time, requiring no additionally training and allowing for flexible application to pre-trained models. Many of the decoding approaches in the literature thus far [2, 8, 9, 10, 11, 12, 13] have been implemented on autoregressive and/or causal LMs such as BERT [14], GPT [15], and LLaMA [16, 17] models instead of seq2seqLMs [18] such as FLAN-T5 [7] and T5 [19], which have an encoder-decoder architecture. Thus, our implementation of DoLa for the T5 family is not only a study of contrastive decoding for instruction following but also extends this technique to encoder-decoder architectures as a whole.

---

[referencia=2d7205e3738744ae score=0.015]
## 5 Results

---

[referencia=2d7205e3738744ae score=0.012]
## 2 Literature Review

### 2.1 Instruction Following

LLM’s often need to follow complex instructions to produce contextually appropriate and accurate responses that align with task requirements and user expectations. Instruction following can be thought of as zero-shot learning, where a model’s language modeling ability is used to perform tasks like sentiment classification without needing to explicitly train the model for those tasks [6]. Successful instruction following can vastly extend the capabilities of a model. In 2021, Chung et al. [7] introduced an “instruction finetuning” procedure called FLAN, which uses a wide range of instruction templates and data to finetune models to be better starting points for new tasks. These FLAN models show a significant performance gain on held-out training tasks. Since MemoTrap and IFEval were not in the instruction tuning data used to create the FLAN-T5 family, we can consider this work a study of zero-shot instruction following performance.

---

[referencia=2d7205e3738744ae score=0.010]
- [26] Thomas Wang, Adam Roberts, Daniel Hesslow, Teven Le Scao, Hyung Chung, Iz Beltagy, Julien Launay, Colin Raffel, Hugging Face, Google, and Lighton. What language model architecture and pretraining objective work best for zero-shot generalization? the bigscience architecture & scaling group, 04 2022. URL https://arxiv.org/pdf/2204.05832.pdf.
- [27] Nelson Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. URL https://arxiv.org/pdf/2307.03172.pdf.
- [28] Waseem AlShikh, Manhal Daaboul, Kirk Goddard, Brock Imel, Kiran Kamble, Parikshith Kulkarni, and Melisa Russak. Becoming self-instruct: introducing early stopping criteria for minimal instruct tuning, 07 2023. URL https://arxiv.org/abs/2307.03692.
- [29]
Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong, and Richard Socher.
Ctrl: A conditional transformer language model for controllable generation.
*arXiv:1909.05858 [cs]* , 09 2019.
URL https://arxiv.org/abs/1909.05858.
- [30] Jin Xu, Xiaojiang Liu, Jianhao Yan, Deng Cai, Huayang Li, and Jian Li. Learning to break the loop: Analyzing and mitigating repetitions for neural text generation, 10 2022. URL https://arxiv.org/abs/2206.02369.
- [31]
Brian Lester, Rami Al-Rfou, and Noah Constant.
The power of scale for parameter-efficient prompt tuning.
*arXiv:2104.08691 [cs]* , 09 2021.
URL https://arxiv.org/abs/2104.08691.

---

[referencia=2d7205e3738744ae score=0.006]
### 5.1 MemoTrap Evaluation

| Model | No DoLa | With DoLa | 
|---|---|---|
| FLAN-T5-Small | 67.86% | 48.98% | 
| FLAN-T5-Base | 44.80% | 11.47% | 
| FLAN-T5-Large | 58.18% | 52.21% | 
| FLAN-T5-XL | 87.34% | 81.48% | 

Across the board, the addition of DoLa causes a significant drop in performance in model accuracy on MemoTrap (Table 1): FLAN-T5-Small drops from 67.86% to 48.98% when we add DoLa, and FLAN-T5-Base decreases even more drastically from 44.80% to 11.47%. While DoLa has less effect on the larger T5 models, it nonetheless has a decidedly negative impact on performance. Interestingly, we see mixed evidence of inverse scaling: while the base and large models perform worse than FLAN-T5-Small without DoLa, FLAN-T5-XL shows the best performance, contrary to previous work [33]. However, it’s difficult to make a fair comparison across the model sizes given the differing nature of the responses: with the same prompts, the smaller models generate mostly sentence completions while FLAN-T5-XL only outputs the options itself (‘A’ or ‘B’) [full results].

| Model | T5 | T5 + DoLa | 
|---|---|---|
| T5-Small | 42.29% | 43.13% | 
| T5-Base | 0.0% | 0.0% | 
| T5-Large | 5.615% | 5.735% |

---

[referencia=2d7205e3738744ae score=0.006]
While we tested the smaller T5 models on MemoTrap, we quickly began to get incoherent text from our models, limiting experimentation. While T5-Small achieves reasonable accuracy, T5-Base and up were entirely unintelligible, causing us to abandon the T5 models for their FLAN counterparts for this study and in IFEval as well. When comparing results between Table 1 and 2, it is unsurprising that the instruction-tuned variant of T5 had better performance. When Chuang et al. [2] compared LLaMA with its instruction-tuned variant Vicuna, Vicuna was likewise better at following instructions [38].

### 5.2 IFEval Evaluation

| FLAN-T5 Model | Instruction-Level Loose Accuracy (%) | Prompt-Level Loose Accuracy (%) | 
|---|---|---|
| Small | 20.38 | 9.982 | 
| Small + DoLa | 22.90 | 11.83 | 
| Base | 26.38 | 14.42 | 
| Base + DoLa | 23.02 | 12.01 | 
| Large | 26.86 | 15.34 | 
| Large + DoLa | 26.74 | 16.45 | 
| XL | 28.78 | 15.71 | 
| XL + DoLa | 25.30 | 14.23 | 

For IFEval, shown in Table 3, the addition of DoLa has varying effect across the FLAN-T5 models. For FLAN-T5-Small, DoLa improves instruction-level accuracy from 20.38% to 22.90%, and the overall prompt-level accuracy from 9.982% to 11.83%. For FLAN-T5-Base and FLAN-T5-XL, DoLa decreases the overall accuracy, and for FLAN-T5-Large, DoLa’s impact is negligible. While these numbers may seem low, this is not entirely surprising as even FLAN-PaLM, the second-best model evaluated on IFEval, only achieves 40-50% accuracy across all metrics [34].

---

[referencia=2d7205e3738744ae score=0.004]
### 6.3 Limitations

Through our results, we were able to find compelling examples where DoLa both improved and hurt our model performance. However, both qualitative and quantitative analysis show that for most part, even the largest models we evaluated struggled to comprehend or properly pay attention to the complex instructions in IFEval. DoLa’s not magic – as a decoding strategy, it only works if the model itself is able to properly generate appropriate token distributions in its intermediate layers. Thus, evaluating larger models like FLAN-XXL and FLAN-UL2 with better base performance may have been able to more clearly demonstrate the situational benefits or drawbacks of DoLa. Furthermore, it would have been interesting to evaluate the LLaMA family on these datasets as well to compare trends between model families.

Also, while we adhered to the zero-shot spirit of the MemoTrap and IFEval datasets, we may have been able to perform better logit analysis if the prompts were restructured to have specific tokens that were unambiguously "correct" for each response. By forcing the model to output the entire sentence completion in MemoTrap, or generating a fixed number of words in IFEval, we may have been able to more quantifiably understand DoLa’s impact and draw comparisons between the different model sizes.

## 7 Conclusion and Future Works

In this paper, we extended DoLa to encoder-decoder language models, tested its performance on a variety of instruction-following tasks, and analyzed the evolution of the model’s intermediate layer outputs to visualize DoLa’s impact on token generation. While DoLa improves categories of instruction following like keyword existence, it harms other categories like start-end, indicating its potential but also its limitations.

Beyond evaluating DoLa on larger models, an interesting future work could be to implement DoLa on the encoder side of the encoder-decoder model architecture and investigate contrastive embeddings. Futhermore, since many of the lower-level early-exit-layers of the model seemed to have similar outputs in the logit analysis, it may be possible to cut them out entirely and experiment with assymmetrical autoencoders, models with more encoder layers than decoder layers, which can also reduce computational load and memory requirements [39].

It would also be interesting to study the effect of DoLa with retrieval augmentation, which has been shown to reduce hallucination [40]. Developing an external knowledge-base query mechanism could be a useful way to better quantify DoLa’s effects on an output token probability distribution.

---

[referencia=2d7205e3738744ae score=0.003]
- [17] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and fine-tuned chat models, 07 2023b. URL https://arxiv.org/abs/2307.09288.
- [18] Ilya Sutskever, Oriol Vinyals, and Quoc V Le. Sequence to sequence learning with neural networks, 2014. URL https://arxiv.org/abs/1409.3215.
- [19] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer, 2019. URL https://arxiv.org/abs/1910.10683.

---

[referencia=2d7205e3738744ae score=0.002]
By inspecting the most likely tokens of the premature layers in Figure 6, we can see that the lower layers encode predominantly syntactic or blank tokens, and that informative tokens like lacking only surface in the final layers. We theorize that the attention mechanism that takes into account the prompt is injecting this "faithfulness" at a higher level in the model, which would have been dominated by model’s predisposition towards language modeling (generating syntax) if it weren’t for DoLa’s intervention. In fact, we can observe that the top 3 tokens lacking, generally, and both from the DoLa output distribution only appear once in the top 5 tokens table across all the premature layers in the model, highlighting the power of contrastive decoding to produce useful signal from intermediate outputs.

### 6.2 Drawbacks of DoLa

While adding DoLa improved the generation of “faithful” tokens in the keyword existence instruction category, it decreased accuracy in the start-end category of instructions (Figure 7), where the model is tasked to attach some specified text to the beginning or end of its response. To understand what might be happening, we compare the responses of FLAN-T5-XL with and without DoLa on prompt 418 of the IFEval dataset in Figure 8.

Although the DoLa model response provides a more informative answer in the spirit of the question, it fails the crucial task of ending the blog post with the specified phrase and as is scored accordingly. The baseline model, on the other hand, only outputs the ending and thus receives a good score. This shows how difficult interpreting DoLa can be – while in the previous example, DoLa helped surface later tokens that presumably came from paying attention to the prompt, it defaults back to language modeling here, a reversal of the previous regime. Thus, without an understanding of how reasoning and knowledge modules are encoded and located in the neurons of a model, it can be difficult or intractable to properly define early exit layers and use DoLa appropriately to reduce faithfulness hallucinations.