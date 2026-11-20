[referencia=3b850513f2939af4 score=0.808]
2024-12-27

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V3.

  152    - Open-source models (e.g., OLMo): weights and data available, paper with most details (but not necessarily the rationale, failed experiments)

[Groeneveld+ 2024]
OLMo: Accelerating the Science of Language Models

[AI2] Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney ... (33 more) ... Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A. Smith, Hannaneh Hajishirzi

2024-02-01

---

[referencia=3b850513f2939af4 score=0.642]
2024-12-27

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V3.

   147     [Groeneveld+ 2024]
OLMo: Accelerating the Science of Language Models

[AI2] Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney ... (33 more) ... Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A. Smith, Hannaneh Hajishirzi

2024-02-01

Language models (LMs) have become ubiquitous in both NLP research and in commercial product offerings. As their commercial importance has surged, the most powerful models have become closed off, gated behind proprietary interfaces, with important details of their training data, architectures, and development undisclosed. Given the importance of these details in scientifically studying these models, including their biases and potential risks, we believe it is essential for the research community to have access to powerful, truly open LMs. To this end, we have built OLMo, a competitive, truly Open Language Model, to enable the scientific study of language models. Unlike most prior efforts that have only released model weights and inference code, we release OLMo alongside open training data and training and evaluation code. We hope this release will empower the open research community and inspire a new wave of innovation.

---

[referencia=3b850513f2939af4 score=0.251]
   146     [DeepSeek-AI+ 2024]
DeepSeek LLM: Scaling Open-Source Language Models with Longtermism

[DeepSeek] DeepSeek-AI, :, Xiao Bi, Deli Chen, Guanting Chen ... (78 more) ... Yao Zhao, Shangyan Zhou, Shunfeng Zhou, Qihao Zhu, Yuheng Zou

2024-01-05

The rapid development of open-source large language models (LLMs) has been truly remarkable. However, the scaling law described in previous literature presents varying conclusions, which casts a dark cloud over scaling LLMs. We delve into the study of scaling laws and present our distinctive findings that facilitate scaling of large scale models in two commonly used open-source configurations, 7B and 67B. Guided by the scaling laws, we introduce DeepSeek LLM, a project dedicated to advancing open-source language models with a long-term perspective. To support the pre-training phase, we have developed a dataset that currently consists of 2 trillion tokens and is continuously expanding. We further conduct supervised fine-tuning (SFT) and Direct Preference Optimization (DPO) on DeepSeek LLM Base models, resulting in the creation of DeepSeek Chat models. Our evaluation results demonstrate that DeepSeek LLM 67B surpasses LLaMA-2 70B on various benchmarks, particularly in the domains of code, mathematics, and reasoning. Furthermore, open-ended evaluations reveal that DeepSeek LLM 67B Chat exhibits superior performance compared to GPT-3.5.

Data: DeepSeek, The Stack, Reddit, etc. (2T tokens)

Architecture: LLaMA, but: for GQA increased depth, 67B parameters

Scaling laws: used non-embedding FLOPs with IsoFLOP

 [DeepSeek-AI+ 2024]
DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model

DeepSeek-AI, Aixin Liu, Bei Feng, Bin Wang, Bingxuan Wang ... (147 more) ... Zhuoshu Li, Zihan Wang, Zihui Gu, Zilin Li, Ziwei Xie

2024-05-07

---

[referencia=3b850513f2939af4 score=0.248]
15T tokens

405B parameters

   145     [Qwen+ 2024]
Qwen2.5 Technical Report

[Alibaba] Qwen, :, An Yang, Baosong Yang, Beichen Zhang ... (34 more) ... Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zihan Qiu

2024-12-19

In this report, we introduce Qwen2.5, a comprehensive series of large language models (LLMs) designed to meet diverse needs. Compared to previous iterations, Qwen 2.5 has been significantly improved during both the pre-training and post-training stages. In terms of pre-training, we have scaled the high-quality pre-training datasets from the previous 7 trillion tokens to 18 trillion tokens. This provides a strong foundation for common sense, expert knowledge, and reasoning capabilities. In terms of post-training, we implement intricate supervised finetuning with over 1 million samples, as well as multistage reinforcement learning. Post-training techniques enhance human preference, and notably improve long text generation, structural data analysis, and instruction following. To handle diverse and varied use cases effectively, we present Qwen2.5 LLM series in rich sizes. Open-weight offerings include base and instruction-tuned models, with quantized versions available. In addition, for hosted solutions, the proprietary models currently include two mixture-of-experts (MoE) variants: Qwen2.5-Turbo and Qwen2.5-Plus, both available from Alibaba Cloud Model Studio. Qwen2.5 has demonstrated top-tier performance on a wide range of benchmarks evaluating language understanding, reasoning, mathematics, coding, human preference alignment, etc. Specifically, the open-weight flagship Qwen2.5-72B-Instruct outperforms a number of open and proprietary models and demonstrates competitive performance to the state-of-the-art open-weight model, Llama-3-405B-Instruct, which is around 5 times larger. Qwen2.5-Turbo and Qwen2.5-Plus offer superior cost-effectiveness while performing competitively against GPT-4o-mini and GPT-4o respectively. Additionally, as the foundation, Qwen2.5 models have been instrumental in training specialized models such as Qwen2.5-Math, Qwen2.5-Coder, QwQ, and multimodal models.

---

[referencia=3b850513f2939af4 score=0.234]
2024-05-07

We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation. Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential. Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models.

 [DeepSeek-AI+ 2024]
DeepSeek-V3 Technical Report

DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang ... (190 more) ... Zilin Li, Ziwei Xie, Ziyang Song, Ziyi Gao, Zizheng Pan

2024-12-27

---

[referencia=3b850513f2939af4 score=0.221]
   148

150    - Closed models (e.g., GPT-4o): API access only

[OpenAI+ 2023]
GPT-4 Technical Report

[OpenAI] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad ... (271 more) ... Shengjia Zhao, Tianhao Zheng, Juntang Zhuang, William Zhuk, Barret Zoph

2023-03-15

We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

No details on the data or model architecture.

  151    - Open-weight models (e.g., DeepSeek): weights available, paper with architecture details, some training details, no data details

[DeepSeek-AI+ 2024]
DeepSeek-V3 Technical Report

DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang ... (190 more) ... Zilin Li, Ziwei Xie, Ziyang Song, Ziyi Gao, Zizheng Pan

2024-12-27

---

[referencia=3b850513f2939af4 score=0.115]
Data: subset of Dolma (2.46T tokens, CommonCrawl, The Stack, Reddit, etc.)

Architecture: no biases, non-parametric layer norm, SwiGLU (8/3 d increased to closest multiple of 128)

Training: 256x4 AMD MI250X on LUMI supercomputer, 27x8 A100s, 800Gbps interconnect

 [OLMo+ 2024]
2 OLMo 2 Furious

[AI2] Team OLMo, Pete Walsh, Luca Soldaini, Dirk Groeneveld, Kyle Lo ... (30 more) ... Michael Wilson, Luke Zettlemoyer, Ali Farhadi, Noah A. Smith, Hannaneh Hajishirzi

2024-12-31

We present OLMo 2, the next generation of our fully open language models. OLMo 2 includes dense autoregressive models with improved architecture and training recipe, pretraining data mixtures, and instruction tuning recipes. Our modified model architecture and training recipe achieve both better training stability and improved per-token efficiency. Our updated pretraining data mixture introduces a new, specialized data mix called Dolmino Mix 1124, which significantly improves model capabilities across many downstream task benchmarks when introduced via late-stage curriculum training (i.e. specialized data during the annealing phase of pretraining). Finally, we incorporate best practices from T\"ulu 3 to develop OLMo 2-Instruct, focusing on permissive data and extending our final-stage reinforcement learning with verifiable rewards (RLVR). Our OLMo 2 base models sit at the Pareto frontier of performance to compute, often matching or outperforming open-weight only models like Llama 3.1 and Qwen 2.5 while using fewer FLOPs and with fully transparent training data, code, and recipe. Our fully open OLMo 2-Instruct models are competitive with or surpassing open-weight only models of comparable size, including Qwen 2.5, Llama 3.1 and Gemma 2. We release all OLMo 2 artifacts openly -- models at 7B and 13B scales, both pretrained and post-trained, including their full training data, training code and recipes, training logs and thousands of intermediate checkpoints. The final instruction model is available on the Ai2 Playground as a free research demo.

   148

---

[referencia=3b850513f2939af4 score=0.078]
2023-07-18

In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases. Our models outperform open-source chat models on most benchmarks we tested, and based on our human evaluations for helpfulness and safety, may be a suitable substitute for closed-source models. We provide a detailed description of our approach to fine-tuning and safety improvements of Llama 2-Chat in order to enable the community to build on our work and contribute to the responsible development of LLMs.

 [Grattafiori+ 2024]
The Llama 3 Herd of Models

[Meta] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian ... (551 more) ... Zef Rosnbrick, Zhaoduo Wen, Zhenyu Yang, Zhiwei Zhao, Zhiyu Ma

2024-07-31

Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development.

15T tokens

405B parameters

   145     [Qwen+ 2024]
Qwen2.5 Technical Report

---

[referencia=3b850513f2939af4 score=0.077]
2024-02-01

Language models (LMs) have become ubiquitous in both NLP research and in commercial product offerings. As their commercial importance has surged, the most powerful models have become closed off, gated behind proprietary interfaces, with important details of their training data, architectures, and development undisclosed. Given the importance of these details in scientifically studying these models, including their biases and potential risks, we believe it is essential for the research community to have access to powerful, truly open LMs. To this end, we have built OLMo, a competitive, truly Open Language Model, to enable the scientific study of language models. Unlike most prior efforts that have only released model weights and inference code, we release OLMo alongside open training data and training and evaluation code. We hope this release will empower the open research community and inspire a new wave of innovation.

Data: subset of Dolma (2.46T tokens, CommonCrawl, The Stack, Reddit, etc.)

Architecture: no biases, non-parametric layer norm, SwiGLU (8/3 d increased to closest multiple of 128)

Training: 256x4 AMD MI250X on LUMI supercomputer, 27x8 A100s, 800Gbps interconnect

  153

154    ## Today's frontier models


 160     [DeepSeek-AI+ 2025]
DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song ... (190 more) ... Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang

2025-01-22

---

[referencia=3b850513f2939af4 score=0.066]
2024-05-07

We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference. It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens. DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE. MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation. Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times. We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential. Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models.

  273    - State-space models: Hyena

[Poli+ 2023]
Hyena Hierarchy: Towards Larger Convolutional Language Models

Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, Christopher Ré

2023-02-21

---

[referencia=3b850513f2939af4 score=0.061]
2022-03-29

We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4 more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

Introduced the rigorous analysis scaling laws for language models

Key improvement over Kaplan: tune learning rate for the compute budget

Approach 1: for each model size, train with 4 learning rates, vary number of training tokens, fit lower envelope

Approach 2 (IsoFLOP): for each model size, train with 9 training budgets, take last point

Approach 3: fit parametric function L(N, D) = E + A/N^alpha + B/D^beta to data collected from approaches 1 and 2

Conclusion: model and data should scale up at same rate

Table 3: extrapolate to 10 trillion parameters

MassiveText, different data distribution (1.5 trillion tokens)

70B parameters

  139

141    - EleutherAI's open datasets (The Pile) and models (GPT-J)

[Gao+ 2020]
The Pile: An 800GB Dataset of Diverse Text for Language Modeling

---

[referencia=3b850513f2939af4 score=0.057]
2024-02-05

Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

  477

478

479

480

481

482

483GPT2_TOKENIZER_REGEX = \

484    r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""

485

486

487def tokenization():

488    This unit was inspired by Andrej Karpathy's video on tokenization; check it out!    489

490    intro_to_tokenization()

491    tokenization_examples()

492    character_tokenizer()

493    byte_tokenizer()

494    word_tokenizer()

495    bpe_tokenizer()

496

498    - Tokenizer: strings <-> tokens (indices)

 499    - Character-based, byte-based, word-based tokenization highly suboptimal

 500    - BPE is an effective heuristic that looks at corpus statistics

 501    - Tokenization is a necessary evil, maybe one day we'll just do it from bytes...

 502

503@dataclass(frozen=True)

504class BPETokenizerParams:

505    """All you need to specify a BPETokenizer."""

506    vocab: dict[int, bytes]     

507    merges: dict[tuple[int, int], int]  

508

509

510

---

[referencia=3b850513f2939af4 score=0.048]
2022-03-29

We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4 more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

Introduced the rigorous analysis scaling laws for language models

Key improvement over Kaplan: tune learning rate for the compute budget

Approach 1: for each model size, train with 4 learning rates, vary number of training tokens, fit lower envelope

Approach 2 (IsoFLOP): for each model size, train with 9 training budgets, take last point

Approach 3: fit parametric function L(N, D) = E + A/N^alpha + B/D^beta to data collected from approaches 1 and 2

Conclusion: model and data should scale up at same rate

Table 3: extrapolate to 10 trillion parameters

MassiveText, different data distribution (1.5 trillion tokens)

70B parameters

   336    TL;DR:  (e.g., 1.4B parameter model should be trained on 28B tokens)

 337    But this doesn't take into account inference costs!

 338

341    - We define a training API (hyperparameters -> loss) based on previous runs

---

[referencia=3b850513f2939af4 score=0.045]
 57    Today, researchers just prompt a proprietary model (e.g., GPT-4/Claude/Gemini).

 58

59    Moving up levels of abstractions boosts productivity, but

 60    - These abstractions are leaky (in contrast to programming languages or operating systems).

 61    - There is still fundamental research to be done that require tearing up the stack.

 62

63    **Full understanding** of this technology is necessary for **fundamental research**.

 64

65    This course: **understanding via building**

 66    But there's one small problem...

 67

68    ## The industrialization of language models


 70

71    GPT-4 supposedly has 1.8T parameters.    72    GPT-4 supposedly cost $100M to train.    73    xAI builds cluster with 200,000 H100s to train Grok.    74    Stargate (OpenAI, NVIDIA, Oracle) invests $500B over 4 years.    75

76    Also, there are no public details on how frontier models are built.

 77    From the GPT-4 technical report  [OpenAI+ 2023]
GPT-4 Technical Report

[OpenAI] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad ... (271 more) ... Shengjia Zhao, Tianhao Zheng, Juntang Zhuang, William Zhuk, Barret Zoph

2023-03-15

We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

---

[referencia=3b850513f2939af4 score=0.038]
 436    sft_data: list[ChatExample] = [

437        ChatExample(

438            turns=[

439                Turn(role="system", content="You are a helpful assistant."),

440                Turn(role="user", content="What is 1 + 1?"),

441                Turn(role="assistant", content="The answer is 2."),

442            ],

443        ),

444    ]

445    Data often involves human annotation.

 446    Intuition: base model already has the skills, just need few examples to surface them.  [Zhou+ 2023]
LIMA: Less Is More for Alignment

Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun ... (5 more) ... Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, Omer Levy

2023-05-18

Large language models are trained in two stages: (1) unsupervised pretraining from raw text, to learn general-purpose representations, and (2) large scale instruction tuning and reinforcement learning, to better align to end tasks and user preferences. We measure the relative importance of these two stages by training LIMA, a 65B parameter LLaMa language model fine-tuned with the standard supervised loss on only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling. LIMA demonstrates remarkably strong performance, learning to follow specific response formats from only a handful of examples in the training data, including complex queries that range from planning trip itineraries to speculating about alternate history. Moreover, the model tends to generalize well to unseen tasks that did not appear in the training data. In a controlled human study, responses from LIMA are either equivalent or strictly preferred to GPT-4 in 43% of cases; this statistic is as high as 58% when compared to Bard and 65% versus DaVinci003, which was trained with human feedback. Taken together, these results strongly suggest that almost all knowledge in large language models is learned during pretraining, and only limited instruction tuning data is necessary to teach models to produce high quality output.

   447    Supervised learning: fine-tune model to maximize p(response | prompt).

 448

449

450def learning_from_feedback():

451    Now we have a preliminary instruction following model.

 452    Let's make it better without expensive annotation.

 453

---

[referencia=3b850513f2939af4 score=0.037]
1import regex

2from abc import ABC

3from dataclasses import dataclass

4from collections import defaultdict

5import random

6

7from execute_util import link, image, text

8from lecture_util import article_link, x_link, youtube_link

9from references import gpt_3, gpt4, shannon1950, bengio2003, susketver2014, \

10    bahdanau2015_attention, transformer_2017, gpt2, t5, kaplan_scaling_laws_2020, \

11    the_pile, gpt_j, opt_175b, bloom, palm, chinchilla, llama, mistral_7b, \

12    instruct_gpt, dpo, adamw2017, lima, deepseek_v3, adam2014, grpo, ppo2017, muon, \

13    large_batch_training_2018, wsd_2024, cosine_learning_rate_2017, olmo_7b, moe_2017, \

14    megatron_lm_2019, shazeer_2020, elmo, bert, qwen_2_5, deepseek_r1, moe_2017, \

15    rms_norm_2019, rope_2021, soap, gqa, mla, deepseek_67b, deepseek_v2, brants2007, \

16    layernorm_2016, pre_post_norm_2020, llama2, llama3, olmo2, \

17    megabyte, byt5, blt, tfree, sennrich_2016, zero_2019, gpipe_2018

18from data import get_common_crawl_urls, read_common_crawl, write_documents, markdownify_documents

19from model_util import query_gpt4o

20

21import tiktoken

22

23def main():

24    welcome()

25    why_this_course_exists()

26    current_landscape()

27

28    what_is_this_program()

29

30    course_logistics()

31    course_components()

32

33    tokenization()

34

35    Next time: PyTorch building blocks, resource accounting

 36

37

38def welcome():

39    ## CS336: Language Models From Scratch (Spring 2025)


 40

42

43    This is the second offering of CS336.

---

[referencia=3b850513f2939af4 score=0.033]
 36

37

38def welcome():

39    ## CS336: Language Models From Scratch (Spring 2025)


 40

42

43    This is the second offering of CS336.

 44    Stanford edition has grown by 50%.

 45    Lectures will be posted on YouTube and be made available to the whole world.

 46

47

48def why_this_course_exists():

49    ## Why did we make this course?


 50

51    Let's ask GPT-4  [OpenAI+ 2023]
GPT-4 Technical Report

[OpenAI] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad ... (271 more) ... Shengjia Zhao, Tianhao Zheng, Juntang Zhuang, William Zhuk, Barret Zoph

2023-03-15

We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

No details on the data or model architecture.

   52    response = query_gpt4o(prompt="Why teach a course on building language models from scratch? Answer in one sentence.")  

53    

54    Problem: researchers are becoming **disconnected** from the underlying technology.

 55    8 years ago, researchers would implement and train their own models.

 56    6 years ago, researchers would download a model (e.g., BERT) and fine-tune it.

 57    Today, researchers just prompt a proprietary model (e.g., GPT-4/Claude/Gemini).

 58

59    Moving up levels of abstractions boosts productivity, but

---

[referencia=3b850513f2939af4 score=0.027]
Model: BLOOM (176B parameters)

Data: ROOTS

Hardware: 48x8 A100s on Jean Zay supercomputer for 3.5 months

ZeRO stage 1

  144     [Touvron+ 2023]
LLaMA: Open and Efficient Foundation Language Models

[Meta] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux ... (4 more) ... Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample

2023-02-27

We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community.

Train only on open data (detailed recipe that is replicated by RedPajama)

Optimize for fast inference at 7B

Data: CommonCrawl, C4, GitHub, Wikipedia, Books, ArXiv, StackExchange

Architecture: Pre-norm, SwiGLU, RoPE

Training: 2048 A100 80GB for 21 days

 [Touvron+ 2023]
Llama 2: Open Foundation and Fine-Tuned Chat Models

[Meta] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi ... (58 more) ... Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, Thomas Scialom

2023-07-18

---

[referencia=3b850513f2939af4 score=0.026]
[Peters+ 2018]
Deep contextualized word representations

Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer

2018-02-15

We introduce a new type of deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). Our word vectors are learned functions of the internal states of a deep bidirectional language model (biLM), which is pre-trained on a large text corpus. We show that these representations can be easily added to existing models and significantly improve the state of the art across six challenging NLP problems, including question answering, textual entailment and sentiment analysis. We also present an analysis showing that exposing the deep internals of the pre-trained network is crucial, allowing downstream models to mix different types of semi-supervision signals.

  130    - BERT: pretraining with Transformer, fine-tuning helps tasks

[Devlin+ 2018]
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova

2018-10-11

We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications. BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

  131    - Google's T5 (11B): cast everything as text-to-text

---

[referencia=3b850513f2939af4 score=0.017]
Linting Xue, Aditya Barua, Noah Constant, Rami Al-Rfou, Sharan Narang, Mihir Kale, Adam Roberts, Colin Raffel

2021-05-28

Most widely-used pre-trained language models operate on sequences of tokens corresponding to word or subword units. By comparison, token-free models that operate directly on raw text (bytes or characters) have many benefits: they can process text in any language out of the box, they are more robust to noise, and they minimize technical debt by removing complex and error-prone text preprocessing pipelines. Since byte or character sequences are longer than token sequences, past work on token-free models has often introduced new model architectures designed to amortize the cost of operating directly on raw text. In this paper, we show that a standard Transformer architecture can be used with minimal modifications to process byte sequences. We characterize the trade-offs in terms of parameter count, training FLOPs, and inference speed, and show that byte-level models are competitive with their token-level counterparts. We also demonstrate that byte-level models are significantly more robust to noise and perform better on tasks that are sensitive to spelling and pronunciation. As part of our contribution, we release a new set of pre-trained byte-level Transformer models based on the T5 architecture, as well as all code and data used in our experiments.

 [Yu+ 2023]
MEGABYTE: Predicting Million-byte Sequences with Multiscale Transformers

Lili Yu, Dániel Simig, Colin Flaherty, Armen Aghajanyan, Luke Zettlemoyer, Mike Lewis

2023-05-12