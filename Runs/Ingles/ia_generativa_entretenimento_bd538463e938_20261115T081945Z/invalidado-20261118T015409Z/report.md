# Relatório de Auditoria — ChatGPT (ia_generativa_entretenimento_bd538463e938_20261115T081945Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/Emergente/ia_generativa_entretenimento.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_bd538463e938_20261115T081945Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-15T09:09:35.133024+00:00 |
| **Total de trechos citados** | 112 |
| **Tempo de processamento** | 0:00:49:50 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 32.1 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 135 marcadores, 26 distintos |
| Referências listadas | 27 (1 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 52 | 46.4% |
| **UNSUPPORTED** | 40 | 35.7% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 20 | 17.9% |
| **TOTAL** | 112 | 100.0% |

Sobre os 92 trechos citados auditados: SUPPORTED 56,52%, UNSUPPORTED 43,47%, CONTRADICTED 0,00%.

> **24 dos 52 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 24 estão **contados dentro** dos 52 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`48` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `16` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `6` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#35` The 2026 MBA preserved those protections and added a requirement that companies notify the Guild when they license cove… | [10] | [3] [2] [1] | — |
| `#39` Copyright addresses a different question from performer identity: it protects original expression fixed in a work, not… | [2] | [1] [21] [15] | — |
| `#40` As of November 2026, the U.S. Copyright Office’s position is that existing copyright doctrine can accommodate AI-assist… | [2] | [15] [3] [1] | — |
| `#65` * and *Waits v. Frito-Lay* are foundational because they recognized claims based on deliberate imitation of distinctive… | [21] [22] | [1] [3] | — |
| `#95` The ethical concern becomes particularly acute after death because an estate may possess legal power to license a repli… | [1] [11] | [14] [2] | — |
| `#96` Synthetic media also complicate audience trust. | [13] | [23] [3] [1] [5] [2] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 3071697 |
| **Média de tokens por requisição** | 33388.0 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 1/27 (3.7%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[8]](https://www.sagaftra.org/contracts-industry-resources/contracts/2023-tvtheatrical-contracts) | blocked | 20 | 0 | 0 | 0 | 20 |
| [[1]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-1-Digital-Replicas-Report.pdf) | downloaded | 19 | 7 | 6 | 6 | 0 |
| [[3]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) | downloaded | 13 | 5 | 4 | 4 | 0 |
| [[13]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | downloaded | 11 | 2 | 4 | 5 | 0 |
| [[2]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[5]](https://www.microsoft.com/en-us/research/project/vall-e-x/vall-e/) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[9]](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement) | blocked | 6 | 0 | 0 | 0 | 6 |
| [[4]](https://studios.disneyresearch.com/2022/11/30/production-ready-face-re-aging-for-visual-effects/) | downloaded | 5 | 2 | 2 | 1 | 0 |
| [[14]](https://www.govinfo.gov/content/pkg/BILLS-119s4591rs/html/BILLS-119s4591rs.htm) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[11]](https://www.gov.ca.gov/2024/09/17/governor-newsom-signs-bills-to-protect-digital-likeness-of-performers/) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[6]](https://research.google/blog/vdtts-visually-driven-text-to-speech/) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[10]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[15]](https://caselaw.findlaw.com/court/us-dc-circuit/117062322.html) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[21]](https://law.justia.com/cases/federal/appellate-courts/F2/849/460/37485/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[23]](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/04/approaches-address-ai-enabled-voice-cloning) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[24]](https://www.sagaftra.org/sag-aftra-statement-fortnites-use-ai-darth-vader-voice-and-ulp-filing) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[25]](https://au.variety.com/2025/film/news/director-brady-corbet-defends-ai-use-the-brutalist-adrien-brody-felicity-jones-19817/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[7]](https://www.vanityfair.com/hollywood/2022/09/darth-vaders-voice-emanated-from-war-torn-ukraine) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[12]](https://www.tn.gov/governor/news/2024/3/21/photos--gov--lee-signs-elvis-act-into-law.html.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[16]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_24-cv-05417/USCOURTS-cand-3_24-cv-05417-1/context) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[17]](https://law.justia.com/cases/federal/district-courts/california/candce/4%3A2024cv05417/434709/680/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[18]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_23-cv-03417/USCOURTS-cand-3_23-cv-03417-33/context) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[19]](https://apps.cand.uscourts.gov/telhrg/?eId=e2b55f93-87d7-41b6-a5c0-f86275ec2d7a) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[20]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_23-cv-00201/USCOURTS-cand-3_23-cv-00201-41/context) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[22]](https://law.justia.com/cases/federal/appellate-courts/F2/978/1093/183202/) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[27]](https://www.congress.gov/119/plaws/publ12/PLAW-119publ12.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[26]](https://www.copyright.gov/ai/) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-1-Digital-Replicas-Report.pdf) | #1, #64, #67, #69, #92–94 | #2, #14, #68, #95, #100, #110 | #0, #6, #12, #99, #101, #106 | `#1` This Report uses the term "digital replica" to refer to a video, image, or audio recording that has been digitally created or manipulated to realistically but… |
| [[3]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) | #47–49, #59, #61 | #50, #60, #100, #111 | #62, #99, #105, #51 (s/ aval.) | `#47` Commenters disagreed about the need to use entire copyrighted works in AI training. |
| [[13]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | #82, #84 | #81, #83, #85, #98 | #96–97, #108–110 | `#82` Article 50 of the AI Act applies as from 2 August 2026. From that date onwards, providers and deployers of AI systems must comply with the transparency obligat… |
| [[2]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | #41–42, #46 | #39–40, #111 | #99 | `#41` Copyright protects the original expression in a work created by a human author, even if the work also includes AI-generated material. [...] Human authors are e… |
| [[5]](https://www.microsoft.com/en-us/research/project/vall-e-x/vall-e/) | #8–9 | #7, #87 | #10, #86 | `#8` VALL-E is a language modeling approach for text-to-speech synthesis (TTS). [...] can be used to synthesize high-quality personalized speech with only a 3-secon… |
| [[4]](https://studios.disneyresearch.com/2022/11/30/production-ready-face-re-aging-for-visual-effects/) | #4–5 | #3, #86 | #88 | `#4` We present the first practical, fully-automatic and production-ready method for re-aging faces in video images. [...] preservation of facial identity across va… |
| [[14]](https://www.govinfo.gov/content/pkg/BILLS-119s4591rs/html/BILLS-119s4591rs.htm) | #76–77 | #74–75, #111 | — | `#76` To protect intellectual property rights in the voice and visual likeness of individuals, and for other purposes. |
| [[11]](https://www.gov.ca.gov/2024/09/17/governor-newsom-signs-bills-to-protect-digital-likeness-of-performers/) | #71–72 | #70, #95 | — | `#71` **AB 2602** by Assemblymember Ash Kalra (D-San Jose) requires contracts to specify the use of AI-generated digital replicas of a performer’s voice or likeness,… |
| [[6]](https://research.google/blog/vdtts-visually-driven-text-to-speech/) | #11 | #86 | #88 | `#11` we present a proof-of-concept visually-driven text-to-speech model, called VDTTS, that automates the dialog replacement process. Given a text and the original… |
| [[10]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | #34 | #33, #35 | — | `#34` Neither traditional AI (technologies including those used in CGI and VFX) nor generative AI (GAI, meaning artificial intelligence that produces content includi… |
| [[15]](https://caselaw.findlaw.com/court/us-dc-circuit/117062322.html) | #44–45 | #43 | — | `#44` Decided: March 18, 2025 |
| [[21]](https://law.justia.com/cases/federal/appellate-courts/F2/849/460/37485/) | #66 | #63, #65 | — | `#66` Mere imitation of a recorded performance would not constitute a copyright infringement even where one performer deliberately sets out to simulate another's per… |
| [[23]](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/04/approaches-address-ai-enabled-voice-cloning) | #80, #107 | — | #106 | `#80` There is no AI exemption from the laws on the books and the FTC remains committed to protecting consumers from the misuse of 'AI'-enabled voice cloning technol… |
| [[24]](https://www.sagaftra.org/sag-aftra-statement-fortnites-use-ai-darth-vader-voice-and-ulp-filing) | #17 | #18, #104 | — | `#17` Fortnite's signatory company, Llama Productions, chose to replace the work of human performers with A.I. technology. Unfortunately, they did so without providi… |
| [[25]](https://au.variety.com/2025/film/news/director-brady-corbet-defends-ai-use-the-brutalist-adrien-brody-felicity-jones-19817/) | #19–20 | #21 | — | `#19` Innovative Respeecher technology was used in Hungarian language dialogue editing only, specifically to refine certain vowels and letters for accuracy. No Engli… |
| [[7]](https://www.vanityfair.com/hollywood/2022/09/darth-vaders-voice-emanated-from-war-torn-ukraine) | #15–16 | — | — | `#15` When he ultimately presented Jones with Respeecher's work, the actor signed off on using his archival voice recordings to keep Vader alive and vital even by ar… |
| [[12]](https://www.tn.gov/governor/news/2024/3/21/photos--gov--lee-signs-elvis-act-into-law.html.html) | #73 | #70 | — | `#73` While Tennessee's preexisting law protected name, image, and likeness, it did not specifically address new, personalized generative AI cloning models and servi… |
| [[16]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_24-cv-05417/USCOURTS-cand-3_24-cv-05417-1/context) | — | — | #52–53 | — |
| [[17]](https://law.justia.com/cases/federal/district-courts/california/candce/4%3A2024cv05417/434709/680/) | #54 | #55 | — | `#54` Anthropic's Rule 23(f) petition was fully briefed in the Ninth Circuit when the Settlement was reached. |
| [[18]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_23-cv-03417/USCOURTS-cand-3_23-cv-03417-33/context) | — | #56 | #52 | `#56` ORDER Denying the Plaintiffs' 482 Motion for Partial Summary Judgment and Granting Meta's 501 Cross-Motion for Partial Summary Judgment. Signed by Judge Vince… |
| [[19]](https://apps.cand.uscourts.gov/telhrg/?eId=e2b55f93-87d7-41b6-a5c0-f86275ec2d7a) | #57 | — | #111 | `#57` Further Case Management Conference held via Zoom on 10/29/2026 in case 3:23-cv-03417-VC; ... Parties in the Kadrey case to begin class discovery. ... Further C… |
| [[20]](https://www.govinfo.gov/app/details/USCOURTS-cand-3_23-cv-00201/USCOURTS-cand-3_23-cv-00201-41/context) | #58 | — | #111 | `#58` ORDER by Judge Lisa J. Cisneros granting 777 Stipulation Regarding Resolution of Plaintiffs' Motion for Discovery Sanctions Against DeviantArt. (bns, COURT STA… |
| [[27]](https://www.congress.gov/119/plaws/publ12/PLAW-119publ12.pdf) | #78 | #79 | — | `#78` This Act may be cited as the ‘‘Tools to Address Known Exploitation by Immobilizing Technological Deepfakes on Websites and Networks Act’’ or the ‘‘TAKE IT DOWN… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.sagaftra.org/contracts-industry-resources/contracts/2023-tvtheatrical-contracts — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930065-GRU 1794730817 648904706 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930078-GRU 1794730830 583221136 Varnish cache server
- https://law.justia.com/cases/federal/appellate-courts/F2/978/1093/183202/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-1`** [1]
  - Trecho: The most legally sensitive applications are “digital replicas”: realistic synthetic or manipulated representations of an identifiable person’s voice or appearance, whether authorized or unauthorized.
  - Justificativa: A evidência define explicitamente 'digital replica' como representação digitalmente criada ou manipulada para retratar realisticamente um indivíduo, podendo ser autorizada ou não. O termo cobre voz e aparência/semelhanç…
  - Suporte veio de: [1]
  - Evidência: “This Report uses the term "digital replica" to refer to a video, image, or audio recording that has been digitally created or manipulated to realistically but falsely depict an individual.”
  - Não coberto pela evidência: A caracterização de digital replicas como 'the most legally sensitive applications' (superlativo 'most') não é explicitamente afirmada na evidência; o relatório trata da sensibilidade legal das digital replicas mas não as classifica como as 'mais' sensíveis em relação a outras aplicações.
- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-4`** [4]
  - Trecho: Disney Research’s Face Re-Aging Network, for example, was designed as an automated system for re-aging faces in video while preserving identity across changes in expression, viewpoint, and lighting and allowing artists…
  - Justificativa: A evidência confirma todos os elementos da afirmação: o sistema é da Disney Research (FRAN), é automático para re-aging em vídeo, preserva identidade através de expressões, viewpoints e iluminação variáveis, e oferece c…
  - Suporte veio de: [4]
  - Evidência: “We present the first practical, fully-automatic and production-ready method for re-aging faces in video images.”
- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-5`** [4]
  - Trecho: Such tools illustrate an important distinction: generative or neural techniques can operate as artist-controlled visual-effects instruments rather than substitutes for actors.
  - Justificativa: A evidência descreve explicitamente uma técnica neural (FRAN, baseada em U-Net) para re-aging facial que 'incorporates simple and intuitive mechanisms that provides artists with localized control and creative freedom to…
  - Suporte veio de: [4]
  - Evidência: “our new face re-aging network (FRAN) incorporates simple and intuitive mechanisms that provides artists with localized control and creative freedom to direct and fine-tune the re-aging effect, a feature that is largely…”
  - Não coberto pela evidência: A afirmação explícita de que tais ferramentas não são 'substitutos para atores' não é declarada literalmente na evidência; é inferida do enquadramento da ferramenta como instrumento de VFX controlado por artistas.
### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-0`** [1]
  - Trecho: Generative AI is changing entertainment less by producing fully autonomous films or songs than by inserting machine-learning systems into existing production pipelines for writing, visual effects, performance capture, d…
  - Justificativa: A evidência trata principalmente de réplicas digitais, clonagem de voz e preocupações com direitos autorais, não sustentando a afirmação específica de que a IA generativa está mudando o entretenimento mais pela inserção…
  - Suporte veio de: [1]
  - Não coberto pela evidência: Comparação entre produção autônoma vs. inserção em pipelines existentes; Lista específica: writing, visual effects, performance capture, dubbing, voice synthesis, localization, advertising, games, post-production; Afirmação de que a mudança ocorre "less by producing fully autonomous films or songs"
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-2`** [1]
  - Trecho: In the United States, the Copyright Office deliberately uses a technologically neutral definition because a replica can be produced by generative AI, conventional computer graphics, compositing, voice conversion, or com…
  - Justificativa: A evidência não contém menção a uma definição 'tecnologicamente neutra' usada deliberadamente pelo Copyright Office, nem lista as técnicas específicas mencionadas na afirmação (generative AI, conventional computer graph…
  - Não coberto pela evidência: O Copyright Office usa uma definição 'tecnologicamente neutra'; O uso dessa definição é 'deliberado'; A razão é que réplicas podem ser produzidas por 'conventional computer graphics'
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-3`** [4]
  - Trecho: For screen production, machine learning can now alter an actor’s apparent age, replace or transform facial performances, generate synthetic faces, and retarget captured performances while preserving much of the original…
  - Justificativa: A evidência sustenta apenas a parte sobre alteração da idade aparente de atores (re-aging), mas não aborda substituição/transformação de performances faciais, geração de faces sintéticas como produto final, nem retarget…
  - Suporte veio de: [4]
  - Evidência: “We present the first practical, fully-automatic and production-ready method for re-aging faces in video images.”
  - Não coberto pela evidência: replace or transform facial performances; generate synthetic faces; retarget captured performances while preserving much of the original acting
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 20 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-13` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-22` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-23` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-24` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-25` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-26` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-27` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-28` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-29` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-30` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-31` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-32` — Referencia(s) citada(s) ['aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-36` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-37` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-38` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-89` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-90` — Referencia(s) citada(s) ['6dcd292ca023401a', 'aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-91` — Referencia(s) citada(s) ['6dcd292ca023401a', 'aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-102` — Referencia(s) citada(s) ['6dcd292ca023401a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_bd538463e938_20261115T081945Z-103` — Referencia(s) citada(s) ['6dcd292ca023401a', 'aca12210a3d2f331'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.