import re 

def email_extractor(phrase):
    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[Cc][oO][Mm]" , phrase)
    return email

emails="mouslimbeneddeb@gmail.comisanemailcanyoudetectit?"
print(email_extractor(emails))