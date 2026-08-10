from rag_eval.chunking import chunk_text

def test_not_empty():
    chunks = chunk_text("First one. Second one.")
    assert len(chunks) > 0

def test_ends_with_period():
    chunks = chunk_text("First one. Second one.")
    for c in chunks:
        assert c.endswith(".")

import pytest

def test_long_sentence_raises():
    with pytest.raises(ValueError):
        chunk_text("one two three four five", size=3)