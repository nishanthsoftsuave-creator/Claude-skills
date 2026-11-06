---
id: WS-C10-001
title: Session Hijacking - Chapter Introduction
source_pages: "121"
chapter: 10
concepts: [session, session-hijacking, authenticated-session, session-management, cookie-theft, session-fixation, weak-session-ids]
related: [WS-C10-002, WS-C10-003, WS-C09-001]
time_sensitive: false
---
# Session Hijacking - Chapter Introduction
(Source: PDF p. 121, tail PDF p. 122. The tail page text above the "How Sessions Work" heading belongs to this row.)

## What the section covers
Chapter 10's opening framing: what a session is, why stealing one is dangerous even when session management is sound, and the chapter road map.

## Meaning
- When a site has authenticated a user, the browser and server open a session. A session is an HTTP conversation in which the browser sends a series of requests matching the user's actions and the server recognises all of them as coming from the same authenticated user, without asking them to log in again for each request (PDF p. 121).
- If an attacker can read or forge the session information the browser sends, they can reach any user's account on your site (PDF p. 121).
- Modern web servers include secure session-management code, which makes manipulating or forging a session practically impossible. Even so, with no flaw in that code, an attacker may still take over someone else's valid session while it is active. That is session hijacking (PDF p. 121).

## Why it matters
- The book rates session hijacking as generally a larger risk than the authentication weaknesses of the previous chapter (WS-C09-001), because it likewise lets an attacker into any user's account. The prize is so attractive that attackers have found many ways to do it (PDF p. 122).

## How the chapter is organised
- It first explains how websites implement session management (WS-C10-002). It then covers three hijacking routes: cookie theft, session fixation, and exploiting weak session IDs (WS-C10-003) (PDF p. 122).

## Relations
Follows Chapter 9, which dealt with the login step; continues in WS-C10-002 and WS-C10-003.
