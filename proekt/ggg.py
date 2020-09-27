import pygame
import math
from random import randint
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
color = (255, 255, 255)
perviy_raz = 0
x_s = 1920
y_s = 1200
x = 0
y = 0
i= 0
r= 255
g= 0
b= 0
n = 1
k =0
dv= 1
color = []
p= 100
size = (x_s, y_s)
screen = pygame.display.set_mode(size)
screen.fill(white)
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)
    if event.type == pygame.KEYDOWN:
        if event.key == 273 or event.key == 119:
            if p<= 150:
                p += 1
        if event.key == 274 or event.key == 115:
            if p>= -150:
                p-= 1
        if event.key == 275 or event.key == 100:
            dv= 0
            n += 0.01
        elif event.key == 276 or event.key == 97:
            dv= 0
            n -= 0.01
        else:
            dv= 1

    if k == 0:
        for x in range(x_s):
            if g != 255 and r == 255 and b == 0:
                g += 5
            if g == 255 and r != 0 and b == 0:
                r -= 5
            if r == 0 and b != 255 and g == 255:
                b += 5
            if b == 255 and r == 0 and g != 0:
                g -= 5
            if g == 0 and b == 255 and r != 255:
                r += 5
            if r == 255 and b != 0 and g == 0:
                b -= 5
            color.append((r, g, b))
    k = 1
    if k == 1:
        for x in range(x_s):
            r = color[x][0]
            g = color[x][1]
            b = color[x][2]
            if g != 255 and r == 255 and b == 0:
                g += 5
            if g == 255 and r != 0 and b == 0:
                r -= 5
            if r == 0 and b != 255 and g == 255:
                b += 5
            if b == 255 and r == 0 and g != 0:
                g -= 5
            if g == 0 and b == 255 and r != 255:
                r += 5
            if r == 255 and b != 0 and g == 0:
                b -= 5
            color[x] = (r, g, b)
            if dv == 1:
                y = round(y_s/2 - (math.cos(math.radians((x-i) * n)) * p))
                y1 = round(y_s/2 - (math.cos(math.radians((x+1-i)*n)) * p))
            else:
                y = round(y_s/2 - (math.cos(math.radians((x-i) * n)) * p))
                y1 = round(y_s/2 - (math.cos(math.radians((x + 1) * n)) * p))
            pygame.draw.line(screen, (r, g, b), [x, y], [x+1, y], 10)
        if dv== 1:
            i += 1




    pygame.display.flip()
    clock.tick(180)
pygame.quit()
