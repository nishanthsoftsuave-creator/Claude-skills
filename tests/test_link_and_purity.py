from core_purity_check import check as purity
from helpers import make_skill
from link_check import check as links


def test_valid_relative_link_ok(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "see [b](b.md)", "core/b.md": "x"})
    assert links(root) == []


def test_broken_xref_link_flagged(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "see [b](missing.md)"})
    p = links(root)
    assert len(p) == 1 and "missing.md" in p[0]


def test_external_anchor_and_mailto_links_ignored(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "[x](https://e.com) [y](#sec) [z](mailto:a@b.c)"})
    assert links(root) == []


def test_link_with_anchor_checks_file_part(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "[b](b.md#top)", "core/b.md": "x"})
    assert links(root) == []


def test_links_inside_code_blocks_ignored(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "```\n[b](nope.md)\n```"})
    assert links(root) == []


def test_core_file_containing_windows_user_path_flagged(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": r"open C:\Users\someone\repo\x.py"})
    assert any("a.md" in p for p in purity(root))


def test_email_and_key_shapes_flagged(tmp_path):
    root = make_skill(tmp_path, [], {"workflows/w.md": "mail me@corp.com", "templates/t.md": "sk-" + "a" * 30})
    assert len(purity(root)) == 2


def test_clean_file_ok(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "Perplexity is the exponential of cross entropy."})
    assert purity(root) == []


def test_evals_and_tests_dirs_excluded(tmp_path):
    root = make_skill(tmp_path, [], {"evals/fixtures/app/x.md": r"C:\Users\someone\x", "tests/t.md": "me@corp.com"})
    assert purity(root) == []


def test_custom_patterns_file_used(tmp_path):
    root = make_skill(tmp_path, [], {"core/a.md": "Acme Corp internal", "scripts/purity-patterns.txt": "# c\nAcme Corp\n"})
    assert purity(root) != []
