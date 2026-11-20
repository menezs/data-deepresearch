[referencia=6ee83218472b4aa1 score=0.420]
# **F Token Counts** 

Table 2, Table 3, and Table 4 present the average and maximum number of tokens in each of the input contexts for all experimental settings. Note that MPT-30B and MPT-30B-Instruct use the same tokenizer, GPT-3.5-Turbo and GPT-3.5-Turbo (16K) use the same tokenizer, and Claude-1.3 and Claude-1.3 (100K) use the same tokenizer. Furthermore, the Claude-1.3 tokenizer is the same as the GPT-3.5-Turbo tokenizer, modulo some additional special tokens that do not appear in our data. As a result, the token counts for these two model families is the same in our experimental settings. 

||Closed-Bo|ok|Oracle||
|---|---|---|---|---|
||avg_±_stdev|max|avg_±_stdev|max|
|LongChat-13B (16K)|55.6_±_2.7|70|219.7_±_48.5|588|
|MPT-30B|43.5_±_2.2|58|187.9_±_41.8|482|
|GPT-3.5-Turbo|15.3_±_2.2|29|156.0_±_41.8|449|
|Claude-1.3|15.3_±_2.2|29|156.0_±_41.8|449|



Table 2: Token count statistics for each of the evaluated models on the closed-book and oracle multi-document question answering settings.

---

[referencia=6ee83218472b4aa1 score=0.069]
Figure 5: The effect of changing the position of relevant information (document containing the answer) on multidocument question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context. 

(16K).<sup>5</sup> GPT-3.5-Turbo has a maximum context length of 4K tokens, and GPT-3.5-Turbo (16K) is a version with an extended maximum context length of 16K tokens. We evaluate Claude-1.3 and Claude1.3 (100K) with the Anthropic API; Claude-1.3 has a maximum context length of 8K tokens, and Claude-1.3 (100K) has an extended context length of 100K tokens.<sup>6</sup> 

|Model|Closed-Book|Oracle|
|---|---|---|
|LongChat-13B (16K)|35.0%|83.4%|
|MPT-30B-Instruct|31.5%|81.9%|
|GPT-3.5-Turbo|56.1%|88.3%|
|GPT-3.5-Turbo (16K)|56.0%|88.6%|
|Claude-1.3|48.3%|76.1%|
|Claude-1.3 (100K)|48.2%|76.4%|



Table 1: Closed-book and oracle accuracy of language models on the multi-document question answering task.

---

[referencia=6ee83218472b4aa1 score=0.068]
20 Total Retrieved Documents (~4K tokens, 500 question sample) 90 

80 70 

60 50 1st 5th 10th 15th 20th Position of Document with the Answer claude-1.3 mpt-30b-instruct claude-1.3-100k longchat-13b-16k gpt-3.5-turbo-0613 gpt-4-0613 gpt-3.5-turbo-16k-0613 

Figure 15: Although GPT-4 has higher absolute performance than other models, its performance still degrades when relevant information occurs in the middle of the input context. 

ples (out of 2655) that exceed Llama-2’s maximum context length of 4096 tokens. We experiment with models of varying sizes (7B, 13B, and 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback (“-chat-” models). The results are presented in Figure 16. 

Comparing Llama-2 models of varying sizes, we find that only the larger models (13B and 70B) exhibit the U-shaped performance curve (i.e., both primacy and recency bias)—the smallest Llama2 models (7B) are solely recency-biased. Given these results, we hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not previously observe any primacy bias in language models because the models they studied were too small (less than 1B parameters).

---

[referencia=6ee83218472b4aa1 score=0.055]
## **2.2 Models** 

We analyze several state-of-the-art open and closed language models. We use greedy decoding when generating outputs and leave exploration of other decoding methods to future work. We use a standard set of prompts for each model (Figure 2). 

**Open models.** We experiment with MPT-30BInstruct, which has a maximum context length of 8192 tokens. The model was initially pre-trained on 1 trillion tokens using 2048-token sequences, followed by an additional sequence length adaptation pre-training phase on 50 billion tokens using 8192-token sequences. MPT-30B-Instruct uses ALiBi (Press et al., 2022) to represent positional information. We also evaluate LongChat-13B (16K) (Li et al., 2023), which extends the LLaMA-13B (Touvron et al., 2023a) context window from 2048 to 16384 tokens by using condensed rotary positional embeddings before fine-tuning with 16384-token sequences. 

**Closed models.** We use the OpenAI API to experiment with GPT-3.5-Turbo and GPT-3.5-Turbo 



<!-- Start of picture text -->
10 Total Retrieved Documents (~2K tokens) 20 Total Retrieved Documents (~4K tokens) 30 Total Retrieved Documents (~6K tokens)<br>75 75 75<br>70 70 70<br>65 65 65<br>60 60 60<br>55 55 55<br>50 50 50<br>1st 5th 10th 1st 5th 10th 15th 20th 1st 5th 10th 15th 20th 25th 30th<br>Position of Document with the Answer Position of Document with the Answer Position of Document with the Answer<br>claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.049]
Table 3: Token count statistics for each of the evaluated models on each of the document question answering settings. 

||75 KV pair|s|140 KV pai|rs|300 KV pai|rs|
|---|---|---|---|---|---|---|
||avg_±_stdev|max|avg_±_stdev|max|avg_±_stdev|max|
|LongChat-13B (16K)|5444.5_±_19.1|5500|10072.4_±_24.1|10139|21467.3_±_35.9|21582|
|MPT-30B|4110.5_±_23.8|4187|7600.9_±_31.1|7687|16192.4_±_46.6|16319|
|GPT-3.5-Turbo|3768.7_±_25.6|3844|6992.8_±_34.1|7088|14929.4_±_50.7|15048|
|Claude-1.3|3768.7_±_25.6|3844|6992.8_±_34.1|7088|14929.4_±_50.7|15048|



Table 4: Token count statistics for each of the evaluated models on each of the key-value (KV) retrieval settings.

---

[referencia=6ee83218472b4aa1 score=0.047]
Table 2: Token count statistics for each of the evaluated models on the closed-book and oracle multi-document question answering settings. 

||10 docs||20 docs||30 docs||
|---|---|---|---|---|---|---|
||avg_±_stdev|max|avg_±_stdev|max|avg_±_stdev|max|
|LongChat-13B (16K)|1749.9_±_112.4|2511|3464.6_±_202.3|4955|5181.9_±_294.7|7729|
|MPT-30B|1499.7_±_88.5|1907|2962.4_±_158.4|3730|4426.9_±_230.5|5475|
|GPT-3.5-Turbo|1475.6_±_86.5|1960|2946.2_±_155.1|3920|4419.2_±_226.5|6101|
|Claude-1.3|1475.6_±_86.5|1960|2946.2_±_155.1|3920|4419.2_±_226.5|6101|



Table 3: Token count statistics for each of the evaluated models on each of the document question answering settings.

---

[referencia=6ee83218472b4aa1 score=0.032]
Comparing between Llama-2 models with and without additional supervised fine-tuning and reinforcement learning from human feedback, we see that additional fine-tuning dramatically improves performance on the multi-document QA task. The 7B models with and without additional fine-tuning show minimal primacy bias, and are largely recency-biased. The 13B base model has a dramatic primacy and recency bias—there is a 20-point accuracy disparity between the best- and worst-case performance. Applying additional finetuning to the 13B seems to slightly reduce this bias (10-point worst-case degradation), but the bias remains significant. However, the 70B models with and without additional fine-tuning have largely similar trends (showing both primacy and recency bias), and additional fine-tuning minimally changes the positional bias severity. 



<!-- Start of picture text -->
20 Total Retrieved Documents (~4K tokens)<br>70<br>60<br>50<br>40<br>30<br>20<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>Llama-2-7b-chat-hf Llama-2-7b-hf<br>Llama-2-13b-chat-hf Llama-2-13b-hf<br>Llama-2-70b-chat-hf Llama-2-70b-hf<br>Accuracy<br><!-- End of picture text -->

Figure 16: Multi-document QA performance (20 total documents) of Llama-2 models of varying sizes (7B, 13B, 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback (“-chat-” models).

---

[referencia=6ee83218472b4aa1 score=0.030]
## **4.1 Effect of Model Architecture** 

The open models we evaluated are all decoder-only models—at each timestep, they may only attend to prior tokens. To better understand the potential effects of model architecture on how language model use context, we compare decoder-only and encoder-decoder language models. 

We experiment with Flan-T5-XXL (Raffel et al., 2020; Chung et al., 2022) and Flan-UL2 (Tay et al., 2023). Flan-T5-XXL is trained with a sequences of 512 tokens (encoder and decoder). Flan-UL2 is initially trained with sequences of 512 tokens (encoder and decoder), but is then pre-trained for an extra 100K steps with 1024 tokens (encoder and decoder) before instruction fine-tuning on sequences with 2048 tokens in the encoder and 512 tokens in the decoder. However, since these models use 

relative positional embeddings, they can (in principle) extrapolate beyond these maximum context lengths; Shaham et al. (2023) find that both models can perform well with sequences of up to 8K tokens. 

Figure 8 compares the performance of decoderonly and encoder-decoder models. When Flan-UL2 is evaluated on sequences within its 2048-token training-time context window (Figure 8; left subplot), its performance is relatively robust to changes in the position of relevant information within the input context (1.9% absolute difference between best- and worst-case performance). When evaluated on settings with sequences longer than 2048 tokens (Figure 8; center and right), Flan-UL2 performance begins to degrade when relevant information is placed in the middle. Flan-T5-XXL shows a similar trend, where longer input contexts result in a greater performance degradation when placing relevant information in the middle of the input context. We hypothesize that encoder-decoder models may make better use of their context windows because their bidirectional encoder allows processing each document in the context of future documents, potentially improving relative importance estimation between documents.

---

[referencia=6ee83218472b4aa1 score=0.022]
These observations complement prior work, which found that non-instruction fine-tuned language models are biased towards recent tokens (i.e., the end of the input context; Khandelwal et al., 2018; Press et al., 2021). This recency bias has been observed in past work when evaluating models on next-word prediction of contiguous text, a setting where language models minimally benefit from long-range information (Sun et al., 2021). In contrast, our results show that language models are capable of using longer-range information (i.e., the beginning of the input context) when prompted with instruction-formatted data. We hypothesize that non-instruction fine-tuned language models learn to use these long contexts from similarlyformatted data that may occur in Internet text seen during pre-training, e.g., StackOverflow questions 

and answers. 

To better understand the effect of additional finetuning and model scale, we also experimented with Llama-2 models of varying sizes (7B, 13B, and 70B) with and without additional supervised fine-tuning and reinforcement learning from human feedback (Appendix E). We find that the U- shaped performance curve only appears in sufficiently large language models (with or without additional fine-tuning)—the 7B Llama-2 models are solely recency biased, while the 13B and 70B models exhibit a U-shaped performance curve. In addition, we see that the Llama-2 supervised fine-tuning and reinforcement learning from human feedback procedure slightly mitigates the positional bias in smaller models (13B, akin to trends shown when comparing MPT-30B and MPT-30B-Instruct), but minimally affects trends on larger models (70B).

---

[referencia=6ee83218472b4aa1 score=0.020]
## **3.2 Results and Discussion** 

We experiment with input contexts containing 75, 140, and 300 key-value pairs (500 examples each). We use the same set of models as the multidocument question answering experiments, see §2.2 for more details. 

Figure 7 presents key-value retrieval performance. Claude-1.3 and Claude-1.3 (100K) do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when contexts have 140 or 300 key-value pairs— although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance. 

Similar to our multi-document QA results, GPT3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30BInstruct have the lowest performance when they must access key-value pairs in the middle of their input context. LongChat-13B (16K) exhibits a different trend in the 140 key-value setting; we qualitatively observe that when relevant information is 



<!-- Start of picture text -->
75 Key-Value Pairs (~4K tokens) 140 Key-Value Pairs (~8K tokens) 300 Key-Value Pairs (~16K tokens)<br>100 100 100<br>90 90 90<br>80 80 80<br>70 70 70<br>60 60 60<br>50 50 50<br>40 40 40<br>1st 25th 50th 75th 1st 35th 70th 105th 140th 1st 50th 100th 150th 200th 250th 300th<br>Position of Key to Retrieve Position of Key to Retrieve Position of Key to Retrieve<br>claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.017]
<!-- Start of picture text -->
2023; Rubin and Berant, 2023, inter alia ) have document question task is lower than its perfor-<br>resulted in language models with larger context mance when predicting  without any documents  (i.e.,<br>windows (e.g., 4096, 32K, and even 100K tokens), the closed-book setting; 56.1%). Furthermore, we<br>but it remains unclear how these extended-context find that models often have identical performance<br>language models make use of their input contexts to their extended-context counterparts, indicating<br>when performing downstream tasks. that extended-context models are not necessarily<br>We empirically investigate this question via better at using their input context (§2.3).<br>Given that language models struggle to retrieve<br>controlled experiments with a variety of state-of-<br>and use relevant information in the multi-document<br>the-art open (MPT-30B-Instruct, LongChat-13B<br>question answering task, to what extent can lan-<br>(16K)) and closed (OpenAI’s GPT-3.5-Turbo and<br>Anthropic’s Claude-1.3) language models in set- guage models even  retrieve  from their input con-<br>texts? We study this question with a synthetic key-<br>tings that require accessing and using information<br>value retrieval task, which is designed to be a mini-<br>within an input context. In particular, our experi-<br>mal testbed for the basic ability to retrieve matching<br>ments make controlled changes to the input context<br>size and the position of the relevant information tokens from the input context. In this task, models<br>are given a collection of JSON-formatted key-value<br>within the input context and study their effects on<br>pairs and must return the value associated with a<br>language model performance. If language models<br>specific key. Similar to the multi-document QA<br><!-- End of picture text -->

can robustly use information within long input contexts, then their performance should be _minimally affected_ by the position of the relevant information in the input context. 

task, the key-value retrieval task admits controlled changes to the input context length (adding more 

key-value pairs) and the position of relevant in-

---

[referencia=6ee83218472b4aa1 score=0.017]
## **4.2 Effect of Query-Aware Contextualization** 

Our multi-document QA and key-value retrieval experiments place the query (i.e., question to answer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or keyvalue pairs, since the query only appears at the end 



<!-- Start of picture text -->
10 Total Retrieved Documents (~2K tokens) 20 Total Retrieved Documents (~4K tokens) 30 Total Retrieved Documents (~6K tokens)<br>70 70 70<br>65 65 65<br>60 60 60<br>55 55 55<br>50 50 50<br>1st 5th 10th 1st 5th 10th 15th 20th 1st 5th 10th 15th 20th 25th 30th<br>Position of Document with the Answer Position of Document with the Answer Position of Document with the Answer<br>mpt-30b-instruct longchat-13b-16k flan-t5-xxl flan-ul2<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

Figure 8: When encoder-decoder models (Flan-UL2 and Flan-T5-XXL) evaluated on sequences that are _shorter_ than their encoder’s training-time maximum sequence length (2048 and 512 tokens, respectively), they are relatively robust to changes in the position of relevant information within their input context (left subplot). In contrast, when these models are evaluated on sequences _longer_ than those seen during training (center and right subplots), we observe a U-shaped performance curve—performance is higher when relevant information occurs at the beginning or end of the input context, as opposed to the middle of the input context. 



<!-- Start of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.011]
Handling these use-cases requires language models to successfully operate over long sequences. Existing language models are generally implemented with Transformers (Vaswani et al., 2017), which require memory and compute that increases quadratically in sequence length. As a result, Transformer language models were often trained with relatively small context windows (between 5122048 tokens). Recent improvements in hardware (e.g., faster GPUs with more memory) and algorithms (Dai et al., 2019; Dao et al., 2022; Poli et al., 



<!-- Start of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.010]
## **4.3 Effect of Instruction Fine-Tuning** 

The models we evaluated are all instruction finetuned—after their initial pre-training, they undergo supervised fine-tuning on a dataset of instructions and responses. The task specification and/or instruction is commonly placed at the beginning of the input context in supervised instruction finetuning data, which might lead instruction finetuned language models to place more weight on the start of the input context. To better understand the potential effects of instruction fine-tuning on how language models use long input contexts, we compare the multi-document question answering performance of MPT-30B-Instruct against its base model (i.e., before instruction fine-tuning) MPT30B. We use the same experimental setup as §2. 

Figure 10 compares the multi-document QA performance of MPT-30B and MPT-30B-Instruct as a function of the position of the relevant in- 



<!-- Start of picture text -->
20 Total Retrieved Documents (~4K tokens)<br>56<br>54<br>52<br>50<br>48<br>46<br>44<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>mpt-30b mpt-30b-instruct<br>Accuracy<br><!-- End of picture text -->

Figure 10: Multi-document QA performance of MPT30B-Instruct compared against its base model (i.e., before instruction fine-tuning) MPT-30B. Both models have a U-shaped performance curve, where performance is much higher when relevant information occurs at the start or end of the input context, indicating that the instruction fine-tuning process itself is not necessarily responsible for these performance trends. 

formation in the input context. Surprisingly, we see that both MPT-30B and MPT-30B-Instruct exhibit a U-shaped performance curve, where performance is highest when relevant information occurs at the very beginning or very end of the context. Although the absolute performance of MPT-30BInstruct is uniformly higher than that of MPT-30B, their overall performance trends are similar. We also observe that instruction fine-tuning slightly reduces the worst-case performance disparity from nearly 10% between the base model best- and worst-case performance to around 4%.

---

[referencia=6ee83218472b4aa1 score=0.008]
## guage models is perhaps surprising, since the self- 

former. ArXiv:2004.05150. 

attention mechanisms underlying Transformer language models is technically equally capable of retrieving any token from their contexts. **7 Conclusion** 

Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob 

We empirically study how language models use long input contexts via a series of controlled experiments. We show that language model performance degrades significantly when changing the position of relevant information, indicating that models struggle to robustly access and use infor- 

mation in long input contexts. In particular, per- 

Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-

---

[referencia=6ee83218472b4aa1 score=0.007]
## **2.1 Experimental Setup** 

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) _k_ documents (e.g., passages from Wikipedia), where _exactly one_ of the documents contains the answer 

1nelsonliu.me/papers/lost-in-the-middle 

to the question and _k −_ 1 “distractor” documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. 

We instantiate this task with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. In particular, we take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). We use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts. For each of the queries, we need a document that contains the answer and _k −_ 1 distractor documents that do not contain the answer. To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations. 

To collect _k −_ 1 distractor documents that do not contain the answer, we use a retrieval system (Contriever, fine-tuned on MS-MARCO; Izacard et al., 2021) to retrieve the _k −_ 1 Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers.<sup>2,3</sup> In the input context, the distractor documents are presented in order of decreasing relevance.<sup>4</sup> 

To modulate the position of relevant information within the input context, we adjust the order of the documents to change the position of the document that contains the answer (Figure 3). To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure 4). 

Following Kandpal et al. (2022) and Mallen et al. (2023), we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.

---

[referencia=6ee83218472b4aa1 score=0.007]
<!-- Start of picture text -->
20 Total Retrieved Documents<br>(~4K tokens, query-aware contextualization)<br>80<br>70<br>60<br>50<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>claude-1.3 gpt-3.5-turbo-16k-0613<br>claude-1.3-100k mpt-30b-instruct<br>gpt-3.5-turbo-0613 longchat-13b-16k<br>Accuracy<br><!-- End of picture text -->

Figure 9: Query-aware contextualization (placing the query before _and_ after the documents) does not substantially improve robustness of language models to changing the position of relevant information in multidocument QA; performance slightly increases when relevant information occurs at the very beginning, but otherwise slightly decreases. 

of the prompt and decoder-only models can only attend to prior tokens at each timestep. In contrast, encoder-decoder models (which seem more robust to changes in the position of relevant information; §4.1) use a bidirectional encoder to contextualize input contexts—can we use this observation to improve decoder-only models by placing the query before _and_ after the data, enabling query-aware contextualization of documents (or key-value pairs)? 

We find that query-aware contextualization dramatically improves performance on the key-value retrieval task—all models achieve near-perfect per- 

formance on the 75, 140, and 300 key-value pair settings. For example, GPT-3.5-Turbo (16K) with query-aware contextualization achieves perfect performance when evaluated with 300 key-value pairs. 

In contrast, without query-aware contextualization, the worst-case performance is 45.6% (Figure 7). Despite the significant impact on keyvalue retrieval performance, query-aware contextualization minimally affects performance trends in the multi-document question answering task (Figure 9); it slightly improves performance when the relevant information is located at the very beginning of the input context, but slightly decreases performance in other settings.

---

[referencia=6ee83218472b4aa1 score=0.007]
task, the key-value retrieval task admits controlled changes to the input context length (adding more 

key-value pairs) and the position of relevant in- 

formation. Although some models perform the synthetic key-value retrieval task perfectly, other models struggle to simply retrieve matching tokens that occur in the middle of their input context and continue to exhibit a U-shaped performance curve. 

We first experiment with multi-document question answering, which requires models to reason over provided documents to find relevant information and use it to answer a given question; this task 

mimics the retrieval-augmented generation setup underlying many commercial generative search and question answering applications (e.g., Bing Chat). In this setting, we control (i) the input context length by changing the number of documents in 

To better understand why language models struggle to robustly access and use information in their input contexts, we study the role of model architecture (decoder-only vs. encoder-decoder), queryaware contextualization, and instruction fine-tuning 

the input context (akin to retrieving more or less 

(§4). We find that:

---

[referencia=6ee83218472b4aa1 score=0.006]
• Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context. 

Our results indicate that prompting language 

models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. To better understand this trade-off in practice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly _one_ document that answers the question, none or many of the top _k_ documents may contain the answer in the open-domain QA setting. When retrieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model performance saturates long before retriever recall saturates, indicating that current models fail to effectively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( _∼_ 1.5% for GPT-3.5-Turbo and _∼_ 1% for claude-1.3). 

Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future longcontext models; to claim that a language model can robustly use information within long input contexts, it is necessary to show that its performance is minimally affected by the position of the relevant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data.<sup>1</sup>

---

[referencia=6ee83218472b4aa1 score=0.006]
- Figure 13: Language model performance on multidocument QA when using random distractors, rather than retrieved distractors. 

- Figure 14 presents the results of this experiment. 

- We continue to see a U-shaped performance curve, with performance degrading when language models must use information in the middle of their input contexts. Comparing the results in §2.3 with those when randomizing the distractor order and mentioning such in the prompt, we see that randomization slightly decreases performance when the relevant information is at the very beginning of the context, and slightly increases performance when using information in the middle and end of the context. 

- **D GPT-4 Performance** We evaluate GPT-4 (8K) on a subset of 500 ran- 

- dom multi-document QA examples with 20 total 

- documents in each input context (Figure 15). GPT4 achieves higher absolute performance than any other language model, but still shows a U-shaped performance curve—its performance is highest when relevant information occurs at the very start or end of the context, and performance degrades when it must use information in the middle of its input context. 

- **E Llama-2 Performance** We evaluate Llama-2 (Touvron et al., 2023b) on 

multi-document QA with 20 total documents in each input context. The Llama tokenizer produces longer sequences than the tokenizers for our previously-studied models, so we discard 20 exam- 

20 Total Retrieved Documents (~4K tokens, randomly ordered) 75 70 

65 60 55 1st 5th 10th 15th 20th Position of Document with the Answer 

claude-1.3 gpt-3.5-turbo-16k-0613 claude-1.3-100k mpt-30b-instruct gpt-3.5-turbo-0613 longchat-13b-16k 

Figure 14: Language model performance when randomizing the order of the distractors (rather than presenting them in order of decreasing relevance) and mentioning as such in the prompt. 

20 Total Retrieved Documents (~4K tokens, 500 question sample) 90 

80 70