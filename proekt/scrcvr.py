import pygame
import pylab
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
color = (255, 255, 255)
size = [100, 100]
s = 10
x = s
y = s
res=[[],[],[]]
v = [1, 1]
k = 0
step= False

while size[0] and size[1] != 110:

    x += v[0]
    y += v[1]

    if (x + s == size[0] or x - s == 0) and (y + s == size[1] or y - s == 0):
        step = True
    if (x + s == size[0] or x - s == 0) and not step:
        v[0] = -v[0]
        k += 1
    if (y + s == size[1] or y - s == 0) and not step:
        v[1] = -v[1]
        k += 1
    if step:
        if size[0] == 1000:
            size[0] = 100
            size[1] += 10
            print(str(int(size[1]/10))+"%")
        else:
            size[0] += 10
        x = s
        y = s
        v = [1, 1]
        res[0].append(size[0])
        res[1].append(size[1])
        res[2].append(k/100)

        k = 0


        step = False



print(res)
fig = plt.figure()

chart = fig.add_subplot(1,1,1,projection = '3d')

x,y,z = res[0],res[1],res[2]

chart.plot(x,y,z)

plt.show()

