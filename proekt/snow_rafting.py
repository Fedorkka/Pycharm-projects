# coding: utf-8
import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
color = (255, 255, 255)
perviy_raz = 0
c = 50
c_v = 5
pygame.init()
x_s = 900
y_s = 900
x = 0
y = 0
s = 15
x_l = 0
y_l = 0
size = (x_s, y_s)
v = 15
lock_x = 1
lock_y = 0
body_coord = []
k = 0
b_h_x = 0
b_h_y = 0
game_over = 0
food = 0
score = 0
font_sc = pygame.font.SysFont("Arial", 16)
body_coord.append((b_h_x, b_h_y))
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")
k_l = 'right'
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(black)
    # управление
    if event.type == pygame.KEYDOWN:
        if (event.key == 275 or event.key == 100) and lock_x == 0:
            k_l = 'right'
            lock_x = 1
            lock_y = 0
        if (event.key == 276 or event.key == 97) and lock_x == 0:
            k_l = 'left'
            lock_x = 1
            lock_y = 0
        if (event.key == 273 or event.key == 119) and lock_y == 0:
            k_l = 'up'
            lock_y = 1
            lock_x = 0
        if (event.key == 274 or event.key == 115) and lock_y == 0:
            k_l = 'down'
            lock_y = 1
            lock_x = 0
        if event.key == 114:
            x = 0
            y = 0
            lock_x = 1
            lock_y = 0
            body_coord = []
            k = 0
            b_h_x = 0
            b_h_y = 0
            body_coord.append((b_h_x, b_h_y))
            k_l = 'right'
            game_over = 0
            food = 0
            score = 0
    if game_over == 0:
        body_coord[0] = (b_h_x, b_h_y)  # начало тела
        for i in reversed(range(k)):
            if i > 0:
                body_coord[i] = body_coord[i - 1]
            pygame.draw.rect(screen, (81, 214, 9), [body_coord[i][0], body_coord[i][1], s, s])  # движение
            pygame.draw.rect(screen, (0, 156, 29), [body_coord[i][0], body_coord[i][1], s - 7, s - 7])
        x_l = body_coord[k - 1][0]  # координаты конца
        y_l = body_coord[k - 1][1]
        b_h_x = x
        b_h_y = y
        pygame.draw.rect(screen, (81, 214, 9), [b_h_x, b_h_y, s, s])
        pygame.draw.rect(screen, (0, 156, 29), [b_h_x, b_h_y, s - 7, s - 7])

        if k_l == 'right':
            x += v
        if k_l == 'left':
            x -= v
        if k_l == 'up':
            y -= v
        if k_l == 'down':
            y += v
        if x < -15:
            x = 900
        if x > 900:
            x = -15
        if y < -15:
            y = 900
        if y > 900:
            y = -15

    if x > 885 or x < 0 or y > 885 or y < 0:  # блокировка поворота при телепортации
        if perviy_raz == 0:
            l_lock_x = lock_x
            l_lock_y = lock_y
            perviy_raz = 1
        lock_x = 1
        lock_y = 1
    else:
        if perviy_raz == 1:
            lock_x = l_lock_x
            lock_y = l_lock_y
            perviy_raz = 0

    if food == 0:
        x_f = randint(0, 59) * 15
        y_f = randint(0, 59) * 15  # появление фруктов
        food = 1

    if x_f == x and y_f == y:
        score += 1
        body_coord.append((x_l, y_l))  # поедание
        k += 1
        food = 0

    pygame.draw.rect(screen, (204, 35, 35), [x_f, y_f, s, s])  # фрукт

    pygame.draw.rect(screen, (81, 214, 9), [x, y, s, s])
    pygame.draw.rect(screen, (100, 50, 50), [x, y, s - 8, s - 8])  # голова

    text_sc = font_sc.render("Счет:" + " " + str(score), True, (50, 50, 50))
    screen.blit(text_sc, (0, 0))
    for i in range(k):
        if x == body_coord[i][0] and y == body_coord[i][1]:  # проверка на столкновение
            game_over = 1
    if game_over == 1:
        screen.fill(black)
        font = pygame.font.SysFont("Arial", 30)  # заново
        c += c_v
        if c == 255:
            c_v = -c_v
        if c == 50:
            c_v = -c_v
        text = font.render("Вы проиграли! Нажмите 'R', чтобы начать новую игру. Ваш Счет:" + " " + str(score), True,
                           (c, c, c))
        screen.blit(text, (450 - text.get_width() // 2, 450 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
