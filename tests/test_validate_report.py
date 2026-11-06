import json

from validate_report import check


def write(run_dir, results, files=None):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "results.json").write_text(json.dumps(results), encoding="utf-8")
    for rel, content in (files or {}).items():
        p = run_dir / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return run_dir


def case(**kw):
    c = {"id": "T1", "title": "t", "status": "PASSED", "criteria_refs": ["C04-005"],
         "evidence": ["evidence/T1.exec.json"], "exec_record": "evidence/T1.exec.json"}
    c.update(kw)
    return c


EXEC_OK = json.dumps({"status": "EXECUTED", "exit_code": 0, "started_at": "2026-10-24T10:00:00"})
FILES = {"evidence/T1.exec.json": EXEC_OK, "evidence/shot.txt": "evidence"}


def has(problems, text):
    return any(text in p for p in problems)


def results(cases, findings=None, **kw):
    return {"run_id": "r", "mode": "review-test", "cases": cases, "findings": findings or [], **kw}


def finding(**kw):
    f = {"id": "F1", "case_ids": ["T2"], "label": "confirmed", "severity": "major",
         "title": "x", "impact": "users see wrong answers", "repro_steps": ["do a", "do b"],
         "evidence": ["evidence/shot.txt"], "basis": "deterministic"}
    f.update(kw)
    return f


def failed_case(**kw):
    base = dict(id="T2", status="FAILED", exec_record="evidence/T1.exec.json",
                evidence=["evidence/shot.txt"], rerun="same")
    base.update(kw)
    return case(**base)


def test_valid_report_passes(tmp_path):
    d = write(tmp_path / "run", results([case(), failed_case()], [finding()]), FILES)
    assert check(d) == []


def test_missing_results_file(tmp_path):
    assert has(check(tmp_path), "results.json")


def test_passed_case_lacking_executed_record_rejected(tmp_path):
    d = write(tmp_path / "run", results([case(exec_record=None)]), FILES)
    assert has(check(d), "PASSED")


def test_passed_with_nonzero_exit_rejected(tmp_path):
    files = {**FILES, "evidence/T1.exec.json": json.dumps({"status": "EXECUTED", "exit_code": 1, "started_at": "t"})}
    assert has(check(write(tmp_path / "run", results([case()]), files)), "exit_code")


def test_passed_from_blocked_record_rejected(tmp_path):
    files = {**FILES, "evidence/T1.exec.json": json.dumps({"status": "BLOCKED", "reason": "no cmd"})}
    assert has(check(write(tmp_path / "run", results([case()]), files)), "executed")


def test_static_review_must_use_reviewed_status(tmp_path):
    c = case(status="REVIEWED", exec_record=None, evidence=["evidence/shot.txt"])
    assert check(write(tmp_path / "run", results([c]), FILES)) == []


def test_failed_finding_without_evidence_file_rejected(tmp_path):
    bad = failed_case(evidence=["evidence/missing.txt"])
    d = write(tmp_path / "run", results([bad], [finding()]), FILES)
    assert has(check(d), "missing.txt")


def test_empty_evidence_file_rejected(tmp_path):
    files = {**FILES, "evidence/empty.txt": ""}
    d = write(tmp_path / "run", results([failed_case(evidence=["evidence/empty.txt"])], [finding()]), files)
    assert has(check(d), "empty")


def test_failed_case_requires_rerun_note(tmp_path):
    c = failed_case()
    del c["rerun"]
    assert has(check(write(tmp_path / "run", results([c], [finding()]), FILES)), "rerun")


def test_blocked_skipped_not_run_require_reason(tmp_path):
    cs = [case(id=f"B{i}", status=s, exec_record=None, evidence=[]) for i, s in
          enumerate(["BLOCKED", "SKIPPED", "NOT_RUN"])]
    assert len([p for p in check(write(tmp_path / "run", results(cs), FILES)) if "reason" in p]) == 3


def test_case_requires_book_criteria_or_supplementary_flag(tmp_path):
    c = case(criteria_refs=[])
    assert has(check(write(tmp_path / "run", results([c]), FILES)), "criteria_refs")
    ok = case(criteria_refs=[], supplementary=True)
    assert check(write(tmp_path / "run2", results([ok]), FILES)) == []


def test_invalid_status_rejected(tmp_path):
    assert has(check(write(tmp_path / "run", results([case(status="OK")]), FILES)), "status")


def test_judge_only_finding_cannot_be_confirmed(tmp_path):
    d = write(tmp_path / "run", results([failed_case()], [finding(basis="judge")]), FILES)
    assert has(check(d), "judge")


def test_confirmed_finding_needs_repro_impact_and_severity(tmp_path):
    f = finding(repro_steps=[], impact="", severity=None)
    p = check(write(tmp_path / "run", results([failed_case()], [f]), FILES))
    assert has(p, "repro_steps") and has(p, "impact") and has(p, "severity")


def test_probable_finding_may_lack_repro_but_needs_evidence(tmp_path):
    f = finding(label="probable", repro_steps=[], evidence=[])
    assert has(check(write(tmp_path / "run", results([failed_case()], [f]), FILES)), "evidence")


def test_unverified_and_risk_findings_allowed_without_evidence(tmp_path):
    fs = [finding(id="F1", case_ids=["T1"], label="unverified", evidence=[], repro_steps=[], severity=None, impact=""),
          finding(id="F2", case_ids=["T1"], label="risk", evidence=[], repro_steps=[], severity=None, impact="")]
    assert check(write(tmp_path / "run", results([case()], fs), FILES)) == []


def test_finding_must_reference_existing_failed_case_when_confirmed(tmp_path):
    f = finding(case_ids=["NOPE"])
    assert has(check(write(tmp_path / "run", results([failed_case()], [f]), FILES)), "NOPE")
    g = finding(case_ids=["T1"])  # T1 PASSED
    assert has(check(write(tmp_path / "run2", results([case(), failed_case()], [g]), FILES)), "FAILED")


def test_every_failed_case_must_be_covered_by_a_finding(tmp_path):
    d = write(tmp_path / "run", results([failed_case()], []), FILES)
    assert has(check(d), "T2")


def test_report_counts_match_run_state(tmp_path):
    cs = [case(), failed_case()]
    bad = results(cs, [finding()], summary={"PASSED": 5, "FAILED": 1})
    assert has(check(write(tmp_path / "run", bad, FILES)), "summary")
    good = results(cs, [finding()], summary={"PASSED": 1, "FAILED": 1})
    assert check(write(tmp_path / "run2", good, FILES)) == []


def test_path_escape_rejected(tmp_path):
    c = failed_case(evidence=["../outside.txt"])
    (tmp_path / "outside.txt").write_text("x", encoding="utf-8")
    assert has(check(write(tmp_path / "run", results([c], [finding()]), FILES)), "outside")


def test_confirmed_finding_requires_case_ids(tmp_path):
    f = finding(case_ids=[])
    assert has(check(write(tmp_path / "run", results([failed_case()], [f]), FILES)), "case_ids")


def test_confirmed_finding_requires_a_known_basis(tmp_path):
    for i, basis in enumerate([None, "", "vibes"]):
        f = finding(basis=basis)
        assert has(check(write(tmp_path / f"run{i}", results([failed_case()], [f]), FILES)), "basis"), basis
    for i, basis in enumerate(["deterministic", "static", "manual"]):
        f = finding(basis=basis)
        assert not has(check(write(tmp_path / f"ok{i}", results([failed_case()], [f]), FILES)), "basis"), basis


def test_confirmed_finding_requires_the_failure_to_reproduce_on_rerun(tmp_path):
    differs = failed_case(rerun="differs")
    assert has(check(write(tmp_path / "run", results([differs], [finding()]), FILES)), "re-run")
    # a probable finding may rest on a failure that did not reproduce
    ok = check(write(tmp_path / "run2", results([differs], [finding(label="probable")]), FILES))
    assert not has(ok, "re-run")


def test_reviewed_case_requires_evidence(tmp_path):
    c = case(status="REVIEWED", exec_record=None, evidence=[])
    assert has(check(write(tmp_path / "run", results([c]), FILES)), "REVIEWED")
