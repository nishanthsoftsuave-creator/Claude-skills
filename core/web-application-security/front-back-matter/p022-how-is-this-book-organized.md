---
id: WAS-P-005
title: Preface - How Is This Book Organized
source_pages: "22-26"
chapter: preface
concepts: [book-structure, recon, offense, defense, black-box-testing, authorized-testing, security-trade-offs, login-error-messages, user-enumeration]
related: [WAS-P-004, WAS-P-006, WAS-T-001, WAS-C09-001, WAS-C17-001]
time_sensitive: false
---
# Preface - How Is This Book Organized
(Source: PDF pp. 22-26, with the closing paragraph on PDF p. 27)

## What the section covers
The three-part layout of the book (recon, offense, defense), the reasoning for each part, a warning about legal use, and a worked example of a security trade-off.

## Overall structure
- The book is deliberately unlike most technology books: it keeps a nearly 1:1 ratio of offensive chapters to defensive chapters (PDF p. 22).
- It starts with a history lesson on the technology, tools and exploits of the past, then moves to its main topic, exploitation and countermeasures for modern web applications (PDF p. 22).
- The main content is three parts. The author recommends a linear read for the most learning, but says the first half works as a hacking reference and the second half as a security engineering reference (PDF p. 22).

## Part I: Recon (PDF p. 23)
- Recon means gaining information about a web application without necessarily attacking it. It covers technologies and concepts that matter to would-be hackers and also to anyone locking down an existing application, because much of what recon exposes can be reduced with planning.
- The author has worked with top penetration testers and bug bounty hunters and concluded that expert-level recon is what separates great hackers from merely good ones.
- Analogies: a fast car (exploit-building skill) still loses if the driver does not know the efficient route; in an RPG, recon is the rogue who scouts ahead and returns with intel, lining up shots and deciding which battles pay best.
- Reason one for recon is intel. Reason two is prioritising exploits: against well-defended targets many attacks may be logged, so there may be only one chance to use a flaw before it is found and closed.
- Recon matters most to would-be penetration testers and bounty hunters, because that work is mostly black box: the tester knows nothing of the application's structure or code and must build understanding through analysis.

## Part II: Offense (PDF pp. 24-25)
- Focus moves from recon and data gathering to analysing code and network requests, then taking advantage of insecurely written or misconfigured web applications (PDF p. 24).
- Warning: many chapters describe real techniques used by black hat hackers. Test them only against an application you own or have explicit written permission to test, since misuse could bring fines or jail time depending on the country (PDF p. 24).
- Readers learn to build and deploy exploits that steal data or change an application's behaviour, building on Part I and attacking demo applications (PDF p. 24).
- Each chapter covers one exploit: how it works mechanically, how to search for places to apply it, then crafting and deploying a payload against the demo application and observing the result (PDF p. 24).
- Cross-Site Scripting is introduced as an example. It involves writing malicious code locally and abusing weak filtration so it runs on another user's machine, and it applies beyond web applications, for instance to mobile apps and Flash/ActionScript games (PDF p. 24).
- Demo applications are kept short, often a few paragraphs. For exploits with many defences the book progressively breaks routine defences and then more advanced ones, on the idea that a wall around a codebase can be climbed over or tunnelled under (PDF p. 25).
- Part II matters because a hacker's mindset is often vital for secure architecture (PDF p. 25).

## Part III: Defense (PDF pp. 25-26)
- It revisits each Part II exploit from the opposite viewpoint: how to prevent or reduce the chance of a break-in. It also teaches general protections such as secure-by-default engineering and secure coding practices that a team can enforce with tests or a linter, plus ways to catch hackers in the act and improve an organisation's attitude to software security (PDF p. 25).
- Most chapters mirror the hacking chapters: an overview of the technology, a basic defence that mitigates but may not stop persistent attackers, then improvements until most or all attempts are stopped (PDF p. 25).
- Part III also discusses trade-offs, because improving security generally costs something outside security. It may not be the reader's place to set acceptable risk, but they should know what is being traded (PDF pp. 25-26).
- Typical costs: application performance (more reading and sanitising of data), more code to maintain, test and engineer, logging and monitoring overhead, and reduced usability (PDF p. 26).

## Worked trade-off: login error messages (PDF p. 26)
- If a login form reports an invalid username, brute forcing becomes much easier: the attacker no longer needs a list of active usernames, because the application confirms accounts, and can then brute force passwords alone, which sharply reduces the search effort.
- When logins use email addresses, the form can also leak valid emails that could be sold for marketing or spam. Even with brute-force protections, carefully crafted guesses of common company email patterns can reveal the naming scheme and pinpoint executives or people with important access for phishing.
- Best practice is therefore a generic error message. That conflicts with usability, since specific messages are better for users: a security gain paid for with reduced usability.

## Importance of the defence part (PDF p. 27)
Part III is described as extremely important for security engineers who want to deepen skills and for software engineers moving toward security work. Understanding how security can be improved also helps any hacker, since routine defences are easily bypassed while complex ones demand deeper knowledge, which is why the author suggests reading start to finish. Each part is another perspective on the same puzzle.

## Relations
The recon part opens in WAS-T-001, the hacker's mindset chapter is WAS-C09-001, and Part III begins at WAS-C17-001. Vocabulary used here is defined in WAS-P-006.
