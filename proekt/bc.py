import pygame
import math
from random import randrange, randint
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
pygame.init()
r= 57
size = (900, 900)
screen = pygame.display.set_mode(size)
screen.fill(black)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(white)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()