[referencia=128e7e40ab379185 score=0.978]
Temperature in Softmax. A key operation in the transformer is the scaled dot-product attention. Large products can lead to attention entropy collapse (Zhai et al., 2023; Shen et al., 2023), which results in very small gradients. In contrast, Chen et al. (2023) observed close to uniform attention over tokens. They scaled down very low scores further while amplifying larger scores, but this only amplified the problem when important tokens are already ignored. Instead, Jiang et al. (2023) proposed to normalize the dot product. Their proposed NormSoftmax avoids low variance attention weights and thus avoids the small gradient problem. We found it as the most effective intervention on the Softmax function. Others proposed to learn the temperature parameter (Dufter et al., 2020; Ali et al., 2021), but this is difficult to optimize. For very large models the problem becomes more severe. Models with more than 8B parameters show attention entropy collapse (Dehghani et al., 2023). They followed (Gilmer et al., 2023) and normalized the with layer norm before the Softmax.

---

[referencia=128e7e40ab379185 score=0.889]
## 3 Background

Preliminaries. This work investigates the popular dot product attention (Vaswani et al., 2017), defined as

|  |  |  | (1) | 

where the weight matrices , and map the input to query , key , value , and the temperature parameter controls the entropy of the output. A low temperature leads to low entropy, i.e., a more “peaky” distribution. Commonly, is set to , where is the dimensionality of and . Thus, is the standard deviation of under the independence assumption of rows of and with 0 mean and variance of 1 (Vaswani et al., 2017).

Softmax attention can cause vanishing gradients. Attention entropy collapse, i.e., too centralized attention, can cause vanishing gradients (Zhai et al., 2023; Shen et al., 2023), since all entries of the Jacobian of the Softmax will become almost 0 (see . A.11). Similarly, uniform attention can cause vanishing gradients for and (Noci et al., 2022).

A remedy to both problems is to control the attention temperature . A larger in the Softmax will dampen differences of and by that prevent vanishing gradients by low attention entropy. In contrast, a smaller will amplify differences of and prevents vanishing gradients caused by uniform attention. Choosing the right temperature is difficult and can have a strong influence on what the model learns, how fast it converges etc. As a remedy, we propose to start training with a low temperature and follow a schedule to heat it up to the default value of . We refer to this approach as Heat Treatment (HT) and it is one of our interventions to test whether the Softmax is indeed the root cause of the optimization difficulties. This approach has multiple advantages. First, it removes the difficulty of choosing the exact temperature. Second, the network gets optimized for “more peaky” attention, but the temperature increases steadily. By that, the network starts with centralized attention but since the next epochs attention will be more uniform than the previous (due to increasing the temperature), it does not run into the issue of low attention entropy. Last, the network can focus on most important features early in training and broaden the view over time, attending to other features.

---

[referencia=128e7e40ab379185 score=0.837]
### 5.2 Can Enforcing Lower Entropy Attention Maps Resolve the Small Gradients?

The previous subsection indicates that a local uniform attention is causing the learning problems of the transformer. To test this hypothesis and show that this causes the observed problems we use targeted interventions. Particularly, we modify Softmax’s temperature in the attention block. Large temperatures increase entropy, while small temperatures decrease it. We apply following interventions: training with lower/higher temperature; HT, where the temperature increases from a low value to default temperature during the first half of training; and NormSoftmax, which adaptively changes the temperature for each sample, head and layer.

Does a lower temperature solve the small gradient issue and thereby mitigate the optimization issues? Increasing the temperature from low to default or using NormSoftmax increases high attention scores (c.f. Fig. 10). Importantly, the transformer learns to also attend to the indicators (Fig. ). Furthermore, all approaches (lower temperature , HT and NormSoftmax) solve the imbalanced gradient issue for , and (Fig. 4) and lead to higher gradients in indicator regions (Fig. 5). Eureka-moments happen much earlier or instantly (see Fig. 6). Thus, the interventions indeed mitigate the optimization issues. A comprehensive comparison between a vanilla ViT and other versions is provided in Tab. 1. Decreasing the temperature or using NormSoftmax increases the Eureka-ratio, accuracy and decreases the Eureka-epoch (i.e., improving the energy landscape). In contrast, increasing the temperature has a negative effect on the Eureka-ratio, showing that the local uniform attention is the main cause for the learning problem.

---

[referencia=128e7e40ab379185 score=0.614]
Grokking.
A similar phenomenon has been discovered on synthetic data (Power et al., 2022) and was further studied in (Liu et al., 2023; Nanda et al., 2023; Thilak et al., 2022; Millidge, 2022; Barak et al., 2022; Liu et al., 2022). Grokking describes the phenomenon of sudden generalization after overfitting, which can be induced by weight decay.
In contrast to Eureka-moments, the training accuracy already saturates at close to 100% (overfitting), a long time before the validation accuracy has a sudden leap from chance level to perfect generalization.
For Eureka-moments, validation and training loss saturate (no overfitting) and the sudden leap occurs for *both simultaneously*.

Unstable gradients in transformers. The position of the layer-norm (LN) (Xiong et al., 2020) and instabilities in the Adam optimizer in combination with LN induced vanishing gradients (Huang et al., 2020). Removing the LN (Baevski & Auli, 2019; Child et al., 2019; Wang et al., 2019) or Warmup (Baevski & Auli, 2019; Child et al., 2019; Wang et al., 2019; Huang et al., 2020) resolves this problem, but in our case, Warmup alone does not help. Others identified the Softmax as one of the problems, showing that both extremes, attention entropy collapse, i.e., too centralized attention (Zhai et al., 2023; Shen et al., 2023) and a large number of small attention scores, i.e., close to maximum entropy (Dong et al., 2021; Chen et al., 2023) can lead to small gradients (Noci et al., 2022). As a remedy to vanishing gradients caused by entropy collapse Wang et al. (2021) proposed to replace the Softmax by periodic functions. However, before Eureka-moments, the attention distribution is in neither extreme. Instead the attention is allocated to the wrong tokens.

---

[referencia=128e7e40ab379185 score=0.479]
NormSoftmax. An alternative to tame the attention is NormSoftmax (Jiang et al., 2023), which replaces the expected standard deviation gets by the empirical standard deviation , for each attention block individually. NormSoftmax can be computed by

|  |  |  | (2) | 

If has low standard deviation differences will be amplified. If , will be used.

---

[referencia=128e7e40ab379185 score=0.380]
Why does the transformer fail to learn to attend to the indicators? Based on the discussion in Sec. 3, we hypothesize that ill-distributed attention scores lead to small gradients for and , which in turn inhibit learning and in particular learning to shift attention towards the indicators. Note that high attention to some pairs with low attention to all others or uniformly distributed attention can result in vanishing gradients (Noci et al., 2022). To test this, we visualize the L1-norm of the gradient of the first layer in Fig. 4. For vanilla ViT the gradients for and are 0.5-1 orders of magnitude smaller than those for . Thus, only small gradients are backpropagated through the Softmax to and , and the attention map improves only slowly, which results in the observed slow learning. Differences between the gradients are much smaller for ViT , ViT+HT and NormSoftmax, in particular before the Eureka-moment. Fig. 5 shows the origin of gradients on the image plane for . For ViT, the gradients mostly originate from the target regions, which further explains why many steps are needed to move attention to the indicators, as these gradients only lead to improved target recognition.

Is too small or too large attention-entropy the problem? We visualize the distribution of attention maps over training in Fig. 10: the vast majority of attention scores is very small. This indicates that a too uniform attention is causing small gradients. Larger attentions are rare, but not absent, as can be seen in Fig. , but indicator regions have small and uniform attention. Thus, we conclude that local uniform attention causes the transformer’s learning problems.

---

[referencia=128e7e40ab379185 score=0.371]
Models and hyper-parameters. Following Hassani et al. (2021), we use a ViT version specifically designed for small datasets. Unless stated otherwise, we train a ViT with 7 layers, 4 heads each with embedding dimension of 64, patch size of 4 and MLP-ratio of 2. Consequently, the default temperature is . The ResNet has a comparable parameter count and consists of 9 layers. For ViT, ViT+HT and NormSoftmax, we tested 5 different temperature parameters in initial experiments. More details on the training setup are provided in A.14. For the reasoning task, we train a transformer on 30% of the entire set of possible inputs (i.e., input combinations) for 10K epochs over five random seeds. More details on model and training are provided in A.16 .

---

[referencia=128e7e40ab379185 score=0.366]
### A.14 Experimental setup — Vision Task

We mostly follow the DeiT (Touvron et al., 2021) training recipe without distillation. For optimization we use AdamW (Loshchilov & Hutter, 2019) with default values, i.e., and and . Unless otherwise stated we Warmup the learning rate for 5 epochs from to the maximum learning rate, use a weight decay of 0.05 and train for 300 epochs. We train all models with a batch size of 512, which fits on a single V100, for all the architectures that we considered. Since position and color can be important cues in our datasets we train without data augmentation. We only sample color-noise from a standard normal Gaussian with standard deviation 0.05 for each color channel independently. Color-noise is sampled for each sub-sample (i.e., each indicator and each target) independently and added to the RGB value.

Learning rate schedules for all models. To compare the tested methods and models fairly, we run a search over 9 learning rate schedules with 4 random seeds, each. We anneal the learning rate from a maximum to a minimum using a cosine scheduler. We also use Warmup, as described in the paragraph above. The different schedules can be seen in Tab. 11. We pick the schedule that leads to highest Eureka-ratio for each model. In case of a tie we pick the schedule with higher accuracy.

| max learning rate | min learning rate | 
|---|---|

Info on taus: In initial experiments we tested for ViT 5 values for , , , , and . We found , to work well and did not further optimize them for the different methods. For HT we set the goal temperature to the default and tried also . Further optimizing these parameters for each model and dataset will most likely lead to improvements, but would add very little to a deeper understanding of the Eureka-moments.

### A.15 Implementation Details NormSoftmax

In practice, can be defined by arbitrary functions. As highlighted in the background section, the standard deviation is a theoretically motivated choice. Alternatives are discussed by Jiang et al. (2023). In this work, we find the variance to work better for ViT and RoBERTa, while we stick to the standard deviation for the reasoning task.

---

[referencia=128e7e40ab379185 score=0.218]
### A.16 Experimental Setup – reasoning task

The input of the model is of the form “a b c d =“, where, where . In our experiments, we set . We train the transformer on 30% of the entire set of possible inputs (i.e., input combinations), that is with a batch size of 4392. The rest is used as test set. We train for 10 000 epochs over five random seeds. We use token embeddings of size of , four attention heads of dimension of , hidden units in the MLP, and learned positional embeddings.

We trained with full batch gradient descent using AdamW (Loshchilov & Hutter, 2019) with a cross-entropy loss. We optimized learning rates via grid search over on seed 0. Following Nanda et al. (2023) we use a weight decay of 1.

### A.17 Slingshot Effects on Reasoning Task

We observed that NormSoftmax caused slingshot effects (Thilak et al., 2022) during the convergence phase of some of the training runs but believe this may be due to the interaction of gradients at different scales with adaptive optimizers (Nanda et al., 2023). Since slingshot effects only occur after Eureka-moments, they cannot be the cause for their occurrence. We did not further investigate this observation.

### A.18 Experimental Setup – RoBERTa

The RoBERTa experiments are based on the Code provided by (Deshpande & Narasimhan, 2020). We follow the data acquisition and preparation strategy of (Shoeybi et al., 2019). Thus, we train on the latest Wikipedia dump (downloaded on the 2<sup>nd</sup> of August 2023). We train a 12 layer RoBERTa model with 12 heads. We use a batch size of 84 and a learning rate of 5e-5.

---

[referencia=128e7e40ab379185 score=0.176]
- Wei et al. (2022)
Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama,
D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O.,
Liang, P., Dean, J., and Fedus, W.
Emergent abilities of large language models.
*Transactions on Machine Learning Research* , 2022.
ISSN 2835-8856.
URL https://openreview.net/forum?id=yzkSU5zdwD.
Survey Certification.
- Xiao et al. (2017)
Xiao, H., Rasul, K., and Vollgraf, R.
Fashion-mnist: a novel image dataset for benchmarking machine
learning algorithms.
*CoRR* , abs/1708.07747, 2017.
URL http://arxiv.org/abs/1708.07747.
- Xiong et al. (2020)
Xiong, R., Yang, Y., He, D., Zheng, K., Zheng, S., Xing, C., Zhang, H., Lan,
Y., Wang, L., and Liu, T.
On layer normalization in the transformer architecture.
In *International Conference on Machine Learning* , pp. 10524–10533. PMLR, 2020.
- Zhai et al. (2023)
Zhai, S., Likhomanenko, T., Littwin, E., Busbridge, D., Ramapuram, J., Zhang,
Y., Gu, J., and Susskind, J. M.
Stabilizing transformer training by preventing attention entropy
collapse.
In *International Conference on Machine Learning* , pp. 40770–40803. PMLR, 2023.
- Zhang et al. (2023)
Zhang, L., Rao, A., and Agrawala, M.
Adding conditional control to text-to-image diffusion models.
In *Proceedings of the IEEE/CVF International Conference on
Computer Vision* , pp.  3836–3847, 2023.

---

[referencia=128e7e40ab379185 score=0.163]
### 5.3 Is This an Artificial Problem Caused by Other Factors?

Does the transformer simply ignore specific indicator locations? The task and dataset used in the previous subsections showed indicators and targets always at the same location, i.e., indicators on top-left and bottom right. Such a dataset design might result in two undesired effects: 1) The transformer might learn to ignore features based on the associated positional embeddings. 2) The task might be easier, since positional embeddings can be used as shortcut to find indicators without the need to rely on the actual features. To disprove both cases we create another dataset, explained in Fig. 7. We observe that removing the fixed position for indicators and targets makes the task even more difficult (Tab. 1 bottom) and differences between methods are even more apparent. Thus, ViTs without Eureka-moment do not simply learn to ignore regions of the image.

Is this a mere artifact of a bad choice of hyper-parameters?

*main dataset*. Both interventions, ViT+HT and NormSoftmax drastically reduce the saturation period and can even lead to a complete disappearance of the saturation period.

*No position task*description. This task is identical to the

*main task*, but removes more information by swapping indicator (digit) and target (fashion) in each row with a probability of 0.5, i.e., task 2 is to classify either the top or bottom fashion sample. Two samples are shown to highlight differences from the task described in Fig. .

We test various competing explanations that could lead to the observed phenomenon, like training instabilities due to inadequate Warmup, bad choice of learning rate schedules and Weight Decay to force circuit formation as observed for grokking (Nanda et al., 2023). Weight Decay and Warmup do not improve the results. We find that Eureka-moments are sensitive to the learning rate. NormSoftmax and HT reduce the sensitivity to sub-optimal learning rates drastically (see Tab. 2). See A.5 for a more detailed answer to the posed question.

Influence of model scale, dataset size and image resolution on Eureka-moments. We found no consistent influence of model scale on Eureka-ratio. See A.6 for more details. Further, we can rule out that this observation is an artifact of image resolution or dataset size by showing the phenomenon on a ImageNet-100 based dataset in A.10.

---

[referencia=128e7e40ab379185 score=0.151]
To further validate the results of our analysis in a real setting we train RoBERTa (Liu et al., 2019) with NormSoftmax for language modeling on Wikipedia, where we suspect task 1 to be learning of general word probabilities and task 2 to be modulating these probabilities based on context, or modulating them based on syntactic relations (Chen et al., 2024). Additionally, we train GPT-2 on the Omniglot (Radford et al., 2019) dataset and test its ICL abilities following Chan et al. (2022). Experimental details for RoBERTa and ICL are provided in A.18 and A.19, respectively. Fig. 9 shows that NormSoftmax indeed leads to earlier Eureka-moments for RoBERTa. Furthermore, NormSoftmax also improves ICL, i.e., GPT-2 with NormSoftmax trained on the Omniglot ICL task results in higher ICL accuracy and seems to prevent failure cases like no or a small Eureka-moment (Baseline s1 in Fig. 9). Thus, our analysis and results are indeed transferable to real datasets and also to transformers with causal attention,i.e., GPT-2.

---

[referencia=128e7e40ab379185 score=0.104]
# Eureka-Moments in Transformers:

Multi-Step Tasks Reveal Softmax Induced Optimization Problems

###### Abstract

In this work, we study rapid improvements of the training loss in transformers when being confronted with multi-step decision tasks.
We found that transformers struggle to learn the intermediate task and both training and validation loss saturate for hundreds of epochs.
When transformers finally learn the intermediate task, they do this rapidly and unexpectedly. We call these abrupt improvements *Eureka-moments* , since the transformer appears to suddenly learn a previously incomprehensible concept.
We designed synthetic tasks to study the problem in detail, but the leaps in performance can be observed also for language modeling and in-context learning (ICL). We suspect that these abrupt transitions are caused by the multi-step nature of these tasks. Indeed, we find connections and show that ways to improve on the synthetic multi-step tasks can be used to improve the training of language modeling and ICL.
Using the synthetic data we trace the problem back to the Softmax function in the self-attention block of transformers and show ways to alleviate the problem. These fixes reduce the required number of training steps, lead to higher likelihood to learn the intermediate task, to higher final accuracy and training becomes more robust to hyper-parameters.

###### Keywords:

Machine Learning, ICML, sudden convergence, in-context learning, grokking, transformer, Softmax, attention, temperature, gradient, phase transition, abrupt learning, rapid improvement, eureka-moment, eureka moment, multi-step task, multi-step decision task, two-step task

---

[referencia=128e7e40ab379185 score=0.100]
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

[referencia=128e7e40ab379185 score=0.097]
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

[referencia=128e7e40ab379185 score=0.076]
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

[referencia=128e7e40ab379185 score=0.070]
## 6 Limitations and Conclusion

Limitations. The ability to decompose tasks into sub-problems and learn to solve those sub-tasks is a common problem, but it is difficult to study on real datasets, due to many confounding factors. As a result many works follow a trial-and-error approach. In contrast, we try to gain deeper understanding by studying this problem in a controlled, synthetic setting. This comes with the assumption that our analysis transfers to real data. We find evidence for that, as the intervention (NormSoftmax) leads to improvements on real data and can prevent getting stuck (Fig. 9).

Conclusion. In this work, we identified that transformers have difficulties to decompose a task into sub-problems and learn to solve the intermediate sub-tasks. We observed that transformers can learn these tasks suddenly and unexpectedly but usually take a long time to do so. We called these sudden leaps Eureka-moments. We pined the problem down to the Softmax in the attention that leads to small gradients. We proposed simple interventions that specifically target the Softmax and show that they improve the transformers’ capabilities to learn sub-tasks and to learn them faster. We identify NormSoftmax as most robust and convenient method, leading to consistently better results. Last, we showed that our observations transfer to real datasets.

## Impact Statement

We do not see any particular societal impact other than the overall impact of advancing the field of Machine Learning.

## Acknowledgements

We thank Philipp Schröppel and the entire Computer Vision Group Freiburg for inspiring discussions. Sudhanshu Mittal for feedback on the manuscript and Matteo Farina for reporting observations of potential Eureka-moments on vision and language tasks.

This research was funded by the Bosch Center for Artificial Intelligence, the Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz (BMUV, German Federal Ministry for the Environment, Nature Conservation, Nuclear Safety and Consumer Protection) based on a resolution of the German Bundestag (67KI2029A), the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – SFB 1597 – 499552394 and 417962828.

---

[referencia=128e7e40ab379185 score=0.068]
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

[referencia=128e7e40ab379185 score=0.061]
- Touvron et al. (2021)
Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., and Jegou, H.
Training data-efficient image transformers & distillation through
attention.
In *International Conference on Machine Learning* , volume 139,
pp.  10347–10357, July 2021.
- Vaswani et al. (2017)
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
Kaiser, Ł., and Polosukhin, I.
Attention is all you need.
*Advances in neural information processing systems* , 30, 2017.
- Voita & Titov (2020)
Voita, E. and Titov, I.
Information-theoretic probing with minimum description length.
In Webber, B., Cohn, T., He, Y., and Liu, Y. (eds.),
*Proceedings of the 2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP)* , pp.  183–196, 2020.
URL https://aclanthology.org/2020.emnlp-main.14.
- Wang et al. (2019)
Wang, Q., Li, B., Xiao, T., Zhu, J., Li, C., Wong, D. F., and Chao, L. S.
Learning deep transformer models for machine translation.
In Korhonen, A., Traum, D., and Màrquez, L. (eds.),
*Proceedings of the 57th Annual Meeting of the Association for
Computational Linguistics* , pp.  1810–1822, 2019.
URL https://aclanthology.org/P19-1176.
- Wang et al. (2021)
Wang, S., Liu, F., and Liu, B.
Escaping the gradient vanishing: Periodic alternatives of softmax in
attention mechanism.
*IEEE Access* , 9:168749–168759, 2021.

---

[referencia=128e7e40ab379185 score=0.058]
Digit grouping.
Finally, we make the indicator task more difficult. We follow the same setting as for the *Main dataset*, as described in Fig. . However, indicators are not sampled from digits 1 and 2, but from 1, 2, 3 and 4. Task 1 is to find out whether both indicators are smaller or both indicators are larger or equal to 3. I.e., we build indicator sets  and  if both indicators are from the same group the top-right image should be classified.
As can be seen in Tab. 10, increasing the difficulty of the indicator task quickly makes the dataset too hard. Further optimization of hyper-parameters and architecture are likely to solve the tasks.

|  |  | Digit grouping |  |  | 
|---|---|---|---|---|
|  |  |  | Avg. over EMs |  | 
| Model |  | ER | Acc. | Avg. EE. | 
| ViT |  | 0/4 | - | - | 
| ViT |  | 0/4 | - | - | 
| NormSoftmax |  | 0/4 | - | - |