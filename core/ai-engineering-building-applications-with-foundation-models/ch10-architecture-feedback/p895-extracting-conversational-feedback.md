---
id: C10-011
title: Extracting Conversational Feedback
source_pages: "895-906"
chapter: 10
concepts: [explicit-feedback, implicit-feedback, conversational-feedback, natural-language-feedback, early-termination, error-correction, user-edits, preference-data, complaints, sentiment, regeneration, conversation-length]
related: [C10-010, C10-009, C10-008]
time_sensitive: false
---
# Extracting Conversational Feedback
(Source: PDF pp. 895-906. The discussion of explicit versus implicit feedback trade-offs begins on p. 906 and its last sentence, about a friend who shares useful conversations, continues onto the next page.)

## What the section covers
How to obtain feedback signals from conversational AI applications: the explicit/implicit distinction, what users' messages and actions reveal, the catalogue of natural language signals (early termination, error correction, edits, complaints, sentiment, refusals), other action-based signals (regeneration, organizing conversations, length, diversity), and the trade-offs between explicit and implicit feedback.

## Meaning
- **Explicit feedback**: information users give in answer to a direct request in the app, such as thumbs up/down, upvote/downvote, star rating, or a yes/no reply to "Did we solve your problem?". It is fairly standard across applications because there are only so many ways to ask whether someone likes something, so it is better understood (PDF p. 895).
- **Implicit feedback**: information inferred from what users do, for example buying a recommended product implies a good recommendation. What counts is highly application-dependent, since it depends on the actions the app offers. Foundation models open new applications and therefore many new kinds of implicit feedback (PDF p. 895).
- The conversational interface makes giving feedback easier: users reward good behavior and correct mistakes as in everyday dialogue. The language a user uses to direct the AI can carry feedback about both the app's performance and the user's preferences (PDF p. 895).
- Worked example (PDF pp. 895-897): a user asks an assistant to find a three-night Sydney hotel. It offers three options: Historic Rocks Boutique Hotel (The Rocks, about $400 a night, charming streets near sights), Stylish Surry Hills House Hotel (Surry Hills, about $200, trendy with cafes and galleries) and Chill Bondi Beachside Hotel (Bondi Beach, about $300, beachside). A reply like "Yes book me the one close to galleries" reveals an interest in art, while "Is there nothing under $200?" reveals price consciousness and suggests the assistant has not understood the user yet.

## Why it matters
Feedback extracted from conversations can serve three uses (PDF p. 897):
- Evaluation: derive metrics for monitoring the application.
- Development: train future models or steer their development.
- Personalization: tailor the application to each user.

Because the feedback is blended into ordinary conversation it is hard to extract. Intuition about conversational cues can yield an initial list of signals, but rigorous data analysis and user studies are needed to truly understand them (PDF p. 897).

Background: conversational feedback was an active research area well before ChatGPT. The reinforcement learning community has tried since the late 2010s to learn from natural language feedback (the book cites Fu et al. 2019; Goyal et al. 2019; Zhou and Small 2020; Sumers et al. 2020), and early conversational products such as Amazon Alexa, Spotify's voice control and Yahoo! Voice studied it too (PDF pp. 897-898).

## How it works: natural language feedback
Feedback taken from message content is called natural language feedback. The book says it is useful to track these signals in production to monitor performance (PDF p. 898).

**Early termination.** The user cuts the response short: stops generation midway, exits the app, tells a voice assistant to stop, or simply leaves the agent hanging without answering which option to proceed with. Likely the conversation is going badly (PDF p. 898).

**Error correction.**
- A follow-up beginning with "No, ..." or "I meant, ..." suggests the response missed the mark (PDF p. 898).
- Users may rephrase. Figure 10-12 (PDF p. 899) shows a chat in which the user asks for "weather in mission bay today"; the assistant (after searching 3 sites) answers about Mission Bay, San Francisco, with temperatures of 56 to 68 F. The user then rephrases with clarifying information, "mission bay san diego", and the assistant (searching 4 sites) answers for Mission Bay, San Diego, at 68 to 74 F. In the figure the first assistant answer visibly breaks off mid-sentence ("Winds are expected"), which is the early termination. The caption's point: because the user both ended generation early and rephrased, one can infer the model misunderstood the original intent. Rephrase attempts can be detected with heuristics or ML models (PDF pp. 898-899).
- Users can point out specific things the model should have done differently, such as "Bill is the suspect, not the victim" after a story summary confuses a character; the model should take this and revise (PDF p. 899).
- Action-correcting feedback is especially common with agents, where users nudge them toward more actions, for instance in a market analysis of company XYZ: "You should also check XYZ GitHub page" or "Check the CEO's X profile" (PDF pp. 899-900).
- Users may ask the model to correct itself with confirmation requests such as "Are you sure?", "Check again" or "Show me the sources". This does not necessarily mean the answer was wrong; it may mean the answer lacked detail the user wanted, or reflect general distrust of the model (PDF p. 900).
- **Edits.** Some applications let users edit responses directly. If a user edits generated code, that is a very strong signal the code was not quite right. Edits are also a valuable source of preference data: preference data, typically (query, winning response, losing response), aligns a model with human preference, and each edit yields one example in which the original output is the losing response and the edited version is the winning one (PDF p. 900).

**Complaints.** Users often just complain without trying to fix anything: the answer is wrong, irrelevant, toxic, lengthy, lacking detail, or just bad (PDF p. 900). Table 10-1 (PDF pp. 901-903) lists eight groups obtained by automatically clustering natural language feedback in the FITS (Feedback for Interactive Talk & Search) dataset (Xu et al., 2022). Counts and percentages as printed:

| Group | Feedback type | Count | Percent |
|---|---|---|---|
| 1 | Clarify their demand again | 3702 | 26 (integer part; clipped) |
| 2 | Complain that the bot does not answer the question, gives irrelevant information, or tells the user to find the answer themselves | 2260 | 16 (integer part; clipped) |
| 3 | Point out specific search results that can answer the question | 2255 | 16 (integer part; clipped) |
| 4 | Suggest that the bot should use the search results | 2130 | 15 (integer part; clipped) |
| 5 | State that the answer is factually incorrect or not grounded in the search results | 1572 | 11 (integer part; clipped) |
| 6 | Point out that the answer is not specific, accurate, complete or detailed | 1309 | 9 (decimal clipped) |
| 7 | Point out that the bot is not confident and always opens with "I am not sure" or "I don't know" | 582 | 4 (decimal clipped) |
| 8 | Complain about repetition or rudeness in bot responses | 137 | 0 (decimal clipped) |

UNVERIFIED: the percentage column is cut off at the right edge of the rendered pages in the PDF (the table sits in a horizontally scrolling frame), so only the integer part of percentages for groups 1-8 is legible; the printed values for groups 6-8 show a trailing decimal point whose digit is lost. The table caption is also clipped after "Resu..." (it credits a result to a 2023 source). Rendered at higher resolution, the percentage column is still cut at the right edge for every row (the last visible glyph of groups 1-5 is partly sliced), so for all eight groups only the integer part is certain and any decimals are unknown.

The book's point: knowing how the bot fails users is crucial to improving it. If users dislike verbose answers, make the prompt ask for conciseness; if answers lack detail, prompt the bot to be more specific (PDF p. 903).

**Sentiment.** Complaints may be general negative sentiment (frustration, disappointment, ridicule) without a stated reason, such as "Uggh". Though it may sound dystopian, tracking sentiment through conversations can show how the bot is doing. Some call centers track callers' voices: a user getting louder signals trouble, while someone who starts angry and ends happy suggests the issue was resolved (PDF pp. 903-904).

**Refusals.** Signals can also come from the model's own responses. An important one is the refusal rate: replies such as "Sorry, I don't know that one" or "As a language model, I can't do ..." probably mean an unhappy user (PDF p. 904).

## Other conversational feedback (from actions, not messages)
- **Regeneration**: many apps let users request another response, sometimes from a different model. It may mean dissatisfaction, but also that the first answer was adequate and the user wants options to compare, which is common for creative requests like image or story generation. The signal may be stronger under usage-based billing than under a subscription, because paying users are less likely to regenerate out of idle curiosity (PDF p. 904). The author says they regenerate on complex requests to check consistency, since two contradicting answers mean neither can be trusted (PDF p. 905). After regeneration some apps ask users to compare the new and previous responses; Figure 10-13 (PDF p. 905) shows ChatGPT asking "Was this response better or worse?" with Better, Worse and Same buttons beside a 2/2 response pager. This better/worse data can drive preference finetuning (PDF p. 905).
- **Conversation organization**: delete, rename, share and bookmark. Deleting is a strong negative signal unless the chat was embarrassing and the user wants no trace. Renaming suggests the conversation is good but the auto-generated title is bad (PDF p. 905).
- **Conversation length**: turns per conversation. Whether it is positive or negative depends on the application: for AI companions a long conversation may mean enjoyment, while for productivity chatbots such as customer support it may mean the bot is inefficient at resolving issues (PDF pp. 905-906).
- **Dialogue diversity**: read alongside length, measured by distinct token or topic counts. A long conversation in which the bot keeps repeating a few lines may mean the user is stuck in a loop (PDF p. 906).

## Alternatives and trade-offs: explicit versus implicit
- Explicit feedback is easier to interpret but costs users effort, so it can be sparse, especially in apps with small user bases. It also suffers from response bias; for example, unhappy users are more likely to complain, making feedback look more negative than reality (PDF p. 906).
- Implicit feedback is more abundant (limited only by imagination) but noisier and harder to interpret. Sharing a conversation can be negative or positive: one friend of the author mostly shares when the model makes glaring mistakes, another mostly shares useful conversations (PDF p. 906; the sentence concludes on the next page).

## Limitations and failure modes
Signals are ambiguous: regeneration, deletion, sharing and conversation length each have both positive and negative readings, depending on the application and user. Treat them as hypotheses to test with data analysis and user studies (PDF pp. 897, 904-906).

## Evaluation and success criteria
Track these signals in production as monitoring metrics (PDF pp. 897-898), and validate their meaning rigorously rather than by intuition alone (PDF p. 897).

## Relations
Follows the user-feedback lead-in (C10-010) on why feedback is a data asset. The signals can be fed into the monitoring metrics of C10-008, and the orchestrator of C10-009 can host the components that collect them.
