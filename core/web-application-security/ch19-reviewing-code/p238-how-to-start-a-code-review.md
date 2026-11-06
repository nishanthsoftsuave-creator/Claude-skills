---
id: WAS-C19-002
title: How to Start a Code Review
source_pages: "238"
chapter: 19
concepts: [code-review-workflow, git-diff, local-review, branch-checkout, web-based-review, github, functionality-review]
related: [WAS-C19-001, WAS-C19-003]
time_sensitive: false
---
# How to Start a Code Review
(Source: PDF p. 238, with the closing lines and Figure 19-1 on PDF p. 239 above the next heading)

## What the section covers
The first practical steps of a security review, done much like a functionality review, using a local checkout and a diff against the main branch.

## Meaning
- A code security review should work very much like a code functionality review. Functionality reviews are standard in nearly every development organization, so the learning curve for security reviews is short (PDF p. 238).

## How it works
The first step is to bring the branch under review to a local development machine. Some organizations allow review in a web-based editor from GitHub or GitLab, but those tools are less comprehensive than what is available locally (PDF p. 238). A common local flow from the terminal is:
1. Check out the main branch.
2. Fetch and merge its latest state from the remote.
3. Check out the feature branch, named like `<username>/feature`.
4. Run a diff against the remote main branch.

The diff returns two things: the files that differ between main and the current branch, and the changes inside those files.

## Figure 19-1 (PDF p. 239)
A GitHub screenshot of a merged pull request titled "misc fixes", showing a configuration file where a profile image URL was replaced by a local path. Its caption notes that GitHub, GitLab, Bitbucket and similar services offer web-based collaboration tools that make reviews easier.

## Where the two kinds of review part
The diff is the starting point of any functionality review and any security review; the two differ from there on. This note is printed at the top of the next page, so it carries no cite here beyond the figure.

## When and how to apply
INTERPRETATION: prefer the local checkout for security reviews so that the reviewer can run searches and tools across the whole tree, not just the diff view.

## Relations
Opens the chapter's method after the timing discussion in WAS-C19-001. The next section says what a security review looks for beyond a functionality review (WAS-C19-003).
