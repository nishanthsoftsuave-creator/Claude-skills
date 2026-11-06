---
id: WAS-T-002
title: Part II - Offense (Part Opener)
source_pages: "143-144"
chapter: part-2
concepts: [offense, part-overview, recon-recap, attack-techniques, applied-recon, exploit-chains]
related: [WAS-T-001, WAS-C08-001, WAS-C09-001]
time_sensitive: false
---
# Part II - Offense (Part Opener)
(Source: PDF pp. 143-144; chapter 9 opens straight afterwards and is described in WAS-C09-001)

## What the section covers
A recap of everything Part I taught and a statement of what the attack chapters will do with it.

## Meaning: the recap
- Part I covered finding and documenting how an application is built and works. It looked at locating APIs on a server, including those on subdomains, and at listing their endpoints and the HTTP verbs they accept (PDF p. 143).
- After mapping subdomains, APIs and verbs, the book showed how to learn what request and response payloads each endpoint accepts, by a generic approach and by finding open specifications (PDF p. 143).
- It then covered third-party dependencies: detecting SPA frameworks, databases and web servers, and general methods like fingerprinting for other versions (PDF p. 143).
- It ended with architectural flaws that leave functionality poorly protected, using insecure designs common in hurried applications (PDF p. 143).

## How it works: what Part II does
- Part II teaches common techniques hackers use against modern applications. It follows Recon because recon is needed to apply these attacks (PDF p. 144).
- Many attacks are powerful and sometimes easy, but cannot be used on any endpoint, form or link. Recon from Part I helps find where they apply to a real application (PDF p. 144).
- The attacks stem from insecure API endpoints, insecure forms, poorly designed browser standards, badly configured server-side parsers and more (PDF p. 144).
- With Part I you can find endpoints and judge whether they are insecure, and inspect client code to see whether it handles DOM changes safely. Fingerprinting client frameworks helps find UI weaknesses, since client code is local and easy to review. The techniques build on each other (PDF p. 144).
- Readers are asked to think about how recon would help find weaknesses where each upcoming exploit applies (PDF p. 144).

## Relations
Follows Part I (WAS-T-001, WAS-C08-001); the next chapter begins in WAS-C09-001.
