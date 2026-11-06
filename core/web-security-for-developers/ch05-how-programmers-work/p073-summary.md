---
id: WS-C05-008
title: Chapter 5 Summary
source_pages: "73-74"
chapter: 5
concepts: [chapter-summary, sdlc, issue-tracking, source-control, test-environment, release-process, continuous-integration, penetration-testing, security-advisories, injection-preview]
related: [WS-C05-002, WS-C05-003, WS-C05-004, WS-C05-005, WS-C05-006, WS-C05-007, WS-C06-001]
time_sensitive: false
---
# Chapter 5 Summary
(Source: PDF pp. 73-74. The row starts part-way down PDF p. 73 at the "Summary" heading; the dependency management text above it is WS-C05-007.)

## What the section covers
The chapter's closing recap of a well-structured software development life cycle and a preview of the next chapter (PDF pp. 73-74).

## Recap
The chapter's claim is that a well-structured SDLC lets you avoid bugs and software vulnerabilities (PDF p. 73). Its bullet points:
- Document design goals with issue-tracking software (PDF p. 73). Recaps WS-C05-002.
- Keep code in source control so older versions are available for inspection and code reviews are easy to organise (PDF p. 73). Recaps WS-C05-003.
- Before release, test in a dedicated, isolated test environment that resembles production and handles your data with the utmost care (PDF p. 73). Recaps WS-C05-004.
- Use a reliable, reproducible and revertible release process. If the build is scripted and produces deployable assets, run it regularly together with unit tests in a continuous integration environment so potential problems show up early in the life cycle (PDF p. 73). Recaps WS-C05-005 and the continuous integration material in WS-C05-004.
- After release, use penetration testing to find site vulnerabilities before a hacker can use them, and use monitoring, logging and error reporting to detect and diagnose problems on the running site (PDF p. 74). Recaps WS-C05-006.
- Stay ahead of security advisories for third-party code, since you may need to deploy patches outside the normal release cycle (PDF p. 74). Recaps WS-C05-007.

## Looking ahead
The next chapter finally turns to specific software vulnerabilities and defences, starting with one of the biggest threats websites face: malicious input designed to inject code into your web server (PDF p. 74). See WS-C06-001.
