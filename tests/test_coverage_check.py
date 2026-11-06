from coverage_check import check
from helpers import make_row, make_skill, module

R1 = dict(id="C01-001", start_page=1, end_page=3, destination_file="core/ch01-intro/p001-a.md")
R2 = dict(id="C01-002", start_page=4, end_page=6, destination_file="core/ch01-intro/p004-b.md",
          section_path="1. Intro > B")


def has(problems, text):
    return any(text in p for p in problems)


def test_clean_build_state_passes(tmp_path):
    root = make_skill(tmp_path, [make_row(**R1), make_row(**R2)])
    assert check(root, stage="build") == []


def test_gap_in_page_coverage_flagged(tmp_path):
    root = make_skill(tmp_path, [make_row(**R1), make_row(**{**R2, "start_page": 5})])
    assert has(check(root), "page 4")


def test_overlap_flagged_unless_rows_share_a_start_page(tmp_path):
    bad = make_skill(tmp_path / "a", [make_row(**R1), make_row(**{**R2, "start_page": 3})])
    assert has(check(bad), "overlap")
    ok_rows = [make_row(**{**R1, "start_page": 1, "end_page": 1}),
               make_row(**{**R2, "start_page": 1, "end_page": 6})]
    assert not has(check(make_skill(tmp_path / "b", ok_rows)), "overlap")


def test_row_without_destination_fails(tmp_path):
    root = make_skill(tmp_path, [make_row(**{**R1, "destination_file": ""})])
    assert has(check(root), "destination_file")


def test_missing_role_reason_flagged(tmp_path):
    root = make_skill(tmp_path, [make_row(**{**R1, "role_reason": " "})])
    assert has(check(root), "role_reason")


def test_bad_status_or_role_flagged(tmp_path):
    root = make_skill(tmp_path, [make_row(**{**R1, "status": "DONE", "role": "MAYBE"})])
    p = check(root)
    assert has(p, "status") and has(p, "role")


def test_verified_row_requires_existing_file(tmp_path):
    rows = [make_row(**{**R1, "status": "VERIFIED", "verification": "agent-2 2026-10-24"})]
    assert has(check(make_skill(tmp_path, rows)), "does not exist")


def test_implemented_row_requires_existing_file(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    assert has(check(make_skill(tmp_path, rows)), "does not exist")


def test_verified_requires_verification_note(tmp_path):
    rows = [make_row(**{**R1, "status": "VERIFIED"})]
    files = {R1["destination_file"]: module(pages="1-3")}
    assert has(check(make_skill(tmp_path, rows, files)), "verification")


def test_gap_requires_gaps_text(tmp_path):
    rows = [make_row(**{**R1, "status": "GAP"})]
    assert has(check(make_skill(tmp_path, rows)), "gaps")


def test_not_started_tolerated_at_build_but_not_final(tmp_path):
    root = make_skill(tmp_path, [make_row(**R1)])
    assert check(root, stage="build") == []
    assert has(check(root, stage="final"), "NOT_STARTED")


def test_cited_pages_outside_row_range_flagged(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    files = {R1["destination_file"]: module(pages="1-3", extra="See (PDF p. 9) for more.")}
    assert has(check(make_skill(tmp_path, rows, files)), "p. 9")


def test_citation_in_range_and_tail_page_ok(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED", "tail_page": 4})]
    files = {R1["destination_file"]: module(pages="1-3", extra="(PDF p. 2) and (pp. 3-4)")}
    assert check(make_skill(tmp_path, rows, files)) == []


def test_module_below_word_floor_flagged(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    files = {R1["destination_file"]: module(pages="1-3", body_words=10)}
    assert has(check(make_skill(tmp_path, rows, files)), "too short")


def test_module_with_high_source_overlap_flagged(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    source_text = " ".join(f"word{i}" for i in range(200))
    (src / "C01-001.txt").write_text(source_text, encoding="utf-8")
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    files = {R1["destination_file"]: module(pages="1-3", body_words=200)}
    root = make_skill(tmp_path / "s", rows, files)
    assert has(check(root, source_dir=src), "verbatim")


def test_actionable_row_without_workflow_fails_at_final_only(tmp_path):
    rows = [make_row(**{**R1, "status": "VERIFIED", "verification": "v"})]
    files = {R1["destination_file"]: module(pages="1-3"), "core/index.md": "# index\n"}
    root = make_skill(tmp_path, rows, files)
    assert check(root, stage="build") == []
    assert has(check(root, stage="final"), "workflow")


def test_actionable_row_named_by_workflow_passes_final(tmp_path):
    rows = [make_row(**{**R1, "status": "VERIFIED", "verification": "v"})]
    files = {R1["destination_file"]: module(pages="1-3"),
             "workflows/architect/x.md": "Uses C01-001 for planning."}
    assert check(make_skill(tmp_path, rows, files), stage="final") == []


def test_knowledge_only_row_must_be_linked_from_index_or_xref(tmp_path):
    rows = [make_row(**{**R1, "role": "KNOWLEDGE_ONLY", "status": "VERIFIED", "verification": "v"})]
    files = {R1["destination_file"]: module(pages="1-3")}
    assert has(check(make_skill(tmp_path / "a", rows, files), stage="final"), "index")
    files["core/index.md"] = "- [Planning](ch01-intro/p001-a.md)\n"
    assert check(make_skill(tmp_path / "b", rows, files), stage="final") == []


def test_frontmatter_id_and_pages_must_match_matrix(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    files = {R1["destination_file"]: module(row_id="C09-999", pages="7-8")}
    p = check(make_skill(tmp_path, rows, files))
    assert has(p, "frontmatter id") and has(p, "source_pages")


def test_non_substantive_exempt_from_module_and_workflow(tmp_path):
    rows = [make_row(**{**R1, "role": "NON_SUBSTANTIVE", "status": "VERIFIED",
                        "verification": "non-substantive: acknowledgments"})]
    assert check(make_skill(tmp_path, rows), stage="final") == []


def test_related_ids_must_exist_and_not_be_self(tmp_path):
    rows = [make_row(**{**R1, "status": "IMPLEMENTED"})]
    extra = "related: [C01-001, C01-002, C99-001]"
    mod = module(pages="1-3").replace('source_pages: "1-3"', 'source_pages: "1-3"\n' + extra)
    p = check(make_skill(tmp_path, rows, {R1["destination_file"]: mod}))
    assert has(p, "C99-001") and has(p, "itself")  # unknown id, and a reference to the module's own id
    assert has(p, "C01-002")  # also not in this one-row matrix
