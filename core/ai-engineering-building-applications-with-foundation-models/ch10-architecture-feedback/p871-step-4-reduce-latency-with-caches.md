---
id: C10-006
title: Step 4. Reduce Latency with Caches
source_pages: "871-874"
chapter: 10
concepts: [system-caching, exact-caching, semantic-caching, eviction-policy, cache-data-leak, similarity-threshold, cache-hit-rate, cache-classifier]
related: [C10-005, C10-007, C10-004, C09-007]
time_sensitive: false
---
# Step 4. Reduce Latency with Caches
(Source: PDF pp. 871-874; the architecture diagram with caches, Figure 10-8, is printed on the next page and is described in C10-007)

## What the section covers
The fourth step in growing an AI application architecture: adding system-level caches to lower latency and cost. The book treats caching only in broad strokes because it is an old technology with ample literature. Inference-level caches (KV cache and prompt cache) are a separate matter, covered in Chapter 9; this section is about system caching (PDF p. 871). Two mechanisms are described: exact caching and semantic caching.

## Meaning
- **Exact caching**: a stored item is reused only when exactly that item is requested again (PDF p. 871).
- **Semantic caching**: a stored item is reused when the new query is merely semantically similar to a cached one, not identical (PDF p. 873).

## How it works

### Exact caching
- Example: a user asks the model to summarize a product. The system looks in the cache for a summary of that exact product; if present it is returned, otherwise the product is summarized and the summary stored (PDF p. 871).
- The same idea applies to embedding-based retrieval, to skip redundant vector searches: if the incoming query is already in the vector-search cache, return the cached result; otherwise run the search and cache its result (PDF p. 871).
- Caching pays off most for queries with several steps (for instance chain-of-thought) or slow actions such as retrieval, SQL execution or web search (PDF pp. 871-872).
- Storage: in-memory storage gives fast retrieval but is limited, so a cache can instead sit on a database such as PostgreSQL or Redis, or on tiered storage that balances speed against capacity (PDF p. 872).
- An eviction policy is essential for controlling cache size and keeping performance up. Named policies: Least Recently Used (LRU), Least Frequently Used (LFU), and first in, first out (FIFO) (PDF p. 872).
- How long to keep an entry depends on how likely it is to be requested again. User-specific queries (the book's example is "What's the status of my recent order?") are unlikely to be reused by other users and should not be cached; time-sensitive queries such as "How's the weather?" make little sense to cache either. Many teams train a classifier to predict whether a query should be cached (PDF p. 872).

### Semantic caching
- Example: one user asks for the capital of Vietnam and gets "Hanoi"; another later asks for the "capital city" of Vietnam. Semantically the same question, so the first answer can be reused instead of recomputing (PDF p. 873).
- Benefit: a higher cache hit rate and possibly lower cost. Drawback stated up front: it can reduce model performance (PDF p. 873).
- It only works if there is a dependable way to decide whether two queries are similar. A common approach uses semantic similarity (Chapter 3). The steps (PDF p. 873):
  1. Create an embedding of each query with an embedding model.
  2. Run vector search for the cached embedding most similar to the current query embedding; call that score X.
  3. If X exceeds a chosen similarity threshold, treat the cached query as similar and return its cached result. Otherwise process the query and cache it along with its embedding and result.
- This approach needs a vector database to hold the embeddings of cached queries (PDF p. 874).

### Where caches sit in the platform
- With the caches added, the platform looks like Figure 10-8 (printed on the next page, described in C10-007). KV cache and prompt cache are typically implemented by model API providers, so the figure leaves them out; to draw them they would go inside the Model API box (PDF p. 874). The sentence about a new arrow that stores generated responses in the cache finishes at the top of the next page.

## Limitations and failure modes
- **Data leak through caching** (warning box, PDF p. 872): if caching is mishandled, one user's private information can reach another. Example: on an ecommerce site, user X asks "What is the return policy for electronics products?" Because the policy depends on membership, the system first fetches X's information and writes an answer containing it. The system treats the query as generic and caches the answer. Later user Y asks the same thing and receives the cached answer, exposing X's information.
- **Semantic cache is of more doubtful value** than other caching techniques because many of its parts can fail. Success depends on good embeddings, working vector search and a reliable similarity metric (PDF p. 874).
- Picking the similarity threshold can be tricky and take a lot of trial and error. If the system wrongly judges a new query as similar to a cached one, it returns an incorrect cached response (PDF p. 874).
- It can be slow and compute-heavy because each lookup involves a vector search; speed and cost scale with the size of the cached embedding set (PDF p. 874).

## When and how to apply
- Cache multi-step or slow-to-compute queries; exclude user-specific and time-sensitive ones, possibly via a trained classifier (PDF p. 872).
- Choose an eviction policy and a storage tier suited to the cache size (PDF p. 872).
- Semantic caching may still be worthwhile when the hit rate is high, i.e. a good share of queries can be served from cache. Before adding its complexity, evaluate its efficiency, cost and performance risks (PDF p. 874).
- INTERPRETATION: because of the leak scenario, decide cacheability by whether the generated answer depended on user-specific retrieved data, not only by how the question reads.

## Evaluation and success criteria
The book names cache hit rate as the figure that justifies a semantic cache (PDF p. 874). The later monitoring section (C10-008) lists the cache's cost and hit rate among the metrics to track.

## Relations
Follows the router and gateway step (C10-005); the architecture diagram showing where caches sit, and the agent-patterns step, are in C10-007. Guardrails that reduce data exposure are in C10-004; KV and prompt caching at the inference layer are in C09-007.
