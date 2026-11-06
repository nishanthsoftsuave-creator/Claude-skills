---
id: WAS-C26-001
title: Defending Against DoS (Chapter Introduction)
source_pages: "301"
chapter: 26
concepts: [dos-defense, request-logging, response-time-logging, async-job-logging, resource-exhaustion, dos-detection]
related: [WAS-C14-001, WAS-C26-002, WAS-C26-003]
time_sensitive: false
---
# Defending Against DoS (chapter introduction)
(Source: PDF p. 301)

## What the section covers
Why DoS is hard to detect after the fact, the first defensive measure (logging), and the three goals a DoS attack can pursue.

## Why it matters
DoS attacks consume system resources, so spotting them is difficult without solid server logging. A past attack that arrived through legitimate channels, such as an API endpoint, is especially hard to find later (PDF p. 301).

## How it works
The first measure is a logging system thorough enough that every request is recorded along with its time to respond. The book also says to log by hand the performance of asynchronous job-style functions, for example a backup triggered through the API that runs in the background and sends no response when finished. That logging makes it possible to find attempts, accidental or malicious, to exploit a server-side DoS weakness that would otherwise be slow to uncover (PDF p. 301).

## Meaning
DoS attacks aim at one or more of these results: exhausting server resources, exhausting client resources, or requesting unavailable resources. The first two are easier to exploit without knowing the server or client environment. A mitigation plan must consider all three (PDF p. 301).

## Relations
The attacks are described from WAS-C14-001; regex and logical DoS defenses follow in WAS-C26-002 and WAS-C26-003.
