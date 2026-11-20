# Relatório de Auditoria — Gemini (semaglutina_saude_82a2bfa61988_20261117T031256Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Emergente/semaglutina_saude.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_82a2bfa61988_20261117T031256Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T10:36:36.513502+00:00 |
| **Total de trechos citados** | 107 |
| **Tempo de processamento** | 0:22:19:21 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3069.8 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-17 03:13:18+00:00 |
| Citações no corpo | 224 marcadores, 96 distintos |
| Referências listadas | 96 (2 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 47 | 43.9% |
| **UNSUPPORTED** | 31 | 29.0% |
| **CONTRADICTED** | 3 | 2.8% |
| **SKIPPED** | 26 | 24.3% |
| **TOTAL** | 107 | 100.0% |

Sobre os 81 trechos citados auditados: SUPPORTED 58,02%, UNSUPPORTED 38,27%, CONTRADICTED 3,70%.

> **17 dos 47 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 17 estão **contados dentro** dos 47 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`37` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `12` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `9` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#0` Semaglutide, originally developed as a long-acting glucagon-like peptide-1 (GLP-1) receptor agonist for glycemic contro… | [1] [2] [3] [4] [5] [6] [7] | [93] [26] [42] [23] [69] [20] [10] [38] [58] [19] [16] [25] [83] [35] | — |
| `#56` However, only about 11% of SELECT participants had baseline eGFR below 60 mL/min/1.73 m², creatinine-based eGFR estimat… | [51] [55] | [10] [8] [52] [9] [3] | — |
| `#69` Neurology demonstrates the sharpest divergence between preclinical or epidemiological promise and randomized Phase 3 co… | [12] [62] [65] | [63] [7] [88] [60] [26] [1] [51] [61] | — |
| `#71` To test disease modification prospectively, Novo Nordisk conducted EVOKE and EVOKE+, two parallel Phase 3 double-blind… | [12] [62] [63] | [60] [61] [26] [13] [88] [10] [71] [38] [46] [1] | — |
| `#84` In dermatology, an open-label randomized trial of weekly semaglutide 1.0 mg in 31 patients with psoriasis and type 2 di… | [75] [76] | [74] [73] [93] [10] [48] [7] [16] [69] [58] [42] [1] [26] | — |
| `#87` Genetically proxied GLP-1R agonism in Mendelian randomization similarly links to lower risk of early-onset COPD, acute… | [80] [81] | [79] [78] [69] [1] [77] [95] [10] [12] [24] [72] [20] | — |
| `#94` In SUSTAIN-6, diabetic retinopathy complications occurred more frequently with semaglutide than placebo (3.0% vs. 1.8%,… | [85] | [83] [36] [5] [35] [4] [38] [93] [1] [3] | — |
| `#102` Delayed gastric emptying also triggered June 2023 American Society of Anesthesiologists guidance advising a one-week pr… | [92] [93] | [91] [90] [96] [21] | — |
| `#104` Within the broader incretin class, older agents such as liraglutide and dulaglutide previously demonstrated MACE superi… | [35] [96] | [94] [31] [83] [24] [12] [25] [8] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2561555 |
| **Média de tokens por requisição** | 31624.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 2/96 (2.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 21.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/11/09/15/04/select) | downloaded | 11 | 2 | 8 | 0 | 1 |
| [[3]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | downloaded | 8 | 2 | 4 | 1 | 1 |
| [[7]](https://www.abom.org/wp-content/uploads/2025/06/Phase-3-Trial-of-Semaglutide-in-Metabolic-Dysfunctio.pdf) | downloaded | 8 | 3 | 3 | 0 | 2 |
| [[12]](https://www.neurologylive.com/view/from-glucose-to-cognition-where-repurposed-diabetes-drugs-stand-ad) | downloaded | 8 | 3 | 4 | 0 | 1 |
| [[51]](http://www.nephjc.com/news/flow) | downloaded | 7 | 2 | 5 | 0 | 0 |
| [[6]](https://gpcardio.org/en/2025-05-03_semaglutide-and-walking-capacity-in-people-with-symptomatic-peripheral-artery-disease-and-type-2-diabetes-stride/) | downloaded | 6 | 1 | 2 | 1 | 2 |
| [[2]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[4]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/08/23/19/18/step-hfpef) | downloaded | 5 | 1 | 3 | 0 | 1 |
| [[13]](https://tnsam.org/wp-content/uploads/2025/05/jamapsychiatry_hendershot_2025_oi_240094_1743461595.52316.pdf) | downloaded | 5 | 1 | 0 | 0 | 4 |
| [[14]](https://psychiatryonline.org/ajp/doi/10.1176/appi.ajp.20260003) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[5]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/04/05/03/29/step-hfpef-dm) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[8]](https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehag524/8774585) | downloaded | 4 | 1 | 1 | 1 | 1 |
| [[15]](https://www.researchgate.net/publication/410945506_Semaglutide_in_obesity-related_knee_osteoarthritis_Interpreting_STEP_9_and_implications_for_practice) | inaccessible | 4 | 0 | 0 | 0 | 4 |
| [[18]](https://www.fda.gov/drugs/drug-safety-communications/fda-requires-safety-labeling-changes-glucagon-peptide-1-receptor-agonists-glp-1-ras-due-potential) | downloaded | 4 | 0 | 1 | 1 | 2 |
| [[27]](https://novofrontier.ai/uploads/Users_old/Digital%20Scientific%20Partner/Non%20User%20Customer%20Journey/Articles%20Repositories/review%20of%20oral%20glp-1.pdf) | downloaded | 4 | 2 | 1 | 0 | 1 |
| [[33]](https://www.mdpi.com/2813-0618/4/3/14) | downloaded | 4 | 0 | 1 | 3 | 0 |
| [[57]](https://pubmed.ncbi.nlm.nih.gov/36934740/) | downloaded | 4 | 0 | 1 | 3 | 0 |
| [[58]](https://www.gastroenterologyandhepatology.net/archives/february-2025/recent-data-from-the-essence-trial-on-semaglutide-in-metabolic-dysfunction-associated-steatohepatitis/) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/41138739/) | downloaded | 3 | 1 | 1 | 0 | 1 |
| [[16]](https://eprints.whiterose.ac.uk/id/eprint/212814/1/Once-weekly%20semaglutide%20versus%20placebo%20in%20adults%20with%20increased%20fracture%20risk%20a%20randomised%2C%20double-blinded%2C%20two-centre%2C%20phas.pdf) | downloaded | 3 | 1 | 0 | 0 | 2 |
| [[17]](https://www.natap.org/2023/HIV/100923_01.htm) | downloaded | 3 | 1 | 1 | 0 | 1 |
| [[24]](https://journals.bioscientifica.com/joe/article/263/1/e240046/5657/GLP-1-receptor-agonist-based-therapies-and) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[26]](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019/213051Orig1s000PharmR.pdf) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[35]](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2021.645566/full) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[47]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/14/43/stride) | downloaded | 3 | 1 | 1 | 0 | 1 |
| [[55]](https://www.theisn.org/in-action/research/clinical-trials-isn-act-archive/semaglutide-in-patients-with-overweight-or-obesity-and-chronic-kidney-disease-without-diabetes-a-randomized-double-blind-placebo-controlled-clinical-trial/) | downloaded | 3 | 0 | 0 | 2 | 1 |
| [[62]](https://www.clinicaltrialsarena.com/analyst-comment/ad-pd-2026-novo-nordisk-semaglutide-early-alzheimers/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[68]](https://pubmed.ncbi.nlm.nih.gov/38486046/) | downloaded | 3 | 0 | 1 | 0 | 2 |
| [[82]](https://www.springermedizin.de/cardiovascular-metabolic-and-safety-outcomes-with-semaglutide-by/50193014) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[88]](https://www.neurologylive.com/view/fda-requires-naion-warning-across-glp-1-receptor-agonist-class) | downloaded | 3 | 0 | 1 | 0 | 2 |
| [[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13574348/) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[11]](https://www.researchgate.net/publication/380552694_Semaglutide_and_NTproBNP_in_Obesity-Related_HFpEF_Insights_from_STEP-HFpEF_Program) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[19]](https://www.ema.europa.eu/en/news/prac-concludes-eye-condition-naion-very-rare-side-effect-semaglutide-medicines-ozempic-rybelsus-wegovy) | downloaded | 2 | 0 | 0 | 0 | 2 |
| [[20]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11222026/) | downloaded | 2 | 0 | 0 | 0 | 2 |
| [[21]](https://www.nrfhh.com/index.php/journal/article/download/2283/1314/4930) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[22]](https://www.researchgate.net/publication/325848624_Pharmacokinetics_and_Clinical_Implications_of_Semaglutide_A_New_Glucagon-Like_Peptide_GLP-1_Receptor_Agonist) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[25]](https://www.scielo.br/j/jbn/a/qhJZhkW8dzY5qzRQ9hhXbkR/?format=html&lang=en) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5939638/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[30]](https://www.jci.org/articles/view/194749) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[31]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12454090/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[32]](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-treatment-serious-liver-disease-known-mash) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[43]](https://pace-cme.org/news/pooled-trial-analysis-shows-consistent-benefits-glp-1ra-obesity-related-hfpef/2462928/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[45]](https://www.prnewswire.com/news-releases/new-pooled-analysis-published-in-the-lancet-demonstrated-reduced-risk-of-combined-cv-death-or-worsening-heart-failure-with-semaglutide-302234945.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[52]](https://diabetesonthenet.com/diabetes-primary-care/distilled-flow-semaglutide/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[56]](https://www.ncbi.nlm.nih.gov/books/NBK603723/) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[60]](https://www.globenewswire.com/news-release/2025/11/24/3193328/0/en/novo-nordisk-a-s-evoke-phase-3-trials-did-not-demonstrate-a-statistically-significant-reduction-in-alzheimer-s-disease-progression.html) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[65]](https://clinicaltrials.gov/study/NCT03659682) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[75]](https://www.ijord.com/index.php/ijord/article/view/2239) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[76]](https://www.news-medical.net/health/How-GLP-1-Drugs-May-Help-Psoriasis-and-Hidradenitis-Suppurativa.aspx) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[85]](https://www.hra.nhs.uk/planning-and-improving-research/application-summaries/research-summaries/focus-semaglutide-effect-on-diabetic-retinopathy/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[89]](https://news.ubc.ca/2023/10/diabetes-weight-loss-drug-leads-to-gastroparesis/) | dead | 2 | 0 | 0 | 0 | 2 |
| [[90]](https://www.ifso.com/pdf/teresa-la-masters-new.pdf) | downloaded | 2 | 0 | 0 | 1 | 1 |
| [[23]](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2017/209637Orig1s000PharmR.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.researchgate.net/publication/373324017_Current_Understanding_of_Sodium_N-8-2-Hydroxylbenzoyl_Amino_Caprylate_SNAC_as_an_Absorption_Enhancer_The_Oral_Semaglutide_Experience) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9417299/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://pubmed.ncbi.nlm.nih.gov/31903692/) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[37]](https://ore.exeter.ac.uk/articles/journal_contribution/Effects_of_semaglutide_on_stroke_subtypes_in_type_2_diabetes_post_hoc_analysis_of_the_randomised_SUSTAIN_6_PIONEER_6/29787056/1/files/56823629.pdf) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[38]](https://www.appliedclinicaltrialsonline.com/view/semaglutide-cardiovascular-risk-type-2-diabetes) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[39]](https://www.researchgate.net/publication/390303462_Oral_Semaglutide_and_Cardiovascular_Outcomes_in_Persons_With_Type_2_Diabetes_According_to_SGLT2i_Use_Prespecified_Analyses_of_the_SOUL_Randomized_Trial) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[40]](https://www.tctmd.com/news/oral-semaglutide-gets-fda-approval-cv-event-reduction-high-risk-diabetes-patients) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[41]](https://pace-cme.org/news/semaglutide-reduces-mace-independent-of-baseline-adiposity/2484958/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://www.tctmd.com/news/step-hfpef-dm-trial-hints-semaglutide-hf-effects-beyond-pounds-shed) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[44]](https://pace-cme.org/news/glp-1ra-reduces-nt-probnp-patients-obesity-related-hfpef/2463033/) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[46]](https://pubmed.ncbi.nlm.nih.gov/39222642/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://www.veithsymposium.org/2025/abstracts/vei/369.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[49]](https://diabetes.org/newsroom/press-releases/semaglutide-increases-walking-capacity-patients-peripheral-artery-disease) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://www.researchgate.net/publication/399777614_Improvement_in_Walking_Distance_With_Semaglutide_in_Smokers_With_Peripheral_Artery_Disease_STRIDE_Trial_Subgroup_Analysis) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[54]](https://www.researchgate.net/publication/380879566_Long-term_kidney_outcomes_of_semaglutide_in_obesity_and_cardiovascular_disease_in_the_SELECT_trial) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[59]](https://firstwordpharma.com/story/6522602) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[63]](https://www.drugdiscoverynews.com/glp-1-and-neurodegeneration-what-the-failed-alzheimer-s-trial-means-for-drug-discovery-17287) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[64]](https://www.ucl.ac.uk/news/2025/feb/glp-1-drug-shows-little-benefit-people-parkinsons-disease) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[66]](https://www.researchgate.net/publication/380939572_Associations_of_semaglutide_with_incidence_and_recurrence_of_alcohol_use_disorder_in_real-world_population) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[67]](https://insight.jci.org/articles/view/170671) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[69]](https://commons.und.edu/cgi/viewcontent.cgi?article=1383&context=nurs-capstones) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[70]](https://www.researchgate.net/publication/377186234_Association_of_semaglutide_with_risk_of_suicidal_ideation_in_a_real-world_cohort) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[71]](https://pubmed.ncbi.nlm.nih.gov/40760781/) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[72]](https://www.hcplive.com/view/semaglutide-linked-to-suicidal-ideation-new-study-reveals) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[73]](https://www.ajmc.com/view/glp-1-drugs-tackle-both-skin-inflammation-and-metabolism-in-psoriasis) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[74]](https://pubmed.ncbi.nlm.nih.gov/41832804/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[77]](https://www.hcplive.com/view/semaglutide-cuts-asthma-attacks-by-up-to-40-real-world-study) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[78]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12302747/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[79]](https://esmed.org/tirzepatide-and-semaglutide-impact-on-sleep-apnea-and-obesity/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[80]](https://pubmed.ncbi.nlm.nih.gov/39476339/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[81]](https://www.rxfiles.ca/rxfiles/uploads/documents/ts-semaglutide-for-OA-STEP-9-2024.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[83]](https://diabetesonthenet.com/wp-content/uploads/DPC_23-4_103-104.pdf) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[84]](https://www.researchgate.net/publication/397297509_Semaglutide_and_diabetic_retinopathy_an_OHDSI_network_study) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[86]](https://www.who.int/news/item/27-06-2025-27-06-2025-semaglutide-medicines-naion) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[87]](https://www.drugdiscoverytrends.com/fdas-glp-1-vision-warning-rests-on-mixed-evidence/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[91]](https://www.medaptly.com/news/surgery/perioperative-glp-1-management-aspiration-2026/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[92]](https://pubmed.ncbi.nlm.nih.gov/38683947/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[93]](https://www.mdpi.com/2076-3271/13/4/265) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[94]](https://diabetesonthenet.com/diabetes-primary-care/distilled-surpass-cvot/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[95]](https://esmed.org/glp-1-and-incretin-agonists-in-obstructive-sleep-apnea/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[96]](https://asa.org.au/wp-content/uploads/2024/10/ASA-FS1-Perioperative-Management-of-Patients-on-GLP-1-Receptor-Agonists-GLP-1-RAs.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[53]](https://www.kidney.org/news-stories/fda-approves-ozempic-type-2-diabetes-and-chronic-kidney-disease) | downloaded | 0 · nunca citada | — | — | — | — |
| [[61]](https://pubmed.ncbi.nlm.nih.gov/41865758/) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/11/09/15/04/select) | #24–25 | #0–1, #21, #26, #30, #42, #101, #103 | #105 (pulado) | `#24` In patients with overweight or obesity and established CVD without DM, once-weekly subcutaneous semaglutide was associated with a 20% reduction in major advers… |
| [[3]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | #48–49 | #0–1, #47, #50 | #52 ⚡, #105 (pulado) | `#48` Total randomized participants: 3,533; Baseline mean eGFR: 47 mL/min/1.73 m2; ACEi, 35.1%; ARB, 60.2%; sodium–glucose cotransporter 2 (SGLT2) inhibitor, 15.6%;… |
| [[7]](https://www.abom.org/wp-content/uploads/2025/06/Phase-3-Trial-of-Semaglutide-in-Metabolic-Dysfunctio.pdf) | #60, #64–65 | #0–1, #101 | #66, #105 (pulado) | `#60` A reduction in liver fibrosis without worsening of steatohepatitis was reported in 36.8% of the patients in the semaglutide group and in 22.4% of those in the… |
| [[12]](https://www.neurologylive.com/view/from-glucose-to-cognition-where-repurposed-diabetes-drugs-stand-ad) | #4, #70, #74 | #69, #71–73 | #3 (pulado) | `#4` The 2 phase 3, placebo-controlled trials (NCT04777396; NCT04777409) randomly assigned 3808 adults aged 55 to 85 years with amyloid-confirmed mild cognitive imp… |
| [[51]](http://www.nephjc.com/news/flow) | #48–49 | #47, #50–51, #55–56 | — | `#48` A total of 5581 participants from 28 countries were screened from June 2019 through May 2021, of whom 3533 were randomized. The mean eGFR was 47 ml/min/1.73m2.… |
| [[6]](https://gpcardio.org/en/2025-05-03_semaglutide-and-walking-capacity-in-people-with-symptomatic-peripheral-artery-disease-and-type-2-diabetes-stride/) | #43 | #1, #45 | #0, #44, #105 (pulado) | `#43` Semaglutide increased walking distance in patients with symptomatic peripheral artery disease and type 2 diabetes. |
| [[2]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | #27–28 | #0–1, #21 | — | `#27` The goal of the phase 3b trial was to assess the cardiovascular efficacy of oral semaglutide, a GLP-1 receptor agonist, and to determine the risk of major adve… |
| [[4]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/08/23/19/18/step-hfpef) | #37 | #0–1, #36 | #105 (pulado) | `#37` Total randomized participants: 529; History of diabetes; Left ventricular ejection fraction (LVEF) of ≥45%; Median BMI: 37 kg/m²; maintenance dose of 2.4 mg; C… |
| [[13]](https://tnsam.org/wp-content/uploads/2025/05/jamapsychiatry_hendershot_2025_oi_240094_1743461595.52316.pdf) | #80 | — | #3, #5, #76, #79 (pulado) | `#80` This was a phase 2, double-blind, randomized, parallel-arm trial involving 9 weeks of outpatient treatment. Of 504 potential participants assessed, 48 non–trea… |
| [[5]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/04/05/03/29/step-hfpef-dm) | #38 | #0–1, #36 | — | `#38` Change in KCCQ-CSS: 13.7 vs. 6.4 (p < 0.001); % change in body weight: -9.8% vs. -3.4% (p < 0.001); Change in 6MWD from baseline to week 52: 12.7 vs. -1.6 m (p… |
| [[8]](https://academic.oup.com/eurheartj/advance-article/doi/10.1093/eurheartj/ehag524/8774585) | #34 | #32 | #33 ⚡, #2 (pulado) | `#34` Point estimates for % mediation were largest for waist circumference (64.0% [95% confidence interval (CI) 27.5, 179.6]), hsCRP (42.1% [17.9, 110.5]), HbA1c (29… |
| [[18]](https://www.fda.gov/drugs/drug-safety-communications/fda-requires-safety-labeling-changes-glucagon-peptide-1-receptor-agonists-glp-1-ras-due-potential) | — | #98 | #93, #6, #96 (pulado) | `#93` NAION is caused by decreased blood flow to the front part of the optic nerve (known as the optic disc) |
| [[27]](https://novofrontier.ai/uploads/Users_old/Digital%20Scientific%20Partner/Non%20User%20Customer%20Journey/Articles%20Repositories/review%20of%20oral%20glp-1.pdf) | #10, #12 | #13 | #11 (pulado) | `#10` Pharmacokinetic studies show 300 mg of SNAC produces the highest semaglutide plasma concentrations. ... The buffering effect of SNAC is localized near the site… |
| [[33]](https://www.mdpi.com/2813-0618/4/3/14) | — | #61 | #19, #60, #68 | `#60` Although semaglutide can be safely used in patients with cirrhosis, its efficacy in this population has not been established. |
| [[57]](https://pubmed.ncbi.nlm.nih.gov/36934740/) | — | #99 | #59, #100, #103 | `#99` The most common adverse events were nausea (21 [45%] vs four [17%]), diarrhoea (nine [19%] vs two [8%]), and vomiting (eight [17%] vs none). |
| [[58]](https://www.gastroenterologyandhepatology.net/archives/february-2025/recent-data-from-the-essence-trial-on-semaglutide-in-metabolic-dysfunction-associated-steatohepatitis/) | #63 | #60–61 | #62 | `#63` I suspect 2025 will also be a great year in the field with a second drug likely being approved by the FDA, specifically for MASH with stage 2 or 3 fibrosis. ..… |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/41138739/) | #31 | #30 | #2 (pulado) | `#31` Lancet. 2025 Nov 8;406(10516):2257-2268. doi: 10.1016/S0140-6736(25)01375-3. Epub 2025 Oct 22. ... An estimated 33% of the observed benefit on MACE was mediate… |
| [[16]](https://eprints.whiterose.ac.uk/id/eprint/212814/1/Once-weekly%20semaglutide%20versus%20placebo%20in%20adults%20with%20increased%20fracture%20risk%20a%20randomised%2C%20double-blinded%2C%20two-centre%2C%20phas.pdf) | #91 | — | #6, #92 (pulado) | `#91` This randomised, placebo-controlled, double-blinded, phase 2 clinical trial was conducted at two public hospitals in Denmark. We enrolled 64 men and women with… |
| [[17]](https://www.natap.org/2023/HIV/100923_01.htm) | #101 | #99 | #6 (pulado) | `#101` gastroparesis (HR, 3.67 [95% CI, 1.15-11.90) ... Gastroparesis was seen at a rate of about 10 cases per 1,000 semaglutide users ... Use of GLP-1 agonists compa… |
| [[24]](https://journals.bioscientifica.com/joe/article/263/1/e240046/5657/GLP-1-receptor-agonist-based-therapies-and) | #16 | #9, #14 | — | `#16` single-cell RNA-seq analyses revealed that cardiac *Glp1r* is expressed in some endothelial cells and localized in the ventricular endocardium in mice (McLean… |
| [[26]](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2019/213051Orig1s000PharmR.pdf) | #10 | #12–13 | — | `#10` SNAC is a small fatty acid derivative that interacts with plasma membranes to promote transcellular absorption of semaglutide and facilitates localized decreas… |
| [[35]](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2021.645566/full) | — | #21–22, #104 | — | `#21` The preapproval SUSTAIN 6 trial aimed to prove noninferiority of subcutaneous semaglutide as compared with placebo for the primary endpoint of time to the firs… |
| [[47]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/14/43/stride) | #43 | #45 | #44 (pulado) | `#43` Peripheral artery disease is a highly morbid type of atherosclerotic vascular disease involving the legs |
| [[55]](https://www.theisn.org/in-action/research/clinical-trials-isn-act-archive/semaglutide-in-patients-with-overweight-or-obesity-and-chronic-kidney-disease-without-diabetes-a-randomized-double-blind-placebo-controlled-clinical-trial/) | — | — | #55–56, #54 (pulado) | — |
| [[62]](https://www.clinicaltrialsarena.com/analyst-comment/ad-pd-2026-novo-nordisk-semaglutide-early-alzheimers/) | — | #69, #71–72 | — | `#69` Semaglutide was being evaluated in Alzheimer's following consistent real-world and observational evidence from multiple studies showing that patients receiving… |
| [[68]](https://pubmed.ncbi.nlm.nih.gov/38486046/) | — | #77 | #76, #78 (pulado) | `#77` Preclinical studies have shown that semaglutide decreased nicotine and alcohol consumption. |
| [[88]](https://www.neurologylive.com/view/fda-requires-naion-warning-across-glp-1-receptor-agonist-class) | — | #98 | #96–97 (pulado) | `#98` FDA said its review of animal data did not identify a biological mechanism, and that adverse event (AE) reports were difficult to interpret because NAION risk… |
| [[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13574348/) | #35 | — | #2 (pulado) | `#35` Semaglutide reduced hsCRP levels (−37.8% [104 weeks]) and risk of MACE across all hsCRP subgroups. Greater reductions in ratio-to-baseline hsCRP with semagluti… |
| [[21]](https://www.nrfhh.com/index.php/journal/article/download/2283/1314/4930) | #7 | #8 | — | `#7` Semaglutide also contains a spacer and C-18 fatty acid to achieve a half-life of approximately 165 h, predominantly via sustained albumin binding and relativel… |
| [[22]](https://www.researchgate.net/publication/325848624_Pharmacokinetics_and_Clinical_Implications_of_Semaglutide_A_New_Glucagon-Like_Peptide_GLP-1_Receptor_Agonist) | — | — | #7–8 | — |
| [[25]](https://www.scielo.br/j/jbn/a/qhJZhkW8dzY5qzRQ9hhXbkR/?format=html&lang=en) | #58 | #9 | — | `#58` In the tubules, GLP1 induces a natriuretic effect, decreasing the activity and expression of sodium-glucose cotransporters type I and II (SGLT1/2) as well as r… |
| [[29]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5939638/) | — | #14 | #15 ⚡ | `#14` The relatively similar abundance of GLP1R mRNA transcripts in all four chambers of the human heart reported here differs from the expression pattern previously… |
| [[30]](https://www.jci.org/articles/view/194749) | #17 | #58 | — | `#17` ...the only GLP-1 receptor that has been identified has limited expression in the kidney (8). Gene expression studies, as reviewed recently (9), have identifie… |
| [[31]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12454090/) | #18 | #83 | — | `#18` GLP-1RAs enhance EPC number and function through multiple mechanisms... boosts their proliferative, adhesive, migratory, and tubulogenic capacity... GLP-1RAs s… |
| [[32]](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-treatment-serious-liver-disease-known-mash) | — | #67 | #19 | `#67` Wegovy received breakthrough therapy designation for this indication and was approved under the accelerated approval pathway, which allows a therapy treating s… |
| [[43]](https://pace-cme.org/news/pooled-trial-analysis-shows-consistent-benefits-glp-1ra-obesity-related-hfpef/2462928/) | #39 | #83 | — | `#39` In the pooled study population, the mean change in the KCCQ-CSS from baseline to 52 weeks was larger in patients treated with semaglutide (n=573) than in those… |
| [[45]](https://www.prnewswire.com/news-releases/new-pooled-analysis-published-in-the-lancet-demonstrated-reduced-risk-of-combined-cv-death-or-worsening-heart-failure-with-semaglutide-302234945.html) | #41 | #42 | — | `#41` Semaglutide also led to a 41% lower risk of worsening HF (2.8% versus 4.7% with placebo; HR 0.59 (95% CI 0.41-0.82), P=0.0019). [...] Statistical analyses were… |
| [[52]](https://diabetesonthenet.com/diabetes-primary-care/distilled-flow-semaglutide/) | #51 | #50 | — | `#51` The authors conclude that the renal benefits cannot solely be explained by weight reduction or risk factor reduction, although these may contribute, and the me… |
| [[60]](https://www.globenewswire.com/news-release/2025/11/24/3193328/0/en/novo-nordisk-a-s-evoke-phase-3-trials-did-not-demonstrate-a-statistically-significant-reduction-in-alzheimer-s-disease-progression.html) | — | — | #67–68 | — |
| [[65]](https://clinicaltrials.gov/study/NCT03659682) | — | — | #69, #73 | — |
| [[75]](https://www.ijord.com/index.php/ijord/article/view/2239) | — | — | #83–84 | `#83` The semaglutide group also showed a larger CRP reduction than the placebo group (estimated treatment ratio: 0.64; 95%CI: 0.56–0.72; P<0.0001). |
| [[76]](https://www.news-medical.net/health/How-GLP-1-Drugs-May-Help-Psoriasis-and-Hidradenitis-Suppurativa.aspx) | — | #84 | #46 | `#84` The Cureus review also includes a 31-participant, open-label randomized trial of semaglutide in patients with psoriasis and type 2 diabetes. The review reporte… |
| [[85]](https://www.hra.nhs.uk/planning-and-improving-research/application-summaries/research-summaries/focus-semaglutide-effect-on-diabetic-retinopathy/) | — | — | #93–94 | `#93` NAION is caused by decreased blood flow to the front part of the optic nerve (known as the optic disc) |
| [[90]](https://www.ifso.com/pdf/teresa-la-masters-new.pdf) | — | — | #98, #97 (pulado) | — |
| [[23]](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2017/209637Orig1s000PharmR.pdf) | #7 | — | — | `#7` a large hydrophilic linker between the lysine in position 26 and the gamma glutamate whereto the fatty acid is attached 3. a C18 fatty diacid with a terminal a… |
| [[34]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9417299/) | #20 | — | — | `#20` Semaglutide may be unable to cross the regular BBB directly but could bind to serum albumin and pass through the tanycytes lining the ventricle wall. According… |
| [[38]](https://www.appliedclinicaltrialsonline.com/view/semaglutide-cardiovascular-risk-type-2-diabetes) | — | #26 | — | `#26` In March 2024, Wegovy was approved by the FDA to reduce the risk of MACE in adults with known heart disease and with obesity or overweight |
| [[41]](https://pace-cme.org/news/semaglutide-reduces-mace-independent-of-baseline-adiposity/2484958/) | #31 | — | — | `#31` Semaglutide reduced MACE compared with placebo consistently across all baseline categories of bodyweight and waist circumference, with no evidence of treatment… |
| [[42]](https://www.tctmd.com/news/step-hfpef-dm-trial-hints-semaglutide-hf-effects-beyond-pounds-shed) | — | #38 | — | `#38` The magnitude of benefit was very similar to what we saw in the first STEP-HFpEF trial in people without diabetes. At 52 weeks, the mean change in KCCQ-CSS was… |
| [[46]](https://pubmed.ncbi.nlm.nih.gov/39222642/) | #41 | — | — | `#41` We conducted a post-hoc pooled, participant-level analysis of four randomised, placebo-controlled trials (SELECT, FLOW, STEP-HFpEF, and STEP-HFpEF DM) [...] Se… |
| [[48]](https://www.veithsymposium.org/2025/abstracts/vei/369.pdf) | — | #46 | — | `#46` Subgroup analysis findings support semaglutide's efficacy across the spectrum of type 2 diabetes, including in patients without obesity and those with well-con… |
| [[49]](https://diabetes.org/newsroom/press-releases/semaglutide-increases-walking-capacity-patients-peripheral-artery-disease) | — | #45 | — | `#45` reduced the risk of disease progression by 54% |
| [[63]](https://www.drugdiscoverynews.com/glp-1-and-neurodegeneration-what-the-failed-alzheimer-s-trial-means-for-drug-discovery-17287) | — | #71 | — | `#71` Across 3,808 participants with early-stage Alzheimer’s disease, semaglutide did not significantly slow the disease’s progression |
| [[64]](https://www.ucl.ac.uk/news/2025/feb/glp-1-drug-shows-little-benefit-people-parkinsons-disease) | — | — | #72 | — |
| [[69]](https://commons.und.edu/cgi/viewcontent.cgi?article=1383&context=nurs-capstones) | — | #77 | — | `#77` semaglutide reduced binge-like alcohol drinking and reduced dependence-induced alcohol drinking in rats |
| [[72]](https://www.hcplive.com/view/semaglutide-linked-to-suicidal-ideation-new-study-reveals) | — | #82 | — | `#82` significant disproportionality was only detected for semaglutide-associated suicidal ideation (Reporting odds ratio [ROR], 1.45; 95% confidence interval [CI],… |
| [[73]](https://www.ajmc.com/view/glp-1-drugs-tackle-both-skin-inflammation-and-metabolism-in-psoriasis) | — | — | #82 | — |
| [[74]](https://pubmed.ncbi.nlm.nih.gov/41832804/) | — | — | #82 | — |
| [[77]](https://www.hcplive.com/view/semaglutide-cuts-asthma-attacks-by-up-to-40-real-world-study) | — | — | #85 | — |
| [[78]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12302747/) | — | — | #85 | — |
| [[79]](https://esmed.org/tirzepatide-and-semaglutide-impact-on-sleep-apnea-and-obesity/) | — | — | #86 | — |
| [[80]](https://pubmed.ncbi.nlm.nih.gov/39476339/) | — | — | #87 | — |
| [[81]](https://www.rxfiles.ca/rxfiles/uploads/documents/ts-semaglutide-for-OA-STEP-9-2024.pdf) | — | — | #87 | — |
| [[86]](https://www.who.int/news/item/27-06-2025-27-06-2025-semaglutide-medicines-naion) | — | — | #95 | — |
| [[87]](https://www.drugdiscoverytrends.com/fdas-glp-1-vision-warning-rests-on-mixed-evidence/) | — | — | #95 | — |
| [[91]](https://www.medaptly.com/news/surgery/perioperative-glp-1-management-aspiration-2026/) | — | — | #101 | — |
| [[92]](https://pubmed.ncbi.nlm.nih.gov/38683947/) | — | — | #102 | — |
| [[93]](https://www.mdpi.com/2076-3271/13/4/265) | — | — | #102 | — |
| [[94]](https://diabetesonthenet.com/diabetes-primary-care/distilled-surpass-cvot/) | — | — | #103 | — |
| [[95]](https://esmed.org/glp-1-and-incretin-agonists-in-obstructive-sleep-apnea/) | — | — | #103 | — |
| [[96]](https://asa.org.au/wp-content/uploads/2024/10/ASA-FS1-Perioperative-Management-of-Patients-on-GLP-1-Receptor-Agonists-GLP-1-RAs.pdf) | — | — | #104 | `#104` superiority was demonstrated with liraglutide, albiglutide, and dulaglutide |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://news.ubc.ca/2023/10/diabetes-weight-loss-drug-leads-to-gastroparesis/ — Referencia nao encontrada (404): https://news.ubc.ca/2023/10/diabetes-weight-loss-drug-leads-to-gastroparesis/

### Inacessíveis (403/timeout/SSL)

- https://www.researchgate.net/publication/380552694_Semaglutide_and_NTproBNP_in_Obesity-Related_HFpEF_Insights_from_STEP-HFpEF_Program — download excedeu 90s
- https://www.researchgate.net/publication/410945506_Semaglutide_in_obesity-related_knee_osteoarthritis_Interpreting_STEP_9_and_implications_for_practice — Rate limit persistente em https://www.researchgate.net/publication/410945506_Semaglutide_in_obesity-related_knee_osteoarthritis_Interpreting_STEP_9_and_implications_for_practice
- https://www.researchgate.net/publication/373324017_Current_Understanding_of_Sodium_N-8-2-Hydroxylbenzoyl_Amino_Caprylate_SNAC_as_an_Absorption_Enhancer_The_Oral_Semaglutide_Experience — Rate limit persistente em https://www.researchgate.net/publication/373324017_Current_Understanding_of_Sodium_N-8-2-Hydroxylbenzoyl_Amino_Caprylate_SNAC_as_an_Absorption_Enhancer_The_Oral_Semaglutide_Experience
- https://www.researchgate.net/publication/390303462_Oral_Semaglutide_and_Cardiovascular_Outcomes_in_Persons_With_Type_2_Diabetes_According_to_SGLT2i_Use_Prespecified_Analyses_of_the_SOUL_Randomized_Trial — Rate limit persistente em https://www.researchgate.net/publication/390303462_Oral_Semaglutide_and_Cardiovascular_Outcomes_in_Persons_With_Type_2_Diabetes_According_to_SGLT2i_Use_Prespecified_Analyses_of_the_SOUL_Randomized_Trial
- https://www.researchgate.net/publication/399777614_Improvement_in_Walking_Distance_With_Semaglutide_in_Smokers_With_Peripheral_Artery_Disease_STRIDE_Trial_Subgroup_Analysis — Rate limit persistente em https://www.researchgate.net/publication/399777614_Improvement_in_Walking_Distance_With_Semaglutide_in_Smokers_With_Peripheral_Artery_Disease_STRIDE_Trial_Subgroup_Analysis
- https://www.researchgate.net/publication/380879566_Long-term_kidney_outcomes_of_semaglutide_in_obesity_and_cardiovascular_disease_in_the_SELECT_trial — Rate limit persistente em https://www.researchgate.net/publication/380879566_Long-term_kidney_outcomes_of_semaglutide_in_obesity_and_cardiovascular_disease_in_the_SELECT_trial
- https://www.researchgate.net/publication/380939572_Associations_of_semaglutide_with_incidence_and_recurrence_of_alcohol_use_disorder_in_real-world_population — Rate limit persistente em https://www.researchgate.net/publication/380939572_Associations_of_semaglutide_with_incidence_and_recurrence_of_alcohol_use_disorder_in_real-world_population
- https://www.researchgate.net/publication/377186234_Association_of_semaglutide_with_risk_of_suicidal_ideation_in_a_real-world_cohort — Rate limit persistente em https://www.researchgate.net/publication/377186234_Association_of_semaglutide_with_risk_of_suicidal_ideation_in_a_real-world_cohort
- https://www.researchgate.net/publication/397297509_Semaglutide_and_diabetic_retinopathy_an_OHDSI_network_study — Rate limit persistente em https://www.researchgate.net/publication/397297509_Semaglutide_and_diabetic_retinopathy_an_OHDSI_network_study

### Bloqueadas por barreira de acesso

- https://psychiatryonline.org/ajp/doi/10.1176/appi.ajp.20260003 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://ore.exeter.ac.uk/articles/journal_contribution/Effects_of_semaglutide_on_stroke_subtypes_in_type_2_diabetes_post_hoc_analysis_of_the_randomised_SUSTAIN_6_PIONEER_6/29787056/1/files/56823629.pdf — anti_bot — barreira de acesso (anti_bot): In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable JavaScript and then re
- https://www.ncbi.nlm.nih.gov/books/NBK603723/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing www.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected after
- https://firstwordpharma.com/story/6522602 — requires_js_login_region — barreira de acesso (requires_js_login_region): You need to enable JavaScript to run this app. Loading...
- https://www.springermedizin.de/cardiovascular-metabolic-and-safety-outcomes-with-semaglutide-by/50193014 — no_content — barreira de acesso (no_content): Please enable JavaScript to proceed. Enter the characters seen in the image below: Audio is currently unavailable. Pleas

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-1`** [1] [2] [3] [4] [5] [6] [7]
  - Trecho: Randomized outcome trials reported through 2026 show that semaglutide reduces major adverse cardiovascular events (MACE) by 20% in adults with overweight or obesity and cardiovascular disease without diabetes (SELECT) a…
  - Justificativa: A evidência sustenta as afirmações essenciais do trecho: SELECT (HR 0.80 = 20% de redução de MACE), SOUL (HR 0.86 = 14% de redução de MACE com semaglutida oral em T2DM), FLOW (HR 0.76 = 24% de redução do desfecho renal…
  - Suporte veio de: [1] [2] [3] [6] [7] [4] [5]
  - Evidência: “once-weekly subcutaneous semaglutide was associated with a 20% reduction in major adverse cardiac events”
  - Não coberto pela evidência: 'reported through 2026' — a evidência cita publicações de 2024 e 2025, sem menção a 2026; 'non-cirrhotic' em ESSENCE — a evidência menciona 'fibrosis stage 2 or 3' mas não usa explicitamente o termo 'non-cirrhotic'; 'high-risk type 2 diabetes' em SOUL — a evidência descreve 'T2DM and ASCVD, CKD, or both' mas não usa o termo exato 'high-risk'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [2] | parcial | hazard ratio, 0.86; 95% CI, 0.77-0.96; p=0.006 |
    | [6] | parcial | Semaglutide increased walking distance in patients with symptomatic peripheral artery disease and type 2 diabetes. |
    | [1] | parcial | once-weekly subcutaneous semaglutide was associated with a 20% reduction in major adverse cardiac events |
    | [7] | parcial | we found evidence for the superiority of semaglutide over placebo for histologic reductions in steatohepatitis and fibr… |
    | [3] | parcial | The primary endpoint... for semaglutide vs. placebo, was: 18.7% vs. 23.2% (hazard ratio [HR] 0.76, 95% confidence inter… |
    | [5] | parcial | semaglutide was superior to placebo in improving body weight and patient-oriented QoL outcomes at 52 weeks |
    | [4] | parcial | semaglutide was superior to placebo in improving body weight (~11% greater weight loss) and patient-oriented QoL outcom… |

- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-4`** [12]
  - Trecho: Two large Phase 3 trials in early symptomatic Alzheimer's disease (EVOKE and EVOKE+) failed to slow clinical progression despite modest cerebrospinal fluid biomarker shifts, highlighting limited central exposure across…
  - Justificativa: A evidência sustenta todos os elementos essenciais da afirmação: EVOKE e EVOKE+ foram dois ensaios de fase 3 em MCI/demência leve (doença sintomática inicial) que não desaceleraram a progressão clínica (CDR-SB praticame…
  - Suporte veio de: [12]
  - Evidência: “The 2 phase 3, placebo-controlled trials (NCT04777396; NCT04777409) randomly assigned 3808 adults aged 55 to 85 years with amyloid-confirmed mild cognitive impairment (MCI) or mild dementia to once-daily oral semaglutid…”
- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-7`** [21] [22] [23]
  - Trecho: Semaglutide achieves sustained systemic exposure through structural modifications to native human GLP-1—including a peptide spacer and a C-18 fatty acid side chain—that enable reversible binding to circulating human ser…
  - Justificativa: A evidência sustenta explicitamente os elementos essenciais da afirmação: semaglutida contém um spacer e ácido graxo C-18, liga-se reversivelmente à albumina, e essa ligação protege contra degradação enzimática e filtra…
  - Suporte veio de: [21] [23]
  - Evidência: “Semaglutide also contains a spacer and C-18 fatty acid to achieve a half-life of approximately 165 h, predominantly via sustained albumin binding and relatively low renal filtration”
  - Não coberto pela evidência: O termo exato 'peptide spacer' não aparece na evidência; a evidência usa 'spacer' e 'hydrophilic linker' sem especificar que o spacer é peptídico.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [21] | sustenta | Semaglutide also contains a spacer and C-18 fatty acid to achieve a half-life of approximately 165 h, predominantly via… |
    | [23] | sustenta | a large hydrophilic linker between the lysine in position 26 and the gamma glutamate whereto the fatty acid is attached… |

### UNSUPPORTED

- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-0`** [1] [2] [3] [4] [5] [6] [7]
  - Trecho: Semaglutide, originally developed as a long-acting glucagon-like peptide-1 (GLP-1) receptor agonist for glycemic control in type 2 diabetes and later approved for chronic weight management, produces broad cardiovascular…
  - Justificativa: A evidência sustenta que semaglutida é um agonista do receptor GLP-1 aprovado para diabetes tipo 2 e obesidade, com efeitos cardiovasculares (SELECT, SOUL, STEP-HFpEF), renais (FLOW), hepáticos (ESSENCE/MASH) e vascular…
  - Suporte veio de: [7] [1] [3] [6] [2] [5] [4]
  - Evidência: “Semaglutide, a glucagon-like peptide-1 (GLP-1) receptor agonist, is approved for the treatment of type 2 diabetes and overweight or obesity, with reports of improvements in cardiovascular and renal outcomes in these pop…”
  - Não coberto pela evidência: originally developed as a long-acting GLP-1 receptor agonist; musculoskeletal effects; neurobehavioral effects
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | subcutaneous semaglutide, a glucagon-like peptide-1 receptor agonist (GLP-1 RA) |
    | [2] | parcial | oral semaglutide, a GLP-1 receptor agonist |
    | [3] | parcial | once weekly subcutaneous semaglutide was superior to placebo in improving renal and CV outcomes over a median follow-up… |
    | [4] | parcial | glucagon-like peptide-1 (GLP-1) receptor agonists |
    | [5] | parcial | Recent glucagon-like peptide-1 (GLP-1) receptor agonist use |
    | [6] | ausente | — |
    | [7] | parcial | Semaglutide, a glucagon-like peptide-1 (GLP-1) receptor agonist, is approved for the treatment of type 2 diabetes and o… |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [93] [26] [42] [23] [69] [20] [10] [38] [58] [19] [16] [25] [83] [35] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-8`** [21] [22]
  - Trecho: This engineering extends the elimination half-life of semaglutide to approximately 165 hours (roughly seven days), allowing once-weekly subcutaneous administration to reach steady-state plasma concentrations after four…
  - Justificativa: A evidência sustenta que a semaglutida tem meia-vida de ~165 h (~7 dias) e permite administração semanal, mas não menciona em nenhum momento que as concentrações plasmáticas de estado estacionário (steady-state) são alc…
  - Suporte veio de: [21]
  - Evidência: “Semaglutide also contains a spacer and C-18 fatty acid to achieve a half-life of approximately 165 h, predominantly via sustained albumin binding and relatively low renal filtration”
  - Não coberto pela evidência: steady-state plasma concentrations after four to five weeks
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [21] | parcial | dosing intervals which can be as long as once-weekly (semaglutide, dulaglutide) |
    | [22] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-14`** [24] [29]
  - Trecho: Mapping human GLP-1R distribution explains why semaglutide acts directly in some organs and indirectly in others, while exposing major divergences from rodent physiology.
  - Justificativa: A evidência sustenta que o mapeamento do GLP-1R humano revela divergências em relação a roedores (diferenças de expressão cardíaca e tireoidiana entre espécies), mas não estabelece que esse mapeamento explique por que a…
  - Suporte veio de: [29] [24]
  - Evidência: “The relatively similar abundance of GLP1R mRNA transcripts in all four chambers of the human heart reported here differs from the expression pattern previously reported in rats and mice.”
  - Não coberto pela evidência: A afirmação de que o mapeamento do GLP-1R explica por que a semaglutida age diretamente em alguns órgãos e indiretamente em outros — a evidência não conecta a distribuição do receptor a mecanismos de ação direta vs. indireta da semaglutida em órgãos específicos.; Semaglutida como agente específico cujas ações diretas/indiretas são explicadas pelo mapeamento — a evidência menciona semaglutida apenas em contextos de aterosclerose e inflamação em modelos murinos, não em relação ao mapeamento de GLP-1R humano.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [24] | parcial | *Glp1r*and human *GLP-1R*challenge the interpretation of mechanistic data |
    | [29] | parcial | The relatively similar abundance of GLP1R mRNA transcripts in all four chambers of the human heart reported here differ… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-15`** [29]
  - Trecho: Quantitative polymerase chain reaction assays across all four human heart chambers detect GLP1R mRNA at levels comparable to human pancreatic islets, yet histological examination of 35 human hearts using in situ hybridi…
  - Justificativa: A afirmacao contem duas assertivas principais que entram em conflito com a evidencia. Primeiro, a evidencia afirma que os niveis de GLP1R mRNA nos quatro camaras cardiacas sao 'comparable to those detected in RNA from h…
  - Evidência: “GLP1R mRNA transcripts were detected in all four chambers of the human heart at levels comparable to those detected in RNA from human pancreas but at lower levels than those detected in RNA from human islets”
  - Não coberto pela evidência: Afirmacao de que os niveis de GLP1R mRNA sao 'comparable to human pancreatic islets' — a evidencia diz que sao inferiores aos das ilhotas; Afirmacao de que a analise histologica 'localized definitive receptor-positive cells specifically to the sinoatrial node' — a evidencia diz que a localizacao celular definitiva permaneceu elusiva
- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-33`** [8]
  - Trecho: Individual point estimates for percentage mediation were 64.0% for waist circumference (95% CI 27.5–179.6), 42.1% for high-sensitivity C-reactive protein (hsCRP; 95% CI 17.9–110.5), 29.0% for HbA1c (95% CI −20.7–120.5),…
  - Justificativa: Os valores individuais de mediação (64.0%, 42.1%, 29.0%, 19.5% com seus respectivos ICs) e os valores de mediação conjunta (31.4% e 46.0%) estão corretos na evidência. No entanto, a afirmação de que a mediação conjunta…
  - Suporte veio de: [8]
  - Evidência: “Point estimates for % mediation were largest for waist circumference (64.0% [95% confidence interval (CI) 27.5, 179.6]), hsCRP (42.1% [17.9, 110.5]), HbA1c (29.0% [−20.7, 120.5]), and body weight (19.5% [−33.0, 110.7]),…”
  - Não coberto pela evidência: A afirmação 'across all 12 variables' para a mediação conjunta de 31.4% está incorreta — o modelo incluiu apenas 8 variáveis, não 12.; A afirmação implícita de que o modelo de 46.0% representa 'all 12 variables minus weight and waist circumference' (ou seja, 10 variáveis) está incorreta — o modelo incluiu apenas 6 variáveis.
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A maior parte dos números e intervalos de confiança citados está correta e sustentada pela evidência. Contudo, a afirmação de que a mediaçã…") — cascata: baseline → context_expansion
- **Trecho citado `semaglutina_saude_82a2bfa61988_20261117T031256Z-52`** [3]
  - Trecho: Among the small baseline SGLT2 inhibitor subgroup (n = 550), primary events were numerically balanced and underpowered for definitive conclusions, though the interaction test was negative.
  - Justificativa: A evidência afirma que o subgrupo de SGLT2 inhibitors (n=550) foi pequeno, o p-valor de interação foi negativo e o tamanho amostral foi insuficiente. Porém, a evidência diz expressamente que os pacientes em SGLT2 inhibi…
  - Evidência: “In this trial, approximately 15% of patients were on these agents at baseline. Although the p-value for interaction was negative and the sample size small (n = 550), patients on SGLT2 inhibitors did not appear to have t…”
  - Não coberto pela evidência: Numerically balanced - a evidência afirma o oposto: os pacientes em SGLT2 inhibitors não tiveram o mesmo benefício numéricamente para o endpoint primário.

---

## 10. Trechos Citados Não Auditados

Motivos: 21 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 2 citam referência não baixada/inacessível.

- `semaglutina_saude_82a2bfa61988_20261117T031256Z-53` — Referencia(s) citada(s) ['a7041a653c38b8f9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-57` — Referencia(s) citada(s) ['47a5dae02d0d4d0e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-81` — Referencia(s) citada(s) ['f2f1f20ec57e14f1'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-88` — Referencia(s) citada(s) ['ecd5db75c8c476b5'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-90` — Referencia(s) citada(s) ['c11d87854dd15515'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-2` — Parte das fontes citadas sem conteudo: referencia(s) ['06223bb9ec2da914'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-3` — Parte das fontes citadas sem conteudo: referencia(s) ['f2f1f20ec57e14f1'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-5` — Parte das fontes citadas sem conteudo: referencia(s) ['f2f1f20ec57e14f1'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-6` — Parte das fontes citadas sem conteudo: referencia(s) ['c11d87854dd15515'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-23` — Parte das fontes citadas sem conteudo: referencia(s) ['c0c7b1fb23e5b8d0'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-29` — Parte das fontes citadas sem conteudo: referencia(s) ['846b28be0e57e7b3'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-40` — Parte das fontes citadas sem conteudo: referencia(s) ['06223bb9ec2da914'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-44` — Parte das fontes citadas sem conteudo: referencia(s) ['488ee0f3e0e2c901'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-54` — Parte das fontes citadas sem conteudo: referencia(s) ['47a5dae02d0d4d0e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-66` — Parte das fontes citadas sem conteudo: referencia(s) ['696ad2d98b6128dd'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-75` — Parte das fontes citadas sem conteudo: referencia(s) ['2fd1e18176999408'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-76` — Parte das fontes citadas sem conteudo: referencia(s) ['f2f1f20ec57e14f1'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-78` — Parte das fontes citadas sem conteudo: referencia(s) ['6c561648c6df0cc9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-79` — Parte das fontes citadas sem conteudo: referencia(s) ['f2f1f20ec57e14f1'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-89` — Parte das fontes citadas sem conteudo: referencia(s) ['c11d87854dd15515', 'ecd5db75c8c476b5'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-92` — Parte das fontes citadas sem conteudo: referencia(s) ['c11d87854dd15515', '5370839a6a69415e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-96` — Parte das fontes citadas sem conteudo: referencia(s) ['f5df628e737a2d15'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-97` — Parte das fontes citadas sem conteudo: referencia(s) ['f5df628e737a2d15'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-105` — Parte das fontes citadas sem conteudo: referencia(s) ['ecd5db75c8c476b5'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-106` — Parte das fontes citadas sem conteudo: marcador(es) ['[97]', '[98]'] sem entrada na lista de referencias — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_82a2bfa61988_20261117T031256Z-11` — Parte das fontes citadas sem conteudo: referencia(s) ['2ae0a30788703213'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.