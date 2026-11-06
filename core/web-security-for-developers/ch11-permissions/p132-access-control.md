---
id: WS-C11-003
title: Access Control
source_pages: "132-135"
chapter: 11
concepts: [access-control, authorization, permission-checking, acl, whitelist-blacklist, rbac, ownership-based-access, centralized-checks, access-control-testing, audit-trails, security-through-obscurity, embargoed-resources]
related: [WS-C11-002, WS-C11-004, WS-C09-006, WS-C10-004]
time_sensitive: true
---
# Access Control
(Source: PDF pp. 132-135, tail PDF p. 136. This row begins at the "Access Control" heading on PDF p. 132. The tail page content above the "Directory Traversal" heading, audit trails and common oversights, belongs here.)

## What the section covers
A three-part strategy for access control, then the stages of a good approach: designing an authorization model, implementing it, testing it, adding audit trails, and avoiding common oversights.

## Meaning: three aspects of an access control strategy
- Authentication: correctly identifying a user when they return to the site.
- Authorization: deciding what the user should and should not be allowed to do once identified.
- Permission checking: evaluating authorization at the moment the user tries to act (PDF p. 132).
- Chapters 9 and 10 handled authentication; secure login and session management tell you who is making requests. What each user may do is a more open-ended problem (PDF p. 132).
- A good strategy has three stages: design an authorization model, implement access control, test it. Afterwards add audit trails and check for common oversights (PDF p. 133).

## Designing an authorization model
Document how the chosen model applies to your users; without agreed rules you cannot define what a "correct" implementation is (PDF p. 133). Common models:
- Access control lists (ACLs): each object carries a list saying which actions each user or account may perform on it. The standard example is the Linux filesystem, with read, write and execute rights per file and directory. Most SQL databases are also ACL-based: the account you connect with decides which tables you can read or update and whether you can alter table structure (PDF p. 133).
- Whitelists and blacklists: a whitelist names the users allowed to reach a resource and bans everyone else; a blacklist names banned users and implies everyone else is allowed. Spam filters use both to decide which senders go straight to junk and which are never junked (PDF p. 133).
- Role-based access control (RBAC): probably the most comprehensive model. Users are given roles, or put into groups that hold roles, and policies say how each role may interact with subjects, meaning resources in the system. For example, adding someone to an Administrators group gives them the Administrator role, and a policy lets that role edit certain content. AWS identity and access management and Microsoft's Active Directory are role-based systems (PDF pp. 133-134). RBAC is powerful but prone to complexity: policies can contradict each other and need resolving, and users may sit in many overlapping groups, so it can be hard to see why a decision was made or which rule won (PDF p. 134).
- Ownership-based access control: common in social media, where each user fully controls what they create. Users are effectively administrators of their own posts, comments, photos and stories: they can create, delete and set visibility. They can tag other users in content such as photos, though the tagged users may have to approve the tag before it becomes public. Each content type has an implied privacy level; comments are generally public while direct messages are private (PDF p. 134).

## Implementing access control
- Centralise access decisions in the codebase so they are easier to check against design documents during code review. All decisions need not pass through a single code path, but there should be a standard way to evaluate them (PDF p. 134).
- Ways to implement: function or method decorators tagging functions with permission levels, URL checking (for example sensitive paths prefixed with /admin), inline assertions, or deferring to a dedicated permission component or in-house API (PDF p. 134).
- Listing 11-1 (Python, Django): a publish-post view is wrapped with a login-required decorator and a permission-required decorator for a publish permission, so the user must be logged in and hold that permission (PDF p. 134).
- Listing 11-2 (Ruby, pundit library): the publish action loads the post and calls an authorize function asking whether the current user may update that post, before publishing it and redirecting (PDF p. 135).
- Whatever the method, base decisions on properly vetted identity data. Use only the session cookie to work out who the user is and what they may do; anything else in the request can be tampered with to escalate privilege (PDF p. 135).

## Testing access control
- Test it critically, as an attacker would, so you are ready when the first real attack comes (PDF p. 135).
- Write unit tests asserting who can reach resources and, more importantly, who cannot. Add new access tests whenever you add features. Administrative interfaces deserve special attention since they are a common back door (PDF p. 135).
- Listing 11-3 is a Ruby test checking that an anonymous visitor who tries to reach the publish-post page is redirected to a login page that shows a login heading (PDF p. 135).
- If time and budget permit, hire an external team for penetration testing to look for missing or wrong access rules (PDF p. 135).

## Adding audit trails
- Since your code is identifying users and checking authorization, record audit trails: logs or database entries written whenever a user does something. Even a simple timestamped log line noting that a user logged in helps diagnose runtime problems and gives vital evidence after a hack (PDF pp. 135-136).

## Avoiding common oversights
- A frequent mistake is to skip access control on resources not meant to be discoverable, assuming unlinked pages are hidden from attackers. The book says this is false (PDF p. 136).
- Tools can quickly enumerate private URLs with opaque IDs (the book's example is an item page with a numeric id parameter), and guessable URL structures, such as a profile path ending in a username, are even easier. Depending on the attacker's inability to guess a URL is security through obscurity and counts as a risk (PDF p. 136).
- Embargoed resources are especially sensitive: financial reporting sites make reports available at a set time, since listed companies must release quarterly or half-yearly results to all investors simultaneously through agreed channels. Some sites upload reports early at predictable URLs (company name and month-year); cheating investors have checked those URLs ahead of time. Regulators have fined companies heavily for improper disclosure caused by broken access logic, so access rules must account for timing requirements (PDF p. 136).
- Every sensitive resource needs access control. File download features invite directory traversal, covered next in WS-C11-004 (PDF p. 136).

## Time-sensitive statements
Named technologies: Linux, AWS IAM, Active Directory, Django, pundit (PDF pp. 133-135).

## Relations
Builds on authentication (WS-C09-006) and session management (WS-C10-004); leads into WS-C11-004.
