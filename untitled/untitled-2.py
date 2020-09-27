#coding: utf-8
import matplotlib.pyplot as plt
import random
from tkinter import *
x=[];
y=[]
i=int(input())
for k in range(i):
    y.append(random.randint(0,100))
    x.append(k+100)
plt.plot(x, y)
plt.show()