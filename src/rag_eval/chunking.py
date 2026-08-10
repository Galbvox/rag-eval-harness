


def chunk_text(text, size=200):
    sentences = text.split(".")
    chunks = []
    current = []
    total = 0
    for item in sentences:
        if total + count_words(item) > size:
            chunks.append(". ".join(current))
            current = []
            total = 0

        current.append(item.strip())
        total = total + count_words(item)

    if current:
        chunks.append(". ".join(current))


    return chunks






def count_words(words):
     return len(words.split())
    
    