---
id: WAS-C14-001
title: Denial of Service Chapter Introduction
source_pages: "193"
chapter: 14
concepts: [denial-of-service, ddos, redos, bug-bounty-scope, testing-safety, availability]
related: [WAS-C14-002, WAS-C14-003, WAS-C14-004, WAS-C26-001]
time_sensitive: false
---
# Denial of Service (DoS): Chapter Introduction
(Source: PDF p. 193)

## What the section covers
A short framing of denial of service before the chapter's three detailed forms: regex-based DoS, logical DoS and distributed DoS. It covers what DoS is, how wide the range of severity is, and why it is awkward to test.

## Meaning
- The most widely publicized attack on the web is arguably the distributed denial of service (DDoS) attack. It is a form of denial of service in which a large network of devices floods a server with requests, slowing it or making it unusable for legitimate users (PDF p. 193).
- DoS comes in many forms. At one end is the familiar distributed version with thousands or more coordinated devices. At the other is a code-level DoS that affects a single user, for example a faulty regular expression that makes validating a string take a very long time (PDF p. 193).
- Seriousness varies widely. The book's range runs from reducing an active server's capacity, through what its garbled wording calls "a functionless electric bill", down to making one user's page load slightly slower or pausing a video part-way through buffering (PDF p. 193).
INTERPRETATION: the "functionless electric bill" phrase appears to mean a server rendered unusable while still costing its owner money; the book does not explain it further.

## Why it matters and how to test
- Because of that range, DoS is hard to test for, particularly the milder cases. Most bug bounty programs ban DoS submissions outright so that hunters do not disturb normal usage (PDF p. 193).
- A warning in the text says DoS vulnerabilities interfere with real users, so the most effective way to test is in a local development environment where real users will not notice interruptions (PDF p. 193).
- Apart from a few exceptions, DoS does not cause permanent damage, but it does harm usability for legitimate users. Finding the sink responsible for degraded experience can be difficult (PDF p. 193).

## Relations
Detailed forms follow in WAS-C14-002 (regex), WAS-C14-003 (logical) and WAS-C14-004 (distributed). Defenses are covered in Chapter 26 (WAS-C26-001).
