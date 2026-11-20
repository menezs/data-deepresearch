# Relatório de Auditoria — Gemini (pix_brasil_ef6e79f227f4_20261115T164301Z)

**Arquivo auditado:** `answers/Ingles/Gemini/EmConsolidacao/pix_brasil.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | pix_brasil_ef6e79f227f4_20261115T164301Z |
| **Ferramenta** | Gemini |
| **Gerado em** | 2026-11-15T17:33:03.139809+00:00 |
| **Total de trechos citados** | 112 |
| **Tempo de processamento** | 0:00:50:02 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 3074.9 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-11-15 16:43:15+00:00 |
| Citações no corpo | 112 marcadores, 36 distintos |
| Referências listadas | 67 (31 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 42 | 37.5% |
| **UNSUPPORTED** | 52 | 46.4% |
| **CONTRADICTED** | 4 | 3.6% |
| **SKIPPED** | 14 | 12.5% |
| **TOTAL** | 112 | 100.0% |

Sobre os 98 trechos citados auditados: SUPPORTED 42,85%, UNSUPPORTED 53,06%, CONTRADICTED 4,08%.

> **21 dos 42 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 21 estão **contados dentro** dos 42 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`56` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `12` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `4` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `12` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` By December 2025, 148.13 million unique individuals—roughly 86 percent of Brazilian adults—and 12.8 million businesses… | [1] | [26] [2] [18] [24] [9] [4] | — |
| `#9` Before Pix arrived, Brazil suffered from a sharp gap between nominal bank registration and active financial participati… | [17] | [9] [24] [18] [2] [36] [33] [4] | — |
| `#17` DICT links simple user aliases—taxpayer IDs (CPF or CNPJ), mobile numbers, emails, or random keys—to transactional acco… | [3] | [4] [21] [18] [24] [2] | — |
| `#19` First, participation was mandated for all institutions with more than 500,000 active transactional accounts—covering 38… | [3] | [9] [18] [2] [24] [4] | — |
| `#23` Formal banking relationships in BCB registries reached 96 percent of adults in 2020, and Caixa registered 25.9 million… | [24] | [18] [25] [19] [2] [17] | — |
| `#28` By late 2025, total registered keys exceeded 920 million (875.4 million individual and 44.7 million corporate), and use… | [1] | [2] [24] [18] [25] | — |
| `#36` Physical currency also contracted after its 2020 pandemic peak: banknotes in circulation fell from 8.54 billion notes i… | [33] | [34] [2] [18] [28] [35] [25] [24] | — |
| `#52` Meanwhile, analog cash-out bridges inside Pix struggled to gain traction. | [26] | — | [9] [18] [2] [24] ⚠ |
| `#78` Judicial and social-policy responses revealed sharp enforcement limits. | [39] | [10] [40] [9] [12] | — |
| `#89` To stop abusive "false MED" reversals against merchants, Normative Instruction BCB No. 766/2026 took effect in Septembe… | [50] | [45] [51] [48] [2] [11] [49] | — |
| `#90` Nonetheless, administrative restitution remains limited and legally contested. | [11] | [45] [10] [4] [24] [50] | — |
| `#98` Even then, a February 2026 intrusion at banking-tech provider JD Consultores forced another temporary Pix suspension. | [13] | [9] [53] [18] [12] [2] [4] [45] | — |
| `#103` Closing Brazil’s credit gap increasingly centers on linking Pix cash-flow data with Open Finance. | [15] | [9] [18] [24] [4] [62] [60] [63] [36] [2] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2171447 |
| **Média de tokens por requisição** | 22157.6 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 31/67 (46.3%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 4.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[2]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf) | downloaded | 18 | 7 | 9 | 2 | 0 |
| [[6]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RIF/relatorio_de_cidadania_financeira_2025.pdf) | inaccessible | 14 | 0 | 0 | 0 | 14 |
| [[3]](https://www.bis.org/publications/bulletin-52-central-banks-monetary-system-and-public-payment-infrastructures-lessons-brazils-pix) | downloaded | 6 | 0 | 6 | 0 | 0 |
| [[7]](https://sintrajud.org.br/conteudo/16435/bets-no-stf-proibicao-expoe-impacto-das-apostas-sobre-familias-e-provoca-reacao) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[12]](https://vigilant.com.br/cm-software-pix-banco-central-um-ano-depois/) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[22]](https://www.trio.com.br/resources/estatisticas-pix) | downloaded | 5 | 0 | 5 | 0 | 0 |
| [[1]](https://www.bcb.gov.br/detalhenoticia/21227/noticia) | downloaded | 4 | 0 | 0 | 4 | 0 |
| [[9]](https://www.ssarkisyan.com/publication/instantpayments/instant_payments.pdf) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[11]](https://datarudder.com/med-pix/) | downloaded | 4 | 1 | 1 | 2 | 0 |
| [[17]](https://www.bcb.gov.br/nor/relcidfin/cap01.html) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[14]](https://exame.com/tecnologia/o-caminho-do-pix-ate-comunidades-ribeirinhas-da-amazonia/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[26]](https://theshift.info/hot/relatorio-gestao-pix-2025-banco-central/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[27]](https://www.bcb.gov.br/detalhenoticia/21300/nota) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[5]](https://www.bcb.gov.br/estabilidadefinanceira/pix-em-numeros-estatisticas?ref=elmomento.io) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[8]](https://crcma.org.br/noticias/pix-e-o-principal-meio-de-pagamento-adotado-pelos-pequenos-negocios) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[15]](https://celcoin.com.br/articles/integracao-pix-open-finance-credito/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[18]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Pix-Management-Report/pix_management_report_2023.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[24]](https://bcb.gov.br/content/publications/report_fincit/Report%20on%20Financial%20Citizenship%20-%202021.pdf) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[29]](https://www.serasa.com.br/carteira-digital/blog/fim-doc/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[33]](https://www.poder360.com.br/poder-tech/5-anos-de-pix-circulacao-de-dinheiro-diminui-e-bancarizacao-sobe/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[39]](https://www.gov.br/fundaj/pt-br/composicao/dipes-1/publicacoes/NotaTcnica39AnlisedoPoderdeCompraEquivalentePCE.pdf) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[45]](https://joaocoelho.adv.br/med-pix-2/) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[50]](https://jusdocs.com/blog/nova-regra-pix-med-2-0-sisbajud-teimosinha-prazos) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[65]](https://www.mercadopago.com.br/blog/drex-diferenca-real-digital-pix) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[4]](https://fastpayments.worldbank.org/sites/default/files/2022-05/Brazil_Pix_Case_Study_May_2022_0.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[13]](https://obastidor.com.br/investigacao/novo-ataque-ao-sistema-financeiro/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[16]](https://www.bcb.gov.br/detalhenoticia/21276/noticia) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[19]](https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/serie_cidadania/serie_cidadania_financeira_7_Global_Findex.pdf) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[21]](https://azify.com/blog/spi-dict-conta-pi-infraestrutura-pix) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://www.caixa.gov.br/Downloads/caixa-governanca/Relatorio_Integrado_Caixa_2020.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[36]](https://agenciabrasil.ebc.com.br/en/economia/noticia/2026-07/imf-praises-brazils-most-popular-payment-method-pix) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://am.agenciasebrae.com.br/inovacao-e-tecnologia/pix-e-a-principal-forma-de-pagamento-aos-pequenos-negocios-no-amazonas/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://www.migalhas.com.br/quentes/419984/stf-confirma-decisao-de-fux-e-impede-uso-de-bolsa-familia-em-bets) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.broadcast.com.br/ultimas-noticias/tcu-lares-que-recebem-bolsa-familia-gastaram-r-37-bilhoes-com-bets/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[43]](https://fpabramo.org.br/stf-suspende-todas-as-acoes-judiciais-contra-proibicao-de-bets-no-pais/) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[62]](https://agenciabrasil.ebc.com.br/radioagencia-nacional/economia/audio/2026-06/banco-central-da-mais-um-passo-na-integracao-entre-pix-e-open-finance) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[10]](https://www.stf.jus.br/arquivo/cms/audienciasPublicas/anexo/AudinciaPblica42ImpactosdasapostasonlinebetsnoBrasil.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?conteudo=PIX&tipoDocumento=Todos) | downloaded | 0 · nunca citada | — | — | — | — |
| [[23]](https://jornalcontabil.com.br/noticia/caixa-tem-libera-transferencia-via-pix-do-auxilio-emergencial/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[28]](https://finsidersbrasil.com.br/pagamentos/pix-domina-pagamentos-no-2o-semestre-de-2025-ted-e-cartoes-tambem-avancam/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[30]](https://blogs.correiobraziliense.com.br/vicente/devido-ao-pix-febraban-anuncia-fim-do-doc-em-29-de-fevereiro-de-2024/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://agenciabrasil.ebc.com.br/geral/noticia/2023-05/bancos-deixarao-de-operar-transferencias-por-doc-e-tec-ate-2024) | downloaded | 0 · nunca citada | — | — | — | — |
| [[32]](https://portal.febraban.org.br/noticia/3926/pt-br/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[34]](https://g1.globo.com/economia/noticia/2022/02/27/pix-e-fim-do-auxilio-emergencial-tiram-de-circulacao-r-45-bilhoes-em-cedulas-e-moedas-indica-bc.ghtml) | downloaded | 0 · nunca citada | — | — | — | — |
| [[35]](https://portal.febraban.org.br/noticia/4290/pt-br/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[38]](https://www.estadao.com.br/politica/luiz-fux-supremo-tribunal-federal-determina-governo-adote-medidas-impedir-apostas-recursos-bolsa-familia-nprp/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[42]](https://agenciabrasil.ebc.com.br/justica/noticia/2024-11/stf-confirma-decisao-que-proibiu-uso-de-beneficios-sociais-para-bets) | downloaded | 0 · nunca citada | — | — | — | — |
| [[44]](https://www.mattosfilho.com.br/unico/bcb-novas-normas-pix/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[46]](https://www.youtube.com/watch?v=vw0asx5w9zw) | downloaded | 0 · nunca citada | — | — | — | — |
| [[47]](https://www.demarest.com.br/forum-pix/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[48]](https://swapofinance.com/pt-br/blog/med-2-pix-devolucao-golpe-obrigatorio/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[49]](https://supplymidia.com.br/blog/med-2-0-o-risco-de-devolver-um-pix-recebido-por-engano/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[51]](https://valid.com/futuroid/b2b-med-2-0-e-regras-antifraude-do-pix) | downloaded | 0 · nunca citada | — | — | — | — |
| [[52]](https://www.bcb.gov.br/meubc/faqs/p/o-que-e-e-como-funciona-o-mecanismo-especial-de-devolucao-med) | downloaded | 0 · nunca citada | — | — | — | — |
| [[53]](https://agenciabrasil.ebc.com.br/economia/noticia/2025-07/bc-suspende-tres-instituicoes-do-pix-apos-ataque-cibernetico) | downloaded | 0 · nunca citada | — | — | — | — |
| [[54]](https://www.mobiletime.com.br/noticias/05/09/2025/bc-limita-em-r-15-mil-pix-de-fintechs-com-conexao-indireta-ao-spi/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[55]](https://g1.globo.com/jornal-nacional/noticia/2025/07/04/funcionario-de-empresa-de-tecnologia-confessa-que-facilitou-ataque-hacker-a-sistema-que-integra-bancos-ao-pix-por-r-15-mil.ghtml) | downloaded | 0 · nunca citada | — | — | — | — |
| [[56]](https://www.bcb.gov.br/detalhenoticia/20827/nota) | downloaded | 0 · nunca citada | — | — | — | — |
| [[57]](https://istoedinheiro.com.br/bc-limita-em-r-15-mil-valor-de-pix-e-ted-para-instituicoes-de-pagamento-nao-autorizadas) | downloaded | 0 · nunca citada | — | — | — | — |
| [[58]](https://okai.com.br/artigo/dispensa-temporaria-do-limite-de-r-15-mil-no-pix-e-na-ted-para-instituicoes-com-psti) | downloaded | 0 · nunca citada | — | — | — | — |
| [[59]](https://www.pluggy.ai/blog/open-finance-2026-novidades) | downloaded | 0 · nunca citada | — | — | — | — |
| [[60]](https://www.maps.com.br/atualizacoes-do-banco-central-pix-drex-e-open-finance-em-foco/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[61]](https://www.bcb.gov.br/detalhenoticia/21278/noticia) | downloaded | 0 · nunca citada | — | — | — | — |
| [[63]](https://www.bcb.gov.br/detalhenoticia/21170/noticia) | downloaded | 0 · nunca citada | — | — | — | — |
| [[64]](https://silvalopes.adv.br/pix-parcelado-o-que-e-e-como-funciona-a-esta-nova-funcionalidade-do-pix/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[66]](https://veja.abril.com.br/economia/emtenda-o-que-vai-mudar-no-drex-o-pix-2-0-do-bc/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[67]](https://g1.globo.com/economia/noticia/2026/10/01/pix-na-europa-conexao-pode-baratear-transferencias-e-reduzir-envio-a-segundos.ghtml) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[2]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2026.pdf) | #26–27, #30, #44, #48, #55–56 | #2, #20, #31, #47, #53, #86, #88, #101, #106 | #25, #46 ⚡ | `#26` Em 2020, ano de seu lançamento, o meio de pagamento era usado sobretudo para transações entre pessoas físicas (person to person – P2P), correspondendo a 85% da… |
| [[3]](https://www.bis.org/publications/bulletin-52-central-banks-monetary-system-and-public-payment-infrastructures-lessons-brazils-pix) | — | #8, #17–19, #63, #111 | — | `#8` Public payment infrastructures build on the central bank's foundational role in the monetary system by promoting competition and interoperability between payme… |
| [[7]](https://sintrajud.org.br/conteudo/16435/bets-no-stf-proibicao-expoe-impacto-das-apostas-sobre-familias-e-provoca-reacao) | #76–77 | #73–75 | — | `#76` Em 2025, os brasileiros depositaram R$ 220,6 bilhões nas bets legalizadas, segundo dados da Secretaria de Prêmios e Apostas do Ministério da Fazenda, divulgado… |
| [[12]](https://vigilant.com.br/cm-software-pix-banco-central-um-ano-depois/) | #94, #97, #99 | #96 | #95 ⚡ | `#94` A C&M Software não era um banco, não movimentava dinheiro de clientes finais e, até aquele momento, nem sequer era uma instituição regulada diretamente pelo Ba… |
| [[22]](https://www.trio.com.br/resources/estatisticas-pix) | — | #29, #32, #60, #92, #102 | — | `#29` R$ 110,4 tri movimentados desde novembro de 2020. |
| [[1]](https://www.bcb.gov.br/detalhenoticia/21227/noticia) | — | — | #0, #3, #28, #100 | — |
| [[9]](https://www.ssarkisyan.com/publication/instantpayments/instant_payments.pdf) | #40–41 | #24, #39 | — | `#40` The banking industry is highly concentrated, with large banks offering low deposit rates and holding significant market share (Drechsler, Savov, and Schnabl (2… |
| [[11]](https://datarudder.com/med-pix/) | #91 | #90 | #7, #84 | `#91` o MED não se aplica a desacordos comerciais sem fraude, Pix enviado para a pessoa errada por erro de quem pagou ou recursos que chegaram a um terceiro de boa-f… |
| [[17]](https://www.bcb.gov.br/nor/relcidfin/cap01.html) | #10–12 | #9 | — | `#10` Em 2017, mais de 140 milhões (86,5%) de pessoas mantinham algum relacionamento bancário [...] Os números do BCB revelam o universo de posse de contas cadastrad… |
| [[14]](https://exame.com/tecnologia/o-caminho-do-pix-ate-comunidades-ribeirinhas-da-amazonia/) | #49–51 | — | — | `#49` O número, porém, se concentra nos lares urbanos. Os três estados com menor proporção de domicílios conectados do país são Acre, com 75,2%, Amazonas, com 77,7%,… |
| [[26]](https://theshift.info/hot/relatorio-gestao-pix-2025-banco-central/) | #109 | #52, #83 | — | `#109` Hoje, o uso do Pix fora do Brasil já existe, mas só por meio de parcerias privadas entre instituições financeiras brasileiras e estrangeiras em países como Chi… |
| [[27]](https://www.bcb.gov.br/detalhenoticia/21300/nota) | #33, #37 | #38 | — | `#33` Nesse cenário destacamos que o Pix concentra a maior parte da quantidade de transações (55,2%), enquanto a TED responde pela maior parcela do volume financeiro… |
| [[5]](https://www.bcb.gov.br/estabilidadefinanceira/pix-em-numeros-estatisticas?ref=elmomento.io) | — | — | #1, #54 | — |
| [[8]](https://crcma.org.br/noticias/pix-e-o-principal-meio-de-pagamento-adotado-pelos-pequenos-negocios) | — | #59, #61 | — | `#59` 96% das pequenas empresas aceitam o sistema como alternativa de pagamento; entre os MEIs, adesão chega a 97% |
| [[15]](https://celcoin.com.br/articles/integracao-pix-open-finance-credito/) | — | #103, #105 | — | `#103` Dados transacionais do Pix combinados com informações de Open Finance permitem construir perfis de crédito mais precisos, o que reduz a dependência de garantia… |
| [[18]](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Pix-Management-Report/pix_management_report_2023.pdf) | #13, #15 | — | — | `#13` However, in 2019, cash was still the most widely used means of payment by Brazilians. Research on the habits of using means of payment revealed that [...] 77%… |
| [[24]](https://bcb.gov.br/content/publications/report_fincit/Report%20on%20Financial%20Citizenship%20-%202021.pdf) | #21 | #23 | — | `#21` Thus, on November 16, 2020, the BCB started the full operation of Pix. [...] A relevant part of this expansion seems to be related to the Federal Emergency Aid… |
| [[29]](https://www.serasa.com.br/carteira-digital/blog/fim-doc/) | #34 | #35 | — | `#34` DOC é sigla de Documento de Ordem de Crédito. Criado em 1985, ele serviu como um importante método de pagamento ao longo de quatro décadas [...] a finalização… |
| [[33]](https://www.poder360.com.br/poder-tech/5-anos-de-pix-circulacao-de-dinheiro-diminui-e-bancarizacao-sobe/) | #42 | #36 | — | `#42` O Pix pode ter contribuído para a abertura de até 115 contas por 1.000 adultos, o que ampliou a bancarização. O avanço do Pix desde 2020 pode explicar um aumen… |
| [[39]](https://www.gov.br/fundaj/pt-br/composicao/dipes-1/publicacoes/NotaTcnica39AnlisedoPoderdeCompraEquivalentePCE.pdf) | #81 | — | #78 | `#81` A Nota Técnica 39 analisa o impacto do Poder de Compra Equivalente (PCE), uma métrica que mede a capacidade das famílias beneficiárias do Programa Bolsa Famíli… |
| [[45]](https://joaocoelho.adv.br/med-pix-2/) | #85 | — | #87 ⚡ | `#85` O MED Pix 2.0, regulado pela Resolução BCB nº 493/2025 e obrigatório para todas as instituições desde 2 de fevereiro de 2026... A versão original do MED foi in… |
| [[50]](https://jusdocs.com/blog/nova-regra-pix-med-2-0-sisbajud-teimosinha-prazos) | — | #89 | #93 ⚡ | `#89` A mudança veio com a Instrução Normativa BCB nº 766, de 27 de julho de 2026 |
| [[65]](https://www.mercadopago.com.br/blog/drex-diferenca-real-digital-pix) | #108 | — | #107 | `#108` o modelo tecnológico original foi encerrado pelo Banco Central em novembro de 2025, abrindo espaço para uma nova abordagem com foco diferente. [...] Na nova fa… |
| [[4]](https://fastpayments.worldbank.org/sites/default/files/2022-05/Brazil_Pix_Case_Study_May_2022_0.pdf) | #14 | — | — | `#14` In May 2018, the Banco Central do Brasil (BCB) initiated the market discussion that led to the development of a new fast payment system PIX. [...] BCB acted to… |
| [[13]](https://obastidor.com.br/investigacao/novo-ataque-ao-sistema-financeiro/) | — | #98 | — | `#98` Um ataque hacker contra a JD Consultores, a principal empresa de fornecimento de serviços de tecnologia para bancos, expôs certificados digitais |
| [[16]](https://www.bcb.gov.br/detalhenoticia/21276/noticia) | — | — | #110 | — |
| [[21]](https://azify.com/blog/spi-dict-conta-pi-infraestrutura-pix) | #16 | — | — | `#16` O SPI opera no modelo LBTR — Liquidação Bruta em Tempo Real. Isso significa que cada transação é liquidada individualmente, de forma definitiva e irrevogável,… |
| [[25]](https://www.caixa.gov.br/Downloads/caixa-governanca/Relatorio_Integrado_Caixa_2020.pdf) | #22 | — | — | `#22` Fomos os responsáveis por operacionalizar o maior pagamento de programas sociais e de transferência de renda da história do Brasil: foram 611,55 milhões de pag… |
| [[36]](https://agenciabrasil.ebc.com.br/en/economia/noticia/2026-07/imf-praises-brazils-most-popular-payment-method-pix) | #43 | — | — | `#43` The International Monetary Fund (IMF) praised Pix as one of the main drivers of the transformation of the Brazilian financial system |
| [[37]](https://am.agenciasebrae.com.br/inovacao-e-tecnologia/pix-e-a-principal-forma-de-pagamento-aos-pequenos-negocios-no-amazonas/) | #62 | — | — | `#62` No Amazonas, o recurso do Pix como forma de pagamento é o mais comum para 58% dos micro e pequenos empreendedores, o que coloca o estado como o terceiro onde o… |
| [[40]](https://www.migalhas.com.br/quentes/419984/stf-confirma-decisao-de-fux-e-impede-uso-de-bolsa-familia-em-bets) | #79 | — | — | `#79` Por unanimidade, STF confirmou liminar do ministro Luiz Fux, que determinava ao governo adoção de medidas imediatas contra o uso de recursos de programas assis… |
| [[41]](https://www.broadcast.com.br/ultimas-noticias/tcu-lares-que-recebem-bolsa-familia-gastaram-r-37-bilhoes-com-bets/) | — | #80 | — | `#80` 663 famílias foram responsáveis por apostas que variam de R$ 100 mil a R$ 1,4 milhão. |
| [[43]](https://fpabramo.org.br/stf-suspende-todas-as-acoes-judiciais-contra-proibicao-de-bets-no-pais/) | — | #82 | — | `#82` determinou a suspensão de todas as ações eventualmente abertas no país contra a proibição das bets |
| [[62]](https://agenciabrasil.ebc.com.br/radioagencia-nacional/economia/audio/2026-06/banco-central-da-mais-um-passo-na-integracao-entre-pix-e-open-finance) | — | #104 | — | `#104` Agora, os correntistas podem optar pelo compartilhamento de saldo e limite ao conectar sua conta no Pix por aproximação em carteiras digitais ou ao autorizar m… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://www.bcb.gov.br/content/cidadaniafinanceira/documentos_cidadania/RIF/relatorio_de_cidadania_financeira_2025.pdf — download excedeu 90s

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-10`** [17]
  - Trecho: In 2017, BCB administrative records showed that over 140 million adults (86.5 percent) held formal banking relationships, whereas only 70 percent of Brazilian adults reported owning an account in that year’s Global Find…
  - Justificativa: Todos os elementos da afirmação estão diretamente sustentados pela evidência: (1) mais de 140 milhões (86,5%) de pessoas com relacionamento bancário em 2017 segundo dados do BCB; (2) 70% dos adultos brasileiros com cont…
  - Suporte veio de: [17]
  - Evidência: “Em 2017, mais de 140 milhões (86,5%) de pessoas mantinham algum relacionamento bancário, como contas de depósitos à vista (conhecidas popularmente como contas-correntes), contas de depósitos de poupança e contas-corrent…”
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-11`** [17]
  - Trecho: As BCB diagnostics noted, millions of registered accounts sat dormant with minimal balances, leaving holders unaware they even maintained active accounts.
  - Justificativa: A evidência sustenta os elementos centrais da afirmação: (1) diagnósticos do BCB mencionam contas cadastradas no SFN; (2) há menção a contas não encerradas com saldos muito baixos e sem movimentação por longos períodos;…
  - Suporte veio de: [17]
  - Evidência: “Esses dados incluem todas as contas não encerradas, até mesmo aquelas que possuem saldos muito baixos ou que não registraram saques, depósitos e transferências por períodos longos.”
  - Não coberto pela evidência: A palavra exata 'dormant' não aparece literalmente, embora o conceito de contas sem movimentação por longos períodos esteja presente.; A afirmação de que os titulares 'desconheciam' (unaware) é apresentada como possibilidade ('pode não se lembrar'), não como fato confirmado.
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-12`** [17]
  - Trecho: Exclusion followed stark regional and occupational lines: in 2017, banking penetration stood at 90.9 percent in the Southeast compared with 72.3 percent in the North, and just 20 percent of legalized individual microent…
  - Justificativa: A evidência confirma explicitamente todos os dados citados na afirmação: 90,9% de bancarização no Sudeste versus 72,3% no Norte, e 20% dos MEIs com relacionamento bancário como pessoa jurídica em 2017. A caracterização…
  - Suporte veio de: [17]
  - Evidência: “o percentual de adultos com relacionamento bancário por região varia, com a Região Sudeste apresentando o maior percentual – 90,9% –, e a Região Norte, o menor, 72,3%.”
### UNSUPPORTED

- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-0`** [1]
  - Trecho: Launched by the Central Bank of Brazil (Banco Central do Brasil, or BCB) in November 2020, Pix has transformed Brazil’s retail payment architecture into an essential national utility, extending active digital payment pa…
  - Justificativa: A evidência consiste apenas em listas de tópicos/navegação do site do Banco Central do Brasil, mencionando 'Pix' como item de menu, mas sem qualquer informação sobre data de lançamento, taxa de adoção, ou impacto na arq…
  - Não coberto pela evidência: Lançamento pelo Banco Central do Brasil (BCB); Data de lançamento: novembro de 2020; Transformação da arquitetura de pagamentos de varejo em utilidade nacional essencial
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-1`** [5]
  - Trecho: By September 2026, more than 150 million individuals used Pix in a single month, executing over 7.8 billion transactions worth more than R$ 3.8 trillion—exceeding three times Brazil’s monthly gross domestic product—and…
  - Justificativa: A evidência consiste apenas em listas de links de navegação do site do Banco Central do Brasil, incluindo seções como 'Estatísticas do Pix' e 'Pix em números', mas não contém nenhum dado numérico, estatística, data ou v…
  - Não coberto pela evidência: Mais de 150 milhões de indivíduos usaram Pix em um único mês até setembro de 2026; Execução de mais de 7,8 bilhões de transações; Valor superior a R$ 3,8 trilhões
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-2`** [2]
  - Trecho: Administrative and survey benchmarks confirm that this expansion coincided with a marked narrowing of formal access gaps: by the end of 2024, 175 million adults (96.4 percent of Brazil’s adult population) maintained for…
  - Justificativa: A evidência sustenta que 96,4% da população adulta possui conta e que ~88% são usuários ativos do SFN (RCF 2025). Porém, o número de 175 milhões de adultos não aparece na evidência; a referência ao '2024 World Bank Glob…
  - Suporte veio de: [2]
  - Evidência: “o Relatório de Cidadania Financeira (RCF) 2025, publicado pelo BC em abril de 2026, aponta que 96,4% da população adulta brasileira possui conta de depósitos ou de pagamento e que cerca de 88% dos adultos são usuários a…”
  - Não coberto pela evidência: 175 million adults — número não aparece na evidência; by the end of 2024 — a evidência refere-se ao RCF 2025 publicado em abril de 2026, sem indicar que os dados se referem ao final de 2024; self-reported account ownership climbed to 86% in the 2024 World Bank Global Findex survey — a evidência não menciona a pesquisa World Bank Global Findex; o 86% na evidência refere-se a usuários do Pix, não a posse de conta autorrelatada no Findex
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-46`** [2]
  - Trecho: Between 2020 and 2025, the Pix Management Report records a 103 percent expansion in individual SFN users (from 77 million to 152 million) and more than a threefold rise in corporate clients (from 3.5 million to 11.6 mil…
  - Justificativa: A afirmacao contem erros factuais em relacao a evidencia. Os dados de 103% de expansao de usuarios do SFN (77M para 152M) e o aumento de pessoas juridicas (3,5M para 11,6M) referem-se ao periodo 2018-2023, e nao 2020-20…
  - Evidência: “Entre 2018 e 2023, o número de usuários ativos do Sistema Financeiro Nacional (SFN) cresceu 103%, passando de 77 milhões para 152 milhões de pessoas físicas. No mesmo período, o número de pessoas jurídicas no sistema fi…”
  - Não coberto pela evidência: Periodo incorreto: a afirmacao diz 'Between 2020 and 2025' mas a evidencia diz 'Entre 2018 e 2023'; Atribuicao incorreta do relatorio: a afirmacao diz 'Pix Management Report' mas a evidencia atribui os dados ao 'Relatorio de Economia Bancaria (REB)'; A parte sobre a pesquisa CP2 Consultoria esta correta e sustentada pela evidencia
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-87`** [45]
  - Trecho: Payers gained an 80-day self-service dispute button in banking apps, while receiving providers face a 7-calendar-day investigation deadline (with sequential returns beginning 72 hours later and total payer notice due wi…
  - Justificativa: A afirmacao contem elementos contraditos e nao sustentados pela evidencia. O prazo de '7 dias corridos para investigacao' contradiz diretamente os '11 dias' citados na evidencia. O 'sweep continuo por 90 dias' nao apare…
  - Suporte veio de: [45]
  - Evidência: “O prazo de 80 dias para a vítima contestar continua o mesmo.”
  - Não coberto pela evidência: 7-calendar-day investigation deadline (evidencia diz 11 dias, nao 7); sequential returns beginning 72 hours later (apenas caso ilustrativo, nao regra geral); continuously sweep incoming balances for up to 90 days (nao mencionado na evidencia)
  - Verificação: reclassificado para CONTRADICTED na etapa `context_expansion` (baseline dizia: "A evidência sustenta o prazo de 80 dias e a contestação por autoatendimento no aplicativo, e o prazo de 11 dias para o banco informar se ac…") — cascata: baseline → context_expansion
- **Trecho citado `pix_brasil_ef6e79f227f4_20261115T164301Z-93`** [50]
  - Trecho: Meanwhile, judicial protection tightened: in May 2026 (finalized July 2026), Brazil’s Superior Court of Justice (STJ) ruled in Tema 1.325 that when Pix transfers aligned with a client’s historical account profile, losse…
  - Justificativa: A claim atribui ao Tema 1.325 do STJ uma decisão sobre transferências por Pix compatíveis com o perfil do cliente e culpa exclusiva da vítima. Contudo, a evidência mostra que o Tema 1.325 trata da 'teimosinha' (reiteraç…
  - Evidência: “Em 7/5/2026, a Primeira Seção do STJ julgou o Tema 1.325, sob relatoria do Ministro Sérgio Kukina, nos REsps n. 2.147.428/RS, n. 2.147.843/SC e n. 2.193.695/RS”
  - Não coberto pela evidência: A associação do Tema 1.325 à decisão sobre Pix e culpa exclusiva da vítima está incorreta segundo a evidência

---

## 10. Trechos Citados Não Auditados

Motivos: 14 citam referência não baixada/inacessível.

- `pix_brasil_ef6e79f227f4_20261115T164301Z-4` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-5` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-6` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-45` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-57` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-58` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-64` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-65` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-66` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-68` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-69` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-70` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-71` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `pix_brasil_ef6e79f227f4_20261115T164301Z-72` — Referencia(s) citada(s) ['ce4ef0b8fb18629f'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).