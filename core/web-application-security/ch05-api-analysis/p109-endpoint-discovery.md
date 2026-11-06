---
id: WAS-C05-001
title: Endpoint Discovery
source_pages: "109-112"
chapter: 5
concepts: [api-endpoint-discovery, rest-recognition, http-verbs, options-method, endpoint-enumeration, stateless-tokens, permission-to-test]
related: [WAS-C05-002, WAS-C05-003, WAS-C04-010, WAS-C03-002]
time_sensitive: false
---
# Endpoint Discovery
(Source: PDF pp. 109-112)

## What the section covers
The opening of the API analysis chapter. It explains the chapter's purpose, shows how to recognise a REST API from observed traffic, and gives two ways to learn which HTTP verbs an endpoint accepts: the OPTIONS method and trying each verb.

## Chapter framing
API endpoint analysis is the next logical recon skill after subdomain discovery. The questions are which domains the application uses and the fact that each of them may have its own API endpoints. The same techniques as for subdomains apply, namely brute force and dictionary attacks, though manual work and logical analysis are also often rewarded. This is the second step in learning the application's structure, and understanding why an API is exposed shows how it fits the application and what its business purpose is (PDF p. 109).

## Recognising a REST API
- Most enterprise apps use either REST or SOAP, and REST is increasingly the norm for modern applications (PDF p. 109).
- While walking through the app with browser developer tools, watch for requests such as a GET for a user resource, a GET for that user's payments and a POST to the same payments path. Each endpoint names a resource instead of a function, and the nested payments resource belonging to a user shows a hierarchy, another mark of RESTful design (PDF pp. 109-110).
- Headers also give hints. A request that carries an authorization bearer token on every call suggests statelessness, which REST requires: the server should not track its callers (PDF p. 110).

## The verbs REST supports
Table 5-1 maps verbs to usage: POST creates, GET reads, PUT updates or replaces, PATCH updates or modifies, and DELETE deletes. Once the API is known to be REST you can form hypotheses about available endpoints and retry the observed resources with other verbs to see what the API returns (PDF p. 110).

## Method 1: the OPTIONS request
- The HTTP specification defines a method, OPTIONS, whose only job is to describe a resource's supported verbs, so it should be the first thing tried. A request with curl asks for the options of a user resource, and a successful reply is a 200 status with an Allow header listing methods such as HEAD, GET, PUT, DELETE and OPTIONS (PDF p. 110).
- OPTIONS is generally available only on APIs designed for public use, and very few enterprise applications expose it, so it is an easy first attempt but not a robust one (PDF p. 111).

## Method 2: try each verb
Starting from an endpoint already known to accept one verb, expand the same URL to GET, POST, PUT, PATCH and DELETE and see which ones respond (PDF p. 111). A warning box says that trying verbs can delete or alter application data, so explicit permission from the application owner is needed before brute forcing any API (PDF p. 111).

The script the book supplies is browser JavaScript built on the XMLHttpRequest object and works like this (PDF pp. 111-112):
- Given an endpoint URL, it creates one request per verb, sets a form content type and sends it, using one promise per verb.
- When a request completes it reports the verb with the HTTP status. If no response arrives within one second it reports a status of minus one.
- When all promises are done it logs the combined results, from which you read off which verbs have an endpoint.

The author says the actual status code does not matter; what matters is seeing a status code at all. Most servers do not answer a request that maps to no valid endpoint, hence the timeout case. One second is described as plenty of time for an API to respond and the value can be tuned (PDF p. 112).

## Time-sensitive statements
None.

## Relations
Continues the recon sequence from WAS-C04-010; REST background is in WAS-C03-002. The next section moves from verbs to authentication (WAS-C05-002).
