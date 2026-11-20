# Relatório de Auditoria — Gamini (escravidao_brasil_556b26a777e4_20261024T231607Z)

**Arquivo auditado:** `answers/Gemini/Consolidado/escravidao_brasil.docx`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | escravidao_brasil_556b26a777e4_20261024T231607Z |
| **Ferramenta** | Gamini |
| **Gerado em** | 2026-11-04T03:35:00.667130+00:00 |
| **Total de trechos citados** | 123 |
| **Tempo de processamento** | 10:04:18:53 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .docx · 30.2 KB |
| Título / Autor | Word Document / — (ausente) |
| Criação / Modificação | — / 2026-10-24 23:16:26+00:00 |
| Citações no corpo | 123 marcadores, 21 distintos |
| Referências listadas | 49 (28 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 40 | 32.5% |
| **UNSUPPORTED** | 73 | 59.3% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 10 | 8.1% |
| **TOTAL** | 123 | 100.0% |

Sobre os 113 trechos citados auditados: SUPPORTED 35,39%, UNSUPPORTED 64,60%, CONTRADICTED 0,00%.

> **22 dos 40 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 22 estão **contados dentro** dos 40 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`80` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `14` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `7` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `31` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 7.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#3` No decorrer do século XIX, a expansão do cultivo do café no Vale do Paraíba e, subsequentemente, no Oeste Paulista cons… | [2] | [17] [24] [49] [7] [11] [5] [3] [8] [1] [20] [33] [47] [4] [23] | — |
| `#5` Essa dependência criou uma contradição de proporções históricas: enquanto as nações ocidentais e as repúblicas hispano-… | [1] | [30] [7] [31] [10] [3] [17] [32] [49] [23] | — |
| `#9` A ação diplomática britânica, o recrudescimento da resistência dos próprios cativos e a emergência de correntes abolici… | [3] | [31] [30] [7] [35] [37] [24] | — |
| `#11` Em 7 de novembro de 1831, sob intensa pressão diplomática do Reino Unido para o reconhecimento da independência do Bras… | [3] | [11] [4] [12] [8] [32] [33] [2] [7] [35] [14] | — |
| `#12` Todavia, a ausência de mecanismos efetivos de fiscalização e o conluio entre autoridades e proprietários rurais tornara… | [3] | [11] [8] [12] [33] [38] [40] [41] [20] [2] [7] [17] [26] [49] [9] [28] | — |
| `#13` Entre 1830 e 1850, mais de meio milhão de africanos foram trazidos ilegalmente ao país para abastecer as fazendas de ca… | [2] | [12] [3] [11] [14] [4] [20] [8] [35] [37] [21] | — |
| `#17` Em 4 de setembro de 1850, foi sancionada a Lei nº 581, conhecida como Lei Eusébio de Queirós, apresentada pelo Ministro… | [11] | [4] [15] [8] [3] [14] [2] [26] [38] [29] [9] [7] [30] | — |
| `#23` Simultaneamente ao encerramento do tráfico transatlântico, o Estado imperial promulgou a Lei nº 601, de 18 de setembro… | [9] | [20] [11] [21] [17] [4] [14] [2] [3] | — |
| `#25` Antevendo a futura escassez de cativos, os grandes proprietários articularam uma legislação destinada a monopolizar o a… | [17] | [21] [20] [11] [41] [3] [8] [2] [29] [7] | — |
| `#31` A Lei de Terras de 1850 consolidou a estrutura fundiária latifundiária no Brasil, cujos impactos na concentração de ren… | [17] | [21] [20] [16] [9] [11] [41] [3] | — |
| `#33` Para atender às demandas do Vale do Paraíba e do Oeste Paulista, intensificou-se o tráfico interprovincial, um comércio… | [2] | [4] [20] [8] [11] [7] [31] [5] [1] | — |
| `#35` Do ponto de vista geopolítico, a concentração da população cativa no Sudeste desidratou o interesse econômico das elite… | [2] | [30] [41] [8] [31] [49] [47] [1] [7] [20] [23] [17] | — |
| `#37` O encerramento da Guerra do Paraguai (1864–1870) reacendeu o debate sobre a abolição. | [5] | [7] [49] [32] [23] [28] [39] [30] [31] | — |
| `#45` A obrigação da matrícula especial dos escravizados, a criação do fundo de emancipação e a legalização do direito ao pec… | [8] | [10] [29] [38] [31] [30] [24] [7] [2] | — |
| `#47` Em 28 de setembro de 1885, promulgou-se a Lei nº 3.270, denominada Lei dos Sexagenários ou Lei Saraiva-Cotegipe. | [27] | [29] [26] [8] [28] [25] [10] [24] [2] [31] | — |
| `#49` A Lei dos Sexagenários foi contestada pelos setores radicais do movimento abolicionista. | [10] | [28] [8] [25] [26] [24] [31] [37] [33] [35] [30] | — |
| `#53` Contudo, investigações históricas demonstraram que a derrocada do cativeiro foi fruto da resistência dos escravizados e… | [1] | [30] [7] [31] [4] | — |
| `#55` Nascido livre em Salvador em 1830, Luiz Gama foi vendido ilegalmente como escravizado por seu próprio pai aos dez anos… | [1] | [12] [33] [32] [7] | — |
| `#58` A estratégia jurídica desenvolvida por Luiz Gama consistia em aplicar rigorosamente as leis imperiais, em especial a Le… | [12] | [33] [1] [8] [38] [32] | — |
| `#67` Filho de uma mulher negra liberta e de um vigário, Patrocínio utilizou os jornais Gazeta da Tarde e Cidade do Rio para… | [24] | [7] [36] [37] [35] [49] [30] [12] [28] [31] | — |
| `#75` A atuação dos Caifazes baseava-se em organizar a desestruturação do trabalho nas lavouras de café. | [6] | [5] [23] [39] [40] [24] [38] [2] | — |
| `#76` Agentes conhecidos como "cometas" infiltravam-se nas propriedades do interior paulista para incitar e coordenar fugas c… | [6] | [39] [40] [5] [24] [23] [31] [7] [30] [32] [12] | — |
| `#77` As rotas de fuga utilizavam as linhas ferroviárias provinciais para transportar os libertandos até abrigos na capital —… | [6] | [39] [5] [24] [40] [31] [2] [30] [7] [37] | — |
| `#80` La, os refugiados encontravam proteção e organização para o trabalho livre. | [6] | [5] [40] [7] [39] [31] [30] [32] [24] [1] [33] [29] | — |
| `#91` Em maio do mesmo ano, a Província do Amazonas adotou medida idêntica. | [24] | — | [8] [30] [31] [28] [32] [7] [4] [2] ⚠ |
| `#94` Fugas em massa, a proliferação de quilombos e a recusa contínua dos cativos em aceitar a disciplina das fazendas tornar… | [6] | [5] [31] [7] [39] [40] [23] [30] [32] [1] [24] [41] | — |
| `#103` A aprovação da Lei Áurea sem indenização financeira provocou o rompimento da classe fundiária com a Monarquia. | [8] | [49] [37] [35] [28] [44] [7] [31] [30] [47] [5] [20] [11] [12] [29] [17] | — |
| `#105` Sentindo-se abandonados pelo Trono, esses proprietários retiraram seu suporte ao imperador D. Pedro II. | [46] | [49] [24] [47] [5] [19] [37] [9] [35] [32] [31] [7] [27] | — |
| `#107` A perda do apoio da elite agroexportadora isolou politicamente a Coroa. | [46] | [49] [31] [24] [30] [47] [19] [41] [32] [7] | — |
| `#108` A articulação entre os proprietários rurais descontentes, os militares positivistas e os setores urbanos culminou no go… | [46] | [47] [49] [24] | — |
| `#109` A ruína da Monarquia demonstrou que o regime imperial estava estruturalmente vinculado à sustentação do cativeiro, ruin… | [1] | [49] [7] [31] [30] [24] [47] | — |
| `#119` Esse processo de exclusão deliberada perpetuou disparidades sociais, econômicas e políticas baseadas na raça. | [3] | [7] [1] [24] [44] [25] [31] [30] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2507545 |
| **Média de tokens por requisição** | 22190.7 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 28/49 (57.1%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 1.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[8]](https://www.gov.br/arquivonacional/pt-br/sites_eventos/sites-tematicos-1/brasil-oitocentista/temas-oitocentistas/legislacao-abolicionista-no-imperio) | downloaded | 16 | 5 | 8 | 3 | 0 |
| [[2]](https://pt.wikipedia.org/wiki/Lei_Eus%C3%A9bio_de_Queir%C3%B3s) | downloaded | 15 | 4 | 10 | 1 | 0 |
| [[1]](https://periodicos.ufs.br/pontadelanca/article/download/25036/18611) | downloaded | 14 | 6 | 6 | 2 | 0 |
| [[3]](https://agenciadenoticias.uniceub.br/brasil/lei-eusebio-de-queiros-historiador-explica-por-que-pressao-contra-escravidao-nao-surtiu-efeito/) | downloaded | 10 | 3 | 5 | 2 | 0 |
| [[6]](https://www.gazetasp.com.br/gazeta-mais/conheca-os-caifazes-grupo-que-libertou-escravizados-em-sp/) | downloaded | 10 | 1 | 9 | 0 | 0 |
| [[22]](https://plenarinho.leg.br/index.php/2022/07/francisco-jose-nascimento-o-dragao-mar/) | inaccessible | 10 | 0 | 0 | 0 | 10 |
| [[24]](https://www.scielo.br/j/rbh/a/t45Yx9zKgpGB8STCkPLxBNL/?format=pdf&lang=pt) | downloaded | 9 | 5 | 3 | 1 | 0 |
| [[5]](https://www.novomilenio.inf.br/santos/h0222p.htm) | downloaded | 6 | 3 | 2 | 1 | 0 |
| [[10]](https://www.historiadomundo.com.br/idade-moderna/lei-do-ventre-livre.htm) | downloaded | 6 | 4 | 2 | 0 | 0 |
| [[17]](https://brasilescola.uol.com.br/historiab/lei-terras-1850.htm) | downloaded | 5 | 0 | 4 | 1 | 0 |
| [[9]](https://www.planalto.gov.br/ccivil_03/leis/l0601-1850.htm) | downloaded | 4 | 2 | 2 | 0 | 0 |
| [[46]](https://www12.senado.leg.br/institucional/museu/exposicoes/brasil-da-monarquia-a-republica/galeria/video/a-proclamacao-da-republica) | downloaded | 4 | 0 | 3 | 1 | 0 |
| [[12]](https://pcdob.org.br/noticias/como-uma-acao-do-advogado-negro-luiz-gama-libertou-217-escravizados/) | downloaded | 3 | 1 | 2 | 0 | 0 |
| [[4]](https://almapreta.com.br/sessao/cotidiano/nao-mudou-a-estrutura-lei-que-proibiu-o-trafico-de-africanos-escravizados-teve-efeito-controverso-no-brasil/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[25]](https://almapreta.com.br/sessao/cotidiano/leis-do-ventre-livre-e-dos-sexagenarios-promessas-de-liberdade-que-prolongaram-a-escravidao/) | downloaded | 2 | 0 | 1 | 1 | 0 |
| [[30]](https://www.scielo.br/j/nec/a/CrVbxyNKtm7vCZWxXgRz6qg/?lang=pt) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[11]](https://mapa.an.gov.br/index.php/assuntos/15-dicionario/65-dicionario-da-administracao-publica-brasileira-do-periodo-imperial/288-lei-euzebio-de-queiroz) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[16]](https://www.youtube.com/watch?v=JZE5kXm_Gfs) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[27]](https://www12.senado.leg.br/noticias/materias/2015/08/31/lei-dos-sexagenarios-completa-130-anos) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[28]](https://brasilescola.uol.com.br/historiab/lei-dos-sexagenarios.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[35]](https://www.scielo.br/j/ea/a/KbgXK6SYWhXTNT4Hv5hCsWG/?lang=pt&format=pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[7]](https://repositorio.ufu.br/bitstream/123456789/31008/4/MovimentoAbolicionistaBrasileiro.pdf) | downloaded | 0 · nunca citada | — | — | — | — |
| [[13]](https://www2.senado.leg.br/bdsf/handle/id/174446) | blocked | 0 · nunca citada | — | — | — | — |
| [[14]](http://www.planalto.gov.br/ccivil_03/leis/lim/LIM581.htm) | downloaded | 0 · nunca citada | — | — | — | — |
| [[15]](https://www12.senado.leg.br/noticias/noticias/audios/2020/09/lei-eusebio-de-queiroz-completa-170-anos) | downloaded | 0 · nunca citada | — | — | — | — |
| [[18]](https://ojs.sites.ufsc.br/index.php/sceh/article/view/182/157) | downloaded | 0 · nunca citada | — | — | — | — |
| [[19]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/ha-170-anos-lei-de-terras-desprezou-camponeses-e-oficializou-apoio-do-brasil-aos-latifundios) | downloaded | 0 · nunca citada | — | — | — | — |
| [[20]](https://mapa.an.gov.br/index.php/assuntos/15-dicionario/65-dicionario-da-administracao-publica-brasileira-do-periodo-imperial/279-lei-de-terras) | downloaded | 0 · nunca citada | — | — | — | — |
| [[21]](https://revistagalo.com.br/edi%C3%A7%C3%B5es/edi%C3%A7%C3%A3o-010/05-lei-de-terras/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[23]](https://pt.wikipedia.org/wiki/Caifases) | downloaded | 0 · nunca citada | — | — | — | — |
| [[26]](https://www.todamateria.com.br/lei-do-ventre-livre-1871/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[29]](https://mapa.an.gov.br/index.php/assuntos/15-dicionario/65-dicionario-da-administracao-publica-brasileira-do-periodo-imperial/280-lei-dos-sexagenarios) | downloaded | 0 · nunca citada | — | — | — | — |
| [[31]](https://www.scielo.br/j/nec/a/CrVbxyNKtm7vCZWxXgRz6qg/?format=pdf&lang=pt) | downloaded | 0 · nunca citada | — | — | — | — |
| [[32]](https://www.scielo.br/j/ea/a/zJHRTBVXN8tqfnkJNhG5YPk/?lang=pt) | downloaded | 0 · nunca citada | — | — | — | — |
| [[33]](https://pt.wikipedia.org/wiki/Luiz_Gama) | downloaded | 0 · nunca citada | — | — | — | — |
| [[34]](https://www.scielosp.org/article/csc/2026.v31n5/e02592026/pt/) | blocked | 0 · nunca citada | — | — | — | — |
| [[36]](https://pt.wikipedia.org/wiki/Sociedade_Brasileira_contra_a_Escravid%C3%A3o) | downloaded | 0 · nunca citada | — | — | — | — |
| [[37]](http://www.scielo.br/j/ea/a/KbgXK6SYWhXTNT4Hv5hCsWG/?lang=pt) | downloaded | 0 · nunca citada | — | — | — | — |
| [[38]](https://periodicos.ufjf.br/index.php/locus/article/download/20657/11070/82472) | downloaded | 0 · nunca citada | — | — | — | — |
| [[39]](https://araoalves.blogspot.com/2012/02/caifazes.html) | downloaded | 0 · nunca citada | — | — | — | — |
| [[40]](https://saopaulopassado.wordpress.com/2015/03/24/os-caifazes-de-antonio-bento/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[41]](https://www1.folha.uol.com.br/fsp/1998/4/04/dinheiro/4.html) | downloaded | 0 · nunca citada | — | — | — | — |
| [[42]](https://www.youtube.com/watch?v=LpDDxbiNbw0) | downloaded | 0 · nunca citada | — | — | — | — |
| [[43]](https://www.youtube.com/watch?v=WY_aBWfTV-Y) | downloaded | 0 · nunca citada | — | — | — | — |
| [[44]](https://blogdoedisonsilva.com.br/2020/05/13/senado-esqueceram-do-ceara-ao-falarem-da-abolicao-da-escravatura-no-brasil/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[45]](https://legis.senado.leg.br/sdleg-getter/documento?dm=2925895&disposition=inline) | downloaded | 0 · nunca citada | — | — | — | — |
| [[47]](https://brasilescola.uol.com.br/historiab/proclamacaodarepublica.htm) | downloaded | 0 · nunca citada | — | — | — | — |
| [[48]](https://www.facebook.com/TVSenado/videos/proclama%C3%A7%C3%A3o-da-rep%C3%BAblica/753944411735824/) | downloaded | 0 · nunca citada | — | — | — | — |
| [[49]](https://www.sbp.com.br/fileadmin/user_upload/2016/10/2016.1.Proclamao-da-Republica-do-Brasil.pdf) | downloaded | 0 · nunca citada | — | — | — | — |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[8]](https://www.gov.br/arquivonacional/pt-br/sites_eventos/sites-tematicos-1/brasil-oitocentista/temas-oitocentistas/legislacao-abolicionista-no-imperio) | #40–41, #100–101, #110 | #45, #97–99, #102–103, #111, #113 | #96, #114–115 | `#40` Somente em 1871 foi promulgada a lei n. 2.040, de 28 de setembro, conhecida como Lei do Ventre Livre ou Lei Rio Branco |
| [[2]](https://pt.wikipedia.org/wiki/Lei_Eus%C3%A9bio_de_Queir%C3%B3s) | #10, #19, #22, #32 | #3–4, #13, #18, #21, #33–35, #117–118 | #116 | `#10` O projeto foi o primeiro a gerar efeitos imediatos na estrutura do tráfico. A entrada de novos escravos baixou a zero em apenas três anos. (...) com a lei, a o… |
| [[1]](https://periodicos.ufs.br/pontadelanca/article/download/25036/18611) | #0, #6, #54, #56–57, #61 | #2, #5, #7, #53, #55, #109 | #1, #104 | `#0` A historiografia tem mostrado que a escravidão não funcionou como simples resíduo colonial em declínio, mas como princípio organizador da vida econômica, socia… |
| [[3]](https://agenciadenoticias.uniceub.br/brasil/lei-eusebio-de-queiros-historiador-explica-por-que-pressao-contra-escravidao-nao-surtiu-efeito/) | #8, #20, #121 | #9, #11–12, #119, #122 | #16, #120 | `#8` Mesmo com as imposições, a escravidão demorou para acabar. Em 1845, o parlamento inglês determinou a Lei Bill Aberdeen [...] As críticas efetivamente relaciona… |
| [[6]](https://www.gazetasp.com.br/gazeta-mais/conheca-os-caifazes-grupo-que-libertou-escravizados-em-sp/) | #78 | #70, #74–77, #79–81, #94 | — | `#78` Além de resgatar escravizados, o movimento oferecia lugares de acolhimento, geralmente no quilombo do Jabaquara, em Santos. |
| [[24]](https://www.scielo.br/j/rbh/a/t45Yx9zKgpGB8STCkPLxBNL/?format=pdf&lang=pt) | #62, #65–66, #68, #93 | #67, #69, #91 | #63 | `#62` Foram os seus discursos que chamaram e estimularam uma atenção mais ampla, que deram início ao processo de mobilização com um comunicado na imprensa em 1879. I… |
| [[5]](https://www.novomilenio.inf.br/santos/h0222p.htm) | #71–73 | #37, #82 | #38 | `#71` Se, num primeiro momento, o movimento abolicionista paulista limitava-se a uma ação parlamentar, o segundo, que se inicia na década de 1880, é marcado por uma… |
| [[10]](https://www.historiadomundo.com.br/idade-moderna/lei-do-ventre-livre.htm) | #39, #42, #44, #46 | #43, #49 | — | `#39` o país estava cada vez mais isolado internacionalmente nessa pauta [...] se o Brasil não fizesse pequenas reformas na escravidão correria o grande risco de lid… |
| [[17]](https://brasilescola.uol.com.br/historiab/lei-terras-1850.htm) | — | #25, #29–31 | #112 | `#25` Dessa maneira, ex-escravos e estrangeiros teriam que enfrentar enormes restrições para possivelmente galgarem a condição de pequeno e médio proprietário. |
| [[9]](https://www.planalto.gov.br/ccivil_03/leis/l0601-1850.htm) | #26–27 | #23, #28 | — | `#26` Art. 1º Ficam prohibidas as acquisições de terras devolutas por outro titulo que não seja o de compra. |
| [[46]](https://www12.senado.leg.br/institucional/museu/exposicoes/brasil-da-monarquia-a-republica/galeria/video/a-proclamacao-da-republica) | — | #105, #107–108 | #106 | `#105` sob fortes questionamentos dos fazendeiros, dos militares e da Igreja, o imperador D. Pedro II é deposto |
| [[12]](https://pcdob.org.br/noticias/como-uma-acao-do-advogado-negro-luiz-gama-libertou-217-escravizados/) | #59 | #58, #60 | — | `#59` Em 7 de novembro de 1831, pressionado pela Inglaterra, o Império brasileiro assinou uma lei que proibia o tráfico de africanos ao Brasil. Ou seja, a partir daq… |
| [[4]](https://almapreta.com.br/sessao/cotidiano/nao-mudou-a-estrutura-lei-que-proibiu-o-trafico-de-africanos-escravizados-teve-efeito-controverso-no-brasil/) | — | #14–15 | — | `#14` Diante da expiração do tratado no início de 1845, o Parlamento britânico aprovou, no mesmo ano, a chamada Lei do Comércio de Escravos, conhecida como Lei Aberd… |
| [[25]](https://almapreta.com.br/sessao/cotidiano/leis-do-ventre-livre-e-dos-sexagenarios-promessas-de-liberdade-que-prolongaram-a-escravidao/) | — | #51 | #50 | `#51` A lei permitia que os senhores se livrassem de uma força de trabalho considerada improdutiva sem arcar com os custos de seu sustento na velhice |
| [[30]](https://www.scielo.br/j/nec/a/CrVbxyNKtm7vCZWxXgRz6qg/?lang=pt) | #52, #95 | — | — | `#52` Nabuco foi o mais poderoso difusor do recorte. Em Um estadista do Império [...] atribuiu a uma facção da elite imperial e ao imperador a capacidade [...] de de… |
| [[11]](https://mapa.an.gov.br/index.php/assuntos/15-dicionario/65-dicionario-da-administracao-publica-brasileira-do-periodo-imperial/288-lei-euzebio-de-queiroz) | — | #17 | — | `#17` A lei n. 581, de 4 de setembro de 1850, conhecida como Lei Eusébio de Queirós |
| [[16]](https://www.youtube.com/watch?v=JZE5kXm_Gfs) | — | — | #24 | — |
| [[27]](https://www12.senado.leg.br/noticias/materias/2015/08/31/lei-dos-sexagenarios-completa-130-anos) | — | #47 | — | `#47` No próximo dia 28 de setembro, a lei que libertou os escravos com 60 anos ou mais completará 130 anos. |
| [[28]](https://brasilescola.uol.com.br/historiab/lei-dos-sexagenarios.htm) | #48 | — | — | `#48` Escravos com mais de 60 anos seriam considerados livres; [...] Como indenização, os sexagenários escravizados deveriam trabalhar para os seus senhores por três… |
| [[35]](https://www.scielo.br/j/ea/a/KbgXK6SYWhXTNT4Hv5hCsWG/?lang=pt&format=pdf) | #64 | — | — | `#64` em 7 de setembro de 1880, nabuco fundou com outros companheiros em sua própria residência no Rio de Janeiro (Rua Bela da Princesa, hoje Correia dutra) a socied… |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://plenarinho.leg.br/index.php/2022/07/francisco-jose-nascimento-o-dragao-mar/ — Falha de SSL em https://plenarinho.leg.br/index.php/2022/07/francisco-jose-nascimento-o-dragao-mar/, mesmo sem verificar o certificado: Failed to perform, curl: (35) Recv failure: Connection reset by peer. See https://curl.se/libcurl/c/libcurl-errors.html first for more details.

### Bloqueadas por barreira de acesso

- https://www2.senado.leg.br/bdsf/handle/id/174446 — anti_bot — barreira de acesso (anti_bot): Verificando sua conexão Estamos confirmando que este acesso é legítimo antes de liberar o conteúdo. Isso leva apenas alg
- https://www.scielosp.org/article/csc/2026.v31n5/e02592026/pt/ — anti_bot — barreira de acesso (anti_bot): This website is using a security service to protect itself from online attacks. We are checking your browser to establis

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-0`** [1]
  - Trecho: A escravidão africana não constituiu apenas um modo de produção ou um arranjo de trabalho transitório no Brasil Oitocentista; configurou-se como o princípio ordenador da vida econômica, social, jurídica e política da so…
  - Justificativa: A evidência, especialmente na primeira referência, afirma explicitamente que a escravidão não funcionou como simples resíduo colonial em declínio, mas como princípio organizador da vida econômica, social, jurídica e pol…
  - Suporte veio de: [1]
  - Evidência: “A historiografia tem mostrado que a escravidão não funcionou como simples resíduo colonial em declínio, mas como princípio organizador da vida econômica, social, jurídica e política do Império.”
- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-6`** [1]
  - Trecho: A defesa do elemento servil mobilizou todo o aparato institucional monárquico.
  - Justificativa: A evidência descreve a escravidão como princípio organizador da vida econômica, social, jurídica e política do Império, e a ordem jurídica imperial como expressão de um amplo pacto social contra os escravizados. Isso su…
  - Suporte veio de: [1]
  - Evidência: “a escravidão não funcionou como simples resíduo colonial em declínio, mas como princípio organizador da vida econômica, social, jurídica e política do Império”
- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-8`** [3]
  - Trecho: Não obstante essa aparente solidez, a perpetuação da escravidão enfrentou tensões internas e pressões internacionais graduais.
  - Justificativa: A evidência sustenta explicitamente tanto as 'pressões internacionais graduais' (Lei Bill Aberdeen de 1845, campanha inglesa de abolição do tráfico, pressão da Inglaterra sobre o Brasil) quanto as 'tensões internas' (cr…
  - Suporte veio de: [3]
  - Evidência: “Mesmo com as imposições, a escravidão demorou para acabar. Em 1845, o parlamento inglês determinou a Lei Bill Aberdeen, que dava autorização aos navios ingleses para abordar embarcações que trafegavam no Atlântico com e…”
### UNSUPPORTED

- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-1`** [1]
  - Trecho: Desde o estabelecimento da lavoura açucareira no período colonial até a consolidação da cafeicultura no século XIX, a posse de seres humanos escravizados operou como o pilar central da estrutura patrimonial, o principal…
  - Justificativa: A evidência sustenta que a escravidão foi princípio organizador da vida econômica, social, jurídica e política do Império e que pessoas escravizadas eram tratadas como propriedade, mas não menciona especificamente a lav…
  - Suporte veio de: [1]
  - Evidência: “a escravidão não funcionou como simples resíduo colonial em declínio, mas como princípio organizador da vida econômica, social, jurídica e política do Império”
  - Não coberto pela evidência: Estabelecimento da lavoura açucareira no período colonial; Consolidação da cafeicultura no século XIX; Principal colateral para a concessão de crédito agrícola
  - Verificação: UNSUPPORTED confirmado — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-2`** [1]
  - Trecho: O processo de formação do Estado nacional brasileiro esteve intrinsecamente vinculado à preservação da ordem escravocrata, articulando um pacto entre as elites agrárias provinciais e a burocracia estatal para garantir a…
  - Justificativa: A evidência sustenta parcialmente a afirmação: confirma a vinculação entre formação do Estado nacional e preservação da ordem escravocrata, e menciona um 'amplo pacto social contra os escravizados'. Contudo, não especif…
  - Suporte veio de: [1]
  - Evidência: “Salles (2012) relaciona a formação do Estado nacional à consolidação histórica da classe senhorial”
  - Não coberto pela evidência: pacto entre as elites agrárias provinciais e a burocracia estatal (a evidência fala em 'amplo pacto social contra os escravizados' entre 'diferentes regiões, classes e setores econômicos', não especifica elites agrárias provinciais nem burocracia estatal); garantir a estabilidade territorial (não mencionado na evidência); continuidade do modelo agroexportador (não mencionado na evidência)
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_556b26a777e4_20261024T231607Z-3`** [2]
  - Trecho: No decorrer do século XIX, a expansão do cultivo do café no Vale do Paraíba e, subsequentemente, no Oeste Paulista consolidou o setor agroexportador como o motor da economia do Império.
  - Justificativa: A evidência trata principalmente da Lei Eusébio de Queirós e do fim do tráfico de escravos. Embora mencione áreas cafeeiras no Rio de Janeiro e São Paulo e 'cafeicultores do oeste paulista', não menciona 'Vale do Paraíb…
  - Suporte veio de: [2]
  - Não coberto pela evidência: Expansão do cultivo do café no Vale do Paraíba (não mencionado por nome); Subsequência cronológica: Vale do Paraíba → Oeste Paulista; Consolidação do setor agroexportador como motor da economia do Império
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [17] [24] [49] [7] [11] [5] [3] [8] [1] [20] [33] [47] [4] [23] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 10 citam referência não baixada/inacessível.

- `escravidao_brasil_556b26a777e4_20261024T231607Z-36` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-83` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-84` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-85` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-86` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-87` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-88` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-89` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-90` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_556b26a777e4_20261024T231607Z-92` — Referencia(s) citada(s) ['46011394e9d2be64'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).