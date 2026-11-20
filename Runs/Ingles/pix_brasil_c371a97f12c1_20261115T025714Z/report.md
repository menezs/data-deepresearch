# Relatório de Auditoria — Claude (pix_brasil_c371a97f12c1_20261115T025714Z)

**Arquivo auditado:** `answers/Ingles/Claude/EmConsolidacao/pix_brasil.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | pix_brasil_c371a97f12c1_20261115T025714Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T03:24:10.985951+00:00 |
| **Total de trechos citados** | 76 |
| **Tempo de processamento** | 0:00:26:57 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 27.0 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 92 marcadores, 40 distintos |
| Referências listadas | 40 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 58 | 76.3% |
| **UNSUPPORTED** | 17 | 22.4% |
| **CONTRADICTED** | 1 | 1.3% |
| **TOTAL** | 76 | 100.0% |

Sobre os 76 trechos citados auditados: SUPPORTED 76,31%, UNSUPPORTED 22,36%, CONTRADICTED 1,31%.

> **21 dos 58 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 21 estão **contados dentro** dos 58 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`23` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `7` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` Quasi-experimental studies find that Pix reshuffled deposits mainly among the already banked, pushed banks to hold more… | [5] [6] [7] | [27] [1] | — |
| `#5` It built the platform, runs the settlement system and keeps the directory of payment aliases, a combination that sets P… | [1] [12] | [14] [27] [40] [7] [6] | — |
| `#46` Persistent informality fits the IPA finding that small firms run sales through personal keys: Pix lets informal busines… | [26] | [1] [7] [27] | — |
| `#56` No data on MED 2.0's results appeared in the sources. Privacy adds exposure, because Pix turns personal identifiers int… | [35] | [34] [2] [1] [33] [5] [6] [7] [14] [24] [28] | — |
| `#59` For these groups cash remains the default even as its infrastructure shrinks: bank branches fell 14.6% between 2020 and… | [24] | [7] [6] [20] [1] [5] [16] [27] | — |
| `#70` PIIE's Monica de Bolle argues that a public payment system is not a trade barrier and that the deeper risk is sanctions… | [11] | [40] [1] [28] [14] [27] [13] [7] [6] [12] | — |
| `#74` Researchers disagree on whether Pix expands lending, and regulators have declined to set rules for the credit products… | [28] [10] | [1] [7] [40] [27] [6] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1517624 |
| **Média de tokens por requisição** | 19968.7 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/40 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[24]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RIF/relatorio_de_cidadania_financeira_2025.pdf) | downloaded | 7 | 2 | 5 | 0 | 0 |
| [[1]](https://www.bcb.gov.br/content/publicacoes/WorkingPaperSeries/WP600.pdf) | downloaded | 6 | 5 | 0 | 1 | 0 |
| [[4]](https://www.infomoney.com.br/?p=1952024) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[10]](https://www.opovo.com.br/noticias/economia/2025/12/04/apos-adiamentos-banco-central-desiste-de-regular-pix-parcelado.html) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[16]](https://eaesp.fgv.br/sites/default/files/arq-publicacao/2026-08/5-anos-do-pix-10-perguntas-para-entender-como-ele-se-espalhou-pelo-brasil-1.pdf) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[6]](https://www.sipa.columbia.edu/sites/default/files/2026-02/liangetal%20%282%29.pdf) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[7]](https://arxiv.org/pdf/2608.13871) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[23]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/serie_cidadania/serie_cidadania_financeira_7_Global_Findex.pdf) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[3]](https://legismap.com.br/conteudos/artigos-e-noticias/noticias-bc-em-07-04-2026) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[8]](https://brasil61.com/n/anuario-de-seguranca-publica-brasil-registrou-mais-de-2-2-milhoes-de-casos-de-estelionato-em-2025-bras2616801) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[9]](https://cetic.br/media/analises/tic_domicilios_2025_principais_resultados.pdf) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[11]](https://www.piie.com/blogs/realtime-economics/2026/latest-us-squeeze-brazil-jeopardizes-its-financial-autonomy) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[12]](https://www.cgap.org/blog/comparing-indias-upi-and-brazils-new-instant-payment-system-pix) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[2]](https://legismap.com.br/conteudos/artigos-e-noticias/bc-divulga-relatorio-de-gestao-do-pix-2023-2025-e-apresenta-agenda-de-evolucao-para-os-proximos-anos) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[5]](https://economics.princeton.edu/wp-content/uploads/2025/03/instant_payments-_Sergey_Sarkisyan.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[26]](https://poverty-action.org/what-brazils-micro-and-small-businesses-reveal-about-future-digital-finance) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[27]](https://bcb.gov.br/content/publicacoes/WorkingPaperSeries/WP619.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[28]](https://theses-dissertations.princeton.edu/entities/publication/45bb0572-3206-480a-951d-4591fd48c50f) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[32]](https://agenciabrasil.ebc.com.br/economia/noticia/2025-08/pix-novas-regras-vao-facilitar-devolucao-de-valores-em-casos-de-golpe) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[34]](https://forbes.com.br/forbes-money/2026/02/med-2-0-do-bc-entra-em-vigor-e-permite-bloqueio-de-pix-fraudulento-entenda-regras/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[38]](https://www.contabeis.com.br/noticias/69122/pix-retoma-crescimento-apos-polemica-de-fiscalizacao/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[40]](https://thenextweb.com/news/brazil-us-pix-trade-clash) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[13]](https://www.bis.org/publ/bisbull52.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[14]](https://www.bis.org/review/r250703g.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[15]](https://portaldeprefeitura.com.br/brasil/pix-por-aproximacao-nova-modalidade-e-lancada-nesta-sexta-28/590177/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[17]](https://metropoles.com/brasil/pix-bate-recorde-em-2025-e-movimenta-r-354-trilhoes) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[18]](https://mercadoeconsumo.com.br/09/10/2026/meios-de-pagamento/pix-ultrapassa-1-bilhao-de-chaves-cadastradas-no-brasil/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[19]](https://economicnewsbrasil.com.br/2026/11/09/recorde-do-pix-movimentacao-consumo/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://finsidersbrasil.com.br/pagamentos/fintechs-ja-dominam-metade-das-transacoes-feitas-no-pix-diz-bc/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[21]](https://www.infomoney.com.br/?p=1824394) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://www.contabeis.com.br/noticias/48957/pix-foi-ferramenta-de-1a-transferencia-bancaria-de-cerca-de-40-milhoes-de-pessoas/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[25]](https://www.infomoney.com.br/minhas-financas/pix-e-usado-por-71-dos-brasileiros-taxa-de-aprovacao-chega-a-99-entre-jovens-indica-pesquisa-da-febraban/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[29]](https://www.povertyactionlab.org/initiative-project/impact-instant-payment-systems-financial-and-labor-market-outcomes-evidence-pix) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[30]](https://www12.senado.leg.br/radio/1/noticia/2025/08/18/mais-de-24-milhoes-de-pessoas-foram-vitimas-de-golpes-pelo-pix) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://olhardigital.com.br/2024/11/01/pro/novas-regras-do-pix-ja-estao-valendo-saiba-o-que-muda/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.infomoney.com.br/minhas-financas/med-2-0-passa-a-ser-obrigatorio-em-todas-as-plataformas-que-oferecem-pix/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[35]](https://finsidersbrasil.com.br/pagamentos/bc-comunica-terceiro-vazamento-de-chaves-pix-no-ano-incidente-atingiu-financeira-da-pernambucanas/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[36]](https://www.suno.com.br/noticias/?p=612244) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://diariodonordeste.verdesmares.com.br/negocios/bc-cria-teto-de-r-15-mil-para-pix-apos-ataques-do-crime-organizado-veja-outras-mudancas-1.3687918) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://www.opovo.com.br/noticias/economia/2025/01/15/amp/apos-onda-de-criticas-e-desinformacao-receita-recua-de-fiscalizacao-do-pix.html) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[24]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RIF/relatorio_de_cidadania_financeira_2025.pdf) | #32–33 | #29, #31, #37, #59, #72 | — | `#32` em dezembro de 2023 – três anos após o lançamento do Pix –, 74% dos adultos inscritos no CadÚnico haviam registrado ao menos uma chave Pix, evidenciando a ampl… |
| [[1]](https://www.bcb.gov.br/content/publicacoes/WorkingPaperSeries/WP600.pdf) | #0, #6, #8, #21, #40 | — | #5 | `#0` Pix, the new instantaneous bank transfer launched in November 2020 by the Central Bank of Brazil (BCB) [...] it became the most popular transaction method in B… |
| [[4]](https://www.infomoney.com.br/?p=1952024) | #2, #24–25 | #34, #37, #71 | — | `#2` Desses, **49 milhões passaram a fazer transferências após o lançamento do sistema de pagamentos do BC** |
| [[10]](https://www.opovo.com.br/noticias/economia/2025/12/04/apos-adiamentos-banco-central-desiste-de-regular-pix-parcelado.html) | #61–62 | #4, #74 | #12 | `#61` O Idec destaca que, por estar associado à marca mais confiável do sistema financeiro brasileiro, o Pix parcelado tende a induzir decisões impulsivas. |
| [[16]](https://eaesp.fgv.br/sites/default/files/arq-publicacao/2026-08/5-anos-do-pix-10-perguntas-para-entender-como-ele-se-espalhou-pelo-brasil-1.pdf) | #15, #35–36, #38 | #37 | — | `#15` 100% 90,9%<br>86,0%<br>90%<br>77,3%<br>80%<br>66,0%<br>70%<br>60%<br>49,5%<br>50%<br>40%<br>30%<br>20%<br>6,2%<br>10%<br>0%<br>nov./2020 nov./2021 nov./2022 no… |
| [[6]](https://www.sipa.columbia.edu/sites/default/files/2026-02/liangetal%20%282%29.pdf) | #43, #60 | #3, #47 | — | `#43` Pauline Liang Matheus Sampaio Sergey Sarkisyan [...] Number of branches declines in high-Pix areas [...] Number of bank accounts rises Sampaio and Ornelas (202… |
| [[7]](https://arxiv.org/pdf/2608.13871) | #44–45 | #3, #47 | — | `#44` The triple interaction coefficient is 0.003, indicating that a one-standard-deviation increase in mobile penetration leads to a 0.3 percent [...] monthly wage… |
| [[23]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/serie_cidadania/serie_cidadania_financeira_7_Global_Findex.pdf) | #27–28, #30, #75 | — | — | `#27` aumentando de 68% para 70%, a pesquisa indicou um crescimento de 14 p.p. entre 2017 e 2021, período em que a quantidade de adultos detentores de conta em insti… |
| [[3]](https://legismap.com.br/conteudos/artigos-e-noticias/noticias-bc-em-07-04-2026) | #19–20 | #1 | — | `#19` responsável por 54,7% das transações efetuadas no segundo semestre de 2025, atingindo 42,9 bilhões de transações naquele período. [...] O instrumento de pagame… |
| [[8]](https://brasil61.com/n/anuario-de-seguranca-publica-brasil-registrou-mais-de-2-2-milhoes-de-casos-de-estelionato-em-2025-bras2616801) | #50 | #4, #49 | — | `#50` Pelo anuário, é provável que os registros policiais revelem uma subnotificação. Os pesquisadores citam uma pesquisa produzida pelo FBSP em março de 2026 que mo… |
| [[9]](https://cetic.br/media/analises/tic_domicilios_2025_principais_resultados.pdf) | #57–58 | #4 | — | `#57` 28 milhões de pessoas não usuárias de Internet \| De 60 anos ou mais 16 mi \| DE 14 mi \| Fez pagamento ou transferência por Pix INÉDITO |
| [[11]](https://www.piie.com/blogs/realtime-economics/2026/latest-us-squeeze-brazil-jeopardizes-its-financial-autonomy) | #68 | #4, #70 | — | `#68` Announcing the June 1 Section 301 determination, Greer said those talks had 'accelerated in recent weeks' but that 'substantial differences' remained. [...] Th… |
| [[12]](https://www.cgap.org/blog/comparing-indias-upi-and-brazils-new-instant-payment-system-pix) | #7, #10 | #5 | — | `#7` PIX launched with a prohibition on any customer fee but allows acquirers to charge merchant fees without any limitation. There is also no interchange set by PI… |
| [[2]](https://legismap.com.br/conteudos/artigos-e-noticias/bc-divulga-relatorio-de-gestao-do-pix-2023-2025-e-apresenta-agenda-de-evolucao-para-os-proximos-anos) | #14 | #1 | — | `#14` o lançamento do Pix Automático, que passou a permitir pagamentos recorrentes mediante autorização única do usuário |
| [[5]](https://economics.princeton.edu/wp-content/uploads/2025/03/instant_payments-_Sergey_Sarkisyan.pdf) | #41 | #3 | — | `#41` Pix increases payment and transfer convenience of small banks - Increase in small bank deposits stronger in richer areas - The results are mostly driven by alr… |
| [[26]](https://poverty-action.org/what-brazils-micro-and-small-businesses-reveal-about-future-digital-finance) | #39 | #46 | — | `#39` 96 percent of respondents use Pix for either business or personal reasons, and nearly half use it daily. [...] 71 percent of those who use Pix for business rep… |
| [[27]](https://bcb.gov.br/content/publicacoes/WorkingPaperSeries/WP619.pdf) | #42 | #47 | — | `#42` we construct our timeout instrument for a given bank i in month t only using variation in timeouts induced by other banks j = i. [...] A one-standard-deviation… |
| [[28]](https://theses-dissertations.princeton.edu/entities/publication/45bb0572-3206-480a-951d-4591fd48c50f) | — | #47 | #74 | `#47` I find that a 1% increase in Pix transactions per person over 15 resulted in a 0.14% increase in access to credit |
| [[32]](https://agenciabrasil.ebc.com.br/economia/noticia/2025-08/pix-novas-regras-vao-facilitar-devolucao-de-valores-em-casos-de-golpe) | #53 | #54 | — | `#53` A partir de 1º de outubro, o MED passa a ser feito de forma 100% digital, sem a necessidade de interação com o atendimento da instituição financeira. Todos os… |
| [[34]](https://forbes.com.br/forbes-money/2026/02/med-2-0-do-bc-entra-em-vigor-e-permite-bloqueio-de-pix-fraudulento-entenda-regras/) | #55, #73 | — | — | `#55` Por isso, a taxa média de recuperação de recursos ficava em torno de 7%, de acordo com o BC. |
| [[38]](https://www.contabeis.com.br/noticias/69122/pix-retoma-crescimento-apos-polemica-de-fiscalizacao/) | #66 | #65 | — | `#66` Entre os dias 1º e 14, foram realizadas 2,29 bilhões de transferências, o número mais baixo desde julho de 2023. [...] Após revogar a norma sobre fiscalização… |
| [[40]](https://thenextweb.com/news/brazil-us-pix-trade-clash) | #67 | #69 | — | `#67` In its Section 301 review, USTR argued that Brazil's central bank holds a conflict of interest by acting as both the regulator and the operator of Pix, and tha… |
| [[13]](https://www.bis.org/publ/bisbull52.htm) | #9 | — | — | `#9` In little over a year since its launch in November 2020, Pix has signed up 67% of adults in Brazil [...] The two key ingredients in the success of Pix are, fir… |
| [[14]](https://www.bis.org/review/r250703g.htm) | — | #11 | — | `#11` Designed as a public, open instant payments platform, Pix quickly transformed Brazil's payments landscape. |
| [[15]](https://portaldeprefeitura.com.br/brasil/pix-por-aproximacao-nova-modalidade-e-lancada-nesta-sexta-28/590177/) | #13 | — | — | `#13` A partir desta sexta-feira, 28 de fevereiro, todas as instituições financeiras deverão oferecer a opção de transferência via Pix por aproximação, que elimina a… |
| [[17]](https://metropoles.com/brasil/pix-bate-recorde-em-2025-e-movimenta-r-354-trilhoes) | #16 | — | — | `#16` as transferências via Pix bateram recorde em 2025 e movimentaram R$ 35,36 trilhões. Foram feitas quase 80 bilhões de transações bancárias no período. Em compar… |
| [[18]](https://mercadoeconsumo.com.br/09/10/2026/meios-de-pagamento/pix-ultrapassa-1-bilhao-de-chaves-cadastradas-no-brasil/) | — | #17 | — | `#17` O número de chaves Pix cadastradas no Brasil ultrapassou a marca de 1 bilhão em setembro, segundo dados do Banco Central (BC). Ao todo, o sistema contabilizava… |
| [[19]](https://economicnewsbrasil.com.br/2026/11/09/recorde-do-pix-movimentacao-consumo/) | #18 | — | — | `#18` O **recorde do Pix**, registrado em 6 de novembro de 2026, levou o sistema de pagamentos instantâneos a processar **319,7 milhões de transações, que movimentar… |
| [[21]](https://www.infomoney.com.br/?p=1824394) | #23 | — | — | `#23` de coautoria de economistas do Banco Central do Brasil para o Banco de Compensações Internacionais (BIS), o Pix tem um custo médio de 0,22% por transação para… |
| [[22]](https://www.contabeis.com.br/noticias/48957/pix-foi-ferramenta-de-1a-transferencia-bancaria-de-cerca-de-40-milhoes-de-pessoas/) | — | #26 | — | `#26` Cerca de 40 milhões de pessoas no Brasil fizeram sua primeira transferência bancária por meio do Pix. O dado foi divulgado pelo diretor de Organização do Siste… |
| [[25]](https://www.infomoney.com.br/minhas-financas/pix-e-usado-por-71-dos-brasileiros-taxa-de-aprovacao-chega-a-99-entre-jovens-indica-pesquisa-da-febraban/) | — | #34 | — | `#34` O Pix... já é usado por 71% dos brasileiros... pesquisa da Federação Brasileira de Bancos (Febraban)... no grupo de pessoas com renda de até dois salários míni… |
| [[29]](https://www.povertyactionlab.org/initiative-project/impact-instant-payment-systems-financial-and-labor-market-outcomes-evidence-pix) | — | #48 | — | `#48` The Impact of Instant Payment Systems on Financial and Labor Market Outcomes: Evidence from Pix |
| [[30]](https://www12.senado.leg.br/radio/1/noticia/2025/08/18/mais-de-24-milhoes-de-pessoas-foram-vitimas-de-golpes-pelo-pix) | #51 | — | — | `#51` Entre julho de 2024 e junho de 2025, cerca de 24 milhões de brasileiros foram vítimas de golpes financeiros envolvendo PIX ou boletos bancários, resultando em… |
| [[31]](https://olhardigital.com.br/2024/11/01/pro/novas-regras-do-pix-ja-estao-valendo-saiba-o-que-muda/) | #52 | — | — | `#52` será permitido transferir apenas até R$ 200 por transação e um total diário de R$ 1.000 a partir de celulares e computadores não reconhecidos pelo sistema. O B… |
| [[33]](https://www.infomoney.com.br/minhas-financas/med-2-0-passa-a-ser-obrigatorio-em-todas-as-plataformas-que-oferecem-pix/) | — | #54 | — | `#54` A partir de desta segunda-feira, 2 de fevereiro, todas as instituições financeiras e de pagamento... passam a ser obrigadas a adotar o MED 2.0... Apesar da obr… |
| [[35]](https://finsidersbrasil.com.br/pagamentos/bc-comunica-terceiro-vazamento-de-chaves-pix-no-ano-incidente-atingiu-financeira-da-pernambucanas/) | — | #56 | — | `#56` Desde o lançamento do sistema de pagamento instantâneo, em novembro de 2020, foram reportados 23 casos. |
| [[36]](https://www.suno.com.br/noticias/?p=612244) | #63 | — | — | `#63` Um ataque hacker à empresa brasileira de tecnologia C&M Software afetou a operação de instituições financeiras conectadas ao Pix e pode ter causado o desvio de… |
| [[37]](https://diariodonordeste.verdesmares.com.br/negocios/bc-cria-teto-de-r-15-mil-para-pix-apos-ataques-do-crime-organizado-veja-outras-mudancas-1.3687918) | #64 | — | — | `#64` o BC limitou em R$ 15 mil o valor máximo de TEDs e Pix realizados por instituições de pagamento não autorizadas e pelas que se conectam à rede por meio de Pres… |
| [[39]](https://www.opovo.com.br/noticias/economia/2025/01/15/amp/apos-onda-de-criticas-e-desinformacao-receita-recua-de-fiscalizacao-do-pix.html) | #65 | — | — | `#65` As novas regras colocavam uma lupa sobre movimentações de Pix a partir de R$ 5 mil para pessoas físicas e R$ 15 mil para pessoas jurídicas. [...] Desde o iníci… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-0`** [1]
  - Trecho: Pix, the instant payment system that the Banco Central do Brasil (BCB) built and launched in November 2020, has become the dominant way Brazilians move money, and its clearest contribution to financial inclusion lies in…
  - Justificativa: Os elementos factuais da afirmação são explicitamente sustentados pela evidência: (1) Pix foi lançado pelo BCB em novembro de 2020; (2) tornou-se o método de pagamento mais popular no Brasil, superando o dinheiro; (3) a…
  - Suporte veio de: [1]
  - Evidência: “Pix, the new instantaneous bank transfer launched in November 2020 by the Central Bank of Brazil (BCB)”
  - Não coberto pela evidência: A expressão 'clearest contribution to financial inclusion' é uma interpretação editorial não literalmente enunciada na evidência, embora inferível a partir dos dados apresentados.
  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "As partes factuais da afirmação (Pix lançado pelo BCB em novembro de 2020; tornou-se o meio dominante de transferência de dinheiro no Brasi…") — cascata: baseline → context_expansion
- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-1`** [2] [3]
  - Trecho: In 2025, **148 million people, about 86% of adults, and 12.8 million firms** made or received at least one Pix, and in the second half of that year Pix carried **54.7% of all payment transactions** in the country.
  - Justificativa: A evidência confirma todos os elementos da afirmação: 148 milhões de pessoas e 12,8 milhões de empresas fizeram ou receberam pelo menos um Pix em 2025, representando cerca de 86% da população adulta; e o Pix respondeu p…
  - Suporte veio de: [2] [3]
  - Evidência: “Em 2025, foram realizadas quase 80 bilhões de transações, movimentando mais de R$ 35 trilhões; 148 milhões de pessoas e 12,8 milhões de empresas fizeram ou receberam pelo menos um Pix. A quantidade de pessoas representa…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [2] | parcial | Em 2025, foram realizadas quase 80 bilhões de transações, movimentando mais de R$ 35 trilhões; 148 milhões de pessoas e… |
    | [3] | parcial | O Pix, continua sendo o instrumento de pagamento mais utilizado, responsável por 54,7% das transações efetuadas no segu… |

- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-2`** [4]
  - Trecho: BCB data show that about **49 million adults made their first electronic transfers only after Pix arrived**, and that these newcomers were poorer and less formally employed than existing transfer users.
  - Justificativa: A evidência confirma explicitamente que 49 milhões de adultos passaram a fazer transferências eletrônicas após o lançamento do Pix, e que esse grupo tinha renda inferior e menor participação no mercado formal em compara…
  - Suporte veio de: [4]
  - Evidência: “Desses, **49 milhões passaram a fazer transferências após o lançamento do sistema de pagamentos do BC**”
### UNSUPPORTED

- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-3`** [5] [6] [7]
  - Trecho: Quasi-experimental studies find that Pix reshuffled deposits mainly among the already banked, pushed banks to hold more liquidity and raised wages at small firms, while evidence that it brought the unbanked into the for…
  - Justificativa: A maior parte da alegação é sustentada pela evidência: (1) depósitos foram reorganizados principalmente entre a população já bancarizada ("The results are mostly driven by already banked population"); (2) salários em pe…
  - Suporte veio de: [7] [5] [6]
  - Evidência: “The results are mostly driven by already banked population”
  - Não coberto pela evidência: "pushed banks to hold more liquidity" — a evidência menciona retenção de depósitos, mas não usa o termo liquidez nem afirma diretamente que bancos passaram a deter mais liquidez; "brought the unbanked into the formal system" — a evidência discute formalização como canal complementar, mas não aborda especificamente a inclusão dos desbancarizados no sistema formal
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | parcial | The results are mostly driven by already banked population |
    | [6] | parcial | Financial inclusion does not explain the results |
    | [7] | parcial | wages in small establishments rise significantly relative to large establishments after Pix |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [27] [1] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-5`** [1] [12]
  - Trecho: It built the platform, runs the settlement system and keeps the directory of payment aliases, a combination that sets Pix apart from most instant-payment schemes.
  - Justificativa: A evidência confirma que o Banco Central do Brasil desenvolveu o Pix e mantém um diretório centralizado de aliases, mas não menciona explicitamente que o BCB 'opera o sistema de liquidação' (settlement system). Além dis…
  - Suporte veio de: [12] [1]
  - Evidência: “User data is maintained in a centralized directory at the central bank of Brazil, as compared to the decentralized model of UPI's domain-based addressing”
  - Não coberto pela evidência: runs the settlement system — não há menção explícita na evidência de que o BCB opera o sistema de liquidação; a combination that sets Pix apart from most instant-payment schemes — a evidência compara apenas com UPI e alguns outros sistemas, sem afirmar que a combinação das três características é o diferencial
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [12] | parcial | User data is maintained in a centralized directory at the central bank of Brazil |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [14] [27] [40] [7] [6] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-11`** [14]
  - Trecho: In May 2025, Deputy Governor Renato Gomes called Pix "a public, open instant payments platform" with "an open architecture and inclusive design," crediting it with reducing reliance on cash and reaching underserved popu…
  - Justificativa: O conteúdo substantivo sobre Pix (plataforma pública, aberta, arquitetura aberta, design inclusivo, redução do uso de dinheiro e alcance de populações subatendidas) está explicitamente presente na evidência. No entanto,…
  - Suporte veio de: [14]
  - Evidência: “Designed as a public, open instant payments platform, Pix quickly transformed Brazil's payments landscape.”
  - Não coberto pela evidência: In May 2025 — data não mencionada na evidência; Deputy Governor Renato Gomes — nome e cargo do falante não mencionados na evidência
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `pix_brasil_c371a97f12c1_20261115T025714Z-53`** [32]
  - Trecho: From October 2025 every app had to offer fully digital fraud contestation, with refunds traceable beyond the first receiving account.
  - Justificativa: O trecho afirma que a contestação 100% digital seria obrigatória a partir de outubro, o que a evidência corrobora. Porém, a rastreabilidade de devoluções além da primeira conta receptora não entra em outubro: a evidênci…
  - Suporte veio de: [32]
  - Evidência: “A partir de 1º de outubro, o MED passa a ser feito de forma 100% digital, sem a necessidade de interação com o atendimento da instituição financeira.”
  - Não coberto pela evidência: Ano 2025 não é explicitamente mencionado na evidência; Rastreabilidade de devoluções além da primeira conta receptora a partir de outubro é contraditada — a evidência indica novembro (facultativa) e fevereiro (obrigatória)