# Arquitetura Transformer e Mecanismos de Atenção: O Fundamento Teórico e Prático dos Grandes Modelos de Linguagem

## Paradigm Shift em Processamento de Linguagem Natural: O Colapso das Arquiteturas Recorrentes

A evolução do Processamento de Linguagem Natural (PLN) e do Aprendizado de Máquina esteve historicamente vinculada ao desenvolvimento de modelos capazes de processar sequências temporais e textuais[1]. Antes da introdução da arquitetura Transformer, o paradigma dominante para a modelagem de linguagem e tradução automática baseava-se em Redes Neurais Recorrentes (RNNs), notadamente as variantes Long Short-Term Memory (LSTM) e Gated Recurrent Unit (GRU)[1]. Essas arquiteturas estruturavam o processamento de forma inerentemente sequencial: para computar o estado oculto  no passo temporal , o modelo dependia diretamente do estado oculto anterior  e do token de entrada [1].

Essa dependência temporal estrita impunha uma limitação computacional intransponível no treinamento em grande escala[1]. O processamento símbolo a símbolo impedia a paralelização das operações ao longo da dimensão da sequência dentro de um mesmo exemplo de treinamento[1]. À medida que a largura de banda de memória e a capacidade de processamento paralelo das Unidades de Processamento Gráfico (GPUs) e Tensor Processing Units (TPUs) evoluíam, as RNNs tornaram-se o gargalo computacional primário, incapazes de saturar a capacidade de cálculo dos aceleradores modernos[1].

Além das limitações de vazão (throughput), as redes recorrentes enfrentavam constrangimentos estruturais na retenção de dependências de longo alcance[1]. Embora os mecanismos de portas nas LSTMs e GRUs tivessem sido projetados para mitigar o esvanecimento do gradiente (vanishing gradient), a informação textual precisava ser comprimida através de uma sequência de transformações até um vetor de dimensão fixa[1]. Esse gargalo de representação resultava em uma perda progressiva de contexto à medida que a distância entre os tokens aumentava[1].

Para amenizar essa rigidez, mecanismos de atenção foram integrados às arquiteturas Encoder-Decoder baseadas em RNNs[1]. A atenção permitia que o decodificador consultasse os estados ocultos do codificador em cada passo de geração, estabelecendo conexões diretas entre palavras distantes no texto[1]. Contudo, a recorrência subjacente continuava presente, mantendo a complexidade temporal sequencial  incólume[1].

A ruptura definitiva ocorreu com a publicação do trabalho seminal "Attention Is All You Need" por Vaswani et al. (2017)[1]. A proposta fundamental do Transformer consistiu na eliminação completa de estruturas recorrentes e convolucionais, substituindo-as integralmente por um mecanismo de autoatenção (self-attention)[1]. Ao dispensar o alinhamento temporal, a arquitetura permitiu que todos os tokens de uma sequência fossem processados simultaneamente em operações matriciais massivamente paralelas, redefinindo os padrões de eficiência e escalabilidade na inteligência artificial[1].

## Decomposição Matemática e Algorítmica do Mecanismo de Atenção

O núcleo operacional da arquitetura Transformer reside na transformação do conceito de atenção em uma operação matricial linearmente escalável em paralelo[2]. O mecanismo de Scaled Dot-Product Attention (Atenção por Produto Escalar Escalado) opera sobre três representações vetoriais derivadas das sequências de entrada: Queries (), Keys () e Values ()².

Dada uma matriz de entrada , onde  representa o comprimento da sequência e  a dimensão de representação oculta da rede, as matrizes ,  e  são obtidas por meio de projeções lineares aprendidas[2]:

onde ,  e  são as matrizes de pesos treináveis[5].

A computação da atenção por produto escalar escalado é formalizada matematicamente pela seguinte expressão[2]:

O produto matricial  calcula a afinidade não normalizada entre cada par de tokens na sequência[2]. O termo de escalonamento  desempenha um papel crucial na estabilidade do treinamento[5]. Para valores elevados da dimensão da chave , a magnitude dos produtos escalares cresce proporcionalmente, o que empurra a função Softmax para regiões de saturação onde os gradientes são extremamente pequenos (vanishing gradients)[5]. A divisão pela raiz quadrada de  garante que a variância dos produtos escalares permaneça próxima de 1, preservando o fluxo adequado de gradientes durante a propagação para trás (backpropagation)[5].

A função Softmax é aplicada de forma posicional ao longo das linhas da matriz de afinidade, gerando uma distribuição de probabilidade que soma 1 para cada token[5]. O resultado dessa ponderação é multiplicado pela matriz de valores , produzindo uma representação contextualizada em que o vetor de cada token é uma combinação linear dos valores de todos os outros tokens da sequência[2].

Para expandir a capacidade do modelo de focar em diferentes subespaços de representação em posições distintas, Vaswani et al. introduziram a Multi-Head Attention (MHA)². Em vez de aplicar uma única função de atenção com dimensão , as projeções de ,  e  são divididas em  subespaços paralelos (heads ou cabeças de atenção)².

onde , ,  e [5]. No trabalho original, definiu-se  e , mantendo o custo computacional total equivalente ao de uma atenção de cabeça única com dimensão total [2].

Operação / Camada Complexidade Computacional por Camada Operações Sequenciais Mínimas Distância Máxima entre Caminhos

Self-Attention (Transformer)

Recorrente (LSTM / GRU)

Convolucional (1D)

A análise das propriedades computacionais evidencia a vantagem estrutural da autoatenção em termos de comprimento de caminho[3]. Enquanto uma rede recorrente exige  operações sequenciais para propagar a informação do primeiro ao último token, a autoatenção conecta qualquer par de tokens em  passos computacionais, eliminando a degradação contextual de longo alcance[1]. Em termos computacionais, a autoatenção é mais eficiente que camadas recorrentes quando o comprimento da sequência  é menor que a dimensão de representação , cenário típico nos modelos iniciais[3].

## Anatomia Estrutural da Arquitetura Transformer Clássica

A arquitetura original do Transformer é constituída por uma estrutura Encoder-Decoder composta pelo empilhamento de  blocos idênticos no codificador e  blocos no decodificador[2]. Cada bloco possui uma subestrutura modular contendo conexões residuais (residual skip connections) e camadas de normalização (Layer Normalization)².

### O Bloco Codificador (Encoder)

O codificador é projetado para construir representações contextuais profundas a partir da sequência de entrada[3]. Cada camada do codificador contém duas subcamadas principais[2]:

Uma camada de Multi-Head Self-Attention não mascarada, permitindo que cada token consulte livremente todas as posições da sequência de entrada[3].

Uma rede neural totalmente conectada Position-wise Feed-Forward Network (FFN), aplicada de forma independente e idêntica a cada posição[5]:

A FFN consiste em duas transformações lineares com uma ativação ReLU intermediária[5]. No modelo base do Transformer, a dimensão interna de projeção se expande de  para , retornando em seguida para 512[6].

Ao redor de cada subcamada, emprega-se uma transformação residual seguida por normalização de camada (Add & Norm)²:

As conexões residuais evitam o esvanecimento do gradiente em redes profundas, enquanto a LayerNorm estabiliza a dinâmica de ativação interna durante o treinamento[2].

### O Bloco Decodificador (Decoder)

O decodificador é responsável pela geração autoregressiva da sequência de saída[2]. Cada camada do decodificador é composta por três subcamadas[3]:

Causal (Masked) Multi-Head Self-Attention: Para manter a propriedade autoregressiva durante o treinamento, impede-se que posições presentes consultem tokens futuros[3]. Isso é implementado aplicando uma máscara triangular superior preenchida com  às matrizes de afinidade antes do cálculo da Softmax, zerando efetivamente a probabilidade de atenção para posições posteriores ()³.

Encoder-Decoder Cross-Attention: Nesta subcamada, as Queries () são derivadas do fluxo de dados do decodificador, enquanto as Keys () e Values () provêm diretamente da saída do codificador[5]. Esse arranjo permite que o decodificador condicione a geração da saída às representações contextuais ricas construídas a partir da entrada original[3].

Position-wise Feed-Forward Network: Estruturalmente análoga à subcamada presente no codificador[5].

### Codificação Posicional (Positional Encoding)

Como o mecanismo de autoatenção executa operações matriciais que consideram todos os tokens simultaneamente, a arquitetura é intrinsecamente invariante à permutação[3]. Para injetar a ordem sequencial das palavras na rede, torna-se estritamente necessário adicionar informações posicionais às representações de entrada (embeddings) antes da primeira camada[2].

Vaswani et al. adotaram uma codificação posicional senoidal e cossenoidal fixa de diferentes frequências[2]:

onde  é a posição do token no texto e  é o índice da dimensão do vetor[2]. A escolha dessas funções trigonométricas fundamentou-se na hipótese de que permitiriam ao modelo interpolar posições relativas facilmente, uma vez que  pode ser expresso como uma transformação linear de , além de facultar a extrapolação para comprimentos de sequência superiores aos observados no treinamento[2].

Componente de Hardware e Configuração Transformer Base (Vaswani et al., 2017) Transformer Big (Vaswani et al., 2017) Papel Funcional no Modelo

Camadas () 6 no Encoder / 6 no Decoder 6 no Encoder / 6 no Decoder Profundidade de abstração hierárquica[3]

Dimensão Oculta () 512 1024 Largura do canal de representação do token[2]

Cabeças de Atenção () 8 16 Diversificação de subespaços de atenção[2]

Dimensão Chave/Valor () 64 64 Escala individual de cada cabeça[2]

Dimensão FFN () 2048 4096 Capacidade de transformação não linear[6]

Custo de Treinamento 12 horas (8 GPUs P100) 3,5 dias (8 GPUs P100) Orçamento computacional do pré-treinamento[1]

Desempenho BLEU (WMT 2014 En-De) 25,8 BLEU 28,4 BLEU Métrica de qualidade na tradução automática[3]

## Taxonomia e Evolução dos Modelos de Linguagem Baseados em Transformer

A flexibilidade modular do Transformer permitiu a bifurcação da arquitetura original em três famílias fundamentais, cada uma especializada em regimes de tarefas específicos e sustentando o ecossistema moderno dos Grandes Modelos de Linguagem (LLMs)³.

### Arquiteturas Encoder-Only (Representacionais / Bidirecionais)

Os modelos baseados exclusivamente no codificador utilizam a autoatenção bidirecional não mascarada para extrair representações densas e contextualmente ricas[8]. O expoente definitivo desta classe é o BERT (Bidirectional Encoder Representations from Transformers), proposto por Devlin et al. (2018)[8].

O BERT revolucionou o pré-treinamento não supervisionado ao introduzir duas tarefas simultâneas[8]:

Masked Language Modeling (MLM): Uma porcentagem (15%) dos tokens de entrada é aleatoriamente mascarada com um token especial [MASK] (ou substituída por tokens aleatórios/mantida inalterada)[8]. O modelo deve prever os tokens mascarados utilizando o contexto bidirecional completo (à esquerda e à direita)[8].

Next Sentence Prediction (NSP): O modelo recebe pares de sentenças e aprende a classificar se a segunda sentença segue logicamente a primeira no corpus[8].

A arquitetura do BERT é disponibilizada em duas dimensões principais:  (, 110M parâmetros) e  (, 340M parâmetros)[9]. Essas redes estabeleceram novos recordes em tarefas de classificação, extração de entidades, resposta a perguntas (Question Answering) e inferência de linguagem natural[9].

### Arquiteturas Decoder-Only (Generativos / Autoregressivos)

A classe Decoder-Only tornou-se o padrão hegemônico para os LLMs modernos (incluindo as famílias GPT, LLaMA, Mistral e Claude)³. Essas redes removem o mecanismo de atenção cruzada e utilizam unicamente a atenção causal[3].

O objetivo de pré-treinamento é a Causal Language Modeling (CLM) ou previsão do próximo token (Next Token Prediction), onde o modelo maximiza a probabilidade logarítmica da sequência :

O processamento estritamente unidirecional garante que o modelo aprenda a estender sequências de forma coerente[3]. A simplicidade matemática do CLM, combinada com leis de escala (Scaling Laws), demonstrou uma capacidade inigualável de emergência de habilidades raciocinativas e aprendizado com poucas amostras (Few-Shot Learning).

### Arquiteturas Encoder-Decoder (Sequence-to-Sequence)

Mantendo a topologia do modelo original de Vaswani et al., arquiteturas como T5 (Text-to-Text Transfer Transformer) e BART preservam a separação entre codificador bidirecional e decodificador causal[2]. Elas mapeiam uma sequência de texto arbitrária para outra sequência de texto, sendo ideais para tradução automática, sumarização abstrativa e reescrita de código[2].

Família Arquitetural Mecanismo de Atenção Objetivos de Pré-treinamento Tarefas Principais Modelos Representativos

Encoder-Only Bidirecional Completo Masked LM (MLM), Next Sentence Prediction (NSP)[8] Classificação de texto, NER, Embeddings, Busca Semântica[8] BERT[8], RoBERTa[13], ELECTRA

Decoder-Only Unidirecional Causal Causal Language Modeling (CLM / Next-Token Prediction) Geração de texto, Agentes, Raciocínio Geral, Código GPT-4, LLaMA 3, Mistral, Gemma

Encoder-Decoder Bidirecional (Enc) + Causal/Cruzado (Dec)³ Span Corruption, Denoising Autoencoding Tradução Automática, Sumarização, Transformação Estruturada[2] T5[13], BART, Transformer Original[2]

## Eficiência Otimizada e Escala: Otimizações Modernas em Atenção e Posicionamento

A ampliação dos contextos operacionais dos LLMs de escopos modestos (512-2048 tokens) para dimensões massivas (32k a mais de 1 milhão de tokens) exigiu reestruturações algorítmicas severas nas mecânicas de autoatenção e no posicionamento relacional[14].

### Codificação Posicional Rotativa (Rotary Position Embeddings - RoPE)

O método tradicional de codificação senoidal absoluta apresentou severas limitações ao lidar com extensões dinâmicas de janela de contexto durante a inferência[2]. Para superar esse obstáculo, Jianlin Su et al. (2021) propuseram a Rotary Position Embedding (RoPE) no artigo RoFormer[16].

Em vez de somar um vetor de posição aos embeddings de entrada, o RoPE codifica a informação posicional multiplicando os vetores de Query () e Key () por uma matriz de rotação ortogonal no espaço complexo[16]. Para um vetor bidimensional  na posição , a transformação  é definida como:

Expandindo essa rotação para subespaços 2D ao longo de toda a dimensão do vetor de atenção , o produto escalar entre uma Query na posição  e uma Key na posição  incorpora naturalmente a distância relativa [16]:

Essa propriedade garante que a afinidade de atenção dependa intrinsecamente da distância relativa entre os tokens, permitindo uma extrapolação de contexto superior e maior estabilidade em sequências extensas[16].

### FlashAttention: Otimização Consciente de Hardware (IO-Awareness)

Apesar das otimizações matemáticas, a complexidade computacional e de memória da autoatenção padrão permanece quadrática  em relação ao comprimento da sequência [14]. Em arquiteturas modernas de GPUs (como a Nvidia A100 ou H100), o gargalo primário não reside na capacidade de cálculo em FLOPS das unidades de processamento (Tensor Cores), mas sim na largura de banda de transferência de dados entre a memória de alta largura de banda (High Bandwidth Memory - HBM) e a memória estática no chip (SRAM ou L1/Shared Memory)[15].

A atenção convencional calcula e armazena materializadamente no HBM as matrizes intermediárias  e [15]. Essa operação realiza contínuas leituras e escritas no HBM, caracterizando um processo categorizado como memory-bound[20].

Para resolver essa ineficiência, Tri Dao et al. (2022) introduziram o FlashAttention, um algoritmo exato de atenção consciente do fluxo de E/S (IO-aware)[14]. O FlashAttention reestrutura a computação da atenção utilizando duas técnicas centrais[15]:

Tiling (Blocagem): Divisão das matrizes de Query, Key e Value em blocos menores que cabem integralmente na memória ultrarrápida SRAM do chip[15]. As operações parciais de produto escalar e redução Softmax são processadas iterativamente bloco a bloco, eliminando a necessidade de materializar a matriz de atenção  completa na HBM[15].

Recomputação do Softmax On-line: Como a função Softmax requer o máximo global das entradas para garantir a estabilidade numérica (), o FlashAttention mantém estatísticas de normalização acumuladas (máximos locais e somas exponenciais parciais) à medida que novos blocos são carregados[15]. No passo de propagação para trás (backward pass), em vez de ler a matriz  do HBM, os valores de atenção são recomputados rapidamente diretamente no SRAM a partir dos vetores mantidos no forward pass[14].

Métrica de Desempenho / Propriedade Atenção Padrão (Standard PyTorch) FlashAttention (Dao et al., 2022) Impacto Prático na Arquitetura

Acessos de Memória (HBM)  (onde  é o tamanho da SRAM) Redução drástica do tráfego no barramento de memória[14]

Pegada de Memória (RAM/HBM)  (Quadrática)  (Linear em relação ao comprimento) Permite escalar janelas de contexto para dezenas de milhares de tokens[14]

Velocidade de Execução (Wall-Clock) Baseline de referência Aceleração de  a  mais rápida Redução expressiva no tempo de treinamento global dos LLMs[14]

Precisão Numérica Exata Exata (Sem aproximação esparsa) Preserva a integridade funcional do Transformer sem degradação do gradiente[14]

## Alinhamento de Grandes Modelos de Linguagem: De RLHF a DPO

O pré-treinamento de um Transformer em larga escala gera um modelo base proficiente na continuação estocástica de textos, contudo desalinhado das intenções humanas de presteza, segurança e precisão factual[23]. O processo tradicional para transformar um modelo pré-treinado em um assistente funcional envolvia a Ajustagem Fina Supervisionada (Supervised Fine-Tuning - SFT) seguida pelo Aprendizado por Reforço com Feedback Humano (Reinforcement Learning from Human Feedback - RLHF)[23].

### O Algoritmo RLHF Tradicional

O pipeline padrão do RLHF baseia-se na otimização de uma política via Proximal Policy Optimization (PPO)[23]:

Treina-se um Modelo de Recompensa (Reward Model - ) para prever a preferência humana dada uma entrada  e duas respostas candidatas , minimizando a perda do modelo Bradley-Terry[24]:

Ajusta-se a política do modelo de linguagem  via PPO para maximizar a recompensa predita, aplicando uma penalidade de Divergência de Kullback-Leibler (KL) em relação ao modelo de referência  para evitar que a política se desvie excessivamente e explore falhas do modelo de recompensa (reward hacking)[24].

Essa abordagem apresenta alta complexidade computacional e instabilidade no treinamento, pois exige a manutenção de quatro redes neurais simultâneas em memória durante a otimização PPO: a política treinada (), a política de referência (), o modelo de recompensa () e o modelo de valor ()[23].

### Otimização Direta de Preferências (Direct Preference Optimization - DPO)

Para eliminar a complexidade do RLHF baseado em PPO, Rafailov et al. (2023) derivaram a Direct Preference Optimization (DPO)[23]. Os autores demonstraram matematicamente que o problema de maximização de recompensa com restrição de divergência KL possui uma solução analítica exata que permite reparametrizar a função de recompensa diretamente em termos da probabilidade implícita do próprio modelo de linguagem[24]:

Substituindo essa equivalência analítica no modelo de preferência de Bradley-Terry, deriva-se a função de perda DPO, otimizada via estimativa de máxima verossimilhança simples[24]:

onde  é um hiperparâmetro de controle que regula o peso do desvio em relação à política de referência [26].

Em termos procedimentais, a transição do RLHF/PPO para o DPO representa uma mudança estrutural significativa: enquanto o pipeline clássico exige a amostragem dinâmica de respostas e o treinamento intermediário de um modelo de recompensa explícito , o DPO converte a otimização de preferências em um problema de classificação supervisionada de etapa única diretamente sobre a política , eliminando a necessidade de gerar saídas do modelo durante a fase de alinhamento[23].

Dimensão de Comparação RLHF Tradicional (PPO) Direct Preference Optimization (DPO)

Modelo de Recompensa Explícito Obrigatório (Treinado na Fase 1)[23] Desnecessário (Recompensa Implícita)[24]

Redes Mantidas em Memória 4 Redes ()[23] 2 Redes ()[24]

Amostragem Online na Inferência Sim (Requer geração de tokens via PPO)[23] Não (Treinamento estático offline)[24]

Estabilidade de Treinamento Baixa (Sensível a hiperparâmetros de RL)[23] Alta (Otimização por Máxima Verossimilhança)[24]

Desempenho de Alinhamento Baseline de Qualidade em Sumarização/Chat Equivalente ou Superior ao PPO[24]

## Desafios Sistêmicos, Otimizações de KV Cache e Perspectivas Futuras

Apesar da dominância irrestrita da arquitetura Transformer na construção dos LLMs modernos, limitações estruturais e gargalos computacionais persistem no horizonte tecnológico[14].

O desafio central decorre da pegada de memória do KV Cache (Key-Value Cache) durante o processo de inferência autoregressiva[22]. Embora o treinamento seja paralelizado em toda a sequência, a geração de texto ocorre token por token[3]. Para evitar a recomputação contínua das chaves () e valores () dos tokens anteriores, essas matrizes são armazenadas na memória VRAM da GPU[22]. À medida que o comprimento da sequência e o tamanho do lote (batch size) expandem, a demanda por memória do KV Cache cresce vertiginosamente, frequentemente superando o tamanho dos próprios parâmetros do modelo[22]. Para conter essa expansão, variações arquiteturais como Grouped-Query Attention (GQA) e Multi-Query Attention (MQA) foram desenvolvidas, reduzindo o número de cabeças alocadas para chaves e valores enquanto mantêm a capacidade de representação do modelo.

Outro vetor de desenvolvimento busca solucionar a complexidade quadrática inerente ao mecanismo de autoatenção em comprimentos de sequência extremos[14]. Embora otimizações em nível de hardware como o FlashAttention reduzam o tráfego de E/S, a complexidade conceitual de operações FLOPS no produto  permanece [14]. Essa limitação impulsionou o avanço de arquiteturas alternativas e híbridas, tais como os State Space Models (SSMs - exemplificados pela arquitetura Mamba) e mecanismos de atenção linear. Essas abordagens prometem uma complexidade de inferência e treinamento , mantendo a capacidade de retenção contextual a distâncias indefinidas.

Em síntese, a arquitetura Transformer redefiniu o ecossistema do Aprendizado de Máquina ao substituir o encadeamento temporal estrito por um mecanismo exato, paralelizável e matematicamente elegante de alinhamento relacional[1]. Desde o artigo original de Vaswani et al. em 2017 até as otimizações contemporâneas em FlashAttention, RoPE e DPO, a flexibilidade estrutural da autoatenção demonstrou ser o catalisador primário da revolução dos Grandes Modelos de Linguagem[2].

#### Referências citadas

(PDF) Attention is All you Need (2017) | Ashish Vaswani - SciSpace, https://scispace.com/papers/attention-is-all-you-need-1hodz0wcqb

Attention Is All You Need - Wikipedia, https://en.wikipedia.org/wiki/Attention_Is_All_You_Need

Attention Is All You Need | alphaXiv, https://www.alphaxiv.org/abs/1706.03762

[1706.03762] Attention Is All You Need - arXiv, https://arxiv.org/abs/1706.03762

Attention is All you Need, https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf

Paper Walkthrough: Attention Is All You Need - Towards Data Science, https://towardsdatascience.com/paper-walkthrough-attention-is-all-you-need-80399cdc59e1/

Attention Is All You Need (Vaswani et al., ArXiv 2017), https://jkk.name/reading-notes/old-blog/2017-10-20_onlyattention/

BERT: Pre-training of Deep Bidirectional Transformers for Language, https://ysu1989.github.io/courses/au20/cse5539/BERT.pdf

BERT: Pre-training of Deep Bidirectional Transformers for Language, http://mlg.postech.ac.kr/~jtkim/courses/2022-spring-trends-in-ml/materials/05_bert.pdf

BERT: Pre-training of Deep Bidirectional Transformers for Language, https://aclanthology.org/N19-1423.pdf

BERT: Pre-training of Deep Bidirectional Transformers for Language, https://www.researchgate.net/publication/328230984_BERT_Pre-training_of_Deep_Bidirectional_Transformers_for_Language_Understanding

BERT: Pre-training of Deep Bidirectional Transformers for Language, https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992

BERT: Pre-training of Deep Bidirectional Transformers for Language, https://scispace.com/papers/bert-pre-training-of-deep-bidirectional-transformers-for-3mez6kncl2

FlashAttention: Fast and Memory-Efficient Exact Attention with IO, https://3dvar.com/Dao2022FlashAttention.pdf

FLASHATTENTION: Fast and Memory-Efficient Exact Attention with, https://openreview.net/pdf?id=H4DqfPSibmx

RoFormer: Enhanced Transformer with Rotary Position Embedding, https://huggingface.co/papers/2104.09864

RoFormer: Enhanced Transformer with Rotary Position Embedding, https://www.researchgate.net/publication/351019664_RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding

时光- 科学空间|Scientific Spaces, https://spaces.ac.cn/me.html/comment-page-10

[투빅스 4주차 논문리뷰] RoFormer — Enhanced Transformer with, https://velog.io/@lyoonji/%ED%88%AC%EB%B9%85%EC%8A%A4-4%EC%A3%BC%EC%B0%A8-%EC%A0%95%EA%B7%9C%EC%84%B8%EC%85%98-TimeSeries

FlashAttention: Fast and Memory-Efficient Exact Attention with IO, https://shreyansh26.github.io/post/2023-03-26_flash-attention/

FlashAttention: Fast and Memory-Efficient Exact Attention with IO, https://arxiv.org/abs/2205.14135

GitHub - Dao-AILab/flash-attention: Fast and memory-efficient exact, https://github.com/dao-ailab/flash-attention

Direct Preference Optimization: Your Language Model is Secretly a, https://medium.com/@EleventhHourEnthusiast/direct-preference-optimization-your-language-model-is-secretly-a-reward-model-5b8f44cb9b9b

(PDF) Direct Preference Optimization: Your Language Model is, https://www.researchgate.net/publication/371136760_Direct_Preference_Optimization_Your_Language_Model_is_Secretly_a_Reward_Model

Direct Preference Optimization:Your Language Model is Secretly a, https://arxiv.org/html/2305.18290v3

Direct Preference Optimization: Your Language Model is Secretly a, https://papers.baulab.info/papers/also/Rafailov-2023.pdf

Direct Preference Optimization: Your Language Model is Secretly a, https://arxiv.org/abs/2305.18290

Direct Preference Optimization: Your Language Model is Secretly a, https://arxiv.org/html/2305.18290v1

Direct Preference Optimization: Your Language Model is Secretly a, https://huggingface.co/papers/2305.18290