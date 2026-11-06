---
id: WS-I-003
title: A Brief History of the Internet
source_pages: "22-24"
chapter: intro
concepts: [web-history, javascript-origins, cross-site-scripting, internet-explorer, malware, cgi, php, injection-attacks, directory-traversal, botnets, iot]
related: [WS-I-002, WS-I-004, WS-C03-003, WS-C02-002]
time_sensitive: true
---
# A Brief History of the Internet
(Source: PDF pp. 22-24. The heading starts part-way down PDF p. 22. The subsection "What to Worry About First" begins at the top of the next PDF page, the first page of WS-I-004; it is summarised at the end of this module without a page cite.)

## What the section covers
A short narrative of how the web reached its present state, told to explain how security weaknesses entered the technology. The author notes that, as in most software projects, security took a back seat while features were added, and knowing how vulnerabilities crept in gives context for learning to fix them (PDF p. 22).

## Origins of the web
- The World Wide Web was invented by Tim Berners-Lee at CERN, the European nuclear research organisation, as a way for universities to share findings. He built the first browser and first web server and created HTML and HTTP. The first website went live in 1993 (PDF pp. 22-23).
- Early pages held only text. The first browser to show inline images was Mosaic, from the National Center for Supercomputing Applications. Its creators later joined Netscape Communications and helped build Netscape Navigator, the first widely used browser. Early pages were mostly static and traffic was not encrypted (PDF p. 23).

## Scripting in the browser
- In 1995 Brendan Eich, newly hired at Netscape, took 10 days to create JavaScript, the first language that could be embedded in web pages. It was called Mocha, then LiveScript, then JavaScript, and was formalised as ECMAScript, a name people avoid outside formal settings (PDF p. 23).
- The language borrowed naming habits from Java (unrelated), C-style syntax, prototype inheritance from Self, and an odd type-conversion scheme of Eich's own (PDF p. 23).
- JavaScript became the de facto browser language. Pages turned interactive, and a whole class of vulnerabilities followed: attackers learned to inject JavaScript into pages through cross-site scripting (PDF p. 23).

## A new challenger
- Internet Explorer was the first real rival to Navigator. It was free and came preinstalled on Windows, so it rapidly became the most popular browser (PDF p. 23).
- Microsoft's push to "own" the web brought proprietary technology such as ActiveX into the browser, which increased malware, since Windows has long been the main virus target and the internet was an effective delivery route (PDF p. 23).
- Explorer's dominance lasted until Mozilla Firefox and then Google's Chrome arrived, which sped up innovation in internet standards. By then hacking was profitable, and flaws were exploited as soon as discovered. Browser vendors made security a top priority, and site owners had to follow security news to protect users (PDF pp. 23-24).

## Machines for writing HTML
- Early web hosting was a niche academic hobby, and most universities ran Linux. In 1993 the Linux community implemented the Common Gateway Interface (CGI), which let webmasters build sites of linked static HTML pages (PDF p. 24).
- CGI also allowed scripting languages such as Perl or PHP to generate HTML dynamically from database content. PHP originally meant Personal Home Page, from the hope that everyone would run their own server (PDF p. 24).
- PHP popularised the template file: HTML with embedded processing tags run through the PHP engine. Dynamic PHP sites, such as the earliest Facebook, flourished (PDF p. 24).
- Dynamic server code brought new vulnerability categories: injection attacks that run an attacker's code on the server, and directory traversal that explores the server's filesystem (PDF p. 24).

## A series of tubes
- Much of today's internet runs on old technology. Software tends to reach "good enough" and go into maintenance mode, especially web servers that must stay online around the clock. Hackers scan for vulnerable sites on older technology. Issues first found a decade ago are still being fixed, which is why the book covers every major flaw (PDF p. 24).
- The internet is also growing faster than ever by connecting everyday devices (cars, doorbells, refrigerators, light bulbs, cat-litter trays). The simpler the appliance on the Internet of Things, the less likely it updates itself securely. These unsecured nodes are a rich host environment for botnets, malicious agents that attackers install and control remotely, giving an attacker large potential firepower against a target site (PDF p. 24).

## What to worry about first (continues on the next page)
This subsection opens the next page and is part of the Introduction's closing reassurance. It says a developer should not be discouraged: security researchers discover, document and fix flaws, and the tools needed are free and usually easy to use. Learning the most common vulnerabilities and how to plug them protects against 99 percent of attacks. A very technical adversary can still compromise a system, but unless you are running an Iranian nuclear reactor or a US political campaign (the book's own examples), this thought should not keep you up at night.

## Relations
Browser scripting history is expanded in WS-C03-003; cross-site scripting, injection and directory traversal get their own chapters listed in WS-I-004; the TCP/IP basics are in WS-C02-002.

## Time-sensitive statements
- Historical dates and products: first website in 1993, CGI in 1993, JavaScript in 1995, Mosaic, Netscape Navigator, Internet Explorer, Firefox, Chrome, ActiveX, PHP.
- The 99 percent figure and the comments on current-day Internet of Things devices reflect the book's 2020 publication.
