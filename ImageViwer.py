from tkinter import *
from PIL import ImageTk, Image
# PIL - Pillow use for images 

root = Tk()

''' Description ''' 
root.title('Image Viewer')
root.iconbitmap('fav_gallery.ico')

''' Functions '''
def forward(image_number):
    global my_label 
    global btn_left 
    global btn_right

    # Removing Old Images
    my_label.grid_forget()

    # Loading New Images
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)
    
    # Updating Forward Button
    btn_right = Button(root, text='>>', command= lambda: forward(image_number+1))
    # Last Image - Disable Button
    if image_number == len(image_list):
        btn_right = Button(root, text='>>', state=DISABLED)
    btn_right.grid(row=1, column=2)
    
    # Updating Backward Button
    btn_left = Button(root, text='<<', command=lambda: backward(image_number-1))
    btn_left.grid(row=1, column=0)
    
    # Updating Status Bar
    status = Label(root, text='Image '+ str(image_number) +' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)

def backward(image_number):
    global my_label 
    global btn_left 
    global btn_right

    # Removing Old Images
    my_label.grid_forget()
    # Loading New Images
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=3)
    
    # Updating Forward Button
    btn_right = Button(root, text='>>', command= lambda: forward(image_number+1))
    btn_right.grid(row=1, column=2)
    
    # Updating Backward Button
    btn_left = Button(root, text='<<', command=lambda: backward(image_number-1))
    # First Image - Disable Button
    if image_number == 1:
        btn_left = Button(root, text='<<', state=DISABLED)
    btn_left.grid(row=1, column=0)

    # Updating Status Bar
    status = Label(root, text='Image '+ str(image_number) +' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=3, column=0, columnspan=3, sticky=W+E)

''' Loading Images '''
my_img1 = ImageTk.PhotoImage(Image.open('Images/Image1.jpg').resize((400, 250)))
my_img2 = ImageTk.PhotoImage(Image.open('Images/Image2.jpg').resize((400, 250)))
my_img3 = ImageTk.PhotoImage(Image.open('Images/Image3.jpg').resize((400, 250)))
my_img4 = ImageTk.PhotoImage(Image.open('Images/Image4.jpg').resize((400, 250)))

image_list = [my_img1, my_img2, my_img3, my_img4]
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

''' Buttom Buttons ''' 
btn_left = Button(root, text='<<', command=backward, state=DISABLED)
btn_right = Button(root, text='>>', command= lambda: forward(2))
btn_exit = Button(root, text='Exit Program', command=root.quit)

''' Status Bar '''
status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

''' Button Display '''
btn_left.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_right.grid(row=1, column=2, pady=2)

status.grid(row=3, column=0, columnspan=3, sticky=W+E)

root.mainloop()