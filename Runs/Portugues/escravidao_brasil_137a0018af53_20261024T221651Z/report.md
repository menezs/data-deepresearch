# Relatório de Auditoria — ChatGPT (escravidao_brasil_137a0018af53_20261024T221651Z)

**Arquivo auditado:** `answers/ChatGPT/Consolidado/escravidao_brasil.md`

---

## 1. Metadados da Execução

| Campo | Valor |
|---|---|
| **Run ID** | escravidao_brasil_137a0018af53_20261024T221651Z |
| **Ferramenta** | ChatGPT |
| **Gerado em** | 2026-11-18T10:36:35.676707+00:00 |
| **Total de trechos citados** | 151 |
| **Tempo de processamento** | 10:04:24:55 |
| **Modelo do juiz LLM** | z-ai/glm-5.2 |
| **Provider do juiz LLM** | openai |
| **Temperature** | 0.0 |
| **Max retries** | 3 |
| **Retry delay** | 2.0s |
| **Base URL** | https://openrouter.ai/api/v1 |

**Arquivo de origem**

| Campo | Valor |
|---|---|
| Formato / tamanho | .md · 40.6 KB |
| Título / Autor | — (ausente) / — (ausente) |
| Citações no corpo | 229 marcadores, 29 distintos |
| Referências listadas | 29 (0 nunca citadas) |

---

## 2. Distribuição de Vereditos

| Veredito | Trechos citados | Percentual |
|---|---|---|
| **SUPPORTED** | 75 | 49.7% |
| **UNSUPPORTED** | 41 | 27.2% |
| **CONTRADICTED** | 0 | 0.0% |
| **SKIPPED** | 35 | 23.2% |
| **TOTAL** | 151 | 100.0% |

Sobre os 116 trechos citados auditados: SUPPORTED 64,65%, UNSUPPORTED 35,34%, CONTRADICTED 0,00%.

> **38 dos 75 SUPPORTED são parciais.** A fonte citada sustenta a afirmação, mas o juiz apontou ao menos um aspecto dela que a evidência não cobre (ex.: o número confere, a data não). Esses 38 estão **contados dentro** dos 75 — o framework não tem uma classe `PARTIAL`. O aspecto não coberto de cada um aparece na seção *Exemplos por Veredito*.

---

## 3. Verificação de UNSUPPORTED

`54` trechos citados tiveram veredito **UNSUPPORTED** no julgamento inicial.

- `19` **confirmados** — sobreviveram à varredura do documento citado inteiro (Etapa B).
- `13` **reclassificados** pela cascata para SUPPORTED/CONTRADICTED.
- `2` **provável erro de citação** — não sustentados pela fonte citada, mas corroborados por outra referência baixada (Etapa C).

Reclassificações por etapa: context_expansion = 11, full_doc_scan = 2.

Os prováveis erros de citação estão detalhados na seção seguinte.

---

## 4. Prováveis Erros de Citação

Trechos citados com veredito **UNSUPPORTED** — a **fonte citada não os sustenta** — mas cuja afirmação **foi encontrada em outra referência já baixada** durante a checagem no corpus inteiro (Etapa C). A Etapa C **nunca** reclassifica para SUPPORTED (a auditoria é sobre a fonte citada), então o veredito continua UNSUPPORTED; o cenário mais provável, porém, é **citação trocada** — o fato é real, a fonte apontada é que está errada. `⚠` marca quando outra fonte **contradiz** o trecho.

| Trecho | Cita | Corroborado por | Contradito por |
|---|---|---|---|
| `#33` A Lei nº 3.270, de 28 de setembro de 1885, conhecida como Lei dos Sexagenários ou Saraiva-Cotegipe, representou outro c… | [4] | [13] [7] [12] [2] [3] | — |
| `#56` A historiografia do pós-1970 transformou justamente esse tipo de evidência — processos, cartas, pedidos de alforria, re… | [7] [11] | [12] | — |

---

## 5. Custo e Uso de Tokens

> ⚠️ **Custo não contabilizado** — o provider `openai` (modelo `z-ai/glm-5.2`) não tem tabela de preços neste framework. Os valores abaixo somam apenas chamadas com preço conhecido (Anthropic) ou custo local zero, e devem ser lidos como um piso, não como o custo real da execução.

| Métrica | Valor |
|---|---|
| **Custo total estimado** | US$ 0.0000 |
| **Total de tokens** | 2788073 |
| **Média de tokens por requisição** | 24035.1 |
| **Média de custo por requisição** | US$ 0.0000 |

---

## 6. Análise por Referência

- Referências sem nenhuma citação: 0/29 (0.0%)
- Referências citadas mas que nunca sustentaram (nem parcialmente) nenhum trecho citado: 3.

> **Citada** = quantos trechos citados citam a fonte. As colunas seguintes abrem esse total e **somam Citada**: **Sustenta / Parcial** (a fonte sustenta a afirmação inteira / em parte); **Não sustenta †** (a fonte foi verificada e não trata a afirmação, a contradiz, ou o juiz não a detalhou); **Não auditada** (o trecho que a cita foi pulado, ou a fonte não pôde ser baixada — não houve verificação).

| Referência | Status | Citada | Sustenta | Parcial | Não sustenta † | Não auditada |
|---|---|---|---|---|---|---|
| [[7]](https://www.scielo.br/j/nec/a/CrVbxyNKtm7vCZWxXgRz6qg/?lang=pt) | downloaded | 66 | 39 | 12 | 7 | 8 |
| [[6]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html) | downloaded | 25 | 10 | 4 | 9 | 2 |
| [[25]](https://books.google.com/books?q=Sidney+Chalhoub+Vis%C3%B5es+da+liberdade) | inaccessible | 15 | 0 | 0 | 0 | 15 |
| [[26]](https://books.google.com/books?q=Hebe+Mattos+Das+cores+do+sil%C3%AAncio) | inaccessible | 14 | 0 | 0 | 0 | 14 |
| [[12]](https://www.scielo.br/j/alm/a/YXWgYBgsydBMjtMfWY3bdTK/?lang=pt) | downloaded | 13 | 1 | 3 | 4 | 5 |
| [[14]](https://www.ibge.gov.br/estatisticas/sociais/populacao/25844-desigualdades-sociais-por-cor-ou-raca.html) | downloaded | 11 | 1 | 1 | 9 | 0 |
| [[5]](https://www.planalto.gov.br/ccivil_03/leis/l0601-1850.htm) | downloaded | 8 | 2 | 2 | 2 | 2 |
| [[8]](https://www2.senado.leg.br/bdsf/handle/id/1063) | blocked | 8 | 0 | 0 | 0 | 8 |
| [[15]](https://www.ipea.gov.br/portal/retrato/indicadores/renda-pobreza-e-desigualdade/apresentacao) | downloaded | 7 | 1 | 2 | 4 | 0 |
| [[16]](https://inclua.ipea.gov.br/igualdade-racial/) | downloaded | 7 | 0 | 2 | 5 | 0 |
| [[1]](https://www.planalto.gov.br/ccivil_03/leis/lim/LIM581.htm) | downloaded | 6 | 1 | 1 | 1 | 3 |
| [[17]](https://www.gov.br/mec/pt-br/lei-de-cotas) | downloaded | 6 | 0 | 3 | 3 | 0 |
| [[20]](https://www2.senado.leg.br/bdsf/item/id/243294) | blocked | 6 | 0 | 0 | 0 | 6 |
| [[2]](https://www.planalto.gov.br/ccivil_03/leis/lim/lim2040.htm) | downloaded | 5 | 4 | 0 | 1 | 0 |
| [[4]](https://www.planalto.gov.br/ccivil_03/leis/lim/LIM3270.htm) | downloaded | 5 | 3 | 1 | 1 | 0 |
| [[11]](https://fpabramo.org.br/livro/cenas-da-abolicao-escravos-e-senhores-no-parlamento-e-na-justica/) | downloaded | 5 | 1 | 2 | 1 | 1 |
| [[18]](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.639.htm) | downloaded | 4 | 1 | 3 | 0 | 0 |
| [[3]](https://www2.camara.leg.br/legin/fed/decret/1824-1899/decreto-4835-1-dezembro-1871-552265-publicacaooriginal-69374-pe.html) | downloaded | 2 | 2 | 0 | 0 | 0 |
| [[10]](https://www.slavevoyages.org/) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[13]](https://abpnrevista.org.br/site/article/view/852) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[19]](https://atom.senado.leg.br/) | downloaded | 2 | 0 | 0 | 0 | 2 |
| [[24]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | downloaded | 2 | 0 | 0 | 2 | 0 |
| [[29]](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14723.htm) | downloaded | 2 | 0 | 2 | 0 | 0 |
| [[9]](https://brasil.un.org/pt-br/320175-onu-lança-página-em-português-sobre-escravidão-e-comércio-transatlântico-de-pessoas) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[21]](https://www.gov.br/museus/pt-br/museus-ibram/museu-da-abolicao) | downloaded | 1 | 0 | 1 | 0 | 0 |
| [[22]](https://www.cambridge.org/core/books/last-abolition/9B7356DED946BE481BE3CBE0C19D7FF6) | downloaded | 1 | 1 | 0 | 0 | 0 |
| [[23]](https://www.loc.gov/item/hlas-bi2017003171/) | blocked | 1 | 0 | 0 | 0 | 1 |
| [[27]](https://memoria.bn.gov.br/) | downloaded | 1 | 0 | 0 | 1 | 0 |
| [[28]](https://sian.an.gov.br/) | downloaded | 1 | 0 | 0 | 1 | 0 |

---

## 7. Tabela de Verificação por Fonte

Uma linha por **referência citada**: quais trechos do documento (`#N` = posição no texto) ela sustenta, sustenta só em parte, ou não sustenta. `⚡` = a fonte **contradiz** o trecho; `s/ aval.` = o juiz não avaliou aquela fonte no trecho; `pulado` = o trecho não foi auditado. O `#N` antes do trecho da fonte indica de qual trecho da resposta ele é evidência.

| Referência | Sustenta | Parcial | Não sustenta | Trecho representativo da fonte |
|---|---|---|---|---|
| [[7]](https://www.scielo.br/j/nec/a/CrVbxyNKtm7vCZWxXgRz6qg/?lang=pt) | #0–1, #9–11, #36, #45–46, #48, #54, #57–69, #72–73, #85–86, #88–89, #113–116, #119, #122–124, #134, #150 | #14, #37–38, #55–56, #70–71, #84, #117–118, #125, #137 | #6, #8, #39, #41, #87, #120, #133, #15, #52–53, #74, #76, #99–100, #149 (pulado) | `#0` A abolição da escravidão no Brasil foi fenômeno complexo. A bibliografia especializada já registrou a relevância da lógica econômica, das instituições política… |
| [[6]](https://www2.camara.leg.br/legin/fed/leimp/1824-1899/lei-3353-13-maio-1888-533138-publicacaooriginal-16269-pl.html) | #12–13, #49, #78–80, #82–83, #90, #94 | #0, #84–85, #121 | #41, #81, #93, #95, #118, #122, #132–133, #135, #77, #149 (pulado) | `#12` Art. 1º É declarada extincta desde a data d'esta Lei, a escravidão no Brazil. Art. 2º Revogam-se as disposições em contrário. |
| [[12]](https://www.scielo.br/j/alm/a/YXWgYBgsydBMjtMfWY3bdTK/?lang=pt) | #36 | #6, #8, #38 | #39–40, #102, #105, #7, #26, #96, #103–104 (pulado) | `#36` Uma explicação que dê conta da totalidade da libertação de alguns territórios, assim como de todo o processo abolicionista, precisa trabalhar com as intersecçõ… |
| [[14]](https://www.ibge.gov.br/estatisticas/sociais/populacao/25844-desigualdades-sociais-por-cor-ou-raca.html) | #16 | #132 | #107–109, #111, #120–122, #135–136 | `#16` a por cor ou raça se revela como uma importante dimensão de exame em razão dos aspectos estruturais que condicionam a sua reprodução permanente ... evidenciam… |
| [[5]](https://www.planalto.gov.br/ccivil_03/leis/l0601-1850.htm) | #27, #43 | #3, #95 | #14, #121, #28–29 (pulado) | `#27` LEI Nº 601, DE 18 DE SETEMBRO DE 1850. Dispõe sobre as terras devolutas do Império. Art. 1º Ficam prohibidas as acquisições de terras devolutas por outro titul… |
| [[15]](https://www.ipea.gov.br/portal/retrato/indicadores/renda-pobreza-e-desigualdade/apresentacao) | #110 | #17, #132 | #107–108, #111, #136 | `#110` Em 2022, a renda das pessoas brancas era em média 87% maior que a renda das pessoas negras. |
| [[16]](https://inclua.ipea.gov.br/igualdade-racial/) | — | #112, #129 | #111, #126, #131, #135–136 | `#112` As desigualdades raciais são reproduzidas na execução de políticas públicas |
| [[1]](https://www.planalto.gov.br/ccivil_03/leis/lim/LIM581.htm) | #42 | #24 | #41, #2, #23, #25 (pulado) | `#42` LEI Nº 581, DE 4 DE SETEMBRO DE 1850. Estabelece medidas para a repressão do trafico de africanos neste Imperio. Eusebio de Queiroz Coitinho Mattoso Camara. |
| [[17]](https://www.gov.br/mec/pt-br/lei-de-cotas) | — | #18, #126, #128 | #129, #131, #136 | `#18` A Lei de Cotas, sancionada em 2012, é fruto da luta dos movimentos negros e de outros movimentos sociais pelo acesso ao ensino superior. |
| [[2]](https://www.planalto.gov.br/ccivil_03/leis/lim/lim2040.htm) | #4, #30–31, #44 | — | #41 | `#4` Declara de condição livre os filhos de mulher escrava que nascerem desde a data desta lei... Art. 1º Os filhos de mulher escrava que nascerem no Imperio desde… |
| [[4]](https://www.planalto.gov.br/ccivil_03/leis/lim/LIM3270.htm) | #5, #34, #47 | #33 | #41 | `#5` São libertos os escravos de 60 annos de idade, completos antes e depois da data em que entrar em execução esta Lei; ficando, porém, obrigados, a titulo de inde… |
| [[11]](https://fpabramo.org.br/livro/cenas-da-abolicao-escravos-e-senhores-no-parlamento-e-na-justica/) | #142 | #55–56 | #150, #53 (pulado) | `#142` Cenas da abolição retoma uma das questões centrais da história do Brasil, a abolição da escravatura, abordando o tema a partir dos debates parlamentares e das… |
| [[18]](https://www.planalto.gov.br/ccivil_03/leis/2003/l10.639.htm) | #127 | #18, #126, #131 | — | `#127` LEI Nº 10.639, DE 9 DE JANEIRO DE 2003. [...] Art. 26-A. Nos estabelecimentos de ensino fundamental e médio, oficiais e particulares, torna-se obrigatório o en… |
| [[3]](https://www2.camara.leg.br/legin/fed/decret/1824-1899/decreto-4835-1-dezembro-1871-552265-publicacaooriginal-69374-pe.html) | #4, #32 | — | — | `#4` Approva o Regulamento para a matricula especial dos escravos e dos filhos livres de mulher escrava... Art. 8º O Governo mandará proceder á matricula especial d… |
| [[10]](https://www.slavevoyages.org/) | — | #20, #144 | — | `#20` This database contains information on more than 37,000 maritime voyages trafficking enslaved people within the Americas between 1550 and 1887. [...] This datab… |
| [[13]](https://abpnrevista.org.br/site/article/view/852) | — | #5, #35 | — | `#5` O contexto marcado pela colonialidade, pelo gradualismo e pelo próprio diploma legal, reproduziram condições de precariedade para a população negra. |
| [[24]](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) | — | — | #130–131 | — |
| [[29]](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14723.htm) | — | #18, #128 | — | `#18` Altera a Lei nº 12.711, de 29 de agosto de 2012, para dispor sobre o programa especial para o acesso às instituições federais de educação superior e de ensino… |
| [[9]](https://brasil.un.org/pt-br/320175-onu-lança-página-em-português-sobre-escravidão-e-comércio-transatlântico-de-pessoas) | #19 | — | — | `#19` Segundo a UNESCO, cerca de 12,5 milhões de africanos e africanas foram deportados à força por meio do comércio transatlântico de pessoas escravizadas entre os… |
| [[21]](https://www.gov.br/museus/pt-br/museus-ibram/museu-da-abolicao) | — | #148 | — | `#148` O Museu da Abolição foi inaugurado em 13 de maio de 1983. Sua primeira exposição foi "O Processo Abolicionista Através dos Textos Oficiais", composta, em grand… |
| [[22]](https://www.cambridge.org/core/books/last-abolition/9B7356DED946BE481BE3CBE0C19D7FF6) | #138 | — | — | `#138` Available for the first time in an English language edition, with a new introduction |
| [[27]](https://memoria.bn.gov.br/) | — | — | #146 | — |
| [[28]](https://sian.an.gov.br/) | — | — | #147 | — |

> Detalhe de cada trecho (justificativa, aspectos não cobertos): ver *Exemplos*.

---

## 8. Referências Mortas, Inacessíveis e Bloqueadas

### Inacessíveis (403/timeout/SSL)

- https://books.google.com/books?q=Sidney+Chalhoub+Vis%C3%B5es+da+liberdade — Rate limit persistente em https://books.google.com/books?q=Sidney+Chalhoub+Vis%C3%B5es+da+liberdade
- https://books.google.com/books?q=Hebe+Mattos+Das+cores+do+sil%C3%AAncio — Rate limit persistente em https://books.google.com/books?q=Hebe+Mattos+Das+cores+do+sil%C3%AAncio

### Bloqueadas por barreira de acesso

- https://www2.senado.leg.br/bdsf/handle/id/1063 — anti_bot — barreira de acesso (anti_bot): Verificando sua conexão Estamos confirmando que este acesso é legítimo antes de liberar o conteúdo. Isso leva apenas alg
- https://www2.senado.leg.br/bdsf/item/id/243294 — anti_bot — barreira de acesso (anti_bot): Verificando sua conexão Estamos confirmando que este acesso é legítimo antes de liberar o conteúdo. Isso leva apenas alg
- https://www.loc.gov/item/hlas-bi2017003171/ — anti_bot — barreira de acesso (anti_bot): This website uses a security service to protect against malicious bots. This page is displayed while the website verifie

---

## 9. Exemplos Representativos por Veredito

### SUPPORTED

- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-0`** [6] [7]
  - Trecho: A abolição legal da escravidão no Brasil, consumada pela Lei nº 3.353 de 13 de maio de 1888, foi o desfecho de um processo longo, conflitivo e não linear, no qual se combinaram transformações econômicas, pressão interna…
  - Justificativa: A evidência cobre todos os elementos essenciais da afirmação: a Lei nº 3.353 de 13/05/1888 está explicitamente citada; o caráter complexo, conflitivo e não linear do processo é amplamente descrito; e cada fator listado…
  - Suporte veio de: [7] [6]
  - Evidência: “LEI Nº 3.353, DE 13 DE MAIO DE 1888 — Declara extinta a escravidão no Brazil.”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | sustenta | A abolição da escravidão no Brasil foi fenômeno complexo. A bibliografia especializada já registrou a relevância da lóg… |
    | [6] | parcial | LEI Nº 3.353, DE 13 DE MAIO DE 1888 — Declara extinta a escravidão no Brazil. |

- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-1`** [7]
  - Trecho: A interpretação tradicional que reduzia o episódio ao gesto humanitário da princesa Isabel é insuficiente, assim como seria reducionista explicá-lo exclusivamente pelo avanço do capitalismo ou apenas pela resistência es…
  - Justificativa: A evidência sustenta a afirmação em sua parte essencial: mostra que a interpretação tradicional da princesa Isabel era 'exagerada', que três famílias interpretativas (estrutural/econômica, resistência escrava, instituiç…
  - Suporte veio de: [7]
  - Evidência: “A aura de "Redentora" era, de fato, exagerada; contudo, o deslocamento de relevância da herdeira do trono imperial para o líder de revolta escrava solapou um fenômeno que não é uma coisa nem outra: o movimento social pe…”
  - Não coberto pela evidência: O termo 'conflitos raciais' não aparece explicitamente na evidência como categoria analítica; A afirmação de que 'a historiografia contemporânea tende a enfatizar' a interação é parcialmente sustentada: a evidência mostra que a fragmentação predomina, com poucas exceções propondo integração
- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-4`** [2] [3]
  - Trecho: A Lei do Ventre Livre, de 1871, declarou livres os filhos de mulheres escravizadas nascidos desde sua promulgação, mas manteve mecanismos que preservavam por muitos anos o controle senhorial sobre essas crianças; a regu…
  - Justificativa: A Lei nº 2.040/1871 declara livres os filhos de mulher escrava nascidos desde sua data (Art. 1º), mas o § 1º mantém os menores sob autoridade senhorial até os 8 anos e permite ao senhor utilizar seus serviços até os 21…
  - Suporte veio de: [2] [3]
  - Evidência: “Declara de condição livre os filhos de mulher escrava que nascerem desde a data desta lei”
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [2] | sustenta | Declara de condição livre os filhos de mulher escrava que nascerem desde a data desta lei... Art. 1º Os filhos de mulhe… |
    | [3] | sustenta | Approva o Regulamento para a matricula especial dos escravos e dos filhos livres de mulher escrava... Art. 8º O Governo… |

### UNSUPPORTED

- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-3`** [5]
  - Trecho: No mesmo ano, a Lei de Terras determinou, como regra, a compra como via de aquisição das terras públicas devolutas, criando um regime fundiário que, embora não mencionasse raça, teria profunda importância para compreend…
  - Justificativa: A evidência sustenta que a Lei de Terras (Lei nº 601 de 1850) determinou a compra como regra de aquisição de terras devolutas (Art. 1º) e que o texto não menciona raça. Contudo, a parte interpretativa da afirmacao — sob…
  - Suporte veio de: [5]
  - Evidência: “Art. 1º Ficam prohibidas as acquisições de terras devolutas por outro titulo que não seja o de compra.”
  - Não coberto pela evidência: profunda importância para compreender as dificuldades posteriores de acesso à propriedade por trabalhadores pobres, libertos e seus descendentes; embora não mencionasse raça (inferência interpretativa sobre o impacto racial, não explicitada na evidência)
  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-6`** [7] [12]
  - Trecho: Na economia, a expansão cafeeira do Sudeste tornou a questão do trabalho particularmente decisiva, enquanto o açúcar permaneceu importante no Nordeste e economias pecuárias regionais combinaram de maneiras distintas tra…
  - Justificativa: A evidência menciona a expansão cafeeira no Sudeste e a economia açucareira no Norte/Nordeste, mas não sustenta que o açúcar 'permaneceu importante' (na verdade, indica declínio de sua relevância). Mais criticamente, a…
  - Suporte veio de: [12] [7]
  - Evidência: “o abolicionismo seria fenômeno do Norte, onde a relevância econômica da escravidão decrescia com a economia do açúcar”
  - Não coberto pela evidência: açúcar permaneceu importante no Nordeste; economias pecuárias regionais combinaram trabalhadores escravizados, livres, agregados e dependentes; a expansão cafeeira tornou a questão do trabalho particularmente decisiva
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | ausente | — |
    | [12] | parcial | cafeicultores de Minas Gerais, Rio de Janeiro e São Paulo, necessitados de mão-de-obra para tocar a expansão de sua pro… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference
- **Trecho citado `escravidao_brasil_137a0018af53_20261024T221651Z-8`** [7] [12]
  - Trecho: Por isso, é inadequado imaginar uma substituição súbita, em 1888, de “escravidão” por “trabalho assalariado”; a transformação do mercado de trabalho atravessou décadas e variou significativamente entre regiões.
  - Justificativa: A evidência não aborda explicitamente a substituição de 'escravidão' por 'trabalho assalariado' nem a transformação do 'mercado de trabalho' como processo de décadas com variação regional significativa. A evidência menc…
  - Suporte veio de: [7] [12]
  - Não coberto pela evidência: substituição súbita em 1888 de 'escravidão' por 'trabalho assalariado'; transformação do mercado de trabalho atravessou décadas; variação significativa entre regiões do mercado de trabalho
  - Verificação por fonte:

    | Fonte | Relação | Trecho |
    |---|---|---|
    | [7] | ausente | — |
    | [12] | parcial | desfizeram-se paulatinamente de seus cativos, vendendo-os para os cafeicultores de Minas Gerais, Rio de Janeiro e São P… |

  - Verificação: UNSUPPORTED (não confirmado) — cascata: baseline → context_expansion → full_doc_scan → cross_reference

---

## 10. Trechos Citados Não Auditados

Motivos: 20 citam várias fontes e parte das fontes citadas está sem conteúdo (ou o `[N]` não existe na lista); 2 citam só referências bloqueadas por barreira de acesso (anti-bot, erro HTTP, login); 13 citam referência não baixada/inacessível.

- `escravidao_brasil_137a0018af53_20261024T221651Z-21` — Referencia(s) citada(s) ['154a9a85ad6e3ef9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-22` — Referencia(s) citada(s) ['154a9a85ad6e3ef9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-50` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-51` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-75` — Referencia(s) citada(s) ['54fa02b8faeef94a'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_137a0018af53_20261024T221651Z-91` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-92` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-97` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-98` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-101` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-106` — Referencia(s) citada(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-139` — Referencia(s) citada(s) ['696cde84ce565eeb'] bloqueada(s) por barreira de acesso (anti-bot, erro HTTP, login) — sem conteudo para auditar.
- `escravidao_brasil_137a0018af53_20261024T221651Z-140` — Referencia(s) citada(s) ['f70a486cae35c55e'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-141` — Referencia(s) citada(s) ['4a896d0f9c2cf752'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-143` — Referencia(s) citada(s) ['154a9a85ad6e3ef9'] nao possui(em) conteudo indexado (nao baixada(s)/inacessivel(is)).
- `escravidao_brasil_137a0018af53_20261024T221651Z-2` — Parte das fontes citadas sem conteudo: referencia(s) ['154a9a85ad6e3ef9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-7` — Parte das fontes citadas sem conteudo: referencia(s) ['154a9a85ad6e3ef9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-15` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e', '4a896d0f9c2cf752'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-23` — Parte das fontes citadas sem conteudo: referencia(s) ['154a9a85ad6e3ef9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-25` — Parte das fontes citadas sem conteudo: referencia(s) ['154a9a85ad6e3ef9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-26` — Parte das fontes citadas sem conteudo: referencia(s) ['154a9a85ad6e3ef9'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-28` — Parte das fontes citadas sem conteudo: referencia(s) ['4a896d0f9c2cf752'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-29` — Parte das fontes citadas sem conteudo: referencia(s) ['4a896d0f9c2cf752'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-52` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-53` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-74` — Parte das fontes citadas sem conteudo: referencia(s) ['54fa02b8faeef94a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-76` — Parte das fontes citadas sem conteudo: referencia(s) ['54fa02b8faeef94a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-77` — Parte das fontes citadas sem conteudo: referencia(s) ['54fa02b8faeef94a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-96` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-99` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-100` — Parte das fontes citadas sem conteudo: referencia(s) ['f70a486cae35c55e'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-103` — Parte das fontes citadas sem conteudo: referencia(s) ['4a896d0f9c2cf752'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-104` — Parte das fontes citadas sem conteudo: referencia(s) ['4a896d0f9c2cf752'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-145` — Parte das fontes citadas sem conteudo: referencia(s) ['54fa02b8faeef94a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.
- `escravidao_brasil_137a0018af53_20261024T221651Z-149` — Parte das fontes citadas sem conteudo: referencia(s) ['54fa02b8faeef94a'] sem conteudo baixado/indexado — o trecho citado nao e julgado so com o restante das fontes.