[referencia=2c2ef6e29ff22be3 score=0.958]
37th Conference on Neural Information Processing Systems (NeurIPS 2023). 

we should pay attention to ensuring comparable performance and accessibility across the supported languages, regardless of whether by design or by chance. 

This work demonstrates how the unequal treatment of languages arises at the tokenization stage,<sup>1</sup> well before the language model sees any data at all. For instance, the tokenizer employed by ChatGPT (OpenAI, 2022) and GPT-4 (OpenAI, 2023) uses about 1.6 times more tokens to encode the same text in Italian as it does in English, 2.6 times for Bulgarian and 3 times for Arabic. For Shan —the native language of people from the Shan State in Myanmar— that difference can be as high as 15 times. Unicode character and byte-level tokenization also result in drastically different encoding lengths across languages: byte-level representation of the same text is over 4 times longer for Burmese or Tibetan than Chinese. 

We discuss three fairness implications of these differences in tokenization: 

1. **Cost:** Commercial services charge users per token or Unicode character. In either case, these discrepancies lead to users of some languages paying at least 2.5 times more for the same task as users of English. 

2. **Latency:** The number of tokens has a direct effect on the processing time for a task. Some languages can require twice the time to process the same content as English. This may be critical for real-time applications like emergency services. 

3. **Long context processing:** Many models have a fixed-size context. Users of languages that are more token-efficient can use these systems to process or generate texts that may be more than an order of magnitude longer than users of other languages. This may lead to significant discrepancies in the quality of service. 

Therefore, we make the case for _multilingual tokenization parity_ : tokenizers should produce similar encoded lengths for the same content across languages. Hence, we advocate for multilingually fair tokenizers for the next generation of language models.

---

[referencia=2c2ef6e29ff22be3 score=0.951]
# **Language Model Tokenizers Introduce Unfairness Between Languages** 

### **Aleksandar Petrov, Emanuele La Malfa, Philip H.S. Torr, Adel Bibi** University of Oxford 

```
aleks@robots.ox.ac.uk
```

## **Abstract** 

Recent language models have shown impressive multilingual performance, even when not explicitly trained for it. Despite this, there are concerns about the quality of their outputs across different languages. In this paper, we show how disparity in the treatment of different languages arises at the tokenization stage, well before a model is even invoked. The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases. These disparities persist even for tokenizers that are intentionally trained for multilingual support. Character-level and byte-level models also exhibit over 4 times the difference in the encoding length for some language pairs. This induces unfair treatment for some language communities in regard to the cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context to the models. Therefore, we make the case that we should train future language models using multilingually fair subword tokenizers.

---

[referencia=2c2ef6e29ff22be3 score=0.927]
**Measuring tokenization lengths.** Zhang et al. (2022) suggested using the ratio of the average sentence length in tokens to the length in characters as a measure of closeness to the character level. However, this method may not be suitable for comparing languages due to differences in sentence length across languages. On the other hand, Ács (2019) and Scao et al. (2022) measure the number of tokens created per word, but this method may not be effective for comparing languages due to differences in semantic content per word and the lack of word delineation in some languages. Rust et al. (2021) show that mBERT (Devlin et al., 2019) breaks down English words the least, in line with our findings of English receiving special treatment. However, to the best of our knowledge, we are the first to leverage a parallel corpus to compare tokenization lengths across languages. 

## **8 Conclusion** 

This paper highlights the significant disparities in tokenization across different languages which can lead to unequal treatment and disadvantages for certain language communities. The findings reveal that even tokenizers explicitly trained for multilingual support exhibit tokenization lengths that vary by up to a factor of 13. Furthermore, character-level and byte-level models also demonstrate encoding length discrepancies that are more than 4 times longer. These disparities have important real-world implications including increased costs for accessing commercial language services, longer processing times and limitations on the amount of contextual information provided to language models. To address these issues, we propose the development of multilingually fair tokenizers for future language models emphasizing the importance of ensuring comparable performance and accessibility across supported languages. By achieving tokenization parity, we can mitigate inequalities and promote fair access to language technologies across diverse linguistic communities. 

10

---

[referencia=2c2ef6e29ff22be3 score=0.910]
Tokenization disparity is also present in the ByT5 model. The tokenization premium for ByT5 ranges from 0.87 (for Yue Chinese) to 3.94 (for Shan). The introduction of the variablewidth UTF-8 encoding of Unicode characters in ByT5 creates another issue of unequal treatment. ASCII characters, which are sufficient for English, require only one byte. Other Latin script characters, as well as Greek, Cyrillic, Coptic, Armenian, Hebrew, Arabic and Syriac, require two bytes, while Chinese, Japanese and Korean characters require three bytes. Therefore, the tokenization of Chinese and Japanese is about three times as long for ByT5 as it is for CANINE (Table 5). Shan’s premium of 3.94 is due to the fact that all its consonants and diacritics require three bytes. For example, the word “မႂ်း” is encoded by ByT5 as 12 tokens, whereas the corresponding “you” requires 3 tokens. The situation is similar for other languages like Dzongkha, Tibetan and Burmese. 

**Summary.** Byte-level models also fail to achieve parity among the languages from FLORES-200 exhibiting a premium of over 4 times for some language pairs. There are two sources of multilingual tokenizer disparities. First, there are natural differences in the number of characters used in different languages to communicate the same content. Second, the UTF-8 standard uses different number of bytes to encode codepoints of different scripts.

---

[referencia=2c2ef6e29ff22be3 score=0.796]
Unequal treatment of dialects or linguistic varieties can lead to social and economic disadvantages making it important to also study the tokenization differences between the “standard” language and its varieties. For Swiss German and the Mauritian and Haitian Creoles, there are large differences in tokenization lengths compared respectively to High German (on GottBERT) and French (on CamemBERT). English is much closer to parity for both models than these language varieties. Therefore subword tokenizers might not be able to generalize to language varieties, such as dialects and creoles. The tokenizers of ArabicBERT and BERT Japanese, however, are close to parity across various dialects of both languages and have lower premiums for the dialects than for English. This is likely due to the good representation of the dialects in the dataset as well as the dialects being linguistically closer to the respective standard languages. The detailed analysis is deferred to Appendix B. 

**Summary.** We observed that the tokenizers targeting French, German and Vietnamese have English as the language closest to parity, rather than more linguistically close languages. On the other hand, tokenizers for Arabic, Chinese and Japanese have lower premiums for languages they share a script with. Notably, despite targeting Indian languages, MuRIL still has the shortest tokenizations for English. Finally, across all tokenizers, the premium for English is lower than the premium for the same language for the English-centric RoBERTa. Hence, we conclude that tokenizers for other languages give English preferential treatment. 

5 



<!-- Start of picture text -->

---

[referencia=2c2ef6e29ff22be3 score=0.772]
|Shan<br>|4.43<br>|1.94 <br>|3.28<br>|4.63<br>|12.06<br>|Standard Arabic|0.88|1.60|
|Std. Arabic<br>|1.18|1.40 <br>|1.35<br>|1.29|1.14<br>|Standard Tibetan|1.13|3.31|
|Std. Tibetan<br>|—|1.44|3.68|—|6.66|TokPisin|1.28|1.28|
|Uyghur<br>|1.41|1.40|2.57|3.00|3.67|<br>Tumbuka|130|132|
|Yue Chinese|0.93|1.05|0.95|1.03|0.93|Yue Chinese|.<br>0.31|.<br>0.87|



The English premium for GottBERT (1.35) is lower than those for Dutch (1.73) and Luxembourgish (1.75), which are more linguistically similar to German. CamemBERT is similar: English has the lowest premium (1.20), while Catalan (1.59) and Friulian (1.66) have higher premiums. PhoBERT also has English with the lowest tokenizer premium (1.20). Thus, even models targeting other languages exhibit a preference for English tokenization. 

RoCBert and BERT Japanese differ by having the other target language as the one closest to parity, possibly due to the partially shared script. ArabicBERT demonstrates a similar behaviour, with Central Kanuri (1.27) and Acehnese (1.73), both written in Arabic script, and with English at 1.82. Sharing writing systems seems to improve tokenization parity. 

Across all tokenizers, the premium for English relative to the respective target language is significantly lower than the premium of RoBERTa for that target language. This asymmetry between English and all other languages likely stems from the extensive incorporation of English in documents written in other languages (Zhang et al., 2022). 

We also consider MuRIL, a BERT-based model trained on 16 Indian languages and English ’ (Khanuja et al., 2021). Despite the model s focus on Indian languages, it remains most token-efficient for English (see Table 3).

---

[referencia=2c2ef6e29ff22be3 score=0.764]
- **5.3 Long context processing** 

Transformers models have difficulty processing long inputs (Liu et al., 2023). Given that the size of the input is contingent upon the tokenization process, inputs of greater length may impose a challenge for language models to adequately reason over. Such a predicament may result in reduced abilities or limited applicability for languages with high tokenization premiums. For example, RoBERTa has a fixed block size of 512, GPT-2 has 768, 1024, 1280, or 1600 Radford et al. (2019), GPT-4 comes in 8,000 and 16,000 context variants.<sup>8</sup> These models cannot process inputs longer than that. Therefore, one can process less than a tenth of the content in languages like Burmese and Dzongkha than they can in English. 

Alongside inconveniencing the users of these languages, this can also result in diminished performance on automated systems, such as content moderation. Reliable content moderation is crucial for tackling hate speech and diminished performance has already been shown to fail to prevent its spread (Stecklow, 2018; Facebook, 2021). Therefore, reduced long context capabilities for some languages could have severe real-world impacts. 

- **6 Towards Multilingual Tokenization Fairness** 

Section 5 showed that high values of tokenization parity for a language lead to increased cost and latency and decreased capacity for long context processing. In this section, we argue that training language models from scratch with a multilingually fair subword tokenizer is the only approach that can effectively address all these aspects of tokenization unfairness. 

**Subword tokenization is necessary to achieve parity.** In Section 4.4, we showed that neither character-level nor byte-level input representation can achieve tokenization parity. Therefore, a variation of subword tokenization is necessary. For example, Chinese characters could be individual tokens, Latin characters might be represented as tokens with an average length of about 3 characters while pairs of Burmese characters and their diacritics being assigned single tokens. Such an approach would account for Chinese requiring one-third the characters English does (as shown in Table 5). 

**A separate tokenizer for determining the processing cost is not sufficient.** An easy patch for existing models is to use a separate tokenizer for calculating how much a user should be charged. Using one tokenizer for computing the cost and another to process

---

[referencia=2c2ef6e29ff22be3 score=0.721]
|Vietnamese|2.52|2.55|—|4.12|—|1.00|||
|Yue Chinese|—|0.92|—|3.75|—|—|||



due to their larger vocabulary size. However, the cheapest languages, Portuguese, Pangasinan and German, still see a premium of 50% when compared to English. Shan has the worst tokenizer parity for all four models. Take as an example “မႂ်း”, one of the Shan words for “you”. It is tokenized by ChatGPT and GPT-4 as: 

```
258702471572242242587011825870116
```

မ ◌ႂ ◌် ◌း 

This word is constructed from one consonant and three diacritics. As the diacritics are encoded separately, there are four Unicode codepoints for this Shan character, resulting in 9 tokens. The English “you” has three characters but a single token. 

FlanT5 has more than 10% `UNK` tokens for 42% of languages (— in Table 1). It has a higher premium than the other tokenizers for all other languages except German and Romanian. 

**Summary.** All four English-centric tokenizers we consider are far from tokenization parity. Portuguese is closest to parity with English for the ChatGPT and GPT-4 tokenizer but still requires about 50% more tokens for the same content. Shan is furthest from parity for this tokenizer with 15 times longer encodings compared to English. FlanT5 is closer to parity with its premium range 1.37–3.41 but it encodes only 54% of the languages, so we cannot say that it is more multilingually fair than the other tokenizers.

---

[referencia=2c2ef6e29ff22be3 score=0.620]
## **7 Related Works** 

**Fairness and bias in language models.** The rapid increase in the size of language models has raised concerns regarding their biases and unfairness (Bender et al., 2021). For example, Bolukbasi et al. (2016), May et al. (2019) and Nadeem et al. (2021) showed that stereotypes and biases exist in language models, while Magee et al. (2021) identified the presence of intersectional biases which may be resistant to debiasing techniques. Language models were also shown to rely on social biases in question answering (Parrish et al., 2022). Another challenge is the generation of toxic content which can occur even without prompting (Gehman et al., 2020). Interestingly, Gururangan et al. (2022) point out that datasets consider one type of English as a higher quality depending on the location of the writer rather than on factuality or literary acclaim. Moreover, Ramesh et al. (2023) and Levy et al. (2023) highlighted the need to consider fairness issues of languages other than English, as they may have distinct sources of bias and solutions for English may not be applicable. 

**Multilingual performance.** One approach towards similar multilingual performance is to frame languages as entities as recently proposed by Choudhury and Deshpande (2021). Another method is to separately train vocabularies for different language clusters to balance cross-lingual and language-specific tokens (Chung et al., 2020). Still, multilingual models struggle to deliver on the promises of deep transfer learning for lower-resourced languages (Virtanen et al., 2019) and perform differently depending on the script and resource level of the language (Bang et al., 2023). Ahuja et al. (2023) found that generative models perform better on higher-resource languages and languages that use the Latin script, possibly due to the context length restrictions for some languages. Zhang et al. (2022) show that a balanced tokenizer corpus results in better translation performance. Separately, Hofmann et al. (2021, 2022) show that the BPE results in suboptimal token choices even for English and demonstrate that addressing this issue boosts performance. Similarly, Rajab (2022) and Oladipo et al. (2022) discuss how tokenization affects performance for African languages.

---

[referencia=2c2ef6e29ff22be3 score=0.615]
## **5 Fairness Implications of Tokenization Length Differences** 

We showed that no matter whether one uses subword, multilingual, or byte-level tokenization, none of the tokenizers gets close to parity for all languages in FLORES-200. This lack of tokenization parity is not merely a curiosity: it leads to unfairness in the cost to access language models, the latency of the service and the amount of data that can be processed. 

### **5.1 Cost** 

It is increasingly common to access LLMs as paid API services. One pricing approach, employed by OpenAI at the time of writing,<sup>6</sup> is to charge per token. Therefore, the tokenization premiums discussed in Section 4 directly map to cost premiums. For ChatGPT and GPT-4, the cost to process a text in German or Italian is about 50% higher than to process the same text in English (Table 1). Using them in Dzongkha, Odia, Santali or Shan, the most expensive languages for these services, costs more than 12 times more than in English. 

Another pricing strategy is per Unicode character: the approach currently taken by the Google Cloud Natural Language service.<sup>7</sup> However, as we showed in Section 4.4, the same content can have very different lengths when measured in Unicode characters. Burmese, Dzongkha, Shan, Tok Pisin or Tumbuka require more than 4 times more characters than Yue Chinese for the same text, resulting in a proportional cost difference. Therefore, both the per-token and the per-character approaches result in large disparities in the cost for users of different languages to use the exact same service.

---

[referencia=2c2ef6e29ff22be3 score=0.510]
**A separate tokenizer for determining the processing cost is not sufficient.** An easy patch for existing models is to use a separate tokenizer for calculating how much a user should be charged. Using one tokenizer for computing the cost and another to process 

> 8 `https://openai.com/pricing` 

8 

Figure 3: How much longer will English language tokenization be if we dedicate a fraction of the `cl100k_base` vocabulary to other languages? This plot shows how many tokens will be necessary to encode the English language corpus of FLORES-200 for different subsets of the `cl100k_base` vocabulary. 



<!-- Start of picture text -->
80000<br>78000<br>76000<br>74000<br>72000 A 10-fold reduction in the vocabulary<br>70000 30% longer sequences for English. would result in only<br>68000<br>66000<br>64000 With one-third of the vocabulary,<br>62000 just 10% longer for ChatGPT/GPT-4English sequences will become<br>60000<br>58000<br>56000<br>54000<br>52000<br>0 10000 20000 30000 40000 50000 60000 70000 80000 90000100000<br>Vocabulary size<br>Tokens necessary to encode FLORES-200<br><!-- End of picture text -->

the input can easily be applied to existing systems without the need to retrain the LLM itself. However, as the tokenizer for the language model is unchanged, this approach would still suffer from latency and inability to process long contexts. Therefore, to ensure similar processing times and long context capabilities across languages, the language model has to be trained with a multilingually fair tokenizer. 

**The tokenization needs to support all Unicode codepoints.** Amongst all tokenizers we examine in this paper, the ones which encode all FLORES-200 languages all have one thing in common: they build their tokenization on top of Unicode representation, allowing them them to represent all characters. Therefore, a multilingually fair tokenizer should also start from a Unicode (or equivalent) encoding. Considering that subword tokenization is necessary, building the vocabulary from UTF-8 would likely result in a smaller dictionary than building it on top of UTF-32. Hence, UTF-8 is likely the more appropriate choice.

---

[referencia=2c2ef6e29ff22be3 score=0.414]
Table 1: Premiums with respect to English on FLORES-200 for several **Englishcentric** models. The languages in the top or bottom three for any tokenizer, as well as the ones discussed in the text, are shown. 

||GPT-2<br>RoBERTa|ChatGPT<br>GPT-4|FlanT5|
|---|---|---|---|
|Bulgarian|5.51|2.64|—|
|Burmese<br>|16.89|11.70|—|
|Chinese (Simplifed)|3.21|1.91|—|
|Dzongkha|16.36|12.33|—|
|English|1.00|1.00|1.00|
|French|2.00|1.60|1.60|
|German|2.14|1.58|1.37|
|Italian|2.01|1.64|2.18|
|Japanese|3.00|2.30|—|
|Jingpho|2.65|2.35|3.41|
|Maori|2.45|2.35|3.28|
|Norwegian Bokmål|1.86|1.56|2.24|
|Odia|13.38|12.48|—|
|Pangasinan|1.66|1.57|2.18|
|Portuguese|1.94|1.48|2.21|
|Romanian|2.48|1.88|1.50|
|Santali|12.86|12.80|—|
|Shan|18.76|15.05|—|
|Spanish|1.99|1.55|2.23|
|Standard Arabic|4.40|3.04|—|
|Tumbuka|2.78|2.57|3.29|
|Vietnamese|4.54|2.45|—|



2The concurrent work by Ahia et al. (2023) also evaluates the tokenization premiums for different languages and reaches similar conclusions. 

> 3An interactive table of all the languages and tokenizers is also available on the project website. 

> 4The largest tokenizer parity difference between them is less than 0.005. 

3

---

[referencia=2c2ef6e29ff22be3 score=0.372]
### **4.3 Parity for Multilingual Models** 

There has been a growing interest in multilingual language models, particularly for translation (Dabre et al., 2020). As these models are intended to support a variety of languages, one would expect them to be close to tokenizer parity. We compare several such multilingual models: XML-R (Conneau et al., 2020), NLLB (Costa-jussà et al., 2022), M2M100 (Fan et al., 2021) and mT5 (Xue et al., 2020). All of these models use the SentencePiece tokenizer with upsampling for rare languages. The final model, BLOOM (Scao et al., 2022), uses byte-level BPE instead of SentencePiece and is designed to maintain similar ratios of tokens per word for each language as reference monolingual tokenizers. 

BLOOM and NLLB encode all languages with less than 10% `UNK` tokens, respectively thanks to byte-level BPE tokenization and being trained on the same 200 languages as FLORES200 (see Table 4). The other three models fail to encode at least one language. All five models have languages with premiums of more than 2.5. Still, all models are better than the English-centric models in Table 1. Figure 1 shows how XLM-R is much closer to parity than RoBERTa (on which it is based), over all languages it can encode. However, none of the models uniformly reaches parity across all languages. Therefore even models which are intentionally designed to be multilingual suffer from a lack of tokenization parity. 

**Summary:** Multilingual models can improve the tokenization parity for different languages but challenges remain in achieving tokenization parity across all languages.

---

[referencia=2c2ef6e29ff22be3 score=0.306]
### **5.2 Latency** 

High latency of real-time interactions for users of certain languages can result in a suboptimal experience and communication breakdowns. For customer support or emergency services, delays in response time can lead to miscommunication or delayed assistance. 

> 6 `https://openai.com/pricing` 

> 7 `https://cloud.google.com/natural-language/pricing` 

7 

As some languages have significantly longer tokenized inputs, they would also experience longer processing times. The transformer attention mechanism has a quadratic complexity in the number of input tokens (Keles et al., 2023). However, the full model architecture contains other submodules and therefore the overall complexity might be different. 

To assess the effect of the tokenization length on the latency, in Figure 2 we plot the computation time of RoBERTa against the tokenization lengths. It appears that the processing time is linear in the tokenization length rather than quadratic, showing a strong correlation between sequence length and execution time. Therefore, tokenization disparities across languages also affect the latency and processing time for text in these languages. 

As expected, English is on the left lower corner, having the shortest tokenization and one of the fastest processing times. Shan is on the other extreme with the longest tokenization length and execution time (almost twice that of English). We can also observe clear trends dependent on the script used. Latin script and other Greek-derived scripts show the shortest tokenization lengths and processing times followed by the Chinese-Japanese-Korean (CJK) and Arabic languages. Other predominantly Asian and African scripts have longer tokenization lengths and processing times. 

The latency implications of tokenization disparity are not limited to text models. Speech recognition models often produce a series of tokens as their output sequentially. Similarly, speech synthesis takes as an input tokenized text (Latif et al., 2023). Therefore, differences in tokenization affect speech models too. 

- **5.3 Long context processing**

---

[referencia=2c2ef6e29ff22be3 score=0.262]
In fact, more than half of the Japanese kanji characters require three tokens. 

> 1We offer a summary of the relevant tokenization approaches in Appendix A. 

2 

The existence of glitch tokens like “ゼウス” and “サ–ティワン” despite the lack of a dedicated token for “言” shows that tokenizers are heavily influenced by the biases of the corpus source. If one uses non-natural inputs, log files, or specialist forums, the tokenizer vocabulary would reflect this. While `cl100k_base` , the tokenizer used for the newer ChatGPT and GPT-4, may not have glitch tokens it still requires two tokens to represent some Cyrillic letters and three tokens for more than 65% of kanji characters. Therefore, to place all languages on an equal footing, it is important to have the tokens balanced across languages. 

## **3 Measuring Tokenizer Parity** 

To demonstrate that the above examples are not anecdotal evidence, we introduce the notion of _tokenizer parity_ to systematically assess how fairly tokenizers treat equivalent sentences in different languages. Parity occurs when a tokenizer exhibits similar tokenized lengths for the same sentence in different languages. Take a sentence _sA_ in language _A_ and its translation _sB_ to language _B_ . Then, a tokenizer _t_ achieves parity for _A_ with respect to _B_ at _sA_ and _sB_ if<sup>_|t_(</sup><sup>_sA_)</sup><sup>_|_</sup> / _|t_ ( _sB_ ) _| ≈_ 1, where _t_ ( _sA_ ) is the tokenization of the sentence _sA_ and _|t_ ( _sA_ ) _|_ represents its length. The ratio<sup>_|t_(</sup><sup>_sA_)</sup><sup>_|_</sup> / _|t_ ( _sB_ ) _|_ is the _premium_ for _A_ relative to _B_ .<sup>2</sup>

---

[referencia=2c2ef6e29ff22be3 score=0.200]
## **1 Introduction** 

Language models are increasingly important in natural language processing tasks, as they can understand and generate human-like language. They have been deployed in applications such as virtual assistants (Chen et al., 2021; Ouyang et al., 2022), chatbots (Kuhail et al., 2023; Lee et al., 2023), machine translation (Stahlberg, 2020; Ranathunga et al., 2023), and text summarization (Kryściński et al., 2019; Xu et al., 2020). As general-purpose technologies, it is also projected that Large Language Models (LLMs) will have a significant impact on the economy and the labour market (Teubner et al., 2023; Eloundou et al., 2023). 

Such LLMs are often trained using large swaths of internet content regardless of language. Hence, these models often end up being multilingual, even if not by design. ChatGPT (OpenAI, 2022) is a prominent recent example (Bang et al., 2023; Jiao et al., 2023; Johnson, ’ 2023). Given the economic benefits of LLMs and LLM-derived technology, it s beneficial that they support multiple languages. Equal access is crucial, and multilingual support is a key component of this. 

However, this multilingualism is currently treated as a curious emergent phenomenon rather than a carefully designed, controlled and managed process. The performance of LLMs has been shown to be generally lower in non-target languages, a problem especially pronounced for low-resource languages (Virtanen et al., 2019; Ahuja et al., 2023). Providing access to the same technology in different languages but moderation and safety tools only for some has resulted in dire societal consequences before (Stecklow, 2018; Facebook, 2021; Leung, 2022). Differing cost of access could also reinforce inequality in opportunities for economic mobility and social participation (Lythreatis et al., 2022). Therefore, as LLM multilingualism emerges, 

37th Conference on Neural Information Processing Systems (NeurIPS 2023). 

we should pay attention to ensuring comparable performance and accessibility across the supported languages, regardless of whether by design or by chance.

---

[referencia=2c2ef6e29ff22be3 score=0.195]
OpenAI. 2022. tiktoken. Git commit: `82facf9` . 

OpenAI. 2023. GPT-4 technical report. _arXiv preprint arXiv:2303.08774_ . 

- Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. _Advances in Neural Information Processing Systems_ . 

- Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon Htut, and Samuel Bowman. 2022. BBQ: A hand-built bias benchmark for question answering. In _Findings of the Association for Computational Linguistics: ACL 2022_ . 

- Jonas Pfeiffer, Ivan Vulić, Iryna Gurevych, and Sebastian Ruder. 2021. UNKs everywhere: Adapting multilingual language models to new scripts. In _Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing_ . 

- Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. Language models are unsupervised multitask learners. 

- Jenalea Rajab. 2022. Effect of tokenisation strategies for low-resourced Southern African languages. In _3rd Workshop on African Natural Language Processing_ . 

- Krithika Ramesh, Sunayana Sitaram, and Monojit Choudhury. 2023. Fairness in language models beyond English: Gaps and challenges. In _Findings of the Association for Computational Linguistics: EACL 2023_ . Association for Computational Linguistics. 

15

---

[referencia=2c2ef6e29ff22be3 score=0.166]
**Building a multilingually fair parallel corpus.** Building and evaluating multilingually fair tokenizers requires attention to the parallel corpus used. One must ensure a balanced representation of topics, otherwise, the resulting tokenizer might end up being multilingually fair only for a subset of topics. The presence of named entities must also be balanced. For example, in FLORES-200, there are many English-centric names and institutions, which might skew the results in favour of English. Additionally, the same sentence can have different translations with varying tokenization lengths. To account for this, a diversity of translations could ensure tokenization fairness across languages. These limitations also hold for the results in this paper. Hence, developing a well-curated and diverse parallel corpus is crucial for the development and evaluation of a multilingually fair tokenizer. 

**Building a multilingually fair tokenizer from monolinugal tokenizers.** As discussed in Section 4, byte-level, character-level and word-level tokenizers cannot achieve tokenization parity and subword tokenization is needed. However, simply training a subword tokenizer on a balanced dataset is also not sufficient as languages can share tokens. For example, “hotel” is written the same way in English, Spanish, Italian, Portuguese, Dutch, Danish, Hungarian, Polish, etc. Hence, languages from more numerous language families will also witness shorter tokenization lengths while more isolated languages and scripts, e.g. Korean, would see larger language premiums: “hotel” in Korean is “호텔” and no other language has the same spelling as no other language uses the Korean script. 

To address this issue, we suggest a two-stage process towards building a multilingually fair tokenizer. First, train individual monolingual tokenizers for all target languages. Then, merge them while maintaining parity. The merging can be done by starting with the 256 tokens corresponding to each value a byte can take and then repeatedly adding the most frequently used token for the language with the highest premium. 

While a multilingually fair tokenizer would lead to more tokens being needed for the dominant language, this additional cost would likely be much smaller than the benefit for the rest of the languages. The vocabulary size has diminishing returns: the additional tokens correspond to increasingly rare (parts of) words. For example, with only a third of the vocab- 

9

---

[referencia=2c2ef6e29ff22be3 score=0.153]
## **2 Intriguing Properties of Tokenization Across Languages** 

Subword tokenization is currently the preferred approach for state of the art language models (Kudo and Richardson, 2018). In this section, we show how artefacts from data collection might result in technical terms or rare words having dedicated tokens, while more commonly used words and non-Latin characters end up requiring multiple tokens. 

Using large corpora scraped from the internet results in _peculiar_ choices for tokens. For instance, GPT-2 contains _glitch tokens_ which can be usernames or concepts from games (Rumbelow and Watkins, 2023b; Miles and Riley, 2023). As an example, `BuyableInstoreAndOnline` , likely coming from an online store backend, has a dedicated token. Another such token is `rawdownloadcloneembedreportprint` . 

While such obscure terms get their own tokens, the frequently used Arabic word “ ” (meaning “why”) is broken into letters with each letter having its own token. The sameلماذا word in Bulgarian (“защо”) is not only broken down to letters, but some of the letters require two tokens to be represented, resulting in 6 tokens for this 4 letter word. 



One may argue that this is because Arabic and Bulgarian are not target languages for GPT-2. However, glitch tokens also exist for Japanese: there are dedicated tokens for “ゼウス”, the name of the ancient Greek god Zeus and “サ–ティワン”, the name of an ice cream chain (Rumbelow and Watkins, 2023a). At the same time, GPT-2 requires 3 tokens to represent the much more commonly used kanji character for “to say”: 



In fact, more than half of the Japanese kanji characters require three tokens. 

> 1We offer a summary of the relevant tokenization approaches in Appendix A. 

2

---

[referencia=2c2ef6e29ff22be3 score=0.133]
## **4 Tokenization Length Differences Across Languages** 

Languages vary significantly in the number of tokens required to encode the same content, as demonstrated in the examples in Section 2. Hence, following Section 3, we measure the tokenization premium of different tokenizers. To this end, we use the FLORES-200 parallel corpus, comprising of the same 2000 sentences taken from Wikipedia and human-translated to 200 different languages (Guzmán et al., 2019; Goyal et al., 2021; Costa-jussà et al., 2022). We look at subword tokenization models which target English, languages other than English, language varieties, multi-lingual tokenizers, as well as tokenizer-free (byte-level) modelling.