# Module specification (contract for writers and verifiers)

One module file per matrix row, at the row's `destination_file` (under `core/`). A module is a faithful, detailed, original-wording rendering of one span of the book, organised so it can be applied. It is a knowledge base, not a summary: a reader who has not read the book should be able to understand and use the section's ideas from the module alone.

## File format

```markdown
---
id: C03-012
title: Limitations of AI as a Judge
source_pages: "281-289"
chapter: 3
concepts: [ai-as-judge, judge-bias, self-bias, position-bias, verbosity-bias]
related: [C03-010, C03-011, C04-016]
time_sensitive: false
---
# Limitations of AI as a Judge
(Source: PDF pp. 281-289)

## What the section covers
...
```

- `id` and `source_pages` must equal the matrix row (`source_pages` is `N` for one page, else `START-END`, using the row's `start_page` and `end_page`).
- `concepts`: 3-12 lowercase hyphenated keywords for the index. `related`: ids of other matrix rows that this section depends on or feeds (only ids that exist).
- `time_sensitive: true` when the section's facts depend on the date of writing (model names, benchmark scores, prices, hardware generations); say which statements in the body.

## Body: headings to use where the source supports them

Use only the headings that fit; skip the others. Never pad, and never invent content to fill a heading. If the book does not say it, the module does not say it as book content.

1. **What the section covers**: scope in a few lines.
2. **Meaning**: the concepts and terms, with the book's own definitions and terminology.
3. **Why it matters**
4. **How it works**: mechanisms, procedures, formulas, step-by-step methods, examples and what each example shows.
5. **Assumptions and prerequisites**
6. **When and how to apply**: decision criteria and guidance for practice.
7. **Alternatives and trade-offs**: options, advantages, disadvantages.
8. **Limitations and failure modes**
9. **Evaluation and success criteria**: how the book says to measure or check it.
10. **Relations**: how it connects to other sections (cite their ids).
11. **Time-sensitive statements**: list them if `time_sensitive: true`.

Preserve the book's own framing, ordering and distinctions where a template would distort them. Capture every substantive point, example, number and caveat; a short paragraph per page is the minimum, not the target.

## Citations and labels

- Cite source pages as `(PDF p. 283)` or `(PDF pp. 283-285)`, after the claim they support. Every page cited must lie inside the row's range (or the tail page when the matrix row has one). Use no other `p.` pattern for anything else.
- Statements are book content by default. Prefix anything else on its own line or sentence with `INTERPRETATION:` (your operational adaptation of the book's idea), `SUPPLEMENTARY:` (outside knowledge; name the source), or `UNVERIFIED:` (could not confirm). Use these sparingly; most of a module is book content.
- Do not invent claims, formulas, numbers, examples or page references. If something is unclear in the extracted text, check the rendered page; if it still cannot be read reliably, say so in the module and report it as a gap.

## Wording, length and copyright

- Write in your own words. Direct quotation is limited to short phrases (at most about 25 words) in quotation marks with a page cite, used for definitions or distinctive claims.
- No more than 25% of the module's 8-word sequences may match the source (`coverage_check.py --source-dir` measures this). Reword, do not copy.
- Length floor: at least 40 words per source page and at least 80 words in total. Typical faithful modules run 80-150 words per source page. Fewer words than the floor means content was dropped.
- Do not copy figures or tables. Describe what a figure or table shows and the point it makes, and record the specific numbers when they matter to the argument.

## Equations, figures and tables

- The text layer flattens superscripts and subscripts. For every page listed under `equation_pages` for your row in the extraction `index.json`, and for any page with a formula, render it (`python scripts/extract_rows.py --render <pdf> <out_dir> <page>`) and read the image before writing the formula.
- Write formulas in plain text with explicit operators, such as `PPL(P) = 2^H(P)`, and define every symbol the first time.
- For pages in `figure_pages`, read the rendered image when the figure carries content that the text does not (a diagram's structure, numbers in a chart) and describe it in the module.
- If the rendered page and the text layer agree on an expression that looks wrong (for example a missing superscript in the book itself), quote it as printed, say that it looks incomplete, and label any corrected reading `INTERPRETATION:`. Never write that a render "confirms" a correction it does not show.
- If a table or figure is cut off in the PDF, record everything legible, mark the missing part `UNVERIFIED:`, and report it as a minor gap with the page.
- If a formula or figure cannot be read reliably, do not guess. Write what is certain, mark the rest `UNVERIFIED:`, and report the row as a GAP with the exact page.

## What writers and verifiers touch

- A writer writes only the module files of its assigned rows. A verifier edits only those modules. Neither edits the matrix CSV or any other file; the main session updates the matrix with `scripts/matrix_update.py` from the agent reports.
- Rows that begin on a page that opens with the previous section's tail (the row's heading appears part-way down the page): cover only from the heading onward. The text above the heading belongs to the previous row, and the previous row's `tail_page` is how it cites it.
- Content above the next row's heading on this row's `tail_page` belongs to THIS row. Content after that heading does not.
- A section that runs onto the next row's first page when this row has no `tail_page`: describe the continuation without a page cite and say in one sentence that it continues on the next page.
- A "one-line relation" to a neighbouring row means one sentence, never a paragraph.
- Tables whose text wraps mid-word, or that are clipped at the page edge: render the page and read the table from the image. Record every legible value; for partly clipped cells record the visible digits and mark the rest `UNVERIFIED:`.
- Figures with values but no printed numbers (bar charts, scatter plots): give approximate readings only when they are clearly legible, label them as estimates, and say plainly when per-item values cannot be read. Inventory a multi-item figure completely (every bar, panel or example), not only the main point.
- A figure that the text refers to on this row's page but that is printed on the next row's page: describe it in the row where it is printed; in the referencing row give a one-sentence pointer with no page cite.
- A sentence split across a row boundary with no `tail_page`: each row records only its own half, and says the sentence continues or begins on the neighbouring page.
- When a table or figure disagrees with the text (for example the table prints 17 rows while the text says 25), record both and say they differ; do not reconcile them silently.
- Shared pages: when two adjacent rows share a page, each row owns only the content under its own heading. Text at the top of the page that precedes the next heading belongs to the earlier row; text after the heading belongs to the later row. Do not describe the neighbour's content beyond a one-line relation.
- Boundary pages: when a row has a `tail_page`, the page after the row's range may hold the end of the section. Use heading text to find where the section ends, and cite the tail page only for content that belongs to this section.

## Verification (a different agent from the writer)

For each module, re-read the source pages (and rendered pages for equations and figures) and check, in this order:

1. **Accuracy**: every claim, number, term and formula matches the source; no invented content; labels (`INTERPRETATION:` and so on) used honestly.
2. **Completeness**: no substantive point, example, caveat, trade-off or relation from the source span is missing.
3. **Citations**: every cited page is correct and inside range.
4. **Fidelity of framing**: the book's terminology and qualifications are preserved.
5. **Copyright**: wording is original.

Fix defects directly in the module and list each correction. Then return one verdict per row: `VERIFIED` (after any fixes, the module meets all five checks), or `GAP` with the exact missing or unreliable material. Never mark `VERIFIED` without re-reading the source.
