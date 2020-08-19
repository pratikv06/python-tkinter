from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open File")
root.iconbitmap('learning.ico')

def open_file():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="D:\Pratik\Study\Python\Python Tkinter\Images", title="Open a File...", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("jpeg Files", "*.jpeg"), ("All Files", "*.*")))
    label1 = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    label2 = Label(image=my_img).pack()

btn1 = Button(root, text="Open Image", command=open_file).pack()


root.mainloop()