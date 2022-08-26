import pygame_widgets
import pygame as pg

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from DotBoid import Boid
from Sim import Sim

flock = [];


def setup():
    for i in range(100):
        flock.append(Boid())

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pg.display.set_caption('Boids')

sim = Sim()

# Sliders
slider = Slider(sim.screen, 100, 100, 800, 40, min=0, max=99, step=1, curved=False)
output = TextBox(sim.screen, 475, 200, 50, 50, fontSize=30)
output.disable()  # Act as label instead of textbox

setup()

# for boid in flock:
#     print(boid.pos)

clock = pg.time.Clock()
while sim.run:
    clock.tick(60)
    sim.screen.fill((BLACK))


    for boid in flock:
        boid.draw(sim.screen, WHITE)
        boid.cohesion(flock)
        boid.seperation(flock)
        boid.alignment(flock)
        boid.update()



    events = pg.event.get()

    output.setText(slider.getValue())
    pygame_widgets.update(events)

    for event in events:
        sim.handle_events(event)

    pg.display.update()
