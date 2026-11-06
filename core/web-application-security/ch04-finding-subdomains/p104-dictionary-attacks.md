---
id: WAS-C04-009
title: Dictionary Attacks
source_pages: "104-106"
chapter: 4
concepts: [dictionary-attack, subdomain-wordlist, dnscan, wordlist-streaming, subdomain-discovery, node-streams, brute-force-alternative]
related: [WAS-C04-008, WAS-C04-007, WAS-C04-010]
time_sensitive: true
---
# Dictionary Attacks
(Source: PDF pp. 104-106)

## What the section covers
A faster alternative to brute force for finding subdomains: instead of generating every possible name, test names taken from a list of the most common ones.

## Meaning and why it works
- A dictionary attack iterates over many candidate subdomains like a brute force does, but the candidates come from a list of common names rather than being generated (PDF pp. 104-105).
- It is much faster and usually finds something of interest. Only the most peculiar, non-standard names stay hidden from it (PDF p. 105).

## A ready-made source of names
- dnscan, a popular open source DNS scanner, ships a list of the most common subdomains on the internet, built from millions of subdomains found in over 86,000 DNS zone records (PDF p. 105).
- The book prints the top 25 from that data, in order: www, mail, ftp, localhost, webmail, smtp, pop, ns1, webdisk, ns2, cpanel, whm, autodiscover, autoconfig, m, imap, test, ns, blog, pop3, dev, www2, admin, forum and news (PDF p. 105).
- The project's repository hosts files containing the top 10,000 subdomains, usable under its GNU version 3 license, which the book calls very open, and the source code is also available there (PDF p. 105).

## How it works
- Plug the dictionary into the earlier resolver program. Short lists can be hard-coded; a large list such as the 10,000-name file should be kept separate and read at runtime, which makes it easy to swap in other lists. Most such lists are in CSV format, so integration is simple (PDF p. 105).
- The program streams the list from disk instead of loading it into memory, in case the file is large. For each line it asks the DNS library to resolve that name under the target domain and stores the promise. When the stream ends and all promises settle, it prints the names that returned an address (PDF p. 106).
- The code comment adds a performance upgrade: if the list is exceptionally large, open a second file and stream results to it as each promise resolves (PDF p. 106).
- INTERPRETATION: the printed snippet hands each parsed row object to the hostname template, so a real run would first have to pull the name string out of the row.
- The book's point is that with a good dictionary (one search away) you can paste it into the brute force script and have a dictionary attack tool (PDF p. 106).

## When and how to apply
Because the dictionary approach is much more efficient, start with it and use generated names only if it does not return what you are looking for (PDF p. 106).

## Time-sensitive statements
The top-25 ranking and the file sizes come from the dnscan data as of the book's writing.

## Relations
Builds directly on WAS-C04-008; the chapter wrap-up is WAS-C04-010.
