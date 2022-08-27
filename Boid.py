import pygame as pg
import math
import random

(S_WIDTH, S_HEIGHT) = (1500, 1000)

def get_random_normalized_vec():
    angle = random.uniform(0, 2 * math.pi)
    vector = pg.math.Vector2(math.cos(angle), math.sin(angle))
    return vector

class Boid:
    def __init__(self, size=10):
        self.pos = pg.math.Vector2(random.randint(0, S_WIDTH), random.randint(0, S_HEIGHT))
        self.angle = 10
        self.speed_limit = 4
        self.size = size
        self.velocity = get_random_normalized_vec()


    def rotate_points(self):
        points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
        rotated_points = [pg.math.Vector2(p).rotate(self.angle) for p in points]
        triangle_points = [(pg.math.Vector2(self.pos) + p * self.size) for p in rotated_points]
        return triangle_points

    def draw(self, screen, color):
        self.angle = math.degrees(math.atan2(self.velocity.y, self.velocity.x))
        pg.draw.polygon(screen, color, self.rotate_points(), width=1)

    def cohesion(self, flock):
        """Get the center of mass and steer towards it"""
        sum_of_pos = pg.math.Vector2()
        n = 0
        perception = 90                # Perception is 100px
        for boid in flock:
            if (not (self is boid) and perception >= self.pos.distance_to(boid.pos)):
                sum_of_pos += boid.pos
                n += 1

        if (n == 0):
            return pg.math.Vector2()

        center_mass = sum_of_pos / n

        factor = 1 / 200                # Percentage to move towards the center
        return (center_mass - self.pos) * factor

    def seperation(self, flock):
        """Make the boid move away from nearby boids"""
        vel = pg.math.Vector2()
        perception = 80
        for boid in flock:
            if (not (self is boid) and perception >= self.pos.distance_to(boid.pos)):
                vel -= (boid.pos - self.pos)

        factor = 1 / 900
        return (vel * factor)

    def alignment(self, flock):
        vel = pg.math.Vector2()
        n = 0
        perception = 80

        for boid in flock:
            if (not (self is boid) and perception >= self.pos.distance_to(boid.pos)):
                vel += boid.velocity
                n += 1

        if (n == 0):
            return pg.math.Vector2()

        avg_vel = vel / n

        factor = 20 / 100
        return (avg_vel - self.velocity) * factor

    def update(self):
        # Limit the velocity
        if (self.velocity.length() > self.speed_limit):
            self.velocity.scale_to_length(self.speed_limit)

        self.pos += self.velocity

        # Make the boids wrap around the screen
        if (self.pos.x < 0):
            self.pos.x += S_WIDTH
        elif (self.pos.x > S_WIDTH):
            self.pos.x -= S_WIDTH
        elif (self.pos.y < 0):
            self.pos.y += S_HEIGHT
        elif (self.pos.y > S_HEIGHT):
            self.pos.y -= S_HEIGHT
