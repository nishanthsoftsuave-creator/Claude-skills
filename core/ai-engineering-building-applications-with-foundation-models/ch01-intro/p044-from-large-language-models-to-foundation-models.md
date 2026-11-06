---
id: C01-003
title: From Large Language Models to Foundation Models
source_pages: "44-50"
chapter: 1
concepts: [foundation-model, multimodal-model, large-multimodal-model, clip, natural-language-supervision, general-purpose-models, prompt-engineering, rag, finetuning, buy-or-build]
related: [C01-001, C01-002, C01-004]
time_sensitive: true
---
# From Large Language Models to Foundation Models
(Source: PDF pp. 44-50)

## What the section covers
How language models were extended beyond text into multiple data modalities, why the result is better called a foundation model, how CLIP and natural language supervision let multimodal models scale, the shift from task-specific to general-purpose models, and the three common adaptation techniques (prompt engineering, RAG, finetuning) with the build-versus-adapt trade-off.

## Why go beyond text
Language models are limited to text, yet humans perceive the world through vision, hearing, touch and more, so handling non-text data is essential for AI operating in the real world (PDF p. 44). Language models are therefore being extended with more modalities: GPT-4V and Claude 3 understand images and text, and some models handle video, 3D assets, protein structures and more (PDF p. 44). More modalities make models more powerful. The book cites OpenAI's 2023 GPT-4V system card, which says adding modalities such as image input to LLMs is viewed by some as a key frontier in AI research (PDF pp. 44-45).

## Meaning
- Foundation model: Gemini and GPT-4V are still often called LLMs but are better described as foundation models. "Foundation" signals both their importance to AI applications and that they can be built upon for different needs (PDF p. 45).
- The breakthrough is structural. AI research was long split by data modality: natural language processing (text only), computer vision (vision only). Text-only models serve translation and spam detection; image-only models serve object detection and classification; audio-only models handle speech recognition (speech-to-text, STT) and speech synthesis (text-to-speech, TTS) (PDF p. 45).
- A multimodal model works with more than one modality. A generative multimodal model is a large multimodal model (LMM). Where a language model generates the next token conditioned on text tokens only, a multimodal model conditions on text and image tokens, or whatever modalities it supports (PDF p. 45). Figure 1-3 shows text tokens ("This is a") and a visual token (a picture of a puppy) entering a multimodal model that outputs the next token "Puppy" (PDF p. 46).
- Terminology in this book: "foundation models" covers both LLMs and LMMs (PDF p. 47).

## How it works: scaling multimodal models
- Multimodal models also need data to scale, and self-supervision works for them too (PDF p. 46).
- Example, CLIP (OpenAI, 2021): trained with a variant called natural language supervision. Instead of hand-labeling images, OpenAI found (image, text) pairs that co-occur on the internet, producing 400 million pairs, 400 times the size of ImageNet, at no manual labeling cost. This made CLIP the first model that could generalize to multiple image classification tasks without additional training (PDF p. 46).
- CLIP is not generative; it was not trained to produce open-ended outputs. It is an embedding model that produces joint embeddings of text and images. For now embeddings can be thought of as vectors meant to capture the meaning of the original data (the book points to a later section on embeddings). Multimodal embedding models like CLIP are the backbone of generative multimodal models such as Flamingo, LLaVA and Gemini (previously Bard) (PDF p. 47).

## From task-specific to general-purpose
- Previously models were built for specific tasks like sentiment analysis or translation, and a sentiment model could not translate. Foundation models, thanks to scale and training method, handle a wide range of tasks and work relatively well out of the box on many. An LLM can do both sentiment analysis and translation, though a general-purpose model can often be tweaked to maximize performance on a specific task (PDF p. 47).
- Figure 1-4 displays the many tasks of the Super-NaturalInstructions benchmark (Wang et al., 2022) as a bubble chart; translation, question answering, sentiment analysis, question generation, program execution, text categorization and many smaller categories appear. It conveys the breadth of tasks a foundation model can be asked to do (PDF pp. 47-49).

## When and how to apply: adapting a model
- Worked scenario: building a product-description generator for a retailer. An out-of-the-box model may write accurate descriptions yet miss the brand voice or messaging, and may be full of marketing speech and cliches (PDF p. 48).
- Three adaptation techniques, each tackling that gap (PDF pp. 49-50):
  1. Prompt engineering: craft detailed instructions with examples of desirable descriptions.
  2. Retrieval-augmented generation (RAG): connect the model to a database, such as customer reviews, to supplement the instructions.
  3. Finetuning: further train the model on a dataset of high-quality product descriptions.
- The book calls these three very common AI engineering techniques for adapting a model to your needs; the rest of the book discusses each in detail (PDF p. 50).

## Alternatives and trade-offs
- Adapting an existing powerful model is generally far easier than building one from scratch, with the illustration of ten examples and one weekend versus 1 million examples and six months. Foundation models thus lower the cost of building AI applications and shorten time to market. How much data adaptation needs depends on the technique, covered per technique later (PDF p. 50).
- Task-specific models still have benefits; for instance they can be much smaller, hence faster and cheaper to use (PDF p. 50).
- Whether to build your own model or use an existing one is a classic buy-or-build decision each team must make; the book's discussions are meant to inform it (PDF p. 50).

## Time-sensitive statements
- Model examples (GPT-4V, Claude 3, Gemini, Flamingo, LLaVA, CLIP) and their capabilities reflect the time of writing (PDF pp. 44-47).
- The ten examples/one weekend versus 1 million examples/six months comparison is an illustration, not a measured figure (PDF p. 50).

## Relations
Builds on C01-002 (language models, tokens, self-supervision) and the chapter framing in C01-001. Prompt engineering, RAG and finetuning are expanded in later chapters; C01-004 continues Chapter 1.
