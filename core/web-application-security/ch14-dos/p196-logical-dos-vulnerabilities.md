---
id: WAS-C14-003
title: Logical DoS Vulnerabilities
source_pages: "196-198"
chapter: 14
concepts: [logical-dos, resource-consumption, synchronous-operations, database-joins, response-time-measurement, account-scaling, api-load]
related: [WAS-C14-002, WAS-C14-004, WAS-C26-003]
time_sensitive: false
---
# Logical DoS Vulnerabilities
(Source: PDF pp. 196-198, tail page 199)

## What the section covers
DoS that arises from application logic rather than a malformed pattern: how one illegitimate user can drain server resources, which operations are resource intensive, how response times can be estimated without server access, and a photo-sharing example in which an endpoint's cost grows with the size of an account.

## Meaning
- In a logical DoS, server resources are drained by an illegitimate user, so legitimate users see degraded performance or lose service (PDF p. 196).
- Figure 14-1 (PDF p. 197) shows a malicious user repeatedly calling an API with high compute cost, while a legitimate user trying to request services finds them unavailable or slow.
- Regex is an easy way into DoS because it gives a centralized place to look, anywhere a regex parser exists. The book stresses that DoS vulnerabilities can appear in almost any kind of software (PDF p. 197).
- Logical DoS is among the hardest kinds to find and exploit, yet appears in the wild more often than expected. It takes some expertise to pin down, but after finding a few, a tester will probably find many (PDF p. 197).

## Why it matters
DoS depends on consuming server or client hardware resources and leaving them unavailable for legitimate use, so the first step is to look for resource-intensive operations in an application (PDF p. 197).

## How it works: finding costly operations
- The book's non-exhaustive list of costly occurrences: any operation confirmed to run synchronously, database writes, drive writes, SQL joins, file backups and looping logical operations. Complex API calls often contain several of these (PDF p. 197).
- Example: a photo-sharing upload route might do a database write for photo metadata, a drive write to log the upload, a SQL join to gather user and album data for the metadata write, and a file backup in case of server failure (PDF pp. 197-198).
- Without server access, operation durations cannot be measured directly, but timing plus estimation helps. One approach is to time the whole request using browser developer tools (PDF p. 198).
- To test whether an operation is synchronous on the server, make the same request several times at once and see whether the responses are staggered. The book recommends scripting this and averaging around one hundred calls so that random effects, such as a traffic spike or a resource-heavy scheduled job, do not distort the measurement (PDF p. 198).
- The structure of backend code can also be inferred from network payloads and the user interface. In the example the application has users, albums (a user has albums), photos (an album has photos) and metadata (photos have metadata), each child referenced by an id. Different tables or documents are likely. An interface request that returns all metadata for a user therefore implies a complex join or iterative query on the backend, at an endpoint of the form metadata/userid (PDF p. 198).
- The cost of that operation varies with usage: a power user needs significant hardware resources, a new user does not (PDF p. 198).

## Evaluation: how the cost scales (printed on the tail page)
- Table 14-3 (PDF p. 199) lists response time of that metadata endpoint by account type: a new account with 1 album and 1 photo takes 120 ms, an average account with 6 albums and 60 photos takes 470 ms, and a power user with 28 albums and 490 photos takes 1,870 ms.
- From this the book reasons that a very large account would make each request costly; it imagines a client-side script that re-uploads the same or similar images into many albums until one account holds about 600 albums and 3,500 photos (PDF p. 199).
- It then concludes that repeated requests to that endpoint would noticeably lower server performance for other users, unless the server code limits resources per request. Requests might simply time out while the database still spends resources on them after the server has stopped waiting (PDF p. 199).
- The book closes by saying this is only an example of how logical DoS is found; such attacks differ case by case, defined by the logic of the particular application (PDF p. 199).

## When and how to apply
INTERPRETATION: when assessing your own application, measure response time against data volume for each endpoint that aggregates data, and compare account archetypes to see where cost is unbounded.

## Relations
Follows ReDoS (WAS-C14-002) and precedes distributed DoS (WAS-C14-004). Defenses are in WAS-C26-003.
