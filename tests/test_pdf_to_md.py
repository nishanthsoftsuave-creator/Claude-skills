import pytest

pymupdf = pytest.importorskip("pymupdf")

from pdf_to_md import convert  # noqa: E402


def _pdf(tmp_path, pages, toc):
    """pages: one list of (x, baseline y, font size, text) per page; the page size is 504 x 720 like the real book."""
    doc = pymupdf.open()
    for texts in pages:
        page = doc.new_page(width=504, height=720)
        for x, y, size, text in texts:
            page.insert_text((x, y), text, fontsize=size)
    doc.set_toc(toc)
    path = tmp_path / "book.pdf"
    doc.save(str(path))
    return path


@pytest.fixture
def book(tmp_path):
    """A skipped Contents page, then a chapter: opener, two sections, a hyphen-split word, running head, page numbers."""
    head = (36, 60, 10, "Chapter 1  RUNNING HEAD")
    return _pdf(tmp_path, [
        [(36, 100, 20, "Contents"), (36, 140, 11, "Nothing to convert here.")],
        [head, (36, 120, 18, "CHAPTER 1"), (36, 170, 40, "Alpha Beta"), (36, 230, 11, "Opening text of the chapter."),
         (36, 330, 20, "First Section"), (36, 370, 11, "Body of the first section with orga-"),
         (36, 384, 11, "nization and more."), (36, 690, 11, "2")],
        [head, (36, 120, 20, "Second Section"), (36, 160, 11, "The organization is large."), (36, 690, 11, "3")],
    ], [[1, "Contents", 1], [1, "Chapter 1: Alpha Beta", 2], [2, "First Section", 2], [2, "Second Section", 3]])


def test_sections_become_files_with_page_markers(book, tmp_path):
    n, warns = convert(book, tmp_path, "demo", "Demo book", skip=["Contents"])
    base = tmp_path / "core" / "demo" / "ch01-alpha-beta"
    assert sorted(p.name for p in base.glob("*.md")) == ["p002-chapter-intro.md", "p002-first-section.md", "p003-second-section.md"]
    assert (n, warns) == (3, [])
    intro = (base / "p002-chapter-intro.md").read_text(encoding="utf-8").split("(Source:", 1)[1]
    assert "Opening text of the chapter." in intro and "CHAPTER" not in intro and "Alpha Beta" not in intro
    first = (base / "p002-first-section.md").read_text(encoding="utf-8")
    assert "organization and more." in first  # orga- + nization: the split word is glued
    assert "<!-- PDF p. 2 (book p. 2) -->" in first and "RUNNING HEAD" not in first
    second = (base / "p003-second-section.md").read_text(encoding="utf-8")
    assert "(Source: PDF p. 3)" in second and "<!-- PDF p. 3 (book p. 3) -->" in second
    index = (tmp_path / "core" / "demo" / "index.md").read_text(encoding="utf-8")
    assert "Contents (not converted)" in index and "p003-second-section.md" in index


def test_refuses_to_overwrite_a_folder_it_did_not_generate(book, tmp_path):
    foreign = tmp_path / "core" / "demo"
    foreign.mkdir(parents=True)
    (foreign / "notes.md").write_text("mine", encoding="utf-8")
    with pytest.raises(SystemExit):
        convert(book, tmp_path, "demo", "Demo book", skip=["Contents"])
    assert (foreign / "notes.md").exists()


def test_ruled_table_becomes_a_pipe_table(tmp_path):
    pdf = _pdf(tmp_path, [[(36, 60, 20, "Table Book"), (60, 125, 11, "Name"), (210, 125, 11, "Value"), (60, 165, 11, "alpha"),
                           (210, 165, 11, "one"), (60, 205, 11, "beta"), (210, 205, 11, "two")]], [[1, "Table Book", 1]])
    page = pymupdf.open(str(pdf))[0]
    shape = page.new_shape()
    for x in (50, 200, 350):
        shape.draw_line((x, 100), (x, 220))
    for y in (100, 140, 180, 220):
        shape.draw_line((50, y), (350, y))
    shape.finish(width=1)
    shape.commit()
    doc = page.parent
    doc.set_toc([[1, "Table Book", 1]])
    doc.save(str(tmp_path / "table.pdf"))
    convert(tmp_path / "table.pdf", tmp_path, "tbl", "Table book")
    text = (tmp_path / "core" / "tbl" / "front-back-matter" / "p001-table-book.md").read_text(encoding="utf-8")
    assert "| Name | Value |" in text and "| alpha | one |" in text and "| beta | two |" in text
