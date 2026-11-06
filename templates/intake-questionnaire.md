# Intake questionnaire (fill from discovery first, ask only the blanks)

Mark each line: `known` (source file), `ask`, or `assume` (with the assumption stated).

## Both modes
- [ ] Objective and definition of success:
- [ ] Users, scale, traffic shape:
- [ ] Constraints (budget, latency, privacy/compliance, data residency, provider preferences):
- [ ] Environment and what may be touched (production is read-only):
- [ ] Audience and format of the output:

## Architect
- [ ] Use case and the cost of a wrong answer:
- [ ] Available data and its sensitivity:
- [ ] Existing systems to integrate:
- [ ] Team skills and timeline:
- [ ] Hosting (cloud, self-hosted, local):

## Review & Test
- [ ] Scope (whole system or component):
- [ ] How to run the project (commands, test suites, env):
- [ ] Dev/staging endpoint, logs, sample inputs, eval data:
- [ ] Permission for paid model calls, and the spend cap:
- [ ] Known issues and recent incidents:

See `workflows/architect/intake.md` for why each question matters and how to ask.
