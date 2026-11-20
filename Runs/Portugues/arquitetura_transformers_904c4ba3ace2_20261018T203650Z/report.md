# Relatório de Auditoria — Claude (arquitetura_transformers_904c4ba3ace2_20261018T203650Z)

**Arquivo auditado:** `answers/Claude/Consolidado/arquitetura_transformers.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_904c4ba3ace2_20261018T203650Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-10-18T20:48:01.907100+00:00 |
| **Total de chunks** | 92 |
| **Tempo de processamento** | 0:00:11:11 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 25.8 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 93 marcadores, 16 distintos |
| Referências listadas | 16 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Chunks | Percentual |
|---|---|---|
| **SUPPORTED** | 91 | 98.9% |
| **UNSUPPORTED** | 1 | 1.1% |
| **CONTRADICTED** | 0 | 0.0% |
| **TOTAL** | 92 | 100.0% |

Sobre as 92 afirmações auditadas: SUPPORTED 98,91%, UNSUPPORTED 1,08%, CONTRADICTED 0,00%.

> **6 dos 91 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 6 estão **contados dentro** dos 91 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`3` chunks tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `0` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

---

## 4. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 862598 |
| **Média de tokens por requisição** | 9376.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 5. Análise por Referência

- Referências sem nenhuma citação: 0/16 (0.0%)

> **Citada** = quantos trechos citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | downloaded | 40 | 40 | 0 | 0 | 0 |
| [[7]](https://arxiv.org/abs/2203.15556) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[10]](https://arxiv.org/pdf/2302.13971) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[12]](https://arxiv.org/abs/2205.14135) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[5]](https://arxiv.org/abs/2005.14165) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[6]](https://arxiv.org/abs/2001.08361) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[8]](https://arxiv.org/abs/2203.02155) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[11]](https://arxiv.org/abs/2305.13245) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[2]](https://arxiv.org/pdf/1409.0473) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[3]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[4]](https://arxiv.org/abs/1810.04805) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[13]](https://jmlr.org/papers/v23/21-0998.html) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[14]](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[16]](https://arxiv.org/abs/2312.00752v2) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[9]](https://arxiv.org/abs/2104.09864) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://huggingface.co/papers/2010.11929) | downloaded | 2 | 1 | 1 | 0 | 0 |

---

## 6. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | #0–1, #5–37, #58, #72–73, #82–83 | — | — | `#0` Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art… |
| [[7]](https://arxiv.org/abs/2203.15556) | #49–52, #85 | — | — | `#49` We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amou… |
| [[10]](https://arxiv.org/pdf/2302.13971) | #56–57, #59–60, #88 | — | — | `#56` We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. |
| [[12]](https://arxiv.org/abs/2205.14135) | #66–67, #69, #90 | #68 | — | `#66` Transformers are slow and memory-hungry on long sequences, since the time and memory complexity of self-attention are quadratic in sequence length. |
| [[5]](https://arxiv.org/abs/2005.14165) | #43–45, #86 | — | — | `#43` Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model |
| [[6]](https://arxiv.org/abs/2001.08361) | #46–48, #85 | — | — | `#46` The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of… |
| [[8]](https://arxiv.org/abs/2203.02155) | #53–55, #87 | — | — | `#53` large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. |
| [[11]](https://arxiv.org/abs/2305.13245) | #63–65, #89 | — | — | `#63` Multi-query attention reduces this overhead at the cost of decreased model capacity and quality. |
| [[2]](https://arxiv.org/pdf/1409.0473) | #2–4 | — | — | `#2` The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from whi… |
| [[3]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | #38–39, #84 | — | — | `#38` We demonstrate that large gains on these tasks can be realized by _generative pre-training_ of a language model on a diverse corpus of unlabeled text, followed… |
| [[4]](https://arxiv.org/abs/1810.04805) | #40–42 | — | — | `#40` BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. |
| [[13]](https://jmlr.org/papers/v23/21-0998.html) | #70–71, #91 | — | — | `#70` Mixture of Experts (MoE) models defy this and instead select different parameters for each incoming example. The result is a sparsely-activated model---with an… |
| [[14]](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/) | #75–76 | #74 | — | `#75` induction heads form abruptly during exactly the same window where in-context learning develops |
| [[16]](https://arxiv.org/abs/2312.00752v2) | #79–81 | — | — | `#79` Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been devel… |
| [[9]](https://arxiv.org/abs/2104.09864) | #61–62 | — | — | `#61` 83213326f5835ccc |
| [[15]](https://huggingface.co/papers/2010.11929) | #78 | #77 | — | `#78` When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 7. Exemplos Representativos por Veredito

### SUPPORTED

- **Chunk `arquitetura_transformers_904c4ba3ace2_20261018T203650Z-0`** [1]
  - Trecho: Isso incluía as LSTMs e as redes com portas (GRUs), consideradas o estado da arte em modelagem de linguagem e tradução automática.
  - Justificativa: A evidência, na seção de Introdução, afirma explicitamente que redes neurais recorrentes, em particular LSTMs e redes recorrentes com portas (gated recurrent), foram firmemente estabelecidas como estado da arte em model…
  - Suporte veio de: [1]
  - Evidência: “Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems su…”
  - Não coberto pela evidência: A sigla 'GRUs' não aparece explicitamente na evidência; a evidência menciona 'gated recurrent neural networks' (referência [7]), que corresponde ao conceito, mas o termo exato 'GRU' não é usado no texto.
- **Chunk `arquitetura_transformers_904c4ba3ace2_20261018T203650Z-1`** [1]
  - Trecho: O problema se agrava com sequências longas, porque limites de memória também restringem o agrupamento de vários exemplos em lote.
  - Justificativa: A evidência do trecho de Introdução afirma explicitamente que a natureza sequencial torna-se crítica em sequências mais longas, pois restrições de memória limitam o agrupamento (batching) entre exemplos, o que correspon…
  - Suporte veio de: [1]
  - Evidência: “This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.”
- **Chunk `arquitetura_transformers_904c4ba3ace2_20261018T203650Z-2`** [2]
  - Trecho: Os sistemas de tradução neural da época seguiam o esquema codificador–decodificador: o codificador comprimia a frase de origem num vetor de tamanho fixo, e o decodificador gerava a tradução a partir dele.
  - Justificativa: A evidência descreve explicitamente que a abordagem convencional de tradução neural da época seguia o esquema codificador–decodificador, no qual o codificador comprimia a frase de origem num vetor de tamanho fixo e o de…
  - Suporte veio de: [2]
  - Evidência: “The conventional approach to neural machine translation, called an encoder–decoder approach, encodes a whole input sentence into a fixed-length vector from which a translation will be decoded.”
### UNSUPPORTED

- **Chunk `arquitetura_transformers_904c4ba3ace2_20261018T203650Z-77`** [15]
  - Trecho: Os fragmentos são tratados como tokens, do mesmo modo que palavras.
  - Justificativa: A evidência menciona que um Transformer puro é aplicado a 'sequences of image patches' e o título metaforicamente equipara patches a palavras ('An Image is Worth 16x16 Words'), mas não afirma explicitamente que os fragm…
  - Não coberto pela evidência: Tratamento de fragmentos como 'tokens'; Equivalência explícita entre fragmentos e palavras no processamento
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference