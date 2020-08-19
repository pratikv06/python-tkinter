from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Structure")
root.iconbitmap('learning.ico')
root.geometry("400x400")

def graph():
    house_price = np.random.normal(200000, 25000, 5000)
    plt.hist(house_price, 50)
    plt.show()

my_btn = Button(root, text="Plot it!", command=graph)
my_btn.pack()

root.mainloop()