[referencia=a15e6a70c6cf4a11 score=0.969]
reduce this scaling factor.

The Transformer model is illustrated in Figure 1. It uses stacked self-attention and point-

wise, fully connected layers for both the encoder and decoder, shown in the left and right halves

of Figure 1 respectively.

Encoder: The encoder is composed of a stack of identical layers. Each layer has two

sub-layers. The ﬁrst is a multi-head self-attention mechanism, and the second is a simple,

positionwise fully connected feed-forward network.

Decoder: The decoder is also composed of a stack of identical layers. In addition to the

two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs

multi-head attention over the output of the encoder stack.

Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential

operations for different layer types. nis the sequence length, dis the representation dimension,

kis the kernel size of convolutions and rthe size of the neighborhood in restricted self-attention.

Layer Type Complexity per Layer Sequential Maximum Path Length

Operations

Self-Attention O(n2·d)O(1) O(1)

Recurrent O(n·d2)O(n)O(n)

Convolutional O(k·n·d2)O(1) O(logk(n))

Self-Attention (restricted) O(r·n·d)O(1) O(n/r)

More details about multi-head attention and overall architecture can be found in Vaswani

et al. (2017).

2.1 Computational Performance

As noted in Table 1, a self-attention layer connects all positions with a constant number of

sequentially executed operations, whereas a recurrent layer requires O(n)sequential operations.

In terms of computational complexity, self-attention layers are faster than recurrent layers when

the sequence length nis smaller than the representation dimensionality d, which is most often

the case with sentence representations used by state-of-the-art models in machine translations,

such as word-piece (Wu et al., 2016) and byte-pair (Sennrich et al., 2015) representations.

A single convolutional layer with kernel width k < n does not connect all pairs of in-

put and output positions. Doing so requires a stack of O(n/k)convolutional layers in the

case of contiguous kernels, or O(logk(n)) in the case of dilated convolutions (Kalchbrenner

---

[referencia=a15e6a70c6cf4a11 score=0.319]
(2015). These early models used a standard RNN on top of the convolution to generate the

output, which creates a bottleneck and hurts performance.

Fully convolutional neural machine translation without this bottleneck was ﬁrst achieved

in Kaiser and Bengio (2016) and Kalchbrenner et al. (2016). The Extended Neural GPU

model (Kaiser and Bengio, 2016) used a recurrent stack of gated convolutional layers, while

the ByteNet model (Kalchbrenner et al., 2016) did away with recursion and used left-padded

convolutions in the decoder. This idea, introduced in WaveNet (van den Oord et al., 2016),

signiﬁcantly improves efﬁciency of the model. The same technique was improved in a number

of neural translation models recently, including Gehring et al. (2017) and Kaiser et al. (2017).

2 Self-Attention

Instead of convolutions, one can use stacked self-attention layers. This was introduced in the

Transformer model (Vaswani et al., 2017) and has signiﬁcantly improved state-of-the-art in ma-

chine translation and language modeling while also improving the speed of training. Research

arXiv:1803.07416v1  [cs.LG]  16 Mar 2018

Figure 1: The Transformer model architecture.

continues in applying the model in more domains and exploring the space of self-attention

mechanisms. It is clear that self-attention is a powerful tool in general-purpose sequence mod-

eling.

While RNNs represent sequence history in their hidden state, the Transformer has no such

ﬁxed-size bottleneck. Instead, each timestep has full direct access to the history through the

dot-product attention mechanism. This has the effect of both enabling the model to learn more

distant temporal relationships, as well as speeding up training because there is no need to wait

for a hidden state to propagate across time. This comes at the cost of memory usage, as the

attention mechanism scales with t2, where tis the length the sequence. Future work may

reduce this scaling factor.

The Transformer model is illustrated in Figure 1. It uses stacked self-attention and point-

wise, fully connected layers for both the encoder and decoder, shown in the left and right halves

of Figure 1 respectively.

---

[referencia=a15e6a70c6cf4a11 score=0.098]
put and output positions. Doing so requires a stack of O(n/k)convolutional layers in the

case of contiguous kernels, or O(logk(n)) in the case of dilated convolutions (Kalchbrenner

et al., 2016), increasing the length of the longest paths between any two positions in the net-

work. Convolutional layers are generally more expensive than recurrent layers, by a factor of

k. Separable convolutions (Chollet, 2016), however, decrease the complexity considerably, to

O(k·n·d+n·d2). Even with k=n, however, the complexity of a separable convolution

is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the

approach we take in our model.

Self-attention can also yield more interpretable models. In Tensor2Tensor, we can visual-

ize attention distributions from our models for each individual layer and head. Observing them

closely, we see that the models learn to perform different tasks, many appear to exhibit behavior

related to the syntactic and semantic structure of the sentences.

2.2 Machine Translation

We trained our models on the WMT Translation task.

On the WMT 2014 English-to-German translation task, the big transformer model (Trans-

former (big) in Table 2) outperforms the best previously reported models (including ensembles)

by more than 2.0BLEU, establishing a new state-of-the-art BLEU score of 28.4. Training took

3.5days on 8P100 GPUs. Even our base model surpasses all previously published models and

ensembles, at a fraction of the training cost of any of the competitive models.

On the WMT 2014 English-to-French translation task, our big model achieves a BLEU

score of 41.8, outperforming all of the previously published single models, at less than 1/4the

training cost of the previous state-of-the-art model.

For the base models, we used a single model obtained by averaging the last 5 checkpoints,

which were written at 10-minute intervals. For the big models, we averaged the last 20 check-

points. We used beam search with a beam size of 4and length penalty α= 0.6(Wu et al.,

---

[referencia=a15e6a70c6cf4a11 score=0.082]
Available via license: CC BY-NC-SA 4.0

Content may be subject to copyright.

Tensor2Tensor for Neural Machine Translation

Ashish Vaswani1,Samy Bengio1,Eugene Brevdo1,Francois Chollet1,Aidan N. Gomez1,

Stephan Gouws1,Llion Jones1,Łukasz Kaiser1, 3,Nal Kalchbrenner2,Niki Parmar1,

Ryan Sepassi1, 4,Noam Shazeer1, and Jakob Uszkoreit1

1Google Brain

2DeepMind

3Corresponding author: lukaszkaiser@google.com

4Corresponding author: rsepassi@google.com

Abstract

Tensor2Tensor is a library for deep learning models that is well-suited for neural machine trans-

lation and includes the reference implementation of the state-of-the-art Transformer model.

1 Neural Machine Translation Background

Machine translation using deep neural networks achieved great success with sequence-to-

sequence models (Sutskever et al., 2014; Bahdanau et al., 2014; Cho et al., 2014) that used recur-

rent neural networks (RNNs) with LSTM cells (Hochreiter and Schmidhuber, 1997). The basic

sequence-to-sequence architecture is composed of an RNN encoder which reads the source sen-

tence one token at a time and transforms it into a ﬁxed-sized state vector. This is followed by an

RNN decoder, which generates the target sentence, one token at a time, from the state vector.

While a pure sequence-to-sequence recurrent neural network can already obtain good

translation results (Sutskever et al., 2014; Cho et al., 2014), it suffers from the fact that the

whole input sentence needs to be encoded into a single ﬁxed-size vector. This clearly manifests

itself in the degradation of translation quality on longer sentences and was partially overcome

in Bahdanau et al. (2014) by using a neural model of attention.

Convolutional architectures have been used to obtain good results in word-level neural

machine translation starting from Kalchbrenner and Blunsom (2013) and later in Meng et al.

(2015). These early models used a standard RNN on top of the convolution to generate the

output, which creates a bottleneck and hurts performance.

---

[referencia=a15e6a70c6cf4a11 score=0.018]
pages 265–283.

Bahdanau, D., Cho, K., and Bengio, Y. (2014). Neural machine translation by jointly learning to align and

translate. CoRR, abs/1409.0473.

Cho, K., van Merrienboer, B., Gulcehre, C., Bougares, F., Schwenk, H., and Bengio, Y. (2014). Learn-

ing phrase representations using RNN encoder-decoder for statistical machine translation. CoRR,

abs/1406.1078.

Chollet, F. (2016). Xception: Deep learning with depthwise separable convolutions. arXiv preprint

arXiv:1610.02357.

Gehring, J., Auli, M., Grangier, D., Yarats, D., and Dauphin, Y. N. (2017). Convolutional sequence to

sequence learning. CoRR, abs/1705.03122.

Gomez, A. N., Ren, M., Urtasun, R., and Grosse, R. B. (2017). The reversible residual network: Back-

propagation without storing activations. CoRR, abs/1707.04585.

Hochreiter, S. and Schmidhuber, J. (1997). Long short-term memory. Neural computation, 9(8):1735–

1780.

Kaiser, Ł. and Bengio, S. (2016). Can active memory replace attention? In Advances in Neural Information

Processing Systems, pages 3781–3789.

Kaiser, L., Gomez, A. N., and Chollet, F. (2017). Depthwise separable convolutions for neural machine

translation. CoRR, abs/1706.03059.

Kalchbrenner, N. and Blunsom, P. (2013). Recurrent continuous translation models. In Proceedings

EMNLP 2013, pages 1700–1709.

Kalchbrenner, N., Espeholt, L., Simonyan, K., van den Oord, A., Graves, A., and Kavukcuoglu, K. (2016).

Neural machine translation in linear time. CoRR, abs/1610.10099.

---

[referencia=a15e6a70c6cf4a11 score=0.012]
Neural machine translation in linear time. CoRR, abs/1610.10099.

Meng, F., Lu, Z., Wang, M., Li, H., Jiang, W., and Liu, Q. (2015). Encoding source language with

convolutional neural network for machine translation. In ACL, pages 20–30.

Parmar, N., Vaswani, A., Uszkoreit, J., Kaiser, Ł., Shazeer, N., and Ku, A. (2018). Image Transformer.

ArXiv e-prints.

Sennrich, R., Haddow, B., and Birch, A. (2015). Neural machine translation of rare words with subword

units. arXiv preprint arXiv:1508.07909.

Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., and Dean, J. (2017). Outrageously

large neural networks: The sparsely-gated mixture-of-experts layer. CoRR, abs/1701.06538.

Sutskever, I., Vinyals, O., and Le, Q. V. (2014). Sequence to sequence learning with neural networks. In

Advances in Neural Information Processing Systems, pages 3104–3112.

van den Oord, A., Dieleman, S., Zen, H., Simonyan, K., Vinyals, O., Graves, A., Kalchbrenner, N., Senior,

A., and Kavukcuoglu, K. (2016). WaveNet: A generative model for raw audio. CoRR, abs/1609.03499.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin,

I. (2017). Attention is all you need. CoRR.

Wu, Y., Schuster, M., Chen, Z., Le, Q. V., Norouzi, M., Macherey, W., Krikun, M., Cao, Y., Gao, Q.,

Macherey, K., et al. (2016). Google’s neural machine translation system: Bridging the gap between

---

[referencia=a15e6a70c6cf4a11 score=0.009]
4. Model: the model ties together the preceding components to instantiate the parameter-

ized transformation from inputs to targets, compute the loss and evaluation metrics, and

construct the optimization procedure.

5. Estimator and Experiment: These classes that are part of TensorFlow handle in-

stantiating the runtime, running the training loop, and executing basic support services like

model checkpointing, logging, and alternation between training and evaluation.

These abstractions enable users to focus their attention only on the component they’re

interested in experimenting with. Users that wish to try models on a new problem usually only

have to deﬁne a new problem. Users that wish to create or modify models only have to create

a model or edit hyperparameters. The other components remain untouched, out of the way, and

available for use, all of which reduces mental load and allows users to more quickly iterate on

their ideas at scale.

Appendix A contains an outline of the code and appendix B contains example usage.

5 Library of research components

Tensor2Tensor provides a vehicle for research ideas to be quickly tried out and shared. Compo-

nents that prove to be very useful can be committed to more widely-used libraries like Tensor-

Flow, which contains many standard layers, optimizers, and other higher-level components.

Tensor2Tensor supports library usage as well as script usage so that users can reuse speciﬁc

components in their own model or system. For example, multiple researchers are continuing

work on extensions and variations of the attention-based Transformer model and the availability

of the attention building blocks enables that work.

Some examples:

•The Image Transformer (Parmar et al., 2018) extends the Transformer model to images. It

relies heavily on many of the attention building blocks in Tensor2Tensor and adds many

of its own.

•tf.contrib.layers.rev block, implementing a memory-efﬁcient block of re-

versible layers as presented in Gomez et al. (2017), was ﬁrst implemented and exercised

in Tensor2Tensor.

•The Adafactor optimizer (pending publication), which signiﬁcantly reduces memory re-

quirements for second-moment estimates, was developed within Tensor2Tensor and tried

on various models and problems.

•tf.contrib.data.bucket by sequence length enables efﬁcient processing

of sequence inputs on GPUs in the new tf.data.Dataset input pipeline API. It was

ﬁrst implemented and exercised in Tensor2Tensor.

---

[referencia=a15e6a70c6cf4a11 score=0.005]
Macherey, K., et al. (2016). Google’s neural machine translation system: Bridging the gap between

human and machine translation. CoRR, abs/1609.08144.

Zhou, J., Cao, Y., Wang, X., Li, P., and Xu, W. (2016). Deep recurrent models with fast-forward connec-

tions for neural machine translation. CoRR, abs/1606.04199.

A Tensor2Tensor Code Outline

•Create HParams

•Create RunConfig specifying devices

–Create and include the Parallelism object in the RunConfig which enables data-parallel

duplication of the model on multiple devices (for example, for multi-GPU synchronous train-

ing).

•Create Experiment, including training and evaluation hooks which control support services like

logging and checkpointing

•Create Estimator encapsulating the model function

–T2TModel.estimator model fn

∗model(features)

·model.bottom: This uses feature type information from the Problem to transform

the input features into a form consumable by the model body (for example, embedding

integer token ids into a dense ﬂoat space).

·model.body: The core of the model.

·model.top: Transforming the output of the model body into the target space using

information from the Problem

·model.loss

∗When training: model.optimize

∗When evaluating: create evaluation metrics

•Create input functions

–Problem.input fn: produce an input pipeline for a given mode. Uses TensorFlow’s

tf.data.Dataset API.

∗Problem.dataset which creates a stream of individual examples

∗Pad and batch the examples into a form ready for efﬁcient processing

•Run the Experiment

–estimator.train

∗train op = model fn(input fn(mode=TRAIN))

∗Run the train op for the number of training steps speciﬁed

–estimator.evaluate

∗metrics = model fn(input fn(mode=EVAL))

∗Accumulate the metrics across the number of evaluation steps speciﬁed

B Example Usage

Tensor2Tensor usage is standardized across problems and models. Below you’ll ﬁnd a set of commands

that generates a dataset, trains and evaluates a model, and produces decodes from that trained model.

Experiments can typically be reproduced with the (problem, model, hyperparameter set) triple.

---

[referencia=a15e6a70c6cf4a11 score=0.004]
on various models and problems.

•tf.contrib.data.bucket by sequence length enables efﬁcient processing

of sequence inputs on GPUs in the new tf.data.Dataset input pipeline API. It was

ﬁrst implemented and exercised in Tensor2Tensor.

6 Reproducibility and Continuing Development

Continuing development on a machine learning codebase while maintaining the quality of mod-

els is a difﬁcult task because of the expense and randomness of model training. Freezing a

codebase to maintain a certain conﬁguration, or moving to an append-only process has enor-

mous usability and development costs.

We attempt to mitigate the impact of ongoing development on historical reproducibility

through 3 mechanisms:

1. Named and versioned hyperparameter sets in code

2. End-to-end regression tests that run on a regular basis for important model-problem pairs

and verify that certain quality metrics are achieved.

3. Setting random seeds on multiple levels (Python, numpy, and TensorFlow) to mitigate

the effects of randomness (though this is effectively impossible to achieve in full in a

multithreaded, distributed, ﬂoating-point system).

If necessary, because the code is under version control on GitHub

(http://github.com/tensorﬂow/tensor2tensor), we can always recover the exact code that

produced certain experiment results.

References

Abadi, M., Barham, P., Chen, J., Chen, Z., Davis, A., Dean, J., Devin, M., Ghemawat, S., Irving, G., Isard,

M., Kudlur, M., Levenberg, J., Monga, R., Moore, S., Murray, D. G., Steiner, B., Tucker, P., Vasudevan,

V., Warden, P., Wicke, M., Yu, Y., and Zheng, X. (2016). Tensorﬂow: A system for large-scale machine

learning. In 12th USENIX Symposium on Operating Systems Design and Implementation (OSDI 16),

pages 265–283.

Bahdanau, D., Cho, K., and Bengio, Y. (2014). Neural machine translation by jointly learning to align and

translate. CoRR, abs/1409.0473.

---

[referencia=a15e6a70c6cf4a11 score=0.003]
that generates a dataset, trains and evaluates a model, and produces decodes from that trained model.

Experiments can typically be reproduced with the (problem, model, hyperparameter set) triple.

The following train the attention-based Transformer model on WMT data translating from English

to German:

pip install tensor2tensor

PROBLEM=translate_ende_wmt32k

MODEL=transformer

HPARAMS=transformer_base

# Generate data

t2t-datagen \

--problem=$PROBLEM \

--data_dir=$DATA_DIR \

--tmp_dir=$TMP_DIR

# Train and evaluate

t2t-trainer \

--problems=$PROBLEM \

--model=$MODEL \

--hparams_set=$HPARAMS \

--data_dir=$DATA_DIR \

--output_dir=$OUTPUT_DIR \

--train_steps=250000

# Translate lines from a file

t2t-decoder \

--data_dir=$DATA_DIR \

--problems=$PROBLEM \

--model=$MODEL \

--hparams_set=$HPARAMS \

--output_dir=$OUTPUT_DIR \

--decode_from_file=$DECODE_FILE \

--decode_to_file=translation.en

---

[referencia=a15e6a70c6cf4a11 score=0.003]
Flow and various T2T-speciﬁc abstractions, researchers can train models on CPU, GPU (single

or multiple), and TPU, locally and in the cloud, usually with no or minimal device-speciﬁc code

or conﬁguration.

Development began focused on neural machine translation and so Tensor2Tensor includes

many of the most successful NMT models and standard datasets. It has since added support for

other task types as well across multiple media (text, images, video, audio). Both the number of

models and datasets has grown signiﬁcantly.

Usage is standardized across models and problems which makes it easy to try a new model

on multiple problems or try multiple models on a single problem. See Example Usage (appendix

B) to see some of the usability beneﬁts of standardization of commands and uniﬁcation of

datasets, models, and training, evaluation, decoding procedures.

Development is done in the open on GitHub (http://github.com/tensorﬂow/tensor2tensor)

with many contributors inside and outside Google.

4 System Overview

There are ﬁve key components that specify a training run in Tensor2Tensor:

1. Datasets: The Problem class encapsulate everything about a particular dataset. A

Problem can generate the dataset from scratch, usually downloading data from a pub-

lic source, building a vocabulary, and writing encoded samples to disk. Problems also

produce input pipelines for training and evaluation as well as any necessary additional

information per feature (for example, its type, vocabulary size, and an encoder able to

convert samples to and from human and machine-readable representations).

2. Device conﬁguration: the type, number, and location of devices. TensorFlow and Ten-

sor2Tensor currently support CPU, GPU, and TPU in single and multi-device conﬁgu-

rations. Tensor2Tensor also supports both synchronous and asynchronous data-parallel

training.

3. Hyperparameters: parameters that control the instantiation of the model and training pro-

cedure (for example, the number of hidden layers or the optimizer’s learning rate). These

are speciﬁed in code and named so they can be easily shared and reproduced.

4. Model: the model ties together the preceding components to instantiate the parameter-

ized transformation from inputs to targets, compute the loss and evaluation metrics, and

construct the optimization procedure.

---

[referencia=a15e6a70c6cf4a11 score=0.001]
which were written at 10-minute intervals. For the big models, we averaged the last 20 check-

points. We used beam search with a beam size of 4and length penalty α= 0.6(Wu et al.,

Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models

on the English-to-German and English-to-French newstest2014 tests at a fraction of the training

cost.

Model

BLEU Training Cost

(in FLOPS * 1018)

EN-DE EN-FR EN-DE EN-FR

ByteNet (Kalchbrenner et al., 2016) 23.75

Deep-Att + PosUnk (Zhou et al., 2016) 39.2 100

GNMT + RL (Wu et al., 2016) 24.6 39.92 23 140

ConvS2S (Gehring et al., 2017) 25.16 40.46 9.6 150

MoE (Shazeer et al., 2017) 26.03 40.56 20 120

GNMT + RL Ensemble (Wu et al., 2016) 26.30 41.16 180 1100

ConvS2S Ensemble (Gehring et al., 2017) 26.36 41.29 77 1200

Transformer (base model) 27.3 38.1 3.3

Transformer (big) 28.4 41.8 23

2016). These hyperparameters were chosen after experimentation on the development set. We

set the maximum output length during inference to input length + 50, but terminate early when

possible (Wu et al., 2016).

3 Tensor2Tensor

Tensor2Tensor (T2T) is a library of deep learning models and datasets designed to make deep

learning research faster and more accessible. T2T uses TensorFlow (Abadi et al., 2016) through-

out and there is a strong focus on performance as well as usability. Through its use of Tensor-

Flow and various T2T-speciﬁc abstractions, researchers can train models on CPU, GPU (single

or multiple), and TPU, locally and in the cloud, usually with no or minimal device-speciﬁc code