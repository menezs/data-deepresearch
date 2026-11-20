| Chunk | Veredito | Citações | Links das citações |
|---|---|---|---|
| **#0** — Isso incluía as LSTMs e as redes com portas (GRUs), consideradas o estado da arte em modelagem de linguagem e tradução automática. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#1** — O problema se agrava com sequências longas, porque limites de memória também restringem o agrupamento de vários exemplos em lote. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#2** — Os sistemas de tradução neural da época seguiam o esquema codificador–decodificador: o codificador comprimia a frase de origem num vetor de tamanho fixo, e o decodificador gerava a tradução a partir dele. | SUPPORTED | [2] | [2] - https://arxiv.org/pdf/1409.0473 |
| **#3** — Eles propuseram deixar o modelo fazer uma busca "suave" pelas partes da frase de origem relevantes para prever cada palavra de destino. | SUPPORTED | [2] | [2] - https://arxiv.org/pdf/1409.0473 |
| **#4** — Os alinhamentos aprendidos também batiam com a intuição humana. | SUPPORTED | [2] | [2] - https://arxiv.org/pdf/1409.0473 |
| **#5** — Em quase todos os casos, porém, ela continuava acoplada a uma rede recorrente. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#6** — O passo radical de Vaswani e colegas, no artigo "Attention Is All You Need", foi propor uma arquitetura baseada apenas em atenção, sem recorrência nem convoluções. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#7** — O peso de cada valor vem de uma função de compatibilidade entre a consulta e a chave correspondente. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#8** — Consultas e chaves têm dimensão d_k, e os valores têm dimensão d_v. O procedimento tem três passos: calcular o produto escalar da consulta com todas as chaves, dividir cada resultado pela raiz quadrada de d_k e aplicar uma softmax para obter os pesos sobre os valores. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#9** — Elas são empacotadas numa matriz Q, e as chaves e valores em matrizes K e V. A fórmula fica Attention(Q, K, V) = softmax(QKᵀ/√d_k)·V. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#10** — Já para valores grandes, a versão aditiva supera o produto escalar sem escala. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#11** — Se os componentes de q e k forem variáveis independentes com média 0 e variância 1, o produto escalar terá variância d_k. A divisão por √d_k neutraliza esse efeito. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#12** — As duas formas têm complexidade teórica parecida, mas o produto escalar é muito mais rápido e econômico em memória na prática, porque usa código de multiplicação de matrizes altamente otimizado. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#13** — A atenção é aplicada em paralelo sobre cada projeção, e os resultados são concatenados e projetados novamente. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#14** — Com uma única cabeça, a média ponderada acaba diluindo essas distinções. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#15** — Como cada cabeça tem dimensão reduzida, o custo total fica parecido com o de uma única cabeça de dimensão completa. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#16** — Uma única cabeça ficou 0,9 ponto BLEU abaixo da melhor configuração, mas a qualidade também caiu com cabeças demais. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#17** — O Transformer de 2017 usa a atenção multi-cabeça de três maneiras: | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#18** — Isso permite que cada posição do decodificador consulte todas as posições da entrada. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#19** — **Autoatenção no codificador.** Consultas, chaves e valores vêm todos do mesmo lugar, a saída da camada anterior, e cada posição pode atender a todas as outras. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#20** — A máscara é implementada atribuindo menos infinito, antes da softmax, às conexões proibidas. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#21** — O codificador original é uma pilha de N = 6 camadas idênticas, cada uma com duas subcamadas: uma autoatenção multi-cabeça e uma rede feed-forward totalmente conectada aplicada a cada posição. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#22** — Todas as subcamadas e embeddings produzem vetores de dimensão d_model = 512. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#23** — Ele acrescenta uma terceira subcamada, que faz atenção sobre a saída do codificador. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#24** — A dimensão interna é d_ff = 2048. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#25** — O modelo compartilha a mesma matriz de pesos entre as camadas de embedding e a transformação anterior à softmax. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#26** — Por isso, os autores somaram "codificações posicionais" aos embeddings de entrada. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#27** — A hipótese era que isso facilitaria aprender a atender por posições relativas, já que, para qualquer deslocamento fixo k, a codificação da posição pos+k é uma função linear da codificação de pos. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#28** — A versão senoidal foi escolhida porque talvez permitisse extrapolar para sequências mais longas que as vistas no treino. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#29** — O artigo compara camadas de autoatenção, recorrentes e convolucionais em três critérios: custo computacional por camada, quantidade de computação paralelizável e comprimento do caminho entre dependências de longo alcance. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#30** — A camada recorrente custa O(n·d²). | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#31** — **Operações sequenciais.** A autoatenção conecta todas as posições com um número constante de operações sequenciais, enquanto a camada recorrente exige O(n). | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#32** — **Caminho máximo.** O caminho máximo entre duas posições é constante na autoatenção e linear na recorrência. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#33** — Caminhos mais curtos facilitam o aprendizado de dependências longas. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#34** — Além disso, a autoatenção é mais barata que a recorrência quando n é menor que d, o que era comum nas frases da tradução automática. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#35** — O modelo grande atingiu 28,4 BLEU na tradução inglês–alemão do WMT 2014, superando em mais de 2 pontos os melhores resultados anteriores, inclusive conjuntos de modelos. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#36** — O modelo base foi treinado em apenas 12 horas. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#37** — A escolha também tinha um preço, que se tornaria central na era dos LLMs: o custo quadrático em n. Os próprios autores sugeriram restringir a atenção a uma vizinhança local para sequências muito longas. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#38** — Em 2018, Radford e colegas, da OpenAI, mostraram que era possível obter grandes ganhos em tarefas de compreensão de linguagem com pré-treinamento generativo de um modelo de linguagem num corpus diverso de texto sem rótulos, seguido de ajuste fino discriminativo em cada tarefa específica. | SUPPORTED | [3] | [3] - https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf |
| **#39** — Com mudanças mínimas na arquitetura, superou modelos desenhados especificamente para cada tarefa e melhorou o estado da arte em 9 das 12 tarefas estudadas. | SUPPORTED | [3] | [3] - https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf |
| **#40** — O modelo pré-treina representações bidirecionais profundas, condicionando cada posição ao contexto à esquerda e à direita em todas as camadas. | SUPPORTED | [4] | [4] - https://arxiv.org/abs/1810.04805 |
| **#41** — Para isso, adotou um objetivo de "modelo de linguagem mascarado", inspirado na tarefa de preenchimento de lacunas (Cloze), que permite fundir os dois contextos. | SUPPORTED | [4] | [4] - https://arxiv.org/abs/1810.04805 |
| **#42** — Obteve novos recordes em onze tarefas de processamento de linguagem natural, incluindo a elevação do placar GLUE para 80,5%. | SUPPORTED | [4] | [4] - https://arxiv.org/abs/1810.04805 |
| **#43** — Em 2020, a OpenAI treinou o GPT-3, um modelo autorregressivo com 175 bilhões de parâmetros, dez vezes mais que qualquer modelo de linguagem não esparso anterior. | SUPPORTED | [5] | [5] - https://arxiv.org/abs/2005.14165 |
| **#44** — As tarefas e alguns exemplos de demonstração eram especificados apenas como texto na entrada do modelo. | SUPPORTED | [5] | [5] - https://arxiv.org/abs/2005.14165 |
| **#45** — Os autores mostraram que aumentar a escala melhora muito o desempenho com poucos exemplos (few-shot), às vezes chegando a competir com abordagens de ajuste fino do estado da arte. | SUPPORTED | [5] | [5] - https://arxiv.org/abs/2005.14165 |
| **#46** — A perda segue uma lei de potência em relação ao tamanho do modelo, ao tamanho do conjunto de dados e à computação de treino, com tendências que se estendem por mais de sete ordens de grandeza. | SUPPORTED | [6] | [6] - https://arxiv.org/abs/2001.08361 |
| **#47** — O mesmo trabalho concluiu que outros detalhes arquiteturais, como largura ou profundidade da rede, têm efeito mínimo dentro de uma faixa ampla. | SUPPORTED | [6] | [6] - https://arxiv.org/abs/2001.08361 |
| **#48** — Por isso, o treino ótimo em computação envolveria modelos muito grandes, treinados com uma quantidade relativamente modesta de dados e interrompidos bem antes da convergência. | SUPPORTED | [6] | [6] - https://arxiv.org/abs/2001.08361 |
| **#49** — Concluíram que os grandes modelos da época estavam significativamente subtreinados e que tamanho do modelo e número de tokens devem crescer na mesma proporção: a cada duplicação de parâmetros, deve-se dobrar também os dados. | SUPPORTED | [7] | [7] - https://arxiv.org/abs/2203.15556 |
| **#50** — Para testar a hipótese, treinaram o Chinchilla, com o mesmo orçamento computacional do Gopher, mas com 70 bilhões de parâmetros e quatro vezes mais dados. | SUPPORTED | [7] | [7] - https://arxiv.org/abs/2203.15556 |
| **#51** — Foram 1,4 trilhão de tokens. | SUPPORTED | [7] | [7] - https://arxiv.org/abs/2203.15556 |
| **#52** — Como é menor, também custa menos para ajuste fino e inferência. | SUPPORTED | [7] | [7] - https://arxiv.org/abs/2203.15556 |
| **#53** — Modelos grandes podem gerar respostas falsas, tóxicas ou simplesmente inúteis. | SUPPORTED | [8] | [8] - https://arxiv.org/abs/2203.02155 |
| **#54** — Depois, coletar rankings de respostas do modelo e usar esses dados para um novo ajuste com aprendizado por reforço a partir de feedback humano (RLHF). | SUPPORTED | [8] | [8] - https://arxiv.org/abs/2203.02155 |
| **#55** — Em avaliações humanas, as respostas do InstructGPT de 1,3 bilhão de parâmetros foram preferidas às do GPT-3 de 175 bilhões, apesar de o modelo ter cem vezes menos parâmetros. | SUPPORTED | [8] | [8] - https://arxiv.org/abs/2203.02155 |
| **#56** — A família LLaMA, da Meta, com modelos de 7 a 65 bilhões de parâmetros, documenta bem esse "Transformer moderno". | SUPPORTED | [10] | [10] - https://arxiv.org/pdf/2302.13971 |
| **#57** — A normalização usa a função RMSNorm. | SUPPORTED | [10] | [10] - https://arxiv.org/pdf/2302.13971 |
| **#58** — No desenho original, a normalização vinha depois da soma residual. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#59** — **Ativação SwiGLU.** A ReLU da rede feed-forward é substituída pela SwiGLU, proposta por Shazeer para melhorar o desempenho. | SUPPORTED | [10] | [10] - https://arxiv.org/pdf/2302.13971 |
| **#60** — **Embeddings rotatórios (RoPE).** Os embeddings posicionais absolutos são removidos e substituídos por embeddings posicionais rotatórios, aplicados em cada camada da rede. | SUPPORTED | [10] | [10] - https://arxiv.org/pdf/2302.13971 |
| **#61** — Ele codifica a posição absoluta com uma matriz de rotação e, ao mesmo tempo, incorpora a dependência de posição relativa diretamente na formulação da autoatenção. | SUPPORTED | [9] | [9] - https://arxiv.org/abs/2104.09864 |
| **#62** — Entre as propriedades apontadas estão flexibilidade quanto ao comprimento da sequência e uma dependência entre tokens que decai à medida que a distância relativa aumenta. | SUPPORTED | [9] | [9] - https://arxiv.org/abs/2104.09864 |
| **#63** — O custo é uma possível perda de qualidade. | SUPPORTED | [11] | [11] - https://arxiv.org/abs/2305.13245 |
| **#64** — Ainslie e colegas propuseram a atenção por consultas agrupadas (GQA), uma generalização que usa um número intermediário de cabeças de chave–valor: mais de uma, mas menos que o número de cabeças de consulta. | SUPPORTED | [11] | [11] - https://arxiv.org/abs/2305.13245 |
| **#65** — Os autores também mostraram que é possível converter modelos multi-cabeça existentes usando cerca de 5% da computação original de pré-treinamento. | SUPPORTED | [11] | [11] - https://arxiv.org/abs/2305.13245 |
| **#66** — O custo quadrático da atenção em tempo e memória torna os Transformers lentos e famintos por memória em sequências longas. | SUPPORTED | [12] | [12] - https://arxiv.org/abs/2205.14135 |
| **#67** — Muitos métodos de atenção aproximada tentaram reduzir a complexidade sacrificando qualidade, mas frequentemente sem ganho real de tempo. | SUPPORTED | [12] | [12] - https://arxiv.org/abs/2205.14135 |
| **#68** — O FlashAttention divide o cálculo em blocos (tiling) para reduzir o tráfego entre a memória de alta largura de banda (HBM) e a SRAM do chip, e calcula a atenção exata, sem aproximação. | SUPPORTED | [12] | [12] - https://arxiv.org/abs/2205.14135 |
| **#69** — O método também viabilizou contextos mais longos, com modelos de melhor qualidade. | SUPPORTED | [12] | [12] - https://arxiv.org/abs/2205.14135 |
| **#70** — Modelos de mistura de especialistas (MoE) selecionam parâmetros diferentes para cada entrada, o que resulta em modelos esparsos, com enorme número de parâmetros, mas custo computacional constante. | SUPPORTED | [13] | [13] - https://jmlr.org/papers/v23/21-0998.html |
| **#71** — Obteve até 7 vezes mais velocidade de pré-treinamento com os mesmos recursos e chegou a modelos com um trilhão de parâmetros. | SUPPORTED | [13] | [13] - https://jmlr.org/papers/v23/21-0998.html |
| **#72** — Os autores observaram que cabeças de atenção individuais aprendem a executar tarefas diferentes, e muitas exibem comportamento relacionado à estrutura sintática e semântica das frases. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#73** — Um dos exemplos mostrava duas cabeças aparentemente envolvidas na resolução de anáfora, ou seja, em identificar a que palavra um pronome se refere. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#74** — [A] → [B]. | SUPPORTED | [14] | [14] - https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads |
| **#75** — Elas surgem exatamente no mesmo ponto do treino em que há um salto abrupto nessa capacidade. | SUPPORTED | [14] | [14] - https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads |
| **#76** — Para modelos maiores com camadas MLP, é correlacional. | SUPPORTED | [14] | [14] - https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads |
| **#77** — Os fragmentos são tratados como tokens, do mesmo modo que palavras. | UNSUPPORTED | [15] | [15] - https://huggingface.co/papers/2010.11929 |
| **#78** — Quando pré-treinado com dados suficientes, o ViT alcançou resultados excelentes em comparação com redes convolucionais de ponta, exigindo menos computação para treinar. | SUPPORTED | [15] | [15] - https://huggingface.co/papers/2010.11929 |
| **#79** — Muitas arquiteturas subquadráticas foram propostas, como atenção linear, convoluções com portas, modelos recorrentes e modelos de espaço de estados, mas não tiveram desempenho equivalente ao da atenção em linguagem. | SUPPORTED | [16] | [16] - https://arxiv.org/abs/2312.00752v2 |
| **#80** — Isso permite propagar ou esquecer informação seletivamente conforme o token atual. | SUPPORTED | [16] | [16] - https://arxiv.org/abs/2312.00752v2 |
| **#81** — Seu modelo de 3 bilhões de parâmetros superou Transformers do mesmo tamanho e igualou Transformers com o dobro do tamanho. | SUPPORTED | [16] | [16] - https://arxiv.org/abs/2312.00752v2 |
| **#82** — Eliminou a dependência sequencial que impedia o paralelismo e encurtou para uma constante o caminho entre quaisquer duas posições da sequência. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#83** — O núcleo é uma operação de poucas linhas, softmax(QKᵀ/√d_k)·V, repetida em várias cabeças e intercalada com redes feed-forward, conexões residuais e normalização. | SUPPORTED | [1] | [1] - https://arxiv.org/abs/1706.03762 |
| **#84** — pré-treinar decodificadores para prever o próximo token | SUPPORTED | [3] | [3] - https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf |
| **#85** — escalar parâmetros e dados segundo leis empíricas | SUPPORTED | [6][7] | [6] - https://arxiv.org/abs/2001.08361<br>[7] - https://arxiv.org/abs/2203.15556 |
| **#86** — descobrir capacidades de aprendizagem em contexto | SUPPORTED | [5] | [5] - https://arxiv.org/abs/2005.14165 |
| **#87** — alinhar os modelos com feedback humano. | SUPPORTED | [8] | [8] - https://arxiv.org/abs/2203.02155 |
| **#88** — No caminho, o bloco original recebeu pré-normalização, SwiGLU e RoPE | SUPPORTED | [10] | [10] - https://arxiv.org/pdf/2302.13971 |
| **#89** — atenção agrupada para inferência eficiente | SUPPORTED | [11] | [11] - https://arxiv.org/abs/2305.13245 |
| **#90** — implementações cientes do hardware | SUPPORTED | [12] | [12] - https://arxiv.org/abs/2205.14135 |
| **#91** — e camadas esparsas de especialistas. | SUPPORTED | [13] | [13] - https://jmlr.org/papers/v23/21-0998.html |
