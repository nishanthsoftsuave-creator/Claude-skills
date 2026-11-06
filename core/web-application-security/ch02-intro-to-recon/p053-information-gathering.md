---
id: WAS-C02-001
title: Information Gathering
source_pages: "53-54"
chapter: 2
concepts: [web-application-recon, information-gathering, authorised-testing, role-based-access-control, privilege-levels, hidden-functionality, unprotected-servers, attack-prioritisation]
related: [WAS-T-001, WAS-C02-002, WAS-C02-003]
time_sensitive: false
---
# Information Gathering
(Source: PDF pp. 53-54, with the end of the section on PDF p. 55)

## What the section covers
What web application reconnaissance is, who does it, why a user interface alone is not enough, and the technical reasons recon is worth doing, argued through a banking example.

## Meaning
- Web application reconnaissance is the exploratory data-gathering phase that usually comes before hacking a web application. Hackers, pen testers and bug bounty hunters normally do it, but security engineers can also use it to find weakly secured mechanisms and patch them before a malicious actor does (PDF p. 53).
- Recon skills have little value by themselves but become increasingly valuable when combined with offensive hacking knowledge and defensive security engineering experience (PDF p. 53).
- Recon is about building a deep understanding of an application before hacking it, and the author sets out to list more technical reasons why that matters (PDF p. 53).

## Warning
Many recon techniques in the following chapters help map applications but can get an IP address flagged, possibly resulting in bans or even legal action. Most recon should only be done against applications you own or have written permission to test (PDF p. 53).

## How recon is done
Sometimes just navigating an application and noting network requests gives a full picture of how it works. But not every application has a user interface that lets you explore visually. Public-facing, often business-to-consumer, applications such as social media do have one, yet you should assume you can see only a subset of the interface until you investigate further (PDF pp. 53-54).

## The banking example (PDF p. 54)
The author reasons logically about a fictional MegaBank:
- Opening a checking account in person also yields web login credentials. Account information is usually typed in by a bank teller, so at some point someone had access to a web or web-connected application able to create accounts in the bank's databases.
- A phone request for a savings account, handled remotely after the customer proves identity, is attached to the same login. So someone also uses an application that edits account information, possibly the same one or a different one.
- A customer cannot close the account online but can at a branch, so closing is not in the customer's web interface.
- Customers can usually only read balances online, and some banks allow paying bills or transferring funds, but none lets customers create, modify or delete their own accounts. Customers hold a limited subset of write access, while bank administrators and trusted staff can modify, create and delete accounts.
- A large bank cannot have developers write database queries by hand for every account change, so software must exist for it even though customers cannot reach it. Applications whose permissions are structured like this are called role-based access controlled applications, and few applications today have a single permission level for all users.

## Why it matters
- Everyday examples of the same controls are an operating system asking for admin credentials before a dangerous command, and social media sites where moderators sit above ordinary users but below admins (PDF p. 55).
- Walking through the user interface alone may never reveal API endpoints meant for admins or moderators. With recon mastery you can often find them and even build a map of an admin's or moderator's full permissions to compare with a standard user's, and sometimes find glitches that let unprivileged users use features meant for privileged ones (PDF p. 55).
- Recon also works on applications you have no access to, such as a school's internal network or a company file server: you can reverse engineer the structure of APIs and the payloads they accept without a user interface (PDF p. 55).
- Sometimes you will find servers or APIs with no protection at all. Forgetting one line of network or firewall configuration can expose an HTTP server to a public network instead of keeping it internal (PDF p. 55).
- As the map of technology and architecture grows, you can prioritise attacks, understanding which parts of the application are most heavily secured and which could use work (PDF p. 55).

## Relations
Mapping what you learn is the next section (WAS-C02-002), and the philosophy behind it is in WAS-T-001.
