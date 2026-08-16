import os
from dotenv import load_dotenv
import psycopg
from anthropic import Anthropic
from sentence_transformers import SentenceTransformer

from rag_eval.vector_search import make_vector_search
from rag_eval.generation import make_generator

print("1 imports ok")

load_dotenv(override=True)

model = SentenceTransformer("all-MiniLM-L6-v2")
print("2 model ok")

client = Anthropic()
print("3 client ok")

conn = psycopg.connect(
    host="localhost",
    port=5435,
    dbname="postgres",
    user="postgres",
    password=os.getenv("PG_PASSWORD"),
)
print("4 conn ok")

search_fn = make_vector_search(conn, model)
generate = make_generator(client)

query = "How long will the delivery take?"

docs = search_fn(query, 3)
print("5 search ok")

answer = generate(query, docs)
print("6 generate ok")

print()
print("QUERY:", query)
for d in docs:
    print("  DOC:", d[:70])
print()
print("ANSWER:", answer)