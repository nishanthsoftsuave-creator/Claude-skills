---
id: WAS-C13-001
title: SQL Injection
source_pages: "179-182"
chapter: 13
concepts: [injection, sql-injection, interpreter, string-concatenation, php-legacy, nodejs-sql, truthy-evaluation, stacked-queries]
related: [WAS-C13-002, WAS-C25-001, WAS-C25-003]
time_sensitive: true
---
# SQL Injection
(Source: PDF pp. 179-182, tail page 183)

## What the section covers
The opening of the injection chapter and its first form, SQL injection: what an injection attack is, why old PHP code was so exposed, why the problem has shrunk, and a Node.js example in which a concatenated query lets a caller read every user, drop a table or change their own balance.

## Meaning
- SQL injection is the best-known attack on web applications. It targets SQL databases: the attacker either supplies their own parameters to an existing query or escapes out of the query and writes one of their own. Because the SQL interpreter runs with elevated permissions by default, the usual result is a compromised database (PDF p. 179).
- It is the most common form of injection but not the only one. Every injection attack has two parts: an interpreter, and a payload from a user that gets read into that interpreter. So the same idea applies to command-line utilities such as FFMPEG, a video compressor, as much as to databases (PDF p. 179).
- The chapter's stated aim is to survey several forms so the reader understands what application architecture makes them possible and how a payload against a vulnerable API is formed and delivered (PDF p. 179).

## How it works
- Figure 13-1 (PDF p. 180) shows the flow in four boxes. A user sends a payload containing SQL escape characters and SQL code to an API endpoint. The endpoint queries a database using that input. The SQL interpreter is escaped and the user's own query runs, in the figure changing the user to "admin". The result may or may not be reflected back to the user, but the query has already run and done its damage.
- Historically many open source packages combined PHP and MySQL. Many of the best-known SQL injection holes arose because PHP tolerated mixing view, logic and data code: developers interleaved SQL, HTML and PHP in the same file, and that style was widely misused (PDF p. 180).
- The book's PHP example is a forum login page (PDF pp. 180-181). If the request is not a POST, the script echoes an HTML sign-in form. Otherwise it connects to MySQL using configuration values and builds a SELECT on the users table, asking for userId, username, admin and moderator, by concatenating the posted username and the SHA-1 of the posted password straight into the query string. Nothing is sanitized before the string is built. The code is not copied here; the point is that HTML, PHP and SQL are intermixed and the query is assembled by plain concatenation.
- The Node.js and Express example (PDF pp. 181-182) is a POST route on /users. It reads a user_id, connects to a SQL Server database through the mssql package, and runs a SELECT on the users table by appending user_id to the query text, then returns the result as JSON. The developer assumed the parameter had not been tampered with, which the book says is never a safe assumption.
- A legitimate id returns one user. A "truthy" value such as 1=1 turns the condition into something always true, so the query effectively becomes "give all user objects back to the requester" (PDF p. 182).
- A value that begins a new statement, such as an id followed by a semicolon and a DROP TABLE users command, appends a second query to the original, and the user table is destroyed (PDF p. 182).
- A stealthier variant (printed at the top of the next page, so the cite is the tail page) uses the appended statement to update the attacker's own record, for instance setting their in-app credits to 10000 instead of dumping or dropping data (PDF p. 183).

## Why the problem has shrunk
- PHP coding standards became stricter, the language gained tools to reduce the odds of injection, and PHP's popularity as an application language fell. The book cites the TIOBE index for a significant decline since about 2010 (PDF p. 181).
- It also states that injection vulnerabilities fell from nearly 5% of all vulnerabilities in 2010 to less than 1% today, citing the National Vulnerability Database (PDF p. 181). Even large open source PHP applications such as WordPress fell victim in the past (PDF p. 181).
- Lessons from PHP carried over to other languages, so SQL injection is harder to find now, but it remains possible and common in applications that ignore secure coding practice (PDF p. 181).

## Limitations and failure modes
The vulnerable pattern is always the same: user-controlled text concatenated into a query that an interpreter will run. The book defers defenses to Part III, noting that SQL injection defenses have been under development for more than two decades (PDF p. 183).

## Relations
The next section generalizes from SQL to any CLI or interpreter (WAS-C13-002). The defensive counterpart is the prepared-statement material in Chapter 25 (WAS-C25-001, WAS-C25-003).

## Time-sensitive statements
The TIOBE and National Vulnerability Database trend claims (decline since about 2010; under 1% of vulnerabilities) reflect the date of writing, around 2019.
