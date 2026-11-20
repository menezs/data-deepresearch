# Relatório de Auditoria — Claude (semaglutina_saude_20d223e3404d_20261102T203502Z)

**Arquivo auditado:** `answers/Claude/Emergente/semaglutina_saude.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_20d223e3404d_20261102T203502Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-02T20:49:11.787645+00:00 |
| **Total de trechos citados** | 102 |
| **Tempo de processamento** | 0:00:14:09 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 27.6 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 104 marcadores, 48 distintos |
| Referências listadas | 48 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 77 | 75.5% |
| **UNSUPPORTED** | 9 | 8.8% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 16 | 15.7% |
| **TOTAL** | 102 | 100.0% |

Sobre os 86 trechos citados auditados: SUPPORTED 89,53%, UNSUPPORTED 10,46%, CONTRADICTED 0,00%.

> **10 dos 77 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 10 estão **contados dentro** dos 77 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`13` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `2` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 4.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#98` A redução consistente de marcadores inflamatórios em vários estudos aponta para um mecanismo anti-inflamatório plausíve… | [10] [35] | [48] [27] [36] [4] [15] [20] [24] [37] [17] | — |
| `#99` Por fim, os benefícios precisam ser pesados contra riscos raros, mas reais, como pancreatite, gastroparesia e NAION. | [38] [41] | [39] [42] [36] [1] [15] [5] [43] [17] [48] [2] [31] [24] [19] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 392102 |
| **Média de tokens por requisição** | 4559.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/48 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://newsroom.clevelandclinic.org/2023/11/11/international-clinical-trial-finds-that-semaglutide-reduced-cardiovascular-events-by-20-in-adults-with-overweight-or-obesity-who-dont-have-diabetes/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[4]](https://scholars.lib.ntu.edu.tw/handle/123456789/737742) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[11]](https://www.uspharmacist.com/article/semaglutide-improved-heart-failure-symptoms-weight-loss) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[2]](https://pharmaceutical-journal.com/?p=201091) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[13]](https://vascularnews.com/?p=17611) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[15]](https://www.theisn.org/?p=40615) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[19]](https://www.healio.com/news/endocrinology/20250501/semaglutide-tied-to-significant-improvements-in-mash-liver-fibrosis-at-72-weeks) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[25]](https://the-rheumatologist.org/?p=61848) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[30]](https://www.eurekalert.org/news-releases/1126086) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[38]](https://www.ema.europa.eu/ga/news/prac-concludes-eye-condition-naion-very-rare-side-effect-semaglutide-medicines-ozempic-rybelsus-wegovy) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[6]](https://www.biospace.com/press-releases/novo-nordisk-a-s-rybelsus-oral-semaglutide-14-mg-demonstrates-superior-reduction-in-cardiovascular-events-in-the-soul-trial-at-acc-2025) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[8]](https://www.escardio.org/static-file/Escardio/Congresses/ESC) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782938) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[32]](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916462) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[36]](https://medicine.washu.edu/news/study-identifies-benefits-risks-linked-to-popular-weight-loss-drugs/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[37]](https://www.expressandstar.com/uk-news/weight-loss-jabs-may-have-wider-health-benefits-study-suggests-5730135) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[3]](https://www.sciencemediacentre.org/?p=56599) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/38914124/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[22]](https://www.managedhealthcareexecutive.com/view/fda-grants-accelerated-approval-of-wegovy-to-treat-liver-disease) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://www.novonordisk-us.com/media/news-archive/news-details.html?id=171970) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[28]](https://epocrates.com/online/article/semaglutide-reduces-alcohol-consumption-cravings-in-randomized-trial) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[31]](https://www.nih.gov/news-events/nih-research-matters/glp-1-plus-therapy-can-reduce-heavy-drinking) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[35]](https://www.neurologylive.com/view/ctad-presentation-lays-insights-disappointing-phase-3-evoke-trial-of-glp-1-semaglutide-alzheimers) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[41]](https://www.epocrates.com/online/article/glp-1-agonists-associated-with-higher-gi-risk-than-older-weight-loss-drug) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[44]](https://timesbrasil.com.br/brasil/anvisa-amplia-indicacoes-de-wegovy-e-ozempic-para-riscos-cardiovascular-e-renal/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[46]](https://revistaoeste.com/brasil/anvisa-aprova-14-novas-canetas-para-diabetes-e-obesidade/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[48]](https://www.medrxiv.org/content/10.64898/2026.04.19.26351196.full.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[5]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://www.ajmc.com/view/fda-approves-oral-semaglutide-as-first-glp-1-pill-for-weight-loss) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://www.acc.org/Latest-in-Cardiology/Articles/2023/08/23/19/16/fri-515am-step-hfpef-esc-2023) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/40169145/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[14]](https://diabetes.acponline.org/archives/2025/09/12/7.htm) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[16]](https://renalinterventions.net/semaglutide-significantly-reduces-risk-of-major-kidney-disease-events-and-mortality-in-patients-with-type-2-diabetes-and-chronic-kidney-disease) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[18]](https://abc7news.com/post/fda-approves-ozempic-reduce-risks-chronic-kidney-disease-diabetes-patients/15846312/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[20]](https://endocrinenews.endocrine.org/?p=16305) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.sec.gov/Archives/edgar/data/353278/000117184325005454/f6k_081525.htm) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[23]](https://www.vcuhealth.org/news/clinical-trial-results-show-weight-loss-drug-reduces-the-risk-of-heart-and-liver-diseases-in-people-with-obesity/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://hcplive.com/view/semaglutide-reduces-knee-osteoarthritis-pain-people-obesity) | dead | 1 | 0 | 0 | 0 | 1 |
| [[27]](https://rheumnow.com/news/glp-1-inhibitor-reduces-knee-osteoarthritis-pain) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://www.healthday.com/healthpro-news/mental-health/semaglutide-may-reduce-craving-in-alcohol-use-disorder) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://alzheimersnewstoday.com/news/oral-semaglutide-fails-slow-alzheimers-pair-clinical-trials/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[34]](https://www.precisionmedicineonline.com/node/44766) | dead | 1 | 0 | 0 | 0 | 1 |
| [[39]](https://www.who.int/news/item/27-06-2025-27-06-2025-semaglutide-medicines-naion) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[40]](https://www.ema.europa.eu/de/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-april-2024) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://www.the-hospitalist.org/hospitalist/article/38195/gastroenterology/gastrointestinal-risks-associated-with-glp-1-receptor-agonists-in-patients-with-obesity/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://clinicaltrials.gov/study/NCT06420739) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://www.poder360.com.br/poder-saude/canetas-emagrecedoras-quais-sao-as-novas-opcoes-no-brasil/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://www.diariodepernambuco.com.br/brasil/2026/08/11721434-anvisa-aprova-novas-canetas-de-semaglutida-incluindo-a-1-generica.html) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://newsroom.clevelandclinic.org/2023/11/11/international-clinical-trial-finds-that-semaglutide-reduced-cardiovascular-events-by-20-in-adults-with-overweight-or-obesity-who-dont-have-diabetes/) | #3–4, #7, #86 | #101 | — | `#3` Death from a cardiovascular event, nonfatal myocardial infarction (heart attack), or nonfatal stroke occurred during the trial in 6.5% of patients who were tre… |
| [[4]](https://scholars.lib.ntu.edu.tw/handle/123456789/737742) | #9–12, #95 | — | — | `#9` Semaglutide significantly reduced MACE incidence compared with placebo among 17 604 patients enrolled in SELECT, with consistent benefits across all baseline w… |
| [[11]](https://www.uspharmacist.com/article/semaglutide-improved-heart-failure-symptoms-weight-loss) | #23–26, #96 | — | — | `#23` In STEP-HFpEF-DM, the effects of semaglutide in 616 patients were evaluated |
| [[2]](https://pharmaceutical-journal.com/?p=201091) | #2, #5–6, #100 | — | — | `#2` The SELECT trial... included 17,604 patients who were overweight or had obesity and were aged over 45 years or older with pre-existing cardiovascular disease.… |
| [[13]](https://vascularnews.com/?p=17611) | #27–29, #90 | — | — | `#27` In the trial, 792 people with type 2 diabetes and early-stage symptomatic PAD were enrolled at 112 medical centres in 20 countries. All were randomly assigned… |
| [[15]](https://www.theisn.org/?p=40615) | #34–35, #88 | — | #33 (s/ aval.) | `#34` a slower mean annual decline in eGFR (by 1.16 ml/min/1.73m2; P <0.001) |
| [[19]](https://www.healio.com/news/endocrinology/20250501/semaglutide-tied-to-significant-improvements-in-mash-liver-fibrosis-at-72-weeks) | #39–40, #42–43 | — | — | `#39` Data were reported for the first 800 participants enrolled in the trial |
| [[25]](https://the-rheumatologist.org/?p=61848) | #49–50, #92, #97 | — | — | `#49` Those patients on semaglutide also reported a 41.7-point drop in the 0-to-100 Western Ontario and McMaster Universities Osteoarthritis Index (WOMAC) pain score… |
| [[38]](https://www.ema.europa.eu/ga/news/prac-concludes-eye-condition-naion-very-rare-side-effect-semaglutide-medicines-ozempic-rybelsus-wegovy) | #75–77 | #99 | — | `#75` PRAC has concluded that NAION is a very rare side effect of semaglutide (meaning it may affect up to 1 in 10,000 people taking semaglutide). |
| [[6]](https://www.biospace.com/press-releases/novo-nordisk-a-s-rybelsus-oral-semaglutide-14-mg-demonstrates-superior-reduction-in-cardiovascular-events-in-the-soul-trial-at-acc-2025) | #14–15 | #87 | — | `#14` SOUL was a multicentre, international, randomised, double-blind, parallel-group, placebo-controlled, phase 3 cardiovascular outcomes trial with 9,650 people en… |
| [[32]](https://www.novonordisk.com/news-and-media/news-and-ir-materials/news-details.html?id=916462) | #62, #64, #94 | — | — | `#62` The evoke and evoke+ trials did not confirm superiority of semaglutide versus placebo in the reduction of progression of Alzheimer's disease, as measured by th… |
| [[36]](https://medicine.washu.edu/news/study-identifies-benefits-risks-linked-to-popular-weight-loss-drugs/) | #66–67, #70 | — | — | `#66` GLP-1RA drugs were associated with significant benefits to neurological and behavioral health, with reduced risks of seizures and addiction to substances such… |
| [[37]](https://www.expressandstar.com/uk-news/weight-loss-jabs-may-have-wider-health-benefits-study-suggests-5730135) | #68–69, #71 | — | — | `#68` The research, published in the scientific journal Nature Medicine, found that participants who used the class of drugs which includes Wegovy and Ozempic had a… |
| [[3]](https://www.sciencemediacentre.org/?p=56599) | #8, #13 | — | — | `#8` 'Semaglutide and cardiovascular outcomes by baseline and changes in adiposity measurements: a prespecified analysis of the SELECT trial' by John Deanfield *et… |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/38914124/) | #36–37 | — | — | `#36` Semaglutide benefits on major CV events and all-cause death were similar regardless of SGLT2i use (P interaction 0.741 and 0.901, respectively). |
| [[22]](https://www.managedhealthcareexecutive.com/view/fda-grants-accelerated-approval-of-wegovy-to-treat-liver-disease) | #45, #91 | — | — | `#45` In Part 2, which is ongoing, the primary objective is to demonstrate that treatment with Wegovy lowers the risk of liver-related clinical events compared with… |
| [[24]](https://www.novonordisk-us.com/media/news-archive/news-details.html?id=171970) | #47 | #52 | — | `#47` Results from 68-week study of 407 adults with obesity and moderate knee osteoarthritis showed semaglutide 2.4 mg significantly reduced body weight, knee osteoa… |
| [[31]](https://www.nih.gov/news-events/nih-research-matters/glp-1-plus-therapy-can-reduce-heavy-drinking) | — | #59–60 | — | `#59` The team also monitored various biomarkers for alcohol consumption and liver damage in the blood. These biomarkers declined more in the semaglutide group than… |
| [[35]](https://www.neurologylive.com/view/ctad-presentation-lays-insights-disappointing-phase-3-evoke-trial-of-glp-1-semaglutide-alzheimers) | #65 | #98 | — | `#65` Following semaglutide treatment, investigators recorded significant decreases in hsCRP, with estimated treatment ratios of 0.76 (95% CI, 0.64-0.90) in EVOKE an… |
| [[44]](https://timesbrasil.com.br/brasil/anvisa-amplia-indicacoes-de-wegovy-e-ozempic-para-riscos-cardiovascular-e-renal/) | #80–81 | — | — | `#80` A **Agência Nacional de Vigilância Sanitária** anunciou, em nota divulgada nesta segunda-feira (2), a aprovação de novas indicações terapêuticas para medicamen… |
| [[46]](https://revistaoeste.com/brasil/anvisa-aprova-14-novas-canetas-para-diabetes-e-obesidade/) | #83–84 | — | — | `#83` Em 17 de agosto, a EMS obteve o registro do primeiro medicamento genérico de semaglutida do país. O produto não tem nome comercial. Na mesma data, a Anvisa apr… |
| [[48]](https://www.medrxiv.org/content/10.64898/2026.04.19.26351196.full.pdf) | #0–1 | — | — | `#0` Semaglutide reduced major adverse cardiovascular events and all-cause mortality. In dedicated complication-specific trials, semaglutide and tirzepatide showed… |
| [[5]](https://www.acc.org/latest-in-cardiology/clinical-trials/2025/03/27/15/04/soul) | #16 | — | — | `#16` The confirmatory secondary outcomes, which included major kidney disease events (a five-point composite outcome), major adverse limb events, and serious advers… |
| [[7]](https://www.ajmc.com/view/fda-approves-oral-semaglutide-as-first-glp-1-pill-for-weight-loss) | #17 | — | — | `#17` Novo Nordisk plans to launch the once-daily oral semaglutide (Wegovy) 25 mg in the US in early January 2026. |
| [[9]](https://www.acc.org/Latest-in-Cardiology/Articles/2023/08/23/19/16/fri-515am-step-hfpef-esc-2023) | #21 | — | — | `#21` Researchers also noted that one patient in the semaglutide group and 12 in the placebo group experienced an adjudicated event of heart failure hospitalization… |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/40169145/) | #31 | — | — | `#31` Research implications include the need for future studies to further elucidate mechanisms of benefit and to assess the efficacy and safety in patients with per… |
| [[16]](https://renalinterventions.net/semaglutide-significantly-reduces-risk-of-major-kidney-disease-events-and-mortality-in-patients-with-type-2-diabetes-and-chronic-kidney-disease) | #32 | — | — | `#32` The FLOW (evaluate renal function with semaglutide once weekly) study is a double-blind, randomised, placebo-controlled international trial comprising 3,533 pa… |
| [[18]](https://abc7news.com/post/fda-approves-ozempic-reduce-risks-chronic-kidney-disease-diabetes-patients/15846312/) | — | #38 | — | `#38` Ozempic, the blockbuster GLP-1 drug that was originally approved to treat type 2 diabetes, has now also been approved by the US Food and Drug Administration to… |
| [[20]](https://endocrinenews.endocrine.org/?p=16305) | #41 | — | — | `#41` 37% of participants on Wegovy had improvement in liver scarring and no worsening of MASH, compared to 22% of participants receiving placebo. |
| [[21]](https://www.sec.gov/Archives/edgar/data/353278/000117184325005454/f6k_081525.htm) | — | — | #44 | — |
| [[23]](https://www.vcuhealth.org/news/clinical-trial-results-show-weight-loss-drug-reduces-the-risk-of-heart-and-liver-diseases-in-people-with-obesity/) | #46 | — | — | `#46` And in people with higher scores on a non-invasive measure for liver scarring, called the FIB-4, semaglutide lowered major heart events by about 26%. |
| [[27]](https://rheumnow.com/news/glp-1-inhibitor-reduces-knee-osteoarthritis-pain) | #51 | — | — | `#51` it will be important to obtain data on whether semaglutide is similarly effective in persons with osteoarthritis without obesity, as well as better data on whe… |
| [[29]](https://www.healthday.com/healthpro-news/mental-health/semaglutide-may-reduce-craving-in-alcohol-use-disorder) | #55 | — | — | `#55` In a subsample of participants with current cigarette use, there was a significant treatment-by-time interaction indicating that semaglutide treatment predicte… |
| [[39]](https://www.who.int/news/item/27-06-2025-27-06-2025-semaglutide-medicines-naion) | — | #78 | — | `#78` WHO is alerting health-care professionals and regulatory authorities to the risk of non-arteritic anterior ischemic optic neuropathy (NAION) associated with th… |
| [[40]](https://www.ema.europa.eu/de/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-8-11-april-2024) | #79 | — | — | `#79` The PRAC has concluded that the available evidence does not support a causal association between the Glucagon-Like Peptide-1 receptor agonists (GLP-1) – dulagl… |
| [[42]](https://www.the-hospitalist.org/hospitalist/article/38195/gastroenterology/gastrointestinal-risks-associated-with-glp-1-receptor-agonists-in-patients-with-obesity/) | #73 | — | — | `#73` they should still be considered in the risk-benefit assessment for patients without a history of diabetes who are considering GLP-1 agonists for weight managem… |
| [[43]](https://clinicaltrials.gov/study/NCT06420739) | #74 | — | — | `#74` In the month of June 2023, three North American anesthesiology societies (the Canadian Anesthesiologists' Society, the American Society of Anesthesiologists an… |
| [[45]](https://www.poder360.com.br/poder-saude/canetas-emagrecedoras-quais-sao-as-novas-opcoes-no-brasil/) | #82 | — | — | `#82` A patente da semaglutida expirou no Brasil em 20 de março. Em maio, a Anvisa aprovou o Ozivy, da EMS, 1º produto sintético com a substância. |
| [[47]](https://www.diariodepernambuco.com.br/brasil/2026/08/11721434-anvisa-aprova-novas-canetas-de-semaglutida-incluindo-a-1-generica.html) | #85 | — | — | `#85` A agência reforça ainda a necessidade do acompanhamento médico para o uso das canetas de semaglutida: "Como todos os medicamentos do tipo GLP-1, a semaglutida… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://hcplive.com/view/semaglutide-reduces-knee-osteoarthritis-pain-people-obesity — Referencia nao encontrada (404): https://hcplive.com/view/semaglutide-reduces-knee-osteoarthritis-pain-people-obesity
- https://www.precisionmedicineonline.com/node/44766 — Referencia nao encontrada (404): https://www.precisionmedicineonline.com/node/44766

### Bloqueadas por barreira de acesso

- https://www.escardio.org/static-file/Escardio/Congresses/ESC — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. The action you just performed triggered 
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10782938 — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing pmc.ncbi.nlm.nih.gov ... Click here if you are not automatically redirected after
- https://diabetes.acponline.org/archives/2025/09/12/7.htm — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://epocrates.com/online/article/semaglutide-reduces-alcohol-consumption-cravings-in-randomized-trial — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that 
- https://www.eurekalert.org/news-releases/1126086 — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://alzheimersnewstoday.com/news/oral-semaglutide-fails-slow-alzheimers-pair-clinical-trials/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.epocrates.com/online/article/glp-1-agonists-associated-with-higher-gi-risk-than-older-weight-loss-drug — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-0`** [48]
  - Trecho: Segundo ela, a semaglutida reduziu eventos cardiovasculares maiores e mortalidade por todas as causas, mostrou benefício em desfechos de insuficiência cardíaca e em dor por osteoartrite de joelho, e foi associada a melh…
  - Justificativa: A afirmacao esta integralmente sustentada pela evidencia, especialmente pelo trecho do Abstract, que confirma cada um dos elementos: reducao de MACE e mortalidade por todas as causas, beneficio em desfechos de insuficie…
  - Suporte veio de: [48]
  - Evidência: “Semaglutide reduced major adverse cardiovascular events and all-cause mortality. In dedicated complication-specific trials, semaglutide and tirzepatide showed benefit on heart-failurerelated outcomes; tirzepatide was as…”
- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-1`** [48]
  - Trecho: Os autores defendem que a escolha entre medicamentos antiobesidade seja individualizada conforme as complicações de cada paciente, e não apenas pela eficácia na perda de peso.
  - Justificativa: A evidência sustenta explicitamente a alegação em vários trechos. Os autores afirmam diretamente que os OMMs devem ser selecionados conforme a presença e o perfil das complicações relacionadas à obesidade, em vez de ape…
  - Suporte veio de: [48]
  - Evidência: “OMMs should be selected according to the presence and profile of obesity-related complications, rather than on weight loss alone.”
- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-2`** [2]
  - Trecho: Ele incluiu 17.604 pessoas com 45 anos ou mais, com sobrepeso ou obesidade e doença cardiovascular preexistente, mas sem diabetes.
  - Justificativa: A evidência confirma explicitamente todos os elementos da afirmação: 17.604 pacientes, com 45 anos ou mais, sobrepeso ou obesidade, doença cardiovascular preexistente e sem diabetes.
  - Suporte veio de: [2]
  - Evidência: “The SELECT trial, results of which were published in the *New England Journal of Medicine* on 11 November 2023, included 17,604 patients who were overweight or had obesity and were aged over 45 years or older with pre-e…”
### UNSUPPORTED

- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-38`** [18]
  - Trecho: Com base nesses dados, a FDA aprovou em janeiro de 2025 o Ozempic para reduzir riscos associados à doença renal crônica em pessoas com diabetes tipo 2.
  - Justificativa: A evidência confirma que a FDA aprovou o Ozempic para reduzir riscos associados à doença renal crônica em pessoas com diabetes tipo 2. No entanto, a data específica de 'janeiro de 2025' não é mencionada em nenhuma parte…
  - Suporte veio de: [18]
  - Evidência: “Ozempic, the blockbuster GLP-1 drug that was originally approved to treat type 2 diabetes, has now also been approved by the US Food and Drug Administration to reduce certain risks associated with chronic kidney disease…”
  - Não coberto pela evidência: Data específica: 'janeiro de 2025' — a evidência não menciona mês nem ano da aprovação, apenas refere-se a 'Tuesday'
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-44`** [21]
  - Trecho: Em 15 de agosto de 2025, a FDA concedeu aprovação acelerada ao Wegovy para MASH não cirrótica com fibrose F2 a F3.
  - Justificativa: A evidência fornecida trata exclusivamente da política de segurança e uso do site SEC.gov, sem qualquer menção à FDA, Wegovy, MASH, aprovação acelerada, ou datas de aprovação. Não há informação suficiente para confirmar…
  - Não coberto pela evidência: Data de 15 de agosto de 2025; FDA concedeu aprovação acelerada; Wegovy
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_20d223e3404d_20261102T203502Z-52`** [24]
  - Trecho: Por isso, a droga não é considerada modificadora da doença articular e não tem aprovação para essa indicação.
  - Justificativa: A evidência sustenta explicitamente que a semaglutida não tem aprovação para o tratamento de osteoartrite de joelho. No entanto, a afirmação de que a droga 'não é considerada modificadora da doença articular' não encont…
  - Suporte veio de: [24]
  - Evidência: “Semaglutide is not approved in the U.S. for the treatment of knee osteoarthritis”
  - Não coberto pela evidência: droga não é considerada modificadora da doença articular
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 14 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 2 citam referência não baixada/inacessível.

- `semaglutina_saude_20d223e3404d_20261102T203502Z-18` — Referencia(s) citada(s) ['6625ffcb734b66a8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-19` — Referencia(s) citada(s) ['6c948e6901afc0fd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-20` — Referencia(s) citada(s) ['6c948e6901afc0fd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-22` — Referencia(s) citada(s) ['6625ffcb734b66a8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-30` — Referencia(s) citada(s) ['39daeecf51a65676'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-48` — Referencia(s) citada(s) ['5d29b469a697113a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_20d223e3404d_20261102T203502Z-53` — Referencia(s) citada(s) ['587e52e7a8c784eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-54` — Referencia(s) citada(s) ['587e52e7a8c784eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-56` — Referencia(s) citada(s) ['65efbec0ba35221e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-57` — Referencia(s) citada(s) ['65efbec0ba35221e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-58` — Referencia(s) citada(s) ['65efbec0ba35221e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-61` — Referencia(s) citada(s) ['5ff540cf79310410'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-63` — Referencia(s) citada(s) ['1fbfc9d6d181a8f5'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semaglutina_saude_20d223e3404d_20261102T203502Z-72` — Referencia(s) citada(s) ['97e347a6949e786f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-89` — Referencia(s) citada(s) ['6c948e6901afc0fd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_20d223e3404d_20261102T203502Z-93` — Referencia(s) citada(s) ['65efbec0ba35221e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.