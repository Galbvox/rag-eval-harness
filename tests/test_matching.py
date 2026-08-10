from rag_eval.matching import matches

def test_all_words_present():
    item = {"must_contain": ["refunds", "unused"]}
    assert matches(item, "Refunds within 14 days if unused.") is True

def test_one_of_present():
    item = {"must_contain_one_of": ["Monday", "Friday"]}
    assert matches(item, "Open Friday only.") is True