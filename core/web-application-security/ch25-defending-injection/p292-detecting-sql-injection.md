---
id: WAS-C25-002
title: Detecting SQL Injection
source_pages: "292"
chapter: 25
concepts: [sql-injection-detection, code-search, database-adapters, nodejs-modules, domain-specific-language, multiple-databases, static-search]
related: [WAS-C25-001, WAS-C25-003, WAS-C20-002]
time_sensitive: true
---
# Detecting SQL Injection
(Source: PDF pp. 292-293)

## What the section covers
How to locate, in an existing codebase, the places where SQL queries are built, so they can be reviewed for injection risk.

## How it works
- Start by learning what SQL injection looks like and where the code is most exposed. In modern applications SQL work sits behind the server-side routing layer, so the client can be skipped (PDF p. 292).
- The book's sample repository has an `api` folder (routes, utils), an `analytics` folder (routes) and a `client` folder (pages, scripts, media). The client is skipped, but the analytics route is not, because even OSS-based analytics probably stores data in a database. Data that persists across devices and sessions lives in server memory, on disk (logs) or in a database (PDF p. 292).
- Many applications use more than one database, for example SQL Server and MySQL. Searches therefore have to be generic enough to find queries in several SQL dialects. Some server software uses a domain-specific language that can issue SQL on the developer's behalf, with a shape unlike raw SQL (PDF p. 292).
- Compile one list of every DSL and SQL type in use. In a Node.js example with the NodeMSSQL adapter and the mysql adapter, searches must cover both (PDF p. 292).

The continuation on the next page notes that Node's import system makes this easy when the library is imported per module: search for the `require` of each adapter. If libraries are declared globally or inherited from a parent class, the search is harder. The two adapters end in a `.query(x)` call, but some libraries use a literal builder style (select, from, where chained on a query object) in which a username is concatenated into the where clause (PDF p. 293).

## Time-sensitive statements
Adapter and package names are examples as of the book's writing.

## Relations
Follows WAS-C25-001; prepared statements, the fix, are WAS-C25-003. Static analysis that automates such searches appears in WAS-C20-002.
