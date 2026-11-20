[referencia=128e7e40ab379185 score=0.084]
## 2 Related Works

Emergence and phase transitions.
Following Steinhardt (2022) & Wei et al. (2022),
*emergence* refers to a qualitative change in a learning system resulting from an increase of model size, training data or training steps, where *phase transitions* are additionally characterized by a sharp change. Eureka-moments are special types of phase transitions.
While recent work showed that sharp emergence may just be an artifact of the choice of a discontinuous metric (Schaeffer et al., 2024; Srivastava et al., 2023), we observe rapid changes also for continuous metrics in our setting.
A connection between phase transitions or emergence and our work may exist, and both may be related to escaping bad energy landscapes as in our work.

Unexplained phase transitions. Previous works reported observations that may be Eureka-moments, without investigating their cause. For instance, rapid improvements happen for in-context-learning (ICL) (Olsson et al., 2022), diffusion model training (Zhang et al., 2023) and BERT training (Gupta & Berant, 2020; Deshpande & Narasimhan, 2020; Nagatsuka et al., 2021; ano, 2023; Chen et al., 2024). Deshpande & Narasimhan (2020) proposed to bias the attention mechanism towards predefined attention patterns and observed speed-ups in BERT training, while Chen et al. (2024) connect the sharp drop to sudden learning of syntactic attention structures. We also identify the learning of the task-required attention pattern to be the cause of the problem. In concurrent work Reddy (2023) studied phase transitions in ICL. Specifically, they show for a small toy-model that slow initial learning is due to a saddle-point, where one path leads to a sub-optimal minimum (i.e., random context label) and the other path to the ICL solution. They discover a “cliff” in the loss landscape and shallow gradients that lead to the ICL solution. While our setting shows substantial differences, our analysis reveals the same underlying mechanisms, i.e., shallow gradients, which we investigate in more detail.

---

[referencia=128e7e40ab379185 score=0.053]
### 5.3 Is This an Artificial Problem Caused by Other Factors?

Does the transformer simply ignore specific indicator locations? The task and dataset used in the previous subsections showed indicators and targets always at the same location, i.e., indicators on top-left and bottom right. Such a dataset design might result in two undesired effects: 1) The transformer might learn to ignore features based on the associated positional embeddings. 2) The task might be easier, since positional embeddings can be used as shortcut to find indicators without the need to rely on the actual features. To disprove both cases we create another dataset, explained in Fig. 7. We observe that removing the fixed position for indicators and targets makes the task even more difficult (Tab. 1 bottom) and differences between methods are even more apparent. Thus, ViTs without Eureka-moment do not simply learn to ignore regions of the image.

Is this a mere artifact of a bad choice of hyper-parameters?

*main dataset*. Both interventions, ViT+HT and NormSoftmax drastically reduce the saturation period and can even lead to a complete disappearance of the saturation period.

*No position task*description. This task is identical to the

*main task*, but removes more information by swapping indicator (digit) and target (fashion) in each row with a probability of 0.5, i.e., task 2 is to classify either the top or bottom fashion sample. Two samples are shown to highlight differences from the task described in Fig. .

We test various competing explanations that could lead to the observed phenomenon, like training instabilities due to inadequate Warmup, bad choice of learning rate schedules and Weight Decay to force circuit formation as observed for grokking (Nanda et al., 2023). Weight Decay and Warmup do not improve the results. We find that Eureka-moments are sensitive to the learning rate. NormSoftmax and HT reduce the sensitivity to sub-optimal learning rates drastically (see Tab. 2). See A.5 for a more detailed answer to the posed question.

Influence of model scale, dataset size and image resolution on Eureka-moments. We found no consistent influence of model scale on Eureka-ratio. See A.6 for more details. Further, we can rule out that this observation is an artifact of image resolution or dataset size by showing the phenomenon on a ImageNet-100 based dataset in A.10.

---

[referencia=128e7e40ab379185 score=0.034]
- Power et al. (2022)
Power, A., Burda, Y., Edwards, H., Babuschkin, I., and Misra, V.
Grokking: Generalization beyond overfitting on small algorithmic
datasets.
*arXiv preprint arXiv:2201.02177* , 2022.
- Radford et al. (2019)
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al.
Language models are unsupervised multitask learners.
*OpenAI blog* , 1(8):9, 2019.
- Reddy (2023)
Reddy, G.
The mechanistic basis of data dependence and abrupt learning in an
in-context classification task.
In *The Twelfth International Conference on Learning
Representations* , 2023.
- Schaeffer et al. (2024)
Schaeffer, R., Miranda, B., and Koyejo, S.
Are emergent abilities of large language models a mirage?
In *Advances in Neural Information Processing Systems* ,
volume 36, 2024.
- Shen et al. (2023)
Shen, K., Guo, J., Tan, X., Tang, S., Wang, R., and Bian, J.
A study on relu and softmax in transformer.
*arXiv preprint arXiv:2302.06461* , 2023.
- Shoeybi et al. (2019)
Shoeybi, M., Patwary, M., Puri, R., LeGresley, P., Casper, J., and Catanzaro,
B.
Megatron-lm: Training multi-billion parameter language models using
model parallelism.
*arXiv preprint arXiv:1909.08053* , 2019.

---

[referencia=128e7e40ab379185 score=0.011]
| ViT+HT |  | 1/4 | 88.36 | 242 | 
| NormSoftmax + HT |  | 1/4 | 90.63 | 19 | 

Does the transformer fail to combine the information? We observe that the target location (solution of task 1) cannot be inferred by the linear probe (Fig. ). Therefore, even though the (indicator) information is available, it is not able to utilize this information to predict the target location of task 2. Thus, the transformer has all the information but fails to combine it to solve the multi-step task.

Differences to a transformer that had a Eureka-moment. Fig. shows the linear probe results for a transformer that had a Eureka-moment. Interestingly, the target location can be inferred by linear probes from all layers and all tested representations with high accuracy. This is in stark contrast to transformers that had no Eureka-moment. The second striking difference is that indicator information is represented in the CLS token. This is even stronger for early layers (Fig. 19). We suspect, that the transformer uses the CLS token to match the classes of the indicators.

Why does the transformer fail to combine the information? We visualize the attention maps of two fully trained ViTs in Fig. 3. We find that the transformer without Eureka-moment does not attend the indicator digits and attends only the targets of task 2, whereas a transformer with Eureka-moment attends the indicator digits in early layers. This suggest that a ViT without Eureka-moment does not pay enough attention to the indicators to match them and struggles to learn to attend different regions.

| Model | Eureka-ratio | 
|---|---|
| ViT | 04/36 | 
| VIT + Warmup 20 | 14/36 | 
| grad scaling | 5/36 | 
| NormSoftmax | 36/36 | 
| ViT | 20/36 | 
| ViT+HT | 25/36 |

---

[referencia=128e7e40ab379185 score=0.011]
| ViT |  | 10/10 | 89.35 0.28 | 66.60 58.55 | 36.71 | 10/10 | 
| ViT+HT |  | 10/10 | 89.81 0.29 | 74.00 61.29 | 39.88 | 10/10 | 
| NormSoftmax + HT |  | 10/10 | 89.83 0.41 | 17.50 04.84 | 16.41 | 10/10 | 

|  |  | No Position Task |  |  | 
|---|---|---|---|---|
|  |  |  | Avg. over EMs |  | 
| Model |  | ER | Acc. | Avg. EE. | 
| ResNet |  | 4/4 | 91.27 0.30 | 4.25 00.43 | 
| ViT |  | 0/4 | - | - | 
| ViT + Warmup 20 |  | 1/4 | 89.55 0.00 | 117 00.00 | 
| grad scaling |  | 0/4 | - | - | 
| NormSoftmax |  | 3/4 | 88.98 0.55 | 228.67 08.22 | 
| NormSoftmax |  | 1/4 | 89.77 0.00 | 20.00 00.00 | 
| ViT |  | 1/4 | 89.68 0.00 | 191.00 00.00 | 
| ViT+HT |  | 1/4 | 88.36 0.00 | 242.00 00.00 | 
| NormSoftmax + HT |  | 1/4 | 90.63 0.00 | 19.00 00.00 | 
| ViT 6 heads, depth 4 |  | 0/0 | - | - | 

Due to space and readability constraints we report in the main paper only the mean over all seeds. In Tabs. 4 & 5 we show the same tables including the standard deviation.

---

[referencia=128e7e40ab379185 score=0.007]
1. 1. 
In general, the gradients are not evenly divided between target and indicator , with usually smaller gradient for the indicator regions. Therefore Fig. 4 even underestimates the difference for the indicator regions, i.e., the regions relevant for a Eureka-moment.
2. 2. 
This difference can explain why more time is needed to reach a Eureka-moment for ViT in comparison to the other methods.
3. 3. 
This difference between indicator and target can also explain, why the grad scaling does not solve the problem.
4. 4. 
For ViT the difference between gradients of “” and ” and “” and ”” is, for most layers, generally much larger compared to the other approaches. This is particularly true before the Eureka-moment, where larger gradients for indicator and indicator are crucial to get an early Eureka-moment. Most prominent is the difference between target and indicator , showing a large mismatch. This explains, why the attention maps change so slowly and why simply increasing the learning rate does not solve the problem.

### A.3 Gradient Norm

Fig. 14 shows the L1 gradient norm for all layers and all methods. It can be seen, that throughout all layers and the entire training ViT has larger gradients for in comparison to and . For the other methods differences are much smaller and less consistent.

### A.4 Why Gradient Magnitude Scaling Does Not Work.

Following the observation of Fig. 4, it stands to reason to simply scale the gradients for , and to the same value. To this end, we compute the gradient norm for , and for each layer and the overall mean. We scale the gradients for , and , such that their norm is equal to the mean norm. This removes the imbalanced gradient issue and results in identical effective learning rate.

While this approach might work, it solves only part of the problem. Different features might receive differently large gradients. For instance the indicator features (here digits) receive little gradient, while target (here fashion) receive large gradients, as can be seen in Fig. 11. Simply scaling up the gradients would not solve the imbalance between indicator and target gradients.

---

[referencia=128e7e40ab379185 score=0.006]
Why does the transformer fail to learn to attend to the indicators? Based on the discussion in Sec. 3, we hypothesize that ill-distributed attention scores lead to small gradients for and , which in turn inhibit learning and in particular learning to shift attention towards the indicators. Note that high attention to some pairs with low attention to all others or uniformly distributed attention can result in vanishing gradients (Noci et al., 2022). To test this, we visualize the L1-norm of the gradient of the first layer in Fig. 4. For vanilla ViT the gradients for and are 0.5-1 orders of magnitude smaller than those for . Thus, only small gradients are backpropagated through the Softmax to and , and the attention map improves only slowly, which results in the observed slow learning. Differences between the gradients are much smaller for ViT , ViT+HT and NormSoftmax, in particular before the Eureka-moment. Fig. 5 shows the origin of gradients on the image plane for . For ViT, the gradients mostly originate from the target regions, which further explains why many steps are needed to move attention to the indicators, as these gradients only lead to improved target recognition.

Is too small or too large attention-entropy the problem? We visualize the distribution of attention maps over training in Fig. 10: the vast majority of attention scores is very small. This indicates that a too uniform attention is causing small gradients. Larger attentions are rare, but not absent, as can be seen in Fig. , but indicator regions have small and uniform attention. Thus, we conclude that local uniform attention causes the transformer’s learning problems.

---

[referencia=128e7e40ab379185 score=0.005]
Due to space and readability constraints we report in the main paper only the mean over all seeds. In Tabs. 4 & 5 we show the same tables including the standard deviation.

Lastly, for Tab. 4 we report the improved convergence speed as a percentage of the number of training steps to reach 95% of ViT accuracy (averaged only over seeds with Eureka-moments), denoted as “% of steps”. This value is computed only over the fraction of seeds, that actually lead to a higher accuracy than 95% of ViTs accuracy. In the last column, we also report this fraction. Note, that the Eureka-ratio is the maximum possible value for the “95%-ratio”, i.e., for “ViT +Warmup 20” 8/10 seeds have a Eureka-moment. Out of these 8 only 5 reach an accuracy higher than 95% of the ViT accuracy.

---

[referencia=128e7e40ab379185 score=0.004]
|  |  | Main Dataset |  |  |  |  | 
|---|---|---|---|---|---|---|
|  |  |  | Avg. over EMs |  | Avg. over ViT 95% Acc. |  | 
| Model |  | ER | Acc. | Avg. EE. | % of steps | 95%-ratio | 
| ResNet |  | 10/10 | 99.40 0.10 | 3.00 00.00 | - | - | 
| ViT |  | 3/10 | 89.40 0.08 | 174.67 37.82 | 84.26 | 3/10 | 
| ViT |  | 6/10 | 90.13 0.40 | 181.34 24.94 | 86.79 | 2/10 | 
| ViT + WD 0.5 |  | 5/10 | 90.09 0.27 | 177.80 52.30 | 84.70 | 5/10 | 
| ViT |  | 7/10 | 89.48 1.10 | 207.43 46.65 | 100.00 | 4/10 | 
| ViT + Warmup 20 |  | 8/10 | 87.65 6.48 | 205.87 57.05 | 91.87 | 5/10 | 
| grad scaling |  | 10/10 | 87.96 2.45 | 119.4 62.70 | 73.79 | 5/10 | 
| NormSoftmax |  | 10/10 | 89.56 0.65 | 28.20 34.85 | 19.87 | 10/10 | 
| NormSoftmax |  | 10/10 | 89.18 0.36 | 23.50 08.15 | 19.25 | 10/10 | 
| ViT |  | 10/10 | 89.35 0.28 | 66.60 58.55 | 36.71 | 10/10 |

---

[referencia=128e7e40ab379185 score=0.004]
| Main Dataset |  |  |  |  | 
|---|---|---|---|---|
|  |  |  | Avg. over EMs |  | 
| Model |  | ER | Acc. | Avg. EE. | 
| ViT |  | 3/10 | 89.40 | 174.67 | 
| ViT |  | 6/10 | 90.13 | 181.34 | 
| ViT + WD 0.5 |  | 5/10 | 90.09 | 177.8 | 
| ViT |  | 7/10 | 89.48 | 207.43 | 
| ViT + Warmup 20 |  | 8/10 | 87.65 | 205.87 | 
| grad scaling |  | 10/10 | 87.96 | 119.4 | 
| NormSoftmax |  | 10/10 | 89.56 | 28.2 | 
| NormSoftmax |  | 10/10 | 89.18 | 23.5 | 
| ViT |  | 10/10 | 89.35 | 66.6 | 
| ViT+HT |  | 10/10 | 89.81 | 74.0 | 
| NormSoftmax + HT |  | 10/10 | 89.83 | 17.5 | 
| No Position Task |  |  |  |  | 
| ViT |  | 0/4 | - | - | 
| ViT + Warmup 20 |  | 1/4 | 89.55 | 117 | 
| grad scaling |  | 0/4 | - | - | 
| NormSoftmax |  | 3/4 | 88.98 | 228 | 
| NormSoftmax |  | 1/4 | 89.77 | 20 | 
| ViT |  | 1/4 | 89.68 | 191 | 
| ViT+HT |  | 1/4 | 88.36 | 242 | 
| NormSoftmax + HT |  | 1/4 | 90.63 | 19 |

---

[referencia=128e7e40ab379185 score=0.003]
## 3 Background

Preliminaries. This work investigates the popular dot product attention (Vaswani et al., 2017), defined as

|  |  |  | (1) | 

where the weight matrices , and map the input to query , key , value , and the temperature parameter controls the entropy of the output. A low temperature leads to low entropy, i.e., a more “peaky” distribution. Commonly, is set to , where is the dimensionality of and . Thus, is the standard deviation of under the independence assumption of rows of and with 0 mean and variance of 1 (Vaswani et al., 2017).

Softmax attention can cause vanishing gradients. Attention entropy collapse, i.e., too centralized attention, can cause vanishing gradients (Zhai et al., 2023; Shen et al., 2023), since all entries of the Jacobian of the Softmax will become almost 0 (see . A.11). Similarly, uniform attention can cause vanishing gradients for and (Noci et al., 2022).

A remedy to both problems is to control the attention temperature . A larger in the Softmax will dampen differences of and by that prevent vanishing gradients by low attention entropy. In contrast, a smaller will amplify differences of and prevents vanishing gradients caused by uniform attention. Choosing the right temperature is difficult and can have a strong influence on what the model learns, how fast it converges etc. As a remedy, we propose to start training with a low temperature and follow a schedule to heat it up to the default value of . We refer to this approach as Heat Treatment (HT) and it is one of our interventions to test whether the Softmax is indeed the root cause of the optimization difficulties. This approach has multiple advantages. First, it removes the difficulty of choosing the exact temperature. Second, the network gets optimized for “more peaky” attention, but the temperature increases steadily. By that, the network starts with centralized attention but since the next epochs attention will be more uniform than the previous (due to increasing the temperature), it does not run into the issue of low attention entropy. Last, the network can focus on most important features early in training and broaden the view over time, attending to other features.

---

[referencia=128e7e40ab379185 score=0.003]
### A.9 Description of and Results on More Datasets

In the following we report results on 5 more datasets. The datasets are depicted in Fig. 16.

Cifar task 1. A schematic for this task is shown in Fig. 16(a). The “Cifar task 1” dataset uses Cifar-10 (Krizhevsky et al., 2009) images of classes “automobile” and “bird” as indicators. Targets are sampled from fashion MNIST and MNIST. All 4 images are randomly placed on a 4x4 canvas and we apply random colors (red or blue) to the MNIST and fashion MNIST samples. Task 1 is to compare the Cifar-10 classes. If they come from the same class, task 2 is to classify the MNIST digit. If not, the tasks is to classify the fashion MNIST sample. Results are reported in Tab. 6. normal ViT fails in 1/4 cases and Eureka-epoch is usually late. Note, that this task may seem difficult, but differences in color distribution of “bird” and “automobile” simplify the task.

|  |  | Cifar task 1 |  |  | 
|---|---|---|---|---|
|  |  |  | Avg. over EMs |  | 
| Model |  | ER | Acc. | Avg. EE. | 
| ViT |  | 3/4 | 83.43 1.83 | 187.67 42.46 | 
| ViT |  | 4/4 | 86.86 0.75 | 76.50 08.90 | 
| NormSoftmax |  | 4/4 | 82.89 0.31 | 100.0 27.89 |

---

[referencia=128e7e40ab379185 score=0.003]
- ano (2023) Escaping the plateau: Dynamic context length adaptation for efficient bert pretraining. 2023. URL https://openreview.net/forum?id=urzQrPofiMM. Anonymous review.
- Ali et al. (2021)
Ali, A., Touvron, H., Caron, M., Bojanowski, P., Douze, M., Joulin, A., Laptev,
I., Neverova, N., Synnaeve, G., Verbeek, J., et al.
Xcit: Cross-covariance image transformers.
*Advances in neural information processing systems* ,
34:20014–20027, 2021.
- Baevski & Auli (2019)
Baevski, A. and Auli, M.
Adaptive input representations for neural language modeling.
In *International Conference on Learning Representations* , 2019.
URL https://openreview.net/forum?id=ByxZX20qFQ.
- Barak et al. (2022)
Barak, B., Edelman, B., Goel, S., Kakade, S., Malach, E., and Zhang, C.
Hidden progress in deep learning: Sgd learns parities near the
computational limit.
*Advances in Neural Information Processing Systems* , 2022.
- Chan et al. (2022)
Chan, S., Santoro, A., Lampinen, A., Wang, J., Singh, A., Richemond, P.,
McClelland, J., and Hill, F.
Data distributional properties drive emergent in-context learning in
transformers.
*Advances in Neural Information Processing Systems* ,
35:18878–18891, 2022.
- Chen et al. (2024)
Chen, A., Shwartz-Ziv, R., Cho, K., Leavitt, M. L., and Saphra, N.
Sudden drops in the loss: Syntax acquisition, phase transitions, and
simplicity bias in MLMs.
In *The Twelfth International Conference on Learning
Representations* , 2024.
URL https://openreview.net/forum?id=MO5PiKHELW.

---

[referencia=128e7e40ab379185 score=0.002]
### A.16 Experimental Setup – reasoning task

The input of the model is of the form “a b c d =“, where, where . In our experiments, we set . We train the transformer on 30% of the entire set of possible inputs (i.e., input combinations), that is with a batch size of 4392. The rest is used as test set. We train for 10 000 epochs over five random seeds. We use token embeddings of size of , four attention heads of dimension of , hidden units in the MLP, and learned positional embeddings.

We trained with full batch gradient descent using AdamW (Loshchilov & Hutter, 2019) with a cross-entropy loss. We optimized learning rates via grid search over on seed 0. Following Nanda et al. (2023) we use a weight decay of 1.

### A.17 Slingshot Effects on Reasoning Task

We observed that NormSoftmax caused slingshot effects (Thilak et al., 2022) during the convergence phase of some of the training runs but believe this may be due to the interaction of gradients at different scales with adaptive optimizers (Nanda et al., 2023). Since slingshot effects only occur after Eureka-moments, they cannot be the cause for their occurrence. We did not further investigate this observation.

### A.18 Experimental Setup – RoBERTa

The RoBERTa experiments are based on the Code provided by (Deshpande & Narasimhan, 2020). We follow the data acquisition and preparation strategy of (Shoeybi et al., 2019). Thus, we train on the latest Wikipedia dump (downloaded on the 2<sup>nd</sup> of August 2023). We train a 12 layer RoBERTa model with 12 heads. We use a batch size of 84 and a learning rate of 5e-5.

---

[referencia=128e7e40ab379185 score=0.002]
### A.5 Are the Learning Problems a mere Artifact of a Bad Choice of Hyper-parameters?

We always use the default of 5 Warmup epochs to avoid training instabilities during early stages of training. We found that 20 Warmup epochs were most effective in mitigating the problem. However, sensitivity to the learning rate schedule (Tab. 2) is high. The average Eureka-epoch is very late (Tab. 1 left) and we found more Warmup epochs lead to worse results on harder tasks (Tab. 1 right). The Eureka-ratio is sensitive to the learning rate schedule. We test 9 learning rate schedules for each method, (Tab. 11). Lower temperatures are less sensitive to the learning rate schedule (see Tab. 2).

Weight Decay (WD) can facilitate grokking (Power et al., 2022) by forcing the network to learn general mechanisms (Power et al., 2022; Nanda et al., 2023). In our setting, we only found mild improvements for higher WD. However, more random seeds revealed, that higher WD rather reduces the Eureka-ratio (Tab. 1) and does not help in solving transformer’s learning issue.

---

[referencia=128e7e40ab379185 score=0.002]
### A.6 Influence of Model Scale on Eureka-ratio.

The low Eureka-ratio could also be due to a too large or too small architecture. Also the number of heads might play an important role, since different features can be attended in different heads. More heads might increase the likelihood of one head specializing in indicators. Also the embedding dimension per head might just be too small or large for the task at hand. Maybe, even the hidden dimension of the MLP at the end of the attention block is the bottleneck. Many parameters of the transformer itself could explain why it fails to solve our tasks. We test these hypotheses in Tab. 3. While most changes lead to a lower Eureka-ratio, reducing the depth and increasing the number of heads leads to mild improvements. Combining both leads to a Eureka-ratio of 4/4, but, as can be seen in Tab. 5, this architecture does not generalize to other datasets.

---

[referencia=128e7e40ab379185 score=0.002]
### A.8 Main Results with Standard Deviation, ResNet and Convergence Speed Improvements

---

[referencia=128e7e40ab379185 score=0.002]
## 1 Introduction

A key quality of any intelligent system is its ability to deal with complex problems that may consist of multiple sub-problems. It should learn to solve these sub-problems even in the absence of direct feedback. Deep learning has enabled such capabilities to a certain degree. For example, deep classifiers learn the hierarchical feature representations necessary to build a good classifier. Reinforcement learning learns object representations required to predict how to receive a sparse reward. Language models group tokens to derive their contextual meaning and then predict a new token. In-context learning (ICL) tasks require to first learn similarities and then associate tokens based on positional information by learning induction heads (Olsson et al., 2022). While aforementioned examples show great promise, researchers spend a large effort on designing the training process to learn sub-tasks. For instance, reward shaping is common in reinforcement learning, many computer vision works use explicit or implicit intermediate supervision, while for language modelling and ICL a good data arrangement plays an important role (Chan et al., 2022). For some of these problems, a saturation of the learning process followed by a sudden improvements can be observed, as shown in Fig. . However, the relation of implicit multi-step learning to saturation of the learning process followed by abrupt improvements in training loss has not been investigated.

---

[referencia=128e7e40ab379185 score=0.002]
## Appendix A Appendix

Here, we provide additional information that supports understanding and helps interpreting the main paper. We provide supplemental experimental results and more detailed analysis. We show the gradient norm for indicators and targets individually, which reveals that most of the already small gradients for and is attributed to target features for models that do not learn the task and very little to indicator features. We provide a more complete version of Fig. 4. Provide more insights into why gradient magnitude scaling does not work and provide more details on our analysis of competing hypotheses. We provide an ablation on model scale and the main results from the main paper with standard deviation and training speed up. We explain additional datasets and report results on them. We repeat the linear probe analysis with more sensitive information probes. We provide the linear probe plots using also , and representations and the full version of Fig. 4. Last, we provide details on training and experimental setups and an explanation for vanishing gradients in case of centralized attention maps.

### A.1 Attention Distribution Over Time

We show the change of the attention distribution during the course of training in Fig. 11

---

[referencia=128e7e40ab379185 score=0.002]
Can the problem be fixed by rescaling of the gradient magnitude for ,  and ?
The observation that lower gradient imbalance leads to higher Eureka-ratio suggests, that simply rescaling of the gradients may solve the problem.
We find that this does work for the *Main task* but not for the *No position task*, (see Tab. 1) and is very sensitive to the learning rate (see Tab. 2).
We attribute this to the differences in gradient magnitudes for indicators and targets and discuss it further in Sec. A.4.

Do gradients vanish completely and can transformers recover? Fig. already suggests, that one potential solution to reliably get Eureka-moments is very long training. This observation is supported by Fig. 4, which indicates that gradients become small, but not 0. Indeed we observe that training for 3000 epochs results in a Eureka-ratio of 4/4 for all the learning rate schedules. In practice, this is of little help because the number of sub-tasks is unknown and Eureka-moments are hard to predict.

Is this truly a transformer optimization problem?

To show that Eureka-moments are general to all transformers and not just artifacts of vision data, we also show their occurrence in single-layer 4 head transformers on simplistic algorithmic tasks, referred to as the reasoning task (Sec. 4). Here, features (numbers) are directly provided as tokens and need not be extracted. Fig. 8 reveals that Eureka-moments appear even in this minimal setting. Both HT and NormSoftmax reduce the training steps required for Eureka-moments to occur and increase the Eureka-ratio from 3/5 to 4/5 or 5/5, respectively.

Does the NormSoftmax intervention translate to real data? Jiang et al. (2023) reported improved performance and faster convergence on ImageNet and machine translation tasks using NormSoftmax. Both tasks likely contain some innate multi-step tasks, e.g., identifying a common discriminative feature and then discriminating between the difficult classes for ImageNet. These improvements may be due to easier multi-step learning with NormSoftmax.