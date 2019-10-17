import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.title('my first msgbox')
def click_btn():
    tkinter.messagebox.showinfo('info to put message','you clicked button')

root.geometry('400x200')
btn = tkinter.Button(text='test', command=click_btn)
btn.pack()
root.mainloop()