---
id: A01-001
title: API1:2019 Broken Object Level Authorization
source_pages: "8-9"
chapter: api1
concepts: [broken-object-level-authorization, bola, idor, object-identifiers, authorization-checks, account-takeover, guid-identifiers, authorization-tests]
related: [A00-006, A00-007, A05-001, A03-001]
time_sensitive: false
---
# API1:2019 Broken Object Level Authorization
(Source: PDF pp. 8-9)

## What the section covers
The first and, by the document's own account, most common and most damaging API risk: endpoints that accept an object identifier from the client and act on that object without checking that the caller is allowed to. The chapter gives the risk scores, explains why the flaw is so frequent in APIs, defines the check that is missing, walks through two attack scenarios and lists the preventions.

## Risk scores
Exploitability 3, prevalence 3, detectability 2, technical impact 3; business impact is business-specific (PDF p. 8). (Scales: A00-006.)

## Meaning
- **Object level authorization** is an access-control mechanism, usually implemented in application code, that confirms a user can only reach the objects they are entitled to (PDF p. 8).
- The rule the document states: every API endpoint that receives an object's ID and performs any kind of action on it should run an object-level authorization check, confirming that the logged-in user may perform the requested action on the requested object (PDF p. 8).
- When the check is absent, the usual outcome is unauthorized disclosure, modification or destruction of all data reachable through the endpoint (PDF p. 8).

## Why it matters
- Threat agents and attack vectors: the attacker simply changes the ID of an object inside a request. This is extremely common in API-based applications because the server component usually does not fully track the client's state; instead it relies on parameters such as object IDs sent by the client to decide which objects to access (PDF p. 8).
- Security weakness: the document calls this the most common and most impactful attack on APIs. Authorization and access control in modern applications are complex and spread across the code base. Even where a proper authorization infrastructure exists, developers may forget to call it before touching a sensitive object. Access-control flaws are not usually something automated static or dynamic testing can find (PDF p. 8).
- Impacts: data disclosure to unauthorized parties, data loss or data manipulation; unauthorized access to objects can escalate to full account takeover (PDF p. 8).

## How it works: the attack scenarios
1. **Hosted shops' revenue data.** An e-commerce platform that hosts online shops shows each shop a page of revenue charts. By inspecting browser requests the attacker finds the data endpoint for those charts and its pattern, a path of the form `/shops/{shopName}/revenue_data.json`. A different endpoint returns the names of all hosted shops. A simple script that substitutes each name into the path yields the sales data of thousands of stores (PDF p. 8).
2. **Wearable device, custom user header.** Watching a wearable's network traffic, the attacker notices an HTTP PATCH request carrying a custom header `X-User-Id` with the value 54796. Changing it to 54795 produces a successful response and lets the attacker modify another user's account data (PDF p. 8).

## How to prevent
- Build a proper authorization mechanism that rests on the user policies and the user hierarchy (PDF p. 9).
- Call that mechanism, in every function that uses client input to reach a database record, to check whether the logged-in user may perform the requested action on that record (PDF p. 9).
- Prefer random, unpredictable values such as GUIDs as record identifiers (PDF p. 9).
- Write tests that exercise the authorization mechanism, and do not deploy vulnerable changes that make those tests fail (PDF p. 9).

## When and how to apply
INTERPRETATION: a review should enumerate every endpoint that takes an identifier anywhere (path, query string, header or body), then exercise each one with two accounts, swapping the identifiers, and record which endpoints answer successfully for the wrong account. Predictable sequential identifiers, like the user ids in scenario 2, make enumeration trivial, so note the ID format as a separate observation. Because the document says automated tools rarely find this class of flaw, a clean scanner result is not evidence of absence.

## References the section lists
CWE-284 Improper Access Control, CWE-285 Improper Authorization and CWE-639 Authorization Bypass Through User-Controlled Key (PDF p. 9).

## Relations
A05-001 is the function-level counterpart (who may call which operation rather than which object); A03-001 covers responses that leak more than the caller should see even when the object check passes; A06-001 covers writes that set properties the caller should not control; A00-007 holds the one-line summary of this risk.
