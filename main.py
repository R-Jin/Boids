import pygame as pg

from DotBoid import Boid
from Sim import Sim

flock = [];


def setup():
    for i in range(150):
        flock.append(Boid())

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.display.set_caption('Boids')

sim = Sim()

setup()

clock = pg.time.Clock()
while sim.run:
    clock.tick(60)
    sim.screen.fill((BLACK))

    for boid in flock:
        boid.draw(sim.screen, WHITE)

        cohesion = boid.cohesion(flock)
        separation = boid.seperation(flock)
        alignment = boid.alignment(flock)

        boid.velocity += cohesion + separation + alignment
        boid.update()

    events = pg.event.get()

    for event in events:
        sim.handle_events(event)

    pg.display.update()
