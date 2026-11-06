import pytest

from helpers import make_row, make_skill
from matrix_update import update
from _common import load_matrix


def rows():
    return [make_row(id="C01-001", start_page=1, end_page=3),
            make_row(id="C01-002", start_page=4, end_page=6,
                     destination_file="core/ch01-intro/p004-b.md")]


def test_updates_only_named_rows(tmp_path):
    root = make_skill(tmp_path, rows())
    n = update(root, ["C01-001"], status="IMPLEMENTED")
    m = {r["id"]: r for r in load_matrix(root)}
    assert n == 1 and m["C01-001"]["status"] == "IMPLEMENTED" and m["C01-002"]["status"] == "NOT_STARTED"


def test_sets_verification_and_gaps(tmp_path):
    root = make_skill(tmp_path, rows())
    update(root, ["C01-002"], status="GAP", gaps="equation unreadable on PDF p. 5")
    r = {r["id"]: r for r in load_matrix(root)}["C01-002"]
    assert r["status"] == "GAP" and "equation" in r["gaps"]


def test_unknown_id_raises_and_changes_nothing(tmp_path):
    root = make_skill(tmp_path, rows())
    with pytest.raises(KeyError):
        update(root, ["C01-001", "NOPE"], status="VERIFIED", verification="v")
    assert load_matrix(root)[0]["status"] == "NOT_STARTED"


def test_invalid_status_rejected(tmp_path):
    root = make_skill(tmp_path, rows())
    with pytest.raises(ValueError):
        update(root, ["C01-001"], status="DONE")


def test_columns_preserved(tmp_path):
    root = make_skill(tmp_path, rows())
    update(root, ["C01-001"], status="IN_PROGRESS")
    assert list(load_matrix(root)[0].keys()) == list(make_row().keys())


def test_sets_tail_page(tmp_path):
    root = make_skill(tmp_path, rows())
    update(root, ["C01-002"], tail_page=7)
    assert {r["id"]: r for r in load_matrix(root)}["C01-002"]["tail_page"] == "7"
