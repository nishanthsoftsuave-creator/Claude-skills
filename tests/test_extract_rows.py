import csv
import warnings

import pytest

warnings.filterwarnings("ignore")
pymupdf = pytest.importorskip("pymupdf")

from extract_rows import extract_row, render_pages, main  # noqa: E402


@pytest.fixture
def text_pdf(tmp_path):
    d = pymupdf.open()
    texts = [
        "Chapter text page one " * 20,
        "Perplexity is defined as PPL (P) = 2H(P) and H = - sum p log p " + "filler " * 40,
        "Figure 2-7. A visualization",  # short page: figure-ish
        "Back to prose " * 30,
    ]
    for t in texts:
        page = d.new_page()
        page.insert_textbox(pymupdf.Rect(40, 40, 560, 780), t, fontsize=9)
    p = tmp_path / "t.pdf"
    d.save(str(p))
    return p


def test_page_markers_for_each_page(text_pdf):
    r = extract_row(str(text_pdf), 1, 2)
    assert "=== PDF page 1 ===" in r["text"] and "=== PDF page 2 ===" in r["text"]
    assert "=== PDF page 3 ===" not in r["text"]


def test_tail_page_included_and_marked(text_pdf):
    r = extract_row(str(text_pdf), 1, 2, tail_page=3)
    assert "=== PDF page 3 (tail: may hold the end of this section) ===" in r["text"]


def test_short_pages_flagged_as_figure_pages(text_pdf):
    r = extract_row(str(text_pdf), 2, 4)
    assert r["figure_pages"] == [3]


def test_equation_pages_flagged(text_pdf):
    r = extract_row(str(text_pdf), 2, 2)
    assert r["equation_pages"] == [2]


def test_render_pages_writes_png(text_pdf, tmp_path):
    paths = render_pages(str(text_pdf), [1, 3], str(tmp_path / "img"), dpi=40)
    assert len(paths) == 2 and all(p.endswith(".png") for p in paths)


def test_cli_writes_one_file_per_row(text_pdf, tmp_path):
    m = tmp_path / "m.csv"
    with open(m, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["id", "start_page", "end_page", "tail_page"])
        w.writeheader()
        w.writerow({"id": "C01-001", "start_page": 1, "end_page": 2, "tail_page": ""})
        w.writerow({"id": "C01-002", "start_page": 3, "end_page": 4, "tail_page": ""})
    out = tmp_path / "out"
    main([str(text_pdf), str(m), str(out)])
    assert (out / "C01-001.txt").exists() and (out / "C01-002.txt").exists()
    assert (out / "index.json").exists()
