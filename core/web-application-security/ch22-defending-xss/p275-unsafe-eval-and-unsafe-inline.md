---
id: WAS-C22-010
title: Unsafe Eval and Unsafe Inline
source_pages: "275"
chapter: 22
concepts: [csp, unsafe-inline, unsafe-eval, string-to-code, settimeout, eval, script-src]
related: [WAS-C22-009, WAS-C22-011, WAS-C22-001]
time_sensitive: false
---
# Unsafe Eval and Unsafe Inline
(Source: PDF p. 275, continuing on the tail page 276)

## What the section covers
What script-src does not protect against, how CSP blocks inline script and eval by default, and how to avoid needing eval.

## The gap in script-src
script-src decides which URLs may load dynamic content into a page. It does not protect against scripts from your own trusted servers. If an attacker gets a script stored on your servers, or reflected by other means, it can still run as an XSS attack (PDF p. 275).

## What CSP does about it
- CSP does not fully protect against this kind of XSS, but it gives mitigation controls that govern common XSS sinks across the user's browser (PDF p. 276).
- With CSP enabled, inline script execution is off by default. It can be switched on again by adding unsafe-inline to the script-src definition (PDF p. 276).
- Likewise eval and similar string-to-code functions are off by default. The restriction can be lifted with the unsafe-eval flag in script-src (PDF p. 276).

## Avoiding eval
If you depend on eval or an eval-like function, rewrite it so no string is interpreted as code. The book's example: a countdown timer that gives setTimeout a string containing an alert call is rewritten to give setTimeout a function that calls alert with the message. Both are valid uses of setTimeout, but the string form is more exposed to XSS as the function grows with new features (PDF p. 276). Any function that is interpreted as a string risks being escaped into code execution, while more specific functions with narrowly defined parameters lower the risk (PDF p. 276).

## Relations
Builds on WAS-C22-009, and the setTimeout case matches the DOM-sink advice in WAS-C22-001. Deployment is in WAS-C22-011.
