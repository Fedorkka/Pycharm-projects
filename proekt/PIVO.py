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
x_s = 500
y_s = 500
x = 0
y = 0
i= 0
r= 255
g= 0
b= 0
n =0
k =0
v= 0.5
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
    if k == 0:
        if g != 255 and r == 255 and b == 0:
             g += 1
        if g == 255 and r != 0 and b == 0:
            r -= 1
        if r == 0 and b != 255 and g == 255:
             b += 1
        if b == 255 and r == 0 and g != 0:
            g -= 1
        if g == 0 and b == 255 and r != 255:
             r += 1
        if r == 255 and b != 0 and g == 0:
            b-= 1
        color = r, g, b
    k = 1
    if k == 1:
        if g != 255 and r == 255 and b == 0:
            g += 1
        if g == 255 and r != 0 and b == 0:
            r -= 1
        if r == 0 and b != 255 and g == 255:
            b += 1
        if b == 255 and r == 0 and g != 0:
            g -= 1
        if g == 0 and b == 255 and r != 255:
            r += 1
        if r == 255 and b != 0 and g == 0:
            b -= 1
        color= r,g, b
    f1 = pygame.font.Font("Arial", 36)
    text1 = f1.render('Глеб алкаш', 1, color)
    screen.blit(text1, (10, 50))



    pygame.display.flip()
    clock.tick(180)
pygame.quit()
