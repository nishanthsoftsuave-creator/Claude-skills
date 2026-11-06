---
id: WS-C18-001
title: "Chapter 18: Summing Up - The 21 Commandments of Web Security"
source_pages: "197-200"
chapter: 18
concepts: [web-security-commandments, release-process, code-review, testing, injection, xss, csrf, password-hashing, cookies, least-privilege, encryption, dependencies, spf-dkim, clickjacking, traffic-surges]
related: [WS-C05-005, WS-C06-002, WS-C07-002, WS-C08-002, WS-C09-005, WS-C10-003, WS-C11-003, WS-C12-002, WS-C13-003, WS-C14-002, WS-C15-006, WS-C16-007, WS-C17-004]
time_sensitive: false
---
# Chapter 18: Summing Up - The 21 Commandments of Web Security
(Source: PDF pp. 197-200)

## What the section covers
The book's closing cheat sheet: 21 short commandments, one per major lesson, each stating what to do. The chapter has no subsections beyond the commandment headings (PDF p. 197). The book claims that following these steps makes the likelihood of being hacked "close to zero" (PDF p. 197).

## The commandments

Development process
1. Automate your release process. Build from a single command line call. Keep code in source control and choose a branching strategy. Keep configuration separate from code so test environments are easy to build. Validate in a testing environment before each release and automate deployment to every environment. Make releases reliable, reproducible and revertible. Always know what code version runs in each environment and be able to roll back simply (PDF p. 197). Background in WS-C05-005.
2. Do thorough code reviews. At least one team member other than the author must review every change before release. Give reviewers time to assess critically; reviewing is as important as writing (PDF p. 198).
3. Test your code "to the point of boredom". Write unit tests for critical sections and run them in the build. Run them on a continuous integration server on every change. Measure the share of code executed by tests and keep pushing it up. Write a test that reproduces a bug before fixing it (PDF p. 198).

Input, output and requests
4. Anticipate malicious input. Every part of an HTTP request can be manipulated. Build database and operating-system queries with parameterized statements to resist injection (PDF p. 198; see WS-C06-002).
5. Neutralize file uploads. Uploaded files must not be executable. Ideally put them on a CDN; if you need finer-grained permissions, a content management system (CMS); as a last resort use a separate disk partition and write files without executable permissions (PDF p. 198).
6. Escape content when writing HTML. Attackers smuggle JavaScript via the database or HTTP parameters. Escape dynamic content, replacing HTML control characters with safe entity encodings, on the client as well as the server. If possible disable inline JavaScript using the Content-Security-Policy response header (PDF p. 198; see WS-C07-002).
7. Be suspicious of HTTP requests from other sites. Make GET requests free of side effects (retrieval only). Make sure other request types, such as the POST that starts a login, come from your own site by adding anti-forgery cookies to HTML forms and to JavaScript-initiated requests. Add the SameSite attribute to Set-Cookie so cookies are stripped from requests started outside your domain (PDF p. 198; see WS-C08-002).

Identity and access
8. Hash and salt your passwords. Hash them with a strong one-way function such as bcrypt before storing, and add randomness to each hash with a salt (PDF p. 198; see WS-C09-005). (The book says "encrypt" here, but describes a one-way hash.)
9. Do not admit who your users are. Only the user should know whether they have an account. Keep error and information messages on login and password-reset pages generic whether or not the username exists (PDF p. 199).
10. Protect your cookies. Stolen cookies let attackers hijack identities. Add HttpOnly to Set-Cookie so JavaScript cannot read the cookie, and Secure so it is sent only over HTTPS (PDF p. 199; see WS-C10-003).
11. Protect sensitive resources even if you do not link to them. Check the user's permission before returning any sensitive resource, even one not listed in search pages or linked elsewhere (PDF p. 199; see WS-C11-003).
12. Avoid direct file references. Do not pass and evaluate file paths in HTTP requests. Use the web server's built-in URL resolution, or refer to files by opaque identifiers (PDF p. 199).

Information, transport and dependencies
13. Do not leak information. Reveal as little about your tech stack as you can: turn off the Server header, make the session parameter name in Set-Cookie generic, avoid telltale file suffixes in URLs, disable detailed client-side error reporting in production, and obfuscate the JavaScript libraries used during the build (as printed) (PDF p. 199; see WS-C12-002).
14. Use encryption correctly. Buy a certificate for your domain and install it with your private key. Divert all traffic to HTTPS, add Secure to Set-Cookie so cookies never travel over plain HTTP, and keep the web server updated to follow encryption standards (PDF p. 199; see WS-C13-003).
15. Secure your dependencies and services. Use a package manager during the build and pin each package to a specific version. Follow security advisories and update regularly. Keep configuration out of source control and stored securely. Use the SafeFrame standard for any ads you host (PDF p. 199; see WS-C14-002).

Third-party abuse of your server
16. Defuse your XML parser. Turn off processing of inline document type declarations (PDF p. 199; see WS-C15-006).
17. Send email securely. Whitelist the servers allowed to send mail from your domain with an SPF record, and let recipients verify the From address and detect tampering using DKIM (PDF pp. 199-200).
18. Check your redirects. If you redirect to a URL taken from the request, for example after login, verify it is local to your domain; otherwise open redirects will disguise malicious links in email (PDF p. 200).
19. Do not allow your site to be framed unless you must. Disable framing by sending the header Content-Security-Policy: frame-ancestors 'none' (PDF p. 200).

Resilience
20. Lock down your permissions. Apply least privilege so each process and component has only the permissions it needs. Consider what an attacker would do after compromising any part of the system and limit the damage. Do not run the web server as a root account. Limit the directories it can reach and prevent unnecessary network calls from it. Connect to the database with a restricted account (PDF p. 200).
21. Detect and prepare for traffic surges. Monitor traffic in real time. Build for scale with a CDN, client-side cookies, caching and asynchronous processing ("client-side cookies" as printed; the book's chapter 17 discusses browser caching via Cache-Control rather than cookies). Be able to add servers easily. If malicious traffic becomes a problem, deploy a firewall or intrusion prevention system, or consider DDoS protection (PDF p. 200; see WS-C17-004).

## Relations
This is the book's final recap, covering the process chapters (5), injection (6), XSS (7), CSRF (8), authentication (9), sessions (10), permissions (11), information leaks (12), encryption (13), third-party code (14), XML (15), accessory vulnerabilities (16; see WS-C16-007) and denial of service (17).
