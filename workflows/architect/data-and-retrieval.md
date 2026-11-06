---
name: data-and-retrieval
mode: architect
rows: [C06-003, C06-004, C06-005, C06-006, C08-003, C08-004, C08-005, C08-006, C08-008, C08-009, C08-010, C08-011]
---
# Data and retrieval layer

## When to use
Run when the design needs the model to use information it was not trained on (RAG over documents, tables, images), or needs a curated, synthesized or distilled dataset (for finetuning, evaluation seeds or a smaller model). Skip the retrieval half if `solution-pattern.md` ruled out external context; skip the data half if nothing will be trained or finetuned.

## Inputs needed
From discovery and `intake.md`; ask only what is missing:
- Data sources and kinds (text, tables, images, audio), volume, and how often they change.
- Sensitivity: PII, privacy law, licence limits on data and on model outputs.
- Query traffic, latency and cost ceilings, and the budget split between data work and compute.
- Whether a finetune is planned (then also read `finetune-decision.md` and `finetune-plan.md`).
- Any existing eval set or user-feedback stream.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C06-003 | [RAG Architecture](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p498-rag-architecture.md) | Retriever, generator, indexing, querying, chunking |
| C06-004 | [Retrieval Algorithms](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p500-retrieval-algorithms.md) | Term-based vs embedding-based, vector search, hybrid, retriever metrics |
| C06-005 | [Retrieval Optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p520-retrieval-optimization.md) | Chunking, reranking, query rewriting, contextual retrieval |
| C06-006 | [RAG Beyond Texts](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p530-rag-beyond-texts.md) | Multimodal and tabular RAG |
| C08-003 | [Data Quality](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p704-data-quality.md) | Six quality characteristics |
| C08-004 | [Data Coverage](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p707-data-coverage.md) | Diversity, data mix |
| C08-005 | [Data Quantity](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p712-data-quantity.md) | How much data, scaling experiments |
| C08-006 | [Data Acquisition and Annotation](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p721-data-acquisition-and-annotation.md) | Sources, flywheel, guidelines |
| C08-008 | [Why Data Synthesis](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p727-why-data-synthesis.md) | Five reasons to synthesize |
| C08-009 | [Traditional Data Synthesis](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p731-traditional-data-synthesis-techniques.md) | Templates, transformation, simulation |
| C08-010 | [AI-Powered Data Synthesis](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p738-ai-powered-data-synthesis.md) | Instruction and preference data, verification, limits |
| C08-011 | [Model Distillation](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p753-model-distillation.md) | Teacher-student, licence caveat |

## Procedure
### A. Retrieval layer
1. **Fix the architecture.** A RAG system has a retriever (indexing plus querying) and a generator; the prompt goes to both. Success hinges on retriever quality, so spend design effort there. Components may be off-the-shelf; end-to-end finetuning can improve the system significantly. Documents are split into chunks and the relevant chunks are joined with the prompt. `[C06-003]`
2. **Choose the retrieval mechanism.** `[C06-004]`

| Situation | Choice | Basis |
|---|---|---|
| Fast, cheap, works out of the box; exact keywords matter (error codes, product names) | Term-based (BM25 or similar) | Much faster and cheaper, few components to tune, ambiguity of terms hurts |
| Meaning matters more than wording; willing to tune | Embedding-based with a vector database | Can outperform term-based with finetuning; embeddings can blur keywords; embedding, storage and search add cost and latency |
| Both needs | Hybrid: sequential (cheap retriever then rerank) or parallel with reciprocal rank fusion | Production systems usually combine retrievers |

   Cost checks: re-embedding when data changes often, and vector storage and search spend (the book says a vector database costing one-fifth to half of model API spend is not uncommon). Query and index must use the same embedding model, and a bad embedding model sinks retrieval. Exact k-NN suits only small data; large data needs approximate nearest neighbour (HNSW, IVF, product quantization, LSH, Annoy are the book's named examples). A more detailed index is more accurate but slower and more memory-hungry to build. `[C06-004]`
3. **Tune the four optimisations**, measuring each on your own data because no chunk size or overlap is universally best: `[C06-005]`
   - Chunking: unit, recursive splitting, overlap, size limits (generator and embedding model context). Overlap stops a boundary slicing key context (the book suggests about 20 characters for a 2,048-character chunk). Smaller chunks give more diversity in context but can lose information and double index size when halved. Token-based chunking ties you to a tokenizer.
   - Reranking: use when you must cut documents to fit context or reduce tokens; recency reranking for time-sensitive data. In parallel hybrid, reciprocal rank fusion sums 1/(k + rank) per retriever (the book gives a typical k of 60).
   - Query rewriting: make follow-up questions standalone. If rewriting needs missing knowledge, the rewriter must say it cannot resolve the query rather than invent.
   - Contextual retrieval: add metadata, entities, answerable questions, or source-document context to each chunk (Anthropic's 50-100 token generated context is the book's example).
4. **Extend beyond text if the data requires it.** Images: retrieve by metadata (titles, tags, captions) or by content with a multimodal embedding model such as CLIP (example, time-sensitive). Tables: text-to-SQL from the query and schemas, SQL execution, then generation; if schemas are too many for context, add a step predicting which tables are needed. Text-to-SQL output must be valid, so apply `structured-outputs-and-sampling.md`. `[C06-006]`
5. **Define retrieval evaluation now.** Context precision and context recall on an annotated query set; NDCG, MAP or MRR if order matters; embedding quality (MTEB-style); ANN metrics (recall, QPS, build time, index size); then end-to-end answer quality. Recall needs relevance annotation of the whole database, which is why some frameworks only report precision. `[C06-004]` When choosing a retrieval product, compare supported mechanisms, hybrid support, embedding models, scale, indexing and query latency and pricing. The book's list omits access control and compliance; add them as `INTERPRETATION`. `[C06-005]`

### B. Data layer (finetuning, eval seeds, distillation)
6. **Set the quality bar before collecting.** Define what each of six traits means here: relevant, aligned with task requirements (not merely accurate), consistent across annotators, correctly formatted, sufficiently unique (duplicates bias and contaminate), compliant (for example no PII where barred). A small high-quality set can beat a large noisy one (Yi 10K, LIMA 1,000 examples), though LIMA was less robust than product-grade models. `[C08-003]`
7. **Set coverage.** Mirror real usage (length, typos, languages, topics, output formats); what counts as diverse depends on the application. Default rule: a mix that reflects real usage; the heavier route is small-model scaling experiments. More heterogeneous data can sometimes hurt. `[C08-004]`
8. **Set quantity by experiment, not by guess.** Hand-craft about 50 examples and finetune; the book says 50-100 usually show visible gains. If none, check learning rate, data quality and prompts before blaming the method. Then train on 25%, 50% and 100% and read the curve (steep means more data helps, flat means it will not). Few hundred to few thousand examples favour PEFT; tens of thousands to millions allow full finetuning; with little data a stronger base model helps most, with abundant data a smaller one suffices; with very large data a pre-trained model can do worse than training from scratch (ossification), so evaluate that. Cap size by annotation budget (money spent on data is not spent on compute). Staging (self-supervised, less relevant or synthetic data first) can cut the high-quality data needed but adds coordination risk. `[C08-005]`
9. **Acquire.** INTERPRETATION order: own application data (the book calls the flywheel the most valuable source), then existing datasets checked for licence and provenance, then annotation, then synthesis. Never trust public data without inspection. Budget several rounds of guideline revision; the evaluation guidelines can be reused. `[C08-006]`
10. **Decide whether to synthesize.** Reasons the book gives: quantity, coverage, quality, privacy, distillation. `[C08-008]` Choose the method by what can be verified: `[C08-009]` `[C08-010]`

| Method | Use for | Verification |
|---|---|---|
| Templates and random fillers, transformations, perturbation | Structured documents, label-preserving augmentation, robustness | The book assumes swaps keep meaning and sentiment; INTERPRETATION: spot-check that labels still fit |
| Simulation | Rare or dangerous events, tool-use sequences | Sim-to-real gap; validate outcomes |
| AI generation (instructions, responses, preference data, paraphrase, translation, reverse instruction) | Post-training data above all | Execute code, round-trip (back-translation), AI judge, heuristic filters, topic and anomaly filters |

    Synthetic data is used far more in post-training than pre-training. Mix in real data and track generator provenance: the book names quality control, superficial imitation, model collapse and obscured lineage as the four limits, and no safe synthetic-to-real ratio is given. For preference data, query the judge twice with order swapped and keep only agreeing pairs. `[C08-010]`
11. **Decide whether to distil.** Goal is a smaller, faster student imitating a teacher; the teacher is the gold standard. Check the teacher's licence first, because many forbid training other models on outputs. Synthetic teacher data is commonly combined with adapter methods such as LoRA (the book's BuzzFeed example). Training on a stronger or smaller model's data that is not imitation of a teacher (reverse instruction, Nemotron-4) is not distillation. Unverified self-generated data can degrade a model. `[C08-011]`

## Evidence and exit gate
Exit when: retrieval mechanism, chunking and optimisations are chosen with measured or planned experiments; retrieval metrics and an annotated query set are in the eval plan; each data trait has a stated target; quantity is justified by the 50-example and 25/50/100% experiments (planned or run); sources, licences and PII handling are recorded; any synthetic or distilled data has a verification method and a real-data share; unknowns are assumptions. If the user will not run experiments, mark chunk size, k and data volume as `UNVERIFIED` defaults.

## Outputs
One [../../templates/decision-record.md](../../templates/decision-record.md) per choice (retrieval mechanism, chunking, data sourcing, synthesis, distillation). Hand retrieval and data metrics to [../../templates/eval-plan.md](../../templates/eval-plan.md) and the component layout to [../../templates/architecture-design.md](../../templates/architecture-design.md).

## Pitfalls
- Judging the retriever only by final answers, or only by retrieval metrics. `[C06-004]`
- Embedding-only retrieval losing exact identifiers. `[C06-004]`
- Changing the generator's tokenizer after token-based chunking forces re-indexing. `[C06-005]`
- Rewriting ambiguous queries by guessing missing facts. `[C06-005]`
- Treating a SQL step as always valid text-to-SQL. `[C06-006]`
- Mistaking "accurate" for "aligned" in annotations; duplicates contaminating evaluation. `[C08-003]`
- Concluding finetuning fails from a tiny run with bad hyperparameters. `[C08-005]`
- Public datasets with a hidden non-commercial source; abandoning annotation guidelines mid-way. `[C08-006]`
- Too many synthetic items per template reducing diversity. `[C08-006]`
- Training indiscriminately on a model's own outputs; contamination via an unknown generator. `[C08-010]` `[C08-011]`
- Synthetic coverage fixes assumed free of drawbacks: the benefits list in `[C08-008]` omits them; read `[C08-010]` limits. `[C08-009]`
- Book numbers (Llama 3 mix, dataset counts, model names) are time-sensitive. `[C08-004]`
