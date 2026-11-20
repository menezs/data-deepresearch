# Relatório de Auditoria — Claude (ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z)

**Arquivo auditado:** `answers/Ingles/Claude/Emergente/ia_generativa_entretenimento.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T13:15:12.945693+00:00 |
| **Total de trechos citados** | 71 |
| **Tempo de processamento** | 0:00:08:14 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 32.2 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 71 marcadores, 65 distintos |
| Referências listadas | 65 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 60 | 84.5% |
| **UNSUPPORTED** | 8 | 11.3% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 3 | 4.2% |
| **TOTAL** | 71 | 100.0% |

Sobre os 68 trechos citados auditados: SUPPORTED 88,23%, UNSUPPORTED 11,76%, CONTRADICTED 0,00%.

> **9 dos 60 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 9 estão **contados dentro** dos 60 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`10` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `2` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#10` Chief negotiator Duncan Crabtree-Ireland has said that in the end an arbitrator will decide whether a synthetic actuall… | [9] | [7] [5] [6] [3] [8] [4] [10] [19] | — |
| `#42` The entertainment industry's own litigation focuses more on outputs. In June 2025, Disney and Universal filed a 110-pag… | [37] | [38] [39] [34] [40] [41] [48] [21] [22] [23] [28] [16] [62] [42] [55] [54] [9] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 288158 |
| **Média de tokens por requisição** | 4237.6 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/65 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://www.itv.com/news/2025-10-02/meet-tilly-norwood-the-ai-generated-actress-facing-backlash-in-hollywood) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[5]](https://www.thewrap.com/industry-news/labor-unions/sag-aftra-members-ratify-new-contract/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[8]](https://awf.labortools.com/listen/sag-aftras-crabtree-ireland-on-ai-protections-and-pension-merger) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[14]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://letsdatascience.com/news/elevenlabs-launches-licensed-celebrity-voice-marketplace-c4ac7a18) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[34]](https://www.npr.org/2025/09/05/nx-s1-5529404/anthropic-settlement-authors-copyright-ai) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[1]](https://www.hola.com/us/entertainment/20250929858561/first-ai-actress-tilly-norwood-next-scarlett-johansson/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://blog.pebblous.ai/blog/sag-aftra-ai-consent-collective-bargaining/en/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[4]](https://senalnews.com/en/content/sag-aftra-members-approve-2026-tv-theatrical-contracts-tentative-agreement) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[6]](https://www.hollywoodreporter.com/business/business-news/sag-aftra-four-year-deal-studios-new-ai-protections-1236590891/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://www.thewrap.com/industry-news/tech/sag-aftra-ai-protections-in-new-contract-synthetic/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://puck.news/hollywood/2026/5/sag-aftras-ai-deal-opens-door-to-synthetic-actors) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[10]](https://www.redsharknews.com/sag-aftra-ai-deal-synthetic-actors-2026) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[11]](https://www.loeb.com/en/insights/passle/2026/11/sagaftra-s-tentative-2026-television-animation-agreement) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://techcrunch.com/2024/05/20/scarlett-johansson-says-that-openai-approached-her-to-use-her-voice) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[13]](https://www.axios.com/2024/05/20/scarlet-johansson-openai-chatgpt-sam-altman) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://getcoai.com/news/voice-actors-win-court-battle-against-ai-voice-cloning-startup) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[16]](https://www.crowell.com/en/insights/client-alerts/fundamental-copyright-principles-underscored-in-ai-context-voice-attributes-are-not-protectable) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[17]](https://www.offitkurman.com/offit-kurman-blogs/ai-voice-cloning-lawsuit-voice-actor-rights) | error | 1 | 0 | 0 | 0 | 1 |
| [[18]](https://www.pocketgamer.biz/sag-aftra-ends-strike-against-video-game-companies-after-reaching-tentative-ai-protections-deal) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://gamesbeat.com/sag-aftra-union-members-approve-to-end-strike-with-game-firms-over-ai/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://allwork.space/?p=1037292) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://decrypt.co/329479/video-game-performers-ai-consent-rules) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://www.thewrap.com/sag-aftra-darth-vader-fortnite-ai-voice/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://news.bloombergtax.com/esg/actors-union-files-labor-charge-over-ai-darth-vader-in-fortnite) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://www.techradar.com/ai-platforms-assistants/michael-caine-and-matthew-mcconaughey-have-licensed-their-voices-to-ai-but-not-every-iconic-voice-on-the-platform-can-consent) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://www.nbcnews.com/tech/tech-news/openai-sora-2-guardrails-sag-aftra-bryan-cranston-rcna238715) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[27]](https://the-decoder.com/openai-tightens-sora-2-safeguards-after-bryan-cranstons-likeness-appears-without-consent/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.jenner.com/en/news-insights/publications/client-alert-us-copyright-office-issues-report-on-copyrightability-of-works-incorporating-ai-generated-material) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://www.hoganlovells.com/en/publications/us-copyright-office-issues-report-on-copyrightability-of-ai-assisted-and-generated-works) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://www.mondaq.com/unitedstates/copyright/1756930/supreme-court-declines-to-hear-thaler-v-perlmutter-leaving-human-authorship-requirement-intact) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://www.wiley.law/alert-Copyright-Office-Issues-Key-Guidance-on-Fair-Use-in-Generative-AI-Training) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.manatt.com/insights/insight/copyright-office-releases-pre-publication-report-on-copyrighted-works-in-generative-ai-training) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://news.bgov.com/litigation/anthropic-authors-1-5-billion-deal-receives-final-approval) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[36]](https://thenextweb.com/news/anthropic-1-5-billion-copyright-settlement-approved) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[37]](https://www.tpr.org/2025-06-12/in-first-of-its-kind-lawsuit-hollywood-giants-sue-ai-firm-for-copyright-infringement) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[38]](https://thedesk.net/2025/06/disney-comcast-midjourney-lawsuit/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://getcoai.com/news/midjourney-claims-studios-use-ai-while-suing-it-for-copyright-infringement/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://www.law360.com/cases/6849920dbaefe0fe54b77b08) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[41]](https://www.c21media.net/news/disney-strikes-deal-with-openai-to-bring-200-characters-to-video-platform-sora/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[42]](https://au.variety.com/2025/digital/global/disney-openai-deal-200-characters-to-sora-video-invests-1-billion-30990/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://www.axios.com/2026/03/24/openai-discontinue-sora-video-app) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[44]](https://www.pcgamer.com/software/ai/openai-discontinues-sora-video-generation-app-disney-pulls-out-of-usd1-billion-investment-deal) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://www.cbsnews.com/news/sora-ai-openai-discontinues) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[46]](https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[47]](https://uk.marketscreener.com/news/warner-music-group-settles-copyright-case-with-suno-for-licensed-ai-music-ce7d5ed2db8bff22) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://completemusicupdate.com/universal-has-settled-its-lawsuit-with-udio-and-signed-ai-deals-with-udio-and-stability/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[49]](https://www.manatt.com/insights/newsletters/client-alert/california-enacts-a-host-of-new-ai-and-digital-rep) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[50]](https://sagaftra.org/gov-newsom-signs-union-championed-ai-bills-sag-aftra-plaza) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[51]](https://www.covingtonblogs.com/2024/09/11/california-passes-digital-replica-legislation-as-congress-considers-federal-approach/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[52]](https://www.grammy.com/advocacy/issues-policy/no-fakes-act/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[53]](https://www.manatt.com/insights/newsletters/client-alert/congress-reintroduces-the-no-fakes-act-what-s-new-in-the-2026-bill) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[54]](https://www.paubox.com/blog/what-is-the-no-fakes-act) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[55]](https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[56]](https://letsdatascience.com/news/no-fakes-act-advances-unanimously-out-of-senate-judiciary-co-553e714b) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[57]](https://letsdatascience.com/news/senate-judiciary-committee-clears-no-fakes-act-aa4c3c17) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[58]](https://www.rawstory.com/ted-cruz-marsha-blackburn/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[59]](https://www.aimusicpreneur.com/ai-music-industry/riaa-mitch-glazier-no-fakes-act-lame-duck-cruz-objection-2026/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[60]](https://reclaimthenet.org/bill/no-fakes-act) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[61]](https://schjodt.com/news/owning-the-self-denmarks-copyright-turn-against-deepfakes) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[62]](https://www.euronews.com/2026/10/08/denmark-introduces-a-bill-protecting-peoples-faces-and-voices-from-deepfakes) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[63]](https://pasqualepillitteri.it/en/news/23036/denmark-deepfake-law-copyright-face-voice) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[64]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/01/EPRS_ATA(2026)782611.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[65]](https://www.faegredrinker.com/en/insights/publications/2026/7/eu-ai-act-commission-confirms-transparency-code-of-practice-as-adequate-and-publishes-final-version-of-its-guidelines-on-transparency-obligations) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://www.itv.com/news/2025-10-02/meet-tilly-norwood-the-ai-generated-actress-facing-backlash-in-hollywood) | #1–2 | — | — | `#1` AI characters should be judged as part of their own genre, on their own merits, rather than compared directly to human actors. |
| [[5]](https://www.thewrap.com/industry-news/labor-unions/sag-aftra-members-ratify-new-contract/) | #5, #7 | — | — | `#5` Synthetic performers became a hot-button topic in Hollywood last year after the rise of the AI-generated Tilly Norwood. |
| [[8]](https://awf.labortools.com/listen/sag-aftras-crabtree-ireland-on-ai-protections-and-pension-merger) | #9, #12 | — | — | `#9` That starts a bargaining window with the union that totals approximately 26 days. The studio faces the possibility of arbitration, with potentially unlimited d… |
| [[14]](https://www.loeb.com/en/insights/publications/2025/07/lehrman-v-lovo-inc) | #16, #19 | — | — | `#16` Lovo used the recordings to train its AI voice generator, “Genny,” and created voice clones marketed under the names “Kyle Snow” and “Sally Coleman.” These clo… |
| [[24]](https://letsdatascience.com/news/elevenlabs-launches-licensed-celebrity-voice-marketplace-c4ac7a18) | #27–28 | — | — | `#27` ElevenLabs named living performers such as Michael Caine, Liza Minnelli, and Art Garfunkel alongside historical figures including Maya Angelou, Alan Turing, Ma… |
| [[34]](https://www.npr.org/2025/09/05/nx-s1-5529404/anthropic-settlement-authors-copyright-ai) | #38–39 | — | — | `#38` In his June ruling, Judge Alsup agreed with Anthropic's argument, stating the company's use of books by the plaintiffs to train their AI model was acceptable.… |
| [[1]](https://www.hola.com/us/entertainment/20250929858561/first-ai-actress-tilly-norwood-next-scarlett-johansson/) | #0 | — | — | `#0` Unveiled at the Zurich Summit, the industry centerpiece of the Zurich Film Festival, Tilly Norwood is the first AI-generated actress created by Xicoia, a newly… |
| [[3]](https://blog.pebblous.ai/blog/sag-aftra-ai-consent-collective-bargaining/en/) | #3 | — | — | `#3` SAG-AFTRA issued a formal statement of its own: Tilly Norwood is not an actor but the output of a computer program trained on the work of countless professiona… |
| [[4]](https://senalnews.com/en/content/sag-aftra-members-approve-2026-tv-theatrical-contracts-tentative-agreement) | #4 | — | — | `#4` The agreement is effective on July 1, 2026, and expires June 30, 2030. |
| [[6]](https://www.hollywoodreporter.com/business/business-news/sag-aftra-four-year-deal-studios-new-ai-protections-1236590891/) | #6 | — | — | `#6` It commits producers to “a principle strongly favoring human performances,” in the union’s description, and calls for producers not to use synthetic performers… |
| [[7]](https://www.thewrap.com/industry-news/tech/sag-aftra-ai-protections-in-new-contract-synthetic/) | #8 | — | — | `#8` Two studio sources told TheWrap that the idea of such a payment — referred to colloquially as the “Tilly Tax” in a nod to Tilly Norwood — was a nonstarter for… |
| [[9]](https://puck.news/hollywood/2026/5/sag-aftras-ai-deal-opens-door-to-synthetic-actors) | — | #10 | — | `#10` it’s all good as long as producers can demonstrate that A.I. actors offer “significant additional value” beyond what could be achieved using an ordinary digita… |
| [[10]](https://www.redsharknews.com/sag-aftra-ai-deal-synthetic-actors-2026) | #11 | — | — | `#11` The catch: no strike rights over AI until 2030. |
| [[11]](https://www.loeb.com/en/insights/passle/2026/11/sagaftra-s-tentative-2026-television-animation-agreement) | #13 | — | — | `#13` Producers licensing covered performances for commercial generative AI training must notify the union and discuss the arrangement upon request. |
| [[12]](https://techcrunch.com/2024/05/20/scarlett-johansson-says-that-openai-approached-her-to-use-her-voice) | — | #14 | — | `#14` Users found that it sounded similar to Scarlett Johansson |
| [[13]](https://www.axios.com/2024/05/20/scarlet-johansson-openai-chatgpt-sam-altman) | #15 | — | — | `#15` Johansson called for more "transparency" and new legislation to protect "individual rights." |
| [[15]](https://getcoai.com/news/voice-actors-win-court-battle-against-ai-voice-cloning-startup) | #17 | — | — | `#17` Lehrman was paid $1,200 and Sage received $800 for what they were told would be used for “academic research purposes only” and “test scripts for radio ads” res… |
| [[16]](https://www.crowell.com/en/insights/client-alerts/fundamental-copyright-principles-underscored-in-ai-context-voice-attributes-are-not-protectable) | #18 | — | — | `#18` The Southern District of New York issued a recent opinion in *Lehrman et al v. Lovo, Inc*., 1-24-cv-03770 (SDNY Jul. 10, 2025) (J. Paul Oetken) ... copyright m… |
| [[18]](https://www.pocketgamer.biz/sag-aftra-ends-strike-against-video-game-companies-after-reaching-tentative-ai-protections-deal) | #21 | — | — | `#21` SAG-AFTRA members have been on strike against video game companies since July 26th, 2024 |
| [[19]](https://gamesbeat.com/sag-aftra-union-members-approve-to-end-strike-with-game-firms-over-ai/) | #22 | — | — | `#22` In national voting completed today, SAG-AFTRA members approved the 2025 SAG-AFTRA Interactive Media Agreement by a vote of 95.04% to 4.96%, ratifying the deal… |
| [[20]](https://allwork.space/?p=1037292) | #23 | — | — | `#23` “AI was the centerpiece of our proposal package,” video game voice actor and member of the negotiation committee Sarah Elmaleh told Reuters after the new agree… |
| [[21]](https://decrypt.co/329479/video-game-performers-ai-consent-rules) | #24 | — | — | `#24` Nine major video game studios have agreed to artificial intelligence “guardrails” for performers, ratifying a deal that ends one of the longest entertainment i… |
| [[22]](https://www.thewrap.com/sag-aftra-darth-vader-fortnite-ai-voice/) | #25 | — | — | `#25` In a blog post, Epic said it worked with Jones' estate to develop the AI voice. |
| [[23]](https://news.bloombergtax.com/esg/actors-union-files-labor-charge-over-ai-darth-vader-in-fortnite) | #26 | — | — | `#26` The AI-powered version of late actor James Earl Jones's voice will take away work traditionally performed by union members, "including those who previously did… |
| [[25]](https://www.techradar.com/ai-platforms-assistants/michael-caine-and-matthew-mcconaughey-have-licensed-their-voices-to-ai-but-not-every-iconic-voice-on-the-platform-can-consent) | #29 | — | — | `#29` If you noticed that some of those people are no longer alive and are wondering how they consented to this, well, they didn't. We'll come back to that. ... Maya… |
| [[26]](https://www.nbcnews.com/tech/tech-news/openai-sora-2-guardrails-sag-aftra-bryan-cranston-rcna238715) | — | #30 | — | `#30` Cranston subsequently raised the issue with SAG-AFTRA, the union representing more than 150,000 film and TV performers, which has resulted in a collaborative e… |
| [[27]](https://the-decoder.com/openai-tightens-sora-2-safeguards-after-bryan-cranstons-likeness-appears-without-consent/) | #31 | — | — | `#31` OpenAI described the incident as "unintentional generations" and, after talks with SAG-AFTRA and Cranston, has "strengthened guardrails around replication of v… |
| [[28]](https://www.jenner.com/en/news-insights/publications/client-alert-us-copyright-office-issues-report-on-copyrightability-of-works-incorporating-ai-generated-material) | #32 | — | — | `#32` It then identifies the key distinction in assessing copyrightability as whether AI tools have been used "to assist" or instead as a "stand in" for human creati… |
| [[29]](https://www.hoganlovells.com/en/publications/us-copyright-office-issues-report-on-copyrightability-of-ai-assisted-and-generated-works) | #33 | — | — | `#33` The report states that a human author who creatively selects or arranges AI-generated output can receive copyright protection in the resulting compilation, but… |
| [[30]](https://www.mondaq.com/unitedstates/copyright/1756930/supreme-court-declines-to-hear-thaler-v-perlmutter-leaving-human-authorship-requirement-intact) | #34 | — | — | `#34` By declining review, the Supreme Court left in place a decision by the United States Court of Appeals for the District of Columbia Circuit, which held that cop… |
| [[31]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | #35 | — | — | `#35` Because Dr. Thaler disclaimed any human creative input, the court did not address how much human involvement is sufficient to support a copyright claim for AI-… |
| [[32]](https://www.wiley.law/alert-Copyright-Office-Issues-Key-Guidance-on-Fair-Use-in-Generative-AI-Training) | #36 | — | — | `#36` the Office also affirmatively states that use of copyright protected materials for AI model training is alone insufficient to justify fair use. Instead, "trans… |
| [[33]](https://www.manatt.com/insights/insight/copyright-office-releases-pre-publication-report-on-copyrighted-works-in-generative-ai-training) | #37 | — | — | `#37` released less than 24 hours before the dismissal of the U.S. Register of Copyrights, Shira Perlmutter |
| [[35]](https://news.bgov.com/litigation/anthropic-authors-1-5-billion-deal-receives-final-approval) | — | #40 | — | `#40` received final approval Monday |
| [[36]](https://thenextweb.com/news/anthropic-1-5-billion-copyright-settlement-approved) | — | #41 | — | `#41` Martínez-Olguín, who inherited the approval stage from Alsup, seemed less taken with the fair-use headline than with whether the deal was fair to the authors i… |
| [[37]](https://www.tpr.org/2025-06-12/in-first-of-its-kind-lawsuit-hollywood-giants-sue-ai-firm-for-copyright-infringement) | — | #42 | — | `#42` The 110-page lawsuit, filed Wednesday in a U.S. district court in Los Angeles |
| [[38]](https://thedesk.net/2025/06/disney-comcast-midjourney-lawsuit/) | #43 | — | — | `#43` “Midjourney is the quintessential copyright free-rider and a bottomless pit of plagiarism,” the lawsuit says. |
| [[39]](https://getcoai.com/news/midjourney-claims-studios-use-ai-while-suing-it-for-copyright-infringement/) | #44 | — | — | `#44` This lawsuit differs from other AI copyright cases by focusing primarily on AI outputs rather than the training process itself. |
| [[40]](https://www.law360.com/cases/6849920dbaefe0fe54b77b08) | — | — | #45 | — |
| [[41]](https://www.c21media.net/news/disney-strikes-deal-with-openai-to-bring-200-characters-to-video-platform-sora/) | #46 | — | — | `#46` Disney itself has sued AI companies such as Midjourney and MiniMax over claims of flagrant copyright infringement. |
| [[42]](https://au.variety.com/2025/digital/global/disney-openai-deal-200-characters-to-sora-video-invests-1-billion-30990/) | #47 | — | — | `#47` Disney said the agreement does not include any talent likenesses or voices. |
| [[43]](https://www.axios.com/2026/03/24/openai-discontinue-sora-video-app) | — | #48 | — | `#48` OpenAI plans to discontinue its popular-for-a-hot-second Sora video app, as the company says it's looking to narrow its focus and its human and computer resour… |
| [[44]](https://www.pcgamer.com/software/ai/openai-discontinues-sora-video-generation-app-disney-pulls-out-of-usd1-billion-investment-deal) | #49 | — | — | `#49` Disney, on the other hand, announced a deal to invest $1 billion into OpenAI, and to license its characters for use in Sora's slop. That's now fallen by the wa… |
| [[45]](https://www.cbsnews.com/news/sora-ai-openai-discontinues) | — | #50 | — | `#50` The move comes as the video platform wanes in popularity among users, according to the Wall Street Journal |
| [[47]](https://uk.marketscreener.com/news/warner-music-group-settles-copyright-case-with-suno-for-licensed-ai-music-ce7d5ed2db8bff22) | #52 | — | — | `#52` Under the deal, Suno will introduce new licensed AI models that will replace its current versions in 2026. |
| [[48]](https://completemusicupdate.com/universal-has-settled-its-lawsuit-with-udio-and-signed-ai-deals-with-udio-and-stability/) | #53 | — | — | `#53` However, the majors have so far resisted calls to secure explicit consent when licensing the general training of AI models. |
| [[49]](https://www.manatt.com/insights/newsletters/client-alert/california-enacts-a-host-of-new-ai-and-digital-rep) | #54 | — | — | `#54` AB 1836 prohibits the use of digital replicas of deceased performers without the consent of such performer’s estate. |
| [[50]](https://sagaftra.org/gov-newsom-signs-union-championed-ai-bills-sag-aftra-plaza) | #55 | — | — | `#55` AB 2602 prohibits contractual provisions that would allow for the use of a digital replica of an individual's voice or likeness in place of the individual's ac… |
| [[52]](https://www.grammy.com/advocacy/issues-policy/no-fakes-act/) | #57 | — | — | `#57` March 2024 Tennessee Signs ELVIS Act Into Law Tennessee Gov. Bill Lee signs the ELVIS Act into law, the first state legislation in the nation to protect agains… |
| [[53]](https://www.manatt.com/insights/newsletters/client-alert/congress-reintroduces-the-no-fakes-act-what-s-new-in-the-2026-bill) | #58 | — | — | `#58` On May 20, 2026, a bipartisan group of legislators reintroduced the latest version of the Nature Originals, Foster Art, and Keep Entertainment Safe Act of 2026… |
| [[54]](https://www.paubox.com/blog/what-is-the-no-fakes-act) | #59 | — | — | `#59` A DMCA-style notice-and-takedown system. Rights holders can send a takedown notice to get unauthorized content removed. [...] Later drafts of NO FAKES, includi… |
| [[55]](https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/) | #60 | — | — | `#60` The NO FAKES Act seeks to address that inconsistency by establishing a nationwide framework governing unauthorized digital replicas while preempting certain ov… |
| [[56]](https://letsdatascience.com/news/no-fakes-act-advances-unanimously-out-of-senate-judiciary-co-553e714b) | #61 | — | — | `#61` On June 18, 2026, the Senate Judiciary Committee advanced the bipartisan NO FAKES Act by unanimous voice vote. |
| [[57]](https://letsdatascience.com/news/senate-judiciary-committee-clears-no-fakes-act-aa4c3c17) | #62 | — | — | `#62` three Republican senators -- Mike Lee (UT), Ted Cruz (TX), and Eric Schmitt (MO) -- raised First Amendment concerns before the vote |
| [[58]](https://www.rawstory.com/ted-cruz-marsha-blackburn/) | #63 | — | — | `#63` Cruz did vote for the NO FAKES Act in committee over the summer, but reportedly failed to help broker a larger agreement folding it into a broader package addr… |
| [[59]](https://www.aimusicpreneur.com/ai-music-industry/riaa-mitch-glazier-no-fakes-act-lame-duck-cruz-objection-2026/) | #64 | — | — | `#64` His read: "We have a shot in the lame duck [period], a real shot." If that fails, the bill starts over in 2027. |
| [[60]](https://reclaimthenet.org/bill/no-fakes-act) | #65 | — | — | `#65` the Senate Judiciary Committee sent it to the floor without closing the free-speech holes that EFF and FIRE flagged. |
| [[61]](https://schjodt.com/news/owning-the-self-denmarks-copyright-turn-against-deepfakes) | #66 | — | — | `#66` enabling individuals to issue takedown notices, claim compensation even without reputational harm, and trigger platform liability if hosts fail to act. |
| [[62]](https://www.euronews.com/2026/10/08/denmark-introduces-a-bill-protecting-peoples-faces-and-voices-from-deepfakes) | — | #67 | — | `#67` The proposed amendment to Denmark’s copyright law would protect ordinary people as well as artists, including against digital imitations of their performances. |
| [[63]](https://pasqualepillitteri.it/en/news/23036/denmark-deepfake-law-copyright-face-voice) | #68 | — | — | `#68` Doubts remain about compatibility with the EU copyright directive. |
| [[64]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/01/EPRS_ATA(2026)782611.html) | #69 | — | — | `#69` Indeed, the planned Danish rules do not constitute copyright in the strict sense. [...] the Danish authorities, indeed, admit that they do not intend to design… |
| [[65]](https://www.faegredrinker.com/en/insights/publications/2026/7/eu-ai-act-commission-confirms-transparency-code-of-practice-as-adequate-and-publishes-final-version-of-its-guidelines-on-transparency-obligations) | #70 | — | — | `#70` Article 50 transparency obligations, which become enforceable on **2 August 2026.** ... The European Commission and the AI Board have confirmed that the Code o… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.covingtonblogs.com/2024/09/11/california-passes-digital-replica-legislation-as-congress-considers-federal-approach/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing this site. This process is automatic. You will arrive shortly. Verification succe

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-0`** [1]
  - Trecho: Xicoia, a new AI talent studio started by actress and producer Eline Van der Velden, CEO of the production company Particle6, presented an AI-generated "actress" named Tilly Norwood at the Zurich Summit, the industry ev…
  - Justificativa: A evidência confirma os elementos centrais da afirmação: Xicoia é um novo estúdio de talentos em IA lançado por Eline Van der Velden, que é atriz e CEO da Particle6, e Tilly Norwood foi apresentada no Zurich Summit, eve…
  - Suporte veio de: [1]
  - Evidência: “Unveiled at the Zurich Summit, the industry centerpiece of the Zurich Film Festival, Tilly Norwood is the first AI-generated actress created by Xicoia, a newly launched AI talent studio from Eline Van der Velden, the ac…”
  - Não coberto pela evidência: A qualificação de Eline Van der Velden como 'producer' não aparece explicitamente na evidência, que a descreve como 'actress, comedian, and CEO'.
- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-1`** [2]
  - Trecho: She also said AI characters should be treated as a genre of their own instead of being compared with human actors.
  - Justificativa: A evidência contém uma declaração direta de Van Der Velden afirmando que personagens de IA devem ser julgados como parte de seu próprio gênero, em vez de serem comparados diretamente a atores humanos, o que sustenta a a…
  - Suporte veio de: [2]
  - Evidência: “AI characters should be judged as part of their own genre, on their own merits, rather than compared directly to human actors.”
- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-2`** [2]
  - Trecho: Scottish actress Briony Monroe said publicly that she believed Norwood was partly based on her likeness, because one promotional image looked like her.
  - Justificativa: A evidência (referência 5ce8f4f18e277b9e) afirma explicitamente que Briony Monroe, atriz escocesa de 28 anos, disse publicamente (ao jornal The Scotsman) que acredita que Tilly Norwood foi parcialmente baseada em sua se…
  - Suporte veio de: [2]
  - Evidência: “Briony Monroe, a 28-year-old actress from Scotland told The Scotsman on Wednesday that she believes Tilly Norwood was partially based on her likeness, as one particular image used to promote Norwood resembled her.”
### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-10`** [9]
  - Trecho: Chief negotiator Duncan Crabtree-Ireland has said that in the end an arbitrator will decide whether a synthetic actually delivered significant additional value.
  - Justificativa: A evidência menciona que produtores precisam demonstrar que atores sintéticos oferecem 'significant additional value', mas não menciona Duncan Crabtree-Ireland, nem afirma que um árbitro decidirá a questão. Esses elemen…
  - Suporte veio de: [9]
  - Não coberto pela evidência: Chief negotiator Duncan Crabtree-Ireland; an arbitrator will decide whether a synthetic actually delivered significant additional value
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [7] [5] [6] [3] [8] [4] [10] [19] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-14`** [12]
  - Trecho: The voice is arguably the most exposed part of a performer's identity. One reason is that voice cloning needs relatively little data. Another is that the law has never treated a voice as property in the way it treats a…
  - Justificativa: A evidência sustenta as partes sobre o caso Scarlett Johansson vs. OpenAI (abordagem, recusa, pausa do Sky, declaração de Altman), mas não contém nenhuma informação sobre voz como 'a parte mais exposta da identidade de…
  - Suporte veio de: [12]
  - Evidência: “OpenAI approached her in September about supplying the voice”
  - Não coberto pela evidência: The voice is arguably the most exposed part of a performer's identity; voice cloning needs relatively little data; the law has never treated a voice as property in the way it treats a recording
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-40`** [35]
  - Trecho: The settlement received final approval on July 20, 2026
  - Justificativa: A evidência confirma que o acordo recebeu aprovação final em uma segunda-feira ('Monday'), mas não fornece a data específica de 20 de julho de 2026. A data exata não pode ser inferida a partir da evidência.
  - Suporte veio de: [35]
  - Não coberto pela evidência: July 20, 2026
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 1 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-20` — Referencia(s) citada(s) ['802e23e78b42446c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-51` — Referencia(s) citada(s) ['89127e7e5f38bd2c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_6721cb7ebff0_20261115T130659Z-56` — Referencia(s) citada(s) ['d83e3d65a0cec798'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.