---
id: WS-C10-004
title: Chapter 10 Summary - Session Hijacking
source_pages: "128-130"
chapter: 10
concepts: [session-hijacking-summary, httponly, secure-cookie, samesite, url-rewriting, weak-session-ids, security-advisories]
related: [WS-C10-002, WS-C10-003, WS-C11-001]
time_sensitive: false
---
# Chapter 10 Summary - Session Hijacking
(Source: PDF pp. 128-130; the text above the "Summary" heading on PDF p. 128 is the end of WS-C10-003. PDF p. 130 carries no text.)

## What the section covers
The book's recap of Chapter 10.

## Recap
- When a site authenticates a user, browser and server open a session. Session state can be kept on the server, or on the client as an encrypted or digitally signed cookie (WS-C10-002) (PDF p. 128).
- Attackers will try to steal session cookies, so protect them (WS-C10-003) (PDF p. 129):
  - against hijacking via cross-site scripting, make cookies inaccessible to JavaScript;
  - against hijacking via man-in-the-middle attacks, send cookies only over HTTPS;
  - against hijacking via cross-site request forgery, strip cookies from sensitive cross-site requests.
- These protections are added through keywords in the Set-Cookie response header. The summary names them as HttpOnly, SecureOnly and SameSite respectively (PDF p. 129). Note that the chapter body (Listing 10-5) uses the keyword Secure, not "SecureOnly"; the summary's spelling appears to be a slip in the book. INTERPRETATION: use Secure.
- Older web servers may be open to session fixation, so disable URL rewriting as a way to carry session IDs. Servers are sometimes found to generate guessable IDs, so watch security advisories for your stack and patch as required (PDF p. 129).
- Looking ahead: the next chapter turns to correctly implementing access control so malicious users cannot see content or perform actions they should not (WS-C11-001) (PDF p. 129).

## Relations
Recaps WS-C10-002 and WS-C10-003.
