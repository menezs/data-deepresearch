[referencia=acf32742b39c0b77 score=0.991]
## RWKV-4-Raven-14B 

## **Summarize the following paragraph.** 

## **<The Abstract of this paper goes here>** 

The paper presents a novel architecture, Receptance Weighted Key Value (RWKV), that combines the efficient parallelizable training of Transformers with the efficient inference of RNNs. The model is able to scale to tens of billions of parameters and exhibits linear computational complexity during training and inference, making it a promising alternative to Transformers for sequence processing tasks. 

## **Please further summarize it in one sentence.** 

The researchers have developed a new architecture that combines the efficient parallelizable training of Transformers with the efficient inference of RNNs, which allows for linear scaling in memory and computational requirements.

---

[referencia=acf32742b39c0b77 score=0.981]
# **8 Conclusions** 

We introduced RWKV, a new approach to RNN models exploiting the potential of time-based mixing components. RWKV introduces several key strategies that allow it to capture locality and longrange dependencies while addressing limitations of current architectures by: (1) replacing the quadratic QK attention with a scalar formulation at linear 

cost, (2) reformulating recurrence and sequential inductive biases to enable efficient training parallelization and efficient inference, and (3) enhancing training dynamics using custom initializations. 

We benchmark the proposed architecture in a wide variety of NLP tasks and show comparable performance to SoTA with reduced cost. Further experiments on expressivity, interpretability, and scaling showcase the model capabilities and draw parallels in behavior between RWKV and other LLMs. 

RWKV opens a new route for scalable and efficient architectures to model complex relationships in sequential data. While many alternatives to Transformers have been proposed with similar claims, ours is the first to back up those claims with pretrained models with tens of billions of parameters. 

# **9 Limitations** 

While our proposed RWKV model has demonstrated promising results regarding training and memory efficiency during inference, some limitations should be acknowledged and addressed in future work. 

First, the linear attention of RWKV leads to significant efficiency gains but still, it may also limit the model’s performance on tasks that require recalling minutiae information over very long contexts. This is due to the funneling of information through a single vector representation over many time steps, compared with the full information maintained by the quadratic attention of standard Transformers. In other words, the model’s recurrent architecture inherently limits its ability to “look back” at previous tokens, as opposed to traditional self-attention mechanisms. While learned time decay helps prevent the loss of information, it is mechanistically limited compared to full selfattention. 

Another limitation of this work is the increased importance of prompt engineering in comparison to standard Transformer models. The linear attention mechanism used in RWKV limits the information from the prompt that will be carried over to the model’s continuation. As a result, carefully designed prompts may be even more crucial for the model to perform well on tasks. 

The above RWKV property was confirmed by studies on prompt engineering presented in Appendix L. By changing the order of the information 

pieces, we were even able to almost double the RWKV performance for some tasks.

---

[referencia=acf32742b39c0b77 score=0.974]
Table 4: Evaluation on Long Range Arena. Other models reported in the literature (Gu et al., 2022; Alam et al., 2023). **Bolded** values are the best. 

MODEL LISTOPS TEXT RETRIEVAL IMAGE PATHFINDER PATH-X AVG Transformer 36.37 64.27 57.46 42.44 71.40 ✗ 53.66 Reformer 37.27 56.10 53.40 38.07 68.50 ✗ 50.56 BigBird 36.05 64.02 59.29 40.83 74.87 ✗ 54.17 Linear Trans. 16.13 65.90 53.09 42.34 75.30 ✗ 50.46 Performer 18.01 65.40 53.82 42.77 77.05 ✗ 51.18 FNet 35.33 65.11 59.61 38.67 77.80 ✗ 54.42 Nyströmformer 37.15 65.52 79.56 41.58 70.94 ✗ 57.46 Luna-256 37.25 64.57 79.29 47.38 77.72 ✗ 59.37 Hrrformer 39.98 65.38 76.15 50.45 72.17 ✗ 60.83 S4 **59.60 86.82 90.90 88.65 94.20 96.35 86.09** RWKV 55.88 86.04 88.34 70.53 58.42 ✗ 72.07 

The results show that RWKV performs second only to the S4 model in five datasets. While RWKV substantially underpreforms S4 on Image, Pathfinder, and Path-X, on the problems related to natural language and computer code processing RWKV performs on par with S4 or nearly so.

---

[referencia=acf32742b39c0b77 score=0.967]
LLaMA (Touvron et al., 2023), and Chinchilla (Hoffmann et al., 2022) showcase the potential of Transformers in NLP. However, the self-attention mechanism’s quadratic complexity makes it computationally and memory intensive for tasks involving long sequences and constrained resources. This has stimulated research to enhance Transformers’ scalability, sometimes sacrificing some of their effectiveness (Wang et al., 2020; Zaheer et al., 2020; Dao et al., 2022a). 

To tackle these challenges, we introduce the Receptance Weighted Key Value ( **RWKV** ) model, combining the strengths of RNNs and Transformers while circumventing key drawbacks. RWKV alleviates memory bottleneck and quadratic scaling associated with Transformers (Katharopoulos et al., 2020) with efficient linear scaling, while maintaining the expressive properties of the Transformer, such as parallelized training and robust scalability. RWKV reformulates the attention mechanism with a variant of linear attention, replacing traditional dot-product token interaction with more effective channel-directed attention. This implementation, _without approximation_ , offers the lowest computational and memory complexity; see Table 1. 

The motivation behind RWKV is to balance computational efficiency with expressive capacity in neural networks. It offers a solution for handling large-scale models with billions of parameters, exhibiting competitive performance at a reduced computational cost. Experiments suggest RWKV addresses scaling and deployment challenges in AI, especially for sequential data processing, pointing towards more sustainable and efficient AI models. 

Our contributions in this paper are as follows: 

- The introduction of RWKV, a novel architec- 

- ture combining RNNs and Transformer advantages while mitigating their limitations. 

- Detailed experiments demonstrating RWKV’s performance and efficiency on benchmark datasets for large-scale models. 

- The release of pretrained models, from 169 million to 14 billion parameters, trained on the Pile (Gao et al., 2020; Biderman et al., 2022).<sup>2</sup>

---

[referencia=acf32742b39c0b77 score=0.965]
for next-token prediction and computation of the cross-entropy loss during training. 



<!-- Start of picture text -->
plications and point-wise operations, are already<br>4 Trained Models and Computing Costs<br>inherently parallelizable and efficient.<br>To demonstrate the scalability of RWKV, we train<br>Small Init Embedding During the initial stage<br>of training a transformer model (Vaswani et al., six models ranging from 169 million to 14 billion<br>2017), we observe that the embedding matrix un- parameters as shown in Table 2. All models are<br>trained for one epoch (330 billion tokens) on the<br>dergoes slow changes, presenting a challenge for<br>Pile (Gao et al., 2020; Biderman et al., 2022).<br>the model to move away from its initial noisy em-<br>bedding state. To address this issue, we propose<br>an approach that involves initializing the embed- Name Layers Model Dimension Parameters FLOP per token<br>ding matrix with small values and subsequently 169 M 12 768 1 . 693  ×  10 8 2 . 613  ×  10 8<br>430 M 24 1024 4 . 304  ×  10 8 7 . 573  ×  10 8<br>applying an additional LayerNorm operation. This 1 . 5 B 24 2048 1 . 515  ×  10 9 2 . 823  ×  10 9<br>accelerates and stabilizes the training process, al- 3 B 32 2560 2 . 985  ×  10 9 5 . 710  ×  10 9<br>7 B 32 4096 7 . 393  ×  10 9 1 . 437  ×  10 10<br>lowing for the training of deep architectures with 14 B 40 5120 1 . 415  ×  10 10 2 . 778  ×  10 10<br>post-LN components. The effectiveness of this<br>approach is demonstrated in Figure 9, illustrating 9, illustrating, illustrating Table 2: RWKV model architectures and FLOP counts.<br><!-- End of picture text -->

---

[referencia=acf32742b39c0b77 score=0.964]
## **5.1 NLP Evaluations** 

To demonstrate that RWKV is competitive with traditional transformers at NLP tasks, we compare with similarly sized models trained for a similar number of tokens (Pythia (Biderman et al., 2023b), OPT (Zhang et al., 2022) and BLOOM (Scao et al., 2022)). All RWKV models were trained for one epoch on the Pile (330B tokens), which is close but not identical to the amount of tokens the Pythia, OPT, and BLOOM models were trained for. Consequently, we compare our models on a _FLOPmatched basis_ . We avoid comparing with model trained in the Chinchilla-optimal regime (Hoffmann et al., 2022) or the overtrained regime (Touvron et al., 2023) to ensure the most equitable comparison. 

We report results on ARC (both Easy and Challenge) (Clark et al., 2018), BoolQ (Clark et al., 2019), COPA (Roemmele et al., 2018), HeadQA (Vilares and Gómez-Rodríguez, 2019), HellaSwag (Zellers et al., 2019), LAMBADA (Paperno et al., 2016), OpenBookQA (Mihaylov et al., 2018), PIQA (Bisk et al., 2020), ReCoRD (Zhang et al., 2018), SciQ (Johannes Welbl Nelson F. Liu, 2017), and Winogrande (Zellers et al., 2020). Figure 1 shows the average results across all benchmarks. Some individual benchmarks are shown in Fig 5, with the rest in Appendix J. 

Additionally, we carried out comparative studies on RWKV and ChatGPT / GPT-4, see Appendix L. They revealed that RWKV is very sensitive to prompt engineering. When the prompts were adjusted (re-ordered) from the ones used for GPT to more suitable for RWKV, the performance (F1) increased even from 44.2% to 74.8%. For sarcasm detection, RWKV outperformed ChatGPT, but was still slightly worse than the SOTA solution.

---

[referencia=acf32742b39c0b77 score=0.961]
Transformers have revolutionized almost all 

natural language processing (NLP) tasks but 

graphs (Brown et al., 2020; Ismail Fawaz et al., 

suffer from memory and computational com2019; Wu et al., 2020; Albalak et al., 2022). Preplexity that scales quadratically with sequence dominant among these techniques include RNNs length. In contrast, recurrent neural networks and Transformers (Vaswani et al., 2017), each with (RNNs) exhibit linear scaling in memory and computational requirements but struggle to specific benefits and drawbacks. RNNs require less match the same performance as Transformers memory, particularly for handling long sequences. due to limitations in parallelization and scalaHowever, they suffer from the vanishing gradient bility. We propose a novel model architecture, problem and non-parallelizability in the time diReceptance Weighted Key Value (RWKV), that mension during training, limiting their scalability combines the efficient parallelizable training (Hochreiter, 1998; Le and Zuidema, 2016). of transformers with the efficient inference of RNNs. 



Our approach leverages a linear attention mechanism and allows us to formulate the model as 55 

either a Transformer or an RNN, thus paralleliz- 

ing computations during training and maintains 

50 45 40 

constant computational and memory complex- 

ity during inference. We scale our models as 

large as 14 billion parameters, by far the largest dense RNN ever trained, and find RWKV performs on par with similarly sized Transformers, suggesting future work can leverage this architecture to create more efficient models. This work presents a significant step towards reconciling trade-offs between computational efficiency and model performance in sequence processing tasks.<sup>1</sup> 

BLOOM Pythia OPT RWKV 10<sup>2</sup> 10<sup>3</sup> Compute (exaFLOP) 

Figure 1: Average performance of RWKV models compared to transformers across twelve NLP tasks. For further details, see section 5. 

**1 Introduction** 

Deep learning has greatly advanced artificial intelligence, impacting a range of scientific and industrial uses. These often involve complex sequential data

---

[referencia=acf32742b39c0b77 score=0.942]
# **6 Inference Experiments** 



<!-- Start of picture text -->
7B 8k<br>14B 8k<br>2 2<br>2 1<br>2 1 2 3 2 5 2 7 2 9 2 11<br>Context Length<br>Pile test loss<br><!-- End of picture text -->

Figure 6: RWKV shows decreasing mean test loss as a function of context length on the Pile (Gao et al., 2020) 

We benchmark inference requirements according to size and family. Specifically, we evaluate text generation speed and memory requirements on typical compute platforms including CPU (x86) and GPU (NVIDIA A100 80 GB). For all of our inference experiments we use float32 precision and the HuggingFace Transformers (Wolf et al., 2020). We include all model parameters in the parameter count, including both embedding and non-embedding layers. Performance under different quantization setups is left to further work. See Appendix K for 

more results. 



Figure 7: Cumulative time on text generation for LLMs. Unlike transformers, RWKV exhibits linear scaling. 

# **7 Future Work** 

There are several promising directions for future work on the RWKV architecture. Work can be done to increase model expressivity by enhancing the time-decay formulations and exploring initial model states while maintaining efficiency. 

The RWKV computational efficiency can be further improved by applying a parallel scan in the _wkvt_ step to reduce the computational cost to _O_ ( _B_ log( _T_ ) _d_ ). 

The mechanisms used in RWKV can be applied to encoder-decoder architectures, potentially replacing the cross-attention mechanism. This could be applicable in seq2seq or multimodal settings, thereby enhancing efficiency during both training and inference. 

RWKV’s state (or _context_ ) can be leveraged for interpretability, predictability in sequence data, and safety. Manipulating the hidden state could also guide behavior and allow greater customizability through prompt tuning. 

The RWKV architecture is not perfect, and can be improved via many aspects, such as modifying the formulae or implementing larger internal states. Larger states can enhance the model’s memory to previous context and improve performance over various tasks.

---

[referencia=acf32742b39c0b77 score=0.936]
# **2 Background** 

Here we briefly review the fundamentals of RNNs and Transformers. 

## **2.1 Recurrent Neural Networks (RNNs)** 

Popular RNN architectures such as LSTM (Hochreiter and Schmidhuber, 1997) and GRU (Chung et al., 2014) are characterized by the following formulation (shown for LSTM, others can be reasoned similarly): 



Although RNNs can be factored into two linear blocks ( _W_ and _U_ ) and an RNN-specific block (1)– (6), as noted by Bradbury et al. (2017), the data dependency relying on previous time steps prohibits parallelizing these typical RNNs. 

## **2.2 Transformers and AFT** 

Introduced by Vaswani et al. (2017), Transformers are a class of neural networks that have become the dominant architecture for several NLP tasks. Instead of operating on sequences step-by-step like RNNs, Transformers rely on attention mechanisms to capture relationships between all input and all output tokens: 



where the multi-headness and scaling factor _~~√~~_ <u>1</u> _dk_<sup>is</sup> omitted for convenience. The core _QK_<sup>_⊤_</sup> multiplication is an ensemble of pairwise attention scores 

2https://huggingface.co/RWKV 

between each token in a sequence, which can be decomposed as vector operations: 



AFT (Zhai et al., 2021), alternately formulates 



where _{wt,i} ∈ R_<sup>_T×T_</sup> is the learned pair-wise position biases, and each _wt,i_ is a scalar. 

Inspired by AFT, RWKV takes a similar approach. However, for simplicity, it modifies the interaction weights so that it can be transformed into an RNN. Each _w_ in RWKV is a channel- _t,i_ wise time decay vector multiplied by the relative position and traced backward from current time as it decays: 



where _w ∈_ ( _R≥_ 0)<sup>_d_</sup> , with _d_ the number of channels. We require _w_ to be non-negative to ensure that _e_<sup>_wt,i_</sup> _≤_ 1 and the per-channel weights decay backwards in time.

---

[referencia=acf32742b39c0b77 score=0.931]
**Rui-Jie Zhu** Tables 1 and 5. Experiments for table 5. **C Additional Related Work** 

Recently, a number of techniques have been proposed to address the limitations of transformers. **Optimizing Attention Mechanism** Many transformer variants (“x-formers”) have been introduced to reduce the complexity of transformers (Tay et al., 2022), including sparse attention (Beltagy et al., 2020; Kitaev et al., 2020; Guo et al., 2022), approximating the full attention matrix (Wang et al., 2020; Ma et al., 2021; Choromanski et al., 2020), combining chunked attention with gating (Ma et al., 2023) and other efficient methods (Katharopoulos et al., 2020; Jaegle et al., 2021). 

Some recent works like FlashAttention (Dao et al., 2022a) and others (Rabe and Staats, 2022; Jang et al., 2019) share similarities with RWKV’s chunked computation scheme. Despite being memory-efficient, their time complexity remains quadratic or contains chunk size as a hidden factor. In contrast, RWKV achieves better space and time complexity during inference by formulating a linear attention as an RNN. **Attention Free Models** Another line of research replaces the attention mechanism with other modules to scale to long sequences. MLP-Mixer and others (Tolstikhin et al., 2021; Liu et al., 2021) propose replacing

---

[referencia=acf32742b39c0b77 score=0.931]
**1 Introduction** 

Deep learning has greatly advanced artificial intelligence, impacting a range of scientific and industrial uses. These often involve complex sequential data 

Transformers emerged as a powerful alternative, adept at managing local and long-range dependencies and supporting parallelized training (Tay et al., 2022). Models such as GPT-3 (Brown et al., 2020), ChatGPT (OpenAI, 2022; Koco´n et al., 2023), 

> _∗_ Equal first authorship. Others listed alphabetically. 

> 1Code at: https://github.com/BlinkDL/RWKV-LM 

|**Model**|**Time**|**Space**|
|---|---|---|
|Transformer|_O_(_T_ <sup>2</sup>_d_)|_O_(_T_ <sup>2 </sup>+_Td_)|
|Reformer|_O_(_T_ log_Td_)|_O_(_T_ log_T_ +_Td_)|
|Performer|_O_(_Td_<sup>2 </sup>log_d_) <br>|_O_(_Td_log_d_+_d_<sup>2 </sup>log_d_)<br>|
|Linear Transformers|_O_(_Td_<sup>2</sup>)<br>|_O_(_Td_+_d_<sup>2</sup>)|
|AFT-full|_O_(_T_ <sup>2</sup>_d_)|_O_(_Td_)|
|AFT-local|_O_(_Tsd_)|_O_(_Td_)|
|MEGA|_O_(_cTd_)|_O_(_cd_)|
|RWKV (ours)|_O_(**Td**)|_O_(**d**)|



Table 1: Inference complexity comparison with different Transformers. Here _T_ denotes the sequence length, _d_ the feature dimension, _c_ is MEGA’s chunk size of quadratic attention, and _s_ is the size of a local window for AFT.

---

[referencia=acf32742b39c0b77 score=0.917]
# **10 Ethics Statement** 

In this paper, we present a novel architecture for sequential data processing and prove its effectiveness by building a series of LLMs trained on publicly released pretraining data (Gao et al., 2020; Biderman et al., 2022) and later fine-tuned on publicly available instructions (Taori et al., 2023; Chaudhary, 2023; Cheung, 2023; Anand et al., 2023; Anonymous, 2023; Yang, 2023; Ji et al., 2023a,b). 

As a novel architecture for sequential data, RWKV has the potential to improve sequencebased models across different applications ranging from natural language processing to biomedical data processing or climate modelling. Since the training code is released open source, RWKV contributes to the democratization of AI, levels the playing field, and empowers members of the Open Source community to inspect, study, and finetune RWKV in particular tasks. Moreover, it contributes to advancing the understanding of LLMs capabilities and limitations. A significant amount of work has been devoted to increasing the efficiency of RWKV training so as to minimize its cost and promote accessibility. 

As LLMs trained on public data, RWKV’s lower inference cost compared to Transformer alternatives makes it more suitable for deployment in consumer and edge hardware, which is a step towards the democratization and distribution of LLMs to the general public, creating better privacy and ownership incentives. It also lowers the resource barrier to Chat assistants and text generation for small and/or underrepresented communities. PreTrained model weights for different sizes ranging from 0.1B to 14B parameters trained on multiple languages are released to increase ease of adoption and allow for the study of emergent phenomena. 

On the other hand, with lower resource barriers, the spreading of AI-generated text might become more prevalent. Current RWKV LLMs may exhibit and/or reproduce biases and potentially harmful content present in the data used for training. Nonetheless, mitigation and finetuning strategies discussed for other, large Transformer models should be applicable to RWKV as well. 

# **Acknowledgements** 

We thank StabilityAI for the compute used to train our models and for technical support in development of RWKV. We also thank the members of the RWKV and EleutherAI Discord servers for their help and work on further extending the applicability of RWKV to different domains.

---

[referencia=acf32742b39c0b77 score=0.891]
# **B Author Contributions** 

**Bo Peng** Original RWKV idea, original code, performance optimizations, original experiments, and trained RWKV models from 0.1B to 14B. 

**Eric Alcaide** Manuscript (initial draft sections 1, C; sections 3, 7 and 8; revision and proofreading; final version ). Figures (2, 3, 3, 8). Experiments section 6. Appendices E, K. Contributions to Appendix M. 

**Quentin Anthony** Manuscript (organization, initial draft sections 1, C, 2; revision and proofreading; final version). 

**Alon Albalak** Manuscript (abstract and sections 1, 9, and 7; proofreading and revision). **Samuel Arcadinho** Contributions to Figures 7, 13, and 14. Contributions to Appendix K. 

**Stella Biderman** Performed the scaling laws analysis and evaluated competitor models on benchmark tasks. 

**Huanqi Cao** Manuscript (contributions to 3.2 and 3.3; proofreading and revision). Experiments for Appendix I. 

**Xin Cheng** Manuscript (proofreading and revision). Contributions to Appendix M, J. 

**Michael Chung** Manuscript (contributions to section I; proofreading and revision). 

**Xingjian Du** Evaluation on Long Range Arena Benchmark (TBD until 5.31). 

**Matteo Grella** Manuscript (sections H, I, 8; contributions to sections 1, 7 and 9; proofreading and revision). Contributions to Appendix D. 

**Kranthi Kiran GV** Manuscript (sections C and 5; contributions to section 2; revision and proofreading). Tables K and K. Appendix 4. 

**Xuzheng He** Manuscript (contributions to section 2; proofreading and revision). Contributions to Figure8. Appendix I. Contributions to appendix H. 

**Haowen Hou** Figure 9. Appendix F. 

**Jiaju Lin** RWKV on LRA benchmarking 

**Przemysław Kazienko** Manuscript (proofreading and revision). Contributions to Section 6, 9, and Appendix L. 

**Jan Kocon** Manuscript (Section 1; proofreading and revision). Contributions to Appendix L.

---

[referencia=acf32742b39c0b77 score=0.846]
# **5 Evaluations** 

Having demonstrated the scalability of RWKV models in the previous section, we now turn our attention to their competitiveness with traditional transformers. We focus on two questions: 

**Competitiveness** Is RWKV competitive against quadratic transformer architectures with the same amount of compute? 

**Long Context** Does increasing the context length of RWKV yield better language modeling loss when RWKV models are trained for context lengths that most open-sourced quadratic transformers _cannot_ efficiently process?

---

[referencia=acf32742b39c0b77 score=0.833]
approach is demonstrated in Figure 9, illustrating 9, illustrating, illustrating Table 2: RWKV model architectures and FLOP counts.<br>improved convergence by enabling the model to Further details of these hyperparameters are elaborated<br>upon in Appendix G.<br>quickly transition away from the initially small em-<br>bedding. This is achieved through small changes<br>occurring in a single step, which subsequently lead The number of parameters for each model is<br>to substantial alterations in directions and further computed using the formula: # parameters =<br>notable changes after the LayerNorm operation. 2 V D  + 13 D 2 L  +  D (11 L  + 4) where  V = 50277<br>is the vocabulary size,  D  represents the Model Di-<br>Custom Initialization Building on principles mension and  L  corresponds to the number of lay-<br>from previous works (He et al., 2016; Jumper et al., ers. FLOPs is for a forward pass for one token. It<br>2021), we adopt an initialization strategy where was calculated as 2(2 V D  + 13 D 2 L ), which is the<br>parameters are set to values resembling an identity<br>twice (add and multiply) the number of parameters<br>mapping while breaking symmetry to establish a<br>in linear layers. The backwards pass FLOPs can<br>clear information flow. The majority of weights are<br>be approximated as twice that of the forward pass,<br>initialized to zero, and linear layers do not employ giving a total of 6(2 V D  + 13 D 2 L ) FLOP per to-<br>biases. Detailed formulas are given in Appendix E. ken. Notably, this matches the standard formula<br>We observe that the choice of initialization plays a for FLOP calculations in transformers Kaplan et al.<br>crucial role in both the speed and quality of conver- (2020): FLOP = 6  ·  [# tokens]  ·  [# parameters].<br>gence (refer to Appendix F for further details).<br>3.5 Implementation 4.1 Additional Training Details<br>RWKV is implemented using the PyTorch Deep For training, we use the standard Adam optimizer<br>

---

[referencia=acf32742b39c0b77 score=0.804]
.<br>gence (refer to Appendix F for further details).<br>3.5 Implementation 4.1 Additional Training Details<br>RWKV is implemented using the PyTorch Deep For training, we use the standard Adam optimizer<br>Learning Library (Paszke et al., 2019). We inte- without weight decay, use bfloat16 precision, and<br>grate additional optimization strategies inspired by train with a context length of 1024 tokens. Fur-<br>DeepSpeed (Rasley et al., 2020) into the system, ther details on hyperparameters are in Appendix G.<br>improving its efficiency and scalability. Diverting from standard practice for transformers,<br>The model begins with an embedding layer, as we apply exponential decay to our learning rate.<br>detailed in Section 3.4. Following this are sev- We also incorporate the auxiliary loss introduced<br>eral identical residual blocks arranged sequentially. by PaLM (Chowdhery et al., 2022), supplement-<br>These are depicted in Figures 2 and 3 and adheres ing the standard cross-entropy loss function. This<br><!-- End of picture text -->

to the principles outlined in Section 3.1.1. After the last block, a simple output projection head, consisting of a LayerNorm (Ba et al., 2016) and a linear projection, is employed for logits generation 

auxiliary loss encourages the softmax normalizer to approximate zero closely. As for the learning rate schedule, it remains constant for the initial iterations, and subsequently decays exponentially.

---

[referencia=acf32742b39c0b77 score=0.781]
## **3.1.3 Output Gating** 

Output gating is implemented in both time-mixing and channel-mixing blocks using the sigmoid of 

the receptance, _σ_ ( _r_ ). The output vector _ot_ post the _WKV_ operator is given by: 



In the channel-mixing block, a similar operation is performed: 



where we adopt the squared ReLU activation function (So et al., 2021). 

## **3.2 Transformer-like Training** 

RWKV can be efficiently parallelized using a technique called _time-parallel mode_ , reminiscent of Transformers. The time complexity of processing a batch of sequences in a single layer is _O_ ( _BTd_<sup>2</sup> ), primarily consisting of matrix multiplications _Wλ_ , where _λ ∈{r, k, v, o}_ (assuming _B_ sequences, _T_ maximum tokens, and _d_ channels). In contrast, updating attention scores _wkvt_ involves a serial scan (see Appendix D for more detail) and has complexity _O_ ( _BTd_ ). 

The matrix multiplications can be parallelized similarly to _Wλ_ , where _λ ∈{Q, K, V, O}_ in conventional Transformers. The element-wise _WKV_ computation is time-dependent but can be readily parallelized along the other two dimensions (Lei et al., 2018)<sup>3</sup> . 

## **3.3 RNN-like Inference** 

Recurrent networks commonly utilize the output at state _t_ as input at state _t_ + 1. This usage is also observed in the autoregressive decoding inference of language models, where each token must be computed before being passed to the next step. RWKV takes advantage of this RNN-like structure, known as _time-sequential mode_ . In this context, RWKV can be conveniently formulated recursively for decoding during inference, as demonstrated in Appendix D.

---

[referencia=acf32742b39c0b77 score=0.745]
# **3 RWKV** 

The RWKV model architecture is defined by four fundamental elements that are intrinsic to the timemixing and channel-mixing blocks: 

- _R_ : The **Receptance** vector acts as the receiver of past information. 

- _W_ : The **Weight** signifies the positional weight decay vector, a trainable parameter within the model. 

- _K_ : The **Key** vector performs a role analogous to _K_ in traditional attention mechanisms. 

- _V_ : The **Value** vector functions similarly to _V_ in conventional attention processes. 

These core elements interact multiplicatively at each timestep, as depicted in Figure 2. 

## **3.1 Architecture** 

The RWKV model is composed of stacked residual blocks. Each block consists of a time-mixing and a channel-mixing sub-block, embodying recurrent structures to leverage past information. 

This model uses a unique attention-like score update process, which includes a time-dependent 



<!-- Start of picture text -->
Output Probabilities<br>Channel  Softmax<br>Mixing<br>? V' Out<br>R' K' LayerNorm<br>?'<br>LayerNorm<br>Channel Mixing<br>Time  Out<br>Mixing<br>LayerNorm<br>? WKV<br>R K V<br>Time Mixing<br>?<br>LayerNorm LayerNorm<br>LayerNorm<br>Input<br>Embedding<br><!-- End of picture text -->

Figure 2: Elements within an RWKV block (left) and the complete RWKV residual block, equipped with a final head for language modeling (right). 

softmax operation improving numerical stability and mitigating vanishing gradients (for rigorous proof, see Appendix H). It ensures that the gradient is propagated along the most relevant path. Additionally, layer normalization (Ba et al., 2016) incorporated within the architecture aids in stabilizing the gradients, effectively addressing both vanishing and exploding gradient issues. These design elements not only enhance the training dynamics of deep neural networks but also facilitate the stacking of multiple layers, leading to superior performance over conventional RNN models by capturing complex patterns across different levels of abstraction (see also Appendix I).

---

[referencia=acf32742b39c0b77 score=0.687]
Figure 13: Text generation inference memory (CPU RAM, GPU VRAM) for LLMs. Model parameters are not accounted. 



Figure 14: Text generation inference time for LLMs. 

|Task Name|Measure|ChatGPT|GPT-4|RWKV-GPT|RWKV-adapted|SOTA|
|---|---|---|---|---|---|---|
|RTE|F1 Macro|88.1|**91.3**|44.2|74.8|92.1|
|WNLI|Accuracy|81.7|**91.6**|47.9|49.3|97.9|
|GoEmotions|F1 Macro|**25.6**|23.1|7.9|7.9|52.8|
|PolEmo2|F1 Macro|**44.1**|41.0|38.2|40.9|76.4|



Table 6: ChatGPT, GPT-4 and RWKV-4-Raven-14B reasoning performance comparison in RTE (Wang et al., 2019), WNLI (Wang et al., 2018), GoEmotions (Demszky et al., 2020), and PolEmo2 (Koco´n et al., 2019) benchmarks. RWKV GPT prompts were primarily used for ChatGPT in (Koco´n et al., 2023). SOTA is provided as a supplementary reference. 

|Task Name|Measure|ChatGPT|RWKV-adapted|SOTA|
|---|---|---|---|---|
|Aggression|F1 Macro|**69.10**|56.66|74.45|
|MathQA|Accuracy|**71.40**|5.43|83.20|
|Sarcasm|F1 Macro|49.88|**50.96**|53.57|
|TweetSent|F1 Macro|**63.32**|52.50|72.07|
|Unhealthy|F1 Macro|**45.21**|43.30|50.96|

---

[referencia=acf32742b39c0b77 score=0.686]
## **4.2 Scaling Laws** 

Scaling laws (Kaplan et al., 2020; Henighan et al., 2020; Hoffmann et al., 2022; Muennighoff et al., 2023) in language models refer to the mathematical relationships that describe how the performance of a language model changes with respect to various factors. These factors can include the model size ( _N_ ), dataset size ( _D_ ), or the optimally allocated compute budget ( _C_ min). Scaling laws are important for two primary reasons: they allow us to make predictions and plans regarding the costs and performance of large models before they are trained via interpolation and extrapolation (Black et al., 2022; Le Scao et al., 2022) and the contexts in which they fail provides rich feedback on important areas for future research (Wei et al., 2022a; Biderman et al., 2023a). 

Previous work on scaling laws for RNNs has claimed that LSTMs do not strictly follow the same log-log linear scaling that transformers do (Kaplan et al., 2020). We train 45 RWKV models for a variety of pairs (dataset, parameters) and find that RWKV _does_ follow the same general form of the scaling law that is well established for transformers. Figure 4 shows our results for loss as a function of compute, with the linear fit to the Pareto optimal points holding an _r_<sup>2</sup> value of 0 _._ 994. Even when we extrapolate our curve an additional order of magnitude (blue), we find an extremely good fit with an _r_<sup>2</sup> of 0 _._ 875. 



<!-- Start of picture text -->
Non-Optimal<br>Optimal<br>Test<br>Trend Line<br>3 × 10 0<br>2 × 10 0<br>10 1 10 0 10 1 10 2 10 3<br>Compute (exaFLOP)<br>Loss<br><!-- End of picture text -->

Figure 4: Scaling laws curves for RWKV models