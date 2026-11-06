---
id: WS-C09-006
title: Chapter 9 Summary - Compromising Authentication
source_pages: "120"
chapter: 9
concepts: [authentication-summary, third-party-login, email-validation, password-hashing, salting, multifactor-authentication, logout, user-enumeration]
related: [WS-C09-003, WS-C09-004, WS-C09-005, WS-C10-001]
time_sensitive: false
---
# Chapter 9 Summary - Compromising Authentication
(Source: PDF p. 120; the text above the "Summary" heading is the end of WS-C09-005.)

## What the section covers
The book's recap of the chapter, in order.

## Recap
- Attackers frequently go after a site's authentication system to steal user credentials. Options for protection include a third-party authentication system such as Facebook Login, or a single sign-on identity provider (WS-C09-003, WS-C09-004) (PDF p. 120).
- With your own system, users choose a username and password at sign-up, and you store and validate an email address for each. The email can serve as the username unless you need a visible display name (PDF p. 120).
- The only dependable way to validate an address is to email a link containing a unique, temporary validation token that your site checks when it is clicked. The password-reset mechanism should work the same way, and both the initial validation email and reset emails should expire after a period of time and after first use (PDF p. 120).
- Process passwords with a cryptographic hash before storing them, and salt the hashes to prevent rainbow-table attacks (PDF p. 120).
- Consider multifactor authentication when the site holds sensitive data. Include a logout function. Keep login failure messages generic so hackers cannot enumerate usernames (PDF p. 120).
- Looking ahead: the next chapter covers how accounts can be compromised after login when an attacker steals the session (WS-C10-001) (PDF p. 120).

## Relations
Recaps WS-C09-003 through WS-C09-005; framing in WS-C09-001.
