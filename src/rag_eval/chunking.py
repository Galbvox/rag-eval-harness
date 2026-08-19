
def chunk_text(text, size=200):
    sentences = text.split(".")
    chunks = []
    current = []
    total = 0
    for item in sentences:
        if not item.strip():
            continue
        if count_words(item) > size:
            raise ValueError("sentence longer than size")
        if total + count_words(item) > size:
            chunks.append(". ".join(current) + ".")
            current = []
            total = 0

        current.append(item.strip())
        total = total + count_words(item)

    if current:
        chunks.append(". ".join(current) + ".")

    return chunks


# מה הוא מחזיר כשה
#item 
# בלי אף מפתח מוכר, ולמה זו בעיה?
# תשובה: מחזיר None - אין תשובה. תאונה
#None נוצר
#כשפונקציה נופלת מהסוף בלי return

#הערה: אם מקבלים False: אז הקורא מבין ש לא התאמה. החלטה
#ולכן - ב-if שניהם מתנהגים אותו דבר — ולכן זה כישלון שקט.





def count_words(words):
     return len(words.split())
    
    