---
id: WS-C17-003
title: Denial-of-Service Attack Mitigation
source_pages: "194-195"
chapter: 17
concepts: [firewall, application-firewall, intrusion-prevention-system, ddos-protection, cdn, caching, job-queue, horizontal-scaling, load-balancer, monitoring]
related: [WS-C17-002, WS-C17-004, WS-C05-005, WS-C16-005]
time_sensitive: true
---
# Denial-of-Service Attack Mitigation
(Source: PDF pp. 194-195, tail PDF p. 196. The text at the top of PDF p. 194 above the "Denial-of-Service Attack Mitigation" heading, the "Unintentional Denial-of-Service Attacks" paragraph, belongs to WS-C17-002. The text on PDF p. 196 above the "Summary" heading is the end of this section and is covered here.)

## What the section covers
How realistic the threat is for most sites, then the three families of countermeasures the book lists: firewalls and intrusion prevention systems, DDoS protection services, and building for scale.

## Why it matters
- Defending against a major DoS attack is expensive and time-consuming. You are unlikely to be hit by one on the scale of the 2016 Dyn attack, which needed extensive planning and which only a handful of adversaries could mount. Terabytes a second at a recipe blog is improbable (PDF p. 194).
- Smaller attacks combined with extortion demands do occur, so some safeguards are worthwhile (PDF p. 194).

## How it works: firewalls and intrusion prevention (PDF p. 194)
- Firewalls: every modern server operating system includes one. A firewall is software that monitors and controls inbound and outbound traffic according to preset rules. It lets you choose which ports accept incoming traffic and filter by IP address with access-control rules. Firewalls sit at the network perimeter to stop bad traffic before it reaches internal servers. Modern ones block most ICMP attacks and can blacklist single IP addresses, which effectively shuts down a single-source attack.
- Application firewalls work higher in the stack as proxies that scan HTTP and other traffic before it enters the network. They reject corrupted or malicious requests matching a malicious signature. Vendors keep signatures current, so they can block many hacking attempts (SQL injection is the book's example) in addition to easing DoS attacks. Open source options include ModSecurity; commercial vendors named are Norton and Barracuda Networks, some of whom sell hardware.
- Intrusion prevention systems (IPS) are more holistic. They add firewalls and signature matching, look for statistical anomalies in traffic, and scan files on disk for unusual changes. An IPS is usually a serious investment but protects very effectively.

## How it works: DDoS protection services (PDF p. 195)
- In a sophisticated attack the packets look just like normal ones. The traffic is valid; only its intent and volume are malicious, so firewalls cannot filter it out.
- Many companies sell DDoS protection, usually at significant cost. You route all incoming traffic through their data centers, where it is scanned and anything malicious is blocked. The provider has a global view of malicious activity and huge bandwidth, so it can use heuristics to keep harmful traffic away from you.
- CDNs often offer this, because they have geographically spread data centers and may already host your static content. If most of your requests are served from a CDN, routing the rest through its data centers is little extra effort.

## How it works: building for scale (PDF pp. 195-196)
- Being attacked is, in many ways, indistinguishable from having many visitors at once, so readiness for surges defends against many attacks. Scaling is a vast subject, but the book highlights four impactful approaches: offload static content, cache database queries, process long-running tasks asynchronously, and deploy to multiple web servers (PDF p. 195).
- CDNs: they take over serving static content such as images and font files. This makes the site more responsive, cuts load on your servers, is easy to integrate, and is cost-effective for most sites (PDF p. 195).
- Caching: once static content is offloaded, database calls usually become the next bottleneck. Effective caching protects the database during a surge. Cached data can live on disk, in memory, or in a shared memory cache such as Redis or Memcached. The browser can cache too: a Cache-Control header on a resource such as an image tells the browser to keep a local copy and not ask again until a configurable future date (PDF p. 195).
- Job queue: move long-running work, such as building large download files or sending email, to background workers. The web server creates jobs and puts them on a queue; separately deployed workers take jobs off one at a time and tell the web server when each is done. The book points to the Netflix technology blog as an example of a massively scalable system built this way (PDF pp. 195-196).
- Scale out: have a deployment strategy that quickly increases the number of web servers in busy periods. An Infrastructure as a Service (IaaS) provider such as Amazon Web Services makes it easy to deploy one server image several times behind a load balancer, and a platform such as Heroku does it with a dashboard slider. Use your host's traffic monitoring, and tools like Google Analytics for session counts, then add servers when monitoring thresholds are reached (PDF p. 196).

## Alternatives and trade-offs
The mitigations rise in cost and coverage: firewall settings handle simple attacks, application firewalls and IPS handle more sophisticated ones, and DDoS protection services are the most comprehensive but also the most expensive (see the recap in WS-C17-004). Building for scale helps against every type, including accidental surges.

## Time-sensitive statements
Named products and vendors (ModSecurity, Norton, Barracuda Networks, Redis, Memcached, AWS, Heroku, Google Analytics, the Netflix blog) and the 2016 Dyn reference reflect the time of writing.

## Relations
Follows WS-C17-002; summarized by WS-C17-004. Outbound firewall whitelisting for SSRF is in WS-C16-005.
