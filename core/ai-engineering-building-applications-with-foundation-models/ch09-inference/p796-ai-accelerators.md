---
id: C09-004
title: AI Accelerators
source_pages: "796-807"
chapter: 9
concepts: [ai-accelerator, gpu, cpu-vs-gpu, flops, memory-hierarchy, hbm, sram, power-consumption, tdp, accelerator-selection, compute-bound, memory-bound]
related: [C09-003, C09-005, C09-006]
time_sensitive: true
---
# AI Accelerators
(Source: PDF pp. 796-807; the top of PDF p. 796, Figure 9-5 and the utilization paragraph, closes the preceding section on inference performance metrics, C09-003, and is not covered here)

## What the section covers
A hardware-focused view of inference: what an accelerator is, how GPUs differ from CPUs, the families of accelerators, the compute primitives chips use, and the three characteristics that matter most when comparing chips (computational capability, memory size and bandwidth, power consumption). It ends with guidance on choosing accelerators. The book says the discussion is written from an inference angle but also applies to training (PDF p. 797). The very end of PDF p. 807 flows into the next section, which starts on PDF p. 808 (C09-005).

## Meaning

### Why hardware matters
- How fast and cheap software runs depends on its hardware. Some optimizations work on any chip, but understanding the hardware allows deeper optimization (PDF pp. 796-797).
- Models and hardware have developed together. The lack of powerful enough computers contributed to the first AI winter in the 1970s. The deep learning revival of 2012 was tied to compute: AlexNet (Krizhevsky et al., 2012) is commonly credited as the first paper to train neural networks successfully on GPUs (graphics processing units). Previously a model of that scale would have needed thousands of CPUs, while a couple of GPUs were within reach of PhD students and researchers, which set off the research boom (PDF p. 797).

### What an accelerator is
- An accelerator is a chip built to speed up one kind of computational workload; an AI accelerator is built for AI workloads. GPUs are the dominant type, and NVIDIA is called the biggest economic driver of the early-2020s AI boom (PDF p. 797).
- CPUs versus GPUs (PDF p. 798):
  - CPUs are general purpose with a few powerful cores, typically up to 64 on high-end consumer machines. They handle multi-threaded work, but their strength is high single-thread performance: operating systems, I/O management, complex sequential processes.
  - GPUs have thousands of smaller, weaker cores suited to work that splits into many small independent calculations, such as graphics rendering and machine learning. Matrix multiplication, which makes up most ML workloads, is highly parallelizable.
  - Efficient parallelism raises compute capability but creates difficulties for memory design and power consumption.
- NVIDIA's success inspired other accelerators: AMD's newer GPUs, Google's TPU (Tensor Processing Unit), Intel's Habana Gaudi, Graphcore's IPU (Intelligent Processing Unit), Groq's LPU (Language Processing Unit), and Cerebras' Wafer-Scale Quant Processing Unit (QPU), with more being introduced (PDF p. 798).

### Inference-specialized and other chips
- Many chips do both training and inference, but a growing theme is chips specialized for inference. A survey by Desislavov et al. (2023) reports that inference can cost more than training in commonly used systems and accounts for up to 90% of ML costs of deployed AI systems (PDF p. 799).
- Reasons given (as discussed in Chapter 7): training needs much more memory because of backpropagation and is harder to run in low precision; training usually stresses throughput, while inference aims to minimize latency. So inference chips often optimize for lower precision and faster memory access rather than large memory capacity (PDF p. 799).
- Examples of inference-oriented chips: Apple Neural Engine, AWS Inferentia, and MTIA (Meta Training and Inference Accelerator). Edge-computing chips such as Google's Edge TPU and NVIDIA Jetson Xavier also tend to target inference (PDF p. 799).
- Some chips are specialized for particular model architectures, such as the transformer. Many are for data centers, and increasingly more are for consumer devices such as phones and laptops (PDF p. 799).

### Compute primitives
- Architectures differ in memory layout and in specialized compute units, which evolve over time. The units are tuned for specific data shapes: scalars, vectors or tensors (PDF pp. 799-800).
- Figure 9-6 (PDF p. 800) shows three panels, Scalar, Vector and Tensor, each drawing a small grid of cells next to a larger grid with highlighted cells. The highlighted portion grows from a single cell (scalar), to a row or column (vector), to a block of cells (tensor), conveying how much data one compute primitive handles at once. Described from the render; the figure carries no numbers.
- A chip may mix unit types. GPUs traditionally supported vector operations, but many modern GPUs add tensor cores for matrix and tensor computation. TPUs use tensor operations as their main primitive. To run a model well on a given architecture, take its memory layout and compute primitives into account (PDF p. 800).
- Spec sheets hold many details, but the characteristics that matter across use cases are computational capabilities, memory size and bandwidth, and power consumption. GPUs are used as the examples (PDF p. 800).

## How it works: the three key characteristics

### Computational capabilities
- Measured by how many operations a chip can do in a given time. The most common metric is FLOP/s (often written FLOPS), the peak number of floating-point operations per second (FLOP/s = floating-point operations per second). Real applications rarely reach the peak. The ratio of actual FLOP/s to theoretical FLOP/s is one utilization metric (PDF p. 801).
- The count depends on numerical precision: higher precision means fewer operations per second. Adding two 32-bit numbers generally takes about twice the computation of adding two 16-bit numbers, though real chips do not give exactly half the 32-bit rate because of chip-specific optimizations. The book points back to its "Numerical Representations" discussion (PDF p. 801).
- Table 9-2 (PDF p. 802), NVIDIA H100 SXM, teraFLOP/s (trillion FLOP/s) with sparsity: TF32 Tensor Core 989; BFLOAT16 Tensor Core 1,979; FP16 Tensor Core 1,979; FP8 Tensor Core 3,958. The table note recalls that TF32 is a 19-bit format, not 32-bit (PDF p. 802). Observation from the numbers: the 16-bit rate is about double the TF32 rate and the FP8 rate is about double the 16-bit rate (989 x 2 = 1,978, roughly 1,979; 1,979 x 2 = 3,958).

### Memory size and bandwidth
- Many GPU cores work in parallel, so data must be moved from memory to the cores quickly; this matters especially for large weight matrices and training data. Hence GPU memory needs higher bandwidth and lower latency than CPU memory, requires more advanced memory technology, and is one reason GPU memory costs more (PDF p. 802).
- CPUs typically use DDR SDRAM (Double Data Rate Synchronous Dynamic Random-Access Memory), a 2D structure. High-end GPUs often use HBM (high-bandwidth memory), a 3D stacked structure (PDF p. 803).
- An accelerator's memory is described by size and bandwidth, to be judged within the whole system. A GPU usually interacts with three memory levels (Figure 9-7) (PDF p. 803):
  1. CPU memory (DRAM), also called system memory, host memory or CPU DRAM. It is accessible because accelerators sit beside CPUs. It has the lowest bandwidth of the three, about 25-50 GB/s. Size varies: average laptops around 16-64 GB, high-end workstations a terabyte or more (PDF p. 803).
  2. GPU high-bandwidth memory (HBM): dedicated to the GPU and placed close to it. Bandwidth typically ranges from 256 GB/s to over 1.5 TB/s, important for big transfers and high throughput. A consumer GPU has around 24-80 GB of HBM (PDF pp. 803-804).
  3. GPU on-chip SRAM: built into the chip to hold frequently used data and instructions for nearly instant access. It includes L1 and L2 caches made of SRAM and, in some architectures, L3 caches, as part of on-chip memory that also has register files and shared memory. Its transfer speed often exceeds 10 TB/s, but it is small, typically 40 MB or less (PDF p. 804). (Note on the source text: the sentence is printed as "RAM has extremely high data transfer speeds, often exceeding 10 TB/s", with "RAM" where SRAM is evidently meant, since it sits under the SRAM heading.)
- Figure 9-7 (PDF p. 805) is a three-tier pyramid labeled with reference numbers: level 1 CPU DRAM, 1 TB, 25 GB/s; level 2 GPU HBM, 40 GB, 1.5 TB/s; level 3 GPU SRAM, 20 MB, 10 TB/s. The caption states the numbers are for reference only and vary by chip. Reading the tiers upward: capacity shrinks while bandwidth rises.
- Much GPU optimization is about using this hierarchy well. As of the book's writing, PyTorch and TensorFlow do not offer fine-grained control over memory access, so many researchers and engineers have turned to GPU programming languages: CUDA (originally Compute Unified Device Architecture), OpenAI's Triton, and ROCm (Radeon Open Compute), the latter being AMD's open source alternative to NVIDIA's proprietary CUDA (PDF p. 805).

### Power consumption
- Computation happens as transistors switch on and off, which costs energy. An NVIDIA A100 has 54 billion transistors and an H100 has 80 billion. Efficient use means billions switching rapidly, drawing much energy and producing considerable heat; cooling systems then use more electricity and add to data-center energy use (PDF pp. 805-806).
- Chip energy use threatens a large environmental impact and pushes companies toward green data centers. An H100 running at peak for a year uses about 7,000 kWh, against roughly 10,000 kWh for the average US household's annual electricity. This is why electricity bottlenecks compute scaling (PDF p. 806).
- Two ways power is specified (PDF p. 806):
  - Maximum power draw: peak power under full load.
  - TDP (thermal design power): the maximum heat the cooling system must remove under typical workloads. It is not an exact power measure but indicates expected draw. For CPUs and GPUs, maximum power draw is roughly 1.1 to 1.5 times TDP, depending on architecture and workload.
- Cloud users need not handle cooling or electricity, but the numbers still help show accelerators' environmental and electricity-demand impact (PDF p. 807).

## When and how to apply: selecting accelerators
- The right choice depends on the workload. For compute-bound workloads, look for chips with more FLOP/s. For memory-bound workloads, spending on higher bandwidth and more memory makes life easier (PDF p. 807).
- Three questions when evaluating chips to buy: can the hardware run your workloads, how long does it take, and how much does it cost (PDF p. 807).
- FLOP/s, memory size and memory bandwidth are the three numbers that answer the first two questions. The cost question is straightforward: cloud pricing is usually usage-based and fairly similar across providers; for owned hardware, cost follows from the initial price plus ongoing power consumption (PDF p. 807).

## Limitations and caveats
- Peak FLOP/s is theoretical; the spec numbers in this section are for reference and real chips vary (PDF pp. 801, 805).
- The framework limitation on memory control is stated for the time of writing (PDF p. 805).

## Relations
Continues the performance-metrics discussion in C09-003 (utilization, compute-bound versus memory-bound) and leads into the optimization overview (C09-005) and model optimization techniques (C09-006).

## Time-sensitive statements
Specific chip names and generations (H100, A100, Gaudi, Inferentia, MTIA and the rest), FLOP/s figures in Table 9-2, memory and bandwidth ranges, transistor counts, the 7,000 kWh figure, and the statement about PyTorch/TensorFlow memory control all reflect the book's time of writing.
