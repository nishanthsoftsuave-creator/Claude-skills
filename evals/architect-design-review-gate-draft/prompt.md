---
tags: [ai-architecture-and-reviewer]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Here is our draft: one large hosted model, a system prompt, a vector DB with 400 documents chunked at 200 characters, no evaluation set yet, no logging, answers go straight to customers. Run it through your design review before we start building.
