# Relatório de Auditoria — Claude (semana_trabalho_d029e3aa4d63_20261115T034149Z)

**Arquivo auditado:** `answers/Ingles/Claude/EmConsolidacao/semana_trabalho.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_d029e3aa4d63_20261115T034149Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T03:59:32.480995+00:00 |
| **Total de trechos citados** | 79 |
| **Tempo de processamento** | 0:00:17:43 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 29.0 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 80 marcadores, 51 distintos |
| Referências listadas | 51 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 47 | 59.5% |
| **UNSUPPORTED** | 26 | 32.9% |
| **CONTRADICTED** | 1 | 1.3% |
| **SKIPPED** | 5 | 6.3% |
| **TOTAL** | 79 | 100.0% |

Sobre os 74 trechos citados auditados: SUPPORTED 63,51%, UNSUPPORTED 35,13%, CONTRADICTED 1,35%.

> **16 dos 47 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 16 estão **contados dentro** dos 47 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`28` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `4` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `10` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 1, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#1` The business claims that dominate headlines, such as rising revenue and steep drops in sick days and resignations, come… | [2] | [1] [20] [3] [40] [12] [15] [17] [41] [14] [48] [23] [5] | — |
| `#9` The five-day week is itself a 20th-century invention: Ford adopted it in 1926, and the Fair Labor Standards Act of 1938… | [9] | [22] [35] [43] [1] [6] [49] [48] [50] [5] [23] [15] [20] [7] [2] [13] [4] [31] | — |
| `#13` It launched with 70 companies and 3,300 workers, so some participants dropped out or were reclassified before the final… | [13] | [2] [1] [15] [48] [14] [6] [5] [17] [3] [19] [40] [12] | — |
| `#21` Microsoft Japan's "Work Life Choice Challenge" closed its offices on Fridays for one month in 2019, and sales per emplo… | [18] | [48] [1] [36] [6] [20] [8] [49] [2] [15] [12] [21] [31] [14] [7] [30] [5] [3] | — |
| `#53` Even so, the public finance minister said in August 2025 that the government "will not be moving to a 32-hour week." Po… | [41] | [43] [49] [51] [13] [42] [40] [20] [50] [8] [7] [29] [14] [17] [2] [5] | — |
| `#67` Bolt made its policy permanent in 2022 after 94% of workers wanted it to continue, a self-reported figure from a tech f… | [49] | [14] [6] [12] [17] [48] [15] [20] [31] [2] [40] [18] [1] [47] | — |
| `#68` Lamborghini's December 2023 union deal gave production workers 22 to 31 extra days off a year with no pay cut, alongsid… | [50] | [14] [29] [13] [32] [48] [6] [44] [2] [31] [20] [17] [12] [25] [15] | — |
| `#69` The economist Daniel Hamermesh said the 4DWG survey "merely demonstrates that people are willing to participate in the… | [2] | [20] [5] [1] [6] [18] [8] [19] [15] [30] [7] [16] [49] [29] | — |
| `#74` Scottish agency SOSE's three-day response rate slipped from 94% to 92%. | [40] | [41] [12] [6] [38] [14] [1] [2] [17] [15] [3] [16] [23] | — |
| `#77` Adoption is creeping rather than surging: more than 200 UK employers, covering about 5,000 staff, had permanently adopt… | [17] | [48] [23] [14] [49] [21] [12] [22] [1] [6] [7] [20] [2] [39] [5] [8] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 617882 |
| **Média de tokens por requisição** | 8349.8 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/51 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 4.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.psypost.org/large-scale-trial-finds-four-day-workweek-improves-employee-well-being-and-physical-health/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[3]](https://www.uni-muenster.de/news/view.php?cmdid=14338) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[4]](https://movimentoeconomico.com.br/trabalho/2026/10/16/congresso-promulga-emenda-do-fim-da-6x1-e-escala-5x2-comeca-em-60-dias/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[5]](https://fortune.com/europe/2024/07/08/asda-scrapping-physically-exhausting-4-day-workweek-why-it-can-fail/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[6]](https://www.henley.ac.uk/news/2024/results-from-portugals-government-backed-4-day-week-trial-released) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[8]](https://abc7news.com/iceland-work-week-shorter-cuccess/10871439/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[11]](https://www.lrt.lt/en/news-in-english/19/2681358/lithuania-debates-four-day-workweek-as-prime-minister-backs-shorter-schedules) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[13]](https://4dayweek.com/press-releases) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[20]](https://shrm.org/topics-tools/news/employee-relations/4-day-workweek-continues-to-gain-interest) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[2]](https://techtarget.com/searchhrsoftware/news/252525395/Four-day-workweek-productivity-claims-gather-criticism) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[7]](https://4dayweek.com/germany-2024-pilot-results) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[10]](https://www.help.senate.gov/dem/newsroom/press/news-sanders-introduces-legislation-to-enact-a-32-hour-workweek-with-no-loss-in-pay) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[12]](https://www.4dayweek.co.uk/pilot-results) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://www.shrm.org/topics-tools/news/report-us-ireland-four-day-workweek-pilot-huge-success) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[17]](https://leftfootforward.org/2025/08/latest-four-day-working-week-trial-delivers-100-success-rate/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://www.koreatimes.co.kr/southkorea/politics/20250919/govt-seeks-passage-of-45-day-workweek-bill-this-year-despite-industry-pushback) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[38]](https://civilserviceworld.com/news/article/ministers-drop-hostilities-against-fourdayweek-council) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[40]](https://autonomy.work/2025/08/27/introducing-a-shorter-working-week-in-scotlands-public-sector/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[9]](https://history.com/articles/five-day-work-week-labor-movement) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[14]](https://autonomy.work/2024/02/21/make-it-stick/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[16]](https://www.4dayweek.com/sa-2023-pilot-results) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[18]](https://www.cnbc.com/2019/11/04/microsoft-japan-4-day-work-week-experiment-sees-productivity-jump-40percent.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[19]](https://www.euronews.com/next/2023/10/31/workers-in-valencias-4-day-week-trial-report-less-stress-and-more-socialising) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.theregister.com/2025/07/22/4_day_week_study/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[22]](https://www.the74million.org/article/students-in-4-day-a-week-schools-can-suffer-covid-level-learning-losses/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://journalistsresource.org/education/four-day-school-week-research/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[24]](https://en.alda.is/2021/07/04/going-public-icelands-journey-to-a-shorter-working-week/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://brusselstimes.com/804328/four-get-about-it-few-belgians-opt-for-shorter-work-week) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://gulfnews.com/living-in-uae/ask-us/will-dubai-bring-back-its-four-day-summer-work-week-in-2026-1.500567705) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[27]](https://gulfnews.com/uae/government/sharjahs-new-four-day-work-week-improved-government-performance-reduced-accidents-by-40-study-finds-1.89814620) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.tokyoweekender.com/japan-life/news-and-opinion/four-day-workweek-for-tokyo-government-workers/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[30]](https://www.semafor.com/article/01/19/2026/south-korean-banks-shorten-workweek) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[31]](https://www.seoulz.com/korea-4-5-day-workweek-2026/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[32]](https://advisory.ecija.com/en/reduccion-jornada-laboral-consulta-publica/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://remoteworkeurope.eu/news/2026/spain-working-hours-bill-stalled) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[34]](https://www.que.es/2026/07/17/nuevo-registro-horario-julio-2026/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[35]](https://www.wtoc.com/2026/09/14/bill-introduced-reduce-workweek-32-hours/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[36]](https://www.foxla.com/news/california-bill-mandating-4-day-work-week-stalled) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://www.fastcompany.com/90842153/will-maryland-be-the-first-state-to-adopt-a-four-day-workweek) | error | 1 | 0 | 0 | 0 | 1 |
| [[39]](https://cambridge.gov.uk/news/2025/07/17/south-cambridgeshire-district-council-votes-to-permanently-adopt-four-day-week) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.civilserviceworld.com/news/article/scottish-government-four-day-week-pilot-assessment-productivity-wellbeing-benefits) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[42]](https://kadry.infor.pl/kodeks-pracy/czas-pracy/7369974,resort-pracy-90-pracodawcow-i-ponad-5-tys-pracownikow-z-branzy-odziezowej-z-wodociagow-oraz-filharmonii-wezmie-udzial-w-pilotazu-skroconego-czasu-pracy-srednie-dofinansowanie-dla-jednego-podmiotu-wyniesie-05-mln-zl.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[43]](https://wydarzenia.interia.pl/kraj/news-pracuja-mniej-za-te-same-pieniadze-pierwsze-wnioski-testu-da,nId,23474291) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[44]](https://movimentoeconomico.com.br/trabalho/2026/10/14/senado-aprova-fim-da-escala-6x1-e-reducao-da-jornada-de-trabalho/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/germany-prepares-shift-to-weekly-working-time-limits) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[46]](https://tech.co/?p=360477) | dead | 1 | 0 | 0 | 0 | 1 |
| [[47]](https://thenewstack.io/kpmgs-ceo-poll-labor-markets-4-day-workweeks-and-genai/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://emexmag.com/four-day-work-week-who-has-stuck-with-it-and-who-reverted/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[49]](https://www.cnbc.com/2022/01/05/the-4-day-workweek-becomes-permanent-for-tech-company-bolt.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://fortune.com/europe/2023/12/07/lamborghini-four-day-workweek-italy-germany-volkswagen-unions-uaw/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[51]](https://www.gbnews.com/money/stealth-tax-on-jobs-flexible-working-report) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.psypost.org/large-scale-trial-finds-four-day-workweek-improves-employee-well-being-and-physical-health/) | #0, #4, #25, #71 | #26 | — | `#0` The researchers collected data from 2,896 employees. ... 141 organizations ... 12 control companies ... significant reductions in burnout, along with notable i… |
| [[3]](https://www.uni-muenster.de/news/view.php?cmdid=14338) | #27, #75 | #2 | — | `#27` the Berlin-based consultancy Intraprenör organised the first large-scale pilot study on the four-day week in Germany. The research involved three waves of data… |
| [[4]](https://movimentoeconomico.com.br/trabalho/2026/10/16/congresso-promulga-emenda-do-fim-da-6x1-e-escala-5x2-comeca-em-60-dias/) | #57 | #3, #78 | — | `#57` A Emenda Constitucional permite ainda, excepcionalmente, e mediante convenção ou acordo coletivo de trabalho, que seja estabelecido regime compensatório que pe… |
| [[5]](https://fortune.com/europe/2024/07/08/asda-scrapping-physically-exhausting-4-day-workweek-why-it-can-fail/) | #5, #65 | #59 | — | `#5` The most successful trials tend to see employees shorten their hours for the same pay, as with South Cambridgeshire Council. [...] However, the latest results… |
| [[6]](https://www.henley.ac.uk/news/2024/results-from-portugals-government-backed-4-day-week-trial-released) | #6, #19, #29 | — | — | `#6` In 51% of companies, workers had one day off per week, while 49% of companies opted for a nine-day fortnight. |
| [[8]](https://abc7news.com/iceland-work-week-shorter-cuccess/10871439/) | #8, #32, #34 | — | — | `#8` Public sector employees taking part in two large trials between 2015 and 2019 worked 35-36 hours per week, with no reduction in pay. Many participants had prev… |
| [[11]](https://www.lrt.lt/en/news-in-english/19/2681358/lithuania-debates-four-day-workweek-as-prime-minister-backs-shorter-schedules) | #11, #36 | #60 | — | `#11` experts warn the country must first boost productivity, efficiency and global competitiveness before moving to a four-day model |
| [[13]](https://4dayweek.com/press-releases) | #17 | #13, #76 | — | `#17` results from a study of 41 US and Canadian companies who trialled a 4 day week for six months found that none were planning to return to five days. |
| [[20]](https://shrm.org/topics-tools/news/employee-relations/4-day-workweek-continues-to-gain-interest) | #23, #61, #64 | — | — | `#23` All but five of 61 companies that took part in a four-day working week trial in the U.K. say they will continue with the policy, according to study results rel… |
| [[2]](https://techtarget.com/searchhrsoftware/news/252525395/Four-day-workweek-productivity-claims-gather-criticism) | — | #1, #69 | — | `#1` "Juliet Schor, professor of sociology at Boston College and lead researcher of 4 Day Week Global" |
| [[7]](https://4dayweek.com/germany-2024-pilot-results) | #7, #28 | — | — | `#7` Many organizations implemented more conservative or adapted versions of work time reduction rather than the classic 100:80:100™ model, and in nearly 40% of cas… |
| [[12]](https://www.4dayweek.co.uk/pilot-results) | #12, #14 | — | — | `#12` The results of the world's biggest ever four-day working week pilot which took place in the UK were revealed in February 2023 |
| [[15]](https://www.shrm.org/topics-tools/news/report-us-ireland-four-day-workweek-pilot-huge-success) | #16, #72 | — | — | `#16` 52 percent of employees thought their pace of work increased; 42 percent thought it was the same. ... 67 percent of employees reported lower levels of burnout;… |
| [[17]](https://leftfootforward.org/2025/08/latest-four-day-working-week-trial-delivers-100-success-rate/) | #20 | #77 | — | `#20` The scheme was organised by the 4 Day Week Foundation. |
| [[29]](https://www.koreatimes.co.kr/southkorea/politics/20250919/govt-seeks-passage-of-45-day-workweek-bill-this-year-despite-industry-pushback) | #40 | #78 | — | `#40` The Korea Employers Federation said that Korea's hourly labor productivity was $54.60 in 2023, which is only 77.4 percent of the OECD average and significantly… |
| [[38]](https://civilserviceworld.com/news/article/ministers-drop-hostilities-against-fourdayweek-council) | #50, #73 | — | — | `#50` Although it is not government policy to support a general move to a four-day working week for five days' worth of pay |
| [[40]](https://autonomy.work/2025/08/27/introducing-a-shorter-working-week-in-scotlands-public-sector/) | #52 | — | #74 | `#52` two organisations made the decision to take part in a year-long pilot of a 32-hour working week. The organisations were Accountant in Bankruptcy (AiB) and Sout… |
| [[9]](https://history.com/articles/five-day-work-week-labor-movement) | — | — | #9 | — |
| [[14]](https://autonomy.work/2024/02/21/make-it-stick/) | — | — | #15 ⚡ | `#15` Job satisfaction and sleep problems nudged down a bit, but the bulk of the original improvement remains. |
| [[16]](https://www.4dayweek.com/sa-2023-pilot-results) | #18 | — | — | `#18` 57% decrease in employee burnout; 10.5% average increase in revenue; 92% of companies will be continuing; The first South African 4 day week trial took place f… |
| [[18]](https://www.cnbc.com/2019/11/04/microsoft-japan-4-day-work-week-experiment-sees-productivity-jump-40percent.html) | — | #21 | — | `#21` Microsoft's "Work Life Choice Challenge," held this August, saw the firm close its doors on Fridays and give its 2,300 employees three-day weekends for the ful… |
| [[19]](https://www.euronews.com/next/2023/10/31/workers-in-valencias-4-day-week-trial-report-less-stress-and-more-socialising) | #22 | — | — | `#22` this one was just a month long ... 360,000 workers living in Valencia taking part ... those taking part reported a 35 per cent reduction in stress levels ... a… |
| [[21]](https://www.theregister.com/2025/07/22/4_day_week_study/) | — | #24 | — | `#24` The research, led by Boston College associate professor of sociology Wen Fan and economics professor Juliet Schor |
| [[22]](https://www.the74million.org/article/students-in-4-day-a-week-schools-can-suffer-covid-level-learning-losses/) | #30 | — | — | `#30` there is increasing evidence that, by and large, a four-day school week causes student achievement to suffer. To study the policy's effects, we looked at a var… |
| [[23]](https://journalistsresource.org/education/four-day-school-week-research/) | — | #31 | — | `#31` students in rural areas fared better on that schedule than students in 'non-rural' areas |
| [[24]](https://en.alda.is/2021/07/04/going-public-icelands-journey-to-a-shorter-working-week/) | #33 | — | — | `#33` since completion 86% of the country's workforce are now working shorter hours or gaining the right to shorten their hours. |
| [[25]](https://brusselstimes.com/804328/four-get-about-it-few-belgians-opt-for-shorter-work-week) | #35 | — | — | `#35` Under the terms of the Federal Government's Labour Deal, introduced in November 2022, full-time workers in Belgium's private sector have been legally permitted… |
| [[26]](https://gulfnews.com/living-in-uae/ask-us/will-dubai-bring-back-its-four-day-summer-work-week-in-2026-1.500567705) | — | #37 | — | `#37` In summer 2024, DGHR launched a pilot called Our Summer is Flexible across 15 government entities. Workers were divided into two groups: one compressed their h… |
| [[27]](https://gulfnews.com/uae/government/sharjahs-new-four-day-work-week-improved-government-performance-reduced-accidents-by-40-study-finds-1.89814620) | #38 | — | — | `#38` The findings said traffic accidents and deaths decreased by up to 40 per cent as against the first quarter of 2021, with a decrease in severe injuries. |
| [[30]](https://www.semafor.com/article/01/19/2026/south-korean-banks-shorten-workweek) | — | #41 | — | `#41` Several lenders in the country, which is considered one of the world’s most overworked, are shutting off computers one hour earlier than normal on Fridays |
| [[31]](https://www.seoulz.com/korea-4-5-day-workweek-2026/) | — | #42 | — | `#42` the government submitted the Reduced Working Hours Support Act to the National Assembly |
| [[32]](https://advisory.ecija.com/en/reduccion-jornada-laboral-consulta-publica/) | #43 | — | — | `#43` On 10 September 2025, the Congress of Deputies **rejected the bill by 178 votes against** to 170 in favour. |
| [[33]](https://remoteworkeurope.eu/news/2026/spain-working-hours-bill-stalled) | — | #44 | — | `#44` There is no parliamentary timetable for reviving the proposal |
| [[34]](https://www.que.es/2026/07/17/nuevo-registro-horario-julio-2026/) | — | #45 | — | `#45` Ahora, la reforma del registro horario se cuela por la vía rápida del decreto para esquivar precisamente ese bloqueo político. |
| [[35]](https://www.wtoc.com/2026/09/14/bill-introduced-reduce-workweek-32-hours/) | — | #47 | — | `#47` Rep. Mark Takano of California and Sen. Bernie Sanders of Vermont reintroduced the “Thirty-Two Hour Workweek Act” last week. |
| [[36]](https://www.foxla.com/news/california-bill-mandating-4-day-work-week-stalled) | #48 | — | — | `#48` AB-2932 would have required larger companies start paying overtime after 32 hours a week instead of 40 hours a week. Lawmakers missed a deadline to pass it thr… |
| [[39]](https://cambridge.gov.uk/news/2025/07/17/south-cambridgeshire-district-council-votes-to-permanently-adopt-four-day-week) | #51 | — | — | `#51` Today (17 July 2025), South Cambridgeshire District Council has voted to become the first council in the UK to permanently adopt a four-day week |
| [[41]](https://www.civilserviceworld.com/news/article/scottish-government-four-day-week-pilot-assessment-productivity-wellbeing-benefits) | — | #53 | — | `#53` But McKee said the Scottish Government and its agencies “will not be moving to a 32-hour week”. |
| [[42]](https://kadry.infor.pl/kodeks-pracy/czas-pracy/7369974,resort-pracy-90-pracodawcow-i-ponad-5-tys-pracownikow-z-branzy-odziezowej-z-wodociagow-oraz-filharmonii-wezmie-udzial-w-pilotazu-skroconego-czasu-pracy-srednie-dofinansowanie-dla-jednego-podmiotu-wyniesie-05-mln-zl.html) | — | #54 | — | `#54` 90 pracodawców i ponad 5 tys. pracowników |
| [[43]](https://wydarzenia.interia.pl/kraj/news-pracuja-mniej-za-te-same-pieniadze-pierwsze-wnioski-testu-da,nId,23474291) | — | — | #55 | — |
| [[44]](https://movimentoeconomico.com.br/trabalho/2026/10/14/senado-aprova-fim-da-escala-6x1-e-reducao-da-jornada-de-trabalho/) | #56 | — | — | `#56` senadores de governo e oposição aprovaram na noite desta **quarta-feira (14)**, por **75 votos a 1** nos dois turnos, a **Proposta de Emenda à Constituição** (… |
| [[45]](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/germany-prepares-shift-to-weekly-working-time-limits) | #58 | — | — | `#58` The reform would implement the coalition agreement proposal to allow a weekly, rather than daily, maximum working time. |
| [[47]](https://thenewstack.io/kpmgs-ceo-poll-labor-markets-4-day-workweeks-and-genai/) | #63 | — | — | `#63` But 30% also said they were exploring new work schedules, organization-wide, "such as a 4-day or 4.5-day workweek." ... Conducted from Feb. 21 through March 14… |
| [[48]](https://emexmag.com/four-day-work-week-who-has-stuck-with-it-and-who-reverted/) | — | — | #66 | — |
| [[49]](https://www.cnbc.com/2022/01/05/the-4-day-workweek-becomes-permanent-for-tech-company-bolt.html) | — | #67 | — | `#67` A four-day workweek is now a permanent perk for employees of tech unicorn Bolt. |
| [[50]](https://fortune.com/europe/2023/12/07/lamborghini-four-day-workweek-italy-germany-volkswagen-unions-uaw/) | — | #68 | — | `#68` Lamborghini reached an agreement with its unions to roll out a shorter week for its production workers without slashing pay |
| [[51]](https://www.gbnews.com/money/stealth-tax-on-jobs-flexible-working-report) | #70 | — | — | `#70` Research referenced in the paper suggests workers in roles allowing remote work experienced wage growth between two and seven per cent lower after the pandemic… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://tech.co/?p=360477 — Referencia nao encontrada (404): https://tech.co/?p=360477

### Bloqueadas por barreira de acesso

- https://www.help.senate.gov/dem/newsroom/press/news-sanders-introduces-legislation-to-enact-a-32-hour-workweek-with-no-loss-in-pay — http_error — barreira de acesso (http_error): # Access Denied You don't have permission to access "http://www.help.senate.gov/$(SERVE_403)/dem/newsroom/press/news-san
- https://www.tokyoweekender.com/japan-life/news-and-opinion/four-day-workweek-for-tokyo-government-workers/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-0`** [1]
  - Trecho: The strongest study, a 2025 *Nature Human Behaviour* paper by Wen Fan, Juliet Schor, Orla Kelly and Guolin Gu, followed 2,896 employees at 141 trial and 12 control organizations and found significant falls in burnout an…
  - Justificativa: A evidência sustenta explicitamente quase todos os elementos da afirmação: autores (Wen Fan, Juliet B. Schor, Orla Kelly, Guolin Gu), periódico (Nature Human Behaviour), número de funcionários (2.896), organizações de t…
  - Suporte veio de: [1]
  - Evidência: “The researchers collected data from 2,896 employees.”
  - Não coberto pela evidência: Ano de publicação 2025 — a evidência diz apenas 'recently published' sem especificar o ano.
- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-4`** [1]
  - Trecho: Fan describes it as "not a compressed workweek," but one that "involves genuine reductions in work hours without reductions in pay." The alternative, compressed hours, packs the same weekly hours into fewer and longer d…
  - Justificativa: A evidência contém citação literal de Fan afirmando que o modelo estudado não é uma semana de trabalho comprimida, mas envolve reduções genuínas nas horas de trabalho sem redução de salário. A evidência também descreve…
  - Suporte veio de: [1]
  - Evidência: “"A common misconception around the four-day workweek is how it's defined," Fan noted. "The model we study, for example, is not a compressed workweek, but involves genuine reductions in work hours without reductions in p…”
- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-5`** [5]
  - Trecho: Fortune's review of failed schemes concluded that the most successful trials used reduced hours at the same pay rather than compression.
  - Justificativa: A evidência, proveniente de artigos da Fortune, revisa esquemas falhados (Asda e D&G) e conclui explicitamente que os testes mais bem-sucedidos envolvem redução de horas com a mesma remuneração ('shorten their hours for…
  - Suporte veio de: [5]
  - Evidência: “The most successful trials tend to see employees shorten their hours for the same pay, as with South Cambridgeshire Council.”
### UNSUPPORTED

- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-1`** [2]
  - Trecho: The business claims that dominate headlines, such as rising revenue and steep drops in sick days and resignations, come largely from self-reported data compiled by advocacy groups and their academic partners.
  - Justificativa: A evidência confirma que os dados são em grande parte autorrelatados ("self-reports of companies") e que são compilados por um grupo de defesa (4 Day Week Global) com parceiros acadêmicos (Schor, de Boston College). No…
  - Suporte veio de: [2]
  - Evidência: “Take it for what it is -- self-reports of companies saying this innovation is working”
  - Não coberto pela evidência: steep drops in sick days; resignations; claims that dominate headlines
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [1] [20] [3] [40] [12] [15] [17] [41] [14] [48] [23] [5] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-2`** [3]
  - Trecho: The most rigorous controlled pilot, in Germany, found no significant change in revenue, profit or sick days, which reads as "no harm" rather than "gain." Governments have mostly chosen soft instruments such as rights to…
  - Justificativa: A primeira parte da afirmação (sobre o piloto alemão não encontrar mudanças significativas em receita, lucro e dias de doença) é sustentada pela evidência. Porém, a segunda parte — sobre governos escolhendo instrumentos…
  - Suporte veio de: [3]
  - Evidência: “Although there were slight increases in key financial performance indicators such as turnover and profit, these were not significantly different from the previous year.”
  - Não coberto pela evidência: Governments have mostly chosen soft instruments such as rights to request, public-sector schemes, subsidies and pilots; The interpretation 'no harm rather than gain' is an editorial judgment not explicitly stated in the evidence
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-3`** [4]
  - Trecho: The biggest statutory change of 2026 was Brazil's constitutional amendment cutting the maximum week from 44 to 40 hours, on a five-day schedule rather than a four-day one.
  - Justificativa: A evidência confirma a emenda constitucional de 2026 que reduz a jornada de 44 para 40 horas na escala 5×2 (cinco dias). Porém, não sustenta que foi 'a maior mudança estatutária de 2026' nem menciona alternativa de jorn…
  - Suporte veio de: [4]
  - Evidência: “O Congresso Nacional promulgou, nesta sexta-feira (16), a Emenda Constitucional nº 141 de 2026”
  - Não coberto pela evidência: biggest statutory change of 2026; rather than a four-day one
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semana_trabalho_d029e3aa4d63_20261115T034149Z-15`** [14]
  - Trecho: Schor noted that the gains in job satisfaction and sleep had "nudged down a bit" from six months.
  - Justificativa: The evidence quotes Schor saying
  - Evidência: “Job satisfaction and sleep problems nudged down a bit, but the bulk of the original improvement remains.”

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 2 citam referência não baixada/inacessível.

- `semana_trabalho_d029e3aa4d63_20261115T034149Z-10` — Referencia(s) citada(s) ['fa1e2427802bfd55'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d029e3aa4d63_20261115T034149Z-39` — Referencia(s) citada(s) ['675cbba9fcba83f8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d029e3aa4d63_20261115T034149Z-46` — Referencia(s) citada(s) ['fa1e2427802bfd55'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d029e3aa4d63_20261115T034149Z-49` — Referencia(s) citada(s) ['0e91bd09abc99aef'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_d029e3aa4d63_20261115T034149Z-62` — Referencia(s) citada(s) ['257109bb88925e42'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).