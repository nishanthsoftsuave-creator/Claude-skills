---
name: prompt-review
mode: review-test
rows: [C05-003, C05-004, C05-005, C05-007, C05-008, C05-009, C05-010, C05-011, C05-012, C05-013, C02-011, C02-014, C03-016]
---
# Prompt review

## When to use
The project has prompts (system prompts, templates, few-shot examples, prompt chains, structured-output instructions) and the user wants them reviewed or tested. Route here from `routing.md` for "Review prompts". Pair with `security-and-prompt-attacks.md` for injection and jailbreak probing, which this workflow does not cover.

## Inputs needed
- Prompt locations and how they are assembled at run time. Discovery (`../discovery.md`) normally answers this; ask only for what it did not (`../architect/intake.md` for how to ask).
- The model and endpoint each prompt targets, and whether prompts are built by a third-party tool or by the project's own code.
- For run checks only: explicit user permission to execute the project's own code or call a model, a spend cap for paid calls, and whether a small input set exists. Without these, run checks are `BLOCKED` or `NOT_RUN`, never `PASSED`.
- What "good output" means for each prompt (format, scale, tone, forbidden behaviour). If nobody has written it down, that is itself a finding (see PR-12).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C05-003 | [In-context learning](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p420-in-context-learning-zero-shot-and-few-shot.md) | Judge the number and value of few-shot examples |
| C05-004 | [System and user prompt](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p423-system-prompt-and-user-prompt.md) | Prompt structure and chat-template correctness |
| C05-005 | [Context length and efficiency](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p428-context-length-and-context-efficiency.md) | Prompt length, positions, needle-in-a-haystack style test |
| C05-007 | [Clear and explicit instructions](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p432-write-clear-and-explicit-instructions.md) | Clarity, persona, examples, output format |
| C05-008 | [Sufficient context](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p440-provide-sufficient-context.md) | Grounding, closed-world restriction |
| C05-009 | [Decomposition](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p442-break-complex-tasks-into-simpler-subtasks.md) | Bloated single prompts, chains |
| C05-010 | [Time to think](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p448-give-the-model-time-to-think.md) | Chain-of-thought and self-critique, and their latency cost |
| C05-011 | [Iterate](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p452-iterate-on-your-prompts.md) | Systematic testing of prompt changes |
| C05-012 | [Prompt engineering tools](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p453-evaluate-prompt-engineering-tools.md) | Hidden calls, tool-written prompts |
| C05-013 | [Organize and version](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p458-organize-and-version-prompts.md) | Separation from code, metadata, versioning |
| C02-011 | [Sampling fundamentals](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p188-sampling-fundamentals.md) | Why identical prompts give varying output; greedy vs sampled |
| C02-014 | [Structured outputs](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p206-structured-outputs.md) | Format enforcement layers and JSON-mode caveats |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | The book's limits of AI judges (inconsistent scores, unstandardized criteria, cost and latency, self, position and verbosity bias). The skill's `probable` cap for judge-only findings is INTERPRETATION built on them; pin and read the judge prompt, never trust an unseen one |

## Procedure
1. **Inventory.** List every prompt, where it is stored, which model it targets, and which are shared by several callers. Note which text is a prompt template filled by the application and which is a model's chat template (they are different things). Record where developer instructions sit (system or user part); the book says to experiment with the structure, and system-first placement may help because earlier instructions may be handled better. `[C05-004]`
2. **Structure and template.** For each prompt, identify the system part and user part and check the final assembled input, not the template alone. If the project builds the final input itself or through a library, require a way to print the final prompt; a missing or mismatched chat template fails silently (the model still answers plausibly), so treat any untested assembly as a risk. `[C05-004]`
3. **Clarity.** Per prompt, check that it states: the task, the scale or label set, what to do when unsure, forbidden behaviours, and the output shape. Decision rule: an unstated scale, tie-break or "don't know" behaviour is a finding; each unwanted behaviour seen in outputs should have a matching explicit instruction. Persona is optional; flag it only where the perspective the output needs is unstated (the book's persona example is one illustration, not a guaranteed effect). `[C05-007]`
4. **Examples.** Check whether examples exist and whether they earn their tokens. Rule: the right number of shots is found by experiment; more shots raise length and cost and are capped by context length; stronger models often need fewer. Compare a compact example format against a verbose one only if accuracy is equal. Examples matter more for domain-specific or rarely seen APIs. `[C05-003]` `[C05-007]`
5. **Output format.** If software parses the output: named keys are specified, a preamble is forbidden where unwanted, and classification-style prompts end with a marker that cannot occur in real inputs. INTERPRETATION (from the book's ordering): apply the structured-output ladder: prompting first, cheap post-processing for recurring slips, constrained sampling or finetuning only when invalid outputs are costly; an AI validator adds a second call per output. JSON mode guarantees valid JSON at most, not correct content, and truncation at the output token limit still breaks parsing. `[C05-007]` `[C02-014]`
6. **Sampling.** Record temperature and related settings. INTERPRETATION: greedy choice suits classification-style outputs; sampled generation gives variety, so a check that expects identical outputs across runs needs fixed settings or repeated trials. `[C02-011]`
7. **Context.** If answers depend on source material, confirm it is supplied or fetched. For closed-world behaviour, expect a context-only instruction, negative examples and a request to quote sources, and record that prompting alone gives no guarantee. Missing context pushes the model to internal knowledge, the route to hallucination. `[C05-008]`
8. **Decomposition.** Flag a single prompt that has grown large with many instructions, examples and edge cases, or that is hard to debug. Check for intermediate outputs that can be monitored and for independent steps that could run in parallel. Trade-off to report, not hide: extra steps raise perceived latency and call count (though smaller prompts may not double cost), while cheaper models can take simple steps such as intent classification. Step size is found by experiment. `[C05-009]`
9. **Reasoning.** If the task needs multi-step reasoning, check whether step-by-step (a one-line instruction, prescribed steps, or a worked example) or self-critique prompting is used, and whether its added tokens and wait time are accepted; self-devised long reasoning is the costliest form. `[C05-010]`
10. **Context length use.** Compute prompt size against the model's context limit. Check where critical instructions sit (start and end are handled better than the middle). Rule: if quality falls steadily as context grows, shorten the prompt. Test with private facts planted at different positions so training data cannot supply the answer (PR-09). Limits and model names in the book are dated May 2024; use the project's model documentation for its actual limit. `[C05-005]`
11. **Process and tooling.** Check for a fixed evaluation set and metrics, versioned prompts, tracked experiments, and system-level (not step-level) judgement of changes; check that model quirks (placement preference, model-specific prompting guide) were looked up, not assumed. If a prompt-optimization tool or library writes prompts, require that someone reads the generated prompts and that the number of model calls it makes is tracked. Keep-it-simple: tools were not the book's starting point. `[C05-011]` `[C05-012]`
12. **Organization and versioning.** Prompts live apart from application code; each has metadata (model, use case, owner, date) and ideally its input and output schema and sampling parameters; versioning is git or a catalog. INTERPRETATION: git suffices for one consumer; once several applications share a prompt and need independent upgrade, an explicit-version catalog is the book's answer to git's forced-upgrade coupling. `[C05-013]`
13. **Test run (only with permission and a spend cap).** Build 10 to 30 inputs: typical, edge cases, and cases from observed failures. Write the acceptance criterion per input before running. Run through `run_check.py` (PR-06 to PR-08), compare to criteria, and re-run each failure once. INTERPRETATION: the size is a pragmatic floor, not a book figure.

## Checks
Run commands as `python scripts/run_check.py --case <ID> --evidence-dir <run>/evidence -- <command>`. The commands are the project's own scripts, a test runner, or a small script the user approves.

| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| PR-01 | Prompt inventory complete, stored apart from code, with metadata | Search and read prompt files and call sites | `PR-01-notes.md` listing prompts, owners, versions | review | C05-013 | Prompts hard-coded inline across call sites with no owner or version: finding (`recommendation`, `probable` if it blocks safe change) |
| PR-02 | Final assembled prompt matches the model's chat template | Review the assembly code; where allowed, run the project's own print or debug path through `run_check.py` | `PR-02-notes.md`, or `PR-02.exec.json` plus printed prompt | review (run if a print path is run) | C05-004 | Third-party or hand-built assembly with no template verification: `risk`; a printed prompt that deviates from the documented template: `confirmed` |
| PR-03 | Instruction clarity: scale, uncertainty rule, output shape, forbidden behaviour | Read each prompt against the checklist in step 3 | `PR-03-notes.md` per prompt | review | C05-007 | Missing item that outputs show is exploited: `probable`; missing item with no output evidence: `recommendation` |
| PR-04 | Few-shot examples justified; compact format considered | Read examples; compare zero-shot vs few-shot on the PR-06 set where permitted | `PR-04-notes.md`, optionally `PR-04.exec.json` | review (run if compared) | C05-003 | Many examples with no measured gain over fewer: `recommendation`; examples contradicting the stated rules: `probable` |
| PR-05 | Parsed outputs have format contract, marker and fallback | Review prompt plus parser; where allowed run the parser on sample outputs | `PR-05-notes.md`, optionally `PR-05.exec.json` | review (run if parser run) | C02-014, C05-007 | Parser fails on a sample the model can plausibly emit (truncation, preamble): `confirmed` if reproduced, else `risk` |
| PR-06 | Prompt input set run against acceptance criteria | Project's own runner over the 10-30 inputs (needs permission and spend cap) | `PR-06.exec.json`, `PR-06-responses.*`, criteria file | run | C05-011 | Share of inputs missing criteria is reported, not thresholded (no book threshold); any criterion violation is reproduced once before it is `confirmed` |
| PR-07 | Output variation under the project's sampling settings | Same input run several times (needs permission and cap) | `PR-07.exec.json`, `PR-07-responses.*` | run | C02-011 | Variation that breaks a downstream parser or the criterion: `confirmed`; variation only in wording: not a defect |
| PR-08 | Prompt change compared on the fixed set at system level | Run old and new version on the same set and the same metric | `PR-08.exec.json`, comparison table | run | C05-011 | New version helps a step but worsens end-to-end result: failure of the change, `confirmed` if reproduced |
| PR-09 | Long-context position test with private planted facts | Script (user-approved) places a private fact at start, middle, end of a realistic-length input | `PR-09.exec.json`, per-position results | run | C05-005 | Lower recall in middle positions or falling quality with length: `confirmed`; a judge-only verdict is capped at `probable` (limits of AI judges: `[C03-016]`) |
| PR-10 | Decomposition: bloated or hard-to-debug prompt | Review prompt size, count of intents handled, intermediate visibility | `PR-10-notes.md` | review | C05-009 | One prompt serving many intents with no intermediate output to inspect: `recommendation`, with the latency and cost trade-off stated |
| PR-11 | Reasoning prompts and their cost | Review for step-by-step or self-critique use against latency budget | `PR-11-notes.md` | review | C05-010 | Long self-devised reasoning on a latency-critical path: `risk` |
| PR-12 | Context sufficiency and closed-world restriction | Review prompts; probe with out-of-context questions (run, if permitted) | `PR-12-notes.md`, optionally `PR-12.exec.json` | review (run if probed) | C05-008 | Model answers an out-of-context question from internal knowledge where closed-world is required: `confirmed` if reproduced; no guarantee is expected from prompting alone |
| PR-13 | Prompt tooling: generated prompts read, hidden calls tracked | Review tool config, call logs or billing view | `PR-13-notes.md` | review | C05-012 | Tool in use with no reading of its prompts or call accounting: `risk` |
| PR-14 | Versioning approach fits sharing pattern | Review repository layout and who consumes each prompt | `PR-14-notes.md` | review | C05-013 | Shared prompt with git-only versioning that forces simultaneous upgrades: `recommendation` |
| PR-15 | Prompt-size and context headroom | Review token counts against the model limit | `PR-15-notes.md` | review | C05-005 | Prompt near the limit with no handling for overflow: `risk` |

## Evidence and exit gate
- Every run check has an exec record from `run_check.py`; every review check has notes naming files and lines read.
- Each failure was re-run once; differing results are reported as unstable, not as passes.
- No model call was made without approval and a cap; no secret appears in evidence.
- Exit gate: each check is `PASSED`, `FAILED`, `BLOCKED`, `SKIPPED`, `NOT_RUN` or `REVIEWED` with its reason, and `python scripts/validate_report.py <run_dir>` prints 0 problems.

## Outputs
Add the check results to the run's results data and the findings report (`../../templates/findings-report.md`). Findings carry the row ids as criteria.

## Pitfalls
- Reviewing the template and never the assembled prompt: template errors fail silently. `[C05-004]`
- Treating a single run as proof; sampling makes outputs vary. `[C02-011]`
- Assuming valid JSON means correct content. `[C02-014]`
- Evaluating a prompt edit on one step only. `[C05-011]`
- Trusting a tool-generated or tool-modified prompt unread. `[C05-012]`
- Reading time-sensitive book figures (context limits, example models, template formats) as current. `[C05-005]` `[C05-004]`
