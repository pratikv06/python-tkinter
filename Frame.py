'''
pack with Pack or grid with Grid
Here, frame is pack but it inner element can be used with grid

'''


from tkinter import *
root = Tk()
root.title("Frame")

frame = LabelFrame(root, text="This is a frame...", padx=15, pady=15) # Padding from frame, inner element
frame.pack(padx=50, pady=50) # padding from root, for frame

btn1 = Button(frame, text="Submit")
btn1.grid(row=0, column=0)

btn2 = Button(frame, text="Reset")
btn2.grid(row=1, column=1)

frame2 = LabelFrame(root, padx=100, pady=100)
frame2.pack(padx=10, pady=10)

btn3 = Button(frame2, text="Cancel")
btn3.pack()
root.mainloop()