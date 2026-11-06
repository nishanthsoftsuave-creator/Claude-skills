---
id: WAS-C23-002
title: CSRF Tokens
source_pages: "281"
chapter: 23
concepts: [csrf-tokens, anti-csrf-token, token-validation, per-session-tokens, collision-resistance, forged-requests, ajax-and-forms]
related: [WAS-C23-001, WAS-C23-003, WAS-C11-001]
time_sensitive: false
---
# CSRF Tokens
(Source: PDF p. 281)

## What the section covers
The introduction to the anti-CSRF token, which the book calls the most powerful defense against cross-site request forgery, and the first two steps of how it works. The paragraph above this heading on the page finishes the header-verification discussion and belongs to WAS-C23-001.

## Meaning
An anti-CSRF token (often just a CSRF token) is a secret value the server hands to the client and expects back on later requests. The book says it defends in a very simple way, can be fitted into many application architectures, and is the primary CSRF defense of most major websites (PDF p. 281).

## How it works
Figure 23-1 shows two flows side by side. In the legitimate flow the client asks for a page, the server returns the page together with a CSRF token, the client calls an HTTP resource and attaches the token, and the server validates the token before responding. In the attack flow a hacker crafts a malicious link that a user follows to reach the same resource; the request carries no valid token because, as the figure puts it, it did not originate from the user, so the server blocks it (PDF p. 281).

The text lists the mechanism in steps:
1. The server sends the client a special token generated cryptographically with a very low-collision algorithm, so two identical tokens are extremely unlikely. It may be regenerated as often as every request, but is generally issued per session (PDF p. 281).
2. Each later request from the web application sends the token back, in forms and in AJAX calls alike. On arrival the server checks that the token is live (not expired), authentic and not altered. If the check fails, the request is logged and fails (PDF p. 281).

A third step continues at the top of the next page: because tokens are unique per session and per user, an attacker would need a current token and would have to target a specific user rather than a crowd. It is described in the next row.

## When and how to apply
The book has the token sent back with each request, in forms and in AJAX calls alike (PDF p. 281).
INTERPRETATION: because every request path must carry the token, the front end needs one consistent mechanism for adding it rather than per-form handling.

## Relations
Follows header verification (WAS-C23-001). The stateless variant is WAS-C23-003, and the attack being stopped is described in WAS-C11-001.
