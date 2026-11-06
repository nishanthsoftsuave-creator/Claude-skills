import csv
from pathlib import Path

from build_matrix import COLUMNS


def make_row(**kw):
    row = {
        "id": "C01-001", "chapter": "1", "section_path": "1. Intro > Planning",
        "start_page": "10", "end_page": "12", "tail_page": "",
        "role": "ACTIONABLE", "role_reason": "feeds a workflow",
        "destination_file": "core/ch01-intro/p010-planning.md",
        "status": "NOT_STARTED", "verification": "", "gaps": "",
    }
    row.update({k: str(v) for k, v in kw.items()})
    return row


def make_skill(tmp_path, rows, files=None):
    """Create a throwaway skill root with a matrix and optional files {relpath: text}."""
    root = Path(tmp_path) / "skill"
    (root / "coverage").mkdir(parents=True)
    with open(root / "coverage" / "coverage-matrix.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    for rel, text in (files or {}).items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return root


def module(row_id="C01-001", pages="10-12", body_words=200, extra=""):
    body = " ".join(f"word{i}" for i in range(body_words))
    return f'---\nid: {row_id}\nsource_pages: "{pages}"\n---\n# Title\n{body}\n{extra}\n'
