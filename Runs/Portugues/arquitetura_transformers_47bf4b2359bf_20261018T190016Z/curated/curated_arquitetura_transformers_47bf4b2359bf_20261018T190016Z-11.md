[referencia=02ad74cdb0c9081f score=0.830]
Figure 1: Overview of our approach. We combine a pre-trained retriever ( _Query Encoder_ + _Document Index_ ) with a pre-trained seq2seq model ( _Generator_ ) and fine-tune end-to-end. For query _x_ , we use Maximum Inner Product Search (MIPS) to find the top-K documents _zi_ . For final prediction _y_ , we treat _z_ as a latent variable and marginalize over seq2seq predictions given different documents. 

but have only explored open-domain extractive question answering. Here, we bring hybrid parametric and non-parametric memory to the “workhorse of NLP,” i.e. sequence-to-sequence (seq2seq) models. 

We endow pre-trained, parametric-memory generation models with a non-parametric memory through a general-purpose fine-tuning approach which we refer to as retrieval-augmented generation (RAG). We build RAG models where the parametric memory is a pre-trained seq2seq transformer, and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We combine these components in a probabilistic model trained end-to-end (Fig. 1). The retriever (Dense Passage Retriever [26], henceforth DPR) provides latent documents conditioned on the input, and the seq2seq model (BART [32]) then conditions on these latent documents together with the input to generate the output. We marginalize the latent documents with a top-K approximation, either on a per-output basis (assuming the same document is responsible for all tokens) or a per-token basis (where different documents are responsible for different tokens). Like T5 [51] or BART, RAG can be fine-tuned on any seq2seq task, whereby both the generator and retriever are jointly learned. 

There has been extensive previous work proposing architectures to enrich systems with non-parametric memory which are trained from scratch for specific tasks, e.g. memory networks [64, 55], stackaugmented networks [25] and memory layers [30]. In contrast, we explore a setting where both parametric and non-parametric memory components are pre-trained and pre-loaded with extensive knowledge. Crucially, by using pre-trained access mechanisms, the ability to access knowledge is present without additional training.

---

[referencia=02ad74cdb0c9081f score=0.643]
**Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** 



<!-- Start of picture text -->
Patrick Lewis †‡ , Ethan Perez ⋆ ,<br>Aleksandra Piktus † , Fabio Petroni † , Vladimir Karpukhin † , Naman Goyal † , Heinrich Küttler † ,<br>Mike Lewis † , Wen-tau Yih † , Tim Rocktäschel †‡ , Sebastian Riedel †‡ , Douwe Kiela †<br>† Facebook AI Research; ‡ University College London; ⋆ New York University;<br>plewis@fb.com<br><!-- End of picture text -->

**Abstract** 



<!-- Start of picture text -->
Large pre-trained language models have been shown to store factual knowledge<br>in their parameters, and achieve state-of-the-art results when fine-tuned on down-<br>stream NLP tasks. However, their ability to access and precisely manipulate knowl-<br>edge is still limited, and hence on knowledge-intensive tasks, their performance<br>lags behind task-specific architectures. Additionally, providing provenance for their<br>decisions and updating their world knowledge remain open research problems. Pre-<br>trained models with a differentiable access mechanism to explicit non-parametric<br>memory have so far been only investigated for extractive downstream tasks. We<br>explore a general-purpose fine-tuning recipe for retrieval-augmented generation<br>(RAG) — models which combine pre-trained parametric and non-parametric mem-<br>ory for language generation. We introduce RAG models where the parametric<br>memory is a pre-trained seq2seq model and the non-parametric memory is a dense<br>vector index of Wikipedia, accessed with a pre-trained neural retriever. We com-<br>pare two RAG formulations, one which conditions on the same retrieved passages<br>across the whole generated sequence, and another which can use different passages<br><!-- End of picture text -->

per token. We fine-tune and evaluate our models on a wide range of knowledgeintensive NLP tasks and set the state of the art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate

---

[referencia=02ad74cdb0c9081f score=0.619]
Our results highlight the benefits of combining parametric and non-parametric memory with generation for _knowledge-intensive tasks_ —tasks that humans could not reasonably be expected to perform without access to an external knowledge source. Our RAG models achieve state-of-the-art results on open Natural Questions [29], WebQuestions [3] and CuratedTrec [2] and strongly outperform recent approaches that use specialised pre-training objectives on TriviaQA [24]. Despite these being extractive tasks, we find that unconstrained generation outperforms previous extractive approaches. For knowledge-intensive generation, we experiment with MS-MARCO [1] and Jeopardy question generation, and we find that our models generate responses that are more factual, specific, and diverse than a BART baseline. For FEVER [56] fact verification, we achieve results within 4.3% of state-of-the-art pipeline models which use strong retrieval supervision. Finally, we demonstrate that the non-parametric memory can be replaced to update the models’ knowledge as the world changes.<sup>1</sup>

---

[referencia=02ad74cdb0c9081f score=0.355]
# **G Parameters** 

Our RAG models contain the trainable parameters for the BERT-base query and document encoder of DPR, with 110M parameters each (although we do not train the document encoder ourselves) and 406M trainable parameters from BART-large, 406M parameters, making a total of 626M trainable 

18 

Table 7: Number of instances in the datasets used. *A hidden subset of this data is used for evaluation 

Task Train Development Test Natural Questions 79169 8758 3611 TriviaQA 78786 8838 11314 WebQuestions 3418 362 2033 CuratedTrec 635 134 635 Jeopardy Question Generation 97392 13714 26849 MS-MARCO 153726 12468 101093* FEVER-3-way 145450 10000 10000 FEVER-2-way 96966 6666 6666 

parameters. The best performing "closed-book" (parametric only) open-domain QA model is T5-11B with 11 Billion trainable parameters. The T5 model with the closest number of parameters to our 

models is T5-large (770M parameters), which achieves a score of 28.9 EM on Natural Questions [52], substantially below the 44.5 that RAG-Sequence achieves, indicating that hybrid parametric/nonparametric models require far fewer trainable parameters for strong open-domain QA performance. The non-parametric memory index does not consist of trainable parameters, but does consists of 21M 728 dimensional vectors, consisting of 15.3B values. These can be easily be stored at 8-bit floating point precision to manage memory and disk footprints. 

**H Retrieval Collapse** 

In preliminary experiments, we observed that for some tasks such as story generation [11], the retrieval component would “collapse” and learn to retrieve the same documents regardless of the input. In these cases, once retrieval had collapsed, the generator would learn to ignore the documents, and the RAG model would perform equivalently to BART. The collapse could be due to a less-explicit requirement for factual knowledge in some tasks, or the longer target sequences, which could result in less informative gradients for the retriever. Perez et al. [46] also found spurious retrieval results when optimizing a retrieval component in order to improve performance on downstream tasks. 

**I Number of instances per dataset**

---

[referencia=02ad74cdb0c9081f score=0.349]
||Model|NQ|TQA|WQ|CT||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Cld|T511B 52|345|/501|374||Model|Jeop|ardy|MSM|ARCO|FVR3|FVR2|
|ose<br>Book|- []<br>T5-11B+SSM[52]|.<br>36.6|- .<br>- /60.5|.<br>44.7|-<br>-||B-1|QB-1|R-L|B-1|Label|Acc.|
|Open|REALM [20]|40.4|- / -|40.7|46.8|SotA|-|-|**49.8* **|**49.9***|**76.8**|**92.2***|
|Book|DPR [26]|41.5|**57.9**/ -|41.1|50.6|BART|15.1|19.7|38.2|41.6|64.0|81.1|
||RAG-Token|44.1|55.2/66.1|**45.5**|50.0|RAG-Tok.|**17.3**|**22.2**|40.1|41.5|725|895|
||RAG-Seq.|**44.5**|56.8/**68.0**|45.2|**52.2**|RAG-Seq.|14.7|21.4|40.8|44.2|.|.|



to more effective marginalization over documents. Furthermore, RAG can generate correct answers even when the correct answer is not in any retrieved document, achieving 11.8% accuracy in such cases for NQ, where an extractive model would score 0%.

---

[referencia=02ad74cdb0c9081f score=0.267]
[67] Shiyue Zhang and Mohit Bansal. Addressing semantic drift in question generation for semisupervised question answering. In _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)_ , pages 2495–2509, Hong Kong, China, November 2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1253. URL `https://www.aclweb.org/anthology/D19-1253` . 

[68] Wanjun Zhong, Jingjing Xu, Duyu Tang, Zenan Xu, Nan Duan, Ming Zhou, Jiahai Wang, and Jian Yin. Reasoning over semantic-level graph for fact checking. _ArXiv_ , abs/1909.03745, 2019. URL `https://arxiv.org/abs/1909.03745` . 

16 



<!-- Start of picture text -->
Appendices for  Retrieval-Augmented Generation for<br>Knowledge-Intensive NLP Tasks<br>A Implementation Details<br>For Open-domain QA we report test numbers using 15 retrieved documents for RAG-Token models.<br>For RAG-Sequence models, we report test results using 50 retrieved documents, and we use the<br>Thorough Decoding approach since answers are generally short. We use greedy decoding for QA as<br>we did not find beam search improved results. For Open-MSMarco and Jeopardy question generation,<br>we report test numbers using ten retrieved documents for both RAG-Token and RAG-Sequence,<br>and we also train a BART-large model as a baseline. We use a beam size of four, and use the Fast<br>Decoding approach for RAG-Sequence models, as Thorough Decoding did not improve performance.<br>B Human Evaluation<br><!-- End of picture text -->



Figure 4: Annotation interface for human evaluation of factuality. A pop-out for detailed instructions and a worked example appear when clicking "view tool guide".

---

[referencia=02ad74cdb0c9081f score=0.254]
**Memory-based Architectures** Our document index can be seen as a large external memory for neural networks to attend to, analogous to memory networks [64, 55]. Concurrent work [14] learns to retrieve a trained embedding for each entity in the input, rather than to retrieve raw text as in our work. Other work improves the ability of dialog models to generate factual text by attending over fact embeddings [15, 13]. A key feature of our memory is that it is comprised of raw text rather distributed representations, which makes the memory both (i) human-readable, lending a form of interpretability to our model, and (ii) human-writable, enabling us to dynamically update the model’s memory by editing the document index. This approach has also been used in knowledge-intensive dialog, where generators have been conditioned on retrieved text directly, albeit obtained via TF-IDF rather than end-to-end learnt retrieval [9]. 

**Retrieve-and-Edit approaches** Our method shares some similarities with retrieve-and-edit style approaches, where a similar training input-output pair is retrieved for a given input, and then edited to provide a final output. These approaches have proved successful in a number of domains including Machine Translation [18, 22] and Semantic Parsing [21]. Our approach does have several differences, including less of emphasis on lightly editing a retrieved item, but on aggregating content from several pieces of retrieved content, as well as learning latent retrieval, and retrieving evidence documents rather than related training pairs. This said, RAG techniques may work well in these settings, and could represent promising future work. 

# **6 Discussion** 

In this work, we presented hybrid generation models with access to parametric and non-parametric memory. We showed that our RAG models obtain state of the art results on open-domain QA. We found that people prefer RAG’s generation over purely parametric BART, finding RAG more factual and specific. We conducted an thorough investigation of the learned retrieval component, validating its effectiveness, and we illustrated how the retrieval index can be hot-swapped to update the model without requiring any retraining. In future work, it may be fruitful to investigate if the two components can be jointly pre-trained from scratch, either with a denoising objective similar to BART or some another objective. Our work opens up new research directions on how parametric and non-parametric memories interact and how to most effectively combine them, showing promise in being applied to a wide variety of NLP tasks. 

9

---

[referencia=02ad74cdb0c9081f score=0.185]
## **4.4** 

Table 2 shows our results on FEVER. For 3-way classification, RAG scores are within 4.3% of state-of-the-art models, which are complex pipeline systems with domain-specific architectures and substantial engineering, trained using intermediate retrieval supervision, which RAG does not require. 

6 



<!-- Start of picture text -->
Document 1 : his works are considered classics of American Doc 1<br>literature ... His wartime experiences formed the basis for his novel Doc 2<br>”A Farewell to Arms”  (1929) ... Doc 3<br>Document 2 : ... artists of the 1920s ”Lost Generation” expatriate Doc 4<br>community. His debut novel,  ”The Sun Also Rises” , was published<br>in 1926. Doc 5<br>BOS ” TheSunAlsoR ises ” is a novelbythisauthorof ” AFarewell toArms”<br><!-- End of picture text -->

Figure 2: RAG-Token document posterior _p_ ( _zi|x, yi, y−i_ ) for each generated token for input “Hemingway" for Jeopardy generation with 5 retrieved documents. The posterior for document 1 is high when generating “A Farewell to Arms" and for document 2 when generating “The Sun Also Rises". 

Table 3: Examples from generation tasks. RAG models generate more specific and factually accurate responses. ‘?’ indicates factually incorrect responses, * indicates partially correct responses.

---

[referencia=02ad74cdb0c9081f score=0.185]
Jeopardy questions often contain two separate pieces of information, and RAG-Token may perform best because it can generate responses that combine content from several documents. Figure 2 shows an example. When generating “Sun”, the posterior is high for document 2 which mentions “The Sun Also Rises”. Similarly, document 1 dominates the posterior when “A Farewell to Arms” is generated. Intriguingly, after the first token of each book is generated, the document posterior flattens. This observation suggests that the generator can complete the titles without depending on specific documents. In other words, the model’s parametric knowledge is sufficient to complete the titles. We find evidence for this hypothesis by feeding the BART-only baseline with the partial decoding <mark>`"The Sun` .</mark> BART completes the generation <mark>`"The Sun Also Rises"`</mark> `is a` <mark>`novel`</mark> `by` <mark>`this`</mark> `a` <mark>`uthor`</mark> `of` <mark>`"The Sun Also Rises"`</mark> indicating the title "The Sun Also Rises" is stored in BART’s parameters. Similarly, BART will complete the partial decoding <mark>`"The Sun Also Rises"`</mark> `is a` <mark>`novel`</mark> `by` <mark>`this`</mark> `a` <mark>`uthor`</mark> `of "A` with <mark>`"The Sun Also Rises"`</mark> `is a` <mark>`novel`</mark> `by` <mark>`this`</mark> `a` <mark>`uthor`</mark> `of "A` <mark>`Farewell`</mark> `to` <mark>`Arms"` .</mark> This example shows how parametric and non-parametric memories _work together_ —the non-parametric component helps to guide the generation, drawing out specific knowledge stored in the parametric memory.

---

[referencia=02ad74cdb0c9081f score=0.137]
# **3 Experiments** 

We experiment with RAG in a wide range of knowledge-intensive tasks. For all experiments, we use a single Wikipedia dump for our non-parametric knowledge source. Following Lee et al. [31] and Karpukhin et al. [26], we use the December 2018 dump. Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents. We use the document encoder to compute an embedding for each document, and build a single MIPS index using FAISS [23] with a Hierarchical Navigable Small World approximation for fast retrieval [37]. During training, we retrieve the top _k_ documents for each query. We consider _k ∈{_ 5 _,_ 10 _}_ for training and set _k_ for test time using dev data. We now discuss experimental details for each task. 

## **3.1 Open-domain Question Answering** 

Open-domain question answering (QA) is an important real-world application and common testbed for knowledge-intensive tasks [20]. We treat questions and answers as input-output text pairs ( _x, y_ ) and train RAG by directly minimizing the negative log-likelihood of answers. We compare RAG to the popular extractive QA paradigm [5, 7, 31, 26], where answers are extracted spans from retrieved documents, relying primarily on non-parametric knowledge. We also compare to “Closed-Book QA” approaches [52], which, like RAG, generate answers, but which do not exploit retrieval, instead relying purely on parametric knowledge. We consider four popular open-domain QA datasets: Natural Questions (NQ) [29], TriviaQA (TQA) [24]. WebQuestions (WQ) [3] and CuratedTrec (CT) [2]. As CT and WQ are small, we follow DPR [26] by initializing CT and WQ models with our NQ RAG model. We use the same train/dev/test splits as prior work [31, 26] and report Exact Match (EM) scores. For TQA, to compare with T5 [52], we also evaluate on the TQA Wiki test set.

---

[referencia=02ad74cdb0c9081f score=0.110]
For 2-way classification, we compare against Thorne and Vlachos [57], who train RoBERTa [35] to classify the claim as true or false given the gold evidence sentence. RAG achieves an accuracy within 2.7% of this model, despite being supplied with only the claim and retrieving its own evidence. We also analyze whether documents retrieved by RAG correspond to documents annotated as gold evidence in FEVER. We calculate the overlap in article titles between the top _k_ documents retrieved by RAG and gold evidence annotations. We find that the top retrieved document is from a gold article in 71% of cases, and a gold article is present in the top 10 retrieved articles in 90% of cases.

---

[referencia=02ad74cdb0c9081f score=0.104]
# **Broader Impact** 

This work offers several positive societal benefits over previous work: the fact that it is more strongly grounded in real factual knowledge (in this case Wikipedia) makes it “hallucinate” less with generations that are more factual, and offers more control and interpretability. RAG could be employed in a wide variety of scenarios with direct benefit to society, for example by endowing it with a medical index and asking it open-domain questions on that topic, or by helping people be more effective at their jobs. 

With these advantages also come potential downsides: Wikipedia, or any potential external knowledge source, will probably never be entirely factual and completely devoid of bias. Since RAG can be employed as a language model, similar concerns as for GPT-2 [50] are valid here, although arguably to a lesser extent, including that it might be used to generate abuse, faked or misleading content in the news or on social media; to impersonate others; or to automate the production of spam/phishing content [54]. Advanced language models may also lead to the automation of various jobs in the coming decades [16]. In order to mitigate these risks, AI systems could be employed to fight against misleading content and automated spam/phishing. 

# **Acknowledgments** 

The authors would like to thank the reviewers for their thoughtful and constructive feedback on this paper, as well as HuggingFace for their help in open-sourcing code to run RAG models. The authors would also like to thank Kyunghyun Cho and Sewon Min for productive discussions and advice. EP thanks supports from the NSF Graduate Research Fellowship. PL is supported by the FAIR PhD program.

---

[referencia=02ad74cdb0c9081f score=0.101]
## **4.5 Additional Results** 

**Generation Diversity** Section 4.3 shows that RAG models are more factual and specific than BART for Jeopardy question generation. Following recent work on diversity-promoting decoding [33, 59, 39], we also investigate generation diversity by calculating the ratio of distinct ngrams to total ngrams generated by different models. Table 5 shows that RAG-Sequence’s generations are more diverse than RAG-Token’s, and both are significantly more diverse than BART without needing any diversity-promoting decoding. 

**Retrieval Ablations** A key feature of RAG is learning to retrieve relevant information for the task. To assess the effectiveness of the retrieval mechanism, we run ablations where we freeze the retriever during training. As shown in Table 6, learned retrieval improves results for all tasks. 

We compare RAG’s dense retriever to a word overlap-based BM25 retriever [53]. Here, we replace RAG’s retriever with a fixed BM25 system, and use BM25 retrieval scores as logits when calculating _p_ ( _z|x_ ). Table 6 shows the results. For FEVER, BM25 performs best, perhaps since FEVER claims are heavily entity-centric and thus well-suited for word overlap-based retrieval. Differentiable retrieval improves results on all other tasks, especially for Open-Domain QA, where it is crucial. 

**Index hot-swapping** An advantage of non-parametric memory models like RAG is that knowledge can be easily updated at test time. Parametric-only models like T5 or BART need further training to update their behavior as the world changes. To demonstrate, we build an index using the DrQA [5] Wikipedia dump from December 2016 and compare outputs from RAG using this index to the newer index from our main results (December 2018). We prepare a list of 82 world leaders who had changed 

7 

Table 4: Human assessments for the Jeopardy Table 5: Ratio of distinct to total tri-grams for Question Generation Task. generation tasks.

---

[referencia=02ad74cdb0c9081f score=0.091]
more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline. **1 Introduction** Pre-trained neural language models have been shown to learn a substantial amount of in-depth knowledge from data [47]. They can do so without any access to an external memory, as a parameterized implicit knowledge base [51, 52]. While this development is exciting, such models do have downsides: They cannot easily expand or revise their memory, can’t straightforwardly provide insight into their predictions, and may produce “hallucinations” [38]. Hybrid models that combine parametric memory with non-parametric (i.e., retrieval-based) memories [20, 26, 48] can address some of these issues because knowledge can be directly revised and expanded, and accessed knowledge can be 

inspected and interpreted. REALM [20] and ORQA [31], two recently introduced models that combine masked language models [8] with a differentiable retriever, have shown promising results, 



<!-- Start of picture text -->
Define "middle ear" (x) The middle ear includes<br>Question Answering: End-to-End Backprop through  q  and  pθ the tympanic cavity andthe three ossicles.   (y)<br>Question Query EncoderQuery Retriever pη DocumentIndex Generator pθ Question Answering:Answer Generation<br>Barack Obama was (Non-Parametric) (Parametric)<br>born in Hawaii. (x) q(x) d(z) z4 supports  (y)<br>Fact Verification: Fact Query z2 z3 Margin-alize Label GenerationFact Verification:<br>The DivineComedy  (x) q MIPS z1 pθ This 14th century workis divided into 3<br>Jeopardy Question sections: "Inferno",<br>Generation: "Purgatorio" &<br>Answer Query "Paradiso"          (y)<br>Question Generation<br><!-- End of picture text -->

---

[referencia=02ad74cdb0c9081f score=0.064]
## **4.1 Open-domain Question Answering** 

Table 1 shows results for RAG along with state-of-the-art models. On all four open-domain QA tasks, RAG sets a new state of the art (only on the T5-comparable split for TQA). RAG combines the generation flexibility of the “closed-book” (parametric only) approaches and the performance of "open-book" retrieval-based approaches. Unlike REALM and T5+SSM, RAG enjoys strong results without expensive, specialized “salient span masking” pre-training [20]. It is worth noting that RAG’s retriever is initialized using DPR’s retriever, which uses retrieval supervision on Natural Questions and TriviaQA. RAG compares favourably to the DPR QA system, which uses a BERT-based “crossencoder” to re-rank documents, along with an extractive reader. RAG demonstrates that neither a re-ranker nor extractive reader is necessary for state-of-the-art performance. 

There are several advantages to generating answers even when it is possible to extract them. Documents with clues about the answer but do not contain the answer verbatim can still contribute towards a correct answer being generated, which is not possible with standard extractive approaches, leading 

5 

Table 1: Open-Domain QA Test Scores. For TQA, left column uses the standard test set for OpenDomain QA, right column uses the TQA-Wiki test set. See Appendix D for further details. 

Table 2: Generation and classification Test Scores. MS-MARCO SotA is [4], FEVER-3 is [68] and FEVER-2 is [57] *Uses gold context/evidence. Best model without gold access underlined.

---

[referencia=02ad74cdb0c9081f score=0.062]
## **3.2 Abstractive Question Answering** 

RAG models can go beyond simple extractive QA and answer questions with free-form, abstractive text generation. To test RAG’s natural language generation (NLG) in a knowledge-intensive setting, we use the MSMARCO NLG task v2.1 [43]. The task consists of questions, ten gold passages retrieved from a search engine for each question, and a full sentence answer annotated from the retrieved passages. We do not use the supplied passages, only the questions and answers, to treat 

4 

MSMARCO as an open-domain abstractive QA task. MSMARCO has some questions that cannot be answered in a way that matches the reference answer without access to the gold passages, such as “What is the weather in Volcano, CA?” so performance will be lower without using gold passages. We also note that some MSMARCO questions cannot be answered using Wikipedia alone. Here, RAG can rely on parametric knowledge to generate reasonable responses.

---

[referencia=02ad74cdb0c9081f score=0.055]
## **3.4** 

FEVER [56] requires classifying whether a natural language claim is supported or refuted by Wikipedia, or whether there is not enough information to decide. The task requires retrieving evidence from Wikipedia relating to the claim and then reasoning over this evidence to classify whether the claim is true, false, or unverifiable from Wikipedia alone. FEVER is a retrieval problem coupled with an challenging entailment reasoning task. It also provides an appropriate testbed for exploring the RAG models’ ability to handle classification rather than generation. We map FEVER class labels (supports, refutes, or not enough info) to single output tokens and directly train with claim-class pairs. Crucially, unlike most other approaches to FEVER, we do not use supervision on retrieved evidence. In many real-world applications, retrieval supervision signals aren’t available, and models that do not require such supervision will be applicable to a wider range of tasks. We explore two variants: the standard 3-way classification task (supports/refutes/not enough info) and the 2-way (supports/refutes) task studied in Thorne and Vlachos [57]. In both cases we report label accuracy.

---

[referencia=02ad74cdb0c9081f score=0.046]
# **2 Methods** 

We explore RAG models, which use the input sequence _x_ to retrieve text documents _z_ and use them as additional context when generating the target sequence _y_ . As shown in Figure 1, our models leverage two components: (i) a retriever _pη_ ( _z|x_ ) with parameters _η_ that returns (top-K truncated) distributions over text passages given a query _x_ and (ii) a generator _pθ_ ( _yi|x, z, y_ 1: _i−_ 1) parametrized 

> 1Code to run experiments with RAG has been open-sourced as part of the HuggingFace Transformers Library [66] and can be found at `https://github.com/huggingface/transformers/blob/master/ examples/rag/` . An interactive demo of RAG models can be found at `https://huggingface.co/rag/` 

2 

by _θ_ that generates a current token based on a context of the previous _i −_ 1 tokens _y_ 1: _i−_ 1, the original input _x_ and a retrieved passage _z_ . 

To train the retriever and generator end-to-end, we treat the retrieved document as a latent variable. We propose two models that marginalize over the latent documents in different ways to produce a distribution over generated text. In one approach, _RAG-Sequence_ , the model uses the same document to predict each target token. The second approach, _RAG-Token_ , can predict each target token based on a different document. In the following, we formally introduce both models and then describe the _pη_ and _pθ_ components, as well as the training and decoding procedure.

---

[referencia=02ad74cdb0c9081f score=0.038]
## **4.2 Abstractive Question Answering** 

As shown in Table 2, RAG-Sequence outperforms BART on Open MS-MARCO NLG by 2.6 Bleu points and 2.6 Rouge-L points. RAG approaches state-of-the-art model performance, which is impressive given that (i) those models access gold passages with specific information required to generate the reference answer , (ii) many questions are unanswerable without the gold passages, and (iii) not all questions are answerable from Wikipedia alone. Table 3 shows some generated answers from our models. Qualitatively, we find that RAG models hallucinate less and generate factually correct text more often than BART. Later, we also show that RAG generations are more diverse than BART generations (see §4.5).

---

[referencia=02ad74cdb0c9081f score=0.030]
## **4.3 Jeopardy Question Generation** 

Table 2 shows that RAG-Token performs better than RAG-Sequence on Jeopardy question generation, with both models outperforming BART on Q-BLEU-1. 4 shows human evaluation results, over 452 pairs of generations from BART and RAG-Token. Evaluators indicated that BART was more factual than RAG in only 7.1% of cases, while RAG was more factual in 42.7% of cases, and both RAG and BART were factual in a further 17% of cases, clearly demonstrating the effectiveness of RAG on the task over a state-of-the-art generation model. Evaluators also find RAG generations to be more specific by a large margin. Table 3 shows typical generations from each model.