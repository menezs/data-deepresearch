[referencia=21b8c0494c3c6e8c score=0.787]
## **4 Experiments** 

We evaluated our Infini-Transformer models on benchmarks involving extremely long input sequences: long-context language modeling, 1M length passkey context block retrieval and 500K length book summarization tasks. For the language modeling benchmark, we train our models from scratch while for the passkey and book summarization tasks, we continually pre-train existing LLMs in order to highlight a plug-and-play long-context adaptation capability of our approach.

---

[referencia=21b8c0494c3c6e8c score=0.473]
7 

Preprint. Under review. 

|Model|Rouge-1|Rouge-2|Rouge-L|Overall|
|---|---|---|---|---|
|BART<br>|36.4|7.6|15.3|16.2|
|BART + Unlimiformer|36.8|8.3|15.7|16.9|
|PRIMERA<br>|38.6|7.2|15.6|16.3|
|PRIMERA + Unlimiformer<br>|37.9|8.2|16.3|17.2|
|Infni-Transformers(Linear)<br>|37.9|8.7|17.6|18.0|
|Infni-Transformers(Linear + Delta)|**40.0**|**8.8**|**17.9**|**18.5**|



Table 4: 500K length book summarization (BookSum) results. The BART, PRIMERA and Unlimiformer results are from Bertsch et al. (2024). 

observed an interleaving of long and short-term content retrievals throughout the forward computation.

---

[referencia=21b8c0494c3c6e8c score=0.100]
<!-- Start of picture text -->
20<br>19<br>18<br>17<br>16K 32K 64K 128K 256K 500K<br>Input length<br>Rouge overall score<br><!-- End of picture text -->

Figure 4: Infini-Transformers obtain better Rouge overall scores with more book text provided as input. 

We set the input length to 32K for fine-tuning and increase to 500K for evaluating. We use a generation temperature of 0.5 and _topp_ = 0.95 and set the number of decoding steps to 1024 to generate a summary of each book. 

Table 4 compares our model against the encoder-decoder models that were built particularly for the summarization task (Lewis et al., 2019; Xiao et al., 2021) and their retrieval-based long-context extension (Bertsch et al., 2024). Our model outperforms the previous best 

8 

Preprint. Under review. 

results and achieves a new SOTA on BookSum by processing the entire text from book. We have also plotted the overall Rouge score on validation split of BookSum data in Figure 4. There is a clear trend showing that with more text provided as input from books, Our Infini-Transformers improves its summarization performance metric.

---

[referencia=21b8c0494c3c6e8c score=0.098]
### 4.3 LLM Continual Pre-training 

We performed a lightweight continual pre-training for long-context adaptation of existing LLMs. The pre-training data includes the PG19 and Arxiv-math corpus as well as C4 text (Raffel et al., 2020) with length more than 4K tokens. The segment length _N_ was set to 2K throughout our experiments. 

**1M passkey retrieval benchmark.** We replaced the vanilla MHA in a 1B LLM with Infiniattention and continued to pre-train on inputs with length of 4K. The model was trained for 30K steps with batch size of 64 before fine-tuning on the passkey retrieval task (Mohtashami & Jaggi, 2024). 

The passkey task hides a random number into a long text and asks it back at the model output. The length of the distraction text is varied by repeating a text chunk multiple times. The previous work (Chen et al., 2023a) showed that a 8B LLaMA model can solve the task up to 32K length when fine-tuned with the same 32K length inputs with Position Interpolation. We take this challenge further and fine-tune on only 5K length inputs to test on 1M length regime. 

Table 3 reports the token-level accuracy for test subsets with input lengths ranging from 32K to 1M. For each test subset, we controlled the position of the passkey so that it is either located around the beginning, middle or the end of the input sequence. We reported both zero-shot accuracy and finetuning accuracy. Infini-Transformers solved the task with up to 1M context length after fine-tuning on 5K length inputs for 400 steps. 

**500K length book summarization (BookSum).** We further scaled our approach by continuously pre-training a 8B LLM model with 8K input length for 30K steps. We then fine-tuned on a book summarization task, BookSum (Krysci´ nski et al., 2021) where the´ goal is to generate a summary of an entire book text. 



<!-- Start of picture text -->

---

[referencia=21b8c0494c3c6e8c score=0.060]
Pentti Kanerva. _Sparse distributed memory_ . MIT press, 1988. 

- Angelos Katharopoulos, Apoorv Vyas, Nikolaos Pappas, and Franc¸ois Fleuret. Transformers are rnns: Fast autoregressive transformers with linear attention. In _International conference on machine learning_ , pp. 5156–5165. PMLR, 2020. 

- Amirhossein Kazemnejad, Inkit Padhi, Karthikeyan Natesan Ramamurthy, Payel Das, and Siva Reddy. The impact of positional encoding on length generalization in transformers. _Advances in Neural Information Processing Systems_ , 36, 2024. 

- Wojciech Krysci´ nski, Nazneen Rajani, Divyansh Agarwal, Caiming Xiong, and Dragomir´ Radev. Booksum: A collection of datasets for long-form narrative summarization. _arXiv preprint arXiv:2105.08209_ , 2021. 

11 

Preprint. Under review.

---

[referencia=21b8c0494c3c6e8c score=0.055]
- Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever. Generating long sequences with sparse transformers. _arXiv preprint arXiv:1904.10509_ , 2019. 

- Djork-Arne´ Clevert, Thomas Unterthiner, and Sepp Hochreiter. Fast and accurate deep network learning by exponential linear units (elus). _arXiv preprint arXiv:1511.07289_ , 2015. 

- Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V Le, and Ruslan Salakhutdinov. Transformer-xl: Attentive language models beyond a fixed-length context. _arXiv preprint arXiv:1901.02860_ , 2019. 

- Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra, and Christopher Re.´ Flashattention: Fast and memory-efficient exact attention with io-awareness. _Advances in Neural Information Processing Systems_ , 35:16344–16359, 2022. 

- Jiayu Ding, Shuming Ma, Li Dong, Xingxing Zhang, Shaohan Huang, Wenhui Wang, Nanning Zheng, and Furu Wei. Longnet: Scaling transformers to 1,000,000,000 tokens. _arXiv preprint arXiv:2307.02486_ , 2023. 

- Yao Fu, Rameswar Panda, Xinyao Niu, Xiang Yue, Hannaneh Hajishirzi, Yoon Kim, and Hao Peng. Data engineering for scaling language models to 128k context. _arXiv preprint arXiv:2402.10171_ , 2024. 

- Tao Ge, Jing Hu, Xun Wang, Si-Qing Chen, and Furu Wei. In-context autoencoder for context compression in a large language model. _arXiv preprint arXiv:2307.06945_ , 2023. 

- Alex Graves, Greg Wayne, and Ivo Danihelka. Neural turing machines. _arXiv preprint arXiv:1410.5401_ , 2014.

---

[referencia=21b8c0494c3c6e8c score=0.042]
# **Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention** 

**Tsendsuren Munkhdalai, Manaal Faruqui and Siddharth Gopal** Google 

```
tsendsuren@google.com
```

## **Abstract** 

This work introduces an efficient method to scale Transformer-based Large Language Models (LLMs) to infinitely long inputs with bounded memory and computation. A key component in our proposed approach is a new attention technique dubbed Infini-attention. The Infini-attention incorporates a compressive memory into the vanilla attention mechanism and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. We demonstrate the effectiveness of our approach on long-context language modeling benchmarks, 1M sequence length passkey context block retrieval and 500K length book summarization tasks with 1B and 8B LLMs. Our approach introduces minimal bounded memory parameters and enables fast streaming inference for LLMs.

---

[referencia=21b8c0494c3c6e8c score=0.030]
**Efficient attention.** The efficient attention techniques attempt to improve the efficiency of the dot-product attention with an approximation or a system-level optimization. Multiple directions have been explored for different forms of efficient attention approximation, including sparsity-based (Child et al., 2019; Beltagy et al., 2020; Sukhbaatar et al., 2021; Ding et al., 2023; Xiao et al., 2024) and linear attention approximation (Shen et al., 2018; Katharopoulos et al., 2020; Schlag et al., 2021). Among those, the linear attention variants are closely related to the associative memory matrix (Schlag et al., 2020; 2021) and the metalearned neural memory (Munkhdalai et al., 2019), where KV bindings (Smolensky, 1990) are stored in Fast-Weights (Hinton & Plaut, 1987; Schmidhuber, 1992; Ba et al., 2016) that are modified in with respect to new contextual information. More recently, system-level optimization techniques have been proposed by leveraging specific hardware architecture to make the exact attention computation more efficient (Dao et al., 2022; Liu et al., 2023). 

9 

Preprint. Under review. 

## **6 Conclusion** 

An effective memory system is crucial not just for comprehending long contexts with LLMs, but also for reasoning, planning, continual adaptation for fresh knowledge, and even for learning how to learn. This work introduces a close integration of compressive memory module into the vanilla dot-product attention layer. This subtle but critical modification to the attention layer enables LLMs to process infinitely long contexts with bounded memory and computation resources. We show that our approach can naturally scale to a million length regime of input sequences, while outperforming the baselines on long-context language modeling benchmark and book summarization tasks. We also demonstrate a promising length generalization capability of our approach. 1B model that was fine-tuned on up to 5K sequence length passkey instances solved the 1M length problem. 

### Acknowledgments 

We would like to thank Dongseong Hwang for their help implementing efficient sequence unrolling mechanism with the jax scan function. We would also like to thank Aditya Gupta, Kalpesh Krishna, Tu Vu and Alexandra Chronopoulou for their feedback.

---

[referencia=21b8c0494c3c6e8c score=0.019]
## **1 Introduction** 

Memory serves as a cornerstone of intelligence, as it enables efficient computations tailored to specific contexts. However, Transformers (Vaswani et al., 2017) and Transformer-based LLMs (Brown et al., 2020; Touvron et al., 2023; Anil et al., 2023; Groeneveld et al., 2024) have a constrained context-dependent memory, due to the nature of the attention mechanism. The attention mechanism in Transformers exhibits quadratic complexity in both memory footprint and computation time. For example, the attention Key-Value (KV) states have 3TB projectionLinear Linear memory footprint for a 500B model with batch size 512 and context length 2048 (Pope et al., 2023). Indeed, scaling LLMs to longer sequences (i.e. 1M tokens) is challenging with the standard Concat Concat Transformerand longer context models becomes costly finan-architectures and serving longer Retrieve cially. Compressive memory & Linear attentionLinear attention Causal scaled dot-product attention & PEattention & PE 



<!-- Start of picture text -->
projectionLinear Linear<br>Concat Concat<br>Retrieve<br>Compressive memory & Linear attentionLinear attention Causal scaled dot-product attention & PEattention & PE<br>Update<br>{KV}Vs-1VVs-1Vs-1V QsQQ {KV}VsV<br><!-- End of picture text -->

Compressive memory systems promise to be Update more scalable and efficient than the attention V {KV}Vs-1VVs-1Vs-1V mechanism for extremely long sequences (Kanerva, 1988; Munkhdalai et al., 2019). Instead of using an array that grows with the input seFigure 1: quence length, a compressive memory primarily tional compressive maintains a fixed number of parameters to store attention for contexts. _{KV}sKV}s}ss−_ and recall information with a bounded storage and computation costs. In the compressive memory, new information is added to the memory by changing its parameters with an objective that this information can be recovered back later embeddings. on. However, the LLMs in their current state have yet to see an effective, practical compressive memory technique that balances simplicity along with quality.

---

[referencia=21b8c0494c3c6e8c score=0.014]
Figure 1: Infini-attention has an additional compressive memory with linear attention for processing infinitely long contexts. _{KV}sKV}s}ss−_ 1 and _{KV}s_ are attention key and values for current and previous input segments, respectively and _Qs_ the attention queries. PE denotes position embeddings. 

1 

Preprint. Under review. 

In this work, we introduce a novel approach that enables Transformer LLMs to effectively process infinitely long inputs with bounded memory footprint and computation. A key component in our proposed approach is a new attention technique dubbed Infini-attention (Figure 1). The Infini-attention incorporates a compressive memory into the vanilla attention mechanism (Bahdanau et al., 2014; Vaswani et al., 2017) and builds in both masked local attention and long-term linear attention mechanisms in a single Transformer block. 

Such a subtle but critical modification to the Transformer attention layer enables a natural extension of existing LLMs to infinitely long contexts via continual pre-training and finetuning. 

Our Infini-attention reuses all the key, value and query states of the standard attention computation for long-term memory consolidation and retrieval. We store old KV states of the attention in the compressive memory, instead of discarding them like in the standard attention mechanism. We then retrieve the values from the memory by using the attention query states when processing subsequent sequences. To compute the final contextual output, the Infini-attention aggregates the long-term memory-retrieved values and the local attention contexts. 

In our experiments, we show that our approach outperforms baseline models on longcontext language modeling benchmarks while having 114x comprehension ratio in terms of memory size. The model achieves even better perplexity when trained with 100K sequence length. A 1B LLM naturally scales to 1M sequence length and solves the passkey retrieval task when injected with Infini-attention. Finally, we show that a 8B model with Infiniattention reaches a new SOTA result on a 500K length book summarization task after continual pre-training and task fine-tuning. 

In summary, our work makes the following contributions:

---

[referencia=21b8c0494c3c6e8c score=0.013]
- Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. _Advances in neural information processing systems_ , 30, 2017. 

- Paul J Werbos. Generalization of backpropagation with application to a recurrent gas market model. _Neural networks_ , 1(4):339–356, 1988. 

- Yuhuai Wu, Markus N Rabe, DeLesley Hutchins, and Christian Szegedy. Memorizing transformers. _arXiv preprint arXiv:2203.08913_ , 2022. 

- Chaojun Xiao, Pengle Zhang, Xu Han, Guangxuan Xiao, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Song Han, and Maosong Sun. Inf m: Unveiling the intrinsic capacity of llms for understanding extremely long sequences with training-free memory. _arXiv preprint arXiv:2402.04617_ , 2024. 

- Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. Efficient streaming language models with attention sinks. _arXiv preprint arXiv:2309.17453_ , 2023. 

- Wen Xiao, Iz Beltagy, Giuseppe Carenini, and Arman Cohan. Primera: Pyramidbased masked sentence pre-training for multi-document summarization. _arXiv preprint arXiv:2110.08499_ , 2021. 

- Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, et al. Effective long-context scaling of foundation models. _arXiv preprint arXiv:2309.16039_ , 2023.

---

[referencia=21b8c0494c3c6e8c score=0.011]
- Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Ves Stoyanov, and Luke Zettlemoyer. Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. _arXiv preprint arXiv:1910.13461_ , 2019. 

- Hao Liu, Matei Zaharia, and Pieter Abbeel. Ring attention with blockwise transformers for near-infinite context. _arXiv preprint arXiv:2310.01889_ , 2023. 

- Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. Lost in the middle: How language models use long contexts. _Transactions of the Association for Computational Linguistics_ , 12:157–173, 2024. 

- Wolfgang Maass, Thomas Natschlager, and Henry Markram.¨ Real-time computing without stable states: A new framework for neural computation based on perturbations. _Neural computation_ , 14(11):2531–2560, 2002. 

- Thomas Miconi, Kenneth Stanley, and Jeff Clune. Differentiable plasticity: training plastic neural networks with backpropagation. In _International Conference on Machine Learning_ , pp. 3559–3568. PMLR, 2018. 

- Amirkeivan Mohtashami and Martin Jaggi. Random-access infinite context length for transformers. _Advances in Neural Information Processing Systems_ , 36, 2024. 

- Jesse Mu, Xiang Li, and Noah Goodman. Learning to compress prompts with gist tokens. _Advances in Neural Information Processing Systems_ , 36, 2024. 

- Tsendsuren Munkhdalai and Hong Yu. Meta networks. In _International conference on machine learning_ , pp. 2554–2563. PMLR, 2017a. 

- Tsendsuren Munkhdalai and Hong Yu. Neural semantic encoders. In _Proceedings of the conference. Association for Computational Linguistics. Meeting_ , volume 1, pp. 397. NIH Public Access, 2017b.

---

[referencia=21b8c0494c3c6e8c score=0.006]
**Gating score visualization.** Figure 3 visualizes the gating score, _sigmoid_ ( _β_ ) for the compressive memory for all attention heads in each layer. There are two types of heads emerged in Infini-attention after training: specialized heads with a gating score near 0 or 1 and mixer heads with a score close to 0.5. The specialized heads either process contextual information via the local attention computation or retrieve from the compressive memory whereas the mixer heads aggregate both current contextual information and long-term memory content together into a single output. Interestingly, each layer has at least a single short-range head, allowing a forward-propagation of input signal up until the output layer. We also 

||||Zero-shot|||
|---|---|---|---|---|---|
||32K|128K|256K|512K|1M|
|Infni-Transformer(Linear)|14/13/98|11/14/100|6/3/100|6/7/99|8/6/98|
|Infni-Transformer(Linear + Delta)|13/11/99|6/9/99|7/5/99|6/8/97|7/6/97|
||||FT (400 steps)|||
|Infni-Transformer(Linear)|100/100/100|100/100/100|100/100/100|97/99/100|96/94/100|
|Infni-Transformer(Linear + Delta)|100/100/100|100/100/99|100/100/99|100/100/100|100/100/100|



Table 3: Infini-Transformers solved the passkey task with up to 1M context length when fine-tuned on 5K length inputs. We report token-level retrieval accuracy for passkeys hidden in a different part ( _start/middle/end_ ) of long inputs with lengths 32K to 1M. 

7 

Preprint. Under review.

---

[referencia=21b8c0494c3c6e8c score=0.003]
## **3 Method** 

Figure 2 compares our model, Infini-Transformer, and Transformer-XL (Dai et al., 2019). Similar to Transformer-XL, Infini-Transformer operates on a sequence of segments. We compute the standard causal dot-product attention context within each segment. So the dot-product attention computation is local in a sense that it covers a total _N_ number of tokens of the current segment with index _S_ ( _N_ is the segment length). 

The local attention (Dai et al., 2019), however, discards the attention states of the previous segment when processing the next one. In Infini-Transformers, instead of leaving out the old KV attention states, we propose to reuse them to maintain the entire context history with a compressive memory. So each attention layer of Infini-Transformers has both global compressive and local fine-grained states. We call such an efficient attention mechanism Infini-attention, which is illustrated in Figure 1 and described formally in the following sections. 

3.1 Infini-attention 

As shown Figure 1, our Infini-attention is a recurrent attention mechanism that computes both local and global context states and combine them for its output. Similar to multi-head 

3 

Preprint. Under review. 

attention (MHA), it maintains _H_ number of parallel compressive memory per attention layer ( _H_ is the number of attention heads) in addition to the dot-product attention and like the RNNs and MNM, it maintains a recurrent memory state to efficiently track the long sequence context:

---

[referencia=21b8c0494c3c6e8c score=0.002]
## **2 Background** 

Recurrent Neural Networks (RNNs) process a single token _xt_ at each step _t_ and computes a recurrent hidden state _ht_ to represent an entire input sequence (Hochreiter & Schmidhuber, 1997; Maass et al., 2002): 

_ht_ = _RNN_ ( _xt_ , _ht−_ 1). (1) 

The RNN computation is very efficient since the model maintains only a fixed-size vector _ht_ for input sequence. However, for processing long sequences it becomes difficult to store entire contextual information into a single fixed-size vector and this limitation had implications on RNNs utility in certain tasks (Kaiser & Sutskever, 2015). To address the limitation, people extended the standard RNNs with an external memory component that can be read from and written to. One such an instance is Metalearned Neural Memory (MNM) (Munkhdalai et al., 2019): 



MNM learns an additional memory state _θ_ parameterized by a feed-forward neural network (FFN) and uses query, key and value vectors (QKV) to interact with the memory, similar to the attention mechanism. To store information, it modifies the parameters of the FFN by using the key vectors as input and the value vectors for the target, and to read memory 

2 

Preprint. Under review. 



<!-- Start of picture text -->
Infini-Transformer<br>Transformer block:<br>Segment 1 Segment 2 Segment 3 Compressive memory:<br>Memory update:<br>Transformer-XL<br>Memory retrieval:<br>Effective context:<br>Input segment: Segment 1<br>Segment 1 Segment 2 Segment 3<br><!-- End of picture text -->

Figure 2: Infini-Transformer (top) has an entire context history whereas Transformer-XL (bottom) discards old contexts since it caches the KV states for the last segment only. 

entries, it forward-passes the query vectors through the memory FFN and retrieves its corresponding value. Like RNNs, the memory state is still bounded in MNM. 

Unlike the RNNs, the attention mechanism however doesn’t maintain a recurrent state and only performs a feed-forward computation on input sequence segment _Xs_ :

---

[referencia=21b8c0494c3c6e8c score=0.002]
- Tsendsuren Munkhdalai, John P Lalor, and Hong Yu. Citation analysis with neural attention models. In _Proceedings of the Seventh International Workshop on Health Text Mining and Information Analysis_ , pp. 69–77, 2016. 

- Tsendsuren Munkhdalai, Alessandro Sordoni, Tong Wang, and Adam Trischler. Metalearned neural memory. _Advances in Neural Information Processing Systems_ , 32, 2019. 

- Bowen Peng, Jeffrey Quesnelle, Honglu Fan, and Enrico Shippole. Yarn: Efficient context window extension of large language models. _arXiv preprint arXiv:2309.00071_ , 2023. 

- Reiner Pope, Sholto Douglas, Aakanksha Chowdhery, Jacob Devlin, James Bradbury, Jonathan Heek, Kefan Xiao, Shivani Agrawal, and Jeff Dean. Efficiently scaling transformer inference. _Proceedings of Machine Learning and Systems_ , 5, 2023. 

- Ofir Press, Noah A Smith, and Mike Lewis. Train short, test long: Attention with linear biases enables input length extrapolation. _arXiv preprint arXiv:2108.12409_ , 2021. 

- Jack W Rae, Anna Potapenko, Siddhant M Jayakumar, and Timothy P Lillicrap. Compressive transformers for long-range sequence modelling. _arXiv preprint arXiv:1911.05507_ , 2019. 

- Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. _The Journal of Machine Learning Research_ , 21(1):5485–5551, 2020. 

- Nir Ratner, Yoav Levine, Yonatan Belinkov, Ori Ram, Omri Abend, Ehud Karpas, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. Parallel context windows improve in-context learning of large language models. _arXiv preprint arXiv:2212.10947_ , 2022.

---

[referencia=21b8c0494c3c6e8c score=0.002]
### 4.1 Implementation details 

**Segment chunking.** we forward-pass the entire input text a Transformer model and then perform segment chunking at each Infini-attention layer - in this way, perform a minimal modification to the existing Transformer implementation. The Infini-attention layer segments the input and process it segment by segment and concatenates back the segments to pass the original-length segment as output to the next layer. 

**Back-propagation through time (BPTT).** Each Infini-attention layer is trained with backpropagation through time (Werbos, 1988) by computing the gradient w.r.t the compressive memory states, similar to how RNNs are trained. To save memory, we perform gradient checkpoint when processing the sequence segment by segment. 

6 

Preprint. Under review. 

|Model|Memorysize(comp.)|XL cache|Segment length|PG19|Arxiv-math|
|---|---|---|---|---|---|
|Transformer-XL|50M (3.7x)|2048|2048|11.88|2.42|
|Memorizing Transformers|183M (1x)|2048|2048|11.37|2.26|
|RMT|2.5M(73x)|None|2048|13.27|2.55|
|Infni-Transformer(Linear)|1.6M (114x)|None|2048|**9.65**|2.24|
|Infni-Transformer(Linear + Delta)|1.6M (114x)|None|2048|9.67|**2.23**|



Table 2: Long-context language modeling results are compared in terms of average tokenlevel perplexity. Comp. denotes compression ratio. Infini-Transformer outperforms memorizing transformers with memory length of 65K and achieves 114x compression ratio. 

**Position Embeddings (PE).** As shown Figure 1, we don’t use position embeddings for the key and query vectors of the compressive memory to store only global contextual information in the long-term memory. The PEs were applied to the QK vectors only after the compressive memory reading and update.

---

[referencia=21b8c0494c3c6e8c score=0.002]
## **References** 

Rohan Anil, Andrew M Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin, Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen, et al. Palm 2 technical report. _arXiv preprint arXiv:2305.10403_ , 2023.

---

[referencia=21b8c0494c3c6e8c score=0.001]
- Jimmy Ba, Geoffrey E Hinton, Volodymyr Mnih, Joel Z Leibo, and Catalin Ionescu. Using fast weights to attend to the recent past. _Advances in neural information processing systems_ , 29, 2016. 

- Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by jointly learning to align and translate. _arXiv preprint arXiv:1409.0473_ , 2014. 

- Iz Beltagy, Matthew E Peters, and Arman Cohan. Longformer: The long-document transformer. _arXiv preprint arXiv:2004.05150_ , 2020. 

- Amanda Bertsch, Uri Alon, Graham Neubig, and Matthew Gormley. Unlimiformer: Longrange transformers with unlimited length input. _Advances in Neural Information Processing Systems_ , 36, 2024. 

- Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. _Advances in neural information processing systems_ , 33:1877–1901, 2020. 

- Aydar Bulatov, Yury Kuratov, and Mikhail Burtsev. Recurrent memory transformer. _Advances in Neural Information Processing Systems_ , 35:11079–11091, 2022. 

- Shouyuan Chen, Sherman Wong, Liangjian Chen, and Yuandong Tian. Extending context window of large language models via positional interpolation. _arXiv preprint arXiv:2306.15595_ , 2023a. 

- Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai, Zhijian Liu, Song Han, and Jiaya Jia. Longlora: Efficient fine-tuning of long-context large language models. _arXiv preprint arXiv:2309.12307_ , 2023b.

---

[referencia=21b8c0494c3c6e8c score=0.001]
## **5 Related Work** 

**Compressive memory.** Inspired by the plasticity in biological neurons (Munkhdalai & Yu, 2017a; Miconi et al., 2018), compressive memory approaches cast parameterized functions as memory to store and retrieve information (Hinton & Plaut, 1987; Schmidhuber, 1992; Ba et al., 2016; Munkhdalai et al., 2019). Unlike the Transformer KV memory array (Vaswani et al., 2017; Wu et al., 2022), which grows with input sequence length, compressive memory systems maintain a constant number of memory parameters for computational efficiency. The parameters are modified with an update rule to store information, which is then retrieved via a memory reading mechanism (Graves et al., 2014; Sukhbaatar et al., 2015; Munkhdalai & Yu, 2017b). 

Compressed input representations can be viewed as a summary of past sequence segments (Rae et al., 2019; Chevalier et al., 2023). Along this direction, more recent works have been utilizing a Transformer LLM itself to compress input sequence for efficient longcontext modeling (Bulatov et al., 2022; Chevalier et al., 2023; Ge et al., 2023; Mu et al., 2024; Hwang et al., 2024). However, the previous segment-level compression methods, including Compressive Transformers (Rae et al., 2019) still discard the memory entries of old segments in order to free up space for the new ones, limiting their context window to the most recent segments. This is in contrast to our Infini-attention that computes incremental memory updates to a fixed amount of memory parameters in a recurrent fashion.