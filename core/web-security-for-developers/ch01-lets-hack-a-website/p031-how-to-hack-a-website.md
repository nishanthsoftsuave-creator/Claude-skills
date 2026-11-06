---
id: WS-C01-003
title: How to Hack a Website
source_pages: "31-32"
chapter: 1
concepts: [kali-linux, metasploit, wmap, virtualbox, vulnerability-scanning, attacker-tooling, low-barrier-to-attack, legal-boundaries]
related: [WS-C01-002, WS-C02-001]
time_sensitive: true
---
# How to Hack a Website
(Source: PDF pp. 31-32)

## What the section covers
A deliberately short, six-step walk-through showing how little effort it takes to start probing websites for vulnerabilities, and the conclusion the author draws for web developers.

## How it works: the steps (PDF p. 31 unless noted)
1. Search the web for a Kali Linux download. Kali is a Linux distribution built for hackers, shipping with more than 600 security and hacking tools. It is free and maintained by a small team of professional security researchers at Offensive Security.
2. Install a virtual container, meaning a host environment that lets you run another operating system without overwriting your current one. Oracle's VirtualBox is free and runs on Windows, macOS and Linux.
3. Install Kali Linux in the container by downloading it and double-clicking the installer.
4. Start Kali and open the Metasploit framework, described as the most popular command-line tool for testing website security and checking for vulnerabilities. Figure 1-2 is a screenshot of its startup banner (ASCII-art cow joke in the caption), with no technical content.
5. Run the wmap utility from the Metasploit prompt against a target site. It scans a list of URLs to test whether the web server shows security flaws. The author stresses to run it only on a website you own. Figure 1-3 shows sample scan output (caption jokes about law enforcement visiting).
6. Pick an exploit from the Metasploit database that can take advantage of a vulnerability found (PDF pp. 31-32).

## Limits of the tutorial
The author stops after step 6 because the next step would likely be a felony (PDF p. 32).

## Why it matters
- The point is how easy website hacking is to begin. Kali and Metasploit are used by real attackers, set up in minutes, and need no special expertise, yet are very good at finding and exploiting website weaknesses (PDF p. 32).
- That is the reality for web developers: sites are open to anyone with an internet connection, and so are the tools to attack them (PDF p. 32).
- The tone ends reassuringly: do not panic. By the end of the book the reader should, hopefully, know as much about security as the hackers do and be ready for attacks. The next topic is the building blocks of the internet protocol suite (PDF p. 32).

## When and how to apply
INTERPRETATION: Treat this as a defender's exercise only on systems you own or are authorised to test, in line with the book's own warning.

## Relations
Builds on WS-C01-002 (exploits and markets). The protocol-suite discussion it hands off to is WS-C02-001.

## Time-sensitive statements
Names tools and vendors as of 2020: Kali Linux (more than 600 tools), Offensive Security, VirtualBox, Metasploit, wmap.
