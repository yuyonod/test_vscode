import tkinter
root = tkinter.Tk()
root.title['fortune']
root.resizable(False, False)
canvas = tkinter.Canvas(root, widht=800, height=600) 
canvas.pack()
img = tkinter.PhotoImage(file='cat.png')
canvas.create_image(400, 300, image=img)
root.mainloop()