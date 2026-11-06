"""Extract source text per matrix row, flag pages needing a visual check, render pages.

Usage:
  python extract_rows.py <book.pdf> <matrix.csv> <out_dir>      # text per row + index.json
  python extract_rows.py --render <book.pdf> <out_dir> <page>...  # PNGs of pages
Page numbers are 1-based PDF page indices.
"""
import csv
import json
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")
import pymupdf  # noqa: E402

SHORT_PAGE_CHARS = 200
EQUATION_RE = re.compile(r"(\bPPL\b|[A-Za-z]\s*\([^)]*\)\s*=|\s=\s|∑|Σ|√|\bEquation\b)")


def page_text(doc, n):
    return doc[n - 1].get_text()


def extract_row(pdf, start, end, tail_page=None, doc=None):
    doc = doc or pymupdf.open(pdf)
    pages = list(range(start, end + 1))
    parts, figure_pages, equation_pages = [], [], []
    for n in pages:
        t = page_text(doc, n)
        parts.append(f"=== PDF page {n} ===\n{t}")
        if len(t.strip()) < SHORT_PAGE_CHARS or re.search(r"^Figure \d+-\d+\.", t, re.M) or doc[n - 1].get_images():
            figure_pages.append(n)
        if EQUATION_RE.search(t):
            equation_pages.append(n)
    if tail_page:
        parts.append(f"=== PDF page {tail_page} (tail: may hold the end of this section) ===\n"
                     f"{page_text(doc, tail_page)}")
    return {"text": "\n".join(parts), "figure_pages": figure_pages, "equation_pages": equation_pages}


def render_pages(pdf, pages, out_dir, dpi=90, doc=None):
    doc = doc or pymupdf.open(pdf)
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    for n in pages:
        p = os.path.join(out_dir, f"p{n:03d}.png")
        doc[n - 1].get_pixmap(dpi=dpi).save(p)
        paths.append(p)
    return paths


def main(argv):
    if argv and argv[0] == "--render":
        pdf, out = argv[1], argv[2]
        for p in render_pages(pdf, [int(x) for x in argv[3:]], out):
            print(p)
        return
    pdf, matrix, out = argv
    os.makedirs(out, exist_ok=True)
    doc = pymupdf.open(pdf)
    index = {}
    with open(matrix, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tail = int(row["tail_page"]) if row.get("tail_page") else None
            r = extract_row(pdf, int(row["start_page"]), int(row["end_page"]), tail, doc=doc)
            with open(os.path.join(out, f"{row['id']}.txt"), "w", encoding="utf-8") as g:
                g.write(r["text"])
            index[row["id"]] = {"figure_pages": r["figure_pages"], "equation_pages": r["equation_pages"],
                                "chars": len(r["text"])}
    with open(os.path.join(out, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, indent=1)
    print(len(index), "rows extracted to", out)


if __name__ == "__main__":
    main(sys.argv[1:])
