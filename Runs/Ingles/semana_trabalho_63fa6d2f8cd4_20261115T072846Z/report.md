# Relatório de Auditoria — ChatGPT (semana_trabalho_63fa6d2f8cd4_20261115T072846Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/EmConsolidacao/semana_trabalho.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_63fa6d2f8cd4_20261115T072846Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T10:36:36.557574+00:00 |
| **Total de trechos citados** | 108 |
| **Tempo de processamento** | 0:00:50:55 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 33.4 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 166 marcadores, 27 distintos |
| Referências listadas | 30 (3 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 43 | 39.8% |
| **UNSUPPORTED** | 47 | 43.5% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 18 | 16.7% |
| **TOTAL** | 108 | 100.0% |

Sobre os 90 trechos citados auditados: SUPPORTED 47,77%, UNSUPPORTED 52,22%, CONTRADICTED 0,00%.

> **23 dos 43 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 23 estão **contados dentro** dos 43 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`53` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `18` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 5, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#43` A more plausible mechanism is that fewer hours can raise **hourly** productivity by reducing fatigue, eliminating low-v… | [10] | [7] [8] | — |
| `#50` Selection therefore remains an important constraint on generalization. | [6] | [12] [10] [8] | — |
| `#77` State rules can materially affect implementation. | [20] | [10] [8] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 3800902 |
| **Média de tokens por requisição** | 42232.2 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 3/30 (10.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[10]](https://www.oecd.org/en/publications/oecd-employment-outlook-2022_1bb305a6-en/full-report/component-9.html) | downloaded | 24 | 8 | 10 | 6 | 0 |
| [[9]](https://www.wiwi.uni-muenster.de/tow/sites/tow/files/downloads/4DW_FollowUp_Report_Englisch.pdf) | downloaded | 21 | 7 | 5 | 9 | 0 |
| [[6]](https://www.nature.com/articles/s41562-025-02259-6) | downloaded | 20 | 4 | 9 | 7 | 0 |
| [[7]](https://www.henley.ac.uk/news/2024/results-from-portugals-government-backed-4-day-week-trial-released) | downloaded | 14 | 7 | 3 | 3 | 1 |
| [[5]](https://digit-research.org/projects/the-four-day-week-and-reducing-working-time/) | downloaded | 13 | 1 | 7 | 5 | 0 |
| [[8]](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_protect/%40protrav/%40travail/documents/publication/wcms_864222.pdf) | downloaded | 9 | 2 | 4 | 1 | 2 |
| [[12]](https://link.springer.com/article/10.1007/s00420-025-02153-8) | downloaded | 8 | 3 | 3 | 2 | 0 |
| [[15]](https://www.sciencedirect.com/science/article/pii/S0967070X17304778) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[16]](https://academic.oup.com/sf/article-abstract/96/4/1851/4951469) | downloaded | 5 | 1 | 0 | 0 | 4 |
| [[23]](https://employment.belgium.be/en/node/3860) | downloaded | 5 | 1 | 0 | 0 | 4 |
| [[24]](https://u.ae/en/information-and-services/jobs/working-in-uae-government-sector/working-hours-in-the-public-sector) | dead | 5 | 0 | 0 | 0 | 5 |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/40075240/) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[14]](https://journals.sagepub.com/doi/10.1177/0961463X261449357) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[18]](https://www.govinfo.gov/app/details/BILLS-119hr10323ih) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[25]](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/industria/paginas/2023/170323-empresas-programa-piloto-jornada-4-dias.aspx) | downloaded | 4 | 0 | 2 | 0 | 2 |
| [[19]](https://www.govinfo.gov/app/details/BILLS-119s5384is) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[20]](https://www.dir.ca.gov/dlse/FAQ_OvertimeExceptions.htm) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[1]](https://www.ilo.org/publications/working-time-and-work-life-balance-around-world) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[4]](https://normlex.ilo.org/dyn/nrmlx_en/f?p=1000:51:0::::51:P51_CONTENT_REPOSITORY_ID:3288167) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[17]](https://www.dol.gov/agencies/whd/overtime/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[22]](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32003L0088) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[29]](https://researchrepository.ilo.org/esploro/outputs/journalArticle/Shorter-hours-wanted-a-systematic-review/995365188502676) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[2]](https://www.dol.gov/general/aboutdol/history/dolchp03) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://www.bls.gov/opub/mlr/2016/article/the-life-of-american-workers-in-1915.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[11]](https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke) | dead | 1 | 0 | 0 | 0 | 1 |
| [[21]](https://www.irs.gov/affordable-care-act/employers/identifying-full-time-employees) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://www.eurofound.europa.eu/en/publications/all/comparative-analysis-of-the-reduction-in-working-time-and-the-four-day-work-week-in-the-eu) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[26]](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[27]](https://www.wiwi.uni-muenster.de/tow/en/4-day-week-germany-wide-pilot-study) | downloaded | 0 · nunca citada | — | — | — | — |
| [[28]](https://www.who.int/news-room/questions-and-answers/item/global-regional-and-national-burdens-of-ischemic-heart-disease-and-stroke-attributable-to-exposure-to-long-working-hours-for-194-countries-2000-2016) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[10]](https://www.oecd.org/en/publications/oecd-employment-outlook-2022_1bb305a6-en/full-report/component-9.html) | #29–31, #42, #51, #66–68 | #43–44, #63–65, #88, #91, #93, #105, #107 | #34, #95–97, #104, #106 | `#29` reforms had no significant effects on employment, on workers' compensation nor on hourly productivity (Figure 5.7). Although insignificant, the evidence displa… |
| [[9]](https://www.wiwi.uni-muenster.de/tow/sites/tow/files/downloads/4DW_FollowUp_Report_Englisch.pdf) | #6, #23, #40–41, #101, #103–104 | #17, #87, #94, #96, #107 | #38–39, #58–60, #62, #88, #90, #92 | `#6` While the original trial was widely associated with a fixed day off per week, some organizations started to adopt more flexible arrangements even within the tr… |
| [[6]](https://www.nature.com/articles/s41562-025-02259-6) | #10, #46–48 | #3, #11, #45, #49, #93, #101–102, #105, #107 | #1, #50, #88–89, #92, #94, #97 | `#10` Both company-level and individual-level reductions in hours are correlated with well-being gains, with larger individual-level (but not company-level) reductio… |
| [[7]](https://www.henley.ac.uk/news/2024/results-from-portugals-government-backed-4-day-week-trial-released) | #5, #22, #35–37, #54–55 | #4, #17, #102 | #87, #90, #104, #53 (pulado) | `#5` The final results of a government-funded 4-day week pilot programme in Portugal were published this week, with 95% of companies rating the experience positivel… |
| [[5]](https://digit-research.org/projects/the-four-day-week-and-reducing-working-time/) | #21 | #3–4, #17, #32–33, #102, #105 | #29, #62, #87, #91, #94 | `#21` The trial, which was conducted in the UK from June to December 2022, involved 61 companies and approximately 2,900 employees. The four-day week is a form of em… |
| [[8]](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_protect/%40protrav/%40travail/documents/publication/wcms_864222.pdf) | #19–20 | #18, #60, #101, #103 | #58, #85–86 (pulado) | `#19` Between 2015 and 2019, Iceland implemented two large-scale pilots of reduced working weeks of 35–36 hours, which at their peak covered more than 1 per cent of… |
| [[12]](https://link.springer.com/article/10.1007/s00420-025-02153-8) | #7–9 | #1, #11, #97 | #2, #106 | `#7` Importantly, studies investigating the consequences of extended daily work hours often do not control for weekly work hours |
| [[16]](https://academic.oup.com/sf/article-abstract/96/4/1851/4951469) | #71 | — | #69, #72–73, #100 (pulado) | `#71` Our findings suggest that over the 2007–2013 period, state-level carbon emissions and average working hours have a strong, positive relationship, which holds a… |
| [[23]](https://employment.belgium.be/en/node/3860) | #26 | — | #25, #28, #85–86 (pulado) | `#26` Artikel 20bis/1 van de Arbeidswet van 16 maart 1971 biedt de mogelijkheid aan de werknemer om de normale voltijdse wekelijkse arbeidsduur te presteren op vier… |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/40075240/) | #61 | #59 | #58, #106 | `#61` Conducted at two hospitals in the United States, this 4-month pilot study... Thirty-eight healthcare leaders voluntarily transitioned to a 4-day workweek... Bu… |
| [[18]](https://www.govinfo.gov/app/details/BILLS-119hr10323ih) | #80 | #81 | #63, #82 | `#80` Mr. Takano (for himself, Ms. Jayapal, Ms. Norton, Ms. Tlaib, Ms. Omar, Mr. Correa, and Mrs. Ramirez) introduced the following bill; which was referred to the C… |
| [[25]](https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/industria/paginas/2023/170323-empresas-programa-piloto-jornada-4-dias.aspx) | — | #17, #24 | #85–86 (pulado) | `#17` Esta convocatoria, pionera en España |
| [[19]](https://www.govinfo.gov/app/details/BILLS-119s5384is) | #80 | #81 | #82 | `#80` Mr. Sanders introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions |
| [[20]](https://www.dir.ca.gov/dlse/FAQ_OvertimeExceptions.htm) | — | #77–78 | #79 | `#77` Special Overtime Rules Under the IWC Wage Orders |
| [[1]](https://www.ilo.org/publications/working-time-and-work-life-balance-around-world) | — | — | #0, #16 | — |
| [[17]](https://www.dol.gov/agencies/whd/overtime/) | — | #75 | #74 | `#75` Unless exempt, employees covered by the Act must receive overtime pay for hours worked over 40 in a workweek at a rate not less than time and one-half their re… |
| [[22]](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32003L0088) | #84 | — | #83 | `#84` 1. This Directive lays down minimum safety and health requirements for the organisation of working time. 2. This Directive applies to: (a) minimum periods of d… |
| [[2]](https://www.dol.gov/general/aboutdol/history/dolchp03) | #15 | — | — | `#15` the Fair Labor Standards Act (FLSA) became law in 1938. Administered by the Department of Labor, the Act set a minimum wage of 25 cents per hour and a maximum… |
| [[3]](https://www.bls.gov/opub/mlr/2016/article/the-life-of-american-workers-in-1915.htm) | — | #14 | — | `#14` It wasn't until 1926 that Henry Ford reduced the workweek in his factories from 48 to 40 hours. |
| [[21]](https://www.irs.gov/affordable-care-act/employers/identifying-full-time-employees) | #76 | — | — | `#76` For purposes of the employer shared responsibility provisions, a full-time employee is, for a calendar month, an employee employed on average at least 30 hours… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke — Referencia nao encontrada (404): https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke
- https://u.ae/en/information-and-services/jobs/working-in-uae-government-sector/working-hours-in-the-public-sector — Referencia nao encontrada (404): https://u.ae/en/information-and-services/jobs/working-in-uae-government-sector/working-hours-in-the-public-sector

### Inacessíveis (403/timeout/SSL)

- https://normlex.ilo.org/dyn/nrmlx_en/f?p=1000:51:0::::51:P51_CONTENT_REPOSITORY_ID:3288167 — HTTP 400 em https://normlex.ilo.org/dyn/nrmlx_en/f?p=1000:51:0::::51:P51_CONTENT_REPOSITORY_ID:3288167

### Bloqueadas por barreira de acesso

- https://journals.sagepub.com/doi/10.1177/0961463X261449357 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.sciencedirect.com/science/article/pii/S0967070X17304778 — http_error — barreira de acesso (http_error): # There was a problem providing the content you requested Please contact our support team for more information and provi
- https://researchrepository.ilo.org/esploro/outputs/journalArticle/Shorter-hours-wanted-a-systematic-review/995365188502676 — interstitial — barreira de acesso (interstitial): As described in our Corporate Privacy Notice and Cookie Policy, we use cookies (including pixels or other similar techno

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-4`** [5] [7]
  - Trecho: Participating firms commonly retain 100% of pay while meaningfully reducing working time and reorganizing work to preserve output, although actual reductions vary and are not always a full 20%.
  - Justificativa: A evidência sustenta as partes essenciais da afirmação: (1) manutenção de 100% do salário ('maintaining their regular full-time pay and benefits'); (2) redução significativa do tempo de trabalho (12% e 13,7% nos trials…
  - Suporte veio de: [7] [5]
  - Evidência: “The four-day week is a form of employment whereby employees work for four days a week as opposed to the traditional five (or a similar, 'meaningful' reduction in hours), whilst maintaining their regular 'full-time' pay…”
  - Não coberto pela evidência: A afirmação de que as firmas reorganizam o trabalho especificamente 'para preservar output' (intencionalidade causal) não é explicitamente declarada na evidência, embora seja inferível.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | Before the pilot project, employees worked 41.6 hours (including overtime) compared to 36.5 hours during the pilot (a r… |
    | [5] | parcial | The four-day week is a form of employment whereby employees work for four days a week as opposed to the traditional fiv… |

- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-5`** [7]
  - Trecho: Portugal’s government-backed trial, for example, produced a company-reported average reduction of 13.7%, with some employers using a weekly day off and others a nine-day fortnight.
  - Justificativa: A evidência confirma os elementos essenciais da afirmação: o trial foi financiado pelo governo ("government-funded"), houve redução de 13,7% do tempo de trabalho ("reduced their work time by 13.7%"), e parte das empresa…
  - Suporte veio de: [7]
  - Evidência: “The final results of a government-funded 4-day week pilot programme in Portugal were published this week”
  - Não coberto pela evidência: company-reported — a evidência não especifica que a redução de 13,7% foi relatada pelas empresas; atribui a constatação aos pesquisadores do estudo
  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência confirma o valor de 13,7% de redução de tempo de trabalho e o uso de um dia livre por semana versus quinzena de nove dias, mas…") — cascata: baseline → context_expansion
- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-6`** [9]
  - Trecho: Germany’s experience similarly evolved away from a rigid “Friday off” model toward flexible weekly reductions, monthly hour targets, and rotation systems, leading researchers there to prefer the broader term “work time…
  - Justificativa: A evidência sustenta a afirmação em sua parte essencial: confirma a evolução de um modelo rígido de dia fixo de folga para arranjos flexíveis (reduções semanais flexíveis, metas mensais de horas, sistemas de rotação), e…
  - Suporte veio de: [9]
  - Evidência: “While the original trial was widely associated with a fixed day off per week, some organizations started to adopt more flexible arrangements even within the trial period.”
  - Não coberto pela evidência: A menção específica a 'Friday off' não é encontrada na evidência, que fala em 'fixed day off per week' sem especificar o dia da semana.
### UNSUPPORTED

- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-0`** [1]
  - Trecho: The “four-day workweek” is best understood as a family of working-time arrangements rather than one standardized policy.
  - Justificativa: A evidência trata de tempo de trabalho, equilíbrio vida-trabalho e arranjos flexíveis, mas não menciona em nenhum momento a 'semana de trabalho de quatro dias' (four-day workweek) nem a caracteriza como uma família de a…
  - Não coberto pela evidência: four-day workweek; family of working-time arrangements; not one standardized policy
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-1`** [6] [12]
  - Trecho: The distinction that matters most is between **reduced working time**, typically around 32 hours across four days with weekly pay preserved, and a **compressed workweek**, in which roughly 38–40 hours are redistributed…
  - Justificativa: A evidência descreve detalhadamente o conceito de 'compressed workweek' (jornada comprimida) como horas diárias estendidas com redução de dias, mantendo as horas semanais totais (ex.: 10h × 4 dias = 40h como alternativa…
  - Suporte veio de: [12] [6]
  - Evidência: “In a compressed workweek, employees work extended daily work hours (≥ 10 h), also referred to as extended shifts, compensated by a reduced number of workdays so that the weekly work hours remain the same. For example, e…”
  - Não coberto pela evidência: A distinção entre 'reduced working time' e 'compressed workweek' como 'a distinção que mais importa'; A definição de 'reduced working time' como tipicamente 32 horas em quatro dias; O numero especifico de 32 horas para reduced working time
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | ausente | — |
    | [12] | parcial | In a compressed workweek, employees work extended daily work hours (≥ 10 h), also referred to as extended shifts, compe… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-2`** [12]
  - Trecho: These models can have materially different effects because the first reduces total exposure to work while the second primarily rearranges it.
  - Justificativa: A evidência não menciona dois 'modelos' distintos onde um 'reduz a exposição total ao trabalho' e o outro 'rearranja' o trabalho. A evidência discute semanas de trabalho comprimidas (que mantêm as horas semanais iguais,…
  - Não coberto pela evidência: A existência de dois 'modelos' distintos referidos na afirmação; A caracterização de que o primeiro modelo 'reduz a exposição total ao trabalho'; A caracterização de que o segundo modelo 'rearranja' o trabalho
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 9 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 5 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 4 citam referência não baixada/inacessível.

- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-12` — Referencia(s) citada(s) ['a9dcdb8b5c239d1c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-13` — Referencia(s) citada(s) ['a9dcdb8b5c239d1c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-27` — Referencia(s) citada(s) ['5b10e21ed11dbf41'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-52` — Referencia(s) citada(s) ['937f9584a4ed59d8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-56` — Referencia(s) citada(s) ['00eb419515bef066'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-57` — Referencia(s) citada(s) ['00eb419515bef066'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-70` — Referencia(s) citada(s) ['f5b6e42d671f6396'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-98` — Referencia(s) citada(s) ['00eb419515bef066', '949d2e8d8f6914a0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-99` — Referencia(s) citada(s) ['949d2e8d8f6914a0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-25` — Parte das fontes citadas sem conteudo: referencia(s) ['5b10e21ed11dbf41'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-28` — Parte das fontes citadas sem conteudo: referencia(s) ['5b10e21ed11dbf41'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-53` — Parte das fontes citadas sem conteudo: referencia(s) ['00eb419515bef066'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-69` — Parte das fontes citadas sem conteudo: referencia(s) ['f5b6e42d671f6396'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-72` — Parte das fontes citadas sem conteudo: referencia(s) ['f5b6e42d671f6396'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-73` — Parte das fontes citadas sem conteudo: referencia(s) ['f5b6e42d671f6396'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-85` — Parte das fontes citadas sem conteudo: referencia(s) ['5b10e21ed11dbf41'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-86` — Parte das fontes citadas sem conteudo: referencia(s) ['5b10e21ed11dbf41'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semana_trabalho_63fa6d2f8cd4_20261115T072846Z-100` — Parte das fontes citadas sem conteudo: referencia(s) ['f5b6e42d671f6396'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.