---
name: feedback-review
mode: review-test
rows: [C10-011, C10-012, C10-013]
---
# Feedback review (signals, design, biases, loops, consent)

## When to use
Use when the task is to review how an AI application collects user feedback, extracts signals from conversations and actions, and uses them for evaluation, development or personalisation. Also use when feedback is already feeding finetuning, ranking or prompt changes and the team wants to know whether it can be trusted. Production data is read-only; work from exports, schemas and code, and never copy user content into evidence beyond what the check needs. Analysis scripts print aggregates only (counts, tables), not raw messages, because `run_check.py` redacts only common key shapes, not personal data.

## Inputs needed
From discovery (`../discovery.md`): the feedback UI elements (thumbs, stars, side-by-side, edit, regenerate), event schemas and analytics code, where feedback is stored, whether it feeds training, ranking or prompts, and the consent or privacy text. Ask only for what is missing (`../architect/intake.md`): an anonymised export of feedback events with timestamps, positions and ratings; which feedback uses the team intends (evaluation, development, personalisation); and the product type (standalone chat, integrated tool, creative generator), because the meaning of most signals depends on it.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C10-011 | [Extracting Conversational Feedback](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p895-extracting-conversational-feedback.md) | catalogue of explicit and implicit signals and their ambiguity |
| C10-012 | [Feedback Design](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p907-feedback-design.md) | when and how feedback should be collected, consent, clarity, visibility |
| C10-013 | [Feedback Limitations](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p921-feedback-limitations.md) | biases, degenerate loops, sycophancy |

## Procedure
1. **State the intended uses.** The book names three: evaluation (monitoring metrics), development (training or steering future models), personalisation. Each use has a different tolerance for noise; training on feedback is the highest-risk use because of step 8. `[C10-011]`
2. **Inventory the signals the product can emit.** Explicit (thumbs, stars, yes/no) and implicit (actions and message content). For each signal record whether it is collected, stored with enough context to interpret it, and used. `[C10-011]`
3. **Check the natural language signals** against the product's logs: early termination (stopped generation, exit, unanswered prompt); error correction (a follow-up beginning "No" or "I meant", rephrasing, pointing out what should have been done, action nudges to agents; "Are you sure?" or "Show me the sources" requests are weaker, since the book says they may mean missing detail or general distrust rather than a wrong answer); edits (a user edit of generated output is a strong signal and each edit yields one preference pair, original as loser, edited as winner); complaints and sentiment; refusal rate. Decision rule: a signal that is observable but not extracted is a `recommendation`; a signal used as a quality metric without validation is a `risk`. `[C10-011]`
4. **Check the action signals** and their ambiguity: regeneration (dissatisfaction or option comparison; stronger evidence under usage-based billing than subscription), delete (a strong negative unless the user wants no trace), rename (the chat may be good and only the generated title bad), share, bookmark, conversation length and dialogue diversity. Length can be good for a companion product and bad for support; a long conversation that repeats lines suggests a user stuck in a loop. Rule: any signal with both positive and negative readings must be treated as a hypothesis to test with data analysis or user studies, not as a metric. `[C10-011]`
5. **Check explicit versus implicit balance.** Explicit feedback is easier to read but sparse and subject to response bias (unhappy users complain more, so it looks worse than reality); implicit feedback is abundant but noisy. A feedback programme that relies on one kind only is a `risk`. `[C10-011]`
6. **Review feedback design: collection moments.** Is there a way to report errors at the moment of failure that does not disrupt the workflow; calibration at the start that is optional unless the product needs it (with a neutral default); help when the model is unsure (side-by-side or partial drafts, "not sure" option); a way to finish the task with human help when the AI fails; and a deliberate decision on positive feedback (the book gives two opposing views, so judge the team's choice by whether it is reasoned, not by which side it took; limiting the ask to a small share of users is the book's remedy for annoyance, at the price of more feedback bias). `[C10-012]`
7. **Review feedback design: mechanism quality.** The feedback should blend into the workflow, need no extra work, and be easy to ignore, with some incentive for users to give good feedback. Test each UI for: ambiguity (unclear icons, reversed scales; the book's example is a rating form whose emoji order was reversed), impossible asks (comparisons between answers the user cannot judge, with no "I don't know"), and whether integrated products capture outcome (accepted, edited, sent) where standalone ones cannot. `[C10-012]`
8. **Review consent and privacy.** Deeper analysis needs context (for example the previous 5 to 10 turns), which may hold personal data. Look for a service agreement covering analytics and improvement, or a donation flow that ties feedback to sharing recent data. Check that users are told what feedback is used for (personalisation, statistics, model training), and that any promise not to train on data or to keep it on device is true. If consent cannot be found in code or text, mark `unverified` and name the legal or privacy owner to confirm; do not assert a legal conclusion. Also decide whether feedback visibility (private or public) was a deliberate choice. `[C10-012]`
9. **Test the data for the book's biases.** Using the export:
   - leniency: plot the rating distribution; a pile-up at the top rating is the symptom (the book gives Uber's 2015 average of 4.8 as an example and no threshold); remedies are verbal options instead of low numbers and collection that needs no extra work;
   - randomness: the book describes users clicking without reading both responses; INTERPRETATION: look for votes made faster than a response could be read, with the reading-time cutoff chosen and stated by you, not taken from the book;
   - position bias: compare click rate by position; this only separates bias from real quality if display order was randomised or a position-corrected rate exists, otherwise report it as confounded; mitigations are randomised order or a position-corrected success rate;
   - preference bias: check whether longer responses win more often in side-by-side votes, and whether the last-seen answer wins more (recency).
   `[C10-013]`
10. **Test for degenerate feedback loops.** Feedback exists only for what was shown. If feedback drives ranking, recommendations or retraining, check whether exposure decides the next round (popular items stay popular; a minority preference grows until it dominates) and whether the product's mix of outputs or users has drifted toward one theme. Mitigation under INTERPRETATION: monitor what the system shows, not only what users click. `[C10-013]`
11. **Test for sycophancy risk.** If feedback is used to finetune or to rank answers, check whether agreement with the user's stated view is rewarded and whether accuracy is evaluated independently of satisfaction. Training on feedback can teach a model to say what users want to hear. `[C10-013]`
12. **Verdict per use.** For each intended use from step 1, say whether the feedback is trustworthy enough, with the evidence and the biases found. Anything resting on an AI judge's reading of the feedback is capped at `probable` (limits in the evaluation workflow, `eval-execution.md`).

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| FB-01 | Intended uses of feedback are stated | ask user; read docs | notes | review | C10-011 | uses undefined, or training use with no safeguards |
| FB-02 | Explicit and implicit signal inventory | read UI code, event schema, analytics config | signal table: collected, stored with context, used | review | C10-011 | key signal observable but dropped, or stored without conversation context |
| FB-03 | Natural language signals extracted (termination, correction, edit, complaint, sentiment, refusal) | read extraction code and sample logs | notes | review | C10-011 | none extracted when the product is conversational |
| FB-04 | Ambiguous signals validated before use as metrics | read how regeneration, length, sharing and deletion are interpreted | notes | review | C10-011 | single reading assumed with no analysis or user study |
| FB-05 | Collection moments covered (start, failure, low confidence, optional positive) | walk the UI or read the flows | notes with screenshots only if the user provides them | review | C10-012 | no way to report a failure in flow, or intrusive mandatory prompts |
| FB-06 | Feedback UI ambiguity and impossible asks | read UI copy, icons, scales; check comparison prompts have an "unsure" option | notes | review | C10-012 | reversed or unclear scale, forced choice on unjudgeable content |
| FB-07 | Consent, disclosure of use, visibility choice | read agreements, consent code, feedback form text | notes; mark `unverified` where only legal can decide | review | C10-012 | context captured without any consent path, or a privacy claim contradicted by the code |
| FB-08 | Leniency: rating distribution | compute the distribution from the export with a throwaway script run via `python scripts/run_check.py --case FB-08 --evidence-dir <run>/evidence -- python <script> <export>` | exec record, histogram | run | C10-013 | extreme concentration at one end that is not explained; the book gives no threshold, so report the figure and judge against the team's expectation or an earlier baseline, and say so |
| FB-09 | Position bias | same method, click rate by displayed position | exec record, table | run | C10-013 | first position wins well above what randomised order would give, with no correction applied |
| FB-10 | Length and recency bias in side-by-side votes | same method, win rate against length difference and display order | exec record, table | run | C10-013 | longer or last-seen response wins systematically |
| FB-11 | Random or too-fast feedback | same method, time between display and vote | exec record | run (INTERPRETATION: the reading-time cutoff is yours, state it) | C10-013 | large share of votes faster than the stated cutoff; noisy signal flagged, no book threshold |
| FB-12 | Degenerate loop exposure | read ranking or retraining code for dependence on past clicks; compare output-mix trend over time if data is available | notes, optional exec record | review (run if trend data supplied) | C10-013 | feedback shapes exposure or training with no monitoring of the output mix |
| FB-13 | Sycophancy guard | read how feedback enters finetuning or ranking; is accuracy evaluated separately | notes | review | C10-013 | satisfaction is the only optimisation target |

## Evidence and exit gate
- A check typed `review (run if ...)` is `REVIEWED` unless an exec record exists for its run part.
- Run checks (FB-08 to FB-11) need an exec record and data from the user's own export. Without an export they are `BLOCKED` with the reason, and the corresponding bias is an `unverified` item, not a pass.
- Review checks end `REVIEWED`. Findings from them are `risk`, `recommendation` or `probable`. A `confirmed` finding needs a failing run record plus repro steps that another reader can repeat on the same export.
- Exit when every intended use has a verdict and every check has a status and, if not run, a reason.
- Run `python scripts/validate_report.py <run_dir>` before the report.

## Outputs
`results.json` cases and findings, then [../../templates/findings-report.md](../../templates/findings-report.md). Put the per-use verdict table in Summary. Redesign work (new collection points, bias corrections) is offered as a handoff to Architect mode, not performed.

## Pitfalls
- Reading regeneration, length, deletion or sharing as one-directional `[C10-011]`.
- Ignoring that explicit feedback comes mostly from unhappy users `[C10-011]`.
- Ratings collected with extra friction, which inflates positives `[C10-013]`.
- Feedback prompts nobody can judge, producing random clicks `[C10-012]`, `[C10-013]`.
- Capturing context without consent or promising privacy the code does not deliver `[C10-012]`.
- Treating clicks on the first-shown option as quality `[C10-013]`.
- Retraining on feedback with no control for exposure, which amplifies the initial bias and can reward flattery `[C10-013]`.
- Quoting Table 10-1 percentages: only their integer parts are legible in the book, so rely on the counts and groups, not decimals `[C10-011]`.
