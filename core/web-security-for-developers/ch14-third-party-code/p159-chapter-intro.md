---
id: WS-C14-001
title: "Chapter 14 Introduction: Third-Party Code"
source_pages: "159"
chapter: 14
concepts: [third-party-code, dependencies, known-vulnerabilities, security-patches, malvertising, third-party-services, chapter-roadmap]
related: [WS-C14-002, WS-C14-003, WS-C14-004, WS-C14-005, WS-C14-006, WS-C05-007]
time_sensitive: false
---
# Chapter 14 Introduction: Third-Party Code
(Source: PDF p. 159, tail PDF p. 160. The tail is the closing lines of the intro at the top of PDF p. 160, above the "Securing Dependencies" heading, which begins WS-C14-002.)

## What the section covers
The framing for the chapter: how much of a website is other people's code, why attackers target known flaws in it, and the three approaches the chapter teaches (PDF pp. 159-160).

## Why it matters
- Hardly anyone builds software from scratch. Most of the code running a website, from the operating system through the web server to programming language libraries, was written by others, which raises the question of how to manage vulnerabilities in other people's code (PDF p. 159).
- Hackers often target known vulnerabilities in popular components. It is far more efficient for an attacker to scan the web for insecure WordPress installations than to pick one site and work out how it might be vulnerable (PDF p. 159).
- The defence is to stay current with security patches so your site is not caught by a malicious scan (PDF p. 159).

## Chapter roadmap: three approaches
1. Dependencies: stay ahead of security advisories for the software components you use (WS-C14-002) (PDF p. 159).
2. Configuration: configure those dependencies correctly so they do not accidentally leave backdoors open to hackers (WS-C14-003) (PDF pp. 159-160).
3. Third-party services: code running on other people's servers that either your web server calls or your pages load through JavaScript imports. This includes malvertising, the alarmingly common tactic of delivering malware through ad networks, and ways to protect users if your site carries advertising (WS-C14-004 and WS-C14-005) (PDF p. 160).

## Relations
Dependency management practice is introduced in Chapter 5 (WS-C05-007). Chapter 12's point about advisories and patching (WS-C12-004) is the same theme. The chapter recap is WS-C14-006.
