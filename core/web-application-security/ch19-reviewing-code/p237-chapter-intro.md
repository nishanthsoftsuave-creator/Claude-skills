---
id: WAS-C19-001
title: Reviewing Code for Security - Chapter Introduction
source_pages: "237"
chapter: 19
concepts: [security-code-review, review-timing, merge-requests, pair-programming, architecture-before-review, move-fast-and-break-things, unbiased-reviewer]
related: [WAS-C17-003, WAS-C18-008, WAS-C19-002]
time_sensitive: false
---
# Reviewing Code for Security: Chapter Introduction
(Source: PDF p. 237, with the end of the introduction on PDF p. 238 above the first section heading)

## What the section covers
Where security code review sits in the development process, why it must come after architecture review, what it adds, and the best moment to run it.

## Order of review
- In an organization that takes security seriously, the code review stage must come after the architecture stage and never before (PDF p. 237).
- Some technology companies follow a "move fast and break things" mantra, which the author says is often abused as a way to ignore security processes. Even a fast-moving company must review application architecture before shipping code.
- Reviewing the whole feature architecture up front would be ideal but may not be feasible under uncertainty. At a minimum, the major and well-known features should be architected and reviewed, and new features should be architected and reviewed for security before development.
- The right time to review code for security gaps is once the architecture behind the commit has been reviewed, making code review the second step.

## What it adds
- A security reviewer is usually outside the immediate development team, so the developer gets an unbiased pair of eyes that may catch unknown bugs and architecture flaws (PDF p. 237).
- The security review phase matters for application functionality as well as security. Where only functional reviews exist, a security review should be added, which should sharply cut high-impact security bugs reaching production.

## When to run it
- Reviews make the most sense on merge requests, which the author notes are traditionally called pull requests, a less accurate name in most cases (PDF p. 237).
- The following page explains why: at merge time the full feature set exists and all connected systems have been integrated, so the whole scope can be reviewed in one sitting. It also says the review can be woven into development more finely, per commit or by pair programming. Either approach needs steady effort, since each sees the code at a point in time that does not cover the full scope. For mission-critical security features it may be wise: one mind on the feature and another on security could produce a feature that merge-time review alone could not. The timing is up to the organization and must fit its processes. These points are printed on the next page, so they carry no page cite here.

## When and how to apply
INTERPRETATION: default to review at merge, and add pairing or per-commit review only for the few features where a security failure would be most costly.

## Relations
The commit-review idea is first introduced in WAS-C17-003. The chapter on architecture (WAS-C18-008) argued for reviewing design first. The practical steps of a review begin in WAS-C19-002.
