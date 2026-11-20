[referencia=de539966b9f54c2c score=0.998]
## **Abstract** 

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at `https://github.com/deepseek-ai/DeepSeek-V3` . 



<!-- Start of picture text -->

---

[referencia=de539966b9f54c2c score=0.998]
### **6. Conclusion, Limitations, and Future Directions** 

In this paper, we introduce DeepSeek-V3, a large MoE language model with 671B total parameters and 37B activated parameters, trained on 14.8T tokens. In addition to the MLA and DeepSeekMoE architectures, it also pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. The training of DeepSeek-V3 is cost-effective due to the support of FP8 training and meticulous engineering optimizations. The post-training also makes a success in distilling the reasoning capability from the DeepSeek-R1 series of models. Comprehensive evaluations demonstrate that DeepSeek-V3 has emerged as the strongest open-source model currently available, and achieves performance comparable to leading closed-source models like GPT-4o and Claude-3.5-Sonnet. Despite its strong performance, it also maintains economical training costs. It requires only 2.788M H800 GPU hours for its full training, including pre-training, context length extension, and post-training. 

While acknowledging its strong performance and cost-effectiveness, we also recognize that DeepSeek-V3 has some limitations, especially on the deployment. Firstly, to ensure efficient inference, the recommended deployment unit for DeepSeek-V3 is relatively large, which might pose a burden for small-sized teams. Secondly, although our deployment strategy for DeepSeekV3 has achieved an end-to-end generation speed of more than two times that of DeepSeek-V2, there still remains potential for further enhancement. Fortunately, these limitations are expected to be naturally addressed with the development of more advanced hardware. 

DeepSeek consistently adheres to the route of open-source models with longtermism, aiming to steadily approach the ultimate goal of AGI (Artificial General Intelligence). In the future, we plan to strategically invest in research across the following directions. 

- We will consistently study and refine our model architectures, aiming to further improve both the training and inference efficiency, striving to approach efficient support for infinite context length. Additionally, we will try to break through the architectural limitations of Transformer, thereby pushing the boundaries of its modeling capabilities. 

35

---

[referencia=de539966b9f54c2c score=0.993]
### **1. Introduction** 

In recent years, Large Language Models (LLMs) have been undergoing rapid iteration and evolution (Anthropic, 2024; Google, 2024; OpenAI, 2024a), progressively diminishing the gap towards Artificial General Intelligence (AGI). Beyond closed-source models, open-source models, including DeepSeek series (DeepSeek-AI, 2024a,b,c; Guo et al., 2024), LLaMA series (AI@Meta, 2024a,b; Touvron et al., 2023a,b), Qwen series (Qwen, 2023, 2024a,b), and Mistral series (Jiang et al., 2023; Mistral, 2024), are also making significant strides, endeavoring to close the gap with their closed-source counterparts. To further push the boundaries of open-source model capabilities, we scale up our models and introduce DeepSeek-V3, a large Mixture-of-Experts (MoE) model with 671B parameters, of which 37B are activated for each token. 

With a forward-looking perspective, we consistently strive for strong model performance and economical costs. Therefore, in terms of architecture, DeepSeek-V3 still adopts Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference and DeepSeekMoE (Dai et al., 2024) for cost-effective training. These two architectures have been validated in DeepSeekV2 (DeepSeek-AI, 2024c), demonstrating their capability to maintain robust model performance while achieving efficient training and inference. Beyond the basic architecture, we implement two additional strategies to further enhance the model capabilities. Firstly, DeepSeek-V3 pioneers an auxiliary-loss-free strategy (Wang et al., 2024a) for load balancing, with the aim of minimizing the adverse impact on model performance that arises from the effort to encourage load balancing. Secondly, DeepSeek-V3 employs a multi-token prediction training objective, which we have observed to enhance the overall performance on evaluation benchmarks.

---

[referencia=de539966b9f54c2c score=0.991]
4 

|**Training Costs**|**Pre-Training**|**Context Extension**|**Post-Training**|**Total**|
|---|---|---|---|---|
|in H800 GPU Hours|2664K|119K|5K|2788K|
|in USD|$5.328M|$0.238M|$0.01M|$5.576M|



Table 1 | Training costs of DeepSeek-V3, assuming the rental price of H800 is $2 per GPU hour. 

and generation length. 

We evaluate DeepSeek-V3 on a comprehensive array of benchmarks. Despite its economical training costs, comprehensive evaluations reveal that DeepSeek-V3-Base has emerged as the strongest open-source base model currently available, especially in code and math. Its chat version also outperforms other open-source models and achieves performance comparable to leading closed-source models, including GPT-4o and Claude-3.5-Sonnet, on a series of standard and open-ended benchmarks. 

Lastly, we emphasize again the economical training costs of DeepSeek-V3, summarized in Table 1, achieved through our optimized co-design of algorithms, frameworks, and hardware. During the pre-training stage, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, i.e., 3.7 days on our cluster with 2048 H800 GPUs. Consequently, our pretraining stage is completed in less than two months and costs 2664K GPU hours. Combined with 119K GPU hours for the context length extension and 5K GPU hours for post-training, DeepSeek-V3 costs only 2.788M GPU hours for its full training. Assuming the rental price of the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M. Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments on architectures, algorithms, or data. 

Our main contribution includes: 

#### **Architecture: Innovative Load Balancing Strategy and Training Objective** 

- On top of the efficient architecture of DeepSeek-V2, we pioneer an auxiliary-loss-free strategy for load balancing, which minimizes the performance degradation that arises from encouraging load balancing. 

- We investigate a Multi-Token Prediction (MTP) objective and prove it beneficial to model performance. It can also be used for speculative decoding for inference acceleration.

---

[referencia=de539966b9f54c2c score=0.988]
#### **4.2. Hyper-Parameters** 

**Model Hyper-Parameters.** We set the number of Transformer layers to 61 and the hidden dimension to 7168. All learnable parameters are randomly initialized with a standard deviation of 0.006. In MLA, we set the number of attention heads _𝑛ℎ_ to 128 and the per-head dimension _𝑑ℎ_ to 128. The KV compression dimension _𝑑𝑐_ is set to 512, and the query compression dimension _𝑑𝑐_<sup>′</sup> is set to 1536. For the decoupled queries and key, we set the per-head dimension _𝑑ℎ_<sup>_𝑅_to 64.We</sup> substitute all FFNs except for the first three layers with MoE layers. Each MoE layer consists of 1 shared expert and 256 routed experts, where the intermediate hidden dimension of each expert is 2048. Among the routed experts, 8 experts will be activated for each token, and each token will be ensured to be sent to at most 4 nodes. The multi-token prediction depth _𝐷_ is set to 1, i.e., besides the exact next token, each token will predict one additional token. As DeepSeek-V2, DeepSeek-V3 also employs additional RMSNorm layers after the compressed latent vectors, and multiplies additional scaling factors at the width bottlenecks. Under this configuration, DeepSeek-V3 comprises 671B total parameters, of which 37B are activated for each token.

---

[referencia=de539966b9f54c2c score=0.985]
In order to achieve efficient training, we support the FP8 mixed precision training and implement comprehensive optimizations for the training framework. Low-precision training has emerged as a promising solution for efficient training (Dettmers et al., 2022; Kalamkar et al., 2019; Narang et al., 2017; Peng et al., 2023b), its evolution being closely tied to advancements in hardware capabilities (Luo et al., 2024; Micikevicius et al., 2022; Rouhani et al., 2023a). In this work, we introduce an FP8 mixed precision training framework and, for the first time, validate its effectiveness on an extremely large-scale model. Through the support for FP8 computation and storage, we achieve both accelerated training and reduced GPU memory usage. As for the training framework, we design the DualPipe algorithm for efficient pipeline parallelism, which has fewer pipeline bubbles and hides most of the communication during training through computation-communication overlap. This overlap ensures that, as the model further scales up, as long as we maintain a constant computation-to-communication ratio, we can still employ fine-grained experts across nodes while achieving a near-zero all-to-all communication overhead. In addition, we also develop efficient cross-node all-to-all communication kernels to fully utilize InfiniBand (IB) and NVLink bandwidths. Furthermore, we meticulously optimize the memory footprint, making it possible to train DeepSeek-V3 without using costly tensor parallelism. Combining these efforts, we achieve high training efficiency. 

During pre-training, we train DeepSeek-V3 on 14.8T high-quality and diverse tokens. The pre-training process is remarkably stable. Throughout the entire training process, we did not encounter any irrecoverable loss spikes or have to roll back. Next, we conduct a two-stage context length extension for DeepSeek-V3. In the first stage, the maximum context length is extended to 32K, and in the second stage, it is further extended to 128K. Following this, we conduct post-training, including Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on the base model of DeepSeek-V3, to align it with human preferences and further unlock its potential. During the post-training stage, we distill the reasoning capability from the DeepSeekR1 series of models, and meanwhile carefully maintain the balance between model accuracy 

4

---

[referencia=de539966b9f54c2c score=0.974]
Figure 3 | Illustration of our Multi-Token Prediction (MTP) implementation. We keep the complete causal chain for the prediction of each token at each depth. 

**Node-Limited Routing.** Like the device-limited routing used by DeepSeek-V2, DeepSeek-V3 also uses a restricted routing mechanism to limit communication costs during training. In short, we ensure that each token will be sent to at most _𝑀_ nodes, which are selected according to the sum of the highest<sup>_𝐾_</sup> _𝑀_<sup>_<u>𝑟</u>_affinity scores of the experts distributed on each node.Under this</sup> constraint, our MoE training framework can nearly achieve full computation-communication overlap. 

**No Token-Dropping.** Due to the effective load balancing strategy, DeepSeek-V3 keeps a good load balance during its full training. Therefore, DeepSeek-V3 does not drop any tokens during training. In addition, we also implement specific deployment strategies to ensure inference load balance, so DeepSeek-V3 also does not drop tokens during inference.

---

[referencia=de539966b9f54c2c score=0.946]
**Auxiliary-Loss-Free Load Balancing.** For MoE models, an unbalanced expert load will lead to routing collapse (Shazeer et al., 2017) and diminish computational efficiency in scenarios with expert parallelism. Conventional solutions usually rely on the auxiliary loss (Fedus et al., 2021; Lepikhin et al., 2021) to avoid unbalanced load. However, too large an auxiliary loss will impair the model performance (Wang et al., 2024a). To achieve a better trade-off between load balance and model performance, we pioneer an auxiliary-loss-free load balancing strategy (Wang et al., 2024a) to ensure load balance. To be specific, we introduce a bias term _𝑏𝑖_ for each expert and add it to the corresponding affinity scores _𝑠𝑖_ , _𝑡_ to determine the top-K routing: 



Note that the bias term is only used for routing. The gating value, which will be multiplied with the FFN output, is still derived from the original affinity score _𝑠𝑖_ , _𝑡_ . During training, we keep monitoring the expert load on the whole batch of each training step. At the end of each step, we will decrease the bias term by _𝛾_ if its corresponding expert is overloaded, and increase it by _𝛾_ if its corresponding expert is underloaded, where _𝛾_ is a hyper-parameter called bias update speed. Through the dynamic adjustment, DeepSeek-V3 keeps balanced expert load during training, and achieves better performance than models that encourage load balance through pure auxiliary losses. 

**Complementary Sequence-Wise Auxiliary Loss.** Although DeepSeek-V3 mainly relies on the auxiliary-loss-free strategy for load balance, to prevent extreme imbalance within any single sequence, we also employ a complementary sequence-wise balance loss: 









where the balance factor _𝛼_ is a hyper-parameter, which will be assigned an extremely small value for DeepSeek-V3; 1(·) denotes the indicator function; and _𝑇_ denotes the number of tokens in a sequence. The sequence-wise balance loss encourages the expert load on each sequence to be balanced. 

9 



<!-- Start of picture text -->

---

[referencia=de539966b9f54c2c score=0.933]
25 

especially on English, multilingual, code, and math benchmarks. As for Chinese benchmarks, except for CMMLU, a Chinese multi-subject multiple-choice task, DeepSeek-V3-Base also shows better performance than Qwen2.5 72B. (3) Compared with LLaMA-3.1 405B Base, the largest open-source model with 11 times the activated parameters, DeepSeek-V3-Base also exhibits much better performance on multilingual, code, and math benchmarks. As for English and Chinese language benchmarks, DeepSeek-V3-Base shows competitive or better performance, and is especially good on BBH, MMLU-series, DROP, C-Eval, CMMLU, and CCPM. 

Due to our efficient architectures and comprehensive engineering optimizations, DeepSeekV3 achieves extremely high training efficiency. Under our training framework and infrastructures, training DeepSeek-V3 on each trillion tokens requires only 180K H800 GPU hours, which is much cheaper than training 72B or 405B dense models.

---

[referencia=de539966b9f54c2c score=0.925]
Table 5 | Ablation results for the auxiliary-loss-free balancing strategy. Compared with the purely auxiliary-loss-based method, the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks. 

Both of the baseline models purely use auxiliary losses to encourage load balance, and use the sigmoid gating function with top-K affinity normalization. Their hyper-parameters to control the strength of auxiliary losses are the same as DeepSeek-V2-Lite and DeepSeek-V2, respectively. On top of these two baseline models, keeping the training data and the other architectures the same, we remove all auxiliary losses and introduce the auxiliary-loss-free balancing strategy for comparison. From the table, we can observe that the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks.

---

[referencia=de539966b9f54c2c score=0.901]
22 

of 7.3 × 10<sup>−6</sup> in the remaining 167B tokens. The gradient clipping norm is set to 1.0. We employ a batch size scheduling strategy, where the batch size is gradually increased from 3072 to 15360 in the training of the first 469B tokens, and then keeps 15360 in the remaining training. We leverage pipeline parallelism to deploy different layers of a model on different GPUs, and for each layer, the routed experts will be uniformly deployed on 64 GPUs belonging to 8 nodes. As for the node-limited routing, each token will be sent to at most 4 nodes (i.e., _𝑀_ = 4). For auxiliary-loss-free load balancing, we set the bias update speed _𝛾_ to 0.001 for the first 14.3T tokens, and to 0.0 for the remaining 500B tokens. For the balance loss, we set _𝛼_ to 0.0001, just to avoid extreme imbalance within any single sequence. The MTP loss weight _𝜆_ is set to 0.3 for the first 10T tokens, and to 0.1 for the remaining 4.8T tokens. 



<!-- Start of picture text -->
Pressure Testing DeepSeek-V3 128K Context via "Needle In A HayStack"<br>10<br>0<br>7 9<br>14<br>21 8<br>29<br>7<br>36<br>43 6<br>50<br>57 5<br>64<br>4<br>71<br>79 3<br>86<br>93 2<br>100<br>1<br>2K 11K 20K 29K 38K 47K 56K 65K 74K 83K 92K 101K 110K 119K 128K<br>Context Length (#Tokens)<br>Score<br>Document Depth Percent (%)<br><!-- End of picture text -->

Figure 8 | Evaluation results on the ”Needle In A Haystack” (NIAH) tests. DeepSeek-V3 performs well across all context window lengths up to 128K.

---

[referencia=de539966b9f54c2c score=0.893]
#### **2.1. Basic Architecture** 

The basic architecture of DeepSeek-V3 is still within the Transformer (Vaswani et al., 2017) framework. For efficient inference and economical training, DeepSeek-V3 also adopts MLA and DeepSeekMoE, which have been thoroughly validated by DeepSeek-V2. Compared with DeepSeek-V2, an exception is that we additionally introduce an auxiliary-loss-free load balancing 

6 



<!-- Start of picture text -->

---

[referencia=de539966b9f54c2c score=0.881]
#### **3.2. Training Framework** 

The training of DeepSeek-V3 is supported by the HAI-LLM framework, an efficient and lightweight training framework crafted by our engineers from the ground up. On the whole, DeepSeek-V3 applies 16-way Pipeline Parallelism (PP) (Qi et al., 2023a), 64-way Expert Parallelism (EP) (Lepikhin et al., 2021) spanning 8 nodes, and ZeRO-1 Data Parallelism (DP) (Rajbhandari et al., 2020). 

In order to facilitate efficient training of DeepSeek-V3, we implement meticulous engineering optimizations. Firstly, we design the DualPipe algorithm for efficient pipeline parallelism. Compared with existing PP methods, DualPipe has fewer pipeline bubbles. More importantly, it overlaps the computation and communication phases across forward and backward processes, thereby addressing the challenge of heavy communication overhead introduced by cross-node expert parallelism. Secondly, we develop efficient cross-node all-to-all communication kernels to fully utilize IB and NVLink bandwidths and conserve Streaming Multiprocessors (SMs) dedicated to communication. Finally, we meticulously optimize the memory footprint during training, thereby enabling us to train DeepSeek-V3 without using costly Tensor Parallelism (TP).

---

[referencia=de539966b9f54c2c score=0.876]
### **4. Pre-Training** 

#### **4.1. Data Construction** 

Compared with DeepSeek-V2, we optimize the pre-training corpus by enhancing the ratio of mathematical and programming samples, while expanding multilingual coverage beyond 

21 

English and Chinese. Also, our data processing pipeline is refined to minimize redundancy while maintaining corpus diversity. Inspired by Ding et al. (2024), we implement the document packing method for data integrity but do not incorporate cross-sample attention masking during training. Finally, the training corpus for DeepSeek-V3 consists of 14.8T high-quality and diverse tokens in our tokenizer. 

In the training process of DeepSeekCoder-V2 (DeepSeek-AI, 2024a), we observe that the Fill-in-Middle (FIM) strategy does not compromise the next-token prediction capability while enabling the model to accurately predict middle text based on contextual cues. In alignment with DeepSeekCoder-V2, we also incorporate the FIM strategy in the pre-training of DeepSeek-V3. To be specific, we employ the Prefix-Suffix-Middle (PSM) framework to structure data as follows: 

`<|fim_begin|>` _𝑓_ pre `<|fim_hole|>` _𝑓_ suf `<|fim_end|>` _𝑓_ middle `<|eos_token|>` . 

This structure is applied at the document level as a part of the pre-packing process. The FIM strategy is applied at a rate of 0.1, consistent with the PSM framework. 

The tokenizer for DeepSeek-V3 employs Byte-level BPE (Shibata et al., 1999) with an extended vocabulary of 128K tokens. The pretokenizer and training data for our tokenizer are modified to optimize multilingual compression efficiency. In addition, compared with DeepSeek-V2, the new pretokenizer introduces tokens that combine punctuations and line breaks. However, this trick may introduce the token boundary bias (Lundberg, 2023) when the model processes multi-line prompts without terminal line breaks, particularly for few-shot evaluation prompts. To address this issue, we randomly split a certain proportion of such combined tokens during training, which exposes the model to a wider array of special cases and mitigates this bias.

---

[referencia=de539966b9f54c2c score=0.875]
#### **_2.1.2. DeepSeekMoE with Auxiliary-Loss-Free Load Balancing_** 

**Basic Architecture of DeepSeekMoE.** For Feed-Forward Networks (FFNs), DeepSeek-V3 employs the DeepSeekMoE architecture (Dai et al., 2024). Compared with traditional MoE architectures like GShard (Lepikhin et al., 2021), DeepSeekMoE uses finer-grained experts and isolates some experts as shared ones. Let **u** _𝑡_ denote the FFN input of the _𝑡_ -th token, we compute the FFN output **h** _𝑡_<sup>′as follows:</sup> 







8 

where _𝑁𝑠_ and _𝑁𝑟_ denote the numbers of shared experts and routed experts, respectively; FFN _𝑖_<sup>(</sup><sup>_𝑠_)</sup> (·) and FFN _𝑖_<sup>(</sup><sup>_𝑟_)</sup> (·) denote the _𝑖_ -th shared expert and the _𝑖_ -th routed expert, respectively; _𝐾𝑟_ denotes the number of activated routed experts; _𝑔𝑖_ , _𝑡_ is the gating value for the _𝑖_ -th expert; _𝑠𝑖_ , _𝑡_ is the token-to-expert affinity; **e** _𝑖_ is the centroid vector of the _𝑖_ -th routed expert; and Topk(·, _𝐾_ ) denotes the set comprising _𝐾_ highest scores among the affinity scores calculated for the _𝑡_ -th token and all routed experts. Slightly different from DeepSeek-V2, DeepSeek-V3 uses the sigmoid function to compute the affinity scores, and applies a normalization among all selected affinity scores to produce the gating values.

---

[referencia=de539966b9f54c2c score=0.868]
26 

|**Benchmark (Metric)**|**# Shots**|**Small MoE**<br>**Aux-Loss-Based**|**Small MoE**<br>**Aux-Loss-Free**|**Large MoE**<br>**Aux-Loss-Based**|**Large MoE**<br>**Aux-Loss-Free**|
|---|---|---|---|---|---|
|# Activated Params|-|2.4B|2.4B|20.9B|20.9B|
|# Total Params|-|15.7B|15.7B|228.7B|228.7B|
|# Training Tokens|-|1.33T|1.33T|578B|578B|
|Pile-test (BPB)|-|0.727|**0.724**|0.656|**0.652**|
|BBH (EM)|3-shot|37.3|**39.3**|66.7|**67.9**|
|MMLU (EM)|5-shot|51.0|**51.8**|**68.3**|67.2|
|DROP (F1)|1-shot|38.1|**39.0**|**67.1**|**67.1**|
|TriviaQA (EM)|5-shot|**58.3**|**58.5**|66.7|**67.7**|
|NaturalQuestions (EM)|5-shot|**23.2**|**23.4**|27.1|**28.1**|
|HumanEval (Pass@1)|0-shot|22.0|**22.6**|40.2|**46.3**|
|MBPP (Pass@1)|3-shot|**36.6**|35.8|59.2|**61.2**|
|GSM8K (EM)|8-shot|27.1|**29.6**|70.7|**74.5**|
|MATH (EM)|4-shot|**10.9**|**11.1**|37.2|**39.6**|



Table 5 | Ablation results for the auxiliary-loss-free balancing strategy. Compared with the purely auxiliary-loss-based method, the auxiliary-loss-free strategy consistently achieves better model performance on most of the evaluation benchmarks.

---

[referencia=de539966b9f54c2c score=0.866]
**Training Hyper-Parameters.** We employ the AdamW optimizer (Loshchilov and Hutter, 2017) with hyper-parameters set to _𝛽_ 1 = 0.9, _𝛽_ 2 = 0.95, and weight_decay = 0.1. We set the maximum sequence length to 4K during pre-training, and pre-train DeepSeek-V3 on 14.8T tokens. As for the learning rate scheduling, we first linearly increase it from 0 to 2.2 × 10<sup>−4</sup> during the first 2K steps. Then, we keep a constant learning rate of 2.2 × 10<sup>−4</sup> until the model consumes 10T training tokens. Subsequently, we gradually decay the learning rate to 2.2 × 10<sup>−5</sup> in 4.3T tokens, following a cosine decay curve. During the training of the final 500B tokens, we keep a constant learning rate of 2.2 × 10<sup>−5</sup> in the first 333B tokens, and switch to another constant learning rate 

22

---

[referencia=de539966b9f54c2c score=0.865]
||CMMLU (EM)|5-shot|84.0|**89.5**|73.7|88.8|
|Chinese|CMRC (EM)|1-shot|**77.4**|75.8|76.0|76.3|
||C3 (EM)|0-shot|77.4|76.7|**79.7**|78.6|
||CCPM (EM)|0-shot|**93.0**|88.5|78.6|92.0|
|Multilingual|MMMLU-non-English (EM)|5-shot|64.0|74.8|73.8|**79.4**|



Table 3 | Comparison among DeepSeek-V3-Base and other representative open-source base models. All models are evaluated in our internal framework and share the same evaluation setting. Scores with a gap not exceeding 0.3 are considered to be at the same level. DeepSeekV3-Base achieves the best performance on most benchmarks, especially on math and code tasks. 

of DeepSeek-V2-Base exhibits a slight difference from our previously reported results. Overall, DeepSeek-V3-Base comprehensively outperforms DeepSeek-V2-Base and Qwen2.5 72B Base, and surpasses LLaMA-3.1 405B Base in the majority of benchmarks, essentially becoming the strongest open-source model. 

From a more detailed perspective, we compare DeepSeek-V3-Base with the other open-source base models individually. (1) Compared with DeepSeek-V2-Base, due to the improvements in our model architecture, the scale-up of the model size and training tokens, and the enhancement of data quality, DeepSeek-V3-Base achieves significantly better performance as expected. (2) Compared with Qwen2.5 72B Base, the state-of-the-art Chinese open-source model, with only half of the activated parameters, DeepSeek-V3-Base also demonstrates remarkable advantages, 

25

---

[referencia=de539966b9f54c2c score=0.826]
In the remainder of this paper, we first present a detailed exposition of our DeepSeek-V3 model architecture (Section 2). Subsequently, we introduce our infrastructures, encompassing our compute clusters, the training framework, the support for FP8 training, the inference deployment strategy, and our suggestions on future hardware design. Next, we describe our pre-training process, including the construction of training data, hyper-parameter settings, longcontext extension techniques, the associated evaluations, as well as some discussions (Section 4). Thereafter, we discuss our efforts on post-training, which include Supervised Fine-Tuning (SFT), Reinforcement Learning (RL), the corresponding evaluations, and discussions (Section 5). Lastly, we conclude this work, discuss existing limitations of DeepSeek-V3, and propose potential directions for future research (Section 6).

---

[referencia=de539966b9f54c2c score=0.824]
#### **_3.4.1. Prefilling_** 

The minimum deployment unit of the prefilling stage consists of 4 nodes with 32 GPUs. The `attention` part employs 4-way Tensor Parallelism (TP4) with Sequence Parallelism (SP), combined with 8-way Data Parallelism (DP8). Its small TP size of 4 limits the overhead of TP communication. For the `MoE` part, we use 32-way Expert Parallelism (EP32), which ensures that each expert processes a sufficiently large batch size, thereby enhancing computational efficiency. For the `MoE` all-to-all communication, we use the same method as in training: first transferring tokens across nodes via IB, and then forwarding among the intra-node GPUs via NVLink. In particular, we use 1-way Tensor Parallelism for the dense MLPs in shallow layers to save TP communication. 

To achieve load balancing among different experts in the `MoE` part, we need to ensure that each GPU processes approximately the same number of tokens. To this end, we introduce a deployment strategy of _redundant experts_ , which duplicates high-load experts and deploys them redundantly. The high-load experts are detected based on statistics collected during the online deployment and are adjusted periodically (e.g., every 10 minutes). After determining the set of redundant experts, we carefully rearrange experts among GPUs within a node based on the observed loads, striving to balance the load across GPUs as much as possible without increasing the cross-node all-to-all communication overhead. For the deployment of DeepSeek-V3, we set 32 redundant experts for the prefilling stage. For each GPU, besides the original 8 experts it hosts, it will also host one additional redundant expert. 

Furthermore, in the prefilling stage, to improve the throughput and hide the overhead of all-to-all and TP communication, we simultaneously process two micro-batches with similar computational workloads, overlapping the `attention` and `MoE` of one micro-batch with the `dispatch` and `combine` of another.