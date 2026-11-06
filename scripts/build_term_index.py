"""Map the book's own Index (PDF pp. 932-988) to the matrix rows.

The Index lists terms with the *section headings* they point to (not page numbers), so each
heading can be resolved to matrix rows by title; headings below the outline depth are found as
standalone lines of the extracted section text.

Usage: python build_term_index.py <book.pdf> [--source-dir DIR] [--out PATH] [--keep-unmapped]
Writes the B-002 module and prints resolution statistics.
"""
import csv
import re
import sys
import warnings
from pathlib import Path

from _common import matrix_path

warnings.filterwarnings("ignore")

FIRST_PAGE, LAST_PAGE = 932, 988
MAIN_X = 95.0
MAX_ROWS_PER_TERM = 8  # a pointer to more sections than this is not useful; reported as unmapped
SKIP_ROWS = ("B-002",)  # the Index's own text must not resolve index terms
PAGE_MARK = re.compile(r"^=== PDF page (\d+)")


# ---- reading the Index -------------------------------------------------------------------------

def extract_index_lines(pdf, first=FIRST_PAGE, last=LAST_PAGE):
    import pymupdf
    doc = pymupdf.open(pdf)
    out = []
    for n in range(first, last + 1):
        for b in doc[n - 1].get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                text = "".join(s["text"] for s in ln["spans"]).strip()
                if text and not re.fullmatch(r"[A-Z]|Index", text):
                    out.append((round(ln["bbox"][0], 1), text))
    return out


def split_entry(text):
    """'term, Heading-Heading' -> (term, refs, see); '(see x)' entries give (term, '', x)."""
    m = re.match(r"^(.*?)\s*\(see(?: also)? ([^)]*)\)\s*$", text)
    if m:
        return m.group(1).strip(), "", m.group(2).strip()
    if ", " in text:
        term, refs = text.split(", ", 1)
        return term.strip(), refs.strip(), None
    return text.strip(), "", None


def _is_new_entry(x, text, prev):
    if prev is None:
        return True
    if ", " in text or "(see" in text:
        return True
    if prev["text"].endswith(("-", ",")):
        return False
    return x <= prev["x"] and x <= MAIN_X + 0.5


def group_lines(lines):
    """Join obviously wrapped lines into raw groups {text, x}. '(see also ...)' lines are dropped."""
    groups, prev = [], None
    for x, text in lines:
        if text.startswith("(see also"):
            continue
        if _is_new_entry(x, text, prev):
            prev = {"text": text, "x": x}
            groups.append(prev)
        else:
            prev["text"] += ("" if prev["text"].endswith("-") else " ") + text
    return groups


def assign_levels(groups):
    """Give each group an indentation level and the chain of parent terms."""
    entries, stack = [], {}
    for g in groups:
        level = max(0, round((g["x"] - MAIN_X) / 18))
        parents = [stack[i] for i in range(level) if i in stack]
        e = {"text": g["text"], "x": g["x"], "level": level, "parents": parents}
        entries.append(e)
        stack[level] = split_entry(g["text"])[0]
        for k in [k for k in stack if k > level]:
            del stack[k]
    return entries


def build_entries(lines, merge_fn=None):
    groups = group_lines(lines)
    if merge_fn:
        groups = merge_fn(groups)
    return assign_levels(groups)


# ---- resolving references ----------------------------------------------------------------------

def heading_map(rows):
    """Heading title (last path segment, or the chapter title) -> row ids."""
    hm = {}
    for r in rows:
        parts = r["section_path"].split(" > ")
        for title in {parts[-1], *([re.sub(r"^\d+\.\s+", "", parts[0])] if len(parts) > 1 else [])}:
            if title.startswith("("):
                continue
            hm.setdefault(title, [])
            if r["id"] not in hm[title]:
                hm[title].append(r["id"])
    return hm


def _norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'")).strip().lower()


def _split_candidates(refs):
    """All ways to read a reference string as one heading or a range 'A-B' of two headings."""
    refs = re.sub(r"\s+", " ", refs).strip()
    cands = [[refs]]
    for m in re.finditer(r"-", refs):
        a, b = refs[:m.start()].strip(), refs[m.end():].strip()
        if a and b:
            cands.append([a, b])
    return cands


def _range_rows(starts, ends, rows):
    """Closest ordered pair of start/end candidates (same chapter preferred), expanded in matrix order."""
    order = {r["id"]: i for i, r in enumerate(rows)}
    chapter = {r["id"]: r["chapter"] for r in rows}
    best = None
    for a in starts:
        for b in ends:
            if order[a] <= order[b]:
                key = (chapter[a] != chapter[b], order[b] - order[a])
                if best is None or key < best[0]:
                    best = (key, a, b)
    if best is None:
        return None
    _, a, b = best
    return [r["id"] for r in rows[order[a]:order[b] + 1]]


def resolve_refs(refs, hm, rows, line_index=None):
    """Resolve a reference string made of one heading or a range of two headings.

    Whole-segment matching only. Headings deeper than the outline come from `line_index`
    (normalised standalone source lines -> row ids). Returns (row_ids, ambiguous, unresolved_text).
    """
    if not refs:
        return [], False, ""
    lookup = {_norm(t): t for t in hm}
    for parts in _split_candidates(refs):
        ids_per_part, ok, amb = [], True, False
        for part in parts:
            n = _norm(part)
            if n in lookup:
                ids = hm[lookup[n]]
            elif line_index and n in line_index:
                ids = line_index[n]
            else:
                ok = False
                break
            amb = amb or len(ids) > 1
            ids_per_part.append(ids)
        if not ok:
            continue
        out = []
        if len(ids_per_part) == 2:
            ranged = _range_rows(ids_per_part[0], ids_per_part[1], rows)
            if ranged is not None:
                out, amb = ranged, False
        if not out:
            for ids in ids_per_part:
                out += [i for i in ids if i not in out]
        if len(out) > MAX_ROWS_PER_TERM:
            return [], False, refs  # too broad to be a useful pointer
        return out, amb, ""
    return [], False, refs


def resolve_multi(refs, hm, rows, line_index=None):
    """An entry may list several references separated by ', ' (headings may contain commas too)."""
    chunks = [c for c in re.split(r",\s+", refs) if c]
    n = len(chunks)
    memo = {}

    def parse(i):
        if i == n:
            return [], False
        if i in memo:
            return memo[i]
        best = None
        for j in range(n, i, -1):
            ids, amb, left = resolve_refs(", ".join(chunks[i:j]), hm, rows, line_index)
            if ids and not left:
                rest = parse(j)
                if rest is not None:
                    best = (ids + [x for x in rest[0] if x not in ids], amb or rest[1])
                    break
        memo[i] = best
        return best

    res = parse(0)
    if res is None:
        return resolve_refs(refs, hm, rows, line_index)
    return res[0], res[1], ""


def build_line_index(source_dir, rows):
    """Normalised standalone source lines (and two-line joins) -> row ids, from extracted row texts.

    Only lines on the row's own pages count: a tail page belongs to the next row.
    """
    idx = {}
    for r in rows:
        f = Path(source_dir) / f"{r['id']}.txt"
        if r["id"] in SKIP_ROWS or not f.exists():
            continue
        lo, hi = int(r["start_page"]), int(r["end_page"])
        page, lines = None, []
        for l in f.read_text(encoding="utf-8").splitlines():
            m = PAGE_MARK.match(l)
            if m:
                page = int(m.group(1))
            elif l.strip() and page is not None and lo <= page <= hi:
                lines.append(l.strip())
        for i, l in enumerate(lines):
            for cand in {l, (l + " " + lines[i + 1]) if i + 1 < len(lines) else l}:
                n = _norm(cand)
                if 3 <= len(n) <= 90:
                    idx.setdefault(n, [])
                    if r["id"] not in idx[n]:
                        idx[n].append(r["id"])
    return idx


def merge_wrapped(groups, hm, rows, line_index=None):
    """Join a group whose references do not resolve with the following group when the join does."""
    out, i = [], 0
    while i < len(groups):
        g = dict(groups[i])
        for _ in range(3):  # a wrapped entry can span a few lines
            _t, refs, see = split_entry(g["text"])
            if see or not refs or i + 1 >= len(groups):
                break
            ids, _a, left = resolve_multi(refs, hm, rows, line_index)
            if ids and not left:
                break
            joined = g["text"] + " " + groups[i + 1]["text"]
            m_ids, _a, m_left = resolve_multi(split_entry(joined)[1], hm, rows, line_index)
            if m_ids and not m_left:
                g["text"] = joined
                i += 1
            else:
                break
        out.append(g)
        i += 1
    return out


def term_rows(entries, hm, rows, line_index=None):
    """term (with parents joined) -> {'rows', 'ambiguous', 'unresolved', 'see', 'has_refs'}"""
    result, by_main = {}, {}
    for e in entries:
        term, refs, see = split_entry(e["text"])
        key = " > ".join(e["parents"] + [term])
        r, amb, left = resolve_multi(refs, hm, rows, line_index)
        result[key] = {"rows": r, "ambiguous": amb, "unresolved": left, "see": see, "has_refs": bool(refs)}
        if e["level"] == 0 and r:
            by_main[_norm(term)] = r
    for v in result.values():
        if v["see"] and not v["rows"]:
            v["rows"] = by_main.get(_norm(v["see"]), [])
    return result


def render(mapping):
    lines = []
    for term in sorted(mapping, key=lambda k: k.lower()):
        v = mapping[term]
        if v["rows"]:
            ids = ", ".join(v["rows"]) + (" (several candidates)" if v["ambiguous"] else "")
        elif not v["has_refs"] and not v["see"]:
            ids = "(heading only; see sub-entries)"
        else:
            ids = "unmapped"
        lines.append(f"| {term} | {ids} |")
    return lines


HEADER_TEXT = (
    "The book ends with an alphabetical index. Each index entry names a term and the section headings it points to "
    "(the book's Index lists headings, not page numbers) (PDF p. 932). This module keeps that structure as a lookup: "
    "for each term it gives the matrix row ids of the modules that cover the headings the entry points to. "
    "Sub-entries are shown as `parent > child`. A reference to a range of headings (`A-B`) is expanded to the rows "
    "between the two headings in book order. A heading below the outline depth was found by locating it as a line of "
    "the section text. The mapping was generated by script and spot-checked by an independent reviewer; where the "
    "Index's own lines wrap, an entry can carry a wrong parent, some parent-only rows are wrap artefacts, and a "
    "reference on a continuation line can be lost (an independent check of 80 sampled entries found 78 correct).",
    "How to use it: look up a term, then open the listed modules (their files are listed in `core/ai-engineering-building-applications-with-foundation-models/index.md`). "
    "`(several candidates)` means the heading could belong to more than one section, so each candidate is listed "
    "without expanding ranges. `(heading only; see sub-entries)` marks a parent term with no direct references. "
    "`unmapped` marks an entry whose references could not be resolved (listed in `coverage/known-gaps.md`).")


def main(argv):
    if not argv:
        sys.exit("usage: build_term_index.py <book.pdf> [--source-dir DIR] [--out PATH] [--keep-unmapped]")
    root = Path(__file__).resolve().parent.parent
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else root / "core/ai-engineering-building-applications-with-foundation-models/front-back-matter/p932-index.md"
    with open(matrix_path(root), newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    src = argv[argv.index("--source-dir") + 1] if "--source-dir" in argv else None
    hm = heading_map(rows)
    line_index = build_line_index(src, rows) if src else None
    entries = build_entries(extract_index_lines(argv[0]),
                            merge_fn=lambda g: merge_wrapped(g, hm, rows, line_index))
    mapping = term_rows(entries, hm, rows, line_index)
    resolved = sum(1 for v in mapping.values() if v["rows"])
    structural = sum(1 for v in mapping.values() if not v["rows"] and not v["has_refs"] and not v["see"])
    unresolved = [k for k, v in mapping.items() if not v["rows"] and (v["has_refs"] or v["see"])]
    print(f"entries: {len(mapping)}; resolved: {resolved}; heading-only: {structural}; unresolved: {len(unresolved)}")
    for k in unresolved[:40]:
        print("  unresolved:", k, "|", mapping[k]["unresolved"] or mapping[k]["see"])
    header = [
        "---", "id: B-002", "title: Index (term to module map)", 'source_pages: "932-988"', "chapter: back",
        "concepts: [index, glossary, term-lookup, navigation]", "related: []", "time_sensitive: false", "---",
        "# Index: term to module map", "(Source: PDF pp. 932-988)", "", "## What this module is", HEADER_TEXT[0], "",
        HEADER_TEXT[1], "",
        f"Entries: {len(mapping)}; resolved to modules: {resolved}; parent-only: {structural}; unmapped: {len(unresolved)}.",
        "", "## Term map", "", "| Term | Modules |", "|---|---|"]
    out.write_text("\n".join(header + render(mapping)) + "\n", encoding="utf-8")
    if "--keep-unmapped" in argv:
        (out.parent / "_index_unmapped.txt").write_text("\n".join(unresolved), encoding="utf-8")
    return mapping


if __name__ == "__main__":
    main(sys.argv[1:])
