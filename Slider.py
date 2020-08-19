from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Structure")
root.iconbitmap('learning.ico')
root.geometry("200x200")

def frame_geometry(v, h):
    msg = str(v) +"x"+ str(h)
    root.geometry(msg)

vertical = Scale(root, from_=200, to=500)
vertical.pack()

horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL)
horizontal.pack()

btn = Button(root, text="Submit", command=lambda: frame_geometry(vertical.get(), horizontal.get())).pack()

root.mainloop()