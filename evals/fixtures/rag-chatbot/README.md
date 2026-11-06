# Acme Support Bot (test fixture)

A small support chatbot that answers customer questions from product documents.
This project is a test fixture for the ai-architecture-and-reviewer skill. It contains deliberate
weaknesses. The model is a stub (`app/llm.py`), so everything runs offline.

Run the tests: `python -m pytest -q`
Try it: `python -m app.chat "What is the return window?"`
