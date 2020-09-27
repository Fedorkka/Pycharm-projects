import numpy as np
import random


class Mind:
    def __init__(self, sizes):
        arr = []
        self.sizes = sizes
        for i in range(len(sizes) - 1):
            arr.append(2 * np.random.random((sizes[i], sizes[i + 1])) - 1)
        self.layers = np.array(arr)

    def step(self, input_layer):
        input_layer = np.array(input_layer)
        r = sigmoid(np.dot(input_layer, self.layers[0]))
        if len(self.layers) > 1:
            for i in range(1, len(self.layers)):
                r = sigmoid(np.dot(r, self.layers[i]))
        return r

        r2 = sigmoid(np.dot(r1, self.layers[1]))
        r3 = sigmoid(np.dot(r2, self.layers[2]))
        output = sigmoid(np.dot(r3, self.layers[3]))
        return output


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def cross(n1, n2):
    nn = Mind(n1.sizes)
    for i in range(len(n1.layers)):
        for z in range(len(n1.layers[i])):
            for k in range(len(n1.layers[i][z])):
                nn.layers[i][z, k] = random.choices([n1.layers[i][z, k], n2.layers[i][z, k]])[0]

    return nn


def mutation(n):
    for i in range(len(n.layers)):
        for z in range(len(n.layers[i])):
            for k in range(len(n.layers[i][z])):
                mutation = random.choices([True, False], weights=[0.1, 0.9])
                if mutation[0]:
                    n.layers[i][z, k] += (2 * random.random() - 1) / 10


def new_population(population):
    population_K = len(population)
    population.sort(key=lambda k: k[1], reverse=True)
    new_population = []
    for i in range(int(0.4 * population_K)):
        new_population.append([population[i][0], 0])
    for i in range(int(0.1 * population_K)):
        new_population.append([cross(random.choices(population[0:int(0.1 * population_K)])[0][0],
                                     random.choices(population[int(0.1 * population_K):int(0.2 * population_K)])[0][0]),
                               0])
    for i in range(int(0.3 * population_K)):
        new_population.append([cross(random.choices(population[0:int(0.2 * population_K)])[0][0],
                                     random.choices(population[int(0.2 * population_K):int(0.4 * population_K)])[0][0]),
                               0])
    for i in range(int(0.2 * population_K)):
        new_population.append([random.choices(population[0:int(0.4 * population_K)])[0][0], 0])
    for i in new_population[int(0.4 * population_K):]:
        mutation(i[0])
    return new_population


population = [[Mind([1, 6, 1]), 0] for i in range(10)]
for i in range(2000):


    print(i)
    population = new_population(population)

while True:
    a = int(input())
    out = list(population[0][0].step([a]))
    print(out.index(max(out)))
