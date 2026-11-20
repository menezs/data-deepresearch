[referencia=83213326f5835ccc score=0.923]
In this paper, we introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. Specifically, RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Note that the proposed RoPE is prioritized over the existing methods through valuable properties, including the sequence length flexibility, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Experimental results on various long text classification benchmark datasets show that the enhanced transformer with rotary position embedding, namely RoFormer, can give better performance compared to baseline alternatives and thus demonstrates the efficacy of the proposed RoPE. 

In brief, our contributions are three-folds as follows: 

- We investigated the existing approaches to the relative position encoding and found that they are mostly built based on the idea of the decomposition of adding position encoding to the context representations. We introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. The key idea is to encode relative position by multiplying the context representations with a rotation matrix with a clear theoretical interpretation. 

- We study the properties of RoPE and show that it decays with the relative distance increased, which is desired for natural language encoding. We kindly argue that previous relative position encoding-based approaches are not compatible with linear self-attention. 

- We evaluate the proposed RoFormer on various long text benchmark datasets. Our experiments show that it consistently achieves better performance compared to its alternatives. Some experiments with pre-trained language models are available on GitHub: `https://github.com/ZhuiyiTechnology/roformer` . 

The remaining of the paper is organized as follows. We establish a formal description of the position encoding problem in self-attention architecture and revisit previous works in Section **(2)** . We then describe the rotary position encoding (RoPE) and study its properties in Section **(3)** . We report experiments in Section **(4)** . Finally, we conclude this paper in Section **(5)** .

---

[referencia=83213326f5835ccc score=0.913]
### **4.5.5 Limitations of the work** 

Although we provide theoretical groundings as well as promising experimental justifications, our method is limited by following facts: 

- Despite the fact that we mathematically format the relative position relations as rotations under 2D sub-spaces, there lacks of thorough explanations on why it converges faster than baseline models that incorporates other position encoding strategies. 

- Although we have proved that our model has favourable property of long-term decay for intern-token products, Section **(3.3)** , which is similar to the existing position encoding mechanisms, our model shows superior performance on long texts than peer models, we have not come up with a faithful explanation. 

Our proposed RoFormer is built upon the Transformer-based infrastructure, which requires hardware resources for pre-training purpose. 

## **5 Conclusions** 

In this work, we proposed a new position embedding method that incorporates explicit relative position dependency in self-attention to enhance the performance of transformer architectures. Our theoretical analysis indicates that relative position can be naturally formulated using vector production in self-attention, with absolution position information being encoded through a rotation matrix. In addition, we mathematically illustrated the advantageous properties of the proposed method when applied to the Transformer. Finally, experiments on both English and Chinese benchmark datasets demonstrate that our method encourages faster convergence in pre-training. The experimental results also show that our proposed RoFormer can achieve better performance on long texts task.

---

[referencia=83213326f5835ccc score=0.885]
# ROFORMER: ENHANCED TRANSFORMER WITH ROTARY POSITION EMBEDDING 

**Jianlin Su** Zhuiyi Technology Co., Ltd. Shenzhen `bojonesu@wezhuiyi.com` 

**Yu Lu** Zhuiyi Technology Co., Ltd. Shenzhen `julianlu@wezhuiyi.com` 

**Shengfeng Pan** Zhuiyi Technology Co., Ltd. Shenzhen `nickpan@wezhuiyi.com` 

**Ahmed Murtadha** Zhuiyi Technology Co., Ltd. Shenzhen `mengjiayi@wezhuiyi.com` 

**Bo Wen Yunfeng Liu** Zhuiyi Technology Co., Ltd. Zhuiyi Technology Co., Ltd. Shenzhen Shenzhen `brucewen@wezhuiyi.com glenliu@wezhuiyi.com` 

November 9, 2023 

## **ABSTRACT** 

Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: `https://huggingface.co/docs/transformers/model_doc/roformer` . 

**_Keywords_** Pre-trained Language Models _·_ Position Information Encoding _·_ Pre-training _·_ Natural Language Processing.

---

[referencia=83213326f5835ccc score=0.421]
### **3.2.2 General form** 

In order to generalize our results in 2D to any **_x_** _i ∈_ R<sup>_d_</sup> where _d_ is even, we divide the d-dimension space into _d/_ 2 sub-spaces and combine them in the merit of the linearity of the inner product, turning _f{q,k}_ into: 

where 



is the rotary matrix with pre-defined parameters Θ = _{θi_ = 10000<sup>_−_2(</sup><sup>_i−_1)</sup><sup>_/d_</sup> _, i ∈_ [1 _,_ 2 _, ..., d/_ 2] _}_ . A graphic illustration of RoPE is shown in Figure **(1)** . Applying our RoPE to self-attention in Equation (2), we obtain: 



where **_R_**<sup>_d_</sup> Θ _,n−m_<sup>= (</sup><sup>**_R_**</sup><sup>_d_</sup> Θ _,m_<sup>)⊺</sup><sup>**_R_**</sup> Θ<sup>_d_</sup> _,n_<sup>.Note that</sup><sup>**_R_**</sup><sup>_d_</sup> Θ<sup>is an orthogonal matrix, which ensures stability during the process of</sup> encoding position information. In addition, due to the sparsity of _R_ Θ<sup>_d_, applying matrix multiplication directly as in</sup> Equation (16) is not computationally efficient; we provide another realization in theoretical explanation. 

In contrast to the additive nature of position embedding method adopted in the previous works, i.e., Equations (3) to (10), our approach is multiplicative. Moreover, RoPE naturally incorporates relative position information through rotation matrix product instead of altering terms in the expanded formulation of additive position encoding when applied with self-attention. 



<!-- Start of picture text -->

---

[referencia=83213326f5835ccc score=0.414]
where _bi,j_ is a trainable bias. The authors of Ke et al. [2020] investigated the middle two terms of Equation (6) and found little correlations between absolute positions and words. The authors of Raffel et al. [2020] proposed to model a pair of words or positions using different projection matrices. 



3 

RoFormer 

The authors of He et al. [2020] argued that the relative positions of two tokens could only be fully modeled using the middle two terms of Equation (6).replaced with the relative position embeddingsAs a consequence, the absolute position embeddings **_p_** ˜ _m−n_ : **_p_** _m_ and **_p_** _n_ were simply 



A comparison of the four variants of the relative position embeddings Radford and Narasimhan [2018] has shown that the variant similar to Equation (10) is the most efficient among the other three. Generally speaking, all these approaches attempt to modify Equation (6) based on the decomposition of Equation (3) under the self-attention settings in Equation (2), which was originally proposed in Vaswani et al. [2017]. They commonly introduced to directly add the position information to the context representations. Unlikely, our approach aims to derive the relative position encoding from Equation (1) under some constraints. Next, we show that the derived approach is more interpretable by incorporating relative position information with the rotation of context representations.

---

[referencia=83213326f5835ccc score=0.405]
1A stack of multiple CNN layers can also capture longer intra-token relation, here we only consider single layer setting. 

RoFormer 

It is noteworthy that the self-attention architecture of the current PLMs has shown to be position-agnostic Yun et al. [2020]. Following this claim, various approaches have been proposed to encode the position information into the learning process. On one side, generated absolute position encoding through a pre-defined function Vaswani et al. [2017] was added to the contextual representations, while a trainable absolute position encoding Gehring et al. [2017], Devlin et al. [2019], Lan et al. [2020], Clark et al. [2020], Radford et al. [2019], Radford and Narasimhan [2018]. On the other side, the previous work Parikh et al. [2016], Shaw et al. [2018], Huang et al. [2018], Dai et al. [2019], Yang et al. [2019], Raffel et al. [2020], Ke et al. [2020], He et al. [2020], Huang et al. [2020] focuses on relative position encoding, which typically encodes the relative position information into the attention mechanism. In addition to these approaches, the authors of Liu et al. [2020] have proposed to model the dependency of position encoding from the perspective of Neural ODE Chen et al. [2018a], and the authors of Wang et al. [2020] have proposed to model the position information in complex space. Despite the effectiveness of these approaches, they commonly add the position information to the context representation and thus render them unsuitable for the linear self-attention architecture.

---

[referencia=83213326f5835ccc score=0.218]
## **2 Background and Related Work** 

### **2.1 Preliminary** 

Let S _N_ = _{wi}_<sup>_N_</sup> _i_ =1<sup>be a sequence of</sup><sup>_N_input tokens with</sup><sup>_wi_being the</sup><sup>_ith_element.The corresponding word embedding</sup> of S _N_ is denoted as E _N_ = _{_ **_x_** _i}_<sup>_N_</sup> _i_ =1<sup>, where</sup><sup>**_x_**</sup><sup>_i∈_R</sup><sup>_d_is the d-dimensional word embedding vector of token</sup><sup>_wi_without</sup> position information. The self-attention first incorporates position information to the word embeddings and transforms them into queries, keys, and value representations. 



where **_q_** _m,_ **_k_** _n_ and **_v_** _n_ incorporate the _m_<sup>_th_</sup> and _n_<sup>_th_</sup> positions through _fq, fk_ and _fv_ , respectively. The query and key values are then used to compute the attention weights, while the output is computed as the weighted sum over the value 

2 

RoFormer 

representation. 



The existing approaches of transformer-based position encoding mainly focus on choosing a suitable function to form Equation (1).

---

[referencia=83213326f5835ccc score=0.214]
## **3 Proposed approach** 

In this section, we discuss the proposed rotary position embedding (RoPE). We first formulate the relative position encoding problem in Section **(3.1)** , we then derive the RoPE in Section **(3.2)** and investigate its properties in Section **(3.3)** . 

### **3.1 Formulation** 

Transformer-based language modeling usually leverages the position information of individual tokens through a selfattention mechanism. As can be observed in Equation (2), **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n_typically enables knowledge conveyance between</sup> tokens at different positions. In order to incorporate relative position information, we require the inner product of query **_q_** _m_ and key **_k_** _n_ to be formulated by a function _g_ , which takes only the word embeddings **_x_** _m_ , **_x_** _n_ , and their relative position _m − n_ as input variables. In other words, we hope that the inner product encodes position information only in the relative form: 



The ultimate goal is to find an equivalent encoding mechanism to solve the functions _fq_ ( **_x_** _m, m_ ) and _fk_ ( **_x_** _n, n_ ) to conform the aforementioned relation. 

### **3.2 Rotary position embedding**

---

[referencia=83213326f5835ccc score=0.086]
linear attention, we encourage readers to refer to original papers. In this section, we focus on discussing incorporating RoPE with Equation (18). Since RoPE injects position information by rotation, which keeps the norm of hidden representations unchanged, we can combine RoPE with linear attention by multiplying the rotation matrix with the outputs of the non-negative functions. 

   - _N_ ⊺ 

   - Attention( **Q** _,_ **K** _,_ **V** ) _m_ = <u>�</u> _n_ =1 <u>�</u> **_R_** <u>�</u><sup>_d_</sup> Θ _<u>,Nnm</u>_ =1<sup>_ϕ_(</sup><sup>_ϕ_</sup><sup>**_q_**(</sup> _m_<sup>**_q_**)</sup> _m_ <u>�</u><sup>)⊺</sup> <u>�</u> **_R_**<sup>_φ_(</sup><sup>_d_</sup> Θ<sup>**_k_**</sup> _<u>,</u>_<sup>_n_</sup> _n_<sup>)</sup><sup>_φ_(</sup><sup>**_k_**</sup><sup>_n_)</sup> <u>�</u> **_v_** _n ._ (19) 

- It is noteworthy that we keep the denominator unchanged to avoid the risk of dividing zero, and the summation in the numerator could contain negative terms. Although the weights for each value **_v_** _i_ in Equation (19) are not strictly 

probabilistic normalized, we kindly argue that the computation can still model the importance of values. **3.4 Theoretical Explanation**

---

[referencia=83213326f5835ccc score=0.054]
### **2.3 Relative position embedding** 

The authors of Shaw et al. [2018] applied different settings of Equation (1) as following: 



where **_p_** ˜<sup>_k_</sup> _r_<sup>_,_˜</sup><sup>**_p_**</sup> _r_<sup>_v∈_R</sup><sup>_d_are trainable relative position embeddings.Note that</sup><sup>_r_=clip(</sup><sup>_m −n, r_min</sup><sup>_, r_max) represents the</sup> relative distance between position _m_ and _n_ . They clipped the relative distance with the hypothesis that precise relative position information is not useful beyond a certain distance. Keeping the form of Equation (3), the authors Dai et al. [2019] have proposed to decompose **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n_of Equation (2) as</sup> 



˜ the key idea is to replace the absolute position embedding **_p_** _n_ with its sinusoid-encoded relative counterpart **_p_** _m−n_ , while the absolute position **_p_** _m_ in the third and fourth term with two trainable vectors **u** and **v** independent of the query positions. Further, **_W_** _k_ is distinguished for the content-based and location-based key vectors **_x_** _n_ and **_p_** _n_ , denoted as **_W_** _k_ and **_W_**<sup>�</sup> _k_ , resulting in: 



It is noteworthy that the position information in the value term is removed by setting _fv_ ( **_x_** _j_ ) := **_W_** _v_ **_x_** _j_ . Later work Raffel et al. [2020], He et al. [2020], Ke et al. [2020], Huang et al. [2020] followed these settings by only encoding the relative position information into the attention weights. However, the authors of Raffel et al. [2020] reformed Equation (6) as:

---

[referencia=83213326f5835ccc score=0.048]
### **3.2 Rotary position embedding** 

### **3.2.1 A 2D case** 

We begin with a simple case with a dimension _d_ = 2. Under these settings, we make use of the geometric property of vectors on a 2D plane and its complex form to prove (refer Section **(3.4.1)** for more details) that a solution to our formulation Equation (11) is: 



where Re[ _·_ ] is the real part of a complex number and ( **_W_** _k_ **_x_** _n_ )<sup>_∗_</sup> represents the conjugate complex number of ( **_W_** _k_ **_x_** _n_ ). _θ ∈_ R is a preset non-zero constant. We can further write _f{q,k}_ in a multiplication matrix: 



where ( _x_<sup>(1)</sup> _m_<sup>_, x_(2)</sup> _m_<sup>) is</sup><sup>**_x_**</sup> _m_<sup>expressed in the 2D coordinates.Similarly,</sup><sup>_g_can be viewed as a matrix and thus enables the</sup> solution of formulation in Section **(3.1)** under the 2D case. Specifically, incorporating the relative position embedding is straightforward: simply rotate the affine-transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind _Rotary Position Embedding_ . 

4 

RoFormer

---

[referencia=83213326f5835ccc score=0.045]
### **3.3 Properties of RoPE** 

**Long-term decay:** Following Vaswani et al. [2017], we set _θi_ = 10000<sup>_−_2</sup><sup>_i/d_</sup> . One can prove that this setting provides a long-term decay property (refer to Section **(3.4.3)** for more details), which means the inner-product will decay when the relative position increase. This property coincides with the intuition that a pair of tokens with a long relative distance should have less connection. 

**RoPE with linear attention:** The self-attention can be rewritten in a more general form. 

5 

RoFormer 

_N_ Attention( **Q** _,_ **K** _,_ **V** ) _m_ = <u>��</u> _<u>n</u>_ = _Nn_ =11<sup>simsim((</sup><sup>**_<u>qq</u>_**</sup> _mm_<sup>_<u>,</u>_</sup><sup>**_k_**</sup><sup>_,_</sup><sup>**_k_**</sup><sup>_n_</sup><sup><u>)</u></sup><sup>_n_</sup><sup>**_v_**)</sup><sup>_n_</sup> _._ (17) The original self-attention chooses sim( **_q_** _m,_ **_k_** _n_ ) = exp( **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n/_</sup> _√d_ ). Note that the original self-attention should

---

[referencia=83213326f5835ccc score=0.038]
### **4.4.1 Implementation details** 

We carry out tests on the Enwik8 dataset Mahoney [2006], which is from English Wikipedia that includes markup, special characters and text in other languages in addition to English text. We incorporate RoPE into the 12 layer char-based PerFormer with 768 dimensions and 12 heads<sup>2</sup> . To better illustrate the efficacy of RoPE, we report the loss curves of the pre-training process with and without RoPE under the same settings, i.e., learning rate 1e-4, batch size 128 and a fixed maximum sequence length of 1024, etc. 

### **4.4.2 Results** 

As shown on the right plot of Figure **(3)** , substituting RoPE into Performer leads to rapid convergence and lower loss under the same amount of training steps. These improvements, in addition to the linear complexity, make Performer more attractive. 

### **4.5 Evaluation on Chinese Data** 

In addition to experiments on English data, we show additional results on Chinese data. To validate the performance of RoFormer on long texts, we conduct experiments on long documents whose length exceeds 512 characters. 

### **4.5.1 Implementation** 

In these experiments, we carried out some modifications on WoBERT Su [2020] by replacing the absolute position embedding with our proposed RoPE. As a cross-comparison with other pre-trained Transformer-based models in Chinese, i.e. BERT Devlin et al. [2019], WoBERT Su [2020], and NEZHA Wei et al. [2019], we tabulate their tokenization level and position embedding information in Table **(3)** . 

Table 3: Cross-comparison between our RoFormer and other pre-trained models on Chinese data. ’abs’ and ’rel’ annotates absolute position embedding and relative position embedding, respectively. 

|Model|BERTDevlin et al. [2019]|WoBERTSu [2020]|NEZHAWei et al. [2019]|RoFormer|
|---|---|---|---|---|
|Tokenization level|char|word|char|word|
|Position embedding|abs.|abs.|rel.|RoPE|

---

[referencia=83213326f5835ccc score=0.034]
### **4.3.2 Implementation details** 

We use Huggingface Transformers library (Apache License 2.0)Wolf et al. [2020] to fine-tune each of the aforementioned downstream tasks for 3 epochs, with a maximum sequence length of 512, batch size of 32 and learning rates 2,3,4,5e-5. Following Devlin et al. [2019], we report the best-averaged results on the validation set. 

Table 2: Comparing RoFormer and BERT by fine tuning on downstream GLEU tasks. 

|Model|MRPC|SST-2|QNLI|STS-B|QQP|MNLI(m/mm)|
|---|---|---|---|---|---|---|
|BERTDevlin et al. [2019]|88.9|93.5|90.5|85.8|71.2|84.6/83.4|
|RoFormer|**89.5**|90.7|88.0|**87.0**|**86.4**|80.2/79.8|



### **4.3.3 Results** 

The evaluation results of the fine-tuning tasks are reported in Table **(2)** . As can be seen, RoFormer can significantly outperform BERT in three out of six datasets, and the improvements are considerable. 

### **4.4 Performer with RoPE** 

Performer Choromanski et al. [2020] introduces an alternative attention mechanism, linear attention, which is designed to avoid quadratic computation cost that scales with input sequence length. As discussed in Section **(3.3)** , the proposed RoPE can be easily implemented in the PerFormer model to realize the relative position encoding while keeping its linearly scaled complexity in self-attention. We demonstrate its performance with the pre-training task of language modeling. 

10 

RoFormer

---

[referencia=83213326f5835ccc score=0.032]
### **2.2 Absolute position embedding** 

A typical choice of Equation (1) is 



where **_p_** _i ∈_ R<sup>_d_</sup> is a d-dimensional vector depending of the position of token **_x_** _i_ . Previous work Devlin et al. [2019], Lan et al. [2020], Clark et al. [2020], Radford et al. [2019], Radford and Narasimhan [2018] introduced the use of a set of trainable vectors **_p_** _i ∈{_ **_p_** _t}_<sup>_L_</sup> _t_ =1<sup>, where</sup><sup>_L_is the maximum sequence length.The authors of Vaswani et al. [2017] have</sup> proposed to generate **_p_** _i_ using the sinusoidal function. 



in which **_p_** _i,_ 2 _t_ is the 2 _t_<sup>_th_</sup> element of the d-dimensional vector **_p_** _i_ . In the next section, we show that our proposed RoPE is related to this intuition from the sinusoidal function perspective. However, instead of directly adding the position to the context representation, RoPE proposes to incorporate the relative position information by multiplying with the sinusoidal functions.

---

[referencia=83213326f5835ccc score=0.030]
### **4.2.2 Implementation details** 

For RoFormer, we replace the sinusoidal position encoding in the self-attention block of the baseline model with our proposed RoPE and realizes self-attention according to Equation (16). We train both BERT and RoFormer with batch size 64 and maximum sequence length of 512 for 100k steps. AdamW Loshchilov and Hutter [2017] is used as the optimizer with learning rate 1e-5. 

### **4.2.3 Results** 

The MLM loss during pre-training is shown on the left plot of Figure **(3)** . Compare to the vanilla BERT, RoFormer experiences faster convergence. 

9 

RoFormer 



<!-- Start of picture text -->
10 RoFormer PerFormer w/. RoPE<br>BERT PerFormer w/o. RoPE<br>9 3.0<br>8<br>7 2.5<br>6<br>5 2.0<br>4<br>3 1.5<br>2<br>0 50 100 150 200 250 0 20 40 60 80 100<br>Train Steps (K) Train Steps (K)<br>MLM Loss LM Loss<br><!-- End of picture text -->

Figure 3: Evaluation of RoPE in language modeling pre-training. **Left** : training loss for BERT and RoFormer. **Right** : training loss for PerFormer with and without RoPE. 

### **4.3 Fine-tuning on GLUE tasks** 

Consistent with the previous experiments, we fine-tune the weights of our pre-trained RoFormer across various GLUE tasks in order to evaluate its generalization ability on the downstream NLP tasks. 

### **4.3.1 Experimental Settings** 

We look at several datasets from GLUE, i.e. MRPC Dolan and Brockett [2005], SST-2 Socher et al. [2013], QNLI Rajpurkar et al. [2016], STS-B Al-Natsheh [2017], QQP Chen et al. [2018b] and MNLI Williams et al. [2018]. We use F1-score for MRPC and QQP dataset, spearman correlation for STS-B, and accuracy for the remaining as the evaluation metrics.

---

[referencia=83213326f5835ccc score=0.017]
## **1 Introduction** 

The sequential order of words is of great value to natural language understanding. Recurrent neural networks (RRNs) based models encode tokens’ order by recursively computing a hidden state along the time dimension. Convolution neural networks (CNNs) based models (CNNs) Gehring et al. [2017] were typically considered position-agnostic, but recent work Islam et al. [2020] has shown that the commonly used padding operation can implicitly learn position information. Recently, the pre-trained language models (PLMs), which were built upon the transformer Vaswani et al. [2017], have achieved the state-of-the-art performance of various natural language processing (NLP) tasks, including context representation learning Devlin et al. [2019], machine translation Vaswani et al. [2017], and language modeling Radford et al. [2019], to name a few. Unlike, RRNs and CNNs-based models, PLMs utilize the self-attention mechanism to semantically capture the contextual representation of a given corpus. As a consequence, PLMs achieve a significant improvement in terms of parallelization over RNNs and improve the modeling ability of longer intra-token relations compared to CNNs<sup>1</sup> . 

1A stack of multiple CNN layers can also capture longer intra-token relation, here we only consider single layer setting. 

RoFormer

---

[referencia=83213326f5835ccc score=0.012]
- Peter Shaw, Jakob Uszkoreit, and Ashish Vaswani. Self-attention with relative position representations. In _NAACL-HLT_ , 2018. 

- Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Noam Shazeer, I. Simon, C. Hawthorne, Andrew M. Dai, M. Hoffman, M. Dinculescu, and D. Eck. Music transformer. _arXiv: Learning_ , 2018. 

- Zihang Dai, Z. Yang, Yiming Yang, J. Carbonell, Quoc V. Le, and R. Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. In _ACL_ , 2019. 

- Z. Yang, Zihang Dai, Yiming Yang, J. Carbonell, R. Salakhutdinov, and Quoc V. Le. Xlnet: Generalized autoregressive pretraining for language understanding. In _NeurIPS_ , 2019. 

- Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, W. Li, and Peter J. Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. _J. Mach. Learn. Res._ , 21: 140:1–140:67, 2020. 

- Guolin Ke, Di He, and T. Liu. Rethinking positional encoding in language pre-training. _ArXiv_ , abs/2006.15595, 2020. 

- Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. Deberta: Decoding-enhanced bert with disentangled attention. _ArXiv_ , abs/2006.03654, 2020.

---

[referencia=83213326f5835ccc score=0.008]
## **References** 

- Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, and Yann N Dauphin. Convolutional sequence to sequence learning. In _International Conference on Machine Learning_ , pages 1243–1252. PMLR, 2017. 

- Md. Amirul Islam, Sen Jia, and Neil D. B. Bruce. How much position information do convolutional neural networks encode? _ArXiv_ , abs/2001.08248, 2020. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, L ukasz Kaiser, and Illia Polosukhin. Attention is all you need. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, editors, _Advances in Neural Information Processing Systems_ , 

12 

RoFormer

---

[referencia=83213326f5835ccc score=0.008]
<!-- Start of picture text -->
Constant θ1 x'2 mθ1<br>x2<br>(x1, x2)<br>Query / Key x'1 x1 Position Encoded Query / Key(x'1, x'2)<br>m<br>d=2 Position<br>θ1 θ2 θd/2-1 θd/2<br>Enhanced 1<br>Transformer 2<br>with 3<br>Rotary 4<br>Position 5<br>Embedding 6<br>Query / Key Position Position Encoded Query / Key<br><!-- End of picture text -->

Figure 1: Implementation of Rotary Position Embedding(RoPE).