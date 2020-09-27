import pygame
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

xs = 600
y = 350
xbl = xs
ybl = y
sxbl=0
sybl=0
sd=2
n=0
w=1
b=2
atk = n
updt=n
sw = 0
sb = 0
g=0

ywg = 325
ybg = 325

xw = 500
xwn = xw
xuw=1100
uw=0

xb = 700
xbn = xb
xub=100
ub=0

size = (1200, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('WWPL 18')

done = False
clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if atk==w:
                if pygame.mouse.get_pressed()[0] == 1:
                    uw=1
                if pygame.mouse.get_pressed()[2] == 1:
                    uw=0
            elif atk==b:
                if pygame.mouse.get_pressed()[0] == 1:
                    ub=1
                if pygame.mouse.get_pressed()[2] == 1:
                    ub=0

        if event.type == pygame.KEYDOWN:
            print(event.key)
            # Старт
            if event.key == 13:
                if atk==n:
                    updt = w
                    if updt == w:
                        xwn = xs
                        atk = w
                    if updt == b:
                        xbn = xs
                        atk = b

                    g=0
                    updt=n
            # Кнопки атаки белых
            if atk == w:
                # Проверяем наличие мяча у игрока
                if (xbl==xwn-15 and ybl==y) or (xbl==xw-15 and(ybl==y-240 or ybl==y+240))or(xbl==xub+40 and ybl==ywg+25):
                    #Пас 1
                    if event.key==49:
                        sxbl=round((xwn-15-xbl)/5)
                        sybl=round((y-ybl)/5)
                        if xwn<xuw-170:
                            sxbl+=sd+1
                    #Пас 2
                    if event.key==50:
                        sxbl=round((xw-15-xbl)/10)
                        sybl=round((y-240-ybl)/10)
                        if xw<xuw-320:
                            sxbl+=sd
                    #Пас 3
                    if event.key==51:
                        sxbl = round((xw - 15 - xbl) / 10)
                        sybl = round((y + 240 - ybl) / 10)
                        if xw < xuw - 320:
                            sxbl += sd
                    if event.key == 97:
                        uw = 0
                        sxbl = round((xuw-xbl)/5)
                        sybl = round((yu - ybl)/5)

            #Кнопки атаки синих
            if atk==b:
                if (xbl==xbn+15 and ybl==y)or(xbl==xb+15 and(ybl==y-240 or ybl==y+240))or(xbl==xuw-40 and ybl==ybg+25):
                    if event.key==257:
                        sxbl=round((xbn+15-xbl)/5)
                        sybl=round((y-ybl)/5)
                        if xbn>xub+170:
                            sxbl-=sd+1
                    if event.key == 258:
                        sxbl = round((xb+15 - xbl) / 10)
                        sybl = round((y - 240 - ybl) / 10)
                        if xw > xuw + 320:
                            sxbl -= sd
                    # Пас 3
                    if event.key == 259:
                        sxbl = round((xb+15 - xbl) / 10)
                        sybl = round((y + 240 - ybl) / 10)
                        if xw > xuw + 320:
                            sxbl -= sd
                    #Удар
                    if event.key==256:
                        ub=0
                        sxbl = round((xub - xbl) / 5)
                        sybl = round((yu - ybl) / 5)

    screen.fill(white)

# Gameplace
    pygame.draw.rect(screen, pec, [100, 0, 1000, 700])
    pygame.draw.rect(screen, lightblue, [150, 50, 900, 600])
    pygame.draw.line(screen, pec2, [100, 0], [150, 50], 5)
    pygame.draw.line(screen, pec2, [1050, 50], [1100, 0], 5)
    pygame.draw.line(screen, pec2, [100, 700], [150, 650], 5)
    pygame.draw.line(screen, pec2, [1050, 650], [1100, 700], 5)
    pygame.draw.lines(screen, black, False, [[xub, 260], [xub-80, 260], [xub-80, 440], [xub, 440]], 5)
    pygame.draw.lines(screen, black, False, [[xuw, 260], [xuw+80, 260], [xuw+80, 440], [xuw, 440]], 5)

# White player 1
    pygame.draw.circle(screen, white, [xwn, y], 25)
    pygame.draw.circle(screen, black, [xwn, y], 25, 3)
    fontp = pygame.font.SysFont("Gotham Pro Narrow Bold", 50)
    text = fontp.render('1', True, black)
    screen.blit(text, [xwn - 10, y - 15])
# White player 2
    pygame.draw.circle(screen, white, [xw, y - 240], 25)
    pygame.draw.circle(screen, black, [xw, y - 240], 25, 3)
    text = fontp.render('2', True, black)
    screen.blit(text, [xw - 10, y - 255])
# White player 3
    pygame.draw.circle(screen, white, [xw, y + 240], 25)
    pygame.draw.circle(screen, black, [xw, y + 240], 25, 3)
    text = fontp.render('3', True, black)
    screen.blit(text, [xw - 10, y + 225])
# white goalkeeper
    pygame.draw.ellipse(screen, darkred, [xub, ywg, 40, 50])
    pygame.draw.ellipse(screen, white, [xub, ywg, 40, 50], 3)

# Blue player 1
    pygame.draw.circle(screen, blue, [xbn, y], 25)
    pygame.draw.circle(screen, white, [xbn, y], 25, 3)
    text = fontp.render('1', True, white)
    screen.blit(text, [xbn - 10, y - 15])
# Blue player 2
    pygame.draw.circle(screen, blue, [xb, y - 240], 25)
    pygame.draw.circle(screen, white, [xb, y - 240], 25, 3)
    text = fontp.render('2', True, white)
    screen.blit(text, [xb - 10, y - 255])
# Blue player 3
    pygame.draw.circle(screen, blue, [xb, y + 240], 25)
    pygame.draw.circle(screen, white, [xb, y + 240], 25, 3)
    text = fontp.render('3', True, white)
    screen.blit(text, [xb - 10, y + 225])
# Blue goalkeeper
    pygame.draw.ellipse(screen, darkred, [xuw-40, ybg, 40, 50])
    pygame.draw.ellipse(screen, blue, [xuw-40, ybg, 40, 50], 3)

# Ball
    pygame.draw.circle(screen, red, [xbl, ybl], 15)

# Счёт
    fontc = pygame.font.SysFont("Gotham Pro Narrow Bold", 200)
    text = fontc.render(str(sw) + ':' + str(sb), True, black)
    screen.blit(text, [500, 710])

# Описание управления
    fonty = pygame.font.SysFont("Gotham Pro Narrow Bold", 30)
    text = fonty.render('Пас белому игроку 1:   1', True, black)
    screen.blit(text, [100, 710])
    text = fonty.render('Пас белому игроку 2:   2', True, black)
    screen.blit(text, [100, 740])
    text = fonty.render('Пас белому игроку 3:   3', True, black)
    screen.blit(text, [100, 770])
    text = fonty.render('Удар:   ЛКМ, потом A', True, black)
    screen.blit(text, [100, 800])
    text = fonty.render('Отбор:   S', True, black)
    screen.blit(text, [100, 830])

    text = fonty.render('Пас синему игроку 1:  Numpad 1', True, black)
    screen.blit(text, [805, 710])
    text = fonty.render('Пас синему игроку 2:  Numpad 2', True, black)
    screen.blit(text, [805, 740])
    text = fonty.render('Пас синмеу игроку 3:  Numpad 3', True, black)
    screen.blit(text, [805, 770])
    text = fonty.render('Удар:   ЛКМ, потом Numpad 0', True, black)
    screen.blit(text, [805, 800])
    text = fonty.render('Отбор:   Numpad Точка', True, black)
    screen.blit(text, [805, 830])

# goalkeepers action
    if xbl <= 600:
        if ywg + 25 > ybl:
            ywg -= 4
    if ywg + 25 < ybl:
        ywg += 4
    if ywg <= 225:
        ywg = 225
    if ywg >= 425:
        ywg = 425
    if xbl >= 600:
        if ybg + 25 > ybl:
            ybg -= 4
    if ybg + 25 < ybl:
        ybg += 4
    if ybg <= 225:
        ybg = 225
    if ybg >= 425:
        ybg = 425

# Players action
    if atk == w:
        xw += sd
        xwn += sd+1
        xb += sd+2
        xbn += sd+2
        if xw >= xuw-320:
            xw = xuw-320
        if xwn >= xuw-170:
            xwn = xuw-170
        if xb >= xuw-280:
            xb = xuw-280
        if xbn >= xuw-130:
            xbn = xuw-130
    elif atk == b:
        xb -= sd
        xbn -= sd+1
        xw -= sd+2
        xwn -= sd+2
        if xw <= xub+280:
            xw = xub+280
        if xwn <= xub+130:
            xwn = xub+130
        if xb <= xub+320:
            xb = xub+320
        if xbn <= xub+170:
            xbn = xub+170
    elif atk == n:
        xw += 0
        xwn += 0
        xb += 0
        xbn += 0

# Ball action
    xbl+=sxbl
    ybl+=sybl

    # Поймали белые
    # Поймал 1
    if ((ybl >= y - 25 and ybl <= y + 25)and(xbl <= xwn + 25 and xbl >= xwn - 25))or(ybl==y and (xbl>=xwn-40 and xbl<=xwn+25)):
            xbl=xwn-15
            atk = w
            sxbl = 0
            sybl = 0
            ybl = y
    # Поймал 2 или 3
    if (xbl <= xw+25 and xbl >= xw-25):
        #Поймал 2
        if ybl >= y - 265 and ybl <= y - 215:
            ybl=y-240
            atk = w
            sxbl = 0
            sybl = 0
            xbl = xw - 15
        # Поймал 3
        elif ybl >= y + 215 and ybl <= y + 265:
            ybl=y+240
            atk = w
            sxbl = 0
            sybl = 0
            xbl = xw - 15
    #Поймал вратарь
    if (xbl>=xub and xbl<=xub+40)and(ybl>=ywg and ybl<=ywg+50):
        atk=w
        xbl=xub+40
        ybl=ywg+25
        sxbl=0
        sybl=0

    # Поймали синие
    # Поймал 1
    if (ybl >= y - 25 and ybl <= y + 25)and(xbl <= xbn + 25 and xbl >= xbn - 25):
            xbl=xbn+15
            atk = b
            sxbl = 0
            sybl = 0
            ybl = y
    # Поймал 2 или 3
    if (xbl <= xb + 25 and xbl >= xb-25):
        # Поймал 2
        if ybl >= y - 265 and ybl <= y - 215:
            ybl=y-240
            atk = b
            sxbl = 0
            sybl = 0
            xbl = xb + 15
        # Поймал 3
        elif ybl >= y + 215 and ybl <= y + 265:
            ybl=y+240
            atk = b
            sxbl = 0
            sybl = 0
            xbl = xb + 15
    #Поймал вратарь
    if (xbl >= xuw-40 and xbl <= xuw) and (ybl >= ybg and ybl <= ybg + 50):
        atk = b
        xbl = xuw- 40
        ybl = ybg + 25
        sxbl = 0
        sybl = 0

    fontg = pygame.font.SysFont("Gotham Pro Narrow Bold", 100)
    if ybl>=260 and ybl<=440:
        if xbl<xub-15:
            sxbl=0
            sybl=0
            text = fontg.render('ГОЛ! ЗАБИЛИ СИНИЕ', True, black)
            screen.blit(text, [240, 250])
            g+=1
        elif xbl>xuw+15:
            sxbl = 0
            sybl = 0
            text = fontg.render('ГОЛ! ЗАБИЛИ БЕЛЫЕ', True, black)
            screen.blit(text, [240, 250])
            g += 1
    if g >= 60:
        if xbl < xub - 15:
            updt = b
            sb+=1
        elif xbl > xuw + 15:
            updt=w
            sw+=1
    if updt!=n:
        atk=n
        xw=500
        xwn=xw
        xb=700
        xbn=xb
        xbl=xs
        ybl=y
        sxbl=0
        sybl=0
        ywg=325
        ybg=325

    xm, ym = pygame.mouse.get_pos()
    if uw==1:
        yu = round(ym*3/10) + 260
        pygame.draw.line(screen, black, [xbl, ybl], [xuw, yu], 2)
    if ub==1:
        yu = round(ym*3/10) + 260
        pygame.draw.line(screen, black, [xbl, ybl], [xub, yu], 2)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()