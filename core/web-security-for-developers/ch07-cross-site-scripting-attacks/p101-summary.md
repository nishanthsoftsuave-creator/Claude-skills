---
id: WS-C07-005
title: Chapter 7 Summary - Cross-Site Scripting Attacks
source_pages: "101-102"
chapter: 7
concepts: [xss-summary, html-escaping, content-security-policy, inline-javascript, stored-reflected-dom-xss]
related: [WS-C07-002, WS-C07-003, WS-C07-004, WS-C08-001]
time_sensitive: false
---
# Chapter 7 Summary - Cross-Site Scripting Attacks
(Source: PDF pp. 101-102. The text on PDF p. 101 above the "Summary" heading belongs to WS-C07-004.)

## What the section covers
The chapter's closing recap of what XSS is, where malicious script enters, and the two defences, with a pointer to the next chapter (PDF p. 101).

## Recap
- Cross-site scripting is an attack in which the attacker injects JavaScript into your site's pages as users view them (PDF p. 101).
- The malicious JavaScript usually enters through dynamic content coming from one of three places: a database (stored XSS, WS-C07-002), the HTTP request (reflected XSS, WS-C07-003) or the URI fragment (DOM-based XSS, WS-C07-004) (PDF p. 101).
- Two defences defeat XSS: escape any HTML control characters in dynamic content, and set a content security policy that prevents inline JavaScript from running (PDF p. 101).

## Relations
The book's next chapter examines another way attackers can prey on a site's users, cross-site request forgery, starting with WS-C08-001 (PDF p. 101).
