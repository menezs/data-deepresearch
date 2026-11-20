# Relatório de Auditoria — Gemini (semana_trabalho_ac2200792987_20261114T193734Z)

**Arquivo auditado:** `answers/Portugues/Gemini/EmConsolidacao/semana_trabalho.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | semana_trabalho_ac2200792987_20261114T193734Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-14T20:34:35.813613+00:00 |
| **Total de trechos citados** | 126 |
| **Tempo de processamento** | 0:00:57:02 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 2957.4 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-14 19:37:56+00:00 |
| Citações no corpo | 126 marcadores, 17 distintos |
| Referências listadas | 36 (19 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 7 | 5.6% |
| **UNSUPPORTED** | 111 | 88.1% |
| **CONTRADICTED** | 5 | 4.0% |
| **SKIPPED** | 3 | 2.4% |
| **TOTAL** | 126 | 100.0% |

Sobre os 123 trechos citados auditados: SUPPORTED 5,69%, UNSUPPORTED 90,24%, CONTRADICTED 4,06%.

> **5 dos 7 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 5 estão **contados dentro** dos 7 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`115` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `85` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `49` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 3, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#1` O marco icônico dessa transição ocorreu na década de 1920, quando Henry Ford adotou a semana laboral de cinco dias em s… | [2] | [23] [10] [1] https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [20] | — |
| `#6` O Brasil ocupa a liderança mundial no diagnóstico de transtornos de ansiedade, figura em segundo lugar global em casos… | [4] | [22] [18] [10] [11] [30] [9] [15] [1] [14] [12] | — |
| `#9` Longe de constituir uma mera concessão de folga adicional ou uma regalia corporativa, o modelo representa uma reconfigu… | [1] | [10] [20] [30] [22] [11] [5] [15] [9] [17] | — |
| `#13` A gênese desse modelo remonta a 2018, quando os fundadores Andrew Barnes e Charlotte Lockhart conduziram um ensaio pion… | [2] | [10] [1] [3] [16] [23] [9] [30] [11] | — |
| `#16` A viabilização do modelo 100:80:100™ baseia-se na premissa de que tempo não é sinônimo de produtividade. | [1] | [10] [15] [17] [20] [30] [16] [22] [3] | — |
| `#17` Para que uma organização consiga recuperar 20% do tempo semanal sem comprometer o output final, faz-se necessária uma r… | [1] | [10] [11] [4] [20] [22] [12] [15] | — |
| `#22` Modelos de cobertura e escalas flexíveis: A semana de quatro dias não exige o fechamento da empresa às sextas-feiras. | [2] | [10] [11] [22] [23] [9] https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ [30] | — |
| `#30` Em 2022, o Reino Unido sediou o maior piloto coordenado da semana de quatro dias em nível empresarial, organizado pela… | [2] | [23] [10] [1] [9] [4] [30] [5] [22] | — |
| `#32` Os resultados quantitativos ao final de seis meses indicaram uma queda de 71% nos níveis de burnout autorreportados e u… | [2] | — | [4] [11] [30] [1] [13] [5] [10] [17] [18] [9] [23] [22] [12] ⚠ |
| `#33` Sob a ótica da retenção e assiduidade, observou-se uma redução de 65% nos dias de baixa médica e uma queda de 57% na ro… | [2] | [4] [1] [15] [11] [10] [12] [5] [30] [23] [20] | — |
| `#37` No setor privado de alta tecnologia, um dos casos mais emblemáticos ocorreu durante o verão de 2019 na subsidiária da M… | [9] | [27] [29] [28] [25] [24] [10] [11] [1] | — |
| `#40` Os resultados operacionais registraram um aumento de 39,9% na produtividade por funcionário, medida pelas vendas efetua… | [9] | [30] [22] [11] [24] [25] [15] [10] [1] [20] [29] [23] https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ | — |
| `#43` Na Europa Continental, a Espanha destacou-se por iniciativas locais e estatais. | [4] | [1] [14] [12] [20] [9] [10] [23] [18] | — |
| `#48` Diferenciando-se do modelo 100:80:100, países como a Bélgica optaram por reformas legislativas focadas na jornada conce… | [11] | [22] [20] [30] [9] [1] [13] [18] [10] [14] [3] [2] [16] [17] [23] | — |
| `#49` No modelo belga, permite-se que o trabalhador cumpra a carga horária semanal completa de 38 horas em quatro dias de tra… | [11] | [9] [1] [10] [22] [13] [23] [14] [30] https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [18] | — |
| `#51` Coordenado pelos economistas Pedro Gomes (da Birkbeck University of London) e Rita Fontinha (da Henley Business School)… | [5] | https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ [9] [11] [10] [13] [23] [12] | — |
| `#53` A avaliação final do piloto revelou um índice de satisfação extraordinário: 95% das empresas participantes avaliaram a… | [14] | [13] [11] [22] [9] [23] [12] [10] [30] [4] | — |
| `#54` Os relatórios apontaram que a produtividade se manteve ou aumentou, impulsionada pelo redesenho de rotinas, otimização… | [5] | [22] [10] [11] [15] [4] [30] [23] [1] [12] | — |
| `#55` Entre os trabalhadores, constataram-se reduções significativas nos níveis de exaustão, ansiedade e problemas de sono, a… | [14] | [13] [11] [9] [22] [4] [1] [10] [12] https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ [30] | — |
| `#60` Sentido e Propósito: 86,0% dos colaboradores relataram enxergar maior propósito e significado no trabalho executado. | [4] | [22] [20] [11] [9] [30] [12] [10] [13] [23] | — |
| `#62` Percepção de Produtividade: 71,5% perceberam que sua produtividade pessoal aumentou de forma expressiva. | [4] | [22] [30] [11] [10] [20] [1] [18] [12] [14] [23] | — |
| `#64` Engajamento e Execução: 60,0% relataram maior engajamento diário, e 56,0% afirmaram executar projetos de maneira mais s… | [4] | [22] [20] [30] [9] [10] [11] [12] [13] | — |
| `#65` Avaliação Geral: 84,0% dos executivos consideraram o piloto altamente benéfico para a empresa. | [4] | [22] [12] [9] [11] [23] [10] [13] https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ [30] | — |
| `#68` Visibilidade e Atração: 63,6% constataram aumento na visibilidade da marca empregadora no mercado. | [4] | [22] [11] [10] [12] [18] [20] [13] | — |
| `#71` A maioria das companhias optou por folgas às sextas-feiras por ser um dia historicamente de menor ritmo comercial, enqu… | [12] | [30] [11] [10] [22] [20] [23] [4] | — |
| `#74` O movimento ganhou impulso com a articulação de propostas de emenda à Constituição voltadas à reconfiguração dos limite… | [16] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [18] [20] | — |
| `#75` A Proposta de Emenda à Constituição (PEC 8/2025), apresentada pela deputada federal Erika Hilton (PSOL-SP), trazia em s… | [16] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ [18] https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [10] [19] | — |
| `#76` Essa medida previa um limite de 36 horas semanais distribuídas em quatro dias de trabalho e três dias de descanso, sem… | [16] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [10] https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [11] [29] [18] | — |
| `#77` Simultaneamente, tramitava na Câmara dos Deputados a PEC 221/2019, de autoria do deputado Reginaldo Lopes (PT-MG), que… | [15] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [10] [18] | — |
| `#78` Em fevereiro de 2026, as matérias foram apensadas para análise conjunta no Congresso Nacional. | [17] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ [18] https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [12] [9] https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais [10] | — |
| `#79` O debate legislativo resultou na elaboração de um substitutivo pelo relator, deputado Leo Prates. | [1] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [9] [20] [18] [10] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [12] | — |
| `#80` O texto aprovado pela Câmara dos Deputados e ratificado pelo Senado Federal acabou por aprovar a extinção da escala 6x1… | [1] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ [18] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [19] [20] | — |
| `#81` Nova Carga Máxima Semanal: Redução do teto constitucional de 44 para 40 horas semanais, mantendo-se o limite diário de… | [1] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [18] [10] | — |
| `#82` Adocao da Escala 5x2: Instituição obrigatória de dois dias de repouso semanal remunerado por semana trabalhada, erradic… | [1] | — | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais [18] [10] [20] ⚠ |
| `#83` Proteção Irredutível do Salário: Proibição expressa de qualquer redução salarial nominal, proporcional ou de qualquer o… | [1] | https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ [10] [9] [20] | — |
| `#84` Cronograma de Transição Gradual: A implementação foi dividida em duas etapas ao longo de 14 meses a partir da promulgaç… | [1] | https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [10] [18] [12] [9] | — |
| `#86` Ao término de 14 meses da promulgação, entra em vigor o limite definitivo de 40 horas semanais. | [17] | https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [18] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 | — |
| `#87` Exceções e Regimes Diferenciados: Para atividades contínuas ou essenciais (como saúde, segurança pública, transporte e… | [1] | https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ [10] [18] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 | — |
| `#88` Isenção de Controle para Alta Renda: Dispensa-se o controle rígido de jornada para trabalhadores com diploma de nível s… | [1] | https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ [9] [10] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [20] https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ | — |
| `#89` Apoio a Microempresas e MEIs: O texto previu a edição de lei complementar para ajustar os limites do Simples Nacional e… | [1] | — | https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ [10] [21] https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ [9] [12] https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/ ⚠ |
| `#95` No âmbito da igualdade de gênero, os dados empíricos apurados nos pilotos internacionais revelam um efeito redistributi… | [2] | [11] [10] [12] [14] [23] [22] [9] [30] | — |
| `#97` Esse movimento atenua a "jornada dupla" historicamente sobrecarregada sobre as mulheres, favorecendo a equidade de opor… | [2] | [10] [20] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 [14] [12] [11] [9] https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/ | — |
| `#98` A semana laboral reduzida opera como uma alavanca de descarbonização e sustentabilidade. | [3] | [20] [10] [30] [1] [12] [11] [15] [9] [14] [5] | — |
| `#101` Estudo da University of Massachusetts estimou que a adoção abrangente da semana de quatro dias poderia reduzir a pegada… | [3] | [1] [23] [12] [9] [11] [30] [4] [10] [22] [14] | — |
| `#102` Se uma organização tentar comprimir cinco dias de trabalho em quatro sem promover o redesenho de processos, a eliminaçã… | [3] | [10] [30] [11] [1] [22] [17] | — |
| `#109` A adoção da semana de quatro dias nesses setores exige a contratação de novos trabalhadores para cobrir os turnos reman… | [3] | [10] [9] https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/ [23] [5] [22] [1] [11] | — |
| `#110` Adicionalmente, algumas empresas enfrentam ruídos na cultura organizacional e resistência gerencial. | [4] | [10] [11] [9] | — |
| `#115` A validação da metodologia 100:80:100™ comprova que é possível manter ou elevar o desempenho corporativo, proteger as r… | [1] | [30] [10] [3] [15] [17] [2] [5] [22] [16] [11] [9] | — |
| `#117` Diagnóstico e Redesenho Prévio de Processos: As empresas devem realizar um diagnóstico profundo de seus processos inter… | [1] | [10] [11] [12] [15] [9] | — |
| `#120` Lideranças e colaboradores devem coconstruir as soluções mais adequadas à realidade de cada setor, definindo se a folga… | [2] | [10] [22] https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/ [30] [9] [20] [11] https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1 | — |
| `#124` A semana de quatro dias não representa uma utopia trabalhista ou uma simples redução da carga de trabalho, mas sim um p… | [1] | [10] [11] [15] [9] [22] [12] [20] | — |
| `#125` Ao alinhar a inteligência operacional ao bem-estar biológico e psicológico do trabalhador, a semana de quatro dias rede… | [1] | [10] [20] [30] [15] [22] [5] [14] [16] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2993073 |
| **Média de tokens por requisição** | 24333.9 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 19/36 (52.8%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 8.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[1]](https://en.wikipedia.org/wiki/Four-day_workweek) | downloaded | 34 | 3 | 13 | 18 | 0 |
| [[2]](https://www.nirandfar.com/4-day-workweek/) | downloaded | 22 | 2 | 6 | 14 | 0 |
| [[4]](https://www.sociology.cam.ac.uk/news/new-results-worlds-largest-trial-four-day-working-week) | downloaded | 20 | 1 | 0 | 19 | 0 |
| [[3]](https://www.4dayweek.com/news-posts/100-80-100-rule-mwmb7) | downloaded | 16 | 0 | 1 | 15 | 0 |
| [[5]](https://disprz.ai/blog/4-day-work-week-experiment-impact) | downloaded | 7 | 0 | 3 | 4 | 0 |
| [[9]](https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[16]](https://leadership.global/insights/news-trends-insights/how-the-four-day-week-model-boosts-employees-happiness/) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[7]](https://recipp.ipp.pt/bitstreams/34066234-3582-4f47-907a-142a99dead62/download) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[10]](https://www.iefp.pt/documents/10181/11729755/Relatorio1Fase_Final.pdf/13cf9e6c-50f7-4830-a822-c1d443f36f31) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[11]](https://rhmagazine.pt/95-das-empresas-avaliam-positivamente-o-projeto-piloto-da-semana-de-quatro-dias/) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[14]](https://www.michaelpage.com.tr/en/advice/career-advice/4-day-work-week-guide) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[17]](https://portal.fgv.br/en/noticias/estudo-indica-que-semana-de-quatro-dias-exige-confianca-e-flexibilidade-para-gerar-resultados) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[18]](https://4dayweek.io/country/brazil) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[8]](https://www.uts.edu.au/case-studies/mythbusting-four-day-work-week) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[12]](https://www.adcoesao.pt/wp-content/uploads/guia_para_a_avaliacao.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[13]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[15]](https://www.4dayweek.com/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[6]](https://support.google.com/knowledgepanel/answer/9787176) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/](https://www.planapp.gov.pt/estudos-avaliacao/avaliacao-do-projeto-piloto-semana-de-quatro-dias/) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1](https://www.migalhas.com.br/quentes/425383/erika-hilton-protocola-pec-para-acabar-com-a-escala-6x1) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/](https://veja.abril.com.br/economia/senado-aprova-em-primeiro-turno-o-fim-da-escala-6x1-e-a-reducao-da-jornada-de-trabalho/) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/](https://exame.com/brasil/de-quem-e-o-projeto-que-acabou-com-a-escala-6x1-conheca-as-propostas/) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/](https://veja.abril.com.br/economia/fim-da-escala-6x1-quando-comeca-a-valer-e-o-que-muda-em-11-respostas/) | downloaded | 0 · nunca citada | — | — | — | — |
| [https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais](https://www.camara.leg.br/noticias/1277141-camara-aprova-em-dois-turnos-fim-da-escala-6x1-com-jornada-maxima-de-40-horas-semanais) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://www.jota.info/opiniao-e-analise/colunas/democracia-em-transe/fim-da-escala-6x1-conecta-lula-a-trabalhadores-e-muda-rumo-da-campanha-eleitoral) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://popularmais.com.br/noticia/25530/sindicatos-fortes-sao-condicao-para-um-brasil-mais-justo-e-produtivo/amp) | downloaded | 0 · nunca citada | — | — | — | — |
| [[21]](https://eco.sapo.pt/2022/07/01/valencia-da-5-500-euros-por-trabalhar-as-empresas-que-implementem-semana-de-quatro-dias/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[22]](https://csb.org.br/noticias/semana-4-dias-de-trabalho-na-alemanha-teste) | downloaded | 0 · nunca citada | — | — | — | — |
| [[23]](https://g1.globo.com/trabalho-e-carreira/noticia/2023/02/27/semana-de-4-dias-o-que-experiencias-mostram-sobre-futuro-do-trabalho.ghtml) | downloaded | 0 · nunca citada | — | — | — | — |
| [[24]](https://bigthink.com/the-present/four-day-work/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[25]](https://www.weforum.org/stories/jobs-and-the-future-of-work/microsoft-4-day-work-week-productivity-increase/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://japantoday.com/category/business/microsoft-japan%E2%80%99s-experiment-with-3-day-weekend-boosts-worker-productivity-by-40) | blocked | 0 · nunca citada | — | — | — | — |
| [[27]](https://www.theguardian.com/technology/2019/nov/04/microsoft-japan-four-day-work-week-productivity) | downloaded | 0 · nunca citada | — | — | — | — |
| [[28]](https://time.com/5717401/microsoft-4-day-workweek/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[29]](https://4dayweek.io/case-study/microsoft) | downloaded | 0 · nunca citada | — | — | — | — |
| [[30]](https://sindishopping.com.br/semana-de-4-dias-empresas-que-participam-de-teste-no-brasil-ja-notam-resultados-positivos/) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[1]](https://en.wikipedia.org/wiki/Four-day_workweek) | #0, #10, #12 | #3, #5, #9, #11, #16, #83, #105–106, #113–115, #124–125 | #4, #8, #17–18, #20, #79–82, #84, #87–89, #111, #117–118, #121, #123 | `#0` The five-day workweek is a cultural norm; the result of early 1900s union advocacy to reduce the six-day workweek, which led to the invention of the weekend. I… |
| [[2]](https://www.nirandfar.com/4-day-workweek/) | #24, #119 | #15, #22, #32, #34, #92, #120 | #1–2, #13–14, #23, #30, #33, #93–97, #122, #31 ⚡ | `#24` Companies should establish a culture founded on psychological safety so employees can freely discuss the questions and concerns above. |
| [[4]](https://www.sociology.cam.ac.uk/news/new-results-worlds-largest-trial-four-day-working-week) | #59 | — | #6–7, #43–44, #47, #58, #60–69, #91, #110, #46 ⚡ | `#59` 71% of employees self-reported lower levels of “burnout”, and 39% said they were less stressed |
| [[3]](https://www.4dayweek.com/news-posts/100-80-100-rule-mwmb7) | — | #25 | #26, #28–29, #45, #50, #98–99, #101–104, #107–109, #27 ⚡ | `#25` When you tell your employees that their output is more important than the time they take to complete it, then they will be more focused and therefore, more pro… |
| [[5]](https://disprz.ai/blog/4-day-work-week-experiment-impact) | — | #21, #54, #112 | #36, #51, #35, #52 ⚡ | `#21` exploring methods to streamline tasks, leverage technology for automation |
| [[9]](https://ipps.iscte-iul.pt/images/Trabalho%20final%20-%20Grupo%201.pdf) | — | — | #37–40, #42 | — |
| [[16]](https://leadership.global/insights/news-trends-insights/how-the-four-day-week-model-boosts-employees-happiness/) | — | — | #72, #74–76, #116 | — |
| [[10]](https://www.iefp.pt/documents/10181/11729755/Relatorio1Fase_Final.pdf/13cf9e6c-50f7-4830-a822-c1d443f36f31) | — | #100 | #41 | `#100` as que fecham têm poupanças até 20% na fatura energética |
| [[11]](https://rhmagazine.pt/95-das-empresas-avaliam-positivamente-o-projeto-piloto-da-semana-de-quatro-dias/) | — | — | #48–49 | `#48` com países como a Bélgica a replicarem o que fizemos |
| [[14]](https://www.michaelpage.com.tr/en/advice/career-advice/4-day-work-week-guide) | — | #53, #55 | — | `#53` over 96% of companies worldwide are likely to stick with a 4-day working week |
| [[17]](https://portal.fgv.br/en/noticias/estudo-indica-que-semana-de-quatro-dias-exige-confianca-e-flexibilidade-para-gerar-resultados) | — | — | #78, #86 | — |
| [[18]](https://4dayweek.io/country/brazil) | #85 | — | #73 | `#85` The first step, to 42 hours for workers under the CLT labour code, comes two months after promulgation, which Agência Senado dates to 15 December 2026. 40 hour… |
| [[8]](https://www.uts.edu.au/case-studies/mythbusting-four-day-work-week) | — | — | #19 | — |
| [[12]](https://www.adcoesao.pt/wp-content/uploads/guia_para_a_avaliacao.pdf) | — | — | #71 | — |
| [[13]](https://portugal.gov.pt/gc23/comunicacao/noticias/95-das-empresas-avaliam-positivamente-experiencia-da-semana-de-quatro-dias) | — | — | #70 | — |
| [[15]](https://www.4dayweek.com/) | — | — | #77 | — |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://recipp.ipp.pt/bitstreams/34066234-3582-4f47-907a-142a99dead62/download — anti_bot — barreira de acesso (anti_bot): # Making sure you're not a bot! RCAAP – Repositórios Científicos de Acesso Aberto de Portugal Calculating... Difficulty:
- https://japantoday.com/category/business/microsoft-japan%E2%80%99s-experiment-with-3-day-weekend-boosts-worker-productivity-by-40 — no_content — barreira de acesso (no_content): Powered and protected by Privacy

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-0`** [1]
  - Trecho: A consolidação da jornada de trabalho padrão de 40 horas semanais, distribuídas ao longo de cinco dias, não representa uma constante imutável da natureza produtiva, mas sim um arranjo institucional e histórico estabelec…
  - Justificativa: A evidência afirma explicitamente que a semana de cinco dias é uma 'norma cultural' resultante de defesa sindical no início dos anos 1900, e que a semana de trabalho média foi reduzida de cerca de 60 para 40 horas no in…
  - Suporte veio de: [1]
  - Evidência: “The five-day workweek is a cultural norm; the result of early 1900s union advocacy to reduce the six-day workweek, which led to the invention of the weekend.”
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-10`** [1]
  - Trecho: A tese central que fundamenta essa transformação sustenta que a otimização de processos, a redução de fricções operacionais e a eliminação de desperdícios temporais permitem que o mesmo volume de produção — ou mesmo um…
  - Justificativa: A evidência sustenta a tese central do trecho: que a otimização de processos, eliminação de desperdício de tempo e melhorias de produtividade permitem manter (ou superar) a produção em jornada reduzida. O texto afirma q…
  - Suporte veio de: [1]
  - Evidência: “trials have indicated that it leads to a better work-life balance, lower stress-levels, and increased productivity, mainly by eliminating wasted work time”
  - Não coberto pela evidência: A caracterização de que essa seria 'a tese central' da transformação (a evidência descreve os mecanismos, mas não usa essa formulação específica de tese central); O termo 'redução de fricções operacionais' não aparece literalmente na evidência (a evidência fala em 'eliminating wasted work time' e 'productivity improvements')
  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A evidência menciona 'eliminating wasted work time' e 'productivity improvements' como mecanismos para manter 100% da produção em menos hor…") — cascata: baseline → context_expansion
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-12`** [1]
  - Trecho: A equação fundamental do modelo estabelece a manutenção de 100% da remuneração e dos benefícios do trabalhador, em troca de 80% do tempo de trabalho semanal anterior, sob o compromisso irredutível de entregar 100% dos r…
  - Justificativa: A evidência descreve explicitamente o modelo 100-80-100: 100% de remuneração (pay/wages) por 80% do tempo de trabalho, em troca do compromisso de manter 100% da produtividade/output anterior. O aspecto 'benefícios' não…
  - Suporte veio de: [1]
  - Evidência: “This follows the 100-80-100 model: 100% pay for 80% of the time, in exchange for a commitment to maintain at least 100% productivity.”
  - Não coberto pela evidência: A menção a 'benefícios' do trabalhador não aparece explicitamente na descrição do modelo 100-80-100 na evidência; apenas 'pay'/'wages' são mencionados.
### UNSUPPORTED

- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-1`** [2]
  - Trecho: O marco icônico dessa transição ocorreu na década de 1920, quando Henry Ford adotou a semana laboral de cinco dias em suas linhas de montagem automotivas, substituindo a escala comum de seis dias de trabalho.
  - Justificativa: A evidência trata exclusivamente da semana de trabalho de quatro dias, estudos da organização 4 Day Week Global e estratégias de adaptação. Não há qualquer menção a Henry Ford, à década de 1920, ou à transição de seis p…
  - Não coberto pela evidência: década de 1920; Henry Ford; adoção da semana laboral de cinco dias
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [23] [10] [1] c8867da9728a894d de61fc78ef7823b1 [20] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-2`** [2]
  - Trecho: A premissa subjacente à época demonstrava que trabalhadores mais descansados apresentavam maior produtividade industrial e dispunham de tempo livre para consumir bens, alimentando a própria engrenagem econômica.
  - Justificativa: A evidência discute um estudo sobre semana de trabalho de quatro dias, mencionando aumento de produtividade e redução de burnout, mas não aborda a 'premissa subjacente à época', nem o tempo livre para consumo de bens, n…
  - Não coberto pela evidência: Premissa subjacente à época; Trabalhadores mais descansados apresentavam maior produtividade industrial (não há menção a produtividade 'industrial' especificamente); Tempo livre para consumir bens
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-3`** [1]
  - Trecho: Ao longo do último século, enquanto a produtividade global registrou saltos exponenciais impulsionados pelo avanço da computação, automação e inteligência artificial, o modelo contratual de alocação de tempo permaneceu…
  - Justificativa: A evidência trata principalmente da semana de trabalho de quatro dias e sua história. Embora mencione que a semana de 5 dias é uma norma cultural resultante de advocacy sindical no início dos anos 1900, e que reduções a…
  - Suporte veio de: [1]
  - Evidência: “The five-day workweek is a cultural norm; the result of early 1900s union advocacy to reduce the six-day workweek, which led to the invention of the weekend.”
  - Não coberto pela evidência: saltos exponenciais de produtividade global ao longo do último século; avanço da computação como impulsionador de produtividade; inteligência artificial como impulsionador de produtividade
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-27`** [3]
  - Trecho: O programa reduziu a semana laboral de 40 para 35 ou 36 horas, sem qualquer diminuição salarial.
  - Justificativa: A evidência afirma que a semana de 4 dias corresponde a 32 horas (4x8), o que contradiz a afirmação de redução para 35 ou 36 horas. A parte sobre não redução salarial (100% de pagamento) é sustentada, mas os números cen…
  - Evidência: “100% pay for 80% of your time while maintaining 100% output”
  - Não coberto pela evidência: Redução de 40 horas (ponto de partida não mencionado na evidência); Redução para 35 ou 36 horas (a evidência indica 32 horas, não 35 ou 36)
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência descreve o modelo 100:80:100™ (100% do salário por 80% do tempo, mantendo 100% da produção) e menciona uma semana de 4 dias com…") — cascata: baseline → context_expansion
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-31`** [2]
  - Trecho: O estudo abrangeu 61 empresas e aproximadamente 2.900 trabalhadores de diversos segmentos, desde agências de marketing até indústrias e instituições financeiras.
  - Justificativa: A evidência menciona um estudo da 4 Day Week Global com 900 funcionários em 33 empresas dos EUA e Irlanda em 2022. A afirmação cita 61 empresas e aproximadamente 2.900 trabalhadores, números que entram em conflito diret…
  - Evidência: “The organization, 4 Day Week Global, did a 6-month study of 900 employees across 33 U.S. and Irish businesses in 2022.”
  - Não coberto pela evidência: 61 empresas; aproximadamente 2.900 trabalhadores; diversos segmentos, desde agências de marketing até indústrias e instituições financeiras
- **Trecho citado `semana_trabalho_ac2200792987_20261114T193734Z-35`** [5]
  - Trecho: Impressionantes 96% das empresas participantes declararam a intenção de manter o modelo de quatro dias após a conclusão do projeto piloto.
  - Justificativa: A evidência afirma que 56 das 61 empresas participantes expressaram intenção de continuar o modelo de quatro dias. 56/61 ≈ 91,8%, e não 96% como afirma o trecho. A evidência fornece números explícitos que conflitam com…
  - Evidência: “Of the 61 companies involved in the pilot, 56 expressed their intent to continue experimenting with the four-day workweek beyond the initial trial period.”
  - Não coberto pela evidência: 96% (a porcentagem correta segundo a evidência seria ~92%)

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login).

- `semana_trabalho_ac2200792987_20261114T193734Z-56` — Referencia(s) citada(s) ['ed8866b69fd6dd43'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_ac2200792987_20261114T193734Z-57` — Referencia(s) citada(s) ['ed8866b69fd6dd43'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `semana_trabalho_ac2200792987_20261114T193734Z-90` — Referencia(s) citada(s) ['ed8866b69fd6dd43'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.