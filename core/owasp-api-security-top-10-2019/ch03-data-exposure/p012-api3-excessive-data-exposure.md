---
id: A03-001
title: API3:2019 Excessive Data Exposure
source_pages: "12-13"
chapter: api3
concepts: [excessive-data-exposure, client-side-filtering, generic-serialization, pii, response-schema-validation, data-classification, traffic-sniffing]
related: [A00-006, A00-007, A01-001]
time_sensitive: false
---
# API3:2019 Excessive Data Exposure
(Source: PDF pp. 12-13)

## What the section covers
APIs that return more data than the consumer should see and leave it to the client to hide the rest. The chapter explains why this happens, why scanners miss it, gives two scenarios and lists the preventions.

## Risk scores
Exploitability 3, prevalence 2, detectability 2, technical impact 2; business impact is business-specific (PDF p. 12). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: exploitation is simple. The attacker sniffs the traffic and reads the API responses looking for sensitive data that should never have been sent to the user (PDF p. 12).
- Security weakness: APIs rely on clients to filter data. Because an API is a data source, developers sometimes write it generically without thinking about how sensitive each field is. Automated tools usually cannot detect this class of problem, because telling legitimate response data from sensitive data that should not be returned requires a deep understanding of the application (PDF p. 12).
- Impacts: the usual consequence is exposure of sensitive data (PDF p. 12).

## Is the API vulnerable?
The API returns sensitive data to the client by design, expecting the client to filter it before display. An attacker can read the raw traffic and sees everything (PDF p. 12).

## How it works: the attack scenarios
1. **Comment metadata that carries author PII.** A mobile team renders comment metadata from an endpoint of the form `/api/articles/{articleId}/comments/{commentId}`. Sniffing the app's traffic shows that the response also includes sensitive data about the comment's author, because the implementation serialises the User model with a generic `toJSON()` method that includes PII (PDF p. 12).
2. **Camera list for a security guard.** An IoT surveillance system lets administrators create users with different permissions. An administrator creates an account for a new guard who should only see cameras in specific buildings. The guard's mobile app calls a cameras endpoint for the site and the response lists every camera with an id, a live-access token and a building id. The client GUI shows only the guard's cameras, but the API response contains the full list for the whole site, tokens included (PDF p. 12).

## How to prevent
The document's list (PDF p. 13):
- Never rely on the client side to filter sensitive data.
- Review the API's responses to make sure they contain only legitimate data.
- Back-end engineers should always ask "who is the consumer of the data?" before exposing a new endpoint.
- Avoid generic serialisation methods such as `to_json()` and `to_string()`; pick the specific properties to return.
- Classify the sensitive and personally identifiable information the application stores and processes, and review every API call that returns such information to see whether the response is a security problem.
- Add schema-based response validation as an extra layer: define and enforce the data returned by every API method, including error responses.

## When and how to apply
INTERPRETATION: capture the raw responses of each endpoint with a proxy on a non-production copy and diff them against what the UI shows; every field present in the response but absent from the screen is a candidate finding. Pay special attention to credentials, tokens and other users' records in list responses, as in scenario 2.

## References the section lists
CWE-213 Intentional Information Exposure (PDF p. 13).

## Relations
A01-001 is the related case where the caller reaches an object it may not see at all; A06-001 is the write-side mirror image, where generic binding lets the client set fields it should not; A07-001 covers verbose error responses, another form of over-disclosure; A00-007 holds the one-line summary.
