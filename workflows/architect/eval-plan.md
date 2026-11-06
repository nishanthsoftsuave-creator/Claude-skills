---
name: eval-plan
mode: architect
rows: [C03-004, C03-005, C03-006, C03-007, C03-008, C03-010, C03-011, C03-012, C03-014, C03-015, C03-016, C03-017, C03-019, C03-020, C04-003, C04-004, C04-005, C04-006, C04-011, C04-012, C04-013]
---
# Evaluation plan (written before building)

## When to use
Every Architect run, after the pattern and model are chosen, and also when the user only needs to choose a model or build an evaluation set. The plan is the contract the design-review gate checks. Review & Test mode reuses it as its criteria source.

## Inputs needed
Success definition and cost of a wrong answer (intake). Components of the system (from `solution-pattern.md`, `architecture-design.md`). Data available for evaluation, including real user queries. Whether logprobs are exposed by the chosen model. Budget for judge calls and human review. Ask only for what discovery did not answer (`intake.md`).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C03-004 | [Entropy](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p242-entropy.md) | Foundation for language-model metrics |
| C03-005 | [Cross Entropy](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p244-cross-entropy.md) | Training objective view of the same metric |
| C03-006 | [Bits-per-Character and Bits-per-Byte](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p245-bits-per-character-and-bits-per-byte.md) | Cross-model comparability |
| C03-007 | [Perplexity](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p246-perplexity.md) | Definition and units |
| C03-008 | [Perplexity Interpretation and Use Cases](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p248-perplexity-interpretation-and-use-cases.md) | When perplexity helps and when it misleads |
| C03-010 | [Functional Correctness](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p253-functional-correctness.md) | Exact check by execution, pass@k |
| C03-011 | [Similarity Measurements Against Reference Data](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p257-similarity-measurements-against-reference-data.md) | Exact match, lexical, semantic similarity |
| C03-012 | [Introduction to Embedding](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p267-introduction-to-embedding.md) | Embeddings behind semantic similarity |
| C03-014 | [Why AI as a Judge?](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p272-why-ai-as-a-judge.md) | When a judge is attractive |
| C03-015 | [How to Use AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p274-how-to-use-ai-as-a-judge.md) | Judge prompt anatomy and scoring systems |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | Inconsistency, ambiguity, cost, biases |
| C03-017 | [What Models Can Act as Judges?](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p290-what-models-can-act-as-judges.md) | Choosing the judge model |
| C03-019 | [Challenges of Comparative Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p302-challenges-of-comparative-evaluation.md) | Limits of ranking by preference |
| C03-020 | [The Future of Comparative Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p308-the-future-of-comparative-evaluation.md) | Why comparison still earns a place |
| C04-003 | [Domain-Specific Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p319-domain-specific-capability.md) | Four criteria buckets, benchmarks, MCQ |
| C04-004 | [Generation Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p324-generation-capability.md) | Factual consistency and safety |
| C04-005 | [Instruction-Following Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p339-instruction-following-capability.md) | Format and constraint compliance |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | Cost and latency criteria |
| C04-011 | [Step 1. Evaluate All Components in a System](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p393-step-1-evaluate-all-components-in-a-system.md) | Per component, per turn, per task |
| C04-012 | [Step 2. Create an Evaluation Guideline](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p396-step-2-create-an-evaluation-guideline.md) | Criteria, rubrics, business mapping |
| C04-013 | [Step 3. Define Evaluation Methods and Data](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p400-step-3-define-evaluation-methods-and-data.md) | Methods, slicing, set size, pipeline reliability |

## Procedure
Follow the book's three steps in order: components, guideline, methods and data `[C04-011]`, `[C04-012]`, `[C04-013]`. The goal is a plan, not scores.

1. **List what is evaluated (template section 1).** Every component and the whole system, since a failure can hide in any component; for a two-step flow score each step separately and the end result `[C04-011]`. Evaluate per turn (quality of each output) and per task (did it finish, in how many turns); task-based matters more to users, though task boundaries are hard to detect `[C04-011]`. Include the guardrail, router and retrieval components from `architecture-design.md`.
2. **Choose criteria from the four buckets** (domain capability, generation, instruction following, cost and latency) `[C04-003]` (template section 2). Write the guideline before building `[C04-012]` (template section 5; the same guideline can later guide training-data annotation):
   - Take criteria from real test queries; produce several responses and decide which are good or bad. A correct answer is not always a good one `[C04-012]`.
   - Also define what the application must not do: out-of-scope inputs, how they are detected, how to answer `[C04-012]`.
   - Pick a scoring system per criterion (binary, 1-5, 0-1, or -1/0/1 for contradiction/neutral/entailment), write a rubric with scored examples, and validate it with humans until unambiguous `[C04-012]`.
   - Map metric levels to business outcomes and set a usefulness threshold (the minimum to be useful). Say where every threshold came from; a threshold without a source is a guess (INTERPRETATION: the book's 80%/90%/98% factual-consistency mapping and 50% floor are illustrations of the method, not targets) `[C04-012]`. Know the business metric being served first (e.g. stickiness or engagement) `[C04-012]`.
3. **Domain capability.** Use public or private benchmarks matching the capability needed `[C04-003]`. Code: functional correctness (run tests; pass@k counts a problem solved if any of k samples passes) plus efficiency where it matters; readability needs subjective methods `[C03-010]`, `[C04-003]`. Knowledge and reasoning: multiple choice with accuracy, or F1, precision and recall for classification, compared with the random baseline (25% with four options); MCQ results move with small formatting changes and do not test generation, so do not use them as the main check of generation quality `[C04-003]`.
4. **Generation capability.** Choose factual consistency by scope: local (against supplied context: summaries, support bots, RAG) or global (against open knowledge) `[C04-004]`. Methods: AI judge, self-verification (many samples, costly), search-augmented checking, textual entailment or a small specialised scorer `[C04-004]`. Safety: list the harm categories relevant to the use case, use a moderation tool or small toxicity classifier, and add toxicity benchmarks if relevant `[C04-004]`. Study where the model actually hallucinates and weight the evaluation set toward those queries `[C04-004]`. What counts as a fact depends on trusted sources, and "no evidence found" is not proof of absence; a neutral entailment result leaves consistency undetermined `[C04-004]`. Fluency and coherence matter mainly for weak models, creative writing and low-resource languages `[C04-004]`.
5. **Instruction following.** Write your own instruction set with your own constraints (the YAML, banned phrases, length, vocabulary limits you need); public benchmarks represent real instructions only loosely `[C04-005]`. Programmatically checkable instructions get code checks; fuzzy ones get a list of yes/no criteria, scored as criteria passed over all criteria `[C04-005]`. If the system plays a role, test that it stays in character, by heuristic or judge `[C04-005]`. Keep this separate from domain capability so a failure can be attributed `[C04-005]`.
6. **Cost and latency.** Write each as a metric with a hard requirement and an ideal, using percentiles, e.g. TTFT at P90 and total query time at P90 on your own prompt set; Table 4-3 is an illustration, not a recommendation `[C04-006]`. Targets come from `inference-plan.md`.
7. **Select a method per criterion** (template section 3) and mix when useful: a cheap classifier on 100% of data plus an expensive judge on 1% `[C04-013]`.

| Method | Use when | Limits | Source |
|---|---|---|---|
| Functional correctness | output can be executed or measured | not always automatable | `[C03-010]` |
| Exact match | short exact answers | "contains" variants accept wrong answers; fails on open text | `[C03-011]` |
| Lexical similarity | overlap with references is meaningful | needs comprehensive, correct references; can rank wrong answers high | `[C03-011]` |
| Semantic similarity (embeddings, cosine) | meaning matters more than wording | depends on embedding quality; embedding cost; embeddings judged by usefulness on your task | `[C03-011]`, `[C03-012]` |
| Perplexity, cross entropy, BPB | judging or choosing a base language model, contamination or duplicate checks | not comparable across tokenizers (use BPB); poor proxy after SFT or RLHF; needs logprobs | `[C03-004]`, `[C03-005]`, `[C03-006]`, `[C03-007]`, `[C03-008]` |
| AI judge | no references, subjective or flexible criteria | see step 8 | `[C03-014]`, `[C03-015]`, `[C03-016]` |
| Comparative evaluation | relative preference, saturated benchmarks, hard-to-score outputs | gives rank, not absolute quality | `[C03-019]`, `[C03-020]` |
| Human review | open-ended quality, calibrating judges | cost and speed | `[C04-013]` |

   Use logprobs when the API exposes them: confidence for classification, perplexity for fluency checks `[C04-013]`. Perplexity is for understanding the base model and for contamination (low perplexity on a benchmark suggests it was seen), not for judging a post-trained assistant `[C03-008]`. The derivations in `[C03-004]` to `[C03-007]` are needed only to read these numbers; do not make perplexity a headline criterion.
8. **Use a judge deliberately.** Judges are fast, cheap against humans, reference-free and flexible `[C03-014]`. The judge prompt states the task, the criteria, the scoring system and scored examples; prefer classification or a small discrete scale (1-5) over continuous or wide scales `[C03-015]`. The judge is the model plus the prompt plus sampling settings; pin and version all three and never trust a judge whose model and prompt you cannot see `[C03-015]`, `[C03-016]`. Plan for known limits `[C03-016]`: inconsistency (examples in the prompt raised one study's consistency but multiplied cost); non-standard criteria (the same criterion name scores differently across tools); extra cost and latency (generation plus each judge prompt multiplies calls; spot-check a subset, which can miss failures); self-bias, first-position bias (randomise order), verbosity bias; privacy when sending data to a proprietary judge. Choose the judge model by role: a stronger judge on a sample, a weaker judge as a background monitor, self-critique for sanity checks, a small specialised judge for a narrow criterion (reward, reference-based, preference model) `[C03-017]`. Supplement judges with exact methods or human review `[C03-016]`. High consistency does not imply accuracy: a judge can repeat the same mistake `[C03-016]`. Using a judge as a pre-response guardrail adds latency `[C03-016]`. Calling any judge or model to try the plan is a paid call: it needs the user's approval and a spend cap. A finding resting only on a judge stays "probable" in any later review.
9. **Comparative evaluation, if used.** Comparison is easier than scoring and does not saturate `[C03-020]`, but needs many matches, assumes transitivity that may not hold, depends on crowd quality, and does not say whether either model is good enough `[C03-019]`. Combine it with pointwise or exact metrics on your own task `[C03-019]`. A public leaderboard may not reflect your retrieval-augmented setup; for private models or your own domain you need your own comparison signals (e.g. in-product side-by-side choices) `[C03-019]`. A win rate (e.g. 51%) does not convert to tasks resolved or settle cost-benefit `[C03-019]`.
10. **Data (template section 4).** Annotate examples for every component and criterion, from real production data when possible; natural labels first `[C04-013]`. Keep several sets: production-like, per-slice (tier, source, language, difficulty), known error-prone inputs, inputs where users err, and out-of-scope inputs `[C04-013]`. Slice to catch bias, debug and avoid Simpson's paradox `[C04-013]`. Size: large enough to be reliable, small enough to afford; check stability by bootstrap (if results swing, say 70% to 90%, the set is too small); to see a 10% difference at 95% confidence expect about 100 samples, 3% about 1,000, 1% about 10,000 (OpenAI rule of thumb; each 3x smaller difference needs about 10x more) `[C04-013]`. Reference points: benchmark median size about 1,000; 300 is called an absolute minimum `[C04-013]`. Keep evaluation data separate from tuning data (INTERPRETATION).
11. **Evaluate the evaluation (template section 7).** Do better outputs score higher; does running it twice give the same result (judge temperature 0); do metrics correlate; what does the pipeline cost in latency and money `[C04-013]`. Iterate criteria as users change, but keep consistency so trends stay readable `[C04-013]`.
12. **Execution (section 6).** Plan production methods too: where no references exist, decide what user feedback to collect (see `ops-cost-feedback.md`) `[C04-013]`. When each check runs (before release, on every change, production sampling), who owns it, the budget, and the action when a threshold is missed. Daily human review of a production sample is a legitimate method `[C04-013]`. Connect to `ops-cost-feedback.md` so monitoring metrics inherit the evaluation metrics `[C04-013]`.

## Evidence and exit gate
Every component and criterion has a method, a data source, a threshold with its origin, and an owner. The judge (if any) is fully specified and has a human or exact cross-check. The set has slices and a stability check. Unknowns are flagged `UNVERIFIED`. Then pass `design-review-gate.md`.

## Outputs
Fill `../../templates/eval-plan.md`. Link it from `../../templates/architecture-design.md` section 4. Record any method or model choice with `../../templates/decision-record.md`.

## Pitfalls
- Evaluating only the end result and not each component `[C04-011]`.
- Vague guideline producing ambiguous scores `[C04-012]`.
- Using MCQ accuracy or public leaderboards as proof of fit for your task `[C04-003]`, `[C03-019]`.
- Reporting perplexity for a post-trained assistant, or comparing bits per token across models `[C03-008]`, `[C03-006]`.
- Lexical similarity scoring a correct answer low because references are narrow `[C03-011]`.
- Judge changes mistaken for product change `[C03-016]`.
- Small, unsliced evaluation set `[C04-013]`.
- Presenting book benchmark numbers and tool names as current `[C04-004]`, `[C03-015]`.
