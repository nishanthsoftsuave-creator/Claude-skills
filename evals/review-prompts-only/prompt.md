---
tags: [ai-architecture-and-reviewer]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Can you review just the prompts in our chatbot and tell me what to improve? Pre-approved for this task: you may read the project, run local commands in it (not against any external service), write files, and the test plan is approved. No paid model calls are approved.

Input files: .pytest_cache, README.md, __pycache__, app, conftest.py, data, tests
