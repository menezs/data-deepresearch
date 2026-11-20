[referencia=46fd66187ec3e6ae score=0.304]
## **Training Compute-Optimal Large Language Models** 

**Jordan Hoffmann**<sup>_★_</sup> **, Sebastian Borgeaud**<sup>_★_</sup> **, Arthur Mensch**<sup>_★_</sup> **, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre**<sup>_★_</sup> 

> _★_ Equal contributions 

**We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number** 

**of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model,** **_Chinchilla_ , that uses the same compute budget as** **_Gopher_ but with 70B parameters and 4** × **more more data.** **_Chinchilla_ uniformly and significantly outperforms** **_Gopher_ (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks.** 

**This also means that** **_Chinchilla_ uses substantially less compute for fine-tuning and inference, greatly** 

**facilitating downstream usage. As a highlight,** **_Chinchilla_ reaches a state-of-the-art average accuracy of** 

**67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_ .**

---

[referencia=46fd66187ec3e6ae score=0.134]
### **4.** **_Chinchilla_** 

Based on our analysis in Section 3, the optimal model size for the _Gopher_ compute budget is somewhere between 40 and 70 billion parameters. We test this hypothesis by training a model on the larger end of this range—70B parameters—for 1.4T tokens, due to both dataset and computational efficiency considerations. In this section we compare this model, which we call _Chinchilla_ , to _Gopher_ and other LLMs. Both _Chinchilla_ and _Gopher_ have been trained for the same number of FLOPs but differ in the size of the model and the number of training tokens. 

While pre-training a large language model has a considerable compute cost, downstream finetuning and inference also make up substantial compute usage (Rae et al., 2021). Due to being 4× smaller than _Gopher_ , both the memory footprint and inference cost of _Chinchilla_ are also smaller.

---

[referencia=46fd66187ec3e6ae score=0.115]
The functions _𝑁𝑜𝑝𝑡_ ( _𝐶_ ), and _𝐷𝑜𝑝𝑡_ ( _𝐶_ ) describe the optimal allocation of a computational budget _𝐶_ . We empirically estimate these functions based on the losses of over 400 models, ranging from under 70M to over 16B parameters, and trained on 5B to over 400B tokens – with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ in Section 2. 

Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train _Gopher_ , an optimal model should be 4 times smaller, while being training on 4 times more tokens. We verify this by training a more _compute-optimal_ 70B model, called _Chinchilla_ , on 1.4 trillion tokens. Not only does _Chinchilla_ outperform its much larger counterpart, _Gopher_ , but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware. The energy cost of a large language model is amortized through its usage for inference an fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the immediate benefits of its improved performance. 

> 1For example, knowing the number of accelerators and a target training duration. 

> 2For simplicity, we perform our analysis on the smoothed training loss which is an unbiased estimate of the test loss, as we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus). 

2 

Table 1 | **Current LLMs** . We show five of the current largest dense transformer models, their size, and the number of training tokens. Other than LaMDA (Thoppilan et al., 2022), most models are trained for approximately 300 billion tokens. We introduce _Chinchilla_ , a substantially smaller model, trained for much longer than 300B tokens.

---

[referencia=46fd66187ec3e6ae score=0.002]
### **E. Curvature of the FLOP-loss frontier** 

- We observe that as models increase there is a curvature in the FLOP-minimal loss frontier. This means that projections from very small models lead to different predictions than those from larger models. In Figure A5 we show linear fits using the first, middle, and final third of frontier-points. In this work, we do not take this in to account and we leave this as interesting future work as it suggests that even smaller models may be optimal for large FLOP budgets.

---

[referencia=46fd66187ec3e6ae score=0.001]
### **2. Related Work** 

**Large language models.** A variety of large language models have been introduced in the last few years. These include both dense transformer models (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022) and mixture-of-expert (MoE) models (Du et al., 2021; Fedus et al., 2021; Zoph et al., 2022). The largest dense transformers have passed 500 billion parameters (Smith et al., 2022). The drive to train larger and larger models is clear—so far increasing the size of language models has been responsible for improving the state-of-the-art in many language modelling tasks. Nonetheless, large language models face several challenges, including their overwhelming computational requirements (the cost of training and inference increase with model size) (Rae et al., 2021; Thoppilan et al., 2022) and the need for acquiring more high-quality training data. In fact, in this work we find that larger, high quality datasets will play a key role in any further scaling of language models.

---

[referencia=46fd66187ec3e6ae score=0.001]
|misconceptions|65.3|61.7|logical_sequence|64.1|36.4|
|implicatures|75.0|62.0|mathematical_induction|47.3|57.6|
|disambiguation_q|54.7|45.5|fantasy_reasoning|69.0|64.1|
|known_unknowns|65.2|63.6|SNARKS|58.6|48.3|
|darkhumordetection|66.2|83.1|crassai|75.0|56.8|
|__<br>analogical_similarity|38.1|17.2|_<br>entailed_polarity|94.0|89.5|
|sentence_ambiguity|71.7|69.1|irony_identifcation|73.0|69.7|
|riddle_sense|85.7|68.2|evaluating_info_essentiality|17.6|16.7|
|date_understanding|52.3|44.1|phrase_relatedness|94.0|81.8|
|analyticentailment|67.1|53.0|novelconcepts|65.6|59.1|
|_<br>odd_one_out|70.9|32.5|_<br>empirical_judgments|67.7|52.5|
|logical_args|56.2|59.1|fgure_of_speech_detection|63.3|52.7|
|alignment_questionnaire|91.3|79.2|english_proverbs|82.4|57.6|
|similarities_abstraction|87.0|81.8|Human_organs_senses_mcc|85.7|84.8|
|anachronisms|69.1|56.4|gre_reading_comprehension|53.1|27.3|



Table A7 | **_Chinchilla_ BIG-bench results.** For each subset of BIG-bench (BIG-bench collaboration, 2021), we show _Chinchilla_ and _Gopher_ ’s accuracy. 

35

---

[referencia=46fd66187ec3e6ae score=0.001]
|Parameters (million)<br>|d_model|fw_size|kv_size|n_heads|n_layers|
|---|---|---|---|---|---|
|44|512|2048|64|8|8|
|57|576|2304|64|9|9|
|74|640|2560|64|10|10|
|90|640|2560|64|10|13|
|106|640|2560|64|10|16|
|117|768|3072|64|12|12|
|140|768|3072|64|12|15|
|163|768|3072|64|12|18|
|175|896|3584|64|14|14|
|196|896|3584|64|14|16|
|217|896|3584|64|14|18|
|251|1024|4096|64|16|16|
|278|1024|4096|64|16|18|
|306|1024|4096|64|16|20|
|425|1280|5120|128|10|18|
|489|1280|5120|128|10|21|
|509|1408|5632|128|11|18|
|552|1280|5120|128|10|24|
|587|1408|5632|128|11|21|
|632|1536|6144|128|12|19|
|664|1408|5632|128|11|24|
|724|1536|6144|128|12|22|
|816|1536|6144|128|12|25|
|893|1792|7168|128|14|20|
|1,018|1792|7168|128|14|23|
|1,143|1792|7168|128|14|26|
|1,266|2048|8192|128|16|22|
|1,424|2176|8704|128|17|22|
|1,429|2048|8192|128|16|25|
|1,593|2048|8192|128|16|28|
|1,609|2176|8704|128|17|25|

---

[referencia=46fd66187ec3e6ae score=0.001]
- J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei. Scaling laws for neural language models. <u>arXiv preprint arXiv:2001.08361, 2020.</u> 

- D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. <u>arXiv preprint arXiv:1412.6980,</u> 2014. 

- T. Kudo and J. Richardson. SentencePiece: A simple and language independent subword tokenizer and detokenizer for neural text processing. <u>arXiv preprint arXiv:1808.06226, 2018.</u> 

- T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin, M. Kelcey, J. Devlin, K. Lee, K. N. Toutanova, L. Jones, M.-W. Chang, A. Dai, J. Uszkoreit, Q. Le, and S. Petrov. Natural questions: a benchmark for question answering research. <u>Transactions of the Association of Computational Linguistics, 2019.</u> 

- G. Lai, Q. Xie, H. Liu, Y. Yang, and E. Hovy. RACE: Large-scale ReAding comprehension dataset from examinations. In <u>Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing, pages 785–794, Copenhagen, Denmark, Sept. 2017. Association for Computational</u> Linguistics. doi: 10.18653/v1/D17-1082. URL `https://aclanthology.org/D17-1082` . 

- Y. Levine, N. Wies, O. Sharir, H. Bata, and A. Shashua. The depth-to-width interplay in self-attention. <u>arXiv preprint arXiv:2006.12467, 2020.</u>

---

[referencia=46fd66187ec3e6ae score=0.001]
### **F. FLOPs computation** 

- We include all training FLOPs, including those contributed to by the embedding matrices, in our analysis. Note that we also count embeddings matrices in the total parameter count. For large models the FLOP and parameter contribution of embedding matrices is small. We use a factor of 2 to describe the multiply accumulate cost. For the forward pass, we consider contributions from: 

   - Embeddings 

      - 2 × seq_len × vocab_size × d_model 

   - Attention (Single Layer) 

      - **Key, query and value projections** : 2 × 3 × seq_len × d_model × (key_size × num_heads) 

27 



<!-- Start of picture text -->
10000<br>6.0<br>5.5 5000<br>5.0<br>2500<br>4.5<br>4.0<br>1000<br>3.5<br>3.0 500<br>2.5 250<br>2.0<br>75<br>10 17 10 18 10 19 10 20 10 21 10 22<br>FLOPS<br>Training loss<br>Million Parameters<br><!-- End of picture text -->

Figure A5 | **Training curve envelopes.** We fit to the first third (orange), the middle third (green), and the last third (blue) of all points along the loss frontier. We plot only a subset of the points. 

   - **Key @ Query logits** : 2 × seq_len × seq_len × (key_size × num_heads) 

   - **Softmax** : 3 × num_heads × seq_len × seq_len 

   - **Softmax @ query reductions** : 2 × seq_len × seq_len × (key_size × num_heads) 

   - **Final Linear** : 2 × seq_len × (key_size × num_heads) × d_model 

- Dense Block (Single Layer) 

   - 2 × seq_len × (d_model × ffw_size + d_model × ffw_size) 

- Final Logits 

   - 2 × seq_len × d_model × vocab_size 

- **Total forward pass FLOPs:** embeddings+num_layers×(total_attention+dense_block) + logits

---

[referencia=46fd66187ec3e6ae score=0.001]
**Estimating hyperparameters for large models.** The model size and the number of training tokens are not the only two parameters to chose when selecting a language model and a procedure to train it. Other important factors include learning rate, learning rate schedule, batch size, optimiser, and width-to-depth ratio. In this work, we focus on model size and the number of training steps, and we rely on existing work and provided experimental heuristics to determine the other necessary hyperparameters. Yang et al. (2021) investigates how to choose a variety of these parameters for training an autoregressive transformer, including the learning rate and batch size. McCandlish et al. (2018) finds only a weak dependence between optimal batch size and model size. Shallue et al. (2018); Zhang et al. (2019) suggest that using larger batch-sizes than those we use is possible. Levine et al. (2020) investigates the optimal depth-to-width ratio for a variety of standard model sizes. We use slightly less deep models than proposed as this translates to better wall-clock performance on our hardware. 

**Improved model architectures.** Recently, various promising alternatives to traditional dense transformers have been proposed. For example, through the use of conditional computation large MoE models like the 1.7 trillion parameter Switch transformer (Fedus et al., 2021), the 1.2 Trillion parameter GLaM model (Du et al., 2021), and others (Artetxe et al., 2021; Zoph et al., 2022) are able to provide a large effective model size despite using relatively fewer training and inference FLOPs. However, for very large models the computational benefits of routed models seems to diminish (Clark et al., 2022). An orthogonal approach to improving language models is to augment transformers with explicit retrieval mechanisms, as done by Borgeaud et al. (2021); Guu et al. (2020); Lewis et al. (2020). This approach effectively increases the number of data tokens seen during training (by a factor of ∼ 10 in Borgeaud et al. (2021)). This suggests that the performance of language models may be more dependant on the size of the training data than previously thought.

---

[referencia=46fd66187ec3e6ae score=0.001]
||_Chinchilla_|_Gopher_|GPT-3|MT-NLG 530B|
|---|---|---|---|---|
|LAMBADA Zero-Shot|**77.4**|74.5|76.2|76.6|
|RACE-m Few-Shot|**86.8**|75.1|58.1|-|
|RACE-h Few-Shot|**82.3**|71.6|46.8|47.9|



Table 7 | **Reading comprehension.** On RACE-h and RACE-m (Lai et al., 2017), _Chinchilla_ considerably improves performance over _Gopher_ . Note that GPT-3 and MT-NLG 530B use a different prompt format than we do on RACE-h/m, so results are not comparable to _Gopher_ and _Chinchilla_ . On LAMBADA (Paperno et al., 2016), _Chinchilla_ outperforms both _Gopher_ and MT-NLG 530B. 

`mathematical_induction` and `logical_args` . Full accuracy results for _Chinchilla_ can be found in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.001]
#### **D.4. Small-scale comparison to Kaplan** **_et al._ (2020)** 

For 10<sup>21</sup> FLOPs, we perform a head-to-head comparison of a model predicted by Approach 1 and that predicted by Kaplan et al. (2020). For both models, we use a batch size of 0.5M tokens and a 

26 

|maximum learning rate of 1_._5×10<sup>−4 </sup>that decays by 10×. FromKaplan et al.(2020), we fnd that<br>the optimal model size should be 4.68 billion parameters. From our approach 1, we estimate a 2.86<br>billion parameter model should be optimal. We train a 4.74 billion parameter and a 2.80 billion<br>parameter transformer to test this hypothesis, using the same depth-to-width ratio to avoid as many<br>confounding factors as possible. We fnd that our predicted model outperforms the model predicted<br>byKaplan et al.(2020) as shown inFigure A4.|
|---|
|2.3<br>2.4<br>2.5<br>2.6<br>2.7<br>2.8<br>Training Loss<br>2.3<br>2.4<br>2.5<br>2.6<br>2.7<br>2.8<br>Training Loss<br>Kaplan et al (2020)<br>Approach 1|
|0<br>1<br>2<br>Sequences<br>1e7<br>2.2<br>0.0<br>0.2<br>0.4<br>0.6<br>0.8<br>1.0<br>FLOPs ×10<sup>21</sup><br>2.2|



- Figure A4 | **Comparison to Kaplan et al. (2020) at** 10<sup>21</sup> **FLOPs.** We train 2.80 and 4.74 billion parameter transformers predicted as optimal for 10<sup>21</sup> FLOPs by Approach 1 and by Kaplan et al. (2020). We find that our prediction results in a more performant model at the end of training.

---

[referencia=46fd66187ec3e6ae score=0.001]
#### **H.1. The Pile** 

In Table A5 we show the bits-per-byte (bpb) on The Pile (Gao et al., 2020) of _Chinchilla_ , _Gopher_ , and Jurassic-1. _Chinchilla_ outperforms _Gopher_ on all subsets. Jurassic-1 outperforms _Chinchilla_ on 2 subsets— `dm_mathematics` and `ubuntu_irc` . 

29 

|Subset|_Chinchilla_(70B)|_Gopher_(280B)|Jurassic-1 (170B)|
|---|---|---|---|
|pile_cc|**0.667**|0.691|0.669|
|pubmed_abstracts|**0.559**|0.578|0.587|
|stackexchange|**0.614**|0.641|0.655|
|github|**0.337**|0.377|0.358|
|openwebtext2|**0.647**|0.677|-|
|arxiv|**0.627**|0.662|0.680|
|uspto_backgrounds|**0.526**|0.546|0.537|
|freelaw|**0.476**|0.513|0.514|
|pubmed_central|**0.504**|0.525|0.579|
|dm_mathematics|1.111|1.142|**1.037**|
|hackernews|**0.859**|0.890|0.869|
|nih_exporter|**0.572**|0.590|0.590|
|opensubtitles|**0.871**|0.900|0.879|
|europarl|**0.833**|0.938|-|
|books3|**0.675**|0.712|0.835|
|philpapers|**0.656**|0.695|0.742|
|gutenberg_pg_19|**0.548**|0.656|0.890|
|bookcorpus2|**0.714**|0.741|-|
|ubuntu_irc|1.026|1.090|**0.857**|

---

[referencia=46fd66187ec3e6ae score=0.001]
- G. Zhang, L. Li, Z. Nado, J. Martens, S. Sachdeva, G. Dahl, C. Shallue, and R. B. Grosse. Which algorithmic choices matter at which batch sizes? insights from a noisy quadratic model. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett, editors, <u>Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019.</u> URL `https: //proceedings.neurips.cc/paper/2019/file/e0eacd983971634327ae1819ea8b621 4-Paper.pdf` . 

- B. Zoph, I. Bello, S. Kumar, N. Du, Y. Huang, J. Dean, N. Shazeer, and W. Fedus. Designing effective sparse expert models, 2022. 

21

---

[referencia=46fd66187ec3e6ae score=0.001]
<!-- Start of picture text -->
2.8 30.0<br>27.5 0.6<br>2.7<br>25.0 0.5<br>2.6 22.5 0.4<br>20.0 0.3<br>2.5 17.5<br>0.2<br>417M, Adam<br>2.4 15.0 0.1 417M, AdamW<br>12.5 1.4B, Adam<br>0.0 1.4B, AdamW<br>2.3 10.0<br>0 25 50 75 100 125 150 0 25 50 75 100 125 150 0 25 50 75 100 125 150<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>LAMBADA Accuracy<br>Wikitext103 Perplexity<br><!-- End of picture text -->

Figure A7 | **Adam vs AdamW.** For a 417M (blue) and 1.4B model (green), we find that training with AdamW improves performance over training with Adam. 

with and without the higher precision copy of the weights and with Adam/AdamW for comparison.

---

[referencia=46fd66187ec3e6ae score=0.001]
|1,593|2048|8192|128|16|28|
|1,609|2176|8704|128|17|25|
|1,731|2304|9216|128|18|24|
|1,794|2176|8704|128|17|28|
|2,007|2304|9216|128|18|28|
|2,283|2304|9216|128|18|32|
|2,298|2560|10240|128|20|26|
|2,639|2560|10240|128|20|30|
|2,980|2560|10240|128|20|34|
|3,530|2688|10752|128|22|36|
|3,802|2816|11264|128|22|36|
|4084|2944|11776|128|22|36|
|,<br>4516|3072|12288|128|24|36|
|,<br>6,796|3584|14336|128|28|40|
|9,293|4096|16384|128|32|42|
|11,452|4352|17408|128|32|47|
|12,295|4608|18432|128|36|44|
|12,569|4608|18432|128|32|47|
|13,735|4864|19456|128|32|47|
|14,940|4992|19968|128|32|49|
|16,183|5120|20480|128|40|47|



Table A9 | **All models.** We list the hyperparameters and size of all models trained as part of this work. Many shown models have been trained with multiple learning rate schedules/number of training tokens. 

36

---

[referencia=46fd66187ec3e6ae score=0.000]
22 



<!-- Start of picture text -->
3.00 3.20<br>1.0 Cosine Cycle Length<br>2.95 3.15 1.0× num. steps<br>0.8 3.10 1.1× num. steps<br>1.25× num. steps<br>2.90<br>3.05 1.5× num. steps<br>0.6 2.0× num. steps<br>2.85 3.00 5.0× num. steps<br>0.4<br>2.95<br>2.80<br>0.2 2.90<br>2.75<br>2.85<br>0.0<br>2.70 2.80<br>0 2 4 6 8 0 2 4 6 8 0 2 4 6<br>Million Sequences Million Sequences Million Sequences<br>3.00 3.20<br>1.0<br>3.15<br>2.95<br>0.8 3.10<br>2.90<br>3.05<br>0.6<br>2.85 3.00<br>0.4<br>2.95<br>2.80<br>0.2 2.90<br>2.75<br>2.85<br>0.0<br>2.70 2.80<br>0.0 2.5 5.0 7.5 10.0 12.5 0.0 2.5 5.0 7.5 10.0 12.5 0.0 2.5 5.0 7.5 10.0 12.5<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>Training Loss<br>Learning Rate/Max LR<br>C4 Loss<br>Training Loss<br>Learning Rate/Max LR<br><!-- End of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.000]
> 10This further emphasises the point of not only determining model size, but also training length before training begins. 

24 

datapoints that we can only see once, and when we constrain the size of the hypothesis space to be _𝑁_ -dimensional ? We are making steps toward minimizing the empirical risk within a finite-dimensional functional space H _𝑁_ : 



We are never able to obtain _𝑓_<sup>ˆ</sup> _𝑁,𝐷_ as we typically perform a single epoch over the dataset of size _𝐷_ . Instead, be obtain _𝑓_<sup>¯</sup> _𝑁,𝐷_ , which is the result of applying a certain number of gradient steps based on the _𝐷_ datapoints—the number of steps to perform depends on the gradient batch size, for which we use well-tested heuristics. 

Using the Bayes-classifier _𝑓_<sup>_★_</sup> , the expected-risk minimizer _𝑓𝑁_ and the “single-epoch empirical-risk minimizer” _𝑓_<sup>¯</sup> _𝑁,𝐷_ , we can finally decompose the loss _𝐿_ ( _𝑁, 𝐷_ ) into 



The loss comprises three terms: the Bayes risk, i.e. the minimal loss achievable for next-token prediction on the full distribution _𝑃_ , a.k.a the “entropy of natural text.”; a functional approximation term that depends on the size of the hypothesis space; finally, a stochastic approximation term that captures the suboptimality of minimizing _𝐿_<sup>ˆ</sup> _𝐷_ instead of _𝐿_ , and of making a single epoch on the provided dataset.

---

[referencia=46fd66187ec3e6ae score=0.000]
12 



<!-- Start of picture text -->
120<br>100<br>80<br>60<br>40<br>20<br>0<br>20<br> over Gopher<br>Relative Improvement<br>crash_blossomdark_humor_detectionmathematical_inductionlogical_argsgeneral_knowledge_jsonHuman_organs_senses_multiple_choiceformal_fallacies_syllogisms_negationknown_unknownsnavigatesentence_ambiguitymoral_permissibilityintent_recognitionirony_identificationentailed_polarityhyperbatonmisconceptionsevaluating_information_essentialitysimilarities_abstractionepistemic_reasoningfantasy_reasoningmovie_dialog_same_or_differentwinowhynovel_conceptsdiscourse_marker_prediction strategyqacausal_judgmenthindu_knowledgephrase_relatednessalignment_questionnairereasoning_about_colored_objectsdate_understandingpenguins_in_a_tablefigure_of_speech_detectiondisambiguation_qimplicaturesSNARKS ruin_nameslogical_fallacy_detectionanachronisms logic_grid_puzzleriddle_senseanalytic_entailmentquestion_selectionnonsense_words_grammarphysics_mcempirical_judgmentssports_understandingcrass_aiphysical_intuitiontimedial implicit_relationsenglish_proverbspresuppositions_as_nlimovie_recommendationunderstanding_fablesmetaphor_booleantemporal_sequenceslogical_sequenceidentify_odd_metaphorgre_reading_comprehensionodd_one_outanalogical_similarity<br><!-- End of picture text -->

Figure 7 | **BIG-bench results compared to** **_Gopher_** _Chinchilla_ out performs _Gopher_ on all but four BIG-bench tasks considered. Full results are in Table A7.

---

[referencia=46fd66187ec3e6ae score=0.000]
Figure 4 | **Parametric fit.** We fit a parametric modelling of the loss _𝐿_<sup>ˆ</sup> ( _𝑁, 𝐷_ ) and display contour ( **left** ) and isoFLOP slices ( **right** ). For each isoFLOP slice, we include a corresponding dashed line in the left plot. In the left plot, we show the efficient frontier in blue, which is a line in log-log space. Specifically, the curve goes through each iso-loss contour at the point with the fewest FLOPs. We project the optimal model size given the _Gopher_ FLOP budget to be 40B parameters. 

**Efficient frontier.** We can approximate the functions _𝑁𝑜𝑝𝑡_ and _𝐷𝑜𝑝𝑡_ by minimizing the parametric loss _𝐿_<sup>ˆ</sup> under the constraint FLOPs( _𝑁, 𝐷_ ) ≈ 6 _𝑁𝐷_ (Kaplan et al., 2020). The resulting _𝑁𝑜𝑝𝑡_ and _𝐷𝑜𝑝𝑡_ balance the two terms in Equation (3) that depend on model size and data. By construction, they have a power-law form: 



We show contours of the fitted function _𝐿_<sup>ˆ</sup> in Figure 4 (left), and the closed-form efficient computational frontier in blue. From this approach, we find that _𝑎_ = 0 _._ 46 and _𝑏_ = 0 _._ 54—as summarized in Table 2.