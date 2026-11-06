---
id: WAS-C14-002
title: Regex DoS (ReDoS)
source_pages: "194-195"
chapter: 14
concepts: [redos, regular-expressions, backtracking, malicious-regex, greedy-matching, input-validation, performance]
related: [WAS-C14-001, WAS-C14-003, WAS-C26-002]
time_sensitive: false
---
# Regex DoS (ReDoS)
(Source: PDF pp. 194-195, tail page 196)

## What the section covers
Regular-expression denial of service: why web applications use regular expressions, the minimal JavaScript regex syntax the chapter needs, why some regexes become slow through backtracking, and the book's timing tables showing cost doubling as input length grows.

## Meaning
- ReDoS is among the most common forms of DoS in web applications. Its risk runs from very minor to medium, often depending on where the regex parser runs (PDF p. 194).
- Applications use regexes to validate form fields: allowing only accepted characters in a password field, or capping a comment's length so it displays well (PDF p. 194).
- Regular expressions were designed by mathematicians studying formal language theory to describe sets of strings compactly. Almost every language used on the web has its own regex parser, JavaScript in the browser included (PDF p. 194).
- A "malicious" or "evil" regex is one that runs slowly on certain inputs. The book calls it a big risk where users can supply their own regexes for other forms or for the server. One can also enter an application by accident, although a developer who knows regexes will usually avoid the common mistakes (PDF p. 195).

## How it works
- JavaScript regexes are written either as a literal between two slashes or through a constructor that takes a string. Regexes are normally fast and powerful, and the book recommends learning at least the basics (PDF p. 194).
- The chapter needs only a few constructs: character ranges (lowercase, uppercase, digits), alternatives joined with a vertical bar, and a test function that returns true or false for a string. The example tests a pattern for the word "dog" against "cat" (false) and "dog" (true) (PDF p. 194).
- Parsing is usually so fast that a regex rarely slows an application, but a regex can be written to run slowly (PDF pp. 194-195).
- Most malicious regexes are built with the plus operator, which makes matching "greedy": the engine looks for one or more matches rather than stopping at the first. When such a regex reaches a failure case it backtracks, retrying other ways of splitting the input (PDF p. 195).
- The book's worked example is a pattern with a repeated group nested inside another repetition, anchored to the whole string. On a well-formed input of repeated pairs it finishes quickly. When the input is made invalid at its very end, the engine does not give up at once: it tries the alternative groupings one after another, and the number of alternatives grows with the length of the string, so the match slows (PDF p. 195).
- The book describes this as the engine exhaustively trying all valid combinations before it can decide the string does not match (PDF p. 195).

## Evaluation: the timing tables (printed on the tail page)
- Table 14-1 (PDF p. 196) times the problematic regex on a failing input: 23 characters take 8 ms, 25 take 15 ms, 27 take 31 ms and 29 take 61 ms. The time roughly doubles for every two characters added. Computed on a server this can cause a significant performance drop; computed on a client it can crash the browser.
- Table 14-2 (PDF p. 196) shows the same regex is not slow on every input. For well-formed inputs of 22, 24 and 26 characters the time is shown as under 1 ms. The 28-character row is printed with a "greater than 1 ms" comparator, which looks like a slip in the book.
UNVERIFIED: the intended comparator in the 28-character row of Table 14-2, because the printed symbol conflicts with the other rows.

## Limitations and failure modes
- A problematic regex can sit unnoticed in an application for years and then seem to appear from nowhere when an input triggers heavy backtracking (PDF p. 196).
- ReDoS is more common than expected and can take down a server or make client machines unusable. Open source is often more exposed because few developers can recognise a malicious regex (PDF p. 196).

## Relations
Follows WAS-C14-001 and precedes logical DoS (WAS-C14-003). Defenses are in WAS-C26-002.
