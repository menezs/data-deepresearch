[referencia=fec598beac277b65 score=0.996]
#### SUMMARY OF EVIDENCE FOR SUB-CLAIMS (STRONGEST ARGUMENT FOR EACH) 

||SmallAttention-Only|Small withMLPs|LargeModels|
|---|---|---|---|
|ContributesSome|Strong,Causal|Strong,Causal|Medium,Correlational &<br>Mechanistic|
|ContributesMajority|Strong,Causal|Medium,Causal|Medium,Correlational|



Here is the list of arguments weʼll be making, one per section, repeated from the introduction: 

- <u>Argument 1 (Macroscopic</u> co-occurrence): Transformer language models undergo a “phase change” early in training, during which induction heads form and simultaneously in-context learning improves dramatically. 

- <u>Argument 2 (Macroscopic</u> co-perturbation): When we change the transformer architecture in a way that shifts whether induction heads can form (and when), the dramatic improvement in in-context learning shifts in a precisely matching way. 

- <u>Argument 3</u> (Direct ablation): When we directly “knock out” induction heads at test-time in small models, the amount of in-context learning greatly decreases. 

- <u>Argument 4 (Specific</u> examples of induction head generality): Although we define induction heads very narrowly in terms of copying literal sequences, we empirically observe that these same heads also appear to implement more sophisticated types of in-context learning, including highly abstract behaviors, making it plausible they explain a large fraction of incontext learning. 

- <u>Argument 5</u> (Mechanistic plausibility of induction head generality): For small models, we can explain mechanistically how induction heads work, and can show they contribute to incontext learning.  Furthermore, the actual mechanism of operation suggests natural ways in which it could be repurposed to perform more general in-context learning. 

- <u>Argument 6 (Continuity</u> from small to large models): In the previous 5 arguments, the case for induction heads explaining in-context learning is stronger for small models than for large ones.  However, many behaviors and data related to both induction heads and in-context learning are smoothly continuous from small to large models, suggesting the simplest explanation is that mechanisms are the same.

---

[referencia=fec598beac277b65 score=0.995]
### Assessing the Evidence 

Despite all of the co-occurrence evidence above (and more in the <u>Model Analysis Table),</u> the fact remains that we havenʼt shown that induction heads are the primary mechanism for in-context 

learning. We have merely shown that induction heads form at the same time as in-context learning, and that in-context learning does not improve thereafter. There are a number of potential confounds in this story. Below we summarize reasons in favor and against thinking the connection is causal. The argument in favor might look like this: 

- The formation of induction heads is correlated with a great increase in models' capacity for 

- in-context learning, for a wide variety of models large and small. 

- It's highly improbable these two sharp transitions would co-occur across so many models by pure chance, without any causal connection. 

- There is almost surely some connection, and the simplest possibility is that induction heads are the primary mechanism driving the observed increase in in-context learning. (However, as discussed below, it could also be a confounding variable.) 

- Since over 75% of final in-context learning forms in this window, one might naively believe 

- this to be the amount of in-context learning that induction heads are responsible for. 

However, the following issues and confounds suggest caution:

---

[referencia=fec598beac277b65 score=0.995]
## Ar uments that induction heads are the g - mechanism for the majority of in context learnin . g 

Now weʼll proceed to the main part of the paper, which makes the case that induction heads may provide the primary mechanism for the majority of in-context learning for transformer models in general. As stated in the introduction, this is a very broad hypothesis and much of our evidence is indirect, but nevertheless we believe that all the lines of evidence together make a relatively strong, though not conclusive, case. 

Before we go through the arguments, itʼs useful to delineate where the evidence is more conclusive vs. less conclusive. This is shown in the table below. For small, attention-only models, we believe we have strong evidence that attention heads are the mechanism for the majority of in-context learning, as we have evidence supported by ablations and mechanistic reverse engineering. Conversely, for all models, we can make a strong case that induction heads play some role in incontext learning, as we can demonstrate examples and show suggestive correlations. However, the larger the models get, the harder it is to establish that induction heads account for the actual majority of in-context learning. For large models with MLPʼs, we must therefore rely on mainly correlational evidence, which could be confounded. We explore alternate hypotheses throughout, including at the end of <u>Argument 1</u> and again briefly in <u>Argument 6.</u>

---

[referencia=fec598beac277b65 score=0.994]
#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 

||SmallAttention-Only|Small withMLPs|LargeModels|
|---|---|---|---|
|ContributesSome|Strong,Causal|Strong,Causal||
|ContributesMajority|Strong,Causal|Medium,Causal||



For the cases they cover, ablations are by far our strongest evidence. The basic argument is that knocking out induction heads decreases the amount of in-context learning we observe in our models. By “knocking out” we mean that we remove a given attention head from the model at test time, doing a forward pass on the transformer without it. (See <u>our methods section</u> for exact details of how the ablation is done.) 

The ablations presented below show how attention heads contribute to in-context learning, but we can also do ablations to study how attention heads contribute to the overall behavior change that occurs during the phase change (see the <u>Model Analysis Table).</u> 



These plots are a small excerpt of the Model Analysis Table; look there to see the full evidence. See our methods section for exact details of how the ablation is done. 

In fact, almost all the in-context learning in small attention-only models appears to come from these induction heads! This begins at the start of the phase change, and remains true through the end of training.<sup>17</sup> 

Unfortunately, we do not have ablations for our full-scale models.18 For the models where we do have ablations, it seems like this evidence is clearly dispositive that induction heads increase incontext learning (at least as we've chosen to evaluate it). But can we further infer that they're the primary mechanism? A couple considerations: 

- In attention-only models, in-context learning must essentially be a sum of contributions from different attention heads.19 But in models with MLPs, in-context learning could also come from interactions between MLP and attention layers. While ablating attention heads would affect such mechanisms, the relationship between the effect of the ablation on in-context learning and its true importance becomes more complicated.20 As a result, we can't be fully confident that head ablations in MLP models give us the full picture. 

- Our ablations measure the marginal effects of removing attention heads from the model. To the extent two heads do something similar and the layer norm before the logits rescales things, the importance of individual heads may be masked.

---

[referencia=fec598beac277b65 score=0.994]
## Ar ument 6: Extra lation from small g po models suggests induction heads are - responsible for the majority of in context learning in large models. 

#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 

|SmallAttention-Only|Small withMLPs|LargeModels|
|---|---|---|
|ContributesSome||Analogy|
|ContributesMajority||Analogy|



This argument is really an extended inference from all the above arguments. Arguments 1-5 present fairly strong evidence that in small transformers (especially small attention-only models), induction heads are responsible for the majority of in-context learning, while for large transformers, the evidence is not as strong. To what extent can one reasonably infer from small models that the same thing is happening in larger models? Obviously this is a matter of judgment. 

The measurements in the <u>model analysis table</u> look fully analogous between the small attentiononly, small models with MLPs, and full-scale model cases. Provided there's more than one layer, all of them go through a phase change. All of them have the same sharp increase in in-context learning, with the same rough amounts before and after the transition. All of them trace similar paths in PCA space. All of them form induction heads. 

If things change from the small model case to the large model case, where do they change? And why is there no visible sign of the change in all our measurements? 

On the flip side, there are many cases where large models behave very differently than small models (see discussion of phase changes with respect to model size in <u>Related Work). Extrapolating</u> from small models to models many orders of magnitude larger is something one should do with caution. 

The most compelling alternative possibility we see is that other composition mechanisms may also form during the phase change. Larger models have more heads, which gives them more capacity for other interesting Q-composition and K-composition mechanisms that small models canʼt afford to express. If all “composition heads” form simultaneously during the phase change, then itʼs possible that above some size, non-induction composition heads could together account for more of the phase change and in-context learning improvement than induction heads do.

---

[referencia=fec598beac277b65 score=0.993]
# - In context Learnin and g Induction Heads 

###### AUTHORS 

Catherine Olsson ,∗ Nelson Elhage ,∗ Neel Nanda ,∗ Nicholas Joseph†, Nova DasSarma†, Tom Henighan†, Ben Mann†, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, 

Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, 

AFFILIATION 

Anthropic 

PUBLISHED 

Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, 

‡ 

Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah 

Mar 8, 2022 

* Core Research Contributor; † Core Infrastructure Contributor; ‡ Correspondence to colah@anthropic.com; 

Author contributions statement below. 

Abstract: “Induction heads” are attention heads that implement a simple algorithm to complete token sequences like [A][B] … [A] → [B]. In this work, we present preliminary and indirect evidence for a hypothesis that induction heads might constitute the mechanism for the majority of all “incontext learning” in large transformer models (i.e. decreasing loss at increasing token indices). We find that induction heads develop at precisely the same point as a sudden sharp increase in incontext learning ability, visible as a bump in the training loss. We present six complementary lines of evidence, arguing that induction heads may be the mechanistic source of general in-context learning in transformer models of any size. For small attention-only models, we present strong, causal evidence; for larger models with MLPs, we present correlational evidence.

---

[referencia=fec598beac277b65 score=0.989]
The hypothesis that induction heads are the primary mechanism of in-context learning predicts that the phase change will happen in one-layer models with this change, and perhaps might happen earlier in models with more layers. If they're one of several major contributing factors, we might expect some of the in-context learning improvement to happen early, and the rest at the same time as the original phase change. 

The results (figure below) are in line with the predictions: when we use the smeared-key 

architecture, in-context learning does indeed form for one-layer models (when it didnʼt before), and it forms earlier for two-layer and larger models.  More such results can be seen in the <u>model analysis table.</u> 



These plots are an excerpt of the Model Analysis Table; look there to see more analysis of how the smear models compare to their vanilla counterparts. 

However, we probably shouldn't make too strong an inference about large models on this evidence. This experiment suggests that induction heads are the minimal mechanism for greatly increased incontext learning in transformers. But one could easily imagine that in larger models, this mechanism isnʼt the whole story, and also this experiment doesnʼt refute the idea of the mechanism of incontext learning changing over the course of training.

---

[referencia=fec598beac277b65 score=0.989]
#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 



<!-- Start of picture text -->
Small Attention-Only Small with MLPs Large Models<br>Contributes Some Plausibility<br>Contributes Majority Plausibility<br><!-- End of picture text -->

All of our previous evidence (in Arguments 1-3) focused on observing or perturbing the connection between induction head formation and macroscopic in-context learning. A totally different angle is to just find examples of induction heads implementing seemingly-difficult in-context learning behaviors; this would make it plausible that induction heads account for the majority of in-context learning. This evidence applies even to the very largest models (and we study up to 12B parameter models), but since it shows only a small number of tasks, itʼs only suggestive regarding in-context learning in general. 

Recall that we <u>define</u> induction heads as heads that empirically copy arbitrary token sequences using a “prefix matching” attention pattern. Our goal is to find heads that meet this definition but also perform more interesting and sophisticated behaviors, essentially showing that induction heads in large models can be “generalizable”. 

In this argument, we show some anecdotal examples of induction heads from larger transformers (our <u>40-layer model</u> with 13 billion parameters) that exhibit exactly such behaviors – namely literal copying, translation, and a specific type of abstract pattern matching. The behaviors are all of the form [A*][B*]...[A][B] , aka the “fuzzy nearest neighbor match” or “find something similar early in the sequence and complete the sequence in analogy”. We verify that these heads score highly on our “copying” <u>and</u> “prefix <u>matching” evaluations</u> (that is, they increase the probability of the token they attend to, and attend to tokens where the prefix matches the present token on random text), and are thus “induction heads” by our strict empirical <u>definition,</u> at the same time as they also perform these more sophisticated tasks. 

The results of some example heads are shown in the table below, and described in the subsections below.

---

[referencia=fec598beac277b65 score=0.987]
Specifically, the paper presents six complementary lines of evidence arguing that induction heads may be the mechanistic source of general in-context learning in transformer models of any size: 

- <u>Argument 1 (Macroscopic</u> co-occurence): Transformer language models undergo a “phase change” early in training, during which induction heads form and simultaneously in-context learning improves dramatically. 

- <u>Argument 2 (Macroscopic</u> co-perturbation): When we change the transformer architecture in a way that shifts whether induction heads can form (and when), the dramatic improvement in in-context learning shifts in a precisely matching way. 

- <u>Argument 3</u> (Direct ablation): When we directly “knock out” induction heads at test-time in small models, the amount of in-context learning greatly decreases. 

- <u>Argument 4 (Specific</u> examples of induction head generality): Although we define induction heads very narrowly in terms of copying literal sequences, we empirically observe that these same heads also appear to implement more sophisticated types of in-context learning, including highly abstract behaviors, making it plausible they explain a large fraction of incontext learning. 

- <u>Argument 5</u> (Mechanistic plausibility of induction head generality): For small models, we can explain mechanistically how induction heads work, and can show they contribute to incontext learning. Furthermore, the actual mechanism of operation suggests natural ways in which it could be re-purposed to perform more general in-context learning. 

- <u>Argument 6 (Continuity</u> from small to large models): In the previous 5 arguments, the case for induction heads explaining in-context learning is stronger for small models than for large ones. However, many behaviors and data related to both induction heads and in-context learning are smoothly continuous from small to large models, suggesting the simplest explanation is that mechanisms are the same.

---

[referencia=fec598beac277b65 score=0.984]
#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 

||SmallAttention-Only|Small withMLPs|LargeModels|
|---|---|---|---|
|ContributesSome|Medium,Interventional|Medium,Interventional|Weak,Interventional|
|ContributesMajority|Medium,Interventional|Medium,Interventional|Weak,Interventional|



One thing that falls short about <u>Argument 1</u> is that weʼre just observing induction heads and incontext learning co-vary; like any observational study, it is not as convincing as if we actively changed one thing and measured what happened to the other. In this section we do a more “interventional” experiment, in which we change the model architecture in a way that makes induction heads easier to form, and observe the effect on in-context learning. The change makes a bigger difference for smaller models so is more convincing there, but also carries some amount of weight for larger models (see table above). 

To design our experiment, we start with the observation (noted in the previous section) that the phase change and the corresponding improvement in in-context learning only occurs in transformers with more than one layer. This is what we'd predict if induction heads were the mechanism for the majority of in-context learning: induction heads require a composition of attention heads, which is only possible with two or more layers.<sup>15</sup> 

Of course, the observation about one-layer models is pretty weak evidence by itself. (One could imagine one-layer models being different from models with more layers in all sorts of ways!) But it suggests a more general line of attack. If induction heads are the mechanism behind the large improvement in in-context learning, that makes predictions about the minimum architectural requirements in order to achieve the observed improvement. For a standard transformer, the important thing is to have two attention layers. But that's only because the key vectors need to be a function of the attended token and the token before it. 

We define a “smeared key" architecture with a very simple modification that should make it easy for transformers of any depth to express induction heads. In our modified models, for each head _h_ , we introduce a trainable real parameter _α_<sup>_h_</sup> which we use as _σ_ ( _αh_ ) ∈[0, 1] to interpolate between the key for the current token and previous token16 :

---

[referencia=fec598beac277b65 score=0.982]
In this paper our goal is to provide evidence for something more expansive: that induction heads play a major role in general in-context learning (not just literal [A][B]...[A] `→` [B] copying), for large models and not just for small 2-layer attention only models.  To do this clearly and coherently, we need a more precise definition of induction heads. Mechanistic analysis of weights and eigenvalue analysis are much more complicated in large models with MLPʼs, so for this paper we choose to define induction heads by their narrow empirical sequence copying behavior (the [A][B]...[A] `→` [B] ), and then attempt to show that they (1) also serve a more expansive function that can be tied to in-context learning, and (2) coincide with the mechanistic picture for small models. 

Formally, we define an induction head as one which exhibits the following two properties5 on a repeated random sequence6 of tokens: 

- Prefix matching: The head attends back to previous tokens that were followed by the current and/or recent tokens.7 That is, it attends to the token which induction would suggest 

- comes next. 

Copying: The headʼs output increases the logit corresponding to the attended-to token. 

In other words, induction heads are any heads that empirically increase the likelihood of [B] given [A][B]...[A] when shown a repeated sequence of completely random tokens. An illustration of induction headsʼ behavior is shown here: 



Note that, as a consequence, induction heads will tend to be good at repeating sequences wholesale. For example, given “The cat sat on the mat. The cat …”, induction heads will promote the continuation “sat on the mat”. This gives a first hint of how they might be connected to general incontext learning and even few-shot learning: they learn to repeat arbitrary sequences, which is a (simple) form of few-shot learning. 

One of things weʼll be trying to establish is that when induction heads occur in sufficiently large models and operate on sufficiently abstract representations, the very same heads that do this sequence copying also take on a more expanded role of analogical sequence copying or in-context nearest neighbors. By this we mean that they promote sequence completions like

---

[referencia=fec598beac277b65 score=0.977]
## Argument 1: Transformer language models “ ” undergo a phase change during training, durin which induction heads form and g - simultaneously in context learning improves dramaticall . y 

Our first line of evidence comes from correlating measures of in-context learning and measures of induction head presence over the course of training. Specifically, we observe a tight co-variation between them across dozens of models, of different sizes, trained on different datasets (See <u>Model Analysis Table</u> for more on the models in which we observe this co-occurrence.). 

The table below summarizes the quality of this evidence for the models we have studied: it applies to both large and small models, and is the expected outcome if induction heads were responsible for the majority of in-context learning, but it is only correlational and so could be confounded (discussed more below).

---

[referencia=fec598beac277b65 score=0.968]
#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 

Small Attention-Only Small with MLPs Large Models Contributes Some Strong, Mechanistic Strong, Mechanistic Medium, Mechanistic Contributes Majority Weak, Mechanistic 

One of the main reasons we care about whether induction heads drive in-context learning is that we can understand them and so have a path to understanding in-context learning. But we can also turn this around: we can use our understanding of induction heads to make a purely logical argument that they should contribute to in-context learning. 

We begin with a semi-empirical argument. Let's take for granted that induction heads behave the way we've described and empirically seen, searching the context for previous examples and copying what happened next. We should expect such a procedure to improve a model's ability to predict tokens later in its context. We're essentially using the previous context as data points for a nearest neighbor algorithm, and nearest neighbors improves as one gives it more data points. Therefore, if induction heads exist as described, they would contribute to in-context learning as we've defined it. 

In some sense, this argument is quite strong if we're only arguing that there exist some cases where induction heads contribute to in-context learning. We've seen concrete examples above where induction heads improve token predictions by copying earlier examples. If nothing else, they must help in those cases! And more generally, our definition of induction heads (in terms of their behavior on repeated random sequences) suggests they behave this way quite generally. This argument doesn't say anything about what fraction of in-context learning is performed by induction heads, but it seems like a very strong argument that some is, both in large and small models.

---

[referencia=fec598beac277b65 score=0.966]
But the really satisfying thing about this line of attack — namely, using our understanding of induction heads to anticipate their impact on in-context learning — is that we can actually drop the dependency on empirical observations of induction head behavior, at the cost of needing to make a more complex argument. In our <u>previous paper,</u> we were able to <u>reverse engineer</u> induction heads, showing from the parameter level how they implement induction behavior (and that they should). If we trust this analysis, we can know how induction heads behave without actually running them, and the argument we made in the previous paragraph goes through. Of course, there are some limitations. In the previous paper, we only reverse engineered a single induction head in a small attention-only model, although we can reverse engineered others (and have done so). A bigger issue is that right now we're unable to reverse engineer induction heads in models with MLP layers. But at least in some cases weʼve observed, we can look at the parameters of a transformer and identify induction heads, just as a programmer might identify an algorithm by reading through source code. 

We can actually push this argument a bit further in the case of the two-layer attention only transformer we reverse engineered in the previous paper. Not only do we understand the induction heads and know that they should contribute to in-context learning, but there doesn't seem to really be an alternative mechanism that could be driving it.23 This suggests that induction heads are the primary driver of in-context learning, at least in very small models. 

The following section will briefly summarize reverse engineering induction heads. Note that it relies heavily on linking to our previous paper. We do not expect it to be possible to follow without reading the linked portions. After that, we briefly discuss how the described mechanism could also implement more abstract types of induction head behavior.

---

[referencia=fec598beac277b65 score=0.964]
It turns out that a sudden improvement in in-context learning isn't the only thing that changes in this window. If we go through the attention heads of a model and and score them for whether they are induction heads (using a prefix matching score which measures their ability to perform the task we used to define induction heads in <u>Key Concepts),</u> we find that induction heads form abruptly during exactly the same window where in-context learning develops (figure below). Again we show only a few models here, but a full set is shown in the <u>Model Analysis Table. The</u> exception is the one-layer model, where induction heads never form – just as in-context learning never substantially develops for the one-layer model. 



This already strongly suggests some connection between induction heads and in-context learning, but beyond just that, it appears this window is a pivotal point for the training process in general: whatever's occurring is visible as a bump on the training curve (figure below). It is in fact the only place in training where the loss is not convex (monotonically decreasing in slope). 

That might not sound significant, but the loss curve is averaging over many thousands of tokens. Many behaviors people find interesting in language models, such as the emergence of arithmetic, would be microscopic on the loss curve. For something to be visible at that scale suggests it's a widespread, major change in model behavior. This shift also appears to be the first point where, at least for small models, the loss curve diverges from a one-layer model – which does not display the bump, just as it does not display the other abrupt changes. 



We can also apply principal components analysis (PCA) to the per-token losses, as described in <u>per-token-loss analysis,</u> which allows us to summarize the main dimensions of variation in how several models' predictions vary over the course of training. 

Below we show the first two principal components of these modelsʼ predictions, with the golden outline highlighting the same interval shown above, when in-context learning abruptly improved. We see that the training trajectories pivot during exactly the same window where the other changes happen. In some sense, whatever is occurring when in-context learning improves is the primary deviation from the basic trajectory our transformers follow during the course of their training.  Once again the only exception is the one-layer model – where induction heads cannot form and incontext learning does not improve. 



In summary, the following things all co-occur during the same abrupt window:

---

[referencia=fec598beac277b65 score=0.956]
Ultimately, however, our goal is to reverse-engineer frontier language models (which often contain hundreds of layers and billions or trillions of parameters), not merely 2-layer attention-only models. Unfortunately, both the presence of many layers, and the presence of MLPs, makes it much more difficult to mathematically pin down the precise circuitry of these models. However, a different approach is possible: by empirically observing, perturbing, and studying the learning process and the formation of various structures, we can try to assemble an indirect case for what might be happening mechanistically inside the network. This is somewhat similar to how a neuroscientist might gain understanding of how part of the brain functions by looking at neural development over time, studying patients with an injury to that part of the brain, perturbing brain function in animals, or looking at a select small number of relevant neurons. 

In this paper, we take the first preliminary steps towards building such an indirect case. In particular, we present preliminary and indirect evidence for a tantalizing hypothesis: that induction heads might constitute the mechanism for the actual majority of all in-context learning in large transformer models. Specifically, the thesis is that there are circuits which have the same or similar mechanism to the 2-layer induction heads and which perform a “fuzzy” or “nearest neighbor” version of pattern completion, completing [A*][B*] … [A] `→` [B] , where A* ≈ A and B* ≈ B are similar in some space; and furthermore, that these circuits implement most in-context learning in large models. 

The primary way in which we obtain this evidence is via discovery and study of a phase change that occurs early in training for language models of every size (provided they have more than one layer), and which is visible as a bump in the training loss. During this phase change, the majority of incontext learning ability (as measured by difference in loss between tokens early and late in the sequence) is acquired, and simultaneously induction heads form within the model that are capable of implementing fairly abstract and fuzzy versions of pattern completion. We study this connection in detail to try to establish that it is causal, including showing that if we perturb the transformer architecture in a way that causes the induction bump to occur in a different place in training, then the formation of induction heads as well as formation of in-context learning simultaneously move along with it.

---

[referencia=fec598beac277b65 score=0.956]
However, the following issues and confounds suggest caution: 

- In large models, we have low time resolution on our analysis over training. Co-occurrence when one only has 15 points in time is less surprising and weaker evidence. 

- Perhaps other mechanisms form in our models at this point, that contribute to not only induction heads, but also other sources of in-context learning. (For example, perhaps the phase change is really the point at which the model learns how to compose layers through the residual stream, enabling both induction heads and potentially many other mechanisms that also require composition of multiple heads) Put another way, perhaps the co-occurrence is primarily caused by a shared latent variable, rather than direct causality from induction heads to the full observed change in in-context learning. 

- The fact that in-context learning score is roughly constant (at 0.4 nats) after the phase change doesn't necessarily mean that the underlying mechanisms of in-context learning are constant after that point. In particular, the metric we use measures a relative loss between the token index 500 and 50, and we know that the modelʼs performance at token 50 improves over training time. Reducing the loss a fixed amount from a lower baseline is likely harder, and so may be driven by additional mechanisms as training time goes on.13 14 

One point worth noting here is that the argument that induction heads account for most in-context learning at the transition point of the phase change is more solid than the argument that they account for most in-context learning at the end of training – a lot could be changing during training even as the in-context learning score remains constant. 

Argument 2: When we change the transformer architecture in a way that shifts when induction heads form or whether the y - can form, the dramatic improvement in in context learnin shifts in a ecisel g pr y matching way.

---

[referencia=fec598beac277b65 score=0.938]
### Induction Heads 

In our <u>previous paper,</u> we discovered a special kind of attention head – which we named induction heads – in two layer attention-only models. Induction heads are implemented by a circuit consisting of a pair of attention heads in different layers that work together to copy or complete patterns. The first attention head copies information from the previous token into each token. This makes it possible for the second attention head to attend to tokens based on what happened before them, rather than their own content. Specifically, the second head (which we call the "induction head") search for a previous place in the sequence where the present token A occurred and attends to the next token (call it B ), copying it and causing the model to be more likely to output B as the next token. That is, the two heads working together cause the sequence …[A][B]…[A] to be more likely to be completed with [B] . 

Induction heads are named by analogy to inductive reasoning. In inductive reasoning, we might infer that if A is followed by B earlier in the context, A is more likely to be followed by B again later in the same context. Induction heads crystallize that inference. They search the context for previous instances of the present token, attend to the token which would come next if the pattern repeated, and increase its probability. Induction heads attend to tokens that would be predicted by basic induction (over the context, rather than over the training data). 

Notice that induction heads are implementing a simple algorithm, and are not memorizing a fixed table of n-gram statistics. The rule [A][B] … [A] `→` [B] applies regardless of what A and B are.4 This means that induction heads can in some sense work out of distribution, as long as local statistics early in the context are representative of statistics later. This hints that they may be capable of more general and abstract behavior. 

Our previous paper focused on a few explorations of induction heads, including showing that these heads occur in 2-layer attention-only models (but not 1-layer models); tracking down how they operate mechanistically as part of our mathematical decomposition of transformers; and making an eigenvalue-based test for detecting their presence. However, we were a bit vague on the exact definition of induction heads: it was more like we found a cluster of behaviors and mechanisms that tended to occur together, and called heads in that cluster “induction heads”.

---

[referencia=fec598beac277b65 score=0.932]
#### STRENGTH OF ARGUMENT FOR SUB-CLAIMS 

||SmallAttention-Only|Small withMLPs|LargeModels|
|---|---|---|---|
|ContributesSome|Medium,Correlational|Medium,Correlational|Medium,Correlational|
|ContributesMajority|Medium,Correlational|Medium,Correlational|Medium,Correlational|



Our first observation is that if we measure in-context learning for transformer models over the course of training (defined as the 50th token loss minus the 500th token loss as described in <u>Key Concepts),</u> it develops abruptly in a narrow window early in training (roughly 2.5 to 5 billion tokens) and then is constant for the rest of training (see figure below).  Before this window there is less than 0.15 nats of in-context learning, after it there is roughly 0.4 nats, an amount that remains constant for the rest of training and is also constant across many different model sizes (except for the one layer model where not much in-context learning ever forms).  This seems surprising – naively, one might expect in-context learning to improve gradually over training, and improve with larger model sizes,9 as most things in machine learning do. 



Although we only show three models above, the pattern holds true very generally: many examples are shown in the <u>Model Analysis Table</u> later in the paper, including models of varying model architecture and size. 

One might wonder if the sudden increase is somehow an artifact of the choice to define in-context learning in terms of the difference between the 500th and 50th tokens. We'll discuss this in more depth <u>later. But</u> for now, an easy way to see that this is a robust phenomena is to look at the derivative of loss with respect to the logarithm token index in context. You can think of this as measuring something like "in-context learning per ε% increase in context length." We can visualize this on a 2D plot, where one axis is the amount of training that has elapsed, the other is the token index being predicted. Before the phase change, loss largely stops improving around token 50, but after the phase change, loss continues to improve past that point.

---

[referencia=fec598beac277b65 score=0.918]
#### We recommend reading this paper as <u>an HTML article.</u> 

As Transformer generative models continue to scale and gain increasing real world use, [1, 2, 3, 4, 5] addressing their associated safety problems becomes increasingly important. Mechanistic interpretability – attempting to reverse engineer the detailed computations performed by the model – offers one possible avenue for addressing these safety issues. If we can understand the internal structures that cause Transformer models to produce the outputs they do, then we may be able to address current safety problems more systematically, as well as anticipating safety problems in future more powerful models.1 

In the past, mechanistic interpretability has largely focused on CNN vision models [6] , but recently, we <u>presented</u> some very preliminary progress on mechanistic interpretability for Transformer language models [7] . Specifically, in our prior work we developed a mathematical framework for decomposing the operations of transformers, which allowed us to make sense of small (1 and 2 layer attention-only) models and give a near-complete account of how they function. Perhaps the most interesting finding was the induction head, a circuit whose function is to look back over the sequence for previous instances of the current token (call it A ), find the token that came after it last time (call it B ), and then predict that the same completion will occur again (e.g. forming the sequence [A][B] … [A] `→` [B] ). In other words, induction heads “complete the pattern” by copying and completing sequences that have occurred before. Mechanically, induction heads in our models are implemented by a circuit of two attention heads: the first head is a “previous token head” which copies information from the previous token into the next token, while the second head (the actual “induction head”) uses that information to find tokens preceded by the present token. For 2-layer attention-only models,2 we were able to show precisely that induction heads implement this pattern copying behavior and appear to be the primary source of in-context learning.