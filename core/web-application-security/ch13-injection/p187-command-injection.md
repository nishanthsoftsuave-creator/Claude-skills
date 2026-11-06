---
id: WAS-C13-003
title: Command Injection
source_pages: "187-189"
chapter: 13
concepts: [command-injection, host-os-compromise, unix-permissions, least-privilege, exec, sensitive-files, privilege-escalation]
related: [WAS-C13-002, WAS-C25-006, WAS-C25-007]
time_sensitive: true
---
# Command Injection
(Source: PDF pp. 187-189, tail page 190)

## What the section covers
Command injection as the elevated form of code injection: an API builds shell commands that include client input, so an attacker's commands run against the operating system. The section lists what a compromised Unix host exposes, the damage possible, the partial mitigation offered by Unix permissions, and a second video-upload example where an unsanitized file name is concatenated into a remove command.

## Meaning
- With command injection an API endpoint generates Bash commands that include a request from a client; a malicious user adds custom commands that change the endpoint's normal operation (PDF p. 187).
- The video-converter example in the previous section was meant to ease into this. Code injection makes an interpreter or CLI do something the developer did not intend. Command injection is the elevated form: the unintended actions run against the OS (PDF p. 187).
- Figure 13-3 (PDF p. 188) is a four-step flow: a user tampers with an HTTP request and adds custom Bash commands; the API executes Bash commands against the server including them; the Bash interpreter executes what the API provided from the user; the system is fully compromised.

## Why it matters
- Executing commands, typically Bash, on a Unix-based OS (Macintosh or Linux) is very serious. The book says over 95% of servers are Unix-based, and if commands run as a super user the attacker can do anything to the OS (PDF p. 188).
- A compromised OS gives access to integral files and permissions. The book lists: the account list in /etc/passwd; encrypted passwords in /etc/shadow; the SSH keys in the user's ~/.ssh folder for talking to other systems; and the web server configuration files for Apache (/etc/apache2/httpd.conf) and Nginx (/etc/nginx/nginx.conf). Command injection may even yield write access to them, not only read access (PDF p. 188).
- Attacks the book says this opens up (PDF p. 189): stealing data from the server; rewriting log files to hide tracks; adding a database user with write access for later use; deleting important files; wiping and killing the server; using integrations with other servers or APIs, for example a server's Sendgrid keys to send spam mail; changing a login form in the web application into a phishing form that sends unencrypted passwords to the attacker; and locking admins out to blackmail them.
- Command injection sits at the top of every vulnerability risk-rating scale, and will stay there despite mitigations on modern web servers (PDF p. 189).

## Alternatives and mitigations
- One mitigation is the robust Unix permissions system: detailed permissions can be set on files, directories, users and commands, so an API running as an unprivileged user could remove the impact of many of the threats above. The book observes that most applications at risk of command injection do not build such permission profiles for their code (PDF p. 189).

## How it works: the second example
- A Node endpoint for video upload requires authentication, writes the raw upload under a raw-videos folder using the request's name field, converts it with a library called safe_converter into a converted-videos folder, and afterwards removes the raw file by running a shell remove command built from the same name. It then responds with 200 (PDF pp. 189-190, tail page for the continuation).
- The book lists the steps: write the raw video, convert it, remove the raw file because it is no longer needed. This is a typical compression workflow, but the remove command uses user input without sanitizing it. The name is not parameterized; it is concatenated into the Bash command as a string, so further commands can follow the removal (PDF p. 190).
- The attack string is a plausible file name followed by the double-ampersand operator and a destructive command targeting the converted-videos folder. As with the final code-injection example, unsanitized input leads to extra commands on the host OS, hence the name command injection (PDF p. 190).

## Limitations and failure modes
INTERPRETATION: the permission mitigation limits damage but does not remove the flaw; an unprivileged account still lets the attacker act with that account's rights.

## Relations
Escalates from WAS-C13-002. Defenses discussed later: least authority (WAS-C25-006) and whitelisting commands (WAS-C25-007).

## Time-sensitive statements
The "over 95% of servers are Unix-based" figure is the author's estimate at the time of writing.
