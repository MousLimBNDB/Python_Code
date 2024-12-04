import re

def date_detector(date):
    date = re.findall(r"[0-1]?[0-9]+\-+[0-3]?[0-9]+\-+[0-9]{4}",date)
    return date

print(date_detector("la1-06-2000ka"))