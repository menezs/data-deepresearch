[referencia=958844d4171dd73c score=0.460]
## **D Training FLOPs Scaling of Context Size** 

Given that our proposed approach unlocks the possibility of training with a context size exceeding 100 million tokens and allows for linear scaling of the context size based on the number of devices, it is essential to understand how the training FLOPs per dataset scale with the context size. While a larger context size results in a higher number of FLOPs, the increased ratio does not scale quadratically because the number of tokens remains fixed. We present these results in Figure 5, which showcases various model sizes and context lengths, representing different computational budgets. The figure shows the ratio of FLOPs for larger context lengths compared to the same model with a shorter 4K context size. We calculated the per sequence FLOPs using (24 _bsh_<sup>2</sup> + 4 _bs_<sup>2</sup> _h_ ) _n_ where _h_ is 



Figure 5: The per dataset trainig FLOPs cost ratio relative to a 4k context size, considering different model dimensions. On the x-axis, you’ll find the context length, where, for example, 32x(128k) denotes a context length of 128k, 32x the size of the same model’s 4k context length.

---

[referencia=958844d4171dd73c score=0.355]
|TPUv5e-256||||||
|3B|4|8|32|**4096**|128x|
|7B|2|8|16|**2048**|128x|



Our Ring Attention model consistently surpasses baselines, delivering superior scalability across diverse hardware setups. For example, with 32 A100 GPUs, we achieve over 1 million tokens in context size for 7B model, a 32 times improvement over previous best. Furthermore, when utilizing larger accelerators like TPUv4-512, Ring Attention enables a 256 times increase in context size, allows training sequences of over 30 million tokens. Furthermore, our Ring Attention model scales linearly with the number of devices, as demonstrated by the 8x improvement over previous best on 8 A100 and the 256x improvement on TPUv3-512. If a model can be trained with context size _s_ on _n_ GPUs using the blockwise attention and feedforward, with our Ring Attention approach, it becomes possible to train a model with a context size of _ns_ .

---

[referencia=958844d4171dd73c score=0.203]
## **C Inference requirement** 

We provide the minimal sequence length required to overlap communication with computation during training in Table 2. Ring Attention enables effortless training of context size that scales linearly with the number of devices. While we focus on introducing training as it is more memory demanding than autoregressive inference where the number of query token is one, Ring Attention is applicable to inference too. For example, serving a LLaMa 7B on 32x TPUv5e, the conventional approach is to distribute the model along the attention heads dimension, with each device computing one attention head. Assuming a batch size of 1, this can serve up to a 256K context length due to key-value cache activation size. Ring Attention can allow 32 times larger context by circulating the key-value cache between a ring of devices. To overlap the communication with computation, it needs d2/F >= 2*d2/B, where B/F >=2. With a bandwidth of 186 GB/s and flops of 196 TFLOPs, and assuming an 

14

---

[referencia=958844d4171dd73c score=0.166]
9 

work extends sequence parallelism for computing self-attention using a ring topology [21], which reduces the communication cost compared to standard sequence parallelism. However, overlapping communication with computation remains challenging due to the constraints of arithmetic intensity. The communication overheads render this approach infeasible for training and inference in largecontext scenarios. Our work leverages on blockwise parallel transformers to distribute blockwise attention and feedforward across devices and concurrently overlaps the communication of key-value blocks in a circular of hosts with the computation of query-key-value blocks and feedforward, reducing memory cost substantially and allowing device count times larger context size with zero overheads. Overlapping communication with computation has been studied in high performance computing literature [7, 38, 8, _inter alia_ ]. While ring communication has found applications in other parallel computing scenarios [2, 16, 14, 33], our work stands out as the first work to show that it can be applied to self-attention as used in Transformers and to make it fit efficiently into Transformer training and inference without adding significant overhead by overlapping blockwise computation and communication. 

## **7 Conclusion** 

In conclusion, we propose a memory efficient approach to reduce the memory requirements of Transformers, the backbone of state-of-the-art AI models. Our approach allows the context length to scale linearly with the number of devices while maintaining performance, eliminating the memory bottleneck imposed by individual devices. Through extensive experiments on language modeling and reinforcement learning, we demonstrate its effectiveness, enabling training sequences that are up to device count times longer than those of prior memory-efficient Transformers, exceeding a context length of 100 million without making approximations to attention. In terms of future prospects, the possibility of near-infinite context introduces a vast array of exciting opportunities, such as large video-audio-language models, learning from extended feedback and trial-and-errors, understanding and generating codebase, adapting AI models to understand scientific data such as gene sequences, and developing strong reasoning from link gathering data.

---

[referencia=958844d4171dd73c score=0.160]
hosts, with each device managing its respective input block. For the inner loop, every device computes blockwise attention and feedforward operations specific to its designated input block. Host devices form a conceptual ring, where during the inner loop, each device sends a copy of its key-value blocks being used for blockwise computation to the next device in the ring, while simultaneously receiving key-value blocks from the previous one. As long as block computations take longer than block transfers, overlapping these processes results in no added overhead compared to standard transformers. The use of a ring topology for computing self-attention has also been studied in prior work [21] but it incurs non-overlapped communication overheads similar to sequence parallelism, making it infeasible for large context sizes. Our work utilizes blockwise parallel transformers [23] to substantially reduce memory costs, enabling zero-overhead scaling of context size across tens of millions of tokens during both training and inference, and allowing for the use of an arbitrarily large context size. Since our approach overlaps the communication of key-value blocks between hosts in a ring through blockwise computation of transformers, we name it Ring Attention with Blockwise Parallel Transformers (Ring Attention). 

We evaluate the effectiveness of our approach on language modeling benchmarks. Our experiments show that Ring Attention can reduce the memory requirements of Transformers, enabling us to train more than 500 times longer sequence than prior memory efficient state-of-the-arts and enables the training of sequences that exceed 100 million in length without making approximations to attention. Importantly, Ring Attention eliminates the memory constraints imposed by individual devices, empowering the training and inference of sequences with lengths that scale in proportion to the number of devices, essentially achieving near-infinite context size. 

Our contributions are twofold: (a) proposing a memory efficient transformers architecture that allows the context length to scale linearly with the number of devices while maintaining performance, eliminating the memory bottleneck imposed by individual devices, and (b) demonstrating the effectiveness of our approach through extensive experiments.

---

[referencia=958844d4171dd73c score=0.157]
### **5.1 Evaluating Max Context Size** 

We evaluate maximum supported context length using fully sharded tensor parallelsim (FSDP) [11] which is widely used in prior end-to-end training [36, 12]. We note that no tensor parallelism is considered in our evaluations since our approach is independent of tensor parallelism. Practitioners can combine our method with tensor parallelism, which we will show in Section 5.2. Using FSDP allows us to set the same batch size in tokens for baselines and our approach, ensuring a fair comparison. Concretely, on _n_ devices, FSDP is used to shard the model for baselines, which gives a sequence length of _l_ . The total batch size in tokens is _nl_ . We utilize FSDP along with Ring Attention to extend the sequence length to<sup>_<u>nl</u>_</sup> _m_<sup>and</sup><sup>_m_sequences.This means that the total batch size in tokens</sup> remains the same, but Ring Attention enables a significantly larger context size. Table 3 summarizes the results of our experiments. 

6 

Table 3: The maximum context length supported in end-to-end training using fully sharded data parallelism and various transformers architectures. We show different model sizes and accelerators. Baselines are vanilla transformer [37], transformer with memory efficient attention [30], and transformer with memory efficient attention and feedforward [23]. The context size is reported in tokens (1e3). Our Ring Attention substantially outperforms baselines and enables training sequences that are up to device count times longer than prior state-of-the-arts.

---

[referencia=958844d4171dd73c score=0.037]
# **Ring Attention with Blockwise Transformers for Near-Infinite Context** 

### **Hao Liu, Matei Zaharia, Pieter Abbeel** 

UC Berkeley 

```
hao.liu@cs.berkeley.edu
```

## **Abstract** 

Transformers have emerged as the architecture of choice for many state-of-the-art AI models, showcasing exceptional performance across a wide range of AI applications. However, the memory demands imposed by Transformers limit their ability to handle long sequences, thereby posing challenges in utilizing videos, actions, and other long-form sequences and modalities in complex environments. We present a novel approach, Ring Attention with Blockwise Transformers (Ring Attention), which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. Our approach enables training and inference of sequences that are up to device count times longer than those achievable by prior memory-efficient Transformers, without resorting to approximations or incurring additional communication and computation overheads. Extensive experiments on language modeling and reinforcement learning tasks demonstrate the effectiveness of our approach in allowing millions of tokens context size and improving performance.<sup>1</sup> .

---

[referencia=958844d4171dd73c score=0.030]
## **A Code** 

The implementation of Ring Attention in Jax is provided in Figure 4. We use `defvjp` function to define both the forward and backward passes, and use collective operation `jax.lax.ppermute` to facilitate the exchange of key-value blocks among a ring of hosts. The provided code snippet highlights essential components of Ring Attention. We provide the complete code of our Ring Attention at `https://github.com/lhao499/llm_large_context` . 

For large scale end-to-end training on TPU or on GPU cluster with high bandwidth inter connection, we recommend using FSDP to shard large models and using Ring Attention to achieve large context. If total batch size is too large, add tensor parallelism to reduce the global batch size. The degree of parallelism can be adjusted using the `mesh_dim` parameter within the codebase. To illustrate, consider a setup with 512 devices, such as 512x A100. If the model size is 30B, you can shard it across 8 devices and allocate the remaining 32 devices for Ring Attention. This setup allows the context size to be expanded 32 times more than if you didn’t use Ring Attention. Conversely, for models sized 7B or 3B, there is no need for FSDP. This means you can utilize all 512 devices exclusively to expand the context using Ring Attention by 512 times. Building upon the result that our approach allows for a 256K context size when using 8x A100 GPUs, it suggests that by employing 512 A100 GPUs, the potential context size can be expanded to 16 million.

---

[referencia=958844d4171dd73c score=0.027]
> 1 Code: `https://github.com/lhao499/llm_large_context` 

Preprint. 

These components facilitate the efficient capture of long-range dependencies between input tokens, and enable scalability through highly parallel computations. To put the memory demand in perspective, even when dealing with a batch size of 1, processing 100 million tokens requires over 1000GB of memory for a modest model with a hidden size of 1024. This is much greater than the capacity of contemporary GPUs and TPUs, which typically have less than 100GB of high-bandwidth memory (HBM). 

To tackle this challenge, we make a key observation: by performing self-attention and feedforward network computations in a blockwise fashion [23], we can distribute sequence dimensions across multiple devices, allowing concurrent computation and communication. This insight stems from the fact that when we compute the attention on a block-by-block basis, the results are invariant to the ordering of these blockwise computations. Our method distributes the outer loop of computing blockwise attention among 



Figure 1: Maximum context length under endto-end large-scale training on TPUv4-1024. Baselines are vanilla transformers [37], memory efficient transformers [30], and memory efficient attention and feedforward (blockwise parallel transformers) [23]. Our proposed approach Ring Attention allows training up to device count times longer sequence than baselines and enables the training of sequences that exceed millions in length without making approximations nor adding any overheads to communication and computation.

---

[referencia=958844d4171dd73c score=0.024]
## **6 Related Work** 

Transformers have garnered significant attention in the field of AI and have become the backbone for numerous state-of-the-art models. Several works have explored memory-efficient techniques to address the memory limitations of Transformers and enable their application to a wider range of problems. Computing exact self-attention in a blockwise manner using the tiling technique [24] has led to the development of memory efficient attention mechanisms [30] and its efficient CUDA implementation [9], and blockwise parallel transformer [23] that proposes computing both feedforward and self-attention block-by-block, resulting in a significant reduction in memory requirements. In line with these advancements, our work falls into the category of memory efficient computation for Transformers. Other works have investigated the approximation of attention mechanisms, yet these efforts have often yielded sub-optimal results or encountered challenges during scaling up. For an in-depth review of these techniques, we recommend referring to the surveys [26, 35]. Another avenue of research explores various parallelism methods, including data parallelism [10], tensor parallelism [34], pipeline parallelism [27, 15, 28], sequence parallelism [21, 18, 17], and FSDP [11, 31]. The activations of self-attention take a substantial amount of memory for large context models. Tensor parallelism can only reduce parts of activations memory and sequence parallelism introduces a significant communication overhead that cannot be fully overlapped with computation. Prior work has studied sharding along sequence and attention heads, and gathering sequences via an optimized all-to-all topology, achieving reduced communication [17]. However, this method is restricted by the number of attention heads and requires gathering the full sequence on each device. In comparison, our approach fully overlaps communication with blockwise computation, enhancing its scalability. Prior 

9

---

[referencia=958844d4171dd73c score=0.012]
computation, the following condition must hold: 4 _dc_<sup>2</sup> _/F ≥_ 4 _cd/B_ . This implies that the block size, denoted as _c_ , should be greater than or equal to _F/B_ . Effectively, this means that the block size needs to be larger than the ratio of FLOPs over bandwidth. 

**Memory Requirement.** A host needs to store multiple blocks, including one block size to store the current query block, two block sizes for the current key and value blocks, and two block sizes for receiving key and value blocks. Furthermore, storing the output of blockwise attention and feedforward necessitates one block size, as the output retains the shape of the query block. Therefore, a total of six blocks are required, which translates to 6 _bch_ bytes of memory. It’s worth noting that the blockwise feedforward network has a maximum activation size of 2 _bch_ [23]. Consequently, the total maximum activation size remains at 6 _bch_ bytes. Table 1 provides a detailed comparison of the memory costs between our method and other approaches. Notably, our method exhibits the advantage of linear memory scaling with respect to the block size _c_ , and is independent of the input sequence length _s_ . 

Our analysis shows that the model needs to have a sequence length of _s_ = 6 _c_ , which is six times the minimal block size. Requirements for popular computing servers are shown in Table 2. The required minimal sequence length (rightmost column) for each host varies between 6K and 10K, and the minimal block size (second-to-rightmost column) for each host is around 1K for TPUs and GPUs with high bandwidth interconnect. For GPUs connected via InfiniBand, which offers lower bandwidth, the requirements are more strict. These requirements are easy to meet with parallelism such as data and tensor parallelism and memory efficient blockwise attention and feedforward [30, 9, 23], which we will show in experiment Section 5.

---

[referencia=958844d4171dd73c score=0.008]
## **1 Introduction** 

Transformers [37] have become the backbone of many state-of-the-art AI systems that have demonstrated impressive performance across a wide range of AI problems. Transformers achieve this success through their architecture design that uses self-attention and position-wise feedforward mechanisms. However, scaling up the context length of Transformers is a challenge [29], since the inherited architecture design of Transformers, _i_ . _e_ . the self-attention has memory cost quadratic in the input sequence length, which makes it challenging to scale to longer input sequences. Large context Transformers are essential for tackling a diverse array of AI challenges, ranging from processing books and high-resolution images to analyzing long videos and complex codebases. They excel at extracting information from the interconnected web and hyperlinked content, and are crucial for handling complex scientific experiment data. There have been emerging use cases of language models with significantly expanded context than before: GPT-3.5 [32] with context length 16K, GPT-4 [29] with context length 32k, MosaicML’s MPT [25] with context length 65k, and Anthropic’s Claude [1] with context length 100k. 

Driven by the significance, there has been surging research interests in reducing memory cost. One line of research leverages the observation that the softmax matrix in self-attention can be computed without materializing the full matrix [24] which has led to the development of blockwise computation of self-attention and feedforward [30, 9, 23] without making approximations. Despite the reduced memory, a significant challenge still arises from storing the output of each layer. This necessity arises from self-attention’s inherent nature, involving interactions among all elements (n to n interactions). The subsequent layer’s self-attention relies on accessing all of the prior layer’s outputs. Failing to do so would increase computational costs cubically, as every output must be recomputed for each sequence element, rendering it impractical for longer sequences. 

> 1 Code: `https://github.com/lhao499/llm_large_context` 

Preprint.

---

[referencia=958844d4171dd73c score=0.008]
**Ring-Based Blockwise Attention.** To tackle the aforementioned challenges, we leverage the permutation invariance property of the inner loop’s key-value block operations. This property stems from the fact that the self-attention between a query block and a group of key-value blocks can be computed in any order, as long as the statistics of each block are combined correctly for rescaling. We leverage this property by conceptualizing all hosts as forming a ring structure: host-1, host-2, ..., host- _N_ . As we compute blockwise attention and feedforward, each host efficiently coordinates by concurrently sending key-value blocks being used for attention computation to the next host while receiving key-value blocks from the preceding host, effectively overlapping transferring of blocks with blockwise computation. Concretely, for any host- _i_ , during the computation of attention between its query block and a key-value block, it concurrently sends key-value blocks to the next host-( _i_ + 1) while receiving key-value blocks from the preceding host-( _i −_ 1). If the computation time exceeds the time required for transferring key-value blocks, this results in no additional communication cost. This overlapping mechanism applies to both forward and backward passes of our approach since the same operations and techniques can be used. Prior work has also proposed leveraging a ring topology to compute self-attention [21], aiming to reduce communication costs. Our work differs by utilizing blockwise parallel transformers to substantially reduce memory costs. As we show in the next section, this enables zero-overhead scaling of context size during both training and inference and allows arbitrarily large context size. 

**Arithmetic Intensity Between Hosts.** In order to determine the minimal required block size to overlap transferring with computation, assume that each host has _F_ FLOPS and that the bandwidth 

3

---

[referencia=958844d4171dd73c score=0.007]
### FFN( _x_ ) = max(0 _, xW_ 1 + _b_ 1) _W_ 2 + _b_ 2 _._ 

**Blockwise Parallel Transformers.** Prior state-of-the-arts have led to substantial reductions in memory utilization, achieved through innovative techniques that enable attention computation without full materialization by computing attention in a block by block manner [30, 9, 23]. These advancements lowered the memory overhead of attention to 2 _bsh_ bytes per layer, where _b_ represents the batch size, _s_ denotes the sequence length, and _h_ stands for the hidden size of the model. To further reduce memory usage, blockwise parallel transformer (BPT) [23] introduced a strategy where the feedforward network associated with each self-attention sub-layer is computed in a block-wise fashion. This approach effectively limits the maximum activation size of feedforward network from 8 _bsh_ to 2 _bsh_ . For a more detailed analysis of memory efficiency, please refer to the discussion provided therein. In summary, the state-of-the-art transformer layer’s memory cost of activation is 2 _bsh_ . 

**Large Output of Each Layer.** While BPT significantly reduces memory demand in Transformers, it still presents a major challenge for scaling up context length because it requires storing the output of each layer. This storage is crucial due to the inherent nature of self-attention, which involves interactions among all elements (n to n interactions). Without these stored outputs, the subsequent layer’s self-attention becomes computationally impractical, necessitating recomputation for each sequence element. To put it simply, processing 100 million tokens with a batch size of 1 requires over 1000GB of memory even for a modest model with a hidden size of 1024. In contrast, modern GPUs and TPUs typically provide less than 100GB of high-bandwidth memory (HBM), and the prospects for significant HBM expansion are hindered by physical limitations and high manufacturing costs.

---

[referencia=958844d4171dd73c score=0.005]
|||**Max contex**|**t size supported (**_×_|1e3**)**||
|---|---|---|---|---|---|
||Vanilla|Memory<br>Effcient Attn|Memory Effcient<br>Attn and FFN|Ring Attention<br>(Ours)|Ours<br>vs SOTA|
|8x A100||||||
|NVLink||||||
|3B|4|32|64|**512**|8x|
|7B|2|16|32|**256**|8x|
|13B|2|4|16|**128**|8x|
|32x A100||||||
|InfniBand||||||
|7B|4|64|128|**4096**|32x|
|13B|4|32|64|**2048**|32x|
|TPUv3-512||||||
|7B|1|4|8|**2048**|256x|
|13B|1|2|8|**1024**|128x|
|TPUv4-1024||||||
|3B|8|16|32|**16384**|512x|
|7B|4|8|16|**8192**|512x|
|13B|4|8|16|**4096**|256x|
|30B|2|4|8|**2048**|256x|
|TPUv5e-256||||||
|3B|4|8|32|**4096**|128x|
|7B|2|8|16|**2048**|128x|

---

[referencia=958844d4171dd73c score=0.005]
 48 `q_chunk_idx_start = q_block_idx * (block_size // query_chunk_size)` 49 `k_chunk_idx_start = k_block_idx * (block_size // key_chunk_size)` 50 `dq, dk, dv = _blockwise_attention_bwd(q, k, v, g, (dq, dk, dv, output, denominator, max_score),` 51 `q_chunk_idx_start, k_chunk_idx_start, bias=attn_bias_slice, **blockwise_kwargs)` 52 `k, v, dk, dv = map(lambda x: lax.ppermute(x, axis_name, perm=[(i,` 53 `(i + 1) % axis_size) for i in range(axis_size)]), (k, v, dk, dv))` 54 `return (dq, dk, dv, k, v), None` 55 `(dq, dk, dv, k, v), _ = lax.scan(scan_kv_block, init=(dq, dk, dv, k, v), xs=jnp.arange(0, axis_size))` 56 `dq, dk, dv = dq.astype(q.dtype), dk.astype(k.dtype), dv.astype(v.dtype)` 57 `return dq, dk, dv, None` 58 59 `@partial(jax.custom_vjp, nondiff_argnums=[4, 5, 6])` 60 `def ring_attention(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs):` 61 `y, _ = _ring_attention_fwd(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs)` 62 `return y` 63 64 `ring_attention.defvjp(_ring_attention_fwd, _ring_attention_bwd)` 

Figure 4: Key parts of the implementation of Ring Attention in Jax. We use collective operation `lax.ppermute` to send and receive key value blocks between previous and next hosts. 

15 

unreasonably high MFU of 40% for this large context, then B/F = 2.4, meaning that Ring Attention allows 32 times larger context for inference without adding overheads.

---

[referencia=958844d4171dd73c score=0.002]
## **2 Large Context Memory Constraint** 

Given input sequences _Q, K, V ∈_ R<sup>_s×d_</sup> where _s_ is the sequence length and _d_ is the head dimension. We compute the matrix of outputs as: 



where softmax is applied row-wise. Each self-attention sub-layer is accompanied with a feedforward network, which is applied to each position separately and identically. This consists of two linear 

2 

transformations with a ReLU activation in between.

---

[referencia=958844d4171dd73c score=0.002]
**Arithmetic Intensity Between Hosts.** In order to determine the minimal required block size to overlap transferring with computation, assume that each host has _F_ FLOPS and that the bandwidth 

3 



Figure 2: **Top (a):** We use the same model architecture as the original Transformer but reorganize the compute. In the diagram, we explain this by showing that in a ring of hosts, each host holds one query block, and key-value blocks traverse through a ring of hosts for attention and feedforward computations in a block-by-block fashion. As we compute attention, each host sends key-value blocks to the next host while receives key-value blocks from the preceding host. The communication is overlapped with the computation of blockwise attention and feedforward. **Bottom (b):** We compute the original Transformer block-by-block. Each host is responsible for one iteration of the query’s outer loop, while the key-value blocks rotate among the hosts. As visualized, a device starts with the first query block on the left; then we iterate over the key-value blocks sequence positioned horizontally. The query block, combined with the key-value blocks, are used to compute self-attention (yellow box), whose output is pass to feedforward network (cyan box). 

between hosts is denoted as _B_ . It’s worth noting that our approach involves interactions only with the immediately previous and next hosts in a circular configuration, thus our analysis applies to both GPU all-to-all topology and TPU torus topology. Let’s consider the variables: block size denoted as _c_ and hidden size as _d_ . When computing blockwise self-attention, we require 2 _dc_<sup>2</sup> FLOPs for calculating attention scores using queries and keys, and an additional 2 _dc_<sup>2</sup> FLOPs for multiplying these attention scores by values. In total, the computation demands amount to 4 _dc_<sup>2</sup> FLOPs. We exclude the projection of queries, keys, and values, as well as blockwise feedforward operations, since they only add compute complexity without any communication costs between hosts. This simplification leads to more stringent condition and does not compromise the validity of our approach. On the communication front, both key and value blocks require a total of 2 _cd_ bytes. Thus, the combined communication demand is 4 _cd_ bytes. To achieve an overlap between communication and 

4

---

[referencia=958844d4171dd73c score=0.002]
model hidden dimension, _b_ is batch size, _s_ is total sequence length, and _n_ is number of layers. The per dataset FLOPs ratio is then given by ((24 _bs_ 2 _h_<sup>2</sup> + 4 _bs_ 2<sup>2</sup> _h_ ) _/_ (24 _bs_ 1 _h_<sup>2</sup> + 4 _bs_ 1<sup>2</sup> _h_ )) _/_ ( _s_ 2 _/s_ 1) = (6 _h_ + _s_ 2) _/_ (6 _h_ + _s_ 1), where _s_ 2 and _s_ 1 are new and old context lengths. Model sizes and their hidden dimensions are as follows: LLaMA-7B (4096), LLaMA-13B (5140), LLaMA-33B (7168), LLaMA-65B (8192), GPT3-175B (12288), and 1TB (36864). These model configurations are from LLaMA [36] and GPT-3 [3] papers, except the 1TB model size and dimension were defined by us. 

As depicted in Figure 5, scaling up small models to a 1M context size results in approximately 20-40 times more FLOPs, and even more for 10M and 100M token context sizes. However, as the model sizes increase, the cost ratio decreases. For instance, scaling up the 170B model from 4K to 10M incurs 162.6x higher per dataset FLOPs, despite the context size being 3072 times longer. 

16

---

[referencia=958844d4171dd73c score=0.002]
## **B Experiment Details** 

### **B.1 Evaluation of context length** 

In the experimental results presented in Section 5.1, we used fully sharded tensor parallelism (FSDP) to partition the model across GPUs or TPU devices. Our evaluation focused on determining the maximum achievable sequence length in commonly used FSDP training scenarios. For TPUs, we utilized its default training configuration, which involved performing matmul operations in `bfloat16` format with weight accumulation in `float32` . On the other hand, for GPUs, we adopted the default setup, where all operations were performed in `float32` . 

### **B.2 Evaluation of MFU** 

In the evaluation presented in Section 5.2. The batch size in tokens is 2 million per batch on GPU and 4 million per batch on TPU. The training was conducted using FSDP [11] with Jax SPMD. For gradient checkpointing [5], we used `nothing_saveable` as checkpointing policies for attention and feedforward network (FFN). For more details, please refer to Jax documentation. 

### **B.3 Evaluation on line retrieval** 

In the evaluation presented in Section 5.4, we finetuned the LLaMA-13B model [36], limiting context length to 512K tokens due to constraints on our cloud compute budget, the training was conducted on 32x A100 80GB Cloud GPUs. We use user-shared conversations gathered from ShareGPT.com with its public APIs for finetuning, following methodologies as outlined in prior works [6, 13]. ShareGPT is a website where users can share their ChatGPT conversations. To ensure data quality, we convert the HTML back to markdown and filter out some inappropriate or low-quality samples, which results in 125K conversations after data cleaning.