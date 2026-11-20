[referencia=14d93332dc180e13 score=0.987]
# Governança de IA em saúde no Brasil: o mapa prático

Carlos Avila · 30 de julho de 2026 · 5 min de leitura

ia-em-saude lgpd seguranca

Quando uma instituição de saúde decide adotar IA, a primeira pergunta certa não é “qual modelo?” — é “sob quantas autoridades diferentes esse projeto vai responder?”. No Brasil, em 2026, são pelo menos quatro, e elas não se substituem umas às outras.

## Camada 1 — Proteção de dados: LGPD e ANPD

Todo dado de saúde tratado por um sistema de IA continua sendo dado pessoal sensível pela LGPD (art. 5º, II, e art. 11) — isso não muda porque o processamento agora é feito por um modelo. A camada de proteção de dados exige base legal para o tratamento, minimização, e — quando o sistema toma ou influencia uma decisão automatizada — o direito do titular a solicitar revisão, previsto no art. 20 da LGPD. A Nota Técnica nº 12/2025 da ANPD consolidou subsídios recebidos especificamente sobre esse ponto — o direito de revisão de decisão automatizada — dentro do item 7 da agenda regulatória 2025-2026 do órgão para inteligência artificial [1].

---

[referencia=14d93332dc180e13 score=0.825]
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

[referencia=14d93332dc180e13 score=0.476]
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

[referencia=14d93332dc180e13 score=0.142]
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