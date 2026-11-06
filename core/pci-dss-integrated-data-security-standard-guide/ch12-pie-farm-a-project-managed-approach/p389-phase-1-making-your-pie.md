---
title: "Phase 1 – Making your PIE"
book: pci-dss-integrated-data-security-standard-guide
chapter: 12
source_pages: "389-395"
format: source-text
---
# Phase 1 – Making your PIE
(Source: PDF pp. 389-395)

<!-- PDF p. 389 (book p. 368) -->

## Stage 1: Plan and Prepare

Much like any project, the importance of sufficient planning and preparation is essential for the success of the project. There were two old adages that were taught to me during my 22 years of service in the RAF Police:

**Figure 12-1.** *PIE FARM*

<!-- PDF p. 390 (book p. 369) -->

*“Failure to Plan is Planning to Fail!”*

*“***5 Ps:**

*Prior Preparation Prevents Poor Performance!”*

Never has the need for stage 1 than when trying to implement an integrated Cyber/ InfoSec strategy using a security controls framework. During this stage, it is essential that SMART (Specific, Measurable, Achievable, Realistic, and Timebound) objectives for the project are documented and agreed by the business. This becomes the foundation for the development of an effective Cyber/InfoSec strategy. This is the starting point where, as a team effort, the expectations of the project are established, resources allocated, funding confirmed, and senior management support obtained, for example:

- *Have you created a suitable Business Case for the PCI DSS project?*
- *As a Merchant, speaking with the Acquirer to confirm the merchant level and compliance validation expectations*
- *Confirming with the Acquirer whether they are happy to accept single SAQs for each payment channel*
  - *Waiting until both payment channels (MOTO and e-Commerce) are PCI DSS compliant shows you to be* **0% compliant***. However, fix a single payment channel and your business is regarded as being* **50% compliant***.*
- *Understanding your various payment channels and aligning them to their appropriate self-assessment questionnaire (SAQ)*
  - *E-commerce, fully outsourced to a PCI DSS-compliant third-party payment service provider.*
    - *SAQ A – Circa 22 controls*
  - *Mail order, telephone order (MOTO), in-house operation using a PCI DSS compliant third-party payment service provider. However, call recording is in place that electronically stores payment card data, making this ineligible for an SAQ C – 155 controls.*
    - *SAQ D – Circa 352 controls*

**Remember, it’s easier to roll a boulder down the hill than to try and struggle to push it up the hill.**

<!-- PDF p. 391 (book p. 370) -->

## Stage 2: Identify and Isolate

The next stage involves the identification of the differing payment channels, their data flows, inventory of connected supporting IT systems (across the network), business processes, personnel, and any outsourced services that are involved in the interaction with payment cardholder data.

*[Figure omitted]*

**Figure 12-2.** *Example Data Flow Diagram (DFD)*

<!-- PDF p. 392 (book p. 371) -->

- **This is the scope for PCI DSS!**

Having identified the scope, the next stage is to identify the applicable PCI DSS controls. Handily, the PCI Security Standards Council (PCI SSC) have provided some aides for this – in the form of the Self-Assessment Questionnaires (SAQs).

With the payment channels having been identified, in order to identify the most applicable controls, the next step is to review these payment channels against the “Before You Begin” section of the available SAQs.

- These are the PCI DSS controls that are deemed applicable to that type of payment channel. Where a payment channel does not fit into the shorter SAQs, the default is the SAQ D-Merchant or SAQ D-Service Provider (SP).

Note If you are a Service Provider that provides a service that aligns to one of the shorter SAQs, your default will still be the SAQ D-SP but with the applicable controls taken from the shorter SAQs, plus the Service Provider-specific controls.

Having identified the people, applicable controls, and outsourced services (per payment channel), it is recommended that these be documented against a PCI DSS controls RACI matrix:

- **R**esponsible (R)
  - Individual responsibilities are assigned against their particular PCI DSS controls.
- **A**ccountable (A)
  - Manager that is assigned as being accountable for ensuring that their department responsibilities have been actioned effectively.
- **C**onsulted (C)
  - Stakeholders that could be impacted by the actions of another.
- **I**nformed (I)
  - Key stakeholders who provide governance and oversight of the data privacy and security strategy.

<!-- PDF p. 393 (book p. 372) -->

*[Figure omitted]*

Now that the scope and the controls have been identified, the next step is to attempt to isolate the technologies, people, and processes as PCI DSS applies to any technologies, people, and processes directly involved in the processing, storage, or transmission of cardholder data or (more importantly) anything connected to these systems which could impact the cardholder data.

- **This is the Cardholder Data Environment (CDE) – In-scope!**
- **Think……**
  - **Red Zone** – In-scope!
  - **Black Zone** – Out-of-scope!

In addition to minimizing the scope for PCI DSS, effectively layered networks and systems should help isolate the in-scope from the out-of-scope environments. This is essential to the Defense, Delay, Disruption, and Deterrence of a “wannabe” attacker while helping with the Detection of malicious activities.

5 Ds

- **Defend**
- **Delay**
- **Disrupt**
- **Deter**
- **Detect**

**Figure 12-3.** *RACI Chart*

<!-- PDF p. 394 (book p. 373) -->

*For example:*

- *Identify all the personnel, assets, and documentation needed for each payment channel. Document these within asset inventories, network, and data flow diagrams to identify any connected environments that would need to be isolated to reduce the potential impact and scope.*

## Stage 3: Engage, Explain, and Evaluate

Unlike popular belief, the ongoing maintenance of secure operations cannot be the responsibility of a handful of employees and takes teamwork. Therefore, following on from stage 2, having identified the key personnel involved in supporting the CDE, this stage starts by engaging with these stakeholders and explaining the controls that apply to their supporting job functions and the implications of their job against their applicable PCI DSS controls.

Having identified the gaps between your current state and your desired state will help provide you with some indicative costs associated with your mitigation options, which could be applied as part of your fixing step.

Next comes the evaluation of the status of any in-place systems, processes, procedures, and policies. This will readily identify any gaps or areas needing improvements and provide the foundation and priorities needed for Phase 2, for example:

- *Carry out a review of each payment channel against their applicable controls, ensuring that any processes are evaluated based upon their maturity levels.*[^1]

[^1]: https://cmmiinstitute.com/learning/appraisals/levels

<!-- PDF p. 395 (book p. 374) -->

*[Figure omitted]*

Note I could have called this phase “Gap Assessment,” but being a Pescatarian (although mostly leaning toward a “Plant-Based” diet, nowadays), I prefer the Acronym “PIE FARM” vs. the alternative “PIG FARM” but I shall leave that for you to choose your preference.
