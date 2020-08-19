from tkinter import *
root = Tk()
root.title("Radio")

def clicked(value):
    result = Label(frame, text=value)
    result.pack()

# Radiobutton(root, text='Option 1', variable=r, value=1).pack()
# Radiobutton(root, text='Option 2', variable=r, value=2).pack()

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set('None')

for txt, val in TOPPINGS:
    Radiobutton(root, text=txt, variable=pizza, value=val).pack(anchor=W)

btn = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
btn.pack()

frame = LabelFrame(root, padx=10, pady=5)
frame.pack()

root.mainloop()