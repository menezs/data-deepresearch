# Relatório de Auditoria — Gemini (vacinacao_hpv_404ecac735ea_20261025T154427Z)

**Arquivo auditado:** `answers/Gemini/Consolidado/vacinacao_hpv.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_404ecac735ea_20261025T154427Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-04T06:00:14.839502+00:00 |
| **Total de trechos citados** | 67 |
| **Tempo de processamento** | 9:14:15:48 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 27.7 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-10-25 15:45:17+00:00 |
| Citações no corpo | 67 marcadores, 23 distintos |
| Referências listadas | 36 (13 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 24 | 35.8% |
| **UNSUPPORTED** | 28 | 41.8% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 15 | 22.4% |
| **TOTAL** | 67 | 100.0% |

Sobre os 52 trechos citados auditados: SUPPORTED 46,15%, UNSUPPORTED 53,84%, CONTRADICTED 0,00%.

> **12 dos 24 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 12 estão **contados dentro** dos 24 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`30` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `7` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `11` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#7` Na Região Norte, o câncer do colo do útero figura em primeiro lugar na incidência de tumores malignos e representa a ca… | [5] | — | [12] [8] [13] [26] [4] https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/controle-do-cancer-do-colo-do-utero/dados-e-numeros ⚠ |
| `#30` A vacina bivalente confere proteção contra os tipos HPV 16 e 18. | [2] | [21] [26] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [3] [24] [13] [8] [19] | — |
| `#31` A vacina quadrivalente agrega proteção contra os tipos HPV 6 e 11, responsáveis por cerca de 90% das verrugas anogenita… | [2] | [3] [26] [13] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [8] [24] [12] [15] | — |
| `#32` A vacina nonavalente expandiu a cobertura imunológica ao incorporar proteção contra outros cinco genótipos oncogênicos… | [2] | https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [3] [26] [13] [12] [21] [8] [5] [10] | — |
| `#42` Em 2014, respaldada por ensaios de imunogenicidade que demonstravam respostas de anticorpos não inferiores em adolescen… | [19] | [24] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [3] [26] [20] [22] [25] | — |
| `#44` O ensaio clínico DoRIS realizado na Tanzânia, o estudo KEN SHE conduzido no Quênia, o acompanhamento de dez anos de coo… | [20] | [3] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [21] [24] [2] [26] [22] | — |
| `#45` A eficácia observada da dose única contra a infecção persistente pelos tipos vacinais permaneceu acima de 97%, com proj… | [21] | [3] [24] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [26] [19] [2] [20] | — |
| `#46` Respaldada por uma revisão minuciosa empreendida pelo Strategic Advisory Group of Experts on Immunization (SAGE) em abr… | [22] | [23] https://www.linkedimmunisation.org/resources/human-papillomavirus-vaccines-who-position-paper-december-2022/ https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [3] [24] [26] [19] [32] [13] [20] [2] | — |
| `#49` Sob a perspectiva da saúde global, a redução do consumo de doses por indivíduo alivia as restrições históricas de ofert… | [19] | [26] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [8] [3] [21] [2] [13] [5] [24] | — |
| `#59` No ano de 2024, a Comissão Nacional de Incorporação de Tecnologias no Sistema Único de Saúde recomendou a incorporação… | [29] | [4] [8] [12] [26] https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490 [13] [25] [10] | — |
| `#60` Em agosto de 2020, a Assembleia Mundial da Saúde aprovou formalmente a Estratégia Global para Acelerar a Eliminação do… | [30] | [31] [3] [12] [1] [8] [26] [32] [21] [25] [13] [24] [23] | — |
| `#64` O terceiro pilar exige que 90% das mulheres identificadas com alterações cervicais recebam tratamento adequado, o que a… | [3] | [32] [24] [21] [31] [30] [12] [26] [8] [1] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 769655 |
| **Média de tokens por requisição** | 14801.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 13/36 (36.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[9]](https://iris.who.int/bitstreams/d63ca5e2-a966-41a8-9fc2-c4e2ff4efc14/download) | error | 11 | 0 | 0 | 0 | 11 |
| [[2]](https://ourworldindata.org/hpv-vaccination-world-can-eliminate-cervical-cancer) | downloaded | 9 | 1 | 4 | 4 | 0 |
| [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12411824/) | downloaded | 7 | 6 | 1 | 0 | 0 |
| [[8]](https://observatoriodeoncologia.com.br/indicadores/2024/indicadores-de-colo-do-utero/) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[18]](https://pubmed.ncbi.nlm.nih.gov/42309117/) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[19]](https://view-hub.org/topics/single-dose-hpv) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[25]](https://portal.conasems.org.br/orientacoes-tecnicas/noticias/6269_ministerio-da-saude-adota-esquema-de-vacinacao-em-dose-unica-contra-o-hpv) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[4]](https://www.inaff.org.br/noticias/em-2025-cancer-de-colo-do-utero-matou-7-240-mulheres-no-brasil/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[5]](https://www.gov.br/inca/pt-br/assuntos/noticias/2026/inca-estima-781-mil-novos-casos-de-cancer-por-ano-no-brasil-entre-2026-e-2028) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[6]](https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22setembro2022.pdf) | dead | 2 | 0 | 0 | 0 | 2 |
| [[7]](https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22marco2023.pdf) | dead | 2 | 0 | 0 | 0 | 2 |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/34741816/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[20]](https://www.path.org/who-we-are/programs/center-for-vaccine-innovation-and-access/single-dose-hpv-vaccine-evaluation-consortium/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[24]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11555274/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[28]](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hpv/notas-tecnicas) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[30]](https://www.who.int/publications/i/item/9789240014107) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[1]](https://www.paho.org/pt/node/76247) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/32997908/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://www.hpvworld.com/articles/hpv-vaccination-and-the-risk-of-invasive-cervical-cancer/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[16]](https://news.ki.se/hpv-vaccine-effective-against-cervical-cancer) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://vaccinesbeat.org/updated-guidelines-for-global-strategy-to-accelerate-the-elimination-of-cervical-cancer-as-a-public-health-problem/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[22]](https://www.iccp-portal.org/news/human-papillomavirus-vaccines-who-position-paper-2022-update) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[29]](https://www.gov.br/conitec/pt-br/midias/relatorios/2024/testagem-molecular-para-deteccao-de-hpv-e-rastreamento-do-cancer-do-colo-do-utero) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[10]](https://revistakdea360.com.br/noticia/93648/cancer-do-colo-do-utero-brasil-deve-registrar-19-mil-novos-casos-por-ano-ate-2028) | downloaded | 0 · nunca citada | — | — | — | — |
| [[12]](https://mulherconsciente.com.br/dia-a-dia-com-saude/o-cancer-do-colo-do-utero-no-brasil/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[13]](https://saude.es.gov.br/Media/sesa/DANTS/Boletim%20Epidemiol%C3%B3gico%20sobre%20C%C3%A2ncer%20do%20Colo%20do%20%C3%9Atero.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[17]](https://www.bmj.com/content/375/bmj.n2689) | blocked | 0 · nunca citada | — | — | — | — |
| [[23]](https://www.who.int/publications/i/item/who-wer9750-645-672) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2024/nota-tecnica-no-41-2024-cgici-dpni-svsa-ms) | downloaded | 0 · nunca citada | — | — | — | — |
| [[27]](https://bvsms.saude.gov.br/pni-adota-dose-unica-para-a-vacinacao-de-pessoas-de-9-a-14-anos-de-idade-contra-o-hpv/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://www.paho.org/en/documents/global-strategy-accelerate-elimination-cervical-cancer-public-health-problem-and-its) | downloaded | 0 · nunca citada | — | — | — | — |
| [[32]](https://www.who.int/initiatives/cervical-cancer-elimination-initiative) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/controle-do-cancer-do-colo-do-utero/dados-e-numeros](https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/controle-do-cancer-do-colo-do-utero/dados-e-numeros) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490](https://saude.df.gov.br/documents/37101/0/Atualiza%C3%A7%C3%A3o+das+recomenda%C3%A7%C3%B5es+da+vacina%C3%A7%C3%A3o+contra+HPV+no+Brasil.pdf/06764bc0-ab94-6a92-3eba-0e0bc49a2d36?t=1722000113490) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.linkedimmunisation.org/resources/human-papillomavirus-vaccines-who-position-paper-december-2022/](https://www.linkedimmunisation.org/resources/human-papillomavirus-vaccines-who-position-paper-december-2022/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[36]](https://medicinecentral.co.uk/article/hpv-vaccination-cervical-cancer-mortality) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://ourworldindata.org/hpv-vaccination-world-can-eliminate-cervical-cancer) | #1 | #16–17, #31–32 | #15, #18–19, #30 | `#1` It's estimated that there were more than 660,000 new cases of cervical cancer and around 350,000 deaths globally in 2022. |
| [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12411824/) | #2–3, #24, #61–63 | #64 | — | `#2` The burden of this disease is particularly pronounced in low‐ and middle‐income countries (LMICs), where both incidence and mortality rates are significantly h… |
| [[8]](https://observatoriodeoncologia.com.br/indicadores/2024/indicadores-de-colo-do-utero/) | — | #9, #21–23 | — | `#9` As regiões com mais centros de tratamento em 2022 foram Sudeste (48%), Sul (24%) e Nordeste (18%) e as que mais aumentaram a quantidade de centros foram Sudest… |
| [[18]](https://pubmed.ncbi.nlm.nih.gov/42309117/) | #37–40 | — | — | `#37` Cervical cancer mortality trends following HPV vaccination in England, 2001-24: an analysis of population-based mortality data. Sasieni P(1), Falcaro M(2). [..… |
| [[19]](https://view-hub.org/topics/single-dose-hpv) | #47 | #42, #48–49 | — | `#47` In December 2022, the WHO updated its position paper on HPV vaccination to include a single-dose schedule as an off-label alternative for girls and boys betwee… |
| [[25]](https://portal.conasems.org.br/orientacoes-tecnicas/noticias/6269_ministerio-da-saude-adota-esquema-de-vacinacao-em-dose-unica-contra-o-hpv) | — | #50–52 | — | `#50` A mudança foi publicada em Nota Técnica nesta segunda-feira (1º). |
| [[4]](https://www.inaff.org.br/noticias/em-2025-cancer-de-colo-do-utero-matou-7-240-mulheres-no-brasil/) | #4 | #6 | — | `#4` O Inca prevê 19, 3 mil casos novos por ano até 2028 [...] Baseando-se em dados disponibilizados pelo Instituto Nacional de Câncer (Inca) , a estimativa é de 19… |
| [[5]](https://www.gov.br/inca/pt-br/assuntos/noticias/2026/inca-estima-781-mil-novos-casos-de-cancer-por-ano-no-brasil-entre-2026-e-2028) | #5 | #7 | — | `#5` Entre as mulheres, em ordem de incidência, predominam os cânceres de mama, cólon e reto, colo do útero, pulmão e tireoide. [...] Colo do útero (7,4%) [...] O B… |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/34741816/) | #36 | — | #20 | `#36` Falcaro M(1), Castañon A(1), Ndlela B(2)... 1. Lancet. 2021 Dec 4;398(10316):2084-2092... The estimated relative reduction in cervical cancer rates by age at v… |
| [[20]](https://www.path.org/who-we-are/programs/center-for-vaccine-innovation-and-access/single-dose-hpv-vaccine-evaluation-consortium/) | #43 | #44 | — | `#43` Since 2018, the Single-Dose HPV Vaccine Evaluation Consortium, coordinated by PATH, has gathered and evaluated data from clinical trials, observational studies… |
| [[24]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11555274/) | — | #55, #66 | — | `#55` As of April 2024, a total of 40 countries have included a single-dose HPV vaccination strategy in their immunization programs |
| [[28]](https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hpv/notas-tecnicas) | — | — | #53–54 | — |
| [[30]](https://www.who.int/publications/i/item/9789240014107) | — | #60, #65 | — | `#60` Global strategy to accelerate the elimination of cervical cancer as a public health problem |
| [[1]](https://www.paho.org/pt/node/76247) | #0 | — | — | `#0` Yet it remains one of the most common cancers and causes of cancer-related death in women across the globe. |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/32997908/) | #33 | — | — | `#33` We used nationwide Swedish demographic and health registers to follow an open population of 1,672,983 girls and women who were 10 to 30 years of age from 2006… |
| [[15]](https://www.hpvworld.com/articles/hpv-vaccination-and-the-risk-of-invasive-cervical-cancer/) | #34 | — | — | `#34` Overall, this corresponds to a 63% lower risk of invasive cervical cancer associated with HPV vaccination in Swedish girls and women 10 to 30 years old |
| [[16]](https://news.ki.se/hpv-vaccine-effective-against-cervical-cancer) | #35 | — | — | `#35` girls vaccinated before age 17 reduced their risk of cervical cancer by 88 percent. Women vaccinated between ages 17 and 30 halved their risk of cervical cance… |
| [[21]](https://vaccinesbeat.org/updated-guidelines-for-global-strategy-to-accelerate-the-elimination-of-cervical-cancer-as-a-public-health-problem/) | — | #45 | — | `#45` A single dose of HPV vaccine has shown approximately 92% efficacy against persistent HPV types 16 and 18 infection |
| [[22]](https://www.iccp-portal.org/news/human-papillomavirus-vaccines-who-position-paper-2022-update) | — | #46 | — | `#46` The World Health Organization updated its recommendations for the human papillomavirus (HPV) vaccine in a position paper published in December 2022. |
| [[29]](https://www.gov.br/conitec/pt-br/midias/relatorios/2024/testagem-molecular-para-deteccao-de-hpv-e-rastreamento-do-cancer-do-colo-do-utero) | — | #59 | — | `#59` Relatório de Recomendação nº 878 - Testagem Molecular para Detecção de HPV e rastreamento do câncer do colo do útero |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22setembro2022.pdf — Referencia nao encontrada (404): https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22setembro2022.pdf
- https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22marco2023.pdf — Referencia nao encontrada (404): https://www.inca.gov.br/sites/ufu.sti.inca.local/files/media/document/dados_e_numeros_colo_22marco2023.pdf

### Bloqueadas por barreira de acesso

- https://www.bmj.com/content/375/bmj.n2689 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-0`** [1]
  - Trecho: O câncer do colo do útero, também denominado neoplasia cérvico-vaginal, permanece como um dos maiores desafios de saúde pública global, figurando entre as principais causas de morbimortalidade por neoplasias na populaçã…
  - Justificativa: A evidência afirma explicitamente que o câncer do colo do útero permanece como um dos cânceres mais comuns e causas de morte por câncer em mulheres no mundo, sustentando a afirmação central do trecho sobre morbimortalid…
  - Suporte veio de: [1]
  - Evidência: “Yet it remains one of the most common cancers and causes of cancer-related death in women across the globe.”
  - Não coberto pela evidência: A denominação alternativa 'neoplasia cérvico-vaginal' não é mencionada na evidência.
- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-1`** [2]
  - Trecho: Estimativas internacionais indicam que, no ano de 2022, foram registrados aproximadamente 660.000 novos casos e cerca de 350.000 óbitos decorrentes dessa enfermidade em todo o planeta.
  - Justificativa: A evidência afirma explicitamente que houve mais de 660.000 novos casos e cerca de 350.000 mortes por câncer cervical globalmente em 2022, o que corresponde diretamente à afirmação do trecho.
  - Suporte veio de: [2]
  - Evidência: “It's estimated that there were more than 660,000 new cases of cervical cancer and around 350,000 deaths globally in 2022.”
- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-2`** [3]
  - Trecho: Trata-se de uma patologia marcada por profundas iniquidades socioeconômicas, na qual os países de baixa e média renda suportam a maior fatia da carga da doença, registrando taxas de incidência de 17,8 casos por 100 mil…
  - Justificativa: A evidência do trecho principal (score=0.789) sustenta explicitamente todos os elementos da afirmação: as iniquidades socioeconômicas, a maior carga em países de baixa e média renda, e os números exatos de incidência (1…
  - Suporte veio de: [3]
  - Evidência: “The burden of this disease is particularly pronounced in low‐ and middle‐income countries (LMICs), where both incidence and mortality rates are significantly higher than the global average: 17.8 new cases per 100 000 wo…”
### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-6`** [4]
  - Trecho: No que tange à mortalidade, dados do Sistema de Informações sobre Mortalidade revelaram que, somente no ano de 2025, o câncer do colo do útero foi a causa direta do óbito de 7.240 mulheres no território nacional.
  - Justificativa: A evidência menciona que o câncer de colo do útero 'matou 20 mulheres por dia no Brasil em 2025', segundo 'dados preliminares do Ministério da Saúde'. O número exato de 7.240 óbitos não aparece na evidência (20/dia × 36…
  - Suporte veio de: [4]
  - Não coberto pela evidência: Número exato de 7.240 óbitos (a evidência menciona 20/dia, que resulta em ~7.300/ano, não 7.240); Fonte 'Sistema de Informações sobre Mortalidade' (a evidência cita 'dados preliminares do Ministério da Saúde'); Expressão 'causa direta do óbito'
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-7`** [5]
  - Trecho: Na Região Norte, o câncer do colo do útero figura em primeiro lugar na incidência de tumores malignos e representa a causa primária de morte por neoplasias na população feminina, sendo responsável por 15,4% do total de…
  - Justificativa: A evidência apenas afirma que o câncer do colo do útero está 'entre os mais incidentes no Norte e Nordeste', sem confirmar que ocupa o primeiro lugar em incidência, que é a causa primária de morte por neoplasias na popu…
  - Suporte veio de: [5]
  - Não coberto pela evidência: Câncer do colo do útero figura em primeiro lugar na incidência de tumores malignos na Região Norte; Representa a causa primária de morte por neoplasias na população feminina da Região Norte; Responsável por 15,4% do total de óbitos por câncer em mulheres nessa localidade
  - Verificação: UNSUPPORTED (não confirmado); afirmação contradita por outra fonte: [12] [8] [13] [26] [4] ad27a2f34b59bf21 — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_404ecac735ea_20261025T154427Z-9`** [8]
  - Trecho: Em 2022, a distribuição dos centros especializados de tratamento oncologicamente estruturados no Brasil revelava uma forte concentração no Sudeste, que sediava 48% das unidades, e no Sul, com 24%, enquanto o Nordeste de…
  - Justificativa: A evidência confirma os percentuais de centros de tratamento em 2022 para Sudeste (48%), Sul (24%) e Nordeste (18%). Porém, a afirmação sobre a Região Norte sofrer com 'escassez de infraestrutura e severos obstáculos ge…
  - Suporte veio de: [8]
  - Evidência: “As regiões com mais centros de tratamento em 2022 foram Sudeste (48%), Sul (24%) e Nordeste (18%)”
  - Não coberto pela evidência: Região Norte sofria com escassez de infraestrutura; severos obstáculos geográficos para o deslocamento de pacientes; centros especializados de tratamento oncologicamente estruturados (a evidência fala apenas em 'centros de tratamento')
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 11 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 4 citam referência não baixada/inacessível.

- `vacinacao_hpv_404ecac735ea_20261025T154427Z-8` — Referencia(s) citada(s) ['8b883383264ea1b9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-10` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-11` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-12` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-13` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-14` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-25` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-26` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-27` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-28` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-29` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-41` — Referencia(s) citada(s) ['66f6d6c55caf05cc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-56` — Referencia(s) citada(s) ['4ea2c404dfeca66b'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-57` — Referencia(s) citada(s) ['8b883383264ea1b9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_404ecac735ea_20261025T154427Z-58` — Referencia(s) citada(s) ['4ea2c404dfeca66b'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).