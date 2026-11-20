[referencia=8ccdf64e8c44880b score=0.773]
The Memory Wall. All  experts’ parameters, gradients, and optimizer states must reside in memory during training, even though only  activate per token. This creates memory pressure far exceeding that of a dense model with comparable per-token compute [4, 7]. Reducing this pressure requires spending elsewhere: distributing parameters across more devices costs *communication bandwidth*; recomputing activations instead of storing them costs *extra computation*; offloading to host memory costs *PCIe bandwidth*. Dynamic routing further complicates matters: uneven token distributions cause unpredictable memory spikes when some experts receive disproportionate load [12, 22].

The Communication Wall. EP requires all-to-all collectives to dispatch tokens to their assigned experts and collect results [12]. The per-GPU send volume in each all-to-all is approximately , where is the local token count, the top-, and the hidden dimension; a full dispatch-and-combine cycle doubles this. As EP grows, this volume saturates but the communication increasingly moves from high-bandwidth intra-node links (e.g., NVLink) to narrower inter-node interconnects, where available bandwidth drops by an order of magnitude [23]. The sparse activation pattern, meanwhile, provides limited computation to overlap with this communication. In architectures like DeepSeek-V3, where experts span multiple nodes, unoptimized all-to-all can consume up to 60% of total training time.

The Compute Efficiency Wall. MoE introduces computational inefficiencies absent in dense models:

- • 
Small GEMMs. Fine-grained experts produce many small matrix multiplications that underutilize GPU compute units [24]. In our measurements, GEMMs account for 70% of execution time in Llama-3 405B (dense) but under 50% in DeepSeek-V3 (MoE). The remainder is consumed by operations that scale with tensor count rather than FLOP count.
- • 
Routing and permutation overhead. Token routing and permutation, absent in dense models, add 9% to layer execution time even after optimization.
- • 
Load imbalance. Dynamic routing assigns uneven token counts to experts, leaving some overloaded while others sit idle, wasting compute capacity [22].
- • 
Host overhead. MoE launches more kernels for the same amount of FLOPs because of sparsity and routing, and each launch carries fixed host-side cost, these add up and leave the GPU idle between kernels. In dropless MoE, dynamic tensor shapes further require costly host-device synchronization.

---

[referencia=8ccdf64e8c44880b score=0.703]
### 4.2. Breaking the Communication Wall

Communication overhead directly reduces GPU utilization: every microsecond spent in collective operations represents lost compute capacity. Before optimization, EP all-to-all communication typically consumes 20–60% of training time, depending on model configuration, EP size, and hardware topology. When EP stays within the NVLink domain (e.g., DeepSeek-V3 with EP64 on GB200 NVL72), the overhead is around 20%; when EP crosses node boundaries (e.g., DeepSeek-V3 with EP64 on H100 across nodes), it rises to 40–60%. The techniques in this section target all points on this spectrum.

Expert Parallelism (EP) distributes experts across devices to scale MoE models beyond single-device capacity, but this distribution introduces a unique communication pattern. Unlike AllReduce, whose volume is independent of parallelism degree, all-to-all volume is proportional to token count and hidden dimension, and larger EP pushes this communication cross-node where bandwidth is limited. For fine-grained MoE architectures like DeepSeek-V3 and Kimi-K2, three factors compound this challenge:

- • 
High frequency: More experts mean more dispatch/combine operations per layer (DeepSeek-V3 has 58 MoE layers, each requiring two all-to-all operations).
- • 
Cross-node bottleneck: With large EP sizes spanning multiple nodes, inter-node all-to-all latency dominates due to lower bandwidth.
- • 
Low arithmetic intensity: Small experts complete computation quickly, leaving less time to overlap with communication.

---

[referencia=8ccdf64e8c44880b score=0.696]
## 11. Conclusion

This report presented Megatron-Core MoE, an open-source stack for training large-scale Mixture-of-Experts models. MoE sparsity introduces two fundamental challenges: a parameter-compute mismatch that manifests as the Three Walls (Memory, Communication, and Compute Efficiency), and a dense-sparse mismatch that requires decoupled parallelism for attention and MoE layers. By combining integrated solutions across these challenges, Megatron-Core MoE enables efficient trillion-parameter-scale training.

The key technical contributions include:

- • 
Multi-Dimensional Parallelism and Parallel Folding. Expert Parallelism integrates seamlessly with tensor, pipeline, context, and data parallelism. MoE Parallel Folding decouples attention and MoE layer configurations, breaking the restrictive constraint and enabling flexible parallelism mapping tailored to model architecture and hardware topology.
- • 
Memory Optimization. Fine-grained activation recomputation, memory-efficient permutation, precision-aware optimizers with BF16 moments, and CPU activation offloading reduce memory footprint from 199.5 GB to under 80 GB per GPU for DeepSeek-V3, making trillion-parameter training feasible on current hardware.
- • 
Communication Optimization. High-performance token dispatchers (DeepEP and HybridEP), and communication-computation overlap transform all-to-all from a bottleneck into a background operation hidden behind expert computation.
- • 
Compute Efficiency. Grouped GEMM kernels batch expert computations for better hardware utilization, kernel fusion consolidates routing and permutation operations, CUDA Graphs reduce launch overhead, and sync-free execution eliminates host-device synchronization for dropless MoE.
- • 
FP8 Training. Full FP8 support with selective precision, protecting numerically sensitive components (router, embeddings, optimizer states) while aggressively quantizing bulk computation, provides benefits across all three walls simultaneously.
- • 
Long-Context Training. Context Parallelism and Tensor Parallelism scaling maintain constant sub-sequence lengths per device, enabling training at 16K to 64K+ token sequences where attention computation dominates.
- • 
Production Features. Load balancing strategies and token dropping ensure stable training, distributed checkpointing enables parallelism-agnostic resharding, upcycling initializes MoE models from dense checkpoints, and multi-token prediction integration supports advanced training objectives.
- • 
Reinforcement Learning Support. Megatron Core and Megatron-Bridge provide seamless integration with popular RL frameworks, while packed sequence support, dynamic context parallelism, and router replay address the unique challenges of RL post-training workloads.

---

[referencia=8ccdf64e8c44880b score=0.694]
## 6. Long-Context MoE Training

The preceding sections addressed the three walls (memory, communication, and compute efficiency) under the assumption that MoE layers dominate computational cost. This assumption holds for typical training tasks with sequence lengths of 4K–8K tokens, where expert computation and all-to-all communication are the primary bottlenecks. However, the rise of reasoning models (OpenAI o1, DeepSeek-R1 [81], etc.) and RL-based training have created a new frontier: sequences of 16K, 64K, or even longer. At these lengths, a fundamental shift occurs in the performance characteristics of MoE training: attention dominates the computation, and the relative importance of the three walls changes accordingly. This section examines how long-context training reshapes the three walls for MoE models, and how Megatron-Core addresses the new challenges.

### 6.1. When Attention Dominates: The Computational Shift

In Section 4, we established that MoE training faces three fundamental walls: memory, communication, and compute efficiency. The optimizations presented there (activation management, dispatcher optimization, Grouped GEMM, and CUDA Graphs) target scenarios where MoE layers dominate the computational profile. Long-context training fundamentally alters this assumption. The key insight is the differing computational complexity between MoE and attention layers, as shown in figure 34:

- • 
MLP Components: Computational cost scales linearly with sequence length, exhibiting complexity.
- •

For example, at 64K tokens, SDPA consumes 69% of FLOPs, compared to only 10–15% in short-sequence scenarios. Attention becomes dominant in computation. Fortunately, SDPA is highly optimized in most GPU-accelerated libraries such as FlashAttention [84, 85, 86] and cuDNN (Table 9), so SDPA does not become a performance bottleneck. The optimization focus therefore shifts to memory and communication: as long as we address these two challenges without introducing excessive overhead, training performance is preserved.

| Platform | Sequence Length | Forward TFLOPS | Backward TFLOPS | 
| Hopper | 4096 | 553 | 422 | 
|  | 16384 | 638 | 523 | 
| Blackwell | 4096 | 1324 | 1083 | 
|  | 16384 | 1698 | 1298 |

---

[referencia=8ccdf64e8c44880b score=0.688]
### 8.1. Experimental Setup

Benchmark Models. We evaluate Megatron-Core MoE on two state-of-the-art fine-grained MoE architectures that stress-test the framework’s capabilities: DeepSeek-V3-685B [6] and Qwen3-235B [32, 87]. Both models feature the fine-grained expert design that amplifies the Three Walls challenges: high expert counts strain memory capacity, top-k routing increases all-to-all communication volume, and smaller per-expert computations reduce GEMM efficiency. These characteristics make them demanding benchmarks for validating our optimization strategies.

Hardware and Software Stack.
Benchmarks are conducted on NVIDIA GB200 and H100 GPUs to assess performance across hardware generations. We use the dev branch of Megatron-LM<sup>5</sup><sup>5</sup>
              5
              
              
              
            https://github.com/NVIDIA/Megatron-LM/tree/dev with the latest TransformerEngine<sup>6</sup><sup>6</sup>
              6
              
              
              
            https://github.com/NVIDIA/TransformerEngine/tree/main. The full optimization stack described in Section 4 is enabled, including but not limited to:

- • 
FP8 training: MXFP8 on GB200/GB300 (Blackwell) with native Tensor Core support and blockwise FP8 on H100 (Hopper)
- • 
Memory optimizations: Selective recomputation and activation & optimizer state offloading to reduce peak memory footprint
- • 
Optimized token dispatchers: HybridEP <sup>7</sup><sup>7</sup> 7
                    
                    
                    
                  https://github.com/deepseek-ai/DeepEP/tree/hybrid-ep on GB200/GB300 NVL systems exploiting Multi-Node NVLink, and DeepEP<sup>8</sup><sup>8</sup> 8
                    
                    
                    
                  https://github.com/deepseek-ai/DeepEP/tree/main on H100 systems
- • 
Communication overlap: 1F1B all-to-all overlap with expert computation
- • 
Kernel optimizations: Grouped GEMM, router fusion, permutation fusion, and CUDA Graphs

Metrics. We report per-GPU throughput in TFLOPS and tokens processed per second per GPU. These metrics provide two views of computational efficiency and practical training throughput.

---

[referencia=8ccdf64e8c44880b score=0.674]
#### 4.1.1. Memory Anatomy: Sources of Memory Consumption

MoE models typically consume substantially more memory than equivalent dense models, owing to several distinct sources of overhead. Consider DeepSeek-V3 trained with BF16 precision using a configuration across 256 GPUs. Table 3 presents the per-GPU memory breakdown, revealing a total requirement of 199.5 GB, well beyond the 80 GB capacity of an H100 GPU without optimization.

| Component | Memory per GPU | Optimization Techniques | 
| Weights & Gradients | 36.4 GB | PP, EP, or TP sharding | 
| Main Weights & Optimizer States | 32.1 GB | Distributed optimizer, BF16 moments | 
| Activations | 131.0 GB | Low Precision, Recomputation, Offloading | 
| Total | 199.5 GB |  | 

Three components contribute to this footprint:

Weights and Gradients (36.4 GB). All expert parameters must stay in memory even though only activate per token. DeepSeek-V3’s 256 experts with top-8 routing illustrate this: 685B parameters but only 37B activated per token, an 18 gap.

Optimizer States (32.1 GB). Adam stores momentum and variance per parameter, tripling parameter memory in FP32. Mixed-precision training with BF16 moments reduces this overhead but does not eliminate it.

Activations (131.0 GB). The largest memory consumer, exceeding weights and optimizer states combined. MoE activations scale with layer depth, hidden dimension, and top-, as well as batch size and sequence length. This makes activations the primary optimization target.

Additional MoE-specific factors add to memory pressure: dynamic routing can create load imbalance where certain experts temporarily receive too many tokens, and tokens must often be padded to fit efficient computation kernels, consuming memory beyond the actual data. These are activation memory costs that can be reduced through the recomputation techniques discussed below. Load imbalance is further addressed by ECHO (Section 4.3.7), which dynamically clones popular experts to balance token distribution across ranks.

Model architecture cannot be changed to reduce memory, so optimization must target how data is stored and managed. Four complementary strategies address memory constraints:

1. 1.

---

[referencia=8ccdf64e8c44880b score=0.598]
### 4.4. Summary: Breaking the Three Walls

This section addressed the three fundamental barriers to efficient MoE training, each a hard constraint that, unaddressed, prevents practical training at scale.

- • 
Memory Wall: Memory is the first constraint. If parameters, optimizer states, and activations exceed the GPU capacity, training cannot proceed. Memory-Efficient Permutation, FP8/FP4 activations, fine-grained recomputation, offloading, precision-aware optimizers, and FSDP together transform the 199.5 GB per-GPU requirement of DeepSeek-V3 into a feasible training configuration.
- • 
Communication Wall: Communication overhead directly reduces GPU utilization. Optimized dispatchers (DeepEP, HybridEP) maximize bandwidth and FWD-BWD overlap hides latency behind computation. Together, these reduce all-to-all overhead from up to 60% of the training time to less than 10% in DeepSeek-V3 training.
- • 
Compute Efficiency Wall: Compute inefficiency stems from two sources: small kernels that underutilize GPU resources, and host overhead that leaves GPUs idle. Grouped GEMM and kernel fusion improve kernel efficiency; CUDA Graphs and Sync-Free MoE eliminate host overhead. These transform computation inefficiency from the dominant bottleneck into a manageable constraint.

These optimizations are not independent. They form a coherent system where solutions to one wall enable or enhance solutions to others. Reduced-precision training shows this clearly: it reduces memory (activations) and improves compute efficiency (faster Tensor Core operations), while requiring careful integration to avoid introducing new bottlenecks (quantization kernel overhead).

---

[referencia=8ccdf64e8c44880b score=0.588]
#### 4.2.1. Communication Anatomy: The Expert Parallel Pattern

Figure 13 illustrates the expert parallelism communication pattern. In standard EP implementations, each MoE layer requires two collective communication operations: dispatch sends tokens to their assigned experts, and combine returns processed tokens to their original ranks. For a model with MoE layers, tokens per batch, hidden dimension , and EP degree EP, each forward pass involves dispatch/combine operations, each transferring data across EP ranks.

At DeepSeek-V3 scale, this translates to 58 MoE layers 2 operations/layer = 116 dispatch/combine operations per forward pass. The backward pass doubles this count. At 50 GB/s inter-node bandwidth (e.g., InfiniBand NDR), a single dispatch with 200 MB payload takes several milliseconds, accumulating to hundreds or thousands of milliseconds per iteration.

Communication volume is determined by the EP configuration and cannot be reduced without changing the parallelism strategy. Optimization must therefore target how communication is executed and scheduled. Two strategies work together to address communication overhead:

1. 1. 
Maximize bandwidth utilization. Standard NCCL all-to-all implementations do not fully exploit available bandwidth, particularly for fine-grained MoE workloads. Optimized dispatchers (DeepEP, HybridEP) use specialized kernels that fuse operations and exploit hardware primitives to approach peak bandwidth.
2. 2. 
Hide latency behind computation. Even with optimal bandwidth, all-to-all operations take time. By overlapping communication with computation from adjacent microbatches, this latency can be hidden rather than exposed on the critical path.

The following subsections present techniques organized by these strategies: bandwidth optimization (DeepEP, HybridEP), and latency hiding (EP communication overlapping, pipeline integration).

---

[referencia=8ccdf64e8c44880b score=0.576]
### 7.2. Shared Experts

Some MoE architectures (DeepSeek-V2/V3 [17, 6], Qwen [32]) include a shared expert that processes all tokens regardless of routing, providing consistent baseline capacity across all tokens (figure 40). When overlap is enabled (--moe-shared-expert-overlap), shared expert computation runs in parallel with the all-to-all communication and routed expert computation, hiding its latency behind the dispatch-compute-combine pipeline.

*all*tokens while routed experts process only their assigned tokens. When overlap is enabled, shared expert computation runs in parallel with the token dispatch/combine communication, hiding its latency.

### 7.3. Latent MoE

In standard MoE, all2all communication dispatches tokens at the full hidden dimension , and each expert is parameterized by weight matrices in and . LatentMoE [19] reduces both costs by inserting a shared down-projection before dispatch and an up-projection after combine, where is the latent dimension. Routing still operates on the full hidden dimension to preserve routing quality; each routed expert operates entirely in the compressed latent space; shared experts remain at dimension . The layer output becomes:

The compression ratio reduces all2all communication volume by a factor of (tokens are dispatched at dimension instead of ) and per-expert weight size by the same factor (expert matrices shrink from to ). Elango et al. [19] define two ways to exploit these savings. In , the total expert count is scaled by while top- is unchanged, preserving baseline accuracy at reduced inference cost. In (recommended), both and top- are scaled by , which restores inference cost to the standard-MoE level but exponentially expands the combinatorial space of expert selections (), yielding higher accuracy at iso-cost. At scales up to 95B parameters, consistently outperforms standard MoE in accuracy per FLOP and per parameter. The architecture has been adopted by NVIDIA’s Nemotron-3 Super and Ultra models.

Implementation. LatentMoE is enabled via --moe-latent-size, which sets . The MoELayer instantiates two TELinear projections: fc1_latent_proj (down-projection in the preprocess step, after routing but before dispatch) and fc2_latent_proj (up-projection in the postprocess step, after combine). Expert backends (TEGroupedMLP, SequentialMLP) automatically adapt their input and output dimensions to .

---

[referencia=8ccdf64e8c44880b score=0.551]
## 7. Production Features

The previous sections focused on performance optimizations that address the Three Walls. However, production MoE training also requires robustness, flexibility, and ease of use. This section describes features that address these operational requirements: load balancing to ensure stable training, shared and latent expert architectures, distributed checkpointing for flexible deployment, upcycling to use existing dense models, and integration with advanced training paradigms like multi-token prediction.

### 7.1. Load Balancing and Token Dropping

Dynamic routing in MoE models can lead to significant workload imbalance, where certain experts receive disproportionately more tokens than others. This causes computational inefficiency, memory bottlenecks, and degraded hardware utilization. We address these challenges with two coordinated mechanisms: load balancing and token dropping.

Load Balancing. Figure 39 illustrates the load balancing strategies available in Megatron-Core MoE. We provide multiple strategies to encourage uniform token distribution. The primary approach employs an auxiliary loss [12, 4], a differentiable penalty term that discourages routing all tokens to a small subset of experts. We also support expert choice routing [93], which formulates balanced routing as an optimal transport problem, and auxiliary-loss-free balancing via learnable expert bias terms [22] that dynamically adjust routing decisions based on historical load.

Token Dropping. We support two dispatch strategies with different capacity management policies. In dropless mode (the default), all routed tokens are processed without capacity constraints, maximizing model expressiveness at the cost of variable per-expert workload. In droppable mode, explicit expert capacity limits are enforced [12, 4]: when tokens assigned to an expert exceed its capacity, excess tokens are dropped and bypassed through residual connections. This provides predictable memory bounds, useful during early training when the router is poorly initialized.

Pad-to-Max for Static Shapes. Droppable mode also enables pad-to-max functionality, which pads all expert inputs to the same capacity limit. This converts MoE’s inherently dynamic per-expert token counts into static shapes, enabling optimizations like CUDA Graphs (Section 4.3.6) that require fixed tensor dimensions across iterations.

---

[referencia=8ccdf64e8c44880b score=0.544]
- • 
Section 2: Megatron-Core MoE Architecture. Introduces Megatron-Core MoE’s design in two parts: the internal design of the MoE layer itself (router, token dispatcher, experts) and the four-stage forward pass (route, dispatch, compute, combine), followed by the external design covering integration with the transformer model, parallel process group organization, and optimizer handling for expert parameters.
- • 
Section 3: Scaling MoE with Parallel Folding and Multi-Dimensional Parallelism. Examines how MoE’s sparsity breaks the parallelism assumptions of dense training, why Expert Parallelism (EP) is needed alongside traditional strategies, and how the resulting dense-sparse mismatch between attention and MoE layers is resolved by MoE Parallel Folding, which decouples their parallelism configurations for flexible, efficient mapping at trillion-parameter scale.
- • 
Section 4: Breaking the Memory, Communication, and Compute Efficiency Walls. Presents Megatron-Core MoE’s solutions to the three fundamental barriers: the Memory Wall (activation management, recomputation strategies, offloading, distributed parameter storage), the Communication Wall (optimized dispatchers including DeepEP and HybridEP, communication-computation overlap), and the Compute Efficiency Wall (Grouped GEMM, kernel fusion, CUDA Graphs, sync-free execution for dropless MoE).
- • 
Section 5: Reduced-Precision Training in FP8/FP4 for MoE. Covers reduced-precision training as a cross-cutting optimization that simultaneously impacts all three walls by reducing activation memory, halving communication volume, and accelerating Tensor Core GEMMs, while presenting strategies for selective precision to maintain training stability.
- • 
Section 6: Long-Context MoE Training. Examines how long-context scenarios (16K to 64K+ tokens) fundamentally shift the optimization landscape as attention computation dominates, and presents techniques for managing activation memory growth through Context Parallelism and Tensor Parallelism scaling.
- • 
Section 7: Production Features. Describes operational features for production training: load balancing and token dropping for stable training, distributed checkpointing for parallelism-agnostic resharding, upcycling from dense checkpoints, and integration with multi-token prediction.
- • 
Section 8: Performance Evaluation. Validates the framework’s effectiveness through empirical benchmarks on DeepSeek-V3 and Qwen3-235B across GB200 and H100 platforms, demonstrating the impact of the full optimization stack.

---

[referencia=8ccdf64e8c44880b score=0.521]
#### 4.3.1. Compute Anatomy: Sources of Inefficiency

Compute inefficiency in MoE training stems from two distinct sources:

Kernel Efficiency. Fine-grained MoE architectures produce workloads that underutilize GPU resources. DeepSeek-V3’s 256 small experts yield GEMMs with M dimensions of 128 tokens per expert, far from the thousands needed for peak Tensor Core utilization. Beyond expert computation, MoE introduces complex routing and dispatching operations composed of many small kernels that individually cannot saturate GPU compute capacity.

Host Overhead. Numerous small operations create kernel launch overhead, and the CPU cannot dispatch work fast enough to keep the GPU saturated. Three factors make this worse:

- • 
Fine-grained experts: Many individual GEMMs rather than few large ones, each requiring a separate kernel launch.
- • 
Reduced-precision training: Additional quantization kernels add to the launch overhead.
- • 
Dropless routing: Dynamic token counts require host-device synchronization to determine tensor shapes, placing the CPU on the critical path.

The result is host-boundedness: GPU kernels separated by microseconds of host-side latency, visible as gaps in profiling traces where compute resources sit idle.

Kernel shapes are determined by model architecture and cannot be changed without modifying the model. Optimization must therefore target how computation is organized and scheduled. Five strategies work together to address compute inefficiency:

1. 1. 
Fuse related operations. Kernel fusion consolidates routing, permutation, and auxiliary loss computations into fewer, larger kernels.
2. 2. 
Accelerate with low precisions. Reduced-precision training in FP8/FP4 uses faster Tensor Core operations, increasing throughput for the same kernel shapes.
3. 3. 
Eliminate per-iteration CPU logic. CUDA Graphs capture kernel sequences and replay them with minimal host involvement.
4. 4. 
Remove host-device synchronization. Sync-free execution enables GPU kernels to proceed without waiting for shape information from the host.
5. 5. 
Balance expert load. ECHO dynamically clones hot experts to underutilized ranks, reducing load imbalance that causes some ranks to wait while others compute.

---

[referencia=8ccdf64e8c44880b score=0.516]
These three walls are tightly coupled: optimizing one often shifts pressure to another. Increasing batch size improves GEMM utilization but amplifies memory pressure and communication volume. CUDA Graphs eliminate host overhead but require static tensor shapes, conflicting with dropless routing. Grouping tokens across experts improves compute efficiency but complicates load balancing. Section 3 provides the detailed parallelism analysis underlying EP and Parallel Folding; Section 4 presents Megatron-Core’s integrated approach to addressing all three walls while managing their interactions.

### 1.3. Megatron-Core MoE

Built within Megatron-Core, a PyTorch-based library for large-scale transformer training [8, 25], this MoE training stack tackles all three walls simultaneously:

Multi-Dimensional Parallelism. Expert Parallelism (EP) integrates with tensor, pipeline, sequence, and data parallelism. MoE Parallel Folding [26] decouples attention and MoE layer configurations, breaking the traditional constraint and enabling configurations tailored to specific model architectures and hardware topologies.

Memory Optimizations. Fine-grained activation recomputation, memory-efficient permutation, precision-aware optimizers, and activation offloading reduce memory footprint without sacrificing throughput [27, 28]. Comprehensive reduced-precision training (FP8 and FP4) support in expert GEMMs, activations, and communication further reduces activation storage while maintaining convergence through selective precision strategies.

Communication Optimizations. High-performance token dispatchers (DeepEP, HybridEP) maximize bandwidth utilization. Communication-computation overlap hides all-to-all latency behind expert computation.

Compute Optimizations. Grouped GEMM kernels, kernel fusion, CUDA Graphs, and sync-free execution address the computational fragmentation inherent in fine-grained MoE architectures.

Production Features. Load balancing strategies, token dropping with capacity control, distributed optimizer and FSDP support, distributed checkpointing with flexible resharding, and upcycling from dense checkpoints enable deployment at scale. The MoE stack’s modular design enables rapid experimentation, while its production-grade optimizations support training from research prototypes to trillion-parameter models [29]. This report explains what the stack provides, why key design decisions were made, and how they address MoE training challenges, with practical guidance for configuration and tuning.

---

[referencia=8ccdf64e8c44880b score=0.466]
### B.2. Key Optimizations

This section summarizes the configuration of the most performance-critical optimization features used in our benchmark runs. Although the full optimization space is larger, these features consistently have first-order impact on throughput and are configured differently across workloads and platforms.

DeepSeek-V3

- • 
Dispatcher: HybridEP on GB300/GB200; DeepEP on H100.
- • 
Recompute: None on GB300; mlp on GB200; up_proj, mlp on H100.
- • 
1F1B overlap: ON for GB300 and H100; OFF for GB200.
- • 
CUDA Graphs: attn, moe_router, moe_preprocess on GB300/GB200; OFF on H100.

These settings are chosen to balance memory headroom, communication overhead, and kernel efficiency for maximum sustained throughput on each platform.

Qwen3-235B

- • 
Dispatcher: HybridEP on GB300/GB200; DeepEP on H100.
- • 
Recompute: moe_act, layernorm on GB200 and H100.
- • 
1F1B overlap: OFF for GB300; ON for GB200 and H100.
- • 
CUDA Graphs: attn, moe_router, moe_preprocess.

The resulting configuration pattern reflects a throughput-first tuning strategy under model- and hardware-specific constraints.

### B.3. Reproducibility

The benchmark numbers in Table 11 can be reproduced through two supported workflows. First, users can run end-to-end training with Megatron-Bridge <sup>11</sup><sup>11</sup>
              11
              
              
              
            https://github.com/NVIDIA-NeMo/Megatron-Bridge/tree/main/scripts/performance, which provides a higher-level interface for model, parallelism, and optimization configuration. Second, users can launch training directly with Megatron-Core (MCore) using model-specific scripts in Megatron-MoE-ModelZoo <sup>12</sup><sup>12</sup>
              12
              
              
              
            https://github.com/yanring/Megatron-MoE-ModelZoo/tree/main/best_practice/readme.md, which exposes the full set of low-level launch flags for performance tuning. In both workflows, start from Table 20 and adjust only a few cluster-specific runtime settings (for example, hostfile, environment modules, and job scheduler options).

---

[referencia=8ccdf64e8c44880b score=0.457]
#### 4.1.8. Summary

Table 6 summarizes the memory optimization techniques described in this section and their primary targets.

| Technique | Memory Target | Trade-off | 
| Reduced-Precision Training | Activations | Numerical Precision and CPU Overhead | 
| Memory-Efficient Permutation | Activations | - | 
| Fine-grained Recomputation | Activations | Compute Overhead | 
| Fine-grained Offloading | Activations | CPU Overhead and Non-Overlapped Copy | 
| Precision-aware Optimizer | Optimizer States | Numerical Precision | 
| FSDP (with EP) | Params + Optimizer | Communication Overhead | 

These memory optimizations complement each other: Memory-Efficient Permutation eliminates redundant storage with zero overhead; FP8/FP4 activations reduce precision with minimal quality impact; fine-grained recomputation offers favorable compute-memory trade-offs for specific modules; activation offloading provides additional headroom when other techniques are insufficient; low-precision storage and state offloading reduce weight and optimizer memory; and FSDP enables scaling beyond single-device capacity. Together, they reduce memory from a blocking barrier to a manageable constraint.

Memory optimization is not a one-time gate that, once passed, can be forgotten. For large-scale MoE models, memory is a persistently scarce resource throughout the entire optimization lifecycle. Beyond enabling training to proceed at all, memory headroom unlocks other optimizations: larger batch sizes provide more computation to hide communication latency (Section 4.2.3), CUDA Graphs require additional static buffers (Section 4.3.6), and EP communication overlap must hold activations from multiple microbatches simultaneously. Many optimizations described in the following sections consume memory, and the techniques above are what make that consumption feasible.

---

[referencia=8ccdf64e8c44880b score=0.453]
### 6.5. Summary

Long-context MoE training represents a distinct optimization regime where the fundamental assumptions of Section 4 must be revisited. While the Three Walls (memory, communication, and compute efficiency) remain the fundamental barriers, their relative importance shifts substantially as sequence length increases:

- • 
Computational Shift: Attention’s complexity displaces MoE layers as the dominant computational bottleneck, consuming 69% of FLOPs at 64K tokens. The MoE-focused optimizations of Section 4.3 remain valuable but no longer address the primary bottleneck.
- •
- • 
Communication Trade-offs: The choice between CP and TP involves nuanced trade-offs between communication overhead, memory savings, and SDPA computational efficiency, a balance distinct from the MoE-centric all-to-all optimization focus of Section 4.2.

By combining context parallelism, tensor parallelism, selective recomputation, and optimizer offloading, Megatron-Core enables efficient training across diverse sequence lengths. Our experiments on 256 Hopper GPUs at 256K sequence length demonstrate this: DeepSeek-V3 achieves 88% of its short-context MFU using TP, optimizer CPU offloading, and selective recomputation, while Qwen3-235B-A22B reaches 129% of its short-context MFU with TP, CP, and selective recomputation (the latter exceeding 100% because SDPA kernels are highly efficient when dominating the computation at longer sequences). The packed sequence and Dynamic-CP features further extend these capabilities to variable-length workloads in RL and SFT training.

---

[referencia=8ccdf64e8c44880b score=0.399]
### 3.2. The Challenge of MoE Parallelism

Traditional parallelism strategies were designed for dense Transformers. MoE models have fundamentally different computation patterns that require a new parallelism dimension, Expert Parallelism (EP), and create unique challenges when combining EP with existing strategies.

#### 3.2.1. The Parallelism Paradox of MoE

Figure 3 illustrates this paradox by plotting total parameters against *forward* FLOPs per token for major LLMs. Dense models (circles) follow the 2N reference line, exhibiting a *virtuous cycle* as they scale: increasing parameters requires more GPUs for memory, but more parameters also means more computation per token. Because computation grows with model size, communication takes a smaller share of each step, keeping MFU stable.

MoE models (triangles) break this cycle. They fall significantly below the 2N line, achieving equivalent capability with far fewer FLOPs per token. Consider the fundamental asymmetry:

| Model | Total Params | Active Params | Ratio | 
| Llama-70B (Dense) | 70B | 70B | 1:1 | 
| DeepSeek-V3 (MoE) | 685B | 37B | 18:1 | 

Note: DeepSeek-V3 comprises 671B Main Model weights and 14B Multi-Token Prediction (MTP) Module weights (685B total). The table shows the total model parameters including MTP.

DeepSeek-V3 has 18 more parameters than its active computation suggests, visible in Figure 3 as the gap between DeepSeek-V3’s position and where a dense model of equivalent parameters would lie. This creates a *compounding effect*:

1. 1. 
Memory grows fast, forcing distribution across many GPUs: All experts’ parameters, gradients, and optimizer states must reside in memory, and larger top- further increases activation memory through token replication.
2. 2. 
More communication: Distributing experts via EP introduces all-to-all traffic whose volume scales with (each token is dispatched to experts across EP ranks).
3. 3. 
But compute stays low: Per-token FLOPs scale only with (), not (), leaving insufficient computation to overlap with the growing communication.

The consequence: MoE training is fundamentally communication-bound unless parallelism is designed specifically for this asymmetry. This is not a matter of degree; it is a *qualitative difference* from dense models.

---

[referencia=8ccdf64e8c44880b score=0.394]
#### 3.1.2. The Trade-off of Parallelism

Parallelism is not free. Every parallelism strategy introduces overhead:

- • 
Communication overhead: Data exchange between GPUs consumes time and bandwidth.
- • 
Synchronization: Fast GPUs must wait for slow GPUs at synchronization points.
- • 
Pipeline bubbles: Pipeline parallelism introduces idle time at pipeline boundaries.
- • 
Reduced compute intensity: Sharding reduces per-GPU matrix sizes, lowering GEMM efficiency.

The result: Model FLOP Utilization (MFU) is heavily influenced by parallelism strategy, and effective parallelism design can minimize the gap between ideal and actual MFU.

Key insight for dense models: The “cost” and “benefit” of parallelism scale proportionally. More parameters require more GPUs, but more parameters also mean more computation per forward-backward pass. Because computation grows with model size, communication takes a smaller share of each step, keeping MFU relatively stable as models scale.

MoE’s sparsity disrupts this balance. Because only of experts activate per token, total parameters scale with while per-token compute scales only with . More GPUs are needed for memory, but per-token computation does not grow to match, leaving communication overhead exposed. The following section examines how this asymmetry breaks the assumptions underlying traditional parallelism strategies and why a new parallelism dimension is needed.

---

[referencia=8ccdf64e8c44880b score=0.388]
To scale overlap to large models, merged FWD-BWD can be combined with Interleaved Pipeline Parallelism (Interleaved PP), which partitions the model into virtual pipeline stages (VPP) and expands overlap opportunities across pipeline ranks. Figure 19 shows an interleaved 1F1B schedule with three phases: warmup, 1F1B, and flush. Adjacent FWD-BWD pairs in the 1F1B phase can apply the EP overlap pattern above. However, adjacent pairs may still have data dependencies when they belong to the same micro-batch. To avoid this, we run one extra micro-batch at the end of warmup before entering 1F1B, ensuring adjacent FWD/BWD pairs are dependency-free and enabling full all-to-all overlap across virtual stages.

A latency comparison between merged FWD-BWD (1F1B) and DualPipeV (a refined DualPipe variant) shows:

- • 
1F1B is faster with large VPP sizes (more virtual stages enable more overlapping opportunities).
- • 
The latency gap shrinks at large PP sizes and micro-batch counts (both strategies reach near-optimal overlap).
- • 
For hybrid models (e.g., DeepSeek-V3 with mixed dense/MoE layers), workload balance across PP stages is critical. Megatron-Core’s Flexible Asymmetric VPP supports custom per-stage layer placement to maximize overlap.

Several factors limit the achievable speedup from all-to-all overlap:

- • 
Proportion of overlapped batches: More micro-batches increase the proportion of overlapped batches.
- • 
all-to-all Proportion: EP overlap gains are larger when all-to-all dominates, especially for cross-node EP and fine-grained MoE models with low compute-to-communication ratios.
- • 
SM Carve-out Overhead: Reserving SMs for all-to-all can reduce GEMM efficiency. In our DeepSeek-V3 benchmark, DeepEP uses 20 SMs per GPU and introduces roughly 20% GEMM-efficiency overhead.

On fine-grained MoE models such as DeepSeek-V3, combining all-to-all overlap with optimized dispatchers (Section 4.2.2) achieves a 93% overlap ratio for expert communication latency, reducing expert communication share from 30–40% of iteration time to under 5%.

---

[referencia=8ccdf64e8c44880b score=0.386]
# Scalable Training of Mixture-of-Experts Models with Megatron Core

Technical Report

###### Abstract

Scaling Mixture-of-Experts (MoE) training introduces systems challenges absent in dense models. Because each token activates only a subset of experts, this sparsity allows total parameters to grow much faster than per-token computation, creating coupled constraints across memory, communication, and computation. Optimizing one dimension often shifts pressure to another, demanding co-design across the full system stack.

We address these challenges for MoE training through integrated optimizations spanning memory (fine-grained recomputation, offloading, etc.), communication (optimized dispatchers, overlapping, etc.), and computation (Grouped GEMM, fusions, CUDA Graphs, etc.). The framework also provides Parallel Folding for flexible multi-dimensional parallelism, low-precision training support for FP8 and NVFP4, and efficient long-context training. On NVIDIA GB300 and GB200, it achieves 1,233/1,048 TFLOPS/GPU for DeepSeek-V3-685B and 974/919 TFLOPS/GPU for Qwen3-235B. As a performant, scalable, and production-ready open-source solution, it has been used across academia and industry for training MoE models ranging from billions to trillions of parameters on clusters scaling up to thousands of GPUs.

This report explains how these techniques work, their trade-offs, and their interactions at the systems level, providing practical guidance for scaling MoE models with Megatron Core.

<sup>†</sup>

<sup>†</sup>footnotetext: © 2026 NVIDIA. All rights reserved.

###### Contents