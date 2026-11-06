---
id: WS-C08-002
title: Anatomy of a CSRF Attack
source_pages: "104"
chapter: 8
concepts: [csrf, get-request-side-effects, malicious-link, twitter-worm, state-changing-get]
related: [WS-C08-001, WS-C08-003, WS-C08-007]
time_sensitive: true
---
# Anatomy of a CSRF Attack
(Source: PDF p. 104. The text at the top of PDF p. 104 above the "Anatomy of a CSRF Attack" heading belongs to WS-C08-001. The "Mitigation 1: Follow REST Principles" heading at the bottom of the page begins WS-C08-003.)

## What the section covers
How CSRF attacks work in practice, why GET requests are the usual vehicle, and the early Twitter worm as the worked example (PDF p. 104).

## How it works
- Attackers usually launch CSRF by targeting sites whose GET requests change server state. A GET request fires when a victim clicks a link, so an attacker can craft a misleading link into the target site that performs an unexpected action (PDF p. 104).
- GET is the only HTTP request type whose entire contents are carried in the URL, which makes it uniquely vulnerable to CSRF, since a link alone can express the whole request (PDF p. 104).

## Example: the early Twitter worm
- In an early version of Twitter, tweets could be created through GET requests, not the POST requests the site uses today. That made it possible to build URL links that, when clicked, posted to the clicker's timeline. Listing 8-1 shows such a link: a share-update address on twitter.com whose status query parameter holds a short joke message about CSRF-ing tweets (PDF p. 104).
- One hacker used this to build a viral worm. Because a single GET could write a tweet, they made a malicious link that, when clicked, posted a tweet containing an obscene message plus the same malicious link. Readers of that tweet who clicked the link became victims too, posting the same thing (PDF p. 104).
- The hacker tricked only a handful of people at first. As more users read the tweets and clicked out of curiosity, they tweeted it as well, until tens of thousands were tricked into posting the initial offensive message. This was the first Twitter worm, and the development team scrambled to close the hole before it got out of hand (PDF p. 104).

## Why it matters
INTERPRETATION: The example shows how one state-changing GET endpoint can be spread virally through links that victims post themselves. The defence, taken up next, begins by making GET requests side-effect free (WS-C08-003).

## Relations
Introduced by WS-C08-001. Mitigations follow in WS-C08-003 to WS-C08-006; recap in WS-C08-007.

## Time-sensitive statements
- The early Twitter GET-based tweet creation and the resulting worm are historical incidents; the book says the site now uses POST (PDF p. 104).
