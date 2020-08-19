from tkinter import *

root = Tk()

# Define a function for button4 to perform
def myClick():
    msg = "Hello, " + e.get() + "..."
    myLabel = Label(root, text=msg)
    myLabel.pack()

# Create a entry i.e. input area
# setting width of the entry
# changing border width of the entry
e = Entry(root, width=50, borderwidth=10)
e.pack()
# Setting a default value of entry
e.insert(0, "Enter Something:")

myButton = Button(root, text="Click Me!", command=myClick)
myButton.pack()


root.mainloop()