---
id: WAS-C01-009
title: Hackers in the Modern Era, Circa 2015+
source_pages: "47-49"
chapter: 1
concepts: [modern-hackers, web-2-0, same-origin-policy, content-security-policy, tls, logic-bugs, third-party-dependencies, cloud-applications]
related: [WAS-C01-008, WAS-C01-010]
time_sensitive: true
---
# Hackers in the Modern Era, Circa 2015+
(Source: PDF pp. 47-49)

## What the section covers
A recap of the historical lessons, a description of the web application landscape when the book was written (2019), and why today's hackers target application logic.

## Recap of the lessons (PDF p. 47)
- Enigma in the 1930s showed the importance of security and how far others go to break it.
- The 1940s showed early security automation, driven by the contest between attackers and defenders: once Enigma improved beyond manual cryptanalysis, Turing automated the attack.
- The 1950s and 1960s showed that hackers and tinkerers have much in common, and that technology designed without thinking of malicious users will eventually be broken, so the worst case must always be considered for technology deployed at scale.
- In the 1980s personal computers became popular and recognisable hackers emerged, hiding viruses inside legitimate applications and spreading them over networks.
- The web and Web 2.0 made the internet a medium for sharing applications, which produced exploits against the user rather than the network or server. That is still true: most hackers now target web applications through browsers instead of desktop software and operating systems (PDF pp. 47-48).

## The landscape in 2019 (PDF p. 48)
- The author started writing in 2019, when thousands of sites were backed by million- and billion-dollar companies, many earning all their revenue from their sites, such as Google, Facebook, Yahoo!, Reddit and Twitter.
- YouTube is the example of a Web 2.0 site (Figure 1-6, a screenshot of its home page): users interact with each other and the application, uploads carry variable permissions, much data persists across sessions, some features reflect changes between users in near real time through notifications, and a lot of critical functionality is offloaded to the browser rather than the server.
- Traditional desktop companies are moving products to what is now called the cloud, a complex network of servers, for instance Adobe's Creative Cloud and Microsoft Office as web applications.
- With so much money parked in web applications the stakes are the highest ever, making them ripe for exploitation with very high rewards. The author calls this one of the best eras for both hackers and security-minded engineers, with work in demand on both sides of the law.

## Why hackers now target logic (PDF p. 49)
- Browsers are far more advanced than ten years earlier and ship many security features. Same Origin Policy (SOP) isolates websites of different origins, so one site cannot access another even when both are open or one is framed in the other.
- Content Security Policy (CSP) lets a site's developer set levels of security, for example whether scripts may execute inline in the HTML.
- HTTP has adopted SSL and TLS, which enforce strong encryption of data on the network and make man-in-the-middle attacks very hard.
- So many of the most successful hackers now go after the logic developers write in their web applications, since exploiting code bugs is easier than attacking the browser. Modern applications are many times larger and more complex than earlier ones, often with hundreds of open source dependencies, integrations with other sites, several databases of different types, and several servers in several locations. These are the applications the book targets.
- In summary: the past decade's hackers attacked servers, networks and browsers; the modern hacker mostly breaks into web applications through vulnerabilities in code, often side effects of advanced user interaction.

## Time-sensitive statements
The state of browsers, the named companies and products, and the claims about the current job market reflect 2019, when the book was written.

## Relations
Builds on WAS-C01-008 and is summarised in WAS-C01-010.
