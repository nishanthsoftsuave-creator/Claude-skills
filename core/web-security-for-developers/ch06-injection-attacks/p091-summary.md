---
id: WS-C06-006
title: Chapter 6 Summary - Injection Attacks
source_pages: "91-92"
chapter: 6
concepts: [injection-summary, bind-parameters, command-injection, remote-code-execution, file-upload, least-privilege]
related: [WS-C06-002, WS-C06-003, WS-C06-004, WS-C06-005, WS-C07-001]
time_sensitive: false
---
# Chapter 6 Summary - Injection Attacks
(Source: PDF pp. 91-92. The text on PDF p. 91 above the "Summary" heading, Mitigations 3 and 4 for file uploads, belongs to WS-C06-005.)

## What the section covers
The chapter's closing recap of the four injection types and the shared defence of least privilege, with a pointer to the next chapter (PDF pp. 91-92).

## Recap by topic
- Chapter theme: an attacker crafts malicious HTTP requests to take control of backend systems (PDF p. 91).
- SQL injection (WS-C06-002): arises when web code does not securely construct SQL strings for the database. Mitigate with bind parameters when talking to the database driver (PDF p. 91).
- Command injection (WS-C06-003): arises from insecure calls to operating system functions. It can be defused similarly through correct use of binding, which the summary phrases loosely; the detailed section describes escaping and argument arrays (PDF p. 91).
- Remote code execution (WS-C06-004): lets hackers run exploits inside the web server process and typically stems from insecure serialization libraries. Keep up with security advisories for serialization libraries and for the web server software (PDF p. 91).
- File uploads (WS-C06-005): often enable command injection when uploaded files are written to disk with executable privileges. Write uploads to a third-party system or to disk with appropriate permissions, and validate file type as far as possible during upload (PDF p. 91).

## Shared defence
All injection types are mitigated by the principle of least privilege: processes and components run with only the permissions needed for their assigned tasks. This limits the harm if an attacker injects code. Examples: limiting file and network access for the web server process, and connecting to the database with a limited-permission account (PDF p. 92).

## Relations
The next chapter turns to attacks that use JavaScript vulnerabilities against the site, starting with WS-C07-001 (PDF p. 92).
