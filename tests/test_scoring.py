from rag_eval.scoring import score, passed

items = [
        {"query": "How long will the delivery take?",
         "must_contain": ["delivery", "days"]}
    ]

def fake_search(query, k):
    return ["Delivery to remote areas may take up to 21 business days."]

def test_score_counts_hits():  
    hits, total = score(items, fake_search)
    assert hits == 1
    
def test_score_Success():  
    test = passed(3, 3, 0.6)
    assert test is True

def test_score_Failed():  
    test = passed(1, 3, 0.6)
    assert test is False

import pytest
    
def test_score_raise():  
    with pytest.raises(ValueError):
        passed(0, 0, 0.6)

    