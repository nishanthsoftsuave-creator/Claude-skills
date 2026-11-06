---
name: structured-outputs-and-sampling
mode: architect
rows: [C02-011, C02-012, C02-013, C02-014, C02-015]
---
# Structured outputs, sampling and output reliability

## When to use
Run after `solution-pattern.md` when the design has any of: output a program must parse (JSON, SQL, regex, tool calls, classes), a need for repeatable answers, factual claims a user could act on, or a quality bar that one sampled answer may not meet. Skip the structured-output steps only if every output is free text read by a person, and say so in the decision record.

## Inputs needed
Take from discovery and `intake.md`; ask only for what is missing:
- Who or what consumes each output (person, parser, downstream tool) and the exact format required.
- Cost of a wrong or malformed output (drives how much invalid-output rate is tolerable).
- Latency and cost ceilings per request.
- Whether the model is self-hosted or behind an API (decides which sampling controls, logprobs, seeds and logits are reachable).
- Whether a quality signal exists for choosing among candidates (reward model, verifier, programmatic check, exact answers).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C02-011 | [Sampling Fundamentals](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p188-sampling-fundamentals.md) | Logits, probability distribution, greedy vs sampled choice |
| C02-012 | [Sampling Strategies](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p191-sampling-strategies.md) | Temperature, top-k, top-p, logprobs, stopping conditions |
| C02-013 | [Test Time Compute](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p199-test-time-compute.md) | Generate several outputs and select; cost and limits |
| C02-014 | [Structured Outputs](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p206-structured-outputs.md) | Five layers for format reliability |
| C02-015 | [The Probabilistic Nature of AI](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p214-the-probabilistic-nature-of-ai.md) | Inconsistency and hallucination, causes and mitigations |

## Procedure
1. **Classify each output by consumer.** Two scenarios need structure: tasks that are inherently structured (semantic parsing such as text-to-SQL or text-to-regex, classification into valid classes) and tasks whose free-form result feeds a downstream program, including agent tool inputs. Mark each output type in the design as structured, parsed-downstream or free text. `[C02-014]`
2. **Understand what the model actually emits.** The model produces a probability distribution over the vocabulary for the next token, and logits are raw per-token values, not probabilities. Greedy choice often suits classification (the book); that sampling is what gives language output variety, and greedy gives dull text, is the book's argument. INTERPRETATION: use greedy-like settings for classification-style outputs. Where the provider exposes logprobs they help for classification, evaluation and sanity checks. `[C02-011]` `[C02-012]`
3. **Set sampling controls per output type.** Use the table, then confirm the values by experiment because the book says to find what suits the application. `[C02-012]`

| Need | Control | Book guidance |
|---|---|---|
| Consistency, extraction, classification | Temperature 0 (the model then picks the largest logit) | Common practice for consistent output; creativity drops `[C02-012]` |
| Creative or varied text | Higher temperature | The book cites 0.7 as often recommended; very high risks incoherence `[C02-012]` |
| Cap candidates, cut compute | Top-k | k from 50 to 500 `[C02-012]` |
| Candidate count varies by prompt | Top-p | p from 0.9 to 0.95 `[C02-012]` |
| Minimum-probability filter | Min-p | Related option `[C02-012]` |

   Providers often limit temperature to 0-2 and may not expose logprobs; these are stated as of the book's writing, so check the chosen provider. `[C02-012]`
4. **Set stopping conditions with format in mind.** Token limits and stop tokens control latency and cost, but stopping early can drop closing brackets and break JSON. Too high a maximum slows and raises cost. Valid JSON from JSON mode can still be truncated and means only valid syntax, not correct content. `[C02-012]` `[C02-014]`
5. **Climb the structured-output ladder only as far as the failure cost requires.** `[C02-014]`

| Layer | Use when | Limits |
|---|---|---|
| Prompting (instruct the format) | Always first | No guarantee; a few percent invalid may be unacceptable. An AI validator adds at least one more call |
| Post-processing (script that repairs common slips) | Mistakes are repeated and easy to fix | Book cites LinkedIn's defensive YAML parser raising correct output from 90% to 99.99% (the book also notes YAML needs fewer output tokens than JSON) |
| Test time compute (regenerate until valid) | Validity is cheap to check, e.g. valid SQL | Multiplies cost, see step 6 |
| Constrained sampling (filter logits by a grammar) | Format must be guaranteed and you control sampling (self-hosted or a supporting tool) | A grammar per format, extra latency, poor generality; some argue the effort is better spent training models to follow instructions |
| Finetuning on the format | Book: most effective and general, any format. INTERPRETATION: pick when many formats or high volume make the lighter layers insufficient | More reliable than prompting, not a guarantee; for classification a classifier head can only emit predefined classes |

   Decision rule: the first three are bandages for a model already near the format; constrained sampling and finetuning are the intensive treatments. Frameworks named in the book (guidance, outlines, instructor, llama.cpp) are examples and time-sensitive. The book expects better instruction following to make these techniques matter less over time, so revisit the layer when the model changes. If finetuning is being considered, hand the question to `finetune-decision.md`. `[C02-014]` `[C02-012]`
6. **Decide whether to sample several outputs.** The book supports each selection example separately; mapping them to task types is INTERPRETATION. `[C02-013]`
   - Exact-answer tasks: majority vote.
   - A quality signal exists: reward model or verifier scoring.
   - Format-bound tasks: keep generating until valid.
   - Latency-bound: generate in parallel, show the first valid result.
   - Otherwise: highest average logprob (length-normalised, because summed logprobs bias toward short outputs; the book says the OpenAI API did this at the time of writing) or an application heuristic such as shortest candidate.
   - Candidate generation: independent samples (Best of N) or beam search, which keeps the most promising partial sequences. Less robust models gain more from multiple samples.

   Vary sampling variables to raise diversity. The book says two outputs cost about twice one; INTERPRETATION: cost grows roughly in proportion to N. Gains are not settled: in one OpenAI experiment performance rose to about 400 outputs then fell (the book's hypothesis: more samples find outputs that fool the verifier), while a Stanford study found solved problems growing log-linearly up to 10,000 samples; the book notes nobody in production likely samples 400 or 10,000. Set N by budget, then measure the gain. A finding resting on one study is not a threshold. `[C02-013]`
7. **Plan for inconsistency.** Two forms: same input giving different outputs, and a slightly changed input giving a very different output. Mitigations for the first: cache answers, fix temperature/top-p/top-k, fix the seed. Fixed settings do not guarantee 100% consistency because hardware affects results, and API providers control that. For the second, fixing settings does not help; use careful prompts and a memory system. `[C02-015]`
8. **Plan for hallucination, which has no complete fix.** Two hypotheses: self-delusion (the model cannot tell given data from its own output, so errors snowball) and mismatch between labeler and model knowledge. Design accordingly: `[C02-015]`
   - Prompt for truthfulness and "I don't know", and ask for concise answers (fewer tokens, fewer chances to invent). INTERPRETATION: treat these as cheap partial mitigations, not guarantees.
   - Ground answers with context construction (see `data-and-retrieval.md`) and add detection, which the book places in Chapter 4 (see `eval-plan.md`).
   - Do not assume RLHF-tuned models hallucinate less: the book's InstructGPT table shows the hallucination metric rose against SFT alone. `[C02-015]`
9. **Write one decision record per output type** with the chosen controls, ladder layer, selection method (or "single sample") and the consistency and hallucination mitigations, each with its book citation.

## Evidence and exit gate
Exit when: every output type has a classified consumer and a format; sampling values are stated with the experiment that will confirm them; the ladder layer is justified against the cost of an invalid output; any multi-sample design states N, the selection method and the cost multiplier; consistency limits and hallucination mitigations are listed with residual risk. For each choice, state what will be measured (invalid-output rate, run-to-run agreement on a fixed input set, grounded-answer rate) so `eval-plan.md` can schedule it. Unknown provider capabilities (logprobs, seed, logit access) are recorded as assumptions.

## Outputs
Fill [../../templates/decision-record.md](../../templates/decision-record.md) once per output type, and pass the measures to [../../templates/eval-plan.md](../../templates/eval-plan.md). Feed constraints to [../../templates/architecture-design.md](../../templates/architecture-design.md).

## Pitfalls
- Treating JSON mode as correctness: it guarantees syntax at best, and truncation still breaks parsing. `[C02-014]`
- Cutting output length for cost and breaking structured output. `[C02-012]`
- Assuming temperature 0 gives identical outputs across runs or machines. `[C02-015]`
- Choosing logprob sum without length normalisation, which favours short outputs. `[C02-013]`
- Sampling very many candidates against a learned verifier: the book's hypothesis is that the verifier can be fooled as N grows. `[C02-013]`
- Relying on logprobs or logits where the provider does not expose them. `[C02-012]`
- Expecting a hallucination fix from one prompt line. `[C02-015]`
- Quoting book numbers (provider ranges, study results) as current; they are time-sensitive. `[C02-012]` `[C02-013]`
- Greedy or low-temperature settings on tasks that need variety, producing dull output. `[C02-011]`
