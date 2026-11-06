---
id: WS-C14-003
title: Securing Configuration
source_pages: "164-165"
chapter: 14
concepts: [secure-configuration, default-credentials, directory-listing, secrets-management, environment-variables, configuration-store, test-environment-hardening, admin-interfaces, google-hacking-database]
related: [WS-C14-002, WS-C14-004, WS-C14-006, WS-C09-005]
time_sensitive: true
---
# Securing Configuration
(Source: PDF pp. 164-165, tail PDF p. 166. The section begins at its heading part-way down PDF p. 164; the text above it belongs to WS-C14-002. The tail is the text at the top of PDF p. 166 above the "Securing the Services That You Use" heading, which begins WS-C14-004.)

## What the section covers
Why third-party software must be configured securely, and the specific configuration practices: disable default credentials and open directory listings, keep sensitive configuration out of source control, harden test environments, and lock down administrative frontends (PDF pp. 164-166).

## Why it matters
- Software is only as secure as its configuration. Installing a new database and keeping its default account and password quickly leads to trouble (PDF p. 164).
- Hackers scan the internet for components running default settings, betting that many site owners never customized them (PDF p. 164).
- An insecure configuration is probably visible to the world. Offensive Security hosts the Google Hacking Database, a listing of insecure software discoverable by simple Google searches, because Google's crawler indexes the web thoroughly and offers powerful search refinement. Searching for the string "index of /etc/certs" lists millions of servers exposing their certificate directories, a major flaw (PDF p. 164).
- A secure configuration means strong credentials, securely stored configuration data, and limiting the damage if an attacker reaches one part of the environment (PDF p. 164).

## Practices
### Disable default credentials
Many packages ship with default logins so first-time users can get going. Disable them before deploying to test or production. A database, web server or CMS deployed with, for example, an admin account will be found quickly by bots scanning for vulnerable software (PDF p. 165).

### Disable open directory listings
- Web servers overshare: older Apache versions map URL paths to files and helpfully list a directory's files when the URL omits a filename. That invites attackers to explore the filesystem for sensitive data files and security keys (PDF p. 165).
- Disable directory listings in server configuration. Listing 14-4 shows an Apache directory block with the options line "Indexes FollowSymLinks"; removing the keyword Indexes stops directory listings being generated (PDF p. 165).

### Protect configuration information
- Configuration often holds database credentials and API keys. Many teams keep configuration files in source control for easier deployment, but an attacker who reaches source control will hunt for exactly this information first. Database credentials, API keys, private encryption keys, certificates and similar secrets must be kept outside source control (PDF p. 165).
- Approach one: put sensitive settings in operating-system environment variables and have the configuration code read them at startup. Those variables can themselves be set from configuration files stored locally on the server (PDF p. 165).
- Approach two: a dedicated configuration store. AWS offers the Systems Manager Parameter Store; Microsoft servers often keep credentials in Active Directory, which supports fine-grained permissions. A database table is another option, but consider how an attacker could escalate from database access, and note that the web server needs the database credentials before it can load the rest of the configuration (PDF p. 165).
- Approach three: store the configuration encrypted, with an algorithm such as AES-128, so an attacker must obtain both the configuration data and the decryption key. Keep the key in a different location from the configuration files or the benefit is negligible (PDF p. 166).

### Harden test environments
Preproduction environments usually run the same software as production but are often less secure. If a test environment holds sensitive data (for example, production data copied across for testing), it must be as secure as production. Production and nonproduction must not share credentials or API keys, which limits damage if a test server is compromised (PDF p. 166).

### Secure administrative frontends
- Some components ship administrative tools reachable over the internet, a favourite hacker target. Bots probe for unsecured WordPress sites by testing for a /wp-login.php page (PDF p. 166).
- If you will not use the admin frontend, disable it. If you will, remove default credentials and, where possible, restrict the IP range allowed to reach it. Check your stack's documentation or search Stack Overflow for how (PDF p. 166).
- The book then turns to code running on other people's servers (see WS-C14-004) (PDF p. 166).

## Time-sensitive statements
- Google Hacking Database (Offensive Security), AWS Systems Manager Parameter Store, Active Directory, Apache directive syntax, WordPress login path and Stack Overflow, as named by the book.

## Relations
Follows WS-C14-002 and precedes WS-C14-004; recapped in WS-C14-006. Credential handling in authentication is in Chapter 9 (WS-C09-005).
