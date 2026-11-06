from app.chunker import chunk


def test_chunk_splits_text():
    assert len(chunk("a" * 450)) == 3
