import tkinter as tk
from tkinter import messagebox , filedialog
import re

# The same functions that i did in the Homework2
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

class ElementExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Element Extractor GUI")
        self.root.geometry("600x700")

        self.title_label = tk.Label(root, text="Element extractor" , font=("Arial",24,"bold"))
        self.title_label.pack()
        
        # Text input area
        self.text_label = tk.Label(root, text="Input Text:")
        self.text_label.pack()
        self.text_area = tk.Text(root, height=10, width=70)
        self.text_area.pack()

        # Checkboxes
        self.checkbox_frame = tk.Frame(root)
        self.checkbox_frame.pack(pady=10)
        
        self.check_email = tk.IntVar()
        self.check_phone = tk.IntVar()
        self.check_dates = tk.IntVar()
        self.check_password = tk.IntVar()
        self.check_hashtags = tk.IntVar()

        self.email_check = tk.Checkbutton(self.checkbox_frame, text="Extract Emails", variable=self.check_email)
        self.email_check.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.phone_check = tk.Checkbutton(self.checkbox_frame, text="Extract Phone Numbers", variable=self.check_phone)
        self.phone_check.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.dates_check = tk.Checkbutton(self.checkbox_frame, text="Extract Dates", variable=self.check_dates)
        self.dates_check.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.password_check = tk.Checkbutton(self.checkbox_frame, text="Validate Password", variable=self.check_password)
        self.password_check.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.hashtags_check = tk.Checkbutton(self.checkbox_frame, text="Extract Hashtags", variable=self.check_hashtags)
        self.hashtags_check.grid(row=2, column=0, padx=10, pady=5, sticky="w", columnspan=2)

        # Frame for Process and Open File buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Process button
        self.process_button = tk.Button(self.button_frame, text="Process", command=self.process_text)
        self.process_button.grid(row=0, column=0, padx=10)

        # File open button
        self.file_button = tk.Button(self.button_frame, text="Open File", command=self.open_file)
        self.file_button.grid(row=0, column=1, padx=10)

        # Output area
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_area = tk.Text(root, height=15, width=70, state='disabled')
        self.output_area.pack()

    def display_output(self, output):
        self.output_area.config(state='normal')
        self.output_area.delete('1.0', tk.END)
        self.output_area.insert(tk.END, output)
        self.output_area.config(state='disabled')

    def process_text(self):
        text = self.text_area.get("1.0", tk.END).strip()
        output = ""

        if self.check_email.get():
            emails = extract_emails(text)
            output += "### Extracted Emails:\n" + "\n".join(emails) + "\n\n"

        if self.check_phone.get():
            phone_numbers = extract_phone_numbers(text)
            output += "### Extracted Phone Numbers:\n" + "\n".join(phone_numbers) + "\n\n"

        if self.check_dates.get():
            dates = extract_dates(text)
            transformed = transform_dates(dates)
            output += "### Extracted and Transformed Dates:\n" + "\n".join(transformed) + "\n\n"

        if self.check_password.get():
            result = validate_password(text)
            output += "### Password Validation Result:\n" + result + "\n\n"

        if self.check_hashtags.get():
            hashtags = extract_hashtags(text)
            if isinstance(hashtags, list):
                output += "### Extracted Hashtags:\n" + ", ".join(hashtags) + "\n\n"
            else:
                output += "### Extracted Hashtags:\n" + hashtags + "\n\n"

        if not output:
            messagebox.showinfo("No Selection", "Please select at least one option to process.")
        else:
            self.display_output(output)
            
    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert(tk.END, file_content)
                self.process_text()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ElementExtractorGUI(root)
    root.mainloop()