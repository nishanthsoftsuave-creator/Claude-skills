---
id: WS-C08-005
title: "Mitigation 3: Use the SameSite Cookie Attribute"
source_pages: "106"
chapter: 8
concepts: [samesite-cookie, samesite-strict, samesite-lax, session-cookie, inbound-links, cross-site-requests, csrf-mitigation]
related: [WS-C08-003, WS-C08-004, WS-C08-006, WS-C10-002, WS-C10-003]
time_sensitive: false
---
# Mitigation 3: Use the SameSite Cookie Attribute
(Source: PDF p. 106, tail PDF p. 107. The "Mitigation 3" heading is on PDF p. 106. On PDF p. 107 the text above the "Bonus Mitigation: Require Reauthentication for Sensitive Actions" heading belongs here.)

## What the section covers
Why cookies must be restricted by origin, how SameSite=Strict and SameSite=Lax behave, and the trade-off for session cookies and inbound links (PDF pp. 106-107).

## Why it matters
- By default a browser attaches to any request to your site the last cookies the site set, regardless of what initiated the request. So malicious cross-site requests reach your server carrying your security cookies (PDF p. 106).
- That alone does not defeat anti-CSRF measures, but if an attacker steals the security token from your HTML forms and puts it in their own malicious forms, they can still mount a CSRF attack (PDF p. 106). This is the loophole left by WS-C08-004.

## How it works
- A SameSite attribute on a cookie tells the browser to strip that cookie from requests to your site when the request comes from an external domain, such as an attacker's site (PDF p. 106).
- Setting SameSite=Strict (Listing 8-3) means the browser sends the cookie only on requests initiated from within your own site (PDF pp. 106-107).

```
Set-Cookie: _xsrf=5978e29d4ef434a1; SameSite=Strict;
```

## When and how to apply
- Set SameSite on all your cookies, not just those for CSRF defence (PDF p. 107).
- Caveat: if you use cookies for session management and set SameSite=Strict on the session cookie, it is removed from any request to your site that originates on another website. Every inbound link then forces the user to log in again, annoying people who already have a session open. The book's comparison: imagine logging back in to Facebook every time somebody shared a video (PDF p. 107).
- Remedy: use the value Lax (Listing 8-4), which lets other sites' GET requests carry the cookie (PDF p. 107).

```
Set-Cookie: session_id=82938d911e13f3; SameSite=Lax;
```

- This keeps seamless linking into your site while removing the attacker's ability to forge actions such as POST requests. If your GET requests are free of side effects, this setting is no less safe (PDF p. 107).

## Alternatives and trade-offs
Strict gives the tightest isolation but breaks session continuity on inbound links; Lax allows cross-site GET only and relies on the side-effect-free GET rule from WS-C08-003 (PDF p. 107).

## Relations
Completes the technical trio with WS-C08-003 and WS-C08-004. A further user-facing layer follows in WS-C08-006. Session cookies are covered in WS-C10-002 and WS-C10-003.
