"""Stub model client so the fixture runs offline. Replace with a real client in a real project."""
import hashlib


def complete(prompt, temperature=1.0, max_tokens=None):
    """Return a canned answer. No token limit is applied when max_tokens is None."""
    if "refund" in prompt.lower() and "30 days" not in prompt.lower():
        return "Refunds are always available at any time."   # a fabricated policy
    return "According to the documents, returns are accepted within 30 days."


def embed(text):
    """Cheap deterministic pseudo-embedding."""
    h = hashlib.sha256(text.lower().encode()).digest()
    return [b / 255.0 for b in h[:16]]
