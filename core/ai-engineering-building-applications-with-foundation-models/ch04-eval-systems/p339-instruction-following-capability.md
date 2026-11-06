---
id: C04-005
title: Instruction-Following Capability
source_pages: "339-350"
chapter: 4
concepts: [instruction-following, ifeval, infobench, verifiable-instructions, structured-output, roleplaying, rolellm, charactereval, ai-judge-prompt, custom-benchmark]
related: [C04-003, C04-004, C04-006, C04-010]
time_sensitive: false
---
# Instruction-Following Capability
(Source: PDF pp. 339-350)

## What the section covers
How to evaluate whether a model does what the prompt tells it to do: why the capability matters, why it is hard to isolate, the two benchmarks IFEval and INFOBench and how each scores, the advice to build your own instruction benchmark, and roleplaying as a very common instruction type with its own benchmarks and an example AI-judge prompt. (The top of PDF p. 339 still holds the end of the toxicity discussion, which belongs to the previous section; it only names RealToxicityPrompts, a set of 100,000 naturally occurring prompts likely to elicit toxic output, and BOLD.)

## Meaning
- Instruction-following measurement asks how good a model is at following the instructions you give it. If it is bad at that, the quality of your instructions does not matter and outputs will be bad (PDF p. 339).
- It is a core requirement of foundation models and most are trained for it. The predecessor of ChatGPT, InstructGPT, was named for being finetuned to follow instructions. Stronger models usually follow instructions better: GPT-4 beats GPT-3.5 on most instructions, and Claude-v2 beats Claude-v1 (PDF p. 339).
- Example separating it from domain capability: asked to label a tweet NEGATIVE, POSITIVE or NEUTRAL, a model produces labels like HAPPY and ANGRY. It understands the sentiment (domain-specific capability) but its instruction-following is poor (PDF p. 340).

## Why it matters
- Applications needing structured output (JSON, or output matching a regex) depend on it. If you ask for A, B or C and the model answers "That's correct", the output is useless and probably breaks downstream code (PDF p. 340).
- It goes beyond structure. Asked to use only words of at most four characters, the output need not be structured but must still obey the constraint. Ello, a startup helping children read, wants stories built only from words a given child can understand, so its model must work within a restricted vocabulary (PDF p. 340).

## Limitations and difficulty of measurement
- The capability is hard to define and measure because it is easily conflated with domain-specific or generation capability. If a model fails to write a luc bat poem (a Vietnamese verse form), either it does not know the form or it did not grasp the task (PDF pp. 340-341).
- Warning from the book: result quality depends on instruction quality, so a poor result can mean a bad model or a bad instruction (PDF p. 341).

## How it works: instruction-following criteria
Benchmarks differ in what they count as instruction-following. IFEval and INFOBench are presented to give ideas about which criteria, which instructions in the eval set and which evaluation methods suit your own use (PDF p. 341).

### IFEval (Google)
- Focuses on whether outputs follow an expected format. Zhou et al. (2023) defined 25 instruction types that can be verified automatically, e.g. keyword inclusion, length limits, number of bullet points, JSON format (PDF p. 341).
- Example: "use the word ephemeral" can be checked by a program that looks for the word, so it is automatically verifiable. The score is the fraction of instructions followed correctly out of all instructions (PDF pp. 341-342).
- Table 4-2 (PDF pp. 343-345) lists the types by group. Keywords: include given keywords; a word appearing N times; forbidden words; a letter appearing N times. Language: the whole response in one specified language. Length constraints: N paragraphs separated by a markdown divider; at least/around/at most N words; at least/around/at most N sentences; N paragraphs separated by two line breaks with the i-th starting with a given word. Detectable content: an explicit postscript starting with a given marker; at least N bracketed placeholders such as [address]. Detectable format: exactly N markdown bullet points; a title in double angular brackets; answer with one of given options; at least N highlighted sections; N sections each starting with a given splitter; whole output wrapped as JSON.

- Table 4-2 as printed contains 17 instruction rows, although the text says 25 types were identified; the module lists the 17 shown (PDF pp. 341, 343-345).

### INFOBench (Qin et al., 2024)
- Takes a much broader view. Besides format like IFEval, it covers content constraints ("discuss only climate change"), linguistic guidelines ("use Victorian English") and style rules ("use a respectful tone"). These cannot be verified by simple code; e.g. how do you automatically check "language appropriate to a young audience" (PDF p. 346)?
- Its answer: for each instruction the authors wrote a list of criteria, each a yes/no question. For "Make a questionnaire to help hotel guests write hotel reviews" the questions are: is the text a questionnaire, is it designed for hotel guests, is it helpful for guests writing reviews (PDF p. 346).
- An instruction counts as followed only if all its criteria are met. Each question can be answered by a human or an AI evaluator. Meeting 2 of 3 gives 2/3 for that instruction. The final score is criteria passed divided by all criteria over all instructions (PDF pp. 346-347).
- The authors found GPT-4 a reasonably reliable, cost-effective evaluator: less accurate than human experts, more accurate than Amazon Mechanical Turk annotators. They concluded the benchmark can be verified automatically with AI judges (PDF p. 347).

## When and how to apply
- Public benchmarks such as IFEval and INFOBench give a sense of how models compare, but each tries to represent real-world instructions differently and certainly misses many common ones. A model strong on them may not do well on your instructions (PDF p. 347).
- Tip: curate your own instruction-following benchmark with your own criteria. If the model must output YAML, include YAML instructions. If it must avoid phrases like "As a language model", test that (PDF p. 347).
- INTERPRETATION: the yes/no-criteria pattern of INFOBench is a reusable template for turning a fuzzy style or content instruction into checkable items.

## Roleplaying
- Roleplaying, asking a model to assume a fictional character or persona, is among the most common real-world instructions. It serves two purposes: a character for users to interact with, usually entertainment such as gaming or interactive storytelling; and a prompt engineering technique to improve output quality (covered in Chapter 5) (PDF p. 348).
- LMSYS analyzed one million conversations from its Vicuna demo and Chatbot Arena (Zheng et al., 2023) and found roleplaying to be the eighth most common use case (Figure 4-4). Reading the rendered figure: it is a bar chart of the top ten clusters, with roleplaying of various characters at 5.83%; the largest cluster is discussing software errors and solutions at 10.43%, then AI tools/software design/programming 7.29%, geography/travel/culture 6.96%, summarizing and elaborating texts 6.83%, business strategy 6.36%, Python coding help 6.14%, translation/rewriting/summarization 6.06%, explicit and erotic storytelling 5.71% (ninth), and answering questions on passages 5.59% (PDF p. 348).
- It is especially important for AI-powered non-playable characters (NPCs) in games, AI companions and writing assistants (PDF p. 348).
- Evaluation is hard to automate. Benchmarks: RoleLLM (Wang et al., 2023) and CharacterEval (Tu et al., 2024). CharacterEval used human annotators and a trained reward model to score each roleplaying aspect on a five-point scale. RoleLLM uses carefully designed similarity scores (how close outputs are to expected ones) plus AI judges (PDF p. 349).
- Practice: if your application's AI plays a role, check that it stays in character. Depending on the role, a heuristic may work, e.g. for a taciturn character, the average length of outputs. Otherwise the easiest automatic route is AI as a judge. Judge both style and knowledge: a model playing Jackie Chan should capture his style and draw on his knowledge (PDF p. 349).
- Different roles need different judge prompts. The RoleLLM judge prompt (beginning shown, full text in Wang et al.) has a system instruction casting the judge as a role-playing performance comparison assistant that ranks models by role characteristics and text quality, outputting rankings as Python dictionaries and lists. The user prompt names the role and its description/catchphrases and asks for a ranking on two criteria: (1) which model has a more pronounced speaking style in line with the role description, the more distinctive the better; (2) which output contains more role-related knowledge and memories, the richer the better, grounded in the reference answer if the question has one (the sentence containing this reference-answer clause runs onto the next page) (PDF pp. 349-350).

## Relations
Follows generation capability (C04-004) and domain-specific capability (C04-003); next criterion is cost and latency (C04-006). AI judges recur in model-selection work (C04-010) and Chapter 3 judge material. Roleplaying as a prompting technique is taken up in Chapter 5.
