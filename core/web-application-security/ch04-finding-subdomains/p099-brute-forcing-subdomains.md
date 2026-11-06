---
id: WAS-C04-008
title: Brute Forcing Subdomains
source_pages: "99-103"
chapter: 4
concepts: [subdomain-brute-force, asynchronous-requests, promises, dns-resolution, rate-limiting, detection-risk, node-dns-library, charset-generation]
related: [WAS-C04-009, WAS-C04-007, WAS-C04-010]
time_sensitive: false
---
# Brute Forcing Subdomains
(Source: PDF pp. 99-103, with the end of the combined program and its sample output on the top of PDF p. 104)

## What the section covers
The last-resort method for discovering subdomains: generate candidate names, test whether each resolves, and keep the ones that do. The book builds it as a small JavaScript program for Node.js in two parts and then combines them.

## Why it is a last resort
- Brute force is effective against applications with few defences, but against established ones it has to be structured very intelligently (PDF p. 99).
- It is easy to log and slow because of rate limits, regex-based filtering and other simple anti-snooping mechanisms. A warning box says such attempts are very easy to detect and can get your addresses logged or banned (PDF p. 99).
- Brute forcing means testing every possible combination until a match is found. With subdomains many names can be valid, so stopping at the first match is not enough (PDF p. 99).
- Unlike a local brute force this one needs the network, and each remote attempt adds roughly 50 to 250 ms of latency. The practical answer is to make requests asynchronous and fire them all off as quickly as possible instead of waiting for each reply (PDF pp. 99-100).

## How it works
The feedback loop is simple: generate a guess, send a lookup for the guess under the target domain, and mark the guess live if an answer comes back or unused if not (PDF p. 100). JavaScript is the chosen language because it is the only client-side language in browsers and, through Node.js, a strong server-side one. The program has three jobs: generate candidates, test each one, and record only the live ones (PDF p. 100).

Candidate generator (PDF pp. 100-101):
- It takes a maximum length and builds every combination from a character set. The set defaults to the lowercase Latin letters but can be extended, for example with a hyphen, and some browsers also accept Chinese, Arabic and other characters (PDF p. 100).
- It starts from single characters and, on each loop, extends every existing candidate with each character of the set. The code comment gives the cost as proportional to string length times the number of valid characters (PDF pp. 100-101). Calling it with a length of four yields every four-character name.
- The text explains it by describing the splitting of the set into an array, the loop over lengths, the nested loops over existing candidates and characters, and a temporary array that replaces the candidate list each round (PDF p. 101).

Resolver (PDF pp. 101-103): it runs on a recent Node.js installation in a Unix-like environment (PDF p. 101).
- It uses the DNS library built into Node.js, keeps an array of promises (the book calls promises a much simpler way to handle asynchronous requests, supported natively by every major browser and Node.js), walks the candidates with the array forEach operator, and for each candidate pushes a promise that asks the library to resolve the candidate under the target domain (PDF pp. 101-102).
- A promise resolves only when the library finishes its network request. A final step waits for all promises, then prints only results that came back with an address; a double negation in the condition keeps only defined answers (PDF pp. 102-103).
- If the code also rejected promises, a catch step would be needed for errors. The DNS library throws several errors, some not worth interrupting the run for; the example leaves this out and calls it a good exercise to add (PDF pp. 102-103).
- The resolve function is preferred over the more common lookup function. Both look asynchronous from JavaScript, but lookup relies on an operating-system routine implemented synchronously through libuv, so it is slower for this use (PDF pp. 102-103).
- The two parts are combined into one program: generate the list, then resolve it all asynchronously (PDF p. 103).

## Output (continuation on the next page)
The combined program ends on the next page. After a short wait it prints a list of valid names with their addresses; the book's sample shows mail, admin, dev, test, www, shop, ftp and forum hosts, each with an example IP (PDF p. 104).

## When and how to apply
INTERPRETATION: because random brute force is slow and noisy, run a dictionary of likely names first (see WAS-C04-009) and fall back to generated names only if that finds nothing.

## Limitations
Detectability, rate limiting and the cost of the search space grow quickly with name length (PDF p. 99).

## Relations
Follows zone transfer attempts (WAS-C04-007) and is superseded in efficiency by the dictionary approach (WAS-C04-009). Chapter lessons are in WAS-C04-010.
