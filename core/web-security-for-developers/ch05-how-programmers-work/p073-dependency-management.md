---
id: WS-C05-007
title: Dependency Management
source_pages: "73"
chapter: 5
concepts: [dependency-management, third-party-code, security-advisories, patching, out-of-cycle-patches, runtime-libraries]
related: [WS-C05-006, WS-C05-008, WS-C14-002]
time_sensitive: false
---
# Dependency Management
(Source: PDF p. 73. The text above the "Dependency Management" heading on this page is the end of WS-C05-006. The "Summary" heading lower on the page starts WS-C05-008.)

## What the section covers
Why a site's third-party software must be managed alongside the normal SDLC, and what diligence that requires (PDF p. 73).

## Meaning
- Modern web developers write only a small minority of the code that runs their site. A site typically relies on operating system code, a language runtime with its libraries, possibly a virtual machine, and a web server process running third-party libraries (PDF p. 73).
- All the third-party tools your code depends on are called dependencies, in other words the software that your software needs in order to run (PDF p. 73).

## Why it matters
- Experts write these dependencies, sparing you from writing your own memory management or low-level TCP handling. They also have strong reason to track security vulnerabilities and issue patches, and you should use what they provide (PDF p. 73).
- Using others' code demands diligence from you (PDF p. 73).

## When and how to apply
- A secure SDLC needs a process to review third-party libraries and decide when patches should be applied (PDF p. 73).
- This often has to happen outside the regular development cycle, because attackers will not wait for your next scheduled release before exploiting a vulnerability (PDF p. 73).
- Keeping ahead of security advisories and deploying patches for other people's code matters as much as securing your own team's code. Chapter 14 shows how to do this (PDF p. 73). See WS-C14-002.

## Relations
Sits beside the five phases (WS-C05-001) and leads into the chapter summary bullet on advisories in WS-C05-008.
