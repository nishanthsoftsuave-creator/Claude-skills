---
id: WAS-C19-004
title: Where to Start a Security Review
source_pages: "241-242"
chapter: 19
concepts: [review-order, client-first-review, api-layer-review, dependency-tracing, exposed-apis, risk-prioritization, review-framework]
related: [WAS-C19-003, WAS-C19-005, WAS-C07-003]
time_sensitive: false
---
# Where to Start a Security Review
(Source: PDF pp. 241-242)

## What the section covers
A five-step order for reading a codebase in a security review when the highest-risk parts are not yet known, with the reasoning behind starting at the client.

## Meaning and why a framework is needed
- Ideally the review begins with the highest-risk components. But a reviewer may not know which they are when asked to review an application they did not design, which is common in consulting and on existing products (PDF p. 241).
- The author offers a framework to simplify getting started, to use until the reviewer knows the application well enough to rank features by risk.
- Take a basic web application with a client in the browser and a server. Starting with the server code is possible, but the server may hold functionality not exposed to the client. Without knowing what is intended for users, as against internal methods, effort could go to lower-risk code while high-risk code waits.
- In an ideal world every piece of code would be reviewed equally. In practice deadlines and other projects intervene.

## How it works: the five steps
1. Start where the client makes requests to the server. Reading the client shows the surface area, what data moves between client and server, whether several servers are used, and how payloads are interpreted by the server. Evaluate the client-side code to learn the business logic and what users can do (PDF pp. 241-242).
2. Follow the client's API calls back to the server and evaluate the calls that connect them. This shows which dependencies the API layer relies on.
3. Trace helper methods, dependencies and the functionality those APIs use, such as databases, logs, uploaded files and conversion libraries, whether called directly or through a helper.
4. Cover functionality that could be exposed to the client but is not called directly, for example APIs built for upcoming features or ones exposed by accident that should be internal.
5. Spend the remaining time on the rest of the codebase, choosing the route by analyzing business logic and the risks such an application would face. Familiarity gained earlier makes this easy.

## When and how to apply
- The book says this is not the only way, and applications with niche security needs may call for another path. It recommends this one because it builds familiarity at a natural pace and puts user-facing functionality first, leaving potentially low-risk functionality for the end (PDF p. 242).
- As the reviewer learns the process and the application, the guidelines can be adapted to the application and the risks it faces.

## Relations
Follows the discussion of what to look for (WAS-C19-003). The anti-patterns that a reviewer should recognize along the way start in WAS-C19-005. The same idea of mapping layers appears in the architecture chapter on weak points (WAS-C07-003).
