import json
from rag_eval.chunking import chunk_text
from rag_eval.search import make_search
from rag_eval.scoring import score, passed, matches

with open("evals/golden/questions.json") as f:
    questions = json.load(f)

with open("evals/golden/corpus.txt") as f:
    corpus = f.read()

chunks = chunk_text(corpus, size=18)
search = make_search(chunks)

for item in questions:
    docs = search(item["query"], k=1)
    ok = any(matches(item, doc) for doc in docs)
    print(ok, "|", item["query"])
    print("   ", docs)