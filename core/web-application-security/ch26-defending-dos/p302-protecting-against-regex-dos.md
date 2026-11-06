---
id: WAS-C26-002
title: Protecting Against Regex DoS
source_pages: "302"
chapter: 26
concepts: [regex-dos, redos-defense, malicious-regex, backtracking, greedy-matching, user-supplied-regex, code-review]
related: [WAS-C14-002, WAS-C26-001, WAS-C26-006]
time_sensitive: false
---
# Protecting Against Regex DoS
(Source: PDF p. 302)

## What the section covers
How to keep regular expressions that trigger heavy backtracking out of an application. The page continues with the logical DoS heading, which belongs to the next row.

## Why it matters
Regex DoS is probably the easiest DoS form to defend against, but defenders have to know how such attacks are structured, which Part II showed. A good code review process can stop malicious or "evil" regexes from entering the codebase at all (PDF p. 302).

## How it works
Look for regexes that backtrack heavily over a repeated group. A typical shape is a group containing an `a` followed by a character class starred, wrapped in a plus (for instance `(a[ab]*)+`). The plus asks for a greedy match that collects all possible matches before returning, and the star repeats the subexpression as many times as possible (PDF p. 302).

## When and how to apply
Regexes built on the same technology can be harmless, so finding every evil one without false positives is slow and hard. This is where an open-source scanner for malicious segments, or a regex performance tester that tries inputs by hand, helps. Blocking such regexes is step one (PDF p. 302).

Step two is making sure no part of the application runs a user-supplied regex. The book compares allowing user-uploaded regexes to crossing a minefield and hoping you remembered the safe path, and calls maintaining such a system a huge coordinated effort and generally a bad idea. Also confirm that no integrated application uses user-supplied or badly written regexes (PDF p. 302).

## Relations
Defends against the attack in WAS-C14-002. The chapter summary (WAS-C26-006) adds a static analysis tool as a mitigation.
