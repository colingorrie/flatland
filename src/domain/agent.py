class Agent:
    def __init__(self, x, y, energy=10):
        self.x = x
        self.y = y
        self.energy = energy

    def decrement_energy(self):
        self.energy -= 1

    def move(self, delta_x, delta_y, world):
        old_x = self.x
        old_y = self.y
        new_x = self.x + delta_x
        new_y = self.y + delta_y
        # Update position on the world.
        world.state[old_x][old_y] = None
        world.state[new_x][new_y] = self
        # Update position on the agent.
        self.x = new_x
        self.y = new_y
