# Relatório de Auditoria — Claude (semana_trabalho_d608d7fd3ef0_20261101T220900Z)

**Arquivo auditado:** `answers/Claude/EmConsolidacao/semana_trabalho.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_d608d7fd3ef0_20261101T220900Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-04T03:42:17.639959+00:00 |
| **Total de trechos citados** | 84 |
| **Tempo de processamento** | 2:05:33:17 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 28.9 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 91 marcadores, 48 distintos |
| Referências listadas | 48 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 72 | 85.7% |
| **UNSUPPORTED** | 6 | 7.1% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 6 | 7.1% |
| **TOTAL** | 84 | 100.0% |

Sobre os 78 trechos citados auditados: SUPPORTED 92,30%, UNSUPPORTED 7,69%, CONTRADICTED 0,00%.

> **6 dos 72 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 6 estão **contados dentro** dos 72 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`7` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `1` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `4` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` Foi o que a Bélgica adotou em 2022, como se verá adiante. | [27] | [28] [17] [46] [26] [31] [14] [3] [1] [32] [22] [44] [7] [23] | — |
| `#21` Uma diferença importante em relação aos relatórios anteriores é a existência de um grupo de comparação: cerca de 300 em… | [12] | [46] [25] [23] [22] [13] [18] [16] [15] [17] [7] [45] | — |
| `#35` Participaram 41 empresas e mais de mil trabalhadores, e 95% das empresas avaliaram a experiência positivamente. | [17] | [18] [20] [19] [22] [46] [45] [23] [47] [7] [16] [3] [1] [36] | — |
| `#83` No Brasil, a mobilização que começou em torno da semana de quatro dias resultou em uma proposta mais moderada, o fim da… | [37] [40] | [35] [38] [36] [3] [24] [48] [41] [22] [1] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 279391 |
| **Média de tokens por requisição** | 3581.9 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/48 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[11]](https://www.scimex.org/newsfeed/a-four-day-workweek-makes-workers-happier-and-more-confident-at-their-jobs) | downloaded | 6 | 5 | 1 | 0 | 0 |
| [[4]](https://abc13.com/iceland-work-week-shorter-cuccess/10871439/) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[7]](https://poulantzas.gr/en/yliko/four-day-workweek-results-of-the-pilot-trial-in-the-united-kingdom/) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[17]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[16]](https://www.thelocal.de/20241106/what-are-the-results-of-germanys-four-day-work-week-trial) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[18]](https://rr.pt/noticia/economia/2023/12/12/semana-de-quatro-dias-reduz-em-137-em-media-de-horas-de-trabalho-semanais/358908/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[27]](https://observador.pt/2022/02/15/belgica-aprova-semana-de-trabalho-de-quatro-dias-para-tornar-economia-mais-inovadora-sustentavel-e-digital/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[37]](https://www.brasildefato.com.br/2026/05/28/camara-aprova-fim-da-escala-6x1-e-reducao-da-jornada-para-40-horas/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[42]](https://www.capradio.org/187667) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[2]](https://www.fox29.com/news/microsoft-japan-tested-out-a-4-day-work-week-and-it-boosted-productivity-by-40-percent) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[6]](https://6abc.com/workweek-four-day-japan-companies-microsoft/5671025/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[10]](https://san.com/cc/4-day-workweek-success-89-of-uk-companies-in-trial-continuing-policy/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[13]](https://www.spektrum.de/news/reduzierte-vollzeitarbeit-funktioniert/2281141) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[14]](https://www.peoplematters.in/article/employee-relations/germanys-4-day-week-trial-offers-interesting-results-43132) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[15]](https://idw-online.de/de/news841503) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[20]](https://vermelho.org.br/?p=695282) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[22]](https://www.infomoney.com.br/?p=2549905) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[23]](https://www.meioemensagem.com.br/comunicacao/4-day-week-brazil) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://napratica.org.br/noticias/como-funciona-a-semana-de-4-dias-no-brasil-e-quais-empresas-ja-adotaram-o-modelo) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[28]](https://www.bloomberglinea.com.br/2022/02/19/belgas-podem-trabalhar-4-dias-por-semana-sem-perda-de-salario/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[29]](https://dc.fortune.com/article/tokyo-is-turning-to-a-4-day-workweek-in-a-desperate-attempt-to-help-japan-shed-its-unwanted-title-of-worlds-oldest-population) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[30]](https://hrmasia.com/tokyo-proposes-four-day-workweek-to-boost-birth-rate/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[31]](https://www.cartacapital.com.br/?p=543449) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[33]](https://diariodepernambuco.com.br/dpmais/oficial-governo-bateu-o-martelo-e-jornada-de-trabalho-de-13-horas-foi-confirmada-neste-pais/) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[40]](https://revistaforum.com.br/politica/escala-6x1-alcolumbre-votacao-pec/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[44]](https://uts.edu.au/news/2023/03/challenging-hype-4-day-work-week) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[45]](https://www.constangy.com/employment-labor-insider/u-k-study-on-four-day-workweek-merits-scrutiny) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[46]](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41562-025-02259-6/MediaObjects/41562_2025_2259_MOESM2_ESM.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[1]](https://www.opovo.com.br/noticias/economia/2023/05/12/amp/brasil-tera-teste-de-semana-de-trabalho-com-quatro-dias-entenda.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://contadores.cnt.br/projetos/42/noticias/artigos/2024/10/07/semana-de-quatro-dias-no-brasil-pode-se-tornar-realidade.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[5]](https://www.wxyz.com/news/national/icelandic-trials-studying-shorter-workweeks-hailed-as-overwhelming-successes) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[8]](https://www.research-live.com/article/news/uk-fourday-week-trial-results-in-reduced-staff-burnout/id/5109272) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://www.britishpoles.uk/?p=28451) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://www.phillyvoice.com/four-day-work-week-wellbeing-performance-benefits/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[19]](https://www.rtp.pt/noticias/economia/mais-de-80-das-empresas-que-testaram-semana-de-4-dias-decidiram-manter-modelo_n1581253) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.insper.edu.br/pt/noticias/2023/9/brasil-inicia-projeto-piloto-de-semana-de-trabalho-de-4-dias) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[25]](https://www.cartacapital.com.br/?p=444064) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://www.portaltela.com/noticias/economia/2025/08/22/experimento-da-semana-de-quatro-dias-no-brasil-resultados-e-licoes-aprendidas/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[32]](https://www.cnnbrasil.com.br/internacional/governo-espanhol-enfrenta-divisao-sobre-reducao-da-jornada-semanal-de-trabalho/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://en.apa.az/europe/greece-adopts-law-extending-working-hours-despite-protests-480903) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://jornalopcao.com.br/ultimas-noticias/proposta-de-erika-hilton-sobre-fim-da-jornada-6x1-repercute-e-ganha-apoio-popular-655522/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://agenciabrasil.ebc.com.br/politica/noticia/2026-09/ccj-do-senado-aprova-pec-que-acaba-com-jornada-6x1) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://www12.senado.leg.br/noticias/materias/2026/10/06/pec-que-acaba-com-escala-6x1-comeca-a-tramitar-no-plenario) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.cnnbrasil.com.br/politica/senado-inicia-discussao-da-pec-do-fim-da-6x1-com-baixa-presenca-da-oposicao/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://techtarget.com/searchhrsoftware/news/252525395/Four-day-workweek-productivity-claims-gather-criticism) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://jornalcontabil.com.br/noticia/semana-de-4-dias-de-trabalho-brasil-tera-nova-rodada-de-testes/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://ihu.unisinos.br/646046-a-pec-que-pode-mudar-a-cena-brasileira-artigo-de-maria-julia-pereira-eduardo-rezende-pereira-e-mateus-oliveira-dos-santos) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[11]](https://www.scimex.org/newsfeed/a-four-day-workweek-makes-workers-happier-and-more-confident-at-their-jobs) | #20, #22–25 | #77 | — | `#20` Wen Fan, Juliet Schor, and colleagues conducted 6-month trials that involved 2,896 employees across 141 organizations in Australia, Canada, New Zealand, the UK… |
| [[4]](https://abc13.com/iceland-work-week-shorter-cuccess/10871439/) | #6–7, #9–10 | — | — | `#6` Public sector employees taking part in two large trials between 2015 and 2019 worked 35-36 hours per week, with no reduction in pay. |
| [[7]](https://poulantzas.gr/en/yliko/four-day-workweek-results-of-the-pilot-trial-in-the-united-kingdom/) | #13–15 | #77 | — | `#13` It involved 61 companies and approximately 2,900 employees, running from June to December 2022 with the support of Autonomy, 4 Day Week Global, the UK's 4 Day… |
| [[17]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | #34, #36 | #35, #77 | — | `#34` Este projeto-piloto, iniciado em junho de 2023, visa proporcionar uma experiência de seis meses na implementação da semana de quatro dias de trabalho, voluntár… |
| [[16]](https://www.thelocal.de/20241106/what-are-the-results-of-germanys-four-day-work-week-trial) | #32–33, #71 | — | — | `#32` Many of the participating organisations decided not to implement a four day working week, but reduced required working hours across the five day week instead. |
| [[18]](https://rr.pt/noticia/economia/2023/12/12/semana-de-quatro-dias-reduz-em-137-em-media-de-horas-de-trabalho-semanais/358908/) | #4, #37 | #79 | — | `#4` Na maioria das empresas (58,5%), os trabalhadores têm um dia livre por semana, tendo 41,5% das empresas optado por uma quinzena de nove dias, alternando uma se… |
| [[27]](https://observador.pt/2022/02/15/belgica-aprova-semana-de-trabalho-de-quatro-dias-para-tornar-economia-mais-inovadora-sustentavel-e-digital/) | #50 | #3, #80 | — | `#50` Os trabalhadores terão, no entanto, de **trabalhar as mesmas 38 horas semanais atuais,** com a diferença de estarem concentradas em quatro dias em vez de cinco. |
| [[37]](https://www.brasildefato.com.br/2026/05/28/camara-aprova-fim-da-escala-6x1-e-reducao-da-jornada-para-40-horas/) | #61–62 | #83 | — | `#61` No 1º turno, foram 472 votos a favor e 22 contra. |
| [[2]](https://www.fox29.com/news/microsoft-japan-tested-out-a-4-day-work-week-and-it-boosted-productivity-by-40-percent) | #2, #11 | — | — | `#2` a New Zealand company, Perpetual Guardian, decided to permanently adopt the four-day week last year after a trial yielded a noticeable boost in productivity as… |
| [[6]](https://6abc.com/workweek-four-day-japan-companies-microsoft/5671025/) | #12 | #79 | — | `#12` In addition to reducing working hours, managers urged staff to cut down on the time they spent in meetings and responding to emails. They suggested that meetin… |
| [[10]](https://san.com/cc/4-day-workweek-success-89-of-uk-companies-in-trial-continuing-policy/) | #18–19 | — | — | `#18` According to a newly released report by the think tank Autonomy, of the 61 companies that participated, 89% of them have continued the four-day workweek policy… |
| [[13]](https://www.spektrum.de/news/reduzierte-vollzeitarbeit-funktioniert/2281141) | #26 | — | #78 | `#26` Fan und ihre Kollegen sprechen sich für weitere Studien aus, um die Befunde zu untermauern – am besten dann mit einer zufälligen Zuteilung von Betrieben zur Te… |
| [[14]](https://www.peoplematters.in/article/employee-relations/germanys-4-day-week-trial-offers-interesting-results-43132) | #29 | #31 | — | `#29` with many gaining an average of 38 additional minutes of sleep each week |
| [[15]](https://idw-online.de/de/news841503) | #28, #30 | — | — | `#28` Since the beginning of 2024, 45 organisations from various sectors in Germany have been taking part in a six-month pilot project by the Berlin consultancy Intr… |
| [[20]](https://vermelho.org.br/?p=695282) | #39, #74 | — | — | `#39` Gomes alerta que as empresas participantes não são representativas do mercado português como um todo |
| [[22]](https://www.infomoney.com.br/?p=2549905) | #41, #44 | — | — | `#41` Das 21 empresas que entraram no piloto da semana de 4 dias, envolvendo cerca de 290 colaboradores, apenas duas não finalizaram. |
| [[23]](https://www.meioemensagem.com.br/comunicacao/4-day-week-brazil) | #45, #47 | — | — | `#45` Entre os líderes que participaram do projeto, 84,6% acreditam que a semana de quatro dias trouxe benefícios para suas empresas. |
| [[24]](https://napratica.org.br/noticias/como-funciona-a-semana-de-4-dias-no-brasil-e-quais-empresas-ja-adotaram-o-modelo) | #43, #46 | — | — | `#43` A iniciativa foi conduzida pela Reconnect Happiness at Work e contou com a FGV-EAESP na pesquisa e avaliação dos resultados. [...] o modelo foi testado durante… |
| [[28]](https://www.bloomberglinea.com.br/2022/02/19/belgas-podem-trabalhar-4-dias-por-semana-sem-perda-de-salario/) | #51–52 | — | — | `#51` As empresas terão o direito de recusar solicitações de funcionários para uma semana de trabalho condensada desde que expliquem a recusa por escrito |
| [[29]](https://dc.fortune.com/article/tokyo-is-turning-to-a-4-day-workweek-in-a-desperate-attempt-to-help-japan-shed-its-unwanted-title-of-worlds-oldest-population) | #53, #76 | — | — | `#53` It is also adding a new “childcare partial leave” policy, which will allow some employees to work two fewer hours per day. The goal is to help employees who ar… |
| [[30]](https://hrmasia.com/tokyo-proposes-four-day-workweek-to-boost-birth-rate/) | #54 | #80 | — | `#54` could opt for a truncated work week while maintaining the current requirement of 155 monthly working hours |
| [[31]](https://www.cartacapital.com.br/?p=543449) | #55, #81 | — | — | `#55` O Congresso dos Deputados rejeitou, nesta quarta-feira 10, a redução da jornada de trabalho semanal, um projeto-chave do governo de esquerda [...] A proposta,… |
| [[40]](https://revistaforum.com.br/politica/escala-6x1-alcolumbre-votacao-pec/) | #65 | #83 | — | `#65` pautou para a próxima quarta-feira (14) a votação em primeiro turno da Proposta de Emenda à Constituição (PEC) que prevê o fim da escala de trabalho 6×1. [...]… |
| [[44]](https://uts.edu.au/news/2023/03/challenging-hype-4-day-work-week) | #68, #78 | — | — | `#68` Organisations in other sectors, with different occupational profiles, may find increased productivity through more intensive working difficult to emulate. |
| [[45]](https://www.constangy.com/employment-labor-insider/u-k-study-on-four-day-workweek-merits-scrutiny) | #5, #70 | — | — | `#5` some closed all operations on Fridays; some divided their staffs' days off between Mondays and Fridays; some continued to work a five-day week, but only with f… |
| [[46]](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41562-025-02259-6/MediaObjects/41562_2025_2259_MOESM2_ESM.pdf) | #27, #78 | — | — | `#27` they should explicitly acknowledge that self-selection into the trial likely biases the results towards detecting an upper bound rather than the average true e… |
| [[1]](https://www.opovo.com.br/noticias/economia/2023/05/12/amp/brasil-tera-teste-de-semana-de-trabalho-com-quatro-dias-entenda.html) | #0 | — | — | `#0` O modelo usado é chamado 100-80-100: 100% do salário, 80% da jornada (quatro dias, em vez de cinco), e 100% da produtividade. |
| [[3]](https://contadores.cnt.br/projetos/42/noticias/artigos/2024/10/07/semana-de-quatro-dias-no-brasil-pode-se-tornar-realidade.html) | #1 | — | — | `#1` A semana de quatro dias começou na Nova Zelândia, em 2019, e foi se expandindo para outros países de diferentes continentes, sob a gestão do movimento *4 Day W… |
| [[5]](https://www.wxyz.com/news/national/icelandic-trials-studying-shorter-workweeks-hailed-as-overwhelming-successes) | #8 | — | — | `#8` In the trials, Alda says productivity and "service provision" remained the same or improved across the majority of trial workplaces. ... The trials also remain… |
| [[8]](https://www.research-live.com/article/news/uk-fourday-week-trial-results-in-reduced-staff-burnout/id/5109272) | #16 | — | — | `#16` The majority of employees taking part in the trial who responded to a survey from researchers ( 90%) reported that they 'definitely want to continue' on a four… |
| [[9]](https://www.britishpoles.uk/?p=28451) | #17 | — | — | `#17` The researchers also reported a 65% reduction in sick days and a 57% reduction in the number of employees quitting their job for other companies. |
| [[12]](https://www.phillyvoice.com/four-day-work-week-wellbeing-performance-benefits/) | — | #21 | — | `#21` The trial compared nearly 3,000 employees at 141 businesses and organizations who adopted a four-day work week with nearly 300 employees at 12 companies who st… |
| [[19]](https://www.rtp.pt/noticias/economia/mais-de-80-das-empresas-que-testaram-semana-de-4-dias-decidiram-manter-modelo_n1581253) | #38 | — | — | `#38` O relatório do projeto-piloto recomenda que uma da forma de estimular a aplicação da semana de quatro dias poderá passar pela atribuição de incentivos fiscais… |
| [[25]](https://www.cartacapital.com.br/?p=444064) | #48 | — | — | `#48` Oito das 19 empresas brasileiras que participaram de testes sobre a semana de quatro dias de trabalho decidiram manter o modelo. É o que mostra um relatório da… |
| [[26]](https://www.portaltela.com/noticias/economia/2025/08/22/experimento-da-semana-de-quatro-dias-no-brasil-resultados-e-licoes-aprendidas/) | — | #49 | — | `#49` Ela aponta que a cultura de trabalho no Brasil ainda é marcada por uma jornada 6×1 e que a crise econômica contribui para essa resistência. |
| [[32]](https://www.cnnbrasil.com.br/internacional/governo-espanhol-enfrenta-divisao-sobre-reducao-da-jornada-semanal-de-trabalho/) | #56 | — | — | `#56` O Banco Central da Espanha e um ex-ministro da Economia alertaram que os custos trabalhistas mais altos poderiam alimentar a inflação e reduzir a criação de em… |
| [[34]](https://en.apa.az/europe/greece-adopts-law-extending-working-hours-despite-protests-480903) | #58 | — | — | `#58` Greece already has among the longest working weeks in Europe at around 40 hours, EU data shows, against an average 34 hours worked in Germany or 32 in the Neth… |
| [[35]](https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1) | #60 | — | — | `#60` O texto estabelece uma carga semanal de quatro dias de trabalho e três dias de descanso, eliminando a atual escala 6x1, seis dias de trabalho e um de descanso,… |
| [[36]](https://jornalopcao.com.br/ultimas-noticias/proposta-de-erika-hilton-sobre-fim-da-jornada-6x1-repercute-e-ganha-apoio-popular-655522/) | #59 | — | — | `#59` O movimento Vida Além do Trabalho surgiu quando Rick Azevedo, ex-balconista de farmácia, fez um desabafo nas redes sociais sobre as dificuldades de viver sob a… |
| [[38]](https://agenciabrasil.ebc.com.br/politica/noticia/2026-09/ccj-do-senado-aprova-pec-que-acaba-com-jornada-6x1) | #63 | — | — | `#63` Estudos sobre o fim da 6x1 divergem sobre os impactos para a inflação e o Produto Interno Bruto (PIB, soma de bens e serviços produzidos no país). |
| [[39]](https://www12.senado.leg.br/noticias/materias/2026/10/06/pec-que-acaba-com-escala-6x1-comeca-a-tramitar-no-plenario) | #64 | — | — | `#64` No Plenário, a matéria precisa passar por cinco sessões de debates antes de ser votada em primeiro turno. Se aprovada, segue para o segundo turno, com outras t… |
| [[41]](https://www.cnnbrasil.com.br/politica/senado-inicia-discussao-da-pec-do-fim-da-6x1-com-baixa-presenca-da-oposicao/) | #66 | — | — | `#66` Para ser aprovada, a PEC precisa de 49 votos favoráveis em dois turnos. |
| [[43]](https://techtarget.com/searchhrsoftware/news/252525395/Four-day-workweek-productivity-claims-gather-criticism) | #69 | — | — | `#69` "Take it for what it is -- self-reports of companies saying this innovation is working," Schor said. |
| [[47]](https://jornalcontabil.com.br/noticia/semana-de-4-dias-de-trabalho-brasil-tera-nova-rodada-de-testes/) | #42 | — | — | `#42` uma delas, localizada no Rio Grande do Sul, desistiu por conta das enchentes, e a outra interrompeu os testes após uma troca no comando. |
| [[48]](https://ihu.unisinos.br/646046-a-pec-que-pode-mudar-a-cena-brasileira-artigo-de-maria-julia-pereira-eduardo-rezende-pereira-e-mateus-oliveira-dos-santos) | #75 | — | — | `#75` Do contrário, o tempo de não trabalho (produtivo) das mulheres corre o risco de se transformar em tempo livre para o trabalho (reprodutivo). |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.insper.edu.br/pt/noticias/2023/9/brasil-inicia-projeto-piloto-de-semana-de-trabalho-de-4-dias — http_error — barreira de acesso (http_error): # Access Denied You don't have permission to access "http://www.insper.edu.br/pt/noticias/2023/9/brasil-inicia-projeto-p
- https://diariodepernambuco.com.br/dpmais/oficial-governo-bateu-o-martelo-e-jornada-de-trabalho-de-13-horas-foi-confirmada-neste-pais/ — http_error — barreira de acesso (http_error): AccessDenied Access Denied This XML file does not appear to have any style information associated with it. The document 
- https://www.capradio.org/187667 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-0`** [1]
  - Trecho: O formato mais associado ao movimento internacional é o chamado 100-80-100: o trabalhador recebe 100% do salário, trabalha 80% da jornada (quatro dias em vez de cinco) e se compromete a manter 100% da produtividade.
  - Justificativa: A evidência descreve explicitamente o modelo 100-80-100 com os mesmos elementos da afirmação: 100% do salário, 80% da jornada (quatro dias em vez de cinco) e 100% da produtividade.
  - Suporte veio de: [1]
  - Evidência: “O modelo usado é chamado 100-80-100: 100% do salário, 80% da jornada (quatro dias, em vez de cinco), e 100% da produtividade.”
  - Não coberto pela evidência: A caracterização do 100-80-100 como 'o formato mais associado ao movimento internacional' não é explicitamente afirmada na evidência, embora a evidência indique que é o modelo usado pela ONG 4 Day Week em diversos países.
- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-1`** [3]
  - Trecho: O movimento ganhou forma na Nova Zelândia, em 2019, e se espalhou por outros continentes sob a coordenação da 4 Day Week Global, uma organização sem fins lucrativos.
  - Justificativa: A evidência afirma explicitamente que a semana de quatro dias começou na Nova Zelândia em 2019, expandiu-se para outros continentes sob a gestão do 4 Day Week Global, descrito como comunidade sem fins lucrativos. O trec…
  - Suporte veio de: [3]
  - Evidência: “A semana de quatro dias começou na Nova Zelândia, em 2019, e foi se expandindo para outros países de diferentes continentes, sob a gestão do movimento *4 Day Week Global*, que é uma comunidade sem fins lucrativos.”
- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-2`** [2]
  - Trecho: Um marco anterior foi a empresa neozelandesa Perpetual Guardian, que adotou o modelo de forma permanente depois que um teste apontou ganhos de produtividade e de satisfação.
  - Justificativa: A evidência confirma explicitamente que a empresa neozelandesa Perpetual Guardian adotou permanentemente a semana de quatro dias após um teste que indicou ganhos de produtividade e satisfação no trabalho, sustentando in…
  - Suporte veio de: [2]
  - Evidência: “a New Zealand company, Perpetual Guardian, decided to permanently adopt the four-day week last year after a trial yielded a noticeable boost in productivity as well as in job satisfaction among employees.”
### UNSUPPORTED

- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-3`** [27]
  - Trecho: Foi o que a Bélgica adotou em 2022, como se verá adiante.
  - Justificativa: A evidência descreve medidas adotadas pela Bélgica (semana de quatro dias, direito a desligar), mas não menciona o ano de 2022. A afirmação faz referência a uma adoção específica em 2022, informação que não consta na ev…
  - Suporte veio de: [27]
  - Não coberto pela evidência: ano de 2022; a que medida específica o trecho se refere ('Foi o que...')
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [28] [17] [46] [26] [31] [14] [3] [1] [32] [22] [44] [7] [23] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-21`** [12]
  - Trecho: Uma diferença importante em relação aos relatórios anteriores é a existência de um grupo de comparação: cerca de 300 empregados de 12 empresas que mantiveram a semana de cinco dias.
  - Justificativa: A evidência confirma a existência de um grupo de comparação de quase 300 empregados de 12 empresas com semana de cinco dias, mas não menciona 'relatórios anteriores' nem que isso seja uma diferença em relação a eles. Es…
  - Suporte veio de: [12]
  - Evidência: “The trial compared nearly 3,000 employees at 141 businesses and organizations who adopted a four-day work week with nearly 300 employees at 12 companies who stuck with a five-day schedule.”
  - Não coberto pela evidência: Diferença em relação aos relatórios anteriores
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [46] [25] [23] [22] [13] [18] [16] [15] [17] [7] [45] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_d608d7fd3ef0_20261101T220900Z-31`** [14]
  - Trecho: Segundo a imprensa especializada, eram duas fabricantes do setor industrial.
  - Justificativa: A evidência confirma que 'two large manufacturing companies' descontinuaram a semana de 4 dias, sustentando a parte sobre 'duas fabricantes do setor industrial'. No entanto, a atribuição 'Segundo a imprensa especializad…
  - Suporte veio de: [14]
  - Evidência: “economic pressures that forced two large manufacturing companies to discontinue the 4-day workweek”
  - Não coberto pela evidência: Segundo a imprensa especializada
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 6 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-40` — Referencia(s) citada(s) ['b2139a2621921ffc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-57` — Referencia(s) citada(s) ['be754527b6103806'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-67` — Referencia(s) citada(s) ['de48be3624ddef10'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-72` — Referencia(s) citada(s) ['de48be3624ddef10'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-73` — Referencia(s) citada(s) ['de48be3624ddef10'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_d608d7fd3ef0_20261101T220900Z-82` — Referencia(s) citada(s) ['be754527b6103806'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.