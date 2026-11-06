---
id: C03-012
title: Introduction to Embedding
source_pages: "267-270"
chapter: 3
concepts: [embedding, embedding-vector, embedding-size, bert, clip, joint-embedding, multimodal-embedding, mteb, cosine-similarity]
related: [C03-011, C03-013]
time_sensitive: true
---
# Introduction to Embedding
(Source: PDF pp. 267-270, with the end of the section on tail page 271)

## What the section covers
A short primer on embeddings, which underpin semantic similarity: what an embedding is, typical sizes and models, how embedding quality is judged, embeddings for non-text data, and joint (multimodal) embedding spaces such as CLIP.

## Meaning
- Computers work with numbers, so a model must convert input into numerical representations. An embedding is a numerical representation meant to capture the meaning of the original data (PDF p. 267).
- An embedding is a vector. The sentence "the cat sits on a mat" might become [0.11, 0.02, 0.54]; this is a toy size. Real embedding vectors typically have 100 to 10,000 elements (PDF p. 267).
- Models trained specifically to produce embeddings include open source BERT, CLIP (Contrastive Language-Image Pre-training) and Sentence Transformers, plus proprietary embedding models offered as APIs (PDF p. 267).

## How it works
- Table 3-2 (PDF p. 268) gives embedding sizes: Google BERT base 768 and BERT large 1024; OpenAI CLIP 512 for images and 512 for text; OpenAI Embeddings API text-embedding-3-small 1536 and text-embedding-3-large 3072; Cohere Embed v3 embed-english-v3.0 1024 and embed-english-light-3.0 384.
- Many ML models, including GPTs and Llamas, also have a step that creates embeddings, because inputs must first become vectors. The transformer embedding layer is shown in the earlier "Transformer architecture" discussion. If you can access intermediate layers of such models you can extract embeddings, but their quality may be worse than that of specialized embedding models (PDF p. 268).
- The goal of an embedding algorithm is embeddings that capture the essence of the data. This is not checkable by eye, since [0.11, 0.02, 0.54] looks nothing like the text (PDF pp. 268-269).

## Evaluation and success criteria
- At a high level, an embedding algorithm is good if more-similar texts get closer embeddings, measured by cosine similarity or related metrics. The embedding of "the cat sits on a mat" should be nearer to that of "the dog plays on the grass" than to that of "AI research is super fun" (PDF p. 269).
- Embeddings can also be judged by usefulness on your task. They serve classification, topic modeling, recommender systems and RAG. MTEB (Massive Text Embedding Benchmark; Muennighoff et al., 2023) measures embedding quality across multiple tasks (PDF p. 269).

## Beyond text
- Any data can be embedded. Ecommerce companies such as Criteo and Coveo have product embeddings; Pinterest has embeddings for images, graphs, queries and even users (PDF p. 269).
- A newer frontier is joint embeddings across modalities. CLIP (Radford et al., 2021) was among the first major models to map text and images into one joint embedding space. ULIP (Xue et al., 2022) aims for unified representations of text, images and 3D point clouds. ImageBind (Girdhar et al., 2023) learns a joint embedding across six modalities, including text, images and audio (PDF pp. 269-270).

### CLIP architecture
- CLIP trains on (image, text) pairs; the text may be a caption or a comment tied to the image. For each pair a text encoder makes a text embedding and an image encoder makes an image embedding; both are projected into a joint embedding space. The training goal is to put an image's embedding close to its matching text's embedding in that space (PDF p. 270).
- Figure 3-6 (viewed on the rendered page, PDF p. 270) diagrams this: the text "Happy hippie hamster" goes through a text encoder, and a picture of a hamster goes through an image encoder, giving a text embedding and an image embedding. A language projection matrix W_l (D_e x D_l) and a vision projection matrix W_v (D_e x D_v) map each into a multimodal embedding of text and of image, and a cosine similarity score compares them.
- A joint space for several modalities is a multimodal embedding space. In a text-image joint space, an image of a man fishing should be nearer to the text "a fisherman" than to "fashion show". This lets embeddings of different modalities be compared and combined, for example for text-based image search: given a text, find the closest images (PDF p. 271, tail page).

## Relations
- Supplies the "embedding" that semantic similarity in C03-011 assumes. Embeddings return in vector search (Chapter 6) and data deduplication (Chapter 8), as noted in C03-011.
- Followed by the AI as a judge section (C03-013).

## Time-sensitive statements
- The model names and embedding sizes in Table 3-2, and the list of embedding models, reflect the date of writing.
