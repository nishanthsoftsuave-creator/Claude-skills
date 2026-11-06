---
id: WAS-C03-016
title: Server-Side Databases
source_pages: "81"
chapter: 3
concepts: [server-side-databases, sql-databases, nosql-databases, mongodb, elasticsearch, data-persistence, sql-injection, multiple-databases]
related: [WAS-C03-015, WAS-C03-017, WAS-C13-001, WAS-C06-007]
time_sensitive: true
---
# Server-Side Databases
(Source: PDF p. 81 from the "Server-Side Databases" heading, plus the top of PDF p. 82 above "Client-Side Data Stores")

## What the section covers
Why servers persist data in databases, the main database families (SQL, NoSQL, specialised search databases) and the security consequence of running several of them side by side.

## Why databases
- Once a client sends data to a server, the server often has to persist it so a later session can retrieve it. Memory is not reliable in the long term, since restarts and crashes could lose data, and RAM is expensive compared to disk (PDF p. 81).
- Storing on disk requires care so the data can be reliably and quickly retrieved, stored and queried. Almost all web applications store user-submitted data in some type of database, often varying the choice by business logic and use case (PDF p. 81).

## Kinds of database
- **SQL databases** remain the most popular general-purpose choice. The query language is strict, reliably fast and easy to learn. It can serve anything from user credentials to JSON objects or small image blobs. The largest named are PostgreSQL, Microsoft SQL Server, MySQL and SQLite (PDF p. 81).
- **NoSQL (schema-less) databases** are used when more flexible storage is needed. MongoDB, DocumentDB and CouchDB store loosely structured "documents" that are flexible and modifiable at any time, but are not as easy or efficient to query or aggregate (PDF p. 81).
- **Specialised databases.** Search engines often use their own highly specialised databases, which must be synchronised with the main database regularly. The widely popular example given is Elasticsearch (PDF p. 81).

## Security consequences
- Every type of database carries unique challenges and risks. SQL injection is a well-known vulnerability archetype that works against major SQL databases when queries are not properly formed. Injection-style attacks can occur against almost any database if the attacker is willing to learn its query model (PDF p. 82).
- Many modern applications use more than one database at once. An application whose SQL query generation is secure may still have insecure MongoDB or Elasticsearch queries and permissions (PDF p. 82).

## When and how to apply
INTERPRETATION: when mapping a target, record every datastore you can infer, not just the main one, because each needs its own injection and permission review.

## Time-sensitive statements
The list of "largest" databases and products named reflects the time of writing.

## Relations
Follows web servers (WAS-C03-015) and precedes client-side stores (WAS-C03-017). SQL injection mechanics are in WAS-C13-001, and fingerprinting databases during recon in WAS-C06-007.
