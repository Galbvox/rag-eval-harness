IGNORED = ["the", "is", "that", "a", "of", "what"]

def make_search(chunks):
    def search(query, k):
        words = query.lower().replace("?", " ").split()  
        scored = []    
        for chunk in chunks:
            count = 0
            chunk_words = chunk.lower().replace(".", " ").replace("?", " ").split()
            for word in words:
                if word in IGNORED:
                    continue
                for cw in chunk_words:                 
                    if cw.startswith(word):
                       count = count + 1
                       break
            
            scored.append((count, chunk))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        result = [chunk for count, chunk in scored[:k]]
        return result
    return search