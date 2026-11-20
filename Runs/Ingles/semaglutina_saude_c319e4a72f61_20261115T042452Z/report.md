# Relatório de Auditoria — Claude (semaglutina_saude_c319e4a72f61_20261115T042452Z)

**Arquivo auditado:** `answers/Ingles/Claude/Emergente/semaglutina_saude.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_c319e4a72f61_20261115T042452Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-18T10:36:36.535510+00:00 |
| **Total de trechos citados** | 95 |
| **Tempo de processamento** | 2:22:27:52 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 33.3 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 106 marcadores, 58 distintos |
| Referências listadas | 58 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 67 | 70.5% |
| **UNSUPPORTED** | 14 | 14.7% |
| **CONTRADICTED** | 2 | 2.1% |
| **SKIPPED** | 12 | 12.6% |
| **TOTAL** | 95 | 100.0% |

Sobre os 83 trechos citados auditados: SUPPORTED 80,72%, UNSUPPORTED 16,86%, CONTRADICTED 2,40%.

> **22 dos 67 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 22 estão **contados dentro** dos 67 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`20` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `5` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 5, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#9` Waist reduction statistically accounted for roughly one-third of the benefit, though the authors cautioned that waist s… | [5] | [4] [6] [51] | — |
| `#48` Spinal-fluid markers of tau and inflammation fell by roughly 8% to 9%, while two blood markers of nerve injury rose sli… | [30] | [12] [36] [51] [1] [7] [20] [5] | — |
| `#63` For Parkinson's disease, no semaglutide trial results were found. Within the GLP-1 class, a phase 2 trial of lixisenati… | [43] | [44] [28] [41] [12] [1] [40] [39] [31] [30] [9] [42] [5] [48] | — |
| `#86` The dedicated long-term FOCUS trial is expected to finish around February 2027. | [57] | [56] [17] [26] [13] [36] [22] [23] [43] [9] [8] [51] [29] [44] | — |
| `#93` and the failure of EVOKE shows how observational signals can mislead. | [30] [28] | [31] [29] [40] [51] [21] [57] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 721381 |
| **Média de tokens por requisição** | 8691.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/58 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[17]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | downloaded | 5 | 4 | 0 | 1 | 0 |
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2016/09/16/09/09/sustain-6) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[2]](https://www.bariatricnews.net/post/select-semaglutide-reduces-cv-events-in-non-diabetic-patients-with-overweight-or-obesity) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[6]](https://news-medical.net/news/20260927/Semaglutide-cuts-major-heart-events-but-researchers-still-cannot-fully-explain-why.aspx) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[7]](https://www.news-medical.net/news/20260824/Semaglutidee28099s-heart-benefits-may-partly-involve-reduced-inflammation.aspx) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[22]](https://www.drugs.com/clinical_trials/essence-phase-3-trial-semaglutide-showed-significant-improvements-72-weeks-adults-mash-published-22022.html) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[23]](https://www.drugs.com/newdrugs/wegovy-approved-us-mash-6595.html) | downloaded | 4 | 1 | 0 | 2 | 1 |
| [[45]](https://www.2minutemedicine.com/semaglutide-reduces-weight-and-pain-in-obese-patients-with-knee-osteoarthritis/) | downloaded | 4 | 3 | 0 | 0 | 1 |
| [[55]](https://pharmaceutical-journal.com/article/news/eye-disorder-is-a-very-rare-side-effect-of-weight-loss-drugs-concludes-ema-review) | downloaded | 4 | 3 | 0 | 0 | 1 |
| [[8]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[30]](https://www.neurologylive.com/view/ctad-presentation-lays-insights-disappointing-phase-3-evoke-trial-of-glp-1-semaglutide-alzheimers) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[33]](https://epocrates.com/online/article/semaglutide-reduces-alcohol-consumption-cravings-in-randomized-trial) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[46]](https://www.mdlinx.com/article/5-year-glp-1-data-raises-red-flags-for-bone-and-joint-health-what-next/3lLWWjMMdpDj4XP3x5NjFa) | error | 3 | 0 | 0 | 0 | 3 |
| [[52]](https://www.acc.org/about-acc/press-releases/2024/08/30/11/41/semaglutide-reduces-covid-19-related-deaths) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[3]](https://www.drugs.com/news/fda-approves-wegovy-help-prevent-heart-attack-stroke-118075.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[11]](https://epocrates.com/online/article/trial-evaluates-semaglutide-in-patients-with-hfpef-and-obesity) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[13]](https://www.biospace.com/press-releases/new-pooled-analysis-published-in-the-lancet-demonstrated-reduced-risk-of-combined-cv-death-or-worsening-heart-failure-with-semaglutide) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[14]](https://medicaldialogues.in/amp/cardiology-ctvs/news/semaglutide-boosts-walking-capacity-in-pad-and-type-2-diabetes-stride-trial-finds-145873) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[20]](https://www.news-medical.net/news/20240528/Semaglutide-shows-significant-kidney-benefits-in-non-diabetic-obese-patients-with-heart-disease.aspx) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[28]](https://neurologylive.com/view/glp-1-agonist-semaglutide-significant-prevention-alzheimers-emulation-target-trials) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[35]](https://researchportal.tuni.fi/en/publications/repurposing-semaglutide-and-liraglutide-for-alcohol-use-disorder/) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[36]](https://nature.com/articles/s41380-024-02498-5.pdf) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[51]](https://www.novo-pi.com/wegovy.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[58]](https://www.pubmed.gov/35441470/) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[4]](https://www.news-medical.net/news/20260211/Semaglutide-lowers-cardiovascular-events-even-without-major-weight-loss-researchers-report.aspx) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[5]](https://www.hcplive.com/view/select-semaglutide-indicates-possible-cardiovascular-disease-modifying-effect) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[9]](https://www.hcplive.com/view/fda-approves-oral-semaglutide-rybelsus-for-cv-risk-reduction-in-type-2-diabetes) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://www.ajmc.com/fda-approves-oral-semaglutide-as-first-glp-1-pill-for-weight-loss) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/04/05/03/29/step-hfpef-dm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://diabetes.acponline.org/archives/2025/09/12/7.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[16]](https://www.nasdaq.com/articles/novo-nordisk-emas-chmp-backs-ozempic-label-update) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[18]](https://www.biospace.com/novo-nordisk-s-semaglutide-cuts-death-risk-in-diabetics-with-ckd-in-phase-iii-trial) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://www.ozempic.com/content/dam/diabetes-patient/ozempic/pdfs/Ozempic_CKD_sNDA_Press_Release_January_28_2025.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.hcplive.com/view/remodel-mechanistic-insights-into-semaglutide-in-ckd-with-petter-bjornstad-md) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://www.ema.europa.eu/en/documents/smop-initial/chmp-summary-positive-opinion-kayshild_en.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://www.ema.europa.eu/es/medicines/human/EPAR/kayshild) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://www.healio.com/news/gastroenterology/20230331/no-difference-between-semaglutide-placebo-in-fibrosis-improvement-in-patients-with-nash) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[27]](https://health.ucsd.edu/news/press-releases/2026-07-16-glp-1-shows-promise-for-patients-with-advanced-fatty-liver-disease/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://www.biospace.com/press-releases/novo-nordisk-a-s-evoke-phase-3-trials-did-not-demonstrate-a-statistically-significant-reduction-in-alzheimers-disease-progression) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://www.news-medical.net/news/20260322/Oral-semaglutide-fails-to-slow-early-Alzheimere28099s-decline-in-two-phase-3-trials.aspx) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://doaj.org/article/2987d7d3f4c144f7aff6183d6f034505) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[34]](https://today.usc.edu/popular-weight-loss-diabetes-drug-shows-promise-in-reducing-cravings-for-alcohol/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://diabetes.acponline.org/archives/2024/08/09/8.htm) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[38]](https://www.news-medical.net/news/20240925/Study-links-semaglutide-to-reduced-opioid-overdose-risk-in-patients-with-OUD-and-diabetes.aspx) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://source.washu.edu/2025/01/study-identifies-benefits-risks-linked-to-popular-weight-loss-drugs) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://www.ema.europa.eu/es/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-april-2024) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.pharmacytimes.com/view/fda-finds-no-increased-suicide-risk-with-glp-1-medications-requests-removal-of-warning-labels) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://www.pharmacytimes.com/view/semaglutide-does-not-increase-depression-or-suicidal-ideation-risk-in-adults-with-overweight-obesity) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://michaeljfox.org/news/results-parkinsons-trial-diabetes-drug-lixisenatide-published) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[44]](https://www.parkinsons.org.uk/node/1020556) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://view.asiae.co.kr/en/article/2026060911182496843) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://clinicaltrials.gov/study/NCT07281196) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[49]](https://www.healio.com/news/endocrinology/20240705/glp1s-tied-to-lower-risk-for-10-types-of-cancer-compared-with-insulin-in-type-2-diabetes) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://clinician.nejm.org/nejm-jw.NA57373) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[53]](https://www.pharmacytimes.com/view/fda-adds-delayed-gastric-emptying-as-adverse-event-on-semaglutide-label) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[54]](https://www.periopleader.com/briefs/glp-1-labels-carry-pulmonary-aspiration-warning/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[56]](https://www.aao.org/newsroom/news-releases/detail/study-weight-loss-drug-doesnt-worsen-eye-disease) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[57]](https://clinicaltrials.gov/study/NCT03811561) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[17]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | #27, #29–30, #32 | — | #89 | `#27` Total randomized participants: 3,533 [...] DM2 with glycated hemoglobin (HbA1c) ≤10% [...] High-risk CKD (estimated glomerular filtration rate [eGFR] 25-75 mL/… |
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2016/09/16/09/09/sustain-6) | #1, #84 | #0, #2 | — | `#1` The primary outcome, CV death, nonfatal myocardial infarction (MI), or stroke for semaglutide vs. placebo, was 6.6% vs. 8.9% (hazard ratio 0.74, 95% confidence… |
| [[2]](https://www.bariatricnews.net/post/select-semaglutide-reduces-cv-events-in-non-diabetic-patients-with-overweight-or-obesity) | #3–4, #6 | — | #89 | `#3` SELECT was a randomised, double-blind, parallel-group, placebo-controlled trial designed to evaluate the efficacy of semaglutide 2.4 mg versus placebo as an ad… |
| [[6]](https://news-medical.net/news/20260927/Semaglutide-cuts-major-heart-events-but-researchers-still-cannot-fully-explain-why.aspx) | #10, #14 | #11, #90 | — | `#10` In a recent study published in the **European Heart Journal**, researchers investigated which measured cardiovascular risk factors might help explain semagluti… |
| [[7]](https://www.news-medical.net/news/20260824/Semaglutidee28099s-heart-benefits-may-partly-involve-reduced-inflammation.aspx) | #12–13, #15 | #90 | — | `#12` Semaglutide produced a 37.8% placebo-corrected reduction in geometric mean hsCRP levels at week 104. [...] In a recent study published in the journal Circulati… |
| [[22]](https://www.drugs.com/clinical_trials/essence-phase-3-trial-semaglutide-showed-significant-improvements-72-weeks-adults-mash-published-22022.html) | #36–37, #77 | #44 | — | `#36` Today, The New England Journal of Medicine (NEJM) published results from part 1 of the ongoing phase 3 ESSENCE trial which investigated the effects of once-wee… |
| [[23]](https://www.drugs.com/newdrugs/wegovy-approved-us-mash-6595.html) | #38 | — | #89, #41 ⚡, #94 (pulado) | `#38` Bagsværd, Denmark, 15 August 2025 – Novo Nordisk today announced that the US Food and Drug Administration (FDA) has approved an additional indication for Wegov… |
| [[45]](https://www.2minutemedicine.com/semaglutide-reduces-weight-and-pain-in-obese-patients-with-knee-osteoarthritis/) | #65–67 | — | #91 (pulado) | `#65` The Semaglutide Treatment Effect in People with Obesity (STEP) 9 trial was a 68-week, double-blind, randomized controlled trial evaluating once-weekly semaglut… |
| [[55]](https://pharmaceutical-journal.com/article/news/eye-disorder-is-a-very-rare-side-effect-of-weight-loss-drugs-concludes-ema-review) | #81–83 | — | #94 (pulado) | `#81` The eye disorder non-arteritic anterior ischemic optic neuropathy (NAION) is a “very rare side effect” of the use of semaglutide medicines, a review conducted… |
| [[8]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | #16–17 | — | #89 ⚡ | `#16` Total number of enrollees: 9,650 Duration of follow-up: median 49.5 months patients with type 2 diabetes mellitus (T2DM) and atherosclerotic cardiovascular dis… |
| [[30]](https://www.neurologylive.com/view/ctad-presentation-lays-insights-disappointing-phase-3-evoke-trial-of-glp-1-semaglutide-alzheimers) | #47 | #48, #93 | — | `#47` there was an estimated –0.06-point (95% CI, –0.48 to 0.36) difference between oral semaglutide (2.2) and placebo (2.2; P = .7727) in EVOKE during that time. Fo… |
| [[52]](https://www.acc.org/about-acc/press-releases/2024/08/30/11/41/semaglutide-reduces-covid-19-related-deaths) | #74–76 | — | — | `#74` Of the 833 deaths in trial participants, 58% were CV related, and 42% were non-CV related. Infection was the most common cause of non-CV death, but that occurr… |
| [[3]](https://www.drugs.com/news/fda-approves-wegovy-help-prevent-heart-attack-stroke-118075.html) | #5, #7 | — | — | `#5` which occurred in 6.5% of participants who received Wegovy compared to 8% of participants who received placebo |
| [[13]](https://www.biospace.com/press-releases/new-pooled-analysis-published-in-the-lancet-demonstrated-reduced-risk-of-combined-cv-death-or-worsening-heart-failure-with-semaglutide) | #22–23 | — | — | `#22` The study was a pooled, post hoc participant-level analysis of 3,743 patients with a history of HFpEF from four randomized trials... semaglutide led to a 31% r… |
| [[14]](https://medicaldialogues.in/amp/cardiology-ctvs/news/semaglutide-boosts-walking-capacity-in-pad-and-type-2-diabetes-stride-trial-finds-145873) | #24 | — | #91 (pulado) | `#24` the trial enrolled 792 participants aged 18 years and older, all diagnosed with T2D and PAD with intermittent claudication. Eligible participants were required… |
| [[20]](https://www.news-medical.net/news/20240528/Semaglutide-shows-significant-kidney-benefits-in-non-diabetic-obese-patients-with-heart-disease.aspx) | #33–34 | — | — | `#33` One or more of these outcomes occurred in 1.8% of semaglutide recipients as compared to 2.2% of the placebo group, thus indicating that the risk for this outco… |
| [[28]](https://neurologylive.com/view/glp-1-agonist-semaglutide-significant-prevention-alzheimers-emulation-target-trials) | #45 | — | #93 | `#45` A recently published target trial emulation of electronic healthy records from more than 1 million patients with type 2 diabetes mellitus (T2DM) showed that tr… |
| [[35]](https://researchportal.tuni.fi/en/publications/repurposing-semaglutide-and-liraglutide-for-alcohol-use-disorder/) | #54 | — | #92 (pulado) | `#54` This cohort study was an observational study conducted nationwide in Sweden [...] The cohort included 227 866 individuals with AUD [...] Semaglutide (4321 user… |
| [[36]](https://nature.com/articles/s41380-024-02498-5.pdf) | #55 | — | #58 | `#55` In patients with obesity (mean age 51.3 years, 65.6% women), semaglutide compared with non-GLP-1RA anti-obesity medications was associated with lower risk for… |
| [[51]](https://www.novo-pi.com/wegovy.pdf) | #73, #79 | — | — | `#73` WEGOVY® is contraindicated in patients with a personal or family history of MTC or in patients with Multiple Endocrine Neoplasia syndrome type 2 (MEN 2). |
| [[4]](https://www.news-medical.net/news/20260211/Semaglutide-lowers-cardiovascular-events-even-without-major-weight-loss-researchers-report.aspx) | #8 | — | — | `#8` with consistent effects across all baseline weight and waist circumference categories. [...] early weight loss did not predict subsequent MACE risk in the sema… |
| [[5]](https://www.hcplive.com/view/select-semaglutide-indicates-possible-cardiovascular-disease-modifying-effect) | — | #9 | — | `#9` Investigators estimated 33% of the observed benefit on MACE was mediated through waist circumference reduction (HR, 0.86; 95% CI, 0.77-0.97 after adjustment fo… |
| [[9]](https://www.hcplive.com/view/fda-approves-oral-semaglutide-rybelsus-for-cv-risk-reduction-in-type-2-diabetes) | #18 | — | — | `#18` Oral semaglutide is FDA-approved for cardiovascular risk reduction in high-risk type 2 diabetes patients, regardless of prior cardiovascular events. [...] Anno… |
| [[10]](https://www.ajmc.com/fda-approves-oral-semaglutide-as-first-glp-1-pill-for-weight-loss) | #19 | — | — | `#19` The FDA has approved the first oral glucagon-like peptide-1 (GLP-1) receptor agonist for weight loss and to reduce the risk of major adverse cardiovascular eve… |
| [[12]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/04/05/03/29/step-hfpef-dm) | #21 | — | — | `#21` Total randomized participants: 616; Change in KCCQ-CSS: 13.7 vs. 6.4 (p < 0.001); weight loss in this trial was lower compared with STEP-HFpEF (10.7% vs. 6.4%)… |
| [[15]](https://diabetes.acponline.org/archives/2025/09/12/7.htm) | #25 | — | — | `#25` The 40-meter improvement in the maximum walking distance with semaglutide was numerically modest and comparable to cilostazol, the only approved and recommende… |
| [[18]](https://www.biospace.com/novo-nordisk-s-semaglutide-cuts-death-risk-in-diabetics-with-ckd-in-phase-iii-trial) | #28 | — | — | `#28` In October 2023, Novo announced that it would stop FLOW ahead of schedule in line with an independent data monitoring committee's recommendation to end the stu… |
| [[19]](https://www.ozempic.com/content/dam/diabetes-patient/ozempic/pdfs/Ozempic_CKD_sNDA_Press_Release_January_28_2025.pdf) | #31 | — | — | `#31` Plainsboro, N.J., January 28, 2025 – Novo Nordisk today announced that the U.S. Food and Drug Administration (FDA) has approved Ozempic® to reduce the risk of… |
| [[21]](https://www.hcplive.com/view/remodel-mechanistic-insights-into-semaglutide-in-ckd-with-petter-bjornstad-md) | #35 | — | — | `#35` At the World Congress of Nephrology (WCN) 2026 Meeting in Yokohama, Japan, Petter Bjornstad, MD [...] presented an overview of REMODEL [...] Using functional M… |
| [[24]](https://www.ema.europa.eu/en/documents/smop-initial/chmp-summary-positive-opinion-kayshild_en.pdf) | #39 | — | — | `#39` On 29 January 2026, the Committee for Medicinal Products for Human Use (CHMP) adopted a positive opinion |
| [[25]](https://www.ema.europa.eu/es/medicines/human/EPAR/kayshild) | #40 | — | — | `#40` Kayshild has been given conditional authorisation for use in the EU. This means that it has been authorised on the basis of less comprehensive data than are no… |
| [[26]](https://www.healio.com/news/gastroenterology/20230331/no-difference-between-semaglutide-placebo-in-fibrosis-improvement-in-patients-with-nash) | #42 | — | — | `#42` In a double-blind, placebo-controlled phase 2 trial published in The Lancet Gastroenterology & Hepatology, Loomba and colleagues enrolled 71 patients (69% wome… |
| [[27]](https://health.ucsd.edu/news/press-releases/2026-07-16-glp-1-shows-promise-for-patients-with-advanced-fatty-liver-disease/) | #43 | — | — | `#43` The Phase II trial followed about 700 adults with biopsy-confirmed MASH and moderate to advanced liver scarring, including participants who had already develop… |
| [[29]](https://www.biospace.com/press-releases/novo-nordisk-a-s-evoke-phase-3-trials-did-not-demonstrate-a-statistically-significant-reduction-in-alzheimers-disease-progression) | #46 | — | — | `#46` Novo Nordisk today announced the top-line results from the 2-year primary analysis of evoke and evoke+ phase 3 trials in early-stage symptomatic Alzheimer's di… |
| [[31]](https://www.news-medical.net/news/20260322/Oral-semaglutide-fails-to-slow-early-Alzheimere28099s-decline-in-two-phase-3-trials.aspx) | #49 | — | — | `#49` Semaglutide produced some biomarker changes, but these did not translate into measurable patient benefit. [...] Differences between this trial and earlier stud… |
| [[34]](https://today.usc.edu/popular-weight-loss-diabetes-drug-shows-promise-in-reducing-cravings-for-alcohol/) | #53 | — | — | `#53` By the second month of treatment, those in the semaglutide group had reduced the quantify of alcohol consumed on drinking days by an average of nearly 30%, com… |
| [[38]](https://www.news-medical.net/news/20240925/Study-links-semaglutide-to-reduced-opioid-overdose-risk-in-patients-with-OUD-and-diabetes.aspx) | #57 | — | — | `#57` The research team - led by biomedical informatics professor Rong Xu - analyzed six years of electronic records of nearly 33,000 patients with OUD who also had… |
| [[39]](https://source.washu.edu/2025/01/study-identifies-benefits-risks-linked-to-popular-weight-loss-drugs) | #59 | — | — | `#59` GLP-1RA drugs were associated with significant benefits to neurological and behavioral health, with reduced risks of seizures and addiction to substances such… |
| [[40]](https://www.ema.europa.eu/es/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-april-2024) | #60 | — | — | `#60` The PRAC has concluded that the available evidence does not support a causal association between the Glucagon-Like Peptide-1 receptor agonists (GLP-1) – dulagl… |
| [[41]](https://www.pharmacytimes.com/view/fda-finds-no-increased-suicide-risk-with-glp-1-medications-requests-removal-of-warning-labels) | #61 | — | — | `#61` In an updated Drug Safety Communication issued on January 13, 2026, the results did not demonstrate an increased risk of suicidal behavior or ideation, along w… |
| [[42]](https://www.pharmacytimes.com/view/semaglutide-does-not-increase-depression-or-suicidal-ideation-risk-in-adults-with-overweight-obesity) | #62 | — | — | `#62` The study used pooled data from the randomized, double-blind, placebo-controlled, multicenter phase 3a STEP 1, 2, and 3 trials and phase 3b STEP 5 trial. [...]… |
| [[43]](https://michaeljfox.org/news/results-parkinsons-trial-diabetes-drug-lixisenatide-published) | — | #63 | — | `#63` Phase 2 clinical trials like this one test the safety of a treatment |
| [[44]](https://www.parkinsons.org.uk/node/1020556) | #64 | — | — | `#64` exenatide had no benefits over the placebo and didn't slow the progression of Parkinson's. [...] these disappointing phase 3 results are from the largest and l… |
| [[47]](https://view.asiae.co.kr/en/article/2026060911182496843) | #69 | — | — | `#69` at the American Diabetes Association (ADA) 2026 Annual Scientific Sessions held in New Orleans from June 5 to 8 (local time), Novo Nordisk simultaneously relea… |
| [[48]](https://clinicaltrials.gov/study/NCT07281196) | — | #70 | — | `#70` Semaglutide Effects on Sleep Apnea in Patients With Type 2 Diabetes/Obesity and Comorbid Obstructive Sleep Apnea |
| [[49]](https://www.healio.com/news/endocrinology/20240705/glp1s-tied-to-lower-risk-for-10-types-of-cancer-compared-with-insulin-in-type-2-diabetes) | — | #71 | — | `#71` People with type 2 diabetes who use a GLP-1 receptor agonist have a lower risk for 10 types of obesity-associated cancer compared with those who use insulin |
| [[50]](https://clinician.nejm.org/nejm-jw.NA57373) | — | #72 | — | `#72` All glucagon-like peptide-1 (GLP-1) receptor agonists available in the U.S. carry a boxed warning about a possible association with thyroid cancer |
| [[53]](https://www.pharmacytimes.com/view/fda-adds-delayed-gastric-emptying-as-adverse-event-on-semaglutide-label) | #78 | — | — | `#78` The FDA has added a new label change for semaglutide (Ozempic; Novo Nordisk) that includes a new section referring to delayed gastric emptying. |
| [[54]](https://www.periopleader.com/briefs/glp-1-labels-carry-pulmonary-aspiration-warning/) | #80 | — | — | `#80` The US Food and Drug Administration (FDA) has updated the labels of all treatments containing GLP-1 receptor agonists with a warning about warning about pulmon… |
| [[56]](https://www.aao.org/newsroom/news-releases/detail/study-weight-loss-drug-doesnt-worsen-eye-disease) | #85 | — | — | `#85` Previous studies have found a link between a rapid improvement in glucose control and the risk of worsening diabetic retinopathy. While the increased risk is t… |
| [[57]](https://clinicaltrials.gov/study/NCT03811561) | — | #86 | — | `#86` A Research Study to Look at How Semaglutide Compared to Placebo Affects Diabetic Eye Disease in People With Type 2 Diabetes (FOCUS) |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.nasdaq.com/articles/novo-nordisk-emas-chmp-backs-ozempic-label-update — Falha ao renderizar https://www.nasdaq.com/articles/novo-nordisk-emas-chmp-backs-ozempic-label-update via playwright: Page.goto: net::ERR_HTTP2_PROTOCOL_ERROR at https://www.nasdaq.com/articles/novo-nordisk-emas-chmp-backs-ozempic-label-update
Call log:
  - navigating to "https://www.nasdaq.com/articles/novo-nordisk-emas-chmp-backs-ozempic-label-update", waiting until "domcontentloaded"


### Bloqueadas por barreira de acesso

- https://epocrates.com/online/article/trial-evaluates-semaglutide-in-patients-with-hfpef-and-obesity — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that 
- https://doaj.org/article/2987d7d3f4c144f7aff6183d6f034505 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://epocrates.com/online/article/semaglutide-reduces-alcohol-consumption-cravings-in-randomized-trial — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that 
- https://diabetes.acponline.org/archives/2024/08/09/8.htm — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.pubmed.gov/35441470/ — http_error — barreira de acesso (http_error): 403 Forbidden

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-1`** [1]
  - Trecho: Major adverse cardiovascular events (cardiovascular death, nonfatal heart attack or nonfatal stroke) occurred in 6.6% of the semaglutide group versus 8.9% of the placebo group, a hazard ratio of 0.74 (95% CI 0.58–0.95).
  - Justificativa: A evidência sustenta explicitamente a afirmação: os percentuais (6,6% vs 8,9%), o hazard ratio (0,74) e o intervalo de confiança de 95% (0,58–0,95) correspondem exatamente. O termo 'heart attack' na afirmação é sinônimo…
  - Suporte veio de: [1]
  - Evidência: “The primary outcome, CV death, nonfatal myocardial infarction (MI), or stroke for semaglutide vs. placebo, was 6.6% vs. 8.9% (hazard ratio 0.74, 95% confidence interval 0.58-0.95, p < 0.001 for noninferiority; p = 0.02…”
- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-3`** [2]
  - Trecho: The confirmatory test in people without diabetes was SELECT, which randomized 17,604 adults aged 45 or older with overweight or obesity and established cardiovascular disease to semaglutide 2.4 mg weekly or placebo.
  - Justificativa: A evidência confirma explicitamente que SELECT foi um estudo randomizado, duplo-cego, controlado por placebo, com 17.604 adultos, idade ≥45 anos, com sobrepeso ou obesidade e doença cardiovascular estabelecida, sem hist…
  - Suporte veio de: [2]
  - Evidência: “SELECT was a randomised, double-blind, parallel-group, placebo-controlled trial designed to evaluate the efficacy of semaglutide 2.4 mg versus placebo as an adjunct to standard of care for reducing the risk of MACE in p…”
  - Não coberto pela evidência: A frequência de administração 'semanal' (weekly) não está explicitamente mencionada na evidência.
- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-4`** [2]
  - Trecho: Semaglutide reduced major adverse cardiovascular events by 20% (hazard ratio 0.80, 95% CI 0.72–0.90).
  - Justificativa: A evidência afirma explicitamente que semaglutida 2.4mg proporcionou uma redução de risco de 20% em MACE versus placebo, com HR 0.80 e IC 95% 0.72–0.90, o que corresponde exatamente à afirmação.
  - Suporte veio de: [2]
  - Evidência: “semaglutide 2.4mg delivered a statistically significant 20% risk reduction in MACE over a period of up to five years versus placebo (HR: 0.80; 95% confidence interval: 0.72; 0.90, p<0.001)”
### UNSUPPORTED

- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-0`** [1]
  - Trecho: The first hint of cardiovascular benefit came from SUSTAIN-6, a pre-approval safety trial of injectable semaglutide in 3,297 people with type 2 diabetes and high cardiovascular risk, followed for about two years.
  - Justificativa: A evidência sustenta a maioria dos detalhes factuais sobre SUSTAIN-6 (trial de segurança CV, semaglutida injetável, 3.297 inscritos, DM2, alto risco CV, ~2,1 anos de seguimento). No entanto, a afirmação de que SUSTAIN-6…
  - Suporte veio de: [1]
  - Evidência: “The goal of the trial was to assess the cardiovascular (CV) safety of semaglutide in patients with type 2 diabetes mellitus (DM2) at high risk for CV events.”
  - Não coberto pela evidência: Afirmação de que SUSTAIN-6 foi 'a primeira pista' (first hint) de benefício cardiovascular — a evidência não estabelece primazia cronológica nem confirma que foi o primeiro trial a mostrar benefício CV; Classificação explícita como 'trial de pré-aprovação' (pre-approval) — a evidência menciona requisitos da FDA para estudos premarketing, mas não rotula explicitamente SUSTAIN-6 como trial de pré-aprovação
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-2`** [1]
  - Trecho: The benefit was driven mainly by fewer strokes, weight loss was modest at roughly 4% to 5%, and because the trial was designed to show noninferiority, its superiority result was suggestive rather than definitive.
  - Justificativa: A evidência sustenta partes da afirmação: (1) o benefício foi impulsionado principalmente por redução de stroke (único componente individual significativo, p=0.04, enquanto MI e CV death não foram significativos); (2) a…
  - Suporte veio de: [1]
  - Evidência: “All stroke: 1.6% vs. 2.7%, p = 0.04”
  - Não coberto pela evidência: A caracterização de que o resultado de superioridade foi 'suggestive rather than definitive' não está explicitamente na evidência; é uma interpretação metodológica que exige conhecimento externo sobre ensaios de não-inferioridade.
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-9`** [5]
  - Trecho: Waist reduction statistically accounted for roughly one-third of the benefit, though the authors cautioned that waist size may be a risk marker rather than a causal pathway.
  - Justificativa: A evidência sustenta que 33% do benefício foi mediado pela redução da circunferência da cintura, mas não contém nenhuma menção explícita a que os autores alertaram que o tamanho da cintura pode ser um marcador de risco…
  - Suporte veio de: [5]
  - Evidência: “Investigators estimated 33% of the observed benefit on MACE was mediated through waist circumference reduction (HR, 0.86; 95% CI, 0.77-0.97 after adjustment for time-varying changes in waist circumference).”
  - Não coberto pela evidência: A afirmação de que os autores alertaram que o tamanho da cintura pode ser um marcador de risco em vez de uma via causal (risk marker rather than a causal pathway) não aparece na evidência.
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [4] [6] [51] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-41`** [23]
  - Trecho: Both approvals depend on the second part of ESSENCE, which will test whether semaglutide reduces hard liver outcomes such as decompensation and is expected to report around 2029.
  - Justificativa: A evidência afirma explicitamente que as aprovações (FDA acelerada, EU e Japão) são baseadas na parte 1 do estudo ESSENCE, não na parte 2. A claim afirma o oposto: que ambas as aprovações dependem da segunda parte. O el…
  - Evidência: “The accelerated approval is based on part 1 of the ESSENCE trial”
  - Não coberto pela evidência: Both approvals depend on the second part of ESSENCE — contradito pela evidência, que indica dependência da parte 1; hard liver outcomes such as decompensation — a evidência menciona 'liver-related clinical events' mas não especifica 'decompensation'
- **Trecho citado `semaglutina_saude_c319e4a72f61_20261115T042452Z-89`** [2] [8] [17] [23]
  - Trecho: Semaglutide reduces major cardiovascular events in people with and without diabetes, protects the kidneys in diabetic kidney disease with albuminuria, and resolves steatohepatitis in noncirrhotic MASH; all three claims…
  - Justificativa: A janela confirma apenas que semaglutida reduz eventos cardiovasculares maiores (MACE) em pacientes com diabetes tipo 2, mas não em pessoas sem diabetes. Além disso, contradiz explicitamente a alegação de proteção renal…
  - Evidência: “The SOUL trial showed that in patients with T2DM and ASCVD, CKD, or both, use of oral semaglutide was associated with a significantly lower risk of MACE vs. placebo”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [8] | contradiz | The SOUL trial showed that in patients with T2DM and ASCVD, CKD, or both, use of oral semaglutide was associated with a… |

  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "A evidência sustenta fortemente três das quatro partes da afirmação: (1) redução de MACE em diabéticos (SOUL) e não diabéticos (SELECT); (2…") — cascata: baseline → context_expansion → full_doc_scan

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 6 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 3 citam referência não baixada/inacessível.

- `semaglutina_saude_c319e4a72f61_20261115T042452Z-20` — Referencia(s) citada(s) ['ffcb3b3726568b29'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-26` — Referencia(s) citada(s) ['a2c13a5f20e8c4b0'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-50` — Referencia(s) citada(s) ['b981e0d9bdde8dd3'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-51` — Referencia(s) citada(s) ['587e52e7a8c784eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-52` — Referencia(s) citada(s) ['587e52e7a8c784eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-56` — Referencia(s) citada(s) ['4e26e51e3a4e6313'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-68` — Referencia(s) citada(s) ['28dfd4633d46fcb8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-87` — Referencia(s) citada(s) ['28dfd4633d46fcb8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-88` — Referencia(s) citada(s) ['a1fc556bcd60ce59'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-91` — Parte das fontes citadas sem conteudo: referencia(s) ['ffcb3b3726568b29'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-92` — Parte das fontes citadas sem conteudo: referencia(s) ['587e52e7a8c784eb'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_c319e4a72f61_20261115T042452Z-94` — Parte das fontes citadas sem conteudo: referencia(s) ['28dfd4633d46fcb8', 'a1fc556bcd60ce59'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.