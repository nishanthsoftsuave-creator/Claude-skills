---
id: WS-C09-001
title: Compromising Authentication - Chapter Introduction
source_pages: "109"
chapter: 9
concepts: [authentication, login, credentials, account-takeover, brute-force, chapter-roadmap, session-boundary]
related: [WS-C09-002, WS-C09-005, WS-C10-001]
time_sensitive: false
---
# Compromising Authentication - Chapter Introduction
(Source: PDF p. 109, tail PDF p. 110. The tail page text above the "Implementing Authentication" heading belongs to this row.)

## What the section covers
The opening framing of Chapter 9: what authentication is, why users accept it, why it attracts attackers, and the road map of the chapter.

## Meaning
- Authentication is the process of identifying users when they come back to a site. Nearly every site offers some login feature, and it gives each person an identity in an online community so they can post content, message others, buy things and so on (PDF p. 109).
- Signing up with a username and password, then logging in again later, is something internet users now do without thinking. Browsers and plug-ins help by remembering or suggesting passwords, and third-party authentication services are everywhere (PDF p. 109).

## Why it matters
- The comfort users feel has a downside: getting into someone's account is very attractive to attackers. Stolen credentials are easy to sell on the dark web, hijacked social media accounts can be used to spread clickbait, and accounts can be used for financial fraud (PDF p. 109).

## How the chapter is organised
- The chapter looks at ways an attacker can compromise an account during the login and authentication step. Vulnerabilities that users face after they have logged in and have a session are left to the next chapter, covered in WS-C10-001 (PDF p. 110).
- It first shows the most common ways websites implement authentication and how attackers use brute-force attacks against them (WS-C09-002). It then presents the protections: third-party authentication (WS-C09-003), single sign-on (WS-C09-004) and securing your own authentication system (WS-C09-005) (PDF p. 110).

## Relations
Leads into WS-C09-002. The session-based risks that follow login are the subject of Chapter 10.
