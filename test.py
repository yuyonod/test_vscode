# import tkinter
# root = tkinter.Tk()
# root.title('my first label')
# root.geometry('800x600')
# label = tkinter.Label(root, text='strings of label', font=('system', 24))
# label.place(x=200, y=400)
# root.mainloop()


# import calendar
# print(calendar.prcal(2019))


# import calendar
# print(calendar.isleap())



# import datetime
# today = datetime.date.today()
# birth = datetime.date(1995, 2,1)
# print(today-birth)


# import random
# cnt = 0
# while True:
#     r = random.randint(1, 100)
#     cnt += 1
#     print('{}回目'.format(cnt), r)
#     if r == 77:
#         print('you got super hero')
#         break


# QUESTION = ['サザエさんの旦那さんの名前は？', 'your blood type?', 'your name?']
# answer = ['マスオ', 'B', 'Yuya']
# for i, q in enumerate(QUESTION):
#     print(q)    
#     ans = input()
#     if ans == answer[i]:
#         print('correct !')
#     else:
#         print('wring !')

import tkinter as tk
root = tk.Tk()
root.title('my first canvas')
canvas = tk.Canvas(root, width =1200, height=900)
canvas.pack()

img = tk.PhotoImage(file='cat.png')
canvas.create_image(200,300, image=img)
root.mainloop()