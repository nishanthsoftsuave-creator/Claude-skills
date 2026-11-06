import pytest

from run_state import STEPS, GateError, RunState, load


def advance_to(rs, step):
    for s in STEPS:
        if s == step:
            return
        rs.advance(s, gate_met=True, note="ok")


def test_steps_order():
    assert STEPS == ["classify", "discover", "intake", "route", "plan_approval",
                     "execute", "verify", "report", "handoff"]


def test_cannot_advance_without_gate(tmp_path):
    rs = load(tmp_path)
    with pytest.raises(GateError):
        rs.advance("classify", gate_met=False)
    assert rs.last_completed() is None


def test_cannot_skip_steps(tmp_path):
    rs = load(tmp_path)
    with pytest.raises(GateError, match="expected 'classify'"):
        rs.advance("execute", gate_met=True, note="x")


def test_plan_approval_requires_the_users_words(tmp_path):
    rs = load(tmp_path)
    advance_to(rs, "plan_approval")
    with pytest.raises(GateError, match="approval"):
        rs.advance("plan_approval", gate_met=True, note="")
    rs.advance("plan_approval", gate_met=True, note="user: yes, go ahead")
    assert rs.last_completed() == "plan_approval"


def test_resume_returns_last_completed_step_and_next(tmp_path):
    rs = load(tmp_path)
    rs.enable_persistence()
    rs.advance("classify", gate_met=True, note="architect")
    rs.advance("discover", gate_met=True, note="summary shown")
    rs2 = load(tmp_path)
    assert rs2.last_completed() == "discover"
    assert rs2.next_step() == "intake"


def test_nothing_written_before_persistence_enabled(tmp_path):
    rs = load(tmp_path)
    rs.advance("classify", gate_met=True, note="x")
    rs.set_answer("goal", "chatbot")
    assert not (tmp_path / ".ai-architecture-and-reviewer").exists()


def test_enable_persistence_flushes_earlier_state(tmp_path):
    rs = load(tmp_path)
    rs.advance("classify", gate_met=True, note="x")
    rs.set_answer("goal", "chatbot")
    rs.add_assumption("staging has no PII")
    rs.enable_persistence()
    again = load(tmp_path)
    assert again.answers["goal"] == "chatbot"
    assert again.assumptions == ["staging has no PII"]
    assert (tmp_path / ".ai-architecture-and-reviewer" / "run-state.md").exists()


def test_cannot_advance_past_last_step(tmp_path):
    rs = load(tmp_path)
    advance_to(rs, "zzz")  # completes all steps
    with pytest.raises(GateError):
        rs.advance("handoff", gate_met=True, note="again")
