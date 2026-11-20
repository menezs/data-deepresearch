# Relatório de Auditoria — ChatGPT (arquitetura_transformers_3bbf3997413c_20261115T044208Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/Consolidado/arquitetura_transformers.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_3bbf3997413c_20261115T044208Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-15T05:18:22.867548+00:00 |
| **Total de trechos citados** | 104 |
| **Tempo de processamento** | 0:00:36:15 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 26.9 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 128 marcadores, 19 distintos |
| Referências listadas | 19 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 78 | 75.0% |
| **UNSUPPORTED** | 24 | 23.1% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 2 | 1.9% |
| **TOTAL** | 104 | 100.0% |

Sobre os 102 trechos citados auditados: SUPPORTED 76,47%, UNSUPPORTED 23,52%, CONTRADICTED 0,00%.

> **26 dos 78 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 26 estão **contados dentro** dos 78 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`38` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `8` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `14` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `7` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 12, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#4` The original Transformer was not itself a “large language model” in the contemporary sense, but its components became t… | [1] | [3] [13] [9] [8] [5] [12] [7] [2] | — |
| `#16` Softmax converts these scores into nonnegative weights that sum to one across the attended positions, and multiplicatio… | [1] | [14] [8] [7] [2] [13] [3] [5] | — |
| `#39` This causal constraint is what makes a decoder-only Transformer a valid autoregressive model: the probability of a toke… | [2] | [15] [12] [1] [16] [13] [3] [5] [14] | — |
| `#40` Before any of this computation occurs, raw text must be converted into discrete token identifiers. | [10] | [9] [2] [3] [11] [5] [7] [16] | — |
| `#43` SentencePiece later provided language-independent BPE and unigram tokenization that can train directly on raw text with… | [11] | [10] [13] [9] [2] [5] | — |
| `#81` Another path to efficiency is conditional computation. | [17] | [1] [5] [12] [14] [9] [8] [2] [7] | — |
| `#91` A second limitation is that the language-modeling objective is fundamentally predictive rather than truth-verifying. | [18] | [5] [6] [3] [13] [12] [9] [2] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2505249 |
| **Média de tokens por requisição** | 24561.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/19 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | downloaded | 39 | 26 | 9 | 4 | 0 |
| [[2]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | downloaded | 8 | 3 | 3 | 2 | 0 |
| [[7]](https://arxiv.org/abs/2205.14135) | downloaded | 8 | 7 | 1 | 0 | 0 |
| [[3]](https://arxiv.org/abs/1810.04805) | downloaded | 7 | 4 | 3 | 0 | 0 |
| [[4]](https://www.jmlr.org/papers/v21/20-074.html) | downloaded | 7 | 1 | 1 | 5 | 0 |
| [[5]](https://arxiv.org/abs/2005.14165) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[6]](https://arxiv.org/abs/2203.02155) | downloaded | 6 | 4 | 1 | 1 | 0 |
| [[12]](https://arxiv.org/abs/2001.08361) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[13]](https://arxiv.org/abs/2203.15556) | downloaded | 6 | 4 | 1 | 1 | 0 |
| [[10]](https://arxiv.org/abs/1508.07909) | downloaded | 5 | 1 | 3 | 1 | 0 |
| [[14]](https://arxiv.org/abs/1911.02150) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[17]](https://www.jmlr.org/papers/v23/21-0998.html) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[15]](https://arxiv.org/abs/2305.13245) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[16]](https://proceedings.mlr.press/v202/leviathan23a.html) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[9]](https://arxiv.org/abs/2302.13971) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[18]](https://aclanthology.org/2022.acl-long.229/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[19]](https://doi.org/10.1145/3442188.3445922) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[8]](https://arxiv.org/abs/2104.09864) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[11]](https://aclanthology.org/D18-2012/) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | #0–3, #9, #12–15, #17–21, #24, #26, #28–32, #36–38, #44, #54 | #16, #22–23, #27, #46–47, #85, #100, #102 | #4, #8, #11, #99 | `#0` We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. |
| [[2]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | #5, #51, #57 | #10, #45, #52 | #39, #86 | `#5` we use a multi-layer Transformer decoder [34] for the language model [...] generative pre-training of a language model on a diverse corpus of unlabeled text, f… |
| [[7]](https://arxiv.org/abs/2205.14135) | #25, #74–77, #88–89 | #101 | — | `#25` the self-attention module at their heart has time and memory complexity quadratic in sequence length |
| [[3]](https://arxiv.org/abs/1810.04805) | #48–50, #57 | #6, #47, #86 | — | `#48` BERT's model architecture is a multi-layer bidirectional Transformer encoder [...] BERT is designed to pretrain deep bidirectional representations from unlabel… |
| [[4]](https://www.jmlr.org/papers/v21/20-074.html) | #55 | #6 | #10, #47, #56–57, #86 | `#55` introducing a unified framework that converts all text-based language problems into a text-to-text format. Our systematic study compares pre-training objective… |
| [[5]](https://arxiv.org/abs/2005.14165) | #53, #97 | #52, #103 | #98, #7 (s/ aval.) | `#53` we train GPT-3, an autoregressive language model with 175 billion parameters [...] For all tasks, GPT-3 is applied without any gradient updates or fine-tuning,… |
| [[6]](https://arxiv.org/abs/2203.02155) | #58–60, #94 | #10 | #103 | `#58` By default, language models optimize the next word prediction objective, which is only a proxy for what we want these models to do. |
| [[12]](https://arxiv.org/abs/2001.08361) | #61–63 | #99–100, #103 | — | `#61` Performance depends strongly on scale, weakly on model shape: Model performance depends most strongly on scale, which consists of three factors: the number of… |
| [[13]](https://arxiv.org/abs/2203.15556) | #64–67 | #101 | #103 | `#64` We hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved… |
| [[10]](https://arxiv.org/abs/1508.07909) | #42 | #41, #46, #100 | #40 | `#42` We adapt byte pair encoding (BPE) (Gage, 1994), a compression algorithm, to the task of word segmentation. BPE allows for the representation of an open vocabul… |
| [[14]](https://arxiv.org/abs/1911.02150) | #68–71, #90 | — | — | `#68` While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralle… |
| [[17]](https://www.jmlr.org/papers/v23/21-0998.html) | #82–83 | #84, #101 | #81 | `#82` Mixture of Experts (MoE) models defy this and instead select different parameters for each incoming example. The result is a sparsely-activated model---with an… |
| [[15]](https://arxiv.org/abs/2305.13245) | #72–73, #90 | #101 | — | `#72` Grouped-query attention divides query heads into _G groups_ , each of which shares a single key head and value head. [...] grouped-query attention (GQA), a gen… |
| [[16]](https://proceedings.mlr.press/v202/leviathan23a.html) | #78–80 | #101 | — | `#78` using speculative execution and a novel sampling method, we can make exact decoding from the large models faster, by running them in parallel on the outputs of… |
| [[9]](https://arxiv.org/abs/2302.13971) | #85 | #35, #87 | — | `#85` Following recent work on large language models, our network is based on the transformer architecture (Vaswani et al., 2017). We leverage various improvements t… |
| [[18]](https://aclanthology.org/2022.acl-long.229/) | #92–93 | #91 | — | `#92` Models generated many false answers that mimic popular misconceptions and have the potential to deceive humans. The largest models were generally the least tru… |
| [[8]](https://arxiv.org/abs/2104.09864) | #33–34 | — | — | `#33` Later work Raffel et al. [2020], He et al. [2020], Ke et al. [2020], Huang et al. [2020] followed these settings by only encoding the relative position informa… |
| [[11]](https://aclanthology.org/D18-2012/) | — | #43 | — | `#43` SentencePiece, a language-independent subword tokenizer and detokenizer |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://doi.org/10.1145/3442188.3445922 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-0`** [1]
  - Trecho: The Transformer is the neural-network architecture that made modern large language models technically practical by replacing recurrent sequence processing with layers built primarily around attention, feed-forward trans…
  - Justificativa: A janela descreve explicitamente o Transformer como arquitetura que dispensa recorrência e convoluções, baseando-se em atenção, feed-forward, conexões residuais e normalização, e destaca ganhos de paralelização e reduçã…
  - Suporte veio de: [1]
  - Evidência: “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
  - Verificação: reclassificado para SUPPORTED na etapa `full_doc_scan` (baseline dizia: "A evidência descreve detalhadamente a arquitetura do Transformer, confirmando que ela substitui processamento recorrente por atenção, feed-…") — cascata: baseline → context_expansion → full_doc_scan
- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-1`** [1]
  - Trecho: Introduced by Vaswani and colleagues in *Attention Is All You Need* in 2017, the original Transformer was developed for neural machine translation and used an encoder-decoder design in which both sides were composed of…
  - Justificativa: A evidência sustenta todas as partes essenciais da afirmação: o título do artigo ('Attention Is All You Need'), o primeiro autor (Ashish Vaswani), o ano (NIPS 2017), a finalidade de tradução automática (machine translat…
  - Suporte veio de: [1]
  - Evidência: “# **Attention Is All You Need** **Ashish Vaswani**”
- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-2`** [1]
  - Trecho: Its key departure from recurrent neural networks was that relationships among tokens could be computed in parallel rather than requiring a hidden state to propagate sequentially from one position to the next.
  - Justificativa: A evidência descreve explicitamente que modelos recorrentes geram estados ocultos sequencialmente (ht em função de ht-1), o que impede paralelização, enquanto o Transformer abandona a recorrência e permite paralelização…
  - Suporte veio de: [1]
  - Evidência: “Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states ht , as a functi…”
### UNSUPPORTED

- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-4`** [1]
  - Trecho: The original Transformer was not itself a “large language model” in the contemporary sense, but its components became the substrate from which the dominant families of pretrained language models developed.
  - Justificativa: A evidência é o artigo original do Transformer ('Attention Is All You Need'), que descreve a arquitetura e seus resultados em tradução automática e parsing. Embora o artigo confirme que o Transformer é um modelo de tran…
  - Não coberto pela evidência: A afirmação de que o Transformer original não era um 'large language model' no sentido contemporâneo; A afirmação de que seus componentes se tornaram o substrato para famílias dominantes de modelos de linguagem pré-treinados
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [3] [13] [9] [8] [5] [12] [7] [2] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-6`** [3] [4]
  - Trecho: BERT subsequently showed the complementary strength of a bidirectional Transformer encoder trained with masked-language-model objectives, while T5 explored encoder-decoder pretraining under a unified text-to-text framew…
  - Justificativa: A parte sobre BERT é amplamente sustentada pela evidência (Transformer encoder bidirecional com masked LM). A parte sobre T5 é parcialmente sustentada: o abstract confirma a 'unified text-to-text framework', mas não men…
  - Suporte veio de: [3] [4]
  - Evidência: “BERT's model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017)”
  - Não coberto pela evidência: T5 'encoder-decoder pretraining' — a evidência não menciona explicitamente 'encoder-decoder'; BERT 'complementary strength' — a evidência mostra vantagens do BERT mas não usa o termo 'complementary'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | BERT's model architecture is a multi-layer bidirectional Transformer encoder |
    | [4] | parcial | we introduce a unified framework that converts all text-based language problems into a text-to-text format |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_3bbf3997413c_20261115T044208Z-8`** [1]
  - Trecho: The modern importance of the Transformer therefore comes from more than the attention mechanism alone.
  - Justificativa: A evidência é o artigo original 'Attention Is All You Need', que descreve a arquitetura do Transformer e seus componentes. Embora a arquitetura inclua outros elementos além da atenção (redes feed-forward, conexões resid…
  - Não coberto pela evidência: importância moderna do Transformer; a afirmação de que a importância vem de 'mais do que o mecanismo de atenção sozinho'
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `arquitetura_transformers_3bbf3997413c_20261115T044208Z-95` — Referencia(s) citada(s) ['5d21dc0cbc3014c2'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_3bbf3997413c_20261115T044208Z-96` — Referencia(s) citada(s) ['5d21dc0cbc3014c2'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.