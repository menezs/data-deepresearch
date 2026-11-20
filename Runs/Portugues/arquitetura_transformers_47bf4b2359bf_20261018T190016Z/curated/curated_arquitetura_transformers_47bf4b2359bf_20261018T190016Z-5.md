[referencia=887da5f02141c29f score=0.739]
in our empirical study. For a broader literature review, we recommend a recent survey by Ruder et al. (2019). 

We systematically study these contributions by taking a reasonable baseline (described 

in Section 3.1) and altering one aspect of the setup at a time. For example, in Section 3.3 we measure the performance of different unsupervised objectives while keeping the rest of our experimental pipeline fixed. This “coordinate ascent” approach might miss second-order 

effects (for example, some particular unsupervised objective may work best on a model larger than our baseline setting), but performing a combinatorial exploration of all of the factors in our study would be prohibitively expensive. In future work, we expect it could be fruitful to more thoroughly consider combinations of the approaches we study. 

Our goal is to compare a variety of different approaches on a diverse set of tasks while keeping as many factors fixed as possible. In order to satisfy this aim, in some cases we do not exactly replicate existing approaches. For example, “encoder-only” models like BERT (Devlin et al., 2018) are designed to produce a single prediction per input token or a single prediction for an entire input sequence. This makes them applicable for classification or span prediction tasks but not for generative tasks like translation or abstractive summarization. 

As such, none of the model architectures we consider are identical to BERT or consist of an encoder-only structure. Instead, we test approaches that are similar in spirit—for example, we consider an analogous objective to BERT’s “masked language modeling” objective in 

10 

Exploring the Limits of Transfer Learning 

Section 3.3 and we consider a model architecture that behaves similarly to BERT on text classification tasks in Section 3.2. 

After outlining our baseline experimental setup in the following subsection, we undertake an empirical comparison of model architectures (Section 3.2), unsupervised objectives (Section 3.3), pre-training data sets (Section 3.4), transfer approaches (Section 3.5), and scaling (Section 3.6). At the culmination of this section, we combine insights from our study with scale to obtain state-of-the-art results in many tasks we consider (Section 3.7).

---

[referencia=32f3c7d144f036a0 score=0.626]
## **3 BERT** 

We introduce BERT and its detailed implementation in this section. There are two steps in our framework: _pre-training_ and _fine-tuning_ . During pre-training, the model is trained on unlabeled data over different pre-training tasks. For finetuning, the BERT model is first initialized with the pre-trained parameters, and all of the parameters are fine-tuned using labeled data from the downstream tasks. Each downstream task has separate fine-tuned models, even though they are initialized with the same pre-trained parameters. The question-answering example in Figure 1 will serve as a running example for this section. 

A distinctive feature of BERT is its unified architecture across different tasks. There is mini- 

mal difference between the pre-trained architec- 

**Model Architecture** BERT’s model architecture is a multi-layer bidirectional Transformer encoder based on the original implementation described in Vaswani et al. (2017) and released in the tensor2tensor library.<sup>1</sup> Because the use of Transformers has become common and our implementation is almost identical to the original, we will omit an exhaustive background description of the model architecture and refer readers to Vaswani et al. (2017) as well as excellent guides such as “The Annotated Transformer.”<sup>2</sup> 

In this work, we denote the number of layers (i.e., Transformer blocks) as _L_ , the hidden size as _H_ , and the number of self-attention heads as _A_ .<sup>3</sup> We primarily report results on two model sizes: **BERTBASE** (L=12, H=768, A=12, Total Parameters=110M) and **BERTLARGE** (L=24, H=1024, A=16, Total Parameters=340M). 

BERTBASE was chosen to have the same model size as OpenAI GPT for comparison purposes. Critically, however, the BERT Transformer uses bidirectional self-attention, while the GPT Transformer uses constrained self-attention where every token can only attend to context to its left.<sup>4</sup> 

> 1https://github.com/tensorflow/tensor2tensor 

> 2http://nlp.seas.harvard.edu/2018/04/03/attention.html 

> 3In all cases we set the feed-forward/filter size to be 4 _H_ ,

---

[referencia=32f3c7d144f036a0 score=0.333]
layer in the output. We use the representation of the first sub-token as the input to the token-level 

To ablate the fine-tuning approach, we apply the feature-based approach by extracting the activations from one or more layers _without_ fine-tuning any parameters of BERT. These contextual embeddings are used as input to a randomly initialized two-layer 768-dimensional BiLSTM before the classification layer. 

Results are presented in Table 7. BERTLARGE performs competitively with state-of-the-art methods. The best performing method concatenates the token representations from the top four hidden layers of the pre-trained Transformer, which is only 0.3 F1 behind fine-tuning the entire model. This demonstrates that BERT is effective for both finetuning and feature-based approaches. 

## **6 Conclusion** 

|Hy|perpar|ams||Dev Se|t Accura|cy|
|---|---|---|---|---|---|---|
|#L|#H|#A|LM (ppl)|MNLI-m|MRPC|SST-2|
|3|768|12|5.84|77.9|79.8|88.4|
|6|768|3|5.24|80.6|82.2|90.7|
|6|768|12|4.68|81.9|84.8|91.3|
|12|768|12|3.99|84.4|86.7|92.9|
|12|1024|16|3.54|85.7|86.9|93.3|
|24|1024|16|3.23|86.6|87.8|93.7|



Table 6: Ablation over BERT model size. #L = the number of layers; #H = hidden size; #A = number of attention heads. “LM (ppl)” is the masked LM perplexity of held-out training data. 

Recent empirical improvements due to transfer learning with language models have demonstrated that rich, unsupervised pre-training is an integral part of many language understanding systems. In particular, these results enable even low-resource tasks to benefit from deep unidirectional architectures. Our major contribution is further generalizing these findings to deep _bidirectional_ architectures, allowing the same pre-trained model to successfully tackle a broad set of NLP tasks.

---

[referencia=32f3c7d144f036a0 score=0.318]
We organize the appendix into three sections: 

Compared to standard langauge model training, 

the masked LM only make predictions on 15% of 

• Additional implementation details for BERT are presented in Appendix A; 

tokens in each batch, which suggests that more pre-training steps may be required for the model 



<!-- Start of picture text -->
BERT (Ours) OpenAI GPT ELMo<br> T1 T2 ... TN  T1 T2 ...  TN  T1 T2 ...  TN<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br>Trm Trm ... Trm Trm Trm ... Trm<br>Lstm Lstm ... Lstm Lstm Lstm ... Lstm<br> E1 E2 ...  EN  E1 E2 ...  EN  E1 E2 ...  EN<br><!-- End of picture text -->

Figure 3: Differences in pre-training model architectures. BERT uses a bidirectional Transformer. OpenAI GPT uses a left-to-right Transformer. ELMo uses the concatenation of independently trained left-to-right and right-toleft LSTMs to generate features for downstream tasks. Among the three, only BERT representations are jointly conditioned on both left and right context in all layers. In addition to the architecture differences, BERT and OpenAI GPT are fine-tuning approaches, while ELMo is a feature-based approach. 

to converge. In Section C.1 we demonstrate that MLM does converge marginally slower than a leftto-right model (which predicts every token), but the empirical improvements of the MLM model far outweigh the increased training cost. 

**Next Sentence Prediction** The next sentence prediction task can be illustrated in the following examples. 

Input = [CLS] the man went to [MASK] store [SEP] he bought a gallon [MASK] milk [SEP] Label = IsNext 

Input = [CLS] the man [MASK] to the store [SEP] penguin [MASK] are flight ##less birds [SEP] Label = NotNext

---

[referencia=887da5f02141c29f score=0.317]
- Figure 4: Schematics of the Transformer architecture variants we consider. In this diagram, blocks represent elements of a sequence and lines represent attention visibility. Different colored groups of blocks indicate different Transformer layer stacks. Dark grey lines correspond to fully-visible masking and light grey lines correspond to causal masking. We use “.” to denote a special end-of-sequence token that represents the end of a prediction. The input and output sequences are represented as _x_ and _y_ respectively. Left: A standard encoder-decoder architecture uses fullyvisible masking in the encoder and the encoder-decoder attention, with causal masking in the decoder. Middle: A language model consists of a single Transformer layer stack and is fed the concatenation of the input and target, using a causal mask throughout. Right: Adding a prefix to a language model corresponds to allowing fully-visible masking over the input. 

obtain the model’s prediction for this example, the model would be fed the prefix “translate English to German: That is good. target:” and would be asked to generate the remainder of the sequence autoregressively. In this way, the model can predict an output sequence given an input, which satisfies the needs of text-to-text tasks. This approach was recently used to show that language models can learn to perform some text-to-text tasks without supervision (Radford et al., 2019). 

A fundamental and frequently cited drawback of using a language model in the textto-text setting is that causal masking forces the model’s representation of the _i_ th entry of the input sequence to only depend on the entries up until _i_ . To see why this is potentially disadvantageous, consider the text-to-text framework where the model is provided with a prefix/context before being asked to make predictions (e.g., the prefix is an English sentence and the model is asked to predict the German translation). With fully causal masking, the model’s representation of a prefix state can only depend on prior entries of the prefix. So, when predicting an entry of the output, the model will attend to a representation of the prefix that is unnecessarily limited. Similar arguments have been made against using a unidirectional recurrent neural network encoder in sequence-to-sequence models (Bahdanau et al., 2015). 

17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.158]
### **4.1 Takeaways** 

- **Text-to-text** Our text-to-text framework provides a simple way to train a single model on a wide variety of text tasks using the same loss function and decoding procedure. We showed how this approach can be successfully applied to generative tasks like abstractive summarization, classification tasks like natural language inference, and even regression tasks like STS-B. In spite of its simplicity, we found the text-totext framework obtained comparable performance to task-specific architectures and ultimately produced state-of-the-art results when combined with scale. 

- **Architectures** While some work on transfer learning for NLP has considered architectural variants of the Transformer, we found the original encoder-decoder form worked best in our text-to-text framework. Though an encoder-decoder model uses twice as many parameters as “encoder-only” (e.g. BERT) or “decoder-only” (language model) architectures, it has a similar computational cost. We also showed that sharing the parameters in the encoder and decoder did not result in a substantial performance drop while halving the total parameter count. 

41 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu

---

[referencia=887da5f02141c29f score=0.123]
### 3.2.1 Model Structures 

A major distinguishing factor for different architectures is the “mask” used by different attention mechanisms in the model. Recall that the self-attention operation in a Transformer takes a sequence as input and outputs a new sequence of the same length. Each entry of the output sequence is produced by computing a weighted average of entries of the input sequence. Specifically, let _yi_ refer to the _i_ th element of the output sequence and _xj_ refer to the _j_ th entry of the input sequence. _yi_ is computed as<sup>�</sup> _j_<sup>_wi,jxj_,where</sup><sup>_wi,j_isthescalar</sup> weight produced by the self-attention mechanism as a function of _xi_ and _xj_ . The attention mask is then used to zero out certain weights in order to constrain which entries of the input can be attended to at a given output timestep. Diagrams of the masks we will consider are shown in Figure 3. For example, the causal mask (Figure 3, middle) sets any _wi,j_ to zero if _j > i_ . 

The first model structure we consider is an an encoder-decoder Transformer, which consists of two layer stacks: The encoder, which is fed an input sequence, and the decoder, which produces a new output sequence. A schematic of this architectural variant is shown in the left panel of Figure 4. 

The encoder uses a “fully-visible” attention mask. Fully-visible masking allows a selfattention mechanism to attend to any entry of the input when producing each entry of its output. We visualize this masking pattern in Figure 3, left. This form of masking is appropriate when attending over a “prefix”, i.e. some context provided to the model that is later used when making predictions. BERT (Devlin et al., 2018) also uses a fully-visible masking pattern and appends a special “classification” token to the input. BERT’s output 

15 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 



<!-- Start of picture text -->

---

[referencia=887da5f02141c29f score=0.123]
### **2.1 Model** 

Early results on transfer learning for NLP leveraged recurrent neural networks (Peters et al., 2018; Howard and Ruder, 2018), but it has recently become more common to use models based on the “Transformer” architecture (Vaswani et al., 2017). The Transformer was initially shown to be effective for machine translation, but it has subsequently been used in a wide variety of NLP settings (Radford et al., 2018; Devlin et al., 2018; McCann et al., 2018; Yu et al., 2018). Due to its increasing ubiquity, all of the models we study are based on the Transformer architecture. Apart from the details mentioned below and the variants we explore in Section 3.2, we do not deviate significantly from this architecture as originally proposed. Instead of providing a comprehensive definition of this model, we refer the interested reader to the original paper (Vaswani et al., 2017) or follow-up tutorials<sup>3,4</sup> for a more detailed introduction. 

The primary building block of the Transformer is self-attention (Cheng et al., 2016). Self-attention is a variant of attention (Graves, 2013; Bahdanau et al., 2015) that processes a sequence by replacing each element by a weighted average of the rest of the sequence. The original Transformer consisted of an encoder-decoder architecture and was intended for sequence-to-sequence (Sutskever et al., 2014; Kalchbrenner et al., 2014) tasks. It has recently also become common to use models consisting of a single Transformer layer stack, with varying forms of self-attention used to produce architectures appropriate for language modeling (Radford et al., 2018; Al-Rfou et al., 2019) or classification and span prediction tasks (Devlin et al., 2018; Yang et al., 2019). We empirically explore these architectural variants in Section 3.2.

---

[referencia=887da5f02141c29f score=0.122]
17 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 

This issue can be avoided in a Transformer-based language model simply by changing the masking pattern. Instead of using a causal mask, we use fully-visible masking during the prefix portion of the sequence. This masking pattern and a schematic of the resulting “prefix LM” (the third model structure we consider) are illustrated in the rightmost panels of Figures 3 and 4, respectively. In the English to German translation example mentioned above, fully-visible masking would be applied to the prefix “translate English to German: That is good. target:” and causal masking would be used during training for predicting the target “Das ist gut.” Using a prefix LM in the text-to-text framework was originally proposed by Liu et al. (2018). More recently, Dong et al. (2019) showed that this architecture is effective on a wide variety of text-to-text tasks. This architecture is similar to an encoder-decoder model with parameters shared across the encoder and decoder and with the encoder-decoder attention replaced with full attention across the input and target sequence. 

We note that when following our text-to-text framework, the prefix LM architecture closely resembles BERT (Devlin et al., 2018) for classification tasks. To see why, consider an example from the MNLI benchmark where the premise is “I hate pigeons.”, the hypothesis is “My feelings towards pigeons are filled with animosity.” and the correct label is “entailment”. To feed this example into a language model, we would transform it into the sequence “mnli premise: I hate pigeons. hypothesis: My feelings towards pigeons are filled with animosity. target: entailment”. In this case, the fully-visible prefix would correspond to the entire input sequence up to the word “target:”, which can be seen as being analogous to the “classification” token used in BERT. So, our model would have full visibility over the entire input, and then would be tasked with making a classification by outputting the word “entailment”. It is easy for the model to learn to output one of the valid class labels given the task prefix (“mnli” in this case). As such, the main difference between a prefix LM and the BERT architecture is that the classifier is simply integrated into the output layer of the Transformer decoder in the prefix LM.

---

[referencia=32f3c7d144f036a0 score=0.111]
### **A.4 Comparison of BERT, ELMo ,and OpenAI GPT** 

Here we studies the differences in recent popular representation learning models including ELMo, OpenAI GPT and BERT. The comparisons between the model architectures are shown visually in Figure 3. Note that in addition to the architecture differences, BERT and OpenAI GPT are finetuning approaches, while ELMo is a feature-based approach. 

The most comparable existing pre-training method to BERT is OpenAI GPT, which trains a left-to-right Transformer LM on a large text corpus. In fact, many of the design decisions in BERT were intentionally made to make it as close to GPT as possible so that the two methods could be minimally compared. The core argument of this work is that the bi-directionality and the two pretraining tasks presented in Section 3.1 account for the majority of the empirical improvements, but we do note that there are several other differences between how BERT and GPT were trained: 

- GPT is trained on the BooksCorpus (800M words); BERT is trained on the BooksCorpus (800M words) and Wikipedia (2,500M words). 

- GPT uses a sentence separator ([SEP]) and classifier token ([CLS]) which are only introduced at fine-tuning time; BERT learns [SEP], [CLS] and sentence A/B embeddings during pre-training. 

- GPT was trained for 1M steps with a batch size of 32,000 words; BERT was trained for 1M steps with a batch size of 128,000 words. 

- GPT used the same learning rate of 5e-5 for all fine-tuning experiments; BERT chooses a task-specific fine-tuning learning rate which performs the best on the development set. 

To isolate the effect of these differences, we perform ablation experiments in Section 5.1 which demonstrate that the majority of the improvements are in fact coming from the two pre-training tasks and the bidirectionality they enable.

---

[referencia=2cab3ea10b8b7ae2 score=0.105]
Another approach to increasing generality and transfer-learning capability in language models is multi-task learning [Car97], which fine-tunes on a mixture of downstream tasks together, rather than separately updating the weights for each one. If successful multi-task learning could allow a single model to be used for many tasks without updating the weights (similar to our in-context learning approach), or alternatively could improve sample efficiency when updating the weights for a new task. Multi-task learning has shown some promising initial results [LGH<sup>+</sup> 15, LSP<sup>+</sup> 18] and multi-stage fine-tuning has recently become a standardized part of SOTA results on some datasets [PFB18] and pushed the boundaries on certain tasks [KKS<sup>+</sup> 20], but is still limited by the need to manually curate collections of datasets and set up training curricula. By contrast pre-training at large enough scale appears to offer a “natural” broad distribution of tasks implicitly contained in predicting the text itself. One direction for future work might be attempting to generate a broader set of explicit tasks for multi-task learning, for example through procedural generation [TFR<sup>+</sup> 17], human interaction [ZSW<sup>+</sup> 19b], or active learning [Mac92]. 

Algorithmic innovation in language models over the last two years has been enormous, including denoising-based bidirectionality [DCLT18], prefixLM [DL15] and encoder-decoder architectures [LLG<sup>+</sup> 19, RSR<sup>+</sup> 19], random permutations during training [YDY<sup>+</sup> 19], architectures that improve the efficiency of sampling [DYY<sup>+</sup> 19], improvements in data and training procedures [LOG<sup>+</sup> 19], and efficiency increases in the embedding parameters [LCG<sup>+</sup> 19]. Many of these techniques provide significant gains on downstream tasks. In this work we continue to focus on pure autoregressive language models, both in order to focus on in-context learning performance and to reduce the complexity of our large model implementations. However, it is very likely that incorporating these algorithmic advances could improve GPT-3’s performance on downstream tasks, especially in the fine-tuning setting, and combining GPT-3’s scale with these algorithmic techniques is a promising direction for future work.

---

[referencia=32f3c7d144f036a0 score=0.093]
In this paper, we improve the fine-tuning based approaches by proposing BERT: **B** idirectional **E** ncoder **R** epresentations from **T** ransformers. BERT alleviates the previously mentioned unidirectionality constraint by using a “masked language model” (MLM) pre-training objective, inspired by the Cloze task (Taylor, 1953). The masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary id of the masked 

word based only on its context. Unlike left-toright language model pre-training, the MLM objective enables the representation to fuse the left and the right context, which allows us to pretrain a deep bidirectional Transformer. In addition to the masked language model, we also use a “next sentence prediction” task that jointly pretrains text-pair representations. The contributions of our paper are as follows: 

- We demonstrate the importance of bidirectional pre-training for language representations. Unlike Radford et al. (2018), which uses unidirectional language models for pre-training, BERT uses masked language models to enable pretrained deep bidirectional representations. This is also in contrast to Peters et al. (2018a), which uses a shallow concatenation of independently trained left-to-right and right-to-left LMs. 

- We show that pre-trained representations reduce the need for many heavily-engineered taskspecific architectures. BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level _and_ token-level tasks, outperforming many task-specific architectures. 

- BERT advances the state of the art for eleven NLP tasks. The code and pre-trained models are available at https://github.com/ google-research/bert.

---

[referencia=887da5f02141c29f score=0.092]
### **3.1 Baseline** 

Our goal for our baseline is to reflect typical, modern practice. We pre-train a standard Transformer (described in Section 2.1) using a simple denoising objective and then separately fine-tune on each of our downstream tasks. We describe the details of this experimental setup in the following subsections. 

### 3.1.1 Model 

For our model, we use a standard encoder-decoder Transformer as proposed by Vaswani et al. (2017). While many modern approaches to transfer learning for NLP use a Transformer architecture consisting of only a single “stack” (e.g. for language modeling (Radford et al., 2018; Dong et al., 2019) or classification and span prediction (Devlin et al., 2018; Yang et al., 2019)), we found that using a standard encoder-decoder structure achieved good results on both generative and classification tasks. We explore the performance of different model architectures in Section 3.2. 

Our baseline model is designed so that the encoder and decoder are each similar in size and configuration to a “BERTBASE” (Devlin et al., 2018) stack. Specifically, both the encoder and decoder consist of 12 blocks (each block comprising self-attention, optional encoder-decoder attention, and a feed-forward network). The feed-forward networks in each block consist of a dense layer with an output dimensionality of _d_ ff = 3072 followed by a ReLU nonlinearity and another dense layer. The “key” and “value” matrices of all attention mechanisms have an inner dimensionality of _d_ kv = 64 and all attention mechanisms have 12 heads. All other sub-layers and embeddings have a dimensionality of _d_ model = 768. In total, this results in a model with about 220 million parameters. This is roughly twice the number of parameters of BERTBASE since our baseline model contains two layer stacks instead of one. For regularization, we use a dropout probability of 0 _._ 1 everywhere dropout is applied in the model.

---

[referencia=32f3c7d144f036a0 score=0.081]
## **5 Ablation Studies** 

In this section, we perform ablation experiments over a number of facets of BERT in order to better understand their relative importance. Additional 

results are still far worse than those of the pre- 



<!-- Start of picture text -->
Dev Set results are still far worse than those of the pre-<br>Tasks MNLI-m QNLI MRPC SST-2 SQuAD trained bidirectional models. The BiLSTM hurts<br>(Acc) (Acc) (Acc) (Acc) (F1)<br>performance on the GLUE tasks.<br>BERTNo NSPBASE 84.483.9 88.484.9 86.786.5 92.792.6 88.587.9 We recognize that it would also be possible to<br>LTR & No NSP 82.1 84.3 77.5 92.1 77.8 train separate LTR and RTL models and represent<br>+ BiLSTM 82.1 84.1 75.7 91.6 84.9 each token as the concatenation of the two mod-<br>els, as ELMo does. However: (a) this is twice as<br>Table 5: Ablation over the pre-training tasks using the<br>BERTBASE architecture. “No NSP” is trained without expensive as a single bidirectional model; (b) this<br>the next sentence prediction task. “LTR & No NSP” is is non-intuitive for tasks like QA, since the RTL<br>trained as a left-to-right LM without the next sentence model would not be able to condition the answer<br>prediction, like OpenAI GPT. “+ BiLSTM” adds a ran- on the question; (c) this it is strictly less powerful<br>domly initialized BiLSTM on top of the “LTR + No than a deep bidirectional model, since it can use<br>NSP” model during fine-tuning. both left and right context at every layer.<br><!-- End of picture text -->

**5.2 Effect of Model Size** In this section, we explore the effect of model size 

ablation studies can be found in Appendix C. 

**5.1 Effect of Pre-training Tasks** 

on fine-tuning task accuracy. We trained a number 

of BERT models with a differing number of layers,

---

[referencia=887da5f02141c29f score=0.061]
To provide a reasonable means of comparison, we consider multiple configurations for our encoder-decoder model. We will refer to the number of layers and parameters in a BERTBASE-sized layer stack as _L_ and _P_ , respectively. We will use _M_ to refer to the number of FLOPs required for an _L_ + _L_ -layer encoder-decoder model or _L_ -layer decoder-only model to process a given input-target pair. In total, we will compare: 

- An encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder. This model has 2 _P_ parameters and a computation cost of _M_ FLOPs. 

- An equivalent model, but with parameters shared across the encoder and decoder, resulting in _P_ parameters and an _M_ -FLOP computational cost. 

- An encoder-decoder model with _L/_ 2 layers each in the encoder and decoder, giving _P_ parameters and an _M/_ 2-FLOP cost. 

- A decoder-only language model with _L_ layers and _P_ parameters and a resulting computational cost of _M_ FLOPs. 

- A decoder-only prefix LM with the same architecture (and thus the same number of parameters and computational cost), but with fully-visible self-attention over the input.

---

[referencia=887da5f02141c29f score=0.041]
### 3.3.2 Simplifying the BERT Objective 

Based on the results in the prior section, we will now focus on exploring modifications to the BERT-style denoising objective. This objective was originally proposed as a pre-training technique for an encoder-only model trained for classification and span prediction. As such, it may be possible to modify it so that it performs better or is more efficient in our encoder-decoder text-to-text setup. 

First, we consider a simple variant of the BERT-style objective where we don’t include the random token swapping step. The resulting objective simply replaces 15% of the tokens in the input with a mask token and the model is trained to reconstruct the original uncorrupted sequence. A similar masking objective was used by Song et al. (2019) where it was referred to as “MASS”, so we call this variant the “MASS-style” objective. Second, we were interested to see if it was possible to avoid predicting the entire uncorrupted text span since this requires self-attention over long sequences in the decoder. We consider two strategies to achieve this: First, instead of replacing each corrupted token with a mask token, we replace the entirety of each consecutive span of corrupted tokens with a unique mask token. Then, the target sequence becomes the concatenation of the “corrupted” spans, each prefixed by the mask token used to replace it in the input. This is the pre-training objective we use in our baseline, described in Section 3.1.4. Second, we also consider a variant where we simply drop the corrupted tokens from the input sequence completely and task the model with reconstructing the dropped tokens in order. Examples of these approaches are shown in the fifth and sixth rows of Table 3. 

An empirical comparison of the original BERT-style objective to these three alternatives is shown in Table 5. We find that in our setting, all of these variants perform similarly. The only exception was that dropping corrupted tokens completely produced a small improvement in the GLUE score thanks to a significantly higher score on CoLA (60 _._ 04, compared to our 

22 

Exploring the Limits of Transfer Learning

---

[referencia=887da5f02141c29f score=0.035]
15 

Raffel, Shazeer, Roberts, Lee, Narang, Matena, Zhou, Li and Liu 



<!-- Start of picture text -->
y5 y5 y5<br>y4 y4 y4<br>y3 y3 y3<br>y2 y2 y2<br>y1 y1 y1<br>x x x x x x x x x x x x x x x<br>1 2 3 4 5 1 2 3 4 5 1 2 3 4 5<br><!-- End of picture text -->

Figure 3: Matrices representing different attention mask patterns. The input and output of the self-attention mechanism are denoted _x_ and _y_ respectively. A dark cell at row _i_ and column _j_ indicates that the self-attention mechanism is allowed to attend to input element _j_ at output timestep _i_ . A light cell indicates that the self-attention mechanism is _not_ allowed to attend to the corresponding _i_ and _j_ combination. Left: A fully-visible mask allows the self-attention mechanism to attend to the full input at every output timestep. Middle: A causal mask prevents the _i_ th output element from depending on any input elements from “the future”. Right: Causal masking with a prefix allows the self-attention mechanism to use fully-visible masking on a portion of the input sequence. 

at the timestep corresponding to the classification token is then used to make a prediction for classifying the input sequence. 

The self-attention operations in the Transformer’s decoder use a “causal” masking pattern. When producing the _i_ th entry of the output sequence, causal masking prevents the model from attending to the _j_ th entry of the input sequence for _j > i_ . This is used during training so that the model can’t “see into the future” as it produces its output. An attention matrix for this masking pattern is shown in Figure 3, middle.

---

[referencia=2cab3ea10b8b7ae2 score=0.033]
GPT-3 has several structural and algorithmic limitations, which could account for some of the issues above. We focused on exploring in-context learning behavior in autoregressive language models because it is straightforward to both sample and compute likelihoods with this model class. As a result our experiments do not include any bidirectional architectures or other training objectives such as denoising. This is a noticeable difference from much of the recent literature, which has documented improved fine-tuning performance when using these approaches over standard language models [RSR<sup>+</sup> 19]. Thus our design decision comes at the cost of potentially worse performance on tasks which empirically benefit from bidirectionality. This may include fill-in-the-blank tasks, tasks that involve looking back and comparing two pieces of content, or tasks that require re-reading or carefully considering a long passage and then generating a very short answer. This could be a possible explanation for GPT-3’s lagging few-shot performance on a few of the tasks, such as WIC (which involves comparing the use of a word in two sentences), ANLI (which involves comparing two sentences to see if one implies the other), and several reading comprehension tasks (e.g. QuAC and RACE). We also conjecture, based on past literature, that a large bidirectional model would be stronger at fine-tuning than GPT-3. Making a bidirectional model at the scale of GPT-3, and/or trying to make bidirectional models work with few- or zero-shot learning, is a promising direction for future research, and could help achieve the “best of both worlds”. 

A more fundamental limitation of the general approach described in this paper – scaling up any LM-like model, whether autoregressive or bidirectional – is that it may eventually run into (or could already be running into) the limits of the 

33 

pretraining objective. Our current objective weights every token equally and lacks a notion of what is most important to

---

[referencia=2cab3ea10b8b7ae2 score=0.030]
|GPT-3 Medium|7.42E+00|6.41E+20|356|300|6|3|2|1.0|
|GPT-3 Large|1.58E+01|1.37E+21|760|300|6|3|2|1.0|
|GPT-3 XL|2.75E+01|2.38E+21|1,320|300|6|3|2|1.0|
|GPT-3 2.7B|5.52E+01|4.77E+21|2,650|300|6|3|2|1.0|
|GPT-3 6.7B|1.39E+02|1.20E+22|6,660|300|6|3|2|1.0|
|GPT-3 13B|2.68E+02|2.31E+22|12,850|300|6|3|2|1.0|
|GPT-3 175B|3.64E+03|3.14E+23|174,600|300|6|3|2|1.0|



**Table D.1:** Starting from the right hand side and moving left, we begin with the number of training tokens that each model was trained with. Next we note that since T5 uses an encoder-decoder model, only half of the parameters are active for each token during a forward or backwards pass. We then note that each token is involved in a single addition and a single multiply for each active parameter in the forward pass (ignoring attention). Then we add a multiplier of 3x to account for the backwards pass (as computing both<sup>_∂p_</sup> _∂loss_<sup>_arams_</sup> and<sup>_<u>∂acts</u>_</sup> _∂loss_<sup>use a similar amount of compute as the</sup> forwards pass. Combining the previous two numbers, we get the total flops per parameter per token. We multiply this value by the total training tokens and the total parameters to yield the number of total flops used during training. We report both flops and petaflop/s-day (each of which are 8.64e+19 flops).

---

[referencia=887da5f02141c29f score=0.023]
### 3.2.2 Comparing Different Model Structures 

In the interest of experimentally comparing these architectural variants, we would like each model we consider to be equivalent in some meaningful way. We might say that two models are equivalent if they either have the same number of parameters or they require roughly the same amount of computation to process a given (input-sequence, target-sequence) pair. Unfortunately, it is not possible to compare an encoder-decoder model to a language model architecture (comprising a single Transformer stack) according to both of these criteria at the same time. To see why, first note an encoder-decoder model with _L_ layers in the encoder and _L_ layers in the decoder has approximately the same number of parameters as a language model with 2 _L_ layers. However, the same _L_ + _L_ encoder-decoder model will have approximately the same computational cost as a language model with _only L_ layers. This is a consequence of the fact that the _L_ layers in the language model must be applied to _both_ the input and output sequence, while the encoder is only applied to the input sequence and the decoder is only applied to the output sequence. Note that these equivalences are approximate—there are some extra parameters in the decoder due to the encoder-decoder attention and there are also some computational costs in the attention layers that are quadratic in the sequence lengths. In practice, however, we observed nearly identical step 

18 

Exploring the Limits of Transfer Learning 

times for _L_ -layer language models versus _L_ + _L_ -layer encoder-decoder models, suggesting a roughly equivalent computational cost. Further, for the model sizes we consider, the number of parameters in the encoder-decoder attention layers is about 10% of the total parameter count, so we make the simplifying assumption that an _L_ + _L_ -layer encoder-decoder model has the same number of parameters as an 2 _L_ -layer language model.