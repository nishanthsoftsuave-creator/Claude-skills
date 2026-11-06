---
name: solution-pattern
mode: architect
rows: [C05-003, C05-004, C05-005, C06-003, C06-008, C07-004, C07-005, C07-006, C01-020, C01-021, C01-022]
---
# Solution pattern

## When to use

After `use-case-and-requirements.md` (and usually `model-selection.md`). Use it to decide whether the application needs prompting alone, retrieval (RAG), an agent, finetuning, or a combination, and which skills and stack layers each choice demands. Also use it to answer "prompt, RAG or finetune?" directly. The detailed design of each chosen pattern happens in the follow-on workflows named by `../routing.md`.

## Inputs needed

The use case, the evaluation criteria and usefulness threshold, current failure evidence if any prototype or baseline exists, what data exists and how sensitive it is, whether the model is hosted by you or a provider, and team skills and timeline. A failure analysis (what goes wrong and why) is the most valuable input; if none exists, the first output of this workflow is a plan to get one. See `intake.md` for how to ask.

## Modules to load

| Row | Module | Why it is needed here |
|---|---|---|
| C01-020 | [Three Layers of the AI Stack](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p093-three-layers-of-the-ai-stack.md) | Where each pattern lives; where to look for a problem |
| C01-021 | [AI Engineering Versus ML Engineering](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p097-ai-engineering-versus-ml-engineering.md) | Prompt-based versus weight-changing adaptation, skills each needs |
| C01-022 | [AI Engineering Versus Full-Stack Engineering](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p112-ai-engineering-versus-full-stack-engineering.md) | Product-first workflow; interface skills |
| C05-003 | [In-Context Learning: Zero-Shot and Few-Shot](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p420-in-context-learning-zero-shot-and-few-shot.md) | How many examples; cost of long prompts |
| C05-004 | [System Prompt and User Prompt](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p423-system-prompt-and-user-prompt.md) | Prompt structure and template risks |
| C05-005 | [Context Length and Context Efficiency](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p428-context-length-and-context-efficiency.md) | Limits of stuffing context |
| C06-003 | [RAG Architecture](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p498-rag-architecture.md) | Retriever and generator; what RAG needs |
| C06-008 | [Agent Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p536-agent-overview.md) | What an agent is; compound mistakes |
| C07-004 | [Reasons to Finetune](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p602-reasons-to-finetune.md) | When finetuning is justified |
| C07-005 | [Reasons Not to Finetune](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p604-reasons-not-to-finetune.md) | Costs, risks, prompting first |
| C07-006 | [Finetuning and RAG](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p611-finetuning-and-rag.md) | Information versus behavior failures; adaptation workflow |

## Procedure

1. **Place the work on the stack and on the adaptation spectrum.** Start at the application layer (prompts, context construction, interface, evaluation) and move down only as needed: model development (finetuning, datasets, inference optimization) then infrastructure (serving, compute, monitoring). Adaptation is either prompt-based (weights untouched; easier, less data; many successful applications use only this) or finetuning (weights change; more complex, more data; can improve quality, latency and cost; some adaptations are impossible without it). `[C01-020]` `[C01-021]`
2. **Start with prompting, and make the experiment real.** Establish a baseline with systematic prompt experiments: clear instructions, examples that represent real data, and defined metrics. INTERPRETATION: start zero-shot, add examples while measuring gain against prompt length and cost. The right number depends on the model and use case (the book's workflow says between 1 and 50), examples are capped by the context limit and raise inference cost, stronger models may gain little from few-shot, but domain-specific or rare-API tasks can gain a lot. Compare models and techniques under the same prompting setup: the book's Gemini example reversed a ranking once both were given the same number of examples. Define evaluation criteria first and use them at every step; version prompts. `[C05-003]` `[C07-005]` `[C07-006]` `[C01-021]`
3. **Fix prompt mechanics before blaming the model.** Put task description and developer instructions in the system prompt and the task and data in the user prompt, but experiment with placement. Follow the model's chat template exactly: template mismatches fail silently, so print the final prompt before sending and verify any third-party tool. `[C05-004]`
4. **Check context limits.** Models use the beginning and end of a long prompt better than the middle, so test with your own private needle-in-a-haystack style cases. Use private test content, so the model cannot answer from training data. If quality worsens steadily as context grows, shorten the prompt (INTERPRETATION: a reason to prefer retrieval over pasting everything). `[C05-005]`
5. **Classify the remaining failures** into information-based or behavior-based, with evidence from outputs. `[C07-006]`

   | Failure observed | Pattern to try | Why |
   |---|---|---|
   | Facts wrong, missing, private or outdated | RAG, starting with simple term-based retrieval (BM25-style) | The book's line: finetuning is for form, RAG is for facts; RAG beat finetuning on fresh-knowledge tasks in the cited study (small models, one benchmark family) |
   | Correct facts but irrelevant output, wrong format, wrong style, unsafe responses | Finetuning | It teaches syntax and style; semantic parsing into rare formats often needs it; low-quality training data can make hallucination worse |
   | Both | RAG first | No training data or model hosting needed |
   | Persisting information failures after simple retrieval | More advanced retrieval (embedding-based, hybrid) | Adds components to the inference pipeline |
   | Persisting behavior failures | Finetuning | Adds model-development complexity; inference unchanged |
   | Both persist | RAG plus finetuned model | The two are not exclusive; in the cited MMLU experiment, adding RAG to a finetuned model improved results 43% of the time and did not beat RAG alone the other 57% |

6. **Apply the finetuning gate** before choosing it. Finetuning is justified by a shown gap: weak task coverage (rare dialect, customer-specific queries), strict structured output, bias to counteract, or a need for a smaller, cheaper model (often distilled). `[C07-004]` INTERPRETATION (the book's checklist, phrased as a gate): finetuning is not justified until all four answers below are yes, or an alternative is recorded. `[C07-005]`
   - Systematic prompt experiments were run and the gap remains.
   - You have the data, training know-how, a serving plan and a maintenance policy (including how big a gain a new base model must show before you switch).
   - The gain justifies the cost relative to simply adopting a newer general model. The book's BloombergGPT case shows a costly domain model overtaken by a general model within the same month; be wary of "general models fail at domain tasks".
   - Other tasks will not regress, or are protected by multi-task data, separate models or merging.
   When yes, hand off to `finetune-decision.md` and `finetune-plan.md`. Note prompt caching has weakened the token-cost argument for finetuning, but finetuning has no limit on example count. `[C07-005]`
7. **Apply the retrieval gate.** If information failures are the cause, the design needs a retriever and a generator; retrieval quality decides success, and chunking, indexing and querying choices follow in `data-and-retrieval.md`. Joint or end-to-end finetuning of the two parts can help but is not required. `[C06-003]`
8. **Apply the agent gate.** An agent is a model with an environment it perceives and a set of actions and tools it can use; RAG systems are simple agents. Agents need stronger models because of compound mistakes: at 95% per-step accuracy, ten steps give about 60% and a hundred steps about 0.6%. INTERPRETATION: choose an agent only if the task needs multiple steps, tool use or planning that a fixed pipeline cannot cover, and require a per-step accuracy target and a step budget. Then continue in `agents-and-tools.md`. `[C06-008]`
9. **Assign skills and sequence the work.** Prompt-based work needs application-layer skills: prompts, context, evaluation, interface. Finetuning needs data, training and serving skills; many GPU-heavy needs arise from large models. INTERPRETATION: retrieval needs data and search engineering. Build the product first and invest in data and models once it shows promise, because models are available and fast iteration is rewarded; this favors full-stack skills and interface work. `[C01-020]` `[C01-021]` `[C01-022]`
10. **Record the pattern and the escalation path.** The book gives no universal workflow; its example flow is prompt, add examples, add simple retrieval, then complex retrieval or finetuning, then both. Each step needs evaluation to justify it. INTERPRETATION: state which evaluation result would move you to the next step. `[C07-006]`

## Evidence and exit gate

- Every pattern in the design is tied to an observed or predicted failure type with evidence (outputs reviewed, baseline metrics), or marked as an assumption to verify.
- Any finetuning, agent or complex retrieval choice has its gate answered in writing.
- The cheaper alternative was considered and the reason it was not enough is recorded.
- Evaluation criteria exist for each added component (see `eval-plan.md`); a pattern without a way to measure it is not accepted.

## Outputs

[decision-record.md](../../templates/decision-record.md): one record for the pattern choice and one for each rejected escalation. Fill sections 2 and 3 of [architecture-design.md](../../templates/architecture-design.md) with the pattern, diagram and components, and the routing to the follow-on workflows.

## Pitfalls

- Declaring "prompting does not work" after minimal, unsystematic experiments. `[C07-005]`
- Finetuning for facts that RAG supplies; finetuning for one task and degrading others. `[C07-005]` `[C07-006]`
- Silent chat-template errors. `[C05-004]`
- Assuming the middle of a long prompt is read as well as the ends. `[C05-005]`
- Choosing an agent for a task a fixed pipeline handles, or ignoring compound error. `[C06-008]`
- Assuming ML engineering is a must-have: for foundation models it widens the toolset and helps troubleshooting, though the book notes people dispute this. `[C01-021]`
- Treating the stack as only a model choice and neglecting evaluation and interface work. `[C01-020]` `[C01-022]`
