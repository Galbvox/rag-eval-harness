#Closure = function that remember value from the created place
def search(query, k):
    words = query.lower().replace("?", " ").split()
    chunks = [
        "Refunds are issued within 14 days if the product is unused.",
        "Items damaged in shipping can be returned at any time.",
        "Store credit is offered when the original receipt is missing.",
        "Warranty claims require the serial number printed on the box.",
        "Delivery to remote areas may take up to 21 business days.",
    ]
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
    

    
            

search("How long will the delivery take?",1)
    