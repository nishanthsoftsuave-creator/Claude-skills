---
id: WS-C02-005
title: Encryption
source_pages: "42"
chapter: 2
concepts: [encryption, man-in-the-middle, tls, https, tls-handshake, cipher, data-integrity, privacy]
related: [WS-C02-004, WS-C02-006, WS-C13-001]
time_sensitive: false
---
# Encryption
(Source: PDF p. 42. The "Summary" heading lower on the same page belongs to WS-C02-006.)

## What the section covers
Why plaintext HTTP is unsafe and how Transport Layer Security (TLS) and HTTPS protect web traffic.

## Meaning
- Early HTTP requests and responses travelled as plaintext, so anyone intercepting the packets could read them. Such interception is a man-in-the-middle attack (PDF p. 42).
- Encryption is a way of disguising message contents from eavesdroppers by encoding them while in transit. Since private communication and online transactions are now ordinary, servers and browsers use it to defend users against interception (PDF p. 42).
- Transport Layer Security (TLS) is the encryption method servers and browsers use to send requests and responses. It gives both privacy and data integrity (PDF p. 42).
- HTTPS (HTTP Secure) is HTTP conducted over TLS (PDF p. 42).

## How it works
- Privacy: packets intercepted by a third party cannot be decrypted without the proper encryption keys (PDF p. 42).
- Integrity: any attempt to tamper with the packets can be detected (PDF p. 42).
- HTTPS begins with a TLS handshake in which client and server agree on an encryption method, called a cipher, and exchange encryption keys. After the handshake, all later requests and responses are opaque to outsiders (PDF p. 42).

## Why it matters
The author calls encryption a complex topic but key to securing a website. How to enable it for your site is covered in Chapter 13 (PDF p. 42).

## Relations
Follows the cookie-based session mechanics in WS-C02-004 and is recapped in WS-C02-006.
