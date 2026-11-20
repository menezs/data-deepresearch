# Relatório de Auditoria — Gemini (ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z)

**Arquivo auditado:** `answers/Gemini/Emergente/ia_generativa_entretenimento.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-02T15:57:43.820971+00:00 |
| **Total de trechos citados** | 87 |
| **Tempo de processamento** | 0:00:24:22 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 2959.6 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-02 15:33:43+00:00 |
| Citações no corpo | 87 marcadores, 20 distintos |
| Referências listadas | 32 (12 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 25 | 28.7% |
| **UNSUPPORTED** | 28 | 32.2% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 34 | 39.1% |
| **TOTAL** | 87 | 100.0% |

Sobre os 53 trechos citados auditados: SUPPORTED 47,16%, UNSUPPORTED 52,83%, CONTRADICTED 0,00%.

> **17 dos 25 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 17 estão **contados dentro** dos 25 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`30` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `7` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `7` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#38` Concebida primordialmente para proteger o setor musical de Nashville e Memphis, a lei atualizou a legislação estadual d… | [10] | [15] [14] [11] [25] [9] [12] [6] [21] | — |
| `#39` O ELVIS Act definiu a voz como um som em qualquer meio que seja prontamente identificável e atribuível a um indivíduo,… | [13] | [14] [15] [10] [12] [11] [25] | — |
| `#40` A inovação legislativa do Tennessee reside no estabelecimento da responsabilidade civil primária e secundária para empr… | [15] | [10] [12] [11] [14] [26] [25] [18] | — |
| `#56` Além disso, o projeto estipula a obrigatoriedade de transparência e rotulagem para conteúdos sintéticos. | [22] | [25] [26] [27] [7] [21] | — |
| `#63` Esse desalinhamento forçava os tradutores a adaptarem os diálogos para encontrar palavras que coincidissem com a abertu… | [30] | [19] [32] [20] [31] [18] [17] [16] | — |
| `#68` Modelagem Tridimensional Generativa: Uma malha 3D dinâmica da área bucal é gerada e modificada em tempo real para acomp… | [30] | [32] [19] [9] [12] [18] [14] [26] [21] [22] [2] [3] [31] | — |
| `#78` Para desenvolver algoritmos capazes de sintetizar vozes, rostos e estilos de atuação, as empresas de tecnologia realiza… | [14] | [18] [17] [15] [9] [26] [19] [2] [6] [22] [25] [3] [31] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 962093 |
| **Média de tokens por requisição** | 18152.7 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 12/32 (37.5%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 2.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | inaccessible | 20 | 0 | 0 | 0 | 20 |
| [[2]](https://blog.promise.legal/sag-aftra-ai-indie-film-compliance/) | downloaded | 12 | 7 | 5 | 0 | 0 |
| [[28]](https://flawlessai.com/) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[30]](https://felixrunye.medium.com/the-invisible-magic-of-netflixs-neural-dubbing-how-ai-rewrites-actor-lips-96e5fc1df317) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[5]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[8]](https://studio.aifilms.ai/blog/california-ai-laws-protect-actors-digital-replicas) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[17]](https://www.satedrj.org.br/sindicato-repudia-globo-por-usar-ia-no-lugar-de-dubladores-em-documentario/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[14]](https://www.americanbar.org/groups/communications_law/resources/magazine/2024-summer/elvis-act-tennessee-shows-its-burning-love-recording-artists/) | downloaded | 4 | 0 | 2 | 2 | 0 |
| [[24]](https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara) | inaccessible | 4 | 0 | 0 | 0 | 4 |
| [[29]](https://quod.lib.umich.edu/j/jcms/images/12_64.1infocus-holliday.pdf) | inaccessible | 4 | 0 | 0 | 0 | 4 |
| [[7]](https://www.dglaw.com/importance-of-digital-replica-consents-under-the-sag-aftra-commercials-contract/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[10]](https://www.armstrongteasdale.com/thought-leadership/artificial-intelligence-and-copyrights-tennessees-elvis-act-becomes-law/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[21]](https://www.congressonacional.leg.br/web/atividade/materias/-/materia/157233/pdf?_materia_WAR_atividadeportlet_utm_source=chatgpt.com) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[22]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[4]](https://www.sagaftra.org/sites/default/files/sa_documents/Contract%20Bulletin%20-%20A.I.%20Synthetic%20Performer%20vs%20Digital%20Replicas.pdf) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[12]](https://aicompliant.ai/blog/ai-impact-assessment-tennessee-elvis-act-2024) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[13]](https://scholarship.law.vanderbilt.edu/context/jetlaw/article/1654/viewcontent/Why_Tennessee_s_ELVIS_Act_is_the_King_of_Artificial_Intelligence__Fowler.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[15]](https://iprmentlaw.com/2024/04/14/tennessees-elvis-act-protecting-the-voice-of-an-artist/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[16]](https://www.youtube.com/watch?v=4yNRe8lHufc) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[27]](https://apublica.org/nota/ia-pl-2338-protege-direitos-autorais-mas-nao-os-trabalhistas/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://www.loeb.com/en/insights/passle/2023/11/artificial-intelligence-terms-of-sagaftra-tv-theatrical-contract) | downloaded | 0 · nunca citada | — | — | — | — |
| [[6]](https://www.facebook.com/61577797664422/posts/%EF%B8%8F-the-entertainment-creative-arts-magaziness-october-creatively-legal-section-di/122186514272926588/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[9]](https://www.proskauer.com/blog/california-enacts-generative-ai-law-addressing-digital-replicas-of-performers) | downloaded | 0 · nunca citada | — | — | — | — |
| [[11]](https://law.vanderbilt.edu/why-tennessees-elvis-act-is-the-king-of-artificial-intelligence-protections/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[18]](https://diplomatique.org.br/inteligencia-artificial-generativa-para-quem/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://gqcanimes.com.br/dubladores-brasileiros-pedem-regulamentacao-para-uso-de-ia/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://diariodopara.com.br/noticias/ia-vai-substituir-dubladores-fim-da-profissao-pode-ser-inevitavel-entenda/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[23]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | inaccessible | 0 · nunca citada | — | — | — | — |
| [[25]](https://www.dataprivacybr.org/a-construcao-da-legislacao-de-inteligencia-artificial-no-brasil-analise-tecnica-do-texto-que-sera-votado-no-plenario-do-senado-federal/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://www.reddit.com/r/artificial/comments/10qwqfp/flawless_ai_lets_you_change_the_dialogue_on_a/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[32]](https://www.ortmoragency.com/blog/ai-lip-sync) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://blog.promise.legal/sag-aftra-ai-indie-film-compliance/) | #1, #3, #5, #7–8, #10, #12 | #6, #11, #76–77, #85 | — | `#1` An Employment-Based Digital Replica is a digital reproduction of a performer's voice or likeness created with the performer's physical participation during the… |
| [[28]](https://flawlessai.com/) | #61, #74 | #60, #75 | #70, #72 | `#61` To meet the needs of the film industry, Flawless has been created in close collaboration with guilds, unions, studios, and post-production partners. Clear Righ… |
| [[30]](https://felixrunye.medium.com/the-invisible-magic-of-netflixs-neural-dubbing-how-ai-rewrites-actor-lips-96e5fc1df317) | #66–67, #69 | #63, #68, #71 | — | `#66` First, the AI analyzes the original film frame-by-frame. It places thousands of invisible tracking points over the actor's face, mapping the precise geometry o… |
| [[8]](https://studio.aifilms.ai/blog/california-ai-laws-protect-actors-digital-replicas) | #32–34, #36 | #35 | — | `#32` AB 2602 prohibits contractual provisions that would allow for the use of a digital replica of an individual's voice or likeness in place of the individual's ac… |
| [[17]](https://www.satedrj.org.br/sindicato-repudia-globo-por-usar-ia-no-lugar-de-dubladores-em-documentario/) | #47–50 | #46 | — | `#47` O Sated-RJ (Sindicato dos Artistas e Técnicos em Espetáculos de Diversões do Estado do Rio de Janeiro) emitiu nota de repúdio contra o Globoplay, plataforma de… |
| [[14]](https://www.americanbar.org/groups/communications_law/resources/magazine/2024-summer/elvis-act-tennessee-shows-its-burning-love-recording-artists/) | — | #78–79 | #80–81 | `#78` generative AI model “learns its skills by analyzing massive amounts of digital [media] culled from the internet |
| [[7]](https://www.dglaw.com/importance-of-digital-replica-consents-under-the-sag-aftra-commercials-contract/) | #28–29 | #30 | — | `#28` The 2025 SAG-AFTRA Commercials Contract, effective April 1, 2025, included for the first time detailed provisions relating to the creation and use of synthetic… |
| [[10]](https://www.armstrongteasdale.com/thought-leadership/artificial-intelligence-and-copyrights-tennessees-elvis-act-becomes-law/) | #37 | #38, #41 | — | `#37` On March 21, 2024, the Ensuring Likeness Voice and Image Security Act (ELVIS Act) was signed into law by Tennessee Gov. Bill Lee. ... Tennessee is the first st… |
| [[21]](https://www.congressonacional.leg.br/web/atividade/materias/-/materia/157233/pdf?_materia_WAR_atividadeportlet_utm_source=chatgpt.com) | #52 | #51 | — | `#52` Decisão: Aprovada pelo Plenário ... Destino: À Câmara dos Deputados ... Último estado: 17/03/2025 - REMETIDA À CÂMARA DOS DEPUTADOS ... Relator(es): Senador Ed… |
| [[22]](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262) | — | — | #56–57 | — |
| [[12]](https://aicompliant.ai/blog/ai-impact-assessment-tennessee-elvis-act-2024) | — | #82 | — | `#82` expands Tennessee's existing "right of publicity" laws to explicitly include protections for individual voices, images, and likenesses against unauthorized use… |
| [[13]](https://scholarship.law.vanderbilt.edu/context/jetlaw/article/1654/viewcontent/Why_Tennessee_s_ELVIS_Act_is_the_King_of_Artificial_Intelligence__Fowler.pdf) | — | — | #39 | — |
| [[15]](https://iprmentlaw.com/2024/04/14/tennessees-elvis-act-protecting-the-voice-of-an-artist/) | — | #40 | — | `#40` It has also introduced a new form of secondary liability relevant for AI companies. Under Section 6[iii] of the amendment act (Section 47-25-1105), the law now… |
| [[16]](https://www.youtube.com/watch?v=4yNRe8lHufc) | — | #45 | — | `#45` FÁBIO AZEVEDO, PRESIDENTE DUBLAR E REPRESENTANTE DO MOVIMENTO DUBLAGEM VIVA |
| [[27]](https://apublica.org/nota/ia-pl-2338-protege-direitos-autorais-mas-nao-os-trabalhistas/) | #55 | — | — | `#55` o projeto de lei da inteligência artificial (IA) resistiu às pressões do setor privado e garantiu que um sistema não possa usar obras autorais protegidas sem a… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf (PDF, sem fallback via playwright)
- https://www.sagaftra.org/sites/default/files/sa_documents/Contract%20Bulletin%20-%20A.I.%20Synthetic%20Performer%20vs%20Digital%20Replicas.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/sa_documents/Contract%20Bulletin%20-%20A.I.%20Synthetic%20Performer%20vs%20Digital%20Replicas.pdf (PDF, sem fallback via playwright)
- https://www25.senado.leg.br/web/atividade/materias/-/materia/157233 — Falha ao conectar em https://www25.senado.leg.br/web/atividade/materias/-/materia/157233: Failed to perform, curl: (28) Connection timed out after 10024 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara — Falha ao conectar em https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara: Failed to perform, curl: (28) Connection timed out after 10022 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://quod.lib.umich.edu/j/jcms/images/12_64.1infocus-holliday.pdf — HTTP 403 em https://quod.lib.umich.edu/j/jcms/images/12_64.1infocus-holliday.pdf (PDF, sem fallback via playwright)

### Bloqueadas por barreira de acesso

- https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930071-GRU 1793633627 1039356947 Varnish cache server

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-1`** [2]
  - Trecho: As Réplicas Digitais Baseadas em Emprego (Employment-Based Digital Replicas - EBDR) correspondem aos ativos virtuais criados com a participação física e direta do artista durante sua contratação para um projeto específi…
  - Justificativa: A evidência define Employment-Based Digital Replica como uma reprodução digital da voz ou imagem de um artista, criada com a participação física do artista durante seu emprego em uma produção. Isso corresponde diretamen…
  - Suporte veio de: [2]
  - Evidência: “An Employment-Based Digital Replica is a digital reproduction of a performer's voice or likeness created with the performer's physical participation during their employment on a production.”
- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-3`** [2]
  - Trecho: As diretrizes contratuais estabelecem que, se a réplica for utilizada dentro do escopo originalmente planejado e conforme o roteiro aprovado, o consentimento do ator é considerado implícito ao contrato inicial de trabal…
  - Justificativa: A evidência afirma que, se a réplica for usada no filme para o qual o ator foi contratado e o uso permanecer substancialmente como roteirizado e performado, o consentimento não é necessário. Isso sustenta a afirmação de…
  - Suporte veio de: [2]
  - Evidência: “Under the agreement, if the replica is used in the motion picture the performer was employed for, and the use remains substantially as scripted and performed, consent is not required.”
- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-5`** [2]
  - Trecho: As Réplicas Digitais Criadas Independentemente (Independently Created Digital Replicas - ICDR) referem-se aos ativos virtuais gerados por sistemas algorítmicos que produzem a clara impressão visual ou auditiva de um art…
  - Justificativa: A evidência define explicitamente as Independently Created Digital Replicas como ativos digitais criados que produzem a clara impressão de um performer natural identificável, sem qualquer arranjo de emprego com esse per…
  - Suporte veio de: [2]
  - Evidência: “An Independently Created Digital Replica is a digitally created asset that creates the clear impression of an identifiable natural performer — but without any employment arrangement with that performer for the productio…”
  - Não coberto pela evidência: A menção específica a 'sistemas algorítmicos' como geradores do ativo não está explícita na definição de ICDR no texto, embora o contexto geral trate de IA.; A menção explícita a 'impressão visual ou auditiva' não é detalhada na definição; o texto diz apenas 'clear impression'.
### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-6`** [2]
  - Trecho: Esta modalidade abrange a recriação sintética de atores consagrados em novos filmes sem sua contratação presencial ou a utilização de modelos generativos treinados em dados públicos para replicar a figura de uma celebri…
  - Justificativa: A evidência sustenta a parte sobre recriação digital de atores sem contratação (Independently Created Digital Replicas), mas não menciona 'modelos generativos treinados em dados públicos' para replicar celebridades. Ess…
  - Suporte veio de: [2]
  - Evidência: “An Independently Created Digital Replica is a digitally created asset that creates the clear impression of an identifiable natural performer — but without any employment arrangement with that performer for the productio…”
  - Não coberto pela evidência: modelos generativos treinados em dados públicos; replicar a figura de uma celebridade (o termo 'celebridade' não é usado; a evidência fala em 'identifiable natural performer' e 'specific actor')
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-11`** [2]
  - Trecho: Caso o processo de geração de um performer sintético utilize comandos (prompts) que citem o nome de um artista real ou incorpore feições faciais específicas (como olhos, nariz ou boca) de um intérprete natural, a legisl…
  - Justificativa: A evidência sustenta parcialmente a afirmação. O requisito de consentimento para uso de feições faciais específicas (olhos, nariz, boca) de um intérprete natural na criação de performer sintético está explicitamente pre…
  - Suporte veio de: [2]
  - Evidência: “If a synthetic performer is created using a recognizable principal facial feature (eyes, nose, ears, or mouth) of a specific natural performer via generative AI, the performer's consent is required.”
  - Não coberto pela evidência: Afirmação de que 'prompts que citam o nome de um artista real' exigiriam autorização — não há menção a prompts nem citação de nomes na evidência; Referência genérica a 'legislação' exigindo autorização — a evidência foca no MOA da SAG-AFTRA (acordo coletivo), não em legislação específica; Exigência de 'negociação de compensações financeiras' especificamente para o caso de uso de feições faciais — a evidência menciona compensação apenas para substituição de humano em papel falante, não para o caso de feições faciais onde só se exige consentimento
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-30`** [7]
  - Trecho: O instrumento exige a especificação detalhada do tipo de mídia, período e território de veiculação, assegurando transparência absoluta ao artista sobre a exploração econômica de seus atributos biométricos.
  - Justificativa: A evidência menciona que o instrumento exige uma 'reasonably specific description of the intended use' e que performers têm 'visibility into how their likeness is being used', mas não especifica que sejam exigidos detal…
  - Suporte veio de: [7]
  - Evidência: “A reasonably specific description of each intended use must be listed in a table following this consent form.”
  - Não coberto pela evidência: especificação detalhada do tipo de mídia; especificação detalhada do período; especificação detalhada do território de veiculação
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 5 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 29 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-0` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-2` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-4` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-9` — Referencia(s) citada(s) ['86b633d7e4e014bb'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-13` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-14` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-15` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-16` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-17` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-18` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-19` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-20` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-21` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-22` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-23` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-24` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-25` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-26` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-27` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-31` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-42` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-43` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-44` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-53` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-54` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-58` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-59` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-62` — Referencia(s) citada(s) ['c1f4cdfc95600424'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-64` — Referencia(s) citada(s) ['c1f4cdfc95600424'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-65` — Referencia(s) citada(s) ['c1f4cdfc95600424'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-73` — Referencia(s) citada(s) ['c1f4cdfc95600424'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-83` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-84` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_083edd66e9bc_20261102T153322Z-86` — Referencia(s) citada(s) ['b1fc05846ad56596'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).