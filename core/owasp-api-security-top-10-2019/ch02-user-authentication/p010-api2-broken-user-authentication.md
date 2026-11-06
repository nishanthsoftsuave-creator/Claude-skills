---
id: A02-001
title: API2:2019 Broken User Authentication
source_pages: "10-11"
chapter: api2
concepts: [broken-user-authentication, credential-stuffing, brute-force, account-lockout, jwt-validation, password-reset, multi-factor-authentication, api-keys, weak-passwords, token-validation]
related: [A00-006, A00-007, A04-001, A09-001, A10-001]
time_sensitive: false
---
# API2:2019 Broken User Authentication
(Source: PDF pp. 10-11)

## What the section covers
Flaws in how an API establishes who is calling it: missing protections around login and recovery endpoints, and mistakes in the authentication mechanism itself. The chapter lists the conditions that make an API vulnerable, gives two attack scenarios and a longer-than-usual prevention list.

## Risk scores
Exploitability 3, prevalence 2, detectability 2, technical impact 3; business impact is business-specific (PDF p. 10). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: authentication in APIs is described as a complex and confusing mechanism. Software and security engineers may hold misconceptions about where authentication's boundaries lie and how to implement it correctly. On top of that, the authentication component is exposed to everyone, which makes it an easy target. Together these two facts make it vulnerable to many exploits (PDF p. 10).
- Security weakness, split into two sub-issues (PDF p. 10):
  1. **Lack of protection mechanisms.** Endpoints responsible for authentication must be treated differently from ordinary endpoints and given extra layers of protection.
  2. **Mis-implementation of the mechanism.** The mechanism is used or built without considering the attack vectors, or it is the wrong mechanism for the use case; the example given is an authentication scheme designed for IoT clients applied to a web application.
- Impacts: attackers can take control of other users' accounts, read their personal data and act on their behalf, including money transfers and sending personal messages (PDF p. 10).

## Is the API vulnerable?
Authentication endpoints and flows are assets that need protection, and "forgot password" or "reset password" flows must be treated exactly like authentication (PDF p. 10). The API is vulnerable if it (PDF p. 10):
- permits credential stuffing, where the attacker holds a list of valid usernames and passwords;
- lets an attacker brute-force one user account without a captcha or account-lockout mechanism;
- permits weak passwords;
- sends sensitive authentication details, such as auth tokens and passwords, in the URL;
- does not validate the authenticity of tokens;
- accepts unsigned or weakly signed JWTs (the `"alg":"none"` case) or does not check their expiry date;
- stores passwords in plain text, unencrypted or weakly hashed;
- uses weak encryption keys.

## How it works: the attack scenarios
1. **Credential stuffing.** Using lists of known username and password pairs is a common attack. An application without automated-threat or credential-stuffing protection becomes a password oracle, a tester that tells the attacker which credentials are valid (PDF p. 10).
2. **Brute-forcing an SMS reset code.** The attacker starts password recovery by posting the victim's username to a verification-codes endpoint, which sends a six-digit SMS token to the victim's phone. Because the endpoint that accepts the token has no rate limit, a multi-threaded script can try every combination against the token-check endpoint and find the right one within minutes (PDF p. 10).

## How to prevent
The document's list (PDF p. 11):
- Know every flow through which a client can authenticate to the API (mobile, web, deep links that implement one-click authentication, and so on), and ask your engineers which flows were missed.
- Read up on the authentication mechanisms in use and understand what they are and how they are used. The document is blunt that OAuth is not authentication, and neither are API keys.
- Do not reinvent authentication, token generation or password storage; use the standards.
- Treat credential-recovery and forgot-password endpoints as login endpoints for brute-force, rate-limiting and lockout purposes.
- Use the OWASP Authentication Cheat Sheet.
- Implement multi-factor authentication where possible.
- Put anti-brute-force mechanisms in place against credential stuffing, dictionary attacks and brute force on authentication endpoints; these must be stricter than the API's ordinary rate limiting.
- Add account lockout or captcha to stop brute force against specific users, and check for weak passwords.
- Use API keys for client application or project authentication, never for user authentication.

## When and how to apply
INTERPRETATION: during a review, list every authentication and recovery endpoint, then check each item of the vulnerability list against it. Probing brute-force resistance means sending repeated wrong attempts against a test account on a non-production copy with the owner's approval; the document gives no numeric threshold for "rate limited", so the project sets one and the report says so.

## References the section lists
OWASP: Key Management Cheat Sheet, Authentication Cheat Sheet, and the Credential Stuffing page. External: CWE-798 Use of Hard-coded Credentials (PDF p. 11).

## Relations
A04-001 covers the general rate limiting that the stricter authentication limits sit on top of; A09-001 shows a forgotten beta host that lacked the production reset-token rate limit; A10-001 covers the alerting that should fire during a credential-stuffing attack; A00-007 holds the one-line summary.
