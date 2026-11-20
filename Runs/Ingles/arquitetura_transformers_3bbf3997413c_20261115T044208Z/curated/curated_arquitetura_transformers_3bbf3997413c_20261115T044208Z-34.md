[referencia=83213326f5835ccc score=0.980]
In this paper, we introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. Specifically, RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Note that the proposed RoPE is prioritized over the existing methods through valuable properties, including the sequence length flexibility, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Experimental results on various long text classification benchmark datasets show that the enhanced transformer with rotary position embedding, namely RoFormer, can give better performance compared to baseline alternatives and thus demonstrates the efficacy of the proposed RoPE. 

In brief, our contributions are three-folds as follows: 

- We investigated the existing approaches to the relative position encoding and found that they are mostly built based on the idea of the decomposition of adding position encoding to the context representations. We introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. The key idea is to encode relative position by multiplying the context representations with a rotation matrix with a clear theoretical interpretation. 

- We study the properties of RoPE and show that it decays with the relative distance increased, which is desired for natural language encoding. We kindly argue that previous relative position encoding-based approaches are not compatible with linear self-attention. 

- We evaluate the proposed RoFormer on various long text benchmark datasets. Our experiments show that it consistently achieves better performance compared to its alternatives. Some experiments with pre-trained language models are available on GitHub: `https://github.com/ZhuiyiTechnology/roformer` . 

The remaining of the paper is organized as follows. We establish a formal description of the position encoding problem in self-attention architecture and revisit previous works in Section **(2)** . We then describe the rotary position encoding (RoPE) and study its properties in Section **(3)** . We report experiments in Section **(4)** . Finally, we conclude this paper in Section **(5)** .

---

[referencia=83213326f5835ccc score=0.954]
## **3 Proposed approach** 

In this section, we discuss the proposed rotary position embedding (RoPE). We first formulate the relative position encoding problem in Section **(3.1)** , we then derive the RoPE in Section **(3.2)** and investigate its properties in Section **(3.3)** . 

### **3.1 Formulation** 

Transformer-based language modeling usually leverages the position information of individual tokens through a selfattention mechanism. As can be observed in Equation (2), **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n_typically enables knowledge conveyance between</sup> tokens at different positions. In order to incorporate relative position information, we require the inner product of query **_q_** _m_ and key **_k_** _n_ to be formulated by a function _g_ , which takes only the word embeddings **_x_** _m_ , **_x_** _n_ , and their relative position _m − n_ as input variables. In other words, we hope that the inner product encodes position information only in the relative form: 



The ultimate goal is to find an equivalent encoding mechanism to solve the functions _fq_ ( **_x_** _m, m_ ) and _fk_ ( **_x_** _n, n_ ) to conform the aforementioned relation. 

### **3.2 Rotary position embedding**

---

[referencia=83213326f5835ccc score=0.949]
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

[referencia=83213326f5835ccc score=0.941]
<!-- Start of picture text -->
Constant θ1 x'2 mθ1<br>x2<br>(x1, x2)<br>Query / Key x'1 x1 Position Encoded Query / Key(x'1, x'2)<br>m<br>d=2 Position<br>θ1 θ2 θd/2-1 θd/2<br>Enhanced 1<br>Transformer 2<br>with 3<br>Rotary 4<br>Position 5<br>Embedding 6<br>Query / Key Position Position Encoded Query / Key<br><!-- End of picture text -->

Figure 1: Implementation of Rotary Position Embedding(RoPE).

---

[referencia=83213326f5835ccc score=0.910]
### **2.2 Absolute position embedding** 

A typical choice of Equation (1) is 



where **_p_** _i ∈_ R<sup>_d_</sup> is a d-dimensional vector depending of the position of token **_x_** _i_ . Previous work Devlin et al. [2019], Lan et al. [2020], Clark et al. [2020], Radford et al. [2019], Radford and Narasimhan [2018] introduced the use of a set of trainable vectors **_p_** _i ∈{_ **_p_** _t}_<sup>_L_</sup> _t_ =1<sup>, where</sup><sup>_L_is the maximum sequence length.The authors of Vaswani et al. [2017] have</sup> proposed to generate **_p_** _i_ using the sinusoidal function. 



in which **_p_** _i,_ 2 _t_ is the 2 _t_<sup>_th_</sup> element of the d-dimensional vector **_p_** _i_ . In the next section, we show that our proposed RoPE is related to this intuition from the sinusoidal function perspective. However, instead of directly adding the position to the context representation, RoPE proposes to incorporate the relative position information by multiplying with the sinusoidal functions.

---

[referencia=83213326f5835ccc score=0.853]
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

[referencia=83213326f5835ccc score=0.847]
### **4.5.5 Limitations of the work** 

Although we provide theoretical groundings as well as promising experimental justifications, our method is limited by following facts: 

- Despite the fact that we mathematically format the relative position relations as rotations under 2D sub-spaces, there lacks of thorough explanations on why it converges faster than baseline models that incorporates other position encoding strategies. 

- Although we have proved that our model has favourable property of long-term decay for intern-token products, Section **(3.3)** , which is similar to the existing position encoding mechanisms, our model shows superior performance on long texts than peer models, we have not come up with a faithful explanation. 

Our proposed RoFormer is built upon the Transformer-based infrastructure, which requires hardware resources for pre-training purpose. 

## **5 Conclusions** 

In this work, we proposed a new position embedding method that incorporates explicit relative position dependency in self-attention to enhance the performance of transformer architectures. Our theoretical analysis indicates that relative position can be naturally formulated using vector production in self-attention, with absolution position information being encoded through a rotation matrix. In addition, we mathematically illustrated the advantageous properties of the proposed method when applied to the Transformer. Finally, experiments on both English and Chinese benchmark datasets demonstrate that our method encourages faster convergence in pre-training. The experimental results also show that our proposed RoFormer can achieve better performance on long texts task.

---

[referencia=83213326f5835ccc score=0.837]
### **3.2.2 General form** 

In order to generalize our results in 2D to any **_x_** _i ∈_ R<sup>_d_</sup> where _d_ is even, we divide the d-dimension space into _d/_ 2 sub-spaces and combine them in the merit of the linearity of the inner product, turning _f{q,k}_ into: 

where 



is the rotary matrix with pre-defined parameters Θ = _{θi_ = 10000<sup>_−_2(</sup><sup>_i−_1)</sup><sup>_/d_</sup> _, i ∈_ [1 _,_ 2 _, ..., d/_ 2] _}_ . A graphic illustration of RoPE is shown in Figure **(1)** . Applying our RoPE to self-attention in Equation (2), we obtain: 



where **_R_**<sup>_d_</sup> Θ _,n−m_<sup>= (</sup><sup>**_R_**</sup><sup>_d_</sup> Θ _,m_<sup>)⊺</sup><sup>**_R_**</sup> Θ<sup>_d_</sup> _,n_<sup>.Note that</sup><sup>**_R_**</sup><sup>_d_</sup> Θ<sup>is an orthogonal matrix, which ensures stability during the process of</sup> encoding position information. In addition, due to the sparsity of _R_ Θ<sup>_d_, applying matrix multiplication directly as in</sup> Equation (16) is not computationally efficient; we provide another realization in theoretical explanation. 

In contrast to the additive nature of position embedding method adopted in the previous works, i.e., Equations (3) to (10), our approach is multiplicative. Moreover, RoPE naturally incorporates relative position information through rotation matrix product instead of altering terms in the expanded formulation of additive position encoding when applied with self-attention. 



<!-- Start of picture text -->

---

[referencia=83213326f5835ccc score=0.835]
### **3.2 Rotary position embedding** 

### **3.2.1 A 2D case** 

We begin with a simple case with a dimension _d_ = 2. Under these settings, we make use of the geometric property of vectors on a 2D plane and its complex form to prove (refer Section **(3.4.1)** for more details) that a solution to our formulation Equation (11) is: 



where Re[ _·_ ] is the real part of a complex number and ( **_W_** _k_ **_x_** _n_ )<sup>_∗_</sup> represents the conjugate complex number of ( **_W_** _k_ **_x_** _n_ ). _θ ∈_ R is a preset non-zero constant. We can further write _f{q,k}_ in a multiplication matrix: 



where ( _x_<sup>(1)</sup> _m_<sup>_, x_(2)</sup> _m_<sup>) is</sup><sup>**_x_**</sup> _m_<sup>expressed in the 2D coordinates.Similarly,</sup><sup>_g_can be viewed as a matrix and thus enables the</sup> solution of formulation in Section **(3.1)** under the 2D case. Specifically, incorporating the relative position embedding is straightforward: simply rotate the affine-transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind _Rotary Position Embedding_ . 

4 

RoFormer

---

[referencia=83213326f5835ccc score=0.758]
### **2.3 Relative position embedding** 

The authors of Shaw et al. [2018] applied different settings of Equation (1) as following: 



where **_p_** ˜<sup>_k_</sup> _r_<sup>_,_˜</sup><sup>**_p_**</sup> _r_<sup>_v∈_R</sup><sup>_d_are trainable relative position embeddings.Note that</sup><sup>_r_=clip(</sup><sup>_m −n, r_min</sup><sup>_, r_max) represents the</sup> relative distance between position _m_ and _n_ . They clipped the relative distance with the hypothesis that precise relative position information is not useful beyond a certain distance. Keeping the form of Equation (3), the authors Dai et al. [2019] have proposed to decompose **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n_of Equation (2) as</sup> 



˜ the key idea is to replace the absolute position embedding **_p_** _n_ with its sinusoid-encoded relative counterpart **_p_** _m−n_ , while the absolute position **_p_** _m_ in the third and fourth term with two trainable vectors **u** and **v** independent of the query positions. Further, **_W_** _k_ is distinguished for the content-based and location-based key vectors **_x_** _n_ and **_p_** _n_ , denoted as **_W_** _k_ and **_W_**<sup>�</sup> _k_ , resulting in: 



It is noteworthy that the position information in the value term is removed by setting _fv_ ( **_x_** _j_ ) := **_W_** _v_ **_x_** _j_ . Later work Raffel et al. [2020], He et al. [2020], Ke et al. [2020], Huang et al. [2020] followed these settings by only encoding the relative position information into the attention weights. However, the authors of Raffel et al. [2020] reformed Equation (6) as:

---

[referencia=83213326f5835ccc score=0.681]
where _ϕ_ ( _·_ ) _, φ_ ( _·_ ) are usually non-negative functions. The authors of Katharopoulos et al. [2020] have proposed _ϕ_ ( _x_ ) = _φ_ ( _x_ ) = elu( _x_ )+1 and first computed the multiplication between keys and values using the associative property of matrix multiplication. A softmax function is used in Shen et al. [2021] to normalize queries and keys separately before the inner product, which is equivalent to _ϕ_ ( **_q_** _i_ ) = softmax( **_q_** _i_ ) and _ϕ_ ( **_k_** _j_ ) = exp( **_k_** _j_ ). For more details about linear attention, we encourage readers to refer to original papers. In this section, we focus on discussing incorporating RoPE with Equation (18). Since RoPE injects position information by rotation, which keeps the norm of hidden representations unchanged, we can combine RoPE with linear attention by multiplying the rotation matrix with the outputs of the non-negative functions. 



It is noteworthy that we keep the denominator unchanged to avoid the risk of dividing zero, and the summation in the numerator could contain negative terms. Although the weights for each value **_v_** _i_ in Equation (19) are not strictly probabilistic normalized, we kindly argue that the computation can still model the importance of values. 

### **3.4 Theoretical Explanation**

---

[referencia=83213326f5835ccc score=0.678]
### **3.4.1 Derivation of RoPE under 2D** 

Under the case of _d_ = 2, we consider two-word embedding vectors **_x_** _q_ , **_x_** _k_ corresponds to query and key and their position _m_ and _n_ , respectively. According to eq. (1), their position-encoded counterparts are: 



where the subscripts of **_q_** _m_ and **_k_** _n_ indicate the encoded positions information. Assume that there exists a function _g_ that defines the inner product between vectors produced by _f{q,k}_ : 



we further require below initial condition to be satisfied: 



which can be read as the vectors with empty position information encoded. Given these settings, we attempt to find a solution of _fq_ , _fk_ . First, we take advantage of the geometric meaning of vector in 2D and its complex counter part, decompose functions in Equations (20) and (21) into: 



where _Rf_ , _Rg_ and Θ _f_ , Θ _g_ are the radical and angular components for _f{q,k}_ and _g_ , respectively. Plug them into Equation (21), we get the relation: 



6 

RoFormer 

with the corresponding initial condition as: 



where _∥_ **_q_** _∥_ , _∥_ **_k_** _∥_ and _θq_ , _θk_ are the radial and angular part of **_q_** and **_k_** on the 2D plane. 

Next, we set _m_ = _n_ in Equation (24) and take into account initial conditions in Equation (25): 



On one hand, from, a straightforward solution of _Rf_ could be formed from Equation (26a) :

---

[referencia=83213326f5835ccc score=0.640]
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

[referencia=83213326f5835ccc score=0.609]
## **2 Background and Related Work** 

### **2.1 Preliminary** 

Let S _N_ = _{wi}_<sup>_N_</sup> _i_ =1<sup>be a sequence of</sup><sup>_N_input tokens with</sup><sup>_wi_being the</sup><sup>_ith_element.The corresponding word embedding</sup> of S _N_ is denoted as E _N_ = _{_ **_x_** _i}_<sup>_N_</sup> _i_ =1<sup>, where</sup><sup>**_x_**</sup><sup>_i∈_R</sup><sup>_d_is the d-dimensional word embedding vector of token</sup><sup>_wi_without</sup> position information. The self-attention first incorporates position information to the word embeddings and transforms them into queries, keys, and value representations. 



where **_q_** _m,_ **_k_** _n_ and **_v_** _n_ incorporate the _m_<sup>_th_</sup> and _n_<sup>_th_</sup> positions through _fq, fk_ and _fv_ , respectively. The query and key values are then used to compute the attention weights, while the output is computed as the weighted sum over the value 

2 

RoFormer 

representation. 



The existing approaches of transformer-based position encoding mainly focus on choosing a suitable function to form Equation (1).

---

[referencia=83213326f5835ccc score=0.604]
### **3.3 Properties of RoPE** 

**Long-term decay:** Following Vaswani et al. [2017], we set _θi_ = 10000<sup>_−_2</sup><sup>_i/d_</sup> . One can prove that this setting provides a long-term decay property (refer to Section **(3.4.3)** for more details), which means the inner-product will decay when the relative position increase. This property coincides with the intuition that a pair of tokens with a long relative distance should have less connection. 

**RoPE with linear attention:** The self-attention can be rewritten in a more general form. 

5 

RoFormer 



The original self-attention chooses sim( **_q_** _m,_ **_k_** _n_ ) = exp( **_q_**<sup>⊺</sup> _m_<sup>**_k_**</sup><sup>_n/_</sup> _√d_ ). Note that the original self-attention should compute the inner product of query and key for every pair of tokens, which has a quadratic complexity O( _N_<sup>2</sup> ). Follow Katharopoulos et al. [2020], the linear attentions reformulate Equation (17) as

---

[referencia=83213326f5835ccc score=0.454]
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

[referencia=83213326f5835ccc score=0.362]
where _bi,j_ is a trainable bias. The authors of Ke et al. [2020] investigated the middle two terms of Equation (6) and found little correlations between absolute positions and words. The authors of Raffel et al. [2020] proposed to model a pair of words or positions using different projection matrices. 



3 

RoFormer 

The authors of He et al. [2020] argued that the relative positions of two tokens could only be fully modeled using the middle two terms of Equation (6).replaced with the relative position embeddingsAs a consequence, the absolute position embeddings **_p_** ˜ _m−n_ : **_p_** _m_ and **_p_** _n_ were simply 



A comparison of the four variants of the relative position embeddings Radford and Narasimhan [2018] has shown that the variant similar to Equation (10) is the most efficient among the other three. Generally speaking, all these approaches attempt to modify Equation (6) based on the decomposition of Equation (3) under the self-attention settings in Equation (2), which was originally proposed in Vaswani et al. [2017]. They commonly introduced to directly add the position information to the context representations. Unlikely, our approach aims to derive the relative position encoding from Equation (1) under some constraints. Next, we show that the derived approach is more interpretable by incorporating relative position information with the rotation of context representations.

---

[referencia=83213326f5835ccc score=0.259]
### **3.4.2 Computational efficient realization of rotary matrix multiplication** 

Taking the advantage of the sparsity of **_R_**<sup>_d_</sup> Θ _,m_<sup>inEquation(15),amorecomputationalefficientrealizationofa</sup> multiplication of _R_ Θ<sup>_d_and</sup><sup>**_x_**</sup><sup>_∈_R</sup><sup>_d_is:</sup> 



7 

RoFormer 



<!-- Start of picture text -->
relative upper bound<br>20<br>18<br>16<br>14<br>12<br>10<br>8<br>relative distance<br>50 100 150 200 250<br><!-- End of picture text -->

Figure 2: Long-term decay of RoPE.

---

[referencia=83213326f5835ccc score=0.228]
### **4.1.2 Implementation details** 

We carry out some modifications on self-attention layer of the baseline model Vaswani et al. [2017] to enable RoPE to its learning process. We replicate the setup for English-to-German translation with a vocabulary of 37k based on a joint source and target byte pair encoding(BPE)Sennrich et al. [2015]. During the evaluation, a single model is obtained by averaging the last 5 checkpoints. The result uses beam search with a beam size of 4 and length penalty 0.6. We implement the experiment in PyTorch in the fairseq toolkit (MIT License)Ott et al. [2019]. Our model is optimized with the Adam optimizer using _β_ 1 = 0 _._ 9, _β_ 2 = 0 _._ 98, learning rate is increased linearly from 1 _e −_ 7 to 5 _e −_ 4 and then decayed proportionally to the inverse square root of the step number. Label smoothing with 0.1 is also adopted. We report the BLEUPapineni et al. [2002] score on the test set as the final metric. 

### **4.1.3 Results** 

We train the baseline model and our RoFormer under the same settings and report the results in Table **(1)** . As can be seen, our model gives better BLEU scores compared to the baseline Transformer. 

### **4.2 Pre-training Language Modeling** 

The second experiment is to validate the performance of our proposal in terms of learning contextual representations. To achieve this, we replace the original sinusoidal position encoding of BERT with our RoPE during the pre-training step. 

### **4.2.1 Experimental Settings** 

We use the BookCorpus Zhu et al. [2015] and the Wikipedia Corpus Foundation [2021] from Huggingface Datasets library (Apache License 2.0) for pre-training. The corpus is further split into train and validation sets at 8:2 ratio. We use the masked language-modeling (MLM) loss values of the training process as an evaluation metric. The well-known BERT Devlin et al. [2019] is adopted as our baseline model. Note that we use bert-base-uncased in our experiments.

---

[referencia=83213326f5835ccc score=0.205]
On one hand, from, a straightforward solution of _Rf_ could be formed from Equation (26a) : 



which interprets the radial functions _Rq_ , _Rk_ and _Rg_ are independent from the position information. On the other hand, as can be noticed in Equation (26b), Θ _q_ ( **_x_** _q, m_ ) _− θq_ = Θ _k_ ( **_x_** _k, m_ ) _− θk_ indicates that the angular functions does not dependent on query and key, we set them to Θ _f_ := Θ _q_ = Θ _k_ and term Θ _f_ ( **_x_** _{q,k}, m_ ) _− θ{q,k}_ is a function of position _m_ and is independent of word embedding **_x_** _{q,k}_ , we denote it as _ϕ_ ( _m_ ), yielding: 



Further, by plugging _n_ = _m_ + 1 to Equation (24) and consider the above equation, we can get: 



Since RHS is a constant irrelevant to _m_ , _ϕ_ ( _m_ ) with continuous integer inputs produce an arithmetic progression: 



where _θ, γ ∈_ R are constants and _θ_ is non-zero. To summarize our solutions from Equations (27) to (30): 



Note that we do not apply any constrains to _fq_ and _fk_ of Equation (22), thus _fq_ ( **_x_** _m,_ 0) and _fk_ ( **_x_** _n,_ 0) are left to choose freely. To make our results comparable to Equation (3), we define: 



Then, we simply set _γ_ = 0 in Equation (31) of the final solution: