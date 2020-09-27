#coding: utf-8
from tkinter import*
z=20
def text():
    t1=Label(root, text='x', font='Arial 20')
    t1.pack(side=LEFT)
def text1():
    t1=Label(root, text='y', font='Arial 20')
    t1.pack(side=LEFT)
def text2():
    t1=Label(root, text='+', font='Arial 20')
    t1.pack(side=LEFT)
def text3():
    t1=Label(root, text='-', font='Arial 20')
    t1.pack(side=LEFT)
def text4():
    t1=Label(root, text='^2', font='Arial 20')
    t1.pack(side=LEFT) 
root=Tk()
root.geometry('500x300')
t=Label(root, text='Введите функцию', font='Arial 30')
t.place(x=85, y=20)
b=Button(root, text='x',font='Arial 20', command=text)
b.place(x=70, y=200)
b1=Button(root, text='y',font='Arial 20', command=text1)
b1.place(x=110, y=200)
b2=Button(root, text='+',font='Arial 20', command=text2)
b2.place(x=152, y=200)
b3=Button(root, text='-',font='Arial 20', command=text3)
b3.place(x=196, y=200)
b4=Button(root, text='a^2',font='Arial 20', command=text4)
b4.place(x=246, y=200)
root.mainloop()

