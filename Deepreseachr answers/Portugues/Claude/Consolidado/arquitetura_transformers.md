# Arquitetura Transformer: o mecanismo de atenção e a base dos LLMs

## Escopo

Este texto cobre cinco pontos. O primeiro é o problema que o Transformer resolveu. O segundo é o funcionamento do mecanismo de atenção, desde as fórmulas até a intuição por trás delas. O terceiro é a anatomia do bloco Transformer original. O quarto é o caminho que levou essa arquitetura a se tornar a base dos grandes modelos de linguagem (LLMs): pré-treinamento, leis de escala e alinhamento. O quinto são as modificações que os LLMs atuais fizeram sobre o desenho de 2017, seus limites e as alternativas que surgiram. A ênfase está no texto, mas o fim do percurso mostra que a mesma ideia se estendeu a outras modalidades.

## O problema antes do Transformer

Até 2017, as redes recorrentes eram o padrão para tarefas de sequência. Isso incluía as LSTMs e as redes com portas (GRUs), consideradas o estado da arte em modelagem de linguagem e tradução automática [1]. Essas redes processam a sequência posição por posição. Cada estado oculto depende do estado anterior e da entrada atual, e essa natureza sequencial impede paralelizar o cálculo dentro de um mesmo exemplo de treino. O problema se agrava com sequências longas, porque limites de memória também restringem o agrupamento de vários exemplos em lote [1].

Havia ainda um gargalo de representação. Os sistemas de tradução neural da época seguiam o esquema codificador–decodificador: o codificador comprimia a frase de origem num vetor de tamanho fixo, e o decodificador gerava a tradução a partir dele [2]. Bahdanau, Cho e Bengio levantaram a hipótese de que esse vetor fixo limitava o desempenho. Eles propuseram deixar o modelo fazer uma busca "suave" pelas partes da frase de origem relevantes para prever cada palavra de destino [2]. Com isso, alcançaram desempenho comparável ao melhor sistema estatístico baseado em frases na tradução inglês–francês. Os alinhamentos aprendidos também batiam com a intuição humana [2].

Essa foi a origem prática da "atenção". Em quase todos os casos, porém, ela continuava acoplada a uma rede recorrente [1]. O passo radical de Vaswani e colegas, no artigo "Attention Is All You Need", foi propor uma arquitetura baseada apenas em atenção, sem recorrência nem convoluções [1].

## O mecanismo de atenção

### Consultas, chaves e valores

O artigo original define uma função de atenção como o mapeamento de uma consulta (query) e de um conjunto de pares chave–valor (key–value) para uma saída, todos vetores. A saída é uma soma ponderada dos valores. O peso de cada valor vem de uma função de compatibilidade entre a consulta e a chave correspondente [1].

Uma analogia ajuda. Imagine uma biblioteca em que cada livro tem uma etiqueta (a chave) e um conteúdo (o valor). Você chega com uma pergunta (a consulta). Em vez de escolher um único livro, compara a pergunta com todas as etiquetas e lê uma mistura dos conteúdos, dando mais peso aos livros cujas etiquetas combinam melhor com o que você procura.

### Atenção por produto escalado

A versão adotada pelo Transformer chama-se "atenção por produto escalar escalado" (scaled dot-product attention). Consultas e chaves têm dimensão d_k, e os valores têm dimensão d_v. O procedimento tem três passos: calcular o produto escalar da consulta com todas as chaves, dividir cada resultado pela raiz quadrada de d_k e aplicar uma softmax para obter os pesos sobre os valores [1].

Na prática, o cálculo é feito para muitas consultas ao mesmo tempo. Elas são empacotadas numa matriz Q, e as chaves e valores em matrizes K e V. A fórmula fica Attention(Q, K, V) = softmax(QKᵀ/√d_k)·V [1].

Por que dividir por √d_k? Os autores observaram que, para valores pequenos de d_k, a atenção aditiva de Bahdanau e a atenção por produto escalar têm desempenho parecido. Já para valores grandes, a versão aditiva supera o produto escalar sem escala [1]. A explicação proposta é que, com d_k grande, os produtos escalares crescem em magnitude e empurram a softmax para regiões de gradiente extremamente pequeno. Se os componentes de q e k forem variáveis independentes com média 0 e variância 1, o produto escalar terá variância d_k. A divisão por √d_k neutraliza esse efeito [1].

A escolha do produto escalar também é de engenharia. As duas formas têm complexidade teórica parecida, mas o produto escalar é muito mais rápido e econômico em memória na prática, porque usa código de multiplicação de matrizes altamente otimizado [1].

### Atenção multi-cabeça

Em vez de uma única atenção sobre vetores de dimensão d_model, os autores projetam linearmente consultas, chaves e valores h vezes, cada vez com projeções diferentes e aprendidas. A atenção é aplicada em paralelo sobre cada projeção, e os resultados são concatenados e projetados novamente [1].

A justificativa é que a atenção multi-cabeça permite ao modelo atender simultaneamente a informações de diferentes subespaços de representação, em posições diferentes. Com uma única cabeça, a média ponderada acaba diluindo essas distinções [1]. No modelo original foram usadas h = 8 cabeças, cada uma com d_k = d_v = 64. Como cada cabeça tem dimensão reduzida, o custo total fica parecido com o de uma única cabeça de dimensão completa [1].

Os experimentos de ablação confirmaram o valor da ideia com uma ressalva. Uma única cabeça ficou 0,9 ponto BLEU abaixo da melhor configuração, mas a qualidade também caiu com cabeças demais [1].

### Três usos da atenção no modelo original

O Transformer de 2017 usa a atenção multi-cabeça de três maneiras [1]:

- **Atenção codificador–decodificador.** As consultas vêm da camada anterior do decodificador, e as chaves e valores vêm da saída do codificador. Isso permite que cada posição do decodificador consulte todas as posições da entrada [1].
- **Autoatenção no codificador.** Consultas, chaves e valores vêm todos do mesmo lugar, a saída da camada anterior, e cada posição pode atender a todas as outras [1].
- **Autoatenção mascarada no decodificador.** Cada posição só pode atender às posições anteriores e a si mesma, o que preserva a propriedade autorregressiva. A máscara é implementada atribuindo menos infinito, antes da softmax, às conexões proibidas [1].

Essa máscara causal é o ingrediente que, mais tarde, permitiria construir LLMs geradores usando apenas a pilha do decodificador.

## A anatomia do bloco Transformer

O codificador original é uma pilha de N = 6 camadas idênticas, cada uma com duas subcamadas: uma autoatenção multi-cabeça e uma rede feed-forward totalmente conectada aplicada a cada posição [1]. Cada subcamada é envolvida por uma conexão residual seguida de normalização de camada, de modo que a saída tem a forma LayerNorm(x + Subcamada(x)). Todas as subcamadas e embeddings produzem vetores de dimensão d_model = 512 [1].

O decodificador também tem seis camadas. Ele acrescenta uma terceira subcamada, que faz atenção sobre a saída do codificador [1].

A rede feed-forward de cada posição consiste em duas transformações lineares com uma ativação ReLU entre elas. A dimensão interna é d_ff = 2048 [1]. Uma intuição útil é que a atenção move informação entre posições, enquanto a feed-forward processa a informação dentro de cada posição.

Os tokens de entrada e saída são convertidos em vetores por embeddings aprendidos. A saída do decodificador passa por uma transformação linear e uma softmax para produzir as probabilidades do próximo token. O modelo compartilha a mesma matriz de pesos entre as camadas de embedding e a transformação anterior à softmax [1].

### Codificação posicional

Sem recorrência nem convolução, a atenção sozinha não distingue a ordem dos tokens. Por isso, os autores somaram "codificações posicionais" aos embeddings de entrada [1]. Eles usaram senos e cossenos de frequências diferentes, com comprimentos de onda em progressão geométrica. A hipótese era que isso facilitaria aprender a atender por posições relativas, já que, para qualquer deslocamento fixo k, a codificação da posição pos+k é uma função linear da codificação de pos [1].

Embeddings posicionais aprendidos deram resultados quase idênticos. A versão senoidal foi escolhida porque talvez permitisse extrapolar para sequências mais longas que as vistas no treino [1]. Esse tema voltaria anos depois com codificações posicionais mais sofisticadas, discutidas adiante.

## Por que a autoatenção funcionou

O artigo compara camadas de autoatenção, recorrentes e convolucionais em três critérios: custo computacional por camada, quantidade de computação paralelizável e comprimento do caminho entre dependências de longo alcance [1].

- **Custo por camada.** A autoatenção custa O(n²·d), em que n é o comprimento da sequência e d a dimensão da representação. A camada recorrente custa O(n·d²) [1].
- **Operações sequenciais.** A autoatenção conecta todas as posições com um número constante de operações sequenciais, enquanto a camada recorrente exige O(n) [1].
- **Caminho máximo.** O caminho máximo entre duas posições é constante na autoatenção e linear na recorrência [1].

Caminhos mais curtos facilitam o aprendizado de dependências longas [1]. Além disso, a autoatenção é mais barata que a recorrência quando n é menor que d, o que era comum nas frases da tradução automática [1].

Os resultados empíricos foram contundentes. O modelo grande atingiu 28,4 BLEU na tradução inglês–alemão do WMT 2014, superando em mais de 2 pontos os melhores resultados anteriores, inclusive conjuntos de modelos [1]. O treino levou 3,5 dias em oito GPUs P100. O modelo base foi treinado em apenas 12 horas [1].

A escolha também tinha um preço, que se tornaria central na era dos LLMs: o custo quadrático em n. Os próprios autores sugeriram restringir a atenção a uma vizinhança local para sequências muito longas [1].

## Do Transformer aos modelos de linguagem pré-treinados

O artigo original tratava de tradução. A virada para os LLMs veio da percepção de que partes da arquitetura podiam ser pré-treinadas em grandes volumes de texto não rotulado e depois reaproveitadas. Três famílias se consolidaram:

- **Só codificador:** o BERT.
- **Só decodificador:** a linha GPT.
- **Codificador–decodificador completo:** a forma original.

### A linha GPT: só decodificador

Em 2018, Radford e colegas, da OpenAI, mostraram que era possível obter grandes ganhos em tarefas de compreensão de linguagem com pré-treinamento generativo de um modelo de linguagem num corpus diverso de texto sem rótulos, seguido de ajuste fino discriminativo em cada tarefa específica [3]. O modelo usava um decodificador Transformer de 12 camadas com autoatenção mascarada. Com mudanças mínimas na arquitetura, superou modelos desenhados especificamente para cada tarefa e melhorou o estado da arte em 9 das 12 tarefas estudadas [3].

O objetivo de treino era simples: prever o próximo token. A máscara causal do decodificador permite fazer isso em paralelo para todas as posições de uma sequência durante o treino.

### BERT: só codificador

Pouco depois, o Google apresentou o BERT, sigla para "Bidirectional Encoder Representations from Transformers". O modelo pré-treina representações bidirecionais profundas, condicionando cada posição ao contexto à esquerda e à direita em todas as camadas [4]. Para isso, adotou um objetivo de "modelo de linguagem mascarado", inspirado na tarefa de preenchimento de lacunas (Cloze), que permite fundir os dois contextos [4].

O BERT pré-treinado podia ser ajustado com apenas uma camada de saída adicional. Obteve novos recordes em onze tarefas de processamento de linguagem natural, incluindo a elevação do placar GLUE para 80,5% [4]. Modelos do tipo BERT tornaram-se a base de sistemas de classificação e busca. A linha generativa, porém, é a que deu origem aos LLMs conversacionais.

### GPT-3 e a aprendizagem em contexto

O salto qualitativo veio com a escala. Em 2020, a OpenAI treinou o GPT-3, um modelo autorregressivo com 175 bilhões de parâmetros, dez vezes mais que qualquer modelo de linguagem não esparso anterior [5]. O GPT-3 foi avaliado sem atualização de gradientes nem ajuste fino. As tarefas e alguns exemplos de demonstração eram especificados apenas como texto na entrada do modelo [5].

Os autores mostraram que aumentar a escala melhora muito o desempenho com poucos exemplos (few-shot), às vezes chegando a competir com abordagens de ajuste fino do estado da arte [5]. Esse comportamento, chamado de aprendizagem em contexto (in-context learning), passou a definir a forma como se usam LLMs: por meio de instruções e exemplos no próprio prompt.

## As leis de escala

O GPT-3 se apoiou num resultado empírico publicado meses antes por Kaplan e colegas. Eles estudaram leis de escala para a perda de entropia cruzada de modelos de linguagem. A perda segue uma lei de potência em relação ao tamanho do modelo, ao tamanho do conjunto de dados e à computação de treino, com tendências que se estendem por mais de sete ordens de grandeza [6].

O mesmo trabalho concluiu que outros detalhes arquiteturais, como largura ou profundidade da rede, têm efeito mínimo dentro de uma faixa ampla [6]. Concluiu também que modelos maiores são muito mais eficientes em amostras. Por isso, o treino ótimo em computação envolveria modelos muito grandes, treinados com uma quantidade relativamente modesta de dados e interrompidos bem antes da convergência [6].

Essa última recomendação foi revista em 2022 pela DeepMind. Hoffmann e colegas treinaram mais de 400 modelos, de 70 milhões a mais de 16 bilhões de parâmetros, com 5 a 500 bilhões de tokens. Concluíram que os grandes modelos da época estavam significativamente subtreinados e que tamanho do modelo e número de tokens devem crescer na mesma proporção: a cada duplicação de parâmetros, deve-se dobrar também os dados [7].

Para testar a hipótese, treinaram o Chinchilla, com o mesmo orçamento computacional do Gopher, mas com 70 bilhões de parâmetros e quatro vezes mais dados [7]. Foram 1,4 trilhão de tokens [7]. O Chinchilla superou de forma uniforme modelos muito maiores, como Gopher (280B), GPT-3 (175B) e Megatron-Turing NLG (530B). Como é menor, também custa menos para ajuste fino e inferência [7].

O que torna essa discussão possível é justamente a regularidade da arquitetura. O Transformer se comporta de forma previsível quando escalado, o que transformou o desenvolvimento de LLMs num problema de alocação de recursos.

## Do modelo pré-treinado ao assistente

Um modelo treinado só para prever o próximo token não é, por si só, um bom assistente. O trabalho da OpenAI sobre o InstructGPT afirma que aumentar o modelo não o torna inerentemente melhor em seguir a intenção do usuário. Modelos grandes podem gerar respostas falsas, tóxicas ou simplesmente inúteis [8].

A solução proposta tinha duas etapas. Primeiro, coletar demonstrações escritas por anotadores e usá-las para ajustar o GPT-3 de forma supervisionada. Depois, coletar rankings de respostas do modelo e usar esses dados para um novo ajuste com aprendizado por reforço a partir de feedback humano (RLHF) [8].

O resultado foi notável. Em avaliações humanas, as respostas do InstructGPT de 1,3 bilhão de parâmetros foram preferidas às do GPT-3 de 175 bilhões, apesar de o modelo ter cem vezes menos parâmetros [8]. Do ponto de vista arquitetural, nada muda: é o mesmo Transformer decodificador. O que muda são os dados e o objetivo do treino posterior.

## A arquitetura dos LLMs modernos

Embora a essência de 2017 permaneça, os LLMs atuais incorporaram uma série de refinamentos. A família LLaMA, da Meta, com modelos de 7 a 65 bilhões de parâmetros, documenta bem esse "Transformer moderno" [10]. Seus autores listam três diferenças principais em relação à arquitetura original:

- **Pré-normalização.** A entrada de cada subcamada é normalizada, em vez da saída, para melhorar a estabilidade do treino. A normalização usa a função RMSNorm [10]. No desenho original, a normalização vinha depois da soma residual [1].
- **Ativação SwiGLU.** A ReLU da rede feed-forward é substituída pela SwiGLU, proposta por Shazeer para melhorar o desempenho [10].
- **Embeddings rotatórios (RoPE).** Os embeddings posicionais absolutos são removidos e substituídos por embeddings posicionais rotatórios, aplicados em cada camada da rede [10].

O RoPE foi proposto por Su e colegas. Ele codifica a posição absoluta com uma matriz de rotação e, ao mesmo tempo, incorpora a dependência de posição relativa diretamente na formulação da autoatenção [9]. Entre as propriedades apontadas estão flexibilidade quanto ao comprimento da sequência e uma dependência entre tokens que decai à medida que a distância relativa aumenta [9].

### O gargalo da inferência e a atenção agrupada

Na geração autorregressiva, o modelo produz um token por vez. Para não recalcular tudo a cada passo, as chaves e os valores dos tokens anteriores ficam guardados em memória, no chamado cache KV. Com contextos longos e muitas cabeças, ler esse cache passa a dominar o tempo de inferência.

A atenção multi-consulta (MQA) usa uma única cabeça de chave–valor compartilhada por todas as cabeças de consulta, o que acelera drasticamente a inferência do decodificador. O custo é uma possível perda de qualidade [11]. Ainslie e colegas propuseram a atenção por consultas agrupadas (GQA), uma generalização que usa um número intermediário de cabeças de chave–valor: mais de uma, mas menos que o número de cabeças de consulta [11]. A GQA atinge qualidade próxima da atenção multi-cabeça com velocidade comparável à MQA. Os autores também mostraram que é possível converter modelos multi-cabeça existentes usando cerca de 5% da computação original de pré-treinamento [11].

### FlashAttention: atenção exata ciente da memória

O custo quadrático da atenção em tempo e memória torna os Transformers lentos e famintos por memória em sequências longas [12]. Muitos métodos de atenção aproximada tentaram reduzir a complexidade sacrificando qualidade, mas frequentemente sem ganho real de tempo [12].

Dao e colegas argumentaram que faltava considerar as leituras e escritas entre os níveis de memória da GPU. O FlashAttention divide o cálculo em blocos (tiling) para reduzir o tráfego entre a memória de alta largura de banda (HBM) e a SRAM do chip, e calcula a atenção exata, sem aproximação [12]. Os ganhos incluíram aceleração de 15% de ponta a ponta no BERT-large e de 3 vezes no GPT-2. O método também viabilizou contextos mais longos, com modelos de melhor qualidade [12].

Esse é um bom exemplo de como a evolução dos LLMs dependeu tanto da implementação em hardware quanto de mudanças matemáticas.

### Mistura de especialistas

Outra linha de evolução atacou a relação entre parâmetros e computação. Modelos de mistura de especialistas (MoE) selecionam parâmetros diferentes para cada entrada, o que resulta em modelos esparsos, com enorme número de parâmetros, mas custo computacional constante [13]. O Switch Transformer simplificou o roteamento dos MoE substituindo a camada feed-forward densa por uma camada esparsa de especialistas. Obteve até 7 vezes mais velocidade de pré-treinamento com os mesmos recursos e chegou a modelos com um trilhão de parâmetros [13]. A estrutura de atenção permanece. O que muda é a subcamada feed-forward, que passa a ser condicional.

## O que a atenção aprende

Uma vantagem secundária apontada desde o artigo original é a interpretabilidade. Os autores observaram que cabeças de atenção individuais aprendem a executar tarefas diferentes, e muitas exibem comportamento relacionado à estrutura sintática e semântica das frases [1]. Um dos exemplos mostrava duas cabeças aparentemente envolvidas na resolução de anáfora, ou seja, em identificar a que palavra um pronome se refere [1].

A pesquisa de interpretabilidade mecanicista avançou essa linha. Pesquisadores da Anthropic descreveram as "cabeças de indução", cabeças de atenção que implementam um algoritmo simples de completar padrões do tipo [A][B] … [A] → [B] [14]. Eles apresentaram evidências de que essas cabeças podem ser o mecanismo da maior parte da aprendizagem em contexto em grandes Transformers. Elas surgem exatamente no mesmo ponto do treino em que há um salto abrupto nessa capacidade [14].

A força da evidência varia com o tamanho do modelo. Para modelos pequenos compostos só de atenção, a evidência é causal e forte. Para modelos maiores com camadas MLP, é correlacional [14]. O achado liga a capacidade mais característica dos LLMs, aprender a partir do prompt, a um circuito concreto construído com o mecanismo de atenção.

## Generalidade, limites e alternativas

A arquitetura provou-se surpreendentemente geral. O Vision Transformer (ViT) mostrou que um Transformer puro, aplicado diretamente a sequências de fragmentos de imagem, tem ótimo desempenho em classificação. Os fragmentos são tratados como tokens, do mesmo modo que palavras [15]. Quando pré-treinado com dados suficientes, o ViT alcançou resultados excelentes em comparação com redes convolucionais de ponta, exigindo menos computação para treinar [15]. Esse resultado ajudou a pavimentar o caminho para os modelos multimodais.

O custo quadrático, porém, continua sendo o calcanhar de Aquiles. Gu e Dao notam que os modelos de fundação são quase universalmente baseados no Transformer. Muitas arquiteturas subquadráticas foram propostas, como atenção linear, convoluções com portas, modelos recorrentes e modelos de espaço de estados, mas não tiveram desempenho equivalente ao da atenção em linguagem [16].

A proposta dos autores, o Mamba, torna os parâmetros do modelo de espaço de estados dependentes da entrada. Isso permite propagar ou esquecer informação seletivamente conforme o token atual [16]. O Mamba oferece cerca de 5 vezes mais vazão na inferência e escala linear com o comprimento da sequência. Seu modelo de 3 bilhões de parâmetros superou Transformers do mesmo tamanho e igualou Transformers com o dobro do tamanho [16].

Se essas alternativas ou híbridos vão deslocar o Transformer é uma questão em aberto. Por ora, o Transformer segue como referência, e a busca por alternativas tem como alvo justamente o custo quadrático da autoatenção.

## Conclusão

O Transformer resolveu dois problemas das redes recorrentes ao mesmo tempo. Eliminou a dependência sequencial que impedia o paralelismo e encurtou para uma constante o caminho entre quaisquer duas posições da sequência [1]. O núcleo é uma operação de poucas linhas, softmax(QKᵀ/√d_k)·V, repetida em várias cabeças e intercalada com redes feed-forward, conexões residuais e normalização [1].

A partir desse núcleo, a área seguiu um percurso relativamente coerente:

- pré-treinar decodificadores para prever o próximo token [3];
- escalar parâmetros e dados segundo leis empíricas [6][7];
- descobrir capacidades de aprendizagem em contexto [5];
- alinhar os modelos com feedback humano [8].

No caminho, o bloco original recebeu pré-normalização, SwiGLU e RoPE [10], atenção agrupada para inferência eficiente [11], implementações cientes do hardware [12] e camadas esparsas de especialistas [13].

O mecanismo de atenção, no entanto, permaneceu essencialmente o de 2017. Essa longevidade é o argumento mais forte de que a ideia central, deixar cada elemento de uma sequência decidir, de forma aprendida e diferenciável, quais outros elementos importam, captura algo fundamental sobre como modelar linguagem e, cada vez mais, outras modalidades.

## Referências

[1] Vaswani, A. et al. "Attention Is All You Need" (2017). https://arxiv.org/abs/1706.03762

[2] Bahdanau, D.; Cho, K.; Bengio, Y. "Neural Machine Translation by Jointly Learning to Align and Translate" (2014/ICLR 2015). https://arxiv.org/pdf/1409.0473

[3] Radford, A. et al. "Improving Language Understanding by Generative Pre-Training" (OpenAI, 2018). https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

[4] Devlin, J. et al. "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" (2018). https://arxiv.org/abs/1810.04805

[5] Brown, T. et al. "Language Models are Few-Shot Learners" (2020). https://arxiv.org/abs/2005.14165

[6] Kaplan, J. et al. "Scaling Laws for Neural Language Models" (2020). https://arxiv.org/abs/2001.08361

[7] Hoffmann, J. et al. "Training Compute-Optimal Large Language Models" (2022). https://arxiv.org/abs/2203.15556

[8] Ouyang, L. et al. "Training language models to follow instructions with human feedback" (2022). https://arxiv.org/abs/2203.02155

[9] Su, J. et al. "RoFormer: Enhanced Transformer with Rotary Position Embedding" (2021). https://arxiv.org/abs/2104.09864

[10] Touvron, H. et al. "LLaMA: Open and Efficient Foundation Language Models" (2023). https://arxiv.org/pdf/2302.13971

[11] Ainslie, J. et al. "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints" (2023). https://arxiv.org/abs/2305.13245

[12] Dao, T. et al. "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness" (2022). https://arxiv.org/abs/2205.14135

[13] Fedus, W.; Zoph, B.; Shazeer, N. "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity" (JMLR, 2022). https://jmlr.org/papers/v23/21-0998.html

[14] Olsson, C. et al. "In-context Learning and Induction Heads" (Anthropic, 2022). https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/

[15] Dosovitskiy, A. et al. "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale" (2020/ICLR 2021). https://huggingface.co/papers/2010.11929

[16] Gu, A.; Dao, T. "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (2023). https://arxiv.org/abs/2312.00752v2