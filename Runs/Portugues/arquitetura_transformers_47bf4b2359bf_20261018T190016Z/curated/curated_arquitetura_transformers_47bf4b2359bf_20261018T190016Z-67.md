[referencia=2f4185a6336708d8 score=0.857]
inductive bias about the task. Through ablations and controlled trials we show both attention types are essential – the local attention is primarily used to build contextual representations, while the global 

**Long-Document Transformers** Tab. 1 summa- 

attention allows Longformer to build full sequence representations for prediction. 

rizes recent prior work on long documents. Two types of self-attention approaches have been ex- 

We first evaluate Longformer on autoregressive character-level language modeling using a combination of windowed and a new dilated attention pattern, allowing the model to process sequences of up to 32K characters on modern GPUs. We achieve state-of-the-art results on text8 and enwik8 

plored. The first is a left-to-right (ltr) approach that processes the document in chunks moving from left-to-right. While such models have been successful in autoregressive language modeling, they are unsuitable for transfer learning approaches with 

benchmark datasets, demonstrating the effective- 



ness of Longformer in long document modeling. 

Then, to evaluate Longformer’s ability to re- 

place the full self-attention operation of existing pretrained models, we pretrain it with the masked language modeling (MLM) objective, continuing from the RoBERTa (Liu et al., 2019) released checkpoint. After pretraining, we apply it to downstream language tasks through finetuning and 

matrix multiplication. The model with the most similar attention pattern to ours is Sparse Transformer (Child et al., 2019), which uses a form of dilated sliding window of blocks of size 8x8 provided by BlockSparse (Gray et al., 2017). Our implementation (§3) also includes a custom CUDA

---

[referencia=2f4185a6336708d8 score=0.826]
need for task-specific architectures. 

- need for task-specific architectures. Model attention char-LM other pretrain matrix tasks 

- Recent work has addressed the computational in- 

- efficiency of Transformers on long sequences (see Transformer-XL (2019) ltr yes no no Adaptive Span (2019) ltr yes no no 

- Tab. 1). 1).). However, they primarily focus on autoreCompressive (2020) ltr <u>yes</u> no no gressive language modeling (LM), while the appliReformer (2020) sparse yes no no cation of long document transformers to documentSparse (2019) sparse yes no no Routing <u>(2020)</u> sparse <u>yes</u> no no 

- level NLP tasks in the transfer learning setting BP-Transformer (2019) sparse yes MT no (DaiDai and Le,, 2015;; Peters et al.,, 2018;; Howard Blockwise (2019) sparse no <u>QA yes</u> Our Longformer sparse yes multiple yes 

- Tab. 1). 1).). However, they primarily focus on autoregressive language modeling (LM), while the appli- 

- (DaiDai and Le,, 2015;; Peters et al.,, 2018;; Howard and Ruder, 2018; Devlin et al., 2019) has remained 

largely unexplored. We address this gap and show 

Table 1: Summary of prior work on adapting Transformers for long documents. ltr: left-to-right. Longformer’s efficient attention pattern on the encoder network, allowing it to address long document seq2seq tasks such as summarization. We demonstrate the effectiveness of LED on the arXiv 

that Longformer’s attention mechanism can act as a drop-in replacement for the self-attention mechanism in pretrained Transformers, and leads to gains across a suite of document NLP tasks. Longformer’s attention mechanism is a combination of a windowed local-context self-attention and an end task motivated global attention that encodes 

summarization dataset (Cohan et al., 2018). **2 Related Work** 

inductive bias about the task. Through ablations and controlled trials we show both attention types are essential – the local attention is primarily used to build contextual representations, while the global 

**Long-Document Transformers** Tab. 1 summa-

---

[referencia=2f4185a6336708d8 score=0.779]
## **A Implementation Details** 

Implementing Longformer’s dilated sliding window attention requires a form of banded matrix multiplication (matrix multiplication where the output is all zero except certain diagonals) that is not directly supported in existing deep learning libraries like PyTorch/Tensorflow. Fig. 1 compares the runtime and memory of three different ways of implementing it. 

Longformer-loop is a naive implementation that computes each diagonal separately in a loop. It is memory efficient because it only computes the non-zero values, but it is unusably slow. We only use it for testing because it is easy to implement but don’t use it to run experiments. 

Longformer-chunks only supports the nondilated case. It chunks _Q_ and _K_ into overlapping blocks of size _w_ and overlap of size<sup><u>1</u></sup> 2<sup>_w_, multiplies</sup> the blocks, then mask out the diagonals. This is very compute efficient because it uses a single matrix multiplication operation from PyTorch, but it consumes 2x the amount of memory a perfectly optimized implementation should consume because it computes some of the zero values. Because of the compute efficiency, this implementation is most suitable for the pretrain/finetune case. We didn’t find the increase in memory to be a problem for this setting. 

> Longformer-cuda is a custom CUDA kernel that we implement using TVM (Chen et al., 2018). It is a fully functioning implementation of our attention (not limited as Longformer-chunks), it is the most memory efficient, and it is as fast as the highly optimized full self-attention.<sup>10</sup> We mainly use this implementation for the autoregressive language modeling experiments because of the memory efficiency (allows the longest sequences) and the support of dilation (needed for characterLM experiments). 

**Tensor Virtual Machine (TVM)** We build our custom CUDA kernel using TVM (Chen et al., 2018), a deep learning compiler stack that compiles high level description of a function into optimized device-specific code. Using TVM, we describe our banded matrix multiplication in high-level python

---

[referencia=2f4185a6336708d8 score=0.767]
## **5 Pretraining and Finetuning** 

Current state-of-the-art systems for many NLP tasks finetune a pretrained model with task supervision (e.g. BERT). One of our main motivations is to develop such a model suitable for long document tasks. To do so, we pretrained Longformer on a document corpus and finetune it for six tasks, including classification, QA and coreference resolution. The resulting model can process sequences up to 4,096 tokens long (8 times longer than BERT)<sup>5</sup> . 

We pretrain Longformer with masked language modeling (MLM), where the goal is to recover randomly masked tokens in a sequence. Since MLM pretraining is expensive, we continue pretraining from the RoBERTa (Liu et al., 2019) released checkpoint, while only making the minimal 

> 4One caveat is that the ordering of end performance will not agree with that at step 150K. However, this approximation saves the huge cost of running every experiment to completion. 

> 5Sequences up to 16K are possible on current GPUs. 

|Model|base|large|
|---|---|---|
|RoBERTa (seqlen: 512)|1.846|1.496|
|Longformer (seqlen: 4,096)|10.299|8.738|
|+ copy position embeddings|1.957|1.597|
|+ 2K gradient updates|1.753|1.414|
|+ 65K gradient updates|1.705|1.358|
|Longformer (train extra pos. embed. only)|1.850|1.504|



Table 5: MLM BPC for RoBERTa and various pretrained Longformer configurations. 

changes necessary to support Longformer’s attention mechanism. Note that our attention pattern can be plugged into any pretrained transformer model without the need to change the model architecture. 

**Attention Pattern** We use sliding window attention with window size of 512, therefore using the same amount of computation as RoBERTa.<sup>6</sup>

---

[referencia=2f4185a6336708d8 score=0.753]
## **1 Introduction** 

Transformers (Vaswani et al., 2017) have achieved state-of-the-art results in a wide range of natural language tasks including generative language modeling (Dai et al., 2019; Radford et al., 2019) and discriminative language understanding (Devlin et al., 2019). This success is partly due to the self-attention component which enables the network to capture contextual information from the entire sequence. While powerful, the memory and computational requirements of self-attention grow 

> _∗_ Equal contribution. 

> 1https://github.com/allenai/longformer 



Figur ~~<u>e</u>~~ <u>1: Runtime and</u> me ~~<u>m</u>~~ <u>ory of full self-</u> attention and different imple ~~m~~ entations of Longformer ~~’s se~~ l ~~f-~~ a ~~t~~ te ~~n~~ t ~~ion; L~~ ongformer-loop is nonvectorized, Longformer-chunk is vectorized, and Longformer-cuda is a custom cuda kernel implementations. Longformer’s memory u ~~s~~ a ~~g~~ e ~~sca~~ l ~~es~~ linearly <u>with the sequence</u> length, <u>unlike the full</u> self-attention mechanism that runs out of memory for long sequences on current GPUs. Different implementations vary in speed, with the vectorized Longformer-chunk being the fastest. More details are in section 3.2. 

quadratically with sequence length, making it infeasible (or very expensive) to process long sequences. 

To address this limitation, we present Longformer, a modified Transformer architecture with a self-attention operation that scales linearly with the sequence length, making it versatile for processing long documents (Fig 1). This is an advantage for natural language tasks such as long document classification, question answering (QA), and coreference resolution, where existing approaches partition or shorten the long context into smaller sequences that fall within the typical 512 token limit of BERT-style pretrained models. Such partitioning could potentially result in loss of important cross-partition information, and to mitigate this problem, existing methods often rely on complex architectures to address such interactions. On the other hand, our proposed Longformer is able to build contextual representations of the entire context using multiple layers of attention, reducing the 

need for task-specific architectures.

---

[referencia=2f4185a6336708d8 score=0.675]
demonstrate that Longformer consistently outperkernel, but it is more flexible and maintainable than forms RoBERTa on a wide range of document-level BlockSparse which is implemented in C++, and natural language tasks including text classification, designed for a specific version of TensorFlow. We QA, and coreference resolution, achieving state-ofalso introduce additional task motivated global atthe-art results on two of these datasets. tention patterns suitable for common NLP tasks We finally introduce a variant of Longformer (§3) and show they are essential for good perforwhich instead of an encoder-only Transformer mance in the transfer learning setting. architecture, it follows an encoder-decoder arA few models tried tasks other than autoregreschitecture similar to the original Transformer sive language modeling, which is a step forward model (Vaswani et al., 2017), and it is inbecause arguably focusing on language modeling tended for sequence-to-sequence (seq2seq) learnas the primary evaluation has led to the develop- 

A few models tried tasks other than autoregressive language modeling, which is a step forward because arguably focusing on language modeling as the primary evaluation has led to the develop- 

ing (Sutskever et al., 2014). We call this model Longformer-Encoder-Decoder (LED) that uses 

ment of models with limited applicability. BPTransformer (Ye et al., 2019) evaluated on machine 

2 









Figure 2: Comparing the full self-attention pattern and the configuration of attention patterns in our Longformer. 

translation (MT), but didn’t explore the pretrainfinetune setting. Blockwise attention (Qiu et al., 2019) pretrained their models and evaluated on question answering (QA). However, the evaluation is limited as it doesn’t include language modeling, and the QA datasets are of relatively short documents,<sup>2</sup> therefore the effectiveness of this model on long document tasks remains unexplored.

---

[referencia=2f4185a6336708d8 score=0.649]
**Attention Pattern** We use sliding window attention with window size of 512, therefore using the same amount of computation as RoBERTa.<sup>6</sup> 

**Position Embeddings** RoBERTa uses learned absolute position embeddings with the maximum position being 512. To support longer documents, we add extra position embeddings to support up to position 4,096. To leverage RoBERTa’s pretrained weights, instead of randomly initializing the new position embeddings, we initialize them by copying the 512 position embeddings from RoBERTa multiple times as analysis of BERT’s attention heads shows a strong learned bias to attending to local context, including the previous or next token (Clark et al., 2019). Using the copy initialization preserves this local structure everywhere except at the partition boundaries. Despite its simplicity, we found this to be a very effective (see Tab. 5), allowing Longformer pretraining to rapidly converge with a small number of gradient updates. 

**Continued MLM Pretraining** We pretrain Longformer using fairseq (Ott et al., 2019) on a corpus of long documents that we compiled (see Appendix C for corpus details). We train two model sizes, a base model and a large model. Both models are trained for 65K gradient updates with sequences length 4,096, batch size 64 (2<sup>18</sup> tokens), maximum learning rate of 3e-5, linear warmup of 500 steps, followed by a power 3 polynomial decay. The rest of the hyperparameters are the same as RoBERTa. 

Tab. 5 shows the BPC on the development set of our training corpus. The first row shows a 1.846 

> 6Adding dilation on a few heads as in §4.1 hurt performance, likely because it is not compatible with the pretrained RoBERTa weights. Retraining such model from scratch might be needed to improve performance. 

6 

Wordpieces WH TQA HQA ON IMDB HY nate all available context into a single sequence. avg. 1,535 6,589 1,316 506 300 705 Our baseline is a RoBERTa based model 95th pctl. 3,627 17,126 1,889 1,147 705 1,975 breaks the context into the 

Our baseline is a RoBERTa based model that

---

[referencia=2f4185a6336708d8 score=0.638]
# **Longformer: The Long-Document Transformer** 

**Iz Beltagy**<sup>_∗_</sup> **Matthew E. Peters**<sup>_∗_</sup> **Arman Cohan**<sup>_∗_</sup> Allen Institute for Artificial Intelligence, Seattle, WA, USA _{_ beltagy,matthewp,armanc _}_ @allenai.org 

## **Abstract** 

Transformer-based models are unable to process long sequences due to their self-attention operation, which scales quadratically with the sequence length. To address this limitation, we introduce the Longformer with an attention mechanism that scales linearly with sequence length, making it easy to process documents of thousands of tokens or longer. Longformer’s attention mechanism is a drop-in replacement for the standard self-attention and combines a local windowed attention with a task motivated global attention. Following prior work on long-sequence transformers, we evaluate Longformer on character-level language modeling and achieve state-of-the-art results on text8 and enwik8. In contrast to most prior work, we also pretrain Longformer and finetune it on a variety of downstream tasks. Our pretrained Longformer consistently outperforms RoBERTa on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA. We finally introduce the Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset.<sup>1</sup>

---

[referencia=2f4185a6336708d8 score=0.513]
### **Task-specific Models for Long Documents** 

Many task-specific approaches have been developed to workaround the 512 limit of pretrained transformer models like BERT. The simplest approach just truncates the document, commonly used for classification (Xie et al., 2019). Another approach chunks the document into chunks of length 512 (could be overlapping), processes each chunk separately, then combines the activations with a task specific model (Joshi et al., 2019). A third approach popular for multihop and open domain QA tasks uses a two-stage model where the first stage retrieves relevant documents that are passed onto the second stage for answer extraction (Clark and Gardner, 2017; Chen et al., 2017). All of these approaches suffer from information loss due to truncation or cascading errors from the two stage approach. In contrast, Longformer can process long sequences without truncating or chunking, allowing us to adopt a much simpler approach that concatenates the available context and processes it in a single pass. 

A few contemporaneous works<sup>3</sup> have explored similar ideas to Longformer using local + global attention in Transformers, and pre-training it for long document natural language tasks. In particular, ETC (Ainslie et al., 2020) uses a similar local + global attention instead of full self-attention to scale Transformers to long documents. Different from Longformer, ETC uses relative position em- 

> 2SQuAD contexts typically fit within the 512 limit, and MRQA is constructed by dropping long-document examples. 3All were published on arXiv after Longformer. 

beddings (which we only used for the Autoregressive LM setting), introduces an additional training objective (CPC loss) for pre-training, and configures global attention in a slightly different way. It shows strong results on several tasks including reading comprehension and classification. GMAT (Gupta and Berant, 2020) uses a similar idea of few global locations in the input serving as global memory. BigBird (Zaheer et al., 2020) is an extension over ETC with evaluation on additional tasks, including summarization. Importantly, through theoretical analysis, BigBird shows that sparse Transformers are universal approximators of sequence functions and preserve these properties of the full self-attention.

---

[referencia=2f4185a6336708d8 score=0.504]
### **3.2 Implementation** 

In regular transformers, attention scores are computed as in Eqn. 1. The expensive operation is the matrix multiplication _QK_<sup>_T_</sup> because both _Q_ and _K_ have _n_ (sequence length) projections. For Longformer, the dilated sliding window attention computes only a fixed number of the diagonals of _QK_<sup>_T_</sup> . As shown in Fig. 1, this results in a linear increase in memory usage compared to quadratic increase for full self-attention. However, implementing it requires a form of banded matrix multiplication that is not supported in existing deep learning libraries like PyTorch/Tensorflow. Fig. 1 compares the performance of three different ways of implementing it: loop is a memory efficient PyTorch implementation that supports dilation but is unusably slow and only used for testing; chunks only supports the non-dilated case and is used for the pretraining/finetuning setting; and cuda is our fully functioning highly optimized custom CUDA kernel implemented using TVM (Chen et al., 2018) and used for the language modeling experiments (see Appendix A for more details).

---

[referencia=2f4185a6336708d8 score=0.495]
## **7 Longformer-Encoder-Decoder (LED)** 

The original Transformer (Vaswani et al., 2017) consisted of an encoder-decoder architecture, intended for sequence-to-sequence tasks (Sutskever et al., 2014), such as summarization and translation. While encoder-only Transformers are effective on a variety of NLP tasks, pre-trained encoderdecoder Transformer models (e.g. BART (Lewis et al., 2020) and T5 (Raffel et al., 2020)) have achieved strong results on tasks like summarization. Yet, such models can’t efficiently scale to seq2seq tasks with longer inputs. 

To facilitate modeling long sequences for seq2seq learning, we propose a Longformer variant that has both the encoder and decoder Transformer stacks but instead of the full self-attention in the encoder, it uses the efficient local+global attention pattern of the Longformer. The decoder uses the full self-attention to the entire encoded tokens and to previously decoded locations. We call this model Longformer-Encoder-Decoder (LED) which scales linearly with the input. Since pre-training LED is expensive, we initialize LED parameters from the BART, and follow BART’s exact architecture in terms of number of layers and hidden sizes. The only difference is that to process longer inputs, we extend position embedding to 16K tokens (up from BART’s 1K tokens) and we initialize the new position embedding matrix by repeatedly copying BART’s 1K position embeddings 16 times as in Section 5 for RoBERTa. Following BART, we release two model sizes, LED-base and LED-large, which respectively have 6 and 12 layers in both encoder and decoder stacks. 

We evaluate LED on the summarization task using the arXiv summarization dataset (Cohan et al., 2018) which focuses on long document summarization in the scientific domain. The 90th percentile of document lengths is 14.5K tokens, making it an appropriate testbed for evaluating LED. LED’s encoder reads the document and its decoder generates the output summary. The encoder uses local attention with window size 1,024 tokens and global attention on the first <s> token. The decoder uses full attention to the entire encoder and previously decoded locations. As standard in seq2seq models, LED is trained using teacher forcing on gold training summaries and uses beam search at inference.

---

[referencia=2f4185a6336708d8 score=0.491]
Figure 3: ROUGE-1 and ROUGE-2 of LED when varying the input size (arXiv validation set). 

pre-training. We observe that LED achieves stateof-the-art results on arXiv, slightly outperforming BigBird (Zaheer et al., 2020). Note that the BigBird summarization model supports sequence length of 4K tokens but starts from and continues pre-training Pegasus (Zhang et al., 2020), a model specifically designed and pre-trained for summarization. With no pre-training or task-specific initialization, but with ability to process longer inputs, LED can slightly outperform BigBird. Further improvements should be possible through pre-training of LED. Fig. 3 further illustrates the importance of sequence length showing the ablility to process longer input significantly improves the results. 

## **8 Conclusion and Future Work** 

We present Longformer, a transformer-based model that is scalable for processing long documents and that makes it easy to perform a wide range of document-level NLP tasks without chunking/shortening the long input and without complex architecture to combine information across these chunks. Longformer employs an attention pattern that combines local and global information while also scaling linearly with the sequence length. Longformer achieves state-of-the-art results on the character-level language modeling tasks of text8 

and enwik8. When pretrained, Longformer consistently outperforms RoBERTa on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA. We further present LED, an encoder-decoder variant of Longformer for modeling sequence-to-sequence tasks, and achieve stateof-the-art results on the arXiv long document summarization task. For future work, we would like to study other pretraining objectives, especially for LED, increase the sequence length, and explore other tasks that might benefit from our model. 

## **Acknowledgment** 

We would like to thank Noah Smith, Dan Weld, Dirk Groeneveld, Kyle Lo, Daniel King and Doug Downey for helpful discussions and feedback, and the AI2 infrastructure team for technical support.

---

[referencia=2f4185a6336708d8 score=0.481]
model from Joshi et al. (2019), a modification of 

7We use the full version of TriviaQA and HotpotQA, not the simplified versions in MRQA (Fisch et al., 2019). 

7 

|||QA||Coref.|Cla|ssifcation|
|---|---|---|---|---|---|---|
|Model|WikiHop|TriviaQA|HotpotQA|OntoNotes|IMDB|Hyperpartisan|
|RoBERTa-base|72.4|74.3|63.5|78.4|95.3|87.4|
|Longformer-base|**75.0**|**75.2**|**64.4**|**78.6**|**95.7**|**94.8**|



Table 7: Summary of finetuning results on QA, coreference resolution, and document classification. Results are on the development sets comparing our Longformer-base with RoBERTa-base. TriviaQA, Hyperpartisan metrics are F1, WikiHop and IMDB use accuracy, HotpotQA is joint F1, OntoNotes is average F1. 

the system from Lee et al. (2018) to replace ELMo with BERT. The Longformer system is a straightforward adaption of the baseline model by replacing RoBERTa with Longformer and extending the sequence length. We didn’t use global attention for this task. 

|Model|WikiHop|TriviaQA|HotpotQA|
|---|---|---|---|
|Current<sup>_∗_</sup>SOTA|78.3|73.3|**74.2**|
|Longformer-large|**81.9**|**77.3**|73.2|



Table 8: Leaderboard results of Longformer-large at time of submission (May 2020). All numbers are F1 scores.

---

[referencia=2f4185a6336708d8 score=0.472]
## **3 Longformer** 

The original Transformer model has a self-attention component with _O_ ( _n_<sup>2</sup> ) time and memory complexity where _n_ is the input sequence length. To address this challenge, we sparsify the full self-attention matrix according to an “attention pattern” specifying pairs of input locations attending to one another. Unlike the full self-attention, our proposed attention pattern scales linearly with the input sequence, making it efficient for longer sequences. This section discusses the design and implementation of this attention pattern.

---

[referencia=2f4185a6336708d8 score=0.464]
### **6.5 Ablations on WikiHop** 

Tab. 10 presents an ablation study for WikiHop on the development set. All results use Longformerbase, fine-tuned for five epochs with identical hyperparameters except where noted. Longformer benefits from longer sequences, global attention, separate projection matrices for global attention, MLM pretraining, and longer training. In addition, when configured as in RoBERTa-base (seqlen: 512, and _n_<sup>2</sup> attention) Longformer performs slightly worse then RoBERTa-base, confirming that performance gains are not due to additional pretraining. Performance drops slightly when using the RoBERTa model pretrained when only unfreezing the additional position embeddings, showing that Longformer can learn to use long range context in task specific fine-tuning with large training datasets such as WikiHop. 

> 9At submission time, May 2020. Later, BigBird (Zaheer et al., 2020) improved leaderboard results on these datasets. There are confounding factors such as using 16X more compute in BigBird’s pretraining compared with Longformer, potentially affecting the performance.

---

[referencia=2f4185a6336708d8 score=0.448]
## **D Task specific model details** 

All the QA and classification models are implemented using PyTorch-Lightning<sup>14</sup> . We use the official train/dev/test splits of all datasets except for the Hyperpartisan news which we randomely split into 80/10/10 for train/dev/test. 

**WikiHop** Instances in WikiHop consist of: a question, answer candidates (ranging from two candidates to 79 candidates), supporting contexts (ranging from three paragraphs to 63 paragraphs), and the correct answer. The dataset does not provide any intermediate annotation for the multihop reasoning chains, requiring models to instead infer them from the indirect answer supervision. 

To prepare the data for input to Longformer and RoBERTa, we first tokenize the question, answer candidates, and support contexts using RoBERTa’s wordpiece tokenizer. Then we concatenate the question and answer candidates with special tokens as [q] question [/q] [ent] candidate1 [/ent] ... [ent] candidateN [/ent]. The contexts are also concatenated using RoBERTa’s document delimiter tokens as separators: </s> context1 </s> ... </s> contextM </s>. The special tokens [q], [/q], [ent], [/ent] were added to the RoBERTa vocabulary and randomly initialized before task finetuning. 

> 14https://github.com/PyTorchLightning/ pytorch-lightning 

After preparing the input data, we compute activations from the top layer of each model as follows. We take the question and answer candidates and concatenate them to as much context as possible up to the model sequence length (512 for RoBERTa, 4,096 for Longformer), run the sequence through the model, collect the output activations, and repeat until all of the context is exhausted (for all models except Longformer-large, where we just include the first 4,096 length sequence due to memory requirements). Then all activations for all chunks are concatenated into one long sequence. In the case of Longformer, we use global attention to the entire question and answer candidate sequence. 

For prediction, we attach a linear layer to each [ent] that outputs a single logit, average over all logits for each candidate across the chunks, apply a softmax and use the cross entropy loss with the correct answer candidate.

---

[referencia=2f4185a6336708d8 score=0.429]
### **4.2 Experiment Setup** 

To compare to prior work we focus on characterlevel LM (text8 and enwik8; Mahoney, 2009). 

**Training** Ideally, we would like to train our model on the largest window size and sequence length we can fit in a modern GPU memory. However, we found that the model needs a large number of gradient updates to learn the local context first, before learning to utilize longer context. To accommodate this, we adopt a staged training procedure where we increase the attention window size and sequence length across multiple training phases. In particular, in the first phase we start with a short sequence length and window size, then on each subsequent phase, we double the window size and the sequence length, and halve the learning rate. This makes training fast, while keeping the slow part (longest sequences and window sizes) to the end. We train the model over 5 total phases with starting sequence length of 2,048 and ending sequence length of 23,040 on the last phase (see Appendix B for detailed configurations of each phase, and for all other hyperparameters). 

|Model|#Param|Dev|Test|
|---|---|---|---|
|**Dataset**text8||||
|T12 (Al-Rfou et al.,2018)|44M|-|1.18|
|Adaptive (Sukhbaatar et al.,2019)|38M|1.05|1.11|
|BP-Transformer (Ye et al.,2019)|39M|-|1.11|
|Our Longformer|41M|1.04|**1.10**|
|**Dataset**enwik8||||
|T12 (Al-Rfou et al.,2018)|44M|-|1.11|
|Transformer-XL (Dai et al.,2019)|41M|-|1.06|
|Reformer (Kitaev et al.,2020)|-|-|1.05|
|Adaptive (Sukhbaatar et al.,2019)|39M|1.04|1.02|
|BP-Transformer (Ye et al.,2019)|38M|-|1.02|
|Our Longformer|41M|1.02|**1.00**|



Table 2: _Small_ model BPC on text8 & enwik8

---

[referencia=2f4185a6336708d8 score=0.406]
8 

|Model|ans.|supp.|joint|
|---|---|---|---|
|TAP 2 (ensemble) (Glaß et al.,2019)|79.8|86.7|70.7|
|SAE (Tu et al.,2019)|79.6|86.7|71.4|
|Quark (dev) (Groeneveld et al.,2020)|81.2|87.0|72.3|
|C2F Reader (Shao et al.,2020)|81.2|87.6|72.8|
|Longformer-large|81.3|88.3|73.2|
|ETC-large<sup>_†_ </sup>(Ainslie et al.,2020)<br>|81.2|89.1|73.6|
|GSAN-large<sup>_†_</sup>|81.6|88.7|73.9|
|HGN-large (Fang et al.,2020)|82.2|88.5|74.2|



Table 9: HotpotQA results in distractor setting test set. Quark’s test results are not available. All numbers are F1 scores.<sup>_†_</sup> shows contemporaneous leaderboard submissions. 

|Model|Accuracy /∆|
|---|---|
|Longformer (seqlen: 4,096)|73.8|
|RoBERTa-base (seqlen: 512)|72.4 / -1.4|
|Longformer (seqlen: 4,096, 15 epochs)<br>|75.0 / +1.2|
|Longformer (seqlen: 512, attention: _n_<sup>2</sup>)|71.7 / -2.1|
|Longformer (seqlen: 2,048)|73.1 / -0.7|
|Longformer (no MLM pretraining)|73.2 / -0.6|
|Longformer (no linear proj.)|72.2 / -1.6|
|Longformer (no linear proj. no global atten.|)<br>65.5 / -8.3|
|Longformer (pretrain extra position embed.|only)<br>73.5 / -0.3|



Table 10: WikiHop development set ablations

---

[referencia=2f4185a6336708d8 score=0.338]
### **6.4 Results** 

**Main Result** Tab. 7 summarizes the results of all our finetuning experiments. We observe that Longformer consistently outperforms the RoBERTa baseline. Its performance gain is especially obvious for tasks that require long context such as WikiHop and Hyperpartisan. For TriviaQA, the improvement is more modest as the local context is often sufficient to answer the question. In the case of HotpotQA, the supporting fact auxiliary supervision allows models to easily find relevant contexts and then focus on local context, leading to smaller gains. This is contrasted with WikiHop that only includes distant supervision of intermediate reasoning chains, where our approach excels by reasoning over the entire context. On the IMDB and OntoNotes datasets the performance gains are smaller. For IMDB, the majority of the dataset consists of short documents and thus it is expected to see smaller improvements. For OntoNotes, we 

> 8For Hyperpartisan we split the training data into 80/10/10 train/dev/test sets, and report mean F1 across five seeds. 

**Longformer-large for QA** We also evaluate the performance of Longformer-large on long context QA tasks. Tab. 8 shows that our Longformer-large achieves new state-of-the-art results<sup>9</sup> on WikiHop and TriviaQA by large margins (3.6 and 4 points respectively), and for HotpotQA, it underperforms the current state-of-the-art (Fang et al., 2020) by a point. Tab. 9 shows the detailed results of HotpotQA compared with published and unpublished concurrent models. Longformer places second on the published leaderboard, outperforming all other published results except for HGN (Fang et al., 2020). All published top performing models in this task (Tu et al., 2019; Fang et al., 2020; Shao et al., 2020) use GNNs (Kipf and Welling, 2017) or graph network of entities, which seem to encode an important inductive bias for the task and can potentially improve our results further. Nevertheless, Longformer performs strongly outperforming all other methods including the recent non-GNN methods (Glaß et al., 2019; Shao et al., 2020; Groeneveld et al., 2020). 

8

---

[referencia=2f4185a6336708d8 score=0.252]
Our baseline is a RoBERTa based model that 





ing. Traininig for 2K steps improves BPC from 1.957 to 1.753, which further decreases to 1.705 af- 



and only training the new position embeddings. The motivation for this configuration is to perfectly preserve the RoBERTa performance on short documents. This configuration has a BPC of 1.850 (down from 1.957 at initialization), but higher than 

vant and the rest are distractors. We use a two-stage 

model that first selects the most relevant paragraphs then passes them to a second stage for answer extraction. Both stages concatenate question and context into one sequence, run it through Longformer, then use task-specific prediction layers. We train 

1.705 where all the weights are trainable. 

the models in a multi-task way to predict relevant paragraphs, evidence sentences, answer spans and question types (yes/no/span) jointly. Note that this 

**6 Tasks** We apply Longformer to multiple long document 

tasks, including QA, coreference resolution and classification. Tab. 6 shows the evaluation datasets have contexts significantly longer than 512 wordpieces. Our primary goal is to evaluate whether our attention mechanism can act as a replacement for the standard self-attention mechanism in 

model is simpler than recent SOTA models that include complex task-specific architectures (e.g., (Tu et al., 2019; Chen et al., 2019; Tu et al., 2020; 

Groeneveld et al., 2020)). See Appendix D for further details about the models and hyperparameters. 



in evaluating whether we can replace complicated task specific models necessitated by BERT’s limited context with simpler models that just concate- 

model from Joshi et al. (2019), a modification of 

7We use the full version of TriviaQA and HotpotQA, not the simplified versions in MRQA (Fisch et al., 2019). 

7