---
title: "Team Player Development"
book: pci-dss-integrated-data-security-standard-guide
chapter: 11
source_pages: "356-361"
format: source-text
---
# Team Player Development
(Source: PDF pp. 356-361)

<!-- PDF p. 356 (book p. 335) -->

Much like the development required to build and maintain a professional rugby league team, an effective PCI DSS compliance program requires the right specialist for the right role and with each specialist having proportionate training to develop and maintain their skill/knowledge levels.

In a professional rugby league side, they will spend each, and every, week carrying out strength, weakness, opportunities, and threat (SWOT) analysis of the members of the team against the upcoming competitions. Even though these players might have been playing for over a decade, the coaching staff still seek any prospects to gain the upper hand against their opponents. However, in business, there is a tendency to regard <!-- PDF p. 357 (book p. 336) --> their Data Privacy and Security programs as being isolated responsibilities, with limited consideration for the potential impact on other supporting roles.

Imagine the chaos that might ensue if a rugby league team were to attempt the same approach:

- During the game, the attacking side are in possession and are on the fifth tackle. The half back receives the ball, in the center of the pitch, and decides to kick the ball into the opposition’s corner. The intention was for their center or winger to rush up on the kicked ball, to put pressure on the receiving opponent, or to regather the ball and go over to score a try. However, at the point that the half back kicks the ball, the center and winger are in front of them and are in an offside[^33] position and must give the receiving opponent 10 meters, unless, of course, the half back was to run ahead of their team players before kicking the ball. Even though one of the responsibilities of the half back might be to kick well-placed kicks, they need to be mindful of their support players to ensure that a team effort is applied.

*[Figure omitted]*

**Figure 11-7.** *Well-Placed Kick*

[^33]: www.rugby-league.com/the_rfl/rules/laws_of_the_game/offside

<!-- PDF p. 358 (book p. 337) -->

Now imagine your PCI DSS compliance program. Your IT team understand the criticality of their public-facing supporting IT systems. However, they fail to inform the vulnerability management specialist, and, thus, a medium-rated vulnerability on a critical public-facing system is deemed to be a lower priority for remediation and is left vulnerable for a period of 90 days. Prior to remediation, the opposition *(hackers)* pounce on the opportunity to pick up this mistake and successfully breach the defensive line *(compromise the network)* to score a try over your goal line *(steal data)*. Alternatively, they fail to include the IT asset owner of a public-facing critical asset that was identified as having a critical vulnerability. As a result, the critical update remains untreated and vulnerable to exploitation.

## Sounds Unrealistic?

I’m sure that Equifax[^34] thought the same, until their lack of a team approach became the cause of their security breach. This simple error resulted in the failure to patch its network after being alerted in March 2017 to a critical security vulnerability (CVE-2017- 5638[^35] – The Jakarta Multipart parser in Apache Struts 2 2.3.x before 2.3.32 and 2.5.x before 2.5.10.1[^36]) affecting its ACIS database. This database handled inquiries from consumers about their personal credit data, enabling the attacker to gain unauthorized access and to steal **148 million** customer records *(credit card numbers of approximately 209,000 consumers)* and resulted in a reported settlement figure of **$700 million**. Their security team had carried out their responsibility of communicating the rule that all critical vulnerabilities affecting critical systems must be updated within 48 hours *(kicked the ball)*. However, they had failed to identify whether the IT asset owner was aware that you were about to *kick the ball* and were left unaware that they were in an *offside position* (failed to notify). This allowed their opponents the opportunity of an *extra 10 meters to pick up and run with the ball* (exploit the vulnerability).

In the case of the Equifax breach, members of their coaching team (chief information officer (CIO) and the chief information security officer (CISO)) appear to have been deemed culpable for the lack of a team effort within their Data Privacy and Security <!-- PDF p. 359 (book p. 338) --> program. Following the cyber-attack (May through July of 2017) and the public announcement of the data breach (September 8, 2017), Equifax announced (September 15, 2017) that with immediate effect “personnel changes” were being made, with the CIO, CISO, and chief executive officer retiring.[^37]

[^34]: https://republicans-oversight.house.gov/wp-content/uploads/2018/12/Equifax-Report.pdf
[^35]: www.exploit-db.com/search?cve=2017-5638
[^36]: https://nvd.nist.gov/vuln/detail/CVE-2017-5638

Each member of the professional rugby league team needs to have a general understanding of the “rules of the game” and must possess a standard skill competency to have been selected for the team. However, each player may have more specialist knowledge, skills, or experiences that make them more suitable for a particular field position. In addition to the 13 players, the coach needs to select four suitable interchanges, who can be timely impact players and who can be as effective as the players they may need to replace. Consequently, some standout players may be those that may be called upon to be effective in multiple positions *(Utility Players)*, deputizing if the primary player is not available, for example:

- **Jason Flowers**[^38]

A former professional rugby league footballer who played in the 1990s and 2000s and has coached in the 2010s

- He played at representative level for Scotland and at club level for Redhill ARLFC (in Airedale, Castleford), the Castleford (Tigers), Halifax, and the Salford City Reds.
  - Primarily as a fullback, but also at wing, center, or second row
- **Ian Smales**[^39]

A former professional rugby league footballer who played in the 1980s and 1990s

- He played at representative level for Great Britain (non-Test matches), and Yorkshire, and at club level for Lock Lane ARLFC, Featherstone Rovers, Castleford Tigers, and Hunslet Hawks.
  - Played as a winger, center, stand-off, second-row, or loose forward

[^37]: www.bankinfosecurity.com/after-mega-breach-at-equifax-ceo-richard-smith-out-a-10335
[^38]: www.loverugbyleague.com/stats/players/Jason-Flowers-/
[^39]: www.rugbyleagueproject.org/players/ian-smales/summary.html

<!-- PDF p. 360 (book p. 339) -->

In order to make the teams more effective, it is vital that the club and coaching staff support the development of complementary “Team Tactics” that can be applied to effectively defend against the tactics, techniques, and protocols (TTPS) of their opposition *(Threat Intelligence*[^40]*)*. As a result, the coaching staff will be continually reviewing the games of their opponents and developing multiple “Playbooks.” These will then have defensive countermeasures developed and be extensively practiced during team practices.

*[Figure omitted]*

**Figure 11-8.** *Creating a “Playbook”*

[^40]: https://whatis.techtarget.com/definition/threat-intelligence-cyber-threat-intelligence

<!-- PDF p. 361 (book p. 340) -->

*[Figure omitted]*
