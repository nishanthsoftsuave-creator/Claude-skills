---
id: A09-001
title: API9:2019 Improper Assets Management
source_pages: "24-25"
chapter: api9
concepts: [improper-assets-management, api-inventory, deprecated-api-versions, documentation, openapi, non-production-hosts, data-flow, retirement-plan, api-firewall]
related: [A00-006, A00-007, A02-001, A04-001]
time_sensitive: false
---
# API9:2019 Improper Assets Management
(Source: PDF pp. 24-25)

## What the section covers
The risk of not knowing which API hosts, versions and integrations exist, so that old, beta or debug deployments stay reachable and unprotected. The chapter gives the risk scores, a list of questions an owner should be able to answer, two scenarios and a prevention list built around inventory and documentation.

## Risk scores
Exploitability 3, prevalence 3, detectability 2, technical impact 2; business impact is business-specific (PDF p. 24). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: old API versions are usually unpatched, which gives attackers an easy way in without having to defeat the modern protections that guard the newest version (PDF p. 24).
- Security weakness: outdated documentation makes vulnerabilities harder to find and fix. Without an asset inventory and a retirement strategy, unpatched systems keep running and sensitive data leaks. Modern practices such as microservices, cloud computing and Kubernetes make services easy to deploy independently, so unnecessarily exposed API hosts are common (PDF p. 24).
- Impacts: attackers can reach sensitive data, or even take over the server, through old unpatched versions connected to the same database (PDF p. 24).

## Is the API vulnerable?
The API might be vulnerable if (PDF p. 24):
- the purpose of an API host is unclear and nobody can answer which environment it runs in (production, staging, test, development), who should have network access to it (public, internal, partners), which version is running, what data it collects and processes (for example PII), and what the data flow is;
- documentation is missing or out of date;
- there is no retirement plan for each API version;
- the hosts inventory is missing or outdated;
- the inventory of integrated first- or third-party services is missing or outdated;
- old or previous API versions are running unpatched.

## How it works: the attack scenarios
1. **The forgotten v1.** After redesigning its applications, a local search service left an old API version running without protection and with access to the user database. An attacker targeting the newest application found the address of the current version, replaced the version number in the URL with the old one, and reached the unprotected API, exposing the PII of over 100 million users (PDF p. 24).
2. **The beta host without the rate limit.** A social network blocked brute-force guessing of password-reset tokens with a rate limiter that sat in a separate component in front of the official API rather than in the API code. A researcher found a beta host running the same API, including password reset, but without that component in front of it. A simple brute force of the six-digit token let the researcher reset any user's password (PDF p. 24).

## How to prevent
The document's list (PDF p. 25):
- Inventory all API hosts and record for each the environment, who should be able to reach it over the network, and the API version.
- Inventory integrated services and record their role, what data is exchanged (the data flow) and how sensitive it is.
- Document every aspect of the API: authentication, errors, redirects, rate limiting, the CORS policy and the endpoints with their parameters, requests and responses.
- Generate documentation automatically by adopting open standards, and put the documentation build in the CI/CD pipeline.
- Make the documentation available to those authorized to use the API.
- Apply external protections such as API security firewalls to every exposed version, not just the current production one.
- Avoid production data in non-production deployments; where that is unavoidable, give those endpoints the same security treatment as production.
- When a newer version contains security improvements, run a risk analysis to decide what to do with older versions: whether the improvements can be back-ported without breaking compatibility, or whether the old version must be withdrawn quickly and clients forced onto the latest one.

## When and how to apply
INTERPRETATION: start a review by asking for the host and version inventory and comparing it with what DNS, the deployment configuration and the gateway routes actually show; any host or version present in the second set but missing from the first is a finding in its own right. Then check each non-production host for the protections that production gets, as in scenario 2, where a control placed outside the code did not follow the code to the beta host.

## References the section lists
CWE-1059 Incomplete Documentation and the OpenAPI Initiative (PDF p. 25).

## Relations
A02-001 describes the reset-token brute force that scenario 2 completes on an unprotected host; A04-001 covers rate limiting generally; A07-001 covers hardening and patching, which forgotten hosts typically lack; A00-007 holds the one-line summary.
