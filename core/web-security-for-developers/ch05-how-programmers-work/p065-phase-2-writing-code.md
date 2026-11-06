---
id: WS-C05-003
title: Phase 2 - Writing Code
source_pages: "65"
chapter: 5
concepts: [source-control, version-control, git, github, distributed-version-control, branching, merge-conflict, code-review, four-eyes-principle, pull-request]
related: [WS-C05-002, WS-C05-004, WS-C05-008]
time_sensitive: true
---
# Phase 2 - Writing Code
(Source: PDF p. 65, tail PDF p. 66. The tail page text above the "Phase 3: Pre-Release Testing" heading belongs here. That heading and what follows it are WS-C05-004.)

## What the section covers
The second SDLC phase: keeping code in source control, the difference between distributed and centralised systems, branching and merging, and code review through pull requests (PDF pp. 65-66).

## Meaning: source control
- Any code that is not a one-off script should live in source control (also called version control). It stores a backup of the codebase, lets you browse earlier versions, tracks changes and lets you annotate them (PDF p. 65).
- Developers push changes to a shared repository, usually with command line tools or plug-ins, so teammates can review them before release. Releasing means deploying to the production website that real users see (PDF p. 65).
- Source control lets you inspect the version running in production, which is key to diagnosing and resolving vulnerabilities found after release. When a team fixes a security issue, it should examine the changes that introduced it and check whether they affected other parts of the site (PDF p. 65).
- It is the number one tool every team needs, even a team of one. Large firms generally run their own source control servers; small firms and open source developers usually use a hosted third-party service (PDF p. 65).

## Distributed versus centralised
- Many tools exist; the most popular is Git, created by Linus Torvalds, Linux's founder, to organise Linux kernel development. Git is distributed: every copy of the code is a full repository. A developer who pulls (downloads) the code for the first time receives the latest version plus the complete change history (PDF p. 65).
- Distributed tools record the developer's changes and send only those on a push. Older software used a central server, with developers downloading and uploading whole files (PDF p. 65).
- Git's popularity owes much to GitHub, which makes it easy to host an online repository and invite team members, view code in the browser and document it in Markdown. GitHub also has an issue tracker and tools to manage competing code changes (PDF p. 65).

## Branching and merging
- Source control lets you be exact about which changes go out in each update. Releases are usually managed with branches: a branch is a logical copy of the codebase, held on the server or in a developer's local repository. Developers change their own branch without touching the master codebase and merge back when the feature or fix is done (PDF p. 66).
- A note says large teams may use elaborate schemes, since branching is cheap and branches can come off other branches indefinitely; several developers may share one feature branch for complex updates (PDF p. 66).
- Before a release, several branches may be merged into master. When different edits touch the same files, the tool tries to merge them automatically. If it cannot, a merge conflict arises and the team must finish the merge manually, choosing line by line how to apply the competing changes. The book calls resolving merge conflicts the bane of a developer's life: it is extra work after you thought the issue was finished (PDF p. 66).

## Code review
- Merge time is a good moment for code review, where teammates examine the changes and give feedback. A strong way to catch security problems is the four eyes principle: two separate people must see every change before release, since a fresh reader can spot problems the author did not foresee (PDF p. 66).
- Git-based tools formalise review with pull requests: a developer's request to merge code into master, which lets tools such as GitHub require another developer's approval before the merge. Approval is often also made conditional on all tests passing in a continuous integration system, covered in WS-C05-004 (PDF p. 66).

## Time-sensitive statements
Names Git, GitHub and the Linux kernel origin; GitHub's features and Git's status as the most popular tool are as of the time the book was written.

## Relations
Follows design and analysis (WS-C05-002) and precedes testing (WS-C05-004). The summary bullet on source control is in WS-C05-008.
