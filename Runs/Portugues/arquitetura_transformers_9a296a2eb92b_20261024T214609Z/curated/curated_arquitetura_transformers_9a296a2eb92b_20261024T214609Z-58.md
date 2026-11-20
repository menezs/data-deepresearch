[referencia=3667345e50c17c08 score=0.141]
# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova 

arXiv:1810.04805 

## What is BERT? 

- Bidirectional Encoder Representations from Transformers 

- A contextualized language model that can be fine-tuned for a variety of tasks 



The two steps of how BERT is developed. You can download the model pre-trained in step 1 (trained on un-annotated data), and only worry about fine-tuning it for step 2. 

## BERT 

● 

> <u>B</u> idirectional <u>E</u> ncoder <u>R epresentations from T ransformers</u> 

- Bidirectional - Uses attention 

○ Attention considers content before and after a word rather than sequentially like an RNN 

- Encoder Representations 

○ Condenses text into a vector that represents its meaning and components (features) 

- Transformers 

   - Layered neural networks which use attention to encode the representations 

3 

## Previous Models: ELMo 

- Creates embeddings based on the context it’s used in (contextualized word-embeddings) 

- ● It is a pair of LSTMs trained to take input vectors and predict the next word in a sequence 

- ● ELMo looks at the entire sentence before assigning each word an embedding 

- ● These vectors are then used as features in a downstream task 





## Previous Models: OpenAI Transformer 

- Often sentences will rely on information significantly distant from each other 

- An RNN may fail to capture this so instead an attention based system is used 

- ● The OpenAI Transformer is a stack of Decoders which are trained to predict the next word in a sequence ○ Decoders sequential data and mask all future information past the target token 

- ● Transfer learning is done by  formatting different problems as if they were sequential and adding a final classifier layer

---

[referencia=3667345e50c17c08 score=0.086]
## Subword Embeddings 

- In the pretraining step, Bert uses WordPiece tokenization 

   - This encodes sub-word information into the language model so that in testing/usage an Out-Of-Vocabulary (OOV) token can still have an embedding 

### The following algorithm is how WordPiece works: 

1. Create a corpus 

2. Define a desired subword vocabulary size 

3. Split word to sequence of characters 

4. Build a language model based on step 3 data 

5. Choose the new word unit out of all the possible ones that increases the likelihood on the training data the most when added to the model. 

6. Repeating step 5 until reaching subword vocabulary size which is defined in step 2 or the likelihood increase falls below a certain threshold. 

Imagine a corpus of ‘walker’, ‘walks’, ‘walked’ 

1. w|a = wa 

2. l|k = lk 

3. wa|lk = walk 

These subwords are selected since they are common in the corpus and thus likely. Now each component, including letters, subwords, and entire words, are included in the dictionary 

Given OOV “walking” the model can use ‘walk’ and ‘ing’ (which it learns from other words) 

## BERT: Transfer Learning 

- In a neural network, each layer gathers different information 

   - Earlier layers extract more general features while later layers get more specific/nuanced features 

- Transfer learning reduces the need for in-domain data 

   - Pre-train a model on a large, general dataset and then fine-tune it for a task using a smaller, specific dataset 

   - ○ Pre-training makes early layers good at extracting general features 

   - Attach new task-specific classification layers to this model, fine-tuning them for a specific task 

   - All previous parameters, which were initialized in pre-training, are then further trained at a fine-tuning learning rate 

   - ○ This is common in computer vision 



13

---

[referencia=3667345e50c17c08 score=0.034]
## BERT: The Next Step 

- OpenAI, by using decoders, goes back to only considering information in 1-direction 

- BERT is instead a stack of encoders that looks at attention in both directions simultaneously ○ To prevent the model from automatically recognizing the target word, it selectively masks (or replaces) 15% of the tokens and is trained to predict the missing term 

- BERT is also trained on predicting likelihood sentence B follows sentence A ○ This likelihood is based on the output vector for a given class label which is appended to the sequence 





## Difference Between Architectures 



## BERT: Input Representation 



## BERT: Input Representation 



## Positional Embedding 

- When using attention, word order is not retained unlike with sequential NN 

● This can lead to ambiguity when comparing tokens within a sentence ○ I <u>do not</u> like the story of the movie, but I <u>do</u> like the cast ○ I do like the story of the movie, but I <u>do not</u> like the cast ○ Same words but different order completely changes sentiment 

● BERT encodes positional embeddings into tokens ○ This encoding uses the same formula as presented in Attention is All You Need ○ pos = position ○ i = dimension ○ d = dimension size of model model

---

[referencia=3667345e50c17c08 score=0.031]
## Conclusion & Limitation 

- BERT builds on several advancements in NLP in recent years 

- BERT presents a new cutting edge for language models than can be quickly applied to a variety of tasks and domains 

○ It especially opens up opportunities on working in low-resource tasks 

- Base BERT has the limitation of only being able to handle 512 tokens at a time, which limits its ability to to work on data sets with larger sample components

---

[referencia=3667345e50c17c08 score=0.029]
## Fine-Tuning : ULM-FiT 

- ULM-FiT introduced convention for transfer learning in language modeling 

A. The model is trained over a large data set B. Each layer of the model is fine tuned using parameters specific to that layer since each layer captures different information a. The triangular learning rate is more aggressive, allowing for less data to make a large impact C. Fine-tunes model for classification task 

a. Concat Pooling: Concatenate as many layers as fit in memory to to retain detailed information b. Gradual Unfreezing: Fine tune a layer at a time to prevent ‘catastrophic forgetting’ 



## BERT: Fine-Tuned for Different Tasks 

- Using fine tuning, BERT can be geared towards a variety of tasks 

- For a given task, tokens are appended into the sequence 

   - The hidden state of this token is output for classification tasks 





## Evaluation: GLUE Tasks 

- <u>General La U Evaluation benchmark</u> nguage nderstanding 

- Collection of diverse language understanding tasks 

   - MNLI: Multi-Genre Language Interference 

   - Entailment classification (Determine if 2 sentence are entailment/contradiction/neutral 

   - ○ QQP: Quora Question Pairs 

      - Determine if 2 questions asked on quora are semantically equivalent 

   - QNLI: Question Natural Language Interference 

      - Stanford Question Answering Dataset converted to classification task 

   - SST-2: Stanford Sentiment Treebank 

   - Single-sentence classification of movie review sentiment 

   - ○ CoLA: Corpus of Linguistic Acceptability 

   - Single sentence classification to see if a sentence is linguistically english 

   - ○ STS-B: Semantic Textual Similarity Benchmark 

      - Determine how similar 2 sentences are by semantic meaning 

   - MRPC: Microsoft Research Paraphrase Corpus 

   - Sentence pairs gathered from the news to determine if they are semantically equivalent 

   - ○ RTE: Recognizing Textual Entailment 

      - Similar to MNLI but less training data 

   - WNLI: Winograd NLI 

      - Small natural language inference dataset

---

[referencia=3667345e50c17c08 score=0.028]
## Evaluation: Glue Results 

- Introduced softmax classification layer 

- Batch size of 32 and 3 epochs 

- Selected best fine-tuning learning rate on Dev set 

- BERT was unstable on some small datasets Large 

○ Performed random restarts that did different fine-tuning data shuffling and classifier layer initialization 



## Evaluation: SQuaD (1.1 & 2.0) 

- Stanford Question Answering Dataset 

   - Collection of 100k crowdsourced Q:A pairs 

   - Given a question and passage from Wikipedia, the task is to predict the answer substring (text span) from the passage 

- Introduce a Start [S] and End [E] vector in fine tuning 

   - Gather probability of a given word Ti being the start or end token for the span by calculating a dot product followed by a softmax over all words in the paragraph 





   - Score of span is calculated by the above formula where j>= i 

   - Training objective is sum of log-likelihoods of the correct start and end positions 

- Squad v2.0 introduces the chance that the text is not in the passage 

   - A null answer has the start and end token at the [CLS] token 



- Compare the probability of null answer vs best non-null answer 

## Evaluation: SWAG 

- Situations With Adversarial Generations dataset 

   - 113k sentence-pair completion examples 

   - Given a sentence, the task is to choose the most plausible continuation among four choices 

- In fine-tuning, they concatenated the given sentence with each of the 4 sentences and labelled accordingly 





## Ablation Studies 





## BERT: Feature Extraction 

- ELMo and Word2Vec both allowed for word vectors to be output and then used for a downstream task 

- ● While fine tuning a model typically works better for an overall task, this feature extraction is useful for quick prototyping and for especially low resource tasks 

- In BERT, we use a combination of hidden layers to create a vector representation 

   - The best combination is dependent on the final task