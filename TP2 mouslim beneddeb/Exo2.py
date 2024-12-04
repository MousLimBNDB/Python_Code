import re 

def all_digits(phrase):
    digits = re.findall(r"\d",phrase)
    print(digits)
    return digits

phrase1 = "C16A9417001D1JV21L"

all_digits(phrase1)