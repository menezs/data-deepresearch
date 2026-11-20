# Relatório de Auditoria — Gemini (regulacao_ia_50ed2d44b720_20261117T023910Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Emergente/regulacao_ia.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | regulacao_ia_50ed2d44b720_20261117T023910Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T03:11:49.066860+00:00 |
| **Total de trechos citados** | 85 |
| **Tempo de processamento** | 1:00:32:39 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3062.6 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-17 02:39:33+00:00 |
| Citações no corpo | 240 marcadores, 61 distintos |
| Referências listadas | 61 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 70 | 82.4% |
| **UNSUPPORTED** | 14 | 16.5% |
| **CONTRADICTED** | 1 | 1.2% |
| **TOTAL** | 85 | 100.0% |

Sobre os 85 trechos citados auditados: SUPPORTED 82,35%, UNSUPPORTED 16,47%, CONTRADICTED 1,17%.

> **31 dos 70 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 31 estão **contados dentro** dos 70 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`22` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#52` Complementing GPAI governance, Article 50 transparency rules for chatbots, deepfakes, and machine-readable synthetic wa… | [3] [18] [45] | [20] [24] [37] [32] [35] [23] [46] [22] [40] | — |
| `#64` Originally, the EU AI Act split supervision between the Commission’s AI Office for GPAI models and national market surv… | [4] [24] | [46] [17] [2] [35] [21] [33] [7] [1] | — |
| `#78` Article 50 of PL 2338/2023 mirrors the LGPD ceiling, capping fines at R$ 50 million per violation or 2% of Brazilian co… | [6] [7] [29] | [34] [25] [31] [8] [9] [5] [59] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1654335 |
| **Média de tokens por requisição** | 19462.8 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/61 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 3.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[4]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/10/EPRS_ATA(2025)772906.html) | downloaded | 14 | 4 | 5 | 5 | 0 |
| [[6]](https://www.globalsuitesolutions.com/pt/marco-legal-da-inteligencia-artificial-brasil/) | downloaded | 14 | 1 | 11 | 2 | 0 |
| [[8]](https://www.barbieriadvogados.com/regulamentacao-inteligencia-artificial-brasil/) | downloaded | 14 | 4 | 9 | 1 | 0 |
| [[3]](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-eu-2026-1744-digital-omnibus-on-ai) | downloaded | 13 | 7 | 4 | 2 | 0 |
| [[7]](https://www.barbieriadvogados.com/brazil-ai-act/) | downloaded | 13 | 3 | 9 | 1 | 0 |
| [[11]](https://www.euaiact.com/digital-omnibus-ai) | downloaded | 10 | 6 | 4 | 0 | 0 |
| [[10]](https://strong.com.br/blog/marco-legal-inteligencia-artificial-pl-2338/) | downloaded | 9 | 0 | 6 | 3 | 0 |
| [[20]](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/) | downloaded | 8 | 3 | 3 | 2 | 0 |
| [[22]](https://www.globalsuitesolutions.com/digital-omnibus-ai-regulation-2026-1744/) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[14]](https://nhimg.org/ai-liability-and-product-liability-guide) | downloaded | 6 | 4 | 2 | 0 | 0 |
| [[29]](https://certificacaoiso.com.br/pl-2338-ai-act/) | downloaded | 6 | 1 | 4 | 1 | 0 |
| [[38]](https://pt.wikipedia.org/wiki/Projeto_de_Lei_2338/2023) | downloaded | 6 | 0 | 3 | 3 | 0 |
| [[2]](https://eur-lex.europa.eu/legal-content/pt/ALL/?uri=CELEX%3A32024R1689) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[18]](https://www.euaiact.com/implementation-timeline) | downloaded | 5 | 1 | 4 | 0 | 0 |
| [[40]](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice) | downloaded | 5 | 1 | 4 | 0 | 0 |
| [[1]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[5]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[9]](https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2868197) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[13]](https://vraneseviclaw.com/en/the-ai-liability-directive-is-gone-what-governs-ai-related-harm-in-the-eu-now/) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[23]](https://www.jonesday.com/en/insights/2025/08/eu-ai-act-european-commission-publishes-generalpurpose-ai-code-of-practice) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[24]](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[26]](https://www.migalhas.com.br/depeso/422014/ia-e-direitos-autorais-o-que-diz-o-pl-2-338-23-aprovado-pelo-senado) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[28]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[32]](https://cms.law/en/nld/publication/eu-ai-act-questions-and-answers) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[35]](https://enactia.com/eu-ai-act-compliance/) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[12]](https://iagovernance.com/en/blog/ai-liability-act-withdrawn/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[15]](https://www.jota.info/opiniao-e-analise/artigos/direitos-autorais-no-pl-de-inteligencia-artificial-em-tempo-para-evitar-um-desastre) | downloaded | 3 | 0 | 1 | 2 | 0 |
| [[21]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202601744) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[27]](https://www.jota.info/opiniao-e-analise/colunas/ia-regulacao-democracia/avaliacao-de-impacto-algoritmico-no-pl-2338-23) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[34]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[36]](https://direitosnarede.org.br/2024/06/18/projeto-de-lei-n-2338-2023/) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[37]](https://www.regulation-ai.eu/en/ai-act/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[41]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[55]](https://euverify.com/resource/eu-product-liability-ai-software/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[16]](https://apublica.org/nota/ia-pl-2338-protege-direitos-autorais-mas-nao-os-trabalhistas/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[19]](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[25]](https://www.gov.br/anpd/pt-br/acesso-a-informacao/participacao-social/outras-acoes/documentos/consulta-a-sociedade-sandbox-regulatorio-de-ia.pdf/@@display-file/file) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[33]](https://www.legalithm.com/en/ai-act-guide) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[43]](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[48]](https://code-of-practice.ai/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[53]](https://ia.wiki.br/direito-e-regulacao/pl-2338-2023) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[54]](https://witniumchain.com/news/ai-liability-directive-withdrawn-product-liability-directive) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[56]](https://ajee-journal.com/the-new-eu-product-liability-directive-doctrinal-analysis) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[58]](https://revistaconsinter.com/index.php/ojs/article/view/900) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[59]](https://www.scirp.net/journal/paperinformation?paperid=141689) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[17]](https://eur-lex.europa.eu/legal-content/EN-FR/TXT/?uri=CELEX%3A32024R1689) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://impactlabglobal.com/policy-radar/instrument/brazil-ai-bill) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[39]](https://www.quinnemanuel.com/media/avvj5y50/eu-ai-act-obligations-on-general-purpose-ai-model-providers.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[42]](https://cset.georgetown.edu/article/eu-ai-code-safety/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[44]](https://digital-strategy.ec.europa.eu/en/faqs/signing-general-purpose-ai-code-practice) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[45]](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[46]](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778575/ECTI_STU(2025)778575_EN.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[47]](https://iapp.org/news/a/the-eu-ai-act-and-copyrights-compliance) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[49]](https://legalblogs.wolterskluwer.com/copyright-blog/the-ai-act-provisions-relating-to-copyright-possibility-of-private-enforcement-germany-as-an-example-part-1/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[50]](https://brasscom.org.br/por-regras-equilibradas-de-direitos-autorais-e-pela-competitividade-do-brasil-no-cenario-global-de-inteligencia-artificial/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[51]](https://www4.ecad.org.br/noticias/ecad-associacoes-da-gestao-coletiva-da-musica-e-entidades-da-cultura-entregam-carta-a-camara-pedindo-protecao-de-direitos-autorais-no-pl-da-inteligencia-artificial/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[52]](https://fenaj.org.br/setor-criativo-reage-a-possivel-retirada-de-direitos-autorais-do-pl-da-inteligencia-artificial/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[57]](https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/after-the-ai-liability-directive-civil-liability-for-healthcare-ai-and-the-limits-of-eu-risk-regulation/13737AF83003FAFAFE0F03F8DFF179F0) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[60]](https://direitosnarede.org.br/inteligencia-artificial/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[61]](https://cadernosjuridicos.fadi.br/cadernosjuridicos/article/view/126) | downloaded | 1 | 0 | 0 | 1 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[4]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/10/EPRS_ATA(2025)772906.html) | #0, #8–10 | #3, #11, #38, #44, #49 | #6–7, #13, #16, #64 | `#0` Published in July 2024 and amended in 2026, the AI Act already applies in part and will take full effect in 2028. |
| [[6]](https://www.globalsuitesolutions.com/pt/marco-legal-da-inteligencia-artificial-brasil/) | #43 | #1, #23, #26, #31, #34, #42, #44, #56, #69, #78, #83 | #57, #80 | `#43` A análise de crédito, que o AI Act põe de forma expressa no alto risco, não aparece com esse nome no art. 14. E a lista final depende das autoridades setoriais… |
| [[8]](https://www.barbieriadvogados.com/regulamentacao-inteligencia-artificial-brasil/) | #1, #24, #31, #76 | #2, #20, #28, #30, #42, #54, #75, #82–83 | #45 | `#1` aprovado pelo Senado Federal em 10 de dezembro de 2024, o projeto aguarda, em outubro de 2026, o parecer do relator na Comissão Especial da Câmara dos Deputado… |
| [[3]](https://www.ey.com/en_gr/technical/tax/tax-alerts/regulation-eu-2026-1744-digital-omnibus-on-ai) | #0, #9, #13, #15–16, #18, #36 | #3, #14, #52, #65 | #12, #66 | `#0` Regulation (EU) 2026/1744 of the European Parliament and of the Council, adopted on 8 July 2026 ("Digital Omnibus on AI" or "Regulation"), was published in the… |
| [[7]](https://www.barbieriadvogados.com/brazil-ai-act/) | #2, #29, #69 | #1, #5, #25, #27–28, #68, #76, #78, #81 | #30 | `#2` Both frameworks adopt a tiered risk classification system, distinguishing between systems that are absolutely prohibited, systems that are subject to heightene… |
| [[11]](https://www.euaiact.com/digital-omnibus-ai) | #3, #15, #18, #36, #39, #41 | #7, #14, #17, #82 | — | `#3` The high-risk obligations moved: Annex III use cases from 2 August 2026 to 2 December 2027, and Annex I product-safety systems from 2 August 2027 to 2 August 2… |
| [[10]](https://strong.com.br/blog/marco-legal-inteligencia-artificial-pl-2338/) | — | #2, #30, #34, #37, #54, #67 | #45, #60, #80 | `#2` O Brasil adota a mesma lógica de risco do Regulamento (UE) 2024/1689, mas a Europa já aplica a norma e o Brasil ainda discute o texto. |
| [[20]](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/) | #12, #16, #35 | #14, #65, #77 | #11, #66 | `#12` The KI-Marktüberwachungs- und Innovationsförderungsgesetz (KI-MIG), passed by the Bundestag on 11 June 2026 and published in the Bundesgesetzblatt on 28 July (… |
| [[22]](https://www.globalsuitesolutions.com/digital-omnibus-ai-regulation-2026-1744/) | #13, #18, #53 | #40, #55, #77 | #84 | `#13` The Digital Omnibus on AI is Regulation (EU) 2026/1744, ... It was published in the Official Journal of the EU on 24 July 2026 and has been in force since 27 J… |
| [[14]](https://nhimg.org/ai-liability-and-product-liability-guide) | #4, #70, #72–73 | #71, #84 | — | `#4` AI Liability Directive proposal, 2022/0303(COD)... withdrawal announced in the Commission 2025 work programme, COM(2025) 45; withdrawal published as C/2025/542… |
| [[29]](https://certificacaoiso.com.br/pl-2338-ai-act/) | #82 | #22, #67, #78, #84 | #26 | `#82` A empresa brasileira entra no escopo quando: **coloca um sistema de IA no mercado europeu** ou o disponibiliza para clientes na UE, mesmo vendendo daqui; **o r… |
| [[38]](https://pt.wikipedia.org/wiki/Projeto_de_Lei_2338/2023) | — | #60–61, #67 | #44, #80, #45 ⚡ | `#45` a partir de dezembro de 2024, a avaliação preliminar para sistemas de baixo risco será obrigatória somente a sistemas generativos e de propósito geral, sendo f… |
| [[2]](https://eur-lex.europa.eu/legal-content/pt/ALL/?uri=CELEX%3A32024R1689) | #0, #6, #8 | #19 | #66 | `#0` REGULATION (EU) 2024/1689 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 13 June 2024 laying down harmonised rules on artificial intelligence |
| [[18]](https://www.euaiact.com/implementation-timeline) | #18 | #6–7, #17, #52 | — | `#18` 2 December 2026## Two new prohibitions and the legacy marking deadline Article 5(1)(ba) and (bb), inserted by the AI Omnibus, prohibit specified non-consensual… |
| [[40]](https://en.wikipedia.org/wiki/General-Purpose_AI_Code_of_Practice) | #50 | #46, #48–49, #51 | — | `#50` The Code is organised into three chapters (Transparency, Copyright, and Safety and Security) and outlines how providers can meet the Act's relevant obligations… |
| [[1]](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727) | #0, #32 | #27 | #82 | `#0` (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I; ... This Regulation shall be binding in its entirety and… |
| [[5]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | #21 | #20 | #1, #22 | `#21` Comissão Temporária Interna sobre Inteligência Artificial no Brasil [...] Senador Eduardo Gomes (PL/TO) [...] Aprovada a Emenda nº 199 (Substitutivo) [...] O P… |
| [[9]](https://www.camara.leg.br/proposicoesWeb/prop_mostrarintegra?codteor=2868197) | #29, #34 | #2, #30 | — | `#29` Dispõe sobre o desenvolvimento, o fomento e o uso ético e responsável da inteligência artificial com base na centralidade da pessoa humana. \| Art. 2º O desenvo… |
| [[13]](https://vraneseviclaw.com/en/the-ai-liability-directive-is-gone-what-governs-ai-related-harm-in-the-eu-now/) | #4, #70 | #71, #74 | — | `#4` Directive (EU) 2024/2853, adopted 23 October 2024, entered into force on 8 December 2024, but applies only to products placed on the EU market from 9 December… |
| [[23]](https://www.jonesday.com/en/insights/2025/08/eu-ai-act-european-commission-publishes-generalpurpose-ai-code-of-practice) | — | #14, #17, #59 | #48 | `#14` From 2 August 2026, for GPAI models where both original and modified versions were placed on the EU market after 2 August 2025 |
| [[24]](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/) | #19 | #35, #47 | #64 | `#19` 2 August 2028: The Commission begins its first formal reviews of the AI Office, the impact of the law and the effectiveness of voluntary codes of conduct. [...… |
| [[26]](https://www.migalhas.com.br/depeso/422014/ia-e-direitos-autorais-o-que-diz-o-pl-2-338-23-aprovado-pelo-senado) | #60 | #21, #26, #61 | — | `#60` O desenvolvedor de IA que utilizar conteúdo protegido por direitos de autor e conexos deve publicar um sumário dos conteúdos utilizados, em sítio eletrônico de… |
| [[28]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | — | #22–24 | #76 | `#22` 17/03/2025 \| **Mesa Diretora ( MESA )** Recebido o Ofício nº 235/2025 do Senado Federal que submete à revisão da Câmara dos Deputados [...] o Projeto de Lei n°… |
| [[32]](https://cms.law/en/nld/publication/eu-ai-act-questions-and-answers) | — | #27, #35, #38, #41 | — | `#27` Preventing market fragmentation. By establishing uniform rules across the EU, the AI Act helps prevent EU market fragmentation, making it easier for businesses… |
| [[35]](https://enactia.com/eu-ai-act-compliance/) | #33 | #55, #84 | #32 | `#33` Under Article 25, a deployer, importer or distributor is treated as the provider of a high-risk system if it puts its own name or trademark on it, makes a subs… |
| [[12]](https://iagovernance.com/en/blog/ai-liability-act-withdrawn/) | #4, #70–71 | — | — | `#4` In its 2025 work program (COM(2025) 45), the Commission announced it was withdrawing it, and the withdrawal was published in the Official Journal dated October… |
| [[15]](https://www.jota.info/opiniao-e-analise/artigos/direitos-autorais-no-pl-de-inteligencia-artificial-em-tempo-para-evitar-um-desastre) | — | #5 | #60, #62 | `#5` Direitos autorais no PL de Inteligência Artificial |
| [[21]](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202601744) | #13, #15 | #66 | — | `#13` REGULATION (EU) 2026/1744 OF THE EUROPEAN PARNIAMENT AND OF THE COUNCIL ... 24.7.2026 ... of 8 July 2026 |
| [[27]](https://www.jota.info/opiniao-e-analise/colunas/ia-regulacao-democracia/avaliacao-de-impacto-algoritmico-no-pl-2338-23) | — | — | #21, #56–57 | — |
| [[34]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | #57 | #30, #56 | — | `#57` Art. 21. Adicionalmente às medidas de governança estabelecidas neste capítulo, órgãos e entidades do poder público da União, Estados, Distrito Federal e Municí… |
| [[36]](https://direitosnarede.org.br/2024/06/18/projeto-de-lei-n-2338-2023/) | — | #37, #75 | #67 | `#37` Definição de usos de IA que são inaceitáveis (lista de riscos excessivos), justificando a vedação da sua implementação e utilização no território nacional |
| [[37]](https://www.regulation-ai.eu/en/ai-act/) | #38, #82 | #40 | — | `#38` An AI system is high-risk under Annex III if it falls into one of these eight areas: 1. Biometric identification and categorisation 2. Critical infrastructure… |
| [[41]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) | #47 | #58 | #53 | `#47` Article 53: Obligations for providers of general-purpose AI models... (a) draw up and keep up-to-date the technical documentation of the model... information s… |
| [[55]](https://euverify.com/resource/eu-product-liability-ai-software/) | #72, #82 | #73 | — | `#72` In October 2024, the EU adopted Directive 2024/2853, which explicitly names software, AI systems, and SaaS (Software as a Service) as products. This means they… |
| [[16]](https://apublica.org/nota/ia-pl-2338-protege-direitos-autorais-mas-nao-os-trabalhistas/) | — | #5, #81 | — | `#5` A discussão foi uma das mais acirradas durante a tramitação do PL na CTIA, com representantes do setor de tecnologia defendendo a utilização de produções alhei… |
| [[19]](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation) | — | #10–11 | — | `#10` They work together in a Joint Technical Committee called JTC 21. |
| [[25]](https://www.gov.br/anpd/pt-br/acesso-a-informacao/participacao-social/outras-acoes/documentos/consulta-a-sociedade-sandbox-regulatorio-de-ia.pdf/@@display-file/file) | — | #20, #68 | — | `#20` in 2019, Bill n. 5051/2019 and Bill n. 21/2020 proposed to establish principles for AI use in Brazil. More recently, a commission composed of jurists was insti… |
| [[33]](https://www.legalithm.com/en/ai-act-guide) | — | #28, #40 | — | `#28` ### Article 85: Right to lodge a complaint with a market surveillance authority [...] ### Article 86: Right to explanation of individual decision-making [...]… |
| [[43]](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) | #50 | #51 | — | `#50` Below you can download the code, consisting of three separately authored chapters: Transparency, Copyright, and Safety and Security. ... - Aleph Alpha - Amazon… |
| [[48]](https://code-of-practice.ai/) | — | #58–59 | — | `#58` provides for an exception or limitation for text and data mining in Article 4(1) of Directive (EU) 2019/790 which shall apply on conditions of lawful access an… |
| [[53]](https://ia.wiki.br/direito-e-regulacao/pl-2338-2023) | #67 | #76 | — | `#67` cria um Sistema Nacional de Regulação e Governança de Inteligência Artificial (SIA), coordenado pela Autoridade Nacional de Proteção de Dados (ANPD) |
| [[54]](https://witniumchain.com/news/ai-liability-directive-withdrawn-product-liability-directive) | — | #70, #73 | — | `#70` The stated reason was to avoid regulatory duplication: the new Product Liability Directive, adopted in November 2024, already covers AI systems and software |
| [[56]](https://ajee-journal.com/the-new-eu-product-liability-directive-doctrinal-analysis) | — | #72 | #73 | `#72` the EU now provides harmonised liability rules only for situations in which AI products injure consumers or other natural persons. |
| [[58]](https://revistaconsinter.com/index.php/ojs/article/view/900) | — | #79–80 | — | `#79` o pioneirismo regulatório europeu consubstanciado no AI Act influencia o Brasil pelo "Efeito Bruxelas", mas essa influência se materializa via adaptações locais |
| [[59]](https://www.scirp.net/journal/paperinformation?paperid=141689) | #79 | #80 | — | `#79` none of the Brazilian versions of the regulations (at their current state, considering that Bill No. 2,338/2023 is still being analyzed and its final text migh… |
| [[17]](https://eur-lex.europa.eu/legal-content/EN-FR/TXT/?uri=CELEX%3A32024R1689) | #6 | — | — | `#6` Having regard to the Treaty on the Functioning of the European Union, and in particular Articles 16 and 114 thereof, Having regard to the proposal from the Eur… |
| [[30]](https://www.mobiletime.com.br/noticias/24/08/2026/marco-ia-voto-fim-do-ano/) | #25 | — | — | `#25` O deputado federal Aguinaldo Ribeiro (PP-PB) informou que a votação do Marco Regulatório de Inteligência Artificial (PL 2338/2023) deve ficar para o final do a… |
| [[31]](https://impactlabglobal.com/policy-radar/instrument/brazil-ai-bill) | — | #25 | — | `#25` Brazil's AI bill vote pushed past the October elections |
| [[39]](https://www.quinnemanuel.com/media/avvj5y50/eu-ai-act-obligations-on-general-purpose-ai-model-providers.pdf) | — | #46 | — | `#46` According to the guidelines published by the European Commission (the "Commission") on 18 July 2025, a model is likely to qualify as GPAI model if (i) the amou… |
| [[42]](https://cset.georgetown.edu/article/eu-ai-code-safety/) | — | #48 | — | `#48` conducting state-of-the-art model evaluations such as benchmarking, red teaming, and human uplift studies, targeting each risk. |
| [[44]](https://digital-strategy.ec.europa.eu/en/faqs/signing-general-purpose-ai-code-practice) | — | #51 | — | `#51` Providers that don't adhere to the code may also be subject to a larger number of requests for information and requests for access to conduct model evaluations… |
| [[45]](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) | — | #52 | — | `#52` applicable from 2 August 2026 |
| [[46]](https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778575/ECTI_STU(2025)778575_EN.pdf) | — | #55 | — | `#55` Article 27 requires deployers of certain high-risk AI systems to conduct a fundamental rights impact assessment prior to their first deployment. This applies w… |
| [[47]](https://iapp.org/news/a/the-eu-ai-act-and-copyrights-compliance) | — | #58 | — | `#58` Generally, web scraping of copyrighted content for AI training is permitted under the DSM directive, provided rightsholders have not explicitly opted out. Righ… |
| [[49]](https://legalblogs.wolterskluwer.com/copyright-blog/the-ai-act-provisions-relating-to-copyright-possibility-of-private-enforcement-germany-as-an-example-part-1/) | — | #59 | — | `#59` The purpose of this article is to analyse to what extent it is possible to enforce under private law violations of these "copyright" provisions in Article 53 A… |
| [[50]](https://brasscom.org.br/por-regras-equilibradas-de-direitos-autorais-e-pela-competitividade-do-brasil-no-cenario-global-de-inteligencia-artificial/) | — | #62 | — | `#62` Brasscom – Associação das Empresas de Tecnologia da Informação e Comunicação (TIC) e de Tecnologias Digitais |
| [[51]](https://www4.ecad.org.br/noticias/ecad-associacoes-da-gestao-coletiva-da-musica-e-entidades-da-cultura-entregam-carta-a-camara-pedindo-protecao-de-direitos-autorais-no-pl-da-inteligencia-artificial/) | — | #63 | — | `#63` Ecad, associações da gestão coletiva da música e entidades da cultura entregam carta à Câmara pedindo proteção de direitos autorais no PL da Inteligência Artif… |
| [[52]](https://fenaj.org.br/setor-criativo-reage-a-possivel-retirada-de-direitos-autorais-do-pl-da-inteligencia-artificial/) | — | #63 | — | `#63` Entre as organizações que subscrevem o documento está a Federação Nacional dos Jornalistas (FENAJ) ... Também assinam o manifesto organizações como ... a União… |
| [[57]](https://www.cambridge.org/core/journals/european-journal-of-risk-regulation/article/after-the-ai-liability-directive-civil-liability-for-healthcare-ai-and-the-limits-of-eu-risk-regulation/13737AF83003FAFAFE0F03F8DFF179F0) | — | #74 | — | `#74` The AI Act and the MDR do not themselves determine civil liability. They do not convert non-compliance into automatic defect or automatic negligence. Nor does… |
| [[60]](https://direitosnarede.org.br/inteligencia-artificial/) | — | — | #81 | — |
| [[61]](https://cadernosjuridicos.fadi.br/cadernosjuridicos/article/view/126) | — | — | #83 | — |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-0`** [1] [2] [3] [4]
  - Trecho: The European Union’s Artificial Intelligence Act, enacted as Regulation (EU) 2024/1689 and substantially amended by Regulation (EU) 2026/1744—the Digital Omnibus on AI—is binding Union law advancing through staggered en…
  - Justificativa: A evidência confirma todos os elementos essenciais da afirmação: o AI Act foi promulgado como Regulation (EU) 2024/1689, foi alterado pela Regulation (EU) 2026/1744 (Digital Omnibus on AI), é direito vinculativo da Uniã…
  - Suporte veio de: [4] [1] [2] [3]
  - Evidência: “REGULATION (EU) 2024/1689 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 13 June 2024 laying down harmonised rules on artificial intelligence”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | sustenta | Published in July 2024 and amended in 2026, the AI Act already applies in part and will take full effect in 2028. |
    | [1] | sustenta | (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I; ... This Regulat… |
    | [2] | sustenta | REGULATION (EU) 2024/1689 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 13 June 2024 laying down harmonised rules on… |
    | [3] | sustenta | Regulation (EU) 2026/1744 of the European Parliament and of the Council, adopted on 8 July 2026 ("Digital Omnibus on AI… |

- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-1`** [5] [6] [7] [8]
  - Trecho: Conversely, Brazil’s proposed AI Legal Framework, Bill No. 2338/2023 (PL 2338/2023), passed the Federal Senate in December 2024 but remains stalled in a Special Committee of the Chamber of Deputies as of October 2026, l…
  - Justificativa: A evidência confirma todos os elementos essenciais da afirmação: aprovação no Senado em dezembro de 2024, tramitação estagnada na Comissão Especial da Câmara em outubro de 2026, regulação doméstica ancorada em LGPD, CDC…
  - Suporte veio de: [8] [7] [6]
  - Evidência: “aprovado pelo Senado Federal em 10 de dezembro de 2024, o projeto aguarda, em outubro de 2026, o parecer do relator na Comissão Especial da Câmara dos Deputados”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | If the bill is not approved before then, approval will likely be deferred to 2027. |
    | [8] | sustenta | aprovado pelo Senado Federal em 10 de dezembro de 2024, o projeto aguarda, em outubro de 2026, o parecer do relator na… |
    | [6] | parcial | O PL 2.338/2023, aprovado pelo Senado em 10 de dezembro de 2024, está na Câmara dos Deputados desde março de 2025, em u… |
    | [5] | ausente | — |

- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-2`** [7] [8] [9] [10]
  - Trecho: Although both frameworks adopt risk tiers, prohibit egregious uses, require impact scrutiny, and authorize regulatory sandboxes, Brussels regulates AI primarily as an internal-market product-safety regime, whereas Brasí…
  - Justificativa: A evidência sustenta explicitamente os elementos centrais da afirmação: (1) ambos os frameworks adotam tiers de risco ('Both frameworks adopt a tiered risk classification system'); (2) ambos proíbem usos graves (Arts. 5…
  - Suporte veio de: [7] [8] [9]
  - Evidência: “Both frameworks adopt a tiered risk classification system, distinguishing between systems that are absolutely prohibited, systems that are subject to heightened obligations by virtue of their high-risk nature, and syste…”
  - Não coberto pela evidência: A afirmação de que o EU AI Act também autoriza regulatory sandboxes não é explicitamente mencionada na evidência — a evidência só menciona sandboxes no contexto brasileiro (PL 2.338/2023 e ANPD).
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | sustenta | Both frameworks adopt a tiered risk classification system, distinguishing between systems that are absolutely prohibite… |
    | [10] | parcial | O Brasil adota a mesma lógica de risco do Regulamento (UE) 2024/1689, mas a Europa já aplica a norma e o Brasil ainda d… |
    | [8] | parcial | A agência conduz um sandbox regulatório em inteligência artificial e proteção de dados [...] O que mais distingue o pro… |
    | [9] | parcial | A autoridade competente e as autoridades setoriais que compõem o SIA deverão promover e autorizar o funcionamento de am… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta fortemente a distinção central: o modelo da UE como regulação de mercado ("The EU AI Act is primarily a market regulat…") — cascata: baseline → context_expansion
### UNSUPPORTED

- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-5`** [7] [15] [16]
  - Trecho: In Brazil, PL 2338/2023 faces intense congressional conflict over mandatory copyright remuneration for training data, weakened labor provisions, civil liability ambiguity, and the institutional capacity of a multi-agenc…
  - Justificativa: A maior parte do conteúdo substantivo da afirmação está sustentada pela evidência (conflito sobre direitos autorais, enfraquecimento de disposições trabalhistas, ambiguidade na responsabilidade civil, capacidade institu…
  - Suporte veio de: [7] [16]
  - Evidência: “The Senate text includes provisions requiring AI developers to disclose which copyright-protected works were used in training their systems and granting rights holders the right to opt out of such use. These provisions…”
  - Não coberto pela evidência: Atribuição específica da análise a 'Barbieri Advogados' — nenhum nome de escritório de advocacia aparece na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | artists (concerned about copyright implications for generative AI training), and trade unions (concerned about labour p… |
    | [15] | parcial | Direitos autorais no PL de Inteligência Artificial |
    | [16] | parcial | A discussão foi uma das mais acirradas durante a tramitação do PL na CTIA, com representantes do setor de tecnologia de… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-23`** [6] [28]
  - Trecho: As of October 2026, the Special Committee still awaited Ribeiro’s opinion, while the file accumulated 37 appended proposals covering deepfakes, watermarking, healthcare AI, and autonomous-system liability.
  - Justificativa: A evidência confirma que em outubro de 2026 o parecer do relator Aguinaldo Ribeiro ainda não tinha sido apresentado e que a ficha de tramitação registra 37 propostas apensadas. Porém, a evidência não sustenta que essas…
  - Suporte veio de: [6]
  - Evidência: “Em outubro de 2026 o parecer ainda não tinha sido apresentado”
  - Não coberto pela evidência: As 37 propostas apensadas cobrem especificamente os temas 'watermarking' e 'autonomous-system liability'; A associação direta entre as 37 propostas apensadas e os temas deepfakes e healthcare AI (estes aparecem em requerimentos de audiência pública, não necessariamente como conteúdo das propostas apensadas)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | parcial | em uma comissão especial, aguardando o parecer do relator, o deputado Aguinaldo Ribeiro |
    | [28] | parcial | Apensação da proposição PL 3615/2026 à proposição PL 6708/2025 |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-37`** [10] [36]
  - Trecho: Article 13 of PL 2338/2023 similarly bans "excessive-risk" practices, spanning subliminal manipulation, vulnerability exploitation, social scoring for public policy access, workplace and educational emotion recognition,…
  - Justificativa: A evidência confirma que o art. 13 veda usos de risco excessivo, incluindo armas autônomas, ranqueamento de pessoas para acesso a políticas públicas e identificação biométrica em espaços públicos com exceções contestada…
  - Suporte veio de: [36] [10]
  - Evidência: “os usos de risco excessivo são vedados (art. 13)”
  - Não coberto pela evidência: manipulação subliminal como prática banida no art. 13; exploração de vulnerabilidades como prática banida no art. 13; reconhecimento de emoções no trabalho e educação como banido no art. 13 (evidência o coloca no art. 14 com recomendação de transferência)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [10] | parcial | os usos de risco excessivo são vedados (art. 13) |
    | [36] | parcial | Definição de usos de IA que são inaceitáveis (lista de riscos excessivos), justificando a vedação da sua implementação… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `regulacao_ia_50ed2d44b720_20261117T023910Z-45`** [8] [10] [38]
  - Trecho: More dramatically, Article 12 of PL 2338/2023 requires all AI systems—including low-risk and generative systems—to undergo a documented preliminary risk assessment before market placement or use, a universal pre-market…
  - Justificativa: A janela contradiz a afirmação de que TODOS os sistemas de IA, incluindo os de baixo risco, devem passar por avaliação preliminar obrigatória. O texto afirma que 'a avaliação preliminar para sistemas de baixo risco será…
  - Evidência: “a partir de dezembro de 2024, a avaliação preliminar para sistemas de baixo risco será obrigatória somente a sistemas generativos e de propósito geral, sendo facultativa nos demais casos”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [38] | contradiz | a partir de dezembro de 2024, a avaliação preliminar para sistemas de baixo risco será obrigatória somente a sistemas g… |

  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "A evidência sustenta que o art. 12 exige avaliação preliminar de toda IA antes da colocação no mercado (incluindo IA generativa) e que enti…") — cascata: baseline → context_expansion → full_doc_scan