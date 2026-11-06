---
id: WS-C06-003
title: Command Injection
source_pages: "84-86"
chapter: 6
concepts: [command-injection, os-command-calls, escape-control-characters, escapeshellarg, argument-arrays, least-privilege, chroot, network-restriction]
related: [WS-C06-002, WS-C06-005, WS-C06-006]
time_sensitive: false
---
# Command Injection
(Source: PDF pp. 84-86. The text at the top of PDF p. 84 above the "Command Injection" heading is the end of WS-C06-002.)

## What the section covers
How a web application that builds operating system command lines from request data can be tricked into running extra commands, using an nslookup example, and how to defend by escaping or by passing arguments as arrays, plus least-privilege hardening (PDF pp. 84-86).

## Meaning
Command injection exploits a site that makes insecure command line calls to the underlying operating system. If a request can influence the command string, attackers can craft HTTP requests that execute arbitrary operating system commands and seize control of the application (PDF p. 84).

## Which languages are exposed
- Building command strings is actually unusual in many languages. Java runs in a virtual machine and is meant to be portable across operating systems; it can reach the OS through the java.lang.Runtime class, but depending on OS-specific functions runs against its philosophy (PDF p. 84).
- Command line calls are more common in interpreted languages. PHP follows the Unix philosophy (programs do one thing and talk to each other through text streams), so PHP apps often call other programs from the command line. Python and Ruby are popular for scripting and make OS-level commands easy (PDF p. 84).

## How it works: anatomy of the attack
- The example is a simple site that uses nslookup to resolve domain names and IP addresses. Listing 6-11 is PHP code that takes a domain parameter from the GET request and inserts it directly into a system call that runs nslookup, then prints the output (PDF p. 84).
- Because the code does not escape the domain argument when it builds the command string, an attacker can craft a URL with an extra command appended. Figure 6-1 shows a fictional lookup site (a robot mascot asks what address to look up) whose address bar carries the domain parameter, with the lookup box holding google.com followed by the && operator and an echo of the text HAXXED in quotes, and a terminal-style result showing the normal nslookup output for google.com followed by the injected output. The browser URL-encodes the whitespace and non-alphanumeric characters. As printed, the encoded URL in the figure shows a percent-3B sequence (a semicolon) where the text describes &&; the book does not comment on this, so both are recorded as printed (PDF p. 85).
- The && syntax in Unix chains separate commands. Since the PHP code does not strip such control characters, two commands run: the expected nslookup for the domain, then the injected echo (PDF p. 85).
- The echo is harmless, but an attacker can inject any command. With a bit of effort they can explore the filesystem, read sensitive information and compromise the whole application. Command line access on a web server gives complete freedom to take over the system unless deliberate steps lessen the impact (PDF p. 85).

## Mitigation: escape control characters
- As with SQL injection, properly escape inputs from the HTTP request: replace sensitive control characters (like the ampersand in the example) with a safe alternative. How to do it depends on the operating system and language (PDF pp. 85-86).
- PHP (Listing 6-12): wrap the request parameter in the built-in escapeshellarg function before building the command, so extra commands cannot be injected through the domain parameter (PDF p. 86).

```
$domain = escapeshellarg($_GET['domain']);
```

- Python (Listing 6-13): call the subprocess module's call function with a list, for example the program name nslookup followed by the domain variable as separate elements, rather than one string. This stops an attacker tagging commands onto the end (PDF p. 86).
- Ruby (Listing 6-14): call system with the program name and its arguments as separate parameters rather than a single string, for the same reason (PDF p. 86).

## Mitigation: least privilege
- As with SQL injection, the principle of least privilege limits the impact of a successful attack. The web server process should have only the permissions it needs, for instance limits on which directories it can read and write (PDF p. 86).
- On Linux, the chroot command can confine the process so it cannot explore outside a designated root directory (PDF p. 86).
- Limit the server's network access too, using firewalls and network access control lists (PDF p. 86).
- Together these make exploitation much harder: even if the hacker can run commands, they can do little beyond reading files in the web server's running directory (PDF p. 86).

## When and how to apply
INTERPRETATION: Prefer the array or argument-list form of process-spawning APIs over any string that mixes fixed text with request data, and use shell escaping only where a string command is unavoidable.

## Relations
The same control-character idea underlies SQL injection (WS-C06-002). A malicious uploaded script can give the attacker the same access, per WS-C06-005. The recap is in WS-C06-006.
