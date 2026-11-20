[referencia=7616a9236ed354b5 score=0.552]
## Abstract

DeepSeek-V3 is a parameter-efficient Mixture-of-Experts language model using MLA and DeepSeekMoE architectures, achieving high performance with efficient training and minimal computational cost.

We present DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2. Furthermore, DeepSeek-V3 pioneers an auxiliary-loss-free strategy for load balancing and sets a multi-token prediction training objective for stronger performance. We pre-train DeepSeek-V3 on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages to fully harness its capabilities. Comprehensive evaluations reveal that DeepSeek-V3 outperforms other open-source models and achieves performance comparable to leading closed-source models. Despite its excellent performance, DeepSeek-V3 requires only 2.788M H800 GPU hours for its full training. In addition, its training process is remarkably stable. Throughout the entire training process, we did not experience any irrecoverable loss spikes or perform any rollbacks. The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V3.

### Community

Cool TL:DR here https://x.com/rm_rafailov/status/1877446475271037314

Please make me an anime music

convolution in matlab signal analysis

عالی

Hermoso

Get this paper in your agent:

`hf papers read 2412.19437` ## Don't have the latest CLI?

`curl -LsSf https://hf.co/cli/install.sh | bash`