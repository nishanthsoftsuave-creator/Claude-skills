---
id: WS-C06-002
title: SQL Injection
source_pages: "78-83"
chapter: 6
concepts: [sql-injection, bind-parameters, parameterized-statements, orm, defense-in-depth, least-privilege, dml-ddl, blind-sql-injection, nosql-injection]
related: [WS-C06-001, WS-C06-003, WS-C06-006, WS-C07-002, WS-C12-003]
time_sensitive: true
---
# SQL Injection
(Source: PDF pp. 78-83, tail PDF p. 84. The text on PDF p. 78 above the "SQL Injection" heading belongs to WS-C06-001; the tail page text above the "Command Injection" heading belongs here.)

## What the section covers
How SQL databases are used by web code, how an insecurely built SQL statement lets an attacker change its meaning, and the mitigations: bind parameters, object-relational mapping, defense in depth with least privilege, and limiting what error messages reveal (PDF pp. 78-84).

## Why it matters
SQL injection targets sites that use an underlying SQL database and construct queries insecurely. Because SQL databases are so common, it is one of the greatest risks a website faces (PDF p. 78). The book's example is a 2008 breach in which hackers stole 130 million credit card numbers from Heartland Payment Systems, a payment processor that stores card details for merchants; the attackers used SQL injection to reach the web servers handling payment data (PDF p. 78). Later the book calls it probably the biggest risk your site will face, and says that if you are unsure whether you use parameterized statements, you should go check immediately (PDF p. 81).

## Meaning: what SQL is
- Structured Query Language extracts data and data structures from relational databases, which keep data in tables where each row is one item such as a user or product (PDF p. 78).
- Four statement types: INSERT adds rows, SELECT reads rows, UPDATE changes rows, DELETE removes rows (PDF p. 78).
- Listing 6-1 shows what a server might run behind a signup and login flow: an INSERT creating a user row with an address and an encrypted password, a SELECT matching both when the user logs in, an UPDATE when the password changes, and a DELETE when the account is closed (PDF p. 79). The UPDATE line as printed is syntactically odd; it is recorded here only as an illustration of the statement type.
- For each interaction the web server takes parts of the HTTP request (for example login form fields) and builds a SQL statement. The statement is run through the database driver, a code library dedicated to talking to the database (PDF p. 79).

## How it works: anatomy of the attack
- The vulnerability arises when the server builds the SQL string insecurely, so arguments from the HTTP request make the driver do something the developer did not intend (PDF p. 79).
- Listing 6-2 is Java code that builds a login query by concatenating the email and password request parameters straight into the SQL text. Control characters such as the single quote are not checked, so an attacker can craft input that changes the statement's meaning and bypasses authentication (PDF pp. 79-80).
- Authentication bypass (Listing 6-3): the attacker supplies an address ending in a single quote followed by two dashes. The quote closes the email argument early and the dashes begin a SQL comment, so the driver runs only the first part and ignores the password check. The attacker can log in as any user without knowing the password by adding just those two characters to the address typed into the login form (PDF p. 80).
- Destructive attack (Listing 6-4): the attacker supplies an address followed by a quote, a semicolon, a DROP TABLE users statement and the comment marker. The semicolon ends the first statement and the driver runs the second, destroying the users table and leaving the database corrupt (PDF p. 80).
- With a vulnerable site an attacker can often run arbitrary SQL: bypass authentication; read, download and delete data at will; even inject malicious JavaScript into pages shown to users (PDF p. 80). Tools such as Metasploit can crawl sites and test HTTP parameters for such flaws, so a vulnerable site will eventually be exploited (PDF p. 80).

## Mitigation 1: use parameterized statements
- Build SQL with bind parameters, placeholder characters the driver replaces safely with the supplied values. A statement containing them is a parameterized statement (PDF pp. 80-81).
- SQL injection works by using control characters to jump out of the intended context. With bind parameters those characters are prefixed with escape characters, so the database does not treat them as control characters, which defuses the attack (PDF p. 81).
- Listing 6-5 shows the safe shape: the query text uses question marks in place of values, and the values are bound to the statement separately.

```
SELECT * FROM users WHERE email = ? AND encrypted_password = ?
```

- Listing 6-6 shows the quote-and-dashes attack input now being treated purely as data (the book's lead-in sentence calls this the method of Listing 6-4, although the quote-and-dashes input is the one shown in Listing 6-3, and the printed address and trailing comma differ slightly from the earlier listing; recorded as printed, PDF p. 81): the driver does not end the statement early, the SELECT returns no users, and the attack fails. All control characters (quote, dashes, semicolon) are handled as input rather than as part of the statement (PDF p. 81).
- The same class of attack can arise whenever a web server talks to any backend by composing statements in that backend's native language. The book lists NoSQL databases (MongoDB, Apache Cassandra), distributed caches (Redis, Memcached) and LDAP directories. Each library has its own bind-parameter mechanism, so learn how it works and use it (PDF p. 81).

## Mitigation 2: use object-relational mapping
- Many frameworks let you reach data through an object-relational mapping (ORM) library, which maps table rows to in-memory objects so developers mostly need not write SQL. This protects against SQL injection in most circumstances, but custom SQL can still be vulnerable, so understand how your ORM works behind the scenes (PDF p. 82).
- The familiar example is Ruby on Rails ActiveRecord; Listing 6-7 looks up a user with a find-by-email call, which is safe because ORMs use bind parameters underneath (PDF p. 82).
- Most ORMs also have a back door for raw SQL. Listing 6-8 shows Rails code that concatenates email and password into a where clause as raw strings and is vulnerable. If an attacker can set the password to a quote followed by OR 1=1, the final clause is trivially true and disables the password check (Listing 6-9), letting them log in as that user (PDF p. 82).
- Listing 6-10 shows the fix: pass the where clause with question-mark placeholders and the values as an array, and ActiveRecord handles control characters in either parameter (PDF pp. 82-83).

## Bonus mitigation: defense in depth
- Always secure a site with redundancy. Checking code line by line is not enough; enforce security at every level of the stack so a failure at one level is covered by another. This is defense in depth (PDF p. 83).
- Analogy used: a home is secured mainly by locks, but also benefits from an alarm, cameras, insurance and perhaps a large, bad-tempered dog (PDF p. 83).
- For SQL injection it means bind parameters plus extra steps that limit the damage if an injection still succeeds (PDF p. 83).

### Principle of least privilege
- Every process and application should run with only the permissions it needs to do its permitted job. If an attacker compromises one component, the damage is limited to what that component could do (PDF p. 83).
- Give the database account your web server uses limited permissions. Most sites need only the data manipulation language (DML) subset: SELECT, INSERT, UPDATE, DELETE (PDF p. 83).
- The data definition language (DDL) subset, with CREATE, DROP and MODIFY (as the book names them), changes table structures. Web servers generally do not need it at runtime, so do not grant it. Restricting the account to DML reduces the harm if a code flaw is found (PDF p. 83).

### Blind and nonblind SQL injection
- If error messages leak sensitive detail to the client, such as a message that a unique constraint was violated because an email already exists in the users table, the attack is nonblind: the attacker receives immediate feedback on each attempt (PDF pp. 83-84).
- Generic messages like "could not find this username and password" or "an unexpected error occurred" make the attack blind, so the attacker operates in the dark with less to work with. Nonblind-vulnerable sites are much easier to compromise, so avoid leaking information in error messages (PDF p. 84).

## When and how to apply
INTERPRETATION: Treat bind parameters as the required default for every database or backend call, review any raw-SQL escape hatch in an ORM as suspect during code review, and give the runtime database account DML rights only.

## Relations
Command injection (WS-C06-003) applies the same escaping idea to the operating system; the chapter recap is WS-C06-006. Stored XSS can be planted through SQL injection, per WS-C07-002. Error-message leakage is revisited in WS-C12-003.

## Time-sensitive statements
- The 2008 Heartland Payment Systems breach and its 130 million stolen card numbers (PDF p. 78).
- Named products and libraries: Metasploit, Ruby on Rails ActiveRecord, MongoDB, Apache Cassandra, Redis, Memcached (PDF pp. 80-82).
