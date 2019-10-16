import tkinter as tk

def click_btn():
    btn['text'] = 'Starting, now loading data'

root = tk.Tk()
root.title('game window')
height = 800
width = 1200
size = str(width) + 'x' + str(height) 
root.geometry(size)
label = 'Monster Hunter World'
label = tk.Label(root, text=label, font=('system', 32))

btn = tk.Button(root, text = 'Start', font=('Times New Roman', 24), command=click_btn)


label.place(x = width/2-(width/100)*15, y = height/2- (width/10)*1)
btn.place(x=width/2, y=height/2)
root.mainloop()
