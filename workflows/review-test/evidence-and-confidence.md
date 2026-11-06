---
name: evidence-and-confidence
mode: review-test
rows: [C03-002, C03-014, C03-015, C03-016, C03-017]
---
# Evidence and confidence: classify every finding

## When to use
After `run-checks.md`, before `scripts/validate_report.py` and the report. Use it to give each finding its label (`confirmed`, `probable`, `risk`, `recommendation`, `unverified`), to apply the cap when AI-as-judge is involved, and to review any AI-judge setup the project itself uses.

## Inputs needed
- `<run>/results.json` with case statuses, exec records and evidence files.
- For any case that used a judge (the project's or one this run used): the judge model, the full judge prompt, the sampling settings, and what the judge saw.
- The approved plan's guideline (criteria, rubric, usefulness threshold), or the note that it was assumed.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C03-002 | [Challenges of Evaluating Foundation Models](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p234-challenges-of-evaluating-foundation-models.md) | Why open-ended output resists ground truth; eyeballing is weak evidence |
| C03-014 | [Why AI as a Judge?](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p272-why-ai-as-a-judge.md) | What a judge is good for, and the trust caveat |
| C03-015 | [How to Use AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p274-how-to-use-ai-as-a-judge.md) | A judge is model plus prompt; what a sound judge prompt contains |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | Inconsistency, unstandardized criteria, cost, biases: the basis of the cap |
| C03-017 | [What Models Can Act as Judges?](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p290-what-models-can-act-as-judges.md) | Stronger, weaker, same-model and specialized judges |

## Procedure
1. **Identify the basis of each finding.** For each candidate finding, list the cases behind it and ask what actually established it: a deterministic check (test run, exact match, functional correctness, measured latency), a read of code or config, an AI judge's verdict, a person's eyeball opinion, or nothing observed. Evidence from output that "looks right" or "looks wrong" is the weakest kind; open-ended output has no complete list of correct answers and smarter models are harder to judge by sound alone. `[C03-002]`
2. **Apply the confidence ladder.** Pick the highest rung the evidence supports, never higher.

| Label | Requires | Cannot be used when |
|---|---|---|
| `confirmed` | a `FAILED` case with an exec record, the failure re-run once with `rerun` = `same`, `basis` = `deterministic` (not `judge`), repro steps, impact, evidence files, severity `[C03-016]` (the validator enforces a `FAILED` case, evidence, severity, repro steps, impact and `basis` not `judge`; the exec record and `rerun` = `same` are this skill's stricter rules) | evidence rests only on a judge, on reading code, or on an unrepeated run |
| `probable` | evidence exists (exec record, output file, sample) but one of: judge-only basis, failure not reproduced, rubric or guideline assumed, sample too small, or a failing case whose cause is not isolated `[C03-016]` | no evidence file exists |
| `risk` | a `REVIEWED` case shows exposure (a missing safeguard, an unpinned model) with no observed failure | a failure was observed (then it is probable or confirmed) |
| `recommendation` | an improvement the book supports, with no failure claimed | used to soften a real failure |
| `unverified` | the concern could not be checked (`BLOCKED`, `NOT_RUN`) and the report says what would settle it | evidence exists that settles it |

3. **Cap judge-only findings at `probable`.** A finding that rests only on an AI judge's verdict is `probable`, with `basis` = `judge`; `validate_report.py` rejects `confirmed` with that basis. Reasons the book gives: judges are probabilistic, so the same input can score differently across runs or with different wording; high consistency is not accuracy (putting examples in the prompt raised one 2023 judge's consistency from 65% to 77.5% but quadrupled its cost, time-sensitive); criteria are not standardized across tools; the judge is a model plus a prompt plus sampling settings, and changing any of them changes the judge; and judges have biases (self-bias, first-position bias, verbosity bias; the last two may fade in stronger models). `[C03-016]` `[C03-015]` The book's own verdict is that judges should be supplemented with exact evaluation and/or human evaluation. `[C03-016]` To lift a finding above the cap, obtain an exact or deterministic check that fails the same way (the finding's basis is then `deterministic`), or record human verification as evidence and say so; keep the label `probable` unless the failure also reproduces. INTERPRETATION: human verification here means the user's own confirmation, saved as a note in `evidence/`.
4. **Treat this skill's own judgement the same way.** INTERPRETATION: when the skill itself reads an output and decides it is wrong or hallucinated, that is an AI judgement by a model with its own biases (it can also favour its own style and longer answers `[C03-016]`). Record such a case as `REVIEWED`, use `basis` = `judge`, and do not confirm on it.
5. **Weigh what a judge is good for.** Judges are fast, cheap relative to people, need no reference data and can apply any criterion, so they are a legitimate signal where nothing else exists, and even an imperfect one may be good enough to steer development. `[C03-014]` That is why a judge finding is kept at `probable` instead of discarded. A judge's agreement with humans in a study (for example 85% against 81% human-to-human, 2023, time-sensitive) applies to that model, prompt and benchmark only. `[C03-014]`
6. **Check any judge used in this run** (and, in review, any judge the project uses) against the checks below. Evidence about judge quality can raise or lower the weight of a judge-based `probable` finding but never lifts it past `probable`.
7. **Resolve conflicts downwards.** If a judge says pass and an exact check says fail, the exact check wins. If two runs differ, report the lower rung, state the variance, and show both exec records. If the guideline was assumed, the finding is `probable` at most.
8. **Assign severity** (needed for `confirmed` and `probable`). INTERPRETATION, not from the book: `critical` = harm to users or data exposure in normal use; `major` = a core criterion or hard requirement is missed; `minor` = a quality shortfall with a workaround; `trivial` = cosmetic. State the impact in the user's terms.
9. **Write what would upgrade it.** For every `probable`, `risk` and `unverified` item state the single check that would move it up (for example "run the test cases through `run_check.py`", "provide a staging endpoint").
10. **Update `results.json`** so each finding has `id`, `case_ids` (each must exist in `cases`; a `confirmed` finding's cases must all be `FAILED`, and every `FAILED` case must be referenced by some finding), `label`, `severity` (required for `confirmed` and `probable`), `title`, `evidence` (required for `confirmed` and `probable`; files that exist), `basis` (`deterministic`, `judge` or another short word such as `review`; only `judge` is special to the validator), and `repro_steps` (a list) and `impact` for `confirmed`. Then run `python scripts/validate_report.py <run>`.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| EC-01 | Every `confirmed` finding sits on a `FAILED` case, deterministic basis, re-run noted | read `results.json` against the ladder; the validator run itself is recorded as RP-01 in `report.md` | notes | review | C03-016 | anything the ladder or validator rejects: relabel to `probable` |
| EC-02 | The project's judge (if any) has model, prompt and sampling settings visible and pinned; no score from a judge whose model and prompt cannot be seen is relied on | read judge code and config | notes | review | C03-016 | not visible or not pinned: `risk` |
| EC-03 | The judge prompt states task, criteria and scoring system, with scored examples; the criterion is defined in the project's own words, not just a tool's built-in name | read the judge prompt | notes | review | C03-015 | missing elements: `recommendation` |
| EC-04 | Scoring uses classification or a small discrete scale rather than a wide or continuous one (book: classification reported to work better than numbers, discrete better than continuous, wider ranges worse, examples help) | read the judge prompt | notes | review | C03-015 | wide scale with no examples: `recommendation` |
| EC-05 | Judge results are checked against an exact method or human review | read eval reports | notes | review | C03-016 | judge-only quality claims: `risk` |
| EC-06 | Bias controls: answer order randomized or repeated in pairwise tests; judge differs from the generating model where self-bias matters; length not rewarded blindly | read eval code | notes | review | C03-016 | pairwise judge with fixed order and same model: `risk` |
| EC-07 | Judge is fixed across before-and-after comparisons; trend claims note any judge or prompt change | read eval history | notes | review | C03-016 | metric trend with a changed judge: `probable` invalidation of the trend |
| EC-08 | Judge choice fits the need: stronger judge on a sampled subset, weaker judge as background monitor, self-critique for sanity checks only, or a small specialized judge for a narrow judgement | read eval design | notes | review | C03-017 | strongest model judging itself as sole check: `risk` |
| EC-09 | Cost and latency of judge calls are accounted for (the book: a judge on every call of the same model roughly doubles calls; three evaluation prompts make four times the calls; judging before replying adds latency; spot-checking a subset lowers cost but can miss failures) | read config and spend records | notes | review | C03-016 | unbudgeted judge in a hot path: `risk` |

## Evidence and exit gate
Every finding has a label that the ladder allows, a basis, evidence files that exist, and a stated upgrade path where it is below `confirmed`. No `confirmed` finding has `basis` = `judge`. `validate_report.py` prints 0 problems. If it fails, correct `results.json` to match reality; never weaken the check.

## Outputs
Final labelled findings inside `results.json`, ready for `report.md` and `../../templates/findings-report.md`. The report must repeat the caveat that judge-based findings are `probable`.

## Pitfalls
- INTERPRETATION: using the judge's fluent explanation as proof. The book values explanations for auditing results `[C03-014]`; an explanation justifies a score, it does not verify it.
- Trusting a judge because it agreed with humans in someone else's study; the agreement was for a specific model, prompt and benchmark. `[C03-014]`
- Comparing scores from different tools' built-in criteria: the same word ("faithfulness", "relevance") hides different prompts and scales. `[C03-016]`
- Reading a month-over-month rise as improvement without checking that the judge did not change. `[C03-016]`
- Using a model to judge its own output as the only check. `[C03-017]`
- Letting an eyeballed impression become a confirmed defect. `[C03-002]`
- Assuming a weaker judge is useless or a stronger judge unnecessary: the book leaves the weaker-judge case open, so state the limit rather than the answer. `[C03-017]`
- Sending proprietary data to an external judge without approval: privacy and IP limits apply to judges too. `[C03-016]`
