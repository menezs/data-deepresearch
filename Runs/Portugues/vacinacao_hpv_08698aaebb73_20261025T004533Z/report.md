# Relatório de Auditoria — ChatGPT (vacinacao_hpv_08698aaebb73_20261025T004533Z)

**Arquivo auditado:** `answers/ChatGPT/Consolidado/vacinacao_hpv.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | vacinacao_hpv_08698aaebb73_20261025T004533Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T10:36:35.992546+00:00 |
| **Total de trechos citados** | 114 |
| **Tempo de processamento** | 10:05:14:26 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 36.7 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 177 marcadores, 27 distintos |
| Referências listadas | 27 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 59 | 51.8% |
| **UNSUPPORTED** | 39 | 34.2% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 16 | 14.0% |
| **TOTAL** | 114 | 100.0% |

Sobre os 98 trechos citados auditados: SUPPORTED 60,20%, UNSUPPORTED 39,79%, CONTRADICTED 0,00%.

> **28 dos 59 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 28 estão **contados dentro** dos 59 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`45` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `7` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `6` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `11` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#4` Elas são profiláticas: impedem novas infecções, mas não eliminam infecção por HPV ou lesões que já estejam estabelecida… | [5] | [7] [3] [18] [12] [1] [4] [25] [6] [2] | — |
| `#15` O desenvolvimento das vacinas contra HPV mudou a prevenção do câncer do colo do útero de uma estratégia historicamente… | [23] [25] | [2] [1] [18] [7] [4] [12] [20] [5] [24] | — |
| `#17` A geração quadrivalente acrescentou HPV6 e HPV11 aos oncogênicos 16 e 18 e tornou possível prevenir simultaneamente gra… | [10] | [2] [11] [18] [1] [26] [13] [3] [8] | — |
| `#20` A quadrivalente contém VLPs de HPV6, 11, 16 e 18. | [10] | [18] [11] [1] [15] [2] [26] [13] [3] [6] | — |
| `#22` O fato de serem VLPs é fundamental para seu perfil biológico: a estrutura externa imita o capsídeo viral e é reconhecid… | [6] [7] | [18] [1] [26] [12] [25] [20] | — |
| `#24` Como a vacina age antes do estabelecimento da infecção persistente, sua eficácia é maximizada quando administrada antes… | [4] [5] | [18] [1] [7] [24] [25] [3] [20] | — |
| `#34` Para pessoas imunocomprometidas, incluindo pessoas vivendo com HIV, a OMS recomenda pelo menos duas doses e, quando pos… | [4] | [3] [1] [19] [5] [24] [25] [27] [18] [21] | — |
| `#47` Quanto à segurança, as reações mais frequentes são locais — dor, edema ou eritema no local da aplicação — acompanhadas… | [5] | [3] [6] [12] [7] [1] [15] | — |
| `#80` O painel oficial do Ministério da Saúde permite acompanhar por coorte, sexo e território a cobertura contra HPV e evide… | [20] | [2] [19] [18] [1] [12] [26] [5] [24] | — |
| `#89` A prorrogação brasileira para não vacinados de 15–19 anos até dezembro de 2026 é, assim, uma janela operacional importa… | [2] | [1] [19] [27] [21] [18] [3] | — |
| `#107` A diferença persistente entre meninos e meninas justifica ações explicitamente dirigidas ao sexo masculino, incluindo c… | [19] [25] [27] | [18] [1] [20] [3] [12] [2] [24] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1698369 |
| **Média de tokens por requisição** | 17330.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/27 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2024/nota-tecnica-no-41-2024-cgici-dpni-svsa-ms) | downloaded | 21 | 10 | 6 | 3 | 2 |
| [[5]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | downloaded | 18 | 6 | 8 | 4 | 0 |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/42309117/) | downloaded | 12 | 4 | 3 | 0 | 5 |
| [[6]](https://www.ema.europa.eu/en/medicines/human/EPAR/gardasil-9) | downloaded | 11 | 2 | 6 | 3 | 0 |
| [[4]](https://www.who.int/publications/i/item/who-wer9750-645-672) | downloaded | 9 | 0 | 0 | 9 | 0 |
| [[16]](https://www.bmj.com/content/392/bmj-2025-087326) | blocked | 9 | 0 | 0 | 0 | 9 |
| [[23]](https://www.who.int/initiatives/cervical-cancer-elimination-initiative) | downloaded | 9 | 4 | 3 | 2 | 0 |
| [[3]](https://familia.sbim.org.br/vacinas/vacinas-disponiveis/vacina-hpv4) | downloaded | 8 | 5 | 1 | 2 | 0 |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/29740819/) | downloaded | 8 | 2 | 3 | 0 | 3 |
| [[14]](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2819%2930298-3/abstract) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[18]](https://www.nature.com/articles/s41541-026-01495-9) | downloaded | 8 | 3 | 3 | 1 | 1 |
| [[7]](https://www.ema.europa.eu/en/medicines/human/EPAR/cervarix) | downloaded | 7 | 2 | 5 | 0 | 0 |
| [[10]](https://pubmed.ncbi.nlm.nih.gov/17494925/) | downloaded | 6 | 2 | 4 | 0 | 0 |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/25693011/) | downloaded | 6 | 2 | 4 | 0 | 0 |
| [[25]](https://www.who.int/news-room/fact-sheets/detail/human-papilloma-virus-and-cancer) | downloaded | 6 | 1 | 3 | 1 | 1 |
| [[2]](https://www.gov.br/mulheres/pt-br/central-de-conteudos/noticias/2026/defeso-eleitoral/vacinacao-contra-o-hpv-para-jovens-de-15-a-19-anos-e-prorrogada-ate-dezembro) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[19]](https://www.unasus.gov.br/noticia/brasil-avanca-na-vacinacao-contra-hpv-e-supera-media-global) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[27]](https://www1.folha.uol.com.br/equilibrioesaude/2026/09/desigualdade-na-cobertura-vacinal-contra-hpv-deixa-jovens-desprotegidos.shtml) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[8]](https://pubmed.ncbi.nlm.nih.gov/15541448/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[24]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[26]](https://link.springer.com/article/10.1186/1471-2334-12-250) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[12]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://www.cdc.gov/hpv/vaccines/index.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[20]](https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_HPV/SEIDIGI_DEMAS_VACINACAO_HPV.html) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[21]](https://www.who.int/teams/immunization-vaccines-and-biologicals/Immunization-data-and-decision-making/global-monitoring/immunization-coverage/who-unicef-estimates-of-national-immunization-coverage) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[9]](https://www.thelancet.com/journals/lancet/article/PIIS0140673609612484/abstract) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[22]](https://www.reuters.com/business/healthcare-pharmaceuticals/global-childhood-vaccination-shows-slight-improvement-challenges-remain-2025-07-15/) | inaccessible | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/notas-tecnicas/2024/nota-tecnica-no-41-2024-cgici-dpni-svsa-ms) | #10, #13, #35–37, #82, #94, #97, #105, #113 | #14, #84, #93, #96, #106, #112 | #32, #46, #104, #87, #95 (pulado) | `#10` 2.5. A vacina HPV quadrivalente incorporada em 2014 no Calendário Nacional de Vacinações do Brasil |
| [[5]](https://www.cdc.gov/hpv/hcp/vaccination-considerations/index.html) | #41–43, #51–52, #74 | #24–25, #47–48, #60, #88, #103–104 | #4, #32, #53, #110 | `#41` CDC recommends HPV vaccine for children 11 or 12 years old to protect against HPV infections that can cause some cancers later in life. HPV vaccination can be… |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/42309117/) | #8, #68–70 | #9, #67, #71 | #7, #72, #85, #99, #111 (pulado) | `#8` In women aged 20-24 years between 2020 and 2024, in whom vaccination coverage was around 88-90% at age 12-13 years, no deaths occurred, compared with 23·1 expe… |
| [[6]](https://www.ema.europa.eu/en/medicines/human/EPAR/gardasil-9) | #2, #21 | #3, #18, #22, #31, #44–45 | #23, #32, #101 | `#2` Gardasil vaccine (a previously approved vaccine which protects against types 6, 11, 16 and 18). HPV types 6 and 11 cause most of genital warts. A further 5 HPV… |
| [[4]](https://www.who.int/publications/i/item/who-wer9750-645-672) | — | — | #24, #32–34, #93–94, #96–98 | — |
| [[23]](https://www.who.int/initiatives/cervical-cancer-elimination-initiative) | #73–74, #108–109 | #15, #110, #113 | #14, #112 | `#73` To eliminate cervical cancer, all countries must reach and maintain an incidence rate of below 4 per 100 000 women. Achieving that goal rests on three key pill… |
| [[3]](https://familia.sbim.org.br/vacinas/vacinas-disponiveis/vacina-hpv4) | #12, #39–40, #97, #105 | #46 | #98, #112 | `#12` Pessoas de 9 a 45 anos com as seguintes condições: Com HIV/Aids; Transplantados; Pacientes oncológicos em tratamento com radioterapia ou quimioterapia; Com imu… |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/29740819/) | #50, #59 | #53, #60, #88 | #7, #72, #111 (pulado) | `#50` The risk of serious adverse events is similar between control and HPV vaccines in women of all ages (669 versus 656/10,000, RR 0.98 (0.92 to 1.05), high certai… |
| [[18]](https://www.nature.com/articles/s41541-026-01495-9) | #64, #66, #102 | #13, #65, #101 | #100, #99 (pulado) | `#64` We evaluated the impact of quadrivalent HPV vaccination in Brazil using data from two repeated population-based cross-sectional surveys conducted in 2016–2017… |
| [[7]](https://www.ema.europa.eu/en/medicines/human/EPAR/cervarix) | #2, #19 | #3, #22–23, #44–45 | — | `#2` Cervarix is a vaccine. It is a suspension for injection that contains purified proteins for two types of the human papillomavirus (types 16 and 18). HPV types… |
| [[10]](https://pubmed.ncbi.nlm.nih.gov/17494925/) | #28–29 | #5–6, #17, #20 | — | `#28` we assigned 12,167 women between the ages of 15 and 26 years to receive three doses of either HPV-6/11/16/18 vaccine or placebo, administered at day 1, month 2… |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/25693011/) | #2, #30 | #5–6, #18, #31 | — | `#2` The investigational 9-valent viruslike particle vaccine against human papillomavirus (HPV) includes the HPV types in the quadrivalent HPV (qHPV) vaccine (6, 11… |
| [[25]](https://www.who.int/news-room/fact-sheets/detail/human-papilloma-virus-and-cancer) | #74 | #0, #15, #107 | #14, #86 (pulado) | `#74` Prophylactic vaccination against HPV can prevent these cancers. In addition, HPV-screening and treatment of pre-cancer lesions is an effective way to prevent c… |
| [[2]](https://www.gov.br/mulheres/pt-br/central-de-conteudos/noticias/2026/defeso-eleitoral/vacinacao-contra-o-hpv-para-jovens-de-15-a-19-anos-e-prorrogada-ate-dezembro) | #11, #38 | #89, #113 | — | `#11` Jovens e adolescentes de 15 a 19 anos que ainda não foram vacinados contra o papilomavírus humano (HPV) poderão receber gratuitamente uma dose do imunizante pe… |
| [[19]](https://www.unasus.gov.br/noticia/brasil-avanca-na-vacinacao-contra-hpv-e-supera-media-global) | #78 | #13, #81, #107 | — | `#78` Desde 2023, o país tem registrado avanços na vacinação, revertendo a tendência de queda nas coberturas vacinais em 15 das 16 vacinas ofertadas ao público infan… |
| [[27]](https://www1.folha.uol.com.br/equilibrioesaude/2026/09/desigualdade-na-cobertura-vacinal-contra-hpv-deixa-jovens-desprotegidos.shtml) | — | #79, #83, #107 | #81 | `#79` O país está próximo do objetivo entre o público feminino (86,22% de adesão entre meninas de 9 a 14 anos em 2025), mas o índice cai para meninos da mesma faixa… |
| [[8]](https://pubmed.ncbi.nlm.nih.gov/15541448/) | #26 | #5, #16 | — | `#26` In the according-to-protocol analyses, vaccine efficacy was 91.6% (95% CI 64.5-98.0) against incident infection and 100% against persistent infection (47.0-100… |
| [[24]](https://www.who.int/news-room/fact-sheets/detail/cervical-cancer) | #1, #109 | #0 | — | `#1` Cervical cancer is the fifth most commonly diagnosed cancer in women globally with around 604 000 new cases and around 280 000 deaths in 2024. The highest rate… |
| [[26]](https://link.springer.com/article/10.1186/1471-2334-12-250) | #91–92 | #90 | — | `#91` The incremental cost-effectiveness ratio (ICER) for routine vaccination of 12-year-old girls' strategy compared to no vaccination strategy was R$350 per QALY g… |
| [[12]](https://www.who.int/groups/global-advisory-committee-on-vaccine-safety/topics/human-papillomavirus-vaccines/safety) | #49, #53 | — | — | `#49` The risk of anaphylaxis has been characterized as approximately 1.7 cases per million doses, and syncope was established as a common anxiety or stress-related… |
| [[15]](https://www.cdc.gov/hpv/vaccines/index.html) | #57–58 | — | — | `#57` Among teen girls, infections with HPV types that cause most HPV cancers and genital warts have **dropped 88%** . Among young adult women, infections with HPV t… |
| [[20]](https://infoms.saude.gov.br/extensions/SEIDIGI_DEMAS_VACINACAO_HPV/SEIDIGI_DEMAS_VACINACAO_HPV.html) | — | #80 | #106 | `#80` a vacinação contra HPV é indica para ambos sexos e nas faixas etárias entre 09 a 14 anos de idade, a meta de Cobertura Vacinal é de 90% para cada sexo. |
| [[21]](https://www.who.int/teams/immunization-vaccines-and-biologicals/Immunization-data-and-decision-making/global-monitoring/immunization-coverage/who-unicef-estimates-of-national-immunization-coverage) | — | #76 | #75 | `#76` WHO and UNICEF have reviewed data available on national immunization coverage and made country-specific estimates of immunization coverage. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.reuters.com/business/healthcare-pharmaceuticals/global-childhood-vaccination-shows-slight-improvement-challenges-remain-2025-07-15/ — HTTP 401 em https://www.reuters.com/business/healthcare-pharmaceuticals/global-childhood-vaccination-shows-slight-improvement-challenges-remain-2025-07-15/

### Bloqueadas por barreira de acesso

- https://www.thelancet.com/journals/lancet/article/PIIS0140673609612484/abstract — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.thelancet.com/journals/lancet/article/PIIS0140-6736%2819%2930298-3/abstract — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.bmj.com/content/392/bmj-2025-087326 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-0`** [24] [25]
  - Trecho: A vacinação contra o papilomavírus humano (HPV) constitui uma das intervenções de prevenção primária do câncer com evidência mais consistente disponível atualmente: a infecção persistente por tipos oncogênicos de HPV é…
  - Justificativa: A evidência sustenta explicitamente que a infecção persistente por tipos oncogênicos de HPV é a causa de praticamente todos os cânceres do colo do útero ('Almost all cases' e 'about 95%'), e que está associada a câncere…
  - Suporte veio de: [25] [24]
  - Evidência: “Persistent HPV infection with high-risk HPV types is the cause of cervical cancer and is associated with cancers of the vulva, vagina, mouth/throat, penis and anus”
  - Não coberto pela evidência: A caracterização da vacinação como 'uma das intervenções de prevenção primária do câncer com evidência mais consistente disponível atualmente' — a evidência afirma eficácia e importância, mas não a classifica explicitamente como tendo a 'evidência mais consistente'.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [25] | parcial | Persistent HPV infection with high-risk HPV types is the cause of cervical cancer and is associated with cancers of the… |
    | [24] | parcial | Almost all cases of cervical cancer are caused by infection with oncogenic types of human papillomavirus (HPV).; Persis… |

- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-1`** [24]
  - Trecho: Em 2024, estimaram-se aproximadamente 604 mil novos casos de câncer cervical e cerca de 280 mil mortes no mundo, com carga desproporcional em populações que têm menor acesso à vacinação, ao rastreamento e ao tratamento.
  - Justificativa: A evidência confirma explicitamente os números de 604 mil novos casos e 280 mil mortes em 2024, e também sustenta a afirmação de carga desproporcional em populações com menor acesso à vacinação, rastreamento e tratament…
  - Suporte veio de: [24]
  - Evidência: “Cervical cancer is the fifth most commonly diagnosed cancer in women globally with around 604 000 new cases and around 280 000 deaths in 2024.”
- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-3`** [6] [7]
  - Trecho: Todas utilizam partículas semelhantes ao vírus, ou *virus-like particles* (VLPs), formadas pela proteína L1 do capsídeo, capazes de induzir títulos elevados de anticorpos neutralizantes sem causar infecção, porque não c…
  - Justificativa: A evidência confirma explicitamente que ambas as vacinas (Gardasil 9 e Cervarix) utilizam VLPs formadas pela proteína L1 do capsídeo, que induzem produção de anticorpos e não causam infecção (explicitamente afirmado par…
  - Suporte veio de: [6] [7]
  - Evidência: “All papillomaviruses have a shell, or 'capsid', that is made up of proteins called 'L1 proteins'. Gardasil 9 contains the purified L1 proteins for the nine HPV types above, produced by a method known as 'recombinant DNA…”
  - Não coberto pela evidência: O termo específico 'anticorpos neutralizantes' não é usado na evidência (apenas 'antibodies' e 'protective antibodies'); 'Todas' (todas as vacinas contra HPV) — a evidência cobre apenas Gardasil 9 e Cervarix, não necessariamente todas as vacinas HPV existentes; Para Cervarix, a evidência não afirma explicitamente que as VLPs 'não contêm vírus HPV infeccioso' ou que 'não causam infecção' (apenas Gardasil 9 tem essa afirmação explícita)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] | parcial | All papillomaviruses have a shell, or 'capsid', that is made up of proteins called 'L1 proteins'. Gardasil 9 contains t… |
    | [7] | parcial | All papillomaviruses have a shell or 'capsid', which is made up of distinctive proteins called 'L1 proteins'. Cervarix… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta parcialmente a afirmacao: confirma que VLPs sao formadas por proteínas L1 do capsídeo, que nao causam infecao, e que i…") — cascata: baseline → context_expansion
### UNSUPPORTED

- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-4`** [5]
  - Trecho: Elas são profiláticas: impedem novas infecções, mas não eliminam infecção por HPV ou lesões que já estejam estabelecidas.
  - Justificativa: A evidência não afirma explicitamente que as vacinas contra HPV são profiláticas nem que não eliminam infecções ou lesões já estabelecidas. O trecho mais próximo menciona que a vacinação 'provides less benefit' para pes…
  - Não coberto pela evidência: Afirmação de que as vacinas são 'profiláticas'; Afirmação de que 'impedem novas infecções'; Afirmação de que 'não eliminam infecção por HPV já estabelecida'
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [7] [3] [18] [12] [1] [4] [25] [6] [2] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-14`** [1] [23] [25]
  - Trecho: A vacinação em escolas, sistemas ativos de busca e resgate, recomendação inequívoca por profissionais de saúde, inclusão de meninos, esquemas simplificados e integração com rastreamento cervical são complementares, e nã…
  - Justificativa: A evidência menciona individualmente várias das estratégias listadas (vacinação em escolas, estratégia de resgate, inclusão de meninos, esquema de dose única, rastreamento cervical), mas em nenhum momento as caracteriza…
  - Suporte veio de: [1]
  - Não coberto pela evidência: Caracterização explícita das estratégias como 'complementares, e não estratégias concorrentes'; Recomendação inequívoca por profissionais de saúde (a evidência trata de recomendações de comitês técnicos, não de profissionais de saúde individualmente)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | promover a vacinação nas escolas também é fundamental para se alcançar altas coberturas, essencial para o impacto da do… |
    | [23] | ausente | — |
    | [25] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `vacinacao_hpv_08698aaebb73_20261025T004533Z-15`** [23] [25]
  - Trecho: O desenvolvimento das vacinas contra HPV mudou a prevenção do câncer do colo do útero de uma estratégia historicamente concentrada em detectar lesões precursoras para uma combinação de prevenção primária por vacinação e…
  - Justificativa: A evidência sustenta que a prevenção do câncer do colo do útero combina vacinação (prevenção primária) e rastreamento (prevenção secundária), conforme descrito na estratégia da WHO e nas recomendações de prevenção. No e…
  - Suporte veio de: [25] [23]
  - Evidência: “Prophylactic vaccination against HPV can prevent these cancers. In addition, HPV-screening and treatment of pre-cancer lesions is an effective way to prevent cervical cancer.”
  - Não coberto pela evidência: A afirmação de que a prevenção era 'historicamente concentrada em detectar lesões precursoras' antes do desenvolvimento das vacinas — a evidência não descreve o panorama histórico anterior às vacinas.; A noção de 'mudança' ou transição histórica de uma estratégia para outra — a evidência descreve apenas a combinação atual de vacinação e rastreamento, sem narrativa de mudança temporal.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [23] | parcial | vaccination: 90% of girls fully vaccinated with the HPV vaccine by the age of 15; - screening: 70% of women screened us… |
    | [25] | parcial | Prophylactic vaccination against HPV can prevent these cancers. In addition, HPV-screening and treatment of pre-cancer… |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [2] [1] [18] [7] [4] [12] [20] [5] [24] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 8 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 7 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 1 citam referência não baixada/inacessível.

- `vacinacao_hpv_08698aaebb73_20261025T004533Z-27` — Referencia(s) citada(s) ['2a7eef803e191135'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-54` — Referencia(s) citada(s) ['6a61d81ecad4bd07'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-55` — Referencia(s) citada(s) ['6a61d81ecad4bd07'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-56` — Referencia(s) citada(s) ['6a61d81ecad4bd07'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-61` — Referencia(s) citada(s) ['7fb33d32d199e38f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-62` — Referencia(s) citada(s) ['7fb33d32d199e38f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-63` — Referencia(s) citada(s) ['7fb33d32d199e38f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-77` — Referencia(s) citada(s) ['955f4abb4d4e7fb4'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-86` — Parte das fontes citadas sem conteudo: referencia(s) ['6a61d81ecad4bd07'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-87` — Parte das fontes citadas sem conteudo: referencia(s) ['6a61d81ecad4bd07'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-95` — Parte das fontes citadas sem conteudo: referencia(s) ['7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-7` — Parte das fontes citadas sem conteudo: referencia(s) ['6a61d81ecad4bd07', '7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-72` — Parte das fontes citadas sem conteudo: referencia(s) ['6a61d81ecad4bd07', '7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-85` — Parte das fontes citadas sem conteudo: referencia(s) ['7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-99` — Parte das fontes citadas sem conteudo: referencia(s) ['7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `vacinacao_hpv_08698aaebb73_20261025T004533Z-111` — Parte das fontes citadas sem conteudo: referencia(s) ['6a61d81ecad4bd07', '7fb33d32d199e38f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.