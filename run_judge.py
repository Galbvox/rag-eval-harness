import os
from dotenv import load_dotenv
import psycopg
import json

from anthropic import Anthropic
from sentence_transformers import SentenceTransformer

from rag_eval.vector_search import make_vector_search
from rag_eval.generation import make_generator
from rag_eval.judge import make_judge


load_dotenv(override=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

client = Anthropic()

conn = psycopg.connect(
    host="localhost",
    port=5435,
    dbname="postgres",
    user="postgres",
    password=os.getenv("PG_PASSWORD"),
)

search_fn = make_vector_search(conn, model)
generate = make_generator(client)
judge = make_judge(client)

with open("evals/golden/questions.json") as f:
    items = json.load(f)
    
hits = 0
total = len(items)
for item in items:
    query = item["query"]
    docs = search_fn(query, 3)
    answer = generate(query, docs)
    verdict = judge(query, docs, answer)
    if verdict:
        hits += 1
    print("PASS" if verdict else "FAIL", "|", query)
    
print("hits: ", hits, "total: ", total)

