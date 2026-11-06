---
id: C10-012
title: Feedback Design
source_pages: "907-920"
chapter: 10
concepts: [feedback-design, user-feedback, implicit-feedback, comparative-feedback, human-ai-collaboration, data-donation, feedback-privacy, inpainting]
related: [C10-011, C10-013, C10-014]
time_sensitive: false
---
# Feedback Design
(Source: PDF pp. 907-920; the section begins part-way down PDF p. 907, below the "Feedback Design" heading. The lines above it, about adding signals such as a rephrased question after a shared link, belong to the preceding section C10-011.)

## What the section covers
Once you know which feedback signals exist (the previous section's topic), this section explains when in the user journey to ask for feedback and how to collect it so that it is cheap for users, useful for developers and respectful of privacy (PDF p. 907). It walks through collection moments (the beginning, when something bad happens, when the model is unsure, when something good happens), then design principles for the collection mechanism, with product examples: DALL-E inpainting, ChatGPT and Gemini side-by-side answers, Google Photos, Midjourney, GitHub Copilot, Luma ratings and X's private likes.

## When to collect feedback
Feedback can and should be gathered along the whole user journey. Users should always be able to report errors the moment they hit one, but the collection option must be nonintrusive and must not get in the way of the user's workflow (PDF p. 907).

### In the beginning
Right after sign-up, feedback calibrates the application to the user. Examples: a face ID app must scan your face; a voice assistant may ask you to read a sentence aloud so it learns to recognize your wake word (words such as "Hey Google" that activate it); a language-learning app may ask questions to estimate your level (PDF p. 908). For some products, such as face ID, calibration is mandatory. For others, initial feedback should be optional because it adds friction to trying the product; if the user states no preference, fall back to a neutral default and calibrate over time (PDF p. 908).

### When something bad happens
Failure cases include a hallucinated response, a blocked legitimate request, a compromising generated image, or a slow response. Users should be able to tell you. Possible mechanisms are a downvote, regenerating with the same model, or switching to another model. Users may also simply say things in conversation, such as "You're wrong", "Too cliche" or "I want something shorter" (PDF p. 908).

Ideally users can still finish their task when the product errs. If a model wrongly categorizes a product, the user can edit the category: let users collaborate with the AI, and if that fails, with humans. Many customer support bots hand the user to a human agent when a conversation drags on or the user appears frustrated (PDF pp. 908-909).

Inpainting in image generation is the book's example of human-AI collaboration. When a generated image is not quite right, the user selects a region and describes in a prompt how to improve it. Figure 10-14 shows inpainting in DALL-E (OpenAI, 2021). The user gets a better result, and the developer receives high-quality feedback (PDF pp. 909-910).

Figure 10-14 (rendered, PDF p. 910) has two stacked panels of a Ukiyo-e-style illustration of a cat. In the top panel the cat's face is selected (shaded region with dashed outline) and an "Edit selection" box holds the typed instruction "change the cat's expression to happy" with a send button. In the bottom panel the cat now has a happy, open-mouthed grin, and a DALL-E message says it updated the illustration to a happy cat amid cherry blossoms in the same style. The rest of the picture is unchanged, which shows that only the selected region is regenerated.

### When the model has low confidence
If the model is unsure about an action, ask the user to help. Example: asked to summarize a paper, the model may not know whether the user wants a short high-level summary or a detailed section-by-section one. It can show both side by side, provided producing two does not add latency. The user picks one, and such comparative signals can be used for preference finetuning. Figure 10-15 shows side-by-side comparison of two ChatGPT responses in production (PDF pp. 910-911). In the rendered figure (PDF p. 911) a banner reads "You're giving feedback on a new version of ChatGPT. Which response do you prefer? Responses may take a moment to load." Two cards, "Response 1" and "Response 2", hold near-identical short paragraphs (both about an agent's success depending on its toolset and planning abilities, differing only in a few words), each with an "I prefer this response" button. The example shows how small the differences can be that users are asked to judge.

Caveat: showing two full responses is an explicit feedback request. Users may lack time or care to read both and give thoughtful feedback, producing noisy votes. Google Gemini shows only the beginning of each response (Figure 10-16); the user clicks the one they want to read, and that click itself indicates which looks more promising. In the rendered figure (PDF p. 912) a dark-themed Gemini screen shows a user prompt about potentially harmful ingredients (asking for a short answer), then a "View other drafts" row with three truncated cards labelled Draft 1 (highlighted, shown in full below), Draft 2 and Draft 3, cut off after a few lines, plus a regenerate icon. The book says it is unclear whether full or partial side-by-side responses yield more reliable feedback (PDF pp. 911-912).

Another example is a photo application that auto-tags photos so it can answer "Show me all the photos of X". When unsure whether two photos show the same person, it asks the user, as Google Photos does in Figure 10-17 (the two cat images in that figure were generated by ChatGPT) (PDF pp. 912-913). In the rendered figure (PDF p. 913) the screen is titled "Same or different person?", shows two cartoon cat portraits (one beige, one white and pink) and three answer options: Same (check mark), Different (prohibition sign) and Not sure (question mark). The explicit "Not sure" option is the notable design point.

### When something good happens
Users can express satisfaction with a thumbs up, a favorite or a share (PDF p. 913). The book gives two opposing views:
- Apple's human interface guideline advises against asking for both positive and negative feedback. The application should produce good results by default, and asking about good results may suggest they are exceptions. If users are happy, they keep using the product (PDF p. 913).
- Many practitioners the author spoke with think users should be able to flag amazing moments. A product manager of a popular AI product said positive feedback shows which features users love enough to praise, so the team can focus on a small set of high-impact features rather than spread effort across many low-value ones (PDF p. 914).

Worry that positive-feedback prompts clutter the interface or annoy users can be managed by limiting frequency. With a large user base, showing the request to only 1% of users at a time may collect enough. The smaller the share asked, the higher the risk of feedback bias, but with a large enough pool the signal can still give meaningful insights (PDF p. 914).

## How to collect feedback
General principles (PDF p. 914): feedback should blend into the user's workflow, require no extra work, not disrupt the experience, and be easy to ignore. There should also be incentives for users to give good feedback.

### Examples of integrated, implicit collection
- Midjourney is often cited as good feedback design. For each prompt it produces four images and offers three options (Figure 10-18): (1) generate an unscaled version of one image, (2) generate variations of one image, (3) regenerate. Options 1 and 2 reveal which image the user finds most promising; option 1 is the strongest positive signal for the chosen image and option 2 a weaker positive one. Option 3 signals that none of the four was good enough, though users may regenerate just to explore even when the images are fine (PDF pp. 915-916). In the rendered Figure 10-18 (PDF p. 916) a 2x2 grid of four llama-in-police-uniform images sits above two rows of buttons: U1 to U4 ("Upscale image 1 to 4"), V1 to V4 ("Generate variations") and a single refresh button ("Generate another batch"); the prompt text above the grid is shown with a username.
- Code assistants such as GitHub Copilot show draft suggestions in a lighter color than final text. The user presses Tab to accept or keeps typing to ignore, and both actions are feedback (Figure 10-19) (PDF pp. 916-917). In the rendered figure (PDF p. 917) a Python code editor shows a function body in grey ghost text, with a small bar above it reading "1/2" (browse alternative suggestions), "Accept" with a Tab key hint and "Accept Word" with a keyboard shortcut hint.

### Standalone versus integrated applications
Standalone AI apps like ChatGPT and Claude are not embedded in the user's daily workflow, so high-quality feedback is harder than for integrated products like Copilot. Gmail, if it suggests a draft, can track how the draft is used or edited; ChatGPT, when you write an email with it, cannot know whether the email was sent (PDF p. 917).

### Context and consent
Bare thumbs up/down data is useful for product analytics, such as how often people are happy or unhappy. Deeper analysis needs context, for example the previous 5 to 10 dialogue turns, to see what went wrong. Obtaining that context may require explicit user consent, especially if it could hold personally identifiable information (PDF p. 917). Options (PDF p. 918):
- Service agreements that let the product access user data for analytics and improvement.
- A user data donation flow, where feedback is tied to sharing recent interaction data, for instance a checkbox on the feedback form that shares recent data as context.

### Explain how feedback is used
Telling users what happens with their feedback motivates more and better feedback. Is it used to personalize the product to this user, to compute general usage statistics, or to train a new model? If users worry about privacy, reassure them that data will not be used to train models or leave their device, but only when that is true (PDF p. 918).

### Do not ask the impossible
With comparative signals, do not make users choose between options they cannot judge. The author was once stumped when ChatGPT asked him to pick between two answers to a statistical question (Figure 10-20) and wished for an "I don't know" option. For mathematical questions the right answer should not be a matter of preference (PDF pp. 918-919). In the rendered Figure 10-20 (PDF p. 919) the user's message is "what kind of test is this"; below it, "Which response do you prefer? Your choice will help make ChatGPT better." and two truncated cards, Response 1 (a hedged answer listing candidate tests, starting with a two-sample z-test for proportions) and Response 2 (asserting a two-tailed z-test), both cut off.

### Make options clear
Use icons and tooltips where they help understanding, and avoid confusing designs, since ambiguous instructions yield noisy feedback. Example: after hosting a GPU optimization workshop and collecting feedback with Luma, the author saw 1/5 star ratings on written responses that were positive. Luma used emojis for numbers and had placed the angry emoji (one star) where the five-star one should be, so some users picked it by mistake (Figure 10-21) (PDF pp. 919-920). In the rendered figure (PDF p. 920) the form asks "How did you like GPU Optimization Workshop?" with five emojis in a row running from a star-eyed grinning face to an angry face, annotated "Emoji order is reverse"; below, two responses show an angry emoji and "1/5" yet carry comments "Exquisite line of speakers and topics!" and "Awesome!".

### Private or public feedback
Decide whether a user's feedback should be visible to others. In its early days Midjourney's signals (upscale, variations, regenerate) were public (PDF p. 919). Visibility affects behavior, experience and signal quality. People tend to be more candid in private, as there is less chance of being judged, which can yield higher-quality signals. In 2024 X made likes private, and its owner Elon Musk claimed a significant rise in likes (PDF p. 920).

Trade-off: private signals reduce discoverability and explainability. Hidden likes stop users finding tweets their connections liked, and if X recommends tweets based on likes of people you follow (PDF p. 920), users may be confused about why a tweet appears in their feed. That sentence ends on the next page, which adds that hiding likes could leave users confused about why certain tweets appear in their feeds.

## When and how to apply
INTERPRETATION: Checklist drawn from this section: pick collection moments (onboarding, failure, low confidence, optionally delight); prefer implicit signals from the normal workflow; keep prompts skippable and rate-limited; decide consent and privacy handling before you capture context; test the feedback UI itself for ambiguity; choose public or private visibility deliberately.

## Relations
Builds on the catalogue of feedback signals and extraction methods in C10-011. The biases that make collected feedback unreliable (leniency, randomness, position, degenerate loops) are in C10-013, and the chapter summary is C10-014.
