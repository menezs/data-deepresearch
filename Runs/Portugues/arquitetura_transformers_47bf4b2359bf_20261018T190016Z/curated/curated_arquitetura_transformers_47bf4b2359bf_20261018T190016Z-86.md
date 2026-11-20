[referencia=1480e50475d6c98e score=0.925]
So, how can we overcome the limitations of existing solutions and train large models more efficiently? To answer this question, we first analyze the full spectrum of memory consumption of the existing systems on model training and classify it into two parts: 1) For large models, the majority of the memory is occupied by _model states_ which include the optimizer states (such as momentum and variances in Adam [6]), gradients, and parameters. 2) The remaining memory is consumed by activation, temporary buffers and unusable fragmented memory, which we refer to collectively as _residual_ states. We develop _ZeRO_ — Zero Redundancy Optimizer — to optimize memory efficiency on both while obtaining high compute and communication efficiency. As these two parts face different challenges, we develop and discuss their solutions correspondingly. 

**Optimizing Model State Memory** Model states often consume the largest amount of memory during training, but existing approaches such as DP and MP do not offer satisfying solution. DP has good compute/communication efficiency but poor memory efficiency while MP can have poor compute/communication efficiency. More specifically, DP replicates the entire model states across all data parallel process resulting in redundant memory consumption; while MP partition these states to obtain high memory efficiency, but often result in too finegrained computation and expensive communication that is less scaling efficient. Furthermore, all of these approaches maintain all the model states required over the entire training process statically, even though not all model states are required all the time during the training. Based on these observations, we develop _ZeRO_ -DP, ZeRO-powered data parallelism, that achieves the computation/communication efficiency of DP while achieving memory efficiency of MP. _ZeRO_ - DP removes the memory state redundancies across data-parallel processes by _partitioning_ the model states instead of replicating them, and it retains the compute/communication efficiency by retaining the computational granularity and communication volume of DP using a dynamic communication schedule during training. 

_ZeRO_ -DP has three main optimization stages (as depicted in Figure 1), which correspond to the partitioning of optimizer states, gradients, and parameters. When enabled cumulatively:

---

[referencia=1480e50475d6c98e score=0.870]
## **5 Deep Dive into** **_ZeRO_ -DP** 

While the existing DP approach replicates the model states at each device and introduces significant memory overhead, _ZeRO_ -DP eliminates this memory redundancy by partitioning them — optimizer states, gradients and parameters — across data parallel processes. Figure 1 quantifies and visualizes the memory requirement with and without _ZeRO_ -DP. The figure shows the memory footprint after partitioning (1) optimizer state, (2) gradient and (3) parameter redundancies accumulatively. We refer to them as the three optimization phases of _ZeRO_ -DP: _Pos_ , _Pg_ , and _Pp_ , which we elaborate below.

---

[referencia=1480e50475d6c98e score=0.856]
# ZeRO: Memory Optimizations Toward Training Trillion Parameter Models 

Samyam Rajbhandari<sup>_∗_</sup> , Jeff Rasley,<sup>_∗_</sup> Olatunji Ruwase, Yuxiong He 

_{_ `samyamr, jerasley, olruwase, yuxhe` _}_ `@microsoft.com` 

## **Abstract** 

Large deep learning models offer significant accuracy gains, but training billions to trillions of parameters is challenging. Existing solutions such as data and model parallelisms exhibit fundamental limitations to fit these models into limited device memory, while obtaining computation, communication and development efficiency. We develop a novel solution, Zero Redundancy Optimizer ( _ZeRO_ ), to optimize memory, vastly improving training speed while increasing the model size that can be efficiently trained. _ZeRO_ eliminates memory redundancies in data- and model-parallel training while retaining low communication volume and high computational granularity, allowing us to scale the model size proportional to the number of devices with sustained high efficiency. Our analysis on memory requirements and communication volume demonstrates: _ZeRO_ has the potential to scale beyond 1 _Trillion_ parameters using today’s hardware. 

We implement and evaluate ZeRO: it trains large models of over 100B parameter with super-linear speedup on 400 GPUs, achieving throughput of 15 Petaflops. This represents an 8x increase in model size and 10x increase in achievable performance over state-of-the-art. In terms of usability, _ZeRO_ can train large models of up to 13B parameters (e.g., larger than Megatron GPT 8.3B and T5 11B) without requiring model parallelism which is harder for scientists to apply. Last but not the least, researchers have used the system breakthroughs of _ZeRO_ to create the world’s largest language model (17B parameters) with record breaking accuracy.

---

[referencia=1480e50475d6c98e score=0.710]
### **4.1 Insights and Overview:** **_ZeRO_ -DP** 

_ZeRO_ powered DP is based on three key insights: 

_a)_ DP has better scaling efficiency than MP because MP reduces the granularity of the computation while also increasing the communication overhead. Beyond a certain point, lower computational granularity reduces the efficiency per GPU, while the increased communication overhead, hiders the scalability across GPUs, especially when crossing node boundaries. On the contrary, DP has both higher computational granularity and lower communication volume, allowing for much higher efficiency. 

_b)_ DP is memory inefficient as model states are stored redundantly across all data-parallel processes. On the contrary, MP partitions the model states to obtain memory efficiency. 

_c)_ Both DP and MP keep all the model states needed over the entire training process, but not everything is required all the time. For example, parameters corresponding to each layer is only needed during the forward propagation and backward propagation of the layer. 

Based on these insights, _ZeRO_ -DP retains the training efficiency of DP while achieving the memory efficiency of MP. _ZeRO_ -DP _partitions_ the model states instead of replicating them (Section 5) and uses a dynamic communication schedule that exploits the intrinsically temporal nature of the model states while minimizing the communication volume (Section 7). By doing so, _ZeRO_ -DP reduces per-device memory footprint of a model _linearly_ with the increased DP degree while maintaining the communication volume close to that of the default DP, retaining the efficiency.

---

[referencia=1480e50475d6c98e score=0.636]
## **2 Related Work** 

### **2.1 Data, Model and Pipeline Parallelism** 

Parallelization is a key strategy on training large models at scale. For a model that fits in the device memory for training, data parallelism (DP) is used to scale training to multiple devices. In DP, model parameters are replicated on each device. At each step, a mini-batch is divided evenly across all the data parallel processes, such that each process executes the forward and backward propagation on a different subset of data samples, and uses averaged gradients across processes to update the model locally. 

When a model does not fit in the device memory, model parallelism (MP) [5, 3] and pipeline parallelism (PP) [10, 11] split the model among processes, in vertical and horizontal way respectively. Sec. 1 discussed how _ZeRO_ relates to DP and MP. We now discuss PP and how it relates to reducing memory consumption. 

PP splits a model horizontally across layers running each partition on a different device and use micro-batching to hide the pipeline bubble [10, 11]. Model functionalities such as tied-weights and batch-normalization are difficult to implement due to horizontal splitting and micro-batching, respectively. Popular PP implementation such as G-pipe [10] partitions both model parameters and total activations but requires a batch size proportional to number of pipeline partitions to hide the pipeline bubble. The large batch size can affect the convergence rate, while also requiring significant memory to store activations. A different implementation of PP in PipeDream [12] keeps multiple copies of stale parameters to hide the pipeline bubble without increasing the batch size significantly, making it less memory efficient. Additionally, the implementation is not equivalent to the standard DL training and has implications on training convergence. In contrast, _ZeRO_ obtains the same or better memory efficiency than PP without incurring functionality, performance and convergence related restrictions of PP.

---

[referencia=1480e50475d6c98e score=0.618]
(within each DGX2 node) and 64-way data parallelism across nodes, and run it efficiently using a modest batch size! 

**Implementation & Evaluation** The complete set of optimizations in _ZeRO_ could allow us to run models with trillion parameters on the high-end hardware cluster today (e.g., with 1K V100 GPUs), however, the hardware compute capacity is still too limited and training time can be impractically long ( _>_ 1 year). Therefore, our focus for this implementation is to efficiently support models with 10x parameters ( _∼_ 100B parameters) than state-of-the-art (SOTA) while still being within reach of the compute capabilities of current hardware. We implement and evaluate a subset of optimizations in _ZeRO_ called _ZeRO_ -100B — _Pos_ + _g_ of _ZeRO_ -DP plus ZeRO-R — that allow us to achieve this goal. The results show: <u>Model Size</u> Combined with MP, _ZeRO_ -100B runs 170B parameter models efficiently, while the existing system like using Megatron alone cannot scale efficiently beyond 40B parameters, as shown in Figure 2. This is an over 8x increase in model size compared to SOTA. Speed Improved memory efficiency powers higher throughput and faster training. As shown in Figure 2, _ZeRO_ runs 100B parameter models on a 400 Nvidia V100 GPU cluster with over 

> 1Prior work [8] shows, very large batch size could slow down convergence. For given model and data, there is a measure of critical-batch size, where increasing batch size further slows down convergence. The detailed discussion of this topic is beyond the scope of the paper. 

4 



Figure 3: Superlinear scalability and per GPU training throughput of a 60B parameter model using _ZeRO_ -100B. 

38 TFlops per GPU, and aggregate performance over 15 Petaflops. This is more than 10x improvement in training speed compared to SOTA for the same model size.

---

[referencia=1480e50475d6c98e score=0.544]
### **4.2 Insights and Overview:** **_ZeRO_ -R** 

#### **4.2.1 Reducing Activation Memory** 

Two key insights are: 

_a)_ MP partitions the model states but often requires replication of the activation memory. For example, if we split the parameters of a linear layer vertically and compute them in parallel across two GPUs, each GPU requires the entire activation to compute its partition 

_b)_ For models such as GPT-2 or larger, the arithmetic intensity (ratio of the amount of computation per iteration to amount of activation checkpoints per iteration) is very large ( _≥_ 10 _K_ ) and increases linearly with hidden dimension making it possible to hide the data-movement cost for the activation checkpoints, even when the bandwidth is low. 

_ZeRO_ removes the memory redundancies in MP by _partitioning_ the activations checkpoints across GPUs, and uses allgather to reconstruct them on demand. The activation memory footprint is reduced proportional to the MP degree. For very large models, _ZeRO_ can even choose to move the activation partitions to the CPU memory, while still achieving good efficiency due to large arithmetic intensity in these models. 

#### **4.2.2 Managing Temporary buffers** 

_ZeRO_ -R uses constant size buffers to avoid temporary buffers from blowing up as the model size increases, while making them large enough to remain efficient. 

#### **4.2.3 Managing fragmented Memory** 

Memory fragmentation is a result of interleaving between short lived and long lived memory objects. During the forward propagation activation checkpoints are long lived but the activations that recomputed are short lived. Similarly, the backward computation, the activation gradients are short lived while the parameter gradients are long lived. Based on this insight, 

9 

_ZeRO_ performs on-the-fly memory defragmentation by moving activation checkpoints and gradients to pre-allocated contiguous memory buffers. This not only increases memory availability but also improves efficiency by reducing the time it takes for the memory allocator to find free contiguous memory.

---

[referencia=1480e50475d6c98e score=0.502]
38 TFlops per GPU, and aggregate performance over 15 Petaflops. This is more than 10x improvement in training speed compared to SOTA for the same model size. 

Scalability We observe super linear speedup in the regime of 64-400 GPUs, where the performance more than doubles when we double the number of GPUs. This is a property of _ZeRO_ -DP which reduces the memory footprint of the model states as we increase the DP degree allowing us to fit larger batch sizes per GPU resulting in better performance. We expect this behaviour to continue further as we increase the number of GPUs beyond 400. 

Democratization of Large Model Training _ZeRO_ -100B powers data scientist to train models with up to 13B parameters without any MP or PP that requires model refactoring, where 13B is more parameters than the largest model in literature (T5 with 11B parameters). Data scientists can thus experiment freely with large models without worrying about parallelism. In comparison, exist systems (e.g., PyTorch Distributed Data Parallel) runs out of memory with 1.4B parameter models. 

<u>New SOTA Model</u> _ZeRO_ powers the largest language model with 17B parameters and record-breaking accuracy, Turing-NLG [9]. 

We share _ZeRO_ as a part of our open source DL training optimization library called DeepSpeed<sup>2</sup> . We plan to release all implementations described in this paper by end of May 2020 and extend it further to support 1 trillion parameters by enabling _ZeRO_ -DP stage 3 partitioning parameters ( _Pos_ + _g_ + _p_ ). We plan to make _ZeRO_ fully accessible to the DL community to catalyze the evolution and democratization of large model training at scale. 

> 2https://github.com/microsoft/deepspeed 

5

---

[referencia=1480e50475d6c98e score=0.482]
Limited memory fragmentation is generally not an issue, when there is plenty of memory to spare, but for large model training running with limited memory, memory fragmentation leads to two issues, i) OOM due to lack of contiguous memory even when there is enough available 

memory, ii) poor efficiency as a result of the memory allocator spending significant time to search for a contiguous piece of memory to satisfy a memory request. 

_ZeRO_ does memory defragmentation on-the-fly by pre-allocating contiguous memory chunks for activation checkpoints and gradients, and copying them over to the pre-allocated memory as they are produced. M _D_ not only enables _ZeRO_ to train larger models with larger batch sizes, but also improves efficiency when training with limited memory. 

**7 Communication Analysis of** **_ZeRO_ -DP** As _ZeRO_ boosts model size by removing memory redundancy, it is only natural to ask if we are trading communication volume for memory efficiency. In other words, what is the communication volume of _ZeRO_ -powered DP approach compared to a baseline DP approach? The answer 

is in two parts: i) _ZeRO_ -DP incurs no additional communication using _Pos_ and _Pg_ , while enabling up to 8x memory reduction, ii) _ZeRO_ -DP incurs a maximum of 1 _._ 5x communication when using _Pp_ in addition to _Pos_ and _Pg_ , while further reducing the memory footprint by _Nd_ 

times. We present the analysis in this section. We begin by first presenting a brief overview of the communication volume for standard DP. **7.1 Data Parallel Communication Volume** 

During data parallel training, gradients across all data parallel processes are averaged at the end 

of the backward propagation before computing the updates for the next step. The averaging is performed using an all-reduce communication collective. For a large model size, the all- 

reduce communication is entirely communication bandwidth bound, and therefore, we limit our analysis to the total communication volume send to and from each data parallel process. State-of-art implementation of all-reduce uses a two-step approach, where the first step is

---

[referencia=1480e50475d6c98e score=0.455]
## **6 Deep Dive into** **_ZeRO_ -R** 

### **6.1** _Pa_ **: Partitioned Activation Checkpointing** 

As discussed in 4.2, MP by design requires a replication of the activations, resulting in redundant copies of the activations across model parallel GPUs. _ZeRO_ eliminates this redundancy by partitioning the activations, and only materializes them in a replicated form one activation layer at a time, right before the activation is used in computation. More specifically, once the forward propagation for a layer of a model is computed, the input activations are partitioned across all the model parallel process, until it is needed again during the backprogation. At this point, _ZeRO_ uses an all-gather operation to re-materialize a replicated copy of the activations. We refer to this optimization as _Pa_ . It works in conjunction with activation checkpointing [7], storing partitioned activation checkpoints only instead of replicated copies. Furthermore, in the case of very large models and very limited device memory, these partitioned activation checkpoints can also be offloaded to the CPU reducing the activation memory overhead to nearly zero at an additional communication cost, which we will discuss in 7. We refer to this as _Pa_ + _cpu_ . 

**Memory Saving** With partitioned activation checkpointing, _ZeRO_ reduces the activation footprint by a factor proportional to the MP degree. Consider training a 100B model shown in Table 4 with a batch size of 32, sequence length of 1024 and a MP degree of 16. If we checkpoint a single activation for each transformer layer, it would require about 33 GB of memory per GPU just to store the activation checkpoints. But with P _a_ in _ZeRO_ , it can be reduced to about 2 GB per GPU. Furthermore, this 2GB can be offloaded to the CPU reducing the memory footprint for activations to nearly zero.

---

[referencia=1480e50475d6c98e score=0.380]
**5.3 P** _p_ **: Parameter Partitioning** Just as with the optimizer states, and the gradients, each process only stores the parameters corresponding to its partition. When the parameters outside of its partition are required for forward and backward propagation, they are received from the appropriate data parallel process through broadcast. While this may seem to incur significant communication overhead at first glance, we show that this approach only increases the total communication volume of a baseline DP system to 1 _._ 5x, while enabling memory reduction proportional to _Nd_ . **Memory Savings:** With parameter partitioning, we reduce the memory consumption of an Ψ parameter model from 16Ψ to <u>16Ψ</u> _Nd_<sup>.</sup> As the example in Figure 1, a 7.5 B parameter model requires 1.9 GB of model-state memory using _Pos_ + _p_ + _g_ with 64-way DP ( _Nd_ = 64), while requiring 120 GB with standard DP. This has a profound implication: ZeRO _powers DP to fit models with arbitrary size as long as there are sufficient number of devices to share the model states_ . 

**5.4 Implication on Model Size** The three phases of partitioning _Pos_ , _Pos_ + _g_ , and _Pos_ + _g_ + _p_ reduces the memory consumption of each data parallel process on model states by up to 4x, 8x, and _Nd_ respectively. Table 1 analyzes model-state memory consumption of a few example models under the 3 stages of _ZeRO_ -DP optimizations for varying DP degree. Without _ZeRO_ , the memory consumption is equal to the first row in the table, regardless of the DP degree. Note that, with _Nd_ = 64, _ZeRO_ can train models with up to 7.5B, 14B, and 128B parameters using _Pos_ , _Pos_ + _g_ , and _Pos_ + _g_ + _p_ , respectively. When _Nd_ = 1024, _ZeRO_ with all of its optimizations enabled ( _Pos_ + _g_ + _p_ ) could train models with 1 Trillion parameters! Or potentially, models with Arbitrary size! 

Without _ZeRO_ , the largest model DP alone can run has less than 1.5 Billion parameters.

---

[referencia=1480e50475d6c98e score=0.375]
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

[referencia=1480e50475d6c98e score=0.359]
### **7.2** **_ZeRO_ -DP Communication Volume** 

#### **7.2.1 Communication Volume with** _Pos_ + _g_ 

With gradient partitioning, each process only stores the portion of the gradients, that is required to update its corresponding parameter partition. As such, instead of an all-reduce, _ZeRO_ only requires a scatter-reduce operation on the gradients, incurring communication volume of Ψ. After each process updates the partition of the parameters that it is responsible for, an allgather is performed to collect all the updated parameters from all the data parallel process. This also incurs a communication volume of Ψ. So the total communication volume per training step is Ψ + Ψ = 2Ψ, exactly the same as the baseline DP. 

#### **7.2.2 Communication Volume with** _Pos_ + _g_ + _p_ 

After parameter partitioning, each data parallel process only stores the parameters that it updates. Therefore, during the forward propagation it needs to receives the parameters for all the other partitions. However, this can be pipelined to avoid the memory overhead. Before computing the forward propagation on the part of the model corresponding to a particular partition, the data parallel process responsible for that partition can broadcast the weights to all the data parallel processes. Once the forward propagation for that partition is done, the parameters can be discarded. The total communication volume is thus<sup><u>Ψ</u></sup><sup>_<u>×</u>_</sup> _N_<sup>_<u>N</u>_</sup> _d_<sup>_<u>d</u>_</sup> = Ψ. In other words, we reschedule the parameter all-gather by spreading it across the entire forward propagation, and discarding the parameters once they have been used. Note however that this all-gather needs to happen once again for the backward propagation in the reverse order. 

The total communication volume is therefore the sum of the communication volumes incurred by these all-gathers in addition to the communication volume incurred by the reducescatter of the gradients. The total volume is therefore 3Ψ which is 1.5x compared to the baseline. Both gradient and parameter partitioning leverage the insight that — not all states of gradients and parameters are needed all the time — to optimize memory by communicating the states judiciously.

---

[referencia=1480e50475d6c98e score=0.332]
1) For activations (stored from forward pass in order to perform backward pass), we noticed checkpointing [7] helps but not sufficient for large models. Thus _ZeRO_ -R optimizes activation memory by identifying and removing activation replication in existing MP approaches through activation partitioning. It also offloads activations to CPU when appropriate. 

2) _ZeRO_ -R defines appropriate size for temporary buffers to strike for a balance of memory and computation efficiency. 

3) We observe fragmented memory during training due to variations in the lifetime of different tensors. Lack of contiguous memory due to fragmentation can cause memory allocation failure, even when enough free memory is available. _ZeRO_ -R proactively manages memory based on the different lifetime of tensors, preventing memory fragmentation. 

_ZeRO_ -DP and _ZeRO_ -R combined together forms a powerful system of memory optimizations for DL training that we collectively refer to as _ZeRO_ . 

**_ZeRO_ and MP** : Since _ZeRO_ eliminates the memory inefficiency in DP, it is natural to ask: Do we still need MP, and when? How does _ZeRO_ work with MP? With _ZeRO_ , MP becomes a less attractive option for the purpose of fitting large models alone. _ZeRO_ -DP is at least as effective on reducing per-device memory footprint as MP, or more effective sometimes when MP cannot divide the model evenly. It also has comparable or better scaling efficiency. Furthermore, data parallelism is so easy to use that it is widely applicable across different workloads, while 

3 



Figure 2: _ZeRO_ training throughput and speedup w.r.t SOTA baseline for varying model sizes. For _ZeRO_ , the MP always fit in a node, while for baseline, models larger than 40B require MP across nodes. 

MP approaches today often need some work from model developers to revise their model, system developers to work out distributed operators, and existing work like Megatron-LM only supports a limited set of operators and models.

---

[referencia=1480e50475d6c98e score=0.192]
### **10.6 Turing-NLG, the SOTA language model with 17B parameters** 

As of May 12th, 2020, Turing-NLG is the largest model in the world with over 17B parameters. It achieved the new SOTA for language models with Webtext-103 perplexity of 10.21. TuringNLG was trained end-to-end using _ZeRO_ -100B and Fig. 5 shows the validation perplexity over 300K iterations compared to previous SOTA, Megatron-LM 8.3B parameter model. _ZeRO_ - 100B achieves a sustained throughput of 41.4 TFlops/GPU for this model. 

## **11 Concluding Remarks** 

From a HPC and system perspective, we believe that _ZeRO_ represents a revolutionary transformation in the large model training landscape. While our implementation, _ZeRO_ -100B, enables 8x increase in model sizes, over 10x in throughput improvement, achieves super-linear speedups on modern GPU clusters, and trains the largest model in the world, it is still just a tip of the iceberg. _ZeRO_ in its entirety has the potential to increase the model size by yet another order of magnitude, enabling the training of trillion parameter models of the future. 

Perhaps, what we feel most optimistic about _ZeRO_ is that it imposes no hurdles on the data scientists. Unlike existing approaches such as MP and PP, no model refactoring is necessary, and it is as easy to use as standard DP, making _ZeRO_ a prime candidate for future investigations on large model training. Through open sourcing and community feedback, we plan to make _ZeRO_ fully accessible to the DL community to catalyze the evolution and democratization of large model training at scale. 

19 

## **Acknowledgement** 

We thank Junhua Wang for his valuable support and advice. We thank Minjia Zhang, Elton Zheng, Shaden Smith, Reza Yazdani Aminabadi, Arash Ashari, and Niranjan Uma Naresh for their great feedback and help on evaluating the work. We thank Brandon Norick, Corby Rossett, Gopi Kumar, Jack Zhang, Jing Zhao, Payal Bajaj, Rangan Majumder, Saksham Singhal, Saurabh Tiwary, and Xia Song for many helpful discussions and suggestions.

---

[referencia=1480e50475d6c98e score=0.177]
### **6.3 M** _D_ **: Memory Defragmentation** 

Memory fragmentation in model training occurs as a result of activation checkpointing and gradient computation. During the forward propagation with activation checkpointing, only selected activations are stored for back propagation while most activations are discarded as they can be recomputed again during the back propagation. This creates an interleaving of short lived memory (discarded activations) and long lived memory (checkpointed activation), leading to memory fragmentation. Similarly, during the backward propagation, the parameter gradients are long lived, while activation gradients and any other buffers required to compute the parameter gradients are short lived. Once again, this interleaving of short term and long term memory causes memory fragmentation. 

12 

|MP|GPU|**Max **|**Theoretic**|**al Mode**|**l Size**|**Measur**|**ed Model Size**|
|---|---|---|---|---|---|---|---|
||s|Baseline|P_os_|P_os_+_g_|P_os_+_g_+_p_|Baseline|_ZeRO_-DP (P_os_)|
|1|64|2B|**7.6B**|14.4B|128B|1.3B|**6.2B**|
|2|128|4B|**15.2B**|28.8B|256B|2.5B|**12.5B**|
|4|256|8B|**30.4B**|57.6B|0.5T|5B|**25B**|
|8|512|16B|**60.8B**|115.2B|1T|_10B_|**50B**|
|16|1024|32B|**121.6B**|230.4B|_2T_|20B|**100B**|



Table 2: Maximum model size through memory analysis (left) and the measured model size when running with _ZeRO-OS_ (right). The measured model size with _Pos_ matches the theoretical maximum, demonstrating that our memory analysis provides realistic upper bounds on model sizes.

---

[referencia=1480e50475d6c98e score=0.168]
MP approaches today often need some work from model developers to revise their model, system developers to work out distributed operators, and existing work like Megatron-LM only supports a limited set of operators and models. 

That being said, there are still cases where we want to leverage MP: i) When used with _ZeRO_ -R, MP can reduce activation memory footprint for very large models. ii) For smaller models where activation memory is not an issue, MP can also have benefits when aggregated batch size using DP alone is too big to have good convergence.<sup>1</sup> In those case, one can combine _ZeRO_ with MP to fit the model with an acceptable aggregated batch size. We show that _ZeRO_ can be combined with MP, resulting in a max theoretical memory reduction of _Nd × Nm_ times on each device with a DP degree of _Nd_ and MP degree of _Nm_ . This could allow us to fit a trillion parameter model on 1024 GPUs with 16-way model parallelism 

(within each DGX2 node) and 64-way data parallelism across nodes, and run it efficiently using a modest batch size!

---

[referencia=1480e50475d6c98e score=0.131]
## **9 Step Towards 1 Trillion Parameters** 

The largest published models today are in the range of 10 billion parameters, which are already challenging to train. Getting to a trillion parameters, 3-orders of magnitude larger, will inevitably happen, but the road will be full of hurdles, surprises and innovations. While we do not claim knowing or addressing all of them, _ZeRO_ addresses one of the most fundamental challenges from a system perspective: the ability to fit a model of this scale on current hardware while allowing it to train with good system scalability. 

**A Leap from State-of-Art** The largest model that the state-of-art framework, Megatron, can train with acceptable throughput is a 16 - 20B parameter model in a DGX-2 system. Scaling further by having model parallelism across multiple DGX nodes results in significant efficiency drop due to limited internode bandwidth. 

_ZeRO_ vastly increase the efficiently-runnable model size. It enables the current generation of hardware to run significantly larger models without requiring fine-grained model parallelism to go across the node boundaries. As demonstrated in Table 1, _ZeRO_ , with all optimizations turned on (P _os_ + _g_ + _p_ ), could fit more than 1 _Trillion_ parameters on 1024 GPUs using DP only. Alternatively, when combined with model parallelism (as shown in Table 2), _ZeRO_ could fit more than 1 _Trillion_ parameters on 1024 GPUs with 16-way model parallelism (within each DGX2 node) and 64-way data parallelism across nodes. Running a model with a trillion parameters efficiently is no longer impossible! 

**Compute Power Gap** Training a trillion parameter model end-to-end within an acceptable time range, however, could still require significant amount of compute power, which is lacking in today’s AI clusters. 

To understand the resource requirement, we present a brief comparison with Bert-Large. Bert-Large can be trained in 67 minutes on a 1024 GPU DGX-2H cluster [26]. A 1 Trillion Parameter model can easily contain 3000x (1 trillion / 330 million) more computation than 

15 



Figure 4: Max model throughput with _ZeRO_ -DP. 



Figure 5: SOTA Turing-NLG enabled by _ZeRO_ .

---

[referencia=1480e50475d6c98e score=0.116]
Table 9: Model configurations for Figure 6 related to throughput with different ZeRO configurations. 

|||||Figure|7||||
|---|---|---|---|---|---|---|---|---|
|Model size|ZeRO/Baseline|Number of GPUs|MP|Layers|Hidden size|Attention head|Batch size|Total batch size|
|1.5B|ZeRO|128|1|34|1920|16|24|3072|
|2.5B|ZeRO|128|1|54|1920|16|24|3072|
|4B|ZeRO|128|1|64|2304|24|16|2048|
|6B|ZeRO|128|1|52|3072|24|12|1536|
|8B|ZeRO|128|1|72|3072|24|8|1024|
|10B|ZeRO|128|1|50|4096|32|6|768|
|11B|ZeRO|128|1|54|4096|32|4|512|
|12B|ZeRO|128|1|58|4096|32|4|512|
|13B|ZeRO|128|1|62|4096|32|2|256|
|1p16B|Baseline|128|1|24|1920|16|8|1024|
|1p38B|Baseline|128|1|40|1536|16|1|128|



Table 10: Model configurations for Figure 7 related to evaluating maximum model sizes vs throughput while using only data-parallelism.

---

[referencia=1480e50475d6c98e score=0.100]
_ZeRO_ -DP has three main optimization stages (as depicted in Figure 1), which correspond to the partitioning of optimizer states, gradients, and parameters. When enabled cumulatively: 

1) Optimizer State Partitioning ( _Pos_ ): 4x memory reduction, same communication volume as DP; 

2) Add Gradient Partitioning ( _Pos_ + _g_ ): 8x memory reduction, same communication volume as DP; 

3) Add Parameter Partitioning ( _Pos_ + _g_ + _p_ ): Memory reduction is linear with DP degree _Nd_ . For example, splitting across 64 GPUs ( _Nd_ = 64) will yield a 64x memory reduction. There is a modest 50% increase in communication volume. 

ZeRO-DP eliminates memory redundancies and makes the full aggregate memory capacity of a cluster available. With all three stages enabled, ZeRO can train a trillion-parameter model on just 1024 NVIDIA GPUs. A trillion-parameter model with an optimizer like Adam [6] in 16- 

2 



Figure 1: Comparing the per-device memory consumption of model states, with three stages of _ZeRO_ -DP optimizations. Ψ denotes model size (number of parameters), _K_ denotes the memory multiplier of optimizer states, and _Nd_ denotes DP degree. In the example, we assume a model size of Ψ = 7 _._ 5 _B_ and DP of _Nd_ = 64 with _K_ = 12 based on mixed-precision training with Adam optimizer. 

bit precision requires approximately 16 terabytes (TB) of memory to hold the optimizer states, gradients, and parameters. 16TB divided by 1024 is 16GB, which is well within a reasonable bound for a GPU (e.g., with 32GB of on-device memory). 

**Optimizing Residual State Memory** After _ZeRO_ -DP boosts memory efficiency for model states, the rest of the memory consumed by activations, temporary buffers, and unusable memory fragments could become a secondary memory bottleneck. We develop _ZeRO_ -R to optimize the residual memory consumed by these three factors respectively.