---
id: WS-C09-002
title: Implementing Authentication and Brute-Force Attacks
source_pages: "110-111"
chapter: 9
concepts: [http-authentication, basic-authentication, digest-authentication, login-form, brute-force, common-passwords, hashing, www-authenticate]
related: [WS-C09-001, WS-C09-003, WS-C09-005, WS-C10-002]
time_sensitive: true
---
# Implementing Authentication and Brute-Force Attacks
(Source: PDF pp. 110-111, tail PDF p. 112. The text at the top of PDF p. 110 above the "Implementing Authentication" heading is the end of WS-C09-001. The tail page content above the "Mitigation 1" heading belongs here.)

## What the section covers
How authentication is carried out on the web (HTTP-native versus HTML login forms) and why brute-force password guessing is the main threat to it.

## Meaning
- Authentication is part of HTTP itself. To challenge a user, the server answers with a 401 status code and a WWW-Authenticate header naming the preferred scheme; the user agent, normally a browser, then asks the user for a username and password, which creates the login behaviour. Two schemes are widely supported: basic and digest (PDF p. 110).
- Basic authentication: the browser joins username and password with a colon, Base64-encodes the result and returns it in the Authorization header of the request (PDF p. 110).
- Digest authentication: more involved; the browser computes a hash from the username, password and URL. A hash is the output of a one-way function, a "fingerprint" that is easy to produce from input data but hard to reverse into the input. Hashing returns later in the chapter for password storage, see WS-C09-005 (PDF p. 110).

## Why popular sites avoid HTTP-native authentication
- The browser's built-in prompt looks like a JavaScript alert, grabs focus and interrupts the visit (Figure 9-1 shows the Chrome prompt) (PDF pp. 110-111).
- It sits outside the HTML, so it cannot be styled to match the site, and the browser cannot autocomplete credentials into it (PDF p. 110).
- HTTP authentication has no password-reset mechanism, so you would have to build one separately from the prompt, which makes the experience confusing (PDF p. 110).
- Because of this, native HTTP authentication is mostly kept for applications where the user experience matters little (PDF p. 111).

## How it works: non-native login forms
- Modern sites build their own HTML login form (Listing 9-1). It contains a username input, a password-type input that masks typed characters, and a submit button, and the form posts to a login URL (PDF p. 111). Book oddity, recorded as printed: the text describes the username field as an input of type text, while Listing 9-1 itself uses type email with an email placeholder (PDF p. 111).
- On submission the credentials go to the server in a POST request. If authentication fails the server replies with a 401 status; if it succeeds the server redirects the user to their homepage (PDF p. 111).

## Brute-force attacks
- Attackers often go after the authentication step by guessing passwords. Films show hackers working from personal knowledge of the target, which may matter for high-profile targets, but a brute-force attack is usually more productive: a script tries thousands of common passwords against a login page (PDF p. 111).
- Earlier data breaches have leaked millions of real passwords, so an attacker knows which ones to try first (PDF p. 111).
- Listing 9-2 gives the ten most common passwords from an annual list published by security firm SplashData, in order: 123456, password, 12345678, qwerty, 12345, 123456789, letmein, 1234567, football, iloveyou. The book notes that such lists change very little from year to year (PDF p. 112).
- The chapter then turns to ways of implementing and protecting authentication against this threat, starting with WS-C09-003 (PDF p. 112).

## Time-sensitive statements
- The password ranking is the SplashData list as printed in the book; the book says such lists change very little from year to year but does not state which year this list is from (PDF p. 112).
- Chrome's native login prompt is shown as an example (PDF p. 111).

## Relations
Followed by the mitigations in WS-C09-003, WS-C09-004 and WS-C09-005. Session handling after login is in WS-C10-002.
