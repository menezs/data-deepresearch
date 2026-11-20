[referencia=128e7e40ab379185 score=0.992]
### A.11 Vanishing Gradient in the Softmax.

Softmax attention can cause vanishing gradients for and . To see that softmax attention can result in vanishing gradients it helps to take a look at the gradients of the attention function. Let

|  |  |  | (3) | 

|  |  |  | (4) | 

|  |  |  |  | (5) | 
|  |  |  |  | (6) | 
|  |  |  |  | (7) | 
|  |  |  |  | (8) | 
|  |  |  |  | (9) | 

be the attention function, where , and are weight matrices, is the input.

Using the chain rule we get

|  |  |  |  | (10) | 
|  |  |  |  | (11) | 

Since are constants we only need to look more closely into .

is given by , where takes the values . Therefore, to analyze how the gradients and behave, we need to analyze the , i.e., the Jacobian of the Softmax . It is given by

|  |  |  | (12) | 

It can be easily seen, that almost all entries in the Jacobian are close to 0 whenever a single is close to 1 and all others are almost 0. Please see (Kurbiel, 2021) for a more detailed analysis.

---

[referencia=128e7e40ab379185 score=0.981]
## 3 Background

Preliminaries. This work investigates the popular dot product attention (Vaswani et al., 2017), defined as

|  |  |  | (1) | 

where the weight matrices , and map the input to query , key , value , and the temperature parameter controls the entropy of the output. A low temperature leads to low entropy, i.e., a more “peaky” distribution. Commonly, is set to , where is the dimensionality of and . Thus, is the standard deviation of under the independence assumption of rows of and with 0 mean and variance of 1 (Vaswani et al., 2017).

Softmax attention can cause vanishing gradients. Attention entropy collapse, i.e., too centralized attention, can cause vanishing gradients (Zhai et al., 2023; Shen et al., 2023), since all entries of the Jacobian of the Softmax will become almost 0 (see . A.11). Similarly, uniform attention can cause vanishing gradients for and (Noci et al., 2022).

A remedy to both problems is to control the attention temperature . A larger in the Softmax will dampen differences of and by that prevent vanishing gradients by low attention entropy. In contrast, a smaller will amplify differences of and prevents vanishing gradients caused by uniform attention. Choosing the right temperature is difficult and can have a strong influence on what the model learns, how fast it converges etc. As a remedy, we propose to start training with a low temperature and follow a schedule to heat it up to the default value of . We refer to this approach as Heat Treatment (HT) and it is one of our interventions to test whether the Softmax is indeed the root cause of the optimization difficulties. This approach has multiple advantages. First, it removes the difficulty of choosing the exact temperature. Second, the network gets optimized for “more peaky” attention, but the temperature increases steadily. By that, the network starts with centralized attention but since the next epochs attention will be more uniform than the previous (due to increasing the temperature), it does not run into the issue of low attention entropy. Last, the network can focus on most important features early in training and broaden the view over time, attending to other features.

---

[referencia=128e7e40ab379185 score=0.961]
Why does the transformer fail to learn to attend to the indicators? Based on the discussion in Sec. 3, we hypothesize that ill-distributed attention scores lead to small gradients for and , which in turn inhibit learning and in particular learning to shift attention towards the indicators. Note that high attention to some pairs with low attention to all others or uniformly distributed attention can result in vanishing gradients (Noci et al., 2022). To test this, we visualize the L1-norm of the gradient of the first layer in Fig. 4. For vanilla ViT the gradients for and are 0.5-1 orders of magnitude smaller than those for . Thus, only small gradients are backpropagated through the Softmax to and , and the attention map improves only slowly, which results in the observed slow learning. Differences between the gradients are much smaller for ViT , ViT+HT and NormSoftmax, in particular before the Eureka-moment. Fig. 5 shows the origin of gradients on the image plane for . For ViT, the gradients mostly originate from the target regions, which further explains why many steps are needed to move attention to the indicators, as these gradients only lead to improved target recognition.

Is too small or too large attention-entropy the problem? We visualize the distribution of attention maps over training in Fig. 10: the vast majority of attention scores is very small. This indicates that a too uniform attention is causing small gradients. Larger attentions are rare, but not absent, as can be seen in Fig. , but indicator regions have small and uniform attention. Thus, we conclude that local uniform attention causes the transformer’s learning problems.

---

[referencia=128e7e40ab379185 score=0.952]
Grokking.
A similar phenomenon has been discovered on synthetic data (Power et al., 2022) and was further studied in (Liu et al., 2023; Nanda et al., 2023; Thilak et al., 2022; Millidge, 2022; Barak et al., 2022; Liu et al., 2022). Grokking describes the phenomenon of sudden generalization after overfitting, which can be induced by weight decay.
In contrast to Eureka-moments, the training accuracy already saturates at close to 100% (overfitting), a long time before the validation accuracy has a sudden leap from chance level to perfect generalization.
For Eureka-moments, validation and training loss saturate (no overfitting) and the sudden leap occurs for *both simultaneously*.

Unstable gradients in transformers. The position of the layer-norm (LN) (Xiong et al., 2020) and instabilities in the Adam optimizer in combination with LN induced vanishing gradients (Huang et al., 2020). Removing the LN (Baevski & Auli, 2019; Child et al., 2019; Wang et al., 2019) or Warmup (Baevski & Auli, 2019; Child et al., 2019; Wang et al., 2019; Huang et al., 2020) resolves this problem, but in our case, Warmup alone does not help. Others identified the Softmax as one of the problems, showing that both extremes, attention entropy collapse, i.e., too centralized attention (Zhai et al., 2023; Shen et al., 2023) and a large number of small attention scores, i.e., close to maximum entropy (Dong et al., 2021; Chen et al., 2023) can lead to small gradients (Noci et al., 2022). As a remedy to vanishing gradients caused by entropy collapse Wang et al. (2021) proposed to replace the Softmax by periodic functions. However, before Eureka-moments, the attention distribution is in neither extreme. Instead the attention is allocated to the wrong tokens.

---

[referencia=128e7e40ab379185 score=0.684]
### 5.2 Can Enforcing Lower Entropy Attention Maps Resolve the Small Gradients?

The previous subsection indicates that a local uniform attention is causing the learning problems of the transformer. To test this hypothesis and show that this causes the observed problems we use targeted interventions. Particularly, we modify Softmax’s temperature in the attention block. Large temperatures increase entropy, while small temperatures decrease it. We apply following interventions: training with lower/higher temperature; HT, where the temperature increases from a low value to default temperature during the first half of training; and NormSoftmax, which adaptively changes the temperature for each sample, head and layer.

Does a lower temperature solve the small gradient issue and thereby mitigate the optimization issues? Increasing the temperature from low to default or using NormSoftmax increases high attention scores (c.f. Fig. 10). Importantly, the transformer learns to also attend to the indicators (Fig. ). Furthermore, all approaches (lower temperature , HT and NormSoftmax) solve the imbalanced gradient issue for , and (Fig. 4) and lead to higher gradients in indicator regions (Fig. 5). Eureka-moments happen much earlier or instantly (see Fig. 6). Thus, the interventions indeed mitigate the optimization issues. A comprehensive comparison between a vanilla ViT and other versions is provided in Tab. 1. Decreasing the temperature or using NormSoftmax increases the Eureka-ratio, accuracy and decreases the Eureka-epoch (i.e., improving the energy landscape). In contrast, increasing the temperature has a negative effect on the Eureka-ratio, showing that the local uniform attention is the main cause for the learning problem.

---

[referencia=128e7e40ab379185 score=0.676]
In summary, the contributions of this analysis paper are: 1) We study multi-step learning without intermediate supervision via a fully controlled data-generating process on synthetic tasks. 2) We discover a new failure mode of transformers.
3) We analyse the mechanisms underlying this failure mode and find that the Softmax function leads to (local) small gradients for the key and value weight matrices, thereby hindering learning.
4) To validate the role of Softmax, we mitigate the failure mode through targeted interventions.
We show that these interventions lead to significantly faster convergence, higher accuracy, higher robustness to suboptimal hyper-parameters, and higher probability of model convergence, affirming our analysis.
5) We find related learning behavior in ICL and language modeling and show that our solution transfers to these settings.
The code to reproduce the results and create the datasets is available<sup>1</sup><sup>1</sup>
            1
            
            
            
            
            
            
            
          https://github.com/boschresearch/eurekaMoments.

---

[referencia=128e7e40ab379185 score=0.594]
## Appendix A Appendix

Here, we provide additional information that supports understanding and helps interpreting the main paper. We provide supplemental experimental results and more detailed analysis. We show the gradient norm for indicators and targets individually, which reveals that most of the already small gradients for and is attributed to target features for models that do not learn the task and very little to indicator features. We provide a more complete version of Fig. 4. Provide more insights into why gradient magnitude scaling does not work and provide more details on our analysis of competing hypotheses. We provide an ablation on model scale and the main results from the main paper with standard deviation and training speed up. We explain additional datasets and report results on them. We repeat the linear probe analysis with more sensitive information probes. We provide the linear probe plots using also , and representations and the full version of Fig. 4. Last, we provide details on training and experimental setups and an explanation for vanishing gradients in case of centralized attention maps.

### A.1 Attention Distribution Over Time

We show the change of the attention distribution during the course of training in Fig. 11

---

[referencia=128e7e40ab379185 score=0.358]
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

[referencia=128e7e40ab379185 score=0.259]
### A.16 Experimental Setup – reasoning task

The input of the model is of the form “a b c d =“, where, where . In our experiments, we set . We train the transformer on 30% of the entire set of possible inputs (i.e., input combinations), that is with a batch size of 4392. The rest is used as test set. We train for 10 000 epochs over five random seeds. We use token embeddings of size of , four attention heads of dimension of , hidden units in the MLP, and learned positional embeddings.

We trained with full batch gradient descent using AdamW (Loshchilov & Hutter, 2019) with a cross-entropy loss. We optimized learning rates via grid search over on seed 0. Following Nanda et al. (2023) we use a weight decay of 1.

### A.17 Slingshot Effects on Reasoning Task

We observed that NormSoftmax caused slingshot effects (Thilak et al., 2022) during the convergence phase of some of the training runs but believe this may be due to the interaction of gradients at different scales with adaptive optimizers (Nanda et al., 2023). Since slingshot effects only occur after Eureka-moments, they cannot be the cause for their occurrence. We did not further investigate this observation.

### A.18 Experimental Setup – RoBERTa

The RoBERTa experiments are based on the Code provided by (Deshpande & Narasimhan, 2020). We follow the data acquisition and preparation strategy of (Shoeybi et al., 2019). Thus, we train on the latest Wikipedia dump (downloaded on the 2<sup>nd</sup> of August 2023). We train a 12 layer RoBERTa model with 12 heads. We use a batch size of 84 and a learning rate of 5e-5.

---

[referencia=128e7e40ab379185 score=0.151]
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

[referencia=128e7e40ab379185 score=0.122]
Temperature in Softmax. A key operation in the transformer is the scaled dot-product attention. Large products can lead to attention entropy collapse (Zhai et al., 2023; Shen et al., 2023), which results in very small gradients. In contrast, Chen et al. (2023) observed close to uniform attention over tokens. They scaled down very low scores further while amplifying larger scores, but this only amplified the problem when important tokens are already ignored. Instead, Jiang et al. (2023) proposed to normalize the dot product. Their proposed NormSoftmax avoids low variance attention weights and thus avoids the small gradient problem. We found it as the most effective intervention on the Softmax function. Others proposed to learn the temperature parameter (Dufter et al., 2020; Ali et al., 2021), but this is difficult to optimize. For very large models the problem becomes more severe. Models with more than 8B parameters show attention entropy collapse (Dehghani et al., 2023). They followed (Gilmer et al., 2023) and normalized the with layer norm before the Softmax.

---

[referencia=128e7e40ab379185 score=0.097]
## 2 Related Works

Emergence and phase transitions.
Following Steinhardt (2022) & Wei et al. (2022),
*emergence* refers to a qualitative change in a learning system resulting from an increase of model size, training data or training steps, where *phase transitions* are additionally characterized by a sharp change. Eureka-moments are special types of phase transitions.
While recent work showed that sharp emergence may just be an artifact of the choice of a discontinuous metric (Schaeffer et al., 2024; Srivastava et al., 2023), we observe rapid changes also for continuous metrics in our setting.
A connection between phase transitions or emergence and our work may exist, and both may be related to escaping bad energy landscapes as in our work.

Unexplained phase transitions. Previous works reported observations that may be Eureka-moments, without investigating their cause. For instance, rapid improvements happen for in-context-learning (ICL) (Olsson et al., 2022), diffusion model training (Zhang et al., 2023) and BERT training (Gupta & Berant, 2020; Deshpande & Narasimhan, 2020; Nagatsuka et al., 2021; ano, 2023; Chen et al., 2024). Deshpande & Narasimhan (2020) proposed to bias the attention mechanism towards predefined attention patterns and observed speed-ups in BERT training, while Chen et al. (2024) connect the sharp drop to sudden learning of syntactic attention structures. We also identify the learning of the task-required attention pattern to be the cause of the problem. In concurrent work Reddy (2023) studied phase transitions in ICL. Specifically, they show for a small toy-model that slow initial learning is due to a saddle-point, where one path leads to a sub-optimal minimum (i.e., random context label) and the other path to the ICL solution. They discover a “cliff” in the loss landscape and shallow gradients that lead to the ICL solution. While our setting shows substantial differences, our analysis reveals the same underlying mechanisms, i.e., shallow gradients, which we investigate in more detail.

---

[referencia=128e7e40ab379185 score=0.078]
## 6 Limitations and Conclusion

Limitations. The ability to decompose tasks into sub-problems and learn to solve those sub-tasks is a common problem, but it is difficult to study on real datasets, due to many confounding factors. As a result many works follow a trial-and-error approach. In contrast, we try to gain deeper understanding by studying this problem in a controlled, synthetic setting. This comes with the assumption that our analysis transfers to real data. We find evidence for that, as the intervention (NormSoftmax) leads to improvements on real data and can prevent getting stuck (Fig. 9).

Conclusion. In this work, we identified that transformers have difficulties to decompose a task into sub-problems and learn to solve the intermediate sub-tasks. We observed that transformers can learn these tasks suddenly and unexpectedly but usually take a long time to do so. We called these sudden leaps Eureka-moments. We pined the problem down to the Softmax in the attention that leads to small gradients. We proposed simple interventions that specifically target the Softmax and show that they improve the transformers’ capabilities to learn sub-tasks and to learn them faster. We identify NormSoftmax as most robust and convenient method, leading to consistently better results. Last, we showed that our observations transfer to real datasets.

## Impact Statement

We do not see any particular societal impact other than the overall impact of advancing the field of Machine Learning.

## Acknowledgements

We thank Philipp Schröppel and the entire Computer Vision Group Freiburg for inspiring discussions. Sudhanshu Mittal for feedback on the manuscript and Matteo Farina for reporting observations of potential Eureka-moments on vision and language tasks.

This research was funded by the Bosch Center for Artificial Intelligence, the Bundesministerium für Umwelt, Naturschutz, nukleare Sicherheit und Verbraucherschutz (BMUV, German Federal Ministry for the Environment, Nature Conservation, Nuclear Safety and Consumer Protection) based on a resolution of the German Bundestag (67KI2029A), the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – SFB 1597 – 499552394 and 417962828.

---

[referencia=128e7e40ab379185 score=0.069]
In each of our synthetic datasets, the answer to the first task , which is not explicitly modeled in the loss function, must be found by the model in order to correctly solve the final second task depending on it . For example, in Fig. , the model must first classify the two digits to find out if they are of the same class, which determines where to look for the subsequent FashionMNIST classification task. The loss only provides a training signal for the latter task. Thus, the model must figure this out by itself during training. Formally, such multi-step tasks can be described as , i.e., the probability of class given evidence and the latent variable .

Our study reveals that transformers have difficulties in learning such two-step tasks (Fig. ). After they learned to classify a randomly selected FashionMNIST image , they saturate and only after a long time suddenly learn , i.e., the task to select the right fashion image by comparing the digits. We call this phenomenon a Eureka-moment. Intriguingly, we find that they never learn task 1 within 1000 epochs and stick with the prior for some random seeds. We later find that the probability of Eureka-moments depends on the difficulty of the task. In contrast to the transformer, a ResNet learns both tasks immediately.

Our goal is not to add to the old transformer vs. CNN discussion, but we want to investigate this particular problem. What is its cause? Is it due to a too small capacity? Is it the number of heads or the learning rate? Is it the spatial arrangement of task 1 and 2? We found that these factors play only a minor role and finally traced the problem back to the Softmax function in the transformer’s attention blocks. We found parts of the gradient’s components become very small depending on the Softmax output. This cannot be fixed by using a larger learning rate, since other components of the gradient are large, but it can be simply fixed by a normalization of the Softmax function.

---

[referencia=128e7e40ab379185 score=0.064]
To further validate the results of our analysis in a real setting we train RoBERTa (Liu et al., 2019) with NormSoftmax for language modeling on Wikipedia, where we suspect task 1 to be learning of general word probabilities and task 2 to be modulating these probabilities based on context, or modulating them based on syntactic relations (Chen et al., 2024). Additionally, we train GPT-2 on the Omniglot (Radford et al., 2019) dataset and test its ICL abilities following Chan et al. (2022). Experimental details for RoBERTa and ICL are provided in A.18 and A.19, respectively. Fig. 9 shows that NormSoftmax indeed leads to earlier Eureka-moments for RoBERTa. Furthermore, NormSoftmax also improves ICL, i.e., GPT-2 with NormSoftmax trained on the Omniglot ICL task results in higher ICL accuracy and seems to prevent failure cases like no or a small Eureka-moment (Baseline s1 in Fig. 9). Thus, our analysis and results are indeed transferable to real datasets and also to transformers with causal attention,i.e., GPT-2.

---

[referencia=128e7e40ab379185 score=0.061]
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

[referencia=128e7e40ab379185 score=0.052]
### A.2 Gradient Norm for Indicators and Targets

Our particular dataset design allows us to look at the gradients for indicators and targets separately. In particular, we make use of the fact, that indicators and targets are always at the exact same spacial location. More precisely, we use the partial derivatives as proxy for the gradients. We compute , and , where is the output of the attention function. To analyze the gradient norm for targets and indicators independently we compute , and , where is the output of the attention function. Since we compute the derivative wrt. the tokens, the spacial dimension remains. By averaging over the batch dimension and heads we can plot the partial derivative for each token. While it’s not exactly the same, we will use the term gradient to refer to these partial derivatives in the following.

Since each token corresponds to a region in the image, we can visualize these results as an image. The results are shown in Figs. 5, 11, 12. It can clearly be seen, that target regions (top-right and bottom-left) receive more gradients than indicator regions for and . ViT, ViT+HT and NormSoftmax mitigate this problem, leading to significant gradient for indicator tokens. Indicator regions for receive comparatively larger gradients, however, the gradients for are much smaller.

Besides that, we compute the mean partial derivative for indicator and target regions of the image, i.e., we average the partial derivatives for tokens corresponding to target regions or indicator regions. This allows us to plot the gradient norm for , and for only target and indicator tokens over the training. We show the results in Fig. 13. We make the following observations:

1. 1.

---

[referencia=128e7e40ab379185 score=0.022]
### 5.1 Why Do Transformers Fail to Learn Two-step Tasks?

To investigate why ViT’s training fails, we analyze the learned representations using progress measures. Note that solving task 1 requires ViT to 1) learn to distinguish the indicators, 2) carry the information through the layers and 3) compare the indicator information to obtain the target location. We use linear probes on the output of the attention heads, i.e., , for all heads . However, note that linear separation becomes very likely as feature dimensionality increases. Thus, a high accuracy on the linear probe classification does not imply that the transformer is using that information. It only shows that the information is represented and linearly separable.

Does the transformer fail to distinguish the indicators? The left bar plots in Fig. show that the indicators can be linearly separated well (orange, brown) across all layers (Fig. 19). Nonetheless, ViT fails to learn task 1 (Fig. right plot). Thus, the transformer represents the information to solve task 1 but does not utilize it.

Does the transformer filter out information required for task 1? Since the loss provides a training signal only for task 2, the transformer may learn to just ignore the indicators. Task 1 information could be ignored in the attention blocks, i.e., the attention function does not attend to the indicators. To test this, we probe the representation after the attention operation at two locations, before and after the residual connection. Fig. reveals that the indicator information is available in all layers. Early in training, some indicator information is filtered out in the attention block (blue). Indicator information is partially filtered out in deeper layers, but is always recovered by the residual connections (see Fig. 19). Thus, features required for task 1 are not filtered out.

ViT

=1/3

ViT+HT

NormSoftmax

*No position task*. ER: Eureka-ratio, Acc.: Accuracy, Avg. EE.: average Eureka-epoch.

---

[referencia=128e7e40ab379185 score=0.018]
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

[referencia=128e7e40ab379185 score=0.018]
### 5.3 Is This an Artificial Problem Caused by Other Factors?

Does the transformer simply ignore specific indicator locations? The task and dataset used in the previous subsections showed indicators and targets always at the same location, i.e., indicators on top-left and bottom right. Such a dataset design might result in two undesired effects: 1) The transformer might learn to ignore features based on the associated positional embeddings. 2) The task might be easier, since positional embeddings can be used as shortcut to find indicators without the need to rely on the actual features. To disprove both cases we create another dataset, explained in Fig. 7. We observe that removing the fixed position for indicators and targets makes the task even more difficult (Tab. 1 bottom) and differences between methods are even more apparent. Thus, ViTs without Eureka-moment do not simply learn to ignore regions of the image.

Is this a mere artifact of a bad choice of hyper-parameters?

*main dataset*. Both interventions, ViT+HT and NormSoftmax drastically reduce the saturation period and can even lead to a complete disappearance of the saturation period.

*No position task*description. This task is identical to the

*main task*, but removes more information by swapping indicator (digit) and target (fashion) in each row with a probability of 0.5, i.e., task 2 is to classify either the top or bottom fashion sample. Two samples are shown to highlight differences from the task described in Fig. .

We test various competing explanations that could lead to the observed phenomenon, like training instabilities due to inadequate Warmup, bad choice of learning rate schedules and Weight Decay to force circuit formation as observed for grokking (Nanda et al., 2023). Weight Decay and Warmup do not improve the results. We find that Eureka-moments are sensitive to the learning rate. NormSoftmax and HT reduce the sensitivity to sub-optimal learning rates drastically (see Tab. 2). See A.5 for a more detailed answer to the posed question.

Influence of model scale, dataset size and image resolution on Eureka-moments. We found no consistent influence of model scale on Eureka-ratio. See A.6 for more details. Further, we can rule out that this observation is an artifact of image resolution or dataset size by showing the phenomenon on a ImageNet-100 based dataset in A.10.