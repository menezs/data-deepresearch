# Relatório de Auditoria — Gemini (ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Emergente/ia_generativa_entretenimento.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-17T23:38:05.972652+00:00 |
| **Total de trechos citados** | 112 |
| **Tempo de processamento** | 0:00:26:07 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 27.2 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-17 23:12:24+00:00 |
| Citações no corpo | 236 marcadores, 92 distintos |
| Referências listadas | 93 (1 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 80 | 71.4% |
| **UNSUPPORTED** | 24 | 21.4% |
| **CONTRADICTED** | 1 | 0.9% |
| **SKIPPED** | 7 | 6.2% |
| **TOTAL** | 112 | 100.0% |

Sobre os 105 trechos citados auditados: SUPPORTED 76,19%, UNSUPPORTED 22,85%, CONTRADICTED 0,95%.

> **35 dos 80 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 35 estão **contados dentro** dos 80 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`33` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `5` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `9` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `6` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#0` As of November 2026, generative artificial intelligence in entertainment has moved past unregulated experimentation int… | [5] [40] [79] [91] | [10] [56] [58] [3] [60] [76] [66] [69] [59] [57] | — |
| `#42` Conversely, international dubbing and localization have become prime automation targets as streaming services expand mu… | [15] [16] | [2] [3] [14] [90] [69] [56] [4] [60] | — |
| `#52` Because federal legislation has lagged production realities, entertainment unions have built the primary binding rules… | [35] [40] [45] | [10] [76] [13] [91] [69] [77] [93] | — |
| `#55` Between 2024 and 2025, SAG-AFTRA extended these guardrails across music, commercials, and video games. | [32] [34] [35] | [18] [76] [13] [37] [36] [56] [41] [27] [77] | — |
| `#62` On June 4, 2026, SAG-AFTRA members ratified a four-year Television and Theatrical Agreement by a 91.42 percent vote. | [40] [41] | [44] [43] [13] [27] [18] [76] [30] [34] [37] [36] | — |
| `#104` On November 12, 2026, the European Parliament also passed a non-binding resolution urging EU Charter amendments protect… | [83] | [88] [84] [80] [82] [73] [71] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1321267 |
| **Média de tokens por requisição** | 12583.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 1/93 (1.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 3.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[6]](https://www.theguardian.com/film/2026/oct/20/ai-actors-val-kilmer-as-deep-as-the-grave-tilly-norwood) | downloaded | 9 | 6 | 2 | 1 | 0 |
| [[13]](https://flauntaudio.com/ai-voice-actor-statistics-2026/) | downloaded | 9 | 6 | 1 | 2 | 0 |
| [[40]](https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[5]](https://www.researchgate.net/publication/417398892_A_Narrative_Review_of_the_Impact_of_AI_on_Film_and_TV_Production) | error | 7 | 0 | 0 | 0 | 7 |
| [[48]](https://copyrightinformation.org/ai/copyright-office-ai-guidance/) | downloaded | 7 | 4 | 3 | 0 | 0 |
| [[55]](https://ailawsuittracker.com/international-ai-lawsuits/) | downloaded | 7 | 2 | 4 | 1 | 0 |
| [[91]](https://blog.promise.legal/ai-generated-content-film-legal-compliance-2026/) | downloaded | 7 | 1 | 6 | 0 | 0 |
| [[1]](https://www.precedenceresearch.com/generative-ai-in-the-media-and-entertainment-market) | downloaded | 6 | 4 | 1 | 1 | 0 |
| [[23]](https://everything-pr.com/the-lawsuit-war-room-every-major-ai-copyright-case-mapped-47-publishers-8-ai-companies-and-the-trial-that-will-reshape-the-internet) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[53]](https://natlawreview.com/article/output-v-input-copyright-ownership-challenges-era-artificial-intelligence) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[71]](https://www.afterlife.ai/no-fakes-act-explained) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[11]](https://www.cbc.ca/news/entertainment/val-kilmer-ai-trailer-9.7166746) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[74]](https://stablediffusionfrivolous.com/deepfakes/right-of-publicity/) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[3]](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/tmt-predictions-hollywood-cautious-of-genai-adoption.html) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[21]](https://dynamoi.com/learn/ai-music-distribution/ai-music-copyright-cases-timeline) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[35]](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[75]](https://talkmie.com/news/no-fakes-act-voice-likeness-us-status) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[79]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[89]](https://www.resemble.ai/resources/generative-ai-watermarking-opportunities-challenges) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[4]](https://www.bfi.org.uk/news/generative-ai-screen-industries) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[12]](https://www.theguardian.com/film/val-kilmer) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[15]](https://www.researchgate.net/publication/391690363_The_Impact_Of_Ai-powered_Dubbing_And_Localization_On_Global_Media) | error | 3 | 0 | 0 | 0 | 3 |
| [[18]](https://en.wikipedia.org/wiki/2024%E2%80%932025_SAG-AFTRA_video_game_strike) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[39]](https://aifilmsafe.com/compliance-calendar) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[49]](https://accordshield.com/blog-who-owns-ai-generated-code-content) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[51]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[52]](https://usfblogs.usfca.edu/centerforlawtechsocialgood/from-studio-to-silicon-human-authorship-ai-generated-art-and-the-supreme-court/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[61]](https://ailawsuittracker.com/cases/disney-enterprises-inc-v-midjourney-inc-2-25-cv-05275/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[68]](https://www.fredlaw.com/alert-federal-court-dismisses-trademark-and-copyright-claims-over-ai-voice-clones-but-leaves-door-open-under-state-publicity-law) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[73]](https://air.io/en/youtube-hacks/youtube-ai-policy-2026-likeness-detection-and-the-no-fakes-act-what-creators-need-to-know) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[77]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[80]](https://ppc.land/non-eu-advertisers-face-3-eu-fines-for-unlabelled-ai-deep-fake-ads/) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[90]](https://www.datamintelligence.com/research-report/digital-watermarking-market) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[2]](https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Media_Entertainment_and_Sport_2025.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[7]](https://www.cbsnews.com/news/ai-actor-hollywood-tilly-norwood-stirs-outrage/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[8]](https://vgtimes.com/movies-and-tv-series/134353-ai-actress-tilly-norwood-dubbed-the-new-scarlett-johansson-sparks-controversy-in-hollywood.html) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[9]](https://www.resultsense.com/news/2025-09-30-tilly-norwood-ai-actor-hollywood-controversy/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[10]](https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1204&context=honors202029) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[14]](https://www.gravyforthebrain.com/voice-acting-in-2025-2026-trends-insights-and-the-future/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[16]](https://www.morningstar.com/news/business-wire/20260826543251/new-data-shows-audiences-are-embracing-ai-dubbing-heres-what-the-media-industry-should-know) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[24]](https://www.universalmusic.com/universal-music-group-and-elevenlabs-announce-multi-year-strategic-agreement-beginning-with-a-new-licensed-ai-music-creation-platform/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[30]](https://productionguild.com/download/file/aGtkbXlabXN0TUVSekJYcXo4UDI3Zz09/sag-aftra-strike-2023_summary-of-agreed-terms/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[32]](https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[34]](https://www.dglaw.com/new-sag-aftra-commercials-contract-is-now-in-effect/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[38]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[43]](https://slator.com/sag-aftra-requires-ai-dubbing-consent/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[45]](https://www.theguardian.com/technology/artificialintelligenceai) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[60]](https://law.duke.edu/centers/cspd/2026supplement.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[65]](https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[67]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[78]](https://www.sagaftra.org/sag-aftra-ai-bargaining-and-policy-work-timeline) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[82]](https://asee.io/blog/eu-ai-act-transparency-rules-customer-service/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[83]](https://www.biometricupdate.com/202611/deepfake-era-puts-likeness-in-legal-spotlight-as-eu-works-to-define-whats-allowed) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[88]](https://adjuris.ro/books/plbs/13.pdf) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[92]](https://aifilmsafe.com/glossary) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[17]](https://mashable.com/article/fortnite-darth-vader-ai-james-earl-jones) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://www.youtube.com/watch?v=gGG7dpHVkrA) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://www.mckoolsmith.com/newsroom-ailitigation-45) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[22]](https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[25]](https://elevenlabs.io/blog/umg) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://routenote.com/blog/universal-music-group-and-elevenlabs-join-forces-on-new-ai-music-platform/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[27]](https://en.wikipedia.org/wiki/2023_SAG-AFTRA_strike) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[28]](https://www.sagaftra.org/sites/default/files/sa_documents/TV-Theatrical_23_Summary_Agreement_Final.pdf) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[31]](https://www.sagaftra.org/contracts-industry-resources/contracts/2024-sound-recordings-code) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[33]](https://www.sagaftra.org/sites/default/files/Sound%20Recordings%20Code%20Appendix%20on%20Artificial%20Intelligence.pdf) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[36]](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://legalmoveslawfirm.com/sag-aftra-ima/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.screendaily.com/news/sag-aftra-national-members-ratify-new-four-year-deal/5217462.article) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[42]](https://www.sagaftra.org/contracts-industry-resources/television/2026-television-animation-agreements) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[44]](https://www.equity.org.uk/news/2026/equity-congratulates-sag-aftra-and-says-ai-standards-must-become-uk-benchmark) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[46]](https://ai.ecu.edu/copy-ai-u-s-copyright-office-guidance/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[47]](https://www.skadden.com/insights/publications/2025/02/copyright-office-publishes-report) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[50]](https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[54]](https://legalblogs.wolterskluwer.com/copyright-blog/beijing-internet-court-grants-copyright-to-ai-generated-image-for-the-first-time/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[56]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[58]](https://uk.practicallaw.thomsonreuters.com/w-046-9134?transitionType=Default&contextData=(sc.Default)) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[59]](https://www.crowell.com/en/insights/client-alerts/us-copyright-office-releases-third-report-on-ai-and-copyright-addressing-training-ai-models-with-copyrighted-materials) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[62]](https://www.theguardian.com/technology/2025/jun/11/disney-universal-ai-lawsuit) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[63]](https://www.law.georgetown.edu/tech-institute/research-insights/insights/disney-nbc-universal-and-dreamworks-file-major-ip-lawsuit-against-ai-image-generator-midjourney/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[64]](https://rpjlaw.com/hollywood-strikes-back-disney-and-universal-sue-a-i-platform-midjourney-for-copyright-infringement/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[66]](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt458646ff62fb9d7f/6a1f2d89339eecced0b42ca0/TH_13.00-14.00_Copyright_and_wrong.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[69]](https://arxiv.org/html/2606.26111v1) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[70]](https://ai.miraheze.org/wiki/Lovo) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[72]](https://www.chartlex.com/blog/business/ai-voice-cloning-music-legal-2026) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[76]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-1-Digital-Replicas-Report.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[81]](https://www.regulation-ai.eu/en/transparency-obligations/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[84]](https://www.europarl.europa.eu/RegData/etudes/ATAG/2026/782611/EPRS_ATA(2026)782611_EN.pdf) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[85]](https://www.researchgate.net/publication/401736407_Copyright_or_personality_rights_A_critical_analysis_of_Denmark's_approach_to_deepfakes) | error | 1 | 0 | 0 | 0 | 1 |
| [[86]](https://english.bjinternetcourt.gov.cn/2024-04/24/c_706.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[87]](https://www.marks-clerk.com/insights/latest-insights/102kv8h-china-new-ruling-on-non-infringement-of-personality-rights-by-ai-voice-does-it-signal-a-shift-in-protection-standards/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[93]](https://www.reedsmith.com/articles/entertainment-media-guide-to-ai-three-years-on/games/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[57]](https://www.jenner.com/en/news-insights/client-alerts/us-copyright-office-releases-pre-publication-version-of-report-on-copyright-issues-in-generative-ai-training) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[6]](https://www.theguardian.com/film/2026/oct/20/ai-actors-val-kilmer-as-deep-as-the-grave-tilly-norwood) | #27, #29–33 | #2, #23 | #19 | `#27` judging by the extended glimpse of the film released earlier this year: it looks like a thirtysomething Kilmer, if a robot version had been sent back to the 19… |
| [[13]](https://flauntaudio.com/ai-voice-actor-statistics-2026/) | #35–39, #41 | #57 | #34, #40 | `#35` 21% of voice actors say they have knowingly lost a job to a synthetic voice (NAVA, 2026). Only **13%** have agreed to let a third party create a synthetic vers… |
| [[48]](https://copyrightinformation.org/ai/copyright-office-ai-guidance/) | #68, #70, #72, #74 | #3, #67, #73 | — | `#68` Thaler v. Perlmutter. On March 18, 2025, the D.C. Circuit held that the Copyright Act "requires all eligible work to be authored in the first instance by a hum… |
| [[55]](https://ailawsuittracker.com/international-ai-lawsuits/) | #86, #89 | #76, #87–88, #106 | #101 | `#86` Outside the United States, AI cases are decided under different copyright and privacy laws, and the answers have differed. A Munich court has held that a model… |
| [[91]](https://blog.promise.legal/ai-generated-content-film-legal-compliance-2026/) | #18 | #0, #3, #75, #107, #110–111 | — | `#18` ### Digital Replicas of Performers If you create or use a digital replica of a performer's voice or likeness—whether through employment-based replication (the… |
| [[1]](https://www.precedenceresearch.com/generative-ai-in-the-media-and-entertainment-market) | #6–8, #13 | #5 | #4 | `#6` The global generative AI in the media and entertainment market size accounted for USD 2.24 billion in 2025 and is predicted to increase from USD 2.8 billion in… |
| [[23]](https://everything-pr.com/the-lawsuit-war-room-every-major-ai-copyright-case-mapped-47-publishers-8-ai-companies-and-the-trial-that-will-reshape-the-internet) | #51, #82, #89 | #77, #84, #88 | — | `#51` Sony Music v. Udio (S.D.N.Y., Jul. 2026). Second filing covering 30,117 additional sound recordings. Alleges stream-ripping from YouTube. [...] Sony Music v. S… |
| [[53]](https://natlawreview.com/article/output-v-input-copyright-ownership-challenges-era-artificial-intelligence) | #79–81 | #67, #73, #77 | — | `#79` Those are fact-intensive questions. Recent decisions have begun to draw the lines, but the appellate courts have not yet supplied a comprehensive framework for… |
| [[71]](https://www.afterlife.ai/no-fakes-act-explained) | #98–99 | #93, #95 | #34, #100 (s/ aval.) | `#98` It cleared the Senate Judiciary Committee in June, then stalled on the Senate floor on September 30. ... The House version, H.R. 8915, has not had a committee… |
| [[11]](https://www.cbc.ca/news/entertainment/val-kilmer-ai-trailer-9.7166746) | #24–26 | #21 | #19 | `#24` The use of generative AI to recreate Kilmer for the historical drama, based on archaeologists Ann and Earl Morris, became a hot-button issue when the filmmaker… |
| [[74]](https://stablediffusionfrivolous.com/deepfakes/right-of-publicity/) | #93–94 | #90, #95, #97 | — | `#93` There is no federal right of publicity. Each state decides whether the right exists, what it covers, and whether it survives death. ... The table covers the fo… |
| [[3]](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/tmt-predictions-hollywood-cautious-of-genai-adoption.html) | #11 | #1, #5, #9 | — | `#11` Although studios may have been quick to experiment with gen AI content creation, they will likely be more cautious in moving it into full production. Some reas… |
| [[21]](https://dynamoi.com/learn/ai-music-distribution/ai-music-copyright-cases-timeline) | #48 | #2, #45, #49 | — | `#48` On June 24, 2024, the Recording Industry Association of America (RIAA) announced two copyright infringement cases on behalf of major record labels. ### Univers… |
| [[75]](https://talkmie.com/news/no-fakes-act-voice-likeness-us-status) | #98 | #3, #99 | #100 (s/ aval.) | `#98` The United States still has no federal law on AI copies of a person's voice or face. ... As of late October 2026: neither chamber has held a recorded vote. |
| [[79]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | — | #101–103 | #0 | `#0` four separate legal frameworks—copyright registration, union consent rules, festival disclosure mandates, and right-of-publicity laws—are converging in 2026 to… |
| [[89]](https://www.resemble.ai/resources/generative-ai-watermarking-opportunities-challenges) | — | #3, #107–108, #111 | — | `#3` AI watermarking embeds or attaches a machine-readable marker to AI-generated content. [...] C2PA Content Credentials [...] Source and edit history through sign… |
| [[4]](https://www.bfi.org.uk/news/generative-ai-screen-industries) | #12 | #1, #9 | — | `#12` The screen sector is already seeing examples of public sector AI-driven service innovation, based on principles of responsible AI such as the Intelligent Syste… |
| [[12]](https://www.theguardian.com/film/val-kilmer) | #28 | #25 | #24 | `#28` September 2026 Reanimated AI Greta Garbo stars again … in a ball-bearing advert Relatives of Hollywood legend say her doppelganger could now be used for more g… |
| [[18]](https://en.wikipedia.org/wiki/2024%E2%80%932025_SAG-AFTRA_video_game_strike) | #46, #58 | #45 | — | `#46` On May 19, 2025, SAG-AFTRA filed an unfair labor practice charge on Llama Productions, a subsidiary of Epic Games, alleging the company replaced actors' work b… |
| [[39]](https://aifilmsafe.com/compliance-calendar) | — | #60–61, #64 | — | `#60` Companies must notify WGA before licensing scripts for GAI training. |
| [[49]](https://accordshield.com/blog-who-owns-ai-generated-code-content) | — | #70–71, #75 | — | `#70` The guidance compares prompts to "instructions to a commissioned artist" — they say what you want, but the system decides how it is expressed. [...] Its Januar… |
| [[51]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | #69, #72 | #68 | — | `#69` On March 18, 2025, a D.C. Circuit panel affirmed the district court's ruling. Although the Copyright Act does not explicitly define "author," the court found t… |
| [[52]](https://usfblogs.usfca.edu/centerforlawtechsocialgood/from-studio-to-silicon-human-authorship-ai-generated-art-and-the-supreme-court/) | #72, #75 | #73 | — | `#72` The case that's going to define the line—the one Thaler was always too extreme to draw—is Allen v. Perlmutter, sitting right now in the District of Colorado. [… |
| [[61]](https://ailawsuittracker.com/cases/disney-enterprises-inc-v-midjourney-inc-2-25-cv-05275/) | — | #3, #84–85 | — | `#3` Active — Midjourney moved for judgment on the pleadings on Disney's contributory infringement claim July 22, 2026. [...] Stakes: Studio IP + injunction |
| [[68]](https://www.fredlaw.com/alert-federal-court-dismisses-trademark-and-copyright-claims-over-ai-voice-clones-but-leaves-door-open-under-state-publicity-law) | — | #90–92 | — | `#90` the court rejected these claims, holding that copyright protection does not extend to voice per se or to mere imitation of vocal characteristics. |
| [[73]](https://air.io/en/youtube-hacks/youtube-ai-policy-2026-likeness-detection-and-the-no-fakes-act-what-creators-need-to-know) | #94 | #95 | #100 (s/ aval.) | `#94` It has been law since July 1, 2024, and despite the name, it protects every individual rather than only recording artists. ... Liability extends to whoever dis… |
| [[77]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | — | — | #96–97, #99 | — |
| [[80]](https://ppc.land/non-eu-advertisers-face-3-eu-fines-for-unlabelled-ai-deep-fake-ads/) | #102 | #103 | #111 | `#102` November 12, 2026 : The guidelines are published in the Official Journal of the European Union as C/2026/6005. ... December 2, 2026 : Deadline for generative A… |
| [[90]](https://www.datamintelligence.com/research-report/digital-watermarking-market) | #108–109 | — | #107 | `#108` C2PA-based Content Credentials can establish a signed record of who created content, what tools were involved and how an asset changed over time. Adobe describ… |
| [[2]](https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Media_Entertainment_and_Sport_2025.pdf) | #10 | #9 | — | `#10` 92% of creators say they have already used genAI in some capacity (vs. only 34% in November 2023). |
| [[7]](https://www.cbsnews.com/news/ai-actor-hollywood-tilly-norwood-stirs-outrage/) | — | #20–21 | — | `#20` Van der Velden, who is also the founder of the AI production studio Particle6, promoted Tilly Norwood last month at the Zurich Summit, the industry sidebar of… |
| [[8]](https://vgtimes.com/movies-and-tv-series/134353-ai-actress-tilly-norwood-dubbed-the-new-scarlett-johansson-sparks-controversy-in-hollywood.html) | — | #20–21 | — | `#20` She was developed by Eline Van der Velden, founder of the Dutch company Particle 6 Productions. Recently, Van der Velden announced the launch of a talent studi… |
| [[9]](https://www.resultsense.com/news/2025-09-30-tilly-norwood-ai-actor-hollywood-controversy/) | #22 | #20 | — | `#22` Norwood's only performance to date—a two-minute AI-generated sketch—has garnered modest viewership of approximately 200,000 views over two months, significantl… |
| [[10]](https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1204&context=honors202029) | — | #20, #23 | — | `#20` In late 2025, weekly trade publication Variety Magazine reported on the announcement of a new acting talent in Hollywood: Tilly Norwood. Norwood is an industry… |
| [[14]](https://www.gravyforthebrain.com/voice-acting-in-2025-2026-trends-insights-and-the-future/) | — | #40, #44 | — | `#40` 2025 has shown that AI can support voice work in some sectors, but will not fully replace it. Human voices will continue to dominate emotionally driven content |
| [[16]](https://www.morningstar.com/news/business-wire/20260826543251/new-data-shows-audiences-are-embracing-ai-dubbing-heres-what-the-media-industry-should-know) | — | #42, #44 | — | `#42` the media and entertainment industry has hesitated to use AI-voiced dubbing |
| [[24]](https://www.universalmusic.com/universal-music-group-and-elevenlabs-announce-multi-year-strategic-agreement-beginning-with-a-new-licensed-ai-music-creation-platform/) | #50 | #45 | — | `#50` Universal Music Group (UMG), the world leader in music-based entertainment, and ElevenLabs, the leading AI audio research and product company, today announced… |
| [[29]](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | #53–54 | — | — | `#53` In the 2023 TV/Theatrical Contracts negotiations, SAG-AFTRA secured protections for the creation and use of digital replicas of performers... An "Employment-Ba… |
| [[30]](https://productionguild.com/download/file/aGtkbXlabXN0TUVSekJYcXo4UDI3Zz09/sag-aftra-strike-2023_summary-of-agreed-terms/) | #54 | #53 | — | `#54` 48−hour advance notice prior to services creation; consent required: clear and conspicuous, separately signed or initialed in employment contract or separate s… |
| [[34]](https://www.dglaw.com/new-sag-aftra-commercials-contract-is-now-in-effect/) | — | #55, #57 | — | `#55` The new Commercials Contract introduces a formal framework for the ethical use of digital replicas and synthetic performers – requiring clear consent and addit… |
| [[38]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | — | #60–61 | — | `#60` The 2026 MBA preserves all of the protections negotiated in 2023 and adds requirements if the companies license writers’ scripts or the produced projects based… |
| [[43]](https://slator.com/sag-aftra-requires-ai-dubbing-consent/) | #65 | #2 | — | `#65` SAG-AFTRA members approved the 2026 Television Animation Agreement and the 2026 Basic Cable Animation Agreement, which run through June 2030 and cover animated… |
| [[45]](https://www.theguardian.com/technology/artificialintelligenceai) | — | — | #52, #66 | — |
| [[60]](https://law.duke.edu/centers/cspd/2026supplement.pdf) | #79 | #81 | — | `#79` this ruling does not stand for the proposition that Meta's use of copyrighted materials to train its language models is lawful. It stands only for the proposit… |
| [[65]](https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing) | #87 | #86 | — | `#87` Getty applied for permission to appeal the dismissal of its secondary copyright infringement claim. Justice Smith granted permission in full. [...] At a conseq… |
| [[67]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | — | #91–92 | — | `#91` The court distinguished between using a voice as the product itself versus using a voice as a brand to identify the source or origin of the product. Here, plai… |
| [[82]](https://asee.io/blog/eu-ai-act-transparency-rules-customer-service/) | — | #102–103 | — | `#102` Most of this became enforceable on 2 August 2026. Providers of systems already on the market before that date have until 2 December 2026 to meet the machine-re… |
| [[83]](https://www.biometricupdate.com/202611/deepfake-era-puts-likeness-in-legal-spotlight-as-eu-works-to-define-whats-allowed) | — | #101, #104 | — | `#101` While the AI Act sets transparency requirements for deepfakes and the Digital Services Act governs platforms' handling of illegal content, there is no general… |
| [[88]](https://adjuris.ro/books/plbs/13.pdf) | — | #105–106 | — | `#105` Denmark has attracted particular attention for its legislative proposal currently under public consultation. The draft amendment to the Copyright Act seeks to… |
| [[92]](https://aifilmsafe.com/glossary) | #110 | #111 | — | `#110` As of 2026, major festivals including Sundance, TIFF, Cannes, Venice, and Berlin have implemented various levels of AI transparency requirements. Requirements… |
| [[17]](https://mashable.com/article/fortnite-darth-vader-ai-james-earl-jones) | #46 | — | — | `#46` developer Epic Games announced in a blog post that Darth Vader is back in Fortnite as a recruitable boss character […] You can voice chat with Darth Vader and… |
| [[19]](https://www.youtube.com/watch?v=gGG7dpHVkrA) | #47 | — | — | `#47` Actor Scarlett Johansson has hired a lawyer after ChatGPT debuted the voice of a new interactive assistant that she says sounds similar to hers. While the Open… |
| [[20]](https://www.mckoolsmith.com/newsroom-ailitigation-45) | — | #48 | — | `#48` The RIAA on behalf of the major record labels filed their lawsuit in the federal district Court in Massachusetts on June 24th, 2024, for mass copyright infring… |
| [[22]](https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform/) | — | #49 | — | `#49` In a landmark move late Wednesday (October 29) evening, Universal Music Group announced that it has settled its copyright infringement litigation against AI mu… |
| [[25]](https://elevenlabs.io/blog/umg) | #50 | — | — | `#50` We've entered a multi-year licensing agreement and strategic collaboration with Universal Music Group (UMG) [...] The platform will give fans new ways to co-cr… |
| [[26]](https://routenote.com/blog/universal-music-group-and-elevenlabs-join-forces-on-new-ai-music-platform/) | — | #50 | — | `#50` The partnership, announced on September 10, 2026, combines UMG's extensive music catalogue with ElevenLabs' AI audio technology. [...] The platform will allow… |
| [[27]](https://en.wikipedia.org/wiki/2023_SAG-AFTRA_strike) | — | #53 | — | `#53` From July 14 to November 9, 2023, the American actors' union Screen Actors Guild–American Federation of Television and Radio Artists (SAG-AFTRA) went on strike… |
| [[36]](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di) | #59 | — | — | `#59` The IMA runs for six years, from November 8, 2022 through October 31, 2028. ... employers cannot grab this consent at the time of initial employment for future… |
| [[37]](https://legalmoveslawfirm.com/sag-aftra-ima/) | #59 | — | — | `#59` Performers can suspend consent for generating new material during a strike ... If you use digital replicas for "Real-Time Generation" (like an AI-powered chatb… |
| [[41]](https://www.screendaily.com/news/sag-aftra-national-members-ratify-new-four-year-deal/5217462.article) | — | #62 | — | `#62` SAG-AFTRA national members have ratified the four-year 2026 TV/Theatrical Agreement with the studios and streamers after a 91.4% vote in favour of the measure. |
| [[44]](https://www.equity.org.uk/news/2026/equity-congratulates-sag-aftra-and-says-ai-standards-must-become-uk-benchmark) | — | — | #66 ⚡ | `#66` There are currently no AI protections in the Equity – PACT agreement. Equity is in negotiations with PACT seeking widespread improvements in pay, royalties, an… |
| [[46]](https://ai.ecu.edu/copy-ai-u-s-copyright-office-guidance/) | — | #70 | — | `#70` Released January 29, 2025 [...] Works created entirely by AI—even with detailed prompting—are **not eligible** for copyright. |
| [[47]](https://www.skadden.com/insights/publications/2025/02/copyright-office-publishes-report) | #71 | — | — | `#71` The Report concludes that if the human-generated work is perceptible in the AI-generated output, the human can claim authorship of, and copyright in, the perce… |
| [[50]](https://law.justia.com/cases/federal/appellate-courts/cadc/23-5233/23-5233-2025-03-18.html) | #69 | — | — | `#69` The Creativity Machine cannot be the recognized author of a copyrighted work because the Copyright Act of 1976 requires all eligible work to be authored in the… |
| [[54]](https://legalblogs.wolterskluwer.com/copyright-blog/beijing-internet-court-grants-copyright-to-ai-generated-image-for-the-first-time/) | — | #76 | — | `#76` On November 27, 2023, the Beijing Internet Court (BIC) ruled in an infringement lawsuit (*Li v. Liu*) that an AI-generated image is copyrightable and that a pe… |
| [[56]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf) | #78 | — | — | `#78` the copying of expressive works from pirate sources in order to generate unrestricted content that competes in the marketplace, when licensing is reasonably av… |
| [[58]](https://uk.practicallaw.thomsonreuters.com/w-046-9134?transitionType=Default&contextData=(sc.Default)) | #78 | — | — | `#78` using a copyrighted work to train a GenAI system requires making multiple copies of the work, implicating the exclusive right of reproduction and in some cases… |
| [[59]](https://www.crowell.com/en/insights/client-alerts/us-copyright-office-releases-third-report-on-ai-and-copyright-addressing-training-ai-models-with-copyrighted-materials) | #78 | — | — | `#78` On May 9, 2025, the U.S. Copyright Office released the third (pre-publication) installment in a series of reports regarding the intersection of artificial inte… |
| [[62]](https://www.theguardian.com/technology/2025/jun/11/disney-universal-ai-lawsuit) | #83 | — | — | `#83` Disney and Universal are two of the biggest industry players thus far to sue over images and videos. |
| [[63]](https://www.law.georgetown.edu/tech-institute/research-insights/insights/disney-nbc-universal-and-dreamworks-file-major-ip-lawsuit-against-ai-image-generator-midjourney/) | #83 | — | — | `#83` this lawsuit marks the first time that major Hollywood studios have sued AI companies. |
| [[64]](https://rpjlaw.com/hollywood-strikes-back-disney-and-universal-sue-a-i-platform-midjourney-for-copyright-infringement/) | #84 | — | — | `#84` Disney and Universal have jointly filed a lawsuit in the U.S. District Court for the Central District of California against generative A.I. image platform Midj… |
| [[66]](https://assets.contentstack.io/v3/assets/bltd4dd5b2d705252bc/blt458646ff62fb9d7f/6a1f2d89339eecced0b42ca0/TH_13.00-14.00_Copyright_and_wrong.pdf) | — | #87 | — | `#87` Model weights are not "copies" of training images and do not store or reproduce the training data; they reflect learned patterns from training. |
| [[69]](https://arxiv.org/html/2606.26111v1) | — | #91 | — | `#91` The court held that Section 114(b) bars infringement claims absent sampling of their actual recordings [12]. The 7th Circuit affirmed, emphasizing that the cop… |
| [[72]](https://www.chartlex.com/blog/business/ai-voice-cloning-music-legal-2026) | #94 | — | — | `#94` Tennessee's ELVIS Act, effective July 1, 2024, was the first US law to cover a simulation of a person's voice, and it reaches tool distributors as well as uplo… |
| [[76]](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-1-Digital-Replicas-Report.pdf) | — | #99 | — | `#99` The Office concludes that the time has come to adopt such a law at the federal level. ... We recommend that Congress establish a federal right that protects al… |
| [[81]](https://www.regulation-ai.eu/en/transparency-obligations/) | — | #102 | — | `#102` Article 50 entered into application on 2 August 2026 and is enforced by national market surveillance authorities. |
| [[84]](https://www.europarl.europa.eu/RegData/etudes/ATAG/2026/782611/EPRS_ATA(2026)782611_EN.pdf) | — | #105 | — | `#105` Denmark has prepared amendments to national copyright rules to grant people more control over their voices and images in AI-generated deepfakes. It proposes a… |
| [[86]](https://english.bjinternetcourt.gov.cn/2024-04/24/c_706.htm) | — | #106 | — | `#106` A Beijing court has issued a landmark ruling that imitating someone's voice through AI without their permission constitutes an infringement of their personal r… |
| [[87]](https://www.marks-clerk.com/insights/latest-insights/102kv8h-china-new-ruling-on-non-infringement-of-personality-rights-by-ai-voice-does-it-signal-a-shift-in-protection-standards/) | — | #106 | — | `#106` In April 2024, the Beijing Internet Court issued China's first ruling on AI voice infringement... This legally effective ruling affirmed that voices recognizab… |
| [[93]](https://www.reedsmith.com/articles/entertainment-media-guide-to-ai-three-years-on/games/) | — | #103 | — | `#103` Synthetic voices, a de-aged or resurrected performer, or a fully AI-generated actor can therefore constitute a 'deepfake' even where all underlying consent has… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.sagaftra.org/sites/default/files/sa_documents/TV-Theatrical_23_Summary_Agreement_Final.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/sa_documents/TV-Theatrical_23_Summary_Agreement_Final.pdf (PDF, sem fallback via playwright)
- https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf — HTTP 403 em https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf (PDF, sem fallback via playwright)
- https://www.sagaftra.org/sites/default/files/Sound%20Recordings%20Code%20Appendix%20on%20Artificial%20Intelligence.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/Sound%20Recordings%20Code%20Appendix%20on%20Artificial%20Intelligence.pdf (PDF, sem fallback via playwright)

### Bloqueadas por barreira de acesso

- https://www.sagaftra.org/contracts-industry-resources/contracts/2024-sound-recordings-code — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930066-GRU 1794957224 1201445468 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930079-GRU 1794957237 1600457280 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930043-GRU 1794957244 1602384994 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/television/2026-television-animation-agreements — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930050-GRU 1794957252 1200372924 Varnish cache server
- https://ai.miraheze.org/wiki/Lovo — no_content — barreira de acesso (no_content): Verification successful. Waiting for ai.miraheze.org to respond Enable JavaScript and cookies to continue
- https://www.sagaftra.org/sag-aftra-ai-bargaining-and-policy-work-timeline — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930049-GRU 1794957292 2310515737 Varnish cache server

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-2`** [6] [21] [40] [43]
  - Trecho: While fully synthetic performers and unauthorized voice clones have triggered fierce cultural backlash and litigation, union agreements and catalog deals have increasingly converted generative tools from low-cost replac…
  - Justificativa: A evidência sustenta as partes essenciais da afirmação: (1) backlash cultural contra performers sintéticos — reação de 'revulsion' à AI 'starlet' Tilly Norwood, Emily Blunt a chamando de 'really, really scary', contrové…
  - Suporte veio de: [43] [21] [6]
  - Evidência: “Members of the Screen Actors Guild-American Federation of Television and Radio Artists union (SAG-AFTRA) have ratified new television animation contracts that strengthen protections for actors regarding the use of AI vo…”
  - Não coberto pela evidência: A afirmação de que os acordos sindicais e de catálogo ocorreram 'increasingly' ao longo do tempo (tendência temporal) não é explicitamente estabelecida pela evidência, que descreve eventos isolados (contratos SAG-AFTRA 2026, settlements de 2025).; A frase 'low-cost replacements' como caracterização do uso anterior das ferramentas generativas é apenas indiretamente suportada; a evidência menciona produção 'far cheaper' e atalhos, mas não descreve explicitamente que as ferramentas eram usadas como substituições de baixo custo antes dos acordos.; A evidência não menciona explicitamente 'unauthorized voice clones' como objeto de litígio específico (os processos citados tratam de treinamento com música protegida por direitos autorais, não de clonagem de voz); a menção a voice cloning não autorizado aparece apenas no contexto da proposta legislativa No AI FRAUD Act.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [43] | parcial | Members of the Screen Actors Guild-American Federation of Television and Radio Artists union (SAG-AFTRA) have ratified… |
    | [21] | parcial | On June 24, 2024, the Recording Industry Association of America (RIAA) announced two copyright infringement cases on be… |
    | [6] | parcial | Many reacted with revulsion to last year’s unveiling of AI “starlet” Tilly Norwood. ... Emily Blunt described her as “r… |

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-3`** [48] [61] [75] [89] [91]
  - Trecho: At the same time, unresolved legal questions—including pending federal court rulings on prompt-based copyrightability, fair use in studio-character training, and stalled federal digital-replica legislation—require enter…
  - Justificativa: A afirmacao e sustentada pela evidencia em seus elementos essenciais. (1) 'Pending federal court rulings on prompt-based copyrightability' e confirmada por Allen v. Perlmutter, sem decisao ate novembro de 2026. (2) 'Sta…
  - Suporte veio de: [91] [75] [89] [48] [61]
  - Evidência: “Allen v. Perlmutter. Artist Jason Allen sued in federal court in Colorado on September 26, 2024, after the Office's Review Board refused his Midjourney image on September 5, 2023. The case asks whether detailed promptin…”
  - Não coberto pela evidência: 'fair use in studio-character training' — a evidencia discute fair use em treinamento (Parte 3) e litigios envolvendo personagens de estudio (Disney/Universal v. Midjourney) separadamente, mas nao combina explicitamente os dois conceitos nessa formulacao especifica; 'entertainment companies' — a evidencia foca primariamente em independent filmmakers e AI product teams, nao em 'entertainment companies' de forma ampla
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [91] | parcial | AB 2602 requires that contracts involving the use of AI-generated digital replicas of a performer's voice or likeness m… |
    | [75] | parcial | On 30 September 2026: a request to pass it by unanimous consent is blocked by an objection from Senator Ted Cruz, who c… |
    | [89] | parcial | AI watermarking embeds or attaches a machine-readable marker to AI-generated content. [...] C2PA Content Credentials [.… |
    | [48] | parcial | The case asks whether detailed prompting can be authorship. [...] the docket showed no ruling on the merits when we che… |
    | [61] | parcial | Active — Midjourney moved for judgment on the pleadings on Disney's contributory infringement claim July 22, 2026. [...… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta parcialmente a afirmação: o caso Allen v. Perlmutter (prompt-based copyrightability) e o NO FAKES Act (stalled federal…") — cascata: baseline → context_expansion
- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-5`** [1] [3]
  - Trecho: Commercial spending on generative AI across media and entertainment is expanding rapidly, though adoption differs sharply by organizational scale.
  - Justificativa: A evidência sustenta ambas as partes da afirmação. O crescimento rápido do mercado é confirmado pelos dados de tamanho de mercado (CAGR de 25,2% de 2026 a 2035, de USD 2,8 bi para USD 21,2 bi). A diferença de adoção por…
  - Suporte veio de: [1] [3]
  - Evidência: “The global generative AI in the media and entertainment market size accounted for USD 2.24 billion in 2025 and is predicted to increase from USD 2.8 billion in 2026 to approximately USD 21.2 billion by 2035, expanding a…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | The global generative AI in the media and entertainment market size accounted for USD 2.24 billion in 2025 and is predi… |
    | [3] | parcial | In 2025, Deloitte predicts that the biggest TV and film studios—especially those in the United States and European Unio… |

### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-0`** [5] [40] [79] [91]
  - Trecho: As of November 2026, generative artificial intelligence in entertainment has moved past unregulated experimentation into a tightly contested regime governed by collective labor contracts, fractured copyright doctrine, s…
  - Justificativa: A evidência sustenta vários elementos da afirmação (contratos trabalhistas coletivos via SAG-AFTRA, doutrina de copyright fragmentada via Copyright Office e Thaler v. Perlmutter, leis de semelhança estaduais e supranaci…
  - Suporte veio de: [91] [79]
  - Evidência: “four separate legal frameworks—copyright registration, union consent rules, festival disclosure mandates, and right-of-publicity laws—are converging in 2026 to create a compliance landscape”
  - Não coberto pela evidência: 'emerging licensing markets' — não há menção a mercados de licenciamento na evidência; 'moved past unregulated experimentation' — a evidência não caracteriza o período anterior como 'experimentação não regulamentada'; 'As of November 2026' — a data específica de novembro de 2026 não aparece na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [79] | ausente | — |
    | [91] | parcial | four separate legal frameworks—copyright registration, union consent rules, festival disclosure mandates, and right-of-… |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [10] [56] [58] [3] [60] [76] [66] [69] [59] [57] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-1`** [3] [4] [5]
  - Trecho: Across film, television, video games, audiobooks, and recorded music, adoption has bifurcated between rapid deployment by independent creators or social platforms and cautious, contract-bound integration inside major st…
  - Justificativa: A evidência sustenta fortemente a bifurcação entre criadores independentes (adoção rápida) e grandes estúdios (adoção cautelosa, com proteções contratuais) para filme, TV e jogos de vídeo. No entanto, a afirmacao lista…
  - Suporte veio de: [3]
  - Evidência: “independent content creators and social media platforms are moving quickly to adopt gen AI into their workflows and content”
  - Não coberto pela evidência: audiobooks — não há menção a audiobooks em nenhuma parte da evidência; recorded music — não há menção a adoção de IA generativa em música gravada (apenas menção a 'music labels' processando modelos públicos, o que não equivale a adoção no setor de música gravada)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | independent content creators and social media platforms are moving quickly to adopt gen AI into their workflows and con… |
    | [4] | parcial | Generative AI is lowering traditional barriers to entry in the UK screen sector – enabling individuals and small teams… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-4`** [1] [5]
  - Trecho: Readers assessing these industry trends should also note two evidentiary caveats: market-sizing forecasts derive primarily from commercial analytics firms, and widely cited labor-disruption estimates reflect executive e…
  - Justificativa: A evidência não menciona que as previsões de dimensionamento de mercado derivam primariamente de firmas de análise comercial, nem que estimativas de disrupção laboral refletem expectativas de executivos em vez de contag…
  - Não coberto pela evidência: market-sizing forecasts derive primarily from commercial analytics firms; widely cited labor-disruption estimates reflect executive expectations rather than verified counts of layoffs
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-66`** [44] [45]
  - Trecho: Internationally, UK union Equity observed the Los Angeles talks and secured a UK agreement reported on November 17, 2026, granting actors explicit consent and payment rights over digital replicas.
  - Justificativa: A janela afirma que 'There are currently no AI protections in the Equity – PACT agreement' e que a Equity ainda está em negociações com a PACT para obter proteções de IA, o que contradiz a alegação de que a Equity já 's…
  - Evidência: “There are currently no AI protections in the Equity – PACT agreement. Equity is in negotiations with PACT seeking widespread improvements in pay, royalties, and working conditions – including for the first time ever, AI…”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [44] | contradiz | There are currently no AI protections in the Equity – PACT agreement. Equity is in negotiations with PACT seeking wides… |

  - Verificação: reclassificado para CONTRADICTED na etapa `full_doc_scan` (baseline dizia: "A evidência confirma que Equity enviou delegação a LA e observou as negociações, mas contradiz ou não sustenta os demais elementos: (1) a p…") — cascata: baseline → context_expansion → full_doc_scan

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 5 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-14` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-15` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-16` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-17` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-43` — Referencia(s) citada(s) ['489282bf7e203d33'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-56` — Referencia(s) citada(s) ['15aae246033f2272', '350de76304ffe6f3', 'c96f1679e56af436'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-63` — Referencia(s) citada(s) ['0ad3078ef2adc633'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.