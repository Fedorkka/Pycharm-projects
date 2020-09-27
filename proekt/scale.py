from PIL import Image
import pygame
import os
import time

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
d1=[]
d2=[]
d3=[]
d4=[]
x=0
y=0
k= 0
global d1, d2, d3, d4, x, y, kx, ky, img
pygame.init()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Project-Spectrometer")
done = False
clock = pygame.time.Clock()


def up_m():
    d1[1] = y_m
    d2[1] = y_m


def down_m():
    d3[1] = y_m
    d4[1] = y_m


def left_m():
    d1[0] = x_m
    d4[0] = x_m


def right_m():
    d2[0] = x_m
    d3[0] = x_m


def new_image():
    img = Image.open("C:/Users/Семья/Desktop/PS/f2223.jpg")
    x, y = img.size
    if x > y:
        ky= (x-y)/2
        kx= 20
        y = x
    else:
        kx = (y - x) / 2
        ky= 20
        x = y

    d1 = [kx, ky]
    d2 = [img.size[0] + kx, ky]
    d3 = [img.size[0] + kx, img.size[1] + ky]
    d4 = [kx, img.size[1] + ky]
    screen = pygame.display.set_mode((x+kx*2, y+kx*2))
def cropped_img():
    cropped_img_v = img.crop((d1[0], d1[1], d3[0], d3[1]))
    os.popen("C:/Users/Семья/Desktop/prg_spktr")




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == 1:
                if ((d1[1] - 5) < y_m < (d1[1] + 5)) and (d1[0] < x_m < d2[0]):
                    up = 1
                if ((d4[1] - 5) < y_m < (d4[1] + 5)) and (d4[0] < x_m < d3[0]):
                    down = 1
                if ((d1[0] - 5) < x_m < (d1[0] + 5)) and (d1[1] < y_m < d4[1]):
                    left = 1
                if ((d2[0] - 5) < x_m < (d2[0] + 5)) and (d2[1] < y_m < d3[1]):
                    right = 1
            if pygame.mouse.get_pressed()[2] == 1:


    screen.fill(white)

    x_m, y_m = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == 0:
        up = 0
        down = 0
        left = 0
        right = 0
    if up == 1:
        up_m()
    if down == 1:
        down_m()
    if right == 1:
        right_m()
    if left == 1:
        left_m()

    surf = pygame.Surface((d3[0] - d1[0], d3[1] - d1[1]))
    surf.set_alpha(50)
    screen.blit(pygame.image.load('C:/Users/Семья/Desktop/PS/f2223.jpg'), (20, 20))
    pygame.draw.polygon(screen, gray, (d1, d2, d3, d4), 2)
    screen.blit(surf, d1)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
