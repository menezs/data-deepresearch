# Relatório de Auditoria — Claude (regulacao_ia_1916d2c857a4_20261102T195932Z)

**Arquivo auditado:** `answers/Claude/Emergente/regulacao_ia.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | regulacao_ia_1916d2c857a4_20261102T195932Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-18T10:36:35.854744+00:00 |
| **Total de trechos citados** | 96 |
| **Tempo de processamento** | 1:09:59:10 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 30.6 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 103 marcadores, 42 distintos |
| Referências listadas | 42 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 73 | 76.0% |
| **UNSUPPORTED** | 10 | 10.4% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 13 | 13.5% |
| **TOTAL** | 96 | 100.0% |

Sobre os 83 trechos citados auditados: SUPPORTED 87,95%, UNSUPPORTED 12,04%, CONTRADICTED 0,00%.

> **8 dos 73 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 8 estão **contados dentro** dos 73 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`12` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `5` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#52` Em 4 de abril, a Mesa determinou a criação de uma comissão especial. | [26] | [36] [28] [27] [34] | — |
| `#64` No fim de maio de 2026, o presidente da Câmara, Hugo Motta, anunciou que o parecer seria votado na comissão especial at… | [37] | [42] [28] [27] [34] [40] [36] [26] [13] [39] [24] [23] [38] | — |
| `#68` A ficha oficial registra a situação "Aguardando Parecer do(a) Relator(a)" na comissão especial. | [36] | [26] [27] [34] [40] | — |
| `#81` O equilíbrio entre os dois polos ainda está em disputa. | [32] [35] | [37] [30] [36] [25] [41] [13] [31] [19] [38] [42] [17] [40] | — |
| `#93` No Brasil, a pergunta central é se a Câmara votará o PL 2338 entre o fim das eleições e o recesso parlamentar, como sin… | [38] | [28] [40] [27] [23] [39] [37] [36] [18] [26] [31] [34] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 530836 |
| **Média de tokens por requisição** | 6395.6 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/42 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | downloaded | 20 | 16 | 2 | 1 | 1 |
| [[6]](https://www.consilium.europa.eu/de/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/) | blocked | 12 | 0 | 0 | 0 | 12 |
| [[19]](https://www.poder360.com.br/poder-congresso/senado-aprova-regulamentacao-da-inteligencia-artificial-entenda/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[16]](https://www.correiobraziliense.com.br/politica/2024/12/7004516-comissao-do-senado-aprova-pl-da-inteligencia-artificial.html) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[10]](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[17]](https://smabr.com/marco-regulatorio-da-inteligencia-artificial-e-aprovado-pelo-senado/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[18]](https://documentacao.senior.com.br/exigenciaslegais/noticias/federal/2025/2025-03-20-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[30]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/apresentacoes-em-eventos/2025.09.09RonyVainzofFecomrcio.pdf) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[32]](https://teletime.com.br/09/12/2025/pl-do-governo-garante-anpd-como-reguladora-residual-de-ia-no-brasil/) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[38]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[9]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[13]](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[15]](https://revistaoeste.com/politica/regulamentacao-da-inteligencia-artificial-e-aprovada-no-senado/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[23]](https://www.migalhas.com.br/depeso/422014/ia-e-direitos-autorais-o-que-diz-o-pl-2-338-23-aprovado-pelo-senado) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://jornaldebrasilia.com.br/noticias/brasil/lei-de-ia-avanca-no-senado-com-previsao-de-remuneracao-de-direitos-autorais/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[25]](https://apublica.org/?p=177447) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[26]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[27]](https://www.camara.leg.br/noticias/1160383-comissao-que-vai-analisar-projeto-sobre-inteligencia-artificial-sera-presidida-por-luisa-canziani-aguinaldo-ribeiro-sera-relator/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[29]](https://www.mobiletime.com.br/?p=834339) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[35]](https://teletime.com.br/19/01/2026/anatel-apoia-projeto-que-cria-sistena-nacional-de-ia-e-anpd-como-regulador-residual/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[36]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[40]](https://certificacaoiso.com.br/pl-2338-ai-act/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[2]](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[4]](https://www.nscale.com/blog/eu-ai-act-heres-what-to-expect) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[5]](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://www.goodwinlaw.com/en/insights/publications/2025/08/alerts-technology-aiml-european-commission-issues) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[8]](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[11]](https://www.eeas.europa.eu/delegations/chile/artificial-intelligence-council-gives-final-green-light-simplify-and-streamline-rules_en) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[14]](https://www12.senado.leg.br/noticias/videos/2024/12/marco-da-inteligencia-artificial-e-aprovado-em-plenario-e-vai-a-camara) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://www.cut.org.br/noticias/regulamentacao-da-ia-expoe-fragilidade-falhas-e-retrocessos-trabalhistas-f015) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/outros-documentos/apresentacao-do-pl-2338-23) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://www.meioemensagem.com.br/midia/regulamentacao-da-ia-no-brasil-e-aprovada-pelo-senado) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.diap.org.br/index.php/noticias/noticias/92249-pl-2338-23-votacao-do-projeto-sobre-inteligencia-artificial-esta-prevista-apenas-para-dezembro) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/apresentacoes-em-eventos/MARCOSALVESDESOUZASecretriodeDireitosAutoraiseIntelectuaisdoMINCCmaradosDeputados02.09.25.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://planalto.gov.br/ccivil_03/projetos/ato_2023_2026/2025/pl/pl-6237.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2594000) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://diariocarioca.com/2026/05/28/politica/camara-votacao-regulamentacao-ia/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[39]](https://convergenciadigital.com.br/governo/marco-legal-de-inteligencia-artificial-so-vota-depois-das-eleicoes/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.aosfatos.org/noticias/aprovada-senado-regulacao-ia-camara/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://boainformacao.com.br/2026/05/camara-dos-deputados-planeja-votar-projeto-de-regulacao-da-inteligencia-artificial/) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | #0, #4–9, #12–14, #18, #26, #73–74, #77, #80 | #72, #92 | #30, #88 (pulado) | `#0` The AI Act (Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence) is the first-ever comprehensive legal framework on AI worldwide.… |
| [[19]](https://www.poder360.com.br/poder-congresso/senado-aprova-regulamentacao-da-inteligencia-artificial-entenda/) | #40, #44–45, #82 | #79 | — | `#40` O texto estabelece uma série de casos para IAs de alto risco, como as que avaliam prioridades para serviços públicos essenciais ou para auxiliar diagnósticos e… |
| [[16]](https://www.correiobraziliense.com.br/politica/2024/12/7004516-comissao-do-senado-aprova-pl-da-inteligencia-artificial.html) | #34, #37–38 | #72 | — | `#34` O PL recebeu quase 200 emendas, sendo que 49 delas foram acatadas, total ou parcialmente. |
| [[10]](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) | #19–20, #22 | — | — | `#19` The European Commission published the Digital Omnibus on AI (Omnibus) on 19 November 2025, proposing to defer the high-risk compliance deadline from 2 August 2… |
| [[17]](https://smabr.com/marco-regulatorio-da-inteligencia-artificial-e-aprovado-pelo-senado/) | #35, #42, #71 | — | — | `#35` Seguindo o modelo do *Artificial Intelligence Act* , aprovado na União Europeia no início deste ano, o Projeto brasileiro classifica as regras de governança de… |
| [[18]](https://documentacao.senior.com.br/exigenciaslegais/noticias/federal/2025/2025-03-20-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil) | #36, #39, #49 | — | — | `#36` Entre eles estão os chamados sistemas de armas autônomas, que podem selecionar e atacar alvos sem intervenção humana. Além disso, o texto veta sistemas que ten… |
| [[30]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/apresentacoes-em-eventos/2025.09.09RonyVainzofFecomrcio.pdf) | #56 | #74 | #86 | `#56` 5) O controle de violação de direitos autorais deve ser feito no output; 6) Permitir o treinamento de IA a partir do uso de dados publicamente disponíveis na i… |
| [[32]](https://teletime.com.br/09/12/2025/pl-do-governo-garante-anpd-como-reguladora-residual-de-ia-no-brasil/) | #58–59 | — | #81 | `#58` O Poder Executivo enviou nesta terça-feira, 9, mensagem ao Congresso Nacional contendo um projeto de lei (PL) que dá o primeiro passo para a regulamentação e e… |
| [[38]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | #66 | #76, #93 | — | `#66` o relator do projeto disse que o trabalho de aprovação deve voltar à "força total" após as eleições |
| [[9]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99) | #17, #78 | — | — | `#17` 3. Non-compliance with the prohibition of the AI practices referred to in Article 5 shall be subject to administrative fines of up to EUR 35 000 000 or, if the… |
| [[13]](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/) | #28 | — | #83 (pulado) | `#28` leaving providers with a regulatory obligation but no finalized technical roadmap for meeting it |
| [[15]](https://revistaoeste.com/politica/regulamentacao-da-inteligencia-artificial-e-aprovada-no-senado/) | #33, #46 | — | — | `#33` O Senado Federal aprovou em votação simbólica, o Projeto de Lei (PL) 2338/2023 [...] Durante a votação simbólica do Senado, apenas os parlamentares Cleitinho (… |
| [[23]](https://www.migalhas.com.br/depeso/422014/ia-e-direitos-autorais-o-que-diz-o-pl-2-338-23-aprovado-pelo-senado) | #48, #75 | — | — | `#48` no entanto, os titulares poderiam proibir essa livre utilização, caso desejem. [...] Cabe ao agente de IA que utilizar obras e conteúdos protegidos remunerar o… |
| [[24]](https://jornaldebrasilia.com.br/noticias/brasil/lei-de-ia-avanca-no-senado-com-previsao-de-remuneracao-de-direitos-autorais/) | #50, #86 | — | — | `#50` Em nota assinada por entidades representantes de empresas de tecnologia e do agronegócio criticaram o texto. [...] A última versão do PL 2338 apresenta um conj… |
| [[25]](https://apublica.org/?p=177447) | #51, #87 | — | — | `#51` Apesar de a gente ter essa vitória nas questões de direitos autorais, a gente entende que a sociedade perde muito com essas outras emendas que acabaram sendo r… |
| [[26]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | — | — | #52, #65 | — |
| [[27]](https://www.camara.leg.br/noticias/1160383-comissao-que-vai-analisar-projeto-sobre-inteligencia-artificial-sera-presidida-por-luisa-canziani-aguinaldo-ribeiro-sera-relator/) | #31, #53 | — | — | `#31` O texto, apresentado pelo senador Rodrigo Pacheco (PSD-MG), ex-presidente do Senado, é fruto do trabalho de uma comissão de juristas. |
| [[29]](https://www.mobiletime.com.br/?p=834339) | #55, #87 | — | — | `#55` A audiência pública realizada nesta terça-feira, 2, pela Comissão Especial de Inteligência Artificial da Câmara dos Deputados, ouviu especialistas em direitos… |
| [[35]](https://teletime.com.br/19/01/2026/anatel-apoia-projeto-que-cria-sistena-nacional-de-ia-e-anpd-como-regulador-residual/) | #62 | — | #81 | `#62` A Anatel elogia a iniciativa e apoia a criação do SIA, mas sugere ajustes no texto de forma a reforçar o papel das agências reguladoras setoriais. [...] endoss… |
| [[36]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | #63 | — | #68 | `#63` \| 07/04/2026 \| **Comissão Especial sobre Inteligência Artificial (PL 2338/23) ( PL233823 )** Apensação do PL 6479/2025 a esta proposição. |
| [[40]](https://certificacaoiso.com.br/pl-2338-ai-act/) | #69, #95 | — | — | `#69` A primeira: o texto que você lê hoje é o do Senado, e a Câmara pode mudá-lo. Se mudar, ele volta ao Senado. |
| [[2]](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) | #1 | — | — | `#1` In April 2021, the European Commission proposed the first EU artificial intelligence law, establishing a risk-based AI classification system. |
| [[4]](https://www.nscale.com/blog/eu-ai-act-heres-what-to-expect) | #3 | — | — | `#3` the EU AI Act applies to all AI system providers based in the EU or who provide their services in the EU, irrespective of their location. |
| [[5]](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | #10 | — | — | `#10` The Commission published a first list of more than 180 organisations that have signed the Code of Practice on transparency of AI-generated content that operati… |
| [[7]](https://www.goodwinlaw.com/en/insights/publications/2025/08/alerts-technology-aiml-european-commission-issues) | #15 | — | — | `#15` A crucial distinction emerges for models posing “systemic risk” — typically those requiring 10^25 floating-point operations in training. |
| [[8]](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice) | #16 | — | — | `#16` Providers that do not sign the GPAI CoP will still have to adhere to the binding requirements of the EU AI Act. ... While adherence to the Code is voluntary, c… |
| [[11]](https://www.eeas.europa.eu/delegations/chile/artificial-intelligence-council-gives-final-green-light-simplify-and-streamline-rules_en) | #23 | — | — | `#23` The new law forms part of the so-called **'Omnibus VII'** legislative package in the EU's **simplification** agenda. |
| [[12]](https://usercentrics.com/knowledge-hub/eu-ai-act-high-risk-delay-article-50-transparency-consent/) | — | #24 | — | `#24` The regulation was signed on 8 July 2026, published in the Official Journal, and entered into force on 27 July 2026, three days after publication. |
| [[14]](https://www12.senado.leg.br/noticias/videos/2024/12/marco-da-inteligencia-artificial-e-aprovado-em-plenario-e-vai-a-camara) | #32 | — | — | `#32` O objetivo é oferecer uma regulação diferenciada, considerando o impacto do sistema na vida humana e direitos fundamentais. |
| [[20]](https://www.cut.org.br/noticias/regulamentacao-da-ia-expoe-fragilidade-falhas-e-retrocessos-trabalhistas-f015) | #41 | — | — | `#41` A versão aprovada nesta terça-feira excluiu os algoritmos das redes sociais da lista de sistemas considerados de alto risco, atendendo a pedidos de senadores o… |
| [[21]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/outros-documentos/apresentacao-do-pl-2338-23) | #43 | — | — | `#43` Saber que está interagindo com IA |
| [[22]](https://www.meioemensagem.com.br/midia/regulamentacao-da-ia-no-brasil-e-aprovada-pelo-senado) | #47 | — | — | `#47` A agência irá coordenar o Sistema Nacional de Regulação e Governança de Inteligência Artificial (SIA). participarão órgãos estatais de regulação setorial, enti… |
| [[28]](https://www.diap.org.br/index.php/noticias/noticias/92249-pl-2338-23-votacao-do-projeto-sobre-inteligencia-artificial-esta-prevista-apenas-para-dezembro) | #54 | — | — | `#54` O grupo definiu um cronograma de trabalho que prevê a votação do projeto apenas no final do ano legislativo, em dezembro de 2025. [...] há preocupação de que o… |
| [[31]](https://www2.camara.leg.br/atividade-legislativa/comissoes/comissoes-temporarias/especiais/57a-legislatura/comissao-especial-sobre-inteligencia-artificial-pl-2338-23/apresentacoes-em-eventos/MARCOSALVESDESOUZASecretriodeDireitosAutoraiseIntelectuaisdoMINCCmaradosDeputados02.09.25.pdf) | #57 | — | — | `#57` Portanto, não ter o capítulo de Direitos de Autor e Conexos no PL 2338/2023 implica onerar empresas e usuários, inviabilizando o desenvolvimento da tecnologia… |
| [[33]](https://planalto.gov.br/ccivil_03/projetos/ato_2023_2026/2025/pl/pl-6237.htm) | #60 | — | — | `#60` PROJETO DE LEI Nº 6.237, DE 2025 [...] Art. 1º Fica instituído o Sistema Nacional para Desenvolvimento, Regulação e Governança de Inteligência Artificial – SIA… |
| [[34]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2594000) | #61 | — | — | `#61` \| 19/03/2026 \| Apense-se à(ao) PL 2338/2023. Proposição Sujeita à Apreciação do Plenário. Regime de Tramitação: Prioridade (Art. 151, II, RICD). Inteiro teor \| |
| [[37]](https://diariocarioca.com/2026/05/28/politica/camara-votacao-regulamentacao-ia/) | — | #64 | — | `#64` O presidente da **Câmara dos Deputados**, **Hugo Motta** (**Republicanos-PB**), anunciou nesta quinta-feira (28) o cronograma definitivo para a votação do marc… |
| [[39]](https://convergenciadigital.com.br/governo/marco-legal-de-inteligencia-artificial-so-vota-depois-das-eleicoes/) | #67 | — | — | `#67` “Estamos ajustando o texto para votarmos”, frisou, de forma bastante cautelosa, em entrevista à CDTV, do portal Convergência Digital. Ribeiro assegura que o ma… |
| [[41]](https://www.aosfatos.org/noticias/aprovada-senado-regulacao-ia-camara/) | #70 | — | — | `#70` Agora, o projeto segue para a Câmara dos Deputados, onde o cenário para aprovação é menos favorável. Entre os pontos de preocupação estão o forte lobby das big… |
| [[42]](https://boainformacao.com.br/2026/05/camara-dos-deputados-planeja-votar-projeto-de-regulacao-da-inteligencia-artificial/) | #94 | — | — | `#94` Embora tenha cogitado inicialmente fundir o Redata ao projeto da inteligência artificial, o relator optou por uma estratégia de tramitação mais simplificada. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing a GSC Managed Website Verification successful. Waiting for www.consilium.europa.e
- https://www.consilium.europa.eu/de/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing a GSC Managed Website Verification successful. Waiting for www.consilium.europa.e

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-0`** [1]
  - Trecho: A Comissão Europeia o apresenta como o primeiro marco jurídico abrangente sobre IA no mundo, com o objetivo de promover uma IA confiável na Europa.
  - Justificativa: A evidência afirma explicitamente que o AI Act é 'the first-ever comprehensive legal framework on AI worldwide' e que 'The aim of the rules is to foster trustworthy AI in Europe', o que corresponde diretamente à afirmaç…
  - Suporte veio de: [1]
  - Evidência: “The AI Act (Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence) is the first-ever comprehensive legal framework on AI worldwide. The aim of the rules is to foster trustworthy AI in Europe.”
- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-1`** [2]
  - Trecho: A proposta original foi feita pela Comissão em abril de 2021 e já previa um sistema de classificação de IA baseado em risco.
  - Justificativa: A evidência afirma explicitamente que em abril de 2021 a Comissão Europeia propôs a primeira lei de IA da UE, estabelecendo um sistema de classificação de IA baseado em risco. Isso corresponde diretamente à afirmação.
  - Suporte veio de: [2]
  - Evidência: “In April 2021, the European Commission proposed the first EU artificial intelligence law, establishing a risk-based AI classification system.”
- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-3`** [4]
  - Trecho: As regras valem para todos os fornecedores de sistemas de IA estabelecidos na UE ou que ofereçam serviços no bloco, independentemente de onde estejam sediados.
  - Justificativa: A evidência afirma explicitamente que o EU AI Act se aplica a todos os fornecedores de sistemas de IA baseados na UE ou que fornecem serviços na UE, independentemente de sua localização, o que sustenta diretamente a afi…
  - Suporte veio de: [4]
  - Evidência: “the EU AI Act applies to all AI system providers based in the EU or who provide their services in the EU, irrespective of their location.”
### UNSUPPORTED

- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-24`** [12]
  - Trecho: O texto final tornou-se o Regulamento (UE) 2026/1744 e entrou em vigor em 27 de julho de 2026, após publicação no Jornal Oficial.
  - Justificativa: A evidência confirma que o regulamento foi publicado no Jornal Oficial e entrou em vigor em 27 de julho de 2026. No entanto, o número específico do regulamento «(UE) 2026/1744» não aparece em nenhuma parte da evidência…
  - Suporte veio de: [12]
  - Evidência: “The regulation was signed on 8 July 2026, published in the Official Journal, and entered into force on 27 July 2026.”
  - Não coberto pela evidência: Número específico do regulamento: (UE) 2026/1744 — não mencionado em nenhuma parte da evidência
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-30`** [1]
  - Trecho: Em setembro, abriu consulta sobre os desafios da tecnologia para o direito autoral.
  - Justificativa: A evidência não menciona nenhuma consulta aberta em setembro sobre os desafios da tecnologia para o direito autoral. O contexto trata do AI Act, modelos GPAI, transparência e riscos de IA, mas não aborda a abertura de u…
  - Não coberto pela evidência: abertura de consulta em setembro; desafios da tecnologia para o direito autoral
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_1916d2c857a4_20261102T195932Z-52`** [26]
  - Trecho: Em 4 de abril, a Mesa determinou a criação de uma comissão especial.
  - Justificativa: A evidência menciona 'Comissão Especial' como situação atual do PL 2338/2023 e registra ações da MESA (apensações em 2026-10-26 e 2026-10-27), mas não há menção à data de 4 de abril nem a qualquer determinação da Mesa p…
  - Não coberto pela evidência: data 'Em 4 de abril'; determinação da Mesa para criação de comissão especial
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [36] [28] [27] [34] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 11 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `regulacao_ia_1916d2c857a4_20261102T195932Z-2` — Referencia(s) citada(s) ['77e096f27c9d4bf6'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-11` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-21` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-25` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-27` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-29` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-84` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-85` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-89` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-90` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-91` — Referencia(s) citada(s) ['06a13daba8c316eb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-83` — Parte das fontes citadas sem conteudo: referencia(s) ['06a13daba8c316eb'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `regulacao_ia_1916d2c857a4_20261102T195932Z-88` — Parte das fontes citadas sem conteudo: referencia(s) ['06a13daba8c316eb'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.