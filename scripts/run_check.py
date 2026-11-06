"""Run a command and record it as evidence, so "executed" is a harness record, not a claim.

Usage: python run_check.py --case T1 --evidence-dir DIR [--timeout 120] [--cwd DIR] -- <command> [args...]
Writes DIR/<case>.exec.json with the command, exit code, timing and redacted output.
A command that cannot be started is recorded as BLOCKED (never as a failure of the project).
"""
import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REDACT = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bghp_[A-Za-z0-9]{30,}"),
    re.compile(r"(?i)(authorization:\s*bearer\s+)\S+"),
    re.compile(r"(?i)(api[_-]?key\s*[=:]\s*)\S+"),
]


def redact(text):
    for pat in REDACT:
        text = pat.sub(lambda m: (m.group(1) if m.groups() else "") + "[REDACTED]", text)
    return text


def _clip(text, max_chars):
    if len(text) > max_chars:
        return text[:max_chars], True
    return text, False


def run_check(cmd, evidence_dir, case_id, timeout=120, max_chars=200_000, cwd=None):
    evidence_dir = Path(evidence_dir)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    rec = {"case": case_id, "command": [redact(str(c)) for c in cmd], "cwd": str(cwd) if cwd else None,
           "started_at": datetime.now().isoformat(timespec="seconds")}
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd,
                           encoding="utf-8", errors="replace")
        out, err, code, timed_out = p.stdout, p.stderr, p.returncode, False
        rec["status"] = "EXECUTED"
    except FileNotFoundError:
        rec.update(status="BLOCKED", reason=f"command not found: {cmd[0]}")
        out = err = ""
        code, timed_out = None, False
    except subprocess.TimeoutExpired as e:
        rec["status"] = "EXECUTED"
        out = e.stdout.decode("utf-8", "replace") if isinstance(e.stdout, bytes) else (e.stdout or "")
        err = e.stderr.decode("utf-8", "replace") if isinstance(e.stderr, bytes) else (e.stderr or "")
        code, timed_out = None, True
    rec["duration_s"] = round(time.time() - t0, 3)
    out, t1 = _clip(redact(out), max_chars)
    err, t2 = _clip(redact(err), max_chars)
    rec.update(exit_code=code, timed_out=timed_out, stdout=out, stderr=err, truncated=t1 or t2)
    (evidence_dir / f"{case_id}.exec.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    return rec


def main(argv):
    if "--" not in argv:
        sys.exit("usage: run_check.py --case ID --evidence-dir DIR [--timeout S] -- command [args...]")
    i = argv.index("--")
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--evidence-dir", required=True)
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--cwd", default=None, help="directory to run the command in (default: current directory)")
    a = ap.parse_args(argv[:i])
    rec = run_check(argv[i + 1:], a.evidence_dir, a.case, timeout=a.timeout, cwd=a.cwd)
    print(json.dumps({k: rec[k] for k in ("case", "status", "exit_code", "timed_out") if k in rec}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
