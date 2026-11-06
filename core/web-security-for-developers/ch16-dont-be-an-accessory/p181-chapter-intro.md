---
id: WS-C16-001
title: "Chapter 16 Introduction: Don't Be an Accessory"
source_pages: "181"
chapter: 16
concepts: [accessory-to-attack, email-spoofing, open-redirect, clickjacking, ssrf, botnet, blacklisting, good-internet-citizen]
related: [WS-C16-002, WS-C16-003, WS-C16-004, WS-C16-005, WS-C16-006, WS-C15-008]
time_sensitive: false
---
# Chapter 16 Introduction: Don't Be an Accessory
(Source: PDF p. 181, tail PDF p. 182. The text on PDF p. 182 above the "Email Fraud" heading is the rest of this introduction and is covered here.)

## What the section covers
The chapter's opening framing: how your web presence can help attackers get away with attacks on other people, and a roadmap of the five vulnerabilities that follow.

## Why it matters
- Malicious actors have plenty of places to hide online. They routinely impersonate others and use compromised servers to avoid detection. The chapter looks at ways your site may be helping them even when you are not their target (PDF p. 181).
- Avoiding this wins "good internet citizen" credit. More practically, if attackers use your system as a launch point against others, your domain and IP addresses will soon be blacklisted by key services, and your hosting provider may cut you off (PDF p. 181).

## How it works: the chapter roadmap
- Two vulnerabilities help attackers send harmful email: email address spoofing, where scammers disguise who sent a message, and open redirects on websites, which disguise malicious links in email (PDF p. 181). These become WS-C16-002 and WS-C16-003.
- Clickjacking: your site is loaded in a frame on someone else's page and used in a bait-and-switch that tricks users into clicking something harmful (PDF p. 182). See WS-C16-004.
- Server-side request forgery (SSRF): the previous chapter showed XML parser flaws triggering network requests. If an attacker can craft HTTP requests that cause outbound access from your server, you enable SSRF attacks. The chapter covers common launch methods and protection (PDF p. 182). See WS-C16-005.
- Botnets: malware installed on your servers can be remotely controlled by an attacker, so you may unknowingly host "zombie code" (PDF p. 182). See WS-C16-006.

## Relations
Continues from the XML chapter (WS-C15-008). The chapter summary is WS-C16-007.
