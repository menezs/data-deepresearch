[referencia=ea6afdae27cfb441 score=0.407]
## **1 Introduction** 

Foundation models are general models of language, vision, speech, and/or other modalities that are designed to support a large variety of AI tasks. They form the basis of many modern AI systems. 

The development of modern foundation models consists of two main stages: **(1)** a pre-training stage in which the model is trained at massive scale using straightforward tasks such as next-word prediction or captioning and **(2)** a post-training stage in which the model is tuned to follow instructions, align with human preferences, and improve specific capabilities (for example, coding and reasoning). 

In this paper, we present a new set of foundation models for language, called **Llama 3** . The Llama 3 Herd of models natively supports multilinguality, coding, reasoning, and tool usage. Our largest model is dense Transformer with 405B parameters, processing information in a context window of up to 128K tokens. Each member of the herd is listed in Table 1. All the results presented in this paper are for the Llama 3.1 models, which we will refer to as Llama 3 throughout for brevity. 

We believe there are three key levers in the development of high-quality foundation models: data, scale, and managing complexity. We seek to optimize for these three levers in our development process: 

- **Data.** Compared to prior versions of Llama (Touvron et al., 2023a,b), we improved both the quantity and quality of the data we use for pre-training and post-training. These improvements include the development of more careful pre-processing and curation pipelines for pre-training data and the development of more rigorous quality assurance and filtering approaches for post-training data. We pre-train Llama 3 on a corpus of about 15T multilingual tokens, compared to 1.8T tokens for Llama 2. 

- **Scale.** We train a model at far larger scale than previous Llama models: our flagship language model was pre-trained using 3 _._ 8 _×_ 10<sup>25</sup> FLOPs, almost 50 _×_ more than the largest version of Llama 2. Specifically, we pre-trained a flagship model with 405B trainable parameters on 15.6T text tokens. As expected per 

1

---

[referencia=ea6afdae27cfb441 score=0.297]
##### **4.3.1 Code** 

LLMs for code have received significant attention since the release of Copilot and Codex (Chen et al., 2021). Developers are now widely using these models to generate code snippets, debug, automate tasks, and improve code quality. For Llama 3, we target improving and evaluating code generation, documentation, debugging, and review capabilities for the following high priority programming languages: Python, Java, Javascript, C/C++, Typescript, Rust, PHP, HTML/CSS, SQL, bash/shell. Here, we present our work on improving these coding capabilities via training a code expert, generating synthetic data for SFT, improving formatting with system prompt steering, and creating quality filters to remove bad samples from our training data. 

**Expert training.** We train a **code expert** which we use to collect high quality human annotations for code throughout subsequent rounds of post-training. This is accomplished by branching the main pre-training run and continuing pre-training on a 1T token mix of mostly (>85%) code data. Continued pre-training on domainspecific data has been shown to be effective for improving performance in a specific domain (Gururangan et al., 2020). We follow a recipe similar to that of CodeLlama (Rozière et al., 2023). For the last several thousand steps of training we perform long-context finetuning (LCFT) to extend the expert’s context length to 16K tokens on a high quality mix of repo-level code data. Finally, we follow the similar post-training modeling recipes described in Section 4.1 to align this model, except with SFT and DPO data mixes primarily targeting code. This model is also used for rejection sampling (Section 4.2.2) for coding prompts. 

**Synthetic data generation.** During development, we identified key issues in code generation, including difficulty in following instructions, code syntax errors, incorrect code generation, and difficulty in fixing bugs. While intensive human annotation could theoretically resolve these issues, synthetic data generation offers a complementary approach at a lower cost and higher scale, unconstrained by the expertise level of annotators. As such, we use Llama 3 and the code expert to generate a large quantity of synthetic SFT dialogs. 

We describe three high-level approaches for generating synthetic code data. In total, we generate over 2 _._ 7M synthetic examples which were used during SFT. 

19

---

[referencia=ea6afdae27cfb441 score=0.243]
- **Managing complexity.** We make design choices that seek to maximize our ability to scale the model development process. For example, we opt for a standard dense Transformer model architecture (Vaswani et al., 2017) with minor adaptations, rather than for a mixture-of-experts model (Shazeer et al., 2017) to maximize training stability. Similarly, we adopt a relatively simple post-training procedure based on supervised finetuning (SFT), rejection sampling (RS), and direct preference optimization (DPO; Rafailov et al. (2023)) as opposed to more complex reinforcement learning algorithms (Ouyang et al., 2022; Schulman et al., 2017) that tend to be less stable and harder to scale. 

The result of our work is Llama 3: a herd of three multilingual<sup>1</sup> language models with 8B, 70B, and 405B parameters. We evaluate the performance of Llama 3 on a plethora of benchmark datasets that span a wide range of language understanding tasks. In addition, we perform extensive human evaluations that compare Llama 3 with competing models. An overview of the performance of the flagship Llama 3 model on key benchmarks is presented in Table 2. Our experimental evaluation suggests that our flagship model performs on par with leading language models such as GPT-4 (OpenAI, 2023a) across a variety of tasks, and is close to matching the state-of-the-art. Our smaller models are best-in-class, outperforming alternative models with similar numbers of parameters (Bai et al., 2023; Jiang et al., 2023). Llama 3 also delivers a much better balance between helpfulness and harmlessness than its predecessor (Touvron et al., 2023b). We present a detailed analysis of the safety of Llama 3 in Section 5.4. 

We are publicly releasing all three Llama 3 models under an updated version of the Llama 3 Community License; see https://llama.meta.com. This includes pre-trained and post-trained versions of our 405B parameter language model and a new version of our Llama Guard model (Inan et al., 2023) for input and output safety. We hope that the open release of a flagship model will spur a wave of innovation in the research community, and accelerate a responsible path towards the development of artificial general intelligence (AGI).

---

[referencia=ea6afdae27cfb441 score=0.241]
## **10 Conclusion** 

In many ways, the development of high-quality foundation models is still in its infancy. Our experience in developing Llama 3 suggests that substantial further improvements of these models are on the horizon. Throughout the development of the Llama 3 model family, we found that a strong focus on high-quality data, scale, and simplicity consistently yielded the best results. In preliminary experiments, we explored more complex model architectures and training recipes but did not find the benefits of such approaches to outweigh the additional complexity they introduce in model development. 

Developing a flagship foundation model such as Llama 3 involves overcoming a plethora of deep technical problems but also requires clever organizational decisions. For example, to ensure Llama 3 is not accidentally overfitted on commonly used benchmarks, our pre-training data was procured and processed by a separate team that was strongly incentivized to prevent contamination of that pre-training data with external benchmarks. As another example, we ensure that our human evaluations remain trustworthy by allowing only a small set of researchers who do not contribute to model development to perform and access these evaluations. While such organizational decisions are rarely discussed in technical papers, we found them to be pivotal to the successful development of the Llama 3 family of models. 

We shared the details of our development process because we believe this will: **(1)** help the larger research community understand the key factors of foundation model development and **(2)** contribute to a more informed debate about the future of foundation models in the general public. We also shared preliminary experiments with integrating multimodal capabilities into Llama 3. While these models are still under active development and not yet ready for release, we hope sharing our results early will accelerate research in this direction. 

70 

Following the positive outcomes of the detailed safety analyses presented in this paper, we publicly release our Llama 3 language models in order to accelerate the development of AI systems for a plethora of societally relevant use cases and enable the research community to scrutinize our models and identify ways to make these models better and safer. We believe that the public release of foundation models plays a key role in the responsible development of such models, and we hope that the release of Llama 3 encourages the industry to embrace the open, responsible development of AGI. 

71

---

[referencia=ea6afdae27cfb441 score=0.236]
### **7.6 Image Recognition Results** 

We evaluate the performance of the image understanding capabilities of Llama 3 on a range of tasks spanning natural image understanding, text understanding, charts understanding and multimodal reasoning: 

- **MMMU** (Yue et al., 2024a) is a challenging dataset for mulitmodal reasoning where model is expected to understand images and solve college-level problems spanning 30 different disciplines. This includes both multiple-choice and open ended questions. We evaluate our model on the validation set with 900 images, in line with other works. 

- **VQAv2** (Antol et al., 2015) tests the ability of a model to combine image understanding, language understanding and commonsense knowlege to answer generic questions about natural images 

- **AI2 Diagram** (Kembhavi et al., 2016) evaluates models capability to parse scientific diagrams and answer questions about the same. We use the same evaluation protocol as Gemini and x.ai, and report scores using a transparent bounding box. 

- **ChartQA** (Masry et al., 2022) is a challenging benchmark for charts understanding. This requires model to visually understand different kinds of charts and answer logical questions about the charts. 

- **TextVQA** (Singh et al., 2019) is a popular benchmark dataset that requires models to read and reason about text in images to answer questions about them. This tests the OCR understanding ability of the model on natural images. 

- **DocVQA** (Mathew et al., 2020) is a benchmark dataset focused on document analysis and recognition. It contains images of a wide range of documents which evaluates a model’s ability to perform OCR understanding and reason about the contents of a document to answer questions about them. 

Table 29 presents the results of our experiments. The results in the table show that our vision module attached to Llama 3 performs competitively across a wide range of image-recognition benchmarks at varying model capacities. Using the resulting Llama 3-V 405B model, we outperform GPT-4V on all benchmarks, while being slightly behind Gemini 1.5 Pro and Claude 3.5 Sonnet. Llama 3 405B appears particularly competitive on document understanding tasks.

---

[referencia=ea6afdae27cfb441 score=0.197]
**Open source.** Open weights foundation models have rapidly improved over the last year, with Llama3-405B now competitive with the current closed weight state-of-the-art. Numerous model families have recently been developed, including Mistral (Jiang et al., 2023), Falcon (Almazrouei et al., 2023), MPT (Databricks, 2024), Pythia (Biderman et al., 2023), Arctic (Snowflake, 2024), OpenELM (Mehta et al., 2024), OLMo (Groeneveld et al., 2024), StableLM (Bellagente et al., 2024), OpenLLaMA (Geng and Liu, 2023), Qwen (Bai et al., 2023), Gemma (Team et al., 2024), Grok (XAI, 2024), and Phi (Abdin et al., 2024). 

**Post-training.** Post-training Llama 3 follows the established strategy of instruction tuning (Chung et al., 2022; Ouyang et al., 2022) followed by alignment with human feedback (Kaufmann et al., 2023). While some studies have shown the surprising effectiveness of lightweight alignment procedures (Zhou et al., 2024), Llama 3 uses millions of human instructions and preference judgments to improve the pre-trained model, including 

69 

techniques such as rejection sampling (Bai et al., 2022), supervised finetuning (Sanh et al., 2022), and Direct Preference Optimization (Rafailov et al., 2023). In order to curate these instruction and preference examples, we deploy earlier versions of Llama 3 to filter (Liu et al., 2024c), re-write (Pan et al., 2024), or generate prompts and responses (Liu et al., 2024b) and apply these techniques through multiple rounds of post-training.

---

[referencia=ea6afdae27cfb441 score=0.173]
**Figure 21 Violation and false refusal rates across models and capabilities.** Each point represents the overall false refusal and violation rate for an internal capability benchmark across all safety categories. Symbols indicate whether we are evaluating model or system level safety. As expected model level safety results indicate higher violation rates and lower refusal rates compared to system level safety results. Llama 3 aims to balance a low violation rate with a low false refusal rate, while some competitors are more skewed towards one or the other. 

while keeping false refusal rate low as well, indicating a solid balance between helpfulness and safety. 

**Multilingual safety.** Our experiments demonstrate that safety knowledge in English does not readily transfer to other languages, particularly given the nuance of safety policies and language-specific context. Therefore, it is essential to collect high-quality safety data for each language. We also found that the distribution of safety data per language significantly impacts performance from a safety standpoint, with some languages benefiting from transfer learning while others require more language-specific data. To achieve a balance between FRR and VR, we iteratively add adversarial and borderline data while monitoring the impact on both metrics. 

We display results on our internal benchmarks in Figure 19 for short context models, showing Llama 3’s violation and false refusal rates for English and non-English languages compared to similar models and systems. To construct the benchmarks for each language, we use a combination of prompts written by native speakers, sometimes supplementing with translations from our English benchmarks. For each of our supported languages, we find that Llama 405B with Llama Guard is at least as safe, if not strictly safer, than the two competing systems when measured on our internal benchmark, while maintaining competitive false refusal rates. Looking at the Llama 405B model on its own, without Llama Guard, we find that it has a significantly lower violation rate than the competing standalone open source model, trading off a higher false refusal rate. 

**Long-context safety.** Long-context models are vulnerable to many-shot jailbreaking attacks without targeted mitigation (Anil et al., 2024). To address this, we finetune our models on SFT datasets that include examples of safe behavior in the presence of demonstrations of unsafe behavior in context. We develop a scalable mitigation strategy that significantly reduces VR, effectively neutralizing the impact of longer context attacks even for 256-shot attacks. This approach shows little to no impact on FRR and most helpfulness metrics.

---

[referencia=ea6afdae27cfb441 score=0.173]
### **3.2 Model Architecture** 

Llama 3 uses a standard, dense Transformer architecture (Vaswani et al., 2017). It does not deviate significantly from Llama and Llama 2 (Touvron et al., 2023a,b) in terms of model architecture; our performance gains are primarily driven by improvements in data quality and diversity as well as by increased training scale. 

We make a few small modifications compared to Llama 2: 

- We use grouped query attention (GQA; Ainslie et al. (2023)) with 8 key-value heads to improve inference speed and to reduce the size of key-value caches during decoding. 

- We use an attention mask that prevents self-attention between different documents within the same sequence. We find that this change had limited impact during in standard pre-training, but find it to be important in continued pre-training on very long sequences. 

6 

||**8B**|**70B**|**405B**|
|---|---|---|---|
|Layers|32|80|126|
|Model Dimension|4,096|8192|16,384|
|FFN Dimension|14,336|28,672|53,248|
|Attention Heads|32|64|128|
|Key/Value Heads|8|8|8|
|Peak Learning Rate|3_×_10<sup>_−_4</sup>|1_._5_×_10<sup>_−_4</sup>|8_×_10<sup>_−_5</sup>|
|Activation Function||SwiGLU||
|Vocabulary Size||128,000||
|Positional Embeddings|RoP|E (_θ_ = 500_,_|000)|



**Table 3 Overview of the key hyperparameters of Llama 3.** We display settings for 8B, 70B, and 405B language models.

---

[referencia=ea6afdae27cfb441 score=0.170]
##### **5.2.4 Multilingual Benchmarks** 

Llama 3 supports 8 languages — English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai, although the underlying foundation model has been trained on a broader collection of languages.<sup>9</sup> In Table 20, we show results from evaluating Llama 3 on the multilingual MMLU (Hendrycks et al., 2021a) and Multilingual Grade School Math (MGSM) (Shi et al., 2022) benchmarks. 

**Multilingual MMLU.** We translate MMLU questions, few-shot examples, and answers using Google Translate. We leave the task instructions in English and perform the evaluation in a 5-shot setting. In Table 20, we report average results across German, French, Italian, Portuguese, Hindi, Spanish, and Thai. 

> 9Llama 3 has not been optimized or safety tuned for use cases in those other languages. Developers may fine-tune Llama 3 models for languages beyond the 8 supported languages provided they comply with the Llama 3 Community License and the Acceptable Use Policy and in such cases are responsible for ensuring that any uses of Llama 3 in additional languages is done in a safe and responsible manner. 

37 

**MGSM** (Shi et al., 2022). We use the same native prompts as in simple-evals (OpenAI, 2024) for testing our models in a 0-shot CoT setting. In Table 20, we report averge results across languages covered in MGSM benchmark. 

We find that Llama 3 405B outperforms most other models on MGSM, achieving an average of 91.6%. On MMLU, in line with English MMLU results shown above, Llama 3 405B falls behind GPT-4o by 2%. On the other hand, both Llama 3 70B and 8B models demonstrate strong performance, leading among competitors with a wide margin on both tasks.

---

[referencia=ea6afdae27cfb441 score=0.154]
##### **4.3.4 Long Context** 

During the final pre-training stage, we extend the context length of Llama 3 from 8K tokens to 128K tokens (see Section 3.4 for more details). Similar to pre-training, we find that during finetuning we must carefully tune the recipe to balance short and long-context capabilities. 

**SFT and synthetic data generation.** Naively applying our existing SFT recipe with only short-context data resulted in significant regressions in long-context capabilities from pre-training, highlighting the need to incorporate long-context data in our SFT data mix. In practice, however, it is largely impractical to get humans to annotate such examples due to the tedious and time-consuming nature of reading lengthy contexts, so we predominantly rely on synthetic data to fill this gap. We use earlier versions of Llama 3 to generate synthetic data based on the key long-context use-cases: (possibly multi-turn) question-answering, summarization for long documents, and reasoning over code repositories, and describe them in greater detail below. 

- **Question answering:** We carefully curate a set of long documents from our pre-training mix. We split these documents into chunks of 8K tokens, and prompted an earlier version of the Llama 3 model to generate QA pairs conditional on randomly selected chunks. During training, the whole document is used as context. 

- **Summarization:** We applied hierarchical summarization of long-context documents by first summarizing the chunks of 8K input length using our strongest Llama 3 8K context model and then summarizing the summaries. During training we provide the full document and prompt the model to summarize the document while preserving all the important details. We also generate QA pairs based on the summaries of the documents and prompt the model with questions that require global understanding of the whole long document. 

- **Long context code reasoning:** We parse Python files to identify import statements and determine their dependencies. From here, we select the most commonly depended-upon files, specifically those referenced by at least five other files. We remove one of these key files from a repository and prompt the model to identify which files depended on the missing file and to generate the necessary missing code. 

We further categorize these synthetically generated samples based on the sequence length (16K, 32K, 64K and 128K) to enable more fine-grained targeting of input lengths.

---

[referencia=ea6afdae27cfb441 score=0.153]
# **The Llama 3 Herd of Models** 

**Llama Team, AI @ Meta**<sup>1</sup> 

> 1A detailed contributor list can be found in the appendix of this paper. 

Modern artificial intelligence (AI) systems are powered by foundation models. This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. Our largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens. This paper presents an extensive empirical evaluation of Llama 3. We find that Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. We publicly release Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and our Llama Guard 3 model for input and output safety. The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach. We observe this approach performs competitively with the state-of-the-art on image, video, and speech recognition tasks. The resulting models are not yet being broadly released as they are still under development. 

**Date:** July 23, 2024 

**Website:** https://llama.meta.com/

---

[referencia=ea6afdae27cfb441 score=0.141]
## **2 General Overview** 

The model architecture of Llama 3 is illustrated in Figure 1. The development of our Llama 3 language models comprises two main stages: 

- **Language model pre-training.** We start by converting a large, multilingual text corpus to discrete tokens and pre-training a large language model (LLM) on the resulting data to perform next-token prediction. In the language model pre-training stage, the model learns the structure of language and obtains large amounts of knowledge about the world from the text it is “reading”. To do this effectively, pre-training is performed at massive scale: we pre-train a model with 405B parameters on 15.6T tokens using a context window of 8K tokens. This standard pre-training stage is followed by a continued pre-training stage that increases the supported context window to 128K tokens. See Section 3 for details. 

- **Language model post-training.** The pre-trained language model has a rich understanding of language but it does not yet follow instructions or behave in the way we would expect an assistant to. We align the model with human feedback in several rounds, each of which involves supervised finetuning (SFT) on instruction tuning data and Direct Preference Optimization (DPO; Rafailov et al., 2024). At this post-training<sup>2</sup> stage, we also integrate new capabilities, such as tool-use, and observe strong improvements in other areas, such as coding and reasoning. See Section 4 for details. Finally, safety mitigations are also incorporated into the model at the post-training stage, the details of which are described in Section 5.4. 

The resulting models have a rich set of capabilities. They can answer questions in at least eight languages, write high-quality code, solve complex reasoning problems, and use tools out-of-the-box or in a zero-shot way. 

We also perform experiments in which we add image, video, and speech capabilities to Llama 3 using a compositional approach. The approach we study comprises the three additional stages illustrated in Figure 28: 

- **Multi-modal encoder pre-training.** We train separate encoders for images and speech. We train our image encoder on large amounts of image-text pairs. This teaches the model the relation between visual content and the description of that content in natural language. Our speech encoder is trained using a

---

[referencia=ea6afdae27cfb441 score=0.138]
##### **4.3.6 Factuality** 

Hallucinations remain a major challenge for large language models. Models tend to be overconfident, even in domains where they have little knowledge. Despite these shortcomings, they are often used as knowledge bases, which can lead to risky outcomes such as the spread of misinformation. While we recognize that factuality can go beyond hallucinations, we took a hallucination-first approach here. 

26 



**Figure 11 Processing file uploads.** Example of Llama 3 performing analysis and visualization of an uploaded file. 

We follow the principle that post-training should align the model to “know what it knows” rather than add knowledge (Gekhman et al., 2024; Mielke et al., 2020). Our primary approach involves generating data that aligns model generations with subsets of factual data present in the pre-training data. To achieve this, we develop a knowledge probing technique that takes advantage of Llama 3’s in-context abilities. This data generation process involves the following procedure: 

1. **Extract a data snippet** from the pre-training data. 

2. **Generate a factual question** about these snippets (context) by prompting Llama 3. 

3. **Sample responses** from Llama 3 to the question. 

4. **Score the correctness** of the generations using the original context as a reference and Llama 3 as a judge. 

5. **Score the informativeness** of the generations using Llama 3 as a judge. 

6. **Generate a refusal** for responses which are consistently informative and incorrect across the generations, using Llama 3. 

We use data generated from the knowledge probe to encourage the model to only answer questions which it has knowledge about, and refuse answering those questions that it is unsure about. Further, pre-training data is not always factually consistent or correct. We therefore also collect a limited set of labeled factuality data that deals with sensitive topics where factually contradictory or incorrect statements are prevalent. 

27 

**4.3.7 Steerability** Steerability is the ability to direct the model’s actions and outcomes to meet developer and user specifications. As Llama 3 is a generic foundational model, it should be maximally steerable to different downstream use cases easily. For Llama 3, we focus on enhancing its steerability through system prompt with natural language instructions, especially around response length, format, tone and character/persona.

---

[referencia=ea6afdae27cfb441 score=0.134]
##### **4.3.5 Tool Use** 

Teaching LLMs to use tools such as search engines or code interpreters hugely expands the range of tasks they can solve, transforming them from pure chat models into more general assistants (Nakano et al., 2021; Thoppilan et al., 2022; Parisi et al., 2022; Gao et al., 2023; Mialon et al., 2023a; Schick et al., 2024). We train Llama 3 to interact with the following tools: 

- **Search engine.** Llama 3 is trained to use Brave Search<sup>7</sup> to answer questions about recent events that go beyond its knowledge cutoff or that require retrieving a particular piece of information from the web. 

- **Python interpreter.** Llama 3 can generate and execute code to perform complex computations, read files uploaded by the user and solve tasks based on them such as question answering, summarization, data analysis or visualization. 

> 7https://brave.com/search/api/ 

24 

- **Mathematical computational engine.** Llama 3 can use the Wolfram Alpha API<sup>8</sup> to more accurately solve math, science problems, or retrieve accurate information from Wolfram’s database. 

The resulting model is able to use these tools in a chat setup to solve the user’s queries, including in multi-turn dialogs. If a query requires multiple tool calls, the model can write a step-by-step plan, call the tools in sequence, and do reasoning after each tool call. 

We also improve Llama 3’s zero-shot tool use capabilities — given in-context, potentially unseen tool definitions and a user query, we train the model to generate the correct tool call. 

**Implementation.** We implement our core tools as Python objects with different methods. Zero-shot tools can be implemented as Python functions with descriptions, documentation ( _i.e._ , examples for how to use them), and the model only needs the function’s signature and docstring as context to generate the appropriate call. We also convert function definitions and calls to JSON format, e.g., for web API calls. All tool calls are executed by the Python interpreter, that must be enabled in the Llama 3 system prompt. Core tools can be individually enabled or disabled in the system prompt.

---

[referencia=ea6afdae27cfb441 score=0.134]
### **9.1 Language** 

**Scale.** Llama 3 follows the enduring trend of applying straightforward methods at ever increasing scales in foundation models. Improvements are driven by increased compute and improved data, with the 405B model using almost fifty times the pre-training compute budget of Llama 2 70B. Despite containing 405B parameters, our largest Llama 3 in fact contains fewer parameters than earlier and much less performant models such as PALM (Chowdhery et al., 2023), due to better understanding of scaling laws (Kaplan et al., 2020; Hoffmann et al., 2022). Little is publicly known about the size of other frontier models, such as Claude 3 or GPT 4 (OpenAI, 2023a), but overall performance is compareable. 

**Small models.** Developments in smaller models have paralleled those in large models. Models with fewer parameters can dramatically improve inference cost and simplify deployment (Mehta et al., 2024; Team et al., 2024). The smaller Llama 3 models achieve this by training far beyond the point of compute optimal training, effectively trading training compute for inference efficiency. An alternative path is to distill larger models into smaller ones, as in Phi (Abdin et al., 2024). 

**Architectures.** While Llama 3 makes minimal architectural modifiations to compared to Llama 2, other recent foundation models have explored other designs. Most notably, mixture of experts architectures (Shazeer et al., 2017; Lewis et al., 2021; Fedus et al., 2022; Zhou et al., 2022) can be used as an efficient way to increase the capacity of a models, such as in Mixtral (Jiang et al., 2024) and Arctic (Snowflake, 2024). Llama 3 outperforms these models, suggesting that dense architectures are not the limiting factor, but there remain numerous trade offs in terms of training and inference efficiency, and model stability at scale.

---

[referencia=ea6afdae27cfb441 score=0.130]
<!-- Start of picture text -->
ZeroSCROLLS (Shaham et al., 2023), Needle-in-a-Haystack (Kamradt, 2023),<br>Long context<br>InfiniteBench (Zhang et al., 2024)<br>Table 16 Post-training benchmarks by category. Overview of all benchmarks we use to evaluate post-trained Llama 3<br>models, ordered by capability.<br>5.2.1 General Knowledge and Instruction-Following Benchmarks<br>We evaluate Llama 3 on benchmarks for general knowledge and instruction-following in Table 2.<br>General knowledge. We leverage MMLU (Hendrycks et al., 2021a) and MMLU-Pro (Wang et al., 2024b) to<br>evaluate Llama 3’s capability on knowledge-based question answering. For MMLU, we report the macro<br>average of subtask accuracy under the 5-shot standard setting without CoT. MMLU-Pro is an extension<br>of MMLU, incorporating more challenging, reasoning-focused questions, eliminating noisy questions, and<br>expanding the choice set from four to ten options. Given its focus on complex reasoning, we report 5-shot<br>CoT for MMLU-Pro. All tasks are formatted as generation tasks, similar to simple-evals (OpenAI, 2024).<br>As shown in Table 2, our 8B and 70B Llama 3 variants outperform other models of similar sizes on both<br>general knowledge tasks. Our 405B model outperforms GPT-4 and Nemotron 4 340B, with Claude 3.5 Sonnet<br>leading among larger models.<br>Instruction following. We assess the ability of Llama 3 and other models to follow natural language instructions<br>on IFEval (Zhou et al., 2023). IFEval comprises approximately 500 “verifiable instructions” such as “write<br><!-- End of picture text -->

in more than 400 words”, which can be verified by heuristics. We report the average of prompt-level and 

instruction-level accuracy, under strict and loose constraints in Table 2. Note that all Llama 3 variants outperform comparable models across IFEval.

---

[referencia=ea6afdae27cfb441 score=0.127]
##### **4.1.5 Model Averaging** 

Finally, we average models obtained from experiments using various versions of data or hyperparameters at each RM, SFT, or DPO stage (Izmailov et al., 2019; Wortsman et al., 2022; Li et al., 2022). 

16 

|**% of**<br>**Dataset**<br>**comparisons**|**Avg. # turns**<br>**per dialog**|**Avg. # tokens**<br>**per example**|**Avg. # tokens**<br>**in prompt**|**Avg. # tokens**<br>**in response**|
|---|---|---|---|---|
|General English<br>81.99%|4.1|1,000.4|36.4|271.2|
|Coding<br>6.93%|3.2|1,621.0|113.8|462.9|
|Multilingual<br>5.19%|1.8|1,299.4|77.1|420.9|
|Reasoning and tools<br>5.89%|1.6|707.7|46.6|129.9|
|Total<br>100%|3.8|1,041.6|44.5|284.0|



**Table 6 Statistics of human preference data.** We list statistics of the internally collected human preference data used for Llama 3 alignment. We ask annotators to perform multi-turn dialogues with the models and make comparisons among responses at each turn. In post-processing, we split each dialogue to multiple examples at a turn level. Each example consists of a prompt (including previous dialog if available) and a response (e.g., chosen or rejected response). 

##### **4.1.6 Iterative Rounds** 

Following Llama 2, we apply the above methods in six rounds. In each cycle, we collect new preference annotations and SFT data, sampling synthetic data from the latest models.

---

[referencia=ea6afdae27cfb441 score=0.117]
**Table 31 Word error rate of our speech interface for Llama 3 on speech recognition tasks.** We report the performance of Whisper, SeamlessM4T, and Gemini for reference. 

||**Llama 3 8B**|**Llama 3 70B**|**Whisper v2**|**SeamlessM4T v2**|
|---|---|---|---|---|
|FLEURS (33 lang. _→_English)|29.5|**33.7**|21.9|28.6|
|Covost 2 (15 lang. _→_English)|34.4|**38.8**|33.8|37.9|



**Table 32 BLEU score of our speech interface for Llama 3 on speech translation tasks.** We report the performance of Whisper and SeamlessM4T for reference. 

on the standard test set of those benchmarks, except for Chinese, Japanese, Korean and Thai, where the character error rate is reported. 

Table 31 shows the results of ASR evaluations. It demonstrates the strong performance of Llama 3 (and multi-modal foundation models more generally) on speech recognition tasks: our model outperforms models that are tailored to speech like Whisper<sup>20</sup> and SeamlessM4T on all benchmarks. On MLS English, Llama 3 performs similarly to Gemini. 

**Speech translation.** We also evaluate our models on speech translation tasks in which the model is asked to translate non-English speech into English text. We use the FLEURS and Covost 2 (Wang et al., 2021b) datasets in these evaluations, measuring BLEU scores of the translated English. Table 32 presents the results of these experiments.<sup>21</sup> The performance of our models in speech translation highlights the advantages of multimodal foundation models for tasks such as speech translation. 

**Spoken question answering.** The speech interface of Llama 3 demonstrates remarkable question answering capabilities. The model can effortlessly comprehend code-switched speech without any prior exposure to such data. Notably, although the model was trained only on single-turn dialogue, it is capable of engaging in extended, coherent multi-turn dialogue sessions. Figure 30 presents a few examples that highlight these multilingual and multi-turn capabilities.

---

[referencia=ea6afdae27cfb441 score=0.117]
1 

||**Finetuned**|**Multilingual**|**Long context**|**Tool use**|**Release**|
|---|---|---|---|---|---|
|Llama 3 8B|✗|✗<sup>1</sup>|✗|✗|April 2024|
|Llama 3 8B Instruct|✓|✗|✗|✗|April 2024|
|Llama 3 70B|✗|✗<sup>1</sup>|✗|✗|April 2024|
|Llama 3 70B Instruct|✓|✗|✗|✗|April 2024|
|Llama 3.1 8B|✗|✓|✓|✗|July 2024|
|Llama 3.1 8B Instruct|✓|✓|✓|✓|July 2024|
|Llama 3.1 70B|✗|✓|✓|✗|July 2024|
|Llama 3.1 70B Instruct|✓|✓|✓|✓|July 2024|
|Llama 3.1 405B|✗|✓|✓|✗|July 2024|
|Llama 3.1 405B Instruct|✓|✓|✓|✓|July 2024|



**Table 1 Overview of the Llama 3 Herd of models.** All results in this paper are for the Llama 3.1 models. 

scaling laws for foundation models, our flagship model outperforms smaller models trained using the same procedure. While our scaling laws suggest our flagship model is an approximately compute-optimal size for our training budget, we also train our smaller models for much longer than is compute-optimal. The resulting models perform better than compute-optimal models at the same inference budget. We use the flagship model to further improve the quality of those smaller models during post-training.

---

[referencia=ea6afdae27cfb441 score=0.117]
### **8.4 Speech Understanding Results** 

We evaluate the speech understanding capabilities of our speech interface for Llama 3 on three tasks: **(1)** automatic speech recognition, **(2)** speech translation, and **(3)** spoken question answering. We compare the performance of our speech interface for Llama 3 with three state-of-the-art models for speech understanding: Whisper (Radford et al., 2023), SeamlessM4T (Barrault et al., 2023), and Gemini.<sup>19</sup> In all the evaluations, we used greedy search for Llama 3 token prediction. 

**Speech recognition.** We evaluate the ASR performance on the English datasets of Multilingual LibriSpeech (MLS; Pratap et al. (2020)), LibriSpeech (Panayotov et al., 2015), VoxPopuli (Wang et al., 2021a), and a subset of the multilingual FLEURS dataset (Conneau et al., 2023). In evaluation, the decoding results are post-processed using the Whisper text normalizer to ensure consistency in comparing with the reported results of other models. On all benchmarks, we measure the word error rate of our speech interface for Llama 3 

> 19Due to technical limitations, we compare with the performance of Gemini on MLS reported in the original paper. 

66 

||**Llama 3 8B**|**Llama 3 70B**|**Whisper**|**SeamlessM4T v2**|**Gemini 1.0 Ultra**|**Gemini 1.5 Pro**|
|---|---|---|---|---|---|---|
|MLS (English)|4.9|4.4|6.2 (v2)|6.5|4.4|**4.2**|
|LibriSpeech (test-other)|3.4|**3.1**|4.9 (v2)|6.2|–|–|
|VoxPopuli (English)|6.2|**5.7**|7.0 (v2)|7.0|–|–|
|FLEURS (34 languages)|9.6|**8.2**|14.4 (v3)|11.7|–|–|