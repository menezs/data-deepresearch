[referencia=6ee83218472b4aa1 score=0.977]
## **2.3 Results and Discussion** 

We experiment with input contexts containing 10, 20, and 30 total documents. Figure 5 presents multidocument question answering performance when varying the position of relevant information within the input context. To contextualize model performance, we also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. 

**Model performance is highest when relevant information occurs at the beginning or end of its input context.** As illustrated in Figure 5, changing the position of relevant information in the input context leads to substantial decreases in model performance. In particular, we see a distinctive U- 

> 5We use the 0613 OpenAI model versions. 

> 6We also evaluate GPT-4 (8K) on a subset of multidocument QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute performance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. 

shaped performance curve—models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded performance when forced to use information within the middle of its input context. For example, GPT-3.5Turbo’s multi-document QA performance can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than performance without _any_ input documents (i.e., closedbook performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks.

---

[referencia=6ee83218472b4aa1 score=0.976]
**Lost in the Middle: How Language Models Use Long Contexts** 

**Nelson F. Liu**<sup>1</sup><sup>_∗_</sup> **Kevin Lin**<sup>2</sup> **John Hewitt**<sup>1</sup> **Ashwin Paranjape**<sup>3</sup> **Michele Bevilacqua**<sup>3</sup> **Fabio Petroni**<sup>3</sup> **Percy Liang**<sup>1</sup> 1Stanford University 2University of California, Berkeley 3Samaya AI nfliu@cs.stanford.edu 

# **Abstract** 

While recent language models have the ability to take long contexts as input, relatively little is known about how well they _use_ longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models.

---

[referencia=6ee83218472b4aa1 score=0.963]
• Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context. 

Our results indicate that prompting language 

models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. To better understand this trade-off in practice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly _one_ document that answers the question, none or many of the top _k_ documents may contain the answer in the open-domain QA setting. When retrieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model performance saturates long before retriever recall saturates, indicating that current models fail to effectively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( _∼_ 1.5% for GPT-3.5-Turbo and _∼_ 1% for claude-1.3). 

Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future longcontext models; to claim that a language model can robustly use information within long input contexts, it is necessary to show that its performance is minimally affected by the position of the relevant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data.<sup>1</sup>

---

[referencia=6ee83218472b4aa1 score=0.940]
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

[referencia=6ee83218472b4aa1 score=0.935]
## documents in retrieval-augmented generation), and 

(ii) control the position of the relevant information 

• Encoder-decoder models are relatively robust to changes in the position of relevant information within their input context, but only when evaluated on sequences within its trainingtime sequence length. When evaluated on sequences longer than those seen during train- 

within the input context by changing the order of the documents to place the relevant document at the beginning, middle or end of the context. We find that changing the position of relevant information in the input context can substantially 

ing, we observe a U-shaped performance curve (§4.1). • Query-aware contextualization (placing the 

affect model performance, indicating that current language models do not robustly access and use information in long input contexts. Furthermore, 

we observe a distinctive U-shaped performance 

query before _and_ after the documents or key- 

curve (Figure 1); language model performance is highest when relevant information occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance significantly degrades when models must access and use information in the middle of their input context (§2.3). For example, when relevant information is placed in the middle of its input context, GPT-3.5-Turbo’s performance on the multi- 

value pairs) enables near-perfect performance on the synthetic key-value task, but minimally changes trends in multi-document QA (§4.2). 

• Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context. 

Our results indicate that prompting language

---

[referencia=6ee83218472b4aa1 score=0.930]
<!-- Start of picture text -->
2023; Rubin and Berant, 2023, inter alia ) have document question task is lower than its perfor-<br>resulted in language models with larger context mance when predicting  without any documents  (i.e.,<br>windows (e.g., 4096, 32K, and even 100K tokens), the closed-book setting; 56.1%). Furthermore, we<br>but it remains unclear how these extended-context find that models often have identical performance<br>language models make use of their input contexts to their extended-context counterparts, indicating<br>when performing downstream tasks. that extended-context models are not necessarily<br>We empirically investigate this question via better at using their input context (§2.3).<br>Given that language models struggle to retrieve<br>controlled experiments with a variety of state-of-<br>and use relevant information in the multi-document<br>the-art open (MPT-30B-Instruct, LongChat-13B<br>question answering task, to what extent can lan-<br>(16K)) and closed (OpenAI’s GPT-3.5-Turbo and<br>Anthropic’s Claude-1.3) language models in set- guage models even  retrieve  from their input con-<br>texts? We study this question with a synthetic key-<br>tings that require accessing and using information<br>value retrieval task, which is designed to be a mini-<br>within an input context. In particular, our experi-<br>mal testbed for the basic ability to retrieve matching<br>ments make controlled changes to the input context<br>size and the position of the relevant information tokens from the input context. In this task, models<br>are given a collection of JSON-formatted key-value<br>within the input context and study their effects on<br>pairs and must return the value associated with a<br>language model performance. If language models<br>specific key. Similar to the multi-document QA<br><!-- End of picture text -->

can robustly use information within long input contexts, then their performance should be _minimally affected_ by the position of the relevant information in the input context. 

task, the key-value retrieval task admits controlled changes to the input context length (adding more 

key-value pairs) and the position of relevant in-

---

[referencia=6ee83218472b4aa1 score=0.928]
## **2.1 Experimental Setup** 

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) _k_ documents (e.g., passages from Wikipedia), where _exactly one_ of the documents contains the answer 

1nelsonliu.me/papers/lost-in-the-middle 

to the question and _k −_ 1 “distractor” documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. 

We instantiate this task with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. In particular, we take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). We use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts. For each of the queries, we need a document that contains the answer and _k −_ 1 distractor documents that do not contain the answer. To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations. 

To collect _k −_ 1 distractor documents that do not contain the answer, we use a retrieval system (Contriever, fine-tuned on MS-MARCO; Izacard et al., 2021) to retrieve the _k −_ 1 Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers.<sup>2,3</sup> In the input context, the distractor documents are presented in order of decreasing relevance.<sup>4</sup> 

To modulate the position of relevant information within the input context, we adjust the order of the documents to change the position of the document that contains the answer (Figure 3). To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure 4). 

Following Kandpal et al. (2022) and Mallen et al. (2023), we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.

---

[referencia=6ee83218472b4aa1 score=0.880]
Figure 4: Modulating the input context length of the multi-document question answering example presented in Figure 2. Adding documents that do not contain the answer increases the length of the input context, but does not affect the desired output. 

Our experimental setup is similar to the needlein-a-haystack experiments of Ivgi et al. (2023), who compare question answering performance when the relevant paragraph is placed (i) at the beginning of the input or (ii) a random position within the input. They find that encoder-decoder models have significantly higher performance when relevant information is placed at the start of the input context. In contrast, we study finer-grained changes in the position of relevant information.

---

[referencia=6ee83218472b4aa1 score=0.877]
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

---

[referencia=6ee83218472b4aa1 score=0.847]
## **3.2 Results and Discussion** 

We experiment with input contexts containing 75, 140, and 300 key-value pairs (500 examples each). We use the same set of models as the multidocument question answering experiments, see §2.2 for more details. 

Figure 7 presents key-value retrieval performance. Claude-1.3 and Claude-1.3 (100K) do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when contexts have 140 or 300 key-value pairs— although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance. 

Similar to our multi-document QA results, GPT3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30BInstruct have the lowest performance when they must access key-value pairs in the middle of their input context. LongChat-13B (16K) exhibits a different trend in the 140 key-value setting; we qualitatively observe that when relevant information is 



<!-- Start of picture text -->
75 Key-Value Pairs (~4K tokens) 140 Key-Value Pairs (~8K tokens) 300 Key-Value Pairs (~16K tokens)<br>100 100 100<br>90 90 90<br>80 80 80<br>70 70 70<br>60 60 60<br>50 50 50<br>40 40 40<br>1st 25th 50th 75th 1st 35th 70th 105th 140th 1st 50th 100th 150th 200th 250th 300th<br>Position of Key to Retrieve Position of Key to Retrieve Position of Key to Retrieve<br>claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.840]
## **4.2 Effect of Query-Aware Contextualization** 

Our multi-document QA and key-value retrieval experiments place the query (i.e., question to answer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or keyvalue pairs, since the query only appears at the end 



<!-- Start of picture text -->
10 Total Retrieved Documents (~2K tokens) 20 Total Retrieved Documents (~4K tokens) 30 Total Retrieved Documents (~6K tokens)<br>70 70 70<br>65 65 65<br>60 60 60<br>55 55 55<br>50 50 50<br>1st 5th 10th 1st 5th 10th 15th 20th 1st 5th 10th 15th 20th 25th 30th<br>Position of Document with the Answer Position of Document with the Answer Position of Document with the Answer<br>mpt-30b-instruct longchat-13b-16k flan-t5-xxl flan-ul2<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

Figure 8: When encoder-decoder models (Flan-UL2 and Flan-T5-XXL) evaluated on sequences that are _shorter_ than their encoder’s training-time maximum sequence length (2048 and 512 tokens, respectively), they are relatively robust to changes in the position of relevant information within their input context (left subplot). In contrast, when these models are evaluated on sequences _longer_ than those seen during training (center and right subplots), we observe a U-shaped performance curve—performance is higher when relevant information occurs at the beginning or end of the input context, as opposed to the middle of the input context. 



<!-- Start of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.827]
Figure 7: The effect of changing the input context length and the position of relevant information on key-value retrieval performance. Lower positions are closer to the start of the input context. Although some models show perfect accuracy on this synthetic task (e.g., Claude-1.3 and Claude-1.3 (100K)), we see again that performance is often highest when relevant information is occurs at the very start or end of the context, and rapidly degrades when models must retrieve from the middle of the input context. 

placed at the start of the input context, LongChat13B (16K) tends to generate code to retrieve the key, rather than outputting the value directly.

---

[referencia=6ee83218472b4aa1 score=0.798]
# **5 Is More Context Is Always Better? A Case Study With Open-Domain QA** 

Our results indicate that prompting language models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. Even if a language model can take in 16K tokens, is it actually beneficial to provide 16K tokens of context? The answer to this question is ultimately downstream task-specific since it depends on the marginal value of the added context and the model’s ability to effectively use long input contexts, but we perform a case study with opendomain question answering on NaturalQuestionsOpen to better understand this trade-off in existing language models. 

We use language models in a standard retrieverreader setup. A retrieval system (Contriever, finetuned on MS-MARCO) takes an input query from NaturalQuestions-Open and returns the _k_ documents from Wikipedia with the highest relevance score. To condition language models on these retrieved documents, we simply include them in the prompt. We evaluate retriever recall and reader accuracy (whether any of the annotated answers appear in the predicted output) as a function of the number of retrieved documents _k_ . We use a subset of NaturalQuestions-Open where the long answer is a paragraph (as opposed to a table or a list). 

Figure 11 presents retriever recall and open- 



<!-- Start of picture text -->
90<br>80<br>70<br>60<br>50<br>5 10 20 30 40 50<br>Number of Retrieved Docs<br>claude-1.3 mpt-30b-instruct<br>claude-1.3-100k longchat-13b-16k<br>gpt-3.5-turbo-0613 contriever recall<br>gpt-3.5-turbo-16k-0613<br>Metric<br><!-- End of picture text -->

Figure 11: Retriever recall and model performance as a function of the number of retrieved documents. Model performance saturates long before retriever recall, indicating that the models have difficulty making use of the extra retrieved documents.

---

[referencia=6ee83218472b4aa1 score=0.794]
## **4.3 Effect of Instruction Fine-Tuning** 

The models we evaluated are all instruction finetuned—after their initial pre-training, they undergo supervised fine-tuning on a dataset of instructions and responses. The task specification and/or instruction is commonly placed at the beginning of the input context in supervised instruction finetuning data, which might lead instruction finetuned language models to place more weight on the start of the input context. To better understand the potential effects of instruction fine-tuning on how language models use long input contexts, we compare the multi-document question answering performance of MPT-30B-Instruct against its base model (i.e., before instruction fine-tuning) MPT30B. We use the same experimental setup as §2. 

Figure 10 compares the multi-document QA performance of MPT-30B and MPT-30B-Instruct as a function of the position of the relevant in- 



<!-- Start of picture text -->
20 Total Retrieved Documents (~4K tokens)<br>56<br>54<br>52<br>50<br>48<br>46<br>44<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>mpt-30b mpt-30b-instruct<br>Accuracy<br><!-- End of picture text -->

Figure 10: Multi-document QA performance of MPT30B-Instruct compared against its base model (i.e., before instruction fine-tuning) MPT-30B. Both models have a U-shaped performance curve, where performance is much higher when relevant information occurs at the start or end of the input context, indicating that the instruction fine-tuning process itself is not necessarily responsible for these performance trends. 

formation in the input context. Surprisingly, we see that both MPT-30B and MPT-30B-Instruct exhibit a U-shaped performance curve, where performance is highest when relevant information occurs at the very beginning or very end of the context. Although the absolute performance of MPT-30BInstruct is uniformly higher than that of MPT-30B, their overall performance trends are similar. We also observe that instruction fine-tuning slightly reduces the worst-case performance disparity from nearly 10% between the base model best- and worst-case performance to around 4%.

---

[referencia=6ee83218472b4aa1 score=0.786]
# **A Ambiguity in Multi-Document QA Distractor Documents** 

Following past work on NaturalQuestions-Open (Izacard et al., 2021; Izacard and Grave, 2021, _inter alia_ ), we use a Wikipedia dump from late 2018 as our retrieval corpus. However, this standard Wikipedia dump has a small amount of temporal mismatch with the NaturalQuestions annotations. 

For example, consider the question “what nfl team does robert griffin iii play for”. The NaturalQuestions annotated answer is “currently a free agent”. However, the Wikipedia retrieval corpus contains the information that he plays for the “Baltimore Ravens”, since he was released from the team between the Wikipedia dump’s timestamp and the NaturalQuestions annotation process. 

We use the ambiguity annotations of Min et al. (2020) to create a subset unambiguous questions. Experiments on this unambiguous subset of the data show similar results and conclusions as the experiments on the full questions collection (Figure 12). 



<!-- Start of picture text -->
20 Total Retrieved Documents<br>(~4K tokens, unambiguous questions)<br>75<br>70<br>65<br>60<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>claude-1.3 gpt-3.5-turbo-16k-0613<br>claude-1.3-100k mpt-30b-instruct<br>gpt-3.5-turbo-0613 longchat-13b-16k<br>Accuracy<br><!-- End of picture text -->

Figure 12: Language model performance on a unambiguous subset of questions. 

# **B Random Distractors in Multi-Document QA** 

We also run multi-document question answering experiments with random Wikipedia documents as distractors, which allows us to ablate the impact of retrieved distractors (hard negatives). Note that in this setting, the the document containing the answer can often be identified with simple heuristics (e.g., lexical overlap with the query). Figure 13 presents the results of this experiment. Although all models have higher absolute accuracy in this setting, they surprisingly still struggle to reason over their entire input context, indicating that their performance degradation is not solely due to an inability to identify relevant documents.

---

[referencia=6ee83218472b4aa1 score=0.780]
# **4 Why Are Language Models Not Robust to Changes in the Position of Relevant Information?** 

Our multi-document question answering and keyvalue retrieval results show that language models struggle to robustly access and use information in long input contexts, since performance degrades significantly when changing the position of relevant information. To better understand why, we perform some preliminary investigations into the role of model architecture (decoder-only vs. encoderdecoder), query-aware contextualization, and instruction fine-tuning.

---

[referencia=6ee83218472b4aa1 score=0.768]
<!-- Start of picture text -->
20 Total Retrieved Documents<br>(~4K tokens, query-aware contextualization)<br>80<br>70<br>60<br>50<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>claude-1.3 gpt-3.5-turbo-16k-0613<br>claude-1.3-100k mpt-30b-instruct<br>gpt-3.5-turbo-0613 longchat-13b-16k<br>Accuracy<br><!-- End of picture text -->

Figure 9: Query-aware contextualization (placing the query before _and_ after the documents) does not substantially improve robustness of language models to changing the position of relevant information in multidocument QA; performance slightly increases when relevant information occurs at the very beginning, but otherwise slightly decreases. 

of the prompt and decoder-only models can only attend to prior tokens at each timestep. In contrast, encoder-decoder models (which seem more robust to changes in the position of relevant information; §4.1) use a bidirectional encoder to contextualize input contexts—can we use this observation to improve decoder-only models by placing the query before _and_ after the data, enabling query-aware contextualization of documents (or key-value pairs)? 

We find that query-aware contextualization dramatically improves performance on the key-value retrieval task—all models achieve near-perfect per- 

formance on the 75, 140, and 300 key-value pair settings. For example, GPT-3.5-Turbo (16K) with query-aware contextualization achieves perfect performance when evaluated with 300 key-value pairs. 

In contrast, without query-aware contextualization, the worst-case performance is 45.6% (Figure 7). Despite the significant impact on keyvalue retrieval performance, query-aware contextualization minimally affects performance trends in the multi-document question answering task (Figure 9); it slightly improves performance when the relevant information is located at the very beginning of the input context, but slightly decreases performance in other settings.

---

[referencia=6ee83218472b4aa1 score=0.673]
## **G.2 20 Total Retrieved Documents** 

|Model|Index 0|Index 4|Index 9|Index 14|Index 19|
|---|---|---|---|---|---|
|Claude-1.3|59.9%|55.9%|56.8%|57.2%|60.1%|
|Claude-1.3 (100K)|59.8%|55.9%|57.0%|57.4%|60.0%|
|GPT-3.5-Turbo|75.8%|57.2%|53.8%|55.4%|63.2%|
|GPT-3.5-Turbo (16K)|75.7%|57.3%|54.1%|55.4%|63.1%|
|MPT-30B-Instruct|53.7%|51.8%|52.2%|52.7%|56.3%|
|LongChat-13B (16K)|68.6%|57.4%|55.3%|52.5%|55.0%|



Table 6: Model performance when evaluated on the multi-document QA task with 20 total retrieved documents.

---

[referencia=6ee83218472b4aa1 score=0.673]
## formance is often lowest when models must use 

information in the middle of long input contexts. 

finetuned language models. ArXiv:2210.11416. Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language models beyond a fixed-length context. In _Proc. of ACL_ . 

We conduct a preliminary investigation of the role of (i) model architecture, (ii) query-aware contextualization, and (iii) instruction fine-tuning to better understand how they affect how language models use context. Finally, we conclude with a practical case study of open-domain question answering, finding that the performance of language model 

Michał Daniluk, Tim Rocktäschel, Johannes Welbl, readers saturates far before retriever recall. Our and Sebastian Riedel. 2017. Frustratingly short results and analysis provide a better understanding of how language models use their input context attention spans in neural language modeling. In _Proc. of ICLR_ . and provides new evaluation protocols for future long-context models. 

Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, 

and Christopher Ré. 2022. FlashAttention: Fast

---

[referencia=6ee83218472b4aa1 score=0.671]
## **G.3 30 Total Retrieved Documents** 

|Model|Index 0|Index 4|Index 9|Index 14|Index 19|Index 24|Index 29|
|---|---|---|---|---|---|---|---|
|Claude-1.3|59.1%|55.1%|54.8%|55.7%|56.4%|56.2%|59.9%|
|Claude-1.3 (100K)|59.1%|55.1%|54.9%|55.7%|56.6%|56.1%|60.0%|
|GPT-3.5-Turbo (16K)|73.4%|55.1%|50.5%|50.9%|51.8%|54.9%|63.7%|
|MPT-30B-Instruct|51.6%|51.3%|51.2%|49.0%|49.6%|51.3%|54.1%|
|LongChat-13B (16K)|66.9%|54.8%|52.5%|52.9%|52.2%|51.3%|55.1%|



Table 7: Model performance when evaluated on the multi-document QA task with 30 total retrieved documents.