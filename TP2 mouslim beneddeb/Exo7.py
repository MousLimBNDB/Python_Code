import re

def cap_let_word (string):
    words = re.findall(r'\b[A-Z][a-zA-Z]*\b',string)
    if not words:
        print("thers is no words with a capitale latter")
        return 0
    else:
        print(f"your word/s are : {words}")
        return words
    
cap_let_word("mqdflm ljkdhfl Lsfb")