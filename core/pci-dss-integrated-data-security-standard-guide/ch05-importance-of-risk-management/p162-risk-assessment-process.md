---
title: "Risk Assessment Process"
book: pci-dss-integrated-data-security-standard-guide
chapter: 5
source_pages: "162-163"
format: source-text
---
# Risk Assessment Process
(Source: PDF pp. 162-163)

<!-- PDF p. 162 (book p. 139) -->

Having created your suite of appropriate and credible risk assessment scenarios, you are then able to start applying your risk assessment processes to ensure that the risks are effectively articulated to Senior Management. This will ensure that any risks remain within your businesses risk tolerances/appetites and will ensure that senior management have sufficient data to make informed risk decisions and ensuring that this answers their “So What?” questions in regard to any identified risks (Vulnerability × Threat × Impact).

remember, your senior management have got to where they are in their careers because they are good at doing business and not because they are risk or security experts. Consequently, you need to ensure that only relevant/critical risks are communicated to them for their attention and that these messages are articulated in a manner that is concise and presented in a way that is easy for them to understand (avoid the unnecessary use of technical or Cyber/InfoSec specific terminologies).

try using concise methodologies to effectively articulate the results of your risk assessments, such as

FAIR (factor analysis of Information risk)

BRA (Binary risk analysis)

CIS RAM (Center for Internet security risk assessment method)

DoD RMF (risk management framework)

Whichever risk assessment process you decide to apply, it needs to be consistently applied across your business. For example, both the NIST SP800-30, r1,[^33] and FAIR employ four distinct steps to their risk assessment processes.

[^33]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf

<!-- PDF p. 163 (book p. 140) -->

| Stage | NIST SP800-30 r1 | FAIR |
|---|---|---|
| 1 | Prepare for assessment<br>• Derived from organizational risk frame | Identify scenario components<br>• Identify the asset at risk<br>• Identify the threat community under consideration |
| 2 | Conduct assessment<br>• Identify threat sources and events<br>• Identify Vulnerabilities and predisposing<br>Conditions<br>• Determine Likelihood of occurrence<br>• Determine magnitude of Impact<br>• Determine risk | Evaluate loss event frequency (LEF)<br>• estimate the probable threat event frequency (tef)<br>• estimate the threat capability (tCap)<br>• estimate control strength (Cs)<br>• Derive Vulnerability (Vuln)<br>• Derive loss event frequency (Lef) |
| 3 | Communicate results | Evaluate probable loss magnitude (PLM)<br>• estimate worst case loss<br>• estimate probable loss magnitude (pLm) |
| 4 | Maintain assessment | Derive and articulate risk |

PCI DSS does not stipulate the risk assessment methodology that you apply to support your risk management process, only that you have a formalized and consistent approach that is reviewed on an annual basis. The most difficult part of the risk assessment process is being able to articulate and communicate this in a manner that means something to your senior management, for example:

- **PCAN** (Problem, Cause, Answers, and Net Benefits)
- **BSC** (Balanced Score Cards)[^34]
- **KRI** (Key Risk Indicator) Heat Maps/Matrices[^35]
- **Risk Dashboard**[^36]

[^34]: http://iia.org.au/sf_docs/default-source/technical-resources/2018-whitepapers/iia-whitepaper_balanced-scorecard-reporting.pdf?sfvrsn=2
[^35]: https://riskmanagementguru.com/risk-matrices-pros-cons-and-alternatives.html/
[^36]: https://acuityrm.com/platform
