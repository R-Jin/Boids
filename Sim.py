import pygame as pg

class Sim:
    def __init__(self):
        (self.WIDTH, self.HEIGHT) = (1500, 1000)
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.run = True
        pg.init()

    def handle_events(self, event):
        match event.type:
            case pg.QUIT:
                self.run = False
            case _:
                return

    def handle_keys(self, boid):
        """Handle keyboad input"""

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            boid.change_boid_dir(-0.3)

        if keys[pg.K_RIGHT]:
            boid.change_boid_dir(0.3)
