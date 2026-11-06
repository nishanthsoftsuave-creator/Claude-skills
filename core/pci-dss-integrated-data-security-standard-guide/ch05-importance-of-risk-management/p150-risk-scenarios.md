---
title: "Risk Scenarios"
book: pci-dss-integrated-data-security-standard-guide
chapter: 5
source_pages: "150-161"
format: source-text
---
# Risk Scenarios
(Source: PDF pp. 150-161)

<!-- PDF p. 150 (book p. 127) -->

Well-prepared risk scenarios help create realistic and business-relevant descriptions of events that could have a real impact *(both positive and negative)* on your business and something that your business should be prepared for. By involving a variety of stakeholders, from across your business, you will help ensure that both the top-down *(analysis of the current and most relevant and probable business risks)* and the bottom-up *(employing generic risk scenarios to define a suite of business relevant and customizable scenarios (a starting point for discussion))* approaches. Each scenario should be linked to your real business risks and be prioritized against your most critical business processes/systems.

- **Documenting the “What If” question**

ISACAs have created a very helpful toolkit[^30] to support your development of risk scenarios that are specific to your organization, as well as providing you with over 50 example risk scenarios. Each scenario incorporates the five key areas that your key stakeholders would need to understand, so that they can make an informed decision as to whether this scenario is being effectively managed within their risk appetite/tolerance.

[^30]: www.isaca.org/Knowledge-Center/Research/Documents/Risk-Scenarios-Toolkit_tkt_Eng_0914.zip

<!-- PDF p. 151 (book p. 128) -->

*[Figure omitted]*

Embedding effective risk scenarios as part of your enterprise risk management practices has considerable benefits. However, their creation must ensure that this is based on suitable representation of realistic, unbiased, and reliable content to provide assurance to senior management that they are making risk decisions based upon good quality information. This will aid management’s ability to identify, analyze, and respond to risks that are pertinent to their business areas of responsibility. Consequently, the scenarios need to incorporate the following characteristics:

- **Relevance**

Provide meaningful information, appropriate to the factors that are relevant to your business.

- **Consistency**

Each scenario should be compelling in itself based upon the credibility and completeness of the content.

**Figure 5-6.** *Risk Scenarios Structure*

<!-- PDF p. 152 (book p. 129) -->

- **Plausibility**

Ensure that they are believable and realistic to your organization.

- **Likelihood**

To some extent, there must be a higher chance of the scenario occurring.

- **Currency**

Ensure that the scenarios reflect current threats to your business type.

The following data is an example of a completed Risk Scenario worksheet[^31] based upon an e-Commerce retailer.

Risk Scenario

Risk Scenario Title: Formjacking Attack

Risk Scenario Category 16: Logical attack on e-Commerce operations

Risk Scenario a vulnerability in a web page, in the earlier steps of the customer journey, allows an attacker to inject malicious code into an out-of-scope web page. however, this web page is part of the customer’s e-Commerce journey. Consequently, although the e-Commerce operation has been fully outsourced, so that all payment card details are entered through a pCI Dss compliant payment service provider (psp) interface, the vulnerability in out-of-scope business web pages presents an association to the psp interface. this enables the potential for an attacker to exploit the “out-of-scope” web pages to carry out a man-in-the-middle (mItm) attack, where the customer’s journey is diverted through their systems before getting to the psp. as a result, the customer remains unaware that the attacker is carrying out clandestine harvesting of their personal and payment card information being entered into the psp interface.

(*continued*)

[^31]: Adapted from ISACA, COBIT 5 for Risk, USA, 2013, www.isaca.org/cobit, pp. 243-244.

<!-- PDF p. 153 (book p. 130) -->

Risk Scenario

Risk Scenario Components

Threat Type the nature of the event

✓ Malicious ◻ Accidental ◻ Error ◻ Failure ◻ Natural ◻ External requirement

Actor Who or what triggers the threat that exploits a vulnerability?

◻ Internal ✓  External ◻ Human ◻ Non-human

Event something happens that was not supposed to happen, something does not happen that was supposed to happen, or a change in circumstances. events always have causes and usually have consequences. a consequence is the outcome of an event and has an impact on objectives.

✓ Disclosure ◻ Interruption ✓ Modification ✓ Theft ◻ Destruction ◻ Ineffective design ◻ Ineffective execution ◻ Rules and regulations ◻ Inappropriate use

<!-- PDF p. 154 (book p. 131) -->

Risk Scenario

Asset an asset is something of either tangible or intangible value that is worth protecting, including people, systems, infrastructure, finances, and reputation.

◻ Process ◻ People and Skills ◻ Organizational Structure ◻ Physical Infrastructure ✓ IT Infrastructure ✓ Information ✓ Applications

Resource a resource is anything that helps to achieve a goal.

✓ Process ✓ People and Skills ◻ Organizational Structure ◻ Physical Infrastructure ✓ IT Infrastructure ✓ Information ✓ Applications

Time Timing Duration Detection Time Lag

◻ non-Critical ◻ short ◻ slow ✓ Immediate

✓ Critical ✓ moderate ✓ moderate ◻ Delayed

◻ extended ◻ Instant

Risk Type

| the nature of this malicious act enables an attacker to exploit vulnerabilities in the corporation’s web site to steal customer sensitive information. |  |  |  |
|---|---|---|---|
| Risk Type | P/S | Risk Description |  |
| It Benefit/Value enablement |  | N/A | (continued) |

<!-- PDF p. 155 (book p. 132) -->

|  |  | Risk Scenario |  |  |  |
|---|---|---|---|---|---|
| It program and project Delivery |  | N/A |  |  |  |
| It operations and service Delivery | P<br>P<br>S | Security Problems<br>Breach of Data Privacy Regulations<br>Breach of PCI DSS compliance |  |  |  |
| Possible Risk Responses |  |  |  |  |  |
| Terminate | n/a |  |  |  |  |
| Tolerate | the Board makes the decision that no attacker would be interested in attacking the customer journeys. |  |  |  |  |
| Transfer | procure the additional services of a third party to monitor the “out-of-scope” web pages. |  |  |  |  |
| Treat | Include all “out-of-scope” corporate web sites into the pCI Dss scope, ensuring that all applicable pCI Dss controls are applied. |  |  |  |  |
| Risk Mitigation |  |  |  |  |  |
| Principles, Policies, and Frameworks Enabler |  |  |  |  |  |
| Reference | Contribution to Response |  | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
| Information security policy | outline information security arrangements for the protection of payment card data |  | HIGH | HIGH | YES |
| Data privacy policy | outline the data handling rules for safeguarding personal data |  | HIGH | HIGH | YES |
| secure<br>Development policies and procedures | Detail the software development consequences for the insecure software development impact on the information security policy |  | HIGH | HIGH | YES |

<!-- PDF p. 156 (book p. 133) -->

|  |  |  | Risk Scenario |  |  |  |
|---|---|---|---|---|---|---|
| secure software<br>Development principles |  | Information security requirements are embedded within the software development practices |  | HIGH | HIGH | YES |
| Process Enabler |  |  |  |  |  |  |
| Reference<br>NIST<br>CSF | PCI DSS | Title Description Governance | and<br>Management<br>Practices | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
| ID.am-2 | 2.4<br>12.3.7 | software platforms and applications within the organization are inventoried. | Identify all web page interfaces and connections. | MEDIUM | HIGH | YES |
| I.D.am-5 | 12.2 | resources<br>(e.g., hardware, devices, data, time, and software) are prioritized based on their classification, criticality, and business value. | Identify potential web site interfaces that could impact e-Commerce operations. | LOW | HIGH | YES |
| pr.Ds-6 | 11.5 | Integrity checking mechanisms are used to verify software, firmware, and information integrity. | monitor web page integrity. | MEDIUM | LOW | YES |

(*continued*)

<!-- PDF p. 157 (book p. 134) -->

|  |  |  | Risk Scenario |  |  |  |
|---|---|---|---|---|---|---|
| pr.Ds-7 | 6.4.1<br>6.4.2 | the development and testing environment(s) are separate from the production environment. | secure software development practices. | MEDIUM | MEDIUM | YES |
| De.Cm-7 | 10.1<br>10.6.1<br>11.5<br>12.10.5 | monitoring for unauthorized personnel, connections, devices, and software is performed. | monitor web page changes. | MEDIUM | MEDIUM | YES |
| pr.Ip-2 | 6.3<br>6.4<br>6.5<br>6.7 | a software<br>Development Life<br>Cycle to manage systems is implemented. | apply secure software development and testing principles. | MEDIUM | HIGH | YES |
| ID.ra-2 | 6.1 | Cyber threat intelligence and vulnerability information is received from information-sharing forums and sources. | Identify potential web attack interfaces. | MEDIUM | HIGH | YES |
| ID.ra-4 | 6.1 | potential business impacts and likelihoods are identified. | Identify risks with vulnerabilities on out-of-scope web interfaces. | MEDIUM | HIGH | YES |

<!-- PDF p. 158 (book p. 135) -->

Risk Scenario pr.Ip-12 6.1 6.2 a vulnerability management plan is developed and implemented.

apply timely identification and remediation of vulnerabilities.

LOW HIGH YES rs.an-5 6.1 6.2 processes are established to receive, analyze, and respond to vulnerabilities disclosed to the organization from internal and external sources (e.g., internal testing, security bulletins, or security researchers).

Vulnerabilities are identified and prioritized based on potential impact.

MEDIUM HIGH YES rs.mI-3 6.1 6.2 10.63 11.2 11.5.1 12.5.2 12.10 newly identified vulnerabilities are mitigated or documented as accepted risks.

Vulnerabilities are identified, risk assessed, and prioritized based on potential impact.

MEDIUM HIGH YES

(*continued*)

<!-- PDF p. 159 (book p. 136) -->

Risk Scenario

Organizational Structures Enabler

| Reference | Contribution to Response | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
|---|---|---|---|---|
| Information security manager | Implement security measures | HIGH | HIGH | YES |
| Data privacy officer | Implement data privacy measures | HIGH | HIGH | YES |
| service manager | In case attacks are successful, help manage the response | LOW | HIGH | YES |
| sCrUm manager | Design security measures | HIGH | HIGH | YES |

Culture, Ethics, and Behavior Enabler

| Reference | Contribution to Response | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
|---|---|---|---|---|
| pCI Dss secure development practices are part of BaU. | prevent web application attacks | HIGH | LOW | YES |
| Developers respect the importance of secure web development practices. | prevent web application attacks | HIGH | LOW | YES |
| stakeholders are aware of how to identify and respond to threats. | prevent web application attacks | MEDIUM | HIGH | YES |

<!-- PDF p. 160 (book p. 137) -->

Risk Scenario

Information Enabler

| Reference | Contribution to Response | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
|---|---|---|---|---|
| threat information reports | Intelligence reports on web-based attacks | HIGH | MEDIUM | YES |
| monitoring reports | Identify attack attempts, threat events, etc. | MEDIUM | HIGH | YES |

Services, Infrastructure, and Applications Enabler

| Reference | Contribution to Response | Effect on<br>Frequency | Effect on<br>Impact | Essential<br>Control |
|---|---|---|---|---|
| Web application testing and monitoring | Identify weaknesses | HIGH | LOW | YES |
| monitoring and alert services | timely notification of potential threats | LOW | HIGH | YES |

People, Skills, and Competencies Enabler

| Reference | Contribution to<br>Response | Effect on Frequency | Effect on<br>Impact | Essential<br>Control |
|---|---|---|---|---|
| pCI Dss security skills | prevent and reduce the impact of web-based attacks | HIGH | HIGH | YES |
| secure software<br>Development skills | maintain secure software development practices | HIGH | HIGH | YES |

(*continued*)

<!-- PDF p. 161 (book p. 138) -->

Risk Scenario

Key Risk Indicators (KRIs) Related to IT Goals

- Percentage of critical business processes, IT services, and IT-enabled business

programs covered by the risk assessment

- No. of significant IT-related incidents that were not identified in the risk assessment
- Percentage of corporate risk assessments included IT-related risk
- Frequency of update of the risk profile
- No. of security incidents causing financial loss, business disruption, or reputational

damage

- No. of IT services with outstanding security requirements
- Frequency of security assessments against latest standards and guidelines

Key Risk Indicators (KRIs) Related to Process Goals

- Percentage of critical operational event types covered by automated detection systems
- No. external facing business systems not covered by the business continuity plan/

incident response plan

- No. of out-of-scope web pages that could potentially impact the in-scope environment
- No. of vulnerabilities discovered on out-of-scope web pages
- Percentage of periodic testing of external digital public-facing web pages
- No. of incidents relating to unauthorized access to information

The use of scenario development can be seen being used by NASA in support of their Technical Risk Management process.

*[Figure omitted]*

**Figure 5-7.** *NASA Scenario Development Process*[^32]

[^32]: www.nasa.gov/seh/6-4-technical-risk-management
