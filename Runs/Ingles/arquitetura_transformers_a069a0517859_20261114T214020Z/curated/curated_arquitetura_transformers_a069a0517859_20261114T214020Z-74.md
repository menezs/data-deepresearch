[referencia=83ddb21bf38bcb8a score=0.994]
### **Reducing memory needs, expanding accessibility**

One of Granite 4.0’s defining features is its ability to significantly reduce GPU memory consumption compared to traditional large language models.

IBM reports that the hybrid Mamba-transformer design can cut RAM requirements by more than 70% (!!!) in production environments, especially for workloads involving long contexts and multiple concurrent sessions.

Benchmarks released alongside the launch illustrate these improvements.

Granite-4.0-H-Small, a 32B-parameter mixture-of-experts model with 9B active parameters, maintains strong throughput on a single NVIDIA H100 GPU, continuing to accelerate even under workloads that typically strain transformer-only systems.

This efficiency translates directly into lower hardware costs for enterprises running intensive inference tasks.

For smaller-scale or edge deployments, Granite 4.0 offers two lighter options: Granite-4.0-H-Tiny, a 7B-parameter hybrid with 1B active parameters, and Granite-4.0-H-Micro, a 3B dense hybrid. IBM is also releasing Granite-4.0-Micro, a 3B transformer-only model intended for platforms not yet optimized for Mamba-based architectures.

### **Performance benchmarks**

Performance metrics suggest that the new models not only reduce costs but also compete with larger systems on enterprise-critical tasks.

According to Stanford HELM’s IFEval benchmark, which measures how well LLMs follow instructions from users, Granite-4.0-H-Small surpasses nearly all open weight models in instruction-following accuracy, ranking just behind Meta’s much larger Llama 4 Maverick.

The models also show strong results on the Berkeley Function Calling Leaderboard v3, where Granite-4.0-H-Small achieves a favorable trade-off between accuracy and hosted API pricing. On retrieval-augmented generation tasks, Granite 4.0 models post some of the highest mean accuracy scores among open competitors.

Notably, IBM highlights that even Granite 4.0’s smallest models outperform Granite 3.3 8B, despite being less than half its size, underscoring the gains achieved through both architectural changes and refined training methods.

---

[referencia=83ddb21bf38bcb8a score=0.796]
### **What Granite 4.0 means for enterprises and what's next**

Granite 4.0 reflects IBM’s strategy of combining open access with enterprise-grade safety, scalability, and efficiency. By focusing on lowering inference costs and reinforcing trust with governance standards, IBM positions the Granite family as a practical foundation for enterprises building AI applications at scale.

For the U.S., the release carries symbolic weight: with Meta stepping back from leading the open-weight frontier after the uneven reception of Llama 4, and with Alibaba’s Qwen family rapidly advancing in China, IBM’s move positions American enterprise once again as a competitive force in globally available models.

By making Granite 4.0 Apache-licensed, cryptographically signed, and ISO 42001-certified, IBM is signaling both openness and responsibility at a moment when trust, efficiency, and affordability are top of mind. This is especially enticing to U.S. and Western-based organizations who may be interested in open source models, but wary of those originating from China — rightly or not — over possible political ramifications and U.S. government contracts.

For practitioners inside organizations, this positioning is not abstract. Lead AI engineers tasked with managing the full lifecycle of LLMs will see Granite 4.0’s smaller memory footprint as a way to deploy faster and scale with leaner teams.

Senior AI engineers in orchestration roles, who must balance budget limits with the need for efficiency, can take advantage of Granite’s compatibility with mainstream platforms like SageMaker and Hugging Face to streamline pipelines without locking into proprietary ecosystems.

Senior data engineers, responsible for integrating AI with complex data systems, will note the hybrid models’ efficiency on long-context inputs, enabling retrieval-augmented generation on large datasets at lower cost.

And for IT security directors charged with managing day-to-day defense, IBM’s bug bounty program, cryptographic signing, and ISO accreditation provide clear governance signals that align with enterprise compliance needs.

By targeting these distinct roles with a model family that is efficient, open, and hardened for enterprise use, IBM is not only courting adoption but also shaping a uniquely American answer to the open-source challenge posed by Qwen and other Chinese entrants. In doing so, Granite 4.0 places IBM at the center of a new phase in the global LLM race — one defined not just by size and speed, but by trust, cost efficiency, and readiness for real-world deployment.

---

[referencia=83ddb21bf38bcb8a score=0.706]
### **Trust, safety, and security**

Alongside technical efficiency, IBM is emphasizing governance and trust. Granite is the first open model family to achieve ISO/IEC 42001:2023 certification, demonstrating compliance with international standards for AI accountability, data privacy, and explainability.

The company has also partnered with HackerOne to run a bug bounty program for Granite, offering up to $100,000 for vulnerabilities that could expose security flaws or adversarial risks. Additionally, every Granite 4.0 model checkpoint is cryptographically signed, enabling developers to verify provenance and integrity before deployment.

IBM provides indemnification for customers using Granite on its watsonx.ai platform, covering third-party intellectual property claims against AI-generated content.

### **Training and roadmap**

Granite 4.0 models were trained on a 22-trillion-token corpus sourced from enterprise-relevant datasets including DataComp-LM, Wikipedia, and curated subsets designed to support language, code, math, multilingual tasks, and cybersecurity.

Post-training is split between instruction-tuned models, released today, and reasoning-focused “Thinking” variants, which are expected later this fall.

IBM plans to expand the family by the end of 2025 with additional models, including Granite 4.0 Medium for heavier enterprise workloads and Granite 4.0 Nano for edge deployments.

### **Broad availability across platforms**

Granite 4.0 models are available immediately on Hugging Face, IBM watsonx.ai, with distribution also through partners such as Dell Technologies, Docker Hub, Kaggle, LM Studio, NVIDIA NIM, Ollama, OPAQUE, and Replicate.

Support through Amazon SageMaker JumpStart and Microsoft Azure AI Foundry is expected soon.

The hybrid architecture is supported in major inference frameworks, including vLLM 0.10.2 and Hugging Face Transformers.

Compatibility has also been extended to llama.cpp and MLX, although optimization work is ongoing. The models are also usable in Unsloth for fine-tuning and in Continue for custom AI coding assistants.

### **Enterprise focus**

Early access testing by enterprise partners, including EY and Lockheed Martin, has guided the launch.

IBM highlights that the models are tailored for real-world enterprise needs, such as supporting multi-agent workflows, customer support automation, and large-scale retrieval systems.

Granite 4.0 models are available in both Base and Instruct forms, with Instruct variants optimized for enterprise instruction-following tasks. The upcoming “Thinking” series will target advanced reasoning.

---

[referencia=83ddb21bf38bcb8a score=0.468]
### **Hybrid (Transformer/Mamba) theory**

At the heart of IBM's Granite 4.0 release is a new hybrid design that combines two very different architectures, or underlying organizational structures, for the LLMs in question: transformers and Mamba.

Transformers, introduced in 2017 by Vaswani and colleagues in the famous Google paper “Attention Is All You Need,” power most large language models in use today.

In this design, every token — essentially a small chunk of text, like a word or part of a word — can compare itself to every other token in the input. This “all-to-all” comparison is what gives transformers their strong ability to capture context and meaning across a passage.

The trade-off is efficiency: because the model must calculate relationships between every possible pair of tokens in the context window, computation and memory demands grow rapidly as the input gets longer. This quadratic scaling makes transformers costly to run on very long documents or at high volume.

Mamba, by contrast, is a newer architecture developed in late 2023 by researchers Albert Gu and Tri Dao at Carnegie Mellon University and Princeton University. Instead of comparing every token against all the others at once, it processes tokens one at a time, updating its internal state as it moves through the sequence. This design scales only linearly with input length, making it far more efficient at handling long documents or multiple requests at once. The trade-off is that transformers still tend to perform better in certain kinds of reasoning and “few-shot” learning, where it helps to hold many detailed token-to-token comparisons in memory.

This enables much greater efficiency, especially for long documents or multi-session inference, though transformers retain advantages for some reasoning and few-shot learning tasks.

---

[referencia=83ddb21bf38bcb8a score=0.359]
IBM today announced the release of Granite 4.0, the newest generation of its homemade family of open source large language models (LLMs) designed to balance high performance with lower memory and cost requirements.

Despite being one of the oldest active tech companies in the U.S. (founded in 1911, 114 years ago!), "Big Blue" as its often nicknamed has already wowed many AI industry workers and followers with this new Granite 4.0 family of LLMs, as they offer high performance on third-party benchmarks; a permissive, business friendly license (Apache 2.0) that allows developers and enterprises to freely take, modify and deploy the models for their own commercial purposes; and, perhaps most importantly, have symbolically put the U.S. back into a competitive place with the growing raft of high-performing new generation open source Chinese LLMs, especially from Alibaba's prolific Qwen team — alongside OpenAI with its gpt-oss model family released earlier this summer.

Meta, the parent company of Facebook and Instagram, was once seen as the world and U.S. leader of open source LLMs with its Llama models, but after the disappointing release of the Llama 4 family in April and lack of its planned, most powerful Llama 4 Behemoth, it has since pursued a different strategy and is now partnering with outside labs like Midjourney on AI products, while it continues to build out an expensive, in-house AI "Superintelligence" team, as well.

Little wonder AI engineer Alexander Doria (aka Pierre-Carl Langlais) observed, with a hilarious *Lethal Weapon* meme, that "ibm suiting up again after llama 4 fumbled," and "we finally have western qwen."

---

[referencia=83ddb21bf38bcb8a score=0.354]
This enables much greater efficiency, especially for long documents or multi-session inference, though transformers retain advantages for some reasoning and few-shot learning tasks.

But whether the model is built on transformers, Mamba, or a hybrid of the two, the way it generates new words works the same way. At each step, the model doesn’t just pick from what’s already in the context window. Instead, it uses its internal weights — built from training on trillions of text samples — to predict the most likely next token from its entire vocabulary. That’s why, when prompted with “The capital of France is…,” the model can output “Paris” even if “Paris” isn’t in the input text. It has learned from countless training examples that “Paris” is a highly probable continuation in that context. In other words, the context window guides the prediction, but the embedding space — the model’s learned representation of all tokens it knows — supplies the actual words it can generate.

**By combining Mamba-2 layers with transformer blocks, Granite 4.0 seeks to offer the best of both worlds: the efficiency of Mamba and the contextual precision of transformers.**

This is the first official Granite release to adopt the hybrid approach. IBM previewed it earlier in 2025 with the Granite-4.0-Tiny-Preview, but Granite 4.0 marks the company’s first full family of models built on the Mamba-transformer combination.

Granite 4.0 is being positioned as an enterprise-ready alternative to conventional transformer-based models, with particular emphasis on agentic AI tasks such as instruction following, function calling, and retrieval-augmented generation (RAG). The models are open sourced under the Apache 2.0 license, cryptographically signed for authenticity, and stand out as the first open language model family certified under ISO 42001, an international standard for AI governance and transparency.

---

[referencia=83ddb21bf38bcb8a score=0.056]
With additional models scheduled for release before the end of the year and broader availability across major AI development platforms, Granite 4.0 is set to play a central role in IBM’s vision of enterprise-ready, open-source AI.

---

[referencia=83ddb21bf38bcb8a score=0.027]
### **Alternate hybrid Mamba / Transformer models**

Besides IBM, several major efforts are already charting different designs for mixing Transformers with Mamba architecture:

| Model | Hybrid strategy / architecture | Highlights | 
| **AI21 Jamba** | Interleaves Transformer blocks and Mamba layers, with Mixture-of-Experts (MoE) in some layers | Supports context lengths up to 256K tokens and offers higher throughput and lower memory usage than pure Transformers while maintaining competitive benchmarks | 
| **Nvidia Nemotron-H** | Replaces most attention layers with Mamba-2 blocks, retaining a few attention layers where needed | Demonstrates up to 3× faster inference throughput compared to pure-Transformer peers while keeping benchmark accuracy comparable | 
| **Nemotron-Nano-2** | A reasoning-optimized hybrid built on Nemotron’s design | Reports up to 6× throughput improvement on reasoning tasks while matching or surpassing accuracy | 
| **Domain-specific variants** | Hybridized architectures in multimodal models, such as swapping in Mamba layers for decoder components | Shows that the hybrid approach extends beyond text into vision-language applications | 

The Qwen family from Alibaba remains a dense, decoder-only Transformer architecture, with no Mamba or SSM layers in its mainline models. However, experimental offshoots like Vamba-Qwen2-VL-7B show that hybrids derived from Qwen are possible, especially in vision-language settings. For now, though, Qwen itself is not part of the hybrid wave.