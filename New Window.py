from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Main Window")
root.iconbitmap('learning.ico')

def open():
    # For some reason image is not loaded
    # So make it global as it was define in root 
    # So we can use it in top
    global my_img
    top = Toplevel()
    top.title("New Window")
    top.iconbitmap('learning.ico')
    my_img = ImageTk.PhotoImage(Image.open('images/Image1.jpg'))
    label1 = Label(top, image=my_img).pack()
    label2 = Label(top, text="Image: Code Snip")
    label2.pack()
    # with quit main window will also close
    btn2 = Button(top, text="Close", command=top.destroy)
    btn2.pack()



btn = Button(root, text="Open New Window", command=open)
btn.pack()


root.mainloop()