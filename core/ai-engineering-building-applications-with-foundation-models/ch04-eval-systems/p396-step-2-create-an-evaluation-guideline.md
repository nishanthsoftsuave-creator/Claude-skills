---
id: C04-012
title: Step 2. Create an Evaluation Guideline
source_pages: "396-399"
chapter: 4
concepts: [evaluation-guideline, evaluation-criteria, scoring-rubric, business-metrics, usefulness-threshold, stickiness-metrics, engagement-metrics]
related: [C04-011, C04-013, C04-014]
time_sensitive: false
---
# Step 2. Create an Evaluation Guideline
(Source: PDF pp. 396-399; the section's closing paragraphs on usefulness threshold and business metrics run onto PDF p. 400, whose lines below the Step 3 heading belong to C04-013)

## What the section covers
The second step of designing an evaluation pipeline: writing a clear guideline that says what good and bad outputs look like. It covers defining the evaluation criteria, building scoring rubrics with examples, and tying evaluation metrics to business metrics. The top of PDF p. 396 is the end of the preceding section's twenty-questions style example (Bob guesses "apple" and the task completes), which is not part of this step.

## Why it matters
- The book calls a clear evaluation guideline the most important step of the pipeline. An ambiguous guideline produces ambiguous, possibly misleading scores. If you do not know what bad responses look like, you cannot catch them (PDF p. 396).
- The guideline is described as "the backbone of a reliable evaluation pipeline" (PDF p. 398), and it can be reused later as annotation guidance for training data (Chapter 8) (PDF pp. 398-399).

## Meaning and how it works

### Define what the application should not do, too
The guideline must cover what the application should and should not do. Example: a customer support chatbot may be asked about something unrelated to the product, such as an upcoming election. If it should not answer, you must define which inputs are out of scope, how to detect them, and how the application should respond (PDF p. 397).

### Define evaluation criteria
- The hardest part of evaluation is often not judging whether an output is good but deciding what "good" means. LinkedIn, reflecting on a year of deploying generative AI applications, said the first hurdle was writing the evaluation guideline (PDF p. 397).
- A correct response is not always a good one. In LinkedIn's AI-powered Job Assessment application, "You are a terrible fit" may be correct but unhelpful. A good response explains the gap between the job requirements and the candidate's background and what the candidate could do to close it (PDF p. 397).
- Think about what makes a good response before building. LangChain's State of AI 2023 found users applied on average 2.3 different kinds of feedback (criteria) to evaluate an application (PDF p. 397).
- Example criteria set for a customer support application (PDF pp. 397-398): (1) relevance, meaning the response is relevant to the user's query; (2) factual consistency, meaning it is consistent with the context; (3) safety, meaning it is not toxic.
- To arrive at criteria, experiment with test queries, ideally real user queries. For each, produce several responses (by hand or with AI models) and decide which are good or bad (PDF p. 398).

### Create scoring rubrics with examples
- For each criterion pick a scoring system: binary (0 and 1), 1 to 5, between 0 and 1, or other. For consistency with a context, some teams score 0 for inconsistent and 1 for consistent; others use three values: -1 for contradiction, 1 for entailment, 0 for neutral. The choice depends on your data and needs (PDF p. 398).
- Build a rubric on that scoring system with examples: what does a response scoring 1 look like, and why does it deserve 1? (PDF p. 398)
- Validate the rubric with humans such as yourself, coworkers or friends. If they find it hard to follow, refine it until it is unambiguous. This can take much back and forth but is necessary (PDF p. 398).

### Tie evaluation metrics to business metrics
- An application must serve a business goal, so its metrics should be read in light of the business problem (PDF p. 399).
- Example: a chatbot with 80% factual consistency. What does that mean for the business? It may be unusable for billing questions but fine for product recommendations or general feedback. Ideally you map metric levels to business outcomes, for instance: 80% factual consistency lets you automate 30% of support requests; 90% lets you automate 50%; 98% lets you automate 90% (PDF p. 399).
- Knowing the business payoff of improving a metric helps planning and gives confidence to invest resources in it (PDF p. 399).
- Also determine a usefulness threshold: the minimum scores for the application to be useful. For example, factual consistency must be at least 50%, below which the chatbot is unusable even for general customer requests (PDF p. 400).

### Know your business metrics first
- Before developing AI evaluation metrics, understand the business metrics being targeted (PDF p. 400).
- Many applications focus on stickiness metrics: daily, weekly or monthly active users (DAU, WAU, MAU). Others favor engagement metrics, such as conversations started per month or time per visit; longer stays mean users are less likely to leave (PDF p. 400).
- Choosing among these resembles balancing profit against social responsibility. Pushing stickiness and engagement can raise revenue but may lead a product toward addictive features or extreme content that harms users (PDF p. 400).

## When and how to apply
Write the guideline before building: criteria from real test queries, a rubric per criterion with examples, human validation of the rubric, then a mapping from metric levels to business outcomes and a minimum usefulness threshold.

## Relations
Follows Step 1 (C04-011) and feeds Step 3, selecting evaluation methods and data (C04-013); the rubric also feeds annotation for training data in Chapter 8. The chapter wrap-up is C04-014.
