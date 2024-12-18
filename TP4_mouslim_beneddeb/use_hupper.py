import tkinter as tk
import hupper


def main():
    root = tk.Tk()
    # root.geometry("500x500")
    root.geometry("500x500+3300+100")
    root.title("my gui")

    label =tk.Label(root,text="hello world",font=("arial",18))
    label.pack(padx=20, pady=50)

    text = tk.Text(root, height=5, font=("arial", 16))
    text.pack(padx=10)
    
    # myentry = tk.Entry(root)
    # myentry.pack()

    root.mainloop()



    
if __name__ == "__main__":
    hupper.start_reloader("basics.main")
    main()

