---
id: WS-C06-004
title: Remote Code Execution
source_pages: "87"
chapter: 6
concepts: [remote-code-execution, serialization, deserialization, yaml, security-advisories, exploit-script, third-party-libraries]
related: [WS-C06-002, WS-C06-003, WS-C06-006, WS-C12-004, WS-C14-002]
time_sensitive: true
---
# Remote Code Execution
(Source: PDF p. 87, tail PDF p. 88. The tail page text above the "File Upload Vulnerabilities" heading belongs here; the rest of PDF p. 88 is WS-C06-005.)

## What the section covers
Injection of code into the web server's own language, how such attacks are found and built, the role of insecure deserialization, and the practical defence for developers: disable code execution in deserializers and track security advisories (PDF pp. 87-88).

## Meaning
- Earlier injection types target a database (SQL injection) or the operating system (command injection). Remote code execution is when an attacker injects malicious code that runs in the language of the web server itself (PDF p. 87).
- It is rarer than the injection attacks discussed earlier but just as dangerous (PDF p. 87).

## How it works: anatomy of the attack
- The attacker finds a vulnerability in a particular type of web server, then writes exploit scripts aimed at sites running that technology. The exploit places malicious code in the body of an HTTP request, encoded so the server reads and executes it while handling the request (PDF p. 87).
- Techniques vary widely. Security researchers study the codebases of common web servers looking for flaws that allow code to be injected (PDF p. 87).
- Example from early 2013: a vulnerability in Ruby on Rails let attackers inject their own Ruby code into the server process. Rails automatically parses requests according to their Content-Type header, so researchers found that an XML request with an embedded YAML object (a markup format commonly used in the Rails community for configuration data) could trick the parser into running arbitrary code (PDF p. 87).

## Mitigation: disable code execution during deserialization
- These vulnerabilities usually appear when server software uses insecure serialization. Serialization converts an in-memory data structure into a stream of binary data, usually to send it across a network; deserialization is the reverse step at the receiving end (PDF p. 87).
- Serialization libraries exist and are widely used in every major language. Some, such as the YAML parser used by Rails, let data structures execute code as they re-create themselves in memory. That is useful if you trust the data source and very dangerous if you do not, because it allows arbitrary code execution (PDF p. 87).
- If a server deserializes data coming from HTTP requests, it must defuse the serialization libraries by disabling their code-execution capabilities. Typically a configuration setting lets the server deserialize data without executing code (PDF p. 87).
- Developers who build sites on a web server, rather than writing the server itself, mostly protect against this by staying aware of security advisories. They are unlikely to write their own serialization libraries, so they should know where the codebase uses third-party ones, turn off active code-execution features in their own code, and watch for vulnerability announcements from the web server vendor (PDF p. 88).

## Time-sensitive statements
- The early 2013 Ruby on Rails YAML vulnerability (PDF p. 87).

## Relations
Compare the database and OS variants in WS-C06-002 and WS-C06-003; the chapter recap is WS-C06-006. Staying on top of advisories is developed further in WS-C12-004, and dependency handling in WS-C14-002.
