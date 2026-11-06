"""Single writer for a book's coverage matrix (parallel agents must not edit the CSV).

Usage: python matrix_update.py --ids C03-001,C03-002 --status IMPLEMENTED
                               [--verification "note"] [--gaps "text"] [--root DIR]
"""
import argparse
import csv
import sys
from pathlib import Path

from _common import STATUSES, load_matrix, matrix_path


def update(root, ids, status=None, verification=None, gaps=None, tail_page=None):
    rows = load_matrix(root)
    by_id = {r["id"]: r for r in rows}
    missing = [i for i in ids if i not in by_id]
    if missing:
        raise KeyError(f"unknown row ids: {missing}")
    if status is not None and status not in STATUSES:
        raise ValueError(f"invalid status {status!r}")
    for i in ids:
        if status is not None:
            by_id[i]["status"] = status
        if verification is not None:
            by_id[i]["verification"] = verification
        if gaps is not None:
            by_id[i]["gaps"] = gaps
        if tail_page is not None:
            by_id[i]["tail_page"] = str(tail_page)
    path = matrix_path(root)
    with open(path, newline="", encoding="utf-8") as f:
        fieldnames = csv.DictReader(f).fieldnames
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    return len(ids)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--ids", required=True, help="comma-separated row ids")
    ap.add_argument("--status")
    ap.add_argument("--verification")
    ap.add_argument("--gaps")
    ap.add_argument("--tail", help="set tail_page (the page after the range that holds this section's end)")
    a = ap.parse_args(argv)
    n = update(a.root, [i.strip() for i in a.ids.split(",") if i.strip()], a.status, a.verification, a.gaps, a.tail)
    print(f"updated {n} row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
