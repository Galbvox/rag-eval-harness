from dotenv import load_dotenv
import os

import psycopg
from sentence_transformers import SentenceTransformer
from rag_eval.chunking import chunk_text

load_dotenv(override=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

conn = psycopg.connect(
    host="localhost",
    port=5435,            
    dbname="postgres",
    user="postgres",
    password=os.getenv("PG_PASSWORD"),
)

cur = conn.cursor()


with open("evals/golden/curpuswithdeps.txt") as f:
    corpus = f.read()

chunks = chunk_text(corpus, size=18)

vectors = model.encode(chunks)

cur.execute("TRUNCATE chunks")

for chunk, vec in zip(chunks, vectors):
    cur.execute(
        "INSERT INTO chunks (content, embedding) VALUES (%s, %s)",
        (chunk, vec.tolist()),
    )

conn.commit()

print(len(chunks), vectors.shape)