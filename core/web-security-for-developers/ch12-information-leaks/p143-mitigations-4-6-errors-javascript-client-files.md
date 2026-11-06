---
id: WS-C12-003
title: "Mitigations 4-6: Errors, JavaScript and Client Files"
source_pages: "143"
chapter: 12
concepts: [client-side-error-reporting, stack-traces, generic-error-page, minification, obfuscation, uglifyjs, code-review, static-analysis, html-comments]
related: [WS-C12-002, WS-C12-004, WS-C12-005, WS-C04-004]
time_sensitive: true
---
# Mitigations 4-6: Errors, JavaScript and Client Files
(Source: PDF p. 143, tail PDF p. 144. Mitigation 6 sits at the top of PDF p. 144 and ends where the "Stay on Top of Security Advisories" heading starts; that later heading is covered in WS-C12-004.)

## What the section covers
Three more mitigations: switch off detailed error output in production, minify or obfuscate JavaScript, and scrub client-side files of sensitive comments and dead code (PDF pp. 143-144).

## Mitigation 4: disable client-side error reporting
- Many web servers can print stack traces and routing information into the HTML of an error page. That helps debugging in test environments (PDF p. 143).
- In production it hands attackers useful facts: stack traces and logs show which modules or libraries you use, so they can pick matching vulnerabilities. Errors from the data access layer can even disclose the structure of the database, a serious hazard (PDF p. 143).
- Therefore disable client-side error reporting in production. Keep the user-facing error page entirely generic: at most, say that an unexpected error happened and someone is investigating (PDF p. 143).
- Keep detailed error reports in production logs and error reporting tools that only administrators can reach (PDF p. 143).
- How to disable it depends on the server; check its documentation. Listing 12-2 shows the Rails setting, placed in the production environment config file (config/environments/production.rb), which turns full error reports off (PDF p. 143):

```
config.consider_all_requests_local = false
```

## Mitigation 5: minify or obfuscate JavaScript
- A minifier takes JavaScript and emits a functionally equivalent, heavily compressed file: it removes whitespace and other unneeded characters and swaps some statements for shorter equivalents (PDF p. 143).
- An obfuscator replaces function and method names with short meaningless tokens without changing behaviour, deliberately making code harder to read. The popular UglifyJS does both and is run from the command line as "uglifyjs" followed by input files, which makes it easy to add to a build process (PDF p. 143).
- Developers usually do this for performance, since smaller files load faster. A side benefit is that it becomes harder for an attacker to tell which JavaScript libraries you use (PDF p. 143).
- That matters because researchers and attackers periodically find vulnerabilities, including cross-site scripting flaws, in popular JavaScript libraries. Hiding your library choices buys breathing room when such exploits surface (PDF p. 143).

## Mitigation 6: sanitize client-side files
- Use code reviews and static analysis tools so sensitive data does not end up in comments and dead code is not shipped to the client (PDF p. 144).
- Developers easily leave overly informative comments in HTML, template or JavaScript files and forget that these files reach the browser (PDF p. 144).
- Minifying JavaScript may strip comments, but comments in template files and hand-written HTML must be spotted in code review and removed by hand (PDF p. 144).
- Hacking tools can crawl a site and extract left-behind comments; attackers often use this to find private IP addresses accidentally left in comments, and it is frequently one of their first steps (PDF p. 144).

## Limitations
INTERPRETATION: obfuscation and minification only obscure the library choice; they do not remove a vulnerable library. The book pairs the measures with staying on top of advisories (see WS-C12-004).

## Time-sensitive statements
- UglifyJS is named as the popular minifier/obfuscator at the time of writing.
- The Rails config file path and option name reflect the framework conventions the book used.

## Relations
Follows WS-C12-002; recapped in WS-C12-005. Dynamic server-side templates are discussed in WS-C04-004.
