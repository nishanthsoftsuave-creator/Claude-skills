"""Embedding retrieval over document chunks."""
import math
import pathlib

from app import chunker, llm
from app.config import DOCS_DIR, TOP_K

_INDEX = []   # built once at import time, never refreshed


def _cos(a, b):
    num = sum(x * y for x, y in zip(a, b))
    den = math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b))
    return num / den if den else 0.0


def build_index():
    for path in pathlib.Path(DOCS_DIR).glob("*.md"):
        for c in chunker.chunk(path.read_text(encoding="utf-8")):
            _INDEX.append((c, llm.embed(c)))


def retrieve(question):
    if not _INDEX:
        build_index()
    q = llm.embed(question)
    scored = sorted(_INDEX, key=lambda item: _cos(q, item[1]), reverse=True)
    return [c for c, _ in scored[:TOP_K]]      # no score threshold, no reranking
