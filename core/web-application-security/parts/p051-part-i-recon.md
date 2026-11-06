---
id: WAS-T-001
title: Part I - Recon (Opening)
source_pages: "51-52"
chapter: part-1
concepts: [recon-philosophy, application-purpose, functional-analysis, revenue-model, valuable-data, information-gathering, mental-model]
related: [WAS-C02-001, WAS-C02-002, WAS-P-005]
time_sensitive: false
---
# Part I - Recon (Opening)
(Source: PDF pp. 51-52)

## What the section covers
The philosophical introduction to the recon part of the book. Instead of a technical overview, which comes later, the author sets out what recon is really for: building a deep understanding of the target application.

## Two kinds of knowledge a hacker needs
- Exploiting web applications efficiently takes a wide array of skills. One kind is technical: network protocols, software development techniques and the common vulnerabilities found in different kinds of application (PDF p. 51).
- The other is understanding the specific application being targeted. The more intimate that knowledge, the better and more applicable it is (PDF p. 51).

## Functional questions to answer (PDF p. 51)
The hacker should grasp the application's purpose from a functional point of view and ask:
- Who are its users?
- How does the application make money?
- Why do users choose it over competitors, and who are those competitors?
- What functionality does the application contain?

## Why non-technical understanding matters
Without a deep, non-technical understanding, it is hard to tell which data and functionality matter. The example in the text compares two car-related sites. A car-sales application may treat stored objects representing cars for sale, with price and inventory, as mission-critical data. A hobby site where enthusiasts share modifications to their own cars may value user accounts more than the inventory in a user's profile. The same reasoning applies to functionality, not just data, because many applications earn revenue in several ways instead of one income stream (PDF p. 51).

## Monetisation example (PDF p. 52)
A media-sharing platform might offer a monthly subscription, serve ads and sell paid downloads. The questions to ask are: which stream is most valuable to the company, how does usage of each differ from a usability viewpoint, and how many users contribute revenue to each stream.

## Definition of recon
- Recon is about collecting data and building a model that combines the application's technical and functional details so its purpose and usage are fully understood. Without both halves, a hacker cannot target attacks properly (PDF p. 52).
- Philosophically it is about generating a deeper understanding of the target, and information is the key whether or not it is technical (PDF p. 52).
- Because the book is technical, most coverage will be on finding and analysing technical components, but it will also discuss functional analysis and a few ways to organise information. The reader is urged to do their own non-technical research whenever a recon opportunity arises (PDF p. 52).

## Relations
The practical side starts in WAS-C02-001 (information gathering) and WAS-C02-002 (mapping). The overview of why recon matters is in WAS-P-005.
