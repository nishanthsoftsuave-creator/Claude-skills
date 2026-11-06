---
id: C03-011
title: Similarity Measurements Against Reference Data
source_pages: "257-266"
chapter: 3
concepts: [reference-based-evaluation, ground-truth, exact-match, lexical-similarity, edit-distance, n-gram, bleu, semantic-similarity, embedding-similarity, cosine-similarity, bertscore]
related: [C03-010, C03-012, C03-013]
time_sensitive: false
---
# Similarity Measurements Against Reference Data
(Source: PDF pp. 257-266)

## What the section covers
How to score a generated output by comparing it with reference data when functional correctness cannot be checked automatically: the vocabulary of reference-based evaluation, the four ways to judge similarity, and the three hand-designed metrics (exact match, lexical similarity, semantic similarity), with their drawbacks and the cosine similarity formula.

## Meaning
- When a task cannot be evaluated by functional correctness, a common alternative is to compare outputs against reference data. Example: a French-to-English translation is checked against a known correct English translation (PDF p. 257).
- Each reference example has the shape (input, reference responses). One input may have several references, for instance several valid translations. References are also called ground truths or canonical responses. Metrics that need them are reference-based; metrics that do not are reference-free (PDF p. 257).
- The closer a generated response is to the references, the better it is considered (PDF p. 258).

## Why it matters: the reference-data bottleneck
- The approach is limited by how much reference data can be produced and how quickly (PDF p. 257).
- References are usually made by humans and increasingly by AI. Human references treat human performance as the gold standard, against which the AI is measured. Human data is costly and slow, so many teams generate references with AI; this output may still need human review, but reviewing takes far less labor than writing from scratch (PDF p. 257).

## How it works: four ways to measure similarity
1. Ask an evaluator whether two texts are the same.
2. Exact match: the response equals one of the references.
3. Lexical similarity: how alike the texts look.
4. Semantic similarity: how close the texts are in meaning (PDF p. 258).

The comparison in option 1 can be done by humans or AI evaluators; AI evaluators are increasingly common and are the subject of the next section (the AI as a judge sections). This section covers the hand-designed metrics only. Exact match yields a binary score; lexical and semantic similarity give scores on a sliding scale (for example 0 to 1, or -1 to 1). Despite the ease and flexibility of AI judges, hand-designed measures remain widely used in industry because they are exact (PDF p. 258).

Side note: similarity measurement has other uses beyond scoring outputs, and the techniques recur later in the book. The book lists retrieval and search (find items similar to a query), ranking (order items by similarity to a query), clustering (group items similar to each other), anomaly detection (find the items least similar to the rest) and data deduplication (remove items too similar to others) (PDF p. 259).

### Exact match
- A response counts as a match only if it equals one of the references exactly. This suits tasks with short, exact answers: simple arithmetic, common-knowledge questions, trivia (PDF pp. 259-260). Examples given: "What's 2 + 3?", "Who was the first woman to win a Nobel Prize?", "What's my current account balance?", and a fill-in-the-blank analogy (Paris to France as ___ to England) (PDF p. 260).
- Variation for formatting issues: accept any output that contains the reference. For reference "5", outputs such as "The answer is 5" and "2 + 3 is 5" pass (PDF p. 260).
- Caveat of that variation: it can accept wrong answers. For "What year was Anne Frank born?" (1929, born June 12), an output of "September 12, 1929" contains the right year but is factually wrong (PDF p. 260).
- Beyond simple tasks exact match rarely works. "Comment ca va?" has many valid translations ("How are you?", "How is everything?", "How are you doing?"). If only these three are in the references, "How is it going?" is marked wrong. Longer, more complex texts have even more possible translations, so an exhaustive reference set is impossible; for complex tasks lexical and semantic similarity work better (PDF pp. 260-261).

### Lexical similarity
Lexical similarity measures how much two texts overlap, after splitting them into tokens (PDF p. 261).
- Simplest form: count shared tokens. Worked example with words as tokens, reference "My cats scare the mice": response A "My cats eat the mice" shares 4 of 5 words (80%); response B "Cats and mice fight all the time" shares 3 of 5 (60%). A is judged more similar (PDF p. 261).
- Approximate string matching (fuzzy matching): count the edits needed to turn one text into another, called edit distance. Usual edit operations are deletion ("brad" to "bad"), insertion ("bad" to "bard") and substitution ("bad" to "bed"). Some matchers also count transposition (swapping two letters, "mats" to "mast") as one edit, while others count it as two (a deletion plus an insertion). Example: "bad" is one edit from "bard" and three from "cash", so it is more similar to "bard" (PDF pp. 261-262).
- N-gram similarity: compare overlapping sequences of n tokens rather than single tokens. A 1-gram (unigram) is one token, a 2-gram (bigram) two tokens. "My cats scare the mice" has four bigrams: "my cats", "cats scare", "scare the", "the mice". The measure is the share of the reference's n-grams that also appear in the generated response (PDF p. 262).
- Common lexical metrics: BLEU, ROUGE, METEOR++, TER and CIDEr; they differ in how overlap is computed. They were common before foundation models, especially for translation; fewer benchmarks use them now. Benchmarks still using them include WMT, COCO Captions and GEMv2 (PDF pp. 262-263).

Drawbacks of lexical similarity (PDF pp. 263-264):
- It needs a comprehensive reference set. A good response gets a low score if no reference resembles it. Adept found its model Fuyu scored poorly on some benchmark examples not because outputs were wrong but because correct answers were missing from the references.
- Figure 3-5 (checked on the rendered page, PDF p. 264) shows an image-captioning case: Fuyu captioned a night image as "A nighttime view of Big Ben and the Houses of Parliament." The five reference captions described only a clock tower, traffic or a lit building without naming Big Ben or Parliament, so the CIDEr score was just 0.4 despite a correct caption.
- References can themselves be wrong. Organizers of the WMT 2023 Metrics shared task reported many bad reference translations; low-quality references are one reason reference-free metrics were strong contenders against reference-based ones in correlation with human judgment (Freitag et al., 2023) (PDF p. 263).
- Higher lexical similarity does not always mean a better response. On HumanEval, a code-generation benchmark, OpenAI found BLEU scores for incorrect and correct solutions to be similar, so optimizing BLEU is not the same as optimizing functional correctness (PDF pp. 263-264).

### Semantic similarity
- Lexical similarity measures whether texts look alike, not whether they mean the same. "What's up?" and "How are you?" share little wording yet are close in meaning (PDF p. 264). Conversely, "Let's eat, grandma" and "Let's eat grandma" look nearly identical but mean very different things (PDF p. 265).
- Semantic similarity first turns each text into a numerical representation, an embedding (the book's example: "the cat sits on a mat" as [0.11, 0.02, 0.54]). Hence it is also called embedding similarity. How embeddings work is covered in the next section (C03-012). Embedding similarity is computed with metrics such as cosine similarity; identical embeddings score 1 and opposite embeddings score -1 (PDF p. 265).
- It works for embeddings of any modality (images, audio); for text it is sometimes called semantic textual similarity (PDF p. 265).
- Cosine similarity (formula read from the rendered page, PDF p. 266): let A be the embedding of the generated response and B the embedding of a reference. Then cosine_similarity(A, B) = (A . B) / (||A|| * ||B||), where A . B is the dot product and ||A|| is the Euclidean (L2) norm of A. For A = [0.11, 0.02, 0.54], ||A|| = sqrt(0.11^2 + 0.02^2 + 0.54^2). As printed, the formula line reads "fracA . B ||A||||B||", i.e. a stray "frac" typesetting artifact with no visible fraction bar (the render and the text layer agree).
INTERPRETATION: the intended form is the standard cosine fraction written above, (A . B) / (||A|| ||B||); the book's own bulleted definitions of the dot product and L2 norm support this reading. The norm of B is defined the same way as that of A.
- Metrics for semantic textual similarity include BERTScore (embeddings from BERT) and MoverScore (embeddings from a mixture of algorithms) (PDF p. 266).

## Limitations and failure modes
- Semantic similarity needs a less exhaustive reference set than lexical similarity, but its reliability depends on the quality of the embedding algorithm: with bad embeddings, two same-meaning texts can still score low. The embedding model may also cost nontrivial compute and time (PDF p. 266).
- Warning from the book: semantic similarity is placed in the exact-evaluation category, yet it can be considered subjective because different embedding algorithms produce different embeddings; however, given two embeddings, the score between them is computed exactly (PDF p. 265).
- Exact match and lexical similarity are limited by reference coverage and quality (see above).

## Relations
- Sits under exact evaluation, after functional correctness (C03-010) in the same chapter.
- Embedding basics, used by semantic similarity, are in C03-012. The AI-judge alternative to hand-designed similarity begins at C03-013. Embeddings reappear in vector search (Chapter 6) and data deduplication (Chapter 8) (PDF p. 266).
