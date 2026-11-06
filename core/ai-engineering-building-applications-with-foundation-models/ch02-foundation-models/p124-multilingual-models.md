---
id: C02-003
title: Multilingual Models
source_pages: "124-130"
chapter: 2
concepts: [multilingual-models, low-resource-languages, common-crawl, language-representation, translation-workaround, tokenization-cost, non-english-performance]
related: [C02-002, C02-004]
time_sensitive: true
---
# Multilingual Models
(Source: PDF pp. 124-130, tail on PDF p. 131)

## What the section covers
How the English dominance of internet training data makes general-purpose models weaker, slower and more expensive in other languages; evidence from benchmarks; why translating through English is only a partial fix; and the response of language-specific models.

## Meaning
- English accounts for almost half of Common Crawl (45.88%), about eight times the second most common language, Russian (5.97%) (Lai et al., 2023). Languages with limited training-data availability, typically those below the list in Table 2-1, are called low-resource (PDF p. 124).
- Table 2-1 lists languages with at least 1% of Common Crawl. Each entry gives population (millions) and CC share: English 1,452M / 45.8786%; Russian 258M / 5.9692%; German 134M / 5.8811%; Chinese 1,118M / 4.8747%; Japanese 125M / 4.7884%; French 274M / 4.7254%; Spanish 548M / 4.4690%; Italian 68M / 2.5712%; Dutch 30M / 2.0585%; Polish 45M / 1.6636%; Portuguese 257M / 1.1505%; Vietnamese 85M / 1.0299%. All twelve are categorised H (high-resource) (PDF p. 125).

## How it works: measuring under-representation
- Many languages with large speaker populations are heavily under-represented. The ideal ratio of world-population share to Common Crawl share is 1; the higher the ratio, the more under-represented the language (PDF p. 126).
- Table 2-2 (population share computed on a world population of eight billion) gives speakers, % world population, % in Common Crawl and the ratio: Punjabi 113M, 1.41%, 0.0061%, ratio 231.5; Swahili 71M, 0.89%, 0.0077%, 115.2; Urdu 231M, 2.89%, 0.0274%, 105.3; Kannada 64M, 0.80%, 0.0122%, 65.57; Telugu 95M, 1.19%, 0.0183%, 64.89; Gujarati 62M, 0.78%, 0.0126%, 61.51; Marathi 99M, 1.24%, 0.0213%, 58.10; Bengali 272M, 3.40%, 0.0930%, 36.56. English, for contrast, is 1,452M, 18.15%, 45.88%, ratio 0.40 (PDF p. 127). In the PDF the table is clipped at the right edge: the caption ends mid-sentence ("The last row, English, is for c...") and the fifth column heading is legible only as "Worl... Com... Craw..." (apparently world-population share to Common Crawl share). The ratio values themselves are in the page text; the full heading wording is UNVERIFIED, but the figures match the ratio defined on PDF p. 126 (e.g. 1.41 / 0.0061 is about 231) (PDF p. 127).

## Evidence of weaker performance
- Given English dominance, general-purpose models generally work much better in English than in other languages (PDF pp. 127-128).
- MMLU (14,000 multiple-choice problems over 57 subjects): GPT-4 did much better in English than in under-represented languages such as Telugu. Figure 2-1 (3-shot accuracy; OpenAI translated the questions with Azure AI Translator) shows GPT-4 English at 85.5%, with Italian, Afrikaans, Spanish, German and French all about 84%, then declining through Indonesian 83.1%, Russian 82.7%, Polish 82.1%, Ukrainian 81.9%, Greek 81.4%, Latvian 80.9%, Mandarin 80.1%, Arabic 80.0%, Turkish 80.0% and Japanese 79.9%, Swahili 78.5%, Welsh 77.5%, Korean 77.0%, Icelandic 76.5%, Bengali 73.2%, Urdu 72.6%, Nepali 72.2%, Thai 71.8%, Punjabi 71.4%, Marathi 66.7% and Telugu 62.0%. Reference bars: random guessing 25.0%, Chinchilla-English 67.0%, PaLM-English 69.3%, GPT-3.5-English 70.1% (PDF p. 128).
- Math: Yennie Jun tested GPT-4 on six Project Euler problems and found it solved problems in English more than three times as often as in Armenian or Farsi. It failed all six in Burmese and Amharic. Figure 2-2 plots pass rate per language, with English highest and Burmese and Amharic at zero (PDF pp. 128-129). The bars carry no printed numbers; eyeball estimates only: English about 35-40% passing, Modern Standard Arabic about a third, Spanish, Portuguese, Korean, German and Traditional Chinese about 30%, Urdu, Russian and Simplified Chinese about 23%, Hindi about 20%, Bengali about 17%, Armenian about 13%, Farsi about 10%. The chart covers six questions (Project Euler #205, #206, #357, #493, #500, #686) (PDF p. 129).
- Unexpected behaviour: NewsGuard found ChatGPT more willing to produce misinformation in Chinese than English. In April 2023 ChatGPT-3.5 was asked for misinformation articles about China in English, simplified Chinese and traditional Chinese; it declined six of seven prompts in English but produced false claims all seven times in both Chinese variants. The cause is unclear (PDF p. 130).

## Why it happens
- Under-representation is a major cause: the three worst MMLU languages for GPT-4 (Telugu, Marathi, Punjabi) are also among the most under-represented in Common Crawl (PDF p. 129).
- It is not the only cause. A language's structure and the culture it embodies can also make it harder for a model to learn (PDF p. 129).

## Alternatives and trade-offs: translate to English and back
- Because LLMs translate well, a common approach is to translate queries into English, get the answer, and translate back. The book calls it not ideal (PDF p. 129).
- Problem one: you need a model that understands the under-represented language well enough to translate it (PDF pp. 129-130).
- Problem two: translation loses information. Vietnamese has pronouns that encode the relationship between speakers; translating to English collapses them into "I" and "you" (PDF p. 130).

## Cost and latency in other languages
- A model's inference latency and cost scale with the number of input and output tokens, and tokenization is much more efficient for some languages than others (PDF p. 130).
- Benchmarking GPT-4 on MASSIVE (a million short texts translated into 52 languages), Yennie Jun found that Burmese and Hindi need many more tokens than English or Spanish for the same meaning. Median token length: English 7, Hindi 32, Burmese 72, about ten times English (PDF p. 130).
- If per-token generation time is constant, GPT-4 takes about ten times longer in Burmese than in English for the same content, and token-priced APIs cost about ten times more (PDF pp. 130-131).

## When and how to apply
- Response in the field: many models are trained to focus on non-English languages. The most active non-English language is Chinese (ChatGLM, YAYI, Llama-Chinese and others); other examples are French (CroissantLLM), Vietnamese (PhoGPT) and Arabic (Jais) (PDF p. 131).
- INTERPRETATION: when targeting a non-English market, check benchmark results in that language, expect higher token counts (cost and latency), and test safety behaviour per language rather than assuming English results carry over.

## Relations
Builds on the Common Crawl discussion in C02-002; the sibling case of specialised data is C02-004.

## Time-sensitive statements
Model names, the April 2023 NewsGuard test, GPT-4 scores, token-length medians and the list of language-specific models date from the time of writing.
