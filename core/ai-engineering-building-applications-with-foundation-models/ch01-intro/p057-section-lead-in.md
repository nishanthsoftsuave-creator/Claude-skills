---
id: C01-005
title: Foundation Model Use Cases (Lead-in)
source_pages: "57-63"
chapter: 1
concepts: [use-cases, use-case-taxonomy, occupation-exposure, enterprise-vs-consumer, internal-vs-external-applications, close-ended-tasks, open-source-applications]
related: [C01-004, C01-006, C01-007, C01-008, C01-009]
time_sensitive: true
---
# Foundation Model Use Cases (Lead-in)
(Source: PDF pp. 57-63)

## What the section covers
The text that opens the use-case section before the first named subsection (Coding): how use cases are categorized by different organizations, research on which occupations are exposed to AI, the author's own eight-category survey of enterprise and consumer applications, and the observation that enterprises prefer lower-risk applications.

## Purpose and framing
- The section is for readers who want inspiration. Readers who already have an application in mind can jump ahead to the planning section (PDF p. 57).
- The potential applications seem endless ("there's probably an AI for that"), so listing every one is impossible. Even categorizing them is hard because surveys use different schemes (PDF p. 57).

## Categorization schemes from others (PDF pp. 57-58)
- AWS groups enterprise generative AI use cases into three buckets: customer experience, employee productivity, and process optimization.
- A 2024 O'Reilly survey used eight categories: programming, data analysis, customer support, marketing copy, other copy, research, web design, and art.
- Deloitte categorizes by value capture: cost reduction, process efficiency, growth, and accelerating innovation.
- Gartner adds business continuity, meaning the organization might go out of business if it does not adopt generative AI. Of 2,500 executives Gartner surveyed in 2023, 7% cited business continuity as their motivation.

## Which occupations are exposed to AI (PDF pp. 58-59)
- Eloundou et al. (2023) studied exposure of occupations. A task is "exposed" if AI and AI-powered software can cut the time to complete it by at least 50%. An occupation with 80% exposure has 80% of its tasks exposed (PDF p. 58).
- Occupations at or near 100% exposure include interpreters and translators, tax preparers, web designers and writers. Occupations with no exposure include cooks, stonemasons and athletes. The author says the study gives a good idea of what AI is suited for (PDF p. 58).
- Table 1-2 (human annotations; alpha means exposure to AI models directly, beta and zeta mean exposure to AI-powered software). Highest exposure per group (PDF p. 59):
  - Human alpha: interpreters and translators 76.5%; survey researchers 75.0%; poets, lyricists and creative writers 68.8%; animal scientists 66.7%; public relations specialists 66.7%.
  - Human beta: survey researchers 84.4%; writers and authors 82.5%; interpreters and translators 82.4%; public relations specialists 80.6%; animal scientists 77.8%.
  - Human zeta: mathematicians, tax preparers, financial quantitative analysts, writers and authors, and web and digital interface designers are all 100%. Humans labeled 15 occupations "fully exposed".

## The author's own survey and categories (PDF pp. 60-62)
- Method: for enterprise use cases the author interviewed 50 companies about AI strategy and read over 100 case studies. For consumer applications the author examined 205 open source AI applications with at least 500 GitHub stars. Applications were sorted into eight groups (PDF p. 60).
- The list is meant as a reference; Chapters 2 (building foundation models) and 3 (evaluating them) help form a better view of what use cases models can and should serve (PDF p. 60).
- Table 1-3 (consumer examples, then enterprise examples) (PDF pp. 61-62):
  - Coding: coding / coding.
  - Image and video production: photo and video editing, design / presentation, ad generation.
  - Writing: email, social media and blog posts / copywriting and SEO, reports, memos, design docs.
  - Education: tutoring, essay grading / employee onboarding, employee upskill training.
  - Conversational bots: general chatbot, AI companion / customer support, product copilots.
  - Information aggregation: summarization, talk-to-your-docs / summarization, market research.
  - Data organization: image search, Memex / knowledge management, document processing.
  - Workflow automation: travel planning, event planning / data extraction, entry and annotation, lead generation.
- Because foundation models are general, one application can fall in several categories. Examples: a bot can offer companionship and aggregate information; an app can extract structured data from a PDF and also answer questions about it (PDF p. 62).
- Figure 1-7 shows the split among the 205 open source apps (read from the rendered page): coding 30.4%, conversational bots 26.5%, information aggregation 12.7%, image and video production 12.7%, workflow automation 11.3%, writing 3.4%, education 1.5%, data organization 1.5% (PDF pp. 62-63). The small shares for education, data organization and writing do not mean these are unpopular; they mean such applications are mostly not open source, since builders may see them as better suited to enterprise (PDF p. 62).

## Enterprise preference for lower risk (PDF p. 63)
- Enterprises generally prefer lower-risk applications. A 2024 a16z Growth report found companies deploy internal-facing applications (for example internal knowledge management) faster than external-facing ones (for example customer support chatbots) (PDF p. 63).
- Figure 1-8 is referenced here but printed at the top of the next page; its contents are described in the Coding module (C01-006).
- Reason: internal applications build a company's AI engineering expertise while limiting risks around data privacy, compliance and catastrophic failure (PDF p. 63).
- Similarly, although foundation models are open-ended, many applications built on them are still close-ended, such as classification. Classification is easier to evaluate, so its risks are easier to estimate (PDF p. 63).

## Closing note of the lead-in (continues on the next page)
The lead-in's closing paragraph is printed on the next page, just above the Coding heading (so it is described here without a page cite). The author says that even after seeing hundreds of AI applications, new ones still surprise them every week. Few people in the early internet days foresaw that social media would become its dominant use case, and as we learn to get the most from AI, the use case that eventually dominates might likewise be a surprise. The author hopes it will be a good one.

## When and how to apply
INTERPRETATION: when choosing a first project, the book's evidence points toward internal-facing, close-ended applications because they are faster to deploy and easier to evaluate.

## Time-sensitive statements
Survey figures (Gartner 2023, O'Reilly 2024, a16z 2024), the 205-repository snapshot, and the exposure percentages are dated snapshots.

## Relations
Follows the AI engineering rise (C01-004). The eight categories are elaborated one by one in C01-006 (coding), C01-007 (image and video), C01-008 (writing) and C01-009 (education).
