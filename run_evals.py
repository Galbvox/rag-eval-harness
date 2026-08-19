#All push
#Does the system still find the right section?
#Optional breakpoint: Change in matching or chunk_text

import sys
from rag_eval.chunking import chunk_text
from rag_eval.search import make_search
from rag_eval.scoring import score, passed
import json


with open("evals/golden/corpus.txt") as f:
    corpus = f.read()
    
chunks = chunk_text(corpus, size=18)

search_fn = make_search(chunks)    

with open("evals/golden/questions.json") as f:
    items = json.load(f)

hits, total = score(items, search_fn, k=1)

ok = passed(hits, total, 0.5)


if ok:
    sys.exit(0)
else:
    sys.exit(1)