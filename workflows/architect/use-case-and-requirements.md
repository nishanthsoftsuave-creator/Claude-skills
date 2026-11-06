---
name: use-case-and-requirements
mode: architect
rows: [C01-006, C01-007, C01-008, C01-009, C01-010, C01-011, C01-012, C01-013, C01-015, C01-016, C01-017, C01-018, C04-003, C04-004, C04-005, C04-006]
---
# Use case and requirements

## When to use

First design workflow in Architect mode, after discovery and `intake.md`. Use it to turn a stated goal into a use case with measurable success criteria, a usefulness threshold, evaluation criteria written as requirements, and a milestone plan. Its output feeds `model-selection.md`, `solution-pattern.md` and `eval-plan.md`.

## Inputs needed

From discovery and intake (do not re-ask what is known): the objective, who the users are, the cost of a wrong answer, constraints (budget, latency, privacy, providers), available data, team skills and timeline. Ask only for the gaps, following `intake.md`. If the session cannot ask, record each gap as an assumption.

## Modules to load

| Row | Module | Why it is needed here |
|---|---|---|
| C01-006 | [Coding](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p064-coding.md) | Pattern: where AI helps most and least in engineering work |
| C01-007 | [Image and Video Production](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p067-image-and-video-production.md) | Pattern: drafts and variants at volume |
| C01-008 | [Writing](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p069-writing.md) | Pattern: writing assistance and its abuse modes |
| C01-009 | [Education](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p071-education.md) | Pattern: personalization and tutoring |
| C01-010 | [Conversational Bots](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p073-conversational-bots.md) | Pattern: support bots, copilots, companions |
| C01-011 | [Information Aggregation](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p074-information-aggregation.md) | Pattern: summarization and talk-to-your-docs |
| C01-012 | [Data Organization](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p076-data-organization.md) | Pattern: organizing unstructured data |
| C01-013 | [Workflow Automation](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p077-workflow-automation.md) | Pattern: structured extraction and agents |
| C01-015 | [Use Case Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p079-use-case-evaluation.md) | Why build, role of AI and humans, defensibility |
| C01-016 | [Setting Expectations](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p085-setting-expectations.md) | Business metrics and the usefulness threshold |
| C01-017 | [Milestone Planning](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p086-milestone-planning.md) | Baseline first, the last mile |
| C01-018 | [Maintenance](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p088-maintenance.md) | What changes after launch |
| C04-003 | [Domain-Specific Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p319-domain-specific-capability.md) | The four criteria buckets; domain capability as a requirement |
| C04-004 | [Generation Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p324-generation-capability.md) | Factual consistency and safety as requirements |
| C04-005 | [Instruction-Following Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p339-instruction-following-capability.md) | Format and constraint compliance as requirements |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | Hard versus ideal thresholds for cost, latency, scale |

## Procedure

1. **State the objective and who benefits.** One sentence each. The book orders the motive for building from high to low risk: competitors with AI could make you obsolete, you would miss profit and productivity gains, or you are unsure where AI fits but do not want to be left behind. Record which one applies, because it sets urgency and the build-versus-buy lean (an existential threat favors in-house; a productivity gain often has buy options). `[C01-015]`
2. **Recognise the use-case pattern** using the library below. Pick the closest one or two, state them, and carry the listed risks into the risk register. If none fits, say so; do not force a pattern.

   | Pattern | Typical shape and known risks (from the book) | Row |
   |---|---|---|
   | Coding | Strongest on documentation, generation and refactoring; minimal gains on highly complex tasks. Funding, revenue and star figures are time-sensitive. | `[C01-006]` |
   | Image and video | Drafts and variants at volume, humans iterate, testing picks winners. | `[C01-007]` |
   | Writing | High tolerance for mistakes is what makes it ideal. Abuse risk: junk content and SEO farms. | `[C01-008]` |
   | Education | Personalization benefits most (the Duolingo course-creation stages); education businesses can also be displaced by AI. | `[C01-009]` |
   | Conversational bots | Support bots cut cost and respond faster; product copilots guide painful tasks; interface may be voice or 3D. | `[C01-010]` |
   | Information aggregation | Talk-to-your-docs and summaries; a fixed output structure plus a downstream integration makes summaries trigger work (INTERPRETATION). | `[C01-011]` |
   | Data organization | Describe and search unstructured data; extract structure for search. | `[C01-012]` |
   | Workflow automation | Extraction and repetitive tasks; tasks needing external tools make it an agent. | `[C01-013]` |

   INTERPRETATION: the book's enterprise survey figure shows internal-facing use cases reaching production more readily than external-facing ones (see the lead-in figure in `[C01-006]`); treat an external-facing launch as needing a higher quality bar and more time.
3. **Place the feature on the book's role dimensions** and record each answer; each changes requirements. `[C01-015]`
   - Critical or complementary: the more critical AI is, the more accurate and reliable it must be.
   - Reactive or proactive: proactive features can be precomputed (latency matters less) but face a higher quality bar because users did not ask for them.
   - Dynamic or static: dynamic means continual updates from user feedback (per-user models or memory); static updates periodically.
   - Role of humans: AI suggests to humans, AI answers simple cases and routes the rest, or AI answers all. Plan Crawl, Walk, Run: human involvement mandatory, then AI with internal staff, then more automation including external users. Move up only when evidence supports it (the book's example is a high acceptance rate of suggestions).
4. **Test defensibility** if this is a standalone AI product. Ask what stops a larger platform copying it in weeks and whether a better base model would subsume it. Name the moat: technology, data or distribution; the book says data is the most nuanced. INTERPRETATION: if there is no moat, record that as a risk, not a blocker. `[C01-015]`
5. **Set business metrics first**, then a usefulness threshold. Business impact comes first (for a support bot: share of messages automated, extra volume handled, response speed, labor saved), plus satisfaction and feedback, since answering more messages does not make users happy. Then define the threshold as a combination of quality, latency (TTFT, TPOT, total), cost per request, and any others such as fairness. Acceptable latency depends on the current process (if humans answer in an hour, faster may be enough). Ask the user to confirm each number. `[C01-016]`
6. **Write the evaluation criteria as requirements** in the four buckets, using the book's legal-summary illustration as the template: domain capability, generation capability, instruction following, cost and latency. `[C04-003]`
   - Domain capability: what the model must know or do. For code add efficiency (runtime, memory) to functional correctness when it affects usability; readability needs subjective judgment. For knowledge and reasoning, multiple-choice accuracy is acceptable, compared with the random baseline (25% for four options); it is not a main check of generation quality. `[C04-003]`
   - Generation: decide local consistency (against supplied context; narrow tasks like summarization, support, analysis) versus global consistency (open knowledge; broad chatbots, fact-checking). Add safety categories that apply. Study where the model hallucinates (the book found niche knowledge and requests about things that do not exist) and weight the evaluation toward those queries. Add any other quality the product needs (the book's examples: controversiality, friendliness, conciseness); fluency and coherence matter mainly for weaker models, creative writing and low-resource languages. `[C04-004]`
   - Instruction following: list format and constraint rules the output must obey (JSON, length, forbidden phrases, persona). Write fuzzy rules as yes/no checks (INTERPRETATION: the book's INFOBench pattern). Build your own instruction set; public ones miss your instructions. `[C04-005]`
   - Cost and latency: separate must-have from nice-to-have. For each of cost, scale (tokens per minute), time to first token and total query time, give a hard requirement and an ideal. Models that miss a hard requirement are dropped; the rest are chosen on quality (the book calls this balancing of objectives Pareto optimization). Note that API cost per token barely falls with scale while self-hosting can fall sharply, so revisit the cost requirement at each scale `[C04-006]`. Table 4-3 is an illustration, not a recommendation. `[C04-006]`
7. **Baseline before promising a date.** Plan to evaluate existing models first, size the gap between baseline and threshold (a model that already handles 30% of tickets leaves less work than one handling none), and state that the work may be abandoned if the effort exceeds the return. `[C01-017]`
8. **Budget the last mile.** A demo may take a weekend while a product takes months. Reaching 80% took one month in the book's LinkedIn example, and going beyond 95% took four more. Schedule the tail separately. `[C01-017]`
9. **Plan for change.** Record what will be maintained: model swaps need versioning and evaluation infrastructure (APIs converge but each model has quirks), and note regulatory (compute, data, talent) and intellectual-property exposure as risks; the book's cautions are that a model built in-house because it looked cheaper was undercut when providers halved prices, and that a provider can fail. INTERPRETATION: re-run build-versus-buy cost comparisons periodically. `[C01-018]`

## Evidence and exit gate

Proceed only when all of these exist and the user has confirmed or explicitly assumed them:
- objective, motive level, use-case pattern(s) and role dimensions (steps 1 to 3);
- business metrics and a numeric usefulness threshold (step 5);
- criteria in all four buckets with hard and ideal values where cost or latency apply (step 6);
- a baseline plan and a milestone list with the check that ends each (steps 7 and 8).
A number with no source is labelled assumption. If the user cannot give a threshold, propose one with its reasoning and mark it `INTERPRETATION`.

## Outputs

- Section 1 (goal and success criteria) and section 7 (milestones) of [architecture-design.md](../../templates/architecture-design.md).
- The criteria table seed for [eval-plan.md](../../templates/eval-plan.md), section 2.
- One [decision-record.md](../../templates/decision-record.md) for the build-or-not and human-role decision.

## Pitfalls

- Treating a good demo as evidence of a product (last mile). `[C01-017]`
- Defining success by volume alone and ignoring satisfaction. `[C01-016]`
- Proactive features shipped at a reactive quality bar. `[C01-015]`
- Blurring domain capability with instruction following, so a failure cannot be attributed; a model that understands sentiment but outputs the wrong labels is an instruction problem. `[C04-005]`
- Relying on multiple-choice scores as proof of generation quality. `[C04-003]`
- Copying the example thresholds of a fictional table as real requirements. `[C04-006]`
- Ignoring that figures, products and rankings in the pattern library are time-sensitive. `[C01-006]` `[C01-008]` `[C01-018]`
