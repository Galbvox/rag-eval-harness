from rag_eval.scoring import score

items = [
        {"query": "How long will the delivery take?",
         "must_contain": ["delivery", "days"]}
    ]

def fake_search(query, k):
    return ["Delivery to remote areas may take up to 21 business days."]

def test_score_counts_hits():  
    hits, total = score(items, fake_search)
    assert hits == 1
    