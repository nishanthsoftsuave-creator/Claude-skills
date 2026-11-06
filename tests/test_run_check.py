import json
import sys

from run_check import run_check

PY = sys.executable


def load(rec_path):
    return json.loads(rec_path.read_text(encoding="utf-8"))


def test_records_exit_code_and_output(tmp_path):
    r = run_check([PY, "-c", "print('hello'); raise SystemExit(0)"], tmp_path, "T1")
    assert r["status"] == "EXECUTED" and r["exit_code"] == 0
    rec = load(tmp_path / "T1.exec.json")
    assert rec["exit_code"] == 0 and "hello" in rec["stdout"]
    assert rec["command"][0] == PY and rec["started_at"] and rec["duration_s"] >= 0


def test_nonzero_exit_is_recorded_as_executed(tmp_path):
    r = run_check([PY, "-c", "import sys; sys.stderr.write('boom'); sys.exit(3)"], tmp_path, "T2")
    assert r["status"] == "EXECUTED" and r["exit_code"] == 3
    assert "boom" in load(tmp_path / "T2.exec.json")["stderr"]


def test_missing_command_recorded_as_blocked(tmp_path):
    r = run_check(["definitely-not-a-real-command-xyz"], tmp_path, "T3")
    assert r["status"] == "BLOCKED" and "not found" in r["reason"]
    assert load(tmp_path / "T3.exec.json")["status"] == "BLOCKED"


def test_timeout_recorded(tmp_path):
    r = run_check([PY, "-c", "import time; time.sleep(5)"], tmp_path, "T4", timeout=1)
    assert r["status"] == "EXECUTED" and r["timed_out"] is True


def test_secret_shapes_redacted_in_evidence(tmp_path):
    secret = "sk-" + "a" * 30
    run_check([PY, "-c", f"print('{secret}'); print('Authorization: Bearer abc.def.ghi')"], tmp_path, "T5")
    text = (tmp_path / "T5.exec.json").read_text(encoding="utf-8")
    assert secret not in text and "abc.def.ghi" not in text and "[REDACTED]" in text


def test_output_truncated(tmp_path):
    run_check([PY, "-c", "print('x' * 500000)"], tmp_path, "T6", max_chars=1000)
    rec = load(tmp_path / "T6.exec.json")
    assert len(rec["stdout"]) <= 1100 and rec["truncated"] is True


def test_cwd_option_runs_in_that_directory(tmp_path):
    work = tmp_path / "proj"
    work.mkdir()
    (work / "marker.txt").write_text("here", encoding="utf-8")
    r = run_check([PY, "-c", "import os; print(os.listdir('.'))"], tmp_path / "ev", "T7", cwd=work)
    assert "marker.txt" in r["stdout"] and r["cwd"] == str(work)


def test_cli_accepts_cwd(tmp_path):
    import subprocess
    work = tmp_path / "proj"
    work.mkdir()
    (work / "m.txt").write_text("x", encoding="utf-8")
    script = __import__("pathlib").Path(__file__).resolve().parent.parent / "scripts" / "run_check.py"
    out = subprocess.run([PY, str(script), "--case", "T8", "--evidence-dir", str(tmp_path / "ev"),
                          "--cwd", str(work), "--", PY, "-c", "import os; print(os.listdir('.'))"],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "m.txt" in (tmp_path / "ev" / "T8.exec.json").read_text(encoding="utf-8")
