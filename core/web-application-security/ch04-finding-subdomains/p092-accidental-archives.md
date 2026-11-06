---
id: WAS-C04-005
title: Accidental Archives
source_pages: "92-93"
chapter: 4
concepts: [web-archives, archive-org, historical-snapshots, subdomain-discovery, url-schemes, view-source, passive-recon]
related: [WAS-C04-004, WAS-C04-006, WAS-C04-003]
time_sensitive: false
---
# Accidental Archives
(Source: PDF pp. 92-93)

## What the section covers
Using public web archives, chiefly archive.org, to recover subdomains and links that an application once exposed but no longer shows, plus a manual routine for harvesting URLs from several old snapshots.

## Meaning
- Archiving utilities such as archive.org periodically build snapshots of websites, so you can view a past copy of a site. The service tries to preserve the history of the internet, since sites die and new ones take over their domains (PDF p. 92).
- Because snapshots can go back around twenty years, the archive is called a goldmine for information that was once disclosed, on purpose or by accident, and later removed. Figure 4-5 shows the Wikipedia home page as captured in 2003, nearly two decades before the book; its caption describes archive.org as a San Francisco-based nonprofit that has been around since 1996 (PDF p. 92).

## Why it matters
- Search engines index current data and recrawl sites to keep caches fresh, so they are the place to look for current data, while archives are the place for historical data (PDF p. 93).
- Example of scale: the front page of The New York Times website, one of the most popular web-based media companies by traffic, has more than 200,000 archived snapshots between 1996 and the book's writing (PDF p. 93).
- Snapshots are especially valuable if you know or can guess when the application shipped a major release or had a serious vulnerability disclosed. For subdomain hunting, old HTML or JavaScript often contains hyperlinks that are gone from the live application (PDF p. 93).

## How it works
In a snapshot you can use the browser's "View source" and search for common URL patterns. A search for the file scheme might reveal a once-live download; a search for http or https should list the hyperlinks (PDF p. 93).

Manual routine the book gives for harvesting the data (PDF p. 93):
1. Open ten archived copies taken on ten dates with long gaps between them.
2. Use "View source" and select all of the HTML.
3. Copy it and paste it into a local file, for example a file named for legacy source.
4. Repeat for each of the other nine snapshots, appending to the same file.
5. Open the file in a text editor.
6. Search for the common schemes: http, https, file, ftp and ftps.

The browsers' full list of supported URL schemes is defined in a specification that all major browsers follow (PDF p. 93).

## When and how to apply
INTERPRETATION: spread the sampled dates across the application's life, and add schemes beyond the five listed if the target is known to use others.

## Limitations
The routine is bounded by what the archive happened to capture. The book introduces these steps as a way to automate discovery of subdomains from an archive, yet every step is a manual copy-and-paste action (PDF p. 93).

## Relations
Same family as search engine caches (WAS-C04-004); social media is the third public-record source (WAS-C04-006).
