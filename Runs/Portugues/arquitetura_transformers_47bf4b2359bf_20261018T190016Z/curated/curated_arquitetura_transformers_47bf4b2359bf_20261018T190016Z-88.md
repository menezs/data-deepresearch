[referencia=1480e50475d6c98e score=0.630]
## **2 Related Work** 

### **2.1 Data, Model and Pipeline Parallelism** 

Parallelization is a key strategy on training large models at scale. For a model that fits in the device memory for training, data parallelism (DP) is used to scale training to multiple devices. In DP, model parameters are replicated on each device. At each step, a mini-batch is divided evenly across all the data parallel processes, such that each process executes the forward and backward propagation on a different subset of data samples, and uses averaged gradients across processes to update the model locally. 

When a model does not fit in the device memory, model parallelism (MP) [5, 3] and pipeline parallelism (PP) [10, 11] split the model among processes, in vertical and horizontal way respectively. Sec. 1 discussed how _ZeRO_ relates to DP and MP. We now discuss PP and how it relates to reducing memory consumption. 

PP splits a model horizontally across layers running each partition on a different device and use micro-batching to hide the pipeline bubble [10, 11]. Model functionalities such as tied-weights and batch-normalization are difficult to implement due to horizontal splitting and micro-batching, respectively. Popular PP implementation such as G-pipe [10] partitions both model parameters and total activations but requires a batch size proportional to number of pipeline partitions to hide the pipeline bubble. The large batch size can affect the convergence rate, while also requiring significant memory to store activations. A different implementation of PP in PipeDream [12] keeps multiple copies of stale parameters to hide the pipeline bubble without increasing the batch size significantly, making it less memory efficient. Additionally, the implementation is not equivalent to the standard DL training and has implications on training convergence. In contrast, _ZeRO_ obtains the same or better memory efficiency than PP without incurring functionality, performance and convergence related restrictions of PP.

---

[referencia=1480e50475d6c98e score=0.609]
## **1 Extended Introduction** 

Deep Learning (DL) models are becoming larger, and the increase in model size offers significant accuracy gain. In the area of Natural Language Processing (NLP), the transformers have paved way for large models like Bert-large (0.3B) [1], GPT-2 (1.5B) [2], Megatron-LM (8.3B) [3], T5 (11B) [4]. To enable the continuation of model size growth from 10s of billions to trillions of parameters, we experience the challenges of training them - they clearly do not fit within the memory of a single device, e.g., GPU or TPU, and simply adding more devices will not help scale the training. 

Basic data parallelism (DP) does not reduce memory per device, and runs out of memory for models with more than 1.4B parameters on current generation of GPUs with 32 GB memory. Other existing solutions such as Pipeline Parallelism (PP), Model Parallelism (MP), 

> _∗_ Equal Contributors 

1 

CPU-Offloading, etc, make trade-offs between functionality, usability, as well as memory and compute/communication efficiency, but all of which are crucial to training with speed and scale. 

Among different existing solution for training large models, MP is perhaps the most promising. The largest models in the current literature, the 11B T5 model [4], and Megatron-LM 8.3B [3], were both powered by model parallelism, implemented in Mesh-Tensorflow [5] and Megatron-LM[3], respectively. However, MP cannot scale much further beyond these models sizes. MP splits the model vertically, partitioning the computation and parameters in each layer across multiple devices, requiring significant communication between each layer. As a result, they work well within a single node where the inter-GPU communication bandwidth is high, but the efficiency degrades quickly beyond a single node [3]. We tested a 40B parameter model using Megatron-LM across two DGX-2 nodes and observe about 5 _Tflops_ per V100 GPU (less than 5% of hardware peak).

---

[referencia=09b3a2927fbd8693 score=0.503]
Within model parallelism, there are two further paradigms: layer-wise pipeline parallelism, and more general distributed tensor computation. In pipeline model parallelism, groups of operations are performed on one device before the outputs are passed to the next device in the pipeline where a different group of operations are performed. Some approaches (Harlap et al., 2018; Chen et al., 2018) use a parameter server (Li et al., 2014) in conjunction with pipeline parallelism. However these suffer from inconsistency issues. The GPipe framework for TensorFlow (Huang et al., 2018) overcomes this inconsistency issue by using synchronous gradient decent. This approach requires additional logic to handle the efficient pipelining of these communication and computation operations, and suffers from pipeline bubbles that reduce efficiency, or changes to the optimizer itself which impact accuracy. 

Distributed tensor computation is an orthogonal and more general approach that partitions a tensor operation across multiple devices to accelerate computation or increase model size. FlexFlow (Jia et al., 2018), a deep learning framework orchestrating such parallel computation, provides a method to pick the best parallelization strategy. Recently, Mesh-TensorFlow (Shazeer et al., 2018) introduced a language for specifying a general class of distributed tensor computations in TensorFlow (Abadi et al., 2015). The parallel dimensions are specified in the language by the end user and the resulting graph is compiled with proper collective primitives. We utilize similar insights to those leveraged in Mesh-TensorFlow and exploit parallelism in computing the transformer’s attention heads to parallelize our transformer model. However, rather than implementing a framework and compiler for model parallelism, we make only a few targeted modifications to existing PyTorch transformer implementations. Our approach is simple, does not 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

require any new compiler or code re-writing, and can be fully implemented by inserting a few simple primitives, as described in the next section.

---

[referencia=09b3a2927fbd8693 score=0.377]
### **2.3. Data and Model Parallelism in Deep Learning** 

There are two central paradigms for scaling out deep neural network training to numerous hardware accelerators: data parallelism (Valiant, 1990) where a training minibatch is split across multiple workers, and model parallelism in which the memory usage and computation of a model is distributed across multiple workers. By increasing the minibatch size proportionally to the number of available workers (i.e. _weak scaling_ ), one observes near linear scaling in training data throughput. However, large batch training introduces complications into the optimization process that can result in reduced accuracy or longer time to convergence, offsetting the benefit of increased training throughput (Keskar et al., 2017). Further research (Goyal et al., 2017; You et al., 2017; 2019) has developed techniques to miti- 

gate these effects and drive down the training time of large neural networks. To scale out training even further, parallel work (Chen et al., 2016) has combined data parallelism with activation checkpointing: recomputing activations in the backward pass without storing them in the forward pass to reduce memory requirements. 

However, these techniques have one fundamental limitation in the problem size they can tackle: the model must fit entirely on one worker. With language models of increasing size and complexity like BERT and GPT-2, neural networks have approached the memory capacity of modern hardware accelerators. One solution to this problem is to employ parameter sharing to reduce the memory footprint of the model (Lan et al., 2019), but this limits the overall capacity of the model. Our approach is to utilize model parallelism to split the model across multiple accelerators. This not only alleviates the memory pressure, but also increases the amount of parallelism independently of the microbatch size.

---

[referencia=1480e50475d6c98e score=0.330]
- [8] Sam McCandlish, Jared Kaplan, Dario Amodei, and OpenAI Dota Team. An empirical model of large-batch training. _CoRR_ , abs/1812.06162, 2018. 

- [9] Microsoft. Turing-nlg: A 17-billion-parameter language model by microsoft. `https://www.microsoft.com/en-us/research/blog/ turing-nlg-a-17-billion-parameter-language-model-by-microsoft/` , 2020. 

- [10] Yanping Huang, Yonglong Cheng, Dehao Chen, HyoukJoong Lee, Jiquan Ngiam, Quoc V. Le, and Zhifeng Chen. Gpipe: Efficient training of giant neural networks using pipeline parallelism. _ArXiv_ , abs/1811.06965, 2018. 

- [11] Aaron Harlap, Deepak Narayanan, Amar Phanishayee, Vivek Seshadri, Nikhil R. Devanur, Gregory R. Ganger, and Phillip B. Gibbons. Pipedream: Fast and efficient pipeline parallel DNN training. _CoRR_ , abs/1806.03377, 2018. 

20

---

[referencia=09b3a2927fbd8693 score=0.321]
- Harlap, A., Narayanan, D., Phanishayee, A., Seshadri, V., Devanur, N., Ganger, G., and Gibbons, P. Pipedream: Fast and efficient pipeline parallel dnn training. _arXiv:1806.03377_ , 2018. 

- Hendrycks, D. and Gimpel, K. Bridging nonlinearities and stochastic regularizers with gaussian error linear units. _CoRR_ , abs/1606.08415, 2016. URL http: //arxiv _._ org/abs/1606 _._ 08415. 

- Howard, J. and Ruder, S. Fine-tuned language models for text classification. _CoRR_ , abs/1801.06146, 2018. 

- Huang, Y., Cheng, Y., Chen, D., Lee, H., Ngiam, J., Le, Q. V., and Chen, Z. Gpipe: Efficient training of giant neural networks using pipeline parallelism. _CoRR_ , abs/1811.06965, 2018. URL http://arxiv _._ org/ abs/1811 _._ 06965. 

- Jia, Z., Zaharia, M., and Aiken, A. Beyond data and model parallelism for deep neural networks. _arXiv:1807.05358_ , 2018. 

- Joshi, M., Chen, D., Liu, Y., Weld, D. S., Zettlemoyer, L., and Levy, O. Spanbert: Improving pre-training by representing and predicting spans. _arXiv:1907.10529_ , 2019. 

- Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., and Tang, P. T. P. On large- batch training for deep learning: Generalization gap and sharp minima. _ICLR_ , 2017. 

- Khandelwal, U., Levy, O., Jurafsky, D., Zettlemoyer, L., and Lewis, M. Generalization through memorization: Nearest neighbor language models. _arXiv:1911.00172_ , 2019.

---

[referencia=09b3a2927fbd8693 score=0.254]
- Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., Corrado, G. S., Davis, A., Dean, J., Devin, M., Ghemawat, S., Goodfellow, I., Harp, A., Irving, G., Isard, M., Jia, Y., Jozefowicz, R., Kaiser, L., Kudlur, M., Levenberg, J., Mane,´ D., Monga, R., Moore, S., Murray, D., Olah, C., Schuster, M., Shlens, J., Steiner, B., Sutskever, I., Talwar, K., Tucker, P., Vanhoucke, V., Vasudevan, V., Viegas, F., Vinyals, O., Warden, P., Watten-´ berg, M., Wicke, M., Yu, Y., and Zheng, X. TensorFlow: Large-scale machine learning on heterogeneous systems, 2015. URL http://tensorflow _._ org/. Software available from tensorflow.org. 

- Ba, J. L., Kiros, J. R., and Hinton, G. E. Layernorm. _CoRR_ , abs/1607.06450, 2016. URL http://arxiv _._ org/ abs/1607 _._ 06450. 

- Chen, C.-C., Yang, C.-L., and Cheng, H.-Y. Efficient and robust parallel dnn training through model parallelism on multi-gpu platform. _arXiv:1809.02839_ , 2018. 

- Chen, T., Xu, B., Zhang, C., and Guestrin, C. Training deep nets with sublinear memory cost. _CoRR_ , abs/1604.06174, 2016. URL http://arxiv _._ org/ abs/1604 _._ 06174.

---

[referencia=09b3a2927fbd8693 score=0.252]
In this work, we implement a simple and efficient model parallel approach using intra-layer model-parallelism. We exploit the inherent structure in transformer based language models to make a simple model-parallel implementation that trains efficiently in PyTorch, with no custom C++ code or compiler required. This approach is orthogonal to pipelinebased model parallelism as advocated by approaches such as GPipe (Huang et al., 2018). 

To demonstrate the scalability of our approach, we establish 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 



_Figure 1._ Model (blue) and model+data (green) parallel FLOPS as a function of number of GPUs. Model parallel (blue): up to 8-way model parallel weak scaling with approximately 1 billion parameters per GPU (e.g. 2 billion for 2 GPUs and 4 billion for 4 GPUs). Model+data parallel (green): similar configuration as model parallel combined with 64-way data parallel. 

- We show that careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased accuracies as the model grows. 

- We demonstrate that scaling the model size results in improved accuracies for both GPT-2 (studied up to 8.3 billion parameters) and BERT (studied up to 3.9B parameters) models. 

- We showcase that our models achieve state of the art results on test sets: perplexity on WikiText103 (10.8 ppl), accuracy on LAMBADA (66.5%), and accuracy on RACE (90.9%). 

- We open source our code along with the training and evaluation pipelines at https://github _._ com/ NVIDIA/Megatron-LM

---

[referencia=c00b8dae0f8e596c score=0.218]
## **6 Design Features and Trade-Offs** 

Several approaches have been proposed to enable efficient large-scale model parallelism. However, each approach chooses its own set of trade-offs, making it suitable for scaling specific architectures under particular hardware constraints. Here we highlight the various design choices and trade-offs involved with several model-parallelism approaches, and how they compare with GPipe in terms of flexibility, scalability and efficiency under various hardware constraints and architecture variants. 

The core idea of model parallelism involves partitioning a network into different computational units, which are then placed on different devices [42, 43, 44, 45]. Conceptually this supports scaling a large spectrum of models to huge capacities. However these approaches typically suffer from low hardware utilization and device communication bottlenecks. Single Program Multiple Data (SPMD) and pipeline parallelism have been proposed as solutions to counter these challenges. 

Mesh-Tensorflow [34] follows the SPMD paradigm, which extends the Single Instruction Multiple Data (SIMD) approach used for data parallelism to other tensor dimensions. SPMD allows splitting every computation across multiple devices, allowing the user to scale the size of individual matrix multiplications (and thus, the model parameters of individual layers) linearly with the number of accelerators. However, this also introduces high communication overhead between the accelerators due to an abundance of AllReduce-like operations used to combine the outputs of each parallelized matrix multiplication. This limits the applicability of the approach to scenarios where accelerators are connected with high speed interconnects. Further, SPMD limits the type of operations that can be efficiently scaled, restricting its use to a specific set of network architectures and machine learning tasks. For example, splitting along the channel dimension of convolution layers under this paradigm is not efficient given that channels are effectively fully connected, whereas splitting along the spatial dimension requires sophisticated techniques for the halo regions. While SPMD allows scaling the model depth by making each operation smaller, it requires splitting each layer over a larger number of accelerators, which in turn further increases the communication overhead across devices.

---

[referencia=09b3a2927fbd8693 score=0.213]
## **6. Conclusion and Future Work** 

In this work, we successfully surpassed the limitations posed by traditional single-GPU-per-model training by implementing model parallelism with only a few modifications to the existing PyTorch transformer implementations. We efficiently trained transformer based models up to 8.3 billion parameter on 512 NVIDIA V100 GPUs with 8-way model parallelism and achieved up to 15.1 PetaFLOPs sustained over the entire application. We also showed that for BERT models, careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased accuracies as the model size increases. We study the effect of model size on down-stream task accuracy and achieve far superior results on downstream tasks and establish new SOTA for WikiText103, LAMBADA, and RACE datasets. Finally, we open sourced our code to enable future work leveraging model parallel transformers. 

There are several directions for future work. Continuing to increase the scale of pretraining is a promising line of 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

investigation that will further test existing deep learning hardware and software. To realize this, improvements in the efficiency and memory footprint of optimizers will be needed. In addition, training a model with more than 16 billion parameters will demand more memory than is available within 16 GPUs of a DGX-2H box. For such models, a hybrid intra-layer and inter-layer model parallelism along with inter-node model parallelism would be more suitable. Three other directions of investigation include (a) pretraining different model families (XLNet, T5), (b) evaluating performance of large models across more difficult and diverse downstream tasks (e.g. Generative Question Answering, Summarization, and Conversation), and (c) using knowledge distillation to train small student models from these large pretrained teacher models.

---

[referencia=1480e50475d6c98e score=0.202]
38 TFlops per GPU, and aggregate performance over 15 Petaflops. This is more than 10x improvement in training speed compared to SOTA for the same model size. 

Scalability We observe super linear speedup in the regime of 64-400 GPUs, where the performance more than doubles when we double the number of GPUs. This is a property of _ZeRO_ -DP which reduces the memory footprint of the model states as we increase the DP degree allowing us to fit larger batch sizes per GPU resulting in better performance. We expect this behaviour to continue further as we increase the number of GPUs beyond 400. 

Democratization of Large Model Training _ZeRO_ -100B powers data scientist to train models with up to 13B parameters without any MP or PP that requires model refactoring, where 13B is more parameters than the largest model in literature (T5 with 11B parameters). Data scientists can thus experiment freely with large models without worrying about parallelism. In comparison, exist systems (e.g., PyTorch Distributed Data Parallel) runs out of memory with 1.4B parameter models. 

<u>New SOTA Model</u> _ZeRO_ powers the largest language model with 17B parameters and record-breaking accuracy, Turing-NLG [9]. 

We share _ZeRO_ as a part of our open source DL training optimization library called DeepSpeed<sup>2</sup> . We plan to release all implementations described in this paper by end of May 2020 and extend it further to support 1 trillion parameters by enabling _ZeRO_ -DP stage 3 partitioning parameters ( _Pos_ + _g_ + _p_ ). We plan to make _ZeRO_ fully accessible to the DL community to catalyze the evolution and democratization of large model training at scale. 

> 2https://github.com/microsoft/deepspeed 

5

---

[referencia=09b3a2927fbd8693 score=0.187]
> 1Equal contribution 2NVIDIA. Correspondence to: Mohammad Shoeybi _<_ mshoeybi@nvidia.com _>_ . 

Natural Language Processing (NLP) is advancing quickly in part due to an increase in available compute and dataset size. The abundance of compute and data enables training increasingly larger language models via unsupervised pretraining (Devlin et al., 2018; Radford et al., 2019). Empirical evidence indicates that larger language models are dramatically more useful for NLP tasks such as article completion, question answering, and natural language inference (Lan et al., 2019; Raffel et al., 2019). By finetuning these pretrained language models on downstream natural language tasks, one can achieve state of the art results as shown in recent work (Devlin et al., 2018; Peters et al., 2018; Howard & Ruder, 2018; Radford et al., 2018; 2017; Ramachandran et al., 2016; Liu et al., 2019b; Dai et al., 2019; Yang et al., 2019; Liu et al., 2019a; Lan et al., 2019). 

As these models become larger, they exceed the memory limit of modern processors, and require additional memory management techniques such as activation checkpointing (Chen et al., 2016). Widely used optimization algorithms such as ADAM require additional memory per parameter to store momentum and other optimizer state, which reduces the size of models that can be effectively trained. Several approaches to model parallelism overcome this limit by partitioning the model such that the weights and their associated optimizer state do not need to reside concurrently on the processor. For example, GPipe (Huang et al., 2018) and Mesh-Tensorflow (Shazeer et al., 2018) provide frameworks for model parallelism of different kinds. However, they require rewriting the model, and rely on custom compilers and frameworks that are still under development.

---

[referencia=09b3a2927fbd8693 score=0.174]
## **D. Further Scaling Analysis** 

In this section we study the effect of number of attention heads on the scaling results. We also present strong scaling results for our 1.2 billion parameter model. 

### **D.1. Attention Heads and Scaling** 

This section studies the effect of attention heads on model parallel scaling. To this end, we consider the 8.3 billion parameter configuration with 8-way model parallelism and vary the number of heads from 16 to 32. The results are presented in Table 7. As the number of attention heads increases, some of the GEMMS inside the self-attention layer become smaller and also the number of elements in the self attention softmax increases. This results in a slight decrease in scaling efficiency. Future research should be wary of this hyperparameter to design large transformer models that balance model speed and model accuracy. 

### **D.2. Strong Scaling** 

Our model parallelism is primarily designed to enable training models larger than what can fit in the memory of a 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

_Table 7._ Effect of number of attention heads on scaling on 8.3 billion of parameters with 8-way model parallelism. 

|Attention heads|Hidden sizeper head|ScalingEffciency|
|---|---|---|
|16|192|82%|
|24|128|80%|
|32|96|77%|



_Table 8._ Speedup obtained for the 1.2 billion parameters model using model parallelism while keeping the batch size constant. 

|# of GPUs|1|2|4|8|
|---|---|---|---|---|
|Speedup|1.0|1.64|2.34|2.98|



single GPU, but it can also accelerate the training of smaller models without increasing the batch size. To measure this acceleration we train a model with a fixed 1.2 billion parameters. We use a fixed batch size of 8 samples per iteration and increase the number of GPUs using model parallelism. The results are listed in Table 8. Using two GPUs makes training 64% faster. Above that we see diminishing returns as the per-GPU computation decreases and the memory bandwidth and communication overheads begin to dominate.

---

[referencia=1480e50475d6c98e score=0.173]
- [12] Deepak Narayanan, Aaron Harlap, Amar Phanishayee, Vivek Seshadri, Nikhil Devanur, Greg Granger, Phil Gibbons, and Matei Zaharia. Pipedream: Generalized pipeline parallelism for dnn training. In _ACM Symposium on Operating Systems Principles (SOSP 2019)_ , October 2019. 

- [13] Animesh Jain, Amar Phanishayee, Jason Mars, Lingjia Tang, and Gennady Pekhimenko. Gist: Efficient data encoding for deep neural network training. In _International Symposium on Computer Architecture (ISCA 2018)_ , 2018. 

- [14] Paras Jain, Ajay Jain, Aniruddha Nrusimha, Amir Gholami, Pieter Abbeel, Kurt Keutzer, Ion Stoica, and Joseph E. Gonzalez. Checkmate: Breaking the memory wall with optimal tensor rematerialization. _ArXiv_ , abs/1910.02653, 2019. 

- [15] Linnan Wang, Jinmian Ye, Yiyang Zhao, Wei Wu, Ang Li, Shuaiwen Leon Song, Zenglin Xu, and Tim Kraska. Superneurons: Dynamic GPU memory management for training deep neural networks. _CoRR_ , abs/1801.04380, 2018. 

- [16] Bharadwaj Pudipeddi, Maral Mesmakhosroshahi, Jinwen Xi, and Sujeeth Bharadwaj. Training large neural networks with constant memory using a new execution algorithm. _ArXiv_ , abs/2002.05645, 2020. 

- [17] M. Rhu, N. Gimelshein, J. Clemons, A. Zulfiqar, and S. W. Keckler. vdnn: Virtualized deep neural networks for scalable, memory-efficient neural network design. In _2016 49th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO)_ , pages 1–13, 2016. 

- [18] Noam Shazeer and Mitchell Stern. Adafactor: Adaptive learning rates with sublinear memory cost. _CoRR_ , abs/1804.04235, 2018.

---

[referencia=c00b8dae0f8e596c score=0.172]
## **7 Conclusion** 

In this work, we introduce GPipe, a scalable model-parallelism library for training giant neural networks. We propose and implement a novel batch-splitting pipeline-parallelism algorithm that uses synchronous gradient updates, allowing model parallelism with high hardware utilization and training stability. We leverage GPipe to train large-scale convolutional and transformer-based models and demonstrate strong empirical results on both image classification and multilingual machine translation. We highlight three key attributes of the GPipe library: 1) Efficiency: Using a novel batch-splitting pipelining algorithm, GPipe achieves almost linear speedup with the number of devices. 2) Flexibility: GPipe supports any deep network that can be represented as a sequence of layers. 3) Reliability: GPipe utilizes synchronous gradient descent and guarantees consistent training regardless of the number of partitions.

---

[referencia=09b3a2927fbd8693 score=0.159]
## **1. Introduction** 

Recent work in language modeling demonstrates that training large transformer models advances the state of the art in Natural Language Processing applications. However, very large models can be quite difficult to train due to memory constraints. In this work, we present our techniques for training very large transformer models and implement a simple, efficient intra-layer model parallel approach that enables training transformer models with billions of parameters. Our approach does not require a new compiler or library changes, is orthogonal and complimentary to pipeline model parallelism, and can be fully implemented with the insertion of a few communication operations in native PyTorch. We illustrate this approach by converging transformer based models up to 8.3 billion parameters using 512 GPUs. We sustain 15.1 PetaFLOPs across the entire application with 76% scaling efficiency when compared to a strong single GPU baseline that sustains 39 TeraFLOPs, which is 30% of peak FLOPs. To demonstrate that large language models can further advance the state of the art (SOTA), we train an 8.3 billion parameter transformer language model similar to GPT-2 and a 3.9 billion parameter model similar to BERT. We show that careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased performance as the model size grows. Using the GPT-2 model we achieve SOTA results on the WikiText103 (10.8 compared to SOTA perplexity of 15.8) and LAMBADA (66.5% compared to SOTA accuracy of 63.2%) datasets. Our BERT model achieves SOTA results on the RACE dataset (90.9% compared to SOTA accuracy of 89.4%). 

> 1Equal contribution 2NVIDIA. Correspondence to: Mohammad Shoeybi _<_ mshoeybi@nvidia.com _>_ .

---

[referencia=c00b8dae0f8e596c score=0.155]
[44] Azalia Mirhoseini, Hieu Pham, Quoc V Le, Benoit Steiner, Rasmus Larsen, Yuefeng Zhou, Naveen Kumar, Mohammad Norouzi, Samy Bengio, and Jeff Dean. Device placement optimization with reinforcement learning. _arXiv preprint arXiv:1706.04972_ , 2017. 

[45] Jeffrey Dean, Greg Corrado, Rajat Monga, Kai Chen, Matthieu Devin, Mark Mao, Marc aurelio Ranzato, Andrew Senior, Paul Tucker, Ke Yang, Quoc V. Le, and Andrew Y. Ng. Large scale distributed deep networks. In F. Pereira, C. J. C. Burges, L. Bottou, and K. Q. Weinberger, editors, _Neurips 25_ , pages 1223–1231. Curran Associates, Inc., 2012. 

[46] A. Petrowski, G. Dreyfus, and C. Girault. Performance analysis of a pipelined backpropagation parallel algorithm. _IEEE Transactions on Neural Networks_ , 4(6):970–981, Nov 1993. 

### [47] Yonghui Wu, Mike Schuster, Zhifeng Chen, Quoc V Le, Mohammad Norouzi, Wolfgang Macherey, Maxim Krikun, Yuan Cao, Qin Gao, Klaus Macherey, et al. Google’s neural machine translation system: Bridging the gap between human and machine translation. _Transactions of_ 

_the Association for Computational Linguistics,_ , 2017. 

[48] Aaron Harlap, Deepak Narayanan, Amar Phanishayee, Vivek Seshadri, Nikhil Devanur, Greg Ganger, and Phil Gibbons. Pipedream: Fast and efficient pipeline parallel dnn training. _arXiv preprint arXiv:1806.03377_ , 2018. 

[49] Mu Li, David G Andersen, Jun Woo Park, Alexander J Smola, Amr Ahmed, Vanja Josifovski, James Long, Eugene J Shekita, and Bor-Yiing Su. Scaling distributed machine learning with the parameter server. In _OSDI_ , volume 14, pages 583–598, 2014. 

11

---

[referencia=09b3a2927fbd8693 score=0.148]
# **Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

**Mohammad Shoeybi**<sup>1 2</sup> **Mostofa Patwary**<sup>1 2</sup> **Raul Puri**<sup>1 2</sup> **Patrick LeGresley**<sup>2</sup> **Jared Casper**<sup>2</sup> **Bryan Catanzaro**<sup>2</sup> 

## **Abstract**

---

[referencia=c00b8dae0f8e596c score=0.137]
- [36] Felix Wu, Angela Fan, Alexei Baevski, Yann N. Dauphin, and Michael Auli. Pay less attention with lightweight and dynamic convolutions. _CoRR_ , abs/1901.10430, 2019. 

- [37] Naveen Arivazhagan, Ankur Bapna, Orhan Firat, Dmitry Lepikhin, Melvin Johnson, Maxim 

Krikun, Mia Xu Chen, Yuan Cao, George Foster, Colin Cherry, et al. Massively multilingual neu- 

ral machine translation in the wild: Findings and challenges. _arXiv preprint arXiv:1907.05019_ , 2019. 

10 

- [38] Hongyi Zhang, Yann N Dauphin, and Tengyu Ma. Fixup initialization: Residual learning without normalization. _arXiv preprint arXiv:1901.09321_ , 2019. 

[39] Nitish Keskar, Dheevatsa Mudigere, Jorge Nocedal, Mikhail Smelyanskiy, and Ping T.P. Tang. On large-batch training for deep learning: Generalization gap and sharp minima. _CoRR_ , abs/1609.04836, 2016. 

- [40] Samuel L. Smith, Pieter-Jan Kindermans, and Quoc V. Le. Don’t decay the learning rate, increase the batch size. _CoRR_ , abs/1711.00489, 2017. 

[41] Myle Ott, Sergey Edunov, David Grangier, and Michael Auli. Scaling neural machine translation. In _Proceedings of the Third Conference on Machine Translation: Research Papers_ , pages 1–9, Belgium, Brussels, October 2018. Association for Computational Linguistics. 

- [42] Alex Krizhevsky. One weird trick for parallelizing convolutional neural networks. _arXiv preprint arXiv:1404.5997_ , 2014. 

[43] Seunghak Lee, Jin Kyu Kim, Xun Zheng, Qirong Ho, Garth A Gibson, and Eric P Xing. On model parallelization and scheduling strategies for distributed machine learning. In _Neurips_ , pages 2834–2842, 2014.

---

[referencia=c00b8dae0f8e596c score=0.132]
## **5 Massive Massively Multilingual Machine Translation** 

Next, we demonstrate the flexibility of GPipe by scaling up models used for Natural Language Processing (NLP). Due to an abundance of available parallel corpora, neural machine translation (NMT) has become a benchmark task for any architecture used for NLP [33, 15, 34, 35, 36]. For this reason, we continue our GPipe experiments on a large-scale multilingual NMT task. We use a corpus of parallel documents over 102 languages and English, containing a total of 25 billion training examples, ranging from 10<sup>4</sup> to 10<sup>9</sup> per language [37]. This dataset creates a realistic test bed for experiments on scalability by spanning a diverse set of languages from data-scarce (low-resource) to data-rich (high-resource). For the first time in machine translation, we show that a large enough NMT model can learn the mapping between more than 100 language pairs simultaneously, while achieving better than bilingual model performance for all languages. This further brings out the importance of having efficient and flexible model-parallelism tools. 

Our comparison is based on the performance of a single Transformer [15] trained on all language pairs in this corpus. We scale the architecture along two dimensions to stress the flexibility of GPipe: (i) along the depth by increasing the number of layers in the model and (ii) along the width by increasing the hidden dimension in the feed-forward layers and the number of attention heads (as well as # attention channels) in multi-head attention layers similar to Shazeer _et al_ . [34]. Please refer to the supplementary material for a detailed description of our dataset, baselines, training configuration and optimization hyper-parameters.