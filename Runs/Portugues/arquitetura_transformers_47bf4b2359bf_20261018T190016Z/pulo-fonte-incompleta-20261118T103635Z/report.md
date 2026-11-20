# Relatório de Auditoria — ChatGPT (arquitetura_transformers_47bf4b2359bf_20261018T190016Z)

**Arquivo auditado:** `answers/ChatGPT/Consolidado/arquitetura_transformers.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_47bf4b2359bf_20261018T190016Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-04T05:24:45.197954+00:00 |
| **Total de trechos citados** | 114 |
| **Tempo de processamento** | 16:10:24:29 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 34.2 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 170 marcadores, 29 distintos |
| Referências listadas | 29 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 92 | 80.7% |
| **UNSUPPORTED** | 20 | 17.5% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 2 | 1.8% |
| **TOTAL** | 114 | 100.0% |

Sobre os 112 trechos citados auditados: SUPPORTED 82,14%, UNSUPPORTED 17,85%, CONTRADICTED 0,00%.

> **25 dos 92 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 25 estão **contados dentro** dos 92 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`28` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `2` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `4` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 8.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#12` Antes do Transformer, a formulação dominante para tradução neural e outras tarefas de sequência era o modelo *sequence-… | [3] | [1] [8] [17] [6] [12] [4] [2] | — |
| `#18` LSTMs e mecanismos de gating amenizaram problemas de propagação de informação, mas não removeram essa dependência seque… | [3] | [1] [4] [6] [27] [25] [15] | — |
| `#35` Reunindo todos os pares, obtém-se \(S=QK^\top\), uma matriz \(n\times n\). | [1] | [10] [8] [18] | — |
| `#109` RAG, porém, não elimina erro factual: se o retriever selecionar documentos irrelevantes, se as fontes forem incorretas… | [14] | [28] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2651771 |
| **Média de tokens por requisição** | 23676.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/29 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | downloaded | 43 | 32 | 7 | 4 | 0 |
| [[10]](https://arxiv.org/abs/2205.14135) | downloaded | 11 | 4 | 6 | 1 | 0 |
| [[9]](https://arxiv.org/abs/2203.02155) | downloaded | 8 | 6 | 2 | 0 | 0 |
| [[6]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | downloaded | 7 | 4 | 2 | 1 | 0 |
| [[7]](https://arxiv.org/abs/2005.14165) | downloaded | 7 | 2 | 3 | 2 | 0 |
| [[14]](https://arxiv.org/abs/2005.11401) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[28]](https://arxiv.org/abs/2307.03172) | downloaded | 6 | 2 | 4 | 0 | 0 |
| [[8]](https://arxiv.org/abs/1910.10683) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[11]](https://arxiv.org/abs/2009.14794) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[12]](https://arxiv.org/abs/2004.05150) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[15]](https://arxiv.org/abs/2310.01889) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[20]](https://arxiv.org/abs/1910.02054) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[27]](https://arxiv.org/abs/2502.11089) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[3]](https://arxiv.org/abs/1409.3215) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[5]](https://arxiv.org/abs/1810.04805) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[13]](https://arxiv.org/abs/2001.04451) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[17]](https://arxiv.org/abs/2404.07143) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[21]](https://arxiv.org/abs/1909.08053) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[23]](https://arxiv.org/abs/2109.07958) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[24]](https://dl.acm.org/doi/10.1145/3442188.3445922) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[26]](https://community.owasp.org/attacks/PromptInjection) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[2]](https://arxiv.org/abs/1409.0473) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[4]](https://arxiv.org/abs/1705.03122) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[18]](https://arxiv.org/abs/2309.00071) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[22]](https://arxiv.org/abs/1811.06965) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[19]](https://arxiv.org/abs/1710.03740) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[25]](https://arxiv.org/abs/2303.08774) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[16]](https://arxiv.org/abs/2307.02486) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://docs.pytorch.org/docs/stable/amp.html) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://arxiv.org/abs/1706.03762) | #0–4, #16–17, #21–23, #25–31, #33, #36–40, #42, #44–47, #52, #57, #64, #66 | #20, #24, #35, #41, #43, #65, #112 | #6, #32, #34, #48 | `#0` We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Expe… |
| [[10]](https://arxiv.org/abs/2205.14135) | #6, #73–75 | #7, #65, #76, #110–112 | #66 | `#6` Standard attention implementations materialize the matrices S and P to HBM, which takes O(N²) memory. ... the inputs Q, K are read from HBM and the output S ∈… |
| [[9]](https://arxiv.org/abs/2203.02155) | #8, #59–61, #63, #95 | #62, #113 | — | `#8` We initialize the RLHF models from a pretrained GPT-3 model and apply supervised fine-tuning for 2 epochs on the demonstration dataset. [...] We focus on fine-… |
| [[6]](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | #8, #51, #54, #89 | #53, #59 | #5 | `#8` We demonstrate that large gains on these tasks can be realized by generative pre-training of a language model on a diverse corpus of unlabeled text, followed b… |
| [[7]](https://arxiv.org/abs/2005.14165) | #55, #89 | #5, #8, #53 | #48, #51 | `#55` we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in… |
| [[14]](https://arxiv.org/abs/2005.11401) | #106–108 | #11, #109–110 | #100 | `#107` We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed… |
| [[28]](https://arxiv.org/abs/2307.03172) | #97–98 | #10, #96, #111, #113 | — | `#97` We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answe… |
| [[8]](https://arxiv.org/abs/1910.10683) | #48, #57 | #5, #56, #58 | — | `#48` A major distinguishing factor for different architectures is the “mask” used by different attention mechanisms in the model. |
| [[11]](https://arxiv.org/abs/2009.14794) | #71–72 | #7, #76, #110 | — | `#72` using only linear (as opposed to quadratic) space and time complexity, without relying on any priors such as sparsity or low-rankness. To approximate softmax a… |
| [[12]](https://arxiv.org/abs/2004.05150) | #67–68 | #7, #110 | #76 | `#67` Longformer's attention mechanism is a drop-in replacement for the standard self-attention and combines a local windowed attention with a task motivated global… |
| [[15]](https://arxiv.org/abs/2310.01889) | #77–79 | #7, #110 | — | `#77` One line of research leverages the observation that the softmax matrix in self-attention can be computed without materializing the full matrix [24] which has l… |
| [[20]](https://arxiv.org/abs/1910.02054) | #86–87 | #9, #88 | #112 | `#86` DP replicates the entire model states across all data parallel process resulting in redundant memory consumption; [...] ZeRO-DP removes the memory state redund… |
| [[27]](https://arxiv.org/abs/2502.11089) | #80–81 | #7, #110 | #113 | `#80` We present NSA, a Natively trainable Sparse Attention mechanism that integrates algorithmic innovations with hardware-aligned optimizations to achieve efficien… |
| [[3]](https://arxiv.org/abs/1409.3215) | — | #12, #16, #18 | #1 | `#12` The idea is to use one LSTM to read the input sequence, one timestep at a time, to obtain large fixeddimensional vector representation, and then to use another… |
| [[5]](https://arxiv.org/abs/1810.04805) | #49–50 | #5 | #48 | `#49` BERT's model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017) |
| [[13]](https://arxiv.org/abs/2001.04451) | #69–70 | #7 | #76 | `#69` Approximate attention computation based on locality-sensitive hashing replaces the O( L² ) factor in attention layers with O( L log L ) and so allows operating… |
| [[17]](https://arxiv.org/abs/2404.07143) | #103–105 | #110 | — | `#103` The Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear atte… |
| [[21]](https://arxiv.org/abs/1909.08053) | #84 | #9, #88 | #112 | `#84` Distributed tensor computation is an orthogonal and more general approach that partitions a tensor operation across multiple devices to accelerate computation… |
| [[23]](https://arxiv.org/abs/2109.07958) | #91–92 | #10, #113 | — | `#91` The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer… |
| [[26]](https://community.owasp.org/attacks/PromptInjection) | — | #10, #99–100 | #113 | `#10` Prompt Injection is a novel security vulnerability that targets Large Language Models (LLMs) like ChatGPT, Bard, and others. It manipulates the model's behavio… |
| [[2]](https://arxiv.org/abs/1409.0473) | #13, #15 | #14 | — | `#13` the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder–decoder architecture |
| [[4]](https://arxiv.org/abs/1705.03122) | #19–20 | #1 | — | `#19` We introduce an architecture based entirely on convolutional neural networks. Compared to recurrent models, computations over all elements can be fully paralle… |
| [[18]](https://arxiv.org/abs/2309.00071) | #101 | #110 | #111 | `#101` We present YaRN (Yet another RoPE extensioN method), a compute-efficient method to extend the context window of such models, requiring 10x less tokens and 2.5x… |
| [[22]](https://arxiv.org/abs/1811.06965) | #85 | #9, #88 | — | `#85` An example neural network with sequential layers is partitioned across four accelerators. [...] Pipeline parallelism divides the input mini-batch into smaller… |
| [[19]](https://arxiv.org/abs/1710.03740) | #82 | #9 | — | `#82` FP16 is used for storage and arithmetic. Weights, activations and gradients are stored using in FP16, an FP32 master copy of weights is used for updates. Loss-… |
| [[25]](https://arxiv.org/abs/2303.08774) | #90 | #10 | — | `#90` Despite its capabilities, GPT-4 has similar limitations to earlier GPT models [1, 37, 38]: it is not fully reliable (e.g. can suffer from “hallucinations”) |
| [[16]](https://arxiv.org/abs/2307.02486) | #102 | — | — | `#102` we propose dilated attention, which expands the attentive field exponentially as the distance grows. LONGNET has significant advantages: 1) it has a linear com… |
| [[29]](https://docs.pytorch.org/docs/stable/amp.html) | #83 | — | — | `#83` # Automatic Mixed Precision package - torch.amp# `torch.amp` provides convenience methods for mixed precision |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://dl.acm.org/doi/10.1145/3442188.3445922 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-0`** [1]
  - Trecho: A arquitetura Transformer, apresentada por Vaswani et al. em 2017, substituiu a recorrência e as convoluções como mecanismo central de modelagem de sequências por operações de atenção, permitindo que todos os tokens de…
  - Justificativa: A evidência (o artigo 'Attention Is All You Need' de Vaswani et al.) sustenta explicitamente todos os elementos da afirmação: a autoria (Vaswani et al.), o ano (NIPS 2017), a substituição de recorrência e convoluções po…
  - Suporte veio de: [1]
  - Evidência: “We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.”
- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-1`** [1] [3] [4]
  - Trecho: Essa mudança atacou dois problemas importantes dos modelos sequenciais anteriores: a dificuldade de paralelizar RNNs, cuja computação avança passo a passo, e a dificuldade de transmitir informação por longas distâncias…
  - Justificativa: A evidência do paper do Transformer (a7468c6851652691) sustenta explicitamente os dois problemas citados: (1) a natureza sequencial das RNNs impede paralelização, e (2) em modelos convolucionais, o número de operações p…
  - Suporte veio de: [1] [4]
  - Evidência: “This inherently sequential nature precludes parallelization within training examples”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | sustenta | This inherently sequential nature precludes parallelization within training examples [...] In these models, the number… |
    | [4] | parcial | This contrasts with RNNs which maintain a hidden state of the entire past that prevents parallel computation within a s… |
    | [3] | ausente | — |

- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-2`** [1]
  - Trecho: na qual cada posição transforma sua representação em uma *query* \(Q\), uma *key* \(K\) e um *value* \(V\); produtos escalares medem compatibilidades entre queries e keys, o softmax converte os escores em pesos e a soma…
  - Justificativa: A evidência descreve explicitamente a função de atenção como mapeamento de query e pares key-value para uma saída (soma ponderada dos values), onde os pesos são calculados por uma função de compatibilidade (produtos esc…
  - Suporte veio de: [1]
  - Evidência: “An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, whe…”
  - Não coberto pela evidência: A afirmação de que cada posição 'transforma sua representação' em Q, K, V não é explicitamente declarada nessas palavras; a evidência diz que em self-attention keys, values e queries 'come from the same place' (output da camada anterior), o que sustenta a ideia mas não usa a terminologia exata de 'transforma'.
### UNSUPPORTED

- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-11`** [14]
  - Trecho: Por isso, a fronteira atual combina janelas maiores, atenção eficiente e mecanismos externos, especialmente *retrieval-augmented generation* (RAG), que complementam a memória paramétrica do modelo com documentos recuper…
  - Justificativa: A evidência sustenta a parte sobre RAG complementar a memória paramétrica com documentos recuperados, mas não menciona 'janelas maiores' nem 'atenção eficiente', que são componentes centrais da afirmação. Como partes es…
  - Suporte veio de: [14]
  - Evidência: “We endow pre-trained, parametric-memory generation models with a non-parametric memory through a general-purpose fine-tuning approach which we refer to as retrieval-augmented generation (RAG).”
  - Não coberto pela evidência: janelas maiores; atenção eficiente; fronteira atual
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-12`** [3]
  - Trecho: Antes do Transformer, a formulação dominante para tradução neural e outras tarefas de sequência era o modelo *sequence-to-sequence*: um encoder recorrente lia a entrada e a condensava em uma representação de dimensão fi…
  - Justificativa: A evidência descreve detalhadamente o modelo sequence-to-sequence com encoder-decoder usando RNN/LSTM, condensando a entrada em vetor de dimensão fixa e gerando saída token a token. No entanto, a evidência NÃO menciona…
  - Suporte veio de: [3]
  - Evidência: “The idea is to use one LSTM to read the input sequence, one timestep at a time, to obtain large fixeddimensional vector representation, and then to use another LSTM to extract the output sequence from that vector”
  - Não coberto pela evidência: A referência ao 'Transformer' e à época 'antes do Transformer' — não há menção ao Transformer na evidência; A caracterização como 'formulação dominante' — a evidência não afirma que era a abordagem dominante
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [1] [8] [17] [6] [12] [4] [2] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-14`** [2]
  - Trecho: Bahdanau, Cho e Bengio atacaram esse problema permitindo que o decoder consultasse diferentes estados do encoder em cada passo, atribuindo pesos diferenciáveis às posições de origem; essa ideia de alinhamento suave foi…
  - Justificativa: A evidência confirma que Bahdanau, Cho e Bengio propuseram um mecanismo em que o decoder consulta estados do encoder (anotações) em cada passo, com pesos diferenciáveis (soft alignment com backpropagation). No entanto,…
  - Suporte veio de: [2]
  - Evidência: “the alignment model directly computes a soft alignment, which allows the gradient of the cost function to be backpropagated through.”
  - Não coberto pela evidência: A afirmação de que o alinhamento suave foi 'uma das raízes diretas da atenção moderna' — a evidência não menciona influência histórica sobre trabalhos posteriores ou 'atenção moderna'.
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-93` — Referencia(s) citada(s) ['6f93afc00a76b64a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_47bf4b2359bf_20261018T190016Z-94` — Referencia(s) citada(s) ['6f93afc00a76b64a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.