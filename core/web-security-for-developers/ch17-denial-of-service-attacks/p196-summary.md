---
id: WS-C17-004
title: "Chapter 17 Summary: Denial-of-Service Attacks"
source_pages: "196"
chapter: 17
concepts: [chapter-summary, denial-of-service, ddos, firewall, application-firewall, ips, cdn, caching, job-queue, scaling]
related: [WS-C17-002, WS-C17-003, WS-C18-001]
time_sensitive: false
---
# Chapter 17 Summary: Denial-of-Service Attacks
(Source: PDF p. 196; the text above the "Summary" heading on this page is the end of WS-C17-003)

## What the section covers
The chapter's recap of attack nature and mitigation tiers, plus a hand-off to the final chapter.

## The recap
- Attackers use DoS attacks to make a site unavailable to legitimate users by flooding it with traffic. Such attacks can occur at any layer of the network stack, can be reflected or amplified by third-party services, and are frequently launched as distributed attacks from an attacker-controlled botnet. This recaps WS-C17-002 (PDF p. 196).
- Simple DoS attacks can be defused by sensible firewall settings. Application firewalls and intrusion prevention systems protect against more sophisticated attacks. The most comprehensive, and therefore most expensive, protection comes from DDoS solution providers that filter out bad traffic before it reaches your network (PDF p. 196).
- All DoS types, including accidental ones from a sudden wave of visitors, are eased by building the site to scale. CDNs lift the load of serving static content, effective caching stops the database becoming a bottleneck, and a job queue for long-running processes keeps web servers working efficiently at full capacity. Active traffic monitoring and an easy way to add web servers prepare you for busy periods (PDF p. 196). These details are in WS-C17-003.

## Relations
This chapter ends the book's list of individual vulnerabilities. The final chapter summarizes the main security principles and recaps each vulnerability and its protection (PDF p. 196). See WS-C18-001.
