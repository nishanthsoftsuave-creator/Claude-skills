"""Split documents into chunks."""
from app.config import CHUNK_SIZE


def chunk(text):
    # fixed-size slices: can cut sentences in half, no overlap, no structure awareness
    return [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
