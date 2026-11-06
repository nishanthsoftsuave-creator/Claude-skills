---
id: WAS-C01-008
title: The Rise of the World Wide Web, Circa 2000
source_pages: "44-46"
chapter: 1
concepts: [world-wide-web, web-2-0, user-generated-data, application-platform, early-dos-attacks, activex-vulnerability, xss-history, phishing-history]
related: [WAS-C01-007, WAS-C01-009]
time_sensitive: false
---
# The Rise of the World Wide Web, Circa 2000
(Source: PDF pp. 44-46, with the end of the section on PDF p. 47)

## What the section covers
How the shift from static pages to user-driven applications (Web 2.0) moved hackers' attention to the user, and the first big web-era attacks.

## From documents to applications
- The web spread in the 1990s, but its popularity exploded at the end of that decade and in the early 2000s (PDF p. 44).
- In the 1990s it was used almost only for sharing HTML documents. Sites paid little attention to user experience and few let users send input back to change the site's flow (PDF p. 44). Figure 1-4, an Apple.com page from July 1997, shows purely informational content where a user cannot sign up, sign in, comment or persist data between sessions (PDF p. 45).
- In the early 2000s sites began storing user-submitted data and changing behaviour based on user input. This is called Web 2.0: users collaborate by submitting input over HTTP to a server, which stores it and shares it with others on request (PDF p. 44).
- That gave birth to social media as we know it and enabled blogs, wikis and media sharing sites (PDF p. 44).
- The web changed from a document-sharing platform into an application distribution platform. The text points to an Apple.com storefront from 2007 (Figure 1-5, an online store with items for sale) with an account link in the top right corner, which suggests user accounts and data persistence. The link had existed on earlier versions, but in 2007 it was promoted from the bottom of the page to the top right; it may have been experimental or underused before (PDF p. 45).

## A new target: the user (PDF p. 46)
- By then serious efforts had been made to secure servers and networks, the two leading attack vectors of the previous decade. With application-like websites, the user became the perfect target.
- Mission-critical functions such as military communications and bank transfers would eventually run through web applications. Few security controls protected users against attacks aimed at them, and education about hacking or about the mechanisms behind the internet was scarce. Few early 2000s users could grasp the technology working for them.

## Early attacks (PDF pp. 46-47)
- In the early 2000s the first widely publicised denial of service attacks shut down Yahoo!, Amazon, eBay and other popular sites (PDF p. 46).
- In 2002 Microsoft's ActiveX plug-in for browsers had a vulnerability that let a malicious website trigger remote file uploads and downloads (PDF pp. 46-47).
- By the mid-2000s hackers regularly used phishing sites to steal credentials, with no controls then protecting users against them (PDF p. 47).
- Cross-Site Scripting flaws, where a hacker's code runs in a user's session inside a legitimate site, ran rampant because browser vendors had not built defences. The author attributes many hacks of the era to web technology having been designed for a single user, the website owner, so it toppled when used to share data among many users (PDF p. 47).

## Relations
Continues from WAS-C01-007 and leads into the modern-era recap in WAS-C01-009.
