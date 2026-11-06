---
id: C07-010
title: Numerical Representations
source_pages: "627-630"
chapter: 7
concepts: [numerical-representations, floating-point, fp32, fp16, bf16, tf32, int8, int4, range-bits, precision-bits, loading-model-format]
related: [C07-009, C07-011, C07-007]
time_sensitive: true
---
# Numerical Representations
(Source: PDF pp. 627-630, plus PDF p. 631 above the Quantization heading; the Quantization section itself is C07-011)

## What the section covers
How numbers are stored in neural networks: the floating-point and integer formats, how their bits split between range and precision, what is lost when converting to a lower-precision format, and a warning about loading a model in the wrong format.

## Figure 7-5 (printed on this row's first page)
PDF p. 627 shows a bar chart from Korthikanti et al. (2022) backing the claim in C07-009 that activation memory can dwarf weight memory. It has paired bars, "baseline" versus "present work", for Megatron models of 22B, 175B, 530B and 1T parameters; each bar is split into "parameters and optimizer state memory" and "activation memory", with a dashed line near 80 GB. Estimated readings (not printed values): baseline totals about 105, 113, 146 and 164 GB, of which parameters plus optimizer state is roughly 46, 46, 32 and 33 GB, so activations make up the larger part; the "present work" bars are about 55 to 60 GB with the same parameter portion. Per-bar numbers are not printed, so treat these as rough. The caption states the point: activation memory can dwarf the model's weights (PDF p. 627).

## Why it matters
The earlier memory math assumed two bytes per value. The memory per value directly feeds the footprint: halve it and weight memory halves (PDF p. 627).

## Meaning: formats
Neural network values are traditionally floats. The most common family is FP, following the IEEE 754 standard (PDF p. 627):
- FP32: 32 bits (4 bytes), single precision.
- FP64: 64 bits (8 bytes), double precision.
- FP16: 16 bits (2 bytes), half precision (PDF p. 628).

FP64 remains the default in NumPy and pandas (as of the book's writing) and is used in many computations, but is rarely used in neural networks because of its memory cost. FP32 and FP16 are more common. Other popular AI formats: BF16 (BFloat16), designed by Google for TPUs, and TF32 (TensorFloat-32), designed by NVIDIA for GPUs (PDF p. 628).

Integers are also used. They are less common than floats but growing in popularity; typical ones are INT8 and INT4 (PDF p. 628).

### Range and precision bits
A float format usually spends 1 bit on the sign; the rest split between range and precision (PDF p. 628).
- Range bits set the span of values the format can represent, like having more digits lets you write a wider range of numbers (PDF pp. 628-629).
- Precision bits set how exactly a value is represented. Example: converting 10.1234 to a format supporting two decimal digits gives 10.12, less precise (PDF p. 629).

Figure 7-6 (PDF p. 629) shows the bit splits (sign bit, range bits, precision bits) and the ranges for two of the formats:
- FP32: 1 + 8 + 23 bits; range about 1e-38 to 3e+38.
- FP16: 1 + 5 + 10 bits; range 6e-8 to 65504.
- BF16: 1 + 8 + 7 bits (range not printed in the figure).
- TF32: 1 + 8 + 10 bits (range not printed in the figure).
The sign bit's width is not labelled in the figure; one bit comes from the text. Consequently BF16 has FP32's range with less precision than FP16, and TF32 has FP32's range bits with FP16's precision bits.

Formats with more bits are called higher precision; converting to a format with fewer bits (e.g., FP32 to FP16) reduces precision, which can change a value or cause errors (PDF pp. 629-630).

## Table 7-3: converting FP32 values to lower precision
The book converts a series of FP32 values, with the inaccurate digits italicised in print (the italics could not be reproduced here) (PDF p. 630). Values (FP32 / FP16 / BF16 / TF32):
- 0.0123456789 / 0.0123443603515625 / 0.0123291 / 0.01234436035
- 0.123456789 / 0.12347412109375 / 0.123535 / 0.12341308593
- 1.23456789 / 1.234375 / 1.23438 / 1.234375
- 12.3456789 / 12.34375 / 12.375 / 12.34375
- 123.456789 / 123.4375 / 123.5 / 123.4375
- 1234.56789 / 1235.0 / 1232.0 / 1234.0
- 12345.6789 / 12344.0 / 12352.0 / 12344.0
- 123456.789 / INF / 123392.0 / 123456.0
- 1234567.89 / INF / 1236990.0 / 1233920.0
A footnote says values out of bound in FP16 are rounded to infinity. The rightmost TF32 column is slightly clipped at the page edge in the render, so the first two TF32 entries (0.01234436035 and 0.12341308593) are taken from the text layer. SUPPLEMENTARY: recomputing with a 10-bit mantissa (TF32) gives 0.0123443603515625 and, truncating rather than rounding, 0.1234130859375, so both entries match the computed values to the digits shown and are not cut off.

## How it works: BF16 versus FP16
Although BF16 and FP16 both use 16 bits, BF16 has more range bits and fewer precision bits. So BF16 can represent large values that overflow FP16 (the 123456.789 row), but is less precise. Worked example (checked): 1234.56789 becomes 1235.0 in FP16, a 0.035% change, versus 1232.0 in BF16, a 0.208% change (PDF pp. 630-631).
INTERPRETATION: re-derived, the percentages follow from |converted - original| / original, about 0.43 / 1234.57 and 2.57 / 1234.57 respectively; the book prints only the percentages.

## Limitations and failure modes
Load a model in the format it was intended for. Wrong format can change the model markedly. Example: Llama 2 shipped with BF16 weights, yet many teams loaded it as FP16 and were frustrated by quality far below the advertised level. The book notes the upside that it forced many people to learn about numerical representations (PDF p. 631).

## When and how to apply
The best format depends on the distribution of values in your workload (what range you need), how sensitive the workload is to small numerical changes, and the underlying hardware (PDF p. 631).

## Time-sensitive statements
FP64 being the default in NumPy and pandas, and Llama 2 releasing in BF16, are stated as of the book's writing (PDF pp. 628, 631).

## Relations
Explains the "M bytes per value" in the memory formulas of C07-009; reducing precision is quantization, covered in C07-011 (whose heading follows on PDF p. 631).
