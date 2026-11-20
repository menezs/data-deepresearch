[referencia=4db29d6755eb1f84 score=0.000]
# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

## Abstract

A Vision Transformer outperforms leading convolutional networks on image classification tasks with reduced computational resources by directly applying a pure Transformer to sequences of image patches.

While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.

### Community

A good TL;DR on this in regards to SORA https://towardsdatascience.com/explaining-openai-soras-spacetime-patches-the-key-ingredient-e14e0703ec5b

arXiv explained breakdown of this paper 👉 https://arxivexplained.com/papers/an-image-is-worth-16x16-words-transformers-for-image-recognition-at-scale

Absolutely phenomenal, i'ts great to see more implementations of attention mechanisms on computer vision, at least it's becoming more frequent now!

Hello

Get this paper in your agent:

`hf papers read 2010.11929` ## Don't have the latest CLI?

`curl -LsSf https://hf.co/cli/install.sh | bash`