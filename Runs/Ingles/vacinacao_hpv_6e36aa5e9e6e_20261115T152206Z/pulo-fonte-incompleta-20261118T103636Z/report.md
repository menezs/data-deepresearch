# Relatório de Auditoria — Gemini (vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Consolidado/vacinacao_hpv.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T01:09:31.462035+00:00 |
| **Total de trechos citados** | 124 |
| **Tempo de processamento** | 2:09:47:25 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3131.5 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-15 15:22:28+00:00 |
| Citações no corpo | 250 marcadores, 86 distintos |
| Referências listadas | 83 (0 nunca citadas) |

> 86 números de citação distintos no corpo para apenas 83 referências listadas — há marcadores `[N]` sem entrada correspondente.

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 46 | 37.1% |
| **UNSUPPORTED** | 66 | 53.2% |
| **CONTRADICTED** | 3 | 2.4% |
| **SKIPPED** | 9 | 7.3% |
| **TOTAL** | 124 | 100.0% |

Sobre os 115 trechos citados auditados: SUPPORTED 40,00%, UNSUPPORTED 57,39%, CONTRADICTED 2,60%.

> **29 dos 46 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 29 estão **contados dentro** dos 46 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`74` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `19` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `27` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#5` Second, the WHO prequalification of lower-cost recombinant vaccines manufactured in China and India—most recently the S… | [14] [15] [16] | [46] [38] [47] [8] [58] [39] [71] [77] [45] [3] [72] | — |
| `#7` Cervical cancer persists as one of the leading causes of preventable cancer morbidity and mortality worldwide, although… | [1] [21] | [28] [26] [71] [67] [32] [8] [69] | — |
| `#19` Human papillomaviruses constitute a family of more than 200 known non-enveloped, double-stranded circular DNA viruses t… | [2] [29] | [30] [3] [38] [35] [28] [81] [8] [26] [58] [80] [32] [36] | — |
| `#31` While early productive infections maintain viral DNA episomally, progression to malignancy frequently involves integrat… | [30] [34] | — | [80] [35] [3] [28] [38] [81] ⚠ |
| `#44` Intramuscular immunization induces vigorous humoral immunity, generating neutralizing antibody titers far exceeding tho… | [2] [12] [13] | [49] [38] [80] [55] [81] [50] [68] [18] | — |
| `#53` Xiamen Innovax Biotech's bivalent Cecolin, licensed in China in December 2019 using an Escherichia coli expression plat… | [15] [38] [46] | [45] [39] [58] [4] [16] [11] [51] | — |
| `#61` Across the combined FUTURE I and II programs, per-protocol efficacy reached 99.0% against genital warts, 100% against H… | [51] [52] | [43] [68] [50] [5] [40] | — |
| `#75` Synthesizing this observational and trial literature, two comprehensive Cochrane systematic reviews published in Novemb… | [9] [19] [59] | [58] [7] [55] [13] | — |
| `#77` Originally introduced on three-dose schedules (at 0, 1–2, and 6 months) and streamlined to two doses spaced 6 to 12 mon… | [38] [60] | [17] [6] [43] [19] [59] [49] [63] [46] [11] [55] [13] [58] [67] [51] | — |
| `#79` Although single-dose regimens generate lower peak and plateau antibody titers than two- or three-dose schedules, the re… | [19] [61] | [49] [38] [20] [60] [66] [6] [50] [40] [43] | — |
| `#81` In Kenya, the randomized, double-blind, delayed-crossover KEN SHE trial enrolled 2,275 sexually active women aged 15 to… | [62] | [60] [66] [61] [4] [40] [13] [6] [58] | — |
| `#82` Blinded crossover extension through 54 months confirmed sustained, non-waning vaccine efficacy of 99.2% (95% CI: 96.1%–… | [62] | [61] [51] [40] [6] | — |
| `#83` To bridge those clinical findings down to preadolescents, the randomized DoRIS trial in Tanzania demonstrated that sing… | [61] [63] | [62] [60] [51] [50] [66] [43] [40] [13] | — |
| `#86` Both vaccines satisfied non-inferiority (p < 0.001), with reported one-dose minus two-dose infection rate differences o… | [64] | [6] [63] [13] [43] | — |
| `#89` Meanwhile, the ongoing PRISMA ESCUDDO trial is assessing single-dose protection against cervical, anal, and oral persis… | [65] | [64] [13] [51] [63] [20] [19] [40] [6] [60] [12] | — |
| `#92` Following its December 2022 off-label guidance endorsing one or two doses for females aged 9 to 20 and two doses six mo… | [11] [60] [66] | [65] [59] [38] [49] [71] [67] [13] [46] [63] [6] [62] | — |
| `#93` Early high-income adopters of single-dose policies include the United Kingdom (since September 2023), Australia, Canada… | [60] [67] | [59] [71] [20] [66] [4] [26] [55] | — |
| `#96` Implementation research in Eswatini, Malawi, and Uganda indicates that delivering differentiated multidose schedules to… | [68] | [67] [26] | — |
| `#98` Randomized trials consistently demonstrate that local injection-site pain and mild reactogenicity occur slightly more o… | [44] [50] [69] | [43] [51] [40] [17] [58] | — |
| `#99` In ESCUDDO, Grade 3 or higher adverse event rates were comparable across one-dose and two-dose arms and across bivalent… | [6] [64] | [63] [13] [58] [43] [12] [49] | — |
| `#100` Public hesitancy has periodically centered on social-media-amplified claims linking HPV vaccination to infertility, neu… | [9] [19] [59] | [58] [66] [40] [17] [49] [55] | — |
| `#103` In November 2020, the World Health Assembly adopted the WHO Global Strategy to Accelerate the Elimination of Cervical C… | [1] [70] | [69] [26] [22] [73] [71] [77] [15] [8] [28] | — |
| `#105` Mathematical modeling for LMICs projects that meeting these 2030 benchmarks will reduce median cervical cancer incidenc… | [1] [70] | [69] [28] [26] [77] [71] [73] | — |
| `#110` When measured across all age-eligible girls worldwide—accounting for populous nations lacking free routine adolescent p… | [60] [71] | — | [66] [77] [28] [72] [26] ⚠ |
| `#112` Bridging the remaining gap requires sustained financing, school- and community-based outreach to out-of-school girls, i… | [10] [71] [74] | [28] [66] [27] [26] [67] [77] [55] [18] [58] [73] | — |
| `#116` Adjunctive biomarkers such as E6/E7 mRNA assays offer improved specificity over HPV DNA detection for CIN2+ in some scr… | [32] [76] | [34] [28] [30] | — |
| `#117` Crucially, as highly vaccinated birth cohorts enter adulthood with sharply diminished risks of HPV 16 and 18 disease, m… | [77] | [51] [61] [55] [58] [9] [29] [19] [49] | — |
| `#118` Simultaneously, next-generation prophylactic and therapeutic vaccine pipelines aim to close residual gaps. | [78] [79] | [77] [38] [81] [80] [3] [76] [35] | — |
| `#119` Experimental 11-valent, 14-valent, and 15-valent prophylactic formulations are advancing through clinical trials to bro… | [78] | [76] [46] [81] [49] [32] [38] [36] [3] [35] [58] [30] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 4172361 |
| **Média de tokens por requisição** | 36281.4 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/83 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 24.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | downloaded | 21 | 7 | 12 | 2 | 0 |
| [[38]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11892266/) | downloaded | 12 | 4 | 8 | 0 | 0 |
| [[2]](https://www.who.int/news-room/fact-sheets/detail/human-papilloma-virus-and-cancer) | downloaded | 11 | 3 | 7 | 1 | 0 |
| [[25]](https://www.mdpi.com/1718-7729/32/3/122) | blocked | 10 | 0 | 0 | 0 | 10 |
| [[12]](https://dceg.cancer.gov/research/cancer-types/cervix/escuddo) | downloaded | 8 | 2 | 6 | 0 | 0 |
| [[19]](https://vaxintegrity.cidrap.umn.edu/new-evidence-review-affirms-strong-safety-and-effectiveness-hpv-vaccines) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[41]](https://rhsupplies.org/news-stories/pressroom/gardasil-prequalified-by-who-246/) | downloaded | 7 | 0 | 0 | 7 | 0 |
| [[6]](https://sto-online.org/wp-content/uploads/2025/12/Noninferiority-of-One-HPV-Vaccine-Dose-to-Two-Doses.-NEJMoa2506765.pdf) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[37]](https://www.researchgate.net/publication/392065828_Human_papillomavirus_infection_and_screening_strategies) | error | 6 | 0 | 0 | 0 | 6 |
| [[10]](https://www.vaccinestoday.eu/stories/hpv-vaccine-cervical-cancer-deaths-plummet-among-young-women-in-england/) | downloaded | 5 | 0 | 4 | 1 | 0 |
| [[30]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12039116/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[31]](https://www.mdpi.com/1422-0067/26/11/5205) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[51]](https://www.fda.gov/media/139433/download) | downloaded | 5 | 1 | 2 | 2 | 0 |
| [[60]](https://media.path.org/documents/HPV_Cnsrt_GeneralSummary_2025_R1_web.pdf?_gl=1h49zkc_gcl_auODE4NDY2NzI2LjE3NDYwMjI1MTI._gaMTM0MTAzNTg4MC4xNzA2NjM4NTAw_ga_YBSE7ZKDQM*czE3NDg0NDQ0NjkkbzE1JGcxJHQxNzQ4NDQ0NzQ4JGo2MCRsMCRoMA) | downloaded | 5 | 0 | 2 | 3 | 0 |
| [[71]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568012/) | downloaded | 5 | 1 | 2 | 2 | 0 |
| [[3]](https://www.ijpsjournal.com/article/targeting-hpv-oncogenes-e6-e7-for-cervical-cancer-therapy-advances-in-molecular-and-natural-strategies) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/41276264/) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[14]](https://extranet.who.int/prequal/vaccines/p/cervavac) | downloaded | 4 | 0 | 2 | 2 | 0 |
| [[15]](https://www.who.int/news/item/04-10-2024-who-adds-an-hpv-vaccine-for-single-dose-use) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[17]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[26]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12290362/) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[28]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13335833/) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[55]](https://www.riscc-h2020.eu/documents/143/HPV_SCREENING_Mod6_Vaccinated_population.pdf) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[61]](https://www.cdc.gov/acip/downloads/slides-2025-04-15-16/03-Barnabas-HPV-508.pdf) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[5]](https://www.mdpi.com/2076-393x/10/2/256) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[8]](https://ourworldindata.org/hpv-vaccination-world-can-eliminate-cervical-cancer) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[11]](https://www.who.int/teams/immunization-vaccines-and-biologicals/diseases/human-papillomavirus-vaccines-(HPV)) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[16]](https://pharmacally.com/serum-institute-cervavac-who-prequalification/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[49]](https://www.cambridge.org/core/journals/epidemiology-and-infection/article/prophylactic-hpv-vaccination-past-present-and-future/661BBE441D98B2DE8685A10B1E124542) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[50]](https://extranet.who.int/prequal/sites/default/files/vwa_vaccine/pq_326_HPV9_1dose_Merck_PI-102022.pdf) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[59]](https://view-hub.org/topics/single-dose-hpv) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[64]](https://clinicaltrials.gov/study/NCT05237947) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[70]](https://www.researchgate.net/publication/392528381_Global_HPV_vaccination_programs_and_coverage_rates_a_systematic_review) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[79]](https://www.mdpi.com/2076-393x/14/6/507) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[7]](https://researchportal.ukhsa.gov.uk/en/publications/the-effects-of-the-national-hpv-vaccination-programme-in-england-/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[13]](https://www.esmo.org/oncology-news/one-dose-of-either-a-bivalent-or-nonavalent-hpv-vaccine-provides-protection-against-hpv16-or-hpv18-infection-and-is-not-inferior-to-two-doses) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[18]](https://www.iasusa.org/wp-content/uploads/2026/08/34-4-dunlevy-johnson.pdf) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[27]](https://www.gavi.org/our-work/vaccine-portfolio/human-papillomavirus) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[32]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12731993/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[33]](https://www.cdc.gov/std/treatment-guidelines/hpv-cancer.htm) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[44]](https://extranet.who.int/prequal/vaccines/prequalified-vaccines) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[47]](https://www.xiameninnovax.com/news/who-prequalification/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[62]](https://pubmed.ncbi.nlm.nih.gov/38365419/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[72]](https://view-hub.org/sites/default/files/2025-11/VIEW-hub%20Report_November%202025.pdf) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[74]](https://www.who.int/publications/i/item/9789240030824) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[75]](https://www.hpvworld.com/articles/impact-of-hpv-vaccination-on-cervical-cancer-screening-requirements/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[78]](https://www.ajmc.com/view/first-ever-therapeutic-hpv-vaccine-promising-against-cervical-cancer) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[80]](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1897025/full) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[4]](https://www.cancer.gov/about-nci/advisory-boards/ncab/meetings/2026/castle-september-presentation.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[20]](https://www.gavi.org/vaccineswork/new-study-validates-previous-conclusions-supporting-single-dose-hpv-vaccination) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[21]](https://mediatum.ub.tum.de/doc/1782277/1782277.pdf) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[22]](https://www.who.int/health-topics/cervical-cancer) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[23]](https://ourworldindata.org/grapher/rate-of-new-cervical-cancer-cases-gco) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[24]](https://gco.iarc.who.int/today/en/fact-sheets-cancers/23/cervix-uteri) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[29]](https://pubmed.ncbi.nlm.nih.gov/21395359/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[34]](https://www.scielo.br/j/rbgo/a/GF8SgJqfwPrSMVtdHrjNXxk/?lang=en) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[35]](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.03116/full) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[36]](https://pmc.ncbi.nlm.nih.gov/articles/PMC3950231/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[39]](https://www.who.int/publications/i/item/9789240089167) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[40]](https://ec.europa.eu/health/documents/community-register/2016/20160729135469/anx_135469_en.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[42]](https://www.researchgate.net/publication/50373593_AS04-Adjuvanted_Human_Papillomavirus_HPV_Types_16_and_18_Vaccine_Cervarix_R_A_Review_of_its_Use_in_the_Prevention_of_Premalignant_Cervical_Lesions_and_Cervical_Cancer_Causally_Related_to_Certain_Oncog) | error | 1 | 0 | 0 | 0 | 1 |
| [[43]](https://www.merck.com/product/usa/pi_circulars/g/gardasil_9/gardasil_9_pi.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[45]](https://www.path.org/our-impact/media-center/new-hpv-vaccine-innovax-receives-who-prequalification/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[46]](https://www.hpvworld.com/articulos/new-hpv-vaccines-current-landscape-and-future-directions/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[48]](https://www.researchgate.net/publication/279795502_Quadrivalent_vaccine_against_human_papillomavirus_to_prevent_high-grade_cervical_lesions_The_FUTURE_II_Study_Group_N_Engl_J_Med_2007_356_1915_1927_101056NEJMoa061741_17494925) | error | 1 | 0 | 0 | 0 | 1 |
| [[52]](https://www.researchgate.net/publication/272074165_Efficacy_of_Human_Papillomavirus_16_and_18_HPV-1618_AS04-Adjuvanted_Vaccine_against_Cervical_Infection_and_Precancer_in_Young_Women_Final_Event-Driven_Analysis_of_the_Randomized_Double-Blind_PATRICIA_) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[53]](https://academic.oup.com/jid/article/199/7/926/853088) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[54]](https://www.semanticscholar.org/paper/The-effects-of-the-national-HPV-vaccination-in-UK%2C-Falcaro-Casta%C3%B1%C3%B3n/00820c7e6c82bbedf3d7fabd15ac754f70f974c9) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[56]](https://publichealthscotland.scot/news/2025/november/new-study-shows-long-term-effectiveness-of-hpv-vaccine/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[57]](https://www.mdpi.com/2076-393x/8/3/391) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[58]](https://es.cochrane.org/sites/es.cochrane.org/files/uploads/Embargos/2025/embargoed_24nov2025_effects-of-human-papillomavirus--hpv--vaccinationprogrammes-on-community-rates-of-hpv-related-diseaseand-harms-from-vaccination.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[63]](https://www.drozdogan.com/en/is-one-dose-of-hpv-vaccine-enough-what-does-the-escuddo-study-published-in-nejm-tell-us/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[65]](https://www.who.int/news/item/20-12-2022-WHO-updates-recommendations-on-HPV-vaccination-schedule) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[66]](https://www.cima.care/insights/hpv-vaccination-transforms-global-cancer-prevention/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[67]](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0004688) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[68]](https://www.mednet.ca/en/report/future-i-and-future-ii-vaccination-against-human.html) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[69]](https://www.who.int/publications/i/item/9789240014107) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[73]](https://www.gavi.org/news/media-room/global-leaders-unite-accelerate-cervical-cancer-elimination-efforts) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[76]](https://www.medconsultasia.com/vaccine/new-hpv-vaccines-in-clinical-trials/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[77]](https://cdn.who.int/media/docs/default-source/immunization/pdvac/pdvac-2024/day-1/therapeutic-hpv-vaccines.pdf?sfvrsn=f9490092_1) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[81]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13103388/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[82]](https://ecancer.org/en/news/25925-a-therapeutic-hpv-vaccine-could-eliminate-precancerous-cervical-lesions) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[83]](https://www.ddw-online.com/therapeutic-hpv-vaccine-could-eliminate-precancerous-cervical-lesions-33407-202501/) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | #11, #14–15, #17, #27, #104, #114 | #0, #6–7, #9–10, #23, #29, #37, #69, #95, #103, #105 | #1, #3 | `#11` The highest rates of cervical cancer incidence and mortality are in low- and middle-income countries. This reflects major inequities driven by lack of access t… |
| [[38]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11892266/) | #42, #46, #50, #54 | #38, #43, #47–48, #52–53, #55, #77 | — | `#42` All marketed L1-based vaccines (listed in Table 1) are produced using recombinant DNA technology in various hosts, allowing the L1 proteins to self-assemble in… |
| [[2]](https://www.who.int/news-room/fact-sheets/detail/human-papilloma-virus-and-cancer) | #20–21, #43 | #0, #8, #10, #16, #19, #45, #113 | #44 | `#20` Almost all sexually active people will be infected at some point in their lives, usually without symptoms. |
| [[12]](https://dceg.cancer.gov/research/cancer-types/cervix/escuddo) | #80, #84 | #4, #44, #76, #78, #91, #94 | — | `#80` These observations raised the possibility that a single dose of HPV vaccine may offer sufficient durable protection and set the basis for ESCUDDO (efficacy tri… |
| [[19]](https://vaxintegrity.cidrap.umn.edu/new-evidence-review-affirms-strong-safety-and-effectiveness-hpv-vaccines) | #90, #97, #101 | #6, #75, #79 | #100 | `#90` Data on long-term protection from a single dose, effectiveness in males, and protection against non-cervical cancers remain limited and warrant further study. |
| [[41]](https://rhsupplies.org/news-stories/pressroom/gardasil-prequalified-by-who-246/) | — | — | #42, #48–49, #51, #63–65 | — |
| [[6]](https://sto-online.org/wp-content/uploads/2025/12/Noninferiority-of-One-HPV-Vaccine-Dose-to-Two-Doses.-NEJMoa2506765.pdf) | #84, #87–88 | #1, #4, #99 | — | `#84` The double-blind, randomized, controlled ESCUDDO trial evaluated the noninferiority of one dose of a bivalent or nonavalent HPV vaccine to the respective two-d… |
| [[10]](https://www.vaccinestoday.eu/stories/hpv-vaccine-cervical-cancer-deaths-plummet-among-young-women-in-england/) | — | #2, #70, #72, #74 | #112 | `#2` health authorities have reported **no deaths** from the disease among women aged 20 to 24 – the first time this has been achieved over a five year period. |
| [[30]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12039116/) | #20–21, #24–25 | #31 | — | `#20` Eighty percent of women who engage in sexual activity will, at some point in their lives, contract HPV |
| [[51]](https://www.fda.gov/media/139433/download) | #67 | #61, #68 | #62, #102 ⚡ | `#67` HPV 31-, 33-, 45-, 52-, 58-related CIN 2/3, AIS, Cervical Cancer, VIN 2/3, VaIN 2/3, Vulvar Cancer, and Vaginal Cancer ... 97.4 (85.0, 99.9) |
| [[60]](https://media.path.org/documents/HPV_Cnsrt_GeneralSummary_2025_R1_web.pdf?_gl=1h49zkc_gcl_auODE4NDY2NzI2LjE3NDYwMjI1MTI._gaMTM0MTAzNTg4MC4xNzA2NjM4NTAw_ga_YBSE7ZKDQM*czE3NDg0NDQ0NjkkbzE1JGcxJHQxNzQ4NDQ0NzQ4JGo2MCRsMCRoMA) | — | #76, #92 | #77, #93, #110 | `#76` As of February 2025, nearly 70 countries have adopted a single-dose HPV vaccination schedule. |
| [[71]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568012/) | #106 | #109, #112 | #110, #107 ⚡ | `#106` Global HPV vaccination coverage (56.9%) in 2024 remains far below the WHO target of 90% coverage for girls aged 9 to 14 years. |
| [[3]](https://www.ijpsjournal.com/article/targeting-hpv-oncogenes-e6-e7-for-cervical-cancer-therapy-advances-in-molecular-and-natural-strategies) | — | #0, #33, #38 | #30 (s/ aval.) | `#0` High-risk Human Papillomavirus (HPV), specifically types HPV-16 and HPV-18, is the necessary cause of nearly all cervical cancers. \| Preventive vaccines are pr… |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/41276264/) | #101 | #2, #75, #100 | — | `#101` Cochrane Database Syst Rev. 2025 Nov 24;11(11):CD015363. [...] HPV vaccination was not associated with an increased risk of postural orthostatic tachycardia sy… |
| [[14]](https://extranet.who.int/prequal/vaccines/p/cervavac) | — | #5, #56 | #48, #55 | `#5` Vaccine type Human Papillomavirus (Quadrivalent) |
| [[15]](https://www.who.int/news/item/04-10-2024-who-adds-an-hpv-vaccine-for-single-dose-use) | #54 | #5, #53, #111 | — | `#54` making it the fifth product available on the global market … Walrinvax® is prequalified with a two-dose schedule. Further data will be needed to assess if this… |
| [[17]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | — | #6, #45, #94–95 | — | `#6` Three doses are recommended for immunocompromised persons (including those with HIV infection) aged 9 through 26 years. |
| [[26]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12290362/) | #11, #13, #18 | #12 | — | `#11` This disease mainly affects women in low- and lower-middle-income countries (LMICs), where 90% of cases occur. [...] Inequalities in access to immunization, sc… |
| [[28]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13335833/) | #114–115 | #16, #46 | — | `#114` Primary HPV DNA testing preferred; if HPV testing is not available, cytology or VIA may be used as alternatives ... 30 years (general population) ... Every 5–1… |
| [[55]](https://www.riscc-h2020.eu/documents/143/HPV_SCREENING_Mod6_Vaccinated_population.pdf) | — | #69–71, #73 | — | `#69` All studies estimated vaccine effectiveness through registry linkage except England, that evaluated the impact of the vaccine comparing vaccinated versus unvac… |
| [[61]](https://www.cdc.gov/acip/downloads/slides-2025-04-15-16/03-Barnabas-HPV-508.pdf) | #80 | #79 | #78, #83 | `#80` We conducted a rigorous randomized trial (the KEN SHE Study) and found that the single dose HPV vaccination is highly efficacious, with 98% vaccine efficacy fo… |
| [[5]](https://www.mdpi.com/2076-393x/10/2/256) | — | #1, #66, #68 | — | `#1` Cervarix® and Gardasil® could prevent 70% of cervical cancer cases, and Gardasil-9® almost 90% [24]. |
| [[8]](https://ourworldindata.org/hpv-vaccination-world-can-eliminate-cervical-cancer) | — | #2, #71, #73 | — | `#2` HPV vaccines are highly effective, which has been demonstrated in large-scale randomized controlled trials. Research shows that, if given early, vaccination re… |
| [[11]](https://www.who.int/teams/immunization-vaccines-and-biologicals/diseases/human-papillomavirus-vaccines-(HPV)) | — | #3, #91–92 | — | `#3` In October 2026, SAGE reviewed further evidence on dose optimization and has strengthened its recommendation for single dose schedule use and extended use to a… |
| [[16]](https://pharmacally.com/serum-institute-cervavac-who-prequalification/) | — | #5, #55–56 | — | `#5` WHO’s official listing records the prequalification as effective September 25, 2026. |
| [[49]](https://www.cambridge.org/core/journals/epidemiology-and-infection/article/prophylactic-hpv-vaccination-past-present-and-future/661BBE441D98B2DE8685A10B1E124542) | #58 | #59–60 | — | `#58` in the according-to-protocol (AP) analysis [...] demonstrated near perfect efficacy (>90%) in [...] women naive to those same HPV genotypes. [...] In the whole… |
| [[50]](https://extranet.who.int/prequal/sites/default/files/vwa_vaccine/pq_326_HPV9_1dose_Merck_PI-102022.pdf) | #67 | #58, #98 | — | `#67` the pivotal clinical study (Protocol 001) evaluated the efficacy of Gardasil 9 using qHPV vaccine as a comparator. ... The efficacy of Gardasil 9 in 16- throug… |
| [[59]](https://view-hub.org/topics/single-dose-hpv) | — | — | #75, #100–101 | — |
| [[64]](https://clinicaltrials.gov/study/NCT05237947) | — | — | #86, #99, #85 ⚡ | `#85` This study examines whether a single dose of HPV vaccine can reduce the frequency with which women between ages 18-30 become infected with HPV. ... Participant… |
| [[70]](https://www.researchgate.net/publication/392528381_Global_HPV_vaccination_programs_and_coverage_rates_a_systematic_review) | — | #103–104 | #105 | `#103` In 2020, the World Health Organization (WHO) proposed the ‘Global Strategy to Accelerate the Elimination of Cervical Cancer,’ committed by 194 countries |
| [[7]](https://researchportal.ukhsa.gov.uk/en/publications/the-effects-of-the-national-hpv-vaccination-programme-in-england-/) | — | #2, #71 | — | `#2` The estimated relative reduction in cervical cancer rates by age at vaccine offer were 34% (95% CI 25-41) for age 16-18 years (school year 12-13), 62% (52-71)… |
| [[13]](https://www.esmo.org/oncology-news/one-dose-of-either-a-bivalent-or-nonavalent-hpv-vaccine-provides-protection-against-hpv16-or-hpv18-infection-and-is-not-inferior-to-two-doses) | — | #4, #44 | — | `#4` After 5 years of follow-up of a double-blind, randomised, controlled ESCUDDO study, a single dose of either a bivalent or nonavalent human papillomavirus (HPV)… |
| [[18]](https://www.iasusa.org/wp-content/uploads/2026/08/34-4-dunlevy-johnson.pdf) | — | #6, #95 | — | `#6` HPV vaccination prior to exposure to the virus can prevent more than 90% of HPV-related cancers. |
| [[27]](https://www.gavi.org/our-work/vaccine-portfolio/human-papillomavirus) | — | #12, #111 | — | `#12` Cervical cancer is the fourth most common cancer in women globally, causing more than 209,000 deaths in 2022 in lower-income countries. |
| [[32]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12731993/) | — | #23, #116 | — | `#23` HPV DNA is detected in nearly all cervical cancer samples (99,7%), compared to the significantly lower detection rates in controls |
| [[33]](https://www.cdc.gov/std/treatment-guidelines/hpv-cancer.htm) | — | #29, #37 | — | `#29` Smoking contributes to the progression of CIN, with both active and passive smoking associated with squamous cell carcinoma of the cervix in women with HPV 16… |
| [[44]](https://extranet.who.int/prequal/vaccines/prequalified-vaccines) | — | — | #50, #98 | — |
| [[47]](https://www.xiameninnovax.com/news/who-prequalification/) | — | #57 | #54 | `#57` the prequalification (PQ) application for Cecolin 9, the HPV 9-valent vaccine, was formally submitted to the World Health Organization (WHO) |
| [[62]](https://pubmed.ncbi.nlm.nih.gov/38365419/) | — | #81 | #82 | `#81` the Kenya single-dose HPV-vaccine efficacy (KEN SHE) trial, showed greater than 97% efficacy against persistent HPV16 and HPV18 infection at 36 months among wo… |
| [[72]](https://view-hub.org/sites/default/files/2025-11/VIEW-hub%20Report_November%202025.pdf) | — | #106 | #109 | `#106` Pakistan launched an HPV vaccine campaign targeting girls aged 9–14 years in September 2025. This is the first phase of the campaign, and the goal is to vaccin… |
| [[74]](https://www.who.int/publications/i/item/9789240030824) | — | — | #108, #112 | — |
| [[75]](https://www.hpvworld.com/articles/impact-of-hpv-vaccination-on-cervical-cancer-screening-requirements/) | — | — | #113–114 | — |
| [[78]](https://www.ajmc.com/view/first-ever-therapeutic-hpv-vaccine-promising-against-cervical-cancer) | — | — | #118–119 | — |
| [[80]](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1897025/full) | — | #120–121 | — | `#120` However, they do not eradicate established infections or preexisting lesions. |
| [[4]](https://www.cancer.gov/about-nci/advisory-boards/ncab/meetings/2026/castle-september-presentation.pdf) | — | #1 | — | `#1` 60 mg HPV16; 40 mg HPV18; 30 mg HPV6; 40 mg HPV11;20 mg HPV31; 20 mg HPV33; 20 mg HPV45; 20 mg HPV52; 20 mg HPV58 ... 90% Cervical Cancer; 90% Warts |
| [[20]](https://www.gavi.org/vaccineswork/new-study-validates-previous-conclusions-supporting-single-dose-hpv-vaccination) | — | — | #6 | — |
| [[22]](https://www.who.int/health-topics/cervical-cancer) | — | #8 | — | `#8` Cervical cancer is the fourth most common cancer in women. In 2022, an estimated 660 000 women were diagnosed with cervical cancer worldwide and about 350 000… |
| [[23]](https://ourworldindata.org/grapher/rate-of-new-cervical-cancer-cases-gco) | — | — | #8 | — |
| [[24]](https://gco.iarc.who.int/today/en/fact-sheets-cancers/23/cervix-uteri) | — | — | #9 | — |
| [[29]](https://pubmed.ncbi.nlm.nih.gov/21395359/) | — | — | #19 | — |
| [[34]](https://www.scielo.br/j/rbgo/a/GF8SgJqfwPrSMVtdHrjNXxk/?lang=en) | — | #31 | — | `#31` For this to occur there should be an overexpression of the E6 and E7 genes from the genome of an integrated HPV. |
| [[35]](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2019.03116/full) | — | #34 | — | `#34` It is responsible for the zinc-dependent dimerization and for mediating E7 interaction with cellular proteins responsible for cell cycle regulation and apoptos… |
| [[36]](https://pmc.ncbi.nlm.nih.gov/articles/PMC3950231/) | — | #34 | — | `#34` the inactivation of Rb is caused by the HPV E7 protein, which may then lead to increased expression of p16 through a negative feedback mechanism |
| [[39]](https://www.who.int/publications/i/item/9789240089167) | — | — | #39 | — |
| [[40]](https://ec.europa.eu/health/documents/community-register/2016/20160729135469/anx_135469_en.pdf) | — | — | #40 | — |
| [[43]](https://www.merck.com/product/usa/pi_circulars/g/gardasil_9/gardasil_9_pi.pdf) | — | — | #49 | — |
| [[45]](https://www.path.org/our-impact/media-center/new-hpv-vaccine-innovax-receives-who-prequalification/) | — | #52 | — | `#52` Countries facing barriers to national introduction or expanding their HPV vaccine program to the full cohort due to price or supply constraints will now have a… |
| [[46]](https://www.hpvworld.com/articulos/new-hpv-vaccines-current-landscape-and-future-directions/) | — | #53 | — | `#53` three bivalent vaccines (Cervarix® by GlaxoSmithKline, Cecolin® by Xiamen Innovax and Walrinvax® by Yuxi Zerun Biotechnology) targeting HPV 16 and 18 |
| [[52]](https://www.researchgate.net/publication/272074165_Efficacy_of_Human_Papillomavirus_16_and_18_HPV-1618_AS04-Adjuvanted_Vaccine_against_Cervical_Infection_and_Precancer_in_Young_Women_Final_Event-Driven_Analysis_of_the_Randomized_Double-Blind_PATRICIA_) | — | — | #61 | — |
| [[56]](https://publichealthscotland.scot/news/2025/november/new-study-shows-long-term-effectiveness-of-hpv-vaccine/) | — | — | #70 | — |
| [[58]](https://es.cochrane.org/sites/es.cochrane.org/files/uploads/Embargos/2025/embargoed_24nov2025_effects-of-human-papillomavirus--hpv--vaccinationprogrammes-on-community-rates-of-hpv-related-diseaseand-harms-from-vaccination.pdf) | — | #74 | — | `#74` the pooled impact of HPV vaccination on rates of anogenital warts indicated a reduction of 47% in the medium term (RR 0.53, 95% CI 0.37 to 0.77; 4 studies, 6,4… |
| [[63]](https://www.drozdogan.com/en/is-one-dose-of-hpv-vaccine-enough-what-does-the-escuddo-study-published-in-nejm-tell-us/) | — | — | #83 | — |
| [[65]](https://www.who.int/news/item/20-12-2022-WHO-updates-recommendations-on-HPV-vaccination-schedule) | — | — | #89 | — |
| [[66]](https://www.cima.care/insights/hpv-vaccination-transforms-global-cancer-prevention/) | — | #92 | — | `#92` In December 2022, the World Health Organization published a landmark position paper updating HPV vaccine dosing recommendations to include a single-dose schedu… |
| [[67]](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0004688) | — | — | #93 | — |
| [[68]](https://www.mednet.ca/en/report/future-i-and-future-ii-vaccination-against-human.html) | — | — | #96 | — |
| [[69]](https://www.who.int/publications/i/item/9789240014107) | — | — | #98 | — |
| [[73]](https://www.gavi.org/news/media-room/global-leaders-unite-accelerate-cervical-cancer-elimination-efforts) | — | — | #108 | — |
| [[76]](https://www.medconsultasia.com/vaccine/new-hpv-vaccines-in-clinical-trials/) | — | — | #116 | — |
| [[77]](https://cdn.who.int/media/docs/default-source/immunization/pdvac/pdvac-2024/day-1/therapeutic-hpv-vaccines.pdf?sfvrsn=f9490092_1) | — | — | #117 | — |
| [[81]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13103388/) | — | #121 | — | `#121` VGX-3100 ... has been tested in cervical, vulvar, anal, and peri-anal intraepithelial neoplasia grade 2/3 (CIN2/3, VIN2/3, AIN2/3, and PAIN2/3, respectively) |
| [[82]](https://ecancer.org/en/news/25925-a-therapeutic-hpv-vaccine-could-eliminate-precancerous-cervical-lesions) | — | #121 | — | `#121` The Vvax001 vaccine is a modified version of the Semliki Forest virus that cannot replicate and produces the oncogenic E6 and E7 proteins that are expressed ex… |
| [[83]](https://www.ddw-online.com/therapeutic-hpv-vaccine-could-eliminate-precancerous-cervical-lesions-33407-202501/) | — | #121 | — | `#121` The Vvax001 vaccine is a modified version of the Semliki Forest virus that cannot replicate |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://mediatum.ub.tum.de/doc/1782277/1782277.pdf — anti_bot — barreira de acesso (anti_bot): # **Making sure you're not a bot!** ## [image] [image] Loading... You are seeing this because the administrator of this 
- https://www.mdpi.com/1718-7729/32/3/122 — http_error — barreira de acesso (http_error): Reference #18.42fbd217.1794963402.62d0116f https://errors.edgesuite.net/18.42fbd217.1794963402.62d0116f
- https://www.mdpi.com/1422-0067/26/11/5205 — http_error — barreira de acesso (http_error): Reference #18.50fbd217.1794963402.55f060d5 https://errors.edgesuite.net/18.50fbd217.1794963402.55f060d5
- https://academic.oup.com/jid/article/199/7/926/853088 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.semanticscholar.org/paper/The-effects-of-the-national-HPV-vaccination-in-UK%2C-Falcaro-Casta%C3%B1%C3%B3n/00820c7e6c82bbedf3d7fabd15ac754f70f974c9 — anti_bot — barreira de acesso (anti_bot): Complete the security check before continuing. This step verifies that you are not a bot, which helps to protect your ac
- https://www.mdpi.com/2076-393x/8/3/391 — http_error — barreira de acesso (http_error): Reference #18.50fbd217.1794963503.55f88627 https://errors.edgesuite.net/18.50fbd217.1794963503.55f88627
- https://www.mdpi.com/2076-393x/14/6/507 — http_error — barreira de acesso (http_error): Reference #18.42fbd217.1794963505.62d94a98 https://errors.edgesuite.net/18.42fbd217.1794963505.62d94a98

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-0`** [1] [2] [3]
  - Trecho: Prophylactic vaccination against human papillomavirus (HPV) targets the primary viral cause of nearly all cervical cancers, establishing a uniquely direct preventive intervention in modern oncology.
  - Justificativa: A evidência sustenta explicitamente que o HPV é a causa primária de quase todos os cânceres cervicais e que a vacinação profilática contra HPV previne esses cânceres. O caráter 'direto' da intervenção é inferível da evi…
  - Suporte veio de: [3] [1] [2]
  - Evidência: “High-risk Human Papillomavirus (HPV), specifically types HPV-16 and HPV-18, is the necessary cause of nearly all cervical cancers.”
  - Não coberto pela evidência: O termo 'uniquely direct preventive intervention in modern oncology' não é explicitamente comparado a outras intervenções preventivas em oncologia; a singularidade é inferida mas não diretamente afirmada no contexto de vacinação profilática.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | High-risk Human Papillomavirus (HPV), specifically types HPV-16 and HPV-18, is the necessary cause of nearly all cervic… |
    | [1] | parcial | Almost all cases of cervical cancer are caused by infection with oncogenic types of human papillomavirus (HPV). \| Cervi… |
    | [2] | parcial | Prophylactic vaccination against HPV can prevent these cancers. \| Persistent HPV infection with high-risk HPV types is… |

- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-8`** [2] [22] [23]
  - Trecho: According to GLOBOCAN 2022 estimates compiled across 185 countries and cited in WHO cancer surveillance, approximately 660,000 women were diagnosed with cervical cancer and 350,000 died from the disease in 2022, ranking…
  - Justificativa: Os números essenciais (660.000 diagnósticos, 350.000 mortes, ano 2022) e a classificação (quarto em incidência e mortalidade entre mulheres) estão explicitamente sustentados pela evidência. Detalhes específicos sobre a…
  - Suporte veio de: [22] [2]
  - Evidência: “Cervical cancer is the fourth most common cancer in women. In 2022, an estimated 660 000 women were diagnosed with cervical cancer worldwide and about 350 000 women died from the disease.”
  - Não coberto pela evidência: GLOBOCAN 2022 estimates compiled across 185 countries; cited in WHO cancer surveillance
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [22] | parcial | Cervical cancer is the fourth most common cancer in women. In 2022, an estimated 660 000 women were diagnosed with cerv… |
    | [23] | ausente | — |
    | [2] | parcial | Cervical cancer was the fourth leading cause of cancer and cancer deaths in women in 2022, with some 660 000 new cases… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência confirma os números (660.000 diagnósticos e 350.000 mortes em 2022) e a classificação (quarto em incidência e mortalidade), mas…") — cascata: baseline → context_expansion
- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-11`** [1] [26]
  - Trecho: The global burden of cervical cancer is heavily concentrated in low- and middle-income countries (LMICs), reflecting stark structural disparities in immunization, screening, and oncology infrastructure.
  - Justificativa: A evidência sustenta explicitamente que o fardo global do câncer cervical está concentrado em LMICs (90% dos casos) e que isso reflete desigualdades estruturais em imunização, rastreamento e infraestrutura de tratamento…
  - Suporte veio de: [26] [1]
  - Evidência: “Cervical cancer is the fourth most common cancer in women worldwide, with 660,000 new cases and 350,000 deaths in 2022, mostly in low- and middle-income countries (LMICs).”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [26] | sustenta | This disease mainly affects women in low- and lower-middle-income countries (LMICs), where 90% of cases occur. [...] In… |
    | [1] | sustenta | The highest rates of cervical cancer incidence and mortality are in low- and middle-income countries. This reflects maj… |

### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-2`** [7] [8] [9] [10]
  - Trecho: Across two decades of randomized clinical trials and nationwide population registries, HPV immunization administered prior to sexual debut has consistently demonstrated greater than 90% efficacy against vaccine-type per…
  - Justificativa: A evidência sustenta parcialmente a afirmação: confirma a redução de ~87% na incidência de câncer cervical na coorte vacinada mais jovem na Inglaterra e a ausência de mortes por câncer cervical em mulheres inglesas de 2…
  - Suporte veio de: [7] [10] [8]
  - Evidência: “The estimated relative reduction in cervical cancer rates by age at vaccine offer were 34% (95% CI 25-41) for age 16-18 years (school year 12-13), 62% (52-71) for age 14-16 years (school year 10-11), and 87% (72-94) for…”
  - Não coberto pela evidência: 'duas décadas de ensaios clínicos randomizados' — duração exata não explicitada na evidência; 'mais de 90% de eficácia contra infecção persistente do tipo vacinal' — a evidência não quantifica eficácia contra infecção persistente especificamente; menciona 99% para 'mudanças graves nas células cervicais' e 97% para CIN3; 'de 2020 a 2024' — datas exatas para o período de zero mortes não são mencionadas na evidência; apenas se diz 'pela primeira vez em um período de cinco anos'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | The estimated relative reduction in cervical cancer rates by age at vaccine offer were 34% (95% CI 25-41) for age 16-18… |
    | [8] | parcial | HPV vaccines are highly effective, which has been demonstrated in large-scale randomized controlled trials. Research sh… |
    | [9] | parcial | Data show that there is greater benefit to vaccinating younger adolescents prior to becoming sexually active. |
    | [10] | parcial | health authorities have reported **no deaths** from the disease among women aged 20 to 24 – the first time this has bee… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-3`** [1] [11]
  - Trecho: By late 2026, two major developments have reshaped the global strategy to eliminate cervical cancer as a public health problem.
  - Justificativa: A evidência não menciona 'dois grandes desenvolvimentos' que tenham 'reformulado' a estratégia global até o final de 2026. Embora a evidência cite uma revisão do SAGE em outubro de 2026 sobre otimização de doses, não há…
  - Suporte veio de: [11]
  - Não coberto pela evidência: By late 2026; two major developments; reshaped the global strategy
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [11] | parcial | In October 2026, SAGE reviewed further evidence on dose optimization and has strengthened its recommendation for single… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-4`** [6] [12] [13]
  - Trecho: First, five-year randomized trial results published in December 2025 demonstrated that one vaccine dose provides non-inferior protection against persistent HPV 16 and 18 infections compared with two doses, leading the W…
  - Justificativa: A evidência sustenta parcialmente a afirmativa: (1) o ensaio ESCUDDO publicado em dezembro de 2025 demonstrou não-inferioridade de uma dose vs. duas doses para infecção persistente por HPV 16/18 em seguimento de 5 anos,…
  - Suporte veio de: [6] [12]
  - Evidência: “The trial results were published in December 2025, showing non-inferiority of one dose, compared to two doses.”
  - Não coberto pela evidência: WHO SAGE em outubro de 2026 fortalecendo a recomendação de dose única; extensão da orientação de dose única até os 30 anos de idade; Referência a SAGE (Strategic Advisory Group of Experts on Immunization) especificamente
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | parcial | This article was published on December 3, 2025, at NEJM.org. |
    | [12] | parcial | The trial results were published in December 2025, showing non-inferiority of one dose, compared to two doses. |
    | [13] | parcial | After 5 years of follow-up of a double-blind, randomised, controlled ESCUDDO study, a single dose of either a bivalent… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-85`** [64]
  - Trecho: As summarized in clinical commentary on the trial, ESCUDDO randomized 20,330 girls aged 12 to 16 years across four equal arms—one or two doses of either the bivalent or nonavalent vaccine—alongside an observational surv…
  - Justificativa: A evidência descreve o ensaio PRISMA-ESCUDDO (NCT05237947) com mulheres de 18 a 30 anos, randomizadas em 3 braços (não 4), com dose única (não uma ou duas doses). A afirmacao cita idades de 12-16 anos, 20.330 participan…
  - Evidência: “This study examines whether a single dose of HPV vaccine can reduce the frequency with which women between ages 18-30 become infected with HPV.”
  - Não coberto pela evidência: 20,330 girls aged 12 to 16 years — contradito pela evidência (idades 18-30); four equal arms — contradito pela evidência (3 braços); one or two doses — contradito pela evidência (apenas dose única)
- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-102`** [51]
  - Trecho: Regulatory registries encompassing more than 1,000 pregnancy exposures to Gardasil 9 similarly confirm no malformative or feto-neonatal toxicity.
  - Justificativa: A evidência contradiz diretamente a afirmação em dois aspectos centrais. Primeiro, o número de exposições na gravidez: a evidência indica que o registro de gravidez tinha apenas 158 mulheres inscritas até 9 de dezembro…
  - Evidência: “As of 9 December 2019, enrollment numbers in studies V503-002-020, V503-021-01 and the pregnancy registry were 1,272, ~4,000 and 158 subjects respectively.”
  - Não coberto pela evidência: Afirmação de 'mais de 1.000 exposições na gravidez' — a evidência mostra apenas 158 inscritas no registro de gravidez; Afirmação de 'nenhuma toxicidade malformativa ou feto-neonatal' — a evidência menciona taxa mais alta de aborto espontâneo e avaliação em andamento, sem confirmação de ausência de toxicidade
- **Trecho citado `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-107`** [71]
  - Trecho: A June 2025 systematic review in EClinicalMedicine documented that 148 of 194 WHO Member States (76%) had incorporated HPV vaccines into national schedules as of February 2025—76 countries (51%) with gender-neutral prog…
  - Justificativa: A evidência contradiz a afirmação em seu dado central: o estudo relata 147/194 (75,8%) países, não 148 (76%). Além disso, a evidência não menciona 'EClinicalMedicine' como revista (parece ser uma publicação MDPI), nem d…
  - Evidência: “The HPV vaccination was introduced into the national schedule of 147 countries in 2024.”
  - Não coberto pela evidência: Publicação em EClinicalMedicine (a evidência indica publicação MDPI, não EClinicalMedicine); Data de junho de 2025 (a evidência não menciona essa data); Data de referência de fevereiro de 2025 (a evidência se refere a 2024)
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência não menciona 'EClinicalMedicine', 'June 2025', 'systematic review', 'February 2025', 'gender-neutral programs', '76 countries (…") — cascata: baseline → context_expansion

---

## 10. Trechos Citados Não Auditados

Motivos: 8 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 1 citam referência não baixada/inacessível.

- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-22` — Referencia(s) citada(s) ['7eeb41f553c06993', 'b773f0f0dbeaae7b'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-26` — Referencia(s) citada(s) ['b773f0f0dbeaae7b'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-28` — Referencia(s) citada(s) ['b773f0f0dbeaae7b'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-32` — Referencia(s) citada(s) ['7eeb41f553c06993'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-35` — Referencia(s) citada(s) ['7eeb41f553c06993'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-36` — Referencia(s) citada(s) ['7eeb41f553c06993', '63af487c8c32d81c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-41` — Referencia(s) citada(s) ['63af487c8c32d81c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-122` — Referencia(s) citada(s) ['b773f0f0dbeaae7b'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_6e36aa5e9e6e_20261115T152206Z-123` — Referencia(s) citada(s) ['582c9bf5107880f8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.