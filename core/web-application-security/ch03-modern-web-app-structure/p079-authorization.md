---
id: WAS-C03-014
title: Authorization
source_pages: "79"
chapter: 3
concepts: [authorization, centralized-authorization, per-api-checks, human-error, privileged-resources, access-control, business-logic]
related: [WAS-C03-013, WAS-C03-012, WAS-C19-003]
time_sensitive: false
---
# Authorization
(Source: PDF p. 79 from the "Authorization" heading, plus the top of PDF p. 80 above "Web Servers")

## What the section covers
Authorization as the step after authentication, how well-designed applications centralise it, and which resources should always be checked.

## Meaning and position
Authorization is the next step after authentication. It is harder to categorise than authentication because it depends heavily on the business logic inside the web application (PDF p. 79).

## How it is designed
- Well-designed applications generally have a centralised authorization class responsible for deciding whether a user may reach a given resource or function (PDF p. 79).
- Poorly written APIs implement checks on a per-API basis and manually reproduce authorization functionality. If you can tell that an application reimplements the checks in every API, the book says it will likely have several APIs where the checks are not sufficient, simply because of human error (PDF p. 79).

## Resources that should always be checked
The book lists the common resources that should always have authorization checks (PDF p. 80):
- settings and profile updates;
- password resets;
- private message reads and writes;
- any paid functionality;
- any elevated user functionality, such as moderation functions.

## When and how to apply
INTERPRETATION: a quick recon signal is whether similar endpoints reject unauthorised users in the same way (a shared check) or inconsistently (per-endpoint checks). Inconsistency points to places worth testing first. The book's architecture chapter makes the same argument about consistent versus per-feature defences.

## Limitations
The signal about per-API checks is a heuristic from the book, not a guarantee that any one API is flawed.

## Relations
Follows authentication in WAS-C03-013 and shares the lead-in in WAS-C03-012. Logic-level bugs such as missing authorization checks are discussed in code review terms in WAS-C19-003.
