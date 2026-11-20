# Relatório de Auditoria — Claude (vacinacao_hpv_704170a7032a_20261115T024026Z)

**Arquivo auditado:** `answers/Ingles/Claude/Consolidado/vacinacao_hpv.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_704170a7032a_20261115T024026Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-18T10:36:36.650960+00:00 |
| **Total de trechos citados** | 81 |
| **Tempo de processamento** | 2:22:35:19 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 29.1 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 93 marcadores, 48 distintos |
| Referências listadas | 48 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 37 | 45.7% |
| **UNSUPPORTED** | 12 | 14.8% |
| **CONTRADICTED** | 1 | 1.2% |
| **SKIPPED** | 31 | 38.3% |
| **TOTAL** | 81 | 100.0% |

Sobre os 50 trechos citados auditados: SUPPORTED 74,00%, UNSUPPORTED 24,00%, CONTRADICTED 2,00%.

> **7 dos 37 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 7 estão **contados dentro** dos 37 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`14` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `2` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#26` Innovax's Cecolin, a bivalent vaccine made in *E. coli*, was licensed in China in December 2019 and in 2021 became the… | [11] | [1] [12] [10] [15] [34] [13] [16] [30] [39] [20] | — |
| `#59` GACVS had warned in 2015 that policy decisions based on weak evidence cause "real harm." In Denmark, uptake fell to 49.… | [34] | [36] [42] [37] [23] [2] [6] [7] [10] | — |
| `#76` With global incidence at 14.1 per 100,000, most of the world remains several times above the threshold. | [2] | [45] [7] [41] [8] [34] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 635676 |
| **Média de tokens por requisição** | 12713.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/48 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[9]](https://who.int/publications/i/item/who-wer9750-645-672 (full text PDF: https://www.iccp-portal.org/sites/default/files/resources/WER9750-645-672-eng-fre.pdf)) | blocked | 15 | 0 | 0 | 0 | 15 |
| [[2]](https://pmc.ncbi.nlm.nih.gov/articles/12276544) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[32]](https://www.ajc.com/news/2026/09/one-shot-or-two-what-to-know-about-hpv-vaccination-recommendations/) | downloaded | 5 | 1 | 3 | 1 | 0 |
| [[1]](https://who.int/news/item/04-10-2024-who-adds-an-hpv-vaccine-for-single-dose-use) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[8]](https://www.who.int/news/item/19-08-2020-world-health-assembly-adopts-global-strategy-to-accelerate-cervical-cancer-elimination) | downloaded | 4 | 0 | 3 | 0 | 1 |
| [[3]](https://es.cochrane.org/sites/es.cochrane.org/files/uploads/Embargos/2025/embargoed_24nov2025_effects-of-human-papillomavirus--hpv--vaccinationprogrammes-on-community-rates-of-hpv-related-diseaseand-harms-from-vaccination.pdf (PubMed: https://pubmed.ncbi.nlm.nih.gov/41276263/)) | dead | 3 | 0 | 0 | 0 | 3 |
| [[4]](https://academic.oup.com/jnci/article/116/6/857/7577291) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[6]](https://www.healio.com/news/infectious-disease/20260114/study-dose-of-hpv-vaccine-on-par-with-dose) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[7]](https://data.unicef.org/wp-content/uploads/2026/07/WUENIC-progress-and-challenges.pdf) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[10]](https://www.frontiersin.org/articles/10.3389/fimmu.2020.01434) | downloaded | 3 | 2 | 0 | 0 | 1 |
| [[35]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10920980) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/41337735/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[30]](https://www.iarc.who.int/news-events/a-prospective-cohort-study-comparing-efficacy-of-1-dose-of-quadrivalent-human-papillomavirus-vaccine-to-2-and-3-doses-at-an-average-follow-up-of-12-years-postvaccination) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[31]](https://www.nih.gov/news-events/nih-research-matters/one-dose-hpv-vaccine-effective-two) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[34]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[47]](https://pressroom.cancer.org/updated-cervical-cancer-screening-guidelines-2025) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[11]](https://www.path.org/our-impact/media-center/new-hpv-vaccine-innovax-receives-who-prequalification/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[12]](https://path.org/our-impact/media-center/new-hpv-vaccine-from-zerun-bio-receives-who-prequalification) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[13]](https://www.indianpharmapost.com/rd/lite/indias-cervavac-gets-who-prequalification-22081) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[14]](https://extranet.who.int/prequal/vaccines/p/cervavac) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[15]](https://www.chinadaily.com.cn/a/202505/30/WS683968e5a310a04af22c284e.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[16]](https://www.merics.org/en/comment/newly-approved-homegrown-hpv-vaccine-closes-gap-us) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[17]](https://www.nejm.org/doi/full/10.1056/NEJMoa061741) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[18]](https://www.nejm.org/doi/full/10.1056/NEJMoa061760) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://pubmed.ncbi.nlm.nih.gov/22075171/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://www.nejm.org/doi/full/10.1056/NEJMoa1405044) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[21]](https://doi.org/10.1016/S0140-6736(17)31821-4) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[22]](https://www.eurekalert.org/news-releases/1106620) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://absolutelymaybe.plos.org/2025/11/24/this-evidence-fundamentally-shifts-the-debate-about-the-hpv-vaccine/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://www.nejm.org/doi/full/10.1056/NEJMoa1917338) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[25]](https://doi.org/10.1093/jnci/djab080) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[26]](https://doi.org/10.1016/S0140-6736(21)02178-4) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[27]](https://www.bmj.com/content/385/bmj-2023-077341) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://jamanetwork.com/journals/jama/fullarticle/10.1001/jama.2024.22169) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[29]](https://doi.org/10.1016/S0140-6736(19)30298-3) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[33]](https://doi.org/10.1056/EVIDoa2100056) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[36]](https://research.cbs.dk/en/publications/resilience-of-hpv-vaccine-uptake-in-denmark-decline-and-recovery/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://www.vaccinestoday.eu/stories/ireland-rescued-falling-hpv-vaccination-rates/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://www.who.int/news/item/20-12-2022-WHO-updates-recommendations-on-hpv-vaccination-schedule) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://cdn.who.int/media/docs/default-source/immunization/wuenic/notes_who_unicef_hpv_estimates_2025.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://www.gavi.org/news/document-library/03b-annex-b-hpv-revitalisation-update-pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[41]](https://www.gavi.org/news/media-room/cervical-cancer-vaccines-save-over-1-million-lives-lower-income-countries) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[42]](https://www.kff.org/other-health/the-new-federal-vaccine-schedule-what-changed/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://www.cidrap.umn.edu/childhood-vaccines/federal-judge-blocks-kennedy-s-changes-childhood-vaccine-policy) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[44]](https://www.pharmacytimes.com/view/overhaul-of-childhood-vaccine-guidance-blocked-by-federal-judge-in-massachusetts) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://who.int/publications/i/item/9789240014107) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[46]](https://doi.org/10.1016/S2468-2667(18)30183-X) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[48]](https://epocrates.com/online/article/uspstf-adds-self-testing-option-for-cervical-cancer-screening) | blocked | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://pmc.ncbi.nlm.nih.gov/articles/12276544) | #1, #16–17, #19 | #76 | — | `#1` Globally, an estimated 662,044 cases (ASIR: 14.12/100,000) and 348,709 deaths (ASMR: 7.08/100,000) from cervical cancer occurred in 2022 |
| [[32]](https://www.ajc.com/news/2026/09/one-shot-or-two-what-to-know-about-hpv-vaccination-recommendations/) | #53 | #69, #72–73 | #50 | `#53` rehtehw saw ot yeht ereht ereht eht eht tneiciffus tneiciffus gniwohs tohs tohs ksir .weiver noitcetorp gnitneverp rehto eno eno no fo ssel gnikcal sdnik si si… |
| [[1]](https://who.int/news/item/04-10-2024-who-adds-an-hpv-vaccine-for-single-dose-use) | #0, #18, #63 | — | #28 ⚡ | `#0` More than 95% of the 660 000 cervical cancer cases occurring globally each year are caused by HPV. Every two minutes, a woman dies from this preventable diseas… |
| [[8]](https://www.who.int/news/item/19-08-2020-world-health-assembly-adopts-global-strategy-to-accelerate-cervical-cancer-elimination) | — | #5–6, #74 | #75 (pulado) | `#5` 90% of girls fully vaccinated with the HPV vaccine by the age of 15 |
| [[6]](https://www.healio.com/news/infectious-disease/20260114/study-dose-of-hpv-vaccine-on-par-with-dose) | #49, #56 | #4 | — | `#49` The effectiveness of one dose of either bivalent or nonvalent HPV vaccines was noninferior to receiving two doses. |
| [[7]](https://data.unicef.org/wp-content/uploads/2026/07/WUENIC-progress-and-challenges.pdf) | #66–67 | #5 | — | `#66` 43.6Mn girls still did not receive the vaccine. 22.8Mn (35% of the global cohort) live in a country where the vaccine is not part of the immunization programme. |
| [[10]](https://www.frontiersin.org/articles/10.3389/fimmu.2020.01434) | #11, #25 | — | #23 (pulado) | `#11` E7 promotes DNA synthesis by interacting with retinoblastoma proteins (). |
| [[35]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10920980) | #57–58 | #80 | — | `#57` In April 2022, they issued a notice to local governments nationwide to restart their own active vaccination recommendations. |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/41337735/) | #4, #47 | — | — | `#4` A total of 20,330 participants were enrolled and underwent randomization, and 3005 unvaccinated participants were enrolled in the survey. The noninferiority an… |
| [[30]](https://www.iarc.who.int/news-events/a-prospective-cohort-study-comparing-efficacy-of-1-dose-of-quadrivalent-human-papillomavirus-vaccine-to-2-and-3-doses-at-an-average-follow-up-of-12-years-postvaccination) | #46 | — | #52 (pulado) | `#46` No high-grade cervical precancer associated with HPV16 and 18 was detected among vaccinated participants. |
| [[31]](https://www.nih.gov/news-events/nih-research-matters/one-dose-hpv-vaccine-effective-two) | #48–49 | — | — | `#48` Girls 15 and older were then tested for new HPV infections every 6 months for five years. |
| [[34]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | #54 | #59 | — | `#54` The risk of anaphylaxis has been characterized as approximately 1.7 cases per million doses, and syncope was established as a common anxiety or stress-related… |
| [[47]](https://pressroom.cancer.org/updated-cervical-cancer-screening-guidelines-2025) | #78 | — | #79 (pulado) | `#78` ACS recommends that average-risk women and individuals with a cervix at average risk initiate cervical cancer screening at age 25 and undergo primary HPV testi… |
| [[11]](https://www.path.org/our-impact/media-center/new-hpv-vaccine-innovax-receives-who-prequalification/) | — | #26 | — | `#26` Cecolin is designed to protect against HPV types 16 and 18 |
| [[12]](https://path.org/our-impact/media-center/new-hpv-vaccine-from-zerun-bio-receives-who-prequalification) | #27 | — | — | `#27` Walrinvax is manufactured by Yuxi Zerun Biotechnology Co., Ltd. in Yuxi City, Yunnan Province, China, a fully owned subsidiary of Shanghai Zerun Biotechnology… |
| [[13]](https://www.indianpharmapost.com/rd/lite/indias-cervavac-gets-who-prequalification-22081) | — | #29 | — | `#29` India's first indigenously developed gender-neutral quadrivalent human papillomavirus (qHPV) vaccine, CERVAVAC, developed by the Serum Institute of India, has… |
| [[14]](https://extranet.who.int/prequal/vaccines/p/cervavac) | — | #29 | — | `#29` Human Papillomavirus (Quadrivalent) |
| [[15]](https://www.chinadaily.com.cn/a/202505/30/WS683968e5a310a04af22c284e.html) | — | #30 | — | `#30` China approved its first domestically developed nine-valent human papillomavirus (HPV) vaccine on Thursday |
| [[16]](https://www.merics.org/en/comment/newly-approved-homegrown-hpv-vaccine-closes-gap-us) | — | #30 | — | `#30` China’s National Medical Products Administration (NMPA) in June approved a new human papillomavirus (HPV) vaccine, Cecolin 9 |
| [[18]](https://www.nejm.org/doi/full/10.1056/NEJMoa061760) | #33 | — | — | `#33` In the type-specific, per-protocol susceptible populations, in the analysis for cervical end points, among 2241 subjects in the vaccine group and 2258 in the p… |
| [[19]](https://pubmed.ncbi.nlm.nih.gov/22075171/) | #34 | — | — | `#34` against all CIN3+ (irrespective of HPV type in the lesion and including lesions with no HPV DNA detected) was 93·2% (78·9-98·7) in the TVC-naive and 45·6% (28·… |
| [[22]](https://www.eurekalert.org/news-releases/1106620) | #36 | — | — | `#36` The first review focused on randomized controlled trials and included 60 studies with 157,414 participants. [...] vaccines such as Cervarix, Gardasil, and Gard… |
| [[23]](https://absolutelymaybe.plos.org/2025/11/24/this-evidence-fundamentally-shifts-the-debate-about-the-hpv-vaccine/) | #37 | — | — | `#37` We don't have randomized evidence for the under-15 target population. |
| [[27]](https://www.bmj.com/content/385/bmj-2023-077341) | #41 | — | — | `#41` The greatest numbers for cervical cancer were prevented in women in the most deprived areas (192 and 199 for first and second fifths, respectively) and the few… |
| [[36]](https://research.cbs.dk/en/publications/resilience-of-hpv-vaccine-uptake-in-denmark-decline-and-recovery/) | #60 | — | — | `#60` After the information campaign, HPV vaccine uptake recovered to its baseline level (109.2%, 95% CI:90.1%–132.4%) due in part to catch-up doses. Despite the rec… |
| [[37]](https://www.vaccinestoday.eu/stories/ireland-rescued-falling-hpv-vaccination-rates/) | #61 | — | — | `#61` Provisional data for the 2017/2018 HPV school campaign shows uptake of 61% for dose 1 of HPV vaccine, says Dr Brenda Corcoran who leads the Health Service Exec… |
| [[38]](https://www.who.int/news/item/20-12-2022-WHO-updates-recommendations-on-hpv-vaccination-schedule) | #62 | — | — | `#62` The recommendation for alternative single-dose scheduling was initially made by WHO's independent expert advisory group, SAGE in April 2022. ... A one or two-d… |
| [[39]](https://cdn.who.int/media/docs/default-source/immunization/wuenic/notes_who_unicef_hpv_estimates_2025.pdf) | #64 | — | — | `#64` 147 (out of respectively 194 WHO and 195) UNICEF Member States) had introduced HPV vaccine for girls in the national immunization schedule by 31 December 2024.… |
| [[40]](https://www.gavi.org/news/document-library/03b-annex-b-hpv-revitalisation-update-pdf) | — | — | #65 | — |
| [[41]](https://www.gavi.org/news/media-room/cervical-cancer-vaccines-save-over-1-million-lives-lower-income-countries) | — | #68 | — | `#68` the price of HPV vaccines in Gavi-supported countries is now between US$ 2.90 and US$ 5.18 per dose, compared with US$ 100 or more elsewhere |
| [[42]](https://www.kff.org/other-health/the-new-federal-vaccine-schedule-what-changed/) | #70 | — | — | `#70` now that the federal government recommends just one dose of HPV (instead of the previously recommended two to three doses), insurers will not be required to co… |
| [[43]](https://www.cidrap.umn.edu/childhood-vaccines/federal-judge-blocks-kennedy-s-changes-childhood-vaccine-policy) | #71 | — | — | `#71` A federal judge in Boston has temporarily blocked the Trump administration's changes to the US childhood immunization schedule. ... The ruling, which will like… |
| [[44]](https://www.pharmacytimes.com/view/overhaul-of-childhood-vaccine-guidance-blocked-by-federal-judge-in-massachusetts) | #71 | — | — | `#71` Murphy also stayed the reconstitution of the Advisory Committee on Immunization Practices (ACIP), as well as all votes taken by the now-stayed ACIP since its r… |
| [[45]](https://who.int/publications/i/item/9789240014107) | — | #74 | — | `#74` a threshold of 4 per 100 000 women-years for elimination as a public health problem |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://es.cochrane.org/sites/es.cochrane.org/files/uploads/Embargos/2025/embargoed_24nov2025_effects-of-human-papillomavirus--hpv--vaccinationprogrammes-on-community-rates-of-hpv-related-diseaseand-harms-from-vaccination.pdf (PubMed: https://pubmed.ncbi.nlm.nih.gov/41276263/) — Referencia nao encontrada (404): https://es.cochrane.org/sites/es.cochrane.org/files/uploads/Embargos/2025/embargoed_24nov2025_effects-of-human-papillomavirus--hpv--vaccinationprogrammes-on-community-rates-of-hpv-related-diseaseand-harms-from-vaccination.pdf (PubMed: https://pubmed.ncbi.nlm.nih.gov/41276263/)

### Bloqueadas por barreira de acesso

- https://academic.oup.com/jnci/article/116/6/857/7577291 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://who.int/publications/i/item/who-wer9750-645-672 (full text PDF: https://www.iccp-portal.org/sites/default/files/resources/WER9750-645-672-eng-fre.pdf) — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. The action you just performed triggered 
- https://www.nejm.org/doi/full/10.1056/NEJMoa061741 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1016/S0140-6736(17)31821-4 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.nejm.org/doi/full/10.1056/NEJMoa1917338 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1093/jnci/djab080 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1016/S0140-6736(21)02178-4 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://jamanetwork.com/journals/jama/fullarticle/10.1001/jama.2024.22169 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1016/S0140-6736(19)30298-3 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1056/EVIDoa2100056 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1016/S2468-2667(18)30183-X — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://epocrates.com/online/article/uspstf-adds-self-testing-option-for-cervical-cancer-screening — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-0`** [1]
  - Trecho: HPV causes more than 95% of cervical cancers, and about 90% of cervical cancer deaths occur in low- and middle-income countries.
  - Justificativa: A evidência afirma explicitamente que mais de 95% dos casos de câncer cervical são causados por HPV e que 90% das mortes por essa doença ocorrem em países de baixa e média renda, sustentando diretamente a afirmação.
  - Suporte veio de: [1]
  - Evidência: “More than 95% of the 660 000 cervical cancer cases occurring globally each year are caused by HPV. Every two minutes, a woman dies from this preventable disease globally, and 90% of these deaths occur in low- and middle…”
- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-1`** [2]
  - Trecho: In 2022 the disease caused an estimated 662,044 new cases and 348,709 deaths.
  - Justificativa: A evidência afirma explicitamente que, em 2022, ocorreram globalmente 662.044 casos e 348.709 mortes por câncer cervical, o que corresponde exatamente à afirmação.
  - Suporte veio de: [2]
  - Evidência: “Globally, an estimated 662,044 cases (ASIR: 14.12/100,000) and 348,709 deaths (ASMR: 7.08/100,000) from cervical cancer occurred in 2022”
- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-4`** [5] [6]
  - Trecho: In December 2025 a randomized trial in 20,330 Costa Rican girls showed that **one dose protected as well as two** against persistent HPV16/18 infection.
  - Justificativa: A evidência sustenta explicitamente os elementos essenciais da afirmação: o estudo randomizado com 20.330 participantes, publicado em dezembro de 2025 (NEJM, 18 dez 2025), demonstrou que uma dose foi não-inferior a duas…
  - Suporte veio de: [5] [6]
  - Evidência: “A total of 20,330 participants were enrolled and underwent randomization”
  - Não coberto pela evidência: Nacionalidade das participantes ('Costa Rican girls') — a evidência não afirma explicitamente que as 20.330 participantes são costa-riquenhas; apenas indica que a instituição de pesquisa é da Costa Rica.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | sustenta | A total of 20,330 participants were enrolled and underwent randomization, and 3005 unvaccinated participants were enrol… |
    | [6] | parcial | To assess the effectiveness of one vs. two doses, the researchers enrolled 20,330 girls aged 12 to 16 years and randoml… |

### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-6`** [8]
  - Trecho: Vaccinated cohorts will take decades to reach the ages of peak risk, so screening and treatment remain essential to WHO's goal of incidence below 4 per 100,000 women in every country.
  - Justificativa: A evidência sustenta que a meta da OMS é incidência abaixo de 4 por 100.000 mulheres e que triagem e tratamento são pilares essenciais da estratégia. Porém, a afirmação específica de que 'as coortes vacinadas levarão dé…
  - Suporte veio de: [8]
  - Evidência: “To eliminate cervical cancer, all countries must reach and maintain an incidence rate of below four per 100 000 women.”
  - Não coberto pela evidência: Vaccinated cohorts will take decades to reach the ages of peak risk
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-26`** [11]
  - Trecho: Innovax's Cecolin, a bivalent vaccine made in *E. coli*, was licensed in China in December 2019 and in 2021 became the fourth HPV vaccine prequalified by WHO.
  - Justificativa: A evidência sustenta que Cecolin é da Innovax, protege contra dois tipos de HPV (16 e 18, portanto bivalente), é produzido em *E. coli*, foi licenciado na China em dezembro de 2019, e que apenas três outras vacinas cont…
  - Suporte veio de: [11]
  - Evidência: “Cecolin is manufactured by Xiamen Innovax Biotech CO., LTD. (Innovax)”
  - Não coberto pela evidência: o ano de 2021 como o ano em que Cecolin se tornou a quarta vacina contra HPV pré-qualificada pela OMS
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [1] [12] [10] [15] [34] [13] [16] [30] [39] [20] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-29`** [13] [14]
  - Trecho: The Serum Institute of India's quadrivalent Cervavac, licensed for girls and boys aged 9–26, was prequalified effective 25 September 2026.
  - Justificativa: A evidência confirma que CERVAVAC, vacina quadrivalente do Serum Institute of India, indicada para meninos e meninas de 9 a 26 anos, recebeu pré-qualificação da OMS. No entanto, a data específica de '25 September 2026'…
  - Suporte veio de: [13]
  - Evidência: “CERVAVAC targets HPV types 6, 11, 16 and 18 and is indicated for both girls and boys aged 9 to 26 years.”
  - Não coberto pela evidência: Data específica de pré-qualificação: '25 September 2026' — não mencionada na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [13] | parcial | India's first indigenously developed gender-neutral quadrivalent human papillomavirus (qHPV) vaccine, CERVAVAC, develop… |
    | [14] | parcial | Human Papillomavirus (Quadrivalent) |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `vacinacao_hpv_704170a7032a_20261115T024026Z-28`** [1]
  - Trecho: WHO prequalified it in August 2024 as the fifth HPV vaccine, and in October 2024 WHO cleared Cecolin for single-dose use.
  - Justificativa: A evidência contradiz a afirmação de que Cecolin foi prequalificada como a quinta vacina HPV. A evidência afirma que Cecolin foi a QUARTA vacina HPV prequalificada pela WHO, e que a QUINTA foi Walrinvax®, prequalificada…
  - Suporte veio de: [1]
  - Evidência: “WHO announced that a fourth WHO-prequalified human papillomavirus (HPV) vaccine product, Cecolin® has been confirmed for use in a single-dose schedule.”
  - Não coberto pela evidência: Data de outubro de 2024 para autorização de uso em dose única de Cecolin não está mencionada na evidência
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência confirma que em agosto de 2024 a WHO prequalificou Walrinvax® como o quinto (fifth) produto de vacina HPV, e que Cecolin® foi c…") — cascata: baseline → context_expansion

---

## 10. Trechos Citados Não Auditados

Motivos: 5 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 23 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 3 citam referência não baixada/inacessível.

- `vacinacao_hpv_704170a7032a_20261115T024026Z-2` — Referencia(s) citada(s) ['ce9d9c9ced459706'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_704170a7032a_20261115T024026Z-3` — Referencia(s) citada(s) ['e872d145d17252c4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-7` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-8` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-9` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-10` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-12` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-13` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-14` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-15` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-20` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-21` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-22` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-24` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-31` — Referencia(s) citada(s) ['2d4ca675eae5da0c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-32` — Referencia(s) citada(s) ['b8bc35059eb26eac'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-38` — Referencia(s) citada(s) ['a4a95ddcdd2bb3e3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-39` — Referencia(s) citada(s) ['39587ddb7a96464b'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-40` — Referencia(s) citada(s) ['1b487e7dc6420bb2'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-42` — Referencia(s) citada(s) ['e872d145d17252c4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-43` — Referencia(s) citada(s) ['e51c4105a9108dfc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-44` — Referencia(s) citada(s) ['ce9d9c9ced459706'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_704170a7032a_20261115T024026Z-45` — Referencia(s) citada(s) ['e5b6d62de8f7159f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-51` — Referencia(s) citada(s) ['fedc75c30ce10387'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-55` — Referencia(s) citada(s) ['ce9d9c9ced459706'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_704170a7032a_20261115T024026Z-77` — Referencia(s) citada(s) ['ade3770d9e3f7a81'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-23` — Parte das fontes citadas sem conteudo: referencia(s) ['2d4ca675eae5da0c'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-35` — Parte das fontes citadas sem conteudo: referencia(s) ['755844a7d53f7b87'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-52` — Parte das fontes citadas sem conteudo: referencia(s) ['e872d145d17252c4'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-75` — Parte das fontes citadas sem conteudo: referencia(s) ['2d4ca675eae5da0c'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_704170a7032a_20261115T024026Z-79` — Parte das fontes citadas sem conteudo: referencia(s) ['9bdb84f73b08bdb0'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.