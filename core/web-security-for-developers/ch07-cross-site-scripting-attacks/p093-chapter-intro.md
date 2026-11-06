---
id: WS-C07-001
title: Chapter 7 Introduction - Cross-Site Scripting Attacks
source_pages: "93"
chapter: 7
concepts: [cross-site-scripting, xss, javascript-injection, browser-execution, session-hijacking, credential-theft]
related: [WS-C06-001, WS-C07-002, WS-C07-003, WS-C07-004, WS-C10-003]
time_sensitive: false
---
# Chapter 7 Introduction - Cross-Site Scripting Attacks
(Source: PDF p. 93)

## What the section covers
The opening framing of the chapter: why the browser is the attacker's next injection target once the server is secure, what cross-site scripting is, and what JavaScript access lets an attacker do (PDF p. 93).

## Meaning
- The previous chapter showed attackers injecting code into web servers. If the server is secure, the attacker's next best target is the web browser (PDF p. 93).
- Browsers obediently run any JavaScript that appears in a page. If an attacker can get malicious JavaScript into a user's browser while that user views your site, the user is in trouble. This kind of code injection is called a cross-site scripting (XSS) attack (PDF p. 93).

## Why it matters
- JavaScript can read or modify any part of a web page, so XSS gives attackers a lot of room (PDF p. 93).
- They can steal login credentials, or other sensitive data such as credit card numbers, as the user types them (PDF p. 93).
- If the script can read the HTTP session information, the attacker can hijack the user's session completely and log in as that user remotely. Session hijacking is covered in Chapter 10 (PDF p. 93).
- XSS is described as remarkably common, with clear dangers (PDF p. 93).

## Scope of the chapter
It presents the three most common kinds of XSS and how to protect against each: stored (WS-C07-002), reflected (WS-C07-003) and DOM-based (WS-C07-004) (PDF p. 93).

## Relations
Continues the injection theme of WS-C06-001, moving from server-side targets to the browser. Session hijacking is treated in WS-C10-003.
