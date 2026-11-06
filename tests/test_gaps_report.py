from gaps_report import update_gaps_section
from helpers import make_row, make_skill

START, END = "<!-- gaps:start -->", "<!-- gaps:end -->"


def skill_with_gaps(tmp_path, known="# Gaps\n\nintro\n\n" + START + "\nold\n" + END + "\n\n## Other\nkeep me\n"):
    rows = [make_row(id="C01-001", start_page=1, end_page=3, status="VERIFIED", gaps="Table clipped on PDF p. 2",
                     section_path="1. Intro > A"),
            make_row(id="C01-002", start_page=4, end_page=6, status="VERIFIED", gaps="",
                     destination_file="core/ch01-intro/p004-b.md", section_path="1. Intro > B")]
    return make_skill(tmp_path, rows, {"coverage/known-gaps.md": known})


def test_section_lists_rows_with_gaps_only(tmp_path):
    root = skill_with_gaps(tmp_path)
    n = update_gaps_section(root)
    text = (root / "coverage" / "known-gaps.md").read_text(encoding="utf-8")
    assert n == 1 and "C01-001" in text and "Table clipped on PDF p. 2" in text
    assert "C01-002" not in text and "old" not in text.split(START)[1].split(END)[0]


def test_text_outside_markers_is_kept(tmp_path):
    root = skill_with_gaps(tmp_path)
    update_gaps_section(root)
    text = (root / "coverage" / "known-gaps.md").read_text(encoding="utf-8")
    assert "intro" in text and "keep me" in text


def test_idempotent(tmp_path):
    root = skill_with_gaps(tmp_path)
    update_gaps_section(root)
    a = (root / "coverage" / "known-gaps.md").read_text(encoding="utf-8")
    update_gaps_section(root)
    assert a == (root / "coverage" / "known-gaps.md").read_text(encoding="utf-8")


def test_missing_markers_are_added(tmp_path):
    root = skill_with_gaps(tmp_path, known="# Gaps\n\nonly intro\n")
    update_gaps_section(root)
    text = (root / "coverage" / "known-gaps.md").read_text(encoding="utf-8")
    assert START in text and END in text and "C01-001" in text and "only intro" in text
