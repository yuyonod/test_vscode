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
import tkinter
import random


def click_btn():
    label['text']=random.choice(['great', 'good', 'not so bad','bad'])
    label.update()
root = tkinter.Tk()
root.title('fortune')
root.resizable(False, False)

width = 800
height = 600
canvas = tkinter.Canvas(root, width=width, height=height) 
canvas.pack()
img = tkinter.PhotoImage(file='cat.png')
canvas.create_image(400, 300, image=img)


label = tkinter.Label(root, text='???', font=('Times New Roman', 120), bg='white')
label.place(x=(width/10)*4, y=(height/10)*1)
btn = tkinter.Button(root, text='dice fortune', font=('Times New Roman', 50), fg='skyblue', command=click_btn)
btn.place(x=(width/10)*3, y=(height/10)*6)
root.mainloop()