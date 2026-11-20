# Relatório de Auditoria — ChatGPT (ia_generativa_entretenimento_240915fb4975_20261102T150022Z)

**Arquivo auditado:** `answers/ChatGPT/Emergente/ia_generativa_entretenimento.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_240915fb4975_20261102T150022Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-02T15:21:47.334511+00:00 |
| **Total de trechos citados** | 85 |
| **Tempo de processamento** | 0:00:21:25 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 40.1 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 135 marcadores, 36 distintos |
| Referências listadas | 36 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 35 | 41.2% |
| **UNSUPPORTED** | 17 | 20.0% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 33 | 38.8% |
| **TOTAL** | 85 | 100.0% |

Sobre os 52 trechos citados auditados: SUPPORTED 67,30%, UNSUPPORTED 32,69%, CONTRADICTED 0,00%.

> **18 dos 35 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 18 estão **contados dentro** dos 35 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`21` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `1` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 4.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#41` A dificuldade apontada pela Equity é que o conjunto atual de copyright, performer rights, contrato e data protection nã… | [16] [17] | [34] [32] [30] [25] [31] [24] [5] [7] [3] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 768367 |
| **Média de tokens por requisição** | 14776.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/36 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 2.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[20]](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement) | blocked | 10 | 0 | 0 | 0 | 10 |
| [[18]](https://www.sagaftra.org/contracts-industry-resources/contracts/2023-tvtheatrical-contracts/artificial-intelligence-resources) | blocked | 9 | 0 | 0 | 0 | 9 |
| [[7]](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm) | downloaded | 8 | 5 | 2 | 1 | 0 |
| [[11]](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[19]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[30]](https://www.gov.ca.gov/2024/09/17/governor-newsom-signs-bills-to-protect-digital-likeness-of-performers/) | downloaded | 7 | 3 | 2 | 2 | 0 |
| [[17]](https://www.equity.org.uk/advice-and-support/know-your-rights/ai-toolkit/equitys-ai-vision-statement) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[6]](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[25]](https://copyright.gov/newsnet/2024/1048.html) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[31]](https://www.tn.gov/governor/news/2024/3/21/photos--gov--lee-signs-elvis-act-into-law.html) | downloaded | 5 | 1 | 3 | 1 | 0 |
| [[5]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[8]](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm) | downloaded | 4 | 2 | 1 | 1 | 0 |
| [[16]](https://www.equity.org.uk/advice-and-support/know-your-rights/ai-toolkit) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[22]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[12]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[23]](https://www.dga.org/News/PressReleases/2023/230603-DGA-and-AMPTP-Reach-Tentative-Agreement) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[24]](https://copyright.gov/ai/) | downloaded | 3 | 0 | 2 | 1 | 0 |
| [[27]](https://www.reuters.com/legal/government/us-supreme-court-declines-hear-dispute-over-copyrights-ai-generated-material-2026-03-02/) | inaccessible | 3 | 0 | 0 | 0 | 3 |
| [[28]](https://www.theguardian.com/technology/2025/jun/25/anthropic-did-not-breach-copyright-when-training-ai-on-books-without-permission-court-rules) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[29]](https://apnews.com/article/e77968015b94fbbf38234e3178ede578) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[32]](https://salazar.house.gov/media/press-releases/rep-salazars-no-fakes-act-advances-out-senate-judiciary-committee-unanimous) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[34]](https://www.theguardian.com/technology/2025/oct/13/equity-threatens-mass-direct-action-over-use-of-actors-images-in-ai-content) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[35]](https://law.justia.com/cases/federal/appellate-courts/F2/849/460/37285/) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[36]](https://law.justia.com/cases/federal/appellate-courts/F2/978/1093/184793/) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[1]](https://cloud.google.com/learn/what-is-artificial-intelligence?hl=pt-BR) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[2]](https://elevenlabs.io/voice-cloning) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[3]](https://www.respeecher.com/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[4]](https://c2pa.org/specifications/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[13]](https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[21]](https://www.sagaftra.org/contracts-industry-resources/television/tv-animation-agreements) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[9]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[10]](https://www12.senado.leg.br/noticias/videos/2024/12/marco-da-inteligencia-artificial-e-aprovado-em-plenario-e-vai-a-camara) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[14]](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[15]](https://www.legislation.gov.uk/ukpga/1988/48/part/II) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[26]](https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[33]](https://apnews.com/article/627d9adac6d4007b3bc489e511c1beb8) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[7]](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm) | #21–24, #76 | #2–3 | #77 | `#21` Art. 11. Autor é a pessoa física criadora de obra literária, artística ou científica. |
| [[30]](https://www.gov.ca.gov/2024/09/17/governor-newsom-signs-bills-to-protect-digital-likeness-of-performers/) | #33, #62, #76 | #5, #78 | #70, #79 | `#33` Governor Gavin Newsom signed two bills to help actors and performers protect their digital likenesses in audio and visual productions, including those who are… |
| [[17]](https://www.equity.org.uk/advice-and-support/know-your-rights/ai-toolkit/equitys-ai-vision-statement) | #52, #74, #82 | #11, #41, #71 | — | `#52` The one-off payments offered to performers who engage in AI work often do not reflect the fact that their image, voice or likeness may be used forever and on t… |
| [[6]](https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm) | — | — | #2, #20, #24, #76–77 | `#77` O PRESIDENTE DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei: ... Lei Geral de Proteção de Dados Pessoais (LGPD). |
| [[25]](https://copyright.gov/newsnet/2024/1048.html) | #28, #60, #83 | #4 | #70 | `#28` Given the gaps in existing legal protections, the Office recommends that Congress enact a new federal law that protects all individuals from the knowing distri… |
| [[31]](https://www.tn.gov/governor/news/2024/3/21/photos--gov--lee-signs-elvis-act-into-law.html) | #34 | #5, #59, #78 | #70 | `#34` first-of-its-kind legislation updating Tennessee's Protection of Personal Rights law to include protections or songwriters, performers, and music industry prof… |
| [[5]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | #19 | #2 | #24, #77 | `#19` X - são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de… |
| [[8]](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm) | #25–26 | #2 | #77 | `#25` I - dado pessoal: informação relacionada a pessoa natural identificada ou identificável; II - dado pessoal sensível: ... dado genético ou biométrico, quando vi… |
| [[16]](https://www.equity.org.uk/advice-and-support/know-your-rights/ai-toolkit) | — | #11, #41, #51 | #82 | `#11` Tell government to introduce a new system of personality rights over your voice, face and body in the age of AI. |
| [[22]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | #48–49, #57 | — | #70 | `#48` Neither traditional AI (technologies including those used in CGI and VFX) nor generative AI (GAI, meaning artificial intelligence that produces content includi… |
| [[12]](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | #36, #68 | #7 | — | `#36` The AI Act entered into force on 1 August 2024 and became applicable on 2 August 2026, with some exceptions: |
| [[23]](https://www.dga.org/News/PressReleases/2023/230603-DGA-and-AMPTP-Reach-Tentative-Agreement) | #50, #56 | — | #70 | `#50` **Artificial Intelligence:** Groundbreaking agreement confirming that AI is not a person and that generative AI cannot replace the duties performed by members. |
| [[24]](https://copyright.gov/ai/) | — | #4, #78 | #28 | `#4` July 31, 2024 - Copyright Office Releases Part 1 of Artificial Intelligence Report, Recommends Federal Digital Replica Law |
| [[28]](https://www.theguardian.com/technology/2025/jun/25/anthropic-did-not-breach-copyright-when-training-ai-on-books-without-permission-court-rules) | #31 | #63 | #70 | `#31` A federal judge in San Francisco said Anthropic made "fair use" of books by the writers Andrea Bartz, Charles Graeber and Kirk Wallace Johnson to train its Cla… |
| [[29]](https://apnews.com/article/e77968015b94fbbf38234e3178ede578) | #32 | #63 | #70 | `#32` This ruling does not stand for the proposition that Meta's use of copyrighted materials to train its language models is lawful, Chhabria wrote. It stands only… |
| [[32]](https://salazar.house.gov/media/press-releases/rep-salazars-no-fakes-act-advances-out-senate-judiciary-committee-unanimous) | #69 | #6 | #70 | `#69` the bipartisan Nurture Originals, Foster Art, and Keep Entertainment Safe (NO FAKES) Act, advanced unanimously out of the Senate Judiciary Committee. |
| [[34]](https://www.theguardian.com/technology/2025/oct/13/equity-threatens-mass-direct-action-over-use-of-actors-images-in-ai-content) | #65 | #55 | #70 | `#65` But Norwood represented a new challenge for the industry, said Budd, because "we haven't really seen the launch of a wholly synthetic actor" before. Equity UK… |
| [[1]](https://cloud.google.com/learn/what-is-artificial-intelligence?hl=pt-BR) | — | — | #0, #14 | — |
| [[2]](https://elevenlabs.io/voice-cloning) | — | #0, #15 | — | `#0` Create a digital replica of your voice that sounds just like you. |
| [[3]](https://www.respeecher.com/) | — | #0, #15 | — | `#0` Cross-Language Voice Cloning |
| [[4]](https://c2pa.org/specifications/) | — | #17, #80 | — | `#17` The Coalition for Content Provenance and Authenticity (C2PA) addresses the prevalence of misleading information online through the development of technical sta… |
| [[33]](https://apnews.com/article/627d9adac6d4007b3bc489e511c1beb8) | #47 | — | — | `#47` Hollywood's actors' union filed an unfair labor practice charge against Llama Productions on Monday, alleging the company replaced actors' work by using artifi… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www25.senado.leg.br/web/atividade/materias/-/materia/157233 — Falha ao conectar em https://www25.senado.leg.br/web/atividade/materias/-/materia/157233: Failed to perform, curl: (28) Connection timed out after 10023 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www12.senado.leg.br/noticias/videos/2024/12/marco-da-inteligencia-artificial-e-aprovado-em-plenario-e-vai-a-camara — Falha ao conectar em https://www12.senado.leg.br/noticias/videos/2024/12/marco-da-inteligencia-artificial-e-aprovado-em-plenario-e-vai-a-camara: Failed to perform, curl: (28) Connection timed out after 10033 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www.reuters.com/legal/government/us-supreme-court-declines-hear-dispute-over-copyrights-ai-generated-material-2026-03-02/ — HTTP 401 em https://www.reuters.com/legal/government/us-supreme-court-declines-hear-dispute-over-copyrights-ai-generated-material-2026-03-02/

### Bloqueadas por barreira de acesso

- https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://www.legislation.gov.uk/ukpga/1988/48/part/II — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://www.sagaftra.org/contracts-industry-resources/contracts/2023-tvtheatrical-contracts/artificial-intelligence-resources — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930036-GRU 1793631687 1930692604 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930048-GRU 1793631687 3148666287 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930033-GRU 1793631690 2070918254 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/television/tv-animation-agreements — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930055-GRU 1793631690 528873109 Varnish cache server
- https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://law.justia.com/cases/federal/appellate-courts/F2/849/460/37285/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://law.justia.com/cases/federal/appellate-courts/F2/978/1093/184793/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-5`** [30] [31]
  - Trecho: Califórnia e Tennessee já adotaram normas relevantes: AB 2602 e AB 1836 protegem performers vivos e falecidos em relação a réplicas digitais; o ELVIS Act do Tennessee ampliou expressamente a proteção da voz diante de cl…
  - Justificativa: A evidência confirma que a Califórnia adotou AB 2602 (protege performers vivos quanto a réplicas digitais de voz ou imagem) e AB 1836 (proíbe uso comercial de réplicas digitais de performers falecidos sem consentimento…
  - Suporte veio de: [31] [30]
  - Evidência: “AB 2602 by Assemblymember Ash Kalra (D-San Jose) requires contracts to specify the use of AI-generated digital replicas of a performer's voice or likeness, and the performer must be professionally represented in negotia…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [31] | parcial | The ELVIS Act builds upon existing state rule protecting against the unauthorized use of someone's likeness by adding "… |
    | [30] | parcial | AB 2602 by Assemblymember Ash Kalra (D-San Jose) requires contracts to specify the use of AI-generated digital replicas… |

- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-11`** [16] [17]
  - Trecho: A Equity britânica, por sua vez, recomenda cautela com escaneamentos e cláusulas de IA e defende remuneração proporcional, negociação coletiva e criação de direitos de personalidade mais claros sobre voz, rosto e corpo.
  - Justificativa: A evidência sustenta explicitamente remuneração proporcional, negociação coletiva e direitos de personalidade sobre voz, rosto e corpo. O aspecto 'cautela com escaneamentos e cláusulas de IA' é inferido a partir dos pri…
  - Suporte veio de: [17] [16]
  - Evidência: “Artists have the right to fair and proportionate remuneration that reflects industry standards and the length and scope of the agreed usage.”
  - Não coberto pela evidência: A expressão 'cautela com escaneamentos e cláusulas de IA' não é literalmente afirmada na evidência; os princípios protetivos implicam cautela, mas não usam esse termo nem referenciam 'cláusulas de IA' especificamente.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [17] | parcial | Artists have the right to fair and proportionate remuneration that reflects industry standards and the length and scope… |
    | [16] | parcial | Tell government to introduce a new system of personality rights over your voice, face and body in the age of AI. |

- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-15`** [2] [3]
  - Trecho: Serviços comerciais como ElevenLabs oferecem clonagem/síntese vocal, enquanto a Respeecher desenvolve tecnologia de transformação de voz dirigida, inclusive para aplicações de mídia.
  - Justificativa: A evidência confirma que ElevenLabs oferece clonagem/síntese vocal como serviço comercial (com APIs, SDKs e planos de preços), e que Respeecher desenvolve tecnologia de voz para aplicações de mídia (filme, jogos, broadc…
  - Suporte veio de: [2] [3]
  - Evidência: “Meet the accurate and advanced ElevenLabs AI Voice cloning”
  - Não coberto pela evidência: O termo 'dirigida' em 'transformação de voz dirigida' não é explicitamente usado na evidência, embora a tecnologia STS e o foco profissional/customizado possam ser inferidos como tal.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [2] | parcial | Meet the accurate and advanced ElevenLabs AI Voice cloning. Create a digital replica of your voice that sounds just lik… |
    | [3] | parcial | Respeecher provides professional AI voice solutions for teams that need consistent quality, clear rights management, an… |

### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-0`** [1] [2] [3]
  - Trecho: Tecnologias de geração de vídeo, clonagem e conversão de voz, sincronização labial, rejuvenescimento digital e modelos multimodais permitem hoje produzir desde pequenos retoques até “réplicas digitais” identificáveis de…
  - Justificativa: A evidência aborda principalmente clonagem de voz (ElevenLabs, Respeecher) e conceitos gerais de IA, mas não menciona geração de vídeo, sincronização labial, rejuvenescimento digital, modelos multimodais, nem a produção…
  - Suporte veio de: [2]
  - Evidência: “Create a digital replica of your voice that sounds just like you.”
  - Não coberto pela evidência: Tecnologias de geração de vídeo; Conversão de voz; Sincronização labial
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [2] | parcial | Create a digital replica of your voice that sounds just like you. |
    | [3] | parcial | Cross-Language Voice Cloning |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-2`** [5] [6] [7] [8]
  - Trecho: No Brasil, a Constituição protege imagem e voz; o Código Civil disciplina direitos da personalidade; a Lei 9.610/1998 protege autores e intérpretes, conferindo aos artistas intérpretes ou executantes poderes sobre fixaç…
  - Justificativa: A evidência sustenta a maior parte da afirmação (Constituição protege imagem e voz; Lei 9.610/1998 confere poderes aos artistas intérpretes sobre fixação, reprodução e outros usos, e estende proteção à voz e imagem asso…
  - Suporte veio de: [5] [7] [8]
  - Evidência: “X - são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pelo dano material ou moral decorrente de sua violação”
  - Não coberto pela evidência: Código Civil disciplina direitos da personalidade — nenhuma menção ao Código Civil ou a direitos da personalidade consta na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | parcial | X - são invioláveis a intimidade, a vida privada, a honra e a imagem das pessoas, assegurado o direito a indenização pe… |
    | [6] | ausente | — |
    | [7] | parcial | Art. 1º Esta Lei regula os direitos autorais, entendendo-se sob esta denominação os direitos de autor e os que lhes são… |
    | [8] | parcial | dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a si… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-3`** [7]
  - Trecho: A LDA também define autor como pessoa física criadora da obra, o que torna difícil encaixar uma máquina como autora de uma criação puramente autônoma; o grau mínimo de contribuição humana necessário para reivindicar pro…
  - Justificativa: A evidência sustenta que a LDA define autor como pessoa física (Art. 11), mas não contém nenhuma menção a IA, grau mínimo de contribuição humana, ou obras produzidas com IA. A afirmação sobre a ausência de especificação…
  - Suporte veio de: [7]
  - Evidência: “Art. 11. Autor é a pessoa física criadora de obra literária, artística ou científica.”
  - Não coberto pela evidência: A dificuldade de encaixar uma máquina como autora de criação puramente autônoma (interpretação não explicitada na evidência); O grau mínimo de contribuição humana necessário para reivindicar proteção em obras produzidas com IA; A afirmação de que tal grau mínimo não é especificado expressamente pela legislação brasileira (ausência não verificável em excertos parciais)
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 30 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 3 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-1` — Referencia(s) citada(s) ['b86c9907dd942c2e', 'c1228a5b83fb96bc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-8` — Referencia(s) citada(s) ['74b46d9019c32b1e', 'e30ab28959e94bb4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-9` — Referencia(s) citada(s) ['c48e1b3caae348b9', '9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-10` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-12` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-13` — Referencia(s) citada(s) ['c48e1b3caae348b9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-16` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-18` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-27` — Referencia(s) citada(s) ['2ddcc05b33f7db1a', 'ea5aedd5ed68db2a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-29` — Referencia(s) citada(s) ['23f8528fd2cb9952'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-30` — Referencia(s) citada(s) ['aab20b9028657da3'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-35` — Referencia(s) citada(s) ['b86c9907dd942c2e', 'c1228a5b83fb96bc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-37` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-38` — Referencia(s) citada(s) ['e30ab28959e94bb4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-39` — Referencia(s) citada(s) ['e636666c3ae8b823'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-40` — Referencia(s) citada(s) ['aea636540b72498d'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-42` — Referencia(s) citada(s) ['c48e1b3caae348b9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-43` — Referencia(s) citada(s) ['c48e1b3caae348b9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-44` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-45` — Referencia(s) citada(s) ['b91cbad094e89ada'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-46` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-53` — Referencia(s) citada(s) ['b86c9907dd942c2e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-54` — Referencia(s) citada(s) ['c1228a5b83fb96bc'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-58` — Referencia(s) citada(s) ['c48e1b3caae348b9'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-61` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-64` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-66` — Referencia(s) citada(s) ['aab20b9028657da3'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-67` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-72` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-73` — Referencia(s) citada(s) ['9d0ca35723cdd785', 'aca12210a3d2f331', 'b91cbad094e89ada'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-75` — Referencia(s) citada(s) ['c48e1b3caae348b9', 'aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-81` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_240915fb4975_20261102T150022Z-84` — Referencia(s) citada(s) ['74b46d9019c32b1e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.