---
id: WAS-C27-007
title: Secure Package Management
source_pages: "310"
chapter: 27
concepts: [package-management, semantic-versioning, version-locking, npm-caret, shrinkwrap, git-sha, npm-mirror]
related: [WAS-C27-006, WAS-C27-008, WAS-C15-006, WAS-C15-007]
time_sensitive: true
---
# Secure Package Management
(Source: PDF p. 310; the section continues on the next page)

## What the section covers
How to reduce the risk of third-party packages installed through a package manager such as npm or Maven by auditing a specific version and then pinning it.

## Meaning
- Package management systems carry a certain amount of accepted risk, tied to each system and to the review that published applications get (PDF p. 310).
- Semantic versioning uses three numbers: a major release, a minor release and a patch. Package managers by default try to keep dependencies on the latest patch, so a library at 1.0.23 could move to 1.0.24 without anyone being told (PDF p. 310).

## How it works
- Audit a specific version of the dependency, then lock the semantic version to the audited number (PDF p. 310).
- npm puts a caret in front of a dependency's version by default. Removing the caret makes the dependency use exactly that version rather than the newest patch (1.0.24 instead of ^1.0.24) (PDF p. 310).

## Continuation on the next page
The section runs on to the next page, ahead of the chapter summary, so the points below carry no page cite. The book says pinning by itself does not help if a maintainer republishes new code under an existing version number, which depends entirely on the maintainer, and that it only pins the top-level dependency, not its descendants. For descendants it describes shrinkwrapping: running `npm shrinkwrap` creates a file named npm-shrinkwrap.json and from then on every dependency and sub-dependency in the tree is used at its exact version. That removes the risk of a dependency moving to a newer, vulnerable patch, though not the rare risk of a maintainer reusing a version number. To remove that, the book suggests editing the shrinkwrap file to reference Git SHAs, or running your own npm mirror holding the right versions.

## Time-sensitive statements
The npm behaviors (default caret, the shrinkwrap command and file name) describe npm as of the book's writing.

## Relations
Builds on the package manager overview in WAS-C15-006 (JavaScript) and WAS-C15-007 (Java); the chapter summary is WAS-C27-008.
