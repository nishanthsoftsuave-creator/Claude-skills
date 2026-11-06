---
id: WAS-C03-002
title: REST APIs
source_pages: "61-63"
chapter: 3
concepts: [rest, rest-api, stateless-api, http-verbs, swagger, soap, xml-vs-json, api-endpoint-design, cacheable-api]
related: [WAS-C03-001, WAS-C03-003, WAS-C05-001, WAS-C12-001]
time_sensitive: false
---
# REST APIs
(Source: PDF pp. 61-63)

## What the section covers
What REST means, the traits that make an API RESTful, how endpoint naming and HTTP verbs line up, how Swagger documents such APIs, and why REST (usually carrying JSON) displaced SOAP (carrying XML).

## Meaning
REST stands for Representational State Transfer. The book describes it as a "fancy way" of defining an API with a few distinctive traits (PDF p. 61):
- **Separate from the client.** REST APIs are built for scalable but simple applications. The client requests resources from the API by following a strict API structure, but cannot call a database or run server-side logic itself.
- **Stateless.** The API only takes inputs and returns outputs and must not store state about the client's connection. It can still perform authentication and authorization, but the authorization should be tokenized and sent on every request.
- **Easily cacheable.** To scale on the internet, responses must be easy to mark as cacheable or not. Because REST defines tightly what data each endpoint serves, this is simple to configure. The caches should ideally be managed programmatically so that privileged information is not leaked to another user (PDF pp. 61-62).
- **Each endpoint defines a specific object or method.** Endpoints are usually hierarchical, for example a path naming a moderator and then one of that moderator's logs by date. This lets the HTTP verbs GET, POST, PUT and DELETE act on the same path, so one endpoint with several verbs documents itself (PDF p. 62).

## How it works: verbs and paths
- The book's example: to modify the moderator account "joe" you would use PUT on the moderators/joe path. To delete the log dated 12_21_2018 you would use DELETE on moderators/joe/logs/12_21_2018, which follows by simple deduction (PDF p. 62).
- Because REST follows a well-defined pattern, tools such as Swagger can integrate and generate documentation of the endpoints, which makes an endpoint's intent easy for other developers to pick up (PDF p. 62).
- Figure 3-1 (rendered and read) is a Swagger page for a "pet" API served over HTTPS with an Authorize button. It lists colour-coded rows: POST for adding a pet, PUT for updating one, GET find-by-status, a struck-through (deprecated) GET find-by-tags, GET and POST on a single pet by id, DELETE a pet, and POST upload-image under a pet id. Each row has a lock icon (PDF p. 62).

## REST versus SOAP
- In the past most web applications used SOAP (Simple Object Access Protocol) APIs. The book gives three REST advantages: requests target data rather than functions, requests are easy to cache, and the design scales well (PDF p. 62).
- SOAP must use XML as its in-transit format. REST can carry any format but typically uses JSON, which is more lightweight (less verbose) and easier for humans to read than XML (PDF pp. 62-63). The two examples below show the difference.
- Example payload: the same user record is shown twice (PDF p. 63). It holds a username (joe), a password, an email, a joined date (12/21/2005) and a nested client-data block with timezone, operating system and a licenses sub-block (video editor and image editor licence keys). In XML each field is a pair of tags with an element per level. In JSON it is a set of quoted keys, braces for nesting, and no closing tags, so it is visibly shorter. The password in the sample is a plain illustrative string.

## Why it matters
- Most modern applications you meet use RESTful or REST-like APIs that serve JSON. SOAP and XML are increasingly rare outside specific enterprise applications that keep a rigid design for legacy compatibility (PDF p. 63).
- Understanding REST structure helps when reverse engineering an application's API layer, because many target APIs follow it. Many tools you may integrate with will also be exposed via REST APIs (PDF p. 63).

## When and how to apply
INTERPRETATION: when you see requests whose paths name resources and nest them, with a token on each request, treat the API as REST and guess further endpoints and verbs from the pattern (the next chapter builds on this).

## Relations
JSON, the usual REST format, is covered next (WAS-C03-003). Endpoint discovery using these patterns is in WAS-C05-001. The XML side matters again for XXE attacks (WAS-C12-001).
