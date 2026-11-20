# Relatório de Auditoria — ChatGPT (rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/EmConsolidacao/rede_social_saude_mental_adolecentes.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T00:28:54.623932+00:00 |
| **Total de trechos citados** | 105 |
| **Tempo de processamento** | 2:17:29:13 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 30.0 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 190 marcadores, 21 distintos |
| Referências listadas | 22 (1 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 66 | 62.9% |
| **UNSUPPORTED** | 29 | 27.6% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 10 | 9.5% |
| **TOTAL** | 105 | 100.0% |

Sobre os 95 trechos citados auditados: SUPPORTED 69,47%, UNSUPPORTED 30,52%, CONTRADICTED 0,00%.

> **26 dos 66 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 26 estão **contados dentro** dos 66 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`36` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `12` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `7` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `14` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#14` High frequency of use should not be equated with disordered or problematic use. | [5] [11] | [7] [4] [19] [3] [8] [12] | — |
| `#17` Problematic use generally refers to impaired control and interference with ordinary functioning rather than simply spen… | [2] [11] | [16] [4] [19] [7] [8] [21] [9] | — |
| `#24` The clearest potential benefit is social connection. | [14] [15] [16] | [3] [9] | — |
| `#40` Cyberbullying represents a more clearly harmful form of online experience than social-media exposure in the abstract. | [13] | [16] [3] [4] [8] [18] [14] [15] | — |
| `#49` Even longitudinal studies may be confounded if they measure exposure poorly or fail to capture relevant changes in the… | [5] [6] | [18] [9] [3] [7] [8] [19] [16] [4] | — |
| `#65` The most defensible interpretation is that gender differences may emerge through exposure to particular content, social… | [4] [12] [16] | [19] [9] [8] [18] [15] [3] | — |
| `#70` Measurement is one of the field’s central weaknesses. | [5] [6] [11] | [4] [7] [9] [18] [8] [19] [15] | — |
| `#73` Heterogeneity across studies is substantial. | [5] [11] | [18] [9] [3] [15] [19] [8] | — |
| `#74` Studies differ in platform definitions, age ranges, mental-health measures, follow-up intervals, socioeconomic settings… | [5] [11] | [8] [9] [16] [4] [15] [18] [7] [19] | — |
| `#79` Platform change creates another research problem because algorithms, norms, features, and dominant services evolve fast… | [4] | [15] [16] [8] [19] [9] | — |
| `#90` Schools therefore have stronger grounds for combining reasonable device rules with cyberbullying prevention, digital li… | [13] [18] [19] | [3] [16] | — |
| `#92` Assessment can usefully cover cyberbullying, compulsive or uncontrolled use, sleep disruption, appearance comparison, e… | [4] [10] [12] [13] [15] | [14] [16] [8] [7] [18] [3] [9] | — |
| `#102` Average time spent on social media shows only small associations with depression and anxiety, while problematic use, cy… | [5] [11] [12] [13] | [19] [8] [7] [16] [9] [4] [3] | — |
| `#103` Conversely, friendship, identity development, social support, creativity, and access to communities can be meaningful b… | [14] [15] [17] | [16] [4] [8] [3] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1625997 |
| **Média de tokens por requisição** | 17115.8 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 1/22 (4.5%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[4]](https://www.nationalacademies.org/read/27396/chapter/2) | downloaded | 35 | 10 | 19 | 6 | 0 |
| [[16]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use) | downloaded | 27 | 13 | 13 | 1 | 0 |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/41589024/) | downloaded | 16 | 3 | 6 | 7 | 0 |
| [[6]](https://onlinelibrary.wiley.com/doi/10.1111/bjc.70100) | blocked | 13 | 0 | 0 | 0 | 13 |
| [[11]](https://doi.org/10.1016/j.jad.2024.08.193) | blocked | 13 | 0 | 0 | 0 | 13 |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/39721448/) | downloaded | 11 | 3 | 4 | 4 | 0 |
| [[17]](https://www.pewresearch.org/internet/2025/04/22/teens-social-media-and-mental-health/) | downloaded | 11 | 9 | 2 | 0 | 0 |
| [[15]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9536523/) | downloaded | 9 | 2 | 6 | 1 | 0 |
| [[10]](https://jamanetwork.com/journals/jamapediatrics/fullarticle/2819781) | downloaded | 8 | 5 | 1 | 2 | 0 |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/39828926/) | downloaded | 8 | 1 | 1 | 6 | 0 |
| [[2]](https://www.who.int/europe/publications/i/item/9789289061322) | downloaded | 6 | 0 | 2 | 4 | 0 |
| [[1]](https://www.pewresearch.org/internet/2024/12/12/teens-social-media-and-technology-2024/) | downloaded | 5 | 4 | 1 | 0 | 0 |
| [[8]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13256062/) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[22]](https://www.unicef.org/documents/drawing-line-digital-spaces) | downloaded | 5 | 0 | 1 | 4 | 0 |
| [[7]](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2834349/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/35390193/) | downloaded | 3 | 1 | 1 | 1 | 0 |
| [[18]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13714660/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[19]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11984610/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[3]](https://www.cdc.gov/mmwr/volumes/73/su/su7304a3.htm) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[9]](https://www.nature.com/articles/s41467-022-29296-3) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[20]](https://acamh.onlinelibrary.wiley.com/doi/10.1111/camh.70118) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[21]](https://www.hhs.gov/surgeongeneral/reports-and-publications/youth-mental-health/social-media/index.html) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[4]](https://www.nationalacademies.org/read/27396/chapter/2) | #3–4, #7, #31, #44, #47–48, #53, #72, #104 | #0–2, #8–9, #30, #35, #39, #45–46, #80, #85, #92, #95–98, #100–101 | #43, #65, #69, #71, #79, #82 | `#3` The committee's review of the literature did not support the conclusion that social media causes changes in adolescent health at the population level. [...] Th… |
| [[16]](https://www.apa.org/topics/social-media-internet/health-advisory-adolescent-social-media-use) | #8, #26, #46–47, #68, #81–83, #85, #91, #93, #97, #104 | #1–2, #7, #9, #24, #30, #48, #65–66, #80, #84, #86, #96 | #76 | `#8` the effects of social media likely depend on what teens can do and see online, teens' preexisting strengths or vulnerabilities, and the contexts in which they… |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/41589024/) | #3, #5, #75 | #7, #14, #45, #83, #101–102 | #49, #70, #72–74, #91, #93 | `#3` general SMU showed weak and inconsistent associations with both well-being and ill-being, while problematic SMU was consistently linked to ill-being. |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/39721448/) | #36–38 | #39, #63, #97, #102 | #62, #65, #85, #92 | `#36` Results from 83 studies with 55,440 participants indicated that the weighted average correlation between higher online social comparison and greater body image… |
| [[17]](https://www.pewresearch.org/internet/2025/04/22/teens-social-media-and-mental-health/) | #18–23, #28–29, #62 | #63, #103 | — | `#18` Teens' views of the benefits and harms of social media vary by which aspect of their lives you ask about. |
| [[15]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9536523/) | #26–27 | #24, #68, #81, #86, #92, #103 | #66 | `#26` LGBTQ youths also resorted to social media to connect with the LGBTQ community when there was a lack of offline opportunities [34,54]. Social media was a vital… |
| [[10]](https://jamanetwork.com/journals/jamapediatrics/fullarticle/2819781) | #64, #67, #69, #81, #91 | #66 | #92, #94 | `#64` There was also no moderation for the type of social media measures (Table), age, or sex (eAppendix 14 in Supplement 1). |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/39828926/) | #41 | #100 | #40, #43, #90, #92, #94, #102 | `#41` yielding a sample of 27 studies encompassing 13,497 children and adolescents aged 8 to 19 years old. The longitudinal association between cyberbullying victimi… |
| [[2]](https://www.who.int/europe/publications/i/item/9789289061322) | — | #10, #15 | #16–17, #62–63 | `#10` This report, Volume 6 in the series, focuses on adolescent social media use and gaming, using the unique HBSC evidence on adolescents aged 11, 13 and 15 years… |
| [[1]](https://www.pewresearch.org/internet/2024/12/12/teens-social-media-and-technology-2024/) | #11–13, #62 | #10 | — | `#11` The Center conducted an online survey of 1,391 U.S. teens from Sept. 18 to Oct. 10, 2024, through Ipsos. [...] The survey was weighted to be representative of… |
| [[8]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13256062/) | #54, #56–58, #60 | — | — | `#54` more than 2 h of SMU per day was associated with a small increased risk for high depressive symptoms in adolescents 1 year later |
| [[22]](https://www.unicef.org/documents/drawing-line-digital-spaces) | — | #99 | #9, #98, #100, #104 | `#99` age-based restrictions emerging as one potential component of a robust approach to protecting children online |
| [[7]](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2834349/) | #54–55, #57 | — | — | `#54` we found that there was a longitudinal association between increases in social media use and subsequent depressive symptoms at the within-person level. These f… |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/35390193/) | #25 | #103 | #24 | `#25` Meta-analysis showed that the correlation of online social support with self-esteem was moderate and significant (r = .29), but with depression was small and i… |
| [[18]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13714660/) | #87–88 | #90 | — | `#87` our findings suggested that phone bans alone may be insufficient to produce population-level improvements in adolescent well-being. Future research should exam… |
| [[19]](https://pmc.ncbi.nlm.nih.gov/articles/PMC11984610/) | #87, #89 | #90 | — | `#87` school policies should be developed as part a more holistic approach. Preventative efforts should also consider how other behaviours that influence mental heal… |
| [[3]](https://www.cdc.gov/mmwr/volumes/73/su/su7304a3.htm) | #42 | — | #94 | `#42` Frequent social media use was associated with a higher prevalence of bullying victimization at school and electronically, persistent feelings of sadness or hop… |
| [[9]](https://www.nature.com/articles/s41467-022-29296-3) | #58–59 | — | — | `#58` provides evidence for the hypothesis that the impact of social media on individuals varies depending on how old they are, as well as their sex |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://onlinelibrary.wiley.com/doi/10.1111/bjc.70100 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://doi.org/10.1016/j.jad.2024.08.193 — http_error — barreira de acesso (http_error): # There was a problem providing the content you requested Please contact our support team for more information and provi
- https://acamh.onlinelibrary.wiley.com/doi/10.1111/camh.70118 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-1`** [4] [16]
  - Trecho: Social media is treated broadly as digitally mediated interaction involving user-generated content, social networking, video sharing, messaging, algorithmically curated feeds, and related interactive functions, rather t…
  - Justificativa: A evidência define redes sociais de forma ampla como tecnologias interativas que facilitam criação e compartilhamento de informação, incluindo redes sociais, compartilhamento de vídeos, blogs, mundos virtuais e jogos, c…
  - Suporte veio de: [4] [16]
  - Evidência: “Social media refers to "interactive technologies that facilitate the creation and sharing of information, ideas, interests, and other forms of expression through virtual communities and networks." Social media can there…”
  - Não coberto pela evidência: O termo 'messaging' não é explicitamente listado como componente das redes sociais na evidência; O termo 'user-generated content' não aparece literalmente; a evidência fala em 'creation and sharing of information'; Os termos 'smartphones' e 'total screen time' não aparecem explicitamente na evidência, embora a distinção entre redes sociais e uso geral de tecnologia esteja presente
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | parcial | Social media refers to "interactive technologies that facilitate the creation and sharing of information, ideas, intere… |
    | [16] | parcial | These recommendations do not address the use of all technology among youth, including educationally-based platforms or… |

- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-2`** [4] [16]
  - Trecho: This distinction matters because platforms differ in features, audiences, recommendation systems, visibility of popularity metrics, modes of communication, and opportunities for public comparison or private support.
  - Justificativa: A evidência sustenta a maior parte da afirmação: plataformas variam em features/audiências/design, usam algoritmos de recomendação, possuem métricas de popularidade visíveis (likes, retweets), oferecem oportunidades par…
  - Suporte veio de: [4] [16]
  - Evidência: “Social media include a broad range of features that facilitate social interaction online; platforms vary widely in their target audiences, purposes, and design.”
  - Não coberto pela evidência: A expressão exata 'modes of communication' não aparece literalmente na evidência, embora se possa inferir a partir da descrição de diferentes modalidades de interação social.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | parcial | Social media include a broad range of features that facilitate social interaction online; platforms vary widely in thei… |
    | [16] | parcial | Youth using social media should be encouraged to use functions that create opportunities for social support, online com… |

- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-3`** [4] [5] [6]
  - Trecho: The best current evidence does **not** support either of two simple claims: that social media is harmless for adolescents, or that social media use as a whole is a large, uniform cause of adolescent mental illness.
  - Justificativa: A evidência sustenta ambas as partes da afirmação: (1) que as redes sociais não são inofensivas para adolescentes — há danos associados a alguns adolescentes e uso problemático está consistentemente ligado a mal-estar;…
  - Suporte veio de: [4] [5]
  - Evidência: “The committee's review of the literature did not support the conclusion that social media causes changes in adolescent health at the population level.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | sustenta | The committee's review of the literature did not support the conclusion that social media causes changes in adolescent… |
    | [5] | sustenta | general SMU showed weak and inconsistent associations with both well-being and ill-being, while problematic SMU was con… |

### UNSUPPORTED

- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-0`** [4] [6]
  - Trecho: This report examines social media use in roughly the second decade of life, with particular attention to ages 10–19 while drawing selectively on studies extending into the early twenties when they illuminate development…
  - Justificativa: A evidência menciona que o comitê adotou uma visão ampla de adolescência e pré-adolescência com um corte transicional em torno dos 18 anos, mas não especifica as idades 10–19, nem a 'segunda década de vida', nem o uso s…
  - Suporte veio de: [4]
  - Evidência: “The sponsors gave the committee some leeway in its interpretation of the report's target age range. Recognizing that experiences in adolescence are influenced by those earlier in childhood, the committee took a broad vi…”
  - Não coberto pela evidência: idades específicas 10–19; segunda década de vida; uso seletivo de estudos que se estendem até o início dos vinte anos
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | parcial | the committee took a broad view of adolescence and late childhood with a transitional cutoff around age 18. |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-14`** [5] [11]
  - Trecho: High frequency of use should not be equated with disordered or problematic use.
  - Justificativa: A evidência distingue entre 'general SMU' e 'problematic SMU', mostrando associações diferentes com saúde mental, o que sugere uma separação conceitual. No entanto, em nenhum momento afirma explicitamente que alta frequ…
  - Não coberto pela evidência: A afirmação de que alta frequência de uso não deve ser equiparada a uso desordenado ou problemático
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | parcial | general SMU showed weak and inconsistent associations with both well-being and ill-being, while problematic SMU was con… |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [7] [4] [19] [3] [8] [12] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-15`** [2]
  - Trecho: The World Health Organization’s Health Behaviour in School-aged Children study, covering 11-, 13-, and 15-year-olds across 44 countries and regions in Europe, Central Asia, and Canada, reported that 11% met its criteria…
  - Justificativa: A evidência confirma a existência do estudo HBSC, sua abrangência (11, 13 e 15 anos, 44 países/regiões da Europa, Ásia Central e Canadá) e o ciclo 2021/2022, mas não menciona nenhuma estatística sobre uso problemático d…
  - Suporte veio de: [2]
  - Não coberto pela evidência: 11% met criteria for problematic social media use in 2021–2022; up from 7% in the prior 2017–2018 survey cycle
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 10 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-6` — Referencia(s) citada(s) ['882acab979a368ea'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-32` — Referencia(s) citada(s) ['43d7c483577498e0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-33` — Referencia(s) citada(s) ['43d7c483577498e0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-34` — Referencia(s) citada(s) ['43d7c483577498e0'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-50` — Referencia(s) citada(s) ['882acab979a368ea'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-51` — Referencia(s) citada(s) ['882acab979a368ea'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-52` — Referencia(s) citada(s) ['882acab979a368ea'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-61` — Referencia(s) citada(s) ['882acab979a368ea'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-77` — Referencia(s) citada(s) ['303178644d5155b8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `rede_social_saude_mental_adolecentes_38e5e33f14c6_20261115T065941Z-78` — Referencia(s) citada(s) ['303178644d5155b8'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.