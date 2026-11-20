# Relatório de Auditoria — Gemini (rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z)

**Arquivo auditado:** `answers/Gemini/EmConsolidacao/rede_social_saude_mental_adolecentes.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-01T21:47:10.035645+00:00 |
| **Total de trechos citados** | 126 |
| **Tempo de processamento** | 0:00:54:29 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 2956.1 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-01 20:53:01+00:00 |
| Citações no corpo | 269 marcadores, 30 distintos |
| Referências listadas | 30 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 72 | 57.1% |
| **UNSUPPORTED** | 46 | 36.5% |
| **CONTRADICTED** | 3 | 2.4% |
| **SKIPPED** | 5 | 4.0% |
| **TOTAL** | 126 | 100.0% |

Sobre os 121 trechos citados auditados: SUPPORTED 59,50%, UNSUPPORTED 38,01%, CONTRADICTED 2,47%.

> **45 dos 72 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 45 estão **contados dentro** dos 72 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`56` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `4` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `10` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 8, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#15` A adolescência é um período crítico de plasticidade cerebral, caracterizado por reorganizações estruturais e funcionais… | [8] [10] | [11] [7] [16] [19] | — |
| `#77` Para crianças entre 2 e 5 anos, o tempo de exposição deve ser rigorosamente limitado a, no máximo, 1 hora diária, exigi… | [6] | [14] [16] [7] [30] [5] [19] | — |
| `#121` É fundamental implementar programas contínuos de alfabetização de mídias e educação digital no currículo da educação bá… | [16] [19] [21] | [7] [30] [3] [6] [14] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2609813 |
| **Média de tokens por requisição** | 21568.7 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/30 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[8]](https://socialmediamdl.com/surgeon-general-social-media-report/) | downloaded | 31 | 6 | 17 | 8 | 0 |
| [[10]](https://www.hopkinsmedicine.org/health/expert-qa/social-media-and-mental-health-in-children-and-teens) | downloaded | 29 | 3 | 16 | 10 | 0 |
| [[11]](https://www.hhs.gov/sites/default/files/sg-youth-mental-health-social-media-advisory.pdf) | downloaded | 28 | 5 | 21 | 2 | 0 |
| [[16]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use.pdf) | downloaded | 22 | 5 | 15 | 2 | 0 |
| [[17]](https://www.mayoclinic.org/healthy-lifestyle/tween-and-teen-health/in-depth/teens-and-social-media-use/art-20474437) | downloaded | 19 | 2 | 11 | 6 | 0 |
| [[22]](https://legis.senado.leg.br/sdleg-getter/documento?dm=9205524&disposition=inline) | inaccessible | 15 | 0 | 0 | 0 | 15 |
| [[14]](https://www.sbp.com.br/sbp-atualiza-recomendacoes-sobre-saude-de-criancas-e-adolescentes-na-era-digital/) | downloaded | 14 | 6 | 4 | 4 | 0 |
| [[19]](https://www.wcwonline.org/2023/health-advisory-on-social-media-use-in-adolescence) | downloaded | 14 | 5 | 9 | 0 | 0 |
| [[1]](https://g1.globo.com/tecnologia/noticia/2024/10/23/83percent-das-criancas-e-adolescentes-que-usam-internet-no-brasil-tem-contas-em-redes-sociais-diz-pesquisa.ghtml) | downloaded | 10 | 8 | 1 | 1 | 0 |
| [[20]](https://www.unesco.org/gem-report/en/articles/how-many-countries-have-phone-bans-school) | downloaded | 10 | 2 | 6 | 2 | 0 |
| [[3]](https://www.gov.br/secom/pt-br/assuntos/uso-de-telas-por-criancas-e-adolescentes/guia/recursos-extras/pesquisas-e-outros-numeros) | downloaded | 9 | 7 | 0 | 2 | 0 |
| [[9]](https://www.hhs.gov/surgeongeneral/reports-and-publications/youth-mental-health/social-media/index.html) | downloaded | 9 | 4 | 4 | 1 | 0 |
| [[25]](https://www.projuris.com.br/blog/pl-2628-eca-digital/) | downloaded | 9 | 1 | 6 | 2 | 0 |
| [[5]](https://cetic.br/media/docs/publicacoes/2/20250512154015/tic_kids_online_2024_resumo_executivo.pdf) | downloaded | 6 | 3 | 1 | 2 | 0 |
| [[6]](https://cetic.br/media/docs/publicacoes/2/20250210193221/estatisticas_tic_criancas.pdf) | downloaded | 5 | 0 | 4 | 1 | 0 |
| [[29]](https://fundacaolemann.org.br/noticias/proibicao-de-celulares-nas-escolas-levanta-debate-sobre-educacao/) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[18]](https://www.apa.org/news/press/releases/2023/05/adolescent-social-media-use-recommendations) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[21]](https://www.unesco.org/en/articles/smartphones-school-only-when-they-clearly-support-learning) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[30]](https://www.gov.br/mec/pt-br/acesso-a-informacao/perguntas-frequentes/uso-de-celulares-nas-escolas) | downloaded | 4 | 0 | 2 | 2 | 0 |
| [[4]](https://www.cgi.br/noticia/releases/tic-kids-online-investiga-pela-primeira-vez-frequencia-do-uso-de-plataformas-digitais-por-criancas-e-adolescentes/) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[26]](https://www.fadc.org.br/noticias/adultizacao-pl-2628) | inaccessible | 3 | 0 | 0 | 0 | 3 |
| [[27]](https://agenciabrasil.ebc.com.br/politica/noticia/2025-08/camara-aprova-projeto-contra-adultizacao-de-criancas-nas-redes-sociais) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[2]](https://nic.br/noticia/releases/tic-kids-online-brasil-65-das-criancas-e-dos-adolescentes-usam-ia-generativa-para-estudar-criar-conteudo-e-lidar-com-emocoes/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[7]](https://cetic.br/media/docs/publicacoes/2/pt-br/20260317181039/tic_kids_online_2025_livro_eletronico.pdf.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[15]](https://resources.pedspandemicnetwork.org/library/3701/health-advisory-on-social-media-use-in-adolescence-3701/) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[24]](https://www.congressonacional.leg.br/web/atividade/materias/-/materia/170017) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[28]](https://www.opiniaoce.com.br/brasil/2026/06/29/mec-divulga-pesquisa-sobre-restricao-do-uso-de-celulares-nas-escolas/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[12]](https://institutodimicuida.org.br/books/saude-na-era-digital-sociedade-brasileira-de-pediatria-gestao-2022-2024/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[13]](https://portaldeboaspraticas.iff.fiocruz.br/biblioteca/menos-telas-mais-saude-atualizacao-2024/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2477340) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[8]](https://socialmediamdl.com/surgeon-general-social-media-report/) | #13, #27–28, #90–91, #124 | #5, #14–15, #17, #19–20, #22, #24–26, #29, #34, #73, #92, #112, #115–116 | #16, #18, #21, #23, #30, #35, #111, #113 | `#13` The Advisory reports that up to 95% of youth ages 13 to 17 use a social media platform, while more than one-third describe their use as "almost constant." |
| [[10]](https://www.hopkinsmedicine.org/health/expert-qa/social-media-and-mental-health-in-children-and-teens) | #63, #66, #71 | #19–23, #29, #37–38, #43, #65, #67–70, #72, #114 | #15–18, #35, #39, #44–45, #64, #112 | `#63` many children and teens may find a community that is more accepting of who they are than their immediate family or school environment. In that sense, social me… |
| [[11]](https://www.hhs.gov/sites/default/files/sg-youth-mental-health-social-media-advisory.pdf) | #42, #54, #90–91, #115 | #19–22, #24–26, #29–30, #33–36, #39–40, #92, #111–113, #116, #119 | #16, #23 | `#42` For example, a study conducted among 14-year-olds (n = 10,904) found that greater social media use predicted poor sleep, online harassment, poor body image, lo… |
| [[16]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use.pdf) | #51, #83, #87–89 | #35, #38–39, #44–45, #57, #73, #84, #86, #111, #113, #121–123, #125 | #43, #79 | `#51` Indicators of problematic social media use include a) a tendency to use social media even when adolescents want to stop, or realize it is interfering with nece… |
| [[17]](https://www.mayoclinic.org/healthy-lifestyle/tween-and-teen-health/in-depth/teens-and-social-media-use/art-20474437) | #63, #71 | #34, #44–45, #64–65, #67–70, #85, #114 | #14, #54, #72, #81, #124–125 | `#63` Friendships help teens feel supported and play a role in forming their identities. [...] Social media lets teens create online identities, chat with others and… |
| [[14]](https://www.sbp.com.br/sbp-atualiza-recomendacoes-sobre-saude-de-criancas-e-adolescentes-na-era-digital/) | #74–75, #79–81, #124 | #48, #113, #123, #125 | #54, #111, #117, #122 | `#74` A Sociedade Brasileira de Pediatria (SBP) divulgou [...] o Manual de Orientação #MenosTelas #MaisSaúde [...] O documento, elaborado pelo Grupo de Trabalho sobr… |
| [[19]](https://www.wcwonline.org/2023/health-advisory-on-social-media-use-in-adolescence) | #51, #63–64, #85, #87 | #65, #68–69, #71, #73, #84, #88, #114, #121 | — | `#51` Indicators of problematic social media use include - a tendency to use social media even when adolescents want to stop, or realize it is interfering with neces… |
| [[1]](https://g1.globo.com/tecnologia/noticia/2024/10/23/83percent-das-criancas-e-adolescentes-que-usam-internet-no-brasil-tem-contas-em-redes-sociais-diz-pesquisa.ghtml) | #4, #6, #14, #49–50, #52, #55–56 | #5 | #1 | `#4` Considerando as crianças de 9 a 10 anos que estão na internet, 60% têm conta em pelo menos uma rede social |
| [[20]](https://www.unesco.org/gem-report/en/articles/how-many-countries-have-phone-bans-school) | #46, #103 | #40, #47–48, #104, #110, #120 | #113, #117 | `#46` Facebook's own research revealed that 32% of teenage girls felt worse about their bodies after using Instagram. |
| [[3]](https://www.gov.br/secom/pt-br/assuntos/uso-de-telas-por-criancas-e-adolescentes/guia/recursos-extras/pesquisas-e-outros-numeros) | #0–3, #6, #10, #12 | — | #8, #11 | `#0` 93% da população de 9 a 17 anos é usuária de internet no país, o que representa atualmente certa de 25 milhões de crianças e adolescentes |
| [[9]](https://www.hhs.gov/surgeongeneral/reports-and-publications/youth-mental-health/social-media/index.html) | #13, #32, #41, #90 | #30–31, #40, #111 | #113 | `#13` Up to 95% of young people aged 13-17 report using a social media platform. Nearly two thirds of teenagers report using social media every day and one third rep… |
| [[25]](https://www.projuris.com.br/blog/pl-2628-eca-digital/) | #94 | #61, #93, #95, #100, #102, #115 | #118–119 | `#94` O Estatuto da Criança e do Adolescente (ECA), instituído em 1990, consolidou no Brasil uma política de proteção integral à infância e juventude. |
| [[5]](https://cetic.br/media/docs/publicacoes/2/20250512154015/tic_kids_online_2024_resumo_executivo.pdf) | #2, #6–7 | #9 | #0, #8 | `#2` Cerca de 83% dos usuários de CONTATOS Internet de 9 a 17 anos possuíam perfil próprio em pelo menos uma das plataformas digitais investigadas, sendo 60% para a… |
| [[6]](https://cetic.br/media/docs/publicacoes/2/20250210193221/estatisticas_tic_criancas.pdf) | — | #75–78 | #8 ⚡ | `#8` Nas classes DE, as proporções de crianças de 3 a 5 anos e de 6 a 8 anos que usaram computador em 2024 foram de apenas 7% e 15%, respectivamente. Na classe C, e… |
| [[29]](https://fundacaolemann.org.br/noticias/proibicao-de-celulares-nas-escolas-levanta-debate-sobre-educacao/) | #107–108 | #110, #120 | #109 | `#107` No dia 13 de janeiro foi sancionada a Lei 15.100/2025, que proíbe o uso de aparelhos eletrônicos portáteis pessoais em escolas públicas e privadas de todo o pa… |
| [[18]](https://www.apa.org/news/press/releases/2023/05/adolescent-social-media-use-recommendations) | #82, #89 | #86, #88 | — | `#82` The result is the American Psychological Association Health Advisory on Social Media Use in Adolescence, which contains 10 recommendations. [...] These recomme… |
| [[21]](https://www.unesco.org/en/articles/smartphones-school-only-when-they-clearly-support-learning) | — | #104–106 | #121 | `#104` Even just having a mobile phone nearby with notifications coming through is enough to result in students losing their attention from the task at hand. Another… |
| [[30]](https://www.gov.br/mec/pt-br/acesso-a-informacao/perguntas-frequentes/uso-de-celulares-nas-escolas) | — | #107–108 | #118, #109 ⚡ | `#107` A Lei 15.100/2025 não busca proibir, mas regulamentar o uso de celulares nas escolas para proteger a saúde mental, física e psíquica dos estudantes. |
| [[4]](https://www.cgi.br/noticia/releases/tic-kids-online-investiga-pela-primeira-vez-frequencia-do-uso-de-plataformas-digitais-por-criancas-e-adolescentes/) | #52–53 | — | #11 ⚡ | `#52` Considerando o contato com desconhecidos, 30% dos usuários de Internet de 9 a 17 anos relataram que tiveram contato com alguém na Internet que não conheciam pe… |
| [[27]](https://agenciabrasil.ebc.com.br/politica/noticia/2025-08/camara-aprova-projeto-contra-adultizacao-de-criancas-nas-redes-sociais) | — | #62, #100 | #61 | `#62` É o chamado PL contra a "adultização" de crianças. |
| [[2]](https://nic.br/noticia/releases/tic-kids-online-brasil-65-das-criancas-e-dos-adolescentes-usam-ia-generativa-para-estudar-criar-conteudo-e-lidar-com-emocoes/) | #58–59 | — | — | `#58` Pela primeira vez a pesquisa investigou a exposição de crianças e adolescentes a vídeos de pessoas divulgando jogos de apostas. Entre os usuários de 11 a 17 an… |
| [[7]](https://cetic.br/media/docs/publicacoes/2/pt-br/20260317181039/tic_kids_online_2025_livro_eletronico.pdf.pdf) | #60 | #0 | — | `#60` O contato com vídeos, fotos ou textos na Internet em que produtos e/ou marcas foram divulgados, sem que tenham sido necessariamente identificados como propagan… |
| [[24]](https://www.congressonacional.leg.br/web/atividade/materias/-/materia/170017) | — | #93, #95 | — | `#93` Norma Gerada: Lei nº 15.211 de 17/09/2025 |
| [[28]](https://www.opiniaoce.com.br/brasil/2026/06/29/mec-divulga-pesquisa-sobre-restricao-do-uso-de-celulares-nas-escolas/) | #107 | #109 | — | `#107` A Lei 15.100/2025, sancionada em janeiro do ano passado pelo presidente Luiz Inácio Lula da Silva, nasce a partir de um projeto de lei de autoria do deputado f… |
| [[12]](https://institutodimicuida.org.br/books/saude-na-era-digital-sociedade-brasileira-de-pediatria-gestao-2022-2024/) | — | #74 | — | `#74` Manual de Orientação – Menos Telas Mais Saúde – Publicação da Sociedade Brasileira de Pediatria (SBP), atualizada em agosto de 2024 |
| [[13]](https://portaldeboaspraticas.iff.fiocruz.br/biblioteca/menos-telas-mais-saude-atualizacao-2024/) | #74 | — | — | `#74` Sociedade Brasileira de Pediatria (SBP). Grupo de Trabalho. Saúde na Era Digital (gestão 2022-2024). Manual de Orientação. #MENOS TELAS #MAIS SAÚDE – Atualizaç… |
| [[23]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2477340) | — | #93 | — | `#93` Transformado na Lei Ordinária 15211/2025 |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://resources.pedspandemicnetwork.org/library/3701/health-advisory-on-social-media-use-in-adolescence-3701/ — HTTP 405 em https://resources.pedspandemicnetwork.org/library/3701/health-advisory-on-social-media-use-in-adolescence-3701/
- https://legis.senado.leg.br/sdleg-getter/documento?dm=9205524&disposition=inline — Falha ao conectar em https://legis.senado.leg.br/sdleg-getter/documento?dm=9205524&disposition=inline: Failed to perform, curl: (28) Connection timed out after 10022 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www.fadc.org.br/noticias/adultizacao-pl-2628 — HTTP 503 em https://www.fadc.org.br/noticias/adultizacao-pl-2628

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-0`** [3] [5] [7]
  - Trecho: Segundo dados da pesquisa TIC Kids Online Brasil, conduzida pelo Centro Regional de Estudos para o Desenvolvimento da Sociedade da Informação (Cetic.br) sob os auspícios do Comitê Gestor da Internet no Brasil (CGI.br),…
  - Justificativa: A evidência confirma explicitamente que 93% da população de 9 a 17 anos é usuária de internet no país, representando cerca de 25 milhões de crianças e adolescentes (referência 463c3baf69530eff). A atribuição à pesquisa…
  - Suporte veio de: [3] [7]
  - Evidência: “93% da população de 9 a 17 anos é usuária de internet no país, o que representa atualmente certa de 25 milhões de crianças e adolescentes”
  - Não coberto pela evidência: O termo 'usuária ativa' não aparece literalmente na evidência, que usa apenas 'usuária de internet'; O valor exato de '24,5 milhões' não aparece literalmente; a evidência menciona 'cerca de 24 milhões' e 'cerca de 25 milhões'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | sustenta | 93% da população de 9 a 17 anos é usuária de internet no país, o que representa atualmente certa de 25 milhões de crian… |
    | [7] | parcial | Em 2025, 92% dos brasileiros de 9 a 17 anos eram usuários de Internet, o que corresponde a cerca de 24 milhões de crian… |
    | [5] | ausente | — |

- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-1`** [1] [3]
  - Trecho: O levantamento estatístico indica que 83% dos jovens brasileiros de 9 a 17 anos que utilizam a internet possuem contas registradas em redes sociais.
  - Justificativa: A evidência afirma explicitamente que 83% dos usuários de internet de 9 a 17 anos reportaram possuir perfil em redes sociais, o que corresponde diretamente à afirmação do trecho avaliado.
  - Suporte veio de: [3]
  - Evidência: “83% dos usuários de internet de 9 a 17 anos reportaram possuir perfil em redes sociais.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | sustenta | 83% dos usuários de internet de 9 a 17 anos reportaram possuir perfil em redes sociais. |
    | [1] | ausente | — |

- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-2`** [3] [5]
  - Trecho: Quando essa proporção é analisada sob a ótica da faixa etária, observa-se que a adesão atinge 99% entre os adolescentes de 15 a 17 anos
  - Justificativa: A evidência confirma explicitamente que, entre os adolescentes de 15 a 17 anos, a proporção de possuir perfil em redes sociais/plataformas digitais é de 99%, partindo de uma proporção geral de 83% para o grupo de 9 a 17…
  - Suporte veio de: [3] [5]
  - Evidência: “83% dos usuários de internet de 9 a 17 anos reportaram possuir perfil em redes sociais. Entre a população de 15 a 17 anos, a proporção foi de 99%.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | sustenta | 83% dos usuários de internet de 9 a 17 anos reportaram possuir perfil em redes sociais. Entre a população de 15 a 17 an… |
    | [5] | sustenta | Cerca de 83% dos usuários de CONTATOS Internet de 9 a 17 anos possuíam perfil próprio em pelo menos uma das plataformas… |

### UNSUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-9`** [5]
  - Trecho: Para aproximadamente um terço dos jovens pertencentes às classes populares, o telefone celular pré-pago representa o único dispositivo de conectividade disponível no domicílio.
  - Justificativa: A evidência afirma que o telefone celular foi 'o único dispositivo digital usado por 32% dos usuários das classes DE', o que se aproxima do 'aproximadamente um terço' e 'classes populares'. Contudo, a CLAIM adiciona doi…
  - Suporte veio de: [5]
  - Evidência: “O telefone celular foi o principal dispositivo utilizado pela população investigada para acesso à rede (98%), sendo o único dispositivo digital usado por 32% dos usuários das classes DE.”
  - Não coberto pela evidência: telefone celular pré-pago (a evidência não menciona 'pré-pago'); disponível no domicílio (a evidência diz 'usado', não 'disponível no domicílio')
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-15`** [8] [10]
  - Trecho: A adolescência é um período crítico de plasticidade cerebral, caracterizado por reorganizações estruturais e funcionais profundas no sistema nervoso central.
  - Justificativa: A evidência menciona que a adolescência é uma 'fase altamente sensível do desenvolvimento cerebral' com 'mudanças significativas' e 'mudanças em áreas do cérebro em desenvolvimento', o que se aproxima do conceito geral.…
  - Suporte veio de: [8] [10]
  - Evidência: “The Advisory emphasizes that adolescence is a highly sensitive stage of brain development. During this period, young people experience significant changes in impulse control, emotional regulation, reward sensitivity, id…”
  - Não coberto pela evidência: plasticidade cerebral (termo não mencionado na evidência); reorganizações estruturais e funcionais profundas (a evidência fala em 'mudanças' e 'desenvolvimento cerebral', mas não em 'reorganizações estruturais e funcionais profundas'); sistema nervoso central (termo não mencionado na evidência)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [8] | parcial | The Advisory emphasizes that adolescence is a highly sensitive stage of brain development. |
    | [10] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [11] [7] [16] [19] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-16`** [8] [10] [11]
  - Trecho: Durante esse estágio do desenvolvimento, ocorre uma maturação assíncrona entre o sistema límbico e o córtex pré-frontal.
  - Justificativa: A evidência menciona a amígdala e o córtex pré-frontal separadamente no contexto de mudanças cerebrais associadas ao uso de redes sociais durante a adolescência, mas em nenhum momento menciona o 'sistema límbico' como t…
  - Não coberto pela evidência: maturação assíncrona entre sistema límbico e córtex pré-frontal; sistema límbico (termo não aparece na evidência; apenas a amígdala é mencionada); maturação assíncrona como conceito ou processo
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [8] | ausente | — |
    | [10] | ausente | — |
    | [11] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-8`** [3] [5] [6]
  - Trecho: Enquanto o uso de computadores alcança 76% a 97% das crianças e adolescentes pertencentes às classes A e B, essa taxa despenca para 40% na classe C e para apenas 20% nas classes D e E.
  - Justificativa: A janela apresenta dados de uso de computador por classe social para crianças de 0 a 8 anos que contradizem diretamente os percentuais alegados. Para classes AB, o documento indica 50% (ambas as faixas), não 76%-97%. Pa…
  - Evidência: “Nas classes DE, as proporções de crianças de 3 a 5 anos e de 6 a 8 anos que usaram computador em 2024 foram de apenas 7% e 15%, respectivamente. Na classe C, essas proporções alcançaram 20% e 30%, enquanto nas classes A…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | contradiz | Nas classes DE, as proporções de crianças de 3 a 5 anos e de 6 a 8 anos que usaram computador em 2024 foram de apenas 7… |

  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "A evidência confirma os valores de 76% (classes AB), 40% (classe C) e 20% (classes DE) para acesso à internet por meio de computadores. No…") — cascata: baseline → context_expansion → full_doc_scan
- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-11`** [3] [4]
  - Trecho: À medida que ingressam na adolescência inicial e média (13 a 14 anos), ocorre uma transição em direção a plataformas baseadas em imagens e vídeos curtos, destacando-se a preferência pelo Instagram (58%) e pelo TikTok.
  - Justificativa: A janela contradiz o trecho avaliado. Para adolescentes de 13 a 14 anos, o documento indica que as plataformas mais usadas são WhatsApp (73%) e Instagram (78%), e não Instagram (58%) e TikTok como afirma o trecho. Os nú…
  - Evidência: “Já no caso dos adolescentes de 13 a 14 anos e de 15 a 17 anos, as plataformas utilizadas com frequência mais alta são o WhatsApp (73% e 91%, respectivamente) e o Instagram (78% e 81%, respectivamente).”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | contradiz | Já no caso dos adolescentes de 13 a 14 anos e de 15 a 17 anos, as plataformas utilizadas com frequência mais alta são o… |

  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "A evidência confirma que o Instagram é a principal plataforma para usuários de 13 a 14 anos com 58%, mas não sustenta a caracterização de '…") — cascata: baseline → context_expansion → full_doc_scan
- **Trecho citado `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-109`** [28] [29] [30]
  - Trecho: O uso de telas é franqueado exclusivamente para finalidades pedagógicas planejadas e orientadas pelos docentes, ou como recurso de acessibilidade e suporte à saúde para estudantes com deficiência ou condições médicas es…
  - Justificativa: A afirmação usa 'exclusivamente' para limitar o uso a três finalidades (pedagógicas, acessibilidade e saúde), mas a evidência lista cinco categorias de uso permitido, incluindo também 'Promoção da inclusão digital e edu…
  - Suporte veio de: [28]
  - Evidência: “Sim. O uso de celulares é permitido para: - **Fins pedagógicos** , com autorização e mediação dos profissionais da educação; - **Garantia da acessibilidade** , atendendo às necessidades de estudantes com deficiência; -…”
  - Não coberto pela evidência: O termo 'telas' (amplo) vs. 'celulares' (específico) na evidência; A palavra 'exclusivamente' é contraditada pela lista de cinco exceções na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [30] | contradiz | Sim. O uso de celulares é permitido para: - **Fins pedagógicos** , com autorização e mediação dos profissionais da educ… |
    | [28] | parcial | Em sala de aula, o uso dos celulares só será permitido para fins pedagógicos ou didáticos, mediante orientação dos prof… |
    | [29] | ausente | — |


---

## 10. Trechos Citados Não Auditados

Motivos: 5 citam referência não baixada/inacessível.

- `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-96` — Referencia(s) citada(s) ['95d77a900cfafb72'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-97` — Referencia(s) citada(s) ['95d77a900cfafb72'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-98` — Referencia(s) citada(s) ['95d77a900cfafb72'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-99` — Referencia(s) citada(s) ['95d77a900cfafb72'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_e4c71cba382a_20261101T205241Z-101` — Referencia(s) citada(s) ['95d77a900cfafb72', '43202571e6b6382f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).