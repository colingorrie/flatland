class Agent:
    def __init__(self, x, y, energy=10):
        self.x = x
        self.y = y
        self.energy = energy

    def decrement_energy(self):
        self.energy -= 1
