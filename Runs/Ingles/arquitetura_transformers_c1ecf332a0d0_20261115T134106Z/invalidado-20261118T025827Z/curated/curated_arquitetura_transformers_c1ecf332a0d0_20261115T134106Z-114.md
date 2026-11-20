[referencia=739b0738cc518ef9 score=0.984]
## **2 Model Architecture** 

Jamba is a hybrid decoder architecture that mixes Transformer layers [51] with Mamba layers [17], a recent state-space model (SSM) [18, 19], in addition to a mixture-of-experts (MoE) module [14, 46]. We call the combination of these three elements a Jamba block. See Figure 1 for an illustration. 

Combining Transformer, Mamba, and MoE elements allows flexibility in balancing among the sometimes conflicting objectives of low memory usage, high throughput, and high quality. In terms of memory usage, note that comparing the total size of the model parameters can be misleading. In an MoE model, the number of active parameters that participate in any given forward step may be much smaller than the total number of parameters. Another important consideration is the KV cache – the memory required to store the attention keys and values in the context. When scaling Transformer models to long contexts, the KV cache becomes a limiting factor. Trading off attention layers for Mamba layers reduces the total size of the KV cache. Our architecture aims to provide 

3 

not only a small number of active parameters but also an 8x smaller KV cache compared to a vanilla Transformer. Table 1 compares Jamba with recent publicly available models, showing its advantage in maintaining a small KV cache even with 256K token contexts. 

||Available params|Active params<br>KV cache|(256K context, 16bit)|
|---|---|---|---|
|LLAMA-2|6.7B|6.7B|128GB|
|Mistral|7.2B|7.2B|32GB|
|Mixtral|46.7B|12.9B|32GB|
|Jamba|52B|12B|4GB|



Table 1: Comparison of Jamba and recent open models in terms of total available parameters, active parameters, and KV cache memory on long contexts. Jamba provides a substantial reduction in the KV cache memory requirements. 

In terms of throughput, with short sequences, attention operations take up a small fraction of the inference and training FLOPS [7]. However, with long sequences, attention hogs most of the compute. In contrast, Mamba layers are more compute-efficient. Thus, increasing the ratio of Mamba layers improves throughput especially for long sequences.

---

[referencia=739b0738cc518ef9 score=0.977]
## **1 Introduction** 

We introduce Jamba, a new publicly available large language model. Jamba is based on a novel hybrid architecture, which combines Transformer layers [51] with Mamba layers [17], a recent state-space model [18, 19], as well as a mixture-of-experts (MoE) module [14, 46]. Jamba thus combines two orthogonal architectural designs that together give it improved performance and higher throughput, while maintaining a manageable memory footprint. The 7B-based Jamba model (12B active parameters, 52B total available parameters) we are releasing was designed to fit in a single 80GB GPU, but the Jamba architecture supports other design choices, depending on one’s hardware and performance requirements. 

> _∗_ Equal contribution. 

The fundamental novelty of Jamba is its hybrid Transformer-Mamba architecture (though see mention below of recent related efforts). Despite the immense popularity of the Transformer as the predominant architecture for language models, it suffers from two main drawbacks. First, its high memory and compute requirements hinders the processing of long contexts, where the key-value (KV) cache size becomes a limiting factor. Second, its lack of a single summary state entails slow inference and low throughput, since each generated token performs a computation on the entire context. In contrast, older recurrent neural network (RNN) models, which summarize an arbitrarily long context in a single hidden state, do not suffer from these limitations. RNN models have their own shortcomings, however. They are costly to train since training cannot be parallelized across time steps. And they struggle with long distance relationships, which the hidden state captures to only a limited extent. 

Recent state space models (SSMs) like Mamba are more efficient to train than RNNs and are more capable at handling long distance relationships, but still lag behind the performance of comparably sized Transformer language models. Taking advantage of both model families, Jamba combines Transformer and Mamba layers, at a certain ratio. Varying the ratio of Transformer/Mamba layers allows balancing memory usage, efficient training, and long context capabilities.

---

[referencia=739b0738cc518ef9 score=0.965]
#### **6.5 Jamba does not Require Explicit Positional Information** 

Table 8 shows results of the Jamba architecture (with MoE) with no positional information and when applying RoPE [47] in the attention layers (1.3B parameter models, 250B tokens). The results are similar, suggesting that explicit positional information may not be required for the hybrid architecture. Presumably, the Mamba layers, which are placed before attention layers, provide implicit position information.<sup>7</sup> 

7Some prior evidence suggested that Transformer decoder models do not need positional encodings [20]. However, all existing large scale models do use some sort of explicit position information. 

12 



Figure 9: Adding RMSNorm to Mamba layers prevents loss spikes. 

|||Hella|Wino||Narrative||||log-prob||
|---|---|---|---|---|---|---|---|---|---|---|
||OLLM|Swag|Grande|ARC-C|QA|NQ|BoolQ|C4|Books|Code|
|Jamba|39.6|71.5|64.2|40.7|50.5|22.2|68.9|-0.516|-0.623|-0.299|
|Jamba+RoPE|40.1|71.8|65.5|40.4|46.2|22.2|67.9|-0.516|-0.623|-0.299|



Table 8: Comparison of Jamba with and without explicit positional information. 

## **7 Conclusion** 

We presented Jamba, a novel architecture which combines Attention and Mamba layers, with MoE modules, and an open implementation of it, reaching state-of-the-art performance and supporting long contexts. We showed how Jamba provides flexibility for balancing performance and memory requirements, while maintaining a high throughput. We experimented with several design choices such as the ratio of Attention-to-Mamba layers and discussed some discoveries made during the development process, which will inform future work on hybrid attention–state-space models. To facilitate such research, we plan to release model checkpoints from smaller-scale training runs. The largest model we provide with this release has 12B active and 52B total available parameters, supporting context lengths of up to 256K tokens and fitting in a single 80GB GPU even when processing 140K-token texts.

---

[referencia=739b0738cc518ef9 score=0.961]
We hypothesize that this phenomenon points to a limitation of SSMs – a potential difficulty in in-context learning (ICL). Indeed, the ability to perform ICL has been linked to the emergence of socalled induction heads in Transformer language models during training, which perform approximate copying operations that are supportive of ICL [35]. We conjecture that the lack of an attention mechanism in the pure Mamba model makes it difficult for it to learn in-context. While Mamba may learn to copy and perform simple ICL when explicitly trained to do so ([17, 36], it is not clear if ICL is an emergent capability in SSM as is typical of Transformer models. In contrast, the hybrid Attention–Mamba model does perform successful ICL, even when only 1 out of 8 layers is an Attention one. 

As anecdotal evidence of an emergent induction mechanism, we visualize in Figure 8 the attention of an example head from a 1.3B Attention-Mamba hybrid model (no MoE), on an IMDB example where the pure Mamba failed and the hybrid succeeded. Clearly, the attention from the last token (“:”) is focused on the labels from the few-shot examples. We have found 12 such heads in our hybrid model, in all three attention layers (which correspond to layers 4, 12, 20 in the model). 

Future work can further investigate the emergence of ICL in hybrid models at large scale. Our released checkpoints would hopefully facilitate such investigations. Finally, very recent work has attempted to extract attention-like scores from state-space models like Mamba [1], which opens another direction to search for induction capabilities in state-space models.

---

[referencia=739b0738cc518ef9 score=0.959]
> 5In all the ablations, “pure Mamba” refers to models with Mamba layers interleaved with MLP layers. 

9 



Figure 6: Training loss curves for pure Attention, pure Mamba, and Attention-Mamba hybrids (no MoE), with ratios _a_ : _m_ of 1:3 and 1:7. All models are 1.3B parameters. The two hybrids achieve better loss throughout this training run, without any noticeable difference between the different Attention/Mamba ratios. 

Next, we compare performance of vanilla Transformer, vanilla Mamba, and Attention-Mamba hybrid models, at 7B model size, after training on 50B tokens. As Table 5 shows, the pure Mamba model is quite competitive, but lags slightly behind pure Attention. The hybrid Attention-Mamba (without MoE) outperforms the pure models while obtaining better throughput than the vanilla Transformer (Section 3.2). 

|||Hella|Wino|||log-prob||
|---|---|---|---|---|---|---|---|
||OLLM|Swag|Grande|NQ|C4|Books|Code|
|Attention|36.1|60.4|59.7|13.7|-0.555|-0.666|-0.347|
|Mamba|35.3|60.2|55.8|14.0|-0.554|-0.667|-0.355|
|Jamba (_a_:_m_= 1 : 7, no MoE)|36.6|62.5|58.8|15.4|-0.547|-0.658|-0.340|



Table 5: Results on academic benchmarks and log-prob evaluations, comparing pure Attention, pure Mamba, and Attention-Mamba hybrid (no MoE). Models are 7B parameters, trained for 50B tokens. 

Figure 7 shows the training loss of the three architectures. While the pure Transformer and Mamba models have a similar convergence, the hybrid Jamba (no MoE) has a lower loss throughout this run. 



Figure 7: Training loss curves for pure Attention, pure Mamba, and an Attention-Mamba hybrid (no MoE). All models are 7B parameters. The hybrid achieves better loss throughout this training run. 

10

---

[referencia=739b0738cc518ef9 score=0.950]
#### **6.1 Benefits of combining Attention and Mamba** 

We first investigate the ratio of Attention to Mamba layers ( _a_ : _m_ ), with 1.3B parameters models trained for 250B tokens. As Table 4 shows, the hybrid Jamba model outperforms the pure attention or Mamba models. The ratio of attention-to-Mamba layers may be 1:3 or 1:7 with virtually no performance difference. Figure 6 shows the training loss of these models, where Jamba exhibits improved loss during training. Given that a 1:7 ratio is more compute-efficient and shows similar performance, we opt for it in our larger-scale experiments. 

|||Hella|Wino|||log-prob||
|---|---|---|---|---|---|---|---|
||OLLM|Swag|Grande|NQ|C4|Books|Code|
|Attention|36.4|62.4|59.6|14.5|-0.543|-0.659|-0.331|
|Mamba|36.1|62.6|59.4|14.5|-0.543|-0.661|-0.334|
|Jamba (_a_:_m_= 1 : 3, no MoE)|37.2|65.1|61.7|16.5|-0.533|-0.649|-0.321|
|Jamba (_a_:_m_= 1 : 7, no MoE)|37.2|65.1|61.7|16.0|-0.533|-0.650|-0.321|



Table 4: Results on academic benchmarks and log-probability evaluations showing an improved performance of Attention-Mamba (no MoE) compared to vanilla Attention and Mamba models. There is no substantial difference between 1:3 and 1:7 ratios of Attention-to-Mamba layers. Models are 1.3B parameters, trained for 250B tokens. 

> 4F1 score is the recommended metric in L-Eval [2]. In addition, our setup calibrates the length of the few-shot completions to approximately match the length of the test completion, increasing the credibility of F1. 

> 5In all the ablations, “pure Mamba” refers to models with Mamba layers interleaved with MLP layers. 

9

---

[referencia=739b0738cc518ef9 score=0.926]
# **Jamba: A Hybrid Transformer-Mamba Language Model** 

**Opher Lieber**<sup>_∗_</sup> **Barak Lenz**<sup>_∗_</sup> **Hofit Bata Gal Cohen Jhonathan Osin Itay Dalmedigos Erez Safahi Shaked Meirom Yonatan Belinkov Shai Shalev-Shwartz Omri Abend Raz Alon Tomer Asida Amir Bergman Roman Glozman Michael Gokhman Avshalom Manevich Nir Ratner Noam Rozen Erez Schwartz Mor Zusman Yoav Shoham** 



## **Abstract** 

We present Jamba, a new base large language model based on a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture. Specifically, Jamba interleaves blocks of Transformer and Mamba layers, enjoying the benefits of both model families. MoE is added in some of these layers to increase model capacity while keeping active parameter usage manageable. This flexible architecture allows resource- and objective-specific configurations. In the particular configuration we have implemented, we end up with a powerful model that fits in a single 80GB GPU. Built at large scale, Jamba provides high throughput and small memory footprint compared to vanilla Transformers, and at the same time state-of-the-art performance on standard language model benchmarks and long-context evaluations. Remarkably, the model presents strong results for up to 256K tokens context length. We study various architectural decisions, such as how to combine Transformer and Mamba layers, and how to mix experts, and show that some of them are crucial in large scale modeling. We also describe several interesting properties of these architectures which the training and evaluation of Jamba have revealed, and plan to release checkpoints from various ablation runs, to encourage further exploration of this novel architecture. We make the weights of our implementation of Jamba publicly available under a permissive license. 

**Model:** `https://huggingface.co/ai21labs/Jamba-v0.1`

---

[referencia=739b0738cc518ef9 score=0.915]
A few other recent attempts to combine Attention and SSM modules are worth noting. [55] mixes an S4 layer [18] with a local attention layer, followed by a sequence of local attention layers; it shows experiments with small models and simple tasks. [17] reports that interleaving Mamba and attention layers is only slightly better than pure Mamba in terms of perplexity, with models up to 1.3B parameters. [37] starts with an SSM layer followed by chunk-based Transformers, with models up to 1.3B showing improved perplexity. [13] adds an SSM layer before the self-attention in a Transformer layer, while [43] adds the SSM after the self-attention, both showing improvements on speech recognition. [36] replaces the MLP layers in the Transformer by Mamba layers, and shows benefits in simple tasks. These efforts are different from Jamba both in the particular way in which the SSM component is mixed with the attention one, and in the scale of implementation. Closest are perhaps H3 [15], a specially designed SSM that enables induction capabilities, and a generalization called Hyena [39]. The former proposed a hybrid architecture that replaces the second and middle layers with self-attention, and was implemented with up to 2.7B parameters and 400B training tokens. However, as shown in [17], its perfomance lags that of pure Mamba. Based on Hyena, StripedHyena [40] interleaves attention and SSM layers in a 7B parameter model. However, it lags behind the Attention-only Mistral-7B [23]. All of this renders Jamba the first production-grade Attention-SSM hybrid model. Scaling the hybrid Jamba architecture required overcoming several obstacles, which we dicsuss in Section 6.

---

[referencia=739b0738cc518ef9 score=0.911]
Here is a description of the main configuration, which provides improved performance and efficiency. Section 6 contains results from ablation experiments supporting the design choices. 

The basic component is a Jamba block, which may be repeated in sequence. Each Jamba block is a combination of Mamba or Attention layers. Each such layer contains either an attention or a Mamba module, followed by a multi-layer perceptron (MLP). The different possible types of layers are shown in Figure 1(b).<sup>2</sup> A Jamba block contains _l_ layers, which are mixed at a ratio of _a_ : _m_ , meaning _a_ attention layers for every _m_ Mamba layers. 

In Jamba, some of the MLPs may be replaced by MoE layers, which helps increase the model capacity while keeping the active number of parameters, and thus the compute, small. The MoE module may be applied to MLPs every _e_ layers. When using MoE, there are _n_ possible experts per layer, with a router choosing the top _K_ experts at each token. In summary, the different degrees of freedom in the Jamba architecture are: 

- _l_ : The number of layers. 

- _a_ : _m_ : ratio of attention-to-Mamba layers. 

- _e_ : how often to use MoE instead of a single MLP. 

- _n_ : total number of experts per layer. 

- _K_ : number of top experts used at each token. 

Given this design space, Jamba provides flexibility in preferring certain properties over others. For example, increasing _m_ and decreasing _a_ , that is, increasing the ratio of Mamba layers at the expense of attention layers, reduces the required memory for storing the key-value cache. This reduces the overall memory footprint, which is especially important for processing long sequences. Increasing the ratio of Mamba layers also improves throughput, especially at long sequences. However, decreasing _a_ might lower the model’s capabilities.

---

[referencia=739b0738cc518ef9 score=0.901]
Table 2: Comparison of Jamba with other publicly available models. Jamba obtains similar performance with much better throughput. 

Table 2 compares Jamba to several publicly available models on common academic benchmarks for evaluating language models. We compare with Llama-2 13B [50], which has about the same number of active paramters as our model, Llama-2 70B, which is larger than our model, Gemma [49], which has 7B parameters, and Mixtral [24], which has about the same number of active and total parameters as our model. 

In most tasks, Jamba performs comparably to leading publicly available models of similar or larger size, including Llama-2 70B and Mixtral. At the same time, our model has a smaller number of total available parameters than Llama-2 (52B compared to 70B). Moreover, as a sparse model, Jamba has only 12B active parameters, similar to Mixtral’s 12.9B active parameters. However, as a fullyattentional model, Mixtral has a large memory footprint with long sequences, requiring 32GB for the KV cache with 256K tokens. In contrast, thanks to its hybrid Attention-Mamba architecture, Jamba’s KV cache takes only 4GB even at such a long context (Section 2). Importantly, our Jamba achieves such a strong performance while having much better throughput than Llama-2 70B and Mixtral, up to 3x improvement (Section 3.2). 

In summary, Jamba demostrates the ability of hybrid architectures to reach the performance of state-of-the-art Transformer models of the same size class, while having the benefits of an SSM. 

#### **5.2 Long-Context Evaluations** 

We have successfully trained Jamba models with context lengths of up to 1M tokens. The released model handles context lengths of up to 256K tokens. In this section, we evaluate it on synthetic and naturalistic benchmarks that test its long-context capabilities. 

#### **5.2.1 Needle-in-a-haystack** 

As Figure 4 shows, Jamba has excellent performance in the needle-in-a-haystack evaluation, which requires retrieving a simple statement planted in a long context window [25]. This result is noteworthy especially given that our implementation of Jamba uses only 4 attention layers.

---

[referencia=739b0738cc518ef9 score=0.746]
## **6 Ablations and Insights** 

This section discusses ablation experiments we ran for different design choices in our implementation of the Jamba architecture. First we show the benefit of combining attention and Mamba layers, at which ratio they should be combined, and how to interleave them. We investigate cases where pure Mamba fails, suggesting that it struggles to develop in-context learning capabilities, while the Attention-Mamba hybrid exhibits in-context learning similar to vanilla Transformers. Then we show the benefit of adding MoE on top of a hybrid Attention-Mamba model. Finally, we share two additional learnings that we found useful: explicit positional information is not needed in Jamba, and Mamba layers necessitate special normalization to stabilize training at large scale.<sup>5</sup> 

For these ablations, we report the following measures, which exhibit informative performance even at small data or model scale. 

- Academic benchmarks: HellaSwag (10-shot) [52], WinoGrande (5-shot) [42], Natural Questions closed-book (NQ; 5-shot) [27]. 

- HuggingFace OpenLLM leaderboard (OLLM) [12]: a summary statistic of several datasets. We report results with our reproduction. 

- Perplexity evaluations: we report log-prob (per byte) on texts from three domains: C4, Books, and code.

---

[referencia=739b0738cc518ef9 score=0.709]
#### **6.3 The Effect of Mixture-of-Experts (MoE)** 

Recent work has shown that MoE improves Transformer language models while keeping compute manageable [24].<sup>6</sup> However, it is not clear if MoE integrates well with state-space models at a large scale, and specifically with our hybrid Attention–Mamba architecture. Indeed, Table 7 shows that MoE improves the performance of the hybrid Attention-Mamba architecture at large scale (7B parameters trained on 50B tokens). The MoE variant has _n_ = 16 total experts, _K_ = 2 experts used at each token, and MoE is applied every _e_ = 2 layers, as described in Section 3.1. 

> 6There is also initial evidence that MoE helps Mamba layers, albeit at small model and data scale [38]. 

11 



### **[…]** 



### **[…]** 



**[…]**

---

[referencia=739b0738cc518ef9 score=0.661]
2 



<!-- Start of picture text -->
MLP MoE<br>Mamba MoE layer<br>RMSNorm RMSNorm<br>Mamba layer<br>Attention Attention<br>Mamba MoE layer<br>RMSNorm RMSNorm<br>Transformer layer Attention MoE layer<br>Transformer layer<br>Mamba MoE layer<br>MLP MoE<br>RMSNorm RMSNorm<br>Mamba layer<br>Mamba Mamba<br>Mamba MoE layer<br>RMSNorm RMSNorm<br>Mamba layer<br>Mamba layer Mamba MoE layer<br>(a)  Jamba block (b)  Different types of layers<br><!-- End of picture text -->

Figure 1: **(a)** A single Jamba block. **(b)** Different types of layers. The implementation shown here is with _l_ = 8, _a_ : _m_ = 1 : 7 ratio of attention-to-Mamba layers, and MoE applied every _e_ = 2 layers. 

**_Important notice_** _: The Jamba model released is a pretrained_ **_base_** _model, which did not go through alignment or instruction tuning, and does not have moderation mechanisms. It should not be used in production environments or with end users without additional adaptation._

---

[referencia=739b0738cc518ef9 score=0.615]
#### **6.2 Why does the Combination Work?** 

The pure Mamba model showed fairly good results in most tasks early on, including in general perplexity evaluations. However, it performed substantially worse than the pure Attention model in three common benchmark tasks: IMDB [32], QuAC [6], and NarrativeQA [26]. In contrast, the hybrid Attention-Mamba performed similarly to the Attention model on these datasets. Table 6 shows the results for 1.3B models after 250B tokens. 

||IMDB|QuAC|NarrativeQA|
|---|---|---|---|
|Attention|84.1|27.9|45.8|
|Mamba|48.8|20.2|27.7|
|Attention-Mamba|90.9|26.6|43.7|



Table 6: Mamba performs poorly on certain datasets, while the Attention-Mamba hybrid performs on par with the Attention model. 

Looking into these results further, we found out that the pure Mamba model often does not follow the correct format. For instance, in the IMDB dataset, answer choices are “Positive” or “Negative”. While the Attention model adheres to this format, the pure Mamba model often produces other answers, such as “Very Good”, “Very Positive”, “Funny”, “Bad”, “Poor”, and “3/10”. While these may be considered correct answers, the difficulty of Mamba to adhere to the format suggests a potential problem. Indeed, to perform successful in-context learning, it is important for models to capture the input-output format [34]. The hybrid Attention-Mamba model follows the format successfully, just like the pure Attention model.

---

[referencia=739b0738cc518ef9 score=0.499]
### **[…]** 



Figure 8: Example induction head (H3, first attention layer) from a hybrid Attention-Mamba model. Highlighted words reflect strong attention from the last token, “:”, just before the model is about to predict the label. We see that the attention is focused on label tokens from the few-shot examples. 

|||Hella|Wino|||log-prob||
|---|---|---|---|---|---|---|---|
||OLLM|Swag|Grande|NQ|C4|Books|Code|
|Jamba (no MoE)|36.6|62.5|58.8|15.4|-0.547|-0.658|-0.340|
|Jamba+MoE|38.1|66.0|61.2|18.9|-0.534|-0.645|-0.326|



Table 7: Mixture-of-experts improves the Attention-Mamba hybrid. 

#### **6.4 Stabilizing Mamba at large scale** 

When training Jamba models of up to 1.3B parameters, we observed stable training without special problems. However, when scaling to the largest model released here (7B-based, which has 12B/52B active/total parameters), we encountered large loss spikes. Investigating this revealed that inner parts of the Mamba layers suffer from large activation values, leading to the spikes. We therefore added RMSNorm [53] to internal activations. As Figure 9 shows, this stabilized training and prevented additional loss spikes.

---

[referencia=739b0738cc518ef9 score=0.474]
#### **3.1 Jamba Implementation for a Single 80GB GPU** 

The specific configuration in our implementation was chosen to fit in a single 80GB GPU, while achieving best performance in the sense of quality and throughput. In our implementation we have a sequence of 4 Jamba blocks. Each Jamba block has the following configuration: 

- _l_ = 8: The number of layers. 

- _a_ : _m_ = 1 : 7: ratio attention-to-Mamba layers. 

- _e_ = 2: how often to use MoE instead of a single MLP. 

- _n_ = 16: total number of experts. 

- _K_ = 2: number of top experts used at each token. 

The _a_ : _m_ = 1 : 7 ratio was chosen according to preliminary ablations, as shown in Section 6, since this ratio was the most compute-efficient variant amongst the best performing variants in terms of quality. 

The configuration of the experts was chosen to enable the model to fit in a single 80GB GPU (with int8 weights), while including sufficient memory for the inputs. In particular, _n_ and _e_ were balanced to have an average of _∼_ 8 experts per layer. In addition, we balanced _n_ , _K_ , and _e_ to allow for high quality, while keeping both compute requirements and communication dependencies (memory transfers) checked. Accordingly, we chose to replace the MLP module with MoE on every other layer, as well as have a total of 16 experts, two of which are used at each token. These choices were inspired by prior work on MoE [8, 54] and verified in preliminary experiments. 

Figure 2 shows the maximal context length that fits a single 80GB GPU with our Jamba implementation compared to Mixtral 8x7B and Llama-2-70B. Jamba provides 2x the context length of Mixtral and 7x that of Llama-2-70B. 



<!-- Start of picture text -->
Context length fitting a single 80GB A100 GPU<br><!-- End of picture text -->



<!-- Start of picture text -->

---

[referencia=739b0738cc518ef9 score=0.256]
Jamba also includes MoE layers [14, 46], which allow increasing the model capacity (total number of available parameters) without increasing compute requirements (number of active parameters). MoE is a flexible approach that enables training extremely large models with strong performance [24]. In Jamba, MoE is applied to some of the MLP layers. The more MoE layers, and the more experts in each MoE layer, the larger the total number of model parameters. In contrast, the more experts we use at each forward pass, the larger the number of active parameters as well as the compute requirement. In our implementation of Jamba, we apply MoE at every other layer, with 16 experts and the top-2 experts used at each token (a more detailed discussion of the model architecture is provided below). 

We evaluated our implementation of Jamba on a wide range of benchmarks and found it performs comparably to Mixtral-8x7B [24], which has a similar number of parameters, and also to the larger Llama-2 70B [50]. In addition, our model supports a context length of 256K tokens – the longest supported context length for production-grade publicly available models. On long-context evaluations, Jamba outperformes Mixtral on most of the evaluated datasets. At the same time, Jamba is extremely efficient; for example, its throughput is 3x that of Mixtral-8x7B for long contexts. Moreover, our model fits in a single GPU (with 8bit weights) even with contexts of over 128K tokens, which is impossible with similar-size attention-only models such as Mixtral-8x7B. 

Somewhat unusual for a new architecture, we release Jamba (12B active parameters, 52B total available parameters) under Apache 2.0 license: `https://huggingface.co/ai21labs/Jamba-v0.1` . We do so since we feel that the novel architecture of Jamba calls for further study, experimentation, and optimization by the community. Our design was based on various ablation experiments we conducted to explore the effect of different tradeoffs and design choices, and insights gleaned from those. These ablations were performed at scales of up to 7B parameters, and training runs of up to 250B tokens. We plan to release model checkpoints from these runs. 

2 



<!-- Start of picture text -->

---

[referencia=739b0738cc518ef9 score=0.248]
Additionally, balancing _n_ , _K_ , and _e_ affects the relationship between active parameters and total available parameters. A larger _n_ increases the model capacity at the expense of memory footprint, while a larger _K_ increases the active parameter usage and the compute requirement. In contrast, a larger _e_ decreases the model capacity, while decreasing both compute (when _K_ >1) and memory requirements, and allowing for less communication dependencies (decreasing memory transfers as well as inter-GPU communication during expert-parallel training and inference). 

Jamba’s implementation of Mamba layers incorporate several normalizations that help stabilize training in large model scales. In particular, we apply RMSNorm [53] in the Mamba layers. 

> 2The figure shows a potential Attention MoE layer, which our architecture does not use, but future variants could. 

4 

We found that with the Mamba layer, positional embeddings or mechanisms like RoPE [47] are not necessary, and so we do not use any explicit positional information. 

Other architecture details are standard, including grouped-query attention (GQA), SwiGLU activation function [7, 45, 50], and load balancing for the MoE [14]. The vocabulary size is 64K. The tokenizer is trained with BPE [16, 33, 44] and each digit is a separate token [7]. We also remove the dummy space used in Llama and Mistral tokenizers for more consistent and reversible tokenization.

---

[referencia=739b0738cc518ef9 score=0.225]
8 

[27]), CUAD (law; [22]), and SFiction (science fiction). The average input length in these datasets ranges from 6K to 62K tokens. These lengths are further highly expanded by the few-shot format. 

Table 3 summarizes the results, in terms of F1.<sup>4</sup> Jamba outperforms Mixtral on most of the datasets as well as on average. In addition, as these long-context tasks require substantial computation, here Jamba’s efficiency shines, with much better throughput with long contexts (Section 3.2). 

||LongFQA|CUAD|NarrativeQA|NQ|SFiction|Avg|
|---|---|---|---|---|---|---|
|Mixtral|0.42|0.46|0.29|0.58|0.42|0.43|
|Jamba|0.44|0.44|0.30|0.60|0.40|0.44|



Table 3: Results (F1) on long-context QA benchmarks, with a 3-shot format.

---

[referencia=739b0738cc518ef9 score=0.208]
#### **3.2 Throughput Analysis** 

For concreteness, we present results of the throughput in two specific settings.<sup>3</sup> In the first setting, we have varying batch size, a single A100 80 GB GPU, int8 quantization, 8K context length, generating output of 512 tokens. As Figure 3a shows, Jamba allows processing of large batches, leading to a 3x increase in throughput (tokens/second) over Mixtral, which does not fit with a batch of 16 despite having a similar number of active parameters. 

In the second setting, we have a single batch, 4 A100 GPUs, no quantization, varying context lengths, generating output of 512 tokens. As demonstrated in Figure 3b, at small context lengths all models have a similar throughput. Jamba excels at long contexts; with 128K tokens its throughput is 3x that of Mixtral. Note that this is despite the fact that Jamba has not yet enjoyed optimizations of the kind the community has developed for pure Transformer models over the past six years. We can expect the throughut gap to increase as such optimizations are developed also for Jamba. 



<!-- Start of picture text -->
Throughput (4 A100 GPUs)<br>Throughput (single GPU) Llama-2 13B Llama-2 70B Mixtral 8x7B Jamba<br>Llama-2 13B  Llama-2 70B Mixtral 8x7B Jamba 2000<br>2000<br>1500<br>1500<br>1000<br>1000<br>500<br>500<br>0 0<br>1 2 4 8 16 1K 2K 4K 8K 16K 32K 64K 128K<br>Batch size Context Window<br>Throughput (t/s)<br>Throughput (t/s)<br><!-- End of picture text -->