---
id: WS-C11-004
title: Directory Traversal
source_pages: "136-139"
chapter: 11
concepts: [directory-traversal, relative-filepath, path-separator, dot-dot-syntax, indirect-file-references, path-sanitization, file-hosting, path-encoding, passwd-file]
related: [WS-C11-003, WS-C11-005, WS-C06-005]
time_sensitive: true
---
# Directory Traversal
(Source: PDF pp. 136-139, tail PDF p. 140. This row begins at the "Directory Traversal" heading on PDF p. 136; the text above it is the end of WS-C11-003. The tail page content above the "Summary" heading belongs here.)

## What the section covers
How attackers use file-path parameters to escape the intended directory, with a worked example, and four mitigations.

## Meaning
- If any of your URLs carry parameters naming file paths, an attacker can use directory traversal to bypass access control: they change the parameter to reach sensitive files you never meant to expose, usually substituting a relative path with the ../ syntax to "climb out" of the hosting directory (PDF p. 136).

## Filepaths and relative filepaths
- A filepath locates a file by listing its enclosing directories joined by path separator characters. The Linux path /tmp/logs/web.log means the file web.log inside the logs directory inside the top-level tmp directory (PDF pp. 136-137).
- A relative filepath starts with a period, meaning the current directory; ./web.log is web.log in the current directory. What "current" means depends on the context of evaluation; at a command prompt it is the directory the user last moved to (PDF p. 137).
- Two dots mean the parent directory, and repeating them climbs further. The path ../../etc/passwd goes up two levels, finds a directory named etc and returns the passwd file inside it. The book compares this to finding an uncle by going back two generations in the family tree and then taking a male child (PDF p. 137).
- If server-side code lets an attacker supply relative paths where filenames belong, they can read files outside the web server's home directory and probe places that commonly hold password or configuration information, breaking access control (PDF p. 137).

## Anatomy of an attack
- Example: a site hosts restaurant menus as PDFs on its filesystem, and users download one by clicking a link that names a file. Figure 11-1 shows a page on an example site (foodle.com in the figure) listing restaurants, with a URL whose menu parameter is a normal PDF name, and the browser downloading that PDF (PDF p. 137).
- If the filename parameter is not interpreted safely, the attacker replaces the menu name with a relative path. In Figure 11-2 the parameter is ../../../../etc/passwd and the browser downloads a file called passwd. The passwd file lists the user accounts on the underlying Linux system, handing the attacker sensitive information to help attack the server (PDF p. 138).

## Mitigation 1: Trust your web server
- Learn how your web server turns URLs into file paths for static content such as scripts, images and stylesheets. For less usual static files like menus, reuse the server's built-in URL resolution rather than writing your own; its static hosting is generally battle-tested against directory traversal (PDF p. 138).

## Mitigation 2: Use a hosting service
- If you serve files that are not part of your codebase, for instance uploads from users or administrators, strongly consider a content delivery network, cloud storage or a content management system (PDF p. 138).
- These reduce file-upload risk (Chapter 6, see WS-C06-005) and also defuse traversal by letting you refer to files by secure URLs or opaque identifiers. Of these, CDNs usually offer less fine-grained permissions (for example, limiting a file to certain users) but are the easiest to integrate (PDF pp. 138-139).

## Mitigation 3: Use indirect file references
- When you write your own code to serve files from local disk, the safest approach is indirection: give each file an opaque ID that maps to a path and make every URL use the ID. You need a registry, for instance in a database, that pairs IDs with paths (PDF p. 139).

## Mitigation 4: Sanitize file references
- If you must keep direct file references, for example in an inherited legacy codebase you cannot refactor in time, ensure arbitrary paths cannot be passed in place of filenames (PDF p. 139).
- Most secure: reject any file reference containing path separator characters, including encoded ones. Windows and Unix-like systems use different separators, backslash and forward slash (PDF p. 139).
- Alternative: check the filename against a regular expression that filters out path-like syntax. Be careful, because attackers constantly find new and obscure encodings; prefer a third-party filename-sanitising library where possible (PDF p. 139).
- Listing 11-4 shows path-cleaning logic from the Sinatra gem for Ruby. It first replaces encoded dot, slash and backslash sequences with plain characters and converts backslashes to slashes. It then splits the path into parts, skips empty parts and single dots, and drops the previous part whenever it meets a double dot. Finally it rebuilds the path with a standard separator, ensuring it starts with a slash (PDF pp. 139-140).
- Such complexity is needed because traversal can be encoded many ways. Listing 11-5 lists eight encodings of the parent-directory syntax for different operating systems: forward and back slash forms (../ and ..\ and a mixed ..\/ form), URL-encoded forms of the dots and slash, a double-URL-encoded form, a form built from %c0%ae and %c0%af sequences, and two forms using %u escapes (PDF p. 140).

## Time-sensitive statements
References to the Sinatra gem and the Linux passwd file are specific to the book's examples (PDF pp. 138-140).

## Relations
Recapped in WS-C11-005; follows the access-control discussion in WS-C11-003.
