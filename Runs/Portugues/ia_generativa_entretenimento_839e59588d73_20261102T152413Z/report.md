# Relatório de Auditoria — Claude (ia_generativa_entretenimento_839e59588d73_20261102T152413Z)

**Arquivo auditado:** `answers/Claude/Emergente/ia_generativa_entretenimento.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | ia_generativa_entretenimento_839e59588d73_20261102T152413Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-04T03:31:05.800318+00:00 |
| **Total de trechos citados** | 68 |
| **Tempo de processamento** | 1:12:06:53 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 31.4 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 68 marcadores, 53 distintos |
| Referências listadas | 53 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 47 | 69.1% |
| **UNSUPPORTED** | 6 | 8.8% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 15 | 22.1% |
| **TOTAL** | 68 | 100.0% |

Sobre os 53 trechos citados auditados: SUPPORTED 88,67%, UNSUPPORTED 11,32%, CONTRADICTED 0,00%.

> **4 dos 47 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 4 estão **contados dentro** dos 47 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`6` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `1` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `0` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `2` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#29` A iniciativa se conecta à United Voice Artists, rede internacional de associações de dublagem, que reuniu mais de 50 mi… | [21] | [19] [20] [9] [24] [30] [31] [5] [7] [44] [49] [3] [16] [32] [50] | — |
| `#63` As fontes divergem sobre a data exata de vigência ao longo de 2026, e vários Estados-membros observaram que os problema… | [50] | [49] [28] [31] [48] [25] [47] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 220730 |
| **Média de tokens por requisição** | 4164.7 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/53 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[9]](https://www.screendaily.com/news/sag-aftra-speaks-out-over-ai-actress-tilly-norwood-creativity-should-remain-human-centred/5209482.article) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[1]](https://fortune.com/2026/03/28/actors-union-sag-aftra-contract-bargaining-tilly-tax-ai-film-characters-hollywood-studios/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[4]](https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[5]](https://variety.com/2026/film/news/sag-aftra-ai-tilly-norwood-tax-digital-performers-1236644931/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://chatgptiseatingtheworld.com/2025/07/10/judge-oetken-allows-new-york-law-misappropriation-claim-by-voice-actors-v-lovo-ai-co-and-limited-copryight-claim-based-on-sages-sound-recordings/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[17]](https://www.news4jax.com/entertainment/2025/07/09/video-game-performers-vote-on-contract-that-could-end-nearly-three-year-long-battle-over-ai/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[18]](https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[27]](https://www.congress.gov/bill/119th-congress/senate-bill/4591) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[28]](https://www.hklaw.com/en/insights/publications/2026/06/senate-judiciary-committee-advances-legislation-to-protect-name) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[29]](https://thehill.com/opinion/congress-blog/technology/6124241-congress-no-fakes-act-vote/) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[31]](https://www.nbcnews.com/tech/tech-news/openai-sora-2-guardrails-sag-aftra-bryan-cranston-rcna238715) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[51]](https://www.cria.digital/blog/marco-legal-da-ia-pl-2338) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[2]](https://www.sagaftra.org/sag-aftra-members-approve-2026-tvtheatrical-contracts-tentative-agreement) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[3]](https://senalnews.com/en/content/sag-aftra-members-approve-2026-tv-theatrical-contracts-tentative-agreement/amp) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[6]](https://variety.com/2026/film/news/sag-aftra-amptp-contract-retirement-funds-1236735826/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://www.thewrap.com/industry-news/tech/sag-aftra-ai-protections-in-new-contract-synthetic/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[8]](https://www.cartoonbrew.com/artist-rights/sag-aftra-tv-animation-deal-vote-267544.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://au.variety.com/2026/film/news/ai-actor-tilly-norwood-movie-debut-misaligned-38324/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[11]](https://news.northeastern.edu/?p=307768) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://techcrunch.com/2024/05/20/scarlett-johansson-says-that-openai-approached-her-to-use-her-voice) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[13]](https://www.ddg.fr/actualite/lehrman-and-sage-v-lovo-inc-a-landmark-us-decision-on-voice-cloning-and-ai) | dead | 1 | 0 | 0 | 0 | 1 |
| [[14]](https://www.silicon.co.uk/e-regulation/legal/actor-ai-lawsuit-621581/amp) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[16]](https://www.law360.com/bankruptcy-authority/cases/66463465c58d261f4e979e33/articles) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://ids.org.br/noticia/dubladores-brasileiros-criam-movimento-dublagem-viva-para-pedir-a-regulamentacao-do-uso-da-ia/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://www.mundoconectado.com.br/inteligencia-artificial/dubladores-campanha-regulamentacao-inteligencia-artificial/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.maisgoias.com.br/entretenimento/dubladores-brasileiros-temem-substituicao-por-inteligencia-artificial/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[22]](https://www.lexblog.com/?p=2768510) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[23]](https://www.globalpolicywatch.com/2024/09/california-passes-digital-replica-legislation-as-congress-considers-federal-approach/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[24]](https://www.hollywoodreporter.com/business/business-news/gavin-newsom-signs-ai-bills-supported-sag-aftra-1236004935/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://wiki.private.law/en/publicity-rights-ai.md) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://www.manatt.com/insights/newsletters/client-alert/congress-reintroduces-the-no-fakes-act-what-s-new-in-the-2026-bill) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://salazar.house.gov/media/press-releases/rep-salazars-no-fakes-act-advances-out-senate-judiciary-committee-unanimous) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://www.thewrap.com/bryan-cranston-open-ai-sora-2-guardrails/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://kvia.com/news/business-technology/cnn-business-consumer/2025/12/11/disney-is-investing-1-billion-in-openai-and-licensing-its-characters-for-sora/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://www.exchange4media.com/digital-news/openai-shuts-down-sora-ends-disney-deal-153241.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://variety.com/2026/film/news/midjourney-studios-ai-copyright-discovery-1236800902/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://www.courtlistener.com/docket/70513159/disney-enterprises-inc-v-midjourney-inc/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[40]](https://www.barchart.com/story/news/35789376/universal-music-and-ai-song-generator-udio-settle-lawsuit-and-partner-on-new-ai-music-platform) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[41]](https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[42]](https://completemusicupdate.com/universal-has-settled-its-lawsuit-with-udio-and-signed-ai-deals-with-udio-and-stability/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://www.taylorwessing.com/de/insights-and-events/insights/2025/11/gema-v-openai) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[44]](https://www.penningtonslaw.com/news-publications/latest-news/2026/ai-art-and-global-approaches-to-copyright-law) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[45]](https://www.mayerbrown.com/pt/insights/publications/2026/03/supreme-court-denies-review-in-ai-authorship-case) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[46]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/ai-transparency-european-commissions-guidelines-on-article-50-part-2-deployer-obligations) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[48]](https://www.mishcon.com/news/ai-act-transparency-obligations-code-of-practice-and-draft-guidelines) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[49]](https://verfassungsblog.de/copyrighting-voice-and-image/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[50]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/01/EPRS_ATA(2026)782611.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[52]](https://documentacao.senior.com.br/exigenciaslegais/noticias/federal/2025/2025-03-20-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[53]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | downloaded | 1 | 0 | 1 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[9]](https://www.screendaily.com/news/sag-aftra-speaks-out-over-ai-actress-tilly-norwood-creativity-should-remain-human-centred/5209482.article) | #11–13, #16 | — | — | `#11` Van der Velden has just launched AI talent studio Xicoia to create, manage and monetise hyperreal digital stars and responded over the weekend to the growing b… |
| [[1]](https://fortune.com/2026/03/28/actors-union-sag-aftra-contract-bargaining-tilly-tax-ai-film-characters-hollywood-studios/) | #1, #7 | #0 | — | `#1` “Collective bargaining has been the fastest and most effective way for the regulation of AI technology,” SAG-AFTRA Executive Director Duncan Crabtree-Ireland s… |
| [[5]](https://variety.com/2026/film/news/sag-aftra-ai-tilly-norwood-tax-digital-performers-1236644931/) | #5–6 | — | — | `#5` In the future, studios that use synthetic actors in place of humans might have to pay a royalty into a union fund. |
| [[15]](https://chatgptiseatingtheworld.com/2025/07/10/judge-oetken-allows-new-york-law-misappropriation-claim-by-voice-actors-v-lovo-ai-co-and-limited-copryight-claim-based-on-sages-sound-recordings/) | #20–21 | — | — | `#20` The motion is denied as to Sage's copyright claims based on the use of her original voice recording, and as to Plaintiffs' contract claims, New York Civil Righ… |
| [[17]](https://www.news4jax.com/entertainment/2025/07/09/video-game-performers-vote-on-contract-that-could-end-nearly-three-year-long-battle-over-ai/) | #24 | #23 | — | `#24` The time spent creating a digital replica will be compensated as work time, according to the agreement. The agreement also requires the employer to provide the… |
| [[28]](https://www.hklaw.com/en/insights/publications/2026/06/senate-judiciary-committee-advances-legislation-to-protect-name) | #37–38 | — | — | `#37` Individuals and companies can be held liable if they produce or distribute an unauthorized digital replica of someone's voice or visual likeness. Online platfo… |
| [[31]](https://www.nbcnews.com/tech/tech-news/openai-sora-2-guardrails-sag-aftra-bryan-cranston-rcna238715) | #43, #45 | — | — | `#43` Cranston subsequently raised the issue with SAG-AFTRA, the union representing more than 150,000 film and TV performers, which has resulted in a collaborative e… |
| [[51]](https://www.cria.digital/blog/marco-legal-da-ia-pl-2338) | #64–65 | — | — | `#64` O PL 2338/2023 foi aprovado pelo Senado em 10 de dezembro de 2024, seguiu para a Câmara dos Deputados em março de 2025 e, até outubro de 2026, continua em comi… |
| [[3]](https://senalnews.com/en/content/sag-aftra-members-approve-2026-tv-theatrical-contracts-tentative-agreement/amp) | #3 | — | — | `#3` The agreement is effective on July 1, 2026, and expires June 30, 2030. |
| [[6]](https://variety.com/2026/film/news/sag-aftra-amptp-contract-retirement-funds-1236735826/) | #8 | — | — | `#8` Instead, the union got the studios to agree not to use synthetics unless they bring “significant additional value” to the production. The union also got a new… |
| [[7]](https://www.thewrap.com/industry-news/tech/sag-aftra-ai-protections-in-new-contract-synthetic/) | #9 | — | — | `#9` And if an agreement between the producers and SAG-AFTRA isn't reached, the union "may arbitrate seeking damages in an amount that will not necessarily be limit… |
| [[8]](https://www.cartoonbrew.com/artist-rights/sag-aftra-tv-animation-deal-vote-267544.html) | #10 | — | — | `#10` The previous animation contract, ratified in 2024, established the union's first AI protections specifically for voice actors. |
| [[10]](https://au.variety.com/2026/film/news/ai-actor-tilly-norwood-movie-debut-misaligned-38324/) | #14 | — | — | `#14` "Misaligned" is currently in early development, with key collaborators currently being attached. |
| [[11]](https://news.northeastern.edu/?p=307768) | #15 | — | — | `#15` the release date hasn't been shared yet. Particle6 publicist Michelle Waldron said production is expected to take about a year. |
| [[12]](https://techcrunch.com/2024/05/20/scarlett-johansson-says-that-openai-approached-her-to-use-her-voice) | #17 | — | — | `#17` Sky is now being paused after OpenAI used it when demoing its new GPT-4o model last week. [...] Sky's voice is not an imitation of Scarlett Johansson but belon… |
| [[14]](https://www.silicon.co.uk/e-regulation/legal/actor-ai-lawsuit-621581/amp) | — | — | #19 | — |
| [[16]](https://www.law360.com/bankruptcy-authority/cases/66463465c58d261f4e979e33/articles) | #22 | — | — | `#22` Artificial intelligence-enabled voice generating software company Lovo Inc. has filed for Chapter 7 protection in New York in the midst of an ongoing putative… |
| [[19]](https://ids.org.br/noticia/dubladores-brasileiros-criam-movimento-dublagem-viva-para-pedir-a-regulamentacao-do-uso-da-ia/) | #27 | — | — | `#27` em novembro de 2023, um grupo de dubladores brasileiros aderiu a um movimento global para exigir a regulação da IA em produções audiovisuais. A adesão nacional… |
| [[20]](https://www.mundoconectado.com.br/inteligencia-artificial/dubladores-campanha-regulamentacao-inteligencia-artificial/) | #28 | — | — | `#28` A IA não deve ser usada para reproduzir vozes de atores em outros idiomas para Língua Portuguesa Brasileira a finalidade de substituir os dubladores. |
| [[21]](https://www.maisgoias.com.br/entretenimento/dubladores-brasileiros-temem-substituicao-por-inteligencia-artificial/) | — | #29 | — | `#29` A United Voice Artists, grupo global de associações de dublagem, lidera uma petição com mais de 50 mil assinaturas, no intuito de impedir a substituição de hum… |
| [[24]](https://www.hollywoodreporter.com/business/business-news/gavin-newsom-signs-ai-bills-supported-sag-aftra-1236004935/) | #33 | — | — | `#33` AB 1836, meanwhile, requires entertainment employers to gain the consent of a deceased performer's estate before using a digital replica of that person. |
| [[25]](https://wiki.private.law/en/publicity-rights-ai.md) | #34 | — | — | `#34` In December 2025 two further statutes were added, both signed on 11 December: S.8420-A on disclosure of a synthetic performer in advertising (an amendment to §… |
| [[26]](https://www.manatt.com/insights/newsletters/client-alert/congress-reintroduces-the-no-fakes-act-what-s-new-in-the-2026-bill) | #35 | — | — | `#35` The most significant change to the bill is a counter-notification process modeled off the Digital Millennium Copyright Act (DMCA) that allows users to contest… |
| [[30]](https://salazar.house.gov/media/press-releases/rep-salazars-no-fakes-act-advances-out-senate-judiciary-committee-unanimous) | #42 | — | — | `#42` Earlier this month, more than 16,000 SAG-AFTRA members signed an open letter urging Congress to pass the NO FAKES Act |
| [[32]](https://www.thewrap.com/bryan-cranston-open-ai-sora-2-guardrails/) | #44 | — | — | `#44` SAG-AFTRA says OpenAI apologized for the generations and committed to working with the union, CAA, UTA and the Association of Talent Agencies to strengthen the… |
| [[33]](https://kvia.com/news/business-technology/cnn-business-consumer/2025/12/11/disney-is-investing-1-billion-in-openai-and-licensing-its-characters-for-sora/) | #46 | — | — | `#46` although the agreement does not include any talent likenesses or voices. |
| [[34]](https://engadget.com/ai/openai-is-shutting-down-its-sora-video-generation-app-211023358.html) | #47 | — | — | `#47` OpenAI is shutting down its Sora video generation app. [...] We've decided to discontinue Sora in the consumer app and API. [...] — Sora (@soraofficialapp) Mar… |
| [[35]](https://www.exchange4media.com/digital-news/openai-shuts-down-sora-ends-disney-deal-153241.html) | #48 | — | — | `#48` The investment, however, had not been completed, and no capital was transferred before the shutdown. |
| [[36]](https://techcrunch.com/2026/07/04/midjourney-wants-hollywood-studios-to-reveal-the-details-of-their-ai-usage/) | #49 | — | — | `#49` A judge previously ruled that the studios would indeed have to provide information about their generative AI usage — but only when it led to “consumer-facing”… |
| [[37]](https://variety.com/2026/film/news/midjourney-studios-ai-copyright-discovery-1236800902/) | #50 | — | — | `#50` Midjourney's lawyers filed a motion this week urging Judge John Kronstadt to overturn that decision, arguing that the studios should have to divulge more much… |
| [[38]](https://www.courtlistener.com/docket/70513159/disney-enterprises-inc-v-midjourney-inc/) | #51 | — | — | `#51` The last day to file all motions is November 23, 2026. The Court grants the parties request to participate in a settlement conference with a private neutral. |
| [[42]](https://completemusicupdate.com/universal-has-settled-its-lawsuit-with-udio-and-signed-ai-deals-with-udio-and-stability/) | #55 | — | — | `#55` can record labels and music publishers unilaterally opt all their artists and songwriters, and their recordings and songs, into those deals? Or do they need sp… |
| [[43]](https://www.taylorwessing.com/de/insights-and-events/insights/2025/11/gema-v-openai) | #56 | — | — | `#56` In the court's view, memorization within the models and the subsequent reproduction of lyrics via the chatbot each infringed exclusive rights of exploitation.… |
| [[44]](https://www.penningtonslaw.com/news-publications/latest-news/2026/ai-art-and-global-approaches-to-copyright-law) | #57 | — | — | `#57` In November 2025, the High Court delivered judgment in *Getty Images v Stability AI*, finding in favour of Getty on trademark infringement but dismissing its s… |
| [[45]](https://www.mayerbrown.com/pt/insights/publications/2026/03/supreme-court-denies-review-in-ai-authorship-case) | #58 | — | — | `#58` the Supreme Court of the United States declined to grant review in *Thaler v. Perlmutter* (Case No. 25-449). In denying certiorari, the Court leaves standing,… |
| [[46]](https://www.bakerdonelson.com/supreme-court-denies-certiorari-in-thaler-v-perlmutter-ai-cannot-be-an-author-under-the-copyright-act) | #59 | — | — | `#59` Because Dr. Thaler disclaimed any human creative input, the court did not address how much human involvement is sufficient to support a copyright claim for AI-… |
| [[47]](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/ai-transparency-european-commissions-guidelines-on-article-50-part-2-deployer-obligations) | #60 | — | — | `#60` The European Commission recently announced that about 190 organisations signed the Code ahead of the entry into application of the Article 50 legal obligations… |
| [[48]](https://www.mishcon.com/news/ai-act-transparency-obligations-code-of-practice-and-draft-guidelines) | #61 | — | — | `#61` On 10 June 2026, the European Commission published the final version of its Code of Practice on Transparency of AI-Generated Content. |
| [[49]](https://verfassungsblog.de/copyrighting-voice-and-image/) | #62 | — | — | `#62` Traditionally, voice and image have been protected as personality rights that are not transferable, primarily defensive in nature, and only partially commercia… |
| [[50]](https://eprs.europarl.europa.eu/contents/publications/EPRS/2026/01/EPRS_ATA(2026)782611.html) | — | #63 | — | `#63` several Member States underlined that concerns linked to the production and dissemination of deepfakes extend beyond the remit of copyright law |
| [[52]](https://documentacao.senior.com.br/exigenciaslegais/noticias/federal/2025/2025-03-20-camara-comeca-a-discutir-projeto-que-regulamenta-a-inteligencia-artificial-no-brasil/) | #66 | — | — | `#66` Nos demais casos, o titular de direitos autorais poderá proibir o uso dos conteúdos protegidos. |
| [[53]](https://monitor.lcfconsulting.com.br/proposicoes/pl-2338-2023/) | — | #67 | — | `#67` votação adiada para depois das eleições de outubro/2026 |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.ddg.fr/actualite/lehrman-and-sage-v-lovo-inc-a-landmark-us-decision-on-voice-cloning-and-ai — Referencia nao encontrada (404): https://www.ddg.fr/actualite/lehrman-and-sage-v-lovo-inc-a-landmark-us-decision-on-voice-cloning-and-ai

### Bloqueadas por barreira de acesso

- https://www.sagaftra.org/sag-aftra-members-approve-2026-tvtheatrical-contracts-tentative-agreement — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930028-GRU 1793763013 862423481 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/contracts/2026-tvtheatrical-contracts — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930059-GRU 1793763013 2210511094 Varnish cache server
- https://www.sagaftra.org/contracts-industry-resources/member-resources/artificial-intelligence — http_error — barreira de acesso (http_error): Error 403 Forbidden Forbidden Error 54113 Details: cache-gru-sbgr1930083-GRU 1793763013 2493503078 Varnish cache server
- https://www.lexblog.com/?p=2768510 — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing this site. This process is automatic. You will arrive shortly. Verification succe
- https://www.globalpolicywatch.com/2024/09/california-passes-digital-replica-legislation-as-congress-considers-federal-approach/ — anti_bot — barreira de acesso (anti_bot): Checking your browser before accessing this site. This process is automatic. You will arrive shortly. Verification succe
- https://www.congress.gov/bill/119th-congress/senate-bill/4591 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://thehill.com/opinion/congress-blog/technology/6124241-congress-no-fakes-act-vote/ — anti_bot — barreira de acesso (anti_bot): Your browser appears to have Javascript disabled. For instructions on how to enable Javascript please click here . If yo
- https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.barchart.com/story/news/35789376/universal-music-and-ai-song-generator-udio-settle-lawsuit-and-partner-on-new-ai-music-platform — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable
- https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-1`** [1]
  - Trecho: O próprio diretor executivo do SAG-AFTRA, Duncan Crabtree-Ireland, passou a defender que a negociação coletiva tem sido a forma mais rápida e eficaz de regular a tecnologia.
  - Justificativa: A evidência cita diretamente Duncan Crabtree-Ireland, diretor executivo do SAG-AFTRA, afirmando que a negociação coletiva tem sido a forma mais rápida e eficaz de regular a tecnologia de IA, o que sustenta a afirmação d…
  - Suporte veio de: [1]
  - Evidência: ““Collective bargaining has been the fastest and most effective way for the regulation of AI technology,” SAG-AFTRA Executive Director Duncan Crabtree-Ireland said Thursday at an AFL-CIO workers’ summit in Washington.”
  - Não coberto pela evidência: O trecho afirma 'passou a defender', sugerindo uma mudança de postura ao longo do tempo, mas a evidência apenas registra a declaração em um evento específico, sem indicar mudança de posição anterior.
- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-3`** [3]
  - Trecho: O contrato vigora de 1º de julho de 2026 a 30 de junho de 2030.
  - Justificativa: A evidência afirma explicitamente que o acordo entra em vigor em 1º de julho de 2026 e expira em 30 de junho de 2030, correspondendo diretamente à afirmação.
  - Suporte veio de: [3]
  - Evidência: “The agreement is effective on July 1, 2026, and expires June 30, 2030.”
- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-5`** [5]
  - Trecho: A ideia era cobrar uma contribuição a um fundo sindical sempre que um estúdio usasse um ator sintético no lugar de um humano.
  - Justificativa: A evidência afirma explicitamente que estúdios que usam atores sintéticos no lugar de humanos poderiam ter que pagar um royalty para um fundo sindical, e que essa é uma das ideias em discussão. Isso sustenta diretamente…
  - Suporte veio de: [5]
  - Evidência: “In the future, studios that use synthetic actors in place of humans might have to pay a royalty into a union fund.”
### UNSUPPORTED

- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-0`** [1]
  - Trecho: Dela saíram as primeiras garantias contratuais de que os estúdios precisariam de consentimento informado e de remuneração justa para usar réplicas digitais de intérpretes.
  - Justificativa: A evidência confirma que a SAG-AFTRA obteve garantias de consentimento informado e remuneração justa para réplicas digitais de atores. No entanto, o trecho afirma que essas foram as 'primeiras' garantias contratuais des…
  - Suporte veio de: [1]
  - Evidência: “SAG-AFTRA secured several AI-related protections for its members, including requirements that studios obtain informed consent and provide fair compensation for the use of digital replicas, after a 2023 strike that groun…”
  - Não coberto pela evidência: as primeiras garantias contratuais — a evidência não afirma que essas foram as primeiras garantias desse tipo
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-19`** [14]
  - Trecho: Mais tarde descobriram que a empresa vendia versões clonadas de suas vozes com os nomes "Kyle Snow" e "Sally Coleman".
  - Justificativa: A evidência fornecida contém apenas manchetes de notícias e descrições de podcasts sobre tecnologia, sem qualquer menção a clonagem de vozes, nomes 'Kyle Snow' ou 'Sally Coleman', ou qualquer empresa vendendo versões cl…
  - Não coberto pela evidência: Descoberta posterior de venda de versões clonadas de vozes; Nomes 'Kyle Snow' e 'Sally Coleman'; Existência de uma empresa vendendo vozes clonadas
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-23`** [17]
  - Trecho: O novo contrato foi ratificado com 95% dos votos em julho de 2025.
  - Justificativa: A evidência confirma que 95% dos membros que votaram favoreceram a ratificação do novo contrato, mas não menciona a data de 'julho de 2025'. Como a evidência não fornece informação suficiente para confirmar a data espec…
  - Suporte veio de: [17]
  - Evidência: “SAG-AFTRA said 95% of the members who voted favored ratification.”
  - Não coberto pela evidência: julho de 2025
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 14 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 1 citam referência não baixada/inacessível.

- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-2` — Referencia(s) citada(s) ['cf4feb10962eb445'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-4` — Referencia(s) citada(s) ['0ad3078ef2adc633'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-18` — Referencia(s) citada(s) ['ec3751446ec09932'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-25` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-26` — Referencia(s) citada(s) ['9d0ca35723cdd785'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-30` — Referencia(s) citada(s) ['0ad3078ef2adc633'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-31` — Referencia(s) citada(s) ['409f4f93bfa35581'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-32` — Referencia(s) citada(s) ['f25206dddb6ca996'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-36` — Referencia(s) citada(s) ['5742a9651bf6ca88'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-39` — Referencia(s) citada(s) ['5742a9651bf6ca88'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-40` — Referencia(s) citada(s) ['87b390438278affb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-41` — Referencia(s) citada(s) ['87b390438278affb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-52` — Referencia(s) citada(s) ['89127e7e5f38bd2c'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-53` — Referencia(s) citada(s) ['cac5f3ab2ca8fb73'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `ia_generativa_entretenimento_839e59588d73_20261102T152413Z-54` — Referencia(s) citada(s) ['b8c1b1befacee0ee'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.