"""Markdown link checker: every relative link in the skill's .md files must resolve.

check(skill_root) -> list[str]
"""
import re
import sys
from pathlib import Path

from _common import md_files

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


def check(skill_root, **_):
    root = Path(skill_root)
    problems = []
    for f in md_files(root, include=("core", "workflows", "templates", "coverage")):
        text = FENCE_RE.sub("", f.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text):
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#", 1)[0]
            if path and not (f.parent / path).resolve().exists():
                problems.append(f"{f.relative_to(root)}: broken link to {target}")
    return problems


def main(argv):
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    problems = check(root)
    for p in problems:
        print(p)
    print(f"link_check: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
