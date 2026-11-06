---
id: WAS-C22-005
title: Blob Sink
source_pages: "271"
chapter: 22
concepts: [blob, createobjecturl, script-injection, base64, dom-sinks, arbitrary-data]
related: [WAS-C22-002, WAS-C22-004, WAS-C22-006]
time_sensitive: false
---
# Blob Sink
(Source: PDF p. 271)

## What the section covers
How a Blob can be used to turn arbitrary data into an executing script, and the advice to avoid it.

## Meaning and mechanism
Blob carries the same risk as SVG. The book's example builds a Blob from a script with the MIME type text/javascript, makes an object URL for it, creates a script element whose source is that URL, and appends the element to the page body. That loads and executes the script (PDF p. 271).

## Why it is risky
Blobs can hold data in many formats. Base64 data held as a Blob is simply a container for arbitrary content, so a Blob can carry code (PDF p. 271).

## When and how to apply
Keep Blobs out of your code if you can, especially when any part of creating the Blob involves user data (PDF p. 271).

## Relations
One of the sinks listed in WAS-C22-002, alongside SVG (WAS-C22-004). Link handling is in WAS-C22-006.
