from rag_eval.search import make_search


chunks = [
    "Refunds are issued within 14 days if the product is unused.",
    "Items damaged in shipping can be returned at any time.",
    "Store credit is offered when the original receipt is missing."
]


def test_make_search():
    test = make_search(chunks)
    docs = test("when do I get a refund?", 3)
    assert "Refunds" in docs[0]




