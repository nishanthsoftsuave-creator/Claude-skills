---
id: WAS-C11-004
title: Chapter 11 Summary - CSRF
source_pages: "171-172"
chapter: 11
concepts: [csrf, trust-model, browser-trust, session-credentials, whatwg, summary]
related: [WAS-C11-001, WAS-C11-003, WAS-C23-007]
time_sensitive: false
---
# Chapter 11 Summary: Cross-Site Request Forgery
(Source: PDF pp. 171-172; PDF p. 172 has no text)

## What the section covers
The closing summary of the CSRF chapter, restating why the attack works.

## Meaning (PDF p. 171)
- CSRF attacks exploit the trust that exists between a web browser, a user, and a web server or API. By default the browser trusts that actions coming from the user's device are made on that user's behalf.
- That is only partly true in a CSRF attack: the user does start the action, but does not understand what it does behind the scenes. When a user clicks a link, the browser makes a GET request for them whatever the link's origin. Because the link is trusted, valuable authentication data can ride along with the request.
- At its core the attack works because of the trust model developed by browser standards bodies such as WhatWG. The book says these standards may change in future and make CSRF-style attacks much harder to carry out, but for the time being the attacks remain common and easy to exploit.

## Why it matters
INTERPRETATION: the summary shows that the fix cannot rely on the user noticing anything, since the user never sees the forged request. Verification has to happen in the application, which is Part III's subject.

## Relations
Recaps WAS-C11-001 to WAS-C11-003; defences are summarised in WAS-C23-007.
