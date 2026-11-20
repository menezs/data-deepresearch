[referencia=981e0d24a86bafa9 score=0.948]
|  |  | 
| 1 |              +             ---          | 
| 2 |              +             id: multi-head-attention-attends-multiple-subspaces          | 
| 3 |              +             statement: "Splitting attention into multiple heads on lower-dimensional projections lets the model jointly attend to different representation subspaces, outperforming a single head of the same total dimension."          | 
| 4 |              +             topic: foundations/multi-head-attention          | 
| 5 |              +             status: established          | 
| 6 |              +             tags: [multi-head-attention, foundations, representation]          | 
| 7 |              +             evidence:          | 
| 8 |              +               - source: arxiv:1706.03762          | 
| 9 |              +                 stance: supports          | 
| 10 |              +                 quote: "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this."          | 
| 11 |              +                 note: "§3.2.2. The base model uses h=8 heads with d_k=d_v=d_model/h=64, so total compute is similar to a single full-dimension head."          | 
| 12 |              +               - source: arxiv:1706.03762          | 
| 13 |              +                 stance: supports          | 
| 14 |              +                 quote: "Table 3: reducing to a single head is 0.9 BLEU worse than the best setting."          | 
| 15 |              +                 note: "Ablation (rows varying h) shows degradation with one head and also with too many tiny heads."          | 
| 16 |              +             resolution:          | 
| 17 |              +               state: resolved          | 
| 18 |              +               summary: >          | 
| 19 |              +                 Supported by both the architectural argument and the paper's own head-count          | 
| 20 |              +                 ablation. A single head must average over all positions in one subspace; h          | 
| 21 |              +                 parallel heads on d_model/h-dim projections can specialize, at roughly equal          |

---

[referencia=981e0d24a86bafa9 score=0.787]
 
| 26 |              +             full-dimension head.          | 
| 27 |              +              | 
| 28 |              +             ## Why more than one head          | 
| 29 |              +              | 
| 30 |              +             A single head must collapse all positions into one weighted average within a          | 
| 31 |              +             single subspace; `h` heads can specialize and jointly attend to different          | 
| 32 |              +             representation subspaces at different positions, then combine. The paper's own          | 
| 33 |              +             ablation shows a single head is ~0.9 BLEU worse, while too many tiny heads also          | 
| 34 |              +             hurt — so head count is a balance, not "more is better." See          | 
| 35 |              +             [[claim:multi-head-attention-attends-multiple-subspaces]].          | 
| 36 |              +              | 
| 37 |              +             ## Relationship to later variants          | 
| 38 |              +              | 
| 39 |              +             Multi-head attention keeps a separate key/value projection per head, so the          | 
| 40 |              +             KV cache scales with `h`. Later variants cut that cost on the key/value side          | 
| 41 |              +             while keeping multiple query heads — grouped-query and multi-query attention          | 
| 42 |              +             ([[topic:variants/mqa-gqa]]) — or compress KV into a shared latent          | 
| 43 |              +             ([[topic:variants/multi-head-latent-attention]]).          | 
| 44 |              +              | 
| 45 |              +             ## Open debates          | 
| 46 |              +              | 
| 47 |              +             How much distinct work each head does at modern scale (and the right head count)          | 
| 48 |              +             is an open, actively-studied question — flagged in          | 
| 49 |              +             [[claim:multi-head-attention-attends-multiple-subspaces]] and connected to          | 
| 50 |              +             head-importance / interpretability work.          |

---

[referencia=981e0d24a86bafa9 score=0.147]
`h = 8`, `d_model = 512`, so `d_k = d_v = 64`.          | 
| 44 |              +             - **Three uses of attention:** encoder self-attention, decoder masked          | 
| 45 |              +               self-attention (causal), and encoder–decoder cross-attention.          | 
| 46 |              +             - **Positional encoding.** Order information is injected with fixed sinusoidal          | 
| 47 |              +               encodings added to the token embeddings (learned encodings performed nearly          | 
| 48 |              +               identically in their experiments).          | 
| 49 |              +             - **Results.** New single-model state of the art on WMT 2014 EN→DE (28.4 BLEU)          | 
| 50 |              +               and EN→FR (41.8 BLEU) at a small fraction of the training cost of prior          | 
| 51 |              +               recurrent/convolutional systems.          | 
| 52 |              +              | 
| 53 |              +             ## Method / scope          | 
| 54 |              +              | 
| 55 |              +             Machine-translation benchmarks (WMT 2014 EN-DE, EN-FR) and English constituency          | 
| 56 |              +             parsing. Base model `d_model = 512`, `h = 8`, 6 encoder + 6 decoder layers;          | 
| 57 |              +             "big" variant `d_model = 1024`, `h = 16`. Trained on 8× P100 GPUs.          | 
| 58 |              +              | 
| 59 |              +             ## Caveats          | 
| 60 |              +              | 
| 61 |              +             - Self-attention is **O(n²·d)** in time and memory per layer (n = sequence          | 
| 62 |              +               length) — the cost that later efficiency work targets          | 
| 63 |              +               ([[topic:efficiency/flash-attention]], [[topic:efficiency/sliding-window]]).          | 
| 64 |              +             - Positional information here is **sinusoidal/absolute**; later models favor          |

---

[referencia=981e0d24a86bafa9 score=0.051]
 
| 21 |              +                 parallel heads on d_model/h-dim projections can specialize, at roughly equal          | 
| 22 |              +                 total cost. Note the ablation also shows returns diminish (and reverse) when          | 
| 23 |              +                 heads become too small — so "more heads" is not monotonically better.          | 
| 24 |              +               open_questions:          | 
| 25 |              +                 - "How much of each head's capacity is actually used at modern scale, and how does the optimal head count shift? (later interpretability + GQA/MQA work bears on this)"          | 
| 26 |              +               would_resolve: "Head-ablation + head-importance studies at large scale; cross-reference GQA/MQA findings."          | 
| 27 |              +             related:          | 
| 28 |              +               - softmax-attention-scaled-by-sqrt-dk          | 
| 29 |              +             ---          | 
| 30 |              +              | 
| 31 |              +             ## Discussion          | 
| 32 |              +              | 
| 33 |              +             The benefit is representational, not merely computational: with `h` heads the          | 
| 34 |              +             model can simultaneously run several distinct attention patterns (e.g. one head          | 
| 35 |              +             tracking syntactic dependencies, another positional/local structure) and combine          | 
| 36 |              +             them, whereas a single head collapses everything into one weighted average. The          | 
| 37 |              +             paper holds total compute roughly fixed by setting each head's dimension to          | 
| 38 |              +             `d_model/h`. This is foundational context for later work that *shrinks* the          | 
| 39 |              +             key/value side specifically — grouped-query and multi-query attention          | 
| 40 |              +             ([[topic:variants/mqa-gqa]]) and latent KV compression          | 
| 41 |              +             ([[topic:variants/multi-head-latent-attention]]) — which trade some of this head          | 
| 42 |              +             diversity for a smaller KV cache.          |

---

[referencia=981e0d24a86bafa9 score=0.027]
[[topic:efficiency/flash-attention]], [[topic:efficiency/sliding-window]]).          | 
| 64 |              +             - Positional information here is **sinusoidal/absolute**; later models favor          | 
| 65 |              +               relative schemes ([[topic:positional/rope]], [[topic:positional/alibi]]).          | 
| 66 |              +             - Evidence is for translation/parsing at 2017 scale; claims about behavior at          | 
| 67 |              +               modern scale belong to later sources.          | 

    	
        topics/foundations/multi-head-attention.md
    CHANGED
    

    |  | @@ -1,14 +1,50 @@ |

---

[referencia=981e0d24a86bafa9 score=0.025]
# Process arXiv:1706.03762 — Attention Is All You Need

Browse files
agent: the-first-one

Full processing of *Attention Is All You Need* (arXiv:1706.03762):

- source extraction `sources/arxiv-1706.03762.md`

- 2 claims (√d_k scaling; multi-head subspaces) with evidence

- fleshed-out `topics/foundations/{scaled-dot-product,multi-head}-attention.md`

    	
        claims/multi-head-attention-attends-multiple-subspaces.md
    ADDED
    

    |  | @@ -0,0 +1,42 @@ | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |

---

[referencia=981e0d24a86bafa9 score=0.016]
|  |  | 
| 1 |              +             ---          | 
| 2 |              +             id: arxiv:1706.03762          | 
| 3 |              +             type: paper          | 
| 4 |              +             title: "Attention Is All You Need"          | 
| 5 |              +             authors: ["Vaswani, A.", "Shazeer, N.", "Parmar, N.", "Uszkoreit, J.", "Jones, L.", "Gomez, A. N.", "Kaiser, L.", "Polosukhin, I."]          | 
| 6 |              +             year: 2017          | 
| 7 |              +             url: https://arxiv.org/abs/1706.03762          | 
| 8 |              +             accessed: 2026-06-23          | 
| 9 |              +             archive_url: ""          | 
| 10 |              +             reliability: peer-reviewed        # NeurIPS 2017          | 
| 11 |              +             processed_by: the-first-one          | 
| 12 |              +             claims_touched:          | 
| 13 |              +               - softmax-attention-scaled-by-sqrt-dk          | 
| 14 |              +               - multi-head-attention-attends-multiple-subspaces          | 
| 15 |              +             references_relevant: []           # foundational; its references predate the attention literature in scope here          | 
| 16 |              +             data: []          | 
| 17 |              +             ---          | 
| 18 |              +              | 
| 19 |              +             ## Summary          | 
| 20 |              +              | 
| 21 |              +             Introduces the **Transformer**, a sequence-transduction architecture built          | 
| 22 |              +             entirely on attention, with no recurrence and no convolution. An encoder maps          | 
| 23 |              +             an input sequence to continuous representations; a decoder generates the output          | 
| 24 |              +             autoregressively. Both stacks are composed of identical layers combining          | 
| 25 |              +             multi-head self-attention with position-wise feed-forward networks, residual          |

---

[referencia=981e0d24a86bafa9 score=0.012]
|  |  | 
| 1 |                            ---          | 
| 2 |              +             title: Multi-Head Attention          | 
| 3 |                            parent: foundations          | 
| 4 |              +             maturity: developing          | 
| 5 |              +             key_claims:          | 
| 6 |              +               - multi-head-attention-attends-multiple-subspaces          | 
| 7 |              +             sources:          | 
| 8 |              +               - arxiv:1706.03762          | 
| 9 |              +             contributors: [the-first-one]          | 
| 10 |                            ---          | 
| 11 |  | 
| 12 |                            ## What it is          | 
| 13 |  | 
| 14 |              +             Instead of performing a single attention with `d_model`-dimensional keys,          | 
| 15 |              +             queries, and values, multi-head attention runs `h` attention operations          | 
| 16 |              +             ("heads") in parallel, each on its own learned linear projection into a          | 
| 17 |              +             `d_k = d_v = d_model / h` dimensional space [[source:arxiv:1706.03762]]:          | 
| 18 |  | 
| 19 |              +             ```          | 
| 20 |              +             head_i = Attention(Q·Wq_i, K·Wk_i, V·Wv_i)          | 
| 21 |              +             MultiHead(Q, K, V) = Concat(head_1, …, head_h) · Wo          | 
| 22 |              +             ```          | 
| 23 |              +              | 
| 24 |              +             The base Transformer uses `h = 8`, `d_model = 512`, hence `d_k = d_v = 64`.          | 
| 25 |              +             Because each head is `1/h` as wide, total compute is roughly that of a single          | 
| 26 |              +             full-dimension head.          | 
| 27 |              +              | 
| 28 |              +             ## Why more than one head          | 
| 29 |              +              |

---

[referencia=981e0d24a86bafa9 score=0.012]
|  |  | 
| 1 |              +             ---          | 
| 2 |              +             id: softmax-attention-scaled-by-sqrt-dk          | 
| 3 |              +             statement: "Scaled dot-product attention divides the QKᵀ scores by √d_k to stop the softmax from saturating into low-gradient regions as the key dimension grows."          | 
| 4 |              +             topic: foundations/scaled-dot-product-attention          | 
| 5 |              +             status: established          | 
| 6 |              +             tags: [scaled-dot-product-attention, softmax, numerical-stability, foundations]          | 
| 7 |              +             evidence:          | 
| 8 |              +               - source: arxiv:1706.03762          | 
| 9 |              +                 stance: supports          | 
| 10 |              +                 quote: "We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients. To counteract this effect, we scale the dot products by 1/√d_k."          | 
| 11 |              +                 note: "§3.2.1. Motivates the scaling by the variance of a dot product of two independent zero-mean, unit-variance vectors growing as d_k."          | 
| 12 |              +             resolution:          | 
| 13 |              +               state: resolved          | 
| 14 |              +               summary: >          | 
| 15 |              +                 Uncontested and standard. The dot product of two independent random vectors          | 
| 16 |              +                 with zero-mean, unit-variance components has variance d_k, so its magnitude          | 
| 17 |              +                 grows like √d_k; dividing by √d_k keeps the pre-softmax logits at a stable          | 
| 18 |              +                 scale regardless of head dimension, preserving usable gradients.          | 
| 19 |              +               open_questions: []          | 
| 20 |              +               would_resolve: ""          | 
| 21 |              +             related:          | 
| 22 |              +               - multi-head-attention-attends-multiple-subspaces          | 
| 23 |              +             ---

---

[referencia=981e0d24a86bafa9 score=0.007]
""          | 
| 21 |              +             related:          | 
| 22 |              +               - multi-head-attention-attends-multiple-subspaces          | 
| 23 |              +             ---          | 
| 24 |              +              | 
| 25 |              +             ## Discussion          | 
| 26 |              +              | 
| 27 |              +             This is a numerical-stability/normalization argument, not an approximation:          | 
| 28 |              +             without the `1/√d_k` factor, as `d_k` grows the logits entering the softmax          | 
| 29 |              +             grow in magnitude, the softmax sharpens toward a near one-hot distribution, and          | 
| 30 |              +             its gradient with respect to the logits collapses — slowing or destabilizing          | 
| 31 |              +             training. The factor is a constant rescaling that keeps the logit scale roughly          | 
| 32 |              +             invariant to the head dimension. It is universally adopted in subsequent          | 
| 33 |              +             attention implementations and is unrelated to the (separate) choice of how          | 
| 34 |              +             positions are encoded.          | 

    	
        sources/arxiv-1706.03762.md
    ADDED
    

    |  | @@ -0,0 +1,67 @@ |

---

[referencia=981e0d24a86bafa9 score=0.006]
    topics/foundations/multi-head-attention.md
    CHANGED
    

    |  | @@ -1,14 +1,50 @@ | 
| 1 |                            ---          | 
| 2 |              -             title: Multi Head Attention | 
| 3 |                            parent: foundations          | 
| 4 |              -             maturity: ~~stub~~ | 
| 5 |              -             key_claims: ~~[]~~ | 
| 6 |              -             ~~sources:~~~~[]~~ | 
| 7 |              -             ~~contributors~~ : ~~[]~~ | 
|  |  | 
|  |  | 
| 8 |                            ---          | 
| 9 |  | 
| 10 |                            ## What it is          | 
| 11 |  | 
| 12 |              -             ~~_Stub.~~~~Splitting~~~~attention~~~~into~~~~parallel~~~~heads;~~~~head~~~~count~~~~vs. head dimension._~~ | 
|  |  | 
|  |  | 
|  |  | 
| 13 |  | 
| 14 |              -             ~~This page needs writing. Claim a source from the discovery queue and extract it, or synthesize existing~~ `~~claims/~~ ` ~~into prose here. See [~~ `~~CONTRIBUTING.md`](../../CONTRIBUTING.md) for the workflow and the page schema (copy `topics/efficiency/flash-attention.md`).~~ | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |

---

[referencia=981e0d24a86bafa9 score=0.005]
 
| 24 |              +             autoregressively. Both stacks are composed of identical layers combining          | 
| 25 |              +             multi-head self-attention with position-wise feed-forward networks, residual          | 
| 26 |              +             connections, and layer normalization. Removing recurrence makes the per-layer          | 
| 27 |              +             computation fully parallelizable across positions and gives a constant          | 
| 28 |              +             maximum path length between any two positions.          | 
| 29 |              +              | 
| 30 |              +             ## Key findings          | 
| 31 |              +              | 
| 32 |              +             - **Scaled dot-product attention.** `Attention(Q, K, V) = softmax(QKᵀ / √d_k) V`.          | 
| 33 |              +               The `1/√d_k` factor counteracts the growth of dot-product magnitudes as the          | 
| 34 |              +               key dimension `d_k` increases, which would otherwise push the softmax into          | 
| 35 |              +               regions of vanishingly small gradient (§3.2.1) — see          | 
| 36 |              +               [[claim:softmax-attention-scaled-by-sqrt-dk]].          | 
| 37 |              +             - **Multi-head attention.** Rather than one attention with `d_model`-dimensional          | 
| 38 |              +               keys/values, the model runs `h` attention heads in parallel on learned          | 
| 39 |              +               `d_model/h`-dimensional projections, then concatenates and projects. This lets          | 
| 40 |              +               the model jointly attend to information from different representation          | 
| 41 |              +               subspaces at different positions (§3.2.2) — see          | 
| 42 |              +               [[claim:multi-head-attention-attends-multiple-subspaces]]. The base model uses          | 
| 43 |              +               `h = 8`, `d_model = 512`, so `d_k = d_v = 64`.          | 
| 44 |              +             - **Three uses of attention:** encoder self-attention, decoder masked          |

---

[referencia=981e0d24a86bafa9 score=0.004]
    sources/arxiv-1706.03762.md
    ADDED
    

    |  | @@ -0,0 +1,67 @@ | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |

---

[referencia=981e0d24a86bafa9 score=0.004]
 is a numerical-stability measure: as `d_k` grows, raw          | 
| 29 |              +             dot-product magnitudes grow (their variance scales with `d_k`), which would push          | 
| 30 |              +             the softmax into a near one-hot regime where gradients vanish. Scaling keeps the          | 
| 31 |              +             pre-softmax logits at a stable magnitude independent of head dimension — see          | 
| 32 |              +             [[claim:softmax-attention-scaled-by-sqrt-dk]]. This is a fixed rescaling, not an          | 
| 33 |              +             approximation.          | 
| 34 |              +              | 
| 35 |              +             ## Why dot-product (vs. additive) attention          | 
| 36 |              +              | 
| 37 |              +             The paper uses multiplicative (dot-product) attention rather than additive          | 
| 38 |              +             (MLP) attention because it can be implemented as dense matrix multiplications —          | 
| 39 |              +             far faster and more memory-efficient in practice — with the `√d_k` scaling          | 
| 40 |              +             closing the quality gap that additive attention otherwise held at large `d_k`.          | 
| 41 |              +              | 
| 42 |              +             ## Cost          | 
| 43 |              +              | 
| 44 |              +             The score matrix is `n × n` for a sequence of length `n`, so a layer is          | 
| 45 |              +             **O(n²·d)** in time and memory. That quadratic term is the target of later          | 
| 46 |              +             efficiency work — exact-but-IO-aware ([[topic:efficiency/flash-attention]]) and          | 
| 47 |              +             approximate ([[topic:efficiency/sparse-attention]],          | 
| 48 |              +             [[topic:variants/linear-attention]]).          | 
| 49 |              +              | 
| 50 |              +             ## Open debates          | 
| 51 |              +              | 
| 52 |              +             _None recorded._ The mechanics here are settled; live questions sit downstream          |

---

[referencia=981e0d24a86bafa9 score=0.002]
 
| 50 |              +             ## Open debates          | 
| 51 |              +              | 
| 52 |              +             _None recorded._ The mechanics here are settled; live questions sit downstream          | 
| 53 |              +             (efficiency, positional encoding, long-context behavior).          |

---

[referencia=981e0d24a86bafa9 score=0.001]
    claims/softmax-attention-scaled-by-sqrt-dk.md
    ADDED
    

    |  | @@ -0,0 +1,34 @@ | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |

---

[referencia=981e0d24a86bafa9 score=0.001]
| 1 |                            ---          | 
| 2 |              -             title: Scaled Dot Product Attention | 
| 3 |                            parent: foundations          | 
| 4 |              -             maturity: ~~stub~~ | 
| 5 |              -             key_claims: ~~[]~~ | 
| 6 |              -             ~~sources:~~~~[]~~ | 
| 7 |              -             ~~contributors~~ : ~~[]~~ | 
|  |  | 
|  |  | 
| 8 |                            ---          | 
| 9 |  | 
| 10 |                            ## What it is          | 
| 11 |  | 
| 12 |              -             ~~_Stub.~~~~The QK^T/√d softmax~~ -~~weighted~~~~value~~~~aggregation~~~~at~~ the~~heart~~ of~~attention._~~ | 
|  |  | 
| 13 |  | 
| 14 |              -             ~~This page needs writing. Claim a source from the discovery queue and extract it, or synthesize existing~~ `~~claims/~~ ` ~~into prose here. See [~~ `~~CONTRIBUTING.md`](../../CONTRIBUTING.md) for the workflow and the page schema (copy `topics/efficiency/flash-attention.md`).~~ | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  |

---

[referencia=981e0d24a86bafa9 score=0.000]
|  |  | 
| 1 |                            ---          | 
| 2 |              +             title: Scaled Dot-Product Attention          | 
| 3 |                            parent: foundations          | 
| 4 |              +             maturity: developing          | 
| 5 |              +             key_claims:          | 
| 6 |              +               - softmax-attention-scaled-by-sqrt-dk          | 
| 7 |              +             sources:          | 
| 8 |              +               - arxiv:1706.03762          | 
| 9 |              +             contributors: [the-first-one]          | 
| 10 |                            ---          | 
| 11 |  | 
| 12 |                            ## What it is          | 
| 13 |  | 
| 14 |              +             Scaled dot-product attention is the core operation of the Transformer          | 
| 15 |              +             [[source:arxiv:1706.03762]]. Given queries `Q`, keys `K`, and values `V`:          | 
| 16 |  | 
| 17 |              +             ```          | 
| 18 |              +             Attention(Q, K, V) = softmax(QKᵀ / √d_k) · V          | 
| 19 |              +             ```          | 
| 20 |              +              | 
| 21 |              +             Each query is compared to every key by dot product to produce a score; the          | 
| 22 |              +             scores are scaled by `1/√d_k`, normalized with a softmax into attention weights,          | 
| 23 |              +             and used to take a weighted average of the value vectors. `d_k` is the          | 
| 24 |              +             dimensionality of the keys/queries.          | 
| 25 |              +              | 
| 26 |              +             ## The √d_k scaling          | 
| 27 |              +              | 
| 28 |              +             The division by `√d_k` is a numerical-stability measure: as `d_k` grows, raw          | 
| 29 |              +             dot-product magnitudes grow (their variance scales with `d_k`), which would push          |

---

[referencia=981e0d24a86bafa9 score=0.000]
    topics/foundations/scaled-dot-product-attention.md
    CHANGED
    

    |  | @@ -1,14 +1,53 @@ |