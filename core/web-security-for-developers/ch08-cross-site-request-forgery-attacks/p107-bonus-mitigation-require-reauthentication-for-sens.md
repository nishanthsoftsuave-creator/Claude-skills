---
id: WS-C08-006
title: "Bonus Mitigation: Require Reauthentication for Sensitive Actions"
source_pages: "107"
chapter: 8
concepts: [reauthentication, sensitive-actions, csrf-mitigation, shared-devices, confirm-credentials, financial-transactions]
related: [WS-C08-005, WS-C08-007, WS-C09-005]
time_sensitive: false
---
# Bonus Mitigation: Require Reauthentication for Sensitive Actions
(Source: PDF p. 107. Text above the heading on this page is the end of WS-C08-005; the Summary heading below it begins WS-C08-007.)

## What the section covers
An extra, user-visible CSRF defence: asking people to confirm their credentials before doing something significant (PDF p. 107).

## Meaning
Many sites make you re-enter your login details when you do something sensitive, such as changing your password or starting a payment. This is reauthentication (PDF p. 107).

## Why it works
- It is a common way to secure sites against CSRF because it gives the user a clear signal that they are about to do something significant and potentially dangerous. (PDF p. 107)
- INTERPRETATION: a forged request made from another site would not carry the user's typed credentials, which is why the prompt interrupts it.
- A side benefit: it protects users who accidentally stay logged in on shared or stolen devices (PDF p. 107).

## When and how to apply
If your site handles financial transactions or confidential data, strongly consider forcing users to re-enter their credentials when they perform sensitive actions (PDF p. 107).

## Relations
Extra layer on top of WS-C08-003, WS-C08-004 and WS-C08-005. The recap is WS-C08-007. Authentication design is discussed in WS-C09-005.
