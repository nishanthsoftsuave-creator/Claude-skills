---
title: "Incident Management"
book: pci-dss-integrated-data-security-standard-guide
chapter: 13
source_pages: "424-427"
format: source-text
---
# Incident Management
(Source: PDF pp. 424-427)

<!-- PDF p. 424 (book p. 403) -->

- Prepare
- Detection and Analysis
- Contain, Eradicate, and Recover
- Post Incident

The concept of having in effective incident response is based on being able to identify and respond to abnormal activities occurring within your corporate environment. The ability to proactively respond is reliant on your ability to quickly identify unusual activity or activity that is in breach of the corporate policies/procedures.

It is important to be prepared and to think that it is inevitable that something will happen, whether that be a deliberate, malicious, or an accidental act, and that you need to be prepared for such an event. Remember that your Incident Management processes should not be restricted to data breaches and not also include minor events or incidents that impact your valued assets *(This could be the stumbling activities of an attacker’s clandestine activities)*, which would need to be subject to further investigation.

Incident Management should include multiple elements, for example, NIST SP800-61 R2:[^43]

- Establishing Incident Response Capabilities
- Incident Handling
  - Planning
  - Detection and Analysis (Investigation)

[^43]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf

<!-- PDF p. 425 (book p. 404) -->

- Containment, Eradication, and Recovery
- Post-Incident activity
- Coordination and Information Sharing

The best way to look at your incident response is to align it with the concept of a burglary.

*[Figure omitted]*

**Figure 13-3.** *Stages of an Incident*

In the event of a real incident occurring, the first thing that happens is your incident response team are highly likely to panic. Therefore, it is essential that extensive, continual training and familiarization against various scenarios, specific to your organization, is established.

<!-- PDF p. 426 (book p. 405) -->

## Stages for Designing a Scenario

1. Select a critical process.

2. Review and identify likely threat actors that would attack the process.

3. Identify possible tactics[^44] of the threat actors.

4. Loosely map the tactics to the kill chain[^45]/cognitive attack loop[^46] process.

5. Review and apply techniques.[^47]

a. *Check techniques against Cyber Analytics Repository (CAR)*[^48] *to identify key*

*actions and events carried out by criminals.*

6. Review, validate, and apply techniques and procedures from

Threat Intelligence Reports.

7. Review, Evaluate, and Validate.

a. *Past Security Assessments* b. *Audit Findings* i. *Known vulnerabilities in systems* **NOT** *patched*

8. Validate if the scenario is viable.

a. *If not, return to step 2.*

9. Review and map against kill chain/cognitive attack loop process.

[^44]: https://attack.mitre.org/tactics/pre/
[^45]: www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
[^46]: www.carbonblack.com/2019/07/31/introducing-the-cognitive-attack-loop-and-the-3-phases-of-cybercriminal-behavior/
[^47]: https://attack.mitre.org/techniques/pre/
[^48]: https://car.mitre.org/

<!-- PDF p. 427 (book p. 406) -->

10. Map existing controls against the five Ds of resilience:

a. **D**eter b. **D**etect c. **D**elay d. **D**eny e. **D**efend

11. Review effectiveness of existing controls and confirm with Audit

Team.

12. If deemed to be effective, identify any missing controls

*(enhancement)*.

a. If ineffective, configure and optimize existing controls.

13. Describe the missing controls effectiveness in addressing the threats.

14. Confirm scenario and business case for additional controls.

15. Formally share scenario with Incident Response Team and

Stakeholders.
