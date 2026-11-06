---
id: WS-C12-005
title: "Chapter 12 Summary: Information Leaks"
source_pages: "144"
chapter: 12
concepts: [chapter-summary, information-leakage, server-header, clean-urls, generic-cookie-name, error-reporting, minification, security-advisories]
related: [WS-C12-002, WS-C12-003, WS-C12-004, WS-C13-001]
time_sensitive: false
---
# Chapter 12 Summary: Information Leaks
(Source: PDF p. 144; this covers only the "Summary" heading and below. The text above it is covered in WS-C12-003 and WS-C12-004.)

## What the section covers
The chapter's closing recap, which restates the reason for avoiding information leaks and the full list of countermeasures (PDF p. 144).

## Summary of the chapter
- Why: a web server should not reveal the software stack it runs, since hackers use that information to decide how to compromise the site (PDF p. 144).
- Configuration: disable telltale headers and use a generic session cookie name in the HTTP response (mitigations 1 and 3, WS-C12-002) (PDF p. 144).
- URLs: use clean URLs that contain no filename extensions (mitigation 2, WS-C12-002) (PDF p. 144).
- JavaScript: minify or obfuscate it so it is harder to tell which third-party libraries are in use (mitigation 5, WS-C12-003) (PDF p. 144).
- Errors: turn off verbose client-side error reporting on the production site (mitigation 4, WS-C12-003) (PDF p. 144).
- Client files: sanitize template files and HTML for comments that give out too much information (mitigation 6, WS-C12-003) (PDF p. 144).
- Patching: stay on top of security advisories so patches are deployed in a timely manner (WS-C12-004) (PDF p. 144).

## Relations
The book moves on in the next chapter to securing traffic to a website with encryption (PDF p. 144; see WS-C13-001).
