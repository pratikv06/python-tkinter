from tkinter import *
# import tkinter

root = Tk()

# Define a function for button4 to perform
def myClick():
    myLabel = Label(root, text="Look! I just clicked the Button... 😜😜😜")
    myLabel.pack()

myButton1 = Button(root, text="Click Me!")
myButton1.pack()

myButton2 = Button(root, text="Disabled", state=DISABLED)
myButton2.pack()

myButton3 = Button(root, text="Padded", padx=15, pady=15)
myButton3.pack()

# Note that in command while setting function we didn't use brackets
#  If we use bracket then the function will be automically called, aven without click
myButton4 = Button(root, text="Function", command=myClick)
myButton4.pack()

myButton5 = Button(root, text="Colors", fg='blue', bg='grey')
myButton5.pack()

root.mainloop()