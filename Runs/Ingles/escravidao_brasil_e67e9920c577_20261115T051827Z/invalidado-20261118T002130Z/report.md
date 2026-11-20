# Relatório de Auditoria — ChatGPT (escravidao_brasil_e67e9920c577_20261115T051827Z)

**Arquivo auditado:** `answers/Ingles/ChatGPT/Consolidado/escravidao_brasil.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | escravidao_brasil_e67e9920c577_20261115T051827Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-15T05:47:40.363683+00:00 |
| **Total de trechos citados** | 111 |
| **Tempo de processamento** | 0:00:29:13 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 32.1 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 111 marcadores, 34 distintos |
| Referências listadas | 34 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 39 | 35.1% |
| **UNSUPPORTED** | 37 | 33.3% |
| **CONTRADICTED** | 1 | 0.9% |
| **SKIPPED** | 34 | 30.6% |
| **TOTAL** | 111 | 100.0% |

Sobre os 77 trechos citados auditados: SUPPORTED 50,64%, UNSUPPORTED 48,05%, CONTRADICTED 1,29%.

> **18 dos 39 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 18 estão **contados dentro** dos 39 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`39` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `15` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `2` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `18` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#8` The result was that even as Atlantic slavery was disappearing elsewhere in the Americas, Brazilian economic modernizati… | [1] | [6] [2] [30] [23] | — |
| `#9` Brazilian slavery nevertheless coexisted with a substantial population of free and freed people of African descent. | [1] | [6] [2] | — |
| `#18` Luiz Gama, born in Bahia in 1830 and illegally enslaved as a child, obtained his own freedom and became a self-taught l… | [12] | [13] [17] [6] | — |
| `#20` Gama’s career illustrates how abolitionism operated not only through parliamentary debate but also through litigation c… | [12] | [6] [17] [34] [29] [23] | — |
| `#23` In 1883, Patrocínio and the Black engineer and intellectual André Rebouças were associated with the Manifesto of the Co… | [15] | [14] [2] [34] [29] [23] [18] [6] [16] | — |
| `#32` Britain abolished its own slave trade in 1807 and increasingly used diplomatic and naval pressure to suppress the Atlan… | [19] | [2] [18] [6] [30] [16] | — |
| `#34` The 1831 statute was systematically violated, however, and hundreds of thousands of Africans were illegally imported in… | [18] | [6] [30] [2] | — |
| `#36` The law nevertheless acquired renewed importance later because Black litigants and abolitionist lawyers could argue tha… | [12] | [6] [30] [18] [29] | — |
| `#38` In 1850, the Brazilian Empire finally passed the Eusébio de Queirós Law, which strengthened enforcement against the imp… | [21] | [2] [18] [30] [6] [34] | — |
| `#53` Princess Isabel’s role should therefore be understood precisely rather than mythologized. | [25] | [23] [34] [28] [2] | — |
| `#61` Approximately 700,000 people were directly liberated from legal enslavement, although the exact number varies according… | [28] | [34] [6] [29] [16] | — |
| `#72` The transition from slave to free labor therefore did not eliminate coercion; rather, some coercive practices were reco… | [6] | [30] [23] | — |
| `#89` Political exclusion was reinforced by the electoral rules of the late empire and early republic. | [6] | [32] [29] [31] [30] [23] [2] | — |
| `#92` The most enduring paradox of Brazilian abolition is that an extraordinarily radical change in legal status occurred wit… | [1] | [16] [6] [2] [34] [29] | — |
| `#93` Former slaves became legally free citizens, but the economic and social structures produced by centuries of slavery con… | [18] | [6] [30] [2] | — |
| `#94` Historians therefore distinguish between emancipation as the termination of legal ownership and freedom as a broader co… | [1] | [6] [30] [29] [34] [23] | — |
| `#100` The history of post-abolition Brazil is therefore simultaneously a history of persistent structural inequality and of s… | [1] | [34] [23] [6] [29] [2] [28] | — |
| `#103` This reinterpretation does not require denying Isabel’s support for abolition or her constitutional act of sanctioning… | [25] | [34] [23] [6] [16] [28] [29] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 1207237 |
| **Média de tokens por requisição** | 15678.4 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/34 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 5.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[9]](https://academic.oup.com/edited-volume/61800/chapter-abstract/546615849) | blocked | 16 | 0 | 0 | 0 | 16 |
| [[6]](https://www.cambridge.org/core/journals/international-review-of-social-history/article/precariousness-of-freedom-in-a-slave-society-brazil-in-the-nineteenth-century/8496E56A9C311D9B941F94E22F48F15D) | downloaded | 10 | 5 | 4 | 1 | 0 |
| [[18]](https://www.gov.br/arquivonacional/pt-br/sites_eventos/sites-tematicos-1/brasil-oitocentista/temas-oitocentistas/legislacao-abolicionista-no-imperio/) | downloaded | 10 | 7 | 3 | 0 | 0 |
| [[1]](https://www.cambridge.org/core/books/boundaries-of-freedom/slavery-and-freedom-in-nineteenthcentury-brazil/EC17B17AE1B57465E31691EEF5C6558A) | downloaded | 9 | 2 | 4 | 3 | 0 |
| [[5]](https://academic.oup.com/edited-volume/61800/chapter-abstract/546391139) | blocked | 6 | 0 | 0 | 0 | 6 |
| [[16]](https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/golden-law) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[23]](https://www.scielo.br/j/rbh/a/BcBZ8KgTsqPZZr7vVmGDc6t/?lang=pt) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[25]](https://cpdoc.fgv.br/sites/default/files/movimento_negro/raca_racismo/Notas_LeiAurea.pdf) | downloaded | 4 | 1 | 0 | 3 | 0 |
| [[29]](https://www.scielo.br/j/rh/a/YJd7BKnhn54kLNRym8VFSTJ/?lang=pt) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[30]](https://www.scielo.br/j/alm/a/6jgKHcz533MNMn5VcPPGR5M/?lang=pt) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[31]](https://cpdoc.fgv.br/artigos/proclamacao-republica) | downloaded | 4 | 3 | 0 | 1 | 0 |
| [[4]](https://guides.loc.gov/brazil-us-relations/slavery-and-abolition) | blocked | 3 | 0 | 0 | 0 | 3 |
| [[12]](https://bndigital.bn.gov.br/dossies/literatura-matriz-afro-brasileira/autores-na-biblioteca-nacional-digital/luis-gama/) | downloaded | 3 | 0 | 0 | 3 | 0 |
| [[27]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html) | inaccessible | 3 | 0 | 0 | 0 | 3 |
| [[32]](https://atlas.fgv.br/verbetes/proclamacao-da-republica) | downloaded | 3 | 0 | 3 | 0 | 0 |
| [[14]](https://www.gov.br/igualdaderacial/pt-br/assuntos/noticias/nesta-data-em-1853-nasceu-jose-carlos-do-patrocinio) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[22]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-2040-28-setembro-1871-538828-publicacaooriginal-35591-pl.html) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[24]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3270-28-setembro-1885-543466-publicacaooriginal-53780-pl.html) | inaccessible | 2 | 0 | 0 | 0 | 2 |
| [[26]](https://www2.senado.leg.br/bdsf/bitstream/handle/id/190819/encarteabolicao.pdf?isAllowed=y&sequence=7) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[34]](https://repositorio.ipea.gov.br/bitstream/11058/12387/1/NT_110_Disoc_a_luta.pdf) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[2]](https://whc.unesco.org/document/159617) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[3]](https://bndigital.bn.gov.br/dossies/rede-da-memoria-virtual-brasileira/escravidao-jose-roberto-pinto-de-goes/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[7]](https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/13162-asi-ibge-lanca-colecao-inedita-da-historia-das-estatisticas-brasileiras) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[8]](https://rbg.ibge.gov.br/index.php/rbg/article/download/2620/1990) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[10]](https://www.loc.gov/item/hlas-bi2007000899/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[11]](https://bndigital.bn.gov.br/dossies/trafico-de-escravos-no-brasil/escravidao-no-brasil/movimentos-abolicionistas-e-alforrias/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[13]](https://www.gov.br/mdh/pt-br/sdh/noticias/2018/janeiro/luis-gama-e-reconhecido-por-lei-como-patrono-da-abolicao-da-escravatura-do-brasil/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://bdlb.bn.gov.br/acervo/handle/20.500.12156.3/420758) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[17]](https://pesquisaescolar.fundaj.gov.br/pt-br/artigo/luiz-gama/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://bndigital.bn.gov.br/dossies/trafico-de-escravos-no-brasil/acordos-internacionais-e-legislacao-sobre-escravidao/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[20]](https://www2.camara.leg.br/legin/fed/lei_sn/1824-1899/lei-37659-7-novembro-1831-564776-publicacaooriginal-88704-pl.html) | inaccessible | 1 | 0 | 0 | 0 | 1 |
| [[21]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-581-4-setembro-1850-559820-publicacaooriginal-82230-pl.html) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[28]](https://www12.senado.leg.br/radio/1/noticia/2018/05/11/senado-promove-exibicao-das-leis-que-culminaram-com-sancao-da-lei-aurea) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[33]](https://guides.loc.gov/brazil-us-relations/empire-of-brazil) | blocked | 1 | 0 | 0 | 0 | 1 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[6]](https://www.cambridge.org/core/journals/international-review-of-social-history/article/precariousness-of-freedom-in-a-slave-society-brazil-in-the-nineteenth-century/8496E56A9C311D9B941F94E22F48F15D) | #10, #79, #90, #95, #97 | #72, #88–89, #91 | #99 ⚡ | `#10` significant rates of manumission resulted in a high percentage of free and freed people of color in the population of the country throughout the nineteenth cen… |
| [[18]](https://www.gov.br/arquivonacional/pt-br/sites_eventos/sites-tematicos-1/brasil-oitocentista/temas-oitocentistas/legislacao-abolicionista-no-imperio/) | #31, #35, #37, #59–60, #64–65 | #34, #93, #109 | — | `#31` O processo de abolição da escravidão no Brasil foi lento e gradual, tendo início ainda no período joanino, quando Portugal e Inglaterra assinaram os primeiros… |
| [[1]](https://www.cambridge.org/core/books/boundaries-of-freedom/slavery-and-freedom-in-nineteenthcentury-brazil/EC17B17AE1B57465E31691EEF5C6558A) | #0, #2 | #8, #92, #100, #110 | #9, #26, #94 | `#0` May 13, 1888, the day that ended legalized slavery in his country. Brazil was the last nation in the Western hemisphere to abolish slavery; it had also been th… |
| [[16]](https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/golden-law) | #24 | #25, #51, #66 | — | `#24` Contemporary abolitionists—particularly Joaquim Nabuco and André Rebouças—were outspoken critics of what they regarded as only a partial abolition that had fai… |
| [[23]](https://www.scielo.br/j/rbh/a/BcBZ8KgTsqPZZr7vVmGDc6t/?lang=pt) | #45–46, #70–71 | — | — | `#45` a importância da garantia do direito dos escravizados de formar um pecúlio, e de obter a alforria caso tivessem os meios para indenizar o seu valor (Chalhoub,… |
| [[25]](https://cpdoc.fgv.br/sites/default/files/movimento_negro/raca_racismo/Notas_LeiAurea.pdf) | #54 | — | #53, #63, #103 | `#54` A Princesa Imperial Regente, em nome de Sua Majestade o Imperador, o Senhor D. Pedro II, faz saber a todos os súditos do Império que a Assembleia Geral decreto… |
| [[29]](https://www.scielo.br/j/rh/a/YJd7BKnhn54kLNRym8VFSTJ/?lang=pt) | #67, #69, #98 | #68 | — | `#67` A população negra não ficou alheia ao fundo de emancipação nem às disputas que o envolvia. Ainda sob a Monarquia, em 26 de abril de 1889, pouco antes da Lei de… |
| [[30]](https://www.scielo.br/j/alm/a/6jgKHcz533MNMn5VcPPGR5M/?lang=pt) | #76–78, #96 | — | — | `#77` o seu 'sentido racista', que valorizava o europeu branco em detrimento dos escravos, libertos e pobres livres no mercado de trabalho, bem como sua importância… |
| [[31]](https://cpdoc.fgv.br/artigos/proclamacao-republica) | #82, #84–85 | — | #80 | `#82` Não havia uma maioria republicana no país e nem mesmo unidade entre os militares. De fato, apenas uma pequena fração do Exército, e com características muito e… |
| [[12]](https://bndigital.bn.gov.br/dossies/literatura-matriz-afro-brasileira/autores-na-biblioteca-nacional-digital/luis-gama/) | — | — | #18, #20, #36 | — |
| [[32]](https://atlas.fgv.br/verbetes/proclamacao-da-republica) | — | #81, #86–87 | — | `#81` o partido era uma força política significativa apenas no Rio Grande do Sul e em São Paulo, onde contava com cerca de 25% do eleitorado e estava em crescimento,… |
| [[14]](https://www.gov.br/igualdaderacial/pt-br/assuntos/noticias/nesta-data-em-1853-nasceu-jose-carlos-do-patrocinio) | #21–22 | — | — | `#21` Filho de Justina Maria do Espírito Santo, mulher escravizada, e do padre João Carlos Monteiro, Patrocínio conheceu desde cedo as marcas de uma sociedade escrav… |
| [[22]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-2040-28-setembro-1871-538828-publicacaooriginal-35591-pl.html) | #44 | #43 | — | `#44` Art. 1º Os filhos de mulher escrava que nascerem no Imperio desde a data desta lei, serão considerados de condição livre. § 1º Os ditos filhos menores ficarão… |
| [[26]](https://www2.senado.leg.br/bdsf/bitstream/handle/id/190819/encarteabolicao.pdf?isAllowed=y&sequence=7) | — | — | #56–57 | — |
| [[34]](https://repositorio.ipea.gov.br/bitstream/11058/12387/1/NT_110_Disoc_a_luta.pdf) | #101–102 | — | — | `#101` O 13 de maio foi ressignificado pelo movimento negro como dia de denúncia e de enfrentamento à discriminação e ao racismo. [...] outras razões para a contestaç… |
| [[2]](https://whc.unesco.org/document/159617) | #1 | — | — | `#1` Over this period 4.864.373 enslaved Africans reached the Brazilian territory alive, brought in by slave ships. […] Thus, according to this database, Brazil rec… |
| [[3]](https://bndigital.bn.gov.br/dossies/rede-da-memoria-virtual-brasileira/escravidao-jose-roberto-pinto-de-goes/) | — | — | #3 | — |
| [[7]](https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/2013-agencia-de-noticias/releases/13162-asi-ibge-lanca-colecao-inedita-da-historia-das-estatisticas-brasileiras) | #11 | — | — | `#11` o Brasil, que no censo de 1872 tinha quase 10 milhões de pessoas sendo 8,4 livres e 1,5 escravos |
| [[11]](https://bndigital.bn.gov.br/dossies/trafico-de-escravos-no-brasil/escravidao-no-brasil/movimentos-abolicionistas-e-alforrias/) | — | — | #17 | — |
| [[13]](https://www.gov.br/mdh/pt-br/sdh/noticias/2018/janeiro/luis-gama-e-reconhecido-por-lei-como-patrono-da-abolicao-da-escravatura-do-brasil/) | #19 | — | — | `#19` advogado Luiz Gama como Patrono da Abolição da Escravidão no Brasil. Nascido em Salvador em 1830, Luiz Gama foi poeta, jornalista e rábula autodidata. Lutou pe… |
| [[15]](https://bdlb.bn.gov.br/acervo/handle/20.500.12156.3/420758) | — | #23 | — | `#23` Title: \| Manifesto da Confederação Abolicionista do Rio de Janeiro |
| [[17]](https://pesquisaescolar.fundaj.gov.br/pt-br/artigo/luiz-gama/) | #28 | — | — | `#28` Sob a inspiração e influência de Luiz Gama, seu amigo, o advogado e maçom Antonio Bento de Souza e Castro organizou os Caifazes, movimento radical de libertaçã… |
| [[19]](https://bndigital.bn.gov.br/dossies/trafico-de-escravos-no-brasil/acordos-internacionais-e-legislacao-sobre-escravidao/) | — | — | #32 | — |
| [[21]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-581-4-setembro-1850-559820-publicacaooriginal-82230-pl.html) | — | #38 | — | `#38` LEI Nº 581, DE 4 DE SETEMBRO DE 1850 |
| [[28]](https://www12.senado.leg.br/radio/1/noticia/2018/05/11/senado-promove-exibicao-das-leis-que-culminaram-com-sancao-da-lei-aurea) | — | #61 | — | `#61` libertou cerca de 700 mil pessoas do cativeiro |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://rbg.ibge.gov.br/index.php/rbg/article/download/2620/1990 — HTTP 500 em https://rbg.ibge.gov.br/index.php/rbg/article/download/2620/1990
- https://www2.camara.leg.br/legin/fed/lei_sn/1824-1899/lei-37659-7-novembro-1831-564776-publicacaooriginal-88704-pl.html — HTTP 504 em https://www2.camara.leg.br/legin/fed/lei_sn/1824-1899/lei-37659-7-novembro-1831-564776-publicacaooriginal-88704-pl.html
- https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3270-28-setembro-1885-543466-publicacaooriginal-53780-pl.html — HTTP 504 em https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3270-28-setembro-1885-543466-publicacaooriginal-53780-pl.html
- https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html — HTTP 504 em https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html

### Bloqueadas por barreira de acesso

- https://guides.loc.gov/brazil-us-relations/slavery-and-abolition — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://academic.oup.com/edited-volume/61800/chapter-abstract/546391139 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://academic.oup.com/edited-volume/61800/chapter-abstract/546615849 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://www.loc.gov/item/hlas-bi2007000899/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie
- https://guides.loc.gov/brazil-us-relations/empire-of-brazil — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-0`** [1]
  - Trecho: The abolition of slavery in Brazil on May 13, 1888, was the endpoint of a centuries-long system of coerced labor that had shaped the country’s economy, population, political institutions, and racial order since the earl…
  - Justificativa: A evidência sustenta explicitamente os elementos centrais da afirmação: a data de 13 de maio de 1888 como fim da escravidão legalizada, o caráter secular do sistema (mais de 350 anos, desde o início do século XVI), e qu…
  - Suporte veio de: [1]
  - Evidência: “May 13, 1888, the day that ended legalized slavery in his country”
  - Não coberto pela evidência: menção explícita a 'instituições políticas' como categoria específica moldada pela escravidão; menção explícita a 'ordem racial' como categoria específica moldada pela escravidão
- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-1`** [2]
  - Trecho: Brazil was the largest destination in the transatlantic slave trade, receiving roughly 4.9 million enslaved Africans who survived the Atlantic crossing, more than 45 percent of all Africans landed alive in the Americas.
  - Justificativa: A evidência sustenta todas as partes essenciais da afirmação: (1) Brazil recebeu mais cativos que qualquer outro país ('received most captives', 'more African slaves than anywhere else in the world'); (2) o número de 4.…
  - Suporte veio de: [2]
  - Evidência: “Over this period 4.864.373 enslaved Africans reached the Brazilian territory alive, brought in by slave ships.”
- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-2`** [1]
  - Trecho: The scale of this forced migration made slavery not merely a labor arrangement but one of the central institutions through which colonial and later imperial Brazilian society was constructed.
  - Justificativa: A evidência sustenta a afirmação de que a escala da migração forçada (quase cinco milhões de africanos escravizados) fez da escravidão um elemento central da sociedade brasileira. A evidência afirma que a escravidão 'sh…
  - Suporte veio de: [1]
  - Evidência: “Over those centuries, nearly five million enslaved Africans arrived in Brazil, more than 45 percent of the total number of persons forcibly brought to the Americas.”
  - Não coberto pela evidência: O termo 'colonial and later imperial' não aparece explicitamente na evidência, embora o período coberto (século XVI a 1888) abranja essas fases.; A expressão 'not merely a labor arrangement' não é literalmente afirmada na evidência, sendo uma inferência interpretativa.
### UNSUPPORTED

- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-3`** [3]
  - Trecho: Portuguese colonization initially relied on multiple forms of coerced Indigenous labor, but the expansion of sugar cultivation, demographic catastrophe among Indigenous peoples caused by warfare and disease, and Portugu…
  - Justificativa: A evidência trata de uma suspensão temporária do acesso aos acervos digitais da Fundação Biblioteca Nacional do Brasil devido a vulnerabilidades de segurança em PHP. Não há qualquer informação sobre colonização portugue…
  - Não coberto pela evidência: Portuguese colonization initially relied on multiple forms of coerced Indigenous labor; expansion of sugar cultivation; demographic catastrophe among Indigenous peoples caused by warfare and disease
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-8`** [1]
  - Trecho: The result was that even as Atlantic slavery was disappearing elsewhere in the Americas, Brazilian economic modernization remained deeply entangled with coerced Black labor.
  - Justificativa: A evidência afirma que o Brasil foi o último país do hemisfério ocidental a abolir a escravidão e que a escravidão moldou a história brasileira, o que tangencialmente se relaciona com a afirmação. Contudo, a afirmação e…
  - Suporte veio de: [1]
  - Não coberto pela evidência: Brazilian economic modernization remained deeply entangled with coerced Black labor; Atlantic slavery was disappearing elsewhere in the Americas
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [6] [2] [30] [23] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-9`** [1]
  - Trecho: Brazilian slavery nevertheless coexisted with a substantial population of free and freed people of African descent.
  - Justificativa: A evidência aborda a história da escravidão no Brasil, sua duração, escala e abolição, mas não menciona a existência de uma população de pessoas livres ou libertas de ascendência africana coexistindo com a escravidão. A…
  - Não coberto pela evidência: substantial population of free and freed people of African descent; coexistence of free/freed population with slavery
  - Verificação: UNSUPPORTED confirmado; afirmação corroborada por outra fonte não citada: [6] [2] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
### CONTRADICTED

- **Trecho citado `escravidao_brasil_e67e9920c577_20261115T051827Z-99`** [6]
  - Trecho: Black families built communities, formed religious and cultural institutions, created mutual-aid associations, entered new labor markets, used courts, moved across regions, and continued political traditions developed d…
  - Justificativa: A evidência contradiz explicitamente parte da afirmação: o texto afirma que pessoas libertas "were not allowed to create mutual aid societies based on racial or ethnic identities", enquanto o trecho a avaliar sustenta q…
  - Suporte veio de: [6]
  - Evidência: “were not allowed to create mutual aid societies based on racial or ethnic identities”
  - Não coberto pela evidência: built communities; formed religious and cultural institutions; entered new labor markets

---

## 10. Trechos Citados Não Auditados

Motivos: 27 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 7 citam referência não baixada/inacessível.

- `escravidao_brasil_e67e9920c577_20261115T051827Z-4` — Referencia(s) citada(s) ['2a7aff30ef7372be'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-5` — Referencia(s) citada(s) ['2a7aff30ef7372be'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-6` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-7` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-12` — Referencia(s) citada(s) ['9644c2b166700874'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-13` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-14` — Referencia(s) citada(s) ['2a7aff30ef7372be'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-15` — Referencia(s) citada(s) ['2c6101b3e57c889f'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-16` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-27` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-29` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-30` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-33` — Referencia(s) citada(s) ['f519f5c4b76450a8'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-39` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-40` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-41` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-42` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-47` — Referencia(s) citada(s) ['51a1e5d1bf229808'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-48` — Referencia(s) citada(s) ['51a1e5d1bf229808'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-49` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-50` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-52` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-55` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-58` — Referencia(s) citada(s) ['bfef16fbfb6faa86'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-62` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-73` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-74` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-75` — Referencia(s) citada(s) ['eaccdcfdbd37e579'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-83` — Referencia(s) citada(s) ['a3f8c5eb87ac18a2'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-104` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-105` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-106` — Referencia(s) citada(s) ['cccef09cf4140c13'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_e67e9920c577_20261115T051827Z-107` — Referencia(s) citada(s) ['bfef16fbfb6faa86'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_e67e9920c577_20261115T051827Z-108` — Referencia(s) citada(s) ['bfef16fbfb6faa86'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).