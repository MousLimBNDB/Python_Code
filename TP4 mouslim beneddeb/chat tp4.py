import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Practical Section - Tkinter")
root.geometry("600x400")

# Function to handle button click
def on_submit():
    name = name_entry.get().strip()  # Get the text from the Entry field
    if name:
        greeting_label.config(text=f"Hello, {name}! Welcome!")
    else:
        greeting_label.config(text="Hello, Guest! Welcome!")

# Create and place widgets
# Label: Welcome text
welcome_label = tk.Label(
    root,
    text="Welcome to Tkinter Practical Section!",
    font=("Arial", 16)
)
welcome_label.pack(pady=20)

# Entry: Text input for name
name_entry = ttk.Entry(root, width=40)
name_entry.pack(pady=10)

# Button: Submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Label: Greeting message (initially empty)
greeting_label = tk.Label(root, text="", font=("Arial", 14))
greeting_label.pack(pady=20)

# Run the application
root.mainloop()
