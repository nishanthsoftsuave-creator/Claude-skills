---
id: WAS-C09-002
title: Applied Recon
source_pages: "146-148"
chapter: 9
concepts: [applied-recon, rest-api-types, endpoint-discovery, authentication-scheme, third-party-exploits, exploit-delivery-paths, code-reuse]
related: [WAS-C09-001, WAS-C05-001, WAS-C05-002, WAS-C06-001, WAS-C07-002]
time_sensitive: false
---
# Applied Recon
(Source: PDF pp. 146-147; PDF p. 148 is blank)

## What the section covers
How each recon skill from Part I is used when you move to exploitation.

## Meaning
- Part I taught how to scout an application and learn its underlying technology and structure; this part is about exploiting security holes in the same applications. The lessons stay important (PDF p. 146).

## How it works: recon skills reused
- **API type.** Part I showed how to work out what API type an application uses to serve its browser client, and most modern ones use REST. The coming examples mostly send a payload over a REST API, so knowing a target's API type matters (PDF pp. 146-147).
- **Endpoint discovery.** Public records and network scripts found undocumented endpoints. Exploits written in this part apply to many applications, and it can pay to try one exploit against several applications of the same owner, since code reuse may carry a flaw to internal applications found earlier. Several endpoints may take similarly shaped payloads; an attack on a user's friends route may reveal nothing sensitive while the settings route could (PDF p. 147).
- **Authentication scheme.** Knowing it is crucial. Most applications give authenticated users a superset of guest functionality, so a token opens more APIs to attack, and the privileges of the resulting processes are probably higher (PDF p. 147).
- **Third-party dependencies.** Part I showed how to identify third-party dependencies, often open source. Here you learn to find and adapt publicly documented exploits against them, and sometimes find holes from the mix of custom and third-party code (PDF p. 147).
- **Architecture.** If application A cannot be exploited but B can, and you cannot reach B directly, you may look at how A talks to B and find a way to deliver a payload to A that A later passes on (PDF p. 147).

## Why it matters
The book concludes that recon and hacking skills go hand in hand and are far more valuable together than apart (PDF p. 147).

## Relations
Reuses WAS-C05-001 (endpoints), WAS-C05-002 (authentication), WAS-C06-001 (dependencies) and WAS-C07-002 (architecture); follows WAS-C09-001.
