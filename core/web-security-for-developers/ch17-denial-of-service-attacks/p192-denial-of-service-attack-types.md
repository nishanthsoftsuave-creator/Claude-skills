---
id: WS-C17-002
title: Denial-of-Service Attack Types
source_pages: "192-193"
chapter: 17
concepts: [dos-asymmetry, icmp-flood, ping-of-death, syn-flood, slowloris, rudy, zip-bomb, reflection, amplification, ddos, botnet, memcached]
related: [WS-C17-001, WS-C17-003, WS-C15-004, WS-C16-006, WS-C02-002]
time_sensitive: true
---
# Denial-of-Service Attack Types
(Source: PDF pp. 192-193, tail PDF p. 194. The text at the top of PDF p. 192 above the "Denial-of-Service Attack Types" heading belongs to WS-C17-001. The "Unintentional Denial-of-Service Attacks" text on PDF p. 194, above the "Denial-of-Service Attack Mitigation" heading, is the end of this section and is covered here.)

## What the section covers
Why DoS works at all, then the attack families by network layer: ICMP, TCP, application layer, reflected and amplified, distributed, and accidental surges.

## Meaning: the underlying asymmetry
Answering a network request usually costs more than sending it. A web server handling an HTTP request must parse it, run database queries, write logs and build the HTML response. The requesting agent only needs to supply three items: the HTTP verb, the destination IP address and the URL. Attackers exploit this gap to swamp servers so real users cannot be served. Attacks exist at every layer of the network stack, not just HTTP, and the book expects more methods to be found (PDF p. 192).

## How it works: attack types
- ICMP attacks (PDF p. 192). The Internet Control Message Protocol lets servers, routers and command-line tools check whether an address is online: a request goes out and a live server confirms. The ping utility uses it. As the simplest internet protocol it was the first abused. A ping flood sends an endless stream of ICMP requests and takes only a few lines of code. The ping of death sends corrupt ICMP packets to crash a server, exploiting older software that does not bounds-check incoming ICMP packets.
- TCP attacks (PDF p. 192). Modern network interfaces defuse most ICMP attacks, so attackers moved up to TCP, which underpins most internet communication. A TCP conversation starts with the client sending SYN, the server replying SYN-ACK, and the client finishing the handshake with ACK. A SYN flood sends many SYN messages without ever finishing the handshake. The server is left with many half-open connections, the connection pool is used up, and legitimate clients are refused.
- Application layer attacks (PDF p. 193). These abuse HTTP. Slowloris opens many HTTP connections and keeps each open by periodically sending partial requests, draining the connection pool. R-U-Dead-Yet? (RUDY) sends never-ending POST requests with absurdly long Content-Length values so the server keeps reading meaningless data. Endpoint-specific attacks include uploading zip bombs, corrupt archives that grow exponentially when expanded, to fill the disk through a file upload feature. Any URL that deserializes request contents into in-memory objects may be vulnerable too; the XML bomb of chapter 15 (WS-C15-004) is an example.
- Reflected and amplified attacks (PDF p. 193). Attackers need a lot of computing power to generate traffic, so they have a third-party service do it. They send requests to the third party with a spoofed return address belonging to the victim, so the replies hit the victim. Reflection also hides the attack's origin. If the replies are bigger or more numerous than the request, they amplify the attack. One of the largest attacks to date used reflection: in 2018 a single attacker pointed 1.3 terabytes per second at GitHub by finding many insecure Memcached servers and sending them User Datagram Protocol (UDP) requests that carried GitHub's IP address as the source. Each reply was roughly 50 times the size of the request, multiplying the attacker's power by that factor.
- Distributed denial of service, DDoS (PDF p. 193). An attack from one IP address is easy to stop by blacklisting that address. Modern attacks such as the 2018 GitHub one use many cooperating sources. Besides reflection, they usually run from a botnet of malware-infected computers and internet-connected devices under the attacker's control. Because so many devices now connect to the internet, including thermostats, refrigerators, cars, doorbells and hairbrushes, and are prone to security flaws, bots have plenty of places to hide.
- Unintentional DoS (PDF p. 194). Not every traffic surge is malicious. A site can go viral and be unexpectedly overwhelmed because it was not built for the load. The book names the "Reddit hug of death" that regularly takes small sites offline when they reach that site's front page.

## Time-sensitive statements
The 2018 GitHub attack (1.3 terabytes per second, Memcached reflection, roughly 50 times amplification) and the Reddit example are dated incidents and named products (PDF pp. 193-194).

## Relations
Follows WS-C17-001; defences are in WS-C17-003. Botnets are introduced in WS-C16-006.
