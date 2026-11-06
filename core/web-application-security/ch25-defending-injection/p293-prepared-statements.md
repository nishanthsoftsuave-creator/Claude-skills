---
id: WAS-C25-003
title: Prepared Statements
source_pages: "293-294"
chapter: 25
concepts: [prepared-statements, bind-variables, query-compilation, sql-injection-prevention, parameterized-queries, mysql-prepare, performance-tradeoff]
related: [WAS-C25-002, WAS-C25-004, WAS-C13-001]
time_sensitive: false
---
# Prepared Statements
(Source: PDF pp. 293-294)

## What the section covers
The first line of defense against SQL injection: preparing the query before user data arrives.

## Meaning
SQL queries have long been widespread and dangerous but not very hard to defend against. Many SQL implementations support prepared statements, which cut the risk of using user-supplied data in a query, are easy to learn and make debugging easier. A tip box calls them the "first line" of defense, easy to implement, well documented and highly effective (PDF p. 293).

They work in two steps. The query is compiled first with placeholders, called bind variables or placeholder variables. Then the placeholders are replaced with the developer-provided values. The query's intent is fixed before any user-submitted data is considered (PDF p. 293).

## Why it matters
In an ordinary query, data and query text travel together as one string, so manipulated data can change the query's meaning. With a prepared statement the query cannot change: a SELECT cannot be escaped into a DELETE, and a second query cannot follow the first. It removes most SQL injection risk and is supported by nearly every major SQL database, including MySQL, Oracle, PostgreSQL and Microsoft SQL Server (PDF p. 294).

## How it works
The MySQL example prepares a statement named `q` that selects name and barcode from products where price is at most a placeholder; sets a price variable to 12; executes `q` using it; then deallocates the statement so its name can be reused for other things. Even if the price were set to a value followed by an extra UPDATE statement, the second query would not run because it was never compiled. The unsafe version concatenates the price into the SQL string (PDF p. 294).

## Alternatives and trade-offs
The only major cost is performance: the database receives the statement and then the values separately, rather than in one trip. In most applications the loss is minimal. Syntax differs between databases and adapters (PDF p. 294).

## Relations
Builds on detection in WAS-C25-002; WAS-C25-004 covers extra database-specific escaping; the attack is WAS-C13-001.
