---
id: WAS-C04-001
title: Multiple Applications per Domain
source_pages: "85"
chapter: 4
concepts: [subdomain-discovery, domain-structure, black-box-testing, bug-bounty-scope, attack-surface, recon-map, hidden-services]
related: [WAS-C04-002, WAS-C04-010, WAS-C02-002]
time_sensitive: false
---
# Multiple Applications per Domain
(Source: PDF p. 85, continuing onto the top of PDF p. 86)

## What the section covers
The opening of the chapter on finding subdomains. It explains why mapping the subdomains of a target domain is worth doing before any other recon step, and sets up the running example of a sponsored black-box test against the fictional MegaBank.

## Why it matters
- To scope and later test API endpoints, you first need to know how the application's domains are organised. A modern web application is rarely served from one domain; it is usually split into at least a client domain and a server domain, plus the familiar "www" versus bare-domain variants (PDF p. 85).
- Being able to find and record subdomains iteratively is described as a useful first recon technique against any web application (PDF p. 85).

## The running example
- The tester is mapping MegaBank's web applications for a black-box penetration test sponsored by the bank. The customer-facing app that holds user bank accounts lives at the "www" host of the bank's domain (PDF p. 85).
- The open question is whether other internet-accessible servers are linked to the same domain name.
- MegaBank runs a bug bounty program whose scope covers the main domain thoroughly. Consequently any easy-to-find flaw there has already been fixed or reported, and any new flaw has to be found before bounty hunters find it (PDF p. 85).
- Because of that, the tester looks for easier targets that still hurt the bank. The text stresses this is an ethical, corporate-sponsored test, although it can still be enjoyable (PDF p. 85).
- First step: perform recon and fill the web application map with a list of subdomains attached to the target domain. The "www" host points at the public application itself, so it is probably of no interest here (PDF p. 85).

## How it works (the continuation on the next page)
The section continues at the top of the next page. Large consumer companies commonly host a variety of subdomains under their primary domain, used for services such as email, admin applications and file servers (PDF p. 86). Figure 4-1 on that page draws a simple subdomain web for the example: the bare domain sits at the bottom centre, with the "www" host and a mail host hanging off it, and an arrow up to a "my" host that in turn leads to a "test.my" host. Its caption warns that real webs are often much more complex and may include servers that cannot be reached from an external network.

The text then notes there are many ways to gather this data, that several usually have to be tried, and that the chapter proceeds from the simplest method to harder ones (PDF p. 86).

## When and how to apply
INTERPRETATION: record every discovered subdomain in the recon map from the start, because lightly scrutinised hosts such as mail or admin servers are often the more promising targets once the main application has been hardened by a bounty program.

## Relations
The first technique in the sequence is reading the browser's own network traffic (WAS-C04-002). The chapter's closing lessons are in WAS-C04-010, and the idea of a recon map comes from WAS-C02-002.
