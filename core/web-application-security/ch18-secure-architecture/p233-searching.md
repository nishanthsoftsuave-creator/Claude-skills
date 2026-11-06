---
id: WAS-C18-007
title: Searching
source_pages: "233-234"
chapter: 18
concepts: [search-engine, database-synchronization, elasticsearch, stale-search-data, permissions-sync, single-source-of-truth, megamerch]
related: [WAS-C18-001, WAS-C18-006, WAS-C18-008]
time_sensitive: true
---
# Searching
(Source: PDF pp. 233-234)

## What the section covers
The security consequences of adding a search engine to an application, mainly the need to keep a second database in step with the primary one, and the book's note on Elasticsearch.

## Why a search engine is a security concern
- Any application that builds its own search engine should think through what that involves (PDF p. 233).
- Search engines need data stored in a way that makes particular queries efficient, and that layout differs from how data is best stored in a general-purpose database.
- So most applications that add search need a separate database from which the engine draws. The book says this could cause complications that call for security architecture up front rather than later (PDF pp. 233-234).

## How the risks arise
- Syncing two databases is a big undertaking. If the permissions model changes in the primary database, the search database must be updated to match (PDF p. 234).
- A bug may delete a model in the primary database but not in the search database. Metadata about an object can then stay searchable after the object is removed from the primary database (PDF p. 234).
- The book says these concerns apply before implementing any search engine, whether Elasticsearch or an in-house one.

## Elasticsearch
- The book calls Elasticsearch the largest and most widely used open source distributed search engine, easy to configure, well documented and free to use, and says it is built on top of Apache's Solr project (PDF p. 234).
SUPPLEMENTARY: Elastic's own documentation describes Elasticsearch as built on the Apache Lucene library, which Solr is also built on; the book's wording (on top of Solr) differs and is recorded as printed.
- Figure 18-3 is a screenshot of the Elastic site-search marketing page, with a call to crawl and search a website; it illustrates the product only.

## When and how to apply
INTERPRETATION: treat the search index as a second copy of sensitive data, and design its deletion and permission updates at the same time as the primary store.

## Time-sensitive statements
Popularity and cost statements about Elasticsearch reflect the time of writing.

## Relations
Follows PII storage (WAS-C18-006) and was named as a risk area in WAS-C18-001. The chapter's closing argument is in WAS-C18-008.
