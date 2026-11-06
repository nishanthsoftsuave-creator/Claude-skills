---
id: C06-005
title: Retrieval Optimization
source_pages: "520-529"
chapter: 6
concepts: [retrieval-optimization, chunking-strategy, chunk-overlap, reranking, query-rewriting, contextual-retrieval, retrieval-evaluation]
related: [C06-004, C06-006, C06-003]
time_sensitive: false
---
# Retrieval Optimization
(Source: PDF pp. 520-529; the box "Evaluating Retrieval Solutions" at the top of PDF p. 530 closes this section, and the lines below the "RAG Beyond Texts" heading on that page belong to C06-006. The reciprocal rank fusion text at the top of PDF p. 520 belongs to the previous section, C06-004.)

## What the section covers
Four tactics that raise the chance that relevant documents are fetched in a RAG system: chunking strategy, reranking, query rewriting, and contextual retrieval (PDF p. 520). A closing box lists factors for evaluating a retrieval solution (PDF p. 530).

## Chunking strategy
### Why it matters
How data should be indexed depends on how it will be retrieved. The previous section assumed documents were already split into manageable chunks; here the book treats the splitting itself, because the chunking strategy can strongly affect retrieval performance (PDF pp. 520-521).

### Ways to chunk
- Equal-length chunks by a chosen unit: characters, words, sentences or paragraphs. Examples: 2,048 characters, 512 words, 20 sentences per chunk, or one paragraph per chunk (PDF p. 521).
- Recursive splitting: start with a large unit (sections), and if a piece is still above the maximum chunk size, split it into paragraphs, then sentences. This lowers the odds that related text is cut apart arbitrarily (PDF p. 521).
- Document-specific splitters: splitters exist for particular programming languages; Q&A documents can be split per question-answer pair; Chinese text may need different handling than English (PDF p. 521).
- Token-based chunking: tokenize with the generative model's own tokenizer (the book's example is Llama 3) and cut on token boundaries. This eases work with downstream models, but switching to a model with a different tokenizer forces re-indexing the data (PDF p. 522).

### Overlap
Without overlap, a chunk boundary can slice through important context. The book's example: "I left my wife a note" split into "I left my wife" and "a note" leaves neither chunk with the real meaning. Overlap makes sure boundary information sits fully in at least one chunk. With a 2,048-character chunk, an overlap of about 20 characters is suggested (PDF pp. 521-522).

### Size constraints and trade-offs
- A chunk must not exceed the generative model's maximum context length, and, for embedding-based retrieval, not the embedding model's context limit either (PDF p. 522).
- Smaller chunks allow more diverse information, since more of them fit in the context; halving the chunk size lets you fit twice as many (PDF p. 522).
- Smaller chunks can lose information. If topic X is discussed throughout a document but named only in the first half, splitting in two means the second half may never be retrieved and its X-related content is unavailable to the model (PDF p. 523).
- Smaller chunks also raise computational cost, especially for embedding retrieval: halving chunk size doubles the number of chunks to index and the embedding vectors to generate and store, makes the vector search space twice as large, and can slow queries (PDF p. 523).
- No universal best chunk size or overlap exists; the book says to experiment (PDF p. 523).

## Reranking
- Initial retriever rankings can be reranked for accuracy. This is especially useful when you must cut the number of retrieved documents, either to fit the model's context or to reduce input tokens (PDF p. 523).
- A common pattern, covered earlier under combining retrieval algorithms: a cheap, less precise retriever fetches candidates and a more precise, costlier mechanism reranks them (PDF p. 523).
- Documents can also be reranked by recency, giving newer data more weight. This suits time-sensitive uses such as news aggregation, chatting with your emails, or stock market analysis (PDF p. 524).
- Context reranking differs from classic search reranking. In search, the exact position (first versus fifth) is crucial. In context reranking, order still matters because models may handle the start and end of the context better (see "Context Length and Context Efficiency"), but once a document is included, its exact position matters less than in search (PDF p. 524).

## Query rewriting
- Also called query reformulation, query normalization, and sometimes query expansion (PDF p. 524).
- Example conversation: the user asks when John Doe last bought something; the AI answers (a Fruity Fedora hat two weeks earlier, January 3, 2030); the user then asks "How about Emily Doe?" Used verbatim as a retrieval query, this ambiguous follow-up will likely fetch irrelevant results. It should be rewritten so it stands alone: "When was the last time Emily Doe bought something from us?" (PDF pp. 524-525).
- Query rewriting is not unique to RAG. Traditional search engines often do it with heuristics. In AI applications another model can do it, using a prompt such as "Given the following conversation, rewrite the last user input to reflect what the user is actually asking." Figure 6-4 shows ChatGPT rewriting a query this way: the figure displays the instruction plus the John Doe conversation as the input and, below it, the single rewritten output "When was the last time Emily Doe bought something from us?" (PDF p. 525).
- It can get complicated when identity resolution or other knowledge is needed. For "How about his wife?", the system must first query a database to learn who the wife is. If that information is absent, the rewriting model should acknowledge the query cannot be solved rather than hallucinate a name and produce a wrong answer (PDF pp. 525-526).

## Contextual retrieval
The idea is to augment each chunk with relevant context so the right chunks are easier to retrieve (PDF p. 526).
- Metadata augmentation: tags and keywords; for ecommerce, a product's description and reviews; for images and videos, titles or captions (PDF p. 526).
- Extracted entities: specific terms such as the error code EADDRNOTAVAIL (99) can be added as metadata so keyword retrieval works even after the document is turned into embeddings (PDF p. 526).
- Questions a chunk can answer: for customer support, attach related questions to each article. A password-reset article might carry "How to reset password?", "I forgot my password", "I can't log in", or "Help, I can't find my account" (PDF p. 526).
- Context from the source document: when a document is split, some chunks lack the information that tells the retriever what they are about, so each chunk can be augmented with the original document's title and summary (PDF pp. 526-527).
- Anthropic's approach: use an AI model to generate a short context, usually 50-100 tokens, explaining the chunk and its relation to the whole document (PDF p. 527). The prompt places the whole document and the chunk in tagged blocks, then asks for a short succinct context that situates the chunk in the document for the purpose of improving search retrieval, answering with only that context (PDF pp. 527-528). The generated context is prepended to the chunk and the augmented chunk is then indexed by the retrieval algorithm; Figure 6-5 (from Anthropic's "Introducing Contextual Retrieval", 2024) illustrates this (PDF pp. 528-529). The figure, labelled "Preprocessing (new)", shows a corpus whose documents are split into chunks (Chunk 1, Chunk 2, ... Chunk X); a prompt is run for every chunk, with the source document as input, to situate the chunk in the document; each output is a "Context N + Chunk N" pair, annotated as 50-100 tokens of context prepended to the chunk. The augmented chunks then feed two indexes: an embedding model into a vector database, and TF-IDF vectors into a TF-IDF index; a user query reaches both (PDF p. 529). The right edge of the figure is cropped in the PDF, so what happens downstream of the two indexes is not visible.

## Evaluating retrieval solutions (box, tail page)
Factors to weigh (PDF p. 530):
- Which retrieval mechanisms are supported, and is hybrid search supported?
- For a vector database: which embedding models and vector search algorithms?
- Scalability for data storage and query traffic, and fit with your traffic pattern.
- Indexing time, and how much data can be bulk added or deleted at once.
- Query latency per retrieval algorithm.
- For a managed service: the pricing structure, whether by document or vector volume or by query volume.
The list leaves out enterprise functions such as access control, compliance, and data-plane/control-plane separation (PDF p. 530).

## When and how to apply
INTERPRETATION: treat chunk size, overlap, reranking depth and context-augmentation as tunable parameters and measure retrieval quality on your own data, since the book says there is no universal best setting.

## Relations
Builds on the retrieval algorithms of C06-004 and the RAG architecture of earlier sections (C06-003); the next section, C06-006, extends RAG to images and tables.
