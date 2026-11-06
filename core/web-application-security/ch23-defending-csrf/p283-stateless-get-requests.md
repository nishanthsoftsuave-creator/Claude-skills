---
id: WAS-C23-005
title: Stateless GET Requests
source_pages: "283"
chapter: 23
concepts: [stateless-get, safe-http-methods, state-changing-requests, csrf-via-links, api-design, get-versus-post]
related: [WAS-C11-001, WAS-C11-002, WAS-C23-004, WAS-C23-006]
time_sensitive: false
---
# Stateless GET Requests
(Source: PDF p. 283)

## What the section covers
Why API calls reached by GET must never change server-side state, with a comparison of a combined endpoint and a split pair of endpoints.

## Why it matters
The most common and most easily distributed CSRF attacks use HTTP GET, because a link or an image tag can fire one. GET requests should therefore neither store nor modify server state. Doing so leaves future GET requests, or later modifications to GET requests, open to potential CSRF vulnerabilities (PDF p. 283).

## How it works
The book contrasts these designs (PDF p. 283):
- A single `user` route reads a user by id from the query string and, when an `updates` query value is present, also applies the update before returning the user. Retrieval and modification are merged into one GET.
- A separate `getUser` GET route that only returns the user, plus an `updateUser` POST route that applies the update.

The merged route can be abused with any GET vector: a link or image whose URL carries a user id and an update such as setting the email to an attacker's address. The split design cannot be hit that way. The POST route might still fall to more advanced CSRF, but not to links, images or other GET-style forgeries.

INTERPRETATION: the printed listings are slightly inconsistent (the merged route applies `req.updates` while reading the other values from `req.query`, and the POST route reads its id from the query); the point of the comparison is unaffected.

## When and how to apply
The author admits this looks like a simple architectural flaw, and says it is exactly that. The key rule covers any GET that could alter server state: do not do it. GET requests are at risk by default because of how the web works, so stateful operations should avoid them (PDF p. 283).

## Relations
The attack side is WAS-C11-001 (query parameter tampering) and WAS-C11-002 (alternate GET payloads). Part of the best-practice list in WAS-C23-004; WAS-C23-006 covers enforcing protection across the whole application.
