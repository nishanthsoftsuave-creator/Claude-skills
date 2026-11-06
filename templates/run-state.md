# Run state

`scripts/run_state.py` writes the real state to `<project>/.ai-architecture-and-reviewer/run-state.json` and a readable `run-state.md` beside it, after the user agrees to a state folder.

Steps, in order, each with a gate: classify, discover, intake, route, plan_approval, execute, verify, report, handoff.

- `RunState.advance(step, gate_met, note)` refuses out-of-order steps and unmet gates. `plan_approval` needs the user's approval words as the note.
- `RunState.enable_persistence()` flushes what was held in memory to disk. Before that, nothing is written to the user's project.
- `load(project)` resumes an interrupted run: `last_completed()` and `next_step()` say where to continue.

Run folder layout for Review & Test:

```
.ai-architecture-and-reviewer/
  run-state.json  run-state.md  context.md
  runs/<timestamp>/
    results.json        (see templates/results.example.json)
    evidence/           (exec records from run_check.py, outputs, notes)
    report.md
```
