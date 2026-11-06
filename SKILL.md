---
name: ai-architecture-and-reviewer
description: Design the architecture of a new AI/LLM application, or review and test an existing one, grounded in a source-cited knowledge base (foundation models, evaluation, prompt engineering, RAG, agents, finetuning, dataset engineering, inference optimization, AI system architecture and user feedback). Use this whenever the user wants to architect, design, plan, review, audit, evaluate, test, debug or cost-estimate anything built on foundation models or LLMs, such as chatbots, RAG pipelines, agents, copilots, prompt or model selection, "why does my AI feature hallucinate or cost too much", eval sets, guardrails, prompt-injection testing, or whether to prompt, use RAG or finetune, even if the user never says "architecture" or "review". Works on any project, language or stack; it inspects the project first and asks only for what it still needs. Do not use for plain non-AI software work.
---

# AI Architecture and Reviewer

Two modes, one knowledge base. The knowledge base is a complete book on AI engineering, kept as source-cited modules under `core/` (one per book section, each opening with its PDF page range). Read only the modules a task needs; the rest stays available.

- **Architect mode**: design a new AI project or feature. Output: an architecture design, a decision record per choice (options, criteria, trade-offs, why, book citations) and an evaluation plan.
- **Review & Test mode**: inspect an existing AI project, run the checks the environment permits, and report findings with evidence, separating confirmed defects, probable issues, risks, recommendations and unverified items.
- A plain question about the book needs neither mode: look the term up (see below), answer from the module, and cite it.

Paths below are relative to this skill's folder (the base directory shown when the skill loads). Call scripts by absolute path from wherever you are, for example `python <skill folder>/scripts/validate_report.py <run dir>`; project commands run from the project through `run_check.py --cwd <project>` (see step 6).

## Why it is built this way

The book's central lesson is that AI applications fail quietly: outputs look plausible while being wrong, and without evaluation nobody notices. So this skill is strict about evidence and honest about its limits. A claim is only as strong as what backs it, and the report says so. Do not weaken that to make a report look more complete.

## The flow (every invocation)

State is held in the conversation until the user approves a plan. After that, `scripts/run_state.py` saves it in `<project>/.ai-architecture-and-reviewer/` (ask before creating that folder). Do not skip a step or move on before its gate is met.

1. **Classify.** Decide Architect, Review & Test, or plain question. Ask once if ambiguous. Gate: the mode is clear.
2. **Discover first.** Follow `workflows/discovery.md`: inspect what exists in the project and nothing more; record facts, assumptions and unknowns; show a one-screen summary the user can correct.
3. **Intake: ask only what is missing.** Follow `workflows/architect/intake.md`. Use AskUserQuestion, at most four questions per round, each with a recommended default; never ask what discovery already answered. In a non-interactive session, proceed on stated assumptions and list them at the top of the output.
4. **Route.** Follow `workflows/routing.md` to choose the workflows; each workflow's "Modules to load" table names the `core/` modules. Keep the list of modules used; the output cites them.
5. **Plan and get approval.** Architect: the decisions to make, in order. Review & Test: a test plan (`templates/test-plan.md`) stating what is checked, how, with what evidence, and what cannot be run. Execution, edits and any paid model call wait for approval, and a paid call also needs a stated spend cap, in both modes. Record their approval words with `RunState.advance("plan_approval", True, note=<their words>, plan=<the plan text shown>)`. Keep run-folder names short (timestamp only), because long Windows paths break tools. A plain question or advice-only answer that runs nothing and edits nothing needs no approval gate. Before citing a module's page range, open the module itself rather than relying on a workflow's summary.
6. **Execute.**
   - Architect: run the `workflows/architect/` workflows in order; write a decision record per choice (`templates/decision-record.md`).
   - Review & Test: seed `<run>/results.json` from the approved plan with every case `NOT_RUN` and a reason, then run the `workflows/review-test/` workflows. Run every command through `python <skill folder>/scripts/run_check.py --case <ID> --evidence-dir <run>/evidence --cwd <project> -- <command>` (no shell: no pipes or `&&`; the exit code is recorded, not returned). Reading code or configuration is `REVIEWED`, never `PASSED`. A tool or access problem is `BLOCKED`.
7. **Verify.** Re-run each failure once and record the re-run. Downgrade weak evidence. A finding that rests only on an AI judge stays `probable`. Then follow `workflows/review-test/report.md` to validate: `validate_report.py` must print 0 problems before the report is written. Fix the data, never the validator.
8. **Report.** `templates/findings-report.md` (Review & Test) or `templates/architecture-design.md` with `templates/eval-plan.md` (Architect). As short as the task allows. State what was not tested and why.
9. **Handoff.** Offer, never perform, anything outward-facing (tickets, messages, pushing changes). Update the project layer (`<project>/.ai-architecture-and-reviewer/context.md`, from `templates/layer-b-seed.md`) only with approval. Never write project details into this skill's folder.

## Labelling what you say

| Label | Meaning |
|---|---|
| `BOOK` | Stated in the book. Cite the row id and `PDF p. N` from the module. |
| `INTERPRETATION` | Your operational adaptation of a book idea, including your own caps, thresholds and probe designs. |
| `SUPPLEMENTARY` | From outside the book. Name the source. |
| `UNVERIFIED` | Could not be confirmed. Say what would confirm it. |
| Project decision | From this project's facts. Lives in the project layer only. |

The book gives few thresholds. Where a check needs one, the user sets it (or an earlier baseline does), it is recorded as the user's or the baseline's, and it is never presented as the book's. Treat the book's model names, benchmark scores, prices and tool names as dated examples; flag them as time-sensitive. Modules mark their own time-sensitive statements and `UNVERIFIED:` spots (a table or figure clipped in the PDF itself, a printed slip); `coverage/known-gaps.md` lists them.

## Test statuses and finding labels

Case statuses: `PASSED`, `FAILED`, `BLOCKED`, `SKIPPED`, `NOT_RUN`, `REVIEWED`. Findings: `confirmed` (reproduced on re-run, deterministic or static or manual basis, with evidence, repro steps and impact), `probable`, `risk`, `recommendation`, `unverified`. Severity: critical, major, minor, trivial (the skill's own scale, not the book's). Never report `PASSED` for something that was not run.

## Safety rules

- Production is read-only. No destructive actions. Nothing external is written, sent or posted without confirmation.
- Probes (prompt attacks, failure injection) run only against the user's own non-production system, with approval, using synthetic data and benign stand-ins.
- Never copy secrets or personal data into reports, evidence or the project layer. `run_check.py` redacts common secret shapes only, not personal data, so scripts that read logs or user exports must print aggregates and counts, never raw user text.
- Inspect the code before changing it, follow the project's conventions, and run its tests after a change.

## When the evidence is thin

Say so. List the unknowns, ask the targeted question that would settle them, and give the next step. Do not assert a root cause or a pass you cannot support. If a project has no AI components, say little of the book applies and why, instead of forcing RAG or finetuning advice onto it.

## Finding things

- `workflows/routing.md`: request to workflows. Start here after discovery.
- `core/ai-engineering-building-applications-with-foundation-models/index.md` (by chapter), `core/ai-engineering-building-applications-with-foundation-models/concepts.md` (by concept), `core/ai-engineering-building-applications-with-foundation-models/xref.md` (how modules relate), `core/ai-engineering-building-applications-with-foundation-models/front-back-matter/p932-index.md` (the book's own Index mapped to modules). These four are generated; do not edit them.
- `workflows/architect/` and `workflows/review-test/`: the procedures. `templates/`: intake questions, run state, architecture design, decision record, test plan, eval plan, findings report, project-layer seed.
- `coverage/`: `coverage-matrix.csv` (every book section, its module, status and recorded gaps), `known-gaps.md`, `module-spec.md`, `workflow-spec.md`, and the audit.
- `scripts/`: `run_state.py`, `run_check.py`, `validate_report.py` (runtime) and the maintenance checks listed in `MAINTENANCE.md`.
