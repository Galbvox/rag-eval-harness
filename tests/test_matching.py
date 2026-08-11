from rag_eval.matching import matches

def test_all_words_present():
    item = {"must_contain": ["refunds", "unused"]}
    assert matches(item, "Refunds within 14 days if unused.") is True

def test_one_of_present():
    item = {"must_contain_one_of": ["Monday", "Friday"]}
    assert matches(item, "Open Friday only.") is True

def test_missing_word_returns_false():
    item = {"must_contain": ["refunds", "unused"]}
    assert matches(item, "Refunds within 14 days.") is False

def test_unknown_key_returns_false():
    item = {"something_else": ["x"]}
    assert matches(item, "any text") is False