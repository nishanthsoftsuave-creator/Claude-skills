---
id: WAS-C25-004
title: Database-Specific Defenses
source_pages: "295"
chapter: 25
concepts: [database-specific-defenses, sql-escaping, oracle-encoder, mysql-quote, real-escape-string, parameterization-fallback]
related: [WAS-C25-003, WAS-C13-001]
time_sensitive: true
---
# Database-Specific Defenses
(Source: PDF p. 295)

## What the section covers
Escaping functions that individual SQL databases provide, used in addition to prepared statements. The page continues with the Generic Injection Defenses heading, which belongs to the next row.

## Meaning
Besides prepared statements, each major SQL database has its own functions that improve security. Oracle, MySQL, MS SQL and SOQL are named as offering ways to escape characters and character sets considered risky in queries. How the sanitization is decided depends on the database and engine (PDF p. 295).

## How it works
- Oracle with Java: an encoder is invoked through the ESAPI encoder, with an Oracle codec and the string to encode (PDF p. 295). The printed method name is spelled `enodeForSQL`, which looks like a typo in the book.
- MySQL `QUOTE`: escapes backslashes, single quotes and NULL, and returns a correctly single-quoted string (PDF p. 295).
- MySQL `mysql_real_escape_string()`: escapes backslashes and single quotes as well as double quotes, newline and carriage-return characters (PDF p. 295).

## Why it matters
Using these sanitizers makes it harder to write an SQL literal in place of a string (PDF p. 295).

## When and how to apply
Use them when a query cannot be parameterized. The book says they are a mitigation, not a comprehensive defense (PDF p. 295).

## Time-sensitive statements
Function names reflect the database versions available when the book was written.

## Relations
Secondary to WAS-C25-003; the attack is WAS-C13-001.
