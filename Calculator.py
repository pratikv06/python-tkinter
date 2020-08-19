from tkinter import *

root = Tk()
# Setting Title Bar Text
root.title("Simple Calculator")
# Setting Icon of the bar
root.iconbitmap('fav_calculator.ico')
# Fix size of canvas/Application
root.resizable(width=False, height=False)
# Set size of application
root.geometry("296x445")

''' Global Variable '''
f_num, maths = [None, None]

''' Function '''
def button_click(number):
    current_val = e.get()
    e.delete(0, END)
    e.insert(0, str(current_val) + str(number))

def button_add():
    global f_num 
    global maths
    maths = "Add"
    f_num = int(e.get())
    e.delete(0, END)

def button_sub():
    global f_num 
    global maths
    maths = "Sub"
    f_num = int(e.get())
    e.delete(0, END)

def button_mul():
    global f_num 
    global maths
    maths = "Mul"
    f_num = int(e.get())
    e.delete(0, END)

def button_div():
    global f_num 
    global maths
    maths = "Div"
    f_num = int(e.get())
    e.delete(0, END)

def button_equal():
    s_num = int(e.get())
    e.delete(0, END)

    if maths == "Add":
        e.insert(0, f_num + s_num)
    if maths == "Sub":
        e.insert(0, f_num - s_num)
    if maths == "Mul":
        e.insert(0, f_num * s_num)
    if maths == "Div":
        e.insert(0, f_num / s_num)

def button_clear():
    e.delete(0, END)

''' Display Text '''
e = Entry(root, width=37, borderwidth=5, font = "Helvetica 10 bold")
# Merging 3 column space in one: columnspan
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

''' Define Buttons '''
# To pass a value to the function use lambda function
button_1 = Button(root, text="1", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(1))
button_2 = Button(root, text="2", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(2))
button_3 = Button(root, text="3", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(3))
button_4 = Button(root, text="4", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(4))
button_5 = Button(root, text="5", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(5))
button_6 = Button(root, text="6", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(6))
button_7 = Button(root, text="7", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(7))
button_8 = Button(root, text="8", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(8))
button_9 = Button(root, text="9", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(9))
button_0 = Button(root, text="0", font = "Helvetica 10 bold", padx=40, pady=20, command=lambda : button_click(0))

button_add = Button(root, text="+", font = "Helvetica 10 bold", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", font = "Helvetica 10 bold", padx=40, pady=20, command=button_sub)
button_mul = Button(root, text="*", font = "Helvetica 10 bold", padx=40, pady=20, command=button_mul)
button_div = Button(root, text="/", font = "Helvetica 10 bold", padx=40, pady=20, command=button_div)

button_equal = Button(root, text="=", font = "Helvetica 10 bold", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", font = "Helvetica 10 bold", padx=78, pady=20, command=button_clear)

''' Displaying Buttons'''
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()