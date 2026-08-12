#Closure = function that remember value from the created place
def make_search(chunks):
    def search(query, k):
        words = query.lower().replace("?", " ").split()  
        scored = []    
        for chunk in chunks:
            count = 0
            for word in words:
                if word in  chunk.lower().replace(".", " ").replace("?", " ").split():
                    count = count + 1
            
            scored.append((count, chunk))
        scored.sort(reverse=True)
        result = [chunk for count, chunk in scored[:k]]
        return result
    return search
    

    
            

    