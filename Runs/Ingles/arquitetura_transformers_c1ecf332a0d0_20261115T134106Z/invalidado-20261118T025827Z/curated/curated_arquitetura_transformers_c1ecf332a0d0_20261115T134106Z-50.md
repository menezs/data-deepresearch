[referencia=d0023c41add26a80 score=0.997]
<!-- Start of picture text -->
Root Mean Square Layer Normalization<br><!-- End of picture text -->

**Biao Zhang**<sup>1</sup> **Rico Sennrich**<sup>2</sup><sup>_,_1</sup> 1School of Informatics, University of Edinburgh 2Institute of Computational Linguistics, University of Zurich 

```
B.Zhang@ed.ac.uk,sennrich@cl.uzh.ch
```

# **Abstract** 

Layer normalization (LayerNorm) has been successfully applied to various deep neural networks to help stabilize training and boost model convergence because of its capability in handling re-centering and re-scaling of both inputs and weight matrix. However, the computational overhead introduced by LayerNorm makes these improvements expensive and significantly slows the underlying network, e.g. RNN in particular. In this paper, we hypothesize that re-centering invariance in LayerNorm is dispensable and propose root mean square layer normalization, or _RMSNorm_ . RMSNorm regularizes the summed inputs to a neuron in one layer according to root mean square (RMS), giving the model re-scaling invariance property and implicit learning rate adaptation ability. RMSNorm is computationally simpler and thus more efficient than LayerNorm. We also present partial RMSNorm, or _pRMSNorm_ where the RMS is estimated from _p_ % of the summed inputs without 

breaking the above properties. Extensive experiments on several tasks using di- 

verse network architectures show that RMSNorm achieves comparable performance against LayerNorm but reduces the running time by 7% _∼_ 64% on different models. Source code is available at `https://github.com/bzhangGo/rmsnorm` .

---

[referencia=d0023c41add26a80 score=0.993]
33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 



<!-- Start of picture text -->
10 10<br>Baseline Baseline<br>9 LayerNorm 9 LayerNorm<br>8 8<br>7.0 7.0<br>7 7<br>6 6 5.9<br>5.4<br>5 5<br>4 4<br>0 20 40 60 80 100 0 20 40 60 80 100 120 140 160<br>Training Step (x 100) Training Time (in minutes)<br>(a) Training loss vs. training steps. (b) Training loss vs. training time.<br>Loss Loss<br><!-- End of picture text -->

Figure 1: Training procedure of a GRU-based RNNSearch [4] for the first 10k training steps. _Baseline_ means the original model without any normalization. When the Baseline training loss arrives at 7.0, the loss of LayerNorm reaches 5.4 after the same number of training steps 1(a), but only 5.9 after the same training time 1(b). 

RMSNorm reduces the amount of computation and increases efficiency over LayerNorm. Despite the simpler formulation, the RMS normalizer helps stabilize the magnitude of layer activations, ensuring invariance to the re-scaling of both weights and datasets. We also show the possibility of estimating RMS on a subset of the summed inputs, maintaining this invariance property. Assuming that the summed inputs have an independent identically distributed structure, we propose partial RMSNorm, where only the first _p_ % summed inputs are utilized for RMS estimation. 

We thoroughly examine our model on various tasks, including machine translation, image classification, image-caption retrieval and question answering. Experimental results show that across different models, RMSNorm yields comparable performance against LayerNorm but shows superiority in terms of running speed with a speed-up of 7% _∼_ 64%. When estimating the RMS with partial (6.25%) summed inputs, _p_ RMSNorm achieves competitive performance compared to RMSNorm.

---

[referencia=d0023c41add26a80 score=0.970]
# **7 Conclusion and Future Work** 

This paper presents RMSNorm, a novel normalization approach that normalizes the summed inputs according to the RMS. RMSNorm preserves the re-scaling invariance property of LayerNorm but eschews the re-centering invariance property which contributes less to the model training. Compared with LayerNorm, models with RMSNorm suffers from less computational overhead. RMSNorm can be easily applied to different model architectures as a drop-in replacement of LayerNorm. Experiments on several NLP tasks show that RMSNorm is comparable to LayerNorm in quality, but accelerates the running speed. Actual speed improvements depend on the framework, hardware, neural network architecture and relative computational cost of other components, and we empirically observed _∼_ speedups of 7% 64% across different models and implementations. Our efficiency improvement come from simplifying the computation, and we thus expect them to be orthogonal to other means of increasing training speed, such as low-precision arithmetic and GPU kernel fusion. We also experimented with _p_ RMSNorm which estimates the RMS on a subset of the summed inputs. While theoretically faster, we did not consistently observe empirical speed improvements for _p_ RMSNorm. We leave it to future work to investigate if the performance can be improved via code optimization. 

In the future, we would like to take more analysis about the success behind RMSNorm. Inspired by recent success of _l_ 1-norm for BatchNorm, we will explore different norms for RMSNorm, and simplify other normalization techniques such as BatchNorm. 

# **Acknowledgments** 

We thank the reviewers for their insightful comments, and Antonio Valerio Miceli Barone for his support with weight normalization for MT. This project has received funding from the grant H2020-ICT-2018-2-825460 (ELITR) by the European Union. Biao Zhang also acknowledges the support of the Baidu Scholarship. This work has been performed using resources provided by the Cambridge Tier-2 system operated by the University of Cambridge Research Computing Service (http://www.hpc.cam.ac.uk) funded by EPSRC Tier-2 capital grant EP/P020259/1. 

9

---

[referencia=d0023c41add26a80 score=0.963]
# **6 Experiments** 

To test the efficiency of layer normalization across different implementations, we perform experiments with Tensorflow [1], PyTorch [20] and Theano [29]. We add RMSNorm to different models, comparing against an unnormalized baseline and LayerNorm. These models are based on diverse architectures, covering different RNN variants, convolutional and self-attentional models, and various activations (such as sigmoid, tanh, and softmax), with initialization ranging from uniform, normal, orthogonal with different initialization ranges or variances. Unless otherwise noted, all speed-related statistics are measured on one TITAN X (Pascal). Reported time is averaged over 3 runs. We also list the standard deviation of these three runs. 

5 

|25<br>re|Model<br>|Test14<br>|Test17<br>|Time<br>|
|---|---|---|---|---|
|20<br>co|Baseline|21.7|23.4|399_±_3.40s|
|15<br>U s<br>Baseline|LayerNorm<br>|22.6<br>|23.6<br>|665_±_32.5s<br>|
|LE<br>LayerNorm|L2-Norm|20.7|22.0|482_±_19.7s|
|10<br> B<br>~~RMSNorm~~|RMSNorm|22.4|**23.7**|501_±_11.8s (24.7%)|
|5<br>alid <br>L2-Norm|_p_RMSNorm|**22.6**|23.1|493_±_10.7s (25.9%)|
|V<br>pRMSNorm|Table 2: Sacre|BLEU sco|re on new|stest2014 (Test14) an|
|0<br>10<br>20<br>30<br>40<br>50<br>Training steps (x30k)<br>0|newstest2017 (<br>version Nematu<br>|Test17) fo<br>s. “_Time_”:<br>|r RNNSe<br>the time i<br>|arch using Tensorfow<br>n second per 1k trainin<br>|

---

[referencia=d0023c41add26a80 score=0.942]
## **6.1 Machine Translation** 

Machine translation aims at transforming a sentence from one (source) language to another (target) language. We focus on neural machine translation based on an attention-enhanced encoder-decoder framework. We train two different models, a GRU-based RNNSearch [4] and a self-attention based neural Transformer [31] on WMT14 English-German translation task. More details about the experimental settings as well as comparison with WeightNorm are listed in Appendix A.1 

We first experiment with RNNSearch. Normalization is added to the recurrent connections and feedforward layers. Apart from RNNSearch without any normalization (Baseline) and with LayerNorm, we also compare against the same model equipped with L2-Norm (i.e. replacing RMS with L2-Norm), which has been observed to improve lexical selection [18]. 

Figure 2 illustrates the evolution of BLEU score on our development set after every 30k training steps, and Table 2 summarizes the test results. In short, both LayerNorm and RMSNorm outperform the Baseline by accelerating model convergence: they reduce the number of training steps until convergence by about 50%, and improve test accuracy, with RMSNorm being comparable to LayerNorm. This supports our hypothesis that re-scaling invariance is the core property of LayerNorm, and that RMSNorm is an effective substitute. Our results with L2-Norm show that it fails to improve the model.<sup>2</sup> Results in Table 2 highlight the challenge that RNN with LayerNorm in Tensorflow suffers from serious computational inefficiency, where LayerNorm is slower than the Baseline by about 67%. In this respect, RMSNorm performs significantly better, improving upon LayerNorm by _∼_ 25%. 

Table 3 further lists translation results of different models implemented in Theano and Pytorch. Overall, RMSNorm yields comparable translation quality compared with LayerNorm but incurs less computational overhead, outperforming LayerNorm with speedups ranging from 11% _∼_ 34%. In addition, we observe that though in theory the amount of computation in _p_ RMSNorm is less than that in RMSNorm, _p_ RMSNorm ( _p_ = 6 _._ 25%) sometimes tends to be slower. We ascribe this to the non-optimal implementation of tensor slicing operation in these computational frameworks, which can be improved with specific low-level coding.

---

[referencia=d0023c41add26a80 score=0.919]
# **2 Related Work** 

One bottleneck deep neural networks have been hypothesized to suffer from is the _internal covariate shift_ issue [27], where a layer’s input distribution changes as previous layers are updated, which significantly slows the training.<sup>1</sup> One promising direction to solve this problem is normalization. Ioffe and Szegedy [12] introduce batch normalization (BatchNorm) to stabilize activations based on mean and variance statistics estimated from each training mini-batch. Unfortunately, the reliance across training cases deprives BatchNorm of the capability in handling variable-length sequences, though several researchers develop different strategies to enable it in RNNs [16, 8]. Instead, Salimans and Kingma [22] propose weight normalization (WeightNorm) to reparameterize weight matrix so as to decouple the length of weight vectors from their directions. Ba et al. [3] propose layer normalization which differs from BatchNorm in that statistics are directly estimated from the same layer without accessing other training cases. Due to its simplicity and effectiveness, LayerNorm has been successfully applied to various deep neural models, and achieves state-of-the-art performance on different tasks [19, 37, 31, 6]. 

These studies pioneer the research direction that integrates normalization as a part of the model architecture. This paradigm ensures encouraging performance by shortening model convergence but at the cost of consuming more time for each running step. To improve efficiency, Arpit et al. [2] employ a data-independent method to approximately estimate mean and variance statistics, thus avoiding calculating batch statistics. Ioffe [11] propose batch renormalization so as to reduce the dependence of mini-batches in BatchNorm. Ulyanov et al. [30] replace batch normalization with instance normalization for image generation. Hoffer et al. [10] and Wu et al. [33] observe that _l_ 1-norm can act as an alternative of variance in BatchNorm with the benefit of fewer nonlinear operations and higher computational efficiency. Nevertheless, all these work still follow the original normalization structure and utilize mean statistic estimated from the whole summed inputs to handle re-centering invariance. 

> 1Note that the internal covariate shift is given as motivation by [12, 3]. Recent studies have proposed alternative explanations for the success of normalization, such as the uncontrollable growth of layer activations in unnormalized deep networks [5]. 

2

---

[referencia=d0023c41add26a80 score=0.907]
# **4 RMSNorm** 

A well-known explanation of the success of LayerNorm is its re-centering and re-scaling invariance property. The former enables the model to be insensitive to shift noises on both inputs and weights, and the latter keeps the output representations intact when both inputs and weights are randomly scaled. In this paper, we hypothesize that the re-scaling invariance is the reason for success of LayerNorm, rather than re-centering invariance. 

We propose RMSNorm which only focuses on re-scaling invariance and regularizes the summed inputs simply according to the root mean square (RMS) statistic: 



Intuitively, RMSNorm simplifies LayerNorm by totally removing the mean statistic in Eq. (3) at the cost of sacrificing the invariance that mean normalization affords. When the mean of summed inputs is zero, RMSNorm is exactly equal to LayerNorm. Although RMSNorm does not re-center 

3 

||Weight matrix<br>re-scaling|Weight matrix<br>re-centering|Weight vector<br>re-scaling|Dataset<br>re-scaling|Dataset<br>re-centering|Single training case<br>re-scaling|
|---|---|---|---|---|---|---|
|BatchNorm|||||||
|WeightNorm|||||||
|LayerNorm|||||||
|RMSNorm|||||||
|_p_RMSNorm|||||||



Table 1: Invariance properties of different normalization methods. “ ” indicates invariant, while “ ” denotes the opposite. 

the summed inputs as in LayerNorm, we demonstrate through experiments that this property is not fundamental to the success of LayerNorm, and that RMSNorm is similarly or more effective.

---

[referencia=d0023c41add26a80 score=0.892]
# **1 Introduction** 

How to train deep neural networks efficiently is a long-standing challenge. To accelerate model convergence, Ba et al. [3] propose the layer normalization (LayerNorm) which stabilizes the training of deep neural networks by regularizing neuron dynamics within one layer via mean and variance statistics. Due to its simplicity and requiring no dependencies among training cases, LayerNorm has been widely applied to different neural architectures, which enables remarkable success on various tasks ranging from computer vision [19, 26], speech recognition [37] to natural language processing [31, 35]. In some cases, LayerNorm was found to be essential for successfully training a model [6]. Besides, the decoupling from batch-based samples endows LayerNorm with the superiority over batch normalization (BatchNorm) [12] in handling variable-length sequences using RNNs. 

Unfortunately, the incorporation of LayerNorm raises computational overhead. Although this is 

negligible to small and shallow neural models with few normalization layers, this problem becomes severe when underlying networks grow larger and deeper. As a result, the efficiency gain from faster and more stable training (in terms of number of training steps) is counter-balanced by an increased computational cost per training step, which diminishes the net efficiency, as show in Figure 

1. One major feature of LayerNorm that is widely regarded as contributions to the stabilization is its re-centering invariance property: the summed inputs after LayerNorm remain intact when the inputs or weight matrix is shifted by some amount of noise. We argue that this mean normalization does not reduce the variance of hidden states or model gradients, and hypothesize that it has little impact on the success of LayerNorm. 

In this paper, we propose root mean square layer normalization (RMSNorm), which regularizes the summed inputs to a neuron in one layer with the root mean square (RMS) statistic alone. 

33rd Conference on Neural Information Processing Systems (NeurIPS 2019), Vancouver, Canada. 



<!-- Start of picture text -->

---

[referencia=d0023c41add26a80 score=0.885]
## **6.3 Image-Caption Retrieval** 

Image-caption retrieval is a cross-modal task aiming at learning a joint embedding space of images and sentences, which consists of two sub-tasks: _image retrieval_ and _caption retrieval_ . The former ranks a set of images according to a query caption, and the latter ranks a set of captions based on a query image. We train an order-embedding model (OE) proposed by Vendrov et al. [32] on the Microsoft COCO dataset [17] using their public source code in Theano. Model details about experimental settings are provides in Appendix A.3. We compare RMSNorm with two models: one without any normalization (Baseline) and one with LayerNorm. 

|Model|Time|
|---|---|
|Baseline|2.11_±_0.047s|
|LayerNorm|12.02_±_0.191s|
|RMSNorm|7.12_±_0.207s (40.8%)|
|_p_RMSNorm|4.34_±_0.168s (63.9%)|



Figure 6 shows the R@K curve on validation set after Baseline 2.11 _±_ 0.047s every 300 training steps, and Table 7 lists the final test results. Across all these metrics, RMSNorm and LayerNorm LayerNorm 12.02 _±_ 0.191s RMSNorm 7.12 _±_ 0.207s (40.8%) consistently outperform the Baseline in terms of model _p_ RMSNorm 4.34 _±_ 0.168s (63.9%) convergence as shown in Figure 6. We observe that on the validation set, RMSNorm slightly exceeds LayerNorm Table 8: Time in seconds per 0.1k training with respect to recall value. For the final test results as steps for the order-embedding model. shown in Table 7, both RMSNorm and LayerNorm improve the model performance, reaching higher recall values (except LayerNorm on R@5) and lower mean rank, though RMSNorm reveals better generalization than LayerNorm. Besides, results in Table 8 show that RMSNorm accelerates training speed by 40% _∼_ 64% compared with LayerNorm, highlighting better efficiency of _p_ RMSNorm.

---

[referencia=d0023c41add26a80 score=0.863]
In _p_ RMSNorm, the partial ratio _p_ directly controls the accuracy of estimated RMS, thereby affecting the stability of model training. Figure 7 shows the effect of _p_ on model performance. Surprisingly, we find that the scale of _p_ has little influence on the final translation quality in RNNSearch: using a small ratio does not significantly degenerate BLEU score. We set _p_ to 6.25% for all following experiments. 

We also experiment with Transformer, which is based on self-attention, avoiding recurrent connections and allowing a higher degree of parallelization. Still, layer normalization is an important part of the architecture. We use an in-house Tensorflow implementation of the Transformer, and employ the base setting as in [31] with all models trained for 300K steps. We treat Transformer with no normalization as our Baseline, and compare RMSNorm-enhanced Transformer with LayerNorm-equipped Transformer. Table 4 shows the results, from which we observe the importance of normalization for Transformer, without which training fails. RMSNorm achieves BLEU scores comparable to LayerNorm, and yields a speedup of 7% _∼_ 9%. Compared with RNNSearch, the relative cost of 

> 2We note that Nguyen and Chiang [18] only applied L2-Norm to the last layer, and treat the scaling factor as a hyperparameter. While not a replication of their experiment, we still found it worth testing L2-Norm as an alternative to LayerNorm. 

6

---

[referencia=d0023c41add26a80 score=0.855]
7 



<!-- Start of picture text -->
1 . 0<br>Baseline<br>0 . 9 BatchNorm-Everywhere Model Time<br>BatchNorm-LSTM<br>0 . 8 LayerNorm Baseline 315 ± 6.30s<br>0 . 7 RMSNormpRMSNorm BatchNorm-Everywhere 348 ± 10.5s<br>BatchNorm-LSTM 345 ± 11.2s<br>0 . 6<br>LayerNorm 392 ± 5.70s<br>0 . 5<br>RMSNorm 333 ± 5.20s (15.1%)<br>0 . 4 0 50 100 150 200 250 300 p RMSNorm 330 ± 5.50s (15.8%)<br>Training steps (x1k) Table 6: Time in seconds per 0.1k training steps for the<br>attentive reader model.<br>5: Error rate on validation set for the<br>attentive reader model.<br>78 90<br>42 77 89<br>40 76 88<br>Baseline 75 Baseline 87 Baseline<br>3836 LayerNormRMSNorm 7473 LayerNorm RMSNorm 86 LaRMSNormyerNorm<br>pRMSNorm 72 pRMSNorm 85 pRMSNorm<br>34 71 84<br>0 50 100 150 200 250 0 50 100 150 200 250 0 50 100 150 200 250<br>Training steps (x0.3k) Training steps (x0.3k) Training steps (x0.3k)<br>(a) Recall@1 (b) Recall@5 (c) Recall@10<br>Figure 6: Recall@K values on validation set for the order-embedding models.<br>rate<br>error<br>Valid<br>Recall@1 Recall@5 Recall@10<br>Mean Mean Mean<br><!-- End of picture text -->

Figure 5: Error rate on validation set for the attentive reader model. 

worse than RMSNorm. Although in Figure 5 the performance of RMSNorm and LayerNorm is comparable, RMSNorm is around 15% faster than LayerNorm as shown in Table 6.<sup>3</sup>

---

[referencia=d0023c41add26a80 score=0.838]
## **4.1 Invariance Analysis** 

Invariance measures whether model output after normalization changes highly in accordance with its input and weight matrix. Ba et al. [3] show that different normalization methods reveal different invariance properties, which contributes considerably to the model’s robustness. In this section, we theoretically examine the invariance properties of RMSNorm. 

We consider the following general form of RMSNorm: 



where _⊙_ denotes element-wise multiplication. Our main results are summarized in Table 1. RMSNorm is invariant to both weight matrix and input re-scaling, because of the following linearity property of RMS: 



where _α_ is a scale value. Suppose the weight matrix is scaled by a factor of _δ_ , i.e. **W**<sup>_′_</sup> = _δ_ **W** , then this change does not affect the final layer output: 



By contrast, if the scaling is only performed on individual weight vectors, this property does not hold anymore as different scaling factors break the linearity property of RMS. Similarly, if we enforce a scale on the input with a factor of _δ_ , i.e. **x**<sup>_′_</sup> = _δ_ **x** , the output of RMSNorm remains through an analysis analogous to that in Eq. 7. We can easily extend the equality to batch-based inputs as well as the whole dataset. Therefore, RMSNorm is invariant to the scaling of its inputs. 

The main difference to LayerNorm is that RMSNorm is not re-centered and thus does not show similar linearity property for variable shifting. It is not invariant to all re-centering operations.

---

[referencia=d0023c41add26a80 score=0.837]
Table 7: Average R@K values across 5 test sets from Microsoft COCO. **R@K** : Recall @ K, higher is better. **Mean r** : mean rank, lower is better. The number in bold highlights the best result.<sup>_‡_</sup> denotes the reproduced results of<sup>_†_</sup> . 

|0_._08<br>Baseline<br>Model|Test Error|Time|
|---|---|---|
|0_._06<br> Rate<br>BatchNorm<br>LayerNorm<br>WeightNorm<br>Baseline<br>BatchNorm|8.96%<br>8.25%|21_±_0.0s<br>38_±_0.0s|
|0_._04<br>Error <br><br>RMSNorm<br>pRMSNorm<br>WeightNorm<br>LayerNorm|8.28%<br>10.49%|23_±_0.0s<br>39_±_0.4s|
|0_._02<br><br>RMSNorm|8.83%|31_±_0.5s (20.5%)|
|000<br>_p_RMSNorm|10.37%|30_±_0.4s (23.1%)|
|0<br>50<br>100<br>150<br>200<br>Training epochs<br>_._<br>Table 10: Test error<br>epoch for the ConvP|rate and tim<br>ool-CNN-C|e in seconds per training<br>model. Time is measured|
|Table 9: Training error rate for the ConvPool-<br>CNN-C model.<br><br>with GeForce RTX 2|080 Ti.||



we also find that layer normalization works worse than BatchNorm and WeightNorm for image processing. Though LayerNorm outperforms Baseline by shorting model convergence, it fails to generalize to the test set, degenerating the test error by 1.53%. In contrast, RMSNorm shows better generalization, surpassing the Baseline by 0.013% and saving about 20.5% training time compared to LayerNorm. _p_ RMSNorm gains further speedup of 2.6%, albeit at the cost of sacrificing test accuracy of 1.54%.

---

[referencia=d0023c41add26a80 score=0.724]
# **5** _p_ **RMSNorm** 

The re-scaling invariance property of RMSNorm ascribes to the linearity property of RMS. Considering that neurons in one layer often have independent identically distributed structure, we argue that the RMS can be estimated on a subset of these neurons rather than all of them. We propose partial RMSNorm ( _p_ RMSNorm). Given the unnormalized input **a** , _p_ RMSNorm infers the RMS statistic 

from first- _p_ % elements of **a** : RMS( **a** ) = � _k_ <u>1 �</u> _ki_ =1<sup>_a_</sup> _i_<sup>2</sup><sup>_,_where</sup><sup>_k_=</sup><sup>_⌈n · p⌉_denotes the number of</sup> elements used for RMS estimation. The linearity property still holds for RMS as in Eq. (6), which indicates _p_ RMSNorm shares the same invariance properties as RMSNorm as shown in Table 1. 

RMS is a biased estimation of the RMS which is often inaccurate. Though theoretically _p_ RMSNorm approximates to RMSNorm, we observe gradient instability where the gradient tends to explode with small _m_ . In practice, however, models with _p_ RMSNorm can succeed in satisfactory convergence with a partial ratio of 6.25%.

---

[referencia=d0023c41add26a80 score=0.723]
the summed inputs as in LayerNorm, we demonstrate through experiments that this property is not fundamental to the success of LayerNorm, and that RMSNorm is similarly or more effective. 

RMS measures the quadratic mean of inputs, which in RMSNorm forces the summed inputs into a _√n_ <u>-scaled unit sphere.</u> By doing so, the output distribution remains regardless of the scaling of input and weight distributions, benefiting the stability of layer activations. Although Euclidean norm which only differs from RMS by a factor of<sup>_√_</sup> _<u>n</u>_ has been successfully explored [22], we empirically find that it does not work for layer normalization. We hypothesize that scaling the sphere with the size of the input vector is important because it makes the normalization more robust across vectors of different size. As far as we know, the idea of employing RMS for neural network normalization has not been investigated before.

---

[referencia=d0023c41add26a80 score=0.676]
|1k training steps, whic<br>V100. “-” indicates <br>model and BLEU scor|h is mea<br> that we <br>e is 0.|sured using Tesla<br> fail to train this|cell in RNNSea<br>_ALL_: the statist<br>bers_1,2,3,4_ind<br>positions.|rch<br>ics av<br>icate|model.  <br>eraged<br>the sta|We use<br>across<br>tistic es|the new<br>all toke<br>timated|stest20<br>n positi<br>for spe|13 dataset.<br>ons. Num-<br>cifc token|



normalization is lower because there are significantly fewer sequential normalization operations in Transformer. 

**Effect of Normalization on Mean and Standard Deviation** Table 5 shows the distribution of mean and standard deviation of hidden representations across token positions for an RNNSearch model. Mean and standard deviation are unstable in the baseline, as observed by Ba et al. [3]. Due to their normalization properties, both RMSNorm and LayerNorm stabilize standard deviation. Although the mean in RMSNorm is not normalized, in practice it is more stable than the mean of the baseline. This supports our hypothesis that RMSNorm stabilizes recurrent activations without the need to explicitly normalize the mean. 

**On the Robustness of RMSNorm** One remaining question is whether the re-centering operation in LayerNorm (which RMSNorm abandons) makes models more robust towards arbitrary weight/bias initializations. We perform an experiment on RNNSearch with Nematus in Tensorflow, and change the center of weight initialization to 0.2. Results in Figure 4 show that LayerNorm becomes very unstable with abnormal initialization, but RMSNorm is more robust (both underperform the original initialization). Our empirical evidence so far suggests that RMSNorm is similarly robust as LayerNorm, or more. 



<!-- Start of picture text -->
25<br>LayerNorm<br>20<br>RMSNorm<br>15<br>10<br>5<br>0<br>0 5 10 15 20 25 30<br>Training steps (x30k)<br>score<br>BLEU<br>Valid<br><!-- End of picture text -->

Figure 4: SacreBLEU score curve of LayerNorm and RMSNorm on newstest2013 (devset) when the initialization center is 0.2.

---

[referencia=d0023c41add26a80 score=0.671]
## **A.3 Image-Caption Retrieval** 

In OE model, sentences are encoded through a GRU-based RNN [7] and images are represented by the output of a pretrained VGGNet [28]. OE treats the caption-image pairs as a two-level partial order, and trains the joint model using the pairwise ranking loss [14]. 

We adopt the _10crop_ feature from VGGNet as image representation, and set word embedding size and GRU hidden size to be 300 and 1024 respectively. Xiavier, Gaussian and Ortogonal initialization are used for different model parameters. All models are trained with Adam optimizer, with a batch size of 128 and learning rate of 1 _e_<sup>_−_3</sup> . We employ Recall@K (R@K) values for evaluation, and report averaged results on five separate test sets (each consisting of 1000 images and 5000 captions) as our 

4Sacrebleu hash: BLEU+case.mixed+lang.en-de+numrefs.1+smooth.exp+test.wmt14+tok.13a+version.1.2.12 and BLEU+case.mixed+lang.en-de+numrefs.1+smooth.exp+test.wmt17+tok.13a+version.1.2.12. 

5Note that there are minor differences between different frameworks, both in implementation details and setup, explaining performance differences between the baselines. 

13 

## **A.4** 

We apply layer normalization to the width and height dimensions of image representation, and perform gain scaling and bias shifting on the channel dimension. We train all models using Adam optimizer with a batch size of 100. Learning rate is set to 0.0003 for Baseline and 0.003 for others following [22]. We set _p_ to 12.5% for _p_ RMSNorm, considering the small model size in this task. 

14

---

[referencia=d0023c41add26a80 score=0.532]
2 

Different from these related work, the proposed RMSNorm modifies the normalization structure by removing the re-centering operation and regularizing the summed inputs with RMS alone. Our model only maintains the re-scaling invariance property which we find can be inherited when the RMS is estimated from only subset of the summed inputs, partially inspired by the group normalization [34]. As a side effect, our model reduces the computational overhead and increases efficiency. Recently, Zhang et al. [36] show that with careful initialization, residual networks can be trained as stable as those with normalization. However, the approach mainly aims at improving residual networks and can not be freely switched without modifying all initialization layers. Besides, it is not trivial to be adapted to other general neural networks, such as RNNs where model depth expands along the variable sequence length. By contrast, our model is simple, effective and can be used as a drop-in replacement of LayerNorm.

---

[referencia=d0023c41add26a80 score=0.508]
## **6.2 CNN/Daily Mail Reading Comprehension** 

This reading comprehension task is a cloze-style question 

answering task, where models are required to answer a question regarding to a passage, and the answer is an anonymized entity from the passage [9]. We train a bidirectional attentive reader model proposed by Hermann et al. [9] on the CNN corpus. More details about the experimental settings are given in Appendix A.2. We compare RMSNorm with both LayerNorm and BatchNorm. 

Figure 5 and Table 6 show the results. After normalizing RNN by BatchNorm with separate statistics for each time step in a sequence, both BatchNorm-LSTM and BatchNorm-Everywhere help speed up the convergence of training process. By contrast, LayerNorm and RMSNorm not only converge faster than BatchNorm, but also reach lower validation error rate, though _p_ RMSNorm performs slightly 

7 



<!-- Start of picture text -->

---

[referencia=d0023c41add26a80 score=0.476]
## **A.1 Machine Translation** 

We experiment on the WMT14 English-German translation task, where the training corpus consists of 4.5M aligned sentence pairs. We use newstest2013 as the development set for model selection, newstest2014 and newstest2017 as the test set. We evaluate translation quality with case-sensitive detokenized BLEU score reported by _sacrebleu_ [21]<sup>4</sup> . Byte pair encoding algorithm is applied to reduce out-of-vocabulary tokens with 32k merge operations [24]. All models are trained based on maximum log-likelihood relaxed by label smoothing with a factor of 0.1.<sup>5</sup> 

For RNNSearch, we select training samples with maximum source/target length of 80. We set the embedding size and hidden size to be 512 and 1024, respectively. We apply Adam [13] to tune model parameters, with learning rate of 1 _e_<sup>_−_4</sup> and batch size of 80. We initialize weight parameters with standard normal distribution scaled by 0.01, except for square weight parameters which are handled with random orthogonal matrix. 

For Transformer, we adopt the base setting as in [31]. We set the model size and FFN hidden size to be 512 and 2048, respectively, and use 8 attention heads. The learning rate is scheduled according to the inverse square root of running steps, with warmup steps of 4000. We organize each batch with 25000 source/target tokens, and train the model using Adam ( _β_ 1 = 0 _._ 9 _, β_ 2 = 0 _._ 98) [13]. We apply Xavier initialization to all weight parameters. 

We also compare our model with WeightNorm. We perform experiments with RNNSearch using the WeightNorm implementation provided by Theano-version Nematus. Results in Figure 7 show that WeightNorm converges slower and requires more training steps. In addition, the overall translation quality of WeightNorm on testsets (21 _._ 7 _/_ 23 _._ 5 on Test14/Test17, respectively) underperforms those of LayerNorm and ( _p_ )RMSNorm. We also attempted integrating WeightNorm into pytorch-based RNNSearch using the official API ( _nn.utils.weight_norm_ ), but this led to out-ofmemory problems.