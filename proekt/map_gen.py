import pygame
from random import choice

# ... Настройки ..................................................................................................
 # размер окна
step = 30  # размер шага и комнаты(-2)
quantity = 20  # кол-во комнат
accuracy = 2  # кучность(падает при уменьшении)
side_room_chance = 3  # вероятность боковых комнат(при значении 'x' вероятность появления будет x к x+5)
side_room_qu_chance = 2  # вероятность двойных боковых комнат(при значении 'n' вероятность появления будет n к n+10)
#  ...............................................................................................................

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
color = (255, 255, 0)
map = []
l_side = None
side_room = 0
side_room_m = [0, 0, 0, 0, 0]
side_room_qu_m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
block = 0
k = 0
fix = [[step, step], [step, -step], [-step, -step], [-step, step], [step*2, 0], [-step*2, 0], [0, step*2], [0, -step*2]]

for i in range(side_room_chance):
    side_room_m.append(1)

for i in range(side_room_qu_chance):
    side_room_qu_m.append(1)


def dell(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


def gen():
    global size, l_side, side, x, y, side_room, block, k
    map = []
    repeat = 0
    screen.fill(white)
    while len(map) < quantity:
        if block == 0:
            side_m = ['left', 'right', 'up', 'down']
        block = 0
        if len(map) == 0:
            x = size[0] / 2 - quantity
            y = size[1] / 2 - quantity
            map.append([x, y])
        else:
            if l_side == 'left':
                side_m = list(set(side_m) - {'right'})
            if l_side == 'right':
                side_m = list(set(side_m) - {'left'})
            if l_side == 'up':
                side_m = list(set(side_m) - {'down'})
            if l_side == 'down':
                side_m = list(set(side_m) - {'up'})
            if repeat == accuracy:
                if l_side == 'left':
                    side_m = list(set(side_m) - {'left'})
                if l_side == 'right':
                    side_m = list(set(side_m) - {'right'})
                if l_side == 'up':
                    side_m = list(set(side_m) - {'up'})
                if l_side == 'down':
                    side_m = list(set(side_m) - {'down'})
            side = choice(side_m)
            if l_side == side:
                repeat += 1
            else:
                repeat = 0

            l_side = side
            if len(map) < quantity - 1:
                side_room = choice(side_room_m)
                side_room_qu = choice(side_room_qu_m)
            if side == 'left':
                x -= step * 2
                map.append([x + step, y])
                if len(map) < quantity:
                    map.append([x, y])
                else:
                    side_room = 0
                if side_room == 1:
                    ch = choice([step, -step])
                    map.append([x, y + ch])
                    if ch == -step:
                        side_m = ['left', 'right', 'down']
                        block = 1
                    if ch == step:
                        side_m = ['left', 'right', 'up']
                        block = 1
                    if side_room_qu == 1:
                        map.append([x, y + ch * 2])

            if side == 'right':
                x += step * 2
                map.append([x - step, y])
                if len(map) < quantity:
                    map.append([x, y])
                else:
                    side_room = 0
                if side_room == 1:
                    ch = choice([step, -step])
                    map.append([x, y + ch])
                    if ch == -step:
                        side_m = ['left', 'right', 'down']
                        block = 1
                    if ch == step:
                        side_m = ['left', 'right', 'up']
                        block = 1
                    if side_room_qu == 1:
                        map.append([x, y + ch * 2])
            if side == 'up':
                y -= step * 2
                map.append([x, y + step])
                if len(map) < quantity:
                    map.append([x, y])
                else:
                    side_room = 0
                if side_room == 1:
                    ch = choice([step, -step])
                    map.append([x + ch, y])
                    if ch == -step:
                        side_m = ['up', 'right', 'down']
                        block = 1
                    if ch == step:
                        side_m = ['left', 'right', 'down']
                        block = 1
                    if side_room_qu == 1:
                        map.append([x + ch * 2, y])
            if side == 'down':
                y += step * 2
                map.append([x, y - step])
                if len(map) < quantity:
                    map.append([x, y])
                else:
                    side_room = 0
                if side_room == 1:
                    ch = choice([step, -step])
                    map.append([x + ch, y])
                    if ch == -step:
                        side_m = ['up', 'right', 'down']
                        block = 1
                    if ch == step:
                        side_m = ['left', 'right', 'down']
                        block = 1
                    if side_room_qu == 1:
                        map.append([x + ch * 2, y])
            if len(map)> quantity:
                while len(map) > quantity:
                    map.pop(len(map) - 1)
            dell(map)



    for i in range(len(map)):
        pygame.draw.rect(screen, black, [map[i][0], map[i][1], step - 2, step - 2], 2)
    pygame.draw.rect(screen, green, [map[0][0], map[0][1], step - 2, step - 2], 2)
    pygame.draw.rect(screen, red, [map[quantity - 1][0], map[quantity - 1][1], step - 2, step - 2], 2)
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode(list(size))
screen.fill(white)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            gen()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
