#coding: utf-8
from tkinter import* 
def c(event):
    x1=(event.x_root)
    y1=(event.y_root)
    while True:
        if x1>200 and x1<700:
            b.destroy()        
    
root=Tk()
root.geometry('600x100')
b=Button(root, text='Попробуй нажать на меня',font='Arial 30')
b.pack()
root.bind('<Motion>', c)
root.mainloop()