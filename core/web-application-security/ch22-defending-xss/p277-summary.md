---
id: WAS-C22-012
title: Defending Against XSS - Summary
source_pages: "277-278"
chapter: 22
concepts: [xss-defence, client-side-mitigation, centralised-dom-append, dom-sinks, content-security-policy, layered-defence]
related: [WAS-C22-001, WAS-C22-002, WAS-C22-009, WAS-C22-011]
time_sensitive: false
---
# Defending Against XSS: Summary
(Source: PDF p. 277; the second page of the row, PDF p. 278, is blank)

## What the section covers
The chapter's closing conclusions on defending against XSS.

## Main points
- The most common forms of XSS are easy to defend against. The difficulty arises mostly when a feature requires showing user-submitted information as DOM instead of text (PDF p. 277).
- XSS can be mitigated at many levels of the stack: network, database or client. The client is nearly always the best place, because an XSS attack needs client-side execution to be an XSS attack at all (PDF p. 277).
- Anti-XSS coding practices should always be used. An application should have one centralised function for appending to the DOM when it is needed, so sanitising is routine across the whole application (PDF p. 277).
- The common sinks for DOM XSS should be considered and, where not needed, sanitised or blocked (PDF p. 277).
- A CSP is a good first measure against common XSS but does not protect against DOM XSS. Treat an application as properly secured against XSS only when all or many of these steps are in place (PDF p. 277).

## Relations
Recaps WAS-C22-001 (coding rule), WAS-C22-002 (sinks and sanitising), WAS-C22-009 and WAS-C22-011 (CSP).
