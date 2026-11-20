[referencia=09b3a2927fbd8693 score=0.881]
Within model parallelism, there are two further paradigms: layer-wise pipeline parallelism, and more general distributed tensor computation. In pipeline model parallelism, groups of operations are performed on one device before the outputs are passed to the next device in the pipeline where a different group of operations are performed. Some approaches (Harlap et al., 2018; Chen et al., 2018) use a parameter server (Li et al., 2014) in conjunction with pipeline parallelism. However these suffer from inconsistency issues. The GPipe framework for TensorFlow (Huang et al., 2018) overcomes this inconsistency issue by using synchronous gradient decent. This approach requires additional logic to handle the efficient pipelining of these communication and computation operations, and suffers from pipeline bubbles that reduce efficiency, or changes to the optimizer itself which impact accuracy. 

Distributed tensor computation is an orthogonal and more general approach that partitions a tensor operation across multiple devices to accelerate computation or increase model size. FlexFlow (Jia et al., 2018), a deep learning framework orchestrating such parallel computation, provides a method to pick the best parallelization strategy. Recently, Mesh-TensorFlow (Shazeer et al., 2018) introduced a language for specifying a general class of distributed tensor computations in TensorFlow (Abadi et al., 2015). The parallel dimensions are specified in the language by the end user and the resulting graph is compiled with proper collective primitives. We utilize similar insights to those leveraged in Mesh-TensorFlow and exploit parallelism in computing the transformer’s attention heads to parallelize our transformer model. However, rather than implementing a framework and compiler for model parallelism, we make only a few targeted modifications to existing PyTorch transformer implementations. Our approach is simple, does not 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

require any new compiler or code re-writing, and can be fully implemented by inserting a few simple primitives, as described in the next section.

---

[referencia=09b3a2927fbd8693 score=0.801]
In this work, we implement a simple and efficient model parallel approach using intra-layer model-parallelism. We exploit the inherent structure in transformer based language models to make a simple model-parallel implementation that trains efficiently in PyTorch, with no custom C++ code or compiler required. This approach is orthogonal to pipelinebased model parallelism as advocated by approaches such as GPipe (Huang et al., 2018). 

To demonstrate the scalability of our approach, we establish 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 



_Figure 1._ Model (blue) and model+data (green) parallel FLOPS as a function of number of GPUs. Model parallel (blue): up to 8-way model parallel weak scaling with approximately 1 billion parameters per GPU (e.g. 2 billion for 2 GPUs and 4 billion for 4 GPUs). Model+data parallel (green): similar configuration as model parallel combined with 64-way data parallel. 

- We show that careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased accuracies as the model grows. 

- We demonstrate that scaling the model size results in improved accuracies for both GPT-2 (studied up to 8.3 billion parameters) and BERT (studied up to 3.9B parameters) models. 

- We showcase that our models achieve state of the art results on test sets: perplexity on WikiText103 (10.8 ppl), accuracy on LAMBADA (66.5%), and accuracy on RACE (90.9%). 

- We open source our code along with the training and evaluation pipelines at https://github _._ com/ NVIDIA/Megatron-LM

---

[referencia=09b3a2927fbd8693 score=0.765]
## **6. Conclusion and Future Work** 

In this work, we successfully surpassed the limitations posed by traditional single-GPU-per-model training by implementing model parallelism with only a few modifications to the existing PyTorch transformer implementations. We efficiently trained transformer based models up to 8.3 billion parameter on 512 NVIDIA V100 GPUs with 8-way model parallelism and achieved up to 15.1 PetaFLOPs sustained over the entire application. We also showed that for BERT models, careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased accuracies as the model size increases. We study the effect of model size on down-stream task accuracy and achieve far superior results on downstream tasks and establish new SOTA for WikiText103, LAMBADA, and RACE datasets. Finally, we open sourced our code to enable future work leveraging model parallel transformers. 

There are several directions for future work. Continuing to increase the scale of pretraining is a promising line of 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

investigation that will further test existing deep learning hardware and software. To realize this, improvements in the efficiency and memory footprint of optimizers will be needed. In addition, training a model with more than 16 billion parameters will demand more memory than is available within 16 GPUs of a DGX-2H box. For such models, a hybrid intra-layer and inter-layer model parallelism along with inter-node model parallelism would be more suitable. Three other directions of investigation include (a) pretraining different model families (XLNet, T5), (b) evaluating performance of large models across more difficult and diverse downstream tasks (e.g. Generative Question Answering, Summarization, and Conversation), and (c) using knowledge distillation to train small student models from these large pretrained teacher models.

---

[referencia=09b3a2927fbd8693 score=0.649]
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

[referencia=09b3a2927fbd8693 score=0.605]
### **5.3. Bi-directional Transformer Results Using BERT** 

In this section, we apply our methodology to BERT-style transformer models and study the effect of model scaling on several downstream tasks. Prior work (Lan et al., 2019) found that increasing model size beyond BERT-large with 336M parameters results in unexpected model degradation. To address this degradation, the authors of that work (Lan et al., 2019) introduced parameter sharing and showed that that their models scale much better compared to the original BERT model. 

We further investigated this behaviour and empirically demonstrated that rearranging the order of the layer normalization and the residual connections as shown in Figure 7 is critical to enable the scaling of the BERT-style models beyond BERT-Large. The architecture (b) in Figure 7 eliminates instabilities observed using the original BERT architecture in (a) and also has a lower training loss. To the best of our knowledge, we are the first to report such a change enables training larger BERT models. 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

_Table 5._ Development set results for MNLI, QQP, SQuAD 1.1 and SQuAD 2.0 and test set results for RACE. The trained tokens represents consumed tokens during model pretraining (proportional to batch size times number of iterations) normalized by consumed tokens during model pretraining for our 336M model.

---

[referencia=09b3a2927fbd8693 score=0.581]
## **C. Text Samples** 

Below are some text samples generated by Megatron-LM using a context prompt. Some of the texts are cut short. 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

**Context** : A flower, sometimes known as a bloom or blossom, is the reproductive structure found in flowering plants (plants of the division Magnoliophyta, also called angiosperms). The biological function of a flower is to effect reproduction, usually by providing a mechanism for the union of sperm with eggs. 

**Megatron-LM** : The structural components of the flower are the petals and sepals, which are the reproductive organs, the hypanthium, which forms the base of the flower, and the calyx, which is the stigma. A flower is a composite structure, made up of sepals and petals, the sepals being composed of three fused tepals and the petals of two fused petals, though there are a few exceptions to this rule. The three sepals are fused to form a tube called the calyx, which is the structure that attracts the pollinating insects. The petals are composed of two fused sepals (the outer ones) which open and fold inward (clasp) at the tips, forming the petals. The four sepals and petals are united to form a corolla, the outermost structure of a flower that carries pollen. 

The structure of the flower has important functional significance, including protection of the ovary from insects and the transfer of pollen between the male and female parts of a flower. The structure of the flower is also used by the plants to attract pollinators, for example by the shape of the petals and the colours of the stamens. 

The structure of a flower varies widely between plants. The simplest flowers are unbranched and made up of only two sepals and a single petal. Other examples are composed of several petals joined together, with the innermost sepals completely fused to form a tube called the calyx. The petals are usually coloured to attract insects, which can only see certain wavelengths of light. The sepals are often coloured too, but usually have a more limited range of colours.

---

[referencia=09b3a2927fbd8693 score=0.554]
# **Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

**Mohammad Shoeybi**<sup>1 2</sup> **Mostofa Patwary**<sup>1 2</sup> **Raul Puri**<sup>1 2</sup> **Patrick LeGresley**<sup>2</sup> **Jared Casper**<sup>2</sup> **Bryan Catanzaro**<sup>2</sup> 

## **Abstract**

---

[referencia=09b3a2927fbd8693 score=0.512]
### **B.1. Hybrid Model and Data Parallelism** 

Model parallelism is orthogonal to data parallelism, and so we can use both simultaneously to train large models in a reasonable amount of time. Figure 8 shows a grouping of GPUs for hybrid model and data parallelism. Two or more GPUs within the same server form model parallel groups (for example GPUs 1 to 8 in Figure 8), and contain one 

Techniques that utilize random number generation, such as dropout, are a staple of modern deep learning training. Transformers have dropout layers outside the model parallel regions before residual connections and within model parallel regions in the self attention block. Because some dropout layers are in a model parallel region, while others are not, we need to treat random number generation carefully to ensure dropout works correctly. To synchronize residual connection dropout across model parallel workers we seed the random number generators at the beginning of training with the same seed. This results in identical dropout patterns across all model parallel workers. However, dropout within a model parallel region should result in different random 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

patterns for each worker to achieve randomness across the entire operation. To achieve this we maintain a separate random number generator for dropout within model parallel regions. This random number generator is uniquely seeded for each model parallel worker. 

**Context** : There is a major force uniting Americas fiercely partisan politicians: big technology companies. Democrats and Republicans at the federal and state levels are coming together to scrutinize the power of the Silicon Valley giants and, potentially, to rein them in. Letitia James, the Democratic attorney general of New York, announced on Friday that attorneys general in eight states four Democrats and four Republicans and the District of Columbia had begun an antitrust investigation of Facebook. 

**Megatron-LM** : The probe, which Ms. James said was likely to result in a lawsuit, is the latest in a string of highprofile regulatory actions, in state and federal courts, that challenge the market dominance of tech companies. The Justice Department is also investigating Facebook’s data practices and whether the company violated a 2011 consent decree with the Federal Trade Commission that required the company to obtain explicit consent from users before sharing their personal information with third parties. 



_Figure 8._ Grouping of GPUs for hybrid model and data parallelism with 8-way model parallel and 64-way data parallel.

---

[referencia=09b3a2927fbd8693 score=0.473]
### **4.2. Training Optimization and Hyperparameters** 

To train our models efficiently we utilize mixed precision training with dynamic loss scaling to take advantage of the V100’s Tensor Cores (Micikevicius et al., 2017; NVIDIA, 2018). We start by initializing our weights _W_ with a simple normal distribution _W ∼N_ (0 _,_ 0 _._ 02). We then scale weights immediately before residual layers by _~~√~~_ 21 _N_<sup>where</sup> N is the number of transformer layers comprised of self attention and MLP blocks. For our optimizer we utilize Adam (Kingma & Ba, 2014) with weight decay (Loshchilov & Hutter, 2019) _λ_ = 0 _._ 01. Additionally, we use global gradient norm clipping of 1.0 to improve the stability of training large models. In all cases, a dropout of 0.1 is used. Lastly, to better manage our memory footprint we utilize activation checkpointing (Chen et al., 2016) after every transformer layer. 

For GPT-2 models, all training is performed with sequences of 1024 subword units at a batch size of 512 for 300k itera- 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

tions. Our learning rate of 1.5e-4 utilizes a warmup period of 3k iterations before following a single cycle cosine decay over the remaining 297k iterations. We stop the decay at a minimum learning rate of 1e-5. 

For BERT models, we largely follow the training process described in (Lan et al., 2019). We use the original BERT dictionary with vocab size of 30,522. In addition, we replace the next sentence prediction head with sentence order prediction as suggested by (Lan et al., 2019) and use whole word n-gram masking of (Joshi et al., 2019). For all cases, we set the batch size to 1024 and use a learning rate of 1.0e4 warmed up over 10,000 iterations and decayed linearly over 2 million iterations. Other training parameters are kept the same as (Devlin et al., 2018).

---

[referencia=09b3a2927fbd8693 score=0.440]
- Kingma, D. P. and Ba, J. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

- Lai, G., Xie, Q., Liu, H., Yang, Y., and Hovy, E. Race: Large-scale reading comprehension dataset from examinations. _arXiv:1704.04683_ , 2017. 

- Lan, Z., Chen, M., Goodman, S., Gimpel, K., and Soricut, P. S. R. Albert: A lite bert for self-supervised learning of language representations. _arXiv:1909.11942_ , 2019. 

- Li, M., Andersen, D. G., Park, J. W., Smola, A. J., Ahmed, A., Josifovski, V., Long, J., Shekita, E. J., and Su, B.-Y. Scaling distributed machine learning with the parameter server, 2014. 

- Liu, X., He, P., Chen, W., and Gao, J. Multi-task deep neural networks for natural language understanding. _CoRR_ , abs/1901.11504, 2019a. URL http://arxiv _._ org/ abs/1901 _._ 11504. 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism**

---

[referencia=09b3a2927fbd8693 score=0.348]
### **2.2. Transformer Language Models and Multi-Head Attention** 

Current work in NLP trends towards using _transformer_ models (Vaswani et al., 2017) due to their superior accuracy 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 



_Figure 2._ Transformer Architecture. Purple blocks correspond to fully connected layers. Each blue block represents a single transformer layer that is replicated N times. 

and compute efficiency. The original transformer formulation was designed as a machine translation architecture that transforms an input sequence into another output sequence using two parts, an _Encoder_ and _Decoder_ . However, recent work leveraging transformers for language modeling such as BERT (Devlin et al., 2018) and GPT-2 (Radford et al., 2019) use only the _Encoder_ or _Decoder_ depending on their needs. This work explores both a decoder architecture, GPT-2, and an encoder architecture, BERT. 

Figure 2 shows a schematic diagram of the model we used. We refer the reader to prior work for a detailed description of the model architecture (Vaswani et al., 2017; Devlin et al., 2018; Radford et al., 2019). It is worthwhile to mention that both GPT-2 and BERT use GeLU (Hendrycks & Gimpel, 2016) nonlinearities and layer normalization (Ba et al., 2016) to the input of the multi-head attention and feed forward layers, whereas the original transformer (Vaswani et al., 2017) uses ReLU nonlinearities and applies layer normalization to outputs.

---

[referencia=09b3a2927fbd8693 score=0.339]
**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 



_Figure 4._ Communication operations in a transformer layer. There are 4 total communication operations in the forward and backward pass of a single model parallel transformer layer. 

contains a portion of the embedding table, an all-reduce ( _g_ operator) is required after the input embedding. For the output embedding, one approach is to perform the parallel GEMM [ _Y_ 1 _, Y_ 2] = [ _XE_ 1 _, XE_ 2] to obtain the logits, add an all-gather _Y_ = all-gather([ _Y_ 1 _, Y_ 2]), and send the results to the cross-entropy loss function. However, for this case, the all-gather will communicate _b × s × v_ elements ( _b_ is the batch-size and _s_ is the sequence length) which is huge due to vocabulary size being large. To reduce the communication size, we fuse the output of the parallel GEMM [ _Y_ 1 _, Y_ 2] with the cross entropy loss which reduces the dimension to _b × s_ . Communicating scalar losses instead of logits is a huge reduction in communication that improves the efficiency of our model parallel approach. 

Much of our model parallel approach can be characterized as techniques aimed at reducing communication and keeping the GPUs compute bound. Rather than having one GPU compute part of the dropout, layer normalization, or residual connections and broadcast the results to other GPUs, we choose to duplicate the computation across GPUs. Specifically, we maintain duplicate copies of layer normalization parameters on each GPU, and take the output of the model parallel region and run dropout and residual connection on these tensors before feeding them as input to the next model parallel regions. To optimize the model we allow each model parallel worker to optimize its own set of parameters. Since all values are either local to or duplicated on a GPU, there is no need for communicating updated parameter values in this formulation. 

We present further details about the hybrid model and data parallelism and handling random number generation in Appendix B for reference. In summary, our approach as described above is simple to implement, requiring only a few extra all-reduce operations added to the forward and backward pass. It does not require a compiler, and is orthogonal and complementary to the pipeline model parallelism advocated by approaches such as (Huang et al., 2018).

---

[referencia=09b3a2927fbd8693 score=0.294]
### **5.2. Language Modeling Results Using GPT-2** 

To demonstrate that large language models can further advance the state of the art, we consider training GPT-2 models of the sizes and configurations listed in Table 2. The 355M model is equivalent in size and configuration of BERT-Large model (Devlin et al., 2018). The 2.5B model is bigger than the previous largest GPT-2 model, and the 8.3B model is larger than any left-to-right transformer language model ever trained, to the best of our knowledge. To train and eval- 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

_Table 2._ Model configurations used for GPT-2. 

|Parameter<br>Count|Layers|Hidden<br>Size|Attn<br>Heads|Hidden<br>Size<br>per|Total<br>GPUs|Time<br>per<br>Epoch|
|---|---|---|---|---|---|---|
|||||Head||(days)|
|355M|24|1024|16|64|64|0.86|
|2.5B|54|1920|20|96|128|2.27|
|8.3B|72|3072|24|128|512|2.10|



_Table 3._ Zero-shot results. SOTA are from (Khandelwal et al., 2019) for Wikitext103 and (Radford et al., 2019) for LAMBADA. 

|Model|Wikitext103|LAMBADA|
|---|---|---|
||Perplexity _↓_|Accuracy _↑_|
|355M|19.31|45.18%|
|2.5B|12.76|61.73%|
|8.3B|**10.81**|**66.51%**|
|Previous SOTA|15.79|63.24%|





_Figure 6._ Validation set perplexity. All language models are trained for 300k iterations. Larger language models converge noticeably faster and converge to lower validation perplexities than their smaller counterparts. 

_Table 4._ Model configurations used for BERT.

---

[referencia=09b3a2927fbd8693 score=0.232]
The problems with the model are many. One of the biggest issues is that grammatical rules are ambiguous. For example, the phrase ”I came down” could mean I came down from the stairs, or I came down from the sky. In English, there are numerous other examples of sentences that are ambiguous. The model does not have any way to tell the difference between the ambiguous sentences, and so it simply makes a prediction about the entire sentence based on what rules it does know. This makes the model vulnerable to the phenomenon of overfitting. In order to avoid this, models must be trained using a large set of data, so that the model can find useful patterns in the data, and use those patterns to help make predictions. This approach is also prone to errors, as it relies on the training data to help make correct predictions, and the data might be incorrectly labeled, resulting in a model that produces a poor set of predictions. In the case of GPT-2, the model only has about 100 training sentences for each type of phrase (subject-verb-object). 

Additionally, languages have different rules for different types of phrasing. In English, the subject-verb-object construction is fairly universal, but other languages have different rules, which makes training a GPT more complicated. 

Finally, there is an inherent trade-off between the number of rules and the performance of the model ... 

**Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** 

**Context** : The 36th International Conference on Machine Learning (ICML 2019) will be held in Long Beach, CA, USA from June 10th to June 15th, 2019. The conference will consist of one day of tutorials (June 10), followed by three days of main conference sessions (June 11-13), followed by two days of workshops (June 14-15). 

**Megatron-LM** : With a broad scope, the conference addresses the challenges and opportunities in machine learning for practitioners and researchers. The conference program will feature sessions that cover different machine learning topics, from reinforcement learning to computational biology and from AI to deep learning. It is the world’s premier forum for exploring and presenting advances in machine learning. 

ICML 2019 will offer an impressive range of sessions, which will be of interest to practitioners, researchers, and students. Some of the topics we will cover include:

---

[referencia=09b3a2927fbd8693 score=0.179]
### **2.3. Data and Model Parallelism in Deep Learning** 

There are two central paradigms for scaling out deep neural network training to numerous hardware accelerators: data parallelism (Valiant, 1990) where a training minibatch is split across multiple workers, and model parallelism in which the memory usage and computation of a model is distributed across multiple workers. By increasing the minibatch size proportionally to the number of available workers (i.e. _weak scaling_ ), one observes near linear scaling in training data throughput. However, large batch training introduces complications into the optimization process that can result in reduced accuracy or longer time to convergence, offsetting the benefit of increased training throughput (Keskar et al., 2017). Further research (Goyal et al., 2017; You et al., 2017; 2019) has developed techniques to miti- 

gate these effects and drive down the training time of large neural networks. To scale out training even further, parallel work (Chen et al., 2016) has combined data parallelism with activation checkpointing: recomputing activations in the backward pass without storing them in the forward pass to reduce memory requirements. 

However, these techniques have one fundamental limitation in the problem size they can tackle: the model must fit entirely on one worker. With language models of increasing size and complexity like BERT and GPT-2, neural networks have approached the memory capacity of modern hardware accelerators. One solution to this problem is to employ parameter sharing to reduce the memory footprint of the model (Lan et al., 2019), but this limits the overall capacity of the model. Our approach is to utilize model parallelism to split the model across multiple accelerators. This not only alleviates the memory pressure, but also increases the amount of parallelism independently of the microbatch size.

---

[referencia=09b3a2927fbd8693 score=0.177]
|class f(torch.autograd.Function):|
|---|
|def forward(ctx, x):|
|return x|
|def backward(ctx, gradient):|
|all_reduce(gradient)|
|return gradient|



- _Code 1._ Implementation of _f_ operator. _g_ is similar to _f_ with identity in the backward and all-reduce in the forward functions. 





_Figure 3._ Blocks of Transformer with Model Parallelism. _f_ and _g_ are conjugate. _f_ is an identity operator in the forward pass and all reduce in the backward pass while _g_ is an all reduce in the forward pass and identity in the backward pass. 

As shown in Figure 3b, for the self attention block we exploit inherent parallelism in the multihead attention operation, partitioning the GEMMs associated with key ( _K_ ), query ( _Q_ ), and value ( _V_ ) in a column parallel fashion such that the matrix multiply corresponding to each attention head is done locally on one GPU. This allows us to split per attention head parameters and workload across the GPUs, and doesnt require any immediate communication to complete the self-attention. The subsequent GEMM from the output linear layer (after self attention) is parallelized along its rows and takes the output of the parallel attention layer directly, without requiring communication between the GPUs. This approach for both the MLP and self attention layer fuses groups of two GEMMs, eliminates a synchronization point in between, and results in better scaling. This enables us to perform all GEMMs in a simple transformer layer using only two all-reduces in the forward path and two in the backward path (see Figure 4). 

The transformer language model has an output embedding with the dimension of hidden-size ( _H_ ) times vocabularysize ( _v_ ). Since the vocabulary size is on the order of tens of thousands of tokens for modern language models (for example, GPT-2 used a vocabulary size of 50,257), it is beneficial to parallelize the output embedding GEMM. However, in transformer language models, the output embedding layer shares weights with the input embedding, requiring modifications to both. We parallelize the input embedding weight matrix _EH×v_ along the vocabulary dimension _E_ = [ _E_ 1 _, E_ 2] (column-wise). Since each partition now only

---

[referencia=09b3a2927fbd8693 score=0.145]
## **A. BERT Finetuning Hyperparameters** 

Table 6 presents the hyperparameters used for each model and task during finetuning. 

instance of the model distributed across these GPUs. The remaining GPUs, which could be within the same server but more typically are located in other servers, run additional model parallel groups. GPUs with the same position in each of the model parallel groups (for example GPUs 1, 9, ..., 505 in Figure 8) form data parallel groups so that all GPUs within a data parallel group hold the same model parameters. During back propagation we run multiple gradient all-reduce operations in parallel to reduce weight gradients within each distinct data parallel group. The total number of required GPUs is the product of the number of model and data parallel groups. For example, for the 8.3 billion parameter model we use 8 GPUs per model parallel group and 64-way data parallelism, for a total of 512 GPUs. All communication is implemented in PyTorch by Python calls to NCCL. GPUs within each model parallel group perform all-reduces amongst all GPUs within the group. For data parallelism, each of the all-reduce operations takes place with one of the GPUs from each model parallel group. 

### **B.2. Model Parallel Random Number Generation**

---

[referencia=09b3a2927fbd8693 score=0.135]
## **1. Introduction** 

Recent work in language modeling demonstrates that training large transformer models advances the state of the art in Natural Language Processing applications. However, very large models can be quite difficult to train due to memory constraints. In this work, we present our techniques for training very large transformer models and implement a simple, efficient intra-layer model parallel approach that enables training transformer models with billions of parameters. Our approach does not require a new compiler or library changes, is orthogonal and complimentary to pipeline model parallelism, and can be fully implemented with the insertion of a few communication operations in native PyTorch. We illustrate this approach by converging transformer based models up to 8.3 billion parameters using 512 GPUs. We sustain 15.1 PetaFLOPs across the entire application with 76% scaling efficiency when compared to a strong single GPU baseline that sustains 39 TeraFLOPs, which is 30% of peak FLOPs. To demonstrate that large language models can further advance the state of the art (SOTA), we train an 8.3 billion parameter transformer language model similar to GPT-2 and a 3.9 billion parameter model similar to BERT. We show that careful attention to the placement of layer normalization in BERT-like models is critical to achieving increased performance as the model size grows. Using the GPT-2 model we achieve SOTA results on the WikiText103 (10.8 compared to SOTA perplexity of 15.8) and LAMBADA (66.5% compared to SOTA accuracy of 63.2%) datasets. Our BERT model achieves SOTA results on the RACE dataset (90.9% compared to SOTA accuracy of 89.4%). 

> 1Equal contribution 2NVIDIA. Correspondence to: Mohammad Shoeybi _<_ mshoeybi@nvidia.com _>_ .

---

[referencia=09b3a2927fbd8693 score=0.117]
- Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., Corrado, G. S., Davis, A., Dean, J., Devin, M., Ghemawat, S., Goodfellow, I., Harp, A., Irving, G., Isard, M., Jia, Y., Jozefowicz, R., Kaiser, L., Kudlur, M., Levenberg, J., Mane,´ D., Monga, R., Moore, S., Murray, D., Olah, C., Schuster, M., Shlens, J., Steiner, B., Sutskever, I., Talwar, K., Tucker, P., Vanhoucke, V., Vasudevan, V., Viegas, F., Vinyals, O., Warden, P., Watten-´ berg, M., Wicke, M., Yu, Y., and Zheng, X. TensorFlow: Large-scale machine learning on heterogeneous systems, 2015. URL http://tensorflow _._ org/. Software available from tensorflow.org. 

- Ba, J. L., Kiros, J. R., and Hinton, G. E. Layernorm. _CoRR_ , abs/1607.06450, 2016. URL http://arxiv _._ org/ abs/1607 _._ 06450. 

- Chen, C.-C., Yang, C.-L., and Cheng, H.-Y. Efficient and robust parallel dnn training through model parallelism on multi-gpu platform. _arXiv:1809.02839_ , 2018. 

- Chen, T., Xu, B., Zhang, C., and Guestrin, C. Training deep nets with sublinear memory cost. _CoRR_ , abs/1604.06174, 2016. URL http://arxiv _._ org/ abs/1604 _._ 06174.

---

[referencia=09b3a2927fbd8693 score=0.076]
## **5. Experiments** 

All of our experiments use up to 32 DGX-2H servers (a total of 512 Tesla V100 SXM3 32GB GPUs). Our infrastructure is optimized for multi-node deep learning applications, with 300 GB/sec bandwidth between GPUs inside a server via NVSwitch and 100 GB/sec of interconnect bandwidth between servers using 8 InfiniBand adapters per server. 

### **5.1. Scaling Analysis** 

To test the scalability of our implementation, we consider GPT-2 models with four sets of parameters detailed in Table 1. To have consistent GEMM sizes in the self attention layer, the hidden size per attention head is kept constant at 96 while the number of heads and layers are varied to obtain configurations ranging from 1 billion to 8 billion parameters. The configuration with 1.2 billion parameters fits on a single GPU whereas the 8 billion parameter model requires 8-way model parallelism (8 GPUs). The original vocabulary size was 50,257, however, to have efficient GEMMs for the logit layer, it is beneficial for the per-GPU vocabulary size to be a multiple of 128. Since we study up to 8-way model parallelism, we pad the vocabulary such that it is divisible by 128 _×_ 8 = 1024, resulting in a padded vocabulary size of 51,200. We study both model and model+data parallel scaling. For the model parallel scaling, a fixed batch size of 8 is used across all configurations. Data parallel scaling is necessary for training many state of the art models which typically use a much larger global batch size. To this end, for the model+data parallel cases we fix the global batch size to 512 for all experiments which corresponds to 64-way data parallelism.