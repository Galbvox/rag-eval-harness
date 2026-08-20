import json
from rag_eval.chunking import chunk_text
from rag_eval.bm25 import make_bm25_search
from rag_eval.scoring import matches

with open("evals/golden/questions.json") as f:
    questions = json.load(f)

with open("evals/golden/corpus.txt") as f:
    corpus = f.read()

chunks = chunk_text(corpus, size=18)
search = make_bm25_search(chunks)

for item in questions:
    docs = search(item["query"], k=1)
    ok = any(matches(item, doc) for doc in docs)
    print(ok, "|", item["query"])
    print("   ", docs)