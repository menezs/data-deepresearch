# Relatório de Auditoria — Claude (regulacao_ia_026c7ad6edf4_20261115T040310Z)

**Arquivo auditado:** `answers/Ingles/Claude/Emergente/regulacao_ia.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | regulacao_ia_026c7ad6edf4_20261115T040310Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T04:24:47.859201+00:00 |
| **Total de trechos citados** | 98 |
| **Tempo de processamento** | 0:00:21:37 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 27.9 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 123 marcadores, 39 distintos |
| Referências listadas | 39 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 55 | 56.1% |
| **UNSUPPORTED** | 26 | 26.5% |
| **CONTRADICTED** | 2 | 2.0% |
| **SKIPPED** | 15 | 15.3% |
| **TOTAL** | 98 | 100.0% |

Sobre os 83 trechos citados auditados: SUPPORTED 66,26%, UNSUPPORTED 31,32%, CONTRADICTED 2,40%.

> **20 dos 55 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 20 estão **contados dentro** dos 55 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`32` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `8` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#4` Both have been shaped by industry lobbying, US pressure and a growing argument that rules written in 2021–2024 should b… | [8] [9] | [15] [6] [36] [22] [34] [13] [27] [5] [12] [20] | — |
| `#25` Enforcement is split between the Commission's AI Office, which oversees GPAI with support from an AI Board of member-st… | [2] [13] | [15] [6] [12] [17] [10] [8] [14] | — |
| `#27` The Commission may fine GPAI providers up to 3% or €15 million, a power that took effect on 2 August 2026. | [2] [12] | — | [15] [17] [10] [13] [19] [18] [6] ⚠ |
| `#32` Stand-alone Annex III high-risk rules now apply from 2 December 2027 instead of 2 August 2026, and product-embedded Ann… | [18] [19] | [13] [17] [6] [15] [12] [27] [26] | — |
| `#37` A new prohibition covers AI that generates non-consensual intimate images of identifiable people, including "nudificati… | [2] [18] | [13] [12] [17] [19] [31] [28] [34] [26] | — |
| `#49` In February 2022 Senate President Rodrigo Pacheco formed a commission of jurists to draft an alternative. | [22] | [6] [4] [23] [3] [5] [34] [24] [27] [26] | — |
| `#73` By May the committee had not met that year, and targets of 19 May for the report and 27 May for a plenary vote were set… | [30] | [10] [34] [9] [13] [35] [32] [6] [26] [27] [4] [16] [3] | — |
| `#84` An earlier ITS Rio count of the November 2024 text, reported by Tech Policy Press, found 56 obligations, so the exact f… | [22] | [6] [7] [17] [5] [29] [27] [24] [26] | — |
| `#90` On governance, Brazil relies on a hub-and-spoke system of sectoral agencies coordinated by the ANPD, while the EU combi… | [30] [17] | [6] [37] [5] [36] [22] [20] [13] [7] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1372688 |
| **Média de tokens por requisição** | 16538.4 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/39 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng/pdf) | blocked | 18 | 0 | 0 | 0 | 18 |
| [[26]](https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=3106629&filename=Avulso+PL+2338%2F2023) | downloaded | 8 | 5 | 3 | 0 | 0 |
| [[17]](https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force) | downloaded | 7 | 3 | 4 | 0 | 0 |
| [[5]](https://policyreview.info/articles/news/road-regulation-artificial-intelligence-brazilian-experience/1737) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[13]](https://fpf.org/?p=250371) | downloaded | 6 | 2 | 4 | 0 | 0 |
| [[22]](https://techpolicy.press/brazils-ai-law-faces-uncertain-future-as-big-tech-warms-to-trump) | downloaded | 6 | 4 | 2 | 0 | 0 |
| [[1]](https://www.consilium.europa.eu/en/policies/artificial-intelligence/timeline-artificial-intelligence/) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[6]](https://www.barbieriadvogados.com/brazil-ai-act/) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[8]](https://www.theregister.com/ai-and-ml/2026/05/07/eu-hits-snooze-on-ai-act-rules-after-industry-backlash/5234530) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[12]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[18]](https://eeas.europa.eu/delegations/chile/artificial-intelligence-council-gives-final-green-light-simplify-and-streamline-rules_en) | downloaded | 5 | 1 | 3 | 1 | 0 |
| [[4]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[9]](https://www.aosfatos.org/noticias/deputados-da-comissao-da-ia-atuaram-em-prol-de-big-techs-apos-visitas-de-lobistas/) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[3]](https://www.aosfatos.org/noticias/aprovada-senado-regulacao-ia-camara/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[27]](https://cesconbarrieu.com.br/en/senado-aprova-o-marco-legal-da-ia-2/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[30]](https://teletime.com.br/04/05/2026/parlamentares-tentam-retomar-cronograma-para-pl-de-ia/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[7]](https://itsrio.org/wp-content/uploads/2017/01/2025.06.23-Matriz-comparada-de-obrigacoes_-PL-2338_2023-vs.-EU-AI-act_Relatorio_AI-16-jun-1.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[10]](https://techcrunch.com/2024/03/13/deal-on-eu-ai-act-gets-thumbs-up-from-european-parliament) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[14]](https://digital-strategy.ec.europa.eu/en/policies/gpai-code-practice) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[15]](https://www.euronews.com/2025/07/03/europes-top-ceos-call-for-commission-to-slow-down-on-ai-act) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[21]](https://www.cnnbrasil.com.br/tecnologia/camara-aprova-marco-legal-para-inteligencia-artificial-entenda-implicacoes/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[35]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[11]](https://eur-lex.europa.eu/eli/reg/2024/1689/2024-07-12/swe/pdf) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[16]](https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[19]](https://www.pinsentmasons.com/out-law/news/law-delaying-eu-high-risk-ai-rules-finalised) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[20]](https://edri.org/our-work/commissions-digital-omnibus-is-a-major-rollback-of-eu-digital-protections/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://teletime.com.br/06/12/2022/comissao-de-juristas-propoe-criacao-de-autoridade-para-inteligencia-artificial/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://institutobrasileiro.ia.br/artigos/pl-2338-2023-onde-esta-o-projeto-de-lei-de-ia/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://agenciabrasil.ebc.com.br/geral/noticia/2024-12/senado-aprova-regras-para-uso-da-inteligencia-artificial) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.camara.leg.br/noticias/1140392-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[31]](https://www.cnnbrasil.com.br/politica/avanco-do-pl-da-ia-esbarra-em-decisao-sobre-redata-e-compromisso-do-senado/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://www.amapadigital.com.br/novo/noticia/10/06/2026-votacao-do-pl-da-inteligencia-artificial-e-adiada-enquanto-camara-busca-consenso-com-o-senado.ghtml) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.congressoemfoco.com.br/noticia/119344/relator-quer-marco-da-ia-atemporal-para-acompanhar-inovacao) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://desinformante.com.br/ue-avanca-regulacao-ia-projeto-brasileiro-parado/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://itif.org/publications/2025/12/05/europe-writes-the-rules-and-the-world-pays-the-price/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[37]](https://techpolicy.press/the-dmas-brussels-effect-tested-and-contested-lessons-from-brazil) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://www.cmtradelaw.com/2026/06/ustr-finds-certain-brazilian-practices-in-six-issue-areas-actionable-under-section-301-proposes-25-tariffs-on-brazilian-goods-and-invites-comments/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[39]](https://www.correiodamanha.com.br/mundo/internacional/2026/07/305010-deputados-dos-eua-acionam-trump-contra-regulacao-das-big-techs-no-brasil.html) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[26]](https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=3106629&filename=Avulso+PL+2338%2F2023) | #59–60, #63, #65–66 | #62, #64, #87 | — | `#59` Seção II Do Risco Excessivo Art. 13. São vedados o desenvolvimento, a implementação e o uso de sistemas de IA: I – com o propósito de: a) instigar ou induzir o… |
| [[17]](https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force) | #31, #33, #39 | #34, #40, #42, #90 | — | `#31` Regulation (EU) 2026/1744, commonly referred to as the AI Omnibus, was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026. |
| [[5]](https://policyreview.info/articles/news/road-regulation-artificial-intelligence-brazilian-experience/1737) | #81–82, #93 | #2, #53, #86 | — | `#81` The Brazilian bill mirrors the EU AI Act in many aspects, as both texts reflect the OECD's expanded definition of AI systems, encompassing not only decision-ma… |
| [[13]](https://fpf.org/?p=250371) | #21, #41 | #22, #25, #30, #42 | — | `#21` The next milestone came on 2 August 2025, when the rules on general-purpose AI (GPAI) models, the governance framework, confidentiality obligations, and the pr… |
| [[22]](https://techpolicy.press/brazils-ai-law-faces-uncertain-future-as-big-tech-warms-to-trump) | #54, #58, #92, #96 | #49, #84 | — | `#54` the senators created a temporary commission for artificial intelligence that, over 19 months, discussed drafts, held 24 meetings and 14 public hearings, and ga… |
| [[6]](https://www.barbieriadvogados.com/brazil-ai-act/) | #3, #86, #89 | #85, #91 | — | `#3` Chapter III of the Senate text establishes a set of substantive rights that go beyond what the EU AI Act provides directly |
| [[8]](https://www.theregister.com/ai-and-ml/2026/05/07/eu-hits-snooze-on-ai-act-rules-after-industry-backlash/5234530) | #35–36, #38 | #4, #44 | — | `#35` The deal marks a notable rollback in the EU's digital rulebook after years of Brussels proudly marketing itself as the world's tech cop. That has come under mo… |
| [[12]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | #11, #13, #16, #29 | #27 | — | `#11` The AI Act defines 4 levels of risk for AI systems: ### Unacceptable risk All AI systems considered a clear threat to the safety, livelihoods and rights of peo… |
| [[18]](https://eeas.europa.eu/delegations/chile/artificial-intelligence-council-gives-final-green-light-simplify-and-streamline-rules_en) | #46 | #32, #37, #40 | #31 | `#46` we are taking another decisive step towards a more competitive European Union. By providing greater legal certainty and ensuring a more harmonised implementati… |
| [[4]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | #52, #67 | #79 | #1 ⚡ | `#52` que "Dispõe sobre o desenvolvimento, o fomento e o uso ético e responsável da inteligência artificial com base na centralidade da pessoa humana" |
| [[9]](https://www.aosfatos.org/noticias/deputados-da-comissao-da-ia-atuaram-em-prol-de-big-techs-apos-visitas-de-lobistas/) | #70–72 | #4 | — | `#70` A conclusão é baseada em levantamento exclusivo do **Aos Fatos**, que mostra que lobistas de *big techs* visitaram o Congresso brasileiro ao menos 83 vezes ent… |
| [[3]](https://www.aosfatos.org/noticias/aprovada-senado-regulacao-ia-camara/) | #55–56 | #1 | — | `#55` Depois de mais de 500 dias de discussão, o Senado aprovou na última terça-feira (10) o projeto de lei que cria um marco regulatório para a inteligência artific… |
| [[27]](https://cesconbarrieu.com.br/en/senado-aprova-o-marco-legal-da-ia-2/) | #61, #63 | #92 | — | `#61` Systemic risk: the text introduces governance measures for a new risk category: "systemic risk". Unlike "high risk" and "excessive risk" categories, the Bill d… |
| [[30]](https://teletime.com.br/04/05/2026/parlamentares-tentam-retomar-cronograma-para-pl-de-ia/) | — | #73, #88, #90 | — | `#73` A Comissão Especial, presidida pela deputada Luisa Canziani (PSD-PR), ainda não realizou nenhuma reunião este ano. |
| [[7]](https://itsrio.org/wp-content/uploads/2017/01/2025.06.23-Matriz-comparada-de-obrigacoes_-PL-2338_2023-vs.-EU-AI-act_Relatorio_AI-16-jun-1.pdf) | #3, #83 | — | — | `#3` o PL 2.338/2023 adota uma estratégia mais horizontal, de criar obrigações para todos os agentes em pelo menos metade dos casos, enquanto o marco europeu adota… |
| [[10]](https://techcrunch.com/2024/03/13/deal-on-eu-ai-act-gets-thumbs-up-from-european-parliament) | #7 | #6 | — | `#7` However a handful of EU Member States, led by France, pushed in the opposite direction — fuelled by lobbying by homegrown AI startups (such as Mistral) — press… |
| [[14]](https://digital-strategy.ec.europa.eu/en/policies/gpai-code-practice) | — | #24 | #23 ⚡ | `#23` AI Studio Delta - Aleph Alpha - Almawave - Amazon - Anthropic - Black Forest Labs - Bria AI - Cohere - Domyn - Dweve - Fastweb - IBM - LINAGORA - Microsoft - M… |
| [[15]](https://www.euronews.com/2025/07/03/europes-top-ceos-call-for-commission-to-slow-down-on-ai-act) | — | #28, #34 | — | `#28` CEOs from more than 40 European companies including ASML, Philips, Siemens and Mistral, are asking for a “two-year clock-stop” on the AI Act before key obligat… |
| [[21]](https://www.cnnbrasil.com.br/tecnologia/camara-aprova-marco-legal-para-inteligencia-artificial-entenda-implicacoes/) | #48 | #69 | — | `#48` A Câmara dos Deputados aprovou na quarta-feira (29) o marco legal para o uso da inteligência artificial (IA) no Brasil. [...] foi aprovado com 413 votos favorá… |
| [[29]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | — | #80 | #68 | `#80` 37 proposições apensadas |
| [[35]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | #78 | #88 | — | `#78` O **deputado federal Aguinaldo Ribeiro (PP-PB)** informou que a votação do Marco Regulatório de Inteligência Artificial (PL 2338/2023) deve ficar para o final… |
| [[16]](https://digital-strategy.ec.europa.eu/en/library/digital-omnibus-ai-regulation-proposal) | — | — | #29 | — |
| [[19]](https://www.pinsentmasons.com/out-law/news/law-delaying-eu-high-risk-ai-rules-finalised) | — | #32 | — | `#32` The rules on high-risk AI systems, contained in the EU AI Act, were due to come into effect on 2 August 2026. |
| [[20]](https://edri.org/our-work/commissions-digital-omnibus-is-a-major-rollback-of-eu-digital-protections/) | #45 | — | — | `#45` The Digital Omnibus on AI tears the AI Act apart, undermining its key protections, including oversight and transparency mechanisms. Those making or selling AI… |
| [[23]](https://teletime.com.br/06/12/2022/comissao-de-juristas-propoe-criacao-de-autoridade-para-inteligencia-artificial/) | #50 | — | — | `#50` apresentou nesta terça-feira, 6, os substitutivos aos Projetos de Lei (PLs) 5.051/2019, 21/2020 e 872/2021. [...] criação de uma autoridade independente, que s… |
| [[24]](https://institutobrasileiro.ia.br/artigos/pl-2338-2023-onde-esta-o-projeto-de-lei-de-ia/) | #51 | — | — | `#51` O PL 2338/2023 foi apresentado no Senado em 3 de maio de 2023 pelo senador Rodrigo Pacheco (PSD/MG). |
| [[25]](https://agenciabrasil.ebc.com.br/geral/noticia/2024-12/senado-aprova-regras-para-uso-da-inteligencia-artificial) | #57 | — | — | `#57` Durante a tramitação no Senado, foi retirado o dispositivo que considerava como sendo de alto risco os sistemas de IA usados pelas plataformas digitais, as cha… |
| [[28]](https://www.camara.leg.br/noticias/1140392-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil/) | — | #64 | — | `#64` conteúdos protegidos poderão ser utilizados livremente somente por instituições de pesquisa, de jornalismo, museus, arquivos, bibliotecas e organizações educac… |
| [[31]](https://www.cnnbrasil.com.br/politica/avanco-do-pl-da-ia-esbarra-em-decisao-sobre-redata-e-compromisso-do-senado/) | #74 | — | — | `#74` A **CNN** apurou que o clima tensionado entre governo e o presidente do Senado, senador **Davi Alcolumbre** (União-AP), também pesa e desperta temor de que a d… |
| [[32]](https://www.amapadigital.com.br/novo/noticia/10/06/2026-votacao-do-pl-da-inteligencia-artificial-e-adiada-enquanto-camara-busca-consenso-com-o-senado.ghtml) | #75 | — | — | `#75` Nesta terça-feira (9), o presidente da Câmara, Hugo Motta (Republicanos-PB), descartou que a proposta seja votada ainda nesta semana [...] o alinhamento com o… |
| [[33]](https://www.congressoemfoco.com.br/noticia/119344/relator-quer-marco-da-ia-atemporal-para-acompanhar-inovacao) | #76 | — | — | `#76` Não existe hoje uma solução que atenda a todos. Estamos buscando esse caminho, mas o mundo inteiro ainda está aprendendo qual é o melhor modelo para permitir o… |
| [[34]](https://desinformante.com.br/ue-avanca-regulacao-ia-projeto-brasileiro-parado/) | #77 | — | — | `#77` A última polêmica em torno do PL 2338 ocorreu no fim de maio, quando o deputado Aguinaldo Ribeiro, afirmou que pretendia retirar do projeto a classificação dos… |
| [[36]](https://itif.org/publications/2025/12/05/europe-writes-the-rules-and-the-world-pays-the-price/) | — | #94 | — | `#94` This alignment has a price, particularly when adopting rules made without emerging economies in mind. |
| [[37]](https://techpolicy.press/the-dmas-brussels-effect-tested-and-contested-lessons-from-brazil) | #95 | — | — | `#95` the 'Brussels effect' is now being tested and contested [...] Brazilian legislation has drawn on EU-style regulatory models in areas such as data protection (G… |
| [[38]](https://www.cmtradelaw.com/2026/06/ustr-finds-certain-brazilian-practices-in-six-issue-areas-actionable-under-section-301-proposes-25-tariffs-on-brazilian-goods-and-invites-comments/) | — | #97 | — | `#97` finding that certain of Brazil’s acts, policies, and practices are actionable under Sections 301(b) and 304(a) of the Trade Act of 1974. If adopted as proposed… |
| [[39]](https://www.correiodamanha.com.br/mundo/internacional/2026/07/305010-deputados-dos-eua-acionam-trump-contra-regulacao-das-big-techs-no-brasil.html) | — | #97 | — | `#97` Um grupo de 20 deputados dos Estados Unidos cobra ações do presidente Donald Trump contra o projeto que visa a regulação das Big Techs no Brasil |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.consilium.europa.eu/en/policies/artificial-intelligence/timeline-artificial-intelligence/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing a GSC Managed Website Verification successful. Waiting for www.consilium.europa.e
- https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng/pdf — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://eur-lex.europa.eu/eli/reg/2024/1689/2024-07-12/swe/pdf — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-3`** [6] [7]
  - Trecho: They diverge on who bears obligations, what rights individuals hold, how copyright is treated, and how hard sanctions bite.
  - Justificativa: A evidência sustenta as quatro divergências citadas: (1) quem assume obrigações — a estratégia horizontal do PL 2.338 vs. pontual do EU AI Act; (2) direitos individuais — capítulo autônomo no PL 2.338 vs. abordagem indi…
  - Suporte veio de: [6] [7]
  - Evidência: “o PL 2.338/2023 adota uma estratégia mais horizontal, de criar obrigações para todos os agentes em pelo menos metade dos casos, enquanto o marco europeu adota uma estratégia mais pontual, criando obrigações para atores…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | sustenta | Chapter III of the Senate text establishes a set of substantive rights that go beyond what the EU AI Act provides direc… |
    | [7] | sustenta | o PL 2.338/2023 adota uma estratégia mais horizontal, de criar obrigações para todos os agentes em pelo menos metade do… |

- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-7`** [10]
  - Trecho: The December 2023 compromise had weakened Parliament's original plans for general-purpose AI, after France and other member states pushed for a carve-out to protect home-grown start-ups such as Mistral.
  - Justificativa: A evidência sustenta explicitamente todos os elementos essenciais da afirmação: o compromisso de dezembro enffraqueceu ("watered down") a proposta original dos MEPs para GPAIs; um grupo de Estados-membros liderado pela…
  - Suporte veio de: [10]
  - Evidência: “However a handful of EU Member States, led by France, pushed in the opposite direction — fuelled by lobbying by homegrown AI startups (such as Mistral) — pressing for a regulatory carve-out for advanced AI model makers…”
  - Não coberto pela evidência: O ano exato (2023) não é explicitamente mencionado na evidência, que se refere apenas a "December".
- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-11`** [12]
  - Trecho: On that definition it builds four tiers: unacceptable risk (banned), high risk (strict obligations), transparency risk, and minimal risk such as spam filters and AI-enabled video games, which carries no obligations.
  - Justificativa: A evidência confirma explicitamente os quatro níveis de risco do AI Act e suas características conforme descritos na afirmação: risco inaceitável (banido), alto risco (obrigações rigorosas), risco de transparência e ris…
  - Suporte veio de: [12]
  - Evidência: “The AI Act defines 4 levels of risk for AI systems:”
### UNSUPPORTED

- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-2`** [5]
  - Trecho: The two texts share a definition of AI, banned uses, a high-risk list and a tier for powerful general-purpose models.
  - Justificativa: A evidência sustenta três dos quatro elementos da afirmação (definição de IA, usos proibidos e lista de alto risco), mas não menciona em nenhum momento a existência de um 'tier para modelos de propósito geral poderosos'…
  - Suporte veio de: [5]
  - Evidência: “both texts reflect the OECD's expanded definition of AI systems, encompassing not only decision-making but also model creation and data training.”
  - Não coberto pela evidência: a tier for powerful general-purpose models
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-4`** [8] [9]
  - Trecho: Both have been shaped by industry lobbying, US pressure and a growing argument that rules written in 2021–2024 should be slowed before they apply.
  - Justificativa: A afirmacao afirma que 'ambos' (presumivelmente a regulacao de IA da UE e do Brasil) foram moldados por tres fatores: lobby da industria, pressao dos EUA e argumento de que regras escritas em 2021-2024 deveriam ser desa…
  - Suporte veio de: [8] [9]
  - Evidência: “Brussels quietly caved to industry pressure and agreed to simplify and delay key parts of the AI Act”
  - Não coberto pela evidência: Pressao dos EUA sobre a regulacao brasileira de IA — nao ha mencao na evidencia; Periodo especifico '2021-2024' para quando as regras foram escritas — nao mencionado na evidencia; Argumento de que regras brasileiras deveriam ser desaceleradas antes de aplicar — nao explicitado para o Brasil na evidencia
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [8] | parcial | Brussels quietly caved to industry pressure and agreed to simplify and delay key parts of the AI Act |
    | [9] | parcial | lobistas de big techs visitaram o Congresso brasileiro ao menos 83 vezes |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [15] [6] [36] [22] [34] [13] [27] [5] [12] [20] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-6`** [10]
  - Trecho: Parliament approved the text on 13 March 2024 by 523 votes to 46, with 49 abstentions.
  - Justificativa: A evidência confirma os números da votação (523 a favor, 46 contra, 49 abstenções), mas não menciona a data específica de '13 March 2024'. A evidência refere-se apenas a 'Wednesday' e 'today', sem indicar a data exata.…
  - Suporte veio de: [10]
  - Evidência: “MEPs overwhelmingly backed the provisional agreement reached in December in trilogue talks with the Council, with 523 votes in favor vs just 46 against (and 49 abstentions).”
  - Não coberto pela evidência: Data exata: '13 March 2024'
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-1`** [3] [4]
  - Trecho: Brazil's Bill PL 2338/2023, which closely mirrors the EU's risk-based architecture, passed the Senate in December 2024 but has sat in a special committee of the Chamber of Deputies for twenty months with no rapporteur's…
  - Justificativa: A alegação contém múltiplos elementos contraditados pela evidência. (1) O prazo de 'vinte meses' na Comissão Especial da Câmara é claramente refutado: o PL 2338/2023 foi recebido pela Câmara em 17/03/2025 e a Comissão E…
  - Suporte veio de: [3]
  - Evidência: “17/03/2025 | Mesa Diretora ( MESA ) Recebido o Ofício nº 235/2025 do Senado Federal que submete à revisão da Câmara dos Deputados, nos termos do art. 65 da Constituição Federal, o Projeto de Lei n° 2.338, de 2023”
  - Não coberto pela evidência: twenty months in special committee — contradicted; bill arrived at Chamber in March 2025, ~6 months of activity through September 2025; no rapporteur's report — evidence shows a rapporteur was designated (Dep. Aguinaldo Ribeiro on 20/05/2025); no report issuance is confirmed or denied; no substitute text — not addressed in evidence
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | Baseado no modelo da União Europeia, o PL 2.338/2023 cria uma regulação baseada em riscos e prevê a criação de uma auto… |
    | [4] | contradiz | 17/03/2025 \| Mesa Diretora ( MESA ) Recebido o Ofício nº 235/2025 do Senado Federal que submete à revisão da Câmara dos… |

  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência confirma que o PL 2338/2023 é baseado no modelo da UE com regulação por riscos e que foi aprovado no Senado, mas não confirma e…") — cascata: baseline → context_expansion
- **Trecho citado `regulacao_ia_026c7ad6edf4_20261115T040310Z-23`** [14]
  - Trecho: As of October 2026 the Commission lists 22 full signatories, including Amazon, Anthropic, Google, Microsoft, Mistral AI and OpenAI, while xAI signed only the Safety and Security chapter.
  - Justificativa: A evidência lista 21 signatários completos (não 22) e Google não aparece na lista, contradizendo a afirmação. A afirmação sobre xAI estar correto. A data 'October 2026' não consta na evidência.
  - Suporte veio de: [14]
  - Evidência: “AI Studio Delta - Aleph Alpha - Almawave - Amazon - Anthropic - Black Forest Labs - Bria AI - Cohere - Domyn - Dweve - Fastweb - IBM - LINAGORA - Microsoft - Mistral AI - Open Hippo - OpenAI - Pleias - Reflection AI, In…”
  - Não coberto pela evidência: Data 'October 2026' não mencionada na evidência; Contagem de 22 signatários: a evidência lista 21, não 22; Google listado como signatário: não aparece na lista de signatários da evidência

---

## 10. Trechos Citados Não Auditados

Motivos: 15 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `regulacao_ia_026c7ad6edf4_20261115T040310Z-0` — Referencia(s) citada(s) ['3ddfb3d5c962b6de', '929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-5` — Referencia(s) citada(s) ['3ddfb3d5c962b6de'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-8` — Referencia(s) citada(s) ['3ddfb3d5c962b6de', '02ce1ed0145f4f7d'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-9` — Referencia(s) citada(s) ['929c7f3f8857377f', '3ddfb3d5c962b6de'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-10` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-12` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-14` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-15` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-17` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-18` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-19` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-20` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-26` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-43` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_026c7ad6edf4_20261115T040310Z-47` — Referencia(s) citada(s) ['929c7f3f8857377f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.