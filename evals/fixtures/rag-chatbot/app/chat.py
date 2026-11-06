"""Chat entry point."""
import json
import sys

from app import llm, prompts, retriever
from app.config import TEMPERATURE

HISTORY = []   # grows for the life of the process


def answer(question):
    chunks = retriever.retrieve(question)
    prompt = prompts.build(question, chunks, HISTORY)
    for _ in range(10):                      # retry until the output parses as JSON
        out = llm.complete(prompt, temperature=TEMPERATURE)
        try:
            json.loads(out)
            break
        except ValueError:
            continue
    HISTORY.append("Q: " + question)
    HISTORY.append("A: " + out)
    return out


if __name__ == "__main__":
    print(answer(" ".join(sys.argv[1:])))
