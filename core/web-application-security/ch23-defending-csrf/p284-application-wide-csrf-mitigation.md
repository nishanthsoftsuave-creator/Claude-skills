---
id: WAS-C23-006
title: Application-Wide CSRF Mitigation
source_pages: "284"
chapter: 23
concepts: [application-wide-defense, csrf-middleware, token-validation, header-validation, request-pipeline, weakest-link]
related: [WAS-C23-001, WAS-C23-003, WAS-C23-004, WAS-C23-007]
time_sensitive: false
---
# Application-Wide CSRF Mitigation
(Source: PDF p. 284)

## What the section covers
Why CSRF defenses must cover the whole application, and a worked middleware that combines header checks with token validation. The code and its explanation run onto the next page, which is described here without a page cite.

## Why it matters
The techniques only help when applied everywhere. As with many attacks, the weakest link breaks the chain, so the book urges designing an application around these protections from the start (PDF p. 284).

## How it works
Most modern server stacks allow middleware: scripts that run on every request before any route logic. Such middleware can apply the defenses to all server routes (PDF p. 284). The example has these parts:
- A whitelist of three trusted origin locations (the main site, API host and portal).
- A header validator that takes the headers and the HTTP method. For POST it requires both the referer and the origin to be in the whitelist; for other methods it checks the referer only.
- A token validator that decrypts the token and splits it, using a colon separator, into a user id, a date and a nonce, then starts three validity flags set to false (PDF p. 284). The three checks themselves are printed at the top of the next page: the user id must match the current user, the date must be less than one week old, and the nonce must validate against the user id and date.

The final handler combines them. It logs the request and answers 401 if the header check or the token check fails, and otherwise moves on to the next middleware. This continuation is printed on the following page, where the book also says the middleware can be invoked on all requests or defined for specific ones, and that it only verifies that the origin and/or referrer headers are correct and then that the CSRF token is valid, returning an error before any other logic if either fails.

The page after also says the middleware depends on the client passing a CSRF token on every request, so that step should be automated on the client too: for example by using the proxy pattern to overwrite the default XMLHttpRequest behavior so the token is always included, or by building a request library that wraps XMLHttpRequest and injects the right token depending on the HTTP verb. The printed handler condition is also missing a closing parenthesis (a printed slip).

## Assumptions and prerequisites
INTERPRETATION: the token format in the example (user identifier, timestamp and nonce) matches the stateless design of WAS-C23-003.

## Limitations
INTERPRETATION: the one-week window is an example value chosen by the author; applications should set expiry to fit their own risk.

## Relations
Combines WAS-C23-001 (header checks) and WAS-C23-003 (stateless tokens) as listed in WAS-C23-004; the closing summary is WAS-C23-007.
