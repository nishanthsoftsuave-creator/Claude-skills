"""Prompt construction."""

SYSTEM = "You are a helpful assistant. Answer using the context."


def build(question, chunks, history):
    # the user's text is concatenated straight into the instructions, with no delimiter
    return (
        SYSTEM + " The customer says: " + question + "\n\nContext:\n" + "\n".join(chunks)
        + "\n\nHistory:\n" + "\n".join(history)
    )
