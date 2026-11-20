[referencia=14d93332dc180e13 score=0.744]
## Checklist de política institucional de uso de IA

| Item | O que verificar | Por quê | 
|---|---|---|
| Inventário de sistemas de IA em uso | Inclusive os que chegaram por fora do time de TI | Uma equipe clínica que já usa um assistente por conta própria é um risco não mapeado | 
| Base legal documentada | Uma base do art. 7º/11 da LGPD para cada tratamento envolvido | Sem base legal, o tratamento é irregular desde o início | 
| Avaliação de impacto (RIPD) | Para sistemas que tocam decisão clínica ou dado sensível em volume | Exigível pela ANPD em cenários de alto risco | 
| Classificação regulatória | O sistema se enquadra como SaMD? Precisa de registro na ANVISA? | Define se a RDC 657/2022 se aplica | 
| Responsável humano nomeado | Para cada decisão assistida por IA, com registro em prontuário | Exigência da Res. CFM 2.454/2026 | 
| Canal de revisão | Rota para o paciente contestar uma decisão automatizada | Direito do art. 20 da LGPD | 
| Rota de atualização | Quem revisa a política quando o marco legal for sancionado ou a RDC 657 concluir a revisão | Duas das quatro camadas ainda estão em movimento | 

Nenhum desses itens é um evento único. É uma política viva, porque pelo menos duas das quatro camadas — a ANVISA e o marco legal — ainda estão em movimento.

*Esse é o fundamento da oferta de Governança e conformidade de IA da Sciereli — política institucional, RIPD e mapeamento regulatório sob medida para a sua instituição. Fale com a gente: [email protected].*

---

[referencia=14d93332dc180e13 score=0.301]
## Camada 4 — O marco legal de IA (ainda em tramitação)

O PL 2338/2023, conhecido como Marco Legal da Inteligência Artificial, foi aprovado pelo Senado em dezembro de 2024 e segue em tramitação na Câmara dos Deputados — **ainda não é lei** em agosto de 2026 [5]. O texto adota um modelo de classificação por risco (inspirado no AI Act europeu), cria o Sistema Nacional de Regulação e Governança de IA (SIA), estabelece direitos de transparência e contestação para sistemas de alto risco — categoria em que um sistema de IA clínica provavelmente se enquadraria — e prevê sanções de até R$ 50 milhões por infração, se e quando o marco for sancionado [5]. Vale acompanhar, mas não vale tratar como obrigação vigente: essa é uma camada que ainda muda de forma.

### Onde cada camada está hoje

| Camada | Instrumento | Status em ago/2026 | 
|---|---|---|
| Proteção de dados | LGPD + Nota Técnica ANPD 12/2025 | Vigente | 
| Regulação sanitária | RDC 657/2022 (ANVISA) | Vigente, revisão parcial em curso (SaMD adaptativo, PCCP) | 
| Ética profissional | CFM 2.454/2026 e 2.314/2022 | Vigente | 
| Marco legal de IA | PL 2338/2023 | Em tramitação na Câmara — não é lei |

---

[referencia=14d93332dc180e13 score=0.110]
# Governança de IA em saúde no Brasil: o mapa prático

Carlos Avila · 30 de julho de 2026 · 5 min de leitura

ia-em-saude lgpd seguranca

Quando uma instituição de saúde decide adotar IA, a primeira pergunta certa não é “qual modelo?” — é “sob quantas autoridades diferentes esse projeto vai responder?”. No Brasil, em 2026, são pelo menos quatro, e elas não se substituem umas às outras.

## Camada 1 — Proteção de dados: LGPD e ANPD

Todo dado de saúde tratado por um sistema de IA continua sendo dado pessoal sensível pela LGPD (art. 5º, II, e art. 11) — isso não muda porque o processamento agora é feito por um modelo. A camada de proteção de dados exige base legal para o tratamento, minimização, e — quando o sistema toma ou influencia uma decisão automatizada — o direito do titular a solicitar revisão, previsto no art. 20 da LGPD. A Nota Técnica nº 12/2025 da ANPD consolidou subsídios recebidos especificamente sobre esse ponto — o direito de revisão de decisão automatizada — dentro do item 7 da agenda regulatória 2025-2026 do órgão para inteligência artificial [1].

---

[referencia=14d93332dc180e13 score=0.016]
## Referências

1. Macher Tecnologia. ANPD, Inteligência Artificial e LGPD: o que a Nota Técnica nº 12/2025 revela. 2025.
2. Engenharia Biomédica. Software como Dispositivo Médico (SaMD): Guia Completo de Regulação no Brasil. 2026.
3. ConJur. IA na medicina e os novos contornos da responsabilidade civil — Resolução CFM 2.454/2026. Agosto de 2026.
4. Conselho Federal de Medicina. Resolução CFM nº 2.314/2022.
5. Senado Federal. PL 2338/2023 — tramitação.

---

[referencia=14d93332dc180e13 score=0.012]
## Camada 2 — Regulação sanitária: ANVISA

Quando um sistema de IA influencia uma decisão clínica — diagnóstico, triagem, dosagem — ele pode se enquadrar como Software como Dispositivo Médico (SaMD), regulado pela RDC 657/2022 da ANVISA, em vigor desde julho de 2023 e ainda a norma vigente em 2026 [2]. A RDC exige demonstração de segurança e desempenho do software, incluindo cibersegurança, e está sob revisão específica para tratar dois temas emergentes: software adaptativo (que aprende e muda ao longo do tempo, como muitos modelos de IA) e o conceito de Plano de Controle de Mudança Pré-determinado (PCCP), já adotado pelo FDA americano para gerenciar atualizações de algoritmo sem exigir nova submissão regulatória a cada mudança [2]. Enquanto essa revisão não conclui, a regra de hoje já se aplica: se a IA influencia uma decisão clínica, o enquadramento regulatório precisa ser avaliado.

## Camada 3 — Ética profissional: CFM

O Conselho Federal de Medicina trata a IA como ferramenta, nunca como substituto de responsabilidade médica. A Resolução CFM nº 2.454/2026 reafirma esse princípio: a responsabilidade final por uma decisão clínica continua sendo humana, e o uso de IA precisa ser documentado — registro em prontuário, rastreabilidade do que foi assistido por máquina [3]. Isso conversa diretamente com a Resolução 2.314/2022, que já regula telemedicina e exige preservação de dados e imagens conforme custódia, integridade e sigilo profissional [4].

---

[referencia=b90b992d0c2eba47 score=0.008]
## What to keep preparing

| Area | Current law | Route-specific status | What to keep | 
|---|---|---|---|
| AI literacy and prohibited-practices screening | Already live from 2 February 2025. | No later route date identified here. | Keep training records, role exposure notes, policy acknowledgements, and prohibited-practices screening. | 
| GPAI and governance framework provisions | Already live from 2 August 2025 for relevant operators. | No later route date identified here. | Keep vendor records, model information, downstream-use limits, and update notices where relevant. | 
| Annex III Article 6(2) high-risk AI obligations | 2 December 2027 under Regulation (EU) 2026/1744. | Regulation (EU) 2026/1744 sets 2 December 2027 for Article 6(2)/Annex III high-risk AI systems, under Regulation (EU) 2026/1744. | Keep inventory, risk rationale, instructions for use, oversight records, logs, and vendor evidence. | 
| Article 50 transparency | Article 50 generally applied from 2 August 2026, subject to route-specific exceptions. | A narrow Article 50(2) legacy-system transition ends on 2 December 2026; Article 50(4) is not included. | Keep notices, labelling decisions, synthetic-content workflow records, and disclosure approvals. | 
| Article 6(1)/Annex I product-integrated high-risk AI systems | 2 August 2028 under Regulation (EU) 2026/1744. | Regulation (EU) 2026/1744 sets 2 August 2028 for Article 6(1)/Annex I systems, under Regulation (EU) 2026/1744. | Map the product regime, AI safety-component role, manufacturer duties, and conformity route. |

---

[referencia=b90b992d0c2eba47 score=0.003]
## Detailed timeline

1 August 2024

### EU AI Act enters into force

The AI Act entered into force. This started the phased implementation clock but did not make every later obligation immediately applicable.

Existing Regulation (EU) 2024/1689 baseline, Article 113

2 February 2025

### Prohibited practices and AI literacy apply

AI literacy and prohibited-practices obligations are already live under the existing AI Act baseline. Organisations should keep training and screening records rather than waiting for later timeline changes.

Articles 4 and 5

2 August 2025

### GPAI and governance provisions apply

GPAI, governance, notified-body, and penalty-framework provisions are part of the already-applicable track for relevant operators.

Existing Regulation (EU) 2024/1689 baseline

2 August 2026

### General application milestone

Article 50 and most remaining provisions generally apply from 2 August 2026, subject to provision-specific exceptions. Regulation (EU) 2026/1744 moved Article 6(2) / Annex III and Article 6(1) / Annex I high-risk routes to later dates.

Regulation (EU) 2024/1689 as amended

2 August 2027

### AI regulatory sandbox milestone

Member States must ensure that at least one AI regulatory sandbox is operational by 2 August 2027. Verify national implementation and access routes.

Regulation (EU) 2026/1744, Article 57

2 December 2027

### Article 6(2) / Annex III application date

The Article 6(2) / Annex III high-risk requirements apply from this date under Regulation (EU) 2026/1744.

Regulation (EU) 2026/1744

2 August 2028

### Article 6(1) / Annex I application date

The Article 6(1) / Annex I product-integrated high-risk requirements apply from this date under Regulation (EU) 2026/1744.

Regulation (EU) 2026/1744

## Frequently asked questions

---

[referencia=b90b992d0c2eba47 score=0.002]
## Frequently asked questions

## What are the current EU AI Act dates?

The EU AI Act entered into force on 1 August 2024 and applies in phases. Regulation (EU) 2026/1744 sets 2 December 2027 for the relevant Article 6(2)/Annex III high-risk provisions and 2 August 2028 for Article 6(1)/Annex I product-integrated high-risk provisions. Article 50 and other obligations must be checked separately.

## What changed under Regulation (EU) 2026/1744?

Regulation (EU) 2026/1744 was published on 24 July 2026 and entered into force on 27 July 2026. Regulation (EU) 2026/1744 changes parts of the timeline. This page separates current law by provision-specific application date.

## Why does the timeline now include 2028?

The timeline includes 2028 because Regulation (EU) 2026/1744 sets 2 August 2028 for Article 6(1)/Annex I product-integrated high-risk AI systems. Product and safety teams still need to map sectoral-law overlap and evidence duties.

## Which high-risk AI systems have later application dates under Regulation (EU) 2026/1744?

Regulation (EU) 2026/1744 sets 2 December 2027 for Article 6(2)/Annex III systems and 2 August 2028 for Article 6(1)/Annex I systems. Use case classification still needs case-by-case review.

## Should deployers keep preparing evidence?

Yes. Inventory, vendor due diligence, human oversight, logs, user instructions, Article 50 notices, and ownership records remain useful under both tracks. The later date does not remove the evidence gap.

## Related resources

Last evidence review date: 2 September 2026

**Source basis:** Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 is the current legal baseline. The consolidated text is current from 27 July 2026. This page is for operational planning and is not legal advice.

Consolidated Regulation (EU) 2024/1689 · Regulation (EU) 2026/1744 · Council adoption history · Council 7 May 2026 agreement press release

---

[referencia=64b4c84a1acfe340 score=0.002]
Implementation monitor

# The EU AI Act timeline

Follow the regulation from publication through its phased application. Dates reflect the current framework, including the AI Omnibus changes in force from July 2026.

1. 12 July 2024## Published in the Official JournalRegulation (EU) 2024/1689 was published, beginning the countdown to entry into force.
2. 1 August 2024## The AI Act entered into forceThe regulation became EU law, with its obligations scheduled to apply in phases.
3. 2 February 2025## First rules began to applyThe AI-system definition and prohibited-practice framework entered into application.
4. 2 August 2025## Governance and GPAI obligationsEU and national governance provisions and obligations for general-purpose AI models began to apply.
5. 27 July 2026## AI Omnibus entered into forceThe amending regulation extended the high-risk implementation schedule and introduced targeted simplifications.
6. 2 August 2026## General applicationMost remaining provisions, including the Article 50 transparency framework, apply from this date.
7. 2 December 2026## Two new prohibitions and the legacy marking deadlineArticle 5(1)(ba) and (bb), inserted by the AI Omnibus, prohibit specified non-consensual intimate imagery and child sexual abuse material: taking the Article 5 list to ten. Generative systems already on the market must also carry machine-readable marking of synthetic output by this date.
8. 2 August 2027## Existing GPAI model transition endsProviders of GPAI models placed on the market before 2 August 2025 must meet the applicable obligations.
9. 2 December 2027## Annex III high-risk systemsHigh-risk requirements begin applying to listed sensitive uses such as employment, education, essential services and biometrics.
10. 2 August 2028## AI embedded in regulated productsHigh-risk requirements apply to AI systems integrated into products such as machinery, toys and lifts.
11. 2 August 2030## Legacy large-scale IT systems must complyAI components of Union large-scale IT systems in the area of freedom, security and justice, placed on the market before 2 August 2027, must be brought into compliance.

Source: Regulation (EU) 2024/1689 and European Commission AI Act implementation updates. Always verify dates against the current official text before legal reliance.

---

[referencia=b90b992d0c2eba47 score=0.001]
**How to read this page:** “Current law” means Regulation (EU) 2024/1689 as amended and consolidated from 27 July 2026. Application dates remain provision-specific: entry into force does not make every later obligation immediately applicable.

## Key dates at a glance

| Date | Track | What it means | Planning action | 
|---|---|---|---|
| 1 August 2024 | Existing Regulation (EU) 2024/1689 baseline | The EU AI Act became law and the phased timeline started. | Use this as the starting point. | 
| 2 February 2025 | Existing Regulation (EU) 2024/1689 baseline | Prohibited practices and AI literacy duties became live. | Keep screening records and training evidence. | 
| 2 August 2025 | Existing Regulation (EU) 2024/1689 baseline | GPAI, governance, notified-body, and penalty rules became live. | Keep GPAI and vendor records where relevant. | 
| 2 August 2026 | Existing Regulation (EU) 2024/1689 baseline | Article 50 and most remaining provisions generally apply from this date, subject to provision-specific exceptions; Article 6(2) / Annex III moved to 2 December 2027. | Use this date for obligations that apply here and verify Article 50 and high-risk routes separately. | 
| 2 December 2026 | Current statutory date | The narrow Article 50(2) legacy-system transition ends; the specified new Article 5 provisions also apply from this date. | Review Article 50 separately. Do not assume every transparency duty moves to 2027. | 
| 2 December 2027 | Current statutory date | Article 6(2) / Annex III high-risk requirements apply from this date under Regulation (EU) 2026/1744. | Continue classification and evidence work before application. | 
| 2 August 2028 | Current statutory date | Article 6(1) / Annex I product-integrated high-risk requirements apply from this date under Regulation (EU) 2026/1744. | Map the product-safety overlap and verify the applicable product regime. |

---

[referencia=b90b992d0c2eba47 score=0.000]
## Keep the evidence work moving

Regulation (EU) 2026/1744 changed the timeline, but it does not remove the need to know which AI systems exist, who owns them, which vendor records support them, and what evidence a deployer can show.