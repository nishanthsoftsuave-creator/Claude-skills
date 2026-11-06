---
id: WS-C14-002
title: Securing Dependencies
source_pages: "160-163"
chapter: 14
concepts: [heartbleed, dependency-management, dependency-tree, version-pinning, os-patching, subresource-integrity, checksums, regression-testing, npm-audit, security-advisories, patch-prioritization]
related: [WS-C14-001, WS-C14-003, WS-C14-006, WS-C05-005, WS-C05-007, WS-C12-004]
time_sensitive: true
---
# Securing Dependencies
(Source: PDF pp. 160-163, tail PDF p. 164. The section begins at its heading part-way down PDF p. 160. The tail is the text at the top of PDF p. 164 above the "Securing Configuration" heading, which begins WS-C14-003; it holds the software tools and "Know When to Upgrade" subsections.)

## What the section covers
Why dependencies need active security management, illustrated by Heartbleed, and the three practices that follow: know what code you run, be able to deploy new versions quickly, and stay alert to security issues (PDF pp. 160-164).

## Case: Heartbleed
- In April 2014 the authors of OpenSSL, the open source C library that implements TLS for most Linux versions and other operating systems, disclosed the Heartbleed bug. By exploiting a buffer over-read, an attacker could read arbitrary chunks of memory from a server using the vulnerable library and steal encryption keys, usernames, passwords and other sensitive data (PDF p. 160).
- Apache and Nginx, the two most popular web servers, use OpenSSL. Researchers at the security firm AVG estimated that over half a million websites became exposed overnight, and the bug has been called the most dangerous of all time (PDF p. 160).
- A patched OpenSSL was released the same day as the disclosure, yet unpatched servers were still common months later. That was a dangerous time to run one: attackers had time to perfect exploitation, and the shrinking pool of vulnerable sites made each remaining one a likelier target (PDF p. 160).
- Lesson: all websites use third-party code, and all third-party libraries, even those by security experts like OpenSSL, can have security flaws. To stay ahead you must learn of issues as soon as they are public and patch promptly (PDF p. 160). There are three aspects: know exactly what dependencies you run, be able to update them quickly, and stay alert to issues (PDF p. 160).

## Practice 1: know what code you are running
Modern stacks are intricate and multilayered, so it is easy to add a library during development and forget it later. Several kinds of tooling help organize dependencies (PDF p. 160).

### Dependency management tools
- Most languages ship with a dependency manager in which the team lists third-party dependencies in a configuration file; the libraries are downloaded on demand during the build. This makes it easy to add dependencies and to rebuild the stack in a new environment such as a server deployment (PDF pp. 160-161).
- Pin explicit version numbers. Packages live in a remote repository, and as authors publish new versions they get new version numbers. By default most dependency managers fetch the latest version the first time you build in a new environment. That default is sensible early in development, but by release the configuration file should list explicit versions. Advisories name the vulnerable versions, so knowing the exact version in each environment tells you what needs patching (PDF p. 161).
- Your declared dependencies have their own dependencies, which the manager also fetches, forming a dependency tree. Consider the whole tree when assessing risk; the manager can print it, including dependencies of dependencies, from the command line (PDF p. 161).
- Listing 14-1 shows output of the "npm list" command in the Node Package Manager for a sample project. It illustrates how one top-level library (a Blueprint UI core package at version 3.10.0) pulls in several subdependencies, among them the popper.js library, with some entries marked "deduped" because they are shared (PDF p. 161).

### Operating system patches
- Also track packages installed at the operating system level. OS vendors such as Red Hat and Microsoft regularly issue security patches, so track the version of each OS library in each environment and have a plan to upgrade servers in a timely way (PDF p. 161).
- With physical servers in a data center, dedicated system administrators likely handle this. With virtualized cloud servers (for example Amazon EC2), update the OS version regularly as part of deployment (PDF pp. 161-162).
- Docker containers help track OS dependencies, because the Docker configuration file explicitly lists what software is installed when the container starts (PDF p. 162).

### Integrity checks
- You need to be sure the code you think you run is the code you actually run. Dependency managers and patching tools do this with checksums: digital fingerprints computed when the dependency is uploaded to the repository and recomputed and verified when it is downloaded (PDF p. 162).
- Provide the same guarantee for JavaScript and other resources sent to the browser. Modern browsers support subresource integrity checks on script and style tags. The build should generate a checksum for each client-side resource file and set it as the integrity attribute of the import tag (PDF p. 162).
- Listing 14-2 generates a checksum on Unix by piping the file into openssl to produce a SHA-384 digest and Base64-encoding it (PDF p. 162):

```
cat FILENAME.js | openssl dgst -sha384 -binary | openssl base64 -A
```

- The browser compares the script with the expected checksum and runs it only if they match. This makes it much harder for an attacker who gains access to your server to swap in malicious JavaScript, since they would also need to alter the code that generates the script tags (PDF p. 162).
- Listing 14-3 shows the tag form: a script element with its src pointing to an externally hosted framework file, an integrity attribute starting "sha384-" followed by the Base64 checksum, and crossorigin set to "anonymous" (PDF p. 162).

## Practice 2: be able to deploy new versions quickly
- Responding to security issues needs an orderly, scripted release process. Chapter 5 covered this: releases should be reliable, reproducible and revertible, and tied to code branches in source control (PDF p. 162).
- Keep the dependency manager's configuration file under source control to know which dependency versions went into each release (PDF pp. 162-163).
- Security patches for third-party components are often deployed alone, upgrading dependency versions with no change to your own code. Such a release still needs regression testing, meaning checking that the upgraded dependencies do not break existing site functionality (PDF p. 163).
- Regression testing becomes more of a formality when unit test coverage is good: the more of the codebase that unit tests execute, the less manual testing is needed. Time spent writing good unit tests makes patching faster and easier (PDF p. 163).

## Practice 3: stay alert to security issues
With managed dependencies and a reliable release process, the last piece is hearing about disclosures, and the internet offers many ways to do so (PDF p. 163).
- Social media and news sites: advisories spread quickly on Twitter, Reddit and Hacker News. Big vulnerabilities are discussed on subreddits such as r/programming and r/technology and usually reach the Hacker News front page. Following technology pundits and software authors on Twitter often surfaces security topics and general software news (PDF p. 163).
- Mailing lists and blogs: programming languages often have mailing lists and channels for major news; the Python Software Foundation, for instance, has a weekly newsletter and a Slack channel. Subscribe to whatever fits your stack. Many information-security blogs exist; the book recommends Brian Krebs and Bruce Schneier (PDF p. 163).
- Official advisories: heed alerts from your hosting provider and software vendors. For Heartbleed-scale issues, hosts engage customers and guide them through patching. Microsoft issues patches every Tuesday ("patch Tuesday"), so subscribe to its newsletter if you use Microsoft technology (PDF p. 163).
- Software tools (PDF p. 164): automated checkers compare your dependencies against known vulnerabilities. Node Package Manager includes the "npm audit" command, which checks your dependency versions against an open source vulnerability database. The Ruby equivalent is the bundler-audit gem. For Java and .NET, the Open Web Application Security Project (OWASP) publishes the dependency-check command line tool. Add these to the build so you are alerted on each build and can assess each vulnerability's risk. Source hosts help too: GitHub scans hosted code and raises security alerts for vulnerable dependencies (PDF p. 164).

## When and how to apply: know when to upgrade
Not every security issue deserves equal priority. Constant upgrading takes time, and many concerns in an advisory may already be mitigated by other factors in your system. Large organizations have formal processes for reviewing and prioritizing alerts and choosing an action. Folding minor security upgrades into the next scheduled release is acceptable, provided the team has assessed the risks (PDF p. 164).

## Time-sensitive statements
- Heartbleed disclosure in April 2014 and the AVG estimate of more than half a million affected sites.
- Named tools and services as of the book's writing: npm audit, bundler-audit, OWASP dependency-check, GitHub alerts, Twitter, Reddit, Hacker News, the Python Software Foundation newsletter and Slack, Microsoft patch Tuesday, Docker, Amazon EC2.
- Example package versions in Listing 14-1.

## Relations
Builds on release practices from Chapter 5 (WS-C05-005) and dependency management (WS-C05-007); echoes the advisory advice in WS-C12-004. Next: configuring dependencies securely (WS-C14-003). Recap in WS-C14-006.
