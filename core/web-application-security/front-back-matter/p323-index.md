---
id: WAS-B-001
title: Index (printed-page term lookup mapped to modules)
source_pages: "323-330"
chapter: back
concepts: [index, term-lookup, navigation, page-conversion, partial-map, glossary-entry-points]
related: [WAS-P-006, WAS-C28-004]
time_sensitive: false
---
# Index: printed-page term lookup, mapped to modules
(Source: PDF pp. 323-330)

## What this module is
The book ends with an alphabetical Index that fills eight pages (PDF pp. 323-330). This module explains how that Index is built and how to turn its entries into module ids of this book, and it gives a partial lookup table from the main topic entries to the modules that cover them. It is a navigation aid, not book content: the book's own text is in the chapter modules.

## How the Index is organized
- The entries run alphabetically, from a short "Symbols" group at the start, which holds entries such as 2FA and 404 pages, through the letters to Z; the last entry is zone transfer attacks (PDF pp. 323-330).
- Each entry lists page numbers separated by commas, with a hyphen marking a range (for example brute force attacks, 4 and 67-72) (PDF pp. 323-330).
- Many main entries have indented sub-entries. For instance "application architecture" has sub-entries for defensive, secure, key points and others, and "attacks" and "integration" are likewise broken into sub-entries (PDF pp. 323-330).
- A few entries are cross-references that send the reader to another entry, such as subdomains, finding (see domain structure, discovering) (PDF pp. 323-330).
- Entries that point to the front matter use lowercase roman numerals (for example admin / system administrators, xxviii). These name pages of the Foreword and Preface, such as the glossary tables (PDF pp. 323-330).
- Unlike an index of headings, this Index gives page numbers, and they are the book's printed page numbers, not PDF page numbers.

## How to use a page number
INTERPRETATION: for an arabic printed page number N, the PDF page is N + 32. For example the table of contents puts the Index at printed page 291, and it starts at PDF page 323. For a roman numeral, the printed numeral already equals the PDF page (the Foreword's page xv is PDF page 15). A PDF page can then be matched to a row in the coverage matrix by its start and end page; when a page is shared by two rows, either may hold the topic, so both are listed in the table.

## Term lookup table
INTERPRETATION: the matrix row ids in this table are the module writer's own mapping, made from the Index entry's printed pages and the matrix page ranges; the Index itself does not name modules. Row ids are written without their WAS- prefix. "C18-001 to C18-007" means every row from the first to the last in matrix order. Where an entry lists several pages, all rows that touch any of them appear. A topic may be named on a page for a passing mention only, so check the module before relying on it.

| Index entry | Printed pages | Rows (ids without the WAS- prefix) |
|---|---|---|
| 2FA (two-factor authentication) | 200 | C18-005 |
| 404 pages, default error messages | 92-95 | C06-004 to C06-007 |
| admin / system administrator (term) | xxviii | P-006 |
| advanced vulnerability scoring | 232 | C21-007, C21-008 |
| AngularJS | 89 | C06-002 |
| Apache | 48 | C03-014, C03-015 |
| API endpoint analysis: endpoint discovery | 77-80 | C05-001 |
| API endpoint analysis: authentication mechanism | 81-82 | C05-002, C05-003 |
| API endpoint analysis: endpoint shapes | 82-84 | C05-002 to C05-005 |
| application architecture: defensive | 188 | C17-001 to C17-003 |
| application architecture: identifying weak points | 99 | C07-001 |
| application architecture: secure versus insecure signals | 100-104 | C07-002, C07-003 |
| application architecture: layers of security | 104 | C07-002, C07-003 |
| application architecture: technology adoption and reinvention | 105 | C07-003, C07-004 |
| application architecture: secure | 193-203 | C18-001 to C18-008 |
| archiving utilities | 60-61 | C04-004, C04-005 |
| asynchrony | 41-44 | C03-009, C03-010 |
| authentication | 46, 81-82, 195-201, 250 | C03-011, C03-012, C05-002, C05-003, C18-001 to C18-007, C23-003, C23-004 |
| authorization | 46-48, 195-201 | C03-011 to C03-015, C18-001 to C18-007 |
| basic authentication | 47, 81 | C03-013, C03-014, C05-002 |
| BCrypt hashing function | 199 | C18-004 |
| blacklists | 211 | C19-005 |
| blackholing | 272 | C26-005 |
| brute force attacks | 4, 67-72 | C01-002, C04-007 to C04-009 |
| bug bounty programs | xxi, xxviii, 222 | P-004, P-006, C20-005, C20-006 |
| client-side data stores | 50 | C03-016, C03-017 |
| client-side frameworks: SPA frameworks | 88-90 | C06-002, C06-003 |
| client-side frameworks: JavaScript and CSS libraries | 90, 91 | C06-002 to C06-004 |
| code injection | 151-155 | C13-001 to C13-003 |
| command injection | 155-158 | C13-002 to C13-004 |
| CVE database | 87, 180, 277 | C06-001, C15-009, C27-003 to C27-005 |
| CVSS: purpose and base scoring | 226, 228-230 | C21-001 to C21-005 |
| CVSS: temporal scoring | 230 | C21-004, C21-005 |
| CVSS: environmental scoring | 231 | C21-005, C21-006 |
| Content Security Policy (CSP) | 17, 123, 242-245 | C01-009, C10-003, C10-004, C22-008 to C22-012 |
| credentials: secure and hashing | 197, 197-201 | C18-003 to C18-007 |
| Cross-Site Request Forgery (CSRF) | 131-139 | C11-001 to C11-004 |
| CSRF defense: header verification | 247-249 | C23-001, C23-002 |
| CSRF defense: tokens | 249, 250 | C23-001 to C23-004 |
| CSRF defense: stateless GET and middleware | 251, 252 | C23-005, C23-006 |
| CSS as an attack vector | 241 | C22-007, C22-008 |
| Cross-Site Scripting (XSS) | 117-130 | C10-001 to C10-007 |
| XSS: stored | 120-123 | C10-002 to C10-004 |
| XSS: reflected | 123-125 | C10-003, C10-004 |
| XSS: DOM-based | 126-128 | C10-005, C10-006 |
| XSS: mutation-based | 128-130 | C10-005 to C10-007 |
| XSS defense | 235-245 | C22-001 to C22-012 |
| database detection | 95 | C06-006, C06-007 |
| database-specific injection defenses | 263 | C25-004, C25-005 |
| server-side databases | 49 | C03-015, C03-016 |
| dependency trees | 275-277 | C27-001 to C27-005 |
| dictionary attacks | 72-74, 197 | C04-008, C04-009, C18-003, C18-004 |
| distributed denial of service (DDoS) | 167, 271 | C14-003, C14-004, C26-003, C26-004 |
| denial of service (DoS) attacks | 161-169 | C14-001 to C14-005 |
| DoS defense | 269-273 | C26-001 to C26-006 |
| DOM (purpose) | 44 | C03-009, C03-010 |
| DOMParser sink | 238 | C22-002 to C22-004 |
| dynamic analysis | 217 | C20-002, C20-003 |
| Enigma machine | 2-5 | C01-001 to C01-003 |
| entity encoding | 240 | C22-006, C22-007 |
| evil (malicious) regexes | 163, 270 | C14-002, C26-002, C26-003 |
| feature requirements, analyzing | 193, 207 | C18-001, C19-002, C19-003 |
| fingerprinting | 88, 92 | C06-002, C06-004 to C06-006 |
| gateway attacks | 257 | C24-002 to C24-004 |
| hashing algorithms | 106 | C07-004 |
| header detection | 92 | C06-004 to C06-006 |
| HTTPS, SSL and TLS | 195-196 | C18-001, C18-002 |
| hyperlinks, sanitizing | 239 | C22-005, C22-006 |
| SQL injection | 147-151 | C13-001, C13-002 |
| injection defense: prepared statements | 261 | C25-002, C25-003 |
| injection defense: principle of least authority | 264 | C25-005, C25-006 |
| injection defense: whitelisting commands | 265 | C25-006, C25-007 |
| integration: branches and forks | 174, 206 | C15-003, C15-004, C19-001, C19-002 |
| integration: self-hosted applications, source code | 174, 175 | C15-003 to C15-005 |
| Java and Maven | 178 | C15-006, C15-007 |
| JavaScript: context | 37 | C03-006, C03-007 |
| JavaScript: functions | 36 | C03-005, C03-006 |
| JavaScript: variables and scope | 34 | C03-004, C03-005 |
| JSON | 32-33, 256 | C03-003, C03-004, C24-002 |
| known plaintext attacks (KPAs) | 8 | C01-004, C01-005 |
| logical DoS vulnerabilities | 165-167, 270 | C14-003, C14-004, C26-002, C26-003 |
| man-in-the-middle attacks | 3, 195 | C01-002, C18-001, C18-002 |
| MongoDB | 95, 212 | C06-006, C06-007, C19-005, C19-006 |
| Morris Worm virus | 11 | C01-006, C01-007 |
| network analysis tools (browser) | 54-57 | C04-001 to C04-003 |
| npm package manager | 176 | C15-005, C15-006 |
| OAuth | 47, 81, 83 | C03-013, C03-014, C05-002 to C05-004 |
| package managers: other languages | 179 | C15-007, C15-008 |
| package managers: secure package management | 278 | C27-005 to C27-007 |
| penetration testing: third-party | 223 | C20-006, C20-007 |
| PII and financial data | 201 | C18-005 to C18-007 |
| phreakers and phreaking | 9, 281 | C01-005, C28-001 |
| principle of least privilege | 279 | C27-008 |
| Prototype Pollution attacks | 40 | C03-008 |
| prototypal inheritance | 38 | C03-007, C03-008 |
| public records | 57-65 | C04-003 to C04-007 |
| query parameter tampering | 131-135 | C11-001 |
| recon: introduction | 21-25 | C02-001 to C02-003 |
| regex DoS (ReDoS) | 162-164 | C14-002, C14-003 |
| regression testing | 191, 218 | C17-006 to C17-008, C20-003, C20-004 |
| responsible disclosure programs | 221 | C20-004, C20-005 |
| REST APIs | 28, 29-31 | C03-001, C03-002 |
| Ruby on Rails | 92-95, 212 | C06-004 to C06-007, C19-005, C19-006 |
| sanitizing user input | 237-241 | C22-001 to C22-008 |
| search engine caches | 58-60 | C04-004, C04-005 |
| security automation | 215-221 | C20-001 to C20-005 |
| separation of concerns | 278 | C27-005 to C27-007 |
| SPA frameworks (purpose) | 45 | C03-010, C03-011 |
| static analysis | 216 | C20-001, C20-002 |
| SVG sink | 238 | C22-002 to C22-004 |
| telephone phreaking | 8-10, 281 | C01-004 to C01-006, C28-001 |
| Twitter API | 62-65 | C04-006, C04-007 |
| trust-by-default anti-pattern | 213 | C19-006 to C19-008 |
| vulnerability management | 190, 225-233 | C17-004 to C17-006, C21-001 to C21-009 |
| vulnerability discovery | 114, 189, 215-224 | C09-001, C09-002, C17-003, C17-004, C20-001 to C20-008 |
| web servers | 48 | C03-014, C03-015 |
| whitelists | 212, 265 | C19-005, C19-006, C25-006, C25-007 |
| XML External Entity (XXE): direct | 141-145 | C12-001, C12-002 |
| XML External Entity (XXE): indirect | 145 | C12-001, C12-002 |
| XXE defense | 255-257 | C24-001 to C24-004 |
| zone transfer attacks | 65-67 | C04-006 to C04-008 |

## What this map leaves out
INTERPRETATION: this is a partial map. The Index has many more entries than the table, and these groups were not mapped:
- Glossary-style entries (occupations, acronyms and common terms such as white hat, black hat, red team, CSRF as an acronym) that point only to the roman-numeral pages of the Preface, apart from the two preface entries shown.
- Most cross-reference ("see") entries and most of the many sub-entries under broad headings such as attacks, hackers, integration, JavaScript, recon and software security.
- Entries naming tools, products and companies (for example Jest, Let's Encrypt, Google Authenticator, Elasticsearch, Nginx, IIS, jQuery, Node.js, Snyk-type scanners).
- History and people entries beyond the few shown, and entries that cite the Part III summary pages (281-289) as key points.
- Entries on the book's own structure, audience, learning goals and conventions.
- Any entry whose printed pages straddle several chapters, which would list too many rows to be useful.

## Limitations
- The Index lists pages, not headings, so a mapped row is a candidate and not a confirmed location of the term.
- Rows sharing a boundary page are both listed, which can overstate where a term appears.
- The table was generated from the matrix page ranges. A verifier recomputed the row ids of all 121 table entries from the matrix page ranges (printed page plus 32, roman numerals as printed) and found no wrong, missing or unknown ids, and re-read the printed pages of more than 30 entries against the Index pages (PDF pp. 323-330) without finding a wrong page number. Entries not shown in the table were not checked.

## Relations
The glossary tables that the roman-numeral entries point to are covered in WAS-P-006; the chapter-by-chapter recap that the Part III summary pages point to is WAS-C28-004.
