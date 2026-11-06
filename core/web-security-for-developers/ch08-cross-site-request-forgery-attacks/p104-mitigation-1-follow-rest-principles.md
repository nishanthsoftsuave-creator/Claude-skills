---
id: WS-C08-003
title: "Mitigation 1: Follow REST Principles"
source_pages: "104"
chapter: 8
concepts: [rest, http-methods, get-side-effect-free, safe-methods, csrf-mitigation, state-changing-requests]
related: [WS-C08-002, WS-C08-004, WS-C08-007]
time_sensitive: false
---
# Mitigation 1: Follow REST Principles
(Source: PDF p. 104, tail PDF p. 105. The "Mitigation 1" heading is at the bottom of PDF p. 104. On PDF p. 105 the text above the "Mitigation 2: Implement Anti-CSRF Cookies" heading belongs here.)

## What the section covers
The first CSRF defence: use GET only to fetch, and use other HTTP methods for anything that changes server state, following Representational State Transfer (PDF pp. 104-105).

## When and how to apply
- Make sure GET requests never change the state of the server. Use GET only to fetch pages or other resources (PDF p. 104).
- Actions that change server state, such as logging in or out, resetting passwords, writing posts or closing an account, should happen only through PUT, POST or DELETE requests (PDF p. 104).
- This design philosophy is called Representational State Transfer (REST) and has many other benefits beyond CSRF protection (PDF p. 104).

## Meaning: mapping operations to methods
- REST says to map site operations to the HTTP method that fits their intention. The book states: fetch data or pages with GET; create new objects on the server (comments, uploads, messages) with PUT; modify objects with POST; delete objects with DELETE (PDF p. 105). The book's mapping is recorded as printed; it is the reverse of the common convention.
  SUPPLEMENTARY: HTTP semantics (RFC 9110) and most REST guides pair creation with POST and full replacement with PUT.
- Some actions have no obvious method. When a user logs in, whether they are creating a new session or changing their status is, in the book's words, a philosophical discussion. For CSRF protection what matters is that no state-changing action is assigned to GET (PDF p. 105).

## Limitations and failure modes
Securing GET does not remove vulnerabilities in other request types; the second mitigation addresses those (WS-C08-004) (PDF p. 105).

## Relations
Follows the Twitter example in WS-C08-002 and is followed by WS-C08-004. The SameSite Lax setting later relies on GET being side-effect free (WS-C08-005).
