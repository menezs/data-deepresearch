# Relatório de Auditoria — Gemini (rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z)

**Arquivo auditado:** `answers/Ingles/Gemini/EmConsolidacao/rede_social_saude_mental_adolecentes.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T00:10:01.136502+00:00 |
| **Total de trechos citados** | 96 |
| **Tempo de processamento** | 2:06:36:48 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3064.9 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-15 17:33:41+00:00 |
| Citações no corpo | 202 marcadores, 65 distintos |
| Referências listadas | 65 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 54 | 56.2% |
| **UNSUPPORTED** | 28 | 29.2% |
| **CONTRADICTED** | 1 | 1.0% |
| **SKIPPED** | 12 | 12.5% |
| **PENDENTE** | 1 | 1.0% |
| **TOTAL** | 96 | 100.0% |

Sobre os 83 trechos citados auditados: SUPPORTED 65,06%, UNSUPPORTED 33,73%, CONTRADICTED 1,20%.

> **31 dos 54 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 31 estão **contados dentro** dos 54 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`33` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `5` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 4, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` Second, aggregate measures of daily screen duration consistently yield small average associations with well-being, obsc… | [4] [9] [10] [11] | [45] [42] [14] [53] [60] [1] [20] | — |
| `#15` Nevertheless, independent clinical surveillance corroborates a post-2021 retreat from pandemic highs. | [6] [23] | [19] [35] [28] [29] [25] [21] [27] | — |
| `#46` Disentangling whether social media causes adolescent psychopathology or reflects preexisting vulnerability sits at the… | [1] [4] | [54] [42] [45] [12] [14] [3] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1677172 |
| **Média de tokens por requisição** | 20206.9 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/65 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 6.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://www.researchgate.net/publication/378522291_Social_media_and_adolescent_mental_health_A_consensus_report_of_the_National_Academies_of_Sciences_Engineering_and_Medicine) | error | 10 | 0 | 0 | 0 | 10 |
| [[5]](https://www.cdc.gov/yrbs/youth-health-in-focus/mental-health.html) | downloaded | 10 | 6 | 3 | 1 | 0 |
| [[1]](https://dr.lib.iastate.edu/server/api/core/bitstreams/352457cb-75c1-4499-a5bf-5608c1ef86e5/content) | downloaded | 9 | 2 | 4 | 3 | 0 |
| [[14]](https://www.ntia.gov/report/2024/kids-online-health-and-safety/online-health-and-safety-for-children-and-youth/identifying-risks-benefits-to-kids-health-safety-privacy-from-their-use-of-online-platforms/health) | downloaded | 8 | 2 | 6 | 0 | 0 |
| [[4]](https://www.researchgate.net/publication/359509628_Windows_of_developmental_sensitivity_to_social_media) | error | 7 | 0 | 0 | 0 | 7 |
| [[9]](https://www.understandingsociety.ac.uk/wp-content/uploads/2024/11/Andrew-Przybylski.pdf) | inaccessible | 7 | 0 | 0 | 0 | 7 |
| [[12]](https://www.aeaweb.org/content/file?id=17257) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857400/) | downloaded | 6 | 5 | 1 | 0 | 0 |
| [[10]](https://www.hbsc.org/new-who-hbsc-report-sheds-light-on-adolescent-digital-behaviours-across-europe-central-asia-and-canada/) | downloaded | 6 | 0 | 3 | 3 | 0 |
| [[11]](https://www.researchgate.net/publication/391460889_Social_media_use_in_adolescents_with_and_without_mental_health_conditions) | error | 6 | 0 | 0 | 0 | 6 |
| [[21]](https://afsp.org/story/2025-youth-risk-behavior-survey-analysis-where-does-us-teen-mental-health-stand) | downloaded | 6 | 6 | 0 | 0 | 0 |
| [[6]](https://www.samhsa.gov/data/sites/default/files/NSDUH-2025-Annual-Release/2025-nsduh-nnr-highlights.pdf) | inaccessible | 5 | 0 | 0 | 0 | 5 |
| [[13]](https://www.researchgate.net/publication/377975417_Problematic_social_media_use_in_childhood_and_adolescence) | error | 5 | 0 | 0 | 0 | 5 |
| [[15]](https://www.scribd.com/document/774403211/237-256) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[17]](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[37]](https://www.pewresearch.org/internet/2025/12/09/teens-social-media-and-ai-chatbots-2025/) | downloaded | 5 | 1 | 4 | 0 | 0 |
| [[8]](https://www.pewresearch.org/internet/2024/12/12/teens-social-media-and-technology-2024/) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[16]](https://research.birmingham.ac.uk/en/publications/school-phone-policies-and-their-association-with-mental-wellbeing/) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[38]](https://www.pewresearch.org/topic/internet-technology/user-demographics/age-generations-tech/teens-tech/) | downloaded | 4 | 0 | 2 | 2 | 0 |
| [[39]](https://www.who.int/europe/news/item/25-09-2024-teens--screens-and-mental-health) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[57]](https://www.infrastructure.gov.au/media-communications/internet/online-safety/social-media-minimum-age) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[59]](https://www.bmj.com/content/390/bmj.r1729) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[7]](https://www.samhsa.gov/blog/release-2025-nsduh-using-data-to-drive-great-american-recovery) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[18]](https://www.researchgate.net/publication/389352830_Smartphone_use_and_mental_health_going_beyond_school_restriction_policies) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[19]](https://www.oecd.org/en/publications/child-adolescent-and-youth-mental-health-in-the-21st-century_1092c3cb-en/full-report/trends-and-patterns-in-the-mental-health-status-of-children-adolescents-and-young-people_696bf3a0.html) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[22]](https://www.prnewswire.com/news-releases/where-does-us-teen-mental-health-stand-improvements-reported-but-disparities-persist-302934163.html) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[36]](https://www.youngminds.org.uk/about-us/media-centre/mental-health-statistics/) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[44]](https://www.cdc.gov/yrbs/results/2023-yrbs-results.html) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[62]](https://en.wikipedia.org/wiki/Online_Safety_Amendment_(Social_Media_Minimum_Age)_Act_2024) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[23]](https://www.kff.org/mental-health/state-indicator/adolescents-with-a-major-depressive-episode-in-the-past-year/) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[30]](https://www.samhsa.gov/data/sites/default/files/reports/rpt56770/2024-nsduh-psr6-adol-mde-suicide.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[31]](https://www.samhsa.gov/data/sites/default/files/reports/rpt57038/2025-nsduh-women-health-short-report/2025-nsduh-women-health-short-report.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[34]](https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/suicidal-thoughts-suicide-attempts-and-self-harm) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[40]](https://data-browser.hbsc.org/measure/problematic-social-media-use/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[42]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7919645/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[46]](https://ajph.aphapublications.org/doi/10.2105/AJPH.2024.307784) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[47]](https://www.semanticscholar.org/paper/Social-media-use-and-its-impact-on-adolescent-An-of-Valkenburg-Meier/4db5117d5fefc571d0e2fabeddc55f9858935ed8) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[52]](https://web.stanford.edu/~gentzkow/research/facebook.pdf) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[53]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11880199/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[54]](https://alexeymakarin.github.io/assets/Braghieri_Levy_Makarin_CEPR_eBook_2023.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[56]](https://www.researchgate.net/publication/366840818_Association_of_Habitual_Checking_Behaviors_on_Social_Media_With_Longitudinal_Functional_Brain_Development) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[60]](https://www.nationalelfservice.net/treatment/digital-health/smartphone-bans-schools-not-associated-better-mental-wellbeing/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[61]](https://www.hindustantimes.com/world-news/teen-who-admitted-planning-terror-attack-in-sydney-says-he-used-ai-for-his-plans-report-101794293455598.html) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[20]](https://www.cdc.gov/mmwr/volumes/73/su/su7304a9.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[24]](https://www.samhsa.gov/data/sites/default/files/reports/rpt56484/NSDUHDetailedTabs2024/NSDUHDetailedTabs2024/2024-nsduh-detailed-tables-sect7pe.htm?s=12%20to%2017&) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[25]](https://www.nimh.nih.gov/health/statistics/major-depression) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[26]](https://www.naco.org/news/samhsa-releases-new-2024-data-rates-mental-illness-and-substance-use-disorder-us) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[27]](https://www.cdc.gov/nchs/products/databriefs/db471.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[28]](https://jedfoundation.org/new-cdc-data-show-youth-suicide-rates-are-declining-but-our-work-is-far-from-over/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://www.samhsa.gov/blog/release-2024-nsduh-leveraging-latest-substance-use-mental-health-data-make-america-healthy-again) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://mhstats.org/blog/youth-mental-health-statistics) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://digital.nhs.uk/data-and-information/publications/statistical/mental-health-of-children-and-young-people-in-england/2023-wave-4-follow-up) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[35]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13314999/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://iris.who.int/server/api/core/bitstreams/30bc5231-b9de-45fa-9e25-eb329c23689f/content) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[43]](https://research.rug.nl/files/1569652992/Problematic_social_media_use_mental_health_.pdf) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[45]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11559676/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://www.scirp.org/reference/referencespapers?referenceid=4372970) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[49]](https://publications.jrc.ec.europa.eu/repository/handle/JRC135339) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://www.researchgate.net/publication/358218905_Specification_curve_analysis_shows_that_social_media_use_is_linked_to_poor_mental_health_especially_among_girls) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[51]](https://www.semanticscholar.org/paper/The-association-between-adolescent-well-being-and-Orben-Przybylski/75e0601958dea426eeff0111ce879a4019dfbe83) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[55]](https://mitsloan.mit.edu/press/academic-study-reveals-new-evidence-facebooks-negative-impact-mental-health-college-students) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[58]](https://www.cdc.gov/yrbs/youth-health-in-focus/index.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[63]](https://www.hindustantimes.com/world-news/google-warns-australia-new-internet-safety-bill-could-cut-off-under-18s-from-gmail-meta-tiktok-snap-raise-alarm-101794204999792.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[64]](https://teen.gwnews.com/articles/aussies-opt-out) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[65]](https://academic.oup.com/pnasnexus/article/3/2/pgae037/7614669) | blocked | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[5]](https://www.cdc.gov/yrbs/youth-health-in-focus/mental-health.html) | #9–12, #22, #25 | #2, #8, #21 | #1 | `#9` Persistent Feelings of Sadness or Hopelessness: 30%, 31%, 37%, 42%, 40%, 33%. ... A callout notes that in 2025, 33% of high school students experienced persist… |
| [[1]](https://dr.lib.iastate.edu/server/api/core/bitstreams/352457cb-75c1-4499-a5bf-5608c1ef86e5/content) | #0, #47 | #46, #48, #94–95 | #1, #6–7 | `#0` social media use is not monolithic. The affordances of different social media platforms allow for a broad range of behaviors that can have dramatically differe… |
| [[14]](https://www.ntia.gov/report/2024/kids-online-health-and-safety/online-health-and-safety-for-children-and-youth/identifying-risks-benefits-to-kids-health-safety-privacy-from-their-use-of-online-platforms/health) | #73, #77 | #4–5, #68, #74, #76, #78 | — | `#73` The use of social media and other online platforms can influence key developmental processes that occur throughout childhood, especially during adolescence. Th… |
| [[12]](https://www.aeaweb.org/content/file?id=17257) | #58, #60–61 | #4, #59, #62 | #57 | `#58` Our index of poor mental health, which aggregates all the relevant mental health variables in the NCHA survey, increased by 0.085 standard deviation units as a… |
| [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857400/) | #0, #68, #70–72 | #69 | — | `#0` social media behaviors in early adolescence may be associated with changes in adolescents' neural development; Social media provides a constant and unpredictab… |
| [[10]](https://www.hbsc.org/new-who-hbsc-report-sheds-light-on-adolescent-digital-behaviours-across-europe-central-asia-and-canada/) | — | #39, #94–95 | #3, #5, #42 | `#39` This study reveals both the promise and the pitfalls of digital engagement for our young people. [...] they should rule social media, and not have social media… |
| [[21]](https://afsp.org/story/2025-youth-risk-behavior-survey-analysis-where-does-us-teen-mental-health-stand) | #10–11, #13–14, #27, #82 | — | — | `#10` The American Foundation for Suicide Prevention (AFSP), the largest private funder of suicide prevention research, recognizes these improvements as encouraging… |
| [[15]](https://www.scribd.com/document/774403211/237-256) | — | — | #5, #51, #75, #77, #81 | — |
| [[17]](https://www.esafety.gov.au/about-us/industry-regulation/social-media-age-restrictions) | #89–90 | #6, #76, #92 | — | `#89` we've been monitoring how platforms have responded to the Social Media Minimum Age legislation. We're assessing what they've done - and where they're falling s… |
| [[37]](https://www.pewresearch.org/internet/2025/12/09/teens-social-media-and-ai-chatbots-2025/) | #37 | #34–36, #38 | — | `#37` The share of teens who say they are on TikTok almost constantly ticked up slightly to 21% this year, from 16% in 2022. [...] Teen boys are more likely than gir… |
| [[8]](https://www.pewresearch.org/internet/2024/12/12/teens-social-media-and-technology-2024/) | — | #2, #34–36 | — | `#2` large shares of teens have or have access to a smartphone (95%) |
| [[16]](https://research.birmingham.ac.uk/en/publications/school-phone-policies-and-their-association-with-mental-wellbeing/) | #85 | #6, #83, #86 | — | `#85` There is no evidence that restrictive school policies are associated with overall phone and social media use or better mental wellbeing in adolescents. The fin… |
| [[38]](https://www.pewresearch.org/topic/internet-technology/user-demographics/age-generations-tech/teens-tech/) | — | #38, #84 | #35–36 | `#38` 12% say they’ve gotten emotional support from these tools |
| [[39]](https://www.who.int/europe/news/item/25-09-2024-teens--screens-and-mental-health) | #39–40, #42 | #41 | — | `#39` Adolescents who are heavy but non-problematic users reported stronger peer support and social connections. [...] Previous research has found that problematic s… |
| [[57]](https://www.infrastructure.gov.au/media-communications/internet/online-safety/social-media-minimum-age) | — | #76, #90–91 | #74 | `#76` endless-feeds (infinite scroll) |
| [[7]](https://www.samhsa.gov/blog/release-2025-nsduh-using-data-to-drive-great-american-recovery) | #20 | #2, #17 | — | `#20` Among the 3.7 million adolescents aged 12 to 17 in 2025 that had a past year major depressive episode, 57.7% (2.1 million) reported receiving mental health tre… |
| [[18]](https://www.researchgate.net/publication/389352830_Smartphone_use_and_mental_health_going_beyond_school_restriction_policies) | — | — | #6, #87, #95 | — |
| [[19]](https://www.oecd.org/en/publications/child-adolescent-and-youth-mental-health-in-the-21st-century_1092c3cb-en/full-report/trends-and-patterns-in-the-mental-health-status-of-children-adolescents-and-young-people_696bf3a0.html) | #29–30 | — | #7 | `#29` some time series data suggest that the declining trend in youth mental health started prior to pandemic. Figure 1.5. shows trends in relative level of mental d… |
| [[22]](https://www.prnewswire.com/news-releases/where-does-us-teen-mental-health-stand-improvements-reported-but-disparities-persist-302934163.html) | #14, #27–28 | — | — | `#14` the decrease in the student sample by nearly half (47%) from 20,103 students in 2023 to 10,710 in 2025 raises the question of whether these findings fully refl… |
| [[36]](https://www.youngminds.org.uk/about-us/media-centre/mental-health-statistics/) | — | #33, #81 | #79 | `#33` In 2023/24, there were 78,577 young people waiting over a year for mental health treatment from the NHS, with 44% of these were waiting over two years. |
| [[44]](https://www.cdc.gov/yrbs/results/2023-yrbs-results.html) | — | #45, #81 | #80 | `#45` The YRBS also included questions about experiencing racism in school, unfair discipline at school, and how often students used social media. |
| [[62]](https://en.wikipedia.org/wiki/Online_Safety_Amendment_(Social_Media_Minimum_Age)_Act_2024) | #90 | #91–92 | — | `#90` It was the first such legislation to be passed in the world. Facebook, Instagram, Reddit, Snapchat, TikTok, Twitter, Threads, Twitch, Kick, and YouTube were ag… |
| [[23]](https://www.kff.org/mental-health/state-indicator/adolescents-with-a-major-depressive-episode-in-the-past-year/) | — | #15 | #16 (pulado) | `#15` 2023-2024 |
| [[30]](https://www.samhsa.gov/data/sites/default/files/reports/rpt56770/2024-nsduh-psr6-adol-mde-suicide.pdf) | #21, #23 | — | — | `#21` An annual average of 17.7% of adolescents aged 12 to 17 had an MDE in the past year. ... Male adolescents aged 12 to 17 were less likely than female adolescent… |
| [[31]](https://www.samhsa.gov/data/sites/default/files/reports/rpt57038/2025-nsduh-women-health-short-report/2025-nsduh-women-health-short-report.pdf) | #24 | #23 | — | `#24` Among adolescent females aged 12 to 17 who had a co-occurring SUD and MDE in the past year, 84.5% had an MDE with severe impairment. |
| [[34]](https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/suicidal-thoughts-suicide-attempts-and-self-harm) | — | #31, #33 | — | `#31` Among 16 to 24 year olds, 31.7% of women and 15.4% of men reported having ever self-harmed. [...] 83.1% of those who had self-harmed reported doing so to relie… |
| [[40]](https://data-browser.hbsc.org/measure/problematic-social-media-use/) | — | — | #40–41 | — |
| [[42]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7919645/) | #43 | #79 | — | `#43` All \| 57.1 (54.8–59.3) \| 33.5 (31.6–35.5) \| 9.4 (8.3–10.8) \| 100 (3077) ... Feeling low \| 26.1 (23.6–28.8) \| 49.2 (45.5–52.9) \| 53.5 (47.2–59.6) ... Morning ti… |
| [[47]](https://www.semanticscholar.org/paper/Social-media-use-and-its-impact-on-adolescent-An-of-Valkenburg-Meier/4db5117d5fefc571d0e2fabeddc55f9858935ed8) | — | #50–51 | — | `#50` There is no evidence that time spent on social media is correlated with adolescent mental health problems: Findings from a meta-analysis. |
| [[52]](https://web.stanford.edu/~gentzkow/research/facebook.pdf) | — | #57, #62 | — | `#57` We can also compare our SWB effects to what we would have estimated using the kind of correlational approach taken by many previous non-experimental studies. |
| [[53]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11880199/) | #63 | — | #57 | `#63` This meta-analysis included a total of 38 effect sizes. [...] Stieger and Lewetz reported that 59% of participants visited social media at least once during th… |
| [[54]](https://alexeymakarin.github.io/assets/Braghieri_Levy_Makarin_CEPR_eBook_2023.pdf) | #58 | #59 | — | `#58` In a recent paper (Braghieri et al. 2022), we provide the most comprehensive causal evidence to date on the effects of social media on mental health by leverag… |
| [[60]](https://www.nationalelfservice.net/treatment/digital-health/smartphone-bans-schools-not-associated-better-mental-wellbeing/) | #87 | #86 | — | `#87` across all participants, greater smartphone and social media use was significantly associated with several negative outcomes including: Reduced mental wellbein… |
| [[61]](https://www.hindustantimes.com/world-news/teen-who-admitted-planning-terror-attack-in-sydney-says-he-used-ai-for-his-plans-report-101794293455598.html) | — | — | #89, #92 | `#92` A director of a mental health service voiced concerns, stating that "73% of young people across Australia who accessed mental health support did so through soc… |
| [[20]](https://www.cdc.gov/mmwr/volumes/73/su/su7304a9.htm) | — | #8 | — | `#8` a cross-sectional, school-based survey conducted biennially since 1991. Each survey year, CDC collects data from a nationally representative sample of public a… |
| [[25]](https://www.nimh.nih.gov/health/statistics/major-depression) | — | — | #17 ⚡ | `#17` In 2021, an estimated 3.7 million adolescents aged 12 to 17 in the United States had at least one major depressive episode with severe impairment in the past y… |
| [[26]](https://www.naco.org/news/samhsa-releases-new-2024-data-rates-mental-illness-and-substance-use-disorder-us) | — | #17 | — | `#17` 15.4 percent of adolescents aged 12 to 17 (about 3.8 million individuals) reported experiencing a major depressive episode (MDE). |
| [[27]](https://www.cdc.gov/nchs/products/databriefs/db471.htm) | — | #19 | — | `#19` Suicide rates for people aged 10–24 increased from 2007 through 2021 (from 6.8 deaths per 100,000 to 11.0) |
| [[28]](https://jedfoundation.org/new-cdc-data-show-youth-suicide-rates-are-declining-but-our-work-is-far-from-over/) | #19 | — | — | `#19` Newly released data from the Centers for Disease Control and Prevention (CDC) offers a measure of hope: Although suicide rates were largely stable the past sev… |
| [[29]](https://www.samhsa.gov/blog/release-2024-nsduh-leveraging-latest-substance-use-mental-health-data-make-america-healthy-again) | #20 | — | — | `#20` Among the 3.8 million adolescents aged 12 to 17 in 2024 that had a past year major depressive episode, 60.6% (2.3 million) reported receiving mental health tre… |
| [[32]](https://mhstats.org/blog/youth-mental-health-statistics) | #26 | — | — | `#26` In 2023, 53% of females and 65% of LGBTQ+ students reported persistent sadness, and LGBTQ+ students attempted suicide at more than three times the rate of hete… |
| [[33]](https://digital.nhs.uk/data-and-information/publications/statistical/mental-health-of-children-and-young-people-in-england/2023-wave-4-follow-up) | — | #31 | — | `#31` This was 20.3% of 8 to 16 year olds, 23.3% of 17 to 19 year olds and 21.7% of 20 to 25 year olds. After a rise in prevalence between 2017 and 2020, rates of pr… |
| [[35]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13314999/) | #32 | — | — | `#32` In total there were 498 deaths likely due to suicide, during the 4 year period. Risk of death by suicide was 14.31 (13.08–15.63) per 1,000,000 CYP per year, wi… |
| [[41]](https://iris.who.int/server/api/core/bitstreams/30bc5231-b9de-45fa-9e25-eb329c23689f/content) | — | #40 | — | `#40` Problematic users: Six or more symptoms of problematic use, regardless of contact frequency. |
| [[45]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11559676/) | #45 | — | — | `#45` In 2023, for the first time, CDC's nationally representative Youth Risk Behavior Survey included an item assessing U.S. high school students' frequency of soci… |
| [[48]](https://www.scirp.org/reference/referencespapers?referenceid=4372970) | — | — | #51 | — |
| [[49]](https://publications.jrc.ec.europa.eu/repository/handle/JRC135339) | — | #51 | — | `#51` SALA Arianna; PORCARO Lorenzo; GOMEZ Emilia; |
| [[50]](https://www.researchgate.net/publication/358218905_Specification_curve_analysis_shows_that_social_media_use_is_linked_to_poor_mental_health_especially_among_girls) | — | #52 | — | `#52` the effect of screen time being equivalent to the effect of eating a potato for well-being (Orben & Przybylski, 2019) |
| [[55]](https://mitsloan.mit.edu/press/academic-study-reveals-new-evidence-facebooks-negative-impact-mental-health-college-students) | — | #59 | — | `#59` a rise of 7% in the number of students who had suffered, at least once during the preceding year, from depression so severe that it was difficult for them to f… |
| [[58]](https://www.cdc.gov/yrbs/youth-health-in-focus/index.html) | — | #78 | — | `#78` Fewer students got at least 8 hours of sleep on an average school night. |
| [[63]](https://www.hindustantimes.com/world-news/google-warns-australia-new-internet-safety-bill-could-cut-off-under-18s-from-gmail-meta-tiktok-snap-raise-alarm-101794204999792.html) | #93 | — | — | `#93` A proposed Australian internet law could force Google to block under-18s from using its Gmail service, an Australia-based company policy head said on Monday, u… |
| [[64]](https://teen.gwnews.com/articles/aussies-opt-out) | — | #94 | — | `#94` Beginning in 2027, California and New York will have laws limiting algorithm-driven feeds for teenagers. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.samhsa.gov/data/sites/default/files/NSDUH-2025-Annual-Release/2025-nsduh-nnr-highlights.pdf — 2a tentativa excedeu 90s
- https://www.understandingsociety.ac.uk/wp-content/uploads/2024/11/Andrew-Przybylski.pdf — 2a tentativa excedeu 90s
- https://research.rug.nl/files/1569652992/Problematic_social_media_use_mental_health_.pdf — HTTP 403 em https://research.rug.nl/files/1569652992/Problematic_social_media_use_mental_health_.pdf (PDF, sem fallback via playwright)
- https://www.researchgate.net/publication/366840818_Association_of_Habitual_Checking_Behaviors_on_Social_Media_With_Longitudinal_Functional_Brain_Development — Rate limit persistente em https://www.researchgate.net/publication/366840818_Association_of_Habitual_Checking_Behaviors_on_Social_Media_With_Longitudinal_Functional_Brain_Development

### Bloqueadas por barreira de acesso

- https://ajph.aphapublications.org/doi/10.2105/AJPH.2024.307784 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.semanticscholar.org/paper/The-association-between-adolescent-well-being-and-Orben-Przybylski/75e0601958dea426eeff0111ce879a4019dfbe83 — anti_bot — barreira de acesso (anti_bot): Complete the security check before continuing. This step verifies that you are not a bot, which helps to protect your ac
- https://www.bmj.com/content/390/bmj.r1729 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://academic.oup.com/pnasnexus/article/3/2/pgae037/7614669 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-0`** [1] [2] [3] [4]
  - Trecho: The relationship between social media use and adolescent mental health operates neither as a uniform dose-response toxin nor as a benign communications utility, but as a contingent interaction among platform design feat…
  - Justificativa: A evidência sustenta os três elementos centrais da afirmação: (1) a relação não é uniforme — 'social media use is not monolithic', efeitos 'differ among individuals' e 'subgroups'; (2) não é benigna — há 'potential harm…
  - Suporte veio de: [1] [3]
  - Evidência: “social media use is not monolithic. The affordances of different social media platforms allow for a broad range of behaviors that can have dramatically different psychological and health implications”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | sustenta | social media use is not monolithic. The affordances of different social media platforms allow for a broad range of beha… |
    | [3] | sustenta | social media behaviors in early adolescence may be associated with changes in adolescents' neural development; Social m… |

- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-8`** [5] [20]
  - Trecho: In the United States, the Centers for Disease Control and Prevention's Youth Risk Behavior Survey (YRBS), a biennial school-based survey of students in grades 9 through 12, documents a steep multi-year deterioration fol…
  - Justificativa: A evidência confirma que o YRBS é um survey escolar bienal para alunos das séries 9 a 12. Os dados de tendência mostram deterioração multi-anual (ex.: tristeza persistente subiu de 30% em 2015 para 42% em 2021) seguida…
  - Suporte veio de: [20] [5]
  - Evidência: “a cross-sectional, school-based survey conducted biennially since 1991. Each survey year, CDC collects data from a nationally representative sample of public and private school students in grades 9–12”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [20] | parcial | a cross-sectional, school-based survey conducted biennially since 1991. Each survey year, CDC collects data from a nati… |
    | [5] | parcial | Persistent feelings of sadness or hopelessness: improved over 2 years, worsened over 10 years. [...] Persistent Feeling… |

- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-9`** [5]
  - Trecho: The proportion of U.S. high schoolers reporting persistent feelings of sadness or hopelessness during the preceding twelve months rose from 30% in 2015 to 31% in 2017 and 37% in 2019, peaked during COVID-19 at 42% in 20…
  - Justificativa: A evidência apresenta explicitamente a série temporal de 'Persistent Feelings of Sadness or Hopelessness' de 2015 a 2025 com os valores exatos citados (30%, 31%, 37%, 42%, 40%, 33%), correspondendo aos anos 2015, 2017,…
  - Suporte veio de: [5]
  - Evidência: “Persistent Feelings of Sadness or Hopelessness: 30%, 31%, 37%, 42%, 40%, 33%.”
  - Não coberto pela evidência: A associação explícita do pico de 42% em 2021 com a pandemia de COVID-19 não é afirmada diretamente na evidência; a evidência apenas fornece os valores numéricos por ano, sem mencionar COVID-19.
### UNSUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-1`** [1] [5] [6]
  - Trecho: Across nationally representative surveillance datasets and major scientific syntheses through 2026, two realities sit side by side.
  - Justificativa: A afirmacao e uma frase de moldura/introducao vaga que nao encontra correspondencia literal na evidencia. A evidencia contem dados de vigilancia do CDC (ate 2025) e um relatorio da National Academy of Sciences, mas: (1)…
  - Não coberto pela evidência: through 2026; nationally representative surveillance datasets; major scientific syntheses
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [5] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-3`** [4] [9] [10] [11]
  - Trecho: Second, aggregate measures of daily screen duration consistently yield small average associations with well-being, obscuring sharper harms concentrated within compulsive use patterns, sex-specific developmental windows,…
  - Justificativa: A evidência não aborda a relação entre medidas agregadas de duração diária de tela e bem-estar, nem a ideia de que essas medidas obscureçam danos mais agudos. Embora a evidência mencione diferenças por sexo e disparidad…
  - Suporte veio de: [10]
  - Não coberto pela evidência: aggregate measures of daily screen duration consistently yield small average associations with well-being; obscuring sharper harms concentrated within compulsive use patterns; sex-specific developmental windows
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [10] | ausente | — |

  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [45] [42] [14] [53] [60] [1] [20] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-4`** [11] [12] [13] [14]
  - Trecho: Quasi-experimental and clinical evidence implicates upward social comparison, sleep displacement, cyberbullying, and exposure to harmful content as active pathways linking social media to depression, anxiety, and body-i…
  - Justificativa: A evidência sustenta parcialmente a afirmação: confirma evidência quasi-experimental sobre comparação social desfavorável e associações com depressão e ansiedade. Contudo, vários elementos centrais da afirmação não estã…
  - Suporte veio de: [14] [12]
  - Evidência: “we provide quasi-experimental estimates of the impact of social media on mental health by leveraging a unique natural experiment: the staggered introduction of Facebook across U.S. colleges”
  - Não coberto pela evidência: cyberbullying como via ativa (não mencionado na evidência); body-image distress como desfecho (não mencionado explicitamente); early-adolescent girls especificamente (evidência menciona apenas 'girls' de forma geral, sem especificar 'early-adolescent')
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [12] | parcial | We provide quasi-experimental estimates of the impact of social media on mental health |
    | [14] | parcial | social comparison, displacement of other activities, interference with attention and learning, sleep disruption, overus… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-17`** [6] [7] [25] [26]
  - Trecho: Single-year estimates trace the same descent, moving from 20.1% (5.0 million youth) in 2021 to 15.4% (3.8 million) in 2024 and 3.7 million in 2025, while MDE with severe functional impairment dropped from 15.2% (3.8 mil…
  - Justificativa: A maior parte da afirmacao encontra suporte na evidencia, mas ha uma contradicao clara nos numeros de 2021 para MDE com comprometimento grave (severe impairment). A afirmacao diz '15.2% (3.8 million) in 2021', mas a evi…
  - Suporte veio de: [7] [26] [25]
  - Evidência: “An estimated 5.0 million adolescents aged 12 to 17 in the United States had at least one major depressive episode. This number represented 20.1% of the U.S. population aged 12 to 17.”
  - Não coberto pela evidência: A porcentagem de 15.1% para MDE em 2025 nao e mencionada na afirmacao (apenas o numero 3.7 million); O numero '15.2% (3.8 million)' para MDE com severe impairment em 2021 esta contradito pela evidencia, que indica 14.7% (3.7 million)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | Among adolescents aged 12 to 17, 15.1% (3.7 million) had a past year major depressive episode (MDE) and 11.0% (2.7 mill… |
    | [26] | parcial | 15.4 percent of adolescents aged 12 to 17 (about 3.8 million individuals) reported experiencing a major depressive epis… |
    | [25] | contradiz | In 2021, an estimated 3.7 million adolescents aged 12 to 17 in the United States had at least one major depressive epis… |

  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A afirmacao contem numeros para 2021 que nao aparecem na evidencia (MDE 20.1%/5.0 milhoes) e um dado contradito pela evidencia: MDE com imp…") — cascata: baseline → context_expansion

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 10 citam referência não baixada/inacessível.

- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-18` — Referencia(s) citada(s) ['3379b7b5769ba550'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-44` — Referencia(s) citada(s) ['0c75dc4b5247fe29'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-49` — Referencia(s) citada(s) ['086835cb336b5e61'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-53` — Referencia(s) citada(s) ['90597fcfba491d26', '34fae9aa3a330a39'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-54` — Referencia(s) citada(s) ['90597fcfba491d26', '34fae9aa3a330a39'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-55` — Referencia(s) citada(s) ['90597fcfba491d26', '34fae9aa3a330a39'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-56` — Referencia(s) citada(s) ['90597fcfba491d26', '34fae9aa3a330a39'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-64` — Referencia(s) citada(s) ['d8737c1efba52fe9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-65` — Referencia(s) citada(s) ['d8737c1efba52fe9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-66` — Referencia(s) citada(s) ['d8737c1efba52fe9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-67` — Referencia(s) citada(s) ['d8737c1efba52fe9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-88` — Referencia(s) citada(s) ['df9dfd489e5b54e4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.

---

## 11. Trechos Citados Pendentes

1 trecho(s) citado(s) ficaram sem veredito: a saída do juiz não pôde ser interpretada (JSON inválido ou truncado). O julgamento não foi marcado como concluído — rode `audit resume rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z` para julgá-los; os já julgados não são refeitos.

- `rede_social_saude_mental_adolecentes_ecb3895829f2_20261115T173312Z-16`