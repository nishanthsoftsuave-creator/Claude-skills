---
id: WAS-C23-003
title: Stateless CSRF Tokens
source_pages: "282"
chapter: 23
concepts: [stateless-csrf-tokens, rest-statelessness, user-identifier, timestamp-expiration, cryptographic-nonce, session-scalability]
related: [WAS-C23-002, WAS-C03-002, WAS-C23-006]
time_sensitive: false
---
# Stateless CSRF Tokens
(Source: PDF p. 282)

## What the section covers
How to issue CSRF tokens in applications whose APIs keep no per-client state. The top of the page finishes the numbered token steps begun in WAS-C23-002; this module covers only what sits under the Stateless CSRF Tokens heading.

## Why it matters
Earlier, before REST-style API design became common, servers often tracked connected clients, so they could also manage CSRF tokens for them. In modern applications statelessness is frequently a design prerequisite and its benefits are large. The book argues it would be unwise to turn a stateless design into a stateful one only to add CSRF tokens (PDF p. 282).

## How it works
Tokens can be added to stateless APIs, but encryption has to be involved. As with stateless authentication tokens, the book says a stateless CSRF token should combine three things (PDF p. 282):
- a unique identifier of the user the token belongs to;
- a timestamp that can drive expiration;
- a cryptographic nonce whose key exists only on the server.

INTERPRETATION: together these make a token the server can verify on each request without remembering it, because the pieces can be re-checked rather than looked up in stored session state.

## Alternatives and trade-offs
The stateless token is described as practical and cheaper in server resources than the stateful alternative, because managing sessions does not scale as well as a sessionless approach (PDF p. 282).

## Relations
Refines the token idea of WAS-C23-002 for REST-style APIs (see WAS-C03-002 for REST traits). WAS-C23-006 shows a middleware that validates a token built from exactly these three parts.
