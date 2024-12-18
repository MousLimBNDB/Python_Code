import tkinter as tk
from tkinter import filedialog, messagebox, Text
import re

# The same functions you provided
month_map = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def extract_emails(text):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+(?:@|\[at\])[a-zA-Z0-9_.+-\[\]]+\.(?:com|org|co\.uk|edu)", text)
    return [re.sub(r"\[at\]", "@", email) for email in emails]

def extract_phone_numbers(text):
    tompolist = []
    numbers = re.findall(r"\+?\(?\b\d{0,4}\)?[-. ]?\(?\d{0,4}\)?[-. ]?\d{3,4}[-. ]?\d{3,4}\b", text)
    for number in numbers:
        if len(number) < 12:
            tompolist.append(number)
    for number in tompolist:
        numbers.remove(number)
    cleaned_numbers = []
    for number in numbers:
        index = len(number) - 5
        if number[index] in [" ", "-", "."]:
            cleaned_numbers.append(number[:index] + number[index + 1:])
        else:
            cleaned_numbers.append(number)
    normalized_numbers = []
    for number in cleaned_numbers:
        normalized_number = re.sub(r"[^\d]", " ", number)
        normalized_number = re.sub(r"\s+", " ", normalized_number).strip()
        normalized_number = f"+{normalized_number}"
        normalized_numbers.append(normalized_number)
    return normalized_numbers

def extract_dates(text):
    dates = re.findall(r"""\d{2,4}[/.-]\d{2}[/.-]\d{2,4}\b|
                       (?:(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*.*?\d{1,2}(?:st|nd|rd|th).*?\d{4})|
                       (?:(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday).*?\d{1,2}
                       (?:st|nd|rd|th).*?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*.*?\d{4})""", text, re.VERBOSE)
    return dates

def transform_dates(dates):
    transformed_dates = []
    for D in dates:
        if "/" in D:
            parts = re.split(r"/", D)
            if len(parts[0]) == 4:
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
        elif "." in D:
            parts = re.split(r"\.", D)
            if len(parts[0]) == 4:
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
        elif "-" in D:
            parts = re.split(r"-", D)
            if len(parts[0]) == 4:
                transformed = f"{parts[0]}-{parts[1]}-{parts[2]}"
            else:
                transformed = f"{parts[2]}-{parts[1]}-{parts[0]}"
        else:
            month_match = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)", D)
            if month_match:
                month = month_map[month_match.group(0)]
            day_match = re.search(r"\d{1,2}(?:st|nd|rd|th)?", D)
            year_match = re.search(r"\d{4}", D)
            if day_match and year_match:
                day = re.sub(r"(st|nd|rd|th)", "", day_match.group(0))
                year = year_match.group(0)
                transformed = f"{year}-{month}-{day}"
        transformed_dates.append(transformed)
    return transformed_dates

def validate_password(password):
    if len(password) < 8:
        return "The password is too short."
    if not re.findall(r"[A-Z]", password):
        return "Your password must contain at least one uppercase letter."
    if not re.findall(r"[a-z]", password):
        return "Your password must contain at least one lowercase letter."
    if not re.findall(r"[0-9]", password):
        return "Your password must contain at least one digit."
    if not re.findall(r'[!@#$%^&*.?]', password):
        return "Your password must contain at least one special character (!@#$%^&*)."
    return "You have a strong password."

def extract_hashtags(text):
    hashs = re.findall(r"#\w+", text)
    return hashs if hashs else "There are no hashtags."

# GUI Code
class TextProcessorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Processing GUI")
        self.root.geometry("600x400")

        # Text input area
        self.text_label = tk.Label(root, text="Input Text:")
        self.text_label.pack()
        self.text_area = tk.Text(root, height=10, width=70)
        self.text_area.pack()

        # Buttons for tasks
        self.email_button = tk.Button(root, text="Extract Emails", command=self.show_emails)
        self.email_button.pack(pady=5)

        self.phone_button = tk.Button(root, text="Extract Phone Numbers", command=self.show_phone_numbers)
        self.phone_button.pack(pady=5)

        self.dates_button = tk.Button(root, text="Extract Dates", command=self.show_dates)
        self.dates_button.pack(pady=5)

        self.password_button = tk.Button(root, text="Validate Password", command=self.validate_password)
        self.password_button.pack(pady=5)

        self.hashtags_button = tk.Button(root, text="Extract Hashtags", command=self.show_hashtags)
        self.hashtags_button.pack(pady=5)

        # Output area
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_area = tk.Text(root, height=10, width=70, state='disabled')
        self.output_area.pack()

    def display_output(self, output):
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', tk.END)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state='disabled')

    def show_emails(self):
        text = self.text_area.get("1.0", tk.END).strip()
        emails = extract_emails(text)
        self.display_output("\n".join(emails))

    def show_phone_numbers(self):
        text = self.text_area.get("1.0", tk.END).strip()
        phone_numbers = extract_phone_numbers(text)
        self.display_output("\n".join(phone_numbers))

    def show_dates(self):
        text = self.text_area.get("1.0", tk.END).strip()
        dates = extract_dates(text)
        transformed = transform_dates(dates)
        self.display_output("\n".join(transformed))

    def validate_password(self):
        password = self.text_area.get("1.0", tk.END).strip()
        result = validate_password(password)
        self.display_output(result)

    def show_hashtags(self):
        text = self.text_area.get("1.0", tk.END).strip()
        hashtags = extract_hashtags(text)
        self.display_output("\n".join(hashtags) if isinstance(hashtags, list) else hashtags)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TextProcessorGUI(root)
    root.mainloop()