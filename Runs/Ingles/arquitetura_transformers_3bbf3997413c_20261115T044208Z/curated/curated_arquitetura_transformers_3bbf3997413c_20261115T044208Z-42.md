[referencia=a2690ed31e8cc7e9 score=0.928]
# **Neural Machine Translation of Rare Words with Subword Units** 

## **Rico Sennrich** and **Barry Haddow** and **Alexandra Birch** School of Informatics, University of Edinburgh 

`{rico.sennrich,a.birch}@ed.ac.uk` , `bhaddow@inf.ed.ac.uk` 

## **Abstract** 

Neural machine translation (NMT) models typically operate with a fixed vocabulary, but translation is an open-vocabulary problem. Previous work addresses the translation of out-of-vocabulary words by backing off to a dictionary. In this paper, we introduce a simpler and more effective approach, making the NMT model capable of open-vocabulary translation by encoding rare and unknown words as sequences of subword units. This is based on the intuition that various word classes are translatable via smaller units than words, for instance names (via character copying or transliteration), compounds (via compositional translation), and cognates and loanwords (via phonological and morphological transformations). We discuss the suitability of different word segmentation techniques, including simple character n- gram models and a segmentation based on the _byte pair encoding_ compression algorithm, and empirically show that subword models improve over a back-off dictionary baseline for the WMT 15 translation tasks English→German and English→Russian by up to 1.1 and 1.3 BLEU, respectively.

---

[referencia=a2690ed31e8cc7e9 score=0.789]
### **4.1 Subword statistics** 

Apart from translation quality, which we will verify empirically, our main objective is to represent an open vocabulary through a compact fixed-size subword vocabulary, and allow for efficient training and decoding.<sup>8</sup> 

Statistics for different segmentations of the Ger- 



> 6Clipped unigram precision is essentially 1-gram BLEU without brevity penalty. 

> 7 `github.com/sebastien-j/LV_groundhog` 

> 8The time complexity of encoder-decoder architectures is at least linear to sequence length, and oversplitting harms efficiency. 

man side of the parallel data are shown in Table 1. A simple baseline is the segmentation of words into character n-grams.<sup>9</sup> Character n-grams allow for different trade-offs between sequence length (# tokens) and vocabulary size (# types), depending on the choice of n. The increase in sequence length is substantial; one way to reduce sequence length is to leave a shortlist of the k most frequent word types unsegmented. Only the unigram representation is truly open-vocabulary. However, the unigram representation performed poorly in preliminary experiments, and we report translation results with a bigram representation, which is empirically better, but unable to produce some tokens in the test set with the training set vocabulary. 

We report statistics for several word segmentation techniques that have proven useful in previous SMT research, including frequency-based compound splitting (Koehn and Knight, 2003), rulebased hyphenation (Liang, 1983), and Morfessor (Creutz and Lagus, 2002). We find that they only moderately reduce vocabulary size, and do not solve the unknown word problem, and we thus find them unsuitable for our goal of open-vocabulary translation without back-off dictionary. 

BPE meets our goal of being open-vocabulary, and the learned merge operations can be applied to the test set to obtain a segmentation with no unknown symbols.<sup>10</sup> Its main difference from the character-level model is that the more compact representation of BPE allows for shorter sequences, and that the attention model operates on variable-length units.<sup>11</sup> Table 1 shows BPE with 59 500 merge operations, and joint BPE with 89 500 operations.

---

[referencia=a2690ed31e8cc7e9 score=0.763]
## **4 Evaluation** 

Figure 1: BPE merge operations learned from dictionary {‘low’, ‘lowest’, ‘newer’, ‘wider’}. 

gorithm 1. In practice, we increase by indexing all pairs, and updating data structures incrementally. 

The main difference to other compression algorithms, such as Huffman encoding, which have been proposed to produce a variable-length encoding of words for NMT (Chitnis and DeNero, 2015), is that our symbol sequences are still interpretable as subword units, and that the network can generalize to translate and produce new words (unseen at training time) on the basis of these subword units. 

Figure 1 shows a toy example of learned BPE operations. At test time, we first split words into sequences of characters, then apply the learned operations to merge the characters into larger, known symbols. This is applicable to any word, and allows for open-vocabulary networks with fixed symbol vocabularies.<sup>3</sup> In our example, the OOV ‘lower’ would be segmented into ‘low er·’. 



> 3The only symbols that will be unknown at test time are unknown characters, or symbols of which all occurrences in the training text have been merged into larger symbols, like ‘safeguar’, which has all occurrences in our training text merged into ‘safeguard’. We observed no such symbols at test time, but the issue could be easily solved by recursively reversing specific merges until all symbols are known. 

We aim to answer the following empirical questions: 

- Can we improve the translation of rare and unseen words in neural machine translation by representing them via subword units? 

- Which segmentation into subword units performs best in terms of vocabulary size, text size, and translation quality? 

We perform experiments on data from the shared translation task of WMT 2015. For English→German, our training set consists of 4.2 million sentence pairs, or approximately 100 million tokens. For English→Russian, the training set consists of 2.6 million sentence pairs, or approximately 50 million tokens. We tokenize and truecase the data with the scripts provided in Moses (Koehn et al., 2007). We use newstest2013 as development set, and report results on newstest2014 and newstest2015.

---

[referencia=a2690ed31e8cc7e9 score=0.750]
## **6 Conclusion** 

The main contribution of this paper is that we show that neural machine translation systems are capable of open-vocabulary translation by representing rare and unseen words as a sequence of subword units.<sup>14</sup> This is both simpler and more effective than using a back-off translation model. We introduce a variant of byte pair encoding for word segmentation, which is capable of encoding open vocabularies with a compact symbol vocabulary of variable-length subword units. We show performance gains over the baseline with both BPE segmentation, and a simple character bigram segmentation. 

Our analysis shows that not only out-ofvocabulary words, but also rare in-vocabulary words are translated poorly by our baseline NMT 



> 14The source code of the segmentation algorithms is available at `https://github.com/rsennrich/ subword-nmt` . 

system, and that reducing the vocabulary size of subword models can actually improve performance. In this work, our choice of vocabulary size is somewhat arbitrary, and mainly motivated by comparison to prior work. One avenue of future research is to learn the optimal vocabulary size for a translation task, which we expect to depend on the language pair and amount of training data, automatically. We also believe there is further potential in bilingually informed segmentation algorithms to create more alignable subword units, although the segmentation algorithm cannot rely on the target text at runtime. 

While the relative effectiveness will depend on language-specific factors such as vocabulary size, we believe that subword segmentations are suitable for most language pairs, eliminating the need for large NMT vocabularies or back-off models. 

## **Acknowledgments** 

We thank Maja Popovi´c for her implementation of CHRF, with which we verified our reimplementation. The research presented in this publication was conducted in cooperation with Samsung Electronics Polska sp. z o.o. - Samsung R&D Institute Poland. This project received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement 645452 (QT21).

---

[referencia=a2690ed31e8cc7e9 score=0.744]
## **1 Introduction** 

Neural machine translation has recently shown impressive results (Kalchbrenner and Blunsom, 2013; Sutskever et al., 2014; Bahdanau et al., 2015). However, the translation of rare words is an open problem. The vocabulary of neural models is typically limited to 30 000–50 000 words, but translation is an open-vocabulary probThe research presented in this publication was conducted in cooperation with Samsung Electronics Polska sp. z o.o. - Samsung R&D Institute Poland. 



lem, and especially for languages with productive word formation processes such as agglutination and compounding, translation models require mechanisms that go below the word level. As an example, consider compounds such as the German _Abwasser|behandlungs|anlange_ ‘sewage water treatment plant’, for which a segmented, variable-length representation is intuitively more appealing than encoding the word as a fixed-length vector. 

For word-level NMT models, the translation of out-of-vocabulary words has been addressed through a back-off to a dictionary look-up (Jean et al., 2015; Luong et al., 2015b). We note that such techniques make assumptions that often do not hold true in practice. For instance, there is not always a 1-to-1 correspondence between source and target words because of variance in the degree of morphological synthesis between languages, like in our introductory compounding example. Also, word-level models are unable to translate or generate unseen words. Copying unknown words into the target text, as done by (Jean et al., 2015; Luong et al., 2015b), is a reasonable strategy for names, but morphological changes and transliteration is often required, especially if alphabets differ. 

We investigate NMT models that operate on the level of subword units. Our main goal is to model open-vocabulary translation in the NMT network itself, without requiring a back-off model for rare words. In addition to making the translation process simpler, we also find that the subword models achieve better accuracy for the translation of rare words than large-vocabulary models and back-off dictionaries, and are able to productively generate new words that were not seen at training time. Our analysis shows that the neural networks are able to learn compounding and transliteration from subword representations. 

This paper has two main contributions:

---

[referencia=a2690ed31e8cc7e9 score=0.585]
### **3.2 Byte Pair Encoding (BPE)** 

Byte Pair Encoding (BPE) (Gage, 1994) is a simple data compression technique that iteratively replaces the most frequent pair of bytes in a sequence with a single, unused byte. We adapt this algorithm for word segmentation. Instead of merging frequent pairs of bytes, we merge characters or character sequences. 

Firstly, we initialize the symbol vocabulary with the character vocabulary, and represent each word as a sequence of characters, plus a special end-ofword symbol ‘·’, which allows us to restore the original tokenization after translation. We iteratively count all symbol pairs and replace each occurrence of the most frequent pair (‘A’, ‘B’) with a new symbol ‘AB’. Each merge operation produces a new symbol which represents a character n-gram. Frequent character n-grams (or whole words) are eventually merged into a single symbol, thus BPE requires no shortlist. The final symbol vocabulary size is equal to the size of the initial vocabulary, plus the number of merge operations – the latter is the only hyperparameter of the algorithm. 

For we do not consider pairs that cross word boundaries. The algorithm can thus be run on the dictionary extracted from a text, with each word being weighted by its frequency. A minimal Python implementation is shown in Al- 

**Algorithm 1** Learn BPE operations 





<!-- Start of picture text -->

---

[referencia=a2690ed31e8cc7e9 score=0.566]
For English→German, we observe the best BLEU score of 25.3 with C2-50k, but the best CHRF3 score of 54.1 with BPE-J90k. For comparison to the (to our knowledge) best non-neural MT system on this data set, we report syntaxbased SMT results (Sennrich and Haddow, 2015). We observe that our best systems outperform the syntax-based system in terms of BLEU, but not in terms of CHRF3. Regarding other neural systems, Luong et al. (2015a) report a BLEU score of 25.9 on newstest2015, but we note that they use an ensemble of 8 independently trained models, and also report strong improvements from applying dropout, which we did not use. We are confident that our improvements to the translation of rare words are orthogonal to improvements achievable through other improvements in the network archi- 

tecture, training algorithm, or better ensembles. 

For English→Russian, the state of the art is the phrase-based system by Haddow et al. (2015). It outperforms our WDict baseline by 1.5 BLEU. The subword models are a step towards closing this gap, and BPE-J90k yields an improvement of 1.3 BLEU, and 2.0 CHRF3, over WDict. 

As a further comment on our translation results, we want to emphasize that performance variability is still an open problem with NMT. On our development set, we observe differences of up to 1 BLEU between different models. For single systems, we report the results of the model that performs best on dev (out of 8), which has a stabilizing effect, but how to control for randomness deserves further attention in future research.

---

[referencia=a2690ed31e8cc7e9 score=0.426]
We evaluate two methods of applying BPE: learning two independent encodings, one for the source, one for the target vocabulary, or learning the encoding on the union of the two vocabularies (which we call _joint BPE_ ).<sup>4</sup> The former has the advantage of being more compact in terms of text and vocabulary size, and having stronger guarantees that each subword unit has been seen in the training text of the respective language, whereas the latter improves consistency between the source and the target segmentation. If we apply BPE independently, the same name may be segmented differently in the two languages, which makes it harder for the neural models to learn a mapping between the subword units. To increase the consistency between English and Russian segmentation despite the differing alphabets, we transliterate the Russian vocabulary into Latin characters with ISO-9 to learn the joint BPE encoding, then transliterate the BPE merge operations back into Cyrillic to apply them to the Russian training text.<sup>5</sup>

---

[referencia=a2690ed31e8cc7e9 score=0.342]
### **3.1 Related Work** 

For Statistical Machine Translation (SMT), the translation of unknown words has been the subject of intensive research. 

A large proportion of unknown words are names, which can just be copied into the target text if both languages share an alphabet. If alphabets differ, transliteration is required (Durrani et al., 2014). Character-based translation has also been investigated with phrase-based models, which proved especially successful for closely related languages (Vilar et al., 2007; Tiedemann, 2009; Neubig et al., 2012). 

The segmentation of morphologically complex words such as compounds is widely used for SMT, and various algorithms for morpheme segmentation have been investigated (Nießen and Ney, 2000; Koehn and Knight, 2003; Virpioja et al., 2007; Stallard et al., 2012). Segmentation algorithms commonly used for phrase-based SMT tend to be conservative in their splitting decisions, whereas we aim for an aggressive segmentation that allows for open-vocabulary translation with a compact network vocabulary, and without having to resort to back-off dictionaries. 

The best choice of subword units may be taskspecific. For speech recognition, phone-level language models have been used (Bazzi and Glass, 2000). Mikolov et al. (2012) investigate subword language models, and propose to use syllables. For multilingual segmentation tasks, multilingual algorithms have been proposed (Snyder and Barzilay, 2008). We find these intriguing, but inapplicable at test time. 

Various techniques have been proposed to produce fixed-length continuous word vectors based on characters or morphemes (Luong et al., 2013; Botha and Blunsom, 2014; Ling et al., 2015a; Kim et al., 2015). An effort to apply such techniques to NMT, parallel to ours, has found no significant improvement over word-based approaches (Ling et al., 2015b). One technical difference from our work is that the attention mechanism still operates on the level of words in the model by Ling et al. (2015b), and that the representation of each word is fixed-length. We expect that the attention mechanism benefits from our variable-length representation: the network can learn to place atten-

---

[referencia=a2690ed31e8cc7e9 score=0.301]
> 11We highlighted the limitations of word-level attention in section 3.1. At the other end of the spectrum, the character level is suboptimal for alignment (Tiedemann, 2009). 

|name|segmentation|shortlist|vocab<br>source|ulary<br>target|BL<br>single|EU<br> ens-8|CHRF3<br>single ens-8|unig<br>all|ram F<br>rare|1 (%)<br> OOV|
|---|---|---|---|---|---|---|---|---|---|---|
|syntax-bas|ed (Sennrich an|d Haddow|, 2015)||24.4|-|55.3<br>-|59.1|46.0|37.7|
|WUnk|-|-|300 000|500 000|20.6|22.8|47.2<br>48.9|56.7|20.4|0.0|
|WDict|-|-|300 000|500 000|22.0|24.2|50.5<br>52.4|58.1|36.8|**36.8**|
|C2-50k|char-bigram|50 000|60 000|60 000|**22.8**|**25.3**|51.9<br>53.5|58.4|40.5|30.9|
|BPE-60k|BPE|-|60 000|60 000|21.5|24.5|**52.0**<br>53.9|58.4|40.9|29.3|
|BPE-J90k|BPE (joint)|-|90 000|90 000|**22.8**|24.7|51.7<br>**54.1**|**58.5 **|**41.8**|33.6|

---

[referencia=a2690ed31e8cc7e9 score=0.274]
systems can productively form new words such as compounds. 

For the 50 000 most frequent words, the representation is the same for all neural networks, and all neural networks achieve comparable unigram F1 for this category. For the interval between frequency rank 50 000 and 500 000, the comparison between C2-3/500k and C2-50k unveils an interesting difference. The two systems only differ in the size of the shortlist, with C2-3/500k representing words in this interval as single units, and C250k via subword units. We find that the performance of C2-3/500k degrades heavily up to frequency rank 500 000, at which point the model switches to a subword representation and performance recovers. The performance of C2-50k remains more stable. We attribute this to the fact that subword units are less sparse than words. In our training set, the frequency rank 50 000 corresponds to a frequency of 60 in the training data; the frequency rank 500 000 to a frequency of 2. Because subword representations are less sparse, reducing the size of the network vocabulary, and representing more words via subword units, can lead to better performance. 

The F1 numbers hide some qualitative differences between systems. For English→German, WDict produces few OOVs (26.5% recall), but with high precision (60.6%) , whereas the subword systems achieve higher recall, but lower precision. We note that the character bigram model C2-50k produces the most OOV words, and achieves relatively low precision of 29.1% for this category. However, it outperforms the back-off dictionary in recall (33.0%). BPE-60k, which suffers from transliteration (or copy) errors due to segmentation inconsistencies, obtains a slightly better precision (32.4%), but a worse recall (26.6%). In contrast to BPE-60k, the joint BPE encoding of BPEJ90k improves both precision (38.6%) and recall (29.8%).

---

[referencia=a2690ed31e8cc7e9 score=0.258]
### **4.2 Translation experiments** 

English→German translation results are shown in Table 2; English→Russian results in Table 3. 

Our baseline **WDict** is a word-level model with a back-off dictionary. It differs from **WUnk** in that the latter uses no back-off dictionary, and just represents out-of-vocabulary words as UNK<sup>12</sup> . The back-off dictionary improves unigram F1 for rare and unseen words, although the improvement is smaller for English→Russian, since the back-off dictionary is incapable of transliterating names. 

All subword systems operate without a back-off dictionary. We first focus on unigram F1, where all systems improve over the baseline, especially for rare words (36.8%→41.8% for EN→DE; 26.5%→29.7% for EN→RU). For OOVs, the baseline strategy of copying unknown words works well for English→German. However, when alphabets differ, like in English→Russian, the subword models do much better. 



> 12 We use _UNK_ for words that are outside the model vocabulary, and _OOV_ for those that do not occur in the training text. 

Unigram F1 scores indicate that learning the BPE symbols on the vocabulary union ( **BPEJ90k** ) is more effective than learning them separately ( **BPE-60k** ), and more effective than using character bigrams with a shortlist of 50 000 unsegmented words ( **C2-50k** ), but all reported subword segmentations are viable choices and outperform the back-off dictionary baseline. 

Our subword representations cause big improvements in the translation of rare and unseen words, but these only constitute 9-11% of the test sets. Since rare words tend to carry central information in a sentence, we suspect that BLEU and CHRF3 underestimate their effect on translation quality. Still, we also see improvements over the baseline in total unigram F1, as well as BLEU and CHRF3, and the subword ensembles outperform the WDict baseline by 0.3–1.3 BLEU and 0.6–2 CHRF3. There is some inconsistency between BLEU and CHRF3, which we attribute to the fact that BLEU has a precision bias, and CHRF3 a recall bias.

---

[referencia=a2690ed31e8cc7e9 score=0.257]
For English→Russian, unknown names can only rarely be copied, and usually require transliteration. Consequently, the WDict baseline performs more poorly for OOVs (9.2% precision; 5.2% recall), and the subword models improve both precision and recall (21.9% precision and 15.6% recall for BPE-J90k). The full unigram F1 plot is shown in Figure 3. 

13We perform binning of words with the same training set frequency, and apply bezier smoothing to the graph. 

|name|segmentation|shortlist|vocab<br>source|ulary<br>target|BL<br>single|EU<br> ens-8|CHR<br>single|F3<br>unig<br> ens-8<br>all|ram F<br>rare|1 (%)<br> OOV|
|---|---|---|---|---|---|---|---|---|---|---|
|phrase-bas|ed (Haddow et|al., 2015)|||24.3|-|53.8|-<br>56.0|31.3|16.5|
|WUnk|-|-|300 000|500 000|18.8|22.4|46.5|49.9<br>54.2|25.2|0.0|
|WDict|-|-|300 000|500 000|19.1|22.8|47.5|51.0<br>54.8|26.5|6.6|
|C2-50k|char-bigram|50 000|60 000|60 000|**20.9**|**24.1**|49.0|51.6<br>55.2|27.8|17.4|
|BPE-60k|BPE|-|60 000|60 000|20.5|23.6|**49.8**|52.7<br>55.3|29.7|15.6|
|BPE-J90k|BPE (joint)|-|90 000|100 000|20.4|**24.1**|49.7|**53.0**<br>**55.8 **|**29.7**|**18.3**|

---

[referencia=a2690ed31e8cc7e9 score=0.238]
- Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural Machine Translation by Jointly Learning to Align and Translate. In _Proceedings of the International Conference on Learning Representations (ICLR)_ . 

- Issam Bazzi and James R. Glass. 2000. Modeling outof-vocabulary words for robust speech recognition. In _Sixth International Conference on Spoken Language Processing, ICSLP 2000 / INTERSPEECH 2000_ , pages 401–404, Beijing, China. 

- Jan A. Botha and Phil Blunsom. 2014. Compositional Morphology for Word Representations and Language Modelling. In _Proceedings of the 31st International Conference on Machine Learning (ICML)_ , Beijing, China. 

- Rohan Chitnis and John DeNero. 2015. VariableLength Word Encodings for Neural Translation Models. In _Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ . 

- Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014. Learning Phrase Representations using RNN Encoder– Decoder for Statistical Machine Translation. In _Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1724–1734, Doha, Qatar. Association for Computational Linguistics. 

- Mathias Creutz and Krista Lagus. 2002. Unsupervised Discovery of Morphemes. In _Proceedings of the ACL-02 Workshop on Morphological and Phonological Learning_ , pages 21–30. Association for Computational Linguistics. 

- Nadir Durrani, Hassan Sajjad, Hieu Hoang, and Philipp Koehn. 2014. Integrating an Unsupervised Transliteration Model into Statistical Machine Translation. In _Proceedings of the 14th Conference of the European Chapter of the Association for Computational Linguistics, EACL 2014_ , pages 148–153, Gothenburg, Sweden.

---

[referencia=a2690ed31e8cc7e9 score=0.194]
Maja Popovi´c. 2015. chrF: character n-gram F-score for automatic MT evaluation. In _Proceedings of the_ Matthew D. Zeiler. 2012. ADADELTA: An Adaptive _Tenth Workshop on Statistical Machine Translation_ , Learning Rate Method. _CoRR_ , abs/1212.5701. 

pages 392–395, Lisbon, Portugal. Association for Computational Linguistics. 



<!-- Start of picture text -->
Rico Sennrich and Barry Haddow. 2015. A Joint<br>Dependency Model of Morphological and Syntac-<br>tic Structure for Statistical Machine Translation. In<br>Proceedings of the 2015 Conference on Empirical<br>Methods in Natural Language Processing , pages<br>2081–2087, Lisbon, Portugal. Association for Com-<br>putational Linguistics.<br>Benjamin Snyder and Regina Barzilay. 2008. Unsu-<br>pervised Multilingual Learning for Morphological<br>Segmentation. In Proceedings of ACL-08: HLT ,<br>pages 737–745, Columbus, Ohio. Association for<br>Computational Linguistics.<br><!-- End of picture text -->

David Stallard, Jacob Devlin, Michael Kayser, Yoong Keok Lee, and Regina Barzilay. 2012. Unsupervised Morphology Rivals Supervised Morphology for Arabic MT. In _The 50th Annual Meeting of the Association for Computational Linguistics, Proceedings of the Conference, July 8-14, 2012, Jeju Island, Korea - Volume 2: Short Papers_ , pages 322– 327. 

Miloš Stanojevi´c, Amir Kamran, Philipp Koehn, and Ondˇrej Bojar. 2015. Results of the WMT15 Metrics Shared Task. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 256– 273, Lisbon, Portugal. Association for Computational Linguistics. 

Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. 2014. Sequence to Sequence Learning with Neural Networks. In _Advances in Neural Information Processing Systems 27: Annual Conference on Neural Information Processing Systems 2014_ , pages 3104–3112, Montreal, Quebec, Canada.

---

[referencia=a2690ed31e8cc7e9 score=0.185]
tion on different subword units at each step. Recall our introductory example _Abwasserbehandlungsanlange_ , for which a subword segmentation avoids the information bottleneck of a fixed-length representation. 

Neural machine translation differs from phrasebased methods in that there are strong incentives to minimize the vocabulary size of neural models to increase time and space efficiency, and to allow for translation without back-off models. At the same time, we also want a compact representation of the text itself, since an increase in text length reduces efficiency and increases the distances over which neural models need to pass information. 

A simple method to manipulate the trade-off between vocabulary size and text size is to use shortlists of unsegmented words, using subword units only for rare words. As an alternative, we propose a segmentation algorithm based on byte pair encoding (BPE), which lets us learn a vocabulary that provides a good compression rate of the text.

---

[referencia=a2690ed31e8cc7e9 score=0.169]
This paper has two main contributions: 

• We show that open-vocabulary neural ma- 

chine translation is possible by encoding (rare) words via subword units. We find our architecture simpler and more effective than using large vocabularies and back-off dictionaries (Jean et al., 2015; Luong et al., 2015b). 

- We adapt _byte pair encoding_ (BPE) (Gage, 1994), a compression algorithm, to the task of word segmentation. BPE allows for the representation of an open vocabulary through a fixed-size vocabulary of variable-length character sequences, making it a very suitable word segmentation strategy for neural network models. 

## **2 Neural Machine Translation** 

We follow the neural machine translation architecture by Bahdanau et al. (2015), which we will briefly summarize here. However, we note that our approach is not specific to this architecture. 

The neural machine translation system is implemented as an encoder-decoder network with recurrent neural networks. 

The encoder is a bidirectional neural network with gated recurrent units (Cho et al., 2014) that reads an input sequence x = (x1, ..., xm) and calculates a forward sequence of hidden states (<sup>−→</sup> h 1, ...,<sup>−→</sup> h m), and a backward sequence (<sup>←−</sup> h 1, ...,<sup>←−</sup> h m). The hidden states<sup>−→</sup> h j and<sup>←−</sup> h j are concatenated to obtain the annotation vector h . j 

The decoder is a recurrent neural network that predicts a target sequence y = (y1, ..., yn). Each word yi is predicted based on a recurrent hidden state si, the previously predicted word yi−1, and a context vector ci. ci is computed as a weighted sum of the annotations hj. The weight of each annotation hj is computed through an _alignment model_ αij, which models the probability that yi is aligned to xj. The alignment model is a singlelayer feedforward neural network that is learned jointly with the rest of the network through backpropagation. 

A detailed description can be found in (Bahdanau et al., 2015). Training is performed on a parallel corpus with stochastic gradient descent. For translation, a beam search with small beam size is employed.

---

[referencia=a2690ed31e8cc7e9 score=0.156]
- Philipp Koehn, Hieu Hoang, Alexandra Birch, Chris Callison-Burch, Marcello Federico, Nicola Bertoldi, Brooke Cowan, Wade Shen, Christine Moran, Richard Zens, Chris Dyer, Ondˇrej Bojar, Alexandra Constantin, and Evan Herbst. 2007. Moses: Open Source Toolkit for Statistical Machine Translation. In _Proceedings of the ACL-2007 Demo and Poster Sessions_ , pages 177–180, Prague, Czech Republic. Association for Computational Linguistics. 

- Franklin M. Liang. 1983. _Word hy-phen-a-tion by com-put-er_ . Ph.D. thesis, Stanford University, Department of Linguistics, Stanford, CA. 

- Wang Ling, Chris Dyer, Alan W. Black, Isabel Trancoso, Ramon Fermandez, Silvio Amir, Luis Marujo, and Tiago Luis. 2015a. Finding Function in Form: Compositional Character Models for Open Vocabulary Word Representation. In _Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 1520– 1530, Lisbon, Portugal. Association for Computational Linguistics. 

- Wang Ling, Isabel Trancoso, Chris Dyer, and Alan W. Black. 2015b. Character-based Neural Machine Translation. _ArXiv e-prints_ , November. 

- Thang Luong, Richard Socher, and Christopher D. Manning. 2013. Better Word Representations with Recursive Neural Networks for Morphology. In _Proceedings of the Seventeenth Conference on Computational Natural Language Learning, CoNLL 2013, Sofia, Bulgaria, August 8-9, 2013_ , pages 104– 113. 

- Thang Luong, Hieu Pham, and Christopher D. Manning. 2015a. Effective Approaches to Attentionbased Neural Machine Translation. In _Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing_ , pages 1412– 1421, Lisbon, Portugal. Association for Computational Linguistics.

---

[referencia=a2690ed31e8cc7e9 score=0.108]
- Chris Dyer, Victor Chahuneau, and Noah A. Smith. 2013. A Simple, Fast, and Effective Reparameterization of IBM Model 2. In _Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , pages 644–648, Atlanta, Georgia. Association for Computational Linguistics. 

- Philip Gage. 1994. A New Algorithm for Data Compression. _C Users J._ , 12(2):23–38, February. 

- Barry Haddow, Matthias Huck, Alexandra Birch, Nikolay Bogoychev, and Philipp Koehn. 2015. The Edinburgh/JHU Phrase-based Machine Translation Systems for WMT 2015. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 126–133, Lisbon, Portugal. Association for Computational Linguistics. 

- Sébastien Jean, Kyunghyun Cho, Roland Memisevic, and Yoshua Bengio. 2015. On Using Very Large Target Vocabulary for Neural Machine Translation. In _Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)_ , pages 1–10, Beijing, China. Association for Computational Linguistics. 

- Nal Kalchbrenner and Phil Blunsom. 2013. Recurrent Continuous Translation Models. In _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing_ , Seattle. Association for Computational Linguistics. 

- Yoon Kim, Yacine Jernite, David Sontag, and Alexander M. Rush. 2015. Character-Aware Neural Language Models. _CoRR_ , abs/1508.06615. 

Philipp Koehn and Kevin Knight. 2003. Empirical Methods for Compound Splitting. In _EACL ’03: Proceedings of the Tenth Conference on European Chapter of the Association for Computational Linguistics_ , pages 187–193, Budapest, Hungary. Association for Computational Linguistics.

---

[referencia=a2690ed31e8cc7e9 score=0.057]
In practice, we did not include infrequent subword units in the NMT network vocabulary, since there is noise in the subword symbol sets, e.g. because of characters from foreign alphabets. Hence, our network vocabularies in Table 2 are typically slightly smaller than the number of types in Table 1. 



> 9Our character n-grams do not cross word boundaries. We mark whether a subword is word-final or not with a special character, which allows us to restore the original tokenization. 

> 10Joint BPE can produce segments that are unknown because they only occur in the English training text, but these are rare (0.05% of test tokens). 

> 11We highlighted the limitations of word-level attention in section 3.1. At the other end of the spectrum, the character level is suboptimal for alignment (Tiedemann, 2009).