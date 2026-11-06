---
id: WS-C06-005
title: File Upload Vulnerabilities
source_pages: "88-90"
chapter: 6
concepts: [file-upload, web-shell, cdn-hosting, executable-permissions, content-type-spoofing, file-type-validation, antivirus, hardened-images]
related: [WS-C06-003, WS-C06-004, WS-C06-006, WS-C04-003]
time_sensitive: true
---
# File Upload Vulnerabilities
(Source: PDF pp. 88-90, tail PDF p. 91. On PDF p. 88 the text above the "File Upload Vulnerabilities" heading belongs to WS-C06-004. On PDF p. 91 the text above the "Summary" heading belongs here; the Summary is WS-C06-006.)

## What the section covers
How attackers abuse upload features to plant executable code, using a web shell example, and four mitigations: host files on a secure system, make uploads non-executable, validate file content, and run antivirus software (PDF pp. 88-91).

## Meaning
- Sites use upload functions for profile or post images, message attachments, paperwork, document sharing and more. Browsers make uploading easy through built-in file widgets and JavaScript APIs that support drag-and-drop with asynchronous sending (PDF p. 88).
- Browsers do not carefully check file contents. Servers typically treat uploads as large binary blobs, so an attacker can get a malicious payload through without detection (PDF p. 88).
- Client-side JavaScript that inspects a file before sending gives no real protection, because an attacker can write a script that posts file data directly to the server endpoint, skipping client-side checks (PDF p. 88).

## How it works: anatomy of a file upload attack
- The example abuses a profile image upload. The attacker writes a small web shell: a simple executable script that takes an argument from an HTTP request, runs it on the command line and outputs the result. Web shells are a common tool for compromising web servers. Listing 6-15 is a PHP web shell that checks for a cmd request parameter, passes it to the system call, and otherwise prints a short fixed message (PDF p. 88).
- The attacker saves it as hack.php and uploads it as the profile "image". Operating systems typically treat PHP files as executable, which is key to the attack. A .php file is plainly not a valid image, but the attacker can easily disable any JavaScript file-type check in the upload page (PDF p. 89).
- Afterwards the profile page shows a broken-image icon, but the attacker has achieved the real aim: the web shell now sits on your server waiting to be run (PDF p. 89).
- Because the shell is reachable at a public URL, it works as a backdoor. If the server's OS has a PHP runtime and the file was written to disk with executable privileges during upload, the attacker just requests the URL of the profile image to run it (PDF p. 89).
- The attacker then passes a cmd argument to run arbitrary OS commands, a command injection attack. Figure 6-2 shows a browser address on a content-delivery host pointing at the uploaded hack.php with the command to display a database client configuration file; the page shows that file's contents, including a user name, a password-like value, a database name, a cloud database host and a port. The point: a vulnerable upload function can expose database credentials (PDF p. 89).
- In effect the attacker gains through the upload feature the same OS access a command injection would give, and can explore the filesystem (PDF p. 89).

## Mitigations: overview
The most important mitigations ensure uploaded files cannot run as code. Following defense in depth, you should also analyse uploads and reject any that look corrupt or malicious (PDF p. 89).

### Mitigation 1: host files on a secure system
- Make sure the web server treats uploads as inert objects, not executables. One way is to host them on a content delivery network such as Cloudflare or Akamai (as described in Chapter 4), which moves the security burden to a third party that stores your files securely (PDF p. 90).
- CDNs have non-security benefits: very fast delivery to the browser, processing pipelines for uploads, and JavaScript upload widgets with extras such as image cropping that need only a few lines to add (PDF p. 90).
- If a CDN is not possible, cloud storage such as Amazon S3, or a dedicated content management system, gives many of the same benefits and defuses web shells at upload. If you host the CMS yourself you must configure it correctly (PDF p. 90).

### Mitigation 2: ensure uploaded files cannot be executed
- If neither a CDN nor a CMS is an option, do yourself what they do behind the scenes: write every file to disk without executable permissions; keep uploads in their own directory or partition so they are not mixed with code; harden servers so only minimally required software is installed (uninstall the PHP engine if unused); and rename files on upload so dangerous extensions are not written to disk (PDF p. 90).
- How to do this depends on hosting, OS and language. Listing 6-16 shows a Python server on Linux creating a file through the os module with an explicit permission mode that grants read and write but not execute (PDF p. 90).

```
os.open("/path/to/file", os.O_WRONLY | os.O_CREAT, 0o600)
```

- Removing unneeded software is always wise since it leaves a hacker fewer tools. The Center for Internet Security (CIS) offers pre-hardened operating system images, available as Docker images or Amazon Machine Images in the AWS Marketplace, as a starting point (PDF p. 90).

### Mitigation 3: validate the content of uploaded files
- For uploads of a known type, add type checks. Confirm the Content-Type header of the upload request matches the expected type, remembering an attacker can easily spoof that header (PDF p. 91).
- Files, especially images, can also be validated after upload on the server by reading their headers. Listing 6-17 uses Python's imghdr module to report the real format of a file (the example output is "gif"). The book warns that results vary: attackers have in the past got into systems with payloads valid in more than one file format (PDF p. 91).

### Mitigation 4: run antivirus software
On a server platform prone to viruses (the book singles out Microsoft Windows) run up-to-date antivirus software, because file upload functions are an open door to virus payloads (PDF p. 91).

## Limitations and failure modes
Header and content-type checks are weak on their own, since both can be spoofed or satisfied by polyglot files; the non-execution mitigations are described as the most important (PDF pp. 89, 91).

## Time-sensitive statements
- Products and services named: Cloudflare, Akamai, Amazon S3, CIS hardened images, AWS Marketplace, Docker, Python imghdr, Microsoft Windows (PDF pp. 90-91). The imghdr module is as printed in the book; SUPPLEMENTARY: it was deprecated and removed from recent Python releases, so check your runtime before relying on it.

## Relations
Command injection in WS-C06-003 is what a web shell enables. Insecure handling of code in requests is also in WS-C06-004. CDNs were introduced in WS-C04-003. The recap is WS-C06-006.
