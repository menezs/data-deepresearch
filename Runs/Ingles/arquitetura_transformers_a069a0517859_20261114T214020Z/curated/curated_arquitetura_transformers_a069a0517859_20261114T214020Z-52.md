[referencia=46fd66187ec3e6ae score=0.694]
As in Kaplan et al. (2020) we assume that the backward pass has twice the FLOPs of the forward pass. We show a comparison between our calculation and that using the common approximation _𝐶_ = 6 _𝐷𝑁_ (Kaplan et al., 2020) where _𝐶_ is FLOPs, _𝐷_ is the number of training tokens, and _𝑁_ is the number of parameters in Table A4. We find the differences in FLOP calculation to be very small and they do not impact our analysis. Compared to the results presented in Rae et al. (2021), we use a slightly more 

|Parameters|num_layers|d_model|fw_size|num_heads|k/q size|FLOP Ratio (Ours/6_𝑁𝐷_)|
|---|---|---|---|---|---|---|
|73M|10|640|2560|10|64|1.03|
|305M|20|1024|4096|16|64|1.10|
|552M|24|1280|5120|10|128|1.08|
|1.1B|26|1792|7168|14|128|1.04|
|1.6B|28|2048|8192|16|128|1.03|
|6.8B|40|3584|14336|28|128|0.99|



Table A4 | **FLOP comparison.** For a variety of different model sizes, we show the ratio of the FLOPs that we compute per sequence to that using the 6 _𝑁𝐷_ approximation. 

accurate calculation giving a slightly different value (6 _._ 3 × 10<sup>23</sup> compared to 5 _._ 76 × 10<sup>23</sup> ). 

28

---

[referencia=46fd66187ec3e6ae score=0.653]
large language models are considerably over-sized, given their respective compute budgets, as shown in Figure 1. For example, we find that a 175 billion parameter model should be trained with a compute budget of 4 _._ 41 × 10<sup>24</sup> FLOPs and on over 4.2 trillion tokens. A 280 billion _Gopher_ -like model is the optimal model to train given a compute budget of approximately 10<sup>25</sup> FLOPs and should be trained on 6.8 trillion tokens. Unless one has a compute budget of 10<sup>26</sup> FLOPs (over 250× the compute used to train _Gopher_ ), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale. While there is significant uncertainty extrapolating out many orders of magnitude, our analysis clearly suggests that given the training compute budget for many current LLMs, smaller models should have been trained on more tokens to achieve the most performant model. 

In Appendix C, we reproduce the IsoFLOP analysis on two additional datasets: C4 (Raffel et al., 2020a) and GitHub code (Rae et al., 2021). In both cases we reach the similar conclusion that model size and number of training tokens should be scaled in equal proportions. 

8

---

[referencia=46fd66187ec3e6ae score=0.647]
### **5. Discussion & Conclusion** 

The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget. 

We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that _Gopher_ is substantially over-sized and estimate that for the same compute budget a smaller model trained on more data will perform better. We directly test this hypothesis by training _Chinchilla_ , a 70B parameter model, and show that it outperforms _Gopher_ and even larger models on nearly every measured evaluation task. 

Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale ( _Chinchilla_ and _Gopher_ ), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log<sup>�</sup> _𝑁𝑜𝑝𝑡_ � at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime. Despite these limitations, the comparison of _Chinchilla_ to _Gopher_ validates our performance predictions, that have thus enabled training a better (and more 

15

---

[referencia=46fd66187ec3e6ae score=0.604]
The functions _𝑁𝑜𝑝𝑡_ ( _𝐶_ ), and _𝐷𝑜𝑝𝑡_ ( _𝐶_ ) describe the optimal allocation of a computational budget _𝐶_ . We empirically estimate these functions based on the losses of over 400 models, ranging from under 70M to over 16B parameters, and trained on 5B to over 400B tokens – with each model configuration trained for several different training horizons. Our approach leads to considerably different results than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ in Section 2. 

Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train _Gopher_ , an optimal model should be 4 times smaller, while being training on 4 times more tokens. We verify this by training a more _compute-optimal_ 70B model, called _Chinchilla_ , on 1.4 trillion tokens. Not only does _Chinchilla_ outperform its much larger counterpart, _Gopher_ , but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware. The energy cost of a large language model is amortized through its usage for inference an fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the immediate benefits of its improved performance. 

> 1For example, knowing the number of accelerators and a target training duration. 

> 2For simplicity, we perform our analysis on the smoothed training loss which is an unbiased estimate of the test loss, as we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus). 

2 

Table 1 | **Current LLMs** . We show five of the current largest dense transformer models, their size, and the number of training tokens. Other than LaMDA (Thoppilan et al., 2022), most models are trained for approximately 300 billion tokens. We introduce _Chinchilla_ , a substantially smaller model, trained for much longer than 300B tokens.

---

[referencia=46fd66187ec3e6ae score=0.518]
> 7We set the cosine schedule length to match the number of tokens, which is optimal according to the analysis presented in Appendix B. 

5 



<!-- Start of picture text -->
10T<br>3.2 1T<br>1.4T<br>3.0 1T<br>100B 63B<br>2.8 6e18<br>100B<br>1e19 10B<br>2.6 3e19<br>6e19 10B<br>2.4 1e20 1B<br>3e20<br>6e20 1B<br>2.2 1e21 100M<br>3e21<br>2.0 100M<br>100M 300M 1B 3B 6B 30B 10 17 10 19 10 21 10 23 10 25 10 17 10 19 10 21 10 23 10 25<br>Parameters FLOPs FLOPs<br>Tokens<br>Training Loss Parameters<br><!-- End of picture text -->

Figure 3 | **IsoFLOP curves.** For various model sizes, we choose the number of training tokens such that the final FLOPs is a constant. The cosine cycle length is set to match the target FLOP count. We find a clear valley in loss, meaning that for a given FLOP budget there is an optimal model to train ( **left** ). Using the location of these valleys, we project optimal model size and number of tokens for larger models ( **center** and **right** ). In green, we show the estimated number of parameters and tokens for an _optimal_ model trained with the compute budget of _Gopher_ .

---

[referencia=46fd66187ec3e6ae score=0.490]
### **3. Estimating the optimal parameter/training tokens allocation** 

We present three different approaches to answer the question driving our research: _Given a fixed FLOPs budget, how should one trade-off model size and the number of training tokens?_ In all three cases we start by training a range of models varying both model size and the number of training tokens and use the resulting training curves to fit an empirical estimator of how they should scale. We assume a power-law relationship between compute and model size as done in Clark et al. (2022); Kaplan et al. (2020), though future work may want to include potential curvature in this relationship for large model sizes. The resulting predictions are similar for all three methods and suggest that — parameter count and number of training tokens should be increased equally with more compute<sup>3</sup> with proportions reported in Table 2. This is in clear contrast to previous work on this topic and warrants further investigation. 

> 3 We compute FLOPs as described in Appendix F. 

4 



<!-- Start of picture text -->
6.0 10B 1T 1.5T<br>5.5 5B 10 12<br>5.0<br>4.5 2.5B 100B 67B<br>4.0 1B 10 11<br>3.5 500M 10B<br>250M<br>3.0 10 10<br>1.0B<br>75M<br>2.5<br>100M 10 9<br>2.0<br>10 17 10 18 10 19 10 20 10 21 10 22 10 17 10 19 10 21 10 23 10 25 10 17 10 19 10 21 10 23 10 25<br>FLOPS FLOPs FLOPs<br>Tokens<br>Training loss Parameters<br><!-- End of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.486]
_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved 



<!-- Start of picture text -->
1T<br>Approach 1<br>100B<br>Approach 2<br>Approach 3<br>Kaplan et al (2020)<br>10B<br>Chinchilla (70B)<br>1.0B Gopher (280B)<br>GPT-3 (175B)<br>Megatron-Turing NLG (530B)<br>100M<br>10M<br>10 17 10 19 10 21 10 23 10 25<br>FLOPs<br>Parameters<br><!-- End of picture text -->

Figure 1 | **Overlaid predictions.** We overlay the predictions from our three different approaches, along with projections from Kaplan et al. (2020). We find that all three methods predict that current large models should be substantially smaller and therefore trained much longer than is currently done. In Figure A3, we show the results with the predicted optimal tokens plotted against the optimal number of parameters for fixed FLOP budgets. **_Chinchilla_ outperforms** **_Gopher_ and the other large models (see Section 4.2).** 

In this work, we revisit the question: _Given a fixed FLOPs budget,_<sup>1</sup> _how should one trade-off model size and the number of training tokens?_ To answer this question, we model the final pre-training loss<sup>2</sup> _𝐿_ ( _𝑁, 𝐷_ ) as a function of the number of model parameters _𝑁_ , and the number of training tokens, _𝐷_ . Since the computational budget _𝐶_ is a deterministic function FLOPs( _𝑁, 𝐷_ ) of the number of seen training tokens and model parameters, we are interested in minimizing _𝐿_ under the constraint FLOPs( _𝑁, 𝐷_ ) = _𝐶_ :

---

[referencia=46fd66187ec3e6ae score=0.458]
### **1. Introduction** 

Recently a series of _Large Language Models_ (LLMs) have been introduced (Brown et al., 2020; Lieber et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022), with the largest dense language models now having over 500 billion parameters. These large autoregressive transformers (Vaswani et al., 2017) have demonstrated impressive performance on many tasks using a variety of evaluation protocols such as zero-shot, few-shot, and fine-tuning. 

The compute and energy cost for training large language models is substantial (Rae et al., 2021; Thoppilan et al., 2022) and rises with increasing model size. In practice, the allocated training compute budget is often known in advance: how many accelerators are available and for how long we want to use them. Since it is typically only feasible to train these large models once, accurately estimating the best model hyperparameters for a given compute budget is critical (Tay et al., 2021). 

Kaplan et al. (2020) showed that there is a power law relationship between the number of parameters in an autoregressive language model (LM) and its performance. As a result, the field has been training larger and larger models, expecting performance improvements. One notable conclusion in Kaplan et al. (2020) is that large models should not be trained to their lowest possible loss to be compute optimal. Whilst we reach the same conclusion, we estimate that large models should be trained for many more training tokens than recommended by the authors. Specifically, given a 10× increase computational budget, they suggests that the size of the model should increase 5 _._ 5× while the number of training tokens should only increase 1.8×. Instead, we find that model size and the number of training tokens should be scaled in equal proportions. 

Following Kaplan et al. (2020) and the training setup of GPT-3 (Brown et al., 2020), many of the recently trained large models have been trained for approximately 300 billion tokens (Table 1), in line with the approach of predominantly increasing model size when increasing compute. 

_Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com_ © 2023 DeepMind. All rights reserved

---

[referencia=46fd66187ec3e6ae score=0.449]
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

[referencia=46fd66187ec3e6ae score=0.444]
#### **3.1. Approach 1: Fix model sizes and vary number of training tokens** 

In our first approach we vary the number of training steps for a fixed family of models (ranging from 70M to over 10B parameters), training each model for 4 different number of training sequences. From these runs, we are able to directly extract an estimate of the minimum loss achieved for a given number of training FLOPs. Training details for this approach can be found in Appendix D. 

For each parameter count _𝑁_ we train 4 different models, decaying the learning rate by a factor of 10× over a horizon (measured in number of training tokens) that ranges by a factor of 16×. Then, for each run, we smooth and then interpolate the training loss curve. From this, we obtain a continuous mapping from FLOP count to training loss for each run. Then, for each FLOP count, we determine which run achieves the lowest loss. Using these interpolants, we obtain a mapping from any FLOP count _𝐶_ , to the most efficient choice of model size _𝑁_ and number of training tokens _𝐷_ such that FLOPs( _𝑁, 𝐷_ ) = _𝐶_ .<sup>4</sup> At 1500 logarithmically spaced FLOP values, we find which model size achieves the lowest loss of all models along with the required number of training tokens. Finally, we fit power laws to estimate the optimal model size and number of training tokens for any given amount of compute (see the center and right panels of Figure 2), obtaining a relationship _𝑁𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑎_</sup> and _𝐷𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑏_</sup> . We find that _𝑎_ = 0 _._ 50 and _𝑏_ = 0 _._ 50—as summarized in Table 2. In Section D.4, we show a head-to-head comparison at 10<sup>21</sup> FLOPs, using the model size recommended by our analysis and by the analysis of Kaplan et al. (2020)—using the model size we predict has a clear advantage.

---

[referencia=46fd66187ec3e6ae score=0.430]
## **Training Compute-Optimal Large Language Models** 

**Jordan Hoffmann**<sup>_★_</sup> **, Sebastian Borgeaud**<sup>_★_</sup> **, Arthur Mensch**<sup>_★_</sup> **, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre**<sup>_★_</sup> 

> _★_ Equal contributions 

**We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model,** **_Chinchilla_ , that uses the same compute budget as** **_Gopher_ but with 70B parameters and 4** × **more more data.** **_Chinchilla_ uniformly and significantly outperforms** **_Gopher_ (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that** **_Chinchilla_ uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight,** **_Chinchilla_ reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_ .**

---

[referencia=46fd66187ec3e6ae score=0.367]
#### **D.4. Small-scale comparison to Kaplan** **_et al._ (2020)** 

For 10<sup>21</sup> FLOPs, we perform a head-to-head comparison of a model predicted by Approach 1 and that predicted by Kaplan et al. (2020). For both models, we use a batch size of 0.5M tokens and a 

26 

maximum learning rate of 1 _._ 5 × 10<sup>−4</sup> that decays by 10×. From Kaplan et al. (2020), we find that the optimal model size should be 4.68 billion parameters. From our approach 1, we estimate a 2.86 billion parameter model should be optimal. We train a 4.74 billion parameter and a 2.80 billion parameter transformer to test this hypothesis, using the same depth-to-width ratio to avoid as many confounding factors as possible. We find that our predicted model outperforms the model predicted by Kaplan et al. (2020) as shown in Figure A4. 



<!-- Start of picture text -->
2.8 2.8<br>Kaplan et al (2020)<br>Approach 1<br>2.7 2.7<br>2.6 2.6<br>2.5 2.5<br>2.4 2.4<br>2.3 2.3<br>2.2 2.2<br>0 1 2 0.0 0.2 0.4 0.6 0.8 1.0<br>Sequences 1e7 FLOPs ×10 21<br>Training Loss Training Loss<br><!-- End of picture text -->

Figure A4 | **Comparison to Kaplan et al. (2020) at** 10<sup>21</sup> **FLOPs.** We train 2.80 and 4.74 billion parameter transformers predicted as optimal for 10<sup>21</sup> FLOPs by Approach 1 and by Kaplan et al. (2020). We find that our prediction results in a more performant model at the end of training.

---

[referencia=46fd66187ec3e6ae score=0.337]
. 



<!-- Start of picture text -->
10 12 Approach 1 1e+2 6<br>Approach 2<br>Approach 3<br>Chinchilla 1e+25<br>Gopher<br>10 11 GPT-3 1e+24<br>Megatron-Turing NLG<br>1e+23<br>10 10 1e+22<br>1e+21<br>10 9 1e+20<br>1e+19<br>10 8 1e+18<br>10 10 10 11 10 12 10 13<br>Tokens<br>Parameters<br><!-- End of picture text -->

Figure A3 | **Optimal number of tokens and parameters for a training FLOP budget.** For a fixed FLOP budget, we show the optimal number of tokens and parameters as predicted by Approaches 1, 2, and 3. For an alternate representation, see Figure 1.

---

[referencia=46fd66187ec3e6ae score=0.328]
### **G. Other differences between** **_Chinchilla_ and** **_Gopher_** 

Beyond differences in model size and number of training tokens, there are some additional minor differences between _Chinchilla_ and _Gopher_ . Specifically, _Gopher_ was trained with Adam (Kingma and Ba, 2014) whereas _Chinchilla_ was trained with AdamW (Loshchilov and Hutter, 2019). Furthermore, as discussed in _Lessons Learned_ in Rae et al. (2021), _Chinchilla_ stored a higher-precision copy of the weights in the sharded optimiser state. 

We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7. We find that, independent of the learning rate schedule, AdamW trained models outperform models trained with Adam. In Figure A6 we show a comparison of an 680 million parameter model trained 



<!-- Start of picture text -->
2.70 26 3.00<br>Training Setup<br>25 2.95 Adam w/ High Precision<br>2.65 24 2.90 AdamW w/ High Precision<br>Adam No High Precision<br>23<br>2.60 2.85 AdamW No High Precision<br>22<br>2.80<br>21<br>2.55 2.75<br>20<br>2.50 19 2.70<br>18 2.65<br>2.45 17 2.60<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>Million Sequences Million Sequences Million Sequences<br>C4 Loss<br>Training Loss<br>Wikitext103 Perplexity<br><!-- End of picture text -->

Figure A6 | **Comparison of other differences.** Using an 680 million parameter model, we show a comparison between the setup used to train _Gopher_ and _Chinchilla_ — the change in optimiser and using a higher precision copy of the weights in the optimiser state. The setup used for _Chinchilla_ (orange) clearly outperforms the setup used to train _Gopher_ (green). 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.327]
**Modelling the scaling behavior.** Understanding the scaling behaviour of language models and their transfer properties has been important in the development of recent large models (Hernandez et al., 2021; Kaplan et al., 2020). Kaplan et al. (2020) first showed a predictable relationship between model size and loss over many orders of magnitude. The authors investigate the question of choosing the optimal model size to train for a given compute budget. Similar to us, they address this question by training various models. Our work differs from Kaplan et al. (2020) in several important ways. First, the authors use a fixed number of training tokens and learning rate schedule for all models; this prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find that setting the learning rate schedule to approximately match the number of training tokens results in the best final loss regardless of model size—see Figure A1. For a fixed learning rate cosine schedule to 130B tokens, the intermediate loss estimates (for _𝐷_<sup>′</sup> _<<_ 130B) are therefore overestimates of the loss of a model trained with a schedule length matching _𝐷_<sup>′</sup> . Using these intermediate losses results in underestimating the effectiveness of training models on less data than 130B tokens, and eventually contributes to the conclusion that model size should increase faster than training data size as compute budget increases. In contrast, our analysis predicts that both quantities should scale at roughly the same rate. Secondly, we include models with up to 16B parameters, as we observe that there is slight curvature in the FLOP-loss frontier (see Appendix E)—in fact, the majority of the models used in our analysis have more than 500 million parameters, in contrast the majority of runs in Kaplan et al. (2020) are significantly smaller—many being less than 100M parameters. 

Recently, Clark et al. (2022) specifically looked in to the scaling properties of Mixture of Expert 

3 

language models, showing that the scaling with number of experts diminishes as the model size increases—their approach models the loss as a function of two variables: the model size and the number of experts. However, the analysis is done with a fixed number of training tokens, as in Kaplan et al. (2020), potentially underestimating the improvements of branching.

---

[referencia=46fd66187ec3e6ae score=0.315]
#### **D.3. Predicted compute optimal frontier for all three methods** 

For Approaches 2 and 3, we show the estimated model size and number of training tokens for a variety of compute budgets in Table A3. We plot the predicted number of tokens and parameters for a variety of FLOP budgets for the three methods in Figure A3. 

||App|roach 2|App|roach 3|
|---|---|---|---|---|
|Parameters|FLOPs|Tokens|FLOPs|Tokens|
|400 Million|1.84e+19|7.7 Billion|2.21e+19|9.2 Billion|
|1 Billion|1.20e+20|20.0 Billion|1.62e+20|27.1 Billion|
|10 Billion|1.32e+22|219.5 Billion|2.46e+22|410.1 Billion|
|67 Billion|6.88e+23|1.7 Trillion|1.71e+24|4.1 Trillion|
|175 Billion|4.54e+24|4.3 Trillion|1.26e+24|12.0 Trillion|
|280 Billion|1.18e+25|7.1 Trillion|3.52e+25|20.1 Trillion|
|520 Billion|4.19e+25|13.4 Trillion|1.36e+26|43.5 Trillion|
|1 Trillion|1.59e+26|26.5 Trillion|5.65e+26|94.1 Trillion|
|10 Trillion|1.75e+28|292.0 Trillion|8.55e+28|1425.5 Trillion|



Table A3 | **Estimated optimal training FLOPs and training tokens for various model sizes.** Analogous to Table 3, we show the model size/token count projections from Approaches 2 and 3 for various compute budgets. 

. 



<!-- Start of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.306]
Figure A1 | **Grid over cosine cycle length.** We show 6 curves with the cosine cycle length set to 1, 1.1, 1.25, 1.5, 2, and 5× longer than the target number of training steps. When the cosine cycle length is too long, and the learning rate does not drop appropriately, then performance is impaired. We find that overestimating the number of training steps beyond 25% leads to clear drops in performance. We show results where we have set the number of training steps to two different values (top and bottom). 



<!-- Start of picture text -->
10T<br>3.2 1T<br>1.3T<br>3.0 1T<br>100B 73B<br>2.8<br>100B<br>10B<br>2.6<br>10B<br>2.4 1e19 1B<br>1e20<br>1B<br>2.2 6e20 100M<br>1e21<br>2.0 100M<br>100M 300M 1B 3B 6B 30B 10 17 10 19 10 21 10 23 10 25 10 17 10 19 10 21 10 23 10 25<br>Parameters FLOPs FLOPs<br>1.0 10T<br>1e19 1T<br>0.9 1e20 1.6T<br>0.8 6e201e21 100B 59B 1T<br>0.7 100B<br>10B<br>0.6<br>0.5 10B<br>1B<br>0.4<br>1B<br>0.3 100M<br>0.2 100M<br>100M 300M 1B 3B 6B 30B 10 17 10 19 10 21 10 23 10 25 10 17 10 19 10 21 10 23 10 25<br>Parameters FLOPs FLOPs<br>Tokens<br>Parameters<br>C4 Training Loss<br>Tokens<br>Parameters<br>GitHub Training Loss<br><!-- End of picture text -->

---

[referencia=46fd66187ec3e6ae score=0.274]
In Table 3 we show the estimated number of FLOPs and tokens that would ensure that a model of a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of 

7 

Table 2 | **Estimated parameter and data scaling with increased training compute.** The listed values are the exponents, _𝑎_ and _𝑏_ , on the relationship _𝑁𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑎_</sup> and _𝐷𝑜𝑝𝑡_ ∝ _𝐶_<sup>_𝑏_</sup> . Our analysis suggests a near equal scaling in parameters and data with increasing compute which is in clear contrast to previous work on the scaling of large models. The 10<sup>th</sup> and 90<sup>th</sup> percentiles are estimated via bootstrapping data (80% of the dataset is sampled 100 times) and are shown in parenthesis. 

|Approach|Coef. _𝑎_where _𝑁𝑜𝑝𝑡_∝_𝐶_<sup>_𝑎_</sup>|Coef. _𝑏_where _𝐷𝑜𝑝𝑡_∝_𝐶_<sup>_𝑏_</sup>|
|---|---|---|
|1. Minimum over training curves|0_._50 (0_._488_,_0_._502)|0_._50 (0_._501_,_0_._512)|
|2. IsoFLOP profles|0_._49 (0_._462_,_0_._534)|0_._51 (0_._483_,_0_._529)|
|3. Parametric modelling of the loss|0_._46 (0_._454_,_0_._455)|0_._54 (0_._542_,_0_._543)|
|Kaplan et al.(2020)|0.73|0.27|

---

[referencia=46fd66187ec3e6ae score=0.199]
**Estimating hyperparameters for large models.** The model size and the number of training tokens are not the only two parameters to chose when selecting a language model and a procedure to train it. Other important factors include learning rate, learning rate schedule, batch size, optimiser, and width-to-depth ratio. In this work, we focus on model size and the number of training steps, and we rely on existing work and provided experimental heuristics to determine the other necessary hyperparameters. Yang et al. (2021) investigates how to choose a variety of these parameters for training an autoregressive transformer, including the learning rate and batch size. McCandlish et al. (2018) finds only a weak dependence between optimal batch size and model size. Shallue et al. (2018); Zhang et al. (2019) suggest that using larger batch-sizes than those we use is possible. Levine et al. (2020) investigates the optimal depth-to-width ratio for a variety of standard model sizes. We use slightly less deep models than proposed as this translates to better wall-clock performance on our hardware. 

**Improved model architectures.** Recently, various promising alternatives to traditional dense transformers have been proposed. For example, through the use of conditional computation large MoE models like the 1.7 trillion parameter Switch transformer (Fedus et al., 2021), the 1.2 Trillion parameter GLaM model (Du et al., 2021), and others (Artetxe et al., 2021; Zoph et al., 2022) are able to provide a large effective model size despite using relatively fewer training and inference FLOPs. However, for very large models the computational benefits of routed models seems to diminish (Clark et al., 2022). An orthogonal approach to improving language models is to augment transformers with explicit retrieval mechanisms, as done by Borgeaud et al. (2021); Guu et al. (2020); Lewis et al. (2020). This approach effectively increases the number of data tokens seen during training (by a factor of ∼ 10 in Borgeaud et al. (2021)). This suggests that the performance of language models may be more dependant on the size of the training data than previously thought.

---

[referencia=46fd66187ec3e6ae score=0.193]
#### **3.4. Optimal model scaling** 

We find that the three approaches, despite using different fitting methodologies and different trained models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs (shown in Table 2). All three approaches suggest that as compute budget increases, model size and the amount of training data should be increased in approximately equal proportions. The first and second approaches yield very similar predictions for optimal model sizes, as shown in Figure 1 and Figure A3. The third approach predicts even smaller models being optimal at larger compute budgets. We note that the observed points ( _𝐿, 𝑁, 𝐷_ ) for low training FLOPs ( _𝐶_ ⩽ 1 _𝑒_ 21) have larger residuals 2 ∥ _𝐿_ − _𝐿_<sup>ˆ</sup> ( _𝑁, 𝐷_ )∥2<sup>thanpointswithhighercomputationalbudgets.Thefittedmodelplacesincreased</sup> weight on the points with more FLOPs—automatically considering the low-computational budget points as outliers due to the Huber loss. As a consequence of the empirically observed negative curvature in the frontier _𝐶_ → _𝑁𝑜𝑝𝑡_ (see Appendix E), this results in predicting a lower _𝑁𝑜𝑝𝑡_ than the two other approaches. 

In Table 3 we show the estimated number of FLOPs and tokens that would ensure that a model of a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of 

7