---
id: WAS-C25-005
title: Potential Injection Targets
source_pages: "295"
chapter: 25
concepts: [generic-injection-defenses, injection-targets, cli-injection, high-risk-components, dependencies, secure-by-default]
related: [WAS-C25-004, WAS-C25-006, WAS-C13-002, WAS-C13-003]
time_sensitive: false
---
# Potential Injection Targets
(Source: PDF pp. 295-296)

## What the section covers
The start of the Generic Injection Defenses section, then a list of components to treat as likely injection targets. It starts partway down the page, after Database-Specific Defenses.

## Why it matters
SQL injection is not the only kind. As Part II showed, injection can hit any command-line utility or interpreter. The book urges looking for non-SQL targets and applying secure-by-default coding throughout the application, so an unexpected injection hole is less likely (PDF p. 295).

## Meaning
Part II used video or image compression CLIs as examples, but injection is not limited to tools like FFMPEG. It covers any script that takes text input and runs it through an interpreter or compares it with a list of commands (PDF p. 295).

## How it works
On the next page the book lists the usual high-risk targets: task schedulers, compression or optimization libraries, remote backup scripts, databases, loggers, any call to the host operating system, and any interpreter or compiler (PDF p. 296).

## When and how to apply
When ranking components for injection risk, compare them against this list; those are the starting points. Dependencies also count, because many bring sub-dependencies that fall into one of these categories (PDF p. 296).

## Relations
Extends the SQL-specific defenses (WAS-C25-004) to other interpreters; the attacks are in WAS-C13-002 and WAS-C13-003. Containing the damage is the topic of WAS-C25-006.
