from build_index import build
from helpers import make_row, make_skill
from run_all_checks import index_up_to_date, run_all


def module(rid="C01-001", pages="1-3"):
    body = " ".join(f"word{i}" for i in range(200))
    return (f'---\nid: {rid}\ntitle: Alpha\nsource_pages: "{pages}"\nchapter: 1\nconcepts: [alpha]\n'
            f'related: []\ntime_sensitive: false\n---\n# Alpha\n{body}\n')


def skill(tmp_path):
    rows = [make_row(id="C01-001", start_page=1, end_page=3, status="VERIFIED", verification="v",
                     destination_file="core/ch01-intro/p001-a.md", role="KNOWLEDGE_ONLY")]
    return make_skill(tmp_path, rows, {"core/ch01-intro/p001-a.md": module(), "workflows/architect/.keep": ""})


def test_stale_index_detected(tmp_path):
    root = skill(tmp_path)
    build(root)
    assert index_up_to_date(root) == []
    (root / "core" / "index.md").write_text("tampered", encoding="utf-8")
    assert any("index.md" in p for p in index_up_to_date(root))


def test_missing_index_detected(tmp_path):
    root = skill(tmp_path)
    assert any("index.md" in p for p in index_up_to_date(root))


def test_run_all_reports_per_check_and_overall(tmp_path):
    root = skill(tmp_path)
    build(root)
    results = run_all(root, stage="build", workflows=False)
    assert set(results) >= {"coverage_check", "link_check", "core_purity_check", "index_up_to_date"}
    assert all(v == [] for v in results.values())


def test_run_all_collects_problems(tmp_path):
    root = skill(tmp_path)
    build(root)
    (root / "core" / "ch01-intro" / "p001-a.md").write_text("tiny", encoding="utf-8")
    results = run_all(root, stage="build", workflows=False)
    assert results["coverage_check"]
