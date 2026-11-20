[referencia=981cecee682065a2 score=0.989]
# Longformer: The Long-Document Transformer

## Abstract

The Longformer addresses the limitations of transformer-based models for long sequences through a linearly scaling attention mechanism, achieving state-of-the-art results in both language modeling and document-based tasks.

Transformer-based models are unable to process long sequences due to their self-attention operation, which scales quadratically with the sequence length. To address this limitation, we introduce the Longformer with an attention mechanism that scales linearly with sequence length, making it easy to process documents of thousands of tokens or longer. Longformer's attention mechanism is a drop-in replacement for the standard self-attention and combines a local windowed attention with a task motivated global attention. Following prior work on long-sequence transformers, we evaluate Longformer on character-level language modeling and achieve state-of-the-art results on text8 and enwik8. In contrast to most prior work, we also pretrain Longformer and finetune it on a variety of downstream tasks. Our pretrained Longformer consistently outperforms RoBERTa on long document tasks and sets new state-of-the-art results on WikiHop and TriviaQA. We finally introduce the Longformer-Encoder-Decoder (LED), a Longformer variant for supporting long document generative sequence-to-sequence tasks, and demonstrate its effectiveness on the arXiv summarization dataset.

Get this paper in your agent:

`hf papers read 2004.05150` ## Don't have the latest CLI?

`curl -LsSf https://hf.co/cli/install.sh | bash`