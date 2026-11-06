---
id: WAS-C25-008
title: Summary - Defending Against Injection
source_pages: "298-300"
chapter: 25
concepts: [injection-summary, sql-mitigations, least-authority, command-whitelist, security-first-architecture, review-team]
related: [WAS-C25-003, WAS-C25-006, WAS-C25-007]
time_sensitive: false
---
# Summary: Defending Against Injection
(Source: PDF pp. 298-300; p. 300 is blank)

## What the section covers
The chapter's closing summary. It starts at the bottom of one page, after the whitelisting discussion, and finishes on the next.

## Key points
- Injection is classically tied to databases, SQL in particular. Databases are vulnerable without well-written code and configuration, but any CLI that an API endpoint or dependency talks to can also be a victim (PDF p. 298).
- Major SQL databases offer mitigations against SQL injection, yet it remains possible with weak architecture and badly written client-to-server code (PDF p. 299).
- Adopting least authority limits the damage to the organization and its infrastructure after a breach. A security-first architecture never lets a client supply a query or command that the server executes (PDF p. 299).
- When user input has to become server-side operations, the allowed operations should be whitelisted so only a vetted subset is available, vetted by a responsible security review team. With these controls, injection-style vulnerabilities become much less likely (PDF p. 299).

## Relations
Summarizes WAS-C25-003 (prepared statements), WAS-C25-006 (least authority) and WAS-C25-007 (whitelisting). The final page in the range is blank in the source.
