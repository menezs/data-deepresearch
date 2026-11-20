[referencia=6ee83218472b4aa1 score=0.003]
• Even base language models (i.e., without instruction fine-tuning) show a U-shaped performance curve as we vary the position of relevant information in the input context. 

Our results indicate that prompting language 

models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. To better understand this trade-off in practice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly _one_ document that answers the question, none or many of the top _k_ documents may contain the answer in the open-domain QA setting. When retrieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model performance saturates long before retriever recall saturates, indicating that current models fail to effectively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( _∼_ 1.5% for GPT-3.5-Turbo and _∼_ 1% for claude-1.3). 

Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future longcontext models; to claim that a language model can robustly use information within long input contexts, it is necessary to show that its performance is minimally affected by the position of the relevant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data.<sup>1</sup>

---

[referencia=6ee83218472b4aa1 score=0.003]
## **2.3 Results and Discussion** 

We experiment with input contexts containing 10, 20, and 30 total documents. Figure 5 presents multidocument question answering performance when varying the position of relevant information within the input context. To contextualize model performance, we also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. 

**Model performance is highest when relevant information occurs at the beginning or end of its input context.** As illustrated in Figure 5, changing the position of relevant information in the input context leads to substantial decreases in model performance. In particular, we see a distinctive U- 

> 5We use the 0613 OpenAI model versions. 

> 6We also evaluate GPT-4 (8K) on a subset of multidocument QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute performance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. 

shaped performance curve—models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded performance when forced to use information within the middle of its input context. For example, GPT-3.5Turbo’s multi-document QA performance can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than performance without _any_ input documents (i.e., closedbook performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks.

---

[referencia=6ee83218472b4aa1 score=0.002]
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

[referencia=6ee83218472b4aa1 score=0.001]
Comparing between Llama-2 models with and without additional supervised fine-tuning and reinforcement learning from human feedback, we see that additional fine-tuning dramatically improves performance on the multi-document QA task. The 7B models with and without additional fine-tuning show minimal primacy bias, and are largely recency-biased. The 13B base model has a dramatic primacy and recency bias—there is a 20-point accuracy disparity between the best- and worst-case performance. Applying additional finetuning to the 13B seems to slightly reduce this bias (10-point worst-case degradation), but the bias remains significant. However, the 70B models with and without additional fine-tuning have largely similar trends (showing both primacy and recency bias), and additional fine-tuning minimally changes the positional bias severity. 



<!-- Start of picture text -->
20 Total Retrieved Documents (~4K tokens)<br>70<br>60<br>50<br>40<br>30<br>20<br>1st 5th 10th 15th 20th<br>Position of Document with the Answer<br>Llama-2-7b-chat-hf Llama-2-7b-hf<br>Llama-2-13b-chat-hf Llama-2-13b-hf<br>Llama-2-70b-chat-hf Llama-2-70b-hf<br>Accuracy<br><!-- End of picture text -->

Figure 16: Multi-document QA performance (20 total documents) of Llama-2 models of varying sizes (7B, 13B, 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback (“-chat-” models).

---

[referencia=6ee83218472b4aa1 score=0.001]
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

[referencia=6ee83218472b4aa1 score=0.001]
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

[referencia=6ee83218472b4aa1 score=0.001]
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

[referencia=6ee83218472b4aa1 score=0.000]
task, the key-value retrieval task admits controlled changes to the input context length (adding more 

key-value pairs) and the position of relevant in- 

formation. Although some models perform the synthetic key-value retrieval task perfectly, other models struggle to simply retrieve matching tokens that occur in the middle of their input context and continue to exhibit a U-shaped performance curve. 

We first experiment with multi-document question answering, which requires models to reason over provided documents to find relevant information and use it to answer a given question; this task 

mimics the retrieval-augmented generation setup underlying many commercial generative search and question answering applications (e.g., Bing Chat). In this setting, we control (i) the input context length by changing the number of documents in 

To better understand why language models struggle to robustly access and use information in their input contexts, we study the role of model architecture (decoder-only vs. encoder-decoder), queryaware contextualization, and instruction fine-tuning 

the input context (akin to retrieving more or less 

(§4). We find that:

---

[referencia=6ee83218472b4aa1 score=0.000]
## **G.3 30 Total Retrieved Documents** 

|Model|Index 0|Index 4|Index 9|Index 14|Index 19|Index 24|Index 29|
|---|---|---|---|---|---|---|---|
|Claude-1.3|59.1%|55.1%|54.8%|55.7%|56.4%|56.2%|59.9%|
|Claude-1.3 (100K)|59.1%|55.1%|54.9%|55.7%|56.6%|56.1%|60.0%|
|GPT-3.5-Turbo (16K)|73.4%|55.1%|50.5%|50.9%|51.8%|54.9%|63.7%|
|MPT-30B-Instruct|51.6%|51.3%|51.2%|49.0%|49.6%|51.3%|54.1%|
|LongChat-13B (16K)|66.9%|54.8%|52.5%|52.9%|52.2%|51.3%|55.1%|



Table 7: Model performance when evaluated on the multi-document QA task with 30 total retrieved documents.

---

[referencia=6ee83218472b4aa1 score=0.000]
These observations complement prior work, which found that non-instruction fine-tuned language models are biased towards recent tokens (i.e., the end of the input context; Khandelwal et al., 2018; Press et al., 2021). This recency bias has been observed in past work when evaluating models on next-word prediction of contiguous text, a setting where language models minimally benefit from long-range information (Sun et al., 2021). In contrast, our results show that language models are capable of using longer-range information (i.e., the beginning of the input context) when prompted with instruction-formatted data. We hypothesize that non-instruction fine-tuned language models learn to use these long contexts from similarlyformatted data that may occur in Internet text seen during pre-training, e.g., StackOverflow questions 

and answers. 

To better understand the effect of additional finetuning and model scale, we also experimented with Llama-2 models of varying sizes (7B, 13B, and 70B) with and without additional supervised fine-tuning and reinforcement learning from human feedback (Appendix E). We find that the U- shaped performance curve only appears in sufficiently large language models (with or without additional fine-tuning)—the 7B Llama-2 models are solely recency biased, while the 13B and 70B models exhibit a U-shaped performance curve. In addition, we see that the Llama-2 supervised fine-tuning and reinforcement learning from human feedback procedure slightly mitigates the positional bias in smaller models (13B, akin to trends shown when comparing MPT-30B and MPT-30B-Instruct), but minimally affects trends on larger models (70B).

---

[referencia=6ee83218472b4aa1 score=0.000]
Handling these use-cases requires language models to successfully operate over long sequences. Existing language models are generally implemented with Transformers (Vaswani et al., 2017), which require memory and compute that increases quadratically in sequence length. As a result, Transformer language models were often trained with relatively small context windows (between 5122048 tokens). Recent improvements in hardware (e.g., faster GPUs with more memory) and algorithms (Dai et al., 2019; Dao et al., 2022; Poli et al., 



<!-- Start of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.000]
20 Total Retrieved Documents (~4K tokens, 500 question sample) 90 

80 70 

60 50 1st 5th 10th 15th 20th Position of Document with the Answer claude-1.3 mpt-30b-instruct claude-1.3-100k longchat-13b-16k gpt-3.5-turbo-0613 gpt-4-0613 gpt-3.5-turbo-16k-0613 

Figure 15: Although GPT-4 has higher absolute performance than other models, its performance still degrades when relevant information occurs in the middle of the input context. 

ples (out of 2655) that exceed Llama-2’s maximum context length of 4096 tokens. We experiment with models of varying sizes (7B, 13B, and 70B parameters), with and without additional supervised fine-tuning and reinforcement learning from human feedback (“-chat-” models). The results are presented in Figure 16. 

Comparing Llama-2 models of varying sizes, we find that only the larger models (13B and 70B) exhibit the U-shaped performance curve (i.e., both primacy and recency bias)—the smallest Llama2 models (7B) are solely recency-biased. Given these results, we hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not previously observe any primacy bias in language models because the models they studied were too small (less than 1B parameters).

---

[referencia=6ee83218472b4aa1 score=0.000]
## **2.1 Experimental Setup** 

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) _k_ documents (e.g., passages from Wikipedia), where _exactly one_ of the documents contains the answer 

1nelsonliu.me/papers/lost-in-the-middle 

to the question and _k −_ 1 “distractor” documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. 

We instantiate this task with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. In particular, we take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). We use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts. For each of the queries, we need a document that contains the answer and _k −_ 1 distractor documents that do not contain the answer. To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations. 

To collect _k −_ 1 distractor documents that do not contain the answer, we use a retrieval system (Contriever, fine-tuned on MS-MARCO; Izacard et al., 2021) to retrieve the _k −_ 1 Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers.<sup>2,3</sup> In the input context, the distractor documents are presented in order of decreasing relevance.<sup>4</sup> 

To modulate the position of relevant information within the input context, we adjust the order of the documents to change the position of the document that contains the answer (Figure 3). To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure 4). 

Following Kandpal et al. (2022) and Mallen et al. (2023), we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.

---

[referencia=6ee83218472b4aa1 score=0.000]
## guage models is perhaps surprising, since the self- 

former. ArXiv:2004.05150. 

attention mechanisms underlying Transformer language models is technically equally capable of retrieving any token from their contexts. **7 Conclusion** 

Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob 

We empirically study how language models use long input contexts via a series of controlled experiments. We show that language model performance degrades significantly when changing the position of relevant information, indicating that models struggle to robustly access and use infor- 

mation in long input contexts. In particular, per- 

Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-

---

[referencia=6ee83218472b4aa1 score=0.000]
# **6 Related Work** 

## **6.1 Long-Context Language Models** 

There is much prior work in designing performant language models with cheaper scaling than Transformers in the context length. Many lines of work pursue Transformer variants with attention modifications like recurrence (Dai et al., 2019), factorizing attention into computationally less intensive approximations (Beltagy et al., 2020; Zaheer et al., 2020), or low-rank approximations (Wang et al., 2020; Peng et al., 2021). Dao et al. (2022) instead provide a faster exact attention by a carefully- 

crafted IO-aware CUDA kernel. Separately, there are attempts to do away with attention entirely to remove quadratic sequence length complexity, often through convolution and/or linear RNNs, e.g., in RWKV (Peng, 2023), S4 (Gu et al., 2022), or Hyena (Poli et al., 2023). Many prior efforts evaluate perplexity on a diverse web corpus as a proxy for the ability to process long contexts; this work shows that precise knowledge access on long contexts may be an added challenge.

---

[referencia=6ee83218472b4aa1 score=0.000]
# **5 Is More Context Is Always Better? A Case Study With Open-Domain QA** 

Our results indicate that prompting language models with longer input contexts is a trade-off— providing the language model with more information may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. Even if a language model can take in 16K tokens, is it actually beneficial to provide 16K tokens of context? The answer to this question is ultimately downstream task-specific since it depends on the marginal value of the added context and the model’s ability to effectively use long input contexts, but we perform a case study with opendomain question answering on NaturalQuestionsOpen to better understand this trade-off in existing language models. 

We use language models in a standard retrieverreader setup. A retrieval system (Contriever, finetuned on MS-MARCO) takes an input query from NaturalQuestions-Open and returns the _k_ documents from Wikipedia with the highest relevance score. To condition language models on these retrieved documents, we simply include them in the prompt. We evaluate retriever recall and reader accuracy (whether any of the annotated answers appear in the predicted output) as a function of the number of retrieved documents _k_ . We use a subset of NaturalQuestions-Open where the long answer is a paragraph (as opposed to a table or a list). 

Figure 11 presents retriever recall and open- 



<!-- Start of picture text -->
90<br>80<br>70<br>60<br>50<br>5 10 20 30 40 50<br>Number of Retrieved Docs<br>claude-1.3 mpt-30b-instruct<br>claude-1.3-100k longchat-13b-16k<br>gpt-3.5-turbo-0613 contriever recall<br>gpt-3.5-turbo-16k-0613<br>Metric<br><!-- End of picture text -->

Figure 11: Retriever recall and model performance as a function of the number of retrieved documents. Model performance saturates long before retriever recall, indicating that the models have difficulty making use of the extra retrieved documents.

---

[referencia=6ee83218472b4aa1 score=0.000]
# **G Full Multi-Document Question Answering Results** 

This section tabulates model performance when evaluated on the multi-document QA task with varying numbers of documents (Figure 5). “Index _n_ ” indicates performance when the document with the answer occurs at position _n_ + 1, where lower indices are closer to the start of the input context. For example, index 0 refers to performance when the document with the answer is placed at the very start of the context (i.e., first amongst all documents). 

## **G.1 10 Total Retrieved Documents** 

|Model|Index 0|Index 4|Index 9|
|---|---|---|---|
|Claude-1.3|62.9%|58.3%|59.7%|
|Claude-1.3 (100K)|63.1%|58.3%|59.7%|
|GPT-3.5-Turbo|76.8%|61.2%|62.4%|
|GPT-3.5-Turbo (16K)|76.9%|61.0%|62.5%|
|MPT-30B-Instruct|60.2%|56.2%|59.7%|
|LongChat-13B (16K)|72.1%|58.9%|58.5%|



Table 5: Model performance when evaluated on the multi-document QA task with 10 total retrieved documents.

---

[referencia=6ee83218472b4aa1 score=0.000]
## **4.2 Effect of Query-Aware Contextualization** 

Our multi-document QA and key-value retrieval experiments place the query (i.e., question to answer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or keyvalue pairs, since the query only appears at the end 



<!-- Start of picture text -->
10 Total Retrieved Documents (~2K tokens) 20 Total Retrieved Documents (~4K tokens) 30 Total Retrieved Documents (~6K tokens)<br>70 70 70<br>65 65 65<br>60 60 60<br>55 55 55<br>50 50 50<br>1st 5th 10th 1st 5th 10th 15th 20th 1st 5th 10th 15th 20th 25th 30th<br>Position of Document with the Answer Position of Document with the Answer Position of Document with the Answer<br>mpt-30b-instruct longchat-13b-16k flan-t5-xxl flan-ul2<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->

Figure 8: When encoder-decoder models (Flan-UL2 and Flan-T5-XXL) evaluated on sequences that are _shorter_ than their encoder’s training-time maximum sequence length (2048 and 512 tokens, respectively), they are relatively robust to changes in the position of relevant information within their input context (left subplot). In contrast, when these models are evaluated on sequences _longer_ than those seen during training (center and right subplots), we observe a U-shaped performance curve—performance is higher when relevant information occurs at the beginning or end of the input context, as opposed to the middle of the input context. 



<!-- Start of picture text -->

---

[referencia=6ee83218472b4aa1 score=0.000]
<!-- Start of picture text -->
2023; Rubin and Berant, 2023, inter alia ) have document question task is lower than its perfor-<br>resulted in language models with larger context mance when predicting  without any documents  (i.e.,<br>windows (e.g., 4096, 32K, and even 100K tokens), the closed-book setting; 56.1%). Furthermore, we<br>but it remains unclear how these extended-context find that models often have identical performance<br>language models make use of their input contexts to their extended-context counterparts, indicating<br>when performing downstream tasks. that extended-context models are not necessarily<br>We empirically investigate this question via better at using their input context (§2.3).<br>Given that language models struggle to retrieve<br>controlled experiments with a variety of state-of-<br>and use relevant information in the multi-document<br>the-art open (MPT-30B-Instruct, LongChat-13B<br>question answering task, to what extent can lan-<br>(16K)) and closed (OpenAI’s GPT-3.5-Turbo and<br>Anthropic’s Claude-1.3) language models in set- guage models even  retrieve  from their input con-<br>texts? We study this question with a synthetic key-<br>tings that require accessing and using information<br>value retrieval task, which is designed to be a mini-<br>within an input context. In particular, our experi-<br>mal testbed for the basic ability to retrieve matching<br>ments make controlled changes to the input context<br>size and the position of the relevant information tokens from the input context. In this task, models<br>are given a collection of JSON-formatted key-value<br>within the input context and study their effects on<br>pairs and must return the value associated with a<br>language model performance. If language models<br>specific key. Similar to the multi-document QA<br><!-- End of picture text -->

can robustly use information within long input contexts, then their performance should be _minimally affected_ by the position of the relevant information in the input context. 

task, the key-value retrieval task admits controlled changes to the input context length (adding more 

key-value pairs) and the position of relevant in-

---

[referencia=6ee83218472b4aa1 score=0.000]
## **2.2 Models** 

We analyze several state-of-the-art open and closed language models. We use greedy decoding when generating outputs and leave exploration of other decoding methods to future work. We use a standard set of prompts for each model (Figure 2). 

**Open models.** We experiment with MPT-30BInstruct, which has a maximum context length of 8192 tokens. The model was initially pre-trained on 1 trillion tokens using 2048-token sequences, followed by an additional sequence length adaptation pre-training phase on 50 billion tokens using 8192-token sequences. MPT-30B-Instruct uses ALiBi (Press et al., 2022) to represent positional information. We also evaluate LongChat-13B (16K) (Li et al., 2023), which extends the LLaMA-13B (Touvron et al., 2023a) context window from 2048 to 16384 tokens by using condensed rotary positional embeddings before fine-tuning with 16384-token sequences. 

**Closed models.** We use the OpenAI API to experiment with GPT-3.5-Turbo and GPT-3.5-Turbo 



<!-- Start of picture text -->
10 Total Retrieved Documents (~2K tokens) 20 Total Retrieved Documents (~4K tokens) 30 Total Retrieved Documents (~6K tokens)<br>75 75 75<br>70 70 70<br>65 65 65<br>60 60 60<br>55 55 55<br>50 50 50<br>1st 5th 10th 1st 5th 10th 15th 20th 1st 5th 10th 15th 20th 25th 30th<br>Position of Document with the Answer Position of Document with the Answer Position of Document with the Answer<br>claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k<br>Accuracy Accuracy Accuracy<br><!-- End of picture text -->