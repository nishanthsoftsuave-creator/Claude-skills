# Discovery: understand the project before anything else

Goal: learn what exists, cheaply, so the next questions are few and the advice fits. Inspect only what bears on the task. Do not read unrelated files, and do not change anything.

## What to look for, and where

Check each item only if the task could depend on it. Use search before reading whole files.

| Question | How to find out |
|---|---|
| Languages, frameworks, runtime versions | manifest and lock files (`package.json`, `pyproject.toml`, `requirements*.txt`, `go.mod`, `pom.xml`, `Cargo.toml`), Dockerfiles |
| Which foundation models and providers | search for SDK imports and endpoints: `openai`, `anthropic`, `google.generativeai` or `genai`, `mistral`, `cohere`, `ollama`, `transformers`, `litellm`, `langchain`, `llama_index`, base URLs, model-name strings |
| Prompts | files named `prompt*`, `*.prompt`, templates, system-message strings, a prompts folder; how they are versioned |
| Retrieval | vector stores and search (`faiss`, `chroma`, `pinecone`, `weaviate`, `qdrant`, `pgvector`, `elasticsearch`, BM25), chunking code, embedding calls |
| Agents and tools | tool or function definitions, agent frameworks, planners, memory stores, loops with model calls |
| Data | datasets, ingestion code, schemas, anything that holds user data or PII |
| Evaluation | `eval*`, `benchmark*`, `golden*`, test folders, metrics code, judge-model calls |
| Operations | CI files, deployment configs, logging, tracing or observability libraries, caching, rate limiting, guardrails, cost tracking |
| Docs and decisions | README, architecture docs, ADRs, known-issue lists, an existing `.ai-architecture-and-reviewer/context.md` |

If the project has an existing project layer, read `context.md` first and treat it as claims to verify, not as truth.

## Output: a one-screen context summary

Present this to the user and let them correct it before moving on.

```
Mode: <architect | review-test | question>
Objective (as understood): ...
Facts (seen in the project): ...            <- each with the file it came from
Assumptions (not confirmed): ...
Unknowns that matter: ...                   <- these drive the intake questions
AI components found: <none | list>
```

## Rules

- Facts need a source file. Anything inferred goes under assumptions.
- No AI components found: say so. In Review & Test, report that little of the book applies and stop. In Architect mode (a greenfield project) that is expected, so continue.
- Never read or copy secrets, `.env` values or credentials. Note that a secret file exists if it matters, without its contents.
- Stop discovering when the unknowns that matter are listed. More reading past that point is waste.
