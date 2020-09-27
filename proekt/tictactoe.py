from tkinter import*
from random import randint
root= Tk()
root.geometry('180x180')
global pr
global h
global v
global s
global a
a= -1
pr=[0,0,0,0,0,0,0,0,0]
pr2=[0,0,0,0,0,0,0,0,0]
h=0
s=1
def bot():
    global a
    global h
    global s
    h = h + 1
    if pr[4] == 1 and h == 1:
        b11.config(text="☉")
        pr[0] = 2
        s= s+1
    if pr[4] == 0 and h==1:
        print(s, h)
        b22.config(text="☉")
        pr[4] = 2
        s= s+1
    for i in range(8):
        if ((pr[i]==1 and pr[i+1]==1) or (pr[i]== 2 and pr[i+1]==2))and(i+1== 1 or i+1 == 4 or i+1 == 7) and s== h:
            if i+1 == 1:
                b13.config(text="☉")
                s= s+1
                pr[2]= 2
            if i+1 == 4:
                b23.config(text="☉")
                s= s+1
                pr[5]= 2
            if i+1 == 7:
                b33.config(text="☉")
                s= s+1
                pr[8]= 2
            print('a')
        if ((pr[i] == 1 and pr[i+1] == 1) or (pr[i] == 2 and pr[i + 1] == 2)) and (i == 1 or i == 4 or i == 7) and s == h:
            if i == 1:
                b11.config(text="☉")
                s= s+1
                pr[0]= 2
            if i == 4:
                b21.config(text="☉")
                s= s+1
                pr[3]= 2
            if i == 7:
                b32.config(text="☉")
                s= s+1
                pr[6]= 2
        if i<= 5:
            if ((pr[i] == 1 and pr[i + 3] == 1) or (pr[i] == 2 and pr[i + 3] == 2)) and (i + 3 == 3 or i + 3 == 4 or i + 3 == 5) and s == h:
                if i + 3 == 3:
                    b31.config(text="☉")
                    s = s + 1
                    pr[6] = 2
                if i + 3 == 4:
                    b32.config(text="☉")
                    s = s + 1
                    pr[7] = 2
                if i + 3 == 5:
                    b33.config(text="☉")
                    s = s + 1
                    pr[8] = 2
                print(pr[i], )
        if i<= 5:
            if ((pr[i] == 1 and pr[i + 3] == 1) or (pr[i] == 2 and pr[i + 3] == 2)) and (i + 3 == 6 or i + 3 == 7 or i + 3 == 8) and s == h:
                if i  == 3:
                    b11.config(text="☉")
                    s = s + 1
                    pr[0] = 2
                if i == 4:
                    b12.config(text="☉")
                    s = s + 1
                    pr[1] = 2
                if i  == 5:
                    b13.config(text="☉")
                    s = s + 1
                    pr[2] = 2
    if (((pr[2]== 1 or pr[6]== 1) and pr[4]== 1) or (pr[2]== 2 or pr[6]== 2 ) and pr[4]== 2) and s == h:
        if (pr[2] == 2 or pr[2] == 1) and s == h:
            b31.config(text="☉")
            s = s + 1
            pr[6] = 2
        if (pr[6] == 2 or pr[6] == 1) and s == h:
            b13.config(text="☉")
            s = s + 1
            pr[2] = 2
    if (pr[0]==1 and pr[2]== 1) or (pr[0]==2 and pr[2]==2) and s == h and pr[1]==0:
        b12.config(text="☉")
        s=s+1
        pr[1]= 2
    if (pr[0]==1 and pr[6]== 1) or (pr[0]==2 and pr[6]==2) and s == h and pr[3]==0:
        b21.config(text="☉")
        s=s+1
        pr[3]= 2
    if (pr[2]==1 and pr[8]== 1) or (pr[2]==2 and pr[8]==2) and s == h and pr[5]==0:
        b23.config(text="☉")
        s=s+1
        pr[5]= 2
    if (pr[6]==1 and pr[8]== 1) or (pr[6]==2 and pr[8]==2) and s == h and pr[6]==0:
        b32.config(text="☉")
        s=s+1
        pr[7]= 2
    else:
        if s ==h:
            b = 0
            for n in range(8):
                if pr[n] == 0:
                    a = a + 1
                    pr2[a] = n
            for n in range(8):
                if pr2[n] != 0:
                    b = b + 1
            r = randint(0, b - 1)
            if r == 0:
                b11.config(text="☉")
                s = s + 1
            if r == 1:
                b12.config(text="☉")
                s = s + 1
            if r == 2:
                b13.config(text="☉")
                s = s + 1
            if r == 3:
                b21.config(text="☉")
                s = s + 1
            if r == 4:
                b22.config(text="☉")
                s = s + 1
            if r == 5:
                b23.config(text="☉")
                s = s + 1
            if r == 6:
                b31.config(text="☉")
                s = s + 1
            if r == 7:
                b32.config(text="☉")
                s = s + 1
            if r == 8:
                b33.config(text="☉")
                s = s + 1


def b11f():
    global pr
    global s
    if pr[0]==0:
        b11.config(text="×")
        pr[0]= 1
        root.after(100, bot)
def b12f():
    global pr
    global s
    if pr[1]==0:
        b12.config(text="×")
        pr[1] = 1
        root.after(100, bot)
def b13f():
    global pr
    global s
    if pr[2]==0:
        b13.config(text="×")
        pr[2] = 1
        root.after(100, bot)
def b21f():
    global pr
    global s
    if pr[3]==0:
        b21.config(text="×")
        pr[3] = 1
        root.after(100, bot)
def b22f():
    global pr
    global s
    if pr[4]==0:
        b22.config(text="×")
        pr[4] = 1
        root.after(100, bot)
def b23f():
    global pr
    global s
    if pr[5]==0:
        b23.config(text="×")
        pr[5] = 1
        root.after(100, bot)
def b31f():
    global pr
    global s
    if pr[6]==0:
        b31.config(text="×")
        pr[6] = 1
        root.after(100, bot)
def b32f():
    global pr
    global s
    if pr[7]==0:
        b32.config(text="×")
        pr[7] = 1
        root.after(100, bot)
def b33f():
    global pr
    global s
    if pr[8]==0:
        b33.config(text="×")
        pr[8] = 1
        root.after(100, bot)
b11= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b11f)
b11.place(x=0,y=0)
b12= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b12f)
b12.place(x=60,y=0)
b13= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b13f)
b13.place(x=120,y=0)
b21= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b21f)
b21.place(x=0,y=60)
b22= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b22f)
b22.place(x=60,y=60)
b23= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b23f)
b23.place(x=120,y=60)
b31= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b31f)
b31.place(x=0,y=120)
b32= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b32f)
b32.place(x=60,y=120)
b33= Button(root, text=' ', font="Arial 20", width=3, height=1, command= b33f)
b33.place(x=120,y=120)
root.mainloop()