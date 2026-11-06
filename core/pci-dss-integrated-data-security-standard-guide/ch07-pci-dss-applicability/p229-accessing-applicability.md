---
title: "Accessing Applicability"
book: pci-dss-integrated-data-security-standard-guide
chapter: 7
source_pages: "229-231"
format: source-text
---
# Accessing Applicability
(Source: PDF pp. 229-231)

<!-- PDF p. 229 (book p. 206) -->

Now that you have an appreciation of what type of data makes your business applicable to the PCI DSS, it is essential to trace the journey of the data, so as to identify the extent of the environments that need to be aligned.

Tracing the journey starts at the point of origin (where the consumers’ payment card data is entrusted to you), right through to its final secure disposal/destruction and

**Figure 7-7.** *Gifting Away CHD*

<!-- PDF p. 230 (book p. 207) -->

including any local reproductions/duplications that are taken from your main data vaults (e.g., local spreadsheets, tables, etc.), and to include any third parties that may come into contact with such data assets.

Unfortunately, you may have fallen into the trap of only looking at the card payment operations and have omitted to include the associated systems, interfaces, suppliers, personnel, and business operations.

For example, what happens to the PANs, which, for convenience, are given a duplicated use as being their account number?

- Printed in full on monthly account statements?
- Added to correspondence?
- Used as a means to carry out online password resets?

*[Figure omitted]*

**Figure 7-8.** *Web Page Using Full PAN Entry*

Consequently, it is essential that for any PCI DSS compliance efforts all applicable interfaces, storage locations, and connected systems/applications are identified in order to identify all potential avenues, which may not have been secured but could be advantageous for the criminal to exploit.

<!-- PDF p. 231 (book p. 208) -->

Identify all your “Nooks and Crannies,” where ChD may be residing!

Recent data breaches, such as the Magecart Group[^2] and Mastercard,[^3] have demonstrated that today’s criminals will seek any opportunity to exploit poor security practices. Additionally, criminals have turned data theft into an extremely profitable professional and are even known to have created online business-style models[^4] to achieve this very goal.

*[Figure omitted]*

**Figure 7-9.** *Criminal Gang Hierarchy*

[^2]: https://threatpost.com/magecart-ecommerce-card-skimming-bonanza/147765/
[^3]: www.finextra.com/newsarticle/34310/mastercard-loyalty-programme-customers-hit-by-data-leak
[^4]: www.ncsc.gov.uk/news/ncsc-publishes-new-report-criminal-online-activity
