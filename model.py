from collections import namedtuple


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
    def __init__(self, length, coords):
        self.circles = []
        for index in range(length):
            self.circles.append(Circle(40, 1, (coords[0], coords[1] + index)))

    def __repr__(self):
        return "Drop(circles: {})".format(self.circles)


class Model:
    def __init__(self):
        self.drops = []
        self.drops.append(Drop(3, (100, 100)))

    def update(self):
        for drop in self.drops:
            last_circle = drop.circles[-1]
            drop.circles = drop.circles[1:]
            last_radius = last_circle.radius
            last_coordinates = last_circle.coords
            first_circle = Circle(last_radius, 1, coords_sum(last_coordinates, (0, 1)))
            drop.circles.append(first_circle)

    def print_model(self):
        print(self.drops)