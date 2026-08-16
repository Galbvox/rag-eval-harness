from dotenv import load_dotenv

from rag_eval.chunking import chunk_text

load_dotenv(override=True)


def make_vector_search(conn, model):
    def search(query, k):
        
        cur = conn.cursor()
        query_vec = model.encode(query).tolist()
        
        cur.execute(
        "SELECT content FROM chunks ORDER BY embedding <=> %s::vector LIMIT %s",
        (query_vec, k),
      )
        rows  = cur.fetchall()
        return [r[0] for r in rows]         

    return search


