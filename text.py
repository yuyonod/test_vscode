import tkinter
root = tkinter.Tk()
def click_btn():
    text.insert(tkinter.END, 'monster appeared!  ')
root.title('text form')
root.geometry('400x200')

btn = tkinter.Button(text='get strings',command=click_btn)
btn.pack()
text = tkinter.Text()
text.pack()

root.mainloop()