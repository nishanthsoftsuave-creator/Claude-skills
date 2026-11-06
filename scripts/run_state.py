"""Run state for one invocation of the skill: ordered steps, gates, answers, assumptions.

State lives in memory until enable_persistence() is called (done only after the user agrees
to a state folder, normally at plan approval); then it is written to
<project>/.ai-architecture-and-reviewer/run-state.json (+ a readable run-state.md).
"""
import json
from datetime import datetime
from pathlib import Path

STEPS = ["classify", "discover", "intake", "route", "plan_approval",
         "execute", "verify", "report", "handoff"]
STATE_DIR = ".ai-architecture-and-reviewer"


class GateError(Exception):
    pass


class RunState:
    def __init__(self, project):
        self.project = Path(project)
        self.completed = []  # [{"step", "note", "at"}]
        self.answers = {}
        self.assumptions = []
        self.persist = False

    @property
    def dir(self):
        return self.project / STATE_DIR

    def last_completed(self):
        return self.completed[-1]["step"] if self.completed else None

    def next_step(self):
        return STEPS[len(self.completed)] if len(self.completed) < len(STEPS) else None

    def advance(self, step, gate_met, note="", plan=""):
        expected = self.next_step()
        if expected is None:
            raise GateError("all steps are already complete")
        if step != expected:
            raise GateError(f"expected {expected!r} next, got {step!r}")
        if not gate_met:
            raise GateError(f"gate for {step!r} is not met")
        if step == "plan_approval" and not note.strip():
            raise GateError("plan_approval needs the user's approval text as the note")
        entry = {"step": step, "note": note, "at": datetime.now().isoformat(timespec="seconds")}
        if plan:
            entry["plan"] = plan  # the approved plan text, so a resumed run knows what was approved
        self.completed.append(entry)
        self.save()

    def set_answer(self, key, value):
        self.answers[key] = value
        self.save()

    def add_assumption(self, text):
        self.assumptions.append(text)
        self.save()

    def enable_persistence(self):
        self.persist = True
        self.save()

    def save(self):
        if not self.persist:
            return
        self.dir.mkdir(parents=True, exist_ok=True)
        data = {"completed": self.completed, "answers": self.answers, "assumptions": self.assumptions}
        (self.dir / "run-state.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
        lines = ["# Run state", "", f"Next step: {self.next_step() or 'done'}", "", "## Completed"]
        lines += [f"- {c['step']} ({c['at']}): {c['note']}" for c in self.completed] or ["- none"]
        lines += ["", "## Answers"] + [f"- {k}: {v}" for k, v in self.answers.items()]
        lines += ["", "## Assumptions"] + [f"- {a}" for a in self.assumptions]
        (self.dir / "run-state.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def load(project):
    rs = RunState(project)
    f = rs.dir / "run-state.json"
    if f.exists():
        data = json.loads(f.read_text(encoding="utf-8"))
        rs.completed = data.get("completed", [])
        rs.answers = data.get("answers", {})
        rs.assumptions = data.get("assumptions", [])
        rs.persist = True
    return rs
