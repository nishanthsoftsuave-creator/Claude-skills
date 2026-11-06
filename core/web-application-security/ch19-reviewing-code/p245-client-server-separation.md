---
id: WAS-C19-008
title: Secure-Coding Anti-Patterns - Client/Server Separation
source_pages: "245"
chapter: 19
concepts: [client-server-coupling, separation-of-concerns, monolithic-applications, html-templating, data-transit-format, authentication-payloads]
related: [WAS-C19-007, WAS-C19-009]
time_sensitive: false
---
# Secure-Coding Anti-Patterns: Client/Server Separation
(Source: PDF p. 245; the section continues on the next page)

## What the section covers
The final anti-pattern in the chapter: client and server code bound so tightly that neither can work alone.

## Meaning
- This is the client/server coupling anti-pattern. It arises when client and server code are so tightly bound that one cannot function without the other (PDF p. 245).
- It is mostly seen in older web applications but can still be found in monolithic applications today.

## What a secure design looks like
A secure application made of a client and a server has the two developed independently, talking over a network with a predefined data format and network protocol (PDF p. 245).

## Why coupling is risky
- Deep coupling, for example PHP templating code mixed with authentication logic, makes an application much easier to exploit because the layers are not separate.
- Instead of reading the result of a network request, a module returns its own HTML including form data, as in an authentication form. The server must then parse that HTML and make sure no script execution or parameter tampering occurs, both in the HTML and in the authentication logic.

## Continuation
The text goes on at the top of the next page: in a fully separated design the server is not responsible for the structure or content of the HTML, rejects any HTML it receives, and accepts authentication payloads only in a predefined transit format. That continuation carries no page cite here and the conclusion is treated in the next module.

## When and how to apply
INTERPRETATION: when a handler both builds markup and checks credentials, flag it as a coupling finding and ask whether the same behavior can be exposed as a data-only endpoint.

## Relations
Follows the permissions anti-pattern (WAS-C19-007). The chapter closes in WAS-C19-009.
