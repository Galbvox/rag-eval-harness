from rag_eval.chunking import chunk_text

def test_not_empty():
    chunks = chunk_text("First one. Second one.")
    assert len(chunks) > 0