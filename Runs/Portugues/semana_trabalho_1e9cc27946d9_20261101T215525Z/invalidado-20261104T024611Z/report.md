# Relatório de Auditoria — ChatGPT (semana_trabalho_1e9cc27946d9_20261101T215525Z)

**Arquivo auditado:** `answers/ChatGPT/EmConsolidacao/semana_trabalho.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_1e9cc27946d9_20261101T215525Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-01T22:08:44.178687+00:00 |
| **Total de trechos citados** | 54 |
| **Tempo de processamento** | 0:00:13:19 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 35.0 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 77 marcadores, 13 distintos |
| Referências listadas | 13 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 21 | 38.9% |
| **UNSUPPORTED** | 9 | 16.7% |
| **CONTRADICTED** | 1 | 1.9% |
| **SKIPPED** | 23 | 42.6% |
| **TOTAL** | 54 | 100.0% |

Sobre os 31 trechos citados auditados: SUPPORTED 67,74%, UNSUPPORTED 29,03%, CONTRADICTED 3,22%.

> **10 dos 21 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 10 estão **contados dentro** dos 21 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`13` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `3` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `1` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 4.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#52` O estado da evidência sustenta uma posição intermediária mais forte: **reduções reais de tempo de trabalho, com remuner… | [1] [2] [3] [6] | [7] [5] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1037763 |
| **Média de tokens por requisição** | 33476.2 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/13 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://autonomy.work/wp-content/uploads/2023/02/The-results-are-in-The-UKs-four-day-week-pilot.pdf) | error | 22 | 0 | 0 | 0 | 22 |
| [[1]](https://www.nature.com/articles/s41562-025-02259-6) | downloaded | 12 | 5 | 4 | 3 | 0 |
| [[6]](https://autonomy.work/wp-content/uploads/2021/06/ICELAND_4DW.pdf) | error | 9 | 0 | 0 | 0 | 9 |
| [[5]](https://www.iefp.pt/documents/10181/11729755/Experiencia-Piloto_Semana%2Bde%2Bquatro%2Bdias.pdf/f4cdc63f-1023-4e1b-89c3-e35e8a7a06ea) | downloaded | 8 | 5 | 2 | 1 | 0 |
| [[7]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693e8a0d0669596b183b27fa/1765706253519/Brazil%2B4%2BDay%2BWeek%2BPilot%2B2024.pdf) | downloaded | 7 | 5 | 2 | 0 | 0 |
| [[3]](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | downloaded | 5 | 0 | 1 | 4 | 0 |
| [[4]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[8]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[9]](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[10]](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003L0088) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[11]](https://www.gov.uk/flexible-working) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://www.camara.leg.br/noticias/1273660-empregadores-propoem-negociacao-coletiva-para-reduzir-jornada-para-36-horas-em-vez-de-mudar-a-constituicao/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[13]](https://www12.senado.leg.br/noticias/materias/2025/04/08/jornada-de-36-horas-trara-empregos-e-qualidade-de-vida-dizem-debatedores) | inaccessible | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.nature.com/articles/s41562-025-02259-6) | #1, #13, #19–21 | #48–49, #52–53 | #11, #29, #37 | `#1` Both company-level and individual-level reductions in hours are correlated with well-being gains, with larger individual-level (but not company-level) reductio… |
| [[5]](https://www.iefp.pt/documents/10181/11729755/Experiencia-Piloto_Semana%2Bde%2Bquatro%2Bdias.pdf/f4cdc63f-1023-4e1b-89c3-e35e8a7a06ea) | #0, #7, #17, #35, #51 | #50, #53 | #36 | `#0` Sem corte de salário. Com redução de horas semanais. Voluntária e reversível. |
| [[7]](https://static1.squarespace.com/static/66d46d86bd7db51794e9c3cd/t/693e8a0d0669596b183b27fa/1765706253519/Brazil%2B4%2BDay%2BWeek%2BPilot%2B2024.pdf) | #8–10, #18, #51 | #11, #49 | — | `#8` In Brazil, 21 companies participated in the 4 day week pilot with around 280 employees. One company located in Rio Grande do Sul was affected by the flood trag… |
| [[3]](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | — | #49 | #6, #11, #37, #52 | `#49` As empresas foram avaliadas quanto à produtividade, custos e lucros; os trabalhadores foram avaliados em termos de bem-estar, qualidade de vida e saúde física… |
| [[4]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | #6–7, #15 | #16, #50 | — | `#6` Se antes da adesão ao projeto essa harmonização era difícil ou muito difícil para 46% dos envolvidos, a percentagem baixou para 8% após quase seis meses de exp… |
| [[8]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | — | #40 | #38 ⚡ | `#38` XIII - duração do trabalho normal não superior a 8 (oito) horas diárias e 40 (quarenta) horas semanais, facultada a compensação de horários e a redução da jorn… |
| [[9]](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm) | — | #39–40 | — | `#39` Art. 66 - Entre 2 (duas) jornadas de trabalho haverá um período mínimo de 11 (onze) horas consecutivas para descanso. \| Art. 67 - Será assegurado a todo empreg… |
| [[11]](https://www.gov.uk/flexible-working) | #45 | — | — | `#45` All employees have the legal right to request flexible working. Employees can request a change to: - the number of hours they work - when they start or finish… |
| [[12]](https://www.camara.leg.br/noticias/1273660-empregadores-propoem-negociacao-coletiva-para-reduzir-jornada-para-36-horas-em-vez-de-mudar-a-constituicao/) | #41 | — | — | `#41` Representantes de setores como indústria, comércio, transporte, agropecuária, saúde e educação sugeriram nesta segunda-feira (18), em audiência pública na Câma… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www12.senado.leg.br/noticias/materias/2025/04/08/jornada-de-36-horas-trara-empregos-e-qualidade-de-vida-dizem-debatedores — Falha ao conectar em https://www12.senado.leg.br/noticias/materias/2025/04/08/jornada-de-36-horas-trara-empregos-e-qualidade-de-vida-dizem-debatedores: Failed to perform, curl: (28) Connection timed out after 10023 milliseconds. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

### Bloqueadas por barreira de acesso

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003L0088 — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-0`** [5]
  - Trecho: O piloto oficial português explicitamente adotou redução de horas, manutenção salarial, voluntariedade e reversibilidade, permitindo que cada organização negociasse formatos como 32, 34 ou 36 horas.
  - Justificativa: Todos os elementos da afirmação estão explicitamente sustentados pela evidência: redução de horas semanais, sem corte salarial (manutenção salarial), carácter voluntário e reversível, e a possibilidade de negociar forma…
  - Suporte veio de: [5]
  - Evidência: “Sem corte de salário. Com redução de horas semanais. Voluntária e reversível.”
- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-1`** [1]
  - Trecho: Reduções maiores nas horas efetivamente trabalhadas no nível individual estiveram associadas a ganhos maiores de bem-estar, mediados parcialmente por menor fadiga e problemas de sono e por melhor percepção da capacidade…
  - Justificativa: A evidência do abstract afirma explicitamente que reduções maiores no nível individual estão associadas a maiores ganhos de bem-estar, e que três fatores mediam essa relação: capacidade de trabalho autoavaliada melhorad…
  - Suporte veio de: [1]
  - Evidência: “Both company-level and individual-level reductions in hours are correlated with well-being gains, with larger individual-level (but not company-level) reductions associated with greater improvements in well-being.”
  - Não coberto pela evidência: O termo 'parcialmente' na mediação não é explicitamente stated na evidência, que apenas diz 'mediate the relationship'.
- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-6`** [3] [4]
  - Trecho: A proporção de trabalhadores que considerava difícil ou muito difícil conciliar trabalho e vida pessoal caiu de 46% para 8%, e os indicadores reportados mostraram reduções de 19% em exaustão, 21% em ansiedade, 23% em fa…
  - Justificativa: Todos os elementos da afirmação estão explicitamente presentes na evidência: a proporção de trabalhadores que considerava difícil ou muito difícil conciliar trabalho e vida pessoal caiu de 46% para 8%, e as reduções per…
  - Suporte veio de: [4]
  - Evidência: “Se antes da adesão ao projeto essa harmonização era difícil ou muito difícil para 46% dos envolvidos, a percentagem baixou para 8% após quase seis meses de experiência.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | sustenta | Se antes da adesão ao projeto essa harmonização era difícil ou muito difícil para 46% dos envolvidos, a percentagem bai… |
    | [3] | ausente | — |

### UNSUPPORTED

- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-11`** [1] [2] [3] [6] [7]
  - Trecho: A evidência hoje é suficientemente positiva para justificar testes mais amplos; ainda é insuficiente para calcular com confiança efeitos macroeconômicos de longo prazo sobre salários, preços, emprego, produtividade agre…
  - Justificativa: A evidência descreve resultados positivos de pilotos da semana de 4 dias (bem-estar, produtividade, engajamento) e menciona planos de expandir o estudo, o que se aproxima da ideia de 'testes mais amplos'. No entanto, a…
  - Suporte veio de: [7]
  - Evidência: “We are excited to expand the study to include more companies interested in testing the 4 day week.”
  - Não coberto pela evidência: insuficiência para calcular com confiança efeitos macroeconômicos de longo prazo; efeitos sobre salários; efeitos sobre preços
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [3] | ausente | — |
    | [7] | parcial | To celebrate the positive data and advancements achieved |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-16`** [4]
  - Trecho: A redução média, de 13,7%, mostra por que o debate não deve ser reduzido à escolha binária “cinco dias versus 32 horas”: organizações têm testado gradientes de redução, desde 10% até aproximadamente 20%.
  - Justificativa: A evidência confirma a redução média de 13,7% das horas semanais, mas não sustenta os demais elementos da afirmação: o enquadramento do debate como escolha binária 'cinco dias versus 32 horas' não aparece na evidência,…
  - Suporte veio de: [4]
  - Evidência: “Em média, a experiência da semana de quatro dias envolveu uma redução de 13,7% das horas semanais, de uma média de 39,3 para 34 horas, reportada pelas empresas.”
  - Não coberto pela evidência: O enquadramento do debate como escolha binária 'cinco dias versus 32 horas'; A afirmação de que organizações testaram gradientes de redução desde 10% até aproximadamente 20%
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-29`** [2] [1]
  - Trecho: Não há, nos principais estudos examinados, evidência causal suficientemente robusta para afirmar que determinado porte obtém sistematicamente retorno maior.
  - Justificativa: A evidência fornecida consiste em listas de referências, resumo e metadados de um estudo sobre redução da jornada de trabalho (4-day workweek) e bem-estar dos trabalhadores. Não há qualquer menção a 'porte' de empresas,…
  - Não coberto pela evidência: porte de empresas; retorno maior por porte; evidência causal sobre porte e retorno
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |

  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semana_trabalho_1e9cc27946d9_20261101T215525Z-38`** [8]
  - Trecho: No Brasil, a Constituição estabelece, como regra geral, duração normal não superior a oito horas diárias e 44 semanais, permitindo compensação e redução mediante acordo ou convenção coletiva; também protege a irredutibi…
  - Justificativa: A evidência mostra que a redação atual do inciso XIII estabelece jornada de '40 (quarenta) horas semanais', e não 44 como afirma o trecho. A versão com 44 horas está riscada (substituída pela EC 141/2026). Os demais pon…
  - Suporte veio de: [8]
  - Evidência: “XIII - duração do trabalho normal não superior a 8 (oito) horas diárias e 40 (quarenta) horas semanais, facultada a compensação de horários e a redução da jornada, mediante acordo ou convenção coletiva de trabalho; (Red…”
  - Não coberto pela evidência: O trecho afirma '44 semanais', mas a redação atual na evidência estabelece '40 (quarenta) horas semanais'

---

## 10. Trechos Citados Não Auditados

Motivos: 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 21 citam referência não baixada/inacessível.

- `semana_trabalho_1e9cc27946d9_20261101T215525Z-2` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-3` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-4` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-5` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-12` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-14` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-22` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-23` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-24` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-25` — Referencia(s) citada(s) ['a38ffa89f273703c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-26` — Referencia(s) citada(s) ['a38ffa89f273703c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-27` — Referencia(s) citada(s) ['a38ffa89f273703c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-28` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-30` — Referencia(s) citada(s) ['a38ffa89f273703c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-31` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-32` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-33` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-34` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-42` — Referencia(s) citada(s) ['0f6a73b74e4adf6e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-43` — Referencia(s) citada(s) ['0f6a73b74e4adf6e'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-44` — Referencia(s) citada(s) ['a38ffa89f273703c'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-46` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `semana_trabalho_1e9cc27946d9_20261101T215525Z-47` — Referencia(s) citada(s) ['26991fcd7fe5b57f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).