---
title: "Chapter 2: The Evolution of PCI DSS (opening)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 2
source_pages: "53-59"
format: source-text
---
# Chapter 2: The Evolution of PCI DSS (opening)
(Source: PDF pp. 53-59)

<!-- PDF p. 53 (book p. 29) -->

Many believe that the Payment Card Industry Data Security Standard (PCI DSS) began in December 2004. However, much like Darwin’s theory of evolution, the evolution of the PCI DSS controls framework has a much longer history.

To truly appreciate the evolution of the PCI DSS integrated framework, it is important to take a look at its roots to ascertain the lessons learned from history, previous associated controls frameworks, and the evolutionary changes that inspired the need for the development of an effective defensive controls framework for the protection of payment card data.

Over the centuries (yes, centuries), we have seen significant changes in the way customers purchase goods and services using payment cards:

1. Starting with the clay tablets[^1] used by the ancient Mesopotamians in around 3300 BC which were used as means of credit for the purchase of goods.

*[Figure omitted]*

**Figure 2-1.** *Clay Tablet*

[^1]: www.metmuseum.org/toah/works-of-art/1988.433.3/

<!-- PDF p. 54 (book p. 30) -->

2. Next came, in the 1800s, the United States’ use of charge plates[^2] as the precursor to the modern-day payment card.

*[Figure omitted]*

3. In the 1880s, the Provident Clothing Group (United Kingdom) introduced a credit voucher[^3] – often regarded as one of the precursors to the modern-day payment card.

4. The 1950s saw the introduction of the Diners’ Club card.[^4]

*[Figure omitted]*

5. In 1958, American Express introduced the first embossed plastic cards.[^5]

**Figure 2-2.** *Charge Plate*

**Figure 2-3.** *Diners’ Club Card*

[^2]: www.digibarn.com/collections/small-items/charga-plate/index.html
[^3]: www.theukcardsassociation.org.uk/history_of_cards/index.asp
[^4]: www.timetoast.com/timelines/credit-card-in-1950
[^5]: www.relativelyinteresting.com/evolution-credit-card-paper-plastic-virtual/

<!-- PDF p. 55 (book p. 31) -->

*[Figure omitted]*

6. In the 1970s, a joint pilot project by American Express,[^6] American

Airlines, and IBM took place at Chicago’s O’Hare Airport. American Express issued hundreds of new cards to frequent travelers in the Chicago area and allowed for electronic payment for tickets and other services using these new cards.

*[Figure omitted]*

7. The 1990s saw the introduction of the first form of digital wallet.[^7]

However, the early versions were extremely unreliable, and these did not become popular until Apple debuted their version in October 2014.

**Figure 2-4.** *AMEX Payment Card*

**Figure 2-5.** *AMEX Mag Stripe Payment Card*

[^6]: https://postalmuseum.si.edu/americasmailingindustry/American-Express.html
[^7]: https://due.com/blog/digital-wallet-revolution/

<!-- PDF p. 56 (book p. 32) -->

*[Figure omitted]*

It is very clear that over the centuries advancements in technologies have increased the convenience of making instant payments through the use of payment cards. Hence, the consumers are increasingly choosing payment cards as their preferred choice for making payments.[^8]

**Figure 2-6.** *Mobile Payments*

*[Figure omitted]*

**Figure 2-7.** *Global Share of Point-of-Sale (PoS) Payment Methods*

[^8]: https://worldpay.globalpaymentsreport.com/#/

<!-- PDF p. 57 (book p. 33) -->

*[Figure omitted]*

This progressive move toward more convenient technical based payments[^10] has made this increasingly attractive to opportunist criminals, with the volume of data breaches[^11] and cases of identity theft continuing to grow, with business being the greatest victim of criminal activity.

**Figure 2-8.** *Global E-commerce Trends*[^9]

[^9]: www.emarketer.com/content/global-ecommerce-2019
[^10]: www.ukfinance.org.uk/sites/default/files/uploads/pdf/UK-Finance-UK-Payment-Markets-Report-2019-SUMMARY.pdf
[^11]: https://safeatlast.co/blog/data-breach-statistics/#gref

<!-- PDF p. 58 (book p. 34) -->

*[Figure omitted]*

*[Figure omitted]*

As a consequence, the Card Brands (Mastercard, Visa, American Express, JCB, and Discover) started to develop their own suites of defensive control sets:

- *Visa’s Cardholder Information Security Program*
- *Mastercard’s Site Data Protection*
- *American Express’s Data Security Operating Policy*
- *Discover’s Information Security and Compliance*
- *JCB’s Data Security Program*

In 2004, the Payment Card Industry Security Standards Council (PCI SSC) had been appointed to develop and manage a single integrated controls framework (Payment Cards Industry Data Security Standard (PCI DSS) v1.0). The intended purpose being to provide payment card processing businesses with a suite of security controls to help them harden the payment card defenses. Consequently, any business involved in the processing, storage, or transmission of payment card data must apply the applicable controls from the PCI DSS catalogue of controls.

*Source: Statistica*[^12]

*Source: FTC Consumer Sentinel Network Databook 2018*[^13]

[^12]: www.statista.com/statistics/273572/number-of-data-breaches-in-the-united-states-by-business/
[^13]: www.ftc.gov/system/files/documents/reports/consumer-sentinel-network-data-book-2018/consumer_sentinel_network_data_book_2018_0.pdf

<!-- PDF p. 59 (book p. 35) -->

Failure to demonstrate their annual compliance to these controls *(using the self- assessment questionnaire (SAQ) or report on compliance (RoC) formats (or self-attested for regulated Merchant/Acquirer/Issuer Bank))* would likely lead to a monthly non-compliance (miscellaneous) charge,[^14] fine, or withdrawal of license to take payments through payment cards.[^15]

[^14]: www.worldpay.com/en-us/insights-hub/article/how-to-become-pci-compliant
[^15]: www.theukcardsassociation.org.uk/security/Non_compliance_PCIDSS.asp
