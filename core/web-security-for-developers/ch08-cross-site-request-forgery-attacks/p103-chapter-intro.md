---
id: WS-C08-001
title: Chapter 8 Introduction - Cross-Site Request Forgery Attacks
source_pages: "103"
chapter: 8
concepts: [csrf, xsrf, malicious-links, inbound-links, cross-site-request-forgery, trusted-user-actions]
related: [WS-C07-001, WS-C08-002, WS-C08-007]
time_sensitive: true
---
# Chapter 8 Introduction - Cross-Site Request Forgery Attacks
(Source: PDF p. 103, tail PDF p. 104. The text on PDF p. 104 below the "Anatomy of a CSRF Attack" heading belongs to WS-C08-002.)

## What the section covers
The opening framing of the chapter: how a malicious link can be turned against your own users, the name and pronunciation of the attack, and examples of what attackers have achieved with it (PDF pp. 103-104).

## Meaning
- The previous chapter covered XSS, where attackers inject JavaScript into a browser through page elements such as comment sections, search results and URLs. This chapter looks at how attackers use malicious links to hack your users (PDF p. 103).
- No website is an island. A public URL means other sites will link to it, which a site owner generally wants, since more inbound links bring more traffic and better search engine rankings (PDF p. 103).
- Not every linker has good intentions. An attacker can trick a user into clicking a malicious link that has undesirable or unexpected side effects. That is cross-site request forgery (CSRF or XSRF), which security researchers sometimes pronounce "sea-surf" (PDF p. 103).

## Why it matters
- CSRF is described as remarkably common; most major websites have shown the vulnerability at one time or another (PDF p. 103).
- Attackers have used it to steal Gmail contact lists, trigger one-click purchases on Amazon and change router configuration (PDF pp. 103-104).
- The chapter examines how CSRF attacks typically work and the coding practices that guard against them (PDF p. 104).

## Relations
Follows the XSS chapter (WS-C07-001). The attack mechanics are in WS-C08-002 and the chapter recap is WS-C08-007.

## Time-sensitive statements
- Historical CSRF incidents involving Gmail contact lists, Amazon one-click purchases and router configuration changes (PDF pp. 103-104).
