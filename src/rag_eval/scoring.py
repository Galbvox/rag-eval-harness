from rag_eval.matching import matches
# [
#     {"query": "what is the return policy?", "must_contain": ["refunds", "unused"]},
#     {"query": "What kind of warranty does it come with?", "must_contain": ["Warranty", "serial", "number"]},
#     {"query": "How long will the delivery take?", "must_contain": ["Delivery", "days"]}

# ]
def score(items, search_fn, k=3) -> tuple:
    hits = 0
    total = len(items)
    
    for item in items:
        query = item["query"]
        docs = search_fn(query, k)
        for doc in docs:
            if matches(item, doc):
                hits+=1
                break
            
    print(f"recall@{k}: {hits}/{total}")
    return hits,total
    