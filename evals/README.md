# Evals for the skill itself

These test whether the skill behaves as designed: routes correctly, follows the flow and its gates, finds what is there, and refuses to claim what it cannot evidence. They are not tests of the book's content (that is what the coverage matrix and the independent verification are for).

## Layout

- `<case-name>/`: one folder per test in the format of skill-creator and `claude plugin eval`: `prompt.md` (what the user types), `case.yaml` (the expected outcome), `graders/NN-*.md` (one verifiable statement each), and `place-files.sh` plus `files/` where a case needs a project copied in.
- `fixtures/`: small unrelated sample projects with deliberate weaknesses. They are tests inputs, not part of the skill's behaviour. Never run them against real services; the "model" in them is a stub.
  - `rag-chatbot/` (Python): prompt built by concatenating user text into the instructions, fixed 200-character chunks with no overlap, top-k of 50, no output limit and a ten-attempt retry loop, temperature 1.0, no evaluation set, no logging, a hard-coded (fake) key, and a small messy ticket dataset with a duplicate, an empty record, mixed field names, an email address, a phone number and fabricated answers.
  - `node-agent/` (JavaScript): infinite loop with no stop condition, unvalidated tool calls, an ungated refund with no limit, unbounded memory, a stub model that retries the same failing call.
  - `crud-app/` (Python): no AI components at all.
  - `greenfield-brief/`: a brief for a project that does not exist yet.
- `trigger-queries.json`: should-trigger and should-not-trigger queries (including near misses) for tuning the `description` in `SKILL.md`.
- `reports/`: results of each run: per-case pass rates against the graders, behaviour notes, failures found and the corrections made.

## The cases

| Group | Cases |
|---|---|
| Architect | greenfield HR assistant; RAG or finetune for tone; model build vs buy; evaluation plan before building; finetune memory feasibility; agent design with refunds; structured-output failures; inference cost and latency; design review gate on a draft |
| Review & Test | full review of the RAG chatbot; prompts only; agent review; prompt-injection test (stops at the approval gate); data quality of the tickets; observability gap; cost measurement with no endpoint; a judge-only finding |
| Flow and negative | no AI components in the project; plain question about perplexity; paid calls without a cap; production target requested; "fix everything" (plan approval gate); resuming an interrupted run; non-interactive run states its assumptions; secrets in code are reported without being copied; diagnosing a hallucination with no evidence |

## How to run

With Claude Code v2.1.269 or later, from the skill folder: `claude plugin eval . --allow-tools Write,Edit,Bash` (add `--scaffold` for cases with input files). These are real, billed model runs.

Without the CLI: for each case, copy its fixture into a clean working folder, run a fresh agent with the skill on `prompt.md` (the user is not available: where the skill would ask a question or needs an approval the prompt does not grant, it must stop at that gate), and grade the final message, files and step log against `graders/`. Run a baseline without the skill on a subset to confirm the skill adds value.

After a change to `SKILL.md`, routing or a workflow, re-run the cases and compare with the previous report in `reports/` before accepting the change.
