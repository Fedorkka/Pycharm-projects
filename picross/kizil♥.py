from tkinter import *
from tkinter import filedialog
import pygame
from tkinter import *
import uuid

global pic, img_size, pic

def click(x, y):
    if pic[x][y] == 0:
        pic[x][y] = 1


def delite(x, y):
    if pic[x][y] == 1:
        pic[x][y] = 0


def clear():
    for i in range(img_size[0]):
        for z in range(img_size[1]):
            pic[i][z] = 0


def save():
    global save_stage
    root = Tk()
    root.withdraw()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", initialfile=str(uuid.uuid4()))
    t = ""
    if f is None:
        return
    for i in range(img_size[1]):
        for z in range(img_size[0]):
            t += str(pic[z][i])
        t += "\n"
    text2save = str(t)
    f.write(text2save)
    f.close()
    root.destroy()
    root.mainloop()


def fnew_sizeX():
    global max_y, s_x, s_y, root
    root = Tk()
    l1 = Label(root, text="Введите Длинну(x)")
    l1.pack()
    s_x = Scale(root, orient=HORIZONTAL, length=300, from_=1, to=100, tickinterval=10, resolution=1)
    s_x.pack()
    b = Button(root, text="OK", command=save_varX)
    b.pack()
    root.mainloop()


def save_varX():
    global max_y, s_x, s_y, root, done
    done= True
    max_y = s_x.get() * 3
    img_size[0] = s_x.get()
    root.destroy()
    fnew_sizeY()

def fnew_sizeY():
    global max_y, s_x, s_y, root
    root = Tk()
    l1 = Label(root, text="Введите Ширину(y)")
    l1.pack()
    s_y = Scale(root, orient=HORIZONTAL, length=300, from_=1, to=max_y, tickinterval=10, resolution=1)
    s_y.pack()
    b = Button(root, text="OK", command=save_varY)
    b.pack()
    root.mainloop()


def save_varY():
    global max_y, s_x, s_y, root
    img_size[1] = s_y.get()
    root.destroy()

    program()

def program():
    global pic, img_size, pic, save_stage

    global done
    black = (0, 0, 0)
    gray = (150, 150, 150)
    if img_size[0] > img_size[1]:
        cell_s = int(800 / img_size[0])
    else:
        cell_s = int(800 / img_size[1])
    pic = []
    l_w = 2
    for i in range(img_size[0]):
        pic.append([])
        for z in range(img_size[1]):
            pic[i].append(0)
    size = (
        cell_s + cell_s * img_size[0] + l_w * (img_size[0] + 1),
        20 + cell_s + cell_s * img_size[1] + l_w * (img_size[1] + 1))
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Picross Generator")
    done = False
    clock = pygame.time.Clock()
    surf = pygame.Surface((cell_s, cell_s))
    surf.set_alpha(77)
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 16)
    b_clear = myfont.render("Очистить", False, (0, 0, 0))
    save_f = myfont.render("Сохранить", False, (0, 0, 0))
    new_size = myfont.render("Новый", False, (0, 0, 0))
    surf2 = pygame.Surface((b_clear.get_width() + 10, b_clear.get_height() + 2))
    surf2.set_alpha(20)
    surf3 = pygame.Surface((save_f.get_width() + 10, save_f.get_height() + 2))
    surf3.set_alpha(20)
    surf4 = pygame.Surface(((20 - new_size.get_height()) / 2, new_size.get_width() + 10))
    surf4.set_alpha(20)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255, 255, 255))
        x, y = pygame.mouse.get_pos()
        x_c = int((x - cell_s / 2 + l_w) // (cell_s + l_w))
        y_c = int((y - cell_s / 2 - 20 + l_w) // (cell_s + l_w))

        for i in range(img_size[0] + 1):
            pygame.draw.line(screen, black, [cell_s / 2 + i * (cell_s + l_w), cell_s / 2 + 20],
                             [cell_s / 2 + i * (cell_s + l_w), size[1] - cell_s / 2 - l_w], l_w)
        for i in range(img_size[1] + 1):
            pygame.draw.line(screen, black, [cell_s / 2, cell_s / 2 + 20 + i * (cell_s + l_w)],
                             [size[0] - cell_s / 2 - l_w, cell_s / 2 + 20 + i * (cell_s + l_w)], l_w)
        for i in range(len(pic)):
            for z in range(len(pic[i])):
                if pic[i][z] == 1:
                    pygame.draw.rect(screen, black, (
                        cell_s / 2 + l_w + cell_s * i + l_w * i, cell_s / 2 + 20 + l_w + cell_s * z + l_w * z, cell_s,
                        cell_s))
        if cell_s / 2 < x < size[0] - cell_s / 2 - 2 * l_w and cell_s / 2 + 20 < y < size[1] - cell_s / 2 - 2 * l_w:

            if pic[x_c][y_c] == 0:
                surf.fill((255, 200, 0))

            else:
                surf.fill((0, 239, 255))

            screen.blit(surf,
                        (cell_s / 2 + l_w + cell_s * x_c + l_w * x_c, cell_s / 2 + 20 + l_w + cell_s * y_c + l_w * y_c))

            if pygame.mouse.get_pressed()[0] == 1 and not save_stage:
                click(x_c, y_c)
            if pygame.mouse.get_pressed()[2] == 1:
                delite(x_c, y_c)
            text_c = myfont.render('x= ' + str(x_c + 1) + " " + "y= " + str(y_c + 1), False, (0, 0, 0))
            screen.blit(text_c, (cell_s / 2, (20 - text_c.get_height()) / 2))

        screen.blit(b_clear, (cell_s / 2 + 80, (20 - b_clear.get_height()) / 2))
        screen.blit(save_f, (cell_s / 2 + 100 + b_clear.get_width(), (20 - save_f.get_height()) / 2))
        screen.blit(new_size,
                    (cell_s / 2 + 120 + b_clear.get_width() + save_f.get_width(), (20 - new_size.get_height()) / 2))
        if cell_s / 2 + 70 < x < cell_s / 2 + 80 + b_clear.get_width() + 10 and (20 - b_clear.get_height()) / 2 < y < (
                20 - b_clear.get_height()) / 2 + b_clear.get_height():
            pygame.draw.rect(screen, (150, 150, 150), (
                cell_s / 2 + 75, (20 - b_clear.get_height() - 2) / 2, b_clear.get_width() + 10,
                b_clear.get_height() + 2), 1)
            surf2.fill((200, 200, 200))
            screen.blit(surf2, (cell_s / 2 + 75, (20 - b_clear.get_height() - 2) / 2))
            if pygame.mouse.get_pressed()[0] == 1:
                clear()
        if cell_s / 2 + 100 + b_clear.get_width() < x < cell_s / 2 + 100 + b_clear.get_width() + save_f.get_width() and (
                20 - save_f.get_height()) / 2 < y < (20 - save_f.get_height()) / 2 + save_f.get_height():
            pygame.draw.rect(screen, (150, 150, 150), (
                cell_s / 2 + 100 + b_clear.get_width() - 5, (20 - save_f.get_height()) / 2, save_f.get_width() + 10,
                save_f.get_height() + 2), 1)
            surf3.fill((200, 200, 200))
            screen.blit(surf3, (cell_s / 2 + 100 + b_clear.get_width() - 5, (20 - save_f.get_height()) / 2))
            if pygame.mouse.get_pressed()[0] == 1:
                save_stage= True
                save()
            save_stage = False
        if cell_s / 2 + 120 + b_clear.get_width() + save_f.get_width() < x < cell_s / 2 + 120 + b_clear.get_width() + save_f.get_width() + new_size.get_width() and (
                20 - new_size.get_height()) / 2 < y < (20 - new_size.get_height()) / 2 + new_size.get_height():
            pygame.draw.rect(screen, (150, 150, 150), (
                cell_s / 2 + 120 + b_clear.get_width() + save_f.get_width() - 5, (20 - new_size.get_height()) / 2,
                new_size.get_width() + 10, new_size.get_height() + 2), 1)
            surf4.fill((200, 200, 200))
            screen.blit(surf4,
                        (cell_s / 2 + 120 + b_clear.get_width() + save_f.get_width() - 5,
                         (20 - new_size.get_height()) / 2))
            if pygame.mouse.get_pressed()[0] == 1:
                fnew_sizeX()

        pygame.display.flip()
        clock.tick(120)
    pygame.quit()
save_stage= False
img_size = [40, 40]  ##Размер поля(x, y)
program()







