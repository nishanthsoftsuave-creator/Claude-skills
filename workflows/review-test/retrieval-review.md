---
name: retrieval-review
mode: review-test
rows: [C06-003, C06-004, C06-005, C06-006, C08-013, C08-014, C03-016]
---
# Retrieval (RAG) review

## When to use
The project retrieves external information to build a model's context: document RAG, chat-history or memory retrieval, image retrieval, or text-to-SQL over tables. Route here from `routing.md` for "Review retrieval or RAG"; run `data-review.md` alongside it for the corpus itself.

## Inputs needed
- Where retrieval code, index configuration and corpus live (from discovery, `../discovery.md`; ask only for gaps, see `../architect/intake.md`).
- Corpus kind: text, images or other media, tables, chat history. Whether data changes often.
- Retrieval mechanism in use: term-based, embedding-based, hybrid, reranked; which embedding model; which vector store or index type.
- For run checks: permission to run the retriever read-only against a non-production copy or the production read path, and a spend cap if embedding or judge calls cost money. Production is read-only.
- Any existing evaluation queries with relevance labels. If none exist, building them is the first run check (RR-06).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C06-003 | [RAG architecture](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p498-rag-architecture.md) | Retriever and generator roles; indexing and querying |
| C06-004 | [Retrieval algorithms](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p500-retrieval-algorithms.md) | Term vs embedding, ANN, hybrid, retrieval metrics |
| C06-005 | [Retrieval optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p520-retrieval-optimization.md) | Chunking, reranking, query rewriting, contextual retrieval, solution factors |
| C06-006 | [RAG beyond texts](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p530-rag-beyond-texts.md) | Multimodal and tabular retrieval |
| C08-013 | [Inspect data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p756-inspect-data.md) | Inspecting what is in the index |
| C08-014 | [Deduplicate data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p759-deduplicate-data.md) | Duplicates in the indexed corpus |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | The book's limits of AI judges (inconsistent scores, unstandardized criteria, cost, biases), relevant when relevance labels or answer verdicts come from a judge. The skill's `probable` cap for judge-only findings is INTERPRETATION built on them |

## Procedure
1. **Map the pipeline.** Draw the actual flow: sources, splitter, embedding step (if any), index, query-time steps (query rewrite, retrieval, rerank), context assembly, generator. A system's success hinges on the retriever; the two retriever functions to locate are indexing and querying. Note whether retriever and generator are off-the-shelf or finetuned. `[C06-003]`
2. **Chunking.** Record unit (characters, words, sentences, paragraphs, tokens), size, overlap and splitter type. Decision rules from the book: a chunk must fit both the generator's context limit and, for embedding retrieval, the embedding model's limit; smaller chunks fit more diverse items but can lose context and multiply index size and cost (halving size doubles chunk count); with no overlap, boundaries can cut meaning apart; recursive or document-specific splitting reduces arbitrary cuts; token-based chunking ties the index to one tokenizer, so a model switch means re-indexing. The book's overlap example is about 20 characters on a 2,048-character chunk, an illustration only. There is no universal best size or overlap: require that the project chose its values by measurement (RR-05), else `recommendation`. `[C06-005]`
3. **Retrieval method fit.** Classify the retriever and apply the trade-off table: term-based (TF-IDF, BM25) is faster, cheaper and strong out of the box but suffers term ambiguity, lost multi-word terms under naive tokenization, and length effects; embedding-based can be improved by finetuning and handles natural queries but is costlier, slower and can blur exact keywords such as error codes or product names. Expect hybrid search when both kinds of query occur. Rule: exact identifiers in user queries with embedding-only retrieval is a `risk` until RR-07 shows otherwise. `[C06-004]`
4. **Embeddings and index.** Confirm the same embedding model is used at indexing and at query time; confirm embeddings are evaluated (on their own or by task), not assumed good. Check the index type against scale: exact k-NN is for small data only; ANN families (hashing, graph, quantization, clustering, tree) trade accuracy against build time, memory and speed (a more detailed index is more accurate but slower and heavier to build). If comparing index options, use the book's four ANN-benchmark axes: recall, queries per second, build time, index size. If data changes often, check re-embedding cost and index update time; embedding and vector-search spend can be large. Library names in the book are examples. `[C06-004]`
5. **Combination and ranking.** If retrievers are combined, check how: sequential (cheap candidate fetch, then precise rerank) or parallel with rank fusion. Parallel fusion by reciprocal rank fusion sums 1/(k + rank) over lists (the book gives a typical k of 60). Check reranking depth against context budget and whether recency matters for the use case; reranking is most useful when the number of retrieved items must be cut. For context (unlike search) reranking, order still matters because models handle start and end better, but exact position matters less. `[C06-004]` `[C06-005]`
6. **Query rewriting.** In conversational systems, check that follow-ups ("How about Emily?") are rewritten to standalone queries before retrieval, and that the rewriter says it cannot resolve a query when needed identity information is absent rather than inventing it. `[C06-005]`
7. **Contextual retrieval.** Check whether chunks carry metadata, extracted entities, questions they answer, or document-level title and summary (one book approach has a model write a short 50-100 token context per chunk, prepended before indexing; this costs a model call per chunk, so state the indexing cost). Missing context on chunks whose text alone is ambiguous is a candidate cause of misses. `[C06-005]`
8. **Non-text cases.** Multimodal: retrieval by metadata (captions, tags) or by content using a multimodal embedding model that embeds both modalities into one space. Tabular: expect text-to-SQL, SQL execution, then generation; with many tables, a step that predicts which tables a query needs. Read-only execution for generated SQL is an INTERPRETATION grounded in the production read-only rule; the book's concern with write actions is in `agent-review.md`. `[C06-006]`
9. **Retrieval quality measurement.** Metrics: context precision (share of retrieved items that are relevant) and context recall (share of relevant items that were retrieved). Recall needs relevance labels over the corpus, so it is often unavailable in production; precision can be judged per query. If order matters use NDCG, MAP or MRR. Judge the retriever also by whether it improves final answers. Evaluate three things: retrieval, final output, embeddings. `[C06-004]`
10. **Index data hygiene.** Inspect the corpus that feeds the index: source mix, length distribution, languages, junk tokens, markup residue, and sampled manual reading. Check duplication at the level the project cares about (document, paragraph, chunk) and fix a definition of duplicate. The book says duplicates skew data and waste compute (for training data); INTERPRETATION: in an index, duplicate chunks also waste context slots and index space and crowd out distinct results in top-k. Full dataset procedures are in `data-review.md`. `[C08-013]` `[C08-014]`
11. **Solution factors.** For a managed or third-party vector store, record the factors the book lists: supported retrieval modes and hybrid support, embedding models and search algorithms, scale for storage and traffic, indexing and bulk delete behaviour, query latency, pricing basis. Compare against needs. `[C06-005]`

## Checks
Run commands as `python scripts/run_check.py --case <ID> --evidence-dir <run>/evidence -- <command>`.

| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| RR-01 | Pipeline map matches code (indexing vs querying, rerank, rewrite) | Read retrieval code and config | `RR-01-notes.md` with diagram and file refs | review | C06-003 | Undocumented or inconsistent stage: `unverified` until clarified |
| RR-02 | Chunk size, overlap, splitter within model limits | Review config; run a project script that prints chunk token counts against both limits (if one exists or user approves one) | `RR-02-notes.md`, optionally `RR-02.exec.json` | review (run if script run) | C06-005 | Chunks exceeding the embedding or generator limit: `confirmed` if reproduced; values never measured: `recommendation` |
| RR-03 | Same embedding model at index and query time | Read indexing and query code and config; compare model identifiers | `RR-03-notes.md` | review | C06-004 | Different models or versions: `probable` defect (reproduce with RR-06 before `confirmed`) |
| RR-04 | Index type fits scale and update pattern | Review index config, corpus size, update frequency | `RR-04-notes.md` | review | C06-004 | Exact k-NN on a large corpus, or full re-embed on frequent change with no plan: `risk` |
| RR-05 | Chunking and rerank parameters compared on labelled queries | Project's retrieval harness over alternatives; metrics from RR-06 | `RR-05.exec.json`, comparison table | run | C06-005 | No comparison is possible: `BLOCKED` or `NOT_RUN`; a worse setting than an available alternative on the same set: `confirmed` after one re-run |
| RR-06 | Retrieval precision and recall on a labelled query set | Build 20-50 queries (INTERPRETATION: pragmatic size) with relevant-document labels from the user or domain experts; run retriever through `run_check.py` | `RR-06.exec.json`, `RR-06-queries.*`, metric table | run | C06-004 | Metrics are reported with the set size; the book gives no pass threshold, so judge against the user's stated need or a baseline (a BM25 baseline is the book's reference point). A judge-labelled set caps findings at `probable` |
| RR-07 | Exact-identifier and keyword queries (error codes, product names) | Probe queries containing identifiers present in the corpus | `RR-07.exec.json`, ranks of expected chunk | run | C06-004 | Expected chunk absent from top-k under embedding-only retrieval: `confirmed` if reproduced; fix direction is hybrid search |
| RR-08 | Rewritten queries for conversational follow-ups | Feed multi-turn fixtures through the rewriter; compare output to a standalone question | `RR-08.exec.json`, fixtures | run | C06-005 | Follow-up retrieved verbatim, or rewriter invents missing facts: `confirmed` if reproduced |
| RR-09 | Chunk context augmentation (metadata, entities, questions, doc summary) | Review indexing code and sample chunks | `RR-09-notes.md` | review | C06-005 | Ambiguous chunks with no context while RR-06 shows misses on them: `probable` cause |
| RR-10 | Multimodal retrieval path: shared embedding space or metadata | Review code; probe a text query for images where permitted | `RR-10-notes.md`, optionally `RR-10.exec.json` | review (run if probed) | C06-006 | Image and text embedded by unrelated models and compared directly: `probable` defect |
| RR-11 | Tabular path: schema fed to text-to-SQL, SQL validated, read-only | Review code; run fixture questions against a non-production database copy | `RR-11-notes.md`, optionally `RR-11.exec.json` | review (run if fixtures run) | C06-006 | Generated SQL able to modify data: `confirmed` if reproduced, severity major; wrong query on a fixture: `confirmed` |
| RR-12 | Corpus inspection: source mix, lengths, languages, markup residue | Script (project's or approved) computing distributions; sample manual read of about 15 minutes' worth | `RR-12.exec.json`, `RR-12-notes.md` | run | C08-013 | Anomalies are findings only with an example in evidence; unexplained outliers are `unverified` |
| RR-13 | Duplicates in the indexed corpus | Script using exact and near-duplicate comparison with the agreed definition (hashing if pairwise is too costly) | `RR-13.exec.json`, duplicate clusters | run | C08-014 | Duplicate rate reported with its definition; high duplication feeding top-k: `probable` impact until RR-06 shows effect |
| RR-14 | Vector solution factors vs requirements | Compare vendor or self-hosted features to the list in step 11 | `RR-14-notes.md` | review | C06-005 | Unmet requirement (e.g. no hybrid search where RR-07 failed): `recommendation` |
| RR-15 | Retrieval judged within end-to-end answers | Run RR-06 queries through the whole system; judge answers | `RR-15.exec.json`, answers | run | C06-004 | Good retrieval metrics but poor answers points away from retrieval; an AI-judge-only verdict is capped at `probable` (`[C03-016]`) |

## Evidence and exit gate
- Every run check has an exec record; labelled queries and their source (who labelled) are saved. Query text may contain private data: redact before storing in evidence.
- A finding that rests on a judge's relevance labels states that and stays `probable`.
- Exit gate: all 15 checks have a status with reason, RR-06 is run or explicitly `BLOCKED` (state what label source is missing), and `python scripts/validate_report.py <run_dir>` prints 0 problems.

## Outputs
Results data and the findings report (`../../templates/findings-report.md`). Hand corpus findings to `data-review.md`; hand design-level problems to the Architect workflows via `handoff-to-architect.md`.

## Pitfalls
- Assuming the retriever is fine because answers look plausible; evaluate retrieval separately. `[C06-004]`
- One chunk size copied from a tutorial. `[C06-005]`
- Embedding-only retrieval for queries full of identifiers. `[C06-004]`
- Rewriting that hallucinates missing identity. `[C06-005]`
- Mixing embedding models between indexing and querying. `[C06-004]`
- Treating the book's retrieval tool and benchmark names as current recommendations; they are examples. `[C06-004]`
- Duplicates and unreviewed junk in the corpus. `[C08-013]` `[C08-014]`
