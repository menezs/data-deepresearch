[referencia=d9c08b4d6cd4e69f score=0.988]
## 7. Stage 5 — Residual connection and normalization (Add & Norm)

**Why this stage is necessary.** Stacking many layers requires both the signal and the training gradient to pass through many transformations. Without a shortcut, deeper networks may perform worse during training, a degradation problem mitigated by residual connections (He et al., 2016). The residual path also preserves the original information and lets each sublayer learn only a correction. Normalization keeps value scales stable with depth (Ba et al., 2016), while its position (Pre-LN or Post-LN) affects training stability when careful warm-up is absent (Xiong et al., 2020). Without these mechanisms, the depth that gives the model capacity could not be trained reliably.

**Residual connection.** After each sublayer (attention or FFN), the sublayer input is added to its output: y = x + Sublayer(x). The idea comes from residual networks in computer vision (He et al., 2016). It creates a direct path for the signal and gradient, enabling deep stacks to be trained, and causes each sublayer to learn a **correction** to what already exists rather than reconstructing everything. In circuit interpretations, this path is the **residual stream**, a channel that every layer reads from and writes to (Elhage et al., 2021).

**Normalization.** Without scale control, values may grow or shrink across layers and destabilize training. **LayerNorm** normalizes each token separately across its d_model components, not across the batch, and then applies a learned scale γ and shift β (Ba et al., 2016):

**RMSNorm** omits mean subtraction and normalizes only by the root mean square, at lower cost and with comparable performance (Zhang and Sennrich, 2019); it is used in models such as LLaMA (Touvron et al., 2023).

**Post-LN and Pre-LN.** The original Transformer applies normalization after the residual addition (**Post-LN**). Many current models apply it before each sublayer (**Pre-LN**), a variant that trains more stably and reduces dependence on careful learning-rate warm-up (Xiong et al., 2020).

---

[referencia=d9c08b4d6cd4e69f score=0.380]
**Numerical parameter example (base Transformer).** W1 contains 512 × 2048 = 1,048,576 weights and W2 contains 2048 × 512 = 1,048,576, totaling 2,097,152 per layer without biases. Adding the 1,048,576 attention weights (Section 6), the layer contains approximately 3.15 million weights, roughly two-thirds of which belong to the FFN.

**Numerical computation example (d_model = 4, d_ff = 8; W1 and W2 generated randomly with a fixed seed and no training).** For the token *estava* at position 2, the FFN input is the normalized vector [1.389; −0.901; −0.999; 0.511]. After W1 and ReLU, the hidden layer is [0.907; 0.660; 0.330; 0; 0.623; 0; 1.541; 0.759]: six of the eight units are active and two are zeroed by ReLU. After W2, the output is [0.231; 0.954; 0.437; −0.291]. Adding it to the input through the residual path and normalizing yields [1.613; −0.351; −1.121; −0.141]. For *banco* at position 1, all eight hidden units are zero in this example, so the FFN output is zero and the vector crosses the sublayer unchanged through the residual path. In a trained model, the sparse activation pattern is learned, and each token activates a different subset of units.

---

[referencia=d9c08b4d6cd4e69f score=0.153]
**Numerical example.** In the output computed in Section 11 using random weights, the probability assigned to *lotado* is p = 0.022 and the probability assigned to *cheio* is 0.623. If the correct token were *lotado*, the loss would be −ln(0.022) = 3.806; if it were *cheio*, the loss would be −ln(0.623) = 0.473. The loss gradient with respect to the logits is simply p − y, where y is the one-hot vector for the correct token. For target *lotado*, the gradient is [−0.978; 0.114; 0.623; 0.094; 0.147], meaning that training pushes the *lotado* logit upward and the others downward in proportion to the error.

**Backpropagation and optimization.** The gradient is propagated backward through all layers by the chain rule, an algorithm known as **backpropagation** (Rumelhart et al., 1986), and an optimizer updates the weights. The original Transformer used **Adam** (Kingma and Ba, 2015) with a learning rate that grows linearly during warm-up and then decays, together with dropout and label smoothing (Vaswani et al., 2017). **AdamW**, which decouples weight-decay regularization from the adaptive update, is a common choice in current models (Loshchilov and Hutter, 2019).

**Parallelism in training and sequence in inference.** During training with a causal mask, all positions are computed at once because the correct text is already known. During inference, token t + 1 depends on the selected token t, so generation is sequential, and the KV cache (Section 6) prevents recomputation of the past.

**Training phases.** A common practice is **pretraining** on a large volume of raw text, followed by adaptation for specific use through supervised fine-tuning and alignment with human preferences, such as reinforcement learning from human feedback (Ouyang et al., 2022).

---

[referencia=d9c08b4d6cd4e69f score=0.100]
**Numerical example (token *banco*, causal version, γ = 1, β = 0).** The attention output projected by Wo is o = [1.074; 1.912; 0.537; 0.956]. The input was x = [0.841; 1.540; 0.510; 1.000]. Residual addition gives r = x + o = [1.915; 3.453; 1.047; 1.956]. The mean is μ = 2.093 and the variance is σ² = 0.748. LayerNorm with ε = 10⁻⁵ gives [(1.915 − 2.093)/0.865; …] = [−0.205; 1.572; −1.209; −0.158], with mean 0 and variance 1. By comparison, RMSNorm of the same vector, with root mean square 2.264, yields [0.846; 1.525; 0.462; 0.864]: it preserves the proportions among components without centering them at zero.

---

[referencia=d9c08b4d6cd4e69f score=0.093]
# FIG 1 flow
fig,ax=plt.subplots(figsize=(9,11)); ax.set_xlim(0,10); ax.set_ylim(0,14.2); ax.axis("off")
box(ax,2,12.9,6,0.9,"1. TEXTO DE ENTRADA\n\"O banco estava lotado\"",C["in"],bold=True)
box(ax,2,11.3,6,0.9,"2. TOKENIZAÇÃO (BPE / SentencePiece)\n[O] [banco] [estava] [lotado] → IDs inteiros",C["tok"],bold=True)
box(ax,2,9.8,6,0.9,"3. EMBEDDING + CODIFICAÇÃO POSICIONAL\nmatriz X ∈ ℝ^(n × d_model)",C["emb"],bold=True)
ax.add_patch(FancyBboxPatch((1.1,3.9),7.8,5.4,boxstyle="round,pad=0.02,rounding_size=0.1",fc="#fafafa",ec="#222",lw=1.6,ls="--"))
ax.text(5,8.95,"4. BLOCO TRANSFORMER  ×  N camadas (pesos próprios por camada)",ha="center",fontsize=9.5,fontweight="bold")
box(ax,2.3,7.65,5.6,0.8,"Self-Attention multi-cabeça\n(Q, K, V = X·Wq, X·Wk, X·Wv)",C["att"],fs=8.8)
box(ax,2.3,6.55,5.6,0.6,"Add & Norm (residual + normalização)",C["gray"],fs=8.8)
box(ax,2.3,5.3,5.6,0.8,"Rede Feed-Forward (FFN) por posição",C["ffn"],fs=8.8)
box(ax,2.3,4.2,5.6,0.6,"Add & Norm (residual + normalização)",C["gray"],fs=8.8)

---

[referencia=d9c08b4d6cd4e69f score=0.092]
## 10. Stage 8 — Weights: what they are and how they are learned

**Why this stage is necessary.** With random weights, the previous stages produce outputs unrelated to language, as in the numerical examples in this article. Training is what turns the architecture into a useful model. Next-token prediction is an effective objective because it provides a learning signal from any text without human labels. Backpropagation is necessary because millions to billions of parameters can only be adjusted using efficiently computed gradients (Rumelhart et al., 1986), while the optimizer, warm-up, and regularization stabilize those updates (Kingma and Ba, 2015; Loshchilov and Hutter, 2019; Vaswani et al., 2017). This stage also explains why inference uses fixed weights: what the model has learned is already encoded in them.

**What weights are.** **Weights**, or **parameters**, are the adjustable numbers in the model: the embedding matrix; Wq, Wk, Wv, Wo, W1, W2, biases, and the normalization parameters γ and β in each layer; and the final vocabulary projection. They remain fixed during **inference**. Everything the model has learned is encoded in these values.

**Training objective.** Generative models are trained to **predict the next token**. Given a sequence x₁…x_T, training minimizes the mean **cross-entropy** between the predicted distribution and the token that actually follows:

BERT uses a different objective, **masked language modeling**, in which some tokens are hidden and the model reconstructs them using context from both directions (Devlin et al., 2019). In both cases, there is no human label for meaning: the signal is the text itself. This supports the idea that disambiguation is an **emergent strategy for reducing prediction error** (Section 13).

---

[referencia=d9c08b4d6cd4e69f score=0.074]
## 3. Stage 1 — Input and tokenization

**Why this stage is necessary.** Computers apply arithmetic operations to numbers; without converting text into IDs, there is no input to the network. The vocabulary must be finite and fixed because the output layer has one dimension per token (Section 11). Subword tokenization addresses a real tradeoff: whole words leave new terms without a representation, whereas individual characters create long sequences and increase the cost of attention, which grows with the square of sequence length (Section 5; Sennrich et al., 2016).

**Concept.** Neural networks operate on numbers, not text. **Tokenization** converts a character string into a sequence of **tokens** (vocabulary units) and each token into an integer **ID**. The **vocabulary** is a finite set established before training, typically containing tens of thousands of entries.

**Why subwords.** Whole-word vocabularies do not represent rare or new words (the out-of-vocabulary, or OOV, problem), whereas character vocabularies produce overly long sequences. **Subword units** balance these extremes: frequent words become a single token, and rare words are decomposed into reusable pieces (Sennrich et al., 2016).

**Techniques discussed.**

- **BPE (Byte Pair Encoding):** starts from characters and iteratively merges the most frequent adjacent pair into a new symbol. It was proposed by Gage (1994) as a compression algorithm and adapted to machine translation by Sennrich et al. (2016). Byte-level variants are used in GPT-series models (Radford et al., 2019).
- **WordPiece:** selects merges by their increase in language-model likelihood rather than simple frequency (Schuster and Nakajima, 2012; Wu et al., 2016). It is used in BERT (Devlin et al., 2019).
- **Unigram LM and SentencePiece:** Unigram starts from a large vocabulary and prunes the entries that contribute least (Kudo, 2018). SentencePiece implements BPE and Unigram directly over raw text without whitespace pre-tokenization, making it language-independent (Kudo and Richardson, 2018).

---

[referencia=d9c08b4d6cd4e69f score=0.065]
## 9. Stage 7 — Multilayer stacking

**Why this stage is necessary.** One layer captures relationships in one step. Many tasks require composition: identify the token, relate it to context, infer its sense, and only then predict. Stacking enables successive refinement, and probing analyses reveal different levels of information across layers (Jawahar et al., 2019; Tenney et al., 2019; Belrose et al., 2023). Some documented mechanisms, such as induction heads, require at least two attention layers (Elhage et al., 2021; Olsson et al., 2022). More layers increase both capacity and cost, so depth is a design choice, as shown below.

**Mechanism.** A **Transformer block** follows the sequence attention → Add & Norm → FFN → Add & Norm. The model stacks N blocks: the output of layer l becomes the input to layer l + 1, and each layer has its **own weights**. The n × d_model matrix retains the same shape across the stack; what changes is the content of each vector as it is progressively refined.

**What different depths tend to represent.** Probing studies in BERT indicate an approximate progression: early layers capture surface and local-order patterns; intermediate layers capture syntactic structure; and higher layers capture semantic and long-range relationships (Jawahar et al., 2019). Tenney et al. (2019) observed that stages of the classical NLP pipeline — part-of-speech tagging, syntactic parsing, entities, semantic roles, and coreference — can be recovered in that order across the layers. Figure 5 summarizes this tendency.

**Iterative refinement of the prediction.** Techniques such as the *logit lens* and *tuned lens* project the intermediate state of each layer onto the vocabulary and show that the predicted next-token distribution becomes more precise layer by layer (Belrose et al., 2023).

**Circuits that require depth.** **Induction heads** are a documented example: one head in an earlier layer copies information from the previous token, and a later head uses it to locate past occurrences of a pattern and predict its continuation. This mechanism requires at least two attention layers and has been associated with the emergence of *in-context learning* during training (Elhage et al., 2021; Olsson et al., 2022).

---

[referencia=d9c08b4d6cd4e69f score=0.047]
## 14. Limitations, caveats, and open debates

**Purpose of this section.** It defines what the article does and does not demonstrate. This is necessary because the examples are simplified and because the mechanism itself has limitations and unresolved questions that readers should understand.

**Limitations of this article.**

- The numerical examples use very small dimensions, a single head, and hand-selected or random weights. They demonstrate the arithmetic, not the behavior of a trained model.
- For simplicity, the article omits biases in all projections, dropout, cross-attention in the decoder of the original model, and variants such as mixtures of experts and attention alternatives such as state-space models (Gu and Dao, 2023).
- Details such as the exact number of layers, activation function, normalization type, and positional encoding vary among models and are not always disclosed.

**Debates and limitations of the mechanism itself.**

- **Attention and explanation.** Attention weights are not, by themselves, a reliable explanation of model behavior (Jain and Wallace, 2019; Wiegreffe and Pinter, 2019).
- **Quadratic cost and long context.** Attention cost grows with the square of sequence length, and long-context models may use information located in the middle of the context less effectively (Liu et al., 2024).
- **Hallucination.** The model computes likely tokens given the context; the architecture contains no step that verifies the truth of what it generates. Fluent but factually incorrect output is a documented problem (Ji et al., 2023).
- **“Only statistics” or a “world model”?** Positions diverge. One argues that models trained only on textual form cannot attain understanding of meaning (Bender and Koller, 2020). Another points to evidence that models trained for next-token prediction can construct internal representations of domain structure, such as the state of an Othello board (Li et al., 2023). The characterization of “understanding” remains contested, and this article is limited to the mechanisms and cited evidence.
- **Emergence.** See Section 13: the nature of capability jumps with scale remains debated (Wei et al., 2022a; Schaeffer et al., 2023).

---

[referencia=d9c08b4d6cd4e69f score=0.032]
**Alternatives used in the literature.**

- **Learned positions:** a trainable table used in BERT and GPT-2 (Devlin et al., 2019; Radford et al., 2019).
- **Relative positions:** attention becomes dependent on the distance between tokens (Shaw et al., 2018).
- **RoPE (rotary position embeddings):** rotates Q and K according to position, encoding relative position in the dot product itself (Su et al., 2021). It is used in models such as LLaMA (Touvron et al., 2023).
- **ALiBi:** adds a linear distance-dependent bias to attention scores, improving extrapolation to sequences longer than those seen in training (Press et al., 2022).

**Numerical example.** Let d_model = 4 (didactic; the original Transformer uses 512), with hand-selected embeddings for the four tokens and sinusoidal encoding computed by the formula above. For *banco* at position 1: PE = [sin(1), cos(1), sin(0.01), cos(0.01)] = [0.841; 0.540; 0.010; 1.000]. Adding the embedding [0; 1; 0.5; 0] yields x = [0.841; 1.540; 0.510; 1.000]. Figure 2 shows the three matrices; X = E + P, of dimension 4 × 4, is the input to the first layer.

---

[referencia=d9c08b4d6cd4e69f score=0.020]
box(ax,2.3,4.2,5.6,0.6,"Add & Norm (residual + normalização)",C["gray"],fs=8.8)
arrow(ax,5,12.9,5,12.2);arrow(ax,5,11.3,5,10.7);arrow(ax,5,9.8,5,9.3)
arrow(ax,5,7.65,5,7.15);arrow(ax,5,6.55,5,6.1);arrow(ax,5,5.3,5,4.8)
for (ya,yb) in [(8.6,6.85),(6.35,4.5)]:
    ax.plot([1.6,1.6],[ya,yb],color="#c0392b",lw=1.4)
    ax.plot([1.6,2.3],[ya,ya],color="#c0392b",lw=1.4)
    ax.add_patch(FancyArrowPatch((1.6,yb),(2.3,yb),arrowstyle="-|>",mutation_scale=11,color="#c0392b",lw=1.4))
ax.text(1.45,7.3,"conexão\nresidual",rotation=90,fontsize=7.5,color="#c0392b",ha="right",va="center")
ax.text(1.45,5.4,"conexão\nresidual",rotation=90,fontsize=7.5,color="#c0392b",ha="right",va="center")
box(ax,2,2.5,6,0.9,"5. PROJEÇÃO PARA O VOCABULÁRIO → LOGITS\nh_final · W_out  (um valor por token do vocabulário)",C["out"],bold=True,fs=8.8)
box(ax,2,1.2,6,0.9,"6. SOFTMAX (com temperatura T) → PROBABILIDADES\nP(próximo token | contexto)",C["out"],bold=True,fs=8.8)
box(ax,2,-0.1,6,0.9,"7.

---

[referencia=d9c08b4d6cd4e69f score=0.018]
## 19.4 LayerNorm and RMSNorm verification for banco

**File:** `04_verificar_ln_rms.py`. **Function.** Recomputes the mean, variance, LayerNorm, and RMSNorm of the residual-sum vector for token *banco* at position 1 in the causal version, and verifies that LayerNorm yields mean 0 and variance 1.

**Supports.** The numerical example in Section 7. Requires `toy.npz` and `toy2.npz` from 19.1 and 19.2.

```
import numpy as np
d=np.load("toy2.npz"); R=d["Rc"]; r=R[1]
print("R",r,"mean",r.mean(),"var",r.var(),"std",np.sqrt(r.var()+1e-5))
print("LN",(r-r.mean())/np.sqrt(r.var()+1e-5))
print("RMS",np.sqrt((r**2).mean()+1e-5), r/np.sqrt((r**2).mean()+1e-5))
X=np.load("toy.npz")["X"]; print("X1",X[1],"O1",d["Oc"][1])
print(d["Yc"][1].mean(), d["Yc"][1].var())
```

---

[referencia=d9c08b4d6cd4e69f score=0.018]
## 19.4 LayerNorm and RMSNorm verification for banco

**File:** `04_verificar_ln_rms.py`. **Function.** Recomputes the mean, variance, LayerNorm, and RMSNorm of the residual-sum vector for token *banco* at position 1 in the causal version, and verifies that LayerNorm yields mean 0 and variance 1.

**Supports.** The numerical example in Section 7. Requires `toy.npz` and `toy2.npz` from 19.1 and 19.2.

```
import numpy as np
d=np.load("toy2.npz"); R=d["Rc"]; r=R[1]
print("R",r,"mean",r.mean(),"var",r.var(),"std",np.sqrt(r.var()+1e-5))
print("LN",(r-r.mean())/np.sqrt(r.var()+1e-5))
print("RMS",np.sqrt((r**2).mean()+1e-5), r/np.sqrt((r**2).mean()+1e-5))
X=np.load("toy.npz")["X"]; print("X1",X[1],"O1",d["Oc"][1])
print(d["Yc"][1].mean(), d["Yc"][1].var())
```

---

[referencia=d9c08b4d6cd4e69f score=0.018]
**Do not confuse this with *grokking*.** *Grokking* denotes a distinct phenomenon: in small algorithmic tasks, generalization appears long after the model has already memorized the training set (Power et al., 2022), and it has been analyzed using mechanistic interpretability techniques (Nanda et al., 2023). Grokking occurs over training time, whereas scale-based emergence occurs across model sizes.

**Application to the *banco* case.** Disambiguation of common senses is already observed in relatively small models such as BERT-base, with 110 million parameters (Reif et al., 2019). There is therefore no basis for asserting a fixed layer or parameter threshold at which the capability “appears.” The literature supports the conclusions that the capability results from training and that its quality and scope improve with scale.

**Implications.** If capabilities can arise without being explicitly designed, evaluation and interpretability become central to development: the model must be tested, not merely inspected at the code level, to determine what it does (Ganguli et al., 2022; Olsson et al., 2022).

---

[referencia=d9c08b4d6cd4e69f score=0.017]
- Olsson, C. et al. (2022). In-context learning and induction heads. Transformer Circuits Thread. arXiv:2209.11895. https://arxiv.org/abs/2209.11895
- Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. In: NeurIPS 35. arXiv:2203.02155. https://arxiv.org/abs/2203.02155
- Pope, R.; Douglas, S.; Chowdhery, A.; Devlin, J.; Bradbury, J.; Levskaya, A.; Heek, J.; Xiao, K.; Agrawal, S.; Dean, J. (2023). Efficiently scaling Transformer inference. Proceedings of Machine Learning and Systems, 5 (MLSys 2023). arXiv:2211.05102. https://arxiv.org/abs/2211.05102 [link auditado] [conferido]
- Power, A.; Burda, Y.; Edwards, H.; Babuschkin, I.; Misra, V. (2022). Grokking: Generalization beyond overfitting on small algorithmic datasets. arXiv:2201.02177. https://arxiv.org/abs/2201.02177
- Press, O.; Smith, N. A.; Lewis, M. (2022). Train short, test long: Attention with linear biases enables input length extrapolation. In: ICLR 2022. arXiv:2108.12409. https://arxiv.org/abs/2108.12409
- Press, O.; Wolf, L. (2017). Using the output embedding to improve language models. In: EACL 2017, p. 157–163. arXiv:1608.05859. https://arxiv.org/abs/1608.05859
- Radford, A.; Narasimhan, K.; Salimans, T.; Sutskever, I. (2018). Improving language understanding by generative pre-training. OpenAI, technical report. https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

---

[referencia=d9c08b4d6cd4e69f score=0.017]
**Caveat.** Layer boundaries vary with the model, task, and analytical method. Layer ranges used in didactic explanations — for example, “layer 6 resolves the sense of *banco*” — are illustrations, not results measured in this article.

---

[referencia=d9c08b4d6cd4e69f score=0.016]
# **Opening the Black Box of LLM Inference: Foundations of Generative AI**

## Anatomy of the Transformer from the Inside, from Input to Output Token

**SGAEIA Research Series — Article 22**

**Aridio Silva**

Independent Researcher, Brazil

Creator of SGAEIA — Secure Governed Autonomous Edge Intelligence Architecture**ORCID:** 0009–0008–2411–6995**DOI:** https://doi.org/10.5281/zenodo.23540392**Published:** October 21, 2026**License:** Creative Commons Attribution 4.0 International — CC BY 4.0

## Abstract

This article provides a technical, formal, and didactic explanation of the inference process in Transformer-based language models, from input tokenization to next-token selection. It combines formulas, reproducible numerical examples, and six figures to explain embeddings, positional encoding, self-attention, masks, residual connections, normalization, feed-forward networks, logits, softmax, and decoding strategies. A small-scale case study of the ambiguous Portuguese word *banco* demonstrates how context changes representations without claiming to reproduce the behavior of a real trained model. Finally, the article distinguishes model inference from the governed execution of an agentic system and presents a public, non-normative interpretation of the implications for SGAEIA.

**Keywords:** AI; Transformer; inference; LLM; attention; tokenization; embeddings; softmax; emergent properties; SGAEIA.

---

[referencia=d9c08b4d6cd4e69f score=0.015]
- Wei, J.; Wang, X.; Schuurmans, D. et al. (2022b). Chain-of-thought prompting elicits reasoning in large language models. In: NeurIPS 35. arXiv:2201.11903. https://arxiv.org/abs/2201.11903
- Wiegreffe, S.; Pinter, Y. (2019). Attention is not not explanation. In: EMNLP-IJCNLP 2019, p. 11–20. arXiv:1908.04626. https://arxiv.org/abs/1908.04626
- Wu, Y. et al. (2016). Google’s neural machine translation system: Bridging the gap between human and machine translation. arXiv:1609.08144. https://arxiv.org/abs/1609.08144
- Xiong, R. et al. (2020). On layer normalization in the Transformer architecture. In: ICML 2020 (PMLR 119). arXiv:2002.04745. https://arxiv.org/abs/2002.04745
- Zhang, B.; Sennrich, R. (2019). Root mean square layer normalization. In: NeurIPS 32. arXiv:1910.07467. https://arxiv.org/abs/1910.07467

**Reproducibility.** The numerical examples in Sections 3–12 were computed in Python 3 with NumPy; W1, W2, and W_out were generated with a fixed random seed (0) and normal distributions with standard deviations 0.5 (W1, W2) and 0.8 (W_out). The programs are reproduced in Section 19; the parameter counts in Sections 6 and 8 are direct arithmetic and require no script.

---

[referencia=d9c08b4d6cd4e69f score=0.013]
## 8. Stage 6 — Feed-forward network (FFN)

**Why this stage is necessary.** In attention, the weights depend on content, but the output is a weighted average of Values obtained through linear projections (V = X·Wv, followed by Wo); the only nonlinearity is the softmax that determines the weights. The FFN adds a nonlinear transformation applied to each token after contextual information has been assembled. There is also a capacity rationale: FFNs contain roughly two-thirds of a Transformer’s parameters and act as memories for patterns (Geva et al., 2021). Expanding to d_ff = 4 × d_model in the original model is a design choice that increases this capacity (Vaswani et al., 2017).

**Concept.** After attention, each position passes through a small neural network with two linear layers and a nonlinearity between them, applied **independently to each token** with the same weights at every position in the layer (Vaswani et al., 2017):

Attention mixes information **between** tokens. The FFN transforms information **within** each token, expanding it to a larger dimension d_ff (2048 in the original model, or 4 × d_model), applying the nonlinearity, and compressing it back to d_model.

**Activation functions.** ReLU is used in the original Transformer; GELU in BERT and GPT (Hendrycks and Gimpel, 2016; Devlin et al., 2019; Radford et al., 2019); and gated variants of GLU, such as **SwiGLU**, in more recent models (Shazeer, 2020; Touvron et al., 2023).

**Interpretation.** Geva et al. (2021) propose that the FFN functions as a **key–value memory**: columns of W1 detect patterns in the input vector (keys), while rows of W2 contribute associated information (values). This interpretation helps explain why much factual knowledge appears to reside in FFNs rather than attention. It is an interpretive hypothesis supported by empirical analysis, not a fact demonstrated for every model.

---

[referencia=d9c08b4d6cd4e69f score=0.013]
## 13. Emergent properties and scaling laws

**Purpose of this section.** It explains how a behavior such as disambiguation can exist without being explicitly programmed, linking the result of Section 12 to the training process in Section 10. It frames the debate on emergence without claiming more than the literature supports.

**Concept.** An **emergent property** is a characteristic of the system as a whole that is not programmed into any single component and arises from large-scale interaction among components (Anderson, 1972). Transformer code contains only matrix multiplications, additions, normalizations, and softmax; the training objective is only to predict the next token. Nothing explicitly names word senses, syntax, or reasoning, yet representations of this kind appear in the learned weights (Sections 9 and 12). A common analogy is an ant colony: no individual ant “knows” how to build a bridge, yet the colony builds one.

**Capabilities that emerge with scale.** Wei et al. (2022a) define an emergent capability as one that is absent in smaller models and present in larger models such that its appearance cannot be predicted by simple extrapolation from the smaller-model curves. Examples discussed in the literature include few-shot prompting in large models (Brown et al., 2020) and chain-of-thought reasoning (Wei et al., 2022b).

**Scaling laws.** While average prediction loss improves smoothly and predictably with parameters, data, and compute (Kaplan et al., 2020; Hoffmann et al., 2022), performance on specific tasks may appear to change abruptly. Ganguli et al. (2022) discuss this combination of predictability in loss and surprise in capabilities.

**Debate: genuine emergence or a metric effect?** Schaeffer et al. (2023) argue that some observed jumps result from discontinuous metrics, such as exact match, and that continuous metrics applied to the same models reveal gradual progress. The debate remains open, and the literature advises caution when claiming that a capability “suddenly appears.”