---
id: WAS-C04-006
title: Social Snapshots
source_pages: "94-96"
chapter: 4
concepts: [social-media-recon, twitter-api, search-api, streaming-api, firehose-api, subdomain-discovery, api-rate-limits, recon-ethics]
related: [WAS-C04-003, WAS-C04-004, WAS-C04-005, WAS-C04-007]
time_sensitive: true
---
# Social Snapshots
(Source: PDF pp. 94-96, with the end of the section on the top of PDF p. 97)

## What the section covers
Finding subdomains that a company advertises on social media, using the Twitter API as the worked example, and choosing among its search, streaming and firehose offerings.

## Meaning and framing
- The author says major social media companies earn money by selling user data, which can include public posts, private posts and sometimes direct messages, while marketing the idea that private data is safe; the book suggests such security claims are often made mainly to attract and keep active users. Few countries have laws that enforce those claims, and many users likely do not understand what is shared, how and why (PDF p. 94).
- Finding subdomains for a company-sponsored pen test this way would not be seen as unethical by most, but the reader is urged to consider the end user when using these APIs for more targeted recon (PDF p. 94).
- Every major social network offers a similar suite of APIs, so the concepts transfer from the Twitter example to the others (PDF p. 94).

## Twitter API offerings
- Twitter's offerings differ in scope, feature set and data set. The more data you want and the more ways you want to filter it, the more you pay. Some searches can even run on Twitter's servers rather than locally. Using this for malicious purposes probably violates the terms of service, so the usage described is for white-hat work only (PDF p. 94). Figure 4-6 shows the developer documentation landing page (PDF p. 95).
- The lowest tier is a trial "search API" that covers 30 days of tweets, with at most 100 tweets per query, at most 30 queries per minute, and a monthly cap of 250 queries. The maximum monthly dataset at that tier can be gathered in about ten minutes and amounts to 25,000 tweets (PDF p. 95).
- These limits make writing analysis tools awkward; if the recon is for a work project the text suggests upgrading or using other data sources (PDF p. 95).

## How it works
Goal: build a JSON result of links to hosts under the target domain. Requirements are a registered developer account, a registered app and a bearer token included in requests for authentication (PDF p. 95). The query is a POST sent with curl to the 30-day search endpoint, with an authorization header carrying the bearer token, a JSON content type and a JSON body that sets the maximum results to 100 and the keyword to the target domain (PDF pp. 95-96).
- The search is fuzzy by default. For exact matches the keyword string must itself be wrapped in escaped double quotes inside the JSON (PDF p. 96).
- Record the results and look for links; subdomains found this way typically come from marketing campaigns, ad trackers and hiring events tied to a server other than the main app (PDF p. 96).
- Real-life example: a query about Microsoft turns up careers, office, powerbi and support subdomains that the company promotes on Twitter, described as a job-posting site, the home of the Office product, the PowerBI product home and customer support (PDF p. 96).
- Popular tweets get indexed by search engines because of inbound links, so the Twitter API is more useful for less popular tweets; otherwise a search engine with the right operators can be more effective (PDF p. 96).

## Alternatives and trade-offs
- Streaming API: a live stream of current tweets, but only a tiny share; more than 99% may be missing. Useful if the target app is trending or very popular, not for a startup (PDF p. 96).
- Firehose API: like streaming but guaranteed to deliver all tweets matching your criteria. The section's last lines are on the next page: it is typically much more valuable than streaming for recon, because relevance matters more than quantity (PDF p. 97).

## When and how to apply
Rules given at the end (PDF p. 97): use the search API for most applications; consider firehose or streaming for large or trending apps; if historical data is acceptable, download a large historical dump and query it locally. Almost every major social site has a data API that can serve the same purpose, so try another if one fails.

## Time-sensitive statements
Tier names, limits (30 days, 100 tweets, 30 queries a minute, 250 monthly queries, 25,000 tweets), endpoint and the Microsoft subdomain list are as of the book's writing.

## Relations
Third public-records source after WAS-C04-004 and WAS-C04-005. The chapter next turns to DNS-level discovery in WAS-C04-007.
