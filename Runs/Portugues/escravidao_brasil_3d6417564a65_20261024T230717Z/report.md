# Relatório de Auditoria — Claude (escravidao_brasil_3d6417564a65_20261024T230717Z)

**Arquivo auditado:** `answers/Claude/Consolidado/escravidao_brasil.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | escravidao_brasil_3d6417564a65_20261024T230717Z |
| **Ferramenta** | Claude |
| **Gerado em** | 2026-11-04T03:40:55.586636+00:00 |
| **Total de trechos citados** | 87 |
| **Tempo de processamento** | 10:04:33:38 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 28.8 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 87 marcadores, 51 distintos |
| Referências listadas | 51 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 80 | 92.0% |
| **UNSUPPORTED** | 2 | 2.3% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 5 | 5.7% |
| **TOTAL** | 87 | 100.0% |

Sobre os 82 trechos citados auditados: SUPPORTED 97,56%, UNSUPPORTED 2,43%, CONTRADICTED 0,00%.

> **6 dos 80 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 6 estão **contados dentro** dos 80 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`2` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `0` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `0` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `1` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#86` A lei extinguiu o cativeiro, mas os libertos continuaram marginalizados e expostos ao racismo e à violência. | [1] | [47] [45] [46] [4] [30] [17] [35] [26] [12] [13] [24] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 408791 |
| **Média de tokens por requisição** | 4985.3 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/51 (0.0%)

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[32]](https://congressoemfoco.com.br/noticia/14616/lei-aurea-a-historia-do-seu-nascimento) | downloaded | 5 | 5 | 0 | 0 | 0 |
| [[1]](https://fpabramo.org.br/timeline/lei-aurea/) | downloaded | 4 | 3 | 1 | 0 | 0 |
| [[6]](https://www.preparaenem.com/historia-do-brasil/lei-eusebio-de-queiros.htm) | downloaded | 4 | 4 | 0 | 0 | 0 |
| [[7]](https://www.preparaenem.com/historia-do-brasil/o-lento-processo-abolicao-escravidao-no-brasil.htm) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[13]](https://almapreta.com.br/sessao/cotidiano/leis-do-ventre-livre-e-dos-sexagenarios-promessas-de-liberdade-que-prolongaram-a-escravidao/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[22]](https://www.preparaenem.com/amp/historia-do-brasil/movimento-abolicionista-elite-ou-popular.htm) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[27]](https://www.preparaenem.com/historia-do-brasil/caifazes-luta-pela-abolicao-no-imperio.htm) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[45]](https://historiaeeconomia.pt/index.php/he/article/download/337/242) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[48]](https://vestibulares.estrategia.com/portal/historia/herancas-da-escravidao-na-primeira-republica/) | downloaded | 3 | 3 | 0 | 0 | 0 |
| [[2]](https://almapreta.com.br/?p=13245) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[3]](https://www.poder360.com.br/brasil/censo-de-1872-registrou-15-milhao-de-escravos-no-brasil/) | downloaded | 2 | 1 | 1 | 0 | 0 |
| [[4]](https://ojs.ifch.unicamp.br/index.php/rhs/article/download/315/271/20740) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[5]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/marinha-britanica-forcou-brasil-a-acabar-com-trafico-negreiro) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[16]](https://www.historiadomundo.com.br/idade-moderna/lei-dos-sexagenarios.htm) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[17]](https://www.preparaenem.com/historia-do-brasil/lei-dos-sexagenarios.htm) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[18]](https://www.conjur.com.br/?p=352983) | dead | 2 | 0 | 0 | 0 | 2 |
| [[23]](https://mais.opovo.com.br/jornal/cidades/2023/03/25/data-magna-do-ceara-marca-pioneirismo-do-estado-em-abolir-a-escravidao.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[31]](https://vermelho.org.br/2014/08/03/joao-quartim-de-moraes-fala-sobre-a-esquerda-militar-no-brasil/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[34]](https://www.infoescola.com/historia-do-brasil/lei-aurea/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[35]](https://www.historiadomundo.com.br/idade-moderna/lei-aurea.htm) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[36]](https://companhiadasletras.com.br/sala_professor/pdfs/CadernoAtividades_BrasilUmaBiografia_cap12.pdf) | dead | 2 | 0 | 0 | 0 | 2 |
| [[39]](https://www.jornalopcao.com.br/colunas-e-blogs/periscopio/luta-de-jose-do-patrocinio-pela-abolicao-da-escravidao-no-brasil-573744/) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[42]](https://www.conjur.com.br/2015-set-13/embargos-culturais-rui-barbosa-polemica-queima-arquivos-escravidao) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[8]](https://periodicos.sbu.unicamp.br/ojs/index.php/resgate/article/download/8659126/25743/89334) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[9]](https://projetoagathaedu.com.br/questoes-vestibular/resolucao-historia/imperio/lei-de-terras.php) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[10]](https://www.eco.unicamp.br/images/arquivos/artigos/447/10-PLINIO6.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[11]](https://www.historiadomundo.com.br/idade-moderna/lei-do-ventre-livre.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[12]](https://www.preparaenem.com/historia-do-brasil/leis-abolicionistas-no-imperio.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[14]](https://anpuh.org.br/uploads/anais-simposios/pdf/2019-01/1548855456_fc442dbc3e312c198a5a1acac6eb5a11.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[15]](https://www.preparaenem.com/historia-do-brasil/lei-do-ventre-livre.htm) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[19]](https://jcconcursos.com.br/noticia/area-juridica/luiz-gama-heroi-do-povo-brasileiro-5458) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[20]](https://jus.com.br/artigos/97597/direito-e-arte) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.brasilparalelo.com.br/noticias/conheca-a-historia-de-quatro-brasileiros-que-lutaram-contra-a-escravidao) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[24]](https://www.opovo.com.br/noticias/ceara/2020/03/24/data-magna-do-ceara--primeira-provincia-a-libertar-escravizados-manteve-exploracao-mesmo-apos-abolicao--aponta-historiadoras.html) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[25]](https://portalamazonia.com/cultura/ruas-manaus-batizadas-com-datas/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[26]](https://portalamazonia.com/historias-da-amazonia/a-maconaria-e-a-libertacao-dos-escravos-no-amazonas/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[28]](https://periodicos.ufpel.edu.br/index.php/CLIO/article/view/16061/10724) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[29]](https://projetoagathaedu.com.br/blog/historia-do-brasil/imperio/questao-escravista.php) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[30]](https://seer.ufrgs.br/index.php/revistaihgrgs/article/download/106925/58221/439482) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[33]](https://www.todamateria.com.br/lei-aurea/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[37]](https://www.todamateria.com.br/exercicio-sobre-a-proclamacao-da-republica-15-de-novembro/) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[38]](https://anpuh.org.br/uploads/anais-simposios/pdf/2019-01/1548772007_1e0263eca733383e79934480401fc831.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[40]](https://www.maxwell.vrac.puc-rio.br/6401/6401_4.PDF) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[41]](https://www.migalhas.com.br/quentes/100434/pretensao-de-incinerar-processos-arquivados-ja-foi-enfrentada-pelo-stj) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[43]](https://www2.ufjf.br/arquivocentral/?p=10421) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[44]](https://www.gov.br/casaruibarbosa/pt-br/centrais-de-conteudo/publicacoes/pdfs/rui-barbosa-e-a-queima-dos-arquivos-ocr.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[46]](https://ojs.uel.br/revistas/uel/index.php/mediacoes/article/download/9096/7647/33416) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[47]](https://anais-siiepe.ufpel.edu.br/2022/CH_06026.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[49]](https://doaj.org/article/0e1d0967ed73404387fb60208ca04c55) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[50]](https://trt15.jus.br/noticia/2022/abolicao-o-protagonismo-dos-escravizados-em-uma-luta-que-ainda-nao-terminou) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[51]](https://static.even3.com/anais/1369885.pdf) | downloaded | 1 | 1 | 0 | 0 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[32]](https://congressoemfoco.com.br/noticia/14616/lei-aurea-a-historia-do-seu-nascimento) | #49–53 | — | — | `#49` Em 1888, o sistema escravista estava apodrecendo e se desintegrando de forma evidente desde o ano anterior. |
| [[1]](https://fpabramo.org.br/timeline/lei-aurea/) | #0, #2, #73 | #86 | — | `#0` Lei nº 3.353 de 13 de maio de 1888 decretou o fim da escravidão no Brasil. Após 388 anos de tráfico e escravidão foi proibido o trabalho forçado, compulsório,… |
| [[6]](https://www.preparaenem.com/historia-do-brasil/lei-eusebio-de-queiros.htm) | #10–12, #14 | — | — | `#10` essa lei dava autorização para que a marinha britânica monitorasse o Oceano Atlântico à procura de navios negreiros. [...] O Bill Aberdeen foi aprovado na Ingl… |
| [[7]](https://www.preparaenem.com/historia-do-brasil/o-lento-processo-abolicao-escravidao-no-brasil.htm) | #13, #15–16 | — | — | `#13` A Lei Eusébio de Queirós, diferentemente da Lei Feijó, foi efetivamente aplicada e, em praticamente três anos, esse mercado já estava extinto no Brasil. |
| [[13]](https://almapreta.com.br/sessao/cotidiano/leis-do-ventre-livre-e-dos-sexagenarios-promessas-de-liberdade-que-prolongaram-a-escravidao/) | #21, #25, #84 | — | — | `#21` Após essa idade, o senhor de escravizados tinha duas opções: entregar a criança ao Estado e receber uma indenização de 600 mil contos de réis ou utilizar os se… |
| [[22]](https://www.preparaenem.com/amp/historia-do-brasil/movimento-abolicionista-elite-ou-popular.htm) | #34–35, #83 | — | — | `#34` Ou na Confederação Abolicionista, fundada por José do Patrocínio e outros militantes em 1883. |
| [[27]](https://www.preparaenem.com/historia-do-brasil/caifazes-luta-pela-abolicao-no-imperio.htm) | #41–43 | — | — | `#41` Antônio Bento formou o grupo dos caifazes em 1882, quando da morte do advogado negro e abolicionista Luiz Gama. Antes disso, Antônio Bento havia sido delegado… |
| [[45]](https://historiaeeconomia.pt/index.php/he/article/download/337/242) | #75–76, #78 | — | — | `#75` São Paulo recebeu mais de dois milhões de imigrantes europeus, e quase metade tiveram suas passagens subsidiadas pelo governo do Estado no processo intencional… |
| [[48]](https://vestibulares.estrategia.com/portal/historia/herancas-da-escravidao-na-primeira-republica/) | #68, #81–82 | — | — | `#68` Rui Barbosa, então ministro da Fazenda do governo Deodoro da Fonseca, mandaria queimar documentos da escravidão, a fim de impedir que fazendeiros buscassem ind… |
| [[2]](https://almapreta.com.br/?p=13245) | #1, #7 | — | — | `#1` Desse total, 4,8 milhões de pessoas sobreviveram à travessia. Ou seja, cerca de 500 mil vidas humanas foram perdidas em quase 10 mil viagens através do Atlânti… |
| [[3]](https://www.poder360.com.br/brasil/censo-de-1872-registrou-15-milhao-de-escravos-no-brasil/) | #3 | #57 | — | `#3` O Censo de 1872 encontrou no país quase 10 milhões de pessoas (mais precisamente, 9.930.478). Hoje, como comparação, só a cidade de São Paulo tem 12,4 milhões… |
| [[4]](https://ojs.ifch.unicamp.br/index.php/rhs/article/download/315/271/20740) | #4–5 | — | — | `#4` a população brasileira somava 9.930.478 habitantes, divididos, quanto à condição social, em 8.419.672 livres (84,78%) e 1.510.806 escravos (15,21%). |
| [[5]](https://www12.senado.leg.br/noticias/especiais/arquivo-s/marinha-britanica-forcou-brasil-a-acabar-com-trafico-negreiro) | #6, #8 | — | — | `#6` Passaram-se longos 24 anos desde a assinatura de um tratado com a Grã-Bretanha, em 1826, pelo qual o governo brasileiro se comprometeu a acabar com comércio de… |
| [[16]](https://www.historiadomundo.com.br/idade-moderna/lei-dos-sexagenarios.htm) | #26, #28 | — | — | `#26` A Lei dos Sexagenários foi considerada uma lei muito conservadora e que retirou as proposições que promoviam as mudanças mais radicais propostas por Dantas. |
| [[17]](https://www.preparaenem.com/historia-do-brasil/lei-dos-sexagenarios.htm) | #24, #27 | — | — | `#24` determinou a libertação dos escravos com mais de 60 anos. Entretanto, a lei também regulou diversos aspectos relativos à alforria de cativos, bem como determin… |
| [[23]](https://mais.opovo.com.br/jornal/cidades/2023/03/25/data-magna-do-ceara-marca-pioneirismo-do-estado-em-abolir-a-escravidao.html) | #36–37 | — | — | `#36` Um dos principais nomes do movimento abolicionista cearense é o do jangadeiro Francisco José do Nascimento, também conhecido como **Dragão do Mar** ou Chico da… |
| [[31]](https://vermelho.org.br/2014/08/03/joao-quartim-de-moraes-fala-sobre-a-esquerda-militar-no-brasil/) | #46, #48 | — | — | `#46` intensificava-se a caça aos fugitivos; como, porém, embora numerosos, os esbirros empregados neste sórdido trabalho de busca e captura mostravam-se incapazes d… |
| [[34]](https://www.infoescola.com/historia-do-brasil/lei-aurea/) | #55, #59 | — | — | `#55` O número de escravizados na data não é tão expressivo tendo em vista um grande contingente de libertos já existentes no país. |
| [[35]](https://www.historiadomundo.com.br/idade-moderna/lei-aurea.htm) | #56, #58 | — | — | `#56` existiam cerca de 720 mil escravos no Brasil quando a Lei Áurea foi assinada em 13 de maio de 1888 |
| [[39]](https://www.jornalopcao.com.br/colunas-e-blogs/periscopio/luta-de-jose-do-patrocinio-pela-abolicao-da-escravidao-no-brasil-573744/) | #64, #66 | — | — | `#64` Patrocínio criou a Guarda Negra da Redentora, formada por negros e ex-escravos, que defendia a monarquia e combatia o movimento republicano. Essa guarda exalta… |
| [[42]](https://www.conjur.com.br/2015-set-13/embargos-culturais-rui-barbosa-polemica-queima-arquivos-escravidao) | #69–70 | — | — | `#69` Quando ministro da fazenda Rui negou pedido de indenização, em passagem memorável de sua biografia. |
| [[8]](https://periodicos.sbu.unicamp.br/ojs/index.php/resgate/article/download/8659126/25743/89334) | #9 | — | — | `#9` mais 500.000 africanos escravizados foram admitidos no país ilegalmente até o fim do tráfico em 1850, como é estimado por Conrad (1978). |
| [[9]](https://projetoagathaedu.com.br/questoes-vestibular/resolucao-historia/imperio/lei-de-terras.php) | #17 | — | — | `#17` Já no artigo 1°, a Lei n° 601/1850 determinava: “ficam proibidas as aquisições de terras devolutas por outro título que não seja o de compra”. |
| [[10]](https://www.eco.unicamp.br/images/arquivos/artigos/447/10-PLINIO6.pdf) | #18 | — | — | `#18` Os grandes fazendeiros perceberam que era indispensável vedar aos futuros libertos e aos imigrantes que fossem trazidos para substituí-los a livre ocupação das… |
| [[11]](https://www.historiadomundo.com.br/idade-moderna/lei-do-ventre-livre.htm) | #19 | — | — | `#19` estabelecia que os filhos de escravas nascidos após a lei entrar em vigor seriam considerados livres. [...] A proposta do Visconde do Rio Branco se tornou a Le… |
| [[12]](https://www.preparaenem.com/historia-do-brasil/leis-abolicionistas-no-imperio.htm) | #20 | — | — | `#20` além de ser, sobretudo, uma resposta à crescente onda de rebeliões e fugas de escravos no Brasil |
| [[14]](https://anpuh.org.br/uploads/anais-simposios/pdf/2019-01/1548855456_fc442dbc3e312c198a5a1acac6eb5a11.pdf) | #22 | — | — | `#22` Dos 400 mil ou mais ingênuos registrados até 1885, apenas 118 haviam sidos confiados ao governo. |
| [[15]](https://www.preparaenem.com/historia-do-brasil/lei-do-ventre-livre.htm) | #23 | — | — | `#23` A Lei do Ventre Livre contribuiu para enfraquecer momentaneamente o movimento abolicionista, embora tenha sido explorada por ele na luta. |
| [[19]](https://jcconcursos.com.br/noticia/area-juridica/luiz-gama-heroi-do-povo-brasileiro-5458) | #31 | — | — | `#31` tomou a opção definitiva de atuar como rábula até o fim da vida, em 1882. [...] No final da vida, Luiz Gama foi o grande inspirador do Movimento dos Caifazes [… |
| [[20]](https://jus.com.br/artigos/97597/direito-e-arte) | #32 | — | — | `#32` Seu reconhecimento ocorreu somente com a promulgação a Lei nº 13.629 de 2018, a qual o declara como patrono da abolição da escravidão do Brasil |
| [[21]](https://www.brasilparalelo.com.br/noticias/conheca-a-historia-de-quatro-brasileiros-que-lutaram-contra-a-escravidao) | #33 | — | — | `#33` Para além da abolição, André Rebouças elaborou um projeto educacional para capacitar os libertos e garantir que conseguissem trabalho. |
| [[24]](https://www.opovo.com.br/noticias/ceara/2020/03/24/data-magna-do-ceara--primeira-provincia-a-libertar-escravizados-manteve-exploracao-mesmo-apos-abolicao--aponta-historiadoras.html) | #38 | — | — | `#38` A crítica da professora diz respeito ao processo de abolição no Estado que, segundo ela, foi majoritariamente encabeçado pela elite branca cearense. [...] Mesm… |
| [[25]](https://portalamazonia.com/cultura/ruas-manaus-batizadas-com-datas/) | #39 | — | — | `#39` foi no dia 10 de julho de 1884, dois meses depois da abolição da escravidão em Manaus, que o Presidente Theodoreto Carlos de Faria Souto (1841-1893) abolia a e… |
| [[26]](https://portalamazonia.com/historias-da-amazonia/a-maconaria-e-a-libertacao-dos-escravos-no-amazonas/) | #40 | — | — | `#40` O Amazonas possuía em relação às outras províncias, pequena quantidade de escravos. Fácil, portanto, a propaganda abolicionista. |
| [[28]](https://periodicos.ufpel.edu.br/index.php/CLIO/article/view/16061/10724) | #44 | — | — | `#44` Concorda também Conrad que as fugas em massa nos anos de 1887-1888 contribuíram decisivamente para a abolição da escravidão [...] Durante a década de 1880 houv… |
| [[29]](https://projetoagathaedu.com.br/blog/historia-do-brasil/imperio/questao-escravista.php) | #45 | — | — | `#45` Fugas coletivas reduziam a capacidade de repressão individual dos senhores e transformavam a liberdade em fato antes mesmo da mudança legal. |
| [[30]](https://seer.ufrgs.br/index.php/revistaihgrgs/article/download/106925/58221/439482) | #47 | — | — | `#47` O Clube Militar registrou sua primeira grande vitória sob a presi- dência do Marechal Deodoro ao enviar petição à Princesa Izabel em 26 de outubro de 1887, (3)… |
| [[33]](https://www.todamateria.com.br/lei-aurea/) | #54 | — | — | `#54` Art. 1°: É declarada extincta desde a data desta lei a escravidão no Brasil. |
| [[37]](https://www.todamateria.com.br/exercicio-sobre-a-proclamacao-da-republica-15-de-novembro/) | #62 | — | — | `#62` Apesar da proximidade do novo governo com os grandes fazendeiros, não houve indenização oficial aos ex-proprietários de escravos. |
| [[38]](https://anpuh.org.br/uploads/anais-simposios/pdf/2019-01/1548772007_1e0263eca733383e79934480401fc831.pdf) | #63 | — | — | `#63` especialmente aqueles que ele denominava "republicanos de 14 de maio", numa alusão à mudança de atitude de alguns proprietários em relação à monarquia. Patrocí… |
| [[40]](https://www.maxwell.vrac.puc-rio.br/6401/6401_4.PDF) | #65 | — | — | `#65` dos acontecimentos que envolveram a conferência de Silva Jardim na Sociedade Francesa de Ginástica no dia 30 de dezembro de 1888 |
| [[41]](https://www.migalhas.com.br/quentes/100434/pretensao-de-incinerar-processos-arquivados-ja-foi-enfrentada-pelo-stj) | #67 | — | — | `#67` Finalmente, em 13 de maio de 1891, na gestão de Tristão Alencar Araripe, sucessor de Rui Barbosa na pasta da Fazenda, todos os documentos foram incinerados. |
| [[43]](https://www2.ufjf.br/arquivocentral/?p=10421) | #72 | — | — | `#72` o episódio toma o significado de uma tentativa de esquecimento do passado escravista e a tentativa de um recomeço na história brasileira a partir do presente n… |
| [[44]](https://www.gov.br/casaruibarbosa/pt-br/centrais-de-conteudo/publicacoes/pdfs/rui-barbosa-e-a-queima-dos-arquivos-ocr.pdf) | #71 | — | — | `#71` Rui Barbosa e a queima dos arquivos FUNDAÇÃO CASA DE RUI BARBOSA 1988 |
| [[46]](https://ojs.uel.br/revistas/uel/index.php/mediacoes/article/download/9096/7647/33416) | #77 | — | — | `#77` No Estado de São Paulo, essa situação era particulannente complexa devido à intensa imigração européia que rapidamente tornou-se mão-de-obra preferencial. |
| [[47]](https://anais-siiepe.ufpel.edu.br/2022/CH_06026.pdf) | #79 | — | — | `#79` O Código Penal de 1890 comportou o mecanismo de perseguição às camadas populares, em sua grande maioria pretos e pardos libertos. |
| [[50]](https://trt15.jus.br/noticia/2022/abolicao-o-protagonismo-dos-escravizados-em-uma-luta-que-ainda-nao-terminou) | #85 | — | — | `#85` pesquisas apontam que são negros 82% das pessoas atualmente resgatadas de trabalho análogo à escravidão |
| [[51]](https://static.even3.com/anais/1369885.pdf) | #74 | — | — | `#74` beneficiou elites agrárias e imigrantes europeus que foram subsidiados pelo Estado |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Mortas (HTTP 404)

- https://www.conjur.com.br/?p=352983 — Referencia nao encontrada (404): https://www.conjur.com.br/?p=352983
- https://companhiadasletras.com.br/sala_professor/pdfs/CadernoAtividades_BrasilUmaBiografia_cap12.pdf — Referencia nao encontrada (404): https://companhiadasletras.com.br/sala_professor/pdfs/CadernoAtividades_BrasilUmaBiografia_cap12.pdf

### Bloqueadas por barreira de acesso

- https://doaj.org/article/0e1d0967ed73404387fb60208ca04c55 — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `escravidao_brasil_3d6417564a65_20261024T230717Z-0`** [1]
  - Trecho: Para dimensionar o problema: a Lei nº 3.353 encerrou formalmente 388 anos de tráfico e escravidão, num período em que se estima que cerca de 5 milhões de pessoas foram trazidas à força para o território brasileiro.
  - Justificativa: A evidência confirma todos os elementos essenciais da afirmação: a Lei nº 3.353 decretou o fim da escravidão após 388 anos de tráfico e escravidão, e estima-se que 5 milhões de pessoas foram trazidas forçadamente ao ter…
  - Suporte veio de: [1]
  - Evidência: “Lei nº 3.353 de 13 de maio de 1888 decretou o fim da escravidão no Brasil. Após 388 anos de tráfico e escravidão foi proibido o trabalho forçado, compulsório, desumanização e maus tratos de negros e negras no Brasil.”
- **Trecho citado `escravidao_brasil_3d6417564a65_20261024T230717Z-1`** [2]
  - Trecho: As estimativas baseadas em bancos de dados especializados indicam que cerca de 4,8 milhões de africanos sobreviveram à travessia, e que o Brasil recebeu em torno de 45% de todos os africanos escravizados levados às Amér…
  - Justificativa: A evidência confirma explicitamente que 4,8 milhões de pessoas sobreviveram à travessia e que o Brasil recebeu cerca de 45% dos africanos escravizados nas Américas. A menção a 'bancos de dados especializados' não está l…
  - Suporte veio de: [2]
  - Evidência: “Desse total, 4,8 milhões de pessoas sobreviveram à travessia.”
  - Não coberto pela evidência: A expressão 'estimativas baseadas em bancos de dados especializados' não é explicitamente confirmada; a evidência menciona 'estatísticas mais recentes'.
- **Trecho citado `escravidao_brasil_3d6417564a65_20261024T230717Z-2`** [1]
  - Trecho: Foi também o último país do continente americano a abolir a escravidão.
  - Justificativa: A evidência afirma explicitamente que o Brasil foi o último país do continente americano a abolir a escravidão, sustentando diretamente a afirmação.
  - Suporte veio de: [1]
  - Evidência: “O Brasil foi o último país do continente americano a abolir a escravidão.”
### UNSUPPORTED

- **Trecho citado `escravidao_brasil_3d6417564a65_20261024T230717Z-57`** [3]
  - Trecho: Comparado aos 1,5 milhão registrados em 1872, esse número evidencia o quanto a escravidão já havia encolhido sob o efeito combinado das alforrias, das leis graduais, das abolições provinciais, das mortes e das fugas.
  - Justificativa: A evidência confirma os 1,5 milhão de escravizados em 1872 e menciona leis vigentes (Eusébio de Queiroz e Ventre Livre) e a expectativa de desaparecimento gradual da escravidão. Contudo, a afirmação lista causas específ…
  - Suporte veio de: [3]
  - Evidência: “Pela contagem feita no Segundo Reinado, havia no território nacional 1,5 milhão de escravizados (15% dos habitantes), entre africanos e brasileiros.”
  - Não coberto pela evidência: alforrias como causa do encolhimento; leis graduais como causa (a evidência menciona leis Eusébio de Queiroz e Ventre Livre, mas não as classifica como 'leis graduais' causadoras do encolhimento); abolições provinciais como causa
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_3d6417564a65_20261024T230717Z-86`** [1]
  - Trecho: A lei extinguiu o cativeiro, mas os libertos continuaram marginalizados e expostos ao racismo e à violência.
  - Justificativa: A evidência confirma que a lei extinguiu a escravidão e que não ofereceu melhores condições de vida ou políticas sociais aos libertos, sustentando a ideia de marginalização. Contudo, a afirmação específica de que os lib…
  - Suporte veio de: [1]
  - Não coberto pela evidência: libertos continuaram expostos ao racismo; libertos continuaram expostos à violência
  - Verificação: UNSUPPORTED (não confirmado); afirmação corroborada por outra fonte não citada: [47] [45] [46] [4] [30] [17] [35] [26] [12] [13] [24] (provável citação trocada) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 3 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 2 citam referência não baixada/inacessível.

- `escravidao_brasil_3d6417564a65_20261024T230717Z-29` — Referencia(s) citada(s) ['20be8c1b93e2c520'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_3d6417564a65_20261024T230717Z-30` — Referencia(s) citada(s) ['20be8c1b93e2c520'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_3d6417564a65_20261024T230717Z-60` — Referencia(s) citada(s) ['1a345b938b0f0ec7'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_3d6417564a65_20261024T230717Z-61` — Referencia(s) citada(s) ['1a345b938b0f0ec7'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_3d6417564a65_20261024T230717Z-80` — Referencia(s) citada(s) ['f92beb5dc1efe601'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.