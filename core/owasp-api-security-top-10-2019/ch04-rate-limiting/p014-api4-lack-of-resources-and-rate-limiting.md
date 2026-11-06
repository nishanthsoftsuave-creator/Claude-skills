---
id: A04-001
title: API4:2019 Lack of Resources & Rate Limiting
source_pages: "14-15"
chapter: api4
concepts: [rate-limiting, resource-limits, denial-of-service, payload-size-limits, pagination-limits, execution-timeouts, container-resource-limits, brute-force]
related: [A00-006, A00-007, A02-001, A09-001]
time_sensitive: false
---
# API4:2019 Lack of Resources & Rate Limiting
(Source: PDF pp. 14-15)

## What the section covers
APIs that let a client consume unbounded resources, either by sending very many requests or by making single requests that are expensive to serve. The chapter lists the limits whose absence makes an API vulnerable, gives two denial-of-service scenarios and the preventions.

## Risk scores
Exploitability 2, prevalence 3, detectability 3, technical impact 2; business impact is business-specific (PDF p. 14). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: exploitation only needs ordinary API requests and no authentication. Many concurrent requests can come from one local machine or from rented cloud computing resources (PDF p. 14).
- Security weakness: it is common to find APIs with no rate limiting at all, or with limits set incorrectly (PDF p. 14).
- Impacts: denial of service (DoS), leaving the API unresponsive or unavailable (PDF p. 14).

## Is the API vulnerable?
Every request consumes network, CPU, memory and storage. How much depends heavily on user input and the endpoint's business logic, and requests from many clients compete for the same resources. The API is vulnerable if at least one of the following limits is missing or set inappropriately, whether too low or too high (PDF p. 14):
- execution timeouts;
- maximum allocatable memory;
- number of file descriptors;
- number of processes;
- request payload size, for example uploads;
- number of requests per client or per resource;
- number of records per page returned in a single response.

## How it works: the attack scenarios
1. **Thumbnail generation exhausts memory.** The attacker uploads a very large image through an images endpoint. After the upload the API builds several thumbnails of different sizes; the image is so large that memory runs out during thumbnail creation and the API stops responding (PDF p. 14).
2. **Page size set to 200,000.** A UI lists users 200 per page and fetches them with a query such as `/api/users?page=1&size=200`. The attacker changes the size parameter to 200,000, which causes performance problems in the database; meanwhile the API cannot serve this or any other client, which is a DoS. The document adds that the same move can be used to trigger integer-overflow or buffer-overflow errors (PDF p. 14).

## How to prevent
The document's list (PDF p. 15):
- Docker makes it easy to limit memory, CPU, number of restarts, file descriptors and processes.
- Limit how often a client may call the API within a defined time frame.
- When the limit is exceeded, tell the client the limit and the time at which it resets.
- Validate query-string and body parameters on the server, in particular the one that controls how many records a response returns.
- Define and enforce a maximum size for every incoming parameter and payload, such as the maximum length of strings and the maximum number of elements in arrays.

## When and how to apply
INTERPRETATION: for each endpoint record whether a per-client request limit exists and what the limit response looks like, then inspect every parameter that controls output size or upload size for a server-side ceiling. Load probes run only against the user's own non-production system with approval, and the document gives no numeric limits, so any threshold used in a finding is the project's.

## References the section lists
OWASP: Blocking Brute Force Attacks, the Docker Cheat Sheet section on limiting resources (memory, CPU, file descriptors, processes, restarts) and the REST Assessment Cheat Sheet. External: CWE-307 Improper Restriction of Excessive Authentication Attempts, CWE-770 Allocation of Resources Without Limits or Throttling, and the "Rate Limiting (Throttling)" part of NIST's Security Strategies for Microservices-based Application Systems (PDF p. 15).

## Relations
A02-001 requires stricter limits on authentication endpoints than the general ones described here; A09-001 shows a rate limit implemented outside the API code and therefore missing on a second host; A08-001 recommends capping returned records to blunt mass disclosure after an injection; A00-007 holds the one-line summary.
