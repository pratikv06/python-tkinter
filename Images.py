from tkinter import *
from PIL import ImageTk, Image
# PIL - Pillow use for images 

root = Tk()

# Description 
root.title('Gallery')
root.iconbitmap('fav_gallery.ico')

# Loading Images
my_img = ImageTk.PhotoImage(Image.open('Image1.jpg').resize((600, 400)))
my_imglabel = Label(image=my_img)
my_imglabel.pack()

# Exit Button
btn_exit = Button(root, text='Exit Program', command=root.quit)
btn_exit.pack()

root.mainloop()