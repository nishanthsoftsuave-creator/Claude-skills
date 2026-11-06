---
id: WS-C10-003
title: How Attackers Hijack Sessions
source_pages: "125-127"
chapter: 10
concepts: [cookie-theft, httponly, secure-cookie, samesite, session-fixation, url-rewriting, weak-session-ids, random-number-seeds, xss, csrf, man-in-the-middle]
related: [WS-C10-002, WS-C10-004, WS-C07-001, WS-C08-002, WS-C08-005, WS-C13-003]
time_sensitive: true
---
# How Attackers Hijack Sessions
(Source: PDF pp. 125-127, tail PDF p. 128. The text at the top of PDF p. 125 above the "How Attackers Hijack Sessions" heading is the end of WS-C10-002. The tail page content above the "Summary" heading belongs here.)

## What the section covers
The three main hijacking methods (cookie theft, session fixation, weak session IDs) and the defence for each.

## Cookie theft
- Because cookies are so universal, attackers usually hijack a session by stealing the Cookie header value from an authenticated user. They use three techniques: injecting JavaScript while the user browses (cross-site scripting), sniffing traffic to capture headers (a man-in-the-middle attack), and causing unintended requests to the site while the user is logged in (cross-site request forgery) (PDF p. 125).
- Modern browsers offer simple defences against all three, switched on by adding keywords to the Set-Cookie header. Listing 10-3 combines them (PDF p. 125):

```
Set-Cookie: session_id=278283910977381992837; HttpOnly; Secure; SameSite=Lax
```

### Cross-site scripting
- Attackers use XSS (Chapter 7, see WS-C07-001) to run JavaScript that reads the victim's cookies and sends them to a server the attacker controls. They collect the values from that server's log and paste them into a browser session, or more likely into a script, to act as the victim (PDF p. 125).
- Defence: mark every cookie HttpOnly in Set-Cookie, so the browser hides it from JavaScript (Listing 10-4). There is seldom any reason for client-side script to read cookies, so there are few downsides (PDF pp. 125-126).

### Man-in-the-middle
- The attacker places themselves between browser and server and reads traffic in transit. Defence: serve the site over HTTPS (how-to in Chapter 13, see WS-C13-003) and mark cookies Secure (Listing 10-5), so the browser never sends them unencrypted over HTTP (PDF p. 126).
- Servers usually answer on both HTTP and HTTPS but redirect HTTP to HTTPS. The Secure flag stops the cookie being sent until after that redirect (PDF p. 126).

### Cross-site request forgery
- CSRF (Chapter 8, see WS-C08-002) needs no access to the cookie. The attacker only tricks the victim into following a link to your site; if the victim has an open session, the browser attaches the session cookie to the triggered request, which may perform a sensitive action such as liking something the attacker wants promoted (PDF p. 126).
- Defence: the SameSite attribute tells the browser to send session cookies only on requests that originate from your own site, and to strip them from others, such as a click on an emailed link (PDF p. 126).
- Two settings. Strict removes cookies from every request triggered by an external site (Listing 10-6) (PDF p. 126). Its drawback is that when a user shares your content on social media, anyone following the link must log in again to see it (PDF p. 127).
- Lax avoids that: cookies go only on incoming GET requests and are stripped from other methods (Listing 10-7). Sensitive actions such as writing content or sending messages normally use POST, PUT or DELETE, so an attacker cannot trigger them this way (PDF p. 127). See WS-C08-005 for the Chapter 8 treatment.

## Session fixation
- In the web's early days many browsers had no cookie support, so servers passed session IDs by URL rewriting, appending the ID to every URL visited. The Java Servlet Specification still describes adding the ID to the URL when cookies are unavailable (Listing 10-8 shows a catalogue URL carrying a jsessionid parameter with the value 1234) (PDF p. 127).
- All browsers support cookies now, so this is an anachronism, but legacy stacks may still accept URL-borne IDs, with two serious problems (PDF p. 127).
- Leakage: IDs in URLs end up in log files, so an attacker with log access can hijack sessions just by loading those URLs (PDF p. 127).
- Session fixation: a vulnerable server meeting an unknown session ID in a URL asks the user to authenticate and then creates a session under that supplied ID. The attacker fixes an ID in advance and sends victims enticing links containing it, typically via spam email or comment sections. Once the victim clicks and logs in, the dummy ID becomes a real session that the attacker knows and can use from their own browser with the same URL (PDF p. 127).
- Mitigation: disable URL rewriting for session tracking in server configuration, as it has no purpose and only invites fixation. Listing 10-9 shows Apache Tomcat 7.0 set to cookie-only tracking in its web.xml, which switches rewriting off (PDF p. 128).

## Taking advantage of weak session IDs
- An attacker holding a session ID can hijack the session, by cookie theft or fixation. A cruder route is guessing: IDs are generally numbers, and if they are small or predictable a script can enumerate candidates and test them against the server until one is valid (PDF p. 128).
- Real randomness is hard to produce in software. Most generators seed from environmental values such as the clock. If an attacker can learn or narrow the seeds to a manageable number of possibilities, they can enumerate likely IDs (PDF p. 128).
- Case study: early versions of Apache Tomcat were found vulnerable. Researchers found the ID generator was seeded by the system time and an in-memory object's hashcode, which let them narrow the inputs enough to guess session IDs reliably (PDF p. 128).
- Mitigation: check your server's documentation to confirm it produces large, unguessable IDs from a strong random-number generator. Researchers often find weak ID algorithms before attackers use them, so follow security advisories and patch the web stack when told to (PDF p. 128).

## Time-sensitive statements
Apache Tomcat 7.0 configuration, the early-Tomcat weak-ID finding, and the Java Servlet Specification reference (PDF pp. 127-128).

## Relations
Summarised in WS-C10-004. Mechanisms for XSS and CSRF are in WS-C07-001 and WS-C08-002.
