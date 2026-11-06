---
tags: [ai-architecture-and-reviewer]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Please review and test our support chatbot. The project is in the working directory. Pre-approved for this task: you may read the project, run local commands in it (not against any external service), write files, and the test plan is approved. No paid model calls are approved. Write your results and report to a run folder under .ai-architecture-and-reviewer/runs/.

Input files: .pytest_cache, README.md, __pycache__, app, conftest.py, data, tests
