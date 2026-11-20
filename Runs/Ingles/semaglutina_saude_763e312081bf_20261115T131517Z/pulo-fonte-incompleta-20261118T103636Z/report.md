# Relatório de Auditoria — ChatGPT (semaglutina_saude_763e312081bf_20261115T131517Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/Emergente/semaglutina_saude.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_763e312081bf_20261115T131517Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T00:20:01.741164+00:00 |
| **Total de trechos citados** | 108 |
| **Tempo de processamento** | 2:11:04:44 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 26.4 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 142 marcadores, 19 distintos |
| Referências listadas | 19 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 68 | 63.0% |
| **UNSUPPORTED** | 28 | 25.9% |
| **CONTRADICTED** | 1 | 0.9% |
| **SKIPPED** | 11 | 10.2% |
| **TOTAL** | 108 | 100.0% |

Sobre os 97 trechos citados auditados: SUPPORTED 70,10%, UNSUPPORTED 28,86%, CONTRADICTED 1,03%.

> **23 dos 68 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 23 estão **contados dentro** dos 68 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`31` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `9` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `3` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `6` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 3.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#47` ESSENCE is an ongoing phase 3 trial in patients with biopsy-confirmed MASH and stage F2 or F3 fibrosis, and the planned… | [9] | [5] [7] [2] [8] [1] [3] | — |
| `#50` On the basis of those histologic results, the FDA approved Wegovy in August 2025 for adults with noncirrhotic MASH and… | [10] | [1] | — |
| `#52` The ongoing 240-week ESSENCE trial is intended to determine whether the histologic improvement translates into those cl… | [10] | [1] [8] [11] [7] [19] [14] | — |
| `#55` Semaglutide reduces caloric intake and adiposity, improves insulin resistance and glycemia, and is associated with redu… | [1] | [8] [19] [11] [7] | — |
| `#78` Addiction research is earlier but more encouraging. | [15] [16] | [7] [8] [14] [12] [19] | — |
| `#91` Vomiting and diarrhea can cause volume depletion and acute kidney injury, a clinically important irony for a drug that… | [1] [6] | [19] [7] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1959126 |
| **Média de tokens por requisição** | 20197.2 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/19 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218316s002lbl.pdf) | downloaded | 25 | 16 | 7 | 2 | 0 |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/41865758/) | downloaded | 10 | 4 | 5 | 1 | 0 |
| [[6]](https://www.nejm.org/doi/10.1056/NEJMoa2403347) | blocked | 9 | 0 | 0 | 0 | 9 |
| [[5]](https://www.nejm.org/doi/full/10.1056/NEJMoa2306963) | downloaded | 8 | 5 | 1 | 2 | 0 |
| [[8]](https://diabetesjournals.org/care/article/47/8/1350/156833/Effect-of-Semaglutide-on-Regression-and) | downloaded | 8 | 7 | 1 | 0 | 0 |
| [[9]](https://www.nejm.org/doi/10.1056/NEJMoa2413258) | downloaded | 8 | 2 | 5 | 1 | 0 |
| [[18]](https://www.ahajournals.org/doi/10.1161/CIR.0000000000001453) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[2]](https://www.nejm.org/doi/full/10.1056/NEJMoa2307563) | downloaded | 7 | 4 | 3 | 0 | 0 |
| [[10]](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-treatment-serious-liver-disease-known-mash) | downloaded | 7 | 2 | 5 | 0 | 0 |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/42837024/) | downloaded | 7 | 1 | 3 | 3 | 0 |
| [[16]](https://pubmed.ncbi.nlm.nih.gov/42070571/) | downloaded | 7 | 2 | 4 | 1 | 0 |
| [[7]](https://www.nature.com/articles/s41591-024-03015-5) | downloaded | 6 | 3 | 2 | 1 | 0 |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/42610271/) | downloaded | 6 | 2 | 2 | 2 | 0 |
| [[3]](https://www.nejm.org/doi/full/10.1056/NEJMoa1607141) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[13]](https://www.fda.gov/news-events/press-announcements/fda-approves-first-medication-obstructive-sleep-apnea) | downloaded | 5 | 1 | 1 | 3 | 0 |
| [[15]](https://pubmed.ncbi.nlm.nih.gov/39937469/) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[17]](https://www.fda.gov/drugs/drug-safety-communications/fda-requires-safety-labeling-changes-glucagon-peptide-1-receptor-agonists-glp-1-ras-due-potential) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[19]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/209637s038lbl.pdf) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[4]](https://www.nejm.org/doi/10.1056/NEJMoa2501006) | blocked | 3 | 0 | 0 | 0 | 3 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218316s002lbl.pdf) | #0–1, #16, #19, #39, #54, #56, #85–90, #92, #94–95 | #2, #11, #55, #91, #93, #100–101 | #38, #57 | `#0` Semaglutide acts as a GLP-1 receptor agonist that selectively binds to and activates the GLP-1 receptor, the target for native GLP-1. |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/41865758/) | #72–75 | #7, #70–71, #77, #107 | #76 | `#72` The trials assessed the efficacy and safety of oral semaglutide up to 14 mg once daily in participants with amyloid-confirmed Alzheimer's disease, aged 55-85 y… |
| [[5]](https://www.nejm.org/doi/full/10.1056/NEJMoa2306963) | #6, #21, #23, #59, #102 | #107 | #20, #22 | `#6` In patients with heart failure with preserved ejection fraction and obesity, treatment with semaglutide (2.4 mg) led to larger reductions in symptoms and physi… |
| [[8]](https://diabetesjournals.org/care/article/47/8/1350/156833/Effect-of-Semaglutide-on-Regression-and) | #4, #40–43, #45, #103 | #44 | — | `#4` a greater proportion treated with semaglutide were normoglycemic (69.5% vs. 35.8%; P < 0.0001) and a smaller proportion had biochemical diabetes by week 156 (1… |
| [[9]](https://www.nejm.org/doi/10.1056/NEJMoa2413258) | #48–49 | #5, #46–47, #53, #107 | #57 | `#48` Resolution of steatohepatitis without worsening of fibrosis occurred in 62.9% of the 534 patients in the semaglutide group and in 34.3% of the 266 patients in… |
| [[2]](https://www.nejm.org/doi/full/10.1056/NEJMoa2307563) | #8–10, #15 | #3, #11, #107 | — | `#8` Among 17,604 patients with a BMI of 27 or greater and preexisting cardiovascular disease but without diabetes, treatment with once-weekly subcutaneous semaglut… |
| [[10]](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-treatment-serious-liver-disease-known-mash) | #51, #53 | #5, #46, #50, #52, #101 | — | `#51` Wegovy received breakthrough therapy designation for this indication and was approved under the accelerated approval pathway, which allows a therapy treating s… |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/42837024/) | #64 | #7, #69, #107 | #63, #67–68 | `#64` A total of 6 RCTs involving 1,069 participants were included, four evaluating liraglutide and two tirzepatide. Compared with control, GLP-1 receptor agonist-ba… |
| [[16]](https://pubmed.ncbi.nlm.nih.gov/42070571/) | #81–82 | #7, #78, #84, #107 | #83 ⚡ | `#81` In a 26-week, single-centre, randomised, double-blinded, placebo-controlled trial, treatment-seeking participants with moderate to severe alcohol use disorder… |
| [[7]](https://www.nature.com/articles/s41591-024-03015-5) | #29, #31, #34 | #32, #37 | #30 (s/ aval.) | `#29` This work is novel in demonstrating a potential beneficial kidney effect of semaglutide in the absence of diabetes and is the first demonstration, to our knowl… |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/42610271/) | #60–61 | #58, #107 | #6, #62 | `#60` In this prespecified SELECT substudy, we evaluated whether baseline hsCRP levels predicted MACE risk and examined the relationships between changes in hsCRP le… |
| [[3]](https://www.nejm.org/doi/full/10.1056/NEJMoa1607141) | #12–13, #92 | #15, #93 | — | `#12` In patients with type 2 diabetes who were at high cardiovascular risk, the rate of cardiovascular death, nonfatal myocardial infarction, or nonfatal stroke was… |
| [[13]](https://www.fda.gov/news-events/press-announcements/fda-approves-first-medication-obstructive-sleep-apnea) | #66 | #65 | #63, #68–69 | `#66` The improvement in AHI in participants with OSA is likely related to body weight reduction with Zepbound. |
| [[15]](https://pubmed.ncbi.nlm.nih.gov/39937469/) | #79–80 | #7, #78, #84 | — | `#79` This was a phase 2, double-blind, randomized, parallel-arm trial involving 9 weeks of outpatient treatment. [...] 48 non-treatment-seeking participants with AU… |
| [[17]](https://www.fda.gov/drugs/drug-safety-communications/fda-requires-safety-labeling-changes-glucagon-peptide-1-receptor-agonists-glp-1-ras-due-potential) | #96–99 | — | — | `#96` The agency is requiring application holders for all GLP-1 RA medications to add information to the Warnings and Precautions section of labeling about the poten… |
| [[19]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/209637s038lbl.pdf) | #28, #33 | #36, #101 | — | `#28` to reduce the risk of sustained eGFR decline, end-stage kidney disease and cardiovascular death in adults with type 2 diabetes mellitus and chronic kidney dise… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.nejm.org/doi/10.1056/NEJMoa2501006 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.nejm.org/doi/10.1056/NEJMoa2403347 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.ahajournals.org/doi/10.1161/CIR.0000000000001453 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-0`** [1]
  - Trecho: Semaglutide is a long-acting glucagon-like peptide-1 receptor agonist, or GLP-1RA, whose clinical effects extend well beyond appetite suppression and body-weight reduction.
  - Justificativa: A evidência confirma que semaglutide é um agonista do receptor GLP-1, possui mecanismo de protração (ligação à albumina) com meia-vida de aproximadamente 1 semana (long-acting), e seus efeitos clínicos vão além da supre…
  - Suporte veio de: [1] [1] [1] [1] [1] [1]
  - Evidência: “Semaglutide acts as a GLP-1 receptor agonist that selectively binds to and activates the GLP-1 receptor”
- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-1`** [1]
  - Trecho: Semaglutide activates the same receptor as endogenous GLP-1, increases insulin secretion and suppresses glucagon in a glucose-dependent manner, delays gastric emptying, and influences brain pathways involved in appetite…
  - Justificativa: Cada componente da afirmacao esta explicitamente sustentado pela evidencia: ativacao do receptor GLP-1 (alvo do GLP-1 nativo), estimulacao da secrecao de insulina e reducao de glucagon de forma glicose-dependente, atras…
  - Suporte veio de: [1]
  - Evidência: “Semaglutide acts as a GLP-1 receptor agonist that selectively binds to and activates the GLP-1 receptor, the target for native GLP-1.”
- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-4`** [8]
  - Trecho: Evidence for glycemic improvement and prevention of biochemical diabetes is also strong, although part of that benefit clearly tracks with weight reduction.
  - Justificativa: A evidência demonstra fortemente a melhora glicêmica (redução de HbA1c de -0,32 pontos percentuais, regressão à normoglicemia 69,5% vs 35,8%) e prevenção de diabetes bioquímico (1,5% vs 6,9%), e explicitamente afirma qu…
  - Suporte veio de: [8]
  - Evidência: “a greater proportion treated with semaglutide were normoglycemic (69.5% vs. 35.8%; P < 0.0001) and a smaller proportion had biochemical diabetes by week 156 (1.5% vs. 6.9%; P < 0.0001)”
### UNSUPPORTED

- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-2`** [1] [18]
  - Trecho: The distinction between an effect occurring *with* weight loss and an effect being *caused entirely by* weight loss is important, because several semaglutide trials have demonstrated clinically meaningful cardiovascular…
  - Justificativa: A evidência sustenta parcialmente a afirmação: confirma que o mecanismo de ação em redução de risco CV não foi estabelecido e que o mecanismo em MASH não é totalmente compreendido, podendo envolver múltiplas vias mediad…
  - Suporte veio de: [1]
  - Evidência: “The exact mechanism of semaglutide in CV risk reduction in adults has not been established.”
  - Não coberto pela evidência: Desfechos renais benéficos demonstrados em ensaios de semaglutida; Desfechos de insuficiência cardíaca demonstrados em ensaios de semaglutida; Desfechos inflamatórios demonstrados em ensaios de semaglutida
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | The exact mechanism of semaglutide in CV risk reduction in adults has not been established. |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-32`** [7]
  - Trecho: Because SELECT was not a dedicated chronic-kidney-disease outcomes trial and most participants were at substantially lower renal risk than FLOW participants, these data are supportive rather than sufficient to create a…
  - Justificativa: A evidência sustenta parcialmente os componentes factuais da afirmação: (1) SELECT não foi um ensaio dedicado a doença renal crônica (foi uma análise secundária, endpoint primário era MACE); (2) participantes do SELECT…
  - Suporte veio de: [7]
  - Evidência: “Although the effect of semaglutide on kidney outcomes was a secondary analysis of SELECT, with the primary endpoint being MACE, the analysis presented here was pre-specified.”
  - Não coberto pela evidência: Conclusão interpretativa de que os dados são 'supportive rather than sufficient to create a general kidney-prevention indication for everyone with obesity' — não está explicitamente afirmada na evidência; Afirmativa sobre 'everyone with obesity' especificamente — a evidência refere-se a 'individuals with overweight/obesity and established CVD, without diabetes', não a todos com obesidade
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-37`** [7]
  - Trecho: For a patient with obesity but no diabetes or CKD, kidney protection remains an attractive secondary benefit rather than an independent reason to prescribe semaglutide.
  - Justificativa: A evidência mostra que os desfechos renais do SELECT foram uma análise secundária (o endpoint primário foi MACE), o que sustenta parcialmente a ideia de benefício renal 'secundário'. No entanto, a afirmação especifica '…
  - Suporte veio de: [7]
  - Evidência: “Although the effect of semaglutide on kidney outcomes was a secondary analysis of SELECT, with the primary endpoint being MACE, the analysis presented here was pre-specified.”
  - Não coberto pela evidência: Especificação de paciente 'sem CKD' — o SELECT incluiu pacientes com CKD; Afirmação de que proteção renal não é 'razão independente para prescrever' — juízo clínico não explicitado na evidência; Caracterização como 'atraente benefício secundário' — termo de valor não usado na evidência
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semaglutina_saude_763e312081bf_20261115T131517Z-83`** [16]
  - Trecho: A separate small 2026 oral-semaglutide trial also found reductions in some alcohol-use outcomes despite missing its laboratory craving endpoint.
  - Justificativa: A evidência descreve um estudo com semaglutida administrada por via subcutânea ("2·4 mg subcutaneously"), não oral, contradizendo diretamente a afirmação de que seria um trial de "oral-semaglutide". Além disso, o endpoi…
  - Evidência: “once-weekly semaglutide (2·4 mg subcutaneously)”
  - Não coberto pela evidência: "oral-semaglutide" — a evidência descreve administração subcutânea, não oral; "missing its laboratory craving endpoint" — não há menção a nenhum endpoint de craving laboratorial, e o endpoint primário foi atingido; "separate" — não há contexto na evidência que indique ser um estudo separado de outro

---

## 10. Trechos Citados Não Auditados

Motivos: 11 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semaglutina_saude_763e312081bf_20261115T131517Z-14` — Referencia(s) citada(s) ['758a12e3e172f5f1'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-17` — Referencia(s) citada(s) ['1c3374f534c1ffe4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-18` — Referencia(s) citada(s) ['1c3374f534c1ffe4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-24` — Referencia(s) citada(s) ['4191e06d1a0d1528'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-25` — Referencia(s) citada(s) ['4191e06d1a0d1528'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-26` — Referencia(s) citada(s) ['4191e06d1a0d1528'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-27` — Referencia(s) citada(s) ['4191e06d1a0d1528'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-35` — Referencia(s) citada(s) ['4191e06d1a0d1528'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-104` — Referencia(s) citada(s) ['1c3374f534c1ffe4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-105` — Referencia(s) citada(s) ['1c3374f534c1ffe4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_763e312081bf_20261115T131517Z-106` — Referencia(s) citada(s) ['1c3374f534c1ffe4'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.