from tkinter import*
from pynput import keyboard
from pynput.keyboard import Key

root=Tk()
def m1(event):
    while format(key)== Key.down:
        a.move(rect2,0,20)
    
   
def m2(event):
    a.move(rect2,0,-20)
def m3(event):
    a.move(rect2,20,0)
def m4(event):
    a.move(rect2,-20,0)    
wid=1000
heig=1000
sn=1
sn1=20
a = Canvas(root, width=wid, height=heig, bg='white')
a.pack()
while sn<=1000:
    a.create_line(sn,0,sn,1000,width=1.5,fill="black")
    a.create_line(0,sn,1000,sn,width=1.5,fill="black")
    sn=sn+20
rect2 = a.create_rectangle(20, 0,20+sn1, 0+sn1, fill="black")
rect3 = a.create_rectangle(40, 0, 40+sn1, 0+sn1, fill="black")
rect1 = a.create_rectangle(0, 0, 0+sn1, 0+sn1, fill="black")
root.bind("<Down>", m1)
root.bind("<Up>", m2)
root.bind("<Right>", m3)
root.bind("<Left>", m4)
with keyboard.Listener(
    on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
root.mainloop()
