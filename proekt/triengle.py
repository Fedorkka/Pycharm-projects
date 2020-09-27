import pygame
from random import randrange, randint
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
color= (255, 255, 255)
pygame.init()
x_s= 800
y_s= 800
s= 20
cl= 0
size = (x_s, y_s)
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.set_caption("My Game")
pygame.draw.circle(screen, black, [400, 200], 2)#3
pygame.draw.circle(screen, black, [200, 600], 2)#1
pygame.draw.circle(screen, black, [600, 600], 2)#2
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.MOUSEBUTTONDOWN and cl == 0:
        mx, my = pygame.mouse.get_pos()
        mx = round(mx)
        my= round(my)
        x= mx
        y= my
        cl= 1



    if cl == 1:
        pygame.draw.circle(screen, black, [x, y], 2)
        a = randint(1, 3)
        if a == 1:
            x = x - ((x - 200) / 2)
            y = y + ((600 - y) / 2)
        if a == 2:
            x = x + ((600 - x) / 2)
            y = y + ((600 - y) / 2)
        if a == 3:
            if x <= 200:
                x = x + ((200 - x) / 2)
                y = y - ((y - 200) / 2)
            if x > 200:
                x = x - ((x - 400) / 2)
                y = y - ((y - 200) / 2)
        x = round(x)
        y = round(y)
    pygame.display.flip()
    clock.tick(180)
pygame.quit()