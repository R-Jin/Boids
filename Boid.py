class Boid:
    def __init__(self, starting_pos, starting_angle, scale):
        self.p1 = starting_pos
        self.p2 = (starting_pos[0] + 4 * scale, starting_pos[1] + 10 * scale)
        self.p3 = (starting_pos[0] - 4 * scale, starting_pos[1] + 10 * scale)
        self.pos = (self.p1, self.p2, self.p3)
