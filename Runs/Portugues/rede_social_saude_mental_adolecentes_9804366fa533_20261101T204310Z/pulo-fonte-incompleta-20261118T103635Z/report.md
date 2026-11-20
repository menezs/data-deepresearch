# Relatório de Auditoria — Claude (rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z)

**Arquivo auditado:** `answers/Claude/EmConsolidacao/rede_social_saude_mental_adolecentes.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-04T03:05:05.725969+00:00 |
| **Total de trechos citados** | 80 |
| **Tempo de processamento** | 2:06:21:55 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 26.8 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 83 marcadores, 35 distintos |
| Referências listadas | 35 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 59 | 73.8% |
| **UNSUPPORTED** | 6 | 7.5% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 15 | 18.8% |
| **TOTAL** | 80 | 100.0% |

Sobre os 65 trechos citados auditados: SUPPORTED 90,76%, UNSUPPORTED 9,23%, CONTRADICTED 0,00%.

> **10 dos 59 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 10 estão **contados dentro** dos 59 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`6` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `3` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `0` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `2` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#9` As meninas apresentaram taxas maiores que os meninos (13% contra 9%). | [17] | [16] [8] [23] [35] | — |
| `#20` Entre os coautores estão Haidt e Rausch, e um dos autores declara atuar como perito remunerado em ações judiciais sobre… | [11] | [35] [7] [18] [6] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 307326 |
| **Média de tokens por requisição** | 4728.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/35 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 3.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[23]](https://www.cetic.br/media/docs/publicacoes/2/pt-br/20260317181001/tic_kids_online_2025_resumo_executivo.pdf.pdf) | downloaded | 7 | 7 | 0 | 0 | 0 |
| [[11]](https://www.medrxiv.org/content/10.64898/2026.06.01.26354614v1) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[5]](https://metatoc.com/papers/118222-review-social-media-use-and-adolescent-mental-health-an-umbrella-review-and-power-analysis) | inaccessible | 4 | 0 | 0 | 0 | 4 |
| [[13]](https://www.ox.ac.uk/news/2022-03-28-negative-impact-social-media-affects-girls-and-boys-different-ages-study) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[14]](https://www.epocrates.com/online/article/addictive-screen-use-tied-to-suicide-risk-mental-health-issues-in-early) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[18]](https://www.ox.ac.uk/news/2026-03-19-world-happiness-report-2026-shows-complex-global-picture-social-media-and-happiness) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[2]](https://www.gdnonline.com/Details/1242509/Social-media-could-harm-youth-mental-health,-US-Surgeon-General-warns) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[16]](https://www.hbsc.org/?p=274696) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[19]](https://www.bostonglobe.com/2026/03/19/world/what-world-happiness-report-reveals-about-social-media-worlds-happiest-country/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[20]](https://observatorioglobal.udlap.mx/?p=5980) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[21]](https://www.chconline.org/resourcelibrary/teens-social-media-and-mental-health-downloadable/) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[24]](https://www.demarest.com.br/?p=166412) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[30]](https://www.radiox.co.uk/news/uk-world/most-australian-teens-still-on-social-media-d/) | dead | 3 | 0 | 0 | 0 | 3 |
| [[35]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13406646/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[1]](https://www.psychiatrictimes.com/view/us-surgeon-general-issues-advisory-on-impact-of-social-media-on-youth-mental-health) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[4]](https://www.hmpgloballearningnetwork.com/site/pcn/news/apa-recommends-smart-sane-social-media-use-adolescents) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[8]](https://www.simplypsychology.org/news/time-spent-on-social-media-adolescent-mental-health-problems-a-meta-analysis) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://medicaldialogues.in/mdtv/psychiatry/videos/addictive-screen-use-may-be-linked-to-poor-mental-health-in-preteens-study-finds-150383) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[22]](https://telehealth.org/news/assessing-social-media-harm-in-teens/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[26]](https://confidata.com.br/blog/eca-digital-o-que-muda-empresas) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[28]](https://euronews.com/next/2026/01/15/australia-under-16-social-media-ban-how-is-it-going-one-month-since-law-took-effect) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://www.aljazeera.com/news/2026/8/3/australias-under-16-social-media-ban-failing-study-shows-what-it-means) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[31]](https://abc30.com/amp/post/los-angeles-social-media-addiction-trial-jury-finds-instagram-youtube-liable-landmark-court-case/18771272/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[33]](https://www.washingtonexaminer.com/?p=4503360) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[3]](https://www.newswise.com/articles/apa-panel-issues-recommendations-for-adolescent-social-media-use) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[6]](https://www.klingensteincenter.org/klingbrief/under-protecting-qm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://platformer.news/anxious-generation-jonathan-haidt-debate-critique/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12421657) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://scholar.usuhs.edu/en/publications/social-media-reduction-or-abstinence-interventions-are-providing-/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://www.theregister.com/2026/03/19/social_media_bad_for_kids/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[17]](https://goinginternational.eu/en/news/2207) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[25]](https://www.conjur.com.br/?p=867020) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[27]](https://atarde.com.br/brasil/escolas-registram-maior-participacao-dos-alunos-em-1-ano-de-veto-ao-celular-1393684) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[32]](https://www.seegerweiss.com/news/jury-finds-meta-and-youtube-liable-in-landmark-california-social-media-addiction-trial/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[34]](https://www.milbank.org/quarterly/articles/us-state-policies-regarding-social-media-do-policies-match-the-evidence/) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[23]](https://www.cetic.br/media/docs/publicacoes/2/pt-br/20260317181001/tic_kids_online_2025_resumo_executivo.pdf.pdf) | #45–51 | — | — | `#45` Em 2025, 92% dos brasileiros de 9 a 17 anos eram usuários de Internet, o que corresponde a cerca de 24 milhões de crianças e adolescentes. |
| [[11]](https://www.medrxiv.org/content/10.64898/2026.06.01.26354614v1) | #18–19, #72–73 | #20 | — | `#18` Pooled estimates favoured SMU constraints across outcomes, with magnitude and precision varying by domain. Confidence intervals were entirely above zero, consi… |
| [[13]](https://www.ox.ac.uk/news/2022-03-28-negative-impact-social-media-affects-girls-and-boys-different-ages-study) | #29–30, #71 | #70 | — | `#29` girls experience a negative link between social media use and life satisfaction when they are 11-13 years old and boys when they are 14-15 years old. [...] Sen… |
| [[18]](https://www.ox.ac.uk/news/2026-03-19-world-happiness-report-2026-shows-complex-global-picture-social-media-and-happiness) | #33–35 | #70 | — | `#33` Heavy social media use appears to be contributing to the drop in wellbeing among young people in English-speaking countries and Western Europe, especially amon… |
| [[2]](https://www.gdnonline.com/Details/1242509/Social-media-could-harm-youth-mental-health,-US-Surgeon-General-warns) | #2–4 | — | — | `#2` Adolescents who spend more than three hours per day on social media face double the risk of experiencing poor mental health outcomes, such as symptoms of depre… |
| [[16]](https://www.hbsc.org/?p=274696) | #8, #68 | #10 | — | `#8` The proportion of adolescents classified as problematic social media users increased from 7% in 2018 to 11% in 2022. |
| [[19]](https://www.bostonglobe.com/2026/03/19/world/what-world-happiness-report-reveals-about-social-media-worlds-happiest-country/) | #36–37, #74 | — | — | `#36` But adolescents are spending an estimated average of 2.5 hours a day on social media. |
| [[20]](https://observatorioglobal.udlap.mx/?p=5980) | #38–39, #77 | — | — | `#38` Improvements in social connections (such as a sense of belonging at school) have a much stronger positive effect on life satisfaction than reductions in social… |
| [[24]](https://www.demarest.com.br/?p=166412) | #53–54, #79 | — | — | `#53` Em **17 de março de 2026,** entrou em vigor a Lei nº 15.211/2025, conhecida como o **Estatuto Digital da Criança e do Adolescente** (**__ECA Digital__**). |
| [[35]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13406646/) | #31–32, #69 | — | — | `#31` while those with externalizing conditions report a lack of control over how much time they spend on social media |
| [[1]](https://www.psychiatrictimes.com/view/us-surgeon-general-issues-advisory-on-impact-of-social-media-on-youth-mental-health) | #0–1 | — | — | `#0` noting that up to 95% of youth aged 13 to 17 years report using at least 1 social media platform, and more than a third report using social media platforms "al… |
| [[4]](https://www.hmpgloballearningnetwork.com/site/pcn/news/apa-recommends-smart-sane-social-media-use-adolescents) | #7, #76 | — | — | `#7` Adolescents using social media should be encouraged to find online communities that foster support, companionship, and health socialization to help alleviate s… |
| [[8]](https://www.simplypsychology.org/news/time-spent-on-social-media-adolescent-mental-health-problems-a-meta-analysis) | #13–14 | — | — | `#13` The mean effect of social media on mental health across all studies was β = .061, which is below the threshold for practical significance (r = .10). ... The pr… |
| [[15]](https://medicaldialogues.in/mdtv/psychiatry/videos/addictive-screen-use-may-be-linked-to-poor-mental-health-in-preteens-study-finds-150383) | #27 | — | #69 | `#27` Addictive use of social media, mobile phones, and video games- but not overall screen time- is associated with worsening mental health and increased risk of su… |
| [[22]](https://telehealth.org/news/assessing-social-media-harm-in-teens/) | #40, #42 | — | — | `#40` A 2025 Pew Research Center study of 13- to 17-year-olds and their parents reveals increasingly complex views about social media and mental health. Although 74%… |
| [[26]](https://confidata.com.br/blog/eca-digital-o-que-muda-empresas) | #56–57 | — | — | `#56` Até 10% do faturamento do grupo econômico no Brasil, limitada a **R$ 50 milhões por infração** |
| [[28]](https://euronews.com/next/2026/01/15/australia-under-16-social-media-ban-how-is-it-going-one-month-since-law-took-effect) | #58 | #59 | — | `#58` Rather than hold parents or children accountable, the rules mean platforms face fines of up to A$49.5 million (V27 million) for serious or repeated breaches of… |
| [[29]](https://www.aljazeera.com/news/2026/8/3/australias-under-16-social-media-ban-failing-study-shows-what-it-means) | #60 | #78 | — | `#60` A new study by Australia's internet regulator has revealed that more than eight in 10 young Australian teens and preteens are continuing to use social media pl… |
| [[31]](https://abc30.com/amp/post/los-angeles-social-media-addiction-trial-jury-finds-instagram-youtube-liable-landmark-court-case/18771272/) | #63–64 | — | — | `#63` The plaintiff, known by her initials KGM, testified at trial that she became addicted to social media as a child and that this addiction exacerbated her mental… |
| [[3]](https://www.newswise.com/articles/apa-panel-issues-recommendations-for-adolescent-social-media-use) | #6 | — | — | `#6` "Social media is neither inherently harmful nor beneficial to our youth," said APA President Thema Bryant, PhD. ... The report is careful to note that, given t… |
| [[6]](https://www.klingensteincenter.org/klingbrief/under-protecting-qm) | #11 | — | — | `#11` Hundreds of researchers, myself included, have searched for the kind of large effects suggested by Haidt. Our efforts have produced a mix of no, small, and mix… |
| [[7]](https://platformer.news/anxious-generation-jonathan-haidt-debate-critique/) | #12 | — | — | `#12` The average correlation between screen time and well-being was analogous to the correlation between wearing glasses and well being — it might just be a roundin… |
| [[9]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12421657) | #16 | — | — | `#16` Notable critiques included decisions related to study inclusion and exclusions; averaging across effect sizes from different types of experiments (i.e., social… |
| [[10]](https://scholar.usuhs.edu/en/publications/social-media-reduction-or-abstinence-interventions-are-providing-/) | #17 | — | — | `#17` These findings suggest that social media use reduction/abstinence interventions should have a minimum length of 1 week or longer to confer mental health benefi… |
| [[12]](https://www.theregister.com/2026/03/19/social_media_bad_for_kids/) | — | — | #15 | — |
| [[17]](https://goinginternational.eu/en/news/2207) | — | — | #9 | — |
| [[25]](https://www.conjur.com.br/?p=867020) | — | — | #55 | — |
| [[27]](https://atarde.com.br/brasil/escolas-registram-maior-participacao-dos-alunos-em-1-ano-de-veto-ao-celular-1393684) | #52 | — | — | `#52` O Ministério da Educação (MEC) junto ao Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) divulgou nesta terça-feira, 30, o primeir… |
| [[32]](https://www.seegerweiss.com/news/jury-finds-meta-and-youtube-liable-in-landmark-california-social-media-addiction-trial/) | #65 | — | — | `#65` Seeger Weiss Founding Partner Christopher Seeger serves as Counsel to the Co-Lead Counsel and Settlement Counsel in the Social Media Adolescent Addiction / Per… |
| [[34]](https://www.milbank.org/quarterly/articles/us-state-policies-regarding-social-media-do-policies-match-the-evidence/) | #24 | — | — | `#24` the current research base has significant limitations and cannot definitively establish causal effects. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.radiox.co.uk/news/uk-world/most-australian-teens-still-on-social-media-d/ — Referencia nao encontrada (404): https://www.radiox.co.uk/news/uk-world/most-australian-teens-still-on-social-media-d/

### Inacessíveis (403/timeout/SSL)

- https://metatoc.com/papers/118222-review-social-media-use-and-adolescent-mental-health-an-umbrella-review-and-power-analysis — download excedeu 90s

### Bloqueadas por barreira de acesso

- https://www.epocrates.com/online/article/addictive-screen-use-tied-to-suicide-risk-mental-health-issues-in-early — requires_js_login_region — barreira de acesso (requires_js_login_region): # Access limited to the U.S. At this time, epocrates is not available outside the U.S. Because we cannot guarantee that 
- https://www.chconline.org/resourcelibrary/teens-social-media-and-mental-health-downloadable/ — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. The action you just performed triggered 
- https://www.washingtonexaminer.com/?p=4503360 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-0`** [1]
  - Trecho: O documento registrou que até 95% dos jovens americanos de 13 a 17 anos usam pelo menos uma plataforma e que mais de um terço diz usá-las "quase constantemente".
  - Justificativa: A evidência afirma explicitamente que até 95% dos jovens de 13 a 17 anos relatam usar pelo menos uma plataforma de redes sociais e que mais de um terço relatam usá-las 'quase constantemente', o que corresponde diretamen…
  - Suporte veio de: [1]
  - Evidência: “noting that up to 95% of youth aged 13 to 17 years report using at least 1 social media platform, and more than a third report using social media platforms "almost constantly."”
  - Não coberto pela evidência: A palavra 'americanos' não aparece explicitamente na evidência, embora seja inferível pelo contexto do US Surgeon General.
- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-1`** [1]
  - Trecho: Também reuniu pesquisas que associam o uso excessivo a sintomas de depressão e ansiedade, baixa autoestima, comparação social, insatisfação corporal e alimentação desordenada, mas reconheceu que faltam estudos para dime…
  - Justificativa: A evidência cita explicitamente que o advisory reúne pesquisas que associam o uso excessivo de redes sociais a sintomas de depressão e ansiedade, baixa autoestima, comparação social, insatisfação corporal e alimentação…
  - Suporte veio de: [1]
  - Evidência: “The advisory also cites research supporting connections between excessive social media use and symptoms of depression and anxiety, low self-esteem, social comparison, body dissatisfaction, and disordered eating behavior…”
- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-2`** [2]
  - Trecho: O dado mais citado do aviso é que adolescentes que passam mais de três horas por dia nas redes teriam o dobro do risco de desfechos ruins de saúde mental, como sintomas depressivos e ansiosos.
  - Justificativa: A evidência afirma explicitamente que adolescentes que passam mais de três horas por dia em redes sociais enfrentam o dobro do risco de desfechos ruins de saúde mental, como sintomas de depressão e ansiedade, conforme o…
  - Suporte veio de: [2]
  - Evidência: “Adolescents who spend more than three hours per day on social media face double the risk of experiencing poor mental health outcomes, such as symptoms of depression and anxiety, according to the advisory.”
  - Não coberto pela evidência: A caracterização de que esse seria o 'dado mais citado' do aviso não é explicitamente afirmada na evidência.
### UNSUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-9`** [17]
  - Trecho: As meninas apresentaram taxas maiores que os meninos (13% contra 9%).
  - Justificativa: A evidência consiste apenas em um trecho de navegação de site, sem qualquer informação sobre taxas, meninas ou meninos. Não há dados que sustentem a afirmação.
  - Não coberto pela evidência: meninas apresentaram taxas maiores que os meninos; 13% contra 9%
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [16] [8] [23] [35] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-10`** [16]
  - Trecho: O mesmo relatório observou um lado positivo: adolescentes que usam muito as redes, mas sem padrão problemático, relataram mais apoio dos colegas e mais conexão social.
  - Justificativa: A evidência menciona aspectos positivos das redes sociais (conexão e conectividade) e cita um adolescente sobre benefícios do uso moderado, mas não afirma explicitamente que adolescentes que usam muito as redes sem padr…
  - Suporte veio de: [16]
  - Não coberto pela evidência: adolescentes que usam muito as redes, mas sem padrão problemático; relataram mais apoio dos colegas; relataram mais conexão social
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-15`** [12]
  - Trecho: Para isso, combinam estudos acadêmicos, documentos internos das empresas e relatos de pais, professores e jovens.
  - Justificativa: A evidência trata de notícias sobre IA, segurança da informação e software livre (FOSS). Não há qualquer menção a estudos acadêmicos, documentos internos de empresas ou relatos de pais, professores e jovens. A afirmação…
  - Não coberto pela evidência: combinação de estudos acadêmicos; documentos internos das empresas; relatos de pais, professores e jovens
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 9 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 6 citam referência não baixada/inacessível.

- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-5` — Referencia(s) citada(s) ['aa9f824adc4e7460'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-21` — Referencia(s) citada(s) ['a01a9ef18e2cd9a8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-22` — Referencia(s) citada(s) ['a01a9ef18e2cd9a8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-23` — Referencia(s) citada(s) ['a01a9ef18e2cd9a8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-25` — Referencia(s) citada(s) ['b7c2f6f663009003'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-26` — Referencia(s) citada(s) ['b7c2f6f663009003'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-28` — Referencia(s) citada(s) ['b7c2f6f663009003'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-41` — Referencia(s) citada(s) ['e94f5a1b98d6b83f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-43` — Referencia(s) citada(s) ['e94f5a1b98d6b83f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-44` — Referencia(s) citada(s) ['e94f5a1b98d6b83f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-61` — Referencia(s) citada(s) ['ae14b8fd77c76408'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-62` — Referencia(s) citada(s) ['ae14b8fd77c76408'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-66` — Referencia(s) citada(s) ['aa9f824adc4e7460'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-67` — Referencia(s) citada(s) ['a01a9ef18e2cd9a8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `rede_social_saude_mental_adolecentes_9804366fa533_20261101T204310Z-75` — Referencia(s) citada(s) ['b7c2f6f663009003'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.