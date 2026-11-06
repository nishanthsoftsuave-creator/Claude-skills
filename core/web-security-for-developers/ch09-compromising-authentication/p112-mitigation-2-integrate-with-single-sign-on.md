---
id: WS-C09-004
title: Mitigation 2 - Integrate with Single Sign-On
source_pages: "112"
chapter: 9
concepts: [single-sign-on, sso, saml, identity-provider, enterprise-authentication, business-users]
related: [WS-C09-003, WS-C09-005]
time_sensitive: true
---
# Mitigation 2 - Integrate with Single Sign-On
(Source: PDF p. 112, tail PDF p. 113. This row begins at the "Mitigation 2" heading on PDF p. 112; the tail page content above the "Mitigation 3" heading belongs here.)

## What the section covers
Single sign-on (SSO) as an option for sites aimed at business users.

## Meaning
- With an OAuth or OpenID identity provider, people normally sign in using their personal email address as the username (PDF p. 112).
- If your target audience is business users, consider an SSO identity provider such as Okta, OneLogin or Centrify. These centralise authentication across a company's systems so staff can log into outside applications smoothly using their work email (PDF p. 112).

## Why it matters
- Company administrators keep final say over which employees may use which sites, and user credentials are stored securely on the company's servers (PDF p. 112).

## How it works
- Integration with an SSO provider usually requires Security Assertion Markup Language (SAML). The book describes SAML as an older and less friendly standard than OAuth or OpenID, but notes that most programming languages offer mature SAML libraries (PDF p. 113).

## When and how to apply
- INTERPRETATION: Choose SSO when your users are employees of organisations that manage their own identities; choose OAuth or OpenID providers (WS-C09-003) for consumer audiences (PDF p. 112).

## Time-sensitive statements
Okta, OneLogin and Centrify are named as examples of identity providers (PDF p. 112).

## Relations
Sits between WS-C09-003 and the do-it-yourself approach in WS-C09-005.
