import math


def make_bm25_search(chunks):
    doc_freq = build_idf(chunks)
    total = len(chunks)
    avg_len = sum(len(c.split()) for c in chunks) / len(chunks)

    def search(query, k):
        words = query.lower().replace("?", " ").split()  
        scored = []
        for chunk in chunks:
            chunk_words = chunk.lower().replace(".", " ").replace("?", " ").split()
            score = 0
            for word in words:
                count = chunk_words.count(word)
                score += idf(word, doc_freq, total) * tf_score(count, len(chunk_words), avg_len)
            scored.append((score, chunk))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [chunk for score, chunk in scored[:k]]
    return search



def build_idf(chunks):
    doc_freq = {}
    for chunk in chunks:
            words = chunk.lower().replace(".", " ").split()
            for word in set(words):
                doc_freq[word] = doc_freq.get(word, 0) + 1
                    
    return doc_freq



def idf(word, doc_freq, total_chunks):
    df = doc_freq.get(word, 0)
    return math.log((total_chunks - df + 0.5) / (df + 0.5) + 1)


def tf_score(count, doc_len, avg_len, k1=1.5, b=0.75):
    norm = 1 - b + b * (doc_len / avg_len)
    return (count * (k1 + 1)) / (count + k1 * norm)


if __name__ == "__main__":
    chunks = ["a b b", "b c", "b d"]
    s = make_bm25_search(chunks)
    print(s("a", 1))
    print(s("c", 1))