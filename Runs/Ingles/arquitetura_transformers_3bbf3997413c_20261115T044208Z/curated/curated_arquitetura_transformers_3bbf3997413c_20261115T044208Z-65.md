[referencia=46fd66187ec3e6ae score=0.984]
## **Training Compute-Optimal Large Language Models** 

**Jordan Hoffmann**<sup>_★_</sup> **, Sebastian Borgeaud**<sup>_★_</sup> **, Arthur Mensch**<sup>_★_</sup> **, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre**<sup>_★_</sup> 

> _★_ Equal contributions 

**We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model,** **_Chinchilla_ , that uses the same compute budget as** **_Gopher_ but with 70B parameters and 4** × **more more data.** **_Chinchilla_ uniformly and significantly outperforms** **_Gopher_ (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that** **_Chinchilla_ uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight,** **_Chinchilla_ reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_ .**

---

[referencia=46fd66187ec3e6ae score=0.982]
_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved 



<!-- Start of picture text -->
1T<br>Approach 1<br>100B<br>Approach 2<br>Approach 3<br>Kaplan et al (2020)<br>10B<br>Chinchilla (70B)<br>1.0B Gopher (280B)<br>GPT-3 (175B)<br>Megatron-Turing NLG (530B)<br>100M<br>10M<br>10 17 10 19 10 21 10 23 10 25<br>FLOPs<br>Parameters<br><!-- End of picture text -->

Figure 1 | **Overlaid predictions.** We overlay the predictions from our three different approaches, along with projections from Kaplan et al. (2020). We find that all three methods predict that current large models should be substantially smaller and therefore trained much longer than is currently done. In Figure A3, we show the results with the predicted optimal tokens plotted against the optimal number of parameters for fixed FLOP budgets. **_Chinchilla_ outperforms** **_Gopher_ and the other large models (see Section 4.2).** 

In this work, we revisit the question: _Given a fixed FLOPs budget,_<sup>1</sup> _how should one trade-off model size and the number of training tokens?_ To answer this question, we model the final pre-training loss<sup>2</sup> _𝐿_ ( _𝑁, 𝐷_ ) as a function of the number of model parameters _𝑁_ , and the number of training tokens, _𝐷_ . Since the computational budget _𝐶_ is a deterministic function FLOPs( _𝑁, 𝐷_ ) of the number of seen training tokens and model parameters, we are interested in minimizing _𝐿_ under the constraint FLOPs( _𝑁, 𝐷_ ) = _𝐶_ :

---

[referencia=46fd66187ec3e6ae score=0.978]
### **5. Discussion & Conclusion** 

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget. 

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that _Gopher_ is substantially over-sized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training _Chinchilla_ , a 70B parameter model, and show that it outperforms _Gopher_ and even larger models on nearly every measured evaluation task. 

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale ( _Chinchilla_ and _Gopher_ ), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log<sup>�</sup> _𝑁𝑜𝑝𝑡_ � at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of _Chinchilla_ to _Gopher_ validates our performance predictions, that have thus enabled training a better (and more 

15

---

[referencia=46fd66187ec3e6ae score=0.973]
### **1. Introduction** 

Recently a series of _Large Language Models_ (LLMs) have been introduced (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022), with the largest dense language models now having over 500 billion parameters. These large autoregressive transformers (Vaswani et al., 2017) have demonstrated impressive performance on many tasks using a variety of evaluation protocols such as zero-shot, few-shot, and fine-tuning. 

The compute and energy cost for training large language models is substantial (Rae et al., 2021; Thoppilan et al., 2022) and rises with increasing model size. In practice, the allocated training compute budget is often known in advance: how many accelerators are available and for how long we want to use them. Since it is typically only feasible to train these large models once, accurately estimating the best model hyperparameters for a given compute budget is critical (Tay et al., 2021). 

Kaplan et al. (2020) showed that there is a power law relationship between the number of parameters in an autoregressive language model (LM) and its performance. As a result, the field has been training larger and larger models, expecting performance improvements. One notable conclusion in Kaplan et al. (2020) is that large models should not be trained to their lowest possible loss to be compute optimal. Whilst we reach the same conclusion, we estimate that large models should be trained for many more training tokens than recommended by the authors. Specifically, given a 10× increase computational budget, they suggests that the size of the model should increase 5 _._ 5× while the number of training tokens should only increase 1.8×. Instead, we find that model size and the number of training tokens should be scaled in equal proportions. 

Following Kaplan et al. (2020) and the training setup of GPT-3 (Brown et al., 2020), many of the recently trained large models have been trained for approximately 300 billion tokens (Table 1), in line with the approach of predominantly increasing model size when increasing compute. 

_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved

---

[referencia=46fd66187ec3e6ae score=0.964]
**Modelling the scaling behavior.** Understanding the scaling behaviour of language models and their transfer properties has been important in the development of recent large models (Hernandez et al., 2021; Kaplan et al., 2020). Kaplan et al. (2020) first showed a predictable relationship between model size and loss over many orders of magnitude. The authors investigate the question of choosing the optimal model size to train for a given compute budget. Similar to us, they address this question by training various models. Our work differs from Kaplan et al. (2020) in several important ways. First, the authors use a fixed number of training tokens and learning rate schedule for all models; this prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find that setting the learning rate schedule to approximately match the number of training tokens results in the best final loss regardless of model size—see Figure A1. For a fixed learning rate cosine schedule to 130B tokens, the intermediate loss estimates (for _𝐷_<sup>′</sup> _<<_ 130B) are therefore overestimates of the loss of a model trained with a schedule length matching _𝐷_<sup>′</sup> . Using these intermediate losses results in underestimating the effectiveness of training models on less data than 130B tokens, and eventually contributes to the conclusion that model size should increase faster than training data size as compute budget increases. In contrast, our analysis predicts that both quantities should scale at roughly the same rate. Secondly, we include models with up to 16B parameters, as we observe that there is slight curvature in the FLOP-loss frontier (see Appendix E)—in fact, the majority of the models used in our analysis have more than 500 million parameters, in contrast the majority of runs in Kaplan et al. (2020) are significantly smaller—many being less than 100M parameters. 

Recently, Clark et al. (2022) specifically looked in to the scaling properties of Mixture of Expert 

3 

language models, showing that the scaling with number of experts diminishes as the model size increases—their approach models the loss as a function of two variables: the model size and the number of experts. However, the analysis is done with a fixed number of training tokens, as in Kaplan et al. (2020), potentially underestimating the improvements of branching.

---

[referencia=46fd66187ec3e6ae score=0.932]
### **4.** **_Chinchilla_** 

Based on our analysis in Section 3, the optimal model size for the _Gopher_ compute budget is somewhere between 40 and 70 billion parameters. We test this hypothesis by training a model on the larger end of this range—70B parameters—for 1.4T tokens, due to both dataset and computational efficiency considerations. In this section we compare this model, which we call _Chinchilla_ , to _Gopher_ and other LLMs. Both _Chinchilla_ and _Gopher_ have been trained for the same number of FLOPs but differ in the size of the model and the number of training tokens. 

While pre-training a large language model has a considerable compute cost, downstream finetuning and inference also make up substantial compute usage (Rae et al., 2021). Due to being 4× smaller than _Gopher_ , both the memory footprint and inference cost of _Chinchilla_ are also smaller.

---

[referencia=46fd66187ec3e6ae score=0.927]
The functions _𝑁𝑜𝑝𝑡_ ( _𝐶_ ), and _𝐷𝑜𝑝𝑡_ ( _𝐶_ ) describe the optimal allocation of a computational budget _𝐶_ . We empirically estimate these functions based on the losses of over 400 models, ranging from under 70M to over 16B parameters, and trained on 5B to over 400B tokens – with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ in Section 2. 

Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train _Gopher_ , an optimal model should be 4 times smaller, while being training on 4 times more tokens. We verify this by training a more _compute-optimal_ 70B model, called _Chinchilla_ , on 1.4 trillion tokens. Not only does _Chinchilla_ outperform its much larger counterpart, _Gopher_ , but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware. The energy cost of a large language model is amortized through its usage for inference an fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the immediate benefits of its improved performance. 

> 1For example, knowing the number of accelerators and a target training duration. 

> 2For simplicity, we perform our analysis on the smoothed training loss which is an unbiased estimate of the test loss, as we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus). 

2 

Table 1 | **Current LLMs** . We show five of the current largest dense transformer models, their size, and the number of training tokens. Other than LaMDA (Thoppilan et al., 2022), most models are trained for approximately 300 billion tokens. We introduce _Chinchilla_ , a substantially smaller model, trained for much longer than 300B tokens.

---

[referencia=46fd66187ec3e6ae score=0.908]
Table 3 | **Estimated optimal training FLOPs and training tokens for various model sizes.** For various model sizes, we show the projections from Approach 1 of how many FLOPs and training tokens would be needed to train compute-optimal models. The estimates for Approach 2 & 3 are similar (shown in Section D.3) 

Parameters FLOPs FLOPs (in _Gopher_ unit) Tokens 400 Million 1.92e+19 1/29 _,_ 968 8.0 Billion 

1 Billion 1.21e+20 1/4 _,_ 761 20.2 Billion 10 Billion 1.23e+22 1/46 205.1 Billion 67 Billion 5.76e+23 1 1.5 Trillion . 175 Billion 3.85e+24 6 _._ 7 3.7 Trillion 280 Billion 9.90e+24 17 _._ 2 5.9 Trillion 520 Billion 3.43e+25 59 _._ 5 11.0 Trillion 1 Trillion 1.27e+26 221 _._ 3 21.2 Trillion 10 Trillion 1.30e+28 22515 _._ 9 216.2 Trillion 

large language models are considerably over-sized, given their respective compute budgets, as shown in Figure 1. For example, we find that a 175 billion parameter model should be trained with a compute budget of 4 _._ 41 × 10<sup>24</sup> FLOPs and on over 4.2 trillion tokens. A 280 billion _Gopher_ -like model is the optimal model to train given a compute budget of approximately 10<sup>25</sup> FLOPs and should be trained on 6.8 trillion tokens. Unless one has a compute budget of 10<sup>26</sup> FLOPs (over 250× the compute used to 

train _Gopher_ ), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale. While there is significant uncertainty extrapolating out

---

[referencia=46fd66187ec3e6ae score=0.885]
#### **3.1. Approach 1: Fix model sizes and vary number of training tokens** 

In our first approach we vary the number of training steps for a fixed family of models (ranging from 70M to over 10B parameters), training each model for 4 different number of training sequences. From these runs, we are able to directly extract an estimate of the minimum loss achieved for a given number of training FLOPs. Training details for this approach can be found in Appendix D. 

For each parameter count _𝑁_ we train 4 different models, decaying the learning rate by a factor of 10× over a horizon (measured in number of training tokens) that ranges by a factor of 16×. Then, for each run, we smooth and then interpolate the training loss curve. From this, we obtain a continuous mapping from FLOP count to training loss for each run. Then, for each FLOP count, we determine which run achieves the lowest loss. Using these interpolants, we obtain a mapping from any FLOP count _𝐶_ , to the most efficient choice of model size _𝑁_ and number of training tokens _𝐷_ such that FLOPs( _𝑁, 𝐷_ ) = _𝐶_ .<sup>4</sup> At 1500 logarithmically spaced FLOP values, we find which model size achieves the lowest loss of all models along with the required number of training tokens. Finally, we fit power laws to estimate the optimal model size and number of training tokens for any given amount of compute (see the center and right panels of Figure 2), obtaining a relationship _𝑁𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑎_</sup> and _𝐷𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑏_</sup> . We find that _𝑎_ = 0 _._ 50 and _𝑏_ = 0 _._ 50—as summarized in Table 2. In Section D.4, we show a head-to-head comparison at 10<sup>21</sup> FLOPs, using the model size recommended by our analysis and by the analysis of Kaplan et al. (2020)—using the model size we predict has a clear advantage.

---

[referencia=46fd66187ec3e6ae score=0.873]
|Model|Size (# Parameters)|Training Tokens|
|---|---|---|
|LaMDA (Thoppilan et al.,2022)|137 Billion|168 Billion|
|GPT-3 (Brown et al.,2020)|175 Billion|300 Billion|
|Jurassic (Lieber et al.,2021)|178 Billion|300 Billion|
|_Gopher_(Rae et al.,2021)|280 Billion|300 Billion|
|MT-NLG 530B (Smith et al.,2022)|530 Billion|270 Billion|
|_Chinchilla_|70 Billion|1.4 Trillion|

---

[referencia=46fd66187ec3e6ae score=0.868]
### **2. Related Work** 

**Large language models.** A variety of large language models have been introduced in the last few years. These include both dense transformer models (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022) and mixture-of-expert (MoE) models (Du et al., 2021; Fedus et al., 2021; Zoph et al., 2022). The largest dense transformers have passed 500 billion parameters (Smith et al., 2022). The drive to train larger and larger models is clear—so far increasing the size of language models has been responsible for improving the state-of-the-art in many language modelling tasks. Nonetheless, large language models face several challenges, including their overwhelming computational requirements (the cost of training and inference increase with model size) (Rae et al., 2021; Thoppilan et al., 2022) and the need for acquiring more high-quality training data. In fact, in this work we find that larger, high quality datasets will play a key role in any further scaling of language models.

---

[referencia=46fd66187ec3e6ae score=0.857]
#### **3.4. Optimal model scaling** 

We find that the three approaches, despite using different fitting methodologies and different trained models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs (shown in Table 2). All three approaches suggest that as compute budget increases, model size and the amount of training data should be increased in approximately equal proportions. The first and second approaches yield very similar predictions for optimal model sizes, as shown in Figure 1 and Figure A3. The third approach predicts even smaller models being optimal at larger compute budgets. We note that the observed points ( _𝐿, 𝑁, 𝐷_ ) for low training FLOPs ( _𝐶_ ⩽ 1 _𝑒_ 21) have larger residuals 2 ∥ _𝐿_ − _𝐿_<sup>ˆ</sup> ( _𝑁, 𝐷_ )∥2<sup>thanpointswithhighercomputationalbudgets.Thefittedmodelplacesincreased</sup> weight on the points with more FLOPs—automatically considering the low-computational budget points as outliers due to the Huber loss. As a consequence of the empirically observed negative curvature in the frontier _𝐶_ → _𝑁𝑜𝑝𝑡_ (see Appendix E), this results in predicting a lower _𝑁𝑜𝑝𝑡_ than the two other approaches. 

In Table 3 we show the estimated number of FLOPs and tokens that would ensure that a model of a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of 

7

---

[referencia=46fd66187ec3e6ae score=0.844]
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

[referencia=46fd66187ec3e6ae score=0.834]
### **G. Other differences between** **_Chinchilla_ and** **_Gopher_** 

Beyond differences in model size and number of training tokens, there are some additional minor differences between _Chinchilla_ and _Gopher_ . Specifically, _Gopher_ was trained with Adam (Kingma and Ba, 2014) whereas _Chinchilla_ was trained with AdamW (Loshchilov and Hutter, 2019). Furthermore, as discussed in _Lessons Learned_ in Rae et al. (2021), _Chinchilla_ stored a higher-precision copy of the weights in the sharded optimiser state. 

We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7. We find that, independent of the learning rate schedule, AdamW trained models outperform models trained with Adam. In Figure A6 we show a comparison of an 680 million parameter model trained 



<!-- Start of picture text -->
2.70 26 3.00<br>Training Setup<br>25 2.95 Adam w/ High Precision<br>2.65 24 2.90 AdamW w/ High Precision<br>Adam No High Precision<br>23<br>2.60 2.85 AdamW No High Precision<br>22<br>2.80<br>21<br>2.55 2.75<br>20<br>2.50 19 2.70<br>18 2.65<br>2.45 17 2.60<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>Training Loss<br>Wikitext103 Perplexity<br><!-- End of picture text -->

Figure A6 | **Comparison of other differences.** Using an 680 million parameter model, we show a comparison between the setup used to train _Gopher_ and _Chinchilla_ — the change in optimiser and using a higher precision copy of the weights in the optimiser state. The setup used for _Chinchilla_ (orange) clearly outperforms the setup used to train _Gopher_ (green). 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.810]
#### **4.1. Model and training details** 

The full set of hyperparameters used to train _Chinchilla_ are given in Table 4. _Chinchilla_ uses the same model architecture and training setup as _Gopher_ with the exception of the differences listed below. 

- We train _Chinchilla_ on _MassiveText_ (the same dataset as _Gopher_ ) but use a slightly different subset distribution (shown in Table A1) to account for the increased number of training tokens. 

- We use AdamW (Loshchilov and Hutter, 2019) for _Chinchilla_ rather than Adam (Kingma and Ba, 2014) as this improves the language modelling loss and the downstream task performance after finetuning.<sup>8</sup> 

- We train _Chinchilla_ with a slightly modified SentencePiece (Kudo and Richardson, 2018) tokenizer that does not apply NFKC normalisation. The vocabulary is very similar– 94.15% of tokens are the same as those used for training _Gopher_ . We find that this particularly helps with the representation of mathematics and chemistry, for example. 

- Whilst the forward and backward pass are computed in `bfloat16` , we store a `float32` copy of the weights in the distributed optimiser state (Rajbhandari et al., 2020). See _Lessons Learned_ from Rae et al. (2021) for additional details. 

In Appendix G we show the impact of the various optimiser related changes between _Chinchilla_ and _Gopher_ . All models in this analysis have been trained on TPUv3/TPUv4 (Jouppi et al., 2017) with JAX (Bradbury et al., 2018) and Haiku (Hennigan et al., 2020). We include a _Chinchilla_ model card (Mitchell et al., 2019) in Table A8.

---

[referencia=46fd66187ec3e6ae score=0.795]
|human_aging|77.6|66.4|human_sexuality|86.3|67.2|
|international_law|90.9|77.7|jurisprudence|79.6|71.3|
|logical_fallacies|80.4|72.4|machine_learning|41.1|41.1|
|management|82.5|77.7|marketing|89.7|83.3|
|medical_genetics|69.0|69.0|miscellaneous|84.5|75.7|
|moral_disputes|77.5|66.8|moral_scenarios|36.5|40.2|
|nutrition|77.1|69.9|philosophy|79.4|68.8|
|prehistory|81.2|67.6|professional_accounting|52.1|44.3|
|professional_law|56.5|44.5|professional_medicine|75.4|64.0|
|professional_psychology|75.7|68.1|public_relations|73.6|71.8|
|security_studies|75.9|64.9|sociology|91.0|84.1|
|us_foreign_policy<br>|92.0|81.0|virology|53.6|47.0|
|world_religions|87.7|84.2||||



Table A6 | **_Chinchilla_ MMLU results.** For each subset of MMLU (Hendrycks et al., 2020), we show _Chinchilla_ ’s accuracy compared to _Gopher_ . 

||**Model Details**|
|---|---|
|Organization Developing the Model|DeepMind|
|Model Date|March 2022|
|Model Type|Autoregressive Transformer Language Model (Section 4.1for<br>details)|
|Feedback on the Model|`{jordanhoffmann, sborgeaud,`<br>`amensch,sifre}@deepmind.com`|
||**Intended Uses**|
|Primary Intended Uses|The primary use is research on language models, including:<br>research on the scaling behaviour of language models along<br>with those listed inRae et al.(2021).|



31

---

[referencia=46fd66187ec3e6ae score=0.793]
#### **4.2. Results** 

- We perform an extensive evaluation of _Chinchilla_ , comparing against various large language models. We evaluate on a large subset of the tasks presented in Rae et al. (2021), shown in Table 5. As 

- the focus of this work is on optimal model scaling, we included a large representative subset, and introduce a few new evaluations to allow for better comparison to other existing large models. The evaluation details for all tasks are the same as described in Rae et al. (2021). 

- **_4.2.1. Language modelling_** 

      - 0.10 0.08 0.06 0.04 0.02 0.00 

- Figure 5 | **Pile Evaluation.** For the different evaluation sets in The Pile (Gao et al., 2020), we show the bits-per-byte (bpb) improvement (decrease) of _Chinchilla_ compared to _Gopher_ . On all subsets, 

- _Chinchilla_ outperforms _Gopher_ . 

   - _Chinchilla_ significantly outperforms _Gopher_ on all evaluation subsets of The Pile (Gao et al., 

- 2020), as shown in Figure 5. Compared to Jurassic-1 (178B) Lieber et al. (2021), _Chinchilla_ is more performant on all but two subsets– `dm_mathematics` and `ubuntu_irc` – see Table A5 for a raw 

- bits-per-byte comparison. On Wikitext103 (Merity et al., 2017), _Chinchilla_ achieves a perplexity of 

- 7.16 compared to 7.75 for _Gopher_ . Some caution is needed when comparing _Chinchilla_ with _Gopher_ on these language modelling benchmarks as _Chinchilla_ is trained on 4× more data than _Gopher_ and 

- thus train/test set leakage may artificially enhance the results. We thus place more emphasis on other 

10

---

[referencia=46fd66187ec3e6ae score=0.777]
Figure 2 | **Training curve envelope.** On the **left** we show all of our different runs. We launched a range of model sizes going from 70M to 10B, each for four different cosine cycle lengths. From these curves, we extracted the envelope of minimal loss per FLOP, and we used these points to estimate the optimal model size ( **center** ) for a given compute budget and the optimal number of training tokens ( **right** ). In green, we show projections of optimal model size and training token count based on the number of FLOPs used to train _Gopher_ (5 _._ 76 × 10<sup>23</sup> ).

---

[referencia=46fd66187ec3e6ae score=0.762]
many orders of magnitude, our analysis clearly suggests that given the training compute budget for 

many current LLMs, smaller models should have been trained on more tokens to achieve the most performant model. 

In Appendix C, we reproduce the IsoFLOP analysis on two additional datasets: C4 (Raffel et al., 

2020a) and GitHub code (Rae et al., 2021). In both cases we reach the similar conclusion that model size and number of training tokens should be scaled in equal proportions. 

8

---

[referencia=46fd66187ec3e6ae score=0.752]
In Table 3 we show the estimated number of FLOPs and tokens that would ensure that a model of a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of 

7 

Table 2 | **Estimated parameter and data scaling with increased training compute.** The listed values are the exponents, _𝑎_ and _𝑏_ , on the relationship _𝑁𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑎_</sup> and _𝐷𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑏_</sup> . Our analysis suggests a near equal scaling in parameters and data with increasing compute which is in clear contrast to previous work on the scaling of large models. The 10<sup>th</sup> and 90<sup>th</sup> percentiles are estimated via bootstrapping data (80% of the dataset is sampled 100 times) and are shown in parenthesis. 

Approach Coeff. _𝑎_ where _𝑁𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑎_</sup> Coeff. _𝑏_ where _𝐷𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑏_</sup> 1. Minimum over training curves 0 _._ 50 (0 _._ 488 _,_ 0 _._ 502) 0 _._ 50 (0 _._ 501 _,_ 0 _._ 512) 2. IsoFLOP profiles 0 _._ 49 (0 _._ 462 _,_ 0 _._ 534) 0 _._ 51 (0 _._ 483 _,_ 0 _._ 529) 3. Parametric modelling of the loss 0 _._ 46 (0 _._ 454 _,_ 0 _._ 455) 0 _._ 54 (0 _._ 542 _,_ 0 _._ 543) Kaplan et al. (2020) 0.73 0.27