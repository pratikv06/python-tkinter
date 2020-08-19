from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Structure")
root.iconbitmap('learning.ico')

def show():
    label = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this Box, I Dare you!", variable=var, onvalue="On", offvalue="Off")
# For string it show select by default and return null value
c.deselect()
c.pack()
btn = Button(root, text="Show Selected", command=show).pack()


root.mainloop()