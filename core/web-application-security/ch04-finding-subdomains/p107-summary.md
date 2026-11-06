---
id: WAS-C04-010
title: Summary - Finding Subdomains
source_pages: "107-108"
chapter: 4
concepts: [chapter-summary, subdomain-discovery, recon-map, attack-surface, hidden-servers, technique-combination]
related: [WAS-C04-001, WAS-C04-008, WAS-C04-009, WAS-C05-001]
time_sensitive: false
---
# Summary: Finding Subdomains
(Source: PDF p. 107; the following page is blank)

## What the section covers
The chapter's closing lessons on why subdomain discovery matters and how to use the several techniques together.

## Main points
- The main goal of recon is a map of the application that is later used to prioritise and deliver attack payloads. An early part of building it is working out which servers keep the application running, which is why the chapter searches for subdomains of the main domain (PDF p. 107).
- Consumer-facing domains, such as the client site of a bank, receive the most scrutiny and have bugs fixed quickly because visitors hit them every day (PDF p. 107).
- Servers that run behind the scenes, such as a mail server or an admin backdoor, are often full of bugs because they have much less use and exposure. Finding one of these behind-the-scenes APIs can be a useful jumpstart when hunting for something to exploit (PDF p. 107).
- No single technique gives comprehensive results, so several should be combined. Once enough subdomains have been collected you can move to other recon techniques, and you may return later for more if the obvious attack vectors yield nothing (PDF p. 107).

## When and how to apply
INTERPRETATION: treat the subdomain list as a living part of the recon map and revisit it whenever other lines of attack stall.

## Relations
The techniques summarised are in WAS-C04-002 to WAS-C04-009, starting from the framing in WAS-C04-001. The next step in the book is finding the API endpoints hosted on those subdomains (WAS-C05-001).
