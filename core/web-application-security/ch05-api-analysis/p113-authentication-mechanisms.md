---
id: WAS-C05-002
title: Authentication Mechanisms
source_pages: "113"
chapter: 5
concepts: [authentication-schemes, http-basic-auth, digest-authentication, oauth-bearer-token, base64-encoding, authorization-header, payload-shape]
related: [WAS-C05-001, WAS-C05-003, WAS-C03-013]
time_sensitive: false
---
# Authentication Mechanisms
(Source: PDF p. 113, with the end of the section on the top of PDF p. 114)

## What the section covers
Why recon should work out which authentication scheme an application uses, a table of the three common schemes, and a worked example of recognising and decoding HTTP basic authentication.

## Why it matters
- Guessing the payload shape an endpoint needs is much harder than showing the endpoint exists. The easiest route is to study the shape of requests the browser already sends; beyond that you make educated guesses and test by hand. Automating shape discovery is possible, but unless it analyses existing requests it is very easy to detect and log (PDF p. 113).
- Start with endpoints nearly every application has: sign in, sign up and password reset. Their payloads tend to look alike across applications because authentication follows standard schemes (PDF p. 113).
- Every app with a public web interface has a login page, but how it authenticates a session can differ. Knowing the scheme matters because many modern applications attach an authentication token to every request. If you can work out the scheme and how the token is attached, other endpoints that need an authenticated user become easier to analyse (PDF p. 113).

## Table 5-2: major authentication schemes (PDF p. 113)
| Scheme | How it works | Strengths | Weaknesses |
|---|---|---|---|
| HTTP basic | username and password sent on each request | all major browsers support it natively | session does not expire; easy to intercept |
| HTTP digest | hashed user name, realm and password sent on each request | harder to intercept; server can reject expired tokens | strength depends on the hashing algorithm |
| OAuth | bearer-token auth; allows signing in with other sites, for example one big service to a streaming site | tokenised permissions can be shared between apps for integrations | phishing risk; the central site can be compromised, compromising every connected app |

## How it works: recognising basic authentication
After logging in to the example bank, the page request that follows carries an Authorization header whose value begins with the word Basic followed by an encoded string (PDF p. 113). That indicates HTTP basic authentication. The encoded part is simply the base64 form of the username and password joined by a colon, the usual way to format credentials for HTTP (PDF p. 114).

The browser console has two built-ins for this: one converts a string to base64 and the other decodes it. Decoding the example string reveals the username and password sent over the network, which the book shows as a short user name and a four-digit password (PDF p. 114).

Because the scheme is so insecure, basic auth is normally used only on applications that enforce SSL/TLS so credentials cannot be intercepted midair, for instance on a public WiFi hotspot (PDF p. 114).

## When and how to apply
The takeaway is that requests are authenticated by this header. If you meet another endpoint that returns nothing interesting with an empty payload, the first thing to try is attaching an authorization header and seeing whether it behaves differently for an authenticated user (PDF p. 114).

## Limitations
Per Table 5-2: basic auth never expires a session and is easy to intercept; digest is only as strong as its hashing algorithm; OAuth brings a phishing risk and lets one compromised central site compromise every connected app (PDF p. 113). Basic auth is therefore normally paired with TLS (PDF p. 114).

## Relations
Builds on endpoint discovery (WAS-C05-001). Shapes of payloads follow in WAS-C05-003 and WAS-C05-004; authentication background is in WAS-C03-013.
