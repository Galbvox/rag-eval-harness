import sys

from rag_eval.matching import matches
# [
#     {"query": "what is the return policy?", "must_contain": ["refunds", "unused"]},
#     {"query": "What kind of warranty does it come with?", "must_contain": ["Warranty", "serial", "number"]},
#     {"query": "How long will the delivery take?", "must_contain": ["Delivery", "days"]}

# ]
#item is golden
def score(items, search_fn, k=3) -> tuple:
    """calculate the hits of docs from search_fn on items (golden sets)
    Args:
        items (list[dict]): golden set rules from question.json
        search_fn (callable): takes (query, k), returns list[str]
        k (int, optional): get the top match k
    Returns:
        tuple: hits + total of items in golden set
    """
    hits = 0
    total = len(items)
    
    for item in items:
        query = item["query"]
        docs = search_fn(query, k) #some docs   like Func<string, int, List<string>> in c#
        for doc in docs:
            if matches(item, doc):
                hits+=1
                break
            
    print(f"recall@{k}: {hits}/{total}")
    return hits,total

def passed(hits, total, min_score):
   if total == 0:
    raise ValueError("empty golden set")
   
   rat = hits / total  
   return rat >= min_score
    
    