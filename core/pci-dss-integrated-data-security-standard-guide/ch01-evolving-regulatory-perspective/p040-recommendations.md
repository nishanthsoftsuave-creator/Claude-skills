---
title: "Recommendations"
book: pci-dss-integrated-data-security-standard-guide
chapter: 1
source_pages: "40-50"
format: source-text
---
# Recommendations
(Source: PDF pp. 40-50)

<!-- PDF p. 40 (book p. 16) -->

It is abundantly clear that the world has moved on both in regard to the increasing use of technology and data and relation to data privacy regulations.

Consequently, it is highly recommended that you embed the data privacy principles and PCI DSS controls into your business operations, so that it becomes a seamless part of your organization. To achieve this, it is extremely important to ensure that your PCI DSS validation efforts are incorporated into your business-as-usual activities and not treated as a “standalone” compliance effort.

Data privacy and data security go “Hand in Glove” and should be treated as complementary to one another. Therefore, the components for data privacy, data security, and PCI DSS compliance should be incorporated into a single data privacy and security program (see Figure 1-8).

**Table 1-2.** *Mastercard Compliance Criteria – Service Providers*[^35]

Level 1 • all third-party processors (tpps)

- all staged Digital Wallet operators (sDWos)
- all Digital activity service providers (Dasps)
- all token service providers (tsps)
- all 3-D secure service providers (3-Dssps)
- all Data storage entities (Dses) and payment Facilitators (pFs) with greater than 300,000 total combined Mastercard and Maestro transactions annually
  - Annual Onsite Assessment conducted by an appropriate PCI SSC-approved QSA
  - Quarterly Network Scan conducted by an ASV

Level 2 • all Data storage entities (Dses) and payment

Facilitators (pFs) with 300,000 or less total combined Mastercard and Maestro transactions annually

- all terminal servicers (tss)
  - Annual Self-Assessment
  - Quarterly Network Scan conducted by an ASV

[^35]: www.mastercard.us/en-us/merchants/safety-security/security-recommendations/service-providers-need-to-know.html

<!-- PDF p. 41 (book p. 17) -->

*[Figure omitted]*

Embed data privacy and information security into your risk programs to ensure that senior management is fully apprised of the risks associated with your various data processes, be that payment card (PCI DSS) or personal data (e.g., GDPR), and that formal information security programs provide regular updates on the status, baselined against the most appropriate security controls frameworks.

The objectives of your data privacy program should be supported by defined roles (e.g., Risk Director, Information Security Manager, Data Privacy Officer, Privacy and Security Steering Committee, Privacy Manager, Risk Management Committee, Data

**Figure 1-8.** *Data Privacy and Security Cycles*

<!-- PDF p. 42 (book p. 18) -->

Controller, Data Processor, and various representative Business Unit Managers), which would form your cohesive process enablement to help deliver the following:

- Evaluation, direction, and monitoring
- Alignment, planning, and organization
- Secure development, procurement, and implementation
- Quality delivery, service, and support
- Monitoring, evaluation, and assessment

Additionally, the objective of this committee is to discuss any perceived risk and to provide guidance on the best practices to their representative teams. The processing, storage, or transmission of personal data has become an integral part of running a successful business. Consequently, this is an essential element of any successful privacy and information security program, as employee interaction with personal data and personal data processing IT systems is regarded as the greatest risk.

Establishing enterprise-wide security cultures, ethics, and behaviors is embedded throughout PCI DSS, seen at the conclusion controls of every requirement and in its entirety at requirement 12. It is important to remember that the foundations of effective security cultures, ethics, and behaviors must be endorsed and supported from the very top of the corporate hill and should not be seen as a once-a-year compliance “tick box” requirement.

Think of your data privacy program as you would regard a road safety program. Every road user needs to understand the “rules of the road” and to appreciate the risks associated with careless driving or breaking the rules. In order to be licensed to navigate the roads, each road user must achieve a minimum standard (pass their driving test) and then maintain these driving standards. Failure to do so results in re-education (e.g., warning, caution, speed awareness training, etc.) or disciplinary action (e.g., fine, driving ban, etc.).

A similar approach should be applied to the development of an effective data privacy program.

<!-- PDF p. 43 (book p. 19) -->

## Behaviors

At the organizational level, behaviors are determined by the values of your business (e.g., PCI DSS Charter) and at an individual level, where the behaviors are defined by personal values:

- **Data privacy is as natural as breathing (practiced in daily operations).**
- Data protection becomes an integral part of business. Rarely do employees wish to do badly by their employers or consumers, but do so out of complacency, neglect, or poor understanding.
  - At the corporate level, behavior indicates that data protection is accepted as a business imperative in business goals setting.
  - At the individual level, the employee recognizes the importance of applying data protection principles into their daily routines for the safeguarding of the consumers and the reputation of the business.
- **People respect the data protection policies and principles.**

Think of this like your “Rules of the Road,” where the employees do not need to be fully conversant with all the content of the data privacy legislations, only those controls that apply to their business functions. For example, if you take the example of the Highway Code,[^36] this is deemed to be essential reading for anyone intending to use the UK road (e.g., pedestrians, equestrians, cyclists, motorcycle riders, car drivers, bus drivers, truck drivers, etc.) and with the sole purpose of reducing the associated risks.

When you are entrusted driving a vehicle on the highways, there are a number of legal requirements that you need to comply with, as detailed in the Highway Code *(e.g., safe driving, maintaining an operational vehicle, having insurance, etc.)*. Any drivers or businesses failing to comply with the guidance from the Highway Code understand that there are consequences, as detailed in Table 1-3.

[^36]: www.gov.uk/guidance/the-highway-code/introduction

<!-- PDF p. 44 (book p. 20) -->

**Table 1-3.** *Driving Penalties*

| Offence | Imprisonment Fine |  | Disqualification | Penalty Points |
|---|---|---|---|---|
| Causing deaths or grievous bodily injury by dangerous driving | 14 years | unlimited | obligatory – two years minimum | 3 to 11 (if exceptionally not disqualified) |
| Dangerous driving | Five years | unlimited | obligatory | 3 to 11 (if exceptionally not disqualified) |
| Causing death or grievous bodily injury by careless driving under the influence of drink or drugs | 14 years | unlimited | obligatory – two years minimum | 3 to 11 (if exceptionally not disqualified) |
| aggravated vehicle taking causing death or grievous bodily injury | 14 years | unlimited | obligatory | 3 to 11 |
| Careless and inconsiderate driving | none | £5,000 | Discretionary | 3 to 9 |
| Driving while unfit through drink or drugs or with excess alcohol, or failing to provide a specimen for analysis | six months | £5,000 | obligatory | 3 to 11 (if exceptionally not disqualified) |
| Failing to stop after an accident (collision) or failing to report an accident<br>(collision) | six months | £5,000 | Discretionary | 5 to 10 |
| Driving when disqualified | two years | unlimited | Discretionary | 6 |
| Causing death or grievous bodily injury by careless or inconsiderate driving | Five years | unlimited | obligatory | 3 to 11 |
| Driving without insurance | six months | £5,000 | Discretionary | 6 to 8<br>(continued) |

<!-- PDF p. 45 (book p. 21) -->

| Offence | Imprisonment Fine |  | Disqualification | Penalty Points |
|---|---|---|---|---|
| Causing death or grievous bodily injury by driving unlicensed, uninsured, or while disqualified | two years | unlimited | obligatory | 3 to 11 |
| Failure to have proper control of vehicle or full view of the road and traffic ahead or using a handheld mobile phone while driving | none | £1,000 (£2,500 for pCv or goods vehicle) | Discretionary | 3 |
| speeding | none | £1,000 (£2,500 for motorway offences) | Discretionary | 3 to 6 or 3<br>(fixed penalty) |
| traffic light offences | none | £1,000 | Discretionary | 3 |
| no Mot certificate | none | £1,000 |  |  |
| seat belt offences | none | £500 |  | 3 |
| Dangerous cycling | none | £2,500 |  |  |
| Careless cycling | none | £1,000 |  |  |
| Failing to identify driver of a vehicle | none | £1,000 | Discretionary | 6 |

Similarities between the legal requirements for driving a motor vehicle can be correlated against the expectations for being a data controller or processor.

- **At the corporate level**
  - Data protection policies and principles are endorsed and supported by senior management and communicated to all. Individuals are encouraged to provide constructive feedback.
  - All systems supporting the personal data processing operations are well maintained.

**Table 1-3.** (*continued*)

<!-- PDF p. 46 (book p. 22) -->

- Individuals receive periodic refresher training, so as to keep their knowledge of the data Protection policies and principles fresh in their minds.
  - *This should be delivered through a variety of mediums (e.g., face to face (department security champions), emails, posters, newsletters, quizzes, etc.).*
  - *Consider the potential Return on Investment (ROI) of outsourcing the production and delivery through a third-party*

*service (e.g., KnowBe4*[^37]*).*

- Adherence to policies and procedures is policed.
- **At an individual level**
  - Employees/contractors have read, understood, and adhere to the data protection policies and principles *(actively encouraged to provide feedback on the content/applicability to their role)*.
  - Personnel adhere to their intent *(raising a formal approval requests for temporary deviations, when required)*. Individuals receive periodic refresher training, so as to keep their knowledge of the data Protection policies and principles fresh in their minds.
- **Individuals are given sufficient guidance and are encouraged to provide constructive feedback.**

Employees/contractors are provided sufficient instruction and are encouraged to challenge the data protection practices to ensure that they remain effective.

- A two-way communicative process is established.
- The culture supports the questioning of data protection practices, identifying potential issues/problems and providing comments, when requested.

[^37]: https://info.knowbe4.com/one-on-one-demo-partners?partnerid=0010c000022xCHUAA2

<!-- PDF p. 47 (book p. 23) -->

- **Everyone is deemed responsible for data protection.**
  - Discipline and sanctions are implemented for non-adherence of policy, with stakeholders confirming enforcement.
  - Individuals understand their data protection policies and principles that apply to their specific roles/duties.
- **Stakeholders identify and respond to threats to the organization.**
  - Threat intelligence is embedded into your company to enhance your ability to identify and respond to such breaches.
  - Personnel receive refresher training that includes relevant data breaches and how they should respond and report to such events.
- **Data Protection challenges are embedded into business projects and innovations.**
  - Research and development has an embedded security culture to ensure that data protection considerations are considered.
  - Individual data protection culture is included when stakeholders introduce new ideas.
- **Cross-functional collaboration supports the efficiency and effectiveness of the data protection programs.**
  - An integrated approach to data protection strategies is embedded into your organization.
  - Individual participation is encouraged for the identification of data protection risks, providing a synergy for the establishment of new data protection mitigations.
- **Executive management understands the business value of data protection.**
  - Data protection is recognized as a means to improve business value (e.g., revenue, expense, reputation, competitive advantage, etc.), maintain trust, and enhance brand value. Failure to be transparent, in the event of an incident/breach, can significantly undermine consumer confidence.
  - Individuals are seen to generate creative ideas that improve the value of any data protection efforts.

<!-- PDF p. 48 (book p. 24) -->

## Leadership

Never has the “Tone at the Top” been more important than in support of an effective data protection program, and this example needs to cascade down with the same message communicated through the departmental leads. Executive management are not expected to know the “ins and outs” of the data protection program; however, their actions should not undermine such a program.

The value of good leadership was a valuable lesson that I learned during my 22 years in the RAF Police and was often seen as being the deciding factor between success and failure. Organizations with weak or ineffectual leadership are doomed to fail, whereas organizations that have clear-sighted and courageous leadership are able to overcome virtually any problem.

the task of leadership is not to put greatness into humanity, but to elicit it, for the greatness is already there!

—John Buchan, lord tweedsmuir of elsfield

Some of the traits of a good leader include

- Creating a sense of belonging
- Developing a sense of duty and service
- Supporting good morale
- Courage
- Communication
- Leading by example
- Knowing your people
- Showing vision and decisiveness
- Creating an air of trust
- Providing command

<!-- PDF p. 49 (book p. 25) -->

All of these traits help to influence behavior across your business. Failure to embrace and support your data protection program can lead to incidents like these:

- I recall a visit to a client where their reception staff had made the visitor process redundant so that no visitor was being booked into the visitor log. Why had this happened? A board member had deemed this to be an inconvenience for them and had set a precedent for everyone else. As a consequence, they had no record of the comings and goings of strangers.
- On another occasion, I was carrying out a PCI DSS gap assessment for a UK football club. During the review of the logical access control practices, the IT Manager reassured me that the Active Directory Group policy had been configured to comply with the PCI DSS requirements (e.g., seven characters, strong complexity, etc.). However, when reviewing the Mail Order Telephone Ordering practices, carried out in a warehouse, it was revealed that the user was using a six-character password. When asked of the complexity used, I was informed that they were only using a six-character simple password. As a result, it would only take 500 milliseconds to crack the password[^38] and be able to gain unauthorized access to the corporate network.

“How could this have happened?”, I hear you shout. During a lunchtime period, when the IT help desk was being manned by a junior member of the IT team, a member of the Board demanded that the password complexity be changed, so as to make it easier for them.

[^38]: https://howsecureismypassword.net/

## Consent or Legitimate Use

Just requesting and collecting personal data from an individual are not acceptable practices. The consumer can reasonably expect that their data will explicitly be used in <!-- PDF p. 50 (book p. 26) --> a manner that they have approved or with which you are able to demonstrate a legal or legitimate business reason for doing so, for example:

- A consumer provides their personal and payment card data for the purchase of annual car insurance. It is reasonable for that consumer to believe that the payment card data shall not be retained once the payment has been processed. Therefore, without the explicit permission of the consumer, it is not acceptable to retain that personal data so that the insurance company can auto-enroll that consumer onto subsequent renewals.
  - Any deviation from this must be through transparent consent from the consumer.
