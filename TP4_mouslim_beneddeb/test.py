from tkinter import *
from PIL import Image , ImageTk


window = Tk() # instantiate an interface of a window
window.geometry("420x420")
window.title("mouslim first gui program")# set the title of the window

# icon of the window
icon_image = Image.open("TP4 mouslim beneddeb\icon.png")
icon = ImageTk.PhotoImage(icon_image)
window.iconphoto(True,icon)

window.config(background="#85A98F")

label = Label(window,text="hello world",font=("arial,"))
# label.place(x=0,y=0)
label.pack()# place it in top center of the window


window.mainloop()