# Relatório de Auditoria — Gemini (ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z)

**Arquivo auditado:** `answers/Ingles/Gemini/Emergente/ia_generativa_entretenimento.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-18T10:36:36.298375+00:00 |
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
| **SUPPORTED** | 74 | 66.1% |
| **UNSUPPORTED** | 10 | 8.9% |
| **CONTRADICTED** | 1 | 0.9% |
| **SKIPPED** | 27 | 24.1% |
| **TOTAL** | 112 | 100.0% |

Sobre os 85 trechos citados auditados: SUPPORTED 87,05%, UNSUPPORTED 11,76%, CONTRADICTED 1,17%.

> **33 dos 74 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 33 estão **contados dentro** dos 74 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`18` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `3` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `1` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#104` On November 12, 2026, the European Parliament also passed a non-binding resolution urging EU Charter amendments protect… | [83] | [88] [84] [80] [82] [73] [71] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1321267 |
| **Média de tokens por requisição** | 15544.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 1/93 (1.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[6]](https://www.theguardian.com/film/2026/oct/20/ai-actors-val-kilmer-as-deep-as-the-grave-tilly-norwood) | downloaded | 9 | 6 | 1 | 1 | 1 |
| [[13]](https://flauntaudio.com/ai-voice-actor-statistics-2026/) | downloaded | 9 | 6 | 0 | 1 | 2 |
| [[40]](https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[5]](https://www.researchgate.net/publication/417398892_A_Narrative_Review_of_the_Impact_of_AI_on_Film_and_TV_Production) | inaccessible | 7 | 0 | 0 | 0 | 7 |
| [[48]](https://copyrightinformation.org/ai/copyright-office-ai-guidance/) | downloaded | 7 | 4 | 3 | 0 | 0 |
| [[55]](https://ailawsuittracker.com/international-ai-lawsuits/) | downloaded | 7 | 2 | 4 | 1 | 0 |
| [[91]](https://blog.promise.legal/ai-generated-content-film-legal-compliance-2026/) | downloaded | 7 | 0 | 5 | 0 | 2 |
| [[1]](https://www.precedenceresearch.com/generative-ai-in-the-media-and-entertainment-market) | downloaded | 6 | 4 | 1 | 0 | 1 |
| [[23]](https://everything-pr.com/the-lawsuit-war-room-every-major-ai-copyright-case-mapped-47-publishers-8-ai-companies-and-the-trial-that-will-reshape-the-internet) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[53]](https://natlawreview.com/article/output-v-input-copyright-ownership-challenges-era-artificial-intelligence) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[71]](https://www.afterlife.ai/no-fakes-act-explained) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[11]](https://www.cbc.ca/news/entertainment/val-kilmer-ai-trailer-9.7166746) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[74]](https://stablediffusionfrivolous.com/deepfakes/right-of-publicity/) | downloaded | 5 | 2 | 2 | 0 | 1 |
| [[3]](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/tmt-predictions-hollywood-cautious-of-genai-adoption.html) | downloaded | 4 | 1 | 2 | 0 | 1 |
| [[21]](https://dynamoi.com/learn/ai-music-distribution/ai-music-copyright-cases-timeline) | downloaded | 4 | 1 | 2 | 0 | 1 |
| [[35]](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[75]](https://talkmie.com/news/no-fakes-act-voice-likeness-us-status) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[79]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | downloaded | 4 | 0 | 3 | 0 | 1 |
| [[89]](https://www.resemble.ai/resources/generative-ai-watermarking-opportunities-challenges) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[4]](https://www.bfi.org.uk/news/generative-ai-screen-industries) | downloaded | 3 | 1 | 1 | 0 | 1 |
| [[12]](https://www.theguardian.com/film/val-kilmer) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[15]](https://www.researchgate.net/publication/391690363_The_Impact_Of_Ai-powered_Dubbing_And_Localization_On_Global_Media) | inaccessible | 3 | 0 | 0 | 0 | 3 |
| [[18]](https://en.wikipedia.org/wiki/2024%E2%80%932025_SAG-AFTRA_video_game_strike) | downloaded | 3 | 1 | 1 | 0 | 1 |
| [[39]](https://aifilmsafe.com/compliance-calendar) | downloaded | 3 | 0 | 1 | 0 | 2 |
| [[49]](https://accordshield.com/blog-who-owns-ai-generated-code-content) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[51]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[52]](https://usfblogs.usfca.edu/centerforlawtechsocialgood/from-studio-to-silicon-human-authorship-ai-generated-art-and-the-supreme-court/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[61]](https://ailawsuittracker.com/cases/disney-enterprises-inc-v-midjourney-inc-2-25-cv-05275/) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[68]](https://www.fredlaw.com/alert-federal-court-dismisses-trademark-and-copyright-claims-over-ai-voice-clones-but-leaves-door-open-under-state-publicity-law) | downloaded | 3 | 0 | 2 | 0 | 1 |
| [[73]](https://air.io/en/youtube-hacks/youtube-ai-policy-2026-likeness-detection-and-the-no-fakes-act-what-creators-need-to-know) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[77]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | downloaded | 3 | 0 | 0 | 2 | 1 |
| [[80]](https://ppc.land/non-eu-advertisers-face-3-eu-fines-for-unlabelled-ai-deep-fake-ads/) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[90]](https://www.datamintelligence.com/research-report/digital-watermarking-market) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[2]](https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Media_Entertainment_and_Sport_2025.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[7]](https://www.cbsnews.com/news/ai-actor-hollywood-tilly-norwood-stirs-outrage/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[8]](https://vgtimes.com/movies-and-tv-series/134353-ai-actress-tilly-norwood-dubbed-the-new-scarlett-johansson-sparks-controversy-in-hollywood.html) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[9]](https://www.resultsense.com/news/2025-09-30-tilly-norwood-ai-actor-hollywood-controversy/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[10]](https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1204&context=honors202029) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[14]](https://www.gravyforthebrain.com/voice-acting-in-2025-2026-trends-insights-and-the-future/) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[16]](https://www.morningstar.com/news/business-wire/20260826543251/new-data-shows-audiences-are-embracing-ai-dubbing-heres-what-the-media-industry-should-know) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[24]](https://www.universalmusic.com/universal-music-group-and-elevenlabs-announce-multi-year-strategic-agreement-beginning-with-a-new-licensed-ai-music-creation-platform/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | downloaded | 2 | 1 | 0 | 0 | 1 |
| [[30]](https://productionguild.com/download/file/aGtkbXlabXN0TUVSekJYcXo4UDI3Zz09/sag-aftra-strike-2023_summary-of-agreed-terms/) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[32]](https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[34]](https://www.dglaw.com/new-sag-aftra-commercials-contract-is-now-in-effect/) | downloaded | 2 | 0 | 0 | 0 | 2 |
| [[38]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[43]](https://slator.com/sag-aftra-requires-ai-dubbing-consent/) | downloaded | 2 | 0 | 0 | 0 | 2 |
| [[45]](https://www.theguardian.com/technology/artificialintelligenceai) | downloaded | 2 | 0 | 0 | 1 | 1 |
| [[60]](https://law.duke.edu/centers/cspd/2026supplement.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[65]](https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[67]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | downloaded | 2 | 0 | 1 | 0 | 1 |
| [[78]](https://www.sagaftra.org/sag-aftra-ai-bargaining-and-policy-work-timeline) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[82]](https://asee.io/blog/eu-ai-act-transparency-rules-customer-service/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[83]](https://www.biometricupdate.com/202611/deepfake-era-puts-likeness-in-legal-spotlight-as-eu-works-to-define-whats-allowed) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[88]](https://adjuris.ro/books/plbs/13.pdf) | downloaded | 2 | 0 | 1 | 0 | 1 |
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
| [[36]](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[37]](https://legalmoveslawfirm.com/sag-aftra-ima/) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[41]](https://www.screendaily.com/news/sag-aftra-national-members-ratify-new-four-year-deal/5217462.article) | downloaded | 1 | 0 | 0 | 0 | 1 |
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
| [[84]](https://www.europarl.europa.eu/RegData/etudes/ATAG/2026/782611/EPRS_ATA(2026)782611_EN.pdf) | downloaded | 1 | 0 | 0 | 0 | 1 |
| [[85]](https://www.researchgate.net/publication/401736407_Copyright_or_personality_rights_A_critical_analysis_of_Denmark's_approach_to_deepfakes) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[86]](https://english.bjinternetcourt.gov.cn/2024-04/24/c_706.htm) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[87]](https://www.marks-clerk.com/insights/latest-insights/102kv8h-china-new-ruling-on-non-infringement-of-personality-rights-by-ai-voice-does-it-signal-a-shift-in-protection-standards/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[93]](https://www.reedsmith.com/articles/entertainment-media-guide-to-ai-three-years-on/games/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[57]](https://www.jenner.com/en/news-insights/client-alerts/us-copyright-office-releases-pre-publication-version-of-report-on-copyright-issues-in-generative-ai-training) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[6]](https://www.theguardian.com/film/2026/oct/20/ai-actors-val-kilmer-as-deep-as-the-grave-tilly-norwood) | #27, #29–33 | #23 | #19, #2 (pulado) | `#27` judging by the extended glimpse of the film released earlier this year: it looks like a thirtysomething Kilmer, if a robot version had been sent back to the 19… |
| [[13]](https://flauntaudio.com/ai-voice-actor-statistics-2026/) | #35–39, #41 | — | #34, #40, #57 (pulado) | `#35` 21% of voice actors say they have knowingly lost a job to a synthetic voice (NAVA, 2026). Only **13%** have agreed to let a third party create a synthetic vers… |
| [[48]](https://copyrightinformation.org/ai/copyright-office-ai-guidance/) | #68, #70, #72, #74 | #3, #67, #73 | — | `#68` Thaler v. Perlmutter. On March 18, 2025, the D.C. Circuit held that the Copyright Act "requires all eligible work to be authored in the first instance by a hum… |
| [[55]](https://ailawsuittracker.com/international-ai-lawsuits/) | #86, #89 | #76, #87–88, #106 | #101 | `#86` Outside the United States, AI cases are decided under different copyright and privacy laws, and the answers have differed. A Munich court has held that a model… |
| [[91]](https://blog.promise.legal/ai-generated-content-film-legal-compliance-2026/) | — | #3, #75, #107, #110–111 | #0, #18 (pulado) | `#3` AB 2602 requires that contracts involving the use of AI-generated digital replicas of a performer's voice or likeness must specifically describe the intended u… |
| [[1]](https://www.precedenceresearch.com/generative-ai-in-the-media-and-entertainment-market) | #6–8, #13 | #5 | #4 (pulado) | `#6` The global generative AI in the media and entertainment market size accounted for USD 2.24 billion in 2025 and is predicted to increase from USD 2.8 billion in… |
| [[23]](https://everything-pr.com/the-lawsuit-war-room-every-major-ai-copyright-case-mapped-47-publishers-8-ai-companies-and-the-trial-that-will-reshape-the-internet) | #51, #82, #89 | #77, #84, #88 | — | `#51` Sony Music v. Udio (S.D.N.Y., Jul. 2026). Second filing covering 30,117 additional sound recordings. Alleges stream-ripping from YouTube. [...] Sony Music v. S… |
| [[53]](https://natlawreview.com/article/output-v-input-copyright-ownership-challenges-era-artificial-intelligence) | #79–81 | #67, #73, #77 | — | `#79` Those are fact-intensive questions. Recent decisions have begun to draw the lines, but the appellate courts have not yet supplied a comprehensive framework for… |
| [[71]](https://www.afterlife.ai/no-fakes-act-explained) | #98–99 | #93, #95 | #34, #100 (s/ aval.) | `#98` It cleared the Senate Judiciary Committee in June, then stalled on the Senate floor on September 30. ... The House version, H.R. 8915, has not had a committee… |
| [[11]](https://www.cbc.ca/news/entertainment/val-kilmer-ai-trailer-9.7166746) | #24–26 | #21 | #19 | `#24` The use of generative AI to recreate Kilmer for the historical drama, based on archaeologists Ann and Earl Morris, became a hot-button issue when the filmmaker… |
| [[74]](https://stablediffusionfrivolous.com/deepfakes/right-of-publicity/) | #93–94 | #90, #95 | #97 (pulado) | `#93` There is no federal right of publicity. Each state decides whether the right exists, what it covers, and whether it survives death. ... The table covers the fo… |
| [[3]](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/tmt-predictions-hollywood-cautious-of-genai-adoption.html) | #11 | #5, #9 | #1 (pulado) | `#11` Although studios may have been quick to experiment with gen AI content creation, they will likely be more cautious in moving it into full production. Some reas… |
| [[21]](https://dynamoi.com/learn/ai-music-distribution/ai-music-copyright-cases-timeline) | #48 | #45, #49 | #2 (pulado) | `#48` On June 24, 2024, the Recording Industry Association of America (RIAA) announced two copyright infringement cases on behalf of major record labels. ### Univers… |
| [[75]](https://talkmie.com/news/no-fakes-act-voice-likeness-us-status) | #98 | #3, #99 | #100 (s/ aval.) | `#98` The United States still has no federal law on AI copies of a person's voice or face. ... As of late October 2026: neither chamber has held a recorded vote. |
| [[79]](https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act) | — | #101–103 | #0 (pulado) | `#101` According to Article 50(2) of the AI Act, providers of AI systems, including general-purpose AI systems, generating synthetic audio, image, video or text conte… |
| [[89]](https://www.resemble.ai/resources/generative-ai-watermarking-opportunities-challenges) | — | #3, #107–108, #111 | — | `#3` AI watermarking embeds or attaches a machine-readable marker to AI-generated content. [...] C2PA Content Credentials [...] Source and edit history through sign… |
| [[4]](https://www.bfi.org.uk/news/generative-ai-screen-industries) | #12 | #9 | #1 (pulado) | `#12` The screen sector is already seeing examples of public sector AI-driven service innovation, based on principles of responsible AI such as the Intelligent Syste… |
| [[12]](https://www.theguardian.com/film/val-kilmer) | #28 | #25 | #24 | `#28` September 2026 Reanimated AI Greta Garbo stars again … in a ball-bearing advert Relatives of Hollywood legend say her doppelganger could now be used for more g… |
| [[18]](https://en.wikipedia.org/wiki/2024%E2%80%932025_SAG-AFTRA_video_game_strike) | #46 | #45 | #58 (pulado) | `#46` On May 19, 2025, SAG-AFTRA filed an unfair labor practice charge on Llama Productions, a subsidiary of Epic Games, alleging the company replaced actors' work b… |
| [[39]](https://aifilmsafe.com/compliance-calendar) | — | #61 | #60, #64 (pulado) | `#61` WGA 2026 MBA — Takes Effect. The ratified WGA 2026 Minimum Basic Agreement becomes effective. Companies must notify WGA before licensing scripts for GAI traini… |
| [[49]](https://accordshield.com/blog-who-owns-ai-generated-code-content) | — | #70–71, #75 | — | `#70` The guidance compares prompts to "instructions to a commissioned artist" — they say what you want, but the system decides how it is expressed. [...] Its Januar… |
| [[51]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | #69, #72 | #68 | — | `#69` On March 18, 2025, a D.C. Circuit panel affirmed the district court's ruling. Although the Copyright Act does not explicitly define "author," the court found t… |
| [[52]](https://usfblogs.usfca.edu/centerforlawtechsocialgood/from-studio-to-silicon-human-authorship-ai-generated-art-and-the-supreme-court/) | #72, #75 | #73 | — | `#72` The case that's going to define the line—the one Thaler was always too extreme to draw—is Allen v. Perlmutter, sitting right now in the District of Colorado. [… |
| [[61]](https://ailawsuittracker.com/cases/disney-enterprises-inc-v-midjourney-inc-2-25-cv-05275/) | — | #3, #84–85 | — | `#3` Active — Midjourney moved for judgment on the pleadings on Disney's contributory infringement claim July 22, 2026. [...] Stakes: Studio IP + injunction |
| [[68]](https://www.fredlaw.com/alert-federal-court-dismisses-trademark-and-copyright-claims-over-ai-voice-clones-but-leaves-door-open-under-state-publicity-law) | — | #90–91 | #92 (pulado) | `#90` the court rejected these claims, holding that copyright protection does not extend to voice per se or to mere imitation of vocal characteristics. |
| [[73]](https://air.io/en/youtube-hacks/youtube-ai-policy-2026-likeness-detection-and-the-no-fakes-act-what-creators-need-to-know) | #94 | #95 | #100 (s/ aval.) | `#94` It has been law since July 1, 2024, and despite the name, it protects every individual rather than only recording artists. ... Liability extends to whoever dis… |
| [[77]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | — | — | #96, #99, #97 (pulado) | — |
| [[80]](https://ppc.land/non-eu-advertisers-face-3-eu-fines-for-unlabelled-ai-deep-fake-ads/) | #102 | #103 | #111 | `#102` November 12, 2026 : The guidelines are published in the Official Journal of the European Union as C/2026/6005. ... December 2, 2026 : Deadline for generative A… |
| [[90]](https://www.datamintelligence.com/research-report/digital-watermarking-market) | #108–109 | — | #107 | `#108` C2PA-based Content Credentials can establish a signed record of who created content, what tools were involved and how an asset changed over time. Adobe describ… |
| [[2]](https://reports.weforum.org/docs/WEF_Artificial_Intelligence_in_Media_Entertainment_and_Sport_2025.pdf) | #10 | #9 | — | `#10` 92% of creators say they have already used genAI in some capacity (vs. only 34% in November 2023). |
| [[7]](https://www.cbsnews.com/news/ai-actor-hollywood-tilly-norwood-stirs-outrage/) | — | #20–21 | — | `#20` Van der Velden, who is also the founder of the AI production studio Particle6, promoted Tilly Norwood last month at the Zurich Summit, the industry sidebar of… |
| [[8]](https://vgtimes.com/movies-and-tv-series/134353-ai-actress-tilly-norwood-dubbed-the-new-scarlett-johansson-sparks-controversy-in-hollywood.html) | — | #20–21 | — | `#20` She was developed by Eline Van der Velden, founder of the Dutch company Particle 6 Productions. Recently, Van der Velden announced the launch of a talent studi… |
| [[9]](https://www.resultsense.com/news/2025-09-30-tilly-norwood-ai-actor-hollywood-controversy/) | #22 | #20 | — | `#22` Norwood's only performance to date—a two-minute AI-generated sketch—has garnered modest viewership of approximately 200,000 views over two months, significantl… |
| [[10]](https://commons.lib.jmu.edu/cgi/viewcontent.cgi?article=1204&context=honors202029) | — | #20, #23 | — | `#20` In late 2025, weekly trade publication Variety Magazine reported on the announcement of a new acting talent in Hollywood: Tilly Norwood. Norwood is an industry… |
| [[14]](https://www.gravyforthebrain.com/voice-acting-in-2025-2026-trends-insights-and-the-future/) | — | #44 | #40 (pulado) | `#44` Investing in general acting skills, such as improvisation, comedic performance and broadening emotional range, will keep you ahead of synthetic AI voices. ...… |
| [[16]](https://www.morningstar.com/news/business-wire/20260826543251/new-data-shows-audiences-are-embracing-ai-dubbing-heres-what-the-media-industry-should-know) | — | #44 | #42 (pulado) | `#44` Creators are leveraging that engagement data to make real investment decisions. "YouTube creators aren't dubbing on faith, they are following the data," said C… |
| [[24]](https://www.universalmusic.com/universal-music-group-and-elevenlabs-announce-multi-year-strategic-agreement-beginning-with-a-new-licensed-ai-music-creation-platform/) | #50 | #45 | — | `#50` Universal Music Group (UMG), the world leader in music-based entertainment, and ElevenLabs, the leading AI audio research and product company, today announced… |
| [[29]](https://www.sagaftra.org/sites/default/files/sa_documents/DigitalReplicas.pdf) | #53 | — | #54 (pulado) | `#53` In the 2023 TV/Theatrical Contracts negotiations, SAG-AFTRA secured protections for the creation and use of digital replicas of performers... An "Employment-Ba… |
| [[30]](https://productionguild.com/download/file/aGtkbXlabXN0TUVSekJYcXo4UDI3Zz09/sag-aftra-strike-2023_summary-of-agreed-terms/) | — | #53 | #54 (pulado) | `#53` no employment arrangement for the motion picture in which the Independently Created Digital Replica will be used exists with the natural performer in the role… |
| [[38]](https://www.wga.org/contracts/know-your-rights/artificial-intelligence) | — | #61 | #60 (pulado) | `#61` Neither traditional AI (technologies including those used in CGI and VFX) nor generative AI (GAI, meaning artificial intelligence that produces content includi… |
| [[45]](https://www.theguardian.com/technology/artificialintelligenceai) | — | — | #66, #52 (pulado) | — |
| [[60]](https://law.duke.edu/centers/cspd/2026supplement.pdf) | #79 | #81 | — | `#79` this ruling does not stand for the proposition that Meta's use of copyrighted materials to train its language models is lawful. It stands only for the proposit… |
| [[65]](https://cms.law/en/gbr/legal-updates/getty-images-v-stability-ai-permission-to-appeal-sought-by-getty-images-at-consequentials-hearing) | #87 | #86 | — | `#87` Getty applied for permission to appeal the dismissal of its secondary copyright infringement claim. Justice Smith granted permission in full. [...] At a conseq… |
| [[67]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | — | #91 | #92 (pulado) | `#91` The court distinguished between using a voice as the product itself versus using a voice as a brand to identify the source or origin of the product. Here, plai… |
| [[82]](https://asee.io/blog/eu-ai-act-transparency-rules-customer-service/) | — | #102–103 | — | `#102` Most of this became enforceable on 2 August 2026. Providers of systems already on the market before that date have until 2 December 2026 to meet the machine-re… |
| [[83]](https://www.biometricupdate.com/202611/deepfake-era-puts-likeness-in-legal-spotlight-as-eu-works-to-define-whats-allowed) | — | #101, #104 | — | `#101` While the AI Act sets transparency requirements for deepfakes and the Digital Services Act governs platforms' handling of illegal content, there is no general… |
| [[88]](https://adjuris.ro/books/plbs/13.pdf) | — | #106 | #105 (pulado) | `#106` China has also adopted a strict regulation through its Deep Synthesis Regulations. These rules impose labelling requirements for AI generated content and make… |
| [[92]](https://aifilmsafe.com/glossary) | #110 | #111 | — | `#110` As of 2026, major festivals including Sundance, TIFF, Cannes, Venice, and Berlin have implemented various levels of AI transparency requirements. Requirements… |
| [[17]](https://mashable.com/article/fortnite-darth-vader-ai-james-earl-jones) | #46 | — | — | `#46` developer Epic Games announced in a blog post that Darth Vader is back in Fortnite as a recruitable boss character […] You can voice chat with Darth Vader and… |
| [[19]](https://www.youtube.com/watch?v=gGG7dpHVkrA) | #47 | — | — | `#47` Actor Scarlett Johansson has hired a lawyer after ChatGPT debuted the voice of a new interactive assistant that she says sounds similar to hers. While the Open… |
| [[20]](https://www.mckoolsmith.com/newsroom-ailitigation-45) | — | #48 | — | `#48` The RIAA on behalf of the major record labels filed their lawsuit in the federal district Court in Massachusetts on June 24th, 2024, for mass copyright infring… |
| [[22]](https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform/) | — | #49 | — | `#49` In a landmark move late Wednesday (October 29) evening, Universal Music Group announced that it has settled its copyright infringement litigation against AI mu… |
| [[25]](https://elevenlabs.io/blog/umg) | #50 | — | — | `#50` We've entered a multi-year licensing agreement and strategic collaboration with Universal Music Group (UMG) [...] The platform will give fans new ways to co-cr… |
| [[26]](https://routenote.com/blog/universal-music-group-and-elevenlabs-join-forces-on-new-ai-music-platform/) | — | #50 | — | `#50` The partnership, announced on September 10, 2026, combines UMG's extensive music catalogue with ElevenLabs' AI audio technology. [...] The platform will allow… |
| [[27]](https://en.wikipedia.org/wiki/2023_SAG-AFTRA_strike) | — | #53 | — | `#53` From July 14 to November 9, 2023, the American actors' union Screen Actors Guild–American Federation of Television and Radio Artists (SAG-AFTRA) went on strike… |
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
| [[86]](https://english.bjinternetcourt.gov.cn/2024-04/24/c_706.htm) | — | #106 | — | `#106` A Beijing court has issued a landmark ruling that imitating someone's voice through AI without their permission constitutes an infringement of their personal r… |
| [[87]](https://www.marks-clerk.com/insights/latest-insights/102kv8h-china-new-ruling-on-non-infringement-of-personality-rights-by-ai-voice-does-it-signal-a-shift-in-protection-standards/) | — | #106 | — | `#106` In April 2024, the Beijing Internet Court issued China's first ruling on AI voice infringement... This legally effective ruling affirmed that voices recognizab… |
| [[93]](https://www.reedsmith.com/articles/entertainment-media-guide-to-ai-three-years-on/games/) | — | #103 | — | `#103` Synthetic voices, a de-aged or resurrected performer, or a fully AI-generated actor can therefore constitute a 'deepfake' even where all underlying consent has… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.researchgate.net/publication/417398892_A_Narrative_Review_of_the_Impact_of_AI_on_Film_and_TV_Production — Rate limit persistente em https://www.researchgate.net/publication/417398892_A_Narrative_Review_of_the_Impact_of_AI_on_Film_and_TV_Production
- https://www.researchgate.net/publication/391690363_The_Impact_Of_Ai-powered_Dubbing_And_Localization_On_Global_Media — Rate limit persistente em https://www.researchgate.net/publication/391690363_The_Impact_Of_Ai-powered_Dubbing_And_Localization_On_Global_Media
- https://www.sagaftra.org/sites/default/files/sa_documents/TV-Theatrical_23_Summary_Agreement_Final.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/sa_documents/TV-Theatrical_23_Summary_Agreement_Final.pdf (PDF, sem fallback via playwright)
- https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf — HTTP 403 em https://www.sagaftra.org/files/sa_documents/2024%20SAG-AFTRA%20Sound%20Recordings%20Code%20Contract%20Summary.pdf (PDF, sem fallback via playwright)
- https://www.sagaftra.org/sites/default/files/Sound%20Recordings%20Code%20Appendix%20on%20Artificial%20Intelligence.pdf — HTTP 403 em https://www.sagaftra.org/sites/default/files/Sound%20Recordings%20Code%20Appendix%20on%20Artificial%20Intelligence.pdf (PDF, sem fallback via playwright)
- https://www.researchgate.net/publication/401736407_Copyright_or_personality_rights_A_critical_analysis_of_Denmark's_approach_to_deepfakes — Rate limit persistente em https://www.researchgate.net/publication/401736407_Copyright_or_personality_rights_A_critical_analysis_of_Denmark's_approach_to_deepfakes

### Bloqueadas por barreira de acesso

- https://www.sagaftra.org/contracts-industry-resources/contracts/2024-sound-recordings-code — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930049-GRU 1794966465 2453970890 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930069-GRU 1794966496 1559067062 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930080-GRU 1794966505 3538513624 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/television/2026-television-animation-agreements — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930095-GRU 1794966516 1687729947 Varnish cache server
- https://ai.miraheze.org/wiki/Lovo — no_content — barreira de acesso (no_content): Verification successful. Waiting for ai.miraheze.org to respond Enable JavaScript and cookies to continue
- https://www.sagaftra.org/sag-aftra-ai-bargaining-and-policy-work-timeline — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930058-GRU 1794966526 4234347310 Varnish cache server

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

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

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-6`** [1]
  - Trecho: A September 2026 report from commercial research firm Precedence Research values the global generative AI in media and entertainment market at $2.24 billion in 2025 and $2.8 billion in 2026, projecting expansion to $21.…
  - Justificativa: A evidência confirma explicitamente todos os valores financeiros e a CAGR citados na afirmativa: USD 2.24 bilhões em 2025, USD 2.8 bilhões em 2026, USD 21.2 bilhões em 2035 e CAGR de 25.2%. A fonte é da Precedence Resea…
  - Suporte veio de: [1]
  - Evidência: “Market Size in 2025 | USD 2.24 Billion”
  - Não coberto pela evidência: September 2026 como data do relatório — a evidência não menciona em que mês/ano o relatório foi publicado
### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-19`** [6] [11]
  - Trecho: Both forms have tested audience acceptance and technical limits throughout 2025 and 2026.
  - Justificativa: A evidência menciona eventos em 2025 e 2026 (CinemaCon 2026, corrida do Oscar 2025, lançamentos de filmes como Hell Grind e The Cully Hill Boys), e discute reações do público e limites técnicos da IA em atuação. Porém,…
  - Suporte veio de: [6] [11]
  - Não coberto pela evidência: Both forms (quais são as duas formas não está claro na evidência); tested audience acceptance (não há afirmação explícita de que ambas as formas testaram aceitação do público); technical limits (não há afirmação explícita de que ambas as formas testaram limites técnicos)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | ausente | — |
    | [11] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-21`** [7] [8] [11]
  - Trecho: Touted alongside plans for an AI talent agency, Norwood provoked immediate condemnation from SAG-AFTRA and actors including Emily Blunt, Melissa Barrera, Mara Wilson, and Whoopi Goldberg, who criticized the concept as "…
  - Justificativa: A evidência sustenta parte da afirmação (condenação do SAG-AFTRA, crítica de Melissa Barrera e Mara Wilson como 'face theft', e planos de agência de talentos AI), mas menciona explicitamente apenas Barrera e Wilson como…
  - Suporte veio de: [8] [7]
  - Evidência: “The actors' union SAG-AFTRA issued a strong statement in response.”
  - Não coberto pela evidência: Emily Blunt como uma das atoras que condenou o projeto; Whoopi Goldberg como uma das atoras que condenou o projeto
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | parcial | Guilds, actors and filmmakers have met the Xicoia product with an immediate wave of backlash |
    | [8] | parcial | The actors’ union SAG-AFTRA issued a strong statement in response. |
    | [11] | parcial | Creations like Tilly Norwood by production company Particle6 are intended to be entirely original, and have raised conc… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-34`** [13] [71]
  - Trecho: Voice cloning has disrupted audio production more immediately than screen acting because neural speech models can synthesize vocal likenesses from just seconds of enrolled audio.
  - Justificativa: A evidência discorre sobre impacto da IA em voice actors (21% perderam trabalho), consentimento, leis e mercado, mas não faz comparação com screen acting, nem afirma que voice cloning disruptou audio production 'more im…
  - Não coberto pela evidência: Comparação entre voice cloning e screen acting em termos de velocidade de disrupção; Afirmação de que voice cloning disruptou audio production 'more immediately than screen acting'; Modelos neurais de síntese vocal a partir de 'just seconds of enrolled audio'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [13] | ausente | — |
    | [71] | ausente | — |

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

Motivos: 20 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 5 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-14` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-15` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-16` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-17` — Referencia(s) citada(s) ['cc1b42afee758e8a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-43` — Referencia(s) citada(s) ['489282bf7e203d33'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-56` — Referencia(s) citada(s) ['15aae246033f2272', '350de76304ffe6f3', 'c96f1679e56af436'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-63` — Referencia(s) citada(s) ['0ad3078ef2adc633'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-0` — Parte das fontes citadas sem conteudo: referencia(s) ['cc1b42afee758e8a', '0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-1` — Parte das fontes citadas sem conteudo: referencia(s) ['cc1b42afee758e8a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-2` — Parte das fontes citadas sem conteudo: referencia(s) ['0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-4` — Parte das fontes citadas sem conteudo: referencia(s) ['cc1b42afee758e8a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-18` — Parte das fontes citadas sem conteudo: referencia(s) ['0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-40` — Parte das fontes citadas sem conteudo: referencia(s) ['489282bf7e203d33'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-42` — Parte das fontes citadas sem conteudo: referencia(s) ['489282bf7e203d33'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-52` — Parte das fontes citadas sem conteudo: referencia(s) ['aca12210a3d2f331', '0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-54` — Parte das fontes citadas sem conteudo: referencia(s) ['53e75ae0f08f1e88'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-55` — Parte das fontes citadas sem conteudo: referencia(s) ['350de76304ffe6f3', 'aca12210a3d2f331'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-57` — Parte das fontes citadas sem conteudo: referencia(s) ['377fa397a3a499a2'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-58` — Parte das fontes citadas sem conteudo: referencia(s) ['aca12210a3d2f331'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-59` — Parte das fontes citadas sem conteudo: referencia(s) ['aca12210a3d2f331'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-60` — Parte das fontes citadas sem conteudo: referencia(s) ['0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-62` — Parte das fontes citadas sem conteudo: referencia(s) ['0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-64` — Parte das fontes citadas sem conteudo: referencia(s) ['0ad3078ef2adc633'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-65` — Parte das fontes citadas sem conteudo: referencia(s) ['c40f2af239094710'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-92` — Parte das fontes citadas sem conteudo: referencia(s) ['23a34f7aff2a3825'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-97` — Parte das fontes citadas sem conteudo: referencia(s) ['377fa397a3a499a2'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `ia_generativa_entretenimento_6d6b9157bae0_20261117T231159Z-105` — Parte das fontes citadas sem conteudo: referencia(s) ['565baf8382fc5938'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.