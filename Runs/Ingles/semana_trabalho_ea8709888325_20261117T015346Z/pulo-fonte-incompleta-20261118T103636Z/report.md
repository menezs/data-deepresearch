# Relatório de Auditoria — Gemini (semana_trabalho_ea8709888325_20261117T015346Z)

**Arquivo auditado:** `answers/Ingles/Gemini/EmConsolidacao/semana_trabalho.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_ea8709888325_20261117T015346Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T01:47:26.124541+00:00 |
| **Total de trechos citados** | 114 |
| **Tempo de processamento** | 0:23:53:40 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 26.2 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-17 01:54:16+00:00 |
| Citações no corpo | 235 marcadores, 81 distintos |
| Referências listadas | 81 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 71 | 62.3% |
| **UNSUPPORTED** | 36 | 31.6% |
| **CONTRADICTED** | 4 | 3.5% |
| **SKIPPED** | 3 | 2.6% |
| **TOTAL** | 114 | 100.0% |

Sobre os 111 trechos citados auditados: SUPPORTED 63,96%, UNSUPPORTED 32,43%, CONTRADICTED 3,60%.

> **37 dos 71 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 37 estão **contados dentro** dos 71 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`48` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `6` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `12` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `12` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 11, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#30` Crucially, however, Pencavel warned against assuming century-old factory fatigue curves guarantee constant output from… | [33] | [3] [18] [4] [35] [48] [25] [9] [72] [7] [73] [76] [44] | — |
| `#36` Early critics worried that compressing five days of deliverables into four days would intensify work pace and accelerat… | [4] | [35] [51] [41] [34] [52] [11] [3] [18] [9] [19] | — |
| `#41` Private corporate trials catalyzed modern interest in 2018 when New Zealand estate-planning firm Perpetual Guardian mov… | [39] [40] | [68] [79] [35] [61] [10] [41] [58] [3] [48] [59] [60] [54] | — |
| `#43` In 2019, Microsoft Japan tested paid Fridays off and self-reported nearly 40% higher productivity alongside 23% lower e… | [40] | [79] [45] [68] [3] [23] [11] [41] [35] [4] [39] [10] [80] | — |
| `#51` Multi-firm private trials coordinated by 4 Day Week Global scaled rapidly after 2022. | [35] | [68] [3] [45] [51] [44] [11] [39] [9] [41] | — |
| `#69` Public-sector trials in Britain tested whether four-day schedules could withstand citizen-facing scrutiny. | [44] [52] [55] | [18] [35] [68] [3] [57] [11] [53] [54] [45] | — |
| `#72` Yet a DJS Research resident survey recorded only 45% public support, and central government opposition persisted across… | [52] [53] [54] | [44] [58] [74] [18] [35] [48] [72] [57] [15] [20] [12] | — |
| `#75` In April 2019, London's Wellcome Trust scrapped plans to trial a four-day week for its 800 head-office staff, concludin… | [58] | [39] [35] [45] [3] [4] [68] [41] [52] [46] [18] [23] [44] [55] [48] | — |
| `#94` Europe's only national four-day statute highlights the limits of mandatory compression: Belgium's 2022 reform gave full… | [22] [66] | [68] [35] [11] [9] [17] [23] [21] [18] [34] [3] [67] [15] | — |
| `#97` Spain allocated €50 million for SME pilots and Valencia reopened regional grants capped at €200,000 per company in Octo… | [12] [68] | [11] [70] [69] [3] [15] [44] [67] [8] | — |
| `#99` In the United States, federal legislation remains gridlocked despite renewed focus on automation and artificial intelli… | [13] [71] | [68] [25] [33] [72] [10] [7] [29] [75] [76] [9] [11] [74] [46] [20] | — |
| `#110` Localized shutdowns can cut energy and transport emissions, as in Microsoft Japan's 23% electricity savings and Valenci… | [40] [69] | [79] [45] [80] [70] [78] [35] [41] [7] [3] [23] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1838355 |
| **Média de tokens por requisição** | 16561.8 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/81 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 4.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[3]](https://www.takeroon.com/blog/4-day-work-week-evidence) | downloaded | 23 | 9 | 12 | 2 | 0 |
| [[4]](https://www.thepeoplespace.com/insights/ideas/4-day-week-works-only-if-you-change-work) | downloaded | 8 | 3 | 5 | 0 | 0 |
| [[8]](https://4dayweek.io/country/germany) | downloaded | 7 | 0 | 7 | 0 | 0 |
| [[9]](https://www.digital-chiefs.de/en/70-continue-20-drop-out-the-honest-balance-sheet-of-the-four-day-week/) | downloaded | 7 | 1 | 5 | 1 | 0 |
| [[36]](https://www.scribd.com/document/785140050/4-week-day-in-Germany) | downloaded | 7 | 0 | 3 | 4 | 0 |
| [[10]](https://www.theguardian.com/business/2026/mar/16/four-day-work-working-week-what-happened) | downloaded | 6 | 0 | 4 | 2 | 0 |
| [[48]](https://medium.com/@andy.a.g/141-organizations-tried-a-four-day-week-burnout-fell-most-for-people-who-cut-8-hours-or-more-c01b5586d76f) | downloaded | 6 | 3 | 2 | 1 | 0 |
| [[5]](https://www.researchgate.net/publication/392873157_The_consequences_of_a_compressed_workweek_a_systematic_literature_review) | downloaded | 5 | 1 | 1 | 3 | 0 |
| [[21]](https://4dayweek.io/country/iceland) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[25]](https://resources.rework.com/libraries/history-of-productivity/history-of-the-8-hour-workday) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[29]](https://www.cambridge.org/core/journals/business-history-review/article/kelloggs-sixhour-day-a-capitalist-vision-of-liberation-through-managed-work-reduction/9AFB41950B8B5C4A050F69A3CA3A975C) | downloaded | 5 | 0 | 5 | 0 | 0 |
| [[30]](https://www.informationweek.com/it-leadership/six-hour-shifts-satisfied-kellogg-s-appetite-for-productivity) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[33]](https://www.scribd.com/document/977314082/Diminishing-Returns-at-Work-The-Consequences-of-Long-Working-Hours-ISBN-9780190876166-0190876166-PDF-ebook-with-Full-Chapters) | downloaded | 5 | 1 | 0 | 4 | 0 |
| [[64]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9979633/) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[13]](https://www.krem.com/article/news/nation-world/32-hour-workweek-bill-introduced-congress/507-60ff6b6f-69f7-4807-95f6-a9ba2cbe87bc) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[26]](https://www.tupi.fm/mundo/em-1926-henry-ford-reduziu-a-semana-de-trabalho-de-suas-fabricas-para-5-dias-e-40-horas-sem-cortar-salarios-e-a-decisao-mudou-a-industria-americana/) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[31]](https://scispace.com/papers/the-productivity-of-working-hours-1w39cbiq4q) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[40]](https://www.weforum.org/stories/jobs-and-the-future-of-work/four-day-work-life-balance-trial) | downloaded | 4 | 0 | 0 | 4 | 0 |
| [[43]](https://autonomy.work/wp-content/uploads/2024/10/Iceland_-1.pdf) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[44]](https://4dayweek.io/country/united-kingdom) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[52]](https://www.scambs.gov.uk/four-day-working-week) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[62]](https://bainultra.com/blogs/news/sweden-experiments-with-six-hour-workday-finds-people-enjoy-having-lives) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[2]](https://www.help.senate.gov/download/dr-schor-help-testimony-3-14-24pdf) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[6]](https://www.theguardian.com/world/2017/jan/04/sweden-sees-benefits-six-hour-working-day-trial-care-workers) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[7]](https://www.smithschool.ox.ac.uk/news/day-save-planet-heres-what-four-day-week-could-mean-uk-carbon-emissions) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[11]](https://www.usecarly.com/blog/four-day-work-week-statistics/) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[12]](https://4dayweek.io/country/spain) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[15]](https://4dayweek.io/country/south-korea) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[17]](https://aciara.com.br/fim-da-escala-6x1-veja-jornada-em-outros-paises/) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[20]](https://autonomy.work/wp-content/uploads/2021/06/ICELAND_4DW.pdf) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[22]](https://4dayweek.io/country/belgium) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[24]](https://www.bc.edu/bc-web/sites/bc-magazine/fall-2022-issue/linden-lane/a-four-day-work-week-.html) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[35]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693da184212d4f030b2a8032/1765646724493/US+Ireland+Results+2023.pdf) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[65]](https://www.researchgate.net/publication/361430073_Effects_of_4-Day_School_Weeks_on_Older_Adolescents_Examining_Impacts_of_the_Schedule_on_Academic_Achievement_Attendance_and_Behavior_in_High_School) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[71]](https://www.safetyandhealthmagazine.com/bernie-sanders-and-mark-takano-renew-push-for-a-32-hour-workweek/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[1]](https://pubmed.ncbi.nlm.nih.gov/40691306/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[14]](https://www.humanresourcesonline.net/tokyo-to-introduce-a-four-day-workweek-and-flexible-working-hours-for-government-staff-from-april-2025) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[16]](https://www12.senado.leg.br/noticias/audios/2026/10/congresso-promulga-emendas-sobre-fim-da-escala-6x1-e-agentes-de-saude) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[18]](https://openpaper.dev/examples/four-day-work-week-outcomes) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[19]](https://www.unisc.edu.au/about/unisc-news/news-archive/2025/november/why-the-four-day-workweek-is-more-than-just-a-fad-boosting-wellbeing-productivity-and-the-future-of-work) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[23]](https://4dayweek.io/country/japan) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[37]](https://greenamerica.org/evolution-work/can-4-day-work-week-heal-people-and-planet) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[39]](https://www.theguardian.com/money/2019/feb/19/four-day-week-trial-study-finds-lower-stress-but-no-cut-in-output) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[49]](https://www.researchgate.net/publication/390052868_Four-Day_Week_Results_from_Portuguese_Trial_Final_Report) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[51]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693e8a0d0669596b183b27fa/1765706253519/Brazil+4+Day+Week+Pilot+2024.pdf) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[53]](https://www.localgov.co.uk/Four-day-week-trial-success-says-council/62636) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[55]](https://www.gov.scot/policies/public-sector-pay/four-day-working-week/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[58]](https://www.theguardian.com/uk-news/2019/apr/12/wellcome-trust-drops-plans-to-trial-four-day-working-week) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[59]](https://www.unilever.com/news/news-search/2022/fourday-work-week-trial-to-start-in-australia/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[66]](https://www.acerta.be/en/inspiration/four-day-working-week-eight-out-of-ten-smes-not-behind-the-idea) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[69]](https://4dayweek.io/region/valencia) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[72]](https://www.rockymountainemployersblog.com/blog/2026/10/1/a-new-bill-in-congress-proposes-a-shift-to-a-thirty-two-hour-workweek-without-reducing-salaries) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[76]](https://worldatwork.org/publications/workspan-daily/pennsylvania-law-would-incentivize-four-day-workweek) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[80]](https://www.welcometothejungle.com/en/articles/how-the-4-day-workweek-can-help-to-reduce-carbon-emissions) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[27]](https://agenciabrasil.ebc.com.br/politica/noticia/2026-05/ha-100-anos-ford-instituia-jornada-de-40-horas-nos-estados-unidos) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[28]](https://teachingamericanhistory.org/document/henry-fords-five-day-week/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[32]](https://www.econstor.eu/bitstream/10419/145237/1/dp10103.pdf) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[34]](https://kommerstad.org/journal/article/download/943/696) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[38]](https://ideas.repec.org/a/nat/nathum/v9y2025i10d10.1038_s41562-025-02259-6.html) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[41]](https://buffer.com/resources/4-day-workweek-2021/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://workfour.org/case-studies/blog-post-title-four-5l997) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://www.europeanbusinessreview.eu/page.asp?pid=6985) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[46]](https://www.theemploymentlawsolicitors.co.uk/news/blog/four-day-working-week-3/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[47]](https://4dayweek.io/country/australia) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://policycommons.net/artifacts/13373666/portugal20420day20week20pilot20results20-20420day20week20global/14271453/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[54]](https://www.theguardian.com/society/2025/oct/29/councils-clampdown-four-day-working-weeks-south-cambridgeshire) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[56]](https://autonomy.work/portfolio/sww-scotland-public-sector/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[57]](https://www.theguardian.com/business/2025/aug/27/scottish-government-trial-of-four-day-week-improves-productivity-and-staff-wellbeing) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[60]](https://www.uts.edu.au/news/2022/11/uts-research-reveals-success-unilever-four-day-work-week) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[61]](https://www.theguardian.com/australia-news/2022/nov/02/australian-workers-at-global-company-to-trial-four-day-week-after-success-of-new-zealand-pilot) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[63]](https://www.ncbi.nlm.nih.gov/books/NBK75539/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[67]](https://4dayweek.io/country/france) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[68]](https://www.4dayjob.com/blog/countries-with-4-day-work-week) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[70]](https://www.healthplanspain.com/blog/health-news/2062-valencian-pilot-scheme-shows-4-day-work-week-improved-workers-health.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[73]](https://www.pbs.org/newshour/politics/what-to-know-about-bernie-sanderss-bill-for-the-u-s-to-adopt-a-32-hour-workweek) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[74]](https://workfour.org/policy-developments) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[75]](https://www.govdocs.com/maryland-4-day-workweek-bill/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[77]](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/10/senado-aprova-fim-da-escala-6x1-pauta-prioritaria-do-governo-federal) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[78]](https://www.4dayweek.com/news-posts/environmental-benefits-2hxgl) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[79]](https://4dayweek.io/pro/environment) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[81]](https://www.researchgate.net/publication/375365733_The_social_economic_and_environmental_impacts_of_a_4-day_workweek_in_an_organization) | downloaded | 1 | 0 | 0 | 1 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[3]](https://www.takeroon.com/blog/4-day-work-week-evidence) | #0–1, #3, #9, #40, #55, #57, #59, #62 | #2, #5, #8, #10–11, #13, #35, #49, #54, #58, #105, #113 | #33, #84 ⚡ | `#0` For well-being in volunteer, mostly white-collar firms: yes, consistently. Burnout drops, sleep improves, fatigue falls, people stay longer... Output mostly he… |
| [[4]](https://www.thepeoplespace.com/insights/ideas/4-day-week-works-only-if-you-change-work) | #33, #39–40 | #2, #32, #36–37, #113 | — | `#33` Before the six-month trial began each company had around eight weeks to reorganise its operations. Meetings were streamlined and workflows were redesigned. |
| [[8]](https://4dayweek.io/country/germany) | — | #4–5, #12, #64–66, #93 | — | `#4` Chancellor Friedrich Merz said in May 2025 that with a four-day week and work-life balance Germany would not keep its prosperity. The 2025 coalition agreement… |
| [[9]](https://www.digital-chiefs.de/en/70-continue-20-drop-out-the-honest-balance-sheet-of-the-four-day-week/) | #79 | #4–5, #65, #74, #113 | #66 ⚡ | `#79` The 2-year follow-up (published February 2026) shows: 70 percent of participants continue to work in some reduced form. [...] In organizations with more than 7… |
| [[36]](https://www.scribd.com/document/785140050/4-week-day-in-Germany) | — | #63–65 | #34, #66, #108, #112 | `#63` Additionally, objective measurements, such as smartwatch tracking data and hair samples, were integrated to provide broader insights, combining subjective and… |
| [[10]](https://www.theguardian.com/business/2026/mar/16/four-day-work-working-week-what-happened) | — | #4, #6, #76, #78 | #74, #83 | `#4` Last year Bupa and Unilever walked away from trials of reduced work hours, citing the four-day model as 'rigid'. ... in Belgium workers have a right to a four-… |
| [[48]](https://medium.com/@andy.a.g/141-organizations-tried-a-four-day-week-burnout-fell-most-for-people-who-cut-8-hours-or-more-c01b5586d76f) | #59–61 | #58, #88 | #87 | `#59` The company average fell from 39.21 to 34.01 a week, and the most common week went from 40 hours to 32. In the control companies, it went from 38.88 to 39.16.… |
| [[5]](https://www.researchgate.net/publication/392873157_The_consequences_of_a_compressed_workweek_a_systematic_literature_review) | #86 | #2 | #1, #113, #84 ⚡ | `#86` Twenty studies met the inclusion criteria. The study is registered in Prospero (CRD42020172595). Results suggest that a compressed workweek increases sickness… |
| [[21]](https://4dayweek.io/country/iceland) | #10, #48 | #46, #49–50 | — | `#10` Hours cut from 40 to 35 or 36 a week with no cut in pay, for over 2,500 staff in over 100 workplaces. ... about 86% of Iceland's working population had by June… |
| [[25]](https://resources.rework.com/libraries/history-of-productivity/history-of-the-8-hour-workday) | #14–15, #19 | #17–18 | — | `#14` After 1941, the legal baseline barely moved. ... The 40-hour framework came from an era of factory shifts. ... The first large test of changing the baseline ar… |
| [[29]](https://www.cambridge.org/core/journals/business-history-review/article/kelloggs-sixhour-day-a-capitalist-vision-of-liberation-through-managed-work-reduction/9AFB41950B8B5C4A050F69A3CA3A975C) | — | #20–24 | — | `#20` "Kellogg Company Announces Six-Hour Day and Basic Pay Raise to Aid Employment: Takes World Leadership in Inauguration of New Industrial Work Policy," Battle Cr… |
| [[30]](https://www.informationweek.com/it-leadership/six-hour-shifts-satisfied-kellogg-s-appetite-for-productivity) | #20–23 | #24 | — | `#20` Inspired by reports that a six-hour shift increased productivity at an English soap company, Kellogg Co. founder W.K. Kellogg changed cereal-plant production s… |
| [[33]](https://www.scribd.com/document/977314082/Diminishing-Returns-at-Work-The-Consequences-of-Long-Working-Hours-ISBN-9780190876166-0190876166-PDF-ebook-with-Full-Chapters) | #25 | — | #28, #30, #113, #31 ⚡ | `#25` while production initially increases with longer hours, beyond a certain point productivity falls due to worker fatigue and errors. This challenges the assumpt… |
| [[64]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9979633/) | #87, #90 | #89, #91–92 | — | `#87` Understanding how these four-day school weeks impact students of different demographic groups, skill levels, and educational programmatic needs will inform sch… |
| [[26]](https://www.tupi.fm/mundo/em-1926-henry-ford-reduziu-a-semana-de-trabalho-de-suas-fabricas-para-5-dias-e-40-horas-sem-cortar-salarios-e-a-decisao-mudou-a-industria-americana/) | #16 | #17–19 | — | `#16` Em 1º de maio de 1926, a Ford Motor Company adotou a semana de cinco dias e 40 horas para os operários das suas fábricas nos Estados Unidos. [...] Os funcionár… |
| [[40]](https://www.weforum.org/stories/jobs-and-the-future-of-work/four-day-work-life-balance-trial) | — | — | #41, #43, #77, #110 | — |
| [[43]](https://autonomy.work/wp-content/uploads/2024/10/Iceland_-1.pdf) | #48–49 | #47, #50 | — | `#48` The survey gathered data between 2021 and 2022. [...] Published 2024 by © The Autonomy Institute and Alda (Association for Sustainability and Democracy) [...]… |
| [[44]](https://4dayweek.io/country/united-kingdom) | — | #69–71, #73 | — | `#69` In the public sector, South Cambridgeshire District Council made a four-day week permanent in July 2025, though in October 2025 the Government wrote to its lea… |
| [[52]](https://www.scambs.gov.uk/four-day-working-week) | #71 | #69–70, #72 | — | `#71` An independent report from the Universities of Salford, Bradford and Cambridge, published in July 2025, highlights how 21 of 24 services have improved or staye… |
| [[62]](https://bainultra.com/blogs/news/sweden-experiments-with-six-hour-workday-finds-people-enjoy-having-lives) | #80 | #81–82 | #83 | `#80` The nursing home hired 14 new staff members to cover the missing hours. |
| [[6]](https://www.theguardian.com/world/2017/jan/04/sweden-sees-benefits-six-hour-working-day-trial-care-workers) | #3, #80 | #81 | — | `#3` To ensure that patients at the home for the elderly were attended to for the same number of hours as before, 15 new employees were hired for the duration of th… |
| [[7]](https://www.smithschool.ox.ac.uk/news/day-save-planet-heres-what-four-day-week-could-mean-uk-carbon-emissions) | #3, #108, #111 | — | — | `#3` My results revealed that switching to a four-day week with no loss of pay would only reduce emissions if people dedicated their newfound leisure time to low-ca… |
| [[11]](https://www.usecarly.com/blog/four-day-work-week-statistics/) | — | #6, #95 | #67 ⚡ | `#6` 0.8% of Belgian private-sector employees used Belgium's full-time four-day regime as of March 31, 2025 |
| [[12]](https://4dayweek.io/country/spain) | #93 | #6, #97 | — | `#93` Congress rejects the bill to cut the legal week to 37.5 hoursAmendments to the whole bill from Junts, PP and Vox passed by 178 votes to 170, ending the bill's… |
| [[15]](https://4dayweek.io/country/south-korea) | #106 | #7 | #104 | `#106` The OECD puts average usual weekly hours at 39.4 for all employed people in 2025, and 43.4 for full-time workers. The Labor Standards Act limits work to 40 hou… |
| [[17]](https://aciara.com.br/fim-da-escala-6x1-veja-jornada-em-outros-paises/) | — | #7, #107 | #104 | `#7` O Chile reduziu a jornada máxima semanal de 45 para 42 horas em 2026... A jornada máxima semanal na Colômbia foi reduzida de 44 para 42 horas em julho de 2026.… |
| [[20]](https://autonomy.work/wp-content/uploads/2021/06/ICELAND_4DW.pdf) | #10, #46–47 | — | — | `#10` Reductions in working time were not accompanied by reductions in pay. ... The trials evolved to include nine-to-five workers alongside those on non-standard sh… |
| [[22]](https://4dayweek.io/country/belgium) | — | #11, #94–95 | — | `#11` Under the law of 3 October 2022, the daily limit can rise to 9.5 hours for a full-time employee who works four days a week. [...] The standard week is 38 hours… |
| [[24]](https://www.bc.edu/bc-web/sites/bc-magazine/fall-2022-issue/linden-lane/a-four-day-work-week-.html) | #35 | #12, #32 | — | `#35` Workers can also communicate in more efficient ways, perhaps shifting from phone calls to using Slack and other messaging apps. Finally, employees move doctor'… |
| [[35]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693da184212d4f030b2a8032/1765646724493/US+Ireland+Results+2023.pdf) | #52 | #29, #51 | — | `#52` In this report we present research results from the first two trials, which comprised 33 companies and 903 employees in the US, Ireland, and a few other countr… |
| [[65]](https://www.researchgate.net/publication/361430073_Effects_of_4-Day_School_Weeks_on_Older_Adolescents_Examining_Impacts_of_the_Schedule_on_Academic_Achievement_Attendance_and_Behavior_in_High_School) | — | — | #89, #91–92 | — |
| [[71]](https://www.safetyandhealthmagazine.com/bernie-sanders-and-mark-takano-renew-push-for-a-32-hour-workweek/) | — | #99–101 | — | `#99` At a time when artificial intelligence and robotics will radically transform our economy |
| [[1]](https://pubmed.ncbi.nlm.nih.gov/40691306/) | — | #0, #58 | — | `#0` Analysis of pre- and post-trial data from 2,896 employees across 141 organizations in Australia, Canada, Ireland, New Zealand, the UK and the USA shows improve… |
| [[14]](https://www.humanresourcesonline.net/tokyo-to-introduce-a-four-day-workweek-and-flexible-working-hours-for-government-staff-from-april-2025) | — | #7, #105 | — | `#7` Tokyo's governor Yuriko Koike has announced a plan to implement a four-day workweek and flexible working hours for metropolitan government employees from April… |
| [[16]](https://www12.senado.leg.br/noticias/audios/2026/10/congresso-promulga-emendas-sobre-fim-da-escala-6x1-e-agentes-de-saude) | — | #7, #107 | — | `#7` As propostas de emenda à Constituição que tratam da aposentadoria especial dos agentes comunitários de saúde (PEC 14/2021) e do fim da escala seis por um (PEC… |
| [[18]](https://openpaper.dev/examples/four-day-work-week-outcomes) | #13 | #8 | — | `#13` A 'four-day work week' can mean fewer paid hours at unchanged pay, forty hours compressed into four long shifts, or a partial reduction spread across the week.… |
| [[19]](https://www.unisc.edu.au/about/unisc-news/news-archive/2025/november/why-the-four-day-workweek-is-more-than-just-a-fad-boosting-wellbeing-productivity-and-the-future-of-work) | #9 | #78 | — | `#9` The most common approach is the 100-80-100 model: employees work 80 percent of the traditional hours but receive 100 percent of their salary and are expected t… |
| [[23]](https://4dayweek.io/country/japan) | — | #11, #105 | — | `#11` In December 2024 Tokyo's governor announced a four-day option for metropolitan staff, built on the flextime system. |
| [[37]](https://greenamerica.org/evolution-work/can-4-day-work-week-heal-people-and-planet) | #38 | — | #37 | `#38` This UK study, which both Lockhart and Fan worked on, ran for six months in 2022 involving 57 companies and 2,548 employees. Across the board, the study's resu… |
| [[39]](https://www.theguardian.com/money/2019/feb/19/four-day-week-trial-study-finds-lower-stress-but-no-cut-in-output) | #42 | #41 | — | `#42` claiming it has resulted in a 20% rise in productivity, appeared to have helped increase profits and improved staff wellbeing. [...] Staff stress levels were d… |
| [[51]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693e8a0d0669596b183b27fa/1765706253519/Brazil+4+Day+Week+Pilot+2024.pdf) | #68 | — | #63 | `#68` In Brazil, 21 companies participated in the 4 day week pilot... One company located in Rio Grande do Sul was affected by the flood tragedy and withdrew from th… |
| [[53]](https://www.localgov.co.uk/Four-day-week-trial-success-says-council/62636) | #71 | #72 | — | `#71` Carried out by the Universities of Salford, Bradford and Cambridge, the analysis revealed that 21 of 24 services have improved or stayed the same since the fou… |
| [[55]](https://www.gov.scot/policies/public-sector-pay/four-day-working-week/) | — | #69, #73 | — | `#69` We committed to running a four day working week pilot in the public sector. |
| [[58]](https://www.theguardian.com/uk-news/2019/apr/12/wellcome-trust-drops-plans-to-trial-four-day-working-week) | — | #74–75 | — | `#74` organisations with workers carrying out a wide range of functions – it employs exhibition curators as well as fund managers – could find it harder to switch th… |
| [[59]](https://www.unilever.com/news/news-search/2022/fourday-work-week-trial-to-start-in-australia/) | — | #77 | #76 | `#77` Following an 18-month pilot in New Zealand, we are extending our four-day work week trial to our Australian business. |
| [[66]](https://www.acerta.be/en/inspiration/four-day-working-week-eight-out-of-ten-smes-not-behind-the-idea) | — | #94–95 | — | `#94` the labour deal will allow employees to request this from their employer |
| [[69]](https://4dayweek.io/region/valencia) | — | #98, #110 | — | `#98` In total, **360K** people took part in a 4-day work week experiment. Stress Reduction: Participants reported a 35% decrease in stress levels. Improved Sleep: 6… |
| [[72]](https://www.rockymountainemployersblog.com/blog/2026/10/1/a-new-bill-in-congress-proposes-a-shift-to-a-thirty-two-hour-workweek-without-reducing-salaries) | — | #100–101 | — | `#100` On September 8, 2026, Representative Mark Takano (D-California) and Senator Bernie Sanders (I-Vermont) introduced to Congress the “Thirty-Two-Hour Work Week Ac… |
| [[76]](https://worldatwork.org/publications/workspan-daily/pennsylvania-law-would-incentivize-four-day-workweek) | #103 | #102 | — | `#103` More than 90 businesses throughout the U.S. have a four-day, 32-hour workweek. Thousands of U.S. organizations have a compressed workweek, where some or all em… |
| [[80]](https://www.welcometothejungle.com/en/articles/how-the-4-day-workweek-can-help-to-reduce-carbon-emissions) | #108 | #112 | — | `#108` Encouragingly, some real-life studies of shortened or compressed workweeks have shown positive environmental outcomes, though these findings sometimes fall sho… |
| [[27]](https://agenciabrasil.ebc.com.br/politica/noticia/2026-05/ha-100-anos-ford-instituia-jornada-de-40-horas-nos-estados-unidos) | — | #17 | — | `#17` A decisão do empresário da Ford, Henry Ford, foi apresentada, na época, como uma forma de atrair profissionais de outras indústrias, onde a escala era muito ma… |
| [[28]](https://teachingamericanhistory.org/document/henry-fords-five-day-week/) | — | #18 | — | `#18` They will receive wages for five days instead of six days. Their earning capacity has been reduced one-sixth. |
| [[34]](https://kommerstad.org/journal/article/download/943/696) | — | #29 | — | `#29` systematic reviews have established that working more than forty hours per week is associated with increased risk of burnout symptoms, including emotional exha… |
| [[38]](https://ideas.repec.org/a/nat/nathum/v9y2025i10d10.1038_s41562-025-02259-6.html) | — | — | #39 | — |
| [[41]](https://buffer.com/resources/4-day-workweek-2021/) | #44 | — | — | `#44` Starting in May of 2020, I measured the following: ... Reported stress dipped down to 2.7 at our June survey, and then only slightly up to 2.9 at our October s… |
| [[42]](https://workfour.org/case-studies/blog-post-title-four-5l997) | #45 | — | — | `#45` Since launching it in 2021, the most profound impact of our 4-day week has been on employee retention. Relatedly, employee engagement is up by 50%. While we we… |
| [[45]](https://www.europeanbusinessreview.eu/page.asp?pid=6985) | — | #54 | — | `#54` the time spent by male workers looking after their children increasing by 27% |
| [[46]](https://www.theemploymentlawsolicitors.co.uk/news/blog/four-day-working-week-3/) | — | #56 | — | `#56` a second four day working week pilot began on the 4th November 2024, with 1000 workers from 17 businesses taking part. ... All 17 companies in the four day wee… |
| [[47]](https://4dayweek.io/country/australia) | — | #56 | — | `#56` 26 companies (10 in Australia, 9 in New Zealand, 4 in Europe, 3 in the US and Canada) ran a six-month pilot that got underway in August 2022, keeping pay at 10… |
| [[54]](https://www.theguardian.com/society/2025/oct/29/councils-clampdown-four-day-working-weeks-south-cambridgeshire) | — | #72 | — | `#72` The local government secretary, Steve Reed, is seeking to clamp down on councils introducing four-day working weeks after writing to South Cambridgeshire warni… |
| [[56]](https://autonomy.work/portfolio/sww-scotland-public-sector/) | #73 | — | — | `#73` Average scores in the area of 'satisfaction with time' increased by 46.8% [...] The percentage of staff feeling 'very satisfied' with their work-life balance r… |
| [[57]](https://www.theguardian.com/business/2025/aug/27/scottish-government-trial-of-four-day-week-improves-productivity-and-staff-wellbeing) | — | #73 | — | `#73` it has stopped short of rolling out a four-day week more widely. [...] The Scottish government said it would use the findings to inform its wider public servic… |
| [[60]](https://www.uts.edu.au/news/2022/11/uts-research-reveals-success-unilever-four-day-work-week) | — | #77 | — | `#77` the trial will continue in New Zealand to garner more insights. |
| [[61]](https://www.theguardian.com/australia-news/2022/nov/02/australian-workers-at-global-company-to-trial-four-day-week-after-success-of-new-zealand-pilot) | — | #77 | — | `#77` British multinational Unilever will expand its trial of a four-day work week to staff in Australia after a successful 18-month pilot in New Zealand. |
| [[63]](https://www.ncbi.nlm.nih.gov/books/NBK75539/) | #85 | — | — | `#85` Forty observational studies (n>3,014; sample size not reported for one study) were included in the review: five prospective cohort studies with control groups |
| [[67]](https://4dayweek.io/country/france) | #96 | — | — | `#96` France's legal working week for full-time private-sector employees is 35 hours [...] A union study of 18 local authorities reached the same conclusion: the fou… |
| [[68]](https://www.4dayjob.com/blog/countries-with-4-day-work-week) | — | #97 | — | `#97` Government funding: €50 million allocated |
| [[70]](https://www.healthplanspain.com/blog/health-news/2062-valencian-pilot-scheme-shows-4-day-work-week-improved-workers-health.html) | — | #98 | — | `#98` retailers reported a decrease in sales. Additionally, emergency medical services faced potential strain as more healthcare workers took time off. smokers and d… |
| [[73]](https://www.pbs.org/newshour/politics/what-to-know-about-bernie-sanderss-bill-for-the-u-s-to-adopt-a-32-hour-workweek) | — | #101 | — | `#101` GOP Sen. Bill Cassidy of Louisiana said paying workers the same wages for fewer hours would force employers to pass the cost of hiring more workers along to co… |
| [[74]](https://workfour.org/policy-developments) | — | #102 | — | `#102` In California in 2022, __Rep. Evan Low__ introduced AB-2392, a directive 4-day workweek bill. After intense opposition from CA businesses and Chamber of Commer… |
| [[75]](https://www.govdocs.com/maryland-4-day-workweek-bill/) | — | #102 | — | `#102` Participating businesses would be eligible for up to $750,000 in tax credits for each fiscal year. |
| [[77]](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/noticias/2026/10/senado-aprova-fim-da-escala-6x1-pauta-prioritaria-do-governo-federal) | — | #107 | — | `#107` O Chile aprovou a redução gradual da jornada de 45 para 40 horas semanais até 2029, enquanto a Colômbia está em transição de 48 para 42 horas até 2026. [...] A… |
| [[78]](https://www.4dayweek.com/news-posts/environmental-benefits-2hxgl) | — | #109 | — | `#109` A study spanning from 1970 to 2007 looked at 24 countries and discovered that if work hours were reduced by 10 percent, there could be drops in ecological foot… |
| [[79]](https://4dayweek.io/pro/environment) | — | #109 | — | `#109` According to a 2021 report by Stop The Clock, adopting a 4-day workweek could lead to a remarkable reduction of up to 21.3% in the UK's carbon footprint. The r… |
| [[81]](https://www.researchgate.net/publication/375365733_The_social_economic_and_environmental_impacts_of_a_4-day_workweek_in_an_organization) | — | — | #112 | — |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.researchgate.net/publication/390052868_Four-Day_Week_Results_from_Portuguese_Trial_Final_Report — download excedeu 90s

### Bloqueadas por barreira de acesso

- https://www.help.senate.gov/download/dr-schor-help-testimony-3-14-24pdf — http_error — barreira de acesso (http_error): # Access Denied You don't have permission to access "http://www.help.senate.gov/$(SERVE_403)/download/dr-schor-help-test
- https://www.krem.com/article/news/nation-world/32-hour-workweek-bill-introduced-congress/507-60ff6b6f-69f7-4807-95f6-a9ba2cbe87bc — http_error — barreira de acesso (http_error): # Access Denied You don't have permission to access "http://www.krem.com/article/news/nation-world/32-hour-workweek-bill
- https://scispace.com/papers/the-productivity-of-working-hours-1w39cbiq4q — anti_bot — barreira de acesso (anti_bot): Complete the security check before continuing. This step verifies that you are not a bot, which helps to protect your ac
- https://www.econstor.eu/bitstream/10419/145237/1/dp10103.pdf — anti_bot — barreira de acesso (anti_bot): # **Making sure you're not a bot!** [image] [image] Loading... You are seeing this because EconStor has set up <a href="
- https://policycommons.net/artifacts/13373666/portugal20420day20week20pilot20results20-20420day20week20global/14271453/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-0`** [1] [2] [3]
  - Trecho: Across corporate, municipal, and multi-country trials conducted since 2018, shortening the workweek without reducing pay has consistently been associated with lower burnout, better sleep, reduced fatigue, and stronger t…
  - Justificativa: A evidência sustenta os elementos essenciais da afirmação: ensaios corporativos (UK 2022, Microsoft Japan 2019), municipais (Islândia, setor público) e multipaíses (Fan et al., 6 países) com redução de jornada sem corte…
  - Suporte veio de: [1] [3]
  - Evidência: “Analysis of pre- and post-trial data from 2,896 employees across 141 organizations in Australia, Canada, Ireland, New Zealand, the UK and the USA shows improvements in burnout, job satisfaction, mental health and physic…”
  - Não coberto pela evidência: A delimitação temporal 'since 2018' não é explicitada na evidência; o ensaio islandês começou em 2015 (embora tenha se estendido a 2019).; A afirmação de 'maintaining organizational output' é qualificada na evidência: output não foi medido na maioria dos ensaios e dados de receita vieram de apenas 23 de 61 firmas no piloto UK.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | Analysis of pre- and post-trial data from 2,896 employees across 141 organizations in Australia, Canada, Ireland, New Z… |
    | [3] | sustenta | For well-being in volunteer, mostly white-collar firms: yes, consistently. Burnout drops, sleep improves, fatigue falls… |

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-3`** [3] [6] [7]
  - Trecho: Even in reduced-hour pilots, documented gains are tempered by volunteer selection bias, incomplete financial reporting, staffing expenses in continuous-coverage services, and potential carbon rebound effects.
  - Justificativa: A evidência sustenta cada elemento da afirmação: viés de seleção de voluntários (firmas auto-selecionadas via organização de advocacy, sem randomização), relatórios financeiros incompletos (dados de receita de apenas 23…
  - Suporte veio de: [3] [7] [6]
  - Evidência: “Every firm entered voluntarily through an advocacy organization. The 92% continuation figure tells you something about these specific firms, not about all firms.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | sustenta | Every firm entered voluntarily through an advocacy organization... Revenue rose 1.4% on average, but only 23 of 61 orga… |
    | [7] | sustenta | My results revealed that switching to a four-day week with no loss of pay would only reduce emissions if people dedicat… |
    | [6] | sustenta | To ensure that patients at the home for the elderly were attended to for the same number of hours as before, 15 new emp… |

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-4`** [8] [9] [10]
  - Trecho: By late 2026, international experience reflects sharp institutional divergence rather than uniform convergence toward a 32-hour week.
  - Justificativa: A evidência mostra resultados divergentes entre países: Alemanha com 20% de desistência e adaptações híbridas, Reino Unido com 92% de adoção permanente, Islândia com transição gradual, Bélgica com compressão (não reduçã…
  - Suporte veio de: [9] [8] [10]
  - Evidência: “The British pilot project (61 companies, 2,900 employees, 2022-2023) provides the most robust data to date. The results are significantly more positive than the German ones: 92 percent of companies permanently adopted t…”
  - Não coberto pela evidência: O termo exato 'late 2026' não aparece literalmente; os dados mais recentes são de fevereiro e outubro de 2026.; A expressão 'sharp institutional divergence' é uma interpretação não usada literalmente na evidência, embora o conceito seja sustentado.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [9] | parcial | The British pilot project (61 companies, 2,900 employees, 2022-2023) provides the most robust data to date. The results… |
    | [8] | parcial | Chancellor Friedrich Merz said in May 2025 that with a four-day week and work-life balance Germany would not keep its p… |
    | [10] | parcial | Last year Bupa and Unilever walked away from trials of reduced work hours, citing the four-day model as 'rigid'. ... in… |

### UNSUPPORTED

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-6`** [10] [11] [12] [13]
  - Trecho: Conversely, major corporations including Unilever and Bupa exited shortened-week trials in Australia in 2025, statutory compressed-week uptake in Belgium stalled below 1% of private-sector workers, and bills to lower st…
  - Justificativa: A evidencia sustenta parcialmente a afirmacao. A saida da Unilever e da Bupa de testes na Australia e confirmada, mas a evidencia diz "Last year" sem especificar 2025; o periodo exato e ambiguo. A taxa de adesao na Belg…
  - Suporte veio de: [11] [10] [12]
  - Evidência: “Last year Bupa and Unilever walked away from trials of reduced work hours, citing the four-day model as "rigid".”
  - Não coberto pela evidência: "exited shortened-week trials in Australia in 2025" — a evidencia diz "Last year" sem especificar o ano 2025; "remain deadlocked in the United States Congress" — a evidencia apenas indica reintroducao e encaminhamento a comissao, sem caracterizar como "deadlocked"
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [10] | parcial | Last year Bupa and Unilever walked away from trials of reduced work hours, citing the four-day model as “rigid”. |
    | [11] | parcial | 0.8% of Belgian private-sector employees used Belgium's full-time four-day regime as of March 31, 2025 |
    | [12] | parcial | Congress rejected it on 10 September 2025, by 178 votes to 170 |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-8`** [3] [18]
  - Trecho: Public debate frequently conflates four distinct scheduling designs under the four-day workweek label.
  - Justificativa: A evidência sustenta a ideia geral de que diferentes arranjos de horários são rotulados como 'semana de quatro dias', mas não afirma explicitamente que existem 'quatro designs distintos' nem que o 'debate público freque…
  - Suporte veio de: [18] [3]
  - Evidência: “A “four-day work week” can mean fewer paid hours at unchanged pay, forty hours compressed into four long shifts, or a partial reduction spread across the week.”
  - Não coberto pela evidência: O número exato de 'quatro' designs distintos não é explicitamente enumerado na evidência; A expressão 'public debate frequently conflates' não aparece; a evidência fala em 'advocacy, law and organizational experiments' usando o mesmo rótulo, mas não caracteriza isso como 'debate público frequentemente'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | The phrase "4 day work week" describes two structurally different schedules. |
    | [18] | parcial | A “four-day work week” can mean fewer paid hours at unchanged pay, forty hours compressed into four long shifts, or a p… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-28`** [32] [33]
  - Trecho: Subsequent research by Pencavel showed that insufficient recovery between consecutive weeks depresses productivity and formalized the distinction between nominal time at work and effective productive effort.
  - Justificativa: A evidência não menciona Pencavel em nenhum momento, nem aborda recuperação insuficiente entre semanas consecutivas ou a distinção entre tempo nominal de trabalho e esforço produtivo efetivo. Embora a evidência trate de…
  - Não coberto pela evidência: Menção a Pencavel como autor de pesquisa subsequente; Insuficiente recuperação entre semanas consecutivas deprime a produtividade; Formalização da distinção entre tempo nominal de trabalho e esforço produtivo efetivo
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [33] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-31`** [33]
  - Trecho: In Diminishing Returns at Work (2018), he noted that trimming hours from a baseline near 35 hours per week generally requires larger offsetting hiring increases to preserve output than cutting from an exhausting 60-hour…
  - Justificativa: A evidência afirma que reduções de horas em contextos de muitas horas (high-hour contexts) exigem aumentos proporcionais maiores de emprego em comparação com contextos de poucas horas (low-hour settings). O trecho do cl…
  - Suporte veio de: [33]
  - Evidência: “reductions in working hours often require proportionally larger increases in employment in high-hour contexts compared to low-hour settings to achieve the same output”
  - Não coberto pela evidência: Título da obra 'Diminishing Returns at Work (2018)'; Ano de publicação 2018; Baseline específico de 35 horas por semana
- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-66`** [8] [9] [36]
  - Trecho: Continuation stood at 73% post-trial (20% reverted, 7% undecided) and 70% at the February 2026 two-year follow-up (20% exited, 10% undecided), with 22% modifying the strict four-day format into 4.5-day weeks, flexible F…
  - Justificativa: A evidência contradiz explicitamente os números pós-teste do trecho: as fontes afirmam 70% de continuação (não 73%) e 10% indecisos (não 7%). As demais partes são sustentadas: 70% no follow-up de fevereiro de 2026, 20%…
  - Suporte veio de: [9] [8]
  - Evidência: “The reality: 70 percent continue, 20 percent return to the 5-day week, and 10 percent are still undecided.”
  - Não coberto pela evidência: A cifra de 73% de continuação pós-teste (a evidência afirma 70%); Os 7% de indecisos pós-teste (a evidência afirma 10%); Os 10% de indecisos no follow-up de fevereiro de 2026 (a evidência apenas diz que 30% não operavam tempo reduzido, sem detalhar indecisos)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [9] | contradiz | The reality: 70 percent continue, 20 percent return to the 5-day week, and 10 percent are still undecided. ... The 2-ye… |
    | [8] | parcial | A follow-up report found that in February 2026, 70% of the 40 responding organisations still operated some form of redu… |
    | [36] | ausente | — |

- **Trecho citado `semana_trabalho_ea8709888325_20261117T015346Z-67`** [11] [49] [50]
  - Trecho: In Portugal's state-backed pilot of 41 companies, average weekly hours fell 12% from over 41 to 36.5 hours, work-family difficulty dropped from 46% to 17%, "very good" or "excellent" mental health doubled from 15% to 30…
  - Justificativa: A evidência contradiz explicitamente a afirmacao sobre a queda de horas: o claim diz 12%, de 'mais de 41' para 36.5, mas a evidencia diz 13.7%, de 39.3 para 34. Varios outros elementos do claim nao aparecem na evidencia…
  - Evidência: “41 companies and more than 1,000 workers took part in Portugal's government-backed pilot in 2023, cutting reported weekly hours 13.7%, from 39.3 to 34”
  - Não coberto pela evidência: average weekly hours fell 12%; from over 41 to 36.5 hours; work-family difficulty dropped from 46% to 17%
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [11] | contradiz | cutting reported weekly hours 13.7%, from 39.3 to 34 |

  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A afirmacao e composta por varios dados especificos. A evidencia confirma 41 empresas, valor de 28% do salario e 4 empresas que voltaram a…") — cascata: baseline → context_expansion

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semana_trabalho_ea8709888325_20261117T015346Z-26` — Referencia(s) citada(s) ['17c3f556ec5ec165'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_ea8709888325_20261117T015346Z-27` — Referencia(s) citada(s) ['17c3f556ec5ec165'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_ea8709888325_20261117T015346Z-53` — Referencia(s) citada(s) ['d4ddca1ad6c6b0d5'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.