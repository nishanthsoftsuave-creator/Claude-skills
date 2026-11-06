---
title: "Chapter 5: The Importance of Risk Management (opening)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 5
source_pages: "136-143"
format: source-text
---
# Chapter 5: The Importance of Risk Management (opening)
(Source: PDF pp. 136-143)

<!-- PDF p. 136 (book p. 113) -->

*[Figure omitted]*

Bearing in mind that you cannot completely eliminate risk *(especially when the “Human Factor” and Supplier Management is involved),* the importance of risk management, within your PCI DSS compliance program, becomes increasingly relevant to your business.

**Figure 5-1.** *Risk Assessment Practice*

<!-- PDF p. 137 (book p. 114) -->

This is probably the most misunderstood aspect of most Cyber/InfoSec strategies, especially within the PCI DSS integrated framework.

Why is this? In traditional control frameworks, such as the ISO/IEC 27001:2013 controls framework, the application of Annex A controls is applied to mitigate identified risks. However, within the Payment Card Industry Data Security Standard (PCI DSS) integrated controls framework, there is an understanding that the catalogue of controls is all that is required to ensure that the payment card processes are secure.

Unfortunately, this is not correct. The Payment Card Industry Security Standards Council (PCI SSC) have provided you with a catalogue of baseline security controls, which under the current version includes the control requirement for carrying out annual risk assessments. Employing the NIST SP800-30, r1,[^1] principles, the annual risk assessment should include the following steps:

1. **Categorize**

In addition to the baseline PCI DSS security controls, identify any additional threats, events, vulnerabilities, or predisposed conditions that are not being mitigated, *for example:*

*Man-in-the-Middle Magecart attacks*[^2] *for an SAQ A eligible e-commerce merchant. In this style of attack, the attacker hijacks the customer journey from the out-of-scope web page, prior to being redirected to the third-party payment service provider’s (PSP’s) secure card payment interface. As a result, the attacker is able to carry out clandestine harvesting of the customer’s card payment details, without needing to compromise the in-scope environment.*

2. **Select**

Having identified potential additional risks, not covered by the existing PCI DSS controls, identify potential additional security controls for your organizational information systems and environments of operation. This should include a number of options to help mitigate any identified risks/threats, *for example:* <!-- PDF p. 138 (book p. 115) --> *In the case of the Magecart attacks*

[^1]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf
[^2]: www.hornetsecurity.com/en/security-information/formjacking/

- *Carrying out web application testing for JavaScript/Code injection vulnerabilities for the out-of-scope web pages, along the customer’s journey*
- *Procuring the services of a third-party service to monitor the entire external web digital footprint (e.g., Cequence Security,*[^3] *Cyber Rescue Alliance Security Scorecard*[^4]*)*
- *Bringing the out-of-scope web pages into scope (potential to impact)*

3. **Implement**

Additional control measures are required to help mitigate against these identified risks, *for example:*

*In the case of the Magecart-style attacks, ensuring that any such vulnerabilities on the out-of-scope web pages are remediated to ensure the integrity of the redirection process cannot be undermined*

4. **Assess**

The effectiveness of the identified, additional, mitigation controls are assessed and documented, *for example:*

*In the aforementioned attack vector, suggested mitigation controls help to demonstrate the inherent risk scores (before mitigation) and residual risk scores (post mitigation) – Impact × Probability.*

5. **Authorize**

Any additional risk mitigation activities should be aligned to the business’s risk appetite. Therefore, the results of any risk assessment should be documented allowing the business to make an informed choice on the best course of action for their business, *for example:*

*In the case of a “Formjacking*[^5]*” risk, as per the Magecart threat, your appropriate business’s risk owner should then be responsible for choosing.*

[^3]: www.cequence.ai/
[^4]: https://securityscorecard.com/
[^5]: https://hackersonlineclub.com/formjacking/

<!-- PDF p. 139 (book p. 116) -->

6. **Monitor**

By its very nature, the payment card information systems threats are dynamic by their very nature and need to be subject to continual monitoring to ensure

- The security controls remain effective
- Any changes to the environment or supporting system do not impact
- Compliance with the appropriate legal, regulatory, policies, and procedures remains extant

*For example, in relation to the “Formjacking” risk, you need to ensure that the chosen risk mitigation approach remains effective and aligned with your business’s risk appetite criteria.*

In addition to identifying and assessing any risks that are not being mitigated by your PCI DSS compliance program, you need to carry out risk assessments against your PCI DSS controls. Remember that these are the minimum baseline security controls, but they may not be aligned with your business’s risk appetite levels. Consequently, you may choose to enhance the existing controls to ensure that they are more appropriate to your business expectations.

As parents, we understand and appreciate the importance of the risk assessment and risk management process and ensure that these concepts are articulated to our children. For example, what parent does not educate their children how to safely cross a road, through the application of risk assessment and mitigation principles?

- **Threat**
  - Serious injury or death
- **Risk**
  - Being hit by a large vehicle or a vehicle travelling at speed
- **Control**
  - Safely cross the road.

<!-- PDF p. 140 (book p. 117) -->

- **Method**
  - Choose the most appropriate option.
- **Performance Standard and Specifications**
  - Green Cross Code[^6]
    - THINK!
    - STOP!
    - USE YOUR EYES AND EARS!
    - WAIT UNTIL IT IS SAFE TO CROSS!
    - LOOK AND LISTEN!
    - ARRIVE ALIVE!
- **Risk Assessment**
  - Assess any additional impact and probability factors for each available option, for example:
    - Lighting conditions
    - Weather conditions
    - Road surface
    - Appropriate footwear
    - Road width
    - Speed limit
    - Volume of traffic
    - Type of traffic
    - Crossing location
    - Obstructions
    - Injuries

[^6]: www.sptraininguk.com/green-cross-code/

<!-- PDF p. 141 (book p. 118) -->

*[Figure omitted]*

However, having taught them the safe way of crossing the road, parents encourage the children to seek alternative/safer options that the child may feel more comfortable with *(e.g., A bridge, Pedestrian crossing, choosing a safer crossing point, etc.)*.

Consequently, much like parents/schools are teaching children, your business needs to consider the pros and cons of the baseline PCI DSS security controls and to consider whether based upon the specific threats to your payment card processing systems and environments and to not be solely reliant on the PCI DSS controls being appropriate defensive measures, for example:

1. Let’s have a look at the growing threat to e-Commerce business operations from the Magecart Group.[^7] You have transferred the

**Figure 5-2.** *Risk Assessment Cycle*

[^7]: www.riskiq.com/research/inside-magecart/?utm_campaign=search_magecart&utm_source= google&utm_medium=cpc&utm_content=inside_magecart&gclid=CjwKCAiAgqDxBRBTEiwA59eEN4 PiqV_SVdvzVcE8ak-AtxYzE1q2HdBTYv6pB-mNXof9DLZGZCZdEBoCwjwQAvD_BwE

<!-- PDF p. 142 (book p. 119) -->

responsibility of processing your customers’ payment card data to a PCI DSS compliant third-party service provider, reducing your risk *(through the use of a crossing supervisor/crossing patrol officer, lollipop man/lady)* and becoming eligible for the completion of an SAQ A[^8] (circa 22 controls). However, this risk assessment only deals with the risk of “crossing the road” and does not make any considerations of the dangers associated with being vulnerable to the dangers that could occur while you are stood on the sidewalk/ footpath *(e.g., runaway vehicle)*.

In the case of the Magecart Group, they will seek to exploit vulnerabilities within the out-of-scope web pages, within your customers’ journey to the payment interface, to carry out a man- in- the-middle attack.

2. Your business takes the decision to use their customers’ primary account numbers for the unique identifier for the customers’ accounts.

*What are the implications for this?*

- *Printed on all paper correspondence?*
- *Spoken during all telephone interactions?*
- *Used to validate customers for online account resets?*

[^8]: www.pcisecuritystandards.org/documents/PCI-DSS-v3_2_1-SAQ-A.pdf?agreement=true& time=1579685825026

<!-- PDF p. 143 (book p. 120) -->

*[Figure omitted]*
