---
id: C08-010
title: AI-Powered Data Synthesis
source_pages: "738-752"
chapter: 8
concepts: [ai-data-synthesis, self-play, back-translation, instruction-data-synthesis, reverse-instruction, llama-3-synthetic-data, data-verification, model-collapse, data-lineage, superficial-imitation]
related: [C08-009, C08-011, C03-010, C03-016, C02-008, C02-009]
time_sensitive: false
---
# AI-Powered Data Synthesis
(Source: PDF pp. 738-752)

## What the section covers
How foundation models themselves are used to create training data: simulating APIs and people, self-play, paraphrasing and translation (natural and programming languages), data for pre-training versus post-training, preference data, instruction data synthesis (with Alpaca, UltraChat, reverse instruction, long-context finetuning and the detailed Llama 3 coding pipeline), verifying synthetic data, and four limitations of AI-generated data (quality, superficial imitation, model collapse, obscured lineage). The author notes the techniques listed are not comprehensive, only a good overview (PDF p. 738). The next row (C08-011) covers model distillation.

## How it works

### AI as a simulator
- Simulating programs and APIs: AI can simulate the outcomes of arbitrary programs. "StableToolBench" (Guo et al., 2024) shows using AI to simulate APIs without calling them. To train a model to use a set of APIs, an AI model can predict the expected result of each call instead of making costly or slow real calls (PDF p. 738).
- Simulating humans: the book's example is training a chess bot, where games played by humans take too long whereas matches with AI players are much faster. OpenAI's Dota 2 bot trained in a simulator letting it play about 180 years of games per day, learning by playing against itself, an approach called self-play (OpenAI, 2019). DeepMind used self-play over millions of Go games to train AlphaGo (Silver et al., 2016) (PDF p. 738).
- Self-play is useful beyond game bots, for general agents: have AIs negotiate against each other with different strategies to see which works better; or have one copy of a model play a customer with a problem and another play the support agent (PDF pp. 738-739).

### Paraphrasing and translation to augment datasets
- Paraphrase: from "How to reset my password?" AI can create three queries: "I forgot my password.", "How can I change my password?", "Steps to reset passwords." (PDF p. 739).
- MetaMath: Yu et al. (2023) rewrote the 15,000 examples of MATH and GSM-8K in different ways to get almost 400,000 examples. Models trained on it beat larger models on related math benchmarks (PDF p. 739).
- Translation from high-resource languages (more material online) into low-resource ones helps train small models specialized in languages such as Quechua or Lao (PDF p. 739).
- Back-translation check for translations: with original English sentence X and Lao translation Y, use another model to translate Y back to X'. If X' differs greatly from X, Y is probably bad (PDF p. 739).
- Programming-language translation: AI can convert code between languages. The Llama 3 authors used code translation to widen the range of programming languages in their SFT dataset; Llama 3 training relies heavily on synthetic data and many creative generation techniques (PDF p. 740).
- Code back-translation in Llama 3: from code snippets, AI generates explanations and documentation; AI then regenerates code from those explanations; the explanation and documentation are used for finetuning only if the regenerated code is judged faithful to the original (PDF p. 740).

### Pre-training versus post-training
- Synthetic data can serve both, but is deliberately included far more often in post-training. A possible reason offered: pre-training aims to add knowledge, and AI can reformat existing knowledge but finds it harder to create new knowledge (PDF p. 740).
- Still, as the internet fills with AI-generated content, models trained on web data are probably already pre-trained on some synthetic data. Cosmopedia (Allal et al., 2024) is a 25-billion-token synthetic collection of textbooks, blog posts, stories, posts and WikiHow articles produced by Mixtral-8x7B-Instruct-v0.1 (Jiang et al., 2024) (PDF pp. 740-741).
- Post-training data (instruction data and preference data) generally takes the most effort to produce, which is another reason synthesis is common there (PDF p. 741).

### Preference data
Using AI to pick the better of several responses is relatively simple (largely covered in Chapter 3). The main challenge is the judge's biases, such as first-position bias (preferring the first option). NVIDIA researchers asked the judge twice, swapping the order, and kept a (prompt, winning, losing) triplet only when both runs chose the same winner (NVIDIA, 2024) (PDF p. 741).

### Instruction data synthesis
- Each instruction-finetuning example is an instruction plus a response. AI can generate the instructions, the responses or both: for instance AI instructions with human responses, or human instructions with AI responses (PDF p. 741).
- Instruction generation: to ensure coverage, begin with a list of topics, keywords and/or instruction types, then generate a set number of instructions per item. Alternatively start with templates and generate a set number of examples per template. Both the topic list and the templates can themselves be AI-generated. For responses, generate one or more per instruction (PDF p. 742).
- UltraChat (Ding et al., 2023), a multi-turn dialogue set: ChatGPT produced 30 topics on daily-life areas (technology, food and drink, fashion, nature, education, finance, travel and so on), then 30 to 50 subtopics per topic, then the same model produced instructions and responses for the subtopics (PDF p. 742).
- Alpaca (Taori et al., 2023): Stanford started with 175 (instruction, response) examples from the Self-Instruct seed dataset (Wang et al., 2022), written to be diverse and interesting, and used GPT-3 (text-davinci-003) to generate 52,000 pairs mirroring them (PDF p. 742). Figure 8-5 shows one seed task (instruction: brainstorm a list of possible New Year's resolutions; output: items such as lose weight, exercise more, eat healthier) beside one generated task (instruction: brainstorm creative ideas for designing a conference room; output shown only as a truncated fragment, "... incorporating flexible components, such as moveable walls and furniture ...", i.e. the generated example is cut off mid-text in the figure; the seed output lists three bullets) (PDF p. 743).

### Reverse instruction
- Problem: long high-quality responses are harder for AI than short instructions, and the longer the response the more chance of hallucination (PDF p. 743).
- Approach (Köksal et al., 2023; Li et al., 2023; Chen et al., 2023): take existing long-form, high-quality human content such as stories, books and Wikipedia articles, and have AI generate prompts that would elicit it. This gives higher-quality instruction data and avoids hallucinations in responses (PDF p. 743).
- Self-improving loop (Li et al., 2023), which can build increasingly strong models without new manual annotation: (1) train a weak model on a few seed examples; (2) use it to generate instructions for existing high-quality content, producing quality instruction data; (3) finetune the weak model on that data; (4) repeat until performance is satisfactory (PDF pp. 743-744).

### Long-context finetuning with synthetic data
If a model handles at most 8K tokens and you want 128K: split long documents into chunks shorter than 8K; generate several (question, answer) pairs per chunk; then for each pair use the original long document as context (it may exceed 8K but stay below the target length), which teaches the model to use the extended context to answer (PDF p. 744).

### Llama 3 as a case study
The Llama 3 paper (Dubey et al., 2024) is detailed enough to serve as a case study (PDF p. 744). Besides code translation and back-translation (which derive more data from existing code), the authors synthesized coding instruction data from scratch (PDF pp. 744-745):
1. Generate many programming problem descriptions spanning diverse topics.
2. Given a description and a programming language, generate a solution. Including general rules of good programming and chain-of-thought reasoning improved quality (PDF p. 745).

Correctness and error-correction pipeline (PDF p. 745):
1. Run code through parsers and linters to catch syntax-type errors such as missing imports and uninitialized variables.
2. Run unit tests to catch runtime errors; the unit tests were themselves AI-generated.
3. When a solution fails any step, prompt the model to revise it, giving the problem description, the faulty solution and the feedback from the parser, linter and tests. Only examples passing all checks enter the final SFT dataset.

Combined workflow of the three methods (code generation, translation, back-translation) (PDF pp. 745-746): AI writes problem descriptions; AI writes solutions in various languages; AI writes unit tests; AI fixes errors; AI translates code into other languages and translated code that fails tests is filtered out; AI generates conversations about the code, such as explanations and documentation, and those failing back-translation verification are filtered out. The result: over 2.7 million synthetic coding-related examples for SFT of Llama 3.1 (PDF p. 746).

## Data verification
- Synthetic data quality can be measured like other AI outputs: by functional correctness and by AI judges. The techniques apply to training data in general, not only synthetic (PDF p. 746).
- Echoing evaluation-driven development from Chapter 4: people tend to synthesize data they can verify. Coding is popular for foundation models because it can be functionally evaluated, and for the same reason coding examples are among the most synthesized. Most of Llama 3's synthetic data is coding-related, and all three of its methods produce data verifiable programmatically through code execution and back-translation (PDF pp. 746-747).
- For data without functional correctness, use AI verifiers: a general-purpose AI judge or a specialized scorer. Simplest forms: score each example 1 to 5, or classify good/bad; or describe quality requirements to a foundation model and ask whether an example meets them. For factual consistency, use the inconsistency-detection techniques from Chapter 4 to drop likely hallucinations (PDF p. 747).
- Creative options: if synthetic data should mimic real data, measure how hard it is to tell them apart, for instance by training an AI content detector (easy to separate means poor synthetic data) (PDF p. 747). To resemble high-quality academic work, train a classifier predicting whether a generated paper would be accepted at a venue like NeurIPS and discard clear rejects (PDF p. 748).
- Detect each example's topic and drop those irrelevant to the task. If data should follow a similar pattern, apply anomaly detection to find outliers, which may be low quality (PDF p. 748).
- Heuristic filtering as for real data: remove empty or too-short examples; truncate or remove overly long ones; filter by keywords, user/author, creation date, metadata or source. Self-Instruct (Wang et al., 2022) filtered out repetitive examples, instructions too long or too short, examples with the same instruction but different responses, and examples whose output merely repeats the input (PDF p. 748).
- Evaluation stays hard. As elsewhere, the ultimate test of AI-generated data is real-world performance, i.e. whether it improves the model, and it has passed that test for many models (PDF p. 749).

## Limitations of AI-generated data
Synthetic data will keep growing in importance but may never fully replace human data. Four main reasons: quality difference, limits of imitation, potential model collapse, and obscured lineage (PDF p. 749).

1. **Quality control**: AI data can be low quality ("garbage in, garbage out"); people hesitate to use synthetic data they cannot verify, so reliable data-evaluation methods and metrics are essential (PDF p. 749).
2. **Superficial imitation**: "The False Promise of Imitating Proprietary LLMs" (Gudibande et al., 2023) warns that gains from mimicry may be superficial. Imitation models copy the teacher's style well but may struggle with factual accuracy and with generalizing to tasks outside the training data (PDF p. 750). Worse, imitation can make the student hallucinate: if the teacher can solve hard math questions, training the student on those solutions teaches it to produce answers that look like solutions even if it cannot solve them. The authors suggest improving reasoning requires improving the base models (PDF p. 750).
3. **Potential model collapse**:
   - It is unclear how much AI-generated data a model can train on. Shumailov et al. (2023), "The Curse of Recursion", showed that recursively training on generated data causes irreversible defects and degrading performance, naming it model collapse; seen in Variational Autoencoders, Gaussian mixture models and LLMs (PDF pp. 750-751). It can occur in pre-training and post-training (PDF p. 751).
   - One possible explanation: models favor probable events (e.g., not having cancer) over improbable ones (having cancer); over iterations probable events become over-represented and rare ones under-represented, so models output more common events and forget rare ones (PDF p. 751).
   - Gerstgrasser et al. (2024) argue collapse is inevitable if the whole training set is synthetic but avoidable by mixing in real data; Bertrand et al. (2023) and Dohmatob et al. (2024) found similar. None gives a definitive recommended synthetic-to-real proportion (PDF p. 751).
   - Counter-evidence: Li et al. (2024) found synthetic data nearly as effective as real data for finetuning Llama 2-7B on math, with no clear saturation up to about one million samples; Nemotron-4 340B-Instruct (NVIDIA, 2024) used 98% synthetic data in instruction and preference finetuning (PDF pp. 751-752). The caveat: these experiments covered only one model iteration (PDF p. 752).
   - Bias perpetuation: Taori and Hashimoto (2023), "Data Feedback Loops", show that training on data containing earlier model outputs can amplify existing biases; the more faithful the outputs are to the original training distribution, the more stable the loop and the lower the bias-amplification risk (PDF p. 752).
4. **Obscure data lineage**: AI generation hides where data came from; models can regurgitate training data unnoticed. If generator model X was trained on copyright-violating data, your model may inherit the violation. If X was trained on benchmark B and you evaluate on B, your strong result is contaminated. Without clear lineage it is hard to judge commercial viability or trust performance (PDF p. 752).

## When and how to apply
INTERPRETATION: choose synthesis methods by what you can verify. Prefer pipelines whose outputs can be executed or round-tripped (code, back-translation), add AI-judge or heuristic filters otherwise, mix in real data, and track the generator's provenance.

## Relations
Builds on traditional techniques (C08-009); distillation as a related use of a stronger model's outputs follows in C08-011. Verification relies on functional correctness (C03-010) and AI judges including position bias (C03-016); instruction and preference data relate to SFT (C02-008) and preference finetuning (C02-009).
