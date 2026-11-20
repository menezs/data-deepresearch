[referencia=de539966b9f54c2c score=0.980]
### **1. Introduction** 

In recent years, Large Language Models (LLMs) have been undergoing rapid iteration and evolution (Anthropic, 2024; Google, 2024; OpenAI, 2024a), progressively diminishing the gap towards Artificial General Intelligence (AGI). Beyond closed-source models, open-source models, including DeepSeek series (DeepSeek-AI, 2024a,b,c; Guo et al., 2024), LLaMA series (AI@Meta, 2024a,b; Touvron et al., 2023a,b), Qwen series (Qwen, 2023, 2024a,b), and Mistral series (Jiang et al., 2023; Mistral, 2024), are also making significant strides, endeavoring to close the gap with their closed-source counterparts. To further push the boundaries of open-source model capabilities, we scale up our models and introduce DeepSeek-V3, a large Mixture-of-Experts (MoE) model with 671B parameters, of which 37B are activated for each token. 

With a forward-looking perspective, we consistently strive for strong model performance and economical costs. Therefore, in terms of architecture, DeepSeek-V3 still adopts Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference and DeepSeekMoE (Dai et al., 2024) for cost-effective training. These two architectures have been validated in DeepSeekV2 (DeepSeek-AI, 2024c), demonstrating their capability to maintain robust model performance while achieving efficient training and inference. Beyond the basic architecture, we implement two additional strategies to further enhance the model capabilities. Firstly, DeepSeek-V3 pioneers an auxiliary-loss-free strategy (Wang et al., 2024a) for load balancing, with the aim of minimizing the adverse impact on model performance that arises from the effort to encourage load balancing. Secondly, DeepSeek-V3 employs a multi-token prediction training objective, which we have observed to enhance the overall performance on evaluation benchmarks.

---

[referencia=de539966b9f54c2c score=0.940]
## **Abstract** 

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at `https://github.com/deepseek-ai/DeepSeek-V3` . 



<!-- Start of picture text -->

---

[referencia=de539966b9f54c2c score=0.929]
#### **4.2. Hyper-Parameters** 

**Model Hyper-Parameters.** We set the number of Transformer layers to 61 and the hidden dimension to 7168. All learnable parameters are randomly initialized with a standard deviation of 0.006. In MLA, we set the number of attention heads _𝑛ℎ_ to 128 and the per-head dimension _𝑑ℎ_ to 128. The KV compression dimension _𝑑𝑐_ is set to 512, and the query compression dimension _𝑑𝑐_<sup>′</sup> is set to 1536. For the decoupled queries and key, we set the per-head dimension _𝑑ℎ_<sup>_𝑅_to 64.We</sup> substitute all FFNs except for the first three layers with MoE layers. Each MoE layer consists of 1 shared expert and 256 routed experts, where the intermediate hidden dimension of each expert is 2048. Among the routed experts, 8 experts will be activated for each token, and each token will be ensured to be sent to at most 4 nodes. The multi-token prediction depth _𝐷_ is set to 1, i.e., besides the exact next token, each token will predict one additional token. As DeepSeek-V2, DeepSeek-V3 also employs additional RMSNorm layers after the compressed latent vectors, and multiplies additional scaling factors at the width bottlenecks. Under this configuration, DeepSeek-V3 comprises 671B total parameters, of which 37B are activated for each token.

---

[referencia=de539966b9f54c2c score=0.906]
#### **_2.1.1. Multi-Head Latent Attention_** 

For attention, DeepSeek-V3 adopts the MLA architecture. Let _𝑑_ denote the embedding dimension, _𝑛ℎ_ denote the number of attention heads, _𝑑ℎ_ denote the dimension per head, and **h** _𝑡_ ∈ **R**<sup>_𝑑_</sup> denote the attention input for the _𝑡_ -th token at a given attention layer. The core of MLA is the low-rank joint compression for attention keys and values to reduce Key-Value (KV) cache during inference: 



7

---

[referencia=de539966b9f54c2c score=0.902]
### **2. Architecture** 

We first introduce the basic architecture of DeepSeek-V3, featured by Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference and DeepSeekMoE (Dai et al., 2024) for economical training. Then, we present a Multi-Token Prediction (MTP) training objective, which we have observed to enhance the overall performance on evaluation benchmarks. For other minor details not explicitly mentioned, DeepSeek-V3 adheres to the settings of DeepSeekV2 (DeepSeek-AI, 2024c).

---

[referencia=de539966b9f54c2c score=0.874]
### **6. Conclusion, Limitations, and Future Directions** 

In this paper, we introduce DeepSeek-V3, a large MoE language model with 671B total parameters and 37B activated parameters, trained on 14.8T tokens. In addition to the MLA and DeepSeekMoE architectures, it also pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. The training of DeepSeek-V3 is cost-effective due to the support of FP8 training and meticulous engineering optimizations. The post-training also makes a success in distilling the reasoning capability from the DeepSeek-R1 series of models. Comprehensive evaluations demonstrate that DeepSeek-V3 has emerged as the strongest open-source model currently available, and achieves performance comparable to leading closed-source models like GPT-4o and Claude-3.5-Sonnet. Despite its strong performance, it also maintains economical training costs. It requires only 2.788M H800 GPU hours for its full training, including pre-training, context length extension, and post-training. 

While acknowledging its strong performance and cost-effectiveness, we also recognize that DeepSeek-V3 has some limitations, especially on the deployment. Firstly, to ensure efficient inference, the recommended deployment unit for DeepSeek-V3 is relatively large, which might pose a burden for small-sized teams. Secondly, although our deployment strategy for DeepSeekV3 has achieved an end-to-end generation speed of more than two times that of DeepSeek-V2, there still remains potential for further enhancement. Fortunately, these limitations are expected to be naturally addressed with the development of more advanced hardware. 

DeepSeek consistently adheres to the route of open-source models with longtermism, aiming to steadily approach the ultimate goal of AGI (Artificial General Intelligence). In the future, we plan to strategically invest in research across the following directions. 

- We will consistently study and refine our model architectures, aiming to further improve both the training and inference efficiency, striving to approach efficient support for infinite context length. Additionally, we will try to break through the architectural limitations of Transformer, thereby pushing the boundaries of its modeling capabilities. 

35

---

[referencia=de539966b9f54c2c score=0.836]
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

[referencia=de539966b9f54c2c score=0.801]
<br>𝑄𝑄<br>𝑡𝑡 𝑡𝑡<br>𝐜𝐜 … … 𝐜𝐜<br>Input Hidden<br>𝑡𝑡<br>𝐡𝐡<br><!-- End of picture text -->

Figure 2 | Illustration of the basic architecture of DeepSeek-V3. Following DeepSeek-V2, we adopt MLA and DeepSeekMoE for efficient inference and economical training. 

strategy (Wang et al., 2024a) for DeepSeekMoE to mitigate the performance degradation induced by the effort to ensure load balance. Figure 2 illustrates the basic architecture of DeepSeek-V3, and we will briefly review the details of MLA and DeepSeekMoE in this section.

---

[referencia=de539966b9f54c2c score=0.759]
7 

where **c** _𝑡_<sup>_𝐾𝑉_</sup> ∈ **R**<sup>_𝑑𝑐_</sup> is the compressed latent vector for keys and values; _𝑑𝑐_ (≪ _𝑑ℎ𝑛ℎ_ ) indicates the KV compression dimension; _𝑊_<sup>_𝐷𝐾𝑉_</sup> ∈ **R**<sup>_𝑑𝑐_×</sup><sup>_𝑑_</sup> denotes the down-projection matrix; _𝑊_<sup>_𝑈𝐾_</sup> , _𝑊_<sup>_𝑈𝑉_</sup> ∈ **R**<sup>_𝑑ℎ𝑛ℎ_×</sup><sup>_𝑑𝑐_</sup> are the up-projection matrices for keys and values, respectively; _𝑊_<sup>_𝐾𝑅_</sup> ∈ **R**<sup>_𝑑_</sup> _ℎ_<sup>_𝑅_×</sup><sup>_𝑑_</sup> is the matrix used to produce the decoupled key that carries Rotary Positional Embedding (RoPE) (Su et al., 2024); RoPE(·) denotes the operation that applies RoPE matrices; and [·; ·] denotes concatenation. Note that for MLA, only the blue-boxed vectors (i.e., **c** _𝑡_<sup>_𝐾𝑉_</sup> and **k** _𝑡_<sup>_𝑅_) need to be cached during generation,</sup> which results in significantly reduced KV cache while maintaining performance comparable to standard Multi-Head Attention (MHA) (Vaswani et al., 2017). 

For the attention queries, we also perform a low-rank compression, which can reduce the activation memory during training:

---

[referencia=de539966b9f54c2c score=0.733]
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

[referencia=de539966b9f54c2c score=0.561]
#### **_5.3.2. Standard Evaluation_** 

Table 6 presents the evaluation results, showcasing that DeepSeek-V3 stands as the bestperforming open-source model. Additionally, it is competitive against frontier closed-source models like GPT-4o and Claude-3.5-Sonnet. 

31 

**English Benchmarks.** MMLU is a widely recognized benchmark designed to assess the performance of large language models, across diverse knowledge domains and tasks. DeepSeek-V3 demonstrates competitive performance, standing on par with top-tier models such as LLaMA3.1-405B, GPT-4o, and Claude-Sonnet 3.5, while significantly outperforming Qwen2.5 72B. Moreover, DeepSeek-V3 excels in MMLU-Pro, a more challenging educational knowledge benchmark, where it closely trails Claude-Sonnet 3.5. On MMLU-Redux, a refined version of MMLU with corrected labels, DeepSeek-V3 surpasses its peers. In addition, on GPQA-Diamond, a PhD-level evaluation testbed, DeepSeek-V3 achieves remarkable results, ranking just behind Claude 3.5 Sonnet and outperforming all other competitors by a substantial margin.

---

[referencia=de539966b9f54c2c score=0.527]
#### **2.1. Basic Architecture** 

The basic architecture of DeepSeek-V3 is still within the Transformer (Vaswani et al., 2017) framework. For efficient inference and economical training, DeepSeek-V3 also adopts MLA and DeepSeekMoE, which have been thoroughly validated by DeepSeek-V2. Compared with DeepSeek-V2, an exception is that we additionally introduce an auxiliary-loss-free load balancing 

6 



<!-- Start of picture text -->

---

[referencia=de539966b9f54c2c score=0.479]
DeepSeekMoE<br>… … Routed Expert<br>Transformer Block  × Output Hidden ′ Shared Expert<br>𝑡𝑡<br>𝐡𝐡<br>𝐿𝐿<br>1 … 1 2 3 4 … -1<br>Feed-Forward Network 0<br>𝑠𝑠 𝑟𝑟 𝑟𝑟<br>𝑁𝑁 𝑁𝑁 𝑁𝑁<br>RMSNorm Router Top-<br>…1… 𝐾𝐾 Input Hidden 𝑟𝑟<br>Multi-Head Latent Attention (MLA) 𝐮𝐮𝑡𝑡<br>Cached During Inference<br>Attention<br>0 Output Hidden  … …<br>𝑡𝑡<br>𝐮𝐮 Multi-Head Attention<br>RMSNorm<br>]} ]}<br>𝐶𝐶𝑡𝑡,𝑖𝑖 concatenate 𝑅𝑅𝑡𝑡,𝑖𝑖 𝐶𝐶𝑡𝑡,𝑖𝑖 concatenate 𝑅𝑅𝑡𝑡<br>{[𝐪𝐪 ; 𝐪𝐪 {[𝐤𝐤 ; 𝐤𝐤<br>} } } }<br>𝐶𝐶 𝑅𝑅 apply apply 𝑅𝑅 𝐶𝐶 𝐶𝐶<br>{𝐪𝐪𝑡𝑡,𝑖𝑖 {𝐪𝐪𝑡𝑡,𝑖𝑖 RoPE 𝐤𝐤 RoPE 𝑡𝑡 {𝐤𝐤𝑡𝑡,𝑖𝑖 {𝐯𝐯𝑡𝑡,𝑖𝑖<br>… Latent  Latent  𝐾 …<br>𝑄𝑄<br>𝑡𝑡 𝑡𝑡<br>𝐜𝐜 … … 𝐜𝐜<br>Input Hidden<br>𝑡𝑡<br>

---

[referencia=de539966b9f54c2c score=0.440]
#### **_5.3.3. Open-Ended Evaluation_** 

In addition to standard benchmarks, we also evaluate our models on open-ended generation tasks using LLMs as judges, with the results shown in Table 7. Specifically, we adhere to the original configurations of AlpacaEval 2.0 (Dubois et al., 2024) and Arena-Hard (Li et al., 2024a), which leverage GPT-4-Turbo-1106 as judges for pairwise comparisons. On Arena-Hard, DeepSeek-V3 achieves an impressive win rate of over 86% against the baseline GPT-4-0314, 

performing on par with top-tier models like Claude-Sonnet-3.5-1022. This underscores the 

robust capabilities of DeepSeek-V3, especially in dealing with complex prompts, including coding and debugging tasks. Furthermore, DeepSeek-V3 achieves a groundbreaking milestone 

as the first open-source model to surpass 85% on the Arena-Hard benchmark. This achievement significantly bridges the performance gap between open-source and closed-source models, setting a new standard for what open-source models can accomplish in challenging domains. 

Similarly, DeepSeek-V3 showcases exceptional performance on AlpacaEval 2.0, outperforming both closed-source and open-source models. This demonstrates its outstanding proficiency in 

writing tasks and handling straightforward question-answering scenarios. Notably, it surpasses DeepSeek-V2.5-0905 by a significant margin of 20%, highlighting substantial improvements in tackling simple tasks and showcasing the effectiveness of its advancements.

---

[referencia=de539966b9f54c2c score=0.433]
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

[referencia=de539966b9f54c2c score=0.407]
In order to achieve efficient training, we support the FP8 mixed precision training and implement comprehensive optimizations for the training framework. Low-precision training has emerged as a promising solution for efficient training (Dettmers et al., 2022; Kalamkar et al., 2019; Narang et al., 2017; Peng et al., 2023b), its evolution being closely tied to advancements in hardware capabilities (Luo et al., 2024; Micikevicius et al., 2022; Rouhani et al., 2023a). In this work, we introduce an FP8 mixed precision training framework and, for the first time, validate its effectiveness on an extremely large-scale model. Through the support for FP8 computation and storage, we achieve both accelerated training and reduced GPU memory usage. As for the training framework, we design the DualPipe algorithm for efficient pipeline parallelism, which has fewer pipeline bubbles and hides most of the communication during training through computation-communication overlap. This overlap ensures that, as the model further scales up, as long as we maintain a constant computation-to-communication ratio, we can still employ fine-grained experts across nodes while achieving a near-zero all-to-all communication overhead. In addition, we also develop efficient cross-node all-to-all communication kernels to fully utilize InfiniBand (IB) and NVLink bandwidths. Furthermore, we meticulously optimize the memory footprint, making it possible to train DeepSeek-V3 without using costly tensor parallelism. Combining these efforts, we achieve high training efficiency. 

During pre-training, we train DeepSeek-V3 on 14.8T high-quality and diverse tokens. The pre-training process is remarkably stable. Throughout the entire training process, we did not encounter any irrecoverable loss spikes or have to roll back. Next, we conduct a two-stage context length extension for DeepSeek-V3. In the first stage, the maximum context length is extended to 32K, and in the second stage, it is further extended to 128K. Following this, we conduct post-training, including Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) on the base model of DeepSeek-V3, to align it with human preferences and further unlock its potential. During the post-training stage, we distill the reasoning capability from the DeepSeekR1 series of models, and meanwhile carefully maintain the balance between model accuracy 

4

---

[referencia=de539966b9f54c2c score=0.405]
||**Benchmark (Metric)**|**# Shots**|**DeepSeek-V2**<br>**Base**|**Qwen2.5**<br>**72B Base**|**LLaMA-3.1**<br>**405B Base**|**DeepSeek-V3**<br>**Base**|
|---|---|---|---|---|---|---|
||Architecture|-|MoE|Dense|Dense|MoE|
||# Activated Params|-|21B|72B|405B|37B|
||# Total Params|-|236B|72B|405B|671B|
||Pile-test (BPB)|-|0.606|0.638|**0.542**|0.548|
||BBH (EM)|3-shot|78.8|79.8|82.9|**87.5**|
||MMLU (EM)|5-shot|78.4|85.0|84.4|**87.1**|
||MMLU-Redux (EM)|5-shot|75.6|83.2|81.3|**86.2**|
||MMLU-Pro (EM)|5-shot|51.4|58.3|52.8|**64.4**|
||DROP (F1)|3-shot|80.4|80.6|86.0|**89.0**|
||ARC-Easy (EM)|25-shot|97.6|98.4|98.4|**98.9**|
|Elih|ARC-Challenge (EM)|25-shot|92.2|94.5|**95.3**|**95.3**|
|ngs|HellaSwag (EM)|10-shot|87.1|84.8|**89.2**|**88.9**|
||PIQA (EM)|0-shot|83.9|82.6|**85.9**|84.7|
||WinoGrande (EM)|5-shot|**86.3**|82.3|85.2|84.9|
||RACE-Middle (EM)|5-shot|73.1|68.1|**74.2**|67.1|

---

[referencia=de539966b9f54c2c score=0.338]
#### **4.3. Long Context Extension** 

We adopt a similar approach to DeepSeek-V2 (DeepSeek-AI, 2024c) to enable long context capabilities in DeepSeek-V3. After the pre-training stage, we apply YaRN (Peng et al., 2023a) for context extension and perform two additional training phases, each comprising 1000 steps, to progressively expand the context window from 4K to 32K and then to 128K. The YaRN configuration is consistent with that used in DeepSeek-V2, being applied exclusively to the decoupled shared key **k** _𝑡_<sup>_𝑅_.The hyper-parameters remain identical across both phases, with the</sup> scale _𝑠_ = 40, _𝛼_ = 1, _𝛽_ = 32, and the scaling factor<sup>~~√~~</sup> _𝑡_ = 0.1 ln _𝑠_ + 1. In the first phase, the sequence length is set to 32K, and the batch size is 1920. During the second phase, the sequence length is increased to 128K, and the batch size is reduced to 480. The learning rate for both phases is set to 7.3 × 10<sup>−6</sup> , matching the final learning rate from the pre-training stage. 

Through this two-phase extension training, DeepSeek-V3 is capable of handling inputs up to 128K in length while maintaining strong performance. Figure 8 illustrates that DeepSeek-V3, following supervised fine-tuning, achieves notable performance on the "Needle In A Haystack" (NIAH) test, demonstrating consistent robustness across context window lengths up to 128K. 

23 

#### **4.4. Evaluations**

---

[referencia=de539966b9f54c2c score=0.326]
#### **Summary of Core Evaluation Results** 

- **Knowledge** : (1) On educational benchmarks such as MMLU, MMLU-Pro, and GPQA, DeepSeek-V3 outperforms all other open-source models, achieving 88.5 on MMLU, 75.9 on MMLU-Pro, and 59.1 on GPQA. Its performance is comparable to leading closed-source models like GPT-4o and Claude-Sonnet-3.5, narrowing the gap between open-source and closed-source models in this domain. (2) For factuality benchmarks, DeepSeek-V3 demonstrates superior performance among open-source models on both SimpleQA and Chinese SimpleQA. While it trails behind GPT-4o and Claude-Sonnet-3.5 in English factual knowledge (SimpleQA), it surpasses these models in Chinese factual knowledge (Chinese SimpleQA), highlighting its strength in Chinese factual knowledge. 

- **Code, Math, and Reasoning** : (1) DeepSeek-V3 achieves state-of-the-art performance on math-related benchmarks among all non-long-CoT open-source and closed-source models. Notably, it even outperforms o1-preview on specific benchmarks, such as MATH-500, demonstrating its robust mathematical reasoning capabilities. (2) On coding-related tasks, DeepSeek-V3 emerges as the top-performing model for coding competition benchmarks, such as LiveCodeBench, solidifying its position as the leading model in this domain. For engineering-related tasks, while DeepSeek-V3 performs slightly below Claude-Sonnet-3.5, it still outpaces all other models by a significant margin, demonstrating its competitiveness across diverse technical benchmarks.

---

[referencia=de539966b9f54c2c score=0.314]
#### **_3.4.1. Prefilling_** 

The minimum deployment unit of the prefilling stage consists of 4 nodes with 32 GPUs. The `attention` part employs 4-way Tensor Parallelism (TP4) with Sequence Parallelism (SP), combined with 8-way Data Parallelism (DP8). Its small TP size of 4 limits the overhead of TP communication. For the `MoE` part, we use 32-way Expert Parallelism (EP32), which ensures that each expert processes a sufficiently large batch size, thereby enhancing computational efficiency. For the `MoE` all-to-all communication, we use the same method as in training: first transferring tokens across nodes via IB, and then forwarding among the intra-node GPUs via NVLink. In particular, we use 1-way Tensor Parallelism for the dense MLPs in shallow layers to save TP communication. 

To achieve load balancing among different experts in the `MoE` part, we need to ensure that each GPU processes approximately the same number of tokens. To this end, we introduce a deployment strategy of _redundant experts_ , which duplicates high-load experts and deploys them redundantly. The high-load experts are detected based on statistics collected during the online deployment and are adjusted periodically (e.g., every 10 minutes). After determining the set of redundant experts, we carefully rearrange experts among GPUs within a node based on the observed loads, striving to balance the load across GPUs as much as possible without increasing the cross-node all-to-all communication overhead. For the deployment of DeepSeek-V3, we set 32 redundant experts for the prefilling stage. For each GPU, besides the original 8 experts it hosts, it will also host one additional redundant expert. 

Furthermore, in the prefilling stage, to improve the throughput and hide the overhead of all-to-all and TP communication, we simultaneously process two micro-batches with similar computational workloads, overlapping the `attention` and `MoE` of one micro-batch with the `dispatch` and `combine` of another.