---
id: WAS-C27-006
title: Separation of Concerns for Third-Party Code
source_pages: "310"
chapter: 27
concepts: [separation-of-concerns, isolated-server, json-boundary, principle-of-least-authority, vulnerability-chaining, process-isolation]
related: [WAS-C27-005, WAS-C27-007, WAS-C25-006]
time_sensitive: false
---
# Separation of Concerns for Third-Party Code
(Source: PDF p. 310)

## What the section covers
Running third-party code apart from the main application so that a compromised dependency has little to take over.

## Why it matters
Third-party code running on the main application server may have side effects. If it is compromised and the principle of least authority is not correctly applied, it may be able to take over system resources and functionality (PDF p. 310).

## How it works
- Run the third-party integration on its own server, ideally one maintained by the organization (PDF p. 310).
- Have the application server talk to it over HTTP, sending and receiving JSON payloads (PDF p. 310).
- The JSON format means script execution on the application server is not possible without additional vulnerabilities, which the book calls vulnerability chaining. The dependency can then be treated more like a "pure function", provided no state is persisted on the dependency server (PDF p. 310).
- The idea can be used elsewhere. A single server could run several modules with process and memory boundaries set by the hardware, so that a risky package struggles to reach the main application's resources and functionality (PDF p. 310).

## Limitations and trade-offs
- Confidential data sent to the dependency server could still be modified, and potentially recorded if the firewall is badly configured, should the package be compromised (PDF p. 310).
- The technique lowers application performance, because functions take longer to return data when they travel over the network (PDF p. 310).

## Relations
Applies the principle of least authority from WAS-C25-006; the package management technique that complements it is WAS-C27-007.
