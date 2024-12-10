import tkinter as tk
from tkinter import ttk, messagebox
import re

# Define functions for processing text
def extract_emails(text):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+(?:@|\[at\])[a-zA-Z0-9_.+-\[\]]+\.(?:com|org|co\.uk|edu)", text)
    return [re.sub(r"\[at\]", "@", email) for email in emails]

def extract_phone_numbers(text):
    numbers = re.findall(r"\+?\(?\b\d{0,4}\)?[-. ]?\(?\d{0,4}\)?[-. ]?\d{3,4}[-. ]?\d{3,4}\b", text)
    normalized_numbers = [re.sub(r"[^\d]", "", num) for num in numbers if len(re.sub(r"[^\d]", "", num)) >= 10]
    return [f"+{num}" for num in normalized_numbers]

def extract_dates(text):
    dates = re.findall(r"\d{2,4}[/.-]\d{2}[/.-]\d{2,4}", text)
    return dates

# Functions triggered by buttons
def display_emails():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        emails = extract_emails(text)
        result.set("\n".join(emails) if emails else "No emails found.")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

def display_phone_numbers():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        numbers = extract_phone_numbers(text)
        result.set("\n".join(numbers) if numbers else "No phone numbers found.")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

def display_dates():
    text = input_text.get("1.0", tk.END).strip()
    if text:
        dates = extract_dates(text)
        result.set("\n".join(dates) if dates else "No dates found.")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Initialize the main application window
root = tk.Tk()
root.title("Data Extraction Application")
root.geometry("600x500")

# Title Label
title_label = tk.Label(root, text="Data Extraction Application", font=("Arial", 16))
title_label.pack(pady=10)

# Text entry for user input
input_label = tk.Label(root, text="Enter your text below:", font=("Arial", 12))
input_label.pack(pady=5)

input_text = tk.Text(root, wrap="word", height=10, width=70)
input_text.pack(pady=10)

# Buttons for each task
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

email_button = ttk.Button(button_frame, text="Extract Emails", command=display_emails)
email_button.grid(row=0, column=0, padx=10)

phone_button = ttk.Button(button_frame, text="Extract Phone Numbers", command=display_phone_numbers)
phone_button.grid(row=0, column=1, padx=10)

dates_button = ttk.Button(button_frame, text="Extract Dates", command=display_dates)
dates_button.grid(row=0, column=2, padx=10)

# Display results
result_label = tk.Label(root, text="Results:", font=("Arial", 14))
result_label.pack(pady=5)

result = tk.StringVar()
result_display = tk.Label(root, textvariable=result, font=("Arial", 12), wraplength=550, justify="left")
result_display.pack(pady=10)

# Run the application
root.mainloop()
