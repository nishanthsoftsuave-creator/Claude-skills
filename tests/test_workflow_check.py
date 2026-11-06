from helpers import make_row, make_skill
from workflow_check import check

ROWS = [make_row(id="C03-010", start_page=1, end_page=3, destination_file="core/ch03-eval-methodology/p001-a.md"),
        make_row(id="C03-011", start_page=4, end_page=6, destination_file="core/ch03-eval-methodology/p004-b.md",
                 section_path="3. X > B")]


def wf(name="run-checks", mode="review-test", rows="[C03-010]", body="Use [C03-010] here."):
    return f"---\nname: {name}\nmode: {mode}\nrows: {rows}\n---\n# {name}\n{body}\n"


def has(problems, text):
    return any(text in p for p in problems)


def run(tmp_path, files, expected=None):
    root = make_skill(tmp_path, ROWS, files)
    return check(root, expected=expected or [])


def test_valid_workflow_passes(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf()})
    assert p == []


def test_missing_expected_workflow_flagged(tmp_path):
    p = run(tmp_path, {}, expected=[("review-test", "run-checks")])
    assert has(p, "run-checks")


def test_name_and_mode_must_match_file_and_folder(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf(name="other", mode="architect")})
    assert has(p, "name") and has(p, "mode")


def test_unknown_row_in_rows_list_flagged(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf(rows="[C03-010, C99-001]", body="[C03-010] [C99-001]")})
    assert has(p, "C99-001")


def test_row_listed_but_not_cited_in_body_flagged(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf(rows="[C03-010, C03-011]", body="only [C03-010]")})
    assert has(p, "C03-011")


def test_cited_row_missing_from_rows_list_flagged(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf(rows="[C03-010]", body="[C03-010] and [C03-011]")})
    assert has(p, "C03-011") and has(p, "rows")


def test_empty_rows_flagged(tmp_path):
    p = run(tmp_path, {"workflows/review-test/run-checks.md": wf(rows="[]", body="nothing")})
    assert has(p, "rows")


def test_cites_inside_code_blocks_ignored(tmp_path):
    body = "[C03-010]\n```\n[C03-011]\n```"
    assert run(tmp_path, {"workflows/review-test/run-checks.md": wf(body=body)}) == []
