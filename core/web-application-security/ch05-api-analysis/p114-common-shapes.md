---
id: WAS-C05-003
title: Endpoint Shapes - Common Shapes
source_pages: "114"
chapter: 5
concepts: [endpoint-shapes, payload-shape, oauth2-parameters, public-specifications, api-documentation, common-archetypes, recon-map]
related: [WAS-C05-002, WAS-C05-004, WAS-C05-001]
time_sensitive: true
---
# Endpoint Shapes: Common Shapes
(Source: PDF p. 114, with the end of the section on the top and middle of PDF p. 115)

## What the section covers
The start of the discussion of endpoint shapes, meaning the structure of the payload an API endpoint expects. This row covers the heading text that frames the topic and the case where the shape is predictable because it follows a public standard, using OAuth 2.0 as the example. The opening lines at the top of the page belong to the authentication section (WAS-C05-002).

## Framing
Once you have found subdomains and the HTTP APIs inside them, you determine the HTTP verbs used per resource and add the findings to the application map. With a comprehensive list of subdomains, APIs and verbs in hand, the next question is how to learn what type of payload any given API expects (PDF p. 114).

## Meaning
- Sometimes the answer is easy because many APIs expect payload shapes that are common across the industry (PDF p. 114).
- Example: an authorization endpoint that is part of an OAuth 2.0 flow expects a response type (a code), a client identifier, a list of scopes, a state value and a redirect URI (PDF pp. 114-115).

## How it works
- OAuth 2.0 is a widely implemented public specification, so the data an authorization endpoint needs can usually be found by combining educated guesses with the public documentation. Naming conventions and scope lists can vary between implementations, but the overall payload shape should not (PDF p. 115).
- Discord's public documentation shows its OAuth 2.0 endpoint as a request path whose query string contains the response type set to code, a client id, the scopes (for example identify and guilds.join), a state value, a redirect URI and a prompt value of consent. All of the first five are part of the official specification (PDF p. 115).
- Facebook's documentation describes a very similar request for the same function, with the app id, redirect URI, app secret and code parameter (PDF p. 115).

## Limitations
The conclusion is that finding the shape is not complex for common archetypes. However, many APIs that follow a public spec such as OAuth do not use a common specification for their internal APIs that run application logic, which is the harder case covered next (PDF p. 115).

## Time-sensitive statements
The endpoint paths and parameter lists printed for the Discord and Facebook APIs reflect their documentation at the time of writing.

## Relations
Follows authentication in WAS-C05-002. The contrasting case is application-specific shapes (WAS-C05-004), and the broader recon sequence started in WAS-C05-001.
