---
title: "Introduction"
book: pci-dss-integrated-data-security-standard-guide
chapter: 4
source_pages: "98-101"
format: source-text
---
# Introduction
(Source: PDF pp. 98-101)

<!-- PDF p. 98 (book p. 74) -->

When looking at an integrated Cyber/InfoSec strategy, it is important to understand the four domains that are needed to achieve an effective program. Each domain is important to each other, but it is extremely important to remember that they are complementary to each other, with a considerable amount of overlap.

In essence, an effective strategy will divide your enterprise so that you are able to clearly understand the extent to which your “In-Scope” environment is protected by each domain.

The concept described in this chapter incorporates the core elements of ISACA’s Business Model for Information Security (BMIS),[^4] which has become an integral part of COBIT 2019.[^5]

The problem with developing a suitable strategy is that organizations often regard it as being unachievable or expensive. However, in truth, we have an obligation to ensure that our customers’ payment, financial, and personal data is adequately protected from misuse or loss. Your data processing operations are consistently at risk from opportunist attackers. This can be in the form of hackers, thieves, organized crime, or even that “trusted” employee.

Consequently, your strategy needs to be broad enough to mitigate the risks to an appropriate level while not be so aggressive as to appear to be “Boiling the Ocean.”

It’s all about balancing the risk!

By gaining an improved understanding of the four domains and their inter-relationships, you will be better able to understand the associated risks and to prioritize your efforts and to significantly reduce your potential for suffering a data breach.

[^4]: http://m.isaca.org/Knowledge-Center/BMIS/Documents/IntrotoBMIS.pdf
[^5]: www.isaca.org/COBIT/Pages/COBIT-2019-Publications-Resources.aspx

<!-- PDF p. 99 (book p. 75) -->

Remember, whether you are mitigating the external or internal attackers, they have some commonalities in the elements that drive them:

1. **Inquisitiveness**

You’ve put up some defenses, so they want to know what is behind your defenses (“They want a peek inside”) to see if there is anything that they can profit from.

- They don’t know whether your business is a viable target until they are able to take a look at what data lies behind your doors and windows.

2. **Challenge**

A fact of modern life is that the attackers seek to develop work-arounds to circumvent your defenses. Often these will be the exploitation of your “Human Firewall,” poor practices, or just looking at your web interfaces or networks through a different lens.

- Think about an e-Commerce shopping basket, where the web developer has made the interface look appealing and easy to use for the consumer. In testing, the developer confirmed that all the required functionality works as expected, with consumers being able to add the number of goods they wish to order and the advertised price – the price is automatically calculated.
  - Can that consumer change the number of goods ordered to a minus figure?
    - List price $100 × **–100** items = Payment card is refunded to the tune of **£10,000**.

Or

- has your developer confirmed that the list price cannot be manually changed?
  - List price $100, changed to **$1** × 100 items = Your business sells $10,000 of goods for just £100 – **1%** of the list price.

<!-- PDF p. 100 (book p. 76) -->

Note Neither of these examples are applicable to PCI DSS, as they do not impact the Confidentiality, Integrity, or Availability of the payment card data. However, they will impact your business!

3. **Reward**

For your attackers, the term “Reward” comes in two forms:

- **Financial**

The modern criminal is looking to monetarize any stolen data, either by using the stolen data to commit identity theft, payment card fraud, to purchase “Black Market” goods or to resell the stolen data to other criminals.

- **Kudos**

Having cleverly created work-arounds, your amateur hacker may only wish to brag to their peer groups at how clever they have been. To do this, they need to retrieve evidence of their deeds so will steal your data to prove what they have done. Frequently, this data remains available on the “Dark/Deep” Web for many months, until it becomes useful for a criminal.

- In 2013, Target was the victim of a piece of malware that was written by a 17-year-old Russian teenager.[^6] Yet, just two weeks later, a Mexican couple[^7] were caught crossing the US-Mexican border in possession of a large number of cloned payment cards related to the Target breach.
- In 2015, TalkTalk (a UK Internet Service Provider (ISP)) was hacked, resulting in **157,000** customer records being stolen. Four years later, **4500** of the customer details were discovered to be still available online.[^8]

[^6]: https://edition.cnn.com/2014/01/20/us/money-target-breach/index.html
[^7]: www.theguardian.com/world/2014/jan/21/texas-police-arrest-pair-linked-target-credit-card-breach-us-mexico-border
[^8]: www.silicon.co.uk/workspace/talktalk-breach-data-found-online-256555

<!-- PDF p. 101 (book p. 77) -->

All these drivers are driven by the attackers being presented with opportunities. Consequently, the belief that your business is not a credible target for an attacker is no longer a sensible approach, and if you are processing any personal data (especially payment card data), you are likely to become a victim without an effective defensive strategy.
