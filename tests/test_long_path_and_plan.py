import sys

import pytest

from run_state import STEPS, load
from validate_report import _resolve


def test_plan_text_is_stored_with_the_approval(tmp_path):
    rs = load(tmp_path)
    for s in STEPS:
        if s == "plan_approval":
            rs.advance(s, True, note="go ahead", plan="1. run tests 2. read prompts")
            break
        rs.advance(s, True, note="ok")
    entry = [c for c in rs.completed if c["step"] == "plan_approval"][0]
    assert entry["plan"] == "1. run tests 2. read prompts"


@pytest.mark.skipif(sys.platform != "win32", reason="the 260-character limit is a Windows rule")
def test_evidence_in_a_path_over_260_characters_is_found(tmp_path):
    long_dir = tmp_path
    for i in range(6):
        long_dir = long_dir / ("segment-" + "x" * 45 + str(i))
    ev_dir = "\\\\?\\" + str(long_dir)
    import os
    os.makedirs(ev_dir)
    with open(ev_dir + "\\evidence.txt", "w", encoding="utf-8") as f:
        f.write("proof")
    problems = []
    p = _resolve(long_dir, "evidence.txt", problems, "case T1")
    assert len(str(long_dir)) > 260
    assert problems == []
    assert p is not None
