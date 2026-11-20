# Relatório de Auditoria — Gemini (semana_trabalho_ac2200792987_20261101T222041Z)

**Arquivo auditado:** `answers/Gemini/EmConsolidacao/semana_trabalho.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_ac2200792987_20261101T222041Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-01T22:52:26.550730+00:00 |
| **Total de trechos citados** | 126 |
| **Tempo de processamento** | 0:00:31:45 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 2957.4 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-01 22:21:02+00:00 |
| Citações no corpo | 126 marcadores, 17 distintos |
| Referências listadas | 36 (19 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 10 | 7.9% |
| **UNSUPPORTED** | 93 | 73.8% |
| **CONTRADICTED** | 3 | 2.4% |
| **SKIPPED** | 20 | 15.9% |
| **TOTAL** | 126 | 100.0% |

Sobre os 106 trechos citados auditados: SUPPORTED 9,43%, UNSUPPORTED 87,73%, CONTRADICTED 2,83%.

> **3 dos 10 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 3 estão **contados dentro** dos 10 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`95` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `69` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `38` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 1, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#0` A consolidação da jornada de trabalho padrão de 40 horas semanais, distribuídas ao longo de cinco dias, não representa… | [1] | [23] [12] [16] [20] [17] [15] [2] [18] | — |
| `#1` O marco icônico dessa transição ocorreu na década de 1920, quando Henry Ford adotou a semana laboral de cinco dias em s… | [2] | [23] [12] [17] [14] [20] [3] | — |
| `#2` A premissa subjacente à época demonstrava que trabalhadores mais descansados apresentavam maior produtividade industria… | [2] | [12] [20] [23] [10] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [22] | — |
| `#9` Longe de constituir uma mera concessão de folga adicional ou uma regalia corporativa, o modelo representa uma reconfigu… | [1] | [12] [20] [30] [22] [10] [3] [7] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [32] | — |
| `#10` A tese central que fundamenta essa transformação sustenta que a otimização de processos, a redução de fricções operacio… | [1] | [12] [20] [7] [10] [3] | — |
| `#13` A gênese desse modelo remonta a 2018, quando os fundadores Andrew Barnes e Charlotte Lockhart conduziram um ensaio pion… | [2] | [12] [1] [8] [23] [22] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [30] [10] | — |
| `#20` Proteção do trabalho focado (deep work): Adoção de blocos temporais sem interrupções (timeboxing), bloqueando e-mails e… | [1] | [12] [5] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [7] [20] | — |
| `#23` Em setores que demandam atendimento contínuo, aplicam-se escalas alternadas de folga entre os colaboradores, mantendo o… | [2] | [30] [12] [22] [17] [10] [20] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf | — |
| `#30` Em 2022, o Reino Unido sediou o maior piloto coordenado da semana de quatro dias em nível empresarial, organizado pela… | [2] | [23] [12] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [9] [30] [3] [10] [22] [6] | — |
| `#31` O estudo abrangeu 61 empresas e aproximadamente 2.900 trabalhadores de diversos segmentos, desde agências de marketing… | [2] | [23] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [3] [9] [12] [10] [22] [11] [30] [13] | — |
| `#37` No setor privado de alta tecnologia, um dos casos mais emblemáticos ocorreu durante o verão de 2019 na subsidiária da M… | [9] | [27] [29] [28] [25] [24] [12] [10] [20] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [6] | — |
| `#39` A organização impôs o limite máximo de 30 minutos para reuniões presenciais e encorajou fortemente o uso de canais de c… | [9] | [29] [25] [28] [24] [12] [10] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [22] [7] | — |
| `#40` Os resultados operacionais registraram um aumento de 39,9% na produtividade por funcionário, medida pelas vendas efetua… | [9] | [30] [22] [10] [24] [25] [7] [12] [20] [29] [23] [13] | — |
| `#51` Coordenado pelos economistas Pedro Gomes (da Birkbeck University of London) e Rita Fontinha (da Henley Business School)… | [5] | [13] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [10] [12] [11] [23] | — |
| `#52` Financiado e promovido sob a chancela governamental, o projeto não impôs uma fórmula única, permitindo que cada empresa… | [5] | — | [12] [10] [16] [22] [13] [17] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [23] [15] ⚠ |
| `#53` A avaliação final do piloto revelou um índice de satisfação extraordinário: 95% das empresas participantes avaliaram a… | [14] | [11] [10] [22] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [23] [12] [30] [9] | — |
| `#54` Os relatórios apontaram que a produtividade se manteve ou aumentou, impulsionada pelo redesenho de rotinas, otimização… | [5] | [22] [12] [10] [30] [7] [9] [23] | — |
| `#55` Entre os trabalhadores, constataram-se reduções significativas nos níveis de exaustão, ansiedade e problemas de sono, a… | [14] | [11] [10] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [22] [9] [12] [30] [13] [23] [31] | — |
| `#56` No Brasil, o primeiro projeto piloto foi conduzido pela organização Reconnect at Work em parceria direta com a 4 Day We… | [7] | [31] [30] [22] [12] [10] [32] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [3] | — |
| `#70` Os relatos do piloto brasileiro confirmaram que a transição exige flexibilidade e confiança mtua. | [13] | [22] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [32] [10] [12] [3] [30] | — |
| `#71` A maioria das companhias optou por folgas às sextas-feiras por ser um dia historicamente de menor ritmo comercial, enqu… | [12] | [30] [10] [22] [20] [23] | — |
| `#78` Em fevereiro de 2026, as matérias foram apensadas para análise conjunta no Congresso Nacional. | [17] | [16] [31] [14] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [20] [12] [15] [18] | — |
| `#79` O debate legislativo resultou na elaboração de um substitutivo pelo relator, deputado Leo Prates. | [1] | [16] [18] [15] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [20] [31] [12] [14] | — |
| `#80` O texto aprovado pela Câmara dos Deputados e ratificado pelo Senado Federal acabou por aprovar a extinção da escala 6x1… | [1] | [16] [18] [15] [17] [31] [14] [19] [20] | — |
| `#81` Nova Carga Máxima Semanal: Redução do teto constitucional de 44 para 40 horas semanais, mantendo-se o limite diário de… | [1] | [16] [15] [17] [18] [14] [31] [12] | — |
| `#82` Adocao da Escala 5x2: Instituição obrigatória de dois dias de repouso semanal remunerado por semana trabalhada, erradic… | [1] | [16] [15] [17] [14] [18] [31] [12] [19] | — |
| `#83` Proteção Irredutível do Salário: Proibição expressa de qualquer redução salarial nominal, proporcional ou de qualquer o… | [1] | [18] [15] [17] [12] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [20] [16] | — |
| `#84` Cronograma de Transição Gradual: A implementação foi dividida em duas etapas ao longo de 14 meses a partir da promulgaç… | [1] | [17] [16] [18] [15] [12] [31] | — |
| `#87` Exceções e Regimes Diferenciados: Para atividades contínuas ou essenciais (como saúde, segurança pública, transporte e… | [1] | [18] [17] [15] [16] [12] [31] [14] | — |
| `#89` Apoio a Microempresas e MEIs: O texto previu a edição de lei complementar para ajustar os limites do Simples Nacional e… | [1] | — | [18] [17] [12] [21] [15] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [16] ⚠ |
| `#95` No âmbito da igualdade de gênero, os dados empíricos apurados nos pilotos internacionais revelam um efeito redistributi… | [2] | [10] [12] [6] [23] [22] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [30] | — |
| `#96` O estudo conduzido na Australásia e no Reino Unido demonstrou que homens em relacionamentos heterossexuais aumentaram s… | [2] | [8] [12] [10] [30] [22] [9] [20] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [6] [23] | — |
| `#97` Esse movimento atenua a "jornada dupla" historicamente sobrecarregada sobre as mulheres, favorecendo a equidade de opor… | [2] | [12] [20] [14] [6] [16] [10] [15] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [17] | — |
| `#106` Nesses segmentos, a eliminação de ineficiências e o ganho de foco cobrem com facilidade as horas reduzidas. | [1] | — | [20] [30] [12] [10] [7] [11] [22] [32] [8] ⚠ |
| `#115` A validação da metodologia 100:80:100™ comprova que é possível manter ou elevar o desempenho corporativo, proteger as r… | [1] | [30] [12] [7] [32] [5] [3] [22] [8] [10] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf | — |
| `#117` Diagnóstico e Redesenho Prévio de Processos: As empresas devem realizar um diagnóstico profundo de seus processos inter… | [1] | [12] [10] [7] [23] | — |
| `#119` Flexibilidade e Coconstrução de Escalas: A definição da jornada reduzida não deve ser imposta de forma rígida ou unilat… | [2] | [16] [20] [17] [22] [18] [12] [32] [15] | — |
| `#120` Lideranças e colaboradores devem coconstruir as soluções mais adequadas à realidade de cada setor, definindo se a folga… | [2] | [12] [22] [18] [17] [30] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [20] [10] [14] | — |
| `#122` É essencial estabelecer métricas claras de desempenho (KPIs), acompanhar indicadores de saúde mental e realizar ajustes… | [2] | [12] [10] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [22] [7] | — |
| `#124` A semana de quatro dias não representa uma utopia trabalhista ou uma simples redução da carga de trabalho, mas sim um p… | [1] | [12] [10] [7] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf [22] [20] | — |
| `#125` Ao alinhar a inteligência operacional ao bem-estar biológico e psicológico do trabalhador, a semana de quatro dias rede… | [1] | [12] [20] [30] [7] [22] [10] [3] [6] [8] https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1625402 |
| **Média de tokens por requisição** | 15334.0 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 19/36 (52.8%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 8.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.4dayweek.com/news-posts/100-80-100-rule-mwmb7) | downloaded | 34 | 2 | 9 | 23 | 0 |
| [[2]](https://www.uts.edu.au/case-studies/mythbusting-four-day-work-week) | downloaded | 22 | 1 | 4 | 17 | 0 |
| [[4]](https://en.wikipedia.org/wiki/Four-day_workweek) | inaccessible | 20 | 0 | 0 | 0 | 20 |
| [[3]](https://disprz.ai/blog/4-day-work-week-experiment-impact) | downloaded | 16 | 2 | 7 | 7 | 0 |
| [[5]](https://www.nirandfar.com/4-day-workweek/) | downloaded | 7 | 0 | 1 | 6 | 0 |
| [[9]](https://www.sociology.cam.ac.uk/news/new-results-worlds-largest-trial-four-day-working-week) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[16]](https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[7]](https://www.4dayweek.com/) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[10]](https://rhmagazine.pt/95-das-empresas-avaliam-positivamente-o-projeto-piloto-da-semana-de-quatro-dias/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[11]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[14]](https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[17]](https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[18]](https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[8]](https://leadership.global/insights/news-trends-insights/how-the-four-day-week-model-boosts-employees-happiness/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[12]](https://www.iefp.pt/documents/10181/11729755/Relatorio1Fase_Final.pdf/13cf9e6c-50f7-4830-a822-c1d443f36f31) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[13]](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[15]](https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[6]](https://www.michaelpage.com.tr/en/advice/career-advice/4-day-work-week-guide) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://www.jota.info/opiniao-e-analise/colunas/democracia-em-transe/fim-da-escala-6x1-conecta-lula-a-trabalhadores-e-muda-rumo-da-campanha-eleitoral) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://popularmais.com.br/noticia/25530/sindicatos-fortes-sao-condicao-para-um-brasil-mais-justo-e-produtivo/amp) | downloaded | 0 · nunca citada | — | — | — | — |
| [[21]](https://eco.sapo.pt/2022/07/01/valencia-da-5-500-euros-por-trabalhar-as-empresas-que-implementem-semana-de-quatro-dias/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[22]](https://csb.org.br/noticias/semana-4-dias-de-trabalho-na-alemanha-teste) | downloaded | 0 · nunca citada | — | — | — | — |
| [[23]](https://g1.globo.com/trabalho-e-carreira/noticia/2023/02/27/semana-de-4-dias-o-que-experiencias-mostram-sobre-futuro-do-trabalho.ghtml) | downloaded | 0 · nunca citada | — | — | — | — |
| [[24]](https://bigthink.com/the-present/four-day-work/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[25]](https://www.weforum.org/stories/jobs-and-the-future-of-work/microsoft-4-day-work-week-productivity-increase/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://japantoday.com/category/business/microsoft-japan%E2%80%99s-experiment-with-3-day-weekend-boosts-worker-productivity-by-40) | blocked | 0 · nunca citada | — | — | — | — |
| [[27]](https://www.theguardian.com/technology/2019/nov/04/microsoft-japan-four-day-work-week-productivity) | downloaded | 0 · nunca citada | — | — | — | — |
| [[28]](https://time.com/5717401/microsoft-4-day-workweek/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[29]](https://4dayweek.io/case-study/microsoft) | downloaded | 0 · nunca citada | — | — | — | — |
| [[30]](https://sindishopping.com.br/semana-de-4-dias-empresas-que-participam-de-teste-no-brasil-ja-notam-resultados-positivos/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://4dayweek.io/country/brazil) | downloaded | 0 · nunca citada | — | — | — | — |
| [[32]](https://portal.fgv.br/en/noticias/estudo-indica-que-semana-de-quatro-dias-exige-confianca-e-flexibilidade-para-gerar-resultados) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://support.google.com/knowledgepanel/answer/9787176](https://support.google.com/knowledgepanel/answer/9787176) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://recipp.ipp.pt/bitstreams/34066234-3582-4f47-907a-142a99dead62/download](https://recipp.ipp.pt/bitstreams/34066234-3582-4f47-907a-142a99dead62/download) | blocked | 0 · nunca citada | — | — | — | — |
| [https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf](https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.adcoesao.pt/wp-content/uploads/guia_para_a_avaliacao.pdf](https://www.adcoesao.pt/wp-content/uploads/guia_para_a_avaliacao.pdf) | error | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.4dayweek.com/news-posts/100-80-100-rule-mwmb7) | #12, #16 | #4, #9–11, #17, #106, #114–115, #124 | #0, #3, #5, #8, #18, #20, #79–84, #87–89, #105, #111, #113, #117–118, #121, #123, #125 | `#12` The 100:80:100™ model refers to 100% pay for 80% of your time while maintaining 100% output. |
| [[2]](https://www.uts.edu.au/case-studies/mythbusting-four-day-work-week) | #22 | #95, #97, #119, #122 | #1–2, #13–15, #23–24, #30–32, #34, #92–94, #96, #120, #33 ⚡ | `#22` Implementation of the four-day work week was far from offering everyone a long weekend, with Unilever NZ employees opting to take the time out at different poi… |
| [[3]](https://disprz.ai/blog/4-day-work-week-experiment-impact) | #104, #109 | #27–28, #50, #98, #102–103, #108 | #25–26, #29, #45, #99, #101, #107 | `#104` ### **Not Suitable for All Industries** Certain sectors, such as emergency services, public transport networks, and logistics, necessitate a seven-day-a-week p… |
| [[5]](https://www.nirandfar.com/4-day-workweek/) | — | #54 | #21, #35–36, #51–52, #112 | `#54` Employees received 100 percent of their pay for working 80 percent of the time at 100 percent of the productivity. |
| [[9]](https://www.sociology.cam.ac.uk/news/new-results-worlds-largest-trial-four-day-working-week) | — | — | #37–40, #42 ⚡ | `#42` some 92% of companies that took part in the UK pilot programme (56 out of 61) say they intend to continue with the four-day working week |
| [[16]](https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/) | #74–76 | #72, #116 | — | `#74` A aprovação da Proposta de Emenda à Constituição (PEC) que acaba com a escala 6x1, na noite da última quarta-feira, 14, é resultado de iniciativas que tramitar… |
| [[7]](https://www.4dayweek.com/) | — | — | #56–57, #90 | — |
| [[10]](https://rhmagazine.pt/95-das-empresas-avaliam-positivamente-o-projeto-piloto-da-semana-de-quatro-dias/) | — | — | #41, #100 | — |
| [[11]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | — | — | #48–49 | — |
| [[14]](https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1) | — | — | #53, #55 | — |
| [[17]](https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/) | #86 | — | #78 | `#86` 14 meses após a promulgação: a jornada máxima será reduzida definitivamente para 40 horas semanais. |
| [[18]](https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais) | #85 | — | #73 | `#85` Depois de dois meses da publicação da futura emenda constitucional, já valerão os dois dias de descanso remunerado por semana, um dos quais preferencialmente a… |
| [[8]](https://leadership.global/insights/news-trends-insights/how-the-four-day-week-model-boosts-employees-happiness/) | — | — | #19 | — |
| [[12]](https://www.iefp.pt/documents/10181/11729755/Relatorio1Fase_Final.pdf/13cf9e6c-50f7-4830-a822-c1d443f36f31) | — | #71 | — | `#71` Fecho ao 5º dia. A empresa encerra as operações por um dia adicional por semana. Esta é a escolha mais popular em empresas onde a colaboração da equipa é mais… |
| [[13]](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | — | — | #70 | — |
| [[15]](https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/) | — | — | #77 ⚡ | `#77` De autoria do deputado federal Reginaldo Lopes (PT-MG), a PEC 221/2019 foi aprovada por maioria esmagadora na Câmara dos Deputados em maio |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://en.wikipedia.org/wiki/Four-day_workweek — Rate limit persistente em https://en.wikipedia.org/wiki/Four-day_workweek

### Bloqueadas por barreira de acesso

- https://japantoday.com/category/business/microsoft-japan%E2%80%99s-experiment-with-3-day-weekend-boosts-worker-productivity-by-40 — no_content — barreira de acesso (no_content): Powered and protected by Privacy
- https://recipp.ipp.pt/bitstreams/34066234-3582-4f47-907a-142a99dead62/download — anti_bot — barreira de acesso (anti_bot): # Making sure you're not a bot! RCAAP – Repositórios Científicos de Acesso Aberto de Portugal Calculating... Difficulty:

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-12`** [1]
  - Trecho: A equação fundamental do modelo estabelece a manutenção de 100% da remuneração e dos benefícios do trabalhador, em troca de 80% do tempo de trabalho semanal anterior, sob o compromisso irredutível de entregar 100% dos r…
  - Justificativa: A evidência confirma explicitamente a equação central do modelo 100:80:100™: 100% da remuneração (pay) por 80% do tempo, mantendo 100% da produtividade (output). O conceito fundamental está sustentado. No entanto, a men…
  - Suporte veio de: [1]
  - Evidência: “The 100:80:100™ model refers to 100% pay for 80% of your time while maintaining 100% output.”
  - Não coberto pela evidência: manutenção de 'benefícios do trabalhador' — a evidência menciona apenas 'pay' (remuneração), sem referenciar benefícios; termo 'compromisso irredutível' — a evidência usa 'crucial', linguagem menos forte que 'irredutível'; 'resultados produtivos acordados' — a evidência fala em 'output' mas não especifica que sejam 'acordados'
  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência confirma a essência do modelo 100:80:100™ (100% de remuneração por 80% do tempo, mantendo 100% da produção), mas não menciona '…") — cascata: baseline → context_expansion
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-16`** [1]
  - Trecho: A viabilização do modelo 100:80:100™ baseia-se na premissa de que tempo não é sinônimo de produtividade.
  - Justificativa: A evidência afirma que 'output is more important than the time they take to complete it', o que sustenta diretamente a premissa de que tempo não é sinônimo de produtividade. O modelo 100:80:100™ (100% pay, 80% time, 100…
  - Suporte veio de: [1]
  - Evidência: “When you tell your employees that their output is more important than the time they take to complete it, then they will be more focused and therefore, more productive.”
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-22`** [2]
  - Trecho: Modelos de cobertura e escalas flexíveis: A semana de quatro dias não exige o fechamento da empresa às sextas-feiras.
  - Justificativa: A evidência mostra que a semana de quatro dias na Unilever NZ não significava um longo fim de semana para todos, pois os funcionários escolhiam tirar o dia livre em diferentes momentos da semana. Isso sustenta a afirmaç…
  - Suporte veio de: [2]
  - Evidência: “Implementation of the four-day work week was far from offering everyone a long weekend, with Unilever NZ employees opting to take the time out at different points throughout the week or when they could.”
### UNSUPPORTED

- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-0`** [1]
  - Trecho: A consolidação da jornada de trabalho padrão de 40 horas semanais, distribuídas ao longo de cinco dias, não representa uma constante imutável da natureza produtiva, mas sim um arranjo institucional e histórico estabelec…
  - Justificativa: A evidência trata apenas da implementação do modelo de semana de 4 dias (100:80:100™), suas origens em 2018 e exemplos de pilotos. Não há qualquer menção à história da jornada de 40 horas semanais em 5 dias, nem à sua c…
  - Não coberto pela evidência: Consolidação da jornada de 40 horas semanais distribuídas em cinco dias; Arranjo institucional e histórico; Estabelecimento no início do século XX
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [23] [12] [16] [20] [17] [15] [2] [18] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-1`** [2]
  - Trecho: O marco icônico dessa transição ocorreu na década de 1920, quando Henry Ford adotou a semana laboral de cinco dias em suas linhas de montagem automotivas, substituindo a escala comum de seis dias de trabalho.
  - Justificativa: A evidência trata exclusivamente do experimento de semana de quatro dias da Unilever Nova Zelândia. Não há qualquer menção a Henry Ford, à década de 1920, à semana de cinco dias ou à substituição da escala de seis dias.…
  - Não coberto pela evidência: Henry Ford como responsável pela adoção da semana de cinco dias; década de 1920 como marco temporal; substituição da escala de seis dias de trabalho pela de cinco dias
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [23] [12] [17] [14] [20] [3] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-2`** [2]
  - Trecho: A premissa subjacente à época demonstrava que trabalhadores mais descansados apresentavam maior produtividade industrial e dispunham de tempo livre para consumir bens, alimentando a própria engrenagem econômica.
  - Justificativa: A evidência trata apenas do estudo de caso da Unilever Nova Zelândia sobre a semana de trabalho de quatro dias, mencionando produtividade e bem-estar dos funcionários, mas não aborda a premissa histórica de que trabalha…
  - Não coberto pela evidência: Premissa subjacente à época sobre trabalhadores mais descansados e maior produtividade industrial; Tempo livre para consumir bens; Alimentação da própria engrenagem econômica pelo consumo
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [12] [20] [23] [10] 0a00cd82a998f1ed [22] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-33`** [2]
  - Trecho: Sob a ótica da retenção e assiduidade, observou-se uma redução de 65% nos dias de baixa médica e uma queda de 57% na rotatividade de funcionários (turnover) em relação a períodos anteriores.
  - Justificativa: A janela afirma que o absenteísmo foi 'significantly reduced' (sem indicar 65%) e que o turnover foi 'stable', o que contradiz diretamente a alegação de uma queda de 57% na rotatividade. A janela não confirma os números…
  - Evidência: “Absenteeism was also significantly reduced, turnover was stable, and all other employee outcome metrics were stable or showed directional improvement.”
  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "O trecho afirma reduções específicas de 65% nos dias de baixa médica e 57% na rotatividade, mas a evidência não contém nenhum desses número…") — cascata: baseline → context_expansion → full_doc_scan
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-42`** [9]
  - Trecho: A aprovação dos trabalhadores atingiu 92% em pesquisas internas.
  - Justificativa: A evidência menciona 92%, mas se refere a empresas (92% das empresas pretendem continuar com a semana de quatro dias), não à aprovação dos trabalhadores em pesquisas internas. A afirmação atribui incorretamente o número…
  - Evidência: “some 92% of companies that took part in the UK pilot programme (56 out of 61) say they intend to continue with the four-day working week”
  - Não coberto pela evidência: aprovação dos trabalhadores; pesquisas internas
- **Trecho citado `semana_trabalho_ac2200792987_20261101T222041Z-77`** [15]
  - Trecho: Simultaneamente, tramitava na Câmara dos Deputados a PEC 221/2019, de autoria do deputado Reginaldo Lopes (PT-MG), que propunha a redução gradual da jornada de 44 para 36 horas semanais ao longo de um período de transiç…
  - Justificativa: A evidência confirma a autoria (Reginaldo Lopes, PT-MG) e a tramitação na Câmara dos Deputados da PEC 221/2019. Porém, contradiz a afirmacao quanto ao objetivo e ao prazo: a evidência indica redução de 44 para 40 horas…
  - Evidência: “De autoria do deputado federal Reginaldo Lopes (PT-MG), a PEC 221/2019 foi aprovada por maioria esmagadora na Câmara dos Deputados em maio”
  - Não coberto pela evidência: redução para 36 horas semanais (evidência indica 40 horas); período de transição de dez anos (evidência indica aproximadamente 14 meses)

---

## 10. Trechos Citados Não Auditados

Motivos: 20 citam referência não baixada/inacessível.

- `semana_trabalho_ac2200792987_20261101T222041Z-6` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-7` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-43` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-44` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-46` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-47` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-58` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-59` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-60` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-61` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-62` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-63` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-64` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-65` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-66` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-67` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-68` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-69` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-91` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_ac2200792987_20261101T222041Z-110` — Referencia(s) citada(s) ['29cf52756bba7b06'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).