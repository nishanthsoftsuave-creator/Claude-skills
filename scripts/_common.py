"""Shared helpers for the check scripts."""
import csv
import re
from pathlib import Path

STATUSES = {"NOT_STARTED", "IN_PROGRESS", "IMPLEMENTED", "VERIFIED", "GAP"}
ROLES = {"ACTIONABLE", "KNOWLEDGE_ONLY", "NON_SUBSTANTIVE"}
CITE_RE = re.compile(r"\bpp?\.\s*(\d{1,3})(?:\s*[–-]\s*(\d{1,3}))?")


def matrix_path(root, book=None):
    """Return a book matrix, retaining the root-level fallback for older test fixtures."""
    root = Path(root)
    if book:
        return root / "coverage" / book / "coverage-matrix.csv"
    nested = root / "coverage" / "ai-engineering-building-applications-with-foundation-models" / "coverage-matrix.csv"
    return nested if nested.exists() else root / "coverage" / "coverage-matrix.csv"


def core_dir(root, book=None):
    """Where a book's modules and generated index files live."""
    if book:
        return Path(root) / "core" / book
    rows = load_matrix(root)
    nested = any(r.get("destination_file", "").startswith(
        "core/ai-engineering-building-applications-with-foundation-models/") for r in rows)
    return Path(root) / "core" / ("ai-engineering-building-applications-with-foundation-models" if nested else "")


def load_matrix(root, book=None):
    with open(matrix_path(root, book), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def split_frontmatter(text):
    """Return (dict of simple `key: value` frontmatter, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, text[end + 4:]


def words(text):
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def shingles(ws, n=8):
    return {" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def md_files(root, include=("core", "workflows", "templates"), top_files=("SKILL.md", "README.md", "MAINTENANCE.md")):
    root = Path(root)
    out = []
    for d in include:
        out += sorted((root / d).rglob("*.md")) if (root / d).exists() else []
    out += [root / f for f in top_files if (root / f).exists()]
    return out
