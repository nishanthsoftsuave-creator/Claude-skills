---
id: WAS-C23-001
title: Header Verification
source_pages: "279-280"
chapter: 23
concepts: [csrf-defense, origin-header, referer-header, header-verification, trusted-origins, post-requests, defense-in-depth, xss-bypass]
related: [WAS-C11-001, WAS-C11-003, WAS-C23-002, WAS-C22-001]
time_sensitive: false
---
# Header Verification
(Source: PDF pp. 279-280)

## What the section covers
The opening of the CSRF defense chapter and its first countermeasure: checking the `origin` and `referer` HTTP headers on incoming requests to see whether a request came from a place the application trusts. The section also says why this check is only a starting point.

## Chapter framing
Part II built Cross-Site Request Forgery attacks that ride on a user's authenticated session, using links, image tags and POST forms. Those attacks are effective and dangerous because they run with elevated privilege and are usually invisible to the user. This chapter turns to defending a codebase against them and lowering the odds that users' authenticated sessions can be abused (PDF p. 279).

## Meaning
- Many CSRF requests are delivered through links in email or on an unrelated website, so the origin of the request differs from the application's own origin. Checking where a request came from can therefore filter much of the attack traffic (PDF p. 279).
- Two headers carry that information: `referer` and `origin`. The book stresses that major browsers do not let JavaScript modify them programmatically, so a header set by a correctly implemented browser is unlikely to be spoofed (PDF p. 279).
- Origin header: sent only on HTTP POST requests, and it states where the request started. Unlike the referer, the text says it also appears on HTTPS requests as well as HTTP ones. The printed example is a scheme, host and port value for the bank's site (PDF pp. 279-280).
- Referer header: present on every request. It is absent only when the referring link carries the `rel=noreferer` attribute. It names the originating location in the same style (PDF p. 280).

## How it works
- When a POST such as a funds transfer (with amount and recipient parameters) reaches the server, the server compares the header values with a list of trusted origins that host its own web applications (PDF p. 280).
- The book's Node.js example keeps an array of three allowed locations (the main site, the API host and a portal host). A validation function reads both headers, returns false if a header is missing, and returns false if either value is outside the array. The transfer handler first confirms the session is authenticated, then runs the header check, answers 401 on failure, and only then calls the transfer operation with the current user, the target user and the amount (PDF p. 280).
INTERPRETATION: as printed, the missing-header guard reads `!origin || referer`, which would reject a request that does have a referer. The surrounding explanation says both headers should be present, so the intended condition is most likely that a request is rejected when either header is absent.

## When and how to apply
- Check both headers whenever possible. If neither is present, treat the request as non-standard and reject it (PDF p. 280).
- Run the check before any state-changing logic, as the transfer example does.

## Limitations and failure modes
- Header checks are a first line of defense only. If an attacker obtains an XSS foothold on one of the whitelisted origins, they can launch the forged request from the application's own origin, and it then looks like a legitimate request from the trusted servers (PDF p. 280).
- The tail page adds that this is worse when the site lets users publish content, because then validating that headers come from your own servers may give no protection at all. The book concludes that several CSRF defenses should be combined, with header verification as the starting point rather than a full solution (PDF p. 281).

## Relations
Builds on the CSRF attacks of WAS-C11-001 and WAS-C11-003; the stronger token defense follows in WAS-C23-002. The XSS defenses in WAS-C22-001 matter here because XSS undermines this check.
