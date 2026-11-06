---
id: WS-C11-005
title: Chapter 11 Summary - Permissions
source_pages: "140"
chapter: 11
concepts: [permissions-summary, access-control-rules, directory-traversal, static-files, indirect-references, path-sanitization]
related: [WS-C11-003, WS-C11-004, WS-C12-001]
time_sensitive: false
---
# Chapter 11 Summary - Permissions
(Source: PDF p. 140; the text above the "Summary" heading is the end of WS-C11-004.)

## What the section covers
The book's recap of Chapter 11.

## Recap
- Users have different permission levels, so you must implement access control rules that are checked whenever someone tries to reach a resource. The rules need to be clearly documented, implemented comprehensively and tested aggressively. Development schedules should include enough slack for the team to assess the security effect of every new code change (WS-C11-003) (PDF p. 140).
- Static resources referenced by filename are open to directory traversal, a common way of defeating access controls (WS-C11-004) (PDF p. 140).
- Ways to defeat it: use the web server's existing method of serving static files, serve them from a secure third-party system, or refer to them through indirection. If filenames cannot be avoided, sanitise every HTTP parameter used to build file paths (PDF p. 140).
- Looking ahead: the next chapter examines how your site may advertise its technology stack, which tells attackers how to go after it (WS-C12-001) (PDF p. 140).

## Relations
Recaps WS-C11-003 and WS-C11-004.
