import pygame as pg
import math

class Boid:
    def __init__(self, starting_pos, angle=0, scale=20):
        # clean up unecessary stuff
        self.pos = starting_pos
        self.angle = angle
        self.scale = scale
        self.velocity = 0.2

    def rotate_points(self):
        points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
        rotated_points = [pg.math.Vector2(p).rotate(self.angle) for p in points]
        triangle_points = [(self.pos + p * self.scale) for p in rotated_points]
        return triangle_points

    def draw_boid(self, screen, color):
        pg.draw.polygon(screen, color, self.rotate_points(), width=1)

    def change_boid_dir(self, degree):
        self.angle += degree
        self.angle = self.angle % 360

    def move(self):
        (x, y) = self.pos
        rad = math.radians(self.angle)
        x += self.velocity * math.cos(rad)
        y += self.velocity * math.sin(rad)

        self.pos = (x, y)
