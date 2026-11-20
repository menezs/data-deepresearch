# Relatório de Auditoria — Claude (arquitetura_transformers_a069a0517859_20261114T214020Z)

**Arquivo auditado:** `answers/Ingles/Claude/Consolidado/arquitetura_transformers.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_a069a0517859_20261114T214020Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T02:13:00.926823+00:00 |
| **Total de trechos citados** | 82 |
| **Tempo de processamento** | 0:04:32:41 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 26.3 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 99 marcadores, 43 distintos |
| Referências listadas | 43 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 69 | 84.1% |
| **UNSUPPORTED** | 11 | 13.4% |
| **CONTRADICTED** | 2 | 2.4% |
| **TOTAL** | 82 | 100.0% |

Sobre os 82 trechos citados auditados: SUPPORTED 84,14%, UNSUPPORTED 13,41%, CONTRADICTED 2,43%.

> **21 dos 69 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 21 estão **contados dentro** dos 69 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`16` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `5` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `1` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 4, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#10` Yet attention was still bolted onto a recurrent network, leaving two deeper problems untouched. Gradient-based learning… | [12] [13] | [21] [1] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1504903 |
| **Média de tokens por requisição** | 18352.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/43 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | downloaded | 22 | 18 | 4 | 0 | 0 |
| [[3]](https://arxiv.org/abs/2302.13971) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[7]](https://huggingface.co/papers/2412.19437) | downloaded | 5 | 1 | 3 | 1 | 0 |
| [[2]](https://arxiv.org/abs/2005.14165) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[9]](https://www.minimax.io/news/why-did-m2-end-up-as-a-full-attention-model) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[10]](https://arxiv.org/abs/1409.0473) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[8]](https://blog.korolevalab.com/blog/2026/hybrid-attention/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[25]](https://arxiv.org/abs/2108.12409) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[28]](https://arxiv.org/abs/2203.15556) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[32]](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[4]](https://arxiv.org/abs/2205.14135) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[5]](https://arxiv.org/abs/2305.13245) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[6]](https://arxiv.org/abs/2310.06825) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[14]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[15]](https://nlp.seas.harvard.edu/annotated-transformer) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[16]](https://arxiv.org/abs/1810.04805) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[19]](https://arxiv.org/abs/1910.10683) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[21]](https://arxiv.org/abs/2002.04745) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[23]](https://arxiv.org/abs/2002.05202) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[43]](https://www.sebastianraschka.com/blog/2026/minimax-m2-technical-report.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[11]](https://arxiv.org/abs/1508.04025) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://scilit.com/publications/4988b98a344caef9bd67bf8370a931c3) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[13]](https://arxiv.org/abs/1211.5063) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[17]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[18]](https://huggingface.co/transformers/v2.5.1/model_doc/gpt.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[20]](https://arxiv.org/abs/1910.13461) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://arxiv.org/abs/1910.07467) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://arxiv.org/abs/2104.09864) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://openai.com/index/better-language-models/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[27]](https://arxiv.org/abs/2001.08361) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://arxiv.org/abs/2203.02155) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://arxiv.org/abs/1902.10186) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://arxiv.org/abs/1908.04626) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.morphllm.com/kv-cache) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://arxiv.org/abs/1911.02150) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://huggingface.co/papers/2004.05150) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://arxiv.org/abs/2101.03961) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[37]](https://arxiv.org/abs/2401.04088) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[38]](https://arxiv.org/abs/2312.00752) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://arxiv.org/abs/2305.13048) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://arxiv.org/abs/2403.19887) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://arxiv.org/abs/2504.03624) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://venturebeat.com/ai/western-qwen-ibm-wows-with-granite-4-llm-launch-and-hybrid-mamba-transformer) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | #0–1, #11, #13, #15–19, #21–29 | #12, #14, #20, #81 | — | `#0` the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder archit… |
| [[3]](https://arxiv.org/abs/2302.13971) | #36, #41, #45 | #81 | #3 | `#36` Pre-normalization [GPT3]. To improve the training stability, we normalize the input of each transformer sub-layer, instead of normalizing the output. We use th… |
| [[7]](https://huggingface.co/papers/2412.19437) | #65 | #53, #69, #78 | #3 | `#65` DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures |
| [[2]](https://arxiv.org/abs/2005.14165) | #38, #47–48 | #2 | — | `#38` We use the same model and architecture as GPT-2 [RWC<sup>+</sup> 19], including the modified initialization, pre-normalization, and reversible tokenization des… |
| [[9]](https://www.minimax.io/news/why-did-m2-end-up-as-a-full-attention-model) | #4, #60, #76 | #79 | — | `#4` the price paid became obvious at a larger scale: the model had clear deficits in complex, multi-hop reasoning tasks. |
| [[10]](https://arxiv.org/abs/1409.0473) | #5–8 | — | — | `#5` Most of the proposed neural machine translation models belong to a family of encoder–decoders |
| [[8]](https://blog.korolevalab.com/blog/2026/hybrid-attention/) | #4, #68, #75 | — | — | `#4` The first large hybrid was Jamba from AI21, in March 2024: Mamba layers with one attention layer in every eight. |
| [[25]](https://arxiv.org/abs/2108.12409) | #43–44 | #80 | — | `#43` ALiBi does not add positional embeddings to word embeddings; instead, it biases query-key attention scores with a penalty that is proportional to their distanc… |
| [[28]](https://arxiv.org/abs/2203.15556) | #50–51 | #52 | — | `#50` We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amou… |
| [[32]](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | #57–59 | — | — | `#57` Induction heads are implemented by a circuit consisting of a pair of attention heads in different layers that work together to copy or complete patterns. The f… |
| [[4]](https://arxiv.org/abs/2205.14135) | #61 | #3 | — | `#61` We propose FlashAttention, an IO-aware exact attention algorithm that uses tiling to reduce the number of memory reads/writes between GPU high bandwidth memory… |
| [[5]](https://arxiv.org/abs/2305.13245) | #64 | #3 | — | `#64` introduce grouped-query attention (GQA), a generalization of multi-query attention which uses an intermediate (more than one, less than number of query heads)… |
| [[6]](https://arxiv.org/abs/2310.06825) | #67 | #3 | — | `#67` Mistral 7B leverages grouped-query attention (GQA) [1], and sliding window attention (SWA) [6, 3]. ... At the last layer, using a window size of W = 4096, we h… |
| [[14]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | — | #12 | #30 ⚡ | `#12` The authors of the paper are Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, and Illia Polosukhin. All eig… |
| [[15]](https://nlp.seas.harvard.edu/annotated-transformer) | #18, #20 | — | — | `#18` Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention… |
| [[16]](https://arxiv.org/abs/1810.04805) | #31, #33 | — | — | `#31` BERT is designed to pretrain deep bidirectional representations [...] pushing the GLUE score to 80.5% (7.7% point absolute improvement) [...] the BERT Transfor… |
| [[19]](https://arxiv.org/abs/1910.10683) | — | #34, #80 | — | `#34` treat every text processing problem as a “text-to-text” problem |
| [[21]](https://arxiv.org/abs/2002.04745) | #37 | — | #80 ⚡ | `#37` we prove with mean field theory that at initialization, for the original-designed Post-LN Transformer, which places the layer normalization between the residua… |
| [[23]](https://arxiv.org/abs/2002.05202) | #40 | #81 | — | `#40` SwiGLU( x, W, V, b, c, β ) = Swish β ( xW + b ) ⊗ ( xV + c ) ... we omit the bias terms. ... we reduce the number of hidden units dff ... by a factor of 3 ...… |
| [[43]](https://www.sebastianraschka.com/blog/2026/minimax-m2-technical-report.html) | #77 | #78 | — | `#77` The flagship M2 is a 62-layer decoder-only transformer [...] MiniMax tested a hybrid sliding-window setup and ultimately retained full attention in every layer… |
| [[11]](https://arxiv.org/abs/1508.04025) | #9 | — | — | `#9` The former approach resembles the model of (Bahdanau et al., 2015) but is simpler architecturally. |
| [[13]](https://arxiv.org/abs/1211.5063) | — | #10 | — | `#10` There are two widely known issues with properly training Recurrent Neural Networks, the _vanishing_ and the _exploding_ gradient problems detailed in Bengio _e… |
| [[17]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | #32 | — | — | `#32` We trained a 12-layer decoder-only transformer with masked self-attention heads (768 dimensional states and 12 attention heads). [...] We used learned position… |
| [[18]](https://huggingface.co/transformers/v2.5.1/model_doc/gpt.html) | — | #32 | — | `#32` It's a causal (unidirectional) transformer pre-trained using language modeling on a large corpus will long range dependencies, the Toronto Book Corpus. |
| [[20]](https://arxiv.org/abs/1910.13461) | #35 | — | — | `#35` It is implemented as a sequence-to-sequence model with a bidirectional encoder over corrupted text and a left-to-right autoregressive decoder. [...] can be see… |
| [[22]](https://arxiv.org/abs/1910.07467) | #39 | — | — | `#39` RMSNorm simplifies LayerNorm by totally removing the mean statistic in Eq. (3) at the cost of sacrificing the invariance that mean normalization affords. [...]… |
| [[24]](https://arxiv.org/abs/2104.09864) | #42 | — | — | `#42` simply rotate the affine-transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind Rotary P… |
| [[26]](https://openai.com/index/better-language-models/) | #46 | — | — | `#46` GPT‑2 is a large transformer-based language model with 1.5 billion parameters, trained on a dataset of 8 million web pages. GPT‑2 is trained with a simple obje… |
| [[27]](https://arxiv.org/abs/2001.08361) | #49 | — | — | `#49` The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of… |
| [[29]](https://arxiv.org/abs/2203.02155) | #54 | — | — | `#54` Figure 2: A diagram illustrating the three steps of our method: (1) supervised fine-tuning (SFT), (2) reward model (RM) training, and (3) reinforcement learnin… |
| [[30]](https://arxiv.org/abs/1902.10186) | #55 | — | — | `#55` learned attention weights are frequently uncorrelated with gradient-based measures of feature importance, and one can identify very different attention distrib… |
| [[31]](https://arxiv.org/abs/1908.04626) | #56 | — | — | `#56` If we accept the Rudin and Riedl definitions of explainability as providing a _plausible_ , but not necessarily _faithful_ rationale for model prediction, then… |
| [[33]](https://www.morphllm.com/kv-cache) | #62 | — | — | `#62` The stored attention keys and values for every token an LLM has processed, kept so each decoding step only computes the new token's keys and values. ... 2 x nu… |
| [[34]](https://arxiv.org/abs/1911.02150) | #63 | — | — | `#63` Noam Shazeer Google noam@google.com November 7, 2019 ##### **Abstract** Multi-head attention layers, as used in the Transformer neural sequence model, are a po… |
| [[35]](https://huggingface.co/papers/2004.05150) | #66 | — | — | `#66` Longformer's attention mechanism is a drop-in replacement for the standard self-attention and combines a local windowed attention with a task motivated global… |
| [[36]](https://arxiv.org/abs/2101.03961) | — | #69 | — | `#69` up to 7x increases in pre-training speed with the same computational resources |
| [[37]](https://arxiv.org/abs/2401.04088) | — | #69 | — | `#69` each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts to process the current state |
| [[38]](https://arxiv.org/abs/2312.00752) | #70 | — | — | `#70` We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the… |
| [[39]](https://arxiv.org/abs/2305.13048) | #71 | — | — | `#71` combines the efficient parallelizable training of Transformers with the efficient inference of RNNs. Our approach leverages a linear attention mechanism and al… |
| [[40]](https://arxiv.org/abs/2403.19887) | #72 | — | — | `#72` Jamba, a new base large language model based on a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture [...] fits in a single 80GB GPU [...] st… |
| [[41]](https://arxiv.org/abs/2504.03624) | #73 | — | — | `#73` we replace the majority of self-attention layers in the common Transformer model architecture with Mamba layers that perform constant computation and require c… |
| [[42]](https://venturebeat.com/ai/western-qwen-ibm-wows-with-granite-4-llm-launch-and-hybrid-mamba-transformer) | #74 | — | — | `#74` IBM reports that the hybrid Mamba-transformer design can cut RAM requirements by more than 70% (!!!) in production environments |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://scilit.com/publications/4988b98a344caef9bd67bf8370a931c3 — http_error — barreira de acesso (http_error): Reference #18.2d290c17.1794692484.35e040e8 https://errors.edgesuite.net/18.2d290c17.1794692484.35e040e8

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-0`** [1]
  - Trecho: The Transformer's central idea is that a sequence can be modeled entirely by letting each token compute a softmax-weighted mix of other tokens' representations, softmax(QK^T / sqrt(d_k)) V, with no recurrence or convolu…
  - Justificativa: A evidência sustenta todas as partes essenciais da afirmação: (1) o Transformer dispensa recorrência e convolução inteiramente; (2) baseia-se inteiramente em autoatenção (self-attention), na qual cada posição calcula um…
  - Suporte veio de: [1]
  - Evidência: “we propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-1`** [1]
  - Trecho: Introduced in 2017 for machine translation, the design mattered most for what it unlocked: a constant-length path between any two tokens and training that parallelizes across a whole sequence.
  - Justificativa: A evidência (o artigo 'Attention Is All You Need') sustenta os elementos factuais da afirmação: (1) foi apresentado no NIPS 2017; (2) aplicado a tarefas de tradução automática (WMT 2014 EN-DE e EN-FR); (3) a self-attent…
  - Suporte veio de: [1]
  - Evidência: “31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.”
  - Não coberto pela evidência: A expressão 'the design mattered most for what it unlocked' é interpretativa/editorial e não corresponde a uma afirmação literal no texto — embora os factos subjacentes estejam sustentados.
- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-4`** [8] [9]
  - Trecho: The most serious challengers, state-space and linear-recurrent models, have largely been absorbed into hybrids that still keep some full-attention layers, and at least one lab reverted to full attention after a hybrid u…
  - Justificativa: A evidência sustenta ambas as partes da afirmação: (1) modelos state-space (Mamba) e lineares-recorrentes (DeltaNet/Gated DeltaNet) foram absorvidos em híbridos que mantêm camadas de atenção completa (Jamba, Nemotron-H,…
  - Suporte veio de: [8] [9]
  - Evidência: “The first large hybrid was Jamba from AI21, in March 2024: Mamba layers with one attention layer in every eight.”
  - Não coberto pela evidência: A expressão 'most serious challengers' é uma caracterização não explicitamente feita na evidência, embora seja inferível pelo contexto de que esses são os principais modelos alternativos descritos.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [8] | sustenta | The first large hybrid was Jamba from AI21, in March 2024: Mamba layers with one attention layer in every eight. |
    | [9] | sustenta | the price paid became obvious at a larger scale: the model had clear deficits in complex, multi-hop reasoning tasks. |

### UNSUPPORTED

- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-2`** [2]
  - Trecho: OpenAI's GPT line took the decoder half, trained it to predict the next token on ever larger corpora, and showed with GPT-3 that a 175-billion-parameter model could perform new tasks from text prompts alone, without gra…
  - Justificativa: A evidência confirma que GPT-3 tem 175 bilhões de parâmetros, é um modelo autoregressivo, e que realiza tarefas via prompts de texto sem gradient updates ou fine-tuning. Porém, a evidência NÃO menciona que a linha GPT '…
  - Suporte veio de: [2]
  - Evidência: “Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is…”
  - Não coberto pela evidência: A linha GPT 'pegou a metade decoder' (decoder half) do Transformer — não há menção a 'decoder' na evidência; Treinar para 'prever o próximo token' (next token prediction) — não explicitamente afirmado, apenas 'autoregressive' é mencionado; Progressão de 'corpora cada vez maiores' (ever larger corpora) ao longo da linha GPT — não descrito como progressão histórica na evidência
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-3`** [3] [4] [5] [6] [7]
  - Trecho: Nine years on, the residual skeleton of the original block survives, though nearly every component around attention has been replaced and attention itself has been made cheaper through IO-aware kernels, shared key-value…
  - Justificativa: A afirmacao e uma sintese narrativa ampla sobre a evolucao da arquitetura Transformer em nove anos, afirmando que 'quase todos os componentes ao redor da atencao foram substituidos' e que a atencao ficou mais barata via…
  - Suporte veio de: [4] [5] [6]
  - Evidência: “We argue that a missing principle is making attention algorithms _IO-aware_ [1]—that is, carefully accounting for reads and writes to different levels of fast and slow memory”
  - Não coberto pela evidência: 'Nine years on' — nenhuma data ou periodo de nove anos e mencionado na evidencia; 'the residual skeleton of the original block survives' — a evidencia nao descreve a estrutura residual do bloco original ou sua sobrevivencia; 'nearly every component around attention has been replaced' — a evidencia nao afirma que componentes ao redor da atencao foram substituidos
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | ausente | — |
    | [4] | parcial | We argue that a missing principle is making attention algorithms _IOaware_ |
    | [5] | parcial | Flashattention: Fast and memory-efficient exact attention with io-awareness |
    | [6] | parcial | Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to… |
    | [7] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-10`** [12] [13]
  - Trecho: Yet attention was still bolted onto a recurrent network, leaving two deeper problems untouched. Gradient-based learning becomes increasingly difficult as the span of the dependencies to be captured grows, a difficulty f…
  - Justificativa: A evidência sustenta partes específicas da afirmação: a frase 'two widely known issues' aparece literalmente no abstract, e a formalização em 1994 é referenciada como 'Bengio et al. (1994)'. No entanto, a afirmação cont…
  - Suporte veio de: [13]
  - Evidência: “There are two widely known issues with properly training Recurrent Neural Networks, the _vanishing_ and the _exploding_ gradient problems detailed in Bengio _et al._ (1994).”
  - Não coberto pela evidência: attention was still bolted onto a recurrent network; leaving two deeper problems untouched; in 2012 (data exata não explicitamente confirmada na evidência)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [13] | parcial | There are two widely known issues with properly training Recurrent Neural Networks, the _vanishing_ and the _exploding_… |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [21] [1] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-30`** [14]
  - Trecho: According to Wikipedia, the paper had been cited more than 250,000 times as of 2026, placing it among the ten most-cited papers of the 21st century.
  - Justificativa: A evidência afirma que o paper foi citado mais de 150.000 vezes até 2026, enquanto o trecho afirma mais de 250.000 vezes. Há conflito direto no número de citações. Os demais elementos (top dez mais citados do século XXI…
  - Evidência: “As of 2026,[update] the paper has been cited more than 150,000 times, placing it among the top ten most-cited papers of the 21st century.”
  - Não coberto pela evidência: Número de citações: o trecho afirma mais de 250.000, mas a evidência diz mais de 150.000.
- **Trecho citado `arquitetura_transformers_a069a0517859_20261114T214020Z-80`** [25] [21] [19]
  - Trecho: The explicit hopes of 2017 fared poorly: sinusoidal encodings did not extrapolate, post-LN needed the warmup that pre-LN later made optional, and T5 found encoder-decoder models stronger than decoder-only ones in a cont…
  - Justificativa: A afirmacao tem tres partes: (1) sinusoidal encodings nao extrapolam — sustentado pela evidencia; (2) T5 encontrou encoder-decoder mais fortes que decoder-only — sustentado pela evidencia; (3) post-LN precisava de warmu…
  - Suporte veio de: [25] [21] [19]
  - Evidência: “We show for the first time that the sinusoidal position method, which technically should be able to extrapolate, in practice has very limited extrapolation capabilities.”
  - Não coberto pela evidência: A afirmacao de que pre-LN tornou o warmup 'opcional' — a evidencia afirma o contrario, que o warmup ainda permanece nos pipelines do Pre-LN.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [25] | parcial | We show for the first time that the sinusoidal position method, which technically should be able to extrapolate, in pra… |
    | [19] | parcial | For all tasks, the encoder-decoder architecture with the denoising objective performed best. / the shared parameter enc… |
    | [21] | contradiz | a learning rate warm-up stage for the Post-LN Transformer seems critical / The PreLN Transformer has been proposed in s… |
