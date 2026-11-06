"""Core purity: the universal core must not contain project paths, emails or secret shapes.

check(skill_root) -> list[str]. Patterns come from scripts/purity-patterns.txt.
evals/, tests/, coverage/ and scripts/ are not scanned.
"""
import re
import sys
from pathlib import Path

from _common import md_files


def load_patterns(root):
    p = Path(root) / "scripts" / "purity-patterns.txt"
    if not p.exists():
        p = Path(__file__).resolve().parent / "purity-patterns.txt"
    return [re.compile(line) for line in p.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")]


def check(skill_root, **_):
    root = Path(skill_root)
    pats = load_patterns(root)
    problems = []
    for f in md_files(root):
        text = f.read_text(encoding="utf-8")
        for pat in pats:
            m = pat.search(text)
            if m:
                problems.append(f"{f.relative_to(root)}: matches {pat.pattern!r} ({m.group(0)[:40]!r})")
    return problems


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    problems = check(root)
    for p in problems:
        print(p)
    print(f"core_purity_check: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
