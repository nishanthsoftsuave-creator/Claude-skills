# Claude web security skills

A Claude Code skill that **designs** new AI/LLM applications and **reviews and tests** existing ones. It checks your project first, asks only what it still needs, and reports only what it can prove.

Repository: [Claude-skills](https://github.com/nishanthsoftsuave-creator/Claude-skills).

## Quick install

Skills live in your `.claude/skills/` folder. Clone this repo there:

**macOS / Linux**
```bash
git clone https://github.com/nishanthsoftsuave-creator/Claude-skills.git ~/.claude/skills/ai-architecture-and-reviewer
```

**Windows (PowerShell)**
```powershell
git clone https://github.com/nishanthsoftsuave-creator/Claude-skills.git "$env:USERPROFILE\.claude\skills\ai-architecture-and-reviewer"
```

No Git? Download the ZIP from GitHub, unzip it, and move the folder to the same place. Avoid a folder inside a folder.

Then:
1. Check that this file exists: `~/.claude/skills/ai-architecture-and-reviewer/SKILL.md` (Windows: `%USERPROFILE%\.claude\skills\...`).
2. Start a **new** Claude Code session (skills load at startup).
3. Type `/` and look for `ai-architecture-and-reviewer`.

**Requirements:** Claude Code, and Python 3.10+ (standard library only).

## Usage

Just ask in plain words, or name the skill ("Use ai-architecture-and-reviewer to review this project").

| Mode | Example | You get |
|---|---|---|
| Architect | "Design a support chatbot over our docs." / "RAG or finetune?" | Architecture design, decision records, evaluation plan |
| Review & Test | "Review my agent." / "Why does it hallucinate?" / "Test for prompt injection." | Test plan you approve, checks with evidence, findings report |
| Question | "What is perplexity?" | A short answer from the knowledge base, with references |

## How it works

classify, inspect your project, ask a few questions, plan, **wait for your approval**, run, verify, report.

- Nothing runs, changes or costs money before you approve the plan. Paid model calls need a spend cap.
- Production is read-only. Nothing is sent or posted without your confirmation.
- Findings are labelled `confirmed`, `probable`, `risk`, `recommendation` or `unverified`. A check is `PASSED` only if a command was actually run.
- It saves run state and reports in `<your project>/.ai-architecture-and-reviewer/`, only if you agree.

## Update / uninstall

- Update: `git pull` inside the skill folder, then start a new session.
- Uninstall: delete the `ai-architecture-and-reviewer` folder.

## Folder guide

| Path | Purpose |
|---|---|
| `SKILL.md` | Entry point: modes, flow, safety rules |
| `core/<book>/` | Knowledge base modules grouped by book |
| `workflows/`, `templates/` | Procedures and report formats |
| `scripts/` | Runtime helpers (plus maintenance checks) |
| `coverage/` | Coverage matrix, audit, known gaps |
| `tests/`, `evals/` | Tests and scenarios for the skill itself |

Maintainers: `pip install pypdf pymupdf pytest`, then `python scripts/run_all_checks.py --final --tests`. See `MAINTENANCE.md`.

## Limitations

- It can only test what your environment allows; the rest is reported as `NOT_RUN` or `BLOCKED`.
- Reading code counts as "reviewed", not "passed".
- Model names, prices and benchmarks in the knowledge base are dated. Check current figures.
- A few clipped tables and figures in the source are marked `UNVERIFIED` (see `coverage/known-gaps.md`).
