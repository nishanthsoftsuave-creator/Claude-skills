---
id: WS-C14-006
title: "Chapter 14 Summary: Third-Party Code"
source_pages: "171-172"
chapter: 14
concepts: [chapter-summary, dependency-inventory, version-pinning, subresource-integrity, secure-configuration, api-keys, webhooks, subdomain-takeover, malvertising, safeframe]
related: [WS-C14-002, WS-C14-003, WS-C14-004, WS-C14-005, WS-C15-001]
time_sensitive: false
---
# Chapter 14 Summary: Third-Party Code
(Source: PDF pp. 171-172; this covers only the "Summary" heading on PDF p. 171 and below. The ad-review text above it belongs to WS-C14-005.)

## What the section covers
The chapter's closing recap of the three areas (dependencies, configuration, third-party services), and a pointer to the next chapter (PDF pp. 171-172).

## Summary of the chapter
Dependencies (recaps WS-C14-002):
- Vulnerabilities in third-party code threaten your site. Use a dependency manager to track what you depend on, keep the dependency inventory under source control, and name explicit versions (PDF p. 171).
- Script your build and deployment so upgrades after an advisory are easy, and include operating system patches (PDF p. 171).
- Follow social media and news sites to learn of advisories, and use auditing tools to find vulnerable components in the dependency tree (PDF p. 171).
- Use the integrity attribute when importing JavaScript so the browser can validate the files (PDF p. 171).

Configuration (recaps WS-C14-003):
- Do not run with an insecure configuration; attackers find insecure components with simple Google searches (PDF p. 171).
- Disable default credentials and open directory listings in the web server (PDF p. 171).
- Keep sensitive configuration (database credentials, API keys) out of source control; store it in a dedicated configuration store and load it at startup (PDF p. 171).
- Secure test environments and administrative frontends, which are common attacker targets (PDF p. 171).

Third-party services (recaps WS-C14-004 and WS-C14-005):
- Do not pass sensitive API keys or access tokens to the client (PDF p. 172).
- Protect webhooks against spoofing (PDF p. 172).
- If you serve content from elsewhere under your domain, for instance on a CDN or cloud storage, make sure an attacker cannot put malware there and serve it under your security certificate (PDF p. 172).
- Understand the malware risk in ads on your site: use a reputable ad network, use all the SafeFrame-based security settings it allows, review the ads periodically, and report and blacklist suspicious ones (PDF p. 172).

## Relations
The next chapter covers vulnerabilities in XML parsing, which the book calls a ubiquitous part of the internet and a common hacker target (PDF p. 172; see WS-C15-001).
