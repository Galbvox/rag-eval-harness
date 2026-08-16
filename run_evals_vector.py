import sys
from rag_eval.vector_search import make_vector_search
from rag_eval.scoring import score, passed
import json

from dotenv import load_dotenv
import os

import psycopg
from sentence_transformers import SentenceTransformer

load_dotenv(override=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

conn = psycopg.connect(
    host="localhost",
    port=5435,            
    dbname="postgres",
    user="postgres",
    password=os.getenv("PG_PASSWORD"),
)    


search_fn = make_vector_search(conn, model)    

with open("evals/golden/questions.json") as f:
    items = json.load(f)

hits, total = score(items, search_fn, k=1)

ok = passed(hits, total, 0.5)


if ok:
    sys.exit(0)
else:
    sys.exit(1)