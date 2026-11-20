# Relatório de Auditoria — Claude (rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z)

**Arquivo auditado:** `answers/Ingles/Claude/EmConsolidacao/rede_social_saude_mental_adolecentes.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-18T03:06:51.495502+00:00 |
| **Total de trechos citados** | 82 |
| **Tempo de processamento** | 2:23:42:36 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 28.7 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 93 marcadores, 39 distintos |
| Referências listadas | 39 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 70 | 85.4% |
| **UNSUPPORTED** | 10 | 12.2% |
| **CONTRADICTED** | 2 | 2.4% |
| **TOTAL** | 82 | 100.0% |

Sobre os 82 trechos citados auditados: SUPPORTED 85,36%, UNSUPPORTED 12,19%, CONTRADICTED 2,43%.

> **20 dos 70 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 20 estão **contados dentro** dos 70 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`14` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `4` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 3, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#43` The National Academies adds support for youth facing bereavement or illness and community for LGBTQ+ teens. | [4] | [7] [14] [5] [1] [2] | — |
| `#46` Online refuges and offline distress are therefore intertwined, and blanket restrictions risk removing support from the… | [6] | [2] [7] [20] [27] [17] [5] [1] | — |
| `#71` The US Congress has still not enacted the Kids Online Safety Act (KOSA) or COPPA 2.0, its companion bill to extend chil… | [33] | [28] [34] [8] [39] | — |
| `#73` In October 2026 the Eleventh Circuit allowed Florida's under-14 ban to be enforced. | [35] | [8] [34] [27] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 701699 |
| **Média de tokens por requisição** | 8557.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/39 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 3.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13668480) | downloaded | 7 | 6 | 1 | 0 | 0 |
| [[4]](https://www.nationalacademies.org/news/to-minimize-harms-and-maximize-benefits-of-social-media-to-adolescent-health-new-report-recommends-setting-industrywide-standards-new-protections-against-harassment) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[5]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[6]](https://www.pewresearch.org/internet/2025/04/22/teens-social-media-and-mental-health/) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[15]](https://platformer.news/anxious-generation-jonathan-haidt-debate-critique/) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[2]](https://repec.cepr.org/repec/cpr/ceprdp/DP17252.pdf) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[10]](https://www.npr.org/2026/03/25/nx-s1-5746125/meta-youtube-social-media-trial-verdict) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[12]](https://www.biometricupdate.com/202608/no-age-checks-for-half-of-australian-kids-but-social-media-accounts-still-drop-10) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[27]](https://mdlupdate.com/mdl/3047-social-media-adolescent-addiction/) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[3]](https://www.contemporarypediatrics.com/view/social-media-potentially-linked-to-depression-in-children) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[7]](https://www.thetrevorproject.org/research-briefs/online-experiences-and-mental-health-of-lgbtq-young-people/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[8]](https://en.wikipedia.org/wiki/Social_media_age_verification_laws_by_country) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[9]](https://www.euronews.com/2026/09/22/eu-kids-act-the-eus-plan-to-make-the-internet-safer-for-kids) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[11]](https://www.pearlcohen.com/meta-settles-with-attorneys-general-for-up-to-17-billion-agrees-to-design-changes/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11850730/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[16]](https://www.ox.ac.uk/node/1434409) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[17]](https://www.researchsquare.com/article/rs-11170337/v1) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[21]](https://www.cnbc.com/2021/09/14/facebook-documents-show-how-toxic-instagram-is-for-teens-wsj.html) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[14]](https://cdc.gov/yrbs/dstr/pdf/YRBS-2023-Data-Summary-Trend-Report.pdf?os=0) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[24]](https://dsnlab.web.unc.edu/wp-content/uploads/sites/12535/2023/02/jamapediatrics_maza_2023_oi_220079_1675957138.23451-1.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[18]](https://matthewbjane.quarto.pub/social-media-and-mental-health/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[19]](https://openresearch-repository.anu.edu.au/entities/publication/543a7b5f-034e-41a5-a4a3-171980e24359) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641642/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[22]](https://www.irishtimes.com/world/uk/2022/09/30/global-first-ruling-that-online-content-contributed-to-14-year-old-molly-russells-death) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://www.americanbanker.com/news/fincen-warns-of-surge-in-financially-motivated-sextortion) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[25]](https://www.unc.edu/?p=224688) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[26]](https://oag.ca.gov/news/press-releases/attorney-general-bonta-unredacted-federal-lawsuit-against-meta-%E2%80%9Cdamning%E2%80%9D) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://www.childrenandscreens.org/newsroom/news/policy-update-july-2026/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[29]](https://variety.com/2026/digital/news/meta-18-billion-settlement-state-ags-lawsuit-social-media-addiction-1236843725/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[30]](https://www.popsci.com/technology/warning-labels-social-media/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[31]](https://www.apa.org/news/press/releases/2024/06/social-media-youth) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://www.globalpolicywatch.com/2026/06/online-safety-in-the-uk-social-media-ban-for-under-16s-and-other-recent-developments/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.crowell.com/en/insights/client-alerts/house-advances-bipartisan-kids-online-safety-bill-but-senate-showdown-looms) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[34]](https://www.loeb.com/en/insights/publications/2026/06/childrens-online-privacy-2026-state-app-store-design-code-and-social-media-laws) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://ccianet.org/news/2026/10/appeals-court-finds-floridas-law-restricting-social-media-can-be-enforced/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[36]](https://www.esafety.gov.au/newsroom/media-releases/platforms-restrict-access-to-47-million-under-16-accounts-across-australia) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://www.esafety.gov.au/research/social-media-age-restrictions-evaluation) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://research.birmingham.ac.uk/en/publications/school-phone-policies-and-their-association-with-mental-wellbeing/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[39]](https://mollyrosefoundation.org/instagram-teen-accounts-fail-to-protect-children-first-of-its-kind-testing-of-safety-tools-reveals/) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13668480) | #0, #13–14, #25, #27, #50 | #29 | — | `#0` problematic SMU, characterized by compulsive behavior and its interference with basic daily functioning, has been shown to have a stronger and more consistent… |
| [[4]](https://www.nationalacademies.org/news/to-minimize-harms-and-maximize-benefits-of-social-media-to-adolescent-health-new-report-recommends-setting-industrywide-standards-new-protections-against-harassment) | #2, #9, #65 | #24, #43 | — | `#2` The report concludes there is not enough evidence to say that social media causes changes in adolescent health at the population level |
| [[5]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use) | #30, #32, #34, #38 | #3 | — | `#30` Data indicate that technology use particularly within one hour of bedtime, and social media use in particular, is associated with sleep disruptions. Insufficie… |
| [[6]](https://www.pewresearch.org/internet/2025/04/22/teens-social-media-and-mental-health/) | #31, #41–42 | #3, #46 | — | `#31` Four-in-ten or more teens say social media platforms hurt the amount of sleep they get (45%), as well as their productivity (40%). Small shares – about one-in-… |
| [[15]](https://platformer.news/anxious-generation-jonathan-haidt-debate-critique/) | #47–49 | #10, #23 | — | `#47` Haidt proposes four changes that he believes to break what he calls "collective action traps": no smartphones before high school, no social media before the ag… |
| [[2]](https://repec.cepr.org/repec/cpr/ceprdp/DP17252.pdf) | #1, #16–18 | — | — | `#1` the introduction of Facebook at a college had a negative impact on student mental health |
| [[10]](https://www.npr.org/2026/03/25/nx-s1-5746125/meta-youtube-social-media-trial-verdict) | #54–55, #57 | #5 | — | `#54` A California jury on Wednesday found that Meta and Google were to blame for the depression and anxiety of a woman who compulsively used social media as a small… |
| [[12]](https://www.biometricupdate.com/202608/no-age-checks-for-half-of-australian-kids-but-social-media-accounts-still-drop-10) | #75–77 | #6 | — | `#75` The number of children with restricted social media accounts was 52.4 percent when Australia's new rules took effect last December, and decreased to 42.1 perce… |
| [[27]](https://mdlupdate.com/mdl/3047-social-media-adolescent-addiction/) | #56, #59, #62 | #58 | — | `#56` The second California bellwether trial (JCCP 5255) was set to open with jury selection on **October 28, 2026** in Los Angeles... Opening statements are expecte… |
| [[3]](https://www.contemporarypediatrics.com/view/social-media-potentially-linked-to-depression-in-children) | #19–20 | — | #1 | `#19` The study observed a marked increase in time spent on social media, from a mean of 7 minutes per day at baseline to 73 minutes daily by year 3. |
| [[7]](https://www.thetrevorproject.org/research-briefs/online-experiences-and-mental-health-of-lgbtq-young-people/) | #44–45 | #3 | — | `#44` The majority of LGBTQ+ young people agreed that they go online to connect with others because it is difficult to do so in their daily lives, with 38% somewhat… |
| [[8]](https://en.wikipedia.org/wiki/Social_media_age_verification_laws_by_country) | #4, #66, #70 | — | — | `#4` The ban came into effect on 10 December 2025. Australia then became the first country in the world to ban social media, banning platforms YouTube, TikTok, X, F… |
| [[9]](https://www.euronews.com/2026/09/22/eu-kids-act-the-eus-plan-to-make-the-internet-safer-for-kids) | #68–69 | — | #4 | `#68` Service providers can’t encourage compulsive or excessive use through endless autoplay, infinite scrolling, or rewards for posting. […] Recommenders that sugge… |
| [[11]](https://www.pearlcohen.com/meta-settles-with-attorneys-general-for-up-to-17-billion-agrees-to-design-changes/) | #5, #61 | #60 | — | `#5` a bipartisan coalition of 51 state attorneys general announced a settlement with Meta Platforms, Inc. [...] Meta will pay the states up to $17 billion over ten… |
| [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11850730/) | #79–80 | #6 | — | `#79` As expected, participants in schools with restrictive policies reported less phone use during the school day (by about 30 min), but compensated for this when o… |
| [[16]](https://www.ox.ac.uk/node/1434409) | #11–12, #51 | — | — | `#11` Study finds only 0.4% of wellbeing in adolescents is associated with technology use; Most definitive study to date, using data from 300,000 adolescents and par… |
| [[17]](https://www.researchsquare.com/article/rs-11170337/v1) | #15, #26 | #21 | — | `#15` Social media use was associated with poorer mental health outcomes (*SMD* = 0.21, 95% *CI* [0.16, 0.27], *p* < .001), although heterogeneity was substantial. D… |
| [[21]](https://www.cnbc.com/2021/09/14/facebook-documents-show-how-toxic-instagram-is-for-teens-wsj.html) | #33, #36 | #52 | — | `#33` "Thirty-two percent of teen girls said that when they felt bad about their bodies, Instagram made them feel worse," the researchers reportedly wrote. |
| [[14]](https://cdc.gov/yrbs/dstr/pdf/YRBS-2023-Data-Summary-Trend-Report.pdf?os=0) | #7 | — | #8 ⚡ | `#7` \|**Seriously considered attempting**<br>**suicide**\|17\|18\|17\|19\|22\|20\|\|\| |
| [[24]](https://dsnlab.web.unc.edu/wp-content/uploads/sites/12535/2023/02/jamapediatrics_maza_2023_oi_220079_1675957138.23451-1.pdf) | #39–40 | — | — | `#39` those with nonhabitual checking behaviors showed initial hyperactivation and decreasing sensitivity over time |
| [[18]](https://matthewbjane.quarto.pub/social-media-and-mental-health/) | — | #22 | — | `#22` Due to some initial concerns about data quality, the preliminary analyses have been taken down. |
| [[19]](https://openresearch-repository.anu.edu.au/entities/publication/543a7b5f-034e-41a5-a4a3-171980e24359) | #28 | — | — | `#28` Meta-analyses found small but significant positive associations between social media use, depression, and anxiety. In addition, problematic social media use wa… |
| [[20]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641642/) | #29 | — | — | `#29` Research shows that passive browsing of others' content often leads to negative psychological effects, while active engagement can yield positive outcomes |
| [[22]](https://www.irishtimes.com/world/uk/2022/09/30/global-first-ruling-that-online-content-contributed-to-14-year-old-molly-russells-death) | #35 | — | — | `#35` Concluding it would not be “safe” to rule the cause of Molly’s death as suicide, Mr Walker said the teenager “died from an act of self-harm while suffering dep… |
| [[23]](https://www.americanbanker.com/news/fincen-warns-of-surge-in-financially-motivated-sextortion) | — | #37 | — | `#37` While anyone can become a victim of sextortion, the schemes often target boys aged 14 to 17. The National Center for Missing & Exploited Children reports that… |
| [[25]](https://www.unc.edu/?p=224688) | — | — | #39 | — |
| [[26]](https://oag.ca.gov/news/press-releases/attorney-general-bonta-unredacted-federal-lawsuit-against-meta-%E2%80%9Cdamning%E2%80%9D) | #53 | — | — | `#53` a bipartisan coalition of 33 attorneys general against Meta Platforms, Inc. and affiliates (Meta) on October 24, 2023 ... Mark Zuckerberg personally vetoed Met… |
| [[28]](https://www.childrenandscreens.org/newsroom/news/policy-update-july-2026/) | — | — | #60 | — |
| [[29]](https://variety.com/2026/digital/news/meta-18-billion-settlement-state-ags-lawsuit-social-media-addiction-1236843725/) | — | — | #60 ⚡ | `#60` All told, a bipartisan group of 52 attorneys general across U.S. states, territories and the District of Columbia joined the agreement with Meta. |
| [[30]](https://www.popsci.com/technology/warning-labels-social-media/) | — | #63 | — | `#63` It is time to require a surgeon general's warning label on social media platforms, stating that social media is associated with significant mental health harms… |
| [[31]](https://www.apa.org/news/press/releases/2024/06/social-media-youth) | #64 | — | — | `#64` We applaud Surgeon General Vivek Murthy for calling attention to the potential dangers to children posed by social media platforms. |
| [[32]](https://www.globalpolicywatch.com/2026/06/online-safety-in-the-uk-social-media-ban-for-under-16s-and-other-recent-developments/) | #67 | — | — | `#67` These developments follow new legislative powers created by two Acts that received Royal Assent on 29 April 2026: the CWSA and the Crime and Policing Act 2026… |
| [[33]](https://www.crowell.com/en/insights/client-alerts/house-advances-bipartisan-kids-online-safety-bill-but-senate-showdown-looms) | — | #71 | — | `#71` Both KOSA and COPPA 2.0 have previously cleared the Senate and the House Energy and Commerce Committee, but neither has reached the President's desk. |
| [[34]](https://www.loeb.com/en/insights/publications/2026/06/childrens-online-privacy-2026-state-app-store-design-code-and-social-media-laws) | #72 | — | — | `#72` Virginia's social media law (SB 854), which took effect Jan. 1 and imposed a one-hour daily time limit on social media use by minors under 16, was enjoined on… |
| [[35]](https://ccianet.org/news/2026/10/appeals-court-finds-floridas-law-restricting-social-media-can-be-enforced/) | — | #73 | — | `#73` The Eleventh Circuit Court of Appeals has ruled that Florida’s HB3, restricting access to social media for teens, can be enforced ahead of the First Amendment… |
| [[36]](https://www.esafety.gov.au/newsroom/media-releases/platforms-restrict-access-to-47-million-under-16-accounts-across-australia) | #74 | — | — | `#74` Major social media companies removed access to about 4.7 million accounts identified as belonging to children under 16 in the first half of December to comply… |
| [[37]](https://www.esafety.gov.au/research/social-media-age-restrictions-evaluation) | #78 | — | — | `#78` The study follows more than 4000 children and families for more than two-years using a range of complementary research methods [...] We will explore a wide ran… |
| [[38]](https://research.birmingham.ac.uk/en/publications/school-phone-policies-and-their-association-with-mental-wellbeing/) | #79 | — | — | `#79` Adolescents attending schools with restrictive, compared to permissive policies had lower phone (adjusted mean difference −0.67 h, 95% CI −0.92 to −0.43, p = 0… |
| [[39]](https://mollyrosefoundation.org/instagram-teen-accounts-fail-to-protect-children-first-of-its-kind-testing-of-safety-tools-reveals/) | #81 | — | — | `#81` Users of Teen Accounts able to view content that promotes suicide, self-harm and eating disorders, with autocomplete suggestions actively recommending search t… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-0`** [1]
  - Trecho: Compulsive or "problematic" use, by contrast, shows a much more consistent tie to depression, anxiety and stress.
  - Justificativa: A evidência afirma explicitamente que o uso problemático de redes sociais (caracterizado por comportamento compulsivo) tem uma relação mais forte e consistente com depressão, ansiedade e estresse, o que corresponde dire…
  - Suporte veio de: [1]
  - Evidência: “problematic SMU, characterized by compulsive behavior and its interference with basic daily functioning, has been shown to have a stronger and more consistent relationship with negative mental health outcomes such as de…”
- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-1`** [2] [3]
  - Trecho: The strongest quasi-experimental and within-person studies point to real but modest harm.
  - Justificativa: A janela descreve um estudo quasi-experimental (introdução do Facebook em faculdades) e within-person (tempo de exposição, Seção 5.3) que encontra efeitos negativos reais mas modestos na saúde mental: tamanho de efeito…
  - Suporte veio de: [2]
  - Evidência: “the introduction of Facebook at a college had a negative impact on student mental health”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [2] | sustenta | the introduction of Facebook at a college had a negative impact on student mental health |

  - Verificação: reclassificado para SUPPORTED na etapa `full_doc_scan` (baseline dizia: "A evidência contém um estudo quasi-experimental (Braghieri et al.) e um estudo within-person (Nagata) que encontram efeitos negativos, mas…") — cascata: baseline → context_expansion → full_doc_scan
- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-2`** [4]
  - Trecho: Even so, the National Academies of Sciences, Engineering, and Medicine concluded that there is not enough evidence to say social media changes adolescent health at the population level.
  - Justificativa: A evidência contém uma afirmação praticamente idêntica à do trecho avaliado: o relatório das National Academies of Sciences, Engineering, and Medicine conclui que não há evidência suficiente para dizer que as redes soci…
  - Suporte veio de: [4]
  - Evidência: “The report concludes there is not enough evidence to say that social media causes changes in adolescent health at the population level”
### UNSUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-10`** [15]
  - Trecho: That timing is the backbone of Jonathan Haidt's argument that a "phone-based childhood" caused the teen mental health crisis.
  - Justificativa: A evidência confirma que Haidt defende que uma 'phone-based childhood' causou a crise de saúde mental entre adolescentes, e menciona elementos temporais ('roughly 12 years ago', 'early 2010s'). No entanto, em nenhum mom…
  - Suporte veio de: [15]
  - Evidência: “the new phone-based childhood that took shape roughly 12 years ago is making young people sick and blocking their progress to flourishing in adulthood.”
  - Não coberto pela evidência: A afirmação de que o 'timing' é a 'espinha dorsal' (backbone) do argumento de Haidt
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-21`** [17]
  - Trecho: The effects are small and observational, and the finding conflicts with the preprint synthesis, which found effects in both directions: use predicted later poorer mental health (d = 0.25), and poorer mental health predi…
  - Justificativa: A evidência confirma os valores de d (0.25 e 0.18) e os efeitos bidirecionais, mas NÃO menciona nenhum 'preprint synthesis' nem qualquer conflito entre achados. A afirmação central do trecho — de que 'the finding confli…
  - Suporte veio de: [17]
  - Evidência: “greater social media use was prospectively associated with poorer subsequent mental health (d = 0.25, 95% CI [0.12, 0.37], p < .001)”
  - Não coberto pela evidência: A existência de um 'preprint synthesis' não é mencionada na evidência; A afirmação de que 'the finding conflicts with the preprint synthesis' não tem base na evidência; O termo 'observational' não aparece explicitamente na evidência (embora 'longitudinal' sugira desenho observacional, não é rotulado como tal)
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-22`** [18]
  - Trecho: One planned meta-analysis of them took down its preliminary results "due to some initial concerns about data quality." Przybylski argues that the evidence linking *reduced* screen time to *better* wellbeing is even weak…
  - Justificativa: A evidência sustenta apenas a primeira parte do trecho (a retirada de resultados preliminares devido a preocupações com qualidade de dados), mas não menciona Przybylski nem seu argumento sobre a evidência ligando reduçã…
  - Suporte veio de: [18]
  - Evidência: “Due to some initial concerns about data quality, the preliminary analyses have been taken down.”
  - Não coberto pela evidência: Przybylski argues that the evidence linking reduced screen time to better wellbeing is even weaker than the correlational evidence.
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-8`** [14]
  - Trecho: Girls reported every outcome more often than boys, and 77% of students used social media several times a day.
  - Justificativa: A segunda parte da afirmação (77% usavam redes sociais várias vezes ao dia) é sustentada pela evidência. Porém, a primeira parte ('Girls reported every outcome more often than boys') é contraditada: a evidência mostra q…
  - Suporte veio de: [14]
  - Evidência: “In 2023, 77% of high school students used social media several times a day .”
- **Trecho citado `rede_social_saude_mental_adolecentes_19a5564d5b8d_20261115T032415Z-60`** [11] [28] [29]
  - Trecho: Reports put the size of the coalition at anywhere from 47 to 51 attorneys general, and at least one outlet reported the value as up to $18 billion.
  - Justificativa: A afirmacao sobre o valor de até $18 bilhoes e sustentada pela referencia 79c6ac176d5d0664. Porem, a afirmacao sobre o tamanho da coalizao variando de 47 a 51 procuradores-gerais e contradita: a evidencia menciona 52 pr…
  - Suporte veio de: [29]
  - Evidência: “Meta will pay up to $18 billion over 10 years”
  - Não coberto pela evidência: O numero 47 como limite inferior do tamanho da coalizao nao aparece em nenhuma fonte; A faixa '47 a 51' como um todo nao corresponde aos dados da evidencia
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [29] | contradiz | All told, a bipartisan group of 52 attorneys general across U.S. states, territories and the District of Columbia joine… |
    | [11] | parcial | a bipartisan coalition of 51 state attorneys general announced a settlement with Meta Platforms, Inc. |
    | [28] | ausente | — |

  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta o valor de até $18 bilhões, mas não confirma a faixa de '47 a 51' attorneys general. A evidência menciona 51 e 52 AGs,…") — cascata: baseline → context_expansion