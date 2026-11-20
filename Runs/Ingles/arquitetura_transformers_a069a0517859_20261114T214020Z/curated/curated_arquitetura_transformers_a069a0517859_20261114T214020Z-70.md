[referencia=5dd64e15cc7592b1 score=0.997]
# Mamba: Linear-Time Sequence Modeling with Selective State Spaces 

Albert Gu<sup>∗1</sup> and Tri Dao<sup>∗2</sup> 

1 Machine Learning Department, Carnegie Mellon University 

2 Department of Computer Science, Princeton University agu@cs.cmu.edu, tri@tridao.me 

##### **Abstract** 

Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers’ computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to _selectively_ propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks ( **Mamba** ). Mamba enjoys fast inference (5× higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation.

---

[referencia=5dd64e15cc7592b1 score=0.993]
### **4.5 Speed and Memory Benchmarks** 

We benchmark the speed of the SSM scan operation (state expansion _𝑁_ = 16), as well as the end-to-end inference throughput of Mamba, in Figure 8. Our efficient SSM scan is faster than the best attention implementation that we know of (FlashAttention-2 (Dao 2024)) beyond sequence length 2K, and up to 20-40× faster than a standard scan implementation in PyTorch. Mamba achieves 4-5× higher inference throughput than a Transformer of similar size, since without the KV cache it can use much higher batch sizes. For example, a Mamba-6.9B (untrained) would have higher inference throughput than a 5× smaller Transformer-1.3B. Details in Appendix E.5, which additionally includes a benchmark of memory consumption. 



<!-- Start of picture text -->
FlashAttention-2Scan vs Convolution vs Attention time (A100 80GB PCIe) Mamba 1.4BInference throughput on A100 80GB (prompt length 20481688 ) 1814<br>1000 Convolution 1500 Transformer 1.3BMamba 6.9B 1445<br>Scan (PyTorch) Transformer 6.7B<br>100 Scan (ours)OOM 1089<br>10 1000<br>744<br>0.11 500 140 79 58 46 247 132 101 66 441 199 172 91 265 261 109 323 364 120 364 443 OOM OOM 490 OOM OOM 515 OOM<br>512 1k 2k 4k 8k 16k 32k 64k 128k 256k 512k 1 2 4 8 16 32 64 128<br>Sequence length Batch size<br>Time (ms)<br>Throughput (tokens / s)<br><!-- End of picture text -->

Figure 8: ( **Efficiency Benchmarks** .) ( _Left_ ) Training: our efficient scan is 40× faster than a standard implementation. ( _Right_ ) Inference: as a recurrent model, Mamba can achieve 5× higher throughput than Transformers.

---

[referencia=5dd64e15cc7592b1 score=0.971]
We empirically validate Mamba’s potential as a general sequence FM backbone, in both pretraining quality and domainspecific task performance, on several types of modalities and settings: 

- **Synthetics.** On important synthetic tasks such as copying and induction heads that have been proposed as being key to large language models, Mamba not only solves them easily but can _extrapolate solutions indefinitely long_ ( _>_ 1M tokens). 

- **Audio and Genomics.** Mamba out-performs prior state-of-the-art models such as SaShiMi, Hyena, and Transformers on modeling audio waveforms and DNA sequences, both in pretraining quality and downstream metrics (e.g. reducing FID on a challenging speech generation dataset by more than half). In both settings, its _performance improves with longer context up to million-length sequences_ . 

- **Language Modeling.** Mamba is the first _linear-time sequence model that truly achieves Transformer-quality performance_ , both in pretraining perplexity and downstream evaluations. With scaling laws up to 1B parameters, we show that Mamba exceeds the performance of a large range of baselines, including very strong modern Transformer training recipes based on LLaMa (Touvron et al. 2023). Our Mamba language model has 5× generation throughput compared to Transformers of similar size, and Mamba-3B’s quality matches that of Transformers twice its size (e.g. 4 points higher avg. on common sense reasoning compared to Pythia-3B and even exceeding Pythia-7B). 

Model code and pre-trained checkpoints are open-sourced at https://github.com/state-spaces/mamba.

---

[referencia=5dd64e15cc7592b1 score=0.922]
**Scaling.** Our empirical evaluation is limited to small model sizes, below the threshold of most strong open source LLMs (e.g. Llama (Touvron et al. 2023)) as well as other recurrent models such as RWKV (B. Peng et al. 2023) and RetNet (Y. Sun et al. 2023), which have been evaluated at the 7B parameter scale and beyond. It remains to assess whether Mamba still compares favorably at these larger sizes. We also note that scaling SSMs may involve further engineering challenges and adjustments to the model that are not discussed in this paper. 

## **6 Conclusion** 

We introduce a selection mechanism to structured state space models, allowing them to perform context-dependent reasoning while scaling linearly in sequence length. When incorporated into a simple attention-free architecture, Mamba achieves state-of-the-art results on a diverse set of domains, where it matches or exceeds the performance of strong Transformer models. We are excited about the broad applications of selective state space models to build foundation models for different domains, especially in emerging modalities requiring long context such as genomics, audio, and video. Our results suggest that Mamba is a strong candidate to be a general sequence model backbone. 

#### **Acknowledgments** 

We thank Karan Goel, Arjun Desai, and Kush Bhatia for helpful feedback on the draft.

---

[referencia=5dd64e15cc7592b1 score=0.904]
#### **4.2.2 Downstream Evaluations** 

Table 3 shows the performance of Mamba on a range of popular downstream zero-shot evaluation tasks. We compare against the most well-known open source models at these sizes, most importantly Pythia (Biderman et al. 2023) and RWKV (B. Peng et al. 2023) which were trained with the same tokenizer, dataset, and training length (300B tokens) as our models. (Note that Mamba and Pythia are trained with context length 2048, while RWKV was trained with context length 1024.) 

Table 3: ( **Zero-shot Evaluations** .) Best results for each size in bold. We compare against open source LMs with various tokenizers, trained for up to 300B tokens. Pile refers to the validation split, comparing only against models trained on the same dataset and tokenizer (GPT-NeoX-20B). For each model size, Mamba is best-in-class on every single evaluation result, and generally matches baselines at twice the model size.

---

[referencia=5dd64e15cc7592b1 score=0.897]
#### **E.3.2 Scaling: Model Size Details** 

**Models.** The models we consider are: 

- Transformer++: a Transformer with improved architecture, notably the usage of RoPE positional encodings (Su et al. 2021). Informally, we found these to be noticeably better than vanilla positional encodings from (Vaswani et al. 2017). 

- HyenaDNA: the Hyena model from Nguyen, Poli, et al. (2023) and Poli et al. (2023), which is roughly a Transformer with the MHA block replaced by an H3 block using a global convolution parameterized by an MLP. 

- Mamba: the standard Mamba architecture. 

**Model Sizes.** We use the following model sizes. 

|Blocks|4|5|6|7|8|10|12|
|---|---|---|---|---|---|---|---|
|Model Dimension|64|96|128|192|256|384|512|
|Params (Approx.)|250K|700K|1.4M|3.5M|7.0M|19.3M|40.7M|



Note that the number of blocks for Mamba is doubled, because one Transformer “layer” includes both the MHA and MLP blocks (and similarly for Hyena), which requires two Mamba blocks to match parameters (Section 3.4). 

32 

**Training.** For each model (Transformer++, HyenaDNA, Mamba), we swept the learning rate across {1 _𝑒_ − 3 _,_ 2 _𝑒_ − 3 _,_ 4 _𝑒_ − 3 _,_ 8 _𝑒_ − 3}. The optimal Transformer and HyenaDNA learning rates were 2e-3 across all sizes. The optimal Mamba learning rate was 8e-3; note that Mamba performed better than baselines with matched learning rates (2e-3), but was more stable and improved even more at higher learning rates. (Furthermore, as this LR is on the upper range of the sweep, it is possible that our results are still suboptimal.)

---

[referencia=5dd64e15cc7592b1 score=0.837]
### **4.2 Language Modeling** 

We evaluate the Mamba architecture on standard autoregressive language modeling against other architectures, on both pretraining metrics (perplexity) and zero-shot evaluations. We set the model sizes (depth and width) to mirror GPT3 specifications. We use the Pile dataset (L. Gao, Biderman, et al. 2020), and follow the training recipe described in Brown et al. (2020). All training details are in Appendix E.2. 

#### **4.2.1 Scaling Laws** 

For baselines, we compare against the standard Transformer architecture (GPT3 architecture), as well as the strongest Transformer recipe we know of (here referred to as Transformer++), based on the PaLM and LLaMa architectures (e.g. rotary embedding, SwiGLU MLP, RMSNorm instead of LayerNorm, no linear bias, and higher learning rates). We also compare against other recent subquadratic architectures (Figure 4). All model details are in Appendix E.2. 

Figure 4 shows scaling laws under the standard Chinchilla (Hoffmann et al. 2022) protocol, on models from ≈ 125 _𝑀_ to ≈ 1 _._ 3 _𝐵_ parameters. **Mamba is the first attention-free model to match the performance of a very strong Transformer recipe (Transformer++) that has now become standard, particularly as the sequence length grows.** (We note that full results on context length 8k are missing for the RWKV and RetNet baselines, prior strong recurrent models that can also be interpreted as SSMs, because of a lack of efficient implementations leading to out-of-memory or unrealistic computation requirements.) 

11

---

[referencia=5dd64e15cc7592b1 score=0.810]
Figure 5: ( **DNA Scaling Laws** .) Pretraining on the HG38 (human genome) dataset. ( _Left_ ) Fixing short context length 2<sup>10</sup> = 1024 and increasing size from ≈ 200 _𝐾_ to ≈ 40 _𝑀_ parameters, Mamba scales better than baselines. ( _Right_ ) Fixing model size and increasing sequence lengths while keeping tokens/batch and total training tokens fixed. Unlike baselines, the selection mechanism of Mamba facilitates better performance with increasing context length. 

#### **4.3.1 Scaling: Model Size** 

In this experiment, we investigate the scaling properties of genomics foundation models with various model backbones (Figure 5 _Left_ ). 

**Training.** To advantage the baselines, we train on a short sequence length of 1024; as shown in Section 4.3.2, we expect results to favor Mamba even more at longer sequence lengths. We fix a global batch size of 1024, for a total of 2<sup>20</sup> ≈ 1 _𝑀_ tokens per batch. Models were trained for 10 _𝐾_ gradient steps for a total of 10 _𝐵_ tokens. 

**Results.** Figure 5 ( _Left_ ) shows that Mamba’s pretraining perplexity improves smoothly with model size, and that Mamba scales better than both HyenaDNA and Transformer++. For example, at the largest model size of ≈ 40 _𝑀_ parameters, the curve shows that **Mamba can match the Transformer++ and HyenaDNA models with roughly** 3× **to** 4× **fewer parameters** .

---

[referencia=5dd64e15cc7592b1 score=0.796]
**Architecture and Training Details.** Our models are: 

- **Transformer** : The standard Transformer based on GPT3 (Table 12). 

- **Transformer++** : A Transformer with an improved architecture, namely rotary positional encodings (Su et al. 2021) and SwiGLU MLP (Shazeer 2020), and the improved training recipe above. 

- **Hyena** : Interleaving a Hyena block (the H3 block with S4 replaced by a global convolution parameterized by an MLP) with standard MLP blocks. The MLP blocks have expansion factor 2 instead of 4 and the number of layers is correspondingly increased by 1 _._ 5× to preserve parameter count. 

- **H3++** : The H3 architecture with a few modifications, including (i) using the same “thin” Hyena dimensions above (ii) the improved training recipe above (iii) a linear attention _head dimension_ of 8. 

- **RWKV** : The default RWKV model from B. Peng et al. (2023), including its modified MLP block. We also used as much of its specified training recipe as possible, such as increasing the learning rates by 2× or 3× on certain parameters. 

- **RetNet** : The default RetNet model from Y. Sun et al. (2023). We also gave it the improved training recipe above. 

- **Mamba** : The standard Mamba architecture, with the improved training recipe.

---

[referencia=5dd64e15cc7592b1 score=0.791]
#### **4.4.2 Autoregressive Speech Generation** 

SC09 is a benchmark speech generation dataset (Donahue, McAuley, and Puckette 2019; Warden 2018), consisting of 1-second clips sampled at 16000 Hz of the digits “zero” through “nine” with highly variable characteristics. We largely follow the autoregressive training setup and generation protocol of Goel et al. (2022). 

Table 4 shows automated metrics of the Mamba-UNet model compared to a variety of baselines from Goel et al. (2022): WaveNet (Oord et al. 2016), SampleRNN (Mehri et al. 2017), WaveGAN (Donahue, McAuley, and Puckette 2019), DiffWave (Z. Kong et al. 2021), and SaShiMi. **A small Mamba model outperforms the state-of-the-art (and much larger) GANand diffusion- based models.** A larger model parameter-matched to the baselines further improves on fidelity metrics dramatically. 

Table 5 takes the small Mamba model and investigates combinations of different architectures for the outer stages and center stage. It shows that Mamba is consistently better than S4+MLP in the outer blocks, and Mamba _>_ S4+MLP _>_ MHA+MLP in the center blocks. 

14 

Table 4: ( **SC09** ) Automated metrics for unconditional generation on a challenging dataset of fixed-length speech clips. ( _Top to Bottom_ ) Autoregressive baselines, non-autoregressive baselines, Mamba, and dataset metrics. 

Table 5: ( **SC09 Model Ablations** ) Models with 6M parameters. In SaShiMi’s U-Net backbone, there are 8 center blocks operating on sequence length 1000, sandwiched on each side by 8 outer blocks on sequence length 4000, sandwiched by 8 outer blocks on sequence length 16000 (40 blocks total). The architecture of the 8 center blocks are ablated independently of the rest. Note that Transformers (MHA+MLP) were not tested in the more important outer blocks because of efficiency constraints.

---

[referencia=5dd64e15cc7592b1 score=0.747]
We use batch size of 1 and increase the sequence length from 2<sup>9</sup> = 512, 2<sup>10</sup> ≈ 1 _𝐾_ , 2<sup>11</sup> ≈ 2 _𝐾_ , up to 2<sup>19</sup> ≈ 500 _𝐾_ (some of the baselines run out of memory before reaching 500K). We use a model dimension of _𝐷_ = 1024 and state dimension _𝑁_ = 16. We measure with BF16 inputs, which is the data type most commonly used for large scale training. 

**End-to-end Inference.** We measure the inference throughput of a Mamba 1.4B model and an untrained Mamba 6.9B model, against a standard Transformer (GPT3 architecture) at 1.3B and 6.7B size. We use the standard Transformer implementation in the Huggingface transformers library. 

We set the prompt length to be 2048 and the generation length to be 128. We vary the batch size from 1, 2, 4, 8, 16, 32, 64, to 128, and measure time time taken to generate 128 tokens. We then calculate the throughput (tokens/s) as batch size × 128/time taken. We repeat the measurements 3 times and take the average. Measurements are done on an A100 80GB PCIe GPU. 

**Memory Benchmark.** The memory usage simply scales proportionally to the size of the activation tensors, as with most deep sequence models. We report measurements of the training memory requirements of 125M models on 1 A100 80GB GPU. Each batch consists of sequences of length 2048. We compare to the most memory-efficient Transformer implementation we are aware of (with kernel fusion from torch.compile and with FlashAttention-2). Table 15 shows that Mamba’s memory requirement is comparable to a similar-sized Transformer with an extremely optimized implementation, and we expect further improvement in Mamba’s memory footprint in the future. 

36

---

[referencia=5dd64e15cc7592b1 score=0.712]
#### **E.4.2 SC09 Speech Generation** 

Autoregressive training largely followed the autoregressive language modeling protocol, such as 

- Weight decay 0 _._ 1 

- Learning rate warmup for 10% of total steps 

- AdamW optimizer with _𝛽_ = (0 _._ 9 _,_ 0 _._ 95) 

- Gradient clip value 0 _._ 1 

We used a learning rate of 0 _._ 002 and 200000 training steps at a batch size of 16. 

The large Mamba model in Table 4 has 15 layers per stage with an outer dimension of _𝐷_ = 96 and pooling factor 4. We note that this dataset is small (training went through 100 epochs) and for this large model, there was significant overfitting of the BPB or NLL. However, automated metrics of generated samples continually improving throughout training. 

The models in the architecture ablations in Table 5 all have 8 layers per stage with an outer dimension of D = 64 and pooling factor 4. The S4+MLP block has roughly 2 _𝐷_<sup>2</sup> + 4 _𝐷_<sup>2</sup> parameters (expansion factor 2 in the MLP). The Transformer block has 4 _𝐷_<sup>2</sup> + 2 _𝐷_<sup>2</sup> parameters (expansion factor 1 in the MLP). The Mamba block has the usual ≈ 6 _𝐷_<sup>2</sup> parameters. All models have roughly 6M total parameters.

---

[referencia=5dd64e15cc7592b1 score=0.666]
**Architecture.** We simplify prior deep sequence model architectures by combining the design of prior SSM architectures (Dao, Fu, Saab, et al. 2023) with the MLP block of Transformers into a single block, leading to a simple and homogenous architecture design ( **Mamba** ) incorporating selective state spaces. 

Selective SSMs, and by extension the Mamba architecture, are fully recurrent models with key properties that make them suitable as the backbone of general foundation models operating on sequences. (i) High quality: selectivity brings strong performance on dense modalities such as language and genomics. (ii) Fast training and inference: computation and memory scales linearly in sequence length during training, and unrolling the model autoregressively during inference requires only constant time per step since it does not require a cache of previous elements. (iii) Long context: the quality and efficiency together yield performance improvements on real data up to sequence length 1M. 

We empirically validate Mamba’s potential as a general sequence FM backbone, in both pretraining quality and domainspecific task performance, on several types of modalities and settings:

---

[referencia=5dd64e15cc7592b1 score=0.660]
> ∗Alphabetical by first name. 

1 

Arena (Tay, Dehghani, Abnar, et al. 2021). Many flavors of SSMs (Gu, Goel, and Ré 2022; Gu, Gupta, et al. 2022; Gupta, Gu, and Berant 2022; Y. Li et al. 2023; Ma et al. 2023; Orvieto et al. 2023; Smith, Warrington, and Linderman 2023) have been successful in domains involving continuous signal data such as audio and vision (Goel et al. 2022; Nguyen, Goel, et al. 2022; Saon, Gupta, and Cui 2023). However, they have been less effective at modeling discrete and information-dense data such as text. 

We propose a new class of **selective state space models** , that improves on prior work on several axes to achieve the modeling power of Transformers while scaling linearly in sequence length. 

**Selection Mechanism.** First, we identify a key limitation of prior models: the ability to efficiently _select_ data in an input-dependent manner (i.e. focus on or ignore particular inputs). Building on intuition based on important synthetic tasks such as selective copy and induction heads, we design a simple selection mechanism by parameterizing the SSM parameters based on the input. This allows the model to filter out irrelevant information and remember relevant information indefinitely. 

**Hardware-aware Algorithm.** This simple change poses a technical challenge for the computation of the model; in fact, all prior SSMs models must be time- and input-invariant in order to be computationally efficient. We overcome this with a hardware-aware algorithm that computes the model recurrently with a scan instead of convolution, but does not materialize the expanded state in order to avoid IO access between different levels of the GPU memory hierarchy. The resulting implementation is faster than previous methods both in theory (scaling linearly in sequence length, compared to pseudo-linear for all convolution-based SSMs) and on modern hardware (up to 3× faster on A100 GPUs).

---

[referencia=5dd64e15cc7592b1 score=0.628]
Figure 4: ( **Scaling Laws** .) Models of size ≈ 125 _𝑀_ to ≈ 1 _._ 3 _𝐵_ parameters, trained on the Pile. Mamba scales better than all other attention-free models and is the first to match the performance of a very strong “Transformer++” recipe that has now become standard, particularly as the sequence length grows. 

Out of positional encoding variants for attention models, xPos (which was designed for length extrapolation) is slightly better than the others; also note that all attention models were only tested up to sequence length 2<sup>14</sup> = 16384 due to memory limitations. Out of other SSMs, H3 and Hyena are similar, contrary to the findings in Poli et al. (2023).

---

[referencia=5dd64e15cc7592b1 score=0.619]
Figure 9 ( _Right_ ) shows these variants compared to the original (homogenous) Mamba architecture. Interestingly, neither change matters too much. The Mamba-MLP architecture is only slightly worse, and still better than all models except Transformer++. The Mamba-MHA architecture is only slightly better, which is somewhat surprising in light of the fact that many recent works have found that combining (LTI) SSMs with Attention can lead to substantial improvements (Dao, Fu, Saab, et al. 2023; Fathi et al. 2023; Fathullah et al. 2023; Saon, Gupta, and Cui 2023; Zuo et al. 2022). 

**H3 Architecture: Training Recipes.** Next we ablate differences between the Hyena and H3++ models, our weakest and strongest models outside of Transformer++ and Mamba, particularly to isolate the effect of training recipes. 

- **Hyena** : The Hyena block with its original architecture and GPT3 training recipe (same as Figure 4). 

- **Hyena+** : The same architecture but with the improved training recipe described above. 

- **H3+** : The same architecture as Hyena+ but with the Hyena convolution kernel swapped out for S4D convolution kernel. 

- **H3++** : The same as H3+, but with a linear attention _head dimension_ of 8. This increases computation inside the SSM recurrence but does not increase parameters. 

Our general convention is that “Model+” represents the base model with the improved training recipe, and “Model++” also allows for architectural changes. 

Figure 9 ( _Right_ ) shows that 

- A large improvement is achieved by the improved training recipe, which was used for many of the models in the main Figure 4 (RetNet, H3++, Transformer++, Mamba). 

- The choice of the inner LTI SSM does not matter (e.g. Hyena vs. S4), consistent with findings throughout this paper. 

- The head dimension expansion improves performance, consistent with one of our main themes that expanded state dimension improves performance for SSMs (Section 3).

---

[referencia=5dd64e15cc7592b1 score=0.583]
### **E.5 Efficiency Benchmark** 

**Scan Operation.** We compare the core operation of selective SSMs, which is the parallel scan (Section 3.3), against convolution and attention, measured on an A100 80GB PCIe GPU. Note that these do not include the cost of other operations outside of this core operation, such as computing the convolutional kernel in global-convolution models, or computing the QKV projections in attention. 

As a baseline, we implement a standard parallel scan in PyTorch with no kernel fusion. This requires materializing the parameters _𝑨, 𝑩, 𝑪_ in HBM. 

Our scan implementation fuses the discretization step and the parallel scan, avoiding the cost of materializing all the large parameters in HBM. 

35 

Table 15: ( **Memory benchmark** .) Mamba’s memory footprint is comparable to the most optimized Transformer. Results for 125M models. 

|Batch size|Transformer (w/ FlashAttention-2)|Mamba|
|---|---|---|
|1|4.6GB|4.8GB|
|2|5.2GB|5.8GB|
|4|6.9GB|7.3GB|
|8|11.5GB|12.3GB|
|16|20.7GB|23.1GB|
|32|34.5GB|38.2GB|



For convolution, we use the standard implementation in PyTorch, which separately performs FFTs on the inputs and the filters, multiply them in frequency domain, then performs an inverse FFT to obtain the result. The theoretical complexity is _𝑂_ ( _𝐿_ log( _𝐿_ )) for sequence length _𝐿_ . 

For attention, we compare against the fastest implementation that we are aware of (FlashAttention-2 (Dao 2024)), with causal mask. Note that FlashAttention-2 with causal mask is about 1.7× faster than without causal mask, since approximately only half of the attention entries are computed.

---

[referencia=5dd64e15cc7592b1 score=0.583]
## **1 Introduction** 

Foundation models (FMs), or large models pretrained on massive data then adapted for downstream tasks, have emerged as an effective paradigm in modern machine learning. The backbone of these FMs are often _sequence models_ , operating on arbitrary sequences of inputs from a wide variety of domains such as language, images, speech, audio, time series, and genomics (Brown et al. 2020; Dosovitskiy et al. 2020; Ismail Fawaz et al. 2019; Oord et al. 2016; Poli et al. 2023; Sutskever, Vinyals, and Quoc V Le 2014). While this concept is agnostic to a particular choice of model architecture, modern FMs are predominantly based on a single type of sequence model: the Transformer (Vaswani et al. 2017) and its core attention layer (Bahdanau, Cho, and Bengio 2015) The efficacy of self-attention is attributed to its ability to route information densely within a context window, allowing it to model complex data. However, this property brings fundamental drawbacks: an inability to model anything outside of a finite window, and quadratic scaling with respect to the window length. An enormous body of research has appeared on more efficient variants of attention to overcome these drawbacks (Tay, Dehghani, Bahri, et al. 2022), but often at the expense of the very properties that makes it effective. As of yet, none of these variants have been shown to be empirically effective at scale across domains. 

Recently, structured state space sequence models (SSMs) (Gu, Goel, and Ré 2022; Gu, Johnson, Goel, et al. 2021) have emerged as a promising class of architectures for sequence modeling. These models can be interpreted as a combination of recurrent neural networks (RNNs) and convolutional neural networks (CNNs), with inspiration from classical state space models (Kalman 1960). This class of models can be computed very efficiently as either a recurrence or convolution, with linear or near-linear scaling in sequence length. Additionally, they have principled mechanisms for modeling long-range dependencies (Gu, Dao, et al. 2020) in certain data modalities, and have dominated benchmarks such as the Long Range 

> ∗Alphabetical by first name. 

1

---

[referencia=5dd64e15cc7592b1 score=0.574]
#### **E.2.2 Additional Scaling Law Ablations** 

We perform additional ablations on the architecture using the same protocol as the 2k context length scaling laws in Figure 4 ( _Left_ ). 

**Mamba Architecture: Interleaving Blocks.** We test the effect of different architectural blocks combined with the Mamba block. We focus on the viewpoint that the Mamba block is simply the standard SwiGLU block with an extra conv → SSM path added. This leads to two natural ablations: 

- What if the Mamba block is interleaved with a standard MLP block, instead of stacked homogenously? This can also be interpreted as taking Mamba and removing half of the SSMs. 

30 



<!-- Start of picture text -->
Scaling Laws on The Pile (Sequence Length 2048) Scaling Laws on The Pile (Sequence Length 2048)<br>Mamba Hyena<br>Mamba-MLP Hyena+<br>Mamba-MHA H3+<br>10 1 H3++<br>9 �10 0<br>10 1<br>8 �10 0<br>7 �10 0<br>10 19 10 20 10 19 10 20<br>FLOPs (log scale) FLOPs (log scale)<br>Perplexity (log scale) Perplexity (log scale)<br><!-- End of picture text -->

Figure 9: ( **Scaling laws: extra ablations** .) ( _Left_ ) Instead of ( _Right_ ) Instead of 

- What if the Mamba block is interleaved with MHA (multi-head attention) blocks? This can also be interpreted as taking a Transformer with SwiGLU MLPs (i.e. what we call Transformer++) and simply adding SSMs to the MLP blocks.

---

[referencia=5dd64e15cc7592b1 score=0.528]
Figure 10 shows that the change from S4 → S6 (i.e. the selection mechanism) is not always beneficial. On long-form audio waveforms, it in fact significantly hampers performance, which may be intuitive from the point of view that audio 

34 



<!-- Start of picture text -->
Audio Waveforms - SSM Parameterization Audio Waveforms - SSM Parameterization<br>1.50 S4+MLP Mamba (S6)<br>Mamba (S6) 1.45 +complex<br>1.45 +complex -selective B/C<br>-selective B/C 1.40 -selective<br>1.40 -selective     (Mamba-S4)<br>   (Mamba-S4) 1.35<br>1.35<br>1.30<br>1.30<br>1.25 1.25<br>10 4 10 5 10 4 10 5<br>Sequence Length Sequence Length<br>Bits Per Byte Bits Per Byte<br><!-- End of picture text -->

Figure 10: ( **Audio Pretraining (YouTubeMix) Ablations** .) As a uniformly-sampled “continuous” signal modality, audio waveforms actually benefit from LTI models which have matching inductive bias. ( _Left_ ) Homogenous models (all blocks have the same parameterization) ( _Right_ ) Only the center U-Net blocks are ablated; the outer blocks are Mamba-S4. Purple line is same as figure on left. 

is uniformly sampled and very smooth, and therefore benefits from continuous linear time-invariant (LTI) methods. After ablating away the selection mechanism, note that the resulting model is the S4 layer inside the Mamba block. To disambiguate, we call this Mamba-S4 as opposed the default Mamba architecture Mamba-S6. 

However, on the right side, we keep the outer layers of the U-Net Mamba-S4 and ablate only the inner layers. The performance differences shrink dramatically; this reinforces the hypothesis that layers closer to the _raw_ audio signal should be LTI, but once they are “tokenized” and compressed by the outer layers, the inner layers no longer need to be LTI. In this setting however, the real-valued SSM still underperforms the complex-valued one.