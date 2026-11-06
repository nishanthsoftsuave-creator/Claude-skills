---
id: WAS-C19-007
title: Secure-Coding Anti-Patterns - Trust-By-Default
source_pages: "245"
chapter: 19
concepts: [trust-by-default, least-privilege, permissions-model, process-isolation, os-users, blast-radius]
related: [WAS-C19-006, WAS-C19-008, WAS-C25-006]
time_sensitive: false
---
# Secure-Coding Anti-Patterns: Trust-By-Default
(Source: PDF p. 245)

## What the section covers
The anti-pattern of running every part of an application under one all-powerful account, and the permissions model that replaces it.

## Meaning
- In an application with several levels of functionality that all ask the host operating system for resources, it is crucial to build a proper permissions model for your own code (PDF p. 245).

## The anti-pattern
- Picture an application that writes server-side logs, writes files to disk and updates an SQL database.
- In many implementations one user account is created on the server with permissions for logging, database access and disk access, and the whole application runs under it.
- If a vulnerability allows code execution or changes how a script executes, all three valuable server-side resources can be compromised at once.

## The secure alternative
- A secure application grants separate permissions for logging, disk writes and database operations, independent of each other (PDF p. 245).
- Each module runs under its own user, whose permissions are set to what that function needs and nothing more.
- A critical failure in one module then does not spread to the others. A vulnerability in the SQL module should not give a hacker access to files or logs on the server.

## When and how to apply
INTERPRETATION: during review, find the account each process runs as and compare the permissions it holds with what its code actually needs; any excess is a finding.

## Relations
Follows boilerplate code (WAS-C19-006). It applies the principle of least authority, whose defensive treatment is in the injection chapter (WAS-C25-006). The last anti-pattern, on client and server coupling, is WAS-C19-008.
