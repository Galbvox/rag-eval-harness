# {"must_contain": ["warranty", "refunds"]}
# {"query": "...", "must_contain": ["warranty", "refunds"]}
# chunk = "Refunds within 14 days if unused."

def matches(item, chunk):
    # item = dict. text = ה-chunk. מחזירה True או False.
    text = chunk.lower()
    if "must_contain" in item:
        for w in item["must_contain"]:
            if w.lower() not in text:
                return False
        return True