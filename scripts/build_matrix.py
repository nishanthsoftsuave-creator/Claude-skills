"""Build the coverage matrix (one row per leaf block of the book) from a PDF outline.

Usage: python build_matrix.py <book.pdf> <out.csv>
Page numbers are 1-based PDF page indices.
"""
import csv
import re
import sys

from pypdf import PdfReader

COLUMNS = [
    "id", "chapter", "section_path", "start_page", "end_page", "tail_page",
    "role", "role_reason", "destination_file", "status", "verification", "gaps",
]

CHAPTER_DIRS = {
    1: "ch01-intro", 2: "ch02-foundation-models", 3: "ch03-eval-methodology",
    4: "ch04-eval-systems", 5: "ch05-prompting", 6: "ch06-rag-agents-memory",
    7: "ch07-finetuning", 8: "ch08-datasets", 9: "ch09-inference",
    10: "ch10-architecture-feedback",
}
FRONT_BACK = "front-back-matter"
NON_SUBSTANTIVE_PREFACE = ("acknowledg", "using code examples", "online learning",
                           "how to contact", "conventions used")
NON_SUBSTANTIVE_TOP = {"about the author"}
KNOWLEDGE_SUBSECTIONS_CH1 = {"from language models to large language models",
                             "from large language models to foundation models",
                             "from foundation models to ai engineering"}


class Node:
    def __init__(self, depth, title, page):
        self.depth, self.title, self.page, self.children = depth, title, page, []


def load_outline(reader):
    roots, stack = [], []

    def walk(items, depth):
        last = None
        for it in items:
            if isinstance(it, list):
                if last is not None:
                    walk(it, depth + 1)
                continue
            n = Node(depth, str(it.title).strip(), reader.get_destination_page_number(it) + 1)
            (roots if depth == 0 else last_parent[depth - 1].children).append(n)
            last_parent[depth] = n
            last = n

    last_parent = {}
    walk(reader.outline, 0)
    return roots


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:50].strip("-") or "section"


def chapter_number(title):
    m = re.match(r"^(\d+)\.\s", title)
    return int(m.group(1)) if m else None


def make_blocks(roots, total_pages):
    """Flatten the outline tree to leaf blocks in document order."""
    blocks = []

    def add(title_path, start, role, reason, chapter, folder):
        blocks.append({"path": title_path, "start": start, "role": role, "reason": reason,
                       "chapter": chapter, "folder": folder})

    first = roots[0].page
    if first > 1:
        add("Front matter", 1, "NON_SUBSTANTIVE", "title page, copyright and table of contents", "front", FRONT_BACK)

    for top in roots:
        num = chapter_number(top.title)
        low = top.title.lower()
        if num is not None:
            folder = CHAPTER_DIRS.get(num, f"ch{num:02d}")
            chap = str(num)
            secs = top.children
            if secs and secs[0].page > top.page:
                add(f"{top.title} > (chapter intro)", top.page, "KNOWLEDGE_ONLY",
                    "chapter framing before the first section", chap, folder)
            elif not secs:
                add(top.title, top.page, "ACTIONABLE", "chapter without sections", chap, folder)
            for sec in secs:
                base = f"{top.title} > {sec.title}"
                if sec.title == "Summary":
                    add(base, sec.page, "KNOWLEDGE_ONLY", "chapter summary", chap, folder)
                elif sec.children:
                    if sec.children[0].page > sec.page:
                        add(f"{base} > (section lead-in)", sec.page, "KNOWLEDGE_ONLY",
                            "section text before its first subsection", chap, folder)
                    for sub in sec.children:
                        known = num == 1 and sub.title.lower() in KNOWLEDGE_SUBSECTIONS_CH1
                        add(f"{base} > {sub.title}", sub.page,
                            "KNOWLEDGE_ONLY" if known else "ACTIONABLE",
                            "historical and conceptual background" if known else "feeds a workflow",
                            chap, folder)
                else:
                    add(base, sec.page, "ACTIONABLE", "feeds a workflow", chap, folder)
        elif low == "preface":
            if top.children and top.children[0].page > top.page:
                add("Preface > (intro)", top.page, "KNOWLEDGE_ONLY", "preface opening", "preface", FRONT_BACK)
            for sec in top.children:
                ns = any(k in sec.title.lower() for k in NON_SUBSTANTIVE_PREFACE)
                add(f"Preface > {sec.title}", sec.page,
                    "NON_SUBSTANTIVE" if ns else "KNOWLEDGE_ONLY",
                    "administrative preface item" if ns else "framing of the book's scope and audience",
                    "preface", FRONT_BACK)
            if not top.children:
                add("Preface", top.page, "KNOWLEDGE_ONLY", "preface", "preface", FRONT_BACK)
        elif low in NON_SUBSTANTIVE_TOP:
            add(top.title, top.page, "NON_SUBSTANTIVE", "author biography", "back", FRONT_BACK)
        else:  # Epilogue, Index, ...
            add(top.title, top.page, "KNOWLEDGE_ONLY",
                "term list that seeds the glossary" if low == "index" else "closing reflections",
                "back", FRONT_BACK)

    for i, b in enumerate(blocks):
        nxt = blocks[i + 1]["start"] if i + 1 < len(blocks) else total_pages + 1
        b["end"] = nxt - 1 if nxt > b["start"] else b["start"]
        b["next_start"] = nxt if i + 1 < len(blocks) else None
    return blocks


def heading_at_page_top(reader, page_no, title):
    """True when `title` appears near the top of the page (a clean page break)."""
    try:
        text = reader.pages[page_no - 1].extract_text() or ""
    except Exception:
        return False
    head = re.sub(r"\s+", " ", text[:500]).lower()
    key = re.sub(r"^(\d+\.|step \d\.)\s*", "", title.split(" > ")[-1].lower())
    key = re.sub(r"\(.*?\)", "", key).strip()[:25]
    return bool(key) and key in head


def build_matrix(pdf, out_csv, detect_tail=True):
    reader = PdfReader(pdf)
    total = len(reader.pages)
    blocks = make_blocks(load_outline(reader), total)
    starts = [b["start"] for b in blocks]
    if starts != sorted(starts):
        raise ValueError("outline pages are not in document order")

    counters, rows = {}, []
    for b in blocks:
        chap = b["chapter"]
        counters[chap] = counters.get(chap, 0) + 1
        prefix = f"C{int(chap):02d}" if chap.isdigit() else chap[:1].upper()
        rid = f"{prefix}-{counters[chap]:03d}"
        tail = ""
        if detect_tail and b["next_start"] and b["next_start"] <= total:
            nxt_title = next(x["path"] for x in blocks if x["start"] == b["next_start"])
            if not heading_at_page_top(reader, b["next_start"], nxt_title):
                tail = b["next_start"]
        elif not detect_tail:
            tail = ""
        last = b["path"].split(" > ")[-1]
        dest = f"core/ai-engineering-building-applications-with-foundation-models/{b['folder']}/p{b['start']:03d}-{slug(last)}.md"
        rows.append({
            "id": rid, "chapter": chap, "section_path": b["path"],
            "start_page": b["start"], "end_page": b["end"], "tail_page": tail,
            "role": b["role"], "role_reason": b["reason"], "destination_file": dest,
            "status": "NOT_STARTED", "verification": "", "gaps": "",
        })
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: build_matrix.py <book.pdf> <out.csv>")
    print(build_matrix(sys.argv[1], sys.argv[2]), "rows")
