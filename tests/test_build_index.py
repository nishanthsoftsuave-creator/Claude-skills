from build_index import build
from helpers import make_row, make_skill
from link_check import check as links


def module(rid, title, pages, concepts="[alpha, beta]", related="[]"):
    return (f'---\nid: {rid}\ntitle: {title}\nsource_pages: "{pages}"\nchapter: 1\n'
            f'concepts: {concepts}\nrelated: {related}\ntime_sensitive: false\n---\n# {title}\nbody\n')


def setup(tmp_path):
    rows = [
        make_row(id="C01-001", start_page=1, end_page=3, status="VERIFIED",
                 destination_file="core/ch01-intro/p001-a.md", section_path="1. Intro > A"),
        make_row(id="C01-002", start_page=4, end_page=6, status="VERIFIED", role="KNOWLEDGE_ONLY",
                 destination_file="core/ch01-intro/p004-b.md", section_path="1. Intro > B"),
        make_row(id="P-010", chapter="preface", start_page=7, end_page=7, status="VERIFIED", role="NON_SUBSTANTIVE",
                 destination_file="core/front-back-matter/p007-ack.md", section_path="Preface > Acknowledgments",
                 role_reason="administrative preface item"),
    ]
    files = {
        "core/ch01-intro/p001-a.md": module("C01-001", "Alpha topic", "1-3", "[alpha, gamma]", "[C01-002]"),
        "core/ch01-intro/p004-b.md": module("C01-002", "Beta topic", "4-6", "[beta, gamma]", "[C01-001]"),
    }
    return make_skill(tmp_path, rows, files)


def test_index_lists_every_module_with_a_relative_link(tmp_path):
    root = setup(tmp_path)
    build(root)
    text = (root / "core" / "index.md").read_text(encoding="utf-8")
    assert "(ch01-intro/p001-a.md)" in text and "(ch01-intro/p004-b.md)" in text
    assert "Alpha topic" in text and "C01-002" in text


def test_non_substantive_rows_listed_without_link(tmp_path):
    root = setup(tmp_path)
    build(root)
    text = (root / "core" / "index.md").read_text(encoding="utf-8")
    assert "P-010" in text and "administrative preface item" in text
    assert "p007-ack.md" not in text


def test_concepts_map_inverts_frontmatter(tmp_path):
    root = setup(tmp_path)
    build(root)
    text = (root / "core" / "concepts.md").read_text(encoding="utf-8")
    gamma = text.split("## gamma")[1].split("##")[0]
    assert "C01-001" in gamma and "C01-002" in gamma
    alpha = text.split("## alpha")[1].split("##")[0]
    assert "C01-002" not in alpha


def test_xref_lists_related_with_links(tmp_path):
    root = setup(tmp_path)
    build(root)
    text = (root / "core" / "xref.md").read_text(encoding="utf-8")
    assert "C01-001" in text and "[C01-002](ch01-intro/p004-b.md)" in text


def test_generated_files_have_no_broken_links(tmp_path):
    root = setup(tmp_path)
    build(root)
    assert links(root) == []


def test_build_is_idempotent(tmp_path):
    root = setup(tmp_path)
    build(root)
    first = {n: (root / "core" / n).read_text(encoding="utf-8") for n in ("index.md", "concepts.md", "xref.md")}
    build(root)
    assert first == {n: (root / "core" / n).read_text(encoding="utf-8") for n in first}
