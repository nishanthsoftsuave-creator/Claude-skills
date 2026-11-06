---
id: A00-007
title: OWASP API Security Top 10 - 2019 (overview)
source_pages: "7"
chapter: front
concepts: [api-top-10, broken-object-level-authorization, broken-user-authentication, excessive-data-exposure, rate-limiting, broken-function-level-authorization, mass-assignment, security-misconfiguration, injection, improper-assets-management, insufficient-logging-and-monitoring, review-checklist]
related: [A01-001, A02-001, A03-001, A04-001, A05-001, A09-001, A10-001, A00-006]
time_sensitive: true
---
# OWASP API Security Top 10 - 2019 (overview)
(Source: PDF p. 7)

## What the section covers
The one-page summary table that names the ten risks and gives each a two- or three-sentence definition. This module keeps those definitions together so the list can be used as a checklist; each chapter module holds the detail.

## The ten risks as the document defines them
1. **API1 Broken Object Level Authorization.** APIs tend to expose endpoints that take object identifiers, which opens a wide access-control attack surface. Any function that reaches a data source using an identifier supplied by the user should check that the caller may act on that object (PDF p. 7). Detail: A01-001.
2. **API2 Broken User Authentication.** Authentication is often implemented incorrectly, letting attackers compromise tokens or exploit implementation flaws to take on other users' identities, temporarily or permanently. Once the system cannot reliably identify its client or user, the whole API's security is undermined (PDF p. 7). Detail: A02-001.
3. **API3 Excessive Data Exposure.** Aiming for generic implementations, developers return every property of an object without weighing each property's sensitivity, and leave the client to filter what the user sees (PDF p. 7). Detail: A03-001.
4. **API4 Lack of Resources & Rate Limiting.** APIs frequently put no limit on the size or number of resources a client may request. Beyond degrading performance to the point of denial of service, this leaves authentication open to brute force (PDF p. 7). Detail: A04-001.
5. **API5 Broken Function Level Authorization.** Complex access-control policies with many hierarchies, groups and roles, plus a blurred line between administrative and regular functions, produce authorization flaws through which attackers reach other users' resources or administrative functions (PDF p. 7). Detail: A05-001.
6. **API6 Mass Assignment.** Binding client-supplied data such as JSON straight onto data models, without filtering properties against an allow-list, lets an attacker set properties they should not touch, after guessing names, exploring other endpoints, reading documentation or simply adding fields to a payload (PDF p. 7). Detail: A06-001.
7. **API7 Security Misconfiguration.** The usual causes are insecure defaults, incomplete or ad-hoc configuration, open cloud storage, misconfigured HTTP headers, unnecessary HTTP methods, permissive Cross-Origin Resource Sharing (CORS) and verbose error messages that leak sensitive information (PDF p. 7). Detail: A07-001.
8. **API8 Injection.** SQL, NoSQL, command injection and similar flaws arise when untrusted data reaches an interpreter as part of a command or query, tricking it into running unintended commands or reading data without authorization (PDF p. 7). Detail: A08-001.
9. **API9 Improper Assets Management.** APIs expose more endpoints than traditional web applications, so current documentation and an inventory of hosts and deployed versions matter; without them, deprecated versions and debug endpoints stay exposed (PDF p. 7). Detail: A09-001.
10. **API10 Insufficient Logging & Monitoring.** Weak logging and monitoring, combined with missing or ineffective incident-response integration, let attackers persist, pivot and tamper with, extract or destroy data. The document cites breach studies in which detection takes over 200 days and usually comes from external parties rather than internal monitoring (PDF p. 7). Detail: A10-001.

## When and how to apply
INTERPRETATION: use the ten headings as the outer loop of an API review. For each, open the chapter module, run its "Is the API vulnerable?" questions against the project's endpoints, and record the document's generic scores (A00-006) next to the project-specific evidence.

## Time-sensitive statements
- The numbering and names above are those of the 2019 edition (PDF p. 7). SUPPLEMENTARY: the 2023 edition of the OWASP API Security Top 10 renumbers and renames several entries (source: the OWASP API Security Project); see the note in A00-005.

## Relations
A00-006 defines the scores that head every chapter; A01-001 through A10-001 expand each line of this table.
