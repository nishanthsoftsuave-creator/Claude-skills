---
id: WAS-C19-003
title: Archetypical Vulnerabilities Versus Custom Logic Bugs
source_pages: "239-240"
chapter: 19
concepts: [logic-vulnerabilities, archetypal-vulnerabilities, feature-context, roles-and-permissions, megachat, privilege-escalation, business-impact]
related: [WAS-C19-002, WAS-C19-004, WAS-C18-001]
time_sensitive: false
---
# Archetypical Vulnerabilities Versus Custom Logic Bugs
(Source: PDF pp. 239-240)

## What the section covers
What a security review checks that a functionality review does not, why logic-level bugs need knowledge of the feature's purpose, and a worked example, MegaChat, that shows how to gather that context.

## Meaning
- A functionality review checks that the code meets the feature specification and has no usability bugs (PDF p. 239).
- A security review checks for common vulnerability types such as XSS, CSRF and injection. More importantly it checks for logic-level vulnerabilities, which need deep context about the purpose of the code and cannot easily be found by automated tools or scanners.
- To find such bugs the reviewer needs context about the feature's goal: the users of the feature, its functionality and its business impact.
- Most vulnerabilities in the book are archetypes of well-known issues, but an application with a very specific use case can have vulnerabilities that a general book cannot list.

## Example: MegaChat
MegaBank plans a social media portal where registered users apply for membership (PDF pp. 239-240). Moderators approve membership after reviewing the user's earlier activity. Users have limited functionality and members have more. Moderators get member functionality automatically plus moderation tools. Users can post only text, while members can also upload games, videos and artwork. Membership is gated because hosting such media is costly, to cut low-quality content and to guard against bot accounts and freeloaders.

From this the reviewer derives (PDF p. 240):
- Users and roles: the users are MegaBank customers, split into three roles (user as the default, member, moderator), each with different permissions and functions.
- Feature functionality: all three can post text; members and moderators can post video, games and images; moderators can use moderation features, including upgrading users to members.
- Business impact: hosting video, games and images is expensive, and membership carries the risk of freeloading and of bots, both costing storage and bandwidth.

## Two kinds of vulnerability in the example
- An archetypal vulnerability would be an XSS in a post written by a user.
- A custom logic vulnerability would be an API endpoint coded improperly so that a plain user can send a payload containing `isMember: true` and post videos without a moderator having granted membership (PDF p. 240).

The code review is where archetypal issues are sought and, with deep application context, custom logic issues too.

## When and how to apply
INTERPRETATION: before reading code, write the roles, functions and cost drivers of the feature on one page, then check every endpoint against that page for actions a role should not be able to perform.

## Relations
Extends the review steps in WAS-C19-002. The following section gives an order in which to read the code (WAS-C19-004). Requirement analysis of the same kind appears in WAS-C18-001.
