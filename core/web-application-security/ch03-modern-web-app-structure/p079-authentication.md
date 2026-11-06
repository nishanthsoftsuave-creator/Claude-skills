---
id: WAS-C03-013
title: Authentication
source_pages: "79"
chapter: 3
concepts: [authentication, http-basic-auth, digest-authentication, oauth, base64, two-factor-authentication, replay-attacks, credential-leakage]
related: [WAS-C03-012, WAS-C03-014, WAS-C05-002, WAS-C18-003, WAS-C18-005]
time_sensitive: false
---
# Authentication
(Source: PDF p. 79 from the "Authentication" heading)

## What the section covers
A short history of web authentication schemes and the main ones in use: HTTP basic, digest, and OAuth, together with their weaknesses.

## HTTP basic authentication
- Early authentication systems were simple. HTTP basic authentication attaches an Authorization header to each request, containing the text "Basic" and a base64-encoded username and password pair (PDF p. 79).
- On every request the server receives that pair and checks it against its database (PDF p. 79).
- The book calls this scheme flawed. The credentials are easy to leak in several ways, from compromised WiFi when the connection is plain HTTP to simple XSS attacks (PDF p. 79).
- SUPPLEMENTARY: the header as printed in the book shows a colon after "Basic"; in the HTTP specification (RFC 7617) the scheme name is followed by a space and the encoded credentials, with no colon.

## Digest authentication
A later development, digest authentication uses cryptographic hashes instead of base64 encoding. After it came many other techniques, including some that do not involve passwords or require external devices (PDF p. 79).

## OAuth
- Today most web applications choose from a suite of authentication architectures depending on the nature of the business. OAuth is described as great for websites that want to integrate with larger websites. A major site such as Facebook or Google provides a token that verifies a user's identity to a partner website (PDF p. 79).
- Benefit: the user's data only has to be updated on one site rather than several. Danger: one compromised website can lead to multiple compromised profiles (PDF p. 79).

## Current use and complements
HTTP basic and digest authentication are both still widely used, digest more so because it offers more defences against interception and replay attacks. They are often paired with tools such as 2FA, to ensure that authentication tokens are not compromised and that the identity of the logged-in user has not changed (PDF p. 79).

## When and how to apply
INTERPRETATION: when recon finds an Authorization header, identify which of the three schemes is in use, since each implies different weaknesses (Chapter 5 shows decoding a basic header with the browser's base64 function).

## Relations
Defines the "who" half of the pair introduced in WAS-C03-012; the "what may they access" half is WAS-C03-014. Recon of authentication mechanisms is in WAS-C05-002, and secure credentials in WAS-C18-003 and 2FA in WAS-C18-005.
