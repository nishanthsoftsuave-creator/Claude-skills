---
id: WAS-C17-007
title: Regression Testing
source_pages: "223"
chapter: 17
concepts: [regression-testing, vulnerability-regression, reopened-bugs, test-framework, fix-validation, cost-benefit]
related: [WAS-C17-006, WAS-C17-008, WAS-C20-004]
time_sensitive: true
---
# Regression Testing
(Source: PDF p. 223)

## What the section covers
Why every deployed security fix should be followed by a regression test, how common regressions are, and how cheap the practice is compared with its value.

## Meaning
- After a fix goes out, the next step is a regression test that asserts the fix is valid and the vulnerability no longer exists (PDF p. 223).
- The author calls this a best practice that fewer companies use than should.

## Why it matters
- A large share of vulnerabilities are regressions: bugs that were closed and then reopened, or new variations of an earlier bug (PDF p. 223).
- A security engineer at a large software company, with more than 10,000 employees, told the author that roughly 25% of their security vulnerabilities came from previously closed bugs regressing to open.

## How it works and what it costs
- Building and adopting a vulnerability regression management framework is described as simple. Adding a test case to it should take a small fraction of the time the actual fix took (PDF p. 223).
- The tests cost little up front but can save large amounts of time and money in the long run.
- The author says later chapters cover how to build, deploy and maintain a regression framework.

## When and how to apply
INTERPRETATION: attach a regression test to every closed security ticket as a condition for closing it, and run the tests in the normal build.

## Time-sensitive statements
The 25% figure is a single anecdote from one large company at the time of writing, not a general statistic.

## Relations
Follows vulnerability management (WAS-C17-006). The discovery chapter shows how to build the framework (WAS-C20-004).
