---
id: WAS-C28-002
title: Part III Summary - Web Application Reconnaissance
source_pages: "315"
chapter: 28
concepts: [recon-summary, application-mapping, modern-web-structure, subdomains, third-party-dependencies, application-architecture, fingerprinting]
related: [WAS-C02-001, WAS-C03-001, WAS-C04-001, WAS-C06-001, WAS-C07-002, WAS-C28-003]
time_sensitive: false
---
# Part III Summary: Web Application Reconnaissance
(Source: PDF p. 315, with the end of the block on PDF p. 316)

## What the section covers
The recap of Part I (recon). It restates why recon comes first, then summarizes the structure of modern applications, subdomains, APIs and HTTP, third-party dependencies and application architecture.

## Why recon matters
- Applications are large and complex, so the first step in finding vulnerabilities is to map the application and examine each major functional component for architectural or logical risk (PDF p. 315).
- Good recon gives a deep understanding of the target, which is used both to prioritize attacks and to avoid detection (PDF p. 315).
- For a defender, recon skill shows how a capable attacker would approach the application, so defenses can be prioritized. Recon skill can be limited by engineering skill, so the two go together (PDF p. 315).

## The structure of modern web applications
- Today's applications sit on many layers of technology and usually have wide server-to-user and user-to-user features. Most keep data in several places, on both server and client (typically the browser), so the potential surface is broad (PDF p. 315).
- The databases, display technologies and server software in use were built on the problems of earlier web applications and are shaped largely by developer productivity and user experience, which has produced new kinds of vulnerabilities (PDF p. 315).

## Subdomains, APIs and HTTP
- Mastering recon means knowing how to map the full surface of an application. Modern applications are more distributed than older ones, so several web servers may need to be found before exploitable code turns up, and how those servers interact helps in prioritizing attacks (PDF p. 315).
- HTTP is the dominant application-layer protocol for client-server traffic, but newer protocols are arriving. The sentence finishes on the next page: future applications may use sockets or real time communication heavily, so recon techniques that are easy to adapt are essential.

## Third-party dependencies (continued on the next page)
Applications lean on third-party integrations as much as on first-party code, sometimes more, and these are not audited to the same standard, which makes them a good attack path. Recon can fingerprint specific versions of web servers, client-side frameworks, CSS frameworks and databases, and those fingerprints can reveal vulnerable versions (PDF p. 316).

## Application architecture
Examining an application's software architecture can expose widespread weaknesses that come from inconsistent security controls. Security architecture can be used as a proxy for code quality, a signal hackers weigh when picking which application to target (PDF p. 316).

## Relations
Condenses Part I; compare the detailed chapters on the structure of modern applications (WAS-C03-001), subdomains (WAS-C04-001), third-party dependencies (WAS-C06-001) and architecture signals (WAS-C07-002). The offense recap follows in WAS-C28-003.
