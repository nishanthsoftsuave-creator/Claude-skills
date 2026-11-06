---
id: WS-C13-005
title: "Chapter 13 Summary: Encryption"
source_pages: "157-158"
chapter: 13
concepts: [chapter-summary, https, tls-handshake, cipher-suite, digital-certificate, domain-verification, hsts, server-upgrades]
related: [WS-C13-002, WS-C13-003, WS-C13-004, WS-C14-001]
time_sensitive: false
---
# Chapter 13 Summary: Encryption
(Source: PDF pp. 157-158; this covers only the "Summary" heading on PDF p. 157 and below. The "Government Agencies" text above it belongs to WS-C13-004.)

## What the section covers
The chapter's recap of how HTTPS works and how to deploy it, plus a closing note about keeping server technology current and a pointer to the next chapter (PDF pp. 157-158).

## Summary of the chapter
- Why use HTTPS: it keeps communication between browsers and your site private and tamper-proof. HTTPS is HTTP over Transport Layer Security (TLS) (PDF p. 157).
- The handshake (recaps WS-C13-002): a TLS conversation starts when a web server and user agent perform a TLS handshake. The browser offers its supported cipher suites; each combines a key-exchange algorithm, a block cipher and a message authentication code algorithm. The server selects one it supports and returns its digital certificate (PDF p. 157).
- Session key: the browser uses the public key in the certificate to encrypt a randomly generated TLS session identifier with the key-exchange algorithm and sends it to the server. With both sides holding it, it serves as the key for subsequent messages encrypted with the chosen block cipher, and each packet's authenticity is checked with the MAC algorithm (PDF p. 157).
- Certificates (recaps WS-C13-003): a handful of certificate authorities issue them and require you to prove ownership of your domain in the Domain Name System first. As trusted third parties between browser and website, they stop spoofed sites from presenting fake certificates (PDF p. 157).
- Deployment: with a certificate in hand, configure the web server to accept traffic on port 443, tell it where the certificate and its decryption key are, and redirect HTTP on port 80 to HTTPS on 443. Finally, set an HTTP Strict Transport Security policy so the browser does not send sensitive data, such as session cookies, in HTTP requests before the upgrade to HTTPS (PDF p. 157).

## When and how to apply (closing advice)
Upgrade your web server technology fairly frequently so you are sure to be using the most modern, and therefore most secure, cipher suites. Encryption standards are constantly researched and improved as older algorithms are compromised or found vulnerable (PDF p. 158).

## Relations
The book links this need to keep servers current to a broader topic: how to test, secure and manage any third-party applications used to serve a website, which is the subject of the next chapter (PDF p. 158; see WS-C14-001). The attacks that motivate HTTPS are in WS-C13-004.
