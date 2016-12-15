from random import random
from time import time
from math import cos, sin

RADIUS = 10
DROP_COUNT = 10
TAIL_LEN = 100
RANDOM_DY_FACTOR = 0
RANDOM_DX_FACTOR = 0
DX_STEP = 0
DY_STEP = 2

TIME_DEPENDENCE = True
DX_TIME_PERIOD = 0.5
DY_TIME_PERIOD = 0.3
WIDE_X = 2
WIDE_Y = 1


def coords_sum(first_coordinates, second_coordinates):
    return first_coordinates[0] + second_coordinates[0],\
           first_coordinates[1] + second_coordinates[1]


class Circle:
    def __init__(self, radius, alpha, coords):
        self.radius = radius
        self.alpha = alpha
        self.coords = coords

    def __repr__(self):
        return "Circle({}, {}, {}".format(self.radius, self.alpha, self.coords)


class Drop:
    def __init__(self, length, coords, step_x, step_y):
        self.circles = []
        self.step_x = step_x
        self.step_y = step_y
        for index in range(length):
            self.circles = [Circle(RADIUS, 1, (coords[0] + index * step_x, coords[1] - index * step_y))] + self.circles

    def __repr__(self):
        return "Drop(circles: {})".format(self.circles)


class Model:
    def __init__(self, width, height):
        # DX_STEP = 1
        # DY_STEP = 1
        self.drops = []
        self.width = width
        self.height = height
        for index in range(DROP_COUNT):
            self.drops.append(Drop(TAIL_LEN, (width * random(), height * random()), DX_STEP, DY_STEP))

    def update(self):
        if TIME_DEPENDENCE:
            step_x = WIDE_X * cos(time() * DX_TIME_PERIOD)
            step_y = WIDE_Y * sin(time() * DY_TIME_PERIOD)
        for index in range(len(self.drops)):
            drop = self.drops[index]
            if not TIME_DEPENDENCE:
                step_x = drop.step_x
                step_y = drop.step_y
            last_circle = drop.circles[-1]
            drop.circles = drop.circles[1:]
            last_radius = last_circle.radius
            last_coordinates = last_circle.coords
            first_circle = Circle(
                last_radius, 1, coords_sum(last_coordinates,
                                           (step_x + random() * RANDOM_DX_FACTOR - RANDOM_DX_FACTOR / 2,
                                            step_y + random() * RANDOM_DY_FACTOR - RANDOM_DY_FACTOR / 2)))
            if first_circle.coords[0] > self.width:
                new_x = first_circle.coords[0] - self.width
                first_circle.coords = (new_x, first_circle.coords[1])

            if first_circle.coords[0] < 0:
                new_x = first_circle.coords[0] + self.width
                first_circle.coords = (new_x, first_circle.coords[1])

            if first_circle.coords[1] > self.height:
                new_y = first_circle.coords[1] - self.height
                first_circle.coords = (first_circle.coords[0], new_y)

            if first_circle.coords[1] < 0:
                new_y = first_circle.coords[1] + self.height
                first_circle.coords = (first_circle.coords[0], new_y)
            drop.circles.append(first_circle)

    def print_model(self):
        print(self.drops)
