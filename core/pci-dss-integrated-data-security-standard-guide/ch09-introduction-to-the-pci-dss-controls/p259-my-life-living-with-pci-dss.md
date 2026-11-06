---
title: "My Life Living with PCI DSS"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "259-262"
format: source-text
---
# My Life Living with PCI DSS
(Source: PDF pp. 259-262)

<!-- PDF p. 259 (book p. 237) -->

Two months into my first appointment within the corporate world, I was selected as the Baseline Security Controls manager, responsible for the successful implementation of a Baseline Security Controls framework. This project first introduced me to the implementation of a suite of industry security controls (ISO 27002, PCI DSS, COBIT 4.1), which were to be aligned to various departments within a financial services institution. This proved to be an extremely useful experience, as the need for detailed cross-mapping helped me understand the similarities and commonalities of different frameworks.

Sequentially to this, I sought to transfer my knowledge gained through the RAF Police for a globally recognized industry information security course and successfully self-studied to become ISACA Certified Information Security Management (CISM) qualified.

My second appointment, within the corporate world, was to join a small Cyber/ InfoSec consultancy team for an organization that provided network security services, penetration testing, and professional consultancy services (including QSA).[^8] This began my journey into the development of a comprehensive understanding of the PCI DSS controls framework.

[^8]: www.professionalsecurity.co.uk/news/interviews/cyber-reserve-unit/

<!-- PDF p. 260 (book p. 238) -->

However, after almost 5 years working as a QSA, I started to become a little disillusioned with the payment card industry’s (PCI’s) tick box approach and the inconsistencies with the interpretation of the standard.

Here are a couple of examples:

1. On one occasion, I had my advice overruled by one of the card brands. I had been carrying out a gap assessment for a client who was a Service Provider, providing printing services for financial institutions. Part of this service included the printing of account statement, which included the full PAN in clear text *(as this was used as the customers’ account information)* which was then posted out, in bulk, via standard post.

Consequently, owing to the known threat that criminals will intercept the post to steal PANs and PINs,[^9] I advised the client that they should try to avoid printing out the full PAN *(not possible)* or to apply PCI DSS control 9.6.2 *(sending media by trackable means, rather through standard post)* to help mitigate this risk.

The client objected, based upon the potential cost implications, and asked that I escalate the incident to the Card Brands. Approximately, 3 months later I received an extremely disappointing response from the Card Brands who contradicted my advice, stating that *(due to the cost implications)* this control does not apply to Financial Institutions.

2. While working with a Financial Institution, to help them align their Acquirer payment card operations of their business with PCI DSS, we were trying to understand and identify the extent of their scope. This was proving to be extremely difficult, as their systems that supported their in-scope systems were heavily entwined with their other payment card operations. Applying the concept that PCI DSS applies to any IT system that directly processes, transmits, or stores *(or any IT systems that could impact)*, <!-- PDF p. 261 (book p. 239) --> as you can imagine as we started to identify and visualize the environment, the scope started to significantly grow.

[^9]: www.usnews.com/news/best-states/new-jersey/articles/2019-12-19/ex-postal-worker-admits-taking-bribes-to-steal-credit-cards

The discussions with the Card Brands resulted in their advice that it was important to remember that the Financial Institution did not need to be PCI DSS compliant *(thankfully, this is a message that has appeared to have changed*[^10]*)* so any in-scope systems that were deemed to be severely intertwined with any out-of-scope systems could be deemed as being out-of-scope.

3. I had been carrying out a gap assessment for a UK-based business, during which their US-based sister company had approximately a dozen of their customer payment cards breached. Consequently, the UK client had asked if I would be willing to go out to the United States to carry out a formal assessment of their sister company, following their remediation efforts. Initial discussions were made with their Acquirer to confirm what they would deem to be acceptable. Being that the client was a small business and only processed a small volume of payment cards, it was agreed that they would accept an onsite completion of a version 2.0, self-assessment questionnaire (SAQ) C by a QSA.

The client was happy with this proposal and asked if I would be willing to go out to the United States to complete this assessment. I was happy to oblige but advised them that they might be better served by engaging with a local QSA company, so as to avoid unnecessary additional travel and accommodation costs.

Several weeks later, I was tasked to go out to the United States to carry out the formal onsite assessment of the sister company. The reason being that despite the fact that their Acquirer had stated they were happy with the QSA completing a SAQ, every QSA Company had appeared to have seen the dollar signs and would only quote for the time-consuming and lengthy completion of a full-blown report on compliance (RoC).

[^10]: https://globalrisk.mastercard.com/wp-content/uploads/2019/06/Q2-2019-PCI-Quarterly-Newsletter.pdf

<!-- PDF p. 262 (book p. 240) -->

4. During another engagement, I was tasked to deliver a 10-day engagement to provide a PCI DSS assessment for a US marketing company, providing services to some large, well-known US retailers.

Previously, the client had been sold a number of security tools and policy templates to help support their PCI DSS compliance efforts and were now apparently ready for their assessment. On arrival, at the client site, I commenced with the planning and preparation phase of the engagement by asking the question

**“So, describe to me how your business is involved with payment card data?”**

The reply:

**“We don’t! Our clients have asked us to become PCI DSS compliant!”**

As a consequence, as the result of the salesperson just selling them the requested service without confirming the requirements, the client had incurred unnecessary expense. I ended up delivering them an alternative effective data privacy and security strategy to provide the assurance that their clients were seeking.
