---
id: A10-001
title: API10:2019 Insufficient Logging & Monitoring
source_pages: "26-27"
chapter: api10
concepts: [insufficient-logging, monitoring, siem, alerting, log-integrity, log-injection, incident-response, breach-detection-time, audit-trail]
related: [A00-006, A00-007, A02-001, A09-001]
time_sensitive: false
---
# API10:2019 Insufficient Logging & Monitoring
(Source: PDF pp. 26-27)

## What the section covers
The risk that attacks go unnoticed or cannot be investigated because the API produces too little log data, nobody watches it, or incident response is not wired in. The chapter gives the risk scores, four conditions that make an API vulnerable, two scenarios and a prevention list.

## Risk scores
Exploitability 2, prevalence 3, detectability 1, technical impact 2; business impact is business-specific (PDF p. 26). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: attackers rely on the lack of logging and monitoring to abuse systems without being noticed (PDF p. 26).
- Security weakness: with no or insufficient logging and monitoring it is almost impossible to track suspicious activity and respond in time (PDF p. 26).
- Impacts: with no visibility into ongoing malicious activity, attackers have plenty of time to compromise systems fully (PDF p. 26). The overview table adds that breach studies put the time to detect a breach at over 200 days, usually by outside parties rather than internal monitoring (see A00-007).

## Is the API vulnerable?
The API is vulnerable if (PDF p. 26):
- it produces no logs, the log level is set wrongly, or log messages lack enough detail;
- log integrity is not guaranteed, for example through log injection;
- logs are not monitored continuously;
- the API infrastructure is not monitored continuously.

## How it works: the attack scenarios
1. **Leaked admin keys, slow reaction.** Access keys for an administrative API were leaked in a public repository. The repository owner was emailed about the possible leak but took more than 48 hours to act. The keys may have exposed sensitive data, and because logging was insufficient the company could not tell what data the malicious actors had touched (PDF p. 26).
2. **Credential stuffing with no alert.** A video-sharing platform suffered a large-scale credential-stuffing attack. Failed logins were logged, but no alert fired while the attack ran. Only after user complaints were the API logs analysed and the attack found. The company had to announce the incident publicly, ask users to reset passwords and report to regulators (PDF p. 26).

## How to prevent
The document's list (PDF p. 27):
- Log all failed authentication attempts, denied accesses and input validation errors.
- Write logs in a format a log-management solution can consume, with enough detail to identify the malicious actor.
- Treat logs as sensitive data and guarantee their integrity at rest and in transit.
- Configure monitoring to watch the infrastructure, the network and the API's behaviour continuously.
- Use a Security Information and Event Management (SIEM) system to aggregate and manage logs from every component of the API stack and the hosts.
- Set up custom dashboards and alerts so suspicious activity is detected and handled earlier.

## When and how to apply
INTERPRETATION: a review should trigger a handful of known-bad events on a non-production copy (failed logins, a denied request, an invalid input) and then trace each one: is it logged, with which fields, who is alerted, and how fast. Scenario 2 shows that logging without alerting does not satisfy this risk. The document gives no numeric detection-time target, so the project sets one.

## References the section lists
OWASP: the Logging Cheat Sheet, the Proactive Controls item on logging and intrusion detection, and the Application Security Verification Standard chapter V7 on error handling and logging. External: CWE-223 Omission of Security-relevant Information and CWE-778 Insufficient Logging (PDF p. 27).

## Relations
A02-001 lists the authentication abuse whose failures should be logged and alerted on; A07-001 and A09-001 describe exposures that monitoring would help surface; A00-007 holds the one-line summary.
