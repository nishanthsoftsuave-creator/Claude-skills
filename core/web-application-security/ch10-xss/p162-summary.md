---
id: WAS-C10-007
title: Cross-Site Scripting Summary
source_pages: "162"
chapter: 10
concepts: [xss-summary, stored-xss, reflected-xss, dom-based-xss, detectability, attack-surface, pen-testing-skills]
related: [WAS-C10-003, WAS-C10-004, WAS-C10-005, WAS-C10-006, WAS-C22-001]
time_sensitive: false
---
# Cross-Site Scripting Summary
(Source: PDF p. 162)

## What the section covers
The chapter's closing summary on XSS: how common it still is, how the three main forms differ in persistence and detectability, and why the book treats it as a core skill.

## Key points (PDF p. 162)
- XSS is less common than in the past but is still rampant across the web. More user interaction and more stored data in web applications give XSS more places to appear than ever.
- Unlike other common vulnerability types, XSS can be used from several angles. Some persist across sessions (stored) and some do not (reflected).
- XSS relies on finding places in the client where script can execute. Because browser specifications are complex, bugs in them can also cause unintended script execution, which is the DOM-based form.
- Detection differs by form. Stored XSS can be found by analysing what the database holds, so it is easy to detect. Reflected and DOM-based forms are often hard to pin down, so the book concludes they probably exist on many applications without having been found.
- The attack has existed for most of the web's history. The basic idea is unchanged, but its surface area and variations have grown.

## Why it matters
Because of its wide surface area, relative ease of use, ability to avoid detection and the power it gives, XSS should be a core part of any penetration tester's or bug bounty hunter's skill set (PDF p. 162).

## Relations
Detail on each form is in WAS-C10-003 (stored), WAS-C10-004 (reflected), WAS-C10-005 (DOM-based) and WAS-C10-006 (mutation-based). The matching defensive chapter begins at WAS-C22-001.
