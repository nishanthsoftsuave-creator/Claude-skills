---
id: C07-006
title: Finetuning and RAG
source_pages: "611-617"
chapter: 7
concepts: [finetuning-vs-rag, information-based-failures, behavior-based-failures, semantic-parsing, bm25, adaptation-workflow, rag-plus-finetuning, prompt-examples]
related: [C07-005, C07-007, C04-012]
time_sensitive: false
---
# Finetuning and RAG
(Source: PDF pp. 611-617; the section's last sentence leads into the Memory Bottlenecks heading at the top of PDF p. 618, which belongs to C07-007. The top of PDF p. 611 is the end of the preceding section.)

## What the section covers
How to choose between RAG and finetuning once prompting has been pushed as far as it will go, and a step-by-step workflow for adapting a model to a task. The decision turns on whether the model's failures are information-based or behavior-based. The section ends by announcing that the rest of the chapter is for readers who decide to finetune, starting with the memory bottleneck.

## Prompting versus finetuning with examples (end of the previous section)
Figure 7-2, printed above this section's heading at the top of the page, belongs to the previous section (C07-005); it contrasts putting examples in every prompt with finetuning on them once.

## Meaning: the two kinds of failure
- Information-based failures: outputs are factually wrong or outdated. A RAG system, which gives the model access to relevant information sources, can help (PDF p. 611).
- Behavior-based failures: the model has the facts but behaves badly. Finetuning may help (PDF p. 613).

### Two scenarios of information failure
1. The model lacks the information. Public models are unlikely to know what is private to you or your organization; such a model either admits it or hallucinates (PDF p. 612).
2. The model has outdated information. Example: asked how many studio albums Taylor Swift has released, the correct answer is 11 but the model says 10, probably because its cut-off date precedes the latest album (PDF p. 612).

### Evidence that RAG beats finetuning for fresh knowledge
Ovadia et al. (2024), "Fine-Tuning or Retrieval?", found that for tasks needing up-to-date information, such as questions about current events, RAG outperformed finetuned models. Even more telling, RAG on the base model beat RAG on finetuned models. The book reads this as a sign that finetuning can improve a model on one specific task while degrading it elsewhere (PDF p. 612).

Table 7-2 (PDF p. 613) gives scores (the metric is not named in the extracted text) on a current-events question-answering task. The columns are base model, base model + RAG, FT-reg and FT-p (two finetuning approaches; the extracted text does not define the two labels). Values: Mistral-7B 0.481 / 0.875 / 0.504 / 0.588; Llama 2-7B 0.353 / 0.585 / 0.219 / 0.392; Orca 2-7B 0.456 / 0.876 / 0.511 / 0.566. In every row base + RAG is the highest. On Llama 2-7B, FT-reg (0.219) is even worse than the base model (0.353). The rendered table is clipped at the right edge on screen but all values were legible in the text layer and agree with the image where visible.

### Behavior issues that finetuning can address
- Outputs that are factually correct yet irrelevant to the task. Example: asking for technical specifications of a software project for engineering teams and getting accurate specs that lack the detail the teams need. Finetuning on well-defined technical specs can make them more relevant (PDF p. 613).
- Failure to follow the expected output format. Example: asked for HTML, the model produces code that does not compile, perhaps because training exposed it too little to HTML. More HTML during finetuning can fix this (PDF p. 613).
- Semantic parsing, meaning conversion of natural language into a structured format such as JSON, is a task family whose success depends on producing the expected format, so it often needs finetuning. Strong off-the-shelf models handle common, simple syntaxes (JSON, YAML, regex) but may struggle with syntaxes that have few examples online, such as a domain-specific language for an obscure tool or a complex syntax (PDF p. 614).

## Why it matters: form versus facts
The book's summary line: finetuning is for form, RAG is for facts (PDF p. 614).
- RAG supplies external knowledge for more accurate, informative answers and can mitigate hallucination.
- Finetuning teaches the model to follow syntaxes and styles. With enough high-quality data it can reduce hallucination, but with low-quality data it can make hallucination worse (PDF p. 614).

## When and how to apply
- If the model has both information and behavior problems, start with RAG. It is usually easier because you do not need to curate training data or host finetuned models. Begin with simple term-based retrieval such as BM25 before moving to anything needing vector databases (PDF p. 614).
- RAG can give a larger boost than finetuning. Ovadia et al. showed that on almost every question category of MMLU, RAG beat finetuning for Mistral 7B, Llama 2-7B and Orca 2-7B (PDF p. 615).
- They are not mutually exclusive. In the same experiment, adding RAG on top of a finetuned model improved MMLU performance 43% of the time; the other 57% of the time it did not beat RAG used alone (PDF p. 615).
- No universal workflow exists. Figure 7-3 (PDF pp. 615-616) sketches an example flow, inspired by an OpenAI (2023) example. It is a plot with time going upward, in four regions: prompt engineering (bottom left), RAG as context optimization (top left), finetuning as behavior optimization (right), and a top-right region for RAG with a finetuned model. The path drawn goes Prompt, Add examples, Add simple retrieval, then branches: either Add complex retrieval, or Finetune; both arrows lead on to "RAG with finetuned model". The caption: after simple retrieval such as term-based, whether to try complex retrieval (for example hybrid search) or finetuning depends on the application and its failure modes (PDF p. 616).

### The adaptation workflow
Before any step, define evaluation criteria and build the evaluation pipeline (Chapter 4). Evaluation is used at every step, not just at the start, to benchmark progress (PDF p. 616).
1. Try prompting alone, following the prompt engineering best practices of Chapter 5, including systematic prompt versioning (PDF p. 616).
2. Add examples to the prompt; depending on the use case, between 1 and 50 (PDF p. 617).
3. If failures come from missing information, connect data sources. Start with basic term-based retrieval; even simple retrieval with accurate relevant knowledge should help (PDF p. 617).
4. Then branch on failure mode: (a) continuing information failures suggest more advanced RAG such as embedding-based retrieval; (b) continuing behavioral problems (irrelevant, malformatted or unsafe responses) suggest finetuning. Trade-off: embedding-based retrieval adds components to the inference pipeline, increasing inference complexity; finetuning increases the complexity of model development but leaves inference unchanged (PDF p. 617).
5. Combine RAG and finetuning for a further boost (PDF p. 617).

## Relations
Follows the reasons-not-to-finetune discussion (C07-005). The decision to finetune leads into the memory-bottleneck material beginning at C07-007. Evaluation pipeline design is covered in C04-012 and neighbouring Chapter 4 rows.
