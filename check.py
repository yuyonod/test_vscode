import tkinter
root = tkinter.Tk()
root.title('check button')
root.geometry('400x200')
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text='check', variable=cval)
cbtn.pack()
root.mainloop()