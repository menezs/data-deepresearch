# Relatório de Auditoria — Gemini (arquitetura_transformers_c1ecf332a0d0_20261115T134106Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Consolidado/arquitetura_transformers.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | arquitetura_transformers_c1ecf332a0d0_20261115T134106Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T03:02:54.675538+00:00 |
| **Total de trechos citados** | 115 |
| **Tempo de processamento** | 2:13:21:48 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 95.5 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-15 13:41:30+00:00 |
| Citações no corpo | 115 marcadores, 66 distintos |
| Referências listadas | 77 (11 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 92 | 80.0% |
| **UNSUPPORTED** | 19 | 16.5% |
| **CONTRADICTED** | 2 | 1.7% |
| **SKIPPED** | 2 | 1.7% |
| **TOTAL** | 115 | 100.0% |

Sobre os 113 trechos citados auditados: SUPPORTED 81,41%, UNSUPPORTED 16,81%, CONTRADICTED 1,76%.

> **42 dos 92 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 42 estão **contados dentro** dos 92 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`27` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `11` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` Pure self-attention stacked without skip connections and multilayer perceptrons loses representation rank doubly expone… | [12] | [13] [32] [6] [1] [4] [75] [35] [29] | — |
| `#4` As models scaled, self-attention's quadratic complexity per layer and growing key-value (KV) cache footprint shifted in… | [6] | [17] [71] [15] [75] [74] [76] [73] | — |
| `#11` Attention mechanisms first emerged to relieve this fixed-vector bottleneck within recurrent encoders and decoders rathe… | [25] | [24] [5] [1] [6] [29] [28] [2] [30] [3] | — |
| `#56` Following the original encoder-decoder blueprint, Transformer NLP bifurcated into three primary configurations. | [8] | [9] [42] [29] [2] [1] [24] [3] [67] [31] [34] [63] [6] | — |
| `#57` Encoder-only models led by BERT (Devlin and colleagues, 2018)—which used 12 heads and in BERT-base according to seconda… | [32] | [33] [41] [8] [42] [9] [34] [4] | — |
| `#58` pretrained deep bidirectional representations via masked language modeling (MLM), advancing SQuAD v1.1 Test F1 to 93.2… | [8] | [41] [9] [52] [24] [38] [42] [10] | — |
| `#60` Causal decoder-only models, however, ultimately anchored general-purpose LLMs after GPT-3 (Brown and colleagues, 2020)… | [11] | [53] [9] [8] [52] | — |
| `#74` Schaeffer, Miranda, and Koyejo (2023) countered that such apparent discontinuities often evaporate under continuous met… | [39] | [54] [32] [58] [53] [59] [51] [17] [42] [21] [13] [50] | — |
| `#96` Shazeer (2019) introduced Multi-Query Attention (MQA) to share a single K/V head across all query heads, speeding up de… | [18] | [15] [70] [21] [52] [71] [72] [17] [6] [74] | — |
| `#108` DeepSeek-V3 extended MoE to 671B main parameters (685B including 14B Multi-Token Prediction weights) with 37B active pe… | [14] | [52] [18] [76] | — |
| `#110` Finally, attention's quadratic scaling revived sub-quadratic alternatives and hybrid models. Katharopoulos and colleagu… | [29] | [77] [20] [21] [4] [5] [64] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2327952 |
| **Média de tokens por requisição** | 20601.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 11/77 (14.3%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 2.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf?utm_source=nationaltribune&utm_medium=nationaltribune&utm_campaign=news) | downloaded | 11 | 11 | 0 | 0 | 0 |
| [[8]](https://arxiv.org/html/2512.03803v1) | downloaded | 5 | 2 | 1 | 2 | 0 |
| [[32]](https://medium.com/@aridiosilva/opening-the-black-box-of-llm-inference-foundations-of-generative-ai-65f6d3563bd2) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[1]](https://arxiv.org/abs/1706.03762) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[6]](https://arxiv.org/pdf/1706.03762) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[39]](https://arxiv.org/html/2310.12956v2) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[3]](https://www.alphaxiv.org/abs/1706.03762v4) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[17]](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60308-3) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[18]](https://local-ai-zone.github.io/blog/deepseek-kv-cache-optimization-research-paper.html) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[25]](https://arxiv.org/pdf/1508.04025) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[48]](https://arxiv.org/html/2404.01856v3) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[5]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[7]](https://www.researchgate.net/publication/323904682_Tensor2Tensor_for_Neural_Machine_Translation) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[12]](https://arxiv.org/abs/2012.14913) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[13]](https://arxiv.org/abs/2103.03404) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[14]](https://arxiv.org/abs/2412.19437) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[19]](https://arxiv.org/abs/2207.00729) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[20]](https://arxiv.org/abs/2312.00752) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[28]](https://arxiv.org/abs/1601.06733) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[29]](https://slds-lmu.github.io/seminar_nlp_ss20/attention-and-self-attention-for-nlp.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[55]](https://arxiv.org/html/2402.11004v1) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[56]](https://arxiv.org/pdf/2212.07677) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[62]](https://arxiv.org/html/2310.03016v1) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[4]](https://huggingface.co/datasets/attention-wiki/knowledge-base/commit/597b4e5675fb2ddd291e75a886eedc568c6fedc2) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://arxiv.org/abs/2407.21783) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[11]](https://arxiv.org/abs/2005.14165) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[15]](https://arxiv.org/abs/2305.13245) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[16]](https://arxiv.org/abs/2205.14135) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://arxiv.org/abs/2405.21060) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://arxiv.org/abs/2403.19887) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://arxiv.org/abs/1409.3215) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://gregorygundersen.com/blog/2025/10/01/large-language-models/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[27]](https://www.researchgate.net/publication/339350384_A_Survey_of_Deep_Learning_Techniques_for_Neural_Machine_Translation) | error | 1 | 0 | 0 | 0 | 1 |
| [[30]](https://arxiv.org/abs/1705.03122) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://arxiv.org/abs/1905.10650) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://arxiv.org/abs/1905.09418) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://arxiv.org/abs/1910.07467) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://arxiv.org/abs/2002.05202) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://arxiv.org/abs/2303.06296) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://arxiv.org/abs/2609.34272) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://www.researchgate.net/publication/404686943_A_Survey_of_Large_Language_Models) | error | 1 | 0 | 0 | 0 | 1 |
| [[44]](https://arxiv.org/abs/1508.07909) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://arxiv.org/abs/1808.06226) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[46]](https://arxiv.org/abs/2305.15425) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://patterniseverything.com/llm/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[49]](https://arxiv.org/abs/2001.08361) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[50]](https://arxiv.org/abs/2203.15556) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[52]](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[53]](https://arxiv.org/abs/2206.07682) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[57]](https://arxiv.org/abs/2211.15661) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[58]](https://arxiv.org/abs/2209.11895) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[59]](https://arxiv.org/pdf/2311.00237) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[60]](https://arxiv.org/html/2402.14180v2) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[61]](https://arxiv.org/html/2402.14735v2) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[63]](https://arxiv.org/abs/1906.06755) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[64]](https://arxiv.org/abs/2104.09864) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[65]](https://arxiv.org/abs/2108.12409) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[66]](https://arxiv.org/abs/2306.15595) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[67]](https://arxiv.org/abs/2309.00071) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[68]](https://arxiv.org/abs/2307.03172) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[69]](https://arxiv.org/abs/2309.17453) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[72]](https://arxiv.org/abs/2307.08691) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[73]](https://arxiv.org/abs/2407.08608) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[74]](https://arxiv.org/abs/2606.07703) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[75]](https://arxiv.org/abs/2101.03961) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[76]](https://arxiv.org/html/2603.07685v2) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://arxiv.org/abs/2204.05832) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://arxiv.org/abs/1409.0473) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://scaledojo.dev/papers/attention-is-all-you-need) | downloaded | 0 · nunca citada | — | — | — | — |
| [[35]](https://arxiv.org/abs/2002.04745) | downloaded | 0 · nunca citada | — | — | — | — |
| [[41]](https://arxiv.org/abs/1810.04805) | downloaded | 0 · nunca citada | — | — | — | — |
| [[42]](https://arxiv.org/abs/1910.10683) | downloaded | 0 · nunca citada | — | — | — | — |
| [[51]](https://arxiv.org/abs/2401.00448) | downloaded | 0 · nunca citada | — | — | — | — |
| [[54]](https://arxiv.org/abs/2304.15004) | downloaded | 0 · nunca citada | — | — | — | — |
| [[70]](https://arxiv.org/abs/1911.02150) | downloaded | 0 · nunca citada | — | — | — | — |
| [[71]](https://arxiv.org/abs/2405.04434) | downloaded | 0 · nunca citada | — | — | — | — |
| [[77]](https://arxiv.org/abs/2006.16236) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf?utm_source=nationaltribune&utm_medium=nationaltribune&utm_campaign=news) | #1, #7, #27–33, #35, #37 | — | — | `#1` a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires O(n) sequential op… |
| [[8]](https://arxiv.org/html/2512.03803v1) | #59, #61 | #2 | #56, #58 | `#59` 2d7205e3738744ae: "The T5 family, on the other hand, uses an encoder-decoder architecture as shown in Figure 1. [...] However, within its own layers, a causal… |
| [[32]](https://medium.com/@aridiosilva/opening-the-black-box-of-llm-inference-foundations-of-generative-ai-65f6d3563bd2) | #34, #48–49 | #57 | #78 | `#34` With d_model = 512 and h = 8, each head has d_k = d_v = 64 |
| [[1]](https://arxiv.org/abs/1706.03762) | #0, #19–20 | — | #41 ⚡ | `#0` We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. [...… |
| [[6]](https://arxiv.org/pdf/1706.03762) | #22, #24 | #4 | #21 | `#22` Recurrent\|_O_(_n · d_<sup>2</sup>)\|_O_(_n_)\|_O_(_n_)\| |
| [[39]](https://arxiv.org/html/2310.12956v2) | #53, #75 | #54, #74 | — | `#53` ill-distributed attention scores lead to small gradients for V and O |
| [[3]](https://www.alphaxiv.org/abs/1706.03762v4) | #38–40 | — | — | `#38` The decoder also has six layers but includes an additional multi-head attention layer that attends to the encoder's output. Crucially, the decoder's self-atten… |
| [[17]](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-026-60308-3) | #26, #95, #106 | — | — | `#26` The standard Transformer architecture is constrained by the quadratic computational complexity of its self-attention mechanism |
| [[18]](https://local-ai-zone.github.io/blog/deepseek-kv-cache-optimization-research-paper.html) | #100–101 | #96 | — | `#100` MLA caches a 512-dimensional compressed latent plus a 64-dimensional rotary key per token — 576 cached elements per layer |
| [[25]](https://arxiv.org/pdf/1508.04025) | #12, #14 | — | #11 | `#12` While our global attention approach is similar in spirit to the model proposed by Bahdanau et al. (2015) [...] A global context vector ct is then computed as t… |
| [[48]](https://arxiv.org/html/2404.01856v3) | #67 | #69 | #71 (s/ aval.) | `#67` we trained a custom byte-level BPE tokenizer using the same pre-normalization as the FinGPT tokenizer. We selected a vocabulary size of 128K tokens, aiming to… |
| [[5]](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need) | #42 | #10 | — | `#42` As of 2026, the paper has been cited more than 150,000 times, placing it among the top ten most-cited papers of the 21st century. |
| [[7]](https://www.researchgate.net/publication/323904682_Tensor2Tensor_for_Neural_Machine_Translation) | #23, #25 | — | — | `#23` Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. [...] Convolutional O(k·n·d2)O(1) O(… |
| [[12]](https://arxiv.org/abs/2012.14913) | #47 | #3 | — | `#47` We show that feed-forward layers in transformer-based language models operate as key-value memories [...] the output of a feed-forward layer is a composition o… |
| [[13]](https://arxiv.org/abs/2103.03404) | #45–46 | — | — | `#45` Yihe Dong Jean-Baptiste Cordonnier Andreas Loukas Google EPFL EPFL [...] without skip connections or multi-layer perceptrons (MLPs), the output converges doubl… |
| [[14]](https://arxiv.org/abs/2412.19437) | #99 | #108 | — | `#99` DeepSeek-V3 still adopts Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference [...] These two architectures have been validated in De… |
| [[19]](https://arxiv.org/abs/2207.00729) | #5, #88 | — | — | `#5` Any c log n-precision depth-d transformer operating on inputs in Σ^n can be simulated by a threshold circuit family of depth 3 + (9 + 2d⊕)d. |
| [[20]](https://arxiv.org/abs/2312.00752) | #111 | #6 | — | `#111` our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation. |
| [[28]](https://arxiv.org/abs/1601.06733) | #15–16 | — | — | `#15` the LSTMN which applies attention for intra-relation reasoning, with the encoder-decoder network whose attention module learns the inter-alignment between two… |
| [[29]](https://slds-lmu.github.io/seminar_nlp_ss20/attention-and-self-attention-for-nlp.html) | #17 | #110 | — | `#17` While the LSTMN introduced self-attention, it retains the drawbacks that come from the use of a RNN which are discussed at the end of the Transformer section. |
| [[55]](https://arxiv.org/html/2402.11004v1) | #76, #80 | — | — | `#76` We show that the transition from a phase of learning the simple-but-inadequate solution to the complex-and-correct solution happens due to an alignment between… |
| [[56]](https://arxiv.org/pdf/2212.07677) | #77, #82 | — | — | `#77` It has been hypothesised that their success is due in part to a phenomenon called in-context learning (Brown et al., 2020; Liu et al., 2021): an ability to fle… |
| [[62]](https://arxiv.org/html/2310.03016v1) | #86, #113 | — | — | `#86` when learning parities their performance is as bad as random guessing, but known algorithms can perform near-perfectly with the same size dataset. |
| [[4]](https://huggingface.co/datasets/attention-wiki/knowledge-base/commit/597b4e5675fb2ddd291e75a886eedc568c6fedc2) | #36 | — | — | `#36` quote: "Table 3: reducing to a single head is 0.9 BLEU worse than the best setting." note: "Ablation (rows varying h) shows degradation with one head and also… |
| [[10]](https://arxiv.org/abs/2407.21783) | — | #62 | — | `#62` In this paper, we present a new set of foundation models for language, called **Llama 3** . |
| [[11]](https://arxiv.org/abs/2005.14165) | — | #60 | — | `#60` GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-th… |
| [[15]](https://arxiv.org/abs/2305.13245) | #97 | — | — | `#97` we introduce grouped-query attention (GQA), a generalization of multi-query attention which uses an intermediate (more than one, less than number of query head… |
| [[16]](https://arxiv.org/abs/2205.14135) | #102 | — | — | `#102` We propose FlashAttention, an IO-aware exact attention algorithm [...] FlashAttention trains Transformers faster than existing baselines: 15% end-to-end wall-c… |
| [[21]](https://arxiv.org/abs/2405.21060) | #112 | — | — | `#112` 0c47ea4675bf3dd1 |
| [[22]](https://arxiv.org/abs/2403.19887) | #114 | — | — | `#114` Jamba is a hybrid decoder architecture that mixes Transformer layers [51] with Mamba layers [17]... We conjecture that the lack of an attention mechanism in th… |
| [[23]](https://arxiv.org/abs/1409.3215) | #8 | — | — | `#8` Our method uses a multilayered Long Short-Term Memory (LSTM) to map the input sequence to a vector of a fixed dimensionality, and then another deep LSTM to dec… |
| [[24]](https://gregorygundersen.com/blog/2025/10/01/large-language-models/) | #9 | — | — | `#9` it would be forced to compress that information into a much shorter, fixed-width vector with no temporal structure that would then be fed into the decoder. [..… |
| [[30]](https://arxiv.org/abs/1705.03122) | #18 | — | — | `#18` We introduce an architecture based entirely on convolutional neural networks. [...] We outperform the accuracy of the deep LSTM setup of Wu et al. (2016) on bo… |
| [[33]](https://arxiv.org/abs/1905.10650) | #43 | — | — | `#43` Are Sixteen Heads Really Better than One? ... Paul Michel ... Omer Levy ... Graham Neubig ... 33rd Conference on Neural Information Processing Systems (NeurIPS… |
| [[34]](https://arxiv.org/abs/1905.09418) | #44 | — | — | `#44` When pruning heads using a method based on stochastic gates and a differentiable relaxation of the _L_ 0 penalty, we observe that specialized heads are last to… |
| [[36]](https://arxiv.org/abs/1910.07467) | #50 | — | — | `#50` Extensive experiments on several tasks using diverse network architectures show that RMSNorm achieves comparable performance against LayerNorm but reduces the… |
| [[37]](https://arxiv.org/abs/2002.05202) | #51 | — | — | `#51` Noam Shazeer Google noom@gmail.com February 14, 2020 |
| [[38]](https://arxiv.org/abs/2303.06296) | #52 | — | — | `#52` STABILIZING TRANSFORMER TRAINING BY PREVENTING ATTENTION ENTROPY COLLAPSE |
| [[40]](https://arxiv.org/abs/2609.34272) | #55 | — | — | `#55` It cuts the remaining median query/key gradient errors from 219%/13% to 0.34%/0.37%, on par with FP32 attention, for 4.7% more time per training step. In match… |
| [[44]](https://arxiv.org/abs/1508.07909) | #63 | — | — | `#63` Rico Sennrich and Barry Haddow and Alexandra Birch School of Informatics, University of Edinburgh; we introduce a simpler and more effective approach, making t… |
| [[45]](https://arxiv.org/abs/1808.06226) | #64 | — | — | `#64` SentencePiece, a simple and language independent text tokenizer and detokenizer mainly for Neural Network-based text generation systems where the size of vocab… |
| [[46]](https://arxiv.org/abs/2305.15425) | #65 | — | — | `#65` Language Model Tokenizers Introduce Unfairness Between Languages — Aleksandar Petrov, Emanuele La Malfa, Philip H.S. Torr, Adel Bibi University of Oxford — 37t… |
| [[47]](https://patterniseverything.com/llm/) | — | — | #66 | — |
| [[49]](https://arxiv.org/abs/2001.08361) | #68 | — | — | `#68` The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of… |
| [[50]](https://arxiv.org/abs/2203.15556) | #70 | — | — | `#70` **_Chinchilla_ reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over** **_Gopher_** |
| [[52]](https://cs336.stanford.edu/spring2025-lectures/?trace=var/traces/lecture_01.json) | #72 | — | — | `#72` We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens |
| [[53]](https://arxiv.org/abs/2206.07682) | #73 | — | — | `#73` We consider an ability to be emergent if it is not present in smaller models but is present in larger models. Thus, emergent abilities cannot be predicted simp… |
| [[57]](https://arxiv.org/abs/2211.15661) | #81 | — | — | `#81` First, we prove by construction that transformers can implement learning algorithms for linear models based on gradient descent and closed-form ridge regressio… |
| [[58]](https://arxiv.org/abs/2209.11895) | #79 | — | — | `#79` For small attention-only models, we present strong, causal evidence; for larger models with MLPs, we present correlational evidence. |
| [[59]](https://arxiv.org/pdf/2311.00237) | #84 | — | — | `#84` Dai et al. (2023) adopted a perspective of viewing LLMs as meta-optimizers and interpreting ICL as a form of implicit fine-tuning. They first conducted a quali… |
| [[60]](https://arxiv.org/html/2402.14180v2) | — | #83 | — | `#83` we prove that in case of GD++, the preconditioner results in a second order optimization algorithm. |
| [[61]](https://arxiv.org/html/2402.14735v2) | #85 | — | — | `#85` However, these works are solely concerned with the representational capabilities of transformers, and do not answer the question of whether gradient descent in… |
| [[63]](https://arxiv.org/abs/1906.06755) | #87 | — | — | `#87` In this work, we mathematically investigate the computational power of self-attention to model formal languages. Across both soft and hard attention, we show s… |
| [[64]](https://arxiv.org/abs/2104.09864) | #89 | — | — | `#89` we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information [...] the enhanced transformer with rotary p… |
| [[65]](https://arxiv.org/abs/2108.12409) | #90 | — | — | `#90` We therefore introduce a simpler and more efficient position method, Attention with Linear Biases (ALiBi). [...] ALiBi's inductive bias towards recency also le… |
| [[66]](https://arxiv.org/abs/2306.15595) | #91 | — | — | `#91` We present Position Interpolation (PI) that extends the context window sizes of RoPE-based (Su et al., 2021) pretrained LLMs such as LLaMA (Touvron et al., 202… |
| [[67]](https://arxiv.org/abs/2309.00071) | #92 | — | — | `#92` We present YaRN (Yet another RoPE extensioN method), a compute-efficient method to extend the context window of such models ... we demonstrate that YaRN exhibi… |
| [[68]](https://arxiv.org/abs/2307.03172) | #93 | — | — | `#93` **Lost in the Middle: How Language Models Use Long Contexts** **Nelson F. Liu** [...] performance is often highest when relevant information occurs at the begi… |
| [[69]](https://arxiv.org/abs/2309.17453) | #94 | — | — | `#94` In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2 × speedup. |
| [[72]](https://arxiv.org/abs/2307.08691) | #103 | — | — | `#103` We empirically validate that when used end-to-end to train GPT-style models, FlashAttention-2 reaches training speed of up to 225 TFLOPs/s per A100 GPU (72% mo… |
| [[73]](https://arxiv.org/abs/2407.08608) | #104 | — | — | `#104` We develop three main techniques to speed up attention on Hopper GPUs: exploiting asynchrony of the Tensor Cores and TMA to (1) overlap overall computation and… |
| [[74]](https://arxiv.org/abs/2606.07703) | — | — | #105 ⚡ | `#105` sparse serving reaches 1.71× for Qwen3.5-0.8B on NPU against the vLLM Ascend FlashAttention baseline and 1.93× for Qwen3.5-9B on GPU against its dense FlashAtt… |
| [[75]](https://arxiv.org/abs/2101.03961) | #107 | — | — | `#107` our work also replaced the FFN layer in the Transformer ... the Switch-C model, with 1.6T parameters and 2048 experts ... the SwitchC Transformer variant is 4x… |
| [[76]](https://arxiv.org/html/2603.07685v2) | #109 | — | — | `#109` 8ccdf64e8c44880b |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-0`** [1]
  - Trecho: Introduced in 2017 by Vaswani and colleagues, the Transformer architecture redesigned neural sequence modeling by replacing recurrence and convolution entirely with self-attention mechanisms.
  - Justificativa: A evidência sustenta a parte essencial da afirmação: o Transformer foi apresentado em 2017 (NIPS 2017), substituiu recorrência e convolução inteiramente por mecanismos de auto-atenção, e redesenhou a modelagem de sequên…
  - Suporte veio de: [1]
  - Evidência: “31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA.”
  - Não coberto pela evidência: A autoria específica 'by Vaswani and colleagues' — o sobrenome 'Vaswani' não aparece explicitamente na evidência, embora primeiros nomes de autores (Jakob, Ashish, Noam, Niki, Llion, Lukasz, Aidan) sejam mencionados.
- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-1`** [2]
  - Trecho: Rather than stepping hidden states sequentially across a sequence, self-attention connects every token position directly to every other position in a constant number of sequential operations, unlocking large-scale GPU p…
  - Justificativa: A evidência sustenta todas as partes essenciais da afirmação: (1) modelos recorrentes geram hidden states sequencialmente, o que impede paralelização; (2) self-attention conecta todas as posições com um número constante…
  - Suporte veio de: [2]
  - Evidência: “Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states ht, as a functio…”
  - Não coberto pela evidência: O termo exato 'large-scale GPU parallelization' não aparece literalmente; a evidência fala em 'significantly more parallelization' e menciona treinamento em GPUs, mas não usa a expressão 'large-scale'.
- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-5`** [19]
  - Trecho: At the same time, theoretical complexity bounds show that fixed-depth, log-precision Transformers remain limited to constant-depth threshold circuits
  - Justificativa: A evidência demonstra explicitamente que transformers de log-precision e profundidade fixa podem ser simulados por famílias de circuitos de limiar (threshold circuits) de profundidade constante (TC^0), tanto na versão n…
  - Suporte veio de: [19]
  - Evidência: “Any c log n-precision depth-d transformer operating on inputs in Σ^n can be simulated by a threshold circuit family of depth 3 + (9 + 2d⊕)d.”
### UNSUPPORTED

- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-2`** [8]
  - Trecho: Over the following decade, this architecture—particularly in its causal decoder-only configuration—became the computational foundation of large language models (LLMs), enabling zero-shot generalization, few-shot in-cont…
  - Justificativa: A evidência menciona que modelos causal decoder-only exibem a mais forte generalização zero-shot após treinamento não supervisionado (Wang et al. [26]) e cita capacidades gerais de LLMs como chain-of-thought reasoning e…
  - Suporte veio de: [8]
  - Evidência: “Wang et al. [26] found that causal decoder-only models trained on an auto-regressive language modeling objectives exhibit the strongest zero-shot generalization after unsupervised training.”
  - Não coberto pela evidência: Over the following decade (período de tempo não mencionado); became the computational foundation of large language models (LLMs) (não afirmado explicitamente); few-shot in-context adaptation (não vinculado explicitamente à arquitetura causal decoder-only)
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-3`** [12]
  - Trecho: Pure self-attention stacked without skip connections and multilayer perceptrons loses representation rank doubly exponentially with depth, while position-wise feed-forward networks (FFNs) act as key-value memories that…
  - Justificativa: A evidência sustenta apenas a segunda parte da afirmação (FFNs atuam como memórias key-value e compõem informação distribuída entre camadas), mas não contém nenhuma informação sobre a primeira parte: que self-attention…
  - Suporte veio de: [12]
  - Evidência: “We show that feed-forward layers in transformer-based language models operate as key-value memories, where each key correlates with textual patterns in the training examples, and each value induces a distribution over t…”
  - Não coberto pela evidência: Pure self-attention stacked without skip connections and multilayer perceptrons loses representation rank doubly exponentially with depth
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [13] [32] [6] [1] [4] [75] [35] [29] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-4`** [6]
  - Trecho: As models scaled, self-attention's quadratic complexity per layer and growing key-value (KV) cache footprint shifted inference constraints toward memory bandwidth, spurring grouped-query and latent cache compression, IO…
  - Justificativa: A evidência (o paper 'Attention Is All You Need') sustenta apenas a complexidade quadrática por camada do self-attention (O(n²·d) na Tabela 1), mas não menciona KV cache, memory bandwidth, grouped-query attention, laten…
  - Suporte veio de: [6]
  - Evidência: “Self-Attention|O(n<sup>2</sup> · d)|O(1)|O(1)|”
  - Não coberto pela evidência: KV cache footprint; inference constraints shifted toward memory bandwidth; grouped-query attention
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [17] [71] [15] [75] [74] [76] [73] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-41`** [1]
  - Trecho: Empirically, the Transformer reached 28.4 BLEU on WMT 2014 English-to-German (beating prior bests by over 2.0 BLEU) and 41.0 BLEU on WMT 2014 English-to-French while training its base model in 12 hours on 8 NVIDIA P100…
  - Justificativa: A afirmacao apresenta os scores 28.4 BLEU (EN-DE) e 41.0 BLEU (EN-FR) como resultados obtidos "treinando seu modelo base em 12 horas". A evidencia contradiz essa associacao: 28.4 BLEU foi alcancado pelo Transformer (big…
  - Suporte veio de: [1]
  - Evidência: “the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU, establishing a new state-of-the-art BLEU score of 28.4. The configura…”
- **Trecho citado `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-105`** [74]
  - Trecho: Recent 2026 research pairs dense layers with oracle-guided sparse prefill—reporting preliminary single-card time-to-first-token speedups of 1.71x to 1.93x over FlashAttention-2 across 4K to 100K RULER sweeps within 0.48…
  - Justificativa: A CLAIM funde três achados distintos e os atribui incorretamente. (1) O speedup de 1.71× é sobre 'vLLM Ascend FlashAttention', NÃO sobre FlashAttention-2; apenas 1.93× é sobre FlashAttention-2. (2) O sweep de RULER de 4…
  - Evidência: “sparse serving reaches 1.71× for Qwen3.5-0.8B on NPU against the vLLM Ascend FlashAttention baseline and 1.93× for Qwen3.5-9B on GPU against its dense FlashAttention-2 baseline”
  - Não coberto pela evidência: Afirmar que 1.71× é sobre FlashAttention-2 — a evidência mostra que é sobre Ascend FlashAttention; Afirmar que os speedups de TTFT ocorrem 'across 4K to 100K RULER sweeps' — o sweep 4K–100K é de qualidade oracle, não de TTFT; Afirmar que 'within 0.48 points' se aplica aos speedups de TTFT — 0.48 pontos refere-se ao gap de qualidade oracle no sweep RULER
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A claim atribui ambos os speedups (1.71x e 1.93x) ao FlashAttention-2, mas a evidência indica que 1.71x é contra o 'vLLM Ascend FlashAttent…") — cascata: baseline → context_expansion

---

## 9. Trechos Citados Não Auditados

Motivos: 2 citam referência não baixada/inacessível.

- `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-13` — Referencia(s) citada(s) ['bd2e5183aeaece3d'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `arquitetura_transformers_c1ecf332a0d0_20261115T134106Z-98` — Referencia(s) citada(s) ['07c2b306964d4bdc'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).