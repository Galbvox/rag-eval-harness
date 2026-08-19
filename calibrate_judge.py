#When invoking the judge model
#Does the judge itself still distinguish?

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
judge = make_judge(client)  

cases = [
    "Delivery takes 2 days for everyone.",
    "Free express shipping is included in all orders.",
    "Our store is open on Sunday.",
    "City deliveries arrive in three business days, while remote locations can take as long as three weeks."
]

query = "How long will the delivery take"
docs = search_fn(query, 3)

for answer in cases:
    verdict = judge(query, docs, answer)
    print("PASS" if verdict else "FAIL", "|", answer)
   
    


    


