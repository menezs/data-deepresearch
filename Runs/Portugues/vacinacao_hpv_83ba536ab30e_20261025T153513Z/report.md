# Relatório de Auditoria — Claude (vacinacao_hpv_83ba536ab30e_20261025T153513Z)

**Arquivo auditado:** `answers/Claude/Consolidado/vacinacao_hpv.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_83ba536ab30e_20261025T153513Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-18T10:36:36.011775+00:00 |
| **Total de trechos citados** | 88 |
| **Tempo de processamento** | 9:12:03:34 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 29.7 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 91 marcadores, 44 distintos |
| Referências listadas | 44 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 65 | 73.9% |
| **UNSUPPORTED** | 11 | 12.5% |
| **CONTRADICTED** | 1 | 1.1% |
| **SKIPPED** | 11 | 12.5% |
| **TOTAL** | 88 | 100.0% |

Sobre os 77 trechos citados auditados: SUPPORTED 84,41%, UNSUPPORTED 14,28%, CONTRADICTED 1,29%.

> **5 dos 65 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 5 estão **contados dentro** dos 65 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`11` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `0` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `5` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#11` As vacinas de espectro mais amplo, como a nonavalente, podem proteger contra os tipos que causam até 90% dos casos. | [9] | [10] [39] [29] [34] [40] [30] [38] [7] | — |
| `#72` A vacina é profilática: não elimina infecções já instaladas e tem pouco efeito em mulheres adultas já expostas. | [13] | [39] [27] [10] [14] [34] [4] [3] [38] [40] [29] [25] | — |
| `#75` **Desigualdades regionais.** O peso maior da doença no Norte e no Nordeste mostra que médias nacionais podem esconder b… | [4] | [44] [39] [5] [26] [1] [30] [32] [33] [43] [38] [31] | — |
| `#82` vacina gratuita para meninas e meninos; - dose única adotada em 2024; - produção nacional e cobertura acima de 80% entr… | [35] | [39] [36] [37] [4] [26] [34] [31] [30] [8] [32] [7] | — |
| `#87` Ela exige sustentar coberturas altas e homogêneas em todo o território, enfrentar a desinformação, concluir a implantaç… | [6] | [5] [8] [39] [44] [26] [4] [32] [43] [7] [1] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 415377 |
| **Média de tokens por requisição** | 5394.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/44 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 2.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[39]](https://www.bemparana.com.br/bem-estar/vacinacao-contra-hpv-reduz-infeccao-mesmo-entre-mulheres-nao-imunizadas-aponta-estudo-brasileiro/) | downloaded | 6 | 6 | 0 | 0 | 0 |
| [[7]](https://medicinasa.com.br/?p=169920) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[16]](https://consumer.healthday.com/substantial-decline-in-cervical-ca-cin3-after-hpv-vaccination-2655486099.html) | downloaded | 4 | 0 | 0 | 4 | 0 |
| [[26]](https://www.who.int/news-room/fact-sheets/detail/immunization-coverage) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[4]](https://medicinasa.com.br/?p=154047) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[6]](https://who.int/publications/i/item/9789240014107) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[8]](https://www.intramed.net/content/fundacao-do-cancer-divulgou-nova-versao-do-guia-sobre-prevencao-e-rastreamento-do-cancer-de-colo-do-utero) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[10]](https://link.springer.com/10.1038/s41591-023-02658-0) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[14]](https://news.ki.se/hpv-vaccine-effective-against-cervical-cancer) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[20]](https://www.sydney.edu.au/news-opinion/news/2025/11/20/australia-on-track-to-eliminating-cervical-cancer.html) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[22]](https://www.who.int/news/item/20-12-2022-who-updates-recommendations-on-hpv-vaccination-schedule) | downloaded | 3 | 2 | 0 | 0 | 1 |
| [[35]](https://www.poder360.com.br/poder-saude/saude-amplia-prazo-para-vacinacao-contra-o-hpv-ate-dezembro/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[38]](https://www.opovo.com.br/noticias/saude/2026/07/24/amp/pesquisa-mostra-que-vacinacao-diminuiu-prevalencia-de-hpv-entre-jovens.html) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[42]](https://www.parana.pr.gov.br/aen/Noticia/Parana-inicia-implementacao-de-teste-inovador-para-rastrear-cancer-do-colo-do-utero) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[1]](https://www.who.int/news-room/fact-sheets/detail/human-papillomavirus-(hpv)-and-cervical-cancer) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[5]](https://www.febrasgo.org.br/wp-content/uploads/2026/01/Pacto-Nacional-Cancer.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[11]](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009069.pub3/pdf/CDSR/CD009069/CD009069_abstract.pdf) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[12]](https://mdedge.com/content/cochrane-report-hpv-vaccine-proves-its-worth-adolescent-young-adult-women) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[13]](https://oalib-perpustakaan.upi.edu/Record/doaj_4e874a61a70a4f4fa1fc761eea178a97/Description) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[15]](https://ascopost.com/news/october-2020/swedish-study-of-hpv-vaccination-and-risk-of-invasive-cervical-cancer/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[18]](https://publichealthscotland.scot/news/2024/january/no-cervical-cancer-cases-detected-in-vaccinated-women-following-hpv-immunisation/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://immattersacp.org/weekly/archives/2025/12/09/1.htm) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[25]](https://dceg.cancer.gov/research/cancer-types/cervix/escuddo) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[27]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[29]](https://www.scielo.br/j/rimtsp/a/KKmPv7mZ39YXfpkfBNTqm5Q/?lang=en) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[31]](https://publichealth.jhu.edu/ivac/2026/latest-global-immunization-coverage-estimates-illustrate-gaps-in-vaccine-access) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[36]](https://www.tnh1.com.br/noticia/nid/ministerio-da-saude-amplia-prazo-de-resgate-vacinal-contra-o-hpv-ate-2026/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[2]](https://www.who.int/initiatives/cervical-cancer-elimination-initiative/cervical-cancer-forum) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[3]](https://www.bemparana.com.br/bem-estar/parana-deve-registrar-mais-de-2-mil-novos-casos-de-cancer-de-utero-e-ovario-em-2026/amp/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://unicef.org/stories/fast-facts-hpv-cervical-cancer) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[17]](https://researchexchange.ocrahope.org/papers/s0140-6736-21-02178-4) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[19]](https://pulsetoday.co.uk/?p=142882) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[21]](https://tri.edu.au/node/6103) | error | 1 | 0 | 0 | 0 | 1 |
| [[23]](https://www.massgeneral.org/news/research-spotlight/research-spotlight-single-dose-of-hpv-is-highly-efficacious-in-protecting-young-women) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[28]](https://english.prescrire.org/en/81/168/52232/0/About.aspx) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://www.aosfatos.org/noticias/como-desinformacao-provocou-rejeicao-de-jovens-vacina-contra-hpv-no-acre/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://data.unicef.org/topic/child-health/immunization/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.gavi.org/vaccineswork/state-global-immunisation-eight-charts) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://www.conass.org.br/?p=7417) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://www.parana.pr.gov.br/aen/Noticia/Saude-intensifica-vacinacao-contra-HPV-passando-abranger-adolescentes-de-15-19-anos) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://portal.afya.com.br/saude/vacinacao-contra-o-hpv-reduz-prevalencia-da-doenca-entre-jovens) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.ocafezinho.com/2026/04/14/sus-implementa-teste-molecular-de-hpv-como-estrategia-principal-de-rastreamento-do-cancer-do-colo-do-utero/amp/) | dead | 1 | 0 | 0 | 0 | 1 |
| [[43]](https://portalelegis.alesc.sc.gov.br/documentos/ZLkQ7) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[44]](https://futurodasaude.com.br/inca-estimativas-cancer-2026-2028/) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[39]](https://www.bemparana.com.br/bem-estar/vacinacao-contra-hpv-reduz-infeccao-mesmo-entre-mulheres-nao-imunizadas-aponta-estudo-brasileiro/) | #55–56, #59, #61–62, #83 | — | — | `#55` Entre as mulheres vacinadas, a prevalência dos tipos de HPV cobertos pela vacina caiu 81% em relação ao período anterior à vacinação (de 15,6% para 3,1%). |
| [[7]](https://medicinasa.com.br/?p=169920) | #8, #10, #67, #74 | — | — | `#8` A vacinação, no entanto, não substitui o rastreamento, já que não oferece proteção contra todos os tipos do HPV associados ao câncer. A vacina oferecida pelo S… |
| [[16]](https://consumer.healthday.com/substantial-decline-in-cervical-ca-cin3-after-hpv-vaccination-2655486099.html) | — | — | #19–20, #71, #78 | — |
| [[26]](https://www.who.int/news-room/fact-sheets/detail/immunization-coverage) | #33, #40–41, #45 | — | — | `#33` By end 2025, 93 countries used a 1-dose schedule, and globally more than 85% of girls aged 9–14 years vaccinated that year were on a single dose schedule. |
| [[4]](https://medicinasa.com.br/?p=154047) | #4, #86 | #75 | — | `#4` O câncer do colo do útero é o segundo mais incidente entre as mulheres nas regiões Norte e Nordeste, enquanto no Sudeste ocupa a quinta posição. |
| [[6]](https://who.int/publications/i/item/9789240014107) | #6–7 | #87 | — | `#6` 90% of girls fully vaccinated with HPV vaccine by age 15 years; 70% of women are screened with a high-performance test by 35 years of age and again by 45 years… |
| [[8]](https://www.intramed.net/content/fundacao-do-cancer-divulgou-nova-versao-do-guia-sobre-prevencao-e-rastreamento-do-cancer-de-colo-do-utero) | #9, #65–66 | — | — | `#9` Quando o teste aponta infecção pelos tipos 16 ou 18 — responsáveis por cerca de 70% dos casos de câncer do colo do útero — a recomendação é encaminhar a pacien… |
| [[10]](https://link.springer.com/10.1038/s41591-023-02658-0) | #12, #30 | #73 | — | `#12` The vaccine virus-like-particle (VLP) structure, which self-assembles to mimic the live virus without the replicating DNA, generates strong immunity with a sin… |
| [[14]](https://news.ki.se/hpv-vaccine-effective-against-cervical-cancer) | #16, #18, #77 | — | — | `#16` This is the first time that we, on a population level, are able to show that HPV vaccination is protective not only against cellular changes that can be precur… |
| [[20]](https://www.sydney.edu.au/news-opinion/news/2025/11/20/australia-on-track-to-eliminating-cervical-cancer.html) | #24, #26, #76 | — | — | `#24` It found there was not a single documented case of cervical cancer among women under 25 across Australia in 2021 – the latest available data – demonstrating th… |
| [[22]](https://www.who.int/news/item/20-12-2022-who-updates-recommendations-on-hpv-vaccination-schedule) | #27–28 | — | #80 (pulado) | `#27` WHO now recommends: - A one or two-dose schedule for girls aged 9-14 years - A one or two-dose schedule for girls and women aged 15-20 years [...] The position… |
| [[35]](https://www.poder360.com.br/poder-saude/saude-amplia-prazo-para-vacinacao-contra-o-hpv-ate-dezembro/) | #49–50 | #82 | — | `#49` Em 2024, o Brasil atingiu mais de 82% de cobertura vacinal entre meninas de 9 a 14 anos, índice acima da média global, de só 37%, segundo dados da OMS (Organiz… |
| [[38]](https://www.opovo.com.br/noticias/saude/2026/07/24/amp/pesquisa-mostra-que-vacinacao-diminuiu-prevalencia-de-hpv-entre-jovens.html) | #54, #57–58 | — | — | `#54` Nos dois períodos, o foco foram os jovens de 16 a 25 anos, como explica a médica epidemiologista e líder da pesquisa Eliana Wendland: "Essa faixa etária é a qu… |
| [[42]](https://www.parana.pr.gov.br/aen/Noticia/Parana-inicia-implementacao-de-teste-inovador-para-rastrear-cancer-do-colo-do-utero) | #64, #68, #84 | — | — | `#64` O teste de DNA-HPV, no entanto, detecta diretamente a presença do HPV, permitindo identificar a infecção antes das alterações celulares. |
| [[1]](https://www.who.int/news-room/fact-sheets/detail/human-papillomavirus-(hpv)-and-cervical-cancer) | #1 | — | #0 | `#1` Women living with HIV are six times more likely to develop cervical cancer compared to the general population |
| [[5]](https://www.febrasgo.org.br/wp-content/uploads/2026/01/Pacto-Nacional-Cancer.pdf) | #5, #85 | — | — | `#5` estima-se que ocorram 19.310 novos casos por ano no triênio 2026–2028, com um risco de 17,59 casos a cada 100.000 mulheres. |
| [[13]](https://oalib-perpustakaan.upi.edu/Record/doaj_4e874a61a70a4f4fa1fc761eea178a97/Description) | #15 | #72 | — | `#15` No protection against cervical precancer was found in mid-adult women unselected by HPV DNA status at enrollment. |
| [[15]](https://ascopost.com/news/october-2020/swedish-study-of-hpv-vaccination-and-risk-of-invasive-cervical-cancer/) | #17 | #71 | — | `#17` the fully adjusted incidence rate ratios for cervical cancer were 0.12 (95% CI = 0.00–0.34) among women vaccinated before age 17 and 0.47 (95% CI = 0.27–0.75)… |
| [[18]](https://publichealthscotland.scot/news/2024/january/no-cervical-cancer-cases-detected-in-vaccinated-women-following-hpv-immunisation/) | #22, #79 | — | — | `#22` no cervical cancer cases have been detected in fully vaccinated women following the human papillomavirus (HPV) immunisation at age 12-13 since the programme st… |
| [[25]](https://dceg.cancer.gov/research/cancer-types/cervix/escuddo) | #32 | #73 | — | `#32` The trial results were published in December 2025, showing non-inferiority of one dose, compared to two doses. |
| [[27]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | #36, #81 | — | — | `#36` Since licensure of HPV vaccines, GACVS has found no new adverse events of concern based on many very large, high quality studies. |
| [[29]](https://www.scielo.br/j/rimtsp/a/KKmPv7mZ39YXfpkfBNTqm5Q/?lang=en) | #38, #47 | — | — | `#38` In the second semester of 2014, the vaccine coverage dropped continuously until the end of that year, the national mean coverage of the second HPV vaccine dose… |
| [[31]](https://publichealth.jhu.edu/ivac/2026/latest-global-immunization-coverage-estimates-illustrate-gaps-in-vaccine-access) | #42, #44 | — | — | `#42` 15 countries introduced HPV vaccines into their nationwide immunization programs in 2025, including China, greatly increasing access. |
| [[36]](https://www.tnh1.com.br/noticia/nid/ministerio-da-saude-amplia-prazo-de-resgate-vacinal-contra-o-hpv-ate-2026/) | #51 | — | #52 ⚡ | `#51` Ministério da Saúde prorrogou até o primeiro semestre de 2026 a estratégia de resgate vacinal contra o HPV destinada a jovens de 15 a 19 anos que não receberam… |
| [[3]](https://www.bemparana.com.br/bem-estar/parana-deve-registrar-mais-de-2-mil-novos-casos-de-cancer-de-utero-e-ovario-em-2026/amp/) | #3 | — | — | `#3` O dado oficial mais recente registra 7.493 mortes por câncer do colo do útero no Brasil em 2024. |
| [[9]](https://unicef.org/stories/fast-facts-hpv-cervical-cancer) | — | #11 | — | `#11` HPV vaccines can protect against up to 90 per cent of cervical cancer cases. |
| [[23]](https://www.massgeneral.org/news/research-spotlight/research-spotlight-single-dose-of-hpv-is-highly-efficacious-in-protecting-young-women) | — | — | #29 | — |
| [[28]](https://english.prescrire.org/en/81/168/52232/0/About.aspx) | #37 | — | — | `#37` A statistically significant association was identified between Guillain-Barré syndrome and HPV vaccine: 1 to 2 additional cases per year per 100 000 vaccinees.… |
| [[30]](https://www.aosfatos.org/noticias/como-desinformacao-provocou-rejeicao-de-jovens-vacina-contra-hpv-no-acre/) | #39 | — | — | `#39` A coordenadora do núcleo do PNI (Programa Nacional de Imunizações do Ministério da Saúde) no Acre, Renata Quiles, também não descarta a possibilidade de que a… |
| [[32]](https://data.unicef.org/topic/child-health/immunization/) | #43 | — | — | `#43` only 33 per cent of girls received the first dose of HPV vaccine (HPV1), and just 31 per cent received the final dose (HPVc). |
| [[33]](https://www.gavi.org/vaccineswork/state-global-immunisation-eight-charts) | #46 | — | — | `#46` In these countries, coverage with a first dose currently stands at 29%. |
| [[34]](https://www.conass.org.br/?p=7417) | #48 | — | — | `#48` O Brasil será o primeiro país da América Latina e o sétimo do mundo a oferecer a vacina contra o HPV para meninos em programas nacionais de imunizações. |
| [[37]](https://www.parana.pr.gov.br/aen/Noticia/Saude-intensifica-vacinacao-contra-HPV-passando-abranger-adolescentes-de-15-19-anos) | #53 | — | — | `#53` outros grupos populacionais também podem se vacinar, como pessoas que vivem com HIV, transplantados de órgãos sólidos, de medula óssea ou pacientes oncológicos… |
| [[40]](https://portal.afya.com.br/saude/vacinacao-contra-o-hpv-reduz-prevalencia-da-doenca-entre-jovens) | #60 | — | — | `#60` O estudo não encontrou diferença na prevalência entre participantes vacinados com uma, duas ou três doses, resultado que sustenta a eficácia do esquema atual d… |
| [[43]](https://portalelegis.alesc.sc.gov.br/documentos/ZLkQ7) | #69 | — | — | `#69` Pessoas imunossuprimidas devem realizar o teste trienalmente. |
| [[44]](https://futurodasaude.com.br/inca-estimativas-cancer-2026-2028/) | #70 | — | — | `#70` A presidente de honra da Sociedade Brasileira de Oncologia Clínica (SBOC), Angélica Nogueira, destaca as projeções de câncer do colo do útero e de cólon e reto… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.ocafezinho.com/2026/04/14/sus-implementa-teste-molecular-de-hpv-como-estrategia-principal-de-rastreamento-do-cancer-do-colo-do-utero/amp/ — Referencia nao encontrada (404): https://www.ocafezinho.com/2026/04/14/sus-implementa-teste-molecular-de-hpv-como-estrategia-principal-de-rastreamento-do-cancer-do-colo-do-utero/amp/

### Inacessíveis (403/timeout/SSL)

- https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009069.pub3/pdf/CDSR/CD009069/CD009069_abstract.pdf — HTTP 403 em https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD009069.pub3/pdf/CDSR/CD009069/CD009069_abstract.pdf (PDF, sem fallback via playwright)
- https://researchexchange.ocrahope.org/papers/s0140-6736-21-02178-4 — HTTP 410 em https://researchexchange.ocrahope.org/papers/s0140-6736-21-02178-4

### Bloqueadas por barreira de acesso

- https://www.who.int/initiatives/cervical-cancer-elimination-initiative/cervical-cancer-forum — interstitial — barreira de acesso (interstitial): # Global cervical cancer elimination forum: advancing the call to action ## Every 2 minutes ### a woman dies of cervical
- https://mdedge.com/content/cochrane-report-hpv-vaccine-proves-its-worth-adolescent-young-adult-women — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. The action you just performed triggered 
- https://pulsetoday.co.uk/?p=142882 — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. The action you just performed triggered 
- https://immattersacp.org/weekly/archives/2025/12/09/1.htm — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-1`** [1]
  - Trecho: A carga é ainda mais desigual entre mulheres que vivem com HIV, cujo risco de desenvolver a doença é cerca de seis vezes maior que o da população geral.
  - Justificativa: A evidência afirma explicitamente que mulheres vivendo com HIV têm seis vezes mais probabilidade de desenvolver câncer cervical em comparação com a população geral, o que corresponde diretamente à afirmação do trecho.
  - Suporte veio de: [1]
  - Evidência: “Women living with HIV are 6 times more likely to develop cervical cancer compared to women without HIV.”
- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-3`** [3]
  - Trecho: O dado oficial mais recente registra 7.493 mortes pela doença em 2024.
  - Justificativa: A evidência afirma explicitamente: 'O dado oficial mais recente registra 7.493 mortes por câncer do colo do útero no Brasil em 2024.', o que corresponde diretamente à afirmação.
  - Suporte veio de: [3]
  - Evidência: “O dado oficial mais recente registra 7.493 mortes por câncer do colo do útero no Brasil em 2024.”
- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-4`** [4]
  - Trecho: A distribuição regional é desigual: nas regiões Norte e Nordeste a doença é o segundo câncer mais incidente entre as mulheres, enquanto no Sudeste ocupa a quinta posição.
  - Justificativa: A evidência afirma explicitamente que o câncer do colo do útero é o segundo mais incidente entre as mulheres nas regiões Norte e Nordeste, enquanto no Sudeste ocupa a quinta posição, o que corresponde exatamente à afirm…
  - Suporte veio de: [4]
  - Evidência: “O câncer do colo do útero é o segundo mais incidente entre as mulheres nas regiões Norte e Nordeste, enquanto no Sudeste ocupa a quinta posição.”
### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-0`** [1]
  - Trecho: Aproximadamente 94% desses óbitos ocorreram em países de baixa e média renda.
  - Justificativa: A evidência menciona que as maiores taxas de incidência e mortalidade por câncer cervical ocorrem em países de baixa e média renda, mas não apresenta a porcentagem específica de 94% dos óbitos. Esse número não consta em…
  - Não coberto pela evidência: Aproximadamente 94% dos óbitos ocorreram em países de baixa e média renda
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-11`** [9]
  - Trecho: As vacinas de espectro mais amplo, como a nonavalente, podem proteger contra os tipos que causam até 90% dos casos.
  - Justificativa: A evidência afirma que vacinas contra HPV podem proteger contra até 90% dos casos de câncer cervical, mas não menciona 'vacinas de espectro mais amplo' nem a vacina 'nonavalente'. A caracterização específica do tipo de…
  - Suporte veio de: [9]
  - Não coberto pela evidência: vacinas de espectro mais amplo; nonavalente
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [10] [39] [29] [34] [40] [30] [38] [7] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-19`** [16]
  - Trecho: Para a lesão precursora de alto grau (NIC3), as reduções foram ainda maiores.
  - Justificativa: A evidência consiste em uma página de navegação do site HealthDay com manchetes de notícias sobre diversos tópicos de saúde. Não há qualquer menção a NIC3, lesões precursoras de alto grau, ou reduções associadas a essas…
  - Não coberto pela evidência: Lesão precursora de alto grau (NIC3); Reduções associadas a NIC3; Comparação de magnitude das reduções em relação a outras lesões
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `vacinacao_hpv_83ba536ab30e_20261025T153513Z-52`** [36]
  - Trecho: **Grupos especiais.** A dose única também vale para usuários de profilaxia pré-exposição ao HIV (PrEP) entre 15 e 45 anos e para vítimas de violência sexual a partir dos 15 anos.
  - Justificativa: A evidência afirma explicitamente que usuários de PrEP entre 15 e 45 anos e vítimas de violência sexual a partir dos 15 anos seguem o esquema de TRÊS doses, e não o esquema de dose única. O trecho do claim afirma que a…
  - Evidência: “Para pessoas imunocomprometidas, como aquelas que vivem com HIV/Aids, pacientes oncológicos e transplantados, o esquema vacinal permanece com três doses. A mesma recomendação se aplica a usuários de PrEP entre 15 e 45 a…”

---

## 10. Trechos Citados Não Auditados

Motivos: 1 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 5 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 5 citam referência não baixada/inacessível.

- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-2` — Referencia(s) citada(s) ['4e792edbdd54108f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-13` — Referencia(s) citada(s) ['3366c2cf3a2971f9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-14` — Referencia(s) citada(s) ['3366c2cf3a2971f9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-21` — Referencia(s) citada(s) ['6317eb68a64a7b60'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-23` — Referencia(s) citada(s) ['dbdde3c4d6251bee'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-25` — Referencia(s) citada(s) ['6b28389c16049223'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-31` — Referencia(s) citada(s) ['60fab7be2b39184c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-34` — Referencia(s) citada(s) ['e5a30ca762aae1b3'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-35` — Referencia(s) citada(s) ['e5a30ca762aae1b3'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-63` — Referencia(s) citada(s) ['259868a97827cf7b'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_83ba536ab30e_20261025T153513Z-80` — Parte das fontes citadas sem conteudo: referencia(s) ['60fab7be2b39184c'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.