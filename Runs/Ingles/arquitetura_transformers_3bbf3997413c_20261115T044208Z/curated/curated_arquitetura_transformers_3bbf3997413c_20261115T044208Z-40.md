[referencia=a2690ed31e8cc7e9 score=0.009]
## **3 Subword Translation** 

The main motivation behind this paper is that the translation of some words is transparent in 

that they are translatable by a competent translator even if they are novel to him or her, based on a translation of known subword units such as morphemes or phonemes. Word categories whose translation is potentially transparent include: 

- named entities. Between languages that share an alphabet, names can often be copied from source to target text. Transcription or transliteration may be required, especially if the alphabets or syllabaries differ. Example: Barack Obama (English; German) Барак Обама (Russian) バラク・オバマ (ba-ra-ku o-ba-ma) (Japanese) 

- cognates and loanwords. Cognates and loanwords with a common origin can differ in regular ways between languages, so that character-level translation rules are sufficient (Tiedemann, 2012). Example: claustrophobia (English) Klaustrophobie (German) Клаустрофобия (Klaustrofobiâ) (Russian) 

- morphologically complex words. Words containing multiple morphemes, for instance formed via compounding, affixation, or inflection, may be translatable by translating the morphemes separately. Example: solar system (English) Sonnensystem (Sonne + System) (German) Naprendszer (Nap + Rendszer) (Hungarian) 

In an analysis of 100 rare tokens (not among the 50 000 most frequent types) in our German training data<sup>1</sup> , the majority of tokens are potentially translatable from English through smaller units. We find 56 compounds, 21 names, 6 loanwords with a common origin ( _emancipate_ → _emanzipieren_ ), 5 cases of transparent affixation ( _sweetish_ ‘sweet’ + ‘-ish’ → _süßlich_ ‘süß’ + ‘-lich’), 1 number and 1 computer language iden- 

Our hypothesis is that a segmentation of rare words into appropriate subword units is sufficient to allow for the neural translation network to learn transparent translations, and to generalize this knowledge to translate and produce unseen words.<sup>2</sup> We provide empirical support for this hy-

---

[referencia=a2690ed31e8cc7e9 score=0.004]
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

[referencia=a2690ed31e8cc7e9 score=0.003]
### **3.2 Byte Pair Encoding (BPE)** 

Byte Pair Encoding (BPE) (Gage, 1994) is a simple data compression technique that iteratively replaces the most frequent pair of bytes in a sequence with a single, unused byte. We adapt this algorithm for word segmentation. Instead of merging frequent pairs of bytes, we merge characters or character sequences. 

Firstly, we initialize the symbol vocabulary with the character vocabulary, and represent each word as a sequence of characters, plus a special end-ofword symbol ‘·’, which allows us to restore the original tokenization after translation. We iteratively count all symbol pairs and replace each occurrence of the most frequent pair (‘A’, ‘B’) with a new symbol ‘AB’. Each merge operation produces a new symbol which represents a character n-gram. Frequent character n-grams (or whole words) are eventually merged into a single symbol, thus BPE requires no shortlist. The final symbol vocabulary size is equal to the size of the initial vocabulary, plus the number of merge operations – the latter is the only hyperparameter of the algorithm. 

For we do not consider pairs that cross word boundaries. The algorithm can thus be run on the dictionary extracted from a text, with each word being weighted by its frequency. A minimal Python implementation is shown in Al- 

**Algorithm 1** Learn BPE operations 





<!-- Start of picture text -->

---

[referencia=a2690ed31e8cc7e9 score=0.003]
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

[referencia=a2690ed31e8cc7e9 score=0.003]
Table 2: English→German translation performance (BLEU, CHRF3 and unigram F1) on newstest2015. Ens-8: ensemble of 8 models. Best NMT system in bold. Unigram F1 (with ensembles) is computed for all words (n = 44085), rare words (not among top 50 000 in training set; n = 2900), and OOVs (not in training set; n = 1168). 

|segmentation|# tokens|# types|# UNK|
|---|---|---|---|
|none|100 m|1 750 000|1079|
|characters|550 m|3000|0|
|character bigrams|306 m|20 000|34|
|character trigrams|214 m|120 000|59|
|compound splitting<sup>△</sup>|102 m|1 100 000|643|
|morfessor*|109 m|544 000|237|
|hyphenation<sup>⋄</sup>|186 m|404 000|230|
|BPE|112 m|63 000|0|
|BPE (joint)|111 m|82 000|32|
|character bigrams<br>(shortlist: 50 000)|129 m|69 000|34|











Table 1: Corpus statistics for German training corpus with different word segmentation techniques. #UNK: number of unknown tokens in newstest2013. △: (Koehn and Knight, 2003); *: (Creutz and Lagus, 2002); ⋄: (Liang, 1983).

---

[referencia=a2690ed31e8cc7e9 score=0.003]
For English→German, we observe the best BLEU score of 25.3 with C2-50k, but the best CHRF3 score of 54.1 with BPE-J90k. For comparison to the (to our knowledge) best non-neural MT system on this data set, we report syntaxbased SMT results (Sennrich and Haddow, 2015). We observe that our best systems outperform the syntax-based system in terms of BLEU, but not in terms of CHRF3. Regarding other neural systems, Luong et al. (2015a) report a BLEU score of 25.9 on newstest2015, but we note that they use an ensemble of 8 independently trained models, and also report strong improvements from applying dropout, which we did not use. We are confident that our improvements to the translation of rare words are orthogonal to improvements achievable through other improvements in the network archi- 

tecture, training algorithm, or better ensembles. 

For English→Russian, the state of the art is the phrase-based system by Haddow et al. (2015). It outperforms our WDict baseline by 1.5 BLEU. The subword models are a step towards closing this gap, and BPE-J90k yields an improvement of 1.3 BLEU, and 2.0 CHRF3, over WDict. 

As a further comment on our translation results, we want to emphasize that performance variability is still an open problem with NMT. On our development set, we observe differences of up to 1 BLEU between different models. For single systems, we report the results of the model that performs best on dev (out of 8), which has a stabilizing effect, but how to control for randomness deserves further attention in future research.

---

[referencia=a2690ed31e8cc7e9 score=0.002]
Maja Popovi´c. 2015. chrF: character n-gram F-score for automatic MT evaluation. In _Proceedings of the_ Matthew D. Zeiler. 2012. ADADELTA: An Adaptive _Tenth Workshop on Statistical Machine Translation_ , Learning Rate Method. _CoRR_ , abs/1212.5701. 

pages 392–395, Lisbon, Portugal. Association for Computational Linguistics. 



<!-- Start of picture text -->
Rico Sennrich and Barry Haddow. 2015. A Joint<br>Dependency Model of Morphological and Syntac-<br>tic Structure for Statistical Machine Translation. In<br>Proceedings of the 2015 Conference on Empirical<br>Methods in Natural Language Processing , pages<br>2081–2087, Lisbon, Portugal. Association for Com-<br>putational Linguistics.<br>Benjamin Snyder and Regina Barzilay. 2008. Unsu-<br>pervised Multilingual Learning for Morphological<br>Segmentation. In Proceedings of ACL-08: HLT ,<br>pages 737–745, Columbus, Ohio. Association for<br>Computational Linguistics.<br><!-- End of picture text -->

David Stallard, Jacob Devlin, Michael Kayser, Yoong Keok Lee, and Regina Barzilay. 2012. Unsupervised Morphology Rivals Supervised Morphology for Arabic MT. In _The 50th Annual Meeting of the Association for Computational Linguistics, Proceedings of the Conference, July 8-14, 2012, Jeju Island, Korea - Volume 2: Short Papers_ , pages 322– 327. 

Miloš Stanojevi´c, Amir Kamran, Philipp Koehn, and Ondˇrej Bojar. 2015. Results of the WMT15 Metrics Shared Task. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 256– 273, Lisbon, Portugal. Association for Computational Linguistics. 

Ilya Sutskever, Oriol Vinyals, and Quoc V. Le. 2014. Sequence to Sequence Learning with Neural Networks. In _Advances in Neural Information Processing Systems 27: Annual Conference on Neural Information Processing Systems 2014_ , pages 3104–3112, Montreal, Quebec, Canada.

---

[referencia=a2690ed31e8cc7e9 score=0.002]
In practice, we did not include infrequent subword units in the NMT network vocabulary, since there is noise in the subword symbol sets, e.g. because of characters from foreign alphabets. Hence, our network vocabularies in Table 2 are typically slightly smaller than the number of types in Table 1. 



> 9Our character n-grams do not cross word boundaries. We mark whether a subword is word-final or not with a special character, which allows us to restore the original tokenization. 

> 10Joint BPE can produce segments that are unknown because they only occur in the English training text, but these are rare (0.05% of test tokens). 

> 11We highlighted the limitations of word-level attention in section 3.1. At the other end of the spectrum, the character level is suboptimal for alignment (Tiedemann, 2009).

---

[referencia=a2690ed31e8cc7e9 score=0.002]
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

[referencia=a2690ed31e8cc7e9 score=0.002]
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

[referencia=a2690ed31e8cc7e9 score=0.002]
### **5.2 Manual Analysis** 



<!-- Start of picture text -->
1<br>50 000 500 000<br>0.8<br>0.6<br>0.4<br>BPE-J90k<br>C2-50k<br>0.2 C2-300/500k<br>WDict<br>WUnk<br>0<br>10 0 10 1 10 2 10 3 10 4 10 5 10 6<br>training set frequency rank<br>1<br>unigram F<br><!-- End of picture text -->

Figure 2: English→German unigram F1 on newstest2015 plotted by training set frequency rank for different NMT systems. 



<!-- Start of picture text -->
1<br>50 000 500 000<br>0.8<br>0.6<br>0.4<br>BPE-J90k<br>0.2 C2-50k<br>WDict<br>WUnk<br>0<br>10 0 10 1 10 2 10 3 10 4 10 5 10 6<br>training set frequency rank<br>1<br>unigram F<br><!-- End of picture text -->

Figure 3: English→Russian unigram F1 on newstest2015 plotted by training set frequency rank for different NMT systems.

---

[referencia=a2690ed31e8cc7e9 score=0.002]
We evaluate two methods of applying BPE: learning two independent encodings, one for the source, one for the target vocabulary, or learning the encoding on the union of the two vocabularies (which we call _joint BPE_ ).<sup>4</sup> The former has the advantage of being more compact in terms of text and vocabulary size, and having stronger guarantees that each subword unit has been seen in the training text of the respective language, whereas the latter improves consistency between the source and the target segmentation. If we apply BPE independently, the same name may be segmented differently in the two languages, which makes it harder for the neural models to learn a mapping between the subword units. To increase the consistency between English and Russian segmentation despite the differing alphabets, we transliterate the Russian vocabulary into Latin characters with ISO-9 to learn the joint BPE encoding, then transliterate the BPE merge operations back into Cyrillic to apply them to the Russian training text.<sup>5</sup>

---

[referencia=a2690ed31e8cc7e9 score=0.001]
**Algorithm 1** Learn BPE operations 





<!-- Start of picture text -->
import re, collections<br>def get_stats(vocab):<br>pairs = collections.defaultdict(int)<br>for word, freq in vocab.items():<br>symbols = word.split()<br>for i in range(len(symbols)-1):<br>pairs[symbols[i],symbols[i+1]] += freq<br>return pairs<br>def merge_vocab(pair, v_in):<br>v_out = {}<br>bigram = re.escape(' '.join(pair))<br>p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')<br>for word in v_in:<br>w_out = p.sub(''.join(pair), word)<br>v_out[w_out] = v_in[word]<br>return v_out<br>vocab = {'l o w </w>' : 5, 'l o w e r </w>' : 2,<br>'n e w e s t </w>':6, 'w i d e s t </w>':3}<br>num_merges = 10<br>for i in range(num_merges):<br>pairs = get_stats(vocab)<br>best = max(pairs, key=pairs.get)<br>vocab = merge_vocab(best, vocab)<br>print (best)<br>r · → r·<br>l o → lo<br>lo w → low<br>e r· → er·<br><!-- End of picture text -->

---

[referencia=a2690ed31e8cc7e9 score=0.001]
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

[referencia=a2690ed31e8cc7e9 score=0.001]
tion on different subword units at each step. Recall our introductory example _Abwasserbehandlungsanlange_ , for which a subword segmentation avoids the information bottleneck of a fixed-length representation. 

Neural machine translation differs from phrasebased methods in that there are strong incentives to minimize the vocabulary size of neural models to increase time and space efficiency, and to allow for translation without back-off models. At the same time, we also want a compact representation of the text itself, since an increase in text length reduces efficiency and increases the distances over which neural models need to pass information. 

A simple method to manipulate the trade-off between vocabulary size and text size is to use shortlists of unsegmented words, using subword units only for rare words. As an alternative, we propose a segmentation algorithm based on byte pair encoding (BPE), which lets us learn a vocabulary that provides a good compression rate of the text.

---

[referencia=a2690ed31e8cc7e9 score=0.001]
## **6 Conclusion** 

The main contribution of this paper is that we show that neural machine translation systems are capable of open-vocabulary translation by representing rare and unseen words as a sequence of subword units.<sup>14</sup> This is both simpler and more effective than using a back-off translation model. We introduce a variant of byte pair encoding for word segmentation, which is capable of encoding open vocabularies with a compact symbol vocabulary of variable-length subword units. We show performance gains over the baseline with both BPE segmentation, and a simple character bigram segmentation. 

Our analysis shows that not only out-ofvocabulary words, but also rare in-vocabulary words are translated poorly by our baseline NMT 



> 14The source code of the segmentation algorithms is available at `https://github.com/rsennrich/ subword-nmt` . 

system, and that reducing the vocabulary size of subword models can actually improve performance. In this work, our choice of vocabulary size is somewhat arbitrary, and mainly motivated by comparison to prior work. One avenue of future research is to learn the optimal vocabulary size for a translation task, which we expect to depend on the language pair and amount of training data, automatically. We also believe there is further potential in bilingually informed segmentation algorithms to create more alignable subword units, although the segmentation algorithm cannot rely on the target text at runtime. 

While the relative effectiveness will depend on language-specific factors such as vocabulary size, we believe that subword segmentations are suitable for most language pairs, eliminating the need for large NMT vocabularies or back-off models. 

## **Acknowledgments** 

We thank Maja Popovi´c for her implementation of CHRF, with which we verified our reimplementation. The research presented in this publication was conducted in cooperation with Samsung Electronics Polska sp. z o.o. - Samsung R&D Institute Poland. This project received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement 645452 (QT21).

---

[referencia=a2690ed31e8cc7e9 score=0.001]
systems can productively form new words such as compounds. 

For the 50 000 most frequent words, the representation is the same for all neural networks, and all neural networks achieve comparable unigram F1 for this category. For the interval between frequency rank 50 000 and 500 000, the comparison between C2-3/500k and C2-50k unveils an interesting difference. The two systems only differ in the size of the shortlist, with C2-3/500k representing words in this interval as single units, and C250k via subword units. We find that the performance of C2-3/500k degrades heavily up to frequency rank 500 000, at which point the model switches to a subword representation and performance recovers. The performance of C2-50k remains more stable. We attribute this to the fact that subword units are less sparse than words. In our training set, the frequency rank 50 000 corresponds to a frequency of 60 in the training data; the frequency rank 500 000 to a frequency of 2. Because subword representations are less sparse, reducing the size of the network vocabulary, and representing more words via subword units, can lead to better performance. 

The F1 numbers hide some qualitative differences between systems. For English→German, WDict produces few OOVs (26.5% recall), but with high precision (60.6%) , whereas the subword systems achieve higher recall, but lower precision. We note that the character bigram model C2-50k produces the most OOV words, and achieves relatively low precision of 29.1% for this category. However, it outperforms the back-off dictionary in recall (33.0%). BPE-60k, which suffers from transliteration (or copy) errors due to segmentation inconsistencies, obtains a slightly better precision (32.4%), but a worse recall (26.6%). In contrast to BPE-60k, the joint BPE encoding of BPEJ90k improves both precision (38.6%) and recall (29.8%).

---

[referencia=a2690ed31e8cc7e9 score=0.001]
- Chris Dyer, Victor Chahuneau, and Noah A. Smith. 2013. A Simple, Fast, and Effective Reparameterization of IBM Model 2. In _Proceedings of the 2013 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , pages 644–648, Atlanta, Georgia. Association for Computational Linguistics. 

- Philip Gage. 1994. A New Algorithm for Data Compression. _C Users J._ , 12(2):23–38, February. 

- Barry Haddow, Matthias Huck, Alexandra Birch, Nikolay Bogoychev, and Philipp Koehn. 2015. The Edinburgh/JHU Phrase-based Machine Translation Systems for WMT 2015. In _Proceedings of the Tenth Workshop on Statistical Machine Translation_ , pages 126–133, Lisbon, Portugal. Association for Computational Linguistics. 

- Sébastien Jean, Kyunghyun Cho, Roland Memisevic, and Yoshua Bengio. 2015. On Using Very Large Target Vocabulary for Neural Machine Translation. In _Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)_ , pages 1–10, Beijing, China. Association for Computational Linguistics. 

- Nal Kalchbrenner and Phil Blunsom. 2013. Recurrent Continuous Translation Models. In _Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing_ , Seattle. Association for Computational Linguistics. 

- Yoon Kim, Yacine Jernite, David Sontag, and Alexander M. Rush. 2015. Character-Aware Neural Language Models. _CoRR_ , abs/1508.06615. 

Philipp Koehn and Kevin Knight. 2003. Empirical Methods for Compound Splitting. In _EACL ’03: Proceedings of the Tenth Conference on European Chapter of the Association for Computational Linguistics_ , pages 187–193, Budapest, Hungary. Association for Computational Linguistics.

---

[referencia=a2690ed31e8cc7e9 score=0.001]
<!-- Start of picture text -->
Graham Neubig, Taro Watanabe, Shinsuke Mori, and Jörg Tiedemann. 2012. Character-Based Pivot Trans-<br>Tatsuya Kawahara. 2012. Machine Translation lation for Under-Resourced Languages and Do-<br>without Words through Substring Alignment. In  The mains. In  Proceedings of the 13th Conference of the<br>50th Annual Meeting of the Association for Compu- European Chapter of the Association for Computa-<br>tational Linguistics, Proceedings of the Conference, tional Linguistics , pages 141–151, Avignon, France.<br>July 8-14, 2012, Jeju Island, Korea - Volume 1: Long Association for Computational Linguistics.<br>Papers , pages 165–174.<br>David Vilar, Jan-Thorsten Peter, and Hermann Ney.<br>Sonja Nießen and Hermann Ney. 2000. Improving 2007. Can We Translate Letters? In  Second Work-<br>SMT quality with morpho-syntactic analysis. In shop on Statistical Machine Translation , pages 33–<br>18th Int. Conf. on Computational Linguistics , pages 39, Prague, Czech Republic. Association for Com-<br>1081–1085. putational Linguistics.<br>Razvan Pascanu, Tomas Mikolov, and Yoshua Ben- Sami Virpioja, Jaakko J. Väyrynen, Mathias Creutz,<br>gio. 2013. On the difficulty of training recurrent and Markus Sadeniemi. 2007. Morphology-Aware<br>neural networks. In Proceedings of the 30th Inter- Statistical Machine Translation Based on Morphs<br>national Conference on Machine Learning, ICML Induced in an Unsupervised Manner. In Proceed-<br>2013 , pages 1310–1318, Atlanta, USA. ings of the Machine Translation Summit XI , pages<br>491–498, Copenhagen, Denmark.<br><!-- End of picture text -->

---

[referencia=a2690ed31e8cc7e9 score=0.001]
- Thang Luong, Ilya Sutskever, Quoc Le, Oriol Vinyals, and Wojciech Zaremba. 2015b. Addressing the Rare Word Problem in Neural Machine Translation. In _Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)_ , pages 11–19, Beijing, China. Association for Computational Linguistics. 

- Tomas Mikolov, Ilya Sutskever, Anoop Deoras, HaiSon Le, Stefan Kombrink, and Jan Cernocký. 2012. Subword Language Modeling with Neural Networks. Unpublished. 



<!-- Start of picture text -->