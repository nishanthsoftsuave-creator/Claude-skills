---
id: WAS-C26-005
title: DDoS Mitigation
source_pages: "304"
chapter: 26
concepts: [ddos-mitigation, bandwidth-management, packet-analysis, blackholing, traffic-filtering, false-positives, usage-metrics]
related: [WAS-C26-004, WAS-C14-004, WAS-C26-006]
time_sensitive: false
---
# DDoS Mitigation
(Source: PDF p. 304)

## What the section covers
The two defenses the book offers against DDoS: a bandwidth management service and blackholing.

## How it works
- Bandwidth management service: the easiest defense is to buy one. Vendors analyze each packet passing through their servers, running well-established scans to judge whether traffic follows a malicious pattern. Traffic judged malicious is not forwarded to your web server. These services are effective because they can intercept large quantities of network requests, which an application's own infrastructure, especially in hobby and small-business applications, probably cannot (PDF p. 304).
- Blackholing: add servers beside the main application server. Suspicious-looking or repeated traffic is sent to a blackhole server that looks like the application server but performs no operations, while legitimate traffic is routed to the real application server as usual. Figure 26-1 shows a legitimate-looking request being processed by the web server and answered. A malicious-looking request is redirected at the routing level to a black hole, where nothing happens and almost no processing power is used. Because the black hole takes most of the malicious traffic, network and compute capacity stays free for real users (PDF p. 304).

## Alternatives and trade-offs
The figure notes that a black hole's filtering algorithm will inevitably affect some real users. The text says blackholes can reroute legitimate traffic if the targeting is not accurate enough, handle small DDoS attacks well, and do poorly against large ones (PDF p. 304).

## When and how to apply
With any technique, oversensitive filters will block legitimate traffic, so collect deep metrics on legitimate usage patterns before any aggressive mitigation. The last words of this advice are printed at the top of the next page.

## Relations
Follows WAS-C26-004; summarized in WAS-C26-006.
