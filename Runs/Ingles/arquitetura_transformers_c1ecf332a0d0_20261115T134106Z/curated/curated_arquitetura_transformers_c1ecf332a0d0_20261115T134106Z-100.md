[referencia=363fb5dd108968a4 score=0.991]
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

[referencia=363fb5dd108968a4 score=0.979]
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

[referencia=363fb5dd108968a4 score=0.977]
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

[referencia=363fb5dd108968a4 score=0.977]
### 5.2 — The RoPE problem and the decoupling

Rotary position embeddings rotate queries and keys by position, and rotation does not commute through matrix multiplication. If RoPE sat between c_KV and the reconstructed key, you could never fold W_UK into anything — the rotation would have to be applied to the full reconstructed key at every step, re-materializing exactly the tensor MLA exists to avoid. DeepSeek's solution, **decoupled RoPE**, splits every head's key into two parts that never mix:

- **The NoPE part (content, 128 dims per head):** derived from the latent, carries semantic content, never rotated, and fully absorbable.
- **The RoPE part (position, 64 dims):** a single shared key k_rope = RoPE(W_KR @ h) computed directly from the hidden state (7168 → 64), cached alongside the latent, and broadcast to all 128 heads.

The asymmetry is the elegant part: each head keeps its *own* 64-dim RoPE query (heads specialize positionally at zero cache cost) while sharing one RoPE key across all heads — saving 128× on the positional cache. Per head, the attention score is simply the sum of the two dot products: q_nope·k_nope + q_rope·k_rope. Total cache per token per layer: **512 (NoPE latent) + 64 (shared RoPE key) = 576 elements** — the number that recurs through every model from V2 to V3.2.

---

[referencia=363fb5dd108968a4 score=0.958]
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

[referencia=363fb5dd108968a4 score=0.948]
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

[referencia=363fb5dd108968a4 score=0.923]
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

[referencia=363fb5dd108968a4 score=0.919]
## 7. V2.5 to V3: Scaling the Latent

December 26, 2024: 671B parameters, 37B active — and the exact same 576-element cache, now carrying the biggest open model on Earth.

DeepSeek-V3 (arXiv:2412.19437) is the model that made the lab globally famous, and its treatment of the KV cache is a study in confidence: **it changed nothing**. The technical report adopts MLA and DeepSeekMoE "thoroughly validated in DeepSeek-V2" as-is — the same 512+64 latent, the same 128 heads, the same decoupled RoPE — and simply scales around them: 671B total parameters, 37B active per token, 61 layers (one more than V2), 14.8T pretraining tokens, and an auxiliary-loss-free load-balancing scheme that keeps the MoE routing healthy without gradient interference. Training consumed 2.788M H800 GPU-hours (about $5.6M at rental rates, the report notes) with zero irrecoverable loss spikes.

That stability is the point of this chapter. V3 was the test of whether MLA's low-rank cache survives a 10× parameter scale-up, 128K native context, FP8 mixed-precision training, and multi-token prediction heads — and it passed without modification. The Tensor Economics recomputation of the cache arithmetic at V3's exact geometry (128 heads, 128 head_dim, 61 layers) makes the inherited advantage precise:

| Attention at V3 geometry (61 layers) | Per layer | Per token (bf16) | Per token (fp8 latent) | vs. MLA | 
|---|---|---|---|---|
| Counterfactual MHA (128 heads) | 65,536 B | 4.0 MB | 2.0 MB | 57× larger | 
| Counterfactual GQA-8 (Llama-3 ratio) | 4,096 B | ~500 KB | ~250 KB | 7× larger | 
| **MLA (as shipped)** | 1,152 B | **70.3 KB** | **~35.2 KB** | 1× |

---

[referencia=363fb5dd108968a4 score=0.917]
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

[referencia=363fb5dd108968a4 score=0.908]
The history breaks into four discontinuities, and this paper treats each as a case study with the arithmetic shown in full. **First, Multi-head Latent Attention (MLA)**, introduced in DeepSeek-V2 in May 2024: instead of caching per-head keys and values, cache a single 512-dimensional compressed latent plus a 64-dimensional rotary key per token, and reconstruct the rest on the fly. The official paper reports a 93.3% KV cache reduction against DeepSeek 67B while boosting maximum generation throughput 5.76×. **Second, DeepSeek Sparse Attention (DSA)**, which arrived experimentally in V3.2-Exp in September 2025: a "lightning indexer" — 64 cheap multi-query heads scoring every cached token — selects the top 2,048 entries, and only those pay the full MLA bill, cutting the bytes read per decode step by roughly 5× at 131K context. **Third, the hybrid compressed attention of DeepSeek-V4** in April 2026: Compressed Sparse Attention (CSA) pools four tokens into one cached entry while Heavily Compressed Attention (HCA) pools 128, together bringing a 1M-token context window within reach at 10% (V4-Pro) to 7% (V4-Flash) of V3.2's cache footprint. **Fourth, CSA2 in DeepSeek-V4.1-Flash** (September 10, 2026), which adds the third axis nobody had dared: reusing KV entries *across layers*, storing the cache in 4-bit MXFP4, and replaying instead of persisting sliding-window state — 890 bytes per token in HBM, one-eighth the persistent SSD footprint of V4-Flash.

---

[referencia=363fb5dd108968a4 score=0.860]
| Ecosystem adoption, MLA/DSA lineage | What shipped | Significance for the cache | 
|---|---|---|
| Kimi K2 (Moonshot, 2025) | MLA in a 1T-class MoE | Latent cache proven outside DeepSeek | 
| FlashMLA + DeepGEMM (Feb 2025, open source) | Production decode kernels, Hopper, paged KV, block 64 | The 576-element latent becomes a standard layout | 
| NSA paper (Feb 2025) | Trainable sparse attention, hardware-aligned | The design V3.2's DSA productionizes | 
| SGLang / vLLM / TRT-LLM (2025) | MLA decode paths in all major engines | Serving the latent becomes table stakes | 
| MLX / llama.cpp lineage (2025–2026) | Absorbed MLA as plain SDPA | Full compression with zero custom kernels — edge-portable | 
| GLM-5 / 5.1 (Z.ai, 2026) | DSA adopted outright | DeepSeek's sparsity becomes the industry's sparsity | 

By the middle of 2025, every piece was on the table except the one that mattered: using it all in a shipping model. The interim release — V3.1 — would be the last DeepSeek model to read its entire cache on every decode step.

---

[referencia=363fb5dd108968a4 score=0.834]
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

[referencia=363fb5dd108968a4 score=0.824]
## 8. R1, FlashMLA & the Ecosystem

January–February 2025: the reasoning model that stress-tested MLA, and the open kernels that turned one lab's trick into an industry standard.

DeepSeek-R1 (January 20, 2025) was the model that put the lab on every front page, and from the KV cache's perspective it was the harshest test the latent would ever face. R1 is built on V3's 671B/37B architecture — same MLA, same 61 layers, same 576-element latent — and then trained with GRPO reinforcement learning to think in long, self-generated chains. Reasoning traces are the input-heavy workload par excellence: tens of thousands of tokens of self-dialogue that stay pinned in the cache while the model generates tens of thousands more. If the low-rank latent were a quality bottleneck, RL would find it — RL is a ruthless optimizer of whatever the model can and cannot express. R1's results (matching OpenAI o1 on math, code, and reasoning benchmarks) showed the compressed cache carried a frontier reasoning model without visible strain, and the May 28, 2025 R1-0528 update, with its deeper thinking traces and better tool use, re-confirmed it under heavier loads.

The second ecosystem event of the winter was the one that mattered structurally: on February 24, 2025, DeepSeek open-sourced **FlashMLA** — its production MLA decode kernels for NVIDIA Hopper GPUs, developed alongside the team's DeepGEMM FP8 GEMM library. The release targeted multi-batch, split-KV serving with paged cache organization (block size 64, matching the page geometry V3.2 would later require), BF16 decode optimized for the H3D regime (300–600 GB/s effective bandwidth conditions), and the now-canonical 576-element latent layout. Together with the earlier NSA paper this constituted a deliberate infrastructure reveal: the attention mechanism *and* the optimized kernels to run it were now public property.

---

[referencia=363fb5dd108968a4 score=0.807]
### 10.2 — The two caches, byte by byte

| Cache component (per token, per layer) | Bytes | Composition | Read per decode step | 
|---|---|---|---|
| **MLA latent** (main cache) | **656 B** | 512 B NoPE latent (fp8_e4m3) + 16 B scales (4 × fp32, block 128) + 128 B RoPE key (bf16, kept high-precision) | Only for the k = 2,048 selected tokens | 
| **Indexer key cache** | **132 B** | 128 B shared 128-d key (fp8) + 4 B scale (1 × fp32, block 128) | For ALL N cached tokens | 
| Total stored | 788 B | — | 61 × (132·N + 656·2048) | 

The asymmetry between the two caches is the entire invention. The indexer must see every token (it cannot know what is irrelevant without scoring it), but it sees them at 132 bytes instead of 656. The main attention reads the full-fat latent only for the 2,048 tokens the indexer selected — a fixed cost that does not grow whether the context holds 10,000 tokens or 131,000. Storage still grows with N (nothing is evicted; the selected set changes every step), but *read traffic*, the thing that determines decode time on a bandwidth-bound GPU, is now:

```
dense_Mla(N) = 656 B * N      * 61          # everything, every step
dsa(N)      = 132 B * N      * 61          # indexer sees all, cheap
             + 656 B * 2048  * 61          # latent read: FIXED (82 MB total)
# N = 131,072 (128K context):
#   dense: 656 * 131072 * 61          = 5.24 GB per step
#   DSA:   132 * 131072 * 61 + 82 MB  = 1.06 + 0.08 = ~1.1 GB per step
#   ratio: ~4.8x less traffic -> near-constant decode time at depth
```

---

[referencia=363fb5dd108968a4 score=0.797]
The arithmetic for an agent is stark and worth internalizing, because it is the template for every pricing decision DeepSeek has made since. A coding agent with a 32K-token system prompt, tool definitions, and repo context, making 500 calls in a session, re-sends that 32K prefix 500 times: 16M input tokens of pure repetition. Without caching that is 16M full-price tokens plus the prefill compute; with an effective disk cache it is one miss plus 499 hits at a tenth (later a fiftieth) of the price. This is why the announcement could honestly claim "up to 90%" — and why cache-hit ratios became a first-class number to monitor in the API's usage dashboard (the docs expose hit/miss fields on every response). The agent era's economics were being quietly rewritten nine months before anyone said "agentic workloads" in a model announcement.

| Context caching economics (Aug 2024 era, deepseek-chat on V2.5) | Uncached | With disk cache | 
|---|---|---|
| 500 calls × 32K shared prefix | 16M tokens @ $0.14/M | 16M tokens: 1 miss + 499 hits | 
| Prefix cost | $2.24 | ~$0.22 (90% cut) | 
| Prefill compute | 500 full re-prefills | 1 prefill + 499 KV loads | 

The model lineage around this systems work kept improving while the attention stayed frozen: **DeepSeek-V2.5** (September 5, 2024) merged the V2 chat and DeepSeek-Coder lines into one model with the same MLA cache and 128K context, and the **V2.5-1210** point release (December 10, 2024) tuned alignment and function-calling — the property agents actually felt. Through all of it, the per-token cache never changed: 576 elements, ~70 KB. The compression and the reuse were now both in place. What remained was scale — and the 671B model that would make MLA carry more parameters than any open model in history.

---

[referencia=363fb5dd108968a4 score=0.781]
### The worked example that frames everything

Fix one benchmark in memory, because this paper returns to it in every part. Take DeepSeek-V3's published attention geometry: 128 heads, head_dim 128, 61 layers, and the MLA latent of 512 + 64 = 576 cached elements per layer. In bf16, the Tensor Economics computation gives 4.0 MB/token for counterfactual MHA, ~500 KB for GQA-8 at the Llama-3 ratio, and **70 KB for MLA** — a 57× and 7× reduction respectively. Now project to a production decode step at 131K context: dense MLA reads 5.2 GB per step (656 bytes × 131,072 tokens × 61 layers); DSA reads 1.1 GB; V4 reads a fraction of that; V4.1-Flash reads 890 bytes × some bounded selection × a layer count that shares entries across halves of the network. The entire history of this paper is visible in that one progression — and every one of those numbers will be re-derived, with sources, in its own chapter.

With the formula and the axes in hand, we can finally meet the baseline: the 2023 models where none of these levers had been pulled, and the cache was exactly as large as naive attention made it.

---

[referencia=363fb5dd108968a4 score=0.747]
### The arithmetic, honestly done

Run the Chapter 2 formula across the full 60-layer stack and the totals fall out cleanly: MHA 3.84 MB/token, GQA-8 240 KB, MLA 67.5 KB (the paper rounds to 70 KB). MLA's per-token footprint is thus **56.9× smaller than MHA** at identical geometry — which matches the ~57× theoretical HBM-traffic reduction the paper derives for decoding — and **5.6× smaller than the 67B's GQA-8 across its 95 layers** (389 KB → 67.5 KB, an 82.2% reduction). The abstract's headline 93.3%, meanwhile, is DeepSeek's own accounting against the 67B under its stated comparison conditions; independent arithmetic at face-value configs lands between 82% and 98% depending on the baseline chosen (the V2 report's MHA-vs-MLA framing implies the upper end, the GQA framing the lower).

The 93.3% is quoted everywhere and verified nowhere at its exact value; what is verifiable is the shape of the result. Face-value arithmetic gives 5.6× (vs. 67B GQA-8) to 56.9× (vs. MHA at V2 scale) — a cache reduction somewhere between 82% and 98.2%. Every downstream claim in this paper uses the transparent arithmetic, and the official 93.3% is cited as the paper's own summary. Engineering readers should replicate the three-line calculation before quoting either number.

---

[referencia=363fb5dd108968a4 score=0.719]
Agents make it worse in a specific, structural way. The V4.1-Flash report describes the new reality plainly: long-horizon agents have made workloads *input-heavy*. A coding agent re-submits a growing repository transcript on every tool call; a browsing agent accumulates page dumps; a reasoning model keeps its own chain of thought in context. Input-heavy means cache-heavy: the prompt is processed once (prefill, compute-bound) but then sits in the cache being re-read on every single decode step (memory-bound) for as long as generation lasts. Multiply by continuous batching — the technique that makes serving profitable by packing dozens of concurrent requests into one GPU — and the cache's linear growth becomes the wall. Weights load once and amortize across the batch; the cache grows with the batch. At large combined sequence lengths, cache traffic exceeds weight traffic and never looks back.

DeepSeek's response to this wall is the through-line of this paper, and it is notably architectural rather than infrastructural. Other labs met the cache with bigger HBM pools, paged memory management (vLLM's PagedAttention), prefix cache reuse, or aggressive speculative decoding. DeepSeek did those too, but its signature move was to keep attacking the *bytes per token* inside the model itself, generation after generation:

**2024 — MLA (DeepSeek-V2).**Compress

*what*is cached: one shared 576-element latent replaces per-head keys and values. Official result: 93.3% cache reduction, 5.76× max generation throughput.

**2025 — DSA (DeepSeek-V3.2-Exp).**Choose

*which*tokens are read: a lightning indexer scores everything cheaply, and full attention touches only the top 2,048. Decode traffic at 131K context drops ~5×.

**2026 (April) — CSA + HCA (DeepSeek-V4).**Shrink the sequence itself: pool 4 tokens into one cached entry (CSA) or 128 into one (HCA), interleaved across layers. 1M-token context at 10%/7% of V3.2's cache.

**2026 (September) — CSA2 + FP4 + CED (DeepSeek-V4.1-Flash).**Share the cache

---

[referencia=363fb5dd108968a4 score=0.663]
## 1. The Cache Problem: Why KV Memory Decides Everything

Attention needs the past. The past needs memory. Memory is the bottleneck.

Transformers generate tokens one at a time, but attention is defined over the entire past. When a model attends, every query must be compared against every key that came before it, and every surviving comparison must fetch its value. Recomputing all of that for every new token would be quadratic hell, so inference engines cache the keys and values once and reuse them: that store is the **KV cache**. It is the model's working memory of the conversation, and its size is brutally predictable — it grows linearly with every token in every sequence in the batch, forever, until something gives.

What gives first is bandwidth. During decoding, the model is *memory-bound*: each new token requires the GPU to read the entire cache (and the active weights) from HBM, do a little math, and write one token out. An H100 ships 3.35 TB/s of HBM bandwidth; the Tensor Economics team's benchmark of a single Llama-3.3-config attention layer at batch 64 shows decode latency tracking the "total bytes moved ÷ 3.35 TB/s" line almost exactly, with compute essentially free by comparison. This is why the chapter of this paper you are reading exists: at long context, **the cache is the workload**. A model whose cache is 10× smaller is, to first order, a model whose decode is 10× cheaper — and whose batching headroom, context ceiling, and offload options all improve at the same time.

---

[referencia=363fb5dd108968a4 score=0.637]
## 3. Before MLA: The 2023 Baseline

DeepSeek LLM 7B and 67B: a textbook MHA/GQA pair, 480 KB and 380 KB per token, and the problem that motivated everything after.

DeepSeek's first-generation language models, released in November 2023 and documented in *DeepSeek LLM: Scaling Open-Source Language Models with Longtermism* (arXiv:2401.02954), are deliberately unglamorous. The two models — a 7B and a 67B dense transformer — were built to prove the lab could scale the standard recipe with unusually careful data hygiene (67B surpassing LLaMA-2 70B on code, math, and reasoning benchmarks with a smaller training corpus), not to innovate on attention. And that makes them the perfect baseline: they show exactly what the cache costs when nobody has touched it.

The attention designs were the era's defaults, as the team's own release notes state plainly: *the 7B model uses Multi-Head attention (MHA) while the 67B model uses Grouped-Query Attention (GQA)*. Plug the published configurations into the Chapter 2 formula and the baseline appears:

| Model (2023) | Attention | Query heads | KV heads | Head dim | Layers | Per layer | KV bytes / token (bf16) | 
|---|---|---|---|---|---|---|---|
| DeepSeek LLM 7B | MHA | 32 | 32 | 128 | 30 | 16,384 B | **491,520 B ≈ 480 KB** | 
| DeepSeek LLM 67B | GQA | 64 | 8 | 128 | 95 | 4,096 B | **389,120 B ≈ 380 KB** |