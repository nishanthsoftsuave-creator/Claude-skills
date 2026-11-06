---
id: WS-C13-001
title: "Chapter 13 Introduction: Encryption"
source_pages: "145"
chapter: 13
concepts: [encryption, https, certificate-authority, cryptography, chapter-roadmap, man-in-the-middle]
related: [WS-C13-002, WS-C13-003, WS-C13-004, WS-C13-005, WS-C02-005]
time_sensitive: false
---
# Chapter 13 Introduction: Encryption
(Source: PDF p. 145, tail PDF p. 146. The tail is the few lines at the top of PDF p. 146 above the "Encryption in the Internet Protocol" heading, which begins WS-C13-002.)

## What the section covers
The chapter's opening framing: why encryption is central to the web, how simple it is to start with HTTPS, and a roadmap of what the chapter covers (PDF pp. 145-146).

## Why it matters
- Encryption underpins the modern internet. Without a way to exchange data packets privately and securely, e-commerce would not exist and users could not safely authenticate themselves to sites (PDF p. 145).
- HTTPS (HyperText Transfer Protocol Secure) is the most widely used form of encryption on the web (PDF p. 145).

## Meaning and framing
- Web servers and web browsers universally support HTTPS, so a developer can divert all traffic to it and guarantee secure communication for users (PDF p. 145).
- To adopt HTTPS, a developer needs only to obtain a certificate from a certificate authority and install it with the hosting provider (PDF p. 145).
- This ease hides substantial complexity in what happens when a site and a user agent talk over HTTPS. Modern cryptography, the study of methods for encrypting and decrypting data, rests on techniques developed and actively researched by mathematicians and security professionals (PDF p. 145).
- Thanks to the abstraction layers of the Internet Protocol, a developer does not need linear algebra or number theory to benefit from those discoveries. Still, the more you understand about the underlying algorithms, the better you can anticipate potential risks (PDF pp. 145-146).

## Chapter roadmap
The chapter has three movements (PDF p. 146):
1. A general overview of how encryption is used in the Internet Protocol and the mathematics behind it (WS-C13-002).
2. The practical steps a developer takes to start using HTTPS (WS-C13-003).
3. How hackers exploit unencrypted or weakly encrypted traffic, and how some attacks bypass encryption entirely (WS-C13-004).

## Relations
Chapter 2 introduced encryption at a high level (WS-C02-005); this chapter goes deeper. The chapter recap is WS-C13-005.
