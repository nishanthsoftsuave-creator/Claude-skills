---
id: WAS-C05-005
title: Summary - API Analysis
source_pages: "116-118"
chapter: 5
concepts: [chapter-summary, api-endpoints, endpoint-shapes, recon-prioritization, application-function, recon-map]
related: [WAS-C05-001, WAS-C05-003, WAS-C05-004, WAS-C04-010]
time_sensitive: false
---
# Summary: API Analysis
(Source: PDF pp. 116-117; the last page of the row is blank)

## What the section covers
The closing lessons of the API analysis chapter: why finding endpoints comes right after finding subdomains, and what finding their payload shapes adds.

## Main points
- After building a mental model of the subdomains that power an application, ideally also written down, the next step is to find the API endpoints hosted on them so their purpose can be determined later (PDF p. 116).
- The step sounds simple, but it is crucial. Without it you may spend time hunting for holes in well-secured endpoints while less-secure endpoints with similar functionality or data exist elsewhere (PDF p. 116).
- Finding endpoints is also one step toward understanding what an API does, if you do not already know its intended use (PDF p. 116).
- With a number of endpoints found and documented, working out the shape of the payloads they accept is the next logical step. A mix of educated guesses, automation and analysis of common endpoint archetypes, as practised in the chapter, will eventually reveal the data endpoints expect and what they send back (PDF p. 117).
- Knowing that makes you understand the function of the application, described as the first major step toward breaking or securing it (PDF p. 117).

## Why it matters
Prioritisation is the thread: skipping this step risks effort spent on well-secured endpoints while weaker ones with similar functionality or data sit untouched (PDF p. 116).

INTERPRETATION: record, for every endpoint, its host, verb, authentication scheme and payload shape in the recon map, because those four facts are what the chapter's techniques produce and what later attack or review work needs.

## Relations
Techniques summarised: WAS-C05-001 (verbs and endpoint discovery), WAS-C05-002 (authentication), WAS-C05-003 and WAS-C05-004 (payload shapes). It follows the subdomain work in WAS-C04-010, and the book's next chapter turns to identifying third-party dependencies.
