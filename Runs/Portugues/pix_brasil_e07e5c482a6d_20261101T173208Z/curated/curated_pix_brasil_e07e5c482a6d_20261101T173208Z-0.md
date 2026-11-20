[referencia=f42eb0724c750e7c score=0.942]
# **<u>Pix: o novo meio de pagamento brasileiro</u>** 

Em 16 de novembro de 2020, os cidadãos, empresas e entes governamentais brasileiros passaram a ter o Pix como uma nova alternativa para realizar seus pagamentos e transferências. O Pix é um arranjo de pagamentos, instituído pelo Banco Central do Brasil (BCB), que disciplina a prestação de serviços de pagamento relacionados a transações de pagamentos instantâneos. Ou seja, o Pix vem se somar ao dinheiro em espécie, ao cheque, à Transferência Eletrônica Disponível (TED), ao DOC, ao boleto e aos cartões de crédito, de débito e pré-pagos, para compor a cesta de meios de pagamento disponíveis para a população brasileira. 

O Pix é um meio de pagamento que permite a transferência de recursos de uma conta transacional (conta de depósito à vista, conta de poupança ou conta de pagamento pré-paga) para outra conta transacional, entre diferentes instituições. Ele possui oito características que o tornam único: 

a) velocidade de disponibilização dos recursos na conta do recebedor: os recursos são creditados em até 10 segundos em 99% das transações e em até 6 segundos em 50%; b) disponibilidade: o Pix pode ser feito 24 horas por dia, em todos os dias do ano, incluindo sábados, domingos e feriados; 

c) multiplicidade de casos de uso: o Pix atende a todo e qualquer pagamento ou transferência feito hoje no Brasil, incluindo transferências entre pessoas, compra de bens e serviços em estabelecimentos físicos e no comércio eletrônico, transferências entre empresas, quitação de faturas e de cobranças, incluindo aquelas referentes a serviços públicos, e pagamentos envolvendo entes governamentais, tanto para fins de cumprimento de suas obrigações quanto para fins de arrecadação de taxas e impostos;<sup>1</sup>

---

[referencia=07b6c5b87f609090 score=0.818]
Download OpenAPI specification:

O Diretório de Identificadores de Contas Transacionais - DICT - é o serviço do arranjo Pix que permite buscar detalhes de contas transacionais com chaves de endereçamento mais convenientes para quem faz um pagamento. Entre os tipos de chave atualmente disponíveis estão CPF, CNPJ, telefone, e-mail e EVP. As informações retornadas pelo DICT permitem ao pagador confirmar a identidade do recebedor, proporcionando uma experiência mais fácil e segura. Permitem também ao PSP do pagador criar a mensagem de instrução de pagamento a ser enviada para o sistema de liquidação com os detalhes de conta do recebedor.

Para informações adicionais, consulte a página do Pix.

O DICT utiliza autenticação mútua TLS.

As definições de autenticação para essa API estão especificadas no manual de segurança do Pix.

Requisições que incluam ou alterem informações no DICT devem ser assinadas com
XML Digital Signature pelo participante que envia a requisição.
Requisições de consulta não precisam ser assinadas. Respostas retornadas pelo DICT serão assinadas digitalmente.
As assinaturas **devem** ser validadas pelos clientes da API.

A assinatura será colocada no elemento `Signature` das requisições e respostas.
O `Signature` será envelopado pelo XML que está
sendo assinado (assinatura é um elemento filho).

Para mais detalhes sobre a forma de construir a assinatura, consulte o manual de segurança do Pix.

Para preservar a estabilidade do serviço, as operações da API do DICT estão sujeitas a políticas de limitação de requisições. Especificamente para a operação de consulta de vínculo, há também limitação de requisições com a finalidade de prevenir ataques de varredura de dados. O algoritmo usado para implementar as políticas de limitação é o token bucket.

---

[referencia=102d3ed3ffd0ee94 score=0.768]
## **2. Pix em Números** 

As principais estatísticas do Pix estão disponíveis na página do Pix no _site_ do BC na internet<sup>5</sup> e na página de dados abertos<sup>6</sup> . Informações diárias sobre a liquidação de transações no SPI, bem como sobre o padrão intradiário de movimentação, estão disponíveis na página de estatísticas do SPI<sup>7</sup> . A página de estatísticas de meios de pagamentos permite a comparação entre as estatísticas de uso do Pix e as estatísticas de uso dos demais meios de pagamento<sup>8</sup> . Essas estatísticas estão detalhadas na página de dados abertos<sup>9</sup> . 

A seguir, apresentam-se algumas informações do Pix, desde o seu lançamento em novembro de 2020 até dezembro de 2025.

---

[referencia=102d3ed3ffd0ee94 score=0.674]
BC participantes do Pix. Publicada em setembro de 2025, com efeitos a partir 

de março de 2026, a regra determinou que apenas instituições integrantes dos 















**Novembro** 

**Julho** 

**Novembro** 

**Setembro** 

**Outubro** 

**Dezembro** 

**Março** 

Cadastro de dispositivos para pessoas naturais 

Vedação à movimentação de transações Pix por usuários fraudadores Aumento de obrigações para instituições autorizadas e estabelecimento de cronograma para solicitação de autorização 

Compatibilidade dos dados associados às chaves Pix com a Receita Federal do Brasil 

Bloqueio cautelar para usuários Restrições para pessoa jurídica chaves Pix com marcação de fraude Limitação do valor de transações para participantes não autorizados Botão de pelo BC ou que se conectam à contestação do Pix RSFN por meio de PSTI (autoatendimento MED) Possibilidade de estabelecimento de limite de valor igual a 0 para transações iniciadas a partir de dispositivos com geolocalizador desligado 

Ferramentas auxiliares de gerenciamento e monitoramento da Conta PI para participantes diretos do SPI 

Aprimoramento das informações de segurança do DICT 

Estabelecimento de requisito mínimo de capital 

e patrimônio líquido para poder participar do Pix 

Restrição para atuar como participante responsável por IPs não autorizadas 

Maior prazo para novo pedido de adesão ao Pix por instituições excluídas por penalidade 

Possibilidade de aplicação de multa diária a instituições participantes 

14 



a instituição de relacionamento do usuário pagador efetua o pagamento do valor integral da transação instantaneamente, via Pix, para o usuário recebedor, e ela vai receber as parcelas do usuário pagador posteriormente. Essa instituição define as condições para oferecer o crédito (como a taxa de juros), considerando seus procedimentos de gerenciamento de riscos e o perfil de risco de seus clientes.

---

[referencia=102d3ed3ffd0ee94 score=0.638]
foi ampliado o conjunto de estatísticas de fraudes retornado pelo DICT aos participantes, trazendo maior riqueza de informações, de forma a robustecer os mecanismos antifraudes dos participantes. 

Limitação do valor de transações: desde setembro de 2025, instituições participantes do Pix não autorizadas a funcionar pelo BC, ou que se conectam à Rede do Sistema Financeiro Nacional (RSFN) por intermédio de um Provedor de Serviços de Tecnologia da Informação (PSTI), passaram a ter um limite de transação Pix no valor de R$15.000,00. Transações com valores acima desse montante são rejeitadas automaticamente pelo Sistema de Pagamentos Instantâneos (SPI), sistema centralizado de liquidação do Pix operado pelo BC. 

- 

- Restrição de retorno de dados de chaves Pix associadas a marcações de fraude no DICT: desde outubro de 2025, o DICT passou a não retornar os dados de chave Pix na iniciação das transações quando a chave consultada ou o seu titular estiverem associados a marcação de fraude realizada pelo participante recebedor da transação. Ou seja, caso o usuário tenha se envolvido em uma fraude naquela instituição recebedora da transação, o DICT não disponibilizará os dados da chave, impedindo que novas transações possam ser realizadas para as chaves daquele usuário naquela instituição. 

- Monitoramento da conta Pagamentos Instantâneos (Conta PI) pelos participantes: em dezembro de 2025, o BC disponibilizou para os participantes diretos do SPI ferramentas auxiliares de gerenciamento e de monitoramento da Conta PI. Essas ferramentas incluem o envio de comunicações automáticas aos participantes diretos em situações de risco, como o atingimento de saldo mínimo ou movimentações atípicas ocorridas na Conta PI, bem como a possibilidade de comando de bloqueios e de desbloqueios manuais da conta. Essas medidas contribuem para que os participantes possam agir de forma rápida e autônoma em situações de risco.

---

[referencia=102d3ed3ffd0ee94 score=0.528]
5 





<!-- Start of picture text -->
INFOGRÁFICO 1<br>Linha do tempo desde a criação do Pix<br>2020 2021<br>Mais produtos<br>Lançamento  • 16/nov<br>e segurança<br>•<br>Pix Saque e Pix Troco<br>•<br>Bloqueio cautelar<br>•<br>Mecanismo Especial de Devolução (MED)<br>•<br>Open Finance: iniciação de pagamento via Pix<br>2023 2022<br>Sinergia para Tecnologia a favor<br>gerar impacto do cidadão<br>• •<br>Maior integração com  Limites noturnos para maior segurança<br>Open Finance • QR code  dinâmico com mais funcionalidades<br>2024 2025<br>Experiência  Usuário em<br>simplificada primeiro lugar<br>• Jornada sem redirecionamento  • Pix por aproximação<br>(Pix + Open Finance) • Pix Automático<br>• •<br>Pix Agendado Autoatendimento do MED<br><!-- End of picture text -->



<!-- Start of picture text -->
PREMIAÇÕES DO PIX 2023-2025<br><!-- End of picture text -->



<!-- Start of picture text -->
Academia iBest Brasil:<br>melhor iniciativa do Brasil em ações<br>digitais do governo, segundo votação do<br>júri de especialistas da Academia e<br>também segundo o júri popular nos três<br>anos consecutivos.<br><!-- End of picture text -->



<!-- Start of picture text -->
2023, 2024 e 2025<br>júri de especialistas da Academia e<br>Prêmio iBest<br>também segundo o júri popular nos três<br>GOVERNO anos consecutivos.<br>2023<br>Bravo Beacon O Banco Central foi premiado pelo<br>desenvolvimento do Pix, destacando<br>of Innovation<br>o sistema como um avanço na<br>Council of the Americas inclusão financeira.<br>2025<br>Vencedor em 2025 na categoria<br>World Summit<br>Negócios e Comércio e na categoria<br>Awards Brasil Acessibilidade Digital.<br><!-- End of picture text -->

6

---

[referencia=f42eb0724c750e7c score=0.511]
**Gráfico 3 – Pix e outros instrumentos** 



<!-- Start of picture text -->
R$ milhões<br>450<br>400<br>350<br>300<br>250<br>200<br>150<br>100<br>50<br>0<br>Nov Dez Jan Fev Mar<br>2020 2021<br> Pix  Boleto  Cheque  DOC  TED<br><!-- End of picture text -->

O elevado uso do Pix fica ainda mais evidente quando a sua taxa de adoção, definida como a quantidade de transações por habitante do país, é comparada com a de arranjos de pagamentos instantâneos em outros países. Em seu primeiro ano de adoção, considerando apenas cinco meses de dados, o Pix é o segundo arranjo de pagamentos instantâneos com adoção mais rápida entre os países identificados (Gráfico 4). Tendo em vista a taxa de crescimento mensal do uso do Pix, espera-se que a taxa de adoção do Pix seja a maior já identificada, quando os dados completos do primeiro ano após a implementação estiverem disponíveis. 

2020  | Relatório de Economia Bancária | 4 



<!-- Start of picture text -->
Gráfico 4 – Taxa de adoção de arranjos de<br>pagamento instantâneo em diversos países<br>(quantidade de transações  per capita )<br>50,0<br>40,0<br>30,0<br>20,0<br>10,0<br>0,0<br>0 1 2 3 4 5 6 7 8 9 10 11<br>Anos após a implementação<br> Nigéria  Austrália  Chile<br> Dinamarca  México  Índia<br> Singapura  Suécia  Reino Unido<br> Brasil*<br>* Dados de novembro de 2020 a março de 2021.<br>Fontes: Bech, Hancock e Zhang (2020) e BCB (dados para o Brasil)<br><!-- End of picture text -->

---

[referencia=102d3ed3ffd0ee94 score=0.482]
###### **Aprimoramentos em processos relacionados ao DICT** 

O DICT armazena as informações de nome e de CPF ou de CNPJ vinculados às chaves Pix registradas. As instituições participantes devem garantir que essas informações estejam em conformidade com as informações registradas nas bases de CPF e de CNPJ da Receita Federal do Brasil. Como uma segunda linha de defesa, o BC irá desenvolver uma solução para garantir que todas as novas chaves registradas estejam com as informações constantes nas bases 

26 



da Receita Federal do Brasil. A intenção é que chaves que não estejam em conformidade sejam bloqueadas até que as informações vinculadas às chaves sejam corrigidas. 

Outra ação prevista é o aprimoramento na tipologia de fraudes do DICT. Essa medida prevê o refinamento da taxonomia de fraudes atualmente existente, de forma a assegurar a relevância, a abrangência e o detalhamento adequado face à constante inovação de fraudes e de golpes digitais. Busca-se, dessa forma, subsidiar os mecanismos antifraude das instituições participantes com informações mais detalhadas sobre as fraudes ocorridas no âmbito do Pix, além de guiar a atuação do BC, tanto no monitoramento quanto no desenvolvimento de soluções para resolver fraudes e golpes específicos que estejam causando maiores danos à população. 

Nesse processo, o BC segue atuando como coordenador e indutor do ecossistema, promovendo inovação, competição e inclusão financeira, ao mesmo tempo em que preserva a estabilidade e a segurança do sistema de pagamentos. A evolução do Pix reflete, assim, um esforço contínuo e coletivo, orientado por objetivos públicos e pela busca permanente por soluções que ampliem a eficiência do mercado de pagamentos e gerem valor para a sociedade brasileira.

---

[referencia=102d3ed3ffd0ee94 score=0.476]
##### **2.1 Transações** 

A quantidade e o volume de transações Pix têm crescido de forma significativa desde o seu lançamento (gráficos 2.1.1 e 2.1.2). Em 2025, o número de transações aumentou 25,7% comparado com o ano anterior, chegando a quase 80 bilhões de transações, enquanto o volume financeiro das transações teve crescimento de 33,8% no mesmo período, ultrapassando R$35 trilhões. 

- _5 Ver https://www.bcb.gov.br/estabilidadefinanceira/pix-em-numeros-estatisticas._ 

- _6 Ver https://dadosabertos.bcb.gov.br/dataset/pix._ 

- _7 Ver https://www.bcb.gov.br/estabilidadefinanceira/estatisticas_spi. Os relatórios anuais do SPI apresentam informações detalhadas sobre a gestão e a operação do SPI. Esses relatórios estão disponíveis na página de publicações sobre o SPB, em https://www.bcb.gov.br/estabilidadefinanceira/ spbpublicacoes._ 

- _8 Ver https://www.bcb.gov.br/estatisticas/spbadendos?ano=2024._ 

- _9 Ver https://dadosabertos.bcb.gov.br/dataset/estatisticas-meios-pagamentos._

---

[referencia=102d3ed3ffd0ee94 score=0.461]
###### O Relatório está divido em três capítulos: 

- **_Evolução do Pix entre 2023 e 2025_** , contemplando os produtos e as funcionalidades desenvolvidos nesse período e a evolução dos mecanismos de segurança; 

- **_Pix em Números_** , trazendo dados estatísticos atualizados sobre transações, chaves, usuários e participantes; e 

- **_O Futuro do Pix_** , com informações sobre os aprimoramentos que estão sendo planejados para os próximos anos, conforme as agendas evolutiva e de segurança. 

O Relatório descreve cada nova funcionalidade do Pix, aderente com os objetivos estratégicos de um mercado de pagamentos de varejo competitivo, eficiente, seguro e inclusivo. A evolução das funcionalidades visa oferecer mais alternativas de pagamento, promover a inovação, a construção de novos modelos de negócio e a competição na prestação de serviços para a população brasileira. 

A evolução na agenda de segurança ao longo dos anos também é um dos temas centrais do Relatório. A segurança é um dos pilares do Pix desde o seu lançamento. O BC possui uma agenda permanente de aprimoramento das regras de segurança, juntamente com o Grupo Estratégico de Segurança do Pix (GE-Seg), coordenado pelo BC e composto por especialistas em segurança que atuam no sistema financeiro. 

Espera-se que este Relatório seja uma fonte rica de informações sobre os cinco anos de existência do Pix para os diversos públicos com interesse em saber mais sobre o ecossistema de pagamentos instantâneos do Brasil e sua evolução no triênio 2023-2025. 

Boa leitura! 

_1 A primeira edição do Relatório de Gestão do Pix foi publicada em 2023, contendo informações sobre o triênio 2020-2022, e pode ser acessada em: www.bcb.gov.br/content/estabilidadefinanceira/pix/relatorio_de_gestao_pix/relatorio_gestao_pix_2023.pdf._ 

5 





<!-- Start of picture text -->

---

[referencia=f42eb0724c750e7c score=0.351]
<!-- Start of picture text -->
4.289.962<br>30.355.453<br>66.876.858<br>Celular CNPJ CPF E-mail Chaves aleatórias<br><!-- End of picture text -->

Com relação às transações propriamente ditas, entre novembro de 2020 e março de 2021, já foram feitas 1,0 bilhão de transações Pix, movimentando R$787,2 bilhões (Gráfico 2).  Em termos de quantidade, 79,9% das transações ocorreram entre pessoas naturais. Essa participação cai para 44,3% em termos de valor. Transações entre pessoas jurídicas representaram 35,7% do valor total transacionado no período. Transações iniciadas por pessoas naturais e recebidas por pessoas jurídicas, que caracterizam, em geral, transações de compra, representaram 9,1% e 8,0% do total, em termos de quantidade e de valor, respectivamente. 

3 Dados atualizados sobre o Pix estão disponíveis em https://www.bcb.gov.br/estabilidadefinanceira/estatisticaspix. 

2020  | Relatório de Economia Bancária | 3 



<!-- Start of picture text -->
Gráfico 2 – Transações Pix<br>R$ bilhões milhões<br>300 450<br>400<br>250<br>350<br>200 300<br>250<br>150<br>200<br>100 150<br>100<br>50<br>50<br>0 0<br>Nov Dez Jan Fev Mar<br>2020 2021<br>Quantidade Pix Valor Pix<br><!-- End of picture text -->

Comparando com outros meios de pagamento, nota-se que o uso do Pix vem crescendo a cada mês e já é maior que o uso de TEDs e de DOCs somados (Gráfico 3). Em março, a quantidade de Pix superou a quantidade de boletos liquidados. 

**Gráfico 3 – Pix e outros instrumentos** 



<!-- Start of picture text -->

---

[referencia=102d3ed3ffd0ee94 score=0.313]
entre os participantes da cadeia de pagamentos e os agentes tributários. 

O BC acompanha e avalia os ajustes nas regras de funcionamento do Pix e na sua infraestrutura que serão necessários para viabilizar essa funcionalidade, 

_23 Disponível em Resolução BCB 505, de 25 de setembro de 2025._ 

25 



as instituições participantes fazem a cobrança das parcelas das operações de crédito contratadas e poderá atuar em relação ao tema como consequência de seu acompanhamento e monitoramento das soluções desenvolvidas pelos agentes privados. 

###### 3.1.4 Inserção internacional do Pix 

No rol de ações voltadas à ampliação dos casos de uso do Pix, o BC acompanha os diversos modelos de transações transfronteiriças que vêm sendo implementados pelos agentes privados, em parceria com instituições de outras jurisdições, que já estão viabilizando o uso do Pix por brasileiros em outros países e o uso do Pix no Brasil por não residentes a partir dos aplicativos de instituições estrangeiras. 

Além do monitoramento desses modelos, o BC avalia a interligação do Pix com sistemas de pagamentos instantâneos de outras jurisdições. Estão em discussão tanto interligações bilaterais como a participação em _hubs_ multilaterais. Essas interligações permitiriam a realização de remessas internacionais e de transações de compra com disponibilização dos recursos em moeda local em poucos segundos. A interligação de sistemas de pagamentos instantâneos tem o potencial de diminuir as tarifas, aumentar a velocidade, ampliar o acesso e melhorar a transparência de transações transfronteiriças.

---

[referencia=102d3ed3ffd0ee94 score=0.283]
##### **2.4 Participantes** 

O Pix encerrou o ano de 2025 com 926 instituições participantes, crescimento de 5,6% em relação ao ano anterior (gráfico 2.4.1). Não obstante os ganhos potenciais em concorrência e diversidade de modelos decorrentes da ampliação do número de participantes, o BC constantemente busca assegurar que tal expansão ocorra em bases sólidas, com a manutenção de participantes que atendam a elevados padrões de segurança e de qualidade na prestação de serviços. 

**Gráfico 2.4.1 – Participantes ativos** 



<!-- Start of picture text -->
950<br>926<br>900<br>877<br>850<br>806<br>795<br>800<br>769<br>742 750<br>700<br>Dez-2020 Dez-2021 Dez-2022 Dez-2023 Dez-2024 Dez-2025<br>Fonte: BC<br><!-- End of picture text -->

O segmento de instituições de pagamento (IPs) apresentou a maior participação na quantidade de transações na ótica pagadora em 2025 (50%), aumento de 3,7 pontos percentuais em relação ao ano anterior (gráfico 2.4.2). O segundo maior segmento é composto pelos bancos múltiplos, com participação de 35%, declínio de 2,1 pontos percentuais em relação a 2024. Vale destacar que em 2020, os bancos múltiplos representavam 55,8% da quantidade de transações e as instituições de pagamento, 25,5%. Essa desconcentração ao longo do tempo demonstra claramente os efeitos benéficos do aumento da competição no setor financeiro proporcionada pelo Pix.

---

[referencia=102d3ed3ffd0ee94 score=0.275]
###### **_Split_ tributário nas transações Pix** 

final. Esse modelo de negócio é, em alguns casos, utilizado por fraudadores, pois o recebedor final não é identificado, inviabilizando o uso do MED. 

Em decorrência da aprovação da reforma tributária que instituiu o chamado “ _split_ 

Como resultado esperado, a solução pode contribuir para a melhoria da 

tributário”, a agenda evolutiva do Pix passou a incorporar o desenvolvimento 

A crescente participação de intermediários nas cadeias de pagamento exige o aperfeiçoamento do arcabouço de regras, com vistas a reforçar a transparência, a rastreabilidade das operações, a visibilidade dos beneficiários finais dos 

qualidade das garantias e para a redução do custo do crédito, especialmente 

dessa medida a partir de 2025, com foco na ampliação da transparência para 

para empresas com forte uso do Pix. Dessa forma, reforça seu papel como elemento integrador entre pagamentos e outros serviços financeiros, 

os usuários pagadores quanto à composição dos valores pagos em tributos 

e na simplificação do recolhimento desses valores pelos recebedores. A 

recursos e as responsabilidades dos agentes envolvidos. Adicionalmente, modelos em que os intermediários fazem parte do fluxo financeiro da transação, retendo recursos do beneficiário final, introduzem risco de crédito desses intermediários, sem garantias de recebimento pelo beneficiário final em caso de falhas. 

ampliando seu potencial de geração de eficiência e de inovação para o SFN. 

implementação do _split_ viabilizará a retenção automática de tributos incidentes 

sobre transações elegíveis a partir da integração de informações estruturadas 

Além disso, o BC acompanha e monitora as soluções desenvolvidas pelos agentes privados para ofertar operações de crédito durante a jornada de iniciação de uma transação, permitindo que seus clientes parcelem pagamentos e transferências por meio do Pix. O BC também monitora como

---

[referencia=102d3ed3ffd0ee94 score=0.214]
**Gráfico 2.1.14 – Transações Pix iniciadas por meio da iniciação de transação de pagamento** 



<!-- Start of picture text -->
Milhões R$ bi<br>70,00 20,00<br>56,00 15,30 16,00<br>42,00 12,00<br>64,53<br>28,00 8,00<br>14,00 4,00<br>3,17<br>0,76<br>0,13 7,39<br>0,64 2,39<br>0,00 0,00<br>2022 2023 2024 2025<br>Quantidade Valor financeiro (dir.)<br>Fonte: BC<br><!-- End of picture text -->



<!-- Start of picture text -->
Milhões R$ mi<br>1,40 70,00<br>57,60<br>1,12 56,00<br>47,70<br>0,84 42,00<br>1,22<br>0,56 28,38 28,23 28,00<br>25,85<br>0,96<br>0,28 0,59 0,61 0,56 14,00<br>1,78<br>0,09 0,04<br>0,00 0,00<br>Jun-2025 Jul-2025 Ago-2025 Set-2025 Out-2025 Nov-2025 Dez-2025<br>Quantidade Valor financeiro (dir.)<br>Fonte: BC<br><!-- End of picture text -->

O uso do Pix Automático vem sendo ampliado de forma consistente. Em dezembro de 2025, foram feitas quase 600 mil transações, mais do que o dobro da quantidade registrada no mês anterior, com volume financeiro de R$133,2 milhões, cinco vezes maior do que em novembro (gráfico 2.1.16).

---

[referencia=102d3ed3ffd0ee94 score=0.210]
Com relação à participação no valor das transações, o segmento de bancos múltiplos ainda detém a maior participação em 2025 (61,3%), 0,4 pontos percentuais abaixo do ano anterior (gráfico 2.4.3). As IPs ficam em segundo lugar, com 21,3% em 2025, aumento de 0,4 pontos percentuais em comparação com o ano anterior. Houve uma mudança ao longo do tempo, considerando que em 2020 os bancos múltiplos representavam 74,5% do valor das transações Pix e as IPs 9,7%. Contudo, nos últimos dois anos, houve certa estabilização nesses dois segmentos, e começou a crescer a relevância, ainda que a taxas baixas, de outros tipos de instituição, entre elas as sociedades de crédito direto e as sociedades de crédito, financiamento e investimento<sup>19</sup> . O gráfico 2.4.4 evidencia essa diferença na participação dos principais segmentos por quantidade e por valor de transações, mostrando que as IPs tendem a atuar em maior quantidade de transações de valores mais baixos, ao contrário dos bancos incumbentes. 

**Gráfico 2.4.2 – Participação nas transações** 

Por segmento na quantidade das transações – Pagadores 



<!-- Start of picture text -->
100%<br>80%<br>60%<br>40%<br>20%<br>0%<br>Dez-2020 Dez-2021 Dez-2022 Dez-2023 Dez-2024 Dez-2025<br>Instituição de Pagamento Banco Múltiplo<br>Caixa Econômica Federal Cooperativa de Crédito<br>Sociedade de Crédito Direto Sociedade de Crédito, Financiamento e Investimento<br>Outros<br>Fonte: BC<br><!-- End of picture text -->

---

[referencia=102d3ed3ffd0ee94 score=0.157]
<!-- Start of picture text -->
Gráfico 2.1.2 – Valor das transações<br>Gráfico 2.1.2 – Valor das transações<br>R$ bi<br> 40.000<br>35.328<br> 32.000<br>26.407<br> 24.000<br>17.117<br> 16.000<br>10.891<br> 8.000<br>5.204<br>151<br> -<br>2020 2021 2022 2023 2024 2025<br>Fonte: BC<br><!-- End of picture text -->

**Você sabia?** 

Recorde de valor total de transações Pix em um único dia: **R$193.473.609.406,39** em 19 de dezembro de 2025. 

Desde o lançamento do Pix, houve uma mudança significativa na distribuição das transações do ponto de vista da sua natureza, conforme mostra o gráfico 2.1.3. Em 2020, ano de seu lançamento, o meio de pagamento era usado sobretudo para transações entre pessoas físicas ( _person to person_ – P2P), correspondendo a 85% das transações. Com o passar do tempo e com o desenvolvimento de novas funcionalidades voltadas para casos de uso específicos, a população começou a utilizar o Pix mais frequentemente para transações com pessoas jurídicas ( _person to business_ – P2B), por exemplo, para o pagamento de bens e serviços. Em 2025, 43% das transações foram de pessoas físicas para pessoas jurídicas, aumento de 4 pontos percentuais em relação ao ano anterior e de 37 pontos percentuais em relação a 2020. Esses números demonstram o processo de maturidade do Pix, que passou de um meio utilizado primordialmente para viabilizar transferências digitais entre pessoas para um meio de pagamento central para o funcionamento do varejo brasileiro. 

**Gráfico 2.1.3 – Distribuição da quantidade** 

Por natureza da transação 



<!-- Start of picture text -->

---

[referencia=f42eb0724c750e7c score=0.145]
Por causa dessas características, o BCB entende que o Pix pode trazer diversos benefícios para a população brasileira. 

Para os pagadores, o Pix é o meio eletrônico que mais se aproxima do dinheiro em espécie. Para os recebedores, é possível destacar a velocidade de disponibilização dos recursos. O Pix é o único meio eletrônico de pagamento que apresenta essa característica. Essa velocidade permite o aprimoramento da gestão de caixa de pessoas, empresas e entes governamentais, diminuindo sua necessidade de crédito. Além disso, o Pix permite ganhos de eficiência significativos nos processos internos das empresas e entes governamentais, ao facilitar a conciliação dos pagamentos e facilitar a automatização de processos e a integração de sistemas. Por fim, o Pix tende a ter um custo de aceitação menor que o dos demais meios eletrônicos. 

Para a economia brasileira, o Pix contribui para: 

- a) aumentar a eficiência do mercado via digitalização dos meios de pagamento, dada a redução relativa do uso do dinheiro em espécie, que é o meio com maior custo social; 

2020  | Relatório de Economia Bancária | 2 

b) aumentar a competição no SPB, ao permitir a entrada e a participação de diversas instituições, inclusive de instituições que não precisem de autorização do BCB para funcionar, e dar condições equânimes de competição a todas elas; 

c) aumentar a competição no próprio mercado de pagamentos de varejo, ao se constituir como um concorrente direto de outros arranjos de pagamento, notadamente os arranjos de cartão de crédito, de débito e de pré-pago; 

d) incentivar a inclusão financeira, ao disponibilizar um serviço de pagamento eletrônico barato e que pode ser ofertado por diversas instituições que atuam em nichos pouco atendidos pelas instituições tradicionais do Sistema Financeiro Nacional (SFN); e

---

[referencia=102d3ed3ffd0ee94 score=0.144]
|,<br>usuário pagador quanto do usuário recebedor.<br>A evolução dessas funcionalidades requer, de forma concomitante, o<br>fortalecimento contínuo da infraestrutura do Pix, de modo a assegurar que<br>as inovações regulatórias e operacionais sejam sustentadas por uma base<br>robusta e preparada para o crescimento do volume transacional.<br>3.1.2 Governança do ecossistema e uso responsável do Pix|pagador registre informações objetivas sobre o pagamento, esse campo tem<br>sido utilizado, em algumas situações, para fns alheios ao propósito original,<br>como veículo para mensagens ofensivas, intimidatórias ou ameaçadoras,<br>frequentemente associadas a transferências de valor irrisório.<br>Diante desse cenário, o BC instituiu, em 2026, um grupo de trabalho no<br>âmbito do Fórum Pix com a participação de associações representativas do<br>ecossistema, com o objetivo de discutir alternativas e encaminhamentos<br>voltados à preservação da integridade do instrumento e da boa experiência<br>dos usuários, sem comprometer as características essenciais do Pix. Com base<br>nas conclusões desse trabalho, o BC avaliará e instituirá, se julgar necessário, as|

---

[referencia=07b6c5b87f609090 score=0.128]
Cada página contém até 200 notificações de eventos e o cursor é retornado na resposta para a próxima página, quando houver.

A janela de eventos é de 7 dias a partir do momento da requisição.

| Participant required | string^[A-Z0-9]{8}$ ISPB do partipante direto ou indireto interessado | 
| IncludeIndirectParticipants | boolean  Default:  false Inclui adicionalmente os eventos de participantes indiretos | 
| Cursor | string Cursor | 

<ListEventNotificationsResponse>
    <Signature></Signature>
    <ResponseTime>2020-01-10T10:00:00.000Z</ResponseTime>
    <CorrelationId>a9f13566e19f5ca51329479a5bae60c5</CorrelationId>
    <HasMoreElements>true</HasMoreElements>
    <NextCursor>baARacfFF3fcxlasTRN6</NextCursor>
    <EventNotifications>
        <EventNotification>
            <Id>10000</Id>
            <Event>FUNDS_RECOVERY_ANALYSED</Event>
            <EntityType>FUNDS_RECOVERY</EntityType>
            <EntityId>91d65e98-97c0-4b0f-b577-73625da1f9fc</EntityId>
            <Timestamp>2025-01-10T10:00:00.000Z</Timestamp>
            <Participant>12345678</Participant>
        </EventNotification>
        <EventNotification>
            <Id>10001</Id>
            <Event>FUNDS_RECOVERY_COMPLETED</Event>
            <EntityType>FUNDS_RECOVERY</EntityType>
            <EntityId>91d65e98-97c0-4b0f-b577-73625da1f9fc</EntityId>
            <Timestamp>2025-01-11T10:00:00.000Z</Timestamp>
            <Participant>12345678</Participant>
        </EventNotification>
    </EventNotifications>
</ListEventNotificationsResponse>

O controle do fluxo de acesso aos serviços do DICT é realizado por meio de políticas de limitação de requisições, utilizando o algoritmo de token bucket. Para cada política de limitação, existe um balde com configurações específicas, de acordo com a seção limitação de requisições.