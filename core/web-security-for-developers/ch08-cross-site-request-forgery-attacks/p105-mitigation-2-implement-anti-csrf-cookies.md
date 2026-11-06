---
id: WS-C08-004
title: "Mitigation 2: Implement Anti-CSRF Cookies"
source_pages: "105"
chapter: 8
concepts: [anti-csrf-cookie, csrf-token, hidden-form-field, same-origin-policy, tornado, double-submit, put-delete-protection]
related: [WS-C08-003, WS-C08-005, WS-C08-007, WS-C10-002, WS-C10-003]
time_sensitive: false
---
# Mitigation 2: Implement Anti-CSRF Cookies
(Source: PDF p. 105, tail PDF p. 106. On PDF p. 106 the text above the "Mitigation 3: Use the SameSite Cookie Attribute" heading belongs here. The text at the top of PDF p. 105 above this heading is the end of WS-C08-003.)

## What the section covers
Why side-effect-free GET is not enough, how an anti-CSRF cookie plus a hidden form token verifies that requests come from your own pages, a Tornado template example, and extending the check to JavaScript requests (PDF pp. 105-106).

## Why it matters
- Fixing GET closes most CSRF attacks, but other verbs still need protection. Such attacks are much rarer and need far more work, but an attacker may try them if the payoff looks big enough (PDF p. 105).
- Example: the attacker can trick a victim into sending a POST by having them submit a malicious form or script hosted on a third-party site the attacker controls. Sensitive actions should be triggered only from your own login forms and JavaScript, not from malicious pages that trick the user (PDF p. 105).

## Meaning
An anti-CSRF cookie is a randomized string token that the server writes to a named cookie. Cookies are small text values passed between browser and server in HTTP headers. If the response carries a Set-Cookie header with the name _xsrf and a token value, the browser sends the same value back in the Cookie header of the next request (PDF p. 105).

## How it works
- The site uses the cookie to verify that POST requests come from pages on the same domain. Pages add the same token as a hidden input named _xsrf in every form that generates a POST (PDF p. 105).
- On submission, if the _xsrf value in the returned cookie does not match the _xsrf value in the request body, the server rejects the request. This confirms the request started on your site rather than a malicious third-party site, since the browser only sends the cookie when the page was loaded from the same domain (PDF p. 105).
- Most modern web servers support anti-CSRF cookies; consult your server's security documentation because the syntax differs slightly (PDF pp. 105-106).
- Listing 8-2 is a Tornado (Python) template. A form posting to a new-message path includes a call to the xsrf_form_html() module, then a text input and a submit button. That function generates a randomized token and writes it into the form as a hidden _xsrf input; Tornado also writes the same token to the response headers as a Set-Cookie. When the user submits, the server checks that the form token equals the token in the returned Cookie header (PDF p. 106).
- The browser's security model returns cookies according to the same-origin policy, so the cookie values can only have been set by the web server. The server can therefore be sure the POST came from the host website (PDF p. 106).

## When and how to apply
- Also use anti-CSRF cookies to validate requests made from JavaScript, which protects PUT and DELETE too. The JavaScript must read the token out of the HTML and send it back in the HTTP request (PDF p. 106).
- Once implemented, the site should be much safer, but one loophole remains: attackers might steal the anti-CSRF tokens and embed them in malicious code. The next mitigation addresses that (PDF p. 106).

## Relations
Builds on WS-C08-003; the SameSite attribute that closes the token-theft loophole is WS-C08-005. Cookies and sessions are developed in WS-C10-002 and WS-C10-003.
