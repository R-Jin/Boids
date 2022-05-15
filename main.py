import pygame as pg
from Boid import Boid
pg.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

(WIDTH, HEIGHT) = (1920, 1080)

screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption('Boids')

run = True

test_boid = Boid((WIDTH / 2, HEIGHT / 2), 30, 10)

while run:
    screen.fill((BLACK))

    # our code
    pg.draw.polygon(screen, WHITE, test_boid.pos, width=2)

    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
