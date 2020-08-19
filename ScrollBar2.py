from tkinter import * 

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


root = Tk()

# --- create canvas with scrollbar ---
canvas = Canvas(root, width=400, height=400)
canvas.pack(side=LEFT)

scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---
frame = Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- add widgets in frame ---
frame1 = LabelFrame(frame, text="www.facebook.com", padx=20, pady=10)
frame1.grid(row=0)
Label(frame1, text="Userid: pratik@gmail.com").grid(row=0, sticky=W)
Label(frame1, text="Password: pratik").grid(row=1, sticky=W)
Button(frame1, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
Button(frame1, text="Delete").grid(padx=15, row=0, column=2, rowspan=2)

frame2 = LabelFrame(frame, text="www.github.com", padx=20, pady=10)
frame2.grid(row=1)
Label(frame2, text="Userid: pratik@gmail.com").grid(row=0, sticky=W)
Label(frame2, text="Password: githubpratik").grid(row=1, sticky=W)
Button(frame2, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
Button(frame2, text="Delete").grid(padx=15, row=0, column=2, rowspan=2)

frame3 = LabelFrame(frame, text="www.gmail.com", padx=20, pady=10)
frame3.grid(row=2)
Label(frame3, text="Userid: pratik@gmail.com").grid(row=0, sticky=W)
Label(frame3, text="Password: gmailpass").grid(row=1, sticky=W)
Button(frame3, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
Button(frame3, text="Delete").grid(padx=15, row=0, column=2, rowspan=2)

frame3 = LabelFrame(frame, text="www.linkedin.com", padx=20, pady=10)
frame3.grid(row=4)
Label(frame3, text="Userid: pratikid@gmail.com").grid(row=0, sticky=W)
Label(frame3, text="Password: pratiklinked").grid(row=1, sticky=W)
Button(frame3, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
Button(frame3, text="Delete").grid(padx=15, row=0, column=2, rowspan=2)

frame4 = LabelFrame(frame, text="www.linkedin.com", padx=20, pady=10)
frame4.grid(row=3)
Label(frame4, text="Userid: pratikid").grid(row=0, sticky=W)
Label(frame4, text="Password: pratiklinked").grid(row=1, sticky=W)
Button(frame4, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
Button(frame4, text="Delete").grid(padx=15, row=0, column=2, rowspan=2)

# --- start program ---
root.mainloop()