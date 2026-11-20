[referencia=4c6fe5590fff18ca score=0.996]
## FAQ

### What is a KV cache?

The stored attention keys and values for every token an LLM has processed, kept so each decoding step only computes the new token's keys and values.

### How do you calculate KV cache size?

2 x layers x KV heads x head dimension x bytes per element, per token. Mistral Small 3.2 in BF16 works out to 160 KiB per token and 20 GiB for a 131,072-token sequence.

### Does the KV cache change model outputs?

Exact caching and prefix caching do not. FP8 KV quantization is lossy, and with Flash Attention 3 vLLM quantizes queries to FP8 as well.

### What is PagedAttention?

A KV cache layout from vLLM that stores keys and values in fixed-size blocks, like OS memory pages, reporting near-zero waste and 2-4x throughput at equal latency.

### Why are cached input tokens cheaper?

The provider reuses a stored KV cache and skips prefill. DeepSeek charges $0.003 per million cache-hit tokens versus $0.15 on a miss, off-peak.

### Related Resources

### The fastest endpoints are private deployments

Morph's top speeds come from dedicated deployments, not shared public endpoints: speculators trained on your traffic, caching tuned to your workload, and volume discounts over public per-token rates. Over 1 trillion tokens per day run this way.

### Keep long agent contexts small

WarpGrep is an agentic code search tool that works as an MCP server. It returns only the code an agent needs, so less of the context window and KV cache goes to files the model never uses.

---

[referencia=4c6fe5590fff18ca score=0.984]
## What Is a KV Cache?

A KV cache (key-value cache) is the memory an LLM inference engine uses to store the attention keys and values of every token it has already processed. Each new token has to attend to all earlier tokens. The cache lets the engine compute keys and values for the new token only and read the earlier ones back from GPU memory, instead of recomputing the whole sequence on every decoding step.

## KV Cache Explained Step by Step

Inference runs in two phases. Prefill processes the whole prompt in one parallel pass and writes a key vector and a value vector for every prompt token, in every attention layer, for every KV head. Decode then generates output one token at a time. At each step the model computes a query for the new token, compares it against all cached keys, takes the weighted sum of cached values, and appends the new token's own key and value to the cache.

Queries are not cached because each one is used once, by the token that produced it. Keys and values are reused by every later token, which is why they are worth keeping. Hugging Face measured a 38% generation speedup after adding a KV cache to its small nanoVLM codebase; the gain grows with sequence length because the recompute it avoids grows with sequence length.

The trade is compute for memory. Decode becomes memory-bandwidth bound: every step reads the model weights plus the entire KV cache for each sequence in the batch. Once sequences get long, the cache is often larger than the activations and competes with the weights for HBM.

## KV Cache Size Formula

For a standard transformer with full attention on every layer:

2 x num_layers x num_key_value_heads x head_dim x bytes_per_element

The leading 2 counts keys and values. Total cache = bytes per token x sequence length x concurrent sequences. BF16 and FP16 use 2 bytes per element; FP8 uses 1.

Every term comes straight from a model's `config.json`. The one that moved most in recent years is `num_key_value_heads`. Grouped-query attention shares one KV head across several query heads, so Mistral Small 3.2 runs 32 query heads against 8 KV heads and stores a quarter of the cache multi-head attention would. Hybrid models change the formula further by giving full attention to only some layers.

---

[referencia=4c6fe5590fff18ca score=0.966]
## KV Cache Size for Real Models

The numbers below are computed from each model's published `config.json` on Hugging Face, in BF16, counting only layers whose cache grows with sequence length.

| Model | Layers that grow the cache | KV heads x head_dim | Per token | Long sequence | 
|---|---|---|---|---|
| Mistral Small 3.2 24B | 40 of 40 (all full) | 8 x 128 | 160 KiB | 20 GiB at 131,072 tokens | 
| gpt-oss-120b | 18 of 36 (rest: 128-token window) | 8 x 64 | 36 KiB | 4.5 GiB at 131,072 tokens | 
| Qwen3.8-27B | 16 of 64 (rest: linear attention) | 4 x 256 | 64 KiB | 16 GiB at 262,144 tokens | 

Layer type matters more than parameter count. gpt-oss-120b alternates full attention with sliding-window layers that only keep the last 128 tokens, so half its layers hold a fixed 4.5 MiB per sequence no matter how long the context gets. vLLM's hybrid KV cache manager exists for this case: it reserves slots for every token on full-attention layers and only the most recent window on sliding layers. Qwen3.8-27B goes further, with 48 of its 64 layers using linear attention that keeps a fixed-size state. If all 64 were full attention it would need 256 KiB per token and 64 GiB at its 262,144-token native context.

DeepSeek attacked the same problem with architecture. The DeepSeek-V4.1-Flash model card puts its per-token global KV cache about 4x below DeepSeek-V4-Flash and 437x below DeepSeek-V1, and DeepSeek says it needs a quarter of the HBM and an eighth of the SSD storage of the previous generation. The full breakdown is in our DeepSeek V4 guide.

---

[referencia=4c6fe5590fff18ca score=0.477]
## KV Cache Quantization (FP8)

Storing keys and values in FP8 halves the cache versus BF16, which doubles the tokens that fit in the same memory. In vLLM the setting is `kv_cache_dtype="fp8"`. Without calibration all scales default to 1.0; the vLLM docs recommend calibrating scales on a dataset with llm-compressor. Per-attention-head scales work only with the Flash Attention backend and need that calibration path.

One detail changes the accuracy picture. With the Flash Attention 3 backend and an FP8 KV cache, vLLM runs the attention math itself in FP8 and quantizes the queries as well as the stored keys and values. Run your evals on the exact backend you deploy.

## KV Cache Pricing: Cache Hits vs Misses

API providers that keep your prefix's KV cache warm skip the prefill and charge less for it. DeepSeek publishes the clearest example.

| Input type | Off-peak | Weekday peak | 
|---|---|---|
| Cache hit | $0.003 | $0.006 | 
| Cache miss | $0.15 | $0.30 | 

A cache hit costs 1/50th of a miss. For an agent that resends a 100K-token history on every turn, almost the whole input bill depends on whether the history stays byte-identical between calls. Editing an earlier message, reordering tools, or injecting a fresh timestamp turns hits back into misses.

---

[referencia=4c6fe5590fff18ca score=0.075]
For capacity planning, take an H200 with 141GB of HBM serving Mistral Small 3.2. The BF16 weights take about 48GB (24B parameters x 2 bytes), which leaves roughly 85GB for cache before activations and framework overhead. At 160 KiB per token that is about four concurrent 128K-token sequences, or about eight with an FP8 KV cache.

## PagedAttention and KV Cache Memory

Early serving systems reserved one contiguous buffer per request sized for the maximum sequence length. Most of that space sat empty, and fragmentation capped batch size. PagedAttention (Kwon et al., SOSP 2023) borrowed paging from operating systems. The KV cache lives in fixed-size blocks that a block table maps to each sequence, so memory is allocated as tokens arrive. The paper reports near-zero KV memory waste and 2-4x higher throughput than FasterTransformer and Orca at the same latency, with larger gains on longer sequences.

Blocks also make sharing cheap. Two sequences that start with the same tokens can point at the same physical blocks, which is what prefix caching builds on. PagedAttention pairs with continuous batching: freed blocks go straight to the next request in the queue.

## Prefix Caching: Reusing the KV Cache Across Requests

Prefix caching keeps the KV blocks of finished requests and reuses them when a new request starts with the same tokens. System prompts, tool definitions, and the growing history of an agent loop all repeat, so the prefill for that shared part can be skipped. In vLLM it is `enable_prefix_caching=True`.

vLLM's design doc has details most explainers skip. Each block is identified by a hash of its own tokens plus the hash of its parent block, so a block only matches when everything before it matches too. Only full blocks are cached, so a prefix that ends mid-block loses the partial block. Since v0.11 the default hash is SHA-256, replacing a scheme that was not guaranteed collision-free, and a per-request cache salt can isolate tenants that should never share cache.

The practical rule for prompts is to put stable content first and variable content last. A timestamp at the top of a system prompt changes the first block and with it every block after it. Our prompt caching guide covers how each API provider exposes this.