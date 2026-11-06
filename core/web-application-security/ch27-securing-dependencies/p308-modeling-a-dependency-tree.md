---
id: WAS-C27-002
title: Modeling a Dependency Tree
source_pages: "308"
chapter: 27
concepts: [dependency-tree, tree-modeling, shared-dependency, jquery-example, version-drift, redundant-imports]
related: [WAS-C27-001, WAS-C27-003, WAS-C27-004]
time_sensitive: false
---
# Modeling a Dependency Tree
(Source: PDF p. 308)

## What the section covers
Why an application should model its dependency tree, using a small example in which three branches of the tree rely on the same library, and why that modeling also matters to security engineers.

## How it works: the example
The book's example application has a tree with three paths (PDF p. 308):
- the primary application depends directly on jQuery;
- the primary application depends on a single-page-application framework, which depends on jQuery;
- the primary application depends on a UI component library, which also depends on jQuery.

Because the tree is modeled, the application can see that three parts of the chain use jQuery. It can then import the library once and share it, instead of importing three copies. The benefit the book names is avoiding redundant file and memory storage (PDF p. 308).

## Why it matters for security
- Modeling is just as important to security engineering. Without a model of the tree it is hard to evaluate each dependency of the first-party application (PDF p. 308).
- In an ideal world every component using jQuery would use the same version. In the real world this is rarely so: the first-party application can standardize on versions, but it is unlikely to standardize the rest of the chain with it (PDF p. 308).
- Reasons given: each item in the chain may depend on functionality or implementation details that vary from version to version, and organizations differ in their philosophy of when and how to upgrade dependencies (PDF p. 308).

## Relations
The version-level example continues in WAS-C27-003; automated tree evaluation is in WAS-C27-004; the lead-in is WAS-C27-001.
