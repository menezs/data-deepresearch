# Relatório de Auditoria — Claude (escravidao_brasil_fa0dd5de0e8e_20261115T021304Z)

**Arquivo auditado:** `answers/Ingles/Claude/Consolidado/escravidao_brasil.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | escravidao_brasil_fa0dd5de0e8e_20261115T021304Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-15T02:40:21.971210+00:00 |
| **Total de trechos citados** | 104 |
| **Tempo de processamento** | 0:00:27:18 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 26.3 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 133 marcadores, 34 distintos |
| Referências listadas | 34 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 87 | 83.7% |
| **UNSUPPORTED** | 15 | 14.4% |
| **CONTRADICTED** | 1 | 1.0% |
| **SKIPPED** | 1 | 1.0% |
| **TOTAL** | 104 | 100.0% |

Sobre os 103 trechos citados auditados: SUPPORTED 84,46%, UNSUPPORTED 14,56%, CONTRADICTED 0,97%.

> **31 dos 87 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 31 estão **contados dentro** dos 87 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`22` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `7` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `3` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 6, full_doc_scan = 1.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#35` An interprovincial trade moved enslaved people from the declining sugar Northeast and from the South to the coffee Sout… | [22] | [18] [16] | — |
| `#65` The Chamber approved it on 10 May by 83 votes to 9 as about 5,000 demonstrators gathered outside. | [26] | [3] [2] [8] [24] [9] [7] [20] [6] | — |
| `#95` In April 2012 the Supreme Federal Court unanimously upheld racial quotas at the University of Brasília, and Justice Lui… | [14] | [16] [3] [20] [7] [11] [23] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1425539 |
| **Média de tokens por requisição** | 13840.2 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/34 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[5]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/marinha-britanica-forcou-brasil-a-acabar-com-trafico-negreiro) | downloaded | 12 | 8 | 4 | 0 | 0 |
| [[2]](https://www.congressoemfoco.com.br/noticia/118759/congresso-viveu-65-anos-de-recuos-e-leis-graduais-ate-a-lei-aurea) | downloaded | 9 | 6 | 3 | 0 | 0 |
| [[8]](https://vermelho.org.br/2016/05/13/a-abolicao-uma-revolucao-pela-metade/) | downloaded | 9 | 4 | 4 | 1 | 0 |
| [[9]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/cem-anos-da-morte-da-princesa-isabel-a-regente-que-reinou-alem-do-machismo) | downloaded | 8 | 4 | 4 | 0 | 0 |
| [[6]](https://www12.senado.leg.br/noticias/materias/2015/08/31/lei-dos-sexagenarios-completa-130-anos) | downloaded | 7 | 5 | 2 | 0 | 0 |
| [[7]](https://en.wikipedia.org/wiki/Abolitionism_in_Brazil) | downloaded | 7 | 1 | 6 | 0 | 0 |
| [[11]](https://library.brown.edu/create/fivecenturiesofchange/?p=78) | downloaded | 6 | 3 | 2 | 1 | 0 |
| [[20]](https://warwick.ac.uk/fac/arts/history/students/modules/hi3s9/programme/abolition/graden_abolition_of_slave_trade_historia_unisinos.pdf) | downloaded | 6 | 3 | 3 | 0 | 0 |
| [[3]](https://en.wikipedia.org/wiki/Lei_%C3%81urea) | downloaded | 5 | 1 | 4 | 0 | 0 |
| [[4]](https://rioonwatch.org/?p=21879) | downloaded | 5 | 2 | 3 | 0 | 0 |
| [[18]](https://repositorio.ipea.gov.br/bitstream/11058/14231/1/_A_economia_da_escravidao_nas_fazendas_%20de_cafe.pdf) | downloaded | 5 | 3 | 2 | 0 | 0 |
| [[10]](https://www.gov.br/casaruibarbosa/pt-br/centrais-de-conteudo/minisites/memoriaescravidao/copy_of_pdfs/04-roteiro-de-atividades-pedagogicas-as-indenizacoes.pdf) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[21]](https://en.wikipedia.org/wiki/Burning_of_slavery_records_in_Brazil) | downloaded | 4 | 1 | 2 | 1 | 0 |
| [[25]](https://mais.opovo.com.br/reportagens-especiais/dragoes-do-ceara/2021/08/28/140-anos-da-greve-contra-a-escravidao-a-jangada-perdida-do-dragao-do-mar.html) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[27]](https://www.britannica.com/place/Brazil/The-collapse-of-the-empire) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[14]](https://www.jb.com.br/pais/noticias/2012/04/26/amp/por-unanimidade-stf-declara-constitucional-cotas-para-negros-nas-universidades.html) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[16]](https://en.wikipedia.org/wiki/Slavery_in_Brazil) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[22]](https://www.redalyc.org/pdf/770/77002404.pdf) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[23]](https://library.brown.edu/create/fivecenturiesofchange/chapters/chapter-3/slavery-and-aboliton/) | downloaded | 3 | 2 | 1 | 0 | 0 |
| [[1]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[12]](https://agenciagov.ebc.com.br/noticias/202312/censo-2022-mostra-que-45-da-populacao-brasileira-e-pardos-e-43-5-branca) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[13]](https://www.cut.org.br/noticias/hora-trabalhada-de-pessoa-branca-vale-67-7-mais-que-a-de-negros-ff0e/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[15]](https://legacy.slavevoyages.org/assessment/estimates) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[17]](https://www.britannica.com/place/Brazil/Agriculture-and-prospecting) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[19]](https://encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/male-rebellion) | downloaded | 2 | 1 | 0 | 1 | 0 |
| [[24]](https://www.congressoemfoco.com.br/noticia/118766/quem-tentou-barrar-a-abolicao-da-escravatura-no-parlamento) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[26]](https://www.em.com.br/app/noticia/politica/2013/05/11/interna_politica,386059/abolicao-da-escravatura-completa-125-anos-e-em-reconta-a-historia.shtml) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[29]](https://revistas.usp.br/revhistoria/article/download/131955/128100/251977) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[30]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/na-primeira-eleicao-presidencial-ha-120-anos-brasil-teve-eleitor-de-menos-e-candidato-demais) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[34]](https://www12.senado.leg.br/noticias/materias/2023/12/22/dia-da-consciencia-negra-se-torna-feriado-nacional) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[28]](https://en.wikipedia.org/wiki/Italo_Brazilian) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[31]](https://ambulatinbr.substack.com/p/when-capoeira-was-a-crime) | dead | 1 | 0 | 0 | 0 | 1 |
| [[32]](https://www.brasildefato.com.br/2026/05/26/homicidios-de-pessoas-negras-representam-77-do-total-de-assassinatos-no-brasil-aponta-atlas-da-violencia/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www12.senado.leg.br/noticias/materias/2023/11/14/sancionada-ampliacao-da-lei-de-cotas) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[5]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/marinha-britanica-forcou-brasil-a-acabar-com-trafico-negreiro) | #22–25, #30–33 | #3, #26, #29, #98 | — | `#22` o país, que havia aprovado uma lei em 1807 abolindo o tráfico em suas colônias, passou a arrancar de outras nações acordos de proibição desse tipo de comércio… |
| [[2]](https://www.congressoemfoco.com.br/noticia/118759/congresso-viveu-65-anos-de-recuos-e-leis-graduais-ate-a-lei-aurea) | #1, #41, #43, #46, #64, #99 | #44, #82, #98 | — | `#1` Não previu transição, indenização aos proprietários nem política de integração para os libertos. |
| [[8]](https://vermelho.org.br/2016/05/13/a-abolicao-uma-revolucao-pela-metade/) | #54, #59, #66, #69 | #4, #58, #60, #71 | #73 | `#54` Joaquim Nabuco, o mais destacado líder essa corrente dizia que era preciso trazer a abolição das ruas para o Parlamento. |
| [[9]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/cem-anos-da-morte-da-princesa-isabel-a-regente-que-reinou-alem-do-machismo) | #42, #63, #67, #74 | #4–5, #60, #72 | — | `#42` Apenas dois dias após ter sancionado a Lei do Ventre Livre — que fixou a data de 28 de setembro de 1871 como o marco a partir do qual as mulheres escravizadas… |
| [[6]](https://www12.senado.leg.br/noticias/materias/2015/08/31/lei-dos-sexagenarios-completa-130-anos) | #47–51 | #3, #98 | — | `#47` O projeto número 48 foi apresentado à Câmara dos Deputados em 15 de julho de 1884 pelo deputado Rodolfo Dantas, do Partido Liberal. A proposta dispunha sobre a… |
| [[7]](https://en.wikipedia.org/wiki/Abolitionism_in_Brazil) | #53 | #3, #45, #55, #57–58, #101 | — | `#53` In 1880, important politicians, such as Joaquim Nabuco and José do Patrocínio, created, in Rio de Janeiro, the Brazilian Society Against Slavery [...] With the… |
| [[11]](https://library.brown.edu/create/fivecenturiesofchange/?p=78) | #6, #62, #83 | #88, #100 | #86 (s/ aval.) | `#6` the Province of São Paulo used state funds to support the society's efforts to recruit European immigrants to Brazil to work as agricultural laborers. By 1895,… |
| [[20]](https://warwick.ac.uk/fac/arts/history/students/modules/hi3s9/programme/abolition/graden_abolition_of_slave_trade_historia_unisinos.pdf) | #21, #23, #34 | #26, #28–29 | — | `#21` Memory of the revolt combined with various manifestations of slave resistance in its wake played a role in shaping imperial politics and decisions from 1848 to… |
| [[3]](https://en.wikipedia.org/wiki/Lei_%C3%81urea) | #39 | #2, #10, #52, #82 | — | `#39` Pedro II was also influenced by the American Civil War, writing in 1864 that the future of slavery in Brazil must be questioned in fear of internal conflict. .… |
| [[4]](https://rioonwatch.org/?p=21879) | #9, #12 | #2, #11, #28 | — | `#9` In the study, 35,000 voyages were catalogued [...] According to the research, close to 4.8 million slaves arrived in coastal Brazil. [...] Maurício Goulart, wh… |
| [[18]](https://repositorio.ipea.gov.br/bitstream/11058/14231/1/_A_economia_da_escravidao_nas_fazendas_%20de_cafe.pdf) | #15–16, #38 | #73, #101 | — | `#15` A Zona Oeste do Vale do Medio Paraíba representa a região onde existiram as primeiras fazendas de café nas décadas de 20 e 30 [...] A totalidade do processo ab… |
| [[10]](https://www.gov.br/casaruibarbosa/pt-br/centrais-de-conteudo/minisites/memoriaescravidao/copy_of_pdfs/04-roteiro-de-atividades-pedagogicas-as-indenizacoes.pdf) | #75–76 | #5, #79 | — | `#75` O documento aborda o apoio repentino dos ex-senhores de escravizados à causa republicana (movimento conhecido como os "republicanos de 14 de maio") e a exigênc… |
| [[21]](https://en.wikipedia.org/wiki/Burning_of_slavery_records_in_Brazil) | #81 | #27, #103 | #80 ⚡ | `#81` It is believed that Barbosa issued the document with the intention that former slave owners would not be able to seek compensation after the abolition of slave… |
| [[25]](https://mais.opovo.com.br/reportagens-especiais/dragoes-do-ceara/2021/08/28/140-anos-da-greve-contra-a-escravidao-a-jangada-perdida-do-dragao-do-mar.html) | #56 | #55, #57, #101 | — | `#56` Em 1881, duas greves de jangadeiros cearenses impulsionaram o movimento pela libertação de escravizados no Brasil. Em janeiro, a revolta puxada por brancos aba… |
| [[27]](https://www.britannica.com/place/Brazil/The-collapse-of-the-empire) | #77–79, #84 | — | — | `#77` Many historians have ascribed the fall of the monarchy to a restive military, a brooding landed aristocracy, and a resentful clergy. Indeed, those three powerf… |
| [[14]](https://www.jb.com.br/pais/noticias/2012/04/26/amp/por-unanimidade-stf-declara-constitucional-cotas-para-negros-nas-universidades.html) | #7 | #95, #102 | — | `#7` A hora trabalhada de uma pessoa branca vale 67,7% mais que a de trabalhadores pretos e pardos. |
| [[16]](https://en.wikipedia.org/wiki/Slavery_in_Brazil) | #17–18 | #10 | — | `#17` In 1872, the population of Brazil was 10 million, and 15% were slaves. As a result of widespread manumission (easier in Brazil than in North America[50]), by t… |
| [[22]](https://www.redalyc.org/pdf/770/77002404.pdf) | #36–37 | #35 | — | `#36` O tráfico interprovincial, somente no auge, entre 1873 e 1881, transportou 90 mil negros para o sudeste, através dos portos de Santos e, principalmente, do Rio… |
| [[23]](https://library.brown.edu/create/fivecenturiesofchange/chapters/chapter-3/slavery-and-aboliton/) | #40, #61 | #101 | — | `#40` Since their enlistment in the Army, many slaves had proven their worth on the battlefield, a realization that caused officers to be increasingly skeptical of t… |
| [[1]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html) | #0, #70 | — | — | `#0` A Princeza Imperial Regente, em nome de Sua Majestade o Imperador, o Senhor D. Pedro II, Faz saber a todos os subditos do Imperio que a Assembléa Geral Decreto… |
| [[12]](https://agenciagov.ebc.com.br/noticias/202312/censo-2022-mostra-que-45-da-populacao-brasileira-e-pardos-e-43-5-branca) | #7, #92 | — | — | `#92` Em 2022, cerca de 92,1 milhões de pessoas se declararam pardas, o equivalente a 45,3% da população do país. Desde 1991, esse contingente não superava a populaç… |
| [[13]](https://www.cut.org.br/noticias/hora-trabalhada-de-pessoa-branca-vale-67-7-mais-que-a-de-negros-ff0e/) | #7, #93 | — | — | `#7` Em 2022, cerca de 92,1 milhões de pessoas se declararam pardas, o equivalente a 45,3% da população do país. Desde 1991, esse contingente não superava a populaç… |
| [[15]](https://legacy.slavevoyages.org/assessment/estimates) | #8 | #11 | — | `#8` Trans-Atlantic Slave Trade - Estimates ... Full extent of coverage by estimates is 1501 - 1866. ... Totals ... 12,521,337 |
| [[17]](https://www.britannica.com/place/Brazil/Agriculture-and-prospecting) | #13–14 | — | — | `#13` The sugar industry, confined primarily to the Northeast, was the principal source of Brazilian wealth from the 16th to the 18th century [...] Sugar production… |
| [[19]](https://encyclopedia.com/history/encyclopedias-almanacs-transcripts-and-maps/male-rebellion) | #20 | — | #19 (s/ aval.) | `#20` During the entire revolt, over seventy Africans lost their lives. ... Floggings ranged from fifty to twelve hundred lashes. ... deportation to the African coas… |
| [[24]](https://www.congressoemfoco.com.br/noticia/118766/quem-tentou-barrar-a-abolicao-da-escravatura-no-parlamento) | #44, #68 | — | — | `#44` O Visconde de Itaboraí, também contrário ao Ventre Livre, advertiu que a liberdade dos filhos de mulheres escravizadas poderia estimular ressentimento nas senz… |
| [[26]](https://www.em.com.br/app/noticia/politica/2013/05/11/interna_politica,386059/abolicao-da-escravatura-completa-125-anos-e-em-reconta-a-historia.shtml) | — | #65 | #72 | `#65` cerca de 5 mil manifestantes que acompanharam a votação do projeto de lei que extingue a escravidão no país |
| [[29]](https://revistas.usp.br/revhistoria/article/download/131955/128100/251977) | #87, #91 | — | — | `#87` a imigração européia trouxe ao "desalojar" o elemento negro como força de trabalho em São Paulo ao contrário dó que ocorreu por exemplo no Rio de Janeiro e Sal… |
| [[30]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/na-primeira-eleicao-presidencial-ha-120-anos-brasil-teve-eleitor-de-menos-e-candidato-demais) | #89 | #100 | — | `#89` O direito era negado a mulheres, analfabetos, mendigos, soldados rasos e religiosos sujeitos a voto de obediência. O eleitor devia ter ao menos 21 anos. Eram r… |
| [[34]](https://www12.senado.leg.br/noticias/materias/2023/12/22/dia-da-consciencia-negra-se-torna-feriado-nacional) | #97 | #102 | — | `#97` É o que determina a Lei 14.759, sancionada no dia anterior pelo presidente Luiz Inácio Lula da Silva. A data remete ao dia da morte de Zumbi, o líder do Quilom… |
| [[28]](https://en.wikipedia.org/wiki/Italo_Brazilian) | #85 | — | — | `#85` the boom of Italian immigration in Brazil happened between 1880 and 1900, when almost one million Italians arrived. |
| [[32]](https://www.brasildefato.com.br/2026/05/26/homicidios-de-pessoas-negras-representam-77-do-total-de-assassinatos-no-brasil-aponta-atlas-da-violencia/) | #94 | — | — | `#94` o Brasil registrou 32.820 homicídios de pessoas negras em 2024, o que corresponde a 77% do total de homicídios registrados naquele ano. |
| [[33]](https://www12.senado.leg.br/noticias/materias/2023/11/14/sancionada-ampliacao-da-lei-de-cotas) | #96 | — | — | `#96` A Lei de Cotas (Lei 12.711, de 2012) reserva no mínimo 50% das vagas em universidades e institutos federais para estudantes que cursaram todo o ensino médio em… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://ambulatinbr.substack.com/p/when-capoeira-was-a-crime — Referencia nao encontrada (404): https://ambulatinbr.substack.com/p/when-capoeira-was-a-crime

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-0`** [1]
  - Trecho: On 13 May 1888, Princess Isabel, acting as regent, sanctioned a two-article law that declared slavery in Brazil extinct from that date.
  - Justificativa: A evidência confirma todos os elementos essenciais da afirmação: a data (13 de maio de 1888), a Princeza Imperial Regente sancionando a lei, a lei com dois artigos, e a declaração de extinção da escravidão no Brasil des…
  - Suporte veio de: [1]
  - Evidência: “LEI n. 3.353, DE 13 DE MAIO DE 1888”
  - Não coberto pela evidência: O nome próprio 'Isabel' não aparece explicitamente na evidência, que se refere apenas a 'Princeza Imperial Regente'.
- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-1`** [2]
  - Trecho: The Lei Áurea, or Golden Law, offered no transition period, no compensation for owners, and no policy to integrate the people it freed.
  - Justificativa: A evidência afirma explicitamente que a Lei Áurea 'Não previu transição, indenização aos proprietários nem política de integração para os libertos', o que corresponde diretamente aos três elementos da afirmação: ausênci…
  - Suporte veio de: [2]
  - Evidência: “Não previu transição, indenização aos proprietários nem política de integração para os libertos.”
- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-2`** [3] [4]
  - Trecho: Brazil was the last country in the Americas to abolish slavery, and it had received more enslaved Africans than any other destination, close to 4.8 million by recent estimates built on the SlaveVoyages database.
  - Justificativa: A evidência sustenta explicitamente que o Brasil foi o último país das Américas a abolir a escravidão e que cerca de 4,8 milhões de escravos chegaram ao Brasil, com base em pesquisa da Emory University hospedada em slav…
  - Suporte veio de: [3] [4]
  - Evidência: “Brazil was the last country in the Americas to abolish slavery.”
  - Não coberto pela evidência: A comparação explícita de que o Brasil recebeu 'mais africanos escravizados do que qualquer outro destino' não é declarada literalmente; é inferida do dado de 40% do total, mas a evidência não compara individualmente com outros destinos.; O número exato de 4,8 milhões refere-se a 'costal Brazil' (Brasil costeiro), não necessariamente a todo o Brasil, embora na prática seja equivalente.
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [3] | parcial | Brazil was the last country in the Americas to abolish slavery. |
    | [4] | parcial | According to the research, close to 4.8 million slaves arrived in coastal Brazil. ... This conclusion is based on a rig… |

### UNSUPPORTED

- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-3`** [5] [6] [7]
  - Trecho: British naval pressure and fear of revolt ended the Atlantic trade in 1850, gradual laws in 1871 and 1885 freed newborns and the elderly on terms friendly to planters, and in the 1880s abolitionists, port workers, and f…
  - Justificativa: A evidência sustenta a maior parte da afirmação: a pressão naval britânica e o medo de revolta levaram ao fim do tráfico em 1850; as leis de 1871 (Ventre Livre) e 1885 (Sexagenários) liberaram recém-nascidos e idosos em…
  - Suporte veio de: [5] [7]
  - Evidência: “a Grã-Bretanha, cansada de esperar que o tratado de 1826 fosse cumprido, ordenou em 1845 que a Marinha real patrulhasse o Atlântico e confiscasse toda embarcação suspeita de transportar carga humana da África para o Bra…”
  - Não coberto pela evidência: port workers (trabalhadores portuários) como agentes que tornaram a escravidão inaplicável nos anos 1880 — não há menção a trabalhadores portuários na evidência
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [5] | parcial | Marinha britânica forçou Brasil a acabar com tráfico negreiro |
    | [6] | parcial | Lei do Ventre Livre (1871), que concedeu liberdade aos filhos de escravos nascidos a partir de sua promulgação |
    | [7] | parcial | British warships chased suspicious vessels into Brazilian waters and threatened to blockade ports involved in the slave… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-10`** [16] [3]
  - Trecho: Secondary compilations range from about 4 million to 5.5 million, and the commonly cited share of roughly 40 percent of Africans brought to the New World fits that band.
  - Justificativa: A evidência fornece números individuais (4 milhões e 5,5 milhões para o Brasil, e 40% como participação do Brasil), mas não caracteriza esses números como 'compilações secundárias' nem faz a análise de que 40% 'se encai…
  - Suporte veio de: [3] [16]
  - Evidência: “by then it had imported an estimated 4,000,000 slaves from Africa. This was 40% of all slaves shipped to the Americas.”
  - Não coberto pela evidência: Caracterização dos números como 'compilações secundárias'; A afirmação de que 40% 'se encaixa nessa faixa' (band) de 4 a 5,5 milhões; O conceito de 'band' ou faixa formada por essas estimativas
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [16] | parcial | by then it had imported an estimated 4,000,000 slaves from Africa. This was 40% of all slaves shipped to the Americas. |
    | [3] | parcial | Of the 10 million African slaves which were forcibly brought to the New World, 40 percent were brought to Brazil |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-27`** [21]
  - Trecho: One secondary account gives a much lower figure of about 300,000, which the stronger scholarship does not support.
  - Justificativa: A evidência menciona a cifra de 300.000 africanos escravizados que entraram no Brasil após 1831 por tráfico ilegal, mas não a caracteriza como uma 'conta secundária' nem afirma que 'estudos mais sólidos não a sustentam'…
  - Suporte veio de: [21]
  - Evidência: “It is estimated that after 1831 around 300,000 enslaved Africans entered Brazil through illegal trafficking.”
  - Não coberto pela evidência: Caracterização da cifra de 300.000 como proveniente de uma 'conta secundária'; Afirmação de que 'estudos mais sólidos' (stronger scholarship) não sustentam essa cifra; Existência de uma figura alternativa mais alta implícita na comparação
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-80`** [21]
  - Trecho: On 14 December 1890, Rui Barbosa ordered the destruction of slave registration books, customs records, and tax records, and the burning reportedly took place on 13 May 1891, the law's third anniversary.
  - Justificativa: A evidência confirma a data da ordem (14 de dezembro de 1890), os tipos de registros destruídos (livros de registro, registros alfandegários e fiscais) e a data da queima (13 de maio de 1891). No entanto, a afirmacao di…
  - Suporte veio de: [21]
  - Evidência: “On 14 December 1890, a document signed by Ruy Barbosa, then serving as Minister of Finance of the newly proclaimed First Brazilian Republic, ordered the burning of all records on the purchase and sale of slaves in Brazi…”
  - Não coberto pela evidência: A afirmacao diz 'third anniversary' (terceiro aniversário), mas a evidência diz 'second anniversary' (segundo aniversário) — conflito direto.

---

## 10. Trechos Citados Não Auditados

Motivos: 1 citam referência não baixada/inacessível.

- `escravidao_brasil_fa0dd5de0e8e_20261115T021304Z-90` — Referencia(s) citada(s) ['919d68b52a3d8f2b'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).