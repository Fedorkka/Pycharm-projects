import pygame
from random import randint

pygame.init()
pygame.font.init()
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
color = (255, 255, 255)
c = 50
c_v = 5
x_s = 450
y_s = 450
s = 15
size = (x_s, y_s)
v = 15
game_over = 2
font_sc = pygame.font.SysFont("Arial", 16)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")
x = 0
y = 0
n = 0
lvl = 10
map = []
for i in range(round((x_s / s - 1) * (y_s / s - 1))):
    map.append((x, y))
    if x == x_s - 15:
        y += 15
        x = 0
    x += 15
y += 15
map.append((x, y))

img = pygame.image.load("D:\snake-games.jpg")
done = False
clock = pygame.time.Clock()
while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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
            body_coord.append((x, y))
            k_l = 'right'
            game_over = 0
            food = 0
            score = 0
            timer2 = 0
            timer = 0
            lvl = 10
            b_food = 0
            perviy_raz = 0

    if game_over == 2:
        screen.fill(white)
        screen.blit(img, ((x_s - 400) / 2, 50))
        text_sr = pygame.font.SysFont("Gotham Pro Narrow Bold", round(x_s / 15)).render('Змейка', True, (0, 0, 0))
        screen.blit(text_sr, (x_s / 2 - text_sr.get_width() / 2, y_s / 2 - text_sr.get_height() / 2 + 50))
        text_sr1 = pygame.font.SysFont("Gotham Pro Narrow Bold", round(x_s / 30)).render('Управление: WASD или стрелки',
                                                                                         True,
                                                                                         (0, 0, 0))
        screen.blit(text_sr1, (x_s / 2 - text_sr1.get_width() / 2, y_s / 2 + 100 - text_sr1.get_height() / 2))
        text_sr2 = pygame.font.SysFont("Gotham Pro Narrow Bold", round(x_s / 30)).render('Перезапуск - R', True,
                                                                                         (0, 0, 0))
        screen.blit(text_sr2, (x_s / 2 - text_sr2.get_width() / 2, y_s / 2 + 150 - text_sr2.get_height() / 2))
        text_sr3 = pygame.font.SysFont("Gotham Pro Narrow Bold", round(x_s / 30)).render('Нажмите "R", чтобы начать',
                                                                                         True,
                                                                                         (0, 0, 0))
        screen.blit(text_sr3, (x_s / 2 - text_sr3.get_width() / 2, y_s / 2 + 200 - text_sr3.get_height() / 2))
        text_sr4 = pygame.font.SysFont("Gotham Pro Narrow Bold", round(x_s / 30)).render(
            'Проектная работа Ужегова. Ф. А', True,
            (150, 150, 150))
        screen.blit(text_sr4, (x_s / 2 - text_sr4.get_width() / 2, y_s / 2 + 250 - text_sr4.get_height() / 2))

    if game_over == 0:

        if b_food == 0:  # таймер фрукта
            timer += 1

        if timer == 600:
            timer = 0
            b_food = 1

        if b_food == 1:
            empty = list(set(map) - set(body_coord) - {x, y})
            x_b_f_c = empty[randint(0, len(empty) - 1)]
            x_b_f = x_b_f_c[0]
            y_b_f = x_b_f_c[1]
            b_food = 2

        if b_food == 2:
            timer2 += 1
            pygame.draw.rect(screen, (255, 215, 0), [x_b_f, y_b_f, s, s])  # бонусный фрукт
            if timer2 == 150:
                b_food = 0
            if x == x_b_f and y == y_b_f:
                timer2 = 0
                b_food = 0
                n = 1
                if lvl != 30 and k % 2 == 0:
                    lvl += 1

        if 5 > n > 0:
            body_coord.append((x_l, y_l))  # постепенное добавление
            k += 1
            score += 1
            n += 1

        if n == 5:
            n = 0

        if food == 0:
            empty = list(set(map) - set(body_coord) - {x, y})
            x_f_c = empty[randint(0, len(empty) - 1)]
            x_f = x_f_c[0]
            y_f = x_f_c[1]  # появление фруктов
            food = 1

        if x_f == x and y_f == y:
            score += 1
            body_coord.append((x_l, y_l))  # поедание
            k += 1
            food = 0
            print(k)
            if lvl != 30 and k % 2 == 0:
                lvl += 1

        pygame.draw.rect(screen, (204, 35, 35), [x_f, y_f, s, s])  # фрукт

        for i in reversed(range(k + 1)):
            if i > 0:
                body_coord[i] = body_coord[i - 1]
            if i == 0:
                body_coord[0] = (x, y)  # начало тела
            pygame.draw.rect(screen, (81, 214, 9), [body_coord[i][0], body_coord[i][1], s, s])  # движение
            pygame.draw.rect(screen, (0, 156, 29), [body_coord[i][0] + 7, body_coord[i][1] + 7, s - 7, s - 7])
        x_l = body_coord[k][0]  # координаты конца
        y_l = body_coord[k][1]

        if k_l == 'right':
            x += v
        if k_l == 'left':
            x -= v
        if k_l == 'up':
            y -= v
        if k_l == 'down':
            y += v
        if x < -s:
            x = x_s
        if x > x_s:
            x = -s
        if y < -s:
            y = y_s
        if y > y_s:
            y = -s

        if x > x_s - s or x < 0 or y > y_s - s or y < 0:  # блокировка поворота при телепортации
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

        pygame.draw.rect(screen, (81, 214, 9), [x, y, s, s])
        pygame.draw.rect(screen, (100, 50, 50), [x, y, s - 8, s - 8])  # голова

        text_sc = font_sc.render("Счет:" + " " + str(score), True, (100, 100, 100))
        screen.blit(text_sc, (0, 0))
        for i in range(k):
            if x == body_coord[i][0] and y == body_coord[i][1]:  # проверка на столкновение
                game_over = 1
    if game_over == 1:
        font = pygame.font.SysFont("Arial", round(x_s / 20))  # заново
        c += c_v
        if c == 255:
            c_v = -c_v
        if c == 50:
            c_v = -c_v
        text_lose = font.render("Вы проиграли!", True, (c, c, c))
        text_lose2 = font.render("Нажмите 'R', чтобы начать новую игру", True, (c, c, c))
        text_lose3 = font.render(" Ваш Счет:" + " " + str(score), True, (c, c, c))
        screen.blit(text_lose, (x_s / 2 - text_lose.get_width() / 2, y_s / 2 - text_lose.get_height() / 2 - 50))
        screen.blit(text_lose2, (x_s / 2 - text_lose2.get_width() / 2, y_s / 2 - text_lose2.get_height() / 2))
        screen.blit(text_lose3, (x_s / 2 - text_lose3.get_width() / 2, y_s / 2 - text_lose3.get_height() / 2 + 50))

    pygame.display.flip()

    clock.tick(lvl)
pygame.quit()
