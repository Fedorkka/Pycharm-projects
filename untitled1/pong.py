import pygame, time
import random
import numpy as np


class Mind:
    def __init__(self):
        self.layers = np.array(
            [2 * np.random.random((4, 12)) - 1, 2 * np.random.random((12, 1)) - 1])

    def step(self, input_layer):
        input_layer = np.array(input_layer)
        r1 = sigmoid(np.dot(input_layer, self.layers[0]))
        output = sigmoid(np.dot(r1, self.layers[1]))
        return output



def sigmoid(x):
    return 1 / (1 + np.exp(x))


def cross(n1, n2):
    nn = Mind()
    for i in range(len(n1.layers)):
        for z in range(len(n1.layers[i])):
            for k in range(len(n1.layers[i][z])):
                nn.layers[i][z, k]= random.choices([n1.layers[i][z, k],n2.layers[i][z, k]])[0]

    return nn


def mutation(n):
    for i in range(len(n.layers)):
        for z in range(len(n.layers[i])):
            for k in range(len(n.layers[i][z])):
                mutation = random.choices([True, False], weights=[0.1, 0.9])
                if mutation[0]:
                    n.layers[i][z, k]+= (2*random.random()-1)/10


def new_population():
    global population, p
    population.sort(key=lambda k: k[1], reverse=True)
    new_population = []
    for i in range(int(0.4*population_K)):
        new_population.append([population[i][0], 0])
    for i in range(int(0.1*population_K)):
        new_population.append([cross(random.choices(population[0:int(0.1*population_K)])[0][0], random.choices(population[int(0.1*population_K):int(0.2*population_K)])[0][0]), 0])
    for i in range(int(0.3*population_K)):
        new_population.append([cross(random.choices(population[0:int(0.2*population_K)])[0][0], random.choices(population[int(0.2*population_K):int(0.4*population_K)])[0][0]), 0])
    for i in range(int(0.2*population_K)):
        new_population.append([random.choices(population[0:int(0.4*population_K)])[0][0], 0])
    for i in new_population[int(0.4*population_K):]:
        mutation(i[0])
    population = new_population
    p += 1


class Platform:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.h = 0
        self.w = 0
        self.vu = 2
        self.vd = 2
        self.a = 0.1

    def set_coord(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        if self.y < 0:
            self.y = 0
        if self.y > 550:
            self.y = 550

    def get_coord(self):
        return [self.x, self.y, self.h, self.w]


class Ball:
    global kk, timer
    kk=1
    timer= 1000
    def __init__(self):
        global kk
        self.x = 395
        self.y = 295
        self.vx = 4*kk
        self.vy = 0

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def move(self):
        global pl1, score, k, population, steps, fitness, max_fitness, choices, b_choices, gen,  kk, timer
        self.x += self.vx
        self.y += self.vy
        if 790 < self.x or self.x < 0 or timer< 0:
            """self.__init__()"""

            if self.x > 790 or timer< 0:
                timer= 1000
                kk= -kk
                self.__init__()
                fitness= steps+(400-abs(pl1.y-self.y))/10
                population[k][1] = fitness
                k += 1
                pl1.y = 275
                pl1.vu=2
                pl1.vd= 2

                score = 0
                steps = 0
                if k == population_K:
                    k= 0
                    new_population()
            if self.x<0:
                score+=1
                timer+=1000
                kk= -kk
                fitness += abs(pl2.y - ball.y)
                self.__init__()



        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        if self.y > 590:
            self.y = 590
            self.vy = -self.vy
        if self.x + 10 > pl1.x and pl1.y + 59 > self.y > pl1.y - 9:
            self.x=pl1.x-10
            self.vx= -self.vx
            if pl1.vu>pl1.vd:
                self.vy = self.vy + pl1.vu - 2
            else:
                self.vy = self.vy + pl1.vd - 2

        if self.x< pl2.x+10 and pl2.y + 59 > self.y > pl2.y - 9:
            self.x = pl2.x + 10
            self.vx = -self.vx




pygame.init()
pygame.font.init()
black = (0, 0, 0)
white = (255, 255, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
color = (255, 255, 255)
x_s = 800
y_s = 600

screen = pygame.display.set_mode((x_s, y_s))
screen.fill(white)

clock = pygame.time.Clock()
global pl1, steps, score, k, population, done, p, fitness, max_fitness, population_K, timer
done = False
pl1 = Platform()
pl2= Platform()
pl1.y = 275
pl2.y = 275
ball = Ball()
pygame.mouse.set_visible(0)
up = False
down = False
population_K= 10
population = [[Mind(), 0] for i in range(population_K)]
k = 0
steps = 0
score = 0
ch = None
f = pygame.font.SysFont("Arial", 12)

p = 1
fitness= 0
max_fitness= 0
u_c=0
d_c= 0
s_c=0

def get_speed():
    return -pygame.mouse.get_rel()[1]


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


            if event.key == pygame.K_DOWN:
                down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True


    screen.fill(black)

    res = population[k][0].step([pl1.x- ball.x, abs(pl1.y- ball.y), ball.x, abs(pl2.y-ball.y)])

    if res[0]>0.5:
        ch = "UP"
    else:
        ch = "DOWN"



    if ch == "UP":
        up = True
        down = False
    if ch == "DOWN":
        down = True
        up = False

    steps += 1
    timer-=1

    if down:
        pl1.vu= 2
        pl1.vd+=pl1.a
        pl1.y += pl1.vd
    if up:
        pl1.vd= 2
        pl1.vu += pl1.a
        pl1.y -= pl1.vu
    pl1.set_coord(790, pl1.y, 10, 50)
    pl2.v= 3
    if ball.y+5>pl2.y:
        pl2.y+=pl2.v
    elif ball.y<pl2.y+25:
        pl2.y-=pl2.v
    pl2.set_coord(0, pl2.y, 10, 50)
    ball.move()
    for i in range(41):
        pygame.draw.rect(screen,(150, 150, 150), [398, 15*i,4, 10])
    pygame.draw.rect(screen, white, [ball.x, ball.y, 10, 10])
    pygame.draw.rect(screen, white, pl1.get_coord())
    pygame.draw.rect(screen, white, pl2.get_coord())
    text = f.render(
        "Популяция: " + str(p)+" ||Особь: "+str(k+1)+" ||Таймер: "+ str(timer) +" ||Счет: "+str(score)+" ||Выход: "+ str(list(res)), 1, white)
    screen.blit(text, (5, 5))





    pygame.display.flip()
    clock.tick(180)
pygame.quit()
