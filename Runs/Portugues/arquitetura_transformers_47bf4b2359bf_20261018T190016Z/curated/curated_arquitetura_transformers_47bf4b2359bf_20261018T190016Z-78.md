[referencia=958844d4171dd73c score=0.975]
# **Ring Attention with Blockwise Transformers for Near-Infinite Context** 

### **Hao Liu, Matei Zaharia, Pieter Abbeel** 

UC Berkeley 

```
hao.liu@cs.berkeley.edu
```

## **Abstract** 

Transformers have emerged as the architecture of choice for many state-of-the-art AI models, showcasing exceptional performance across a wide range of AI applications. However, the memory demands imposed by Transformers limit their ability to handle long sequences, thereby posing challenges in utilizing videos, actions, and other long-form sequences and modalities in complex environments. We present a novel approach, Ring Attention with Blockwise Transformers (Ring Attention), which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. Our approach enables training and inference of sequences that are up to device count times longer than those achievable by prior memory-efficient Transformers, without resorting to approximations or incurring additional communication and computation overheads. Extensive experiments on language modeling and reinforcement learning tasks demonstrate the effectiveness of our approach in allowing millions of tokens context size and improving performance.<sup>1</sup> .

---

[referencia=958844d4171dd73c score=0.947]
**Ring-Based Blockwise Attention.** To tackle the aforementioned challenges, we leverage the permutation invariance property of the inner loop’s key-value block operations. This property stems from the fact that the self-attention between a query block and a group of key-value blocks can be computed in any order, as long as the statistics of each block are combined correctly for rescaling. We leverage this property by conceptualizing all hosts as forming a ring structure: host-1, host-2, ..., host- _N_ . As we compute blockwise attention and feedforward, each host efficiently coordinates by concurrently sending key-value blocks being used for attention computation to the next host while receiving key-value blocks from the preceding host, effectively overlapping transferring of blocks with blockwise computation. Concretely, for any host- _i_ , during the computation of attention between its query block and a key-value block, it concurrently sends key-value blocks to the next host-( _i_ + 1) while receiving key-value blocks from the preceding host-( _i −_ 1). If the computation time exceeds the time required for transferring key-value blocks, this results in no additional communication cost. This overlapping mechanism applies to both forward and backward passes of our approach since the same operations and techniques can be used. Prior work has also proposed leveraging a ring topology to compute self-attention [21], aiming to reduce communication costs. Our work differs by utilizing blockwise parallel transformers to substantially reduce memory costs. As we show in the next section, this enables zero-overhead scaling of context size during both training and inference and allows arbitrarily large context size. 

**Arithmetic Intensity Between Hosts.** In order to determine the minimal required block size to overlap transferring with computation, assume that each host has _F_ FLOPS and that the bandwidth 

3

---

[referencia=958844d4171dd73c score=0.935]
## **C Inference requirement** 

We provide the minimal sequence length required to overlap communication with computation during training in Table 2. Ring Attention enables effortless training of context size that scales linearly with the number of devices. While we focus on introducing training as it is more memory demanding than autoregressive inference where the number of query token is one, Ring Attention is applicable to inference too. For example, serving a LLaMa 7B on 32x TPUv5e, the conventional approach is to distribute the model along the attention heads dimension, with each device computing one attention head. Assuming a batch size of 1, this can serve up to a 256K context length due to key-value cache activation size. Ring Attention can allow 32 times larger context by circulating the key-value cache between a ring of devices. To overlap the communication with computation, it needs d2/F >= 2*d2/B, where B/F >=2. With a bandwidth of 186 GB/s and flops of 196 TFLOPs, and assuming an 

14

---

[referencia=958844d4171dd73c score=0.903]
**Arithmetic Intensity Between Hosts.** In order to determine the minimal required block size to overlap transferring with computation, assume that each host has _F_ FLOPS and that the bandwidth 

3 



Figure 2: **Top (a):** We use the same model architecture as the original Transformer but reorganize the compute. In the diagram, we explain this by showing that in a ring of hosts, each host holds one query block, and key-value blocks traverse through a ring of hosts for attention and feedforward computations in a block-by-block fashion. As we compute attention, each host sends key-value blocks to the next host while receives key-value blocks from the preceding host. The communication is overlapped with the computation of blockwise attention and feedforward. **Bottom (b):** We compute the original Transformer block-by-block. Each host is responsible for one iteration of the query’s outer loop, while the key-value blocks rotate among the hosts. As visualized, a device starts with the first query block on the left; then we iterate over the key-value blocks sequence positioned horizontally. The query block, combined with the key-value blocks, are used to compute self-attention (yellow box), whose output is pass to feedforward network (cyan box). 

between hosts is denoted as _B_ . It’s worth noting that our approach involves interactions only with the immediately previous and next hosts in a circular configuration, thus our analysis applies to both GPU all-to-all topology and TPU torus topology. Let’s consider the variables: block size denoted as _c_ and hidden size as _d_ . When computing blockwise self-attention, we require 2 _dc_<sup>2</sup> FLOPs for calculating attention scores using queries and keys, and an additional 2 _dc_<sup>2</sup> FLOPs for multiplying these attention scores by values. In total, the computation demands amount to 4 _dc_<sup>2</sup> FLOPs. We exclude the projection of queries, keys, and values, as well as blockwise feedforward operations, since they only add compute complexity without any communication costs between hosts. This simplification leads to more stringent condition and does not compromise the validity of our approach. On the communication front, both key and value blocks require a total of 2 _cd_ bytes. Thus, the combined communication demand is 4 _cd_ bytes. To achieve an overlap between communication and 

4

---

[referencia=958844d4171dd73c score=0.902]
## **3 Ring Attention with Blockwise Parallel Transformers** 

Our primary objective is to eliminates the memory constraints imposed by individual devices by efficiently distribute long sequences across multiple hosts without adding overhead. To achieve this goal, we propose an enhancement to the blockwise parallel transformers (BPT) framework [23]. When distributing an input sequence across different hosts, each host is responsible for running one element of the outer loop of blockwise attention corresponding to its designated block, as well as the feedforward network specific to that block. These operations do not necessitate communication with other hosts. However, a challenge arises in the inner loop, which involves key-value block interactions that require fetching blocks from other hosts. Since each host possesses only one key-value block, the naive approach of fetching blocks from other hosts results in two significant issues. Firstly, it introduces a computation delay as the system waits to receive the necessary key-value blocks. Secondly, the accumulation of key-value blocks leads to increased memory usage, which defeats the purpose of reducing memory cost.

---

[referencia=958844d4171dd73c score=0.887]
**Algorithm and Implementation.** Algorithm 1 provides the pseudocode of the algorithm. Ring Attention is compatible with existing code for memory efficient transformers: Ring Attention just needs to call whatever available memory efficient computation locally on each host, and overlap the communication of key-value blocks between hosts with blockwise computation. We use collective operation `jax.lax.ppermute` to send and receive key value blocks between nearby hosts. A Jax implementation is provided in Appendix A. 

5 

**Algorithm 1** Reducing Transformers Memory Cost with Ring Attention. 

**Required:** Input sequence _x_ . Number of hosts _Nh_ . Initialize 

Split input sequence into _Nh_ blocks that each host has one input block. Compute query, key, and value for its input block on each host. **for** Each transformer layer **do for** _count_ = 1 **to** _Nh −_ 1 **do for** For each host concurrently. **do** Compute memory efficient attention incrementally using local query, key, value blocks. Send key and value blocks to next host and receive key and value blocks from previous host. 

**end for end for for** For each host concurrently. **do** Compute memory efficient feedforward using local attention output. **end for end for**

---

[referencia=958844d4171dd73c score=0.854]
> 1 Code: `https://github.com/lhao499/llm_large_context` 

Preprint. 

These components facilitate the efficient capture of long-range dependencies between input tokens, and enable scalability through highly parallel computations. To put the memory demand in perspective, even when dealing with a batch size of 1, processing 100 million tokens requires over 1000GB of memory for a modest model with a hidden size of 1024. This is much greater than the capacity of contemporary GPUs and TPUs, which typically have less than 100GB of high-bandwidth memory (HBM). 

To tackle this challenge, we make a key observation: by performing self-attention and feedforward network computations in a blockwise fashion [23], we can distribute sequence dimensions across multiple devices, allowing concurrent computation and communication. This insight stems from the fact that when we compute the attention on a block-by-block basis, the results are invariant to the ordering of these blockwise computations. Our method distributes the outer loop of computing blockwise attention among 



Figure 1: Maximum context length under endto-end large-scale training on TPUv4-1024. Baselines are vanilla transformers [37], memory efficient transformers [30], and memory efficient attention and feedforward (blockwise parallel transformers) [23]. Our proposed approach Ring Attention allows training up to device count times longer sequence than baselines and enables the training of sequences that exceed millions in length without making approximations nor adding any overheads to communication and computation.

---

[referencia=958844d4171dd73c score=0.783]
 48 `q_chunk_idx_start = q_block_idx * (block_size // query_chunk_size)` 49 `k_chunk_idx_start = k_block_idx * (block_size // key_chunk_size)` 50 `dq, dk, dv = _blockwise_attention_bwd(q, k, v, g, (dq, dk, dv, output, denominator, max_score),` 51 `q_chunk_idx_start, k_chunk_idx_start, bias=attn_bias_slice, **blockwise_kwargs)` 52 `k, v, dk, dv = map(lambda x: lax.ppermute(x, axis_name, perm=[(i,` 53 `(i + 1) % axis_size) for i in range(axis_size)]), (k, v, dk, dv))` 54 `return (dq, dk, dv, k, v), None` 55 `(dq, dk, dv, k, v), _ = lax.scan(scan_kv_block, init=(dq, dk, dv, k, v), xs=jnp.arange(0, axis_size))` 56 `dq, dk, dv = dq.astype(q.dtype), dk.astype(k.dtype), dv.astype(v.dtype)` 57 `return dq, dk, dv, None` 58 59 `@partial(jax.custom_vjp, nondiff_argnums=[4, 5, 6])` 60 `def ring_attention(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs):` 61 `y, _ = _ring_attention_fwd(q, k, v, attn_bias, axis_name, float32_logits, blockwise_kwargs)` 62 `return y` 63 64 `ring_attention.defvjp(_ring_attention_fwd, _ring_attention_bwd)` 

Figure 4: Key parts of the implementation of Ring Attention in Jax. We use collective operation `lax.ppermute` to send and receive key value blocks between previous and next hosts. 

15 

unreasonably high MFU of 40% for this large context, then B/F = 2.4, meaning that Ring Attention allows 32 times larger context for inference without adding overheads.

---

[referencia=958844d4171dd73c score=0.782]
hosts, with each device managing its respective input block. For the inner loop, every device computes blockwise attention and feedforward operations specific to its designated input block. Host devices form a conceptual ring, where during the inner loop, each device sends a copy of its key-value blocks being used for blockwise computation to the next device in the ring, while simultaneously receiving key-value blocks from the previous one. As long as block computations take longer than block transfers, overlapping these processes results in no added overhead compared to standard transformers. The use of a ring topology for computing self-attention has also been studied in prior work [21] but it incurs non-overlapped communication overheads similar to sequence parallelism, making it infeasible for large context sizes. Our work utilizes blockwise parallel transformers [23] to substantially reduce memory costs, enabling zero-overhead scaling of context size across tens of millions of tokens during both training and inference, and allowing for the use of an arbitrarily large context size. Since our approach overlaps the communication of key-value blocks between hosts in a ring through blockwise computation of transformers, we name it Ring Attention with Blockwise Parallel Transformers (Ring Attention). 

We evaluate the effectiveness of our approach on language modeling benchmarks. Our experiments show that Ring Attention can reduce the memory requirements of Transformers, enabling us to train more than 500 times longer sequence than prior memory efficient state-of-the-arts and enables the training of sequences that exceed 100 million in length without making approximations to attention. Importantly, Ring Attention eliminates the memory constraints imposed by individual devices, empowering the training and inference of sequences with lengths that scale in proportion to the number of devices, essentially achieving near-infinite context size. 

Our contributions are twofold: (a) proposing a memory efficient transformers architecture that allows the context length to scale linearly with the number of devices while maintaining performance, eliminating the memory bottleneck imposed by individual devices, and (b) demonstrating the effectiveness of our approach through extensive experiments.

---

[referencia=958844d4171dd73c score=0.690]
### **5.2 Evaluating Model Flops Utilization** 

We evaluate the model flops utilization (MFU) of Ring Attention in standard training settings using fully sharded data parallelism(FSDP) [11] and tensor parallelism following LLaMA and OpenLLaMA [36, 12] with Jax SPMD. The batch size in tokens are 2M on 8/32x A100 and 4M on TPUv4-256. Our goal is investigating the impact of model size and context length on MFU, a critical performance metrics while highlighting the benefits of our approach. Table 5.1 presents the results of our experiments on MFU for different model sizes and context lengths. We present the achieved MFU using state-of-the-art memory efficient transformers BPT [23], compare it to our anticipated MFU based on these results, and demonstrate the actual MFU obtained with our approach (Ring Attention). For fair comparison, both BPT and our approach are based on the same BPT implementation on both GPUs and TPUs. 

Ring Attention trains much longer context sizes for self-attention, resulting in higher self-attention FLOPs compared to baseline models. Since self-attention has a lower MFU than feedforward, Ring Attention is expected to have a lower MFU than the baseline models. Our method offers a clear 

7 

Table 4: Model flops utilization (MFU) with different training configurations: model sizes, compute, and context lengths. Ring Attention enables training large models <u>(7B-65B)</u> on large input context sizes <u>(over</u> 4M) with negligible overheads. 



Model size 7B 13B 13B 30B 65B Compute 8x A100 8x A100 32x A100 TPUv4-1024 TPUv4-1024 Memory efficient Context size 32 16 64 16 8 attention & FFN ( _×_ 1e3) Context size Ring Attention ( _×_ 1e3) 256 128 2048 2048 1024

---

[referencia=958844d4171dd73c score=0.641]
## **A Code** 

The implementation of Ring Attention in Jax is provided in Figure 4. We use `defvjp` function to define both the forward and backward passes, and use collective operation `jax.lax.ppermute` to facilitate the exchange of key-value blocks among a ring of hosts. The provided code snippet highlights essential components of Ring Attention. We provide the complete code of our Ring Attention at `https://github.com/lhao499/llm_large_context` . 

For large scale end-to-end training on TPU or on GPU cluster with high bandwidth inter connection, we recommend using FSDP to shard large models and using Ring Attention to achieve large context. If total batch size is too large, add tensor parallelism to reduce the global batch size. The degree of parallelism can be adjusted using the `mesh_dim` parameter within the codebase. To illustrate, consider a setup with 512 devices, such as 512x A100. If the model size is 30B, you can shard it across 8 devices and allocate the remaining 32 devices for Ring Attention. This setup allows the context size to be expanded 32 times more than if you didn’t use Ring Attention. Conversely, for models sized 7B or 3B, there is no need for FSDP. This means you can utilize all 512 devices exclusively to expand the context using Ring Attention by 512 times. Building upon the result that our approach allows for a 256K context size when using 8x A100 GPUs, it suggests that by employing 512 A100 GPUs, the potential context size can be expanded to 16 million.

---

[referencia=958844d4171dd73c score=0.610]
## **6 Related Work** 

Transformers have garnered significant attention in the field of AI and have become the backbone for numerous state-of-the-art models. Several works have explored memory-efficient techniques to address the memory limitations of Transformers and enable their application to a wider range of problems. Computing exact self-attention in a blockwise manner using the tiling technique [24] has led to the development of memory efficient attention mechanisms [30] and its efficient CUDA implementation [9], and blockwise parallel transformer [23] that proposes computing both feedforward and self-attention block-by-block, resulting in a significant reduction in memory requirements. In line with these advancements, our work falls into the category of memory efficient computation for Transformers. Other works have investigated the approximation of attention mechanisms, yet these efforts have often yielded sub-optimal results or encountered challenges during scaling up. For an in-depth review of these techniques, we recommend referring to the surveys [26, 35]. Another avenue of research explores various parallelism methods, including data parallelism [10], tensor parallelism [34], pipeline parallelism [27, 15, 28], sequence parallelism [21, 18, 17], and FSDP [11, 31]. The activations of self-attention take a substantial amount of memory for large context models. Tensor parallelism can only reduce parts of activations memory and sequence parallelism introduces a significant communication overhead that cannot be fully overlapped with computation. Prior work has studied sharding along sequence and attention heads, and gathering sequences via an optimized all-to-all topology, achieving reduced communication [17]. However, this method is restricted by the number of attention heads and requires gathering the full sequence on each device. In comparison, our approach fully overlaps communication with blockwise computation, enhancing its scalability. Prior 

9

---

[referencia=958844d4171dd73c score=0.562]
|TPUv5e-256||||||
|3B|4|8|32|**4096**|128x|
|7B|2|8|16|**2048**|128x|



Our Ring Attention model consistently surpasses baselines, delivering superior scalability across diverse hardware setups. For example, with 32 A100 GPUs, we achieve over 1 million tokens in context size for 7B model, a 32 times improvement over previous best. Furthermore, when utilizing larger accelerators like TPUv4-512, Ring Attention enables a 256 times increase in context size, allows training sequences of over 30 million tokens. Furthermore, our Ring Attention model scales linearly with the number of devices, as demonstrated by the 8x improvement over previous best on 8 A100 and the 256x improvement on TPUv3-512. If a model can be trained with context size _s_ on _n_ GPUs using the blockwise attention and feedforward, with our Ring Attention approach, it becomes possible to train a model with a context size of _ns_ .

---

[referencia=958844d4171dd73c score=0.532]
### **5.1 Evaluating Max Context Size** 

We evaluate maximum supported context length using fully sharded tensor parallelsim (FSDP) [11] which is widely used in prior end-to-end training [36, 12]. We note that no tensor parallelism is considered in our evaluations since our approach is independent of tensor parallelism. Practitioners can combine our method with tensor parallelism, which we will show in Section 5.2. Using FSDP allows us to set the same batch size in tokens for baselines and our approach, ensuring a fair comparison. Concretely, on _n_ devices, FSDP is used to shard the model for baselines, which gives a sequence length of _l_ . The total batch size in tokens is _nl_ . We utilize FSDP along with Ring Attention to extend the sequence length to<sup>_<u>nl</u>_</sup> _m_<sup>and</sup><sup>_m_sequences.This means that the total batch size in tokens</sup> remains the same, but Ring Attention enables a significantly larger context size. Table 3 summarizes the results of our experiments. 

6 

Table 3: The maximum context length supported in end-to-end training using fully sharded data parallelism and various transformers architectures. We show different model sizes and accelerators. Baselines are vanilla transformer [37], transformer with memory efficient attention [30], and transformer with memory efficient attention and feedforward [23]. The context size is reported in tokens (1e3). Our Ring Attention substantially outperforms baselines and enables training sequences that are up to device count times longer than prior state-of-the-arts.

---

[referencia=958844d4171dd73c score=0.459]
advantage in terms of maintaining MFU while enabling training with significantly longer context lengths. As shown in Table 5.1, when comparing our approach to prior state-of-the-arts, it is evident that we can train very large context models without compromising MFU or throughput. **5.3 Impact on In Context RL Performance** 

We present results of applying Ring Attention for learning trial-and-error RL experience using Transformers. We report our results in Table 5, where we evaluate our proposed model on the ExoRL benchmark across six different tasks. On ExoRL, we report the cumulative return, as per ExoRL [39]. We compare BC, DT [4], AT [22], and AT with memory efficient attention [30] (AT+ME), AT with blockwise parallel transformers [23] (AT+BPT), and AT with our Ring Attention (AT+Ring Attention). The numbers of BC, DT, AT are from the ExoRL and AT paper. AT + Ring Attention numbers are run by ourselves. Since the ExoRL data is highly diverse, having been collected using unsupervised RL [19], it has been found that TD learning performs best, while behavior cloning struggles [39]. AT [22] shows that conditioning Transformer on multiple trajectories with relabeled target return can achieve competitive results with TD learning. For more details, please refer to their papers. We are interested in applying Ring Attention to improve the performance of AT by conditioning on a larger 

Table 5: Application of Ring Attention on improving Transformer in RL. BC and DT use vanilla attention. AT + ME denotes using memory efficient attention, AT + BPT denotes using blockwise parallel transformer. AT + RA denotes using Ring Attention.

---

[referencia=958844d4171dd73c score=0.409]
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

[referencia=958844d4171dd73c score=0.399]
Table 5: Application of Ring Attention on improving Transformer in RL. BC and DT use vanilla attention. AT + ME denotes using memory efficient attention, AT + BPT denotes using blockwise parallel transformer. AT + RA denotes using Ring Attention. 

**ExoRL BC-10% DT AT + ME AT + BPT AT + BPT AT + RA Task** N Trajs = 32 N Trajs = 32 N Trajs = 128 N Trajs = 128 Walker Stand 52.91 34.54 oom 95.45 oom 98.23 Walker Run 34.81 49.82 oom 105.88 oom 110.45 Walker Walk 13.53 34.94 oom 78.56 oom 78.95 Cheetah Run 34.66 67.53 oom 178.75 oom 181.34 Jaco Reach 23.95 18.64 oom 87.56 oom 89.51 Cartpole Swingup 56.82 67.56 oom 120.56 oom 123.45 **Total Average** 36.11 45.51 oom 111.13 oom **113.66** 

8 



Figure 3: Comparison of different models on the long-range line retrieval task. 

number of trajectories rather than 32 trajectories in prior works. It is worth noting that each trajectory has 1000 _×_ 4 length where 1000 is sequence length while 4 is return-state-action-reward, making training 128 trajectories with modest 350M size model infeasible for prior state-of-the-art blockwise parallel transformers. Results in Table 5 show that, by scaling up the sequence length (number of trajectories), AT + Ring Attention consistently outperforms oringal AT with BPT across all six tasks, achieving a total average return of 113.66 compared to the AT with BPT model’s total average return of 111.13. The results show that the advantage of Ring Attention for training and inference with long sequences.

---

[referencia=958844d4171dd73c score=0.355]
4 

Table 1: Comparison of maximum activation sizes among different Transformer architectures. Here, _b_ is batch size, _h_ is hidden dimension, _n_ is number of head, _s_ is sequence length, _c_ is block size, the block size ( _c_ ) is independent of the input sequence length ( _s_ ). The comparison is between vanilla Transformer [37], memory efficient attention [30], memory efficient attention and feedforward [23], and our proposed approach Ring Attention. Numbers are shown in bytes per layer, assuming _bfloat16_ precision. 

|Layer Type|Self-Attention|FeedForward|Total|
|---|---|---|---|
|Vanilla|2_bns_<sup>2</sup>|8_bsh_|2_bhs_<sup>2</sup>|
|Memory effcient attention|2_bsh_+ 4_bch_|8_bsh_|8_bsh_|
|Memory effcient attention<br>and feedforward|2_bsh_|2_bsh_|2_bsh_|
|Ring Attention|6_bch_|2_bch_|6_bch_|



Table 2: Minimal sequence length needed on each device. Interconnect Bandwidth is the unidirectional bandwidth between hosts, _i_ . _e_ ., NVLink / InfiniBand bandwidth between GPUs and ICI bandwidth between TPUs. The minimal block size required _c_ = FLOPS _/_ Bandwidth, and minimal sequence length _s_ = 6 _c_ . 

|Spec Per Host|FLOPS|HBM|Interconnect<br>Bandwidth|Minimal<br>Blocksize|Minimal<br>Sequence Len|
|---|---|---|---|---|---|
||(TF)|(GB)|(GB/s)|(_×_1e3)|(_×_1e3)|
|A100 NVLink|312|80|300|1.0|6.2|
|A100 InfniBand|312|80|12.5|24.5|149.5|
|TPU v3|123|16|112|1.1|6.6|
|TPU v4|275|32|268|1.0|6.2|
|TPU v5e|196|16|186|1.1|6.3|

---

[referencia=958844d4171dd73c score=0.302]
## **5 Results** 

In our experiments, our primary objective is to comprehensively evaluate the performance of Ring Attention across multiple key metrics, including maximum supported sequence length within accelerator memory, model flops utilization, and throughput. We compare Ring Attention’s performance with several baseline models , including the vanilla transformers [37], transformers with memory efficient attention [30], and transformers with both memory efficient attention and feedforward [23], across different model sizes and accelerator configurations.

---

[referencia=958844d4171dd73c score=0.191]
## **4 Setting** 

We evaluate the impact of using Ring Attention in improving Transformer models by benchmarking maximum sequence length and model flops utilization. 

**Model Configuration.** Our study is built upon the LLaMA architecture, we consider 3B, 7B, 13B, and 30B model sizes in our experiments. 

**Baselines.** We evaluate our method by comparing it with vanilla transformers [37] which computes self-attention by materializing the attention matrix and computes the feedforward network normally, transformers with memory efficient attention [30] and its efficient CUDA implementation [9], and transformers with both memory efficient attention and feedforward [23]. 

**Training Configuration.** For all methods, we apply full gradient checkpointing [5] to both attention and feedforward, following prior works [30, 23]. The experiments are on both GPUs and TPUs. For GPUs, we consider both single DGX A100 server with 8 GPUs and distributed 32 A100 GPUs. We also experiment with TPUs, from older generations TPUv3 to newer generations of TPUv4 and TPUv5e. We note that all of our results are obtained using full precision instead of mixed precision.