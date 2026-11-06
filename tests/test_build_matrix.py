import csv

import pytest

from build_matrix import build_matrix, COLUMNS
from conftest import BOOK_PDF


def rows_of(csv_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build(pdf, tmp_path, **kw):
    out = tmp_path / "m.csv"
    n = build_matrix(str(pdf), str(out), **kw)
    return n, rows_of(out)


def test_columns_and_count_returned(fixture_pdf, tmp_path):
    n, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    assert n == len(rows)
    assert list(rows[0].keys()) == COLUMNS


def test_every_page_covered_at_least_once(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    covered = set()
    for r in rows:
        covered |= set(range(int(r["start_page"]), int(r["end_page"]) + 1))
    assert covered == set(range(1, 23))


def test_pages_overlap_only_when_headings_share_a_start_page(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    seen = {}
    for r in rows:
        for p in range(int(r["start_page"]), int(r["end_page"]) + 1):
            seen.setdefault(p, []).append(r["id"])
    for p, ids in seen.items():
        assert len(ids) == 1, f"page {p} in {ids}"


def test_lead_in_row_created_for_parent_with_gap_before_first_child(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    lead = [r for r in rows if "lead-in" in r["section_path"] and "The Rise" in r["section_path"]]
    assert len(lead) == 1
    assert (lead[0]["start_page"], lead[0]["end_page"]) == ("8", "8")
    # Training Data starts on the chapter's first page: no chapter-intro row for ch 2
    assert not [r for r in rows if r["section_path"].startswith("2. Foundation Models > (chapter intro)")]
    td = [r for r in rows if "Training Data" in r["section_path"] and "lead-in" in r["section_path"]]
    assert (td[0]["start_page"], td[0]["end_page"]) == ("15", "16")


def test_chapter_intro_row_when_pages_precede_first_section(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    intro = [r for r in rows if r["section_path"] == "1. Introduction > (chapter intro)"]
    assert len(intro) == 1
    assert (intro[0]["start_page"], intro[0]["end_page"]) == ("6", "7")


def test_front_matter_row_covers_pages_before_first_outline_entry(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    assert (rows[0]["start_page"], rows[0]["end_page"]) == ("1", "2")
    assert rows[0]["role"] == "NON_SUBSTANTIVE"


def test_all_rows_start_not_started_with_destination_and_role_reason(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    for r in rows:
        assert r["status"] == "NOT_STARTED"
        assert r["destination_file"].startswith("core/") and r["destination_file"].endswith(".md")
        assert r["role"] in {"ACTIONABLE", "KNOWLEDGE_ONLY", "NON_SUBSTANTIVE"}
        assert r["role_reason"].strip()


def test_ids_and_destinations_unique(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    assert len({r["id"] for r in rows}) == len(rows)
    assert len({r["destination_file"] for r in rows}) == len(rows)


def test_roles(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    by = {r["section_path"]: r for r in rows}
    assert by["Preface > Acknowledgments"]["role"] == "NON_SUBSTANTIVE"
    assert by["Preface > What This Book Is About"]["role"] == "KNOWLEDGE_ONLY"
    assert by["1. Introduction > Summary"]["role"] == "KNOWLEDGE_ONLY"
    assert by["1. Introduction > The Rise > From Language Models to Large Language Models"]["role"] == "KNOWLEDGE_ONLY"
    assert by["1. Introduction > Planning"]["role"] == "ACTIONABLE"
    assert by["2. Foundation Models > Training Data > Multilingual Models"]["role"] == "ACTIONABLE"
    assert by["Epilogue"]["role"] == "KNOWLEDGE_ONLY"
    assert by["Index"]["role"] == "KNOWLEDGE_ONLY"
    assert by["About the Author"]["role"] == "NON_SUBSTANTIVE"


def test_chapter_folder_in_destination(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    by = {r["section_path"]: r for r in rows}
    assert by["1. Introduction > Planning"]["destination_file"].startswith("core/ai-engineering-building-applications-with-foundation-models/ch01-intro/")
    assert by["Epilogue"]["destination_file"].startswith("core/ai-engineering-building-applications-with-foundation-models/front-back-matter/")


def test_last_row_ends_at_last_page(fixture_pdf, tmp_path):
    _, rows = build(fixture_pdf, tmp_path, detect_tail=False)
    assert rows[-1]["end_page"] == "22"


@pytest.mark.skipif(not BOOK_PDF.exists(), reason="book PDF not on this machine")
def test_real_book_counts_match_outline(tmp_path):
    n, rows = build(BOOK_PDF, tmp_path, detect_tail=False)
    paths = [r["section_path"] for r in rows]
    sub = [p for p in paths if p.count(" > ") == 2 and "lead-in" not in p and "chapter intro" not in p
           and not p.startswith("Preface")]
    summaries = [p for p in paths if p.endswith("> Summary")]
    assert len(summaries) == 10
    assert len(sub) == 112
    covered = set()
    for r in rows:
        covered |= set(range(int(r["start_page"]), int(r["end_page"]) + 1))
    assert covered == set(range(1, 992))
    assert 170 <= n <= 230
