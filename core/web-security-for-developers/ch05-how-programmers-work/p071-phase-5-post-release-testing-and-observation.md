---
id: WS-C05-006
title: Phase 5 - Post-Release Testing and Observation
source_pages: "71-72"
chapter: 5
concepts: [post-release-testing, smoke-testing, penetration-testing, logging, monitoring, error-reporting, observability, sensitive-data-in-logs, log-scraping]
related: [WS-C05-005, WS-C05-007, WS-C05-008]
time_sensitive: true
---
# Phase 5 - Post-Release Testing and Observation
(Source: PDF pp. 71-72, tail PDF p. 73. The row starts part-way down PDF p. 71 at the "Phase 5" heading; the database migration text above it is WS-C05-005. On the tail page, content above the "Dependency Management" heading belongs here, and that section is WS-C05-007.)

## What the section covers
The fifth SDLC phase: checking a deployment after release, penetration testing, and the three runtime observation practices of logging, monitoring and error reporting (PDF pp. 71-73).

## Meaning and how it works
### Post-release (smoke) testing
- After deployment, test that you released correctly and that your assumptions about production behaviour hold. This post-release testing, often called smoke testing, can in theory be fairly cursory given a good test environment and a reliable release process (PDF p. 71).
- Still, trust your instincts and be risk-averse about how much to test at each SDLC stage. A saying captures the right attitude: continue testing until fear turns into boredom (PDF p. 71).

### Penetration testing
- Penetration testing probes a website from outside for security vulnerabilities. It is typically done by security professionals and ethical hackers, and is useful both before and after release (PDF p. 72).
- Teams can also use sophisticated automated tools that analyse URLs and try to craft malicious HTTP requests to find common vulnerabilities (PDF p. 72).
- It can be costly and slow but is far cheaper than being hacked, so the book urges adding it to your testing procedures (PDF p. 72).

### Monitoring, logging and error reporting
After release the production environment must be observable at runtime, so administrators can spot unusual, possibly malicious behaviour and diagnose problems as they happen. This takes three activities (PDF p. 72).
- Logging: code writes to a log file as the application acts, showing what the server is doing at any moment. Log every HTTP request with timestamp, URL and response code, plus significant user actions (such as authentication and password-reset requests) and site actions (such as sending email and calling APIs) (PDF p. 72).
- Logs should be available to administrators at runtime, via command line or web console, and archived for later reading in case of postmortems. Add log statements to help diagnose problems, but never write sensitive data such as passwords or credit card details into logs, in case an attacker gets access (PDF p. 72).
- Monitoring: measure response times and other metrics at runtime. Watching the web server and database lets administrators spot high load or degraded performance through alerts when network speeds drop or queries run long. Feed HTTP and database response times into monitoring software that raises alerts past set thresholds. Many cloud platforms include monitoring, so configure error conditions and alerting properly (PDF p. 72).
- Error reporting: capture and record unexpected errors in the code. Error conditions can be extracted from logs or captured in code, then collated in a datastore available to administrators. Many intrusions exploit badly handled errors, so pay attention to unexpected errors when they occur (PDF p. 72).
- Services such as Rollbar and Airbrake offer plug-ins that collect errors with a few lines of code, a good option if you lack time or inclination to build your own. Log-scraping tools such as Splunk can instead pick errors out of log files and make sense of them (PDF pp. 72-73).

## Time-sensitive statements
Named tools: Rollbar, Airbrake, Splunk.

## Relations
Follows the release process (WS-C05-005). Dependency handling that runs alongside the lifecycle is WS-C05-007. The chapter summary restates these points (WS-C05-008).
