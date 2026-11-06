---
id: WAS-C25-001
title: Defending Against Injection - Chapter and SQL Injection Lead-in
source_pages: "291"
chapter: 25
concepts: [injection-defense, sql-injection-mitigation, interpreters, command-injection, defense-categories, detection]
related: [WAS-C13-001, WAS-C25-002, WAS-C25-003, WAS-C25-005]
time_sensitive: false
---
# Defending Against Injection: chapter introduction and the SQL injection lead-in
(Source: PDF p. 291)

## What the section covers
The chapter opening and the short lead-in to "Mitigating SQL Injection". No separate intro row exists, so both sit in this module.

## Chapter framing
Injection-style attacks are still around, though more common in the past. They typically stem from a developer's inattention when writing automation that mixes a command-line interface with user-submitted data. The surface is wide: injection can target CLIs or any other isolated interpreter on the server, and once it reaches the operating-system level it becomes command injection (PDF p. 291).

The book therefore splits defenses into categories (PDF p. 291):
1. Defenses against SQL injection, the most common and best-known form.
2. A check of which of those defenses carry over to other forms of injection.
3. A few generic defenses that are not tied to any one kind of injection attack.

## Why SQL injection is a good starting point
It is the most common injection attack and also one of the easiest to defend against. Because it is so widespread, and nearly every complex web application uses an SQL database, many mitigations and countermeasures exist. SQL injection also takes place inside the SQL interpreter, so detecting vulnerable code can be quite simple. With detection and mitigation in place, the odds of exposure are low (PDF p. 291).

## Relations
The attack itself is in WAS-C13-001. Detection is WAS-C25-002, prepared statements are WAS-C25-003, and the generic defenses begin at WAS-C25-005.
