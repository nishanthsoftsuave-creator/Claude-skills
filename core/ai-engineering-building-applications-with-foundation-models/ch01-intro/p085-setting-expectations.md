---
id: C01-016
title: Setting Expectations
source_pages: "85"
chapter: 1
concepts: [success-metrics, business-metrics, usefulness-threshold, latency-metrics, ttft, tpot, cost-per-inference, customer-satisfaction]
related: [C01-015, C01-017, C01-018]
time_sensitive: false
---
# Setting Expectations
(Source: PDF p. 85, continuing on the tail page PDF p. 86)

## What the section covers
After deciding to build, define what success looks like and how it will be measured. The top of PDF p. 85 finishes the defensibility discussion from C01-015; the "Milestone Planning" heading at the bottom of p. 86 begins C01-017.

## End of the defensibility discussion
Many successful companies began with products that could have been features of bigger products: Calendly could have been a feature of Google Calendar, Mailchimp of Gmail, Photoroom of Google Photos. Many startups eventually overtake larger competitors by starting with a feature those competitors overlooked (PDF p. 85).

## Business metrics first
The most important metric is the impact on the business. For a customer support chatbot, candidate business metrics are (PDF p. 85):
- what percentage of customer messages to automate;
- how many more messages the bot lets you handle;
- how much faster you can respond;
- how much human labor it saves.
Answering more messages does not make users happy, so customer satisfaction and customer feedback must also be tracked. The book points to its "User Feedback" discussion for designing a feedback system (PDF p. 85).

## Usefulness threshold
To keep a product from reaching customers before it is ready, set a clear usefulness threshold: how good it must be to be useful. It can combine groups of metrics (PDF p. 86):
- Quality metrics for response quality.
- Latency metrics: TTFT (time to first token), TPOT (time per output token) and total latency. Acceptable latency depends on the use case. If humans currently handle every request with a median response time of an hour, anything faster may be good enough (PDF p. 86).
- Cost metrics: cost per inference request (PDF p. 86).
- Other metrics such as interpretability and fairness (PDF p. 86).
If you are not yet sure which metrics to use, the author says not to worry, as the rest of the book covers many of them (PDF p. 86).

## Relations
Follows use case evaluation (C01-015); milestone planning (C01-017) and maintenance (C01-018) follow.
