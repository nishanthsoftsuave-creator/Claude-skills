---
name: failure-diagnosis
mode: review-test
rows: [C02-012, C02-013, C02-014, C02-015, C03-002, C06-011, C05-003, C05-005, C03-016]
---
# Failure diagnosis

## When to use
The user reports a failure in an AI feature: hallucination, inconsistent answers, wrong output format, poor retrieval, an agent loop or wrong action, a regression after a change, or a cost spike. The procedure is hypothesis-driven. It never asserts a root cause beyond the evidence, and it asks before it guesses.

## Inputs needed
- The symptom in the user's words, a concrete example (input, actual output, expected output), when it started, and what changed (model version, prompt, data, settings, traffic). Discovery answers some of this; ask only for the rest (see `../architect/intake.md` for how to ask: at most four questions per round, each with a recommended default).
- How often it happens: every time, sometimes, or once. Frequency separates a sampling effect from a deterministic defect `[C02-015]`.
- Access: logs, traces, prompt files, settings, the ability to replay a request. Paid replays need approval and a spend cap.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C02-012 | [Sampling Strategies](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p191-sampling-strategies.md) | temperature, top-k, top-p, stopping conditions, logprobs |
| C02-013 | [Test Time Compute](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p199-test-time-compute.md) | multiple candidates, selection, robustness |
| C02-014 | [Structured Outputs](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p206-structured-outputs.md) | why format fails and the five fix layers |
| C02-015 | [The Probabilistic Nature of AI](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p214-the-probabilistic-nature-of-ai.md) | inconsistency, hallucination hypotheses |
| C03-002 | [Challenges of Evaluating Foundation Models](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p234-challenges-of-evaluating-foundation-models.md) | why a failure can go unseen or unmeasured (open-ended outputs, eyeballed evaluation) |
| C06-011 | [Agent Failure Modes and Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p576-agent-failure-modes-and-evaluation.md) | planning, tool and efficiency failures |
| C05-003 | [In-Context Learning](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p420-in-context-learning-zero-shot-and-few-shot.md) | examples, prompt length and cost |
| C05-005 | [Context Length and Context Efficiency](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p428-context-length-and-context-efficiency.md) | position effects, long-context degradation |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | judge inconsistency, changing or opaque judges, biases; why judge-only evidence is capped at `probable` (the cap is the skill's rule in `SKILL.md`) |

Poor retrieval is not diagnosed here: hand it to `retrieval-review.md` (and `data-review.md` for the corpus) and load the modules those name. Judge-scored evidence is classified in `evidence-and-confidence.md`; the judge limits are in `[C03-016]`.

## Procedure
1. **Restate and classify.** One sentence: what was expected, what happened, how often. Assign the symptom to a branch below. A symptom may sit in several.
2. **List unknowns.** Write what you do not know (settings used, model version, whether the prompt changed, the baseline behaviour, how success was ever measured). Ask the one to three targeted questions that would eliminate the most hypotheses. If the user cannot answer, proceed on stated assumptions and label the result `unverified` or `probable`.
3. **Establish whether the failure was ever measurable.** Evaluation of open-ended output is hard and many teams only eyeball results, so a "regression" may be an unmeasured change `[C03-002]`. If no eval set exists, say so; a regression claim then rests on anecdote, label it `unverified` and propose a small fixed prompt set as the first step.
4. **Pick hypotheses from the branch table, cheapest test first.** Write each as "if H, then we should see E". Run the cheap test (read config, replay once with fixed settings, inspect logs) before any paid or invasive one.
5. **Test and update.** Record each hypothesis as supported, refuted or untested. A hypothesis is `confirmed` only when a `run_check.py` record reproduces the failure and a controlled change removes it. Otherwise it is `probable` at best, or `risk` or `unverified`.
6. **Stop when the evidence stops.** Report the leading hypotheses with the evidence missing for each, not a single cause stated as fact.

### Branch table (hypotheses and cheap tests)
| Symptom | Hypotheses from the book | Cheap test |
|---|---|---|
| Inconsistent answers (same input, different output; tiny input change, big change) | Sampling is probabilistic; variables not fixed (temperature, top-p, top-k, seed); hardware differences prevent a 100% guarantee; input-wording sensitivity that fixing settings will not cure `[C02-015]` `[C02-012]` | Read the sampling settings; replay the same input several times at temperature 0 and compare; if it still varies, note hardware or provider control limits `[C02-015]`; where the provider exposes logprobs, inspect the token probabilities `[C02-012]`. Mitigations to recommend: cache repeated answers, fix variables and seed, sharper prompts, memory `[C02-015]` |
| Hallucination | Self-delusion (the model treats its own earlier tokens as fact, so errors snowball) and mismatch between labeler and model knowledge; the book offers these as complementary hypotheses, neither settled for a given case `[C02-015]`. INTERPRETATION: also missing or poor context, since the book says context construction can help `[C02-015]` | Check whether the first wrong claim appears early and later text builds on it; check whether the needed fact was in the context; ask for a concise answer or an "I don't know" allowance as a test, since fewer tokens leave fewer chances to invent `[C02-015]`. If the fact was missing or wrongly retrieved, switch to the retrieval branch below. Detecting hallucination is hard; do not call an output a hallucination without a checked reference |
| Wrong or unparsable format | Truncation at a token limit or stop condition (valid JSON can still be cut off); JSON mode guarantees valid JSON, not correct content; the model is weak at the format `[C02-012]` `[C02-014]` | Inspect finish reason, max-output setting and stop sequences; count how many failures are truncations; check whether a cheap post-processing fix would catch the recurring slip `[C02-014]` |
| Poor quality only on long prompts | Position effects: instructions or evidence in the middle are used worse than at the start or end; context too long `[C05-005]`; many few-shot examples inflating length and cost `[C05-003]` | Move the key instruction or document to the start or end and replay; shorten the prompt; compare zero-shot against the current number of examples (the book reports few-shot gains can be small for stronger models yet large for domain-specific or rarely seen tasks) `[C05-003]`. Test with private data so the model cannot answer from training memory `[C05-005]`. Fuller prompt review: `prompt-review.md` |
| Agent loop, wrong tool, wrong action | Invalid tool; valid tool with invalid parameters; valid tool with wrong values; goal failure including ignored constraints; time as an overlooked constraint; reflection error (claims done when not); tool itself wrong, or a translation error between plan and command; missing tool; inefficiency `[C06-011]` | Read the tool-call trace: classify each failed step into those categories; test each tool alone; count steps and cost per task against a baseline (another agent or a human; efficiency differs between them) `[C06-011]`. Fuller agent, tool and memory review: `agent-review.md` |
| Regression after a change | A model or provider update, a prompt edit, a settings change, or a judge or metric that changed `[C03-002]` `[C02-015]` | Diff prompts, settings and model version; replay a fixed set on old and new; do not trust a metric whose judge model or prompt changed or cannot be seen `[C03-016]` |
| Cost spike | Longer prompts (more shots, longer context) `[C05-003]` `[C05-005]`; more candidates per query (the book says two outputs cost about twice one; INTERPRETATION: roughly proportional) `[C02-013]`; longer outputs or no stopping condition `[C02-012]`; agent step inflation `[C06-011]` | Compare token counts per request before and after; check best-of-N settings, max output and step counts; hand the lever analysis to `perf-cost-latency.md` |
| Poor retrieval (wrong, missing or stale documents; answer ignores the context) | INTERPRETATION: a retrieval or corpus problem rather than a generation one (the book's retrieval material is in `retrieval-review.md`) | Check whether the needed fact was in the retrieved context at all; then run `retrieval-review.md` and `data-review.md`. Not diagnosed in this workflow |

7. **Repair options, to recommend only.** For format failures use the ordering: prompt, post-process, test-time selection, constrained sampling, finetuning; the first three are for a model already near the format, the last two for harder cases `[C02-014]`; a validating second model call adds cost and latency `[C02-014]`. Where outputs need selection use majority vote for exact answers, a verifier or reward model for scored tasks, or a validity check such as valid SQL `[C02-013]`; sampling many outputs raises cost, and the book's evidence is mixed (one experiment peaked near 400 samples, another kept improving) `[C02-013]`. Do not apply fixes unless the user asks.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| FD-01 | Sampling variables and seed on the failing path | read config and call sites | notes | review | C02-012 | unfixed variables on a task that needs consistency: `probable` cause of inconsistency |
| FD-02 | Same-input repeatability | replay one approved request N times with fixed settings via `run_check.py` | `FD-02.exec.json` and outputs | run | C02-015 | different outputs at fixed settings: finding `probable` (hardware or provider limits cannot be excluded) |
| FD-03 | Truncation or early stop on format failures | inspect finish reasons and limits in logs | log excerpts | review | C02-014 | failures coincide with the limit: `probable`; replay with a higher limit removes them: `confirmed` |
| FD-04 | Format validity rate | run the user's own parser over saved outputs via `run_check.py` | exec record with counts | run | C02-014 | invalid rate above the stated tolerance: FAILED |
| FD-05 | Prompt length and key-instruction position | read the prompt template; replay with the key item moved | notes; run record if replayed | review | C05-005 | accuracy changes with position: `probable` |
| FD-06 | Few-shot count against gain and cost | compare token counts and eval results at different shot counts | notes | review | C05-003 | many shots, no measured gain: `recommendation` |
| FD-07 | Agent failure classification | classify a trace into the C06-011 categories | notes with counts per category | review | C06-011 | cannot classify for lack of tool-call logs: `BLOCKED` |
| FD-08 | Per-tool correctness | run each tool alone on known inputs via `run_check.py` | exec records | run | C06-011 | wrong output from a tool alone: FAILED, finding `confirmed` with repro |
| FD-09 | Measurability of the failure | check for an eval set or metric history | notes | review | C03-002 | none exists: `unverified` regression claim, recommend a fixed set |
| FD-10 | Candidate selection in use | read code for best-of-N, voting, verifiers | notes | review | C02-013 | cost spike tracks N: `probable` |

## Evidence and exit gate
- Each diagnosed failure ends with: symptom, hypotheses with status, evidence per status, unknowns, the next question or test. A root cause appears only as `confirmed` (reproduced and removed by a controlled change) or is labelled hypothesis.
- Judge-scored evidence caps a finding at `probable` (judge limits in `[C03-016]`; method in `evidence-and-confidence.md`).
- If logs or traces are too thin to test any hypothesis, say so, mark the cause `unverified`, and suggest `observability-review.md`; if no eval exists, suggest `eval-execution.md`.
- Gate: the user has seen the unknown list and answered or waived each question.

## Outputs
Cases and findings in `results.json` for `report.md`; unresolved items go to "Unverified items". Redesign implications go to `handoff-to-architect.md`.

## Pitfalls
- Declaring "the model hallucinated" as a cause; the book gives two complementary hypotheses and neither is settled for a given case `[C02-015]`.
- Treating temperature 0 as a determinism guarantee `[C02-015]`.
- Blaming the model for truncated JSON caused by a stop condition `[C02-012]`.
- Believing a regression you cannot measure `[C03-002]`.
- Benchmarks and model comparisons cited in the modules are dated; treat them as time-sensitive `[C02-015]` `[C05-003]` `[C05-005]`.
- Retesting with paid calls without an approved spend cap.
