---
id: WAS-C06-001
title: Identifying Third-Party Dependencies - Chapter Introduction and Client-Side Framework Lead-in
source_pages: "119"
chapter: 6
concepts: [third-party-dependencies, open-source-software, cve-database, client-side-frameworks, spa-libraries, css-frameworks, version-detection, recon]
related: [WAS-C03-011, WAS-C06-002, WAS-C15-001, WAS-C15-009]
time_sensitive: false
---
# Identifying Third-Party Dependencies - Chapter Introduction and Client-Side Framework Lead-in
(Source: PDF p. 119)

## What the section covers
The opening of Chapter 6: why third-party code matters during reconnaissance, followed by the short lead-in to the section on detecting client-side frameworks. This page has no separate chapter-intro row, so both parts are described here.

## Meaning
- Most modern web applications combine in-house code with external code brought in through one of several integration techniques (PDF p. 119).
- An external dependency is either proprietary, supplied by another company under a licensing model, or free, often from the open source community (PDF p. 119).

## Why it matters
- Relying on third-party code is not risk free. Such code often receives a less rigorous security review than the organisation's own code (PDF p. 119).
- While doing recon you will meet many integrations. The book asks you to note both the dependency itself and how it was integrated (PDF p. 119).
- Dependencies can become attack vectors. Some weaknesses are well known, so an attacker may not need to craft anything and can reuse an attack documented in a Common Vulnerabilities and Exposures (CVE) database (PDF p. 119).

## How it works: client-side frameworks
- Instead of building a complex user-interface layer from scratch, developers lean on well-maintained, well-tested frameworks (PDF p. 119).
- Three families are named: single-page-application (SPA) libraries that manage complex state; JavaScript-only helper frameworks that patch gaps in the language across browsers, with Lodash and jQuery as examples; and CSS frameworks that improve the look and feel, with Bootstrap and Bulma as examples (PDF p. 119).
- All three are usually easy to detect. If the exact version can be pinned down, matching ReDoS, Prototype Pollution and XSS weaknesses can often be found online, especially for older versions that were never updated (PDF p. 119).

## When and how to apply
INTERPRETATION: treat detection of a framework and its version as the first step of a lookup chain, from fingerprint to version to published weakness, which the following rows develop one family at a time.

## Relations
SPA frameworks were introduced in WAS-C03-011 and are detected in WAS-C06-002. Exploiting what you find is the subject of WAS-C15-001 and the CVE database in WAS-C15-009.
