---
id: WS-C02-004
title: Stateful Connections
source_pages: "41"
chapter: 2
concepts: [stateful-connection, http-session, cookies, set-cookie, cookie-header, session-tracking, cookie-theft, cookie-forgery, impersonation]
related: [WS-C02-003, WS-C02-005, WS-C10-001]
time_sensitive: false
---
# Stateful Connections
(Source: PDF p. 41. The text at the top of PDF p. 41, above the heading, is the end of WS-C02-003.)

## What the section covers
Why HTTP alone cannot tell users apart, how sessions are built on top of it using cookies, and why those cookies are attractive to attackers.

## Meaning
- HTTP does nothing to distinguish which requests came from which user agent, even though a server handles many at once. This did not matter in the early internet because pages were mostly read-only (PDF p. 41).
- Modern sites let users log in and follow their activity across pages, so HTTP conversations must be made stateful. A connection is stateful when client and server perform a handshake and keep sending packets back and forth until one side ends it (PDF p. 41).
- The whole conversation between one user agent and a server is an HTTP session (PDF p. 41).

## How it works
- To recognise which user each request belongs to, the server needs a mechanism to track the agent across requests. The usual one: the server includes a Set-Cookie header in the first response, asking the user agent to store a cookie, a small piece of text data tied to that web domain (PDF p. 41).
- The user agent then sends the same data back in the Cookie header of every later request. If done correctly, the cookie contents uniquely identify the agent and so establish the session (PDF p. 41).

## Limitations and failure modes
- Session data in cookies is a "juicy target". An attacker who steals another user's cookie can impersonate that user on the site. If an attacker gets a site to accept a forged cookie, they can impersonate any user they like (PDF p. 41).
- Stealing and forging cookies is covered in Chapter 10, on session hijacking (PDF p. 41).

## Relations
Follows the HTTP request and response mechanics in WS-C02-003. Encryption, the next topic, protects the traffic carrying these cookies (WS-C02-005).
