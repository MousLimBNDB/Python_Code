import tkinter

def greeting ():
    name = txtField.__getstate__
    if name == "":
        printLbl.configure(text="Hello, Guest! Welcome!")
        return f"Hello, Guest! Welcome!"
    else:
        printLbl.configure(text=f"Hello, {name}! Welcome!")
        return f"Hello, {name}! Welcome!"
root = tkinter.Tk()
root.title("Practical Section - Tkinter")
root.geometry("600x400")
lbl = tkinter.Label(root, text="Welcome to Tkinter Practical Section!",font=("Arial",16))
lbl.pack(expand=True)
printLbl = tkinter.Label(root, text="")
printLbl.pack(expand=True)
txtField = tkinter.Entry(root,borderwidth=2,width=50)
txtField.pack(expand=True)
btn = tkinter.Button(root, text="Submit", command = greeting)
btn.pack(expand=True)
root.mainloop()


