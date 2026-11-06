import sys
from pathlib import Path

import pytest

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

BOOK_PDF = Path(r"book.pdf")


@pytest.fixture
def fixture_pdf(tmp_path):
    """22-page PDF whose outline mimics the book: Preface, chapters with
    sections/subsections/summaries, Epilogue, Index, About the Author."""
    from pypdf import PdfWriter

    w = PdfWriter()
    for _ in range(22):
        w.add_blank_page(width=200, height=200)
    pre = w.add_outline_item("Preface", 2)  # page 3 (0-based 2)
    w.add_outline_item("What This Book Is About", 3, parent=pre)  # p4
    w.add_outline_item("Acknowledgments", 4, parent=pre)  # p5
    c1 = w.add_outline_item("1. Introduction", 5)  # p6
    rise = w.add_outline_item("The Rise", 7, parent=c1)  # p8
    w.add_outline_item("From Language Models to Large Language Models", 8, parent=rise)  # p9
    w.add_outline_item("From Large Language Models to Foundation Models", 9, parent=rise)  # p10
    w.add_outline_item("Planning", 11, parent=c1)  # p12
    w.add_outline_item("Summary", 13, parent=c1)  # p14
    c2 = w.add_outline_item("2. Foundation Models", 14)  # p15
    td = w.add_outline_item("Training Data", 14, parent=c2)  # p15 (same page)
    w.add_outline_item("Multilingual Models", 16, parent=td)  # p17
    w.add_outline_item("Summary", 17, parent=c2)  # p18
    w.add_outline_item("Epilogue", 18)  # p19
    w.add_outline_item("Index", 20)  # p21
    w.add_outline_item("About the Author", 21)  # p22
    p = tmp_path / "fixture.pdf"
    with open(p, "wb") as f:
        w.write(f)
    return p
