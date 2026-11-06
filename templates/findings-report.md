# Findings report: <project or component>

Run: <run id> · Date: <date> · Mode: Review & Test · Requested by: <who>

Keep this short when the result is simple. Every section below earns its place only if it has content.

## Summary

- Verdict in two sentences: what is solid, what is not.
- Counts: PASSED n · FAILED n · BLOCKED n · SKIPPED n · NOT_RUN n · REVIEWED n
- Findings: confirmed n · probable n · risk n · recommendation n · unverified n

## Scope and assumptions

- What was reviewed and tested; environment (dev/staging); spend cap if model calls were made.
- Assumptions made (each one, and which answer would change the result).
- Book modules used: `<module ids>` (these are the criteria behind the checks).

## Confirmed findings

Repeat per finding, ordered by severity.

### F<n>: <short title> (severity: critical | major | minor | trivial)

- **Affected component:** <file, endpoint, prompt, pipeline stage>
- **Impact:** <what goes wrong for users or the business>
- **Expected:** <what should happen, and the criterion it comes from, e.g. `C04-005`, PDF p. N>
- **Actual:** <what happened>
- **Steps to reproduce:**
  1. ...
- **Evidence:** `evidence/<file>` (<what it shows>); re-run result: <same | differs>
- **Likely cause:** <labelled as hypothesis unless proven>
- **Suggested fix and how to verify it:** ...

## Probable issues

Same fields, but state what evidence is missing to confirm each one.

## Risks and recommendations

One line each: the risk or suggestion, why it matters, the criterion behind it.

## Test status

| Case | Status | Criterion | Evidence |
|---|---|---|---|
| T1 | PASSED | C04-005 | evidence/T1.exec.json |

`REVIEWED` means code or configuration was read, not run. `BLOCKED` means the environment prevented the check; say why.

## Not tested, and why

List every case that is NOT_RUN, SKIPPED or BLOCKED with its reason and the manual step that would cover it. Do not leave this out.

## Unverified items

Claims or concerns that could not be confirmed, and what would confirm them.

## Next steps

Ordered by impact. Offer follow-up actions (tickets, a redesign through Architect mode) without performing them.
