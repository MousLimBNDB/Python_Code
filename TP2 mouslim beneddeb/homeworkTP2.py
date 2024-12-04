import re

with open("TP2 mouslim beneddeb\\text.txt", 'r') as file:
    test = file.read()

month_map = {
"January": "01", "February": "02", "March": "03", "April": "04",
"May": "05", "June": "06", "July": "07", "August": "08",
"September": "09", "October": "10", "November": "11", "December": "12"}

#Task 1: Extract and Normalize Emails
def extract_emails(text):

    emails = re.findall(r"[a-zA-Z0-9_.+-]+(?:@|\[at\])[a-zA-Z0-9_.+-\[\]]+\.(?:com|org|co\.uk|edu)" , text)
    #The normalization part of the email
    convert =[] 
    for email in emails:
        convert.append(re.sub(r"\[at\]","@",email))
    return convert

#Task 2: Extract and Normalize Phone Numbers
def extract_phone_numbers(text):
    tompolist = []  #This list is to separate the phone numbers from the date numbers 
    numbers = re.findall(r"\+?\(?\b\d{0,4}\)?[-. ]?\(?\d{0,4}\)?[-. ]?\d{3,4}[-. ]?\d{3,4}\b", text)
    for number in numbers: #A phone number have at least 12 numbers
        if len(number) < 12 : 
            tompolist.append(number)
    for number in tompolist: #This loop is to remove the the dates from the phone nuber list
        numbers.remove(number)
    tompolist.clear # To clear the list and use it here 
    # To separate the area code
    for number in numbers:
        index = len(number) - 5
        if number[index] in [" ","-","."]:
            tompolist.append(number[:index] + number[index+1:])
        else :
            tompolist.append(number)
    numbers = tompolist #To put phone numbers with the area code format  
    tompolist.clear #To clear it again 
    for number in numbers:
        # Replaces any non-numeric character with a space
        normalized_number = re.sub(r"[^\d]", " ", number)
        # Remove any extra spaces
        normalized_number = re.sub(r"\s+", " ", normalized_number).strip()
        # Add a '+' at the beginning
        normalized_number = f"+{normalized_number}"
        tompolist.append(normalized_number)
    return tompolist

# Task 3: Extract and Transform Dates
def extract_dates(text):
    dates = re.findall(r"""\d{2,4}[/.-]\d{2}[/.-]\d{2,4}\b|
                       (?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*.*?\d{1,2}(?:st|nd|rd|th).*?\d{4})|
                       (?:(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday).*?\d{1,2}
                       (?:st|nd|rd|th).*?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*.*?\d{4})""",text)
    
    return dates

def transform_dates(date):
    transformed_dates = []
    for D in date:
        if "/" in D:#The case where the separator is /
            parts = re.split(r"/",D)
            if len(parts[0]) == 4:  # YYYY/MM/DD
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:  # DD/MM/YYYY
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
                
        elif "." in D:#The sepataror .
            parts = re.split(r"\.",D)
            if len(parts[0]) == 4:  # YYYY/MM/DD
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:  # DD/MM/YYYY
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
                
        elif "-" in D:#The separator is-
            parts = re.split(r"-",D)
            if len(parts[0]) == 4:  # YYYY/MM/DD
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:  # DD/MM/YYYY
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
        else:#The case where the date is a sentence
            #To extract the month parte and transform it a numeric format
            month_match = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)", D)
            if month_match:
                month = month_map[month_match.group(0)] 
            #To extract the day part
            day_match = re.search(r"\d{1,2}(?:st|nd|rd|th)?", D)
            #To extract the year part
            year_match = re.search(r"\d{4}", D)
            #To transform the year and day to the right format and assemble them to one single variable
            if day_match and year_match:
                day = re.sub(r"(st|nd|rd|th)", "", day_match.group(0))  # Remove suffixes
                year = year_match.group(0)
                transformed = f"{year}-{month}-{day}"
        transformed_dates.append(transformed)

    return transformed_dates

# Task 4: Password Validation
def validate_password(password):
    
    if len(password) < 8 : #Testing the length of the password
        print("the password is too short")
        return False
    
    if not re.findall(r"[A-Z]",password): #Testing if there is at least one uppercase letter
        print("your password must Contain at least one uppercase letter")
        return False
    
    if not re.findall(r"[a-z]",password): #Testing if the is at least one lowercase letter
        print("your password must Contain at least one lowercase letter")
        return False
    
    if not re.findall(r"[0-9]",password): #Testing if there is any digits 
        print("your password must Contain at least one digit")
        return False

    if not re.findall(r'[!@#$%^&*.?]', password): #Testing if there is a special character
        print("your password must Contain at least one special character (!@#$%^&*)")
        return False
    else:#in case the password meets the criteria we return True
        print("you have a strong password")
        return True

# Task 5: Extract Hashtags
def extract_hashtags(text):
    hashs = re.findall(r"#\w+",text)
    if not hashs:# in case there is no hashtags in the given text
        print("thers is no hashtages")
        return 0
    else:
        print(f"your hashtage/s are : {hashs}")
        return hashs

#Bonus Task: Extract Important Dates
def find_upcoming_events(text, year):
    year = str(year)
    #To extract events with in a sentence
    eventTextDates = re.finditer(r"(?P<event>[Mm]eet|[Tt]ask|[Dd]eadline).*?(?P<date>\d\d.*?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*.*?\d{4})\b",text)
    #To extract events with numeric dates
    eventRegulareDates = re.finditer(r"(?P<event>[Mm]eet|[Tt]ask|[Dd]eadline).*?(?P<date>\d{2,4}[/.-]\d{2}[/.-]\d{2,4})\b",text)
    #To assemble the types of events  
    event = []
    for match in eventTextDates:
        event.append(match)
    for match in eventRegulareDates:
        event.append(match)
    #To split the type of event an the date
    final_event_list = []
    for match in event:
        event = match.group("event").strip()
        date = match.group("date")
        
        #To normalize the dates into YYYY-MM-DD format
        normalized_date = None
        if re.match(r"\d{4}[/.-]\d{2}[/.-]\d{2}", date):  # YYYY/MM/DD
            normalized_date = re.sub(r"[/.]", "-", date)
        elif re.match(r"\d{2}[/.-]\d{2}[/.-]\d{4}", date):  # DD/MM/YYYY
            day, month, year_val = re.split(r"[/.]", date)
            normalized_date = f"{year_val}-{month}-{day}"
        elif re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)", date):
            day = re.search(r"\d{1,2}(?:st|nd|rd|th)?", date).group()
            day = re.sub(r"(st|nd|rd|th)", "", day)  # Remove ordinal suffix
            month = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)", date).group()
            year_val = re.search(r"\d{4}", date).group()
            normalized_date = f"{year_val}-{month_map[month]}-{day}"
        #Testing if the year event match the given year and adding into the final list
        if year_val == year:
            final_event_list.append({"event": event, "date": normalized_date})
    
    return final_event_list


#To test every 

print(extract_dates(test))


