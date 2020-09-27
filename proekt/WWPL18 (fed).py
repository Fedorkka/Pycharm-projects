import pygame
import os.path

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
darkred = (100, 0, 0)
lightblue = (0, 200, 255)
pec = (0, 100, 255)
pec2 = (0, 50, 255)
pi = 3.14

y = 350
xbl = 600
ybl = 350
sxbl = 0
sybl = 0
sd = 4
xs = 600
n = 0
w = 1
b = 2
atk = n
sw = 0
sb = 0

ywg = 325
ybg = 325

xw = 500
xwn = xw
xuw = 1100
uw = 0

xb = 700
xbn = xb
xub = 100
ub = 0
size = (1200, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('WWPL 18')

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            print(event.key)
            # Старт
            if event.key == 13:
                if atk == n:
                    xwn = xs
            # Кнопки атаки белых
            if atk == w:
                # Проверяем наличие мяча у игрока
                if (xbl == xwn - 15 and ybl == y) or (xbl == xw - 15 and (ybl == y - 240 or ybl == y + 240)):
                    # Пас 1
                    if event.key == 49:
                        print('sas')
                        sxbl = round((xwn - 15 - xbl) / 5)
                        sybl = round((y - ybl) / 5)
                        if xwn < xuw - 320:
                            sxbl += sd + 1
                            plt = 1

                    # Пас 2
                    if event.key == 50:
                        print('ses')
                        sxbl = round((xw - 15 - xbl) / 5)
                        sybl = round((y - 240 - ybl) / 5)
                        if xw < xuw - 170:
                            sxbl += sd
                    # Пас 3
                    if event.key == 51:
                        print('sos')
                        sxbl = round((xw - 15 - xbl) / 5)
                        sybl = round((y + 240 - ybl) / 5)
                        if xw < xuw - 170:
                            sxbl += sd
        if event.type == pygame.MOUSEBUTTONDOWN:
            if atk == w:
                if pygame.mouse.get_pressed()[0] == 1:
                    uw = 1
                if pygame.mouse.get_pressed()[2] == 1:
                    uw = 0
            elif atk == b:
                if pygame.mouse.get_pressed()[0] == 1:
                    ub = 1
                if pygame.mouse.get_pressed()[2] == 1:
                    ub = 0

    screen.fill(white)

    # Gameplace
    pygame.draw.rect(screen, pec, [100, 0, 1000, 700])
    pygame.draw.rect(screen, lightblue, [150, 50, 900, 600])
    pygame.draw.line(screen, pec2, [100, 0], [150, 50], 5)
    pygame.draw.line(screen, pec2, [1050, 50], [1100, 0], 5)
    pygame.draw.line(screen, pec2, [100, 700], [150, 650], 5)
    pygame.draw.line(screen, pec2, [1050, 650], [1100, 700], 5)
    pygame.draw.lines(screen, black, False, [[xub, 250], [xub - 80, 250], [xub - 80, 450], [xub, 450]], 5)
    pygame.draw.lines(screen, black, False, [[xuw, 250], [xuw + 80, 250], [xuw + 80, 450], [xuw, 450]], 5)

    # White player 1
    pygame.draw.circle(screen, white, [xwn, y], 25)
    pygame.draw.circle(screen, black, [xwn, y], 25, 3)
    font = pygame.font.SysFont('FreeSans', 50)
    text = font.render('1', True, black)
    screen.blit(text, [xwn - 10, y - 15])
    # White player 2
    pygame.draw.circle(screen, white, [xw, y - 240], 25)
    pygame.draw.circle(screen, black, [xw, y - 240], 25, 3)
    text = font.render('2', True, black)
    screen.blit(text, [xw - 10, y - 255])
    # White player 3
    pygame.draw.circle(screen, white, [xw, y + 240], 25)
    pygame.draw.circle(screen, black, [xw, y + 240], 25, 3)
    text = font.render('3', True, black)
    screen.blit(text, [xw - 10, y + 225])
    # white goalkeeper
    pygame.draw.ellipse(screen, darkred, [xub, ywg, 40, 50])
    pygame.draw.ellipse(screen, white, [xub, ywg, 40, 50], 3)

    # Blue player 1
    pygame.draw.circle(screen, blue, [xbn, y], 25)
    pygame.draw.circle(screen, white, [xbn, y], 25, 3)
    text = font.render('1', True, white)
    screen.blit(text, [xbn - 10, y - 15])
    # Blue player 2
    pygame.draw.circle(screen, blue, [xb, y - 240], 25)
    pygame.draw.circle(screen, white, [xb, y - 240], 25, 3)
    text = font.render('2', True, white)
    screen.blit(text, [xb - 10, y - 255])
    # Blue player 3
    pygame.draw.circle(screen, blue, [xb, y + 240], 25)
    pygame.draw.circle(screen, white, [xb, y + 240], 25, 3)
    text = font.render('3', True, white)
    screen.blit(text, [xb - 10, y + 225])
    # Blue goalkeeper
    pygame.draw.ellipse(screen, darkred, [xuw - 40, ybg, 40, 50])
    pygame.draw.ellipse(screen, blue, [xuw - 40, ybg, 40, 50], 3)

    xbl += sxbl
    ybl += sybl

    # Ball
    pygame.draw.circle(screen, red, [xbl, ybl], 15)

    # Счёт
    font1 = pygame.font.SysFont('FreeSans', 200)
    text = font1.render(str(sw) + ':' + str(sb), True, black)
    screen.blit(text, [500, 710])

    # Описание управления
    font2 = pygame.font.SysFont("FreeSans", 30)
    text = font2.render('Пас белому игроку 1:   1', True, black)
    screen.blit(text, [100, 710])
    text = font2.render('Пас белому игроку 2:   2', True, black)
    screen.blit(text, [100, 740])
    text = font2.render('Пас белому игроку 3:   3', True, black)
    screen.blit(text, [100, 770])
    text = font2.render('Удар:   ЛКМ, потом A', True, black)
    screen.blit(text, [100, 830])
    text = font2.render('Отбор:   S', True, black)
    screen.blit(text, [100, 860])
    text = font2.render('Пас синему игроку 1:  Numpad 1', True, black)
    screen.blit(text, [805, 710])
    text = font2.render('Пас синему игроку 2:  Numpad 2', True, black)
    screen.blit(text, [805, 740])
    text = font2.render('Пас синмеу игроку 3:  Numpad 3', True, black)
    screen.blit(text, [805, 770])
    text = font2.render('Удар:   ЛКМ, потом Numpad 0', True, black)
    screen.blit(text, [805, 830])
    text = font2.render('Отбор:   Numpad Точка', True, black)
    screen.blit(text, [805, 860])

    # goalkeepers action
    if xbl <= 600:
        if ywg + 25 > ybl:
            ywg -= 1
    if ywg + 25 < ybl:
        ywg += 1
    if ywg <= 225:
        ywg = 225
    if ywg >= 425:
        ywg = 425
    if xbl >= 600:
        if ybg + 25 > ybl:
            ybg -= 1
    if ybg + 25 < ybl:
        ybg += 1
    if ybg <= 225:
        ybg = 225
    if ybg >= 425:
        ybg = 425

    # Players action
    if atk == w:
        xw += sd
        xwn += sd + 1
        xb += sd + 2
        xbn += sd + 2
        if xw >= xuw - 320:
            xw = xuw - 320
        if xwn >= xuw - 170:
            xwn = xuw - 170
        if xb >= xuw - 280:
            xb = xuw - 280
        if xbn >= xuw - 130:
            xbn = xuw - 130
    elif atk == b:
        xb -= sd
        xbn -= sd + 1
        xw -= sd + 2
        xwn -= sd + 2
        if xw <= xub + 280:
            xw = xub + 280
        if xwn <= xub + 130:
            xwn = xub + 130
        if xb <= xub + 320:
            xb = xub + 320
        if xbn <= xub + 170:
            xbn = xub + 170
    elif atk == n:
        xw += 0
        xwn += 0
        xb += 0
        xbn += 0

    # Поймали белые
    # Поймал 1
    if (ybl >= y - 25 and ybl <= y + 25) and (xbl <= xwn + 25 and xbl >= xwn - 25):
        xbl = xwn - 15
        atk = w
        sxbl = 0
        sybl = 0
        ybl = y
    # Поймал 2 или 3
    if (xbl <= xw + 25 and xbl >= xw - 25):
        # Поймал 2
        if ybl >= y - 265 and ybl <= y - 215:
            ybl = y - 240
            atk = w
            sxbl = 0
            sybl = 0
            xbl = xw - 15
        # Поймал 3
        elif ybl >= y + 215 and ybl <= y + 265:
            ybl = y + 240
            atk = w
            sxbl = 0
            sybl = 0
            xbl = xw - 15

    # Поймали синие
    # Поймал 1
    if (ybl >= y - 25 and ybl <= y + 25) and (xbl <= xbn + 25 and xbl >= xbn - 25):
        xbl = xbn + 15
        atk = b
        sxbl = 0
        sybl = 0
        ybl = y
    # Поймал 2 или 3
    if (xbl <= xb + 25 and xbl >= xb - 25):
        # Поймал 2
        if ybl >= y - 265 and ybl <= y - 215:
            ybl = y - 240
            atk = b
            sxbl = 0
            sybl = 0
            xbl = xb + 15
        # Поймал 3
        elif ybl >= y + 215 and ybl <= y + 265:
            ybl = y + 240
            atk = b
            sxbl = 0
            sybl = 0
            xbl = xb + 15

    if uw == 1:
        xw += 0
        xwn += 0
        xm, ym = pygame.mouse.get_pos()
        yuw = round(ym * 2 / 9) + 250
        pygame.draw.line(screen, black, [xbl, ybl], [xuw, yuw])

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
