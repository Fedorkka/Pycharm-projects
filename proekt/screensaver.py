import pygame
from random import randrange, randint
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)

green = (0, 255, 0)
red = (255, 0, 0)
color= (255, 255, 255)
pygame.init()
x_s= 1920
y_s= 1200
size = (x_s, y_s)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
screen.fill(black)
pygame.display.set_caption("My Game")
x= randrange(0, x_s)
y = randrange(0, y_s)
s=0
n=0
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    x_o= x
    y_o= y
    x= randrange(0, x_s)
    y = randrange(0, y_s)
    s= randint(1, 5)
    if n ==0:
        pygame.draw.ellipse(screen, gray, [x_o-s, y_o-s, s*2, s*2])
    pygame.draw.aaline(screen, gray, [x_o, y_o], [x, y], s)
    n=n+1
    if n== 200:
        screen.fill(black)
        n=0


    pygame.display.flip()
    clock.tick(10)

pygame.quit()