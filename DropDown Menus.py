from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Structure")
root.iconbitmap('learning.ico')
root.geometry("400x400")

def show():
    label1 = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Select Day")
# drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday")

days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]
drop = OptionMenu(root, clicked, *days)
drop.pack()

btn = Button(root, text="Submit", command=show).pack()

root.mainloop()