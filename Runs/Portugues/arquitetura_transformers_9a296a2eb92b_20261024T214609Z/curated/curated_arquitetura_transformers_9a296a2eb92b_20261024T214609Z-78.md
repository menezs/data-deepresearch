[referencia=bb174fbed3aeca2b score=0.524]
# RoFormer: Enhanced Transformer with Rotary Position Embedding

## Abstract

RoPE, a novel rotary position embedding method, enhances transformer-based language models by encoding positional information with a rotation matrix and relative position dependencies, leading to improved performance in long text classification tasks.

Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: https://huggingface.co/docs/transformers/model_doc/roformer.

### Community

---

[referencia=bb174fbed3aeca2b score=0.167]
# RoFormer: Transforming Transformers with Rotary Positional Embeddings

## Links 🔗:

👉 Subscribe: https://www.youtube.com/@Arxflix

👉 Twitter: https://x.com/arxflix

👉 LMNT (Partner): https://lmnt.com/

@librarian-bot recommend

This is an automated message from the Librarian Bot. I found the following papers similar to this paper.

The following papers were recommended by the Semantic Scholar API

- VRoPE: Rotary Position Embedding for Video Large Language Models (2025)
- Sliding Window Attention Training for Efficient Large Language Models (2025)
- Context-aware Biases for Length Extrapolation (2025)
- Training Sparse Mixture Of Experts Text Embedding Models (2025)
- HaploVL: A Single-Transformer Baseline for Multi-Modal Understanding (2025)
- Neural Attention: A Novel Mechanism for Enhanced Expressive Power in Transformer Models (2025)
- Forgetting Transformer: Softmax Attention with a Forget Gate (2025)

Please give a thumbs up to this comment if you found it helpful!

If you want recommendations for any Paper on Hugging Face checkout this Space

 You can directly ask Librarian Bot for paper recommendations by tagging it in a comment: `@librarian-bot recommend`

Get this paper in your agent:

`hf papers read 2104.09864` ## Don't have the latest CLI?

`curl -LsSf https://hf.co/cli/install.sh | bash`