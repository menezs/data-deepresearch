# Relatório de Auditoria — Gemini (regulacao_ia_87ba15eb4df4_20261102T161649Z)

**Arquivo auditado:** `answers/Gemini/Emergente/regulacao_ia.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | regulacao_ia_87ba15eb4df4_20261102T161649Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-04T05:58:57.873973+00:00 |
| **Total de trechos citados** | 175 |
| **Tempo de processamento** | 1:13:42:08 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 2955.0 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-02 16:17:11+00:00 |
| Citações no corpo | 410 marcadores, 25 distintos |
| Referências listadas | 22 (2 nunca citadas) |

> 25 números de citação distintos no corpo para apenas 22 referências listadas — há marcadores `[N]` sem entrada correspondente.

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 107 | 61.1% |
| **UNSUPPORTED** | 66 | 37.7% |
| **CONTRADICTED** | 2 | 1.1% |
| **TOTAL** | 175 | 100.0% |

Sobre os 175 trechos citados auditados: SUPPORTED 61,14%, UNSUPPORTED 37,71%, CONTRADICTED 1,14%.

> **57 dos 107 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 57 estão **contados dentro** dos 107 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`88` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `13` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `22` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `17` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 17, full_doc_scan = 5.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#21` e a identificação biométrica remota em tempo real em espaços acessíveis ao público para fins de aplicação da lei, com e… | [6] | [17] [28] [36] [21] | — |
| `#26` Incluem-se nessa classificação os sistemas aplicados a infraestruturas críticas (tráfego, abastecimento de água e energ… | [6] | [17] [21] [30] [32] [28] [36] [26] | — |
| `#27` educação e formação profissional (avaliação de estudantes e acesso a instituições) | [6] | [17] [30] [32] [34] [28] [36] | — |
| `#35` a elaboração e atualização de documentação técnica detalhada e o registro automático de eventos (logs) para garantir a… | [6] | [17] [34] [28] [36] [5] [11] [30] [32] | — |
| `#41` Os fornecedores e implantadores devem garantir que as pessoas naturais sejam claramente informadas de que estão interag… | [2] [3] [5] | [21] [17] [28] [36] [30] [32] | — |
| `#68` No Brasil, o debate sobre a regulação da inteligência artificial ganhou tração estruturada a partir do Projeto de Lei n… | [16] [18] [19] | [20] [30] [32] [28] [36] [27] [17] | — |
| `#81` O direito ao uso de linguagem simples, transparente e acessível nas interações automatizadas, com salvaguardas especiai… | [20] [21] | [17] [34] [28] [36] [27] | — |
| `#83` O direito à explicação substancial e inteligível sobre a decisão tomada pelo sistema, compreendendo os critérios, os da… | [20] [21] | [17] [27] [29] [31] [28] [36] [34] [26] | — |
| `#84` O direito à contestação das decisões automatizadas e à submissão de razões de contrariedade. | [20] [21] | [17] [27] [28] [36] [34] [29] [31] | — |
| `#90` A utilização de câmeras para identificação biométrica em tempo real é restringida a exceções penais e de segurança públ… | [20] [21] | [17] [28] [36] [30] [32] | — |
| `#123` A ANPD atuará como órgão central articulador para evitar sobreposições ou conflitos normativos entre as agências. | [34] | [28] [36] [21] [27] | — |
| `#149` Ao incorporar dispositivos que tratam especificamente do fomento à língua portuguesa e ao patrimônio cultural, de diret… | [20] [21] | [28] [36] [34] [30] [32] | — |
| `#154` Em seguida, realiza-se a Classificação de Risco e Avaliação Preliminar, avaliando a aderência de cada sistema aos nívei… | [2] [6] [17] [20] | [21] [29] [31] [27] | — |
| `#165` Embora a imposição de requisitos rigorosos aumente os custos operacionais de compliance e exija maior suporte jurídico… | [2] [5] [35] | [28] [36] [34] [30] [32] | — |
| `#170` Ao adotar a classificação de risco europeia, mas adaptar o texto à realidade nacional com um rol explícito de direitos… | [17] [20] [21] | [27] [28] [36] [30] [32] [29] [31] [34] | — |
| `#173` À medida que o AI Act alcança suas fases de plena aplicabilidade na Europa e o PL 2338/2023 avança no Congresso Naciona… | [1] [2] [5] [18] [35] | [27] [28] [36] [17] [34] | — |
| `#174` A conformidade ética e regulatória deixa de ser um mero custo burocrático e passa a figurar como elemento estratégico i… | [6] [20] [31] [35] | [34] [28] [36] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 4849757 |
| **Média de tokens por requisição** | 27712.9 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 2/22 (9.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[20]](https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara) | downloaded | 64 | 27 | 26 | 11 | 0 |
| [[6] [13]](https://reversa.ai/regulations/eu-ai-act) | downloaded | 58 | 14 | 24 | 20 | 0 |
| [[21]](https://www12.senado.leg.br/noticias/materias/2024/12/05/comissao-chega-a-consenso-e-regulamentacao-da-inteligencia-artificial-vai-a-plenario) | downloaded | 36 | 21 | 13 | 2 | 0 |
| [[2] [10]](https://www.euaiact.com/implementation-timeline) | downloaded | 35 | 15 | 6 | 14 | 0 |
| [[29] [31]](https://gedai.ufpr.br/responsabilizacao-das-plataformas-digitais-pela-violacao-de-direitos-autorais/) | downloaded | 31 | 10 | 11 | 10 | 0 |
| [[17]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | downloaded | 29 | 15 | 13 | 1 | 0 |
| [[5] [11]](https://euaicompass.com/timeline.html) | downloaded | 27 | 14 | 6 | 7 | 0 |
| [[1] [4]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) | downloaded | 22 | 13 | 6 | 3 | 0 |
| [[25] [35]](https://sciereli.com.br/blog/governanca-ia-saude-brasil/) | downloaded | 21 | 9 | 9 | 3 | 0 |
| [[9] [15]](https://artificialintelligenceact.eu/) | downloaded | 16 | 1 | 11 | 4 | 0 |
| [[3] [14]](https://artificialintelligenceact.eu/implementation-timeline/) | downloaded | 13 | 8 | 3 | 2 | 0 |
| [[34]](https://vlklaw.com.br/wp-content/uploads/2024/12/Tendencias-Direito-Digital-2025.-comprimido.pdf) | downloaded | 10 | 3 | 6 | 1 | 0 |
| [[16] [24]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf) | downloaded | 8 | 4 | 2 | 2 | 0 |
| [[18] [23]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | downloaded | 8 | 1 | 5 | 2 | 0 |
| [[19] [22]](https://www.congressonacional.leg.br/materias/materias-bicamerais/-/ver/pl-2338-2023) | downloaded | 7 | 2 | 3 | 2 | 0 |
| [[26]](https://repositorio.uel.br/bitstreams/d2237cbd-9bfb-4b9e-90d3-cd3721add89c/download) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[7] [8]](https://artificialintelligenceact.eu/the-act/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[27]](https://douglasvilar.com.br/artigos/posts/2026-06-13_marco-legal-ia-pl-2338-regulacao-brasil) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[28] [36]](https://itsrio.org/wp-content/uploads/2017/01/Livro-Inteligencia-Artificial-e-Sociedade-Conectada.pdf) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[12]](https://www.trooper.dk/en/eu-ai-act-guide/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[30] [32]](https://intic.gov.mz/wp-content/uploads/2025/05/Inteligencia_Artificial_Desafios_e_Oportunidades_assinado.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[33]](https://repositorio.ufrn.br/bitstreams/fe6b8240-cdbf-45ea-8704-7c2882b10194/download) | blocked | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[20]](https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara) | #5, #7, #69, #79–80, #82, #85–86, #91, #101–103, #105, #108, #111–113, #116–119, #124–125, #142, #146, #163, #171 | #9, #75, #77–78, #81, #83–84, #88–90, #94–95, #100, #104, #107, #110, #127–128, #130–131, #135, #149, #154, #156–157, #170 | #72–73, #76, #106, #120, #129, #148, #164, #166, #172, #174 | `#5` E esse projeto, por sua vez, surgiu a partir de um anteprojeto elaborado por uma comissão de juristas. O substitutivo também engloba dispositivos sugeridos em… |
| [[6] [13]](https://reversa.ai/regulations/eu-ai-act) | #2, #11–13, #16, #30, #32–34, #36, #44, #52–53, #56 | #3, #14–15, #26–28, #31, #35, #37–39, #46–47, #49, #54–55, #57–58, #127–128, #145, #154, #167–168 | #17–21, #29, #45, #48, #129–130, #134, #137, #144, #147, #155–157, #164, #166, #174 | `#2` The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence. Adopted in 2024 [...] Regulation (EU) 2024/1689 |
| [[21]](https://www12.senado.leg.br/noticias/materias/2024/12/05/comissao-chega-a-consenso-e-regulamentacao-da-inteligencia-artificial-vai-a-plenario) | #79–80, #82, #85, #91, #96–99, #101–102, #105, #108, #112–113, #118, #120, #124–125, #138, #142 | #77, #81, #83–84, #89–90, #100, #130–131, #139, #148–149, #170 | #73, #136 | `#79` Direito a privacidade e proteção de dados pessoais; |
| [[2] [10]](https://www.euaiact.com/implementation-timeline) | #10–11, #16, #22–25, #56–58, #60–63, #65 | #15, #40–41, #59, #131, #168 | #12, #39, #44–45, #49, #137, #145, #150–154, #165, #173 | `#10` 12 July 2024## Published in the Official Journal Regulation (EU) 2024/1689 was published, beginning the countdown to entry into force. |
| [[29] [31]](https://gedai.ufpr.br/responsabilizacao-das-plataformas-digitais-pela-violacao-de-direitos-autorais/) | #1–2, #7–8, #107, #126, #132, #141–142, #167 | #3–4, #9, #75, #127, #135, #140, #147–148, #156, #172 | #76, #103, #114, #117, #133–134, #136, #166, #174, #106 ⚡ | `#1` A jornada empreendida neste artigo, do plano ético e voluntário da soft law às iniciativas concretas de hard law na Europa e no Brasil, revela que o dilema jur… |
| [[17]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | #7, #76, #78, #80, #86–87, #91–95, #155–157, #172 | #9, #75, #77, #104, #106, #109, #127–128, #130, #135, #143, #154, #170 | #129 | `#7` Estruturalmente, a proposição estabelece uma regulação baseada em riscos e uma modelagem regulatória fundada em direitos. |
| [[5] [11]](https://euaicompass.com/timeline.html) | #11, #16, #22, #24–25, #51, #56–58, #60, #62, #64–66 | #15, #40, #59, #61, #131, #153 | #41, #48, #150–152, #165, #173 | `#11` 1 August 2024 ### EU AI Act enters into force |
| [[1] [4]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) | #11, #16, #23–24, #51, #56–58, #60–62, #64, #66 | #40, #48, #50, #55, #168, #173 | #52, #137, #164 | `#11` 01 Aug 2024Entry into force |
| [[25] [35]](https://sciereli.com.br/blog/governanca-ia-saude-brasil/) | #6–7, #86, #152, #158–159, #161–163 | #8, #122, #126, #150–151, #153, #160, #173–174 | #121, #155, #165 | `#6` O PL 2338/2023, conhecido como Marco Legal da Inteligência Artificial, foi aprovado pelo Senado em dezembro de 2024 e segue em tramitação na Câmara dos Deputad… |
| [[9] [15]](https://artificialintelligenceact.eu/) | #44 | #3, #13, #17, #28, #39, #43, #49–50, #145, #147, #167 | #14, #40, #60, #42 ⚡ | `#44` Enforcement of Chapter V under the EU AI Act; This page aims to provide an overview of the EU AI Act's enforcement provisions relating to Chapter V, namely the… |
| [[3] [14]](https://artificialintelligenceact.eu/implementation-timeline/) | #11, #51, #56, #58, #62–64, #67 | #10, #41, #55 | #48, #52 | `#11` 1 August 2024 **Application:** Date of entry into force of the AI Act. |
| [[34]](https://vlklaw.com.br/wp-content/uploads/2024/12/Tendencias-Direito-Digital-2025.-comprimido.pdf) | #121, #144, #146 | #115–116, #122–123, #139, #171 | #114 | `#121` A lógica é valorizar e reforçar as competências regulatória, sancionatória e normativa das autoridades setoriais em harmonia com as correlatas gerais da autori… |
| [[16] [24]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf) | #70–73 | #68, #169 | #5, #69 | `#70` 23/08/2023 ... CTIA - Comissão Temporária Interna sobre Inteligência Artificial no Brasil ... MATÉRIA COM A RELATORIA ... Distribuído ao Senador Eduardo Gomes,… |
| [[18] [23]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | #70 | #4, #68, #71, #74, #173 | #6, #169 | `#70` CTIA - Comissão Temporária Interna sobre Inteligência Artificial no Brasil ... Ao Relator, Senador Eduardo Gomes, para prosseguimento da tramitação. |
| [[19] [22]](https://www.congressonacional.leg.br/materias/materias-bicamerais/-/ver/pl-2338-2023) | #71, #74 | #5, #68–69 | #70, #169 | `#71` Na 14ª Reunião [...] a Comissão realiza audiência pública, com a finalidade de debater os impactos da Inteligência Artificial nos Setores da Indústria, Agricul… |
| [[26]](https://repositorio.uel.br/bitstreams/d2237cbd-9bfb-4b9e-90d3-cd3721add89c/download) | — | — | #114, #116–117, #146, #171 | — |
| [[7] [8]](https://artificialintelligenceact.eu/the-act/) | #10 | #49, #145 | — | `#10` The EU AI Act was published in the Official Journal (OJ) of the European Union on 12 July 2024. |
| [[27]](https://douglasvilar.com.br/artigos/posts/2026-06-13_marco-legal-ia-pl-2338-regulacao-brasil) | #116 | #114, #171 | — | `#116` A ANPD (a mesma da LGPD) é designada como órgão coordenador do Sistema Nacional de IA, com competência para editar normas gerais, fiscalizar setores que não te… |
| [[28] [36]](https://itsrio.org/wp-content/uploads/2017/01/Livro-Inteligencia-Artificial-e-Sociedade-Conectada.pdf) | #0 | #1, #110 | — | `#0` Em um cenário de inovação acelerada, em que a Inteligência Artificial e as tecnologias digitais vêm impactando as relações humanas e institucionais |
| [[12]](https://www.trooper.dk/en/eu-ai-act-guide/) | — | #2, #12 | — | `#2` The EU AI Act – formally Regulation (EU) 2024/1689 of the European Parliament and of the Council |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://repositorio.ufrn.br/bitstreams/fe6b8240-cdbf-45ea-8704-7c2882b10194/download — interstitial — barreira de acesso (interstitial): We collect and process your personal information for the following purposes: Functional, Statistical That's ok Decline C

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-0`** [28], [36]
  - Trecho: A expansão acelera dos sistemas de inteligência artificial (IA) nas mais diversas instâncias da sociedade contemporânea reconfigurou a relação entre inovação tecnológica, proteção de direitos fundamentais e soberania es…
  - Justificativa: A evidência sustenta a afirmação em seus elementos essenciais. Diversos trechos descrevem a expansão acelerada da IA na sociedade, a necessidade de reequilibrar inovação tecnológica e proteção de direitos fundamentais,…
  - Suporte veio de: [28] [36]
  - Evidência: “Em um cenário de inovação acelerada, em que a Inteligência Artificial e as tecnologias digitais vêm impactando as relações humanas e institucionais”
  - Não coberto pela evidência: O termo 'soberania estatal' especificamente não é usado; a evidência fala em 'soberania digital' e 'soberania nacional' no contexto de cibersegurança, não diretamente de IA
  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta parcialmente a afirmação: documenta a expansão da IA na sociedade, a tensão entre inovação tecnológica e proteção de d…") — cascata: baseline → context_expansion
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-10`** [2], [10] [3], [14] [7], [8]
  - Trecho: O Regulamento (UE) 2024/1689 do Parlamento Europeu e do Conselho foi formalmente publicado no Jornal Oficial da União Europeia em 12 de julho de 2024
  - Justificativa: A evidência confirma explicitamente que o Regulamento (UE) 2024/1689 foi publicado no Jornal Oficial da União Europeia em 12 de julho de 2024. A referência cf6364475f91d784 afirma a publicação no OJ nessa data, e a refe…
  - Suporte veio de: [7] [8] [2] [10]
  - Evidência: “The EU AI Act was published in the Official Journal (OJ) of the European Union on 12 July 2024.”
  - Não coberto pela evidência: A expressão 'do Parlamento Europeu e do Conselho' não aparece literalmente na evidência, embora o número do regulamento (UE) 2024/1689 seja identificado de forma inequívoca.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] [8] | sustenta | The EU AI Act was published in the Official Journal (OJ) of the European Union on 12 July 2024. |
    | [2] [10] | sustenta | 12 July 2024## Published in the Official Journal Regulation (EU) 2024/1689 was published, beginning the countdown to en… |
    | [3] [14] | parcial | 12 July 2024 |

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-11`** [1], [4] [2], [10] [3], [14] [5], [11] [6], [13]
  - Trecho: e entrou em vigor em 1º de agosto de 2024.
  - Justificativa: A evidência confirma explicitamente e de forma consistente em múltiplas fontes que o EU AI Act entrou em vigor em 1º de agosto de 2024.
  - Suporte veio de: [1] [4] [5] [11] [2] [10] [3] [14] [6] [13]
  - Evidência: “01 Aug 2024Entry into force”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] [4] | sustenta | 01 Aug 2024Entry into force |
    | [5] [11] | sustenta | 1 August 2024 ### EU AI Act enters into force |
    | [2] [10] | sustenta | 1 August 2024## The AI Act entered into force |
    | [3] [14] | sustenta | 1 August 2024 **Application:** Date of entry into force of the AI Act. |
    | [6] [13] | sustenta | in force since 1 August 2024 |

### UNSUPPORTED

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-14`** [6], [13] [9], [15]
  - Trecho: O objetivo é evitar sobrecarregar sistemas de baixo risco com exigências burocráticas excessivas, concentrando o fardo regulatório, as auditorias e os testes de conformidade sobre aplicações que possam impactar diretame…
  - Justificativa: A evidência descreve a abordagem baseada em risco do AI Act (sistemas de alto risco são fortemente regulados, enquanto os de risco mínimo são amplamente não regulados), o que se alinha vagamente com a ideia geral da afi…
  - Suporte veio de: [9] [15] [6] [13]
  - Não coberto pela evidência: O 'objetivo' explícito de evitar sobrecarregar sistemas de baixo risco com exigências burocráticas excessivas; Menção a 'auditorias'; Áreas específicas: 'saúde, segurança, direitos fundamentais e estado de direito'
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] [13] | parcial | classifying AI systems into four risk categories: unacceptable risk (banned), high-risk (heavily regulated), limited ri… |
    | [9] [15] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-17`** [6], [13] [9], [15]
  - Trecho: Entre as condutas banidas estão: a pontuação social (social scoring) conduzida por autoridades públicas ou agentes privados que resulte em tratamento prejudicial desproporcional
  - Justificativa: A evidência menciona apenas 'government-run social scoring' como exemplo de prática banida, mas não aborda a extensão para agentes privados nem a condição de 'tratamento prejudicial desproporcional'. A afirmação é mais…
  - Suporte veio de: [9] [15]
  - Evidência: “First, applications and systems that create an **unacceptable risk**, such as government-run social scoring of the type used in China, are banned.”
  - Não coberto pela evidência: social scoring conduzida por agentes privados; que resulte em tratamento prejudicial desproporcional
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] [13] | ausente | — |
    | [9] [15] | parcial | applications and systems that create an **unacceptable risk**, such as government-run social scoring of the type used i… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-18`** [6], [13]
  - Trecho: o emprego de técnicas subliminares ou deliberadamente manipulativas destinadas a distorcer o comportamento humano e causar danos físicos ou psicológicos
  - Justificativa: A evidência menciona 'prohibited AI practices' e 'unacceptable-risk AI practices' que são banidas, mas não detalha quais são essas práticas. O texto não faz qualquer referência a técnicas subliminares, manipulação delib…
  - Não coberto pela evidência: técnicas subliminares; técnicas deliberadamente manipulativas; distorcer o comportamento humano
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-42`** [9], [15]
  - Trecho: A quarta e última categoria abrange os sistemas de risco mínimo ou nulo, que representam a maioria das aplicações em uso corrente (como filtros de spam ou sistemas de otimização industrial sem impacto direto em pessoas).
  - Justificativa: A evidência afirma explicitamente que o AI Act divide as aplicações em TRÊS categorias de risco (risco inaceitável, alto risco e aplicações não regulamentadas), enquanto a afirmação fala em uma 'quarta e última categori…
  - Evidência: “The Act assigns applications of AI to three risk categories. First, applications and systems that create an **unacceptable risk**, such as government-run social scoring of the type used in China, are banned. Second, **h…”
  - Não coberto pela evidência: Existência de uma 'quarta' categoria de risco; Sistemas de risco mínimo ou nulo como categoria distinta; Filtros de spam como exemplo
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-106`** [17] [20] [29], [31]
  - Trecho: A disciplina da responsabilidade civil no PL 2338/2023 afasta-se de ambiguidades conceituais ao regular expressamente a reparação dos danos patrimoniais, morais, individuais ou difusos causados pelo funcionamento de sis…
  - Justificativa: The claim is contradicted on two fronts. First, the claim states the civil liability discipline "afasta-se de ambiguidades conceituais" (moves away from conceptual ambiguities), but the academic evidence explicitly stat…
  - Suporte veio de: [17]
  - Evidência: “No Brasil, o Projeto de Lei n. 2.338/2023 representa o esforço inicial de regulação da IA, aproximando-se do modelo europeu, mas com lacunas quanto à responsabilidade objetiva e maior dependência da interpretação judici…”
  - Não coberto pela evidência: "difusos" — Art. 27 uses "coletivo" not "difusos"; "afasta-se de ambiguidades conceituais" — evidence indicates remaining gaps and uncertainties in the civil liability framework
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [17] | parcial | **Art. 27.** O fornecedor ou operador de sistema de inteligência artificial que cause dano patrimonial, moral, individu… |
    | [29] [31] | contradiz | No Brasil, o Projeto de Lei n. 2.338/2023 representa o esforço inicial de regulação da IA, aproximando-se do modelo eur… |
    | [20] | ausente | — |
