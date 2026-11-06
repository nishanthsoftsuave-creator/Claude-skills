---
id: C10-013
title: Feedback Limitations
source_pages: "921-924"
chapter: 10
concepts: [feedback-limitations, leniency-bias, position-bias, recency-bias, degenerate-feedback-loop, sycophancy, exposure-bias, randomness]
related: [C10-012, C10-014]
time_sensitive: false
---
# Feedback Limitations
(Source: PDF pp. 921-924, plus tail PDF p. 925 up to the "Summary" heading. The first two lines of PDF p. 921 finish the previous section's sentence on private likes on X: hiding likes could leave users confused about why certain tweets appear in their feeds. That point is developed in C10-012.)

## What the section covers
User feedback is valuable but "isn't a free lunch" (PDF p. 921). This section lists its limitations: several biases in how people give feedback, and degenerate feedback loops that arise when feedback is used to change the model.

## Biases
Like any data, feedback is biased. You must understand the biases of your own application and design the feedback system around them. The book offers examples to show what to watch for (PDF p. 921).

### Leniency bias
People tend to rate items more positively than deserved, often to avoid conflict, because they feel obliged to be nice, or because it is the easiest path. Scenario: you are in a hurry, an app asks you to rate a transaction, you are unhappy, but a negative rating would trigger a request for reasons, so you pick positive to finish. This is why you should not make people do extra work to give feedback (PDF p. 921).

On a five-star scale, four and five stars nominally mean a good experience, but users often feel pushed to give five and reserve four for when something went wrong. Per Uber, in 2015 the average driver rating was 4.8, and scores below 4.6 put drivers at risk of deactivation (PDF p. 922).

The bias is not necessarily a dealbreaker: Uber wants to separate good drivers from bad, and even with the bias the system seems to do that. To detect the bias, look at the distribution of ratings (PDF p. 922). For more granular feedback, remove the strong negative connotation of low numbers. Instead of 1 to 5, offer verbal options, such as "Great ride. Great driver.", "Pretty good.", "Nothing to complain about but nothing stellar either.", "Could've been better." and "Don't match me with this driver again." (PDF p. 922).

### Randomness
Users sometimes give random feedback, not from malice but from lack of motivation to be thoughtful. When two long responses are shown for comparison, a user may not read both and click one at random. In Midjourney, users may also pick an image at random to generate variations (PDF p. 923).

### Position bias
The position of an option affects how it is perceived; users are generally more likely to click the first suggestion than the second, so a click on the first does not necessarily mean it is good. Mitigations: randomly vary suggestion positions, or build a model that computes a suggestion's true success rate given its position (PDF p. 923).

### Preference bias
Other biases discussed earlier in the book also apply. People may favor the longer response in a side-by-side comparison even when it is less accurate, because length is easier to notice than inaccuracies. Recency bias is another: people tend to favor the answer they saw last when comparing two (PDF p. 923).

The takeaway is to inspect your feedback to uncover its biases, so you interpret it correctly and avoid misleading product decisions (PDF p. 924).

## Degenerate feedback loop
Feedback is incomplete: you only receive feedback on what you show users (PDF p. 924). When feedback is used to modify model behavior, a degenerate feedback loop can arise: the model's predictions influence the feedback, which in turn shapes the next model iteration and amplifies the initial biases (PDF p. 924).

Video recommendation example (PDF p. 924): higher-ranked videos appear first and collect more clicks, which reinforces the system's belief that they are best. Videos A and B may start nearly equal, but A ranked slightly higher, got more clicks and kept being boosted until its rank soared and B was left behind. This is why popular videos stay popular and new ones struggle. The problem is known as "exposure bias", "popularity bias" or "filter bubbles" and is well studied.

The loop can also shift the product's focus and user base. Cat example (PDF pp. 924-925): a few users say they like cat photos; the system generates more cats; this draws cat lovers, who give more positive feedback, so the system produces still more cats until the application becomes a "cat haven". The same mechanism can amplify other biases, such as racism, sexism and preference for explicit content (PDF p. 925).

### Sycophancy
Acting on user feedback can make a conversational agent, in the author's words, a kind of liar. Several studies show that training a model on user feedback can teach it to give users what it thinks they want, even when not the most accurate or beneficial (Stray, 2023). Sharma et al. (2023) show models trained on human feedback tend toward sycophancy: they are more likely to produce answers that match the user's own view (PDF p. 925).

## Conclusion of the section
User feedback is crucial for improving user experience, but used indiscriminately it can perpetuate biases and "destroy your product" (PDF p. 925). Before incorporating feedback, understand its limitations and potential impact. The chapter summary follows on the same page and belongs to C10-014.

## When and how to apply
INTERPRETATION: Practical checks implied by the section: plot the rating distribution to spot leniency; randomize or position-correct suggestion order; keep feedback actions low-effort; treat random clicks and length preference as noise; and guard against loops by watching what the system shows, not just what users click.

## Relations
The mechanisms for collecting feedback are in C10-012; the chapter wrap-up is C10-014.
