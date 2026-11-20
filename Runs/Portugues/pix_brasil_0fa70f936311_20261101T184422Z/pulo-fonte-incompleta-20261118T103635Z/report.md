# Relatório de Auditoria — Gemini (pix_brasil_0fa70f936311_20261101T184422Z)

**Arquivo auditado:** `answers/Gemini/EmConsolidacao/pix_brasil.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | pix_brasil_0fa70f936311_20261101T184422Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-04T05:57:39.846516+00:00 |
| **Total de trechos citados** | 111 |
| **Tempo de processamento** | 2:11:13:18 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 20.6 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-01 18:44:45+00:00 |
| Citações no corpo | 258 marcadores, 37 distintos |
| Referências listadas | 40 (4 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 62 | 55.9% |
| **UNSUPPORTED** | 47 | 42.3% |
| **CONTRADICTED** | 2 | 1.8% |
| **TOTAL** | 111 | 100.0% |

Sobre os 111 trechos citados auditados: SUPPORTED 55,85%, UNSUPPORTED 42,34%, CONTRADICTED 1,80%.

> **37 dos 62 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 37 estão **contados dentro** dos 62 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`63` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `15` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `16` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `9` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 15, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` A arquitetura dos instrumentos tradicionais de transferência eletrônica do varejo bancário brasileiro, consubstanciada… | [5] [30] [34] | [33] [36] [32] [20] [13] [6] | — |
| `#11` No centro dessa infraestrutura opera o Sistema de Pagamentos Instantâneos (SPI), que atua como a infraestrutura central… | [3] [6] [17] | [13] [36] [9] [38] [28] [33] [37] [18] | — |
| `#13` Para simplificar a experiência do usuário e eliminar os gargalos operacionais da digitação exaustiva de dados bancários… | [3] [7] [36] | [9] [33] [34] [28] [23] [13] | — |
| `#18` Esse modelo de incentivos econômicos perfeitamente alinhados garantiu a capilaridade universal da plataforma em todo o… | [15] [17] | — | [39] [13] [18] [38] [36] [20] [16] ⚠ |
| `#21` Embora a TED continue operacional para liquidações corporativas de grande porte e agendas específicas do mercado financ… | [1] [6] [30] | [36] [33] [13] [32] [34] [5] [9] | — |
| `#37` A efetividade desse uso cotidiano é comprovada pelo valor mediano das transações realizadas por pessoas físicas, que se… | [35] | — | [12] [9] [36] [13] ⚠ |
| `#48` Adicionalmente, a liquidação em tempo real garantiu a injeção imediata de caixa nos estabelecimentos, aprimorando a ges… | [17] [19] | [20] [13] [9] [36] [37] [3] [5] | — |
| `#53` Além de atuar como meio de pagamento, a trilha transacional aberta pelo Pix serviu de ponte para o acesso ampliado a pr… | [8] [10] [15] | [13] [37] [9] [38] [36] [5] | — |
| `#59` A velocidade de liquidação e o volume transacionado no Pix atraíram a atuação atrevida de redes criminosas especializad… | [22] [23] [29] | [12] [38] [9] [28] [36] [10] [13] [5] | — |
| `#101` A massificação da plataforma brought também a necessidade de aperfeiçoamentos constantes na segurança cibernética e no… | [22] [24] | [13] [36] [29] [9] [37] [38] | — |
| `#109` Por fim, recomenda-se avançar nas tratativas regulatórias e operacionais para a interconexão transfronteiriça do Pix co… | [2] [11] [19] | [36] [9] [18] [10] [20] [37] [13] [17] [38] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 3177543 |
| **Média de tokens por requisição** | 28626.5 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 4/40 (10.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 8.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[11]](https://www.jota.info/executivo/bc-apresenta-relatorio-do-pix-e-elenca-funcionalidades-em-desenvolvimento) | downloaded | 20 | 0 | 3 | 17 | 0 |
| [[24]](https://finsidersbrasil.com.br/pagamentos/pix/com-med-2-0-bc-quer-diminuir-falsos-positivos-e-rastrear-laranjas/) | downloaded | 17 | 2 | 7 | 8 | 0 |
| [[9]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf) | downloaded | 16 | 9 | 6 | 1 | 0 |
| [[17]](https://www.bis.org/publications/bulletin-52-central-banks-monetary-system-and-public-payment-infrastructures-lessons-brazils-pix) | downloaded | 16 | 2 | 5 | 9 | 0 |
| [[29]](https://valid.com/futuroid/b2b-med-2-0-e-regras-antifraude-do-pix) | downloaded | 16 | 5 | 7 | 4 | 0 |
| [[39]](https://www.bcb.gov.br/conteudo/home-ptbr/TextosApresentacoes/Apresentacao_GabrielGalipolo_FebrabanTech_24.8.2026.pdf) | downloaded | 14 | 3 | 5 | 6 | 0 |
| [[23]](https://www.matera.com/br/blog/med-mecanismo-especial-de-devolucao/) | downloaded | 13 | 6 | 4 | 3 | 0 |
| [[36]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2023.pdf) | downloaded | 13 | 6 | 6 | 1 | 0 |
| [[1]](https://www.bcb.gov.br/detalhenoticia/744/noticia) | downloaded | 10 | 0 | 0 | 10 | 0 |
| [[10]](https://www.gov.br/fazenda/pt-br/composicao/orgaos/orgaos-colegiados/crsfn/acesso-a-informacao/noticias/2026/pix-consolida-lideranca-nos-pagamentos-digitais-e-projeta-novas-evolucoes-ate-2030) | downloaded | 10 | 2 | 5 | 3 | 0 |
| [[35]](https://movimentoeconomico.com.br/economia/2026/08/11/chaves-pix-chegam-a-920-milhoes-e-sistema-movimenta-r-35-tri-em-2025/) | downloaded | 10 | 6 | 3 | 1 | 0 |
| [[5]](https://www.bcb.gov.br/noticiablogbc/40/noticia) | downloaded | 9 | 1 | 3 | 5 | 0 |
| [[3]](https://agenciabrasil.ebc.com.br/economia/noticia/2026-10/pix-ultrapassa-1-bilhao-de-chaves-cadastradas-no-brasil) | downloaded | 8 | 5 | 2 | 1 | 0 |
| [[8]](https://exame.com/invest/minhas-financas/numero-de-jovens-com-acesso-a-credito-dobra-no-brasil-em-oito-anos/) | downloaded | 7 | 1 | 2 | 4 | 0 |
| [[13]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RCF/relatorio_de_cidadania_financeira_2025.pdf) | downloaded | 7 | 3 | 3 | 1 | 0 |
| [[25]](https://www.tupi.fm/economia/vitima-sofre-golpe-do-pix-banco-recebedor-demora-48-horas-para-bloquear-conta-de-laranja-e-justica-condena-instituicao-a-pagar-todo-o-desfalque/) | downloaded | 7 | 5 | 1 | 1 | 0 |
| [[19]](https://www.bcb.gov.br/conteudo/home-ptbr/TextosApresentacoes/Central%20Bank%20of%20Brazil%20-%20The%20Pix%20Case%20-%20Lessons%20for%20Enhancing%20Cross%20Border.pdf) | downloaded | 6 | 0 | 3 | 3 | 0 |
| [[22]](https://www.bcb.gov.br/estabilidadefinanceira/pix-seguranca) | downloaded | 6 | 0 | 0 | 6 | 0 |
| [[2]](https://www.facebook.com/Febraban/videos/atualmente-86-da-popula%C3%A7%C3%A3o-adulta-brasileira-usa-o-pix-segundo-o-banco-central-d/1388563870084565/) | downloaded | 5 | 0 | 1 | 4 | 0 |
| [[4]](https://www.bcb.gov.br/estabilidadefinanceira/estatisticaspix) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[6]](https://www.bcb.gov.br/estatisticas/spbadendos) | downloaded | 5 | 0 | 0 | 5 | 0 |
| [[15]](https://www.elibrary.imf.org/view/journals/002/2023/289/article-A004-en.xml) | blocked | 5 | 0 | 0 | 0 | 5 |
| [[30]](https://www.infinitepay.io/blog/fim-do-doc-15-janeiro) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[38]](https://repositorio.animaeducacao.com.br/bitstreams/f2ef5c01-a7c9-413d-8edf-e684deb2af3a/download) | downloaded | 4 | 0 | 4 | 0 | 0 |
| [[28]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Guia_MED.pdf) | downloaded | 3 | 2 | 0 | 1 | 0 |
| [[34]](https://qitech.blog/doc-e-ted-diferencas/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[7]](https://dadosabertos.bcb.gov.br/dataset/pix) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[12]](https://theshift.info/hot/relatorio-gestao-pix-2025-banco-central/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[18]](https://africanenda.org/travel-notes-converging-forces-for-inclusion-lessons-from-pix-brazil) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[21]](https://ideas.repec.org/a/spr/eurase/v15y2025i2d10.1007_s40822-024-00300-z.html) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[32]](https://blog.reclameaqui.com.br/febraban-anuncia-o-fim-das-transferencias-por-doc/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[33]](https://creci-pb.gov.br/fim-do-ted-e-doc-banco-central-divulga-taxa-para-o-pix-r-001-a-cada-10-transacoes/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[37]](https://www.zoop.com.br/blog/negocios/arranjo-de-pagamento) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[40]](https://finsidersbrasil.com.br/pagamentos/pix/um-ano-depois-pix-automatico-ainda-nao-pegou-e-ha-um-motivo/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[27]](https://www12.senado.leg.br/verifica/materias-especiais/2026/pix-fui-vitima-de-golpe-como-recuperar-meu-dinheiro) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[31]](https://www.youtube.com/watch?v=nfowUjwwX5U) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[14]](https://borgenproject.org/financial-inclusion/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[16]](https://www.youtube.com/watch?v=sbBqMCzbN8U) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://aaltodoc.aalto.fi/bitstreams/852afc8d-f6a5-4c38-a826-127fab9805e6/download) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://www.facebook.com/jornaljangadeiro/videos/confira-os-detalhesa-atualiza%C3%A3o-do-mecanismo-especial-de-devolu%C3%A7%C3%A3o-do-pix-entro/877247651842447/) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[11]](https://www.jota.info/executivo/bc-apresenta-relatorio-do-pix-e-elenca-funcionalidades-em-desenvolvimento) | — | #85, #87, #107 | #80, #82–84, #86, #88–98, #109 | `#85` Banco Central trabalha no PIX por aproximação offline e em melhorias de segurança, entre outros temas. |
| [[24]](https://finsidersbrasil.com.br/pagamentos/pix/com-med-2-0-bc-quer-diminuir-falsos-positivos-e-rastrear-laranjas/) | #69, #92 | #64, #67–68, #90, #101–102, #105 | #60, #66, #72, #91, #93–94, #106, #74 ⚡ | `#69` o BC desenvolveu o MED 2.0 para conseguir rastrear o caminho do dinheiro para além da primeira conta que recebe os recursos originalmente |
| [[9]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf) | #80, #82, #85–86, #88, #92, #94–96 | #83, #87, #90–91, #93, #107 | #84 | `#80` A agenda evolutiva do Pix constitui o conjunto estruturado de iniciativas voltadas à ampliação das funcionalidades, ao aprimoramento dos mecanismos de seguranç… |
| [[17]](https://www.bis.org/publications/bulletin-52-central-banks-monetary-system-and-public-payment-infrastructures-lessons-brazils-pix) | #10, #99 | #8–9, #22, #39, #100 | #2, #11–12, #15, #18, #41, #47–48, #110 | `#10` The two key ingredients in the success of Pix are, first, the mandatory participation of large banks to kick-start network effects for users, and second, the c… |
| [[29]](https://valid.com/futuroid/b2b-med-2-0-e-regras-antifraude-do-pix) | #60, #65, #67, #69, #106 | #59, #72, #74, #78, #102, #105, #108 | #0–1, #70, #79 | `#60` o Bacen ataca diretamente o modelo de negócios do crime organizado fundamentado na abertura de "contas-laranja" e "mulas financeiras" para pulverização de capi… |
| [[39]](https://www.bcb.gov.br/conteudo/home-ptbr/TextosApresentacoes/Apresentacao_GabrielGalipolo_FebrabanTech_24.8.2026.pdf) | #32, #35–36 | #23, #57–58, #78–79 | #45–46, #56, #63, #103, #108 | `#32` R$ 35 trilhões ... movimentados pela plataforma ao longo de 2025 ... 80 bilhões ... de transações realizadas por Pix em 2025 |
| [[23]](https://www.matera.com/br/blog/med-mecanismo-especial-de-devolucao/) | #68–73 | #64, #67, #102, #105 | #59, #65–66 | `#68` trouxeram um processo mais robusto para rastrear movimentações suspeitas e aumentar as chances de recuperação dos valores desviados. Na prática, o foco da atua… |
| [[36]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2023.pdf) | #7–8, #14, #16, #88, #99 | #13, #15, #17, #80–81, #89 | #27 | `#7` Em 3 de novembro de 2020, começou a operação restrita, quando as instituições participantes do Pix disponibilizaram a uma parcela reduzida de seus clientes a o… |
| [[1]](https://www.bcb.gov.br/detalhenoticia/744/noticia) | — | — | #7, #17, #21–22, #24–25, #34, #42–43, #100 | — |
| [[10]](https://www.gov.br/fazenda/pt-br/composicao/orgaos/orgaos-colegiados/crsfn/acesso-a-informacao/noticias/2026/pix-consolida-lideranca-nos-pagamentos-digitais-e-projeta-novas-evolucoes-ate-2030) | #22, #110 | #8, #10, #31, #39, #100 | #16, #53–54 | `#22` O relatório evidencia o crescimento contínuo do sistema. Em 2025, o Pix registrou quase 80 bilhões de transações e movimentou mais de R$35 trilhões. Ao final d… |
| [[35]](https://movimentoeconomico.com.br/economia/2026/08/11/chaves-pix-chegam-a-920-milhoes-e-sistema-movimenta-r-35-tri-em-2025/) | #32, #38, #42, #49–51 | #31, #34, #37 | #43 ⚡ | `#32` o sistema de pagamentos instantâneos registrou quase **80 bilhões** de transações, aumento de **25,7%** sobre **2024**. O volume financeiro movimentado superou… |
| [[5]](https://www.bcb.gov.br/noticiablogbc/40/noticia) | #40 | #5, #38, #41 | #2–4, #25, #39 | `#40` Monique de Abreu Azevedo, Breno Santana Lobo, Alex Nery Caetité e Daniel Palaro Canhete são servidores do Banco Central do Brasil e atuam no Departamento de Co… |
| [[3]](https://agenciabrasil.ebc.com.br/economia/noticia/2026-10/pix-ultrapassa-1-bilhao-de-chaves-cadastradas-no-brasil) | #14, #26, #28–30 | #11, #27 | #13 | `#26` O número de chaves Pix cadastradas no Brasil ultrapassou a marca de 1 bilhão em setembro, segundo dados do Banco Central (BC). Ao todo, o sistema contabilizava… |
| [[8]](https://exame.com/invest/minhas-financas/numero-de-jovens-com-acesso-a-credito-dobra-no-brasil-em-oito-anos/) | #55 | #57–58 | #53–54, #103–104 | `#55` O número de pessoas entre 15 e 29 anos com alguma operação ativa ou limite de crédito disponível passou de 13,7 milhões em 2016 para 27,6 milhões em 2024, cres… |
| [[13]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RCF/relatorio_de_cidadania_financeira_2025.pdf) | #35, #56, #104 | #2, #9, #58 | #103 | `#35` cuja adoção, até o final de 2023, já alcançava mais de 70% da população de baixa renda. Este boxe analisa a evolução da inclusão financeira da população de bai… |
| [[25]](https://www.tupi.fm/economia/vitima-sofre-golpe-do-pix-banco-recebedor-demora-48-horas-para-bloquear-conta-de-laranja-e-justica-condena-instituicao-a-pagar-todo-o-desfalque/) | #61, #66, #75–77 | #108 | #73 | `#61` O **Mecanismo Especial de Devolução (MED)** foi criado pelas **Resoluções BCB nº 103/2021 e nº 147/2021 do Banco Central do Brasil** para padronizar o estorno… |
| [[19]](https://www.bcb.gov.br/conteudo/home-ptbr/TextosApresentacoes/Central%20Bank%20of%20Brazil%20-%20The%20Pix%20Case%20-%20Lessons%20for%20Enhancing%20Cross%20Border.pdf) | — | #48, #95, #109 | #45–46, #98 | `#48` Payments in a few seconds, with immediate availability of funds to the final beneficiary |
| [[22]](https://www.bcb.gov.br/estabilidadefinanceira/pix-seguranca) | — | — | #59–62, #74, #101 | — |
| [[2]](https://www.facebook.com/Febraban/videos/atualmente-86-da-popula%C3%A7%C3%A3o-adulta-brasileira-usa-o-pix-segundo-o-banco-central-d/1388563870084565/) | — | #23 | #96–98, #109 | `#23` Atualmente, 86% da população adulta brasileira usa o Pix, segundo o Banco Central do Brasil. |
| [[4]](https://www.bcb.gov.br/estabilidadefinanceira/estatisticaspix) | — | — | #23, #31, #33–34, #81 | — |
| [[6]](https://www.bcb.gov.br/estatisticas/spbadendos) | — | — | #11–12, #21, #24, #97 | — |
| [[30]](https://www.infinitepay.io/blog/fim-do-doc-15-janeiro) | #20 | #3, #19 | #21 | `#20` a Febraban (Federação Brasileira de Bancos) soltou um comunicado dizendo que, a partir de 15 de janeiro de 2024, o DOC (Documento de Ordem de Crédito) e a TEC… |
| [[38]](https://repositorio.animaeducacao.com.br/bitstreams/f2ef5c01-a7c9-413d-8edf-e684deb2af3a/download) | — | #0–1, #5–6 | — | `#0` o impacto do PIX no SFN é a democratização do mundo de pagamentos e a redução das barreiras de entrada criadas por grandes instituições. |
| [[28]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Guia_MED.pdf) | #62–63 | — | #61 | `#62` O Mecanismo Especial de Devolução (MED), conforme disposto na Seção II do Capítulo XI do Regulamento do Pix, é o conjunto de regras que permite que o PSP de um… |
| [[34]](https://qitech.blog/doc-e-ted-diferencas/) | #20 | #3, #19 | — | `#20` Essas transações diminuíram significativamente nos últimos anos, representando um total de apenas 3.7% de operações realizadas em 2022. ... a descontinuação de… |
| [[7]](https://dadosabertos.bcb.gov.br/dataset/pix) | — | — | #13–14 | — |
| [[12]](https://theshift.info/hot/relatorio-gestao-pix-2025-banco-central/) | — | #8–9 | — | `#8` Com apenas cinco anos de existência, o Pix tornou-se "Infraestrutura Pública Digital essencial para o bom funcionamento da economia", como descreve o Banco Cen… |
| [[18]](https://africanenda.org/travel-notes-converging-forces-for-inclusion-lessons-from-pix-brazil) | #99 | #110 | — | `#99` Pix is an amazing case of a country believing in DPI's potential to transform its development trajectory and deliver inclusive outcomes for consumers, business… |
| [[21]](https://ideas.repec.org/a/spr/eurase/v15y2025i2d10.1007_s40822-024-00300-z.html) | — | — | #49, #52 | — |
| [[32]](https://blog.reclameaqui.com.br/febraban-anuncia-o-fim-das-transferencias-por-doc/) | #20 | #19 | — | `#20` a Federação Brasileira de Bancos (Febraban) anunciou que os bancos associados à instituição deixarão de oferecer operações bancárias por DOC ... a descontinuaç… |
| [[33]](https://creci-pb.gov.br/fim-do-ted-e-doc-banco-central-divulga-taxa-para-o-pix-r-001-a-cada-10-transacoes/) | — | #4, #17 | — | `#4` Além disso as operações são “caras” e o cliente dos bancos chega a pagar até R$ 19 por transação. |
| [[37]](https://www.zoop.com.br/blog/negocios/arranjo-de-pagamento) | #44 | — | #47 | `#44` Conforme apontado na pesquisa da Zoop em parceria com a QualiBest, os brasileiros optam por esse meio de pagamento porque é: - mais prático (76%); - dispensa l… |
| [[40]](https://finsidersbrasil.com.br/pagamentos/pix/um-ano-depois-pix-automatico-ainda-nao-pegou-e-ha-um-motivo/) | #82 | #84 | — | `#82` tem o melhor potencial |
| [[27]](https://www12.senado.leg.br/verifica/materias-especiais/2026/pix-fui-vitima-de-golpe-como-recuperar-meu-dinheiro) | — | — | #107 | — |
| [[31]](https://www.youtube.com/watch?v=nfowUjwwX5U) | — | — | #20 | — |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Bloqueadas por barreira de acesso

- https://www.elibrary.imf.org/view/journals/002/2023/289/article-A004-en.xml — anti_bot — barreira de acesso (anti_bot): JavaScript is disabled In order to continue, we need to verify that you're not a robot. This requires JavaScript. Enable

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-5`** [5] [38]
  - Trecho: O cenário de desbancarização sofreu um forte catalisador de mudança durante a emergência sanitária provocada pela pandemia de COVID-19 em 2020.
  - Justificativa: A evidência mostra repetidamente que a pandemia de COVID-19 foi um catalisador de mudança no cenário de inclusão financeira e bancarização, acelerando a digitalização de pagamentos e a inclusão de milhões de não bancari…
  - Suporte veio de: [38] [5]
  - Evidência: “como a pandemia da COVID-19 acelerou e incentivou esse processo”
  - Não coberto pela evidência: O ano exato '2020' não é explicitamente citado como o ano do catalisador em todas as referências, embora seja implícito
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [38] | parcial | como a pandemia da COVID-19 acelerou e incentivou esse processo |
    | [5] | parcial | O surgimento do Pix e a crescente inclusão digital financeira, também impulsionada pela pandemia, pode ter contribuído… |

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-7`** [1] [15] [36]
  - Trecho: Foi nesse contexto de acelerada transição digital que o Banco Central do Brasil (BCB) lançou o ecossistema Pix em novembro de 2020.
  - Justificativa: A evidência confirma que o Pix foi lançado em novembro de 2020 (operação restrita em 3/11/2020 e operação plena em 16/11/2020) e que o contexto era de revolução digital com adoção de novas tecnologias pela população, su…
  - Suporte veio de: [36]
  - Evidência: “Em 3 de novembro de 2020, começou a operação restrita”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [36] | sustenta | Em 3 de novembro de 2020, começou a operação restrita, quando as instituições participantes do Pix disponibilizaram a u… |

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-8`** [10] [12] [17] [36]
  - Trecho: Concebido sob a premissa de funcionar como uma Infraestrutura Pública Digital (DPI), o Pix foi estruturado com o objetivo estratégico de democratizar o acesso aos serviços financeiros, intensificar a competição bancária…
  - Justificativa: Os objetivos estratégicos listados na afirmação são diretamente sustentados pelo Relatório de Gestão do Pix (e1d223cef2b8e3ba), que enumera explicitamente: democratizar o acesso, fomentar competição, promover eficiência…
  - Suporte veio de: [36] [12] [17]
  - Evidência: “Mais especificamente, o Pix foi criado com os seguintes objetivos: diminuir o uso de dinheiro em espécie e promover maior digitalização dos meios de pagamento; fomentar a competição e promover a eficiência do mercado de…”
  - Não coberto pela evidência: O termo 'Infraestrutura Pública Digital (DPI)' não aparece explicitamente como premissa de concepção no relatório 2020-2022; é usado retrospectivamente no relatório 2023-2025.; A expressão exata 'competição bancária' não é usada; o texto fala em 'competição' e 'concorrência no Sistema Financeiro Nacional'.; A expressão 'reduzir custos operacionais para a economia real' não é literal; o texto fala em 'reduzir o custo das transações eletrônicas' e viabilizar modelos de negócio 'nas demais atividades da economia real'.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [36] | sustenta | Mais especificamente, o Pix foi criado com os seguintes objetivos: [...] fomentar a competição e promover a eficiência… |
    | [12] | parcial | Com apenas cinco anos de existência, o Pix tornou-se "Infraestrutura Pública Digital essencial para o bom funcionamento… |
    | [10] | parcial | O documento demonstra como o sistema evoluiu de uma inovação voltada à modernização dos pagamentos para uma infraestrut… |
    | [17] | parcial | Public payment infrastructures build on the central bank's foundational role in the monetary system by promoting compet… |

  - Verificação: reclassificado para SUPPORTED na etapa `context_expansion` (baseline dizia: "A maior parte dos objetivos estratégicos citados (democratização do acesso, competição bancária, eficiência do mercado de pagamentos de var…") — cascata: baseline → context_expansion
### UNSUPPORTED

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-0`** [15] [29] [38]
  - Trecho: A estrutura do Sistema Financeiro Nacional (SFN) brasileiro foi historicamente marcada por uma elevada concentração bancária, altas tarifas operacionais e barreiras geográficas e socioeconômicas expressivas para a popul…
  - Justificativa: A CLAIM possui três componentes: (1) elevada concentração bancária, (2) altas tarifas operacionais e (3) barreiras geográficas e socioeconômicas para população de menor renda. A evidência apoia parcialmente o item 3, ci…
  - Suporte veio de: [38]
  - Não coberto pela evidência: elevada concentração bancária (não explicitamente mencionada na evidência); altas tarifas operacionais (não mencionadas em nenhuma parte da evidência)
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [29] | ausente | — |
    | [38] | parcial | o impacto do PIX no SFN é a democratização do mundo de pagamentos e a redução das barreiras de entrada criadas por gran… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-1`** [29] [38]
  - Trecho: Antes do advento da tecnologia de pagamentos instantâneos, estimava-se que aproximadamente 70 milhões de cidadãos viviam em condição de exclusão financeira ou sub-bancarização no país, enfrentando acesso precário aos se…
  - Justificativa: The claim attributes the figure of 70 million to financial exclusion/under-banking, but the evidence shows that 70 million refers to precarious or absent internet access, while the number of unbanked people is 45 millio…
  - Evidência: “Dados recentes, publicados pelo site do UOL da Folha de São Paulo, em 20 de maio de 2020, revelam que 70 milhões de brasileiros têm acesso precário ou sequer têm acesso a internet.”
  - Não coberto pela evidência: The figure of ~70 million attributed to financial exclusion/under-banking (evidence shows 45 million unbanked; 70 million refers to internet access); The framing of this as a condition 'before the advent of instant payment technology'; The assertion that this population depended 'almost exclusively' on paper money for daily exchanges
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [29] | ausente | — |
    | [38] | parcial | o país ainda enfrenta um cenário bastante desafiador no que tange à marginalização da inclusão financeira no Brasil |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-2`** [5] [13] [17]
  - Trecho: Essa dependência da moeda física perpetuava um círculo vicioso de vulnerabilidade econômica, ao restringir a criação de histórico financeiro para trabalhadores informais, dificultar a reserva de poupança e impor altos c…
  - Justificativa: A evidência sustenta de forma isolada que a moeda física implica altos custos de circulação, armazenamento e distribuição, e que trabalhadores informais/MEIs enfrentam ausência de histórico financeiro. No entanto, o CLA…
  - Suporte veio de: [13] [5]
  - Evidência: “A utilização da moeda física, por seu turno, implica altos custos de circulação, de armazenamento e de distribuição, bem como está associada a problemas como a corrupção, a lavagem de dinheiro e a segurança.”
  - Não coberto pela evidência: causalidade entre dependência da moeda física e restrição de histórico financeiro para trabalhadores informais; dificultar a reserva de poupança por conta da moeda física; impor altos custos operacionais especificamente ao comércio periférico
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | ausente | — |
    | [13] | parcial | trabalhadores da economia informal, que, por muito tempo, possuíam dificuldade em comprovar sua renda e que, agora com… |
    | [17] | ausente | — |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-43`** [1] [35]
  - Trecho: Enquanto nos primeiros meses após o lançamento em 2020 as operações P2B representavam cerca de 10% do total movimentado no Pix, essa fatia expandiu-se continuamente até atingir a faixa de 41% a 43% do total de transaçõe…
  - Justificativa: A evidência afirma que em 2020, 85% das transações eram P2P, e que P2B chegou a 43% em 2025, com avanço de 37 pontos percentuais em cinco anos. Isso implica que P2B começou em aproximadamente 6% (43% − 37pp), e não 'cer…
  - Suporte veio de: [35]
  - Evidência: “Em 2020, 85% das transações eram entre pessoas físicas (P2P). Em 2025, as operações de pessoas físicas para pessoas jurídicas (P2B) chegaram a 43% do total, avanço de 37 pontos percentuais em cinco anos.”
  - Não coberto pela evidência: P2B representava 'cerca de 10%' nos primeiros meses após o lançamento em 2020 — a evidência implica ~6% (43% − 37pp); A fatia expandiu-se 'continuamente' — a evidência não descreve continuidade; Faixa de '41% a 43%' — a evidência menciona apenas 43%
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [35] | contradiz | Em 2020, 85% das transações eram entre pessoas físicas (P2P). Em 2025, as operações de pessoas físicas para pessoas jur… |
    | [1] | ausente | — |

- **Trecho citado `pix_brasil_0fa70f936311_20261101T184422Z-74`** [22] [24] [29]
  - Trecho: Paralelamente, o prazo concedido para que o usuário vítima de golpe possa solicitar a contestação e a abertura do MED junto ao seu banco foi estendido de 30 para até 80 dias.
  - Justificativa: A evidência principal [891db28797a5c29e] afirma explicitamente que o MED JÁ concedia 80 dias para quem enviou a transferência (a vítima) solicitar a devolução. A ampliação de 30 para 80 dias beneficia quem RECEBEU o Pix…
  - Suporte veio de: [29]
  - Evidência: “O **Banco Central** (BC) ampliou de 30 para 80 dias o prazo para contestar devoluções do Pix suspeitas de fraude por meio do **Mecanismo Especial de Devolução** (MED).”
  - Não coberto pela evidência: A afirmativa atribui a extensão de 30 para 80 dias à vítima do golpe, mas a evidência [891db28797a5c29e] indica que a vítima (quem enviou a transferência) já tinha 80 dias e que a mudança de 30→80 beneficia o recebedor que contesta a devolução.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [24] | contradiz | o MED já concede 80 dias para que quem enviou a transferência solicite a devolução. Agora, a mudança beneficia a empres… |
    | [29] | parcial | A ampliação para até 80 dias garante tempo hábil para contestar a operação sem perder o direito de acionar a infraestru… |
    | [22] | ausente | — |
