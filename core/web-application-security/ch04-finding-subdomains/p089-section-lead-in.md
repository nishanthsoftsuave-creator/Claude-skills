---
id: WAS-C04-003
title: Taking Advantage of Public Records (lead-in)
source_pages: "89"
chapter: 4
concepts: [public-records, accidental-data-leaks, osint, search-engines, social-media, web-archives, subdomain-discovery]
related: [WAS-C04-004, WAS-C04-005, WAS-C04-006, WAS-C04-002]
time_sensitive: false
---
# Taking Advantage of Public Records (lead-in)
(Source: PDF p. 89)

## What the section covers
The introduction to the group of subdomain-finding techniques that rely on information already published somewhere on the web. This row covers only the text under the "Taking Advantage of Public Records" heading, before its first subsection. The few lines at the very top of the page finish the preceding network-tools section (see WAS-C04-002).

## Why it matters
- The amount of publicly stored information is so large that an accidental leak can sit unnoticed for years. A capable hacker can mine this and find tidbits that make a later attack easy (PDF p. 89).
- For subdomain hunting specifically, public records help because a subdomain that a dictionary would never guess may still have been indexed by one of the services described next (PDF p. 89).

## Examples of what the author has found in public data during penetration tests
- Cached copies of GitHub repositories that were accidentally made public and then made private again.
- SSH keys.
- Keys for services such as Amazon AWS or Stripe that were exposed for a while and then removed from a public-facing application.
- DNS listings and URLs that were never meant for a public audience.
- Pages describing unreleased products that were not supposed to be live.
- Financial records hosted on the web but not intended to be crawled by a search engine.
- Email addresses, phone numbers and usernames (PDF p. 89).

## Where such information lives
Search engines, social media posts, archiving applications such as archive.org, and image searches including reverse image searches (PDF p. 89). The three following subsections work through search engine caches, web archives and social media.

## Relations
The technique-level detail is in WAS-C04-004 (search engine caches), WAS-C04-005 (archives) and WAS-C04-006 (social snapshots).
