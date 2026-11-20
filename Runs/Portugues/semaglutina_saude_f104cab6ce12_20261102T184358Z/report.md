# Relatório de Auditoria — Gemini (semaglutina_saude_f104cab6ce12_20261102T184358Z)

**Arquivo auditado:** `answers/Gemini/Emergente/semaglutina_saude.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semaglutina_saude_f104cab6ce12_20261102T184358Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-04T03:48:46.503547+00:00 |
| **Total de trechos citados** | 55 |
| **Tempo de processamento** | 1:09:04:48 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 26.6 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-02 18:44:20+00:00 |
| Citações no corpo | 55 marcadores, 10 distintos |
| Referências listadas | 28 (18 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 36 | 65.5% |
| **UNSUPPORTED** | 15 | 27.3% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 4 | 7.3% |
| **TOTAL** | 55 | 100.0% |

Sobre os 51 trechos citados auditados: SUPPORTED 70,58%, UNSUPPORTED 29,41%, CONTRADICTED 0,00%.

> **15 dos 36 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 15 estão **contados dentro** dos 36 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`16` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `3` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `1` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `6` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#7` O desfecho composto de insuficiência cardíaca, compreendido por morte cardiovascular ou hospitalização/visita médica de… | [1] | [4] [8] [2] [6] https://pubmed.ncbi.nlm.nih.gov/37952131/ [7] [10] | — |
| `#12` Do ponto de vista hemodinâmico, o estudo SELECT registrou uma redução média sustentada na pressão arterial sistólica de… | [1] | [7] [8] https://pubmed.ncbi.nlm.nih.gov/37952131/ [6] [17] [4] [2] | — |
| `#21` Além disso, a semaglutida atenuou a taxa de perda anual da função renal, preservando a TFGe em um valor médio de 1,16 m… | [7] | [8] [10] [11] [1] [12] [15] [13] | — |
| `#23` No âmbito hemodinâmico, os receptores de GLP-1 expressos no túbulo contorcido proximal modulam a atividade do trocador… | [7] | [8] [6] [1] [12] https://pubmed.ncbi.nlm.nih.gov/37952131/ [17] [25] [4] [2] | — |
| `#30` Os estudos foram desenhados como ensaios randomizados, duplo-cegos e controlados por placebo, englobando 3.808 paciente… | [17] | [21] [18] [1] [8] | — |
| `#46` A avaliação do perfil de segurança da semaglutida em populações não diabéticas e diabéticas expostas a doses de até 2,4… | [1] | [13] [8] https://pubmed.ncbi.nlm.nih.gov/37952131/ [2] [15] [14] [10] [4] [11] [12] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 458027 |
| **Média de tokens por requisição** | 8980.9 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 18/28 (64.3%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/11/09/15/04/select) | downloaded | 20 | 14 | 5 | 1 | 0 |
| [[7]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | downloaded | 11 | 7 | 3 | 1 | 0 |
| [[17]](https://pandapeptide.ca/peptide-blog/semaglutide-and-alzheimers/) | downloaded | 9 | 7 | 2 | 0 | 0 |
| [[22]](https://neurologytoday.aan.com/doi/10.1212/breakingnews.1444) | blocked | 4 | 0 | 0 | 0 | 4 |
| [[12]](https://gi.org/journals-publications/ebgi/kwo_sep2025/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[6]](https://www.news-medical.net/news/20251026/Semaglutide-protects-the-heart-beyond-weight-loss-SELECT-trial-shows.aspx) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[13]](https://pace-cme.org/news/phase-3-trial-results-of-semaglutide-in-mash-with-liver-fibrosis/2475390/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[23]](https://pubmed.ncbi.nlm.nih.gov/38598572/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[5]](https://sciencehub.novonordisk.com/scientific-publications/articles/original-article.NN19a58b3e511.semaglutide-and-cardiovascular-outcomes-by.html) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[24]](https://www.ovid.com/journals/nejm/pdf/10.1056/nejmoa2312323~trial-of-lixisenatide-in-early-parkinsons-disease) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[2]](https://www.cardionerds.com/cardsjc-semaglutide-and-cardiovascular-outcomes-in-obesity-without-diabetes-select-trial/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[3]](https://franquia.sergios.com.br/select-trial-semaglutide-cv-outcomes-pro/) | error | 0 · nunca citada | — | — | — | — |
| [[4]](https://pubmed.ncbi.nlm.nih.gov/39181597/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[8]](http://www.nephjc.com/news/flow) | downloaded | 0 · nunca citada | — | — | — | — |
| [[9]](https://franquia.sergios.com.br/flow-trial-semaglutide-chronic-kidney-disease-line/) | error | 0 · nunca citada | — | — | — | — |
| [[10]](https://pubmed.ncbi.nlm.nih.gov/38785209/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[11]](https://www.theisn.org/in-action/research/clinical-trials-isn-act-archive/the-flow-study-effects-of-semaglutide-on-chronic-kidney-disease-in-patients-with-type-2-diabetes/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[14]](https://www.biochempeg.com/article/416.html) | downloaded | 0 · nunca citada | — | — | — | — |
| [[15]](https://www.prnewswire.com/news-releases/essence-phase-3-trial-results-demonstrating-statistically-significant-and-superior-improvements-with-semaglutide-2-4-mg-in-people-with-mash-presented-at-aasld-2024--the-liver-meeting-302310474.html) | downloaded | 0 · nunca citada | — | — | — | — |
| [[16]](https://www.springermedicine.com/metabolic-dysfunction-associated-steatohepatitis/semaglutide/essence-trial-reduces-liver-fibrosis-steatohepatitis-mash/50971388) | downloaded | 0 · nunca citada | — | — | — | — |
| [[18]](https://pubmed.ncbi.nlm.nih.gov/41522368/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://www.researchgate.net/publication/387830143_evoke_and_evoke_design_of_two_large-scale_double-blind_placebo-controlled_phase_3_studies_evaluating_efficacy_safety_and_tolerability_of_semaglutide_in_early-stage_symptomatic_Alzheimer's_disease) | error | 0 · nunca citada | — | — | — | — |
| [[20]](https://www.neurology.org/doi/10.1212/WNL.0000000000216975) | blocked | 0 · nunca citada | — | — | — | — |
| [[21]](https://www.alz.org/news/2025/alzheimers-association-statement-oral-semaglutide-phase-3-topline-data-release) | downloaded | 0 · nunca citada | — | — | — | — |
| [[25]](https://www.michaeljfox.org/news/results-parkinsons-trial-diabetes-drug-lixisenatide-published) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://www.parkinsons.org.uk/news/2024/results-phase-2-trial-lixisenatide-have-been-published) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://pubmed.ncbi.nlm.nih.gov/37952131/](https://pubmed.ncbi.nlm.nih.gov/37952131/) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.ovid.com/journals/nejm/fulltext/10.1056/nejmc2410532~semaglutide-for-chronic-kidney-disease-in-type-2-diabetes](https://www.ovid.com/journals/nejm/fulltext/10.1056/nejmc2410532~semaglutide-for-chronic-kidney-disease-in-type-2-diabetes) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://www.acc.org/latest-in-cardiology/clinical-trials/2023/11/09/15/04/select) | #0–6, #8, #44–45, #48–50, #52 | #7, #12, #46, #51, #53 | #47 | `#0` The SELECT trial extends the findings of SUSTAIN-6 and other GLP-1 RA trials, which have demonstrated CV benefit in DM, to this increased-risk population. [...… |
| [[7]](https://www.acc.org/latest-in-cardiology/clinical-trials/2024/05/29/17/23/flow) | #14–16, #18–20, #22 | #13, #17, #21 | #23 | `#14` Total randomized participants: 3,533 [...] High-risk CKD (estimated glomerular filtration rate [eGFR] 25-75 mL/min/1.73 m2 with a urinary albumin-to-creatinine… |
| [[17]](https://pandapeptide.ca/peptide-blog/semaglutide-and-alzheimers/) | #29, #31, #33–37 | #30, #32 | — | `#29` Semaglutide and Alzheimer's research now includes results from two phase 3 trials involving 3,808 adults with early symptomatic disease. At 104 weeks, oral sem… |
| [[12]](https://gi.org/journals-publications/ebgi/kwo_sep2025/) | #24–25, #28 | — | — | `#24` The Essence trial provides strong evidence that semaglutide can also effectively treat MASH with fibrosis, a severe form of liver disease that is closely linke… |
| [[6]](https://www.news-medical.net/news/20251026/Semaglutide-protects-the-heart-beyond-weight-loss-SELECT-trial-shows.aspx) | #10–11 | — | — | `#10` In the semaglutide arm, there was no linear or non-linear trend in subsequent MACE risk by the amount of weight loss at week 20 |
| [[13]](https://pace-cme.org/news/phase-3-trial-results-of-semaglutide-in-mash-with-liver-fibrosis/2475390/) | #27 | #26 | — | `#27` resolution of steatohepatitis with no worsening of liver fibrosis (first primary endpoint) was observed in 62.9% of the 534 patients treated with semaglutide a… |
| [[23]](https://pubmed.ncbi.nlm.nih.gov/38598572/) | #41–42 | — | — | `#41` The primary end point was the change from baseline in scores on the Movement Disorder Society-Unified Parkinson's Disease Rating Scale (MDS-UPDRS) part III (ra… |
| [[5]](https://sciencehub.novonordisk.com/scientific-publications/articles/original-article.NN19a58b3e511.semaglutide-and-cardiovascular-outcomes-by.html) | — | — | #9 | — |
| [[24]](https://www.ovid.com/journals/nejm/pdf/10.1056/nejmoa2312323~trial-of-lixisenatide-in-early-parkinsons-disease) | — | #54 | — | `#54` Nausea occurred in 46% of participants receiving lixisenatide, and vomiting occurred in 13%. |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.neurology.org/doi/10.1212/WNL.0000000000216975 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://neurologytoday.aan.com/doi/10.1212/breakingnews.1444 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-0`** [1]
  - Trecho: A caracterização da semaglutida como um agente capaz de modificar a história natural da doença cardiovascular aterosclerótica em populações sem diabetes foi consolidada pelos resultados do ensaio clínico landmark SELECT.
  - Justificativa: A evidência descreve o ensaio SELECT como demonstrando benefício cardiovascular (redução de 20% em MACE) em pacientes com sobrepeso/obesidade e doença cardiovascular estabelecida sem diabetes, estendendo achados anterio…
  - Suporte veio de: [1]
  - Evidência: “The SELECT trial extends the findings of SUSTAIN-6 and other GLP-1 RA trials, which have demonstrated CV benefit in DM, to this increased-risk population.”
  - Não coberto pela evidência: O termo 'landmark' não aparece literalmente na evidência, sendo uma caracterização interpretativa.; A expressão exata 'modificar a história natural da doença' não é usada literalmente na evidência, embora o conceito seja inferível a partir da descrição de papel expandido na prevenção secundária.
- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-1`** [1]
  - Trecho: Trata-se de um estudo multicêntrico, internacional, duplo-cego, randomizado e controlado por placebo que incluiu 17.604 pacientes com idade igual ou superior a 45 anos, apresentando índice de massa corporal (IMC) de pel…
  - Justificativa: Todos os elementos da afirmação estão explicitamente sustentados pela evidência: design do estudo (multicêntrico, internacional, duplo-cego, randomizado, controlado por placebo), número de pacientes (17.604), critérios…
  - Suporte veio de: [1]
  - Evidência: “Randomized - International multicenter - Double-blind - Placebo-controlled”
- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-2`** [1]
  - Trecho: Os participantes foram randomizados para receber semaglutida subcutânea na dose semanal de 2,4 mg ou placebo, adicionados ao tratamento padrão de prevenção secundária cardiovascular, que incluía estatinas em 88% dos ind…
  - Justificativa: A evidência confirma todos os elementos essenciais da afirmação: randomização para semaglutida subcutânea semanal vs. placebo, dose-alvo de 2.4 mg, contexto de prevenção secundária cardiovascular, e uso de estatinas em…
  - Suporte veio de: [1]
  - Evidência: “Patients with overweight or obesity (body mass index [BMI] ≥27 kg/m²) and established CVD were randomized to receive once-weekly subcutaneous semaglutide (n = 8,803) vs. placebo (n = 8,801).”
  - Não coberto pela evidência: A afirmação diz 'na dose semanal de 2,4 mg' sem mencionar que era uma dose-alvo com titulação gradual (iniciada em 0,24 mg e aumentada a cada 4 semanas), nem que apenas 77% atingiram a dose-alvo.
### UNSUPPORTED

- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-7`** [1]
  - Trecho: O desfecho composto de insuficiência cardíaca, compreendido por morte cardiovascular ou hospitalização/visita médica de urgência por insuficiência cardíaca, sofreu uma redução de 18% (3,4% no grupo semaglutida versus 4,…
  - Justificativa: Os números centrais da afirmação (3,4% vs 4,1%; HR 0,82; IC 95% 0,71-0,96) e a redução de 18% (inferível diretamente de HR 0,82) estão explicitamente sustentados pela evidência. Contudo, a afirmação descreve o desfecho…
  - Suporte veio de: [1]
  - Evidência: “HF composite outcome, CV death or HF hospitalization, for semaglutide vs. placebo: 3.4% vs. 4.1% (HR 0.82, 95% CI 0.71-0.96)”
  - Não coberto pela evidência: 'visita médica de urgência por insuficiência cardíaca' como parte do desfecho composto — a evidência menciona apenas 'HF hospitalization', sem referência a visitas médicas de urgência
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [4] [8] [2] [6] fe4fe99e25e4d1b5 [7] [10] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-9`** [5]
  - Trecho: Análises secundárias detalhadas do estudo SELECT focadas nas variações de adiposidade basal e durante o tratamento demonstraram que a redução do risco de MACE foi mantida de forma homogênea em todos os decis de IMC basa…
  - Justificativa: A evidência fornecida é apenas uma descrição genérica do portal Science Hub da Novo Nordisk, sem qualquer menção ao estudo SELECT, MACE, IMC, circunferência da cintura ou análises secundárias. Não há informação suficien…
  - Não coberto pela evidência: análises secundárias do estudo SELECT; variações de adiposidade basal e durante o tratamento; redução do risco de MACE
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semaglutina_saude_f104cab6ce12_20261102T184358Z-12`** [1]
  - Trecho: Do ponto de vista hemodinâmico, o estudo SELECT registrou uma redução média sustentada na pressão arterial sistólica de 3,8 mmHg no grupo semaglutida versus 0,5 mmHg no grupo placebo na semana 104.
  - Justificativa: A evidência confirma os valores numéricos da redução da pressão arterial sistólica (–3.8 vs. –0.5 mmHg) para semaglutida vs. placebo, mas não explicita que essa medida foi na semana 104 (o marcador 'at 104 weeks' aparec…
  - Suporte veio de: [1]
  - Evidência: “Change in systolic blood pressure: –3.8 vs. –0.5 mm Hg”
  - Não coberto pela evidência: Afirmar que a medida de pressão arterial foi na semana 104 (a evidência só associa 'at 104 weeks' à mudança de peso, não à pressão arterial); Caracterizar a redução como 'sustentada' (a evidência não usa esse termo nem indica sustentabilidade temporal)
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [7] [8] fe4fe99e25e4d1b5 [6] [17] [4] [2] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 4 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semaglutina_saude_f104cab6ce12_20261102T184358Z-38` — Referencia(s) citada(s) ['d028cc9ae1f893dd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_f104cab6ce12_20261102T184358Z-39` — Referencia(s) citada(s) ['d028cc9ae1f893dd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_f104cab6ce12_20261102T184358Z-40` — Referencia(s) citada(s) ['d028cc9ae1f893dd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semaglutina_saude_f104cab6ce12_20261102T184358Z-43` — Referencia(s) citada(s) ['d028cc9ae1f893dd'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.