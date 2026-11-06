---
id: WAS-C17-003
title: Comprehensive Code Reviews
source_pages: "220"
chapter: 17
concepts: [code-review, commit-review, conflict-of-interest, independent-reviewer, data-transmission, data-storage, review-checklist]
related: [WAS-C17-002, WAS-C17-004, WAS-C19-001]
time_sensitive: false
---
# Comprehensive Code Reviews
(Source: PDF p. 220, continuing onto the next page above the Vulnerability Discovery heading)

## What the section covers
The second defensive step: once the architecture has been judged secure and the application is being written, every commit is evaluated before it enters the codebase, with security as part of that evaluation.

## Meaning and context
- The step applies to an application whose architecture was already evaluated as secure (PDF p. 220).
- Most companies already require code reviews for quality assurance, to reduce technical debt and to remove easy-to-find programming mistakes. The security review builds on that existing habit.

## Why it matters and how it is run (continues on the next page)
The text on the following page states that code review is also where released code is checked against security standards. To limit conflict of interest, commits should be reviewed not only by the committer's own team but also by an unrelated team, particularly on the security side.

The author says catching security holes per commit is easier than people expect, and gives four questions that reviewers can start from:
- How is data transmitted from one point to another, typically over a network and in a specific format?
- How is data stored?
- When data reaches the client, how is it shown to the user?
- When data reaches the server, what operations run on it and how is it persisted?

The author notes that later chapters give much more specific measures and that this list is a basis anyone can use to start reviewing for security. These points are printed on the next page, so they carry no page cite here.

## When and how to apply
INTERPRETATION: add the four data questions as a standing checklist in the code review template, and route security-sensitive commits to a reviewer outside the author's team.

## Relations
Follows architecture review (WAS-C17-002) and is followed by discovery of vulnerabilities that slip through (WAS-C17-004). The full treatment is the chapter on reviewing code for security (WAS-C19-001).
