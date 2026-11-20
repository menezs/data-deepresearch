# Relatório de Auditoria — ChatGPT (semaglutina_saude_85364a75d53b_20261102T190705Z)

**Arquivo auditado:** `answers/ChatGPT/Emergente/semaglutina_saude.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_85364a75d53b_20261102T190705Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T10:36:35.945583+00:00 |
| **Total de trechos citados** | 109 |
| **Tempo de processamento** | 1:10:52:08 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 38.7 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 159 marcadores, 26 distintos |
| Referências listadas | 26 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 68 | 62.4% |
| **UNSUPPORTED** | 35 | 32.1% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 6 | 5.5% |
| **TOTAL** | 109 | 100.0% |

Sobre os 103 trechos citados auditados: SUPPORTED 66,01%, UNSUPPORTED 33,98%, CONTRADICTED 0,00%.

> **29 dos 68 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 29 estão **contados dentro** dos 68 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`43` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `9` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `8` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `7` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 8.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#8` Estudos observacionais sugeriram menor incidência de déficits cognitivos ou diagnósticos de demência entre usuários de… | [14] | [13] [3] [1] [20] [6] [7] [21] [17] [4] | — |
| `#11` Náuseas, vômitos, diarreia, constipação e dor abdominal são os eventos mais frequentes e são relacionados em parte à do… | [7] | [20] [25] [21] [6] [3] | — |
| `#16` A semaglutida é um análogo de GLP-1 resistente à rápida degradação, com ativação prolongada do GLP-1R, e sua farmacolog… | [20] | [1] [21] [14] [2] [7] [19] [9] | — |
| `#43` Semaglutida oral 14 mg reduziu o risco de MACE em aproximadamente 14%, HR 0,86 (IC95% 0,77–0,96), durante seguimento pr… | [6] | [10] [5] [4] [20] [14] [3] [9] [13] | — |
| `#46` Os lipídios apresentam padrão semelhante: estudos do programa STEP documentaram melhora de triglicerídeos e de medidas… | [9] | [21] [1] [25] [18] [2] [20] | — |
| `#86` Tanto o agonismo de GLP-1 quanto a perda rápida de peso podem contribuir para esse risco, tornando especialmente releva… | [18] | [21] [25] [1] [16] [8] [2] [7] [9] | — |
| `#107` Reduções de eventos cardiovasculares em diabetes e obesidade, proteção renal em diabetes com DRC, melhora glicêmica e p… | [3] [4] [5] [10] [11] | [2] [21] [19] [6] [9] [12] [20] [16] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1901754 |
| **Média de tokens por requisição** | 18463.6 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/26 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[20]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/209637s025lbl.pdf) | downloaded | 25 | 13 | 11 | 0 | 1 |
| [[4]](https://pubmed.ncbi.nlm.nih.gov/37952131/) | downloaded | 12 | 3 | 7 | 2 | 0 |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/40305708/) | downloaded | 12 | 3 | 5 | 3 | 1 |
| [[10]](https://pubmed.ncbi.nlm.nih.gov/42610271/) | downloaded | 10 | 3 | 6 | 1 | 0 |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/38785209/) | downloaded | 9 | 3 | 5 | 1 | 0 |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/41865758/) | downloaded | 9 | 3 | 4 | 2 | 0 |
| [[21]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/215256s033lbl.pdf) | downloaded | 9 | 8 | 1 | 0 | 0 |
| [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6314963/) | downloaded | 8 | 1 | 7 | 0 | 0 |
| [[3]](https://pubmed.ncbi.nlm.nih.gov/27633186/) | downloaded | 8 | 3 | 5 | 0 | 0 |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/39764175/) | downloaded | 7 | 1 | 3 | 3 | 0 |
| [[22]](https://pubmed.ncbi.nlm.nih.gov/42825923/) | downloaded | 7 | 3 | 1 | 2 | 1 |
| [[1]](https://insight.jci.org/articles/view/133429) | downloaded | 6 | 0 | 4 | 2 | 0 |
| [[15]](https://pubmed.ncbi.nlm.nih.gov/37531876/) | downloaded | 6 | 1 | 3 | 2 | 0 |
| [[7]](https://pubmed.ncbi.nlm.nih.gov/33667417/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[8]](https://pubmed.ncbi.nlm.nih.gov/39217502/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/36200477/) | downloaded | 3 | 0 | 2 | 0 | 1 |
| [[16]](https://pubmed.ncbi.nlm.nih.gov/38018310/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/38555109/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[18]](https://pubmed.ncbi.nlm.nih.gov/35344001/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[19]](https://pubmed.ncbi.nlm.nih.gov/29178519/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[23]](https://academic.oup.com/eurheartj/article/44/39/4043/7238227) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[6]](https://pubmed.ncbi.nlm.nih.gov/40162642/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[24]](https://diabetesjournals.org/care/article/49/Supplement_1/S183/163934/9-Pharmacologic-Approaches-to-Glycemic-Treatment) | blocked | 2 | 0 | 0 | 0 | 2 |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/41201884/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://pubmed.ncbi.nlm.nih.gov/33567185/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://www.journal-of-hepatology.eu/article/S0168-8278(24)00329-5/fulltext) | blocked | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[20]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/209637s025lbl.pdf) | #7, #28, #35, #50, #71, #74, #79–82, #92, #94, #99 | #12, #16–18, #72, #84–85, #87, #89–90, #98 | #100 (pulado) | `#7` to reduce the risk of sustained eGFR decline, end-stage kidney disease and cardiovascular death in adults with type 2 diabetes mellitus and chronic kidney dise… |
| [[4]](https://pubmed.ncbi.nlm.nih.gov/37952131/) | #4, #38–39 | #0, #5, #25, #40–41, #95, #107 | #2, #101 | `#4` A total of 17,604 patients were enrolled; 8803 were assigned to receive semaglutide and 8801 to receive placebo. The mean (±SD) duration of exposure to semaglu… |
| [[11]](https://pubmed.ncbi.nlm.nih.gov/40305708/) | #55–57 | #0, #54, #58, #95, #107 | #14, #29–30, #53 (pulado) | `#55` In this ongoing phase 3, multicenter, randomized, double-blind, placebo-controlled trial, we assigned 1197 patients with biopsy-defined MASH and fibrosis stage… |
| [[10]](https://pubmed.ncbi.nlm.nih.gov/42610271/) | #32–33, #63 | #1, #5, #31, #62, #102, #107 | #101 | `#32` Semaglutide reduced hsCRP levels (-37.8% [104 weeks]) and risk of MACE across all hsCRP subgroups. [...] Modeling suggests decreased inflammation as contributi… |
| [[5]](https://pubmed.ncbi.nlm.nih.gov/38785209/) | #6, #48–49 | #0, #14, #27, #95, #107 | #26 | `#6` The risk of a primary-outcome event was 24% lower in the semaglutide group than in the placebo group (331 vs. 410 first events; hazard ratio, 0.76; 95% confide… |
| [[13]](https://pubmed.ncbi.nlm.nih.gov/41865758/) | #9, #67, #103 | #10, #66, #68, #108 | #22, #106 | `#9` 3808 were randomly assigned; 1855 in evoke (semaglutide, n=928; placebo, n=927) and 1953 in evoke+ (semaglutide, n=976; placebo, n=977). [...] oral semaglutide… |
| [[21]](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/215256s033lbl.pdf) | #59, #71, #75, #80, #92–94, #99 | #60 | — | `#59` for the treatment of noncirrhotic metabolic dysfunction-associated steatohepatitis (MASH), formerly known as nonalcoholic steatohepatitis (NASH), with moderate… |
| [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6314963/) | #23 | #1–2, #24–25, #31, #62, #108 | — | `#23` In 2 murine models of atherosclerosis (ApoE−/− and LDLr−/−), liraglutide and semaglutide showed significant reductions of aortic plaque areas, at least partial… |
| [[3]](https://pubmed.ncbi.nlm.nih.gov/27633186/) | #3, #36–37 | #0, #25, #87, #95, #107 | — | `#3` We randomly assigned 3297 patients with type 2 diabetes who were on a standard-care regimen to receive once-weekly semaglutide (0.5 mg or 1.0 mg) or placebo fo… |
| [[14]](https://pubmed.ncbi.nlm.nih.gov/39764175/) | #64 | #8, #10, #68 | #65, #105–106 | `#64` Semaglutide was not associated with an increased risk of neurological and psychiatric outcomes. Instead, after multiple-testing correction, semaglutide was ass… |
| [[22]](https://pubmed.ncbi.nlm.nih.gov/42825923/) | #15, #52, #96 | #51 | #14, #98, #100 (pulado) | `#15` This update has broadened the focus from the management of hyperglycaemia to the holistic management of type 2 diabetes and its risk of associated multiple lon… |
| [[1]](https://insight.jci.org/articles/view/133429) | — | #1, #19–21 | #2, #22 | `#1` Semaglutide, a glucagon-like peptide 1 (GLP-1) analog, induces weight loss, lowers glucose levels, and reduces cardiovascular risk in patients with diabetes. |
| [[15]](https://pubmed.ncbi.nlm.nih.gov/37531876/) | #69 | #72, #104, #108 | #73, #106 | `#69` Data from 37 RCTs and 19 real-world studies [...] Compared to placebo, occurrence of pancreatic cancer [OR 0.25 (95%CI: 0.03-2.24); P = 0.21], thyroid cancer [… |
| [[7]](https://pubmed.ncbi.nlm.nih.gov/33667417/) | #76–77 | #11 | — | `#76` Estimated change in mean bodyweight from baseline to week 68 was -9·6% (SE 0·4) with semaglutide 2·4 mg vs -3·4% (0·4) with placebo. Estimated treatment differ… |
| [[8]](https://pubmed.ncbi.nlm.nih.gov/39217502/) | #44 | #1, #45 | — | `#44` The difference in SBP change between the treatment (n = 2109) and placebo (n = 1027) groups was -4.95 mmHg [95% confidence interval (CI) -5.86 to -4.05] overal… |
| [[9]](https://pubmed.ncbi.nlm.nih.gov/36200477/) | — | #1, #46 | #47 (pulado) | `#1` reductions in waist circumference, SBP, DBP, FPG, fasting serum insulin, lipids and HOMA-IR were greater with semaglutide versus placebo |
| [[16]](https://pubmed.ncbi.nlm.nih.gov/38018310/) | #70 | #72, #104 | — | `#70` Our meta-analysis showed that GLP-1RA treatment could be associated with a moderate increase in relative risk for thyroid cancer in clinical trials, with a sma… |
| [[17]](https://pubmed.ncbi.nlm.nih.gov/38555109/) | #83 | #12, #84 | — | `#83` This updated meta-analysis demonstrates that the use of semaglutide is not associated with an increased risk of acute pancreatitis compared to placebo. In the… |
| [[18]](https://pubmed.ncbi.nlm.nih.gov/35344001/) | #13 | #85–86 | — | `#13` A total of 76 RCTs [...] were included. [...] randomization to GLP-1 RA treatment was associated with increased risks of gallbladder or biliary diseases (RR, 1… |
| [[19]](https://pubmed.ncbi.nlm.nih.gov/29178519/) | #88–89 | #98 | — | `#88` The majority of the effect with semaglutide vs placebo in SUSTAIN 6 may be attributed to the magnitude and rapidity of HbA1c reduction during the first 16 week… |
| [[6]](https://pubmed.ncbi.nlm.nih.gov/40162642/) | #42 | #43 | — | `#42` Funded by Novo Nordisk; SOUL ClinicalTrials.gov number, NCT03914326. ... Among the 9650 participants who had undergone randomization ... had type 2 diabetes ..… |
| [[12]](https://pubmed.ncbi.nlm.nih.gov/41201884/) | #61 | — | — | `#61` This practice recommendation serves as an update to the 2023 AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver dise… |
| [[25]](https://pubmed.ncbi.nlm.nih.gov/33567185/) | #78 | — | — | `#78` The mean change in body weight from baseline to week 68 was -14.9% in the semaglutide group as compared with -2.4% with placebo |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://academic.oup.com/eurheartj/article/44/39/4043/7238227 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://diabetesjournals.org/care/article/49/Supplement_1/S183/163934/9-Pharmacologic-Approaches-to-Glycemic-Treatment — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.journal-of-hepatology.eu/article/S0168-8278(24)00329-5/fulltext — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-0`** [3] [4] [5] [11]
  - Trecho: A semaglutida é um agonista do receptor do peptídeo semelhante ao glucagon tipo 1 (GLP-1) cujo efeito clínico não se limita à redução do peso: ela melhora a glicemia, reduz eventos cardiovasculares maiores em populações…
  - Justificativa: A evidência sustenta explicitamente os elementos essenciais da afirmação: semaglutida como agonista do receptor GLP-1, redução de eventos cardiovasculares maiores em populações de alto risco (SUSTAIN-6 e SELECT), retard…
  - Suporte veio de: [11] [4] [3] [5]
  - Evidência: “Semaglutide, a glucagon-like peptide-1 receptor agonist, is a candidate for the treatment of metabolic dysfunction-associated steatohepatitis (MASH).”
  - Não coberto pela evidência: melhora a glicemia — não há menção explícita a melhora da glicemia na evidência fornecida; atualmente denominada MASH e anteriormente NASH — a evidência menciona MASH mas não afirma explicitamente que era anteriormente chamada NASH
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [11] | parcial | Semaglutide, a glucagon-like peptide-1 receptor agonist, is a candidate for the treatment of metabolic dysfunction-asso… |
    | [4] | parcial | Semaglutide, a glucagon-like peptide-1 receptor agonist, has been shown to reduce the risk of adverse cardiovascular ev… |
    | [3] | parcial | In patients with type 2 diabetes who were at high cardiovascular risk, the rate of cardiovascular death, nonfatal myoca… |
    | [5] | parcial | Semaglutide reduced the risk of clinically important kidney outcomes and death from cardiovascular causes in patients w… |

- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-3`** [3]
  - Trecho: No SUSTAIN-6, realizado em 3.297 pessoas com diabetes tipo 2 e alto risco cardiovascular, semaglutida subcutânea 0,5 ou 1,0 mg/semana reduziu o desfecho composto de morte cardiovascular, infarto não fatal ou AVC não fat…
  - Justificativa: A evidência sustenta explicitamente todos os elementos essenciais da afirmação: 3.297 pacientes com diabetes tipo 2 e alto risco cardiovascular, semaglutida 0,5 ou 1,0 mg semanal, redução do desfecho composto de 8,9% (p…
  - Suporte veio de: [3]
  - Evidência: “We randomly assigned 3297 patients with type 2 diabetes who were on a standard-care regimen to receive once-weekly semaglutide (0.5 mg or 1.0 mg) or placebo for 104 weeks.”
  - Não coberto pela evidência: Via de administração subcutânea não é explicitamente mencionada na evidência (apenas 'once-weekly semaglutide (0.5 mg or 1.0 mg)')
- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-4`** [4]
  - Trecho: No SELECT, 17.604 adultos com sobrepeso ou obesidade, doença cardiovascular estabelecida e sem diabetes receberam semaglutida 2,4 mg/semana ou placebo; após seguimento médio de 39,8 meses, eventos cardiovasculares maior…
  - Justificativa: A evidência confirma explicitamente todos os elementos da afirmação: número de pacientes (17.604), perfil (sobrepeso/obesidade, doença cardiovascular pré-existente, sem diabetes), dose (2,4 mg/semana vs placebo), seguim…
  - Suporte veio de: [4]
  - Evidência: “A total of 17,604 patients were enrolled”
### UNSUPPORTED

- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-1`** [1] [2] [8] [9] [10]
  - Trecho: Os efeitos decorrem de uma combinação de menor ingestão energética e adiposidade, melhora da resistência à insulina e da hiperglicemia, redução da pressão arterial e de lipídios aterogênicos, alterações no esvaziamento…
  - Justificativa: A evidência sustenta vários elementos individuais da alegação: menor ingestão energética e adiposidade (cd5e92f80b4dc387), melhora da resistência à insulina/hiperglicemia (71b015cf64d48aaf — HOMA-IR, FPG), redução da pr…
  - Suporte veio de: [9] [1] [8] [10] [2]
  - Evidência: “semaglutide dose-dependently reduced BW and suppressed food intake”
  - Não coberto pela evidência: Alegação de que os efeitos derivam de uma combinação destes mecanismos (síntese causal combinada não explicitada na evidência); Alterações no esvaziamento gástrico para semaglutida (evidência refere apenas lixisenatida/liraglutida numa citação bibliográfica); Sinalização cardiorrenal (não mencionada em nenhuma parte da evidência)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | parcial | Semaglutide, a glucagon-like peptide 1 (GLP-1) analog, induces weight loss, lowers glucose levels, and reduces cardiova… |
    | [2] | parcial | GLP-1RAs lower BW by suppressing food intake |
    | [8] | parcial | Reduction in SBP was mediated substantially by weight loss. |
    | [9] | parcial | reductions in waist circumference, SBP, DBP, FPG, fasting serum insulin, lipids and HOMA-IR were greater with semagluti… |
    | [10] | parcial | Modeling suggests decreased inflammation as contributing in part to the benefits seen with semaglutide in SELECT. |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-2`** [1] [2] [4]
  - Trecho: Entretanto, os ensaios clínicos de desfechos não permitem separar perfeitamente efeitos “diretos” do GLP-1R daqueles mediados por emagrecimento, melhor controle glicêmico ou mudança de outros fatores de risco; alegações…
  - Justificativa: A evidência discute mecanismos pré-clínicos de GLP-1RAs (neural, anti-inflamatório, antiaterosclerótico) e menciona que alguns efeitos são 'parcialmente independentes' ou 'independentes' de perda de peso, mas não afirma…
  - Não coberto pela evidência: A afirmação de que ensaios clínicos de desfechos não permitem separar perfeitamente efeitos 'diretos' do GLP-1R daqueles mediados por emagrecimento, controle glicêmico ou mudança de outros fatores de risco; A recomendação de que alegações de pleiotropia devem ser graduadas conforme o nível de evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [1] | ausente | — |
    | [2] | parcial | This attenuation was partly independent of weight and cholesterol lowering. |
    | [4] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_85364a75d53b_20261102T190705Z-5`** [4] [10]
  - Trecho: O SELECT é uma demonstração importante de que a proteção cardiovascular não depende da presença de diabetes, mas não prova que seja independente do emagrecimento, pois perda de peso, inflamação, pressão, metabolismo lip…
  - Justificativa: A evidência sustenta que SELECT demonstrou redução de MACE em pacientes sem diabetes, confirmando que a proteção cardiovascular não depende da presença de diabetes. A evidência também mostra que múltiplos mediadores mud…
  - Suporte veio de: [10] [4]
  - Evidência: “In SELECT (Semaglutide Effects on Heart Disease and Stroke in Patients With Overweight or Obesity), among 17 604 patients with known atherosclerotic cardiovascular disease and overweight or obesity, but not diabetes, ra…”
  - Não coberto pela evidência: Pressão arterial como mediador que mudou simultaneamente após a randomização em SELECT; A afirmação interpretativa de que SELECT 'não prova independência do emagrecimento' — a evidência não explicita essa conclusão; Metabolismo lipídico como mediador que mudou (a evidência menciona LDL e estatinas como fatores independentes das mudanças de hsCRP, mas não confirma que o metabolismo lipídico mudou após randomização)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [4] | parcial | In patients with preexisting cardiovascular disease and overweight or obesity but without diabetes, weekly subcutaneous… |
    | [10] | parcial | among 17 604 patients with known atherosclerotic cardiovascular disease and overweight or obesity, but not diabetes, ra… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semaglutina_saude_85364a75d53b_20261102T190705Z-34` — Referencia(s) citada(s) ['586e8f68c77b6817'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_85364a75d53b_20261102T190705Z-91` — Referencia(s) citada(s) ['586e8f68c77b6817'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_85364a75d53b_20261102T190705Z-97` — Referencia(s) citada(s) ['53f6a43a20c76c40'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_85364a75d53b_20261102T190705Z-47` — Parte das fontes citadas sem conteudo: referencia(s) ['53f6a43a20c76c40'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_85364a75d53b_20261102T190705Z-53` — Parte das fontes citadas sem conteudo: referencia(s) ['b4422f8db869546f'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `semaglutina_saude_85364a75d53b_20261102T190705Z-100` — Parte das fontes citadas sem conteudo: referencia(s) ['53f6a43a20c76c40'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.