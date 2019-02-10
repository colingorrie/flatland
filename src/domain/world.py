from domain.agent import Agent

import numpy as np


class World:
    def __init__(self, width, height):
        self.time = 0
        self.agents = []
        self.state = np.zeros((width, height), dtype=Agent)

    def add_agent(self, x, y):
        agent = Agent(x, y, energy=1)
        self.state[x][y] = agent
        self.agents.append(agent)

    def get_cell(self, x, y):
        return self.state[x][y]

    def step(self):
        self.time += 1
        for agent in list(self.agents):
            agent.decrement_energy()
            if agent.energy <= 0:
                # kill agent
                self.state[agent.x][agent.y] = None
                self.agents.remove(agent)
        # self.state = new_state
