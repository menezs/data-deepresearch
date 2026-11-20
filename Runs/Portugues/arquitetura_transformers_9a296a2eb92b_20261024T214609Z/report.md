# Relatório de Auditoria — Gemini (arquitetura_transformers_9a296a2eb92b_20261024T214609Z)

**Arquivo auditado:** `answers/Gemini/Consolidado/arquitetura_transformers.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_9a296a2eb92b_20261024T214609Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-04T05:57:23.128249+00:00 |
| **Total de trechos citados** | 124 |
| **Tempo de processamento** | 10:08:11:14 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3153.8 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-10-24 21:47:20+00:00 |
| Citações no corpo | 124 marcadores, 16 distintos |
| Referências listadas | 29 (13 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 45 | 36.3% |
| **UNSUPPORTED** | 43 | 34.7% |
| **CONTRADICTED** | 1 | 0.8% |
| **SKIPPED** | 35 | 28.2% |
| **TOTAL** | 124 | 100.0% |

Sobre os 89 trechos citados auditados: SUPPORTED 50,56%, UNSUPPORTED 48,31%, CONTRADICTED 1,12%.

> **25 dos 45 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 25 estão **contados dentro** dos 45 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`46` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `15` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `3` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `16` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2, revisao_manual = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#19` O produto matricial calcula a afinidade não normalizada entre cada par de tokens na sequência. | [2] | [6] [4] [5] [10] [21] [14] [9] [3] | — |
| `#23` A função Softmax é aplicada de forma posicional ao longo das linhas da matriz de afinidade, gerando uma distribuição de… | [5] | [4] [7] [8] [21] [14] [22] [20] [6] | — |
| `#24` O resultado dessa ponderação é multiplicado pela matriz de valores , produzindo uma representação contextualizada em qu… | [2] | [10] [6] [4] [3] [5] [7] [9] [8] [21] [14] | — |
| `#26` No trabalho original, definiu-se e , mantendo o custo computacional total equivalente ao de uma atenção de cabeça única… | [2] | [5] [4] [21] [14] [7] | — |
| `#30` A arquitetura original do Transformer é constituída por uma estrutura Encoder-Decoder composta pelo empilhamento de blo… | [2] | [6] [5] [4] [3] [10] [9] | — |
| `#32` Cada camada do codificador contém duas subcamadas principais: | [2] | [21] [14] [9] [5] [6] [4] | — |
| `#39` Cada camada do decodificador é composta por três subcamadas: | [3] | [5] [4] [21] [14] [9] | — |
| `#45` Para injetar a ordem sequencial das palavras na rede, torna-se estritamente necessário adicionar informações posicionai… | [2] | [5] [4] [8] [3] [10] [16] [7] [6] | — |
| `#48` A escolha dessas funções trigonométricas fundamentou-se na hipótese de que permitiriam ao modelo interpolar posições re… | [2] | [5] [27] [26] [7] [28] [25] [9] | — |
| `#52` Dimensão Chave/Valor () 64 64 Escala individual de cada cabeça | [2] | [6] [4] [5] [7] [21] [14] [3] | — |
| `#53` Dimensão FFN () 2048 4096 Capacidade de transformação não linear | [6] | [4] [5] [21] [14] | — |
| `#57` (2018). | [8] | [10] [18] [28] [25] [9] [26] [27] | — |
| `#59` Masked Language Modeling (MLM): Uma porcentagem (15%) dos tokens de entrada é aleatoriamente mascarada com um token esp… | [8] | [10] [9] [28] [26] [27] [25] [6] [21] [14] | — |
| `#78` Em vez de somar um vetor de posição aos embeddings de entrada, o RoPE codifica a informação posicional multiplicando os… | [16] | [19] [5] [2] [3] [7] [4] [6] [8] [9] [10] | — |
| `#79` Expandindo essa rotação para subespaços 2D ao longo de toda a dimensão do vetor de atenção , o produto escalar entre um… | [16] | [4] [22] [7] [6] [19] [5] [2] | — |
| `#96` O processo tradicional para transformar um modelo pré-treinado em um assistente funcional envolvia a Ajustagem Fina Sup… | [23] | [28] [25] [26] [27] [10] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1688605 |
| **Média de tokens por requisição** | 18973.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 13/29 (44.8%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | downloaded | 23 | 4 | 10 | 9 | 0 |
| [[1]](https://scispace.com/papers/attention-is-all-you-need-1hodz0wcqb) | blocked | 18 | 0 | 0 | 0 | 18 |
| [[3]](https://www.alphaxiv.org/abs/1706.03762) | downloaded | 13 | 7 | 4 | 2 | 0 |
| [[14]](https://3dvar.com/Dao2022FlashAttention.pdf) | downloaded | 11 | 9 | 2 | 0 | 0 |
| [[5]](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf) | downloaded | 10 | 8 | 1 | 1 | 0 |
| [[23]](https://medium.com/@EleventhHourEnthusiast/direct-preference-optimization-your-language-model-is-secretly-a-reward-model-5b8f44cb9b9b) | downloaded | 10 | 4 | 4 | 2 | 0 |
| [[8]](https://ysu1989.github.io/courses/au20/cse5539/BERT.pdf) | downloaded | 9 | 6 | 2 | 1 | 0 |
| [[24]](https://www.researchgate.net/publication/371136760_Direct_Preference_Optimization_Your_Language_Model_is_Secretly_a_Reward_Model) | error | 9 | 0 | 0 | 0 | 9 |
| [[15]](https://openreview.net/pdf?id=H4DqfPSibmx) | blocked | 6 | 0 | 0 | 0 | 6 |
| [[16]](https://huggingface.co/papers/2104.09864) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[22]](https://github.com/dao-ailab/flash-attention) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[6]](https://towardsdatascience.com/paper-walkthrough-attention-is-all-you-need-80399cdc59e1/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[9]](http://mlg.postech.ac.kr/~jtkim/courses/2022-spring-trends-in-ml/materials/05_bert.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[13]](https://scispace.com/papers/bert-pre-training-of-deep-bidirectional-transformers-for-3mez6kncl2) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[20]](https://shreyansh26.github.io/post/2023-03-26_flash-attention/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://papers.baulab.info/papers/also/Rafailov-2023.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[4]](https://arxiv.org/abs/1706.03762) | downloaded | 0 · nunca citada | — | — | — | — |
| [[7]](https://jkk.name/reading-notes/old-blog/2017-10-20_onlyattention/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[10]](https://aclanthology.org/N19-1423.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[11]](https://www.researchgate.net/publication/328230984_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Language_Understanding) | error | 0 · nunca citada | — | — | — | — |
| [[12]](https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992) | blocked | 0 · nunca citada | — | — | — | — |
| [[17]](https://www.researchgate.net/publication/351019664_RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding) | error | 0 · nunca citada | — | — | — | — |
| [[18]](https://spaces.ac.cn/me.html/comment-page-10) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://velog.io/@lyoonji/%ED%88%AC%EB%B9%85%EC%8A%A4-4%EC%A3%BC%EC%B0%A8-%EC%A0%95%EA%B7%9C%EC%84%B8%EC%85%98-TimeSeries) | downloaded | 0 · nunca citada | — | — | — | — |
| [[21]](https://arxiv.org/abs/2205.14135) | downloaded | 0 · nunca citada | — | — | — | — |
| [[25]](https://arxiv.org/html/2305.18290v3) | downloaded | 0 · nunca citada | — | — | — | — |
| [[27]](https://arxiv.org/abs/2305.18290) | downloaded | 0 · nunca citada | — | — | — | — |
| [[28]](https://arxiv.org/html/2305.18290v1) | downloaded | 0 · nunca citada | — | — | — | — |
| [[29]](https://huggingface.co/papers/2305.18290) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | #18, #38, #46–47 | #16, #24, #30, #45, #48, #51–52, #67, #74, #123 | #19, #26, #32, #37, #50, #66, #72, #76, #15 ⚡ | `#18` The paper described the scaled dot-product attention as follows: |
| [[3]](https://www.alphaxiv.org/abs/1706.03762) | #27, #31, #33, #40, #42, #44, #117 | #29, #49, #55, #65 | #39, #64 | `#27` A self-attention layer uses a constant number of sequential operations across sequence positions, while a recurrent layer needs a number that grows with sequen… |
| [[14]](https://3dvar.com/Dao2022FlashAttention.pdf) | #81, #85, #90–93, #115, #120–121 | #75, #94 | — | `#81` the time and memory complexity of self-attention are quadratic in sequence length |
| [[5]](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf) | #17, #20–22, #34–35, #41, #43 | #23 | #25 | `#17` we found it beneficial to linearly project the queries, keys and values _h_ times with different, learned linear projections to _dk_ , _dk_ and _dv_ dimensions… |
| [[23]](https://medium.com/@EleventhHourEnthusiast/direct-preference-optimization-your-language-model-is-secretly-a-reward-model-5b8f44cb9b9b) | #97, #101, #105, #112 | #96, #100, #106, #110 | #95, #108 | `#97` RLHF often employs Proximal Policy Optimization (PPO) to fine-tune language models based on human preferences. PPO is a widely used reinforcement learning algo… |
| [[8]](https://ysu1989.github.io/courses/au20/cse5539/BERT.pdf) | #56, #58, #60–61, #68, #70 | #59, #69 | #57 | `#56` BERT is instead a stack of encoders that looks at attention in both directions simultaneously ○ To prevent the model from automatically recognizing the target… |
| [[16]](https://huggingface.co/papers/2104.09864) | #77 | #78–80 | — | `#77` we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the… |
| [[22]](https://github.com/dao-ailab/flash-attention) | — | #116, #118 | #119 | `#116` Optimize for inference (iterative decoding) when query has very small sequence length (e.g., query sequence length = 1). The bottleneck here is to load KV cach… |
| [[6]](https://towardsdatascience.com/paper-walkthrough-attention-is-all-you-need-80399cdc59e1/) | #36 | #53 | — | `#36` the dimensionality of each token, which is initially 512, becomes 2048 thanks to the `self.linear_0` layer (`#(1)`). This tensor size remains unchanged until t… |
| [[9]](http://mlg.postech.ac.kr/~jtkim/courses/2022-spring-trends-in-ml/materials/05_bert.pdf) | #62 | #63 | — | `#62` **BASE** model: _L_ = 12, _H_ = 768, _A_ = 12, Total Parameters = 110M. **LARGE** model: _L_ = 24, _H_ = 1024, _A_ = 16, Total Parameters = 340M. |
| [[20]](https://shreyansh26.github.io/post/2023-03-26_flash-attention/) | #84 | — | — | `#84` In standard attention implementations, the S and P matrices are materialized in the HBM, which takes O(N^2) memory. Also, most operations are memory-bound/elem… |
| [[26]](https://papers.baulab.info/papers/also/Rafailov-2023.pdf) | #104 | — | — | `#104` where _β_ is a parameter controlling the deviation from the base reference policy _⇡_ ref, namely the initial SFT model _⇡_<sup>SFT</sup> . |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://scispace.com/papers/attention-is-all-you-need-1hodz0wcqb — anti_bot — barreira de acesso (anti_bot): Before proceeding to your request, you need to solve a puzzle, and the puzzle requires Google Translate to be disabled. 
- https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992 — anti_bot — barreira de acesso (anti_bot): Before proceeding to your request, you need to solve a puzzle, and the puzzle requires Google Translate to be disabled. 
- https://scispace.com/papers/bert-pre-training-of-deep-bidirectional-transformers-for-3mez6kncl2 — anti_bot — barreira de acesso (anti_bot): Before proceeding to your request, you need to solve a puzzle, and the puzzle requires Google Translate to be disabled. 
- https://openreview.net/pdf?id=H4DqfPSibmx — interstitial — barreira de acesso (interstitial): OpenReview .net Verifying your browser Complete the check below to continue to OpenReview Please complete the verificati

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-16`** [2]
  - Trecho: Dada uma matriz de entrada , onde representa o comprimento da sequência e a dimensão de representação oculta da rede, as matrizes , e são obtidas por meio de projeções lineares aprendidas:
  - Justificativa: A evidência sustenta a parte essencial da afirmação: que as matrizes Q, K e V são obtidas por meio de projeções lineares aprendidas a partir da entrada. O trecho menciona explicitamente que cada cabeça de atenção 'learn…
  - Suporte veio de: [2]
  - Evidência: “Each attention head learns different linear projections of the Q, K, and V matrices.”
  - Não coberto pela evidência: A notação específica da matriz de entrada com dimensões representando comprimento da sequência e dimensão de representação oculta não é explicitamente mencionada na evidência.
- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-17`** [5]
  - Trecho: onde , e são as matrizes de pesos treináveis.
  - Justificativa: A afirmacao fragmentada refere-se a matrizes de pesos treinaveis associadas às projecoes no contexto de multi-head attention. A evidencia na secao 3.2.2 descreve explicitamente "learned linear projections" e define as m…
  - Suporte veio de: [5]
  - Evidência: “we found it beneficial to linearly project the queries, keys and values _h_ times with different, learned linear projections to _dk_ , _dk_ and _dv_ dimensions, respectively.”
  - Não coberto pela evidência: Os nomes especificos das variaveis/matrizes referidas no trecho estao ausentes devido a fragmentacao da afirmacao.
- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-18`** [2]
  - Trecho: A computação da atenção por produto escalar escalado é formalizada matematicamente pela seguinte expressão:
  - Justificativa: A evidência confirma que a atenção por produto escalar escalado (scaled dot-product attention) é descrita matematicamente no artigo, mencionando explicitamente 'The paper described the scaled dot-product attention as fo…
  - Suporte veio de: [2]
  - Evidência: “The paper described the scaled dot-product attention as follows:”
  - Não coberto pela evidência: A expressão matemática completa não está visível na evidência (a fórmula parece ter sido omitida por problemas de renderização), embora os componentes sejam descritos.
### UNSUPPORTED

- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-19`** [2]
  - Trecho: O produto matricial calcula a afinidade não normalizada entre cada par de tokens na sequência.
  - Justificativa: A evidência descreve o mecanismo de atenção por produto escalar escalado (scaled dot-product attention) com matrizes Q, K, V e a aplicação de softmax, e menciona 'unnormalized linear transformer' em outro contexto (fast…
  - Não coberto pela evidência: produto matricial como operação específica que calcula afinidade; afinidade não normalizada como conceito; cada par de tokens na sequência como resultado do produto matricial
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [6] [4] [5] [10] [21] [14] [9] [3] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-23`** [5]
  - Trecho: A função Softmax é aplicada de forma posicional ao longo das linhas da matriz de afinidade, gerando uma distribuição de probabilidade que soma 1 para cada token.
  - Justificativa: A evidência confirma que a função softmax é aplicada sobre os produtos escalares (dot products) para obter pesos sobre os valores, mas não menciona explicitamente os termos 'matriz de afinidade', 'aplicada de forma posi…
  - Suporte veio de: [5]
  - Evidência: “We compute the dot products of the query with all keys, divide each by √dk, and apply a softmax function to obtain the weights on the values.”
  - Não coberto pela evidência: matriz de afinidade (termo não presente na evidência); aplicada de forma posicional ao longo das linhas; gerando uma distribuição de probabilidade que soma 1 para cada token
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [4] [7] [8] [21] [14] [22] [20] [6] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-24`** [2]
  - Trecho: O resultado dessa ponderação é multiplicado pela matriz de valores , produzindo uma representação contextualizada em que o vetor de cada token é uma combinação linear dos valores de todos os outros tokens da sequência.
  - Justificativa: A evidência menciona os conceitos de Query, Key, Value matrices e a aplicação do softmax no mecanismo de scaled dot-product attention, mas não descreve explicitamente que o resultado da ponderação (pesos de atenção) é m…
  - Suporte veio de: [2]
  - Não coberto pela evidência: multiplicação do resultado da ponderação pela matriz de valores; produção de uma representação contextualizada; o vetor de cada token como combinação linear dos valores de todos os outros tokens da sequência
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [10] [6] [4] [3] [5] [7] [9] [8] [21] [14] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-15`** [2]
  - Trecho: O núcleo operacional da arquitetura Transformer reside na transformação do conceito de atenção em uma operação matricial linearmente escalável em paralelo.
  - Justificativa: A evidência sustenta que o Transformer se baseia no mecanismo de atenção matricial (Q, K, V) e que é paralelizável. No entanto, a afirmação de que a operação é 'linearmente escalável' é explicitamente contradizida pela…
  - Evidência: “Since the model relies on Query, Key, and Value matrices that come from the same source (i.e., the input sequence or context window), this eliminates the need for RNNs, completely ensuring parallelizability for the arch…”
  - Não coberto pela evidência: linearmente escalável — contraditado pela evidência que menciona custo quadrático

---

## 10. Trechos Citados Não Auditados

Motivos: 26 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 9 citam referência não baixada/inacessível.

- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-0` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-1` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-2` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-3` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-4` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-5` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-6` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-7` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-8` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-9` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-10` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-11` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-12` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-13` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-14` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-28` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-54` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-71` — Referencia(s) citada(s) ['ab4c8cf624c8a6ac'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-73` — Referencia(s) citada(s) ['ab4c8cf624c8a6ac'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-82` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-83` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-86` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-87` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-88` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-89` — Referencia(s) citada(s) ['bb646e9065fdcfcd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-98` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-99` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-102` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-103` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-107` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-109` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-111` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-113` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-114` — Referencia(s) citada(s) ['6d274bf31e96172c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_9a296a2eb92b_20261024T214609Z-122` — Referencia(s) citada(s) ['3f86da314b54d5c0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.