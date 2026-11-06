"""Run every integrity check of the skill and report one result.

Usage: python run_all_checks.py [--final] [--source-dir DIR] [--tests]
  --final       final-stage coverage rules (every row VERIFIED or an explained GAP, workflow and index links)
  --source-dir  extracted source text per row, enables the verbatim-copy check
  --tests       also run the pytest suite
Exit code 0 only when every check reports no problems.
"""
import subprocess
import sys
from pathlib import Path

import build_index
import core_purity_check
import coverage_check
import link_check
import workflow_check
from _common import core_dir

GENERATED = ("index.md", "concepts.md", "xref.md")


def index_up_to_date(root):
    """The generated index files must equal what build_index would produce now."""
    import shutil
    import tempfile
    root = Path(root)
    problems = []
    actual_core = core_dir(root)
    relative_core = actual_core.relative_to(root)
    with tempfile.TemporaryDirectory() as tmp:
        shadow = Path(tmp) / "skill"
        shadow.mkdir()
        shutil.copytree(root / "coverage", shadow / "coverage")
        shutil.copytree(root / "core", shadow / "core")
        for name in GENERATED:
            (shadow / relative_core / name).unlink(missing_ok=True)
        build_index.build(shadow)
        for name in GENERATED:
            have = actual_core / name
            if not have.exists():
                problems.append(f"{relative_core.as_posix()}/{name} is missing; run scripts/build_index.py")
            elif have.read_text(encoding="utf-8") != (shadow / relative_core / name).read_text(encoding="utf-8"):
                problems.append(f"{relative_core.as_posix()}/{name} is out of date; run scripts/build_index.py")
    return problems


def run_all(root, stage="build", source_dir=None, workflows=True):
    results = {
        "coverage_check": coverage_check.check(root, stage=stage, source_dir=source_dir),
        "link_check": link_check.check(root),
        "core_purity_check": core_purity_check.check(root),
        "index_up_to_date": index_up_to_date(root),
    }
    if workflows:
        results["workflow_check"] = workflow_check.check(root)
    return results


def main(argv):
    root = Path(__file__).resolve().parent.parent
    stage = "final" if "--final" in argv else "build"
    src = argv[argv.index("--source-dir") + 1] if "--source-dir" in argv else None
    results = run_all(root, stage=stage, source_dir=src)
    failed = False
    for name, problems in results.items():
        print(f"{name}: {'OK' if not problems else str(len(problems)) + ' problem(s)'}")
        for p in problems:
            print("   ", p)
        failed = failed or bool(problems)
    if "--tests" in argv:
        code = subprocess.call([sys.executable, "-I", "-m", "pytest", str(root / "tests"), "-q"])
        print(f"pytest: {'OK' if code == 0 else 'FAILED'}")
        failed = failed or code != 0
    print("run_all_checks:", "FAILED" if failed else "all checks passed", f"({stage} stage)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
