# Arquitetura Transformer: mecanismo de atenção e base dos LLMs

## Resumo executivo

A arquitetura Transformer, apresentada por Vaswani et al. em 2017, substituiu a recorrência e as convoluções como mecanismo central de modelagem de sequências por operações de atenção, permitindo que todos os tokens de uma sequência fossem processados em paralelo durante o treinamento e que relações entre posições distantes fossem representadas por caminhos computacionais curtos.[1] Essa mudança atacou dois problemas importantes dos modelos sequenciais anteriores: a dificuldade de paralelizar RNNs, cuja computação avança passo a passo, e a dificuldade de transmitir informação por longas distâncias sem atravessar muitos estados recorrentes ou muitas camadas convolucionais.[1][3][4]

O núcleo matemático do Transformer é a atenção por produto escalar escalado,

\[
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V,
\]

na qual cada posição transforma sua representação em uma *query* \(Q\), uma *key* \(K\) e um *value* \(V\); produtos escalares medem compatibilidades entre queries e keys, o softmax converte os escores em pesos e a soma ponderada dos values produz uma nova representação contextual.[1] O fator \(1/\sqrt{d_k}\) impede que a variância dos produtos escalares cresça proporcionalmente à dimensão das chaves, o que tenderia a levar o softmax a regiões de saturação e gradientes menores.[1] A atenção *multi-head* executa várias dessas operações em subespaços projetados diferentes e concatena seus resultados, permitindo que diferentes cabeças representem simultaneamente tipos distintos de relação entre tokens.[1]

Essa mesma primitiva deu origem a três grandes famílias arquiteturais: modelos *encoder-only*, como BERT, que usam atenção bidirecional e são naturalmente adequados à representação e compreensão de texto; modelos *decoder-only*, como a família GPT, que usam uma máscara causal e modelam \(p(x_t\mid x_{<t})\); e modelos *encoder-decoder*, como T5, que combinam um codificador bidirecional com um decodificador autoregressivo ligado ao encoder por *cross-attention*.[5][6][7][8]

O grande custo dessa flexibilidade é que a atenção densa entre \(n\) tokens calcula essencialmente uma matriz \(n\times n\), dando custo computacional \(O(n^2d)\) por camada e, em uma implementação ingênua que materialize os pesos de atenção, memória intermediária quadrática em \(n\).[1][10] As principais linhas de pesquisa em eficiência atacam partes diferentes desse problema: Longformer restringe conectividade com janelas locais e posições globais; Reformer usa hashing sensível à localidade; Performer aproxima o softmax por *random features*; FlashAttention mantém a atenção densa matematicamente exata, mas reorganiza o algoritmo para reduzir tráfego entre níveis de memória; e abordagens como Ring Attention e Native Sparse Attention reorganizam respectivamente a distribuição da atenção entre dispositivos e a própria esparsidade do padrão computado.[10][11][12][13][15][27]

LLMs modernos acrescentam à arquitetura um regime de treinamento em larga escala: pré-treinamento em grandes corpora, seguido por formas de especialização ou pós-treinamento, como *supervised fine-tuning* e, em sistemas alinhados por preferências humanas, RLHF.[6][7][9] Para tornar esse treinamento viável, técnicas como precisão mista, paralelismo tensorial, paralelismo em pipeline e particionamento de estados com ZeRO distribuem computação e memória entre muitos aceleradores.[19][20][21][22]

Por fim, aumentar parâmetros ou contexto não transforma um Transformer em um sistema de conhecimento infalível: modelos ainda podem produzir afirmações falsas, reproduzir vieses dos dados, utilizar de modo irregular informações espalhadas por contextos longos e ser vulneráveis a ataques como *prompt injection*.[23][24][25][26][28] Por isso, a fronteira atual combina janelas maiores, atenção eficiente e mecanismos externos, especialmente *retrieval-augmented generation* (RAG), que complementam a memória paramétrica do modelo com documentos recuperados em tempo de execução.[14]

## Da recorrência à atenção

Antes do Transformer, a formulação dominante para tradução neural e outras tarefas de sequência era o modelo *sequence-to-sequence*: um encoder recorrente lia a entrada e a condensava em uma representação de dimensão fixa, e outro RNN ou LSTM produzia a saída token a token.[3] Essa arquitetura era conceitualmente elegante, mas a representação única entre encoder e decoder constituía um gargalo particularmente problemático para sequências longas.[2]

Bahdanau, Cho e Bengio atacaram esse problema permitindo que o decoder consultasse diferentes estados do encoder em cada passo, atribuindo pesos diferenciáveis às posições de origem; essa ideia de alinhamento suave foi uma das raízes diretas da atenção moderna.[2] Em vez de obrigar todo o conteúdo da entrada a atravessar um único vetor, o decoder passou a formar dinamicamente um vetor de contexto a partir das partes mais relevantes da sequência.[2]

A recorrência, entretanto, mantinha uma limitação estrutural: para calcular o estado \(h_t\), é necessário ter o estado anterior \(h_{t-1}\), de modo que os passos temporais não podem ser todos avaliados simultaneamente durante o treinamento.[1][3] Relações entre posições muito afastadas também percorrem uma cadeia de muitos estados, criando um caminho computacional proporcional à distância entre os tokens.[1] LSTMs e mecanismos de gating amenizaram problemas de propagação de informação, mas não removeram essa dependência sequencial fundamental.[3]

Redes convolucionais constituíram uma alternativa importante: o ConvS2S de Gehring et al. mostrou que convoluções permitem computar simultaneamente as representações de diferentes posições e, portanto, explorar melhor o paralelismo disponível em GPUs.[4] Ainda assim, uma convolução de largura limitada vê apenas uma vizinhança local; para conectar posições muito distantes, é necessário empilhar camadas ou aumentar o campo receptivo.[1][4]

O Transformer fez uma escolha mais radical: remover tanto recorrência quanto convolução do mecanismo principal de comunicação entre posições e deixar que cada token atendesse diretamente aos demais.[1] Na comparação teórica apresentada no artigo original, uma camada de self-attention densa tem complexidade \(O(n^2d)\), exige \(O(1)\) operações sequenciais e cria caminhos de comprimento máximo \(O(1)\) entre quaisquer duas posições; uma camada recorrente custa \(O(nd^2)\), exige \(O(n)\) passos sequenciais e tem caminho máximo \(O(n)\).[1] Essa troca é decisiva: o Transformer sacrifica eficiência assintótica em sequências extremamente longas para obter paralelização e conectividade global muito favoráveis nas dimensões de sequência para as quais foi originalmente concebido.[1]

Esse é um ponto importante para compreender os LLMs: o sucesso do Transformer não veio simplesmente de “memorizar melhor”, mas de fornecer uma operação altamente paralelizável, diferenciável e capaz de combinar informação globalmente, justamente um padrão de computação que escala bem em aceleradores matriciais.[1]

## Arquitetura original e matemática da atenção

O Transformer de 2017 é uma arquitetura encoder-decoder.[1] O modelo base empregava seis blocos de encoder e seis de decoder, dimensão de representação \(d_\text{model}=512\) e oito cabeças de atenção.[1] Cada bloco do encoder continha uma subcamada de multi-head self-attention e uma rede feed-forward aplicada independentemente a cada posição, com conexões residuais e Layer Normalization ao redor das subcamadas.[1] A feed-forward original tinha duas transformações lineares separadas por ReLU e dimensão interna \(d_\text{ff}=2048\).[1]

O decoder acrescentava uma terceira subcamada: atenção entre o decoder e a saída do encoder, hoje normalmente chamada *cross-attention*.[1] Sua self-attention era mascarada para impedir que a representação da posição \(t\) tivesse acesso a posições futuras, preservando a fatoração autoregressiva necessária à geração.[1] O diagrama canônico dessas duas pilhas aparece na Figura 1 do artigo original de Vaswani et al., referenciado em [1].[1]

Matematicamente, considere uma matriz de representações \(X\in\mathbb{R}^{n\times d_\text{model}}\), uma linha por token.[1] Aprendem-se projeções lineares

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V.
\]

Cada linha \(q_i\) de \(Q\) representa aquilo que a posição \(i\) “procura”; cada \(k_j\) funciona como uma chave contra a qual essa consulta é comparada; e cada \(v_j\) contém a informação que será agregada se a posição \(j\) receber peso elevado.[1] Essa terminologia é interpretativa, mas a operação efetiva é simplesmente álgebra linear aprendida de ponta a ponta.[1]

O escore entre as posições \(i\) e \(j\) é

\[
s_{ij}=q_i^\top k_j.
\]

Reunindo todos os pares, obtém-se \(S=QK^\top\), uma matriz \(n\times n\).[1] Aplicando o softmax a cada linha após a escala:

\[
a_{ij}=
\frac{\exp(s_{ij}/\sqrt{d_k})}
{\sum_{\ell=1}^{n}\exp(s_{i\ell}/\sqrt{d_k})},
\]

e, portanto,

\[
z_i=\sum_j a_{ij}v_j.
\]

Em forma matricial, isso resulta na conhecida expressão

\[
\boxed{
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}
\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
}.
\][1]

O divisor \(\sqrt{d_k}\) tem uma justificativa estatística simples.[1] Se os componentes de \(q\) e \(k\) forem aproximadamente independentes, com média zero e variância unitária, o produto escalar é a soma de \(d_k\) produtos e tem variância proporcional a \(d_k\).[1] Dividi-lo por \(\sqrt{d_k}\) estabiliza a escala típica dos logits, evitando que dimensões grandes empurrem excessivamente o softmax para distribuições quase saturadas.[1]

A atenção multi-head repete esse processo usando projeções aprendidas diferentes:

\[
\operatorname{head}_i=
\operatorname{Attention}(QW_i^Q,KW_i^K,VW_i^V),
\]

\[
\operatorname{MultiHead}(Q,K,V)
=
\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O.
\]

No Transformer-base, \(h=8\) e cada cabeça tinha \(d_k=d_v=64\), de modo que o custo agregado permanecia aproximadamente comparável ao de uma única atenção com a dimensão integral.[1] O objetivo não é impor previamente que uma cabeça seja “sintática” ou “semântica”; as diferentes projeções apenas fornecem subespaços paralelos nos quais o treinamento pode aprender relações distintas.[1]

Como a atenção pura não conhece a ordem dos elementos, o Transformer original soma aos embeddings uma codificação posicional senoidal.[1] Para posição \(pos\) e dimensão \(i\),

\[
PE_{(pos,2i)}=
\sin\left(\frac{pos}{10000^{2i/d_\text{model}}}\right),
\]

\[
PE_{(pos,2i+1)}=
\cos\left(\frac{pos}{10000^{2i/d_\text{model}}}\right).
\][1]

Esses sinais fornecem ao modelo informação de posição sem recorrer a um relógio recorrente.[1] A versão original também testou embeddings posicionais aprendidos e encontrou desempenho semelhante em seu experimento de tradução, optando pelas senoides em parte pela possibilidade de extrapolar para comprimentos não observados.[1]

Em pseudocódigo conceitual, uma cabeça pode ser resumida por `Q = X @ Wq; K = X @ Wk; V = X @ Wv; scores = Q @ K.T / sqrt(dk); scores += mask; A = softmax(scores); Y = A @ V`.[1] Para self-attention, \(Q,K,V\) derivam da mesma sequência; para cross-attention, as queries vêm do decoder e keys/values vêm do encoder; na atenção causal, a máscara substitui logits correspondentes ao futuro por valores efetivamente equivalentes a \(-\infty\) antes do softmax.[1]

## Famílias de Transformer e treinamento de LLMs

As diferenças entre encoder-only, decoder-only e encoder-decoder resultam principalmente de quais posições podem atender a quais outras e de qual objetivo de treinamento é utilizado.[1][5][7][8]

BERT é o exemplo clássico de um Transformer encoder-only: seus blocos permitem que cada posição use contexto de ambos os lados e o pré-treinamento emprega um objetivo de *masked language modeling*, no qual tokens ocultados precisam ser inferidos usando o restante do contexto.[5] Essa bidirecionalidade torna a representação especialmente útil como entrada para classificadores, sistemas de extração e outras tarefas de compreensão, e o artigo de BERT mostrou que uma camada de saída relativamente pequena podia ser adicionada durante o fine-tuning para diversas tarefas.[5]

Em modelos autoregressivos do tipo GPT, o objetivo fundamental é

\[
\mathcal L_{\mathrm{AR}}
=
-\sum_t \log p_\theta(x_t\mid x_1,\ldots,x_{t-1}),
\]

isto é, maximizar a probabilidade do próximo token dadas apenas as posições anteriores.[6][7] A máscara causal é crucial porque impede que o modelo “veja a resposta” durante o treinamento.[1] Essa formulação também coincide naturalmente com a geração: dado um prefixo, calcula-se uma distribuição para o token seguinte, escolhe-se ou amostra-se um token e repete-se o processo.[6][7]

O GPT original articulou explicitamente a combinação de pré-treinamento generativo não supervisionado em texto com ajuste supervisionado posterior.[6] GPT-3 ampliou substancialmente essa estratégia, chegando a 175 bilhões de parâmetros e demonstrando capacidades *zero-shot*, *one-shot* e *few-shot* por condicionamento no prompt, sem atualizar os pesos para cada tarefa em tempo de inferência.[7]

T5 representa a terceira família: um Transformer encoder-decoder no qual diversas tarefas são formuladas uniformemente como transformação de texto em texto.[8] O encoder pode construir uma representação bidirecional da entrada, enquanto o decoder produz a saída causalmente e consulta o encoder por cross-attention.[1][8] Essa separação é útil conceitualmente em problemas em que existe uma entrada claramente distinta de uma saída, como tradução e sumarização.[8]

O pré-treinamento produz um modelo geral, mas não necessariamente um assistente que segue instruções humanas.[6][9] O trabalho InstructGPT sistematizou uma etapa de pós-treinamento em três movimentos: primeiro, *supervised fine-tuning* sobre demonstrações escritas por humanos; depois, coleta de comparações humanas entre respostas para treinar um modelo de recompensa; por fim, otimização da política linguística segundo essa recompensa, usando PPO no experimento descrito.[9] Os avaliadores do estudo chegaram a preferir um modelo InstructGPT de 1,3 bilhão de parâmetros ao GPT-3 de 175 bilhões em sua distribuição de prompts, ilustração de que alinhamento e qualidade comportamental não são simples funções do número de parâmetros.[9]

RLHF, contudo, não substitui pré-treinamento nem cria um verificador lógico de verdade; ele modifica o comportamento do modelo com base no sinal fornecido por preferências e pelo modelo de recompensa.[9] O próprio trabalho reporta que erros e limitações permanecem após o alinhamento.[9]

## Escalabilidade, atenção eficiente e engenharia distribuída

A maior fraqueza algorítmica da self-attention densa aparece diretamente em \(QK^\top\): para \(n\) tokens há \(n^2\) pares query-key.[1] Com dimensão \(d\), a ordem de trabalho é \(O(n^2d)\); em implementações convencionais que armazenam explicitamente scores ou probabilidades, também surge um tensor intermediário de tamanho \(O(n^2)\) por cabeça ou lote.[1][10] Dobrar a sequência, portanto, pode aproximadamente quadruplicar a parte quadrática da atenção, mesmo sem aumentar os parâmetros do modelo.[1][10]

As soluções não são equivalentes porque atacam gargalos diferentes.

Longformer troca atenção global completa por uma janela deslizante local complementada por posições com atenção global, obtendo custo que cresce linearmente com o comprimento quando a largura da janela é mantida fixa.[12] Essa estratégia é adequada a documentos longos porque muitos vínculos importantes são locais, enquanto alguns tokens escolhidos podem funcionar como canais globais.[12]

Reformer substitui a busca exaustiva por pares por atenção baseada em *locality-sensitive hashing*, agrupando queries e keys provavelmente semelhantes e reduzindo, na formulação do artigo, a complexidade da atenção de \(O(L^2)\) para aproximadamente \(O(L\log L)\).[13] O trabalho também emprega camadas residuais reversíveis para evitar manter todas as ativações intermediárias durante o backpropagation.[13]

Performer toma outra rota: aproxima a matriz de atenção softmax por meio do mecanismo FAVOR+, baseado em *random features*, de modo a reorganizar o cálculo sem materializar todos os pares de tokens.[11] O método reivindica complexidade linear em tempo e espaço em relação ao comprimento da sequência, mediante uma aproximação controlada da atenção softmax.[11]

FlashAttention resolve um problema diferente e, por isso, é incorreto descrevê-lo simplesmente como “atenção linear”.[10] O algoritmo continua calculando atenção densa exata e, portanto, não remove o número quadrático de interações matemáticas; a inovação é fazer *tiling* e recomputação de maneira consciente da hierarquia de memória, reduzindo leituras e escritas caras entre a memória de alta largura de banda da GPU e a SRAM local.[10] Assim, ele evita materializar grandes matrizes intermediárias e pode produzir grandes ganhos práticos de memória e velocidade sem alterar a função de atenção calculada.[10] A distinção é central: Performer, Longformer e Reformer modificam ou aproximam a estrutura da atenção; FlashAttention otimiza a execução da atenção densa.[10][11][12][13]

*Chunking* ou processamento em blocos é outra família de técnicas: divide-se a sequência em blocos que podem ser processados ou comunicados separadamente, reduzindo o pico de memória e tornando possível distribuir contextos muito extensos.[15] Ring Attention combina atenção em blocos com uma topologia em anel na qual cada dispositivo mantém parte dos estados e recebe blocos de keys e values de vizinhos, procurando sobrepor comunicação e computação.[15] O contexto suportável pode então crescer com o número de dispositivos, embora o método não transforme as interações densas em uma operação matematicamente linear.[15]

Native Sparse Attention, publicada em 2025, ilustra uma linha mais recente de atenção esparsa projetada explicitamente em conjunto com características do hardware.[27] NSA combina compressão hierárquica de tokens, seleção fina de posições e atenção local, e seus autores relatam acelerações em sequências de 64 mil tokens tanto no treinamento quanto na inferência em comparação com full attention.[27]

A eficiência do algoritmo de atenção, contudo, é apenas uma parte da engenharia de LLMs. *Mixed-precision training* usa formatos numéricos menores para grande parte da aritmética, mantendo operações ou estados sensíveis em maior precisão e empregando técnicas como *loss scaling* para evitar perda de gradientes pequenos; o trabalho clássico de Micikevicius et al. demonstrou treinamento FP16 com cópias mestres FP32 e redução substancial de uso de memória.[19] Frameworks atuais, como PyTorch, expõem suporte explícito a *automatic mixed precision* por meio de `torch.amp`.[29]

Quando um único acelerador não comporta o modelo, o paralelismo tensorial distribui partes das grandes multiplicações matriciais de uma mesma camada por diferentes dispositivos; Megatron-LM demonstrou essa estratégia em Transformers de múltiplos bilhões de parâmetros.[21] O paralelismo em pipeline, exemplificado por GPipe, distribui conjuntos de camadas sequenciais entre aceleradores e divide lotes em microbatches para manter vários estágios ocupados simultaneamente.[22]

ZeRO ataca a redundância do paralelismo de dados: em vez de cada worker manter cópias completas de todos os estados necessários ao treinamento, os dados são particionados entre workers.[20] A progressão conhecida como ZeRO-1, ZeRO-2 e ZeRO-3 particiona sucessivamente estados do otimizador, gradientes e parâmetros, permitindo que a memória agregada do cluster seja usada para modelos muito maiores.[20] Na prática, treinamento de LLMs de grande escala combina várias dimensões — dados, tensores, pipeline e sharding — em vez de existir uma única técnica universal de paralelização.[20][21][22]

## Limitações e fronteiras de pesquisa

A primeira limitação fundamental é factualidade. Um modelo autoregressivo é treinado para atribuir probabilidade ao próximo token condicionado ao contexto, não para executar por definição uma consulta a uma base de fatos verificada.[6][7] Por isso, texto linguisticamente plausível pode conter entidades inventadas, relações incorretas ou justificativas sem fundamento; relatórios de modelos de grande escala continuam identificando alucinações como uma limitação mesmo após pós-treinamento.[25]

TruthfulQA mostrou de forma particularmente clara que aumentar escala não garante verdade factual: no conjunto de 817 perguntas construído para provocar concepções equivocadas comuns, os modelos avaliados no estudo permaneceram muito abaixo do desempenho humano em veracidade, e os maiores modelos testados não foram sistematicamente os mais verdadeiros.[23] Esse resultado não significa que modelos maiores sejam sempre menos corretos; significa que a otimização da probabilidade linguística e a otimização da verdade são objetivos distintos.[23]

A segunda limitação envolve dados e viés. LLMs aprendem regularidades de grandes corpora produzidos socialmente, que contêm estereótipos, assimetrias de representação, linguagem ofensiva e outros padrões indesejáveis.[24] Bender et al. chamaram atenção para riscos associados à escala indiscriminada de corpora e modelos, incluindo reprodução de vieses, dificuldades de documentação e custos sociais e ambientais.[24] Técnicas de alinhamento podem reduzir determinadas classes de comportamento, mas não demonstram eliminação geral de vieses ou riscos.[9][24]

Uma terceira limitação é a própria noção de “contexto”. O número máximo de tokens aceitos e a capacidade de usar corretamente todos esses tokens não são a mesma coisa.[28] Em *Lost in the Middle*, Liu et al. observaram que modelos de longo contexto podiam apresentar desempenho muito melhor quando a informação relevante aparecia no início ou no fim do prompt e pior quando ela estava no meio, tanto em question answering multidocumento quanto em recuperação de pares chave-valor.[28] Assim, anunciar uma janela maior é uma propriedade de capacidade de entrada, não uma prova de recuperação uniforme ou raciocínio perfeito sobre todo o conteúdo.[28]

Há ainda riscos especificamente ligados à integração dos modelos com sistemas externos. A OWASP caracteriza *prompt injection* como a manipulação da entrada de um LLM para alterar seu comportamento esperado, potencialmente contornando instruções, expondo dados ou desencadeando ações indevidas quando o modelo possui acesso a ferramentas.[26] O problema torna-se especialmente relevante para agentes e aplicações RAG, porque textos recuperados de fontes externas podem conter instruções adversariais juntamente com conteúdo legítimo.[14][26]

As pesquisas sobre contexto extenso seguem várias direções complementares. YaRN propôs adaptar embeddings posicionais rotacionais para estender a janela de modelos existentes com menos treinamento adicional, reportando extensões de contexto de até 128 mil tokens em seus experimentos.[18] LongNet introduziu *dilated attention*, com o objetivo de manter crescimento aproximadamente linear de computação e caminhos logarítmicos de dependência, e apresentou experimentos de escala superior a um bilhão de tokens; esse resultado deve ser entendido como demonstração experimental de arquitetura, não como evidência de que LLMs convencionais usem um bilhão de tokens com fidelidade uniforme.[16]

Infini-attention combina atenção local mascarada com uma memória compressiva de longo prazo, buscando manter requisitos de memória limitados mesmo quando o histórico cresce.[17] Os autores reportaram experimentos incluindo recuperação em sequências de até um milhão de tokens e sumarização de livros muito extensos.[17] Como toda memória comprimida, a proposta muda a questão de “armazenar todos os pares de tokens” para “decidir que informação resumida deve persistir”, isto é, resolve um gargalo introduzindo outro problema de representação.[17]

RAG oferece uma solução conceitualmente diferente: em vez de tentar colocar todo o conhecimento nos parâmetros ou toda a evidência no contexto permanente, um componente de recuperação procura documentos relevantes em uma memória não paramétrica e os fornece ao gerador quando necessários.[14] No trabalho original, Lewis et al. combinaram um retriever neural sobre uma base de Wikipedia com um modelo seq2seq e obtiveram ganhos em tarefas intensivas em conhecimento.[14] A vantagem arquitetural é separar parcialmente “saber produzir linguagem” de “encontrar evidência”, permitindo atualizar o acervo recuperável sem necessariamente retreinar todos os parâmetros.[14] RAG, porém, não elimina erro factual: se o retriever selecionar documentos irrelevantes, se as fontes forem incorretas ou se o gerador ignorar a evidência, a saída ainda pode falhar.[14]

O quadro que emerge é que “resolver o contexto” não corresponde a uma única inovação. FlashAttention reduz o custo de movimentação de memória sem aproximar a atenção; Performer aproxima a operação; Longformer e NSA tornam as conexões esparsas; Ring Attention distribui blocos; YaRN altera a capacidade de extrapolação posicional; Infini-attention comprime história; e RAG desloca uma parte da memória para um sistema externo.[10][11][12][14][15][17][18][27] Essas soluções são complementares porque “contexto longo” envolve ao menos quatro problemas diferentes: custo aritmético, memória dos aceleradores, codificação de posição e capacidade efetiva de localizar e utilizar informação relevante.[10][18][28]

Em perspectiva, o Transformer tornou-se a base dos LLMs não porque tenha eliminado todos os gargalos da modelagem sequencial, mas porque converteu o problema em grandes operações matriciais paralelizáveis, combinou acesso flexível ao contexto com aprendizado end-to-end e criou uma interface arquitetural na qual melhorias algorítmicas, de hardware e de treinamento podem ser acumuladas.[1][10][20][21] O desafio contemporâneo é preservar essas vantagens à medida que contexto, parâmetros, dados e autonomia dos sistemas aumentam, sem tratar escala como substituta de eficiência, factualidade ou segurança.[9][23][26][27][28]

## Referências

**[1]** Vaswani, A. et al. *Attention Is All You Need*. 2017.  
https://arxiv.org/abs/1706.03762

**[2]** Bahdanau, D.; Cho, K.; Bengio, Y. *Neural Machine Translation by Jointly Learning to Align and Translate*. 2014.  
https://arxiv.org/abs/1409.0473

**[3]** Sutskever, I.; Vinyals, O.; Le, Q. V. *Sequence to Sequence Learning with Neural Networks*. 2014.  
https://arxiv.org/abs/1409.3215

**[4]** Gehring, J. et al. *Convolutional Sequence to Sequence Learning*. 2017.  
https://arxiv.org/abs/1705.03122

**[5]** Devlin, J. et al. *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. 2018.  
https://arxiv.org/abs/1810.04805

**[6]** Radford, A. et al. *Improving Language Understanding by Generative Pre-Training*. OpenAI, 2018.  
https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

**[7]** Brown, T. B. et al. *Language Models are Few-Shot Learners*. 2020.  
https://arxiv.org/abs/2005.14165

**[8]** Raffel, C. et al. *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer*. 2019/2020.  
https://arxiv.org/abs/1910.10683

**[9]** Ouyang, L. et al. *Training Language Models to Follow Instructions with Human Feedback*. 2022.  
https://arxiv.org/abs/2203.02155

**[10]** Dao, T. et al. *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness*. 2022.  
https://arxiv.org/abs/2205.14135

**[11]** Choromanski, K. et al. *Rethinking Attention with Performers*. 2020/2021.  
https://arxiv.org/abs/2009.14794

**[12]** Beltagy, I.; Peters, M. E.; Cohan, A. *Longformer: The Long-Document Transformer*. 2020.  
https://arxiv.org/abs/2004.05150

**[13]** Kitaev, N.; Kaiser, Ł.; Levskaya, A. *Reformer: The Efficient Transformer*. 2020.  
https://arxiv.org/abs/2001.04451

**[14]** Lewis, P. et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. 2020.  
https://arxiv.org/abs/2005.11401

**[15]** Liu, H.; Zaharia, M.; Abbeel, P. *Ring Attention with Blockwise Transformers for Near-Infinite Context*. 2023.  
https://arxiv.org/abs/2310.01889

**[16]** Ding, J. et al. *LongNet: Scaling Transformers to 1,000,000,000 Tokens*. 2023.  
https://arxiv.org/abs/2307.02486

**[17]** Munkhdalai, T. et al. *Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention*. 2024.  
https://arxiv.org/abs/2404.07143

**[18]** Peng, B. et al. *YaRN: Efficient Context Window Extension of Large Language Models*. 2023.  
https://arxiv.org/abs/2309.00071

**[19]** Micikevicius, P. et al. *Mixed Precision Training*. 2017/2018.  
https://arxiv.org/abs/1710.03740

**[20]** Rajbhandari, S. et al. *ZeRO: Memory Optimizations Toward Training Trillion Parameter Models*. 2019/2020.  
https://arxiv.org/abs/1910.02054

**[21]** Shoeybi, M. et al. *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism*. 2019.  
https://arxiv.org/abs/1909.08053

**[22]** Huang, Y. et al. *GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism*. 2018/2019.  
https://arxiv.org/abs/1811.06965

**[23]** Lin, S.; Hilton, J.; Evans, O. *TruthfulQA: Measuring How Models Mimic Human Falsehoods*. 2021.  
https://arxiv.org/abs/2109.07958

**[24]** Bender, E. M. et al. *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* FAccT 2021.  
https://dl.acm.org/doi/10.1145/3442188.3445922

**[25]** OpenAI. *GPT-4 Technical Report*. 2023.  
https://arxiv.org/abs/2303.08774

**[26]** OWASP Foundation. *Prompt Injection*.  
https://community.owasp.org/attacks/PromptInjection

**[27]** Yuan, J. et al. *Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention*. 2025.  
https://arxiv.org/abs/2502.11089

**[28]** Liu, N. F. et al. *Lost in the Middle: How Language Models Use Long Contexts*. 2023.  
https://arxiv.org/abs/2307.03172

**[29]** PyTorch. *Automatic Mixed Precision package — torch.amp*. Documentação oficial.  
https://docs.pytorch.org/docs/stable/amp.html