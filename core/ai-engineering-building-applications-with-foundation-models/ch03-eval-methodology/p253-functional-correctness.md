---
id: C03-010
title: Functional Correctness
source_pages: "253-256"
chapter: 3
concepts: [functional-correctness, execution-accuracy, unit-tests, pass-at-k, humaneval, mbpp, text-to-sql, measurable-objectives]
related: [C03-009, C03-011, C03-002]
time_sensitive: false
---
# Functional Correctness
(Source: PDF pp. 253-256)

## What the section covers
Evaluating a system by whether it does what it is meant to do, with code generation as the main case where this can be automated, the benchmarks that use it, the pass@k metric, and other tasks with measurable objectives.

## Meaning
- Functional correctness means judging a system by whether it performs its intended function. Examples: does a generated website meet your requirements, does a model asked to book a restaurant succeed (PDF pp. 253-254).
- It is the ultimate metric for any application because it checks whether the application does its job. But it is not always easy to measure and cannot always be automated (PDF p. 254).
- In coding it is sometimes called execution accuracy (PDF p. 254).

## How it works: code generation
- Example: ask the model to write a Python function gcd(num1, num2) returning the greatest common denominator of two numbers. Feed the generated code to a Python interpreter to check it is valid and gives the right result for a pair. For (15, 20) the correct answer is 5; if gcd(15, 20) returns anything else, the function is wrong (PDF p. 254).
- Automatic verification of code long predates AI code writing. Software engineering routinely uses unit tests that run code in varied scenarios and compare against expected outputs. Platforms such as LeetCode and HackerRank validate submissions this way (PDF p. 254).
- Popular code benchmarks scored by functional correctness: OpenAI's HumanEval and Google's MBPP (Mostly Basic Python Problems Dataset). Text-to-SQL benchmarks also rely on it: Spider (Yu et al., 2018), BIRD-SQL (Li et al., 2023) and WikiSQL (Zhong et al., 2017) (PDF p. 255).
- A benchmark problem ships with test cases, each a scenario for the code to run plus its expected output. HumanEval's example gives a function signature and docstring for has_close_elements(numbers, threshold), which checks whether any two numbers in a list are closer than a threshold, together with a check function containing a series of assert statements, each one a test case (PDF pp. 255-256). In the book's listing the signature is has_close_elements(numbers: List[float], threshold: float) with a docstring containing two doctest-style example calls; the check(candidate) function holds seven assert lines (one on p. 255, six on p. 256). The PDF's code block is horizontally cut off, so the end of every line, including the expected values, the full docstring and the threshold arguments, is not legible; those parts are UNVERIFIED and not reproduced.

## pass@k
- For each problem the model generates k code samples. A problem counts as solved if any of the k samples passes all of that problem's test cases. The score pass@k is the fraction of problems solved out of all problems (PDF p. 256).
- Worked example: 10 problems, 5 solved with k = 3 gives pass@3 = 50% (PDF p. 256).
- More samples give more chances per problem, so in expectation pass@1 < pass@3 < pass@10 (PDF p. 256). No other formula appears on this page (rendered page checked).

## When and how to apply
- Other tasks with automatically measurable functional correctness include game bots: a Tetris-playing bot is judged by its game score (PDF p. 256).
- More generally, tasks with measurable objectives can typically be evaluated by functional correctness. For example, if AI schedules workloads to optimize energy use, performance is the energy saved (PDF p. 256).

## Limitations
Functional correctness may not be straightforward to measure and often cannot be automated easily; code is the notable case where it can (PDF p. 254).

## Relations
Introduced in the exact-evaluation lead-in (C03-009). The other exact approach, similarity against reference data, is C03-011. The open-ended nature that makes ground-truth comparison hard is in C03-002.
