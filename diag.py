import tkinter
root = tkinter.Tk()
root.title('your diagnosis')
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
img = tkinter.PhotoImage(file='cat.png')
canvas.create_image(400,300,image=img)
btn = tkinter.Button(text='check it out', font=('Times New Roman', 16))
btn.place(x=400,y=300)
text = tkinter.Text(width=40, height=5, font=('Times New Roman', 16))
text.place(x=320, y=30)

bvar = [None] * 7
cbtn = [None] * 7
ITEM=['do you like high place', ' do you like rolling something' , 'are you good', 'are you doing great', 'do you smell something', 'do you care mouse', 'ddo you like your hair']

for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=('Times New Roman', 12), variable=bvar[i], bg='#dfe')
    cbtn[i].place(x=400, y=160+40*i)

root.mainloop()