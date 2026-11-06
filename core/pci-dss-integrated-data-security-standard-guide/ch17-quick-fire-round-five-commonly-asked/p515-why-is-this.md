---
title: "Why is this?"
book: pci-dss-integrated-data-security-standard-guide
chapter: 17
source_pages: "515-532"
format: source-text
---
# Why is this?
(Source: PDF pp. 515-532)

<!-- PDF p. 515 (book p. 497) -->

*It is important to remember that every QSA company needs to ensure that all their QSAs meet the minimum qualification requirements,*[^15] *their QSAs adhere to the PCI SSC’s Code of Professional Responsibility,*[^16] *and all QSA work is subject to quality control.*

*However, despite these minimum requirements, it is inevitable that different QSAs will have differing strengths, qualities, and experiences. Consequently, it is increasingly likely that these factors will result in differing interpretations of the intent of specific controls and how these controls should be implemented.*

**2.2.7 Information Security Program** A Customer must maintain a comprehensive written information security program that includes technical, physical, administrative, and organizational safeguards designed to:

1. Ensure the security and confidentiality of Personal Data;
2. Protect against any anticipated threats or hazards to the security, confidentiality, and integrity of Personal Data;
3. Protect against any actual or suspected unauthorized processing, loss, or unauthorized acquisition of any Personal Data; and
4. Ensure the proper and secure disposal of Personal Data.

***A Customer’s information security program must regularly test or monitor the effectiveness of the safeguards stated in this Rule.***

**Figure 17-1.** *Mastercard Rules Extract*

[^15]: www.pcisecuritystandards.org/documents/QSA_Qualification_Requirements_v3_0.pdf
[^16]: www.pcisecuritystandards.org/documents/PCI_SSC_Code_of_Professional_Responsibility.pdf?agreement=true&time=1515177926566

<!-- PDF p. 516 (book p. 498) -->

*Your QSA should be able to explain the reason for their specific interpretation and understanding of these controls and how they believe that their approach will still ensure that your organization is still ensuring that the risks are being effectively mitigated.*

*Some of the most commonly misinterpreted controls are as follows:*

- **Marking wireless controls as N/A because no wireless environment is used**
  - **1.2.3:** *Configuring firewalls to prohibit unauthorized wireless traffic flows*
  - **11.1.:** *Quarterly testing to test for the presence of wireless access points*

Consider

How does marking these controls as being N/A reduce the risk associated with rogue wireless devices?

- AT&T Security Incident

“In return, the employees engaged in various illegal activities, including unlocking expensive iPhones meant exclusively for AT&T’s network, installing two pieces of malware on AT&T’s network at the Bothell call center, as well as installing rogue wireless access points at the same location.”

Source: www.itproportal.com/news/atandt-employees-took- bribes-to-put-malware-on-network/

<!-- PDF p. 517 (book p. 499) -->

- **Not including the testing of REST application programmable interfaces (APIs) for common vulnerabilities**
  - **6.5.1–6.5.6** *– Applicable to all applications (internal or external)*

Consider

How does this help mitigate the risks associated with your REST APIs having a commonly known vulnerability?

- Authentication
- Cross-Site Script
- Cross-Forge Request Forgery
- Injection

Source: https://dzone.com/articles/rest-api-security-vulnerabilities

Treat your procurement of QSA services the same as you might regard the hiring of a driving instructor. This is a service you are paying for, and if this service is failing to meet your expectations, do not be afraid to challenge the QSA and engage with their QSA to provide you with a satisfactory resolution.

Furthermore, do not be afraid to change your suppliers as this will help you avoid becoming complacent and if you periodically bring in “new pairs of eyes” can actually enhance your PCI DSS compliance strategy.

<!-- PDF p. 518 (book p. 500) -->

**Table 17-1.** *PCI SSC Index of FAQs*

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1003 | Where is the pCi security standards Council located? |
| #1004 | does the pCi security standards Council enforce compliance? |
| #1009 | in case of a suspected breach, should the pCi security standards Council be contacted directly? |
| #1014 | do Qsas and asvs need to send reports of compliance (roCs) or scanning results to the pCi security standards Council directly? |
| #1015 | What are the consequences to my business if i do not comply with the pCi dss? |
| #1016 | i want to add input into this process. how do i become a member of the Council? |
| #1017 | how can my organization find assistance in completing the self-assessment<br>Questionnaire? |
| #1018 | Will the pCi security standards Council list compliant service providers and/or merchants on its web site? |
| #1019 | if my business was deemed compliant but my system was still breached and payment account data compromised after the fact, what liability would my business incur? |
| #1020 | how does pa-dss support a merchant’s pCi dss compliance? |
| #1021 | how much will it cost for a vendor to have their products validated to pa-dss by a pa-Qsa? |
| #1022 | do small merchants with limited transaction volumes need to comply with pCi dss? |
| #1023 | What are the requirements that have to be satisfied to be in compliance with the pCi data security standard? |
| #1024 | is pCi dss a global standard? |
| #1032 | Can you provide clarification of pCi dss requirement 10.3.6? |
| #1033 | Can you provide clarification for logging/audit trail per pCi dss requirements 10.2.5 and<br>10.2.6? |
| #1034 | What are system-level objects, as identified in pCi dss requirement 10.2.7? |
| #1035 | What is the definition of “remote access”? |
| #1036 | how can i provide feedback (negative or positive) about my Qsa/asv? |

(*continued*)

<!-- PDF p. 519 (book p. 501) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1037 | do hosting providers have responsibility for liabilities/fines? |
| #1038 | does pCi dss apply to “hot cards,” expired, cancelled, or invalid card account numbers? |
| #1039 | does pCi dss apply to debit cards, debit payments, and debit systems? |
| #1040 | is it required that all of a company’s sites, even those located in other countries, must be included in the company’s pCi dss review? |
| #1041 | What is the scope of a pCi dss assessment for a network that is not segmented? |
| #1042 | should cardholder data be encrypted while in memory? |
| #1043 | is frame relay considered a private network and are there any encryption requirements? |
| #1044 | do isps that provide only internet connection need to comply with the pCi dss? |
| #1045 | is mpls considered a private or public network when transmitting cardholder data? |
| #1046 | Will the pCi security standards Council “approve” my organization’s implementation of compensating controls in my effort to comply with the pCi dss? |
| #1050 | i make atms, what do i need to do for pts? |
| #1051 | Can application whitelisting be used to meet pCi dss requirement 5? |
| #1052 | Can a payment application that implements the same cryptographic keys across multiple installations be pa-dss compliant? |
| #1053 | Can a payment application that uses cryptographic keys hard-coded by the vendor be pa-dss compliant if they cannot be changed by the customer? |
| #1054 | does the pCi security standards Council provide information on security breaches, status of investigations, or pCi dss compliance status? |
| #1055 | should i complete the prioritized approach milestones in sequential order? |
| #1060 | how would an identified denial of service (dos) vulnerability affect a company's ability to pass a pCi dss vulnerability scan from an approved scanning vendor (asv)? |
| #1061 | how frequently will the pCi security standards Council update the pCi dss and pa-dss? |
| #1062 | What is meant by a “payment application” in part 2d of the attestation of Compliance? |
| #1063 | does saQ C-vt replace saQ C? |

(*continued*)

<!-- PDF p. 520 (book p. 502) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1064 | What is a vt or virtual terminal? |
| #1065 | should service providers demonstrate pCi dss compliance as part of their client’s assessment or in their own separate assessment? |
| #1066 | What is an “inactive user account” as used in pCi dss requirement 8.1.4? |
| #1067 | What is meant by “non-consumer users” in pCi dss requirement 8? |
| #1068 | are digital leased lines considered public or private? |
| #1069 | does pCi dss apply to paper with cardholder data (e.g., receipts, reports, etc.)? |
| #1070 | are digital images containing cardholder data and/or sensitive authentication data included in the scope of the pCi dss? |
| #1071 | Can the full credit card number be displayed within a browser window? |
| #1072 | What is the purpose of requiring account lockout, per pCi dss requirements 8.1.6 and<br>8.1.7? |
| #1073 | What are the pCi dss requirements regarding transmission of cardholder data via<br>Bluetooth technology? |
| #1074 | is intrusion detection required if centralized log correlation is in place? |
| #1075 | is it permissible to use self-decrypting files for encryption to send cardholder data? |
| #1076 | is it permissible to use Ftp if proper security measures are implemented? |
| #1077 | how extensive must background checks be for employees who have access to cardholder data? |
| #1078 | in what circumstances is multi-factor authentication required? |
| #1079 | What is the definition of “merchant”? |
| #1080 | are administrators allowed to share passwords? |
| #1081 | do pCi dss requirements 10.2 and 10.3 mean that both database and application logging are required? |
| #1082 | if a merchant has multiple processing environments, should the merchant complete multiple saQs to validate their pCi dss compliance? |

(*continued*)

<!-- PDF p. 521 (book p. 503) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1083 | What is the mission of the pCi security standards Council? |
| #1084 | What is the intent of pCi dss requirement 3.4.1? |
| #1085 | Can unencrypted pans be sent over email, instant messaging, sms, or chat? |
| #1086 | how does encrypted cardholder data impact pCi dss scope? |
| #1087 | For vulnerability scans, what is meant by quarterly? |
| #1088 | What is meant by “adequate network segmentation” in the pCi dss? |
| #1089 | are hashed primary account numbers (pan) considered cardholder data that must be protected in accordance with pCi dss? |
| #1091 | What are acceptable formats for truncation of primary account numbers? |
| #1092 | does pCi dss apply to merchants who outsource all payment processing operations and never store, process, or transmit cardholder data? |
| #1093 | does requirement 3.4 apply to mainframes? |
| #1094 | Will the pCi security standards Council be involved in performing forensic investigations as a result of an account data compromise event? |
| #1095 | What will be the role of the pCi security standards Council in expanding the global coverage of both Qsas and asvs? |
| #1096 | When a Qsa or asv is newly approved, who is the contact at the pCi security standards<br>Council to request a press release? |
| #1115 | how does pCi dss apply to individual pCs or workstations? |
| #1117 | are truncated primary account numbers (pan) required to be protected in accordance with pCi dss? |
| #1122 | What is the scope of the pCi security standards Council's activities? |
| #1123 | in what way does the pCi security standards Council make payment card data more secure? |
| #1124 | pCi dss provides a common data security standard across all payment brands. are there any plans to provide a common structure of penalties and/or fines for non-compliance to this standard? |

(*continued*)

<!-- PDF p. 522 (book p. 504) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1125 | are there any plans for pCi ssC to be a single point of contact for a merchant, financial institute, or processor to send a pCi dss compliance report to? |
| #1126 | how do i determine whether my business would be required to conduct an independent assessment or a self-assessment? |
| #1127 | is there opportunity to provide feedback on the pCi Council's standards? |
| #1128 | What happens if i'm using a pa-dss-validated payment application that is breached? |
| #1129 | does media containing cardholder data (e.g., backup tapes or disks) need to be physically labeled as confidential for pCi dss requirement 9.6.1? |
| #1130 | are operating systems that are no longer supported by the vendor non-compliant with the pCi dss? |
| #1131 | does the council have a mapping between pCi dss and iso 27002 (formerly iso 17799) or other standards? |
| #1132 | What is an attestation of Compliance? |
| #1133 | Why are there multiple pCi dss self-assessment Questionnaires (saQs)? |
| #1134 | What are the steps needed to perform a self-assessment to validate compliance with pCi dss? |
| #1135 | Can vlans be used for network segmentation? |
| #1136 | Can the full payment card number be printed on the consumer's copy of the receipt? |
| #1137 | how can i validate if a number is a legitimate credit card number? |
| #1138 | does pCi ssC provide a list of pCi dss-compliant service providers? |
| #1139 | Can i fax payment card numbers and still be pCi dss Compliant? |
| #1140 | Which self-assessment Questionnaire (saQ) should i complete? |
| #1141 | What are the fines and penalties assessed to companies for non-compliance with the pCi dss? |
| #1142 | how do i contact the payment card brands? |
| #1146 | What is the difference between masking and truncation? |

(*continued*)

<!-- PDF p. 523 (book p. 505) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1147 | What is the purpose of requiring consoles/pCs to become “locked” after 15 minutes of idle time, per pCi dss requirement 8.1.8? |
| #1152 | Can an entity be pCi dss compliant if they have performed quarterly scans, but do not have four “passing” scans? |
| #1153 | how does pCi dss apply to voip? |
| #1154 | is pre-authorization account data in-scope for pCi dss? |
| #1155 | Which service provider category should i use for part 2 of the pCi dss attestation of<br>Compliance (aoC) for service providers? |
| #1156 | are call center environments considered “sensitive areas” for pCi dss requirement<br>9.1.1? |
| #1157 | What should a merchant do if cardholder data is accidentally received via an unintended channel? |
| #1158 | What effect does the use of a pCi-listed p2pe solution have on a merchant's pCi dss validation? |
| #1162 | Can merchants use encryption solutions not listed on the pCi Council's web site to reduce their pCi dss validation effort? |
| #1163 | is a “p2pe assessor” required for a merchant's pCi dss assessment if the merchant uses a Council-listed p2pe solution? |
| #1164 | is the pCi p2pe standard applicable for merchants that have developed/implemented their own encryption solution? |
| #1165 | are p2pe solution providers required to have their solutions validated and listed by the<br>Council? |
| #1166 | Which pCi pts point-of-interaction (poi) devices can be used in a validated p2pe solution? |
| #1168 | What assurances does the Council provide regarding the quality of organizations assessing my systems for compliance with the pCi standards? |
| #1169 | What are the Council's requirements for Qsa and asv Companies to maintain a Quality assurance (Qa) manual? |

(*continued*)

<!-- PDF p. 524 (book p. 506) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |  |
|---|---|---|
| #1170 | how does the prioritized approach work? |  |
| #1171 | is the prioritized approach mandatory? |  |
| #1172 | does the prioritized approach replace the pCi dss? |  |
| #1173 | Who is qualified to perform pa-dss assessments? |  |
| #1174 | For the list of validated pa-dss applications, what is the difference between revalidation date and expiry date? |  |
| #1175 | if a merchant is using a payment application listed as “acceptable only for pre-existing deployments,” is the merchant allowed to install more copies of the application? |  |
| #1176 | how does an organization maintain compliance when a standard changes? |  |
| #1177 | how does my company become a qualified assessor (Qsa, pa-Qsa, Qsa (p2pe), pa-Qsa<br>(p2pe)) or approved scanning vendor (asv)? |  |
| #1178 | how do i reduce the scope of a pCi dss assessment? |  |
| #1181 | how can i check whether a payment application is pa-dss validated? |  |
| #1182 | is it acceptable to make minor changes to a pa-dss-validated application and retain the existing version number? |  |
| #1183 | the pa-dss program Guide says application version numbers may consist of a combination of fixed and variable alphanumeric characters. What does this mean? |  |
| #1195 | What is the difference between a validated payment application which is shown on the pCi ssC web site as “acceptable for new deployments” and one which is shown as<br>“acceptable only for pre-existing deployments”? |  |
| #1196 | if i am deemed pCi dss compliant today by one of the payment card brands, will the other brands in the pCi security standards Council recognize this designation of compliance, and if so, what information must be put forth to achieve such recognition? |  |
| #1210 | are audio/voice recordings permitted to contain sensitive authentication data? |  |
| #1211 | to whom should media inquiries or requests for interviews about the pCi security standard Council be directed? | (continued) |

<!-- PDF p. 525 (book p. 507) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1212 | What is the involvement of the pCi ssC on the compliance validation processes for pCi dss assessments and scan reports? |
| #1213 | are there any plans to standardize the reporting requirements (reports) for the pCi dss, pa-dss, asv, Qsa, and pts programs that are sent to each of the payment brands? |
| #1214 | do the pCi dss requirements apply to card manufacturers, embossers, card personalizers, or entities that prepare data for card manufacturing? |
| #1216 | does the pCi dss apply to acquirers? |
| #1217 | does the pCi dss apply to issuers? |
| #1220 | are compliance certificates recognized for pCi dss validation? |
| #1221 | do shared hosting providers need to comply with pCi dss? |
| #1222 | does cardholder name, expiration date, etc. need to be rendered unreadable if stored in conjunction with the pan (primary account number)? |
| #1223 | does pCi dss, pa-dss, or pts apply to atms? |
| #1224 | What does one function per server mean? |
| #1225 | What is the relationship between the pCi data security standard and the payment application data security standard and pts device security requirements? |
| #1226 | What is the role of the advisory Board? |
| #1227 | Who are the founders of the pCi security standards Council? |
| #1228 | Will the pCi security standards Council approve and list vendors for participation in forensic investigations? |
| #1229 | What is saQ C-vt? |
| #1233 | how does encrypted cardholder data impact pCi dss scope for third-party service providers? |
| #1234 | i have had an external vulnerability scan completed by an asv, does this mean i am pCi dss compliant? |

(*continued*)

<!-- PDF p. 526 (book p. 508) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1235 | if a merchant or service provider has internal corporate credit cards used by employees for company purchases like travel or office supplies, are these corporate cards considered “in-scope” for pCi dss? |
| #1246 | Can a Qsa that is not also a p2pe assessor validate if an encryption solution meets p2pe requirements? |
| #1247 | Who can use saQ p2pe? |
| #1248 | in p2pe, how do “hybrid” decryption environments differ from “hardware” decryption environments? |
| #1251 | What is the process to use previously deployed poi devices in a pCi p2pe solution? |
| #1252 | do all pCi dss requirements apply to every system component? |
| #1253 | does hashing of passwords meet the intent of pCi dss requirement 8.2.1? |
| #1254 | What is the intent of pCi dss requirement 10? |
| #1257 | Can i report on my prioritized approach progress instead of producing a report on<br>Compliance or attestation of Compliance? |
| #1258 | does pCi ssC endorse specific products to meet pCi dss requirements? |
| #1261 | does a p2pe-validated application also need to be validated against pa-dss? |
| #1262 | Will pa-dss-validated applications continue to be acceptable for new deployments if they run on an unsupported operating system? |
| #1263 | What are the Card production logical and physical security requirements? |
| #1265 | Can i combine sections from different versions of the pCi dss? |
| #1266 | i'm in the middle of a pCi dss assessment when a new version is released, should i start again using the new version? |
| #1270 | how do the requirements in pCi dss version 3 that are “best practices” until June 30,<br>2015, impact my pCi dss assessment? |
| #1271 | Can i combine sections from different versions of the pa-dss? |
| #1272 | Can my payment application be validated using pa-dss version 1.2.1? |
| #1273 | Can my payment application be validated using pa-dss version 3.0 or 3.1? |

(*continued*)

<!-- PDF p. 527 (book p. 509) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1274 | Can my payment application be validated using pa-dss version 2? |
| #1275 | What are the pa-dss expiry dates? |
| #1277 | are merchants required to meet pCi dss requirement 12.9? |
| #1278 | are pa-dss applications considered valid if installed on an operating system that is not included in the payment application listing? |
| #1279 | how does using a pa-dss-validated application affect the scope of a merchant's pCi dss assessment? |
| #1280 | Can card verification codes/values be stored for card-on-file or recurring transactions? |
| #1281 | are point-of-sale devices required to be physically secured (e.g., with a cable or tether) to prevent removal or substitution in order to meet pCi dss requirement 9.9? |
| #1282 | Can an entity be pCi dss compliant if they use a service provider that is validated to a previous version of pCi dss? |
| #1283 | if a merchant develops an application that runs on a consumer's device (e.g., smartphone, tablet, or laptop) that is used to accept payment card data, what are the merchant's obligations regarding pCi dss and pa-dss for that application? |
| #1284 | are acquirers considered service providers for the purpose of pCi dss requirements 12.8 and 12.9? |
| #1285 | does pCi dss apply to one-time or single-use pans? |
| #1286 | does pCi dss apply to virtual (electronic-only) pans? |
| #1287 | Why does pa-dss v3 require passwords to be protected by a one-way hash (requirement<br>3.3.2), whereas pans can be stored in an encrypted form (requirement 2.3)? |
| #1288 | does pa-dss requirement 3.3.2 apply to passwords used by the payment application to access other systems/applications (e.g., for the payment application to access a third-party database)? |
| #1289 | does the pa-dss v3 requirement for hashing stored passwords meet pCi dss requirement 8.2.1? |

(*continued*)

<!-- PDF p. 528 (book p. 510) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1290 | if a merchant uses a service provider to host part or all of their Cde and the service provider has been validated as pCi dss compliant, is the merchant's assessor required to go onsite to the third-party location and retest the pCi dss requirements? |
| #1291 | Why is saQ a-ep used for direct post while saQ a is used for iFrame or url redirect? |
| #1292 | Why is there a different approach for direct post implementations than for iFrame and url redirect – what are the technical differences and how do they impact the security of e-commerce transactions? |
| #1293 | if a merchant's e-commerce implementation meets the criteria that all elements of payment pages originate from a pCi dss-compliant service provider, is the merchant eligible to complete saQ a or saQ a-ep? |
| #1299 | are manual imprinter machines in-scope for pCi dss requirements? |
| #1300 | how does pCi dss apply to payment terminals? |
| #1301 | how do pts-approved payment terminals support pCi dss compliance? |
| #1302 | how does use of an expired pts device affect my pCi dss compliance? |
| #1304 | What devices does pCi dss requirement 10.6.2 apply to? |
| #1305 | do you offer examination accommodation? |
| #1306 | are pCi Forensic investigators (pFis) permitted to enter into retainer-type agreements with merchants and service providers? |
| #1308 | how can an entity ensure that hashed and truncated versions cannot be correlated as required in pCi dss requirement 3.4? |
| #1309 | must payment applications ensure that hashed and truncated versions cannot be correlated? |
| #1310 | are merchants allowed to request that cardholder data be provided over end-user messaging technologies? |
| #1311 | are pFi Companies which are “in remediation” permitted to perform investigations? |
| #1312 | if an entity uses a service provider that is not pCi dss compliant, how does this impact the entity's compliance? |

(*continued*)

<!-- PDF p. 529 (book p. 511) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1313 | Can saQ B-ip be used if cardholder data is transmitted over wireless? |
| #1314 | is storage of encrypted cardholder data considered “cardholder data” per the saQ eligibility criteria? |
| #1315 | is storage of truncated pan considered storage of “cardholder data” per the saQ eligibility criteria? |
| #1316 | are merchants required to perform the “expected testing” in the saQs? |
| #1317 | What is a “significant change” for pCi dss requirements 11.2 and 11.3? |
| #1318 | What is the maximum period of time that cardholder data can be stored? |
| #1319 | are merchants allowed to request card verification codes/values from cardholders? |
| #1320 | Who do i report insecure merchant behavior to? |
| #1321 | do parent/subsidiary companies validate as a single entity or as separate entities? |
| #1322 | What are the expiry dates for pts poi device approvals? |
| #1323 | are disaster recovery (dr) sites in-scope for pCi dss? |
| #1324 | What changes are pFi companies allowed to make to the pFi reporting templates? |
| #1325 | does pCi ssC provide a “pCi dss Compliant” logo? |
| #1326 | how does pCi dss apply to emvCo payment tokens? |
| #1327 | do pans need to be masked on cardholder statements sent by issuers to customers? |
| #1328 | What version of pCi dss should i use? |
| #1329 | What is the current version of pa-dss? |
| #1330 | For p2pe solutions, can you use pCi-approved poi devices with sred, where the pts listing indicates “non-Ctls”? |
| #1331 | Can saQ eligibility criteria be used for determining applicability of pCi dss requirements for onsite assessments? |
| #1332 | is a merchant web site still in-scope for pCi dss if it meets all the criteria for saQ a? |
| #1333 | Can pCi dss compliance be determined by testing only pre-production environments using test data? |

(*continued*)

<!-- PDF p. 530 (book p. 512) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1334 | Where can i find unlocked versions of the aoCs and saQs? |
| #1335 | does pCi dss apply to bank account data? |
| #1338 | What is the difference between poi firmware and additional software that may be present on the poi device? |
| #1339 | are poi devices with only the pts-approved firmware (i.e., no additional software) eligible for use in a pCi p2pe solution? |
| #1354 | Can the aoC be redacted to protect sensitive information? |
| #1355 | are applications listed as acceptable only for pre-existing deployments able to meet the current pa-dss and pCi dss? |
| #1356 | What does “duly authorized officer” mean? |
| #1358 | Which version of the p2pe standard should be used for a p2pe assessment? |
| #1367 | Can pCi-listed p2pe v1.1 applications be used in pCi p2pe v2 solutions? |
| #1368 | Can pCi-listed p2pe v2 applications be used in a pCi p2pe v1.1 listed solution? |
| #1369 | does pCi p2pe v2 allow for partial assessments of third parties with services that will be used in one or more p2pe solutions? |
| #1372 | how should entities apply the new ssl/tls migration dates to requirements 2.2.3, 2.3, and 4.1 for pCi dss v3.1? |
| #1373 | how should entities complete their roC or saQ for pCi dss v3.1 using the new ssl/tls migration dates? |
| #1374 | is payment account reference (par) as defined by emvCo considered pCi account data? |
| #1375 | Can an attestation of Compliance (aoC) be provided to an assessed entity before the report on Compliance (roC) is finalized? |
| #1382 | Can a partial pCi dss assessment be documented in a report on Compliance (roC)? |
| #1383 | to whom do the pCi token service provider security requirements apply? |
| #1384 | What is the difference between “acquiring tokens,” “issuer tokens,” and “payment tokens”? |
| #1385 | Which types of tokens are addressed by the pCi ssC tokenization documents? |

(*continued*)

<!-- PDF p. 531 (book p. 513) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1425 | What is the difference between “multi-factor” authentication and “two-factor” authentication? |
| #1426 | is “two-step” authentication the same as “two-factor” or “multi-factor” authentication? |
| #1427 | are oems and/or hardware/software resellers subject to pCi dss requirements 12.8 and<br>12.9? |
| #1434 | how do pCi pts-approved poi device expiry dates affect a pCi-listed p2pe solution? |
| #1435 | What is the Council's guidance on the use of sha-1? |
| #1436 | Who has to comply with the pCi standards? |
| #1437 | Can pCi dss be used to protect non-payment card data? |
| #1438 | how is the payment page determined for saQ a merchants using iFrame? |
| #1439 | how do pCi dss requirements 2, 6, and 8 apply to saQ a merchants? |
| #1440 | how does pCi dss appendix a2 apply after the ssl/early tls migration deadline? |
| #1441 | how do the updated ssl/early tls migration dates apply to service providers? |
| #1442 | Can merchants using non-console administrative access be eligible for saQ B-ip, C-vt, or C?) |
| #1443 | What is the intent of the saQ eligibility criteria? |
| #1444 | Can a pFi Company perform subsequent pFi investigations for the same entity? |
| #1445 | how should Qsa assistance with completion of self-assessment Questionnaire (saQs) be documented? |
| #1446 | how did prioritized approach tool calculations change for dss v3.2? |
| #1447 | how does pCi dss requirement 11.3.4.1 impact timing of penetration tests for service providers? |
| #1448 | What is meant by “at risk” and “at-risk timeframe” referenced in the Final pFi report? |
| #1449 | is two-step authentication acceptable for pCi dss requirement 8.3? |
| #1450 | Where can i find more information about the assessment Guidance for non-listed encryption solutions (a.k.a. nesa)? |

(*continued*)

<!-- PDF p. 532 (book p. 514) -->

**Table 17-1.** (*continued*)

| Ref # | Frequently Asked Question (FAQ) |
|---|---|
| #1451 | Can pFis provide reports to their clients before sending the report to the affected payment brands? |
| #1452 | how does triple dea (tdea) impact asv scan results? |
| #1453 | Can a pFi Company provide Qsa services to an entity after performing a pFi investigation for that entity? |
| #1454 | What is the intent of “administrative access” in pCi dss? |
| #1455 | does a Qsa need to be onsite at the client's premises for all aspects of a pCi dss assessment? |
| #1456 | Can pCi ssC revoke a Qsa Company's eligibility to participate in the associate Qsa program due to quality concerns in connection with that program, and not revoke qualification as a Qsa Company? |
| #1457 | is a software-based pin entry on Cots solution eligible for a p2pe solution approval? |
| #1458 | What date should be used for “date of report” in the roC? |
| #1460 | Where should reports be sent when the pFi investigation has concluded there is no evidence of a breach? |
| #1461 | What are the security considerations for tls 1.3? |
| #1462 | What does “Window of payment Card data storage” mean in the Final pFi report template? |
| #1464 | does the use of expired pts poi devices meet eligibility criteria for saQ B-ip? |
| #1467 | Can organizations use alternative password management methods to meet pCi dss requirement 8? |
| #1468 | Can i have the same assessor company or individual assessor perform a pCi dss and pin assessment for our organization? |
| #1469 | how do pCi pts-approved hsm expiry dates affect a pCi-listed p2pe solution or Component? |
| #1470 | are pFis required to fill out all the fields in the Final pFi report? |
| #1471 | What does “servicing market” on the Qsa listing mean? |
| #1472 | how can i determine whether a Qsa is authorized to perform pCi dss assessments in all countries that are in-scope for my company's pCi dss assessment? |
