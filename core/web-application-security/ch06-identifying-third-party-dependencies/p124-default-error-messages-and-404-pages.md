---
id: WAS-C06-006
title: Default Error Messages and 404 Pages
source_pages: "124-126"
chapter: 6
concepts: [default-error-pages, 404-page, ruby-on-rails, fingerprinting, git-history, version-range, cve-2016-6316, action-view-xss]
related: [WAS-C06-005, WAS-C15-009, WAS-C10-002]
time_sensitive: true
---
# Default Error Messages and 404 Pages
(Source: PDF pp. 124-126; the vulnerability description continues onto PDF p. 127)

## What the section covers
Using a framework's built-in error or not-found page to estimate its version by comparing the page with the framework's public change history. Ruby on Rails is the worked example.

## Meaning
- Some popular frameworks give no easy way to read their version. If they are open source, fingerprinting can work (PDF p. 124).
- Rails is one of the largest open source web frameworks. Its code is on GitHub, with every historical version in Git, so commit-by-commit changes can fingerprint the version in use. Figure 6-3 shows the repository page; its counters (roughly 74 thousand commits, about 3,870 contributors) are read from the figure and are dated (PDF p. 125).
- Web servers ship default error and 404 pages that stay until the owner replaces them. These pages can reveal the software and often the version or a range of versions (PDF p. 125).

## How it works
1. Rails' default 404 page is an HTML box reading that the page you were looking for does not exist (Figure 6-4). Its source is a file under the railties generators templates in the public Rails repository (PDF p. 126).
2. Clone the repository and search the history of that file. The book lists three changes: namespaced CSS selectors added on April 20, 2017; a non-breaking space (U+00A0) replaced with whitespace on November 21, 2013; and the HTML5 type attribute removed on April 5, 2012 (PDF p. 126).
3. On a target's 404 page, look for type="text/css". If present, the version shipped on April 5, 2012 or earlier. Then look for U+00A0; if present, November 21, 2013 or earlier. Then look for the namespaced selector .rails-default-error-page; if absent, April 20, 2017 or earlier (PDF p. 126).
4. In the book's example the type attribute was removed and U+00A0 replaced but the namespaced selectors are missing. Cross-referencing those dates with the release schedule on the Ruby Gems site gives a range the book prints as 3.2.16 to 4.2.8 (PDF p. 126).
5. Rails 3.2.x through 4.2.7 had a documented XSS flaw, CVE-2016-6316 (PDF p. 126). It let an attacker inject quote-padded HTML into a database field read by an Action View tag helper; script in that HTML then ran in any browser that used the app and triggered the helper (PDF p. 127).
6. This is one illustration. Any third-party dependency whose software and version can be found is open to the same route to easy exploitation, which later chapters cover (PDF p. 127).

## When and how to apply
INTERPRETATION: collect the dates implied by each marker on the page, combine them into an earliest and latest window, then check the release list and a CVE database for that window.

## Limitations
The result is a range, not an exact version, and the markers only work while the owner has not replaced the default page.

## Relations
Follows header detection (WAS-C06-005). The CVE lookup is described in WAS-C15-009 and XSS in WAS-C10-002.

## Time-sensitive statements
All Rails dates, version ranges, repository counts and the CVE number are dated facts.
