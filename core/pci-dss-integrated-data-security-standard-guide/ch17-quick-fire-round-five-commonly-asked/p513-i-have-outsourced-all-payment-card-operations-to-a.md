---
title: "I have outsourced all payment card operations to a third-party supplier, so as neither my business systems nor personnel interact with any cardholder data, surely, I do not need to validate my compliance?"
book: pci-dss-integrated-data-security-standard-guide
chapter: 17
source_pages: "513-514"
format: source-text
---
# I have outsourced all payment card operations to a third-party supplier, so as neither my business systems nor personnel interact with any cardholder data, surely, I do not need to validate my compliance?
(Source: PDF pp. 513-514)

<!-- PDF p. 513 (book p. 495) -->

*Unfortunately, if you are a business that provides goods or services in exchange for payment through a payment card, you are still accountable for ensuring that your third- party suppliers are carrying out these support services in accordance with PCI DSS.*

*The most difficult part of transferring your risk and responsibilities to a third-party supplier (a.k.a. Service Provider*[^10]*/Merchant Agent*[^11]*) is ensuring that the services you are paying for cover the full extent of your PCI DSS obligations.*

*It is extremely likely that your chosen supplier will be in the business of providing PCI DSS support services to numerous clienteles and the services offered could be wide- ranging. Consequently, you need to ensure that you fully understand the services being supplied by all your third parties and that your contracts legally oblige the supplier to fulfill their security requirements.*

*This concept is very similar to that seen in Article 29*[^12] *of the European Union’s General Data Protection Regulation (EU GDPR). In the event of a breach, both the Processor (Third Party) and the Controller can be subject to an administrative fine (Article 83*[^13]*).*

*Consequently, as part of your PCI DSS validation, you need to*

- *Identify all your suppliers.*
- *Review your contracts to ensure that they are still appropriate.*
- *Ask for evidence against a sample of the controls that they are responsible for.*

[^10]: https://globalrisk.mastercard.com/wp-content/uploads/2018/06/Service-Provider-Categories-and-PCI.pdf
[^11]: www.visa.co.uk/dam/VCOM/regional/ve/unitedkingdom/PDF/risk/ve-merchant-agent-list-june-2019.pdf
[^12]: www.privacy-regulation.eu/en/article-29-processing-under-the-authority-of-the-controller-or-processor-GDPR.htm
[^13]: www.privacy-regulation.eu/en/article-83-general-conditions-for-imposing-administrative-fines-GDPR.htm#4

<!-- PDF p. 514 (book p. 496) -->

- *Review their compliance status by requesting a copy of their latest attestation on compliance (AoC).*
- *Collate all the outsourced PCI DSS controls into a responsible, accountable, consulted, and informed (RACI) matrix – this will help you identify and confirm that all the PCI DSS controls are being managed by your suppliers.*
