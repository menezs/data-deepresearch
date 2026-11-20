# Relatório de Auditoria — ChatGPT (vacinacao_hpv_acc5fdffce00_20261115T054744Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/Consolidado/vacinacao_hpv.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_acc5fdffce00_20261115T054744Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-15T06:07:46.461070+00:00 |
| **Total de trechos citados** | 101 |
| **Tempo de processamento** | 0:00:20:02 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 31.8 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 101 marcadores, 37 distintos |
| Referências listadas | 37 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 61 | 60.4% |
| **UNSUPPORTED** | 29 | 28.7% |
| **CONTRADICTED** | 2 | 2.0% |
| **SKIPPED** | 9 | 8.9% |
| **TOTAL** | 101 | 100.0% |

Sobre os 92 trechos citados auditados: SUPPORTED 66,30%, UNSUPPORTED 31,52%, CONTRADICTED 2,17%.

> **27 dos 61 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 27 estão **contados dentro** dos 61 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`32` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `8` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `3` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `18` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#2` The International Agency for Research on Cancer (IARC) has classified 12 HPV types as carcinogenic to humans in relatio… | [3] | [1] [17] [10] [2] [16] [9] [5] [7] [19] [8] | — |
| `#4` The causal pathway is biologically coherent as well as epidemiologically established: persistent high-risk HPV infectio… | [5] | [1] [28] [36] [3] [17] [16] [9] [25] [7] [18] | — |
| `#17` HPV vaccine development has progressed from bivalent vaccines directed principally at HPV16 and HPV18, through quadriva… | [4] | [17] [36] [9] [6] [16] [25] [37] [19] [3] | — |
| `#26` England provides complementary population evidence from a different vaccine program. | [12] | [13] [14] [17] [20] [26] [16] | — |
| `#38` CDC states that evidence from more than 160 studies supports a favorable safety profile, and more than 135 million HPV-… | [18] | [19] [20] [16] [24] [21] [17] [6] [4] [37] [36] | — |
| `#40` Syncope is particularly relevant in adolescents after injections generally, which is why CDC recommends vaccination whi… | [18] | [24] [32] [23] [27] | — |
| `#51` Under WHO's 2022 position paper, girls aged 9–14 could receive either one or two doses, girls and women aged 15–20 coul… | [25] | [4] [23] [14] [22] [24] [32] [27] | — |
| `#52` WHO identified girls aged 9–14 as the primary vaccination target because vaccination before HPV exposure produces the g… | [25] | [23] [4] [2] [26] [36] [37] [17] [32] [14] [22] [28] [16] [6] | — |
| `#53` WHO also recommended that immunocompromised people, including people living with HIV, receive at least two doses and, w… | [25] | [4] [24] [22] [23] [36] [27] [37] | — |
| `#55` After reviewing new dose-optimization evidence, SAGE strengthened its preference for a single-dose schedule for girls a… | [26] | [4] [23] [36] [14] [37] | — |
| `#62` For adults aged 27–45, CDC does not recommend universal catch-up vaccination; instead, vaccination may be offered throu… | [27] | [24] [22] [32] [23] | — |
| `#63` The expected average benefit is smaller in this age range because previous HPV exposure becomes increasingly common, al… | [27] | [16] [6] [14] [32] [24] [9] [17] [23] [19] [2] [22] [4] | — |
| `#64` A new sexual partner at any age creates an opportunity for new HPV acquisition, whereas people in long-term mutually mo… | [27] | [24] [16] [28] [17] [2] [23] [19] [9] [22] [36] [18] [37] [8] | — |
| `#75` Until guidelines formally change, reducing screening solely because an individual was vaccinated would run ahead of cur… | [6] | [28] [23] [14] [25] [31] | — |
| `#77` Comparative modeling suggests that achieving these targets in low- and lower-middle-income countries could avert tens o… | [29] | [2] [28] [13] [7] [8] [17] [14] [31] [30] | — |
| `#82` U.S. coverage is higher but remains incomplete and geographically unequal. | [32] | [31] [30] | — |
| `#93` These findings, alongside immunobridging data in younger adolescents, underpin WHO's move toward single-dose schedules. | [26] | [36] [14] [23] [37] [32] | — |
| `#99` Its safety profile is supported by extensive randomized, registry, and post-marketing evidence, while the major unresol… | [18] | [26] [16] [20] [17] [31] [32] [21] [14] [36] [19] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1198285 |
| **Média de tokens por requisição** | 13024.8 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/37 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 2.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | downloaded | 10 | 9 | 1 | 0 | 0 |
| [[6]](https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents/hpv-vaccine-fact-sheet) | downloaded | 8 | 5 | 3 | 0 | 0 |
| [[27]](https://www.cdc.gov/vaccines/hcp/imz-schedules/child-adolescent-notes.html) | downloaded | 8 | 3 | 0 | 5 | 0 |
| [[18]](https://www.cdc.gov/vaccine-safety/vaccines/hpv.html) | downloaded | 7 | 2 | 5 | 0 | 0 |
| [[11]](https://www.nejm.org/doi/full/10.1056/NEJMoa1917338) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[26]](https://www.who.int/americansamoa/news/detail-global/29-10-2026-message-by-the-director-of-the-department-of-immunization--vaccines-and-biologicals-at-who---october-2026) | downloaded | 5 | 1 | 4 | 0 | 0 |
| [[4]](https://www.who.int/teams/immunization-vaccines-and-biologicals/diseases/human-papillomavirus-vaccines-%28HPV%29) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[32]](https://www.cdc.gov/mmwr/volumes/75/wr/mm7534a1.htm) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[36]](https://www.nature.com/articles/s41591-023-02658-0) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/34741816/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[16]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7329692/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[25]](https://www.who.int/publications-detail-redirect/who-wer9750-645-672) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[28]](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/cervical-cancer-screening) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[29]](https://www.who.int/Publications/i/item/9789240014107) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[5]](https://www.iarc.who.int/reference/carcinogenic-human-papillomavirus-infection) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[9]](https://www.cdc.gov/united-states-cancer-statistics/publications/hpv-associated-cancers.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[14]](https://academic.oup.com/jnci/article/116/6/857/7577291) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[22]](https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-notes.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[24]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[30]](https://www.who.int/news-room/fact-sheets/detail/immunization-coverage) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[33]](https://publications.aap.org/pediatrics/article/139/1/e20161764/51685/Announcements-Versus-Conversations-to-Improve-HPV) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[37]](https://pubmed.ncbi.nlm.nih.gov/34634254/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[1]](https://www.iarc.who.int/reference/the-human-papillomavirus-family-and-its-role-in-carcinogenesis/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://www.iarc.who.int/reference/are-20-human-papillomavirus-types-causing-cervical-cancer/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[7]](https://www.iarc.who.int/cancer-type/cervical-cancer) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[8]](https://seer.cancer.gov/statfacts/html/cervix.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://www.iarc.who.int/reference/effect-of-prophylactic-human-papillomavirus-l1-virus-like-particle-vaccine-on-risk-of-cervical-intraepithelial-neoplasia-grade-2-grade-3-and-adenocarcinoma-in-situ-a-combined-analysis-of-four-rando/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/38749552/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://www.bmj.com/content/365/bmj.l1161) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[17]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8724969/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/safety-and-effectiveness-data.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://www.bmj.com/content/347/bmj.f5906) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.who.int/publications/journals/weekly-epidemiological-record/wer101-34) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://cdn.who.int/media/docs/default-source/immunization/immunization_schedules/immunization-summary-table-2.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[31]](https://cdn.who.int/media/docs/default-source/immunization/wuenic/wuenic-progress-and-challenges.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/talking-with-parents.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://publications.aap.org/pediatrics/article/151/3/e2022058794/190722/Early-Initiation-of-HPV-Vaccination-and-Series) | blocked | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | #1, #5, #10–11, #13, #67, #72–73, #81 | #71 | — | `#1` Almost all cases of cervical cancer are caused by infection with oncogenic types of human papillomavirus (HPV). In most cases, the immune system clears the vir… |
| [[6]](https://www.cancer.gov/about-cancer/causes-prevention/risk/infectious-agents/hpv-vaccine-fact-sheet) | #7–9, #20, #66 | #65, #74–75 | — | `#7` Like other immunizations that guard against viral infection, the HPV vaccine stimulates the body to produce antibodies that, in future encounters with HPV, bin… |
| [[27]](https://www.cdc.gov/vaccines/hcp/imz-schedules/child-adolescent-notes.html) | #59–61 | — | #57, #62–64, #58 ⚡ | `#59` Age 9 –14 years at initial vaccination : 2-dose series at 0, 6–12 months (minimum interval: 5 months; repeat dose if administered too soon) |
| [[18]](https://www.cdc.gov/vaccine-safety/vaccines/hpv.html) | #39, #42 | #37–38, #40, #43, #99 | — | `#39` The most common adverse events reported were: syncope (fainting); dizziness; nausea; headache; fever; and injection site reactions (pain, swelling, and redness… |
| [[26]](https://www.who.int/americansamoa/news/detail-global/29-10-2026-message-by-the-director-of-the-department-of-immunization--vaccines-and-biologicals-at-who---october-2026) | #54 | #55–56, #93, #97 | — | `#54` From 5 to 8 October, the Strategic Advisory Group of Experts on Immunization (SAGE) met to review the evidence on vaccines against human papillomavirus (HPV),… |
| [[4]](https://www.who.int/teams/immunization-vaccines-and-biologicals/diseases/human-papillomavirus-vaccines-%28HPV%29) | #3, #18–19 | #17 | — | `#3` All vaccines are highly efficacious in preventing infection with virus types 16 and 18, which are together responsible for approximately 77%% of cervical cance… |
| [[32]](https://www.cdc.gov/mmwr/volumes/75/wr/mm7534a1.htm) | #83–85 | #82 | — | `#83` In 2025, among adolescents aged 13–17 years, 77.7% had received ≥1 dose of HPV vaccine and 63.4% were up to date with the HPV vaccination series. HPV vaccinati… |
| [[36]](https://www.nature.com/articles/s41591-023-02658-0) | #91, #94–95 | #90 | — | `#91` Overall, 2,275 healthy women aged 15–20 years were recruited and randomly assigned to receive bivalent (n = 760), nonavalent (n = 758) or control (n = 757) vac… |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/34741816/) | #27–28 | #26 | — | `#27` We used data from a total of 13·7 million-years of follow-up of women aged 20 years to younger than 30 years. The estimated relative reduction in cervical canc… |
| [[16]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7329692/) | #33–34, #36 | — | — | `#34` No cases of HPV16/18-related high-grade cervical dysplasia were observed in the per-protocol effectiveness population (N = 2121; 24,099·0 person-years of follo… |
| [[25]](https://www.who.int/publications-detail-redirect/who-wer9750-645-672) | — | — | #51–53 | — |
| [[28]](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/cervical-cancer-screening) | #68–70 | — | — | `#68` The first 3 recommendations apply to individuals who have a cervix, regardless of their sexual history or HPV vaccination status. [...] Update in Progress for… |
| [[29]](https://www.who.int/Publications/i/item/9789240014107) | #76 | #77, #100 | — | `#76` a threshold of 4 per 100 000 women-years for elimination as a public health problem; the following 90–70–90 targets that must be met by 2030 for countries to b… |
| [[5]](https://www.iarc.who.int/reference/carcinogenic-human-papillomavirus-infection) | #6 | #4 | — | `#6` Although the great majority of infections resolve within 2 years, 13 phylogenetically related, sexually transmitted HPV genotypes, notably HPV16, cause – if no… |
| [[9]](https://www.cdc.gov/united-states-cancer-statistics/publications/hpv-associated-cancers.html) | #15–16 | — | — | `#15` We estimated that 39,300 cancers (79%) were attributable to HPV each year during 2018 to 2022. Of these, we estimated that 36,400 cancers could have been preve… |
| [[14]](https://academic.oup.com/jnci/article/116/6/857/7577291) | #30–31 | — | — | `#30` No cases of invasive cancer were recorded in women immunized at 12 or 13 years of age irrespective of the number of doses. |
| [[22]](https://www.cdc.gov/vaccines/hcp/imz-schedules/adult-notes.html) | #47 | #46 | — | `#47` Pregnancy testing is not needed before vaccination. HPV vaccination is not recommended until after pregnancy. No intervention needed if inadvertently vaccinate… |
| [[24]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | — | #50 | #49 | `#50` This page summarizes CDC's current HPV vaccine recommendations. |
| [[30]](https://www.who.int/news-room/fact-sheets/detail/immunization-coverage) | #78 | #79 | — | `#78` Global coverage with the first dose of HPV vaccine among girls is now estimated at 33%. While still far from the 90% target by 2030, this represents a substant… |
| [[37]](https://pubmed.ncbi.nlm.nih.gov/34634254/) | #92, #96 | — | — | `#92` Vaccine efficacy against persistent HPV 16 and 18 infection among participants evaluable for the endpoint was 95·4% (95% CI 85·0-99·9) in the single-dose defau… |
| [[1]](https://www.iarc.who.int/reference/the-human-papillomavirus-family-and-its-role-in-carcinogenesis/) | #0 | — | — | `#0` Human papillomaviruses (HPVs) are a family of small double-stranded DNA viruses that have a tropism for the epithelia of the genital and upper respiratory trac… |
| [[3]](https://www.iarc.who.int/reference/are-20-human-papillomavirus-types-causing-cervical-cancer/) | — | #2 | — | `#2` In 2012, the International Agency for Research on Cancer concluded that there was consistent and sufficient epidemiological, experimental and mechanistic evide… |
| [[7]](https://www.iarc.who.int/cancer-type/cervical-cancer) | — | #12 | — | `#12` High incidence rates and high mortality rates of cervical cancer occur mainly (~90% for both) in low- and middle-income countries. |
| [[8]](https://seer.cancer.gov/statfacts/html/cervix.html) | #14 | — | — | `#14` In 2026, it is estimated that there will be 13,490 new cases of cervical cancer and an estimated 4,200 people will die of this disease. |
| [[10]](https://www.iarc.who.int/reference/effect-of-prophylactic-human-papillomavirus-l1-virus-like-particle-vaccine-on-risk-of-cervical-intraepithelial-neoplasia-grade-2-grade-3-and-adenocarcinoma-in-situ-a-combined-analysis-of-four-rando/) | — | #21 | — | `#21` In women negative for HPV16 or HPV18 infection during the vaccination regimen (n=17 129, per protocol), vaccine efficacy was 99% for the primary endpoint (95%… |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/38749552/) | #29 | — | — | `#29` the HPV vaccination programme had a large effect in all five levels of deprivation. In women offered catch-up vaccination, CIN3 rates decreased more in those f… |
| [[17]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8724969/) | #35 | — | — | `#35` We present results for the CVT and its long-term follow-up phase (LTFU), evaluating efficacy of the bivalent HPV vaccine to prevent HPV-16/18 associated cervic… |
| [[19]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/safety-and-effectiveness-data.html) | #41 | — | — | `#41` On very rare occasions, a person may have a serious allergic reaction (anaphylaxis) to any vaccine, including HPV vaccines. In the United States, anaphylaxis f… |
| [[20]](https://www.bmj.com/content/347/bmj.f5906) | #44 | — | — | `#44` This large cohort study found no evidence supporting associations between exposure to qHPV vaccine and autoimmune, neurological, and venous thromboembolic adve… |
| [[21]](https://www.who.int/publications/journals/weekly-epidemiological-record/wer101-34) | #45 | — | — | `#45` The Committee found no new adverse events of concern based on many very large, high-quality studies (GACVS 2017). However, safety concerns can be the basis for… |
| [[23]](https://cdn.who.int/media/docs/default-source/immunization/immunization_schedules/immunization-summary-table-2.pdf) | — | — | #48 ⚡ | `#48` The vaccine is contraindicated for mothers during breastfeeding. |
| [[31]](https://cdn.who.int/media/docs/default-source/immunization/wuenic/wuenic-progress-and-challenges.pdf) | #80 | — | — | `#80` 43.6Mn girls still did not receive the vaccine. - 22.8Mn (35% of the global cohort) live in a country where the vaccine is not part of the immunization program… |
| [[34]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/talking-with-parents.html) | #88 | — | — | `#88` Recommend HPV vaccination in the same way and on the same day you recommend other vaccines for adolescents. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.nejm.org/doi/full/10.1056/NEJMoa1917338 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.bmj.com/content/365/bmj.l1161 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://publications.aap.org/pediatrics/article/139/1/e20161764/51685/Announcements-Versus-Conversations-to-Improve-HPV — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://publications.aap.org/pediatrics/article/151/3/e2022058794/190722/Early-Initiation-of-HPV-Vaccination-and-Series — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-0`** [1]
  - Trecho: Human papillomaviruses (HPVs) are small double-stranded DNA viruses with tropism for squamous epithelia, and a subset of sexually transmitted mucosal HPV genotypes has a well-established causal role in cervical carcinog…
  - Justificativa: A evidência sustenta as partes essenciais da afirmação: HPVs são pequenos vírus de DNA dupla fita com tropismo por epitélios, e subtipos mucosais de HPV estão claramente associados ao câncer cervical. Aspectos como 'epi…
  - Suporte veio de: [1]
  - Evidência: “Human papillomaviruses (HPVs) are a family of small double-stranded DNA viruses that have a tropism for the epithelia of the genital and upper respiratory tracts and for the skin.”
  - Não coberto pela evidência: tropism for squamous epithelia (evidência diz 'epithelia of the genital and upper respiratory tracts and for the skin', sem especificar 'squamous'); sexually transmitted (evidência não menciona transmissão sexual); causal role (evidência diz 'clearly associated with', não explicitamente 'causal')
- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-1`** [2]
  - Trecho: Most genital HPV infections are transient and are controlled by the immune system, but persistent infection with a carcinogenic HPV type is the necessary causal precursor of virtually all cervical cancers.
  - Justificativa: A evidência afirma explicitamente que 'quase todos os casos de câncer cervical são causados por infecção com tipos oncogênicos de HPV' e que 'cerca de 95% dos cânceres cervicais' decorrem de infecção persistente. Também…
  - Suporte veio de: [2]
  - Evidência: “Almost all cases of cervical cancer are caused by infection with oncogenic types of human papillomavirus (HPV).”
- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-3`** [4]
  - Trecho: Current WHO estimates attribute approximately 76%–77% of cervical cancers to HPV16 and HPV18 together.
  - Justificativa: A evidência, proveniente de documento da OMS, afirma que os tipos de HPV 16 e 18 são juntos responsáveis por aproximadamente 77% dos casos de câncer cervical globalmente, o que sustenta a afirmação de que estimativas at…
  - Suporte veio de: [4]
  - Evidência: “All vaccines are highly efficacious in preventing infection with virus types 16 and 18, which are together responsible for approximately 77%% of cervical cancer cases globally.”
  - Não coberto pela evidência: O limite inferior de 76% não é explicitamente mencionado na evidência, que cita apenas 'aproximadamente 77%'.
### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-2`** [3]
  - Trecho: The International Agency for Research on Cancer (IARC) has classified 12 HPV types as carcinogenic to humans in relation to cervical cancer, with HPV16 and HPV18 accounting for the largest share of disease.
  - Justificativa: A evidência confirma que a IARC classificou 12 tipos de HPV como carcinogênicos (grupo 1A) para câncer cervical, listando-os explicitamente. No entanto, a afirmação de que 'HPV16 e HPV18 respondem pela maior parcela da…
  - Suporte veio de: [3]
  - Evidência: “In 2012, the International Agency for Research on Cancer concluded that there was consistent and sufficient epidemiological, experimental and mechanistic evidence of carcinogenicity to humans for 12 HPV types (HPV16, HP…”
  - Não coberto pela evidência: A afirmação de que HPV16 e HPV18 respondem pela maior parcela da doença (largest share of disease) não está explicitamente sustentada na evidência.
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [1] [17] [10] [2] [16] [9] [5] [7] [19] [8] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-4`** [5]
  - Trecho: The causal pathway is biologically coherent as well as epidemiologically established: persistent high-risk HPV infection can evolve from productive infection toward transforming infection, while the viral E6 and E7 onco…
  - Justificativa: A evidência sustenta parte da afirmação (transição de infecção produtiva para transformadora e atividade de E6/E7 em vias regulatórias de crescimento), mas não menciona especificamente 'vias de ciclo celular, apoptótica…
  - Suporte veio de: [5]
  - Evidência: “Persistent high-risk HPVs can transition from a productive (virion-producing) to an abortive or transforming infection”
  - Não coberto pela evidência: cell-cycle pathways; apoptotic pathways; genome-maintenance pathways
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [1] [28] [36] [3] [17] [16] [9] [25] [7] [18] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-17`** [4]
  - Trecho: HPV vaccine development has progressed from bivalent vaccines directed principally at HPV16 and HPV18, through quadrivalent vaccines adding HPV6 and HPV11, to nonavalent vaccines that additionally cover HPV31, 33, 45, 5…
  - Justificativa: A evidência confirma a composição dos tipos de vacina (bivalente para HPV16/18, quadrivalente adicionando HPV6/11, nonavalente adicionando HPV31/33/45/52/58), mas não descreve uma progressão cronológica de desenvolvimen…
  - Suporte veio de: [4]
  - Evidência: “Currently there are nine licensed HPV vaccines: three bivalent, one trivalent, three quadrivalent, and two nonavalent vaccine”
  - Não coberto pela evidência: Progressão cronológica de desenvolvimento 'do bivalente ao quadrivalente ao nonavalente'; Vacinas bivalentes 'dirigidas principalmente ao HPV16 e HPV18' (a evidência diz que 'todas as vacinas' são eficazes contra 16 e 18, não especifica que as bivalentes são dirigidas principalmente a esses tipos); Ausência de menção à vacina trivalente na afirmação, que consta na evidência
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [17] [36] [9] [6] [16] [25] [37] [19] [3] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-48`** [23]
  - Trecho: Breastfeeding is not considered a contraindication under WHO guidance.
  - Justificativa: A afirmação generaliza que amamentação não é contraindicação sob orientação da OMS, mas a evidência mostra que isso depende do vacina. Para a vacina TAK-003, a evidência afirma explicitamente: 'The vaccine is contraindi…
  - Evidência: “The vaccine is contraindicated for mothers during breastfeeding.”
  - Não coberto pela evidência: A afirmação não especifica a qual vacina se refere, tratando-se de uma declaração geral sobre orientação da OMS
- **Trecho citado `vacinacao_hpv_acc5fdffce00_20261115T054744Z-58`** [27]
  - Trecho: Routine HPV vaccination is recommended at age 11–12, vaccination may begin at age 9, and catch-up vaccination is recommended for everyone who is not adequately vaccinated through age 26.
  - Justificativa: A evidência confirma a vacinação de rotina aos 11-12 anos e que pode iniciar aos 9 anos, mas contradiz explicitamente a idade de catch-up: a evidência diz 'through age 18 years', enquanto a afirmação diz 'through age 26…
  - Suporte veio de: [27]
  - Evidência: “HPV vaccination routinely recommended at **age 11–12 years (can start at age 9 years)** and catch-up HPV vaccination recommended for all persons through age 18 years if not adequately vaccinated”
  - Não coberto pela evidência: catch-up vaccination recommended for everyone who is not adequately vaccinated through age 26

---

## 10. Trechos Citados Não Auditados

Motivos: 9 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-22` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-23` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-24` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-25` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-32` — Referencia(s) citada(s) ['717164fa9556ab45'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-86` — Referencia(s) citada(s) ['2c1018c3a3d7e426'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-87` — Referencia(s) citada(s) ['2c1018c3a3d7e426'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-89` — Referencia(s) citada(s) ['9bd1bf297cf87fa6'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_acc5fdffce00_20261115T054744Z-98` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.