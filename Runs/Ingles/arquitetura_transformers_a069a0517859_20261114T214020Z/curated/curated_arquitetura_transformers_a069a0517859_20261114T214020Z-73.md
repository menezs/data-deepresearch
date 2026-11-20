[referencia=29ab108383433c26 score=0.998]
# **Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models** 

### **NVIDIA** 

**Abstract.** As inference-time scaling becomes critical for enhanced reasoning capabilities, it is increasingly becoming important to build models that are efficient to infer. We introduce NemotronH, a family of 8B and 56B/47B hybrid Mamba-Transformer models designed to reduce inference cost for a given accuracy level. To achieve this goal, we replace the majority of self-attention layers in the common Transformer model architecture with Mamba layers that perform constant computation and require constant memory per generated token. We show that Nemotron-H models offer either better or on-par accuracy compared to other similarly-sized state-of-the-art open-sourced Transformer models (e.g., Qwen-2.5-7B/72B and Llama-3.1-8B/70B), while being up to 3 _×_ faster at inference. To further increase inference speed and reduce the memory required at inference time, we created Nemotron-H-47B-Base from the 56B model using a new compression via pruning and distillation technique called MiniPuzzle. Nemotron-H-47B-Base achieves similar accuracy to the 56B model, but is 20% faster to infer. In addition, we introduce an FP8-based training recipe and show that it can achieve on par results with BF16-based training. This recipe is used to train the 56B model. We are releasing Nemotron-H base model checkpoints with support in Hugging Face and NeMo.

---

[referencia=29ab108383433c26 score=0.995]
© 2025 NVIDIA. All rights reserved. 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 



<!-- Start of picture text -->
Input sequence length = 65536  / Output sequence length = 1024<br>62.5<br>Nemotron-H-47B<br>Nemotron-H-56B<br>60.0<br>Qwen-2.5-72B<br>57.5<br>55.0<br>Llama-3.1-405B<br>52.5<br>Llama-3.1-70B<br>50.0 2.4x 1.2x<br>0 5 10 15 20 25 30 35 40<br>Throughput (Output tokens/s/GPU)<br>MMLU-Pro accuracy (%)<br><!-- End of picture text -->

Figure 1 _|_ MMLU-Pro accuracy (Wang et al., 2024a) versus per-GPU inference throughput for Nemotron-H-56B/47B-Base compared to existing similarly-sized Transformer models. Nemotron-H models provide state-of-the-art accuracy and inference time speedups. 

Qwen-2.5-7B/Llama-3.1-8B and Qwen-2.5-72B/Llama-3.1-70B, respectively. For example, NemotronH-56B-Base outperforms Llama-3.1-70B on 16 out of 17 tasks that we evaluated (§2.5). With larger sequences (65536 input sequence length, 1024 output tokens), we measure up to 3 _×_ higher inference throughput on NVIDIA H100 GPUs.

---

[referencia=29ab108383433c26 score=0.994]
## **6. Conclusions** 

The Nemotron-H family of models demonstrates that hybrid model architectures can offer the best of both worlds: comparable to state-of-the-art Transformer models in terms of capabilities while offering improved inference speed. We find the Nemotron-H base models offer either better or on-par accuracy compared to other similarly-sized state-of-the-art open-sourced Transformer models (e.g., Qwen-2.5-7B/72B and Llama-3.1-8B/70B), while being up to 3 _×_ faster at inference. We also find these base models can be adapted to yield effective VLMs as well as instruction-tuned models. Additionally, both our FP8-based training recipe and MiniPuzzle can be used to reduce the cost of creating these models. 

We have released the Nemotron-H base checkpoints described in this paper with support in Hugging Face and NeMo to facilitate further research: 

- **Nemotron-H-56B-Base.** Hugging Face and NGC. 

- **Nemotron-H-47B-Base.** Hugging Face and NGC. 

- **Nemotron-H-8B-Base.** Hugging Face and NGC. 

25 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 

Nemotron-H Reasoning checkpoints described are also available in Hugging Face: 

- **Nemotron-H-47B-Reasoning.** Hugging Face. 

- **Nemotron-H-8B-Reasoning.** Hugging Face.

---

[referencia=29ab108383433c26 score=0.993]
## **1. Introduction** 

Attention (Vaswani et al., 2023) traditionally has been the powerhouse of large language models (LLMs). Yet, to generate one token during auto-regressive inference, the self-attention layer must perform computation that scales linearly with the number of tokens seen so far since it models interactions between all pairs of tokens in a sequence (potentially in a causal way); as a result, selfattention layers also have to store state in a KV cache during inference that is linearly proportional to the number of tokens in the sequence (Kwon et al., 2023). Recent reasoning LLMs, however, exhibit _inference-time scaling_ , where generating more tokens at inference time can improve the quality of model responses (OpenAI, 2025; DeepSeek-AI, 2025b). Thus, attention layers can fundamentally limit overall model intelligence. 

To address this issue, much recent work has proposed alternative architectures (Katharopoulos et al., 2020; Beltagy et al., 2020; Gu & Dao, 2024; Dao & Gu, 2024). One such example is a series of _hybrid models_ that replace the majority of the self-attention layers in the standard Transformer architecture with more efficient layers (e.g., Mamba, Mamba-2, or sliding-window attention layers) that have sub-linear or even constant compute and memory requirements. Recent work has shown hybrid models to be competitive with more traditional Transformer architectures (Waleffe et al., 2024; Lieber et al., 2024; DeepMind, 2025). 

Motivated by improving inference efficiency, we introduce the Nemotron-H family of hybrid MambaTransformer models. The Nemotron-H models consist of a mixture of Mamba-2, self-attention and MLP layers, and achieve state-of-the-art accuracy and improved inference speed when compared to open-sourced Transformer models of similar size (Figure 1). The Nemotron-H family has a series of 8-billion-parameter models (Nemotron-H-8B-Base, Nemotron-H-8B-Instruct, NemotronH-8B-VLM), and a series of 47/56-billion-parameter models (Nemotron-H-47B-Base, NemotronH-56B-Base, Nemotron-H-56B-VLM) that offer either better or on-par accuracy compared to 

© 2025 NVIDIA. All rights reserved.

---

[referencia=29ab108383433c26 score=0.991]
In the setting described above, Nemotron-H-56B-Base can generate 2.4 _×_ more output tokens per second per GPU compared to Qwen-2.5-72B and Llama-3.1-70B (and 2.9 _×_ more after distillation to Nemotron-H-47B-Base, see §3). Compared to Llama-3.1-405B, Nemotron-H-56B-Base achieves 19.6 _×_ higher throughput. Similar to the larger models, Nemotron-H-8B-Base is also faster to infer than corresponding Transformer models. As shown in Figure 7, on longer contexts, we measure a 1.8 _×_ and 3 _×_ speedup compared to Qwen-2.5-7B and Llama-3.1-8B. Inference speedups are a byproduct of two factors: a) constant computation in the Mamba-2 layers as opposed to linear computation in self-attention layers, b) lower memory footprint from Mamba-2 layers facilitates using higher batch sizes, increasing efficiency. We expect further optimizing Nemotron-H inference to lead to additional speedups compared to Transformers, which have been heavily optimzed over the last couple of years.

---

[referencia=29ab108383433c26 score=0.977]
#### **2.6. Inference Speed** 

Due to the reduction in self-attention layers, Nemotron-H-8B/56B-Base provide inference-time speedups compared to the alternative Transformer models in Tables 4 and 5 above. To quantify these speedups, we plot the MMLU-Pro accuracy versus inference throughput for Nemotron-H-56B-Base 

13 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 

|25<br>20<br>25<br>30<br>35<br>40<br>45<br>50<br>55<br>MMLU-Pro accuracy (%)|50<br>75<br>100<br>125<br>150<br>175<br>200<br>225<br>250<br>Throughput (Output tokens/s/GPU)<br>1.8x<br>Nemotron-H-8B<br>Nemotron-T-8B<br>Llama-3.1-8B<br>Llama-3.2-3B<br>Qwen-2.5-7B<br>Gemma-3-12B<br>Gemma-3-27B<br>Input sequence length = 65536  / Output sequence length = 1024|
|---|---|



Figure 7 _|_ MMLU-Pro accuracy versus inference throughput (normalized by number of GPUs used) for Nemotron-H-8B-Base compared to existing similarly-sized Transformer models. 

and similarly-sized Transformer models in Figure 1 and for Nemotron-H-8B-Base and relevant baselines in Figure 7. We use an input sequence length of 65536 and ask the models to generate 1024 output tokens. We use an initial Megatron-LM implementation for Nemotron-H inference and vLLM v0.7.3<sup>12</sup> for baselines. In these experiments, we try to maximize per-GPU inference throughput by using as large a batch size as possible, and we run all experiments on NVIDIA H100 GPUs. We report results normalized by the number of GPUs used (i.e., output tokens per second per GPU).

---

[referencia=29ab108383433c26 score=0.977]
generated by DeepSeek-R1 (DeepSeek-AI, 2025b). Both Nemotron-H and the Qwen 2.5 models show significant improvement on the benchmark by simply changing the prompt. 

3. For code tasks (HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021) and their EvalPlus variants), we always sanitize the generations using EvalPlus (Liu et al., 2023b). 

4. General reasoning benchmarks (OpenBookQA (Mihaylov et al., 2018), PIQA (Bisk et al., 2019), Hellaswag (Zellers et al., 2019), Winogrande Sakaguchi et al. (2019)) are unchanged except for ARC-Challenge (Clark et al., 2018), where we present all options at the same time, similar to MMLU (Hendrycks et al., 2021a). 

Accuracy results for Nemotron-H-56B-Base and Nemotron-H-8B-Base on common benchmark tasks are shown in Table 4 and Table 5. Nemotron-H-56B-Base and Nemotron-H-47B-Base are both evaluated in FP8, and all other models are evaluated in BF16. Across both model sizes, NemotronH base models reach comparable or better accuracy relative to similarly-sized state-of-the-art Transformer models. 

We compare Nemotron-H-56B-Base directly with Qwen-2.5-72B-Base (Qwen, 2025) and Llama-3.170B-Base (Meta, 2024). Out of the 17 task we evaluate, Nemotron-H-56B-Base achieves the highest accuracy of the three models on 9 tasks, Qwen-2.5-72B-Base achieves the highest accuracy on 7 tasks, and Llama-3.1-70B-Base achieves the highest accuracy on 1 task; Nemotron-H-56B-Base outperforms Llama-3.1-70B-Base on all but that single task (Winogrande). We further compare Nemotron-H-56BBase with two much larger state-of-the-art models, DeepSeek-V3-671B-Base (DeepSeek-AI, 2025c) 

12

---

[referencia=29ab108383433c26 score=0.970]
Overall, the Nemotron-H family of models demonstrates that hybrid models can be state-of-the-art in terms of capabilities while offering improved inference speed. Moreover, we believe FP8 pre-training and compression techniques like MiniPuzzle make it cheaper and more efficient to create such models. 

2 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 



<!-- Start of picture text -->
Nemotron-H-8B<br>x3 x4 x1<br>Nemotron-H-56B<br>x3 x10 x1<br>FFN FFN FFN FFN FFN FFN FFN<br>Mamba-2 Mamba-2 Attention Mamba-2 Mamba-2 Mamba-2 Mamba-2 Mamba-2<br>FFN FFN FFN FFN FFN FFN FFN<br>Mamba-2 Mamba-2 Attention Mamba-2 Mamba-2 Mamba-2 Mamba-2 Mamba-2<br><!-- End of picture text -->

Figure 2 _|_ Nemotron-H-8B/56B model architectures. Roughly 8% of the total layers in the model are self-attention layers; these layers are evenly dispersed throughout the model. The rest of the model is made up of alternating Mamba-2 and FFN layers. 

To enable further research, we have released the following base model checkpoints in Hugging Face and NeMo formats on the Hugging Face and NGC model repositories: 

- **Nemotron-H-56B-Base.** Hugging Face and NGC. 

- **Nemotron-H-47B-Base.** Hugging Face and NGC. 

- **Nemotron-H-8B-Base.** Hugging Face and NGC. 

The rest of this technical report is organized as follows: 

- In §2, we discuss the Nemotron-H model architecture and the pre-training process (including details on the pre-training dataset and FP8 recipe used). 

- In §3, we describe the pruning and distillation methods used for model compression. 

- In §4, we introduce the vision-language models based on the Nemotron-H models. 

- In §5, we show that Nemotron-H models can be extended to create competitive instruct and long-context versions.

---

[referencia=29ab108383433c26 score=0.958]
|Hellaswag (10-shot)|**83.2**|82.5|80.3|82.3|_84.2_|
|Winogrande (5-shot)|**80.5**|78.8|76.1|78.1|_74.3_|
|PIQA (0-shot)|**82.2**|82.0|80.1|81.0|_81.8_|
|OpenbookQA (0-shot)|**47.2**|44.8|47.0|45.4||



Table 5 _|_ Accuracy of Nemotron-H-8B-Base versus existing SoTA models and a Transformer (Nemotron-T-8B-Base) trained on exactly the same data. Likelihood-based evaluations of the Gemma 3 model are based on the Gemma 3 report (DeepMind, 2025), all other numbers are run by us. We bold the highest accuracy in each row, excluding italicized numbers. 

and Llama-3.1-405B-Base (Meta, 2024); we use publicly-reported numbers for these two models on the subset of common tasks where numbers are reported. Surprisingly, Nemotron-H-56B-Base remains competitive with these models, outperforming DeepSeek-V3-671B-Base and Llama-3.1-405B-Base on 4 and 5 out of the 10 overlapping tasks respectively. 

We observe similar accuracy results for Nemotron-H-8B-Base compared to Qwen-2.5-7B-Base and Llama-3.1-8B-Base (Table 5). Out of the 15 tasks used for evaluation, Nemotron-H-8B-Base, Qwen2.5-7B-Base, and Llama-3.1-8B-Base achieve the highest accuracy of the three models on 7, 8, and 0 tasks respectively. Nemotron-H-8B-Base is particularly strong on commonsense understanding tasks, achieving the highest accuracy on 4 out of 5 tasks in this category. As above, we also include comparisons to a larger model, Gemma-3-12B-Base (DeepMind, 2025); Nemotron-H-8B-Base is competitive with the larger model.

---

[referencia=29ab108383433c26 score=0.948]
#### **2.1. Model Architecture** 

Nemotron-H models consist of a mixture of Mamba-2 (Dao & Gu, 2024), self-attention, and FFN layers as summarized in Figure 2 and Table 1. As suggested by prior work (Waleffe et al., 2024), 

3 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 

|**Mdl**|**Number of**|**Model**|**FFN**|**Q**|**KV**|**State**|**Mamba**|
|---|---|---|---|---|---|---|---|
|**oe**|**layers**|**dimension**|**dimension**|**heads**|**heads**|**dimension**|**groups**|
|Nemotron-H-8B|52|4096|21504|32|8|128|8|
|Nemotron-H-56B|118|8192|32768|64|8|256|8|



Table 1 _|_ Summary of the Nemotron-H hybrid Mamba-Transformer architectures. 

we set the number of attention layers to be roughly 8% of the total number of layers and evenly disperse them throughout the model. This amounts to 4 self-attention layers (out of 52 layers) for Nemotron-H-8B and 10 for Nemotron-H-56B (out of 118 layers). The rest of the layers consist of an even split between FFN and Mamba-2 layers. We also ensure that a) the first layer in the model is a Mamba-2 layer, b) the last layer in the model is a FFN layer, and c) self-attention layers always precede FFN layers (as they do in a standard Transformer block like in Vaswani et al. (2023)).

---

[referencia=29ab108383433c26 score=0.939]
#### **5.3. Results** 

#### **_5.3.1. Nemotron-H-47B-Reasoning-128K_** 

Across benchmarks in math, coding, science, tool use, and dialogue, **Nemotron-H-47B-Reasoning128K** achieves accuracy on par with or better than Llama-Nemotron Super 49B V1.0, and outperforms Qwen3 32B on all non-coding benchmarks. The model supports post-training quantization of all linear layers, enabling efficient deployment with minimal accuracy loss. We also provide the quantized checkpoint and its corresponding results to demonstrate effectiveness in practical settings.

---

[referencia=29ab108383433c26 score=0.934]
#### **_5.3.2. Nemotron-H-8B-Reasoning-128K_** 

**Checkpoint merging** We observed that the smaller 8B model struggled on internal safety benchmarks. To address this, we opted for checkpoint interpolation Wortsman et al. (2022), blending in an earlier RL checkpoint aligned from a safer long-context extended checkpoint. Checkpoint interpolation is performed by linearly interpolating model weights: (1 _− 𝛼_ ) _* 𝑤𝑚𝑜𝑑𝑒𝑙_ 1 + _𝛼 * 𝑤𝑚𝑜𝑑𝑒𝑙_ 2. We experimented with a parameter sweep over _𝛼_ values from 0.1 to 0.9 in increments of 0.1, and found that values around 0.5 offered a good trade-off between reasoning capabilities and safe behavior. 

Across benchmarks in AIME25, science, tool use, and instruction-following, **Nemotron-H-8BReasoning-128K** achieves accuracy on par with or better than Llama-Nemotron Nano 8B V1.0. The model supports post-training quantization of all linear layers, enabling efficient deployment with 

24 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models

---

[referencia=29ab108383433c26 score=0.926]
|MBPP+ (0-shot greedy pass@1)|67.2|65.6|**71.7**|66.9|||
|**Commonsense understanding**|||||||
|Arc-Challenge (25-shot)|95.0|94.6|**95.8**|93.0|_95.3_|_95.3_|
|Hellaswag (10-shot)|**89.0**|87.9|87.6|88.1|_88.9_|_89.2_|
|Winogrande (5-shot)|84.5|83.9|84.4|**85.6**|_84.9_|_85.2_|
|PIQA (0-shot)|**85.0**|83.9|83.6|84.1|_84.7_|_85.9_|
|OpenbookQA (0-shot)|48.6|**48.8**|46.2|47.6|||
|**Long-thought reasoning**|||||||
|MATH (R1-style 4-shot COT)|**87.8**||73.9|38.7|||
|MATH Level 5 (R1-style 4-shot COT)|**74.8**||53.2|16.7|||



Table 4 _|_ Accuracy of Nemotron-H-56B-Base (and its distilled version Nemotron-H-47B-Base, discussed in §3) versus existing SoTA models. N-H is short for Nemotron-H, DS is short for DeepSeek. Numbers in italics are from the DeepSeek-V3 report (DeepSeek-AI, 2025c), all other numbers are run by us. We bold the highest accuracy in each row, excluding italicized numbers. 

generated by DeepSeek-R1 (DeepSeek-AI, 2025b). Both Nemotron-H and the Qwen 2.5 models show significant improvement on the benchmark by simply changing the prompt.

---

[referencia=29ab108383433c26 score=0.913]
19 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 

|**Task**|**Nemotron-H**<br>**8B-VLM**|**VLM w/ Llama3.1**<br>**8B-Instruct**|**VLM w/ Qwen2.5**<br>**7B-Instruct**|
|---|---|---|---|
|MMMU (val)|**51.3**|44.8|51.1|
|MathVista|62.5|61.7|**63.8**|
|ChartQA|84.8|**85.4**|84.9|
|AI2D|89.6|90.9|**91.0**|
|OCRBench|840|**847**|836|
|TextVQA|76.2|**76.4**|76.1|
|RealWorldQA|**62.2**|60.9|60.6|
|DocVQA|90.6|**91.3**|91.2|



Table 7 _|_ Evaluation of Nemotron-H-8B-VLM on vision-language benchmarks. We compare to the VLMs built with Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct using the same training recipe.

---

[referencia=29ab108383433c26 score=0.901]
#### **3.2. Importance Estimation** 

MiniPuzzle first collects importance or sensitivity scores for each model component (e.g., layers, FFN neurons) to help decide which components to remove; this is the _importance estimation_ phase. The scores computed in this phase are used to decide which model components can be pruned. We note that sensitivity analysis based on gradient information is typically impractical at modern LLM scale (Muralidharan et al., 2024); instead, we rely on a lightweight strategy that uses only on forward passes. In this work, we use a simplified approach that works well in our ablation studies: a) prune layers, and b) prune FFN hidden dimensions (effectively neurons). We also experimented with pruning Mamba heads and Mamba head dimension; unfortunately, both axes caused severe accuracy degradation (particularly head dimension pruning). 

We now describe how we compute the importance of each layer and FFN neuron. 

**Layer importance.** We use the scoring method from Puzzle to estimate the importance of each layer in the model. Given an input tensor, layer importance is computed as the Mean Squared Error (MSE) between the intermediate activation tensor just before the LM head of the full model and the same activation tensor for a model with the particular layer removed. We average these rankings over a small random subset of the training data (128 samples in our case) to obtain a reliable estimate of importance that takes into account sample variability. 

Figure 9 plots average importance scores of each layer in Nemotron-H-56B-Base. The green, blue and red dotted lines correspond to self-attention, FFN and Mamba layers. We notice from the figure that the 56B model follows a typical pattern observed in Minitron: the most important layers are concentrated at the beginning and end of the model. Additionally, MSE importance reveals that even though the 56B model only has 10 self-attention layers, some self-attention layers are ranked among the least important, particularly the 84th (7th self-attention layer). However, layers 40, 51, 62 and 73 seem to be more important compared to the other layers in their immediate vicinity. 

15 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 



<!-- Start of picture text -->

---

[referencia=29ab108383433c26 score=0.899]
Figure 11 _|_ Pruned layers for the top three candidates. Each row represents a candidate, with dots indicating dropped layers. Vertical dotted lines denote layer types: green for self-attention, blue for FFN, and red for Mamba. 

   - the irrelevant layers and prune all FFN layers to the same target width. Only architectures that meet the target memory constraint of less than 31.7 GiB (computed as the total memory required for FP4 inference on a context of size 1 million tokens) are retained, resulting in around 400 candidate architectures. 

2. **Architecture ranking.** We score the candidate architectures using a lightweight metric that compares them to the parent model (Nemotron-H-56B-Base) on a small validation corpus with 1 million tokens. Specifically, we use two different scores to estimate the quality of each candidate model: a) next-token accuracy which computes how often the child model correctly predicts the next ground-truth token, and b) next-token parent agreement which computes how often the child model agrees with the parent model about the greedy prediction of the next token. We rank all candidate architectures using both scoring metrics, and retain the top 130 performers. 

3. **Candidate selection.** We now refine the set of ranked architectures from 130 to a manageable 3 by benchmarking them on a subset of evaluation tasks. The first column of Table 6 lists the tasks we use to evaluate the final 3 candidates. We use the average scores across all these tasks for evaluation. Figure 10 plots the average benchmark scores for all 130 candidates, and Figure 11 illustrates the specific layers dropped by all three candidates. Candidates 1 and 2 achieve the highest benchmark scores and drop similar layers. Candidate 3, which drops a slightly different set of layers, performs significantly worse after pruning. However, we include it here to study the extent to which distillation can compensate for the loss. 

17 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models

---

[referencia=29ab108383433c26 score=0.862]
9 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 



<!-- Start of picture text -->
BF16 FP8<br>MMLU Average commonsense understanding<br>70<br>64<br>65<br>62<br>60<br>60<br>55<br>58<br>50<br>56<br>45<br>54<br>Tokens 1e13 Tokens 1e13<br>Average code GSM8K<br>55<br>50<br>60<br>45<br>40 40<br>35<br>30 20<br>25<br>Tokens 1e13 Tokens 1e13<br>0.00 0.25 0.50 0.75 1.00 1.25 1.50 0.00 0.25 0.50 0.75 1.00 1.25 1.50<br>0.00 0.25 0.50 0.75 1.00 1.25 1.50 0.00 0.25 0.50 0.75 1.00 1.25 1.50<br>Accuracy (%) Accuracy (%)<br>Accuracy (%) Accuracy (%)<br><!-- End of picture text -->

Figure 6 _|_ Downstream task accuracies for a pair of 8B-parameter Transformer models trained on 15 trillion tokens with BF16 and mixed precision FP8. FP8 accuracies are consistently equal to or better than BF16 ones. The jump in accuracies at 9 trillion tokens is a result of switching data mixtures from Phase 1 to Phase 2. 

For coding and math tasks, experiments using per-tensor current scaling often had results that were substantially better than BF16 experiments. Figure 6 shows the accuracy gap between two 8B-parameter Transformers trained for 15 trillion tokens, with one trained in FP8 and the other in BF16. Because of the equal or better downstream results on the same token horizon, we never had to overtrain FP8 models relative to BF16 ones. We ran evaluations in both BF16 and FP8 precision for models trained in FP8; they were typically the same, with BF16 evaluations usually slightly better. However, for the 56B model, the FP8 evaluations eventually outperformed the BF16 ones.

---

[referencia=29ab108383433c26 score=0.855]
Table 11 _|_ Comparison of benchmark performance across multiple model variants. Best scores per row are shown in bold. 

|**Benchmark**|**Llama-Nemotron**<br>**Nano 8B v1.0**|**Nemotron-H 8B**<br>**Reasoning**|**Nemotron-H 8B**<br>**Reasoning (FP8)**|
|---|---|---|---|
|AIME25|51.4|**51.7**|46.7|
|MATH500|**94.8**|94.0|94.0|
|GPQA-D|53.5|**55.1**|54.5|
|MBPP|84.1|86.0|**86.2**|
|MBPP_PLUS|71.4|**74.1**|73.3|
|LCB|**52.6**|49.5|44.8|
|BFCL|63.6|68.8|**70.6**|
|IFEVAL-Prompt|**71.8**|71.4|71.5|
|IFEVAL-Instruction|79.3|79.6|**79.9**|



Table 12 _|_ Comparison of benchmark performance across multiple 8B model variants. Best scores per row are bolded. 

minimal accuracy loss. We also provide the FP8 quantized checkpoint and its corresponding results to demonstrate effectiveness in practical settings.

---

[referencia=29ab108383433c26 score=0.843]
Table 5 additionally includes the largest apples-to-apples comparison of a hybrid Mamba-Transformer and pure Transformer model to date (Nemotron-H-8B-Base versus Nemotron-T-8B-Base). NemotronH-8B-Base reaches higher accuracy than the Transformer trained on exactly the same data on 7 out of 15 tasks, and is within one point on an additional 4 tasks. Overall, this experiment shows that hybrid models can reach equal or better accuracy compared to Transformer models when trained at state-of-the-art scales.

---

[referencia=29ab108383433c26 score=0.818]
24 

Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models 

|**Benchmark**|**Llama-Nemotron**<br>**Super V1**|**Nemotron-H 47B**<br>**Reasoning**|**Nemotron-H 47B**<br>**Reasoning (FP8)**|**Qwen3**<br>**32B**|
|---|---|---|---|---|
|AIME25|53.0|54.2|54.2|**55.8**|
|MATH500|96.6|96.2|**96.8**|91.4|
|GPQA-D|65.1|**65.7**|64.6|65.2|
|MBPP|90.2|91.8|91.9|**95.5**|
|MBPP_PLUS|75.1|79.9|79.9|**81.5**|
|LCB|41.2|50.2|53.4|**64.2**|
|BFCL|72.7|72.9|**73.2**|71.3|
|IFEVAL-Prompt|81.8|**84.5**|84.5|83.9|
|IFEVAL-Instruction|87.4|**89.7**|89.6|88.6|
|Arena Hard|85.0|85.0|80.5|**93.8**|



Table 11 _|_ Comparison of benchmark performance across multiple model variants. Best scores per row are shown in bold.