"""Report gate for Review & Test runs: validates <run_dir>/results.json against evidence rules.

check(run_dir) -> list[str]  (empty = the report may be generated)
It verifies structure and evidence presence. It cannot prove that a finding is correct; the
re-run, independent re-read and honest labelling in the workflow cover that.
"""
import json
import sys
from pathlib import Path

CASE_STATUSES = {"PASSED", "FAILED", "BLOCKED", "SKIPPED", "NOT_RUN", "REVIEWED"}
LABELS = {"confirmed", "probable", "risk", "recommendation", "unverified"}
SEVERITIES = {"critical", "major", "minor", "trivial"}
NEEDS_REASON = {"BLOCKED", "SKIPPED", "NOT_RUN"}
CONFIRMABLE_BASES = {"deterministic", "static", "manual"}


def _long(p):
    """On Windows, prefix absolute paths so ones over 260 characters can still be opened."""
    s = str(p)
    if sys.platform == "win32" and not s.startswith("\\\\?\\") and len(s) > 240:
        return Path("\\\\?\\" + s)
    return p


def _resolve(run_dir, rel, problems, ctx):
    """Return the Path for an evidence reference if it is inside run_dir and non-empty."""
    p = (run_dir / rel).resolve()
    if run_dir.resolve() not in p.parents and p != run_dir.resolve():
        problems.append(f"{ctx}: evidence path {rel} is outside the run directory")
        return None
    p = _long(p)
    if not p.exists():
        problems.append(f"{ctx}: evidence file {rel} does not exist")
        return None
    if p.stat().st_size == 0:
        problems.append(f"{ctx}: evidence file {rel} is empty")
        return None
    return p


def _check_case(run_dir, c, problems):
    cid = c.get("id", "?")
    ctx = f"case {cid}"
    status = c.get("status")
    if status not in CASE_STATUSES:
        problems.append(f"{ctx}: invalid status {status!r}")
        return
    if not c.get("criteria_refs") and not c.get("supplementary"):
        problems.append(f"{ctx}: criteria_refs is empty (cite a matrix row id or mark supplementary)")
    if status in NEEDS_REASON and not str(c.get("reason", "")).strip():
        problems.append(f"{ctx}: {status} needs a reason")
    if status == "REVIEWED" and not c.get("evidence"):
        problems.append(f"{ctx}: REVIEWED needs evidence (the notes of what was read)")
    for ev in c.get("evidence") or []:
        _resolve(run_dir, ev, problems, ctx)
    if status in ("PASSED", "FAILED") or c.get("exec_record"):
        rec_ref = c.get("exec_record")
        if status == "PASSED" and not rec_ref:
            problems.append(f"{ctx}: PASSED needs an exec_record from run_check.py (use REVIEWED for static review)")
        elif rec_ref:
            p = _resolve(run_dir, rec_ref, problems, ctx)
            if p:
                try:
                    rec = json.loads(p.read_text(encoding="utf-8"))
                except ValueError:
                    problems.append(f"{ctx}: exec_record {rec_ref} is not valid JSON")
                    return
                if status == "PASSED":
                    if rec.get("status") != "EXECUTED":
                        problems.append(f"{ctx}: PASSED but the record shows the command was not executed")
                    elif rec.get("exit_code") != 0:
                        problems.append(f"{ctx}: PASSED but exit_code is {rec.get('exit_code')}")
                    elif not rec.get("started_at"):
                        problems.append(f"{ctx}: PASSED but the record has no started_at")
    if status == "FAILED":
        if not c.get("evidence") and not c.get("exec_record"):
            problems.append(f"{ctx}: FAILED needs evidence")
        if not c.get("rerun"):
            problems.append(f"{ctx}: FAILED needs a rerun note (same / differs / not_possible)")


def _check_finding(run_dir, f, cases, problems):
    fid = f.get("id", "?")
    ctx = f"finding {fid}"
    label = f.get("label")
    if label not in LABELS:
        problems.append(f"{ctx}: invalid label {label!r}")
        return
    for cid in f.get("case_ids") or []:
        if cid not in cases:
            problems.append(f"{ctx}: references unknown case {cid}")
        elif label == "confirmed" and cases[cid].get("status") != "FAILED":
            problems.append(f"{ctx}: confirmed finding must be backed by a FAILED case, {cid} is {cases[cid].get('status')}")
    if label in ("confirmed", "probable"):
        if not f.get("evidence"):
            problems.append(f"{ctx}: {label} finding needs evidence")
        for ev in f.get("evidence") or []:
            _resolve(run_dir, ev, problems, ctx)
        if f.get("severity") not in SEVERITIES:
            problems.append(f"{ctx}: severity must be one of {sorted(SEVERITIES)}")
    if label == "confirmed":
        if not f.get("case_ids"):
            problems.append(f"{ctx}: confirmed finding needs case_ids")
        if f.get("basis") == "judge":
            problems.append(f"{ctx}: a finding based only on a judge model cannot be confirmed (cap at probable)")
        elif f.get("basis") not in CONFIRMABLE_BASES:
            problems.append(f"{ctx}: basis must be one of {sorted(CONFIRMABLE_BASES)} for a confirmed finding")
        for cid in f.get("case_ids") or []:
            if cid in cases and cases[cid].get("status") == "FAILED" and cases[cid].get("rerun") != "same":
                problems.append(f"{ctx}: confirmed finding needs the failure to reproduce on re-run, "
                                f"but case {cid} re-run is {cases[cid].get('rerun')!r}")
        if not f.get("repro_steps"):
            problems.append(f"{ctx}: confirmed finding needs repro_steps")
        if not str(f.get("impact") or "").strip():
            problems.append(f"{ctx}: confirmed finding needs impact")


def check(run_dir):
    run_dir = Path(run_dir)
    f = run_dir / "results.json"
    if not f.exists():
        return [f"results.json not found in {run_dir}"]
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except ValueError as e:
        return [f"results.json is not valid JSON: {e}"]
    problems = []
    cases = {c.get("id"): c for c in data.get("cases", [])}
    for c in data.get("cases", []):
        _check_case(run_dir, c, problems)
    findings = data.get("findings", [])
    for fd in findings:
        _check_finding(run_dir, fd, cases, problems)
    covered = {cid for fd in findings for cid in fd.get("case_ids") or []}
    for cid, c in cases.items():
        if c.get("status") == "FAILED" and cid not in covered:
            problems.append(f"case {cid}: FAILED but no finding references it")
    if "summary" in data:
        actual = {}
        for c in data.get("cases", []):
            actual[c.get("status")] = actual.get(c.get("status"), 0) + 1
        claimed = {k: v for k, v in data["summary"].items() if v}
        if claimed != actual:
            problems.append(f"summary {claimed} does not match case counts {actual}")
    return problems


def main(argv):
    if len(argv) != 1:
        sys.exit("usage: validate_report.py <run_dir>")
    problems = check(argv[0])
    for p in problems:
        print(p)
    print(f"validate_report: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
