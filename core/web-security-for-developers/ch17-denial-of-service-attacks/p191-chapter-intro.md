---
id: WS-C17-001
title: "Chapter 17 Introduction: Denial-of-Service Attacks"
source_pages: "191"
chapter: 17
concepts: [denial-of-service, dns-attack, dyn-outage, availability, traffic-flooding, resource-exhaustion]
related: [WS-C17-002, WS-C17-003, WS-C16-006, WS-C16-007]
time_sensitive: true
---
# Chapter 17 Introduction: Denial-of-Service Attacks
(Source: PDF p. 191, tail PDF p. 192. The text on PDF p. 192 above the "Denial-of-Service Attack Types" heading is the end of this introduction and is covered here.)

## What the section covers
The chapter's opening framing: a landmark outage that shows what a denial-of-service attack can do, and how this attack differs in purpose from the vulnerabilities in earlier chapters.

## Meaning
- A denial-of-service (DoS) attack does not aim to compromise a system or site, unlike most vulnerabilities in the book. Its intent is only to make the target unavailable to other users (PDF p. 191).
- It is generally done by flooding the site with inbound traffic until all the server's resources are used up (PDF pp. 191-192).

## How it works: the opening incident
- On October 21, 2016, many popular sites appeared offline, among them Twitter, Spotify, Netflix, GitHub and Amazon. The cause was an attack on a DNS provider: a massive wave of DNS lookup requests overwhelmed the provider Dyn. Two more large waves followed, and it took most of the day to restore services fully (PDF p. 191).
- The scale and impact were unprecedented. The book's only comparable example is a shark biting through an undersea cable that took Vietnam offline for a while. It was, though, just the latest form of the increasingly dangerous DoS attack (PDF p. 191).

## Why it matters
The chapter goes on to break down the common techniques of DoS attacks and ways to defend against them (PDF p. 192). Attack types are in WS-C17-002 and mitigations in WS-C17-003.

## Time-sensitive statements
The October 2016 Dyn outage and the sites named as affected (Twitter, Spotify, Netflix, GitHub, Amazon) are dated incidents (PDF p. 191).

## Relations
Follows the botnet and accessory material of chapter 16 (WS-C16-006, WS-C16-007), which previewed DoS as a brute-force technique.
