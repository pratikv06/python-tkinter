# Everything is widget
# Importing tkinter package
from tkinter import *

# Creating a MainFrame
root = Tk()

# Creating a label Widget   
myLabel = Label(root, text="Hello Python!")
# Displaying label on screen
myLabel.pack()

# Running the MainFrame
root.mainloop()