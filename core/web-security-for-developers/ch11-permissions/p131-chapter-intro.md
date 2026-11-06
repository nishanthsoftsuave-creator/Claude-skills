---
id: WS-C11-001
title: Permissions - Chapter Introduction
source_pages: "131"
chapter: 11
concepts: [permissions, access-control, user-privileges, privilege-escalation, directory-traversal, facebook-2018-breach, user-trust]
related: [WS-C11-002, WS-C11-003, WS-C10-004]
time_sensitive: true
---
# Permissions - Chapter Introduction
(Source: PDF p. 131, tail PDF p. 132. The tail page text above the "Privilege Escalation" heading belongs to this row.)

## What the section covers
The opening framing of Chapter 11: why sites have different permission levels, a cautionary incident, and the chapter's scope.

## Meaning
- Users of a site normally hold different levels of permission. In a content management system, administrators can edit content while most users can only view and interact with it. Social media has a richer set of rules: users can share certain content only with friends or lock their profile. On a webmail site, each person must be able to reach only their own mail (PDF p. 131).
- Permissions must be enforced correctly and uniformly across the site, or users lose trust in you (PDF p. 131).

## Why it matters: the September 2018 Facebook incident
- In September 2018 Facebook suffered a severe permissions failure: attackers exploited a bug in its video-upload tool to generate access tokens, and up to 50 million accounts were compromised. Private profile details such as names, emails and phone numbers were stolen (PDF p. 131).
- Facebook fixed the bug, published a security advisory and made public apologies. The episode came at the end of a year of bad press about its business practices, and the share price suffered (PDF pp. 131-132).

## Scope of the chapter
- The Facebook attack is an instance of privilege escalation, where a malicious user takes over another user's permissions. Setting up a site so each user gets the right privileges is called implementing access control (PDF p. 132).
- The chapter covers both ideas and presents directory traversal, one common way attackers exploit weak access control (PDF p. 132). See WS-C11-002, WS-C11-003 and WS-C11-004.

## Time-sensitive statements
The September 2018 Facebook breach, the 50 million figure and the share price effect (PDF pp. 131-132).

## Relations
Follows Chapter 10 (WS-C10-004), which promised this topic next.
