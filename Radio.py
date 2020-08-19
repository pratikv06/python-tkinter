from tkinter import *
root = Tk()
root.title("Radio")

def clicked(value):
    result = Label(root, text=value)
    result.pack()


r = IntVar()
# Initlizing Variable - Default = 0
r.set(3)
# Reterive value - r.get()

Radiobutton(root, text='Option 1', variable=r, value=1).pack()
Radiobutton(root, text='Option 2', variable=r, value=2).pack()

btn = Button(root, text="CLick Me!", command=lambda: clicked(r.get()))
btn.pack()

root.mainloop()