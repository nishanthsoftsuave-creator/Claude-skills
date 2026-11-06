---
id: WAS-C22-011
title: Implementing a CSP
source_pages: "276"
chapter: 22
concepts: [csp-implementation, content-security-policy-header, meta-tag, xss-first-measure, policy-configuration]
related: [WAS-C22-009, WAS-C22-010, WAS-C22-012]
time_sensitive: false
---
# Implementing a CSP
(Source: PDF p. 276; the last sentence is printed at the top of the next page)

## What the section covers
How a CSP is actually delivered to the browser and when to adopt it.

## Meaning
A CSP is only a configuration string, read by the browser and turned into security rules. Major browsers support several ways of delivering it, and the two most common are (PDF p. 276):
- Have the server send a Content-Security-Policy header with every request, the header value being the policy.
- Put a meta tag in the HTML with http-equiv set to Content-Security-Policy and the policy in its content attribute; the example restricts script-src to https://www.mega-bank.com.

## When to adopt it
It is wise to enact CSP as a first step against XSS if you already know which programming constructs and APIs the application will rely on. The sentence breaks at the page end: if you know where and how code will be consumed, make sure to (PDF p. 276) write the CSP strings up and use them from the start of development. That clause and the closing note that a CSP can easily be changed later are printed at the top of the next page, so no page cite applies to them.

## Relations
Uses the directives in WAS-C22-009 and WAS-C22-010. The chapter recap that says CSP does not cover DOM XSS is WAS-C22-012.
