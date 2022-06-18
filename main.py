import pygame as pg
from Boid import Boid
from Sim import Sim

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.display.set_caption('Boids')

sim = Sim()

test_boid = Boid((sim.WIDTH / 2, sim.HEIGHT / 2), 2, 6)

while sim.run:
    sim.screen.fill((BLACK))

    # our code
    test_boid.draw_boid(sim.screen, WHITE)
    test_boid.move()

    pg.display.update()

    sim.handle_keys(test_boid)
    for event in pg.event.get():
        sim.handle_events(event)