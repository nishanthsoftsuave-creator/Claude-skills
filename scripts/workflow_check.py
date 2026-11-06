"""Workflow consistency checks (structure, not correctness of the guidance).

check(skill_root, expected=EXPECTED) -> list[str]
For every workflow under workflows/architect and workflows/review-test:
  - the file exists for each expected (mode, name);
  - front matter `name` equals the file name and `mode` equals the folder;
  - `rows` is non-empty and every id exists in the matrix;
  - every id in `rows` is cited in the body as [ID], and every [ID] cited is in `rows`.
It cannot prove that a citation is apt; independent workflow verification covers that.
"""
import re
import sys
from pathlib import Path

from _common import load_matrix, split_frontmatter

EXPECTED = [("architect", n) for n in (
    "intake", "use-case-and-requirements", "model-selection", "solution-pattern", "structured-outputs-and-sampling",
    "data-and-retrieval", "agents-and-tools", "finetune-decision", "finetune-plan", "inference-plan",
    "architecture-design", "eval-plan", "ops-cost-feedback", "design-review-gate")] + [("review-test", n) for n in (
    "system-understanding", "review-checklist", "test-plan", "run-checks", "prompt-review", "retrieval-review",
    "agent-review", "data-review", "observability-review", "feedback-review", "eval-execution",
    "security-and-prompt-attacks", "perf-cost-latency", "failure-diagnosis", "evidence-and-confidence", "report",
    "handoff-to-architect")]

FENCE_RE = re.compile(r"```.*?```", re.S)
CITE_RE = re.compile(r"\[([A-Z]\d{0,2}-\d{3})\]")


def _rows_list(meta):
    return [x.strip() for x in meta.get("rows", "").strip().strip("[]").split(",") if x.strip()]


def check(skill_root, expected=EXPECTED):
    root = Path(skill_root)
    ids = {r["id"] for r in load_matrix(root)}
    problems = []
    for mode, name in expected:
        if not (root / "workflows" / mode / f"{name}.md").exists():
            problems.append(f"workflows/{mode}/{name}.md is missing")
    for mode in ("architect", "review-test"):
        d = root / "workflows" / mode
        for f in sorted(d.glob("*.md")) if d.exists() else []:
            rel = f"{mode}/{f.name}"
            meta, body = split_frontmatter(f.read_text(encoding="utf-8"))
            if meta.get("name") != f.stem:
                problems.append(f"{rel}: front matter name is {meta.get('name')!r}, expected {f.stem!r}")
            if meta.get("mode") != mode:
                problems.append(f"{rel}: front matter mode is {meta.get('mode')!r}, expected {mode!r}")
            rows = _rows_list(meta)
            if not rows:
                problems.append(f"{rel}: rows list is empty")
            cited = set(CITE_RE.findall(FENCE_RE.sub("", body)))
            for r in rows:
                if r not in ids:
                    problems.append(f"{rel}: rows lists unknown id {r}")
                elif r not in cited:
                    problems.append(f"{rel}: {r} is in rows but not cited in the body as [{r}]")
            for c in sorted(cited - set(rows)):
                problems.append(f"{rel}: body cites [{c}] which is not in the rows list")
    return problems


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    problems = check(root)
    for p in problems:
        print(p)
    print(f"workflow_check: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
