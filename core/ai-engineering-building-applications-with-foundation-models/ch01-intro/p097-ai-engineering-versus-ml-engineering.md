---
id: C01-021
title: AI Engineering Versus ML Engineering
source_pages: "97-111"
chapter: 1
concepts: [ai-engineering, ml-engineering, model-adaptation, prompt-engineering, finetuning, dataset-engineering, inference-optimization, evaluation, ai-interface, pre-training, post-training]
related: [C01-019, C01-020, C01-022, C01-023]
time_sensitive: true
---
# AI Engineering Versus ML Engineering
(Source: PDF pp. 97-111)

## What the section covers
How building on foundation models differs from classical ML engineering: three high-level differences, the two families of model adaptation (prompt-based versus finetuning), then a walk through the model development layer (modeling and training, dataset engineering, inference optimization) and the application development layer (evaluation, prompt engineering and context construction, AI interface), including terminology about training, pre-training, finetuning and post-training.

## Meaning: why compare
- The enduring principles of deploying AI applications are reassuring, but it is also important to see what has changed. The comparison helps teams that want to adapt existing platforms to new AI use cases and developers deciding which skills to learn to stay competitive in a new market (PDF p. 97). The preceding section (C01-020) covers the ML engineering practices that carry over.

## The three major differences
1. No need to train your own model: you use one trained by someone else, so the work is less about modeling and training and more about model adaptation (PDF p. 98).
2. Models are bigger, consume more compute and have higher latency, creating pressure for efficient training and inference optimization. A corollary is that many companies need more GPUs and larger clusters than before, so engineers who can work with GPUs and big clusters are in demand (PDF p. 98).
3. Models give open-ended outputs, which makes them flexible across tasks but harder to evaluate, so evaluation becomes a much bigger problem (PDF p. 98).
In short: less model development, more adaptation and evaluation (PDF p. 98).

## Model adaptation: two categories
Divided by whether weights are updated (PDF p. 98).
- Prompt-based techniques (including prompt engineering) adapt a model with instructions and context, leaving weights untouched. They are easier to start, need less data, and many successful applications rely on them alone. Their ease lets you try more models, raising the chance of finding one that is unexpectedly good. They may be insufficient for complex tasks or strict performance requirements (PDF p. 99).
- Finetuning changes the weights. It is more complicated and needs more data but can improve quality, latency and cost significantly. Some things, such as adapting a model to a task it never saw in training, are impossible without changing weights (PDF p. 99).

## Model development layer
The layer most associated with traditional ML engineering has three responsibilities: modeling and training, dataset engineering, inference optimization. Evaluation is also needed but is discussed under application development because most people meet it there first (PDF p. 100).

### Modeling and training
- Covers designing a model architecture, training it and finetuning it; tools named include TensorFlow, Hugging Face Transformers and PyTorch (PDF p. 100).
- Classically it demands knowledge of algorithms (clustering, logistic regression, decision trees, collaborative filtering), network architectures (feedforward, recurrent, convolutional, transformer) and learning concepts (gradient descent, loss function, regularization) (PDF p. 100).
- With foundation models, ML knowledge is no longer a must-have; the author has met successful builders uninterested in gradient descent. It remains valuable because it widens the toolset and helps troubleshoot unexpected behavior (PDF pp. 100-101). Table 1-4 flags that many people dispute the "nice-to-have" claim and consider ML knowledge a must (PDF p. 106).

### Training, pre-training, finetuning, post-training (sidebar)
- Training always changes weights, but not every weight change is training: quantization (lowering weight precision) changes values but is not training (PDF p. 102).
- Pre-training: training from scratch with randomly initialized weights; for LLMs usually text completion. It is by far the most resource-intensive step; for InstructGPT it took up to 98% of the total compute and data. A small mistake can cause large financial loss and delay, so few practice it and experts are heavily sought (PDF p. 102).
- Finetuning: continuing to train a previously trained model, so weights come from earlier training. It needs fewer resources than pre-training because the model already has knowledge (PDF pp. 102-103).
- Post-training: training after pre-training. Conceptually the same as finetuning and interchangeable, but by usage it is "post-training" when model developers do it (e.g., OpenAI improving instruction following before release) and "finetuning" when application developers do it (PDF p. 103).
- Pre-training and post-training form a spectrum with very similar processes and tooling; later chapters 2 and 7 explore the differences (PDF p. 103).
- Calling prompt engineering "training" is technically incorrect. The example is a writer who "trained ChatGPT" by feeding it her journals; teaching via context input is prompt engineering. Some people likewise say finetuning when they mean prompt engineering (PDF pp. 103-104).

### Dataset engineering
- Curating, generating and annotating data needed to train and adapt models (PDF p. 104).
- Traditional ML use cases are mostly close-ended (output within predefined values, e.g., spam or not spam); foundation models are open-ended. Annotating open-ended queries is much harder (it is easier to judge whether an email is spam than to write an essay), so annotation is a bigger challenge (PDF p. 104).
- Traditional ML mostly uses tabular data; foundation models use unstructured data. Data work becomes deduplication, tokenization, context retrieval and quality control, including removing sensitive and toxic data (PDF p. 104). Chapter 8 is the focus (PDF p. 104).
- Argument that models are commodities so data is the differentiator. Data needs scale by technique: training from scratch needs more than finetuning, which needs more than prompt engineering. Data expertise also helps in examining a model, since training data hints at its strengths and weaknesses (PDF p. 105).

### Inference optimization
- Making models faster and cheaper; always important, even more so as foundation models raise cost and latency (PDF p. 105).
- Autoregressive generation is sequential: at 10 ms per token, 100 tokens take one second. Reaching the roughly 100 ms latency of a typical internet application is a huge challenge, and the area is now an active subfield in industry and academia (PDF pp. 105-106).
- Table 1-4 summary (PDF p. 106): modeling and training goes from ML knowledge required to train from scratch to nice-to-have; dataset engineering goes from mostly feature engineering (especially tabular) to less feature engineering and more deduplication, tokenization, context retrieval and quality control; inference optimization goes from important to even more important.
- Techniques such as quantization, distillation and parallelism are discussed in chapters 7 through 9 (PDF p. 107).

## Application development layer
- With proprietary models, model quality is the differentiator in traditional ML. When many teams use the same foundation model, differentiation has to come from the application development process (PDF p. 107).
- Responsibilities: evaluation, prompt engineering, AI interface (PDF p. 107).

### Evaluation
- About mitigating risks and uncovering opportunities, needed throughout adaptation: selecting models, benchmarking progress, deciding deployment readiness, and detecting production issues and improvement opportunities (PDF p. 107).
- Harder with foundation models because of open-ended outputs and expanded capabilities (chapter 3). In close-ended tasks like fraud detection there are expected ground truths to compare against; for a chatbot there are too many valid responses to curate an exhaustive list (PDF pp. 107-108).
- Many adaptation techniques complicate things: a system weak under one technique may be much better under another (PDF p. 108).
- Example: Google's December 2023 Gemini launch claimed to beat ChatGPT on MMLU, but evaluated Gemini with CoT@32 (32 examples shown) while ChatGPT got 5. With five examples each, ChatGPT performed better (PDF p. 108). Table 1-5 lists MMLU results: Gemini Ultra 90.04% (CoT@32) versus 83.7% (5-shot); Gemini Pro 79.13% (CoT@8) versus 71.8% (5-shot); GPT-4 87.29% (CoT@32, via API) versus 86.4% (5-shot, reported); a fourth column headed "GPT-" shows 70% with "5-sho" in its first row and nothing visible in its second row (PDF p. 109). The table is clipped at the right edge in the PDF, as is its caption. UNVERIFIED: the full header of that fourth column, the rest of its entries, and any further columns; only the legible text is recorded.

### Prompt engineering and context construction
- Prompt engineering aims to elicit desired behavior from the input alone, without changing weights. The Gemini story shows its impact: a different technique moved Gemini Ultra from 83.7% to 90.04% on MMLU (PDF p. 109).
- It is more than instructions: it includes supplying context and tools, and for complex long-context tasks a memory management system so the model can track history. Chapter 5 covers prompt engineering and chapter 6 context construction (PDF pp. 109-110).

### AI interface
- Creating the interface through which end users reach the application. Before foundation models, only organizations able to build models could build AI applications, usually embedded in existing products (fraud detection in Stripe, Venmo, PayPal; recommenders in Netflix, TikTok, Spotify) (PDF p. 110).
- Now anyone can build one, as a standalone product or embedded into others' products. Examples: ChatGPT and Perplexity standalone; GitHub Copilot as a VSCode plug-in; Grammarly as a browser extension for Google Docs; Midjourney via web app or Discord (PDF p. 110).
- Popular interfaces: standalone web, desktop and mobile apps; browser extensions; chatbots in Slack, Discord, WeChat, WhatsApp; and plug-in/add-on APIs from products like VSCode, Shopify and Microsoft 365, which AI agents can also use (chapter 6) (PDF pp. 110-111).
- Chat is most common, but interfaces can be voice-based or embodied (AR/VR) (PDF p. 111).
- New interfaces change feedback collection: conversation makes natural-language feedback easy to give but harder to extract; user feedback design is in chapter 10 (PDF p. 111).
- A summary of how application-development categories change is given in Table 1-6 (PDF p. 111). The table itself is printed at the top of the next page and is described in C01-022: AI interface less important to important, prompt engineering not applicable to important, evaluation important to more important.

## Relations
Follows the three-layer stack overview (C01-019, C01-020); the comparison with full-stack engineering is in C01-022; chapter wrap-up in C01-023.

## Time-sensitive statements
The Gemini/ChatGPT MMLU comparison and the tool and product names are as of the book's writing (2023-2024) (PDF pp. 108-110).
