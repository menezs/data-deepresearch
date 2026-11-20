[referencia=1480e50475d6c98e score=0.857]
So, how can we overcome the limitations of existing solutions and train large models more efficiently? To answer this question, we first analyze the full spectrum of memory consumption of the existing systems on model training and classify it into two parts: 1) For large models, the majority of the memory is occupied by _model states_ which include the optimizer states (such as momentum and variances in Adam [6]), gradients, and parameters. 2) The remaining memory is consumed by activation, temporary buffers and unusable fragmented memory, which we refer to collectively as _residual_ states. We develop _ZeRO_ — Zero Redundancy Optimizer — to optimize memory efficiency on both while obtaining high compute and communication efficiency. As these two parts face different challenges, we develop and discuss their solutions correspondingly. 

**Optimizing Model State Memory** Model states often consume the largest amount of memory during training, but existing approaches such as DP and MP do not offer satisfying solution. DP has good compute/communication efficiency but poor memory efficiency while MP can have poor compute/communication efficiency. More specifically, DP replicates the entire model states across all data parallel process resulting in redundant memory consumption; while MP partition these states to obtain high memory efficiency, but often result in too finegrained computation and expensive communication that is less scaling efficient. Furthermore, all of these approaches maintain all the model states required over the entire training process statically, even though not all model states are required all the time during the training. Based on these observations, we develop _ZeRO_ -DP, ZeRO-powered data parallelism, that achieves the computation/communication efficiency of DP while achieving memory efficiency of MP. _ZeRO_ - DP removes the memory state redundancies across data-parallel processes by _partitioning_ the model states instead of replicating them, and it retains the compute/communication efficiency by retaining the computational granularity and communication volume of DP using a dynamic communication schedule during training. 

_ZeRO_ -DP has three main optimization stages (as depicted in Figure 1), which correspond to the partitioning of optimizer states, gradients, and parameters. When enabled cumulatively:

---

[referencia=09b3a2927fbd8693 score=0.843]
### **2.3. Data and Model Parallelism in Deep Learning** 

There are two central paradigms for scaling out deep neural network training to numerous hardware accelerators: data parallelism (Valiant, 1990) where a training minibatch is split across multiple workers, and model parallelism in which the memory usage and computation of a model is distributed across multiple workers. By increasing the minibatch size proportionally to the number of available workers (i.e. _weak scaling_ ), one observes near linear scaling in training data throughput. However, large batch training introduces complications into the optimization process that can result in reduced accuracy or longer time to convergence, offsetting the benefit of increased training throughput (Keskar et al., 2017). Further research (Goyal et al., 2017; You et al., 2017; 2019) has developed techniques to miti- 

gate these effects and drive down the training time of large neural networks. To scale out training even further, parallel work (Chen et al., 2016) has combined data parallelism with activation checkpointing: recomputing activations in the backward pass without storing them in the forward pass to reduce memory requirements. 

However, these techniques have one fundamental limitation in the problem size they can tackle: the model must fit entirely on one worker. With language models of increasing size and complexity like BERT and GPT-2, neural networks have approached the memory capacity of modern hardware accelerators. One solution to this problem is to employ parameter sharing to reduce the memory footprint of the model (Lan et al., 2019), but this limits the overall capacity of the model. Our approach is to utilize model parallelism to split the model across multiple accelerators. This not only alleviates the memory pressure, but also increases the amount of parallelism independently of the microbatch size.

---

[referencia=1480e50475d6c98e score=0.771]
## **2 Related Work** 

### **2.1 Data, Model and Pipeline Parallelism** 

Parallelization is a key strategy on training large models at scale. For a model that fits in the device memory for training, data parallelism (DP) is used to scale training to multiple devices. In DP, model parameters are replicated on each device. At each step, a mini-batch is divided evenly across all the data parallel processes, such that each process executes the forward and backward propagation on a different subset of data samples, and uses averaged gradients across processes to update the model locally. 

When a model does not fit in the device memory, model parallelism (MP) [5, 3] and pipeline parallelism (PP) [10, 11] split the model among processes, in vertical and horizontal way respectively. Sec. 1 discussed how _ZeRO_ relates to DP and MP. We now discuss PP and how it relates to reducing memory consumption. 

PP splits a model horizontally across layers running each partition on a different device and use micro-batching to hide the pipeline bubble [10, 11]. Model functionalities such as tied-weights and batch-normalization are difficult to implement due to horizontal splitting and micro-batching, respectively. Popular PP implementation such as G-pipe [10] partitions both model parameters and total activations but requires a batch size proportional to number of pipeline partitions to hide the pipeline bubble. The large batch size can affect the convergence rate, while also requiring significant memory to store activations. A different implementation of PP in PipeDream [12] keeps multiple copies of stale parameters to hide the pipeline bubble without increasing the batch size significantly, making it less memory efficient. Additionally, the implementation is not equivalent to the standard DL training and has implications on training convergence. In contrast, _ZeRO_ obtains the same or better memory efficiency than PP without incurring functionality, performance and convergence related restrictions of PP.

---

[referencia=1480e50475d6c98e score=0.757]
# ZeRO: Memory Optimizations Toward Training Trillion Parameter Models 

Samyam Rajbhandari<sup>_∗_</sup> , Jeff Rasley,<sup>_∗_</sup> Olatunji Ruwase, Yuxiong He 

_{_ `samyamr, jerasley, olruwase, yuxhe` _}_ `@microsoft.com` 

## **Abstract** 

Large deep learning models offer significant accuracy gains, but training billions to trillions of parameters is challenging. Existing solutions such as data and model parallelisms exhibit fundamental limitations to fit these models into limited device memory, while obtaining computation, communication and development efficiency. We develop a novel solution, Zero Redundancy Optimizer ( _ZeRO_ ), to optimize memory, vastly improving training speed while increasing the model size that can be efficiently trained. _ZeRO_ eliminates memory redundancies in data- and model-parallel training while retaining low communication volume and high computational granularity, allowing us to scale the model size proportional to the number of devices with sustained high efficiency. Our analysis on memory requirements and communication volume demonstrates: _ZeRO_ has the potential to scale beyond 1 _Trillion_ parameters using today’s hardware. 

We implement and evaluate ZeRO: it trains large models of over 100B parameter with super-linear speedup on 400 GPUs, achieving throughput of 15 Petaflops. This represents an 8x increase in model size and 10x increase in achievable performance over state-of-the-art. In terms of usability, _ZeRO_ can train large models of up to 13B parameters (e.g., larger than Megatron GPT 8.3B and T5 11B) without requiring model parallelism which is harder for scientists to apply. Last but not the least, researchers have used the system breakthroughs of _ZeRO_ to create the world’s largest language model (17B parameters) with record breaking accuracy.

---

[referencia=c00b8dae0f8e596c score=0.743]
To evaluate efficiency, we report the normalized training throughput of AmoebaNet-D (18, 256) and Transformer-48 using GPipe with different numbers of partitions and different numbers of micro-batches in Table 2. Each partition is assigned to a separate accelerator. We observe that when the number of micro-batches _M_ is at least 4 _×_ the number of partitions, the bubble overhead is almost negligible. For Transformer model, there is a 3 _._ 5 _×_ speedup when it is partitioned across four times more accelerators. Furthermore, training throughput scales almost linearly with the number of devices, thanks to the computation being evenly distributed across Transformer layers. In contrast, the AmoebaNet model achieves sub-linear speedup due to its imbalanced computation distribution. When _M_ is 

Table 2: Normalized training throughput using GPipe with different # of partitions _K_ and different # of micro-batches _M_ on TPUs. Performance increases with more micro-batches. There is an almost linear speedup with the number of accelerators for Transformer model when _M ≫ K_ . Batch size was adjusted to fit memory if necessary. 

|TPU|A|moebaN|et|Tr|ansform|er|
|---|---|---|---|---|---|---|
|_K_ =|2|4|8|2|4|8|
|_M_ = 1|1|1.13|1.38|1|1.07|1.3|
|_M_ = 4|1.07|1.26|1.72|1.7|3.2|4.8|
|_M_ = 32|1.21|1.84|3.48|1.8|3.4|6.3|



relatively small, the bubble overhead can no longer be negligible. When _M_ is 1, there is effectively no pipeline parallelism. We observe relatively constant throughput regardless of the number of accelerators used, indicating only one device is actively computing at any given time.

---

[referencia=1480e50475d6c98e score=0.709]
### **4.1 Insights and Overview:** **_ZeRO_ -DP** 

_ZeRO_ powered DP is based on three key insights: 

_a)_ DP has better scaling efficiency than MP because MP reduces the granularity of the computation while also increasing the communication overhead. Beyond a certain point, lower computational granularity reduces the efficiency per GPU, while the increased communication overhead, hiders the scalability across GPUs, especially when crossing node boundaries. On the contrary, DP has both higher computational granularity and lower communication volume, allowing for much higher efficiency. 

_b)_ DP is memory inefficient as model states are stored redundantly across all data-parallel processes. On the contrary, MP partitions the model states to obtain memory efficiency. 

_c)_ Both DP and MP keep all the model states needed over the entire training process, but not everything is required all the time. For example, parameters corresponding to each layer is only needed during the forward propagation and backward propagation of the layer. 

Based on these insights, _ZeRO_ -DP retains the training efficiency of DP while achieving the memory efficiency of MP. _ZeRO_ -DP _partitions_ the model states instead of replicating them (Section 5) and uses a dynamic communication schedule that exploits the intrinsically temporal nature of the model states while minimizing the communication volume (Section 7). By doing so, _ZeRO_ -DP reduces per-device memory footprint of a model _linearly_ with the increased DP degree while maintaining the communication volume close to that of the default DP, retaining the efficiency.

---

[referencia=1480e50475d6c98e score=0.650]
(within each DGX2 node) and 64-way data parallelism across nodes, and run it efficiently using a modest batch size! 

**Implementation & Evaluation** The complete set of optimizations in _ZeRO_ could allow us to run models with trillion parameters on the high-end hardware cluster today (e.g., with 1K V100 GPUs), however, the hardware compute capacity is still too limited and training time can be impractically long ( _>_ 1 year). Therefore, our focus for this implementation is to efficiently support models with 10x parameters ( _∼_ 100B parameters) than state-of-the-art (SOTA) while still being within reach of the compute capabilities of current hardware. We implement and evaluate a subset of optimizations in _ZeRO_ called _ZeRO_ -100B — _Pos_ + _g_ of _ZeRO_ -DP plus ZeRO-R — that allow us to achieve this goal. The results show: <u>Model Size</u> Combined with MP, _ZeRO_ -100B runs 170B parameter models efficiently, while the existing system like using Megatron alone cannot scale efficiently beyond 40B parameters, as shown in Figure 2. This is an over 8x increase in model size compared to SOTA. Speed Improved memory efficiency powers higher throughput and faster training. As shown in Figure 2, _ZeRO_ runs 100B parameter models on a 400 Nvidia V100 GPU cluster with over 

> 1Prior work [8] shows, very large batch size could slow down convergence. For given model and data, there is a measure of critical-batch size, where increasing batch size further slows down convergence. The detailed discussion of this topic is beyond the scope of the paper. 

4 



Figure 3: Superlinear scalability and per GPU training throughput of a 60B parameter model using _ZeRO_ -100B. 

38 TFlops per GPU, and aggregate performance over 15 Petaflops. This is more than 10x improvement in training speed compared to SOTA for the same model size.

---

[referencia=1480e50475d6c98e score=0.541]
38 TFlops per GPU, and aggregate performance over 15 Petaflops. This is more than 10x improvement in training speed compared to SOTA for the same model size. 

Scalability We observe super linear speedup in the regime of 64-400 GPUs, where the performance more than doubles when we double the number of GPUs. This is a property of _ZeRO_ -DP which reduces the memory footprint of the model states as we increase the DP degree allowing us to fit larger batch sizes per GPU resulting in better performance. We expect this behaviour to continue further as we increase the number of GPUs beyond 400. 

Democratization of Large Model Training _ZeRO_ -100B powers data scientist to train models with up to 13B parameters without any MP or PP that requires model refactoring, where 13B is more parameters than the largest model in literature (T5 with 11B parameters). Data scientists can thus experiment freely with large models without worrying about parallelism. In comparison, exist systems (e.g., PyTorch Distributed Data Parallel) runs out of memory with 1.4B parameter models. 

<u>New SOTA Model</u> _ZeRO_ powers the largest language model with 17B parameters and record-breaking accuracy, Turing-NLG [9]. 

We share _ZeRO_ as a part of our open source DL training optimization library called DeepSpeed<sup>2</sup> . We plan to release all implementations described in this paper by end of May 2020 and extend it further to support 1 trillion parameters by enabling _ZeRO_ -DP stage 3 partitioning parameters ( _Pos_ + _g_ + _p_ ). We plan to make _ZeRO_ fully accessible to the DL community to catalyze the evolution and democratization of large model training at scale. 

> 2https://github.com/microsoft/deepspeed 

5

---

[referencia=1480e50475d6c98e score=0.515]
**5.3 P** _p_ **: Parameter Partitioning** Just as with the optimizer states, and the gradients, each process only stores the parameters corresponding to its partition. When the parameters outside of its partition are required for forward and backward propagation, they are received from the appropriate data parallel process through broadcast. While this may seem to incur significant communication overhead at first glance, we show that this approach only increases the total communication volume of a baseline DP system to 1 _._ 5x, while enabling memory reduction proportional to _Nd_ . **Memory Savings:** With parameter partitioning, we reduce the memory consumption of an Ψ parameter model from 16Ψ to <u>16Ψ</u> _Nd_<sup>.</sup> As the example in Figure 1, a 7.5 B parameter model requires 1.9 GB of model-state memory using _Pos_ + _p_ + _g_ with 64-way DP ( _Nd_ = 64), while requiring 120 GB with standard DP. This has a profound implication: ZeRO _powers DP to fit models with arbitrary size as long as there are sufficient number of devices to share the model states_ . 

**5.4 Implication on Model Size** The three phases of partitioning _Pos_ , _Pos_ + _g_ , and _Pos_ + _g_ + _p_ reduces the memory consumption of each data parallel process on model states by up to 4x, 8x, and _Nd_ respectively. Table 1 analyzes model-state memory consumption of a few example models under the 3 stages of _ZeRO_ -DP optimizations for varying DP degree. Without _ZeRO_ , the memory consumption is equal to the first row in the table, regardless of the DP degree. Note that, with _Nd_ = 64, _ZeRO_ can train models with up to 7.5B, 14B, and 128B parameters using _Pos_ , _Pos_ + _g_ , and _Pos_ + _g_ + _p_ , respectively. When _Nd_ = 1024, _ZeRO_ with all of its optimizations enabled ( _Pos_ + _g_ + _p_ ) could train models with 1 Trillion parameters! Or potentially, models with Arbitrary size! 

Without _ZeRO_ , the largest model DP alone can run has less than 1.5 Billion parameters.

---

[referencia=1480e50475d6c98e score=0.508]
1) For activations (stored from forward pass in order to perform backward pass), we noticed checkpointing [7] helps but not sufficient for large models. Thus _ZeRO_ -R optimizes activation memory by identifying and removing activation replication in existing MP approaches through activation partitioning. It also offloads activations to CPU when appropriate. 

2) _ZeRO_ -R defines appropriate size for temporary buffers to strike for a balance of memory and computation efficiency. 

3) We observe fragmented memory during training due to variations in the lifetime of different tensors. Lack of contiguous memory due to fragmentation can cause memory allocation failure, even when enough free memory is available. _ZeRO_ -R proactively manages memory based on the different lifetime of tensors, preventing memory fragmentation. 

_ZeRO_ -DP and _ZeRO_ -R combined together forms a powerful system of memory optimizations for DL training that we collectively refer to as _ZeRO_ . 

**_ZeRO_ and MP** : Since _ZeRO_ eliminates the memory inefficiency in DP, it is natural to ask: Do we still need MP, and when? How does _ZeRO_ work with MP? With _ZeRO_ , MP becomes a less attractive option for the purpose of fitting large models alone. _ZeRO_ -DP is at least as effective on reducing per-device memory footprint as MP, or more effective sometimes when MP cannot divide the model evenly. It also has comparable or better scaling efficiency. Furthermore, data parallelism is so easy to use that it is widely applicable across different workloads, while 

3 



Figure 2: _ZeRO_ training throughput and speedup w.r.t SOTA baseline for varying model sizes. For _ZeRO_ , the MP always fit in a node, while for baseline, models larger than 40B require MP across nodes. 

MP approaches today often need some work from model developers to revise their model, system developers to work out distributed operators, and existing work like Megatron-LM only supports a limited set of operators and models.

---

[referencia=1480e50475d6c98e score=0.497]
### **2.2 Non-parallelism based approach to reduce memory** 

In addition to MP and PP, there are multiple lines of work that target reducing memory overheads of DL training. 

#### **2.2.1 Reducing Activation Memory** 

Multiple efforts have focused on reducing the memory footprint of activations through compression [13], activation checkpointing [7, 14], or live analysis [15]. These efforts are complimentary and can work together with _ZeRO_ . In fact, activation memory reduction in _ZeRO_ -R works in parallel with activation checkpointing. 

#### **2.2.2 CPU** 

[16, 17] exploit heterogeneous nature of today’s compute nodes, offloading model states to CPU memory through algorithmic design or virtualized memory, respectively. Up to 50% of training time can be spent on GPU-CPU-GPU transfers [16]. _ZeRO_ differs in that it reduces the memory consumption significantly without storing the model states to CPU memory whose bandwidth is severely constrained due to PCI-E. On rare cases, _ZeRO_ -R may offload just the activation checkpoints for very large models to improve performance (see Sec. 6.1 for details). 

6 

#### **2.2.3 Memory Efficient Optimizer** 

[18, 19] focus on reducing memory consumption of adaptive optimization methods by maintaining coarser-grained statistics of model parameters and gradients, with potential impact on model convergence guarantees. _ZeRO_ is orthogonal to these efforts, and its optimizations do not change the model optimization method or affect model convergence, but effectively reduce memory footprint of optimizer states and gradients per device. 

### **2.3 Training Optimizers** 

Adaptive optimization methods [20, 6, 21, 22] are crucial to achieving SOTA performance and accuracy for effective model training of large models. Compared to SGD, by maintaining finegrained first-order and second-order statistics for each model parameter and gradient at the cost of significant memory footprint. _ZeRO_ can reduce the memory footprint of these optimizers by orders of magnitude, making these sophisticated optimization methods practical for training large models on hardware with modest device memory. It also makes it possible to develop and use even more complex and memory hungry optimizers that may have better convergence.

---

[referencia=1480e50475d6c98e score=0.435]
_ZeRO_ -DP has three main optimization stages (as depicted in Figure 1), which correspond to the partitioning of optimizer states, gradients, and parameters. When enabled cumulatively: 

1) Optimizer State Partitioning ( _Pos_ ): 4x memory reduction, same communication volume as DP; 

2) Add Gradient Partitioning ( _Pos_ + _g_ ): 8x memory reduction, same communication volume as DP; 

3) Add Parameter Partitioning ( _Pos_ + _g_ + _p_ ): Memory reduction is linear with DP degree _Nd_ . For example, splitting across 64 GPUs ( _Nd_ = 64) will yield a 64x memory reduction. There is a modest 50% increase in communication volume. 

ZeRO-DP eliminates memory redundancies and makes the full aggregate memory capacity of a cluster available. With all three stages enabled, ZeRO can train a trillion-parameter model on just 1024 NVIDIA GPUs. A trillion-parameter model with an optimizer like Adam [6] in 16- 

2 



Figure 1: Comparing the per-device memory consumption of model states, with three stages of _ZeRO_ -DP optimizations. Ψ denotes model size (number of parameters), _K_ denotes the memory multiplier of optimizer states, and _Nd_ denotes DP degree. In the example, we assume a model size of Ψ = 7 _._ 5 _B_ and DP of _Nd_ = 64 with _K_ = 12 based on mixed-precision training with Adam optimizer. 

bit precision requires approximately 16 terabytes (TB) of memory to hold the optimizer states, gradients, and parameters. 16TB divided by 1024 is 16GB, which is well within a reasonable bound for a GPU (e.g., with 32GB of on-device memory). 

**Optimizing Residual State Memory** After _ZeRO_ -DP boosts memory efficiency for model states, the rest of the memory consumed by activations, temporary buffers, and unusable memory fragments could become a secondary memory bottleneck. We develop _ZeRO_ -R to optimize the residual memory consumed by these three factors respectively.

---

[referencia=1480e50475d6c98e score=0.336]
## **5 Deep Dive into** **_ZeRO_ -DP** 

While the existing DP approach replicates the model states at each device and introduces significant memory overhead, _ZeRO_ -DP eliminates this memory redundancy by partitioning them — optimizer states, gradients and parameters — across data parallel processes. Figure 1 quantifies and visualizes the memory requirement with and without _ZeRO_ -DP. The figure shows the memory footprint after partitioning (1) optimizer state, (2) gradient and (3) parameter redundancies accumulatively. We refer to them as the three optimization phases of _ZeRO_ -DP: _Pos_ , _Pg_ , and _Pp_ , which we elaborate below.

---

[referencia=c00b8dae0f8e596c score=0.312]
To address these challenges, we introduce GPipe, a flexible library that enables efficient training of large neural networks. GPipe allows scaling arbitrary deep neural network architectures beyond the memory limitations of a single accelerator by partitioning the model across different accelerators and supporting re-materialization on every accelerator [13, 14]. With GPipe, each model can be specified as a sequence of layers, and consecutive groups of layers can be partitioned into cells. Each cell is then placed on a separate accelerator. Based on this partitioned setup, we propose a novel pipeline parallelism algorithm with batch splitting. We first split a _mini-batch_ of training examples into smaller _micro-batches_ , then pipeline the execution of each set of micro-batches over cells. We apply synchronous mini-batch gradient descent for training, where gradients are accumulated across all micro-batches in a mini-batch and applied at the end of a mini-batch. Consequently, gradient updates using GPipe are consistent regardless of the number of partitions, allowing researchers to easily train increasingly large models by deploying more accelerators. GPipe can also be complemented with data parallelism to further scale training. 

We demonstrate the flexibility and efficiency of GPipe on image classification and machine translation. For image classification, we train the AmoebaNet model on 480 _×_ 480 input from the ImageNet 2012 dataset. By increasing the model width, we scale up the number of parameters to 557 million and achieve a top-1 validation accuracy of 84.4%. On machine translation, we train a single 128-layer 6-billion-parameter multilingual Transformer model on 103 languages (102 languages to English). We show that this model is capable of outperforming the individually trained 350-million-parameter bilingual Transformer Big [15] models on 100 language pairs.

---

[referencia=1718c427cff7b5e5 score=0.307]
## 5 CONCLUSIONS AND FUTURE WORK 

Mixed precision training is an important technique that allows us to reduce the memory consumption as well as time spent in memory and arithmetic operations of deep neural networks. We have demonstrated that many different deep learning models can be trained using this technique with no loss in accuracy without any hyper-parameter tuning. For certain models with a large number of small gradient values, we introduce the gradient scaling method to help them converge to the same accuracy as FP32 baseline models. 

DNN operations benchmarked with DeepBench<sup>1</sup> on Volta GPU see 2-6x speedups compared to FP32 implementations if they are limited by memory or arithmetic bandwidth. Speedups are lower when operations are latency-limited. Full network training and inference speedups depend on library 

> 1https://github.com/baidu-research/DeepBench 

8 

Published as a conference paper at ICLR 2018 

and framework optimizations for mixed precision and are a focus of future work (experiments in this paper were carried out with early versions of both libraries and frameworks). 

We would also like to extend this work to include generative models like text-to-speech systems and deep reinforcement learning applications. Furthermore, automating loss-scaling factor selection would further simplify training with mixed precision. Loss-scaling factor could be dynamically increased or decreased by inspecting the weight gradients for overflow, skipping weight updates 

9 

Published as a conference paper at ICLR 2018

---

[referencia=c00b8dae0f8e596c score=0.282]
# **GPipe: Easy Scaling with Micro-Batch Pipeline Parallelism** 

**Yanping Huang** `huangyp@google.com` 

**Youlong Cheng Ankur Bapna** `ylc@google.com ankurbpn@google.com` 

**Orhan Firat** `orhanf@google.com` 

**Mia Xu Chen Dehao Chen** `miachen@google.com dehao@google.com` 

**HyoukJoong Lee** `hyouklee@google.com` 

**Jiquan Ngiam Quoc V. Le** `jngiam@google.com qvl@google.com` 

**Yonghui Wu** `yonghui@google.com` 

**Zhifeng Chen** `zhifengc@google.com` 

## **Abstract** 

Scaling up deep neural network capacity has been known as an effective approach to improving model quality for several different machine learning tasks. In many cases, increasing model capacity beyond the memory limit of a single accelerator has required developing special algorithms or infrastructure. These solutions are often architecture-specific and do not transfer to other tasks. To address the need for efficient and task-independent model parallelism, we introduce GPipe, a pipeline parallelism library that allows scaling any network that can be expressed as a sequence of layers. By pipelining different sub-sequences of layers on separate accelerators, GPipe provides the flexibility of scaling a variety of different networks to gigantic sizes efficiently. Moreover, GPipe utilizes a novel batchsplitting pipelining algorithm, resulting in almost linear speedup when a model is partitioned across multiple accelerators. We demonstrate the advantages of GPipe by training large-scale neural networks on two different tasks with distinct network architectures: (i) _Image Classification_ : We train a 557-million-parameter AmoebaNet model and attain a top-1 accuracy of 84.4% on ImageNet-2012, (ii) _Multilingual Neural Machine Translation_ : We train a single 6-billion-parameter, 128-layer Transformer model on a corpus spanning over 100 languages and achieve better quality than all bilingual models.

---

[referencia=1480e50475d6c98e score=0.264]
## **6 Deep Dive into** **_ZeRO_ -R** 

### **6.1** _Pa_ **: Partitioned Activation Checkpointing** 

As discussed in 4.2, MP by design requires a replication of the activations, resulting in redundant copies of the activations across model parallel GPUs. _ZeRO_ eliminates this redundancy by partitioning the activations, and only materializes them in a replicated form one activation layer at a time, right before the activation is used in computation. More specifically, once the forward propagation for a layer of a model is computed, the input activations are partitioned across all the model parallel process, until it is needed again during the backprogation. At this point, _ZeRO_ uses an all-gather operation to re-materialize a replicated copy of the activations. We refer to this optimization as _Pa_ . It works in conjunction with activation checkpointing [7], storing partitioned activation checkpoints only instead of replicated copies. Furthermore, in the case of very large models and very limited device memory, these partitioned activation checkpoints can also be offloaded to the CPU reducing the activation memory overhead to nearly zero at an additional communication cost, which we will discuss in 7. We refer to this as _Pa_ + _cpu_ . 

**Memory Saving** With partitioned activation checkpointing, _ZeRO_ reduces the activation footprint by a factor proportional to the MP degree. Consider training a 100B model shown in Table 4 with a batch size of 32, sequence length of 1024 and a MP degree of 16. If we checkpoint a single activation for each transformer layer, it would require about 33 GB of memory per GPU just to store the activation checkpoints. But with P _a_ in _ZeRO_ , it can be reduced to about 2 GB per GPU. Furthermore, this 2GB can be offloaded to the CPU reducing the memory footprint for activations to nearly zero.

---

[referencia=1480e50475d6c98e score=0.255]
### **10.3 Super-Linear Scalability** 

_ZeRO_ -100B demonstrates super-linear scalability for very large model sizes. Figure 3 shows scalability results for a 60B parameter model going from 64 to 400 GPUs and we expect this trend to continue further for more GPUs. _Pos_ + _g_ reduces per GPU memory consumption of 

> 4https://github.com/nvidia/Megatron-LM 

17 

||_ZeRO_-DP|_ZeRO_-R|
|---|---|---|
|1|P_os_|C_B_+M_D_|
|2|P_os_|C_B_+M_D_+P_a_|
|3|P_os_+_g_|C_B_+M_D_|
|4|P_os_+_g_|C_B_+M_D_+P_a_|
|5|P_os_+_g_|C_B_+M_D_+P_a_+_cpu_|



Table 3: _ZeRO_ configurations 

_ZeRO_ -100B with increase in DP degree, allowing _ZeRO_ -100B to fit larger batch sizes per GPU<sup>5</sup> , which in turn improves throughput as a result of increasing arithmetic intensity. 

### **10.4 Democratizing Large Model Training** 

Using MP and PP is challenging for many data scientists, which is a well-known hurdle to train large models. _ZeRO_ does not require any changes to the model itself and it can be used as simple as baseline DP while delivering significantly boosted model size and speed. Fig. 4 shows that _ZeRO_ -100B can train models with up to 13B parameters without MP on 128 GPUs, achieving throughput over 40 TFlops per GPU on average. In comparison, without _ZeRO_ , the largest trainable model with DP alone has 1.4B parameters with throughput less than 20 TFlops per GPU. Furthermore, in the absence of the communication overhead from MP, these models can be trained with lower-end compute nodes without very fast intra-node interconnect such as NVLINK or NVSwitch, which is required to achieve good efficiency with MP.

---

[referencia=1480e50475d6c98e score=0.238]
MP approaches today often need some work from model developers to revise their model, system developers to work out distributed operators, and existing work like Megatron-LM only supports a limited set of operators and models. 

That being said, there are still cases where we want to leverage MP: i) When used with _ZeRO_ -R, MP can reduce activation memory footprint for very large models. ii) For smaller models where activation memory is not an issue, MP can also have benefits when aggregated batch size using DP alone is too big to have good convergence.<sup>1</sup> In those case, one can combine _ZeRO_ with MP to fit the model with an acceptable aggregated batch size. We show that _ZeRO_ can be combined with MP, resulting in a max theoretical memory reduction of _Nd × Nm_ times on each device with a DP degree of _Nd_ and MP degree of _Nm_ . This could allow us to fit a trillion parameter model on 1024 GPUs with 16-way model parallelism 

(within each DGX2 node) and 64-way data parallelism across nodes, and run it efficiently using a modest batch size!

---

[referencia=09b3a2927fbd8693 score=0.225]
Within model parallelism, there are two further paradigms: layer-wise pipeline parallelism, and more general distributed tensor computation. In pipeline model parallelism, groups of operations are performed on one device before the outputs are passed to the next device in the pipeline where a different group of operations are performed. Some approaches (Harlap et al., 2018; Chen et al., 2018) use a parameter server (Li et al., 2014) in conjunction with pipeline parallelism. However these suffer from inconsistency issues. The GPipe framework for TensorFlow (Huang et al., 2018) overcomes this inconsistency issue by using synchronous gradient decent. This approach requires additional logic to handle the efficient pipelining of these communication and computation operations, and suffers from pipeline bubbles that reduce efficiency, or changes to the optimizer itself which impact accuracy. 

Distributed tensor computation is an orthogonal and more general approach that partitions a tensor operation across multiple devices to accelerate computation or increase model size. FlexFlow (Jia et al., 2018), a deep learning framework orchestrating such parallel computation, provides a method to pick the best parallelization strategy. Recently, Mesh-TensorFlow (Shazeer et al., 2018) introduced a language for specifying a general class of distributed tensor computations in TensorFlow (Abadi et al., 2015). The parallel dimensions are specified in the language by the end user and the resulting graph is compiled with proper collective primitives. We utilize similar insights to those leveraged in Mesh-TensorFlow and exploit parallelism in computing the transformer’s attention heads to parallelize our transformer model. However, rather than implementing a framework and compiler for model parallelism, we make only a few targeted modifications to existing PyTorch transformer implementations. Our approach is simple, does not 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

require any new compiler or code re-writing, and can be fully implemented by inserting a few simple primitives, as described in the next section.