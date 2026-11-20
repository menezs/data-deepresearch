[referencia=363fb5dd108968a4 score=0.939]
## 4. DeepSeek-V2: MLA Changes Everything

May 2024: 236B parameters, 21B active, and a KV cache compressed into a single latent vector per token.

DeepSeek-V2 (arXiv:2405.04434, released May 2024) is one of the most consequential architecture papers of the decade, and its abstract compresses the entire business case into three numbers: **saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76×** — all comparisons against the lab's own DeepSeek 67B. The model itself is a 236B-parameter MoE with 21B activated per token, 60 transformer layers, native 128K context (via the MLLA architecture plus YaRN-style extension from a shorter pretraining window), and 8.1T pretraining tokens. But the number everyone remembers is the cache.

### The idea in one paragraph

MQA shares one K/V head across all query heads (tiny cache, degraded quality). GQA splits the difference (smaller cache, small quality cost). MLA refuses the trade: instead of *sharing heads*, it **caches a compressed latent representation and reconstructs per-head keys and values from it on demand**. Per token, per layer, the cache holds exactly two things: a 512-dimensional compressed latent c<sub>KV</sub> shared by all heads, and a single 64-dimensional RoPE-encoded key k<sub>rope</sub> (the decoupled positional key, Chapter 5). That is 576 cached elements versus 32,768 for the counterfactual MHA — 1.76% of the bytes, with the V2 paper's own ablation table showing MLA *outperforming* MHA on hard benchmarks, not merely matching it.

**MHA @ V2 scale**

128 heads × 128 dims × 2 (K,V)

32,768 elems · 65,536 B

**GQA-8 @ V2 scale**

8 KV heads × 128 dims × 2

2,048 elems · 4,096 B

**MLA (V2)**

latent 512 + rope key 64

576 elems · 1,152 B (bf16)

---

[referencia=363fb5dd108968a4 score=0.890]
### 16.1 — The mechanisms, compared

| Mechanism | Core idea | Typical cache effect | Used by | 
|---|---|---|---|
| MHA | Every head caches its own K/V | baseline (4 MB/token @ V3 scale) | Pre-2023 models; DeepSeek LLM 7B | 
| GQA | Groups share KV heads | ÷ 8 (500 KB) | Llama 3, Qwen3, gpt-oss; DeepSeek LLM 67B | 
| MQA | One KV head for all | ÷ 128, quality cost | PaLM era; the indexer inside DSA borrows its shape | 
| SWA | Fixed local window, old context discarded | O(window) | Gemma 3; the local branch in CSA/HCA | 
| **MLA** | Cache a shared low-rank latent; reconstruct on demand | ÷ 57 vs. MHA (70 KB) | **DeepSeek V2–V3.2** ; Kimi K2; MLX-portable via absorption | 
| **DSA** | Lightning indexer selects top-2,048; attention reads only those | read ÷ ~5 @131K; stored unchanged | **DeepSeek V3.2** ; GLM 5/5.1 (indexer shared across layers) | 
| **CSA + HCA** | Pool 4× (sparse) and 128× (dense) entries, interleaved | ÷ ~10 end-to-end vs. V3.2 | **DeepSeek V4** | 
| **CSA2** | Entry × sequence × *layer* compression; MXFP4; CED projection | **890 B/token global** | **DeepSeek-V4.1-Flash** | 

Three patterns in the table are worth naming. The industry's default (GQA) plateaued at ~8× while DeepSeek compounded 57× more on top of it; the labs that followed DeepSeek adopted its mechanisms rather than inventing parallel ones (Kimi K2 took MLA, Z.ai took DSA whole — including the layer-shared indexer refinement); and every DeepSeek mechanism degrades gracefully into a standard component (MLA decodes as SDPA, DSA adds a gather, CSA pools existing entries), which is precisely why the ecosystem could absorb each generation in days rather than quarters.

---

[referencia=363fb5dd108968a4 score=0.875]
### 5.5 — The configuration, for the record

| Parameter | Value (V2 / V3) | Role | 
|---|---|---|
| num_attention_heads | 128 | Query heads per layer | 
| kv_lora_rank (d <sub>c</sub> ) | 512 | The joint K/V latent — the cached content | 
| q_lora_rank | 1536 | Query latent (not cached) | 
| qk_nope_head_dim | 128 | Per-head content dims (from latent) | 
| qk_rope_head_dim | 64 | Per-head positional dims (decoupled RoPE) | 
| v_head_dim | 128 | Per-head value dims (from latent) | 
| n_layers | 60 / 61 | V2 / V3 transformer layers | 
| **Cached elements per token per layer** | **512 + 64 = 576** | **1,152 bytes bf16 · 576 bytes fp8** | 

Two properties of this design earned it the industry's respect. First, **quality parity**: the V2 ablations show MLA outscoring MHA (and GQA, and MQA) at matched training budgets — low-rank projection turned out to be a mild regularizer of attention rather than a bottleneck, which is why no DeepSeek model since has felt the need to widen the latent. Second, **portability**: because absorbed decode is plain SDPA, MLA runs anywhere a matmul runs — MLX on Apple Silicon, consumer runtimes, research code — with the full compression and no custom kernel. The custom kernels (FlashMLA, Chapter 8) exist to go *faster* than SDPA, not to make the mechanism possible.

MLA caches a 576-element thought per token per layer instead of 32,768 numbers, reconstructs whatever the current phase needs from it, and arranges the algebra so decode never reconstructs anything — 57× less traffic, no measured quality loss, and a fixed 576-element target that every later precision trick (fp8 in V3.2, MXFP4 in V4.1) could attack with arithmetic instead of architecture.

---

[referencia=363fb5dd108968a4 score=0.721]
| Term | Definition | 
|---|---|
| **KV cache** | Stored keys and values (or their compressed proxies) for every past token, so attention need not recompute them each step. Grows linearly with tokens; read every decode step. | 
| **MLA** | Multi-head Latent Attention. Caches a 512-d joint K/V latent plus a 64-d shared RoPE key per token per layer; reconstructs or absorbs (q-side) the rest. | 
| **Absorption** | Folding up-projections into precomputed query-side matrices so decode attends against the latent directly, MQA-style. | 
| **Decoupled RoPE** | Splitting keys into unrotated content (NoPE, from the latent) and rotated positional (RoPE, cached separately) parts so absorption stays legal. | 
| **DSA** | DeepSeek Sparse Attention: lightning indexer + top-k token selection over the full cache. | 
| **Lightning indexer** | 64 MQA heads sharing one 128-d key per token; ReLU-weighted scoring; 132 B/token/layer fp8. | 
| **CSA / HCA** | V4's paired mechanisms: 4× pooled entries with sparse top-k selection; 128× pooled entries with dense attention. | 
| **CSA2** | V4.1's mechanism: entry-size, sequence, and *cross-layer* compression with Full/Reindex/Reuse modes and a hierarchical indexer. | 
| **CED** | Causal Encoder-Decoder: 20 encoder layers (8B active) produce global KV projected into 20 decoder layers (16B active); halves prefill compute for input-heavy workloads. | 
| **MXFP4** | OCP-standard 4-bit floating format with per-block scales; applied to the main KV cache via quantization-aware training in V4.1. | 
| **SWA Bounded Replay** | Reconstructing missing sliding-window KV by replaying the most recent n <sub>win</sub> tokens instead of persisting it. | 
| **Engram** | V4.1's 196B conditional memory module: multi-head hashing + context-aware gating; knowledge in weights, not cache. | 
| **Context caching (API)** | Disk-backed prefix KV reuse with hit/miss billing; automatic since August 2024. |

---

[referencia=363fb5dd108968a4 score=0.699]
## 2. The Arithmetic of Cache Memory

One formula, three precisions, and the three axes on which every DeepSeek innovation operates.

Before the history, the mathematics — because every claim in this paper reduces to it. The KV cache size for a standard multi-head or grouped-query attention transformer is:

```
bytes_per_token = 2                            # K and V, both cached
                * n_kv_heads                  # key/value heads (shared in GQA/MQA)
                * head_dim                    # dimension of each head
                * n_layers                    # every transformer layer caches its own
                * bytes_per_element           # 2 for bf16, 1 for fp8, 0.5 for fp4
```
The factor of 2 is the K/V pair; the per-layer multiplication is the silent killer — a 61-layer model stores 61 independent copies of every token's past. Work it for three familiar configurations in bf16 and the scale of the problem appears immediately:

| Configuration | KV heads | Head dim | Layers | Per layer | Per token (bf16) | At 32K ctx, batch 1 | 
|---|---|---|---|---|---|---|
| Llama-3.3-70B (GQA-8) | 8 | 128 | 80 | 4,096 B | 320 KB | 10.5 GB | 
| Hypothetical MHA @ V2 scale | 128 | 128 | 60 | 65,536 B | 3.84 MB | 126 GB | 
| Hypothetical GQA-8 @ V2 scale | 8 | 128 | 60 | 4,096 B | 240 KB | 7.9 GB | 

Two observations fall out of this table. First, MHA is not a serious option at frontier scale: 3.84 MB per token means a single 32K-context request would need 126 GB of cache before the weights arrive. Second, GQA's 8× head sharing only buys you to ~240 KB per token — still 7.9 GB for one long-context request. The gap between "GQA is fine" and "GQA is fine at 1M tokens" is where the entire DeepSeek program lives: 240 KB × 1M tokens × a commercial batch is measured in petabytes.

---

[referencia=363fb5dd108968a4 score=0.576]
## 3. Before MLA: The 2023 Baseline

DeepSeek LLM 7B and 67B: a textbook MHA/GQA pair, 480 KB and 380 KB per token, and the problem that motivated everything after.

DeepSeek's first-generation language models, released in November 2023 and documented in *DeepSeek LLM: Scaling Open-Source Language Models with Longtermism* (arXiv:2401.02954), are deliberately unglamorous. The two models — a 7B and a 67B dense transformer — were built to prove the lab could scale the standard recipe with unusually careful data hygiene (67B surpassing LLaMA-2 70B on code, math, and reasoning benchmarks with a smaller training corpus), not to innovate on attention. And that makes them the perfect baseline: they show exactly what the cache costs when nobody has touched it.

The attention designs were the era's defaults, as the team's own release notes state plainly: *the 7B model uses Multi-Head attention (MHA) while the 67B model uses Grouped-Query Attention (GQA)*. Plug the published configurations into the Chapter 2 formula and the baseline appears:

| Model (2023) | Attention | Query heads | KV heads | Head dim | Layers | Per layer | KV bytes / token (bf16) | 
|---|---|---|---|---|---|---|---|
| DeepSeek LLM 7B | MHA | 32 | 32 | 128 | 30 | 16,384 B | **491,520 B ≈ 480 KB** | 
| DeepSeek LLM 67B | GQA | 64 | 8 | 128 | 95 | 4,096 B | **389,120 B ≈ 380 KB** |

---

[referencia=363fb5dd108968a4 score=0.574]
### 5.3 — The absorption trick

Decode's cost is bytes read, so the game is: attend *against the latent directly*, never reconstruct K. Matrix associativity makes it legal:

```
q_nope @ k_nope^T
  = (c_Q @ W_UQ_nope) @ (c_KV @ W_UK_nope)^T
  = c_Q @ [ W_UQ_nope @ W_UK_nope^T ] @ c_KV^T
             \______ precomputed once: W_absorb ____/      # 1536 x 512
# decode attention = SDPA(q_absorbed, c_KV) + SDPA(q_rope, k_rope)
#                  ~ MQA-shaped: one shared 576-elem "key" per token
```
Precompute W_absorb = W_UQ_nope @ W_UK_nope^T once at engine warmup, and every decode step's key path is a plain matrix multiply against the 576-element cache — structurally identical to multi-query attention, which is why FlashMLA and even Apple's MLX run MLA decode as ordinary scaled_dot_product_attention after absorption. The value path has a mirror trick available (folding W_UV @ W_O), but production engines decline it: the fused matrix would be 3.7× larger than keeping the two separate (a weight-traffic regression that would eat the cache savings), so W_UV and W_O are applied as two small post-attention operations. Engineering is knowing which algebra to leave on the table.

### 5.4 — Two modes, one mechanism

Because prefill is compute-bound and decode is memory-bound, MLA runs in two mathematically equivalent regimes — the V2 paper's own framing, confirmed by the V3.2 infrastructure notes:

| Mode | Strategy | Where used | Why | 
|---|---|---|---|
| **MHA mode** | Reconstruct full K, V from latents; run standard multi-head flash attention | Training · prefill | Compute-bound phase: FLOPs dominate, reconstruction is free, kernels are optimal | 
| **MQA mode** | Absorb W_UK/W_UV into Q and O; attend directly against the cached latent | Decode | Memory-bound phase: extra FLOPs are free, reading 57× fewer cache bytes is everything |

---

[referencia=363fb5dd108968a4 score=0.481]
## Frequently asked questions

### What is Multi-head Latent Attention (MLA)?

MLA is the attention design DeepSeek introduced in DeepSeek-V2 (May 2024). Instead of caching per-head keys and values, it caches a single 512-dimensional compressed latent plus a 64-dimensional rotary key per token — 576 cached elements per layer — and reconstructs the per-head keys and values on demand. The V2 paper reports a 93.3% KV cache reduction and a 5.76x maximum generation throughput versus DeepSeek 67B.

### What is DeepSeek Sparse Attention (DSA)?

DSA is the sparse-attention mechanism shipped experimentally in DeepSeek-V3.2-Exp (September 2025). A 64-head lightning indexer scores every cached token cheaply and selects the top 2,048, so only those entries pay the full MLA cost. This cuts the bytes read per decode step by roughly 5x at 131K context.

### What is the lightning indexer in DeepSeek Sparse Attention?

The lightning indexer is DSA's cheap scoring stage: 64 multi-query heads that score every cached token so the model can select the top 2,048 to attend to. Because it scores all tokens but only selects a few, it shrinks the bytes read per decode step without shrinking what must be stored.

### How small is DeepSeek-V4.1-Flash's KV cache?

890 bytes per token in HBM, down from roughly 390 KB per token for DeepSeek's 2023 models — a 438x reduction. It is achieved with CSA2 cross-layer KV reuse, 4-bit MXFP4 cache storage, and replaying instead of persisting sliding-window state, which also gives one-eighth the persistent SSD footprint of V4-Flash.

### What is CSA2 in DeepSeek-V4.1-Flash?

CSA2 (Compressed Sparse Attention 2) is the attention design in DeepSeek-V4.1-Flash. It adds a third compression axis — reusing KV entries across layers through Full, Reindex and Reuse modes — on top of CSA's 4x token pooling and HCA's 128x pooling, and stores the cache in 4-bit MXFP4.

---

[referencia=363fb5dd108968a4 score=0.453]
### 10.1 — The indexer, precisely

The indexer is deliberately dumb and deliberately small. It runs in multi-query mode — 64 heads, all sharing one cached 128-dimensional key per token — and computes nothing but dot products:

```
I(t, s) = sigmoid( tau * sum_j w_j * ReLU( q_tj . k_s ) )
#          \_______/    \__ head weights __/ \_ shared key _/
# 64 query heads, 128-dim shared index key, one score per (query, token)
# - ReLU: only positive evidence counts (no softmax over all tokens)
# - w_j: learned per-head weights, combined into ONE relevance score
# - sigmoid(tau * .): bounded gate; tau is a learned temperature
#
# top_k = 2048:  the k tokens with highest I(t, s) get full MLA attention
```
Because the indexer stores keys only — no values, no full attention — and shares its key across heads MQA-style, its per-token footprint is minimal: 128 bytes for the fp8 key plus a 4-byte fp32 block scale, **132 bytes per token per layer**, one-fifth of the latent's 656. The vLLM Day-0 support post documents the production layout exactly, including the per-block fp8 scales and the block size of 64 that FlashMLA's paged layout had already standardized. The indexer is trained jointly with the model — the V3.2 report describes learning it during a continued-pretraining phase — so the selection policy is the model's own learned judgment, not a heuristic bolted on afterward.

---

[referencia=363fb5dd108968a4 score=0.352]
### 14.2 — CSA2: the three axes, all at once

CSA2 is the mechanism the V4.1 report describes as minimizing cache storage and computation "across three dimensions" — the taxonomy from Chapter 2, finally complete:

| CSA2 axis | Mechanism | Inherited from | 
|---|---|---|
| **Entry size** | Projection shares information across heads; **main KV quantized to MXFP4** (OCP-standard 4-bit) via quantization-aware training | MLA (V2) + the precision ladder | 
| **Sequence dimension** | Multiple tokens compressed into single KV entries (the V4 pooling family) | CSA/HCA (V4) | 
| **Layer dimension** | **KV entries reused across layers** — the new move | V4.1-Flash (2026) | 

Cross-layer reuse is implemented as three operating modes that different layers run in. **Full mode**: the layer computes its own main K and V, projects an indexer key, and generates fresh top-k indices — the expensive, authoritative pass. **Reindex mode**: the layer reuses the main KV *and the indexer keys* from a previous layer but computes its own indexer query, selecting a different top-k subset — new selection, zero re-storage. **Reuse mode**: both the main KV and the top-k indices are inherited outright from a preceding layer, eliminating essentially all index-related computation. Stacked across 20 decoder layers, the modes mean one authoritative KV computation serves several layers of attention, with only queries (which are never cached) varying per layer.

The residual risk — that shared indices starve some layers of the tokens they need — is handled by the **Hierarchical Sparse Indexer**: the first Full-mode decoder layer selects a blockwise candidate pool, and subsequent Reindex-mode layers score only candidates *within that pool*. The report's claim is the one that makes 1M context boring: per-query indexing cost stays bounded whether the context is 10,000 tokens or 1,000,000. Selection no longer scales with history.

---

[referencia=363fb5dd108968a4 score=0.327]
### The worked example that frames everything

Fix one benchmark in memory, because this paper returns to it in every part. Take DeepSeek-V3's published attention geometry: 128 heads, head_dim 128, 61 layers, and the MLA latent of 512 + 64 = 576 cached elements per layer. In bf16, the Tensor Economics computation gives 4.0 MB/token for counterfactual MHA, ~500 KB for GQA-8 at the Llama-3 ratio, and **70 KB for MLA** — a 57× and 7× reduction respectively. Now project to a production decode step at 131K context: dense MLA reads 5.2 GB per step (656 bytes × 131,072 tokens × 61 layers); DSA reads 1.1 GB; V4 reads a fraction of that; V4.1-Flash reads 890 bytes × some bounded selection × a layer count that shares entries across halves of the network. The entire history of this paper is visible in that one progression — and every one of those numbers will be re-derived, with sources, in its own chapter.

With the formula and the axes in hand, we can finally meet the baseline: the 2023 models where none of these levers had been pulled, and the cache was exactly as large as naive attention made it.

---

[referencia=363fb5dd108968a4 score=0.299]
## 1. The Cache Problem: Why KV Memory Decides Everything

Attention needs the past. The past needs memory. Memory is the bottleneck.

Transformers generate tokens one at a time, but attention is defined over the entire past. When a model attends, every query must be compared against every key that came before it, and every surviving comparison must fetch its value. Recomputing all of that for every new token would be quadratic hell, so inference engines cache the keys and values once and reuse them: that store is the **KV cache**. It is the model's working memory of the conversation, and its size is brutally predictable — it grows linearly with every token in every sequence in the batch, forever, until something gives.

What gives first is bandwidth. During decoding, the model is *memory-bound*: each new token requires the GPU to read the entire cache (and the active weights) from HBM, do a little math, and write one token out. An H100 ships 3.35 TB/s of HBM bandwidth; the Tensor Economics team's benchmark of a single Llama-3.3-config attention layer at batch 64 shows decode latency tracking the "total bytes moved ÷ 3.35 TB/s" line almost exactly, with compute essentially free by comparison. This is why the chapter of this paper you are reading exists: at long context, **the cache is the workload**. A model whose cache is 10× smaller is, to first order, a model whose decode is 10× cheaper — and whose batching headroom, context ceiling, and offload options all improve at the same time.

---

[referencia=363fb5dd108968a4 score=0.219]
The history breaks into four discontinuities, and this paper treats each as a case study with the arithmetic shown in full. **First, Multi-head Latent Attention (MLA)**, introduced in DeepSeek-V2 in May 2024: instead of caching per-head keys and values, cache a single 512-dimensional compressed latent plus a 64-dimensional rotary key per token, and reconstruct the rest on the fly. The official paper reports a 93.3% KV cache reduction against DeepSeek 67B while boosting maximum generation throughput 5.76×. **Second, DeepSeek Sparse Attention (DSA)**, which arrived experimentally in V3.2-Exp in September 2025: a "lightning indexer" — 64 cheap multi-query heads scoring every cached token — selects the top 2,048 entries, and only those pay the full MLA bill, cutting the bytes read per decode step by roughly 5× at 131K context. **Third, the hybrid compressed attention of DeepSeek-V4** in April 2026: Compressed Sparse Attention (CSA) pools four tokens into one cached entry while Heavily Compressed Attention (HCA) pools 128, together bringing a 1M-token context window within reach at 10% (V4-Pro) to 7% (V4-Flash) of V3.2's cache footprint. **Fourth, CSA2 in DeepSeek-V4.1-Flash** (September 10, 2026), which adds the third axis nobody had dared: reusing KV entries *across layers*, storing the cache in 4-bit MXFP4, and replaying instead of persisting sliding-window state — 890 bytes per token in HBM, one-eighth the persistent SSD footprint of V4-Flash.

---

[referencia=363fb5dd108968a4 score=0.124]
Agents make it worse in a specific, structural way. The V4.1-Flash report describes the new reality plainly: long-horizon agents have made workloads *input-heavy*. A coding agent re-submits a growing repository transcript on every tool call; a browsing agent accumulates page dumps; a reasoning model keeps its own chain of thought in context. Input-heavy means cache-heavy: the prompt is processed once (prefill, compute-bound) but then sits in the cache being re-read on every single decode step (memory-bound) for as long as generation lasts. Multiply by continuous batching — the technique that makes serving profitable by packing dozens of concurrent requests into one GPU — and the cache's linear growth becomes the wall. Weights load once and amortize across the batch; the cache grows with the batch. At large combined sequence lengths, cache traffic exceeds weight traffic and never looks back.

DeepSeek's response to this wall is the through-line of this paper, and it is notably architectural rather than infrastructural. Other labs met the cache with bigger HBM pools, paged memory management (vLLM's PagedAttention), prefix cache reuse, or aggressive speculative decoding. DeepSeek did those too, but its signature move was to keep attacking the *bytes per token* inside the model itself, generation after generation:

**2024 — MLA (DeepSeek-V2).**Compress

*what*is cached: one shared 576-element latent replaces per-head keys and values. Official result: 93.3% cache reduction, 5.76× max generation throughput.

**2025 — DSA (DeepSeek-V3.2-Exp).**Choose

*which*tokens are read: a lightning indexer scores everything cheaply, and full attention touches only the top 2,048. Decode traffic at 131K context drops ~5×.

**2026 (April) — CSA + HCA (DeepSeek-V4).**Shrink the sequence itself: pool 4 tokens into one cached entry (CSA) or 128 into one (HCA), interleaved across layers. 1M-token context at 10%/7% of V3.2's cache.

**2026 (September) — CSA2 + FP4 + CED (DeepSeek-V4.1-Flash).**Share the cache

---

[referencia=363fb5dd108968a4 score=0.119]
### What it meant at the time

V2's 128K context arrived at 67.5 KB/token instead of 240 KB: at full window, one request's cache falls from ~31.5 GB (counterfactual GQA-8) to ~8.9 GB, and — because decode traffic scales with cache bytes — the measured maximum generation throughput rose 5.76× against the 67B. The launch-era API pricing made the savings visible to customers immediately, and the lab followed with a systems-level complement that turned prefix reuse into a near-free operation (Chapter 6). But the deeper consequence was strategic: V2 proved that a frontier-quality model could carry an order-of-magnitude cache advantage, which is precisely the property that later made a 671B V3 affordable to train (Chapter 7), a reasoning RL run viable on top of it (Chapter 8), and a 1M-token V4 conceivable (Chapter 12).

| DeepSeek-V2 vs. predecessors | DeepSeek 67B (2023) | DeepSeek-V2 (May 2024) | 
|---|---|---|
| Total / active params | 67B dense | 236B total · 21B active (MoE) | 
| Attention | GQA-8 | **MLA** (512+64 latent, 128 heads) | 
| Context | 4K (32K ext.) | 128K | 
| KV bytes / token | ~389 KB | **~70 KB (bf16)** | 
| Official claims vs. 67B | — | −42.5% training cost · −93.3% KV cache · 5.76× max generation throughput | 
| Ecosystem effect | — | MLA later adopted by Kimi K2, reused unchanged in V3/R1/V3.1 |

---

[referencia=363fb5dd108968a4 score=0.107]
### 14.3 — The 890 bytes, accounted

The arithmetic of the headline now closes. Per token: MXFP4 main KV entries (4 bits per element across the pooled, head-shared latents), a 4×-pooled sequence representation inherited from the V4 compressor family, an indexer's worth of small keys — and the layer dimension divided by the reuse factor of the Full/Reindex/Reuse schedule. The result, always resident in HBM: **890 bytes per token, against ~390,000 bytes for DeepSeek-V1 at 67B scale — a 438× reduction** in the report's own retrospective framing. Composed with the CED prefill halving and the bounded indexer, the report plots decode computation remaining nearly constant as context scales to one million tokens.

### 14.4 — SWA Bounded Replay: deleting the local cache

The slickest systems trick in the release targets persistent storage. Hybrid attention needs a sliding-window cache for recent tokens, and that cache traditionally must be persisted (to SSD or host DRAM) so a resumed request can rebuild its state. V4.1-Flash declines: **when a request resumes and the sliding-window KV is missing, the system replays only the most recent n<sub>win</sub> tokens to approximately reconstruct the local state** — accepting a bounded approximation on local detail rather than paying to persist exact copies. The global cache (long-term dependencies) remains worth persisting exactly; the local one does not. Persistent footprint: one eighth of V4-Flash's, and the agent-billing consequence is the announcement's own line — cache-hit charges are a large share of agent costs, and compressing the cache cuts them significantly.

**ENCODER · 20 layers · 8B active**

processes the input once; produces H

<sub>L/2</sub>

global KV entries projected from encoder output

**DECODER · 20 layers · 16B active**

generates; reuses encoder-projected global KV

Full / Reindex / Reuse modes share entries across layers

**Hierarchical indexer**

Full-mode layer picks a blockwise candidate pool; Reindex layers search only inside it

**MXFP4 main cache**

QAT-trained 4-bit KV entries · 890 B/token in HBM

**SWA Bounded Replay**

local window reconstructed by replaying n

<sub>win</sub>recent tokens · persistent KV ÷ 8

---

[referencia=363fb5dd108968a4 score=0.101]
### 10.3 — What it cost and what it bought

The quality story is the part the industry watched most closely, and it is clean: across the V3.2-Exp evaluation suite, benchmark scores match V3.1-Terminus — the same model with dense attention — to within noise on standard reasoning and knowledge tasks, with long-context retrieval tasks (where full attention's exhaustive scan was thought to matter most) holding at or above the dense baseline. Sparsity, trained properly, was free. What it bought was commercial: the launch announcement's price table — input cache-miss $0.28/M (from $0.56), cache-hit $0.028/M, output $0.42/M (from $1.68) — a cut of 50% on input and 75% on output, effective the same day. The Tensor Economics commentary called the mechanism out as the enabler of profitable long-context coding products; the pricing table is that thesis with numbers attached.

**Query q**(128 MLA heads + 64 indexer heads)

<sub>t</sub>
**Lightning indexer**

score all N tokens vs. shared 128-d keys (132 B/token, fp8)

I(t,s) = sigmoid(τ · Σ w

<sub>j</sub>ReLU(q

<sub>j</sub>·k

<sub>s</sub>))

**Top-k selection**

keep the 2,048 highest-scoring tokens

fused TileLang-style topk kernel

**Sparse MLA attention**

full 656-byte latents for exactly k = 2,048 tokens

fixed cost · identical to dense MLA, minus 99% of the tokens

---

[referencia=363fb5dd108968a4 score=0.100]
## 12. V4: CSA + HCA, the 1M Era

April 24, 2026: two checkpoints, one million tokens of context, and a hybrid attention stack that pools the past before it caches it.

DeepSeek-V4 Preview (arXiv:2606.19348, open-sourced April 24, 2026) is the release where the KV cache stops being a compressed record of the past and becomes a *summary* of it. Two MoE checkpoints shipped together: **V4-Pro**, 1.6T total parameters with 49B active, and **V4-Flash**, 284B total with 13B active — both carrying a 1M-token context window. The headline comparisons were framed against V3.2 at one million tokens: **V4-Pro uses 27% of the single-token inference FLOPs and 10% of the KV cache memory; V4-Flash drops to 10% of the FLOPs and 7% of the cache**. Against a conventional GQA-8 design storing bf16, the V4 cache is roughly 2% of the size. The mechanism is a hybrid of two new attention types, interleaved layer by layer.

### 12.1 — Compressed Sparse Attention (CSA)

CSA attacks the sequence axis directly: **every 4 tokens are pooled into a single cached KV entry** using softmax-gated pooling with a learned positional bias — the compressor decides, per group, how to represent four tokens in one pair of latent vectors. A lightning indexer (the V3.2 inheritance, now running its dot-product scoring over the 4×-shorter compressed stream in FP4) then picks the top-k compressed blocks per query, and attention reads only those. The causality subtlety that pooling introduces — a compressed entry aggregates future tokens into a past token's representation — is handled by a strict guard documented in DeepSeek's LMCache collaboration: **entries are only compressed once they are at least 128 tokens behind the current position**, so no query ever attends to information from its own future. A sliding-window branch covers the uncompressed recent tokens, whose local detail pooling would blur.

---

[referencia=363fb5dd108968a4 score=0.095]
## 5. Inside MLA: The Mathematics

Down-projections, up-projections, the absorption trick, decoupled RoPE, and the two execution modes that make prefill and decode each optimal.

MLA is six matrices and one idea. This chapter is the complete derivation, using DeepSeek-V3's published configuration as the running example (identical geometry to V2's attention except for layer count), because those are the values every serving kernel in the ecosystem is compiled around today. Follow the symbols once here and Chapters 10, 12, and 14 read like plain prose; the dimensions are also collected in Table 5.1 for reference.

### 5.1 — Compress, then cache

For each token's hidden state h (7168 dims in V3), MLA computes a **compressed latent for K and V jointly**:

```
c_KV = W_DKV @ h          # W_DKV: 7168 x 512   -> the ONLY thing cached for content
# c_KV: 512 dims per token per layer, shared by all 128 heads
# reconstruction (used in prefill / training):
K_C = W_UK @ c_KV         # 512 -> 128 heads x 128 dims
V_C = W_UV @ c_KV         # 512 -> 128 heads x 128 dims
```
The latent is the cache: 512 floats instead of 32,768. Queries get the same treatment with a wider bottleneck — c_Q = W_DQ @ h with W_DQ projecting 7168 → 1536 — but queries are never cached, so their compression is purely a FLOPs/regularization play. The asymmetry (512 for cached KV, 1536 for transient Q) is deliberate: you spend dimensions where persistence costs money.

---

[referencia=363fb5dd108968a4 score=0.088]
| Model (date) | Attention | Total / active | Context | KV bytes / token | Basis | vs. V1 | 
|---|---|---|---|---|---|---|
| DeepSeek LLM 7B (Nov 2023) | MHA | 7B dense | 4K | 491,520 B | bf16 arithmetic | 1.26× worse | 
| DeepSeek LLM 67B (Nov 2023) | GQA-8 | 67B dense | 4K–32K | 389,120 B | bf16 arithmetic | 1× (baseline) | 
| DeepSeek-V2 (May 2024) | MLA | 236B / 21B | 128K | 69,120 B | bf16 arithmetic | 5.6× smaller | 
| V2.5 / V2.5-1210 (Sep–Dec 2024) | MLA | 236B / 21B | 128K | 69,120 B | unchanged | 5.6× smaller | 
| DeepSeek-V3 (Dec 2024) | MLA | 671B / 37B | 128K | 70,272 B | bf16 (35.4 KB fp8) | 5.5× smaller | 
| R1 / R1-0528 (2025) | MLA | 671B / 37B | 128K | 70,272 B | unchanged | 5.5× smaller | 
| V3.1-Terminus (Aug 2025) | MLA | 671B / 37B | 128K | 70,272 B | unchanged | 5.5× smaller | 
| V3.2 / V3.2-Exp (Sep–Dec 2025) | MLA + DSA | 671B / 37B | 128K | 48,068 B | stored, fp8 latent + 132 B indexer | 8.1× smaller | 
| V4-Pro (Apr 2026) | CSA + HCA + SWA | 1.6T / 49B | 1M | ~10% of V3.2 | DeepSeek claim @1M | ~80× smaller |