from tkinter import *

root = Tk()

def myClick():
    msg = "Hello, " + e.get() + "..."
    myLabel = Label(root, text=msg)
    myLabel.pack()

# changing font of the text: f_family f_size f_style
e = Entry(root, width=50, borderwidth=10, font = "Helvetica 16 normal")
e.pack()
e.insert(0, "Enter Something:")
# e.config(state=DISABLED)
# Removing the default text after mouse click 
# Deleting entry value
e.bind("<FocusIn>", lambda args: e.delete('0','end'))

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()


root.mainloop()