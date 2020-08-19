from tkinter import *

root = Tk()
 
myLabel1 = Label(root, text="Hello Python!")
myLabel2 = Label(root, text="Hello TKinter!")
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

Label(root, text="Directly using grid with Label").grid(row=2, column=2)

root.mainloop()