---
tags: [ai-architecture-and-reviewer]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We need to pick a model for a customer-facing summarisation feature, about 20 requests per second at peak. Legal is nervous about sending customer text to outside providers. API or self-host?
