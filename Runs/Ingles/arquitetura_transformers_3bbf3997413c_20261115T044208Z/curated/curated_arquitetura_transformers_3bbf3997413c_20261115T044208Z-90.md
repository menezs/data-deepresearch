[referencia=a114e852aac1b2cb score=0.847]
# Google Research 

## **Abstract** 

Multi-query attention (MQA), which only uses a single key-value head, drastically speeds up decoder inference. However, MQA can lead to quality degradation, and moreover it may not be desirable to train a separate model just for faster inference. We (1) propose a recipe for uptraining existing multi-head language model checkpoints into models with MQA using 5% of original pre-training compute, and (2) introduce grouped-query attention (GQA), a generalization of multi-query attention which uses an intermediate (more than one, less than number of query heads) number of key-value heads. We show that uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA. 

## **1 Introduction** 

Autoregressive decoder inference is a severe bottleneck for Transformer models due to the memory bandwidth overhead from loading decoder weights and all attention keys and values at every decoding step (Shazeer, 2019; Pope et al., 2022; de Jong et al., 2022). The memory bandwidth from loading keys and values can be sharply reduced through _multi-query attention_ (Shazeer, 2019), which uses multiple query heads but single key and value heads. 

However, multi-query attention (MQA) can lead to quality degradation and training instability, and it may not be feasible to train separate models optimized for quality and inference. Moreover, while some language models already use multiquery attention, such as PaLM (Chowdhery et al., 2022), many do not, including publicly available language models such as T5 (Raffel et al., 2020) and LLaMA (Touvron et al., 2023). 

This work contains two contributions for faster inference with large language models. First, we 

> _∗_ Equal contribution. 

show that language model checkpoints with multihead attention (MHA) can be _uptrained_ (Komatsuzaki et al., 2022) to use MQA with a small fraction of original training compute. This presents a cost-effective method to obtain fast multi-query as well as high-quality MHA checkpoints. 

Second, we propose grouped-query attention (GQA), an interpolation between multi-head and multi-query attention with single key and value heads _per subgroup of query heads_ . We show that uptrained GQA achieves quality close to multihead attention while being almost as fast as multiquery attention.

---

[referencia=a114e852aac1b2cb score=0.800]
### **2.2 Grouped-query attention** 

Grouped-query attention divides query heads into _G groups_ , each of which shares a single key head and value head. GQA-G refers to grouped-query with _G_ groups. GQA-1, with a single group and therefore single key and value head, is equivalent to MQA, while GQA-H, with groups equal to number of heads, is equivalent to MHA. Figure 2 shows a comparison of grouped-query attention and multihead/multi-query attention. When converting a multi-head checkpoint to a GQA checkpoint, we construct each group key and value head by meanpooling all the original heads within that group. 

An intermediate number of groups leads to an interpolated model that is higher quality than MQA but faster than MHA, and, as we will show, represents a favorable trade-off. Going from MHA to MQA reduces _H_ key and value heads to a single key and value head, reducing the size of the key-value cache and therefore amount of data that needs to be loaded by a factor of _H_ . However, larger models generally scale the number of heads, such that multi-query attention represents a more aggressive cut in both memory bandwidth and capacity. GQA lets us keep the same proportional decrease in bandwidth and capacity as model size increases. 

Moreover, larger models suffer relatively less from memory bandwidth overhead from attention, as the KV-cache scales with model dimension while model FLOPs and parameters scale with the square of model dimension. Finally, standard sharding for large models replicates the single key and value head by the number of model partitions (Pope 

et al., 2022); GQA removes the waste from such partitioning. Therefore, we expect GQA to present a particularly good trade-off for larger models. 

We note that GQA is not applied to the encoder self-attention layers; encoder representations are computed in parallel, and memory bandwidth is therefore generally not the primary bottleneck.

---

[referencia=a114e852aac1b2cb score=0.763]
Figure 5: Performance as a function of uptraining proportion for T5 XXL models with MQA and GQA-8. 

**Number of groups** Figure 6 demonstrates the effect of the number of GQA groups on inference speed. For larger models the memory bandwidth overhead from the KV cache is less constraining (Shazeer, 2019), while the reduction in key-value size is sharper due to the increased number of heads. As a result, increasing the number of groups from MQA only results in modest slowdowns initially, with increasing cost as we move closer to MHA. We selected 8 groups as a favorable middle ground.

---

[referencia=a114e852aac1b2cb score=0.758]
## **5 Conclusion** 

Language models are expensive for inference primarily due to the memory bandwidth overhead from loading keys and values. Multi-query attention reduces this overhead at the cost of decreased model capacity and quality. We propose to convert multi-head attention models to multi-query models with a small fraction of original pre-training compute. Moreover, we introduce grouped-query attention, an interpolation of multi-query and multi-head attention that achieves quality close to multi-head at comparable speed to multi-query attention. 

## **Limitations** 

This paper focuses on ameliorating the memory bandwidth overhead from loading keys and values. This overhead is most important when generating longer sequences, for which quality is inherently difficult to evaluate. For summarization we employ Rouge score, which we know is a flawed evaluation that does not tell the whole story; for that reason, it is difficult to be certain our trade-offs are correct. Due to limited computation, we also do not compare our XXL GQA model to a comparitive model trained from scratch, so we do not know the relative performance of uptraining vs training from scratch. Finally, we evaluate the impact of uptraining and GQA only on encoder-decoder models. Recently, decoder-only models are extremely popular, and since these models do not have separate self-attention and cross-attention, we expect GQA to have a stronger advantage over MQA.

---

[referencia=a114e852aac1b2cb score=0.415]
**Fine-tuning** For fine-tuning, we use a constant learning rate of 0.001, batch size 128, and dropout rate 0.1 for all tasks. CNN/Daily Mail and WMT use input length of 512 and output length 256. Other summarization datasets use input length 2048 and output length 512. Finally, TriviaQA uses input length 2048 and output length 32. We train until convergence and select the checkpoint with the highest dev performance. We use greedy decoding for inference. 

**Timing** We report time per sample per TPUv4 chip, as measured by xprof (Google, 2020). For timing experiments we use 8 TPUs with the largest batch size that fits up to 32 per TPU, and parallelization optimized separately for each model. 



<!-- Start of picture text -->
MHA-XXL<br>GQA-XXL<br>47<br>46 . 5<br>MQA-XXL<br>46<br>MHA-Large<br>0 0 . 5 1 1 . 5<br>Time per sample (ms)<br>Performance<br><!-- End of picture text -->

Figure 3: **Uptrained MQA yields a favorable tradeoff compared to MHA with higher quality and faster speed than MHA-Large, and GQA achieves even better performance with similar speed gains and comparable quality to MHA-XXL.** Average performance on all tasks as a function of average inference time per sample for T5-Large and T5-XXL with multihead attention, and 5% uptrained T5-XXL with MQA and GQA-8 attention. 

### **3.2 Main results** 

Figure 3 shows average performance over all datasets as a function of average inference time for MHA T5-Large and T5-XXL, and uptrained MQA and GQA-8 XXL models with uptraining proportion _α_ = 0 _._ 05. We see that a larger uptrained MQA model provides a favorable tradeoff relative to MHA models, with higher quality and faster inference than MHA-Large. Moreover, GQA achieves significant additional quality gains, achieving performance close to MHA-XXL with speed close to MQA. Table 1 contains full results for all datasets.

---

[referencia=a114e852aac1b2cb score=0.383]
## **4 Related Work** 

This work is focused on achieving a better tradeoff between decoder quality and inference time through reducing the memory bandwidth overhead (Williams et al., 2009) from loading keys and values. Shazeer (2019) first proposed reducing this overhead through multi-query attention. Follow-up work showed that multi-query attention 

is especially helpful for long inputs (Pope et al., 2022; de Jong et al., 2022). Rabe (2023) independently developed GQA with public implementation. Other works have explored grouping attention heads for computational efficiency (Park et al., 2020; Luo et al., 2022; Ni et al., 2023) without focusing specifically on key-value heads, which determine memory bandwidth overhead. 

A number of other methods have been proposed to reduce memory bandwidth overhead from keys and values, as well as parameters. Flash attention (Dao et al., 2022) structures the attention computation to avoid materializing the quadratic attention scores, reducing memory and speeding up training. Quantization (Dettmers et al., 2022; Frantar et al., 2022) reduces the size of weights and activations, including keys and values, by lowering precision. Model distillation (Hinton et al., 2015; Gou et al., 2021) instead reduces model size at a given precision, using data generated from the larger model to finetune the smaller model. Layersparse cross-attention (de Jong et al., 2022) eliminates most cross-attention layers which make up the primary expense for longer inputs. Speculative sampling (Chen et al., 2023; Leviathan et al., 2022) ameliorates the memory bandwidth bottleneck by proposing multiple tokens with a smaller model which are then scored in parallel by a larger model. 

Finally, the uptraining procedure we propose is inspired by Komatsuzaki et al. (2022), which uptrains standard T5 checkpoints into sparsely activated Mixture-of-Experts models.

---

[referencia=a114e852aac1b2cb score=0.275]
### **3.3 Ablations** 

This section presents experiments to investigate the effect of different modeling choices. We eval- 

uate performance on a representive subsample of tasks: CNN/Daily Mail, (short-form summarization), MultiNews (long-form summarization), and TriviaQA (question-answering). 

**Checkpoint conversion** Figure 4 compares the performance of different methods for checkpoint conversion. Mean pooling appears to work best, followed by selecting a single head and then random initialization. Intuitively, results are ordered by the degree to which information is preserved from the pre-trained model. 

**Uptraining steps** Figure 5 shows how performance varies with uptraining proportion for T5 XXL with MQA and GQA. First, we note that GQA already achieves reasonable performance after conversion while MQA requires uptraining to 



<!-- Start of picture text -->
Mean<br>First<br>Random<br>54 . 4 54 . 6 54 . 8 55 55 . 2 55 . 4 55 . 6<br><!-- End of picture text -->

Figure 4: Performance comparison of different checkpoint conversion methods for T5-Large uptrained to MQA with proportion _α_ = 0 _._ 05. ‘Mean’ mean-pools key and value heads, ‘First’ selects the first head and ‘Random’ initializes heads from scratch. 



<!-- Start of picture text -->
2<br>MHA<br>GQA<br>MQA<br>1<br>1 4 8 16 32 64<br>GQA groups<br>Time per sample (s)<br><!-- End of picture text -->

Figure 6: Time per sample for GQA-XXL as a function of the number of GQA groups with input length 2048 and output length 512. Going from 1 (MQA) to 8 groups adds modest inference overhead, with increasing cost to adding more groups. 

be useful. Both MQA and GQA gain from 5% uptraining with diminishing returns from 10%. 



<!-- Start of picture text -->
57<br>56<br>MHA<br>GQA<br>55<br>MQA<br>54<br>0 0 . 02 0 . 04 0 . 06 0 . 08 0 . 1<br>Uptraining proportion  α<br>Performance<br><!-- End of picture text -->

---

[referencia=a114e852aac1b2cb score=0.194]
### **3.1 Experimental setup** 

**Configurations** All models are based on the T5.1.1 architecture (Raffel et al., 2020), implemented with JAX (Bradbury et al., 2018), Flax (Heek et al., 2020), and Flaxformer<sup>1</sup> . For our main experiments we consider T5 Large and XXL with multi-head attention, as well as uptrained versions of T5 XXL with multi-query and grouped-query attention. We use the Adafactor optimizer with the same hyperparameters and learning rate schedule as T5 (Raffel et al., 2020). We apply MQA and GQA to decoder self-attention and cross-attention, but not encoder self-attention. 

**Uptraining** Uptrained models are initialized from public T5.1.1 checkpoints. The key and value heads are mean-pooled to the appropriate MQA or GQA structure, and then pre-trained for a further _α_ proportion of original pre-training steps with the original pre-training setup and dataset from (Raffel et al., 2020). For _α_ = 0 _._ 05, training took approximately 600 TPUv3 chip-days. 

**Data** We evaluate on summarization datasets CNN/Daily Mail (Nallapati et al., 2016), arXiv and PubMed (Cohan et al., 2018), MediaSum (Zhu et al., 2021), and Multi-News (Fabbri et al., 2019); 

1https://github.com/google/flaxformer

---

[referencia=a114e852aac1b2cb score=0.153]
1https://github.com/google/flaxformer 

|**Model**|**Tinfer**|**Average**|**CNN**|**arXiv**|**PubMed**|**MediaSum**|**MultiNews**|**WMT**|**TriviaQA**|
|---|---|---|---|---|---|---|---|---|---|
||**s**||**R1**|**R1**|**R1**|**R1**|**R1**|**BLEU**|**F1**|
|MHA-Large|0.37|46.0|42.9|44.6|46.2|35.5|46.6|27.7|78.2|
|MHA-XXL|1.51|47.2|43.8|45.6|47.5|36.4|46.9|28.4|81.9|
|MQA-XXL|0.24|46.6|43.0|45.0|46.9|36.1|46.5|28.5|81.3|
|GQA-8-XXL|0.28|47.1|43.5|45.4|47.7|36.3|47.2|28.4|81.6|



Table 1: Inference time and average dev set performance comparison of T5 Large and XXL models with multi-head attention, and 5% uptrained T5-XXL models with multi-query and grouped-query attention on summarization datasets CNN/Daily Mail, arXiv, PubMed, MediaSum, and MultiNews, translation dataset WMT, and questionanswering dataset TriviaQA. 

translation dataset WMT 2014 English-to-German; and question answering dataset TriviaQA (Joshi et al., 2017). We do not evaluate on popular classification benchmarks such as GLUE (Wang et al., 2019) as autoregressive inference is less applicable for those tasks.

---

[referencia=5e9c4b0d7e28a9c7 score=0.040]
# **Fast Transformer Decoding: One Write-Head is All You Need** 



Noam Shazeer Google noam@google.com 

November 7, 2019 

##### **Abstract** 

Multi-head attention layers, as used in the Transformer neural sequence model, are a powerful alternative to RNNs for moving information across and between sequences. While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors. We propose a variant called multi-query attention, where the keys and values are shared across all of the different attention "heads", greatly reducing the size of these tensors and hence the memory bandwidth requirements of incremental decoding. We verify experimentally that the resulting models can indeed be much faster to decode, and incur only minor quality degradation from the baseline. 

## **1 Introduction** 

The Transformer neural sequence model [Vaswani et al., 2017] has emerged as a popular alternative to recurrent sequence models. Transformer relies on attention layers to communicate information between and across sequences. One major challenge with Transformer is the speed of incremental inference. As we will discuss, the speed of incremental Transformer inference on modern computing hardware is limited by the memory bandwidth necessary to reload the large "keys" and "values" tensors which encode the state of the attention layers. In the following sections, we will review the multi-head-attention layers used by Transformer, provide a performance analysis, and propose an architectural variation (multi-query attention) which greatly improves inference speed with only minor quality degradation.

---

[referencia=5e9c4b0d7e28a9c7 score=0.029]
### **3.1 Performance Analysis for Incremental Multi-Query Attention** 

We make the same simplifying assumptions as in section 2.3.1. 

Across _n_ calls, the total number of arithmetic operations is again Θ( _bnd_<sup>2</sup> ). 

Across _n_ calls, the total amount of memory access is Θ( _bnd_ + _bn_<sup>2</sup> _k_ + _nd_<sup>2</sup> ), the first term due to _x_ , _q_ , _o_ and _y_ , the second term due to _K_ and _V_ and the third term due to _Pq_ , _Pk_ , _Pv_ , _Po_ . 

Dividing the memory by the computations, we find that the ratio of memory access to arithmetic operations is Θ( _d_<sup>1+</sup> _dh_<sup>_n_+1</sup> _b_<sup>).Wehavereducedtheoffensive</sup><sup>_n_</sup> _d_<sup>byafactorof</sup><sup>_h_.Theoretically,givenlargebatch</sup> size _b_ , this should dramatically improve performance of incremental generation. In our experimental section, we will show that the performance gains are real and that model quality remains high.

---

[referencia=5e9c4b0d7e28a9c7 score=0.028]
### **4.3 Speed** 

Table 2 shows training and inference times for the various models. Both training and inference speeds were evaluated on one TPUv2 (8 cores). A training step (consisting of 32,768 input tokens and 32,768 target tokens, as described above) took 433ms for the base model and 425ms for the multi-query model. Dividing by 32,768, we find that the training time is 13.2 _µs_ per (input-token + target-token), as listed in Table 2. 

We ran incremental greedy inference on a batch of 1024 sequences (128 per core) using a source-sequence length of 128 tokens and a target sequence length of 128.<sup>1</sup> For the baseline model, the encoder part of the model took 222ms and each incremental step of the decoder took 47ms. Dividing by the respective numbers of tokens, we find that the amortized inference time is 1 _._ 7 _µs_ per token for the encoder and a much larger 46 _µs_ per token for the decoder, as listed in Table 2. For the multi-query model, the encoder took 195ms and the decoder took 3.9ms per step, for amortized per-token costs of 1 _._ 5 _µs_ and 3 _._ 8 _µs_ respectively. Table 2 shows these values as well as similar results for beam-search. 



> 1Due to system limitations requiring fixed shapes, we used padding and masking in our decoder-self-attention implementation. The memory tensors were thus padded to the maximum length (128), or to the window-size (32) in the case of local attention. Each decoding step thus took the same amount of time. An alternative implementation of incrementally growing the tensors could save time near the beginning of the sequence. 

7 

Table 1: WMT14 EN-DE Results.

---

[referencia=5e9c4b0d7e28a9c7 score=0.020]
#### **2.4.1 Performance Analysis** 

We make the same simplifying assumptions as in section 2.3.1. 

Across _n_ calls, the total number of arithmetic operations is again Θ( _bnd_<sup>2</sup> ). 

Across _n_ calls, the total amount of memory access is Θ( _bn_<sup>2</sup> _d_ + _nd_<sup>2</sup> ), the first term due to _K_ and _V_ and the second term due to _Pq_ , _Pk_ , _Pv_ and _Po_ . 

Dividing the memory by the computations, we find that the ratio of memory access to arithmetic operations is Θ(<sup>_n_</sup> _d_<sup>+1</sup> _b_<sup>).When</sup><sup>_n_≈</sup><sup>_d_or</sup><sup>_b_≈1,theratioiscloseto1,causingmemorybandwidthtobeamajor</sup> performance bottleneck on modern computing hardware. In order to make incremental generation efficient, we must reduce both of these terms to be ≪ 1. The<sup>1</sup> _b_<sup>term istheeasier one-wecan justusealarger batch</sup> size, memory size permitting. 

Reducing the<sup>_n_</sup> _d_<sup>term is harder.This term is related to the expense of reloading at each step the</sup><sup>_K_and</sup><sup>_V_</sup> tensors representing the memory which have size _bhmk_ = _bn_<sup>2</sup> . One solution is to limit the sequence length _n_ . Another is to reduce the number of positions being attended-to, either by attending to a local neighborhood, or by otherwise compressing the number of memory positions, as in [Liu et al., 2018], [Zhang et al., 2018], [Povey et al., 2018]. In this paper we present an orthogonal approach to reducing the size of the _K_ and _V_ tensors - namely removing their "heads" dimension, while maintaining the "heads" dimension in the queries. 

4

---

[referencia=5e9c4b0d7e28a9c7 score=0.017]
#### **2.3.1 Performance Analysis of Batched Multi-head Attention** 

To simplify the performance analysis, we will make several simplifying assumptions: 

- _m_ = _n_ 

- _k_ = _v_ =<sup>_d_assuggestedby[Vaswanietal.,2017]</sup> _h_<sup>,</sup> 

- _n_ ≤ _d_ 

The total number of arithmetic operations is Θ( _bnd_<sup>2</sup> ). (Since the complexity of each of the tf.einsum operations above is _O_ ( _bnd_<sup>2</sup> ) given the simplifying assumptions. 

The total size of memory to be accessed is equal to the sum of the sizes of all the tensors involved: _O_ ( _bnd_ + _bhn_<sup>2</sup> + _d_<sup>2</sup> ). The first term is due to _X_ , _M_ , _Q_ , _K_ , _V_ , _O_ and _Y_ , the second term due to the logits and weights, and the third term due to the projection tensors _Pq_ , _Pk_ , _Pv_ and _Po_ . 

Dividing the two, we find that the ratio of memory access to arithmetic operations is _O_ ( _k_<sup>1+</sup> _bn_<sup>1).This low</sup> ratio is necessary for good performance on modern GPU/TPU hardware, where the computational capacity can be two orders of magnitude higher than the memory bandwidth.

---

[referencia=5e9c4b0d7e28a9c7 score=0.012]
## **5 Conclusion** 

We have proposed multi-query attention - an alternative to multi-head attention with much lower memorybandwidth requirements in the incremental setting. We believe that this enables wider adoption of attentionbased sequence models in inference-performance-critical applications. 

## **References** 

Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate, 2014. 

- Ciprian Chelba, Tomas Mikolov, Mike Schuster, Qi Ge, Thorsten Brants, and Phillipp Koehn. One billion word benchmark for measuring progress in statistical language modeling. _CoRR_ , abs/1312.3005, 2013. URL http://arxiv.org/abs/1312.3005. 

Peter J Liu, Mohammad Saleh, Etienne Pot, Ben Goodrich, Ryan Sepassi, Lukasz Kaiser, and Noam Shazeer. 

8 

Generating wikipedia by summarizing long sequences. In _Proceedings of the International Conference on Learning Representations_ , 2018. 

- Daniel Povey, Hossein Hadian, Pegah Ghahremani, Ke Li, and Sanjeev Khudanpur. A time-restricted selfattention layer for ASR. In _Proceddings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ . IEEE, 2018. 

- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. In _NIPS_ , 2017. 

- Biao Zhang, Deyi Xiong, and Jinsong Su. Accelerating neural transformer via an average attention network, 2018. 

9

---

[referencia=a114e852aac1b2cb score=0.010]
 - Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Anselm Levskaya, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. 2022. Efficiently scaling transformer inference. _arXiv preprint arXiv:2211.05102_ . 

   - Markus Rabe. 2023. Memory-efficient attention. https://github.com/google/flaxformer/ blob/main/flaxformer/components/ attention/memory_efficient_attention.py. Accessed: 2023-05-23. 

   - Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the limits of transfer learning with a unified text-to-text transformer. _J. Mach. Learn. Res._ , 21:140:1–140:67. 

   - Noam Shazeer. 2019. Fast transformer decoding: One write-head is all you need. _arXiv preprint arXiv:1911.02150_ . 

   - Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023. Llama: Open and efficient foundation language models. 

   - Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. 2019. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In _7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019_ . OpenReview.net. 

   - Samuel Williams, Andrew Waterman, and David A. Patterson. 2009. Roofline: an insightful visual performance model for multicore architectures. _Commun. ACM_ , 52(4):65–76.

---

[referencia=a114e852aac1b2cb score=0.006]
# **GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints** 

**Joshua Ainslie**<sup>_∗_</sup> **, James Lee-Thorp,**<sup>_∗_</sup> **Michiel de Jong**<sup>_∗_</sup><sup>**_†_**</sup> **Yury Zemlyanskiy** , **Federico Lebrón** , **Sumit Sanghai**

---

[referencia=5e9c4b0d7e28a9c7 score=0.006]
### **2.3 Multi-head Attention (Batched)** 

In practice, it is far more efficient to batch together multiple queries. The code below adds two types of batching. First, we generate queries from _n_ different positions in a sequence. These queries all interact with the same keys and values. In addition, we process a batch of _b_ different non-interacting sequences at once. Following [Vaswani et al., 2017], in an autoregressive model, we can prevent backward-information-flow by adding a "mask" to the logits containing the value −∞ in the illegal positions. 

def MultiheadAttentionBatched( X, M, mask , P_q, P_k, P_v, P_o ) : " " " Multi−head Attention . Args : X: a tensor with shape [ b , n , d ] M: a tensor with shape [ b , m, d ] mask : a tensor with shape [ b , h , n , m] P_q: a tensor with shape [ h , d , k ] P_k: a tensor with shape [ h , d , k ] P_v: a tensor with shape [ h , d , v ] P_o: a tensor with shape [ h , d , v ] Returns : Y: a tensor with shape [ b , n , d ] " " " Q = t f . einsum ( "bnd , hdk−>bhnk " , X, P_q) K = t f . einsum ( "bmd, hdk−>bhmk" , M, P_k) V = t f . einsum ( "bmd, hdv−>bhmv" , M, P_v) l o g i t s = t f . einsum ( "bhnk , bhmk−>bhnm" , Q, K) weights = t f . softmax ( l o g i t s + mask ) O = t f . einsum ( "bhnm,bhmv−>bhnv " , weights , V) Y = t f . einsum ( "bhnv , hdv−>bnd" , O, P_o) return Y

---

[referencia=5e9c4b0d7e28a9c7 score=0.005]
### **4.1 Experimental Setup** 

Following [Vaswani et al., 2017], we evaluate on the WMT 2014 English-German translation task. As a baseline, we use an encoder-decoder Transformer model with 6 layers, using _dmodel_ = 1024 _dff_ = 4096, _h_ = 8, _dk_ = _dv_ = 128, learned positional embeddings, and weight-sharing between the token-embedding and output layers. The baseline model and all variations have 211 million parameters. All models were trained for 100,000 steps ( 20 epochs). Each training batch consisted of 128 examples, each of which consisted of a 256-token input sequence and a 256-token target sequence (multiple training sentences were concatenated together to reach this length). Models were trained on a 32-core TPUv3 cluster, with each model taking about 2 hours to train. We used an implementation from the tensor2tensor and mesh-tensorflow libraries. 

6 

The configurations used can be found at [to be added before publication] , including details about learning rates, dropout, label smoothing, etc. 

In our "multi-query" model, we replace all of the attention layers in the model to multi-query attention. This includes the encoder-self-attention, decoder-self-attention and encoder-decoder-attention layers. We widen the feed-forward hidden layers from 4096 to 5440 to make the total parameter-count equal to that of the baseline. 

To demonstrate that local-attention and multi-query attention are orthogonal, we also trained "local" versions of the baseline and multi-query models, where the decoder-self-attention layers (but not the other attention layers) restrict attention to the current position and the previous 31 positions. 

A simpler alternative way to reduce the sizes of _K_ and _V_ is to reduce the number of heads _h_ and/or to reduce the dimensionalities _k_ and _v_ of the keys and values. We trained several such models for comparison, again widening the feed-forward hidden layers to make the total parameter-count equal to that of the baseline.

---

[referencia=5e9c4b0d7e28a9c7 score=0.005]
Table 3: Billion-Word LM Benchmark Results. 

|Attention|_h_|_dk, dv_|_dff_|dev-PPL|
|---|---|---|---|---|
|multi-head|8|128|8192|**29.9**|
|multi-query|8|128|9088|30.2|
|multi-head|1|128|9984|31.2|
|multi-head|2|64|9984|31.1|
|multi-head|4|32|9984|31.0|
|multi-head|8|16|9984|30.9|









## **5 Conclusion** 

We have proposed multi-query attention - an alternative to multi-head attention with much lower memorybandwidth requirements in the incremental setting. We believe that this enables wider adoption of attentionbased sequence models in inference-performance-critical applications.