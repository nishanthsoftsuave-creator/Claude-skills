---
id: WS-C10-002
title: How Sessions Work
source_pages: "122-124"
chapter: 10
concepts: [session-identifier, session-state, server-side-sessions, client-side-sessions, session-cookie, cookie-signing, cookie-encryption, scalability, serialization]
related: [WS-C10-001, WS-C10-003, WS-C09-005, WS-C02-004]
time_sensitive: true
---
# How Sessions Work
(Source: PDF pp. 122-124, tail PDF p. 125. The text at the top of PDF p. 122 above the "How Sessions Work" heading is the end of WS-C10-001. The tail page paragraph above the "How Attackers Hijack Sessions" heading belongs here.)

## What the section covers
How a session is established and the two common ways to implement it, server-side and client-side, including their scaling and security trade-offs.

## Meaning
- At login, the web server assigns the user a session identifier (session ID), usually a large random number. It is the minimum the browser must send with each later request so the server can carry on the conversation with the authenticated user; the server maps the ID to the user and acts for them (PDF p. 122).
- The session ID must be a temporary value distinct from the username. If the username were the ID, anyone could impersonate any user. By design, only a tiny fraction of the possible ID values should be valid sessions at any moment; if that is not so, the server has a weak-session vulnerability (WS-C10-003) (PDF p. 122).
- Besides the username, the server usually keeps session state against the ID: details of recent activity, such as pages visited or the contents of a shopping basket (PDF p. 122).

## Server-side sessions
- Traditionally the server holds session state in memory, and server and browser pass only the session ID back and forth. Listing 10-1 shows how Ruby on Rails does this: one function looks a session up in a cache by its ID (generating a new ID and empty session if none is found), and another writes the session to the cache with an expiry or deletes it (PDF pp. 122-123).
- Historically IDs were tried in the URL, an HTTP header or the request body. The method the community settled on, as the most common and reliable, is a session cookie: the server returns the ID in a Set-Cookie response header and the browser returns it in a Cookie request header (PDF p. 123).
- Cookies have been part of HTTP since Netscape introduced them in 1995. Unlike HTTP-native authentication (WS-C09-002), nearly every site uses them; EU law is why users see cookie notices everywhere (PDF p. 123).
- Server-side sessions are widely deployed and generally very secure, but they scale poorly because state sits in server memory. When a user authenticates, only one web server knows about the session; if a later request reaches a different server, that server must be able to recognise the user, so servers need to share session data (PDF p. 123).
- That typically means writing session state to a shared cache or database on every request and having each server read it. Both are costly in time and resources and can slow responsiveness on large sites, since every added user adds load to the session store (PDF p. 123).

## Client-side sessions
- Because server-side sessions are hard to scale, client-side sessions were invented: the server puts all the session state in the cookie rather than just the ID. It serialises the state to text before setting the header, often as JSON, and deserialises it when it comes back. Listing 10-2 shows Rails code that stores session data in a client-side cookie through a cookie jar that is signed or encrypted (PDF p. 124).
- Benefit: servers no longer share state, because each holds everything needed to restore the session from an incoming request, a big plus when scaling to thousands of simultaneous users (PDF p. 124).
- Security problem: in a naive implementation, a malicious user can modify or entirely forge the cookie contents, so the state must be encoded to prevent tampering (PDF p. 124).
- Option 1, encryption: encrypt the serialised cookie before sending and decrypt on return. The state is opaque to the client, and any attempt to alter or forge it corrupts the data so it cannot be read; the server logs the offender out and shows an error page (PDF p. 124).
- Option 2, digital signature: a lighter approach. A signature is a "fingerprint" of the serialised session state that anyone holding the signing key can recompute. The server recalculates the signature on return and rejects the session if it differs, thereby detecting tampering (PDF p. 124).
- Trade-off: signed (not encrypted) cookies can still be read by a curious user in the browser debugger. Keep that in mind if the session holds data, such as tracking information, that the user should not see (PDF p. 125).

## Time-sensitive statements
The Rails listings and the 1995 Netscape cookie origin are specific to the book's examples (PDF pp. 122-124).

## Relations
Sets up the attacks in WS-C10-003. Related background: stateful connections in WS-C02-004; logout in WS-C09-005.
