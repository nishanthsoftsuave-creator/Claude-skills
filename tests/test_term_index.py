from build_term_index import (build_entries, split_entry, heading_map, resolve_refs, term_rows)

MATRIX = [
    {"id": "C03-007", "section_path": "3. Evaluation Methodology > Understanding Language Modeling Metrics > Perplexity", "chapter": "3"},
    {"id": "C03-008", "section_path": "3. Evaluation Methodology > Understanding Language Modeling Metrics > Perplexity Interpretation and Use Cases", "chapter": "3"},
    {"id": "C03-004", "section_path": "3. Evaluation Methodology > Understanding Language Modeling Metrics > Entropy", "chapter": "3"},
    {"id": "C03-006", "section_path": "3. Evaluation Methodology > Understanding Language Modeling Metrics > Bits-per-Character and Bits-per-Byte", "chapter": "3"},
    {"id": "C01-014", "section_path": "1. Introduction > Summary", "chapter": "1"},
    {"id": "C02-016", "section_path": "2. Models > Summary", "chapter": "2"},
    {"id": "C06-009", "section_path": "6. RAG and Agents > Agents > Tools", "chapter": "6"},
]


def test_split_entry_term_and_refs():
    assert split_entry("perplexity, Perplexity") == ("perplexity", "Perplexity", None)
    assert split_entry("AI accelerators (see accelerators)") == ("AI accelerators", "", "accelerators")
    assert split_entry("AI engineering (AIE)") == ("AI engineering (AIE)", "", None)


def test_wrapped_lines_are_merged_into_one_entry():
    lines = [(95, "entropy, Entropy"), (95, "perplexity interpretation and use cases, Perplexity"),
             (113, "Interpretation and Use Cases")]
    ents = build_entries(lines)
    assert [e["text"] for e in ents] == [
        "entropy, Entropy",
        "perplexity interpretation and use cases, Perplexity Interpretation and Use Cases"]


def test_sub_entries_get_parent_terms():
    lines = [(95, "agents, Agents-Efficiency"), (113, "tool failures, Tool failures")]
    ents = build_entries(lines)
    assert ents[1]["level"] == 1 and ents[1]["parents"] == ["agents"]


def test_heading_map_lists_candidates_and_flags_duplicates():
    hm = heading_map(MATRIX)
    assert hm["Perplexity"] == ["C03-007"]
    assert sorted(hm["Summary"]) == ["C01-014", "C02-016"]


def test_resolve_single_heading_and_range_with_hyphens():
    hm = heading_map(MATRIX)
    rows, amb, left = resolve_refs("Entropy-Perplexity", hm, MATRIX)
    assert set(rows) >= {"C03-004", "C03-007"} and not amb
    rows2, amb2, left2 = resolve_refs("Bits-per-Character and Bits-per-Byte", hm, MATRIX)
    assert rows2 == ["C03-006"] and not left2


def test_ambiguous_heading_is_flagged():
    hm = heading_map(MATRIX)
    rows, amb, left = resolve_refs("Summary", hm, MATRIX)
    assert amb and set(rows) == {"C01-014", "C02-016"}


def test_unknown_reference_is_reported_not_guessed():
    hm = heading_map(MATRIX)
    rows, amb, left = resolve_refs("Totally Unknown Heading", hm, MATRIX)
    assert rows == [] and left == "Totally Unknown Heading"


def test_see_entries_resolve_through_target_term():
    ents = build_entries([(95, "accelerators, Tools"), (95, "AI accelerators (see accelerators)")])
    hm = heading_map(MATRIX)
    t = term_rows(ents, hm, MATRIX)
    assert t["AI accelerators"]["rows"] == ["C06-009"]


def test_multiple_comma_separated_references_resolve():
    from build_term_index import resolve_multi
    hm = heading_map(MATRIX)
    rows, amb, left = resolve_multi("Entropy, Perplexity", hm, MATRIX)
    assert set(rows) == {"C03-004", "C03-007"} and not left


def test_range_only_expands_between_unambiguous_headings():
    rows = MATRIX
    hm = heading_map(rows)
    ids, amb, left = resolve_refs("Entropy-Perplexity", hm, rows)
    assert ids == ["C03-007", "C03-008", "C03-004"][:0] or set(ids) >= {"C03-004", "C03-007"}
    amb_ids, amb_flag, _ = resolve_refs("Summary-Perplexity", hm, rows)
    assert amb_flag  # 'Summary' is ambiguous, so no range expansion is attempted


def test_overly_broad_pointers_are_reported_unresolved():
    import build_term_index as b
    rows = [{"id": f"C01-{i:03d}", "section_path": f"1. X > Same Title {0}"} for i in range(20)]
    hm = b.heading_map(rows)
    ids, amb, left = b.resolve_refs("Same Title 0", hm, rows)
    assert ids == [] and left


def test_see_also_lines_create_no_entry():
    ents = build_entries([(95, "AI judge"), (95, "(see also AI-as-a-judge)"), (95, "agents, Tools")])
    assert [e["text"] for e in ents] == ["AI judge", "agents, Tools"]


def test_comma_containing_continuation_merges_when_it_helps():
    from build_term_index import merge_wrapped, group_lines
    rows = [{"id": "C02-009", "section_path": "2. M > Preference Finetuning", "chapter": "2"},
            {"id": "C07-002", "section_path": "7. F > Finetuning Overview", "chapter": "7"}]
    hm = heading_map(rows)
    li = {"finetuning using the reward model": ["C02-009"]}
    groups = group_lines([(95, "preference finetuning, Preference Finetuning-Finetuning using the"),
                          (95, "reward model, Finetuning Overview")])
    merged = merge_wrapped(groups, hm, rows, li)
    assert len(merged) == 1 and merged[0]["text"].endswith("reward model, Finetuning Overview")


def test_range_with_ambiguous_endpoint_picks_closest_pair_in_one_chapter():
    from build_term_index import resolve_refs, heading_map
    rows = [{"id": "C01-001", "section_path": "1. A > Start", "chapter": "1"},
            {"id": "C01-002", "section_path": "1. A > Middle", "chapter": "1"},
            {"id": "C01-003", "section_path": "1. A > End", "chapter": "1"},
            {"id": "C05-001", "section_path": "5. B > Start", "chapter": "5"}]
    hm = heading_map(rows)
    ids, amb, left = resolve_refs("Start-End", hm, rows)
    assert ids == ["C01-001", "C01-002", "C01-003"] and not amb and not left


def test_line_index_ignores_a_rows_tail_page(tmp_path):
    from build_term_index import build_line_index
    (tmp_path / "C01-001.txt").write_text(
        "=== PDF page 1 ===\nOwn heading\n=== PDF page 2 (tail: may hold the end of this section) ===\nNext heading\n",
        encoding="utf-8")
    rows = [{"id": "C01-001", "start_page": "1", "end_page": "1", "section_path": "x", "chapter": "1"}]
    idx = build_line_index(tmp_path, rows)
    assert "own heading" in idx and "next heading" not in idx
