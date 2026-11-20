# Relatório de Auditoria — Gemini (regulacao_ia_87ba15eb4df4_20261102T161649Z)

**Arquivo auditado:** `answers/Gemini/Emergente/regulacao_ia.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | regulacao_ia_87ba15eb4df4_20261102T161649Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-02T18:25:31.011107+00:00 |
| **Total de trechos citados** | 175 |
| **Tempo de processamento** | 0:02:08:41 |
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
| **SUPPORTED** | 89 | 50.9% |
| **UNSUPPORTED** | 71 | 40.6% |
| **CONTRADICTED** | 3 | 1.7% |
| **SKIPPED** | 11 | 6.3% |
| **PENDENTE** | 1 | 0.6% |
| **TOTAL** | 175 | 100.0% |

Sobre os 163 trechos citados auditados: SUPPORTED 54,60%, UNSUPPORTED 43,55%, CONTRADICTED 1,84%.

> **51 dos 89 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 51 estão **contados dentro** dos 89 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`89` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `14` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `18` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `22` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 15, full_doc_scan = 3.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` Concebido como a primeira legislação horizontal abrangente sobre inteligência artificial no mundo, o texto europeu proj… | [6] [9] [31] | [34] [30] [32] [28] [36] [17] | — |
| `#8` A análise comparativa entre o EU AI Act e o PL 2338/2023 revela não apenas convergências na neutralização de riscos ali… | [25] [31] | [27] [34] [28] [36] [17] [30] [32] [9] [15] | — |
| `#21` e a identificação biométrica remota em tempo real em espaços acessíveis ao público para fins de aplicação da lei, com e… | [6] | [17] [28] [36] [21] | — |
| `#26` Incluem-se nessa classificação os sistemas aplicados a infraestruturas críticas (tráfego, abastecimento de água e energ… | [6] | [17] [21] [30] [32] [28] [36] [26] | — |
| `#27` educação e formação profissional (avaliação de estudantes e acesso a instituições) | [6] | [17] [30] [32] [34] [28] [36] | — |
| `#35` a elaboração e atualização de documentação técnica detalhada e o registro automático de eventos (logs) para garantir a… | [6] | [17] [34] [28] [36] [5] [11] [30] [32] | — |
| `#41` Os fornecedores e implantadores devem garantir que as pessoas naturais sejam claramente informadas de que estão interag… | [2] [3] [5] | [21] [17] [28] [36] [30] [32] | — |
| `#68` No Brasil, o debate sobre a regulação da inteligência artificial ganhou tração estruturada a partir do Projeto de Lei n… | [16] [18] [19] | [30] [32] [28] [36] [27] [17] | — |
| `#69` O projeto teve como alicerce o anteprojeto elaborado pela Comissão de Juristas responsável por subsidiar a regulação da… | [16] [19] [20] | [28] [36] [17] [30] [32] [21] [27] | — |
| `#73` Em 10 de dezembro de 2024, o Plenário do Senado Federal aprovou a matéria na forma do substitutivo consolidado, declara… | [16] [20] [21] | [19] [22] [27] [17] [30] [32] | — |
| `#81` O direito ao uso de linguagem simples, transparente e acessível nas interações automatizadas, com salvaguardas especiai… | [20] [21] | [17] [34] [28] [36] [27] | — |
| `#83` O direito à explicação substancial e inteligível sobre a decisão tomada pelo sistema, compreendendo os critérios, os da… | [20] [21] | [17] [27] [28] [36] [34] [26] | — |
| `#90` A utilização de câmeras para identificação biométrica em tempo real é restringida a exceções penais e de segurança públ… | [20] [21] | [17] [28] [36] [30] [32] | — |
| `#117` Expedir normas infralegais regulamentares sobre procedimentos de Avaliação de Impacto Algorítmico e requisitos de certi… | [20] [26] [31] | [17] [21] [34] [28] [36] [30] [32] | — |
| `#123` A ANPD atuará como órgão central articulador para evitar sobreposições ou conflitos normativos entre as agências. | [34] | [28] [36] [21] [27] | — |
| `#126` A comparação minuciosa entre o EU AI Act e o PL 2338/2023 evidencia que o legislador brasileiro utilizou a estrutura eu… | [25] [31] | [27] [28] [36] [34] [17] [19] [22] | — |
| `#130` Tanto o Regulamento (UE) 2024/1689 quanto o PL 2338/2023 banem o social scoring coercitivo, a manipulação subliminar de… | [6] [17] [20] [21] | [28] [36] [27] [30] [32] [5] [11] [34] [25] [35] | — |
| `#163` O Marco Legal de IA (PL 2338/2023), que exigirá a Avaliação de Impacto Algorítmico para sistemas médicos de alto risco. | [20] [35] | [17] [21] [27] [28] [36] [34] | — |
| `#165` Embora a imposição de requisitos rigorosos aumente os custos operacionais de compliance e exija maior suporte jurídico… | [2] [5] [35] | [28] [36] [34] [30] [32] | — |
| `#167` O EU AI Act europeu (Regulamento UE 2024/1689) estabeleceu o padrão de referência para a regulação global da IA. | [6] [9] [31] | [34] [30] [32] [27] [28] [36] [2] [10] | — |
| `#173` À medida que o AI Act alcança suas fases de plena aplicabilidade na Europa e o PL 2338/2023 avança no Congresso Naciona… | [1] [2] [5] [18] [35] | [27] [28] [36] [17] [34] [19] [22] | — |
| `#174` A conformidade ética e regulatória deixa de ser um mero custo burocrático e passa a figurar como elemento estratégico i… | [6] [20] [31] [35] | [34] [28] [36] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 4193722 |
| **Média de tokens por requisição** | 25728.4 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 2/22 (9.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[20]](https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara) | inaccessible | 64 | 0 | 0 | 0 | 64 |
| [[6] [13]](https://reversa.ai/regulations/eu-ai-act) | downloaded | 58 | 15 | 23 | 20 | 0 |
| [[21]](https://www12.senado.leg.br/noticias/materias/2024/12/05/comissao-chega-a-consenso-e-regulamentacao-da-inteligencia-artificial-vai-a-plenario) | downloaded | 36 | 20 | 14 | 2 | 0 |
| [[2] [10]](https://www.euaiact.com/implementation-timeline) | downloaded | 35 | 15 | 7 | 13 | 0 |
| [[29] [31]](https://gedai.ufpr.br/responsabilizacao-das-plataformas-digitais-pela-violacao-de-direitos-autorais/) | inaccessible | 31 | 0 | 0 | 0 | 31 |
| [[17]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | downloaded | 29 | 13 | 15 | 1 | 0 |
| [[5] [11]](https://euaicompass.com/timeline.html) | downloaded | 27 | 14 | 6 | 7 | 0 |
| [[1] [4]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) | downloaded | 22 | 13 | 6 | 3 | 0 |
| [[25] [35]](https://sciereli.com.br/blog/governanca-ia-saude-brasil/) | downloaded | 21 | 7 | 10 | 4 | 0 |
| [[9] [15]](https://artificialintelligenceact.eu/) | downloaded | 16 | 1 | 11 | 4 | 0 |
| [[3] [14]](https://artificialintelligenceact.eu/implementation-timeline/) | downloaded | 13 | 8 | 3 | 2 | 0 |
| [[34]](https://vlklaw.com.br/wp-content/uploads/2024/12/Tendencias-Direito-Digital-2025.-comprimido.pdf) | downloaded | 10 | 4 | 5 | 1 | 0 |
| [[16] [24]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf) | inaccessible | 8 | 0 | 0 | 0 | 8 |
| [[18] [23]](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233) | inaccessible | 8 | 0 | 0 | 0 | 8 |
| [[19] [22]](https://www.congressonacional.leg.br/materias/materias-bicamerais/-/ver/pl-2338-2023) | downloaded | 7 | 4 | 2 | 0 | 1 |
| [[26]](https://repositorio.uel.br/bitstreams/d2237cbd-9bfb-4b9e-90d3-cd3721add89c/download) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[7] [8]](https://artificialintelligenceact.eu/the-act/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[27]](https://douglasvilar.com.br/artigos/posts/2026-06-13_marco-legal-ia-pl-2338-regulacao-brasil) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[28] [36]](https://itsrio.org/wp-content/uploads/2017/01/Livro-Inteligencia-Artificial-e-Sociedade-Conectada.pdf) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[12]](https://www.trooper.dk/en/eu-ai-act-guide/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[30] [32]](https://intic.gov.mz/wp-content/uploads/2025/05/Inteligencia_Artificial_Desafios_e_Oportunidades_assinado.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[33]](https://repositorio.ufrn.br/bitstreams/fe6b8240-cdbf-45ea-8704-7c2882b10194/download) | blocked | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[6] [13]](https://reversa.ai/regulations/eu-ai-act) | #2, #11–13, #16, #30, #32–34, #36, #44, #52–53, #56, #154 | #3, #14–15, #26–28, #31, #35, #37–39, #46–47, #49, #54–55, #57–58, #127–128, #145, #167–168 | #17–21, #29, #45, #48, #129–130, #134, #137, #144, #147, #155–157, #164, #166, #174 | `#2` The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence. Adopted in 2024 |
| [[21]](https://www12.senado.leg.br/noticias/materias/2024/12/05/comissao-chega-a-consenso-e-regulamentacao-da-inteligencia-artificial-vai-a-plenario) | #77, #82, #85, #89, #91, #96–99, #101–102, #112–113, #118, #120, #124–125, #138, #142, #148 | #73, #79–81, #83–84, #90, #100, #108, #130–131, #139, #149, #170 | #136 ⚡, #105 (s/ aval.) | `#77` O projeto assegura uma série de direitos para as pessoas que forem afetadas pelos sistemas de inteligência artificial: - Direito à informação prévia de que est… |
| [[2] [10]](https://www.euaiact.com/implementation-timeline) | #10–11, #16, #22–25, #56–58, #60–63, #65 | #15, #40–41, #59, #131, #168, #173 | #12, #39, #44–45, #49, #137, #145, #150–154, #165 | `#10` 12 July 2024## Published in the Official Journal Regulation (EU) 2024/1689 was published, beginning the countdown to entry into force. |
| [[17]](https://legis.senado.leg.br/sdleg-getter/documento?disposition=inline&dm=9347622) | #7, #77–78, #87, #91–94, #154–157, #172 | #9, #75–76, #80, #86, #95, #104, #106, #109, #127–128, #130, #135, #143, #170 | #129 | `#7` Art. 1º ... com o objetivo de proteger os direitos fundamentais ... em benefício da pessoa humana ... I – a centralidade da pessoa humana ... Art. 5º Pessoas a… |
| [[5] [11]](https://euaicompass.com/timeline.html) | #11, #16, #22, #24–25, #51, #56–58, #60, #62, #64–66 | #15, #40, #59, #61, #153, #173 | #41, #48, #131, #150–152, #165 | `#11` 1 August 2024 ### EU AI Act enters into force |
| [[1] [4]](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) | #11, #16, #23–24, #51, #56–58, #60–62, #64, #66 | #40, #48, #50, #55, #168, #173 | #52, #137, #164 | `#11` 01 Aug 2024Entry into force |
| [[25] [35]](https://sciereli.com.br/blog/governanca-ia-saude-brasil/) | #6–7, #152, #158–159, #161–162 | #8, #86, #122, #126, #150–151, #153, #160, #163, #173 | #121, #155, #165, #174 | `#6` O PL 2338/2023, conhecido como Marco Legal da Inteligência Artificial, foi aprovado pelo Senado em dezembro de 2024 e segue em tramitação na Câmara dos Deputad… |
| [[9] [15]](https://artificialintelligenceact.eu/) | #44 | #3, #13, #17, #28, #39, #43, #49–50, #145, #147, #167 | #14, #40, #60, #42 ⚡ | `#44` Enforcement of Chapter V under the EU AI Act; This page aims to provide an overview of the EU AI Act's enforcement provisions relating to Chapter V, namely the… |
| [[3] [14]](https://artificialintelligenceact.eu/implementation-timeline/) | #11, #51, #56, #58, #62–64, #67 | #10, #41, #55 | #48, #52 | `#11` 1 August 2024 **Application:** Date of entry into force of the AI Act. |
| [[34]](https://vlklaw.com.br/wp-content/uploads/2024/12/Tendencias-Direito-Digital-2025.-comprimido.pdf) | #121, #144, #146, #171 | #115–116, #122–123, #139 | #114 | `#121` A lógica é valorizar e reforçar as competências regulatória, sancionatória e normativa das autoridades setoriais em harmonia com as correlatas gerais da autori… |
| [[19] [22]](https://www.congressonacional.leg.br/materias/materias-bicamerais/-/ver/pl-2338-2023) | #5, #70–71, #74 | #68–69 | #169 (pulado) | `#5` debater o Relatório Final da Comissão de Juristas responsável por subsidiar elaboração de Substitutivo sobre Inteligência Artificial no Brasil (CJSUBIA) \| Laur… |
| [[26]](https://repositorio.uel.br/bitstreams/d2237cbd-9bfb-4b9e-90d3-cd3721add89c/download) | — | — | #114, #116–117, #146, #171 | — |
| [[7] [8]](https://artificialintelligenceact.eu/the-act/) | #10 | #49, #145 | — | `#10` The EU AI Act was published in the Official Journal (OJ) of the European Union on 12 July 2024. |
| [[27]](https://douglasvilar.com.br/artigos/posts/2026-06-13_marco-legal-ia-pl-2338-regulacao-brasil) | #116, #171 | — | #114 ⚡ | `#116` A ANPD (a mesma da LGPD) é designada como órgão coordenador do Sistema Nacional de IA |
| [[28] [36]](https://itsrio.org/wp-content/uploads/2017/01/Livro-Inteligencia-Artificial-e-Sociedade-Conectada.pdf) | #0 | #1, #110 | — | `#0` Em um cenário de inovação acelerada, em que a Inteligência Artificial e as tecnologias digitais vêm impactando as relações humanas e institucionais |
| [[12]](https://www.trooper.dk/en/eu-ai-act-guide/) | — | #2, #12 | — | `#2` The EU AI Act – formally Regulation (EU) 2024/1689 of the European Parliament and of the Council |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf — Falha ao conectar em https://www25.senado.leg.br/web/atividade/materias/-/materia/157233/pdf: Failed to perform, curl: (28) Connection timed out after 10001 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www25.senado.leg.br/web/atividade/materias/-/materia/157233 — Falha ao conectar em https://www25.senado.leg.br/web/atividade/materias/-/materia/157233: Failed to perform, curl: (28) Connection timed out after 10056 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara — Falha ao conectar em https://www12.senado.leg.br/noticias/materias/2024/12/10/senado-aprova-regulamentacao-da-inteligencia-artificial-texto-vai-a-camara: Failed to perform, curl: (28) Connection timed out after 10032 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.
- https://gedai.ufpr.br/responsabilizacao-das-plataformas-digitais-pela-violacao-de-direitos-autorais/ — Falha ao conectar em https://gedai.ufpr.br/responsabilizacao-das-plataformas-digitais-pela-violacao-de-direitos-autorais/: Failed to perform, curl: (60) SSL certificate OpenSSL verify result: unable to get local issuer certificate (20). See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

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
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-2`** [6], [13] [12] [29], [31]
  - Trecho: Nesse cenário de virada regulatória, a União Europeia assumiu o pioneirismo normativo global ao promulgar o Regulamento (UE) 2024/1689, amplamente conhecido como EU AI Act.
  - Justificativa: A evidência confirma que o Regulamento (UE) 2024/1689 é 'o primeiro quadro jurídico abrangente do mundo que regula a inteligência artificial', sustentando o pioneirismo normativo global da UE. O nome 'EU AI Act' e o núm…
  - Suporte veio de: [6] [13] [12]
  - Evidência: “The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence.”
  - Não coberto pela evidência: A expressão 'cenário de virada regulatória' é uma moldura narrativa não explicitamente mencionada na evidência, embora seja inferível a partir do contexto de pioneirismo.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] [13] | sustenta | The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence. Adopted in 2024 |
    | [12] | parcial | The EU AI Act – formally Regulation (EU) 2024/1689 of the European Parliament and of the Council |

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-5`** [16], [24] [19], [22] [20]
  - Trecho: Fruto do trabalho de uma comissão de juristas instalada no Senado Federal e da consolidação de diversas iniciativas anteriores
  - Justificativa: A evidência menciona explicitamente a 'Comissão de Juristas' instituída pelo Senado Federal (CJSUBIA) e mostra a tramitação conjunta e posterior consolidação de múltiplos projetos de lei anteriores (PL 21/2020, PL 5.051…
  - Suporte veio de: [19] [22]
  - Evidência: “debater o Relatório Final da Comissão de Juristas responsável por subsidiar elaboração de Substitutivo sobre Inteligência Artificial no Brasil (CJSUBIA)”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [19] [22] | sustenta | debater o Relatório Final da Comissão de Juristas responsável por subsidiar elaboração de Substitutivo sobre Inteligênc… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência menciona uma 'Comissão Especial' e 'CTIA' no Senado Federal, e a consolidação de iniciativas anteriores (via declaração de prej…") — cascata: baseline → context_expansion
### UNSUPPORTED

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-1`** [28], [36] [29], [31]
  - Trecho: A transição histórica de diretrizes éticas voluntárias e instrumentos não vinculantes (soft law) — editados por organismos internacionais como a Organização para a Cooperação e Desenvolvimento Econômico (OCDE) e a UNESC…
  - Justificativa: A evidência menciona a OCDE, discute opacidade, autonomia e riscos dos sistemas algorítmicos, e aborda tanto iniciativas voluntárias (Partnership on AI) quanto regulatórias vinculantes (GDPR, AI Act). Porém, o CLAIM con…
  - Suporte veio de: [28] [36]
  - Evidência: “Em mesmo sentido ao posicionamento da ONU, se posiciona a OCDE (Organização para Cooperação e Desenvolvimento Econômico)”
  - Não coberto pela evidência: UNESCO como organismo mencionado; transição histórica explícita de soft law para hard law; capacidade de escala como risco específico
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [28] [36] | parcial | nos últimos vinte anos observa-se uma visão muito mais cética e pessimista sobre o tema, reconhecendo-se a necessidade… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-3`** [6], [13] [9], [15] [29], [31]
  - Trecho: Concebido como a primeira legislação horizontal abrangente sobre inteligência artificial no mundo, o texto europeu projeta os efeitos do chamado "Efeito Bruxelas", pelo qual padrões regulatórios adotados no mercado inte…
  - Justificativa: A evidência confirma que o EU AI Act é a primeira legislação abrangente sobre IA no mundo, mas não menciona o termo 'Efeito Bruxelas' nem descreve o mecanismo específico pelo qual padrões regulatórios do mercado interno…
  - Suporte veio de: [6] [13] [9] [15]
  - Evidência: “The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence.”
  - Não coberto pela evidência: Termo 'Efeito Bruxelas' não aparece na evidência; Mecanismo específico de padronização de condutas operacionais em jurisdições globais; Mecanismo específico de padronização de arquiteturas de tecnologia em jurisdições globais
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [6] [13] | parcial | The EU AI Act is the world's first comprehensive legal framework regulating artificial intelligence. |
    | [9] [15] | parcial | the first comprehensive regulation on AI by a major regulator anywhere |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [34] [30] [32] [28] [36] [17] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-8`** [25], [35] [29], [31]
  - Trecho: A análise comparativa entre o EU AI Act e o PL 2338/2023 revela não apenas convergências na neutralização de riscos alinhadas ao desenvolvimento ético da tecnologia, mas também escolhas institucionais e dogmáticas disti…
  - Justificativa: A evidência menciona apenas que o PL 2338/2023 adota um 'modelo de classificação por risco (inspirado no AI Act europeu)', mas não apresenta nenhuma análise comparativa entre o EU AI Act e o PL 2338/2023. Não há menção…
  - Suporte veio de: [25] [35]
  - Não coberto pela evidência: análise comparativa entre EU AI Act e PL 2338/2023; convergências na neutralização de riscos alinhadas ao desenvolvimento ético da tecnologia; escolhas institucionais distintas
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [25] [35] | parcial | O texto adota um modelo de classificação por risco (inspirado no AI Act europeu) |

  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [27] [34] [28] [36] [17] [30] [32] [9] [15] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-42`** [9], [15]
  - Trecho: A quarta e última categoria abrange os sistemas de risco mínimo ou nulo, que representam a maioria das aplicações em uso corrente (como filtros de spam ou sistemas de otimização industrial sem impacto direto em pessoas).
  - Justificativa: A evidência afirma explicitamente que o AI Act divide as aplicações em TRÊS categorias de risco (risco inaceitável, alto risco e aplicações não regulamentadas), enquanto a afirmação fala em uma 'quarta e última categori…
  - Evidência: “The Act assigns applications of AI to three risk categories. First, applications and systems that create an **unacceptable risk**, such as government-run social scoring of the type used in China, are banned. Second, **h…”
  - Não coberto pela evidência: Existência de uma 'quarta' categoria de risco; Sistemas de risco mínimo ou nulo como categoria distinta; Filtros de spam como exemplo
- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-114`** [26] [27] [29], [31] [34]
  - Trecho: Para garantir a aplicação efetiva da lei, o PL 2338/2023 autoriza o Poder Executivo a instituir o Sistema Nacional de Regulação e Governança de Inteligência Artificial (SIA).
  - Justificativa: A evidência afirma explicitamente que o PL 2338/2023, por ser de origem parlamentar, NÃO poderia instituir o SIA sozinho, devido a vício de iniciativa constitucional. O SIA foi criado por um PL separado do governo (09/1…
  - Suporte veio de: [27]
  - Evidência: “Em 09/12/2025, o governo federal publicou em edição extra do Diário Oficial da União um PL próprio criando o Sistema Nacional para Desenvolvimento, Regulação e Governança de Inteligência Artificial (SIA).”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [27] | contradiz | Atribuir competências e estruturar órgão da administração, como dar poderes à ANPD, é matéria de iniciativa privativa d… |
    | [34] | ausente | — |

- **Trecho citado `regulacao_ia_87ba15eb4df4_20261102T161649Z-136`** [21] [29], [31]
  - Trecho: A segunda divergência relevante diz respeito à flexibilidade da lista de sistemas de alto risco.
  - Justificativa: A evidência indica explicitamente que os dois temas de maior divergência são direitos autorais e integridade da informação, não a flexibilidade da lista de sistemas de alto risco. Embora o texto mencione que a lista de…
  - Evidência: “Tudo indica que os dois temas de maior divergência, como os dispositivos que tratam de direitos autorais e integridade da informação deverão ainda ser tratados em Plenário, com tentativas de votação de destaques por gov…”
  - Não coberto pela evidência: A afirmação de que a 'segunda divergência relevante' seria a flexibilidade da lista de sistemas de alto risco não encontra respaldo, pois a evidência aponta como divergências os temas de direitos autorais e integridade da informação.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [21] | contradiz | Tudo indica que os dois temas de maior divergência, como os dispositivos que tratam de direitos autorais e integridade… |

  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência menciona que 'os dois temas de maior divergência' são 'direitos autorais e integridade da informação', não a flexibilidade da l…") — cascata: baseline → context_expansion

---

## 10. Trechos Citados Não Auditados

Motivos: 11 citam referência não baixada/inacessível.

- `regulacao_ia_87ba15eb4df4_20261102T161649Z-4` — Referencia(s) citada(s) ['2ddcc05b33f7db1a', 'c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-72` — Referencia(s) citada(s) ['c881d3853a0f27f3', 'd50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-88` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-103` — Referencia(s) citada(s) ['d50904ab9268760a', 'c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-107` — Referencia(s) citada(s) ['d50904ab9268760a', 'c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-111` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-119` — Referencia(s) citada(s) ['d50904ab9268760a'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-132` — Referencia(s) citada(s) ['c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-133` — Referencia(s) citada(s) ['c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-140` — Referencia(s) citada(s) ['c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `regulacao_ia_87ba15eb4df4_20261102T161649Z-141` — Referencia(s) citada(s) ['c20cbdad998e6a81'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).

---

## 11. Trechos Citados Pendentes

1 trecho(s) citado(s) ficaram sem veredito: a saída do juiz não pôde ser interpretada (JSON inválido ou truncado). O julgamento não foi marcado como concluído — rode `audit resume regulacao_ia_87ba15eb4df4_20261102T161649Z` para julgá-los; os já julgados não são refeitos.

- `regulacao_ia_87ba15eb4df4_20261102T161649Z-169`