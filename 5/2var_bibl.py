import pygame
import numpy as np
from math import *

white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
orange = [255, 165, 0]
darkorange = [255, 140, 0]


WIDTH, HEIGHT = 700, 500
pygame.display.set_caption("3Д куб.")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(white)

scale = 150

circle_pos = [WIDTH / 1.5 , HEIGHT/ 1.5]  #

angle = 0

points = []

points.append(np.matrix([-0.5, -0.5, 0.5]))
points.append(np.matrix([0.5, -0.5, 0.5]))
points.append(np.matrix([0.5, 0.5, 0.5]))
points.append(np.matrix([-0.5, 0.5, 0.5]))
points.append(np.matrix([-0.5, -0.5, -0.5]))
points.append(np.matrix([0.5, -0.5, -0.5]))
points.append(np.matrix([0.5, 0.5, -0.5]))
points.append(np.matrix([-0.5, 0.5, -0.5]))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]


def connect_points(i, j, points):
    pygame.draw.line(
        screen, orange, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


clock = pygame.time.Clock()

while True:

    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])

    angle += 0.01

    screen.fill(white)

    i = 0
    # key = pygame.key.get_pressed()

    for point in points:
        rotated2d = np.dot(rotation_x, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_z, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]

        projected_points[i] = [x, y]
        pygame.draw.circle(screen, darkorange, (x, y), 5)
        i += 1

    for p in range(4):
        connect_points(p, (p + 1) % 4, projected_points)
        connect_points(p + 4, ((p + 1) % 4) + 4, projected_points)
        connect_points(p, (p + 4), projected_points)

    pygame.display.update()
