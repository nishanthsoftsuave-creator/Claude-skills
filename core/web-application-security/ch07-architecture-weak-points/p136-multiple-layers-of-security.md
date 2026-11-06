---
id: WAS-C07-003
title: Multiple Layers of Security
source_pages: "136"
chapter: 7
concepts: [defense-in-depth, security-layers, weakest-link, bulk-api, headless-browser, input-sanitization, prioritizing-targets]
related: [WAS-C07-002, WAS-C10-003, WAS-C07-004]
time_sensitive: false
---
# Multiple Layers of Security
(Source: PDF p. 136; the end of the section is on PDF p. 137)

## What the section covers
Why a vulnerability can be blocked or missed at several layers of an application, and how to use the number of layers to choose where to test first.

## Meaning
- In the messaging example five layers could each carry XSS risk: API POST, database write, database read, API GET and client read (PDF p. 136).
- The same holds for other vulnerability types such as XXE or CSRF: each can arise when mechanisms are missing at more than one layer (PDF p. 136).

## How it works
- Suppose the application adds sanitisation at the API POST layer. XSS through that layer may now be impossible (PDF p. 136).
- Later a new POST endpoint accepts a list of messages for bulk messaging. If its sanitisation is weaker, it can store script in the database and bypass the intent of the single-message endpoint (PDF p. 136).
- The book's point is that an application is only as secure as the weakest link in its architecture. Had protections also existed at the database write stage, the new attack would have been blocked (PDF p. 136).
- Layers can offer different defences. The POST layer could launch a headless browser, simulate rendering the message, and reject it if any script runs (PDF p. 136). Such a check is not possible at the database or client layer (PDF p. 137).
- Different mechanisms catch different payloads. A browser-specific bug could let a script slip past the headless browser and run only in a user's vulnerable browser version, which differs from the one used on the server (PDF p. 137).

## When and how to apply
- The most secure applications add mechanisms at many layers; insecure ones at only one or two (PDF p. 137).
- When testing, look for functionality with few mechanisms, or with many layers, since it has a lower ratio of mechanisms to layers. Prioritise it, because it is more likely to be exploitable (PDF p. 137).

## Relations
Builds on WAS-C07-002. See WAS-C10-003 for stored XSS and WAS-C07-004 for the next architecture risk factor.
