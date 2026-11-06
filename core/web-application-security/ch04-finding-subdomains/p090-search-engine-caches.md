---
id: WAS-C04-004
title: Search Engine Caches
source_pages: "90-91"
chapter: 4
concepts: [google-dorking, search-operators, site-operator, inurl-operator, subdomain-discovery, false-positive-filtering, search-engine-index]
related: [WAS-C04-003, WAS-C04-005, WAS-C04-006]
time_sensitive: true
---
# Search Engine Caches
(Source: PDF pp. 90-91, with the end of the technique on the top of PDF p. 92)

## What the section covers
Using the query operators of a search engine, mainly Google, to surface subdomains that a search engine has already indexed, and narrowing the results step by step by excluding hosts you already know.

## Meaning
- Google is described as the most used search engine and probably the one that has indexed the most data. A plain search would drown you in results, and Google has cracked down on automated requests, rejecting those that do not closely resemble a real browser (PDF p. 90).
- Special operators raise the specificity of a query. The "site:" operator restricts the search to one domain, for example a query for the login pages of the target domain (PDF p. 90).
- The minus operator adds negative conditions. Writing minus-inurl followed by a pattern rejects every result whose URL matches the pattern (PDF p. 90).

## How it works
1. Search with the site operator for the target domain. On a popular site this returns pages of content from the main domain and very little from interesting subdomains (PDF p. 90).
2. Exclude the subdomains you already know. Adding the exclusion for "www" to the site query hides the main application's pages so other hosts show up (PDF p. 90).
3. Caveat: the exclusion matches the whole URL string, not just the host. A URL such as an admin host with "www" in its path would also be removed, so false-positive removals are possible (PDF p. 90).
4. Figure 4-4 demonstrates the combination on Wikipedia: a query for pages about puppies on that domain that leaves out URLs containing the word dog. The screenshot shows roughly 73,600 results in about half a second, an image strip, a Puppy article result and a "People also ask" box (PDF p. 91). The book prints the exclusion operator with a doubled hyphen in the caption and in the running text, but the query in the figure uses a single one. The text adds that the combination narrows the result count and lets you search specific subdomains while ignoring keywords, and that mastering the operators of Google and other engines surfaces information not easily found otherwise (PDF pp. 90-91).
5. Worked example on Reddit: querying its domain while excluding "www" first returns the code subdomain, an archive of code from the early versions of Reddit that the staff chose to publish. Sites purposely expose domains like this (PDF pp. 90-91).
6. For the MegaBank test, any additional domain that is intentionally public and uninteresting is filtered out in the same way (PDF p. 91).

## Continuation at the top of the next page
The section ends on the following page: a mobile host, if the bank had one, can be filtered by adding a second exclusion so the query excludes both "www" and "mobile". You repeat the process until no more relevant results appear. It may help to try other search engines such as Bing because the large engines support similar operators. Record anything interesting and then move on to other subdomain recon methods (PDF p. 92).

## When and how to apply
INTERPRETATION: this is the cheapest passive technique, so run it early and iterate, adding an exclusion for each new host you identify.

## Limitations
Results are only as complete as the engine's index, and excluding by URL substring can hide legitimate hits (PDF p. 90).

## Time-sensitive statements
Search operator behaviour, the result count in Figure 4-4 and Google's handling of automated requests are as of the time of writing.

## Relations
Part of the public-records group introduced in WAS-C04-003. Next technique: archived snapshots in WAS-C04-005; then social media in WAS-C04-006.
