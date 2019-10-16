import tkinter as tk
root = tk.Tk()
root.title('my first canvas')
canvas = tk.Canvas(root, width =400, height=600, bg ='skyblue')
canvas.pack()
root.mainloop()