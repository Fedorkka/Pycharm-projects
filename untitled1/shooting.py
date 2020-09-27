import math
import pygame
import random
import time


class Bullet:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

    def draw(self):
        pygame.draw.rect(screen, black, [self.x, self.y, 2, 2])


class Gun:
    def __init__(self, bullet_interval, spread_angle, delta_angle, interval, function, bullet_v):
        self.spread_angle = spread_angle
        self.delta_angle = delta_angle
        self.interval = interval
        self.function = function
        self.bullet_v = bullet_v
        self.bullet_interval = bullet_interval

    def get_bullet_speed(self, pl_x, pl_y, mouse_x, mouse_y, queue_time):
        k = int(self.spread_angle + self.delta_angle * self.function(queue_time / self.interval))
        s_angle = random.randint(-k, k)
        if mouse_x - pl_x == 0:
            if mouse_y> pl.y:
                angle = math.radians(270+s_angle)
            else:
                angle = math.radians(90 + s_angle)

        else:
            angle = math.atan((mouse_y - pl_y) / (mouse_x - pl_x)) + math.radians(s_angle)

        if mouse_x > pl_x:
            return self.bullet_v * math.cos(angle), self.bullet_v * math.sin(angle)
        return -self.bullet_v * math.cos(angle), -self.bullet_v * math.sin(angle)


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y


pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
x_s = 800
y_s = 800
size = (x_s, y_s)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
released = False
delta = 0
pl = Player(400, 400)
minigun = Gun(10, 0, 5, 1000, lambda x: (2 / (1 + math.exp(-4 * x))) - 1, 10)

bullets = []
new_list = []
interval_time = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)
    t = time.time() * 1000
    m_x, m_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if not released:
            released = True
            interval_time = t
        if t - interval_time > minigun.bullet_interval:
            interval_time = t
            delta += minigun.bullet_interval

            bv_x, bv_y = minigun.get_bullet_speed(pl.x, pl.y, m_x, m_y, delta)
            bullets.append(Bullet(pl.x, pl.y, bv_x, bv_y))
    else:
        if released:
            if delta > minigun.interval:
                delta = minigun.interval
            released = False
        if delta > 0:
            if t - interval_time > minigun.bullet_interval:
                interval_time = t
                delta -= minigun.bullet_interval//2
        else:
            delta = 0

    for i in bullets:
        i.move()
        i.draw()
        if 0 < i.x < x_s and 0 < i.y < y_s:
            new_list.append(i)
    bullets = new_list
    new_list = []

    pygame.display.flip()
    clock.tick(100)
pygame.quit()
