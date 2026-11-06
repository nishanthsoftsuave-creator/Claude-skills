---
title: "Case Study 1: Telephone-Based Payments Risk Balance Case"
book: pci-dss-integrated-data-security-standard-guide
chapter: 6
source_pages: "187-200"
format: source-text
---
# Case Study 1: Telephone-Based Payments Risk Balance Case
(Source: PDF pp. 187-200)

<!-- PDF p. 187 (book p. 164) -->

Many organizations will attempt to manage and articulate their risks *(both PCI DSS and Business)* through the use of an in-house manual process, employing a mix of spreadsheets, documents, and presentations. Therefore, the first of my example case studies has been developed to show how this might be presented to show an informed choice has been made by senior management *(where the levels have exceeded risk appetites)*.

ABC Corporation are concerned with the risks from their Call/Contact Center operations and are seeking to risk manage this as part of their PCI DSS program.

They have chosen to document their risk management process using a manual process, consisting of three components:

- **Part A:** This is the opportunity for the business to articulate the identified and to present the potential risk treatment options that are available.
- **Part B:** Here the Information Security/Risk specialists have their inputs. This may result in the specialists disagreeing with the business departments’ preferred course of action (CoA).
- **Part C:** This is the executive sign off, where they have considered all the facts presented to them and chose the option that they are most comfortable with.

Table 6-3 provides an example of how this might look.

<!-- PDF p. 188 (book p. 165) -->

**Table 6-3.** *Business Risk Case Example*

Part A

Section 1: Completion by Submitting Business Department

| Submitted By | Signature<br>Joe Bloggs<br>Name<br>Joe Bloggs<br>Job Title<br>Call Center Manager<br>Company<br>ABC Corporation<br>Dates<br>April 01, 2020 |
|---|---|
| Detail | The business is concerned that the Call/Contact Center is susceptible to the threat from a trusted employer/ contractor stealing customer payment card information, or from customer payment card data being breached, as the result of a compromised network (as the Call Agents’ systems reside on a flat network). |
| Assets at Risk | Call Center systems and associated customer payment card data |
| The Risk | • Insider<br>• Technology |
| The Reason the<br>Risk Exists | Customers are required to speak their payment card data to the receiving Call Agents, who then manually enter the details into the payment application via their network-connected PCs. As a result, the payment card data is passed through the voice over Internet protocol (voIP) system, call recordings, and the Call Agents. each of which presents a potential threat vector for the business. |
| Impact Statement | A large-scale breach of the customers’ data would present a considerable reputational, financial, and regulatory impact.<br>(continued) |

<!-- PDF p. 189 (book p. 166) -->

Duration of Risk The Call Center is operational 24/7, 365 days a year.

Task To identify the best option that will reduce the risk to within tolerances, be the most manageable, and provide the best return on investment (RoI) for the business

Worst Case

Scenario A large-scale breach (e.g., 500,000) of customers’ personal data and payment card information

Policy

- Information Security Policy
- Data Privacy Policy

➤ Mitigation: Identify the available mitigating options. Discuss the RBC with the RM and obtain clear direction; if the RM has indicated that they wish to Treat a risk, provide suitable courses of action (CoA) that result in treating the risk.

CoA 1 Tolerate Require the Call Center shift managers to remain vigilant and to periodically train Call Agents of the policies and processes.

Advantages Minimal cost and resource impact to the business

Disadvantages Although this does partially address the insider risk, it does not address the technology risk associated with the potential risk from a compromised network, voIP risk, or payment card data storage (call recordings) risk.

**Table 6-3.** (*continued*)

Part A

(*continued*)

<!-- PDF p. 190 (book p. 167) -->

CoA 2 Treat Apply the full weight of the controls from the SAQ D (Circa 354 controls).

Advantages ensure that a full array of mitigation controls are applied from the PCI DSS controls catalogue.

Disadvantages This is extremely resources and cost intensive and difficult to manage and maintain.

CoA 3 Treat Apply to the criteria for the eligibility of an SAQ C (circa 155 controls):

- Payment application system and an Internet connection on the same device and/or same local area network (LAn).
- Segment/Isolate the payment application system/Internet device from other out-of-scope systems on the network.
- The physical location of the PoS environment is not connected to other premises or locations, and any LAn is for a single location only.

Avoid the electronic storage of cardholder, including call recordings.

Advantages Reduces the compliance burden and enhances the security through the silo of the Call Center systems and the removal of call recordings

Disadvantages extremely difficult to achieve, requiring significant network architecture and process changes

(*continued*)

<!-- PDF p. 191 (book p. 168) -->

CoA 4 Treat Apply to the criteria for the eligibility of the SAQ C/vT (circa 88 controls):

- only payment processing is via a virtual payment terminal, accessed by an Internet-connected web browser.
- The virtual payment terminal solution is provided and hosted by a PCI DSS-validated third-party service provider.
- Call Agents only access the PCI DSS-compliant virtual payment terminal solution via a computer that is isolated in a single location and is not connected to other locations or

systems within the environment.

- Prohibit the installation of software that enables cardholder data to be stored.
- Prohibit the attachment of hardware devices that are used to capture or store cardholder data.
- Prohibit the receipt or transmission of electronic cardholder data through any channels.
- Prohibit the storage of cardholder data.

Advantages Significantly reduces the compliance burden and enhances the security through the silo of the Call Center systems and removes the transmission and storage of electronic cardholder data

Disadvantages The business systems become extremely limited in their functionality.

**Table 6-3.** (*continued*)

Part A

(*continued*)

<!-- PDF p. 192 (book p. 169) -->

CoA 5: Transfer/

Terminate Remove the need for any systems or Call Agents to interact with any payment cardholder data, using third-party service provider’s dual-tone multi-frequency (DTMF) solution (e.g.,

GCI Com’s Cloud IVR [^30]). This aligns to the eligibility to complete an SAQ A (circa 22 controls

(only five of which are applicable)):

- only card-not-present (e-commerce or mail/telephone order) transactions.
- All processing of cardholder data is entirely outsourced to PCI DSS-validated third-party service providers.
- no electronic storage, processing, or transmission of any cardholder data on your systems or premises, but relying solely on a third party(s) to handle all these functions.

Confirmation that all third parties handling storage, processing, and/or transmission of cardholder data are PCI DSS compliant.

Advantages Significantly reduces the risk and the burden of the Call Center’s requirement to process customers’ cardholder data

Disadvantages The Call Center operations need to be adjusted to accommodate the new business processes.

Some personal data may still need to be processed; however, the high-risk number-based information (e.g., national Insurance, Date of Birth, etc.) can be replaced with DTMF.

CoA 6 Terminate Remove the requirement to interact with any customer cardholder data.

Advantages Completely removes the PCI DSS burden and associated risks

Disadvantages The interaction with personal data (non-cardholder data) may still be required, which may still need to be secured in line with local data privacy requirements.

The elimination of all cardholder data processing may not be possible.

(*continued*)

[^30]: www.gcicom.net/Our-Services/Unified-Communications/GCI-Contact-Centre/Cloud-IVR

<!-- PDF p. 193 (book p. 170) -->

Section 2: Recommendation and Business Unit’s Decision

➤ Risk Appetite: only complete Section 2 if the risk is within Business Department’s delegated Risk Appetite; RBCs relating to

InfoSec are passed directly to the Security Steering/Risk Committee. If the risk is beyond the Business Department’s delegated Risk

Appetite, complete and forward the RBC to the Security Steering/Risk Committee who will pass it to the relevant Risk owner.

➤ Risk Advisor Recommendation: Make a recommendation with supporting comment. Identify similar risks and provide comment on compliance with previous decision conditions.

Recommended CoA

(if applicable) CoA 5 It is recommended CoA 5 be accepted for the following reasons:

- Has minimal impact on the business operations while significantly reducing the associated risks
- Considerably minimizes the PCI DSS compliance burden on the business

Signature

Name Joe Bloggs

Job Title Call Center Manager

Company ABC Corporation

Date April 01, 2020

Within Risk

Appetite? Yes/No no

Within risk tolerances, the Business Manager is authorized to carry out the risk assessment decision.

If outside the formal risk appetite levels, this must be escalated to include Part B.

**Table 6-3.** (*continued*)

Part A

(*continued*)

<!-- PDF p. 194 (book p. 171) -->

Part B

Section 1: Information Security Input

| InfoSec<br>Recommendation | Agree with CoA 5<br>Signature<br>Name<br>Job Title<br>Company<br>Date | Jimmy Jones<br>CISo<br>ABC Corporation<br>April 12, 2020 |  |
|---|---|---|---|
| Risk ID of similar | 1. | 2. | 3. |
| risks/RBC (if |  |  |  |
| applicable) |  |  |  |
| Compliance with |  |  |  |
| previous Decision |  |  |  |
| Conditions (If |  |  |  |
| Extension Request) |  |  | (continued) |

<!-- PDF p. 195 (book p. 172) -->

Section 2: Security Steering/Risk Committee Decision

Agree with the recommended CoA, as all other options are too resource and cost intensive.

When balancing the resource and costs of outsourcing vs. the resource and costs of developing and maintaining an in-house operations, outsourcing presents the most significant ROI.

Signature

Name Tom Mann

Job Title Risk Chair

Company ABC Corporation

Date April 08, 2020

Decision Review Date: April 01, 2021

Section 3: Risk Assessment

5 × 5 Risk Heat Map

**Table 6-3.** (*continued*)

Part B

(*continued*)

<!-- PDF p. 196 (book p. 173) -->

*[Figure omitted]*

**Figure 6-5.** *Risk Heat Map*

Part B

(*continued*)

<!-- PDF p. 197 (book p. 174) -->

*[Figure omitted]*

**Figure 6-6.** *Legend*

**Table 6-3.** (*continued*)

Part B

(*continued*)

<!-- PDF p. 198 (book p. 175) -->

*[Text inside a figure could not be extracted]*

**Figure 6-7.** *Risk Matrix*

Part B

(*continued*)

<!-- PDF p. 199 (book p. 176) -->

*[Text inside a figure could not be extracted]*

Source(s)

- Mitre Att&ck
- QSA Recommendation
- 2013 Target breach investigation

Threat Assessment Attackers are increasingly seeking opportunities to move laterally across corporate networks from untrusted to trusted environments.

Personnel authorized access to the cardholder data environment, or to cardholder data, could compromise the network or steal the cardholder data.

[^31]

**Table 6-3.** (*continued*)

Part B

(*continued*)

[^31]: Impact post mitigation referees to the recommended CoA.

<!-- PDF p. 200 (book p. 177) -->

Within Risk Appetite? Yes/No no

Within risk tolerances, the InfoSec/Security Committee is authorized to carry out the risk assessment decision.

If outside the formal risk appetite levels, this must be escalated to include Part C.

Part C

Section 4: Risk Owner’s Statement

Risk Owner’s

Recommendation (if applicable) I conquer with the decision to pursue CoA 5.

Signature

Name Robert Hill

Job Title Risk Director

Company ABC Corporation

Date April 14, 2020

Part B
