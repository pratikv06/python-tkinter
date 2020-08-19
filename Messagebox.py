from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")

# showinfo (return: ok), showwarning (return: ok), showerror (return: ok), 
# askquestion (return: YES/NO), askokcancel (return: bool), askyesno (return: bool)
def popup():
    response = messagebox.askokcancel("ShowInfo!!!", "This is a Popup\nSample of Popup")
    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()
root.mainloop()