"""Coverage-matrix integrity checks.

check(skill_root, stage="build"|"final", source_dir=None) -> list[str]  (empty = pass)
  build: structure (matrix columns, page tiling, statuses, modules, cites, size, overlap);
         NOT_STARTED rows are tolerated.
  final: additionally every row VERIFIED or an explained GAP, ACTIONABLE rows named by a
         workflow, KNOWLEDGE_ONLY rows linked from the book's index or cross-reference.
What it cannot prove: that an independent verifier really ran, or that a claim is right.
"""
import sys
from pathlib import Path

from _common import (CITE_RE, ROLES, STATUSES, core_dir, load_matrix, shingles, split_frontmatter, words)

MIN_WORDS_PER_PAGE = 40
MIN_WORDS = 80
MAX_VERBATIM_RATIO = 0.25


def _pages(row):
    return int(row["start_page"]), int(row["end_page"])


def _check_pages(rows, problems):
    owners = {}
    for r in rows:
        s, e = _pages(r)
        for p in range(s, e + 1):
            owners.setdefault(p, []).append(r)
    if not owners:
        return
    for p in range(min(owners), max(owners) + 1):
        if p not in owners:
            problems.append(f"page {p} is not covered by any row")
    for p, rs in owners.items():
        if len(rs) > 1 and len({int(r["start_page"]) for r in rs}) > 1:
            problems.append(f"overlap on page {p}: rows {', '.join(r['id'] for r in rs)} do not share a start page")


def _check_related(rid, meta, all_ids, problems):
    raw = meta.get("related", "").strip().strip("[]")
    for ref in [x.strip() for x in raw.split(",") if x.strip()]:
        if ref == rid:
            problems.append(f"{rid}: related lists the module itself")
        elif ref not in all_ids:
            problems.append(f"{rid}: related id {ref} is not in the matrix")


def _check_module(root, r, problems, source_dir, all_ids):
    rid = r["id"]
    path = Path(root) / r["destination_file"]
    if not path.exists():
        problems.append(f"{rid}: module {r['destination_file']} does not exist but status is {r['status']}")
        return
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    s, e = _pages(r)
    if meta.get("id") != rid:
        problems.append(f"{rid}: frontmatter id is {meta.get('id')!r}")
    _check_related(rid, meta, all_ids, problems)
    expected = f"{s}" if s == e else f"{s}-{e}"
    if meta.get("source_pages") != expected:
        problems.append(f"{rid}: source_pages is {meta.get('source_pages')!r}, matrix says {expected!r}")
    hi = e + 1 if r.get("tail_page") else e
    for m in CITE_RE.finditer(body):
        a = int(m.group(1))
        b = int(m.group(2)) if m.group(2) else a
        if a < s or b > hi:
            problems.append(f"{rid}: citation {m.group(0).strip()} outside source range {s}-{hi}")
    n_words = len(words(body))
    floor = max(MIN_WORDS, MIN_WORDS_PER_PAGE * (e - s + 1))
    if n_words < floor:
        problems.append(f"{rid}: module too short ({n_words} words, floor {floor})")
    if source_dir:
        src = Path(source_dir) / f"{rid}.txt"
        if src.exists():
            mod_sh = shingles(words(body))
            if mod_sh:
                ratio = len(mod_sh & shingles(words(src.read_text(encoding="utf-8")))) / len(mod_sh)
                if ratio > MAX_VERBATIM_RATIO:
                    problems.append(f"{rid}: {ratio:.0%} of module text is verbatim from the source "
                                    f"(max {MAX_VERBATIM_RATIO:.0%})")


def check(skill_root, stage="build", source_dir=None):
    root = Path(skill_root)
    rows = load_matrix(root)
    problems = []
    all_ids = {r["id"] for r in rows}
    _check_pages(rows, problems)
    wf = root / "workflows"
    workflows_text = "\n".join(p.read_text(encoding="utf-8") for p in wf.rglob("*.md")) if wf.exists() else ""
    core = core_dir(root)
    link_text = "\n".join(p.read_text(encoding="utf-8")
                          for p in (core / n for n in ("index.md", "xref.md")) if p.exists())
    for r in rows:
        rid = r["id"]
        if r["status"] not in STATUSES:
            problems.append(f"{rid}: invalid status {r['status']!r}")
        if r["role"] not in ROLES:
            problems.append(f"{rid}: invalid role {r['role']!r}")
        if not r["role_reason"].strip():
            problems.append(f"{rid}: role_reason is empty")
        if not r["destination_file"].strip():
            problems.append(f"{rid}: destination_file is empty")
            continue
        non_sub = r["role"] == "NON_SUBSTANTIVE"
        if r["status"] in ("IMPLEMENTED", "VERIFIED") and not non_sub:
            _check_module(root, r, problems, source_dir, all_ids)
        if r["status"] == "VERIFIED" and not r["verification"].strip():
            problems.append(f"{rid}: VERIFIED but the verification note is empty")
        if r["status"] == "GAP" and not r["gaps"].strip():
            problems.append(f"{rid}: GAP but the gaps text is empty")
        if stage == "final":
            if r["status"] not in ("VERIFIED", "GAP"):
                problems.append(f"{rid}: status is {r['status']} at final stage")
            if r["role"] == "ACTIONABLE" and rid not in workflows_text:
                problems.append(f"{rid}: ACTIONABLE row is not named by any workflow")
            if r["role"] == "KNOWLEDGE_ONLY":
                rel = r["destination_file"].removeprefix("core/")
                if rid not in link_text and rel not in link_text:
                    core_rel = core.relative_to(root).as_posix()
                    problems.append(f"{rid}: KNOWLEDGE_ONLY row is not linked from {core_rel}/index.md or {core_rel}/xref.md")
    return problems


def main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--final", action="store_true", help="final-stage checks")
    ap.add_argument("--source-dir", default=None, help="dir of extracted <row-id>.txt files for the verbatim check")
    a = ap.parse_args(argv)
    stage = "final" if a.final else "build"
    problems = check(a.root, stage=stage, source_dir=a.source_dir)
    for p in problems:
        print(p)
    print(f"coverage_check ({stage}): {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
